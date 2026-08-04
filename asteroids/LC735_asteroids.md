* Asteroids Leetcode 735 (Stack), Premium   https://leetcode.com/problems/asteroid-collision/description/


### A's solution:
*placeholder*

### Nick's solution
```python 
from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        astro_turf = deque(asteroids)
        stack = []

        while astro_turf:
            cur = astro_turf.popleft()
            stack.append(cur)
            while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:
                # EXPLODE!
                last = stack.pop()
                penultimate = stack.pop()
                if abs(last) > abs(penultimate):
                    stack.append(last)
                elif abs(last) == abs(penultimate):
                    continue
                else:
                    stack.append(penultimate)
                    
        return stack




        # lets add asteroids to the stack. when we have a sign mismatch lets
        # do some explosion math/logic. 

        # can no longer explode when all signs are the same 
        # OR all - on left and + on right
```
### OR chat GPT solution

```python
        from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] < -asteroid:
                    stack.pop()
                elif stack[-1] == -asteroid:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(asteroid)

        return stack
```
