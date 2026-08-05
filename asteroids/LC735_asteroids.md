* Asteroids Leetcode 735 (Stack), Premium   https://leetcode.com/problems/asteroid-collision/description/


### A's solution:
```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = asteroids[::-1]
        pos = []
        res = []

        while len(s) > 0:
            curr = s.pop()
            if curr > 0:
                pos.append(curr)
            else:
                if len(pos) > 0:
                    curr_pos = pos.pop()
                    # Continually crush smaller asteroids
                    while abs(curr) > curr_pos and len(pos) > 0:
                        curr_pos = pos.pop()
                    # If of the same value, explode both (meaning don't add either anywhere)
                    if abs(curr) == curr_pos:
                        continue
                    # If a larger pos asteroid, put it back on the pos stack
                    if abs(curr) < curr_pos:
                        pos.append(curr_pos)
                    # No more pos asteroids, so this neg one will continue to move left with no collisions
                    if len(pos) == 0:
                        res.append(curr)
                else:
                    res.append(curr)
        # Add all pos asteroids to res
        return res + pos
```

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
