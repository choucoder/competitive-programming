#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef long long ll;

#define PB push_back


ll computeSum(ll n) {
  ll sum;
  sum = (n*(n - 1) / 2);
  return sum;
}


int main(int argc, char *argv[]) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  ll n;
  cin >> n;
  cin.ignore(numeric_limits<streamsize>::max(), '\n');
  
  ll sum;

  cout << "Sum: " << computeSum(n) << "\n";
  return 0;
}