#include <cstdio>
#include <vector>

std::vector<int> lessthanhundred(101, 0);

int fninetyone(int n) {
    if (n > 100) {
        return n - 10;
    } else {
        if (lessthanhundred[n] == 0) {
            lessthanhundred[n] = fninetyone(fninetyone(n + 11));
        }
        return lessthanhundred[n];
    }
}

int main() {
    int n;
    scanf("%d", &n);

    while (n != 0) {
        if (n > 100) {
	  printf("f91(%d) = %d\n", n, n - 10 );
        } else {
            if (lessthanhundred[n] == 0) {
                fninetyone(n);
            }
	    printf("f91(%d) = %d\n", n, lessthanhundred[n]);
        }
	scanf("%d", &n);
    }

    return 0;
}
