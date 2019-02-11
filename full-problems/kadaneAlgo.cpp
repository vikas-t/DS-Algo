// https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

#include <iostream>
#include <climits>
using namespace std;

int maxContSum(int arr[], int size){
    //int size = sizeof(arr)/sizeof(arr[0]);
    int meh = 0;
    int mine = INT_MIN;
    int msf = INT_MIN;
    for (int i=0; i<size; i++) {
        meh = meh + arr[i];
        if (meh < 0) meh = 0;
        if (meh > msf) {
            msf = meh;
        }//if
        mine = max(mine, arr[i]);
    }//for
    
    if (mine == 0 && msf == 0) return 0;
    if (msf == 0 && mine < 0 ) return mine;
    return msf;
}

int main() {
	int t, n, i;
	cin >> t;
	while (t--) {
	    cin >> n;
	    int arr[n];
	    for(i=0; i<n; i++) {
	        cin >> arr[i];
	    }//for
	    cout << maxContSum(arr, n) << endl;
	}
	return 0;
}