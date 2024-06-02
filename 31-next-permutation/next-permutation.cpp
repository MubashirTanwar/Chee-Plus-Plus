class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int target = returnUnsortedIndex(nums);
        if (target == -1 ) return sort(nums.begin(), nums.end());
        swapNextBig(nums, target);
        reverse(nums.begin() + target + 1, nums.end());
      
    }

    int returnUnsortedIndex(vector<int>& nums){
        int i = nums.size()-1;
        while(i != 0){
            // check from the end if the array is sorted
            // [7,5,6,4,3,2,1]
            if(nums[i]<=nums[i-1]){
                --i;
            } else {
                return i-1;
            }
        }
        return -1;
    }

    void swapNextBig(vector<int>& nums, int idx){
        // check the next number from index; bada = 101
        // if bada and less than current bada use bada
        // 274321
        int bada = 101;
        int badaIdx = -1;
        int i = idx;
        while(i != nums.size()-1){
            if(nums[idx] < nums[i+1] && nums[i+1] <= bada){
                bada = nums[i+1];
                badaIdx = i+1;
            }
            i++;
            
        }
        cout << badaIdx << "\n";
        swap(nums[idx], nums[badaIdx]);
        for(int a = 0; a < nums.size(); a++){
            cout << nums[a];
        }

    }
};
