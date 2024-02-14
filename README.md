# UPC_JWXT
中国石油大学（华东），UPC，查询老师已经上传、但是还没出的成绩，理论上所有使用强智教务系统的学校都通用、中国石油大学查成绩  
PS:2024-2-24更新一更简单方法，但是仅能查到一部分成绩，没有在评教系统的成绩不能查到  
新方法：进入评教系统，点开你想查询的课程老师的评教页面，会弹出一个链接，复制链接中如下图所示部分：  
![image](https://github.com/Mao0324/UPC_JWXT/assets/133934785/992a9c83-f1f7-4d34-896b-c7e48c229ac9)  
然后进入查询成绩页面随意点击一个已经出的成绩，会弹出页面，替换如下图所示部分  
![image](https://github.com/Mao0324/UPC_JWXT/assets/133934785/d4f480f4-79eb-4368-9128-ec792bfd947a)  
进入链接即可查询到详细成绩信息  
下面方法为原来方法，比较慢，但是能查到本学期所有课程成绩  
使用步骤：  
![image](https://github.com/Mao0324/UPC_JWXT/assets/133934785/ffeaabc6-10e2-449d-af55-3e12ca0009a1)  
使用任意浏览器登录数字石大并进入到教务系统如图所示页面  
点击F12，刷新一下  
![image](https://github.com/Mao0324/UPC_JWXT/assets/133934785/92fabf74-4730-46ce-aa55-3b19019cc04f)  
点击如图所示文件  
![image](https://github.com/Mao0324/UPC_JWXT/assets/133934785/9bf177c7-f8cc-4260-bac0-0bedfa613e0a)  
复制如图所示cookie  
打开代码按照提示修改  
![image](https://github.com/Mao0324/UPC_JWXT/assets/133934785/1ee7b458-5a25-4b8c-90f8-6560c81948e3)  
按照注释修改  
![image](https://github.com/Mao0324/UPC_JWXT/assets/133934785/6051927a-951f-48f5-a596-ff137c746a9d)  
如果速度太慢可以分成十段0001-0999、1001-1999……  
![image](https://github.com/Mao0324/UPC_JWXT/assets/133934785/6553bc15-450a-4f80-b710-5e96321b2463)  
此处填上你的cookie  
![image](https://github.com/Mao0324/UPC_JWXT/assets/133934785/78d6f292-8cdf-4292-9cea-485feca52482)  
![image](https://github.com/Mao0324/UPC_JWXT/assets/133934785/55298974-01e9-45d7-b7fc-604fb403ed0d)  
运行程序，会在程序所在文件夹中生成出一个excel文件，里面是出成绩的链接  
![image](https://github.com/Mao0324/UPC_JWXT/assets/133934785/9b85ed35-8726-4f18-b6f7-0e1a821b98a8)  
复制这些链接到浏览器就可以查到成绩具体信息  
有问题添加QQ：1793252356  
关键词：中国石油大学（华东）、UPC、强智教务、中国石油大学

原理：  
![image](https://github.com/Mao0324/UPC_JWXT/assets/133934785/314841f8-a6fe-4950-9d11-575fdaf26236)  
教务系统给出了接口，点击如上成绩可以查询成绩具体构成  
![image](https://github.com/Mao0324/UPC_JWXT/assets/133934785/fc31ca7c-d519-4aef-8bbd-10cd1a62a831)  
通过比对不同课程成绩链接发现链接主要有用的部分由如上部分组成：学号、课程号（指的是该学年该课程某种唯一标识符）、总成绩（没用）  
于是想到遍历课程号，找到已经上传但是并未发布的成绩  
尝试修改学号，发现也可以查到同学的成绩  
声明：仅供学习交流，不得用于其他用途
