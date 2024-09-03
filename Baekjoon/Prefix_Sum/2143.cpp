#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T, n, m;
	cin >> T;

	cin >> n;
	vector<int> A(n);
	for (int i = 0; i < n; i++) {
		cin >> A[i];
	}

	cin >> m;
	vector<int> B(m);
	for (int i = 0; i < m; i++) {
		cin >> B[i];
	}

	vector<int> sumA;
	for (int s = 0; s < n; s++) {
		int sum = 0;
		for (int e = s; e < n; e++) {
			sum += A[e];
			sumA.push_back(sum);
		}
	}

	vector<int> sumB;
	for (int s = 0; s < m; s++) {
		int sum = 0;
		for (int e = s; e < m; e++) {
			sum += B[e];
			sumB.push_back(sum);
		}
	}

	sort(sumB.begin(), sumB.end());
	long long count = 0;

	for (size_t i = 0; i < sumA.size(); i++) {
		int temp = T - sumA[i];
		count += upper_bound(sumB.begin(), sumB.end(), temp) - lower_bound(sumB.begin(), sumB.end(), temp);
	}

	cout << count << endl;

	return 0;
}
