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
public class Exercicio_1847 {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        String[] linha = teclado.nextLine().split(" ");
        int A = Integer.parseInt(linha[0]);
        int B = Integer.parseInt(linha[1]);
        int C = Integer.parseInt(linha[2]);
        if (B < A) {
            if (C >= B) {
                System.out.println(":)");
            } else {
                int dia4 = A - B;
                int dia5 = B - C;
                if (dia5 < dia4) {
                    System.out.println(":)");
                } else {
                    System.out.println(":(");
                }
            }

        } else if (B > A) {
            if (C <= B) {
                System.out.println(":(");
            } else {
                int dia1 = B - A;
                int dia2 = C - B;
                if (dia2 < dia1) {
                    System.out.println(":(");
                } else {
                    System.out.println(":)");
                }
            }
        } else if (A == B && C > B) {
           System.out.println(":)");
        } else {
            System.out.println(":(");
        }
    }
}
