# __Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic product is the pairing $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ on $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the product of the block (*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*), and it is the product read throughout this article. A root of a central value $\lambda$ is a nonzero element with $\tilde\Xi\star\tilde\Xi=\lambda e_0$, and a nilpotent is an element some power of which vanishes, the index being the least such power, a square-zero element being one of index two (*Definitions for the Study of the 12 Algebraic Structures* §*Powers, the Square and the Roots* and §*The Nilpotent*).

The article treats two subjects, and in this order. The first is the square roots of the central value $0$, the elements $\tilde\Xi\in\mathbb{B}$ with

$$
\tilde\Xi\star\tilde\Xi=0,\qquad \tilde\Xi\neq0 .
$$

The second is the nilpotents, the elements with $\tilde\Xi^{\star k}=0$ for some $k$. The two subjects meet at the index two case: the roots of $0$ are exactly the square-zero elements, that is the nilpotents of index two, and the nilpotents of the block add one more family, the pure non-isotropic elements, of index three. The roots-of-$0$ part states the reduction, the set and the pointer to the index; the nilpotent part states the powers, the criterion and everything downstream of it. The criterion is proved once, in §*The Criterion and the Index*, and §*The Roots of Zero* cites it.

**The results.** The roots of $0$ are the punctured isotropic cone $\{N=0\}\setminus\{0\}$ of the form $N(\tilde\Xi)=\Xi_0^2+(\mathbf\Xi,\mathbf\Xi)$, of complex dimension three and real dimension six, with the two families of *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*; they are exactly the square-zero elements of the block and exactly the zero divisors of the parent algebra, while the block's own zero-divisor set is the whole punctured space. The powers of an element are central from the square on,

$$
\tilde\Upsilon^{\star k}=N(\tilde\Upsilon)\,\Upsilon_0^{\,k-2}\,e_0\qquad(k\geq2),
$$

so an element is nilpotent exactly when it is isotropic, $N=0$, or pure, $\Upsilon_0=0$. The index is two on the whole isotropic cone and three on the pure non-isotropic part of the vector subspace, and it is bounded by three. The nilpotents and the idempotents meet only at $0$; the nilpotent set and its two families are stable under the three conjugations; and in the $2\times2$ model the trace is $2Q_0$ and the determinant is $N(\tilde Q)$, so the block's nilpotents are the matrices that are trace-free or singular.

The article is algebraic. It does not treat the roots of $+1$ and the idempotents, which are *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra*; the roots of a general element, which are *Square Roots of a General Element in the Symmetric Quaternionic Algebra*; the isotropic cone and its two families, which are *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*; the structure of the zero-divisor set, which is *Zero Divisors of the Symmetric Quaternionic Algebra*; or the square-zero sets of the four general products, which are *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and *Comparison Between the Four General Products*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, and central scalar imaginary $i$, $i^2=-1$. A general element is $\tilde\Upsilon=\Upsilon_0e_0+\mathbf\Upsilon$ with $\Upsilon_\mu\in\mathbb{C}$ and $\mathbf\Upsilon=\Upsilon_1e_1+\Upsilon_2e_2+\Upsilon_3e_3$, and $(\mathbf P,\mathbf Q)=\sum_{k=1}^{3}P_kQ_k$ may vanish without $\mathbf\Upsilon$ vanishing. The **symmetric quaternionic multiplication** is

$$
\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0,\qquad N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q),
$$

and its diagonal is $N(\tilde\Upsilon)=N(\tilde\Upsilon,\tilde\Upsilon)=\sum_{\mu=0}^{3}\Upsilon_\mu^2$; the operation is also written $\bullet$. The centre is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ and the vector subspace is $\mathrm{Vect}(\mathbb{B})=\mathbb{C}e_1+\mathbb{C}e_2+\mathbb{C}e_3$. A root of a central value is written $\tilde\Xi$, a nilpotent $\tilde\Upsilon$ (§*The Nilpotent Convention* of *Conventions in Mathematics*), and a generic element $\tilde P$.

The equations name a product, so the roots and the nilpotents are relative to it. The general definition of the nilpotent and of the square-zero element is *Definitions for the Study of the 12 Algebraic Structures* §*The Nilpotent*. Throughout this article the product is the symmetric quaternionic product; the block is not associative, so the bracketing of a power is fixed to the left-nested reading, and for this product the right-nested reading gives the same value.

