#include <iostream>
#include <queue>

using namespace std;

bool board[50][50];

//           상  하  좌  우
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

void bfs(int r, int c, int N, int M) {
	queue<pair<int, int> > q;

	q.push(make_pair(r, c));
	board[r][c] = 0;

	while (!q.empty()) {
		r = q.front().first;
		c = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int nr = r + dr[i];
			int nc = c + dc[i];

			if (0 <= nr && nr < N && 0 <= nc && nc < M) {
				if (board[nr][nc] == 1) {
					q.push(make_pair(nr, nc));
					board[nr][nc] = 0;
				}
			}
		}
	}
}

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	for (int t = 0; t < T; t++) {
		int M, N, K;
		cin >> M >> N >> K;

		for (int k = 0; k < K; k++) {
			int x, y;
			cin >> x >> y;
			board[y][x] = 1;
		}

		int count = 0;
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < M; c++) {
				if (board[r][c] == 1) {
					bfs(r, c, N, M);
					count += 1;
				}
			}
		}
		cout << count << endl;
	}

	return 0;	
}
