public class Solution {
    public int FindMin(int[] nums) {
        int res = int.MaxValue;
        int start = 0, end = nums.Length-1;

        while (start <= end) {
            if (nums[start] < nums[end])
            {
                res = Math.Min(res, nums[start]);
            }

            int mid = (start + end) / 2;
            res = Math.Min(res, nums[mid]);

            if (nums[mid] >= nums[start])
                start = mid + 1;
            else
                end = mid - 1;
        }
        return res;
    }
}
