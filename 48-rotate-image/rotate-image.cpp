class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        for(int i = 0; i < matrix.size(); i++){
            cout << "[";
            for(int j = i; j < matrix.size(); j++){
                swap(matrix[i][j], matrix[j][i]);
            }
            cout << "],";

        }
        int mid = (matrix.size())/2;
        cout << mid;
        for(int i = 0; i < matrix.size(); i++){
            for(int j = 0; j < mid; j++){
                swap(matrix[i][j], matrix[i][matrix.size()-1-j]);
            }
        }

        
    }
};