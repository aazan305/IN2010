import java.util.Scanner;
import java.util.PriorityQueue;

public class BalansertSokeTraer {
   public static void lageBST(int[] liste,int start, int slutt) {
        if (start>slutt) {
            return ;
        }
        int midten= (start+slutt)/2;
        
        System.out.println(liste[midten]);
        lageBST(liste,start,midten-1);
        lageBST(liste, midten+1, slutt);
        


    }
    public static void BSTHeap(PriorityQueue<Integer> heap){
        int[] liste = new int[heap.size()];
        int posisjon=0;
        while (heap.size()>0) {
            liste[posisjon]=heap.poll();
            posisjon++;
        }
        lageBST(liste, 0, liste.length-1);





    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        PriorityQueue<Integer> heap= new PriorityQueue<>();
        for (int i=0;i<input.length;i++) {
            heap.offer(Integer.parseInt(input[i]));
        }
        BSTHeap(heap);
        sc.close();
    }
    

    
}


