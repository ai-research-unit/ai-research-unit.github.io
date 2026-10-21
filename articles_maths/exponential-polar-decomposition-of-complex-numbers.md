# __Exponential Polar Decomposition of Complex Numbers__

## Introduction

This article develops the **exponential polar decomposition** of a nonzero complex number: the writing

$$
Q = \exp(\ln r + i\theta), \qquad r = \lvert Q\rvert > 0, \quad \theta = \operatorname{Arg}Q \in (-\pi,\pi].
$$

The two data are read directly from the coordinates $Q = a+ib$:

$$
r = \sqrt{a^2+b^2}, \qquad \theta = \operatorname{atan2}(b,a),
$$

the Euclidean length and the polar angle of the point $(a,b)$. The modulus $r$ is positive and determined; the angle $\theta$ is the unique representative in $(-\pi,\pi]$ of the argument of $Q$, and every other angle of $Q$ is $\theta+2\pi k$. The exponent $\ln r+i\theta$ is the principal logarithm of $Q$. This is the entire content of the decomposition: the rest of the article explains why the exponential reproduces $Q$ from those two numbers, and what changes when the angle is not restricted.

The exponential form is the third of the three polar decompositions of $\mathbb{C}$. The first is the modulus–unit form $Q = ru$ with $r = \lvert Q\rvert$ and $u = Q/\lvert Q\rvert$, developed in *Modulus–Unit Polar Decomposition of Complex Numbers*; the second is the rational-chart form, developed in *Rational-Chart Polar Decomposition of Complex Numbers*; the third is the exponential form treated here. The three are the same factorisation in three presentations: the modulus–unit form is coordinate-free, while the rational and exponential forms put a coordinate on the unit factor, the rational one local and the exponential one global. The comparison is the subject of §*The Three Polar Decompositions*.

The symbols are those of *Complex Algebra* and *Complex Norm and Invertibility*, and the conventions are those of *Conventions in Mathematics*; the modulus–unit decomposition is recalled from *Modulus–Unit Polar Decomposition of Complex Numbers*, the rational-chart coordinate from *Rational-Chart Polar Decomposition of Complex Numbers*, and the exponential and its group law from *Complex Exponential and Lie Group Structure*.

The plan follows the order in which the objects are needed. The exponential and its closed form are recalled, with the modulus and the angle written explicitly (§*The Exponential and Its Closed Form*, §*The Modulus and the Angle*), and the directions it uses are classified (§*The Three Rows of the Exponential*). Its image and kernel are then computed (§*The Image and the Kernel*), and the polar word is read as one exponential (§*The Polar Word as One Exponential*). The logarithm and the principal strip follow (§*The Logarithm and the Principal Strip*), then the decomposition is stated and proved (§*The Exponential Polar Decomposition*), and the matrix picture (§*The Matrix Picture*) and the comparison with the two other forms (§*The Three Polar Decompositions*) follow. Examples are computed (§*Worked Examples*), and the exponential coordinates close the article (§*The Exponential Coordinates*).

Every numerical value displayed below was recomputed in double precision.

## The Exponential Map and the Polar Word

### The Exponential and Its Closed Form

For $Q = x+iy$ the exponential is the power series

$$
\exp(Q) = \sum_{n=0}^{\infty} \frac{Q^n}{n!},
$$

which converges absolutely and locally uniformly. Separating even and odd powers, and using $i^{2n} = (-1)^n$ and $i^{2n+1} = (-1)^n i$, gives the closed form

$$
\exp(x+iy) = \exp(x)\left(\sum_{n=0}^{\infty}\frac{(-1)^n y^{2n}}{(2n)!} + i\sum_{n=0}^{\infty}\frac{(-1)^n y^{2n+1}}{(2n+1)!}\right) = \exp(x)\bigl(\cos y+i\sin y\bigr).
$$

The modulus and the argument follow at once:

$$
\lvert\exp(x+iy)\rvert = \exp(x), \qquad \arg\exp(x+iy) = y \pmod{2\pi}, \qquad \exp(x+iy)\neq0.
$$

The exponential never vanishes. Its real part is a logarithmic scale and its imaginary part is an angle, which is exactly the shape of the decomposition.

The exponential is a homomorphism from the additive group of $\mathbb{C}$ to the multiplicative group $\mathbb{C}^\times$:

$$
\exp(Q_1+Q_2) = \exp(Q_1)\exp(Q_2).
$$

**Proof.** The complex numbers commute, so the binomial theorem reorders the product of the two absolutely convergent series into the series of $\exp(Q_1+Q_2)$. No bracket survives, and the identity is exact.

### The Modulus and the Angle

**Definition.** Let $Q = a+ib\neq0$. The **modulus** of $Q$ is

$$
r = \lvert Q\rvert = \sqrt{a^2+b^2} > 0,
$$

