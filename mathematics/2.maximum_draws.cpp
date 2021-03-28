#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef long long ll;

int maximumDraws(int n) {
  return n + 1;
}

int main(int argc, char *argv[]) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin >> t;
  cin.ignore(numeric_limits<streamsize>::max(), '\n');

  for(int c=0; c < t; c++) {
    int n;
    cin >> n;
    cout << maximumDraws(n) << "\n";
  }
  return 0;
}