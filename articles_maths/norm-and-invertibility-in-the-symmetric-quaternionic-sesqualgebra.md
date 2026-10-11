# __Norm and Invertibility in the Symmetric Quaternionic Sesqualgebra__

## Introduction

This article records what the block, the symmetric quaternionic sesquilinear product
$\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ of
*Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*, carries in the place of a unit,
an inverse and a norm. The answer is negative on the two first counts and partial on the third: the block has
no unit, so it has no inverse and no group of units; the replacing object is the **regularity** of
*Zero Divisors of the Symmetric Quaternionic Sesqualgebra*, and the norm-like object is the **Krein form**
$K$, which does not detect the zero divisors.

The unit and the inverse are relative to a product, and the product is part of the definition: they are
stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures*,
§*The Unit and the Inverse*, and read on the products of the space. The unqualified
words mean the block. The block's absence of a unit is proved in *Introduction to the Symmetric Quaternionic
Sesqualgebra of Biquaternions* and is recalled here because the whole of the invertibility question depends
on it; the article then reads the two quadratic objects of the block, the square map and the form, and the
multiplication operators, which are the only sense in which invertibility survives.

The product, its class and its two one-sided actions are *Introduction to the Symmetric Quaternionic
Sesqualgebra of Biquaternions* and *The Two One-Sided Actions and the Absence of a Unit*; the zero divisors
and the regular elements are *Zero Divisors of the Symmetric Quaternionic Sesqualgebra*; the operators are
*The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*; the form $K$ and its isotropy are
*The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* and *The Isotropic Structure of the
General Quaternionic Sesqualgebra*; and the plain norm is *Norm and Invertibility in the General Plain
Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$,
$e_k^2=-e_0$ and $e_1e_2=e_3$; $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$ and central
scalar imaginary $i$; $\mathbf Q=\sum_kQ_ke_k$; $(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$; ${}^{\natural}$ negates
$e_1,e_2,e_3$ and fixes the coefficients, $\bar{\cdot}$ conjugates the coefficients, and
${}^{*}={}^{\natural}\circ\bar{\cdot}$. The **plain norm** is
$N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^2$, the **central square** is the same expression
$c(\tilde Q)$, the **Krein form** is $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$
with $\varepsilon=(1,-1,-1,-1)$, and the diagonal of the block is
$\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf Q}-\overline{Q_0}\mathbf Q$.
Throughout this article the product is the block.

## Definition

**Definition (unit and inverse of a product).** Let $\star$ be a product on $\mathbb{B}$. An element
$\tilde E$ is a **left unit of $\star$** when $\tilde E\star\tilde X=\tilde X$ for every $\tilde X$, a
**right unit of $\star$** when $\tilde X\star\tilde E=\tilde X$ for every $\tilde X$, and a **unit of
$\star$** when it is both; a unital product has a unit. An element $\tilde Q$ is **invertible in $\star$**
when there is a unit $\tilde E$ of $\star$ and an element $\tilde Q^{-1}$ with
$\tilde Q\star\tilde Q^{-1}=\tilde Q^{-1}\star\tilde Q=\tilde E$; the invertible elements form the **group
of units** of $\star$.

This is *Definitions for the Study of the 12 Algebraic Structures*, §*The Unit and the Inverse*. Unqualified,
the product is the block.

## The Absence of a Unit and of an Inverse

**Theorem (the block has no unit).** The block has no left unit and no right unit; in particular it has no
unit.

*Proof.* If $\tilde E$ is a left unit then $\tilde E\star e_0=e_0$. Evaluating the product at $e_0$ gives
$\tilde E\star e_0=\tfrac12\bigl(\tilde E^{\natural}e_0+e_0\tilde E^{\natural}\bigr)=\tilde E^{\natural}$,
so $\tilde E^{\natural}=e_0$, hence $\tilde E=e_0$. But then
$e_0\star e_1=\tfrac12\bigl(e_0(-e_1)+(-e_1)e_0\bigr)=-e_1\neq e_1$, so $e_0$ is not a left unit and
there is none. If $\tilde E$ is a right unit then $e_0\star\tilde E=e_0$; evaluating gives
$e_0\star\tilde E=\tfrac12\bigl(e_0\tilde E^{*}+\tilde E^{*}e_0\bigr)=\tilde E^{*}$, so $\tilde E^{*}=e_0$
and $\tilde E=e_0$, but $e_1\star e_0=\tfrac12\bigl((-e_1)e_0+e_0(-e_1)\bigr)=-e_1\neq e_1$, so there is no
right unit.

**Corollary (the block has no inverse and an empty group of units).** No element of the block is invertible,
and the group of units of the block is empty.

*Proof.* The definition of an inverse requires a unit of the product; the block has none, so the defining
relation of an inverse has no right-hand side and no element satisfies it. The group of units is the set of
the invertible elements, hence empty.

