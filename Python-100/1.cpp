#include<iostream>
using namespace std;

int main()
{
    int n;
    cin>>n;
    int a[n];
    for (int i = 0; i < n; i++)
    {
cout<<"weight list "<<i+1<<endl;
        cin>>a[i];
    }

    for (int i = 0; i < n; i++)
    {
        if(a[i]>a[i+1])
        {
            swap(a[i],a[i+1]);
        }
    }
    
for (int i = 0; i < n; i++)
{
    cout<<a[i]<<"will be at" <<i+1<<" number "<<endl;
}


    
}