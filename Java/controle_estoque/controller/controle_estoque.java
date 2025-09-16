package Java.controle_estoque.controller;

import java.util.Scanner;

import Java.controle_estoque.model.estoque;

public class controle_estoque {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("=====MENU=====");

        System.out.println("1 - adicionar item");

        System.out.println("escolha uma opção");

        int opcao = entrada.nextInt();
        entrada.nextLine();

        switch (opcao) {
            case 1:
                System.out.println("Digite o nome do produto");
                String nome_produto_estoque = entrada.nextLine();

                System.out.println("digite a quantidade do produto");
                int quantidade_estoque = entrada.nextInt();
                entrada.nextLine();

                

                break;


            default:
                System.out.println("opção nao existe");
                break;
        }

        entrada.close();
    }
}
