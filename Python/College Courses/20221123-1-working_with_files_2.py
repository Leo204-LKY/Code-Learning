# 不建议运行，因为会创建很多文件不便管理

# Working with files 2 文件处理 2

# Shutil Module
# Shutil 模块(shell utilities)为文件和目录的高级操作提供了方法
# 与 OS Module 一样需要导入
import os, shutil

# 举个例子，将 copyme.txt 从 dir1 复制到 dir2
# 注意：运行前要将终端目录定位到当前目录(College Courses)，否则会报错
print(os.getcwd())      # 输出当前目录

os.mkdir("dir1")        # 创建 dir1 文件夹
os.mkdir("dir2")        # 创建 dir2 文件夹

os.chdir("dir1")        # 将目录设置为 dir1 文件夹
with open("copyme.txt", "w") as f:
    f.write("Going to copy this file")

src = os.getcwd() + "/copyme.txt"
dest = "../dir2"
shutil.copy(src, dest)
# 如果使用 shutil.copy2() ，则会尝试保存文件的元数据，而 shutil.copy() 不会
os.chdir(dest)
print(os.listdir())

os.chdir("..")
# 使用循环可以创建多个文件夹
dirs = ["dir3", "dir4"]
for d in dirs:
    os.mkdir(d)

# 复制文件夹
# 使用 shutil 的 copytree 方法可以将文件夹及文件夹中的所有内容复制
shutil.copytree("dir1", "dir5")

# 重命名
# 使用 shutil.move 方法可以移动文件和文件夹
# 详细介绍：https://blog.csdn.net/seanblog/article/details/78885423
#          https://docs.python.org/zh-cn/3.10/library/shutil.html
# 如果目标文件不存在，原文件则会被重命名为目标文件参数
os.rename("dir3", "dir6")   # 重命名文件/目录
shutil.move("dir6","dir7")  # 移动文件/目录

# 删除文件夹
# os.remove() 只能删除空文件夹， shutil.rmtree() 则可以删除文件夹和文件夹中的所有文件
shutil.rmtree("dir3","aFolder")

# shutil 模块总结
# https://blog.csdn.net/jiandanjinxin/article/details/71489080
# shutil.copyfile(src, dst)   
# 从源src复制到dst中去。 如果当前的dst已存在的话就会被覆盖掉
# shutil.move(src, dst)
# 移动文件或重命名
# shutil.copymode(src, dst)
# 只是会复制其权限其他的东西是不会被复制的
# shutil.copystat(src, dst)
# 复制权限、最后访问时间、最后修改时间
# shutil.copy(src, dst)
# 复制一个文件到一个文件或一个目录
# shutil.copy2(src, dst)
# 在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西
# shutil.copy2(src, dst)
# 如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；如果是不在相同的文件系统的话就是做move操作
# shutil.copytree(olddir, newdir, True/Flase)
# 把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
# shutil.rmtree(src)
# 递归删除一个目录以及目录内的所有内容