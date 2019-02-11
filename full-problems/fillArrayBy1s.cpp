
// https://practice.geeksforgeeks.org/problems/fill-array-by-1s/0
// The same logic times out with python

#include <iostream>
#include <climits>
using namespace std;

long sol(int arr[], long n){
    long ld[n] = {0};
    long rd[n] = {0};
    long res=-1, d;
    
    if (arr[0] == 1) ld[0] = 0; else ld[0] = LONG_MAX;
    for (long i=1; i < n; i++) {
        if (arr[i] == 1) ld[i] = i; 
        else ld[i] = ld[i-1]; 
    }//ld
    // Create an auxiliary array such that it stores the index of nearest 1
    // from the left
    
    if (arr[n-1] == 1) rd[n-1] = n-1; 
    else rd[n-1] = LONG_MAX;
    for (long i=n-2; i >= 0; i--) {
        if (arr[i] == 1) rd[i] = i; 
        else rd[i] = rd[i+1]; 
    } //rd
    // Create an auxiliary array such that it stores the index of nearest 1
    // from the right
    
    for (long i=0; i<n; i++) {
        if (arr[i] == 0 ) {
            if (ld[i] != LONG_MAX && rd[i] != LONG_MAX) d = min(i-ld[i], rd[i]-i);
            else if (ld[i] == LONG_MAX) d = rd[i]-i;
            else d = i-ld[i];
            // Take the min of left and right
            res = max(res, d);
            // The max of the requirement is the final result
        }//if
    } //for
    if (res == LONG_MAX) return -1;
    return res;
}//sol

int main() {
	long t, n;
	cin >> t;
	while (t--) {
	    cin >>n;
	    int arr[n];
	    for(long i=0; i<n; i++) cin>>arr[i];
	    cout<<sol(arr, n)<<endl;
	}
	return 0;
}

/*
Test cases
1
6 
0 0 0 0 0 1

1
6
1 0 0 0 0 0
*/