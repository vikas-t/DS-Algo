//demonstrate arrays

#include <iostream>
using namespace std;

int arrSize(int arr[]){
    return sizeof(arr)/sizeof(arr[0]);
}


int main() {
    int arr[4] = {1, 2, 3, 5};
    cout << arrSize(arr);
    return 0;
}