#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N, X;
	cin >> N >> X;

	vector<int> visitor(N);
	for (int i = 0; i < N; i++) {
		cin >> visitor[i];
	}

	if (*max_element(visitor.begin(), visitor.end()) == 0) {
		cout << "SAD" << endl;
	} else {
		int curr_visitor = 0;
		for (int i = 0; i < X; i++) {
			curr_visitor += visitor[i];
		}
		int max_visitor = curr_visitor;
		int count = 1;

		// i-X+1 ... i -> 개수: i-(i-X+1)+1 = X
		for (int i = X; i < N; i++) {
			curr_visitor -= visitor[i - X];
			curr_visitor += visitor[i];

			if (curr_visitor > max_visitor) {
				max_visitor = curr_visitor;
				count = 1;
			} else if (curr_visitor == max_visitor) {
				count += 1;
			}
		}

		cout << max_visitor << endl;
		cout << count << endl;
	}

	return 0;
}
