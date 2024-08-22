// 음수 * 음수 / 양수 * 양수
// 절댓값이 큰 수끼리 곱셈

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int n;
	cin >> n;

	vector<long long> pos;
	vector<long long> neg;
	int one = 0;
	int zero = 0;

	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		if (num > 1) {
			pos.push_back(num);
		} else if (num < 0) {
			neg.push_back(num);
		} else if (num == 1) {
			one += 1;
		} else {
			zero = 1;
		}
	}

	sort(pos.begin(), pos.end());
	sort(neg.rbegin(), neg.rend());
	// sort(neg.begin(), neg.end(), greater<int>());
	// sort(neg.begin(), neg.end());
	// reverse(neg.begin(), neg.end());

	long long total = 0;

	while (pos.size() >= 2) {
		long long a = pos.back();
		pos.pop_back();
		long long b= pos.back();
		pos.pop_back();
		total += a * b;
	}

	if (!pos.empty()) {
		total += pos.back();
		pos.pop_back();
	}

	while (neg.size() >= 2) {
		long long a = neg.back();
		neg.pop_back();
		long long b = neg.back();
		neg.pop_back();
		total += a * b;
	}

	if (!neg.empty() && zero == 0) {
		total += neg.back();
		neg.pop_back();
	}

	total += one;

	cout << total << endl;

	return 0;
}
