class Solution {
public:
    int singleNumber(std::vector<int>& nums) {
        int target = 0;
        for (int num : nums) {
            target ^= num;
        }
        return target;
    }
};