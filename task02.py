# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

s = int(input('Введите общее количество журавликов:'))  

x = s // 6

k = (x+x)*2

print('Петя и Сережа сделали по -',x,'Катя сделала -',k)