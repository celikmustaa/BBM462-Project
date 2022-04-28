import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {

        ReadFile reader = new ReadFile();
        Graph graph = reader.createGraph();

        System.out.println(KeyProperties.degreeDistribution(graph));
        System.out.println(KeyProperties.averagePathLength(graph));
        System.out.println(KeyProperties.diameter);
        //System.out.println(KeyProperties.averageClusteringCoefficient(graph));
        System.out.println(KeyProperties.sizeOfComponent(graph));
    }

}
