package Generics;

public class Plane {

    String color;
    String wings;

    public Plane(String color) {
        this.color = color;
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("Plane{");
        sb.append("color='").append(color).append('\'');
        sb.append(", wings='").append(wings).append('\'');
        sb.append('}');
        return sb.toString();
    }
}
