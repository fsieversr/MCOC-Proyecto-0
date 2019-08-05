# MCOC-Proyecto-0
## Introducción

En este proyecto se mostrará en un ejemplo la pérdida de significancia. Este término describe básicamente la inexactitud que se produce cuando el computador trabaja con números muy grandes o muy pequeños, en esos casos solo toma hasta un cierto número de décimales finitos, dependiendo si son 32 o 64 bit. 

##Ejemplo

En este caso, ocuparemos el número de Avogrado, muy conocido en química, para ilustrar la pérdida de significancia. 
Este número es muy ocupado para calcular la masa de un átomo o molécula. El número de Avogrado se ocupa generalmente como *6,023x10^23*, se puede observar que es un número muy grande y la masa de un átomo es claramente muy pequeña, por lo que es muy útil para ejemplificar la pérdida de significancia. 

Tomaremos el número de Avogrado descrito anteriormente, el cuál es usado comunmente para los cálculos y el número más exacto *6.022140857x10^23* para trabajarlo con 32 y 64 bit. 

Se ocuparon los siguientes valores de gramos por mol de algunos átomos y moléculas:
Agua:18
Acido Sulfurico: 98
Azufre: 32
Cloruro de Sodio: 58
Nitrato de Plata:170
Acido Fosforico: 98 
Metano: 16 
Etano:30 
Alcohol Etilico: 46 
Cloruro Mercuroso: 235
Cianuro de Potasio: 65 
Propano: 44

Dividiendo esos valores por el número de Avogrado se obtiene la masa en gramos del elemento.
Para demostrar la pérdida de significancia se divide por el número que usamos comúnmente, por el de 32 bit y por último el de 64 bit.
Después se procede a calcular el error relativo de la siguiente forma: 

Error relativo = (Valor calculado - Valor real)/Valor real

Donde el valor real, será obtenido con el número de Avogrado usado comúnmente y el valor calculado será el con 32 y 64 bit.

Una vez hecho el cálculo se obtienen los siguientes resultados:

Error float 32	      Error float 64	      Diferencia (32bit-64bit)
0,000142634923801381	0,000142664049280817	-2,91255E-08
0,000142663595495046	0,000142664049280847	-4,53786E-10
0,000142660746134251	0,000142664049280932	-3,30315E-09
0,000142698883733404	0,000142664049280994	3,48345E-08
0,000142645722231555	0,000142664049280897	-1,8327E-08
0,000142680982411280	0,000142664049280907	1,69331E-08
0,000142674518044958	0,000142664049280915	1,04688E-08
0,000142674518044997	0,000142664049280876	1,04688E-08
0,000142634923801381	0,000142664049280817	-2,91255E-08
0,000142651603929602	0,000142664049280873	-1,24454E-08
0,000142680982411280	0,000142664049280907	1,69331E-08
0,000142678244562014	0,000142664049280827	1,41953E-08


De estos se puede observar que la mayoría el error mayor es el que con 64 bit, es decir ocupando más decimales (diferencia negativa)
