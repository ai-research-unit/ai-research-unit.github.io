# __Idempotents of the Symmetric Quaternionic Sesqualgebra__

## Introduction

This article classifies the idempotents of the block, the symmetric quaternionic sesquilinear product
$\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ of
*Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*. It follows
*Zero Divisors of the Symmetric Quaternionic Sesqualgebra* and reads the second named class of the block;
the first, the nilpotents, is *Nilpotents of the Symmetric Quaternionic Sesqualgebra*.

The idempotent is the solution of an equation in the product, and the product is part of the definition: it
is stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures*,
§*The Idempotent, the Projection and the Peirce Decomposition*, and read on the products of the space. The
unqualified word means the idempotent of the block. The nontrivial idempotents of the plain product are a
family indexed by the roots of $-1$ and are all zero divisors; the nontrivial idempotents of the block are a
real sphere and are all regular, and the difference is the point of §*The Idempotents and the Other Classes*.

The product is *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*; the diagonal
$\tilde Q\star\tilde Q$ is *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic
Sesqualgebra*; the zero divisors and the regular elements are *Zero Divisors of the Symmetric Quaternionic
Sesqualgebra*; the roots of the central values are *Square Roots of Minus One, Zero and Plus One in the
Symmetric Quaternionic Sesqualgebra*; and the idempotents of the plain product are *Idempotents of the
General Plain Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$,
$e_k^2=-e_0$ and $e_1e_2=e_3$; $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$ and central
scalar imaginary $i$; $\mathbf Q=\sum_kQ_ke_k$; $(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$; ${}^{\natural}$ negates
$e_1,e_2,e_3$ and fixes $e_0$ and the coefficients, ${}^{*}={}^{\natural}\circ\bar{\cdot}$; and
$\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_0+\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$ is the real quaternion
subspace. The diagonal of the block is
$\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf Q}-\overline{Q_0}\mathbf Q$, with
$K(\tilde Q,\tilde Q)=|Q_0|^2-\sum_k|Q_k|^2$. Throughout this article the product is the block.

## Definition

