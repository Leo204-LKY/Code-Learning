## Session 3: Regular expressions 正则表达式  

### 正则表达式（regex）  
- 正则表达式（regular expressions，regex）是一个字符串，用于描述匹配其他字符串中字符的搜索模式  
    - 此类表达式可用于验证输入，确保数据符合特定格式  
- 正则表达式可用于执行所有类型的文本搜索和文本替换操作  
- 例如，大型复杂的正则表达式可用于验证程序的语法  
    - 如果程序代码与正则表达式不匹配，编译器就会知道代码中存在语法错误  

### 正则表达式符号  
- 一个 regex 由*字面字符（literal characters）* 和*元字符（metacharacters）* 组成  
    - 字面字符是具有字面意义的常规字符：例如，字符 `b` 是与字符“b”匹配的字面字符  
    - 元字符是在 regex 中具有特殊含义的字符：例如，元字符 `.`（点）可与任何字符匹配  
    - 有些元字符前面有转义序列 `\`（反斜杠）：例如，元字符 `\d` 可与任何数字匹配  
    - 反斜杠也用于区分字面字符和元字符：例如，`*` 是一个元字符，而 `\*` 是一个与字符“\*”（星号）匹配的字面字符  

### 部分常用元字符  
| 元字符 | 描述 |
| --- | --- |
| `.` | 匹配任意字符（换行符除外） |
| `^` | 匹配字符串的起始位置 |
| `$` | 匹配字符串的结束位置 |
| `*` | 与前一个元素匹配 0 次、1 次或多次 |
| `?` | 与前一个元素匹配 0 次或 1 次 |
| `+` | 与前面一个元素匹配 1 次或多次 |
| `\|` | 匹配以 `\|` 分隔的任何模式（patterns） |
#### 元字符使用的例子  
| Regex | ✔️匹配例 | ❌不匹配例 |
| --- | --- | --- |
| `bo.` | box 和 boy | but 和 bo |
| `^cat` | cat | a cat |
| `hat$` | hat 和 chat | hatch |
| `c*at` | at 和 cat 和 ccat | chat |
| `c?at` | at 和 cat | ccat |
| `c+at` | cat 和 ccat | at |
| `cat\|dog` | cat 和 dog | cow |

### 部分常用字符类  
- 字符类是继字面匹配之后最基本的 regex 概念  
    - 字符类由与特定类型字符（如数字或空格）匹配的元字符定义  
- 字符类别的一些常用示例：  
  | 字符 | 匹配 | 字符 | 匹配 |
  | --- | --- | --- | --- |
  | `\d` | 任意数字 | `\D` | 任意非数字 |
  | `\w` | 任意字母数字字符\* | `\W` | 任意非字母数字字符 |
  | `\s` | 任意空白符\*\* | `\S` | 任意非空白字符 |
  | `\b` | 单词边界\*\*\* |  |  |
- \* 字母数字字符 word character，匹配字母、数字、下划线  
  \*\* 空白字符 whitespace character 匹配任何空白字符，包括空格、制表符、换页符等等  
  \*\*\* 单词边界 word boundaries，即字与空格间的位置  

### 在正则表达式中使用括号  
- 括号 `[ ]` 用于匹配括号内的任何单个字符  
    - 例如，`[abc]` 匹配 a、b 和 c，而不是 d  
- 在括号内，元字符 `^` 用于匹配不包含在括号内的字符  
    - 例如，`[^ab]` 匹配 c 和 z，而不是 a 和 b  
- 在括号内， `-` 用于匹配范围内的字符  
    - 例如，`[a-d]` 匹配 a、b、c 和 d，而不是 e  

### Quantifiers 数量词  
Regex 数量词用于指定要匹配的序列长度  
| 数量词 | 描述 |
| --- | --- |
| `n{x}` | 匹配任何包含 x 次字符“n”（x 为数字）的字符串 |
| `n{x,y}` | 匹配任何包含至少 x 个但不多于 y 个字符“n”的序列的字符串 |
| `n{x,}` | 匹配任何至少包含 x 个字符“n”的字符串 |

### 用于执行 regex 操作的字符串方法  
- String 类提供了几种执行 regex 操作的方法  
    - 方法 `matches()` 将包含 regex 的字符串对象作为输入参数，只有当整个字符串与 regex 匹配时才返回 true  
    - 方法 `split()` 使用 regex 表达式作为输入，为标记化字符串找到分隔符  
    - 方法 `replaceAll()` 使用 regex 输入参数查找匹配的子串，并用替换参数替换它们  
    - 方法 `replaceFirst()` 与 `replaceAll()` 类似，但只替换第一个匹配的子字符串  
    - 请注意，String 方法 `replace()` 不支持 regex！  
#### 使用字符串方法的 regex 例  
```java
import java.util.Scanner;

