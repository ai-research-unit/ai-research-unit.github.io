# __Norm and Invertibility in the General Quaternionic Sesqualgebra__

## Introduction

A **unit** of a product $\star$ is an element $\tilde E$ with $\tilde E\star\tilde X = \tilde X\star\tilde E = \tilde X$ for every $\tilde X$, an **inverse** of $\tilde X$ is an element $\tilde Y$ with $\tilde X\star\tilde Y = \tilde Y\star\tilde X = \tilde E$, and $\tilde X$ is **invertible** when it has an inverse; the definitions are *Definitions for the Study of the 12 Algebraic Structures*. This article fixes the product to the **general quaternionic sesquilinear product**

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*}
$$

of *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*, and it answers the two questions of its title. The answer is a **double absence**, stated as a law, together with the two algebraic norms that do exist and the plain invertibility criterion that replaces the missing one.

The two actions of $e_0$ are the star and the natural conjugation, $\tilde Q\star e_0 = \tilde Q^{\natural}$ and $e_0\star\tilde Q = \tilde Q^{*}$, so no element is a two-sided unit and the block has **no unit, no inverse and no invertible element**; the absence is proved in *The Two One-Sided Actions and the Absence of a Unit*. What survives is the **norm of the plain algebra**, the central square $c(\tilde Q) = \sum_\mu Q_\mu^2$ of *Norm and Invertibility in the General Plain Algebra*, whose non-vanishing is the plain invertibility criterion, and the **Krein form** of the block, the indefinite form of *The Krein Gram Matrix and the Restrictions of the Form*. Neither is multiplicative for $\star$: the central square obeys the twisted law $c(\tilde P\star\tilde Q) = c(\tilde P)\,\overline{c(\tilde Q)}$, and the Krein form is not multiplicative at all. The article states the absence, then the two quadratic objects, then the twisted law, then the classes of the block that are units of the plain algebra, and it closes with the absence law.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0 = 1, e_1, e_2, e_3$ with $e_1e_2 = e_3$ and central scalar imaginary $i$. An element is $\tilde Q = Q_0e_0+\mathbf Q$. The conjugations are $\tilde Q^{\natural} = Q_0-\mathbf Q$, $\tilde Q^{*} = \overline{\tilde Q^{\natural}}$, $\overline{\tilde Q} = \tilde Q^{\natural*} = \tilde Q^{*\natural}$. The **central square** is $c(\tilde Q) = \sum_\mu Q_\mu^2$ with $c(\tilde Q)e_0 = \tilde Q\tilde Q^{\natural}$; the **Krein form** is $K(\tilde P,\tilde Q) = \mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*}) = \sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ with $\varepsilon = (1,-1,-1,-1)$. The product is $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$, with the natural conjugation ${}^{\natural}$ in the first slot and the star ${}^{*}$ in the second; juxtaposition is the general plain bilinear product.

## The Double Absence

**Proposition (the two one-sided actions of $e_0$).** For every $\tilde Q$,

$$
e_0\star\tilde Q = \tilde Q^{*} , \qquad \tilde Q\star e_0 = \tilde Q^{\natural} ,
$$

so the left action of $e_0$ is the star and the right action is the natural conjugation.

**Proof.** $e_0\star\tilde Q = e_0^{\natural}\tilde Q^{*} = e_0\tilde Q^{*} = \tilde Q^{*}$, and $\tilde Q\star e_0 = \tilde Q^{\natural}e_0^{*} = \tilde Q^{\natural}$.

**Theorem (no unit, no inverse, no invertible element).** The product $\star$ has no left unit, no right unit and no two-sided unit; no element has an inverse; and the set of invertible elements of $\star$ is empty.

**Proof.** A left unit $\tilde E$ would satisfy $\tilde E\star\tilde Q = \tilde Q$ for every $\tilde Q$, and at $\tilde Q = e_0$ this reads $\tilde E\star e_0 = e_0$, that is $\tilde E^{\natural} = e_0$ by the proposition, so $\tilde E = e_0$; but $e_0\star\tilde Q = \tilde Q^{*}$ is not $\tilde Q$ for every $\tilde Q$, for instance at $\tilde Q = e_1$, so there is no left unit. The same computation at $\tilde Q = e_0$ for a right unit gives $\tilde E^{*} = e_0$, hence $\tilde E = e_0$, and $e_0$ is not a right unit because $\tilde Q\star e_0 = \tilde Q^{\natural}$ is not $\tilde Q$ at $\tilde Q = e_1$. A two-sided unit would be both, so there is none. An inverse requires a unit in its definition, so no inverse exists, and the set of invertible elements is empty. The same statements, with the monoid and the one-sided families, are *The Two One-Sided Actions and the Absence of a Unit*, where the left and the right multiplications of the block are computed as well.

