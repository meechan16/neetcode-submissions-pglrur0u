class Solution:
    def carFleet(self, target, position, speed):
        n = len(position)
        
        indices = list(range(n))
        
        indices.sort(key=position.__getitem__, reverse=True)
        
        fleets = 0
        prev_time = 0
        
        for i in indices:
            time = (target - position[i]) / speed[i]
            
            if time > prev_time:
                fleets += 1
                prev_time = time
        
        return fleets