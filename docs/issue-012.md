# AIToBox周刊：第 12 期

这里记录每周值得分享的AI科技内容，周末发布。

本杂志开源（GitHub: [aitobox/newsweekly](https://github.com/aitobox/newsweekly)），欢迎提交 issue，投稿或推荐你的项目。


## AI资讯

#### 1. Meta 发布新一代开源大模型 Llama 3.1

2024-07-24，Meta 正式发布新一代开源大模型 Llama 3.1 系列，提供 8B、70B 及 405B 参数版本。

**详细内容** 

Llama 3 使用了超过 1.6 万个 H100 GPU、以及超过 15T token 的公开数据进行训练。

架构方面，该模型选择标准的仅解码器 transformer 模型架构进行调整，而不是混合专家模型，以最大化训练稳定性。


此外，Llama 3 采用了迭代的后训练程序，每一轮使用监督微调和直接偏好优化。

Meta 表示，Llama 3.1 系列在推理能力和多语言支持方面进行了改善，其上下文长度被提升至 128K，而模型参数也被提高到了 4050 亿规模，是近年来规模最大的大语言模型之一。该模型在通用常识、可引导性、数学、工具使用和多语言翻译等广泛任务中足以对标 GPT-4、Claude 3.5 Sonnet 等领先闭源模型。

Llama 3.1 现已于 [Meta 官网](https://llama.meta.com/llama-downloads) 开放下载。

**资讯地址**

[Llama 3.1 论文](https://ai.meta.com/research/publications/the-llama-3-herd-of-models/)
[Llama 3.1 官方文档](https://llama.meta.com/docs/overview/)

![image](https://github.com/user-attachments/assets/fcaff352-673b-4ccd-b280-94516ebf74e0)


## AI服务和工具

#### 1.Lobe Chat-一键搭建你自己的大模型服务

Lobe Chat 是一个现代化设计的开源 ChatGPT/LLMs 聊天应用与开发框架；支持语音合成、多模态、可扩展的插件系统；一键免费拥有你自己的 ChatGPT/Gemini/Claude/Ollama 应用

**功能特点**

1. [多模型服务商支持](https://lobehub.com/docs/usage/features/multi-ai-providers)
2. [支持本地大语言模型 (LLM)](https://lobehub.com/docs/usage/features/local-llm)
3. [模型视觉识别 (Model Visual)](https://lobehub.com/docs/usage/features/vision)
4. [TTS & STT 语音会话](https://lobehub.com/docs/usage/features/tts)
5. [Text to Image 文生图](https://lobehub.com/docs/usage/features/text-to-image)
6. [插件系统 (Function Calling)](https://lobehub.com/docs/usage/features/plugin-system)
7. [助手市场 (GPTs)](https://lobehub.com/docs/usage/features/agent-market)
8. [支持本地 / 远程数据库](https://lobehub.com/docs/usage/features/database)
9. [支持多用户管理](https://lobehub.com/docs/usage/features/auth)
10. [渐进式 Web 应用 (PWA)](https://lobehub.com/docs/usage/features/pwa)
11. [移动设备适配](https://lobehub.com/docs/usage/features/mobile)
12. 既可以本地部署，也可以试用官方的服务

**体验地址**

https://lobechat.com/

![image](https://github.com/user-attachments/assets/c42a9726-8559-42f7-a8c9-c22db8abc35e)

![image](https://github.com/user-attachments/assets/01f408be-acd7-49f5-9975-a8f1498a728c)


#### 2. Fish Speech-支持中英日语言、效果非常好的开源TTS模型

支持中日英语言，支持文字转语音的TTS开源模型

**功能特点**

* 语音处理接近人类水平

* 模型使用约十五万小时三语数据训练，对中文支持非常的完美。


**体验地址**

https://speech.fish.audio/


![image](https://github.com/aitobox/newsweekly/assets/137874861/9b0a6022-98ec-4e54-9cce-0ed898da89b3)


(完)
