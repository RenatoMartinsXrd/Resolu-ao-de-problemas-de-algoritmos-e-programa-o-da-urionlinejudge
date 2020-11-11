/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package A_NivelIniciante;

import java.util.Scanner;
import java.util.Random;
/**
 *
 * @author Scarlxrd2112
 */
public class Exercicio1011 {
    public static void main(String[] args) {
         Scanner s = new Scanner(System.in);
         float a = s.nextFloat();
       System.out.printf("VOLUME = %.3f\n", (4 * 3.14159 * Math.pow(a, 3.0)) / 3);
    }
}
