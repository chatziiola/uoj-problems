#include <cstdio>
#include <iostream>
#include <set>
#include <queue>
#include <utility>
// #include <pair>

using namespace std;

int grid[100][100];

int main() {
  int even = 0;
  int odd = 0;

  int cases,r,c,m,n,w;
  int tmpRow, tmpCol;

  scanf("%d",&cases);
  cases++;
  for (int i = 1; i<cases; i++)
    {
      even = 0;
      odd = 0;

      scanf("%d %d %d %d",&r,&c,&m,&n);
      scanf("%d",&w);

      for (int row=0; row<r; row++)
	for (int col=0; col<c; col++)
	  grid[row][col]=-1;

      while(w--)
	{
	scanf("%d %d",&tmpRow,&tmpCol);
	grid[tmpRow][tmpCol] = -2; //water code
	}

      // End of input for the case
      int checkRow[] = {m,m,-m,-m,n,n,-n,-n};
      int checkCol[] = {n,-n,n,-n,m,-m,m,-m};

      queue<pair<int, int> >  myQ;
      myQ.push(make_pair(0,0));

      pair <int,int> currentSquare;
      grid[0][0]++;
      
      while (not myQ.empty())
	{
	  currentSquare = myQ.front();
	  myQ.pop();
	  set<pair <int,int> > checkedSquares;

	  for (int l=0; l<8; l++)
	    {
	      tmpRow = currentSquare.first + checkRow[l];
	      tmpCol = currentSquare.second + checkCol[l];
	      
	      // Starting to think this is the problem
	      if (checkedSquares.find(make_pair(tmpRow, tmpCol))
		  != checkedSquares.end())
		continue;
	      checkedSquares.insert(make_pair(tmpRow,tmpCol));

	      if ((tmpRow > -1) && (tmpRow < r) &&
		  (tmpCol > -1) && (tmpCol < c) &&
		  (grid[tmpRow][tmpCol] != -2))
		{
		  grid[tmpRow][tmpCol] += 1;
		  if (grid[tmpRow][tmpCol] == 0)
		    myQ.push(make_pair(tmpRow, tmpCol));
		}
	    }
	}

      grid[0][0]--;
      for (int row=0; row<r; row++)
	for (int col=0;col<c;col++)
	  if (grid[row][col] > -1) //visited
	    {
	      if (grid[row][col] % 2 == 0)
		odd++;
	      else
		even++;
	    }

      if (odd == even && even == 0)
	even++;

      printf("Case %d: %d %d\n",i,even,odd);
    }
  return 0;
}
