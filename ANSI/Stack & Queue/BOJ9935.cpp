#include <iostream>
#include <string>
using namespace  std;

int main() {
    string bomb_str;
    string bomb_name;
    string print_ans;

    cin >> bomb_str;
    cin >> bomb_name;
    print_ans = "";

    int bomb_len = bomb_name.length();
    for (int i = 0; i < bomb_str.length(); i ++){
        print_ans.push_back(bomb_str[i]);
        if (print_ans.back() == bomb_name.back()) {
            bool check = true;
            for (int j = 1; j <= bomb_len; j++){
                if (print_ans[print_ans.length() - j] != bomb_name[bomb_name.length() - j]){
                    check = false;
                }
            }
            if (check) {
                for (int j = 0; j < bomb_len; j++){
                    print_ans.pop_back();
                }
            }
        }
    }

    if (print_ans.empty()) {
        cout << "FRULA";
    } else {
        cout << print_ans;
    }

    return 0;
}