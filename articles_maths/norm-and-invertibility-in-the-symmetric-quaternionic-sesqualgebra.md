# __Norm and Invertibility in the Symmetric Quaternionic Sesqualgebra__

## Introduction

This article records what the block, the symmetric quaternionic sesquilinear product
$\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ of
*Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*, carries in the place of a unit,
an inverse and a norm. The answer is negative on the two first counts and precise on the third: the block has
no unit, so it has no inverse and no group of units; the replacing object is the **regularity** of
*Zero Divisors of the Symmetric Quaternionic Sesqualgebra*, and the algebraic norm is the **Krein form** $K$,
which does not detect the zero divisors.

A norm and an inverse name a product, and the product is part of the definition: the unit and the inverse are
stated once for a general product in *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,
§*The Unit and the Inverse*, and the algebraic norm of a product is the diagonal of its scalar-part form,
the definition of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*. For the block the form is
$K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\star\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ and
its diagonal is

$$
K(\tilde Q)=K(\tilde Q,\tilde Q)=\sum_{\mu=0}^{3}\varepsilon_\mu\lvert Q_\mu\rvert^{2}
=\lvert Q_0\rvert^{2}-\lvert Q_1\rvert^{2}-\lvert Q_2\rvert^{2}-\lvert Q_3\rvert^{2},
$$

the symmetric quaternionic sesquilinear algebraic norm, **real and indefinite** of signature $(2,6)$, one of
the four algebraic norms of the space and not one of the other three. The unqualified words *unit*,
*inverse*, *norm* mean the block.

The block's absence of a unit is proved in *Introduction to the Symmetric Quaternionic Sesqualgebra of
Biquaternions* and is recalled here because the whole of the invertibility question depends on it; the article
then reads the algebraic norm, its failure of multiplicativity, the regularity that replaces invertibility,
and the **absence of a criterion**: $K$ does not detect the zero divisors.

**Boundaries.** The product, its class and its two one-sided actions are *Introduction to the Symmetric
Quaternionic Sesqualgebra of Biquaternions* and *The Two One-Sided Actions and the Absence of a Unit*; the
zero divisors and the regular elements are *Zero Divisors of the Symmetric Quaternionic Sesqualgebra*; the
operators are *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*; the form $K$ and its
isotropy are *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* and *The Isotropic
Structure of the General Quaternionic Sesqualgebra*; the algebraic norm of the plain product is $B$, a
different form, and its theory is *Norm and Invertibility in the General Plain Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$,
$e_k^2=-e_0$ and $e_1e_2=e_3$; $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$ and central
scalar imaginary $i$; $\vec Q=\sum_kQ_ke_k$; $(\vec P,\vec Q)=\sum_kP_kQ_k$; ${}^{\natural}$ negates
$e_1,e_2,e_3$ and fixes the coefficients, $\bar{\cdot}$ conjugates the coefficients, and
${}^{*}={}^{\natural}\circ\bar{\cdot}$. The **algebraic norm of the block** is
$K(\tilde Q)=\mathrm{Sc}(\tilde Q\star\tilde Q)=K(\tilde Q,\tilde Q)=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$,
the diagonal of the **Krein form** $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ with
$\varepsilon=(1,-1,-1,-1)$; the square of an element is
$\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\vec Q}-\overline{Q_0}\vec Q$.
Throughout this article the product is the block.

**The results.** The block has no unit, so no element has an inverse and the group of units is empty. It carries one algebraic norm, the Krein form $K(\tilde Q)=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$, real and indefinite of signature $(2,6)$, which is **not multiplicative** and does **not** detect the zero divisors: $K(e_0+e_1)=0$ on a regular element and $K(e_1)=-1$ on a pure zero divisor. Invertibility is replaced by regularity, $Q_0\neq0$ and $C(\tilde Q)\neq0$, where the left multiplication is injective with rank eight, six and four on the regular, non-pure and pure classes and rank zero at the origin.

## Definition

**Definition (unit and inverse of a product).** Let $\star$ be a product on $\mathbb{B}$. An element
$\tilde E$ is a **left unit of $\star$** when $\tilde E\star\tilde X=\tilde X$ for every $\tilde X$, a
**right unit of $\star$** when $\tilde X\star\tilde E=\tilde X$ for every $\tilde X$, and a **unit of
$\star$** when it is both; a unital product has a unit. An element $\tilde Q$ is **invertible in $\star$**
when there is a unit $\tilde E$ of $\star$ and an element $\tilde Q^{-1}$ with
$\tilde Q\star\tilde Q^{-1}=\tilde Q^{-1}\star\tilde Q=\tilde E$; the invertible elements form the **group
of units** of $\star$.

