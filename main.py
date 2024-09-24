from pyannote.audio import Pipeline
from pydub import AudioSegment
import torch

input_file = "./input/1.mp3"

# 检查是否有可用的GPU,如果有则使用GPU,否则使用CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 初始化 pyannote.audio 管道
# 使用预训练的说话人分离模型
# 注意: 需要使用有效的Hugging Face访问令牌
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1",
                                    use_auth_token="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")

# 将管道移动到指定的设备(GPU或CPU)
pipeline = pipeline.to(device)

# 处理音频文件,进行说话人分离
diarization = pipeline(input_file)

# 使用pydub加载原始MP3音频文件
audio = AudioSegment.from_mp3(input_file)

# 为每个说话者创建一个空的字典,用于存储音频段
speaker_segments = {}

# 遍历分离结果
for turn, _, speaker in diarization.itertracks(yield_label=True):
    # 将时间转换为毫秒
    start_ms = int(turn.start * 1000)
    end_ms = int(turn.end * 1000)
    # 从原始音频中提取当前说话者的片段
    segment = audio[start_ms:end_ms]
    
    # 如果是新的说话者,创建新的条目;否则,将片段添加到现有的音频中
    if speaker not in speaker_segments:
        speaker_segments[speaker] = segment
    else:
        speaker_segments[speaker] += segment

# 导出每个说话者的音频
for i, (speaker, segment) in enumerate(speaker_segments.items(), 1):
    # 为每个说话者创建一个新的MP3文件
    output_file = f"./output/speaker_{i}.mp3"
    segment.export(output_file, format="mp3")
    print(f"已保存 {speaker} 的音频到 {output_file}")

# 完成提示
print("音频分离完成！")