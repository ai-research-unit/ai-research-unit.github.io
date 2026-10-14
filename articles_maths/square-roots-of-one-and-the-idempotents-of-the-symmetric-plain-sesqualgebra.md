# __Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ on the biquaternion space (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*). This article determines the **roots of one**, the nonzero elements $\tilde\Xi$ with $\tilde\Xi\star\tilde\Xi = e_0$, and then the **idempotents**, the elements $\tilde\Pi$ with $\tilde\Pi\star\tilde\Pi = \tilde\Pi$. The order is fixed: the roots of one come first and the idempotents after, because the idempotent architecture rests on the roots of one alone. The roots of $-1$ are a short remark closing the roots-of-one part, and nothing later uses them.

The two subjects are joined by one reduction. The square of an element is central, $\tilde\Xi\star\tilde\Xi = H(\tilde\Xi)e_0$ with $H(\tilde\Xi) = \sum_\mu\lvert \Xi_\mu\rvert^{2}$ a real non-negative number (*Norm and Invertibility in the Symmetric Plain Sesqualgebra*), so the equation of a root is the single scalar equation $H(\tilde\Xi) = \lambda$, and the root set of $+1$ is the algebraic-norm-one quadric, a real quadric of real dimension seven. On the same reduction the idempotent equation is forced into the centre, where the product is the field rule $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$ and the equation reads $\lvert\lambda\rvert^{2} = \lambda$; its roots are $0$ and $1$, so the idempotents are the two elements $0$ and $e_0$. The **halving map** $\tilde\Pi = \tfrac12(e_0+\tilde\Xi)$ and its inverse $\tilde\Xi = 2\tilde\Pi-e_0$ tie the two: recomputed on the block, it carries the two real central roots of one, $\pm e_0$, onto the two idempotents, and it is not idempotent-valued on the rest of the quadric, because an idempotent of the block is central. No root of $-1$ enters, and the block has none.

**Placement.** The article is the fifth entry of the *Common Theory* section of the block, after the zero divisors and the annihilators, and before the roots of zero. It uses the product and the class of the introduction, the algebraic norm and the definiteness of *Norm and Invertibility in the Symmetric Plain Sesqualgebra*, and the zero-divisor set of *Zero Divisors of the Symmetric Plain Sesqualgebra*; the roots of zero and the nilpotents are *Square Roots of Zero and the Nilpotents of the Symmetric Plain Sesqualgebra*, and the general problem is *Square Roots of a General Element in the Symmetric Plain Sesqualgebra*.

**Boundaries.** The product, its class and its placement are *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*; the relative definitions of the root, of the square root, of the idempotent, of the projection and of the Peirce decomposition are *Definitions for the Study of the 12 Algebraic Structures*, where the halving map is stated for a general product. The roots of one of the parent and its idempotents are *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* and *Idempotents of the General Plain Algebra*; the idempotents of the general plain sesquilinear product are *Idempotents of the General Plain Sesqualgebra*. The projectors of the multiplication operators of the block are *The Multiplication Operators of the Symmetric Plain Sesqualgebra*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with central scalar imaginary $i$. A general element is $\tilde\Xi = \sum_{\mu=0}^{3}\Xi_\mu e_\mu$ with $\Xi_\mu\in\mathbb{C}$; the natural conjugation is $\tilde\Xi^{\natural} = \sum_\mu\varepsilon_\mu \Xi_\mu e_\mu$ with $\varepsilon = (1,-1,-1,-1)$, the coefficientwise conjugation is $\overline{\tilde\Xi} = \sum_\mu\overline{\Xi_\mu}e_\mu$, and the Hermitian conjugation is $\tilde\Xi^{*} = \overline{\tilde\Xi^{\natural}}$. The product of the block is

$$
\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0, \qquad H(\tilde P,\tilde Q) = \sum_{\mu=0}^{3}P_\mu\overline{Q_\mu},
$$

and the algebraic norm is $H(\tilde Q) = H(\tilde Q,\tilde Q) = \sum_\mu\lvert Q_\mu\rvert^{2}$. A root of a central value is written $\tilde\Xi$ and an idempotent $\tilde\Pi$.

