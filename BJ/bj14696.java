package com.ssafy.algo;

import java.util.Scanner;

public class BJ14696 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		for(int i = 0; i < N; i++) {
			int a = sc.nextInt();
			
			int[] aScore = new int[4 + 1];
			for(int j = 0; j < a; j++) {
				aScore[sc.nextInt()]++;
			}
			
			int b = sc.nextInt();
			int[] bScore = new int[4 + 1];
			for(int j = 0; j < b; j++) {
				bScore[sc.nextInt()]++;
			}
			
			char winner = 'D';
			for(int k = 4; k > 0; k--) {
				if(aScore[k] > bScore[k]) {
					winner = 'A';
					break;
				} else if(aScore[k] < bScore[k]) {
					winner = 'B';
					break;
				}
			}
			System.out.println(winner);
		}
	}
}
