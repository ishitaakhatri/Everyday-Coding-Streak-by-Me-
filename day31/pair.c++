#include<bits/stdc++.h>
using namespace std;
int main()
{
    pair<int,int> p = {1,3};
    cout<< p.first <<" "<< p.second<<endl;
    pair<int,pair<int,int>> f = {2,{3,4}};
    cout<< f.first <<" "<< f.second.second<<" "<<f.second.first<<endl;
    pair<int,int> arr[] = {{1,2},{2,3},{3,4}};
    cout<<arr[1].second;
}