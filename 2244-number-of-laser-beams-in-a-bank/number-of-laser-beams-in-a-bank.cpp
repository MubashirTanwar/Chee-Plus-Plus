class Solution {
public:
    int numberOfBeams(std::vector<std::string>& bank) {
        int prev_count = 0;
        int res = 0;
        for (const auto& string : bank) {
            int count = 0;
            for (char num : string) {
                if (num == '1') {
                    count++;
                }
            }
            if (count > 0) {
                res += (prev_count * count);
                prev_count = count;
            }
        }

        return res;
    }
};