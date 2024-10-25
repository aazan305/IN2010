import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

class Movie{
    String id;
    String tittel;
    double rating; //bruker ikke
    
    public Movie(String id,String tittel, double rating){
        this.id=id;
        this.tittel=tittel;
        this.rating=rating;


    }
}
//klasse for skuespiller
class Actor{
    String id;
    String navn;
    List<String> filmIder;

    public Actor(String id,String navn, List<String> filmIder){
        this.id=id;
        this.navn=navn;
        this.filmIder=filmIder;
    }
}

public class Graf {
    public static void main(String[] args) {
        // filene som input
        if (args.length<2){
            System.err.println("du må gi 2 filene");

        }
        String movieFil= args[1];
        String actorFil=args[0];
        // lager en hashmap for filmer og skuespiller og en for grafen
        try{
            Map<String, Movie> movies= lesFilm(movieFil);
            Map<String, Actor> actors= lesActors(actorFil,movies);
            Map<String, List<String>> graf= lageGraf(actors, movies);
            


            // Her kan du legge til kode for å teste grafen din, kjøre algoritmer, etc.
            //System.out.println("Graf bygging fullført!");
            // For eksempel kan du skrive ut en del av grafen for å teste
            //for (String actorId : graph.keySet()) {
                //System.out.println("Actor: " + actorId + " med linker: " + graph.get(actorId));
            //}

            grafInfo(graf);

        } catch (IOException e) {
            System.err.println("Feil ved lesing av filer: " + e.getMessage());
            e.printStackTrace();
            System.exit(1);
        }

    }
    private static Map<String,Movie> lesFilm(String movieFil) throws IOException {
        Map<String,Movie> movies=new HashMap<>();

        BufferedReader br= new BufferedReader(new FileReader(movieFil));
        String linje;
        while((linje=br.readLine()) !=null){
            String[] felt= linje.split("\t");
            String id= felt[0];
            String tittel= felt[1];
            double rating= Double.parseDouble(felt[2]);
            movies.put(id, new Movie(id,tittel,rating));
        }
        br.close();
        return movies;


    }
    private static Map<String, Actor> lesActors(String actorFil, Map<String, Movie> movies) throws IOException {
        Map<String, Actor> actors = new HashMap<>();

        BufferedReader br = new BufferedReader(new FileReader(actorFil));
        String linje;
        while ((linje = br.readLine()) != null) {
            String[] felt = linje.split("\t");
            String id = felt[0];
            String name = felt[1];
            List<String> movieIds = new ArrayList<>();
            for (int i = 2; i < felt.length; i++) {
                if (movies.containsKey(felt[i])) {
                    movieIds.add(felt[i]);
                }
            }
            actors.put(id, new Actor(id, name, movieIds));
        }
        br.close();
        return actors;
    }
    private static Map<String, List<String>> lageGraf(Map<String,Actor> actors,Map<String, Movie> movies){
        Map<String, List<String>> graf= new HashMap<>();
        for(Actor actor : actors.values()){

            graf.putIfAbsent(actor.id, new ArrayList<>());
            for (String filmId : actor.filmIder){
                for(Actor otherActor : actors.values()){
                    if(!otherActor.id.equals(actor.id) && otherActor.filmIder.contains(filmId)){
                        graf.get(actor.id).add(otherActor.id);
                    }
                }

            }
        } 
       return graf; 
    }
    private static void grafInfo(Map<String,List<String>> graf){
        int noder= graf.keySet().size();
        int kanter= 0;
        int count=0;
        for(List<String> kanteList :graf.values()){
            count+=1;
            System.out.println(count);
            kanter += kanteList.size();
        }
        System.out.println("Oppgave 1");
        System.out.println("Nodes: " + noder);
        System.out.println("Edges: " + kanter);
    }

}