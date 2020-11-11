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


public class Exercicio_3065 {
    static int total = 0;
    static String juntaNumero = "";
    static char [] expressao = {};
    static String sinalAnterior = "+";
            public static void soma(int i){
             total += Integer.parseInt(juntaNumero);
                sinalAnterior = String.valueOf(expressao[i]);
                juntaNumero = "";    
            }
            
            
            public static void subtrair(int i){
                total -= Integer.parseInt(juntaNumero);
                 sinalAnterior = String.valueOf(expressao[i]);
                juntaNumero = "";     
            }
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
       
        int contador = 0;
        while (true) {
            total = 0;
            contador += 1;
            int qtdNumeros = s.nextInt();
            if (qtdNumeros == 0) {
                break;
            }
            s.nextLine();
            expressao = (s.nextLine() + "+").toCharArray();

            for (int i = 0; i < expressao.length; i++) {
                if (expressao[i] != '+' && expressao[i] != '-') {
                    juntaNumero += expressao[i];
                } else if ("+".equals(sinalAnterior)) {
                    soma(i);
                } else if ("-".equals(sinalAnterior)) {
                    subtrair(i);
                }
            }
            System.out.println("Teste " + contador);
            System.out.println(total);
            System.out.println();
        }
    }
}
