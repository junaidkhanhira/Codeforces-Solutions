#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    string s;
    cin >> s;
    int r = 0, b = 0, y = 0, g = 0;
    int rp = s.find('R');
    int rb = s.find('B');
    int ry = s.find('Y');
    int rg = s.find('G');

    for (auto i = 0; i < s.length(); i++) {
        if (s[i] == '!') {
            if (rp%4 == i%4) r++;
            if (rb%4 == i%4) b++;
            if (ry%4 == i%4) y++;
            if (rg%4 == i%4) g++;
        }
    }

    cout << r << " " << b << " " << y << " " << g << endl;

    return 0;
}