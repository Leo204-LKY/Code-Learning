## Session 3: Conditional structures and loops 条件结构和循环  
### Conditional statements 条件语句  
- 在许多情况下，程序需要进行比较来决定下一步要做什么  
- 在 Java 中，条件操作通常使用 if…then 结构实现  

```java
if (condition) { // 条件：布尔表达式（如比较）或布尔值
    do this // 条件为真
}
else {
    do that // 条件为假
}
```

#### 大括号/花括号  
- 注意，Java 允许在编写只包含一条语句的 if 语句时省略大括号  
- 但是，建议始终使用它们来避免难以注意到的错误  

```java
// ✔️
if (x > y) {
    System.out.println("x>y");
}

if (x > y)
    System.out.println("x>y");

// ❌
if (x > y);
    System.out.println("x>y");
```
#### 使用 if 的比较例  
```java
// Example of comparison with if
import java.util.Scanner; // needed for input
public class ComparisonIf {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter x: "); int x = input.nextInt(); 
        System.out.print("Enter y: "); int y = input.nextInt(); 
        if( x == y ) {
            System.out.printf("%d == %d\n", x, y);
        }
        if( x < y ) {
            System.out.printf("%d < %d\n", x, y);
        } 
        if( x > y ) {
            System.out.printf("%d > %d\n", x, y);
        } 
    }
}
```
```shell
$ java ComparisonIf
Enter x: 5
Enter y: 5
5 == 5
$
$ java ComparisonIf
Enter x: 0
Enter y: 1
0 < 1
$
$ java ComparisonIf
Enter x: 55
Enter y: 10
55 > 10
$
```

### 布尔运算符  
- 使用布尔运算符来组合条件：!（NOT），&&（AND）及 ||（OR）  
```java
if (x > a && y > a) {
    System.out.println("x > a and y > a!");
}
if (x > a || y > a) {
    System.out.println("x > a or y > a!");
}
if (!(x > y)) {
    System.out.println("x <= y!");
}
```

### _if...else_ 语句  
大多数 Java 程序员喜欢将前面的嵌套 if...else 语句写成：  
```java
if (studentGrade >= 90) {
    System.out.println("A");
}
else if (studentGrade >= 80) {
    System.out.println("B");
}
else if (studentGrade >= 70) {
    System.out.println("C");
}
else if (studentGrade >= 60) {
    System.out.println("D");
}
else {
    System.out.println("F");
}
```
- **注意**：按照惯例，Java 中的变量名标识符使用首字母小写的驼峰命名惯例（例如 `firstNumber`、`studentGrade`）  

### _switch...case_ 语句  
有时使用 switch...case 结构代替多重比较是合理的：  
```java
switch (control) { // 变量“control”将在不同条件下进行测试
    case 0:
        // 当变量的值为 0 时，完成以下操作
        do something
        break; // 退出 switch
    case 1:
        // 当变量的值为 1 时，完成以下操作
        do something else
        break;
    default:   // 默认操作
        // 当变量的值不慢速上述任何情况时，默认完成以下操作
        error handling etc.
        break;
}
```

#### 使用 if 结构的比较例  
```java
// Example of conditional statements with case
import java.util.Scanner; // needed for input
public class TestCase {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Choose 1 or 2: "); int value = input.nextInt(); 
        switch(value) {
            case 1:
                System.out.println("You chose 1!");
                break; 
            case 2:
                System.out.println("You chose 2!");
                break; 
            default:
                System.out.println("You did not choose 1 or 2!");
                break; 
        } 
    }
}
```
```shell
$ java TestCase
Choose 1 or 2: 1
You chose 1!
$
$ java TestCase
Choose 1 or 2: 2
You chose 2!
$
$ java TestCase
Choose 1 or 2: 3
You did not choose 1 or 2!
$
```

