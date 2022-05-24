/*
* ACMICPC 13900
* 순서쌍의 곱의 합
* Sum of Products of Pairs
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
	int n;
	long sum = 0;
	scanf("%d", &n);
	
	int *numbers = new int[n];
	
	for (int i=0 ; i<n ; i++) {
		scanf("%d", numbers+i);
		if (numbers[i] == 0) {
			n--;
			i--;
		}
	}
	
	long partSum = 0;
	for (int i=0 ; i<n-1 ; i++) {
		partSum += numbers[i];
		sum += partSum * numbers[i+1];
	}
	
	printf("%ld\n", sum);
	
	delete [] numbers;
	
	return 0;
}