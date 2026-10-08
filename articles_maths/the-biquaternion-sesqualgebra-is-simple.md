
# __The Biquaternion Sesqualgebra Is Simple__

## Introduction

The general plain sesquilinear product $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ makes $\mathbb{B}$ a sesqualgebra by *Introduction to the General Plain Sesqualgebra of Biquaternions*, and the two-sided ideals of that multiplication are the two trivial ones,

$$
0 \quad\text{and}\quad \mathbb{B} .
$$

This article proves the statement in full. The proof is a single computation: a two-sided ideal of the multiplication is a two-sided ideal of the algebra, because in a unital derived model the involution drags the conjugate of an element into every ideal it lies in; and the algebra $\mathbb{B}$ is a full matrix algebra over $\mathbb{C}$, which has no proper two-sided ideal. So one nonzero element of a two-sided ideal generates a nonzero two-sided ideal of the algebra, which is the whole algebra, and the ideal contains the unit.

The article is the third of the structural batch: the element theory is *Projections of the Biquaternion Sesqualgebra*, the square theory is *The Squares and the Positive Cone of the Biquaternion Sesqualgebra*, and the structure theory of the ideals is here. The general theory that it reads is *Ideals and Quotients of a Sesqualgebra*, where the one-sided and two-sided ideals of a sesqualgebra are defined, and *Simple Sesqualgebras and Minimal Ideals*, where the two notions of simplicity are compared and the one-sided case is treated. On the biquaternion side the two-sided ideals of the algebra and the simplicity of the ring are *Biquaternion Ideals and Peirce Decomposition*, and the minimal one-sided ideals of the algebra and the idempotents that determine them are the same article.

The setting is that of *Introduction to the General Plain Sesqualgebra of Biquaternions*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the unit, and the multiplication $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ with ${}^{*}$ the conjugate-linear involution. The two halves of the involution are the subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ of *Hermitian and Skew-Hermitian Elements*, and the ideal theory of the general sesqualgebra is the one that is applied.

## Ideals of the Multiplication

### The Definitions

**Definition.** A **left ideal** of the multiplication is an $R$-submodule $I\subseteq\mathbb{B}$ with $\mathbb{B}\star I\subseteq I$; a **right ideal** is an $R$-submodule with $I\star\mathbb{B}\subseteq I$; a **two-sided ideal** is an $R$-submodule with both. The **conjugate image** of a subset $I$ is $I^{*}=\{\tilde X^{*}:\tilde X\in I\}$, and a **$\ast$-ideal** is a two-sided ideal with $I^{*}\subseteq I$.

**Remark.** The definitions are those of *Ideals and Quotients of a Sesqualgebra*, §*Ideals*, read on $\mathbb{B}$ with the multiplication $\star$. The scalar-closure clause is automatic in the unital case, by the proposition of that article on the unital case, so the three notions are the plain product-closed ones here, the unit being $e_0$ on the right.

### Two-Sided $\star$-Ideals Are $\ast$-Ideals

**Theorem.** A two-sided ideal of the multiplication is stable under the involution, so the two-sided $\star$-ideals of $\mathbb{B}$ and the $\ast$-ideals of $\mathbb{B}$ are the same class.

**Proof.** This is the theorem of *Simple Sesqualgebras and Minimal Ideals*, §*The Two Notions Coincide in the Derived Model*, applied to the derived model $\tilde X\star\tilde Y=\tilde X\tilde Y^{*}$ with the unit $e_0$. The one computation is $\tilde X^{*}=e_0\star\tilde X$ for an element of a two-sided ideal, which lies in $\mathbb{B}\star I\subseteq I$ and so drags the conjugate into the ideal; the involution is then of order two and gives equality. With stability in hand the $\star$-conditions read $\mathbb{B}I\subseteq I$ and $I\mathbb{B}\subseteq I$, so a two-sided $\star$-ideal is a two-sided algebra ideal as well, that is, a $\ast$-ideal; and conversely an $\ast$-ideal satisfies the $\star$-conditions because $\mathbb{B}\star I=\mathbb{B}I^{*}=\mathbb{B}I\subseteq I$. $\square$

**Remark.** The stability is what a general sesqualgebra need not have, and *Ideals and Quotients of a Sesqualgebra* records the example of the principal ideal that is not stable; the derived model with a unit is exactly the case in which the involution is strong enough to close the gap. On $\mathbb{B}$ the theorem says that the two-sided ideals of the multiplication are the $\ast$-stable two-sided algebra ideals, and the next section computes them.

## The Simplicity Theorem

### The Statement

