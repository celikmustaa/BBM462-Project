import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        ReadFile reader = new ReadFile();
        Graph graph = reader.createGraph();

        CountMotifs count = new CountMotifs(graph);


        int[] k_sets = {100, 200, 500, 1000, 3000, 10000, 100000, 1000000};

        for(int k: k_sets){
            double[] estimated = count.three_path_sampler(k);
            for(double i: estimated){
                System.out.printf("%8d ", (int) i);
            }
            System.out.println(" estimated for k = " + k);

            estimated = count.centered_sampler(k);
            for(double i: estimated){
                System.out.printf("%8d ", (int) i);
            }
            System.out.println(" centered  for k = " + k);
        }

        System.out.println("10573946  8357359  3207969   298698   414582    65442  Actual");

        /*
        int[] actual = count.brute_force_count();
        for(int i: actual){
            System.out.printf("%8d ", i);
        }
        System.out.println("  Actual");
        */

    }

}
