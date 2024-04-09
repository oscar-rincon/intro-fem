
Considere una función $f(x)$ cuyos valores son conocidos en $x_1, x_2, \ldots, x_n$. Sin embargo se requiere concocer el valor de $f(x)$ en algun punto en $x \in\left[x_1, x_n\right]$ diferente a alguno de los $n$ puntos.

Este proceso envuelve 2 pasos:

1. Ajustar una función aproximada, conocida como interpolación polinomial.
2. Evaular la función en el punto de interes donde la función es conocida.


Para ajustar la función se utiliza el [teorema de interpolación de Lagrange](https://www.youtube.com/watch?v=nvkX1Bd90Gk) el cual afirma que:


Dados un conjunto de puntos $\left\{\left(x^1, y^1\right), \cdots,\left(x^n, y^n\right)\right\}$ donde $y^n \equiv f\left(x^n\right)$. Entonces existe un unico polinomio $p(x)$ of order at most $(n-1)$ donde  $p\left(x^I\right)=f\left(x^I\right)$ para $I=1,2, \cdots, n "$. Este polinomio esta dado por:

$$
p(x)=L^1(x) f\left(x^1\right)+L^2(x) f\left(x^2\right)+\ldots+L^n(x) f\left(x^n\right)
$$
 
y el termino $L^I(x)$ es expresado como:

$$
L^I(x)=\prod_{\substack{J=1 \\ I \neq J}}^n \frac{\left(x-x^J\right)}{\left(x^I-x^J\right)} .
$$

[Un pequeño ejemplo de interpolación de Lagrange](https://github.com/oscar-rincon/intro-fem/tree/main/programas).


Para satisfacer que $p\left(x^I\right)=f\left(x^I\right)$ el polinomio de interpolación debe cumplir que:


$$
L^I\left(x^J\right)=\delta^{I J}
$$

En notación indicial 

$$
f(x) \approx p(x) = L^Q(x) f(x^Q) = L^Q(x) f^Q
$$

Que es la función de interpolación de Lagrange. En dos dimensiones:

$$
f(x,y) \approx p(x,y) = N^Q(x,y) f^Q
$$

que es la función de forma para dos variables. Tambien para el caso de un vector de posición $\vec{r}$:

$$
F(\vec{r})=N^Q(\vec{r}) f^Q 
$$

