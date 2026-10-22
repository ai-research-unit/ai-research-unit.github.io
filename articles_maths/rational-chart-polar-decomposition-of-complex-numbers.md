# __Rational-Chart Polar Decomposition of Complex Numbers__

## Introduction

The modulus–unit polar decomposition of *Modulus–Unit Polar Decomposition of Complex Numbers* writes every nonzero complex number as

$$
Q = r\,u, \qquad r = \sqrt{\langle Q\rangle_{*}} > 0, \qquad \langle u\rangle_{*} = 1,
$$

with $r$ the modulus and $u$ the unit factor. That article proves the pair unique and treats $u$ as a point of the unit circle. It chooses no coordinate on the circle: the unit factor is named by the equation $\langle u\rangle_{*}=1$, not by a number.

This article names it. For a real number $s$ put

$$
u(s) = \frac{1-is}{1+is},
$$

and write

$$
Q = r\,u(s) = r\,\frac{1-is}{1+is}.
$$

Nothing in the decomposition changes. The number $r$ is still the modulus, the element $u = u(s)$ is still the same unit factor, and the pair $(r,u)$ is still unique. The only new object is the real number $s$, which replaces the point of the circle by a coordinate on a line.

The chart is rational: $u(s)$ and its inverse are ratios of polynomials, and no transcendental function occurs. The price is locality. As $\lvert s\rvert$ grows the unit $u(s)$ approaches $-1$ without attaining it, so the one unit factor that is missed is $-1$, the unit factor of every negative real number. The decomposition therefore holds on the plane cut along the negative real axis, and it fails on the cut.

The plan is as follows. The modulus–unit form is recalled (§*The Modulus–Unit Form Recalled*), the chart and its inverse are defined (§*The Chart*, §*The Inverse*), and the chart is proved a bijection (§*The Bijection*). The decomposition is then stated and proved (§*The Rational-Chart Decomposition*), the group law in the coordinate is computed (§*The Group Law*), the covering of the circle by two charts and the cost of rationality are described (§*Covering the Circle and the Price of Locality*), and the matrix picture (§*The Matrix Picture*) and worked examples (§*Worked Examples*) close the article.

The symbols are those of *Complex Algebra* and *Complex Norm and Invertibility*, and the conventions are those of *Conventions in Mathematics*. The notation is collected in §*Summary of Notation*.

Every numerical value displayed below was recomputed in double precision.

## The Unit Factor and Its Chart

### The Modulus–Unit Form Recalled

For a complex number $Q$ the norm is

$$
\langle Q\rangle_{*} = Q\bar{Q} = q^2+q'^2,
$$

which is positive off the origin. The modulus is $r = \sqrt{\langle Q\rangle_{*}}$, a positive real with no sign choice, and the unit factor is

$$
u = \frac{Q}{r}, \qquad \langle u\rangle_{*} = \frac{\langle Q\rangle_{*}}{r^2} = 1.
$$

The unit factor lies on the unit circle $\mathrm{U}(1) = \{u : \langle u\rangle_{*}=1\}$. The pair $(r,u)$ is unique: taking norms in $Q = ru$ forces $r = \sqrt{\langle Q\rangle_{*}}$, and then $u = Q/r$.

This is where the modulus–unit article stops. The present article adds one object, the real number $s$, and changes nothing else.

### The Chart

**Definition.** For $s \in \mathbb{R}$ the **chart** is

$$
u(s) = \frac{1-is}{1+is} = \frac{1-s^2}{1+s^2} - i\,\frac{2s}{1+s^2}.
$$

The real and imaginary parts are rational functions of $s$, and their squares sum to one:

$$
\left(\frac{1-s^2}{1+s^2}\right)^2 + \left(\frac{2s}{1+s^2}\right)^2
= \frac{(1-s^2)^2+4s^2}{(1+s^2)^2}
= \frac{(1+s^2)^2}{(1+s^2)^2} = 1.
$$

