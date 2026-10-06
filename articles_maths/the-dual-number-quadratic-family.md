# __The Dual-Number Quadratic Family__

## Introduction

The dual numbers $\mathbb{D}' = \mathbb{R}[\varepsilon]$, $\varepsilon^2 = 0$, carry the quadratic family

$$
f_c(z) = z^2 + c, \qquad z, c \in \mathbb{D}' ,
$$

and the nilpotence of $\varepsilon$ makes the dynamics **triangular**: writing $z = x+\varepsilon y$ and $c = \gamma+\varepsilon\delta$, the map is

$$
f_c(x+\varepsilon y) = (x^2+\gamma) + \varepsilon(2xy+\delta) .
$$

The real part $x$ evolves by the real quadratic map $x \mapsto x^2+\gamma$, independently of the infinitesimal coordinate, and the infinitesimal coordinate $y$ evolves **affinely**, with coefficient $2x$ equal to the derivative of the real map at the point. This article fixes the family and its triangular form, identifies the critical locus — the ideal of the nilpotents, which collapses to the single critical value $c$ — describes the escape and the connectedness locus as read on the real part, and compares the family with the real, the complex and the split-complex cases. The infinitesimal coordinate itself, which is the derivative cocycle along the real orbit, is the subject of *The Infinitesimal Dynamics of the Dual Numbers*.

The article is the $\mathbb{D}'$ instance of the quadratic family. The algebra, the norm and the invertibility are those of *Dual-Numbers Algebra* and *Dual-Numbers Norm and Invertibility*; the shears and the parabolic rotations are those of *Shears and Parabolic Rotations*; the real quadratic family is that of *The Mandelbrot Set and the Quadratic Family*, and the complex and split-complex comparisons are *The Mandelbrot Set and the Quadratic Family* and *The Split-Complex Quadratic Family*. No physics is invoked, and every numerical value displayed was recomputed. The article is deliberately short: the dual family has no fractal content of its own beyond the real one, and the value of the article is the exactness of the collapse.

## The Family and the Triangular Form

### The Coordinates

**Definition.** The **dual numbers** are $\mathbb{D}' = \mathbb{R}[\varepsilon]$ with $\varepsilon^2 = 0$; a general element is $z = x+\varepsilon y$ with $x, y \in \mathbb{R}$, its **real part** is $x$, its **infinitesimal part** is $y$, and $x+\varepsilon y$ is a unit exactly when $x \neq 0$. The **norm** is $N(z) = z\bar z = x^2$, where $\bar z = x-\varepsilon y$.

**Theorem (the triangular form).** With $z = x+\varepsilon y$ and $c = \gamma+\varepsilon\delta$,

$$
f_c(x+\varepsilon y) = (x^2+\gamma) + \varepsilon(2xy+\delta) .
$$

Hence $f_c$ is a **skew product**: the projection $\pi(x+\varepsilon y) = x$ to the real part satisfies $\pi \circ f_c = g_\gamma \circ \pi$ with $g_\gamma(x) = x^2+\gamma$ the real quadratic map, and on each fibre the map is the affine map $y \mapsto 2x\,y+\delta$, whose linear coefficient is the derivative $g_\gamma'(x) = 2x$.

**Proof.** $(x+\varepsilon y)^2 = x^2+2\varepsilon xy+\varepsilon^2y^2 = x^2+2\varepsilon xy$ because $\varepsilon^2 = 0$; adding $c = \gamma+\varepsilon\delta$ gives the display. The projection statement is immediate, and $g_\gamma'(x) = 2x$ is the coefficient of $y$.

**Remark (the comparison with the other number systems).** In $\mathbb{C}$ the map $z^2+c$ is a single holomorphic map and cannot be split; in $\mathbb{D}$ the map splits into two coupled real quadratic maps and neither factor is subordinate to the other; in $\mathbb{D}'$ the map splits into the real quadratic map and a **linear** fibre map, so the second factor is derivative data determined by the first. This is the triangularity: there is an invariant foliation by the vertical lines $\{x = \mathrm{const}\}$, and the real part is a genuine quotient dynamics.

### The Critical Locus and the Collapse

**Theorem (the critical locus is the ideal).** The derivative of $f_c$ is the multiplication by $2z$, and

$$
2z = 2x + 2\varepsilon y \ \text{ is a unit} \iff x \neq 0 .
$$

So the **critical locus** of $f_c$ is the set $\{x = 0\} = \mathbb{R}\varepsilon$, the ideal of the nilpotents, a whole line and not a point.

