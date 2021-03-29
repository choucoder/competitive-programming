#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vl;
typedef set<ll> sl;

#define PB push_back

int nonDivisibleSubset(vl s, int k) {
  sl r;

  for(int i=0; i < s.size(); ++i) {
    for(int j=(i + 1); j < s.size(); ++j) {
      if (((s[i] + s[j]) % k) != 0) {
        r.insert(s[i]);
        r.insert(s[j]);
      }
    }
  }
  return r.size();
}

int main(int argc, char *argv[]) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n, k, si;
  vl s;
  cin >> n >> k;

  for (int i=0; i<n; ++i) {
    cin >> si;
    s.PB(si);
  }

  cout << nonDivisibleSubset(s, k) << "\n";
  return 0;
}