**Theorem.** The two-sided ideals of the sesquilinear multiplication on $\mathbb{B}$ are $0$ and $\mathbb{B}$; in the terminology of *Simple Sesqualgebras and Minimal Ideals*, the sesqualgebra $(\mathbb{B},\star)$ is **simple** and invariant-simple.

**Proof.** A two-sided $\star$-ideal is an $\ast$-ideal by §*Ideals of the Multiplication*, hence a two-sided algebra ideal. The algebra ideals of $\mathbb{B}$ are $0$ and $\mathbb{B}$, by *Biquaternion Ideals and Peirce Decomposition*, §*The Two-Sided Ideals: Simplicity of $\mathbb{B}$*, because $\mathbb{B}$ is a full two-by-two matrix algebra over the field $\mathbb{C}$ and such an algebra has no proper two-sided ideal. So the two-sided $\star$-ideals are $0$ and $\mathbb{B}$. Simplicity is the definition, and invariant-simplicity follows from it. $\square$

**Remark.** The proof is a transport and not a new computation, and it is the transport that the article makes explicit. The direct form of the argument, which uses one element and the unit criterion, is the next two subsections.

### The Proof from One Element and the Unit Criterion

**Proposition (the unit criterion).** A two-sided ideal of an algebra with a unit that contains a unit is the whole algebra.

**Proof.** If $I$ contains the unit $e_0$ then for every $\tilde X$ one has $\tilde X=\tilde X e_0\in I\mathbb{B}\subseteq I$, so $I=\mathbb{B}$. The general-algebra form is the unit criterion for ideals. $\square$

**Proposition (one element generates the algebra).** Let $I$ be a two-sided $\star$-ideal of $\mathbb{B}$ and let $0\neq\tilde X\in I$. Then $I=\mathbb{B}$.

**Proof.** By stability, $I$ is a two-sided algebra ideal. The set
$$
\mathbb{B}\,\tilde X\,\mathbb{B}=\Bigl\{\sum_{i}\tilde A_i\tilde X\tilde B_i\Bigr\}
$$
is a two-sided algebra ideal, it contains $\tilde X$, and it is contained in $I$ because $I$ is two-sided. Since $\tilde X\neq0$, the ideal $\mathbb{B}\tilde X\mathbb{B}$ is nonzero, and the only nonzero two-sided ideal of $\mathbb{B}$ is $\mathbb{B}$ itself, by *Biquaternion Ideals and Peirce Decomposition*; hence $\mathbb{B}\tilde X\mathbb{B}=\mathbb{B}$. The unit criterion now gives $e_0\in I$ and $I=\mathbb{B}$. $\square$

**Corollary.** A nonzero two-sided $\star$-ideal contains the unit, and the two-sided $\star$-ideals are exactly $0$ and $\mathbb{B}$.

**Proof.** The proposition shows that every nonzero two-sided $\star$-ideal is $\mathbb{B}$, and the unit criterion is the mechanism. $\square$

**Remark.** The argument is the one the group article compresses: one element of an ideal, the algebra's simplicity, and the unit criterion. The element $\tilde X$ is used only through the nonzero two-sided ideal it generates, and the generation is the content of the algebra's simplicity; the involution is used only to pass from the multiplication to the algebra.

### The Quotients

**Corollary.** The only quotients of the sesqualgebra by two-sided ideals are the zero sesqualgebra and the sesqualgebra itself.

**Proof.** The two-sided ideals are $0$ and $\mathbb{B}$, and $\mathbb{B}/0=\mathbb{B}$ while $\mathbb{B}/\mathbb{B}=0$. $\square$

**Remark.** A sesqualgebra that is simple has no nontrivial quotient, so the whole of the representation theory of $\mathbb{B}$ is the theory of $\mathbb{B}$ itself. The corresponding statement for the algebra is the same, and it is the reason the four products of the corpus all live on one algebra and not on a family of quotients.

## The Lattice of Ideals

### The Two-Sided Lattice

| ideal | of the multiplication $\star$ | of the algebra $\tilde P\tilde Q$ |
|---|---|---|
| zero | $0$ | $0$ |
| whole | $\mathbb{B}$ | $\mathbb{B}$ |
| proper nonzero two-sided | none | none |
| proper nonzero $\ast$-ideal | none | none |

**Remark.** The two-sided lattice is the same for the two products, and it is the trivial lattice of two elements. The agreement is the coincidence theorem of the derived model; it is not automatic, and *Simple Sesqualgebras and Minimal Ideals* records an algebra over a finite field where the two-sided ideals of the derived product are strictly fewer than the two-sided algebra ideals.

### The Involution Swaps the Two Sides

**Proposition.** The conjugate image of a left $\star$-ideal is a right $\star$-ideal and conversely, and the conjugate image of a two-sided $\star$-ideal is two-sided.