Every $u(s)$ is therefore a point of the circle. The denominator $1+is$ never vanishes.

Three values fix the orientation of the chart:

$$
u(0) = 1, \qquad u(1) = \frac{1-i}{1+i} = -i, \qquad u(-1) = \frac{1+i}{1-i} = i.
$$

The chart almost covers the circle, but not quite. If $u(s) = -1$ then $1-is = -1-is$, hence $1 = -1$, which is impossible; so $-1$ is not attained. As $\lvert s\rvert$ grows without bound,

$$
u(s) = \frac{1-s^2-2is}{1+s^2} = -1 - \frac{2is}{1+s^2} + \frac{2}{1+s^2} \longrightarrow -1,
$$

so $-1$ is the limit of the chart at both ends of the line.

Geometrically, the line through $-1$ and $u(s)$ meets the imaginary axis at $-is$, so the chart is the stereographic projection of the circle from $-1$ onto that axis, followed by the identification $-is \leftrightarrow s$.

### The Inverse

**Proposition.** Let $u \in \mathrm{U}(1)$ with $u \neq -1$. Then $u = u(s)$ for the real number

$$
s = i\,\frac{u-1}{u+1}.
$$

**Proof.** Put $s = i(u-1)/(u+1)$. Since $\lvert u\rvert = 1$, one has $\bar u = u^{-1}$, hence

$$
\bar s = -i\,\frac{\bar u-1}{\bar u+1} = -i\,\frac{u^{-1}-1}{u^{-1}+1} = -i\,\frac{1-u}{1+u} = i\,\frac{u-1}{u+1} = s,
$$

so $s$ is real. Moreover

$$
1-is = 1+\frac{u-1}{u+1} = \frac{2u}{u+1}, \qquad 1+is = 1-\frac{u-1}{u+1} = \frac{2}{u+1},
$$

so $u(s) = (1-is)/(1+is) = u$.

For a complex number $Q$ of modulus $r$ the unit factor is $u = Q/r$, and the coordinate is

$$
s = i\,\frac{u-1}{u+1} = i\,\frac{Q-r}{Q+r}.
$$

The second form is the one used below: it names $s$ by $Q$ alone. Its denominator vanishes exactly at $Q = -r$, the negative real axis, where the chart has no point.

### The Bijection

**Theorem.** The map $s \mapsto u(s)$ is a bijection from $\mathbb{R}$ onto $\mathrm{U}(1)\setminus\{-1\}$.

**Injectivity.** Suppose $u(s_1) = u(s_2)$. Cross-multiplying,

$$
(1-is_1)(1+is_2) = (1-is_2)(1+is_1),
$$

and expanding both sides gives

$$
1+i(s_2-s_1)+s_1s_2 = 1+i(s_1-s_2)+s_1s_2.
$$

Hence $i(s_2-s_1) = i(s_1-s_2)$, that is $s_1 = s_2$.

**Surjectivity.** This is the proposition of §*The Inverse*: for every unit $u \neq -1$, the real number $s = i(u-1)/(u+1)$ satisfies $u(s) = u$.

The chart is therefore one-to-one, and its image is the circle with the single point $-1$ removed.

## The Rational-Chart Decomposition

### Existence and Uniqueness

**Theorem.** Every complex number $Q$ outside the closed negative real axis has exactly one rational-chart polar decomposition

$$
Q = r\,\frac{1-is}{1+is}, \qquad r > 0, \quad s \in \mathbb{R}.
$$

**Existence.** Let $Q \notin (-\infty,0]$, and put $r = \sqrt{\langle Q\rangle_{*}}$ and $u = Q/r$. Then $r > 0$ and $\langle u\rangle_{*} = 1$. If $u = -1$ then $Q = -r$ is a negative real, contrary to the hypothesis, so $u \neq -1$; the bijection then gives a real $s$ with $u = u(s)$. Hence $Q = ru(s)$.

