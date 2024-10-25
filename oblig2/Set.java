class Node{
    int nokkel;
    Node left, right;
    public Node(int item){
        nokkel=item;
        left=null;
        right=null;
        
    }
}
class Set {
    private Node root;
    private int storrelse;
    public Set(){
        root=null;
        storrelse=0;

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
        return root;
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
        return root;
    }
    public int size(){
        return storrelse;
    }
    
}

