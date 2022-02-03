import java.util.*;

public class Highly_divisible_triangular_number
{
  public static void main(String [] args)
  {


    /*long n = 1L;
    long k = 2L;
    long diviseurs = 0;

    while(diviseurs < 500L)

    {
      diviseurs = 0L;



      for( long i = 1L ; i < (long)Math.sqrt(n) +1 ; i++)
      {
        if( n%i == 0)
        {
          diviseurs +=1;
          if( i != n/i)
            {
            diviseurs +=1;
            }


        }
      }
      if(diviseurs >= 500L)
        {

        break;
        }
      System.out.println(n);
      n += k;
      k+=1; */  // marche aussi bien 


    long n = 1L;
    long k = 2L;
    boolean [] crible = Main_fct.crible_eratos(200000000);
    long nombre_diviseur = Main_fct.nombre_diviseurs(n, crible);
    while( nombre_diviseur < 500L)
    {
      n += k;

      nombre_diviseur = (long)Main_fct.nombre_diviseurs(n, crible);
      k += 1L;

    }
    System.out.println(n);
  }

 }
