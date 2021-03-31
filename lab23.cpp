#include <iostream>

using namespace std;

int main()
{
	int peptide = 0;
	int subpeptide = 0;

	cin >> peptide;

	subpeptide = peptide*(peptide - 1);

	cout << subpeptide;
}
