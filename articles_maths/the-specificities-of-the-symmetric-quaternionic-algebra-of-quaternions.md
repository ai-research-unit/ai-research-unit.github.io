# __The Specificities of the Symmetric Quaternionic Algebra__

## Introduction

This article collects the properties that single the symmetric quaternionic algebra out among the six structures of *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*: the centrality of its values, its commutativity, the definiteness of its coefficient, the absence of a unit and hence of an inverse, its idempotents, its nilpotents, and its isolation. The properties are not new computations; each is the governing formula $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$ of *Introduction to the Symmetric Quaternionic Algebra of Quaternions* read for one class of element, and each class is defined in *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*. The article is the Common Theory companion of *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*, below this article in this category, which reads the same formula through the radical and the isotropic elements.

**Boundaries.** The product and its laws are *Introduction to the Symmetric Quaternionic Algebra of Quaternions*; the zero divisors are *Zero Divisors of the Symmetric Quaternionic Algebra*, above this article in this category; the roots of a central value are *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra* and *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra*, above this article in this category; the definitions are *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*; the form and its definiteness are *The 2 Forms over the Quaternion $\mathbb{R}$ Space*.

**Conventions.** The algebra is $\mathbb{H}$ over $\mathbb{R}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$; an element is $\tilde x=x_0e_0+\vec x$ with $\vec x=\sum_kx_ke_k$. The **quaternion conjugation** is $\tilde x^{\natural}=x_0e_0-\vec x$; the bar is the identity, the star coincides with the natural sign ${}^{\natural}$. The **quaternion form** is $N(\tilde p,\tilde q)=p_0q_0+\vec p\cdot\vec q$ and $N(\tilde x)=N(\tilde x,\tilde x)=x_0^{2}+|\vec x|^{2}$; the **symmetric quaternionic product** is $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$.

## The Scalar Law

**Theorem (the values are central and the block is commutative).** Every value of the block lies in the scalar line $\mathbb{R}e_0$, the operation is commutative and $\mathbb{R}$-bilinear, and it satisfies

$$
\tilde p\star\tilde q=\tilde q\star\tilde p,\qquad
[\tilde p,\tilde q]_{\star}=\tilde p\star\tilde q-\tilde q\star\tilde p=0 .
$$

*Proof.* The value is $N(\tilde p,\tilde q)e_0$ by the governing formula, and the form is symmetric; the commutator vanishes by the symmetry.

**Remark (the parent is reconstructed from the block and its companion).** The parent general quaternionic product is $\tilde p^{\natural}\tilde q=\tilde p\star\tilde q+\tfrac12[\tilde p,\tilde q]_{\natural}$, where $[\tilde p,\tilde q]_{\natural}=\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p$ is the companion block $\mathrm{AQA}$. The block is the symmetric half of the quaternionic row, and its centrality is the collapse of the parent's scalar part; the antisymmetric half carries the vector part and the Lie structure that the block does not have.

## The Definite Character

**Theorem (definiteness).** The coefficient of the block is positive definite:

$$
N(\tilde x,\tilde x)=x_0^{2}+|\vec x|^{2}\geq0,\qquad N(\tilde x,\tilde x)=0\iff\tilde x=0 .
$$

Equivalently, the form is anisotropic: it has no nonzero isotropic element, and its radical is $\{0\}$.

*Proof.* The form is a sum of four squares, which is nonnegative and vanishes only when every coordinate does; an element with $N(\tilde x,\tilde x)=0$ is therefore $0$, and the radical, being contained in the isotropic set, is $\{0\}$.

**Corollary (every square is nonnegative).** For every $\tilde x$, the square is $\tilde x\star\tilde x=N(\tilde x)e_0\geq0$, so no element squares to a negative central value; in particular the equation $\tilde x\star\tilde x=-e_0$ has no solution.

*Proof.* Immediate from the theorem and the square formula of *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra*, above this article in this category.

**Remark (definiteness against the parent).** The parent product $\tilde p^{\natural}\tilde q$ has the same coefficient $N$ on the diagonal, but the parent is not scalar valued and its diagonal is not its only quadratic invariant; the block is the one place where the definite form *is* the whole product.

