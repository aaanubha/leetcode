class Solution(object):
    def videoStitching(self, clips, time):
        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        clips.sort(key=lambda x: x[0])
        
        n = len(clips)
        start = end = count = 0
        
        while start < time:
            max_end = start
            while end < n and clips[end][0] <= start:
                max_end = max(max_end, clips[end][1])
                end += 1
            
            if max_end <= start:
                return -1
            count += 1
            start = max_end
            
            if start >= time:
                return count
            
        return -1