**Remark (what $e_0$ does instead).** The unit candidate $e_0$ is not a unit, but its two one-sided actions
are the two conjugations, $e_0\star\tilde X=\tilde X^{*}$ and $\tilde X\star e_0=\tilde X^{\natural}$, so
$e_0\star\tilde X=\tilde X$ holds exactly for the Hermitian elements and $\tilde X\star e_0=\tilde X$
exactly for the real ones; on $e_0+e_1$, $e_0\star(e_0+e_1)=e_0-e_1$, so the unit candidate fails at the
first witness. The two actions are *The Two One-Sided Actions and the Absence of a Unit*.

## The Two Quadratic Objects

**Theorem (the square and the form).** For every $\tilde Q$,
$\mathrm{Sc}(\tilde Q\star\tilde Q)=K(\tilde Q,\tilde Q)$, real, and
$\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf Q}-\overline{Q_0}\mathbf Q$, which is a
real quaternion with scalar part $K(\tilde Q,\tilde Q)$ and vector part $-2\mathrm{Re}(Q_0\overline{\mathbf Q})$.

*Proof.* The scalar part is the definition of the Krein form as the product of the block
(*The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*); the rest is the diagonal formula
of *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra*.

So the block carries two quadratic objects: the **square map** $\tilde Q\mapsto\tilde Q\star\tilde Q$, whose
scalar part is the form $K$, and the **plain norm** $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^2$
of the general plain algebra. The first is the block's own; the second is inherited and is the quadratic form
of the product whose symmetric part would be the block's companion in the plain row. The plain norm is
multiplicative for the plain product (*Norm and Invertibility in the General Plain Algebra*); for the block
it is not, and neither is the form.

**Theorem (neither quadratic object is multiplicative).** The form and the norm fail multiplicativity for the
block:

$$
K(\tilde P\star\tilde Q,\tilde P\star\tilde Q)\neq K(\tilde P,\tilde P)\,K(\tilde Q,\tilde Q),
\qquad
N(\tilde P\star\tilde Q)\neq N(\tilde P)\,N(\tilde Q),
$$

and the square map is not multiplicative,
$(\tilde P\star\tilde Q)\star(\tilde P\star\tilde Q)\neq(\tilde P\star\tilde P)\star(\tilde Q\star\tilde Q)$.

*Proof.* Take $\tilde P=e_3$ and $\tilde Q=e_2$. For the form,
$K(e_3\star e_2,e_3\star e_2)=K(0,0)=0$ while
$K(e_3,e_3)K(e_2,e_2)=(-1)(-1)=1$. For the norm,
$N(e_3\star e_2)=N(0)=0$ while $N(e_3)N(e_2)=1\cdot1=1$ (the norm here is the plain norm, whose signs are
absent: $N(e_k)=1$ for every $k$, in contrast with $K(e_k,e_k)=-1$). For the square map,
$(e_3\star e_2)\star(e_3\star e_2)=0\star0=0$ while
$(e_3\star e_3)\star(e_2\star e_2)=(-e_0)\star(-e_0)=e_0$. The values use
$e_3\star e_2=0$ and $e_k\star e_k=-e_0$ of the table.

## Regularity in the Place of Invertibility

The absence of a unit does not leave the block without an invertibility notion; it replaces the invertibility
of the element by the injectivity of its multiplication operator.

**Theorem (the element and its operator).** For $\tilde Q\in\mathbb{B}$ the left multiplication
$L^{\star}_{\tilde Q}:\tilde X\mapsto\tilde Q\star\tilde X$ is injective if and only if $\tilde Q$ is
regular, and then it is a conjugate-linear bijection of $\mathbb{B}$; when $\tilde Q$ is a zero divisor the
rank is six in the non-pure family $\{Q_0\neq0,\ c(\tilde Q)=0\}$ and four in the pure family $\{Q_0=0\}$,
and the rank is zero at the origin.

*Proof.* The kernel of $L^{\star}_{\tilde Q}$ is the annihilator
$A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\}$, of real dimension zero, two and four according to
whether $\tilde Q$ is regular, a non-pure zero divisor or a pure zero divisor
(*Zero Divisors of the Symmetric Quaternionic Sesqualgebra*), and of dimension eight at the origin; the rank
is eight minus the dimension of the kernel. The origin is neither regular nor a zero divisor, so it is the
one kernel outside the two families, and $L^{\star}_{\tilde Q}$ is conjugate-linear because the second slot
of the block is conjugate-linear.

So the largest class on which the block's multiplication is faithful is the set of the regular elements,
$Q_0\neq0$ and $c(\tilde Q)\neq0$. Every nonzero idempotent of the block is regular
(*Idempotents of the Symmetric Quaternionic Sesqualgebra*), and no nonzero nilpotent is; the regular elements are the
substitute for the invertible ones that the absence of a unit leaves, and they are the elements on which the
operator calculus of *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra* is a group-like
structure without being a group.