## The Roots of Zero

**The roots of $0$ are exactly the elements with $N(\tilde\Xi)=\Xi_0^2+(\mathbf\Xi,\mathbf\Xi)=0$ and $\tilde\Xi\neq0$: the punctured isotropic cone of the form, of complex dimension three and real dimension six, whose elements are exactly the square-zero elements of the block and the zero divisors of the parent algebra.**

A **root of $0$** is a nonzero element $\tilde\Xi\in\mathbb{B}$ with $\tilde\Xi\star\tilde\Xi=0$, the square being the one of the symmetric quaternionic product.

### The Reduction

**The reduction of the square of the block, $\tilde\Xi\star\tilde\Xi=N(\tilde\Xi)e_0$, gives for the value $0$ the single scalar equation $N(\tilde\Xi)=\Xi_0^2+(\mathbf\Xi,\mathbf\Xi)=0$, so the root set of $0$ is the level set $N=0$ minus the origin: the isotropic cone of the form, the only level that is invariant under every scaling.**

**Theorem (the roots of zero).** The roots of $0$ are exactly the elements with

$$
N(\tilde\Xi)=\Xi_0^2+(\mathbf\Xi,\mathbf\Xi)=0,\qquad \tilde\Xi\neq0 .
$$

*Proof.* The square is $N(\tilde\Xi)e_0$ by the definition of the product, and it vanishes exactly when $N(\tilde\Xi)=0$; the value $\tilde\Xi=0$ is excluded by the definition of a root, which is a nonzero element. The reduction and the behaviour of the level sets under the conjugations and the scalings are *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra* §*The Reduction* and §*The Three Level Sets*.

The origin is the only element of vanishing square that is not a root, and it is the trivial nilpotent of §*The General Definition*.

### The Zero Element

**The element $0$ is not a root of $0$, by the definition of a root, and it is the only element whose square is $0$ and that is excluded from the root set: a root of a central value is required to be nonzero, so the level set $N=0$ minus the origin, and not the whole cone, is the root set.**

### The Isotropic Cone

**The level set $\{N=0\}$ is the isotropic cone of the form $N$: a quadric cone of complex dimension three and real dimension six with vertex $0$, and the root set of $0$ is that cone minus its vertex. Its two families are those of *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*.**

**Theorem (the cone).** The set $\{\tilde\Xi:N(\tilde\Xi)=0\}$ is a quadric cone of complex dimension three and real dimension six, with vertex the origin and with the two families of *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*; the roots of $0$ are this cone minus the origin.

*Proof.* $N$ is a nonsingular quadratic form in four complex variables and homogeneous, so its zero set is a cone of complex dimension three; the puncturing is the definition of a root. The families are computed in the Specific Theory entry.

**Examples.** $\tilde\Xi=e_0+ie_1$: $N=1+(i)^2=0$ and $\tilde\Xi\star\tilde\Xi=0$, a root of $0$. $\tilde\Xi=e_1+ie_2$: $N=1-1=0$, a root of $0$. $\tilde\Xi=e_1+ie_1=(1+i)e_1$: $N=(1+i)^2=2i\neq0$, not isotropic.

### The Roots of Zero and the Nilpotents

**The nonzero roots of $0$ are exactly the square-zero elements of the block, that is the elements whose square vanishes and that are not $0$: the nilpotents of index two, as §*The Criterion and the Index* proves. They are exactly the isotropic elements, and hence exactly the zero divisors of the parent algebra, a proper subset of the block's zero-divisor set.**

**Corollary (the roots of zero and the square-zero elements).** The roots of $0$ and the square-zero elements of the block are the same set: the punctured isotropic cone

$$
\{\tilde\Xi:\tilde\Xi\star\tilde\Xi=0,\ \tilde\Xi\neq0\}=\{N=0\}\setminus\{0\}.
$$

Every root of $0$ is a nilpotent of index two, and every zero divisor of the parent algebra is a root of $0$, while the block's own zero-divisor set is the whole punctured space (*Zero Divisors of the Symmetric Quaternionic Algebra*, and §*The Criterion and the Index* below).

*Proof.* The square-zero elements are by definition the nonzero elements with vanishing square, which the reduction identifies with the roots of $0$; the parent's zero divisors are the isotropic elements and the block's are everything but the origin.

