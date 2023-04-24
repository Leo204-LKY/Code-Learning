# Lecture 10: Binary Search Trees 二叉查找树  

## Binary Search 二分查找  
二分查找可以对有序映射(map)执行最近邻查询，有序映射是由一个按键(key)排序的数组实现的，类似于 high-low children 的游戏:  
- 在每一步中，候选项的数量减半  
- 在O(log n)步长后终止，例如: `find(7)`  

![find(7)](https://user-images.githubusercontent.com/57821066/233935599-1abd1b47-2466-4284-878b-c103b624a31e.png)  

## Search Tables 查找表  
- 查找表是通过有序序列实现的有序映射  
    - 我们将元素存储在基于数组的序列中，按键排序  
    - 我们使用外部比较器来比较键  
- 性能:  
    - 使用二分查找时，查找时间为O(log n)  
    - 插入一个新元素的时间复杂度为O(n)，因为在最坏的情况下，我们需要移动n/2个元素来为新元素腾出空间  
    - 移除一个元素的时间复杂度为O(n)，因为在最坏的情况下，我们需要移动n/2个元素来压缩移除后的元素  
- 查找表只对小尺寸的有序映射有效，或者对搜索是最常见操作的映射有效，而插入和删除很少执行(例如，信用卡授权)。  

## Sorted Map Operations 排序映射操作  
- 标准的序列方法：  
    ![Standard Map methods](https://user-images.githubusercontent.com/57821066/233937392-eca10981-c560-4d61-8050-20516bd2c9ce.png)  
- 排序映射ADT包括额外的功能，保证迭代按排序顺序报告键，并支持额外的搜索，如 `find_gt(k)` 和 `find_range(start, stop)`  

## Binary Search Trees 二叉查找树/二叉搜索树  
- 二叉搜索树是一棵在其节点上存储键(或键值项)并满足以下属性的二叉树：  
    - 设 `u`, `v`, `w` 为三个节点上的键，使得 `u` 在 `v` 的左子树中， `w` 在 `v` 的右子树中，则有`键(u) ≤ 键(v) ≤ 键(w)`  
- 外部节点不存储项，而是将其视为 `None`  
- 二叉搜索树的无序遍历以递增的顺序访问键
    ![Binary Search Tree Example](https://user-images.githubusercontent.com/57821066/233942915-791af527-c840-4cb6-8f0a-ead18aad2859.png")  

### 二叉树与决策树类似
![Image](https://user-images.githubusercontent.com/57821066/233943197-32b5ecd1-7ec3-4c14-b028-90638ed38bd7.png)
> Is the key  
> - Equal to key at position p, (search done),  
> - If greater, search right subtree,  
> - If less, search left subtree  

## 搜索  
为了查找键 `k`，我们从根开始向下追踪一条路径  
访问的下一个节点取决于将 `k` 与当前节点的键值进行比较  
如果到达叶节点，则表示没有找到键  
```
Algorithm TreeSearch(T, p, k):
    **if** k == p.key() **then**
        **return** p                         {Successful search}
    **else if** k < p.key() and T.left(p) is not None **then**
        return TreeSearch(T, T.left(p), k)   {Recur on left subtree}
    **else if** k > p.key and T.right(p) is not None **then**
        return TreeSearch(T, T.right(p), k)  {Recur on right subtree}
    **return** p                             {Unsuccessful search}
```

### 二分查找依赖于时间深度  
我们在每一层花费O(1)时间，所以总时间(在最坏的情况下)取决于高度  
![Total Time](https://user-images.githubusercontent.com/57821066/233945542-1824ad35-7ac1-4e92-a0e6-67fbbf0baad6.png)  

## Insertion 插入  
![Insertion](https://user-images.githubusercontent.com/57821066/233947434-28ccaac4-60ad-4790-8404-118be2e83812.png)  

## Deletion 删除  
### 删除时可能需要移动节点
![Deletion Example 1](https://user-images.githubusercontent.com/57821066/233948247-4e95c74e-cf6b-45bd-9432-336546725f59.png)  
- 我们移除了 32，并将子节点上移  
- 如果 32 是外部的(external)，那么只需移除即可  

### 删除时节点级别可能会提高  
![Deletion Example 2](https://user-images.githubusercontent.com/57821066/233948851-30044193-fcf7-40d5-b7c2-36374c334833.png)  
- 当删除一个元素时，我们需要考虑子节点右边的子树，这样树才能保持有序。  

## 二叉查找树的性能与高度(Height)有关  
- 高度 `h` 在最坏情况下是 `O(n)` ，在最好情况下是 `O(log n)`  
- `find_range()` 方法也依赖于项的数量  

![Operations and its running time](https://user-images.githubusercontent.com/57821066/233949807-ac49f58f-3544-4537-984d-2e3518a26fa2.png)

## 在 Python 中实现二叉查找树  
见 `10-2-BST-Implementation.py`  