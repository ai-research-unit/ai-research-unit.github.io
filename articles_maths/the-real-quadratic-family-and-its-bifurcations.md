# __The Real Quadratic Family and Its Bifurcations__

## Introduction

The **real quadratic family** is the one-parameter family of maps of the line

$$
f_c : \mathbb{R} \to \mathbb{R}, \qquad f_c(x) = x^2 + c, \qquad c \in \mathbb{R}.
$$

This article studies it as a family of dynamical systems of the line: the normalisation that puts every real quadratic polynomial in this form, the fixed points and the interval of parameters for which the fixed point is attracting, the period-doubling cascade that begins at the parameter $c=-3/4$ and accumulates at the Feigenbaum point, and the **real Mandelbrot set**, the set of parameters whose critical orbit is bounded, which is the interval $[-2,1/4]$. The general theory of the bifurcations — the normal forms, the period-doubling operator, the renormalisation and the universality — is the subject of *Bifurcation Theory* of Part III, and the dynamical notions of chaos, the topological entropy and the limit set are those of *Topological Dynamics*, *Symbolic Dynamics* and *Ergodic Theory*; the complex Mandelbrot set is the subject of *The Mandelbrot Set and the Quadratic Family*, whose intersection with the real axis the present article computes. All of these are cited and none is restated.

The two self-similar articles of this subcategory, *Self-Similar Subsets of the Real Line* and *Iterated Function Systems on the Real Line*, are the contrast to this one: they concern maps that contract and produce a self-similar attractor, while the quadratic family is a family that expands on its Julia set and produces a bifurcation diagram. The two are not continuations of one another, and they are placed in this order to bring out the difference. The real quadratic family is also the first of the quadratic families of Part VI; the complex, split-complex, dual-number, quaternion, split-quaternion, biquaternion, split-biquaternion and octonion families are the subject of the corresponding articles of this Part, and the comparison is drawn at the end.

Throughout, $c$ is a real parameter, $x$ a real variable, $f_c^n$ the $n$-th iterate, and $\lambda = (f_c^p)'(x)$ the multiplier of a $p$-periodic cycle, with the cycle **attracting** when $\lvert\lambda\rvert<1$, **superattracting** when $\lambda=0$, **repelling** when $\lvert\lambda\rvert>1$ and **indifferent** when $\lvert\lambda\rvert=1$; the critical point is $x=0$, whose orbit $0\mapsto c\mapsto c^2+c\mapsto\cdots$ is the **critical orbit** of $c$.

## The Family and Its Normalisation

**Definition.** A **real quadratic polynomial** is a map $p(x)=ax^2+bx+d$ with $a,b,d\in\mathbb{R}$ and $a\neq0$. A map $h(x)=\alpha x+\beta$ with $\alpha\neq0$ is an **affine conjugacy**, and two maps $p,q$ are conjugate when $q=h\circ p\circ h^{-1}$ for some such $h$.

**Theorem (the normal form).** Every real quadratic polynomial is affinely conjugate to exactly one map $f_c(x)=x^2+c$, with

$$
c = ad + \frac{b}{2} - \frac{b^2}{4},
$$

and the conjugating map is $h(x)=ax+b/2$.

*Proof.* Compute $h\circ p\circ h^{-1}(y)$ with $h^{-1}(y)=(y-b/2)/a$. Writing $p(x)=ax^2+bx+d$, one has $p(h^{-1}(y))=(y-b/2)^2/a+b(y-b/2)/a+d$, so $h(p(h^{-1}(y)))=(y-b/2)^2+b(y-b/2)+ad+b/2=y^2-b^2/4+ad+b/2$. This is $y^2+c$ with the stated $c$, and $a\neq0$ makes $h$ a conjugacy. For uniqueness, an affine conjugacy of $x^2+c$ to a quadratic polynomial is again a quadratic polynomial with the same leading coefficient up to the square of the scaling, so the normalised leading coefficient $1$ and the vanishing linear term are preserved. $\square$

