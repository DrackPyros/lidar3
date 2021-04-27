# import time
import csv

# salir = False
# n_archivo = 'data.csv'
# myFile = open(n_archivo, 'w')

# while salir == False:
#     try:
#         with myFile:
#             writer = csv.writer(myFile)
#             # writer.writerows(myData)  
#         # print("Writing complete")  
#         salir = True
#     except IOError:
#         salir = False
#         open(n_archivo, 'x')
#     print(salir)





# print(time.time_ns())
# print(type(time.time_ns()))

n_archivo = 'data.csv'
myFile = open(n_archivo, 'w')
is_plot = True
x = [2, 4, 28, 65, 69]
string_ints = [str(int) for int in x]
str_of_ints = ",".join(string_ints)
n_vueltas = 0
# pipo = ', '.join(x)

def escribir():
    salir = False
    while salir == False:
        try:
            with open('data.csv', 'w') as pedro:
                # string = separator.join(x)
                pedro.write(str_of_ints)
                # spamwriter = csv.writer(n_archivo, delimiter=',')
                # for row in spamwriter:
                # spamwriter.writerow(pipo)
            salir = True
        except IOError:
            open(n_archivo, 'x')

escribir()
