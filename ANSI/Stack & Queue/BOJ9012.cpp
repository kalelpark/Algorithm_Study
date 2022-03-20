#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(){
    int test_case;
    cin >> test_case;
    string st_vps;
    int num;
    for (int i = 0; i < test_case; i++) {
        stack<char> vps_stack;
        cin >> st_vps;
        num = 0;
        for ( int j = 0; j < st_vps.length(); j++) {
            if (st_vps[j] == '(') {
                vps_stack.push('(');
            } else if ((st_vps[j] == ')') && (vps_stack.size() == 0)){
                num = 1;
                break;
            } else{
                vps_stack.pop();
            }
        }

        if ((num == 0) && (vps_stack.size() == 0)) {
            cout << "YES" << "\n";
        } else {
            cout << "NO" << "\n";
        }
    }
    return 0;
}