**Remark (why $x^2+c$ and not $x^2+x+c$).** The normal form places the critical point at the origin and removes the linear term, which is the same normalisation as in the complex quadratic family of *The Mandelbrot Set and the Quadratic Family*; the real and the complex families are therefore the same algebraic family, read on different fields. The parameter $c$ is a real number, and the critical point is $0$ for every $c$.

## Fixed Points, Stability and the First Bifurcations

**Theorem (the fixed points).** The fixed points of $f_c$ are

$$
x_\pm = \frac{1\pm\sqrt{1-4c}}{2},
$$

real precisely for $c\leq1/4$; their multipliers are $\lambda_\pm = 2x_\pm = 1\pm\sqrt{1-4c}$. Consequently:

**(a)** for $c<1/4$ the point $x_+$ is repelling, with $\lambda_+>1$;

**(b)** the point $x_-$ is attracting exactly for $-3/4<c<1/4$, superattracting exactly at $c=0$, with multiplier $\lambda_-=1$ at $c=1/4$ and $\lambda_-=-1$ at $c=-3/4$;

**(c)** at $c=1/4$ the two fixed points collide in a **tangent (saddle-node) bifurcation** at $x=1/2$ with multiplier $1$;

**(d)** at $c=-3/4$ the attracting fixed point loses stability in a **period-doubling bifurcation**, and a period-two cycle is born.

*Proof.* Solving $x^2+c=x$ gives $x_\pm$ with discriminant $1-4c$, and $(f_c)'(x)=2x$, so $\lambda_\pm=2x_\pm=1\pm\sqrt{1-4c}$. The inequality $\lvert\lambda_-\rvert<1$ is $\lvert1-\sqrt{1-4c}\rvert<2$, which is $-3/4<c<1/4$; $\lambda_-=0$ at $c=0$; the boundary values are $\lambda_-=1$ at $c=1/4$ and $\lambda_-=-1$ at $c=-3/4$. At $c=1/4$ the two roots coincide, and at $c=-3/4$ the multiplier crossing $-1$ is the period-doubling condition of *Bifurcation Theory*. $\square$

**Theorem (the invariant interval and the escape).** Put $x_+ = (1+\sqrt{1-4c})/2$ for $c\leq1/4$ and $I_c = [-x_+,x_+]$. For $-2\leq c\leq1/4$ the interval $I_c$ is invariant, $f_c(I_c)\subseteq I_c$; for $c>1/4$ every orbit tends to $+\infty$; and for $c<-2$ the critical orbit escapes to $+\infty$. Consequently the set of parameters with bounded critical orbit is contained in $[-2,1/4]$.

*Proof.* For $x\in I_c$ one has $0\leq x^2\leq x_+^2$, so $f_c(I_c)=[c,\,x_+^2+c]=[c,x_+]$, using $x_+^2+c=x_+$; and $c\geq-x_+$ exactly when $c\geq-2$ (the boundary case $c=-2$ gives $x_+=2$ and $c=-x_+$). Hence $[c,x_+]\subseteq[-x_+,x_+]=I_c$ for $c\geq-2$. For $c>1/4$, $x^2+c-x = x^2-x+c>0$ for all $x$, since the discriminant $1-4c$ is negative, so $f_c(x)>x$ everywhere and every orbit increases without bound. For $c<-2$, $\lvert c\rvert>2$ and $\lvert c^2+c\rvert\geq\lvert c\rvert^2-\lvert c\rvert=\lvert c\rvert(\lvert c\rvert-1)>\lvert c\rvert$, and the same inequality propagates, so the critical orbit escapes monotonically. $\square$

## Period Doubling and the Feigenbaum Constants

**Theorem (the period-two cycle).** For $c\leq-3/4$ the map $f_c$ has a period-two cycle, the roots of

$$
x^2+x+c+1=0, \qquad x_{1,2}=\frac{-1\pm\sqrt{-3-4c}}{2},
$$

