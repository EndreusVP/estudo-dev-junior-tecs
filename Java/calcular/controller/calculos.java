package Java.calcular.controller;

import java.util.Scanner;

import Java.calcular.model.Operacao;

public class calculos {
    public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);

        int opcao = -1;

        while (opcao!=0) {

            System.out.println("digite um numero: ");

            int numero1 = entrada.nextInt();
            entrada.nextLine();

            System.out.println("digite outro numero: ");

            int numero2 = entrada.nextInt();
            entrada.nextLine();

            Operacao numeros = new Operacao(numero1, numero2);


            System.out.println("=====Menu=====");

            System.out.println("1 - somar");
            System.out.println("2 - subtrair");
            System.out.println("3 - multiplicar");
            System.out.println("4 - dividir");

            System.out.println("Escolha uma opção: ");
            opcao = entrada.nextInt();
            entrada.nextLine();

            if (opcao == 0) {
                System.out.println("saindo...");
                break;
            }

            switch (opcao) {
                case 1:
                    System.out.println("resultado: " + numeros.somar());
                    break;
                case 2:
                    System.out.println("resultado: " + numeros.sub());
                    break;
                case 3:
                    System.out.println("resultado: " + numeros.mult());
                    break;
                case 4:
                    System.out.println("resultado: " + numeros.div());
                    break;
                default:
                    System.out.println("escolheu oq nao existe prr");
                    break;
            }

        }

        entrada.close();
    }
    
}
