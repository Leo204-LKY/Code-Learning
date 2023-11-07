## Session 2: Interfaces 接口  

### 接口  
- 有了**接口**，互不相关的类就可以实现一套通用方法：人和系统可以通过接口以标准化的方式进行交互  
- 例：收音机上的控制器是收音机用户与收音机内部组件之间的接口  
    - 提供一套有限的操作（如更换电台、调节音量、在调幅 AM 和调频 FM 之间进行选择）  
    - 不同的收音机可能以不同的方式实现控制（如使用按钮、转盘、语音指令等）  
    - 接口规定了收音机必须允许用户控制的操作（***what***），但没有规定如何进行操作（***how***）  

### Java 中的接口  
- Java 接口描述了一组可在对象上调用的方法  
- 接口声明以关键字 `interface` 开头，通常只包含常量和抽象方法  
    - 所有接口成员*必须*是公共的  
    - 接口中声明的强制方法隐含为公共抽象方法  
    - 所有字段都是隐式公共、静态和最终字段  
- 接口不能被实例化，因此它没有定义构造函数

### 在类中使用接口  
- 要使用接口，具体类必须指定它实现了接口，并用指定的签名声明接口中的每个方法  
- 没有实现接口所有方法的类是抽象类，必须声明为抽象类  
    - 实现接口就像与编译器签订合同：*“我将声明接口指定的所有方法，否则我需声明自己为抽象类”*  
#### 使用接口的例子  
```java
abstract class Animal {
    protected boolean hungry = true;
}

interface Feedable {
    public void feed();
}

class Cat extends Animat implements Feedable {
    public void feed() {
        hungry = false;
    }
}

public class InterfaceExample1 {
    public static void main(String[] args) {
        Cat cat = new Cat();
        cat.feed();
        System.out.print("Is the cat hungry? ");
        System.out.println(cat.hungry ? "Yes" : "No");
    }
}
```
输出：  
```shell
$ java InterfaceExample1
Is the cast hungry? No
```

### Java 接口的新特性  
- 从 Java SE 8 开始，接口还可包含具有具体默认实现的公共（public）默认方法，这些默认实现可指定在未重载的情况下如何执行操作  
    - 如果一个类实现了这样的接口，该类也会接收接口的默认（default）实现（如果有的话）  
    - 要声明默认方法，请在方法的返回类型前加上关键字 `default`，并提供一个具体的方法实现  
- 从 Java SE 8 开始，接口可包含静态方法  
- 从 Java SE 9 开始，接口也可以包含私有方法，但定义受保护方法会导致编译错误  
#### 接口使用默认方法的例子  
```java
abstrace class Animal {
    protected boolean hungry = true;
}

interface Feedable {
    public default void feed() {
        System.out.println("No method for feeding!");
    }
}

class Cat extends Animal implements Feedable {}

public class InterfaceExample2 {
    public static void main(String[] args) {
        Cat cat = new Cat();
        cat.feed;
        System.out.print("Is the cat hungry? ");
        System.out.println(cat.hungry ? "Yes" : "No");
    }
}
```
输出：  
```shell
$ java InterfaceExample2
No method for feeding!
Is the cat hungry? Yes
```

### 使用多个接口  
- Java 不允许子类从一个以上的超类继承（多重继承）；但是，一个类可以从一个超类继承，并根据需要实现多个接口  
- 要实现多个接口，请在类声明中的关键字 `implements` 后使用以逗号分隔的接口名称列表，例如  
  ```java
  public class Subclass extends Superclass implements
      FirstInstance, SecondInstance {...}
  ```
- Java API 包含大量接口，许多 Java API 方法都会接收接口参数并返回接口值  

### 什么时候使用接口  
- 当不同的类（即不相关的类）需要共享共同的方法和常量时，通常会使用接口  
    - 通过响应相同的方法调用，允许多态处理不相关类的对象  
    - 您可以创建一个描述所需功能的接口，然后在任何需要该功能的类中实现该接口  