## The Absence of a Unit

**Theorem (there is no unit).** The block has no unit and no one-sided unit; consequently no element has an inverse, and the block is not a division algebra in the unital sense.

*Proof.* An element $\tilde u$ with $\tilde u\star\tilde q=\tilde q$ for every $\tilde q$ would give at $\tilde q=e_0$ the value $\tilde u\star e_0=u_0e_0=e_0$, so $u_0=1$, and then at $\tilde q=e_1$ the value $\tilde u\star e_1=u_1e_0=e_1$, impossible because $u_1e_0$ is scalar. The same computation with the roles exchanged excludes a right unit, and an element invertible from both sides would be a unit. This is *Introduction to the Symmetric Quaternionic Algebra of Quaternions*, restated here as a specificity.

**Remark (the contrast with the symmetric plain block).** The other commutative structure, the symmetric plain algebra, is unital with unit $e_0$: $e_0\bullet\tilde q=\tilde q$. The two blocks differ exactly at the unit, and this is why the zero divisors and the inverses behave oppositely in them; the zero-divisor comparison is *Zero Divisors of the Symmetric Quaternionic Algebra*, above this article in this category.

## The Idempotents

**Theorem (the idempotents).** An element $\tilde x$ satisfies $\tilde x\star\tilde x=\tilde x$ if and only if $\tilde x\in\{0,e_0\}$.

*Proof.* The square is $N(\tilde x)e_0=(x_0^{2}+|\vec x|^{2})e_0$, while $\tilde x=x_0e_0+\vec x$; equality forces the vector part of $\tilde x$ to vanish, $\vec x=0$, and then $x_0^{2}=x_0$, whose solutions are $x_0=0$ and $x_0=1$. So the idempotents are $0$ and $e_0$.

**Remark (the idempotents are the central ones, and only those).** The block has no idempotent in the vector subspace and none off the centre; the reduction $\vec x=0$ in the proof is the entire restriction of the block to the diagonal of the quaternionic row. The companion plain block has the same two idempotents but reaches them with a different computation (*The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*).

## The Nilpotents and the Square-Zero Elements

A **nilpotent** of the block is an element some left-nested power of which vanishes, and a **square-zero** element is one of index two (*Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*). The powers of the block are governed by one formula.

**Theorem (the powers).** For every $\tilde x$ and every $k\geq2$,

$$
\tilde x^{\star k}=N(\tilde x)\,x_0^{\,k-2}\,e_0 .
$$

*Proof.* For $k=2$ this is the square. If it holds at $k$, then $\tilde x^{\star(k+1)}=\tilde x^{\star k}\star\tilde x=N(\tilde x)x_0^{k-2}e_0\star\tilde x=N(\tilde x)x_0^{k-2}\cdot x_0e_0=N(\tilde x)x_0^{k-1}e_0$, the formula at $k+1$.

**Theorem (the nilpotents and their index).** An element $\tilde x$ is a nilpotent of the block if and only if $\tilde x$ is pure, that is $x_0=0$; and every nonzero pure element has index three. The only element whose square vanishes is $0$.

*Proof.* By the powers formula, $\tilde x^{\star3}=N(\tilde x)x_0e_0$. If $x_0=0$ then the cube vanishes; a pure nonzero element has $N(\tilde x)=|\vec x|^{2}\neq0$, so its square is $N(\tilde x)e_0\neq0$ and it is not square-zero, and its index is exactly three. If $x_0\neq0$, then $N(\tilde x)x_0\neq0$, because $N(\tilde x)\geq|x_0|^{2}>0$, so the cube is nonzero and, by the formula, every higher power is nonzero; the element is not nilpotent. The square vanishes only when $N(\tilde x)=0$, that is only at $\tilde x=0$, by definiteness.

**Corollary (the two classes).** The nilpotent set of the block is the vector subspace,

$$
\{\text{nilpotents}\}=\{\tilde x:x_0=0\}=\operatorname{Im}\mathbb{H}=\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3,
$$