**The results.** The root equation $\tilde\Xi\star\tilde\Xi = \lambda e_0$ reduces to the single real scalar equation $H(\tilde\Xi) = \lambda$, so a root of $\lambda$ exists exactly when $\lambda\in\mathbb{R}_{>0}$ and the root set is then the real quadric $\{H(\tilde\Xi) = \lambda\}$ of real dimension seven. The root set of $+1$ is the algebraic-norm-one quadric $\{H(\tilde\Xi) = 1\}$, nonempty, containing $e_0$ and $ie_0$, stable under the three conjugations and under multiplication by the complex scalars of modulus one; every one of its elements is a zero divisor of the block. The root set of $-1$ is empty, stated in the closing remark of the roots-of-one part. The idempotents of the block are exactly $0$ and $e_0$: the equation forces the centre, and there $\lvert\lambda\rvert^{2} = \lambda$ has the two roots. The element $e_0$ is an idempotent and not a unit; both idempotents are fixed by the three conjugations and are projections, and there is no Peirce decomposition, the construction needing a unit and its complement. The halving map carries the two real central roots of one, $\pm e_0$, onto the two idempotents and nothing else.

## The Root Equation and Its Reduction

**The root equation reduces to one real scalar equation: the square is $\tilde\Xi\star\tilde\Xi = H(\tilde\Xi)e_0$ with $H(\tilde\Xi) = \sum_\mu\lvert \Xi_\mu\rvert^{2}$ real and non-negative, so a root of $\lambda$ exists exactly when $\lambda\in\mathbb{R}_{>0}$, and the root set is then the real quadric $\{H(\tilde\Xi) = \lambda\}$ of real dimension seven.**

**Definition (recalled).** A **root of $\lambda$** in the block is a nonzero element $\tilde\Xi$ with $\tilde\Xi\star\tilde\Xi = \lambda e_0$; the **root set** of $\lambda$ is the set of such elements. The definition is that of *Definitions for the Study of the 12 Algebraic Structures*, read on the product $\star$; a root of $0$ is a nonzero square-zero element, and a root of $+1$ is a nonzero element of square one.

**Theorem (the reduction).** For every $\tilde\Xi\in\mathbb{B}$,

$$
\tilde\Xi\star\tilde\Xi = H(\tilde\Xi)e_0 = \Bigl(\sum_{\mu=0}^{3}\lvert \Xi_\mu\rvert^{2}\Bigr)e_0,
$$

with $H(\tilde\Xi)$ a real non-negative number vanishing exactly at $\tilde\Xi = 0$. Consequently the equation $\tilde\Xi\star\tilde\Xi = \lambda e_0$ is the scalar equation $H(\tilde\Xi) = \lambda$ together with the requirement $\tilde\Xi\neq0$, and the central values are read on the single real function $H$.

*Proof.* The display is the definition of the algebraic norm and the square map of *Norm and Invertibility in the Symmetric Plain Sesqualgebra*, $\tilde\Xi\star\tilde\Xi = H(\tilde\Xi)e_0$, with $H(\tilde\Xi) = \sum_\mu\lvert \Xi_\mu\rvert^{2}$; a sum of squares of moduli is real and non-negative, and it vanishes exactly when every $\Xi_\mu$ does. The two sides of $\tilde\Xi\star\tilde\Xi = \lambda e_0$ are therefore central, and comparing the coefficients gives $H(\tilde\Xi) = \lambda$.

**Corollary (the trichotomy).** A necessary and sufficient condition for the existence of a root of $\lambda$ is $\lambda\in\mathbb{R}_{>0}$; for such a $\lambda$ the root set is the real quadric

$$
\{\tilde\Xi\in\mathbb{B} : H(\tilde\Xi) = \lambda\},
$$

a real algebraic set of real dimension seven. For $\lambda\in\mathbb{R}_{<0}$, for $\lambda\notin\mathbb{R}$, and for $\lambda = 0$ there is no root.

*Proof.* $H$ takes every positive real value, since $H(\sqrt{\lambda}e_0) = \lambda$ for $\lambda>0$, and takes no value outside $\mathbb{R}_{\geq0}$; at $\lambda = 0$ the only solution is $\tilde\Xi = 0$, which is excluded from being a root by the definition. The level set of the positive definite quadratic form $H$ at a positive value is a quadric whose real codimension is one, hence of real dimension seven.

