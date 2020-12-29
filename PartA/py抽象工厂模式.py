
# 从模块中导入内容。
from abc import ABCMeta, abstractmethod

# 抽象类的方法。
class Shape(metaclass=ABCMeta):
	@abstractmethod
	def draw(self):
		pass

class Circle(Shape):
	def draw(self):
		print("draw a Circle method")

class Rectangle(Shape):
	def draw(self):
		print("draw a Rectangle method")

class Square(Shape):
	def draw(self):
		print("draw a Square method")

class Factory(object):
	def getShape(self,shapetype):

		if shapetype==None:
			print("什么玩意也不用画")

		elif shapetype.lower()=="circle":
			return Circle()

		elif shapetype.lower()=="rectangle":
			return Rectangle()

		elif shapetype.lower()=="square":
			return Square()
		return None


if __name__=="__main__":
	shapeFactory  = Factory()

	shape1 = shapeFactory.getShape("circle")
	shape1.draw()

	shape2 = shapeFactory.getShape("rectangle")
	shape2.draw()

	shape3 = shapeFactory.getShape("square")
	shape3.draw()





