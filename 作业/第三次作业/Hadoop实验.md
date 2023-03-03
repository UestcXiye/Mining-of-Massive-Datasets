#  一、实验内容

使用 Hadoop 实现WordCount 应用。

WordCount 是一个最简单的分布式应用实例，主要功能是统计输入目录中所有单词出现的总次数，如文本文件中有如下内容：

Hello world

则统计结果应为：

Hello 1

world 1

WordCount 可以使用多种方式实现，本次实验内容选择使用 Hadoop 实现 WordCount 程序，并完成对应实验报告。

# 二、平台及版本

- Windows10
- JDK1.8.0_192
- Hadoop2.7.3

# 三、实验原理

## 3.1 安装 Java1.8，并配置环境变量

路径：C:\Program Files\Java\jdk1.8.0_192

环境变量：HAVA_HOME，值：C:\Program Files\Java\jdk1.8.0_192

## 3.2 安装Hadoop2.7.3

1. 从[hadoop-2.7.3](https://archive.apache.org/dist/hadoop/common/hadoop-2.7.3/)下载hadoop-2.7.3.tar.gz，解压后放到C盘根目录下：

<img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917174240773.png" alt="image-20220917174240773" style="zoom:67%;" />

2. 原版的Hadoop不支持Windows系统，我们需要修改一些配置方便在Windows上运行，需要从网上搜索下载hadoop对应版本的windows运行包[hadooponwindows-master.zip]()。解压后，复制解压开的bin文件和etc文件到hadoop-2.7.3文件中，并替换原有的bin和etc文件。

3. 配置Java环境变量：

   <img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917174705076.png" alt="image-20220917174705076" style="zoom:67%;" />

   并在Path系统变量中加上：%JAVA_HOME%\bin;

4. 配置Hadoop环境变量：

   <img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917175055683.png" alt="image-20220917175055683" style="zoom:67%;" />

   并在Path系统变量中加上：%HADOOP_HOME%\bin;

5. 使用编辑器打开C:\hadoop-2.7.3\etc\hadoop\hadoop-env.cmd，找到set JAVA_HOME，将等号右边的值改成自己Java jdk的路径（如果路径中有Program Files，则将Program Files改为 PROGRA~1）。

   <img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917175341728.png" alt="image-20220917175341728" style="zoom:67%;" />

6. 配置好上面所有操作后，win+R 输入cmd 打开命令提示符，然后输入hadoop version，按回车，如果出现如图所示结果，则说明安装成功：

   <img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917175613133.png" alt="image-20220917175613133" style="zoom:67%;" />

## 3.3 Hadoop核心配置文件

在hadoop-2.7.3根目录下新建data文件夹和tmp文件夹，再在data文件夹里面新建datanote和namenote文件夹：

<img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917180543403.png" alt="image-20220917180543403" style="zoom:67%;" />



在hadoop-2.7.3\etc\hadoop中找到以下几个文件用文本编辑器打开。

1. 打开 hadoop-2.7.3/etc/hadoop/core-site.xml, 复制下面内容粘贴到最后并保存：

   ```
   <configuration>
       <property>
           <name>fs.defaultFS</name>
           <value>hdfs://localhost:9000</value>
       </property>
   </configuration>
   ```

2. 打开hadoop-2.7.3/etc/hadoop/mapred-site.xml, 复制下面内容粘贴到最后并保存：

   ```
   <configuration>
       <property>
          <name>mapreduce.framework.name</name>
          <value>yarn</value>
       </property>
   </configuration>
   ```

3. 打开hadoop-2.7.3/etc/hadoop/hdfs-site.xml, 复制下面内容粘贴到最后并保存：

   ```
   <configuration>
    <property>
           <name>dfs.replication</name>
           <value>1</value>
       </property>
       <property>
           <name>dfs.namenode.name.dir</name>
           <value>file:/C:/hadoop-2.7.3/data/namenode</value>
       </property>
       <property>
           <name>dfs.datanode.data.dir</name>
           <value>file:/C:/hadoop-2.7.3/data/datanode</value>
       </property>
   </configuration>
   ```

4. 打开hadoop-2.7.3/etc/hadoop/yarn-site.xml,复制下面内容粘贴到最后并保存：

   ```
   <configuration>
       <property>
          <name>yarn.nodemanager.aux-services</name>
          <value>mapreduce_shuffle</value>
       </property>
       <property>
          <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
          <value>org.apache.hadoop.mapred.ShuffleHandler</value>
       </property>
   </configuration>
   ```

从C:\hadoop-2.7.3\bin下拷贝hadoop.dll到 C:\Windows\System32 ，不然在window平台使用MapReduce测试时报错：

<img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917182549453.png" alt="image-20220917182549453" style="zoom:67%;" />

## 3.4 启动Hadoop服务

到C:\hadoop-2.7.3\bin下，按下Win+R进入命令行窗口，输入hdfs namenode -format，执行结果如下图所示：

<img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917185224734.png" alt="image-20220917185224734" style="zoom:67%;" />

格式化之后，namenode文件夹里会自动生成一个current文件，说明格式化成功：

<img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917185353101.png" alt="image-20220917185353101" style="zoom:67%;" />

到C:\hadoop-2.7.3\sbin下，按下Win+R进入命令行窗口，输入start-all，启动Hadoop集群：

<img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917185719804.png" alt="image-20220917185719804" style="zoom:67%;" />

出现下面四个窗口表示启动Hadoop集群成功：

<img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917185810475.png" alt="image-20220917185810475" style="zoom:67%;" />

在同命令行窗口下输入start-all（或运行start-all.cmd），启动Hadoop服务，等待他启动完成。

完成之后，输入jps，可以查看运行的所有服务：

<img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917185912053.png" alt="image-20220917185912053" style="zoom:67%;" />

访问http://localhost:50070，这是Hadoop的管理页面：

![image-20220917191603772](C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917191603772.png)

访问http://localhost:8088，这是yarn的Web界面：

![image-20220917192604677](C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917192604677.png)

在同命令行窗口下输入stop-all（或运行stop-all.cmd），关闭Hadoop服务。

# 四、WordCount实现

到C:\hadoop-2.7.3\sbin下，按下Win+R进入命令行窗口，输入start-all（或运行start-all.cmd），启动Hadoop服务。

1. 按Win+R输入cmd打开命令行窗口，键入==hadoop fs -mkdir /wordcount/==命令，在hdfs中创建一个wordcount文件夹。

   <img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917212121969.png" alt="image-20220917212121969" style="zoom:67%;" />

   可以在http://localhost:8088/中查看。

2. 键入==hadoop fs -mkdir /wordcount/input==命令，在wordcount文件夹下创建input文件夹。

3. 再次键入==hdfs dfs -ls /wordcount/==命令，显示wordcount文件夹里的内容：

<img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917202201991.png" alt="image-20220917202201991" style="zoom:67%;" />

4. 键入==hadoop fs -put C:/Users/81228/Desktop/input.txt /wordcount/input==命令，将桌面的input.txt放入hdfs中的input内。

5. 键入==hdfs dfs -ls /wordcount/input==命令，显示wordcount/input文件夹里的内容，可以看到input.txt已经在input中：

   <img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917202726991.png" alt="image-20220917202726991" style="zoom:67%;" />

6. 键入==hadoop dfs -cat /wordcount/input/input.txt==命令，查看上传文件中的内容：

   <img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917203341380.png" alt="image-20220917203341380" style="zoom:67%;" />

   > 这是taylor swift的歌——《Love Story》的歌词 :)

