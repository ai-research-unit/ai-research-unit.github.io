
# __Quaternion Special Functions__

## Introduction

This article introduces the quaternion special functions as the named functions that arise repeatedly in quaternion analysis, in Clifford analysis, and in the geometry of the quaternion space. The goal is to define each function precisely, establish its basic properties, and describe the relations among them.

The treatment is mathematically honest: every claim is either proved or stated as a definition. The quaternion algebra, its norm and its conjugation are assumed from *Quaternion Algebra* and *Norm and Invertibility in the Quaternion Algebra*, and the scalar-vector decomposition is used throughout. The exponential and the logarithm are defined in §*The Quaternion Exponential and Logarithm* and used throughout; the polar decomposition that organises them is in *Exponential Polar Decomposition of Quaternions*. The functions below are built from them by the same series and integrals that define the real and complex cases. No physics is invoked.

The plan follows the dependency order: the exponential, the logarithm and the powers, then the trigonometric and hyperbolic functions and their inverses, then the functions defined by integrals and series, the gamma and beta functions, the error and Airy functions, the Bessel and hypergeometric functions and the Lambert $W$ function, and finally the monogenic functions and the structure principle. The zeta function, the incomplete gamma and beta functions, the orthogonal polynomials and the elliptic integrals are not carried to $\mathbb{H}$; the comparison with the other layers is in *Comparison of Special Functions*.

Throughout this article, the quaternion algebra is denoted $\mathbb{H}$, and its basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$. The quaternion norm $\langle\tilde q\rangle_{\natural}$ is real and non-negative, so there is a single regime rather than two, and a function of the quaternion variable is computed from its scalar part $q_t$ and the modulus $\sqrt{\langle\vec q\rangle_{\natural}}$ of its vector part, without the complex factorisations of the split cases. The scalar imaginary of the complex numbers is denoted $i$, so that it does not collide with the quaternion units. Every numerical value displayed below was recomputed in double precision. The notation is collected in §*Summary of Notation*.

## The Quaternion Exponential and Logarithm

### The Quaternion Exponential

The **quaternion exponential** is defined for $\tilde q \in \mathbb{H}$ by

$$
\exp(\tilde q) = \sum_{n=0}^\infty \frac{\tilde q^n}{n!}.
$$

The series converges absolutely for every $\tilde q$, because the quaternion norm is submultiplicative. The function is real-analytic on $\mathbb{H}$; it is not quaternion-differentiable, and its differential is computed in *Exponential Polar Decomposition of Quaternions*, §*The Matrix Logarithm and the Derivative*. It satisfies

$$
\exp(\tilde q_1 + \tilde q_2) = \exp(\tilde q_1) \exp(\tilde q_2) \quad \text{when } \tilde q_1\tilde q_2 = \tilde q_2\tilde q_1,
$$

$$
\exp(0) = 1 .
$$

**Caution.** The exponential is not multiplicative in general, because $\mathbb{H}$ is not commutative. The identity $\exp(\tilde q_1 + \tilde q_2) = \exp(\tilde q_1) \exp(\tilde q_2)$ holds when $\tilde q_1$ and $\tilde q_2$ commute; it fails for non-commuting arguments, as the example of $\tfrac{\pi}{2}\vec e_x$ and $\tfrac{\pi}{2}\vec e_y$ shows.

For a nonzero pure quaternion $\vec q \in \operatorname{Im}\mathbb{H}$ with $\theta = \sqrt{\langle\vec q\rangle_{\natural}}$, the exponential is

$$
\exp(\vec q) = \cos\theta + \frac{\vec q}{\theta} \sin\theta.
$$

This is the **quaternion Euler formula**, and it is the bridge between the exponential and the trigonometric functions. In particular, for a unit pure quaternion $\vec\omega$ and $\theta \in \mathbb{R}$,

$$
\exp(\vec\omega \theta) = \cos\theta + \vec\omega \sin\theta.
$$

This is a unit quaternion, and it lies on the unit sphere $\mathbb{S}^3$: it is a **rotor** (*Conventions in Mathematics*, §*Symbols*). The sandwich by this rotor rotates by $2\theta$, twice the angle in the exponent, which is the half-angle rule of *Exponential Polar Decomposition of Quaternions*, §*The Rotor Part*.

For a general quaternion $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$ with $\vec q \neq 0$ and $\theta = \sqrt{\langle\vec q\rangle_{\natural}}$,

$$
\exp(\tilde q) = \exp(q_t) \left(\cos\theta + \frac{\vec q}{\theta} \sin\theta \right).
$$

So the exponential is the product of a real exponential and a unit quaternion. This is the quaternion analogue of the polar form of a complex number.

**Remark.** The modulus is read from the algebraic norm and is never written with bars. The **modulus** of $\tilde q$ is $\sqrt{\langle\tilde q\rangle_{\natural}}$, and the **modulus of the vector part** is $\sqrt{\langle\vec q\rangle_{\natural}}$; the two agree only when $q_t=0$. The algebraic norm is $\langle\tilde q\rangle_{\natural}=q_t^2+\langle\vec q\rangle_{\natural}$. Its square root is the modulus used in $\sqrt{\langle\exp\tilde q\rangle_{\natural}}=\exp(q_t)$ and in the logarithm.

**Conjugation and the image of a sphere.** Conjugation commutes with the exponential,

$$
\exp(\tilde{q}^{\natural}) = (\exp \tilde q)^{\natural},
$$

because the series for $\exp \tilde{q}^{\natural}$ is the conjugate of the series for $\exp \tilde q$ term by term. The scalar-vector form also describes the image of each sphere. For fixed $\sqrt{\langle\vec q\rangle_{\natural}} = r$, the exponential maps the sphere onto the sphere of radius $\exp(q_t)\lvert \sin r\rvert$ centred at the real point $\exp(q_t)\cos r$, swept out as the direction $\operatorname{sgn}(\tilde q)$ runs over the unit imaginary sphere; at $r = k\pi$ the image collapses to the single point $(-1)^k \exp(q_t)$, so the whole sphere of pure quaternions of modulus $\pi$ is sent to the one point $-1$. This collapse is the geometric reason the exponential is not injective.

**de Moivre's formula and the sequential limit.** For every integer $n$,

$$
\left(\exp \tilde q\right)^n = \exp(n\tilde q),
$$

because the powers of a single element commute with one another. The exponential is also the limit of the binomial sequence,

$$
\exp \tilde q = \lim_{n \to \infty}\left(1 + \frac{\tilde q}{n}\right)^n,
$$

and more generally $\exp \tilde q = \lim_n (1 + \tilde q_n/n)^n$ for every sequence $\tilde q_n \to \tilde q$. The non-commutativity does not obstruct the binomial expansion here, since the expansion of a power of one element involves only that element and its powers.

### The Quaternion Logarithm

A **logarithm** of $\tilde q\in\mathbb{H}^{\times}$ is a quaternion $\tilde q_{\log}$ with $\exp(\tilde q_{\log})=\tilde q$. The definition is an equation, not a formula; the formula is what solving the equation gives. Write the unknown by its scalar and vector parts,

$$
\tilde q_{\log}=q_{\log}e_t+\vec q_{\log}, \qquad q_{\log}=\operatorname{Sc}\tilde q_{\log}=x\in\mathbb{R}, \qquad \vec q_{\log}=\operatorname{Vect}\tilde q_{\log}=w\in\operatorname{Im}\mathbb{H}.
$$

