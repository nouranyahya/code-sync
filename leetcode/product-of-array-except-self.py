class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int size = nums.size();
        vector<int> answer (size, 0);
        int value = 1;
        int count=0;

        if(size==2){
            answer[0]=nums[1];
            answer[1]=nums[0];
            return answer;
        }

        for(int i=1; i<nums.size(); i++){
            if(nums[i]==0){
                count++;
            }else{
                value *= nums[i];
            }
        }

        answer[0] = value;
        if(count>=1){
            answer[0] = 0;
        }

        for (int i=1; i<nums.size(); i++){
            if(nums[i]==0 &&count==1){
                answer[i]=value*nums[0];
            }else if(count>=2){
                answer[i]=0;
            }else if(nums[i]!=0 && count>=1){
                answer[i]=0;
            }else{
                answer[i]=(value/nums[i]) * nums[0];
            }
        }

        return answer;
    }
};