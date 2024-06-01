class Solution {
public:
    vector<vector<int>> generate(int numRows) {
    vector<vector<int>> bigArr(numRows);
    for (int i = 0; i < numRows; ++i) {
        bigArr[i].resize(i + 1, 1);
    }
    
    for (int row = 2; row < numRows; ++row) {
        for (int col = 1; col < bigArr[row].size() - 1; ++col) {
            bigArr[row][col] = bigArr[row - 1][col - 1] + bigArr[row - 1][col];
        }
    }
    return bigArr;
    }
};
