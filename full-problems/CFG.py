/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class SieveOfErat
{
    boolean[] sieveOfErat(int n)
    {
        boolean prime[] = new boolean[n+1];
        for(int i=0;i<n;i++)
            prime[i] = true;
         
        for(int p = 2; p*p <=n; p++)
        {
            if(prime[p] == true)
            {
                for(int i = p*2; i <= n; i += p)
                    prime[i] = false;
            }
        }
         
    return primes
    }
     

class GFG {
	public static void main (String[] args) {
	    SieveOfErat ss = new SieveOfErat()
	    boolean primes[] = new boolean[1000001];
	    primes = ss.sieveOfErat(l)
		Scanner s= new Scanner(system.in);
		int t = s.nextInt();
		for (int q=0; q<t; q++){
		    for (i=0; i<2; i++){
		        l = s.nextInt()
		        r = s.nextInt()
		    }
		}
		
		
	}
}