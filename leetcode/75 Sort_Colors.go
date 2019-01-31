func sortColors(nums []int)  {
    if len(nums) == 0{
        return
    }
    red, white, blue := 0, 0, 0
    for i := 0;i < len(nums); i ++{
        switch nums[i] {
        case 0:
            red ++
            break
        case 1:
            white ++
            break
        case 2:
            blue ++    
            break
        }
    }
    for j := 0; j < len(nums); j++{
        if red != 0{
            nums[j] = 0
            red --
            continue
        }
        if white != 0{
            nums[j] = 1
            white --
            continue
        }
        if blue != 0{
            nums[j] = 2
            blue --
            continue
        }
    }
    return
}