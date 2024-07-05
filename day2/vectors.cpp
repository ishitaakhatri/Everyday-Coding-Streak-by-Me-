#include<iostream>
#include<vector>
using namespace std;
int main()
{
    vector<int> v;
    v.push_back(10);
    v.push_back(20);
    v.push_back(30);
    v.push_back(40);
    for(int i=0;i<v.size();i++)
    {
        cout<<v.at(i)<<endl;
    }
    //another way for declaring a vector 
    vector<int> numbers{20,40,60,80};
    for( int x:numbers)
    {
        cout<<x<<endl;
    }
//pop-back,front(),back()operations
    numbers.pop_back();
    cout<<"modified vector is"<<endl;
    for(auto p:numbers)
    {
        cout<<p<<" "<<endl;
    }   
    cout<<"performing front() and back() funtions"<<endl;
    cout<<numbers.front()<<endl;
    cout<<numbers.back()<<endl; 
//inserting an element in a vector 
    numbers.insert(numbers.begin(),200);
    numbers.insert(numbers.begin()+2,3,500);
    for(auto s:numbers)
    {
        cout<<s<<endl;
    }  
//erase function
cout<<"using the erase function"<<endl;
    v.erase(v.begin());
    numbers.erase(numbers.end()-1);
    cout<<"on numbers"<<endl;
    for(auto r:numbers)
    {
        cout<<r<<endl;
    } 
    cout<<"on v"<<endl;   
    for(auto t:v)
    {
        cout<<t<<endl;
    }
}