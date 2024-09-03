#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N, M;
	
	cin >> N;
	vector<int> A(N);
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}

	cin >> M;
	vector<int> B(M);
	for (int i = 0; i < M; i++) {
		cin >> B[i];
	}

	vector<int> arr;

	while (!A.empty() && !B.empty()) {
		int maxA = *max_element(A.begin(), A.end());
		int maxB = *max_element(B.begin(), B.end());
		int maxIdxA = max_element(A.begin(), A.end()) - A.begin();
		int maxIdxB = max_element(B.begin(), B.end()) - B.begin();

		if (maxA == maxB) {
			arr.push_back(maxA);
			A.erase(A.begin(), A.begin() + maxIdxA + 1);
			B.erase(B.begin(), B.begin() + maxIdxB + 1);
		} else if (maxA > maxB) {
			A.erase(A.begin() + maxIdxA);
		} else {
			B.erase(B.begin() + maxIdxB);
		}
	}

	if (!arr.empty()) {
		cout << arr.size() << endl;
		for (size_t i = 0; i < arr.size(); i++) {
			cout << arr[i] << " ";
		}
		cout << endl;
	} else {
		cout << "0" << endl;
	}
	
	return 0;
}
