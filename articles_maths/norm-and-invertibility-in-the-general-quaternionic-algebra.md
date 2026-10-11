# __Norm and Invertibility in the General Quaternionic Algebra__

## Introduction

This article studies the **algebraic norm** of the biquaternion algebra read through the general quaternionic bilinear product, and it settles what invertibility means for that product.

A norm is relative to a product, and the algebraic norm of a product is the diagonal of its scalar-part form, the definition of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*. For the general quaternionic product the square of every element is scalar, so the scalar-part form is read directly off the square and its diagonal is the scalar that the square produces. That scalar is the quadratic form $N(\tilde Q)=\sum_\mu Q_\mu^{2}$, the algebraic norm of this product and not the algebraic norm of the plain product, which is a different form on the same space; and it is multiplicative for $\star$.

The inverse is where the two products separate. The definition of an inverse, stated once in *Definitions for the Study of the 12 Algebraic Structures*, §*The Unit and the Inverse*, presupposes a product with a **two-sided unit**, and the general quaternionic product has a **left unit** alone. The consequence is stated and not filled: no element of $\mathbb{B}$ is invertible of $\star$, the product has no group of units of its own, and the word has no reading for it. What survives is the pair of one-sided inverse equations relative to the left unit $e_0$, and the article computes them: the two have the same unique solution, $(\tilde P^{-1})^{\natural}$, exactly when the norm is non-zero, and neither has a solution when the norm vanishes. The criterion is therefore the algebraic norm of this product, and it is not the algebraic norm of the plain product; the two products do not share their algebraic norms.

**Boundaries.** The algebraic norm of the plain product is $B(\tilde Q)=\sum_\mu\varepsilon_\mu Q_\mu^{2}$, a different form, and its theory is *Norm and Invertibility in the General Plain Algebra*; the algebraic norm $N$ is the one of this product, and the criterion $N\neq0$ is proved here. The zero divisors are *Zero Divisors of the General Quaternionic Algebra*, where the set $\{N=0\}\setminus\{0\}$ is characterised as a set; the one-sided inverse equations of the four general products side by side, and the tabulation of their solutions, are *The Zero Divisors and the Four General Products*, §*The One-Sided Inverse Equations*, whose table is quoted and not restated. The product and its element theory are *Introduction to the General Quaternionic Algebra of Biquaternions*; the left multiplications and the monoid they form are *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*; and the signatures of the norm on the remarkable subspaces are *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$, with $e_1e_2=e_3$ and central scalar imaginary $i$, $i^2=-1$. Juxtaposition is the plain product $\tilde P\tilde Q$, and the product of this article is the general quaternionic bilinear product

$$
\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q ,
$$

with $\natural$ the natural conjugation $\tilde Q^{\natural}=Q_0-\mathbf Q$ and $\mathbf Q=\sum_{k=1}^{3}Q_ke_k$ the vector part. An element is $\tilde Q=Q_0e_0+\mathbf Q$, and $(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$ is the complex bilinear form of the vector parts.

## The Algebraic Norm of the Product

### Definition

The algebraic norm of a product is the diagonal of its scalar-part form (*The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*).

**Definition.** Let $\star$ be a product on $\mathbb{B}$ and let $\varphi(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\star\tilde Q)$ be its scalar-part form. The **algebraic norm of $\star$** is the diagonal

$$
\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q)=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr).
$$

Throughout this article the product is the general quaternionic bilinear product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$, whose square is central, so that the algebraic norm is the scalar coefficient of the square; it means the algebraic norm of that product.

**Proposition.** For every $\tilde Q\in\mathbb{B}$,

