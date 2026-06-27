# AIToBox周刊：第 9 期

这里记录每周值得分享的AI科技内容，周末发布。

本杂志开源（GitHub: [aitobox/newsweekly](https://github.com/aitobox/newsweekly)），欢迎提交 issue，投稿或推荐你的项目。


## AI资讯

#### 1. Meta 发布开源模型 Llama 3

Meta 发布开源模型 Llama 3，以及新版本Meta AI 助手

Meta同时还发布了由Meta Llama 3驱动的Meta AI助手，Meta AI整合了搜索功能现在可以在Facebook、Instagram、WhatsApp和Messenger上使用。

**详细内容**
  
Llama3的几个核心点：

1. 本体具备中文能力，对话时需要使用Prompt 以后请使用中文回答 来激发。期待社区的ft版本，估计很快。
2. 70B 性能碾压gpt-3.5-turbo，不足GPT-4。
3. 400B 是dense model，也是目前推理效率最低的模型（GPT-4是220B激活的MoE模型，总参数1.2TB左右）。性能号称和GPT-4持平，数月后放出。

**资讯地址**

https://llama.meta.com/llama3/

![image](https://github.com/aitobox/newsweekly/assets/137874861/6727fa36-50f6-4840-a8f9-c05031b765ca)



## AI服务和工具

#### 1.ChatGPT3.5将免费免注册使用
  
OpenAI 表示，它正在向用户提供流行 AI 聊天机器人的免费 G​​PT 3.5 版本，而无需用户先注册。

**详细内容**

“对于任何对人工智能的潜力感到好奇但又不想完成设置帐户步骤的人，请立即开始使用 ChatGPT，”该公司在谈到更新时表示。

目前，想要使用“免费人工智能系统”的用户必须创建一个 OpenAI 帐户才能访问该机器人。

不过，想要成为 Plus 订阅会员并访问更先进的 ChatGPT-4（其中包括 OpenAI 的 DALL·E 2 文本到图像生成模型）的人仍然需要创建一个帐户。

OpenAI此举可能是为正在提出的GPT 5做一系列准备，结合此前的逐步取消GPT 4的聊天条数限制，应该是逐步在下放一些功能到基础模型！

同时OpenAI未来有可能将会把GPT 3.5这样基础模型将变成一个通用的模型，任何人都可以直接免费使用，加入网络搜索功能，变成通用的搜索引擎！

需要说明的是，并非所有地区的用户都可以免登录直接使用 ChatGPT，相关的区域支持还在逐渐扩展中，多数区域暂时仍需要注册账号才能使用

**资讯地址**

https://openai.com/blog/start-using-chatgpt-instantly

![image](https://github.com/aitobox/newsweekly/assets/137874861/02bace2e-5b7d-49ea-a71e-cb1d1934e26b)


#### 2. midreal.ai: 让AI帮你写爽文

Midreal AI是一款由MIT、NYU、剑桥、普林斯顿联合打造的AI生成小说产品；

**功能特点**
即使是ChatGPT，写一些比较长的小说也会出现连贯性问题；Midreal AI就是为了解决这一问题，用来写有连贯性小说的工具；

之前它是在Discord 里面使用的，最近推出了网页版本；他的能力有：

* Midreal AI的核心竞争力在于其前沿技术，尤其是内存跨越技术和长篇写作能力。
* 解决了以往文本互动游戏中连贯性难以维持的问题。该技术能够实现近乎无限的记忆保留，确保故事线连贯无缝，提供用户一个持久的故事体验。
* 不仅是小说生成器，Midreal AI能够根据用户输入生成引人入胜的长篇故事。这在大型语言模型中是罕见的，展示了其在文本生成、故事构架和情节发展上的深度理解。
* 目前支持英文和中文，未来还将添加更多语言，包括日语。这使得Midreal AI能够跨越语言障碍，服务更广泛的用户群体。
* 不仅是游戏或小说生成器，Midreal AI是一个全新的故事叙述平台，为用户提供前所未有的创造空间和自由度。
* 通过创新技术，Midreal AI不仅改变了用户与故事互动的方式，也在人工智能领域中开创了新的可能性。
* 适用于游戏玩家、小说爱好者、电视剧和电影迷，以及同人小说创作者，为他们提供一个无限创造的空间。

**体验地址**

https://midreal.ai/

![image](https://github.com/aitobox/newsweekly/assets/137874861/31804d6d-04a5-4e07-a162-2601d4282943)


## AI文章

#### 1. 微软介绍用图片生成人脸视频的VASA项目

微软介绍其内部实现的一个VASA-1项目，只需要一张单人像照片+语音音频，就可以生成超逼真的人脸视频

**详细内容**

* 可以生成长达一分钟的视频，而且保持唇部同步，还能捕捉到大量的情感和表情细微差别以及自然的头部动作。

* 支持接受可选信号作为条件，例如主眼注视方向和头部距离，以及情绪偏移。

* 能够处理超出训练分布的照片和音频输入。它可以处理艺术照片、歌唱音频和非英语语音。

* 支持表情和姿势的编辑。

* 在离线批处理模式下以每秒 45 帧的速度生成 512x512 大小的视频帧，在在线流模式下可支持高达每秒 40 帧的速度，之前的延迟时间仅为 170 毫秒。

**论文地址和介绍**

https://www.microsoft.com/en-us/research/project/vasa-1/

![image](https://github.com/aitobox/newsweekly/assets/137874861/86ed99b5-995a-4e29-a8eb-95401a8a5fb3)


(完)
