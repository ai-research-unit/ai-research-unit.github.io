# __Idempotents of the Symmetric Quaternionic Algebra__

## Introduction

An idempotent is an element equal to its own square, and in the block the square is the diagonal of the form, $\tilde x\star\tilde x=N(\tilde x)e_0$. The two conditions together force the element onto the scalar line, and there the only solutions are $0$ and $e_0$. The idempotent set of the block is therefore the pair $\{0,e_0\}$: there is no non-trivial idempotent. The collapse that over $\mathbb{R}$ removes the roots of the central value $-e_0$ and reduces the root sets of a central value removes here the continuum of idempotents that the complexified parent plain algebra carries; the block has no idempotent in the vector subspace, none off the centre, no Peirce decomposition and no classification of the zero divisors by idempotents. This article proves the classification, compares it with the parent plain algebra, reads the two idempotents as operators, and records the absences.

**Boundaries.** The definition of an idempotent and of the orthogonality of idempotents is *Definitions for the Study of the 6 Algebraic Structures*; the product and its scalar law are *Introduction to the Symmetric Quaternionic Algebra of Quaternions*; the radical and the isotropic elements are *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*; the roots of $\pm e_0$ and of $0$ are *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra*; the multiplication operators and the classification of the idempotent operators are *The Multiplication Operators of the Symmetric Quaternionic Algebra*, and the collected element classes are *The Specificities of the Symmetric Quaternionic Algebra*; the zero divisors are *Zero Divisors of the Symmetric Quaternionic Algebra*; the parent's idempotents, the complexified continuum, are *Idempotents of the General Plain Algebra*, and the biquaternion twin is *Idempotents of the Symmetric Quaternionic Algebra*.

**Conventions.** The algebra is $\mathbb{H}$ over $\mathbb{R}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$; an element is $\tilde x=x_0e_0+\mathbf x$. The **quaternion conjugation** is $\tilde x^{\natural}=x_0e_0-\mathbf x$; the bar is the identity, the star coincides with the natural sign ${}^{\natural}$. The **quaternion form** is $N(\tilde p,\tilde q)=p_0q_0+\mathbf p\cdot\mathbf q$, its diagonal is $N(\tilde x)=x_0^{2}+|\mathbf x|^{2}$, and the **symmetric quaternionic product** is $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$. The centre is $\mathbb{R}e_0$ and the vector subspace is $\mathrm{Vect}(\mathbb{H})=\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$.

## The General Definition

**Definition (idempotent).** An **idempotent** of a real-bilinear rule is an element $\tilde\Pi$ with $\tilde\Pi^{2}=\tilde\Pi$, that is $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ in the block. The set of the idempotents contains $0$, since $0\star0=0$, and it contains the two-sided unit when the rule has one; an idempotent different from $0$ is **non-trivial**. Two idempotents $\tilde\Pi,\tilde\Pi'$ are **orthogonal** when $\tilde\Pi\star\tilde\Pi'=\tilde\Pi'\star\tilde\Pi=0$, and the **complement** of an idempotent is defined only when the rule has a two-sided unit $e$, the complement of $\tilde\Pi$ being $e-\tilde\Pi$.

The definition is quoted, and the article now reads it on the block.

## The Classification

**Theorem (the idempotents).** An element $\tilde x$ satisfies $\tilde x\star\tilde x=\tilde x$ if and only if $\tilde x\in\{0,e_0\}$.

*Proof.* The square of the block is $\tilde x\star\tilde x=N(\tilde x)e_0=(x_0^{2}+|\mathbf x|^{2})e_0$, while $\tilde x=x_0e_0+\mathbf x$; the equality of the two elements forces the vector part of the right-hand side to vanish, hence $\mathbf x=0$, and then the scalar equation $x_0^{2}=x_0$, whose solutions are $x_0=0$ and $x_0=1$. Both are idempotents: $0\star0=0$ and $e_0\star e_0=N(e_0)e_0=e_0$.

**Corollary (no non-trivial idempotent).** The block has exactly two idempotents, and both are central. There is no idempotent in the vector subspace and none outside the centre; every idempotent of the block lies on the scalar line.

*Proof.* The classification gives the pair; the scalar line is the centre.

**Remark (the same pair, reached differently in the companion block).** The symmetric plain algebra has the same two idempotents, $0$ and $e_0$, but reaches them by the square of the plain product and not by the diagonal of the form; the block's proof is short, because the square of the block is scalar and the vector part is annihilated at the first step (*The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*).

## The Relation to the Roots of Plus and Minus One

The complexified parent plain algebra reaches its idempotents through the affine map $\tilde\Pi=\tfrac12(e_0+\tilde\Xi i)$, the parameter $\tilde\Xi$ running over the roots of $-e_0$: the idempotents form the continuum $\tfrac12(e_0+\tilde\Xi i)$, of real dimension four, a two-sphere when $\tilde\Xi$ ranges over the unit pure quaternions, and the two trivial idempotents are the images of the two degenerate roots $\tilde\Xi=\pm i$, since $\tfrac12(e_0+i\cdot i)=0$ and $\tfrac12(e_0-i\cdot i)=e_0$ (*Idempotents of the General Plain Algebra*). Over $\mathbb{R}$ the coordinate $i$ is gone and the map collapses: the block has no root of $-e_0$ at all, and among the roots of $+e_0$ only the two central ones reach an idempotent. The biquaternion twin *Idempotents of the Symmetric Quaternionic Algebra* records the same pair $\{0,e_0\}$ for the block over $\mathbb{C}$, the continuum being the plain parent's and not the block's.

