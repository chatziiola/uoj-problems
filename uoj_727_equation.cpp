#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <stack>
#include <string>
using namespace std;
int main() {
  int t, j, i, len, k, length;
  char expr[100];
  char ch[5];
  scanf("%d\n", &t);
  for (j = 1; j <= t; j++) {
    stack<char> expstack;
    expstack.push('(');
    k = 0;
    while (gets(ch)) {
      len = strlen(ch);
      if (len == 0)
	break;
      else
	expr[k++] = ch[0];
    }
    expr[k++] = ')';
    length = k;
    if (j > 1)
      printf("\n");
    for (i = 0; i < length; i++) {
      if (expr[i] == '(' || expr[i] == '+' || expr[i] == '-' ||
	  expr[i] == '*' || expr[i] == '/') {
	if ((expr[i] == '+' || expr[i] == '-') &&
	    (expstack.top() == '*' || expstack.top() == '/' ||
	     expstack.top() == '+' || expstack.top() == '-')) {
	  while (expstack.top() == '*' || expstack.top() == '/' ||
		 expstack.top() == '+' || expstack.top() == '-') {
	    printf("%c", expstack.top());
	    expstack.pop();
	  }
	  expstack.push(expr[i]);

	} else if ((expr[i] == '*' || expr[i] == '/') &&
		   (expstack.top() == '*' || expstack.top() == '/')) {
	  printf("%c", expstack.top());
	  expstack.pop();
	  expstack.push(expr[i]);

	} else
	  expstack.push(expr[i]);
      }
      else if (expr[i] == ')')
     {
	while (expstack.top() != '(') {
	  printf("%c", expstack.top());
	  expstack.pop();
	}
	expstack.pop();
      }
      else printf("%c", expr[i]);
    }
    while (!expstack.empty()) {
      printf("%c", expstack.top());
      expstack.pop();
    }
    printf("\n");
  }
  return 0;
}
