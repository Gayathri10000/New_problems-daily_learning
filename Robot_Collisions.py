class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = [[positions[index],healths[index],directions[index],index] for index in range(n)]
        robots.sort(key=lambda x: (x[0], x[2]))
        stack= []

        for robot in robots:
            if robot[2] =='R' or not stack or stack[-1][2] == 'L':
                stack.append(robot)
                continue
            
            if robot[2] == 'L':
                flag = True
                while stack and stack[-1][2] == 'R'and flag:
                    last_health = stack[-1][1]
                    if robot[1] > last_health:
                        stack.pop()
                        robot[1] -=1
                    elif robot[1] < last_health:
                        stack[-1][1] -= 1
                        flag = False
                    else:
                        stack.pop()
                        flag = False
                if flag:
                    stack.append(robot)
        return [robot[1] for robot in sorted(stack,key = lambda robot: robot[3])]
