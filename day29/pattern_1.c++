#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    int m;
    cout<<"enter the no. of rows"<<endl;
    cin>>n;
    cout<<"enter the number of columns"<<endl;
    cin>>m;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            cout<<"*"<<" ";
        }
        cout<<endl;
    }
}