and the factorisation $f_c^2(x)-x = (x^2-x+c)(x^2+x+c+1)$. The multiplier of the cycle is

$$
\lambda_2(c) = 4(1+c),
$$

independent of the point of the cycle; it is $1$ at $c=-3/4$ (the birth), $0$ at $c=-1$ (the superattracting case), and $-1$ at $c=-5/4$ (the period-doubling to period four). The cycle is attracting exactly for $-5/4<c<-3/4$.

*Proof.* The factorisation is the division of $f_c^2(x)-x=x^4+2cx^2-x+c^2+c$ by $f_c(x)-x=x^2-x+c$; the quotient is $x^2+x+c+1$, whose roots form the 2-cycle. The multiplier is the product of the derivatives at the two points, $(2x_1)(2x_2)=4x_1x_2=4\bigl((x_1+x_2)^2-(x_1^2+x_2^2)\bigr)/2$; from $x_1+x_2=-1$ and $x_1x_2=c+1$ it is $4(c+1)$. The sign of $4(1+c)-1$ at $c=-3/4$ and of $4(1+c)+1$ at $c=-5/4$ gives the birth and the doubling. $\square$

**Definition.** The parameter $c$ is **superstable** of period $p=2^n$ when the critical point is periodic of period exactly $p$, that is $f_c^p(0)=0$ and $f_c^{p/2}(0)\neq0$; write $c_n$ for the largest such parameter. The first values are $c_0=0$ (period one), $c_1=-1$ (period two), and the computation of the roots of $f_c^{2^n}(0)=0$ gives

| $n$ | period $2^n$ | $c_n$ |
|---|---|---|
| $1$ | $2$ | $-1$ |
| $2$ | $4$ | $-1.3107026413$ |
| $3$ | $8$ | $-1.3815474844$ |
| $4$ | $16$ | $-1.3969453597$ |
| $5$ | $32$ | $-1.4002530812$ |
| $6$ | $64$ | $-1.4009619629$ |
| $7$ | $128$ | $-1.4011138049$ |

**Theorem (the cascade and the Feigenbaum constants).** The parameters $c_n$ decrease to a limit $c_\infty=-1.4011551890\ldots$, the **Feigenbaum point**, and the ratios of successive gaps satisfy

$$
\delta_n = \frac{c_{n-1}-c_n}{c_n-c_{n+1}} \;\longrightarrow\; \delta = 4.6692016091\ldots,
$$

the **Feigenbaum constant**, with the computed values $\delta_2=4.3857$, $\delta_3=4.6009$, $\delta_4=4.6551$, $\delta_5=4.6661$, $\delta_6=4.6685$. The space rescaling along the cascade has the limit

$$
\alpha = 2.5029078750\ldots,
$$

the second Feigenbaum constant. Both constants are universal: they are the same for every smooth unimodal family with a quadratic critical point. The constants are those of Feigenbaum; the renormalisation argument, in which the second iterate of $f_c$ on a neighbourhood of the critical point, rescaled by $\alpha$, is again a quadratic map, and the proof of universality are the subject of *Bifurcation Theory* of Part III.

**Proof sketch.** The period-doubling theorem of *Bifurcation Theory* applied at each crossing $\lambda=-1$ produces the doubling from period $2^n$ to $2^{n+1}$ at the parameter $c$ solving $f_c^{2^n}(0)=0$ with the critical point periodic; the superstable parameters therefore increase in number and the intervals between them shrink. The renormalisation operator $R$ acting on a unimodal map with a quadratic maximum by restricting the second iterate to the interval between the critical point and its image, rescaling affinely to the unit interval, is a contraction on the space of such maps in the appropriate norm, and its unique fixed point has derivative $-1/\delta$ at the critical value and rescaling $\alpha$; the two constants are the display of the fixed point, and they are independent of the family by the contraction. The full proof is Part III's. $\square$

