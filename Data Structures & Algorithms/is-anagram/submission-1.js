class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
            let j = 1;
            if(s.length == t.length){
        for(let i =0;i<s.length; i++){
let shouldExtract = false;
            shouldExtract = t.includes(s.substring(i,j));
            let letter = s.substring(i,j);
            if (shouldExtract){
               t = t.replace(letter,"");
            }
            j++;
            }
            }
            else{
                return false
            }
            if(t==""){
                return true;
            }
            return false;
    }
}
