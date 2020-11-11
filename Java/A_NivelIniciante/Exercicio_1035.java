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
public class Exercicio_1035 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String [] split = sc.nextLine().split(" ");
        int A = Integer.parseInt(split[0]);
        int B = Integer.parseInt(split[1]);
        int C = Integer.parseInt(split[2]);
        int D = Integer.parseInt(split[3]);
        if(B>C && D>A && C+D>A+B && C>0 && D>0 && A%2==0){
            System.out.println("Valores aceitos");
        }else{
            System.out.println("Valores nao aceitos");
        }
    }
}
