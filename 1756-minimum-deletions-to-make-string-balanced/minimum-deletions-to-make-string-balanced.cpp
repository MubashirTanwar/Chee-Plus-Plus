class Solution {
public:
    int minimumDeletions(string s) {
        int del = 0;
        int bs = 0;
        for (char c : s){
            if (c == 'b') bs++;
            else if (bs){
                del++;
                bs--;
            }
        }
        return del;
    }
};