#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

#define PB push_back

int gameWithCells(int n, int m) {
  int mp;

  if (n % 2 == 0 && m % 2 == 0) {
    mp = (n * m) / 4;
  }
  else if (n % 2 != 0 && m % 2 != 0) {
    mp = ((n - 1) * (m - 1) / 4) + (n / 2) + (m / 2) + 1;
  }
  else if (n % 2 == 0 && m % 2 != 0) {
    mp = (n * (m - 1)) / 4 + (n / 2);
  }
  else{
    mp = ((n - 1) * m) / 4 + (m / 2);
  }
  return mp;
}

int main(int argc, char *argv[]) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  freopen("testset1.in", "r", stdin);

  int n, m;
  cin >> n >> m;
  cout << gameWithCells(n, m) << "\n";

  return 0;
}