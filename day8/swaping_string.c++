#include<iostream>
#include<string>
using namespace std;
int main()
{
    string letters;
    cout<<"please enter a string"<<endl;
    cin>>letters;
    for(int i=0;i<letters.length()-1;i+=2)
    {
       swap(letters[i],letters[i+1]);
    }
    cout<<letters;

}