$$
\tilde Q\star\tilde Q=\tilde Q^{\natural}\tilde Q=N(\tilde Q)\,e_0 , \qquad N(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^2=Q_0^2+(\mathbf Q,\mathbf Q) .
$$

**Proof.** The first display is the definition of the product at equal arguments; the scalar–vector form of *Introduction to the General Quaternionic Algebra of Biquaternions* gives $\tilde Q^{\natural}\tilde Q=(Q_0-\mathbf Q)(Q_0+\mathbf Q)=Q_0^2-\mathbf Q^2$, and $\mathbf Q^2=-(\mathbf Q,\mathbf Q)$ for a vector part. The same scalar is produced in the two orders, $\tilde Q^{\natural}\tilde Q=\tilde Q\tilde Q^{\natural}$, because the computation read the other way, $(Q_0+\mathbf Q)(Q_0-\mathbf Q)=Q_0^2-\mathbf Q^2$, gives the same value.

The norm is therefore an element of $\mathbb{C}$ and not a length: it is the value of a quadratic form on the complex space $\mathbb{B}$, and its vanishing set is a cone and not a sphere.

### The Polarisation

**Proposition.** The polar form of the norm is the scalar coefficient of the symmetrised product. Writing

$$
N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q) ,
$$

one has

$$
N(\tilde P+\tilde Q)-N(\tilde P)-N(\tilde Q)=2N(\tilde P,\tilde Q) , \qquad
\tilde P\star\tilde Q+\tilde Q\star\tilde P=2N(\tilde P,\tilde Q)\,e_0 .
$$

**Proof.** The scalar–vector form of $\tilde P+\tilde Q$ gives $N(\tilde P+\tilde Q)=N(\tilde P)+N(\tilde Q)+2N(\tilde P,\tilde Q)$; and $\tilde P\star\tilde Q+\tilde Q\star\tilde P=(\tilde P^{\natural}\tilde Q)+(\tilde P^{\natural}\tilde Q)^{\natural}$ has scalar part twice $\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=N(\tilde P,\tilde Q)$ and vanishing vector part, by the symmetry computation of the introduction.

The symmetric half read as an operation, with its centrality, its coefficient on the remarkable subspaces and its Jordan reading, is *The Symmetrised Quaternionic Product and the Hermitian Subspace*, which owns the symmetrisation; the proposition above is the same statement read as the polarisation of the quadratic form of the norm.

### Multiplicativity

**Proposition.** The algebraic norm is multiplicative for the product,

$$
N(\tilde P\star\tilde Q)=N(\tilde P)\,N(\tilde Q) ,
$$

and it is invariant under the natural conjugation, $N(\tilde P^{\natural})=N(\tilde P)$.

