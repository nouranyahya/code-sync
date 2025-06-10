class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> numsind;
        for (int i=0; i<nums.size(); i++){
            if(numsind.count(nums[i]) && i-numsind[nums[i]]<=k){
                return true;
            }
            numsind[nums[i]]=i;
        }
        return false;
    }
};