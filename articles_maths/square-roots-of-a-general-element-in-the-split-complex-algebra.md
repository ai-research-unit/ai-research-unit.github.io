# __Square Roots of a General Element in the Split-Complex Algebra__

## Introduction

This article solves the square-root problem in the split-complex algebra $\mathbb{D}$: given $Q\in\mathbb{D}$, find every $\Xi\in\mathbb{D}$ with

$$
\Xi^{2}=Q .
$$

The method needs no norm and no form. It is the same idempotent-coordinate split that solves the two central cases $\Xi^{2}=0$ and $\Xi^{2}=1$ in *Square Roots of Zero and the Nilpotents of the Split-Complex Algebra* and *Square Roots of One and the Idempotents of the Split-Complex Algebra*, carried one step further: the split turns the equation into two independent scalar equations,

$$
\Xi_{+}^{2}=Q_{+},\qquad \Xi_{-}^{2}=Q_{-},
$$

one for each idempotent coordinate. Each equation is a one-dimensional real square-root problem, and the answer is read off the signs of $Q_{+}$ and $Q_{-}$: four roots when both are positive, two when exactly one is zero and the other positive, one when both are zero, and none otherwise. The roots are finite in every case; there is no continuous family, because the two coordinates are real and independent.

**The results.** For a radicand $Q=Q_{+}\Pi_{+}+Q_{-}\Pi_{-}$ the roots are the elements

$$
\Xi=\varepsilon_{+}\sqrt{Q_{+}}\,\Pi_{+}+\varepsilon_{-}\sqrt{Q_{-}}\,\Pi_{-},\qquad \varepsilon_{\pm}\in\{+1,-1\},
$$

taken over the signs for which the square roots are real. There are **four roots** when $Q_{+}>0$ and $Q_{-}>0$, **two** when exactly one coordinate is zero and the other is positive, **one** when $Q=0$, and **none** when one of the coordinates is negative. The roots come in pairs $\pm\Xi$ except at $Q=0$, where the two signs coincide. The three central values recover the known sets: $\Xi^{2}=1$ has the four roots $\pm1,\pm j$; $\Xi^{2}=0$ has the one root $0$; $\Xi^{2}=-1$ has none. The image of the square map is the forward cone $Q_{+}\ge0$, $Q_{-}\ge0$; the order cone it defines is *The Classes of Element of the Split-Complex Algebra*.

The article is algebraic. The two central values are recovered in §*The Three Central Values*, which checks this method against the direct computations of the two companion articles. The zero-divisor cone, of which the boundary of the forward cone is a part, is *Zero Divisors of the Split-Complex Algebra*, named here only where the classification touches it. The polar and exponential decompositions that the answer must be consistent with are *Modulus–Unit Polar Decomposition of Split-Complex Numbers* and *Exponential Polar Decomposition of Split-Complex Numbers*.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked.

Throughout, the algebra is $\mathbb{D}=\mathbb{R}[j]$, $j^{2}=+1$, a general element is $Q=q+jq'$, the conjugation is $\bar Q=q-jq'$, and the idempotents are $\Pi_{\pm}=\tfrac12(1\pm j)$, with idempotent coordinates $Q=Q_{+}\Pi_{+}+Q_{-}\Pi_{-}$ and $Q_{\pm}=q\pm q'$. A root is written $\Xi=x+jx'$, with idempotent coordinates $\Xi_{\pm}=x\pm x'$.

The equation $\Xi^{2}=Q$ names a product, so the root is relative to it. The plain square $\Xi\Xi$ and the general definition with the roots of a central value are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*Powers, the Square and the Roots*; throughout this article the square is the one of the general plain bilinear product $\Xi\Xi$, the multiplication of the split-complex algebra, and the other product of the space and its root problem are *Relations and Comparison Between the Two Products of the Split-Complexoid Space*.

## The Reduction

Write the root and the radicand in the idempotent coordinates,

$$
\Xi=\Xi_{+}\Pi_{+}+\Xi_{-}\Pi_{-},\qquad
Q=Q_{+}\Pi_{+}+Q_{-}\Pi_{-},
$$

