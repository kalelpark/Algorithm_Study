#include <iostream>
#include <queue>
#include <algorithm>
#define N 1001
using namespace std;

int array_array[N][N];
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
int array_time[N][N];

int main(){
    int m, n;
    cin >> m >> n;
    queue<pair<int, int>> q;

    for (int i = 0; i <n; i++){
        for (int j = 0; j < m; j++){
            cin >> array_array[i][j];
            array_time[i][j] = -1;
            if (array_array[i][j] == 1){
                q.push(make_pair(i, j));
                array_time[i][j] = 0;
            }
        }
    }

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int temp_x = x + dx[i];
            int temp_y = y + dy[i];
            if (temp_x >= 0 && temp_y >= 0 && temp_x < n && temp_y < m){
                if(array_array[temp_x][temp_y] == 0 && array_time[temp_x][temp_y] == -1){
                    array_time[temp_x][temp_y] = array_time[x][y] + 1;
                    q.push(make_pair(temp_x, temp_y));
                }
            }
        }
    }

    int result = 0;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            result = max(result, array_time[i][j]);
        }
    }

    for (int i =0; i < n; i++){
        for (int j =0; j < m; j++){
            if (array_array[i][j]  == 0 && array_time[i][j] == -1) {
                result = -1;
            }
        }
    }

    cout << result;

    return 0;
}
