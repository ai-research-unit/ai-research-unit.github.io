# __Square Roots of a General Element in the Quaternion Algebra__

## Introduction

This article solves the equation $\tilde q_2^2=\tilde q_1$ in $\mathbb{H}$ for an arbitrary $\tilde q_1$. It is the general case of which *Square Roots of One and the Idempotents of the Quaternion Algebra* and *Square Roots of Zero and the Nilpotents of the Quaternion Algebra*, above this article in this category, treat the three central values; the method is the split of a quaternion into its scalar and its vector part and the resulting pair of a quadratic and a linear equation, and it uses neither Clifford algebras nor forms. The result is a classification by the vanishing of the vector part of $\tilde q_1$: away from the scalar line there are exactly two roots, and on the scalar line the count is two roots, one root or a sphere of roots according as the scalar is positive, zero or negative. The quaternion norm and the invertibility criterion are *Norm and Invertibility in the Quaternion Algebra*, above this article in this category, and they are neither used nor needed.

## The Reduction

Throughout, $\tilde q_1=q_{1t}e_t+\vec q_1$ and $\tilde q_2=q_{2t}e_t+\vec q_2$ with $q_{1t},q_{2t}\in\mathbb{R}$ and $\vec q_1,\vec q_2$ in the vector subspace $V=\mathbb{R}\vec e_x+\mathbb{R}\vec e_y+\mathbb{R}\vec e_z$, and $|\vec q_2|^2=q_{2x}^2+q_{2y}^2+q_{2z}^2$ is the sum of the squares of the three coordinates, a non-negative real number.

**Proposition (the square).** For $\tilde q_2=q_{2t}e_t+\vec q_2$,

$$
\tilde q_2^2=(q_{2t}^2-|\vec q_2|^2)e_t+2q_{2t}\vec q_2.
$$

*Proof.* Expand: $q_{2t}^2+2q_{2t}\vec q_2+\vec q_2^2$. The square of a vector is the scalar $\vec q_2^2=-|\vec q_2|^2$, because the vector coordinates anticommute in pairs and $\vec e_\mu^2=-e_t$; the cross terms cancel in pairs.

**Corollary.** The equation $\tilde q_2^2=\tilde q_1$ is the pair

$$
2q_{2t}\vec q_2=\vec q_1,\qquad q_{2t}^2-|\vec q_2|^2=q_{1t}.
$$

The second is the **reduced quadratic** in the unknown $t=q_{2t}^2$; when $\vec q_1\neq0$ the first determines $\vec q_2=\vec q_1/(2q_{2t})$ and the second becomes the quadratic

$$
t^2-q_{1t}t-\tfrac14|\vec q_1|^2=0,\qquad \Delta=q_{1t}^2+|\vec q_1|^2,
$$

with discriminant $\Delta\geq0$ and $\sqrt\Delta=|\tilde q_1|$.

## The Two Cases

**Theorem (non-scalar case).** Let $\vec q_1\neq0$. Then $\tilde q_1$ has exactly two square roots, and they are

$$
\tilde q_{2\pm}=\pm\Bigl(\sqrt{\tfrac12\bigl(q_{1t}+|\tilde q_1|\bigr)}\;e_t+\frac{\vec q_1}{2\sqrt{\tfrac12(q_{1t}+|\tilde q_1|)}}\Bigr).
$$

*Proof.* The vector equation $2q_{2t}\vec q_2=\vec q_1$ forces $q_{2t}\neq0$ and $\vec q_2=\vec q_1/(2q_{2t})$. Substituting in the reduced quadratic gives $4q_{2t}^4-4q_{1t}q_{2t}^2-|\vec q_1|^2=0$, that is $t^2-q_{1t}t-\tfrac14|\vec q_1|^2=0$ with roots $\tfrac12(q_{1t}\pm\sqrt\Delta)$. The minus root is $\tfrac12(q_{1t}-|\tilde q_1|)$, negative because $\vec q_1\neq0$ gives $|\tilde q_1|>|q_{1t}|$; it yields no real $q_{2t}$. The plus root is $\tfrac12(q_{1t}+|\tilde q_1|)>0$, and it yields the two values $q_{2t}=\pm\sqrt{\tfrac12(q_{1t}+|\tilde q_1|)}$ and the two displayed roots. Since $q_{2t}\neq0$ and $\vec q_2$ is determined by $q_{2t}$, there are no others.

