#import <iostream>
#import <queue>
#import <vector>

using namespace std;

int main() {
  int n; // number of test cases
  cin >> n;

  int b,sg,sb; // battle positions, greensoldiers, bluesoldiers;
  int tmp, win; // placeholders, avoid reinitialization

  while (n--) {
    cin >> b >> sg >> sb;

    priority_queue<int> greenSoldiers;
    priority_queue<int> blueSoldiers;

    for (int i = 0; i < sg; i++) {
      cin >> tmp;
      greenSoldiers.push(tmp);
    }

    for (int i = 0; i < sb; i++) {
      cin >> tmp;
      blueSoldiers.push(tmp);
    }

    // Finished with input handling

    while (true)
      {
	vector<int> tmpblue;
	vector<int> tmpgreen;

	for (int i = 0; i < b; i++)
	  {
	    if ((blueSoldiers.empty())||(greenSoldiers.empty()))
	      break;

	    win = blueSoldiers.top() - greenSoldiers.top();
	    blueSoldiers.pop();
	    greenSoldiers.pop();

	    if (win > 0)
	      tmpblue.push_back(win);
	    else if (win < 0)
	      tmpgreen.push_back(-win);
	  }

	for (int i = 0; i < tmpblue.size(); i++)
	  blueSoldiers.push(tmpblue[i]);
	for (int i = 0; i < tmpgreen.size(); i++)
	  greenSoldiers.push(tmpgreen[i]);

	if ((blueSoldiers.empty())||(greenSoldiers.empty()))
	    break;
      }
    if ((blueSoldiers.empty())&&(greenSoldiers.empty()))
      cout << "green and blue died" << endl;
    else if (greenSoldiers.empty())
      {
	cout << "blue wins" << endl;
	while (not (blueSoldiers.empty()))
	  {
	    cout << blueSoldiers.top() << endl;
	    blueSoldiers.pop();
	  }
      }
    else // if (blueSoldiers.empty())
      {
	cout << "green wins" << endl;
	while (not (greenSoldiers.empty()))
	  {
	    cout << greenSoldiers.top() << endl;
	    greenSoldiers.pop();
	  }
      }
    if (n)
      cout << endl;


  }
}
