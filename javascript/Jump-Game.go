func canJump(nums []int) bool {
    var target=len(nums)-1
    for i:=len(nums)-2; i>-1; i--{
        if i+nums[i]>=target{
            target=i
        }
    }
    return target==0
}