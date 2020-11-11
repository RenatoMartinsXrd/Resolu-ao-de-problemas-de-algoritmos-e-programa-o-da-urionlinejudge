/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package A_NivelIniciante;

import static java.util.Arrays.asList;
import java.util.List;
import java.util.Scanner;

/**
 *
 * @author Scarlxrd2112
 */
public class Exercicio1013 {
  
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        List<Integer> lista = asList(s.nextInt(),s.nextInt(),s.nextInt()); 
        int get = lista.stream().max((x ,y)->x.compareTo(y)).get();
        System.out.printf("%d eh o maior\n", get);
    }
}
