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

2.2 编码格式及文件命名

将文本保存在csv表格中后，需要将文件保存为utf-8编码格式。因为软件仅能读取该格式的表格。该步骤可以通过表格的“文件-另存为-CSV UTF-8（逗号隔开）”来实现，如图3所示。该步骤仅适用于office办公软件，不适用于WPS。因为WPS的另存为界面无“-CSV UTF-8（逗号隔开）”选项。最后，将该文件命名为input.csv，并将其放置在“基于tomotopy的中文文本主题自动提取软件.exe”可执行程序的相同目录下。

![image](https://user-images.githubusercontent.com/84764583/161983082-e210e5fe-904b-4c0c-9dd6-acc1ad9da9f4.png)

图3 编码格式及文件命名

3.数据分析

3.1 软件运行

文本数据处理完之后，可以通过双击“基于tomotopy的中文文本主题自动提取软件.exe”来运行软件执行文本分析。双击exe程序后会出现一个黑色界面，这代表软件已经开始运行。运行一段时间后，黑色界面会打印前5条文档文本清理后的结果，并打印最佳主题数，如图4所示。软件将会按照最佳主题数来提取文本中的主题。

![image](https://user-images.githubusercontent.com/84764583/161985130-ac69405a-2141-4bc0-b243-cdef912afa1c.png)

图4 软件运行界面

3.2 导出结果

软件运行完之后，黑色界面将会自动关闭。并且input文件相同目录下会出现三个文件：清理后的详细文本.txt、主题词.txt、主题值.csv，如图5所示。其中，清理后的详细文本.txt包含了去除标点符号、数字后的纯汉字文本，主题词.txt记录了每个主题的特征词，主题值.csv记录了所有文档不同主题的主题值，即主题的概率分布。

![image](https://user-images.githubusercontent.com/84764583/161986493-271836c8-db49-4c20-83fe-f40e5a8ab0d5.png)

图5 软件导出结果


参考文献
Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet Allocation. Journal of Machine Learning Research, 3, 993–1022. 
