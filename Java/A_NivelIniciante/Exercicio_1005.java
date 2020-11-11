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
public class Exercicio1005 {
    public static void main(String[] args) throws IOException {
        InputStreamReader ir = new InputStreamReader(System.in);
        BufferedReader in = new BufferedReader(ir);

        double A, B, r = 0;

        A = Double.parseDouble(in.readLine()) * 3.5;
        B = Double.parseDouble(in.readLine()) * 7.5;

        r = (A + B) / 11;
        System.out.printf("MEDIA = %.5f\n", r);
    }
}
