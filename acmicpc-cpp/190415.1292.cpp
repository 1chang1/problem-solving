/*
* ACMICPC 1292
* 쉽게 푸는 문제
* Easy Question
*/

#include <stdio.h>

int main() {
	int a, b, sum = 0;
	scanf("%d %d", &a, &b);
	
	int prev = 1;
	for (int i=a ; i<=b ; i++) {
		int j;
		for (j=prev ; j<i ; j++) {
			if (j*(j+1)/2 >= i) {
				break;
			}
		}
		sum += j;
		prev = j;
	}
	
	printf("%d", sum);
	
	return 0;
}