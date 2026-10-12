# __Nilpotents of the Symmetric Quaternionic Algebra__

## Introduction

A nilpotent of a product is an element some power of which vanishes, the index being the least such power, and a square-zero element is one of index two (*Definitions for the Study of the 12 Algebraic Structures* §*The Nilpotent*). In the symmetric quaternionic block the powers of an element are central from the square on, and one formula governs all of them:

$$
\tilde\Upsilon^{\star k}=N(\tilde\Upsilon)\,\Upsilon_0^{\,k-2}\,e_0\qquad(k\geq2),
$$

the powers being read in the left-nested sense. The block is therefore one of the products of the twelve whose nilpotent index is not bounded by two: its nilpotents have index two or index three, and the two families are a cone and a vector subspace. This article computes the powers, states the criterion, separates the two index classes, computes the square-zero set, relates the nilpotents to the zero divisors and to the idempotents, records the behaviour under the three conjugations, and reads the whole in the $2\times2$ matrix model.

**Boundaries.** The general definition of the nilpotent and of the square-zero element is the definitions article; the square-zero elements of the four general products and their comparison are *Zero Divisors* and *Comparison Between the Four General Products*; the zero divisors are *Zero Divisors of the Symmetric Quaternionic Algebra*; the idempotents are *Idempotents of the Symmetric Quaternionic Algebra*; the roots of $0$ are *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra*; the matrix models are *The Symmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* and its $4\times4$ companion.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, and central scalar imaginary $i$; a general element is $\tilde Q=Q_0e_0+\mathbf Q$ with $(\mathbf P,\mathbf Q)=\sum_{k=1}^{3}P_kQ_k$. The **symmetric quaternionic multiplication** is $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ with $N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ and diagonal $N(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^2$; it is also written $\bullet$. The centre is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ and the vector subspace is $\mathrm{Vect}(\mathbb{B})=\mathbb{C}e_1+\mathbb{C}e_2+\mathbb{C}e_3$.

## The General Definition

**Definition (nilpotent of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Upsilon$ is **nilpotent of $\star$** when

$$
\tilde\Upsilon^{\star k}=0\quad\text{for some }k\geq1,
$$

the power being the left-nested one when $\star$ is not associative; the least such $k$ is the **index of nilpotency**, and an element of index two, $\tilde\Upsilon\star\tilde\Upsilon=0$ with $\tilde\Upsilon\neq0$, is a **square-zero element**.

Throughout this article the product is the **symmetric quaternionic product** of the block, and a nilpotent, an index or a square-zero element, written without qualification, is one of that product. The block is not associative, so the bracketing of a power matters a priori and is fixed to the left-nested reading; for this product the right-nested reading gives the same value, because $\tilde\Upsilon\star(\tilde\Upsilon\star\tilde\Upsilon)=\Upsilon_0N(\tilde\Upsilon)e_0$ by the same computation as below.

## The Powers of an Element

**Theorem (the powers).** For every $\tilde\Upsilon$ and every $k\geq2$,

$$
\tilde\Upsilon^{\star k}=N(\tilde\Upsilon)\,\Upsilon_0^{\,k-2}\,e_0=\Upsilon_0^{\,k-2}\bigl(\tilde\Upsilon\star\tilde\Upsilon\bigr).
$$

*Proof.* For $k=2$ the formula is $\tilde\Upsilon^{\star2}=N(\tilde\Upsilon)e_0$, the square of the block. Assume it for $k$; then $\tilde\Upsilon^{\star(k+1)}=\tilde\Upsilon^{\star k}\star\tilde\Upsilon=N(\tilde\Upsilon)\Upsilon_0^{k-2}e_0\star\tilde\Upsilon=N(\tilde\Upsilon)\Upsilon_0^{k-2}\cdot\Upsilon_0e_0=N(\tilde\Upsilon)\Upsilon_0^{k-1}e_0$, which is the formula at $k+1$; the displayed equality with $\Upsilon_0^{k-2}(\tilde\Upsilon\star\tilde\Upsilon)$ is the same computation reversed.

**Corollary (the index is at most three).** The index of nilpotency of a nilpotent of the block is two or three, and the higher powers vanish as soon as $N(\tilde\Upsilon)\Upsilon_0=0$.

*Proof.* The formula shows that $\tilde\Upsilon^{\star3}=N(\tilde\Upsilon)\Upsilon_0e_0$; if this vanishes then every later power vanishes by the formula, and if it does not vanish then no power vanishes, because $\Upsilon_0^{k-2}$ is a power of a nonzero scalar.

## The Criterion and the Index

**Theorem (the nilpotents and their index).** An element $\tilde\Upsilon$ is a nilpotent of the block if and only if

$$
N(\tilde\Upsilon)=0\quad\text{or}\quad\Upsilon_0=0,
$$

that is if and only if it is isotropic or pure. The index is two on the first family, the isotropic cone, and three on the pure non-isotropic family $\{\Upsilon_0=0,\ N\neq0\}$.

*Proof.* By the formula $\tilde\Upsilon^{\star3}=N(\tilde\Upsilon)\Upsilon_0e_0$, a nilpotent of index three satisfies $N(\tilde\Upsilon)\Upsilon_0=0$ with $\Upsilon_0\neq0$, hence $N=0$, which is already the index two case; so the index three case is $\Upsilon_0=0$ and $N\neq0$, where the cube is zero while the square is $N e_0\neq0$. Conversely if $N=0$ the square is zero (index two, if $\tilde\Upsilon\neq0$), and if $\Upsilon_0=0$ the cube is zero.

**Corollary (the nilpotent set).**

$$
\{\text{nilpotents of the block}\}=\{N=0\}\cup\mathbb{C}e_1+\mathbb{C}e_2+\mathbb{C}e_3,
$$

the union of the isotropic cone and the vector subspace, and the two meet in the pure isotropic elements, which are of index two. The set is the union of a quadric cone of complex dimension three and a linear subspace of complex dimension three.

## The Square-Zero Set

**Theorem (the square-zero elements are the isotropic elements).** The square-zero elements of the block are exactly the nonzero isotropic elements,

$$
\{\tilde\Upsilon:\tilde\Upsilon\star\tilde\Upsilon=0,\ \tilde\Upsilon\neq0\}=\{N=0\}\setminus\{0\},
$$

the punctured isotropic cone of complex dimension three and real dimension six, with the two families of *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*. They are exactly the roots of $0$ of the block and exactly the zero divisors of the parent algebra.

*Proof.* $\tilde\Upsilon\star\tilde\Upsilon=N(\tilde\Upsilon)e_0$ vanishes exactly when $N(\tilde\Upsilon)=0$, and $0$ is excluded by the definition; the identification with the roots of $0$ and with the zero divisors of the parent is *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra* and *Zero Divisors of the Symmetric Quaternionic Algebra*.

**Examples.** $\tilde\Upsilon=e_0+ie_1$: $N=0$, index two. $\tilde\Upsilon=e_1$: pure, $N=1$, index three, since $e_1\star e_1=e_0$ and $e_1\star e_0=0$. $\tilde\Upsilon=e_1+e_2$: pure, $N=2$, index three. $\tilde\Upsilon=e_0+e_1$: $N=2$ and $\Upsilon_0=1$, not a nilpotent.

## The Relation to the Zero Divisors and to the Idempotents

**Proposition (the nilpotents are zero divisors, and they are far from exhausting them).** Every nonzero nilpotent of the block is a zero divisor of it, since the block's zero-divisor set is the whole punctured space; conversely the non-isotropic, non-pure elements, for instance $e_0$, are zero divisors and not nilpotents. The implication *nilpotent implies zero divisor* therefore holds trivially in the block, and the converse fails in the sharpest possible way.

*Proof.* *Zero Divisors of the Symmetric Quaternionic Algebra* gives $\mathcal{Z}_{\star}=\mathbb{B}\setminus\{0\}$; the criterion above excludes $e_0$ from the nilpotents since $N(e_0)=1$ and its scalar part is $1$.

**Proposition (the nilpotents and the idempotents meet only at the origin).** The only element of the block that is both an idempotent and a nilpotent is $0$. The idempotent $e_0$ is not a nilpotent, all its powers being $e_0$, and the square-zero elements are not idempotents, since $\tilde\Upsilon\star\tilde\Upsilon=0$ and $\tilde\Upsilon\star\tilde\Upsilon=\tilde\Upsilon$ give $\tilde\Upsilon=0$.

*Proof.* The classification of the idempotents is *Idempotents of the Symmetric Quaternionic Algebra*, where they are shown to be $0$ and $e_0$; the two statements displayed are immediate.

**Remark (the two families the index separates).** The block's two nilpotent families are not the parent's two zero-divisor families. In the parent the nilpotents are the pure isotropic elements and the non-pure zero divisors are the idempotent multiples (*Zero Divisors of the General Plain Algebra*); in the block the index two family is the whole isotropic cone — pure or not — and the index three family is the pure anisotropic part of the vector subspace, which in the parent consists of units and of no zero divisor at all. The block thus produces nilpotents of an index the parent does not have, and it produces them on elements that the parent regards as regular.

## The Conjugations

**Theorem (the nilpotent set is invariant).** The three conjugations preserve the nilpotent set and its two index families:

$$
N(\tilde\Upsilon^{\natural})=N(\tilde\Upsilon),\qquad N(\tilde\Upsilon^{*})=\overline{N(\tilde\Upsilon)},\qquad
(\Upsilon^{\natural})_0=\Upsilon_0,\qquad (\Upsilon^{*})_0=\overline{\Upsilon_0},
$$

so $\Upsilon_0=0$ is preserved by ${}^{\natural}$ and by ${}^{*}$, and $N=0$ by ${}^{\natural}$ and by the Hermitian conjugation, while ${}^{*}$ preserves $N=0$ by conjugating the value.

*Proof.* The natural conjugation negates the vector part, the star conjugates all four coefficients and negates the vector part; the identities for $N$ are those of *Norm and Invertibility in the Symmetric Quaternionic Algebra*, and a vanishing scalar or form is preserved by the sign or conjugation of the value.

**Corollary.** The square-zero set and the vector subspace are each stable under the three conjugations, and the index of a nilpotent is unchanged by them.

## The Matrix Model

**Theorem (the two invariants of the model).** In the realization $M_2(\mathbb{C})$ of the algebra, the matrix of a general element is

$$
\mathsf M(\tilde Q)=\begin{pmatrix} Q_0-iQ_3 & -Q_2-iQ_1\\ Q_2-iQ_1 & Q_0+iQ_3\end{pmatrix},
$$

with

$$
\operatorname{Tr}\mathsf M(\tilde Q)=2Q_0,\qquad \det\mathsf M(\tilde Q)=N(\tilde Q),
$$

the natural conjugation being the adjugate; and the symmetric quaternionic product of two elements is the symmetrisation of the adjugated matrix product, with value the scalar matrix $N(\tilde P,\tilde Q)I_2$.

*Proof.* The trace is $2Q_0$ by inspection; the determinant is $(Q_0-iQ_3)(Q_0+iQ_3)-(-Q_2-iQ_1)(Q_2-iQ_1)=Q_0^2+Q_3^2+Q_1^2+Q_2^2=N(\tilde Q)$; the product statement is the definition of the block read through the realization of *The Symmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*: in the model the plain product is the matrix product, the natural conjugation is the adjugate, and $\tfrac12\bigl(\operatorname{adj}\mathsf M(\tilde P)\mathsf M(\tilde Q)+\operatorname{adj}\mathsf M(\tilde Q)\mathsf M(\tilde P)\bigr)=N(\tilde P,\tilde Q)I_2$.

**Corollary (the nilpotents of the block in the matrix model).** An element of the block is a nilpotent exactly when its matrix is **trace-free or singular**,

$$
\Upsilon_0=0\ \text{or}\ N(\tilde\Upsilon)=0\iff \operatorname{Tr}\mathsf M(\tilde\Upsilon)=0\ \text{or}\ \det\mathsf M(\tilde\Upsilon)=0,
$$

the index two family being the singular matrices and the index three family the trace-free nonsingular ones. The contrast with the parent is exact: the nilpotents of the plain algebra are the matrices that are simultaneously trace-free and singular (*Nilpotents of the General Plain Algebra*), and the block replaces the *and* by an *or*, one factor for each of its two nilpotent families.

## Summary

In the symmetric quaternionic block the powers of an element are central from the square on, $\tilde\Upsilon^{\star k}=N(\tilde\Upsilon)\Upsilon_0^{k-2}e_0$ for $k\geq2$, so an element is nilpotent exactly when it is isotropic, $N=0$, or pure, $\Upsilon_0=0$; the index is two on the isotropic cone and three on the pure non-isotropic part of the vector subspace, and the index is bounded by three. The square-zero elements are exactly the nonzero isotropic elements, hence exactly the roots of $0$ and the zero divisors of the parent algebra, while the block's own zero-divisor set is larger; the nilpotents and the idempotents of the block meet only at the origin; the nilpotent set and its two families are stable under the three conjugations. In the $2\times2$ model the trace of the matrix of $\tilde Q$ is $2Q_0$ and its determinant is $N(\tilde Q)$, so the block's nilpotents are the matrices that are trace-free or singular, against the parent's nilpotents, which are the matrices that are both.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ | the symmetric quaternionic multiplication |
| $N(\tilde Q)=\sum_\mu Q_\mu^2$ | the form at the two equal arguments |
| $\tilde\Upsilon^{\star k}=N\Upsilon_0^{k-2}e_0$ | the $k$-th power, $k\geq2$ |
| $N=0$ | the square-zero family, index two, the isotropic cone |
| $\Upsilon_0=0$, $N\neq0$ | the index three family, the pure anisotropic vectors |
| $\operatorname{Tr}\mathsf M=2Q_0$, $\det\mathsf M=N$ | the two invariants of the $2\times2$ model |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the general definition of the nilpotent, the index and the square-zero element.
- *Nilpotents of the General Plain Algebra* (`articles_maths/nilpotents-of-the-general-plain-algebra.md`), for the parent's nilpotents, their index and their matrix characterisation.
- *Zero Divisors* (`articles_maths/zero-divisors.md`), for the square-zero sets of the four general products.
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra.md`), for the maximal zero-divisor set of the block.
- *Idempotents of the Symmetric Quaternionic Algebra* (`articles_maths/idempotents-of-the-symmetric-quaternionic-algebra.md`), for the two idempotents and the disjointness from the nilpotents.
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), for the isotropic cone and its two families.
- *The Symmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-symmetric-quaternionic-algebra-in-the-2x2-matrix-element-representation.md`), for the realization used here.
