import pygame
from game_elf import *


class MainGame(object):
	"""主游戏"""
	def __init__(self):

		# 创建游戏窗口
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)

		# 创建游戏时钟
		self.clock = pygame.time.Clock()

		# 调用私有方法 创建精灵族
		self.__create_elf()

		# 设置定时器事件 创建敌人/1000ms
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
		# 设置定时器事件 创建射/200ms
		pygame.time.set_timer(SHOOT_FREQUENCY_EVENT,200)

	def __create_elf(self):

		# 创建背景精灵和精灵族
		bg1 = Background()
		bg2 = Background(True)

		self.background_group = pygame.sprite.Group(bg1,bg2)

		# 创建空的敌人精灵族
		self.enemies = pygame.sprite.Group()

		# 创建英雄精灵、精灵族
		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)

		self.bullets = pygame.sprite.Group()

	def start_game(self):
		
		while True:
			# 1.设置刷新率
			self.clock.tick(FRAME_PER_SEC)
			# 2.监听事件
			self.__event_handler()
			# 3.判断碰撞
			self.__check_collide()
			# 4.更新精灵
			self.__update_elf()
			# 5.绘制显示
			pygame.display.update()

	def __event_handler(self):

		for event in pygame.event.get():

			if event is not None:

				print(event)

				if event.type == pygame.QUIT: 

					MainGame.__game_over()

				elif event.type == CREATE_ENEMY_EVENT:

					# 1.创建敌人精灵
					enemy = Enemy()
					# 2.将敌人精灵加到敌人精灵族
					self.enemies.add(enemy)

			#if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			# 使用键盘模块获取按键元组
			keys_pressed = pygame.key.get_pressed()
			# 判断元组中对应的按键索引值
			if keys_pressed[pygame.K_RIGHT]:
				if keys_pressed[pygame.K_LEFT]:
					self.hero.x_speed = 0
				else:
					self.hero.x_speed = 2
				#print(pygame.K_RIGHT)
				#print(keys_pressed[pygame.K_RIGHT])
			else:
				if keys_pressed[pygame.K_LEFT]:
					self.hero.x_speed = -2
				else:
					self.hero.x_speed = 0
			if keys_pressed[pygame.K_UP]:
				if keys_pressed[pygame.K_DOWN]:
					self.hero.y_speed = 0
				else:
					self.hero.image = pygame.image.load("./images/me1.png")
					self.hero.y_speed = -2
			else:
				self.hero.image = pygame.image.load("./images/me2.png")
				if keys_pressed[pygame.K_DOWN]:
					self.hero.y_speed = 2
				else:
					self.hero.y_speed = 0
			if keys_pressed[pygame.K_a]:
				if event.type == SHOOT_FREQUENCY_EVENT:
					bullet = self.hero.fire()
					# 创建子弹精灵族
					self.bullets.add(bullet)
			
					

	def __check_collide(self):
		pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
		pygame.sprite.groupcollide(self.hero_group, self.enemies, True, True)
		

	def __update_elf(self):

		self.background_group.update()
		self.background_group.draw(self.screen)

		self.enemies.update()
		self.enemies.draw(self.screen)

		self.hero_group.update()
		self.hero_group.draw(self.screen)

		self.bullets.update()
		self.bullets.draw(self.screen)

	@staticmethod
	def __game_over():
		print("游戏结束")

		pygame.quit()
		exit()


if __name__ == '__main__':

	# 创建游戏对象
	game = MainGame()

	# 启动游戏
	game.start_game()