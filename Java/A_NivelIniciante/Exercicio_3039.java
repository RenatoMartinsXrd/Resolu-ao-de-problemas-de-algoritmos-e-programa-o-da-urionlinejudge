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
public class Exercicio_3039 {
    public static void main(String[] args) {
         Scanner s = new Scanner(System.in);
         int criancas = s.nextInt();
         int m = 0;
         int f = 0;
         s.nextLine();
         for (int i = 0; i < criancas; i++) {
            String str = s.nextLine();
             
            if(str.endsWith("M")){
                m+=1;
            }else{
                f+=1; 
            }
        }
        System.out.printf("%d carrinhos\n",m);
        System.out.printf("%d bonecas\n",f);
    }
}
