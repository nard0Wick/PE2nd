import openpyxl as opx 
import matplotlib.pyplot as plt  
import math

workbook = opx.load_workbook(filename="data.xlsx") 
sheet = workbook.active 
data_tuples = list(sheet.values)[1:]  
x_list = list(map(lambda x: x[0], data_tuples)) 
y_list = list(map(lambda x: x[1], data_tuples)) 

#working here! 
#searching m 
x_sum = sum(x_list) 
y_sum = sum(y_list) 
num_items = len(data_tuples) 

m = ( num_items * sum(list(map(lambda x: x[0]*x[1], data_tuples))) - x_sum * y_sum ) / (num_items * sum(list(map(lambda x : x**2, x_list))) - x_sum**2)  
theta = math.degrees(math.atan(m)) #need to convert from radiants to degrees 
b = ( y_sum - m * x_sum ) / num_items  

#now let's define the lower and higher points for the line that will cut the chart
x_line_points = [0, max(x_list)] 
y_line_points = list(map(lambda x: m * x + b, x_line_points)) 


#setting the title
plt.title("My chart")  
#setting the x label fo the chart
plt.xlabel("ml")  
#settign the y label for the chart
plt.ylabel("pH") 

#here is where the magic starts 
plt.scatter(x_list, y_list, label = "puntos", color = "purple")  
plt.plot(x_line_points, y_line_points, label = "transversal", color = "green") 
plt.legend(loc = 'best')
plt.show()


# plt.plot(data_tuples) 
# plt.show()

# print(list(data_tuples))