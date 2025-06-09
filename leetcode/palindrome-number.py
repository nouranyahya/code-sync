class Solution {
public:
    bool isPalindrome(int x) {
        int i=0;
        string n = to_string(x);
        int j=n.length()-1;

        if (x<0){
            return false;
        }
        while (i<j){
            if (n[i]!= n[j]){
                return false;
            }
            i++;
            j--;
        }

        return true;
    }
};