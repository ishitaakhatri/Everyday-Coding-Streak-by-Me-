#include<iostream>
#include<vector>
using namespace std;
void largest(vector<int> numbers,int size)
{
    for(int i=0;i<size;i++)
    {
        cin>>numbers[i];
    }
    for(int j=1;j<size;j++)
    {
        if(numbers[0]<numbers[j])
        {
            swap(numbers[0],numbers[j]);
        }
    }
    cout<<"the largest number is"<<numbers[0]; 
}
int main()
{
    int size;
    cout<<"enter the size of the array"<<endl;
    cin>>size;
    vector<int>numbers(size);
    largest(numbers,size);
    
}
