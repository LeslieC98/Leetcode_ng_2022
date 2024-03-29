### python 八股

### 1.1 **is 与 == 区别 ：**

#### is 用于判断两个变量引用对象是否为同一个， **==** 用于判断引用变量的值是否相等。

![image-20221114151940475](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20221114151940475.png)



### 2. Python的基本数据类型

Python3 中有六个标准的数据类型：

- Number（数字）(包括整型、浮点型、复数、布尔型等)
- String（字符串）
- List（列表）
- Tuple（元组）
- Set（集合）
- Dictionary（字典）

Python3 的六个标准数据类型中：

- 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
- 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。



### 3. Python 是强语言类型还是弱语言类型？

Python 是强类型的动态脚本语言。

> 强类型：不允许不同类型相加。
> 动态：不使用显示数据类型声明，且确定一个变量的类型是在第一次给它赋值的时候。
> 脚本语言：一般也是解释型语言，运行代码只需要一个解释器，不需要编译。
>
> Python 是一种解释型语言，Python 在代码运行之前不需要编译解释执行。
>
> Python 是动态类型语言，在声明变量时，不需要说明变量的类型。

### 4. 谈一下什么是解释性语言，什么是编译性语言？

解释性语言在运行程序的时候才会进行翻译。

编译型语言写的程序在执行之前，需要一个专门的编译过程，把程序编译成机器语言（可执行文件）。



### 5. 函数传递中*args，**kwargs

用来处理可变参数，接收参数后，args会变成一个tuple，kwargs会变成一个dict

*args就是就是传递一个可变参数列表给函数实参，而**kwargs则是将一个可变的关键字参数的字典传给函数实参



### 6. **问：说说Python中迭代器和生成器的区别？**

**答：**Python中生成器能做到迭代器能做的所有事，而且因为自动创建了__iter__()和next()方法，生成器显得特别简洁，而且生成器也是高效的，使用生成器表达式取代列表解析，同时节省内存。除了创建和保持程序状态的自动生成，当发生器终结时，还会自动跑出StopIterration异常

**下面分别来说说这两者的具体区别:**

**1、迭代器**迭代器（`iterator`）是访问集合内元素的一种方式，提供了一种遍历类序列对象的方法。

迭代器对象要求支持迭代器协议的对象。在Python中，支持迭代器协议就是实现对象的__iter__()和next()方法。其中__iter__()方法返回迭代器对象本身；next()方法返回[容器](https://cloud.tencent.com/product/tke?from=10680)的下一个元素，在结尾时引发StopIteration异常。

下面用个简单的列表来说迭代器的用法：

**2、生成器**

生成器(generator)就是一个函数，它提供了一种实现迭代器协议的便捷方式。生成器与普通函数的区别在于它包含 yield 表达式，并且不需要定义 __iter__()和__next__()。

生成器是一种惰性的序列，如果我们需要创建一个 0～1000000000 的序列，这样大的序列创建出来会占用比较多的内存，生成器就是为了解决这样的问题 。



相比于迭代器，生成器具有以下优点：

1. 减少内存
2. 延迟计算
3. 有效提高代码可读性

## 面向对象篇

### 什么是组合和继承？

- 组合是使用其他的类实例作为自己的一个属性（Has-a关系）
- 继承是子类继承父类的属性和方法（Is a关系）
- 优先使用组合保持代码简单

### 类变量和实例变量的区别？

- 类变量由所有实例共享
- 实例变量由实例单独享有，不同实例之间不影响
- 当我们需要在一个类的不同实例之间共享变量的时候使用类变量

### 7. 浅拷贝深拷贝

浅拷贝是在另一块地址中创建一个新的变量或容器，但是容器内的元素的地址均是源对象的元素的地址的拷贝。也就是说新的容器中指向了旧的元素（ 新瓶装旧酒 ）

> 深拷贝是在另一块地址中创建一个新的变量或容器，同时容器内的元素的地址也是新开辟的，仅仅是值相同而已，是完全的副本。也就是说（ 新瓶装新酒 ）。
>
> 

乐观锁和悲观锁是两种思想，用于解决并发场景下的数据竞争问题。

- 乐观锁：乐观锁在操作数据时非常乐观，认为别人不会同时修改数据。因此乐观锁不会上锁，只是在执行更新的时候判断一下在此期间别人是否修改了数据：如果别人修改了数据则放弃操作，否则执行操作。
- 悲观锁：悲观锁在操作数据时比较悲观，认为别人会同时修改数据。因此操作数据时直接把数据锁住，直到操作完成后才会释放锁；上锁期间其他人不能修改数据。

悲观锁的实现方式是加锁，加锁既可以是对代码块加锁（如Java的synchronized关键字），也可以是对数据加锁（如MySQL中的排它锁）。

乐观锁的实现方式主要有两种：CAS机制