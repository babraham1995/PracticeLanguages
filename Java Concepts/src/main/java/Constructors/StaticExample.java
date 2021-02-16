package Constructors;

//Java Program to demonstrate the use of an instance variable
//which get memory each time when we create an object of the class.  
class StaticExample{
    int count=0;//will get memory each time when the instance is created  
    static int staticCounter=0;
     static int a = 0;
     //this static block gets called once for all instantiations of this class
    static {
        a++;
        System.out.println(a);
    }

    StaticExample(){
        staticCounter++;
        count++;//incrementing value
//        System.out.println("static " + staticCounter);
//        System.out.println("not static" + count);
    }

    public static String staticStringMethod(){
        System.out.println("ho");
        return "hi";
    }
    public static int increment(){
    a++;
        System.out.println(a);
        return a;
    }


    public static void main(String args[]){
//Creating objects  
        StaticExample c1=new StaticExample();
        StaticExample c2=new StaticExample();
        StaticExample c3=new StaticExample();

        //string literal:
        String c = staticStringMethod();
//        c1.increment();
//        c2.increment();
//        c3.increment();

        //why no new keyword for String
        //string object:
        String d = new String("hey");
        //String literal in the pool vs String object in the heap

//        System.out.println(c);
//        System.out.println(d);
    }
}  