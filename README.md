# Предисловие
Задание из предпрофессионального экзамена по Алгоритмическому программированию, 2020.
# Задача
Сапёр Пётр готовится к сдаче экзамена по обезвреживанию бомб. Среди
прочего, для успешной сдачи экзамена ему необходимо обезвредить модуль с
проводами.  
  
Помогите начинающему сапёру в подготовке к экзамену и напишитеCancel changes
программу, которая позволит ему тренироваться в решении данной задачи.
Предполагается, что интерфейс программы будет «консольным», тем не менее,
вы можете выбрать тот тип интерфейса, который будет удобнее вам.
Допускается использование английского языка в интерфейсе.  

Правила обезвреживания следующие
> Модуль с проводами имеет от 3 до 6 проводов, с возможными цветами:
красный, синий, белый, жёлтый, чёрный.  
Только один правильный провод необходимо перерезать для
обезвреживания модуля.  
Нумерация проводов начинается с верхнего.  


| Количество проводов | Действия                                                                                                                                                                                                                                                                                                                                                                |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3 провода           | • Если нет чёрных проводов, режьте первый.  <br>• Иначе, если жёлтых проводов больше двух, режьте последний жёлтый.  <br>• Иначе, если последний синий или белый, режьте последний.  <br>• Иначе режьте второй.                                                                                                                                                         |
| 4 провода           | • Если красных проводов больше, чем один, и последняя цифра серийного<br>номера нечетная, режьте последний красный.  <br>• Иначе, если последний провод желтый, а красных проводов нет, режьте<br>первый.  <br>• Иначе, если синий провод всего один, режьте первый.  <br>• Иначе, если желтых проводов больше, чем один, режьте последний.  <br>• Иначе режьте второй. |
| 5 проводов          | • Если последний провод черный, и последняя цифра серийного номера<br>нечетная, режьте четвертый.  <br>• Иначе, если красный провод всего один, а желтых проводов больше, чем<br>один, режьте первый.  <br>• Иначе, если черных проводов нет, режьте второй.  <br>• Иначе режьте первый.                                                                                |
| 6 проводов          | • Если желтых проводов нет, и последняя цифра серийного номера<br>нечетная, режьте третий.  <br>• Иначе, если желтый провод всего один, а белых проводов больше, чем<br>один, режьте четвертый.  <br>• Иначе, если красных проводов нет, режьте последний.<br>• Иначе режьте четвертый.                                                                                 |

# Подзадачи
1. Программа должна выводить на экран серийный номер бомбы и
цвета проводов в модуле, при каждом запуске программы они должны
быть разными.  
2. Программа должна ждать ввода номера провода от пользователя и
сообщать ему корректный номер провода, если сапёр совершил ошибку.  
3. После решения модуля (верного или нет) программа должна
выдавать новое задание и продолжать тестирование сапёра.  
4. Программа должна выводить количество верно решённых заданий
подряд, а также процент верно решённых заданий за всё время работы
программы.  
5. Серийный номер должен быть длинной шесть символов, состоять
из заглавных согласных букв латинского алфавита и цифр вперемешку,
заканчиваясь при этом всегда на цифру.  
6. В программе должен быть способ узнать правильный ответ без
изменения статистики, например при вводе знака вопроса программа
будет сообщать правильный ответ, не учитывая это ни как правильный, ни
как неправильный ответ.  
7. Все выводимые на экран сообщения должны сопровождаться
пояснением выводимых данных (например, вывод серийного номера
должен сопровождаться надписью «Серийный номер: » или «Serial
number: » и так далее для всех данных), также при ожидании ввода от
пользователя должно быть сообщено обо всех корректных командах,
доступных пользователю или должно быть предложено ввести команду
для получения списка доступных команд.  
8. Если пользователь ввёл неверную команду, то программа должна
сообщить, что ввод некорректен, повторить сообщение о допустимых
командах и снова ждать ввод от пользователя.  
9. В программе должен быть способ сбросить статистику (количество
верно решённых подряд заданий и процент верно решённых заданий) без
закрытия и открытия программы, например при помощи ввода слова
“сбросить” или “reset”.  
10. В программе должна быть возможность сохранить текущую
статистику в файл с названием, которое вводит пользователь, например
при вводе команды «save file.txt» должен быть создан или перезаписан
файл с названием «file.txt». Должна быть возможность загрузить
статистику из файла и заменить ей текущую статистику, либо просто
посмотреть на статистику в файле, например при вводе команды «load
file.txt» текущая статистика должна быть заменена на статистику из файла
«file.txt», а при вводе «show file.txt» должна быть просто отображена на
экране.  
11. Данные, записываемые в файл сохранения статистики, должны
быть замаскированы таким образом, чтобы пользователю было сложно
подделать их так, чтобы программа при загрузке файла выдала
фальшивую статистику. Программа должна определять, корректны ли
данные в файле сохранения.  
12. При написании исходного кода придерживайтесь общих стандартов
к чистоте кода на вашем языке программирования. Соблюдайте отступы,
именуйте нужные переменные в соответствии с их предназначением.  
