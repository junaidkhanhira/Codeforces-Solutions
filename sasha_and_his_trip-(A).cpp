#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, v, m = 0, d;
    cin >> n >> v;
    d = n-1;

    if (v >= d) {
        cout << d;
    } else {
        m = 1*v;
        d--;
        for (auto i = 2; i < n; i++) {
            m += i;
            if (v == d)
                break;
            d--;

        }
        cout << m;
    }




    return 0;
}