**Proposition (the affine map and the roots of $+e_0$).** Let $\tilde\Pi=\tfrac12(e_0+\tilde x)$. Then $\tilde\Pi\star\tilde\Pi=\tfrac14\bigl(1+2x_0+N(\tilde x)\bigr)e_0$, and $\tilde\Pi$ is idempotent if and only if $\tilde x=\pm e_0$. The two roots of $+e_0$ that are central, $\tilde x=e_0$ and $\tilde x=-e_0$, give the two idempotents $\tilde\Pi=e_0$ and $\tilde\Pi=0$; every noncentral root of $+e_0$ gives a non-idempotent, and the roots of $-e_0$ do not exist.

*Proof.* The square of a half-sum is read on the form, $\tilde\Pi\star\tilde\Pi=\tfrac14N(e_0+\tilde x)e_0$, and $N(e_0+\tilde x)=N(e_0)+2N(e_0,\tilde x)+N(\tilde x)=1+2x_0+N(\tilde x)$. The equality $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ reads $\tfrac14(1+2x_0+N(\tilde x))e_0=\tfrac12(e_0+\tilde x)$; comparing the vector parts gives $\mathbf x=0$, so $\tilde x=x_0e_0$, and the scalar equation $(1+x_0)^{2}=2(1+x_0)$, whose solutions are $x_0=-1$ and $x_0=1$. Thus $\tilde x=\pm e_0$, both being roots of $+e_0$; the value $\tilde x=e_0$ gives $\tilde\Pi=e_0$ and the value $\tilde x=-e_0$ gives $\tilde\Pi=0$. The roots of $-e_0$ are empty in the block, so no idempotent arises from them. The noncentral roots of $+e_0$ are the remaining points of the sphere $Sp(1)$; for such a root $\mathbf x\neq0$ and the vector part of $\tilde\Pi$ does not vanish, so $\tilde\Pi\star\tilde\Pi=\tfrac14(1+2x_0+N(\tilde x))e_0$ is scalar and cannot equal the noncentral $\tilde\Pi$.

**Example (an explicit noncentral root).** For $\tilde x=e_1$ the element $\tilde\Pi=\tfrac12(e_0+e_1)$ has the square $\tfrac14N(e_0+e_1)e_0=\tfrac14\cdot2\,e_0=\tfrac12e_0$, which is not $\tilde\Pi$; the failure of the bridge is the failure of the centrality of $\tilde\Pi$.

**Remark (the roots of $-e_0$ are not available).** Over $\mathbb{R}$ the branch of the affine map that the complex chapter feeds from the roots of $-e_0$ is empty, because $-e_0$ has no square root (*Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra*). The block therefore has no idempotent built from a root of $-e_0$, and the only roots that reach an idempotent are the two central roots of $+e_0$.

## The Idempotents as Projections

**Definition (left multiplication).** For an element $\tilde x$ the **left multiplication** $L_{\tilde x}$ is the endomorphism of $\mathbb{H}$ given by $L_{\tilde x}(\tilde y)=\tilde x\star\tilde y=N(\tilde x,\tilde y)e_0$.

**Theorem (the operator of an idempotent).** For every $\tilde x$ the operator $L_{\tilde x}$ has the square $L_{\tilde x}^{2}=x_0L_{\tilde x}$, so it is idempotent exactly when $\tilde x=0$ or $x_0=1$; among the nonzero elements, exactly the elements of scalar coordinate $1$. The idempotent element $e_0$ gives the operator

$$
L_{e_0}=E:\tilde y\mapsto y_0e_0,
$$

the projection onto the centre along the vector subspace: $E^{2}=E$, the image of $E$ is $\mathbb{R}e_0$, its kernel is $\mathrm{Vect}(\mathbb{H})$, and it is not the identity.

*Proof.* The composition is $L_{\tilde x}(L_{\tilde x}\tilde y)=N(\tilde x,y_0e_0)e_0=x_0y_0e_0=x_0L_{\tilde x}\tilde y$, using $N(\tilde x,e_0)=x_0$; hence $L_{\tilde x}^{2}=x_0L_{\tilde x}$, which equals $L_{\tilde x}$ exactly when $x_0=1$ or when $L_{\tilde x}=0$, the latter only at $\tilde x=0$. For $\tilde x=e_0$ the operator is $E(\tilde y)=N(e_0,\tilde y)e_0=y_0e_0$, whose image and kernel are as displayed; it is not the identity because $E(e_1)=0\neq e_1$, the block having no unit.

