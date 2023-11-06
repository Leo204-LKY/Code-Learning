# Day 4: Abstract classes and interfaces 抽象类和接口  
- 目标
    - 学会在 Java 程序中使用抽象类和接口  
    - 能使用抽象类和接口设计适当的类层次结构  

## Session 1: Abstract class 抽象类  
### 抽象类  
- *抽象类*是不能实例化为对象的类  
    - 只在继承层次中作为超类使用，因此有时被称为*抽象超类（abstract superclasses）*  
    - 不能用于实例化对象——抽象类不完整  
    - 子类必须声明“缺失的部分”，才能成为“具体”（concrete）类，你才能从中实例化对象；否则，这些子类也将是抽象的  
- 抽象类提供了一个超类，其他类可以从中继承，从而共享一个共同的设计  

### 抽象类 vs. 具体类  
- 可用于实例化对象的类是*具体类*  
    - 这些类为其声明的每个方法提供实现（implementations，其中一些实现可以继承）  
- 抽象超类过于笼统，无法创建真正的对象——它们只规定了子类之间的共同点  
- 具体类提供了使对象实例化成为可能的具体内容  
- 并非所有层次结构都包含抽象类  

### 声明抽象类  
- 使用关键字 `abstract` 来声明一个抽象类  
- 抽象类通常包含一个或多个*抽象方法（abstract methods）*  
    - 抽象方法是用关键字 `abstract` 定义的，如  
      ```java
      public abstract void draw(); // abstract method
      ```
    - 抽象方法不提供实现  
- 包含抽象方法的类必须是抽象类，即使该类包含一些具体（非抽象）方法  
- 抽象超类的每个具体子类也必须提供超类抽象方法的具体实现  
#### 定义抽象类例  
```java
public abstract class Shape {
// 注意，公有类必须放在自己的 java 文件中！
    public abstract double area();  // 抽象方法：注意用分号“;”代替正文“{...}”
    public abstract double circumference();
}
```
#### 扩展抽象类例  
```java
class Circle extends Shape {
    public static final double PI = 3.14159265358979323846;
    protected double r;
    public Circle(double r)         { this.r = r;         }
    public double getRadius()       { return r;           }
    public double area()            { return PI * r * r;  }
    public double circumference()   { return 2 * PI * r;  }
}
```
```java
class Rectangle extends Shape {
    protected double w, h;
    public Rectangle(double w, double h) {
        this.w = w;
        this.h = h;
    }
    public double getWidth()        { return w;           }
    public double getHeight()       { return h;           }
    public double area()            { return w * h;       }
    public double circumference()   { return 2 * (w + h); }
}
```
#### 测试继承类例  
```java
class TestShape {
    public static void main(String[] args) {
        Shape shape;
        shape = new Circle(5);
        System.out.println("Area: " + shape.area());
        shape = new Rectangle(5, 10);
        System.out.println("Area: " + shape.area());
    }
}
```
输出：  
```shell
Area: 78.53981633974483
Area: 50.0
```

### 覆写抽象类  
- 子类可以覆盖父类的公共非静态方法  
    - 如果超类包含抽象方法，具体子类<b><i><u>必须</b></i></u>覆盖这些方法！  
- `@Override` 注解的使用是可选的  
    - 但是，如果不使用 `@Override` 注解，编译器就不会检查你是否真的在覆盖一个现有方法  
#### 覆写抽象类例  
1. 正确示例  
    ```java
    abstract class Animal {
        public abstract void makeSound();
    }

    class Cat extends Animal {
        public void makeSound() {
            System.out.println("Meow!");
        }
    }

    class Dog extends Animal {
        public void makeSound() {
            System.out.println("Woff woff!");
        };
    }

    public class AnimalTest {
        public static void main(String[] args) {
            Cat cat = new Cat(); cat.makesound();
            Dog dog = new Dog(); dog.makesound();
        }
    }
    ```
    输出：
    ```shell
    $ java AnimalTest
    Meow!
    Woff woff!
    ```
2. 具体子类需要覆盖超类中的抽象方法  
    ```java
    abstract class Animal {
        public abstract void makeSound();   // <-- 抽象方法 makeSound()
    }
    class Cat extends Animal {
        public void makeNoise() {           // <-- 具体方法 makeNoise()
            System.out.println("Meow!");
        };
    }

    ...
    ```
    输出：
    ```shell
    $ javac AnimalTest.java
    error: Cat is not abstract and does not override abstract method makeSound() in Animal
    ```
3. 具体类则没有这些限制  
    ```java
    abstract class Animal {
        public void makeSound() {           // <-- 具体方法 makeSound()
            System.out.println("Burp!");
        }
    }
    class Cat extends Animal {
        public void makeNoise() {           // <-- 具体方法 makeNoise()
            System.out.println("Meow!");
        };
    }

    ...
    ```
    输出：
    ```shell
    $ java AnimalTest
    Burp!
    Woff woff!
    ```
4. `@override` 注解  
    ```java
    abstract class Animal {
        public void makeSound() {
            System.out.println("Burp!");
        }
    }
    class Cat extends Animal {
        @override
        public void makeNoise() {
            System.out.println("Meow!");
        };
    }

    ...
    ```
    输出：
    ```shell
    $ javac AnimalTest.java
    error: method does not override or implement a method from a supertype
    ```

### Dynamic binding 动态绑定  
- *动态绑定（或 late binding 延迟绑定）*：例如，Java 在执行时而不是编译时决定调用哪个类的方法  
    - 超类引用（reference）只能用于调用超类的方法——*子类*方法的实现是*多态调用*的  
