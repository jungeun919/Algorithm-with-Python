#include <iostream>
#include <queue>
#include <tuple> // C++11 이상

using namespace std;

int N, M;
int board[1001][1001];
int dist[1001][1001][2] = {0, }; // 벽 부순 여부에 따른 최단 거리

//           상  하  좌  우
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

int bfs() {
	queue<tuple<int, int, int> > q;

	q.push(make_tuple(0, 0, 0)); // (r, c, 벽 부순 여부)
	dist[0][0][0] = 1;

	while (!q.empty()) {
		int r, c, wall;
		tie(r, c, wall) = q.front();
		q.pop();

		if (r == N-1 && c == M-1) {
			return dist[r][c][wall];
		}

		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d];
			int nc = c + dc[d];

			if (0 <= nr && nr < N && 0 <= nc && nc < M) {
				// 이동할 수 없고, 벽을 부순 적이 없는 경우
				if (board[nr][nc] == 1 && wall == 0) {
					dist[nr][nc][1] = dist[r][c][0] + 1;
					q.push(make_tuple(nr, nc, 1));
				}
				// 이동할 수 있고, 아직 방문하지 않은 경우
				else if (board[nr][nc] == 0 && dist[nr][nc][wall] == 0) {
					dist[nr][nc][wall] = dist[r][c][wall] + 1;
					q.push(make_tuple(nr, nc, wall));
				}
			}
		}
	}

	return -1;
}

int main() {
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			char temp;
			cin >> temp;
			board[i][j] = temp - '0';
		}
	}

	cout << bfs() << endl;

	return 0;
}
