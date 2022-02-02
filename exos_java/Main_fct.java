import java.util.*;
import java.math.BigInteger;

public class Main_fct
{
  public Main_fct()
  {

  }

  public static long fact( long n)
  {
    if( n==0 )
      return(1);
    else
    {
    long r = 1;
    for(long i = 1; i<= n; i++)
      r = r * i;

    return r ;



    }


  }
  public static boolean[] crible_eratos (int n)
  {
    boolean Tab[] = new boolean[n-1];
    if(n%2 == 0 ){
        for(int i = 0; i<(n-2); i+=2){
          Tab[i] = false;
          Tab[i+1] = true;
          }
      }
    else{
        for(int i = 0; i< n-1; i+=2){
          Tab[i] = false;
          Tab[i+1] = true;
          }
        Tab[n-2] = false;
        }
    Tab[0] = true;
    int c = 1;
    while(c < n-2){
      if(Tab[c]){
        for(int k = 2; k < n/(c+2); k+=2){
          Tab[c + k*(c+2)] = false;
        }
      }
      c+=1;
    }
    return Tab;

  }
  public static boolean palindrome ( String s)
  {

    if(s.equals(""))
      return(false);
    else{
      int n = s.length();
      for(int i = 0; i<n/2; i++){
        if(!(s.charAt(i) == s.charAt(n-1-i))){
          return(false);

      }
    }
    return(true);
  }
}
  public static boolean test_premier (long n)
  {
    if(n < 10){
      if( n == 2 || n==3 || n==5 || n==7)
        return true;
      else
        return false;
    }

    else{
      if(n%2==0)
        return false;
      else{
        for(long k = 3; k<= (long)Math.sqrt(n) +1; k+=2){
          if(n%k==0)
            return false;
        }
        return true;
      }
    }

  }
  public static boolean test_premier (int n)
  {
    if(n < 10){
      if( n == 2 || n==3 || n==5 || n==7)
        return true;
      else
        return false;
    }

    else{
      if(n%2==0)
        return false;
      else{
        for(int k = 3; k<= (int)Math.sqrt(n) +1; k+=2){
          if(n%k==0)
            return false;
        }
        return true;
      }
    }

  }
  public static HashMap<Integer,Integer> decomposition_facteur( int n, boolean[] Tab)
  {
    // il faut length Tab > sqrt(n) +1 !!!

    if(n==1){
      HashMap<Integer,Integer> dico = new HashMap<Integer,Integer>();
      dico.put(1,1);
      return dico;
    }
    else if(n==2){
      HashMap<Integer,Integer> dico = new HashMap<Integer,Integer>();
      dico.put(2,1);
      return dico;

    }
    else{
      HashMap<Integer,Integer> dico = new HashMap<Integer,Integer>();
      while(n>1){
          boolean bool = true;
          for(int k = 0; k< Tab.length;k++){
            if(Tab[k] && n%(k+2) == 0){
              bool = false;
              boolean getKey = dico.containsKey(k+2);
              if(getKey){
                int value = dico.get(k+2);
                dico.remove(k+2);
                dico.put(k+2,value+1);
              }
              else{
                dico.put(k+2,1);
                }
              n = n/(k+2);
              break;
              }
            }
            if(bool)
              {
                if(dico.containsKey(n)){
                  int value = dico.get(n);
                  dico.remove(n);
                  dico.put(n,value+1);
                }
                else{
                  dico.put(n,1);
                }
                n = 1;
              }
          }
          return dico;
        }
    }
  public static HashMap<Long,Long> decomposition_facteur( Long n, boolean[] Tab)// marche si sqrt(n) peut etre int ... donc n pas trop trop grand
  {
    // il faut length Tab > sqrt(n) +1 !!!

    if(n==1){
      HashMap<Long,Long> dico = new HashMap<Long,Long>();
      dico.put(1L,1L);
      return dico;
    }
    else if(n==2){
      HashMap<Long,Long> dico = new HashMap<Long,Long>();
      dico.put(2L,1L);
      return dico;

    }
    else{
      HashMap<Long,Long> dico = new HashMap<Long,Long>();
      while(n>1){
          boolean bool = true;
          for(int k = 0; k< Tab.length;k++){
            if(Tab[k] && n%(k+2) == 0){
              bool = false;
              boolean getKey = dico.containsKey((long)(k+2));
              if(getKey){
                long value = dico.get((long)(k+2));
                dico.remove((long)(k+2));
                dico.put((long)(k+2),value+1);
              }
              else{
                dico.put((long)(k+2),1L);
                }
              n = n/(k+2);
              break;
              }
            }
            if(bool)
              {
                if(dico.containsKey(n)){
                  long value = dico.get(n);
                  dico.remove(n);
                  dico.put(n,value+1);
                }
                else{
                  dico.put((long)n,1L);
                }
                n = 1L;
              }
          }
          return dico;
        }
    }
  public static int nombre_diviseurs(int n)
  {
    if(n==1)
      return 1;
    boolean [] crible = crible_eratos ((int)Math.sqrt(n) +1);
    HashMap<Integer, Integer> dico = decomposition_facteur( n, crible);
    int p = 1;
    for(Map.Entry element : dico.entrySet())
    {
      p *= (int)element.getValue() +1;

    }
    return p;
  }
  public static long nombre_diviseurs(long n)
  {
      if(n==1)
        return 1L;
      boolean [] crible = crible_eratos ((int)Math.sqrt(n) +1);
      HashMap<Long, Long> dico = decomposition_facteur( n, crible);
      Long p = 1L;
      for(Map.Entry element : dico.entrySet())
      {
        p *= (long)element.getValue() +1L;

      }
      return p;
  }
  // pareil avec crible en argument pour ne pas avoir à calculer plusieurs fois si plusieurs appels !!

  public static long nombre_diviseurs(long n, boolean [] crible) // long type avec crible
  {
      if(n==1)
        return 1L;
      HashMap<Long, Long> dico = decomposition_facteur( n, crible);
      Long p = 1L;
      for(Map.Entry element : dico.entrySet())
      {
        p *= (long)element.getValue() +1L;

      }
      return p;



  }
  public static int nombre_diviseurs(int n, boolean [] crible) // int avec crible
  {
    if(n==1)
      return 1;
    HashMap<Integer, Integer> dico = decomposition_facteur( n, crible);
    int p = 1;
    for(Map.Entry element : dico.entrySet())
    {
      p *= (int)element.getValue() +1;
    }
    return p;
  }
  public static BigInteger fact(int n)
    {
      BigInteger resultat = BigInteger.valueOf(1);
      if(n == 0 || n== 1)
        return 1;
      for(int i = 1; i<= n ; i++)
      {
        resultat = resultat.multiply(BigInteger.valueOf(i));
      }
      return resultat;
    }



}
