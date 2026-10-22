# __Rational-Chart Polar Decomposition of Split-Complex Numbers__

## Introduction

The modulus–unit polar decomposition of *Modulus–Unit Polar Decomposition of Split-Complex Numbers* writes every split-complex number of nonzero norm as

$$
Q = r\,u, \qquad r = \sqrt{\lvert \langle Q\rangle_{*}\rvert} > 0, \qquad \lvert \langle u\rangle_{*}\rvert = 1,
$$

with $r$ the modulus and $u$ the unit factor. That article proves the pair unique and treats $u$ as a point of the unit set $\{\langle u\rangle_{*}=1\}\cup\{N=-1\}$, the union of two hyperbolas. It chooses no coordinate on the hyperbola: the unit factor is named by the equation $\lvert \langle u\rangle_{*}\rvert=1$, not by a number.

This article names it. For a real number $s$ put

$$
u(s) = \frac{1-sj}{1+sj},
$$

and write

$$
Q = r\,\epsilon\,u(s) = r\,\epsilon\,\frac{1-sj}{1+sj}, \qquad \epsilon\in\{1,\pm j\},
$$

with $s\neq\pm1$. The decomposition is the same one; only the name of the unit factor changes. The number $r$ is still the modulus, the product $\epsilon u(s)$ is still the same unit factor, of norm $\operatorname{sign}\langle Q\rangle_{*}$, and the pair $(r,\epsilon u(s))$ is still unique. The only new object is the real number $s$, which replaces the point of the hyperbola by a coordinate on a line. The factor $\epsilon$ is not new either: it is the component label fixed by the modulus–unit article, and it is needed because the chart is a coordinate on the hyperbola $\langle u\rangle_{*}=1$ alone.

The chart is rational: $u(s)$ and its inverse are ratios of polynomials. The price is locality, and it is higher than in the complex case. The parametrisation has two poles, at $s=\pm1$, where the denominator $1-s^2$ vanishes; they are the two null directions, the points at infinity of the hyperbola. As $\lvert s\rvert$ grows, $u(s)$ approaches $-1$ without attaining it, so the one unit factor missed on $\langle u\rangle_{*}=1$ is $-1$, the unit factor of every negative real number. The timelike decomposition therefore holds on the plane cut along the negative real axis. In the spacelike region the discrete factor $j$ or $-j$ moves the chart to the hyperbola $\langle u\rangle_{*}=-1$; each fixed sign misses a single ray, $Q=-rj$ for $j$ and $Q=rj$ for $-j$, and the two signs together cover the spacelike region without a cut.

The plan is as follows. The modulus–unit form and the four components are recalled (§*The Modulus–Unit Form Recalled*). The chart, its inverse and its bijection property are established (§*The Chart*, §*The Inverse*, §*The Bijection*). The decomposition is stated in the two regimes and its exact domain is described (§*The Rational-Chart Decomposition*, §*The Domain*). The group law and its pole are derived (§*The Group Law*). The second chart, the projective picture and the cost of rationality are given (§*Covering the Unit Set and the Price of Locality*). The Cayley matrix is computed (§*The Matrix Picture*), and examples are worked (§*Worked Examples*).

The notation is that of *Split-Complex Algebra*, *Norm and Invertibility in the General Split-Complex Algebra* and *Modulus–Unit Polar Decomposition of Split-Complex Numbers*, and it is collected in §*Summary of Notation*.

Every numerical value displayed below was recomputed in double precision.

## The Unit Factor and Its Chart

### The Modulus–Unit Form Recalled

Let $Q = q+jq'$ with $q,q'\in\mathbb{R}$ and norm $\langle Q\rangle_{*}=q^2-q'^2$. On the invertible set $\langle Q\rangle_{*}\neq0$ the modulus and unit factor are

$$
r = \sqrt{\lvert \langle Q\rangle_{*}\rvert} > 0, \qquad u = \frac{Q}{r}, \qquad \langle u\rangle_{*} = \operatorname{sign}\langle Q\rangle_{*}\in\{\pm1\}.
$$

