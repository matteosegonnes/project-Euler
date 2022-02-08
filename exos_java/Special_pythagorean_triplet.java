public class Special_pythagorean_triplet {

  public static void main(String[] args){

    for(int a = 1; a < 1000; a++){
      for(int b = 1; b < 1000-a; b++){
        int c_carre = (int)Math.pow(a,2) + (int)Math.pow(b,2);
        int c = (int)Math.sqrt(c_carre);
        if(((int)Math.pow(c,2) == c_carre) && (a + b + c == 1000))
          System.out.println(a*b*c); //va donc apparaitre 2 fois avec a,b = b,a
      }
    }
  }
}