7. 键入==hadoop jar C:/hadoop-2.7.3/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar wordcount /wordcount/input/input.txt /wordcount/output==命令，运行C:/hadoop-2.7.3/share/hadoop/mapreduce文件夹中hadoop-mapreduce-examples-2.7.3.jar这个Java程序，调用wordcount方法，输入为/wordcount/input/input.txt，输出结果存储在/wordcount/output里。以下是运行细节：

   <img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917204029967.png" alt="image-20220917204029967" style="zoom:67%;" />

   报错信息：Diagnostics: Failed to setup local dir /tmp/hadoop-81228/nm-local-dir, which was marked as good.

   解决方法：使用管理员身份命令行启动Hadoop集群，然后使用普通用户身份命令行提交作业。

8. 以管理员身份打开命令行窗口，cd定位到C:\hadoop-2.7.3\sbin下，再次启动Hadoop集群：

   <img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917205828417.png" alt="image-20220917205828417" style="zoom:67%;" />

9. 再次运行7中的命令，可以看到，成功运行：

   <img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917210124957.png" alt="image-20220917210124957" style="zoom:67%;" />

10. 键入==hdfs dfs -ls /wordcount/==命令，显示wordcount文件夹里的内容，可以看到output文件夹：

    <img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917210221425.png" alt="image-20220917210221425" style="zoom:67%;" />