**Theorem (scalar case).** Let $\tilde q_1=q_{1t}e_t$, so $\vec q_1=0$. Then

$$
\tilde q_2^2=q_{1t}e_t\iff
\begin{cases}
\tilde q_2=\pm\sqrt{q_{1t}}\,e_t, & q_{1t}>0,\\
\tilde q_2=0, & q_{1t}=0,\\
\tilde q_2=\vec q_2\in V,\quad |\vec q_2|^2=-q_{1t}, & q_{1t}<0.
\end{cases}
$$

*Proof.* With $\vec q_1=0$ the vector equation reads $q_{2t}\vec q_2=0$, so $q_{2t}=0$ or $\vec q_2=0$. If $\vec q_2=0$ the scalar equation is $q_{2t}^2=q_{1t}$, solvable only for $q_{1t}\geq0$, giving $\pm\sqrt{q_{1t}}e_t$ for $q_{1t}>0$ and $0$ for $q_{1t}=0$. If $q_{2t}=0$ the scalar equation is $-|\vec q_2|^2=q_{1t}$, solvable only for $q_{1t}\leq0$, giving $|\vec q_2|^2=-q_{1t}$; for $q_{1t}=0$ this is again $\tilde q_2=0$, and for $q_{1t}<0$ it is the level set of a positive-definite quadratic form on the three-dimensional space $V$, a sphere of roots.

**Theorem (classification).** Every $\tilde q_1\in\mathbb{H}$ has at least one square root, and the root set is

| Case | Root set | Cardinality |
|---|---|---|
| $\vec q_1\neq0$ | $\{\tilde q_{2+},\tilde q_{2-}\}$ | two |
| $\vec q_1=0$, $q_{1t}>0$ | $\{\pm\sqrt{q_{1t}}e_t\}$ | two |
| $\vec q_1=0$, $q_{1t}=0$ | $\{0\}$ | one |
| $\vec q_1=0$, $q_{1t}<0$ | $\{\vec q_2\in V : |\vec q_2|^2=-q_{1t}\}$ | a sphere |

*Proof.* The two preceding theorems.

The minus root of the reduced quadratic is what the positive-definiteness of the sum of squares discards.

## The Specialisation to the Central Values

The three central equations of *Square Roots of One and the Idempotents of the Quaternion Algebra* and *Square Roots of Zero and the Nilpotents of the Quaternion Algebra*, above this article in this category, are the cases $\vec q_1=0$, $q_{1t}=-1,0,1$ of the classification:

- $q_{1t}=-1$: the sphere $\{\vec q_2\in V : |\vec q_2|^2=1\}$, the unit sphere of the vector subspace, matching the roots of $-1$;
- $q_{1t}=0$: the single root $0$, matching the root set of $0$;
- $q_{1t}=1$: the pair $\{\pm e_t\}$, matching the roots of $+1$.

The count of the roots of $-1$ is a two-dimensional sphere, that of $+1$ is two points, and that of $0$ is one point; these are the three values of the classification table, and the agreement is a consistency check on the two articles rather than a new computation.

## Worked Examples

Each root below is checked by squaring.

