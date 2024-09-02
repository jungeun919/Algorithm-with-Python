#include <iostream>
#include <queue>

using namespace std;

int main() {
	int n, w, L;
	cin >> n >> w >> L;

	queue<int> trucks;
	for (int i = 0; i < n; i++) {
		int truck;
		cin >> truck;
		trucks.push(truck);
	}

	queue<int> bridge;
	for (int i = 0; i < w; i++) {
		bridge.push(0);
	}

	int curr_weight = 0;
	int time = 0;

	while (!bridge.empty()) {
		curr_weight -= bridge.front();
		bridge.pop();

		if (!trucks.empty()) {
			if (curr_weight + trucks.front() <= L) {
				int next = trucks.front();
				bridge.push(next);
				curr_weight += next;
				trucks.pop();
			} else {
				bridge.push(0);
			}
		}

		time += 1;
	}

	cout << time << endl;

	return 0;
}
