f = open("./input.txt", 'r')
lines = f.readlines()
f.close()

result_list = ""

for line in lines:
    text = line
    text = text.replace('\n', "<br>") # 줄바꿈 치환
    text = text.replace(' ', "&nbsp;") # 공백 치환
    text = text.replace('"', "&quot;") # 큰 따옴표 치환
    text = text.replace('\'', "&apos;") # 작은 따옴표 치환
    result_list += text

f = open("./output.txt", 'w')
f.write(result_list)
f.close()