package Generics;

public class Car {

    String color;
    String wheels;

    public Car(String color) {
        this.color = color;
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("Car{");
        sb.append("color='").append(color).append('\'');
        sb.append(", wheels='").append(wheels).append('\'');
        sb.append('}');
        return sb.toString();
    }
}
