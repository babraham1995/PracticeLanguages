package Generics;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class GenericMethods {

    //methods in collections such a binary search, sort have been generified
    //methods that take in generic lists, objects

    //normal method
    public List<Car> carManufacturer(List<Car> carsList) {

        return carsList;
    }

    //generic method
    public <T> List<T> anythingManufacturer(List<T> itemList) {

//        if (itemList.get(0).getClass()){
//            System.out.println("tis but a car");
//        }
        return itemList;

    }
    //bounded generic method
    public <T extends Number> List<T> anythingNumberManufacturer(List<T> itemList) {

//        if (itemList.get(0).getClass()){
//            System.out.println("tis but a car");
//        }
        return itemList;
    }


    public static void main(String[] args) {
        
        Car c = new Car("blue");
        List<Car> carList = Arrays.asList(c);
        Plane p = new Plane("green");
        List<Plane> planeList = Arrays.asList(p);
        List<Integer> numberList = Arrays.asList(1,2,3);
        List<Object> stringList = Arrays.asList("1","2",3);
        System.out.println(carList);
        System.out.println(new GenericMethods().carManufacturer(carList));
        System.out.println(new GenericMethods().anythingManufacturer(planeList));
        System.out.println(new GenericMethods().anythingNumberManufacturer(numberList));


    }
    
}
