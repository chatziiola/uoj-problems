// Implementation of python version There is something wrong with
// python and this site 100%
#include <cstdio>

int main()
{
  int n,c,p;
  int tmpPos;
  while(scanf("%d",&n) && n)
    {
      int StartingLineUp[1000] = {0};
      bool impossibol = false;

      for (int position = 0; position < n; position++)
	{
	  scanf("%d %d", &c,&p);
	  tmpPos = position + p;
	  if ((tmpPos > n-1) || (tmpPos < 0) || StartingLineUp[tmpPos])
	    {
	      impossibol = true;
	      continue;
	    }
	  StartingLineUp[tmpPos] = c;
	}

      if (impossibol)
	printf("-1\n");
      else
	{
	  for (int car = 0; car < n-1; car++)
	    printf("%d ", StartingLineUp[car]);
	  printf("%d\n", StartingLineUp[n-1]);
	}
	 
      
    }
  return 0;
  
}
