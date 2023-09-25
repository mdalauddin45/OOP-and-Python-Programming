#include<bits/stdc++.h>
using namespace std;
void fib(int n){
    if (n <= 1)
        cout<< n;
   else cout<< fib(n - 1) + fib(n - 2)<<" "; 
}
int main()
{
    int t;
    cin>>t;
    
    return 0;
}