**Uniqueness.** Taking norms gives $r = \sqrt{\langle Q\rangle_{*}}$, and then $u = Q/r$; the chart is injective, so $s$ is determined by $u$.

The coordinate is $s = i(Q-r)/(Q+r)$ of §*The Inverse*, and the reconstruction is exact:

$$
Q = r\,\frac{1-is}{1+is} = r\,\frac{1-s^2}{1+s^2} - i\,r\,\frac{2s}{1+s^2}.
$$

### The Domain

The domain is

$$
\mathbb{C}\setminus(-\infty,0] = \{\,Q : Q \neq 0 \ \text{and} \ Q \notin \mathbb{R}_{<0}\,\},
$$

the plane cut along the closed negative real axis.

The origin is excluded because no polar decomposition of any kind exists there. The negative real axis is excluded because its unit factor is $-1$, the point the chart does not attain. Every other point of the circle is attained exactly once. In the formula $s = i(Q-r)/(Q+r)$ the two exclusions are visible at once: the denominator vanishes at $Q = -r$, the negative real axis, and numerator and denominator both vanish at $Q = 0$, where $r = 0$ and no decomposition exists.

## The Group Law

The product of two unit factors is a unit factor, and the coordinate of the product is a rational function of the two coordinates.

**Proposition.** For $s_1, s_2 \in \mathbb{R}$ with $s_1s_2 \neq 1$,

$$
u(s_1)\,u(s_2) = u(s_3), \qquad s_3 = \frac{s_1+s_2}{1-s_1s_2}.
$$

**Proof.** Multiplying the two fractions,

$$
u(s_1)u(s_2) = \frac{(1-is_1)(1-is_2)}{(1+is_1)(1+is_2)}
= \frac{(1-s_1s_2)-i(s_1+s_2)}{(1-s_1s_2)+i(s_1+s_2)}.
$$

Dividing numerator and denominator by $1-s_1s_2$ puts the right-hand side in the form $(1-is_3)/(1+is_3)$ with $s_3 = (s_1+s_2)/(1-s_1s_2)$, which is $u(s_3)$.

The law has the identity $s = 0$, because $u(0) = 1$, and the inverse $-s$, because

$$
u(s)\,u(-s) = \frac{1-is}{1+is}\cdot\frac{1+is}{1-is} = 1.
$$

It is associative wherever it is defined, being inherited from the multiplication of the circle.

When $s_1s_2 = 1$ the formula has a pole. The product is then

$$
u(s)\,u(1/s) = \frac{(1-is)(1-i/s)}{(1+is)(1+i/s)} = \frac{-i(s+1/s)}{i(s+1/s)} = -1,
$$

the missing point. The product is a perfectly good unit, but its coordinate does not exist: it has escaped to infinity. The chart is therefore a **group chunk**, not a global group. It is a coordinate on the line, and the line must be compactified to see the whole circle.

## Covering the Circle and the Price of Locality

The chart misses $-1$. A second chart, $v(s) = -u(s)$, misses $+1$ and supplies $-1$. On the common domain the two are related by

$$
v(s) = -u(s) = u\!\left(-\frac{1}{s}\right), \qquad s \neq 0,
$$

so the second chart is the first composed with $s \mapsto -1/s$. The two charts

$$
s \longmapsto u(s), \qquad s \longmapsto -u(s)
$$

therefore cover the circle, the first missing $-1$ and the second missing $+1$. Topologically the one-point compactification $\mathbb{R}\cup\{\infty\}$ is a circle, and the first chart extends to a homeomorphism onto $\mathrm{U}(1)$ by setting $u(\infty) = -1$.

The chart has three properties, and they are the terms of an exchange.

- **It is rational.** Both $u(s)$ and its inverse are ratios of polynomials. The decomposition is computed by field operations alone, with no transcendental function and no infinite series.
- **It is local.** It misses one point of the circle, and therefore one ray of the plane. A second chart, or the point at infinity, is needed to recover the circle.
- **It is unbounded.** Near the missing point the coordinate escapes to infinity, and the two sides of the cut carry opposite signs of $s$.

