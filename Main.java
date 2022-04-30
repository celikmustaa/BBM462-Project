import java.io.IOException;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {

        ReadFile reader = new ReadFile();
        Graph graph = reader.createGraph();

        HashMap<Integer, Integer> degree_map = KeyProperties.degreeDistribution(graph);
        System.out.print("Degree Distribution:\n{");
        for(int key: degree_map.keySet()){
            System.out.printf("'%d':%.4f, ",key, (float)degree_map.get(key)/(graph.map.size()-1));
        }
        System.out.println("}\n");

//        System.out.println("Degree Distribution: " + KeyProperties.degreeDistribution(graph));
//        System.out.println("Average Path Length: " + KeyProperties.averagePathLength(graph));
//        System.out.println("Diameter:" + KeyProperties.diameter);
//        System.out.println("Average Clustering Coefficient: " + KeyProperties.averageClusteringCoefficient(graph));
//        System.out.println("Size of Component: " + KeyProperties.sizeOfComponent(graph));
    }

}
