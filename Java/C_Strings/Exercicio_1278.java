/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package C_Strings;

import java.util.Scanner;

/**
 *
 * @author Scarlxrd2112
 */
public class Exercicio_1278 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int qtdLinhas = 0;
        int contador = 0;
        while(true){
            qtdLinhas = teclado.nextInt();
            if(qtdLinhas==0){
                break;
            }
            String texto = "";
            teclado.nextLine();
            int maiorLinhaTamanho = 0;
            String maiorLinha = "";
            for (int i = 0; i < qtdLinhas; i++) {
                String linha = teclado.nextLine().replaceAll("\\s+", " ").trim();
                if (i==0){
                   maiorLinhaTamanho = linha.length(); 
                   maiorLinha = linha;
                }else{
                    int tam = linha.length();
                   if(tam>maiorLinhaTamanho){
                       maiorLinhaTamanho = tam;
                       maiorLinha = linha;
                   } 
                }
                
                if(i!= qtdLinhas-1){
                   texto+= linha + "\n";
                }else{
                    texto+= linha;
                }
            }
            String [] textoArray = texto.split("\n");
            for (int i = 0; i < qtdLinhas; i++) {
                textoArray[i] = String.format("%" + maiorLinhaTamanho +"s", textoArray[i]);
            }
            if(contador>0){
                     System.out.println();
            }
       
            
            for (String string : textoArray) {
                System.out.println(string);
            }
            
            contador+=1;
            }
        
    }
    
}

