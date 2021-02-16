package Consumer;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

//import static org.graalvm.compiler.debug.TTY.println;

public class Generics {

    //generic list
    List<Integer> list = new LinkedList<>();

    //generic method
    public <T> List<T> fromArrayToList(T[] a) {
        return Arrays.stream(a).collect(Collectors.toList());
    }

//    @Test
//    public void givenArrayOfIntegers_thanListOfStringReturnedOK() {
//        Integer[] intArray = {1, 2, 3, 4, 5};
//        List<String> stringList
//                = Consumer.Generics.fromArrayToList(intArray, Object::toString);
//
//        assertThat(stringList, hasItems("1", "2", "3", "4", "5"));
//    }

    //bounded generics
    public <T extends Number> List<T> fromArrayToList(T[] a) {
        List<T> i = new LinkedList<>();
        return i;
    }
//    multiple bounds: <T extends Number & Comparable>
}
