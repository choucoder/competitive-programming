#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<unsigned long long> vll;

#define PB push_back

bool isPrime(int n) {
  if (n == 1) return false;

  for(int i=2; i <= (int)sqrt(n); ++i) {
    if(n % i == 0)
      return false;
  }
  return true;
}

unsigned long long mult(vll &factors) {
  unsigned long long prod = 1;
  unsigned long long b = 1;
  
  for(int i=0; i < factors.size(); ++i){
    prod *= factors[i];
    b = b * factors[i];
  }  
  return prod;
}

void printFactors(vll arr) {
  for (int i=0; i < arr.size(); ++i) {
    cout << " " << arr.at(i) <<"";
  }
  cout << "\n";
}

int solve(unsigned long long n) {
  int i = 1;
  int facts = 0;
  unsigned long long prod = 1;
  vll factors;

  while (prod <= n && i <= n) {
    if (isPrime(i)) {
      prod *= i;
      facts += 1;
      factors.PB(i);
    }
    i += 1;
  }
  while (mult(factors) > n) {
    factors.pop_back();
    facts = facts - 1;
  }
  return factors.size();
}

int main(int argc, char *argv[]) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int q;
  cin >> q;
  cin.ignore(numeric_limits<streamsize>::max(), '\n');

  for (int t=1; t <= q; ++t) {
    unsigned long long n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    cout << solve(n) << "\n";
  }

  return 0;
}