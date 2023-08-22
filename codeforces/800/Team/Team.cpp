// TotalInputs = int(input())

// Inputs = []

// for _ in range(TotalInputs):
//     Inputs.append(sum([int(i) for i in input().split(" ")]))

// Output = 0

// for i in Inputs:
//     if i >= 2:
//         Output += 1

// print(Output)

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int numOfInputs;

    cin >> numOfInputs;

    vector<int> answers;

    for (int i = 0; i < numOfInputs; i++) {
        int sum = 0;

        for (int i = 0; i < 3; i++) {
            int input;
            cin >> input;
            sum += input;
        }

        answers.push_back(sum);
    }

    int output = 0;

    for (int answer: answers) {
        if (answer >= 2) {
            output += 1;
        }
    }

    cout << output;

    return 0;
}