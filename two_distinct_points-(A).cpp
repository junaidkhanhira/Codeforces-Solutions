#include <iostream>

using namespace std;

int main() {
    int q;
    unsigned long long l1, r1, l2, r2;

    cin >> q;

    for (int i = 0; i < q; i++) {
        cin >> l1 >> r1 >> l2 >> r2;
        if (l1 == r2)
            l1++;
        cout << l1 << " " << r2 << endl;
    }

    return 0;
}