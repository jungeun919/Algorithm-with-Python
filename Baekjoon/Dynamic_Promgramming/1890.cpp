#include <iostream>
#include <vector>

using namespace std;

int main() {
	int N;
	cin >> N;

	vector<vector<int> > board(N, vector<int>(N));
	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N; c++) {
			cin >> board[r][c];
		}
	}

	vector<vector<long long> > dp(N, vector<long long>(N)); // (r, c)까지 가는 경로 개수
	dp[0][0] = 1;

	for (int r = 0; r < N; r++) {
		for (int c = 0; c < N; c++) {
			if (r == N-1 && c == N-1) {
				cout << dp[r][c] << endl;
				break;
			}

			int move = board[r][c];
			if (c + move < N) { // 오른쪽 이동
				dp[r][c + move] += dp[r][c];
			} 
			if (r + move < N) { // 아래 이동
				dp[r + move][c] += dp[r][c];
			}
		}
	}

	return 0;
}
