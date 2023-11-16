## Session 2: Advanced string and character operations 高级字符串和字符运算  

### Tokenising strings 字符串标记化  
- 将长字符串分割成更小的片段或标记通常很有用，例如从句子中提取单个单词  
    - 这一过程称为*标记化（tokenisation）*  
- String 类的 `split()` 方法可将字符串分解为多个部分（标记）  
    - 标记之间由分隔符分隔，通常是空白字符，如*空格、制表符、换行符和回车符*  
    - 其他字符也可用作分隔符来分隔标记  
    - `split()` 的参数包括分隔正则表达式和可选的最大标记数限制  
#### 标记化例
1. ```java
   import java.util.Scanner;
   public class TokenizingExample1 {
       public static void main(String[] args) {
           Scanner scanner = new Scanner(System.in);
           System.out.println("Enter a sentence and press Enter");
           String sentence = scanner.nextLine();
           String[] tokens = sentence.split(" "); // 分隔符为空格 " "

           System.out.printf("Number of tokens: %d%n", tokens.length);
           System.out.println("The tokens are:");
           for (String token : tokens) {
               System.out.println(token);
           }
       }
   }
   ```
   输出：  
   ```shell
   $ java TokenizingExample1
   Enter a sentence and press Enter:
   I like Java
   Number of elements: 3
   The tokens are:
   I
   like
   Java
   $ 
   ```
2. ```java
   import java.util.Scanner;
   public class TokenizingExample2 {
       public static void main(String[] args){ 
           Scanner scanner = new Scanner(System.in);
           System.out.println("Enter your email address:");
           String sentence = scanner.nextLine();
           String[] tokens = sentence.split("@", 2);
           // 分隔符为"@"，最多提取 2 个标记符

           System.out.printf("Your user name is: %s%n", tokens[0]);
           System.out.printf("Your URL is: %s%n", tokens[1]);
       }
   }
   ```
   输出：  
   ```shell 
   $ java TokenizingExample2
   Enter your email address:
   userName@example.com
   Your user name is: userName
   Your URL is: example.com
   $ 
   ```

### 串联字符串  
- String 的方法 `concat()` 可用来将两个 String 对象连接成一个新的 String 对象，其中包含两个字符串中的字符  
    - 语法：`s1.concat(s2)` 将连接字符串对象 s1 和 s2，使 s2 出现在 s1 之后  
- 在 Java 中，用于字符串对象的加法运算符 `+` 被定义为执行连接操作  
    - 假设 s1、s2 和 s3 都是字符串对象：  
      `s1 + s2` 与 `s1.concat(s2)` 效果相同  
      `s1 + s2 + s3` 与 `s1.concat(s2).concat(s3)` 效果相同  
#### 串联例  
```java
public class ConcatenationExample {
    public static void main(String[] args){ 
        String s1 = "Good ";
        String s2 = "morning ";
        String s3 = "world!";
        System.out.println(s1 + s2 + s3);
        System.out.println(s1.concat(s2).concat(s3));

        int age = 18;
        System.out.println("Michael is " + age + " years old");
        // 注意，如果数据类型不是字符串对象，Java 会在使用运算符 + 时自动将其转换为字符串表示法，但在使用 concat() 时则不会这么做
    }
}
```
输出：  
```shell
$ java ConcatenationExample
Good morning world!
Good morning world!
Michael is 18 years old
$
```

### 使用 StringBuilder 生产可修改字符串  
- 在经常执行字符串连接或其他字符串修改的程序中，使用类 StringBuilder 而不是类 String 通常会更有效率  
    - StringBuilder 是 String 的“可修改”版本：它提供了 `append()`、`insert()` 和 `delete()` 等方法来修改它所包含的字符串的内容  
    - 当修改一个 StringBuilder 对象时，它不会返回一个新的 StringBuffer 对象，而是更改原来对象的内容  

### StringBuilder 构造函数  
- StringBuilder 类提供了几种不同的构造函数  
    - `StringBuilder()`： 构造一个字符串生成器，不含任何字符，初始容量为 16 个字符  
    - `StringBuilder(CharSequence seq)`：构造一个字符串生成器，其中包含与 CharSequence 对象 `seq` 相同的字符  
    - `StringBuilder(int capacity)`：构造一个没有字符的字符串生成器，初始容量由容量参数指定  
    - `StringBuilder(String str)`：构造一个字符串生成器，初始化为字符串参数 `str` 的内容  

