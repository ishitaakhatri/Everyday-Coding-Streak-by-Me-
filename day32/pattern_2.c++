#include<bits/stdc++.h>
using namespace std;
void print_pattern(int n){
    for(int i = 0;i <= n;i++){
        for(char ch = 'A';ch <= 'A'+ i;ch++){
            cout<<ch;
            
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