**Remark (superstable, and not the bifurcation points).** The sequence $c_n$ is the sequence of superstable parameters, where the multiplier of the period-$2^n$ cycle is $0$; the sequence of bifurcation parameters, where the multiplier crosses $-1$, also has ratios tending to the same $\delta$, so the two sequences are interchangeable for the numerical value. The superstable sequence is used here because the equation $f_c^{2^n}(0)=0$ is the easiest to compute and to state. The value $\alpha$ is quoted from the standard reference and is not recomputed here; only the $\delta_n$ are recomputed, in double precision, from the roots of $f_c^{2^n}(0)=0$.

## The Real Mandelbrot Set

**Definition.** The **real Mandelbrot set** is the set of parameters $c\in\mathbb{R}$ for which the critical orbit of $f_c$ is bounded; it is the intersection of the real axis with the Mandelbrot set $M$ of *The Mandelbrot Set and the Quadratic Family*.

**Theorem.** The real Mandelbrot set is exactly the interval $[-2,1/4]$.

*Proof.* For $c\in[-2,1/4]$ the interval $I_c=[-x_+,x_+]$ is invariant and contains $0$, so the critical orbit stays in the compact interval $I_c$ and is bounded. For $c>1/4$ every orbit escapes by the previous section, and for $c<-2$ the critical orbit escapes. Hence the real Mandelbrot set is $[-2,1/4]$. $\square$

**Remark (the components and the windows).** The interval $[-2,1/4]$ decomposes into the **hyperbolic windows**, the maximal intervals of $c$ on which $f_c$ has an attracting periodic cycle of a fixed period: the period-one window $[-3/4,1/4]$, the period-two window $[-5/4,-3/4]$, the period-four window $[-1.3681\ldots,-5/4]$, and the further windows accumulating at the Feigenbaum point $c_\infty$. At a window's endpoints the cycle is born by a tangent bifurcation or dies by a period doubling, and the window's interior contains exactly one superstable parameter. The complement in $[-2,1/4]$ of the union of the windows is a compact set of Lebesgue measure zero, a Cantor-like set of parameters at which no attracting cycle exists, of which $c=-2$ is the endpoint. The **density of hyperbolicity** on the real axis — the statement that the union of the windows is dense in $[-2,1/4]$, equivalently that every parameter is a limit of hyperbolic ones — is the theorem of Graczyk and Świątek and of Lyubich; the proof is Part IV's, and the corresponding statement for the complex parameter is open. The comparison of the real interval with the full Mandelbrot set is drawn next.

## Comparison with the Other Number Systems

**The complex case.** The real quadratic family is the restriction to the real axis of the complex family $z\mapsto z^2+c$, and the real Mandelbrot set is $M\cap\mathbb{R}=[-2,1/4]$. Over the complex numbers the connectedness locus is the Mandelbrot set, a compact connected subset of the plane of full Hausdorff dimension $2$ and of rich boundary structure; the real axis meets it in the interval computed above, and the hyperbolic components of the complex set meet the real axis in the windows. The complex theory, the hyperbolic components, the multiplier map and the dimension of the boundary are the subject of *The Mandelbrot Set and the Quadratic Family*, *The Julia Sets of a Complex Polynomial* and *The Hausdorff Dimension of the Julia Sets*.

**The quaternion and split-quaternion cases.** For the quaternionic family $q\mapsto q^2+c$ the critical orbit of $0$ lies in the associative subalgebra generated by $c$, which is a copy of $\mathbb{C}$ when $c$ has a nonzero vector part; the connectedness locus is therefore the family of copies of the complex Mandelbrot set rotated about the real axis, a four-dimensional solid of revolution, the **quaternion Mandelbrot set** of *The Quaternion Mandelbrot Set*. The split-quaternion family has a different normal form and a different parameter space, because the norm is indefinite, and its connectedness locus is the subject of *The Split-Quaternion Mandelbrot Set*. The real interval is the common slice of all of them.

