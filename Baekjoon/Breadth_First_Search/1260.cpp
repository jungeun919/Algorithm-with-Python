#include <iostream>
#include <vector>
#include <queue>
#include <algorithm> // sort
#include <string.h> // memset

using namespace std;

int n, m, v;
vector<int> graph[1001];
bool visited[1001];

void dfs(int v) {
	visited[v] = true;
	cout << v << " ";

	for (int i = 0; i < graph[v].size(); i++) {
		int next = graph[v][i];
		if (!visited[next]) {
			dfs(next);
		}
	}
}

void bfs(int v) {
	queue<int> q;

	q.push(v);
	visited[v] = true;
	cout << v << " ";

	while (!q.empty()) {
		v = q.front();
		q.pop();

		for (int i = 0; i < graph[v].size(); i++) {
			int next = graph[v][i];
			if (!visited[next]) {
				q.push(next);
				visited[next] = true;
				cout << next << " ";
			}
		}
	}
}

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> n >> m >> v;

	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}

	for (int i = 1; i <= n; i++) {
		sort(graph[i].begin(), graph[i].end());
	}

	dfs(v);

	cout << endl;
	memset(visited, 0, sizeof(visited));

	bfs(v);

	return 0;
}