and the **principal argument** is the unique $\theta\in(-\pi,\pi]$ with

$$
\cos\theta = \frac{a}{r}, \qquad \sin\theta = \frac{b}{r}.
$$

In coordinates, $\theta = \operatorname{atan2}(b,a)$: the angle of the vector $(a,b)$ measured from the positive real axis. On each quadrant it is an elementary arctangent:

| position of $Q = a+ib$ | $\operatorname{Arg}Q$ |
|---|---|
| $a>0$ | $\arctan(b/a)$ |
| $a=0$, $b>0$ | $\pi/2$ |
| $a<0$, $b\ge0$ | $\arctan(b/a)+\pi$ |
| $a<0$, $b<0$ | $\arctan(b/a)-\pi$ |
| $a=0$, $b<0$ | $-\pi/2$ |

At the origin the angle is undefined, so $Q\neq0$ throughout. The angle is defined modulo $2\pi$: the angles of $Q$ are $\theta+2\pi k$ with $k\in\mathbb{Z}$, and $\theta$ is the unique representative in $(-\pi,\pi]$.

With these two numbers the decomposition is an identity, not a construction:

$$
Q = r\bigl(\cos\theta+i\sin\theta\bigr) = r\exp(i\theta) = \exp(\ln r+i\theta).
$$

The first equality is the definition of $r$ and $\theta$, the second is the Euler formula, and the third writes $r = \exp(\ln r)$ and adds the two exponents, which commute. For example, $Q = 3+4i$ has $r = \sqrt{9+16} = 5$ and $\theta = \arctan(4/3) = 0.9272952180016122$, hence

$$
Q = 5\exp(0.9272952180016122\,i) = \exp(1.6094379124341003+0.9272952180016122\,i).
$$

### The Three Rows of the Exponential

The closed form is one row of a trichotomy governed by the square of the exponent direction. Let $\nu\in\mathbb{C}$ be an element with $\nu^2\in\{-1,0,+1\}$, and let $t\in\mathbb{R}$. Then

$$
\exp(\nu t) =
\begin{cases}
\cos t+\nu\sin t, & \nu^2 = -1,\\[2pt]
1, & \nu^2 = 0,\\[2pt]
\cosh t+\nu\sinh t, & \nu^2 = +1,
\end{cases}
$$

the three rows being the trigonometric, the parabolic and the hyperbolic.

| equation | roots in $\mathbb{C}$ | row | image of $t\mapsto\exp(\nu t)$ |
|---|---|---|---|
| $\nu^2 = -1$ | $\nu = \pm i$ | trigonometric | $\mathrm{U}(1)$ |
| $\nu^2 = 0$ | $\nu = 0$ | parabolic | $\{1\}$ |
| $\nu^2 = +1$ | $\nu = \pm1$ | hyperbolic | $\mathbb{R}_{>0}$ |

The roots of $-1$ are $\pm i$, the two points where the unit circle meets the imaginary axis; they generate the unit circle. The roots of $+1$ are $\pm1$, both real; they generate the positive scale. In the polar word the unit factor uses the first row and the scale the third. The middle row contributes nothing, because the algebra has no nilpotent direction: the only solution of $\nu^2 = 0$ is $\nu = 0$.

The split-complex algebra exchanges the two occupied rows. There $-1$ has no root, so the trigonometric row is empty; $+1$ has the four roots $\pm1,\pm j$, so the unit factor is hyperbolic and the scale stays real. The complex algebra is the case in which the unit factor is compact, and this single fact explains most of the differences between the two articles.

### The Image and the Kernel

**Kernel.** Suppose $\exp(x+iy) = 1$. Taking moduli gives $\exp(x) = 1$, hence $x = 0$; then $\cos y+i\sin y = 1$, hence $y\in2\pi\mathbb{Z}$. Therefore

$$
\ker\exp = 2\pi i\,\mathbb{Z}.
$$

It is a lattice, not $\{0\}$: the exponential is not injective, and it is periodic with period $2\pi i$. It is also the entire failure of injectivity: the exponential forgets the integer $k$ and nothing else.

**Image.** Let $Q = a+ib\neq0$, and take $r$ and $\theta$ as in §*The Modulus and the Angle*. Then

$$
\exp(\ln r+i\theta) = r\exp(i\theta) = Q,
$$

so every nonzero complex number is an exponential and $\exp(\mathbb{C}) = \mathbb{C}^\times$. The fibre over $Q$ is the coset

$$
\exp^{-1}(Q) = \operatorname{Log}Q+2\pi i\,\mathbb{Z}, \qquad \operatorname{Log}Q = \ln\lvert Q\rvert+i\operatorname{Arg}Q.
$$

The exponential is therefore a surjective homomorphism with kernel $2\pi i\mathbb{Z}$, and the first isomorphism theorem gives

