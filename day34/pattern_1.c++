#include<bits/stdc++.h>
using namespace std;
void print_pattern(int n)
{
    int inis = 0;
    for(int i=1;i<=10;i++)
    {
        for(int j = 0;j <= n-i;j++){
            cout<<"*";
        }
        for(int j = 0;j < inis;j++){
            cout<<" ";
        }
        for(int j = 0;j <= n-i;j++){
            cout<<"*";
        }
        inis+=2;
        cout<<endl;
    }


     int inis2 =  2 * (n - 1);
    for(int i=1;i<=10;i++)
    {
        for(int j = 1;j <= i;j++){
            cout<<"*";
        }
        for(int j = 0;j < inis2;j++){
            cout<<" ";
        }
        for(int j = 1;j <= i;j++){
            cout<<"*";
        }
        inis2-=2;
        cout<<endl;
    }
}
int main()
{
    int n;
    cin>>n;
    print_pattern(n);
}