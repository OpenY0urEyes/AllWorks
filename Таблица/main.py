
with open('schedule.csv', 'r', encoding='utf-8') as f:
    data = f.read()

new = data.split(",")

with open("result.txt", "w", encoding="utf-8") as res:
    for i in new:
        res.write(i + " ")

with open('result.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()


data = [line.strip() for line in data if line.strip()]

with open('result.txt', 'w', encoding='utf-8') as f:
    for line in data:
        f.write(line + '\n')

with open('result.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

with open('result.txt', 'w', encoding='utf-8') as f:
    for line in data:
        if line.startswith('"Предмет  вид занятия" Ауд.'):
            continue
        f.write(line)

with open('result.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

with open('result.txt', 'w', encoding='utf-8') as f:
    for line in data:
        new_line = line.replace("402", "(402)").replace("133", "(133)").replace("312", "(312)").replace("318", "(318)").replace("319", "(319)").replace("323", "(323)").replace("407", "(407)").replace("411", "(411)").replace("418", "(418)").replace("419", "(419)").replace("422", "").replace("2.Иностранный язык", "").replace("132", "(132)").replace("-", "(-)")
        f.write(new_line)


with open('result.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

with open('result.txt', 'w', encoding='utf-8') as f:
    for line in data:
        new_line = line.replace("1.Иностранный язык (407)", "Иностранный язык(407/422)")
        f.write(new_line)

with open('result.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()


data = [line.strip() for line in data if line.strip()]

with open('result.txt', 'w', encoding='utf-8') as f:
    for line in data:
        f.write(line + '\n')