$$
\mathbb{C}^\times \cong \mathbb{C}/2\pi i\,\mathbb{Z}
$$

as groups and as real manifolds.

The complex and the split-complex cases fail in opposite ways. Here existence is free and uniqueness fails: every nonzero element is an exponential, and the angle is ambiguous. There existence fails on three of the four components and uniqueness is free: the exponential is injective, and three components have no logarithm at all. In neither algebra is the exponential an isomorphism, but the obstruction sits in the kernel in one case and in the image in the other.

### The Polar Word as One Exponential

**Definition.** Let $Q\in\mathbb{C}$, $Q\neq0$. An **exponential polar decomposition** of $Q$ is a writing

$$
Q = \exp(\ln r)\exp(i\theta), \qquad r>0, \quad \theta\in\mathbb{R}/2\pi\mathbb{Z},
$$

in which $\exp(\ln r)$ is the positive scale and $\exp(i\theta)$ is the unit factor.

The two factors are the two exponentials of the polar word. If $Q = \exp(\ln r+i\theta)$, then

$$
\exp(\ln r) = \lvert Q\rvert, \qquad \exp(i\theta) = \frac{Q}{\lvert Q\rvert},
$$

because the modulus of $\exp(\ln r+i\theta)$ is $r$ and its argument is $\theta$. The scale is the real exponential, the unit factor is the imaginary exponential, and the two exponents commute, since $\mathbb{R}$ is central in $\mathbb{C}$:

$$
Q = \exp(\ln r)\exp(i\theta) = \exp(\ln r+i\theta).
$$

The word is therefore **one exponential**, not a product of two independent exponentials. The amalgamation is a property of the commutative algebra; in a noncommutative algebra the two exponents need not commute and the product need not be a single exponential, as the polar word of *The Polar Element Representation of Biquaternions* shows.

| factor | formula | real dimension | range | exponent | parameter |
|---|---|---|---|---|---|
| scale | $\exp(\ln r)$ | $1$ | $(0,\infty)$ | $\ln r$ | $r>0$ |
| unit factor | $\exp(i\theta)$ | $1$ | $\mathrm{U}(1)$ | $i\theta$ | $\theta\in\mathbb{R}/2\pi\mathbb{Z}$ |

The counts add to the real dimension two of $\mathbb{C}$. The scale is non-compact, the unit factor is compact, and the exponential form separates the two.

## The Logarithm and the Principal Strip

### The Logarithm

**Definition.** A **logarithm** of $Q\in\mathbb{C}^\times$ is a complex number $Q_{\log}$ with $\exp Q_{\log} = Q$.

**Theorem.** Every nonzero complex number has a logarithm, and the logarithms of $Q$ are exactly

$$
\operatorname{Log}Q+2\pi i k, \qquad k\in\mathbb{Z}, \qquad \operatorname{Log}Q = \ln\lvert Q\rvert+i\operatorname{Arg}Q.
$$

**Proof.** Existence is the image statement of §*The Image and the Kernel*: with $r = \lvert Q\rvert$ and $\theta = \operatorname{Arg}Q$, the number $\operatorname{Log}Q = \ln r+i\theta$ satisfies $\exp(\operatorname{Log}Q) = Q$. If $\exp Q_{\log} = \exp Q'_{\log} = Q$, then $\exp(Q_{\log}-Q'_{\log}) = 1$, so $Q_{\log}-Q'_{\log}\in\ker\exp = 2\pi i\mathbb{Z}$. Hence every logarithm is $\operatorname{Log}Q+2\pi i k$.

The formula is read in coordinates: the real part is $\ln\lvert Q\rvert = \tfrac12\ln(a^2+b^2)$, the imaginary part is $\operatorname{atan2}(b,a)$. The theorem is the exact analogue of the split-complex statement, with the roles of existence and uniqueness exchanged: there the logarithm exists only on the future cone and is then unique; here it exists everywhere on $\mathbb{C}^\times$ and is never unique.

### The Principal Strip

**Theorem (principal strip).** The map

$$
S = \{\,\ln r+i\theta : r>0,\ -\pi<\theta\le\pi\,\} \longrightarrow \mathbb{C}^\times, \qquad Q_{\log} \longmapsto \exp Q_{\log},
$$

is a bijection, with inverse $\operatorname{Log}$.

**Proof.** Existence is the theorem above, whose angle lies in $(-\pi,\pi]$. For uniqueness, suppose $\exp(\ln r_1+i\theta_1) = \exp(\ln r_2+i\theta_2)$ with both angles in $(-\pi,\pi]$. Taking moduli gives $r_1 = r_2$, hence $\ln r_1 = \ln r_2$. Dividing, $\exp\bigl(i(\theta_1-\theta_2)\bigr) = 1$, so $\theta_1-\theta_2\in2\pi\mathbb{Z}$. The two angles lie in $(-\pi,\pi]$, an interval of length $2\pi$ with one endpoint open and one closed, so their difference lies in $(-2\pi,2\pi)$; the only multiple of $2\pi$ in that interval is $0$. Hence $\theta_1 = \theta_2$.

