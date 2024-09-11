// dp[0] = 0
// dp[1] = P1
// dp[2] = max(dp[2], P2 + dp[2-0], P1 + dp[2-1])

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N;
	cin >> N;

	vector<int> P(N+1); // 벡터의 모든 요소는 기본값 0으로 초기화
	for (int i = 1; i <= N; i++) {
		cin >> P[i];
	}

	// cout << P[0] << endl; // 0

	vector<int> dp(N+1);

	for (int i = 1; i <= N; i++) { // i개가 들어있는 카드팩 구매시 금액의 최댓값
		for (int j = 1; j <= i; j++) { // j개가 들어있는 카드팩 + 나머지 카드팩
			dp[i] = max(dp[i], P[j] + dp[i-j]);
		}
	}

	cout << dp[N] << endl;

	return 0;
}