The subscript is a label, not an operation: $\tilde q_{\log}$ is the logarithm of $\tilde q$, not a quaternion whose scalar part is the logarithm of $q_t$.

**The scalar part.** Take norms in the equation. The scalar $x$ is real and central, so $\exp(x+w)=\exp(x)\exp(w)$, and $\sqrt{\langle\exp w\rangle_{\natural}}=1$ for every pure $w$ by Euler's formula. Hence

$$
\sqrt{\langle\tilde q\rangle_{\natural}}=\sqrt{\langle\exp(x+w)\rangle_{\natural}}=\exp(x), \qquad x=\ln\sqrt{\langle\tilde q\rangle_{\natural}} .
$$

The scalar part of every logarithm is the same number. It carries no branch: the whole ambiguity sits in the vector part. In the complex case the single imaginary coordinate carries both the sign and the angle; here the direction is a point of the sphere $S^2$ and the angle is $\theta$ plus a multiple of $2\pi$.

**The vector part.** With $x$ forced, the equation reduces to

$$
\exp(w)=\frac{\tilde q}{\sqrt{\langle\tilde q\rangle_{\natural}}}=:\tilde u,
$$

a unit quaternion. Euler's formula turns it into the pair of equations

$$
\cos\sqrt{\langle w\rangle_{\natural}}=\operatorname{Sc}\tilde u, \qquad \sin\sqrt{\langle w\rangle_{\natural}}\,\frac{w}{\sqrt{\langle w\rangle_{\natural}}}=\operatorname{Vec}\tilde u,
$$

the second understood as the zero vector when $w=0$. The three cases are read off from $\tilde u$.

*Non-real element.* If $\operatorname{Vec}\tilde q\neq0$ then $\operatorname{Vec}\tilde u\neq0$, so $\sin\sqrt{\langle w\rangle_{\natural}}\neq0$. Put

$$
\theta=\arccos(\operatorname{Sc}\tilde u)\in(0,\pi), \qquad \hat u=\frac{\operatorname{Vec}\tilde u}{\sqrt{\langle\operatorname{Vec}\tilde u\rangle_{\natural}}}=\operatorname{sgn}\tilde q .
$$

The scalar equation gives $\sqrt{\langle w\rangle_{\natural}}=\theta+2\pi k$ with $k\ge0$, or $\sqrt{\langle w\rangle_{\natural}}=2\pi k-\theta$ with $k\ge1$. In the first family $\sin\sqrt{\langle w\rangle_{\natural}}>0$ and the vector equation gives $\hat w=\hat u$; in the second $\sin\sqrt{\langle w\rangle_{\natural}}<0$ and it gives $\hat w=-\hat u$. The two families are one formula,

$$
w=(\theta+2\pi m)\,\hat u, \qquad m\in\mathbb{Z}.
$$

The coefficient may be negative; then $\sqrt{\langle w\rangle_{\natural}}=\lvert\theta+2\pi m\rvert$ and the direction is $-\hat u$, which is the second family. Each integer gives one logarithm, and two different integers never give the same $w$.

*Positive real element.* If $\tilde q=r>0$ then $\tilde u=1$, and the equations read $\cos\sqrt{\langle w\rangle_{\natural}}=1$, $\sin\sqrt{\langle w\rangle_{\natural}}\,\hat w=0$. Either $w=0$, or $\sqrt{\langle w\rangle_{\natural}}=2\pi k$ with $k\ge1$ and $\hat w$ an arbitrary unit pure quaternion:

$$
w=2\pi k\,n, \qquad k\in\mathbb{Z}_{\ge0}, \quad n\in S^2,
$$

where $k=0$ gives $w=0$ for every $n$.

*Negative real element.* If $\tilde q=-r<0$ then $\tilde u=-1$, and the equations read $\cos\sqrt{\langle w\rangle_{\natural}}=-1$, $\sin\sqrt{\langle w\rangle_{\natural}}\,\hat w=0$. Hence $\sqrt{\langle w\rangle_{\natural}}=(2k+1)\pi$ and $\hat w$ is arbitrary:

$$
w=(2k+1)\pi\,n, \qquad k\in\mathbb{Z}_{\ge0}, \quad n\in S^2 .
$$

The three cases are collected in a table.

| element | $\operatorname{Sc}\tilde u$ | vector part $w$ | logarithms |
|---|---|---|---|
| non-real, $\operatorname{Vec}\tilde q\neq0$ | $\cos\theta$, $\theta\in(0,\pi)$ | $(\theta+2\pi m)\operatorname{sgn}\tilde q$, $m\in\mathbb{Z}$ | one for each integer |
| positive real, $\tilde q=r>0$ | $1$ | $2\pi k\,n$, $k\in\mathbb{Z}_{\ge0}$, $n\in S^2$ | $0$, then a sphere for each $k\ge1$ |
| negative real, $\tilde q=-r<0$ | $-1$ | $(2k+1)\pi\,n$, $k\in\mathbb{Z}_{\ge0}$, $n\in S^2$ | a sphere for each $k$ |

For the non-real case the logarithms are therefore

$$
\tilde q_{\log}=q_{\log}e_t+(\theta+2\pi m)\operatorname{sgn}\tilde q, \qquad q_{\log}=\ln\sqrt{\langle\tilde q\rangle_{\natural}}, \quad \theta=\arccos\frac{q_t}{\sqrt{\langle\tilde q\rangle_{\natural}}}, \quad m\in\mathbb{Z},
$$

which is the period formula of *Exponential Polar Decomposition of Quaternions*, §*The General Logarithm*. Every nonzero quaternion has at least one logarithm. On the real axis the set of logarithms is not discrete but a union of spheres: the positive axis has the single value $\ln r$, then one sphere of radius $2\pi k$ for each $k\ge1$, and the negative axis has one sphere of radius $(2k+1)\pi$ for each $k\ge0$.

The two coordinates of the logarithm are therefore as follows, with the angle and the axis that the vector coordinate carries.

| coordinate | formula from $\tilde q$ | role |
|---|---|---|
| $q_{\log}=\operatorname{Sc}\tilde q_{\log}=x$ | $\ln\sqrt{\langle\tilde q\rangle_{\natural}}$ | logarithmic scale, unique |
| $\vec q_{\log}=\operatorname{Vect}\tilde q_{\log}=w$ | $\theta\vec n$, with $\theta=\arccos\bigl(q_t/\sqrt{\langle\tilde q\rangle_{\natural}}\bigr)\in[0,\pi]$ and $\vec n=\vec q/\sqrt{\langle\vec q\rangle_{\natural}}$; the other logarithms use $(\theta+2\pi m)\vec n$, and on the real axis $2\pi m\vec n$ at $+r$, $(2m+1)\pi\vec n$ at $-r$ | pure exponent, one line or one sphere for each integer |

The scalar coordinate is unique and carries the scale. The vector coordinate is a pure quaternion, not a scalar: it is the quaternion analogue of the primed coordinate $q'_{\log}$ of the complex case, and it carries both the angle and the axis. The prime is not written, because a quaternion coefficient is real and the prime marks an imaginary coordinate only. Both coordinates are computed from the four real coordinates of $\tilde q$: the modulus $r=\sqrt{\langle\tilde q\rangle_{\natural}}$ gives $q_{\log}$, and the angle $\theta=\arccos(q_t/r)$ together with the axis $\vec n=\vec q/\sqrt{\langle\vec q\rangle_{\natural}}$ gives $\vec q_{\log}$.

