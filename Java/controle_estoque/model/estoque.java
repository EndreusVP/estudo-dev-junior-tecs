package Java.controle_estoque.model;

import java.util.HashMap;

public class estoque {
    HashMap<String, Integer> estoque = new HashMap<>();

    private String nome_produto;
    private int quantidade;

    public estoque (String nome_produto, int quantidade) {
        this.nome_produto = nome_produto;
        this.quantidade = quantidade;
    }
    
    public estoque () {

    }

    public void adicionar_item() {
        estoque.put(nome_produto, quantidade);
    }

    public void setNome_estoque(String nome_produto) {
        this.nome_produto = nome_produto;
    }

    public String getNome_produto(){
        return nome_produto;
    }

    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }

    public int getQuantidade() {
        return quantidade;
    }

    
}
