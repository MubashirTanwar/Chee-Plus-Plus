class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        double max = -numeric_limits<double>::infinity();
        int end = 0;
        for(int i = 0; i <nums.size(); ++i){
            end = end + nums[i];;
            if(max < end) max = end;
            if (end < 0) end = 0;
        }
        return max;
    }
};