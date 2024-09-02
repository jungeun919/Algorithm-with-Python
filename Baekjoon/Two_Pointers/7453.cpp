#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int n;
	cin >> n;

	vector<int> A(n), B(n), C(n), D(n);
	for (int i = 0; i < n; i++) {
		cin >> A[i] >> B[i] >> C[i] >> D[i];
	}

	vector<int> AplusB, CplusD;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			AplusB.push_back(A[i] + B[j]);
			CplusD.push_back(C[i] + D[j]);
		}
	}

	sort(AplusB.begin(), AplusB.end());
	sort(CplusD.begin(), CplusD.end());

	int left = 0;
	int right = CplusD.size() - 1;
	long long res = 0;

	while (left < AplusB.size() && right >= 0) {
		long long temp = AplusB[left] + CplusD[right];
		if (temp < 0) {
			left += 1;
		} else if (temp > 0) {
			right -= 1;
		} else {
			long long checkAB = 1; // 중복
			while (left + checkAB < AplusB.size() && AplusB[left] == AplusB[left + checkAB]) {
				checkAB += 1;
			}

			long long checkCD = 1; // 중복
			while (right - checkCD >= 0 && CplusD[right] == CplusD[right - checkCD]) {
				checkCD += 1;
			}

			res += checkAB * checkCD;
			left += checkAB;
			right -= checkCD;
		}
	}

	cout << res << endl;

	return 0;
}
