package Builders;

public class App {

    public static void main(String[] args) {


        Person person = new PersonBuilder()
                .with($ -> {
                    $.salutation = "Mr.";
                    $.firstName = "John";
                    $.lastName = "Doe";
                    $.isFemale = false;
                })
                .with($ -> $.isHomewOwner = true)
                .with($ -> {
                    $.address =
                            new AddressBuilder()
                                    .with($_address -> {
                                        $_address.city = "Pune";
                                        $_address.state = "MH";
                                        $_address.pin = "411001";
                                    }).createAddress();
                })
                .createPerson();

        System.out.println(person);
    }
}