- $\tilde q_1=4e_t$: the roots are $\pm2e_t$, and $(-2e_t)^2=4e_t$.
- $\tilde q_1=0$: the only root is $0$.
- $\tilde q_1=-4e_t$: the roots are the pure quaternions $\vec q_2$ with $q_{2x}^2+q_{2y}^2+q_{2z}^2=4$, for instance $\tilde q_2=2\vec e_y$, and $(2\vec e_y)^2=-4e_t$.
- $\tilde q_1=\vec e_x$, a pure unit quaternion: $|\tilde q_1|=1$ and $\tfrac12(q_{1t}+|\tilde q_1|)=\tfrac12$, so $\tilde q_{2\pm}=\pm\bigl(\tfrac{1}{\sqrt2}e_t+\tfrac{1}{\sqrt2}\vec e_x\bigr)$; squaring gives $\tfrac12-\tfrac12+2\cdot\tfrac12 \vec e_x=\vec e_x$.
- $\tilde q_1=3e_t+2\vec e_x+2\vec e_y$: $|\tilde q_1|=\sqrt{9+4+4}=\sqrt{17}$, so $q_{2t}^2=\tfrac12(3+\sqrt{17})\approx3.56$, so $\tilde q_2\approx1.89\,e_t+0.53\,\vec e_x+0.53\,\vec e_y$; squaring returns $\tilde q_1$ to the precision of the arithmetic.
- $\tilde q_1=-3e_t+4\vec e_z$: $|\tilde q_1|=5$, $q_{2t}^2=\tfrac12(-3+5)=1$, and the roots are $\pm(e_t+2\vec e_z)$, since $(e_t+2\vec e_z)^2=e_t+4\vec e_z-4e_t=-3e_t+4\vec e_z$.

## Summary

Writing $\tilde q_1=q_{1t}e_t+\vec q_1$ and $\tilde q_2=q_{2t}e_t+\vec q_2$, the square is $\tilde q_2^2=(q_{2t}^2-|\vec q_2|^2)e_t+2q_{2t}\vec q_2$, so the equation $\tilde q_2^2=\tilde q_1$ is the vector equation $2q_{2t}\vec q_2=\vec q_1$ and the reduced quadratic $t^2-q_{1t}t-\tfrac14|\vec q_1|^2=0$ in $t=q_{2t}^2$, whose discriminant is $\Delta=q_{1t}^2+|\vec q_1|^2\geq0$. If the vector part of $\tilde q_1$ does not vanish there are exactly two roots, $\pm\tilde q_2$ with $q_{2t}=\sqrt{\tfrac12(q_{1t}+|\tilde q_1|)}$ and $\vec q_2=\vec q_1/(2q_{2t})$; if it vanishes the roots are $\pm\sqrt{q_{1t}}e_t$ for $q_{1t}>0$, the single root $0$ for $q_{1t}=0$, and the sphere $\{|\vec q_2|^2=-q_{1t}\}$ for $q_{1t}<0$. Every quaternion therefore has at least one square root over $\mathbb{R}$, and the three central equations $q_{1t}=-1,0,1$ reproduce the roots of $-1$, of $0$ and of $+1$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde q_1=q_{1t}e_t+\vec q_1$ | Quaternion split into scalar part $q_{1t}$ and vector part $\vec q_1$ |
| $\tilde q_2=q_{2t}e_t+\vec q_2$ | The unknown root, similarly split |
| $V=\mathbb{R}\vec e_x+\mathbb{R}\vec e_y+\mathbb{R}\vec e_z$ | The vector subspace |
| $|\vec q_2|^2=q_{2x}^2+q_{2y}^2+q_{2z}^2$ | Sum of the squares of the vector coordinates |
| $t=q_{2t}^2$ | The unknown of the reduced quadratic |
| $\Delta=q_{1t}^2+|\vec q_1|^2$ | Discriminant of the reduced quadratic, $=|\tilde q_1|^2$ |

## Further Reading

- [Introduction to the Quaternion Algebra](introduction-to-the-quaternion-algebra.html), for the product, the unit and the square.
- [Square Roots of One and the Idempotents of the Quaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-quaternion-algebra.html), above this article in this category, for the central values $+1$ and $-1$ and the idempotents.
- [Square Roots of Zero and the Nilpotents of the Quaternion Algebra](square-roots-of-zero-and-the-nilpotents-of-the-quaternion-algebra.html), above this article in this category, for the central value $0$ and the empty nilpotent class.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the square of a quaternion and the vector-part computation.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the square and the square-root problem on the quaternion sphere.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the square roots of quaternions and the role of the vector part.
