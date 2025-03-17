import random


def guess_number_game():
    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个1到100之间的数字，你能猜到它是什么吗？")

    # 随机生成一个1到100之间的数字
    target_number = random.randint(1, 100)
    attempts = 0  # 记录玩家尝试的次数

    while True:
        try:
            # 获取玩家的猜测
            guess = int(input("请输入你的猜测（1-100）："))
            attempts += 1  # 每次猜测次数加1

            # 判断玩家的猜测
            if guess < 1 or guess > 100:
                print("输入的数字超出范围，请输入1到100之间的数字！")
            elif guess < target_number:
                print("太小了！再试一次。")
            elif guess > target_number:
                print("太大了！再试一次。")
            else:
                print(f"恭喜你！你猜对了！数字就是{target_number}！")
                print(f"你总共尝试了{attempts}次。")
                break  # 猜对了，退出循环
        except ValueError:
            print("请输入一个有效的整数！")

    print("游戏结束，感谢你的参与！")


# 运行游戏
if __name__ == "__main__":
    guess_number_game()