# __Idempotents of the Symmetric Quaternionic Algebra__

## Introduction

An idempotent of a product is an element with $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ (*Definitions for the Study of the 12 Algebraic Structures* §*The Idempotent, the Projection and the Peirce Decomposition*). In the parent plain algebra the idempotents are a continuum: they are in bijection with the roots of $-1$, they classify the non-pure zero divisors, and they drive the Peirce decomposition (*Idempotents of the General Plain Algebra*). In the symmetric quaternionic block the idempotents are **two and trivial**, $0$ and $e_0$, and every one of the four jobs the parent's idempotents do collapses with them. This article states the classification, states the three absences — the bijection with the roots, the classification of the zero divisors, the Peirce decomposition — names the witness of each, and records the one thing that does survive, the rank-one operator $L_{e_0}$, which is the projection onto the centre and is not the identity.

**Boundaries.** The general definitions of the idempotent, of the orthogonal and primitive idempotents, of the projection and of the Peirce decomposition are the definitions article; the idempotents of the parent are *Idempotents of the General Plain Algebra*; the roots of $\pm1$ are *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra*; the zero divisors are *Zero Divisors of the Symmetric Quaternionic Algebra*; the ideals and the Peirce decomposition of the parent are *Ideals and Peirce Decomposition of the General Plain Algebra*; the operators of the block are *The Multiplication Operators of the Symmetric Quaternionic Algebra* and *The Specificities of the Symmetric Quaternionic Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$; a general element is $\tilde Q=Q_0e_0+\mathbf Q$. The **symmetric quaternionic multiplication** is $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ with $N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ and diagonal $N(\tilde Q)=\sum_\mu Q_\mu^2$; it is also written $\bullet$. The centre is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, the vector subspace $\mathrm{Vect}(\mathbb{B})=\mathbb{C}e_1+\mathbb{C}e_2+\mathbb{C}e_3$, and $E$ is the projection $\tilde Y\mapsto Y_0e_0$ of the space onto its centre along the vector subspace.

## The General Definition

