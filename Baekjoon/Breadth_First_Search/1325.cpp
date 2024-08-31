#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int N, M;
vector<vector<int> > graph(10001);
vector<int> res(10001);

int bfs(int start) {
	queue<int> q;
	q.push(start);

	vector<bool> visited(N+1, false);
	visited[start] = true;

	int count = 0;
	while (!q.empty()) {
		int v = q.front();
		q.pop();

		for (int i : graph[v]) { // for i in graph[v]
			if (!visited[i]) {
				q.push(i);
				visited[i] = true;
				count += 1;
			}
		}
	}
	return count;
}

int main() {
	cin >> N >> M;

	graph.resize(N+1);
	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b; // a가 b를 신뢰
		graph[b].push_back(a);
	}

	res.resize(N+1);
	for (int i = 1; i <= N; i++) {
		res[i] = bfs(i);
	}

	// 두 수 비교 -> max(a, b)
	// 벡터에서의 최댓값 -> *max_element(범위)
	int max_val = *max_element(res.begin(), res.end());
	for (int i = 1; i <= N; i++) {
		if (res[i] == max_val) {
			cout << i << " ";
		}
	}

	return 0;
}
