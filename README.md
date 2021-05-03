# Предисловие
Задача из предпрофильного экзамена по Алгоритмическому программированию, 2020.
# Задача
Сапёр Пётр готовится к сдаче экзамена по обезвреживанию бомб. Среди
прочего, для успешной сдачи экзамена ему необходимо обезвредить модуль с
проводами. 
### Правила обезвреживания следующие:
• Модуль с проводами имеет от 3 до 6 проводов, с возможными цветами:
красный, синий, белый, жёлтый, чёрный.  
• Только один правильный провод необходимо перерезать для
обезвреживания модуля.  
• Нумерация проводов начинается с верхнего.  
##### 3 провода:
• Если нет чёрных проводов, режьте первый.  
• Иначе, если жёлтых проводов больше двух, режьте последний жёлтый.  
• Иначе, если последний синий или белый, режьте последний.  
• Иначе режьте второй.  
##### 4 провода:
• Если красных проводов больше, чем один, и последняя цифра серийного
номера нечетная, режьте последний красный.  
• Иначе, если последний провод желтый, а красных проводов нет, режьте
первый.  
• Иначе, если синий провод всего один, режьте первый.  
• Иначе, если желтых проводов больше, чем один, режьте последний.  
• Иначе режьте второй.  
##### 5 проводов:
• Если последний провод черный, и последняя цифра серийного номера
нечетная, режьте четвертый.  
• Иначе, если красный провод всего один, а желтых проводов больше, чем
один, режьте первый.  
• Иначе, если черных проводов нет, режьте второй.  
• Иначе режьте первый.  
##### 6 проводов:
• Если желтых проводов нет, и последняя цифра серийного номера
нечетная, режьте третий.  
• Иначе, если желтый провод всего один, а белых проводов больше, чем
один, режьте четвертый.  
• Иначе, если красных проводов нет, режьте последний.
• Иначе режьте четвертый.  
Помогите начинающему сапёру в подготовке к экзамену и напишите
программу, которая позволит ему тренироваться в решении данной задачи.
Предполагается, что интерфейс программы будет «консольным», тем не менее,
вы можете выбрать тот тип интерфейса, который будет удобнее вам.
Допускается использование английского языка в интерфейсе. Далее
перечислены требования, за каждое из которых начисляется 10 баллов при
полном выполнении.
