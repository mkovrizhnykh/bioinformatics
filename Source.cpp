#include<vector>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int main() {
	std::ifstream in("C:/Users/lumpofsugar/Downloads/input.txt");
	vector <char> let,inp;
	vector<int> num,sum,final;
	string line;
	char iinp, llet;
	int nnum, ssum = 0;
	for (int i = 3; i >= 0; i--) {
		cin >> iinp;
		inp.push_back(iinp);
	}

	if (in.is_open())
	{
		while (getline(in, line)) {
			istringstream iss(line);
			iss >> llet >> nnum;
			let.push_back(llet);
			num.push_back(nnum);
		} in.close();
	} else {

		cout << "We Havet file";
	}
	sort(sum.begin(), sum.end());
	for (int i = 0; i < let.size(); i++) {
		if ((let[i] == inp[0]) || (let[i] == inp[1]) || (let[i] == inp[2]) || (let[i] == inp[3])) sum.push_back(num[i]);
	}

	for (int i = 4; i >= 0; i--) {
		if (i == 4) {
			cout << ssum <<" ";
		} if (i == 3) {
			for (int j = 0; j < sum.size();j++)
			cout << sum[j] << " ";
		} if (i == 2) {
			final.push_back(sum[0] + sum[1]);
			final.push_back(sum[1] + sum[2]);
			final.push_back(sum[2] + sum[3]);
			final.push_back(sum[0] + sum[3]);
			sort(final.begin(), final.end());
			for (int j = 0; j < final.size(); j++)
					cout << final[j] << " ";
			final.clear();
		} if (i == 1) {
			final.push_back(sum[0] + sum[1] + sum[2]);
			final.push_back(sum[1] + sum[2] + sum[3]);
			final.push_back(sum[2] + sum[3] + sum[0]);
			final.push_back(sum[3] + sum[0] + sum[1]);
			sort(final.begin(), final.end());
			for (int j = 0; j < final.size(); j++)
				cout << final[j] << " ";
			final.clear();
		} if (i == 0) {
			cout << sum[0] + sum[1] + sum[2] + sum[3] << " ";
		}
	}
	system("pause");
	return 0;
}
