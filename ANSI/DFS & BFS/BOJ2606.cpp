#define N 101
#include <iostream>
#include <vector>
using namespace std;
int array[N][N] = {0,};
int visited[N] = {0, };
int cnt = 0;
int n, m;
void dfs(int start){
    cnt += 1;
    visited[start] = 1;
    for (int i =1; i <= n; i++) {
        if (array[start][i] == 1 && visited[i] == 0){
            dfs(i);
        }
    }
}

int main(){
    int x, y;
    cin >> n;
    cin >> m;
    for (int i =0; i < m; i++){
        cin >> x >> y;
        array[x][y]= 1;
        array[y][x] = 1;
    }
    dfs(1);
    cout << cnt-1;
    return 0;
}