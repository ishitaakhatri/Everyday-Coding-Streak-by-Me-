#include<bits/stdc++.h>
using namespace std;
void print_1(int n){
    for(int i=1;i<=n;i++){
        for(int j=i;j<=n;j++){
            cout<<"*"<<" ";
        }
        cout<<endl;
    }
}
int main(){
    int n;
    cin>>n;
    print_1(n);
}