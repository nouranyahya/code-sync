class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> transl{{'I',1},{'V',5},{'X',10}, {'L',50},{'C',100},{'D',500},{'M',1000}};

        int ans=0;
        for (int i=0; i<s.length(); i++){
            if (transl[s[i]]<transl[s[i+1]]){
                ans -= transl[s[i]];
            }else{
                ans += transl[s[i]];
            }
        }
        return ans;
    }
};