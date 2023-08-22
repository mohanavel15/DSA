#include <iostream>

using namespace std;

int main() {
    int numOfInputs;
    cin >> numOfInputs;

    int policeAvailable = 0;
    int unreportedCrime = 0;

    for (int i = 0; i < numOfInputs; i++) {
        int action;
        cin >> action;
        if (action > 0) {
            policeAvailable += action;
        } else {
            if (policeAvailable > 0) {
                policeAvailable -= 1;
            } else {
                unreportedCrime += 1;
            }
        }
    }

    cout << unreportedCrime;

    return 0;
}