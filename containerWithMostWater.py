class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # max_area = 0
        # for h in range(0, len(height)):
        #     for i in range(h+1, len(height)):
        #         l = min(height[h], height[i])
        #         b = abs(h-i)
        #         area = l*b

        #         if area > max_area:
        #             max_area = area
        # return max_area

        left = 0
        right = len(height)-1
        max_area = 0
        
        while left <= right:
            area = min(height[left], height[right])*abs(left-right)

            if area > max_area:
                max_area = area
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area




            

            

            
            

        