The strip is a **fundamental domain** for the action of $2\pi i\mathbb{Z}$ on $\mathbb{C}$ by translations, and the exponential identifies the two edges $\theta = -\pi$ and $\theta = \pi$, whose common image is the branch cut. The restriction to the open strip $-\pi<\theta<\pi$ is a diffeomorphism onto the cut plane $\mathbb{C}\setminus(-\infty,0]$. The half-open strip adds the negative real axis at $\theta = \pi$; there the inverse is discontinuous, and the two sides of the cut differ by $2\pi i$.

### The Principal Logarithms of Some Elements

| $Q$ | $\lvert Q\rvert$ | $\operatorname{Arg}Q$ | $\operatorname{Log}Q$ |
|---|---|---|---|
| $3+4i$ | $5$ | $0.9272952180016122$ | $1.6094379124341003+0.9272952180016122\,i$ |
| $-1$ | $1$ | $\pi$ | $\pi i$ |
| $i$ | $1$ | $\pi/2$ | $\frac{\pi}{2}i$ |
| $1+i$ | $\sqrt{2}$ | $\pi/4$ | $0.3465735902799727+0.7853981633974483\,i$ |
| $-1-i$ | $\sqrt{2}$ | $-3\pi/4$ | $0.3465735902799727-2.356194490192345\,i$ |

The fifth line shows the branch convention: the argument of $-1-i$ is $-3\pi/4$, not $5\pi/4$, because the principal argument lies in $(-\pi,\pi]$. In the split-complex table the entries $-1$ and $j$ have no logarithm; here every nonzero entry has one.

## The Exponential Polar Decomposition

### Existence and Uniqueness

**Theorem.** Every nonzero complex number $Q$ has exactly one exponential polar decomposition

$$
Q = \exp(\ln r)\exp(i\theta), \qquad r>0, \quad \theta\in(-\pi,\pi],
$$

namely

$$
r = \lvert Q\rvert = \sqrt{(\operatorname{Re}Q)^2+(\operatorname{Im}Q)^2}, \qquad \theta = \operatorname{Arg}Q = \operatorname{atan2}(\operatorname{Im}Q,\operatorname{Re}Q),
$$

the modulus and the principal angle of §*The Modulus and the Angle*.

**Existence.** Take $r = \lvert Q\rvert$ and $\theta = \operatorname{Arg}Q$. Then $\exp(\ln r) = \lvert Q\rvert$ and $\exp(i\theta) = Q/\lvert Q\rvert$, so the product is $Q$.

**Uniqueness.** Suppose $\exp(\ln r_1)\exp(i\theta_1) = \exp(\ln r_2)\exp(i\theta_2)$ with both angles in $(-\pi,\pi]$. The product is $\exp(\ln r_1+i\theta_1) = \exp(\ln r_2+i\theta_2)$, and the principal-strip theorem gives $\ln r_1 = \ln r_2$ and $\theta_1 = \theta_2$; hence $r_1 = r_2$.

The theorem is the modulus–unit theorem with the scale and the unit factor written as exponentials, and it is the principal-strip theorem read as a decomposition. It is unique because the principal argument is unique; without the restriction on $\theta$, the exponent is unique only modulo $2\pi i$.

### The Two Factors

The factors of the decomposition are

$$
\exp(\ln r) = \lvert Q\rvert, \qquad \exp(i\theta) = \frac{Q}{\lvert Q\rvert}.
$$

The first is the positive scale, the second is the unit factor on the circle. The exponent is their sum:

$$
Q_{\log} = \ln r+i\theta = \ln\lvert Q\rvert+i\operatorname{Arg}Q = \operatorname{Log}Q.
$$

The exponential form is therefore the statement that the principal logarithm is a right inverse of the exponential on $\mathbb{C}^\times$, and the decomposition is the graph of the principal logarithm.

The parameters are two: the modulus $r>0$ and the angle $\theta\in\mathbb{R}/2\pi\mathbb{Z}$. The scale is non-compact, the angle runs on the compact circle, and the product is the group of units:

$$
\mathbb{C}^\times \cong \mathbb{R}_{>0}\times(\mathbb{R}/2\pi\mathbb{Z}) \cong \mathbb{R}_{>0}\times\mathrm{U}(1).
$$

### The Group Law in Exponential Coordinates

The exponential turns multiplication into addition:

