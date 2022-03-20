#include <iostream>
#include <queue>
using namespace  std;

int main() {
    queue<int> q;
    int num, temp;
    int tomp;
    cin >> num >> tomp;
    queue<int> ans;

    for (int i = 1; i <= num; i++){
        q.push(i);
    }

    while (!q.empty()) {
        for (int i = 0; i < tomp-1; i++) {
            temp = q.front();
            q.pop();
            q.push(temp);
        }
        temp = q.front();
        ans.push(temp);
        q.pop();
    }
    cout << "<";
    for (int i = 0; i < num; i++){
        temp = ans.front();
        ans.pop();
        cout << temp;
        if (i == num-1) {
            cout << ">";
        } else {
            cout << ", ";
        }
    }

    return 0;
}