// Obviously tedious, solved with euler's r(r+1)/2
#include <cstdio>
#include <cmath>

using namespace std;

int main()
{
  int cases;
  long n;
  scanf("%d",&cases);
  while (cases--)
    {
      scanf("%ld",&n);
      // Remaining soldiers are considered outside of said rows
      printf("%ld\n", (long) ((sqrt(1+8*n)-1)/2));
    }
  
}