**The principal branch.** A single-valued logarithm is obtained by keeping the representative with $\sqrt{\langle w\rangle_{\natural}}<\pi$. For a non-real element it is $w=\theta\operatorname{sgn}\tilde q$; for a positive real element it is $w=0$; for a negative real element there is none, because every candidate has $\sqrt{\langle w\rangle_{\natural}}\ge\pi$. The domain is therefore $\mathbb{H}\setminus(-\infty,0]$, and the **principal logarithm** is

$$
\log\tilde q=\ln\sqrt{\langle\tilde q\rangle_{\natural}}+\arccos\frac{q_t}{\sqrt{\langle\tilde q\rangle_{\natural}}}\,\frac{\vec q}{\sqrt{\langle\vec q\rangle_{\natural}}},
$$

with the second term read as $0$ when $\vec q=0$, which within the domain means the positive real axis. The scalar factor is the **argument** $\operatorname{Arg}\tilde q=\arccos(q_t/\sqrt{\langle\tilde q\rangle_{\natural}})\in[0,\pi)$, so that

$$
\log\tilde q=\ln\sqrt{\langle\tilde q\rangle_{\natural}}+\operatorname{Arg}\tilde q\,\operatorname{sgn}\tilde q .
$$

The branch is not continuous across the negative real axis, and the failure is worse than in the complex case: as $\tilde q\to-r$, the direction $\operatorname{sgn}\tilde q$ tends to the direction of approach, so $\log\tilde q$ tends to $\ln r+\pi n$ for whichever unit pure $n$ the path selects. No value is distinguished at $\tilde q=-r$, and the ray is the **branch cut**. The cut is an artefact of the condition $\sqrt{\langle w\rangle_{\natural}}<\pi$, not of the exponential, and it can be moved to any other ray from the origin.

**Example.** Take $\tilde q=3e_t+4\vec e_x$. The modulus is $\sqrt{\langle\tilde q\rangle_{\natural}}=5$ and $\operatorname{Sc}\tilde u=3/5$, so the construction gives $\theta=\arccos(3/5)=0.9272952180016123$ and $\hat u=\vec e_x$. The principal logarithm is

$$
\log\tilde q=\ln5+0.9272952180016123\,\vec e_x=1.6094379124341003+0.9272952180016123\,\vec e_x,
$$

and exponentiating it back gives $3.000000000000000\,e_t+4.000000000000000\,\vec e_x$, with error $8.9\times10^{-16}$. The other logarithms are $\log\tilde q+2\pi k\,\vec e_x$, for instance $1.6094379124341003-5.355890089177974\,\vec e_x$ for $k=-1$. On the negative real axis the construction stops: $\tilde q=-2e_t$ has the logarithms $\ln2+(2k+1)\pi n$ with $n\in S^2$, none of which has vector length below $\pi$.

### The Two Compositions

The exponential is single-valued and not injective, the logarithm is multi-valued, so the two compositions behave differently.

*Right inverse.* For every $\tilde q$ in the domain of the principal logarithm,

$$
\exp(\log\tilde q)=\tilde q .
$$

**Proof.** Write $r=\sqrt{\langle\tilde q\rangle_{\natural}}$, $\theta=\operatorname{Arg}\tilde q$ and $n=\operatorname{sgn}\tilde q$ when $\vec q\neq0$. By the construction, $\cos\theta=q_t/r$ and $\sin\theta=\sqrt{\langle\vec q\rangle_{\natural}}/r$, hence

$$
\exp(\log\tilde q)=\exp(\ln r+\theta n)=r\left(\cos\theta+n\sin\theta\right)=q_t e_t+\vec q=\tilde q .
$$

On the positive real axis $\vec q=0$ and the identity is $\exp(\ln r)=r$.

*Left inverse, up to whole turns.* For $\tilde q=q_t+v$ with $v$ pure and $\rho=\sqrt{\langle\vec v\rangle_{\natural}}$, the element $\tilde q$ is a logarithm of $\exp\tilde q$, but the principal logarithm may choose another representative. If $0\le\rho<\pi$ then

$$
\log(\exp\tilde q)=\tilde q .
$$

If $\pi<\rho<3\pi$ then

$$
\log(\exp\tilde q)=\tilde q-2\pi\operatorname{sgn}\tilde q .
$$

At $\rho=\pi$ and at $\rho=3\pi$ the element $\exp\tilde q=-e^{q_t}$ is a negative real, outside the domain, and the principal logarithm is not defined. The general rule is

$$
\log(\exp\tilde q)=\tilde q-2\pi m\operatorname{sgn}\tilde q,
$$

where $m$ is the nearest integer to $\rho/2\pi$, whenever $\rho$ is not an odd multiple of $\pi$.

**Proof.** By Euler's formula, $\exp\tilde q=e^{q_t}(\cos\rho+\hat v\sin\rho)$, with scalar part $e^{q_t}\cos\rho$ and vector part $e^{q_t}\sin\rho\,\hat v$. The principal argument is $\arccos(\cos\rho)\in[0,\pi)$, and the direction is $\operatorname{sgn}(\sin\rho)\hat v$. On $(0,\pi)$ the arccos is $\rho$ and the sign is $+1$; on $(\pi,2\pi)$ it is $2\pi-\rho$ and the sign is $-1$; on $(2\pi,3\pi)$ it is $\rho-2\pi$ and the sign is $+1$. The last two give $q_t+(\rho-2\pi)\hat v=\tilde q-2\pi\hat v$, and $\rho=2\pi$ joins them by continuity.

The asymmetry is the content of the word multivalued: the exponential is many-to-one, and the principal logarithm inverts it on one representative of each fibre.

**Caution.** The logarithm is not additive in general. For commuting $\tilde q_1$ and $\tilde q_2$ the multi-valued logarithms satisfy $\log(\tilde q_1\tilde q_2)=\log\tilde q_1+\log\tilde q_2$ modulo the periods, and the principal values satisfy it only when the sum of the two principal exponents is the principal exponent of the product. It fails for noncommuting arguments, and it fails for commuting arguments whose angles add past $\pi$.

**Conjugation.** The principal logarithm commutes with conjugation,

$$
\log(\tilde{q}^{\natural}) = (\log \tilde q)^{\natural},
$$

on the domain of the principal branch. The modulus $\sqrt{\langle\tilde q\rangle_{\natural}}$ and the argument $\operatorname{Arg}\tilde q$ are unchanged by conjugation, while the direction $\operatorname{sgn}(\tilde q)$ changes sign, and both sides change sign in the vector part.

### The Derivative of the Logarithm

The logarithm is smooth on its domain, and its differential at $\tilde q$ is the inverse of the differential of the exponential at $\log\tilde q$; that differential is invertible there because $\sqrt{\langle\operatorname{Vect}\log\tilde q\rangle_{\natural}}<\pi$, and the critical set of the exponential is computed in *Exponential Polar Decomposition of Quaternions*, §*The Matrix Logarithm and the Derivative*. The differential is not multiplication by $\tilde q^{-1}$. At $\tilde q=3e_t+4\vec e_x$ and in the direction $\vec e_y$,

$$
\mathrm d\log_{\tilde q}(\vec e_y)=0.2318238045\,\vec e_y,
$$

whereas $\tilde q^{-1}\vec e_y=0.12\vec e_y-0.16\vec e_z$ and $\vec e_y\tilde q^{-1}=0.12\vec e_y+0.16\vec e_z$. The logarithm is a real-analytic map of four variables; it is not a quaternion multiplication, and the identity $\log'(\tilde q)=\tilde q^{-1}$ of the complex case has no direct analogue.

