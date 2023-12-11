public class Main {
    public static void main(String[] args) {
        int num1 = 1000, num5 = 1000, num10 = 1000, num20 = 1000, num50 = 1000, num100 = 1000;
        int total = num1 + num5 * 5 + num10 * 10 + num20 * 20 + num50 * 50 + num100 * 100;
        int ways = 0;
        for (int i = 0; i <= num100; i++) {
            for (int j = 0; j <= num50; j++) {
                for (int k = 0; k <= num20; k++) {
                    for (int l = 0; l <= num10; l++) {
                        for (int m = 0; m <= num5; m++) {
                            for (int n = 0; n <= num1; n++) {
                                if (i * 100 + j * 50 + k * 20 + l * 10 + m * 5 + n == 500) {
                                    ways++;
                                }
                            }
                        }
                    }
                }
            }
        }
        System.out.println("共有" + ways + "种支付方式");
    }
}