**Corollary (the absence and the element classes).** The concepts of §*The Nilpotents*, §*The Idempotents* and the roots of a central value of the block are read **without** a unit: an idempotent is an element equal to its square and not a projection onto the unit, a nilpotent is an element of vanishing square and not a multiple of a unit, and a root of $\lambda$ is an element of square $\lambda e_0$ and not the product of a unit with a root of $\lambda$ in the plain algebra.

**Proof.** Each definition names only the product and $e_0$, and none of them names a unit; the corollary is the reading of *Definitions for the Study of the 12 Algebraic Structures* with the theorem above.

## The Two Algebraic Norms

Two quadratic objects of the space are attached to the block, and they are the two halves of the square.

**Proposition (the central square).** The element $c(\tilde Q) = \sum_\mu Q_\mu^2$ satisfies

$$
c(\tilde Q)e_0 = \tilde Q\tilde Q^{\natural} = \tilde Q^{\natural}\tilde Q ,
$$

it is the **norm of the general plain algebra**, it vanishes exactly on the zero-divisor cone, and its non-vanishing is the invertibility criterion of the plain product.

**Proof.** The identity is the definition of $c$ and the commutativity of $\tilde Q$ with $\tilde Q^{\natural}$; the vanishing on the cone is *Zero Divisors of the General Quaternionic Sesqualgebra*, and the criterion is *Norm and Invertibility in the General Plain Algebra*.

**Proposition (the Krein form).** The scalar part of the square is the **Krein form**

$$
\mathrm{Sc}\bigl(\tilde P\star\tilde Q\bigr) = K(\tilde P,\tilde Q) = \sum_\mu \varepsilon_\mu P_\mu\overline{Q_\mu} , \qquad \varepsilon = (1,-1,-1,-1) ,
$$

a form of signature $(2,6)$ on the real space.

**Proof.** The scalar part of $\tilde P^{\natural}\tilde Q^{*}$ is $\sum_\mu \varepsilon_\mu P_\mu\overline{Q_\mu}$ with $\varepsilon = (1,-1,-1,-1)$, as in *The Krein Gram Matrix and the Restrictions of the Form*; the inertia is the one of the four entries $1,-1,-1,-1$ read on the eight real coordinates, two positive and six negative.

**Theorem (the twisted multiplicativity).** For all $\tilde P,\tilde Q$,

$$
c\bigl(\tilde P\star\tilde Q\bigr) = c(\tilde P)\,\overline{c(\tilde Q)} ,
$$

and in particular $\lvert c(\tilde P\star\tilde Q)\rvert = \lvert c(\tilde P)\rvert\,\lvert c(\tilde Q)\rvert$; the central square is **not** multiplicative, and the Krein form is not multiplicative either.

**Proof.** The central square is multiplicative for the plain product, $c(\tilde X\tilde Y) = c(\tilde X)c(\tilde Y)$, and the three conjugations act on it by $c(\tilde Q^{\natural}) = c(\tilde Q)$, $c(\tilde Q^{*}) = \overline{c(\tilde Q)}$ and $c(\overline{\tilde Q}) = \overline{c(\tilde Q)}$, all three being read on the four coordinates. Hence $c(\tilde P\star\tilde Q) = c(\tilde P^{\natural})c(\tilde Q^{*}) = c(\tilde P)\overline{c(\tilde Q)}$. The first display shows that $c$ is not multiplicative; for the Krein form, $K(\tilde P\star\tilde Q,\tilde P\star\tilde Q)$ is the scalar part of $\overline{(\tilde P\star\tilde Q)}(\tilde P\star\tilde Q)$, which is not $K(\tilde P,\tilde P)K(\tilde Q,\tilde Q)$ in general. The law is *The Annihilating Elements of the Four General Products*, where it is read for the four products.

So the block has a quadratic object that behaves under the product only up to the complex conjugation of one factor. That is the price of the two slot conjugations, and it is the reason the block is not a normed object in the algebraic sense: the product does not respect either quadratic form.

## The Units of the Plain Algebra

The invertibility that the block does not have is available for the plain product, and it separates the element classes.

**Theorem (the element classes and the plain criterion).** An element of the block is a unit of the **plain** product exactly when $c(\tilde Q)\neq0$. Under this criterion,

- the nontrivial idempotents of $\star$ are units of the plain algebra: a nontrivial idempotent $\tilde\Pi = -\tfrac12e_0+\mu$ with $\lvert\mu\rvert^2 = \tfrac34$ has $c(\tilde\Pi) = 1$;
- the roots of $-1$ and of $+1$ are units of the plain algebra;
- the roots of $0$, that is the square-zero elements, are the plain zero divisors;
- the unit $e_0$ of the plain algebra is an idempotent of $\star$ and is not a unit of $\star$.

