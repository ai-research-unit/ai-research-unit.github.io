# __Rational-Chart Polar Decomposition of Reduced Biquaternions__

## Introduction

The modulus–unit polar decomposition of *Modulus–Unit Polar Decomposition of Reduced Biquaternions* writes every unit as

$$
\breve Q=\breve r\,u,\qquad \breve r\in P,\qquad u\bar u=1,
$$

with $\breve r$ the modulus in the positive cone $P=\{x+jy:x>|y|\}$ and $u$ the unit factor on the torus $T^2=\{u:u\bar u=1\}$. That article proves the pair unique and treats $u$ as a point of the torus. It chooses no coordinate on the torus: the unit factor is named by the equation $u\bar u=1$, not by a pair of numbers.

This article names it. For real numbers $s_1,s_2$ put

$$
c(s)=\frac{1-is}{1+is},
$$

and let $u(s_1,s_2)$ be the unit whose two circular components are $c(s_1)$ and $c(s_2)$:

$$
u(s_1,s_2)=\frac{c(s_1)+c(s_2)}{2}+j\,\frac{c(s_1)-c(s_2)}{2}.
$$

Nothing in the decomposition changes. The modulus is still $\breve r$, the element $u=u(s_1,s_2)$ is still the same unit factor, and the pair $(\breve r,u)$ is still unique. The only new object is the pair of real numbers $(s_1,s_2)$, which replaces the point of the torus by a point of the plane.

The chart is rational: $c(s)$ and its inverse are ratios of polynomials, and no transcendental function occurs. The price is locality, and the locality is doubled. As $\lvert s\rvert$ grows the unit $c(s)$ approaches $-1$ without attaining it, so the chart on one circle misses the point $-1$. On the torus the chart misses the union of the two circles on which one circular component equals $-1$. The rational-chart decomposition therefore holds on the complement of two walls and fails on them. Four charts, obtained by multiplying the unit factor by $1,j,-1,-j$, cover the torus.

The plan is as follows. The modulus–unit form is recalled (§*The Modulus–Unit Form Recalled*), the chart and its inverse are defined (§*The Chart*, §*The Inverse*), and the chart is proved a bijection (§*The Bijection*). The decomposition is then stated and proved (§*The Rational-Chart Decomposition*), the group law in the coordinates is computed (§*The Group Law*), the covering of the torus and the cost of rationality are described (§*Covering the Torus and the Price of Locality*), and the matrix picture (§*The Matrix Picture*) and worked examples (§*Worked Examples*) close the article.

The symbols are those of *Modulus–Unit Polar Decomposition of Reduced Biquaternions*. The notation is collected in §*Summary of Notation*.

Every numerical value displayed below was recomputed in double precision.

## The Unit Factor and Its Chart

### The Modulus–Unit Form Recalled

For a reduced biquaternion $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ the bar is $\bar{\breve Q}=\bar Q_{\blacktriangle}+j\bar Q_{\blacktriangledown}$, and the product

$$
\breve Q\bar{\breve Q}=\bigl(|Q_{\blacktriangle}|^2+|Q_{\blacktriangledown}|^2\bigr)+2j\operatorname{Re}(Q_{\blacktriangle}\bar Q_{\blacktriangledown})
$$

lies in the cone $P$ exactly when $\breve Q$ is a unit. The modulus is the positive square root $\breve r=\sqrt{\breve Q\bar{\breve Q}}$ in $P$, an element of $P$ fixed by the bar, and the unit factor is

$$
u=\breve r^{-1}\breve Q,\qquad u\bar u=1.
$$

The two scales of the modulus are

$$
\rho_+=|Q_{+}|>0,\qquad \rho_-=|Q_{-}|>0,
$$

and the two circular components of the unit factor are

$$
u_+=\frac{Q_{+}}{\rho_+},\qquad u_-=\frac{Q_{-}}{\rho_-}.
$$

Each is a unit complex number. The pair $(\breve r,u)$ is unique: taking the bar forces $\breve r^2=\breve Q\bar{\breve Q}$, the cone fixes the square root, and then $u=\breve r^{-1}\breve Q$.

