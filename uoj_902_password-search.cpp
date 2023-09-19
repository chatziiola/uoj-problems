            
#include <iostream>
#include <iterator>
#include <map>
#include <string>

int main()
{
  int length;
  std::string message;

  while (std::cin >> length >> message)
    {
      // std::cout<< "Length " << length << " and message\n\t" << message << std::endl;
      std::map<std::string, int> tempMap;
      std::string mySubstr;
      for (int i = length; i < message.length()+1; i++)
	{
	  mySubstr.assign(message,i-length,length);
	  tempMap[mySubstr] += 1;
	}
      int reps = 1;
      std::string answer;

      
      for (std::map<std::string,int>::iterator i =  tempMap.begin(); i!=tempMap.end(); i++)
	{
	  if (i->second > reps)
	    {
	      answer = i->first;
	      reps = i->second;
	    }
	}
      std::cout << answer << std::endl;
    }
}