**Remark (idempotent elements against idempotent operators).** The idempotent elements are only $0$ and $e_0$, and their operators are the zero operator and $E$. The idempotent **operators** are the larger family made of the zero operator $L_0$ together with the $L_{\tilde x}$ of scalar coordinate $1$: the latter form a hyperplane, parallel to the vector subspace, of pairwise distinct rank-one projections onto the centre. The two families are different, and the operator family is classified in *The Multiplication Operators of the Symmetric Quaternionic Algebra*, where the operators form an algebra whose idempotents are $0$ and the elements of scalar coordinate $1$.

## The Relation to the Zero Divisors

**Proposition (no classification by idempotents).** In the complex parent the non-trivial idempotents classify the zero divisors and read a Peirce decomposition; over $\mathbb{R}$ neither survives. The real parent is a division algebra, with no zero divisor and only the two trivial idempotents, and the block has only those same two idempotents while its own zero-divisor set is the whole punctured space $\mathbb{H}\setminus\{0\}$ (*Zero Divisors of the Symmetric Quaternionic Algebra*): no idempotent can distinguish one zero divisor from another, the classification by idempotents being empty because the idempotents are trivial, and the zero-divisor set maximal at the same time.

*Proof.* The idempotents are $0$ and $e_0$; a classification by non-trivial idempotents therefore has no entry; the zero-divisor set is the punctured space, which contains every nonzero element.

**Remark (the absent complementation).** The complementation $\tilde\Pi\mapsto e_0-\tilde\Pi$ and the orthogonality of idempotents are not defined for the block: the complement of an idempotent requires a two-sided unit, and the block has none. The two idempotents do satisfy $0\star e_0=0$, but there is no complete orthogonal system of idempotents and no Peirce decomposition, the available splitting

$$
\mathbb{H}=\mathbb{R}e_0\oplus\mathrm{Vect}(\mathbb{H})
$$

being the image–kernel splitting of $E$ and not a decomposition into corner algebras. This is the idempotent reading of the absence of a unit, and it is the reason the block has no idempotent calculus beyond the two elements.

## Summary

The idempotents of the symmetric quaternionic block are exactly $0$ and $e_0$: the equation $\tilde x\star\tilde x=N(\tilde x)e_0=\tilde x$ forces the vector part of $\tilde x$ to vanish and the scalar part to satisfy $x_0^{2}=x_0$, so both idempotents are central and there is no non-trivial one. The continuum of idempotents of the complexified parent plain algebra, the family $\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-e_0$, has no counterpart in the block: the affine map $\tilde\Pi=\tfrac12(e_0+\tilde x)$ carries no root of $-e_0$, because the block has none, and of the roots of $+e_0$ only the two central ones, $\pm e_0$, to the pair $e_0$ and $0$; a noncentral root gives only a scalar square and not an idempotent, the biquaternion twin records the same pair for the block, and the real parent's own two idempotents are the same pair. The idempotent $e_0$ acts by the projection $E$ onto the centre along the vector subspace, which is not the identity, and the idempotent operators are a larger family than the idempotent elements. The block has no Peirce decomposition, no complementation and no classification of the zero divisors by idempotents; the complementation and the orthogonality that the complex parent's theory uses require the unit that the block does not have.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ | the idempotent equation |
| $\{0,e_0\}$ | the idempotents of the block |
| $\tilde\Pi=\tfrac12(e_0+\tilde x)$ | the affine map of the parent, idempotent only at $\tilde x=\pm e_0$ |
| $Sp(1)=\{\tilde u:N(\tilde u)=1\}$ | the roots of $+e_0$; only $\pm e_0$ give idempotents |
| $L_{\tilde x}^{2}=x_0L_{\tilde x}$ | the square of a left multiplication |
| $E=L_{e_0}:\tilde y\mapsto y_0e_0$ | the projection onto the centre, not the identity |
| $\mathbb{H}=\mathbb{R}e_0\oplus\mathrm{Vect}(\mathbb{H})$ | the image–kernel splitting of $E$, not a Peirce decomposition |

## Further Reading

- *Definitions for the Study of the 6 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-6-algebraic-structures.md`), for the idempotent, the orthogonal idempotents and the complementation
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra-of-quaternions.md`), for the same two-point class over the division algebra $\mathbb{H}$, reached by the plain equation
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra.md`), the complexified parent, for the continuum $\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-e_0$, of real dimension four
- *Idempotents of the Symmetric Quaternionic Algebra* (`articles_maths/idempotents-of-the-symmetric-quaternionic-algebra.md`), the biquaternion twin, which records the same pair $\{0,e_0\}$ for the block over $\mathbb{C}$ and locates the continuum in the plain parent
- *The Specificities of the Symmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), where the idempotents and the nilpotents are collected
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the operators $L_{\tilde x}$, the projection $E$ and the classification of the idempotent operators
- *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the roots of $+e_0$ and the emptiness of the roots of $-e_0$
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the maximal zero-divisor set that makes the classification by idempotents vacuous
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for idempotents, orthogonality and the Peirce decomposition.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, Universitext, 2004), for the flexibility and power-associativity of a symmetric product.
