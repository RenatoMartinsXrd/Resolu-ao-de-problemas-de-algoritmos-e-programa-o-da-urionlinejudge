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
public class Exercicio1015 {
        public static void main(String[] args) {
       Scanner s = new Scanner(System.in);
        float x1 = s.nextFloat(); 
        float y1 = s.nextFloat();
        float x2 = s.nextFloat();
        float y2 = s.nextFloat();

        System.out.printf("%.4f\n",Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2)));
    }
}