**Proof.** The plain criterion is *Norm and Invertibility in the General Plain Algebra*. For an idempotent, $c(\tilde\Pi) = \sum_\mu Q_\mu^2$ computed from the parametrization of *Idempotents of the General Quaternionic Sesqualgebra* gives $1$, as the article records. The roots of $-1$ and $+1$ have $c(\tilde P) = c^2(1-t^2)$ with $t^2\neq1$, by *Square Roots of Minus One, Zero and Plus One in the General Quaternionic Sesqualgebra*, hence non-vanishing; the roots of $0$ have $t = \pm1$ and vanishing central square. The last statement is the proposition on the two actions and the theorem above.

**Remark (the plain unit is not a unit of the block).** The element $e_0$ is the unit of the plain product and is a two-sided unit of **no** sesquilinear product of the twelve, because the left action of $e_0$ is the star and the right action is the natural conjugation; the block has no unit, and its nontrivial idempotents are therefore not units **of the block** but units **of the plain algebra**, the corrected reading of the claim that the nontrivial idempotents of the quaternionic sesquilinear product are units.

## The Absence Law

The block has **no unit, no inverse, no invertible element and no multiplicative norm**. The two quadratic objects it carries are the norm of the plain algebra, the central square $c$, and the indefinite form $K$, and neither is multiplicative for $\star$; the central square is twisted by the complex conjugation of one factor. What replaces the missing invertibility is the plain criterion $c\neq0$, which is stated for the plain product and is used in the block as a separating criterion of the element classes. This is a statement of **absence**, recorded as a law, and the article claims no existence of an algebraic norm or of an inverse in the block beyond the twisted law of the central square.

## Summary

The general quaternionic sesquilinear product $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$ has no unit, no inverse and no invertible element: the left action of $e_0$ is the star, $e_0\star\tilde Q = \tilde Q^{*}$, and the right action is the natural conjugation, $\tilde Q\star e_0 = \tilde Q^{\natural}$, so no element is a two-sided unit. The two quadratic objects of the space are the central square $c(\tilde Q) = \sum_\mu Q_\mu^2$, the norm of the plain algebra, vanishing exactly on the zero-divisor cone, and the Krein form $K(\tilde P,\tilde Q) = \sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$, of signature $(2,6)$. The central square obeys the twisted law $c(\tilde P\star\tilde Q) = c(\tilde P)\overline{c(\tilde Q)}$ and is not multiplicative, and the Krein form is not multiplicative.

The invertibility available to the block is the plain criterion $c\neq0$, and it separates the classes: the nontrivial idempotents of the block, the roots of $-1$ and the roots of $+1$ are units of the plain algebra, the square-zero elements are the plain zero divisors, and the plain unit $e_0$ is an idempotent of the block but a unit of no sesquilinear product of the twelve. The block therefore carries an element theory but no division theory.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$ | the general quaternionic sesquilinear product |
| unit, inverse, invertible | relative to a product; the block has none |
| $e_0\star\tilde Q = \tilde Q^{*}$, $\tilde Q\star e_0 = \tilde Q^{\natural}$ | the two actions of $e_0$, star and natural conjugation |
| $c(\tilde Q) = \sum_\mu Q_\mu^2$ | the central square, the norm of the plain algebra |
| $c(\tilde P\star\tilde Q) = c(\tilde P)\overline{c(\tilde Q)}$ | the twisted multiplicativity |
| $K(\tilde P,\tilde Q) = \sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the Krein form, signature $(2,6)$ |
| $c(\tilde Q)\neq0$ | the invertibility criterion of the plain algebra |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the unit, the inverse and the invertible element relative to a product.
- *The Two One-Sided Actions and the Absence of a Unit* (`articles_maths/the-two-one-sided-actions-and-the-absence-of-a-unit.md`), for the proof of the absence and the two one-sided families of the block.
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra.md`), for the central square and the plain invertibility criterion.
- *The Annihilating Elements of the Four General Products* (`articles_maths/the-annihilating-elements-of-the-four-general-products.md`), for the twisted multiplicativity law across the four products.
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the Krein form, its Gram matrix and its signatures.
- *Idempotents of the General Quaternionic Sesqualgebra* (`articles_maths/idempotents-of-the-general-quaternionic-sesqualgebra.md`), for the nontrivial idempotents, units of the plain algebra.
- *Square Roots of Minus One, Zero and Plus One in the General Quaternionic Sesqualgebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-quaternionic-sesqualgebra.md`), for the roots and their central squares.
- *Conventions in Mathematics* (`articles_maths/conventions-in-mathematics.md`), for the notation and the article format.
