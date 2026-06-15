class Solution {
    public boolean hasDuplicate(int[] nums) {

        for(int j=1; j< nums.length ; j++){
            for(int i=0; i < j ; i++ ){
               if (nums[i]==nums[j]){
                return true;
               }
            }
        }
        return false;
    }
}