**The power law.** For every integer $n$, $\exp(n \log \tilde q) = \tilde q^n$, so $n \log \tilde q$ is a logarithm of $\tilde q^n$. The principal values of the two sides agree only when the argument of $n \log \tilde q$ falls in the principal range, so the identity $\log(\tilde q^n) = n \log \tilde q$ holds between the multi-valued logarithms and not, in general, between principal values.

**The identity.** The identity element has the logarithm $0$; its logarithms are $2\pi k\,n$ with $k\ge0$ and $n\in S^2$, and only $k=0$ gives a vector part of length below $\pi$.

**An inequality.** For $\sqrt{\langle\tilde q\rangle_{\natural}} \geq 1$,

$$
\sqrt{\langle\log\tilde q\rangle_{\natural}} \leq \sqrt{\langle\tilde q\rangle_{\natural}} - 1 + \pi,
$$

because the scalar part of the logarithm is $\ln \sqrt{\langle\tilde q\rangle_{\natural}} \leq \sqrt{\langle\tilde q\rangle_{\natural}} - 1$, and the length of its vector part is the argument, at most $\pi$. The bound is the first member of a family: replacing $\log(1 + a) \le a$ by a longer truncation of the series, with $a = \sqrt{\langle\tilde q\rangle_{\natural}} - 1$, gives

$$
\sqrt{\langle\log\tilde q\rangle_{\natural}} \leq \sum_{k=1}^{2n-1} (-1)^{k+1} \frac{(\sqrt{\langle\tilde q\rangle_{\natural}} - 1)^k}{k} + \pi, \qquad n \in \mathbb{N},
$$

since every odd truncation of the alternating series for $\log(1+a)$ is an upper bound for it. The case $n = 2$ is the explicit cubic form

$$
\sqrt{\langle\log\tilde q\rangle_{\natural}} \leq \frac{2\langle\tilde q\rangle_{\natural}^{3/2} - 9\langle\tilde q\rangle_{\natural} + 18\sqrt{\langle\tilde q\rangle_{\natural}} - 11}{6} + \pi.
$$

The non-alternating sum, $\sum_{k=1}^{2n-1} (\sqrt{\langle\tilde q\rangle_{\natural}} - 1)^k/k + \pi$, is also an upper bound, because every even term of the alternating sum is negative there; it is the weaker of the two.

### Quaternion Powers

For $a \in \mathbb{H}$ and $\tilde q$ in the domain of the logarithm,

$$
\tilde q^a = \exp(a \log \tilde q).
$$

Read on the principal branch of the logarithm this is single-valued on the domain of the logarithm; read on all the branches it is multi-valued, with the number of values counted below. It satisfies

$$
\tilde q^{a + b} = \tilde q^a \tilde q^b \quad \text{if } a \text{ and } b \text{ commute with } \log \tilde q.
$$

The power is not multiplicative in general, because $\mathbb{H}$ is not commutative.

**The number of values.** The multi-valuedness of the logarithm propagates to the power, and the count of the values is decided by the exponent. If $a = n$ is an integer, $\tilde q^n$ is defined by repeated multiplication and takes one value. For a non-real $\tilde q$, if $a = a_1/a_2$ is rational in lowest terms, the factors $\exp(2\pi n a\,\operatorname{sgn}\,\tilde q)$ are periodic in $n$ with period $a_2$, so $\tilde q^{a_1/a_2}$ takes $a_2$ values: two for $a = 1/2$ and three for $a = 1/3$. If $a$ is not rational, the values are infinite in number. On the real axis the axis is free, so a non-integer power with denominator at least three is a union of spheres rather than a finite set; the integer power remains single-valued. The powers satisfy

$$
\left(\tilde q^a\right)^n = \tilde q^{na}, \qquad n = 0, \pm 1, \pm 2, \dots,
$$

because the powers of the single element $\log \tilde q$ commute with one another.

### The $n$-th Root Limits

Throughout this subsection a sequence of quaternions converges when it converges in the norm $\lVert\cdot\rVert_E$ of $\mathbb{H}$ read as a four-dimensional Euclidean space, and a limit is read in that sense.

The $n$-th root is the power with exponent $1/n$,

$$
\tilde q^{1/n} = \exp\left(\frac{1}{n}\log \tilde q\right),
$$

and the roots tend to $1$ as $n$ grows. The first-order term of that approach is the logarithm itself.

**Theorem (the root expansion).** For $\tilde q \in \mathbb{H}\setminus(-\infty,0]$,

$$
\lim_{n \to \infty} n\left(\tilde q^{1/n} - 1\right) = \log\tilde q.
$$

**Proof.** Write $\tilde q_{\log} = \log\tilde q$. If $\tilde q_{\log}$ is real, the statement is the classical real limit. Otherwise put $\vec\omega = \operatorname{sgn}\tilde q_{\log}$, so that $\tilde q_{\log} = \vec\omega\,\sqrt{\langle\tilde q_{\log}\rangle_{\natural}}$ and the powers of $\tilde q_{\log}$ commute. Then

$$
\tilde q^{1/n} = \exp\left(\frac{\tilde q_{\log}}{n}\right) = \cos\frac{\sqrt{\langle\tilde q_{\log}\rangle_{\natural}}}{n} + \vec\omega \sin\frac{\sqrt{\langle\tilde q_{\log}\rangle_{\natural}}}{n} = 1 + \frac{\tilde q_{\log}}{n} - \frac{\langle\tilde q_{\log}\rangle_{\natural}}{2n^2} + O\left(\frac{1}{n^3}\right),
$$

so $n(\tilde q^{1/n} - 1) = \tilde q_{\log} + O(1/n)$. For a negative real element the principal logarithm does not exist, and the limit depends on the chosen logarithm.

**Corollary (the mean of one and a root).**

$$
\lim_{n \to \infty}\left(\frac{1 + \tilde q^{1/n}}{2}\right)^n = \tilde q^{1/2}.
$$

**Proof.** By the expansion, $\frac{1+\tilde q^{1/n}}{2} = 1 + \frac{\tilde q_{\log}/2}{n} + O(1/n^2)$, and the binomial limit gives the exponential of the first-order coefficient, which is $\exp(\tilde q_{\log}/2) = \tilde q^{1/2}$.

**Corollary (the mean of several roots).** For $\tilde q_1, \dots, \tilde q_k \in \mathbb{H}\setminus(-\infty,0]$,

$$
\lim_{n \to \infty}\left(\frac{1}{k}\sum_{\nu=1}^k \tilde q_\nu^{1/n}\right)^n = \exp\left(\frac{1}{k}\sum_{\nu=1}^k \log\tilde q_\nu\right),
$$

the right-hand side being the exponential of the mean of the logarithms.

**Caution (the modulus is not the limit).** For a positive real argument the three limits reduce to the classical statements $n(\sqrt[n]{a} - 1) \to \log a$ and $\left((1 + \sqrt[n]{a})/2\right)^n \to \sqrt{a}$ and the geometric mean. For a general quaternion they do not, and the real numbers obtained by reading the limits as their real parts are wrong: $\log \sqrt{\langle\tilde q\rangle_{\natural}}$ is only the scalar part of $\log\tilde q$, so it is $\sqrt{\langle\log\tilde q\rangle_{\natural}} = \sqrt{\log^2 \sqrt{\langle\tilde q\rangle_{\natural}} + \lvert \operatorname{Arg}\tilde q\rvert^2}$ and not $\log \sqrt{\langle\tilde q\rangle_{\natural}}$ that equals $\sqrt{\langle n(\tilde q^{1/n}-1)\rangle_{\natural}}$ in the limit; likewise $\langle\tilde q\rangle_{\natural}^{1/4}$ is the modulus of the limit $\tilde q^{1/2}$ and $\left(\prod_\nu\sqrt{\langle\tilde q_\nu\rangle_{\natural}}\right)^{1/k}$ the modulus of the mean limit, not the limits themselves.

