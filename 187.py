class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        if len(gas) == 0:
            return 0
        act_cost = [gas[i] - cost[(i+1)%len(gas)] for i in range(len(gas))]
        # print(act_cost)
        for i in range(len(gas)):
            if act_cost[i] >= 0:
                # print("i", i)
                tmp = (i+1)%len(gas)
                res_gap = act_cost[i]
                res_gap += act_cost[tmp]
                tmp = (tmp+1)%len(gas)
                while res_gap > 0 and tmp != i:
                    # print("res_gap", res_gap)
                    res_gap += act_cost[tmp]
                    # print("res_gap", res_gap)
                    tmp = (tmp+1)%len(gas)
                if tmp == i and res_gap >= 0:
                    return (i + 1)%len(gas)
        return -1

print(Solution.canCompleteCircuit(1, [2,0,1,2,3,4,0], [0,1,0,0,0,0,11]))