#include <iostream>
#include <vector>

using namespace std;

int n, m;
vector<int> graph[101];
bool visited[101] = {0, };
int cnt = 0;

int dfs(int v) {
	visited[v] = 1;

	for (int i = 0; i < graph[v].size(); i++) {
		int next = graph[v][i];
		if (!visited[next]) {
			dfs(next);
			cnt += 1;
		}
	}

	return cnt;
}

int main() {
	cin >> n >> m;

	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}

	cout << dfs(1) << endl;

	return 0;
}

/*
#include <iostream>
#include <queue>

using namespace std;

int n, m; // 노드 수, 간선 수
int graph[101][101];
// bool visited[101]; // 초기화되지 않음 (undefined value)
bool visited[101] = {0, }; // 모두 0(false)으로 초기화

int bfs(int start) {
	queue<int> q;
	int count = 0;

	q.push(start);
	visited[start] = 1;

	while (!q.empty()) {
		int v = q.front();
		q.pop();

		for (int i = 1; i <= n; i++) {
			if (!visited[i]) {
				if (graph[v][i] == 1) {
					q.push(i);
					visited[i] = 1;
					count += 1;
				}
			}
		}
	}

	return count;
}

int main() {
	cin >> n >> m;

	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		graph[a][b] = 1;
		graph[b][a] = 1;
	}

	cout << bfs(1) << endl;

	return 0;
}
*/
