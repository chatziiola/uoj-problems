#include <iostream>
#include <string>

using namespace std;

int main()
{
  int counter = 1;
  string s;

  while ( cin >> s && s != "*")
    {
	if (s == "Hajj")
	  cout << "Case " << counter++ << ": Hajj-e-Akbar" << endl;
	else // "Umrah":
	    cout << "Case " << counter++ << ": Hajj-e-Asghar" << endl;
	  
    }
}