**Definition (idempotent of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Pi$
is an **idempotent of $\star$** when

$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi .
$$

The origin is an idempotent of every product, and so is the unit when there is one; these are the **trivial
idempotents**, and the others are **nontrivial**. The set of the idempotents of $\star$ is its **idempotent
set**.

This is *Definitions for the Study of the 12 Algebraic Structures*, §*The Idempotent, the Projection and
the Peirce Decomposition*. Unqualified, the product is the block, so the equation to solve is

$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi ,
$$

and the block has no unit, so the only trivial idempotents are $0$ and the unit candidate $e_0$. The
idempotent is not the root of $+1$: the root of $+1$ solves $\tilde P\star\tilde P=e_0$ and is a different
equation, treated in *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic
Sesqualgebra*.

## The Equation and Its Reduction

Write $\tilde\Pi=\alpha e_0+\mathbf x$ with $\alpha\in\mathbb{C}$ and $\mathbf x\in\mathbb{C}^3$. The
diagonal formula splits the equation into the two displays

$$
K(\tilde\Pi,\tilde\Pi)=|\alpha|^2-\lVert\mathbf x\rVert^2=\alpha ,
\qquad
-2\,\mathrm{Re}\bigl(\alpha\overline{\mathbf x}\bigr)=\mathbf x ,
$$

the first the scalar part and the second the vector part of the equality.

**Proposition (the reduction).** The vector equation is equivalent to the pair

$$
\alpha\overline{\mathbf x}+(\overline{\alpha}+1)\mathbf x=\mathbf 0 ,
\qquad
\overline{\alpha}\,\mathbf x+(\alpha+1)\overline{\mathbf x}=\mathbf 0 ,
$$

the second being the conjugate of the first.

*Proof.* The vector equation $\alpha\overline{\mathbf x}+\overline{\alpha}\mathbf x=-\mathbf x$ is the
first display; conjugating it, coefficient by coefficient, gives the second.

**Corollary (the scalar part is forced).** If $\tilde\Pi$ is a nontrivial idempotent with $\alpha\neq0$ and
$\mathbf x\neq0$, then

$$
\mathrm{Re}\,\alpha=-\tfrac12 ,
\qquad
\mathbf x\in\mathbb{R}^3 ,
\qquad
\lVert\mathbf x\rVert^2=\tfrac34 .
$$

*Proof.* Multiply the first display of the reduction by $\alpha$ after eliminating $\overline{\mathbf x}$
with the second: the two displays give
$\bigl[(1+\alpha)(1+\overline{\alpha})-\alpha\overline{\alpha}\bigr]\mathbf x=\mathbf 0$, that is
$(1+2\mathrm{Re}\,\alpha)\mathbf x=\mathbf 0$, so $\mathrm{Re}\,\alpha=-\tfrac12$ because
$\mathbf x\neq0$. Substituting back, $(1+\overline{\alpha})(\overline{\mathbf x}-\mathbf x)=\mathbf 0$; with
$\alpha=-\tfrac12+ib$ this reads $(\tfrac12-ib)(\overline{\mathbf x}-\mathbf x)=\mathbf 0$. If $b\neq0$ then
$\overline{\mathbf x}=\mathbf x$ and $\mathbf x$ is real, and the scalar equation
$\alpha=|\alpha|^2-\lVert\mathbf x\rVert^2$ equates the complex number $-\tfrac12+ib$ with a real number, so
$b=0$, a contradiction. Hence $b=0$ and $\alpha=-\tfrac12$; then $\overline{\mathbf x}=\mathbf x$, so
$\mathbf x$ is real, and the scalar equation gives $\lVert\mathbf x\rVert^2=\tfrac34$.

## The Classification

**Theorem (the idempotent set of the block).** The idempotents of the block are

$$
0 ,
\qquad
e_0 ,
\qquad\text{and}\qquad
-\tfrac12e_0+\boldsymbol\mu ,
\qquad
\boldsymbol\mu\in\mathbb{R}^3,\quad
\lVert\boldsymbol\mu\rVert^2=\tfrac34 .
$$

*Proof.* Let $\tilde\Pi=\alpha e_0+\mathbf x$ be an idempotent.

If $\alpha=0$ the vector equation is $\mathbf x=\mathbf 0$, so $\tilde\Pi=0$.

If $\alpha\neq0$ and $\mathbf x=\mathbf 0$ the vector equation is void and the scalar equation reads
$\alpha^2=\alpha$, so $\alpha\in\{0,1\}$; with $\alpha\neq0$ this gives $\tilde\Pi=e_0$.

If $\alpha\neq0$ and $\mathbf x\neq0$ the corollary of §*The Equation and Its Reduction* gives
$\alpha=-\tfrac12$ and $\mathbf x\in\mathbb{R}^3$ with $\lVert\mathbf x\rVert^2=\tfrac34$; conversely every
element of this form satisfies both displays, since $-\tfrac12$ is real and
$K=|\alpha|^2-\lVert\mathbf x\rVert^2=\tfrac14-\tfrac34=-\tfrac12=\alpha$, while the vector part
$-2\mathrm{Re}(\alpha\overline{\mathbf x})=-2\alpha\mathbf x=\mathbf x$ because $2\alpha=-1$.

**Corollary (the shape of the set).** The nontrivial idempotents are a two-sphere of radius $\tfrac{\sqrt3}{2}$
in the real quaternion subspace, centred at $-\tfrac12e_0$, and the origin and $e_0$ are the two isolated
idempotents.

*Proof.* The family is the intersection of the affine hyperplane $\alpha=-\tfrac12$ of
$\mathbb{H}_{\mathbb{B}}$ with the sphere $\lVert\mathbf x\rVert^2=\tfrac34$.

## Properties of the Idempotent Set

**Theorem (the idempotents lie in the real quaternion subspace; the nonzero ones are regular).** Every
idempotent of the block is a real quaternion; every nonzero idempotent has central square $C(\tilde\Pi)=1$
and is regular.

*Proof.* Real quaternion: $0$, $e_0$ and $-\tfrac12e_0+\boldsymbol\mu$ are real by the classification. The
central square of $-\tfrac12e_0+\boldsymbol\mu$ is
$C=\tfrac14+\lVert\boldsymbol\mu\rVert^2=\tfrac14+\tfrac34=1$, and $c(e_0)=1$. Since a nonzero idempotent
has $Q_0\neq0$ (its scalar part is $1$ or $-\tfrac12$) and $C=1\neq0$, it is regular by the criterion of
*Zero Divisors of the Symmetric Quaternionic Sesqualgebra*.

So no nonzero idempotent of the block is a zero divisor, and every one lies on the slice $C=1$ of the
central square $C=\tilde Q\tilde Q^{\natural}$; the comparison with the plain product, where the nontrivial
idempotents are zero divisors, is the subject of §*The Idempotents and the Other Classes*.

**Theorem (the fixed-point reading).** The idempotent set is the fixed set of the quadratic map
$\mathsf{M}_2(\tilde Q)=\tilde Q\star\tilde Q$ on the block, and on the nontrivial family $\mathsf{M}_2$ is the constant
map with value the idempotent itself.

*Proof.* The idempotents are the solutions of $\mathsf{M}_2(\tilde\Pi)=\tilde\Pi$ by definition; the second
statement is the same equation read on the family.

**Theorem (no orthogonal pair).** For two nontrivial idempotents
$\tilde\Pi=-\tfrac12e_0+\boldsymbol\mu$ and $\tilde\Pi'=-\tfrac12e_0+\boldsymbol\nu$,

$$
\tilde\Pi\star\tilde\Pi'=\tfrac14-\boldsymbol\mu\!\cdot\!\boldsymbol\nu
+\tfrac12\bigl(\boldsymbol\mu+\boldsymbol\nu\bigr),
$$

whose scalar part is $\tfrac14-\boldsymbol\mu\!\cdot\!\boldsymbol\nu$ and whose vector part is
$\tfrac12(\boldsymbol\mu+\boldsymbol\nu)$; it vanishes for no pair, so the nontrivial idempotents are
pairwise non-orthogonal.

*Proof.* Both elements are real quaternions, and for real arguments the block reads
$\tilde P\star\tilde Q=[\mathrm{SPA}(\tilde P,\tilde Q)]^{\natural}$, the natural conjugate of the plain
symmetric product; computing $\mathrm{SPA}$ of the two idempotents, whose vector-part term is
$-\tfrac12(\boldsymbol\mu+\boldsymbol\nu)$, and applying the natural conjugation, which reverses the vector
sign, gives the display. The scalar part vanishes only if $\boldsymbol\mu\!\cdot\!\boldsymbol\nu=\tfrac14$
and the vector part only if
$\boldsymbol\nu=-\boldsymbol\mu$, which would give
$\boldsymbol\mu\!\cdot\!\boldsymbol\nu=-\lVert\boldsymbol\mu\rVert^2=-\tfrac34$, a contradiction.

**Remark (no complete family, no Peirce calculus).** The block has no unit, so the notion of an orthogonal
family summing to the unit has no content here, and no two nontrivial idempotents are orthogonal (only the
origin annihilates, and is annihilated, trivially). The Peirce
decomposition relative to an idempotent is a property of the plain product
(*The Specificities of the General Plain Algebra*) and is not available in the block.

## The Idempotents and the Other Classes

The three named classes of the block meet in a way opposite to the plain product.

| class of the block | idempotents it contains |
|---|---|
| zero divisors, pure family $\{Q_0=0\}$ | none, every nonzero idempotent having $Q_0\neq0$ |
| zero divisors, non-pure family $\mathcal{C}$ | none, every nonzero idempotent having $C=1$ |
| regular elements $\{Q_0\neq0,\ C\neq0\}$ | $e_0$ and the sphere $-\tfrac12e_0+\boldsymbol\mu$ |
| nilpotents $\{\alpha(e_0+i\boldsymbol\mu)\}$ | none, the two classes meeting only at $0$ |

The last row is proved in *Nilpotents of the Symmetric Quaternionic Sesqualgebra*: an element cannot have
both $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ and $\tilde\Upsilon\star\tilde\Upsilon=0$ unless it is $0$. The
contrast with the plain product is exact. There the nontrivial idempotents are
$\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-1$, their central square is $0$, and they are zero divisors;
here the nontrivial idempotents have central square $1$ and are regular. The reason is the shape of the
diagonal: the plain square of $\tfrac12(e_0+\tilde\Xi i)$ is the element itself with central square $0$, while
the block's diagonal carries the Krein form in its scalar part, and the equation
$K(\tilde\Pi,\tilde\Pi)=\alpha$ forces the scalar coordinate $-\tfrac12$ rather than leaving it free.

## Worked Examples

**The unit candidate.** $\tilde\Pi=e_0$: $e_0\star e_0=e_0$ by the multiplication table, so $e_0$ is an
idempotent; it is the unit candidate of the block and not a unit, since $e_0\star e_1=-e_1$.

**A nontrivial idempotent.** $\boldsymbol\mu=\tfrac{\sqrt3}{2}\cdot\tfrac{1}{\sqrt3}(1,1,1)=\tfrac12(1,1,1)$:
$\lVert\boldsymbol\mu\rVert^2=\tfrac34$ and
$\tilde\Pi=-\tfrac12e_0+\tfrac12e_1+\tfrac12e_2+\tfrac12e_3$ satisfies
$\tilde\Pi\star\tilde\Pi=\tilde\Pi$, as the classification states.

**An element of the sphere that is not the previous one.** $\boldsymbol\mu=\tfrac{\sqrt3}{2}e_1$:
$\tilde\Pi=-\tfrac12e_0+\tfrac{\sqrt3}{2}e_1$ is an idempotent, and it is a real quaternion of modulus one; it is
regular, so it annihilates nothing.

**The origin.** $\tilde\Pi=0$: $0\star0=0$, the trivial idempotent.

## Summary

The idempotent of the block is an element equal to its own square, and the block's idempotent set is

$$
\{0\}\ \cup\ \{e_0\}\ \cup\ \Bigl\{-\tfrac12e_0+\boldsymbol\mu:\boldsymbol\mu\in\mathbb{R}^3,\
\lVert\boldsymbol\mu\rVert^2=\tfrac34\Bigr\},
$$

the origin and the unit candidate isolated and the rest a two-sphere of radius $\tfrac{\sqrt3}{2}$ in the
real quaternion subspace. Every nonzero idempotent has central square $1$, so every one is regular and none
is a zero divisor; every nonzero idempotent lies on the slice $C=1$ of the central square. The idempotents of
the block differ from those of the plain product: the plain nontrivial idempotents have vanishing central
square and are zero divisors, while the block's have central square $1$ and are regular, the difference
being the shape of the diagonal, whose scalar part is the Krein form. The two named classes of the block,
the idempotents and the nilpotents, meet only at the origin, and the block, having no unit, carries neither
an orthogonal idempotent family nor a Peirce decomposition.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ | the idempotent equation of the block |
| $\{0\},\{e_0\}$ | the trivial idempotents, $e_0$ the unit candidate |
| $-\tfrac12e_0+\boldsymbol\mu,\ \lVert\boldsymbol\mu\rVert^2=\tfrac34$ | the nontrivial idempotents, a two-sphere |
| $C(\tilde\Pi)=\sum_\mu\Pi_\mu^2$ | the central square, equal to $1$ on the nonzero idempotents |
| $K(\tilde Q,\tilde Q)=|Q_0|^2-\lVert\mathbf Q\rVert^2$ | the scalar part of the diagonal, forcing $Q_0=-\tfrac12$ |
| $\mathbb{H}_{\mathbb{B}}$ | the real quaternion subspace, carrying the whole idempotent set |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Idempotent, the Projection and the Peirce Decomposition*, for the definition relative to a general product and for the idempotent sets of the four general products.
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra.md`), for the plain idempotents $\tfrac12(e_0+\tilde\Xi i)$ and their relation to the roots of $-1$.
- *Zero Divisors of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-sesqualgebra.md`), for the criterion that makes every nonzero idempotent regular.
- *Nilpotents of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/nilpotents-of-the-symmetric-quaternionic-sesqualgebra.md`), for the class disjoint from the idempotents.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product and its diagonal.
- *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-non-central-diagonal-and-the-two-halves-of-the-symmetric-quaternionic-sesqualgebra.md`), for the diagonal and the two halves out of which the equation is read.