This is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Unit and the Inverse*. Unqualified,
the product is the block.

## The Absence of a Unit and of an Inverse

**The block has no unit, so no element has an inverse and the group of units is empty; the unit candidate $e_0$ is not a unit and acts by the two conjugations, $e_0\star\tilde X=\tilde X^{*}$ and $\tilde X\star e_0=\tilde X^{\natural}$.**

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

## The Algebraic Norm of the Block

**The block carries one algebraic norm, the diagonal of its scalar-part form, $K(\tilde Q)=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}=\lvert Q_0\rvert^{2}-\lvert Q_1\rvert^{2}-\lvert Q_2\rvert^{2}-\lvert Q_3\rvert^{2}$, real and indefinite of signature $(2,6)$, with the $K$-isotropic cone as its vanishing set.**

**Definition.** The **algebraic norm of the block** is the diagonal of the scalar-part form of the product,

$$
K(\tilde Q)=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=K(\tilde Q,\tilde Q)
=\sum_{\mu=0}^{3}\varepsilon_\mu\lvert Q_\mu\rvert^{2},
$$

equivalently $K(\tilde Q)=K(\tilde Q,\tilde Q)$ for the form

$$
K(\tilde P,\tilde Q)=\mathrm{Sc}\bigl(\tilde P\star\tilde Q\bigr)=\sum_{\mu=0}^{3}\varepsilon_\mu P_\mu\overline{Q_\mu},
$$

the general quaternionic sesquilinear form of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, also
called the **Krein form** of the block. The two arities of the letter are one object: with two arguments the
form, with one argument its diagonal.

**Theorem (the square and the algebraic norm).** For every $\tilde Q$ the square is a real quaternion,
$\mathrm{Sc}(\tilde Q\star\tilde Q)=K(\tilde Q)$, and

$$
\tilde Q\star\tilde Q=K(\tilde Q)e_0-Q_0\overline{\vec Q}-\overline{Q_0}\vec Q,
$$

with vector part $-2\mathrm{Re}(Q_0\overline{\vec Q})$.

*Proof.* The scalar part is the diagonal of the Krein form as the scalar part of the product of the block
(*The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*); the rest is the diagonal formula
of *The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic Sesqualgebra*.

**Basic properties.** Each is a direct reading of the definition.

- $K(\tilde Q)$ is **real**, and **indefinite**: the four entries $1,-1,-1,-1$ on the real and the imaginary
  parts of the four coefficients give the inertia $(2,6)$ on the realification $\mathbb{B}\cong\mathbb{R}^{8}$.
- $K$ is **homogeneous of degree two over the reals**, $K(\lambda\tilde Q)=\lvert\lambda\rvert^{2}K(\tilde Q)$
  for $\lambda\in\mathbb{C}$.
- Its polarisation is the sesquilinear form $K(\tilde P,\tilde Q)$, and
  $K(\tilde Q,\tilde P)=\overline{K(\tilde P,\tilde Q)}$: the form is Hermitian.
- Its **vanishing set** is the $K$-isotropic cone, a nonzero cone: $K(e_0+e_1)=1-1=0$, so the algebraic norm
  vanishes on nonzero elements.

## The Algebraic Norm Is Not Multiplicative

**Neither the algebraic norm nor the square map is multiplicative: $K(\tilde P\star\tilde Q)\neq K(\tilde P)K(\tilde Q)$ and $(\tilde P\star\tilde Q)\star(\tilde P\star\tilde Q)\neq(\tilde P\star\tilde P)\star(\tilde Q\star\tilde Q)$ in general, the pair $e_3,e_2$ separating both.**

**Theorem (neither the algebraic norm nor the square is multiplicative).** For the block,

$$
K(\tilde P\star\tilde Q)\neq K(\tilde P)\,K(\tilde Q)\quad\text{in general},
$$

and the square map is not multiplicative,
$(\tilde P\star\tilde Q)\star(\tilde P\star\tilde Q)\neq(\tilde P\star\tilde P)\star(\tilde Q\star\tilde Q)$.

