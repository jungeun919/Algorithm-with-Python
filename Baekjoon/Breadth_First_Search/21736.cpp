#include <iostream>
#include <queue>

using namespace std;

int N, M;
char board[601][601];
int start_r, start_c;

//           상  하  좌  우
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

int bfs(int start_r, int start_c) {
	bool visited[601][601] = {0, };
	int count = 0;

	queue<pair<int, int> > q;
	q.push(make_pair(start_r, start_c));
	visited[start_r][start_c] = 1;

	while (!q.empty()) {
		int r = q.front().first;
		int c = q.front().second;
		q.pop();

		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d];
			int nc = c + dc[d];
			if (0 <= nr && nr < N && 0 <= nc && nc < M) {
				if (!visited[nr][nc]) {
					if (board[nr][nc] != 'X') {
						if (board[nr][nc] == 'P') {
							count += 1;
						}
						q.push(make_pair(nr, nc));
						visited[nr][nc] = 1;
					}
				}
			}
		}
	}

	return count;
}

int main() {
	cin >> N >> M;
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> board[i][j];
			if (board[i][j] == 'I') {
				start_r = i;
				start_c = j;
			}
		}
	}

	int count = bfs(start_r, start_c);

	if (count == 0) {
		cout << "TT" << endl;
	} else {
		cout << count << endl;
	}

	return 0;
}
