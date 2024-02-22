# AIToBox周刊：第 6 期

这里记录每周值得分享的AI科技内容，周末发布。

本杂志开源（GitHub: [aitobox/newsweekly](https://github.com/aitobox/newsweekly)），欢迎提交 issue，投稿或推荐你的项目。


## AI资讯

#### 1. OpenAI宣布ChatGPT的一项重要更新：增加了记忆功能和新的用户控制选项

GPT现在可以在与用户的交互中跨聊天记住你们互动的所有信息，并在后续对话中利用这些信息来提供更相关和个性化的回答。

之前测试的内容是GPT可以利用你们之间的对话来自我进化和学习，但是这一次没有提及这些功能！只说了改进聊天回答！

主要特点和功能：

• 记忆功能： ChatGPT可以跨所有聊天记住用户讨论的事情，减少用户重复提供信息的需要，让未来的对话更加有用。

• 用户控制： 用户可以显式地告诉ChatGPT记住某些内容，询问它记住了什么，通过对话或设置告诉它忘记某些信息，甚至可以完全关闭记忆功能。

• 如何工作： 用户与ChatGPT聊天时，可以要求它记住特定的信息或让它自行捕捉细节。ChatGPT的记忆功能会随着使用的增加而改善，并且用户会逐渐注意到这种改进。

• 隐私和安全标准： 记忆功能带来了额外的隐私和安全考虑，OpenAI采取措施评估和减轻偏见，并避免ChatGPT主动记住敏感信息，除非用户明确要求。

• 企业和团队用户： 对于企业和团队用户，记忆功能可以在使用ChatGPT进行工作时提供帮助，学习用户的风格和偏好，并在过去的互动上建立，节省时间并提供更相关和深刻的响应。

• GPTs也将拥有记忆： GPTs将拥有自己独特的记忆。构建者将有选项为他们的GPTs启用记忆功能。与用户的聊天一样，记忆不会与构建者共享。

* 资讯地址:

https://openai.com/blog/memory-and-new-controls-for-chatgpt


![image](https://github.com/aitobox/newsweekly/assets/137874861/0042daff-547a-4595-bdac-fa62132c5116)

#### 2. 谷歌Bard正式改名！同时宣布上线“有史以来最强大模型”Ultra 1.0"

2月8日，谷歌宣布，将旗下AI聊天机器人Bard正式更名为Gemini。同时宣布推出新的订阅计划，允许用户访问其“最强大模型”Gemini Ultra 1.0，与竞争对手OpenAI的GPT-4直接竞争。

Bard全新升级后，参数较低的版本将继续免费供用户使用，但愿意每月支付19.99美元的用户可以使用谷歌Gemini的最强版本。安卓用户可以下载一个新的专用安卓应用程序来使用Gemini，而iPhone用户可以在iOS上的谷歌应用中使用Gemini。用户通过谷歌One（该公司的付费存储服务）访问的费用为每月19.99美元，对于现有的谷歌One订阅者，还提供两个月的免费试用期。

谷歌表示，这是其迄今为止最大、功能最强的AI模型，在第三方评测员进行的盲测中，与其他主要聊天机器人相比，配备Ultra 1.0 的 Gemini Advanced 是最受欢迎的AI聊天机器人。谷歌副总裁兼谷歌助手及Bard的总经理Sissie Hsiao表示，Gemini的改变是“构建一个真正的AI助手”的第一步。

谷歌还表示，Gemini Advanced还在不断改进，后续会上线附带扩展的多模态功能、更多的交互式编码功能、更深入的数据分析功能等。

支付AI订阅费用的谷歌One订阅者还将能够在Gmail、Docs、Sheets、Slides和Meet等Google Workspace平台中使用Gemini的助手功能，原来在Google Workspace中的AI助手Duet AI被终止，新AI助手将统称为Gemini for Workspace。谷歌云中使用的Duet AI也将更名为Gemini for Google Cloud。

谷歌希望能够将更多来自用户在Gmail、Docs和Drive中的内容的上下文融入Gemini。例如，如果你正在回复一个长邮件串，建议的回复将考虑到邮件串中较早消息的上下文，以及Google Drive中可能相关的文件。

* 资讯地址:

https://blog.google/products/gemini/bard-gemini-advanced-app/

![image](https://github.com/aitobox/newsweekly/assets/137874861/e9b116d6-4d8a-4bc3-9881-030b8c237533)


## AI服务和工具

#### 1. MetaVoice-1B：高度真实和自然的文本到语音（TTS）转换模型
  
开源支持商用的语音模型：模型有1.2亿个参数，经过了10万小时的语音数据训练。

* 专注英语情感演讲
* 跨语言语音克隆
* 支持美国和英国声音的零样本克隆
* 支持长篇内容语音合成

功能特点

1、情感语音节奏和音调：MetaVoice-1B专注于英语语音的情感表达，提供流畅、自然的语音输出，无幻觉现象。

2、跨语言语音克隆：支持通过微调实现跨语言的声音克隆。例如，对于印度说话者，仅需1分钟的训练数据即可实现成功克隆。

3、零样本克隆：对于美国和英国的声音，MetaVoice能够实现零样本克隆，只需30秒的参考音频即可。

4、长篇朗读支持：适用于长文本内容的语音合成。

体验地址:

模型下载：https://huggingface.co/metavoiceio/metavoice-1B-v0.1

GitHub：https://github.com/metavoiceio/metavoice-src

在线体验：https://ttsdemo.themetavoice.xyz

![image](https://github.com/aitobox/newsweekly/assets/137874861/a62bbc53-a1fc-4f72-9977-2092ba957233)

