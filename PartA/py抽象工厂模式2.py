
from abc import ABCMeta,abstractmethod

class Shape(metaclass=ABCMeta):
	@abstractmethod
	def draw(self):
		pass

class Rectangle(Shape):
	def draw(self):
		print("draw a  rectangle picture")

class Circle(Shape):
	def draw(self):
		print("draw a circle picture")

class Square(Shape):
	def draw(self):
		print("draw a square picture")

class Color(metaclass=ABCMeta):
	@abstractmethod
	def fill(self):
		pass

class Red(Color):
	def fill(self):
		print("inside color is red")

class Green(Color):
	def fill(self):
		print("inside color is green")

class Blue(Color):
	def fill(self):
		print("inside color is blue")


class AbstractFactory(metaclass= ABCMeta):
	@abstractmethod
	def getColor(self,color):
		pass
	@abstractmethod
	def getShape(self,shape):
		pass

class ShapeFactory(AbstractFactory):
	def getShape(self, shapeType):
		if shapeType==None:
			return None
		elif shapeType.lower()=="circle":
			return Circle()

		elif shapeType.lower()=="square":
			return Square()

		elif shapeType.lower()=="rectangle":
			return Rectangle() 
		return None

	def getColor(self, colorType):
		pass

class ColorFactory(AbstractFactory):
	def getShape(self,shapeType):
		pass

	def getColor(self, colorType):
		if colorType==None:
			return None
		elif colorType.lower()=="red":
			return Red()
		elif colorType.lower()=="blue":
			return Blue()
		elif colorType.lower()=="green":
			return Green()

		return None


class FactoryProducer(object):

	@staticmethod
	def getFactory(choiceType):
		if choiceType.lower()=="shape":
			return ShapeFactory()

		elif choiceType.lower()=="color":
			return ColorFactory()

		return None

if __name__=="__main__":
	shapeFactory = FactoryProducer.getFactory("Shape")

	Shape1 = shapeFactory.getShape("Circle") #
	Shape1.draw()

	Shape2 = shapeFactory.getShape("Square")
	Shape2.draw()

	Shape3 = shapeFactory.getShape("Rectangle")
	Shape3.draw()

	# 分割图形还是颜色的工厂模式。
	shapeFactory2 = FactoryProducer.getFactory("Color")
	color1 = shapeFactory2.getColor("blue")
	color1.fill()

	color2 = shapeFactory2.getColor("red")
	color2.fill()

	color3  = shapeFactory2.getColor("green")
	color3.fill()






