print("ЗАДАЧА: Найти наибольший курс доллара за день в течении года, используя данные за год из файла 'kursUSD.txt.'.\n"
      "А так же вывести некорректные значения из данного файла и даты"
      ", к которым относятся эти значения.")

input_file = open('kursUSD.txt', 'r')
max_dolr=1
max_data= " "
for line in input_file:
    date,d = map(str, line.split())
    try:
        dolr= float(d)
        if dolr > max_dolr:
            max_dolr=dolr
            max_data=date
    except ValueError:
        print("В", date, "некорректые значения")
print(max_data,max_dolr,"-наибольший курс за год")