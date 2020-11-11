/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package A_Iniciante;

import java.util.Scanner;

/**
 *
 * @author Scarlxrd2112
 */
public class Exercicio_1047 {

    public static int abs(int n) {
        return n < 0 ? (n * -1) : n;
    }

    public static void main(String[] args) {
        int hora_inicial, hora_final, minuto_inicial, minuto_final, inicio, final1, res, resultado, hora = 0, minuto = 0;
        Scanner s = new Scanner(System.in);
        hora_inicial = s.nextInt();
        minuto_inicial = s.nextInt();
        hora_final = s.nextInt();
        minuto_final = s.nextInt();
        hora_inicial *= 60;
        hora_final *= 60;

        inicio = hora_inicial + minuto_inicial;
        final1 = hora_final + minuto_final;
        res = final1 - inicio;

        if (hora_inicial == hora_final) {
            res = (24 * 60);
            if (minuto_inicial > minuto_final) {
                res -= (minuto_inicial - minuto_final);
                hora = (res / 60);
                minuto = (res % 60);
            } else if (minuto_inicial < minuto_final) {
                res = 0 + (minuto_final - minuto_inicial);
                hora = (res / 60);
                minuto = (res % 60);
            } else {
                hora = (res / 60);
                minuto = (res % 60);
            }
        } else if (res > 0) {
            hora = (res / 60);
            minuto = (res % 60);
        } else if (res < 0) {
            resultado = (24 * 60) - abs(res);
            hora = (resultado / 60);
            minuto = (resultado % 60);
        }

        System.out.printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", hora, minuto);
    }
}
