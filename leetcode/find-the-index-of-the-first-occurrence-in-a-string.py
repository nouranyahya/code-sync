class Solution {
public:
    int strStr(string haystack, string needle) {
        int index=-1;

        for (int i=0; i<haystack.length(); i++){
            if (needle[0]==haystack[i]){
                index=i;
                for (int j=0; j<needle.length(); j++){
                    if(needle[j]!=haystack[j+i]){
                        index=-1;
                        break;
                    }else if(j==needle.length()-1){
                        return index;
                    }
                }
            }
        }
        return index;
    }
};