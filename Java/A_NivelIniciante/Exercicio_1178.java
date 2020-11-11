package A_NivelIniciante;


import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Scarlxrd2112
 */
public class Exercicio_1178 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        float number = s.nextFloat();
        for (int i = 0; i <100; i++) {
            System.out.printf("N[%d] = %.4f\n",i,number);
            number = number/2;
        }
    }
}
