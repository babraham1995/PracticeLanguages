//package Constructors;
//
//public static class NutritionFactsBuilder {
//    // Required parameters
//    private final int servingSize;
//    private final int servings;
//    // Optional parameters - initialized to default values
//    private int calories = 0;
//    private int fat = 0;
//    private int carbohydrate = 0;
//    private int sodium = 0;
//
//    public NutritionFactsBuilder(int servingSize, int servings) {
//        this.servingSize = servingSize;
//        this.servings = servings;
//    }
//
//    public NutritionFactsBuilder calories(int val) {
//        calories = val;
//        return this;
//    }
//
//    public NutritionFactsBuilder fat(int val) {
//        fat = val;
//        return this;
//    }
//
//    public NutritionFactsBuilder carbohydrate(int val) {
//        carbohydrate = val;
//        return this;
//    }
//
//    public NutritionFactsBuilder sodium(int val) {
//        sodium = val;
//        return this;
//    }
//
//    public NutritionFacts build() {
//        return new NutritionFacts(this);
//    }
//}
//
