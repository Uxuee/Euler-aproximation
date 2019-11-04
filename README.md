# Euler-aproximation

https://en.wikipedia.org/wiki/Euler_method

https://raw.githubusercontent.com/Uxuee/Euler-aproximation/blob/master/800px-Euler_method.svg.png

Se pueden resolver ED faciles usando la aproximación de Euler que es lo mismo que Taylor a primer orden. Por ejemplo si tienes una EDO de primer orden así:



Tonces con Taylor tienes que

alt text

Donde el tn es tu tiempo enésimo que es t0 + n * (delta t), con la condición inicial de y en t=0 puedes obtener y para todos los demás tiempos usando el algoritmo. El delta debería ser chiquito para que la aproximación de Taylor tenga sentido.

Así que primero programa el algoritmo y usalo para resolver

La ecuación de decaimiento
alt text