The modulus–unit form is global and uses a square root. The exponential form, treated in *Exponential Polar Decomposition of Complex Numbers*, is global and uses a transcendental function. The present form is the one that stays rational, and locality is its price.

## The Matrix Picture

In the real basis $\{1,i\}$ the unit $u(s)$ is the matrix

$$
M(s) = \frac{1-s^2}{1+s^2}\,I - \frac{2s}{1+s^2}\,J, \qquad J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad J^2 = -I.
$$

It is the Cayley transform of the line $\mathbb{R}J$:

$$
M(s) = (I-sJ)(I+sJ)^{-1}.
$$

Indeed $(I+sJ)(I-sJ) = I-s^2J^2 = (1+s^2)I$, so $(I+sJ)^{-1} = (I-sJ)/(1+s^2)$ and

$$
M(s) = \frac{(I-sJ)^2}{1+s^2} = \frac{(1-s^2)I-2sJ}{1+s^2}.
$$

The determinant is one and the matrix is orthogonal:

$$
\det M(s) = \frac{(1-s^2)^2+4s^2}{(1+s^2)^2} = 1, \qquad M(s)^{\mathsf T}M(s) = I,
$$

so $M(s) \in SO(2)$. The decomposition of $Q$ reads, in matrices,

$$
M_Q = r\,(I-sJ)(I+sJ)^{-1},
$$

a rational expression in $s$ for the conformal matrix. At $s = 0$ the factor is the identity and at infinity it approaches $-I$; the point $-I$ is the missing one.

## Worked Examples

The example $Q = 3-4i$ runs the mechanism end to end. Its modulus is $r = 5$, so its unit factor is

$$
u = \frac{Q}{r} = 0.6-0.8i.
$$

The inverse formula in $u$ gives

$$
s = i\,\frac{u-1}{u+1} = i\,\frac{-0.4-0.8i}{1.6-0.8i} = i\,(-0.5i) = \frac{1}{2},
$$

and the formula in $Q$ gives the same number. The numerator and the denominator are

$$
Q-r = -2-4i, \qquad Q+r = 8-4i,
$$

so, multiplying above and below by the conjugate $8+4i$ of the denominator,

$$
s = i\,\frac{Q-r}{Q+r} = i\,\frac{-2-4i}{8-4i} = i\,\frac{(-2-4i)(8+4i)}{(8-4i)(8+4i)} = i\,\frac{-40i}{80} = \frac{1}{2}.
$$

The reconstruction closes the loop:

$$
u\!\left(\tfrac{1}{2}\right) = \frac{1-\tfrac{i}{2}}{1+\tfrac{i}{2}} = \frac{(2-i)^2}{5} = \frac{3-4i}{5} = 0.6-0.8i, \qquad Q = 5(0.6-0.8i) = 3-4i.
$$

| $Q$ | $r = \sqrt{\langle Q\rangle_{*}}$ | $s = i(Q-r)/(Q+r)$ | $u$ | reconstruction error |
|---|---|---|---|---|
| $2$ | $2$ | $0$ | $1$ | $0$ |
| $5i$ | $5$ | $-1$ | $i$ | $0$ |
| $-5i$ | $5$ | $1$ | $-i$ | $0$ |
| $1+i$ | $\sqrt{2}$ | $-(\sqrt{2}-1) = -0.4142135623730951$ | $(1+i)/\sqrt{2}$ | $2.2\times10^{-16}$ |
| $3-4i$ | $5$ | $0.5$ | $0.6-0.8i$ | $0$ |
| $3+4i$ | $5$ | $-0.5$ | $0.6+0.8i$ | $0$ |
| $-3+4i$ | $5$ | $-2$ | $-0.6+0.8i$ | $0$ |
| $-2-i$ | $\sqrt{5} = 2.23606797749979$ | $\sqrt{5}+2 = 4.23606797749979$ | $(-2-i)/\sqrt{5}$ | $0$ |
| $-3$ | $3$ | — | $-1$ | excluded |

