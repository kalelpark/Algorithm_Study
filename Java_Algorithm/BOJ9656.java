import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // write your code here
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] dp = new int[n+5];
        dp[0] = 0;
        dp[1] = 0;
        dp[2] = 1;
        dp[3] = 0;

        for (int i = 4; i<=n; i++) {
            if (dp[i-1] == 0 || dp[i-3] == 0) {
                dp[i] = 1;
            } else {
                dp[i] = 0;
            }
        }
        if (dp[n] == 1) {
            System.out.print("SK");
        } else {
            System.out.print("CY");
        }
    }
}