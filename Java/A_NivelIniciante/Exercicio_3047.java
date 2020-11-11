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
public class Exercicio_3047 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int idade_mae = s.nextInt();
        int idade_filho1 = s.nextInt();
        int idade_filho2 = s.nextInt();
        int idade_filho3 = idade_mae - idade_filho1 - idade_filho2;
        System.out.println((idade_filho1 > idade_filho2 )? (idade_filho1 > idade_filho3) ? idade_filho1 :idade_filho3:(idade_filho2 > idade_filho3) ? idade_filho2 : idade_filho3);
    }
}
