## Session 4: Liveness and high-level concurrency 实时性和高级并发性  

### Liveness 实时性  
- 应用程序及时执行的能力被称为 *“实时性”*  
- *死锁*、*饥饿*和*活锁*都会影响有效性  
    - 当两个线程相互阻塞时就会出现*死锁（deadlocks）*  
    - 当低优先级线程无法访问共享资源时，就会出现*饥饿（starvation）* 现象，因为这些资源被高优先级的“贪婪”线程占用了  
    - *活锁（livelocks）* 与死锁类似，但线程不会无限期阻塞，只是彼此响应太慢而已  
#### 死锁例  
```java
public class DeadLockExample {
    public static void main(String[] args) {
        String hammer = new String("Hammer");
        String nails = new String("Nails");

        // Worker 1
        Thread worker1 = new Thread() {
            public void run() {
                System.out.println("Worker 1 going to get hammer...");

                // hammer locked
                synchronized(hammer) {
                    System.out.println("Worker 1 got the hammer!");
                    try { Thread.sleep(1000); } catch (Exception e) {}

                    System.out.println("Worker 1 going to get nails...");

                    // nails locked
                    synchronized(nails) {
                        System.out.println("Worker 1 got the nails!");
                        System.out.println("Worker 1 does the work...");
                        try { Thread.sleep(5000); } catch (Exception e) {}
                        System.out.println("Worker 1 finished the work!");
                    }
                    // nails unlocked

                    System.out.println('worker 1 returned the nails!');
                }
                // hammer unlocked

                System.out.println("Worker 1 returned the hammer!");
            }
        };

        // Worker 2
        Thread worker2 = new Thread() {
            public void run() {
                System.out.println("Worker 2 going to get nails...");

                // nails locked
                synchronized(nails) {
                    System.out.println("Worker 2 got the nails!");
                    try { Thread.sleep(500); } catch (Exception e) {}

                    System.out.println("Worker 2 going to get hammer...");

                    // hammer locked
                    synchronized(hammer) {
                        System.out.println("Worker 2 got the hammer!");
                        System.out.println("Worker 2 does the work...");
                        try { Thread.sleep(5000); } catch (Exception e) {}
                        System.out.println("Worker 2 finished the work!");
                    }
                    // hammer unlocked

                    System.out.println('worker 2 returned the hammer!');
                }
                // nails unlocked

                System.out.println("Worker 2 returned the nails!");
            }
        };

        worker1.start();
        worker2.start();
    }
}
```
输出：  
```shell
$ java DeadLockExample
Worker 1 going to get hammer...
Worker 1 got the hammer!
Worker 2 going to get nails...
Worker 2 got the nails!
Worker 2 going to get hammer...
Worker 1 going to get nails...
```
- 程序陷入死锁，因为工人 1 拿着锤子，工人 2 拿着钉子，两个工人都无法继续…  

### 避免死锁  
- 避免嵌套锁（同步 synchronization 块之间相互嵌套）  
- 避免不必要的锁定：只锁定真正需要的对象  
- 尽可能使用不可变对象，而不是通过同步锁定对象  
    - 如果一个对象在构建后其状态无法改变，那么它就是不可变（immutable）的  
    - 不提供设置器（setter）方法，将所有字段定义为最终字段和私有字段  
- 调用线程 t 的 `t.join()` 方法，使其他线程在 t 结束后启动  
    - 定时版本 `join(m)` 最多等待 m 毫秒，否则线程中止  
#### 使用 `join()` 避免死锁的例子  
```java
public class DeadLockExample1 {
    public static void main(String[] args) {
        ... // 与之前例子中的代码相同

        try {
            worker1.start();
            worker1.join();
            worker2.start();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```
输出：  
```shell
$ java DeadLockExample2
Worker 1 going to get hammer...
Worker 1 got the hammer!
Worker 1 going to get nails...
Worker 1 got the nails!
Worker 1 does the work...
Worker 1 finished the work!
Worker 1 returned the nails!
Worker 1 returned the hammer!
Worker 2 going to get nails...
Worker 2 got the nails!
Worker 2 going to get hammer...
Worker 2 got the nails!
Worker 2 does the work...
Worker 2 finished the work!
Worker 2 returned the hammer!
Worker 2 returned the nails!
$ 
```

