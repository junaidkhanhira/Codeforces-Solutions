#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, zCount = 0, nCount = 0, pCount = 0;
    cin >> n;
    vector<int> v(n);

    for (int i = 0; i < n; i++)
        cin >> v[i];

    for (int i = 0; i < n; i++)
    {
        if (v[i] == 0)
            zCount++;
        if (v[i] < 0)
            nCount++;
        if (v[i] > 0)
            pCount++;
    }

    if (pCount >= (n+1)/2)
    	cout << 1;
    else if (nCount >= (n+1)/2)
    	cout << -1;
    else 
    	cout << 0;


    return 0;
}