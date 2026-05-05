func sortColors(nums []int) {
    start := 0;
    end := len(nums) - 1;

    for i := 0; i < len(nums); i++ {
        if nums[i] == 0 {
            nums[i] = nums[start];
            nums[start] = 0;
            start += 1;
        } else if nums[i] == 2 {
            nums[i] = nums[end];
            nums[end] = 2;
            end -= 1;
            i--;
        }

        if i >= end {
            break
        }
    }
}
