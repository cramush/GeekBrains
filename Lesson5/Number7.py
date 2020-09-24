import json

with open("File7.1.txt") as file, open ("File7.2.txt", "w") as res:
    firm_dict = {}
    count = 0
    av_profit = 0
    for line in file:
        firm_list = line.split()
        profit = int(firm_list[2]) - int(firm_list[3])
        firm_dict[firm_list[0]] = profit
        if profit > 0:
            av_profit += profit
            count +=1
    av_profit /= count
    res_list = [firm_dict, {"Средняя прибыль: ": av_profit}]
    print(res_list)
    json.dump(res_list, res)
