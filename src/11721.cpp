/*
* ACMICPC 11721
* 열 개씩 끊어 출력하기
* Print 10 Characters Per Line
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
	char input[100];
	scanf("%s", input);
	
	for (int i=1 ; i<=100, input[i-1] != '\0' ; i++) {
		printf("%c", input[i-1]);
		if (i % 10 == 0) printf("\n");
	}
	
	return 0;
}