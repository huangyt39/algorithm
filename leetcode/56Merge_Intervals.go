/**
 * Definition for an interval.
 * type Interval struct {
 *	   Start int
 *	   End   int
 * }
 */

type IntervalArr []Interval

func (arr IntervalArr) Len() int{
    return len(arr)
}

func (arr IntervalArr) Less(i, j int) bool{
    return arr[i].Start < arr[j].Start 
}

func (arr IntervalArr) Swap(i, j int){
    arr[i], arr[j] = arr[j], arr[i]
}

func merge(intervals []Interval) []Interval {
    if len(intervals) == 0{
        return nil
    }
    
    sort.Sort(IntervalArr(intervals))
    res := make([]Interval, 0)
    pInter := &intervals[0]
    for i := 1; i < len(intervals);i ++{
        curInter := &intervals[i]
        if curInter.Start <= pInter.End{
            if curInter.End > pInter.End{
                pInter.End = curInter.End
            }
        }else{
            res = append(res, *pInter)
            pInter = curInter
        }
    }
    res = append(res, *pInter)
    return res
}