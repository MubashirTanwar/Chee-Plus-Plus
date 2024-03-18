class Solution {
public:
    string intToRoman(int num) {
        vector <string> roman = {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"};
        vector <int> nums = {1,4,5,9,10,40,50,90,100,400,500,900,1000};
        int index = nums.size() - 1;
        string result;
        while(num>0){

            if( num/nums[index] != 0 ){

                result = result + roman[index];
                num = num - nums[index];
            }
            else {
                index--;
            }
        } return result;
    }
};

