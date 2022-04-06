# 基于tomotopy的中文文本主题自动提取软件：使用指南
                                                          
该软件旨在自动分析大批量文档中的主题，并计算每个文档中不同主题的概率分布，即主题值。该软件是基于Python(3.7)语言开发的，适用于Windows操作系统。软件中文本主题的分析主要依赖于LDA主题模型（Latent Dirichlet Allocation Model），该模型的原理可参见Blei et al. (2003)的论文。

1.软件安装

该软件的可执行程序（exe）可通过Microsofthttps的OneDrive储存器下载:https://1drv.ms/u/s!AmzgU0mRIM3naRKYGL8jsd6HIF4?e=Zf32aW 。下载后无需安装，只需配置好文本数据即可实现LDA主题分析。储存器中包含两个文件，其中input.csv为文本储存的示例数据，exe可执行程序为软件主体，如图1所示。
![image](https://user-images.githubusercontent.com/84764583/161943603-44dae4ca-f203-42a1-b49b-f43575e4075b.png)

图1 软件安装

2.数据预处理

在使用该软件分析文本主题前，需要对数据进行一些预处理。因为该软件对文本数据的存储形式、编码格式及文件命名做出了限制。

2.1 文本数据存储

用于提取主题及分析主题值的文本需要储存在csv表格中。其中，每个文档占用一个单元格，所有文档需放置在同一列下，该列标题需要设置为“text”，如图2所示。同时，为确保分析不会出错，建议在使用前将每个单元格的文本中的换行符删除。删除换行符的便捷方式见该链接：https://jingyan.baidu.com/article/5d6edee2577a5dd9eadeecb6.html 。
![image](https://user-images.githubusercontent.com/84764583/161950126-d6a08cda-5b2e-412d-b7a0-f3d58479a688.png)

图2 文本数据存储示例





参考文献
Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet Allocation. Journal of Machine Learning Research, 3, 993–1022. 
