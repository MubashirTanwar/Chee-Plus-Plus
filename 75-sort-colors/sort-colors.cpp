class Solution {
public:
    void sortColors(vector<int>& nums) {
        // [2,2,0,0,1,1]
        for (int i = 0; i < nums.size(); i++){
            if(nums[i] == 2){
                int j = nums.size()-1;
                while(j > i) {
                    if (nums[j] != 2){
                        swap(nums[i], nums[j]);
                        break;
                    }
                    j--;
                }
            }
            if(nums[i] == 0){
                // nums[1]
                int j = 0;
                while(j < i){
                    if(nums[j] != 0){
                        swap(nums[i], nums[j]);
                        break;
                    }
                    j++;
                }
            }
        }
    }
};