### The Three Central Values Compared

**Of the three central values $-1$, $0$ and $+1$ the block carries only $+1$: the root sets of $-1$ and of $0$ are empty, and the root set of $+1$ is the algebraic-norm-one quadric of real dimension seven.**

| central value $\lambda$ | equation | root set | size |
|---|---|---|---|
| $-1$ | $H(\tilde\Xi) = -1$ | empty | none |
| $0$ | $H(\tilde\Xi) = 0$ | empty, $0$ being the only solution and excluded | none |
| $+1$ | $H(\tilde\Xi) = 1$ | the algebraic-norm-one quadric | real dimension seven |

The three rows are read from the single real function $H$: the first two are its negative and its zero, forbidden by the definition of the root and by the definiteness, and the third is its value one. The block therefore carries exactly one of the three classes, and the one it carries is the largest. The root set of $+1$ is the subject of §*The Roots of One*; the root set of $0$ and the nilpotents are *Square Roots of Zero and the Nilpotents of the Symmetric Plain Sesqualgebra*, and the root set of $-1$ is the remark that closes §*The Roots of One*.

## The Roots of One

**The root set of $+1$ is the algebraic-norm-one quadric $\{H(\tilde\Xi) = 1\}$, a real quadric of real dimension seven, nonempty, containing $e_0$ and $ie_0$, and stable under the three conjugations and under multiplication by the complex scalars of modulus one.**

**Theorem (the roots of $+1$).** The root set of $+1$ is the quadric

$$
\mathcal{R}(+1) = \Bigl\{\tilde\Xi\in\mathbb{B} : \sum_{\mu=0}^{3}\lvert \Xi_\mu\rvert^{2} = 1\Bigr\},
$$

a real quadric of real dimension seven; it is nonempty, it contains the two elements $e_0$ and $ie_0$, and it is stable under the three conjugations and under complex multiplication by a scalar of modulus one.

*Proof.* The description is the corollary of the reduction at $\lambda = 1$. The elements $e_0$ and $ie_0$ have algebraic norm $1$ and are nonzero. The stability is that of $H$: $H(\lambda\tilde\Xi) = \lvert\lambda\rvert^{2}H(\tilde\Xi)$, and each of the three conjugations preserves the moduli of the coordinates.

**Proposition (the roots of $+1$ are exactly the elements of algebraic norm one).** An element is a root of $+1$ if and only if it has algebraic norm one. Every root of $+1$ is a zero divisor of the block, and every root of $+1$ has a nonzero orthogonal companion, $\tilde\Xi^{\perp}$ being a hyperplane.

*Proof.* The first is the theorem. The zero-divisor statement is that every nonzero element is a zero divisor (*Zero Divisors of the Symmetric Plain Sesqualgebra*), and the companion is the hyperplane of the same article.

### The Roots of One and the Three Conjugations

**The root set of $+1$ is carried to itself by the natural conjugation, by the coefficientwise conjugation, and by the Hermitian conjugation, these acting on the moduli of the coordinates; consequently a statement about a root of $+1$ is a statement about its three conjugates, and the root set is a real algebraic set stable under the three of them.**

*Proof.* Each of the three conjugations preserves the modulus of each coordinate, hence preserves $H(\tilde\Xi) = \sum_\mu\lvert \Xi_\mu\rvert^{2}$, so it carries $H = 1$ to itself. The natural conjugation is $\mathbb{C}$-linear, the coefficientwise and the Hermitian ones are antilinear, and the three are involutions.

### The Roots of One and the Zero Divisors

**Every root of $+1$ is a zero divisor of the block, since every nonzero element is one; the converse fails, because the zero-divisor set is the whole punctured space and the root set of $+1$ is the algebraic-norm-one quadric inside it.**

*Proof.* Every nonzero element is a two-sided zero divisor and the zero element alone is not (*Zero Divisors of the Symmetric Plain Sesqualgebra*), so the root set, being a subset of the punctured space, is a set of zero divisors; the converse fails because the punctured space is larger, containing for instance $2e_0$, of algebraic norm four. Being a zero divisor is therefore no condition on the block, and the root condition is a genuine condition, the value of the algebraic norm.

