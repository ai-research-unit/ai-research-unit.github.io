# __Square Roots of a General Element in the General Plain Algebra__

## Introduction

This article solves the equation $\tilde p^2=\tilde q$ in $\mathbb{H}$ for an arbitrary $\tilde q$. It is the general case of which *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, above this article in this category, treats the three central values; the method is the split of a quaternion into its scalar and its vector part and the resulting pair of a quadratic and a linear equation, and it uses neither Clifford algebras nor forms. The result is a classification by the vanishing of the vector part of $\tilde q$: away from the scalar line there are exactly two roots, and on the scalar line the count is two roots, one root or a sphere of roots according as the scalar is positive, zero or negative. The quaternion norm and the invertibility criterion are *Norm and Invertibility in the General Plain Algebra*, above this article in this category, and they are neither used nor needed.

## The Reduction

Throughout, $\tilde q=q_0+\mathbf Q$ and $\tilde p=p_0+\mathbf P$ with $q_0,p_0\in\mathbb{R}$ and $\mathbf Q,\mathbf P$ in the vector subspace $V=\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$, and $|\mathbf P|^2=p_1^2+p_2^2+p_3^2$ is the sum of the squares of the three coordinates, a non-negative real number.

**Proposition (the square).** For $\tilde p=p_0+\mathbf P$,

$$
\tilde p^2=(p_0^2-|\mathbf P|^2)+2p_0\mathbf P .
$$

*Proof.* Expand: $p_0^2+2p_0\mathbf P+\mathbf P^2$. The square of a vector is the scalar $\mathbf P^2=-|\mathbf P|^2$, because the vector coordinates anticommute in pairs and $e_k^2=-e_0$; the cross terms cancel in pairs.

**Corollary.** The equation $\tilde p^2=\tilde q$ is the pair

$$
2p_0\mathbf P=\mathbf Q,\qquad p_0^2-|\mathbf P|^2=q_0 .
$$

The second is the **reduced quadratic** in the unknown $t=p_0^2$; when $\mathbf Q\neq0$ the first determines $\mathbf P=\mathbf Q/(2p_0)$ and the second becomes the quadratic

$$
t^2-q_0t-\tfrac14|\mathbf Q|^2=0,\qquad \Delta=q_0^2+|\mathbf Q|^2,
$$

with discriminant $\Delta\geq0$ and $\sqrt\Delta=|\tilde q|$.

## The Two Cases

**Theorem (non-scalar case).** Let $\mathbf Q\neq0$. Then $\tilde q$ has exactly two square roots, and they are

$$
\tilde p_\pm=\pm\Bigl(\sqrt{\tfrac12\bigl(q_0+|\tilde q|\bigr)}\;e_0+\frac{\mathbf Q}{2\sqrt{\tfrac12(q_0+|\tilde q|)}}\Bigr).
$$

*Proof.* The vector equation $2p_0\mathbf P=\mathbf Q$ forces $p_0\neq0$ and $\mathbf P=\mathbf Q/(2p_0)$. Substituting in the reduced quadratic gives $4p_0^4-4q_0p_0^2-|\mathbf Q|^2=0$, that is $t^2-q_0t-\tfrac14|\mathbf Q|^2=0$ with roots $\tfrac12(q_0\pm\sqrt\Delta)$. The minus root is $\tfrac12(q_0-|\tilde q|)$, negative because $\mathbf Q\neq0$ gives $|\tilde q|>|q_0|$; it yields no real $p_0$. The plus root is $\tfrac12(q_0+|\tilde q|)>0$, and it yields the two values $p_0=\pm\sqrt{\tfrac12(q_0+|\tilde q|)}$ and the two displayed roots. Since $p_0\neq0$ and $\mathbf P$ is determined by $p_0$, there are no others.

**Theorem (scalar case).** Let $\tilde q=q_0e_0$, so $\mathbf Q=0$. Then

$$
\tilde p^2=q_0e_0\iff
\begin{cases}
\tilde p=\pm\sqrt{q_0}\,e_0, & q_0>0,\\
\tilde p=0, & q_0=0,\\
\tilde p=\mathbf P\in V,\quad |\mathbf P|^2=-q_0, & q_0<0 .
\end{cases}
$$

*Proof.* With $\mathbf Q=0$ the vector equation reads $p_0\mathbf P=0$, so $p_0=0$ or $\mathbf P=0$. If $\mathbf P=0$ the scalar equation is $p_0^2=q_0$, solvable only for $q_0\geq0$, giving $\pm\sqrt{q_0}e_0$ for $q_0>0$ and $0$ for $q_0=0$. If $p_0=0$ the scalar equation is $-|\mathbf P|^2=q_0$, solvable only for $q_0\leq0$, giving $|\mathbf P|^2=-q_0$; for $q_0=0$ this is again $\tilde p=0$, and for $q_0<0$ it is the level set of a positive-definite quadratic form on the three-dimensional space $V$, a sphere of roots.

**Theorem (classification).** Every $\tilde q\in\mathbb{H}$ has at least one square root, and the root set is

