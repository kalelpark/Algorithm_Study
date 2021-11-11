package com.company;

import java.util.Scanner;

public class AnimalExample {
    public static void main(String[] args) {
	// write your code here
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] dp = new int[n+5];
        dp[0] = 0;
        dp[1] = 1;      // 후공이 이기는 경우
        dp[2] = 0;      // ㅓ선공이 이기는 경우
        dp[3] = 1;      //
        dp[4] = 0;

        // 선공이 가져가면 선공이 이기므로.....
        for (int i = 5; i<=n; i++) {
            // 이미 가져간 상태를 반대로 한 것이므로
            if (dp[i-1] != 0 || dp[i-3] != 0 || dp[i-4] != 0) {
                dp[i] = 0;
            } else {
                dp[i] = 1;
            }
        }
        System.out.print(dp[n] == 1 ? "CY" : "SK");
    }
}
