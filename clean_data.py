# 读取原始文本文件
with open('data.txt', 'r') as f:
    original_text = f.read()

# 按行分割文本
lines = original_text.split('\n')

# 处理每一行文本
cleaned_lines = []
for line in lines:
    if line[-1] == ':' and line[0] == '\t':
        continue
    # 查找句号的位置
    dot_position = line.find('.')
    if dot_position != -1:
        # 去除句号及其后面的内容
        cleaned_line = line[:dot_position].strip()
        cleaned_lines.append(cleaned_line)
    else:
        cleaned_lines.append(line)

# 将处理后的文本保存到新文件
with open('cleaned_data.txt', 'w') as f:
    for line in cleaned_lines:
        f.write(line + '\n')

print("处理完成，结果已保存到cleaned_data.txt文件中。")