**Definition (idempotent of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Pi$ is an **idempotent of $\star$** when

$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi ,
$$

and it is **nontrivial** when it is neither the element $0$ nor the two-sided unit, when a unit exists. Idempotents of an associative product are **orthogonal** when $\tilde\Pi\star\tilde\Pi'=\tilde\Pi'\star\tilde\Pi=0$, **complete** when in addition their sum is the unit, and **primitive** when not a sum of two nonzero orthogonal idempotents.

Throughout this article the product is the **symmetric quaternionic product** of the block, and an idempotent, written without qualification, is an idempotent of that product.

## The Classification

**Theorem (the two idempotents).** The idempotents of the block are exactly $0$ and $e_0$.

*Proof.* The equation is $\tilde\Pi\star\tilde\Pi=N(\tilde\Pi)e_0=\tilde\Pi$. The right side must be central, so $\tilde\Pi=\Pi_0e_0$ has vanishing vector part; the equation becomes $\Pi_0^2=\Pi_0$, whose solutions are $\Pi_0=0$ and $\Pi_0=1$. Both are realized, $\tilde\Pi=0$ and $\tilde\Pi=e_0$, since $0\star0=0$ and $e_0\star e_0=e_0$.

**Corollary (the pair is orthogonal and trivial).** The two idempotents are orthogonal, $0\star e_0=e_0\star0=0$, and their sum is $e_0$, which acts as the identity on the image $\mathbb{C}e_0$ of the block without being a unit of the algebra, since the block has none (*Norm and Invertibility in the Symmetric Quaternionic Algebra*). Neither idempotent is primitive in the sense of the corner algebra, because no associative structure and no Peirce decomposition exists in the block, and the words *trivial* and *nontrivial* are used below with the ambient notion only.

**Comparison (with the parent's continuum).** In the parent the idempotents are $\tilde\Pi=\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-1$, a set of real dimension four, and the two trivial idempotents are the images of the two degenerate roots $\tilde\Xi=\pm i$, since $\tfrac12(e_0+i\cdot i)=0$ and $\tfrac12(e_0-i\cdot i)=e_0$. In the block the whole continuum disappears and exactly the two trivial idempotents survive; the block shares its two trivial idempotents with every other product of the twelve, since $0$ and $e_0$ are idempotents of each of the twelve operations for which the square of $e_0$ is $e_0$.

## The Bijection With the Roots of Minus One

**Theorem (the bijection fails).** There is no bijection between the roots of $\pm1$ of the block and its idempotents. What survives is the following: the affine map

$$
\tilde P\ \longmapsto\ \tilde\Pi=\tfrac12(e_0+\tilde P)
$$

carries the **central** roots of $+1$, that is $\tilde P=\pm e_0$, onto the two idempotents $e_0$ and $0$, and carries no other root of $+1$ and no root of $-1$ to an idempotent.

*Proof.* $\tilde\Pi\star\tilde\Pi=\tfrac14\bigl(1+2P_0+N(\tilde P)\bigr)e_0$ and $\tilde\Pi=\tfrac12(e_0+\tilde P)$ are equal only if $\tilde P$ is central, and then the condition is $P_0^2=1$; the computation is the one of *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra* §*The Relation to the Idempotents and to the Zero Divisors*, where the failure of the bijection of the parent is traced to the absence of associativity and of a unit.

**Remark (the reason, in one sentence).** In the parent the identity is read from associativity and the unit, and the vector part of $\tilde\Pi$ is cancelled by the equation $\tilde\Xi^2=-1$; in the block the product is central-valued, the square $\tilde\Pi\star\tilde\Pi$ can only be a scalar multiple of $e_0$, and the vector part of $\tilde\Pi$ can never be cancelled. The bijection of the parent is therefore not merely unproved in the block but false in it, the root sets being three-dimensional and the idempotent set being two points.

## The Idempotents as Projections

**Theorem (the operator of $e_0$ is the projection onto the centre).** The left multiplication by the idempotent $e_0$,

$$
L_{e_0}:\tilde Y\longmapsto e_0\star\tilde Y=Y_0e_0=E(\tilde Y),
$$

is the projection of $\mathbb{B}$ onto its centre along its vector subspace; the multiplication by $0$ is the zero operator; and the two are the only idempotent endomorphisms that are multiplications by idempotents. The operator $L_{e_0}$ is not the identity, because the block has no unit: it fixes the centre and annihilates the vector subspace.

*Proof.* $e_0\star\tilde Y=N(e_0,\tilde Y)e_0=Y_0e_0$ by the definition of the product; the operator thus has image the centre, kernel the vector subspace, and it is idempotent, $L_{e_0}^2=L_{e_0}$; the statement about the identity is the absence of a unit. The operator theory of the block, including its other idempotent endomorphisms, is *The Specificities of the Symmetric Quaternionic Algebra*.

**Corollary (the substitution and the absence of a Peirce decomposition).** The block has **no Peirce decomposition**: the construction presupposes that the product is associative with a unit, and the block is neither (*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*). The decomposition that is available is the elementary splitting of the operator $L_{e_0}$,

$$
\mathbb{B}=\mathbb{C}e_0\oplus\mathrm{Vect}(\mathbb{B})=\operatorname{im}L_{e_0}\oplus\ker L_{e_0},
$$

which is a direct sum decomposition of the space under the projection $E$ and not a Peirce decomposition: the two summands are not corner algebras, and the vector subspace is not stable under the product, since $e_1\star e_1=e_0$ leaves it.

**Remark (the idempotents as projections in the sense of the $*$-algebras).** With the ambient involution the two idempotents are self-adjoint, $e_0^{*}=e_0$ and $0^{*}=0$, so both are projections of the ambient $*$-algebra, and the splitting above is the orthogonal direct sum for the form $N$, the centre and the vector subspace being mutually orthogonal. No other element of the block is an idempotent, so the block carries no other projection, Hermitian or not.

## The Relation to the Zero Divisors

**Theorem (no classification of the zero divisors by the idempotents).** In the parent every non-pure zero divisor is the complex multiple $2Q_0\tilde\Pi$ of a nontrivial idempotent $\tilde\Pi$, which is the way the parent classifies its zero divisors (*Zero Divisors of the General Plain Algebra*). In the block the statement has no analogue: the block has no nontrivial idempotent, and its zero-divisor set is the whole punctured space (*Zero Divisors of the Symmetric Quaternionic Algebra*), so no subfamily of idempotents can index it.

*Proof.* The parent's statement is a theorem there and presupposes its continuum of idempotents; the block's idempotents are the two of the classification theorem, so the only multiples available are the central elements $\lambda e_0$, a one-dimensional family inside the eight-real-dimensional zero-divisor set.

**Remark (the two ends of the collapse).** The pair $0$ and $e_0$ is the extreme case of the two constructions the parent's idempotents carry. The idempotent **endomorphisms** of the block are a strictly larger family than its idempotent **elements**: by the identity $L_{\tilde X}^2=X_0L_{\tilde X}$ of *The Specificities of the Symmetric Quaternionic Algebra* the idempotent multiplications are the $L_{\tilde X}$ with $X_0=1$, a hyperplane of pairwise distinct rank-one projections onto the central line, together with the zero operator; the idempotent elements are $0$ and $e_0$ alone, and $E=L_{e_0}$ is the member of the family whose kernel is the vector subspace. The idempotent endomorphisms of the block and the idempotents of the product are therefore two different sets, and the difference is stated in *The Specificities of the Symmetric Quaternionic Algebra*.

## Summary

The idempotents of the symmetric quaternionic product are exactly $0$ and $e_0$: the equation $\tilde\Pi\star\tilde\Pi=N(\tilde\Pi)e_0=\tilde\Pi$ forces the vector part to vanish, and the scalar part satisfies $\Pi_0^2=\Pi_0$. The continuum of idempotents of the parent plain algebra, which is in bijection with the roots of $-1$, dissolves in the block: the affine map $\tilde\Pi=\tfrac12(e_0+\tilde P)$ carries only the two central roots of $+1$ to idempotents, and no root of $-1$ at all, because the centrality of the product prevents the vector part of $\tilde\Pi$ from being cancelled. The idempotent $e_0$ acts by the projection $E$ onto the centre along the vector subspace, which is not the identity — the block having no unit — and the block has no Peirce decomposition, the available splitting $\mathbb{B}=\mathbb{C}e_0\oplus\mathrm{Vect}(\mathbb{B})$ being the image–kernel splitting of $E$ and not a decomposition into corner algebras. The parent's classification of the zero divisors by nontrivial idempotents has no analogue, since the block has neither the idempotents nor a proper zero-divisor set; the idempotent endomorphisms of the block are a different, larger family, treated in the Specificities entry.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ | the symmetric quaternionic multiplication |
| $N(\tilde Q)=\sum_\mu Q_\mu^2$ | the diagonal of the form |
| $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ | the idempotent equation of the block |
| $0$, $e_0$ | the two idempotents of the block |
| $E(\tilde Y)=Y_0e_0$ | the projection onto the centre, the operator of $e_0$ |
| $\mathbb{B}=\mathbb{C}e_0\oplus\mathrm{Vect}(\mathbb{B})$ | the image–kernel splitting of $E$, not a Peirce decomposition |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the general definitions of the idempotent, the projection and the Peirce decomposition.
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra.md`), for the parent's classification and its bijection with the roots of $-1$.
- *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-symmetric-quaternionic-algebra.md`), for the root sets and the failure of the affine map.
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra.md`), for the maximal zero-divisor set.
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra.md`) and *The Specificities of the Symmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-symmetric-quaternionic-algebra.md`), for the operators of the idempotents and for the idempotent endomorphisms.
