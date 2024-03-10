class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> duplicate;
        // ONE LINE LMAOOOOOO
        for (const int item : nums) if (!duplicate.insert(item).second)return true;
        return false;
    }
};