# __The Infinitesimal Dynamics of the Dual Numbers__

## Introduction

The infinitesimal coordinate of a dual number is not a second dynamical variable; it is the carrier of the **derivative**. For the dual quadratic map $f_c(x+\varepsilon y) = (x^2+\gamma)+\varepsilon(2xy+\delta)$ of *The Dual-Number Quadratic Family*, the infinitesimal part evolves by the affine map $y \mapsto 2xy+\delta$, so the product of the coefficients along an orbit is the derivative of the corresponding real iterate, and the infinitesimal dynamics **is** the derivative cocycle of the real quadratic map $x \mapsto x^2+\gamma$. This article makes that identification, reads the multiplier and the Lyapunov exponent from it, shows that there is no genuinely infinitesimal Julia set — the Fatou and the Julia sets of the dual map are the vertical cylinders over the real ones — and compares the real cocycle with the complex one, where the multiplier carries a rotation that the dual case cannot see.

The article spends the tools of *The Dual-Number Quadratic Family* and of *The Fatou Components and the Classification of the Dynamics*; the algebra of the dual numbers and their parabolic interpretation are those of *Dual-Numbers Algebra* and *Shears and Parabolic Rotations*; the real quadratic dynamics is cited to the real theory of Part III; and the complex derivative cocycle and the multiplier of a hyperbolic component are those of *The Fatou Components and the Classification of the Dynamics* and *The Hyperbolic Geometry of the Split-Complex Julia Sets*. No physics is invoked, and every numerical value displayed was recomputed.

## The Derivative Cocycle

### The Fibre Map Is the Derivative

**Theorem (the cocycle).** Let $x_n = g_\gamma^n(x_0)$ and $y_{n+1} = 2x_ny_n+\delta$ be the two coordinates of the orbit. Then the homogeneous solution is the derivative of the real iterate,

$$
\prod_{k=0}^{n-1} 2x_k = (g_\gamma^n)'(x_0) ,
$$

and the general solution is

$$
y_n = (g_\gamma^n)'(x_0)\,y_0 + \delta \sum_{k=0}^{n-1} \prod_{j=k+1}^{n-1} 2x_j .
$$

**Proof.** The chain rule gives $(g^n)'(x_0) = \prod_{k=0}^{n-1} g'(x_k) = \prod_{k=0}^{n-1} 2x_k$. The affine recursion has the homogeneous solution $\prod 2x_k$ and the particular solution obtained by the variation of constants, which is the displayed sum.

**Remark (what the dual direction records).** The infinitesimal coordinate records two things, and only two: the derivative $(g^n)'(x_0)$ of the real iterate through the homogeneous part, and the accumulated affine term $\delta\sum\prod 2x_j$ through the parameter $\delta$. There is no nonlinearity, no rotation and no second dimension: the entire infinitesimal dynamics is the derivative cocycle of a one-dimensional real map.

**Definition.** The **multiplier** of a periodic orbit $x_0, \ldots, x_{p-1}$ of period $p$ of $g_\gamma$ is

$$
\lambda = (g_\gamma^p)'(x_0) = \prod_{k=0}^{p-1} 2x_k ,
$$

and the **Lyapunov exponent** of an orbit with respect to an invariant measure $\mu$ is

$$
\chi = \lim_{n \to \infty} \frac{1}{n}\log|(g_\gamma^n)'(x_0)| = \frac{1}{p}\log|\lambda| \ \text{ for a periodic orbit} = \int \log|2x|\,d\mu \ \text{ in general} .
$$

**Theorem (what the infinitesimal dynamics reports).** On a periodic orbit of period $p$ the infinitesimal coordinate is multiplied by the multiplier in one period,

$$
y_{n+p} = \lambda\,y_n + (\text{an affine term depending on } \delta) ,
$$

