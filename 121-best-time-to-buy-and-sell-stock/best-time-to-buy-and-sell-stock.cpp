class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 1;
        int profit = 0;
        while(r < prices.size()){
            // check if we are in loss
            if (prices[r] <= prices[l]){
                l = r;
                r++;
            } else {
                profit = max(profit, prices[r] - prices[l]);
                r++;
            }
        }
        return profit;
    }
};
       