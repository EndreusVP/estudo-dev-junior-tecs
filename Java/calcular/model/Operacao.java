package Java.calcular.model;

public class Operacao {
    private int num1;
    private int num2;

    public Operacao() {

    }

    public Operacao( int num1, int num2) {
        this.num1 = num1;
        this.num2 = num2;
    }

    public void setNum1(int num1){
        this.num1 = num1;
    }

    public int getNum1(){
        return num1;
    }

    public void setNum2(int num2){
        this.num2 = num2;
    }

    public int getNum2(){
        return num2;
    }

    public int somar() {
        int res = this.getNum1() + this.getNum2();
        return res;
    }

    public int sub() {
        int res = getNum1() - getNum2();
        return res;
    }

    public int mult() {
        int res = getNum1() * getNum2();
        return res;
    }

    public int div(){
        int res = getNum1()/getNum2();
        return res;
    }
}

