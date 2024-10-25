class Node{
    int nokkel;
    int hoyde;
    Node left, right;
    public Node(int item){
        nokkel=item;
        hoyde=1;
        left=null;
        right=null;
        
    }
}
class SetAVL {
    private Node root;
    private int storrelse;
    public SetAVL(){
        root=null;
        storrelse=0;

    }
    public int hoyde(Node root){
        if ( root==null) {
            return 0;
        }
        else{
            return root.hoyde;
        }
    }
    private int setHoyde(Node root){
        return root.hoyde=Math.max(hoyde(root.left), hoyde(root.right)) + 1;
    }
    public boolean contains(int nokkel){
        return contains(root,nokkel);
    }
    private boolean contains(Node root, int nokkel){
        if (root== null){
            return false;
        }
        if(root.nokkel== nokkel){
            return true;
        }
        if (nokkel<root.nokkel){
            return contains(root.left,nokkel);
        }
        if (nokkel>root.nokkel){
            return contains(root.right,nokkel);
        }
        else{
            return false;
        }
    }
   
    public void insert(int nokkel){
        if(!contains(nokkel)){
        root=insert(root,nokkel);
        storrelse++;}


    }
    private Node insert (Node root, int nokkel){
        if (root==null){
            root= new Node(nokkel);
        }
        if (nokkel< root.nokkel){
            root.left=insert(root.left,nokkel);
        }
        else if(nokkel> root.nokkel){
            root.right=insert(root.right,nokkel);
        }
        
        setHoyde(root);
        return balanse(root);
    }
    public int minsteVerdi(Node root){
        int minsteVerdi= root.nokkel;
        while(root.left!=null){
            minsteVerdi=root.left.nokkel;
            root=root.left;
        }
        return minsteVerdi;


    }
    public void remove (int nokkel){
        if (contains(nokkel)){
        root=remove(root,nokkel);
        storrelse--;}

    }
    private Node remove(Node root,int nokkel){
        if (root==null){
            return null;
        }
        if(nokkel< root.nokkel){
            root.left=remove(root,nokkel);

        }
        if (nokkel> root.nokkel){
            root.right=remove(root,nokkel);
        }
        if(root.left==null){
            return root.right;
        }
        if(root.right==null){
            return root.left;
        }
        root.nokkel=minsteVerdi(root.right);
        root.right=remove(root.right,root.nokkel);
        
        setHoyde(root);
        return balanse(root);
    }
    public int balanseFaktor(Node root){
        if (root==null) {
            return 0;
        }
        else{
            return hoyde(root.left)-hoyde(root.right);
        }
    }
    public Node balanse(Node root){
        if(balanseFaktor(root)<1){
            if (balanseFaktor(root.right)>0) {
                root.right=rightRotate(root.right);
                return leftRotate(root.left);
                
            }
        }
        if(balanseFaktor(root)>1){
            if (balanseFaktor(root.left)<0) {
                root.left=leftRotate(root.left);
                return rightRotate(root.right);
                
            }
        }
        return root;
    }
    private Node leftRotate(Node root){
        Node y = root.right;
        Node T1 = y.left; 
        y.left = root;
        root.right = T1;
        setHoyde(root); 
        setHoyde(y);    
        return y;
    }
    private Node rightRotate(Node root){
        Node y = root.left;
        Node T1 = y.right; 
        y.right = root;
        root.left = T1;
        setHoyde(root); 
        setHoyde(y);    
        return y;
    }
   
   
    public int size(){
        return storrelse;
    }
   
    
}

