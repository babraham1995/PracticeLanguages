package Interfaces;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class App {

    public static void main(String[] args) {
        List<String> listS = Arrays.asList("Hello", "World!", "How", "Are", "You");

        IterableExample i = new IterableExample(listS);

        i.forEach(Object::notifyAll);
        i.iterator();
//        i instanceof  ? (() i) : null;
//        i.equals();
//        i.spliterator();
//        i.hashCode();
//        ((int) i);
        for (Object o : i) {
            System.out.println("**"+o);
        }

        Vehicle vehicle = new Vehicle() {
            @Override
            public void startEngine() {
                System.out.println("vroom!");
            }

            @Override
            public String makeANoise() {
                System.out.println("toot a loot!");
                return "bro";
            }
        };
        System.out.println(vehicle.makeANoise());
        vehicle.startEngine();

    }


}
