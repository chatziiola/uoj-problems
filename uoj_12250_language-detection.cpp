// Tedious
#include <iostream>
#include <string>
using namespace std;

int main() {
  string inputArr;
  string lang;
  int cases = 1;
  while (cin >> inputArr and inputArr != "#") {

    if (inputArr == "HELLO")
      lang = "ENGLISH";
    else if (inputArr == "HOLA")
      lang = "SPANISH";
    else if (inputArr == "HALLO")
      lang = "GERMAN";
    else if (inputArr == "BONJOUR")
      lang = "FRENCH";
    else if (inputArr == "CIAO")
      lang = "ITALIAN";
    else if (inputArr == "ZDRAVSTVUJTE")
      lang = "RUSSIAN";
    else
      lang = "UNKNOWN";
    cout << "Case " << cases++ << ": " << lang << endl;
  }
}
