# Day 11: Strings and collections 字符串和集合  
- 目标  
    - 能在 Java 程序中使用字符串、字符串构建器和字符串操作  
    - 能使用基本的正则表达式 (RegExp) 操作  
    - 能在 Java 程序中使用列表和迭代器实现集合  

## Session 1: Strings and basic string operations 字符串和基本字符串操作  

### 字符串简介  
- 在许多 Java 程序中，字符串和字符串操作是必不可少的  
    - 字符串（`String`）类的实例代表一个字符串，即一个字符序列  
    - 字符串类提供了多种创建和操作字符串的方法：在前面的课程中，我们已经使用了一些基本的字符串操作  
- String 对象是不可变的（immutable）  
    - String 对象的内容在创建后无法更改；这就是为什么许多字符串方法实际上是创建了一个被操作的原始字符串副本的原因  

### 字符串构造函数  
- String 类提供了构造函数，可通过多种不同方式初始化 String 对象  
    - 在没有参数的情况下，会创建一个空字符串；但是，由于字符串是不可变的，空字符串通常没有价值  
      ```java
      String s0 = new String();                 // s0 = ""
      ```
    - 你可以使用常量字符串作为参数  
      ```java
      String s1 = new String("hello");          // s1 = "hello"
      ```
    - 也可以使用 String 对象作为参数来创建副本  
      ```java
      String s2 = new String(s1);               // s2 = "hello"
      ```
    - String 类还提供了可接受字符或字节数组作为参数的构造函数  
      ```java
      char[] = charArray = {'b', 'i', 'r', 't', 'h', ' ', 'd', 'a', 'y'};
      String s3 = new String(charArray);        // s3 = "birth day"
      String s4 = new String(charArray, 6, 3);  // s4 = "day"
      ```
        - `String(array, start, count)`
            - `start`：访问数组中字符的起始位置（偏移量）  
            - `count`：要访问的字符数（计数）  

### 将字符串初始化为字面量  
- 在 Java 中，字符串对象也可以通过赋值*字符串字面量（string literal）* 来创建，而无需使用关键字 new  
  ```java
  String s = "hello";
  ```
- 需要注意的是，关键字 new **总是**创建一个新的字符串对象，而通过字面量创建的字符串将引用现有对象，如果字符串字面量库中已经存在类似字符串的话  
    - 由于字符串对象是不可变的，因此两者的差别实际上微不足道  
#### 字符串字面量例  
```java
public class StringLiteralExample {
    public static void main(String[] args) {
        String s1 = "hello";                // 在内存中新建 "hello"
        String s2 = new String("hello");    // 在内存中新建 "hello"
        String s3 = "hello";                // 在内存中指向 s1 所在的位置

        // 注意，比较 (==) 适用于指针，而不是指针指向的数据！
        System.out.println("Are s1 and s2 same? " + (s1 == s2));
        System.out.println("Are s1 and s3 same? " + (s1 == s3));
        System.out.println("Are s2 and s3 same? " + (s2 == s3));
    }
}
```
输出：  
```shell
$ java StringLiteralExample
Are s1 and s2 same? false
Are s1 and s3 same? true
Are s2 and s3 same? false
$
```

### 基本字符串方法  
字符串的基本方法包括  
- int `length()`：返回长度（字符串中的字符数）  
- char `charAt(pos)`: 返回参数 `pos` 中指定位置的字符（注意第一个字符位于 0 位置）  
- void `getChars(begin,end,dest,destBeg)`：将字符串中的字符复制到字符数组中  
    - int `beg`：复制开始的索引  
    - int `end`：最后一个要复制的字符的下一个索引  
    - char[] `dest`：目标字符数组  
    - int `destBeg`：目标数组中的起始偏移量  
