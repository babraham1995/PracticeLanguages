package Enum;

 enum BruhEnum {
     //alternative method
//     THIS {
//         public String toString() {
//             return "this is one";
//         }
//     },
//
//     TOO {
//         public String toString() {
//             return "this is two";
//         }
//     }
//
    THIS("this!"),
    TOO("too!"),
    SHALL("shall"),
    PASS("pass");

     private final String text;

     /**
      * @param text
      */
     BruhEnum(final String text) {
         this.text = text;
     }

     /* (non-Javadoc)
      * @see java.lang.Enum#toString()
      */
     @Override
     public String toString() {
         return text;
     }


}
