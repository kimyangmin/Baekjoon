import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		
		String[] c = {"C", "A", "M", "B", "R", "I", "D", "G", "E"};
		
		for (String ca : c) {
			s = s.replaceAll(ca, "");
		}
		
		System.out.println(s);
		sc.close();
	}
}
