class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {

        int size = nums.size();

        if (target<nums[0]){
            return 0;
        }
        if(target<=nums[size/2]){
            size = size/2;

            for(int i=0; i<size; i++){
                if (target == nums[i]){
                    return i;
                }else if (target<nums[i]&&target>nums[i-1]){
                    return i;
                }
            }
        }else{
            for(int i=nums.size()/2; i<nums.size(); i++){
                if (target == nums[i]){
                    return i;
                }else if (target<nums[i]&&target>nums[i-1]){
                    return i;
                }
            }
        }

        return size;
    }
};