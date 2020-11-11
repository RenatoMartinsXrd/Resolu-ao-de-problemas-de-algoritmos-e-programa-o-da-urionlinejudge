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
public class Exercicio_3040 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        for (int i = 0; i < n; i++) {
            String [] arvore = s.nextLine().split(" ");
            System.out.println(Integer.parseInt(arvore[0])>= 200 && Integer.parseInt(arvore[0]) <= 300 && Integer.parseInt(arvore[1]) * 1 >= 50 && Integer.parseInt(arvore[2]) * 1 >= 150 ? "Sim" : "Nao") ;   
        }

    }
}
