//https://practice.geeksforgeeks.org/problems/count-triplets-with-sum-smaller-than-x/0

#include <iostream>
#include <algorithm>
using namespace std;

int sol(int arr[], int n, int t) {
    /*
    The approach is meet in the middle with the array sorted as usual
    This did not work with python
    */
    sort(arr, arr+n);
    int l, r, count=0;
    
    for (int i=0; i<n-2; i++) {
        l = i+1;
        r = n-1;
        while (l<r) {
            if (arr[l]+arr[r]+arr[i] >= t) {
                r-=1;
            }
            else {
                count+=(r-l);
                l+=1;
            }
        }
    }//i
    
    return count;
}

int main() {
	int t, n, sum;
	cin >> t;
	while (t--) {
	    cin >> n;
	    cin >> sum;
	    int arr[n];
	    for(int i=0; i<n; i++) { cin>>arr[i]; }
	    cout<< sol(arr, n, sum) << endl;
	}
	return 0;
}