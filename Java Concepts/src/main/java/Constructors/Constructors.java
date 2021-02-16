package Constructors;

import org.codehaus.plexus.util.StringUtils;

import java.util.Objects;

public class Constructors {

    //constructors and use of static key word

    public Constructors(String person) {

        this.person = StringUtils.capitalise(person);
    }

    public String person;
    public int age;
    public static String name;

//    public void stupidFunction(){
//        person = "hi person";
//        System.out.println(person);
//    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = StringUtils.capitalise(name);
    }


    public String getperson() {
        return person;
    }

    public void setperson(String person) {
        this.person = StringUtils.capitalise(person);
    }

    //instance controlled static factory method as alternative to constructor
    public static Boolean valueOf(boolean b) {
        return b ? Boolean.TRUE : Boolean.FALSE;
    }

    public String exampleSingleton(String name){
        return name;
    }

    @Override
    public String toString() {
        return "Constructors{" +
                "person='" + person + '\'' +
                ", age=" + age +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Constructors that = (Constructors) o;
        return age == that.age && Objects.equals(person, that.person);
    }

    @Override
    public int hashCode() {
        return Objects.hash(person, age);
    }

    public Constructors thisa(Object o){
        System.out.println(o);
        return this;
    }
}
