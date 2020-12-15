# Auto_test
```
1.关键字设计模式
2.PO设计模式
3.配置文件读取 config.ini ,email.ini
4.excel文件操作
5.sendemail
6.CI集成,自动执行
```

六 命名规范
总体原则，新编代码必须按下面命名风格进行，现有库的编码尽量保持风格。

```
1 尽量单独使用小写字母‘l’，大写字母‘O’等容易混淆的字母。
2 模块命名尽量短小，使用全部小写的方式，可以使用下划线。
3 包命名尽量短小，使用全部小写的方式，不可以使用下划线。
4 类的命名使用CapWords的方式，模块内部使用的类采用_CapWords的方式。
5 异常命名使用CapWords+Error后缀的方式。
6 全局变量尽量只在模块内有效，类似C语言中的static。实现方法有两种，一是__all__机制;二是前缀一个下划线。
7 函数命名使用全部小写的方式，可以使用下划线。
8 常量命名使用全部大写的方式，可以使用下划线。
9 类的属性（方法和变量）命名使用全部小写的方式，可以使用下划线。
9 类的属性有3种作用域public、non-public和subclass API，可以理解成C++中的public、private、protected，non-public属性前，前缀一条下划线。
11 类的属性若与关键字名字冲突，后缀一下划线，尽量不要使用缩略等其他方式。
12 为避免与子类属性命名冲突，在类的一些属性前，前缀两条下划线。比如：类Foo中声明__a,访问时，只能通过Foo._Foo__a，避免歧义。如果子类也叫Foo，那就无能为力了。
13 类的方法第一个参数必须是self，而静态方法第一个参数必须是cls。
```

七 编码建议

```
1 编码中考虑到其他python实现的效率等问题，比如运算符‘+’在CPython（Python）中效率很高，都是Jython中却非常低，所以应该采用.join()的方式。
2 尽可能使用‘is’‘is not’取代‘==’，比如if x is not None 要优于if x。
3 使用基于类的异常，每个模块或包都有自己的异常类，此异常类继承自Exception。
4 异常中不要使用裸露的except，except后跟具体的exceptions。
5 异常中try的代码尽可能少。
```


接口自动化测试框架 :

获取接口信息的方式 :
1. 接口文档
2. 抓包的方式 ,fiddler等
3. 浏览器开发者工具

# git项目

## 目录

### python+requests+ddt+unittest+CI

### selenium+python+unittest+ddt+CI

#### 设计模式 :

关键字驱动设计模式

POM设计模式

#### 执行方式 :

CI 集成 :

e: cd .\auto_test_py\webui\ python .\api_keyword_all.py

以上执行 ,可以把selenium ,requests ,一起执行完成 .