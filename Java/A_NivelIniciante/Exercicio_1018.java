/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package A_NivelIniciante;

import java.util.Scanner;

/**
 *
 * @author Scarlxrd2112
 */
public class Exercicio1018 {
    public static void main(String[] args) {
         Scanner s = new Scanner(System.in);
        int grana = s.nextInt();
     //   System.out.println(grana/100);
        System.out.printf("%d\n",grana);
        System.out.printf("%d nota(s) de R$ 100,00\n",grana/100);
        grana = grana - ((grana/100)*100);
        System.out.printf("%d nota(s) de R$ 50,00\n",grana/50);
        grana = grana - ((grana/50)*50);
        System.out.printf("%d nota(s) de R$ 20,00\n",grana/20);
        grana = grana - ((grana/20)*20);
        System.out.printf("%d nota(s) de R$ 10,00\n",grana/10); 
         grana = grana - ((grana/10)*10);
        System.out.printf("%d nota(s) de R$ 5,00\n",grana/5);
         grana = grana - ((grana/5)*5);
        System.out.printf("%d nota(s) de R$ 2,00\n",grana/2);
        grana = grana - ((grana/2)*2);
        System.out.printf("%d nota(s) de R$ 1,00\n",grana/1);
    }
}