**The octonion case.** The same reduction applies at the top of the ladder: the critical orbit of the octonion family lies in the associative subalgebra generated by the parameter, so the octonion connectedness locus is the body of revolution of the complex Mandelbrot set about the real axis, an $S^6$-family of copies of it, and it is the subject of *The Octonion Mandelbrot Set*. The genuinely non-associative effects are not in the quadratic map of a single parameter but in the maps defined by words with three independent directions, which are the subject of *The Octonion Quadratic Map and the Non-Associative Julia Sets* and *The Associator and the Closure of the Octonion Orbits*.

**The biquaternion and split-biquaternion cases.** The complexified families $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$ contain zero divisors, and their quadratic families have singular loci and a connectedness locus that is a slice of the complex one with the additional complex directions; they are the subject of *The Biquaternion Quadratic Map and Its Julia Sets* and *The Split-Biquaternion Quadratic Family*. The real interval is again the common real slice.

**Remark (the pattern).** For every one of the normed division families the connectedness locus of the critical orbit is an $S^{d-2}$-family of copies of the complex Mandelbrot set, for $d=4,8$ the dimension of the system, while in dimension $d=2$ it is the complex set itself; the reason is the same in each case, namely that the critical orbit remains in the two-dimensional associative subalgebra generated by the parameter. The higher-dimensional dynamics is in the Julia sets and not in the connectedness locus. This is the pattern that the octonion subcategory makes precise, and it is the reason the real quadratic family is placed first.

## The Topological Dynamics of the Family

**Theorem (the Chebyshev conjugacy at $c=-2$).** With the change of variable $x=2\cos\theta$,

$$
f_{-2}(2\cos\theta) = 4\cos^2\theta-2 = 2\cos 2\theta,
$$

so $f_{-2}$ on $[-2,2]$ is conjugate to the doubling map $\theta\mapsto2\theta$ on the circle; the conjugacy is two-to-one, and the dynamics of $f_{-2}$ on $[-2,2]$ has topological entropy $\log2$. The point $x=-1$ is fixed with multiplier $-2$, the point $x=2$ is fixed with multiplier $4$, and every point of $[-2,2]$ has bounded orbit.

*Proof.* The addition formula $2\cos2\theta=4\cos^2\theta-2$ is the identity; composing with $x=2\cos\theta$ gives the conjugacy, and the doubling map's entropy is $\log2$ by the count of its periodic points, which is Part III's. The fixed points and multipliers are $x_\pm$ at $c=-2$, namely $-1$ and $2$, but the critical orbit lands on the repelling fixed point $2$: $0\mapsto-2\mapsto2\mapsto2$, so $c=-2$ is a post-critically finite parameter and the Julia set is the whole interval $[-2,2]$. $\square$

**Remark (the several regimes).** For $c>1/4$ every real orbit escapes to $+\infty$; for $c<-2$ the real points with bounded orbit form a totally disconnected Cantor set, and the map is hyperbolic on the complement of the escaping set; for $-2\leq c\leq1/4$ the set of real points with bounded orbit is the interval $I_c$, and the dynamics on it ranges from the attracting-cycle regime in the hyperbolic windows to the chaotic regime at $c=-2$. The limiting cases $c=1/4$ (a parabolic fixed point with multiplier $1$) and $c=-3/4$ (a period-doubling) are the two bifurcation types of the family, and the classification of the possible cycles, their multipliers and their basins is the theory of *Bifurcation Theory* and *Topological Dynamics*. The **bifurcation diagram** — the plot of the attracting cycle against $c$ — is the real analogue of the Mandelbrot set, and the two are different pictures of the same family: the diagram is the collection of the attracting orbits, the set is the collection of the bounded critical orbits.

## Summary

