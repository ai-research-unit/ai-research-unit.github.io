# __Idempotents of the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ on the biquaternion space (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*). This article studies its **idempotents**: the elements $\tilde\Pi$ with $\tilde\Pi\star\tilde\Pi = \tilde\Pi$, an equation that names the product $\star$.

The block is a **rank-one pairing** with a definite form, and the idempotent equation collapses. The square of an element is central, $\tilde\Pi\star\tilde\Pi = H(\tilde\Pi)e_0$ with $H(\tilde\Pi) = \sum_\mu\lvert\Pi_\mu\rvert^{2}$ a real non-negative number, so an idempotent is forced into the centre, where the product is the field rule $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$ and the equation reads $\lvert\lambda\rvert^{2} = \lambda$. The roots are $0$ and $1$, and they give the two idempotents $0$ and $e_0$. The element $e_0$ is an idempotent and **not a unit**: the block has no unit, and the square root of the idempotent equation is not a unit for the block. The block therefore carries the minimum possible number of idempotents after the trivial one, and the companion objects of the plain product, the Peirce decomposition and the bijection with the roots of $-1$, have no analogue here.

**Placement.** The article is the sixth entry of the *Common Theory* section of the block, after the square roots of the central values and before the nilpotents. It uses the product and the class of the introduction, the algebraic norm and the definiteness of *Norm and Invertibility in the Symmetric Plain Sesqualgebra*, the rootlessness of $-1$ of *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Sesqualgebra*, and the punctured-space zero-divisor set of *Zero Divisors of the Symmetric Plain Sesqualgebra*.

**Boundaries.** The product, its class and its placement are *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*; the relative definition of the idempotent, the orthogonal and complete families and the projection is *Definitions for the Study of the 12 Algebraic Structures*. The idempotents of the parent, their classification and their Peirce decomposition are *Idempotents of the General Plain Algebra*; the idempotents of the general plain sesquilinear product, the projections of the sesqualgebra, are *Idempotents of the General Plain Sesqualgebra*. The idempotent of a sesqualgebra and the projector of its morphism space are two different objects and are not interchanged; the projectors of the multiplication operators of the block, which are only the zero operator, are *The Multiplication Operators of the Symmetric Plain Sesqualgebra*. Nothing topological and nothing metric appears.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with central scalar imaginary $i$. A general element is $\tilde{Q} = \sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; the natural conjugation is $\tilde{Q}^{\natural} = \sum_\mu\varepsilon_\mu Q_\mu e_\mu$ with $\varepsilon = (1,-1,-1,-1)$, the coefficientwise conjugation is $\overline{\tilde{Q}} = \sum_\mu\overline{Q_\mu}e_\mu$, and the Hermitian conjugation is $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$. The product of the block is

$$
\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0, \qquad H(\tilde P,\tilde Q) = \sum_{\mu=0}^{3}P_\mu\overline{Q_\mu},
$$

