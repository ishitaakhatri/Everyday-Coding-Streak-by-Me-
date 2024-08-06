#include<bits/stdc++.h>
using namespace std;

void print_1(int n){
    for(int i = 1;i <= n;i++){
        for(int j = 0;j <= i;j++){
            cout<<" ";
        }
        for(int j = (2 * n) - (2 * i) + 1; j > 0;j--){
            cout<<"*";
        }
        for(int j = 0;j <= i;j++){
            cout<<" ";
        }
        cout<<endl;
    }


}
int main()
{
    int n;
    cin>>n;
    print_1(n);
}