### 操作符的优先级和逻辑性  
| 操作符 | 结合性 | 类型 |
| --- | --- | --- |
| \*   /   $ | 从左到右 | multiplicative |
| +   - | 从左到右 | additive |
| <   <=  > | 从左到右 | relational |
| ==  != | 从左到右 | equality |
| = | 从右到左 | assignment |

### 条件运算符（?:）  
- 条件运算符（`?:`）是 if...else 的简略写法  
    - 三元（ternary）运算符（接受三个操作数）  
- 操作数和 `?:` 构成*条件表达式*  
  ```java
  <Boolean expression> ? <if true> : <if false>
  // Example:
  System.out.printls(StudentGrade >= 60 ? "Passed" : "Failed");
  ```
    - `?` 左边的操作数是布尔表达式，其值为布尔值（true 或 false）  
    - 第二个操作数（在 `?` 和 `:` 之间）是布尔表达式为真时的值  
    - 第三个操作数（在`:`的右边）是布尔表达式为假时的值  
#### 条件运算符例  
```java
// Example of conditional operator
import java.util.Scanner; // needed for input
public class ClassCond {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Write your age: "); 
        int age = input.nextInt(); 
        String str = age < 18 ? "minor" : "adult";
        System.out.printf("You are %s!\n", str);
    }
}
```
```shell
$ java ClassCond
Write your age: 10
You are minor!
$
$ java ClassCond
Write your age: 50
You are adult!
$ 
```
- 条件运算符允许编写紧凑的代码，但要注意：它会使代码难以阅读，并容易出现错误！  

### 遍历语句 _while_  
- 在某些情况下，如果条件仍然为真，程序需要多次重复操作  
- 在 Java 中，`while` 循环语句可用于此目的  
```java
while (condition) { // 条件：布尔表达式（如比较）或布尔值
    do this // 条件为真时做这些，然后再次判断条件是否为真，重复
}
// 如果条件为假，跳出循环，继续执行后续代码
continue here
```
#### while 使用例  
- 找出第一个大于 100 的 3 的幂  
  ```java
  product = 3;
  while (product <= 100)
      product = 3 * product;
- 每次迭代都将乘积乘以 3，因此乘积的值依次为 9、27、81 和 243  
- 当乘积变为 243 时，乘积 <= 100 变为 false  
- 迭代结束，积的最终值为 243  
- 程序继续执行 while 语句后的下一条语句  

### 遍历语句 _do...while_  
- 迭代语句 `do...while` 类似于 `while` 语句  
- 在 while 语句中，在执行循环正文***之前***，在循环*开始时*测试循环终止条件；如果条件为*假*，则正文永远不会执行  
- `do...while` 语句在执行循环正文***之后***测试循环终止条件；因此，正文*总是至少执行一次*  
- 当 `do...while` 循环终止时，会按顺序继续执行下一条语句  
#### do...while 使用例  
```java
// Example of do..while loop
public class DoWhileTest {
    public static void main(String[] args) {
        int counter = 1; // initialize counter

        do { 
            System.out.printf("%d ", counter);
            ++counter;
        } while (counter <= 10);

        System.out.println();
    }
}
```
```shell
1 2 3 4 5 6 7 8 9 10
```

### _for_ 循环  
- _for_ 循环在很多编程语言中都能见到  
- Java 中，_for_ 循环有以下头语句  
  ```java
  for (int counter = 1; counter <= 10; counter++) {...}
  ```
    - `int counter = 1` - 初始化表达式：启动循环时，将控制变量的值初始化为 1  
    - `counter < 10` - 测试表达式：如果测试表达式为真，则重复循环  
    - `counter++` - 更新表达式：在每次迭代中更新控制变量  
#### for 循环使用例  
```java
// Example of for loop
public class ForTest {
    public static void main(String[] args) {

        for (int counter = 1; counter <= 10; counter++) { 
            System.out.printf("%d ", counter);
        } 

        System.out.println();
    }
}
```
```shell
1 2 3 4 5 6 7 8 9 10
```