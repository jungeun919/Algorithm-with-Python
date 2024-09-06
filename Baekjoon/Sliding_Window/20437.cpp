#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;

	while (T--) {
		string W;
		cin >> W;
		int K;
		cin >> K;

		map<char, vector<int> > alpha_map; // {'문자': [등장인덱스1, 등장인덱스2, ...]}
		for (size_t i = 0; i < W.size(); i++) {
			alpha_map[W[i]].push_back(i);
		}

		vector<int> res;
		// for (const pair<char, vector<int> >& pair : alpha_map) {
		for (const auto& pair : alpha_map) {
			const vector<int>& idx_list = pair.second;

			if (idx_list.size() >= (size_t)K) {
				for (size_t i = 0; i < idx_list.size() - K + 1; i++) {
					res.push_back(idx_list[i+K-1] - idx_list[i] + 1);
				}
			}
		}

		if (!res.empty()) {
			cout << *min_element(res.begin(), res.end()) << " " << *max_element(res.begin(), res.end()) << endl;
		} else {
			cout << "-1" << endl;
		}
	}

	return 0;
}
