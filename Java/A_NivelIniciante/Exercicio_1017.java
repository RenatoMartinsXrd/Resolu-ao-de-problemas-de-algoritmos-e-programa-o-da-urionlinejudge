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
public class Exercicio1017 {

        public static void main(String[] args) {
      Scanner s = new Scanner(System.in);
        int horas = s.nextInt();
        int velocidade = s.nextInt();
        System.out.printf("%.3f\n",((velocidade / 12.0)* horas));  
    }
}
