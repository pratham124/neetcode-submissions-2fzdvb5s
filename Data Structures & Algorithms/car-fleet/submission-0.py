class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # first car: 9 /3 = 3 seconds
        # 5 seconds
        # second car: 6 / 2 = 3 seconds

        position_speed_arr = [(position[i], speed[i]) for i in range(len(position))]
        position_speed_arr.sort()
        time_arr = []
        for pos, speed in position_speed_arr:
            seconds = (target - pos) / speed
            time_arr.append(seconds)
        
        stack = []
        for t in time_arr:
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)
        return len(stack)