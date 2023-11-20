## Session 2: Formatted file writting and reading 格式化文本读取/写入  

### 使用 Formatter 写入格式化数据  
- Java 不对文件施加任何结构；文本文件基本上只是单个字符流，没有特定的结构  
    - 为满足应用程序的要求，你需要确定文件中存储的数据结构  
- 要将格式化的字符串输出到文件，可以使用 java.util 包中的 Formatter 类  
    - 提供与 `System.out.printf()` 方法类似的功能  
    - `format()` 方法用于生成输出，`flush()` 方法用于刷新数据，`close()` 方法用于关闭格式器  
#### 使用 Formatter 的例子  
```java
import java.io.*;
import java.util.Formatter;

public class WriteFormattedData {
    public static void main(String[] args) {
        String[] names = {"Scissors", "Hammer", "Screwdriver"};
        int[] codes = {15002, 1840, 22567};
        double[] prices = {10.20, 15.30, 9.95};

        try {
            // 创建格式化对象，写入文件 products.txt
            Formatter out = new Formatter("products.txt");
            for (int i = 0; i < names.length; i++) {
                // 使用 format() 方法写入格式化数据
                out.format("%s %05d %.2f\n", names[i], codes[i], prices[i]);
                // 使用 flush() 方法完成写入
                out.flush();
            }
        } catch (Exception e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
```
输出：  
```shell
$ java WriteFormattedData
$
```
文件 products.txt：  
```
Scissors 15002 10.20
Hammer 01840 15.30
Screwdriver 22567 9.95
```

### 使用 Scanner 读取格式化数据  
- 使用 Scanner 类，我们可以逐行读取文本文件，或使用正则表达式解析原始类型和字符串  
    - 我们之前已经使用 Scanner 从键盘读取了输入内容！  
    - 方法 `nextLine()` 以字符串对象的形式返回文件中的下一行  
    - 方法 `next()` 可用于使用 regex 模式（默认情况下使用空白分隔符）逐个标记（逐个子串）读取字符串  
    - 方法 `nextBoolean()`、`nextByte()`、`nextDouble()`、`nextFloat()`、`nextInt()` 和 `nextLong()` 可用于读取特定原始数据类型的文本  
        - 注意，文件中错误的数据类型可能会导致异常！  
#### 使用 Scanner 的例子  
```java
import java.io.*;
import java.util.Scanner;

public class ReadFormattedData {
    public static void main(String[] args) {
        System.out.printf("%-15s%-10s%-10s%n", "Product", "Code", "Price");

        try {
            // 创建与文件关联的 Scanner 对象
            File file = new File("products.txt");
            Scanner in = new Scanner(file);
            while (in.hasNext()) { // 方法 hasNext() 测试是否有更多数据可用
                System.out.printf("%-15s%-10d%-10.2f%n", in.next(). in.nextInt(), in.nextDouble()); // 读取特定类型的项目（字符串、int、double）
            }
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
```
文件 products.txt：  
```
Scissors 15002 10.20
Hammer 01840 15.30
Screwdriver 22567 9.95
```
输出：  
```
$ java WriteFormattedData
Product        Code      Price 
Scissors       15002     10.20 
Hammer         1840      15.30 
Screwdriver    22567     9.95
$
```

### 从文件中检索（retrieve）数据  
- BufferReader 和 Scanner 对象按顺序检索数据  
    - 从文件开头开始读取，连续读取所有数据，直到找到所需信息为止  
    - 无法重新定位到文件开头：如果需要再次读取文件，程序必须关闭文件并重新打开  
    - 在程序执行过程中，可能需要多次（从文件开头）顺序处理文件  
- 如果文件不是很大，用数据结构一次性读取所有内容（例如，用字符串列表表示每一行）会更有效率  
#### 从文件检索数据例  
```java
import java.io.*;
import java.util.Scanner;

public class RetrieveFormattedData {
    public static void main(String[] args) {
        String itemToFind = "Hammer";

        try {
            File file = new File("products.txt");
            Scanner in = new Scanner(file);
            while (in.hasNext()) {
                String item = in.next();
                int code = in.nextInt();
                double price = in.nextDouble();

                if (item.equals(itemToFind)) {
                    System.out.println("Price of %s is £%.2f\n", item, price);
                    break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```
文件 products.txt：  
```
Scissors 15002 10.20
Hammer 01840 15.30
Screwdriver 22567 9.95
```
输出：  
```
$ java RetrieveFormattedData
Price of Hammer is £15.30
$
```

### 将 CSV 文件读入数组  
- CSV（Comma-Separated Values，逗号分隔值）文件包含用逗号分隔符分隔的条目信息  
    - 在文本文件中存储表格数据的常用文件格式  
    - 使用 Formatter 类等轻松创建 CSV 文件  