**Proof.** Since $\natural$ is an anti-automorphism and an involution, $(\tilde P^{\natural}\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P^{\natural\natural}=\tilde Q^{\natural}\tilde P$, so

$$
N(\tilde P\star\tilde Q)=(\tilde P^{\natural}\tilde Q)^{\natural}(\tilde P^{\natural}\tilde Q)=\tilde Q^{\natural}\tilde P\tilde P^{\natural}\tilde Q=\tilde Q^{\natural}N(\tilde P)\tilde Q=N(\tilde P)\,\tilde Q^{\natural}\tilde Q=N(\tilde P)\,N(\tilde Q) ,
$$

using that $N(\tilde P)$ is central. For the invariance, $N(\tilde P^{\natural})=\tilde P^{\natural}(\tilde P^{\natural})^{\natural}=\tilde P^{\natural}\tilde P=N(\tilde P)$.

The multiplicativity is the law of the algebraic norm of this product, and it is the reason this product is the one that carries the multiplicative quadratic form of the space; the plain product carries a different algebraic norm, $B$, which is not multiplicative.

**Corollary.** The vanishing set of the norm is stable under the product: if $N(\tilde Q)=0$ then $N(\tilde P\star\tilde Q)=0$ for every $\tilde P$, and the same with the factors exchanged.

## The Unit and the Absence of the Inverse

**Definition.** Let $\star$ be a product on $\mathbb{B}$. An element $e$ is a **left unit of $\star$** when $e\star x=x$ for every $x$, a **right unit** when $x\star e=x$ for every $x$, and a **two-sided unit**, or **identity**, when it is both; and if $\star$ has a two-sided unit $e$, an element $x$ is **invertible of $\star$** when there is a $y$ with $x\star y=y\star x=e$. The definitions are *Definitions for the Study of the 12 Algebraic Structures*, §*The Unit and the Inverse*, and they name the product at every step.

The unit of the general quaternionic product is settled in *Introduction to the General Quaternionic Algebra of Biquaternions*, and it is recalled here because the inverse depends on it.

**Proposition (the unit).** The element $e_0$ is a left unit of $\star$ and the only one; there is no right unit; hence there is no two-sided unit.

**Proof.** $e_0\star\tilde Q=e_0^{\natural}\tilde Q=e_0\tilde Q=\tilde Q$, and a left unit $\tilde E$ reads $\tilde E^{\natural}=e_0$ at $\tilde Q=e_0$, whence $\tilde E=e_0$. The equation $\tilde P\star\tilde E=\tilde P$ at $\tilde P=e_0$ forces $\tilde E=e_0$, and at $\tilde P=e_1$ reads $e_1\star e_0=-e_1\neq e_1$; so there is no right unit.

**Absence (the inverse).** The quaternionic product has no two-sided unit, so the definition of the inverse has no reading for it: **no element of $\mathbb{B}$ is invertible of $\star$**, and the product has no group of units. What the article computes in the next section is the pair of one-sided equations relative to the left unit $e_0$; it is not an inverse theory of the product, and it is never called one.

## The One-Sided Inverse Equations

Relative to a left unit $e_0$ the two halves of the inverse equation remain meaningful, and they are the definition of the one-sided invertibility of the product.

**Definition.** Let $\tilde P\in\mathbb{B}$. An element $\tilde R$ with $\tilde P\star\tilde R=e_0$ is a **right inverse** of $\tilde P$ relative to $e_0$, and an element $\tilde L$ with $\tilde L\star\tilde P=e_0$ is a **left inverse** of $\tilde P$ relative to $e_0$. The element $\tilde P$ is **right-invertible** when it has a right inverse and **left-invertible** when it has a left inverse.

**Theorem (the one-sided equations).** For every $\tilde P\in\mathbb{B}$ the two equations

$$
\tilde P\star\tilde X=e_0 , \qquad \tilde X\star\tilde P=e_0
$$

have a solution exactly when $N(\tilde P)\neq0$, and then each has the **same unique** solution,

$$
\tilde X=(\tilde P^{-1})^{\natural}=\frac{\tilde P^{\natural\natural}}{N(\tilde P^{\natural})}=\frac{\tilde P}{N(\tilde P)} ,
$$

where $\tilde P^{-1}=\tilde P^{\natural}/N(\tilde P)$ is the inverse of the plain product. When $N(\tilde P)=0$ neither equation has a solution.

**Proof.** The first equation is $\tilde P^{\natural}\tilde X=e_0$, a plain-product equation with the fixed right-hand side $e_0$; composing on the left with the plain inverse of $\tilde P^{\natural}$, legitimate exactly when that element is invertible, gives $\tilde X=(\tilde P^{\natural})^{-1}$. The plain algebra is associative, so the solution is unique when it exists. Now $\tilde P^{\natural}$ is a unit of the plain product exactly when $N(\tilde P^{\natural})\neq0$, that is exactly when $N(\tilde P)\neq0$, and its inverse is $(\tilde P^{\natural})^{-1}=(\tilde P^{\natural})^{\natural}/N(\tilde P^{\natural})=\tilde P/N(\tilde P)=(\tilde P^{-1})^{\natural}$. This proves the statement for the first equation. For the second, $\tilde X\star\tilde P=\tilde X^{\natural}\tilde P=e_0$; composing on the right with the plain inverse of $\tilde P$ gives $\tilde X^{\natural}=\tilde P^{-1}$, hence $\tilde X=(\tilde P^{-1})^{\natural}$, the same element, and the same invertibility condition. If $N(\tilde P)=0$ and $\tilde P\neq0$ then $\tilde P^{\natural}$ is a zero divisor of the plain product, so the equation $\tilde P^{\natural}\tilde X=e_0$ has no solution; and if $\tilde P=0$ the equations read $0=e_0$, also with no solution.

**Remark.** The common solution is the natural conjugate of the plain inverse, and not the plain inverse itself. The coincidence of the two one-sided solutions, and the fact that they are given by the plain inverse of the conjugated element, are the whole content of the table of *The Zero Divisors and the Four General Products* §*The One-Sided Inverse Equations* read on this product; the table is quoted there and the computation is the one above.

**Corollary.** The element $\tilde P$ is left-invertible and right-invertible relative to $e_0$ exactly when $N(\tilde P)\neq0$, and then one and the same element, $(\tilde P^{-1})^{\natural}$, serves as both a left inverse and a right inverse:

$$
\tilde P\star(\tilde P^{-1})^{\natural}=e_0=(\tilde P^{-1})^{\natural}\star\tilde P .
$$

**Proof.** The theorem gives the two solutions and they are equal. The displayed identity is the theorem at that element, using $\tilde P\star\tilde R=\tilde P^{\natural}(\tilde P^{-1})^{\natural}=(\tilde P^{-1}\tilde P)^{\natural}=e_0$ and $(\tilde P^{-1})^{\natural}\star\tilde P=(\tilde P^{-1})^{\natural\natural}\tilde P=\tilde P^{-1}\tilde P=e_0$.

The corollary is a statement about the left unit $e_0$ and not an inverse of the product, because the product has no right unit: the equation it solves uses $e_0$ on the right, where $e_0$ is not a right unit, so the solution is a one-sided object of each equation and not an inverse in the sense of *Definitions for the Study of the 12 Algebraic Structures*.

## The Criterion

**Theorem (the criterion for the general quaternionic product).** For a nonzero $\tilde P\in\mathbb{B}$ the following are equivalent:

1. $N(\tilde P)\neq0$;
2. the plain-product equation $\tilde P\tilde X=e_0$ has a solution, namely $\tilde X=\tilde P^{-1}=\tilde P^{\natural}/N(\tilde P)$;
3. the two one-sided equations of §*The One-Sided Inverse Equations* have a solution.

They are equivalent to the single negative statement that $\tilde P$ is a zero divisor of the algebra if and only if $N(\tilde P)=0$.

**Proof.** The equivalence of (1) and (2) is the statement that the scalar $\tilde P^{\natural}\tilde P=N(\tilde P)e_0$ is nonzero exactly when $\tilde P$ is not a zero divisor of the plain product, which is the zero-divisor criterion of *Zero Divisors of the General Quaternionic Algebra*. The equivalence of (1) and (3) is the theorem of the preceding section. For the last clause, $\tilde P\neq0$ with $N(\tilde P)=0$ is a zero divisor of the algebra, and conversely (*Zero Divisors of the General Quaternionic Algebra*).

The criterion is expressed by the algebraic norm $N$ of this product, because the vanishing set of $N$ is the zero-divisor set; it is not expressible by the algebraic norm of the plain product, which is $B$ and does not decide invertibility (*Norm and Invertibility in the General Plain Algebra*).

## The Three-Way Classification

The elements of $\mathbb{B}$ fall into three classes according to the value of the norm, and the classes are the ones of the plain algebra with the inverse column replaced by the one-sided column.

| condition on $N(\tilde P)$ | condition on $\tilde P$ | under the plain product | under the quaternionic product |
|---|---|---|---|
| $N(\tilde P)\neq0$ | none | a unit | the one-sided equations soluble, with the common solution $(\tilde P^{-1})^{\natural}$ |
| $N(\tilde P)=0$ | $\tilde P=0$ | the zero element | the zero element |
| $N(\tilde P)=0$ | $\tilde P\neq0$ | a zero divisor | a zero divisor, with neither one-sided equation soluble |

The classification is a classification of the elements by their behaviour in the two products, and the middle column is quoted from *Zero Divisors of the General Quaternionic Algebra*; the third column is this article.

## The Group of Units, and Why There Is None

Let $\mathbb{B}^{\times}=\{\tilde P:N(\tilde P)\neq0\}$ be the set of the elements on which the norm does not vanish.

**Proposition.** The set $\mathbb{B}^{\times}$ is the group of units of the plain product, it contains $e_0$, and it is stable under the quaternionic product. It is **not** a group under $\star$: the product has no two-sided unit and it is not associative, so $\mathbb{B}^{\times}$ with $\star$ is a set with a left unit in which every left translation is a bijection, and nothing more.

**Proof.** The first clause is the plain invertibility criterion. Stability under $\star$ is the multiplicativity of the norm: $N(\tilde P\star\tilde Q)=N(\tilde P)N(\tilde Q)\neq0$. The absence of a two-sided unit is §*The Unit and the Absence of the Inverse*, and the failure of associativity is *Introduction to the General Quaternionic Algebra of Biquaternions*; a group requires both, so there is none. Finally, the left translation $\tilde X\mapsto\tilde P\star\tilde X=L^{\mathrm{plain}}_{\tilde P^{\natural}}(\tilde X)$ is a plain left multiplication by a unit and is therefore a bijection, and the same holds on the right by the multiplicativity read in the other order.

**Corollary (the group of the left multiplications).** The left multiplications $L_{\tilde P}$ with $\tilde P\in\mathbb{B}^{\times}$ are the invertible left multiplications of the product; they form a group under composition, and the map $\tilde P\mapsto L_{\tilde P}$ is an anti-isomorphism of $\mathbb{B}^{\times}$ onto it. The monoid law $L_{\tilde P}L_{\tilde R}=L_{\tilde R\tilde P}$ and the failure of the right family are *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*.

**Proof.** $L_{\tilde P}=L^{\mathrm{plain}}_{\tilde P^{\natural}}$ is invertible exactly when $\tilde P^{\natural}$, hence $\tilde P$, is a plain unit; the composition law is the one cited, and it reverses the order, so the map is an anti-isomorphism onto its image, which is stable under composition and inversion.

This is the precise sense in which the product "has a group of units" only on the operator side. The set $\mathbb{B}^{\times}$ carries the inverse of the plain product, and it is the index set of the invertible operators; the product $\star$ does not make it a group.

## The Algebraic Norm on the Remarkable Subspaces

The algebraic norm is the quadratic form of the algebra, so its restriction to the remarkable subspaces is a form with a signature, and the sign decides which subspaces carry elements of algebraic norm zero. The signatures are computed in *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions* and are quoted here.

| remarkable subspace | signature of $N$ | elements of norm zero |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | $(1,1)$ | $0$ alone |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | $(3,3)$ | the isotropic cone of the vector subspace |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | $(4,0)$ | $0$ alone |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | $(0,4)$ | $0$ alone |
| $\mathbb{M}_{+}$, the Hermitian subspace | $(1,3)$ | the isotropic cone of $\mathbb{M}_{+}$, all of it non-pure |
| $\mathbb{M}_{-}$, the anti-Hermitian subspace | $(3,1)$ | the isotropic cone of $\mathbb{M}_{-}$, all of it non-pure |

**Corollary.** Every nonzero element of the quaternion subspace and of the anti-quaternion subspace is a unit of the plain product and satisfies both one-sided equations of $\star$. The other four subspaces contain nonzero elements of norm zero; on those the criterion fails and neither one-sided equation is soluble, and they are zero divisors of the algebra.

**Proof.** The norm is definite on the quaternion and the anti-quaternion subspaces and indefinite on the other four, by the table; the criterion of §*The Criterion* converts the values into the two statements. On a pure element the norm is $(\mathbf P,\mathbf P)$ and on a Hermitian element it is $|a_0|^2-|\mathbf b|^2$ in the coordinates of the subspace, so every zero of the norm in $\mathbb{M}_{+}$ or in $\mathbb{M}_{-}$ has non-zero scalar part, that is, is non-pure.

## Summary

The general quaternionic bilinear product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ has a central square, $\tilde Q\star\tilde Q=N(\tilde Q)e_0$ with $N(\tilde Q)=\sum_\mu Q_\mu^2=Q_0^2+(\mathbf Q,\mathbf Q)$, and this scalar is the **algebraic norm** of the product, with polar form the scalar coefficient $N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ of the symmetrised product and with the multiplicative law $N(\tilde P\star\tilde Q)=N(\tilde P)N(\tilde Q)$.

The product has the left unit $e_0$ and no right one, hence no two-sided unit, and the definition of the inverse, which requires one, applies to no element: **there is no invertible element and no group of units of the quaternionic product**. What survives is the pair of one-sided equations relative to $e_0$: both have the same unique solution, $(\tilde P^{-1})^{\natural}=\tilde P/N(\tilde P)$, exactly when $N(\tilde P)\neq0$, and neither has a solution when $N(\tilde P)=0$. The criterion is thus the norm, as for the plain product, and the elements of non-vanishing norm form the plain group of units $\mathbb{B}^{\times}$, stable under $\star$ and carrying the invertible left multiplications, without being a group of the product. On the quaternion and the anti-quaternion subspaces the norm is definite and every nonzero element is a unit of the plain product; on the centre, the vector, the Hermitian and the anti-Hermitian subspaces it is indefinite and they carry the zero divisors.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $e_0,e_1,e_2,e_3$ | the basis, $e_0$ the identity, $e_k$ the quaternion units |
| $\tilde Q=Q_0e_0+\mathbf Q$ | an element and its scalar–vector split |
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ | the general quaternionic bilinear product |
| $N(\tilde Q)=\sum_\mu Q_\mu^2$ | the algebraic norm of the product, the scalar of the square, $\tilde Q\star\tilde Q=N(\tilde Q)e_0$ |
| $N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ | the polar form of the algebraic norm |
| $e_0$ | the left unit of $\star$; there is no right unit, hence no two-sided one |
| $\tilde P^{-1}=\tilde P^{\natural}/N(\tilde P)$ | the inverse of the plain product |
| $(\tilde P^{-1})^{\natural}$ | the common solution of the two one-sided equations of $\star$ |
| $\mathbb{B}^{\times}=\{N\neq0\}$ | the plain group of units, stable under $\star$ |
| $\mathbb{C}_{\mathbb{B}},\mathrm{Vect}(\mathbb{B}),\mathbb{H}_{\mathbb{B}},i\mathbb{H}_{\mathbb{B}},\mathbb{M}_{+},\mathbb{M}_{-}$ | the remarkable subspaces |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the norm and the one-sided inverses of a non-associative algebra.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for a quadratic form defined by a product and the polarisation of its multiplicative law.
- *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternion-c-space.md`), for the definition of the algebraic norm as the diagonal of a form and the separation of the four algebraic norms.
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra.md`), for the algebraic norm $B$ of the plain product, which is not the form $N$ of this article.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Unit and the Inverse*, for the definitions of the unit, the two-sided inverse and the one-sided inverse.
- *Zero Divisors of the General Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-general-quaternionic-algebra.md`), for the set $\{N=0\}\setminus\{0\}$, its criterion and its annihilators.
- *The Zero Divisors and the Four General Products* (`articles_maths/the-zero-divisors-and-the-four-general-products.md`), for the one-sided inverse equations of the four general products tabulated side by side.
- *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* (`articles_maths/the-left-multiplications-of-the-quaternionic-product-and-the-opposite-monoid.md`), for the monoid law of the left multiplications and the group of its invertible elements.
- *Remarkable Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), for the signatures of the norm on the six subspaces.