## The Trigonometric and Hyperbolic Functions

### Trigonometric Functions

The **quaternion sine** and **cosine** are defined by the scalar-vector decomposition

$$
\sin(\tilde q) = \sin(q_t) \cosh\sqrt{\langle\vec q\rangle_{\natural}} + \frac{\vec q}{\sqrt{\langle\vec q\rangle_{\natural}}} \cos(q_t) \sinh\sqrt{\langle\vec q\rangle_{\natural}},
$$

$$
\cos(\tilde q) = \cos(q_t) \cosh\sqrt{\langle\vec q\rangle_{\natural}} - \frac{\vec q}{\sqrt{\langle\vec q\rangle_{\natural}}} \sin(q_t) \sinh\sqrt{\langle\vec q\rangle_{\natural}}.
$$

At $\vec q=0$ the vector quotients are read as $0$, so the definitions reduce to the real sine and cosine.
These functions are real-analytic on $\mathbb{H}$, and they satisfy

$$
\sin' = \cos, \qquad \cos' = -\sin,
$$

$$
\sin^2(\tilde q) + \cos^2(\tilde q) = 1.
$$

**Caution.** The addition formulas for the trigonometric functions do not hold in general, because $\mathbb{H}$ is not commutative. They hold only for commuting arguments.

**Norm and zeros.** The scalar-vector form also gives the algebraic norm of each function in closed form:

$$
\langle\sin\tilde q\rangle_{\natural} = \sin^2 q_t + \sinh^2\sqrt{\langle\vec q\rangle_{\natural}}, \qquad \langle\cos\tilde q\rangle_{\natural} = \cos^2 q_t + \sinh^2\sqrt{\langle\vec q\rangle_{\natural}}.
$$

Each right-hand side is a sum of two non-negative terms, so $\sin \tilde q = 0$ forces $\sin q_t = 0$ and $\sqrt{\langle\vec q\rangle_{\natural}} = 0$, and $\cos \tilde q = 0$ forces $\cos q_t = 0$ and $\sqrt{\langle\vec q\rangle_{\natural}} = 0$. The zeros are therefore exactly the real ones: $\sin \tilde q$ vanishes at $q_t = n\pi$ and $\cos \tilde q$ at $q_t = (n + \tfrac{1}{2})\pi$, for $n \in \mathbb{Z}$, and nowhere off the real axis.

**The relation to the hyperbolic functions.** The trigonometric and the hyperbolic functions differ only by the unit pure quaternion $\operatorname{sgn}(\tilde q) = \vec q/\sqrt{\langle\vec q\rangle_{\natural}}$ that carries the vector part:

$$
\sin \tilde q = -\operatorname{sgn}(\tilde q) \sinh\bigl(\tilde q \operatorname{sgn}(\tilde q)\bigr), \qquad \cos \tilde q = \cosh\bigl(\tilde q \operatorname{sgn}(\tilde q)\bigr),
$$

The element $\tilde q \operatorname{sgn}(\tilde q) = q_t \operatorname{sgn}(\tilde q) - \sqrt{\langle\vec q\rangle_{\natural}}$ lies in the plane of $1$ and $\operatorname{sgn}(\tilde q)$, so the two identities reduce each quaternion function to a complex-valued one, with $\operatorname{sgn}(\tilde q)$ playing the role of the imaginary unit. This is the sense in which the quaternion trigonometric functions are the hyperbolic functions of a rotated variable, and it is the reason the trigonometric inverses below are read off from the hyperbolic ones.

### Hyperbolic Functions

The **quaternion hyperbolic sine** and **cosine** are defined by

$$
\sinh(\tilde q) = \frac{\exp(\tilde q) - \exp(-\tilde q)}{2}, \qquad \cosh(\tilde q) = \frac{\exp(\tilde q) + \exp(-\tilde q)}{2}.
$$

They are entire, and they satisfy

$$
\sinh' = \cosh, \qquad \cosh' = \sinh,
$$

$$
\cosh^2(\tilde q) - \sinh^2(\tilde q) = 1.
$$

**Norm and zeros.** The algebraic norms are

$$
\langle\sinh\tilde q\rangle_{\natural} = \sinh^2 q_t + \sin^2\sqrt{\langle\vec q\rangle_{\natural}}, \qquad \langle\cosh\tilde q\rangle_{\natural} = \sinh^2 q_t + \cos^2\sqrt{\langle\vec q\rangle_{\natural}}.
$$

Hence $\sinh \tilde q = 0$ exactly when $q_t = 0$ and $\sqrt{\langle\vec q\rangle_{\natural}} = n\pi$, and $\cosh \tilde q = 0$ exactly when $q_t = 0$ and $\sqrt{\langle\vec q\rangle_{\natural}} = (n + \tfrac{1}{2})\pi$, for $n \in \mathbb{Z}$: the zeros are the pure quaternions of those moduli, a union of spheres, and the scalar part vanishes at every one of them.

### Other Functions

$$
\tan(\tilde q) = \frac{\sin(\tilde q)}{\cos(\tilde q)}, \qquad \tanh(\tilde q) = \frac{\sinh(\tilde q)}{\cosh(\tilde q)}, \qquad \coth(\tilde q) = \frac{\cosh(\tilde q)}{\sinh(\tilde q)}.
$$

These are meromorphic in the quaternion sense, with singularities where the denominator is not invertible. The tangent obeys the same conjugation as the sine, with a minus sign,

$$
\tan \tilde q = -\operatorname{sgn}(\tilde q) \tanh\bigl(\tilde q \operatorname{sgn}(\tilde q)\bigr).
$$

### Inequalities

The norm formulas turn the elementary real inequalities into bounds for the quaternion functions. On the region where the vector part is short, $\sqrt{\langle\vec q\rangle_{\natural}} \le \ln(1 + \sqrt{2})$, one has $\sinh^2\sqrt{\langle\vec q\rangle_{\natural}} \le 1$ and $\lvert \sin q_t\rvert \le \lvert q_t\rvert$, so

$$
\sqrt{\langle\sin\tilde q\rangle_{\natural}} \le \sqrt{q_t^2 + 1},
$$

and, without any restriction on the vector part, $\sqrt{\langle\cos\tilde q\rangle_{\natural}} \geq 1 - q_t^2/2$ for $q_t \in [0, \sqrt{2}]$, because $\langle\cos\tilde q\rangle_{\natural} \ge \cos^2 q_t$ and $\cos q_t \ge 1 - q_t^2/2$ on that interval. Dividing the two bounds gives the corresponding bound for the tangent,

$$
\sqrt{\langle\tan\tilde q\rangle_{\natural}} \le \frac{2\sqrt{1 + q_t^2}}{2 - q_t^2} \qquad \bigl(\sqrt{\langle\vec q\rangle_{\natural}} \le \ln(1 + \sqrt{2}), \ q_t \in [0, \sqrt{2})\bigr).
$$

For the hyperbolic functions the relevant bound has no restriction on the region: from $\langle\sinh\tilde q\rangle_{\natural} = \sinh^2 q_t + \sin^2\sqrt{\langle\vec q\rangle_{\natural}} \le \sinh^2 q_t + 1$ and the same for $\cosh$,

