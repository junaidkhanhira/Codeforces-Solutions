#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    while (n--) {
        int a, b, c;
        cin >> a >> b >> c;
        int r = 0;
        while (b >= 1 && c >= 2) {
            r += 3;
            c -= 2;
            b -= 1;
        }
        while (a >= 1 && b >= 2) {
            r += 3;
            b -= 2;
            a -= 1;
        }
        cout << r << endl;
    }

    return 0;
}