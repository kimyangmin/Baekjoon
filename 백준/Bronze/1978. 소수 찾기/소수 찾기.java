import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int prime_cnt = 0;

        for (int i = 0; i < n; i++) {
            if (is_Prime(sc.nextInt())) prime_cnt++;
        }
        System.out.println(prime_cnt);
    }
    
    public static boolean is_Prime(int number) {
        if (number == 1) return false;


        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) return false;
        }

        return true;
    }

}