The table separates four kinds of element. The real positive line, $2$, has $s = 0$ and unit factor $1$. The imaginary axis, $5i$ and $-5i$, has $s = \mp1$ and unit factors $\pm i$. The elements off the axes have coordinates of both signs; the ones with negative real part, $-3+4i$ and $-2-i$, lie outside $[-1,1]$, and $\lvert s\rvert$ grows as the element approaches the negative real axis. The last line is that axis itself: its unit factor is the missing point $-1$, and its coordinate is infinite.

On the two sides of the cut the chart distinguishes the approaches:

$$
u(10^9) \approx -1-2\times10^{-9}i, \qquad u(-10^9) \approx -1+2\times10^{-9}i.
$$

The cut corresponds to the single unit factor $-1$, which neither side attains.

## Summary

Every complex number outside the closed negative real axis has exactly one rational-chart polar decomposition $Q = r(1-is)/(1+is)$, with $r = \sqrt{\langle Q\rangle_{*}} > 0$ and $s = i(Q-r)/(Q+r) \in \mathbb{R}$. It is the modulus–unit decomposition of *Modulus–Unit Polar Decomposition of Complex Numbers*, with the same modulus and the same unit factor, and with the unit factor named by a real coordinate instead of by a point of the circle.

The chart $s \mapsto u(s)$ is a bijection from $\mathbb{R}$ onto $\mathrm{U}(1)\setminus\{-1\}$. It is the stereographic projection from $-1$ onto the imaginary axis, read in the coordinate $s$ of the point $-is$. It is rational in both directions, and it sends $0$ to $1$ and $\pm1$ to $\mp i$.

The group law is $s_1*s_2 = (s_1+s_2)/(1-s_1s_2)$, with identity $0$ and inverse $-s$; it has a pole at $s_1s_2 = 1$, where the product is the missing point $-1$ and the coordinate escapes to infinity. The chart is a group chunk. A second chart, $v(s) = -u(s)$, misses $+1$ and supplies $-1$, and the two cover the circle.

In the matrix picture the decomposition is $M_Q = r(I-sJ)(I+sJ)^{-1}$, the Cayley transform of the line $sJ$ onto $SO(2)$ minus $-I$. The price of rationality is locality: one point of the circle, and one ray of the plane, are not covered.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | the complex algebra, basis $1$, $i$, $i^2 = -1$ |
| $Q$ | a complex number outside the closed negative real axis |
| $\langle Q\rangle_{*} = Q\bar{Q} = q^2+q'^2$ | the norm, positive definite |
| $r = \sqrt{\langle Q\rangle_{*}}$ | the modulus, a positive real |
| $u$ | the unit factor, $\langle u\rangle_{*} = 1$ |
| $s$ | the real chart parameter of the unit factor |
| $u(s) = (1-is)/(1+is)$ | the chart, the unit of parameter $s$ |
| $s = i(Q-r)/(Q+r)$ | the coordinate of $Q$, a real number |
| $\mathrm{U}(1)$ | the unit circle, a compact group |
| $J$ | the complex structure, multiplication by $i$, $J^2 = -I$ |
| $M(s) = (I-sJ)(I+sJ)^{-1}$ | the matrix of $u(s)$, the Cayley transform on $SO(2)$ |
| $SO(2)$ | the special orthogonal group of the plane |

## Further Reading

- Tristan Needham, *Visual Complex Analysis* (Oxford University Press, 1997), for stereographic projection, the Riemann sphere and the Möbius transformations of the circle.
- Alan F. Beardon, *The Geometry of Discrete Groups* (Springer, 1983), for Möbius transformations, the Cayley transform and the action on the circle.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 1985), for the Cayley transform of a matrix and its relation to the orthogonal group.
- John B. Conway, *Functions of One Complex Variable* (Springer, 2nd edition 1978), for Möbius transformations and the extended plane.
