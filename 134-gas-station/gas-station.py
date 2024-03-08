class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_start = 0
        my_tank = 0
        total_net_left_over = 0
        for i in range(len(gas)):
            total_net_left_over += gas[i] - cost[i]
            my_tank += gas[i] - cost[i]
            if my_tank < 0:
                my_tank = 0
                cur_start = i + 1
        if total_net_left_over < 0:
            return -1
        return cur_start
        


        