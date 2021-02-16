package Constructors;


public class App {

    public static void main(String[] args) {

        String s = SingletonExample.leaveTheBuilding();


        System.out.println(s);

        NutritionFacts cocaCola = new NutritionFacts.Builder(240, 8).
                calories(100).sodium(35).carbohydrate(27).build();

        System.out.println(cocaCola);

        Constructors con = new Constructors("pete");
        Constructors con1d = new Constructors("pete");
        System.out.println("****" + con.thisa(s));
        System.out.println("****" + con.equals(con1d));
        con.hashCode();
        con.setName("steve");
        con.setName("john");
        con.setName("pete");
//        System.out.println(con.getName());

        Constructors con1 = new Constructors("pete");
//
//        System.out.println(con);
//
//        con.setperson("steve");
//
//        System.out.println(con);
        con1.setName("steve");
        con1.setName("john");
//        System.out.println(con.getName());


//        con.setperson("hi guys pete here");

//        con.stupidFunction();

//        System.out.println(con);
    }
}