**Proof.** The statement for the algebra ideals is *Ideals and Quotients of a Sesqualgebra*, §*The Involution Swaps the Two Sides*: for a left ideal $I$ one has $\tilde X^{*}\tilde A=(\tilde A^{*}\tilde X)^{*}\in I^{*}$, so $I^{*}$ is a right ideal. The $\star$-conditions are the algebra conditions on the conjugate, by the theorem of §*Ideals of the Multiplication*, so the statement carries over to the multiplication. $\square$

**Remark.** The involution is the map that identifies the two sides, so a one-sided $\star$-ideal and its conjugate image are a left and a right ideal of the same size. In $\mathbb{B}$ the two sides are exchanged by ${}^{*}$ between the left and right ideals generated by the projections of *Projections of the Biquaternion Sesqualgebra*.

### The One-Sided Ideals

**Theorem.** A one-sided $\star$-ideal of a derived model with a unit is stable under the involution; consequently the one-sided $\star$-ideals of $\mathbb{B}$ are exactly the stable one-sided algebra ideals.

**Proof.** The stability is *Simple Sesqualgebras and Minimal Ideals*, §*The One-Sided Case*: for a left $\star$-ideal $I$ and $\tilde X\in I$ one has $\tilde X^{*}=e_0\star\tilde X\in\mathbb{B}\star I\subseteq I$; the right case is the same on the other side, and the two-sided case is the two together. With $I^{*}=I$ the $\star$-condition $\mathbb{B}\star I\subseteq I$ reads $\mathbb{B}I^{*}=\mathbb{B}I\subseteq I$, which is the left algebra condition; conversely a stable left algebra ideal satisfies $\mathbb{B}\star I=\mathbb{B}I^{*}=\mathbb{B}I\subseteq I$. $\square$

**Proposition (no proper one-sided $\star$-ideal).** The only left $\star$-ideals of $\mathbb{B}$ are $0$ and $\mathbb{B}$, and the same for the right ideals.

**Proof.** A left $\star$-ideal is a stable left algebra ideal by the theorem. A proper nonzero left ideal of the full matrix algebra $M_2(\mathbb{C})$, hence of $\mathbb{B}$, is the set of the matrices whose kernel contains a fixed line, by *Biquaternion Ideals and Peirce Decomposition*, §*The Lattice of Left Ideals*; its conjugate image is a right ideal of the same dimension, and it differs from the left ideal, because a set that is both a left and a right ideal is a two-sided ideal and the proper nonzero two-sided ideals do not exist in $\mathbb{B}$. Hence no proper nonzero left algebra ideal is stable and the only left $\star$-ideals are $0$ and $\mathbb{B}$. The right case is the same under the involution. $\square$

**Corollary (a single element generates the sesqualgebra).** For every $0\neq\tilde X$ the smallest left $\star$-ideal containing $\tilde X$ is $\mathbb{B}$, and the same on the right.

**Proof.** Let $I$ be the smallest left $\star$-ideal containing $\tilde X$. By the stability of one-sided $\star$-ideals, $I$ is stable and so contains $\tilde X^{*}$; hence it contains the left algebra ideal $\mathbb{B}\star\tilde X=\mathbb{B}\tilde X^{*}$, and, being stable, it also contains its conjugate image $\tilde X\mathbb{B}$. As a left ideal $I$ then contains $\mathbb{B}(\tilde X\mathbb{B})=\mathbb{B}\tilde X\mathbb{B}$, the two-sided algebra ideal generated by $\tilde X$, which is $\mathbb{B}$ because $\tilde X\neq0$ and the algebra is simple. Hence $I=\mathbb{B}$. The right case is the same. $\square$

**Remark.** The one-sided theory is therefore sharper than the two-sided one: not only are there no proper two-sided $\star$-ideals, there are no proper one-sided ones either, and every nonzero element is a one-sided generator. This is a property of the multiplication and not of the algebra, and the next section isolates the contrast.

### The Algebra's Minimal One-Sided Ideals

**Recall.** The minimal left algebra ideals of $\mathbb{B}$ are the spaces $\mathbb{B}\tilde\Pi$ over the primitive idempotents $\tilde\Pi$, equivalently the spaces $\mathbb{B}\tilde X$ over the nonzero elements $\tilde X$ whose square vanishes, by *Biquaternion Ideals and Peirce Decomposition*, §*The Decomposition into Minimal Left and Right Ideals* and *Biquaternion Zero Divisors*.

**Proposition.** A minimal left algebra ideal of $\mathbb{B}$ is not a left $\star$-ideal.

