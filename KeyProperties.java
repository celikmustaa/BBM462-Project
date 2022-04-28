import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;

public class KeyProperties {
    public static int diameter = 0;

    public static HashMap<Integer, Integer> degreeDistribution(Graph graph){
        HashMap<Integer, Integer> degree_counts = new HashMap<>();  // key=degree value=count

        for(int node_id: graph.map.keySet()){
            UndirectedNode node = graph.map.get(node_id);
            if(degree_counts.containsKey(node.degree)){
                degree_counts.put(node.degree, degree_counts.get(node.degree) + 1);
            }
            else{
                degree_counts.put(node.degree, 1);
            }
        }
        return degree_counts;
    }

    public static double averagePathLength(Graph graph){
        int N = graph.map.size();
        long sum_of_shortest_paths = 0;

        int counter = 0;
        for(int node_id: graph.map.keySet()){
            LinkedList<Integer> extend = new LinkedList<>();
            LinkedList<Integer> temp = new LinkedList<>();
            extend.add(node_id);

            HashMap<Integer, Integer> path_lengths = new HashMap<>(); // node_id: path_length
            path_lengths.put(node_id, 0);

            int current_length = 0;
            while(extend.size() > 0){
                UndirectedNode node = graph.map.get(extend.removeFirst());
                for(int neighbour: node.adjacency_list){
                    if(!path_lengths.containsKey(neighbour) ){
                        counter += 1;
                        path_lengths.put(neighbour, current_length + 1);
                        sum_of_shortest_paths += path_lengths.get(neighbour);
                        temp.add(neighbour);

                        if(path_lengths.get(neighbour) > diameter){
                            diameter = path_lengths.get(neighbour);
                        }
                    }
                }

                if(extend.size() == 0){ // copy tem to extend and delete the content of temp
                    extend = temp;
                    temp = new LinkedList<>();
                    current_length += 1;
                }
            }

            System.out.println("Number of neighbour of node "+ node_id+" is: "+ path_lengths.size());
        }

        sum_of_shortest_paths /= 2; // because we counted both i-j and j-i

        System.out.println("N is: "+N+"\nN*(N-1)/2 is :"+N*(N-1)/2+"\nNumber of pairs is: "+ counter );
        return (double)sum_of_shortest_paths / ((double) N*(N-1)/2);
    }


    public static double averageClusteringCoefficient(Graph graph){
        double sum_of_clustering_coefficients = 0;

        int counter = 0;
        for(int node_id: graph.map.keySet()){
            UndirectedNode node = graph.map.get(node_id);
            if(node.degree > 1){
                counter += 1;

                double clustering_coefficient = 0;

                for(int i=0; i<node.degree - 1; i++){
                    for(int j=i+1; j<node.degree; j++){
                        if(graph.map.get(node.adjacency_list.get(i)).adjacency_list.contains(node.adjacency_list.get(j))){
                            clustering_coefficient += 1;
                        }
                    }
                }

                clustering_coefficient /= (double) node.degree * (node.degree - 1) / 2;
                sum_of_clustering_coefficients += clustering_coefficient;
            }

        }

        return sum_of_clustering_coefficients / counter;
    }

    public static int numberOfComponents(Graph graph){
        int number_of_components = 0;

        return number_of_components;
    }

    public static int sizeOfComponent(Graph graph){
        return graph.map.size();
    }


} // class
