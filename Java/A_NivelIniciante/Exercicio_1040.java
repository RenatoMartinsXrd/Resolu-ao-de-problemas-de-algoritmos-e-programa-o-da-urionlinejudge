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
public class Exercicio_1040 {

    public static void main(String[] args) {
        float N1, N2, N3, N4, media, exame, media_final;
        Scanner input = new Scanner(System.in);
        String [] ns = input.nextLine().split(" ");
        N1 = Float.parseFloat(ns[0]);
        N2 = Float.parseFloat(ns[1]);
        N3 = Float.parseFloat(ns[2]);
        N4 = Float.parseFloat(ns[3]);

        media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10;
        System.out.printf("Media: %.1f\n", media);
        if (media >= 7.0){
            System.out.print("Aluno aprovado.\n");

        } else if (media >= 5.0 && media <= 6.9) {
            System.out.print("Aluno em exame.\n");
            exame = Float.parseFloat(input.nextLine());
            System.out.printf("Nota do exame: %.1f\n", exame);
            media_final = (media + exame) / 2;

            if (media_final >= 5.0) {
                System.out.print("Aluno aprovado.\n");

            } else {
                System.out.print("Aluno reprovado.\n");

            }

            System.out.printf("Media final: %.1f\n", media_final);

        } else if (media < 5.0) {
            System.out.print("Aluno reprovado.\n");

        }

    }
}