### The Roots of One and the Sibling Products

**In the plain product the roots of $+1$ are the image $\tilde P i$ of the roots of $-1$ under multiplication by the central imaginary, and its idempotents are its halved roots of $+1$, $\tfrac12(e_0+\tilde\Xi)$ with $\tilde\Xi\star\tilde\Xi = e_0$, the different image of the same set; here the roots of $+1$ are the algebraic-norm-one quadric, a much larger set, and they are classified directly, without reference to the roots of $-1$, which do not exist.**

The plain product's two images differ: the roots of $+1$ and the idempotents meet only at $e_0$ (*Idempotents of the General Plain Algebra*). In the block the two sets are the quadric $\{H = 1\}$ and the two points $\{0,e_0\}$; the element $e_0$ belongs to both, being an idempotent and a root of $+1$, and every other root of $+1$ is not idempotent. The comparison of the root sets of the block with those of the parent is in *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*.

**The sibling blocks.** The plain product has the three roots of $-1$, $0$ and $+1$; the block has one of the three. The difference lies in the sign of the diagonal: the plain product's quadratic form $\sum_\mu \Xi_\mu^{2}$ takes the two signs and vanishes off the origin, while the block's algebraic norm is definite, so the negative and the zero values are excluded.

**Remark (the roots of $-1$).** The roots of $-1$ are read off the same reduction. For a bilinear product the sign flips under multiplication by the central imaginary, because $(i\tilde\Xi)\star(i\tilde\Xi) = i^{2}(\tilde\Xi\star\tilde\Xi) = -\tilde\Xi\star\tilde\Xi$, so on such a product the root set of $-1$ is the root set of $+1$ read through one map; the block is sesquilinear, so this mechanism is unavailable to it, the second slot carrying the conjugation and a scalar of modulus one leaving the algebraic norm unchanged, $H(i\tilde\Xi) = H(\tilde\Xi)$. The root set of $-1$ of the block is therefore **empty**, and it is quoted here alone; nothing later uses it.

## The Definition of the Idempotent

**Definition (recalled).** An **idempotent of the symmetric plain sesqualgebra** is an element $\tilde\Pi\in\mathbb{B}$ with

$$
\tilde\Pi\star\tilde\Pi = \tilde\Pi .
$$

The equation names the product, so the notion is relative to it: the definition is the general one of *Definitions for the Study of the 12 Algebraic Structures*, read on the product $\star$, and the idempotents of the four general products are a different matter (*Comparison Between the Four General Products*). Throughout this article the product is the block and another one is named where it is meant.

**Remark (the idempotent and the projection).** An idempotent is an **element** of the algebra equal to its own square, and a **projector** is an **operator** of the morphism space equal to its own square; the two words name different objects and are never interchanged. The projections of the sesqualgebra, the idempotents of the general plain sesquilinear product, are *Idempotents of the General Plain Sesqualgebra*, and the idempotents of the block are the restriction of that theory to the block.

## The Idempotents Are $0$ and $e_0$

**An element $\tilde\Pi$ satisfies $\tilde\Pi\star\tilde\Pi = \tilde\Pi$ if and only if $\tilde\Pi\in\{0,e_0\}$, so the block carries the two-point idempotent set, the origin and the identity of the centre, both central, both fixed by the three conjugations, orthogonal and exhausting the set.**

**Theorem (the classification).** An element $\tilde\Pi$ satisfies $\tilde\Pi\star\tilde\Pi = \tilde\Pi$ if and only if $\tilde\Pi\in\{0,e_0\}$.

*Proof.* By the square map of *Norm and Invertibility in the Symmetric Plain Sesqualgebra*, $\tilde\Pi\star\tilde\Pi = H(\tilde\Pi)e_0$ is central; the equation then reads $H(\tilde\Pi)e_0 = \tilde\Pi$, which forces $\tilde\Pi$ to be central, $\tilde\Pi = \lambda e_0$ with $\lambda\in\mathbb{C}$. On the centre the product is the field rule $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$, so the square of $\lambda e_0$ is $\lvert\lambda\rvert^{2}e_0$ and the equation reads $\lvert\lambda\rvert^{2} = \lambda$. Comparing the real and the imaginary parts, $\lambda$ is real, and then $\lambda^{2} = \lambda$, so $\lambda\in\{0,1\}$; conversely $0\star0 = 0$ and $e_0\star e_0 = H(e_0,e_0)e_0 = e_0$.

