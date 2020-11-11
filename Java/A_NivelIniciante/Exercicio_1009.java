/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package A_NivelIniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

/**
 *
 * @author Scarlxrd2112
 */
public class Exercicio1009 {
    public static void main(String[] args) throws IOException {
                InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);
        Scanner ler = new Scanner(System.in);
        String A;
        double  B,C, r = 0;

        A = ler.next();
        B = ler.nextDouble();
        C = ler.nextDouble() * 0.15;
        r = B + C;
       
        System.out.printf("TOTAL = R$ %.2f\n", r);
    }
}
