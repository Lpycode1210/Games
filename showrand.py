#十种颜色拼颜色带
# from PIL import Image, ImageDraw
# import random
#
# # 定义画布大小和颜色数量
# canvas_width = 1000  # 画布宽度
# canvas_height = 100  # 画布高度
# num_colors = 10      # 颜色数量
#
# # 生成随机颜色
# def generate_random_color():
#     return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#
# # 生成10种不同的颜色，确保相邻颜色不相同
# colors = []
# for _ in range(num_colors):
#     while True:
#         color = generate_random_color()
#         # 如果颜色列表为空，或者新颜色与上一个颜色不同，则添加到列表
#         if not colors or color != colors[-1]:
#             colors.append(color)
#             break
#
# # 计算每个颜色块的宽度
# block_width = canvas_width // num_colors
#
# # 创建一个空白画布
# image = Image.new("RGB", (canvas_width, canvas_height), "white")
# draw = ImageDraw.Draw(image)
#
# # 绘制颜色块
# for i, color in enumerate(colors):
#     left = i * block_width
#     right = (i + 1) * block_width
#     draw.rectangle([left, 0, right, canvas_height], fill=color)
#
# # 保存或显示图像
# image.show()  # 显示图像
# # image.save("color_blocks.png")  # 保存图像



#5种颜色拼出十个块的颜色带，相邻不相同
from PIL import Image, ImageDraw
import random

# 定义画布大小和颜色数量
canvas_width = 1000  # 画布宽度
canvas_height = 100  # 画布高度
num_unique_colors = 5  # 独特的颜色数量
num_blocks = 10        # 颜色块数量

# 生成随机颜色
def generate_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# 生成5种不同的颜色
unique_colors = []
while len(unique_colors) < num_unique_colors:
    color = generate_random_color()
    if color not in unique_colors:
        unique_colors.append(color)

# 生成10个颜色块，确保相邻颜色不相同
colors = []
for i in range(num_blocks):
    while True:
        # 从5种颜色中随机选择一个
        color = random.choice(unique_colors)
        # 如果颜色列表为空，或者新颜色与上一个颜色不同，则添加到列表
        if not colors or color != colors[-1]:
            colors.append(color)
            break

# 计算每个颜色块的宽度
block_width = canvas_width // num_blocks

# 创建一个空白画布
image = Image.new("RGB", (canvas_width, canvas_height), "white")
draw = ImageDraw.Draw(image)

# 绘制颜色块
for i, color in enumerate(colors):
    left = i * block_width
    right = (i + 1) * block_width
    draw.rectangle([left, 0, right, canvas_height], fill=color)

# 保存或显示图像
image.show()  # 显示图像
# image.save("color_blocks.png")  # 保存图像