- 将 CSV 文件读入数组的方法有以下几种  
    - 使用 Scanner 或 BufferReader 类  
    - 使用第三方库 OpenCSV：可将其作为依赖项添加到 Maven 项目的 pom.xml 文件中进行安装（OpenCSV 在频繁处理大型 CSV 文件时非常有用）  
#### 使用 Scanner 读取 CSV 文件  
```java
import java.io.*;
import java.util.*;

public class ReadCSVWithScanner {
    public static void main(String[] args) {
        // 值存储在二维列表（列表的列表）中
        List<List<String>> records = new ArrayLIst<>();

        try {
            File file = new File("products.csv");
            Scanner scanner = new Scanner(file);
            // 循环读取文件中的行
            while (scanner.hasNextLine()) {
                String[] values = scanner.nextLine().split(",");
                    // 注意使用分隔符“,”将字符串分割成标记（字符串数组）
                records.add(Arrays.asList(values));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(records);
    }
}
```
文件 products.csv：  
注意，除逗号分隔符外，products.csv 与 products.txt 类似  
```
Scissors,15002,10.20
Hammer,01840,15.30
Screwdriver,22567,9.95
```
输出：  
```shell
$ java ReadCSVWithScanner
[[Scissors, 15002, 10.20], 
[Hammer, 01840, 15.30], 
[Screwdriver, 22567, 9.95]]
$
```
#### 使用 BufferReader 读取 CSV 文件  
```java
import java.io.*;
import java.util.*;

public class ReadCSVWithBufferReader {
    public static void main(String[] args) {
        List<List<String>> records = new ArrayList<>();

        // 使用 Scannner 执行与上一示例类似的功能
        try {
            BufferReader br = new BufferReader(new FileReader("products.csv"));
            String line;
            while ((line = br.readLine()) != null) {
                String[] values = line.split(",");
                records.add(Arrays.asList(values));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(records);
    }
}
```
输出：  
```shell
$ java ReadCSVWithBufferedReader
[[Scissors, 15002, 10.20], 
[Hammer, 01840, 15.30], 
[Screwdriver, 22567, 9.95]]
$
```

### Binary files 二进制文件  
- 二进制文件不是文本文件：二进制文件被视为字节流（或比特流），而不是字符流  
    - 二进制文件比文本文件更紧凑地存储数字数据  
        - 例如，一个 32 位整数的十进制表示法在文本文件中最多可占用 11 个字符（每个字符 16 位）  
    - 二进制文件通常具有特定的应用程序结构，用于存储非文本数据，如图像、音频、可执行程序等  
        - 通常，解析二进制文件需要深入了解相关的特定文件格式  

### 在 Java 中使用二进制文件  
- FileOutputStream 类可用于写入二进制文件  
    - 方法 `write()` 可用于将单个字节或字节数组写入文件  
- FileInputStream 类可用于读取二进制文件  
    - 方法 `read()` 可用于将单个字节或字节序列读入字节数组  
- 这两个类都是通过使用文件名作为构造函数的参数来实例化的，并使用方法 `close()` 关闭  
- java.nio 包提供了字节缓冲器（ByteBuffer）类，用于在原始类型和它们作为字节数组的表示形式之间进行转换  
#### 使用二进制文件例  
```java
import java.io.*;
import java.nio.ByteBuffer;

public class BinaryFileExample {
    public static void main(String[] args) {
        int[] data = {1786, 45, 567};

        // 通过分配字节数来实例化 ByteBuffer 对象；在 Java 中，int 为 32 位（4 个字节）
        ByteBuffer buf = ByteBuffer.allocate(4);

        try {
            // 创建并打开 FileOutputStream 对象
            FileOutputStream out = new FileOutputStream("datafile.bin");
            for (int i = 0; i < data.length; i++) {
                // 在索引 0 的字节缓冲区位置放入一个 int
                buf.putInt(0, data[i]);
                // 将字节缓冲区内容（字节数组）写入文件
                out.write(buf.array());
            }
            out.close();

            // 创建并打开 FileInputStream 对象
            FileInputStream in = new FileInputStream("datafile.bin");
            // 重复，直到剩下的字节少于 4 个
            while (in.available() >= 4) {
                // 读取字节缓冲区中的数据
                in.read(buf.array());
                // 从字节数组索引 0 位置获取 int
                System.out.printf("%d. int: %d\n", i + 1, buf.getInt());
            }
            in.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```
输出：  
```shell
$ java BinaryFileExample
Read int: 1786
Read int: 45
Read int: 567
$
```