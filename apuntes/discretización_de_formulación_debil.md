
# Discretización de la formulación debil del problema de valores en la frontera


La formulación fuerte del problema de valores en la frontera esta dado por:


$$
\begin{equation}
\sigma_{ij,j} + f_i = 0 \quad \forall \hspace{1mm} \mathbf{x} \in V, 
\end{equation}
$$

donde $\sigma_{i j}$ es el tensor de esfuersos, $f_{i}$ es el vector de fuerzas de cuerpo y $\mathbf{x}$ una coordenada espacial en el volumen $V$. Al multiplicar la ecuación 1 por $w_{i}$ y luego integrar sobre el dominio $V$, obtenemos:

$$
\begin{equation}
\int_V \left( \sigma_{ij,j} + f_i \right)  w_{i} dV = 0 , 
\end{equation}
$$

donde $w_{i}$ son las funciones de prueba o funciones de ponderación, que satisfacen:

$$
\begin{equation}
w_{i} = 0 \in S_u
\end{equation}
$$

donde $S_t \cup S_u=S$ y $S_t \cap S_u=\emptyset$.

Expandiendo los terminos en la integral 

$$
\int_V \sigma_{ij,j}   w_{i} dV + \int_V  f_i  w_{i} dV  = 0 , 
$$

aplicando el teorema de divergencia

$$
 -\int_V \sigma_{ij}w_{i,j} \ dV + \int_S \sigma_{ij}w_{i} n_{j} \ dS+ \int_V  f_i  w_{i} dV  = 0
$$

De acuerdo a la ecuación 3 tenemos que:


$$
 -\int_V \sigma_{ij}w_{i,j} \ dV + \int_{S_{t}} \sigma_{ij}w_{i} n_{j} \ dS + \int_V  f_i  w_{i} dV  = 0
$$

Por la definición del vector de tracciones tenemos que:

$$
\begin{equation}
t_{i}^{\hat{n}} = \sigma_{ij} \hat{n_{j}}
\end{equation}
$$

Entonces al reemplazar la ecuación 4:

$$
 \int_V \sigma_{ij}w_{i,j} \ dV - \int_{S_{t}} t_{i}^{\hat{n}} w_{i}  \ dS - \int_V  f_i  w_{i}  \ dV  = 0
$$

Ahora considerando que el dominio $V$ es dividido en un número finito de subdominios $\Omega_e$. Entonces aplicando una sumatoria de los subdominios a la formulación devil, tenemos que:


$$
\begin{equation}
\sum_e \int_{\Omega_e} \sigma_{i j} w_{i, j} \mathrm{~d} \Omega_e-\sum_e \int_{\Omega_e} f_i w_i \mathrm{~d} \Omega_e-\sum_e \int_{S_e} t_i w_i \mathrm{~d} S_e=0
\end{equation}
$$



Por definición del tensor de deformaciones tenemos que:

$$
\begin{equation}
\varepsilon_{i j}=\frac{1}{2}\left(u_{i, j}+u_{j, i}\right)
\end{equation}
$$


Si asumimos que dentro de cada subdominio los desplazamientos $u_{i}$ y las funciones de ponderación $w_{i}$ se pueden aproximar con:

<!-- $$
%\begin{aligned} u_i(\vec{x}) & =N_i^Q(\vec{x}) \widehat{u}^Q \\ w_i(\vec{x}) & =N_i^Q(\vec{x}) \widehat{w}^Q\end{aligned}
$$ -->

$$
u_i(\vec{x}) = N_i^Q(\vec{x}) \widehat{u}^Q
$$

donde $N_i^Q(\vec{x})$ es la función de forma y $\widehat{u}^Q$ el componente escalar de $u_i(\vec{x})$ en el nodo $Q$. Entonces:

$$
\begin{equation}
u_{i,j}(\vec{x}) = \frac{\partial u_{i}(\vec{x})}{\partial x_j}  = \frac{\partial N_i^Q(\vec{x})}{\partial x_{j}} \widehat{u}^Q = N_{i,j}^Q(\vec{x})\widehat{u}^Q 
\end{equation}
$$

y


$$
\begin{equation}
u_{j,i}(\vec{x}) = \frac{\partial u_{j}(\vec{x})}{\partial x_i}  = \frac{\partial N_j^Q(\vec{x})}{\partial x_{i}} \widehat{u}^Q = N_{j,i}^Q(\vec{x})\widehat{u}^Q 
\end{equation}
$$

Reemplazando 7 y 8 en 6:


$$
\varepsilon_{i j} = \frac{1}{2} \left( N_{i,j}^Q(\vec{x})\widehat{u}^Q  + N_{j,i}^Q(\vec{x})\widehat{u}^Q  \right) = \frac{1}{2} \left( N_{i,j}^Q(\vec{x})  + N_{j,i}^Q(\vec{x}) \right) \widehat{u}^Q 
$$

y si

$$
B_{ij}^{Q}(\vec{x})  = \frac{1}{2} \left( N_{i,j}^Q(\vec{x})  + N_{j,i}^Q(\vec{x}) \right) 
$$

Entonces

$$
\begin{equation}
\varepsilon_{i j} = B_{ij}^{Q}(\vec{x})   \widehat{u}^Q 
\end{equation}
$$

Por definición tenemos que:

$$
\begin{equation}
\sigma_{i j}= C_{i j k l} \varepsilon_{k l}
\end{equation}
$$

Reemplazando la ecuación 9 en la 10:


$$
\begin{equation}
\sigma_{i j}= C_{i j k l} B_{kl}^{Q}(\vec{x})   \widehat{u}^Q 
\end{equation}
$$

De manera similar la para la función de prueba $w_{i}$ tenemos que:

$$
\begin{equation}
w_i(\vec{x}) = N_i^Q(\vec{x}) \widehat{w}^Q
\end{equation}
$$

y

$$
\begin{equation}
w_{i,j}(\vec{x}) = \frac{\partial w_{i}(\vec{x})}{\partial x_j}  = \frac{\partial N_i^Q(\vec{x})}{\partial x_{j}} \widehat{w}^Q = N_{i,j}^Q(\vec{x})\widehat{w}^Q 
\end{equation}
$$

Para un solo elemento del dominio $V$ tenemos que:

$$
\begin{equation}
 \int_{\Omega_e} \sigma_{i j} w_{i, j} \mathrm{~d} \Omega_e-  \int_{\Omega_e} f_i w_i \mathrm{~d} \Omega_e-  \int_{S_e} t_i w_i \mathrm{~d} S_e=0
\end{equation}
$$

Reemplazando 11, 12 y 13 en 14:

$$
\begin{equation}
 \widehat{u}^Q \widehat{w}^P \int_{\Omega_e} C_{i j k l} B_{kl}^{Q}(\vec{x}) N_{i,j}^P(\vec{x}) \mathrm{~d} \Omega_e-  \widehat{w}^P  \int_{\Omega_e} f_i N_i^P(\vec{x}) \mathrm{~d} \Omega_e-   \widehat{w}^P \int_{S_e} t_i N_i^P(\vec{x}) \mathrm{~d} S_e=0
\end{equation}
$$

ahora cancelamos el termino comun $\widehat{w}^{P}$:

$$
\begin{equation}
 \widehat{u}^Q \int_{\Omega_e} C_{i j k l} B_{kl}^{Q}(\vec{x}) N_{i,j}^P(\vec{x}) \mathrm{~d} \Omega_e =  \int_{\Omega_e} f_i N_i^P(\vec{x}) \mathrm{~d} \Omega_e + \int_{S_e} t_i N_i^P(\vec{x}) \mathrm{~d} S_e
\end{equation}
$$