#include <bits/stdc++.h>
using namespace std;
int dp[100010];
#define int long long int
#define append push_back
int func(int i, vector<int> &v){  // what value you get from 0 or -1 upto i, if you take
    //base case
    if (i==0) return dp[0]=v[i];
    else if (i<0) return 0;
    if (dp[i]!=-1) return dp[i];
    // picked v[i]
    int pick = v[i] + func(i-2, v);
    // not picking v[i]
    int npick = func(i-1, v);

    return dp[i] = max(npick, pick);
}
signed main(){
    int n=4;
    memset(dp, -1, sizeof(dp));
    vector<int> v={1, 2, 3, 1};
    for(auto &val: v) cin >> val;
    cout<<func(n-1, v)<<endl;
    return 0;
}
