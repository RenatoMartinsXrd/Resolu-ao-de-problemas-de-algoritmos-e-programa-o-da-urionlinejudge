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
public class Exercicio1019 {
     public static void main(String[] args) {
         Scanner s = new Scanner(System.in);
         int segundosorigem = s.nextInt();
         int sobrasegundos = (segundosorigem - (segundosorigem / 60) * 60);
         int name = segundosorigem - sobrasegundos;
         int minutos = name / 60;
         int horas = minutos < 60 ? 0 : minutos / 60;
         minutos -= horas * 60;
         System.out.printf("%d:%d:%d\n", horas, minutos, sobrasegundos);
     
    }
}
