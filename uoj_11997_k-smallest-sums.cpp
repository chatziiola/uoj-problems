#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

struct posINT
{
  int val;
  int pos;

  posINT(int a, int b)
  {
    val = a;
    pos = b;
  }

  bool operator < (const posINT &B) const
  {
    return val > B.val;
  }
  
};
// We are asked to find the k smallest sums using an item of each
// array of length K

int main() {
  int k;
  int out[800];
  int lin[800];

  while (scanf("%d",&k) != EOF) {
    // First line is written in out to save on memory and then every
    // subsequent line will be written on lin, since it is only used
    // once.
    for (int entry = 0; entry < k; entry ++)
      scanf("%d", &out[entry]);
    sort(out, out+k);

    // For every subsequent line of input:
    for (int line = 1; line < k; line++) 
      {
      for (int entry = 0; entry < k; entry ++)
	scanf("%d", &lin[entry]);
      sort(lin, lin+k);
    
      // It is only logical to keep the K lowest sums on a
      // line-to-line basis. To do that, I can efficiently utilize a
      // priority queue (min).

      // However, it can't just be an int priority queue. The reason
      // behind that: the algorithm would then be at least O(k^3logk),
      // and I have seen solutions that make do in just O(k^2logk) //
      // To overcome the O(k3) limitation, I just need to add position
      // information: thus I'm creating a different struct.
      priority_queue<posINT> myPQ;

      // Initial queue
      for (int newint = 0; newint < k; newint++) 
	myPQ.push(posINT(out[newint] + lin[0], 0));

      // Start populating the solution, while adding potential
      // /candidates/ as well
      for (int roundssum = 0; roundssum < k; roundssum++)
	{
	  posINT tmp =  myPQ.top();
	  myPQ.pop();
	  out[roundssum] = tmp.val;
	  if (tmp.pos + 1 < k)
	    myPQ.push(posINT(tmp.val-lin[tmp.pos]+lin[tmp.pos+1],tmp.pos+1));
	}
    }
    for (int answ = 0; answ < k-1; answ++)
      printf("%d ", out[answ]);
    printf("%d\n", out[k-1]);
  }
}
