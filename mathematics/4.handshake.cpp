#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int hanshake(int n) {
  int sum = 0;
  for(int i=1; i <= n; ++i) {
    sum += (n - i);
  }
  return sum;
}

int main(int argc, char *argv[]) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  int cases;
  cin >> cases;
  cin.ignore(numeric_limits<streamsize>::max(), '\n');

  for(int t=1; t <= cases; ++t) {
    int n;
    cin >> n;
    cout << hanshake(n) << "\n";
  }

  return 0;
}