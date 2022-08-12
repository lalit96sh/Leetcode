class Solution:
    def racecar(self, target: int) -> int:

        q = collections.deque()

        q.append((0,1,0,[]))

        vis = set()
        vis.add((0,1))

        while q:
            
            qlen = len(q)
            for _ in range(qlen):
                position,speed,steps,path = q.popleft()

                if position==target:
                    # print(path)
                    # print(q)
                    return steps

                if (position+speed,2*speed) not in vis and position+speed>0 and position+speed<=2*target:
                    vis.add((position+speed,2*speed))
                    q.append((position+speed,2*speed,steps+1,path+[position+speed]))
                d = -1 if speed>0 else 1
                if position>=0 and (position,d) not in vis:
                    vis.add((position,d))
                    q.append((position,d,steps+1,path+[position]))
            
        return -1
                
            
            
            
            