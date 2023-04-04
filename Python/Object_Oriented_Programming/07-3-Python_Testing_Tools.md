# Lecture 7.3: Python Testing Tools | Python 测试工具  

## Python `unittest`  
- 为单元测试提供公共接口  
    - 每个单元测试测试可用代码总量中的一个单元  
- `TestCase` 类  
    - 用于比较值、设置测试以及完成后进行清理  
    - 要为特定的任务编写一组单元测试，可以创建 `TestCase` 的子类，并编写单独的方法来执行实际的测试  
        ```Python
        import unittest

        def foo(x):
            return x + 1
        # Code to be tested.

        class MyTest(unittest.TestCase):
            def test(self):
                self.assertEqual(foo(3), 4)

        if __name__ == "__main__":
            unittest.main()
        ```
        ```
        $ python main.py
        .
        --------------------------------------
        Ran 1 test in 0.000s OK
        ```
- 在一个 `TestCase` 类上可以有任意多的测试方法  
    - 每个方法名必须以test开头  
    - `assert` 内置的范围  
- 测试运行程序将每个测试作为单独的测试执行  
    - 每个测试都应该完全独立于其他测试  
    - `setUp()`, `tearDown()` 方法  

## Python `doctest`  
- 轻量级测试框架  
- 在 Python 文档字符串注释中嵌入简单测试(使用 `>>>`)  
    - Example 1  
        ```Python
        def square(x):
            """Return the square of x.
            >>> square(2)
            4
            >>> square(-2)
            4
            """
            return x * x

            if __name__ == '__main__’:
                import doctest
                doctest.testmod()
        ```
        ```
        测试通过，因此不会有任何 doctest 输出。
        ```
    - Example 2  
        ```Python
        def square(x):
            """Return the square of x.
            
            >>> square(2)
            4
            >>> square(-2)
            4
            """
            return x + x
            # 这里的 x * x 是一个 fault

        if __name__ == '__main__’:
            import doctest
            doctest.testmod()
        ```
        ```
        $ python main.py
        ********************************************
        File "main.py", line 6, in __main__.square
        Failed example:
        square(-2)
        Expected:
        4
        Got:
        -4
        ********************************************
        1 items had failures:
        1 of 2 in __main__.square
        ***Test Failed*** 1 failures.
        ```

## `pytest`
- `unittest` 的替代方法
- 下载：[https://pytest.org/](https://pytest.org/)
- 测试用例需要更少的编码工作
- 测试用例命名:
    - 函数以 `test` 开头
    - 类名以 `Test` 开头
    - 类中的方法以 `test_` 开头
    ```Python
    # content of test_sample.py
    def func(x):
        return x + 1
    def test_answer():
        assert func(3) == 5
    ```
    ```
    $ py.test
    ============================= test session starts ==============================
    platform darwin -- Python 3.6.4, pytest-3.3.2, py-1.5.2, pluggy-0.6.0
    rootdir: /Users/pedwards/Desktop, inifile:
    collected 1 item
    test_sample.py F [100%]
    =================================== FAILURES ===================================
    _________________________________ test_answer __________________________________
    def test_answer():
    >    assert func(3) == 5
    E    assert 4 == 5
    E     + where 4 = func(3)
    test_sample.py:6: AssertionError
    =========================== 1 failed in 0.06 seconds ===========================
    ```