# 🦌 AI Partner 

[简体中文](#chinese)

---
<a name="english"></a>
A lightweight, customizable AI roleplay companion built with **Streamlit** and the **DeepSeek API** **(feel free to change to other models)**. Unlike many web-based AI chats, this project focuses on privacy by saving all your conversation history locally on your own machine.

<img width="2560" height="1262" alt="Image" src="https://github.com/user-attachments/assets/d5183c74-328e-456c-a35e-cacef617c7d6" />

## ✨ Features

  * **Custom Persona System**: Easily change the AI's name and personality traits directly from the sidebar.
  * **Persistent Local History**: Conversations are saved as `.json` files in a local `/sessions` folder.
  * **Session Management**: Create new chat sessions, switch between historical dialogues, or delete old ones.
  * **Roleplay Ready**: Pre-configured with a default *cat* persona to demonstrate the "Short & Sweet" chat style.
  * **Streaming UI**: Real-time response generation for a smooth "typing" experience.

## 🛠️ Environment & Prerequisites

  * **Python**: 3.8 or higher.
  * **API Key**: You will need a **DeepSeek API Key**.
      * Get one at: [platform.deepseek.com](https://platform.deepseek.com/)

### Dependencies

  * `streamlit`: For the web interface.
  * `openai`: To communicate with the DeepSeek API (using OpenAI-compatible SDK).

## 🚀 Getting Started

### 1\. Clone the repository

```bash
git clone https://github.com/your-username/ai-partner.git
cd ai-partner
```

### 2\. Install dependencies

```bash
pip install -r requirements.txt
```

### 3\. Set up your Environment File
1. Locate the `.env.example` file in the project folder.
2. Duplicate it and rename the copy to `.env`.
3. Open `.env` and paste your DeepSeek API key:

```bash
DEEPSEEK_API_KEY=your_real_key_here
```

### 4\. Run the application

```bash
streamlit run ai_partner.py
```

Once running, the app will automatically open in your default browser (usually at `http://localhost:8501`).

## 📁 Project Structure

  * `ai_partner.py`: The main application logic.
  * `/sessions`: (Auto-generated) Stores your chat history in JSON format.
  * `.env`: Stores private API keys (local use only).

## ⚙️ How to Use

1.  **Sidebar Configuration**: Enter the name and character traits of the person/character you want to talk to.
2.  **Chat**: Type in the chat box at the bottom. The AI will respond based on your defined personality rules.
3.  **Manage History**:
      * Click **"Create a new session"** to start fresh.
      * Click any file in the **"History Files"** list to reload a previous chat.
      * Click the **"❌"** next to a history file to delete it permanently.

---

# 🦌 AI 伙伴

[English](#english)

<a name="chinese"></a>

这是一个轻量级、可定制的 AI 角色扮演伴侣，基于 **Streamlit** 和 **DeepSeek API** 开发。与许多基于 Web 的 AI 聊天不同，本项目专注于隐私保护，所有对话历史都会本地保存。

<img width="2560" height="1262" alt="Image" src="https://github.com/user-attachments/assets/3db4a46e-8331-49cd-b56d-e43df6372877" />

## ✨ 功能特性

* **自定义人格系统**：直接在侧边栏修改 AI 的名称和性格特征，即刻生效。
* **本地持久化历史**：所有对话均以 `.json` 格式保存在本地 `/sessions` 文件夹中。
* **会话管理**：支持创建新会话、在历史对话间无缝切换，或永久删除旧记录。
* **角色扮演优化**：预配置了“可爱猫咪”角色示例，展示“简短精炼”的聊天风格。
* **流式响应 UI**：实时生成回复内容，提供流畅的“打字中”交互体验。
* **双语切换**：界面支持中英文一键切换。

## 🛠️ 环境与准备工作

* **Python**: 3.8 或更高版本。
* **API Key**: 你需要一个 **DeepSeek API Key**。
    * 获取地址：[platform.deepseek.com](https://platform.deepseek.com/)

### 依赖库
* `streamlit`: 用于构建网页交互界面。
* `openai`: 用于调用 DeepSeek API（兼容 OpenAI SDK）。

## 🚀 快速开始

### 1. 克隆仓库
```bash
git clone [https://github.com/your-username/ai-partner.git](https://github.com/your-username/ai-partner.git)
cd ai-partner
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置环境变量
1.  在项目根目录找到 `.env.example` 文件。
2.  复制该文件并重命名为 `.env`。
3.  打开 `.env` 文件，填入你的 DeepSeek API Key：

```bash
DEEPSEEK_API_KEY=你的实际密钥
```

### 4. 运行程序
```bash
streamlit run ai_partner.py
```
程序启动后，会自动在默认浏览器中打开应用（通常地址为 `http://localhost:8501`）。

## 📁 项目结构

* `ai_partner.py`: 主程序逻辑文件。
* `/sessions`: (自动生成) 用于存储 JSON 格式聊天记录的文件夹。
* `.env`: 存储私密 API 密钥（本地使用）。

## ⚙️ 使用说明

1.  **侧边栏配置**：在输入框中定义你想要互动的角色名称和性格细节。
2.  **聊天交互**：在底部的聊天框中输入内容，AI 将根据你定义的规则进行回复。
3.  **管理历史记录**：
    * 点击 **"新建对话会话" (Create a new session)** 开启一段新对话。
    * 点击 **"历史记录"** 列表中的文件名即可重新加载之前的聊天内容。
    * 点击文件名旁的 **"❌"** 按钮可永久删除该记录。
