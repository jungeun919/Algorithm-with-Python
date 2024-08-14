#include <iostream>

using namespace std;

int calc(int M, int N, int x, int y) {
	int k = x;
	while (k <= M * N) {
		if ((k-y) % N == 0) {
			return k;
		}
		k += M;
	}
	return -1;
}

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		int M, N, x, y;
		cin >> M >> N >> x >> y;
		cout << calc(M, N, x, y) << endl;
	}
}
