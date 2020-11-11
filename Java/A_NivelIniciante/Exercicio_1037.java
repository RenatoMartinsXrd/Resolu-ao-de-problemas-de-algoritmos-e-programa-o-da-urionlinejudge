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
public class Exercicio_1037 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        float a = s.nextFloat();
        if (a < 0 || a > 100) {
            System.out.println("Fora de intervalo");
        } else if (a >= 0 && a <= 25) {
            System.out.println("Intervalo [0,25]");
        } else if (a <= 50) {
            System.out.println("Intervalo (25,50]");
        } else if (a <= 75) {
            System.out.println("Intervalo (50,75]");
        } else if (a <= 100) {
            System.out.println("Intervalo (75,100]");
        }
    }
}
