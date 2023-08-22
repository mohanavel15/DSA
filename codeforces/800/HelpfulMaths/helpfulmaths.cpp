#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string input;
    cin >> input;

    int n = input.length();
    vector<int> nums;

    for (int i = 0; i < n; i++) {
        char ch = input[i];
        if (ch != '+') {
            int num = input[i] - '0';
            nums.push_back(num);
        }
    }

    n = nums.size();

    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (nums[j] > nums[j+1]) {
                int num1 = nums[j];
                nums[j] = nums[j+1];
                nums[j+1] = num1;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << nums[i];
        if (i+1 < n) {
            cout << '+';
        }
    }

    return 0;
}