$$
\exp\bigl((\ln r_1+i\theta_1)+(\ln r_2+i\theta_2)\bigr) = \exp(\ln r_1+i\theta_1)\exp(\ln r_2+i\theta_2).
$$

In the coordinates $(\ln r,\theta)$ the group law is

$$
(\ln r_1,\theta_1)*(\ln r_2,\theta_2) = \bigl(\ln(r_1r_2),\ \theta_1+\theta_2\bmod 2\pi\bigr).
$$

The first coordinate is the logarithmic scale, the second is the angle, and the two do not mix. The exponential coordinates are the coordinates in which the group $\mathbb{C}^\times$ is the product of a line and a circle.

### The Decomposition in One Table

| datum | exponential polar decomposition |
|---|---|
| domain | $Q\neq0$ |
| modulus | $r = \lvert Q\rvert = \sqrt{(\operatorname{Re}Q)^2+(\operatorname{Im}Q)^2}$ |
| angle | $\theta = \operatorname{Arg}Q = \operatorname{atan2}(\operatorname{Im}Q,\operatorname{Re}Q)\in(-\pi,\pi]$ |
| exponent | $Q_{\log} = \ln r+i\theta = \operatorname{Log}Q$ |
| scale | $\exp(\ln r) = \lvert Q\rvert$ |
| unit factor | $\exp(i\theta) = Q/\lvert Q\rvert$ |
| uniqueness | $Q_{\log}$ unique in the principal strip; modulo $2\pi i$ in general |
| group | $\mathbb{C}^\times\cong\mathbb{C}/2\pi i\mathbb{Z}$ |
| factor types | non-compact scale, compact unit factor |

## The Matrix Picture

### The Exponential of a Conformal Matrix

In the real basis $\{1,i\}$ a complex number is $Q = a+ib$, and multiplication by $Q$ is the matrix

$$
M_Q = aI+bJ, \qquad J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad J^2 = -I.
$$

The matrices $I$ and $J$ commute, so the exponential splits:

$$
\exp(xI+yJ) = \exp(xI)\exp(yJ) = \exp(x)\bigl(\cos y\,I+\sin y\,J\bigr).
$$

The exponential polar decomposition of $M_Q$ is therefore

$$
M_Q = \exp\bigl(\ln r\,I+\theta J\bigr) = r\bigl(\cos\theta\,I+\sin\theta\,J\bigr) = rR_\theta,
$$

with $r = \lvert Q\rvert$ and $\theta = \operatorname{Arg}Q$. The positive factor is the scalar $rI$, and the orthogonal factor is the rotation $R_\theta\in SO(2)$. This is the polar decomposition of the conformal matrix: the positive definite part is a scalar, because the only symmetric positive definite matrices in the family $aI+bJ$ are the positive scalar multiples of the identity.

More generally, every invertible real $2\times2$ matrix $B$ has a unique polar decomposition $B = PU$, with $P$ symmetric positive definite and $U$ orthogonal. The factors are $P = (BB^{\mathsf T})^{1/2}$ and $U = P^{-1}B$; the square root exists because $BB^{\mathsf T}$ is symmetric positive definite, and $UU^{\mathsf T} = P^{-1}BB^{\mathsf T}P^{-1} = I$. For $B = M_Q$ the two factors collapse to $P = rI$ and $U = R_\theta$, because $M_Q$ is conformal; the general theorem is the same splitting without the conformal restriction, the positive factor then carrying the two singular values instead of the single scale $r$.

### The Matrix Logarithm

The matrix logarithm of $M_Q$ is

$$
\log M_Q = \ln r\,I+\theta J
$$

on the principal branch. Adding $2\pi k J$ gives another logarithm, because $\exp(2\pi k J) = I$; for $Q$ non-real the centraliser of $M_Q$ is spanned by $I$ and $J$, so this is the full ambiguity of the angle. The eigenvalues of $M_Q$ are $a\pm ib$, neither zero when $Q\neq0$, and the real logarithm exists; for $Q$ real and negative the principal one is $\ln\lvert Q\rvert\,I+\pi J$. On the two-dimensional subalgebra spanned by $I$ and $J$ the exponential is the map $(x,y)\mapsto\exp(x)R_y$, a local diffeomorphism with Jacobian determinant $\exp(2x)$.

### The Derivative and the Jacobian

The derivative of the exponential at $Q_{\log}$ is multiplication by $\exp Q_{\log}$:

$$
d\exp_{Q_{\log}}(H) = \exp(Q_{\log})H,
$$

because $\exp(Q_{\log}+tH) = \exp(Q_{\log})\exp(tH)$ when $Q_{\log}$ and $H$ commute, as they do in $\mathbb{C}$.

The derivative is invertible, with inverse multiplication by $\exp(-Q_{\log})$, so the exponential is a local diffeomorphism. In the real coordinates $(\ln r,\theta)$ the Jacobian determinant is

