## Session 2: Java language basics  
### 主题  
- 在今天剩下的课程中，我们将介绍 Java 编程语言的基础知识  
    - 基本的Java控制台程序结构
    - 转义序列，格式化打印，控制台输入
    - 基本类型、算术运算、比较
    - 条件结构和循环
    - 数组和数组列表
- 大部分材料是基于 _Java: How to Program_ 第2、4、5、7章的幻灯片，可从 MyAberdeen 获取  

### 学习目标  
今天的理论课后，你们应该能够  
- 编写简单的 Java 控制台程序，将输出打印到控制台并从键盘接收用户输入  
- 使用变量、基本的算术运算和比较  
- 实现条件结构和循环  
- 定义和初始化数组和数组列表，并将它们用于简单的任务，如计算数组中元素的和  

### 如何编写一个基础的 Java 程序？  
- Java 程序被组织成包含方法的类  
    - 基本规则是公共 Java 类的源代码必须保存在与公共类同名的 .java 文件中  
    - 类和方法将在后面更详细地解释  
- 每个 Java 程序都需要一个带有*公共*静态方法（_public_ static method） main 的*公共*类（_public_ class）作为程序的起点  
    - 当使用 `java MyClass` 命令启动 MyClass 程序时，程序在 MyClass 类的方法 main 中启动  

### 声明类和方法  
- 声明类的基本语法：  
  ```java
  public static class MyClass {...}
  ```
    - `public static`：修饰符（modifiers，可选）  
    - `class`：关键字 class  
    - `MyClass`：类名  
    - `{...}`：类主体（在大括号内）  
- （在类内）声明方法的基本语法：  
  ```java
  protected final void myMethod(int a, int b) {...}
  ```
    - `protected final`：修饰符（可选）  
    - `void`：返回值类型（若不返回内容则为 `void`）  
    - `myMethod`：方法名  
    - `(int a, int b)`：参数（可为空）  
    - `{...}`：方法主题（在大括号内）  

#### 一个简单的 Java 控制台程序例  
```java
// 使用双斜杠 // <comments> 或 /* <comments> */ 在程序内创建注释（会被编译器忽略）
// Example text-printing Java program Welcome1.java

// 每个 Java 程序需要至少一个类
public class Welcome1 {
    // main method begins execution of Java application
    // main 方法是整个程序的起点
    public static void main(String[] args) {
        System.out.println("Welcome to Java programming!");
        // 内建方法 System.out.println 用于在控制台输出一行文字
    } // end section main
} // end class Welcome1
```
```shell
$ javac Welcome1.java           # 编译 Welcome1.java 中的代码
$ java Welcome1                 # 运行编译的程序 Welcome1
Welcome to Java programming!    # 程序的输出
$
```
- 修改 main 中的代码：  
  ```java
  System.out.print("Welcome to ");
  System.out.println("Java programming!");
  ```
  输出如下：
  ```shell
  $ java Welcome2
  Welcome to Java programming!
  $ 
  ```
- ```java
  System.out.println("Welcome\nto\nJava\nprogramming!");
  ```
  输出如下：
  ```shell
  $ java Welcome3
  Welcome
  to
  Javaprogramming!
  $
  ```

### 转义序列  
| 转义符 | 描述 |
| --- | --- |
| `\n` | 换行符。将屏幕光标置于*下一行*的开头 |
| `\t` | 水平制表符（Horizontal tab）。将屏幕光标移动到下一个制表位 |
| `\r` | 回车。将光标定位在当前行的开头。`\r`之后输出的任何字符都将覆盖当前行的字符 |
| `\\` | 反斜杠。用于打印反斜杠字符（\） |
| `\"` | 双引号。用于打印双引号字符（"） |

### 使用 printf 格式化输出  
- 使用 `System.out.printf` 将输出打印到控制台  
    - `f` 代表“格式化”（formatted）：`printf` 展示格式化数据  
- 参数放在逗号分隔的列表中  
- 调用（calling）方法也被称为 _invoking_ a method  
- Java 允许将大型语句拆分为许多行  
    - 但是，不能在标识符或字符串的中间分割语句  
#### printf 的参数  
- 方法 `printf` 的第一个参数是一个*格式字符串*  
    - 可能包含*固定的文本*（_fixed text_）和*格式说明符*（_format specifiers_）  
    - 固定文本的输出方式与 `print` 或 `println` 方法的输出方式相同  
    - 每个格式说明符都是一个值的占位符，并指定要输出的数据类型  
- 格式说明符是百分号 (%) 后跟代表数据类型的字符  
- 对于字符串（string）， `%s` 是占位符，对于 整型（int），`%d` 是占位符  
- 其他占位符：`%f` 表示浮点数，`%b` 表示布尔值  
#### 格式化输出例  
```java
// Example formatted printing Java program

public class Welcome4 {
    // main method begins execution of Java application
    public static void main(String[] args) {
        System.out.printf("%s%n%s%n", "Welcome to", "Java programming!")
    } // end section main
} // end class Welcome4
```
```shell
Welcome to
Java programming!
```
- 注：`\n` 和 `%n` 都可用于换行  

### 声明变量  
- 在 Java 中，使用变量前需要先声明它们  
- 声明一个变量并使用其默认值：  
  ```java
  public int number;
  ```
    - `public`：修饰符（可选）  
    - `int`：数据类型  
    - `number`：变量名  
