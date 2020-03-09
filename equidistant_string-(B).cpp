#include <bits/stdc++.h>
using namespace std;

int main() {
    string s, t, p;
    cin >> s;
    cin >> t;
    int ss = s.size(), sm = 0, d1 = 0, d2 = 0;
    char arr[ss], fl = 's';

    if (s == t)
        cout << s << endl;
    else {
        for (int i = 0; i < ss; i++) {
            if (s[i] != t[i]) {
                if (fl == 's') {
                    arr[i] = s[i];
                    fl = 't';
                }
                else {
                    arr[i] = t[i];
                    fl = 's';
                }
            } else {
                sm++;
                arr[i] = s[i];
            }
        }

        
        for (int i = 0; i < ss; i++)
            p += arr[i];

        for (int i = 0; i < ss; i++) {
            if (s[i] == p[i])
                d1++;
        }

        for (int i = 0; i < ss; i++) {
            if (t[i] == p[i])
                d2++;
        }

        if (d1 == d2)
            cout << p;
        else
            cout << "impossible";
    }

    return 0;
}