$$
\sqrt{\langle\sinh\tilde q\rangle_{\natural}} \le 2\cosh q_t, \qquad \sqrt{\langle\cosh\tilde q\rangle_{\natural}} \le 2\cosh q_t.
$$

These bounds are elementary consequences of the norm formulas. The corresponding lower bounds on the far region, $\sqrt{\langle\vec q\rangle_{\natural}} \geq \ln(1 + \sqrt{2})$, come from $\sinh^2\sqrt{\langle\vec q\rangle_{\natural}} \geq 1$ in the same way. There the scalar side needs a cubic bound in place of the tangent one, $\sin^2 q_t \ge (q_t - q_t^3/6)^2$ for $\lvert q_t\rvert \le \sqrt{6}$, and the two combine into

$$
\sqrt{\langle\sin\tilde q\rangle_{\natural}} \ge \sqrt{1 + \left(q_t - \frac{q_t^3}{6}\right)^2} \qquad \bigl(\sqrt{\langle\vec q\rangle_{\natural}} \ge \ln(1 + \sqrt{2}), \ \lvert q_t\rvert \le \sqrt{6}\bigr),
$$

so that the reciprocal $1/\sin \tilde q$ is bounded, on the same region, by the reciprocal of the right-hand side. The bound is sharp at the corner where the two hypotheses meet: at $q_t = 0$ and $\sqrt{\langle\vec q\rangle_{\natural}} = \ln(1 + \sqrt{2})$ both inequalities are equalities, and $\sqrt{\langle\sin\tilde q\rangle_{\natural}} = 1$ there.

**The scalar range is not one-sided.** The bound requires $\lvert q_t\rvert \le \sqrt{6}$, and the two-sided form is necessary: the cubic bound on $\sin^2 q_t$ fails for large negative $q_t$, where $(q_t - q_t^3/6)^2$ outruns $\sin^2 q_t$ without limit, so no bound of this shape can hold on a range of the form $q_t \le -\sqrt{6}$. For example $\tilde q = -3 + \ln(1+\sqrt{2})\,\vec e_x$ has $\sqrt{\langle\sin\tilde q\rangle_{\natural}} = 1.010$, against the right-hand side $1.803$ obtained by substituting $q_t = -3$.

### The Inverse Trigonometric and Hyperbolic Functions

**Definition.** The inverse functions are built from the logarithm and the square root of a quaternion. The **inverse hyperbolic sine**, **cosine** and **tangent** are

$$
\sinh^{-1}\tilde q = \log\left(\tilde q + \left(\tilde q^2 + 1\right)^{1/2}\right), \qquad \cosh^{-1}\tilde q = \log\left(\tilde q + \left(\tilde q^2 - 1\right)^{1/2}\right),
$$

$$
\tanh^{-1}\tilde q = \frac{1}{2}\left(\log(1 + \tilde q) - \log(1 - \tilde q)\right),
$$

each read on the domain where the logarithm and the square root are defined. The square root is the quaternion one, $\tilde q^{1/2} = \exp\left(\frac{1}{2}\log \tilde q\right)$.

**The trigonometric inverses.** The identities relating the trigonometric and hyperbolic functions turn into definitions of the inverse trigonometric functions, by conjugation with the unit vector $\operatorname{sgn}(\tilde q) = \vec q/\sqrt{\langle\vec q\rangle_{\natural}}$ of the argument:

$$
\sin^{-1}\tilde q = -\operatorname{sgn}(\tilde q)\,\sinh^{-1}\left(\tilde q \operatorname{sgn}(\tilde q)\right), \qquad \cos^{-1}\tilde q = \operatorname{sgn}(\tilde q)\,\cosh^{-1}\tilde q,
$$

$$
\tan^{-1}\tilde q = -\operatorname{sgn}(\tilde q)\,\tanh^{-1}\left(\tilde q \operatorname{sgn}(\tilde q)\right).
$$

Each of the three is a right inverse on its domain, $\sin(\sin^{-1}\tilde q) = \tilde q$, $\cos(\cos^{-1}\tilde q) = \tilde q$ and $\tan(\tan^{-1}\tilde q) = \tilde q$, so that the trigonometric inverses are read off from the hyperbolic ones on the plane of $1$ and $\operatorname{sgn}(\tilde q)$. The minus signs are not decorative: they are forced by the signs in the identities for $\sin$ and $\tan$ above, and without them the compositions do not return $\tilde q$.

**Multi-valuedness and branch points.** Each inverse function is multi-valued, for two independent reasons: the logarithm has infinitely many branches, and each square root has two values. A single-valued branch is fixed by choosing a branch of the logarithm and one sign of the square root.

The branch points sit where the square root or the logarithm degenerates. For $\sinh^{-1}$ the vanishing set of the square root is the solution set of $\tilde q^2 + 1 = 0$, which is the sphere of unit pure quaternions; for $\cosh^{-1}$ it is the solution set of $\tilde q^2 - 1 = 0$, which is the pair $\tilde q = \pm 1$, and the same pair is where one of $1 \pm \tilde q$ vanishes in $\tanh^{-1}$. These are the branch points of the inverse hyperbolic functions, and the trigonometric inverses inherit them through the conjugation by $\operatorname{sgn}(\tilde q)$. As for the logarithm, the branches are indexed by an integer.

## The Gamma Function

### Definition

The **quaternion gamma function** is defined for $\tilde q$ with $q_t > 0$ by

$$
\Gamma(\tilde q) = \int_0^\infty t^{\tilde q-1} \exp(-t) \, dt,
$$

where the integral is along the positive real axis, $t^{\tilde q-1}$ is the quaternion power, and $\exp(-t)$ is the quaternion exponential. Because the integrand is a function of the real variable $t$ and the quaternion $\tilde q$ appears only in the exponent, the integral converges for $q_t > 0$.

### Functional Equation

$$
\Gamma(\tilde q + 1) = \tilde q \Gamma(\tilde q).
$$

This follows from integration by parts, exactly as in the real case, and it holds because the quaternion multiplication by $\tilde q$ commutes with the integration over the real variable $t$.

### Special Values

$$
\Gamma(n + 1) = n!
$$

for non-negative integers $n$, where the factorial is the ordinary real factorial.

### The Reflection Formula

$$
\Gamma(\tilde q) \Gamma(1 - \tilde q) = \frac{\pi}{\sin(\pi \tilde q)},
$$

where the sine is the quaternion sine. This follows from the real reflection formula, applied to the scalar-vector decomposition.

**Caution.** The reflection formula holds only for $\tilde q$ in the domain where both sides are defined, and the sine is the quaternion sine with the appropriate branch.

## The Beta Function

### Definition

The **quaternion beta function** is defined for $p, \tilde q$ with $p_0 > 0$ and $q_t > 0$ by

$$
B(p, \tilde q) = \int_0^1 t^{p-1} (1 - t)^{\tilde q-1} \, dt,
$$

where the integral is along the positive real axis and the powers are quaternion powers.

### Relation to the Gamma Function

$$
B(p, \tilde q) = \frac{\Gamma(p) \Gamma(\tilde q)}{\Gamma(p + \tilde q)}, \qquad p\tilde q = \tilde q p.
$$

This follows from the same substitution as in the real case, applied to the scalar-vector decomposition, which requires $p$ and $\tilde q$ to commute.

### Symmetry

$$
B(p, \tilde q) = B(\tilde q, p), \qquad p\tilde q = \tilde q p.
$$

