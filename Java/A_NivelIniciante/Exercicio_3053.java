/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package A_NivelIniciante;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 *
 * @author Scarlxrd2112
 */
public class Exercicio_3053 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        Map<String, Integer> atual = new HashMap<String, Integer>();
                atual.put("A", 0); 
        atual.put("B", 0); 
        atual.put("C", 0); 
        s.nextLine();
        String letra = s.next();
        atual.put(letra,1);
        String local = letra;
        for(int i = 0; i < n; i++) {
	int movimento = s.nextInt();
        if (atual.get("A") == 1) {
            switch (movimento) {
                case 1:
                    atual.put("B", 1); 
                    atual.put("A", 0); 
                    local = "B";
                    break;
                case 2:
                    continue;
                case 3:
                    atual.put("C", 1); 
                    atual.put("A", 0); 
                    local = "C";
                    break;
                default:
                    break;
            }
        } else if (atual.get("B") == 1) {
            switch (movimento) {
                case 1:
                    atual.put("A", 1); 
                    atual.put("B", 0); 
                    local = "A";
                    break;
                case 2:
                    atual.put("C", 1);
                    atual.put("B", 0);
                    local = "C";
                    break;
                case 3:
                    continue;
                default:
                    break;
            }
        } else if (atual.get("C") == 1) {
            switch (movimento) {
                case 1:
                    continue;
                case 2:
                    atual.put("C", 0);
                    atual.put("B", 1);
                    local = "B";
                    break;
                case 3:
                    atual.put("C", 0);
                    atual.put("A", 1);
                    local = "A";
                    break;
                default:
                    break;
            }
        }
    }

        System.out.println(local);
}
}
