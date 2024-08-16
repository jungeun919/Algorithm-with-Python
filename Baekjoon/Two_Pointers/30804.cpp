#include <iostream>
#include <vector>
#include <algorithm> // max

using namespace std;

int main() {
	int N;
	cin >> N;

	vector<int> fruit(N);
	for (int i = 0; i < N; i++) {
		cin >> fruit[i];
	}

	vector<int> counter(10 ,0);
	int left = 0, right = 0;
	int kind = 0;
	int max_count = 0;

	while (right < N) {
		if (counter[fruit[right]] == 0) {
			kind += 1;
		}
		counter[fruit[right]] += 1;
		right += 1;

		if (kind > 2) {
			counter[fruit[left]] -= 1;
			if (counter[fruit[left]] == 0) {
				kind -= 1;
			}
			left += 1;
		}

		max_count = max(max_count, right - left);
	}

	cout << max_count << endl;

	return 0;
}
