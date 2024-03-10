class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> HashMap;
        if (s.length() != t.length()) {
            return false;
        }

        for (int i = 0; i < s.length(); i++) {
            HashMap[s[i]]++;
        }
        for (int i = 0; i < t.length(); i++) {
            if (HashMap.find(t[i]) != HashMap.end()) {
                HashMap[t[i]] -= 1;
            } else
                return false;
        }
        for (auto items : HashMap) {
            if (items.second != 0) {
                return false;
            }
        }
        return true;
    }
};