Every real quadratic polynomial is affinely conjugate to exactly one map $f_c(x)=x^2+c$, and the family is the real restriction of the complex quadratic family. The fixed points are $x_\pm=(1\pm\sqrt{1-4c})/2$ with multipliers $1\pm\sqrt{1-4c}$; the fixed point $x_-$ is attracting exactly for $-3/4<c<1/4$, superattracting at $c=0$, collides with $x_+$ in a tangent bifurcation at $c=1/4$, and loses stability in a period-doubling at $c=-3/4$. The period-two cycle is born at $c=-3/4$, has multiplier $4(1+c)$, is superattracting at $c=-1$ and doubles at $c=-5/4$. The doubling cascade has superstable parameters $c_1=-1$, $c_2=-1.3107026413$, $c_3=-1.3815474844$, $c_4=-1.3969453597,\ldots$, accumulating at the Feigenbaum point $c_\infty=-1.4011551890\ldots$, with the ratios tending to the Feigenbaum constant $\delta=4.6692016\ldots$ and the space rescaling $\alpha=2.5029079\ldots$; both constants are universal and are quoted from the standard theory of *Bifurcation Theory*.

The real Mandelbrot set — the parameters with bounded critical orbit — is the interval $[-2,1/4]$: the interval $I_c=[-x_+,x_+]$ is invariant for $-2\leq c\leq1/4$ and contains the critical point, while every orbit escapes for $c>1/4$ and the critical orbit escapes for $c<-2$. The interval decomposes into hyperbolic windows accumulating at the Feigenbaum point, and the density of hyperbolicity on the real axis is the theorem of Graczyk–Świątek and Lyubich. Over the complex, quaternion, split-quaternion, biquaternion, split-biquaternion and octonion families the connectedness locus is a higher-dimensional family of copies of the complex Mandelbrot set, because the critical orbit stays in the associative subalgebra generated by the parameter; the genuinely higher-dimensional dynamics is in the Julia sets, and it is the subject of the corresponding articles of Part VI.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $f_c(x)=x^2+c$ | The real quadratic family; critical point $0$ |
| $x_\pm=\frac{1\pm\sqrt{1-4c}}{2}$ | The fixed points; multipliers $1\pm\sqrt{1-4c}$ |
| $-3/4<c<1/4$ | The interval of attraction of $x_-$ |
| $c=1/4$, $c=-3/4$ | Tangent bifurcation; period-doubling |
| $4(1+c)$ | The multiplier of the period-two cycle |
| $c_n$, $c_\infty$ | Superstable parameters of period $2^n$; the Feigenbaum point |
| $\delta=4.6692016\ldots$, $\alpha=2.5029079\ldots$ | The Feigenbaum constants (quoted) |
| $[-2,1/4]$ | The real Mandelbrot set $M\cap\mathbb{R}$ |
| $I_c=[-x_+,x_+]$ | The invariant interval for $-2\leq c\leq1/4$ |
| $x=2\cos\theta$ | The conjugacy of $f_{-2}$ to the doubling map |

## Further Reading

- Mitchell J. Feigenbaum, "Quantitative universality for a class of nonlinear transformations", *Journal of Statistical Physics* **19** (1978), 25–52, for the constants $\delta$ and $\alpha$ and the universality.
- Pierre Collet and Jean-Pierre Eckmann, *Iterated Maps on the Interval as Dynamical Systems* (Birkhäuser, 1980), for the period-doubling cascade and the renormalisation.
- Jacek Graczyk and Grzegorz Świątek, "Generic hyperbolicity in the logistic family", *Annals of Mathematics* **146** (1997), 1–52, for the density of hyperbolicity on the real axis.
- Mikhail Lyubich, "Dynamics of quadratic polynomials, I–II", *Acta Mathematica* **178** (1997), 185–297, for the real quadratic family and its rigidity.
- John Milnor, *Dynamics in One Complex Variable*, 3rd edition (Princeton University Press, 2006), for the quadratic family over $\mathbb{C}$ and the Mandelbrot set.
- Benoit B. Mandelbrot, *The Fractal Geometry of Nature* (Freeman, 1982), for the bifurcation diagram and the parameter space.
- Robert L. Devaney, *An Introduction to Chaotic Dynamical Systems*, 2nd edition (Addison-Wesley, 1989), for the Chebyshev conjugacy and the chaotic parameters.
