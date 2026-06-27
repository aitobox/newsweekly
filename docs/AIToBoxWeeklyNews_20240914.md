# AIToBox周刊：第 14 期

这里记录每周值得分享的AI科技内容，周末发布。

本杂志开源（GitHub: [aitobox/newsweekly](https://github.com/aitobox/newsweekly)），欢迎提交 issue，投稿或推荐你的项目。


## AI资讯

#### 1. OpenAI 发布全新的 o1 系列模型

北京时间 9 月 13 日午夜，OpenAI 宣布推出其全新产品 OpenAI o1，也就是此前广受期待的代号为 “草莓（Strawberry）” 生成式 AI 模型。

**详细内容** 

o1 实际上一系列用于解决难题的全新推理模型，经过强化学习训练可以执行复杂的推理，擅长准确生成和调试复杂代码。目前发布的是 OpenAI o1-preview 版本以及 OpenAI o1-mini。OpenAI o1-mini 是一种速度更快、成本更低的推理模型，作为一款较小的模型，o1-mini 比 o1-preview 便宜 80%。

OpenAI 表示，对于复杂推理任务而言，新模型代表着 AI 能力的崭新水平，因此值得将计数重置为 1，并将该系列命名为 OpenAI o1，给它一个有别于 “GPT-4” 系列的全新名号。

测试结果表明，OpenAI o1 在竞争性编程问题（Codeforces）中排名第 89 位，在美国数学奥林匹克 (AIME) 预选赛中跻身美国前 500 名学生之列（o1 正确解答了 83% 的题目，而 GPT-4o 仅解答了 13%。），并在物理、生物和化学问题 (GPQA) 基准测试中超越人类博士级准确度。

**资讯地址**

https://openai.com/o1/

![image](https://github.com/user-attachments/assets/c298669e-a03a-404b-b16c-608e5a9bed50)

![image](https://github.com/user-attachments/assets/e09ab19c-e8df-472c-95d8-c74b4c4c4eaf)


## AI文章

#### 1. MiniMind-教你3小时完全从0训练一个仅有26M的小参数GPT

这是一份开源教程，旨在完全从0开始，最快仅用3小时！即可训练出仅为26M大小的微型语言模型MiniMind

**详细内容** 

项目的目标是把上手LLM的门槛无限降低， 直接从0开始训练一个极其轻量的语言模型。

1. 提供完整的训练流程代码，包括预训练、指令微调、LoRA微调和DPO偏好优化等。
2. 支持单机单卡、单机多卡(DDP、DeepSpeed)训练，并支持在任意位置停止和继续训练。
3. 实现了Openai-Api基本的chat接口，方便集成到第三方ChatUI使用。
4. 提供了多个不同参数量的MiniMind模型供选择，最小仅需26M参数。
5. 在Ceval数据集上进行了模型测试和评估。

**项目地址**

https://github.com/jingyaogong/minimind

![image](https://github.com/user-attachments/assets/48e62795-cb2d-4eff-b8b2-52427699b032)
![image](https://github.com/user-attachments/assets/f5ddac06-1a51-470c-a590-bca80b09ffc7)

## AI服务

#### 1. Monica - ChatGPT4 驱动的 AI Copilot

这是一个浏览器助手，针对每个网站推荐常用的 AI 工具，包括翻译、总结内容，回答复杂问题，撰写邮件，阅读文章，智能搜索。随处可用。

**功能特点** 

你的 AI 全能助手，由GPT-4 驱动。回答复杂问题，撰写邮件，阅读文章，智能搜索。随处可用。

🔥 Monica是您的全能GPT-4 AI助手。
按下Cmd/Ctrl + M，即可启动。
我们提供搜索、阅读、写作、翻译、绘画等多种任务的帮助。

💪主要功能：
👉与AI聊天
✔️多聊天机器人：在一个平台上与GPT-3.5、GPT-4、Bard和Claude等多种LLM模型进行交流。
✔️提示图书馆：在提示库中用'/'快速访问保存的历史提示。
✔️实时信息：获取当前实时网络信息。
✔️语音支持：使用麦克风按钮无需打字即可聊天。

👉聊天与摘要
✔️ChatPDF：上传并与PDF聊天，更好地理解内容。
✔️与图片聊天：上传图片，借助GPT-4V进行内容提问。
✔️网页摘要：无需阅读整个网页即可获取摘要。
✔️YouTube摘要：无需观看整个视频即可获取摘要。

👉搜索
✔️搜索代理：提问后我们会使用多个关键字搜索、审查并找到答案。
✔️搜索增强：在Google和New Bing等搜索引擎旁边加载ChatGPT的回答。

👉写作
✔️撰写：使用'compose'快速定制撰写论文或报告，并控制篇幅、风格和语调。
✔️写作代理：只需提供一个主题，我们就会自动起草带有延伸内容和参考资料的大纲。
✔️电子邮件回复：在Gmail中，我们根据邮件内容提供回复选项，允许您点击选择回复，无需打字。

👉翻译
✔️PDF翻译：翻译PDF，并将左侧原文和右侧译文进行比较。
✔️平行翻译：翻译网页时不遮盖原文，以便进行语言对比和获取准确答案。
✔️文本翻译：即时翻译网页上选定的文本。

👉创作艺术
✔️将您的文字转换为视觉图像。只需输入简短的文本，您就可以成为画家。

👉 AI Memo
✔️Memo是一个AI知识库，您可以在其中保存网页、聊天记录、图片和PDF。通过与Memo聊天的方式来查找信息，随着其内容的增长，我们可以为您提供更加个性化和准确的回复。

**服务地址**

https://monica.im/home

![image](https://github.com/user-attachments/assets/0cb7d2f1-7ee0-4195-871d-7d5d8040ee9d)

![image](https://github.com/user-attachments/assets/1baa52d9-0cac-49c7-87d4-647d6840b800)


## 往期推荐

* [AI资讯快报](https://github.com/aitobox/newsweekly/issues?q=is%3Aissue+is%3Aclosed+label%3AAI%E8%B5%84%E8%AE%AF%E5%BF%AB%E6%8A%A5)
* [AI服务推荐](https://github.com/aitobox/newsweekly/issues?q=is%3Aissue+is%3Aclosed+label%3AAI%E6%9C%8D%E5%8A%A1%E6%8E%A8%E8%8D%90)
* [AI文章推荐](https://github.com/aitobox/newsweekly/issues?q=is%3Aissue+is%3Aclosed+label%3AAI%E6%96%87%E7%AB%A0%E6%8E%A8%E8%8D%90)

(完)
