#include<bits/stdc++.h>
using namespace std;

void print_pattern(int n){
    for(int i = 0;i <= ((n+1)/2);i++){
        for(int j = 0;j < i;j++)
        {
            cout<<"*";
        }
        cout<<endl;
    }
    for(int i =((n+1)/2)-1;i>0;i--){
         for(int j = 0;j < i;j++)
        {
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