**Corollary (the two idempotents are the origin and the identity of the centre).** The idempotents of the block are the origin and the unit idempotent of the centre. Both are central, both are fixed by the three conjugations, $\tilde\Pi^{\natural} = \overline{\tilde\Pi} = \tilde\Pi^{*} = \tilde\Pi$, and both are **orthogonal**, $0\star e_0 = e_0\star0 = 0$, with sum the idempotent $e_0$; the sum is not a unit of the block.

**Remark (why the centre is the whole story).** The collapse to the centre is not an accident of the block: a product whose image is the central line forces the square of every element into the centre, so the idempotent equation has only central solutions. The same collapse occurs in the symmetric quaternionic algebra, whose idempotents are also $0$ and $e_0$ (*The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*); it fails in the symmetric plain algebra, whose product has a vector part and whose idempotents come in two families attached to the roots of $+1$ (*The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*).

## $e_0$ Is an Idempotent and Not a Unit

**The element $e_0$ satisfies $\tilde Q\star e_0 = Q_0e_0$ and $e_0\star\tilde Q = \overline{Q_0}e_0$, so it is not a left, a right or a two-sided unit and the block has no unit.**

**Theorem ($e_0$ is not a unit).** For every $\tilde Q$,

$$
\tilde Q\star e_0 = Q_0e_0, \qquad e_0\star\tilde Q = \overline{Q_0}e_0,
$$

so the idempotent $e_0$ is not a left unit, not a right unit and not a two-sided unit, and the block has no unit.

*Proof.* The two displays are $H(\tilde Q,e_0) = Q_0$ and $H(e_0,\tilde Q) = \overline{Q_0}$; an element with a nonzero vector part is reproduced by neither side, since both values are central. The absence of a unit is *The Absence of a Unit* of *Norm and Invertibility in the Symmetric Plain Sesqualgebra*.

**Remark (the two distinct meanings of the word).** The element $e_0$ is an idempotent of the block and the identity of the plain product at once (*Norm and Invertibility in the General Quaternionic Algebra*), and it is a unit of the one and not of the block. The distinction is exactly the distinction between the two products: an equation that names a product has its solutions in the elements selected by that product, and the idempotent equation of the block selects $e_0$ while the unit equation of the block has no solution.

## The Idempotents and the Roots of One

**The idempotents are the roots of one halved: the map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$, with inverse $\tilde\Pi\mapsto2\tilde\Pi-e_0$, carries the two real central roots of one, $\pm e_0$, onto the two idempotents, and it is not idempotent-valued on the rest of the norm-one quadric, because an idempotent of the block is central.**

**The general statement.** The definitions article states the map for a general product: the idempotents are the roots of $+1$ halved, the map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ carrying the roots of $+1$ onto the idempotents, with the inverse $\tilde\Xi = 2\tilde\Pi-e_0$ (*Definitions for the Study of the 12 Algebraic Structures*, *Idempotents of the General Plain Algebra*). The block is a product whose image is the central line and whose form is definite, so the map must be recomputed on it, and it collapses.

**Theorem (the halving map on the block).** Let $\tilde\Xi$ be a root of $+1$ and put $\tilde\Pi = \tfrac12(e_0+\tilde\Xi)$. Then

$$
\tilde\Pi\star\tilde\Pi = \tfrac14\bigl(1 + 2\,\mathrm{Re}\,\Xi_0 + H(\tilde\Xi)\bigr)e_0 = \tfrac12\bigl(1 + \mathrm{Re}\,\Xi_0\bigr)e_0 ,
$$

so $\tilde\Pi$ is idempotent if and only if $\tilde\Xi = \pm e_0$. The inverse map carries the two idempotents back, $2e_0-e_0 = e_0$ and $2\cdot0-e_0 = -e_0$, both roots of $+1$.

