#include <iostream>
#include <vector>
#include <string>

int main() {
    int cases;
    std::cin >> cases;
    std::cin.ignore();
    
    for (int caseNum = 0; caseNum < cases; caseNum++) {
        std::string myString;
        std::cin.ignore(); // Consume the newline after cases
        std::getline(std::cin, myString);
        
        std::vector<int> startingPoints;
        startingPoints.push_back(0);
        
	// std::cout << "Case: " << caseNum << "\t" + myString << std::endl;
        for (int index = 1; index < myString.length(); index++) 
            if (myString[0] == myString[index]) 
                startingPoints.push_back(index);
        
        bool periodFound = false;
	// For every other character in the string.
        for (int index = 1; index < myString.length(); index++)
	  {
            char currentChar = myString[index];
            if (periodFound) 
                break;
	    // std::cout << "Starting with index " << index << std::endl;

	    // Clever hack to iterate startingPoints
            for (int i = 0; i < startingPoints.size(); )
	      {
		// std::cout << "startingPoint " << startingPoints[i] << std::endl;
		if (startingPoints[i]+index < myString.length())
		  {
		    // If this is not a valid starting point, delete
		    // it, otherwise, move to the next (i++)
                    if (myString[startingPoints[i] + index]
			!= currentChar) 
                        startingPoints.erase(startingPoints.begin() + i);
		    else 
		      i++;
		  }
		else
		  {
                    if (index * startingPoints.size()
			== myString.length() ||
			startingPoints.size() == 1) 
		      {
			periodFound = true;
			break;
                       } 
		    else
		      startingPoints.erase(startingPoints.begin() + i);
		  }
	      }
        }
        
        if (caseNum > 0) {
            std::cout << std::endl;
        }


        if (startingPoints.size() > 1) {
            std::cout << startingPoints[1] << std::endl;
        } else {
            std::cout << myString.length() << std::endl;
        }
    }
    
    return 0;
}
