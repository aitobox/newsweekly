# AIToBox周刊：第 19 期

这里记录每周值得分享的AI科技内容，周末发布。

本杂志开源（GitHub: [aitobox/newsweekly](https://github.com/aitobox/newsweekly)），欢迎提交 issue，投稿或推荐你的项目。


## AI资讯

#### 1. DeepSeek发布DeepSeek-V3-0324，登上Huggingface趋势榜，编程能力大幅提升

3月24日晚，DeepSeek发布了模型更新——DeepSeek-V3-0324，本次为DeepSeek V3模型的小版本更新，其参数量为 671 亿。

**详细内容** 

目前，DeepSeek-V3-0324已在Hugging Face上开源，并迅速登上了Trending榜（现列第4）：

Aider已经更新了榜单：[Aider LLM Leaderboards](https://aider.chat/docs/leaderboards/)

DeepSeek-V3-0324在榜单上排第7位，价格远远低于所有其他上榜大模型，是claude 3.7的三十分之一，o1的百分之一，甚至是自家DeepSeek-R1的五分之一！！！

此次更新的核心亮点在于性能的显著提升。尽管公司将其定位为"小版本更新"，但初步测试显示模型在数学能力和前端设计方面均有明显进步。多位技术评测者报告称，模型的编程能力大幅提升，接近Claude 3. 5 的水平。一些评测者分享了V3- 0324 生成的样例图像，称初步效果"相当不错"。


**资讯地址**

https://huggingface.co/deepseek-ai/DeepSeek-V3-0324

![Image](https://github.com/user-attachments/assets/9ab4ebfb-5f3d-4be5-84d6-f27afe2ea746)


#### 2. 阿里巴巴团队推出一个开源的3D AI 动作控制模型 LHM

只需要您提供一张图片和一个动作视频，就可以将图片中的人物替换到动作视频中去；

**详细内容** 

LHM是一个大型可动画人类重建模型,可以从单个图像中快速生成3D人体模型。该项目提供了官方的PyTorch实现,包括推理代码、预训练模型和实时渲染管线。

主要功能点

* 提供LHM-0.5B、LHM-1B等不同规模的预训练模型
* 支持从单个图像快速生成可动画的3D人体模型
* 提供实时渲染管线和Gradio在线演示
* 包含视频运动处理脚本,可以将视频转换为驱动3D人体模型的运动序列
* 提供计算人脸相似度、PSNR、SSIM和LPIPS等指标的脚本

**资讯地址**

https://github.com/aigc3d/LHM?tab=readme-ov-file

**体验地址**

https://github.com/user-attachments/assets/7dd05cd0-7980-4ab5-9f77-8e97f03e5d34



## AI服务

#### 1. Google Gemini 2.0 Flash 新增「原生图像生成」功能

Google Gemini 服务新增了图像编辑的功能，您可以直接用语言描述需求，实现图片编辑

**功能特点** 


上述功能目前仅在 Google AI Studio 中提供，开发者可以通过 Gemini API 进行体验测试；

您可以访问[aistudio](https://aistudio.google.com/)，选择`gemini-2.0-flash-exp-image-generation`模型，同时将`output format`设置为`images and text`来体验这个功能；

Gemini 2.0 Flash 支持文字理解并生成图像，并能够理解上下文保持角色和图像场景的一致性；同时 Gemini 2.0 Flash 还支持自然语言对话的理解，以及利用现实世界的内容和增强版推理来生成图像，Google 官方指出，这对绘制食谱等精准类的内容将会有很大帮助。

**服务地址**

https://aistudio.google.com/

下面提供10 个典型的使用案例：

1. 修改人物动作

![Image](https://github.com/user-attachments/assets/6cf1b556-af23-47ba-890f-4cdeaeb0cecc)

2. 为证件照添加背景

![Image](https://github.com/user-attachments/assets/71c657ed-9588-4de1-aab1-1b62fda24ee7)

3. 添加logo元素

![Image](https://github.com/user-attachments/assets/88682441-a241-4596-a126-52fd86ad6003)

4. 植入式广告

![Image](https://github.com/user-attachments/assets/92c87fb9-5af6-453f-b4a3-d6e31aa8188a)

5. 黑白图片彩色化

![Image](https://github.com/user-attachments/assets/26c2927e-3e10-472f-b754-62bbfab5b40b)

6. 设计家居装饰

![Image](https://github.com/user-attachments/assets/e3f7b9a2-caae-4923-8096-3abba5c32ac3)

7. 人像照变换角度

![Image](https://github.com/user-attachments/assets/a68aed9a-9bfb-405b-87da-92a3e3ec4ea6)

8. 去除水印

![Image](https://github.com/user-attachments/assets/a4e14545-7780-484e-a050-39f3a4930a80)

9. 为故事生成插图

![Image](https://github.com/user-attachments/assets/23e8f9fe-5994-495f-9db5-37b2b56907cd)

10. 虚拟换衣

![Image](https://github.com/user-attachments/assets/a4ffd701-fb7c-4bb2-9ff2-a4246f8abbaf)


## AI文章

#### 1. 不到 4 万元的 DeepSeek-R1-671B-Q8 部署方案

腾讯玄武实验室探索了以廉价硬件运行Deepseek的方案，使用Q8量化模型，最高22K上下文；

**详细内容** 

在 DeepSeek-R1 发布后，Rasim Nadzhafov 等人发现可以用基于 CPU 的硬件方案进行部署。腾讯玄武实验室在网上诸多相关实践的基础上进行了深入研究，从硬件、系统、推理框架等各个层面进行优化，在使用更低成本、更低功耗硬件的同时实现了长文本生成速度提升约 25%、峰值输出速度提升约 15%、预填充速度提升约 20%。使用玄武实验室的软硬件优化方案，只需不到 4 万元人民币的硬件就可部署 DeepSeek-R1-671B-Q8，峰值生成速度 7.17 tokens/s，即每秒输出约 10 个汉字，且整机功耗和噪音和家用台式机类似。

**文章地址**

https://mp.weixin.qq.com/s/vIrvbVJ6Nv00Ehre1zZwMw?v_p=90

![Image](https://github.com/user-attachments/assets/ec39386c-cb8e-4796-90d6-c17137df5312)




## 往期推荐

* [AI资讯快报](https://github.com/aitobox/newsweekly/issues?q=is%3Aissue+is%3Aclosed+label%3AAI%E8%B5%84%E8%AE%AF%E5%BF%AB%E6%8A%A5)
* [AI服务推荐](https://github.com/aitobox/newsweekly/issues?q=is%3Aissue+is%3Aclosed+label%3AAI%E6%9C%8D%E5%8A%A1%E6%8E%A8%E8%8D%90)
* [AI文章推荐](https://github.com/aitobox/newsweekly/issues?q=is%3Aissue+is%3Aclosed+label%3AAI%E6%96%87%E7%AB%A0%E6%8E%A8%E8%8D%90)

(完)
