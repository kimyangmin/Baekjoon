
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for (int i = 0; i <= N; i++) {
            if (N-i != N) {
                for (int j = N - i; j > 0; j--) {
                    System.out.print(" ");
                }

                for (int j = 0; j < (2 * i) - 1; j++) {
                    System.out.print("*");
                }
                System.out.println();
            }
        }

        for (int i = N-1; i > 0; i--) {
            for (int j = 1; j < (N - i) + 1; j++) {
                System.out.print(" ");
            }

            for (int j = 0; j < (i * 2) - 1; j++) {
                System.out.print("*");
            }
            if (i != 1) {
                System.out.println();
            }
        }
    }
}
