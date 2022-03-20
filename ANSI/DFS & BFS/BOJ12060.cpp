#define N 1010
#include <iostream>
#include <queue>
using namespace std;

int n, m, v;
int x, y;
int array[N][N] = {0, };
int visited[N] = {0, };
queue<int> q;

void reset() {
    for (int i = 0; i <= n; i++){
        visited[i] = 0;
    }
}
void dfs(int v) {
    visited[v] = 1;
    cout << v << " ";
    for (int i = 1; i <= n; i++){
        if (array[v][i] == 1 && visited[i] == 0){
            dfs(i);
        }
    }
}
void bfs(int v) {
    q.push(v);
    visited[v] = 1;
    cout << v << " ";
    while (!q.empty()) {
        v = q.front();
        q.pop();

        for (int w = 1; w <= n; w++){
            if (array[v][w] == 1 && visited[w] == 0) {
                q.push(w);
                visited[w] = 1;
                cout << w << " ";
            }
        }
    }
}

int main() {
    cin >> n >> m >> v;
    for (int i = 0; i < m; i++){
        int x, y;
        cin >> x >> y;
        array[x][y] = 1;
        array[y][x] = 1;
    }
    reset();
    dfs(v);
    cout << "\n";
    reset();
    bfs(v);

    return 0;
}
