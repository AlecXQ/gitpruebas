import math

# print ('Hola mundo')
# print ("hhhh")

# def saludo():
# 	print('funciona')

# saludo="hello it's me again"

# print(len(saludo))
	

# print(saludo.find("again"))

# print(saludo[2:3])

# print(3**5)

# num= 10
# num+=100

# print(num)

# print(round(2.7))

# print(pow(2,5))

# #nombre =input("Enter your first name")

# #print("Hello", nombre+ "! welcome")

# """num1= int(input("Enter a number"))
# num2= int(input("Enter a second number"))
# print(num1*num2,"Works!")"""

# numbers_try=[1,2,4,"just"]

# print(numbers_try[2:3])

# def sum_numbers(numero,numero2):
# 	return numero+numero2


# print(sum_numbers(5,3))

# #edad1= int(input("Ingrese la primera edad"))
# #edad2= int(input("Ingrese la segunda edad"))

# """if edad1<edad2:
# 	print("La persona 1 es menor que la persona 2")
# elif edad1>edad2:
# 	print("La persona 1 es mayor que la persona 2")
# else:
# 	print("La edad de las personas es la misma") """

# """index=1
# while index <= 7:
# 	print(index)
# 	index+=1 """

# # for index in range(5):
# # 	print(index)


class Ponente:
	def __init__(self,nombre,mensaje):
		self.nombre=nombre
		self.mensaje=mensaje


	"""@property
	def nombre(self):
		return self._nombre
	
	@nombre.setter
	def nombre(self,value):
		print("Setting title")
		self

	def imprimir(self):
		print("hello prueba")
	"""	

	def exponerju(self):
		print("El ponente es: ", self.nombre,"con su tema: " ,self.mensaje)
		#self.imprimir()

prueba = Ponente("Dokird","Sueños cuanticos.")

prueba.exponerju()


#vamos a probar git quizas para ver de nuevo