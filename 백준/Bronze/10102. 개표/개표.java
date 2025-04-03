import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int V = sc.nextInt();
		int cntA = 0;
		int cntB = 0;
		
		String S = sc.next();
		
		for (int i = 0; i < V; i++) {
			if (S.charAt(i) == 'A') {
				cntA++;
			} else {
				cntB++;
			}
		}
		if (cntA > cntB) {
			System.out.println('A');
		} else if (cntB > cntA) {
			System.out.println('B');
		} else {
			System.out.println("Tie");
		}
	}
}