so the cycle is attracting for $|\lambda| < 1$, parabolic for $|\lambda| = 1$ and repelling for $|\lambda| > 1$, exactly as in the real dynamics; and along a typical orbit the infinitesimal coordinate grows at the exponential rate $\chi$, with the growth dominated by the Lyapunov exponent.

**Proof.** Composing the fibre map over one period multiplies the homogeneous part by $\prod_{k=0}^{p-1} 2x_k = \lambda$; the affine term is the finite sum over one period. The classification by $|\lambda|$ is the real multiplier classification, and the exponential rate is the definition of $\chi$ by the ergodic theorem.

**Example.** For $\gamma = 0$ and the fixed point $x = 1$ the multiplier is $\lambda = 2$, so the fixed point is repelling and the infinitesimal coordinate grows like $2^n$; for the fixed point $x = 0$ the multiplier is $\lambda = 0$, superattracting, and the infinitesimal coordinate is constant after the first step, as in the computation of the previous article; for $\gamma = -1$ the two-cycle $\{0,-1\}$ has multiplier $0\cdot(-2) = 0$, superattracting, and $y_n$ is bounded. The values were recomputed.

## The Failure of an Infinitesimal Julia Set

**Definition.** The **Fatou set** of $f_c$ is the set of points of $\mathbb{D}'$ at which the family of iterates is equicontinuous on some neighbourhood, the plane being given the Euclidean metric and its one-point compactification, and the **Julia set** is the complement. The map $f_c$ being triangular, the projection $\pi(z) = x$ carries the dynamics to the real quadratic map $g_\gamma$.

**Theorem (the collapse of the two sets).** For every $c = \gamma+\varepsilon\delta$,

$$
F(f_c) = \pi^{-1}\bigl(F(g_\gamma)\bigr), \qquad J(f_c) = \pi^{-1}\bigl(J(g_\gamma)\bigr) = J(g_\gamma)\times\mathbb{R}\varepsilon ,
$$

so the Fatou and the Julia sets of the dual map are the vertical cylinders over the real Fatou and Julia sets: the dual Julia set is a union of vertical lines, and it has no structure in the infinitesimal direction beyond the factor $\mathbb{R}$.

**Proof.** If $x \in J(g_\gamma)$ then the iterates are not equicontinuous near $x$ already in the real direction, so no point of $x+\mathbb{R}\varepsilon$ is in the Fatou set. If $x \in F(g_\gamma)$ then on a neighbourhood the real orbit is either attracted to an attracting cycle, where $(g^n)'$ is bounded and tends to $0$ on the cycle, or it escapes, where the whole iterates collapse to the point at infinity of the compactified dual plane; in both cases the affine fibre family $\{y \mapsto (g^n)'(x)y+\ldots\}$ is equicontinuous, jointly with the real family, on a neighbourhood of the fibre. Hence the Fatou set is the full preimage of the real one, and the complement is the preimage of the real Julia set.

**Corollary (the failure of a second dimension).** The dual Julia set is fractal exactly to the extent that the real Julia set is: its Hausdorff dimension in the Euclidean metric is $\dim_H J(g_\gamma)+1$ when $J(g_\gamma)$ is nonempty, the addend one being the non-fractal line factor of the infinitesimal direction; and read infinitesimally, with $\varepsilon$ a nilpotent and the set the first-order thickening of $J(g_\gamma)$, the dimension is that of $J(g_\gamma)$. There is no "infinitesimal Julia set" in the sense of a second fractal dimension generated by the dual coordinate; the only fractal data are the real ones.

**Example.** For $\gamma = -2$ the real Julia set is the interval $[-2,2]$, so the dual Julia set is the strip $[-2,2]\times\mathbb{R}\varepsilon$ of Hausdorff dimension $2$, and for $\gamma = 0$ the real Julia set is the two points $\{\pm1\}$, so the dual Julia set is the two vertical lines $x = \pm1$ of dimension $1$. In both cases the fractal content is the real one; the dual coordinate contributes the straight factor.