**Proof.** The units of $\mathbb{D}'$ are exactly the elements with nonzero real part, by the invertibility criterion $z\bar z = x^2 \neq 0$ of *Dual-Numbers Norm and Invertibility*.

**Theorem (the collapse of the critical set).** Every critical point has the same image:

$$
f_c(\varepsilon y) = c \qquad \text{for every } y \in \mathbb{R} .
$$

Consequently the critical set collapses to the single critical value $c$, the critical orbit is the orbit of $c$, and the family has no "critical point" in the sense of *The Julia Sets of a Complex Polynomial* other than the value $c$ itself.

**Proof.** $(\varepsilon y)^2 = \varepsilon^2 y^2 = 0$, so $f_c(\varepsilon y) = 0 + c = c$; the statement follows since the real part of $\varepsilon y$ is $0$.

**Remark.** The collapse is the reason the dual theory is so thin: in the complex case the critical point is the single point $0$ and the critical orbit is a sequence of interest; in the dual case the critical locus is a line, all of its points have the same image $c$, and the "postcritical" object is a single sequence, the orbit of $c$. The critical point $0$ used in *The Split-Complex Quadratic Family* is also a critical point here — it is the origin of the critical line — and its orbit is the orbit of $\varepsilon\cdot0$, that is of $0$, which after one step is the orbit of $c$.

## The Escape and the Connectedness Locus

**Definition.** A point $z = x+\varepsilon y$ **escapes** under $f_c$ if its orbit is unbounded in the Euclidean metric of the plane; the **connectedness locus** is

$$
M_{\mathbb{D}'} = \{c \in \mathbb{D}' : \text{the orbit of the critical point } 0 \text{ is bounded}\} .
$$

**Theorem (the escape is read on the real part).** The norm is $N(z) = x^2$, so the norm-escape of $z$ is exactly the escape of its real part; the real part of the orbit is the orbit of $x$ under $g_\gamma$, and the orbit is bounded in the Euclidean metric if and only if both the real orbit $(g_\gamma^n(x))$ and the sequence

$$
y_n = \delta\,P_n(\gamma), \qquad P_0 = 0, \quad P_{n+1} = 2g_\gamma^n(0)\,P_n + 1 ,
$$

are bounded; for the critical orbit, $x_0 = 0$ and the real orbit is $(g_\gamma^n(0))$.

**Proof.** $N(z) = (x+\varepsilon y)(x-\varepsilon y) = x^2$, and the real part recursion is $x_{n+1} = x_n^2+\gamma$. For the infinitesimal part, $y_{n+1} = 2x_n y_n+\delta$ with $x_n = g_\gamma^n(x_0)$; for $y_0 = 0$ the solution is the displayed affine combination, since $y_n$ is linear in $\delta$ with the homogeneous part built from the derivatives $2x_n$.

