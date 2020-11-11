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
public class Exercicio_1041 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String [] ns = input.nextLine().split(" ");
        float x = Float.parseFloat(ns[0]);
        float y = Float.parseFloat(ns[1]);
        if (x > 0 && y > 0) {
            System.out.println("Q1");
        } else if (x == 0 && y == 0) {
            System.out.println("Origem");
        } else if (x < 0 && y > 0) {
            System.out.println("Q2");
        } else if (x < 0 && y < 0) {
            System.out.println("Q3");
        } else if (x > 0 && y < 0) {
            System.out.println("Q4");
        } else if (x == 0 && y < 0 || y > 0) {
            System.out.println("Eixo Y");
        } else if (y == 0 && x < 0 || x > 0) {
            System.out.println("Eixo X");
        }
    }
}