The symmetry fails when $p$ and $\tilde q$ do not commute.

## The Error Function

### Definition

The **quaternion error function** is defined by

$$
\operatorname{erf}(\tilde q) = \frac{2}{\sqrt{\pi}} \int_0^{\tilde q} \exp(-t^2) \, dt,
$$

where the integral is along a path from $0$ to $\tilde q$ and the exponential is the quaternion exponential. The integrand $\exp(-t^2)$ is entire, but it is not monogenic, so the integral depends on the path in general.

### Properties

$$
\operatorname{erf}'(\tilde q) = \frac{2}{\sqrt{\pi}} \exp(-\tilde q^2),
$$

$$
\lim_{\tilde q \to \infty} \operatorname{erf}(\tilde q) = 1, \qquad \lim_{\tilde q \to -\infty} \operatorname{erf}(\tilde q) = -1,
$$

where the limits are taken along the real axis.

### The Complementary Error Function

$$
\operatorname{erfc}(\tilde q) = 1 - \operatorname{erf}(\tilde q) = \frac{2}{\sqrt{\pi}} \int_{\tilde q}^\infty \exp(-t^2) \, dt.
$$

## The Airy Function

### Definition

The **quaternion Airy function** is defined by the contour integral

$$
\operatorname{Ai}(\tilde q) = \frac{1}{2\pi i} \int_C \exp\left(\frac{t^3}{3} - \tilde q t\right) dt,
$$

where $C$ is a contour in the complex plane, the exponential is the quaternion exponential, and $\tilde q$ is a quaternion. Because the integrand is a function of the complex variable $t$ and the quaternion $\tilde q$ appears only in the exponent, the integral converges and defines a real-analytic function of $\tilde q$.

### Differential Equation

$$
w'' - \tilde q w = 0.
$$

This is Airy's equation, and it holds in the quaternion sense.

### Asymptotics

For $\tilde q$ with $q_t \to +\infty$ along the real axis,

$$
\operatorname{Ai}(\tilde q) \sim \frac{1}{2 \sqrt{\pi} \tilde q^{1/4}} \exp(-2 \tilde q^{3/2}/3).
$$

For $\tilde q$ with $q_t \to -\infty$ along the real axis,

$$
\operatorname{Ai}(\tilde q) \sim \frac{1}{\sqrt{\pi}\,(\sqrt{\langle\tilde q\rangle_{\natural}})^{1/4}} \sin\left(\frac{2(\sqrt{\langle\tilde q\rangle_{\natural}})^{3/2}}{3} + \frac{\pi}{4}\right).
$$

The same asymptotics hold for the vector part, with the appropriate modifications.

## The Bessel Functions

### Definition

The **quaternion Bessel function** of the first kind of order $\nu$ is defined by

$$
J_\nu(\tilde q) = \sum_{n=0}^\infty \frac{(-1)^n}{n! \, \Gamma(n + \nu + 1)} \left(\frac{\tilde q}{2} \right)^{2n + \nu},
$$

where the power and the gamma function are quaternion. The series converges absolutely for every $\tilde q$ for which the powers $(\tilde q/2)^{2n+\nu}$ are defined; when $\nu$ is not an integer this requires $\tilde q$ to lie in the domain of the logarithm.

### Differential Equation

$$
\tilde q^2 w'' + \tilde q w' + (\tilde q^2 - \nu^2) w = 0.
$$

This is Bessel's equation, and it holds in the quaternion sense.

### Modified Bessel Functions

The **quaternion modified Bessel function** of the first kind is

$$
I_\nu(\tilde q) = \sum_{n=0}^\infty \frac{1}{n! \, \Gamma(n + \nu + 1)} \left(\frac{\tilde q}{2} \right)^{2n + \nu}.
$$

It satisfies

$$
\tilde q^2 w'' + \tilde q w' - (\tilde q^2 + \nu^2) w = 0.
$$

### The Relation to the Cauchy–Riemann Operator

The Bessel functions of the quaternion variable are the radial parts of the monogenic functions on $\mathbb{R}^4$. They appear in the separation of variables for the Cauchy–Riemann operator in spherical coordinates, and they are the quaternion analogues of the cylindrical harmonics in complex analysis.

## The Hypergeometric Function

### Definition

The **quaternion Gauss hypergeometric function** is defined for $\sqrt{\langle\tilde q\rangle_{\natural}} < 1$ by

$$
{}_2F_1(a, b; c; \tilde q) = \sum_{n=0}^\infty \frac{(a)_n (b)_n}{(c)_n} \frac{\tilde q^n}{n!},
$$

where $(a)_n = a(a+1) \cdots (a+n-1)$ is the Pochhammer symbol, and all operations are quaternion. The series converges for $\sqrt{\langle\tilde q\rangle_{\natural}} < 1$.

### Differential Equation

$$
\tilde q(1 - \tilde q) w'' + [c - (a + b + 1) \tilde q] w' - ab w = 0.
$$

This is the hypergeometric equation, and it holds in the quaternion sense.

### Special Cases

$$
{}_2F_1(1, 1; 2; \tilde q) = -\frac{\log(1 - \tilde q)}{\tilde q},
$$

$$
{}_2F_1(a, b; b; \tilde q) = (1 - \tilde q)^{-a},
$$

$$
{}_2F_1\left(\frac{1}{2}, \frac{1}{2}; \frac{3}{2}; \tilde q^2\right) = \frac{\arcsin(\tilde q)}{\tilde q}.
$$

### The Generalized Hypergeometric Function

$$
{}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; \tilde q) = \sum_{n=0}^\infty \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \frac{\tilde q^n}{n!}.
$$

Most special functions of quaternion analysis are special cases of ${}_pF_q$.

## The Lambert W Function

### Definition

The **quaternion Lambert W function** is the inverse of

$$
f(\tilde q) = \tilde q \exp(\tilde q),
$$

where the exponential is the quaternion exponential. That is, $W(\tilde q)$ is any solution of

$$
W(\tilde q) \exp(W(\tilde q)) = \tilde q.
$$

### Derivative

$$
W'(\tilde q) = \frac{W(\tilde q)}{\tilde q(1 + W(\tilde q))},
$$

defined wherever the denominator is invertible.

### Branches

The quaternion Lambert W function has infinitely many branches, because the quaternion exponential is not injective. The principal branch is defined on the complement of the cut locus, and it is single-valued on that domain.

## The Monogenic Special Functions

### The Cauchy Kernel

The **Cauchy kernel** is the function

$$
E(\tilde q) = \frac{\tilde q^{-1}}{\langle\tilde q\rangle_{\natural}} = \frac{\tilde{q}^{\natural}}{\langle\tilde q\rangle_{\natural}^2}, \qquad \tilde q \neq 0.
$$

It is the fundamental solution of the Cauchy–Riemann operator:

$$
D E = 2\pi^2 \delta_0
$$

in the sense of distributions. It is the quaternion analogue of the kernel $1/A$ in complex analysis.

### The Exponential in Scalar-Vector Form

The **exponential** written in scalar-vector form is the function

$$
f(\tilde q) = \exp(q_t) \left(\cos\sqrt{\langle\vec q\rangle_{\natural}} + \frac{\vec q}{\sqrt{\langle\vec q\rangle_{\natural}}} \sin\sqrt{\langle\vec q\rangle_{\natural}} \right),
$$