- 声明一个变量并给其赋值：  
  ```java
  private double number = 5.8;
  ```
    - `private`：修饰符（可选）  
    - `double`：数据类型  
    - `number`：变量名  
    - `5.8`：为变量赋的值  

### Java 中的原始类型  
原始类型不是从其他数据类型派生而来的  
| 类别 | 长度（位） | 值范围 |
| --- | --- | --- |
| boolean 布尔 | 1 | true 或 false |
| char 字符 | 16 | 0 至 65535 |
| byte 字节 | 8 | -128 至 +127（-2⁷ 至 +2⁷-1） |
| short | 16 | -32,768 至 +32,767（-2¹⁵ 至 +2¹⁵-1） |
| int | 32 | -2³¹ 至 +2³¹-1（约 10⁹） |
| long | 64 | -2⁶⁴ 至 +2⁶⁴-1（约 10¹⁹） |
| float （单精度）浮点数 | 32 | 约 (+/-)1.4\*10^(-45) 至 3.4\*10³⁸ |
| double 双精度浮点数 | 64 | 约 (+/-)4.9\*10^(-324) 至 1.8\*10³⁰⁸ |

### 有输入和整数的格式化打印  
```java
// Example formatted printing Java program with input
import java.util.Scanner // need for input
public class Addition {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter first integer: "); // prompt
        int number1 = input.nextInt(); // read first number
        System.out.print("Enter second integer: "); // prompt
        int number2 = input.nextInt(); // read second number
        int sum = number1 + number2; // add numbers and store the result
        System.out.printf("Sum is: %d%n", sum);
    }
}
```

### 导入的类  
- 每个 Java 程序都会默认导入 java.lang 包（package）；因此，java.lang 中的类（如 System）是唯一不需要导入的类  
- 在前面的示例中，需要使用 Scanner 类来使程序能够读取数据供程序使用  
    - 数据有多种来源，例如键盘上的用户或磁盘上的文件  
    - 在使用 Scanner 之前，必须创建它并指定数据源  

### 二进制溢出  
- 在其他一些编程语言（如 C 语言）中，变量可能会溢出其分配的位数范围  
    - 例如，对于字节，127+1 的结果是 -128  
- 在 Java 中，这种情况通常是可以避免的，并且会出错，但对于 int 和 long 类型，二进制溢出仍有可能发生。对大数要谨慎！  
```shell
java Addition
Enter first integer: 2000000000
Enter second integer: 2000000000
Sum is: -294967296
```

### 浮点数的格式化打印  
```java
// Example formatted printing Java program with input
import java.util.Scanner; // needed for input
public class Addition2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter x: "); // prompt
        float x = input.nextFloat(); // read first number
        Syetem.out.print("Enter y: "); // prompt
        float y = input.nextFloat(); // read second number
        float sum = x + y; // add numbers and store the result
        System.out.printf("Sum is: %f%n", sum);
        System.out.printf("Sum is: %.2f%n", sum);
    }
}
```
```shell
Enter x: 1.255
Enter y: 2.75
Sum is: 4.005000
Sum is: 4.01
```

### Java 中的算术运算  
| Java 运算 | 运算符 | 代数表达式 | Java 表达式 |
| --- | --- | ---- | --- |
| Addition 加 | + | $f + 78$ | f + 78 |
| Substraction 减 | - | $f - c$ | f - c |
| Multiplication 乘 | \* | $bm$ | b * m |
| Division 除以 | / | $x/y$（或分数表示） | x / y |
| Remainder 取余 | % | _r_ mod _s_ | r % s |
#### 算术优先级  
- Java 中的算术操作遵循标准优先级  
    - 首先计算**乘法**、**除法**和**余数**（\*、/、%）。如果有多个这种类型的操作符，则*从左到右*求值  
    - 接下来计算**加法**和**减法**（+，-）。如果有多个这种类型的操作符，则*从左到右*求值  
    - 最后计算**赋值**（=）  
- 为了提高可读性和避免错误，可以在复杂表达式中使用括号

### 相等和关系操作符  
| 代数符号 | Java 操作符 | Java 例 | 含义 |
| --- | --- | --- | --- |
| **=** | == | x == y | x 等于 y |
| **≠** | != | x != y | x 不等于 y ||
| **＞** | > | x > y | x 大于 y |
| **＜** | < | x < y | x 小于 y |
| **≥** | >= | x >= y | x 大于或等于 y |
| **≤** | <= | x <= y | x 小于或等于 y |
#### 比较和布尔例  
```java
// Example comparison Java program
import hava.util.Scanner
public class Comparison {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter x: "); // prompt
        int x = input.nextInt(); // read first number
        System.out.print("Enter y: "); // prompt
        int y = input.nextInt(); // read second number
        boolean isLarger = x > y; // compare if x is larger than y
        boolean isLess = x < y; // compare if x is less than y
        System.out.printf("x is larger than y: %b%n", isLarger);
        System.out.printf("x is less than y: %b%n", isLess);

    }
}
```
```shell
$ java Comparison
Enter x: 5
Enter y: 10
x is larger than y: false
x is less than y: true
$
$ java Comparison
Enter x: 5
Enter y: 5
x is larger than y: false
x is less than y: false
$
$ java Comparison
Enter x: 10
Enter y: 5
x is larger than y: true
x is less than y: false
$
```