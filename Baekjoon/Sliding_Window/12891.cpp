#include <iostream>
#include <map>

using namespace std;

int S, P;
string word;
int A, C, G, T;
map<char, int> curr_dict;

bool check_valid() {
	if (curr_dict['A'] < A) return false;
	if (curr_dict['C'] < C) return false;
	if (curr_dict['G'] < G) return false;
	if (curr_dict['T'] < T) return false;
	return true;
}

int main() {
	cin >> S >> P;
	cin >> word;
	cin >> A >> C >> G >> T;

	curr_dict['A'] = 0;
	curr_dict['C'] = 0;
	curr_dict['G'] = 0;
	curr_dict['T'] = 0;

	int count = 0;

	for (int i = 0; i < P; i++) { // 초기 윈도우
		curr_dict[word[i]] += 1;
	}
	if (check_valid() == true) {
		count += 1;
	}

	for (int i = P; i < S; i++) {
		curr_dict[word[i - P]] -= 1;
		curr_dict[word[i]] += 1;
		if (check_valid() == true) {
			count += 1;
		}
	}

	cout << count << endl;

	return 0;
}
