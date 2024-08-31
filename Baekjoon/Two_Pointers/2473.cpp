#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath> // abs

using namespace std;

int main() {
	int n;
	cin >> n;

	vector<int> nums(n);
	for (int i = 0; i < n; i++) {
		cin >> nums[i];
	}

	sort(nums.begin(), nums.end());

	long long res_sum = 3000000000LL;
	vector<int> res_num(3); // fix, left, right

	for (int i = 0; i < n - 2; i++) {
		long long fix = nums[i];
		long long left = i + 1;
		long long right = n - 1;

		while (left < right) {
			long long temp = fix + nums[left] + nums[right];
			if (abs(temp) < res_sum) {
				res_sum = abs(temp);
				res_num[0] = fix;
				res_num[1] = nums[left];
				res_num[2] = nums[right];

				if (temp == 0) {
					break;
				}
			}

			if (temp < 0) {
				left += 1;
			} else {
				right -= 1;
			}
		}
	}

	cout << res_num[0] << " " << res_num[1] << " " << res_num[2] << endl;

	return 0;
}
