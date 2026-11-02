class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int first = 1, second = 2;
        while (first < numbers.length) {
            while ((second <= numbers.length)) {
                int a = numbers[first - 1];
                int b = numbers[second - 1];
                if (a + b == target) {
                    return new int [] {first, second}; 
                }
                second++;
            }
            first++;
        }
        return new int[]{};
    }
}