### StringBuilder 方法  
以下是一些最基本的 StringBuilder 类  
- `length()`：返回长度（字符数）；`setLength(int length)`：设置长度  
- `capacity()`：返回当前容量；`ensureCapacity()`：如果低于指定的最小容量，则增加容量  
- `charAt()`、`setCharAt()`、`getChars()`：获取和设置指定位置的字符  
- `append()`、`insert()`、`delete()`、`deleteCharAt()`：通过追加、插入和删除内容来修改字符串生成器；这些方法有多个重载版本，以支持不同的数据类型  
#### StringBuilder 例  
1. ```java
   public class StringBuilderExample1 {
       public static void main(String[] args){ 
           StringBuilder sb = new StringBuilder("Good morning world!");
           System.out.printf("Buffer = %s | length = %d | capacity = %d%n", sb.toString(), sb.length(), sb.capacity());

           sb.ensureCapacity(75);
           System.out.printf("New capacity = %d%n", sb.capacity());

           sb.setLength(10);
           System.out.printf("New buffer = %s | new length = %d%n", sb.toString(), sb.length());
       }
   }
   ```
   输出：  
   ```shell
   $ java StringBuilderExample1
   Buffer = Good morning world! | length = 19 | capacity = 35
   New capacity = 75
   New buffer = Good morni | new length = 10
   $
   ```
2. ```java
   public class StringBuilderExample2 {
       public static void main(String[] args){ 
           StringBuilder sb = new StringBuilder("Good morning world!"); 
           System.out.printf("Buffer = %s%n", sb.toString());

           char[] charArray = new char[7];
           sb.getChars(5, 12, charArray, 0);
           System.out.printf("Char array = ");
           for (char character : charArray) {
               System.out.print(character);
           } 

           sb.setCharAt(5,'M');
           sb.setCharAt(13,'W');
           System.out.printf("%nNew Buffer = %s%n", sb.toString());

           sb.deleteCharAt(sb.length()-1);
           sb.append(" Again!");
           System.out.printf("New Buffer = %s%n", sb.toString());
       }
   }
   ```
   输出：  
   ```shell
   $ java StringBuilderExample2
   Buffer = Good morning world!
   Char array = morning
   New Buffer = Good Morning World!
   New Buffer = Good Morning World Again!
   ```

### StringBuffer 类  
- 使用 StringBuilder 类创建的字符串构建器不是线程安全的： 
如果多个线程需要访问相同的动态（即可修改）字符串内容，应使用 StringBuffer 类而不是 StringBuilder 类  
    - StringBuilder 和 StringBuffer 这两个类提供了相同的功能，但只有 StringBuffer 是线程安全的（即同步）  
    - 如果*不*需要从多个线程访问同一个字符串生成器，StringBuilder 类比 StringBuffer 更快、更有效  

### 封装类  
- 在某些情况下，需要将基元类型值（primitive type values）视为对象（即引用类型值）  
    - Java 为布尔 Boolean、字符 Character、双精度浮点数 Double、浮点数 Float、字节 Byte、短 Short 和整数 Integer 等原始类型分别提供了封装类  
    - 将原始类型转换为封装类对象的推荐方法是使用每个类的静态方法 valueOf()，例如  
      ```java
      int iPrim = 1;
      Integer i = Integer.valueOf(iPrim);
      ```
    - 封装类也可以通过字面形式（*autoboxing 自动框选*）直接初始化  
      ```java
      Character c = 'A';
      Integer i = 5;
      ```

### Character 类方法  
- Character （字符）类方法可用于测试和操作单个字符值  
    - 每个方法至少需要一个字符作为输入参数  
    - 测试字符的方法包括：`isDefined()`、`isDigit()`、`isJavaIdentifierStart()`、`isJavaIdentifierPart()`、`isLetter()`、`isLetterOrDigit()`、`isLowerCase()` 和 `isUpperCase()`  
    - 操作字符的方法示例包括：`toUpperCase()` 返回字符的大写版本，`toLowerCase()` 返回字符的小写版本  
#### Character 例  
```java
public class CharacterExample {
    public static void main(String[] args) {
        // 不同的初始化方法
        char c = 'a';
        Character c1 = "A";
        Character c2 = Character.valueOf(c);

        System.out.printf("c1 = %c | c2 = %s%n", c1, c2.toString);

        // 不同比较方法
        // 注： equalsIgnoreCase() 是在 String 中定义的，而不是 Character
        System.out.printf("c1 and c2 are equal? %b%n", c1.equals(c2));
        System.out.printf("c1 and c2 are equal when case ignored? %b%n",
                          c1.toString().equalsIgnoreCase(c2.toString()));

        // 基本测试
        System.out.printf("'%c' is digit? %b%n", c1, Character.isdigit(c1));
        System.out.printf("'%c' is letter? %b%n", c1, Character.isLetter(c1));
        System.out.printf("'%c' is uppercase? %b%n", c1, Character.isUpperCase(c1));
        System.out.printf("'%c' is uppercase? %b%n", c2, Character.isUpperCase(c2));

        // 基本字符操作
        System.out.printf("'%c' in uppercase is %c%n", c1, Character.toUpperCase(c1));
        System.out.printf("'%c' in uppercase is %c%n", c2, Character.toUpperCase(c2));
    }
}
```
输出：  
```shell
$ java CharacterExample
c1 = A | c2 = a
c1 and c2 are equal? false
c1 and c2 are equal when case ignored? true
'A' digit? false
'A' letter? true
'A' uppercase? true
'a' uppercase? false
'A' in uppercase is A
'a' in uppercase is A
$
```