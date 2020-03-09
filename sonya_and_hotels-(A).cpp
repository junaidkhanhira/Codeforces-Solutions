#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, ind = 0;
    long long d;
    cin >> n >> d;
    vector<long long> xv(n);
    vector<long long> xvr(n*2);
    set<long long> rs;
    for (int i = 0; i < n; i++) {
        cin >> xv[i];
    }

    if (n == 1) {
        cout << 2;
    } else {
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                xvr[ind] = xv[i] - d;
                ind++;
                if (xv[i] + d <= xv[i+1] - d) {
                    xvr[ind] = xv[i] + d;
                    ind++;
                }
                continue;
            }
            if (i == n-1) {
                xvr[ind] = xv[i] + d;
                ind++;
                if (xv[i] - d >= xv[i-1]+d) {
                    xvr[ind] = xv[i] - d;
                    ind++;
                }
                continue;
            }
            if (xv[i] - d >= xv[i-1] + d) {
                xvr[ind] = xv[i] - d;
                ind++;
            }
            if (xv[i] + d <= xv[i+1] - d) {
                xvr[ind] = xv[i] + d;
                ind++;
            }
        }

        for (int i = 0; i < ind; i++)
            rs.insert(xvr[i]);

        cout << rs.size();
    }

    return 0;
}