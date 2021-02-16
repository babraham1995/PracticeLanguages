package Interfaces;


import java.util.Iterator;
import java.util.List;

public class IterableExample implements Iterable{

    List<String> userList;

    public IterableExample(List<String> userList) {
        this.userList = userList;
    }

    //what does this function do?
    @Override
    public Iterator iterator() {
        return null;
    }
}
