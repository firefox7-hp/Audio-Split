# 说话人音频分离工具

这个项目是一个Python脚本,用于将包含多个说话人的单个音频文件分离成多个单独的音频文件,每个文件包含一个说话人的声音。

## 功能

- 使用高级的说话人分离技术处理音频文件
- 支持MP3格式的输入文件
- 自动检测并使用GPU加速(如果可用)
- 为每个检测到的说话人生成单独的MP3文件

## 安装

1. 克隆此仓库:
   ```bash
   git clone https://github.com/你的用户名/说话人音频分离工具.git
   cd 说话人音频分离工具
   ```

2. 创建并激活虚拟环境(可选但推荐):
   ```bash
   python -m venv venv
   source venv/bin/activate  # 在Windows上使用 venv\Scripts\activate
   ```

3. 安装所需的依赖:
   ```bash
   pip install pyannote.audio pydub torch
   ```

## 使用方法

1. 将您要处理的MP3文件重命名为`1.mp3`并放在项目根目录中。

2. 在[Hugging Face](https://huggingface.co/)上注册并获取访问令牌。

3. 在`main.py`文件中,将`use_auth_token`的值替换为您的Hugging Face访问令牌:
   ```python
   pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1",
                                       use_auth_token="你的访问令牌")
   ```

4. 运行脚本:
   ```bash
   python main.py
   ```

5. 脚本执行完成后,您将在同一目录下看到生成的`speaker_1.mp3`、`speaker_2.mp3`等文件,每个文件包含一个说话人的音频。

## 注意事项

- 处理大型音频文件可能需要较长时间。
- 确保您有足够的磁盘空间来存储生成的音频文件。
- 该脚本使用了预训练的模型,结果的准确性可能因音频质量和说话人特征而异。

## 许可证

本项目采用MIT许可证。详情请见[LICENSE](LICENSE)文件。

## 贡献

欢迎提交问题报告和拉取请求。对于重大更改,请先开issue讨论您想要改变的内容。

## 致谢

本项目使用了[pyannote.audio](https://github.com/pyannote/pyannote-audio)库进行说话人分离。感谢其开发者的贡献。