*Proof.* Take $\tilde P=e_3$ and $\tilde Q=e_2$. For the algebraic norm,
$K(e_3\star e_2)=K(0)=0$ while $K(e_3)K(e_2)=(-1)(-1)=1$. For the square map,
$(e_3\star e_2)\star(e_3\star e_2)=0\star0=0$ while
$(e_3\star e_3)\star(e_2\star e_2)=(-e_0)\star(-e_0)=e_0$. The values use
$e_3\star e_2=0$ and $e_k\star e_k=-e_0$ of the table.

## Regularity in the Place of Invertibility

**Invertibility is replaced by regularity: the left multiplication $L^{\star}_{\tilde Q}$ is injective exactly when $\tilde Q$ is regular, $Q_0\neq0$ and $C(\tilde Q)\neq0$, and it then has rank eight, six and four on the regular, non-pure zero-divisor and pure zero-divisor classes and rank zero at the origin.**

The absence of a unit does not leave the block without an invertibility notion; it replaces the invertibility
of the element by the injectivity of its multiplication operator.

**Theorem (the element and its operator).** For $\tilde Q\in\mathbb{B}$ the left multiplication
$L^{\star}_{\tilde Q}:\tilde X\mapsto\tilde Q\star\tilde X$ is injective if and only if $\tilde Q$ is
regular, and then it is a conjugate-linear bijection of $\mathbb{B}$; when $\tilde Q$ is a zero divisor the
rank is six in the non-pure family $\{Q_0\neq0,\ C(\tilde Q)=0\}$ and four in the pure family $\{Q_0=0\}$,
and the rank is zero at the origin.

*Proof.* The kernel of $L^{\star}_{\tilde Q}$ is the annihilator
$A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\}$, of real dimension zero, two and four according to
whether $\tilde Q$ is regular, a non-pure zero divisor or a pure zero divisor
(*Zero Divisors of the Symmetric Quaternionic Sesqualgebra*), and of dimension eight at the origin; the rank
is eight minus the dimension of the kernel. The origin is neither regular nor a zero divisor, so it is the
one kernel outside the two families, and $L^{\star}_{\tilde Q}$ is conjugate-linear because the second slot
of the block is conjugate-linear.

So the largest class on which the block's multiplication is faithful is the set of the regular elements,
$Q_0\neq0$ and $C(\tilde Q)\neq0$. Every nonzero idempotent of the block is regular
(*Idempotents of the Symmetric Quaternionic Sesqualgebra*), and no nonzero nilpotent is; the regular elements
are the substitute for the invertible ones that the absence of a unit leaves, and they are the elements on
which the operator calculus of *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra* is a
group-like structure without being a group.

## The Absence of a Criterion from the Algebraic Norm

**The algebraic norm does not detect the zero divisors: $K(\tilde Q)=0$ does not force $\tilde Q$ to be a zero divisor, and a zero divisor need not have $K(\tilde Q)=0$, the witnesses being the regular $e_0+e_1$ with $K=0$ and the pure zero divisor $e_1$ with $K=-1$.**

**Theorem (the algebraic norm does not detect the zero divisors).** The block has no invertible element, so
no criterion can name one; and the algebraic norm does not decide the zero-divisor class either, the two
implications

$$
K(\tilde Q)=0\ \Longrightarrow\ \tilde Q\text{ is a zero divisor},
\qquad
\tilde Q\text{ is a zero divisor}\ \Longrightarrow\ K(\tilde Q)=0
$$

both failing.

*Proof.* $K(e_0+e_1)=|1|^2-|1|^2=0$ while the central square is $c(e_0+e_1)=1+1=2\neq0$, so $e_0+e_1$ is
regular and the first implication fails. $K(e_1)=-1\neq0$ while $e_1$ is a pure zero divisor, since
$e_1\star e_2=0$, so the second fails.

**Remark (what carries the class).** The algebraic norm vanishes on the regular isotropic elements and does
not vanish on the pure zero divisors, so the zero-divisor class is carried by the scalar part $Q_0$ and the
central square $C$, and not by $K$. The isotropic elements of $K$ are computed in *The Isotropic Structure of
the General Quaternionic Sesqualgebra* and its restriction to the block in *The Krein Form as a Product on
the Symmetric Quaternionic Sesqualgebra*.

## Worked Examples

**A value with no inverse.** $\tilde Q=e_1$: the equation $e_1\star\tilde Y=\tilde E$ has no solution with a
unit $\tilde E$, since there is no unit; and $\tilde Q$ is a pure zero divisor, so its left multiplication
has rank four and is not injective.