$$
\det d\exp_{Q_{\log}} = \lvert\exp Q_{\log}\rvert^2 = r^2 = N(Q),
$$

the squared modulus. The exponential is conformal: it multiplies lengths by $r$ and preserves angles and orientation.

## The Three Polar Decompositions

### The Three Forms

| decomposition | formula | parameters | domain | uniqueness | functions | group reading |
|---|---|---|---|---|---|---|
| modulus–unit | $Q = ru$ | $r>0$, $u\in\mathrm{U}(1)$ | $\mathbb{C}^\times$ | unique | square root | $\mathbb{R}_{>0}\times\mathrm{U}(1)$ |
| rational-chart | $Q = r\frac{1-is}{1+is}$ | $r>0$, $s\in\mathbb{R}$ | $\mathbb{C}\setminus(-\infty,0]$ | unique on the chart | rational | $\mathbb{R}_{>0}\times\mathbb{R}$, the Cayley coordinate, local |
| exponential | $Q = \exp(\ln r+i\theta)$ | $r>0$, $\theta\in\mathbb{R}/2\pi\mathbb{Z}$ | $\mathbb{C}^\times$ | exponent modulo $2\pi i$; unique with the principal angle | exponential and logarithm | $\mathbb{C}/2\pi i\mathbb{Z}$ |

### The Modulus–Unit Form

The modulus–unit form is $Q = ru$ with $r = \lvert Q\rvert$ and $u = Q/\lvert Q\rvert$. It is unique on the whole of $\mathbb{C}^\times$, it uses the square root of the norm, and it is the product decomposition of the group of units. It is the form developed in *Modulus–Unit Polar Decomposition of Complex Numbers*.

### The Rational-Chart Form

The rational-chart form writes the unit factor by the Cayley chart of the circle, and it is the form developed in *Rational-Chart Polar Decomposition of Complex Numbers*. For $s\in\mathbb{R}$,

$$
u(s) = \frac{1-is}{1+is} = \frac{1-s^2}{1+s^2}-i\frac{2s}{1+s^2},
$$

and $s\mapsto u(s)$ is a bijection from $\mathbb{R}$ onto $\mathrm{U}(1)\setminus\{-1\}$. It is rational, uses no transcendental function, and misses the single point $u = -1$, the unit factor of the negative real axis. The decomposition $Q = r\,u(s)$ is therefore a rational chart, not a global decomposition.

### The Exponential Form

The exponential form is $Q = \exp(\ln r+i\theta)$ with $r = \lvert Q\rvert$ and $\theta = \operatorname{Arg}Q$ in the principal strip. It is global on $\mathbb{C}^\times$, it uses the exponential and the logarithm, and its exponent is unique only modulo the kernel $2\pi i\mathbb{Z}$; the principal strip restores uniqueness. It is the form that exposes the Lie algebra and the group law.

### The Change of Coordinates

Comparing $u(s) = (1-is)/(1+is)$ with $u = \exp(i\theta)$ and using the half-angle identity gives

$$
\frac{1-is}{1+is} = \exp\bigl(-2i\arctan s\bigr),
$$

so the passage between the rational coordinate and the angle is

$$
s = -\tan\frac{\theta}{2}, \qquad \theta = -2\arctan s.
$$

The map $s\mapsto\theta$ sends $\mathbb{R}$ onto $(-\pi,\pi)$, and $s\to\pm\infty$ corresponds to $\theta\to\mp\pi$. The cut $\theta = \pi$ is the negative real axis; its unit factor is $-1$, the single point the rational chart misses, and it is also the point at which the rational coordinate escapes to infinity.

### What the Comparison Says

The three forms are three presentations of one factorisation, not three different factorisations of the element; the modulus–unit form is coordinate-free, and the other two put a coordinate on the circle, the rational one local and the exponential one global. The modulus–unit form is the product decomposition, global and algebraic, with a square root. The rational-chart form is the Cayley chart, rational and local, missing the negative real axis. The exponential form is the Lie algebra coordinate, global and transcendental, with the kernel as the only ambiguity of the exponent.

The exponential form is the only one in which the group law is addition. The modulus–unit form is the only one that is algebraic and global. The rational-chart form is the only one that is rational and local. They are three presentations of the complex member of the eight algebras whose polar decompositions are compared in *Comparison of the Polar Element Representation*; in a noncommutative algebra the exponential of a sum is not the product of the exponentials, the exponents need not commute, and the amalgamation into one exponential fails. In the polar word of *The Polar Element Representation of Biquaternions* the order of the factors carries information.

## Worked Examples

### A Generic Complex Number

Take $Q = 3+4i$. Then

$$
r = \sqrt{9+16} = 5, \qquad \ln r = 1.6094379124341003, \qquad \theta = \arctan\tfrac{4}{3} = 0.9272952180016122,
$$

