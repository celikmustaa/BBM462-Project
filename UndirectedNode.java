import java.util.*;

public class UndirectedNode implements Comparable<UndirectedNode>{
    public int id;
    public int value; // not important for that graph
    public int degree;
    public ArrayList<Integer> adjacency_list;

    //Constructors
    public UndirectedNode(int id){
        this.id = id;
        this.value = 0;
        this.degree = 0;
        this.adjacency_list = new ArrayList<Integer>();
    }

    public UndirectedNode(int id, int value){
        this.id = id;
        this.value = value;
        this.degree = 0;
        this.adjacency_list = new ArrayList<Integer>();
    }


    // doesn't mean anything because adjacency list holds ids, not nodes
    @Override
    public int compareTo(UndirectedNode other) {
        if (this.degree > other.degree) {
            return 1;
        }
        return this.id < other.id ? -1 : 1;
    }



}
