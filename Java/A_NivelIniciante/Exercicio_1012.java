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
public class Exercicio1012 {

    public static void main(String[] args) {
// a) a área do triângulo retângulo que tem A por base e C por altura. 
//b) a área do círculo de raio C. (pi = 3.14159) 
//c) a área do trapézio que tem A e B por bases e C por altura. 
//d) a área do quadrado que tem lado B. 
//e) a área do retângulo que tem lados A e B.       
        float A, B, C;
        Scanner s = new Scanner(System.in);
        A = s.nextFloat();
        B = s.nextFloat();
        C = s.nextFloat();
        System.out.printf("TRIANGULO: %.3f\n", A * C / 2);
        System.out.printf("CIRCULO: %.3f\n", 3.14159 * Math.pow(C, 2));
        System.out.printf("TRAPEZIO: %.3f\n", ((A + B) / 2) * C);
        System.out.printf("QUADRADO: %.3f\n", Math.pow(B, 2));
        System.out.printf("RETANGULO: %.3f\n", A * B);
    }
}
