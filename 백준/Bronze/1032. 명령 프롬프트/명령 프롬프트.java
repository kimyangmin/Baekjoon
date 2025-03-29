import java.util.Scanner;
import java.lang.StringBuilder;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        StringBuilder sb = new StringBuilder(sc.nextLine());
        StringBuilder result = new StringBuilder(sb);
        for (int i = 1; i < N; i++) {
            StringBuilder sb2 = new StringBuilder(sc.nextLine());

            for (int j = 0; j < sb2.length(); j++) {
                char index1 = sb.charAt(j);
                char index2 = sb2.charAt(j);

                if (index1 != index2) {
                    result.setCharAt(j, '?');
                }
            }
        }
        System.out.println(result);
    }
}
