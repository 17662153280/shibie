
---

# 评论识别模型

这是一个基于深度学习的情感分析模型，使用LSTM网络对IMDB电影评论数据集进行训练，实现评论的情感分类。项目中包括模型的训练、评估和使用示例，代码已托管在 GitHub 上。

## 目录

- [简介](#简介)
- [功能](#功能)
- [安装](#安装)
- [使用指南](#使用指南)
- [项目结构](#项目结构)
- [贡献](#贡献)
- [许可证](#许可证)
- [联系方式](#联系方式)

## 简介

本项目使用 TensorFlow 和 Keras 构建了一个基于LSTM的情感分析模型。模型使用IMDB数据集进行训练，能够对电影评论进行情感分类，判断评论是积极的还是消极的。

## 功能

- **训练模型**：使用IMDB数据集训练LSTM模型。
- **评估模型**：在测试数据上评估模型性能。
- **保存和加载模型**：保存训练好的模型，并在需要时加载它。
- **预测功能**：通过Web接口对输入的文本进行情感预测。

## 安装

### 必要的软件和库

确保你的系统上安装了以下软件和库：

- Python 3.x
- TensorFlow 2.x
- Keras
- NumPy

### 克隆项目

```bash
git clone https://github.com/17662153280/shibie.git
cd shibie
```


## 使用指南

### 训练模型

使用以下命令训练模型：

```bash
python test.py
```

模型将被保存为 `sentiment_analysis_model.h5`。



### 预测功能

#### 启动Flask应用

运行以下命令启动Flask应用：

```bash
python app.py
```

Web应用将运行在 `http://127.0.0.1:5000/`，你可以通过Web接口输入文本并获得情感预测。

### 示例命令

以下是一个示例命令，用于测试Flask应用的预测功能：

```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"text": "This movie was fantastic!"}'
```

## 项目结构

```
shibie/
│
├── test.py            # 模型训练脚本
├── app.py                    # Flask应用脚本
├── sentiment_analysis_model.h5 # 训练好的模型
├── README.md                 # 项目的 README 文件
├── static/
│   ├── style.css             # CSS 样式文件
├── templates/
│   └── index.html            # HTML 文件
└── LICENSE                   # 项目许可证

```

## 网页截图
以下是应用程序的界面截图：

![首页](shibie/shibie/screenshot/web.jpeg)


## 贡献

欢迎贡献代码、提出问题或进行改进。请遵循以下步骤：

1. Fork 这个项目。
2. 创建一个新的分支：`git checkout -b feature-branch`
3. 提交你的更改：`git commit -am 'Add new feature'`
4. 推送到分支：`git push origin feature-branch`
5. 提交 Pull Request

## 许可证

这个项目使用 [MIT 许可证](LICENSE) 进行许可。

## 联系方式

如有问题或建议，请通过以下方式联系我：

- **邮箱**：yaobing202402@sina.com
- **GitHub**：[@17662153280](https://github.com/17662153280)

---