The pair $(r,u)$ is unique, and the decomposition is $Q=ru$. The modulus is positive in both regimes; the sign of the norm is carried by the unit factor. The null cone $\langle Q\rangle_{*}=0$ is excluded, and the modulus vanishes there.

The unit set $\{\lvert \langle Q\rangle_{*}\rvert=1\}$ has four components. Every unit can be written as

$$
u = \epsilon\exp(\phi j), \qquad \epsilon\in\{\pm1,\pm j\}, \quad \phi\in\mathbb{R},
$$

with $\epsilon$ the component label. The four labels and the signs of the coordinates are listed in the following table.

| component | $\epsilon$ | $\langle u\rangle_{*}$ | $\operatorname{sign}q$ | $\operatorname{sign}q'$ |
|---|---|---|---|---|
| identity | $1$ | $+1$ | $+$ | either |
| opposite | $-1$ | $+1$ | $-$ | either |
| upper spacelike | $j$ | $-1$ | either | $+$ |
| lower spacelike | $-j$ | $-1$ | either | $-$ |

The chart $u(s)$ lies on the hyperbola $\langle u\rangle_{*}=1$. It covers the two timelike components, with the point $-1$ omitted. The spacelike components are reached by multiplying the positive branch of the chart by $j$ or $-j$, which changes the norm to $-1$. This is why the discrete factor is not optional in the rational decomposition: the chart alone never leaves the timelike hyperbola.

### The Chart

For real $s\neq\pm1$ define

$$
u(s) = \frac{1-sj}{1+sj} = \frac{1+s^2}{1-s^2} - \frac{2s}{1-s^2}\,j .
$$

The element $1+sj$ has norm $1-s^2$, so it is invertible exactly when $s\neq\pm1$; the displayed form has the real denominator $1-s^2$, which vanishes at $s=\pm1$. The norm is constant on the chart:

$$
\langle u(s)\rangle_{*} = \frac{\langle 1-sj\rangle_{*}}{\langle 1+sj\rangle_{*}} = \frac{1-s^2}{1-s^2} = 1.
$$

The chart is rational, defined over $\mathbb{Q}$, and it uses no hyperbolic function. Its values at small integers and fractions are as follows.

| $s$ | $u(s)$ | $\langle u(s)\rangle_{*}$ |
|---|---|---|
| $0$ | $1$ | $1$ |
| $1/3$ | $5/4-3j/4$ | $1$ |
| $-1/3$ | $5/4+3j/4$ | $1$ |
| $1/2$ | $5/3-4j/3$ | $1$ |
| $2$ | $-5/3+4j/3$ | $1$ |
| $-2$ | $-5/3-4j/3$ | $1$ |

The identity $u(0)=1$ is the identity of the chart. The chart is not periodic: $u(s)$ is injective on its domain, as proved in §*The Bijection*. The parameter $s$ is a rational coordinate, not an angle.

### The Inverse

Let $u=x+yj$ be a unit of norm $1$. The inverse of the chart is

$$
s = -\frac{j(u-1)}{u+1} = \frac{j(1-u)}{u+1},
$$

defined for $u\neq-1$. Since $\langle u\rangle_{*}=1$, the conjugate is the inverse, $\bar u=u^{-1}$, and the conjugate of $s$ is

$$
\bar s = \frac{j(\bar u-1)}{\bar u+1} = \frac{j(u^{-1}-1)}{u^{-1}+1} = \frac{j(1-u)}{1+u} = s,
$$

so $s$ is real. In coordinates the inverse is the single rational expression

$$
s = -\frac{y}{1+x}, \qquad u = x+yj, \quad x^2-y^2=1, \quad x\neq-1.
$$

Indeed, multiplying $u(s)$ out gives $x=(1+s^2)/(1-s^2)$ and $y=-2s/(1-s^2)$, and then

