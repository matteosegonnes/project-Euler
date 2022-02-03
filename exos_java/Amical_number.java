import java.util.HashMap;
public class Amical_number
  {
    public static void main(String[] args)
      {
        String s = "25";
        Integer n = Integer.valueOf(s);
        System.out.println(n+1);
        HashMap<Long,Long> dico = new HashMap<Long,Long>();
        long somme = 0L;
        for ( long i = 1; i <= 10000; i++)
          {
            long amical = somme_diviseurs(i);
            long amical2 = somme_diviseurs(amical);
            if(i == amical2 && amical2 <= 10000 && !(dico.containsKey(i) ) && i != amical  )
              {
                somme += (i + amical);
                dico.put( i, 1L);
                dico.put( amical, 1L);
              }
          }
        System.out.println(somme);
      }
    public static long somme_diviseurs( long n)
      {
        long somme = 0L;
        long limit = (long)Math.sqrt(n);
        for( long i = 1L; i<= limit; i++)
          {
            if(n%i == 0)
              {
                somme += i;
                if (n/i != i && i!=1L)
                    somme +=n/i;
              }

          }
        return somme;
      }
  }
