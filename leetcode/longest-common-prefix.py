class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans="";
        int strsl = strs.size();
        if (strsl==1){
            return strs[0];
        }
        for (int j=0; j<strs[0].size(); j++){
            int i=1;
            while (i!=strsl){
                if (strs[i][j]!= strs[0][j]){
                return ans;
                }
                if (i==strsl-1){
                    ans += strs[i][j];
                }
                i++;
            }
        }

        return ans;
    }
};