This is where the modulus–unit article stops. The present article adds two real numbers, $s_1$ and $s_2$, one for each circular component, and changes nothing else.

### The Chart

**Definition.** For $s\in\mathbb{R}$ the **circle chart** is

$$
c(s)=\frac{1-is}{1+is}=\frac{1-s^2}{1+s^2}-i\,\frac{2s}{1+s^2}.
$$

The real and imaginary parts are rational functions of $s$, and their squares sum to one:

$$
\left(\frac{1-s^2}{1+s^2}\right)^2+\left(\frac{2s}{1+s^2}\right)^2
=\frac{(1-s^2)^2+4s^2}{(1+s^2)^2}
=\frac{(1+s^2)^2}{(1+s^2)^2}=1.
$$

Every $c(s)$ is therefore a point of the unit circle, and the denominator $1+is$ never vanishes. Three values fix the orientation:

$$
c(0)=1,\qquad c(1)=\frac{1-i}{1+i}=-i,\qquad c(-1)=\frac{1+i}{1-i}=i.
$$

The circle chart almost covers the circle, but not quite. If $c(s)=-1$ then $1-is=-1-is$, hence $1=-1$, which is impossible; so $-1$ is not attained. As $\lvert s\rvert$ grows without bound,

$$
c(s)=\frac{1-s^2-2is}{1+s^2}=-1-\frac{2is}{1+s^2}+\frac{2}{1+s^2}\longrightarrow-1,
$$

so $-1$ is the limit of the chart at both ends of the line.

Geometrically, the line through $-1$ and $c(s)$ meets the imaginary axis at $-is$, so the circle chart is the stereographic projection of the circle from $-1$ onto that axis, followed by the identification $-is\leftrightarrow s$.

**Definition (the torus chart).** For $(s_1,s_2)\in\mathbb{R}^2$ the **torus chart** is the unit $u(s_1,s_2)$ whose circular components are $c(s_1)$ and $c(s_2)$:

$$
u(s_1,s_2)=\frac{c(s_1)+c(s_2)}{2}+j\,\frac{c(s_1)-c(s_2)}{2}.
$$

The definition is consistent because an element of the torus is determined by its two circular components. The element is a unit factor: its components have modulus one, so $u\bar u=1$.

The chart misses the set on which one circular component equals $-1$:

$$
M=\{\,u:u_+=-1\,\}\cup\{\,u:u_-=-1\,\},
$$

the union of two circles in $T^2$, each a copy of $S^1$. On the complement the chart is a coordinate, and the coordinate is rational in the components.

### The Inverse

**Proposition.** Let $u\in T^2$ with $u_+\neq-1$ and $u_-\neq-1$, where $u_+,u_-$ are the circular components of $u$. Then $u=u(s_1,s_2)$ for the real numbers

$$
s_1=i\,\frac{u_+-1}{u_++1},\qquad s_2=i\,\frac{u_--1}{u_-+1}.
$$

**Proof.** For a unit complex number $w\neq-1$, the number $s=i(w-1)/(w+1)$ is real, because

$$
\bar s=-i\,\frac{\bar w-1}{\bar w+1}=-i\,\frac{w^{-1}-1}{w^{-1}+1}=-i\,\frac{1-w}{1+w}=i\,\frac{w-1}{w+1}=s,
$$

and it satisfies

$$
1-is=1+\frac{w-1}{w+1}=\frac{2w}{w+1},\qquad
1+is=1-\frac{w-1}{w+1}=\frac{2}{w+1},
$$

so $c(s)=(1-is)/(1+is)=w$. Applying this to $w=u_+$ and $w=u_-$ gives the two coordinates, and an element of the torus is determined by its circular components.

For a unit $\breve Q$ the circular components of the unit factor are $Q_{+}/\rho_+$ and $Q_{-}/\rho_-$, so the coordinates are

$$
s_1=i\,\frac{Q_{+}-\rho_+}{Q_{+}+\rho_+},\qquad
s_2=i\,\frac{Q_{-}-\rho_-}{Q_{-}+\rho_-}.
$$

