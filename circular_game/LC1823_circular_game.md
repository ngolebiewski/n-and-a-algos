# Leet Code 1823. Find the Winner of the Circular Game
https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/


# Nick Mock interview solution

1823. Find the Winner of the Circular Game

```python
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        make a list of the n players
        object{player number + bool isAlive?}

        while loop.
        ongoing counter.
        some sort of modulo math in relation for the length of the array.


        go circularly through the list.
        where we are in list when we delete a number out -  !!Mutation caution!!
        end state: 1 left and output the player number.


        [1,2,3,4,5]
        k = 2
        1 2 (player 2 is out)   [1, 3, 4, 5]
        3 4 (player 4 is out).  [1, 3, 5]
        5 1 (player 1 is out)   [3,5]
        3 5 (player 5 is out).  [3]
        3 is the winner.

        at best ologn - On2


        """
        players = [num + 1 for num in range(n)]
        position = 0

        while len(players) > 1:
            next =  (position + k - 1) % len(players)
            print(next)

            position = next

            del players[next] # bad time usage
            print(players)

            if position > len(players) - 1:
                position = 0

        return players[0]
```

## A solution

```python

List Iteration:
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Initialize list of N friends, labeled from 1-N
        circle = list(range(1, n + 1))

        # Maintain the index of the friend to start the count on
        start_index = 0

        # Perform eliminations while there is more than 1 friend left
        while len(circle) > 1:
            # Calculate the index of the friend to be removed
            removal_index = (start_index + k - 1) % len(circle)

            # Remove the friend at removal_index
            circle.pop(removal_index)

            # Update the start_index for the next round
            start_index = removal_index

        return circle[0]
```


The catch here is that this has a Time complexity of O(n^2), since the inner pop() call can take O(n) time in worst case

```python
Queue implementation:
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Initialize deque with n friends
        circle = deque(range(1, n + 1))

        # Perform eliminations while more than 1 player remains
        while len(circle) > 1:
            # Process the first k-1 friends without eliminating them
            for _ in range(k - 1):
                circle.append(circle.popleft())
            # Eliminate the k-th friend
            circle.popleft()

        return circle[0]
The queue implementation only has O(n) time
```