*Proof.* By the reduction, $e_0\star\tilde\Xi = \overline{\Xi_0}e_0$, $\tilde\Xi\star e_0 = \Xi_0e_0$ and $\tilde\Xi\star\tilde\Xi = H(\tilde\Xi)e_0$, and $e_0\star e_0 = e_0$; distributing the product over the sum, $\tilde\Pi\star\tilde\Pi = \tfrac14\bigl(1 + 2\,\mathrm{Re}\,\Xi_0 + H(\tilde\Xi)\bigr)e_0$, which is the first display, and the second follows from $H(\tilde\Xi) = 1$. This value is central, while $\tilde\Pi$ is central if and only if $\tilde\Xi$ is central; and $\tilde\Xi$ central with $H(\tilde\Xi) = 1$ means $\tilde\Xi = \lambda e_0$ with $\lvert\lambda\rvert = 1$, for which $\tfrac12(1+\mathrm{Re}\,\lambda) = \tfrac12(1+\lambda)$ forces $\lambda$ real, hence $\lambda = \pm1$. The two values $\tilde\Xi = \pm e_0$ give $\tilde\Pi = e_0$ and $\tilde\Pi = 0$, and the inverse displays are immediate.

**Corollary (the idempotents correspond to the two real central roots of one).** The halving map restricts to a bijection between the two real central roots of $+1$, namely $e_0$ and $-e_0$, and the two idempotents $e_0$ and $0$. The complementary pair $\tilde\Pi$, $e_0-\tilde\Pi$ corresponds to the pair $\tilde\Xi$, $-\tilde\Xi$: the idempotent $e_0$ and its complement $0$ correspond to the roots $e_0$ and $-e_0$.

**Remark (no bijection with the whole quadric, and no root of $-1$).** The map does not carry the whole norm-one quadric onto the idempotents: a non-central root of $+1$ has a non-central half, and a non-central element of the block is never idempotent, its square being central. What the map gives is the correspondence between the idempotents and the two central roots of one, $\pm e_0$. The idempotent classification of the block is therefore a classification **by the roots of one**, the root the architecture uses, and not by the roots of $-1$: the parent's bijection between its idempotents and its roots of $-1$ is a bijection of the parent (*Idempotents of the General Plain Algebra*), and the block replaces it by the correspondence above, the block having no root of $-1$ at all. The two subjects are kept apart: the roots of one are a fact about the root set, and the idempotents are a fact about the fixed points of the square map, and the halving map is the only bridge, carrying the two central roots to the two idempotents.

## The Idempotents as Projections

**The two idempotents $0$ and $e_0$ are fixed by the three conjugations, $\tilde\Pi^{*} = \tilde\Pi$, so both are projections of the block and the projection set is the minimum of two points.**

**Theorem (both idempotents are projections).** The two idempotents $0$ and $e_0$ are fixed by the three conjugations, $\tilde\Pi^{*} = \tilde\Pi$, so both are projections of the sesqualgebra in the sense of the star-fixed idempotents.

*Proof.* $0$ and $e_0$ are real central elements; the natural conjugation fixes the scalar line, the coefficientwise conjugation fixes the real line, and the Hermitian conjugation is their composite, so all three fix $e_0$ and $0$.

**Remark (the projections are the minimum).** The projections of the block are the two idempotents, and the idempotent theory of the sesqualgebra, which cuts the general plain sesquilinear product into its Peirce pieces, restricts here to these two points (*Idempotents of the General Plain Sesqualgebra*). The element $e_0$ is a projection of the block and of the plain product at once; the difference is that the block has no unit, so the projection of the block onto the central line is not the identity of the block.

## The Absence of a Peirce Decomposition

**The block has no Peirce decomposition attached to its idempotents, the construction needing a two-sided unit and its complement, and what replaces it is the decomposition $\mathbb{B} = \mathbb{C}e_0\oplus\mathrm{Vect}(\mathbb{B})$ by the scalar coordinate.**

**Proposition (no Peirce decomposition).** The block has no Peirce decomposition attached to its idempotents.

*Proof.* The Peirce decomposition is built from an idempotent $\tilde\Pi$ together with the complementary idempotent $e - \tilde\Pi$, where $e$ is a two-sided unit; the four pieces are the corners of the algebra relative to the pair. Without a unit there is no complement, and the block has no unit; the construction is unavailable.