| Case | Root set | Cardinality |
|---|---|---|
| $\mathbf Q\neq0$ | $\{\tilde p_+,\tilde p_-\}$ | two |
| $\mathbf Q=0$, $q_0>0$ | $\{\pm\sqrt{q_0}e_0\}$ | two |
| $\mathbf Q=0$, $q_0=0$ | $\{0\}$ | one |
| $\mathbf Q=0$, $q_0<0$ | $\{\mathbf P\in V : |\mathbf P|^2=-q_0\}$ | a sphere |

*Proof.* The two preceding theorems.

**Remark.** The reduced quadratic always has the discriminant $\Delta=q_0^2+|\mathbf Q|^2$, a non-negative real, so a real square root is never excluded; the "no root" slot that a general real quadratic equation can occupy is empty over $\mathbb{R}$, and it is the complex coefficient field of the biquaternion chapter that makes it non-empty there. The minus root of the reduced quadratic is what the positive-definiteness of the sum of squares discards.

## The Specialisation to the Central Values

The three central equations of *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, above this article in this category, are the cases $\mathbf Q=0$, $q_0=-1,0,1$ of the classification:

- $q_0=-1$: the sphere $\{\mathbf P\in V : |\mathbf P|^2=1\}$, the unit sphere of the vector subspace, matching the roots of $-1$;
- $q_0=0$: the single root $0$, matching the root set of $0$;
- $q_0=1$: the pair $\{\pm e_0\}$, matching the roots of $+1$.

The count of the roots of $-1$ is a two-dimensional sphere, that of $+1$ is two points, and that of $0$ is one point; these are the three values of the classification table, and the agreement is a consistency check on the two articles rather than a new computation.

## Worked Examples

Each root below is checked by squaring.

- $\tilde q=4e_0$: the roots are $\pm2e_0$, and $(-2e_0)^2=4e_0$.
- $\tilde q=0$: the only root is $0$.
- $\tilde q=-4e_0$: the roots are the pure quaternions $\mathbf P$ with $p_1^2+p_2^2+p_3^2=4$, for instance $\tilde p=2e_2$, and $(2e_2)^2=-4e_0$.
- $\tilde q=e_1$, a pure unit quaternion: $|\tilde q|=1$ and $\tfrac12(q_0+|\tilde q|)=\tfrac12$, so $\tilde p_\pm=\pm\bigl(\tfrac{1}{\sqrt2}e_0+\tfrac{1}{\sqrt2}e_1\bigr)$; squaring gives $\tfrac12-\tfrac12+2\cdot\tfrac12 e_1=e_1$.
- $\tilde q=3+2e_1+2e_2$: $|\tilde q|=\sqrt{9+4+4}=\sqrt{17}$, so $p_0^2=\tfrac12(3+\sqrt{17})\approx3.56$, so $\tilde p\approx1.89\,e_0+0.53\,e_1+0.53\,e_2$; squaring returns $\tilde q$ to the precision of the arithmetic.
- $\tilde q=-3+4e_3$: $|\tilde q|=5$, $p_0^2=\tfrac12(-3+5)=1$, and the roots are $\pm(e_0+2e_3)$, since $(e_0+2e_3)^2=e_0+4e_3-4e_0=-3+4e_3$.

## Summary

Writing $\tilde q=q_0+\mathbf Q$ and $\tilde p=p_0+\mathbf P$, the square is $\tilde p^2=(p_0^2-|\mathbf P|^2)+2p_0\mathbf P$, so the equation $\tilde p^2=\tilde q$ is the vector equation $2p_0\mathbf P=\mathbf Q$ and the reduced quadratic $t^2-q_0t-\tfrac14|\mathbf Q|^2=0$ in $t=p_0^2$, whose discriminant is $\Delta=q_0^2+|\mathbf Q|^2\geq0$. If the vector part of $\tilde q$ does not vanish there are exactly two roots, $\pm\tilde p$ with $p_0=\sqrt{\tfrac12(q_0+|\tilde q|)}$ and $\mathbf P=\mathbf Q/(2p_0)$; if it vanishes the roots are $\pm\sqrt{q_0}e_0$ for $q_0>0$, the single root $0$ for $q_0=0$, and the sphere $\{|\mathbf P|^2=-q_0\}$ for $q_0<0$. Every quaternion therefore has at least one square root over $\mathbb{R}$, and the three central equations $q_0=-1,0,1$ reproduce the roots of $-1$, of $0$ and of $+1$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde q=q_0+\mathbf Q$ | Quaternion split into scalar part $q_0$ and vector part $\mathbf Q$ |
| $\tilde p=p_0+\mathbf P$ | The unknown root, similarly split |
| $V=\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$ | The vector subspace |
| $|\mathbf P|^2=p_1^2+p_2^2+p_3^2$ | Sum of the squares of the vector coordinates |
| $t=p_0^2$ | The unknown of the reduced quadratic |
| $\Delta=q_0^2+|\mathbf Q|^2$ | Discriminant of the reduced quadratic, $=|\tilde q|^2$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the square of a quaternion and the vector-part computation.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the square and the square-root problem on the quaternion sphere.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the square roots of quaternions and the role of the vector part.
