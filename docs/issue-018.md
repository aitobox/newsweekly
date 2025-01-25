# AIToBox周刊：第 18 期

这里记录每周值得分享的AI科技内容，周末发布。

本杂志开源（GitHub: [aitobox/newsweekly](https://github.com/aitobox/newsweekly)），欢迎提交 issue，投稿或推荐你的项目。


## AI资讯

#### 1. 英伟达推出个人计算产品Project DIGITS

在正在举办的CES 2025上，英伟达创始人兼CEO黄仁勋宣布，将推出了全新的个人计算产品Project DIGITS。据介绍，Project DIGITS搭载了英伟达GB10超级芯片，提供千万亿次的AI计算性能，可支持AI大模型的原型设计、微调和运行。Project DIGITS的愿景：超算中心搬回家

**详细内容** 

Project Digits的核心是新一代 GB10 Grace Blackwell 芯片，这款桌面级系统可以处理高达2000 亿参数的 AI 模型，同时使用标准家用电源插座实现供电——这点在以往同等算力需要更大且耗电更多的硬件上来讲通常是难以想象的事。

在 CPU 部分，Project Digits 采用英伟达自家的 Grace CPU，采用定制 20 核心 ARM 架构，每台系统配备了 128GB 的统一内存以及高达 4TB 的 NVMe 存储空间。

从渲染图来看，竟然还有2个QSFP28或者更高速别的以太网接口，这意味着可能单机就能跑100G甚至400G以太网，能非常容易的组建多机互联。而且双口还可以组成环形拓扑。

目前该设备起售价3000美元，可能是未来的个人AI中心的雏形，可能开拓一个全新的设备市场品类；

**资讯地址**

https://resources.nvidia.com/en-us-data-center-overview/hpc-datasheet-grace-cpu-superchip

![image](https://github.com/user-attachments/assets/720144a8-8611-472f-946a-f579ce4d7160)


#### 2. DeepSeek发布并开源 R1 模型

DeepSeek发布并开源 R1 模型，性能对标 OpenAI o1 正式版； 引起了极大关注；

**详细内容** 

* DeepSeek-R1 在后训练阶段大规模使用了强化学习技术，在仅有极少标注数据的情况下，极大提升了模型推理能力。

* 在数学、代码、自然语言推理等任务上，性能比肩 OpenAI o1 正式版。

* DeepSeek开源了DeepSeek-R1 和 DeepSeek-R1-Zero两个模型，660B 参数。

* 并通过模型蒸馏，开源 6 个小模型，其中 32B 和 70B 模型在多项能力上超越 OpenAI o1-mini。

* 目前它的API价格极其低廉：缓存命中每百万输入 tokens 1 元，未命中 4 元；输出 tokens 每百万 16 元。

**资讯地址**

https://github.com/deepseek-ai/DeepSeek-R1/tree/main

**体验地址**

https://chat.deepseek.com/

![image](https://github.com/user-attachments/assets/307a83f8-34fb-454d-b6cc-097240122adb)


#### 3. Kimi.ai 推出 Kimi k1.5 --- o1 级多模态模型

Kimi.ai 推出 Kimi k1.5 --- o1 级多模态模型，国产开源AI大模型竞争激烈；

**详细内容** 

* Sota short-CoT 性能，在 AIME、MATH-500、LiveCodeBench 上的表现大大优于 GPT-4o 和 Claude Sonnet 3.5 💻 （高达 +550%）

* Long-CoT 性能在多种模态（MathVista、AIME、Codeforces 等）中匹配 o1

* 长上下文缩放。高达 128k 个令牌用于生成 RL。部分推出的高效训练。

* 改进的策略优化：在线镜像下降、采样策略、长度惩罚等。

* 多模式。文本和视觉的联合推理。

**资讯地址**

https://github.com/MoonshotAI/Kimi-k1.5

![image](https://github.com/user-attachments/assets/6cb2e98e-6b7d-4fcc-ae72-b571c8284cfa)


## AI服务

#### 1. 字节推出 Cursor 的竞品 Trae 

字节新出了个 Cursor 的竞品 Trae ，可以用 claude3.5，限时免费；目前只支持MacOS；

**功能特点** 


* Builder 模式

自动分解和执行任务，优化每一步，并允许用户预览和控制流程。
 
* 多模态能力

支持上传图像，精准理解需求，提升协作效率。
 
* 上下文理解

分析整个代码库，利用编辑器和终端的洞察力，提供更精确的代码生成和定制修改。

* 智能自动补全

实时扩展代码，预测用户意图并自动应用更改。

**服务地址**

https://www.trae.ai/

![image](https://github.com/user-attachments/assets/95c277bc-1354-4eaa-955a-5c95041d03f7)


## AI文章

#### 1. DeepSeek-R1 的技术报告

DeepSeek开源了一系列新模型，DeepSeek-R1-Zero和DeepSeek-R1，能力接近OpenAI o1；1.5B到70B大小的开源模型蒸馏版本；

他们的模型训练成本低到让人震惊，他们也将自己的思考和实践都总结为论文分享出来，采用MIT 许可全面开源，这些技术文章值得细细学习；

**详细内容** 

* 采用 GRPO 算法: GRPO 算法相较于传统的 RL 算法，省去了 critic model，节省了训练成本。  

* 基于规则的奖励模型: DeepSeek 主要使用基于规则的奖励系统，避免了训练和重新训练神经网络奖励模型的额外成本。  

* 简单的训练模板: DeepSeek 使用简单的训练模板，避免了内容特定的偏差，减少了训练的复杂度。  

* 蒸馏技术: DeepSeek 使用蒸馏技术将大型模型的推理能力迁移到较小的模型上，从而降低了训练成本。 

**文章地址**

https://github.com/deepseek-ai/DeepSeek-R1/

![image](https://github.com/user-attachments/assets/3cc7d679-2ca4-4818-b53c-3f13d463a382)




## 往期推荐

* [AI资讯快报](https://github.com/aitobox/newsweekly/issues?q=is%3Aissue+is%3Aclosed+label%3AAI%E8%B5%84%E8%AE%AF%E5%BF%AB%E6%8A%A5)
* [AI服务推荐](https://github.com/aitobox/newsweekly/issues?q=is%3Aissue+is%3Aclosed+label%3AAI%E6%9C%8D%E5%8A%A1%E6%8E%A8%E8%8D%90)
* [AI文章推荐](https://github.com/aitobox/newsweekly/issues?q=is%3Aissue+is%3Aclosed+label%3AAI%E6%96%87%E7%AB%A0%E6%8E%A8%E8%8D%90)

(完)
