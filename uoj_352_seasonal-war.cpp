#include <cstdio>
#include <queue>
#include <utility>

using namespace std;

int k, eaglesCounter;
char matrix[25][25];
pair<int, int> cords;


int main() {
  int cases = 1;
  while (scanf("%d", &k) != EOF) {
    for (int line = 0; line < k; line++)
      scanf("%s", matrix[line]);

    eaglesCounter = 0;
    queue<pair<int, int> > myQ;

    for (int line = 0; line < k; line++) {
      for (int index = 0; index < k; index++)
	if (matrix[line][index] == '1') {
	  eaglesCounter++;
	  myQ.push(make_pair(line, index));

	  while (not myQ.empty()) {
	    cords = myQ.front();
	    matrix[cords.first][cords.second] = '0';
	    myQ.pop();

	    for (int i = -1; i < 2; i++)
	      for (int l = -1; l < 2; l++) {
		if (((cords.first+i > k) or (cords.first+i<0)) or ((cords.second+l > k) or (cords.second+l<0)))
		  continue;
		if (matrix[cords.first+i][cords.second+l] == '1') 
		  myQ.push(make_pair(cords.first+i,cords.second+ l));
	      }
	  }
        }
    }
      printf("Image number %d contains %d war eagles.\n", cases++,
	     eaglesCounter);
  }
}
