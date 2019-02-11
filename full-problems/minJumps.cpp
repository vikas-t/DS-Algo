// https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps/0

#include <iostream>
#include <climits>
using namespace std;

int minJumpsRec(int arr[], int size, int p){
    
    if (p >= size-1) return 0;
    if (arr[p]==0) return 0;
    int m=INT_MAX;
    for(int i=1; i<=arr[p]; i++){
        m = min(m, 1+minJumpsRec(arr, size, p+i));
    }//for
    return m;
}

int minJumpsDp(int arr[], int size){
    int dp[size];
    dp[0] = 0;
    int m = INT_MAX;
    for (int i=1; i<size; i++) {
        dp[i] = m;
        if (arr[i] == 0) {
            dp[i] = m;
            continue;
        }
        for (int j=0; j<i; j++) {
            if (j + arr[j] >= i && dp[j] != m) {
                dp[i] = min(dp[j] + 1, dp[i]);
            }//if
            
        }//inner
    }//for outer
    
    for (int i=0; i<size; i++) {
        cout << dp[i] << " ";
    }
    cout << endl;
    
    if (dp[size-1] == m) return -1;
    return dp[size-1];
}

// To take the input from the stdout
// int main() {
// 	int t, i, n;
// 	cin>>t;
// 	while (t--) {
// 	    cin>>n;
// 	    int arr[n];
// 	    for(i=0;i<n;i++){
// 	        cin>>arr[i];
// 	    }//for
// 	    cout << minJumpsDp(arr, n)<<endl;
// 	} //while
	
// 	return 0;
// }

int main(){
int arr[] = {1,3,5,8,9,2,6,7,6,8,9};
int size = sizeof(arr)/(arr[0]); 
cout << minJumpsDp(arr, size);
return 0;
}