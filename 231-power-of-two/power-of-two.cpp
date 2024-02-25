class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n < 1) {
            return false;
        } else {
            if (std::abs(std::log2(n)) == (int)std::log2(n)) {
                return true;
            }
        }
        return false;
    }
};