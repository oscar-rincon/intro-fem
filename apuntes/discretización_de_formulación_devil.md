
# Discretización de la formulación devil del problema de valores en la frontera


La formulación fuerte del problema de valores en la frontera esta dado por:


$$
\begin{equation}
\sigma_{ij,j} + f_i = 0 \quad \forall \hspace{1mm} \mathbf{x} \in V, 
\end{equation}
$$

donde $\sigma_{i j}$ es el tensor de esfuersos, $f_{i}$ es el vector de fuerzas de cuerpo y $\mathbf{x}$ una coordenada espacial en el volumen $V$. Aplicando el producto interno de la ecuación 1 con $w_{i}$ y la integral sobre el dominio $V$, tenemos que:

$$
\begin{equation}
\int_V \left( \sigma_{ij,j} + f_i \right)  w_{i} dV = 0 , 
\end{equation}
$$

donde $w_{i}$ son las funciones de prueba o funciones de ponderación, que satisfacen:

$$
w_{i} = 0 \in S_u
$$

Expandiendo los terminos en la integral 

$$
\int_V \sigma_{ij,j}   w_{i} dV + \int_V  f_i  w_{i} dV  = 0 , 
$$

aplicando el teorema de divergencia

$$
 -\int_V \sigma_{ij}w_{i,j} \ dV + \int_S \sigma_{ij}w_{i} n_{j} \ dS+ \int_V  f_i  w_{i} dV  = 0
$$

De acuerdo a la ecuación 2 tenemos que:


$$
 -\int_V \sigma_{ij}w_{i,j} \ dV + \int_{S_{t}} \sigma_{ij}w_{i} n_{j} \ dS + \int_V  f_i  w_{i} dV  = 0
$$

Por definición del vector de tracciones tenemos que:

$$
\begin{equation}
t_{i}^{\hat{n}} = \sigma_{ij} \hat{n_{j}}
\end{equation}
$$

Entonces al reemplazar la ecuación 3 y multiplicar por -1:

$$
 \int_V \sigma_{ij}w_{i,j} \ dV - \int_{S_{t}} t_{i}^{\hat{n}} w_{i}  \ dS - \int_V  f_i  w_{i}  \ dV  = 0
$$

Aahora considerando que el dominio $V$ es dividido en un munero finito de subdominios $\Omega_e$. Entonces aplicando una sumatoria de los subdominios a la formulación devil, tenemos que:


$$
\sum_e \int_{\Omega_e} \sigma_{i j} w_{i, j} \mathrm{~d} \Omega_e-\sum_e \int_{\Omega_e} f_i w_i \mathrm{~d} \Omega_e-\sum_e \int_{S_e} t_i w_i \mathrm{~d} S_e=0
$$


Por definición tenemos que:

$$
\sigma_{i j}= C_{i j k l} \varepsilon_{k l}
$$

y que:

$$
\varepsilon_{i j}=\frac{1}{2}\left(u_{i, j}+u_{j, i}\right)
$$


Si asumimos que dentro de cada subdominio los desplazamientos $u_{i}$ y las funciones de ponderación $w_{i}$ se pueden aproximar con la función de forma:


$$
\begin{aligned} u_i(\vec{x}) & =N_i^Q(\vec{x}) \widehat{u}^Q \\ w_i(\vec{x}) & =N_i^Q(\vec{x}) \widehat{w}^Q\end{aligned}
$$