#include<iostream>
#include<vector>
using namespace std;
int largest(vector<int> numbers,int size)
{
    for(int i=0;i<size;i++)
    {
        if(numbers[0]<numbers[i])
        {
            return i;
        }
    }
}
int second_largest(vector<int>numbers,int size)
{
    int largest=largest(numbers,size);

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
    int second_largest=second_largest(numbers,size,largest);
}