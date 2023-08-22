#include <iostream>

using namespace std;

int main() {    
    int limak, bob;
    cin >> limak;
    cin >> bob;

    int year = 0;
    
    while (limak <= bob) {
        year += 1;
        limak *= 3;
        bob *= 2;
    }

    cout << year;

    return 0;
}
