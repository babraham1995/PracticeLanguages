// val a: Int

// val b: Int

// a = 78

// b = 100

// data class Book(var title: String, Var author: Author)

// Val book = Book(“Kotlin”, “JetBrains”)

// Val copy = book.copy()
    data class User(val name: String = "", val age: Int = 0)


public static void main(String[] args) {
    User user = new User();
    println(user);
    println("$name, $age years of age");
}