and the algebraic norm is $H(\tilde{Q}) = H(\tilde{Q},\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$. An idempotent is written $\tilde\Pi$.

## The Definition Relative to the Product

**Definition (recalled).** An **idempotent of the symmetric plain sesqualgebra** is an element $\tilde\Pi\in\mathbb{B}$ with

$$
\tilde\Pi\star\tilde\Pi = \tilde\Pi .
$$

The equation names the product, so the notion is relative to it: the definition is the general one of *Definitions for the Study of the 12 Algebraic Structures*, read on the product $\star$, and the idempotents of the four general products are a different matter (*Comparison Between the Four General Products*). Throughout this article the product is the block and another one is named where it is meant.

**Remark (the idempotent and the projection).** An idempotent is an **element** of the algebra equal to its own square, and a **projector** is an **operator** of the morphism space equal to its own square; the two words name different objects and are never interchanged. The projections of the sesqualgebra, the idempotents of the general plain sesquilinear product, are *Idempotents of the General Plain Sesqualgebra*, and the idempotents of the block are the restriction of that theory to the block.

## The Idempotents Are $0$ and $e_0$

**Theorem (the classification).** An element $\tilde\Pi$ satisfies $\tilde\Pi\star\tilde\Pi = \tilde\Pi$ if and only if $\tilde\Pi\in\{0,e_0\}$.

*Proof.* By the square map of *Norm and Invertibility in the Symmetric Plain Sesqualgebra*, $\tilde\Pi\star\tilde\Pi = H(\tilde\Pi)e_0$ is central; the equation then reads $H(\tilde\Pi)e_0 = \tilde\Pi$, which forces $\tilde\Pi$ to be central, $\tilde\Pi = \lambda e_0$ with $\lambda\in\mathbb{C}$. On the centre the product is the field rule $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$, so the square of $\lambda e_0$ is $\lvert\lambda\rvert^{2}e_0$ and the equation reads $\lvert\lambda\rvert^{2} = \lambda$. Comparing the real and the imaginary parts, $\lambda$ is real, and then $\lambda^{2} = \lambda$, so $\lambda\in\{0,1\}$; conversely $0\star0 = 0$ and $e_0\star e_0 = H(e_0,e_0)e_0 = e_0$.

**Corollary (the two idempotents are the origin and the identity of the centre).** The idempotents of the block are the origin and the unit idempotent of the centre. Both are central, both are fixed by the three conjugations, $\tilde\Pi^{\natural} = \overline{\tilde\Pi} = \tilde\Pi^{*} = \tilde\Pi$, and both are **orthogonal**, $0\star e_0 = e_0\star0 = 0$, and **complete** in the sense that their sum is the idempotent $e_0$ and not a unit of the block.

**Remark (why the centre is the whole story).** The collapse to the centre is not an accident of the block: a product whose image is the central line forces the square of every element into the centre, so the idempotent equation has only central solutions. The same collapse occurs in the symmetric quaternionic algebra, whose idempotents are also $0$ and $e_0$ (*The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*); it fails in the symmetric plain algebra, whose product has a vector part and whose idempotents come in two families indexed by the roots of $-1$ (*The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*).

## $e_0$ Is an Idempotent and Not a Unit

**Theorem ($e_0$ is not a unit).** For every $\tilde{Q}$,

$$
\tilde{Q}\star e_0 = Q_0e_0, \qquad e_0\star\tilde{Q} = \overline{Q_0}e_0,
$$

so the idempotent $e_0$ is not a left unit, not a right unit and not a two-sided unit, and the block has no unit.

*Proof.* The two displays are $H(\tilde{Q},e_0) = Q_0$ and $H(e_0,\tilde{Q}) = \overline{Q_0}$; an element with a nonzero vector part is reproduced by neither side, since both values are central. The absence of a unit is *The Absence of a Unit* of *Norm and Invertibility in the Symmetric Plain Sesqualgebra*.

**Remark (the two distinct meanings of the word).** The element $e_0$ is an idempotent of the block and the identity of the plain product at once (*Norm and Invertibility in the General Plain Algebra*), and it is a unit of the one and not of the block. The distinction is exactly the distinction between the two products: an equation that names a product has its solutions in the elements selected by that product, and the idempotent equation of the block selects $e_0$ while the unit equation of the block has no solution.

## The Absence of a Bijection with the Roots of Minus One

**Theorem (no bijection).** There is no root of $-1$ in the block, so the idempotents $0$ and $e_0$ are not in bijection with the roots of $-1$.

*Proof.* A root of $-1$ would be a nonzero $\tilde{Q}$ with $\tilde{Q}\star\tilde{Q} = -e_0$, that is $H(\tilde{Q}) = -1$, impossible for a sum of squares of moduli (*Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Sesqualgebra*).

**Remark (what the absence removes).** In the plain product the map $\tilde{Q}\mapsto\tfrac12(e_0 + \tilde{Q} i)$ is a bijection between the roots of $-1$ and the nontrivial idempotents, and it is the reason the idempotent classification is a root classification (*Idempotents of the General Plain Algebra*). The block has no root of $-1$, and the map has no domain; the idempotents are two isolated points and their classification is the two-element solution of the equation $\lvert\lambda\rvert^{2} = \lambda$. The idempotent theory of the block is therefore not a root theory, and the root sets of the block carry no idempotent classification.

## The Idempotents as Projections

**Theorem (both idempotents are projections).** The two idempotents $0$ and $e_0$ are fixed by the three conjugations, $\tilde\Pi^{*} = \tilde\Pi$, so both are projections of the sesqualgebra in the sense of the star-fixed idempotents.

*Proof.* $0$ and $e_0$ are real central elements; the natural conjugation fixes the scalar line, the coefficientwise conjugation fixes the real line, and the Hermitian conjugation is their composite, so all three fix $e_0$ and $0$.

**Remark (the projections are the minimum).** The projections of the block are the two idempotents, and the idempotent theory of the sesqualgebra, which cuts the general plain sesquilinear product into its Peirce pieces, restricts here to these two points (*Idempotents of the General Plain Sesqualgebra*). The element $e_0$ is a projection of the block and of the plain product at once; the difference is that the block has no unit, so the projection of the block onto the central line is not the identity of the block.

## The Absence of a Peirce Decomposition

**Proposition (no Peirce decomposition).** The block has no Peirce decomposition attached to its idempotents.

*Proof.* The Peirce decomposition is built from an idempotent $\tilde\Pi$ together with the complementary idempotent $e - \tilde\Pi$, where $e$ is a two-sided unit; the four pieces are the corners of the algebra relative to the pair. Without a unit there is no complement, and the block has no unit; the construction is unavailable.

**Remark (what replaces it).** The block's structural decomposition is the orthogonal direct sum $\mathbb{B} = \mathbb{C}e_0\oplus\mathrm{Vect}(\mathbb{B})$ into the central line and the vector subspace, and it is the decomposition by the scalar coordinate, not the Peirce decomposition. The idempotent $e_0$ projects onto the central line in the sense that $\tilde{Q}\star e_0 = Q_0e_0$ is the central part of $\tilde{Q}$; the other piece, the vector part, is not the image of an idempotent of the block, because the block has no second idempotent. The decomposition is a decomposition by a projection-like map of the operator algebra, and it is in *The Multiplication Operators of the Symmetric Plain Sesqualgebra*.

## The Relation to the Parents and the Siblings

The idempotents of the four symmetric structures come in two kinds, a positive-dimensional family for the symmetric plain algebra and the two points for the three others, and the block is of the two-point kind. The table collects the comparison.

| structure | product | idempotents | index set |
|---|---|---|---|
| $\mathrm{SPA}$ | $\tfrac12(\tilde P\tilde Q + \tilde Q\tilde P)$ | the two families $\tfrac12(e_0 + \tilde\Xi i)$ with $\tilde\Xi$ a square root of $-1$ | the roots of $-1$ |
| $\mathrm{SQA}$ | $N(\tilde P,\tilde Q)e_0$ | $0$ and $e_0$ | two points |
| $\mathrm{SPS}$ | $H(\tilde P,\tilde Q)e_0$ | $0$ and $e_0$ | two points |
| $\mathrm{SQS}$ | $\tfrac12(\tilde P^{\natural}\tilde Q^{*} + \tilde Q^{*}\tilde P^{\natural})$ | $0$ and $e_0$ | two points |

The plain sibling is the one with a unit and the one whose product has a vector part, and it alone carries a positive-dimensional idempotent family; the two central blocks carry the two points, and among them the block is distinguished not by the idempotents but by the image and the sign of its form. The comparison with the general plain product, whose idempotents are the two standard ones $\tilde\Pi_1$ and $\tilde\Pi_2$ and the complex multiples, is *Idempotents of the General Plain Algebra*.

## Summary

The idempotents of the symmetric plain sesqualgebra, the elements with $\tilde\Pi\star\tilde\Pi = \tilde\Pi$, are exactly $0$ and $e_0$. The proof is the square map: the square is central, so an idempotent is central, $\tilde\Pi = \lambda e_0$, and on the centre the equation reads $\lvert\lambda\rvert^{2} = \lambda$, whose roots are $0$ and $1$. The element $e_0$ is an idempotent and **not a unit**: $\tilde{Q}\star e_0 = Q_0e_0$ and $e_0\star\tilde{Q} = \overline{Q_0}e_0$, so no element with a vector part is reproduced, and the block has no unit. Both idempotents are fixed by the three conjugations and are therefore projections; the **Peirce decomposition** is unavailable, because it needs a unit and its complement, and what replaces it is the decomposition $\mathbb{B} = \mathbb{C}e_0\oplus\mathrm{Vect}(\mathbb{B})$ by the scalar coordinate. The bijection between the idempotents and the roots of $-1$ **fails**, because the block has no root of $-1$; the idempotent classification of the block is the two-point solution of a scalar equation and not a root theory. Among the four symmetric products the block carries the two-point idempotent set, the smallest possible after the trivial one, and it shares the set with its central sibling $\mathrm{SQA}$ and its sesquilinear sibling $\mathrm{SQS}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q = H(\tilde P,\tilde Q)e_0$ | the product of the block |
| $H(\tilde{Q}) = H(\tilde{Q},\tilde{Q}) = \sum_\mu\lvert Q_\mu\rvert^{2}$ | the algebraic norm of the block, real and non-negative |
| $\tilde\Pi\star\tilde\Pi = \tilde\Pi$ | the idempotent equation of the block |
| $(\lambda e_0)\star(\mu e_0) = \lambda\overline{\mu}e_0$ | the product on the centre |
| $\lvert\lambda\rvert^{2} = \lambda$ | the idempotent equation on the centre |
| $\{0, e_0\}$ | the idempotents of the block |
| $\tilde{Q}\star e_0 = Q_0e_0$, $e_0\star\tilde{Q} = \overline{Q_0}e_0$ | the failure of $e_0$ as a unit |
| $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_0$ | the centre of $\mathbb{B}$ |
| $\mathbb{B} = \mathbb{C}e_0\oplus\mathrm{Vect}(\mathbb{B})$ | the decomposition that replaces the Peirce one |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product, its class and its placement.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the relative definition of the idempotent, the orthogonal and complete families and the projection.
- *Norm and Invertibility in the Symmetric Plain Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-plain-sesqualgebra.md`), for the square map and the absence of a unit.
- *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Sesqualgebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-symmetric-plain-sesqualgebra.md`), for the rootlessness of $-1$ that removes the bijection.
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra.md`), for the idempotents of the parent, their classification and the Peirce decomposition.
- *Idempotents of the General Plain Sesqualgebra* (`articles_maths/idempotents-of-the-general-plain-sesqualgebra.md`), for the idempotents of the general plain sesquilinear product.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra* (`articles_maths/the-square-the-idempotents-and-the-jordan-inverse-of-the-symmetric-plain-algebra.md`), for the two idempotent families of the plain sibling.
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), for the two idempotents of the quaternionic sibling.
