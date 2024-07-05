c:\Users\Admin\Desktop\C_C++_DSA\day104\vectors.cpp#include <iostream>
#include <vector>
using namespace std;
int delete_element(int n,int arr[])
{
    int target;
    cout<<"enter the element you want to delete"<<endl;
    cin>>target;
    for(int p=0;p<n;p++)
    {
        if(arr[p]==target)
        {
            for(int q=n-1;q>=target;q--)
            {
                arr[q-1]=arr[q];
            }
            cout<<"new array formed would be"<<endl;
            for(int r=0;r<n;r++)
            {
                cout<<arr[r]<<" ";
            }
        }
    }
}
int search(int n, int arr[])
{
    int target;
    cout << "enter the number you wanna search" << endl;
    cin >> target;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == target)
        {
            cout << "element to be searched is present at" << endl;
            cout << i<<endl;
        }
    }
}
int insert(int n, int arr[])
{
    int position;
    int number;
    cout << "enter the position where you want to insert the number" << endl;
    cin >> position;
    cout << "enter the number you want to insert" << endl;
    cin >> number;
    for (int j = 0; j < n; j++)
    {
        if (j == position)
        {
           for(int k=n;k>=position;k--)
           {
            arr[k+1]=arr[k];
           }
           arr[position]=number;
        }
    }
    cout<<"new array formed"<<endl;
    for(int l=0;l<n;l++)
    {
        cout<<arr[l]<<" "<<endl;
    }
}
int main()
{
    int arr[7] = {10, 20, 30, 40, 50};
    int size = sizeof(arr) / sizeof(arr[0]);
    search(size, arr);
    insert(size, arr);
    delete_element(size,arr);
}
