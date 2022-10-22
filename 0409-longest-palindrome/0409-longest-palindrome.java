class Solution {
    public int longestPalindrome(String s) {
        if (s == null || s.length() < 1) return 0;
        Set<Character> set = new HashSet<>();
        for (char i : s.toCharArray()) {
            if (set.contains(i)) set.remove(i);
            else set.add(i);
        }
        if (set.size() <= 1) return s.length();
        return s.length() - set.size() + 1;
        
    }
}