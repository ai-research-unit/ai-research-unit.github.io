# __Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra__

## Introduction

A root of a central value $\lambda$ in a product is a nonzero element with $\tilde P\star\tilde P=\lambda e_0$ (*Definitions for the Study of the 12 Algebraic Structures* §*Powers, the Square and the Roots*). In the symmetric quaternionic product the square is always central, $\tilde P\star\tilde P=N(\tilde P)e_0$, so the equation is the single scalar equation $N(\tilde P)=\lambda$ for the quadratic form $N(\tilde P)=\sum_{\mu=0}^{3}P_\mu^2$ (*Norm and Invertibility in the Symmetric Quaternionic Algebra*). The three values the algebra singles out — $-1$, $0$ and $+1$ — therefore give three level sets of one quadratic form, and this article computes them, compares them, and reads their relations to the idempotents of the block and to its zero divisors.

The reduction is total in the block, in the sense that the vector part enters only through the single scalar $(\mathbf P,\mathbf P)$ and never through a vector equation; the three sets are consequently **quadric hypersurfaces of complex dimension three**, one of which, the level $0$, is a cone. The article gives the common reduction, the three sets with their parametrisations and their examples, the three-set comparison through the scaling of the form, and the two relations at the end: the roots of $0$ are exactly the square-zero elements, hence exactly the zero divisors of the parent algebra, while the correspondence between the roots and the idempotents of the block fails.

