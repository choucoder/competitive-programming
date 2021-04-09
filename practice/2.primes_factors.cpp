#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef long long ll;

#define PB push_back

vi getPrimesFactors(int n) {
  vi factors;

  while (n % 2 == 0) {
    n = n / 2;
    factors.PB(2);
  }

  for(int i=3; i < sqrt(n); i = i + 2) {
    while (n % i == 0) {
      n = n / i;
      factors.PB(i);
    }
  }

  if (n > 2)
    factors.PB(n);
  
  for(auto i: factors)
    cout << i << " ";

  return factors;
}

int main(int argc, char *argv[]) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n = 315;
  vi result = getPrimesFactors(n);
  return 0;
}