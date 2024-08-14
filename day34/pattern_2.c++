#include<bits/stdc++.h>
using namespace std;
void print_pattern(int n)
{
    int start=1;
    for(int i=1;i<=n;i++)
    {
        //star
        for(int j = 0;j < start;j++){
            cout<<"*";
        }
        //space
        for(int j = 0;j<((2*n)-(2*i));j++){
            cout<<" ";
        }
        //star
        for(int j = 0;j < start;j++){
            cout<<"*";
        }
        start=start+1;
        cout<<endl;
    }


    for(int i = 0;i < n;i++){
        //star
        for(int j =0;j<(n-i-1);j++){
            cout<<"*";
        }
        //space
        for(int j = 0;j<((2*i)+2);j++){
            cout<<" ";
        }
        //star
          for(int j =0;j<(n-i-1);j++){
            cout<<"*";
        }
        cout<<endl;
    }
}
int main()
{
    int n;
    cin>>n;
    print_pattern(n);
}