**Remark (what replaces it).** The block's structural decomposition is the orthogonal direct sum $\mathbb{B} = \mathbb{C}e_0\oplus\mathrm{Vect}(\mathbb{B})$ into the central line and the vector subspace, and it is the decomposition by the scalar coordinate, not the Peirce decomposition. The idempotent $e_0$ projects onto the central line in the sense that $\tilde Q\star e_0 = Q_0e_0$ is the central part of $\tilde Q$; the other piece, the vector part, is not the image of an idempotent of the block, because the block has no second idempotent. The decomposition is a decomposition by a projection-like map of the operator algebra, and it is in *The Multiplication Operators of the Symmetric Plain Sesqualgebra*.

## The Idempotents and the Sibling Symmetric Products

**Among the four symmetric products the block carries the two-point idempotent set $\{0,e_0\}$, which it shares with its central sibling $\mathrm{SQA}$, while $\mathrm{SPA}$ carries a four-parameter family and $\mathrm{SQS}$ a two-parameter family.**

The idempotents of the four symmetric structures are of two kinds beyond the two points. The symmetric plain algebra carries the four-parameter plain family, the symmetric quaternionic sesqualgebra the two-parameter family $-\tfrac12e_0+\vec n$, and the two central blocks, $\mathrm{SQA}$ and the present $\mathrm{SPS}$, the two points. The table collects the comparison.

| structure | product | idempotents | index set |
|---|---|---|---|
| $\mathrm{SPA}$ | $\tfrac12(\tilde P\tilde Q + \tilde Q\tilde P)$ | the two families $\tfrac12(e_0 + \tilde\Xi)$ with $\tilde\Xi$ a root of $+1$ | the roots of $+1$ |
| $\mathrm{SQA}$ | $N(\tilde P,\tilde Q)e_0$ | $0$ and $e_0$ | two points |
| $\mathrm{SPS}$ | $H(\tilde P,\tilde Q)e_0$ | $0$ and $e_0$ | two points |
| $\mathrm{SQS}$ | $\tfrac12(\tilde P^{\natural}\tilde Q^{*} + \tilde Q^{*}\tilde P^{\natural})$ | $0$, $e_0$, and the family $-\tfrac12e_0+\vec n$ with $(\vec n,\vec n)=\tfrac34$ | the two-sphere |

The plain sibling is the one with a unit and the one whose product has a vector part, and it carries a four-parameter family of nontrivial idempotents, indexed by its roots of $+1$; the quaternionic sesquilinear sibling carries the two-parameter family $-\tfrac12e_0+\vec n$, and the two central blocks carry the two points; among the central blocks the present one is distinguished not by the idempotents but by the image and the sign of its form. The comparison with the general plain product, whose idempotents are the two standard ones $\tilde\Pi_+$ and $\tilde\Pi_-$ and the complex multiples, is *Idempotents of the General Plain Algebra*.

## Summary