public class StringRegexExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter 'stop' when you want to finish!");
        do {
            System.out.print("Enter the email: ");
            String input = scanner.nextLine();

            // 为简单起见，我们假设邮箱格式是 username@domain.xx
            // 且在用户名和链接处只接受小写字母
            if (input.matches("[a-z]+@[a-z]+\\.[a-z]{2,3}"))
            // [a-z]+ 匹配一个或多个小写字母
            // @ 匹配 @
            // \\. 匹配点号（注意，在 Java 字符串中，regex 字符“\.”必须写成“\\.”，因为 Java 编译器在编译 regex 之前会将反斜杠假定为转义字符！）
            // [a-z]{2,3} 匹配两个或三个小写字符组成的序列
            {
                System.out.println("Your email is valid!");
            } else if (input.matches("stop|Stop|STOP"))
            // 接受多种输入 stop 的方法
            {
                break;
            } else {
                System.out.println("Your email is invalid!");
            }
        } while (true);
    }
}
```
输出：  
```shell
$ java StringRegexExample
Enter 'stop' when you want to finish!
Enter the email: teacher@school.edu
Your email is valid!
Enter the email: james.smith@company.com
Your email is not valid!
Enter the email: STOP
$
```

### Pattern 和 Matcher 类  
- Java 没有任何内置的 regex 类，但我们可以导入 java.util.regex 包，使用以下类处理正则表达式  
    - 类 Pattern：定义模式（pattern，用于搜索）  
    - 类 Matcher：用于搜索模式  
    - 类 PatternSyntaxException：定义当 regex 字符串中出现语法错误时抛出的异常  

### 使用 Pattern 和 Matcher  
- 模式对象由静态方法 `Pattern.compile()` 创建  
    - 第一个参数是一个 regex 字符串，指定了要搜索的模式  
    - 第二个参数（可选）指定指示如何执行搜索的标志，例如，标志 `Pattern.CASE_INSENSITIVE` 指示忽略大小写  
- Pattern 对象的 `matcher()` 方法用于搜索输入参数所给字符串中的模式；该方法返回一个包含结果信息的 Matcher 对象  
- Matcher 对象的 find() 方法会在找到匹配的模式时返回 true；没有找到时返回 false  
#### Pattern 和 Matcher 例  
```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PatternMatcherExample {
    public static void main(String[] args) {
        // 编译日期格式为 dd/mm/yyyy 的模式匹配器
        // 注意，该 regex 只对日期进行弱验证
        Pattern pattern = Pattern.compile("[0-3]\\d/[0-1]\\d/\\d\\d\\d\\d");

        String text = "John Smith was born on 14/05/1973.\n" +
                      "His wife Jane was born on 09/12/1976.\n" +
                      "They had a son, born on 31/10/1997 " +
                      "and a daughter, born on 01/02/2001.";

        // 尝试在文本中找出指定的模式
        Matcher matcher = pattern.matcher(text);
        // 循环查找输入字符串中所有匹配的子字符串
        while(matcher.find()) {
            System.out.println("Date found " + matcher.group());
        }
    }
}
```
输出：  
```shell
$ java PatternMatcherExample
Date found: 14/05/1973
Date found: 09/12/1976
Date found: 31/10/1997
Date found: 01/02/2001
$ 
```