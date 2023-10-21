#include <string>
#include <iostream>
#include <map>

using namespace std;


char myArray[] = {'C','G','T'};
char letter;

int main()
{
  int cases;
  int m, n;

  cin >> cases;
  while (cases--)
    {
      cin >> m >> n;
      
      string sequences[m];
      getline(cin,sequences[0]); // Ignore \n

      for (int index = 0; index < m; index++)
	{
	  getline(cin, sequences[index]);
	  // cout << "\t>" << sequences[index] << endl;
	}

      string consensusString = sequences[0];
      long consensusError = 0;
      char consensusLetter = 'A';


      for (int index = 0; index < n; index++)
	{
	  map<char,int> characterMap ;
	  characterMap['A'] = 0;
	  characterMap['C'] = 0;
	  characterMap['G'] = 0;
	  characterMap['T'] = 0;

	  for (int seq = 0; seq < m; seq++)
            characterMap[sequences[seq][index]]++;

	  consensusLetter = 'A';
	  for (int i = 0; i < 3; i++)
	    {
	      letter = myArray[i];
	      if (characterMap[letter] > characterMap[consensusLetter])
		consensusLetter = letter;
	    }

	  consensusString[index] = consensusLetter;
	  consensusError += m - characterMap[consensusLetter];
	}
      // cout << "\t>" << m << " " << n << endl;
      cout << consensusString << endl;
      cout << consensusError << endl;
    }
  
}
