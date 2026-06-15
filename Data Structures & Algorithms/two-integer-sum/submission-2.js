class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        for(let j=nums.length - 1; j > 0 ; j--){
            for(let i=0;i<nums.length;i++){
                if(nums[j]+nums[i] == target){
                    return [j,i];
                }
            }
        }
    }
}
