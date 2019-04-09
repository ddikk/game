import pygame
from game_elf import *


pygame.init()

# 创建游戏窗口(480,700)
screen = pygame.display.set_mode((480,700))

# 绘制背景图像
# 1>加载图像数据
bg = pygame.image.load("./images/background.png")
# 2>blit 绘制图像
screen.blit(bg, (0,0))

# 绘制英雄飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(189,500))

# 3>update 更新到屏幕
pygame.display.update()

clock = pygame.time.Clock()

# 1.定义rect记录飞机起始位置
hero_rect = pygame.Rect(189,500,102,126)

# 创建敌方精灵
enemy1 = GameElf("./images/enemy1.png")
enemy2 = GameElf("./images/enemy1.png", 2)

# 创建敌方精灵族
enemy_group = pygame.sprite.Group(enemy1, enemy2)

# 游戏循环
while True:

	# 指定游戏循环内部执行频率
	clock.tick(60)

	# 捕获事件
	#event_list = pygame.event.get()
	#if len(event_list) > 0:
	#	print(event_list)

	for event in pygame.event.get():
		if event is not None:
		 	print(event)
		# 判断事件是不是退出
		if event.type == pygame.QUIT:
			print("游戏退出")

			# 结束程序调用quit卸载模块
			pygame.quit()

			# exit()
			exit()

	# 2.修改飞机位置
	hero_rect.y -= 1
	# # 判断飞机是否飞出屏幕
	if hero_rect.y == -126:
		hero_rect.y = 700

	# 3.调用blit方法绘制图像
	screen.blit(bg, (0,0))
	screen.blit(hero,hero_rect)

	# 精灵族调用update
	enemy_group.update()
	# 精灵族调用draw
	enemy_group.draw(screen)

	# 4.调用update方法更新屏幕显示
	pygame.display.update()

pygame.quit()
