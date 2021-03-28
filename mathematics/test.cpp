#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef pair<int, int> pi;

#define F first
#define S second
#define PB push_back
#define MP make_pair


int main(int argc, char *argv[]) {
  int n = 10;
  vi numbers;
  for(int i=0; i < n; i++) {
    numbers.PB(i);
  }
  for (int i=0; i < numbers.size(); i++) {
    cout << numbers.at(i) << " ";
  }
  cout << "\n";
  return 0;
}