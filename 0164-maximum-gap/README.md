<h2><a href="https://leetcode.com/problems/maximum-gap/">164. Maximum Gap</a></h2><h3>Medium</h3><hr><div><p>Given an integer array <code>nums</code>, return <em>the maximum difference between two successive elements in its sorted form</em>. If the array contains less than two elements, return <code>0</code>.</p>

<p>You must write an algorithm that runs in linear time and uses linear extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,6,9,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [10]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The array contains less than 2 elements, therefore return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>


SOUTION:


Idea

Suppose in our integer array N elements, the min value is min and the max value is max. Then the maximum gap will be greater or equal to ceiling[(max - min ) / (N - 1)].
Let bucketSize = ceiling[(max - min ) / (N - 1)].
We divide all numbers in the array into N buckets, each bucket has size of bucketSize, where i-th (zero-based index) bucket contains all numbers in range [min + i*bucketSize, min + (i+1)*bucketSize).
Because maximum gap is always greater or equal to bucketSize so in each bucket, we only need to store max element and min element, skip middle elements (min < middle < max) in the same bucket.
Finally, we only need to compare max number in current bucket and min number in next bucket to get the relatively large gap and find out which two bucket have the maximum gap.
Example picture
image

Complexity

Time: O(N)
Space: O(N)

![image](https://github.com/ms5914/leetcode_practice_in_python/assets/55366357/9d54cc8b-2133-4d9b-9273-8015ce69c920)

