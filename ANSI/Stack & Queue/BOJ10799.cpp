#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
    int count = 0;
    stack<int> stack_vps;
    string vps;
    cin >> vps;
    for (int i = 0; i < vps.length(); i++){
        if (vps[i] == '(') {
            stack_vps.push(i);
        } else {
            if (stack_vps.top() + 1 == i) {
                stack_vps.pop();
                count += stack_vps.size();
            } else {
                stack_vps.pop();
                count += 1;
            }
        }
    }
    cout << count;

    return 0;
}