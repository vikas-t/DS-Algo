// Vectors demonstration

#include <iostream>
#include <vector>
using namespace std;

void vectors() {
    vector <int> t;
    t.push_back(10);
    t.push_back(12);
    t.push_back(13);

    vector <int>::iterator i;
    for(i=t.begin(); i!=t.end();  i++) {
        cout<<*i<<" ";
    }//for
    cout<<endl;
}//vectors

void vectors2() {
    vector <vector <int>> t;
    vector <int> t1;
    vector <int> t2;

    t1.push_back(1);
    t1.push_back(3);
    t1.push_back(5);

    t2.push_back(2);
    t2.push_back(4);
    t2.push_back(6);

    t.push_back(t1);
    t.push_back(t2);

    vector <vector<int>>::iterator i;
    vector <int>::iterator j;

    for(i=t.begin(); i!=t.end(); i++) {
        for(j=(*i).begin(); j!=(*i).end(); j++) {
            cout<<*j<<" ";
        }
        cout<<endl;
    }//for

    for(int i=0;  i<t2.size(); i++) cout<<t2[i]<<" ";
    cout<<endl;
} //vectors2


int main() {
    vectors();
    vectors2();
    return 0;
}