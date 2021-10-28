class Solution {
public:
    int search(vector<int>& nums, int target) {
        int ans=0;
        return findt(nums,target,0,nums.size()-1);
    }
    int findt(vector<int>& nums, int target, int l, int r){
        if(l>r){
            return -1;
        }
        int mid=(l+r)/2;
        if(nums[mid]==target)
            return mid;
        if(nums[mid]<=nums[r]){
            if(target>nums[mid]&&target<=nums[r])
                return findt(nums,target,mid+1,r);
            else
                return findt(nums,target,l,mid-1);
        }
        else{
            if(target<nums[mid]&&target>=nums[l])
                return findt(nums,target,l,mid-1);
            else
                return findt(nums,target,mid+1,r);
        }
    }
};