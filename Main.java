import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {

        ReadFile reader = new ReadFile();
        Graph graph = reader.createGraph();

        System.out.println("Degree Distribution: " + KeyProperties.degreeDistribution(graph));
        System.out.println("Average Path Length: " + KeyProperties.averagePathLength(graph));
        System.out.println("Diameter:" + KeyProperties.diameter);
        System.out.println("Average Clustering Coefficient: " + KeyProperties.averageClusteringCoefficient(graph));
        System.out.println("Size of Component: " + KeyProperties.sizeOfComponent(graph));
    }

}
