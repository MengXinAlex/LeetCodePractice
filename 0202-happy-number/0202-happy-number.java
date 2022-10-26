class Solution {
    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<Integer> (); 
        set.add(n);
        while(n != 1) {
            char[] chars = ("" + n).toCharArray();
            int digits = 0;
            for (char i : chars) {
                digits += Math.pow((int)(i-48) , 2);
            }
            if (set.contains(digits)) return false;
            n = digits;
            set.add(digits);
        }
        return true;
    }
}