**Boundaries.** The classification of the roots of a general element is *Square Roots of a General Element in the Symmetric Quaternionic Algebra*; the square-zero elements and their index are *Nilpotents of the Symmetric Quaternionic Algebra*; the idempotents are *Idempotents of the Symmetric Quaternionic Algebra*; the isotropic cone and its families are *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*; the three parallel classifications in the parent are *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, and the general definitions are the definitions article.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$, and central scalar imaginary $i$, $i^2=-1$; a general element is $\tilde P=P_0e_0+\mathbf P$, and $(\mathbf P,\mathbf P)=\sum_{k=1}^{3}P_k^2$ may vanish without $\mathbf P$ vanishing. The **symmetric quaternionic multiplication** is $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ with $N(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$, and its diagonal is $N(\tilde P)=N(\tilde P,\tilde P)=\sum_{\mu=0}^{3}P_\mu^2$; the operation is also written $\bullet$. The centre is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, and the subspaces $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_\pm$ are those of *Introduction to the Remarkable Subspaces*.

## The Common Reduction

**Theorem (the reduction).** For every $\lambda\in\mathbb{C}$, the equation $\tilde P\star\tilde P=\lambda e_0$ is equivalent to the single scalar equation

$$
N(\tilde P)=P_0^2+(\mathbf P,\mathbf P)=\lambda ,
$$

so that every root set is a level set of the diagonal form: the natural conjugation and the sign leave each level set in place, while the star and the Hermitian conjugation carry the level set of $\lambda$ onto the level set of $\overline{\lambda}$.

*Proof.* The square is $N(\tilde P)e_0$ by the definition of the product; comparing coefficients of the basis gives the scalar equation, since $N$ depends only on the four coefficients squared and not on their order. The natural conjugation replaces $\mathbf P$ by $-\mathbf P$ and leaves the scalar part, so $N(\tilde P^{\natural})=N(\tilde P)$; the star conjugates the four coefficients and negates the vector part, and the Hermitian conjugation conjugates all four, so both give $N(\tilde P^{*})=N(\overline{\tilde P})=\overline{N(\tilde P)}$.

**Corollary (the three equations).** The roots of $-1$, of $0$ and of $+1$ are

$$
\{\tilde P: N(\tilde P)=-1\},\qquad\{\tilde P: N(\tilde P)=0\},\qquad\{\tilde P: N(\tilde P)=1\},
$$

three level sets of the same quadratic form, pairwise disjoint, and each invariant under the three conjugations. The description of the sets does not involve the order of the coefficients: the block's root problem is a problem of a quadratic form and not of a multiplication.

**Remark (the shape of the level sets).** For $\lambda\neq0$ the level set is an affine hyperquadric of $\mathbb{C}^4$ — the zero set of the nonsingular quadratic polynomial $N-\lambda$ — of complex dimension three and real dimension six; for $\lambda=0$ it is the isotropic cone of the form, a quadric cone of the same dimensions with vertex $0$. Throughout the article the words *quadric* and *cone* name these algebraic sets and nothing else.

## The Roots of Minus One

**Theorem (parametrisation of the roots of $-1$).** The roots of $-1$ are exactly the elements

$$
\tilde P=P_0e_0+\mathbf P,\qquad P_0^2=-1-(\mathbf P,\mathbf P).
$$

Over each vector part $\mathbf P$ the solutions are the square roots of $-1-(\mathbf P,\mathbf P)$: two of them, $P_0$ and $-P_0$, when $(\mathbf P,\mathbf P)\neq-1$, and the single value $P_0=0$ when $(\mathbf P,\mathbf P)=-1$. The set has complex dimension three; it is nonempty, it contains the two central roots $\pm ie_0$, and it contains no isotropic element.

*Proof.* The reduction gives $P_0^2+(\mathbf P,\mathbf P)=-1$; for fixed $\mathbf P$ with $-1-(\mathbf P,\mathbf P)\neq0$ there are exactly two values of $P_0$; for the exceptional $\mathbf P$ with $(\mathbf P,\mathbf P)=-1$ the value $P_0=0$ gives the root $\tilde P=\mathbf P$, drawn by the same formula with the double value $0$. An isotropic root would satisfy $N(\tilde P)=0\neq-1$. The value $(\mathbf P,\mathbf P)=-1$ is attained, for instance at $\mathbf P=ie_1$, and there the root $ie_1$ has vanishing scalar part.

**Examples.** $\tilde P=ie_0$: $N=-1$. $\tilde P=ie_1$: $N=(i)^2=-1$. $\tilde P=e_1$: $N=1$, a root of $+1$ and not of $-1$. $\tilde P=e_0+e_1$: $N=1+1=2$, a root of neither.

**Remark (the two central roots).** The only central roots of $-1$ are $\pm ie_0$, since a central element is $\lambda e_0$ with $\lambda^2=-1$. The central roots are the ones that the idempotent correspondence of the parent uses, and it is exactly they that the block cannot use, as §*The Relation to the Idempotents* shows.

## The Roots of Zero

**Theorem (the roots of zero are the square-zero elements).** The set $\{\tilde P: N(\tilde P)=0\}$ is exactly the set of nonzero elements whose square vanishes in the block, $\tilde P\star\tilde P=0$, and it is the punctured isotropic cone of *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*: a cone of complex dimension three, real dimension six, with the two families of the isotropic structure.

*Proof.* $\tilde P\star\tilde P=N(\tilde P)e_0$ vanishes exactly when $N(\tilde P)=0$; the cone and its families are the ones computed in the Specific Theory entry.

**Examples.** $\tilde P=e_0+ie_1$: $N=1+(i)^2=0$ and $\tilde P\star\tilde P=0$. $\tilde P=e_1+ie_2$: $N=1-1=0$. $\tilde P=e_1+ie_1=(1+i)e_1$: $N=(1+i)^2=2i\neq0$.

**Corollary.** Every root of $0$ is an isotropic element, hence a zero divisor of the *parent* plain product, and a nilpotent of index two of the block; the block's own zero-divisor set is larger and contains the non-isotropic elements as well (*Zero Divisors of the Symmetric Quaternionic Algebra*).

## The Roots of Plus One

**Theorem (the roots of $+1$).** The roots of $+1$ are the elements with $N(\tilde P)=1$. The set has complex dimension three and contains the four basis elements $e_0,e_1,e_2,e_3$ and the level set $N=1$ read on the two Hermitian subspaces; it is the level set of the diagonal used in *Norm and Invertibility in the Symmetric Quaternionic Algebra* as the analogue of the norm-one group of an associative unital product.

*Proof.* The reduction gives the equation; the four basis elements have $N=1$ by the table $N(e_\mu,e_\nu)=\delta_{\mu\nu}$; the level set is an affine hyperquadric because $1\neq0$.

**Examples.** $e_0\star e_0=e_0$ and $e_k\star e_k=e_0$, so the four basis elements are roots. $ie_1$ is a root of $-1$ and not of $+1$. On the Hermitian subspace $\mathbb{M}_+$, an element $q_0e_0+i(q_1e_1+q_2e_2+q_3e_3)$ with real $q$ has $N=q_0^2-q_1^2-q_2^2-q_3^2$, so the roots of $+1$ there are the elements of the level set of that form, and the roots of $0$ the light cone.

## The Three Sets

**Proposition (the three sets in one display).** On every complex line $\mathbb{C}\tilde P$ through the origin, the three equations read $t^2N(\tilde P)=\lambda$ for $\tilde P=t\tilde A$, since $N(t\tilde A)=t^2N(\tilde A)$:

- if $N(\tilde A)=0$ the line lies in the cone $\{N=0\}$ and meets neither of the other two levels;
- if $N(\tilde A)\neq0$ and $\lambda\neq0$ the line meets the level $\{N=\lambda\}$ in the two points $t=\pm\sqrt{\lambda/N(\tilde A)}$;
- if $N(\tilde A)\neq0$ and $\lambda=0$ the line meets the cone only at the origin.

Consequently the two non-central levels are carried onto one another by the scalings, the scaling $\tilde P\mapsto\mu\tilde P$ carrying $\{N=\lambda\}$ onto $\{N=\mu^2\lambda\}$, and the three sets are pairwise disjoint and cover the level set $\{N\in\{-1,0,1\}\}$.

*Proof.* The display is the homogeneity $N(t\tilde A)=t^2N(\tilde A)$ of the diagonal; the two solutions of $t^2=\lambda/N(\tilde A)$ give two points unless $\lambda=0$; disjointness is that a scalar has one of the three values and not two.

**Remark (the sizes).** The two non-central levels are affine hyperquadrics of complex dimension three; the cone is their common asymptotic object at the origin, because $N$ is homogeneous; and the scaling $\tilde P\mapsto\lambda\tilde P$ carries the level $1$ onto the level $\lambda^2$ for every $\lambda$, so the family of non-central levels is a single orbit of the scalings and the three values $-1$, $+1$ and any other nonzero value give algebraically isomorphic sets.

## The Relation to the Idempotents and to the Zero Divisors

**Theorem (the affine map, and the failure of the bijection).** In the block the map

$$
\tilde P\ \longmapsto\ \tilde\Pi=\tfrac12(e_0+\tilde P)
$$

carries the roots of $+1$ that are **central** — that is $\tilde P=\pm e_0$ — onto the idempotents $e_0$ and $0$, and it carries **no other root of $+1$** to an idempotent. There is therefore no bijection between the roots of $\pm1$ and the idempotents of the block.

*Proof.* $\tilde\Pi\star\tilde\Pi=\tfrac14(e_0\star e_0+2\tilde P\star e_0+\tilde P\star\tilde P)=\tfrac14\bigl(1+2P_0+N(\tilde P)\bigr)e_0$, while $\tilde\Pi=\tfrac12e_0+\tfrac12\tilde P$. The two are equal only if $\tilde P$ is central, $\tilde P=P_0e_0$, and then the equality reads $\tfrac14(1+2P_0+P_0^2)=\tfrac12(1+P_0)$, that is $(1+P_0)(P_0-1)=0$, or $P_0^2=1$. For a central root of $+1$ the value $P_0=1$ gives $\tilde\Pi=e_0$ and $P_0=-1$ gives $\tilde\Pi=0$; for a non-central root of $+1$, of which the level set is full, no value of the scalar part repairs the failure.

**The parent's map, and why it fails here.** In the parent the map acts on the roots of $-1$ through $\tilde\Pi=\tfrac12(e_0+\xi i)$, because the product is associative and unital and because $(\xi i)^2=1$ results from $\xi^2=-1$ and $i^2=-1$ (*Idempotents of the General Plain Algebra*). In the block the associativity and the unit are absent, and for a pure root $\xi$, with $N(\xi)=1$, the same element $\xi i$ has $N(\xi i)=i^2N(\xi)=-1$, so that the block reads it as a root of $-1$ and not of $+1$; the computation of $\tilde\Pi\star\tilde\Pi$ stops at the central element $\tfrac12(1+P_0)e_0$ and cannot produce the vector part of $\tilde\Pi$.

**The relation to the zero divisors.** The roots of $0$ are exactly the isotropic elements, hence exactly the square-zero elements of the block and exactly the zero divisors of the parent algebra: $\{N=0\}\setminus\{0\}=\mathcal{Z}_{\tilde P\tilde Q}$ (*Zero Divisors of the Symmetric Quaternionic Algebra*). The block's own zero-divisor set is the whole punctured space, so the roots of $0$ are a proper subset of it, and the equality of the two notions, valid in the parent, fails in the same way as the bijection with the idempotents.

## Summary

In the symmetric quaternionic product the square is the diagonal of the form, $\tilde P\star\tilde P=N(\tilde P)e_0$ with $N(\tilde P)=P_0^2+(\mathbf P,\mathbf P)$, so the roots of $-1$, of $0$ and of $+1$ are the three level sets $N=-1$, $N=0$ and $N=1$ of one quadratic form: a pair of affine hyperquadrics of complex dimension three and the cone between them, pairwise disjoint, invariant under the three conjugations, and related by the scaling $\tilde P\mapsto\mu\tilde P$ with $N(\mu\tilde P)=\mu^2N(\tilde P)$. The roots of $-1$ are parametrised by $P_0^2=-1-(\mathbf P,\mathbf P)$ and contain the two central roots $\pm ie_0$; the roots of $0$ are exactly the square-zero elements and the isotropic cone, hence exactly the zero divisors of the parent algebra; the roots of $+1$ contain the four basis elements and the level set $N=1$ on the Hermitian subspaces. The affine map $\tilde\Pi=\tfrac12(e_0+\tilde P)$ of the parent carries only the two central roots of $+1$ to the idempotents $e_0$ and $0$ and no other, so the bijection between the roots and the idempotents fails in the block; and the identification of the roots of $0$ with the zero divisors holds only for the parent and not for the block, whose zero-divisor set is the whole punctured space.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ | the symmetric quaternionic multiplication |
| $N(\tilde P)=P_0^2+(\mathbf P,\mathbf P)=\sum_\mu P_\mu^2$ | the diagonal of the form, the norm of the parent |
| $N=-1$, $N=0$, $N=1$ | the roots of $-1$, of $0$, of $+1$ |
| $(\mathbf P,\mathbf P)=0$ | the cone condition of the vector part for the level $0$ |
| $e_0,e_1,e_2,e_3$ | the four roots of $+1$ of the basis |
| $\pm ie_0$ | the two central roots of $-1$ |
| $\tilde\Pi=\tfrac12(e_0+\tilde P)$ | the affine map of the parent, defined but not bijective in the block |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the general definition of a root of a central value.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the parallel classification in the parent.
- *Square Roots of a General Element in the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-symmetric-quaternionic-algebra.md`), for the radicands that are not central.
- *Nilpotents of the Symmetric Quaternionic Algebra* (`articles_maths/nilpotents-of-the-symmetric-quaternionic-algebra.md`), for the roots of $0$ as the square-zero elements of index two.
- *Idempotents of the Symmetric Quaternionic Algebra* (`articles_maths/idempotents-of-the-symmetric-quaternionic-algebra.md`), for the failure of the bijection.
- *Norm and Invertibility in the Symmetric Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-quaternionic-algebra.md`), for the diagonal and the non-isotropic class.
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), for the cone and its two families.