## The Krein Form Does Not Detect the Zero Divisors

**Theorem (the form and the divisor class are independent).** For the block the implications

$$
K(\tilde Q,\tilde Q)=0\ \Longrightarrow\ \tilde Q\text{ is a zero divisor},
\qquad
\tilde Q\text{ is a zero divisor}\ \Longrightarrow\ K(\tilde Q,\tilde Q)=0
$$

both fail.

*Proof.* $K(e_0+e_1,e_0+e_1)=|1|^2-|1|^2=0$ while
$c(e_0+e_1)=1+1=2\neq0$, so $e_0+e_1$ is regular and the first implication fails. $K(e_1,e_1)=-1\neq0$
while $e_1$ is a pure zero divisor, since $e_1\star e_2=0$, so the second fails.

The contrast with the plain product is exact. There the norm $N$ is multiplicative and its vanishing is the
criterion of the zero divisor, so $N$ detects the class; here the form vanishes on the regular isotropic
elements and does not vanish on the pure zero divisors, so the class is carried by the scalar part $Q_0$ and
the central square $c$ and not by $K$. The isotropic elements of $K$ are computed in *The Isotropic Structure
of the General Quaternionic Sesqualgebra* and its restriction to the block in *The Krein Form as a Product on
the Symmetric Quaternionic Sesqualgebra*.

## Worked Examples

**A value with no inverse.** $\tilde Q=e_1$: the equation $e_1\star\tilde Y=\tilde E$ has no solution with a
unit $\tilde E$, since there is no unit; and $\tilde Q$ is a pure zero divisor, so its left multiplication
has rank four and is not injective.

**A regular element whose left multiplication is a bijection.** $\tilde Q=e_0+e_1$: $Q_0=1$ and
$c=2\neq0$, so it is regular; $L^{\star}_{\tilde Q}$ is a conjugate-linear bijection, though $\tilde Q$ has
no inverse.

**Two multiplicativity failures at the same pair.** $\tilde P=e_3$, $\tilde Q=e_2$: the form
gives $0\neq1$ and the norm gives $0\neq1$.

**The unit candidate.** $\tilde Q=e_0$: $e_0\star(e_0+e_1)=e_0-e_1$, so the element $e_0$ does not fix the
block; it is an idempotent and a root of $+1$ and not a unit.

## Summary

The block has no unit, so no element has an inverse and the group of units is empty; the unit candidate $e_0$
acts by the two conjugations instead, $e_0\star\tilde X=\tilde X^{*}$ and
$\tilde X\star e_0=\tilde X^{\natural}$. The two quadratic objects of the block are the square map, whose
scalar part is the Krein form $K$, and the inherited plain norm $N=\tilde Q\tilde Q^{\natural}$; neither is
multiplicative for the block, and the square map is not multiplicative either, the three failures being read
at the pair $e_3,e_2$. Invertibility is replaced by regularity: the left multiplication of $\tilde Q$ is
injective exactly when $\tilde Q$ is regular, $Q_0\neq0$ and $c(\tilde Q)\neq0$, and has rank eight, six and
four on the regular elements, the non-pure zero divisors and the pure zero divisors, and rank zero at the
origin. The Krein form does not
detect the zero divisors, vanishing on the regular $e_0+e_1$ and not on the pure zero divisor $e_1$; the
class is carried by the scalar part and the central square, not by the form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde E\star\tilde X=\tilde X$ (left), $\tilde X\star\tilde E=\tilde X$ (right) | the unit equations; the block has no solution |
| $\tilde Q\star\tilde Q^{-1}=\tilde Q^{-1}\star\tilde Q=\tilde E$ | the inverse equation; empty without a unit |
| $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the Krein form, the scalar part of the square |
| $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^2=c(\tilde Q)$ | the plain norm, the central square |
| $Q_0\neq0,\ c(\tilde Q)\neq0$ | the regular elements, the substitute for the invertible ones |
| $\mathrm{rank}\,L^{\star}_{\tilde Q}\in\{8,6,4,0\}$ | the ranks: regular, non-pure divisor, pure divisor, origin |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Unit and the Inverse*, for the definitions relative to a general product and for the unit tables.
- *The Two One-Sided Actions and the Absence of a Unit* (`articles_maths/the-two-one-sided-actions-and-the-absence-of-a-unit.md`), for the two actions of $e_0$ and the proof that no element is a unit.
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra.md`), for the multiplicative norm and the invertibility criterion of the plain product.
- *Zero Divisors of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-sesqualgebra.md`), for the criterion of the zero divisors and the regular elements.
- *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-sesqualgebra.md`), for the operators whose kernels give the ranks.
- *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-krein-form-as-a-product-on-the-symmetric-quaternionic-sesqualgebra.md`), for the form that is the scalar part of the square.
