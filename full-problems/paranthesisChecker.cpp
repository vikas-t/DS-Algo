#include <iostream>
#include <stack>
using namespace std;

bool isBalanced(string str) {
    stack<char> s;
    int x;
    
    for (int i=0; i<str.length(); i++) {
        
        if (str[i] == '(' || str[i] == '{' || str[i] == '['){
            s.push(str[i]);
            continue;
        } //if
        
        if (s.empty()) return false;
        
        switch (str[i]) {
            case ')':
            x = s.top();
            s.pop();
            if (x != '(') return false; 
            break;
            
            case '}':
            x = s.top();
            s.pop();
            if ( x != '{') return false;
            break;
            
            case ']':
            x = s.top();
            s.pop();
            if ( x != '[') return false;
            break;
        }//switch
    }//for
    
    return (s.empty());
}

// int main() {
// 	int t;
// 	string s;
// 	cin>>t;
// 	while (t--) {
// 	    cin>>s;
// 	    if (isBalanced(s)) {
// 	        cout << "balanced" << endl;
// 	    }
// 	    else 
// 	        cout << "not balanced" << endl;
// 	}
	
// 	return 0;
// }

int main() {
    cout << isBalanced("{([])}") << endl;
    cout << isBalanced("{([])})") << endl;
    return 0;
}