The square of an element of the symmetric plain sesqualgebra is $\tilde\Xi\star\tilde\Xi = H(\tilde\Xi)e_0$ with $H(\tilde\Xi) = \sum_\mu\lvert \Xi_\mu\rvert^{2}$ a real non-negative definite number, so the root equation $\tilde\Xi\star\tilde\Xi = \lambda e_0$ reduces to the scalar equation $H(\tilde\Xi) = \lambda$. Of the three central values the block carries only $+1$: its root set is the **algebraic-norm-one quadric** $\{H = 1\}$, a real quadric of real dimension seven, nonempty, containing $e_0$ and $ie_0$, stable under the three conjugations and under the multiplication by the complex scalars of modulus one; the root set of $-1$ is **empty**, the sesquilinear sign being unflippable by a scalar, and the root set of $0$ is empty too, the origin being excluded. Every root of $+1$ is a zero divisor, and the converse fails because every nonzero element is one. The **idempotents** are exactly $0$ and $e_0$: the square map forces an idempotent into the centre, and there the equation reads $\lvert\lambda\rvert^{2} = \lambda$, whose roots are $0$ and $1$. The **halving map** $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$, inverse $\tilde\Pi\mapsto2\tilde\Pi-e_0$, carries the two real central roots of one, $\pm e_0$, onto the two idempotents and nothing else; the idempotent classification rests on the **roots of one** and not on the roots of $-1$, of which the block has none. The element $e_0$ is an idempotent and **not a unit**: $\tilde Q\star e_0 = Q_0e_0$ and $e_0\star\tilde Q = \overline{Q_0}e_0$, so no element with a vector part is reproduced, and the block has no unit. Both idempotents are fixed by the three conjugations and are therefore projections; the **Peirce decomposition** is unavailable, because it needs a unit and its complement, and what replaces it is the decomposition $\mathbb{B} = \mathbb{C}e_0\oplus\mathrm{Vect}(\mathbb{B})$ by the scalar coordinate. Among the four symmetric products the block carries the two-point idempotent set, the smallest possible after the trivial one, and it shares the set with its central sibling $\mathrm{SQA}$ alone; the two remaining siblings, $\mathrm{SPA}$ and $\mathrm{SQS}$, carry positive-dimensional families.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ | the product of the block |
| $H(\tilde{Q}) = H(\tilde{Q},\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$ | the algebraic norm of the block, real and non-negative |
| $\tilde\Xi\star\tilde\Xi = H(\tilde\Xi)e_0$ | the reduction of the root equation |
| $\mathcal{R}(+1) = \{H = 1\}$ | the root set of $+1$, the algebraic-norm-one quadric, real dimension seven |
| $\mathcal{R}(-1) = \varnothing$ | no root of $-1$ |
| $\mathcal{R}(0) = \varnothing$ | no nonzero root of $0$ |
| $\tilde\Xi^{\natural}$, $\overline{\tilde\Xi}$, $\tilde\Xi^{*}$ | the three conjugations, acting on the root set by preserving the moduli of the coordinates |
| $\tilde\Pi\star\tilde\Pi = \tilde\Pi$ | the idempotent equation of the block |
| $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$ | the product on the centre |
| $\lvert\lambda\rvert^{2} = \lambda$ | the idempotent equation on the centre |
| $\{0, e_0\}$ | the idempotents of the block |
| $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$, $\tilde\Pi\mapsto2\tilde\Pi-e_0$ | the halving map and its inverse |
| $\tilde{Q}\star e_0 = Q_0e_0$, $e_0\star\tilde{Q} = \overline{Q_0}e_0$ | the failure of $e_0$ as a unit |
| $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_0$ | the centre of $\mathbb{B}$ |
| $\mathbb{B} = \mathbb{C}e_0\oplus\mathrm{Vect}(\mathbb{B})$ | the decomposition that replaces the Peirce one |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product, its class and its placement.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the relative definition of the root, of the square root, of the idempotent, of the projection and of the Peirce decomposition, and for the halving map stated for a general product.
- *Norm and Invertibility in the Symmetric Plain Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-plain-sesqualgebra.md`), for the algebraic norm, its definiteness, the square map and the absence of a unit.
- *Zero Divisors of the Symmetric Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-sesqualgebra.md`), for the punctured-space set that contains every root and the annihilators.
- *Square Roots of Zero and the Nilpotents of the Symmetric Plain Sesqualgebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-plain-sesqualgebra.md`), for the emptiness of the root set of $0$ and the index-three nilpotents.
- *Square Roots of a General Element in the Symmetric Plain Sesqualgebra* (`articles_maths/square-roots-of-a-general-element-in-the-symmetric-plain-sesqualgebra.md`), for the general reduction the present one specialises.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra-of-quaternions.md`), for the three root sets of the parent and their idempotent and nilpotent reading.
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra-of-quaternions.md`), for the idempotents of the parent, their classification, the halving map and the Peirce decomposition.
- *Idempotents of the General Plain Sesqualgebra* (`articles_maths/idempotents-of-the-general-plain-sesqualgebra.md`), for the idempotents of the general plain sesquilinear product, of which the two are the restriction.
- *The Multiplication Operators of the Symmetric Plain Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-plain-sesqualgebra.md`), for the decomposition $\mathbb{B} = \mathbb{C}e_0\oplus\mathrm{Vect}(\mathbb{B})$ that replaces the Peirce one.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* (`articles_maths/the-square-the-idempotents-and-the-jordan-inverse-of-the-symmetric-plain-algebra.md`), for the two idempotent families of the plain sibling.
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), for the two idempotents of the quaternionic sibling.
