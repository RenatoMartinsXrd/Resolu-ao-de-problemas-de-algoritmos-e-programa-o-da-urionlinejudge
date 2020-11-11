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
public class Exercicio_1036 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String linha = s.nextLine();
        String [] linha2 = linha.split(" ");
        double A = Double.parseDouble(linha2[0]);
        double B = Double.parseDouble(linha2[1]);
        double C = Double.parseDouble(linha2[2]);
        double delta = (Math.pow(B, 2)- (4 * A * C));
        if ((A != 0) && (delta > 0)) {
            double raiz = 1/2;
            System.out.printf("R1 = %.5f\n",(-B + Math.sqrt(delta))/(2*A));
            System.out.printf("R2 = %.5f\n",(-B - Math.sqrt(delta))/(2*A));
        } else {
            System.out.println("Impossivel calcular");
        }
    }
}
