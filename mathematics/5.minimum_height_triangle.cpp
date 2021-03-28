/*Given integers b and a, find the smallest integer h,
such that there exists a triangle of height h, base b,
having an area of at least a*/

#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef long long ll;

#define PB push_back

int lowestTriangle(double b, double a) {
  return ceil((2 * a) / b);
}

int main(int argc, char *argv[]) {
  int b, a;
  cin >> b >> a;
  cout << lowestTriangle((double) b, (double) a) << "\n";
  return 0;
}