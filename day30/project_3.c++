#include <bits/stdc++.h>
using namespace std;
void print_pattern(int n)
{
    int start = 1;
    for (int i = 0; i <= n; i++)
    {

        for (int j = i; j > 0; j--)
        {
            if (j % 2 != 0)
            {
                cout << start;
            }
            if (j % 2 == 0)
            {
                cout << start - 1;
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