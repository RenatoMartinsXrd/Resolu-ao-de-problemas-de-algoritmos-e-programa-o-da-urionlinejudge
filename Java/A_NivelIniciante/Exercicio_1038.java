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
public class Exercicio_1038 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String [] ns = input.nextLine().split(" ");
        int cod_produto = Integer.parseInt(ns[0]);
        int qtd = Integer.parseInt(ns[1]);
        double [] precos = {4.00,4.50,5.00,2.00,1.50};
        System.out.printf("Total: R$ %.2f\n",precos[cod_produto-1] * qtd);
    }
}