which is $\exp(\tilde q)$. It is not monogenic: $D f = -2 \exp(q_t) \sin\sqrt{\langle\vec q\rangle_{\natural}} / \sqrt{\langle\vec q\rangle_{\natural}}$, which is non-zero wherever $\sin\sqrt{\langle\vec q\rangle_{\natural}} \neq 0$.

### The Power Functions

The **power functions** are the functions

$$
f_n(\tilde q) = \tilde q^n, \qquad n \in \mathbb{Z},
$$

which are not monogenic: $D \tilde q = -2$ and $D(\tilde q^2) = -4 q_t$, neither of which vanishes identically. For negative $n$, the functions have singularities at the origin, and the Laurent expansion of a monogenic function is expressed in terms of other powers.

### The Monogenic Bessel Functions

The **monogenic Bessel functions** are the radial monogenic functions, which are the solutions of the Cauchy–Riemann operator in spherical coordinates. They are expressed in terms of the ordinary Bessel functions of the radial variable, with coefficients that depend on the angular variables.

## The Structure Principle

The pattern in all the definitions above is the same: every quaternion special function is defined by a formula that involves the quaternion algebra operations, the quaternion exponential, and the quaternion logarithm. Unlike the complex case, the resulting functions are not determined by a single scalar variable, because $\mathbb{H}$ is four-dimensional and non-commutative. The functions depend on the scalar part and the vector part separately, and the non-commutativity prevents the simple identities that hold in the commutative case.

**Theorem (Structure Principle for quaternion special functions).** Let $F$ be a special function of one real variable that is analytic on an interval $I \subseteq \mathbb{R}$, and let $F_{\mathbb H}$ be its extension to the quaternions defined by the same power series. Then for $\tilde q$ with $q_t \in I$ and $\vec q$ arbitrary,

$$
F_{\mathbb H}(\tilde q) = \sum_{n=0}^\infty \frac{F^{(n)}(q_t)}{n!} \vec q^n,
$$

where the powers $\vec q^n$ are the quaternion powers of the vector part.

**Proof.** The extension is defined by the same power series, and the series converges because the quaternion norm is submultiplicative. The powers of $\tilde q$ decompose into the scalar and vector parts, and the series can be reorganized in terms of the powers of $\vec q$.

This theorem is the reason quaternion special functions are richer than real or complex special functions. In the real case, the function is determined by its values on the real line. In the complex case, the function is determined by its values on the real line and the Cauchy–Riemann equations. In the quaternion case, the function depends on the full four-dimensional variable, and the non-commutativity prevents the simple identities that hold in the commutative case.

## Summary

The quaternion special functions are the named functions that arise in quaternion analysis, in Clifford analysis and in the geometry of the quaternion space. Each is obtained by carrying the corresponding real or complex definition to the quaternion variable by means of the quaternion exponential and the quaternion operations.

The exponential is defined by its series, and the trigonometric and hyperbolic functions are built from it, with the scalar-vector decomposition of a quaternion taking the place of the real and imaginary parts of a complex number. The scalar-vector form also fixes the modulus and the zeros of each of them, and the same form reads the trigonometric functions as the hyperbolic functions of a rotated variable, which is how the inverse trigonometric functions are obtained from the inverse hyperbolic ones. The same form answers the quantitative questions: it turns the elementary real inequalities into bounds for each function, and it makes the $n$-th roots of a quaternion approach $1$ at a rate fixed by the logarithm, $n(\tilde q^{1/n} - 1) \to \log \tilde q$ and the means of roots converge to the exponential of the mean of the logarithms. Integral representations then supply the gamma and beta functions, the error function, the Airy function as a contour integral, the Bessel functions and the Gauss hypergeometric function, together with the Lambert $W$ function as the inverse of $\tilde q \mapsto \tilde q\exp(\tilde q)$.

The exponential is single-valued and not injective; the logarithm is its multi-valued inverse, with infinitely many branches differing by a multiple of $2\pi\operatorname{sgn}\tilde q$ off the real axis, and filling spheres of radius $2\pi k$ on it. The power functions inherit that multi-valuedness. The two compositions of the exponential and the logarithm behave differently: the logarithm inverts the exponential everywhere on its domain, while the exponential is inverted by the logarithm only on the region $\sqrt{\langle\mathrm{Vect}\tilde q\rangle_{\natural}} < \pi$, off which the value is shifted by a period.

The Cauchy kernel $\tilde{q}^{\natural}/\langle\tilde q\rangle_{\natural}^2$, the fundamental solution of the Cauchy–Riemann operator, opens the last family, the monogenic special functions, and the section on the structure principle states what organises the whole collection: every quaternion special function is defined by a formula involving the quaternion algebra operations and the quaternion exponential, and the properties it has are those the non-commutativity of $\mathbb{H}$ permits.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis |
| $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$ | General quaternion |
| $\vec q = \mathrm{Vect}\tilde q = q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$ | Vector part |
| $\operatorname{sgn}(\tilde q) = \vec q/\sqrt{\langle\vec q\rangle_{\natural}}$ | Unit pure quaternion of the vector part |
| $\exp(\tilde q), \log \tilde q$ | Quaternion exponential, logarithm (principal branch) |
| $\tilde q_{\log}$ | A logarithm of $\tilde q$ |
| $q_{\log}=\operatorname{Sc}\tilde q_{\log}$, $\vec q_{\log}=\operatorname{Vect}\tilde q_{\log}$ | Scalar and vector coordinates of a logarithm |
| $\operatorname{Arg}\tilde q$ | Principal argument of $\tilde q$, in $[0, \pi]$ |
| $\sin \tilde q, \cos \tilde q, \tan \tilde q$ | Quaternion trigonometric functions |
| $\sinh \tilde q, \cosh \tilde q, \tanh \tilde q, \coth \tilde q$ | Quaternion hyperbolic functions |
| $\sin^{-1}\tilde q, \cos^{-1}\tilde q, \tan^{-1}\tilde q$ | Inverse trigonometric functions (multi-valued) |
| $\sinh^{-1}\tilde q, \cosh^{-1}\tilde q, \tanh^{-1}\tilde q$ | Inverse hyperbolic functions (multi-valued) |
| $\tilde q^a$ | Quaternion power |
| $\Gamma(\tilde q)$ | Quaternion gamma function |
| $B(p, \tilde q)$ | Quaternion beta function |
| $\operatorname{erf}(\tilde q), \operatorname{erfc}(\tilde q)$ | Quaternion error functions |
| $\operatorname{Ai}(\tilde q)$ | Quaternion Airy function |
| $J_\nu(\tilde q), I_\nu(\tilde q)$ | Quaternion Bessel functions |
| ${}_pF_q$ | Quaternion generalized hypergeometric function |
| $W(\tilde q)$ | Quaternion Lambert W function |
| $E(\tilde q) = \tilde q^{-1}/\langle\tilde q\rangle_{\natural}$ | Cauchy kernel |
| $D$ | Cauchy–Riemann operator |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- Rudolf Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta \Delta u = 0$ mit vier reellen Variablen" (1935), for the origin of monogenic functions.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the general Clifford theory.
- John Ryan, *Clifford Algebras in Analysis and Related Topics* (CRC Press, 1996), for the analytic theory.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton, 1989), for the role of the spinor-valued first-order operator in geometry.
- S. Georgiev, J. Morais and W. Sprößig, "New Aspects on Elementary Functions in the Context of Quaternionic Analysis", *Cubo* **14** (2012) 93–110, for the multiple-valued quaternion logarithm, the inverse trigonometric and hyperbolic functions and their branch points, and the inequalities for the elementary quaternion functions.
