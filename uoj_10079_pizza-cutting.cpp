#include <cstdio>

int main() {
    while (true) {
        long long n = 0;
        scanf("%lld", &n) ;

        if (n < 0) 
            break;

        printf("%lld\n", 1 + n * (n + 1) / 2);
    }

    return 0;
}
