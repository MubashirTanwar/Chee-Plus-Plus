class Solution {
public:
    bool isPalindrome(int x) {
        std::string str = std::to_string(x);
        int length = str.length();
        for (int i = 0; i < length / 2; ++i) {
            if (str[i] != str[length - i - 1]) {
                return false;
            }
        }
        return true;
    }
};