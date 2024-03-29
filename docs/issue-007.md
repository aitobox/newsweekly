# AIToBox周刊：第 7 期

这里记录每周值得分享的AI科技内容，周末发布。

本杂志开源（GitHub: [aitobox/newsweekly](https://github.com/aitobox/newsweekly)），欢迎提交 issue，投稿或推荐你的项目。


## AI资讯

#### 1. 如何寻找真实的AI需求

找对需求，开发就成功了一半，那么如何去确定真实世界中用户们最渴望的AI工具是什么呢？

全球最大的AI导航站，月访问量500万的 There's An AI For That 上线了一个AI需求频道，人人都能发帖说出自己的需求，其他人可以回复符合这个需求的AI产品。

现在上面有几百条需求，想要开发应用的可以去看一看，说不定能够找到自己能做的需求。

* 资讯地址:

https://theresanaiforthat.com/requests/

![image](https://github.com/aitobox/newsweekly/assets/137874861/2f99d32f-626c-4908-ae47-31b83f1241c4)



## AI服务和工具

#### 1. Mistral 正式发布 Mistral Large
  
Mistral 正式发布 Mistral Large在基准测试中仅次于GPT-4，超过其他所有模型。

* 功能特点

Mistral Large具有新的功能和优势：

它在英语、法语、西班牙语、德语和意大利语方面拥有母语般流利的能力，并对语法和文化背景有细致的理解。

其32K令牌的上下文窗口允许从大型文档中精确地寻找信息。

它精确的指令跟随能够让开发者设计他们的管理政策 - 我们用它来建立 le Chat 的系统级管理。

它本身就能够进行函数调用。这一点，再加上在la Plateforme上实现的受限输出模式，使得应用程序开发和技术栈现代化能够大规模进行。

支持在La Plateforme、Azure和私有部署。

还发布了具有低生成延迟的Mistral Small，Mistral Small的性能优于Mixtral 8x7B，并且具有更低的延迟。

其中，JSON格式模式强制语言模型输出为有效的JSON。此功能使开发人员能够更自然地与我们的模型进行交互，以提取结构化格式的信息，这些信息可以轻松地在其余的流水线中使用。

* 更多信息请参考：

https://mistral.ai/news/mistral-large/

* 体验地址

https://auth.mistral.ai/

![image](https://github.com/aitobox/newsweekly/assets/137874861/aee2b2e8-7c9c-4d27-ad19-1025f9911a3b)


#### 2. immersive translate--沉浸式观看各种外语网页和视频 

一个沉浸式的翻译浏览器插件

* 功能特点

支持网页翻译，文档翻译，支持40+视频国内外网站，100+语言双语字幕翻译，

沉浸式观看各种外语视频，包括YouTube、Vimeo、Udemy、NetFlix、Coursera、Bloomberg等。

* 体验地址:

https://www.producthunt.com/products/video-bilingual-subtitle-translation

![image](https://github.com/aitobox/newsweekly/assets/137874861/c0332c07-8b51-4683-8761-6644f54d4aeb)

#### 3. SUPIR-一个提升图片分辨率的工具

SUPIR：通过增加模型的规模（即增加模型的参数数量）提升图像修复的能力。

通过参数增加使得模型不仅能够修复图像中的错误或损坏，还能根据文本提示进行智能修复。

例如根据描述来改变图像中的特定细节。这样的处理方式提升了图像修复的质量和智能度，使得模型能够更准确、更灵活地恢复和改进图像。

* 功能特点

图像修复： SUPIR的核心功能是对低质量或损坏的图像进行修复，提高其视觉质量。这包括处理如模糊、噪点、色彩失真等问题，使图像恢复到高清晰度和高质量状态。

文本引导的修复： SUPIR能够根据文本提示来指导图像修复。这意味着用户可以通过文本描述来指定希望修复或改变的图像部分，使得修复过程更加定制化和精确。

* 核心技术创新：

1、模型放大： SUPIR通过扩大模型规模（即增加模型的参数数量）来提升图像修复的能力。这种放大使得模型能够学习更多的特征，处理更复杂的图像修复任务。

2、多模态技术： 结合了图像处理和文本处理的技术，允许模型不仅理解图像内容，还能理解与之相关的文本描述，从而进行更准确的修复。

3、高质量训练数据集：收集了2000万高质量图像和文本注释，用于训练和控制图像修复。利用大量高分辨率、高质量的图像和相关文本注释作为训练数据，提高了模型的性能和适用性。

4、负质量提示： 通过引入质量较差的图像样本和相应的负面描述作为训练数据，进一步提升模型在感知质量方面的表现。

* 工作原理：

1、图像编码与解码： SUPIR利用一个编码器将低质量图像映射到潜在空间，然后使用解码器重建修复后的图像。

2、文本处理： 通过一个多模态语言模型，SUPIR能够理解与图像相关的文本描述，并将这些信息融入到图像修复过程中。

3、适配器设计： SUPIR设计了一个大规模适配器，用于将模型的生成能力调整到与输入图像相匹配的状态，确保修复过程符合用户的具体需求。

4、采样方法： 采用特殊的采样方法，用于指导图像的恢复过程，以防止过度生成，确保修复后的图像保持真实和高质量。

* 体验地址:

https://t.co/0pmpsPQsnF

https://github.com/Fanghua-Yu/SUPIR

![image](https://github.com/aitobox/newsweekly/assets/137874861/f56ea9cf-720f-48f3-884a-cbf56c9e6082)


(完)
