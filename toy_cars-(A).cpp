#include <bits/stdc++.h>

using namespace std;

int main() {
    int cars, gCars;
    cin >> cars;
    int cArr[cars];
    gCars = cars;

    for (int i = 0; i < cars; i++) {
        cArr[i] = i+1;
    }

    for (int i = 0; i < cars; i++) {
        for (int j = 0; j < cars; j++) {
            int num;
            cin >> num;
            switch (num) {
                case 0:
                    break;
                case 1:
                    cArr[i] = 0;
                    break;
                case 2:
                    cArr[j] = 0;
                    break;
                case 3:
                    cArr[i] = 0;
                    cArr[j] = 0;
                    break;
                default:
                    break;
            }
        }
    }

    for (int i = 0; i < cars; i++) {
        if (cArr[i] == 0)
            gCars--;
    }

    cout << gCars << endl;

    if (gCars > 0) {
        for (int i = 0; i < cars; i++) {
            if (cArr[i] != 0)
                cout << cArr[i] << " ";
        }
    }

    return 0;
}