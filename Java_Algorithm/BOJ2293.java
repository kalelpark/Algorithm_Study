import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();        // 3
        int num2 = sc.nextInt();        // 10
        // 필요한 거 입력 넣기

        // dp 생성하기
        int[] dp = new int[num2+1];     // 배열 11까지 생성된다.

        dp[0] = 1;                      // 미리 초기화 시켜두기

        // 사용 가능한 동전
        int[] array = new int[num1];
        for (int i=0; i<num1; i++) {
            array[i] = sc.nextInt();
        }

        // 1, 2, 5
         {


        }
        for(int list : array) {
            for(int t=1; t<=num2; t++) {
                if (t - list >= 0) {
                    dp[t] += dp[t - list];
                }
            }
        }
        System.out.println(dp[num2]);

        // 처음 시도 부터 중복되는 것을 제외해야 함..
//      1 2 3 4 5 6 7 8 9 10
//  1   aΩ
//  2
//  5
//  0
    }
}
// 동전의 가장 작은 값보다는 낮은 동전은 표현이 불가능하다.

// 2 = 1 + 1
//