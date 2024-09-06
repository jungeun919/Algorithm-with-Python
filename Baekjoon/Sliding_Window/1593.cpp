#include <iostream>
#include <map>

using namespace std;

int main() {
	int w_len, s_len;
	cin >> w_len >> s_len;

	string W, S;
	cin >> W >> S;

	map<char, int> W_dict;
	map<char, int> S_dict;

	for (int i = 0; i < w_len; i++) {
		W_dict[W[i]] += 1; // 자동으로 초기값 0 설정
	}

	int start = 0;
	int count = 0;

	for (int i = 0; i < s_len; i++) {
		S_dict[S[i]] += 1;

		if (i >= w_len - 1){
			if (W_dict == S_dict) {
				count += 1;
			}

			S_dict[S[start]] -= 1;
			if (S_dict[S[start]] == 0) {
				S_dict.erase(S[start]);
			}
			start += 1;
		}
	}

	cout << count << endl;

	return 0;
}
