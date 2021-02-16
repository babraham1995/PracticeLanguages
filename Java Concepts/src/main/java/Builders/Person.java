package Builders;

public class Person {
    String salutation;
    String firstName;
    String middleName;
    String lastName;
    String suffix;
    Address address;
    boolean isFemale;
    boolean isEmployed;
    boolean isHomewOwner;

    public Person(String salutation, String firstName, String middleName, String lastName, String suffix, Address address, boolean isFemale, boolean isEmployed, boolean isHomewOwner) {
        this.salutation = salutation;
        this.firstName = firstName;
        this.middleName = middleName;
        this.lastName = lastName;
        this.suffix = suffix;
        this.address = address;
        this.isFemale = isFemale;
        this.isEmployed = isEmployed;
        this.isHomewOwner = isHomewOwner;
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("Person{");
        sb.append("salutation='").append(salutation).append('\'');
        sb.append(", firstName='").append(firstName).append('\'');
        sb.append(", middleName='").append(middleName).append('\'');
        sb.append(", lastName='").append(lastName).append('\'');
        sb.append(", suffix='").append(suffix).append('\'');
        sb.append(", address=").append(address);
        sb.append(", isFemale=").append(isFemale);
        sb.append(", isEmployed=").append(isEmployed);
        sb.append(", isHomewOwner=").append(isHomewOwner);
        sb.append('}');
        return sb.toString();
    }
}
