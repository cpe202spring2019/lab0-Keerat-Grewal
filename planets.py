def weight_on_planets():
   # write your code here
   earth_weight = float(input("What do you weigh on earth? "))
   mars_weight = earth_weight * 0.38
   jupiter_weight = earth_weight * 2.34   
   print("\nOn Mars you would weigh {0:.2f} pounds.\nOn Jupiter you would weigh {1:.2f} pounds.".format(mars_weight, jupiter_weight))   
   
if __name__ == '__main__':
   weight_on_planets()
