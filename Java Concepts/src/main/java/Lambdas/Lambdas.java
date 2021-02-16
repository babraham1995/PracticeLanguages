package Lambdas;

import org.codehaus.plexus.util.StringUtils;

import javax.swing.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.function.BiConsumer;
import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.Stream;


public class Lambdas {

        public static void printFormatted(String str, StringFunction format) {
            String result = format.run(str);
            System.out.println(result);
        }

        public static void lammy(){
//             () -> System.out.println("hello!!!");
        }


        public static class UseTodo {
            public String add(String string, Function<String, String> fn) {
                return fn.apply(string);
            }
        }

        public static void main(String[] args) {

            //event listener
            JButton button =  new JButton("Submit");
            button.addActionListener((e) -> {
                System.out.println("Click event triggered !!");
            });

            //no parameter
            // () -> System.out.println();
            //multiple parameters
//            (s, a) -> System.out.println();
//            //mulitple parameters with type
//            (String s, String a) -> System.out.println();
            //multiple statements
            Todo todo = parameter -> parameter + " from lambda";
            System.out.println("yoyo" + todo);

            UseTodo useTodo = new UseTodo();


            Function<String, String> fn =
                    parameter -> parameter + " from lambda";
            String result = useTodo.add("I've added something", fn);


//            (Integer x, Integer y) -> {
//                System.out.println();
//                System.out.println();
//                return x + y;
//            };
//            ArrayList<Integer> numbers = new ArrayList<Integer>();
//            numbers.add(5);
//            numbers.add(9);
//            numbers.add(8);
//            numbers.add(1);
//            numbers.forEach((n) -> {
//                System.out.println(n);
//            });
//
//            StringFunction exclaim = (s) -> s + "!";
//            StringFunction ask = (s) -> s + "?";
//            printFormatted("Hello", exclaim);
//            printFormatted("Hello", ask);

//            String j = "";
            List<String> list = Arrays.asList("hi", "there", "i'm", "steve");

//            (list) ->
                   List<String> newlist = list.stream()
                           .map(i -> StringUtils.capitalise(i))
                           .collect(Collectors.toList());
//                           .forEach(System.out::println);
            System.out.println(newlist);
        }
}

