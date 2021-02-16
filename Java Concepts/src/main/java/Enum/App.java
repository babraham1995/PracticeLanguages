package Enum;

public class App {

    public static void main(String[] args) {
        System.out.println("hi: " + BruhEnum.THIS);

        BruhEnum myVar = BruhEnum.THIS;
        switch(myVar) {
            case THIS:
                System.out.println("Low level");
                break;
            case TOO:
                System.out.println("Medium level");
                break;
            case SHALL:
                System.out.println("High level");
                break;
        }
    }
}
