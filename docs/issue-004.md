# AIToBox周刊：第 4 期

这里记录每周值得分享的AI科技内容，周末发布。

本杂志开源（GitHub: [aitobox/newsweekly](https://github.com/aitobox/newsweekly)），欢迎提交 issue，投稿或推荐你的项目。


## AI资讯

#### 1. OpenAI服务更新

详细内容
新嵌入模型推出：

• 推出了两种新的嵌入模型：text-embedding-3-small和text-embedding-3-large。

新一代向量大模型text-embedding-3，embedding长度升级，价格最高下降5倍，包含2个版本，新增了一个可以控制生成的向量长度的参数！

新一代嵌入模型性能对比：

• 小型模型(text-embedding-3-small)对比：与上一代模型text-embedding-ada-002相比，新模型在多语言检索基准(MIRACL)上的平均得分从31.4%提高到44.0%，在英语任务基准(MTEB)上的平均得分从61.0%提高到62.3%。

• 大型模型(text-embedding-3-large)对比：与text-embedding-ada-002相比，在MIRACL上平均得分从31.4%提高到54.9%，在MTEB上从61.0%提高到64.6%。

• 新模型的性能普遍优于上一代模型，尤其是在多语言检索方面表现出色。

GPT-3.5 Turbo降价对比：

• 新的GPT-3.5 Turbo模型gpt-3.5-turbo-0125的输入价格降低50%，至$0.0005 /1K tokens，输出价格降低25%，至$0.0015 /1K tokens。

• 降价旨在帮助客户扩大规模使用，同时该模型还包含多项改进，如提高响应准确度和修复非英语语言功能调用的文本编码问题。

新内容审核模型发布：

• 发布了新的内容审核模型text-moderation-007，作为提高内容安全的一部分。

API使用和管理改进：

• 提供了更多的API使用可视化和控制工具，如API密钥权限分配和API使用情况的仪表板。


原文请参考[这里](https://openai.com/blog/new-embedding-models-and-api-updates)

#### 2. 2023年最受欢迎的人工智能工具

人工智能在2023年取得了重大突破，其中最受关注的是大型语言模型（LLM）和图像生成器。文章列出了最受欢迎的AI工具，并提供了这些工具的网站访问量数据。

其中，ChatGPT成为最受欢迎的工具，占网站访问量的60.2%。其他受欢迎的工具包括Character.AI、QuillBot、Midjourney和Hugging Face。文章还讨论了这些工具在技术采用周期中的角色以及它们如何推动用户采用新技术。最后指出，尽管这些AI工具已经非常强大，但随着公众对AI的接受度提高，未来将会出现更多功能强大且独特的AI工具和产品。

[资讯地址](https://www.visualcapitalist.com/ranked-the-most-popular-ai-tools/)

![image](https://github.com/aitobox/newsweekly/assets/137874861/afb6cedd-e994-47b6-bd3d-a8a0f038b767)


#### 3. 亚马逊已经部署了超过 750,000 台机器人

亚马逊已经部署了超过 750,000 台机器人。而 10 年前，机器人数量不过 1000 台！

下面是近 10 年来亚马逊机器人数量的数据：

* 2013: 1,000
* 2014: 15,000
* 2017: 100,000
* 2019: 200,000
* 2021: 350,000
* 2022: 520,000
* 2023: 750,000

如果你注意看，会发现最近两年的增长幅度相当大，在短短两年内，亚马逊额外增加了 40万台机器人。这意味着他们几乎每周都部署了几千台新的机器人 ！

很明显。毫无疑问。人工智能、机器人技术、计算机视觉正在取代大量人力工作。并将在未来十年继续加速这一进程。

重要的是要注意，这也将加速对更多高技能工作的需求。使行业更安全。

我们将面临的最大挑战是在不久的将来需要重新培训和提升技能的劳动力的庞大规模。

我们一下子进入了机器人时代和智能时代。

[资讯地址](https://twitter.com/LinusEkenstam/status/1749216813416636791)

![image](https://github.com/aitobox/newsweekly/assets/137874861/3d4b21aa-a4cc-45aa-b11b-06eac5036d50)


#### 4. 用AI技术创作的货币演进视频

有人为人类从原始时代的物物交换开始，到最新的区块链技术，这个演进过程制作了一个视频，非常形象生动

这个视频的场景切换非常完美的体现了人类多个世代的金融演进过程，作者说是AI技术帮助创作的；这个片子可能就是预示着未来AI和区块链技术能产生的深远影响，仅仅43秒，推荐大家看一看，

[资讯地址](https://twitter.com/intothefab/status/1749889115187736909)

![image](https://github.com/aitobox/newsweekly/assets/137874861/e6a813fe-08d5-4254-a1cc-baed167e8576)


## AI文章推荐

#### 1. Lumiere：一次性生成整个视频

Google Research团队开发的基于空间时间的文本到视频扩散模型。

它采用了创新的空间时间U-Net架构，能够一次性生成整个视频的时间长度，不同于其他模型那样逐帧合成视频。

确保了生成视频的连贯性和逼真度。

支持文本到视频、图像到视频 、风格化视频生成 、视频编辑等

主要功能特点：

1、文本到视频的扩散模型： Lumiere能够根据文本提示生成视频，实现了从文本描述到视频内容的直接转换。

2、空间时间U-Net架构： 与其他需要逐步合成视频的模型不同，Lumiere能够一次性完成整个视频的制作。这种独特的架构允许Lumiere一次性生成整个视频的时间长度，不同于其他模型那样逐帧合成视频。

3、全局时间一致性： 由于其架构的特点，Lumiere更容易实现视频内容的全局时间一致性，确保视频的连贯性和逼真度。

4、多尺度空间时间处理： Lumiere通过在多个空间时间尺度上处理视频来学习直接生成视频，这是一种先进的方法。

5、风格化视频生成： 使用单个参考图像，Lumiere可以按照目标风格生成视频，这种能力在其他视频生成模型中较为罕见。

6、广泛的内容创作和视频编辑应用： Lumiere支持多种内容创作任务和视频编辑应用，如图像到视频、视频修补和风格化生成。

视频样式化编辑： 使用文本基础的图像编辑方法，Lumiere可以对视频进行一致性的样式编辑。

影像合成能力： 该模型能在用户指定的区域内对图像内容进行动画化处理，为静态图像增添动态效果。

视频修补功能： Lumiere提供视频修补功能，能够在视频中修改和修饰特定内容。

[体验地址](https://lumiere-video.github.io/)

[论文地址](https://arxiv.org/abs/2401.12945)

![image](https://github.com/aitobox/newsweekly/assets/137874861/192bb9c0-477a-49f1-bd55-db68ca6e7592)



## AI服务和工具

#### 1. [GPT-SoVITS-适用于中文的语音克隆](https://www.bilibili.com/video/BV12g4y1m7Uw/)

GPT-SoVITS是一个声音克隆和文本到语音转换的开源 Python RAG框架。

5秒数据就能模仿你，1分钟的声音数据就能训练出一个高质量的TTS模型，完美克隆你的声音！

根据演示来看完美适配中文，应该是目前中文支持比较好的模型。

界面也易用。

主要特点：

1、零样本 TTS： 输入5 秒的声音样本即可体验即时的文本到语音转换。

2、少量样本训练： 只需 1 分钟的训练数据即可微调模型，提高声音相似度和真实感。模仿出来的声音会更加接近原声，听起来更自然。

跨语言支持： 支持与训练数据集不同语言的推理，目前支持英语、日语和中文。

3、易于使用的界面：集成了声音伴奏分离、自动训练集分割、中文语音识别和文本标签等工具，帮助初学者更容易地创建训练数据集和 GPT/SoVITS 模型。

4、适用于不同操作系统： 项目可以在不同的操作系统上安装和运行，包括 Windows。

5、预训练模型： 项目提供了一些已经训练好的模型，你可以直接下载使用。

[体验地址](https://github.com/RVC-Boss/GPT-SoVITS)


（完）
