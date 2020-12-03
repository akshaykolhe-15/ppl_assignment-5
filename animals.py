class Animals:
    def __init__(self, legs=4, eyes=2):
        self.legs = legs
        self.eyes = eyes


class wild_animals(Animals):
    def place(self):
        print("place- Jungle")

class carnivores(wild_animals):
    def food(self):
        print("food- Meat")
    
        
class tiger(carnivores):
    def speak(self):
        print("voice- Roar")
    def colour(self):
        print("colour- Orange")
        
class lion(carnivores):
    def speak(self):
        print("voice- Roar")
    def colour(self):
        print("colour- Yellow")
        
class hyena(carnivores):
    def speak(self):
        print("voice- laugh")
    def colour(self):
        print("colour- Grey")


                        
class herbivores(wild_animals):
    def food(self):
        print("food- Plant based")

class deer(herbivores):
    def speak(self):
        print("voice- dummyvalue")
    def colour(self):
        print("colour- Brown")
        
class elephant(herbivores):
    def speak(self):
        print("voice- dummyvalue")
    def colour(self):
        print("colour- Grey")
        
class zebra(herbivores):
    def speak(self):
        print("voice- like a dog(bark)")
    def colour(self):
        print("colour- Black and white")




class domestic_animals(Animals):
    def place(self):
        print("place- Areas habitated by human beings")

        
class dog(domestic_animals):
    def speak(self):
        print("voice- bark")
    def colour(self):
        print("colours- brown,black,white,golden,etc.")
        
class cat(domestic_animals):
    def speak(self):
        print("voice- meow")
    def colour(self):
        print("colours- Grey,brown,black,white, etc.")
        
class cow(domestic_animals):
    def speak(self):
        print("voice- moo")
    def colour(self):
        print("colours- white,brown,etc.")
        
class goat(domestic_animals):
    def speak(self):
        print("voice- dummyvalue")
    def colour(self):
        print("colours- black,brown,white,etc.")

#p1=Animals()

print("class tiger : ")
Max1 = tiger()
Max1.place()
Max1.food()
Max1.speak()
Max1.colour()
print("number of eyes-",Max1.eyes)
print("number of legs-",Max1.legs)

print("\nclass lion : ")
Max2 = lion()
Max2.place()
Max2.food()
Max2.speak()
Max2.colour()
print("number of eyes-",Max2.eyes)
print("number of legs-",Max2.legs)

print("\nclass hyena : ")
Max3 = hyena()
Max3.place()
Max3.food()
Max3.speak()
Max3.colour()
print("number of eyes-",Max3.eyes)
print("number of legs-",Max3.legs)

print("\nclass deer : ")
Max4 = deer()
Max4.place()
Max4.food()
Max4.speak()
Max4.colour()
print("number of eyes-",Max4.eyes)
print("number of legs-",Max4.legs)

print("\nclass elephant : ")
Max5 = elephant()
Max5.place()
Max5.food()
Max5.speak()
Max5.colour()
print("number of eyes-",Max5.eyes)
print("number of legs-",Max5.legs)

print("\nclass zebra : ")
Max6 = zebra()
Max6.place()
Max6.food()
Max6.speak()
Max6.colour()
print("number of eyes-",Max6.eyes)
print("number of legs-",Max6.legs)

print("\nclass dog : ")
Max7 = dog()
Max7.place()
Max7.speak()
Max7.colour()
print("number of eyes-",Max7.eyes)
print("number of legs-",Max7.legs)

print("\nclass cat : ")
Max8 = cat()
Max8.place()
Max8.speak()
Max8.colour()
print("number of eyes-",Max8.eyes)
print("number of legs-",Max8.legs)

print("\nclass cow : ")
Max9 = cow()
Max9.place()
Max9.speak()
Max9.colour()
print("number of eyes-",Max9.eyes)
print("number of legs-",Max9.legs)

print("\nclass goat : ")
Max10 = goat()
Max10.place()
Max10.speak()
Max10.colour()
print("number of eyes-",Max10.eyes)
print("number of legs-",Max10.legs)