and

$$
Q_{\log} = \ln r+i\theta = 1.6094379124341003+0.9272952180016122\,i.
$$

The reconstruction is

$$
\exp Q_{\log} = 3+3.999999999999999\,i,
$$

with error $8.9\times10^{-16}$ in the Euclidean modulus.

### A Table of Examples

| $Q$ | $\ln\lvert Q\rvert$ | $\theta = \operatorname{Arg}Q$ | $Q_{\log} = \ln\lvert Q\rvert+i\theta$ | $\lvert\exp Q_{\log}-Q\rvert$ |
|---|---|---|---|---|
| $3+4i$ | $1.6094379124341003$ | $0.9272952180016122$ | $1.6094379124341003+0.9272952180016122\,i$ | $8.9\times10^{-16}$ |
| $-1$ | $0$ | $\pi$ | $\pi i$ | $1.2\times10^{-16}$ |
| $i$ | $0$ | $\pi/2$ | $\frac{\pi}{2}i$ | $6.1\times10^{-17}$ |
| $1+i$ | $0.3465735902799727$ | $\pi/4$ | $0.3465735902799727+0.7853981633974483\,i$ | $2.2\times10^{-16}$ |
| $-1-i$ | $0.3465735902799727$ | $-3\pi/4$ | $0.3465735902799727-2.356194490192345\,i$ | $2.2\times10^{-16}$ |

The third line is the pure rotation $i$, with zero logarithmic scale. The second and fifth lines show the two sides of the branch cut: $-1$ is on the cut with principal angle $\pi$, and $-1-i$ is below it with principal angle $-3\pi/4$.

### The Kernel and the Non-Uniqueness

The kernel of the exponential is the lattice $2\pi i\mathbb{Z}$:

$$
\exp(2\pi i) = 1-2.4\times10^{-16}\,i, \qquad \exp(4\pi i) = 1-4.9\times10^{-16}\,i.
$$

The error is machine precision. The element $-1$ has the logarithms $i(\pi+2\pi k)$; the two with angle in $[-\pi,\pi]$ are $i\pi$ and $-i\pi$:

$$
\exp(i\pi) = -1+1.2\times10^{-16}\,i, \qquad \exp(-i\pi) = -1-1.2\times10^{-16}\,i,
$$

and only $i\pi$ lies in the principal strip. The exponential polar decomposition of $-1$ is therefore $(-1)_{\log} = i\pi$ on the principal branch, and $(-1)_{\log} = -i\pi$ on the other branch. This is the opposite of the split case, where the kernel is $\{0\}$ and $-1$ has no logarithm at all.

## The Exponential Coordinates

### The Coordinate Lines

Write $Q = \exp(\ln r+i\theta)$. The vertical lines $\ln r = \ln r_0$ map to the circles

$$
\lvert Q\rvert = r_0,
$$

and the horizontal lines $\theta = \theta_0$ map to the rays

$$
\arg Q = \theta_0 \pmod{2\pi}.
$$

The strip $-\pi<\theta\le\pi$ is a fundamental domain: its translates by $2\pi i$ tile the plane, and the exponential identifies the two edges. The real part $\ln r$ is the logarithmic modulus, the imaginary part $\theta$ is the angle, and the exponential turns the flat strip into the punctured plane.

### The Conformal Factor

The derivative of the exponential is multiplication by $\exp(Q_{\log})$, so the pullback of the Euclidean metric is

$$
(\exp^* g)_{Q_{\log}} = r^2\bigl(d(\ln r)^2+d\theta^2\bigr) = dr^2+r^2\,d\theta^2.
$$

The exponential is conformal with scale factor $r = \lvert Q\rvert$. Its Jacobian determinant is $r^2 = N(Q)$, and the area element is

$$
dA = r^2\,d(\ln r)\,d\theta = r\,dr\,d\theta.
$$

The area of the image of a rectangle $[\ln r_1,\ln r_2]\times[\theta_1,\theta_2]$ with $0\le\theta_2-\theta_1\le2\pi$ is

$$
\int_{\ln r_1}^{\ln r_2}\int_{\theta_1}^{\theta_2} r^2\,d\theta\,d(\ln r) = \frac{1}{2}\bigl(r_2^2-r_1^2\bigr)(\theta_2-\theta_1),
$$

the area of the annular sector between the radii $r_1$ and $r_2$ and the angle $\theta_2-\theta_1$. The formula is exact; it is the change-of-variables formula for the exponential in polar coordinates.

### The Harmonic Reading

The real part $\ln r = \ln\lvert Q\rvert$ is harmonic on $\mathbb{C}^\times$, and the imaginary part $\theta = \arg Q$ is harmonic on the cut plane. The complex coordinate $\ln r+i\theta$ is the local holomorphic coordinate supplied by the principal logarithm, and the exponential is its inverse. The logarithm is not global because the angle is not; the obstruction is the kernel $2\pi i\mathbb{Z}$.

