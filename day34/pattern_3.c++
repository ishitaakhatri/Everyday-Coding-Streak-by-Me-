#include <bits/stdc++.h>
using namespace std;
void print_pattern(int n)
{
    for (int i = 0; i < n; i++)
    {
        if (i == 0 || i == n-1)
        {
            for (int j = 0; j < n; j++)
            {
                cout << "*";
            }
        }
        else
        {
            for (int j = 0; j < n; j++)
            {
                if (j == 0 || j == n-1)
                {
                    cout << "*";
                }
                else
                {
                    cout << " ";
                }
            }
        }
        cout<<endl;
    }
}
int main()
{
    int n;
    cin >> n;
    print_pattern(n);
}