**Remark (the comparison with the complex derivative cocycle).** In the complex quadratic family the derivative cocycle is the sequence of complex numbers $f_c'(z_n) = 2z_n$, whose product over a cycle is the complex multiplier $\lambda = (f_c^p)'(z_0)$, a rotation together with a scale. The dual cocycle is the real sequence $2x_n$, and its product is the real multiplier: the dual numbers see the modulus of the multiplier and not its argument. This is why the dual theory knows nothing of the rotational structure of *The Fatou Components and the Classification of the Dynamics*: the hyperbolic components, their multipliers and the rotation numbers are invisible without the imaginary direction, and the dual analogue of the multiplier is only the real contraction rate. The infinitesimal dynamics of the shears and the parabolic rotations, where the dual numbers are the linearisation of a rotation, is the subject of *Shears and Parabolic Rotations*.

## Summary

The infinitesimal coordinate of the dual quadratic map evolves by $y \mapsto 2xy+\delta$, and the homogeneous part of its $n$-th iterate is the derivative $(g_\gamma^n)'(x_0)$ of the real iterate: the infinitesimal dynamics **is** the derivative cocycle. Within one period it multiplies the coordinate by the real multiplier $\lambda = (g_\gamma^p)'(x_0)$, so the attracting, parabolic and repelling characters of the real cycles are read on the dual coordinate, and along a typical orbit the growth rate is the Lyapunov exponent $\chi = \int\log|2x|\,d\mu$. The Fatou and Julia sets of the dual map are the vertical cylinders over the real ones, $F(f_c) = \pi^{-1}(F(g_\gamma))$ and $J(f_c) = J(g_\gamma)\times\mathbb{R}\varepsilon$: the dual Julia set is a union of vertical lines, of Hausdorff dimension $\dim_H J(g_\gamma)+1$ in the Euclidean metric and of dimension $\dim_H J(g_\gamma)$ in the infinitesimal reading. There is therefore no genuinely infinitesimal Julia set and no second fractal dimension from the dual coordinate. The complex derivative cocycle, whose multiplier carries a rotation that the real cocycle cannot see, is that of *The Fatou Components and the Classification of the Dynamics*, and the parabolic and shear interpretation of the dual numbers is that of *Shears and Parabolic Rotations*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $x_n = g_\gamma^n(x_0)$ | Real part of the orbit, the base dynamics |
| $y_{n+1} = 2x_ny_n+\delta$ | Infinitesimal coordinate, the fibre recursion |
| $\prod_{k=0}^{n-1}2x_k = (g_\gamma^n)'(x_0)$ | The derivative cocycle |
| $\lambda = (g_\gamma^p)'(x_0)$ | Multiplier of a periodic orbit (real) |
| $\chi = \int\log\lvert 2x\rvert\,d\mu$ | Lyapunov exponent |
| $F(f_c) = \pi^{-1}(F(g_\gamma))$ | Fatou set, the vertical cylinder over the real one |
| $J(f_c) = J(g_\gamma)\times\mathbb{R}\varepsilon$ | Julia set, the vertical cylinder over the real one |
| $\mathbb{R}\varepsilon$ | The infinitesimal direction, a non-fractal line factor |

## Further Reading

- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the dual numbers and the infinitesimal interpretation of $\varepsilon$.
- Robert L. Devaney, *An Introduction to Chaotic Dynamical Systems*, 2nd edition (Addison-Wesley, 1989), for the derivative cocycle, the multiplier and the Lyapunov exponent of the real quadratic family.
- Ricardo Mañé, *Ergodic Theory and Differentiable Dynamics* (Springer, 1987), for the multiplicative ergodic theorem and the Lyapunov exponents of a cocycle.
- John Milnor, *Dynamics in One Complex Variable*, 3rd edition (Princeton University Press, 2006), for the complex multiplier and its role in the hyperbolic components.
