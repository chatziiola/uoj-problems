// Nice: TTL :P

// After first reading it: I can use BFS on every query. I just think
// that this might have too many instances of BFS for one /case/

#include <algorithm>
#include <cstdio>
#include <map>
#include <queue>
#include <vector>

using namespace std;

int main() {
  int nc;
  int a, b;
  int nodes;
  int cases = 1;

  while (scanf("%d", &nc) and nc) {
    // Parse the topology input
    vector<int> adjList[31];
    map<int, int> myMap;

    nodes = 1;

    for (int i = 0; i < nc; i++) {
      scanf("%d %d", &a, &b);
      if (myMap.find(a) == myMap.end())
	myMap.insert(make_pair(a, nodes++));
      if (myMap.find(b) == myMap.end())
	myMap.insert(make_pair(b, nodes++));
      adjList[myMap[a]].push_back(myMap[b]);
      adjList[myMap[b]].push_back(myMap[a]);
    }

    // // // For every subcase:
    while (scanf("%d %d", &a, &b) and (a or b)) {
      queue<int> myQ;

      bool visited[31] = { false };
      int parent[31] = { -1 };
      int distance[31] = { 0 };

      myQ.push(myMap[a]);
      visited[myMap[a]] = true;
      parent[myMap[a]] = -1;
      nodes = myMap.size();

      int tmpNode;

      while (not myQ.empty()) {
	tmpNode = myQ.front();
	myQ.pop();

	// ugly but worked and didn't have to change
	if (parent[tmpNode] == -1)
	    distance[tmpNode] = 0;
	else
	    distance[tmpNode] = distance[parent[tmpNode]] + 1;
	if (distance[tmpNode] > b)
	  break;

	nodes--;
	for (int i = 0; i < adjList[tmpNode].size(); i++) {
	  if (not visited[adjList[tmpNode][i]]) {
	    parent[adjList[tmpNode][i]] = tmpNode;
	    visited[adjList[tmpNode][i]] = true;
	    myQ.push(adjList[tmpNode][i]);
	  }
	}


      }

      // A = starting node, B = ttl
      printf("Case %d: %d nodes not reachable from node %d with TTL = %d.\n",
	     cases++, nodes, a, b);
    }
  }
}
