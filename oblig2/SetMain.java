import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class SetMain {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("sett inputfil");
            return;
        }
        
        Scanner sc;
        try {
            sc = new Scanner(new File(args[0]));
        } catch (FileNotFoundException e) {
            System.out.println("fant ikke fil" + args[0]);
            return;
        }

        Set set = new Set();
        if (sc.hasNextInt()) {
            int neste = sc.nextInt();
            sc.nextLine();
            

            for (int i = 0; i < neste; i++) {
                String operasjon = sc.next();
                
                if (operasjon.equals("contains")) {
                    int x = sc.nextInt();
                    System.out.println(set.contains(x));
                } else if (operasjon.equals("insert")) {
                    int x = sc.nextInt();
                    set.insert(x);
                    
                } else if (operasjon.equals("remove")) {
                    int x = sc.nextInt();
                    set.remove(x);
                } else if (operasjon.equals("size")) {
                    System.out.println(set.size());
                }
                sc.nextLine();
            }
        } else {
            System.out.println("feil");
            
        }

        sc.close();
    }
}
