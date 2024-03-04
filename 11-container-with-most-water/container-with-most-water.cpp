class Solution {
public:
    int maxArea(vector<int>& height) {
    int i = 0;
    int j = height.size() - 1;
    int max_vol = 0;
    while(i<j){
        max_vol = max(max_vol , min(height[i],height[j])*(j-i));
        if (height[i]<height[j]) i++;
        else j--;
    }
    return max_vol;
    }
};