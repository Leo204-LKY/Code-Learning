# Lecture 3.2: Polymorphism 多态性
# 源自希腊语，意思是 many (poly) shapes (morph) 许多(多边形)形状(变形)
# Python中的多态性：不同的行为取决于正在使用的子类，而不必显式地知道子类实际上是什么

# 多态性的例子：方法重载(Method overload) - 类中有两个或多个方法，它们的名称相同，但是参数列表不同，行为也不同；子类型(Subtyping) - 允许一个方法被写入一个特定类 B 的对象，但如果传入一个属于类 S 的对象，该对象是 B 的子类，也可以正确工作

# 当我们想要编写可以处理一系列不同对象的代码时很有用——只要它们提供相同的接口
# 例： Media Player 媒体播放器
'''
- 对于不同类型的文件，解压和提取音频文件的过程是非常不同的。.wav文件是未压缩的，而.mp3、.wma都有完全不同的压缩算法。
- 我们可以使用继承和多态性来简化设计。每种类型的文件都可以由AudioFile的不同子类表示，例如:Wav 文件, MP3 文件。
- 每个文件都有一个play()方法，但该方法对每个文件的实现方式不同，以确保遵循正确的提取过程。
- 媒体播放器对象永远不需要知道它引用的是AudioFile的哪个子类;它只调用play()并多态地让对象处理播放的实际细节。'''
class AudioFile:
    def __init__(self, filename): 
        if not filename.endswith(self.ext):
            raise Exception('Invalid file format')
        self.filename = filename 
    
class MP3File(AudioFile):
    ext = 'mp3'
    def play(self):
        print('playing as mp3')
    
class WavFile(AudioFile):
    ext = 'wav' 
    def play(self):
        print('playing as wav')

# mp3 = MP3File(‘myfile.mp3’)
# mp3.play()
# >>> playing as mp3
#
# wav = WavFile(‘anofile.wav’)
# wav.play()
# >>> playing as wav
#
# nofile = MP3File(‘thisfile.abc’)
# >>> Exception: Invalid file format

# 动态类型(Dynamic Typing)
# - Python支持动态类型——允许我们声明变量而不需要指定它们的类型(int, string, float…)
# - 在后面的代码中，我们可以将其他数据类型分配给同一个变量：
# my_var = 100 subclass.
# type(my_var)
# >>> <class 'int’>
#
# my_var = 'Dynamic typing here'
# type(my_var)
# >>> <class 'str’>
#
# my_var = [1, 2, 3]
# type(my_var)
# >>> <class 'list'>
#
#
# 鸭子类型(Duck Typing)
# - 由 Python 实现的多态形式
# - 鸭子类型允许我们使用任何提供所需行为的对象，而不必强制它是子类。 
'''“Duck Typing”一词来自诗人詹姆斯·惠特科姆·莱利(James Whitcomb Riley)的一句格言，他说：“当我看到一只鸟像鸭子一样走路，像鸭子一样游泳，像鸭子一样呱呱叫，我就把这只鸟叫做鸭子。”'''
class Foo:
    def __init__(self, some_string): 
        if not some_string.startswith('foo.'):
            raise Exception('Invalid foo thing')
        self.some_string = some_string
    
    def play(self):
        print('doing something as foo')
# mp3 = MP3File(‘myfile.mp3’)
# mp3.play()
# >>> playing as mp3

# foobar = Foo(‘foo.thing’)
# foobar.play()
# >>> doing something as foo

# 其他有用的内置组件
# isinstance(<object>, <classinfo>) - 如果 object 参数是 classinfo 参数或其子类的实例，则返回 True
# issubclass(<class>, <classinfo>) - 如果 class 是 classinfo 的子类，则返回 True