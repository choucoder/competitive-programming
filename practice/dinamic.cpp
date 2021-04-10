#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vl;
typedef vector<int> vi;

#define PB push_back

void printArray(vl arr) {
  for(int i=0; i < arr.size(); ++i) {
    cout << arr[i] << " ";
  }
  cout << "\n";
}

ll fibonnaci(ll n) {
  if (n <= 1)
    return n;
  else
    return fibonnaci(n - 1) + fibonnaci(n - 2);
}

ll fiboMemoization(ll n, vl &memo) {
  if (memo[n] != -1) return memo[n];
  
  if (n <= 1) {
    memo[n] = n;
    return n;
  }
  else {
    ll r = fiboMemoization(n - 1, memo) + fiboMemoization(n - 2, memo);
    memo[n] = r;
    return r;
  }
}

ll fiboLinearMemoize(ll n) {
  vl memo;
  memo.PB(0);
  memo.PB(1);

  for(int i=2; i <= n; ++i) {
    memo.PB(-1);
  }
  for(int i=2; i <= n; ++i) {
    memo[i] = memo[i - 1] + memo[i - 2];
  }
  return memo[n];
}

int main(int argc, char *argv[]) {
  //ios::sync_with_stdio(0);
  //cin.tie(0);

  ll n = 1000;
  vl memo;
  for(int i=0; i <= n; ++i) {
    memo.PB(-1);
  }
  cout << "Fibonnaci de " << n << " es: " << fiboMemoization(n, memo) << "\n";
  cout << "Linear Fibo " << n << " es: " << fiboLinearMemoize(n) << "\n";
  return 0;
}