- 当没有默认实现可继承时，应使用接口代替抽象类  
- 与公共抽象类一样，接口通常也是公共的  
    - 公共接口必须在与接口名称相同的文件中声明，文件扩展名为 .java  

### 多接口中的同名方法  
- 如果一个类实现了两个接口，而这两个接口都定义了一个同名的默认方法，那么该类**必须**覆盖该方法并提供一个实现  
- 可以使用以下语法调用接口默认方法之一：  
  ```java
  InterfaceName.super.method();
  ```
#### 使用多接口的例子  
```java
interface Pianist {
    default void play() { System.out.println("Bling blong"); }
}

interface Violinist {
    default void play() { System.out.println("Viih vooh"); }
}

class Musician implements Pianist, Violinist {
    public void play() {
        Pianist.super.play();
    }
}

public class MusicianExample {
    public static void main(String[] args) {
        new Musician().play();
    }
}
```
输出：  
```shell
$ java MusicianExample
Bling blong
```

### 扩展接口  
- 与类一样，接口也可以扩展  
    - 扩展接口继承超级（superinterface，即父接口）的所有方法  
- 一个接口可以扩展多个超级接口
- 实现该接口的类必须实现接口直接定义的抽象方法，以及从所有超接口继承的所有抽象方法  
#### 扩展接口的例子  
```java
interface Scalable  { void scale(double scaler);    }
interface Rotatable { void rotate();                }
interface Transformable extends Scalable, Rotatable {}

class Rectangle implements Transformable {
    public double w, h;
    public Rectangle(double w, double h) { this.w = w; this.h = h; }
    public void scale(double scaler) {this.w *= scaler; this.h *= scaler; }
    public void rotate() {
        double temp = this.w;
        this.w = this.h;
        this.h = temp;
    }
}

public class TransformableExample {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle(10.0, 5.0);
        rect.scale(0.5);
        System.out.printf("New dimensions: %f, %f\n", rect.w, rect.h);
    }
}
```
输出：  
```shell
$ java TransformableExampl
New dimensions: 5.000000, 2.500000
```

### 功能接口  
- 从 Java SE 8 开始，任何只包含一个抽象方法的接口都称为功能接口，也称为 SAM（Single Abstract Method 单抽象方法）接口  
- 可以使用可选注解 `@FunctionalInterface`  
- Java API 中定义的功能接口示例：  
    - 比较器（Comparator）——实现该接口可定义一种方法，用于比较给定类型的两个对象，以确定第一个对象是否小于、等于或大于第二个对象  
    - 可运行（Runnable）——实现该接口可定义与程序其他部分并行运行的任务  
#### 功能接口的例子  
```java
@FunctionalInterface
interface Talkable {
    void talk(String msg);
}

public class FunctionalInterfaceExample {
    public static void main(String[] args) {
        Talkable person = new Talkable() {
            public void talk(String msg) {
                System.out.println(msg);
            }
        };
        person.talk("Hello world!");
    }
}
```
输出：
```shell
$ java FunctionalInterfaceExample
Hello world!
```

### Lambda 表达式  
- *Lambda 表达式（lambda expression）* 是 Java SE 8 中引入的一项新功能，可用于表示功能接口的单个方法  
- Lambda 表达式的格式：
  ```java
  (argument list) -> { body }
  ```
    - 参数列表 `()` 可以为空或包含一个或多个参数  
    - 主体包含方法的实现  
- Lambda 表达式用于*函数式编程（functional programming）*  
    - 我们将在本课程稍后部分详细讨论 Lambda 表达式  
#### Lambda 表达式例  
```java
@FunctionalInterface
interface Talkable {
    void talk(String msg);
}

public class LambdaExample {
    public static void main(String[] args) {
        Talkable person = (msg) -> {System.out.println(msg);};
        person.talk("Hello World!");
    }
}
```
输出：  
```shell
$ java LambdaExample
Hello world!
```