#include <iostream>
#include <deque>
#include <string>
using namespace  std;

int main() {
    int count = 0;
    bool No = true;
    deque<int> Num_Stack;
    deque<char>  calc_Stack;
    string temp;
    int n;
    int put;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> put;

        while (count < put){
            count += 1;
            Num_Stack.push_back(count);
            calc_Stack.push_back('+');
        }

        if (Num_Stack.back() == put) {
            Num_Stack.pop_back();
            calc_Stack.push_back('-');
        } else {
            No = false;
            break;
        }
    }

    if (!No){
        cout << "NO";
    } else {
        for (int i = 0; i < calc_Stack.size(); i++){
            cout << calc_Stack[i] << "\n";
        }
    }
    return 0;
}