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
public class Exercicio_1021 {
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);

    double notas[] = {100.0, 50.0, 20.0, 10.0, 5.0, 2.0};
    double moedas[] = {1.0, 0.50, 0.25, 0.10, 0.05, 0.01};
    String [] valoresString = {"100.00","50.00","20.00","10.00","5.00","2.00","1.00","0.50","0.25","0.10","0.05","0.01"};
    int qtdNota, qtdMoeda;

    double valor = sc.nextDouble();
    valor = (valor * 100) + 0.05;

    System.out.println("NOTAS:");
    for (int i = 0; i < notas.length; i++) {
        double nota = notas[i] * 100;
        qtdNota = (int) (valor / nota);
        valor %= nota;
        System.out.printf("%d nota(s) de R$ %.2f%n", qtdNota, nota);
    }

    System.out.println("MOEDAS:");
    for (int i = 0; i < moedas.length; i++) {
        double moeda = moedas[i];
        qtdMoeda = (int) (valor / (moeda * 100));
        valor %= moeda * 100;
        System.out.printf("%d moeda(s) de R$ %.2f%n", qtdMoeda, moeda);
    }
    }
}
