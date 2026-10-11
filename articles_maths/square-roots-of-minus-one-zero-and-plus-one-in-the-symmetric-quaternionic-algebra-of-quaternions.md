# __Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra__

## Introduction

In the symmetric quaternionic block the square of an element is a scalar multiple of $e_0$, and the multiple is the quaternion form:

$$
\tilde x\star\tilde x=N(\tilde x,\tilde x)e_0=\bigl(x_0^{2}+|\mathbf x|^{2}\bigr)e_0 .
$$

The equation $\tilde x\star\tilde x=\lambda e_0$ is therefore one scalar equation in the four coordinates, and its solution set is a level set of the form. This article reads the three level sets that the theory distinguishes, together with the general central value: the roots of $-e_0$, of $0$ and of $+e_0$, and then the roots of $\lambda e_0$ for an arbitrary real $\lambda$. The definition of a **root of a central value** is the general one of *Definitions for the Study of the 6 Algebraic Structures*, §*The Element Vocabulary*, and the square of the block is *Introduction to the Symmetric Quaternionic Algebra of Quaternions*.

**Boundaries.** The block's square and its governing formula are *Introduction to the Symmetric Quaternionic Algebra of Quaternions*; the form is *The 2 Forms over the Quaternion $\mathbb{R}$ Space* and *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*, below this article in this category; the general-radicand case belongs to a later article of the block, and the square-zero elements are *The Specificities of the Symmetric Quaternionic Algebra*, below this article in this category. The parallel over the plain product is *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*; the biquaternion counterpart is *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra*.

**Conventions.** The algebra is $\mathbb{H}$ over $\mathbb{R}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$; an element is $\tilde x=x_0e_0+\mathbf x$ with $\mathbf x=\sum_kx_ke_k$. The **quaternion conjugation** is $\tilde x^{\natural}=x_0e_0-\mathbf x$; the bar is the identity, the star coincides with the natural sign ${}^{\natural}$. The **quaternion form** is $N(\tilde p,\tilde q)=p_0q_0+\mathbf p\cdot\mathbf q$ and $N(\tilde x)=N(\tilde x,\tilde x)=x_0^{2}+|\mathbf x|^{2}$. The **symmetric quaternionic product** is $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$. A **root of the central value** $\lambda e_0$ is an element $\tilde x$ with $\tilde x\star\tilde x=\lambda e_0$.

## The Square of the Form as a Product

**Proposition (the square and its polarisation).** For every $\tilde x$,

$$
\tilde x\star\tilde x=N(\tilde x)\,e_0=\bigl(x_0^{2}+x_1^{2}+x_2^{2}+x_3^{2}\bigr)e_0,
$$

and the square is the polarisation of the form on the diagonal, $2N(\tilde p,\tilde q)e_0=\tilde p\star\tilde p+\tilde q\star\tilde q-(\tilde p-\tilde q)\star(\tilde p-\tilde q)$.

*Proof.* The first display is the governing formula at $\tilde p=\tilde q=\tilde x$. For the polarisation, the block is $\mathbb{R}$-bilinear and commutative, so $(\tilde p+\tilde q)\star(\tilde p+\tilde q)$ expands as $\tilde p\star\tilde p+2\tilde p\star\tilde q+\tilde q\star\tilde q$, and the square of $\tilde p-\tilde q$ is $\tilde p\star\tilde p-2\tilde p\star\tilde q+\tilde q\star\tilde q$; subtracting gives the display.

**Corollary (the square is nonnegative).** Every square is a nonnegative multiple of $e_0$, and $\tilde x\star\tilde x=0$ forces $\tilde x=0$.

*Proof.* $N(\tilde x)=x_0^{2}+|\mathbf x|^{2}\geq0$; the equality of a sum of squares to zero forces every coordinate to zero.

## The Three Root Sets

**Theorem (the three root sets).** The solutions of the three central equations are:

$$
\{\tilde x:\tilde x\star\tilde x=-e_0\}=\varnothing,\qquad
\{\tilde x:\tilde x\star\tilde x=0\}=\{0\},\qquad
\{\tilde x:\tilde x\star\tilde x=e_0\}=\{\tilde x:N(\tilde x)=1\},
$$

and the last set is the level set of the form at $1$, the group of unit quaternions $Sp(1)$ of the algebra, a real algebraic set of real dimension $3$.

*Proof.* By the square formula the equation $\tilde x\star\tilde x=\lambda e_0$ is $N(\tilde x)=\lambda$. For $\lambda=-1$ the left side is a sum of squares, which cannot equal the negative number $-1$. For $\lambda=0$ the sum of squares vanishes only at the origin. For $\lambda=1$ the solution set is the level set of the form at $1$, a nonempty quadric in $\mathbb{R}^4$; it is cut by one equation with nonzero gradient off the origin, hence of real dimension $3$; and it is the set of unit quaternions, closed under the plain product by multiplicativity of the form.

