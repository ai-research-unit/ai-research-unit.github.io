# __Exponential Polar Decomposition of Complex Numbers__

## Introduction

This article treats the **exponential polar decomposition** of a nonzero complex number: the writing

$$
Q = \exp(Q_{\log}), \qquad Q_{\log} = \ln r + i\theta,
$$

with $r>0$ the modulus, $\theta$ the angle, $\ln r$ the logarithmic scale, and $r\exp(i\theta)$ the product of the scale and the unit factor. The exponential and the logarithm are defined and studied in *Complex Special Functions*, §*The Complex Exponential and Logarithm*; this article does not define them again. It uses only the group law $\exp(Q_{1\log}+Q_{2\log})=\exp(Q_{1\log})\exp(Q_{2\log})$ and the description of the logarithms of $Q$ from that article.

The decomposition is the exponential form of the modulus–unit polar decomposition of *Modulus–Unit Polar Decomposition of Complex Numbers*, which writes every nonzero complex number as

$$
Q = r\,u, \qquad r \in \mathbb{R}, \quad r > 0, \qquad u \in \mathbb{C}, \quad \langle u\rangle_{*} = 1,
$$

with $r$ the modulus and $u$ the unit factor. The unit factor is written $u=\exp(i\theta)$, and $r=\sqrt{\langle Q\rangle_{*}}$. The rational-chart form of *Rational-Chart Polar Decomposition of Complex Numbers* is the third presentation. Since $\mathbb{C}$ is commutative, the scale and the unit factor are not two independent exponentials: their product is the single exponential $\exp(Q_{\log})$.

The article states the decomposition and computes its data (§*The Decomposition*), identifies the exponent with the logarithm and separates the principal logarithm from the general one (§*The Logarithm*), proves existence and uniqueness (§*Existence and Uniqueness*), gives examples (§*Worked Examples*), and then treats the matrix picture (§*The Matrix Picture*), the comparison with the two other polar forms (§*The Three Polar Decompositions*) and the exponential coordinates (§*The Exponential Coordinates*).

The symbols are those of *Complex Algebra*, *Complex Norm and Invertibility* and *Conventions in Mathematics*. Every numerical value displayed below was recomputed in double precision.

## The Decomposition

### The Data

Let $Q=q+iq'\neq0$. The **modulus** and the **principal angle** are

