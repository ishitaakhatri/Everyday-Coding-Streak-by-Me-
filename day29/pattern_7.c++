#include <bits/stdc++.h>
using namespace std;

void print_1(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < (n - i - 1); j++) {
            cout << " ";
        }
        for (int j = 0; j < (2 * i + 1); j++) {
            cout << "*";
        }
        for (int j = 0; j < (n - i - 1); j++) {
            cout << " ";
        }
        cout << endl;
    }
}

int main() {
    int n;
    cin >> n;
    print_1(n);
    return 0;
}
