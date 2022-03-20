#include <iostream>
#include <deque>
using namespace std;

int main(void){
    deque<int> q;
    int num;
    int temp;
    int temp_2;
    cin >> num;
    deque<int> drop_list;
    for (int i = num; i > 0; i--) {
        q.push_back(i);
    }
    while (1 != q.size()) {
        temp = q.back();
        q.pop_back();
        drop_list.push_back(temp);
        temp_2 = q.back();
        q.pop_back();
        q.push_front(temp_2);
    }
    temp = q.back();
    drop_list.push_back(temp);

    for (int i = 0; i < drop_list.size(); i++) {
        cout << drop_list[i] << ' ';
    }
    return 0;
}