#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef long long ll;

vi findPoint(vi pq) {
  vi p = {pq[0], pq[1]};
  vi q = {pq[2], pq[3]};
  vi pr = {0, 0};
  
  for(int i=0; i < q.size(); ++i) {
    q[i] = 2*q[i];
  }
  
  for(int i=0; i < pr.size(); ++i) {
    pr[i] = q[i] - p[i];
  }
  return pr;
}

int main(int argc, char *argv[]) {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin >> t;
  cin.ignore(numeric_limits<streamsize>::max(), '\n');

  for(int i=0; i < t; ++i) {
    vi pq;
    for(int i=0; i < 4; ++i) {
      int p;
      cin >> p;
      pq.push_back(p);
    }
    vi pr = findPoint(pq);

    for(auto pi: pr)
      cout << pi << " ";
    cout << "\n";
  }
  return 0;
}