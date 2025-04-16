import java.util.Scanner;
import java.util.Stack;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int[] A = new int[N];
		
		for (int i = 0; i < N; i++) {
			A[i] = sc.nextInt();
		}
		
		Stack<Integer> stack = new Stack<Integer>();
		StringBuffer bf = new StringBuffer();
		int num = 1;
		boolean result = true;
		
		for (int i = 0; i < A.length; i++) {
			int su = A[i];
			if (su >= num) {
				while (su >= num) {
					stack.push(num++);
					bf.append("+\n"); // push가 이뤄질 때 마다 + 를 bf 저장하고 한줄 띄운다.(\n)
				}
				stack.pop();
				bf.append("-\n"); // pop이 이뤄질 때 마다 - 를 bf 저장하고 한 줄 띄운다. (\n)
			} else {
				int p = stack.pop();
				
				if (p != su) {
					System.out.println("NO");
					result = false;
					break;
				} else {
					bf.append("-\n");
				}
			}
		}
		if (result) {
			System.out.println(bf.toString());
		}
		sc.close();
	}
}
