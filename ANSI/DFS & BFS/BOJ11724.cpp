#include <iostream>
#include <vector>
#define N 1010
using namespace std;
vector<int> array[N];
int visited[N] = {0, };
void dfs(int start) {
    visited[start] = 1;
    for (int temp = 0; temp < array[start].size(); temp++){
        int take = array[start][temp];
        if (visited[take] == 0) {
            dfs(take);
        }
    }
}

int main(){
    int n, m, x, y;
    int ans = 0;
    cin >> n >> m;

    for (int i = 0; i <m; i++){
        cin >> x >> y;
        array[x].push_back(y);
        array[y].push_back(x);
    }
    for (int i = 1; i <= n; i++){
        if (visited[i] == 0){
            ans +=  1;
            dfs(i);
        }
    }

    cout << ans;
    return 0;
}