class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty())
            return "";

        for (int s = 0; s < strs[0].length(); s++) {
            for (int e = 1; e < strs.size(); e++) {
                if (s == strs[e].length() || strs[e][s] != strs[0][s])
                    return strs[0].substr(0, s);
            }
        };

        return strs[0];
    }
};