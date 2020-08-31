



time = input("Введи кол-во секунд ")
time = int(time)

hour = time // 3600
min = (time - hour * 3600) // 60
sec = time - (hour * 3600 + min * 60)
print("Секунд: {} \nМинут: {} \nЧасов: {} ".format (sec, min, hour))
