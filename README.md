What is npp_auto_complete_extension？
===========================

专为windows用户写的一个notepad++自动补全工具，初衷源于matlab2012自带的编辑器的TAB自动补全太慢了。
twins参加美赛，所以尝试下写一个适合notepad++的matlab自动补全，测试结果还不错，与君共享。

What I want to do next?
===========================

我初步的想法就是做一个模拟linux下vim的工具，vim下的ctags插件只针对c语言有效，而且每次都必须合理的
配置tags的目录，twins想在windows下做一个自动化的生成工具，基于这样的而一个规律：正常coder使用到的
补全是自带的库函数和他自己写的函数，通过定位他自己的项目，就能完成一个可定制的自动补全，而这些都可
以用自动补全实现。twins曾今改造过checkstyle，使用过antlr，里面的tokens分析很受启发,twins想通过拓展
一个python词法库，来实现这个功能。

How to use it?
==========================
把matlab.xml文件放在$notepad_home/plugin/API文件夹下，开启notepat++函数自动补全即可看到效果；

如果你想制作自己的自动补全，(大部分语言都是支持的),那么模仿funciton_list_example.list里面的内

容进行，注意'\t'.

Can you join me?
===========================

只要你对词法分析和编程感兴趣，我们就能实现这个目标。