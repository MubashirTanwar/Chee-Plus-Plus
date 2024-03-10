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
        for (int j = 0; j < t.length(); j++) {
            if (HashMap.find(t[j]) != HashMap.end()) {
                HashMap[t[j]] -= 1;
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