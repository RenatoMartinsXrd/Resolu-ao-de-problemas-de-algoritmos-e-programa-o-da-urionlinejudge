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
public class Exercicio_3037 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        s.nextLine();
        for (int i = 0; i < n; i++) {
            int total1 = 0;
            int total2 = 0;
            for (int z = 0; z < 3; z++) {
                String [] lancamento = s.nextLine().split((" "));
                total1 += Integer.parseInt(lancamento[0])* Integer.parseInt(lancamento[1]);
            }
            for (int z = 0; z < 3; z++) {
                String [] lancamento = s.nextLine().split((" "));
                total2 += Integer.parseInt(lancamento[0])* Integer.parseInt(lancamento[1]);
            }
            System.out.println(total1 > total2 ? "JOAO" : "MARIA");
        }
    }
}
