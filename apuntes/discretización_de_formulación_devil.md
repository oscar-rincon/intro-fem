
# Discretización de la formulación devil del problema de valores en la frontera


La formulación fuerte del problema de valores en la frontera esta dado por:


$$
\begin{equation}
\sigma_{ij,j} + f_i = 0 \quad \forall \hspace{1mm} \mathbf{x} \in V, 
\end{equation}
$$

donde $\sigma_{i j}$ es el tensor de esfuersos, $f_{i}$ es el vector de fuerzas de cuerpo y $\mathbf{x}$ una coordenada espacial en el volumen $V$.


Aplicando el producto interno de la ecuación 1 con $w_{i}$ y la integral sobre el dominio $V$, tenemos que:

$$
\int_V \left( \sigma_{ij,j} + f_i \right)  w_{i} dV = 0 , 
$$

donde $w_{i}$ are the test funtions, which satisfy that:

$$
w_{i} = 0 \in S_u
$$

. Expandiendo los terminos en la integral 

$$
\int_V \sigma_{ij,j}   w_{i} dV + \int_V  f_i  w_{i} dV  = 0 , 
$$


aplicando el teorema de divergencia

$$
 -\int_V \sigma_{ij}w_{i,j} \ dV + \int_S \sigma_{ij}w_{i} n_{j} \ dS+ \int_V  f_i  w_{i} dV  = 0
$$