#include <iostream>

using namespace std;

int main() {
    int distance;
    cin  >> distance;

    int possible_steps[5] = {1, 2, 3, 4, 5};
    bool reached = false;

    int steps = 0;

    while (!reached) {
        for (int i = 5; i > 0; i--) {
            if (distance >= i) {
                steps += 1;
                distance -= i;
                break;
            }
            
            if (distance <= 0) {
                reached = true;
            }
        }
    }

    cout << steps;

    return 0;
}
