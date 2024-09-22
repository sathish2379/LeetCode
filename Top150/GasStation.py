'''
134. Gas Station
Medium

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        Total_gas = 0
        n = len(gas)
        # My code O(n^2), giving TLE
        # for i in range(0, n):
        #     Total_gas = gas[i]
        #     if Total_gas < cost[i]:
        #         continue
        #     final_index = -1
        #     for j in range(0, n):
        #         k = (i+j)%n
        #         if Total_gas >= cost[k]:
        #             Total_gas = Total_gas - cost[k] + gas[(k+1)%n]
        #             final_index = (k+1)%n
        #         else:
        #             final_index = -1
        #             break
        #         if final_index == i:
        #             return final_index
        # return -1

        #Let's try greedy approach
        # if you start at a station and run out of gas before completing the circuit, 
        # any station between the start and the station where you run out of gas 
        # cannot be the starting station either. 

        # If total_gas >= 0, it means that the total amount of fuel available in all stations 
        # is at least equal to the total cost, making it theoretically possible to 
        # complete the circuit.

        # current_gas Identifies a Valid Starting Point:

        current_gas = 0
        start_index = 0
        for i in range(len(gas)):
            Total_gas += gas[i] - cost[i] ## This actually doing sum (gas[i] - cost[i]) which is our idea
            current_gas += gas[i] - cost[i]

            if current_gas < 0:
                start_index = i + 1
                current_gas = 0
        return start_index if Total_gas >= 0 else -1

            
                
            


            
            
        