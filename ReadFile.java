import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class ReadFile {
    public static String line = "";
    public static String file_location = "C:\\Users\\musta\\Desktop\\Hacettepe\\DREAM\\twitch_gamers\\large_twitch_edges.csv";
    //public static String file_location = "C:\\Users\\musta\\Desktop\\Hacettepe\\DREAM\\lasftm_asia\\lastfm_asia_target.csv";
    public static ArrayList<String> lines = new ArrayList<String>();

    public ReadFile() throws IOException {
        BufferedReader br = new BufferedReader((new FileReader(file_location)));

        while ((line = br.readLine()) != null){
            lines.add(line);
        }
    }

    public Graph createGraph(){
        Graph graph = new Graph();

        for (String line: lines) {
            String[] splitted = line.split(",");

            for(int i=0; i<2; i++){
                if (!graph.map.containsKey(Integer.parseInt(splitted[i]))){
                    UndirectedNode node = new UndirectedNode(Integer.parseInt(splitted[i]));
                    graph.map.put(node.id, node);
                }
            }

            graph.connect(Integer.parseInt(splitted[0]), Integer.parseInt(splitted[1]));

        }

        // sort the adjacency lists of graphs
        for(int id: graph.map.keySet()){
            Collections.sort(graph.map.get(id).adjacency_list, (node1_id, node2_id) -> {
                if (graph.map.get(node1_id).degree > graph.map.get(node2_id).degree) {
                    return 1;
                }
                if (graph.map.get(node1_id).degree == graph.map.get(node2_id).degree){
                    return graph.map.get(node1_id).id < graph.map.get(node2_id).id ? -1 : 1;
                }
               return -1;
            });
        }

        return graph;
    }
}
