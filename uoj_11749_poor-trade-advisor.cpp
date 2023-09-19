// 230907: Rewriting this from python
#include <cstdio>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

struct City {
  bool visited = false;
  vector<pair<int, int> > adjacencyList;
};

int main() {

  while (true) {
    int n, m;
    scanf("%d %d", &n, &m);

    if (n == 0 && m == 0)
      break;

    vector<City> citiesArray(n + 1);

    int myPPA = 1 << 31;
    int start, end, PPA;

    for (int i = 0; i < m; i++) {
      scanf("%d %d %d", &start, &end, &PPA);
      myPPA = max(PPA, myPPA);
      citiesArray[start].adjacencyList.push_back(make_pair(end, PPA));
      citiesArray[end].adjacencyList.push_back(make_pair(start, PPA));
    }

    stack<int> myStack;
    int currentProvinceSize;
    int myCities = 2;
    int city;

    for (int anycity = 1; anycity <= n; anycity++) {
      if (citiesArray[anycity].visited)
	continue;

      myStack.push(anycity);
      currentProvinceSize = 0;

      while (not myStack.empty()) {
	city = myStack.top();
	myStack.pop();
	if (citiesArray[city].visited)
	  continue;

	currentProvinceSize++;

	for (int currIndex = 0;
	     currIndex < citiesArray[city].adjacencyList.size(); currIndex++) {
	  if (citiesArray[city].adjacencyList[currIndex].second == myPPA &&
	      not citiesArray[citiesArray[city].adjacencyList[currIndex].first]
		      .visited)
	    myStack.push(citiesArray[city].adjacencyList[currIndex].first);
	}

	citiesArray[city].visited = true;
      }
      myCities = max(myCities, currentProvinceSize);
    }
    printf("%d\n", myCities);
  }

  return 0;
}
