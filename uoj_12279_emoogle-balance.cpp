#include <cstdio>

int main()
{
  int n, tmp;
  int cases = 1;
  int answ;
  while (scanf("%d",&n) and n)
    {
      answ = 0;
      while (n--)
	{
	  scanf("%d",&tmp);
	  if ( tmp > 0 )
	    answ++;
	  else
	    answ--;
	}
      printf("Case %d: %d\n", cases++, answ);
    }
}