**Proof.** A minimal left algebra ideal is $\mathbb{B}\tilde\Pi$ with $\tilde\Pi$ a primitive idempotent. Its conjugate image is $(\mathbb{B}\tilde\Pi)^{*}=\tilde\Pi^{*}\mathbb{B}$, a minimal right ideal, and it equals $\mathbb{B}\tilde\Pi$ only if $\tilde\Pi$ is central, which no primitive idempotent of $\mathbb{B}$ is, the centre being $\mathbb{C}e_0$ and the primitive idempotents the elements $\tilde\Pi(\xi)$ and the projections. So the ideal is not stable and, by the stability of one-sided $\star$-ideals, it is not a left $\star$-ideal. $\square$

**Remark.** The elements of the algebra therefore determine a rich lattice of minimal one-sided ideals, one for each primitive idempotent and one for each zero divisor, and the multiplication keeps none of them: the passage from the algebra to the sesqualgebra collapses the one-sided lattice to the two trivial elements. The contrast of the two lattices is the one-sided face of the simplicity of the sesqualgebra.

## The Centre and the Field

**Theorem.** The centre of $\mathbb{B}$ is $\mathbb{C}e_0$, a field, and the only central idempotents are $0$ and $e_0$.

**Proof.** The centre of the full matrix algebra is the scalar multiples of the identity, transported to $\mathbb{C}e_0$ by *Biquaternion $2\times2$ Matrix Element Representation* and *Biquaternion Ideals and Peirce Decomposition*; the centre of a field is a field, and $\mathbb{C}e_0$ is identified with $\mathbb{C}$. A central idempotent $\tilde Z$ satisfies $\tilde Z(1-\tilde Z)=0$ and, being central, generates the two-sided ideal $\mathbb{B}\tilde Z$; since the only two-sided ideals are $0$ and $\mathbb{B}$, the idempotent is $0$ or $e_0$. $\square$

**Remark.** The centre is the field of scalars of the algebra, so $\mathbb{B}$ is a **central** simple algebra, in the sense of *Central Simple Algebras and the Brauer Group*; the two-sided simplicity and the trivial centre are the two halves of that notion.

## Summary

The two-sided ideals of the sesquilinear multiplication on $\mathbb{B}$ are $0$ and $\mathbb{B}$: in the unital derived model a two-sided $\star$-ideal is stable under the involution and hence a two-sided algebra ideal, and the algebra is a full matrix algebra with no proper two-sided ideal; directly, one nonzero element of a two-sided $\star$-ideal generates the nonzero two-sided algebra ideal $\mathbb{B}\tilde X\mathbb{B}=\mathbb{B}$, so the ideal contains the unit and is the whole algebra. The sesqualgebra is therefore simple and invariant-simple, its only quotients are itself and zero, and its one-sided theory is even sharper: a one-sided $\star$-ideal is stable, hence a stable one-sided algebra ideal, and $\mathbb{B}$ has no proper one-sided algebra ideal that is stable, so the only one-sided $\star$-ideals are $0$ and $\mathbb{B}$ and every nonzero element generates the whole sesqualgebra on either side. The algebra's own minimal one-sided ideals, determined by the primitive idempotents and the zero divisors, are not ideals of the multiplication, and the two-sided lattices of the two products coincide by the coincidence theorem of the derived model.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | the sesquilinear multiplication |
| $I^{*}=\{\tilde X^{*}:\tilde X\in I\}$ | the conjugate image of a subset |
| left, right, two-sided $\star$-ideal | an $R$-submodule closed under $\mathbb{B}\star\cdot$, $\cdot\star\mathbb{B}$, or both |
| $\ast$-ideal | a two-sided algebra ideal with $I^{*}\subseteq I$ |
| $\mathbb{B}\tilde X\mathbb{B}$ | the two-sided algebra ideal generated by $\tilde X$ |
| $\mathbb{B}\tilde\Pi$ | a minimal left algebra ideal, $\tilde\Pi$ primitive |
| $Z(\mathbb{B})=\mathbb{C}e_0$ | the centre, a field |
| $e_0$ | the unit and the two-sided generator of the unit criterion |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the two-sided ideals of an involutive ring and their stability under the involution.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society Colloquium Publications 37, 1956), for the simplicity of a full matrix ring, the lattice of one-sided ideals and the unit criterion.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the central simple algebras, their centres and their two-sided ideals.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the ideal lattice of a finite-dimensional algebra, the minimal one-sided ideals and the idempotents that determine them.
- Joseph J. Rotman, *Advanced Modern Algebra* (American Mathematical Society, 2015), for the module-theoretic treatment of the one-sided ideals of a matrix algebra.