| equation | root set | dimension | reason |
|---|---|---|---|
| $\tilde x\star\tilde x=-e_0$ | $\varnothing$ | — | definiteness, a sum of squares is not negative |
| $\tilde x\star\tilde x=0$ | $\{0\}$ | $0$ | definiteness, a sum of squares vanishes only at $0$ |
| $\tilde x\star\tilde x=e_0$ | $\{N=1\}=Sp(1)$ | $3$ | one equation, nonzero gradient, level set of a definite form |

**Remark (the roots of $+1$ are a group, the roots of $-1$ are empty).** The level set $\{N=1\}$ is the group $Sp(1)$ of unit quaternions under the plain product of $\mathbb{H}$, of real dimension $3$; it is the set that the topology of the chapter names $S^3$ (*Quaternion Topology*, below this article in this category). For the block it is the root set of $+e_0$, and the contrast with the plain product is the point of the next section. The empty root set of $-e_0$ says that the block has no element that plays the role of the imaginary unit of a complex structure: the block admits no complex structure modelled on a root of $-1$, and every square is real and nonnegative.

## The General Central Value

**Theorem (the roots of $\lambda e_0$).** For a real $\lambda$ the solution set of $\tilde x\star\tilde x=\lambda e_0$ is

- $\{0\}$ for $\lambda=0$;
- $\varnothing$ for $\lambda<0$;
- the level set $\{\tilde x:N(\tilde x)=\lambda\}$ of the form, a set of real dimension $3$, for $\lambda>0$.

*Proof.* The equation is $N(\tilde x)=\lambda$, by the square formula, and the three cases are the sign of $\lambda$ read on the sum of squares.

**Corollary (the free parameters and the canonical root).** For $\lambda>0$ the root set is the orbit of the canonical root $\sqrt{\lambda}\,e_0$ under multiplication by unit quaternions: every root is $\tilde x=\sqrt{\lambda}\,\tilde u$ with $\tilde u\in Sp(1)$, the three parameters of $\tilde u$ being the free parameters of the solution; and the map $\tilde u\mapsto\sqrt{\lambda}\,\tilde u$ is a bijection from $Sp(1)$ onto the root set.

*Proof.* $N(\sqrt{\lambda}\tilde u)=\lambda N(\tilde u)=\lambda$ for $\tilde u\in Sp(1)$, so the displayed elements are roots; conversely a root $\tilde x$ with $\lambda>0$ is nonzero, and $\tilde u=\tilde x/\sqrt{N(\tilde x)}$ is a unit quaternion with $\tilde x=\sqrt{\lambda}\tilde u$. The bijection is the inverse of the first statement.

**Remark (the level sets are not preserved by the conjugation).** The quaternion conjugation carries the level set of $\lambda$ onto itself, because $N(\tilde x^{\natural})=N(\tilde x)$ for the real form; the plain conjugation and the star do the same, being the identity and the natural sign. The three levels $-1,0,+1$ are therefore individually invariant under the three conjugations, the invariance of the first and the third being the invariance of $Sp(1)$ and of the empty set.

## The Relation to the Idempotents

**Proposition (the affine map of a root).** For a root $\tilde x$ of $+e_0$ put $\tilde\Pi=\tfrac12(e_0+\tilde x)$. Then

$$
\tilde\Pi\star\tilde\Pi=\tfrac14\bigl(1+2x_0+N(\tilde x)\bigr)e_0=\tfrac14(2+2x_0)e_0=\tfrac{1+x_0}{2}e_0 .
$$

The map $\tilde\Pi$ is idempotent exactly when $\tilde x=\pm e_0$, and then $\tilde\Pi$ is $e_0$ for $\tilde x=e_0$ and $0$ for $\tilde x=-e_0$.

*Proof.* The square is computed from the governing formula, $N(\tilde\Pi)=\tfrac14(1+2x_0+N(\tilde x))$, and $N(\tilde x)=1$ at a root; so $\tilde\Pi\star\tilde\Pi=\tfrac{1+x_0}{2}e_0$. But the element $\tilde\Pi$ itself is $\tfrac{1+x_0}{2}e_0+\tfrac12\mathbf x$, which equals a scalar multiple of $e_0$ only when $\mathbf x=0$; then $N(\tilde x)=x_0^{2}=1$ and $x_0=\pm1$, and the two values give $\tilde\Pi=e_0$ and $\tilde\Pi=0$. The identity $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ therefore holds exactly at $\tilde x=\pm e_0$.

