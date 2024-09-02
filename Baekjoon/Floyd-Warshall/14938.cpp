#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;

int main() {
	int n, m, r;
	cin >> n >> m >> r;

	vector<int> items(n+1, 0);
	for (int i = 1; i <= n; i++) {
		cin >> items[i];
	}

	// graph = [[INF] * (n+1) for _ in range(n+1)]
	vector<vector<int> > graph(n+1, vector<int>(n+1, INF));
	for (int i = 1; i <= n; i++) {
		graph[i][i] = 0;
	}
	for (int i = 0; i < r; i++) {
		int a, b, l;
		cin >> a >> b >> l;
		graph[a][b] = l;
		graph[b][a] = l;
	}

	for (int k = 1; k <= n; k++) {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
			}
		}
	}

	int max_count = 0;
	for (int i = 1; i <= n; i++) {
		int count = 0;
		for (int j = 1; j <= n; j++) {
			if (graph[i][j] <= m) {
				count += items[j];
			}
		}
		max_count = max(max_count, count);
	}
	cout << max_count << endl;

	return 0;
}