## The Nilpotents

**An element of the block is a nilpotent exactly when $N(\tilde\Upsilon)=0$ or $\Upsilon_0=0$, that is exactly when it is isotropic or pure; the index is two on the isotropic cone and three on the pure non-isotropic family $\{\Upsilon_0=0,\ N\neq0\}$, the nilpotent set is the union of the cone and the vector subspace, and the index is bounded by three.**

### The General Definition

**Definition (nilpotent of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Upsilon$ is **nilpotent of $\star$** when

$$
\tilde\Upsilon^{\star k}=0\quad\text{for some }k\geq1,
$$

the power being the left-nested one when $\star$ is not associative; the least such $k$ is the **index of nilpotency**, and an element of index two, $\tilde\Upsilon\star\tilde\Upsilon=0$ with $\tilde\Upsilon\neq0$, is a **square-zero element**.

Throughout this article a nilpotent, an index or a square-zero element, written without qualification, is one of the **symmetric quaternionic product**. The block is not associative, so the bracketing of a power matters a priori and is fixed to the left-nested reading; for this product the right-nested reading gives the same value, because $\tilde\Upsilon\star(\tilde\Upsilon\star\tilde\Upsilon)=\Upsilon_0N(\tilde\Upsilon)e_0$ by the computation of the next section.

### The Powers of an Element

**For every element and every $k\geq2$ the $k$-th power is central, $\tilde\Upsilon^{\star k}=N(\tilde\Upsilon)\Upsilon_0^{k-2}e_0=\Upsilon_0^{k-2}(\tilde\Upsilon\star\tilde\Upsilon)$, so the index of nilpotency is at most three.**

**Theorem (the powers).** For every $\tilde\Upsilon$ and every $k\geq2$,

$$
\tilde\Upsilon^{\star k}=N(\tilde\Upsilon)\,\Upsilon_0^{\,k-2}\,e_0=\Upsilon_0^{\,k-2}\bigl(\tilde\Upsilon\star\tilde\Upsilon\bigr).
$$

*Proof.* For $k=2$ the formula is $\tilde\Upsilon^{\star2}=N(\tilde\Upsilon)e_0$, the square of the block. Assume it for $k$; then $\tilde\Upsilon^{\star(k+1)}=\tilde\Upsilon^{\star k}\star\tilde\Upsilon=N(\tilde\Upsilon)\Upsilon_0^{k-2}e_0\star\tilde\Upsilon=N(\tilde\Upsilon)\Upsilon_0^{k-2}\cdot\Upsilon_0e_0=N(\tilde\Upsilon)\Upsilon_0^{k-1}e_0$, which is the formula at $k+1$; the displayed equality with $\Upsilon_0^{k-2}(\tilde\Upsilon\star\tilde\Upsilon)$ is the same computation reversed. The right-nested reading gives the same value, since $\tilde\Upsilon\star(\tilde\Upsilon\star\tilde\Upsilon)=\tilde\Upsilon\star(N(\tilde\Upsilon)e_0)=N(\tilde\Upsilon)\Upsilon_0e_0$.

**Corollary (the index is at most three).** The index of nilpotency of a nilpotent of the block is two or three, and the higher powers vanish as soon as $N(\tilde\Upsilon)\Upsilon_0=0$.

*Proof.* The formula shows that $\tilde\Upsilon^{\star3}=N(\tilde\Upsilon)\Upsilon_0e_0$; if this vanishes then every later power vanishes by the formula, and if it does not vanish then no power vanishes, because $\Upsilon_0^{k-2}$ is a power of a nonzero scalar.

### The Criterion and the Index

**An element is a nilpotent of the block exactly when $N(\tilde\Upsilon)=0$ or $\Upsilon_0=0$, that is exactly when it is isotropic or pure; the index is two on the isotropic cone and three on the pure non-isotropic family, and the nilpotent set is the union of the cone and the vector subspace.**

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

the union of the isotropic cone and the vector subspace, the two meeting in the pure isotropic elements, which are of index two. The set is the union of a quadric cone of complex dimension three and a linear subspace of complex dimension three.

### The Square-Zero Set

**The square-zero elements are exactly the nonzero isotropic elements, $\{N=0\}\setminus\{0\}$, the punctured isotropic cone of complex dimension three and real dimension six, and they are exactly the roots of $0$ of the block and the zero divisors of the parent algebra.**

**Theorem (the square-zero elements are the isotropic elements).** The square-zero elements of the block are exactly the nonzero isotropic elements,

$$
\{\tilde\Upsilon:\tilde\Upsilon\star\tilde\Upsilon=0,\ \tilde\Upsilon\neq0\}=\{N=0\}\setminus\{0\},
$$

the punctured isotropic cone of complex dimension three and real dimension six, with the two families of *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*. They are exactly the roots of $0$ of the block and exactly the zero divisors of the parent algebra.

*Proof.* $\tilde\Upsilon\star\tilde\Upsilon=N(\tilde\Upsilon)e_0$ vanishes exactly when $N(\tilde\Upsilon)=0$, and $0$ is excluded by the definition; the identification with the roots of $0$ is §*The Roots of Zero* and with the zero divisors of the parent is *Zero Divisors of the Symmetric Quaternionic Algebra*.

**Examples.** $\tilde\Upsilon=e_0+ie_1$: $N=0$, index two. $\tilde\Upsilon=e_1$: pure, $N=1$, index three, since $e_1\star e_1=e_0$ and $e_1\star e_0=0$. $\tilde\Upsilon=e_1+e_2$: pure, $N=2$, index three. $\tilde\Upsilon=e_0+e_1$: $N=2$ and $\Upsilon_0=1$, not a nilpotent.

### The Nilpotents and the Zero Divisors

**Every nonzero nilpotent of the block is a zero divisor, the block's zero-divisor set being the whole punctured space, while $e_0$ is a zero divisor and not a nilpotent; the implication *nilpotent implies zero divisor* therefore holds trivially in the block, and the converse fails in the sharpest possible way.**

**Proposition (the nilpotents are zero divisors, and they are far from exhausting them).** Every nonzero nilpotent of the block is a zero divisor of it, since the block's zero-divisor set is the whole punctured space; conversely the non-isotropic, non-pure elements, for instance $e_0$, are zero divisors and not nilpotents.

*Proof.* *Zero Divisors of the Symmetric Quaternionic Algebra* gives the block's zero-divisor set as the whole punctured space; the criterion excludes $e_0$ from the nilpotents, since $N(e_0)=1$ and its scalar part is $1$.

**Remark (the two families the index separates).** The block's two nilpotent families are not the parent's two zero-divisor families. In the parent the nilpotents are the pure isotropic elements and the non-pure zero divisors are the idempotent multiples (*Zero Divisors of the General Plain Algebra*); in the block the index two family is the whole isotropic cone — pure or not — and the index three family is the pure anisotropic part of the vector subspace, which in the parent consists of units and of no zero divisor at all. The block thus produces nilpotents of an index the parent does not have, and it produces them on elements that the parent regards as regular.

### The Nilpotents and the Idempotents

**The only element of the block that is both an idempotent and a nilpotent is $0$; the idempotent $e_0$ is not a nilpotent, all its powers being $e_0$, and the square-zero elements are not idempotents.**

**Proposition (the nilpotents and the idempotents meet only at the origin).** The only element of the block that is both an idempotent and a nilpotent is $0$. The idempotent $e_0$ is not a nilpotent, all its powers being $e_0$, and the square-zero elements are not idempotents, since $\tilde\Upsilon\star\tilde\Upsilon=0$ and $\tilde\Upsilon\star\tilde\Upsilon=\tilde\Upsilon$ give $\tilde\Upsilon=0$.

*Proof.* The classification of the idempotents is *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra*, where they are shown to be $0$ and $e_0$; the two statements displayed are immediate.

### The Conjugations

**The three conjugations preserve the nilpotent set and its two index families: the natural conjugation and the star preserve $\Upsilon_0=0$, and $N=0$ is preserved by the natural conjugation and by the Hermitian conjugation, while the star conjugates the value, so the square-zero set and the vector subspace are each stable and the index of a nilpotent is unchanged.**

**Theorem (the nilpotent set is invariant).** The three conjugations preserve the nilpotent set and its two index families:

$$
N(\tilde\Upsilon^{\natural})=N(\tilde\Upsilon),\qquad N(\tilde\Upsilon^{*})=\overline{N(\tilde\Upsilon)},\qquad
(\Upsilon^{\natural})_0=\Upsilon_0,\qquad (\Upsilon^{*})_0=\overline{\Upsilon_0},
$$

so $\Upsilon_0=0$ is preserved by ${}^{\natural}$ and by ${}^{*}$, and $N=0$ by ${}^{\natural}$ and by the Hermitian conjugation, while ${}^{*}$ preserves $N=0$ by conjugating the value.

*Proof.* The natural conjugation negates the vector part, the star conjugates all four coefficients and negates the vector part; the identities for $N$ are those of *Norm and Invertibility in the Symmetric Quaternionic Algebra*, and a vanishing scalar or form is preserved by the sign or the conjugation of the value.

**Corollary.** The square-zero set and the vector subspace are each stable under the three conjugations, and the index of a nilpotent is unchanged by them.

### The Matrix Model

**In the $2\times2$ realization the matrix of $\tilde Q$ has trace $2Q_0$ and determinant $N(\tilde Q)$; an element is a nilpotent exactly when its matrix is trace-free or singular, the index two family being the singular matrices and the index three family the trace-free nonsingular ones.**

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

the index two family being the singular matrices and the index three family the trace-free nonsingular ones. The contrast with the parent is exact: the nilpotents of the plain algebra are the matrices that are simultaneously trace-free and singular (*Square Roots of Zero and the Nilpotents of the General Plain Algebra*), and the block replaces the *and* by an *or*, one factor for each of its two nilpotent families.

## Summary

In the symmetric quaternionic block the square is always central, $\tilde\Xi\star\tilde\Xi=N(\tilde\Xi)e_0$, so the roots of $0$ are the elements with $N=0$ and $\tilde\Xi\neq0$: the punctured isotropic cone, of complex dimension three and real dimension six, and exactly the square-zero elements and the zero divisors of the parent algebra, a proper subset of the block's own zero-divisor set, which is the whole punctured space. The powers of an element are central from the square on, $\tilde\Upsilon^{\star k}=N(\tilde\Upsilon)\Upsilon_0^{k-2}e_0$ for $k\geq2$, so an element is nilpotent exactly when it is isotropic, $N=0$, or pure, $\Upsilon_0=0$; the index is two on the isotropic cone and three on the pure non-isotropic part of the vector subspace, and the index is bounded by three. The nilpotents are the square-zero elements together with the pure anisotropic vectors, they are all zero divisors and they meet the idempotents only at $0$; the nilpotent set and its two families are stable under the three conjugations. In the $2\times2$ model the trace of the matrix of $\tilde Q$ is $2Q_0$ and its determinant is $N(\tilde Q)$, so the block's nilpotents are the matrices that are trace-free or singular, against the parent's nilpotents, which are the matrices that are both.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ | the symmetric quaternionic multiplication |
| $N(\tilde Q)=\sum_\mu Q_\mu^2=\Xi_0^2+(\mathbf\Xi,\mathbf\Xi)$ | the form at the two equal arguments |
| $\{N=0\}\setminus\{0\}$ | the roots of $0$, the square-zero elements, the nilpotents of index two |
| $\tilde\Upsilon^{\star k}=N\Upsilon_0^{k-2}e_0$ | the $k$-th power, $k\geq2$ |
| $N=0$ | the square-zero family, index two, the isotropic cone |
| $\Upsilon_0=0$, $N\neq0$ | the index three family, the pure anisotropic vectors |
| $\operatorname{Tr}\mathsf M=2Q_0$, $\det\mathsf M=N$ | the two invariants of the $2\times2$ model |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the general definition of the nilpotent, of the index and of the square-zero element.
- *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-quaternionic-algebra.md`), for the roots of $+1$, the idempotents and the reduction.
- *Square Roots of a General Element in the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-symmetric-quaternionic-algebra.md`), for the radicands that are not the central values.
- *Square Roots of Zero and the Nilpotents of the General Plain Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-plain-algebra.md`), for the parent's nilpotents, their index and their matrix characterisation.
- *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the square-zero sets of the four general products.
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra.md`), for the maximal zero-divisor set of the block.
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), for the isotropic cone and its two families.
- *The Symmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-symmetric-quaternionic-algebra-in-the-2x2-matrix-element-representation.md`), for the realization used here.