### High-level concurrency 高级并发性  
- 本课程迄今为止所讲解的并发功能（concurrency）都是基于对基本任务有用的低级 API，但不适用于更高级的任务  
- 包 java.util.concurrent 提供了更多高级功能  
    - 用于更复杂同步功能的*锁（lock）* 对象  
    - 用于启动和管理线程的定义高级 API 的*执行器（executors）*  
    - 用于管理和同步大型数据集合的*并发集合（concurrent collections）*  
    - 用于无同步原子操作的*原子变量（atomic variables）*  

### 锁对象  
- 锁对象的主要优势在于它们能够在试图获取锁定的对象时退出  
- 方法 `tryLock()` 可用于尝试锁定一个锁对象，如果无法锁定（已经有人获得了锁），则返回 false  
- 也可以使用定时版本 `tryLock(m)`，即等待给定的超时 m（毫秒）后才放弃  
- 以及其他高级功能（不在本课程范围内）  
#### 使用锁来避免死锁例  
```java
import java.util.concurrent.locks.ReentrantLock;

public class LockExample {
    public static void main(String[] args) {
        ReentrantLock hammerLock = new ReentrantLock();
        ReentrantLock nailLock = new ReentrantLock();

        // Worker 1
        Thread worker1 = new Thread() {
            public void run() {
                System.out.println("Worker 1 going to get hammer");
                if (!hammerLock.tryLock()) {
                    System.out.println("Hammer already taken!");
                    return;
                }
                System.out.println("Worker 1 got the hammer!");
                try { Thread.sleep(1000); } catch (Exception e) {}

                ... // 尝试以同种方式锁定 nails

                ...

                System.out.println("Worker 1 finished the work!");
                nailLock.unlock();
                System.out.println("Worker 1 returned the nails!");

                ...
            }
        };

        ... // 以类似方式实现线程 Worker2
    }
}
```
输出：  
```shell
$ java LockExample
Worker 1 going to get hammer...
Worker 2 going to get nails...
Worker 1 got the hammer!
Worker 1 going to get nails...
Worker 2 got the hammer!
Worker 2 going to get hammer...
Nails already taken!
Hammer already taken!
$
```
- 检测到已使用的项目，避免出现死锁！  

### Executer interfaces 执行器接口  
- java.util.concurrent 包中的执行器接口提供了启动和管理任务（如线程）的方法  
- 假设 `r` 是 **Runnable**，`e` 是 **Executor** 对象，那么就可以用 `e.execute(r);` 替换 `(new Thread(r)).start();`  
- 大多数执行器的实现都是为了处理由多个*工作线程（worker threads）*组成的*线程池（thread pools）*  
    - 在大规模应用中具有优势，例如需要以可扩展的方式协调大量线程的网络服务器  
#### 简单的执行器接口例  
```java
import java.util.concurrent.*;
import java.util.*;

class MyThread implements Runnable {
    int threadNum, start, end;
    MyThread(int num, int start, int end) {
        this.threadNum = num; this.start = start; this.end = end;
    }

    public void run() {
        try {
            for (int i = start; i <= end; i++) {
                System.out.printf("Thread #%d, step %d\n", threadNum, i);
                Random rand = new Random();
                Thread.sleep(rand.nextInt(1000));
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

public class ExecutorExample {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(10);
        Random rand = new Random();

        // 创建五个具有不同随机特征的线程，并通过执行器对象执行它们
        for (int i = 0; i < 5; i++) {
            int start = rand.nextInt(100);
            int end = start + rand.nextInt(3) + 1;

            MyThread thread = new MyThread(i + 1; start, end);
            executor.execute(thread);
        }

        executor.shutdown();
    }
}
```
输出：  
```shell
$ java ExecutorExample
Thread #1, step 46
Thread #5, step 19
Thread #4, step 49
Thread #3, step 49
Thread #2, step 24
Thread #3, step 50
Thread #2, step 25
Thread #1, step 47
Thread #2, step 26
Thread #3, step 51
Thread #3, step 52
Thread #4, step 50
Thread #5, step 20
Thread #4, step 51
$
```

### 结语 - 高级并发性  
- 并发是一个非常复杂的话题，尤其是涉及到多核平台的时候  
- 对于大多数程序员来说，低级应用程序接口已经足够，但对于处理大量数据和线程的高级应用程序来说，java.util.concurrent 的高级应用程序接口则是必不可少的  
- 更多信息：
    - https://docs.oracle.com/javase/tutorial/essential/concurrency/procthread.html  
    - 书籍：Brian Goetz et al.: *Java Concurrency in Practice* (Addison-Wesley)  