$$
r=\sqrt{\langle Q\rangle_{*}}=\sqrt{q^2+q'^2}>0, \qquad
\theta=\operatorname{Arg}Q=\operatorname{atan2}(q',q)\in(-\pi,\pi].
$$

Euler's formula, $\exp(i\theta)=\cos\theta+i\sin\theta$, and $r=\exp(\ln r)$ give

$$
Q=r(\cos\theta+i\sin\theta)=r\exp(i\theta)=\exp(Q_{\log}), \qquad Q_{\log}=\ln r+i\theta.
$$

The three expressions are the same number. The middle one is the modulus–unit form; the last one is the exponential polar decomposition.

**Definition.** An **exponential polar decomposition** of $Q\neq0$ is a writing

$$
Q=\exp(Q_{\log}), \qquad Q_{\log}=\ln r+i\theta, \quad r>0,\quad \theta\in\mathbb{R},
$$

equivalently $Q=\exp(\ln r)\exp(i\theta)$, in which $\exp(\ln r)=r$ is the **scale** and $\exp(i\theta)$ is the **unit factor**. The **exponent** is the logarithm $Q_{\log}$, with coordinates $q_{\log}=\ln r$ and $q'_{\log}=\theta$.

The angle is defined modulo $2\pi$, because $\exp(i(\theta+2\pi k))=\exp(i\theta)$. The pair $(r,\exp(i\theta))$ is the modulus–unit pair. The exponent $Q_{\log}$ is a logarithm of $Q$ in the sense of §*The Logarithm*.

### The Two Factors

The factors are read from $Q$ directly:

$$
\exp(\ln r)=r=\sqrt{\langle Q\rangle_{*}}, \qquad
\exp(i\theta)=\frac{Q}{r}=\frac{Q}{\sqrt{\langle Q\rangle_{*}}}.
$$

The first is positive real; the second has modulus one. They recover the modulus–unit decomposition. The table records the two factors.

| factor | formula | range | logarithm | parameter |
|---|---|---|---|---|
| scale | $\exp(\ln r)=r$ | $(0,\infty)$ | $q_{\log}=\ln r$ | $r>0$ |
| unit factor | $\exp(i\theta)=Q/r$ | $\mathrm{U}(1)$ | $iq'_{\log}=i\theta$ | $\theta\in\mathbb{R}$ modulo $2\pi$ |

The real dimensions are $1$ and $1$, and they add to the real dimension $2$ of $\mathbb{C}$. The scale is non-compact; the unit factor is compact. This is the compact case of the polar decomposition.

### One Exponential

The product of the two factors is one exponential:

$$
Q=\exp(\ln r)\exp(i\theta)=\exp(Q_{\log}).
$$

The amalgamation uses the group law and the fact that $\ln r$ is real and central in $\mathbb{C}$. It is not a property of a general algebra: in a noncommutative algebra the two exponents need not commute, and the product need not be a single exponential. The polar word of *Modulus–Unit Polar Decomposition of Biquaternions* is the counterexample.

The word **polar** names the two factors, not two independent exponentials. The single exponent $Q_{\log}=\ln r+i\theta$ carries both the scale and the angle.

### Existence and Uniqueness

**Theorem.** Every $Q\neq0$ has exactly one exponential polar decomposition with the principal angle,

$$
Q=\exp(\ln r)\exp(i\theta), \qquad r>0,\quad \theta\in(-\pi,\pi],
$$

namely

$$
r=\sqrt{\langle Q\rangle_{*}}, \qquad \theta=\operatorname{Arg}Q,
$$

and exponent the principal logarithm $Q_{\log}=\operatorname{Log}Q=\ln r+i\theta$.

**Existence.** The data above give $r>0$ and $\theta\in(-\pi,\pi]$, and Euler's formula gives the identity.

**Uniqueness.** Suppose $\exp(\ln r_1)\exp(i\theta_1)=\exp(\ln r_2)\exp(i\theta_2)$ with both angles in $(-\pi,\pi]$. Taking moduli gives $r_1=r_2$. Dividing gives $\exp(i(\theta_1-\theta_2))=1$, so $\theta_1-\theta_2\in2\pi\mathbb{Z}$. The difference lies in $(-2\pi,2\pi)$, so it is $0$. Hence $\theta_1=\theta_2$.

Without the restriction on $\theta$ the exponent is not unique: the same pair of factors is written with every logarithm $Q_{\log}+2\pi i k$. The factors are unique; the exponent is unique only modulo the kernel. This distinction is the subject of §*The Logarithm*.

The data of the principal decomposition are collected in one table.

| datum | formula |
|---|---|
| element | $Q=q+iq'\neq0$ |
| modulus | $r=\sqrt{q^2+q'^2}$ |
| angle | $\theta=\operatorname{atan2}(q',q)\in(-\pi,\pi]$ |
| exponent | $Q_{\log}=\operatorname{Log}Q=\ln r+i\theta$ |
| scale | $\exp(\ln r)=r$ |
| unit factor | $\exp(i\theta)=Q/r$ |
| reconstruction | $Q=\exp(Q_{\log})=r\exp(i\theta)$ |

### The Group Law

Because the exponential is a homomorphism, multiplication adds the exponents. In the coordinates $(q_{\log},q'_{\log})=(\ln r,\theta)$,

$$
(\ln r_1,\theta_1)*(\ln r_2,\theta_2)
=\bigl(\ln(r_1r_2),\ \theta_1+\theta_2 \bmod 2\pi\bigr).
$$

The logarithmic scale and the angle do not mix. The group of units is the product of a line and a circle.

## The Logarithm

### The General Logarithm

**Recall.** From *Complex Special Functions*, §*The Complex Logarithm*, a **logarithm** of $Q\neq0$ is a complex number $Q_{\log}$ with $\exp(Q_{\log})=Q$.

Let $Q_{\log}$ be one logarithm of $Q$. Every other logarithm differs from it by an element of the kernel $\ker\exp=2\pi i\mathbb{Z}$, because the exponential is a homomorphism. Hence the logarithms of $Q$ are exactly

$$
Q_{\log}+2\pi i k, \qquad k\in\mathbb{Z}.
$$

Choosing the principal angle gives the family

$$
Q_{\log}=\ln\sqrt{\langle Q\rangle_{*}}+i\bigl(\operatorname{Arg}Q+2\pi k\bigr),
\qquad k\in\mathbb{Z}.
$$

In coordinates,

$$
Q_{\log}=\tfrac12\ln(q^2+q'^2)+i\bigl(\operatorname{atan2}(q',q)+2\pi k\bigr).
$$

The two coordinates have different roles.

| coordinate | formula | role |
|---|---|---|
| $q_{\log}=\operatorname{Re}Q_{\log}$ | $\tfrac12\ln(q^2+q'^2)$ | logarithmic scale, unique |
| $q'_{\log}=\operatorname{Im}Q_{\log}$ | $\operatorname{atan2}(q',q)+2\pi k$ | angle, one value for each $k$ |

The real part is unique; it is $\ln r$. The imaginary part is one number for each integer $k$, and the numbers differ by $2\pi$. Hence every $Q\neq0$ has a logarithm, and no logarithm is unique. The ambiguity is exactly the kernel $2\pi i\mathbb{Z}$ of the exponential.

For example, $Q=3+4i$ has $r=5$ and $\theta=\operatorname{atan2}(4,3)=0.9272952180016122$. Its logarithms are

$$
Q_{\log}=1.6094379124341003+i(0.9272952180016122+2\pi k), \qquad k\in\mathbb{Z}.
$$

### The Principal Logarithm

Single-valuedness is obtained by restricting the exponent to the **principal strip**

$$
S=\{\ln r+i\theta:r>0,\ -\pi<\theta\le\pi\}.
$$

The exponential maps $S$ bijectively onto $\mathbb{C}^\times$, and its inverse is the **principal logarithm**

$$
\operatorname{Log}Q=\ln\sqrt{\langle Q\rangle_{*}}+i\operatorname{Arg}Q,
\qquad -\pi<\operatorname{Arg}Q\le\pi.
$$

This is the exponent of the principal decomposition. The proof of the bijection is in *Complex Special Functions*, §*The Principal Logarithm*; the content here is the reading as a decomposition.

The inverse is discontinuous on the negative real axis, the **branch cut**. On the cut the principal value is still defined and still exponentiates to $Q$; it is continuity, not the identity, that fails. The strip is a fundamental domain for the translations by $2\pi i\mathbb{Z}$.

| $Q$ | $r$ | $\operatorname{Arg}Q$ | $\operatorname{Log}Q$ |
|---|---|---|---|
| $3+4i$ | $5$ | $0.9272952180016122$ | $1.6094379124341003+0.9272952180016122\,i$ |
| $-1$ | $1$ | $\pi$ | $\pi i$ |
| $i$ | $1$ | $\pi/2$ | $\tfrac{\pi}{2}i$ |
| $1+i$ | $\sqrt{2}$ | $\pi/4$ | $0.3465735902799727+0.7853981633974483\,i$ |
| $-1-i$ | $\sqrt{2}$ | $-3\pi/4$ | $0.3465735902799727-2.356194490192345\,i$ |

The fifth line shows the branch convention: the argument of $-1-i$ is $-3\pi/4$, not $5\pi/4$, because the principal argument lies in $(-\pi,\pi]$.

### The Kernel and the Fibre

The fibre of the exponential over $Q\neq0$ is the coset

$$
\exp^{-1}(Q)=\operatorname{Log}Q+2\pi i\mathbb{Z}.
$$

The kernel is

$$
\ker\exp=2\pi i\mathbb{Z},
$$

and the first isomorphism theorem gives

$$
\mathbb{C}^\times\cong\mathbb{C}/2\pi i\mathbb{Z}
$$

as groups and as real manifolds. The quotient is a cylinder: one line $\ln r$ and one circle $\theta\bmod2\pi$. The exponential coordinates are global on the quotient; the principal strip is a fundamental domain.

## Worked Examples

### A Generic Complex Number

Take $Q=3+4i$. Then

$$
r=\sqrt{9+16}=5, \qquad \ln r=1.6094379124341003, \qquad
\theta=\arctan\frac{4}{3}=0.9272952180016122,
$$

and

$$
Q_{\log}=\ln r+i\theta=1.6094379124341003+0.9272952180016122\,i.
$$

The reconstruction is

$$
\exp(Q_{\log})=3+3.999999999999999\,i,
$$

with error $8.9\times10^{-16}$ in the Euclidean modulus.

### A Table of Examples

| $Q$ | $r$ | $\theta=\operatorname{Arg}Q$ | $Q_{\log}$ | $\sqrt{\langle\exp Q_{\log}-Q\rangle_{*}}$ |
|---|---|---|---|---|
| $3+4i$ | $5$ | $0.9272952180016122$ | $1.6094379124341003+0.9272952180016122\,i$ | $8.9\times10^{-16}$ |
| $-1$ | $1$ | $\pi$ | $\pi i$ | $1.2\times10^{-16}$ |
| $i$ | $1$ | $\pi/2$ | $\tfrac{\pi}{2}i$ | $6.1\times10^{-17}$ |
| $1+i$ | $\sqrt{2}$ | $\pi/4$ | $0.3465735902799727+0.7853981633974483\,i$ | $2.2\times10^{-16}$ |
| $-1-i$ | $\sqrt{2}$ | $-3\pi/4$ | $0.3465735902799727-2.356194490192345\,i$ | $2.2\times10^{-16}$ |

The second and fifth lines show the two sides of the branch cut: $-1$ is on the cut with principal angle $\pi$, and $-1-i$ is below it with principal angle $-3\pi/4$.

### The Kernel and the Branch

The kernel is the lattice $2\pi i\mathbb{Z}$:

$$
\exp(2\pi i)=1-2.4\times10^{-16}\,i, \qquad
\exp(4\pi i)=1-4.9\times10^{-16}\,i.
$$

The element $-1$ has the logarithms $i(\pi+2\pi k)$. The two with angle in $[-\pi,\pi]$ are $i\pi$ and $-i\pi$:

$$
\exp(i\pi)=-1+1.2\times10^{-16}\,i, \qquad
\exp(-i\pi)=-1-1.2\times10^{-16}\,i,
$$

and only $i\pi$ lies in the principal strip. The principal logarithm of $-1$ is therefore $\pi i$; the other branch gives $-\pi i$.

## The Matrix Picture

### The Exponential of a Conformal Matrix

In the real basis $\{1,i\}$ a complex number is $Q=q+iq'$, and multiplication by $Q$ is the matrix

$$
M_Q=qI+q'J, \qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}, \qquad J^2=-I.
$$

The matrices $I$ and $J$ commute, so the exponential splits:

$$
\exp(xI+yJ)=\exp(xI)\exp(yJ)=\exp(x)\bigl(\cos y\,I+\sin y\,J\bigr).
$$

The exponential polar decomposition of $M_Q$ is therefore

$$
M_Q=\exp\bigl(\ln r\,I+\theta J\bigr)
=r\bigl(\cos\theta\,I+\sin\theta\,J\bigr)=rR_\theta,
$$

with $r=\sqrt{\langle Q\rangle_{*}}$ and $\theta=\operatorname{Arg}Q$. The positive factor is the scalar $rI$, and the orthogonal factor is the rotation $R_\theta\in SO(2)$. This is the polar decomposition of the conformal matrix: the positive definite part is a scalar, because the only symmetric positive definite matrices in the family $aI+bJ$ are the positive scalar multiples of the identity.

Every invertible real $2\times2$ matrix $B$ has a unique polar decomposition $B=PU$, with $P$ symmetric positive definite and $U$ orthogonal. The factors are $P=(BB^{\mathsf T})^{1/2}$ and $U=P^{-1}B$. For $B=M_Q$ they collapse to $P=rI$ and $U=R_\theta$, because $M_Q$ is conformal. The general theorem is the same splitting without the conformal restriction; the positive factor then carries the two singular values instead of the single scale $r$.

### The Matrix Logarithm and the Derivative

The matrix logarithm of $M_Q$ is

$$
\log M_Q=\ln r\,I+\theta J
$$

on the principal branch. Adding $2\pi kJ$ gives another logarithm, because $\exp(2\pi kJ)=I$. For $Q$ non-real the centraliser of $M_Q$ is spanned by $I$ and $J$, so this is the full ambiguity of the angle. The eigenvalues of $M_Q$ are $q\pm iq'$, neither zero when $Q\neq0$, and the real logarithm exists; for $Q$ real and negative the principal one is $\ln\sqrt{\langle Q\rangle_{*}}\,I+\pi J$.

The exponential is a homomorphism, so its derivative at $Q_{\log}$ is multiplication by $\exp(Q_{\log})$:

$$
d\exp_{Q_{\log}}=\exp(Q_{\log})\,\mathrm{id}.
$$

It is invertible, so the exponential is a local diffeomorphism. In the real coordinates $(\ln r,\theta)=(q_{\log},q'_{\log})$ the Jacobian determinant is

$$
\det d\exp_{Q_{\log}}=\lvert\exp(Q_{\log})\rvert^2=r^2=\langle Q\rangle_{*}.
$$

The exponential is conformal: it multiplies lengths by $r$ and preserves angles and orientation.

## The Three Polar Decompositions

### The Three Forms

| decomposition | formula | parameters | domain | uniqueness | functions | group reading |
|---|---|---|---|---|---|---|
| modulus–unit | $Q=ru$ | $r>0$, $u\in\mathrm{U}(1)$ | $\mathbb{C}^\times$ | unique | square root | $\mathbb{R}_{>0}\times\mathrm{U}(1)$ |
| rational-chart | $Q=r\dfrac{1-is}{1+is}$ | $r>0$, $s\in\mathbb{R}$ | $\mathbb{C}\setminus(-\infty,0]$ | unique on the chart | rational | $\mathbb{R}_{>0}\times\mathbb{R}$, local |
| exponential | $Q=\exp(Q_{\log})$ | $r>0$, $\theta\in\mathbb{R}$ modulo $2\pi$ | $\mathbb{C}^\times$ | exponent modulo $2\pi i$; unique with the principal angle | exponential and logarithm | $\mathbb{C}/2\pi i\mathbb{Z}$ |

### The Modulus–Unit Form

The modulus–unit form is $Q=ru$ with $r=\sqrt{\langle Q\rangle_{*}}$ and $u=Q/\sqrt{\langle Q\rangle_{*}}$. It is unique on the whole of $\mathbb{C}^\times$, it uses the square root of the norm, and it is the product decomposition of the group of units. It is the form developed in *Modulus–Unit Polar Decomposition of Complex Numbers*.

### The Rational-Chart Form

The rational-chart form writes the unit factor by the Cayley chart of the circle. For $s\in\mathbb{R}$,

$$
u(s)=\frac{1-is}{1+is}=\frac{1-s^2}{1+s^2}-i\frac{2s}{1+s^2},
$$

and $s\mapsto u(s)$ is a bijection from $\mathbb{R}$ onto $\mathrm{U}(1)\setminus\{-1\}$. It is rational, uses no transcendental function, and misses the single point $u=-1$, the unit factor of the negative real axis. The decomposition $Q=r\,u(s)$ is therefore a rational chart, not a global decomposition.

### The Change of Coordinates

Comparing $u(s)=(1-is)/(1+is)$ with $u=\exp(i\theta)$ and using the half-angle identity gives

$$
\frac{1-is}{1+is}=\exp\bigl(-2i\arctan s\bigr),
$$

so the passage between the rational coordinate and the angle is

$$
s=-\tan\frac{\theta}{2}, \qquad \theta=-2\arctan s.
$$

The map $s\mapsto\theta$ sends $\mathbb{R}$ onto $(-\pi,\pi)$, and $s\to\pm\infty$ corresponds to $\theta\to\mp\pi$. The cut $\theta=\pi$ is the negative real axis; its unit factor is $-1$, the single point the rational chart misses, and it is also the point at which the rational coordinate escapes to infinity.

### What the Comparison Says

The three forms are three presentations of one factorisation. The modulus–unit form is coordinate-free; the rational form puts a local rational coordinate on the circle; the exponential form puts a global transcendental coordinate on it. The exponential form is the only one in which the group law is addition. The modulus–unit form is the only one that is algebraic and global. The rational-chart form is the only one that is rational and local.

They are three presentations of the complex member of the eight algebras whose polar decompositions are compared in *Comparison of the Polar Decomposition*. In a noncommutative algebra the exponential of a sum is not the product of the exponentials, the exponents need not commute, and the amalgamation into one exponential fails.

## The Exponential Coordinates

### The Coordinate Lines

Write $Q=\exp(Q_{\log})$ with $Q_{\log}=\ln r+i\theta$. The vertical lines $\ln r=\ln r_0$ map to the circles

$$
\sqrt{\langle Q\rangle_{*}}=r_0,
$$

and the horizontal lines $\theta=\theta_0$ map to the rays

$$
\arg Q=\theta_0 \pmod{2\pi}.
$$

The strip $-\pi<\theta\le\pi$ is a fundamental domain: its translates by $2\pi i$ tile the plane, and the exponential identifies the two edges. The real part $q_{\log}=\ln r$ is the logarithmic scale, the imaginary part $q'_{\log}=\theta$ is the angle, and the exponential turns the flat strip into the punctured plane.

### The Conformal Factor

The derivative of the exponential is multiplication by $\exp(Q_{\log})$, so the pullback of the Euclidean metric is

$$
(\exp^* g)_{Q_{\log}}=r^2\bigl(d(\ln r)^2+d\theta^2\bigr)=dr^2+r^2\,d\theta^2.
$$

The exponential is conformal with scale factor $r=\sqrt{\langle Q\rangle_{*}}$. Its Jacobian determinant is $r^2=\langle Q\rangle_{*}$, and the area element is

$$
dA=r^2\,d(\ln r)\,d\theta=r\,dr\,d\theta.
$$

The area of the image of a rectangle $[\ln r_1,\ln r_2]\times[\theta_1,\theta_2]$ with $0\le\theta_2-\theta_1\le2\pi$ is

$$
\int_{\ln r_1}^{\ln r_2}\int_{\theta_1}^{\theta_2}r^2\,d\theta\,d(\ln r)
=\frac{1}{2}\bigl(r_2^2-r_1^2\bigr)(\theta_2-\theta_1),
$$

the area of the annular sector between the radii $r_1$ and $r_2$ and the angle $\theta_2-\theta_1$.

### The Harmonic Reading

The real part $q_{\log}=\ln r$ is harmonic on $\mathbb{C}^\times$, and the imaginary part $q'_{\log}=\theta$ is harmonic on the cut plane. The complex coordinate $Q_{\log}=\ln r+i\theta$ is the local holomorphic coordinate supplied by the principal logarithm, and the exponential is its inverse. The logarithm is not global because the angle is not; the obstruction is the kernel $2\pi i\mathbb{Z}$.

## Summary

Every nonzero complex number has exactly one exponential polar decomposition with the principal angle,

$$
Q=\exp(\ln r)\exp(i\theta), \qquad
r=\sqrt{\langle Q\rangle_{*}}=\sqrt{q^2+q'^2}>0, \qquad
\theta=\operatorname{Arg}Q=\operatorname{atan2}(q',q)\in(-\pi,\pi],
$$

namely the modulus and the principal angle of $Q$. The exponent is the principal logarithm $Q_{\log}=\operatorname{Log}Q=\ln\sqrt{\langle Q\rangle_{*}}+i\operatorname{Arg}Q$, the scale is $\exp(\ln r)=r$, and the unit factor is $\exp(i\theta)=Q/r$. Because $\mathbb{C}$ is commutative the two exponentials amalgamate into one, $Q=\exp(Q_{\log})$.

The general logarithms of $Q$ are $Q_{\log}+2\pi i k$ with $k\in\mathbb{Z}$; the ambiguity is the kernel $2\pi i\mathbb{Z}$. The principal strip $-\pi<\theta\le\pi$ is a fundamental domain on which the exponential is a bijection onto $\mathbb{C}^\times$, and the quotient is $\mathbb{C}^\times\cong\mathbb{C}/2\pi i\mathbb{Z}$, the product of a line and a circle.

The matrix picture is the exponential of the conformal matrix: $M_Q=\exp(\ln r\,I+\theta J)=rR_\theta$, with matrix logarithm $\ln r\,I+\theta J$ on the principal branch, the angle defined modulo $2\pi$. The derivative is multiplication by $\exp(Q_{\log})$, the Jacobian determinant is $\langle Q\rangle_{*}$, and the exponential is conformal with scale $\sqrt{\langle Q\rangle_{*}}$.

The exponential form is the third of the three polar decompositions of $\mathbb{C}$. The modulus–unit form is global, unique and algebraic; the rational-chart form is the rational Cayley chart, local and missing the negative real axis; the exponential form is global and transcendental, and it is unique once the principal representative of the angle is chosen, the exponent being unique modulo the kernel. The three are presentations of the same factorisation.

## Summary of Notation

| symbol | meaning |
|---|---|
| $Q=q+iq'$ | a complex number, $q$ the real part, $q'$ the imaginary part |
| $\langle Q\rangle_{*}=Q\bar Q=q^2+q'^2$ | the norm, positive definite |
| $r=\sqrt{\langle Q\rangle_{*}}$ | the modulus, a positive real |
| $\ln r$ | the logarithmic scale |
| $\theta$ | the angle, defined modulo $2\pi$; $\operatorname{Arg}Q=\operatorname{atan2}(q',q)\in(-\pi,\pi]$ is the principal representative |
| $q_{\log}=\operatorname{Re}Q_{\log}$, $q'_{\log}=\operatorname{Im}Q_{\log}$ | the logarithmic scale and the angle |
| $Q_{\log}=\ln r+i\theta$ | the exponent, a logarithm of $Q$; the principal one is $\operatorname{Log}Q$ |
| $\operatorname{Log}Q=\ln\sqrt{\langle Q\rangle_{*}}+i\operatorname{Arg}Q$ | the principal logarithm |
| $\exp$ | the exponential, defined in *Complex Special Functions* |
| $\ker\exp=2\pi i\mathbb{Z}$ | the kernel of the exponential |
| $\mathrm{U}(1)$ | the unit circle, the group of unit factors |
| $s=-\tan(\theta/2)$ | the rational-chart coordinate of the unit factor |
| $J$ | the complex structure, multiplication by $i$, $J^2=-I$ |
| $M_Q=qI+q'J$ | the conformal matrix of multiplication by $Q$ |

## Further Reading

- Leonhard Euler, *Introductio in analysin infinitorum* (Bousquet, Lausanne, 1748), for the exponential form of a complex number and the trigonometric functions.
- Reinhold Remmert, *Theory of Complex Functions* (Springer, 1991), for the argument, the logarithm and the polar form on the cut plane.
- Walter Rudin, *Real and Complex Analysis*, 3rd edition (McGraw-Hill, 1987), for the exponential homomorphism, its kernel and the polar decomposition.
- Tristan Needham, *Visual Complex Analysis* (Oxford University Press, 1997), for the exponential as a map of the plane and the circle as a one-parameter group.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd edition 2015), for the matrix exponential and the matrix logarithm.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 1985), for the polar decomposition of an invertible matrix.