11. 键入==hadoop dfs -cat /wordcount/output==命令，output文件夹下有两个文件：

    <img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917210338210.png" alt="image-20220917210338210" style="zoom:67%;" />

    在工作的顺利完成，MapReduce的运行时创建的输出目录中的文件_SUCCESS。

12. 键入==hadoop dfs -cat /wordcount/output/part-r-00000==命令，查看part-r-00000文件，里面就是我们要的结果：

    <img src="C:\Users\81228\AppData\Roaming\Typora\typora-user-images\image-20220917210906664.png" alt="image-20220917210906664" style="zoom:67%;" />
    
    完整的MapReduce结果如下所示：

```
'Cause  1
And     8
Baby    4
Begging 1
But     1
Cause   1
Don't   1
Escape  1
Go      1
He      1
I       18
I'll    4
I'm     1
I've    1
Is      1
It's    4
Juliet  3
Little  1
Marry   1
My      1
Oh      4
On      1
Romeo   6
See     1
So      2
That    1
They're 1
This    1
We      2
When    1
Wondering       1
You'll  2
a       9
afraid  1
air     1
all     3
alone   4
and     5
around  1
away    2
balcony 1
ball    1
be      10
been    1
begging 1
both    2
but     2
can     2
cause   1
close   2
come    1
coming  1
crowd   1
crying  1
dad     1
daddy   2
dead    1
did     1
difficult       1
do      2
don't   3
dress   1
ever    1
everything      1
eyes    2
fading  1
faith   1
feel    1
feeling 1
first   2
flashback       1
for     2
from    2
garden  1
go      2
got     1
gowns   1
ground  1
have    1
head    1
hello   1
how     1
if      2
in      3
is      3
it      1
it's    1
just    4
keep    2
knelt   1
knew    1
know    3
left    2
letter  1
lights  1
little  1
love    6
make    2
me      7
mess    1
met     1
my      4
never   2
of      3
oh      7
on      2
out     4
outskirts       1
party   1
pebbles 1
pick    1
please  2
prince  2
princess        2
pulled  1
quiet   1
real    1
really  1
ring    1
run     2
said    6
save    2
saw     2
say     5
scarlet 1
see     3
sneak   1
so      1
somewhere       2
staircase       1
standing        1
starts  1
stay    2
story   4
summer  1
take    2
talked  1
tell    1
that's  1
the     13
there   1
there's 2
they    1
think   1
this    3
through 1
throwing        1
tired   1
to      11
town    2
trying  1
waiting 4
was     4
way     1
we      3
we'll   1
we're   1
were    7
what    1
when    2
while   1
white   1
yes     4
you     16
you'll  1
young   2
your    3
```