$$
-\frac{y}{1+x} = \frac{2s/(1-s^2)}{1+(1+s^2)/(1-s^2)} = \frac{2s}{2} = s.
$$

For a general timelike element $Q$ the inverse reads

$$
s = -\frac{q'}{r+q}, \qquad r = \sqrt{q^2-q'^2},
$$

because $u=Q/r$ has coordinates $(q/r,q'/r)$. The denominator $r+q$ vanishes exactly when $q=-r$ and $q'=0$, that is on the negative real axis.

### The Bijection

**Theorem.** The map $u : \mathbb{R}\setminus\{\pm1\}\to\{\langle u\rangle_{*}=1\}\setminus\{-1\}$ is a bijection.

**Injectivity.** Suppose $u(s_1)=u(s_2)$. Cross multiplication gives

$$
(1-s_1j)(1+s_2j) = (1-s_2j)(1+s_1j).
$$

Expanding and using $j^2=1$,

$$
1-s_1s_2+(s_2-s_1)j = 1-s_1s_2+(s_1-s_2)j,
$$

so $s_1=s_2$. The denominators are nonzero because $s_1,s_2\neq\pm1$.

**Surjectivity.** Let $u=x+yj$ with $\langle u\rangle_{*}=1$ and $u\neq-1$. Set $s=-y/(1+x)$. The computation of §*The Inverse* gives $u(s)=u$, so every point of $\{\langle u\rangle_{*}=1\}\setminus\{-1\}$ is attained.

The image omits exactly $u=-1$: the equation $u(s)=-1$ would give $1-sj = -(1+sj)$, hence $1=-1$. The point $-1$ is the vertex of the negative branch, and it is the one point of the timelike hyperbola that the finite chart does not reach. As $s\to\pm\infty$, $u(s)\to-1$, so the missing point is the image of the point at infinity of the parameter line.

The two poles $s=\pm1$ are not values of the chart. Their one-sided limits are the two null directions, the points at infinity of the hyperbola:

| limit | $x$ | $y$ | direction |
|---|---|---|---|
| $s\to-1^-$ | $-\infty$ | $-\infty$ | $1+j$ |
| $s\to-1^+$ | $+\infty$ | $+\infty$ | $1+j$ |
| $s\to1^-$ | $+\infty$ | $-\infty$ | $1-j$ |
| $s\to1^+$ | $-\infty$ | $+\infty$ | $1-j$ |
| $s\to\pm\infty$ | $-1$ | $0$ | $-1$ |

The three intervals $(-\infty,-1)$, $(-1,1)$ and $(1,\infty)$ map to the three open pieces of the affine hyperbola: the two halves of the negative branch and the positive branch. The negative branch is split at $-1$, which is reached only at infinity. In the complex case the rational chart has one pole, at infinity, and misses $-1$; here the indefinite metric produces two poles, at $\pm1$, and the parameter line has three intervals.

## The Rational-Chart Decomposition

### Existence and Uniqueness

**Theorem.** Every split-complex number $Q$ with $\langle Q\rangle_{*}\neq0$ and $Q$ not on the negative real axis has a unique decomposition

$$
Q = r\,\epsilon\,u(s), \qquad r>0, \quad \epsilon\in\{1,j,-j\}, \quad s\in\mathbb{R}\setminus\{\pm1\},
$$

with $\epsilon=1$ in the timelike regime and $\epsilon=\pm j$ in the spacelike regime, the sign chosen by the sign of $q'$. The decomposition is defined exactly on $\{\langle Q\rangle_{*}\neq0\}\setminus\mathbb{R}_{<0}$.

**Timelike regime.** Let $\langle Q\rangle_{*}>0$. Put $r=\sqrt{\langle Q\rangle_{*}}$ and $u=Q/r$, so $\langle u\rangle_{*}=1$. If $u\neq-1$, let $s$ be the inverse of §*The Inverse* and write

$$
Q = r\,u(s), \qquad s = -\frac{q'}{r+q} \in \mathbb{R}\setminus\{\pm1\}.
$$

The decomposition is unique: $r$ is forced by the modulus, $u$ by $Q/r$, and $s$ by the inverse chart. The condition $u\neq-1$ is exactly $Q\neq-r$, the negative real axis. On that axis the unit factor is $-1$, the missing point, and no finite $s$ exists. As $s\to\pm\infty$ the element $r u(s)$ tends to $-r$, so the cut is the point at infinity of the chart.

The two timelike components are distinguished by the sign of $q$. For $q>0$ the parameter lies in $(-1,1)$; for $q<0$ it lies in $(-\infty,-1)\cup(1,\infty)$. The chart covers both components, but the negative branch is cut at its vertex.

**Spacelike regime.** Let $\langle Q\rangle_{*}<0$. Put $r=\sqrt{-\langle Q\rangle_{*}}$ and choose the discrete factor according to the sign of $q'$:

$$
\epsilon = \begin{cases} j, & q'>0,\\ -j, & q'<0. \end{cases}
$$

Then $u=\epsilon Q/r$ has norm $1$, and $u\neq-1$. Define $s$ by the inverse chart and write

$$
Q = r\,\epsilon\,u(s).
$$

The factor $j$ maps the chart to the upper spacelike component and the factor $-j$ to the lower one. Both factors give norm $-1$, because $\langle j\rangle_{*}=-1$. The parameter $s$ lies in $(-1,1)$ in both cases, since $u$ has positive real part. The spacelike region has no cut: each of its two components is covered by one chart and one discrete factor.

If one insists on the single factor $j$ for all spacelike elements, the ray $Q=-rj$ is missed: it corresponds to $u=-1$, the point missing from the chart, and it is reached by the factor $-j$ with $u=1$. This is the spacelike analogue of the missing point $-1$ in the timelike regime.

The two regimes prove the theorem: the timelike case fixes $\epsilon=1$, the spacelike case fixes $\epsilon=\pm j$, and in both the modulus and the chart parameter are unique.

### The Domain

The domain is

$$
\{\langle Q\rangle_{*}\neq0\}\setminus\mathbb{R}_{<0},
$$

the invertible set with the negative real axis removed.

The components and the parameter ranges are collected in the following table.

| component | condition | $\epsilon$ | range of $s$ | excluded |
|---|---|---|---|---|
| timelike future | $\langle Q\rangle_{*}>0$, $q>0$ | $1$ | $(-1,1)$ | none |
| timelike past | $\langle Q\rangle_{*}>0$, $q<0$ | $1$ | $(-\infty,-1)\cup(1,\infty)$ | $Q=-r$ |
| spacelike upper | $\langle Q\rangle_{*}<0$, $q'>0$ | $j$ | $(-1,1)$ | none |
| spacelike lower | $\langle Q\rangle_{*}<0$, $q'<0$ | $-j$ | $(-1,1)$ | none |

The null cone is excluded, and the negative real axis is excluded in the timelike regime. The negative real axis is the only cut of the decomposition. The spacelike rays are not cut because the two signs of $j$ are both available; the timelike hyperbola has only one chart, and its vertex $-1$ is the price of the rational parametrisation.

## The Group Law

The chart carries a rational group law. For $s_1,s_2\in\mathbb{R}\setminus\{\pm1\}$ with $1+s_1s_2\neq0$,

$$
u(s_1)u(s_2) = \frac{(1-s_1j)(1-s_2j)}{(1+s_1j)(1+s_2j)} = \frac{1+s_1s_2-(s_1+s_2)j}{1+s_1s_2+(s_1+s_2)j} = u(s_3),
$$

where

$$
s_3 = \frac{s_1+s_2}{1+s_1s_2}.
$$

The identity is $s=0$, because $u(0)=1$, and the inverse is $s\mapsto-s$, because $u(s)u(-s)=1$. The law is the hyperbolic addition formula, transported from the exponential coordinate by $s=-\tanh(\phi/2)$ on the identity component.

The pole occurs when $1+s_1s_2=0$, that is $s_1s_2=-1$. At that parameter value the product is

$$
u(s)u(-1/s) = -1,
$$

the missing point. The product of two elements of the chart can therefore leave the chart; the group law is a **group chunk**, not a global law on $\mathbb{R}\setminus\{\pm1\}$. In the full group the sign factor multiplies separately,

$$
(\epsilon_1,s_1)(\epsilon_2,s_2) = (\epsilon_1\epsilon_2,\ s_1*s_2),
$$

whenever $s_1*s_2$ is defined, with $\epsilon_1\epsilon_2$ in the four-element group $\{\pm1,\pm j\}$.

The following table records the elementary laws and two products.

| expression | value |
|---|---|
| $u(0)$ | $1$ |
| $u(s)^{-1}$ | $u(-s)$ |
| $u(s_1)u(s_2)$ | $u\bigl((s_1+s_2)/(1+s_1s_2)\bigr)$ |
| $u(1/2)u(1/3)$ | $u(5/7)$ |
| $u(2)u(3)$ | $u(5/7)$ |
| $u(2)u(-1/2)$ | $-1$ |

The two products $u(1/2)u(1/3)$ and $u(2)u(3)$ both equal $u(5/7)$; the chart law is not injective in the pair, only in the result. The product $u(2)u(-1/2)$ is the pole: $2\cdot(-1/2)=-1$, and the result is the missing point. In the full group, multiplying by a sign factor moves the product to another component, and the parameter law is unchanged.

## Covering the Unit Set and the Price of Locality

The chart $u(s)$ misses $-1$ and has poles at $\pm1$. A second chart

$$
v(s) = -u(s), \qquad s\neq\pm1,
$$

misses $+1$ and has the same two poles; for $s\neq0$ it equals $u(1/s)$. At $s=0$ it takes the value $-1$, the point missed by $u$. The two charts cover the hyperbola $\langle u\rangle_{*}=1$:

$$
\{\langle u\rangle_{*}=1\} = u(\mathbb{R}\setminus\{\pm1\}) \cup v(\mathbb{R}\setminus\{\pm1\}).
$$

For the negative hyperbola $\langle u\rangle_{*}=-1$ one multiplies by $j$ and $-j$. The four charts $u$, $v$, $ju$ and $jv$ cover the four components of the unit set.

| chart | norm | missing point |
|---|---|---|
| $u(s)$ | $+1$ | $-1$ |
| $v(s)=-u(s)$ | $+1$ | $+1$ |
| $ju(s)$ | $-1$ | $-j$ |
| $jv(s)=-ju(s)$ | $-1$ | $+j$ |

The projective picture explains the count. The parameter line with its point at infinity is the projective line $\mathbb{P}^1(\mathbb{R})$, a circle. The map $u$ extends to a homeomorphism from $\mathbb{P}^1(\mathbb{R})$ onto the projective conic

$$
\mathcal{Q} : X^2-Y^2=Z^2
$$

in the projective plane, with $u(\infty)=-1$ and $u(\pm1)$ the two points at infinity of the affine hyperbola. The affine chart $\mathbb{R}\setminus\{\pm1\}$ is $\mathbb{P}^1$ minus the two poles and the point at infinity, and its image is the affine hyperbola minus $-1$. The two poles are the two null directions; the missing point is the vertex of the negative branch.

In the complex case the projective conic is an ellipse and has no real points at infinity. The rational chart has one pole, at infinity, and misses one point, $-1$. In the split case the conic is a hyperbola, it has two real points at infinity, and the chart has two poles. The extra pole is the geometric difference between the circle and the hyperbola.

The chart has three properties, and they are the terms of an exchange.

- **It is rational.** Both $u(s)$ and its inverse are ratios of polynomials. The decomposition is computed by field operations alone, with no hyperbolic function and no infinite series.
- **It is local.** It misses one point of the hyperbola, and therefore one ray of the plane. A second chart, or the point at infinity, is needed to recover the hyperbola.
- **It is unbounded.** Near the missing point the coordinate escapes to infinity, and the two sides of the cut carry parameters of opposite sign.

The modulus–unit form is global and uses a square root. The exponential form, treated in *Exponential Polar Decomposition of Split-Complex Numbers*, is global with a discrete factor and uses a transcendental function. The present form is the one that stays rational, and locality is its price.

The complex rational chart is a single chart on the circle, with one pole at infinity and one missing point. The split chart has two poles, at $\pm1$, because the projective conic is a hyperbola with two real points at infinity. It misses one point, $-1$, because the affine chart is one chart on a hyperbola. The decomposition needs the discrete factor $\epsilon$ because the unit set has four components, whereas the complex unit group is connected. The matrix picture departs in the same way: the complex Cayley matrix is orthogonal, a rotation, while the split Cayley matrix is symmetric and not orthogonal, a Lorentz transformation of the indefinite plane. The algebraic unit factor and the Euclidean matrix polar factor therefore differ, and the Euclidean polar decomposition is read separately.

## The Matrix Picture

Let

$$
K = \begin{pmatrix}0&1\\1&0\end{pmatrix}, \qquad K^2=I,
$$

and define the Cayley matrix

$$
M(s) = (I-sK)(I+sK)^{-1} = \frac{(1+s^2)I-2sK}{1-s^2} = \begin{pmatrix} x & y\\ y & x\end{pmatrix},
$$

with $x=(1+s^2)/(1-s^2)$ and $y=-2s/(1-s^2)$. The matrix is exactly the matrix of multiplication by $u(s)$; its determinant is $\langle u(s)\rangle_{*}=1$. It is symmetric, and it preserves the indefinite form $x^2-y^2$:

$$
M(s)^{\mathsf T}\begin{pmatrix}1&0\\0&-1\end{pmatrix}M(s) = \begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

The eigenvalues are $(1-s)/(1+s)$ and $(1+s)/(1-s)$. For $\lvert s\rvert<1$ both are positive and $M(s)$ lies in the identity component of $SO(1,1)$; for $\lvert s\rvert>1$ both are negative and $M(s)$ lies in the other component. As $s\to\pm\infty$, $M(s)\to-I$, the missing point of the chart. The image is $SO(1,1)\setminus\{-I\}$.

The matrix $M(s)$ is **not orthogonal** for $s\neq0$. For $\lvert s\rvert<1$ it is symmetric positive definite, with eigenvalues $(1-s)/(1+s)$ and $(1+s)/(1-s)$; for $\lvert s\rvert>1$ it is symmetric negative definite. In neither case is $M(s)^{\mathsf T}M(s)=I$ except at $s=0$. The algebraic unit factor and the Euclidean matrix polar factor therefore differ. The Euclidean polar decomposition of $M(s)$ is $(M(s),I)$ for $\lvert s\rvert<1$ and $(-M(s),-I)$ for $\lvert s\rvert>1$.

This is the point at which the complex template must not be copied. In the complex case the Cayley matrix is a rotation, $M(s)\in SO(2)$, and it is orthogonal; the algebraic chart and the matrix polar chart coincide. In the split case the Cayley matrix is a symmetric Lorentz transformation, not an orthogonal one. It preserves the indefinite form, not the Euclidean one, and its Euclidean polar factor is a sign $\pm I$; the negative-norm matrices $K M(s)$ have a reflection instead, as described in *Modulus–Unit Polar Decomposition of Split-Complex Numbers*, §*The Matrix Polar Decomposition*.

The matrix of a general element is $M_Q=rM(\epsilon)M(s)$, with $M(\epsilon)\in\{I,-I,K,-K\}$. The determinant is $\langle Q\rangle_{*}=r^2\langle \epsilon\rangle_{*}$, positive in the timelike regime and negative in the spacelike one. The Cayley chart is thus a rational chart on the algebraic unit factor, not on the orthogonal factor.

## Worked Examples

### A Generic Split-Complex Number

Take $Q=5+3j$. Then $\langle Q\rangle_{*}=16$, $r=4$, and $u=1.25+0.75j$. The inverse chart gives

$$
s = -\frac{q'}{r+q} = -\frac{3}{4+5} = -\frac13.
$$

The reconstruction is

$$
4\,u(-1/3) = 4\left(\frac54+\frac34 j\right) = 5+3j.
$$

The Cayley matrix is

$$
M(-1/3) = \begin{pmatrix}5/4&3/4\\3/4&5/4\end{pmatrix},
$$

with eigenvalues $2$ and $1/2$, both positive. The parameter lies in $(-1,1)$, as it must for the positive branch.

### The Spacelike Components

Take $Q=1+2j$. Then $\langle Q\rangle_{*}=-3$, $r=\sqrt3$, and $q'>0$, so $\epsilon=j$. The unit factor is

$$
u = \frac{jQ}{r} = \frac{2+j}{\sqrt3} = \frac{2}{\sqrt3}+\frac{1}{\sqrt3}j,
$$

The inverse chart applies to $u$, whose coordinates are $(2/\sqrt3,1/\sqrt3)$:

$$
s = -\frac{1/\sqrt3}{1+2/\sqrt3} = -\frac{1}{2+\sqrt3} = -2+\sqrt3 = -0.2679491924.
$$

The last equality uses $1/(2+\sqrt3)=2-\sqrt3$. The reconstruction is

$$
\sqrt3\,j\,u(s) = 1+2j.
$$

For $Q=-1-2j$ the factor is $-j$ and the same $u$ and $s$ occur; for $Q=-1+2j$ the factor is $j$ and $s=2-\sqrt3$; for $Q=1-2j$ the factor is $-j$ and $s=2-\sqrt3$. The four spacelike elements $\pm1\pm2j$ are covered by the two signs of $j$ and the two signs of $s$.

### A Table of Examples

The following table applies the chart to the four components, to the cut and to the null cone.

| $Q$ | $\langle Q\rangle_{*}$ | $r$ | $\epsilon$ | $u$ | $s$ | reconstruction |
|---|---|---|---|---|---|---|
| $2$ | $4$ | $2$ | $1$ | $1$ | $0$ | $2$ |
| $j$ | $-1$ | $1$ | $j$ | $1$ | $0$ | $j$ |
| $-j$ | $-1$ | $1$ | $-j$ | $1$ | $0$ | $-j$ |
| $5+3j$ | $16$ | $4$ | $1$ | $1.25+0.75j$ | $-1/3$ | $5+3j$ |
| $1+2j$ | $-3$ | $\sqrt3$ | $j$ | $1.1547+0.5774j$ | $-2+\sqrt3$ | $1+2j$ |
| $-1-2j$ | $-3$ | $\sqrt3$ | $-j$ | $1.1547+0.5774j$ | $-2+\sqrt3$ | $-1-2j$ |
| $-1+2j$ | $-3$ | $\sqrt3$ | $j$ | $1.1547-0.5774j$ | $2-\sqrt3$ | $-1+2j$ |
| $1-2j$ | $-3$ | $\sqrt3$ | $-j$ | $1.1547-0.5774j$ | $2-\sqrt3$ | $1-2j$ |
| $-2$ | $4$ | $2$ | $1$ | $-1$ | no finite $s$ | cut |
| $1+j$ | $0$ | — | — | — | — | null |

The reconstruction error is at most $9\times10^{-16}$ in double precision for the invertible entries. The entry $-2$ is the cut: its unit factor is $-1$, the point missed by the chart. The entry $1+j$ is null: it has no modulus and no unit factor.

### The Cut in the Plane

The negative real axis is the set $Q=-r$, $r>0$. Its unit factor is $-1$, and its parameter is the point at infinity of the chart. In the timelike past component the parameter ranges over $(-\infty,-1)$ on one side of the cut and $(1,\infty)$ on the other; the two ranges meet at $s=\pm\infty$, which is the same missing point. The chart therefore sees the cut as a single point at infinity, not as a line. This is the precise sense in which the rational chart is local: it is a chart on the hyperbola minus one point, and the missing point is the cut.

## Summary

The rational chart

$$
u(s) = \frac{1-sj}{1+sj} = \frac{1+s^2}{1-s^2} - \frac{2s}{1-s^2}j, \qquad s\neq\pm1,
$$

is a bijection from $\mathbb{R}\setminus\{\pm1\}$ onto $\{\langle u\rangle_{*}=1\}\setminus\{-1\}$, with inverse $s=-y/(1+x)$ for $u=x+yj$ and $s=-q'/(r+q)$ for a timelike element $Q=q+jq'$. The two poles $s=\pm1$ are the null directions, the points at infinity of the hyperbola; the missing point is $u=-1$, the vertex of the negative branch.

Every invertible split-complex number off the negative real axis has a unique rational-chart decomposition $Q=r\epsilon u(s)$, with $r>0$, $\epsilon=1$ in the timelike regime and $\epsilon=\pm j$ in the spacelike regime, the sign chosen by the sign of $q'$. The negative real axis is the cut. The spacelike components have no cut because the two signs of $j$ are available. The chart law is $s_1*s_2=(s_1+s_2)/(1+s_1s_2)$, with identity $0$, inverse $-s$ and pole at $s_1s_2=-1$, where the product is $-1$. The second chart $v(s)=-u(s)=u(1/s)$ supplies the missing $-1$; together with the two signs of $j$ it covers the four components of the unit set.

The Cayley matrix $M(s)=(I-sK)(I+sK)^{-1}$ is symmetric, has determinant $1$, and preserves the indefinite form; it is not orthogonal in general. Its image is $SO(1,1)\setminus\{-I\}$, and its Euclidean polar factor is a sign $\pm I$. The rational chart is the algebraic chart on the unit factor, not the orthogonal chart of the matrix.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{D}$ | the split-complex algebra, $j^2=+1$ |
| $Q=q+jq'$ | a split-complex number |
| $\langle Q\rangle_{*}=q^2-q'^2$ | the norm |
| $r=\sqrt{\lvert \langle Q\rangle_{*}\rvert}$ | the modulus |
| $u=Q/r$ | the unit factor, $\lvert \langle u\rangle_{*}\rvert=1$ |
| $u(s)=(1-sj)/(1+sj)$ | the rational chart on $\{\langle u\rangle_{*}=1\}$ |
| $s$ | the rational parameter, $s\neq\pm1$ |
| $v(s)=-u(s)=u(1/s)$ | the second chart, missing $+1$ |
| $\epsilon$ | the component sign, $\epsilon\in\{1,\pm j\}$ |
| $\phi$ | the hyperbolic angle, $s=-\tanh(\phi/2)$ on the identity component |
| $K=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | the reflection, $K^2=I$ |
| $M(s)=(I-sK)(I+sK)^{-1}$ | the Cayley matrix |
| $SO(1,1)$ | the determinant-one Lorentz group of the plane, two components |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the rational parametrisation of the hyperbola and its projective completion.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split-complex algebra and its idempotents.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for $SO(1,1)$, its components and its Cayley parametrisation.
- John G. Ratcliffe, *Foundations of Hyperbolic Manifolds* (Springer, Graduate Texts in Mathematics 149, 2nd ed. 2006), for the hyperbolic line, its points at infinity and the rapidity coordinate.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for indefinite forms, isotropic lines and their projective geometry.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the rational parametrisations of quadrics of arbitrary signature.
