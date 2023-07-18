#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
  
    vector<int> v;
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int el;
        cin>>el;
        v.push_back(el);
    }
    sort(v.begin(),v.end());
    for(int i:v)
    {
        cout<<i<<" ";
    }
    return 0;
}
