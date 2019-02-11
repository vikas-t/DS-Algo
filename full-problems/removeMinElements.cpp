//https://practice.geeksforgeeks.org/problems/remove-minimum-elements/0

#include <iostream>
#include <climits>
#include <algorithm>
using namespace std;


long long sol(long long arr[], long long n){
    // Take 2 variables for chosing the start and end and check the condition
    long long i, j, mx, mn, subRes, s, e, res;
    
    sort(arr, arr+n);
    // The test cases do not pass if the array is not sorted, meaning
    // the original array can be modified
    subRes = 0;
    for(i=0; i<n; i++) {
        mx=arr[i];
        mn=arr[i];
        for(j=i; j<n; j++) {
            if (arr[j] >= mx) mx = arr[j];
            else if (arr[j] <= mn) mn = arr[j];    
            if (mn*2 > mx){
                subRes = max(subRes, j-i+1);
            }
            
        }//end
    }//start
    
    return n-subRes;
}

int main() {
    long long n;
    int t;
    cin >> t;
    while (t--) {
        cin>>n;
        long long arr[n];
        for(long long i=0; i<n ; i++) cin>>arr[i];
        cout<<sol(arr, n)<<endl;
    }//while
	//code
	return 0;
}