**Remark (no idempotent off the centre).** A noncentral root of $+e_0$, for instance $\tilde x=e_1$, gives $\tilde\Pi=\tfrac12(e_0+e_1)$ with $\tilde\Pi\star\tilde\Pi=\tfrac12e_0\neq\tilde\Pi$, and the difference is the vector part $\tfrac12e_1$; so the affine map carries the roots of $+e_0$ onto elements that are not idempotent as soon as the root is not central. The idempotents of the block are only $0$ and $e_0$, as *The Specificities of the Symmetric Quaternionic Algebra* records.

## The Comparison with the Plain Algebra and with the Biquaternion Case

The plain algebra has a full root theory, and the comparison fixes the originality of the block.

| equation | plain product $\tilde p\tilde q$ | symmetric quaternionic block | biquaternion block |
|---|---|---|---|
| $\tilde x^{2}$ or $\tilde x\star\tilde x=-e_0$ | the pure unit quaternions, real dimension $2$ | empty | a complex quadric, complex dimension $3$ |
| $\tilde x^{2}$ or $\tilde x\star\tilde x=0$ | $\{0\}$ | $\{0\}$ | the isotropic cone, complex dimension $3$ |
| $\tilde x^{2}$ or $\tilde x\star\tilde x=+e_0$ | $\{\pm e_0\}$ | $Sp(1)$, real dimension $3$ | a complex quadric, complex dimension $3$ |

**Proposition (the plain roots).** In the general plain algebra the roots of $-e_0$ are the pure quaternions of unit form, a set of real dimension $2$; the roots of $0$ are only $0$; and the roots of $+e_0$ are $\pm e_0$.

*Proof.* For the plain product $\tilde x^{2}=(x_0^{2}-|\mathbf x|^{2})e_0+2x_0\mathbf x$; the vector part vanishes for $x_0=0$ or $\mathbf x=0$. At $x_0=0$ the square is $-|\mathbf x|^{2}e_0$, giving the roots of $-e_0$ as the pure elements with $|\mathbf x|^{2}=1$, of dimension $2$, and only $0$ as a root of $0$; at $\mathbf x=0$ the equation $x_0^{2}=1$ gives $\pm e_0$, and $x_0^{2}=0$ gives $0$ again. This is *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*.

**Remark (the block turns a two-dimensional family of complex structures into nothing).** The plain algebra has a whole family of square roots of $-e_0$, the pure unit quaternions, and each of them makes the vector subspace a complex vector space; the block has none, because its square is the definite form and a definite form is never negative. Of the three levels of the biquaternion block, which are congruent complex quadrics, the middle one $\{N=0\}$ being the isotropic cone, the real block keeps the level $\{N=1\}$, which is the group $Sp(1)$ of unit quaternions, and collapses the other two, one to the origin and one to the empty set.

## Summary

The square of the block is the definite form, $\tilde x\star\tilde x=(x_0^{2}+|\mathbf x|^{2})e_0$, nonnegative at every element. The root sets of the three central values are the empty set for $-e_0$, the origin for $0$, and the level set $\{N=1\}$ for $+e_0$, the group $Sp(1)$ of unit quaternions of real dimension $3$. For a general central value $\lambda e_0$ the root set is empty for $\lambda<0$, the origin for $\lambda=0$, and the orbit of $\sqrt{\lambda}e_0$ under $Sp(1)$ for $\lambda>0$, with three free parameters. The affine map $\tilde\Pi=\tfrac12(e_0+\tilde x)$ carries the roots of $+e_0$ to idempotents only at the two central roots $\pm e_0$, so the idempotents stay $0$ and $e_0$; and the comparison with the plain algebra, whose roots of $-e_0$ fill a two-dimensional family, and with the biquaternion block, whose three levels are congruent complex quadrics, isolates the definiteness of the coefficient as the single cause.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde x\star\tilde x=N(\tilde x)e_0$ | the square of the block |
| $N(\tilde x)=x_0^{2}+|\mathbf x|^{2}$ | the definite quaternion form, the coefficient of the square |
| $Sp(1)=\{\tilde x:N(\tilde x)=1\}$ | the unit quaternions, the root set of $+e_0$ |
| $\lambda e_0$ | a central value; its roots are $\{N=\lambda\}$ for $\lambda>0$ |
| $\tilde\Pi=\tfrac12(e_0+\tilde x)$ | the affine map from a root of $+e_0$ to a candidate idempotent |

## Further Reading

- *Introduction to the Symmetric Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the square and the governing formula
- *Definitions for the Study of the 6 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-6-algebraic-structures.md`), for the root of a central value
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra-of-quaternions.md`), for the plain-algebra roots
- *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-symmetric-quaternionic-algebra.md`), for the biquaternion counterpart
- *The Specificities of the Symmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the idempotents and the nilpotents of the block
- *Quaternion Topology* (`articles_maths/quaternion-topology.md`), for the level set $\{N=1\}$ and its reading in the topological half