The second form names the coordinates by $\breve Q$ alone. The denominators vanish exactly at $Q_{+}=-\rho_+$ and $Q_{-}=-\rho_-$, that is at the two walls of §*The Domain*, where the chart has no point.

### The Bijection

**Theorem.** The map $(s_1,s_2)\mapsto u(s_1,s_2)$ is a bijection from $\mathbb{R}^2$ onto $T^2\setminus M$.

**Injectivity.** If $u(s_1,s_2)=u(s_1',s_2')$, the two elements have the same circular components, so $c(s_1)=c(s_1')$ and $c(s_2)=c(s_2')$. On one circle, $c(s)=c(s')$ cross-multiplies to

$$
(1-is)(1+is')=(1-is')(1+is),
$$

that is $1+i(s'-s)+ss'=1+i(s-s')+ss'$, hence $s=s'$. The same for $s_2$.

**Surjectivity.** This is the proposition of §*The Inverse*: for every unit $u$ with neither circular component equal to $-1$, the real numbers $s_1,s_2$ of that proposition satisfy $u(s_1,s_2)=u$.

The chart is therefore one-to-one, and its image is the torus with the two circles $M$ removed.

## The Rational-Chart Decomposition

### Existence and Uniqueness

**Theorem.** Every unit $\breve Q$ with

$$
Q_{+}\notin(-\infty,0]\quad\text{and}\quad Q_{-}\notin(-\infty,0]
$$

has exactly one rational-chart polar decomposition

$$
\breve Q=\breve r\,u(s_1,s_2),\qquad \breve r\in P,\quad (s_1,s_2)\in\mathbb{R}^2.
$$

**Existence.** Let $\breve Q$ satisfy the two conditions, and put $\breve r=\sqrt{\breve Q\bar{\breve Q}}$ and $u=\breve r^{-1}\breve Q$. Then $\breve r\in P$ and $u\bar u=1$. Its circular components are $Q_{+}/\rho_+$ and $Q_{-}/\rho_-$. If the first were $-1$ then $Q_{+}=-\rho_+\le0$, contrary to the hypothesis; if the second were $-1$ then $Q_{-}=-\rho_-\le0$, also contrary. Hence neither component is $-1$, and the bijection gives real $s_1,s_2$ with $u=u(s_1,s_2)$. Therefore $\breve Q=\breve r u(s_1,s_2)$.

**Uniqueness.** Taking the bar gives $\breve r^2=\breve Q\bar{\breve Q}$, so $\breve r$ is the modulus; then $u=\breve r^{-1}\breve Q$; the chart is injective, so $(s_1,s_2)$ is determined by $u$.

The coordinates are those of §*The Inverse*, and the reconstruction is exact:

$$
\breve Q=\breve r\left(\frac{c(s_1)+c(s_2)}{2}+j\,\frac{c(s_1)-c(s_2)}{2}\right).
$$

### The Domain

The domain is the complement of the two walls

$$
W_+=\{\,Q_{+}\in(-\infty,0]\,\},\qquad W_-=\{\,Q_{-}\in(-\infty,0]\,\},
$$

each of real dimension three. The domain is

$$
\mathbb{B}_{\mathrm{r}}^{\times}\setminus(W_+\cup W_-).
$$

The zero divisors are excluded twice over: they are the lines $Q_{\blacktriangle}=Q_{\blacktriangledown}$ and $Q_{\blacktriangle}=-Q_{\blacktriangledown}$, and $Q_{\blacktriangle}=Q_{\blacktriangledown}$ lies in $W_-$ while $Q_{\blacktriangle}=-Q_{\blacktriangledown}$ lies in $W_+$. The walls are larger than the zero divisors. A unit can have $Q_{+}$ real and negative, for instance $Q_{\blacktriangle}=-3/2$, $Q_{\blacktriangledown}=1/2$, where $Q_{+}=-1$ and $Q_{-}=-2$; such a unit lies on both walls and has no chart coordinate, although it has a perfectly good modulus–unit decomposition with unit factor $(-1,-1)$.

In the formula $s_k=i(u_k-1)/(u_k+1)$ the two exclusions are visible at once: the denominator of the first vanishes at $u_+=-1$, that is $Q_{+}=-\rho_+$, and the denominator of the second at $u_-=-1$. The numerator and denominator of the second form both vanish at a zero divisor, where one of $\rho_+,\rho_-$ is zero and no decomposition of any kind exists.

## The Group Law

The product of two unit factors is a unit factor, and the coordinates of the product are rational functions of the two pairs of coordinates.

**Proposition.** For $(s_1,s_2)$ and $(t_1,t_2)$ in $\mathbb{R}^2$ with $s_1t_1\neq1$ and $s_2t_2\neq1$,

$$
u(s_1,s_2)\,u(t_1,t_2)=u(s_3,s_4),\qquad
s_3=\frac{s_1+t_1}{1-s_1t_1},\qquad s_4=\frac{s_2+t_2}{1-s_2t_2}.
$$

**Proof.** The circular components of the product are the products of the circular components:

$$
c(s_1)c(t_1),\qquad c(s_2)c(t_2).
$$

Multiplying the two fractions on one circle,

$$
c(s)c(t)=\frac{(1-is)(1-it)}{(1+is)(1+it)}
=\frac{(1-st)-i(s+t)}{(1-st)+i(s+t)}.
$$

Dividing numerator and denominator by $1-st$ puts the right-hand side in the form $(1-is_3)/(1+is_3)$ with $s_3=(s+t)/(1-st)$, which is $c(s_3)$. Applying this on each circle gives the two coordinates of the product.

The law has the identity $(0,0)$, because $c(0)=1$, and the inverse $(-s_1,-s_2)$, because

$$
c(s)c(-s)=\frac{1-is}{1+is}\cdot\frac{1+is}{1-is}=1
$$

on each circle. It is associative wherever it is defined, being inherited from the multiplication of the torus.

When $s_1t_1=1$ the first formula has a pole. The product of the first components is then

$$
c(s)c(1/s)=\frac{(1-is)(1-i/s)}{(1+is)(1+i/s)}=\frac{-i(s+1/s)}{i(s+1/s)}=-1,
$$

which is the missing point of the chart. The product is a perfectly good unit factor, but its first coordinate does not exist: it has escaped to infinity. The chart is therefore a **group chunk**, not a global group. It is a coordinate on the plane, and the plane must be compactified, component by component, to see the whole torus.

## Covering the Torus and the Price of Locality

### The Second Chart

The chart misses the two circles on which a component equals $-1$. The chart

$$
v(s_1,s_2)=-u(s_1,s_2)
$$

has circular components $-c(s_1)$ and $-c(s_2)$, so it misses the two circles on which a component equals $+1$, and it attains $-1$ in either component. On the common domain the two charts are related by

$$
v(s_1,s_2)=u\!\left(-\frac{1}{s_1},-\frac{1}{s_2}\right),\qquad s_1s_2\neq0,
$$

because $-c(s)=c(-1/s)$:

$$
c(-1/s)=\frac{1+i/s}{1-i/s}=\frac{s+i}{s-i}=-\frac{1-is}{1+is}.
$$

### The Four Charts

The two charts $u$ and $-u$ do not suffice. The unit with circular components $(1,-1)$ has its first component equal to $+1$ and its second equal to $-1$: the chart $u$ misses it on the second component and the chart $-u$ misses it on the first. The split unit $j$ has exactly these components, so it is missed by both.

Multiplying by $j$ flips the second circular component and leaves the first, and multiplying by $-j$ flips the first. The four charts

$$
u,\qquad ju,\qquad -u,\qquad -ju
$$

have the coordinate descriptions

$$
(s_1,s_2),\qquad \left(s_1,-\frac{1}{s_2}\right),\qquad
\left(-\frac{1}{s_1},s_2\right),\qquad
\left(-\frac{1}{s_1},-\frac{1}{s_2}\right).
$$

Their missed sets are the four unions

$$
\{u_+=\varepsilon_1\}\cup\{u_-=\varepsilon_2\},\qquad \varepsilon_1,\varepsilon_2\in\{\pm1\}.
$$

Every point of the torus avoids at least one of these sets, because a unit complex number cannot equal both $+1$ and $-1$. The four charts therefore cover the torus. They are the product of the two charts of each circle, and the multiplier $j$ is what makes the two circles independent.

### The Cut

The domain of one chart is the complement of the two walls $W_+$ and $W_-$. The wall $W_+$ is the set on which the first circular component is a non-positive real, and $W_-$ the set on which the second is. Each is a real three-dimensional half-space, and their union is the cut.

The cut is not the zero-divisor set, which is the union of the two lines $Q_{\blacktriangle}=Q_{\blacktriangledown}$ and $Q_{\blacktriangle}=-Q_{\blacktriangledown}$: the zero divisors are the part of the walls where $\rho_+\rho_-=0$. The cut is the price of the chart, not a singularity of the decomposition.

The chart has three properties, and they are the terms of an exchange.

- **It is rational.** Both $c(s)$ and its inverse are ratios of polynomials, and the reconstruction uses field operations alone. No transcendental function and no infinite series occur.
- **It is local.** It misses two circles of the torus, and therefore two walls of the unit group. Four charts, or a compactification in each component, are needed to recover the torus.
- **It is unbounded.** Near a missed circle the coordinate escapes to infinity, and the two sides of a wall carry opposite signs of the corresponding coordinate.

The modulus–unit form is global and uses a square root. The exponential form, treated in *Exponential Polar Decomposition of Reduced Biquaternions*, is global and uses a transcendental function. The present form is the one that stays rational, and locality is its price.

## The Matrix Picture

In the complex basis $\{1,j\}$ the unit $u(s_1,s_2)=u_{\blacktriangle}+ju_{\blacktriangledown}$ is the block matrix

$$
M_u=\begin{pmatrix}u_{\blacktriangle}&u_{\blacktriangledown}\\u_{\blacktriangledown}&u_{\blacktriangle}\end{pmatrix}
=\frac12\begin{pmatrix}c(s_1)+c(s_2)&c(s_1)-c(s_2)\\ c(s_1)-c(s_2)&c(s_1)+c(s_2)\end{pmatrix}.
$$

The change of basis $(z,w)\mapsto(z+w,z-w)$ diagonalises it:

$$
M_u\longmapsto\begin{pmatrix}c(s_1)&0\\0&c(s_2)\end{pmatrix}.
$$

In the real basis the change is orthogonal after the rescaling $u_\pm\mapsto u_\pm/\sqrt2$, and the matrix becomes the block diagonal matrix of the two rotations

$$
R(\theta_1)\oplus R(\theta_2),\qquad
R(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix},
$$

with $c(s_k)=e^{i\theta_k}$. The angles are related to the coordinates by

$$
\theta_k=-2\arctan s_k,\qquad s_k=-\tan\frac{\theta_k}{2}.
$$

The matrix lies in $SO(4)$. Its determinant is $\lvert c(s_1)\rvert^2\lvert c(s_2)\rvert^2=1$, and its trace is $2\cos\theta_1+2\cos\theta_2$. It is conformal exactly when $\theta_1=\pm\theta_2$, that is when $s_1=\pm s_2$; otherwise it has two distinct rotation angles.

## Worked Examples

### A Generic Element

Take $\breve Q=3+4i+j(1-i)$, so $Q_{\blacktriangle}=3+4i$ and $Q_{\blacktriangledown}=1-i$. The circular components and scales are

$$
Q_{+}=4+3i,\quad \rho_+=5,\qquad Q_{-}=2+5i,\quad \rho_-=\sqrt{29}=5.385164807134504.
$$

The unit factor has circular components

$$
u_+=\frac{4+3i}{5}=0.8+0.6i,\qquad
u_-=\frac{2+5i}{\sqrt{29}}=0.371390676354104+0.928476690885259\,i.
$$

The first is $c(-1/3)$, because

$$
c\!\left(-\tfrac13\right)=\frac{1+i/3}{1-i/3}=\frac{3+i}{3-i}=0.8+0.6i.
$$

The second is $c(s_2)$ with

$$
s_2=i\,\frac{u_--1}{u_-+1}
=-\tan\frac{\theta_-}{2}
=-\frac{5}{\sqrt{29}+2}=-0.6770329614269008,
$$

where $\theta_-=\arctan(5/2)=1.1902899$. The chart coordinate is therefore

$$
(s_1,s_2)=\left(-\frac13,\ -0.6770329614269008\right).
$$

The modulus is the one computed in *Modulus–Unit Polar Decomposition of Reduced Biquaternions*,

$$
\breve r=5.192582403567252-0.192582403567252\,j,
$$

and the reconstruction

$$
\breve r\,u(s_1,s_2)
$$

returns $3+4i+j(1-i)$ with Euclidean error of order $10^{-16}$ in double precision.

### The Circle Charts

The scalar circle is the locus $s_1=s_2$. On it the chart reduces to the complex chart:

$$
u(s,s)=c(s)=\frac{1-is}{1+is},
$$

and the decomposition is the complex rational-chart decomposition of the two equal circular components.

The $ij$-circle is the locus $s_2=-s_1$. In terms of the angles, the unit $u=e^{i\alpha}e^{ij\beta}$ has circular components $e^{i(\alpha+\beta)}$ and $e^{i(\alpha-\beta)}$, so

$$
s_1=-\tan\frac{\alpha+\beta}{2},\qquad s_2=-\tan\frac{\alpha-\beta}{2}.
$$

The scalar circle is $\beta=0$, where $s_1=s_2$; the $ij$-circle is $\alpha=0$, where $s_2=-s_1$.

The values of the chart at the small integers are

$$
c(0)=1,\qquad c(1)=-i,\qquad c(-1)=i,\qquad c(2)=\frac{1-4-4i}{5}=-\frac35-\frac45 i.
$$

### The Pole and the Missing Unit

Take $s_1=1/2$ and $t_1=2$, so $s_1t_1=1$. The product of the first components is

$$
c(1/2)\,c(2)=\frac{1-i/2}{1+i/2}\cdot\frac{1-2i}{1+2i}.
$$

The first factor is $(3-4i)/5$ and the second is $(-3-4i)/5$, and their product is $-1$. The product unit has $u_+=-1$: it exists, but the first coordinate of the product does not. The formula $s_3=(s_1+t_1)/(1-s_1t_1)$ has a pole at $s_1t_1=1$. The product lies in the chart $-u$, whose first coordinate is $-1/s_3$, and there the value is $0$: the point at infinity of the first chart is the origin of the second.

The unit $j$ has circular components $(1,-1)$: its first coordinate is $s_1=0$, and its second is missing in the chart $u$. In the chart $ju$ the second component is flipped to $+1$, so the second coordinate becomes $-1/s_2=0$, and the point has coordinates $(0,0)$. The unit $-1$ has components $(-1,-1)$ and is missing in the chart $u$; it is covered by $-u$, with coordinates $(0,0)$.

### A Table of Examples

| $\breve Q$ | $u_+$ | $u_-$ | chart | $(s_1,s_2)$ |
|---|---|---|---|---|
| $3+4i+j(1-i)$ | $0.8+0.6i$ | $(2+5i)/\sqrt{29}$ | $u$ | $(-1/3,\ -0.6770329614)$ |
| $1+i$ | $e^{i\pi/4}$ | $e^{i\pi/4}$ | $u$ | $(-\tan(\pi/8),\ -\tan(\pi/8))$ |
| $i$ | $i$ | $i$ | $u$ | $(-1,\ -1)$ |
| $ij$ | $i$ | $-i$ | $u$ | $(-1,\ 1)$ |
| $j$ | $1$ | $-1$ | $ju$ | $(0,\ 0)$ |
| $-1$ | $-1$ | $-1$ | $-u$ | $(0,\ 0)$ |
| $1+j$ | $2$ | $0$ | — | — |

The coordinates are read in the chart named. The row $1+i$ is the scalar case: the two coordinates are equal and the decomposition is the complex one. The rows $j$ and $-1$ are outside the chart $u$ and inside another chart, where their coordinates are $(0,0)$ because $ju=1$ and $-(-1)=1$. The row $1+j$ is the zero divisor, where no decomposition exists.

## Summary

Every unit $\breve Q$ with $Q_{+}\notin(-\infty,0]$ and $Q_{-}\notin(-\infty,0]$ has exactly one rational-chart polar decomposition

$$
\breve Q=\breve r\,u(s_1,s_2),\qquad
u(s_1,s_2)=\frac{c(s_1)+c(s_2)}{2}+j\,\frac{c(s_1)-c(s_2)}{2},\qquad
c(s)=\frac{1-is}{1+is},
$$

with $\breve r=\sqrt{\breve Q\bar{\breve Q}}$ the modulus in $P$ and $(s_1,s_2)\in\mathbb{R}^2$. The coordinates are rational in the circular components,

$$
s_1=i\,\frac{u_+-1}{u_++1},\qquad s_2=i\,\frac{u_--1}{u_-+1},
$$

and the reconstruction is exact by field operations.

The chart is a bijection from $\mathbb{R}^2$ onto the torus minus the two circles on which a circular component equals $-1$. It is a group chunk: for $s_1t_1\neq1$ and $s_2t_2\neq1$,

$$
u(s_1,s_2)u(t_1,t_2)=u\!\left(\frac{s_1+t_1}{1-s_1t_1},\frac{s_2+t_2}{1-s_2t_2}\right),
$$

with the identity $(0,0)$ and the inverse $(-s_1,-s_2)$. At a pole the product has a component equal to $-1$, and its coordinate does not exist. The four charts $u$, $ju$, $-u$, $-ju$ cover the torus, and they are the product of the two charts of each circle.

The domain is the complement of the two walls $W_+=\{Q_{+}\in(-\infty,0]\}$ and $W_-=\{Q_{-}\in(-\infty,0]\}$, each of real dimension three. The walls are strictly larger than the zero divisors, which are the part of the walls where $\rho_+\rho_-=0$. The chart is rational, local and unbounded; the modulus–unit form is global and algebraic, and the exponential form is global and transcendental.

In the matrix picture the unit factor is orthogonally conjugate to the block diagonal matrix of the two rotations $R(\theta_1)\oplus R(\theta_2)$, with $\theta_k=-2\arctan s_k$, and it lies in $SO(4)$. It is conformal exactly when $s_1=\pm s_2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | the element, $Q_{\blacktriangle}$ scalar part, $Q_{\blacktriangledown}$ split part |
| $\breve r\in P$ | the modulus |
| $u\in T^2$ | the unit factor |
| $Q_{+}$, $Q_{-}$ | the two circular components |
| $u_+= (Q_{+})/\rho_+$, $u_-=(Q_{-})/\rho_-$ | the circular components of the unit factor |
| $c(s)=\dfrac{1-is}{1+is}$ | the circle chart |
| $u(s_1,s_2)$ | the torus chart with components $c(s_1),c(s_2)$ |
| $M=\{\text{a circular component}=-1\}$ | the two circles missed by the chart |
| $W_\pm=\{Q_{\pm}\in(-\infty,0]\}$ | the two walls of the cut |
| $s_k=i(u_k-1)/(u_k+1)$ | the inverse chart |
| $(s_3,s_4)$ | the coordinates of a product |
| $R(\theta)$ | the rotation block |
| $SO(4)$ | the special orthogonal group |

## Further Reading

- [Modulus–Unit Polar Decomposition of Reduced Biquaternions](modulus-unit-polar-decomposition-of-reduced-biquaternions.html), for the modulus, the torus and the uniqueness of the pair.
- [Exponential Polar Decomposition of Reduced Biquaternions](exponential-polar-decomposition-of-reduced-biquaternions.html), for the transcendental coordinate on the torus.
- [Rational-Chart Polar Decomposition of Complex Numbers](rational-chart-polar-decomposition-of-complex-numbers.html), for the complex member of the family.
- [Rational-Chart Polar Decomposition of Split-Complex Numbers](rational-chart-polar-decomposition-of-split-complex-numbers.html), for the hyperbolic companion.
- [The Group of Units of the Algebra of the Reduced Biquaternions](the-group-of-units-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the topology of the torus.
- [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the two zero-divisor lines.
