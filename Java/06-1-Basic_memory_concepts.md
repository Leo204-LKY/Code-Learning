# Day 6: Memory concepts and exceptions  
- 目标：  
- 能解释内存的基本概念，如破坏性处理和非破坏性处理之间的区别，以及逐值传递和逐引用传递  
- 能使用递归实现算法  
- 能在 Java 代码中使用 try...catch 结构处理异常  
- 定义和使用自己的自定义异常  

## Session 1: Basic memory concepts  

### 内存的概念  
- Java 中的每个变量都有一个*名称（name）*、一种*类型（type）*、一个*大小*（*size*，以字节为单位）和一个*值（value）*  
    - 名称可将变量彼此区分开来  
    - 大小取决于类型  
    - 值可在程序执行过程中改变（除非变量是最终变量）  
- 初始化变量时，JVM 会在计算机工作内存中为变量分配空间  
    - 为变量分配新值时，会丢失旧值（destructive process 破坏性过程）  
    - 当读取变量值时，它可以被使用，但不会发生变化（nondestructive process非破坏性过程）  
#### 例子  
- 非破坏性过程例
    1. 初始化  
       ![Memory concepts example 1-1](img/06-1-01-Memory_concepts_example-1-1.png)  
    2. 初始化 x  
       ![Memory concepts example 1-2](img/06-1-02-Memory_concepts_example-1-2.png)  
    3. 初始化 y  
       ![Memory concepts example 1-3](img/06-1-03-Memory_concepts_example-1-3.png)  
    4. 初始化 z  
       ![Memory concepts example 1-4](img/06-1-04-Memory_concepts_example-1-4.png)  
    5. 使用 z 的值  
       ![Memory concepts example 1-5](img/06-1-05-Memory_concepts_example-1-5.png)  
    6. 结束执行  
       ![Memory concepts example 1-6](img/06-1-06-Memory_concepts_example-1-6.png)  
- 破坏性过程例  
    1. 初始化  
       ![Memory concepts example 2-1](img/06-1-07-Memory_concepts_example-2-1.png)  
    2. 初始化 x
       ![Memory concepts example 2-2](img/06-1-08-Memory_concepts_example-2-2.png)  
    3. 为 x 重新赋值  
       ![Memory concepts example 2-3](img/06-1-09-Memory_concepts_example-2-3.png)  
    4. 使用 x 的值  
       ![Memory concepts example 2-4](img/06-1-10-Memory_concepts_example-2-4.png)  
    5. 结束执行  
       ![Memory concepts example 2-5](img/06-1-11-Memory_concepts_example-2-5.png)  

### 引用类型变量  
- 不是原始类型变量的变量是引用类型变量（reference type variables）：变量包含指向实际数据内存位置的引用（指针）  
    - 数组和对象引用是引用类型变量  
- 请注意修改变量（指针）和修改变量指向的数据之间的区别！  
#### 引用类型变量例  
1. `x[]`  
   ![Reference type variable example-1](img/06-1-12-Reference_type_variable_example-1.png)  
2. `y[]`  
   ![Reference type variable example-2](img/06-1-13-Reference_type_variable_example-2.png)  
3. `z[]`  
   ![Reference type variable example-3](img/06-1-14-Reference_type_variable_example-3.png)  
4. x、y、z 数组的哈希值  
   ![Reference type variable example-4](img/06-1-15-Reference_type_variable_example-4.png)  
   ![Reference type variable example-5](img/06-1-16-Reference_type_variable_example-5.png)  
   ![Reference type variable example-6](img/06-1-17-Reference_type_variable_example-6.png)  
5. 结束  
   ![Reference type variable example-7](img/06-1-18-Reference_type_variable_example-7.png)  

### 复制方法：`clone()`  
- 如果要复制引用数据的完整副本，而不仅仅是另一个引用，可以使用方法 `clone()`  
  ![Deep copy method clone()](img/06-1-19-Deep_copy_method-clone.png)  

### 逐值传递与逐引用传递  
- 在许多编程语言（如 C++）中，在方法调用中传递参数有两种方式：逐值传递（或逐值调用）和逐引用传递（逐引用调用）  
    - 逐值传递：将参数值的副本传递给被调用方法。被调用方法只使用副本。对副本的更改不会影响原始变量的值  
    - 逐引用传递：被调用方法可以直接访问调用者中的参数值，并在必要时修改该数据。这样就无需复制大量数据，从而提高了性能  
- 在 Java 中，你无法选择让*所有参数都通过值传递*  
#### 逐值传递例子  
![Pass-by-value example-1](img/06-1-20-Pass-by-value_example-01.png)  
![Pass-by-value example-2](img/06-1-21-Pass-by-value_example-02.png)  
![Pass-by-value example-3](img/06-1-22-Pass-by-value_example-03.png)  
![Pass-by-value example-4](img/06-1-23-Pass-by-value_example-04.png)  
![Pass-by-value example-5](img/06-1-24-Pass-by-value_example-05.png)  
![Pass-by-value example-6](img/06-1-25-Pass-by-value_example-06.png)  
![Pass-by-value example-7](img/06-1-26-Pass-by-value_example-07.png)  
![Pass-by-value example-8](img/06-1-27-Pass-by-value_example-08.png)  
![Pass-by-value example-9](img/06-1-28-Pass-by-value_example-09.png)  
![Pass-by-value example-10](img/06-1-29-Pass-by-value_example_10.png)  
![Pass-by-value example-11](img/06-1-30-Pass-by-value_example_11.png)  