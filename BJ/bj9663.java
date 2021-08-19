package com.ssafy.algo;

import java.util.Scanner;

public class BJ9663 {
	static int N, cnt;
	static int[] col;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		col = new int[N + 1];

		cnt = 0;
		setQueens(1);
		System.out.println(cnt);
	}

	private static void setQueens(int rowNo) {
		if(rowNo > N) {
			cnt++;
			return;
		}


		for(int i = 1; i <= N; i++) {
			col[rowNo] = i;
			if(isAvailable(rowNo)) {
				setQueens(rowNo + 1);
			}
		}
	}

	private static boolean isAvailable(int rowNo) {
		for(int r = 1; r < rowNo; r++) {
			if(col[r] == col[rowNo] || Math.abs(col[rowNo] - col[r]) == (rowNo  - r)) return false;
		}
		return true;
	}
}
