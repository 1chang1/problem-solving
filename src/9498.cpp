/*
* ACMICPC 9498
* 시험 성적
* Test Score
*/

#include <stdio.h>

int main() {
	int score;
	scanf("%d", &score);
	char grade[11] = {'F','F','F','F','F','F','D','C','B','A','A'};
	printf("%c", grade[score/10]);
	
	return 0;
}