**A regular element whose left multiplication is a bijection.** $\tilde Q=e_0+e_1$: $Q_0=1$ and
$C=2\neq0$, so it is regular; $L^{\star}_{\tilde Q}$ is a conjugate-linear bijection, though $\tilde Q$ has
no inverse.

**A multiplicativity failure.** $\tilde P=e_3$, $\tilde Q=e_2$: the algebraic norm gives
$0\neq1$ and the square map gives $0\neq e_0$.

**The unit candidate.** $\tilde Q=e_0$: $e_0\star(e_0+e_1)=e_0-e_1$, so the element $e_0$ does not fix the
block; it is an idempotent and a root of $+1$ and not a unit.

## Summary

The block has no unit, so no element has an inverse and the group of units is empty; the unit candidate $e_0$
acts by the two conjugations instead, $e_0\star\tilde X=\tilde X^{*}$ and
$\tilde X\star e_0=\tilde X^{\natural}$. It carries one algebraic norm, the diagonal of its scalar-part form,
the symmetric quaternionic sesquilinear algebraic norm

$$
K(\tilde Q)=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\sum_{\mu=0}^{3}\varepsilon_\mu\lvert Q_\mu\rvert^{2}
=\lvert Q_0\rvert^{2}-\lvert Q_1\rvert^{2}-\lvert Q_2\rvert^{2}-\lvert Q_3\rvert^{2},
$$

real, indefinite of signature $(2,6)$, also called the Krein form, with the $K$-isotropic cone as its
vanishing set; it is **not multiplicative**, the pair $e_3,e_2$ separating the two sides,
$K(e_3\star e_2)=K(0)=0$ against $K(e_3)K(e_2)=1$, and the square map is not multiplicative either.
Invertibility is replaced by regularity: the left multiplication of $\tilde Q$ is injective exactly when
$\tilde Q$ is regular, $Q_0\neq0$ and $C(\tilde Q)\neq0$, and has rank eight, six and four on the regular
elements, the non-pure zero divisors and the pure zero divisors, and rank zero at the origin. The article
records the **absence of a criterion**: the algebraic norm does not detect the zero divisors, vanishing on
the regular $e_0+e_1$ and not on the pure zero divisor $e_1$; the class is carried by the scalar part and the
central square, not by $K$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde E\star\tilde X=\tilde X$ (left), $\tilde X\star\tilde E=\tilde X$ (right) | the unit equations; the block has no solution |
| $\tilde Q\star\tilde Q^{-1}=\tilde Q^{-1}\star\tilde Q=\tilde E$ | the inverse equation; empty without a unit |
| $K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\star\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the Krein form, the scalar-part form of the product |
| $K(\tilde Q)=K(\tilde Q,\tilde Q)=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ | the algebraic norm of the block, one of the four algebraic norms of the space |
| $\tilde Q\star\tilde Q=K(\tilde Q)e_0-Q_0\overline{\vec Q}-\overline{Q_0}\vec Q$ | the square, a real quaternion with scalar part $K(\tilde Q)$ |
| $K(\tilde P\star\tilde Q)\neq K(\tilde P)K(\tilde Q)$ | the failure of multiplicativity |
| $Q_0\neq0,\ C(\tilde Q)\neq0$ | the regular elements, the substitute for the invertible ones |
| $\mathrm{rank}\,L^{\star}_{\tilde Q}\in\{8,6,4,0\}$ | the ranks: regular, non-pure divisor, pure divisor, origin |

## Further Reading

- *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternioid-c-space.md`), for the definition of the algebraic norm as the form at the two equal arguments and the four algebraic norms of the space.
- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`), for the general quaternionic sesquilinear form $K$ and the table of the four forms.
- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), §*The Unit and the Inverse*, for the definitions relative to a general product and for the unit tables.
- *The Two One-Sided Actions and the Absence of a Unit* (`articles_maths/the-two-one-sided-actions-and-the-absence-of-a-unit.md`), for the two actions of $e_0$ and the proof that no element is a unit.
- *Norm and Invertibility in the General Plain Algebra* (`articles_maths/norm-and-invertibility-in-the-biquaternion-algebra.md`), for the algebraic norm $B$ of the plain product, which is not the form $K$ of this article.
- *Zero Divisors of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-sesqualgebra.md`), for the criterion of the zero divisors and the regular elements.
- *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-sesqualgebra.md`), for the operators whose kernels give the ranks.
- *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-krein-form-as-a-product-on-the-symmetric-quaternionic-sesqualgebra.md`), for the form that is the scalar part of the square.
