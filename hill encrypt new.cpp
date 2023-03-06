#include<bits/stdc++.h>
using namespace std ;

int key[3][3];

int mod(int x)
{
	return x >= 0 ? (x%26) : 26-(abs(x)%26) ;
}

void multiply_Matrices(int a[1000][3] , int a_rows , int a_cols ,  int b[1000][3] , int b_rows , int b_cols , int res[1000][3])
{
	for(int i=0 ; i < a_rows ; i++)
	{
		for(int j=0 ; j < b_cols ; j++)
		{
			for(int k=0 ; k < b_rows ; k++)
			{
				res[i][j] += a[i][k]*b[k][j] ;
			}
			res[i][j] = mod(res[i][j]) ;
		}
	}
}

string encrypt(string pt, int n)
{
	int P[1000][3] = {0} ;
	int C[1000][3] = {0} ;
	int ptIter = 0  ;

	while(pt.length()%n != 0)
	{
		pt += "x" ;
	}
	int row = (pt.length())/n;

	for(int i=0; i<row ; i++)
	{
		for(int j=0; j<n; j++)
		{
			P[i][j] = pt[ptIter++]-'a' ;
		}
	}


	multiply_Matrices(P, row , n , key , n , n , C) ;

	string ct = "" ;
	for(int i=0 ; i<row ; i++)
	{
		for(int j=0 ; j<n ;j++)
		{
			ct += (C[i][j] + 'a');
		}
	}
	return ct ;
}


int main()
{
	string msg ;
	int n=3 ;

	cout << "Enter the text to be encrypted    : " ;
	cin >> msg;

	cout << "Enter 3x3 matrix for key (It should be inversible):\n";
	cout<<"Enter key matrix: " <<endl;
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<n; j++)
		{
			cin >> key[i][j];
		}
	}

	string ct = encrypt(msg, n) ;
	cout << "Encrypted text : " << ct << endl;

	return 0;
}
