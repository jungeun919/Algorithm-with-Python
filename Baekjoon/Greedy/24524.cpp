#include <iostream>
#include <vector>

using namespace std;

int main() {
	string S, T;
	cin >> S >> T;

	vector<int> counter(T.size()); // i번째까지 완성된 문자 개수

	for (char s : S) {
		size_t idx = T.find(s);
		if (idx == string::npos) { // if s in T
			continue;
		}

		if (s == T[0]) {
			counter[0] += 1;
		} else if (idx != string::npos) {
			if (counter[idx - 1] > 0) {
				counter[idx - 1] -= 1;
				counter[idx] += 1;
			}
		}
	}

	cout << counter.back() << endl; // 마지막 요소

	return 0;
}
