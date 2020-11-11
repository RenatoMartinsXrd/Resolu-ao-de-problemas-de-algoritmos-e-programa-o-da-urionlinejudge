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
public class Exercicio1010 {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);
        int A,B;
        float C, peca1,peca2,peca3;

        A = ler.nextInt();
        B = ler.nextInt();
        C = ler.nextFloat();
        
        peca1 = ler.nextInt();
        peca2 = ler.nextInt();
        peca3 = ler.nextFloat();
        
         float TOTAL = (B*C)+(peca2*peca3);
        System.out.printf("VALOR A PAGAR: R$ %.2f\n", TOTAL);
    }
}
