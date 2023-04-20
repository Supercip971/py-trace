

# Intersection entre une droite et une sphère:

Soit un point $t$ et un vecteur $\vec{v}$ directeur d'une droite, avec une sphère d'origine $O$ et de rayon $r$:

Cela revient à faire une intersection avec une sphère d'origine $0$ et une droite d'origine $t'=t-O$.

![sphere](../../schema/Untitled-2023-04-20-1431.svg).


Ainsi, l'intersection de la droite à pour équation:

$$
\begin{align*}
    \begin{cases}
        x &= v_x*t + p'_x \\
        y &= v_y*t + p'_y \\
        z &= v_z*t + p'_z \\
    \end{cases}
\end{align*}
$$

Et la sphère a pour équation: $x^2+y^2+z^2=r^2$.

Ainsi, on cherches pour le paramètre $t$ de la droite:

$$
\begin{align*}

    &\begin{cases}
        x &= v_x*t + p'_x \\
        y &= v_y*t + p'_y \\
        z &= v_z*t + p'_z \\
        x^2+y^2+z^2&=r^2
    \end{cases}\\

\end{align*}
$$

$$
\begin{align*}

    r^2 &= x^2 + y^2 + z^2\\
    r^2 &= (\vec{v}_x*t + p'_x)^2 + (\vec{v}_y*t + p'_y)^2 + (\vec{v}_z*t + p'_z)^2\\
    r^2 &= (\vec{v}_x*t)^2 + (\vec{v}_y*t)^2 + (\vec{v}_z*t)^2 + 2(p'_x*\vec{v}_x *t + p'_y *\vec{v}_y*t + p'_z *\vec{v}_z *t) + (p'^2_z + p'^2_y + p'^2_z)\\
    r^2 &= (\vec{v}_x*t)^2 + (\vec{v}_y*t)^2 + (\vec{v}_z*t)^2 + 2t(p'_x*\vec{v}_x  + p'_y *\vec{v}_y + p'_z *\vec{v}_z ) + ||p||^2\\
    r^2 &= (\vec{v}_x*t)^2 + (\vec{v}_y*t)^2 + (\vec{v}_z*t)^2 + 2t(p' \cdot \vec{v} ) + ||p||^2\\
    r^2 &= \vec{v}_x^2*t^2 + \vec{v}_y^2*t^2 + \vec{v}_z^2*t^2 + 2t(p' \cdot \vec{v} ) + ||p||^2\\
    r^2 &= (\vec{v}_x^2 + \vec{v}_y^2 + \vec{v}_z^2)*t^2 + 2t(p' \cdot \vec{v} ) + ||p||^2 \\
    r^2 &= (||\vec{v}||^2)*t^2 + 2t(p' \cdot \vec{v} ) + ||p||^2 \\
    0 &= (||\vec{v}||^2)*t^2 + 2t(p' \cdot \vec{v} ) + ||p||^2 - r^2\\

\end{align*}
$$

Or, dans notre contexte, on sait que $||\vec{v}|| = 1$. Alors:

$$
\begin{align*}
    0 &= (||\vec{v}||^2)*t^2 + 2t(p' \cdot \vec{v} ) + ||p||^2 - r^2\\
    0 &= t^2 + 2t(p' \cdot \vec{v} ) + ||p||^2 - r^2\\
\end{align*}
$$
Ici on a une équation du second degré. Avec:

$$
\begin{align*}
    c &= ||p||^2-r^2\\
    b &= 2(p' \cdot \vec{v})\\
    a &= 1\\
    \Delta &= b^2 - 4ac \\
\end{align*}
$$
$$
\begin{align*}
\begin{cases}
    \text{Si } & \Delta < 0 \text{ alors il n'y a pas d'intersection}\\
    \text{Si } & \Delta \geq 0 \text{ alors: } t = \dfrac{-b \pm \sqrt{\Delta}}{2a} \\
\end{cases} \\
\end{align*}

$$

Ainsi, les deux intersections sont les points: $t_1$ et $t_2$ de la droite.