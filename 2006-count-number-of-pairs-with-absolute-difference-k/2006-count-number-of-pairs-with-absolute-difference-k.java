class Solution {
    public int countKDifference(int[] nums, int k) {
        int ans = 0;
        
        Map<Integer,Integer> m = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            
            if(m.containsKey(nums[i]+k))
                ans+=m.get(nums[i]+k);
                
            if(m.containsKey(nums[i]-k))    
                ans+=m.get(nums[i]-k);
               
            m.put(nums[i],m.getOrDefault(nums[i],0) +1);
        }
        
         
        return ans;
        
    }
}