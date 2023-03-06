#define  fastio         ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#include <bits/stdc++.h>
#include <iomanip>
#define  all(x)                      x.begin(),x.end()
  using namespace std;
    int main(){
      int t;
      cin >> t;
      while(t--){
         int n, a,b,c,d;
         cin >> n;
         int arr[n];
         for(int i=0; i<n; i++){
            cin >> arr[i];
         }
         sort(arr,arr+n);
         int ans=arr[n-1]/arr[0];
         cout<<ans<<endl;
      }

   return 0;
   }
