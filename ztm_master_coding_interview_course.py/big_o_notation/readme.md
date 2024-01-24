[![S0OIe.png](https://s13.gifyu.com/images/S0OIe.png)](https://gifyu.com/image/S0OIe)
*source: https://www.bigocheatsheet.com/*

# Table of contents
1. [Time complexity](#time)
2. [Space complexity](#space)

# Time complexity <a name="time"></a>

An essential concept we must learn is Big O notation. This is because we need to measure how fast our algorithm can be, and also, how much memory does it requires. Keeping this on mind, **can help us to write more scalable code** , which by the way, is a requirement if we want to write great code.

When it comes to time complexity, there are three essential ones we need to learn. 
1. First one is *constant time*, represented as **O(1)** where our algorithm, no matter how big the input is, we just do one thing and that is it.

2.  Second one is *linear time*, represented as **O(n)** where our algorithm depends on the input (n), which means the computer will be affected on how large is it the input.

3. Third one is *quadratic time*, represented as **O(n^2)**. At this point the algorithm is pretty inefficient since based on the input, the algorithm will iterate over that input two times every iteration.

> Note: As the graphic above can show, there is more notations we did not specified. I just focused on the key ones, but you can google the rest of them if you want : D

# Space complexity <a name="space"></a>

Ok, now that we know how fast or not an algorithm could be measured, we need to know what happens to the memory right?

Most of the times when optimizing an algorithm, there is trade-offs. For example, if you want to optimize your code in terms of time complexity, your space most likely will be affected, and vice-versa when optimizing in terms of space complexity, but for this time since we are focused on getting a job, interviewers tend to optimize our codes in terms of time complexity.

What can cause space complexity? Based on the information gathered from the course, there are four things that affect space complexity:
- Variables
- Data structures (Arrays, tuples, dictionaries, objects, trees, linked list, etc.)
- Function calls
- Allocations

**As an example of a linear time** complexity, or O(1) using Python:

```python
def constant_space_example(n):
	sum_result = 0

	for i in range(1, n + 1):
		sum_result += i

	return sum_result
```
As we can see, we are just using one variable and returning it.


