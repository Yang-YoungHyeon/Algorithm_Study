/**
 * 00:00:00 ~ N:59:59 ���� K�� ���Ե� �ð��� ���� ���ϱ�
 * 0 <= N <= 23
 * 0 <= K <= 9
 * ex) N=5, K=3 �϶�
 * ���� -> 05:02:53
 * ������ -> 04:02:01
 * 
 * �Է¿���1) 5 3 
 * ��¿���1) 11475
 * 
 * �Է¿���2) 22 7
 * ��¿���2) 21564
 * */
public class Fastcampus_Solution {
	public static void main(String[] z) {
		int N = 22;
		int K = 7;
		
		solution(N,K);
	}
	
	public static void solution(int N, int K) {
		int hour=0,min=0,second=0;
		int count = 0;
		for(int i=0; i<3600*(N+1);i++) {
			String str = String.format("%02d", hour)+":"+String.format("%02d", min)+":"+String.format("%02d", second);
			if(str.contains(K+"")==true) {
				count++;
			}
			second++;
			if(second == 60) {
				second = 0;
				min++;
			}
			
			if(min == 60) {
				min = 0;
				hour++;
			}
		}
		System.out.println("[00:00:00 ~ "+String.format("%02d", N)+":59:59] ���� ["+K+"]��(��) ���Ե� ���� :"+count);
	}
}
