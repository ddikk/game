import random
import pygame

# 定义矩形常量
SCREEN_RECT = pygame.Rect(0,0,480,700)
# 定义刷新率常量
FRAME_PER_SEC = 60
# 定义创建敌人事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 定义射事件常量
SHOOT_FREQUENCY_EVENT = pygame.USEREVENT + 1

class GameElf(pygame.sprite.Sprite):
	"""飞机大战游戏精灵"""
	def __init__(self,image_path,speed = 1):

		# 调用父类初始化方法
		super().__init__()
		# 定义对象属性
		# 定义对象数据属性
		self.image = pygame.image.load(image_path)
		# 定义对象位置属性
		self.rect = self.image.get_rect()
		# 定义对象速度属性
		self.speed = speed

	def update(self):

		# 在垂直方向移动
		self.rect.y += self.speed


class Background(GameElf):
	"""背景精灵"""
	def __init__(self, is_alt = False):
		
		#调用父类初始化方法
		super().__init__("./images/background.png")

		#判断是否为替换图像
		if is_alt:
			self.rect.y = -self.rect.height

	def update(self):

		super().update()
		
		if self.rect.y >= SCREEN_RECT.height:

			self.rect.y = -self.rect.height


class Enemy(GameElf):


	def __init__(self):

		# 1.调用父类，创建敌人，加载图片
		super().__init__("./images/enemy1.png")

		# 2.随机指定敌人初速度
		self.speed = random.randint(1,3)

		# 3.随机指定敌人初始位置
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)
		self.rect.bottom = 0
		

	def update(self):

		# 1.调用父类方法，保持垂直方向飞行
		super().update()
		# 2.判断飞出屏幕，从精灵族删除
		if self.rect.y >= SCREEN_RECT.height:
			self.kill()
		
	def __del__(self):
		print("销毁小飞机 %s" % self.rect)


class Hero(GameElf):
	"""英雄精灵"""

	def __init__(self):
		super().__init__("./images/me2.png")
		self.speed = 0
		self.x_speed = 0
		self.y_speed = 0
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120

	def update(self):

		# 在垂直方向移动
		self.rect.y += self.y_speed

		# 在水平方向移动
		self.rect.x += self.x_speed

		if self.rect.x <= 0:
			self.rect.x = 0
		elif self.rect.right >= SCREEN_RECT.width:
			self.rect.right = SCREEN_RECT.width
		if self.rect.y <= 0:
			self.rect.y = 0
		elif self.rect.bottom >= SCREEN_RECT.height:
			self.rect.bottom = SCREEN_RECT.height

	def fire(self):
		print("射了")
		bullet = Bullet()
		bullet.rect.centerx = self.rect.centerx
		bullet.rect.y = self.rect.y
		return bullet


class Bullet(GameElf):

	def __init__(self):
		super().__init__("./images/bullet1.png")
		self.speed = -2		

	def update(self):

		# 1.调用父类方法，保持垂直方向飞行
		super().update()
		# 2.判断飞出屏幕，从精灵族删除
		if self.rect.bottom <= 0:
			self.kill()
		
	def __del__(self):
		print("销毁子弹 %s" % self.rect)