- 试图在超类引用上直接调用子类专用方法会导致编译错误  
- 操作符 `instanceof` 可用于检查对象是否可以被转换为特定类型  
#### 多态处理（polymorphic processing）例  
```java
class TestShape {
    public static void main(String[] args) {
        Shape[] shapes = new Shape[3];
        shapes[0] = new Circle(3.0);
        shapes[1] = new Rectangle(5.0, 2.0);
        shapes[2] = new Rectangle(4.0, 4.0);

        double totalArea = 0.0;
        for (int i = 0; i < shapes.length; i++)
            totalArea += shapes[i].area;
        System.out.println("Total area: " + totalArea);
    }
}
```
输出：  
```
$ java TestShape
Total area: 54.27433388230814
```
#### `instanceof` 使用例  
```java
class TestShapeInstanceof {
    public static void main(String[] args) {
        Shape shape;
        shape = new Circle(5);

        if (shape instanceof Rectangle) {
            System.out.println("Shape is Rectangle!");
        }

        if (shape instanceof Circle) {
            System.out.println("Shape is Circle!");
        }
    }
}
```
输出：
```
$ java TestShapeInstanceof
Shape is Circle!
```
### 向子类转换的例  
```java
class ShrinkShape2 {
    public static void main(String[] args) {
        Shape shape = new Rectangle(1.0, 3.0);
        System.out.println("Original area: " + shape.area());
        if (shape instanceof Rectangle) {
            Rectangle rect = (Rectangle)shape;  // <--
            double w = rect.getWidth();
            double h = rect.getHeight();
            shape = new Rectangle(w / 2, h / 2);
            System.out.println("New area: " + shape.area());
        }
    }
}
```
输出：
```shell
$ java ShrinkShape2
Original area: 3.0
New area 0.75
```

### 获取一个类的信息  
- 每个对象都*知道自己的类*，并可通过 `getClass()` 方法访问这些信息  
    - getClass 方法返回一个 Class 类型的对象（来自 java.lang 包），其中包含对象类型的相关信息，包括其类名  
        - 注意，关键字 class 和类 Class 是不同的东西！  
    - getClass 调用的结果用于调用 `getName()` 获得对象的类名  
#### `getClass()` 例  
```java
abstract class Animal {
    public abstract void makeSound();
}

class Cat extends Animal {
    public void makeSound() {System.out.println("Meow!");}
}

class Dog extends Animal {
    public void makeSound() {System.out.println("Woff woff!");}
}

public class AnimalGetClass {
    public static void main(String[] args) {
        Animal animal = new Cat();
        Class cl = animal.getClass();
        System.out.println("Animal is " + cl.getName());
    }
}
```
输出：  
```shell
$ java AnimalGetClass
Animal is Cat
```

### 最终方法和类  
- 超类中的最终方法（final method）不能在子类中重写  
    - 声明为 `private`（私有）的方法隐含为最终方法，因为不可能在子类中覆盖这些方法  
    - 声明为 `static`（静态）的方法隐含为最终方法  
    - `final`（最终）方法的声明永远不会改变，因此所有子类都使用相同的方法实现，对最终方法的调用在编译时就已解决，这就是所谓的静态绑定  
- 最终类不能扩展以创建子类  
    - 最终类中的所有方法都是隐式最终方法  

### Java API 中的最终方法  
- String 类是最终类的一个例子  
    - 如果允许创建字符串的子类，那么该子类的对象就可以在任何需要使用字符串的地方使用了  
    - 由于字符串类无法扩展，因此使用字符串的程序可以依赖 Java API 中指定的字符串对象功能  
    - 将类设为最终类还能防止程序员创建子类，从而绕过安全限制  
- 请注意，在 Java API 中，***大多数***类都不是最终类  

### 从构造函数调用方法  
- ***不要在构造函数中调用可重载的方法***：在创建子类对象时，这可能导致在子类对象完全初始化之前就调用了重载方法  
    - 回想一下，当你构造一个子类对象时，它的构造函数会首先调用直接超类的一个构造函数  
    - 如果超类构造函数调用了可重载方法，子类版本的方法将被超类构造函数调用——在子类构造函数的主体执行之前  
    - 如果子类方法依赖于子类构造函数中尚未执行的初始化，就会出现难以检测的错误  
- 不过，从构造函数中调用 `static`（静态）方法是可以接受的  
#### 向子类转换例  
1. 子类会先调用超类中的构造函数，然后运行自己的构造函数  
    ```java
    abstract class Animal {
        public Animal() {
            System.out.println("Called constructor Animal");
        }
    }

    abstract class Mammal extends Animal {
        public Mammal() {
            System.out.println("Called constructor Mammal");
        }
    }
    class Cat extends Mammal {
        public Cat() {
            System.out.println("Called constructor Cat");
        }
    }
    public class ConstructorExample1 {
        public static void main(String[] args) {
            Cat cat = new Cat();
        }
    }
    ```
    ```shell
    $ java ConstructorExample1
    Called constructor Animal
    Called constructor Mammal
    Called constructor Cat
    ```
2. 
    ```java
    abstract class Animal {
        public String sound() { return "nothing"; }     // <--
        public Animal() {
            System.out.println("Animal says " + sound());
        }
    }
    class Cat extends Animal {
        public String sound() { return "meow"; }        // <--
        public Cat() {
            System.out.println("Cat says " + sound());
        }
    }

    public class ConstructorExample2 {
        public static void main(String[] args) {
            Cat cat = new Cat();
        }
    }
    ```
    输出：
    ```
    $ java ConstructorExample1
    Animal says meow
    Cat says meow
    ```