with $\Xi_{\pm}=x\pm x'$ and $Q_{\pm}=q\pm q'$ real. Because the product is componentwise in the idempotent basis and $\Pi_{\pm}^{2}=\Pi_{\pm}$, $\Pi_{+}\Pi_{-}=0$, the square is

$$
\Xi^{2}=\Xi_{+}^{2}\Pi_{+}+\Xi_{-}^{2}\Pi_{-}.
$$

The equation $\Xi^{2}=Q$ is therefore equivalent to the **pair of independent real equations**

$$
\Xi_{+}^{2}=Q_{+},\qquad \Xi_{-}^{2}=Q_{-}.
$$

There is no coupling between the two coordinates, and each equation is the ordinary real square-root problem. The whole classification follows from the signs of $Q_{+}$ and $Q_{-}$.

**Remark (the scalar form).** In the basis $1,j$ the same equations read

$$
x^{2}+x'^{2}=q,\qquad 2xx'=q',
$$

because $\Xi^{2}=(x^{2}+x'^{2})+2xx'j$. Adding and subtracting gives the two idempotent equations, and solving them directly reproduces the classification; the idempotent form is the shorter route.

## The Roots with Positive Coordinates

**If $Q_{+}>0$ and $Q_{-}>0$ then the equation has exactly four roots,**

$$
\boxed{\;\Xi=\varepsilon_{+}\sqrt{Q_{+}}\,\Pi_{+}+\varepsilon_{-}\sqrt{Q_{-}}\,\Pi_{-},\qquad \varepsilon_{+},\varepsilon_{-}\in\{+1,-1\}\;}.
$$

**Proof.** Each of the two real equations $\Xi_{\pm}^{2}=Q_{\pm}$ has the two solutions $\Xi_{\pm}=\pm\sqrt{Q_{\pm}}$ when $Q_{\pm}>0$. The four combinations are distinct, because the two coordinates are independent and the two square roots are nonzero. Each combination is a root by the reduction, and every root arises this way.

**Corollary (the pairs).** The four roots are the two pairs

$$
\pm\Bigl(\sqrt{Q_{+}}\,\Pi_{+}+\sqrt{Q_{-}}\,\Pi_{-}\Bigr),\qquad
\pm\Bigl(\sqrt{Q_{+}}\,\Pi_{+}-\sqrt{Q_{-}}\,\Pi_{-}\Bigr),
$$

so the roots come in opposite pairs and $\Xi$ and $-\Xi$ have the same square.

**Remark (the scalar coordinates).** In the basis $1,j$ one root is

$$
\Xi=\tfrac12\Bigl(\sqrt{Q_{+}}+\sqrt{Q_{-}}\Bigr)+\tfrac12\Bigl(\sqrt{Q_{+}}-\sqrt{Q_{-}}\Bigr)j,
$$

and the other three are obtained by the two independent sign changes. The four roots are the four sign choices, not the four rotations of a single root.

## The Roots on the Boundary

**If exactly one of $Q_{+},Q_{-}$ is zero and the other is positive, the equation has exactly two roots; the vanishing coordinate of the root is zero, and the root lies on one of the two null lines.**

There are two cases.

- If $Q_{+}>0$ and $Q_{-}=0$, then $\Xi_{-}^{2}=0$ forces $\Xi_{-}=0$ and $\Xi_{+}^{2}=Q_{+}$ gives $\Xi_{+}=\pm\sqrt{Q_{+}}$. The roots are

$$
\boxed{\;\Xi=\pm\sqrt{Q_{+}}\,\Pi_{+}\;}.
$$

They are the two points $\pm\sqrt{Q_{+}}\,\Pi_{+}$ of the line $\mathbb{R}\Pi_{+}$, and they are zero divisors of the algebra.

- If $Q_{+}=0$ and $Q_{-}>0$, then symmetrically

$$
\Xi=\pm\sqrt{Q_{-}}\,\Pi_{-},
$$

the two points of the opposite null line.

In both cases the two roots are opposite, $\pm\Xi$, and they are nonzero zero divisors. The radicand is itself a zero divisor in these cases, since one of its idempotent coordinates vanishes.

**Proposition.** On the boundary of the forward cone the root set has two elements, and each root lies on the same null line as the radicand.

**Proof.** The vanishing coordinate of the radicand forces the same coordinate of the root to vanish, and the nonzero coordinate has the two signs. The line $\mathbb{R}\Pi_{+}$ is the support of the radicand and of its roots in the first case, and $\mathbb{R}\Pi_{-}$ in the second.

## The Roots of a Real Scalar

**For a real scalar radicand $Q=\lambda$, $\lambda\in\mathbb{R}$, the roots are: four, $\pm\sqrt{\lambda}$ and $\pm j\sqrt{\lambda}$, when $\lambda>0$; one, $0$, when $\lambda=0$; none when $\lambda<0$.**

Let $Q=\lambda$ with $\lambda\in\mathbb{R}$. Then $Q_{+}=Q_{-}=\lambda$, and the two equations are the same equation $\Xi_{\pm}^{2}=\lambda$.

- If $\lambda>0$, each coordinate has the two signs $\pm\sqrt{\lambda}$, and the four roots are

$$
\Xi=\pm\sqrt{\lambda}\,\Pi_{+}\pm\sqrt{\lambda}\,\Pi_{-},
$$

that is the four elements

$$
+\sqrt{\lambda},\qquad -\sqrt{\lambda},\qquad +\sqrt{\lambda}\,j,\qquad -\sqrt{\lambda}\,j .
$$

The first two are the real roots, the last two the split-imaginary roots.

- If $\lambda=0$, the only root is $\Xi=0$.
- If $\lambda<0$, neither coordinate has a real square root, and there is no root.

**Corollary (the roots of a positive scalar form a scaled copy of the four-element group).** For $\lambda>0$ the root set is $\sqrt{\lambda}\,\{1,-1,j,-j\}$, a scaled copy of the four-element group of *Square Roots of One and the Idempotents of the Split-Complex Algebra*.

## The Classification

**The root set of $\Xi^{2}=Q$ is classified by the signs of the two idempotent coordinates of $Q$: four roots if both are positive, two if exactly one is zero and the other positive, one if both are zero, and none if either is negative.**

**Theorem (the classification).** Let $Q=Q_{+}\Pi_{+}+Q_{-}\Pi_{-}$. The number of roots of $\Xi^{2}=Q$ and their form are as follows.

| $Q_{+}$ | $Q_{-}$ | roots | number |
|---|---|---|---|
| $>0$ | $>0$ | $\pm\sqrt{Q_{+}}\,\Pi_{+}\pm\sqrt{Q_{-}}\,\Pi_{-}$ | $4$ |
| $>0$ | $=0$ | $\pm\sqrt{Q_{+}}\,\Pi_{+}$ | $2$ |
| $=0$ | $>0$ | $\pm\sqrt{Q_{-}}\,\Pi_{-}$ | $2$ |
| $=0$ | $=0$ | $0$ | $1$ |
| $<0$ | any | none | $0$ |
| any | $<0$ | none | $0$ |

**Proof.** The reduction gives the two independent equations $\Xi_{\pm}^{2}=Q_{\pm}$. A real equation $t^{2}=a$ has two solutions when $a>0$, one when $a=0$, and none when $a<0$. The number of roots of the pair is the product of the numbers for the two coordinates, and the form is the product of the solution sets. The table enumerates the sign cases; the last two rows both encode the case in which at least one coordinate is negative, and either negative coordinate alone makes the product of the two solution sets empty.

**Corollary (the dichotomy of the radicand).** The equation has a root exactly when $Q$ lies in the **forward cone**

$$
\boxed{\;\mathcal{C}=\{Q:Q_{+}\ge0,\ Q_{-}\ge0\}=\{Q:q\ge|q'|\}\;},
$$

the closed cone whose two sides are the non-negative rays of the two null lines, containing the positive real axis. The radicands with four roots are the interior of the cone, those with two roots are its boundary minus the origin, those with one root are the origin, and those with no roots are the complement.

**Corollary (roots of units and of zero divisors).** If $Q$ is a unit, every root is a unit. If $Q$ is a nonzero zero divisor, every root is a zero divisor. If $Q=0$, the root is $0$.

**Proof.** A unit has both coordinates nonzero, so a root has both coordinates nonzero, hence is a unit. A zero divisor has exactly one coordinate zero and the other nonzero; a root has the same vanishing coordinate and a nonzero square root in the other, hence is a zero divisor. The origin has the root $0$.

## The Three Central Values

The classification recovers the two companion articles and adds the third central value.

### The Value $+1$

For $Q=1$ one has $Q_{+}=Q_{-}=1$, and the four roots are

$$
\pm\Pi_{+}\pm\Pi_{-}=\pm1,\ \pm j .
$$

This is the four-element set of *Square Roots of One and the Idempotents of the Split-Complex Algebra*.

### The Value $0$

For $Q=0$ one has $Q_{+}=Q_{-}=0$, and the only root is $\Xi=0$. This is the result of *Square Roots of Zero and the Nilpotents of the Split-Complex Algebra*: there is no nonzero square-zero element.

### The Value $-1$

For $Q=-1$ one has $Q_{+}=Q_{-}=-1$, both negative, and there is no root. This is the empty set of *Square Roots of One and the Idempotents of the Split-Complex Algebra*, §*The Roots of Minus One*.

The three central values therefore give the three cardinalities $4,1,0$, and the pattern is the pattern of the signs of the scalar: positive, zero, negative.

## Worked Examples

**Example ($Q=5+3j$).** Here $Q_{+}=8$ and $Q_{-}=2$, both positive, so there are four roots. One of them is

$$
\Xi=\sqrt8\,\Pi_{+}+\sqrt2\,\Pi_{-}
=2\sqrt2\cdot\tfrac12(1+j)+\sqrt2\cdot\tfrac12(1-j)
=\frac{3\sqrt2}{2}+\frac{\sqrt2}{2}j .
$$

Squaring, $x^{2}+x'^{2}=\tfrac{18}{4}+\tfrac{2}{4}=5$ and $2xx'=2\cdot\tfrac{3\sqrt2}{2}\cdot\tfrac{\sqrt2}{2}=3$, so $\Xi^{2}=5+3j$. The other three roots are obtained by changing the signs of the two coordinates.

**Example ($Q=1+j$).** Here $Q_{+}=2$ and $Q_{-}=0$, so there are two roots,

$$
\Xi=\pm\sqrt2\,\Pi_{+}=\pm\frac{1+j}{\sqrt2}.
$$

Squaring, $\sqrt2\,\Pi_{+}$ has square $2\Pi_{+}=1+j$. The roots lie on the null line $\mathbb{R}\Pi_{+}$ and are zero divisors, as the radicand is.

**Example ($Q=j$).** Here $Q_{+}=1$ and $Q_{-}=-1$, one negative, so there is no root. In scalar coordinates the equations would be $x^{2}+x'^{2}=0$ and $2xx'=1$; the first forces $x=x'=0$, and the second then fails.

**Example ($Q=0$).** The only root is $0$.

**Example ($Q=-1$).** There is no root, because both coordinates are negative.

The examples exhibit the four cases of the table: four roots, two roots, no roots, and one root.

## The Image of the Square

**The image of the square map $Q\mapsto Q^{2}$ is the forward cone $\mathcal{C}=\{Q:Q_{+}\ge0,Q_{-}\ge0\}=\{Q:q\ge|q'|\}$; the fibre has four points over the interior, two over the boundary minus the origin, and one over the origin, and up to the sign of the root it has two points over the interior and one over the rest of the cone.**

The square map sends $\Xi=\Xi_{+}\Pi_{+}+\Xi_{-}\Pi_{-}$ to

$$
\Xi^{2}=\Xi_{+}^{2}\Pi_{+}+\Xi_{-}^{2}\Pi_{-},
$$

so the image is the set of radicands whose two coordinates are non-negative squares. That is exactly the forward cone $\mathcal{C}$, the closed cone of angle $90^{\circ}$ between the two null lines and containing the positive real axis. The inverse image of an interior point has four elements, the inverse image of a boundary point other than the origin has two, and the inverse image of the origin has one. The cone is pointed, convex and closed; it is the order cone of the algebra, and its order is developed in *The Classes of Element of the Split-Complex Algebra*, §*The Order Cone of Squares*.

The square map is not injective and not surjective; its fibres have the four, two and one points above. The origin is the only point where the two signs of a root coincide, and the boundary of the cone is the image of the null lines, on which the two signs of the nonzero coordinate are the two roots.

## Summary

The square-root problem in the split-complex algebra reduces to the two independent real equations $\Xi_{+}^{2}=Q_{+}$ and $\Xi_{-}^{2}=Q_{-}$ in the idempotent coordinates. The roots are

$$
\Xi=\varepsilon_{+}\sqrt{Q_{+}}\,\Pi_{+}+\varepsilon_{-}\sqrt{Q_{-}}\,\Pi_{-},
$$

over the signs for which the square roots are real. There are four roots when both coordinates of the radicand are positive, two when exactly one is zero and the other positive, one when the radicand is zero, and none when a coordinate is negative. The roots come in opposite pairs except at the origin; the roots of a unit are units, the roots of a nonzero zero divisor are zero divisors, and the root of $0$ is $0$.

The three central values give the cardinalities $4,1,0$: four roots of $+1$, the root $0$ of $0$, and no root of $-1$. The image of the square map is the forward cone $Q_{+}\ge0,Q_{-}\ge0$, that is $q\ge|q'|$; the square map is four-to-one over the interior of the cone, two-to-one over the boundary minus the origin, and one-to-one at the origin; up to the sign of the root it is a two-to-one cover of the cone, branched along the boundary, the boundary of the cone being the two non-negative null rays. The order cone is the subject of *The Classes of Element of the Split-Complex Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $Q=q+jq'$ | Radicand |
| $\Xi=x+jx'$ | Root |
| $Q_{\pm}=q\pm q'$ | Idempotent coordinates of the radicand |
| $\Xi_{\pm}=x\pm x'$ | Idempotent coordinates of the root |
| $\Xi_{\pm}^{2}=Q_{\pm}$ | The two independent real equations |
| $\mathcal{C}=\{Q:Q_{+}\ge0,Q_{-}\ge0\}=\{q\ge|q'|\}$ | Forward cone, the image of the square |
| $\pm\sqrt{Q_{+}}\,\Pi_{+}\pm\sqrt{Q_{-}}\,\Pi_{-}$ | The four roots in the interior |
| $\pm\sqrt{Q_{+}}\,\Pi_{+}$ | The two roots on the boundary $\mathbb{R}\Pi_{+}$ |

## Further Reading

- [Square Roots of One and the Idempotents of the Split-Complex Algebra](square-roots-of-one-and-the-idempotents-of-the-split-complex-algebra.html), for the value $+1$ and the four roots.
- [Square Roots of Zero and the Nilpotents of the Split-Complex Algebra](square-roots-of-zero-and-the-nilpotents-of-the-split-complex-algebra.html), for the value $0$ and the absence of nilpotents.
- [The Classes of Element of the Split-Complex Algebra](the-classes-of-element-of-the-split-complex-algebra.html), for the order cone of squares and the synthesis of the classes.
- [Zero Divisors of the Split-Complex Algebra](zero-divisors-of-the-split-complex-algebra.html), for the null lines on the boundary of the forward cone.
- [Norm and Invertibility in the General Split-Complex Algebra](norm-and-invertibility-in-the-general-split-complex-algebra.html), for the units and the zero divisors that the roots preserve.
- [Split-Complex Algebra](split-complex-algebra.html), for the algebra and its element theory.