## Summary

Every nonzero complex number has exactly one exponential polar decomposition $Q = \exp(\ln r)\exp(i\theta)$ with

$$
r = \lvert Q\rvert = \sqrt{(\operatorname{Re}Q)^2+(\operatorname{Im}Q)^2}>0, \qquad \theta = \operatorname{Arg}Q = \operatorname{atan2}(\operatorname{Im}Q,\operatorname{Re}Q)\in(-\pi,\pi],
$$

namely the modulus and the principal angle of $Q$. The exponent is the principal logarithm $Q_{\log} = \ln\lvert Q\rvert+i\operatorname{Arg}Q$, the scale is $\exp(\ln r) = \lvert Q\rvert$, and the unit factor is $\exp(i\theta) = Q/\lvert Q\rvert$. Because $\mathbb{C}$ is commutative the two exponentials amalgamate into one, $Q = \exp(\ln\lvert Q\rvert+i\operatorname{Arg}Q)$.

The exponential is a surjective homomorphism from $(\mathbb{C},+)$ onto $(\mathbb{C}^\times,\cdot)$ with kernel $2\pi i\mathbb{Z}$. The logarithm is unique modulo that kernel, and the principal strip $-\pi<\theta\le\pi$ is a fundamental domain on which the exponential is a bijection onto $\mathbb{C}^\times$. The quotient is $\mathbb{C}^\times\cong\mathbb{C}/2\pi i\mathbb{Z}$, the product of a line and a circle.

The matrix picture is the exponential of the conformal matrix: $M_Q = \exp(\ln r\,I+\theta J) = rR_\theta$, with the matrix logarithm $\ln r\,I+\theta J$ on the principal branch, the angle defined modulo $2\pi$. The derivative is multiplication by $\exp(Q_{\log})$, the Jacobian determinant is $N(Q)$, and the exponential is conformal with scale $\lvert Q\rvert$. The general polar decomposition $B = PU$ of an invertible real matrix specialises to $P = rI$ and $U = R_\theta$.

The exponential form is the third of the three polar decompositions of $\mathbb{C}$. The modulus–unit form is global, unique and algebraic; the rational-chart form is the rational Cayley chart, local and missing the negative real axis; the exponential form is global and transcendental, and it is unique once the principal representative of the angle is chosen, the exponent being unique modulo the kernel. The three are presentations of the same factorisation.

## Summary of Notation

| symbol | meaning |
|---|---|
| $Q = a+ib$ | a complex number, $a$ the real part, $b$ the imaginary part |
| $N(Q) = Q\bar Q = a^2+b^2$ | the norm, positive definite |
| $r = \lvert Q\rvert = \sqrt{N(Q)}$ | the modulus, a positive real |
| $\ln r$ | the logarithmic scale |
| $\theta$ | the angle, a class in $\mathbb{R}/2\pi\mathbb{Z}$ |
| $\theta = \operatorname{Arg}Q$ | the principal angle, $\operatorname{atan2}(b,a)\in(-\pi,\pi]$ |
| $s = -\tan(\theta/2)$ | the rational-chart coordinate of the unit factor |
| $Q_{\log} = \ln r+i\theta$ | the exponent, a logarithm of $Q$ |
| $\operatorname{Log}Q = \ln\lvert Q\rvert+i\operatorname{Arg}Q$ | the principal logarithm |
| $\exp : Q_{\log} \mapsto \sum_n Q_{\log}^n/n!$ | the exponential, entire and a homomorphism |
| $\ker\exp = 2\pi i\mathbb{Z}$ | the kernel of the exponential |
| $\mathrm{U}(1)$ | the unit circle, the group of unit factors |
| $J$ | the complex structure, multiplication by $i$, $J^2 = -I$ |
| $M_Q = aI+bJ$ | the conformal matrix of multiplication by $Q$ |

## Further Reading

- Leonhard Euler, *Introductio in analysin infinitorum* (Bousquet, Lausanne, 1748), for the exponential form of a complex number and the trigonometric functions.
- Reinhold Remmert, *Theory of Complex Functions* (Springer, 1991), for the argument, the logarithm and the polar form on the cut plane.
- Walter Rudin, *Real and Complex Analysis*, 3rd edition (McGraw-Hill, 1987), for the exponential homomorphism, its kernel and the polar decomposition.
- Tristan Needham, *Visual Complex Analysis* (Oxford University Press, 1997), for the exponential as a map of the plane and the circle as a one-parameter group.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd edition 2015), for the matrix exponential and the matrix logarithm.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 1985), for the polar decomposition of an invertible matrix.