**Theorem (the projection of the connectedness locus).** The projection $\pi(M_{\mathbb{D}'}) \subseteq \mathbb{R}$ is the real Mandelbrot interval $[-2,\tfrac14]$, and the fibre over $\gamma \in [-2,\tfrac14]$ is

$$
\{\delta \in \mathbb{R} : (\gamma,\delta) \in M_{\mathbb{D}'}\} = \begin{cases} \mathbb{R}, & \sup_n |P_n(\gamma)| < \infty, \\ \{0\}, & \sup_n |P_n(\gamma)| = \infty, \end{cases}
$$

so the connectedness locus is the real interval in $\gamma$ with the fibre either the whole line or the single point $0$.

**Proof.** The real part of the orbit of $0$ is $(g_\gamma^n(0))$, which is bounded exactly for $\gamma \in [-2,\tfrac14]$, the real slice of the Mandelbrot set. For fixed $\gamma$ the sequence $y_n = \delta P_n(\gamma)$ is bounded for every $\delta$ if $P_n$ is bounded, and for no $\delta \neq 0$ if $|P_n|$ is unbounded; this gives the two cases.

**Example (a hyperbolic parameter).** For $\gamma = 0$ the real orbit of $0$ is constantly $0$, so $P_n = 1$ for $n \geq 1$ and the fibre is $\mathbb{R}$; the orbit of the critical point $0$ under $c = \varepsilon\delta$ has $x_n = 0$ and $y_n = \delta$ for $n \geq 1$, bounded. For $\gamma = -1$ the real orbit is the superattracting cycle $0,-1,0,-1,\ldots$, so $2x_n \in \{0,-2\}$ and $P_n \in \{0,1,-1\}$ is bounded; the fibre is $\mathbb{R}$, and the numerical orbit confirms $y \in \{1,-1\}$.

**Example (the Chebyshev parameter).** For $\gamma = -2$ the real orbit is $0,-2,2,2,\ldots$, so $2x_n = 4$ for $n \geq 2$ and $P_n = -\tfrac23 4^{n-1} - \tfrac13$ grows like $-\tfrac23 4^{n-1}$; the numerical values $1, -3, -11, -43, -171, -683, \ldots$ are recomputed, and the fibre is $\{0\}$. So the parameter $c = -2+\varepsilon\delta$ with $\delta \neq 0$ has a bounded real part and an unbounded infinitesimal part: the point is outside the connectedness locus although its projection is in the real Mandelbrot interval.

**Example (the parabolic parameter).** For $\gamma = \tfrac14$ the real orbit converges to the parabolic fixed point $\tfrac12$ with multiplier $1$, so $2x_n \to 1$ and $P_n$ grows linearly; the numerical values $1, 1.5, 1.9375, 2.347\ldots, 5.321\ldots$ at the twelfth step are recomputed, and the fibre is $\{0\}$.

**Remark (the honest summary).** The connectedness locus is not a product: it is the real Mandelbrot interval in the real direction and, in the infinitesimal direction, either the whole line or the single origin. The reason is that the infinitesimal direction is not an independent dynamical variable but the linearisation of the real one; the base dynamics decides everything, and the fibre only records whether the derivative cocycle is bounded. The fractal content is entirely that of the real quadratic family.

## Summary

The dual-number quadratic family $f_c(z) = z^2+c$ is triangular: with $z = x+\varepsilon y$ and $c = \gamma+\varepsilon\delta$ it is $f_c(z) = (x^2+\gamma)+\varepsilon(2xy+\delta)$, so the real part is the real quadratic map $x \mapsto x^2+\gamma$ and the infinitesimal part is the affine map $y \mapsto 2xy+\delta$, whose coefficient is the derivative of the real map. The derivative of $f_c$ is the multiplication by $2z$, a unit exactly off the ideal $\mathbb{R}\varepsilon$; the critical locus is therefore the whole ideal of the nilpotents, and every critical point has the image $c$, so the critical value is the single parameter $c$. The norm is $N(z) = x^2$, so the escape is the escape of the real part; the connectedness locus projects onto the real Mandelbrot interval $[-2,\tfrac14]$, and its fibre over $\gamma$ is $\mathbb{R}$ when the derivative cocycle is summable and the single point $0$ when it is not. The hyperbolic parameters give the whole line; the Chebyshev parameter $-2$ and the parabolic parameter $\tfrac14$ give the single point, and at those parameters a nonzero $\delta$ escapes. The algebra, the norm and the units are those of *Dual-Numbers Algebra* and *Dual-Numbers Norm and Invertibility*; the real quadratic family that the base dynamics repeats is that of *The Mandelbrot Set and the Quadratic Family*; and the infinitesimal coordinate, the derivative cocycle, is the subject of *The Infinitesimal Dynamics of the Dual Numbers*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}' = \mathbb{R}[\varepsilon]$, $\varepsilon^2=0$ | Dual numbers |
| $z = x+\varepsilon y$ | Element, with real part $x$ and infinitesimal part $y$ |
| $\bar z = x-\varepsilon y$, $N(z) = x^2$ | Conjugation and norm |
| $f_c(z) = z^2+c$ | The dual quadratic family |
| $g_\gamma(x) = x^2+\gamma$ | The real quadratic map of the real part |
| $\mathbb{R}\varepsilon$ | The ideal of the nilpotents, the critical locus |
| $P_n(\gamma)$ | Partial sums of the derivative cocycle; $y_n = \delta P_n$ |
| $M_{\mathbb{D}'}$ | Connectedness locus; projects onto $[-2,\tfrac14]$ |

## Further Reading

- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the dual numbers and their infinitesimal interpretation.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of the two-dimensional real algebras.
- Robert L. Devaney, *An Introduction to Chaotic Dynamical Systems*, 2nd edition (Addison-Wesley, 1989), for the real quadratic family and its interval of bounded orbits.
- Benoit B. Mandelbrot, "On the quadratic mapping $z \mapsto z^2-\mu$", *Physica D* 7 (1983), 224–239, for the quadratic family in the complex case.
