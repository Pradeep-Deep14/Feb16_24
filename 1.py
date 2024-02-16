def find_hot_days(temps,threshold):
    return tuple(reading for reading in temps if reading[1]>threshold)

temps=(("Mon",72),("Tues",85),("Weds",89),("Thurs",78),("Fri",90),
       ("Sat",77),("Sun",84))
threshold=85
print(find_hot_days(temps,threshold))