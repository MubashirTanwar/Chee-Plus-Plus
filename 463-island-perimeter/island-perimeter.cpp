class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int sides = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) {
                if (grid[i][j] == 1) {
                    checkSides(grid, i, j, sides);
                }
            }
        }
        return sides;
    }

    void checkSides(vector<vector<int>>& grid, int i, int j, int& sides) {
        if (i - 1 < 0 || grid[i - 1][j] == 0) sides++; // Check upper side
        if (j - 1 < 0 || grid[i][j - 1] == 0) sides++; // Check left side
        if (i + 1 >= grid.size() || grid[i + 1][j] == 0) sides++; // Check lower side
        if (j + 1 >= grid[i].size() || grid[i][j + 1] == 0) sides++; // Check right side
    }
};