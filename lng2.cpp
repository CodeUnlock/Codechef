#include<bits/stdc++.h>
#include<iostream>
#include<stdio.h>
using namespace std;
void fs(int &number)
{
    bool negative = false;
    register int c;

    number = 0;
    c = getchar();
    if (c=='-')
    {
        negative = true;
        c = getchar();
    }
    for (; (c>47 && c<58); c=getchar())
        number = number *10 + c - 48;
    if (negative)
        number *= -1;
}
int main()
{
    int t,n,q,even=0,odd=0;
    int a[10000],p,k=0,d=0,rs2;
    long result,num=0;
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    fs(t);
    while(t--)
    {
        even=0;odd=0;rs2=0;
        fs(n);
        fs(q);
        for(int i=0;i<n;i++)
        {
            fs(a[i]);
        }
        while(q--)
        {
            even=0;
            odd=0;
            fs(p);
        for(int i=0;i<n;i++)
        {

            result=a[i]^p;
             bitset<2056>binary(result);
             bitset<2056>b1(binary);
             rs2=b1.count();
             if(rs2%2==0)
             {
                 even++;
             }
             else
                {
                odd++;
              }

             }
             
              printf("%d %d\n",even,odd);

    }
    }
}
