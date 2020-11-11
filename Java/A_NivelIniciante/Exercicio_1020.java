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
public class Exercicio_1020 {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       int s = sc.nextInt();
        System.out.println((int)(s/365) + " ano(s)\n" + s%365/30 + " mes(es)\n" + s%365%30 + " dia(s)");
}
}
