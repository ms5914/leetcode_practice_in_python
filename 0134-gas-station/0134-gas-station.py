class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        num_stations = len(gas)
        curr_gas = 0

        if sum(cost)-sum(gas) > 0:
            return -1

        start = 0
        for current_station_index in range(num_stations):
            curr_gas+=(gas[current_station_index]-cost[current_station_index])
            if curr_gas < 0:
                start = current_station_index+1
                curr_gas = 0
        
        return start



#Keep revisiting this until clear https://www.chuckmblog.com/2023/09/02/programmingleetcode-134-gas-station/





        