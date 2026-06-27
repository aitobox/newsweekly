# AIToBox周刊：第 20 期

这里记录每周值得分享的AI科技内容，周末发布。

本杂志开源（GitHub: [aitobox/newsweekly](https://github.com/aitobox/newsweekly)），欢迎提交 issue，投稿或推荐你的项目。


## AI资讯

#### 1. Meta发布 Llama 4 模型

4月6日，Meta推出首批 Llama 4 模型：Llama 4 Scout 与 Llama 4 Maverick

**详细内容** 

Llama 4 Scout
• 采用 17 亿活跃参数模型，配备 16 位专家系统。
• 拥有业界领先的 1000 万 token 上下文窗口。
• 在广泛认可的基准测试中表现优于 Gemma 3、Gemini 2.0 Flash-Lite 和 Mistral 3.1。

亮点：17B活跃参数的 16 位专家MoE模型，1000 万上下文窗口，仅需单个 NVIDIA H100 GPU 可运行

Llama 4 Maverick
• 170 亿活跃参数模型，配备 128 位专家。
• 顶尖的图像接地能力，能够将用户提示与相关视觉概念对齐，并将模型响应锚定到图像中的特定区域。
• 在广泛认可的基准测试中全面超越 GPT-4o 和 Gemini 2.0 Flash。
• 推理与编码能力媲美 DeepSeek v3，而激活参数量仅为其一半。
• 在 LMArena 上以 1417 ELO 分数实现无与伦比的性价比表现（聊天版本）。

亮点：17B活跃参数的128 位专家MoE模型，LLM竞技场得分最高的开源模型，支持图像多模态识别

**资讯地址**

https://ai.meta.com/blog/llama-4-multimodal-intelligence/

![image](https://github.com/user-attachments/assets/e6d419fc-c028-4fbf-8f72-43306461b24d)



#### 2. 谷歌发布Gemini 2.5人工智能模型

谷歌于3月25日晚正式推出新一代人工智能推理模型Gemini 2.5，该模型以“思考-验证-回答”的多模态推理能力为核心，被谷歌称为“目前最智能的模型”。

**详细内容** 

其旗舰版本Gemini 2.5 Pro Experimental在多项基准测试中超越OpenAI、Anthropic等竞争对手，尤其在代码生成和数学推理领域表现亮眼，标志着AI技术在复杂任务处理上的重大突破。

Gemini 2.5 Pro支持文本、图像、音频、视频及代码的多模态输入，上下文窗口达100万token（约75万单词），可解析完整《指环王》系列文本，未来将升级至200万token。这一能力使其在处理跨模态复杂问题时更具优势。

代码生成：在Aider Polyglot代码编辑测试中得分68.6%，超越OpenAI、Anthropic等模型；SWE-bench Verified测试中获63.8%，仅次于Claude 3.7 Sonnet（70.3%）。

数学与科学推理：在“人类最后考试”（多模态综合测试）中以18.8%准确率领先多数竞品，且无需依赖外部工具。

通用能力：在LMArena排行榜上以40分优势超越GPT-4.5，登顶视觉竞技场（Vision Arena）及网页开发竞技场（WebDev Arena）。

Gemini 2.5 Pro即日起通过Google AI Studio和Gemini应用向订阅“Gemini Advanced”（月费20美元）的用户开放，未来将登陆Vertex AI平台。谷歌暂未公布API定价，但表示将在几周内披露企业级应用方案。

**资讯地址**

https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/

![image](https://github.com/user-attachments/assets/715441bc-f47e-41a7-9e82-b987c8d84672)



#### 3. 通义千问Qwen3模型发布

2025年4月29日，阿里巴巴发布并开源了新一代大语言模型——通义千问Qwen3（以下简称“千问3”）。作为阿里巴巴通义系列的最新成员，千问3在技术架构、性能指标及部署成本上均有所突破，尤其在Agent能力和模型上下文协议（MCP）支持方面表现突出，值得开发者关注。

**详细内容** 

模型架构与规模
千问3共提供了8个模型版本，覆盖了从轻量级到超大规模的广泛需求，包含：

MoE（混合专家）模型：30B（激活参数3B）与235B（激活参数22B）两款。
Dense（稠密）模型：提供0.6B、1.7B、4B、8B、14B、32B多种规模。
其旗舰型号——千问3-235B-A22B在多个国际基准测试（如数学、编程、综合任务）中表现优异，与DeepSeek-R1、OpenAI-o1、Grok-3等国际一线模型不相上下，甚至在部分任务上稍有领先。相较于前代产品，千问3实现了相同甚至更低参数量下的显著性能提升，例如，Qwen3-30B-A3B仅需激活3B参数，即可匹敌前代Qwen2.5-32B模型。

Agent与工具调用能力
千问3的显著特性之一，是在Agent能力上的明显提升：

在专门评估Agent任务能力的BFCL基准测试中，千问3达到70.8分，表现超过Gemini 2.5 Pro、OpenAI-o1等高端模型。这意味着千问3在Agent调用、环境交互、任务理解与执行方面表现突出，更易集成于复杂的AI任务和智能体应用中。
同时，千问3原生支持工具调用（Function Calling）特性，配合Qwen-Agent框架，提供预封装的工具调用模板和解析器，大幅降低开发门槛，适合快速开发基于AI Agent的应用场景，例如移动端、桌面端的助手类、任务自动化及环境交互式应用。
MCP模型上下文协议支持
Qwen3还原生支持一种名为模型上下文协议（MCP）的特性：

MCP使模型能够动态感知并管理上下文信息，在执行多轮对话或复杂任务时，可显著提高上下文感知的稳定性与响应准确性。
在API调用时，开发者能够明确指定模型的“思考预算”（即预期的最大推理深度或tokens数），实现精准控制，灵活满足不同场景下的算力成本与响应质量需求。
千问3提出的“快思考”与“慢思考”混合推理模式，通过MCP进行上下文动态切换，使得模型对简单请求可快速响应，对复杂任务则自动采用深入的多步骤推理模式。
部署便利性
千问3在部署方面也颇具吸引力：

旗舰级235B模型仅需4张H20 GPU即可部署，显存占用仅为同性能级别模型的1/3，这显著降低了企业用户的部署成本门槛。
小尺寸模型如4B、8B则可轻松部署到手机、PC、汽车等端侧设备，适合于各种嵌入式与边缘计算场景。
推荐部署工具包括SGLang、vLLM、Ollama、LMStudio、MLX、llama.cpp、KTransformers，满足从个人到企业的多样化需求。

多语言能力
Qwen3支持119种语言和方言，包括中文（普通话、粤语）、英语、日语、韩语，以及多种东南亚、欧洲、中东语言。这种广泛的语言支持，有利于千问3在国际化应用与全球市场拓展中发挥作用。

开源与商用
千问3系列模型沿用Apache 2.0协议开源，全球开发者均可自由下载、修改、商用。提供的平台包括：

**资讯地址**

https://qwenlm.github.io/blog/qwen3/

![image](https://github.com/user-attachments/assets/d79a9c14-8a65-461c-a833-e4567d5a9d94)



## AI服务

#### 1. 闪稿Ai论文- 一键生成高质量论文初稿

来源于网友自荐服务：选择专业,输入论题,一键生成高质量原创论文初稿

**功能特点** 

闪稿Ai论文，好用的ai智能论文生成工具.闪稿AI论文写作助手,选择专业,输入论题,一键生成高质量原创论文初稿.毕业论文,期刊论文,职称论文

**服务地址**

https://www.shangaoai.com/


![image](https://github.com/user-attachments/assets/755cf470-5320-4208-8ca3-03942fb17ef0)



## 往期推荐

* [AI资讯快报](https://github.com/aitobox/newsweekly/issues?q=is%3Aissue+is%3Aclosed+label%3AAI%E8%B5%84%E8%AE%AF%E5%BF%AB%E6%8A%A5)
* [AI服务推荐](https://github.com/aitobox/newsweekly/issues?q=is%3Aissue+is%3Aclosed+label%3AAI%E6%9C%8D%E5%8A%A1%E6%8E%A8%E8%8D%90)
* [AI文章推荐](https://github.com/aitobox/newsweekly/issues?q=is%3Aissue+is%3Aclosed+label%3AAI%E6%96%87%E7%AB%A0%E6%8E%A8%E8%8D%90)

(完)


