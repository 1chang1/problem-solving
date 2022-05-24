/*
* ACMICPC 1002
* 터렛
* Turret
*/

#include <stdio.h>
#include <cmath>

int main() {
	int n, x1, y1, r1, x2, y2, r2;
	scanf("%d", &n);
	
	for (int i=0 ; i<n ; i++) {
		scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
		int powDiffR = pow(r1 - r2, 2);
		int powD = pow(x1 - x2, 2) + pow(y1 - y2, 2);
		int powSumR = pow(r1 + r2, 2);
		
		if (powDiffR == 0 && powD == 0) printf("-1\n");
		else if (powDiffR < powD && powD < powSumR) printf("2\n");
		else if (powDiffR == powD || powD == powSumR) printf("1\n");
		else if (powSumR < powD || powD < powDiffR || powD == 0) printf("0\n");
	}
		
	return 0;
}