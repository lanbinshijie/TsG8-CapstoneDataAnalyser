import base64
from datetime import datetime

# 定义评分表
score_table = {
    'a': [2,2,2,0,0,2,2,2,0,2,2,2,2,0,2,2,2,2,2,2], # 第一题选a得2分，选b得1分，选c和d各得0分
    'b': [0,0,0,2,2,0,0,0,2,0,0,0,0,2,0,1,1,2,1,0],  # 第一题选b得0分，选a得0分，选c得2分，选d得1分
    'c': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0],
    'd': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,2,1,0]
}

kp = True
while kp:
    # 获取用户输入的答案字符串
    answer = input("请输入20位答案字符串：")
    if answer == 'q':
        kp = False
        break

    # 检查答案字符串是否合法
    if len(answer) != 20 or not all(option in ['a', 'b', 'c', 'd'] for option in answer):
        print("答案字符串不合法，请重新输入！")
    else:
        # 计算问卷总分
        total_score = 0
        for i in range(len(answer)):
            option = answer[i]
            if i < 15 and option not in ['a', 'b']:
                print(f"第{i+1}题只能选择a或b，请重新作答！")
                break
            else:
                scores = score_table[option]
                score = scores[int(i/5)] # 每个问题有4个选项，共5个问题，因此每隔5个字符对应一个问题
            total_score += score

        name = input("请输入受试者姓名：")

        # 获取当前日期和时间
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 输入备注信息
        remark = input("请输入备注信息（如果没有备注可以直接回车）：")

        # 输出问卷总分
        print(f"问卷总分：{total_score}")

        # 输出当前问卷的分数
        current_score = sum(score_table[answer[i]][int(i/5)] for i in range(len(answer)))
        print(f"当前问卷的分数：{current_score}")

        # 输出当前问卷的支持程度
        progress = int(current_score / 2)
        print('当前问卷的支持程度：', end='')
        for i in range(progress):
            print('■', end='')
        for i in range(20 - progress):
            print('□', end='')
        print('')

        # 编码问卷信息成一串英文字母
        data_str = f"{answer}|{total_score}|{current_score}|{progress}|{name}|{timestamp}|{remark}"
        encoded_data = base64.b64encode(data_str.encode()).decode()
        print("问卷信息储存码："+encoded_data)