and the square-zero set is $\{0\}$: over $\mathbb{R}$ the block has no nonzero square-zero element.

Over $\mathbb{R}$ the isotropic family of the coefficient collapses to the origin, so only the pure family survives, and the block's nilpotents are exactly the pure quaternions. The menu comment's phrase that the nilpotents "reduce to $0$" describes instead the square-zero class, which over $\mathbb{R}$ is only $\{0\}$; the nilpotent class is the whole vector subspace, and the distinction is recorded in the context of this article.

**Remark (the meeting of the two classes).** The idempotents $\{0,e_0\}$ and the nilpotents $\operatorname{Im}\mathbb{H}$ meet only at the origin, and the square-zero elements are the origin alone; the three classes overlap only at $0$.

## The Isolation among the Six

**Theorem (the scalar row).** Among the six structures of *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, the symmetric quaternionic structure is the only one whose values all lie in the central line $\mathbb{R}e_0$; equivalently, it is the only operation of the six that is a pairing $\mathbb{H}\times\mathbb{H}\to Z(\mathbb{H})$ placed on the centre.

*Proof.* Read the six products on one noncentral pair each: the general plain product has $e_1e_2=e_3$, the symmetric plain product has $e_0\bullet e_1=e_1$, the antisymmetric plain product has $e_1\bullet e_2=e_3$, the general quaternionic product has $e_0^{\natural}e_1=e_1$, and the antisymmetric quaternionic product has $\tfrac12(e_0^{\natural}e_1-e_1^{\natural}e_0)=e_1$. Each value is noncentral, so none of the five has all its values in the central line. The symmetric quaternionic product has $e_\mu\star e_\nu=\delta_{\mu\nu}e_0$ on the basis, and by bilinearity all its values are scalar. The six rows of *The 6 Products of the Quaternion Real Space* are thereby exhausted.

**Corollary (the isolation).** The block is the unique structure of the six that is commutative and scalar valued; it is also the unique structure of the six whose square, $\tilde x\star\tilde x=N(\tilde x)e_0$, is a scalar quadratic form. It is nevertheless the only commutative structure of the six without a unit; the other commutative structure, the symmetric plain algebra, has the unit $e_0$.

*Proof.* The first two clauses are the theorem; the third is the comparison of *The Absence of a Unit* with the symmetric plain block.

## Summary

The symmetric quaternionic block is commutative with central values $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$; its coefficient is the positive definite quaternion form, anisotropic with radical $\{0\}$, so every square is a nonnegative multiple of $e_0$ and none vanishes off the origin. The block has no unit, no one-sided unit and no inverse; its idempotents are exactly $0$ and $e_0$; its powers obey $\tilde x^{\star k}=N(\tilde x)x_0^{k-2}e_0$, so its nilpotents are the pure quaternions, each nonzero one of index three, and its only square-zero element is $0$. Among the six structures it is the unique one with central values and the unique commutative one whose square is a scalar form, and the unique commutative one without a unit.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$ | the product; values in the scalar line |
| $N(\tilde x)=x_0^{2}+|\vec x|^{2}$ | the definite coefficient; anisotropic, radical $\{0\}$ |
| $\{0,e_0\}$ | the idempotents |
| $\operatorname{Im}\mathbb{H}=\{\tilde x:x_0=0\}$ | the nilpotents; each nonzero one has index three |
| $\{0\}$ | the square-zero elements |
| $\tilde x^{\star k}=N(\tilde x)x_0^{k-2}e_0$ | the powers, $k\geq2$ |

## Further Reading

- *Introduction to the Symmetric Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the product and its laws
- *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternion-r-space.md`), for the unit, the inverse, the idempotent and the nilpotent
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-quaternionic-algebra-of-quaternions.md`) and *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the classes read with the same formula
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the radical, the isotropic elements and the positivity
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* (`articles_maths/the-square-the-idempotents-and-the-jordan-inverse-of-the-symmetric-plain-algebra-of-quaternions.md`), for the comparison with the other commutative block
