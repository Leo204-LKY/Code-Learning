# Lecture 9.2: Hash Tables 哈希表  

### 重要性  
- 哈希表是实现映射最实用的数据结构之一  
- Python 的字典以哈希表的形式实现  

### 回忆一下映射的概念
直观地说，映射M支持使用 `M[k]` 这样的语法将键抽象为索引。  
作为热身，考虑一个受限设置，在这个设置中，一个具有 `n` 个项的映射使用的键已知是范围从 `0` 到 `N − 1` 的整数，对于某些 `N≥n` 。  
![image](https://user-images.githubusercontent.com/57821066/232949831-e0f0d37c-007c-4224-b58f-4606e3c7bd14.png)  

### 如果要存储的物品比空间多，那么我们可以把它们放进桶(bucket)里  
![image](https://user-images.githubusercontent.com/57821066/232950153-46799da2-f190-4e10-a859-bbc43eb89404.png)  
我们可以使用哈希函数将项分配到桶数组的索引中  
> 目标是使用哈希函数 `h(k)` 将项目 `(k, v)` 存储在桶 `A[h(k)]` 中  

### 一个哈希函数包含两部分  
![image](https://user-images.githubusercontent.com/57821066/232950654-7f578db0-2f86-4725-97d6-e365d992ee68.png)  
- Hash code 哈希码：将一个键映射到一个整数  
- Compression function 压缩函数：将哈希码映射为 bucket 数组索引范围 `[0, N-1]` 内的整数  

## 哈希函数与哈希表  
- 哈希函数 `h` 将给定类型的键映射到固定间隔内的整数 `[0, N - 1]`  
- 例：`h(x) = x mod N` 是整数键值的哈希函数  
    - 整数 `h(x)` 称为键 `x` 的哈希值  
- 给定键类型的哈希表包含：  
    - 哈希函数 `h`  
    - 大小为 `N` 的数组（称为表）  
- 在使用哈希表实现映射时，目标是在索引 `i = h(k)` 处存储项 `(k, o)`  

### 哈希函数的目标是随机分散键  
哈希函数通常被指定为两个函数的组合：  
- Hash code 哈希码 - `h₁`: keys → integers  
- Compression function 压缩函数 - `h₂`: integers → [0, N - 1]  

首先应用哈希码，然后对结果应用压缩函数，即 `h(x) = h₂(h₁(X))`  
哈希函数的目标是以一种明显随机的方式“分散”键  

## Hash Codes 哈希码  
- Memory address 内存地址  
    - 我们将键对象的内存地址重新解释为一个整数（除了数字键和字符串键）  
- Integer cast  
    - 将键的位置(the bits of the key)重新解释为整数  
    - 适用于长度小于或等于整数位数的键  
- Component sum 组件和  
    - 我们将键的位置分割成固定长度的组件（如 16 位或 32 位），并将组件相加（忽略溢出）  
    - 适用于大于或等于整数位数的固定长度的数字键(numeric keys)  
- Polynomial accumulation 多项式积累
    - 我们将键的位置分割成固定长度（如 8 位、 16 位或 32 位）的组件序列 `a0`, `a1`, ..., `a[n-1]`  
    - 计算固定值 `z` 的多项式 `p(z) = a0 + a1*z + a2*z^2 + ... + a[n-1]z^(n-1)` ，忽略溢出  
        - 特别适合于字符串（例如，选择 `z = 33` 时，在 50,000 个英语单词的集合上最多给出 6 次冲突[collisions]）  
    - 多项式 `p(z)` 可以在 `O(n)` 时间内使用霍尔法则计算：  
        - 依次计算以下多项式，其中每个多项式都是 `O(1)` 时间内的前一项  
            - `p0(z) = a[n-1]`  
            - `pi(z) = a[n-i-1] + zp[i-z](z)`（i = 1, 2, ..., n - 1）  
        - 有 `p(z) = p[n-1](z)`  

## Compression Functions 压缩函数  
### 使冲突(collisions)最小化  
- 除法(Division)： `y mod N`  
    - 桶数组的大小 N 通常被选为素数  
    - 原因与数论有关，超出了这门课的范围  
- 乘法、加法和除法(Multiply, Add and Divide [MAD])：`[(ay + b) mod p] mod n`
    - 整数 `y`, `p` 是大于 `N` 的质数。`a` 和 `b` 是随机选择的非负整数，使得模(mod) `N≠0` 。否则，每个整数都映射到相同的值 `b`  

## 抽象哈希表类  
```Python
class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression."""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map."""
        self._table = cap * [None]
        self._n = 0                         # number of entries in the map
        self._prime = p                     # prime for MAD compression
        self._scale = 1 + randrange(p - 1)  # scale from 1 to p-1 for MAD
        self._shift = randrange(p)          # shift from 0 to p-1 for MAD

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)   # may raise KeyError

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)       # subroutine maintains self._n
        if self._n > len(self._table) // 2: # keep load factor <= 0.5
            self._resize(2 * len(self._table) - 1)  # number 2^x - 1 is often prime

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)      # may raise KeyError

    def _resize(self, c):               # resize bucket array to capacity c
        old = list(self._items())       # use iteration to record existing items
        self._table = c * [None]        # then reset table to desired capacity
        self._n = 0                     # n recomputed during subsequent adds
        for (k, v) in old:
            self[k] = v                 # reinsert old key-value pair
```

## 解决冲突很有必要  
- 当不同元素被映射到同一个单元时，就会发生冲突(collision)  
- Separate Chaining 分离链：让表中的每个元素指向映射到表中的条目的链表  
> 单独的链接很简单，但是需要额外的表外内存  

![image](https://user-images.githubusercontent.com/57821066/232959151-56bd4aba-8626-45c2-97b6-e68c264aac8c.png)  

### 带有分离链的哈希表
```Python
class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error" + repr(k))       # no match found
        return bucket[k]                                # may raise KeyError

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()         # bucket is new to the table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:               # key was new to the table
            self._n += 1                                # increase overall map size

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error:' + repr(k))      # no match found
        del bucket[k]                                   # may raise KeyError

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:                      # a nonempty slot
                for key in bucket:
                    yield key
```