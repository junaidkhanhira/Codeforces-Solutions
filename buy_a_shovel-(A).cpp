#include <iostream>

using namespace std;

int main()
{
	int k, r, n = 1;

	cin >> k >> r;

	while(true){
        if((n * k) % 10 == 0){
            break;
        }
        else if ((n * k - r) % 10 == 0){
            break;
        }else{
            n++;
        }
	}

	cout << n << endl;

	return 0;
}
