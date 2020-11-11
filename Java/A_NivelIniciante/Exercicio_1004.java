/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package A_NivelIniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 *
 * @author Scarlxrd2112
 */
public class Exercicio1004 {
    public static void main(String[] args) throws IOException {
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);
        int A, B, resultado;
        A = Integer.parseInt(in.readLine());
        B = Integer.parseInt(in.readLine());
        resultado = A * B;
        System.out.printf("PROD = %d\n", resultado);
    }
}
