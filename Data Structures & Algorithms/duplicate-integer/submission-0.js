class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
    let result = 0;
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums.length; j++){
            if(nums[i] == nums[j]){
                result++;
            }
        }
    }
     if (result == nums.length){
        return false;
    } else {
    return true;
    }
   
    }
}