#### 基本字符串方法例  
```java
public class BasicStringExample {
    public static void main(String[] args) {
        String str = "hello world!";

        // 向后循环打印字符，并逐个打印。注意，最后一个字符位于索引位置 length()-1
        for (int i = str.length() - 1; i >= 0; i--) {
            System.out.printf("%c", str.charAt(i));
        }
        System.out.println();

        // 将字符串索引 6 至索引 10 中的字符复制到字符数组 charArr 中
        char[] charArr = new char[5];
        str.getChars(6, 11, charArr, 0);
        System.out.println(charArr);
    }
}
```
输出：  
```shell
$ java BasicStringExample
!dlrow olleh
World
$
```

### 字符串比较  
- 请注意，Java 比较运算符 `==` 比较的是引用（指针），而不是字符串的内容  
- 要比较两个字符串的内容，可以使用 `equals()` 和 `compareTo()` 方法  
    - 如果参数字符串包含与此对象相同的字符序列，方法 `equals()` 将返回 true  
    - 方法 `equalsIgnoreCase()` 与 `equals()` 类似，但忽略大小写  
    - 方法 `compareTo()`
        - 如果该字符串按词典顺序（字母顺序）排在参数字符串之前，则返回一个负整数  
        - 如果字符串相等，则返回 0  
        - 如果该字符串按词典顺序排在参数字符串之后，则返回正整数  
#### 字符串比较例  
```java
public class BasicStringComparisonExample {
    public static void main(String[] args) {
        String s1 = "albert";
        String s2 = "Albert";
        String s3 = "Bertha";

        System.out.printf("%s equals %s: %b%n", s1, s2, s1.equals(s2));
        System.out.printf("%s equalsIgnoreCase %s", s1, s2, s1.equalsIgnoreCase(s2));
        System.out.printf("%s compareTo %s", s2, s3, sa.compareTo(s3));
        System.out.printf("%s compareTo %s", s3, s2, s3.compareTo(s2));
    }
}
```
输出：
```shell
$ java BasicStringComparisonExample
albert equals Albert: false
albert equalsIgnoreCase Albert: true
Albert compareTo Bertha: -1
Bertha compareTo Albert: 1
$
```

### 比较字符串区域（即 substrings 子字符串）  
- 要比较字符串的区域而非完整字符串，可使用方法 `regionMatches()`  
    - 如果指定区域中的子字符串（子串）相等，则返回 true  
- 两个版本（四个或五个参数）  
    - 方法 `regionMatches(off1, str2, off2, len)`：如果从本字符串中 off1 位置开始的长度为 len 的子字符串与参数字符串 str2 中 off2 位置开始的长度为 len 的子字符串相等，则返回 true  
    - `regionMatches(ignoreCase,off1,str2,off2,len)` 方法中，还有一个布尔类型的第一参数，用于确定是否忽略大小写  

### 从字符串中提取子字符串  
- 提取子串时，可使用方法 `substring()`  
    - 返回通过复制现有字符串对象的一部分创建的新字符串对象  
- 两个版本（一个或两个参数）  
    - 方法 `substring(start)` 返回从位置索引 start 开始到字符串最后一个字符结束的子字符串  
    - 方法 `substring(start,end)` 返回从位置索引 start 开始到位置索引 end（不包括）的子串  
#### 使用 `regionMatches()` 和 `substring()` 的例子  
```java
public class RegionMatchesExample {
    public static void main(String[] args){ 
        String s1 = "Hello World!";
        String s2 = "good morning world!";

        System.out.println("Regions matching: " + s1.regionMatches(6, s2, 13, 6)); 
        System.out.println("Regions matching with case ignored: " + s1.regionMatches(true, 6, s2, 13, 6));
        System.out.println("Substring of s1 from 6 to end: " + s1.substring(6));
        System.out.println("Substring of s2 from 13 to 17: " + s2.substring(13, 18));
    } 
}
```
输出：  
```java
$ java RegionMatchesExample
Regions matching: false
Regions matching with case ignored: true
Substring of s1 from 6 to end: World!
Substring of s2 from 13 to 17: world
$
```