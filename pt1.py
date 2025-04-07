#def my_function(country = "Norway"):
  #print("I am from " + country)

#my_function("Sweden")
#my_function("India")
#my_function()
#my_function("Brazil")

#def printVoting(msg = "Current Result"):
    #print(msg)
    
#printVoting("Final Result")
#printVoting()

shoppinglist = []

class product:
    def __init__(self,ProductID,ProductName, Price): #constructor
       self.ProductID = ProductID
       self.ProductName = ProductName
       self.Price = Price  
    def __str__(self): # this function for printing object
        return(f' {self.ProductID} -- {self.ProductName} -- {self.Price}')
    
class ShoppingCart:
    def __init__(self):
        self.ProductList=[]
    def AddProduct(self,product):
        self.ProductList.append(product)
    def RemoveProduct(self,productID):
        for x in self.ProductList:
            if(x.ProductID == productID):
                self.ProductList.remove(x)
    def ListProduct(self):
        for x in self.ProductList:
            print(x)
# shopping cart object            
cart = ShoppingCart()
#adding product to the cart
cart.AddProduct(product(1,"Name1",2.3))
cart.AddProduct(product(2,"Name2",3.3))
cart.AddProduct(product(3,"Name3",4.3))
print("after adding")
#print all products in cart
cart.ListProduct()
#Remove product withID 1
cart.RemoveProduct(1)
print("after removing")
#print all products in cart
cart.ListProduct()
