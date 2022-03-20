#include <iostream>
#include <vector>
#define N 51
using namespace std;
int array[N][N];
int visited[N][N];
int w, h;
int dy[] = {0,0,-1,1,-1,-1,1,1};
int dx[] = {1,-1,0,0,-1,1,-1,1};
void reset() {
    for (int i = 0; i < h; i++){
        for (int j = 0; j < w; j++){
            array[i][j] = 0;
            visited[i][j] = 0;
        }
    }
}

void dfs(int x, int y){
    visited[x][y] = 1;
    for (int i = 0; i < 8; i ++){
        int temp_x = x + dx[i];
        int temp_y = y + dy[i];
        if (temp_y < 0 || temp_x < 0 || temp_x >= h || temp_y >= w)
            continue;
        if (array[temp_x][temp_y] == 1 && visited[temp_x][temp_y] == 0) {
            dfs(temp_x, temp_y);
        }
    }
}


int main(){
    while (1) {
        cin >> w >> h;
        if (w == 0 && h == 0){
            break;
        }
        reset();

        for (int i = 0; i < h; i++){
            for (int j = 0; j <w; j++){
                cin >> array[i][j];
            }
        }
        int ans = 0;
        for (int i = 0; i < h; i++){
            for (int j = 0; j < w; j++){
                if (array[i][j] == 1 && visited[i][j] == 0) {
                    dfs(i, j);
                    ans += 1;
                }
            }
        }
        cout << ans << "\n";
    }
    return 0;
}