# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        vis = set()
        clean = set()
        d = 1
        ds = [(1,0),(0,1),(-1,0),(0,-1)]
        
        def dfs(point):
            
            x,y = point
            
            nonlocal d
            
            clean.add(point)
            robot.clean()
            for _ in range(4):
                dx,dy = ds[d]
                new_p = (x+dx,y+dy)
                curd = d
                if new_p not in clean and robot.move():
                    dfs(new_p)
                d = (d+1)%4
                robot.turnLeft()
                
                    
            
            
            vis.add(point)
            
            
            
            
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
            
        dfs((0,0))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        