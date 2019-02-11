//https://practice.geeksforgeeks.org/problems/count-the-elements/0
using namespace std;
#include <iostream>

int main() {
	int t;
	long n, m=-1;
	cin >> t;
	while (t--) {
	    cin >> n;
	    long a[n];
	    long b[n];
	    
	    for(long i=0; i<n; i++) {
	        cin>>a[i];
	        m = max(a[i], m);
	    }
	    for(long i=0; i<n; i++) {
	        cin>>b[i];
	        m = max(b[i], m);
	    }
	    
	    
	    long c[m+1] = {0};
        for(long i=0; i<n; i++) c[b[i]]++;
	    // Count the occurences
        for(long i=1; i<=m; i++) c[i] += c[i-1];
	    // Sum up cumulatively 
	    
        long qc;
	    long q;
	    cin>>qc;
	    for(int i=0; i<qc; i++){
	        cin>>q;
	        cout << c[a[q]] <<endl;
	    }//for 
	    
	}//while
	return 0;
}

/*
1
6
1 2 3 4 7 9
0 1 2 1 1 4
2
5
4 
*/
// Note: The results get written to after just after reading the query input
// Dont get confused seeing the output