#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;

	while (T--) {
		int n;
		cin >> n;

		vector<vector<int> > sticker(2, vector<int>(n));
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < n; j++) {
				cin >> sticker[i][j];
			}
		}

		// dp[0][i]: i열까지 봤을 경우, 0행 i열을 마지막으로 선택
		// dp[1][i]: i얄까지 봤을 경우, 1행 i열을 마지막으로 선택
		vector<vector<int> > dp(2, vector<int>(n));
		// for (int i = 0; i < 2; i++) {
		// 	for (int j = 0; j < n; j++) {
		// 		cout << dp[i][j] << " ";
		// 	}
		// 	cout << endl;
		// }

		dp[0][0] = sticker[0][0];
		dp[1][0] = sticker[1][0];
		if (n == 1) {
			cout << max(dp[0][0], dp[1][0]) << endl;
			continue;
		}

		dp[0][1] = sticker[1][0] + sticker[0][1];
		dp[1][1] = sticker[0][0] + sticker[1][1];
		if (n == 2) {
			cout << max(dp[0][1], dp[1][1]) << endl;
			continue;
		}

		for (int i = 2; i < n; i++) {
			dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + sticker[0][i];
			dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + sticker[1][i];
		}
		cout << max(dp[0][n-1], dp[1][n-1]) << endl;
	}

	return 0;
}
