#include<iostream>
#include<vector>
using namespace std;
void second_largest(vector<int>numbers,int size)
{
    for(int i=1;i<size;i++)
    {
        if(numbers[0]<numbers[i])
        {
            swap(numbers[0],numbers[i]);
        }
    }
    for(int j=2;j<size;j++)
    {
        if(numbers[1]<numbers[j])
        {
            swap(numbers[1],numbers[j]);
        }
    }
    cout<<"the second largest element is "<<numbers[1]<<endl;
}
int main()
{
    int size;
    cout<<"enter the size of array"<<endl;
    cin>>size;
    vector<int> numbers(size);
    for(int i=0;i<size;i++)
    {
        cin>>numbers[i];
    }
    second_largest(numbers,size);
}
