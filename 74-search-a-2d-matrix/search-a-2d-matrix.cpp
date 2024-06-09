class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        int row=0;
        int col= matrix[0].size() - 1;
        int totalRow = matrix.size();
        int index;
        while(row<totalRow && col>=0)
        {
            index = matrix[row][col];
            if(index==target) return 1;
            if(index>target)col--;
            else row++;
        }
        return 0;
    }
};


