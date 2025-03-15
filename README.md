# 🎭 EmotionWeb - 语音情感分析系统

![Python Version](https://img.shields.io/badge/Python-3.11-blue)
![Django Version](https://img.shields.io/badge/Django-4.2-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 项目简介

EmotionWeb 是一个基于网页的语音情感分析系统，它能够实时分析语音中蕴含的情感特征。无论是实时录音还是上传音频文件，系统都能快速准确地识别出说话者的情感状态。

### ✨ 主要特性

- 🎤 支持实时录音分析
- 📁 支持音频文件上传
- 📊 直观的情感分析结果展示
- 🚀 快速响应的Web界面
- 💻 跨平台兼容性

## 🛠️ 技术栈

- 前端：HTML5 + JavaScript + Bootstrap 5
- 后端：Python + Django
- AI模型：FunASR emotion2vec-plus-large
- 音频处理：Web Audio API

## 📦 安装部署

1. 克隆仓库
```bash
git clone https://github.com/ZamShi/EmotionWeb.git
cd EmotionWeb
 ```

2. 创建虚拟环境
```bash
python -m venv emotion_venv
emotion_venv\Scripts\activate
 ```

3. 安装依赖
```bash
pip install -r requirements.txt
 ```

4. 运行服务器
```bash
python manage.py runserver
 ```

## 🎯 使用方法
1. 访问 http://localhost:8000
2. 选择录音或上传音频文件
3. 等待分析结果
4. 查看情感分析详情
## ⚠️ 免责声明
- 本项目仅供学习和研究使用，不得用于商业目的
- 模型来源： FunASR emotion2vec-plus-large
- 使用本项目时请遵守相关法律法规和道德准则
- 不对使用本项目产生的任何后果承担责任
## 📝 模型声明
本项目使用的 emotion2vec-plus-large 模型由 FunASR 提供，遵循 Apache-2.0 license。使用该模型时请注意：

- 仅供研究和学习使用
- 需注明模型来源
- 不得用于商业用途
- 遵守模型原始许可证的所有条款
## 🤝 贡献指南
欢迎提交 Issue 和 Pull Request！

## 📄 开源协议
本项目采用 MIT 协议开源，但不包括其使用的模型。详见 LICENSE 文件。

## 🎉 致谢
- FunASR 提供的情感识别模型
- Django 框架
- Bootstrap 框架
⭐️ 如果这个项目对你有帮助，欢迎点个 star！