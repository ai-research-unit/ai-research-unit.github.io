# __Norm and Invertibility in the Symmetric Quaternionic Sesqualgebra__

## Introduction

This article records what the block, the symmetric quaternionic sesquilinear product
$\tilde Q_1\star\tilde Q_2=\tfrac12(\tilde Q_1^{\natural}\tilde Q_2^{*}+\tilde Q_2^{*}\tilde Q_1^{\natural})$ of
*Introduction to the Symmetric Quaternionic Sesqualgebra*, carries in the place of a unit,
an inverse and a norm. The answer is negative on the two first counts and precise on the third: the block has
no unit, so it has no inverse and no group of units; the replacing object is the **regularity** of
*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, and the algebraic norm is the **Krein form** $\langle\cdot,\cdot\rangle_{\natural*}$,
which does not detect the zero divisors.

A norm and an inverse name a product, and the product is part of the definition: the unit and the inverse are
stated once for a general product in *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,
§*The Unit and the Inverse*, and the algebraic norm of a product is the diagonal of its scalar-part form,
the definition of *The Four Forms and the Four Algebraic Norms*. For the block the form is
$\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)=\sum_\mu\varepsilon_\mu Q_{1,\mu}\overline{Q_{2,\mu}}$ and
its diagonal is

$$
\langle\tilde Q\rangle_{\natural*}=\langle\tilde Q,\tilde Q\rangle_{\natural*}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\lvert Q_\mu\rvert^{2}
=\lvert Q_t\rvert^{2}-\lvert Q_x\rvert^{2}-\lvert Q_y\rvert^{2}-\lvert Q_z\rvert^{2},
$$

the symmetric quaternionic sesquilinear algebraic norm, **real and indefinite** of signature $(2,6)$, one of
the four algebraic norms of the space and not one of the other three. The unqualified words *unit*,
*inverse*, *norm* mean the block.

The block's absence of a unit is proved in *Introduction to the Symmetric Quaternionic Sesqualgebra of
Biquaternions* and is recalled here because the whole of the invertibility question depends on it; the article
then reads the algebraic norm, its failure of multiplicativity, the regularity that replaces invertibility,
and the **absence of a criterion**: $\langle\cdot\rangle_{\natural*}$ does not detect the zero divisors.

**The results.** The block has no unit, so no element has an inverse and the group of units is empty. It carries one algebraic norm, the Krein form $\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$, real and indefinite of signature $(2,6)$, which is **not multiplicative** and does **not** detect the zero divisors: $\langle e_t+\vec e_x\rangle_{\natural*}=0$ on a regular element and $\langle \vec e_x\rangle_{\natural*}=-1$ on a pure zero divisor. Invertibility is replaced by regularity, $Q_t\neq0$ and $C(\tilde Q)\neq0$, where the left multiplication is injective with rank eight, six and four on the regular, non-pure and pure classes and rank zero at the origin.

## Definition

**Definition (unit and inverse of a product).** Let $\star$ be a product on $\mathbb{B}$. An element
$\tilde E$ is a **left unit of $\star$** when $\tilde E\star\tilde Q_1=\tilde Q_1$ for every $\tilde Q_1$, a
**right unit of $\star$** when $\tilde Q_1\star\tilde E=\tilde Q_1$ for every $\tilde Q_1$, and a **unit of
$\star$** when it is both; a unital product has a unit. An element $\tilde Q$ is **invertible in $\star$**
when there is a unit $\tilde E$ of $\star$ and an element $\tilde Q^{-1}$ with
$\tilde Q\star\tilde Q^{-1}=\tilde Q^{-1}\star\tilde Q=\tilde E$; the invertible elements form the **group
of units** of $\star$.

This is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Unit and the Inverse*. Unqualified,
the product is the block.

## The Absence of a Unit and of an Inverse

**The block has no unit, so no element has an inverse and the group of units is empty; the unit candidate $e_t$ is not a unit and acts by the two conjugations, $e_t\star\tilde Q_1=\tilde Q_1^{*}$ and $\tilde Q_1\star e_t=\tilde Q_1^{\natural}$.**

**Theorem (the block has no unit).** The block has no left unit and no right unit; in particular it has no
unit.

*Proof.* If $\tilde E$ is a left unit then $\tilde E\star e_t=e_t$. Evaluating the product at $e_t$ gives
$\tilde E\star e_t=\tfrac12\bigl(\tilde E^{\natural}e_t+e_t\tilde E^{\natural}\bigr)=\tilde E^{\natural}$,
so $\tilde E^{\natural}=e_t$, hence $\tilde E=e_t$. But then
$e_t\star \vec e_x=\tfrac12\bigl(e_t(-\vec e_x)+(-\vec e_x)e_t\bigr)=-\vec e_x\neq \vec e_x$, so $e_t$ is not a left unit and
there is none. If $\tilde E$ is a right unit then $e_t\star\tilde E=e_t$; evaluating gives
$e_t\star\tilde E=\tfrac12\bigl(e_t\tilde E^{*}+\tilde E^{*}e_t\bigr)=\tilde E^{*}$, so $\tilde E^{*}=e_t$
and $\tilde E=e_t$, but $\vec e_x\star e_t=\tfrac12\bigl((-\vec e_x)e_t+e_t(-\vec e_x)\bigr)=-\vec e_x\neq \vec e_x$, so there is no
right unit.

**Corollary (the block has no inverse and an empty group of units).** No element of the block is invertible,
and the group of units of the block is empty.

*Proof.* The definition of an inverse requires a unit of the product; the block has none, so the defining
relation of an inverse has no right-hand side and no element satisfies it. The group of units is the set of
the invertible elements, hence empty.

**Remark (what $e_t$ does instead).** The unit candidate $e_t$ is not a unit, but its two one-sided actions
are the two conjugations, $e_t\star\tilde Q_1=\tilde Q_1^{*}$ and $\tilde Q_1\star e_t=\tilde Q_1^{\natural}$, so
$e_t\star\tilde Q_1=\tilde Q_1$ holds exactly for the Hermitian elements and $\tilde Q_1\star e_t=\tilde Q_1$
exactly for the real ones; on $e_t+\vec e_x$, $e_t\star(e_t+\vec e_x)=e_t-\vec e_x$, so the unit candidate fails at the
first witness. The two actions are *The Two One-Sided Actions and the Absence of a Unit*.

## The Algebraic Norm of the Block

**The block carries one algebraic norm, the diagonal of its scalar-part form, $\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}=\lvert Q_t\rvert^{2}-\lvert Q_x\rvert^{2}-\lvert Q_y\rvert^{2}-\lvert Q_z\rvert^{2}$, real and indefinite of signature $(2,6)$, with the $\langle\cdot\rangle_{\natural*}$-isotropic cone as its vanishing set.**

**Definition.** The **algebraic norm of the block** is the diagonal of the scalar-part form of the product,

$$
\langle\tilde Q\rangle_{\natural*}=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\langle\tilde Q,\tilde Q\rangle_{\natural*}
=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\lvert Q_\mu\rvert^{2},
$$

equivalently $\langle\tilde Q\rangle_{\natural*}=\langle\tilde Q,\tilde Q\rangle_{\natural*}$ for the form

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}\bigl(\tilde Q_1\star\tilde Q_2\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_{1,\mu}\overline{Q_{2,\mu}},
$$

the general quaternionic sesquilinear form of *The Four Forms and the Four Algebraic Norms*, also
called the **Krein form** of the block. The two arities of the letter are one object: with two arguments the
form, with one argument its diagonal.

**Theorem (the square and the algebraic norm).** For every $\tilde Q$ the square is a real quaternion,
$\mathrm{Sc}(\tilde Q\star\tilde Q)=\langle\tilde Q\rangle_{\natural*}$, and

$$ \boxed{\; \tilde Q\star\tilde Q=\langle\tilde Q\rangle_{\natural*}e_t-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q \;}, $$

with vector part $-2\mathrm{Re}(Q_t\overline{\vec Q})$.

*Proof.* The scalar part is the diagonal of the Krein form as the scalar part of the product of the block
(*The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*); the rest is the diagonal formula
of *The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic Sesqualgebra*.

**Basic properties.** Each is a direct reading of the definition.

- $\langle\tilde Q\rangle_{\natural*}$ is **real**, and **indefinite**: the four entries $1,-1,-1,-1$ on the real and the imaginary
  parts of the four coefficients give the inertia $(2,6)$ on the realification $\mathbb{B}\cong\mathbb{R}^{8}$.
- $\langle\cdot\rangle_{\natural*}$ is **homogeneous of degree two over the reals**, $\langle\lambda\tilde Q\rangle_{\natural*}=\lvert\lambda\rvert^{2}\langle\tilde Q\rangle_{\natural*}$
  for $\lambda\in\mathbb{C}$.
- Its polarisation is the sesquilinear form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$, and
  $\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*}=\overline{\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}}$: the form is Hermitian.
- Its **vanishing set** is the $\langle\cdot,\cdot\rangle_{\natural*}$-isotropic cone, a nonzero cone: $\langle e_t+\vec e_x\rangle_{\natural*}=1-1=0$, so the algebraic norm
  vanishes on nonzero elements.

## The Algebraic Norm Is Not Multiplicative

**Neither the algebraic norm nor the square map is multiplicative: $\langle\tilde Q_1\star\tilde Q_2\rangle_{\natural*}\neq \langle\tilde Q_1\rangle_{\natural*}\langle\tilde Q_2\rangle_{\natural*}$ and $(\tilde Q_1\star\tilde Q_2)\star(\tilde Q_1\star\tilde Q_2)\neq(\tilde Q_1\star\tilde Q_1)\star(\tilde Q_2\star\tilde Q_2)$ in general, the pair $\vec e_z,\vec e_y$ separating both.**

**Theorem (neither the algebraic norm nor the square is multiplicative).** For the block,

$$ \boxed{\; \langle\tilde Q_1\star\tilde Q_2\rangle_{\natural*}\neq \langle\tilde Q_1\rangle_{\natural*}\,\langle\tilde Q_2\rangle_{\natural*}\quad\text{in general} \;}, $$

and the square map is not multiplicative,
$(\tilde Q_1\star\tilde Q_2)\star(\tilde Q_1\star\tilde Q_2)\neq(\tilde Q_1\star\tilde Q_1)\star(\tilde Q_2\star\tilde Q_2)$.

*Proof.* Take $\tilde Q_1=\vec e_z$ and $\tilde Q_2=\vec e_y$. For the algebraic norm,
$\langle \vec e_z\star \vec e_y\rangle_{\natural*}=\langle 0\rangle_{\natural*}=0$ while $\langle \vec e_z\rangle_{\natural*}\langle \vec e_y\rangle_{\natural*}=(-1)(-1)=1$. For the square map,
$(\vec e_z\star \vec e_y)\star(\vec e_z\star \vec e_y)=0\star0=0$ while
$(\vec e_z\star \vec e_z)\star(\vec e_y\star \vec e_y)=(-e_t)\star(-e_t)=e_t$. The values use
$\vec e_z\star \vec e_y=0$ and $\vec e_k\star \vec e_k=-e_t$ of the table.

## Regularity in the Place of Invertibility

**Invertibility is replaced by regularity: the left multiplication $L^{\star}_{\tilde Q}$ is injective exactly when $\tilde Q$ is regular, $Q_t\neq0$ and $C(\tilde Q)\neq0$, and it then has rank eight, six and four on the regular, non-pure zero-divisor and pure zero-divisor classes and rank zero at the origin.**

The absence of a unit does not leave the block without an invertibility notion; it replaces the invertibility
of the element by the injectivity of its multiplication operator.

**Theorem (the element and its operator).** For $\tilde Q\in\mathbb{B}$ the left multiplication
$L^{\star}_{\tilde Q}:\tilde Q_1\mapsto\tilde Q\star\tilde Q_1$ is injective if and only if $\tilde Q$ is
regular, and then it is a conjugate-linear bijection of $\mathbb{B}$; when $\tilde Q$ is a zero divisor the
rank is six in the non-pure family $\{Q_t\neq0,\ C(\tilde Q)=0\}$ and four in the pure family $\{Q_t=0\}$,
and the rank is zero at the origin.

*Proof.* The kernel of $L^{\star}_{\tilde Q}$ is the annihilator
$A_\star(\tilde Q)=\{\tilde Q_1:\tilde Q\star\tilde Q_1=0\}$, of real dimension zero, two and four according to
whether $\tilde Q$ is regular, a non-pure zero divisor or a pure zero divisor
(*Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*), and of dimension eight at the origin; the rank
is eight minus the dimension of the kernel. The origin is neither regular nor a zero divisor, so it is the
one kernel outside the two families, and $L^{\star}_{\tilde Q}$ is conjugate-linear because the second slot
of the block is conjugate-linear.

So the largest class on which the block's multiplication is faithful is the set of the regular elements,
$Q_t\neq0$ and $C(\tilde Q)\neq0$. Every nonzero idempotent of the block is regular
(*Idempotents of the Symmetric Quaternionic Sesqualgebra*), and no nonzero nilpotent is; the regular elements
are the substitute for the invertible ones that the absence of a unit leaves, and they are the elements on
which the operator calculus of *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra* is a
group-like structure without being a group.

## The Absence of a Criterion from the Algebraic Norm

**The algebraic norm does not detect the zero divisors: $\langle\tilde Q\rangle_{\natural*}=0$ does not force $\tilde Q$ to be a zero divisor, and a zero divisor need not have $\langle\tilde Q\rangle_{\natural*}=0$, the witnesses being the regular $e_t+\vec e_x$ with $\langle\cdot\rangle_{\natural*}=0$ and the pure zero divisor $\vec e_x$ with $\langle\cdot\rangle_{\natural*}=-1$.**

**Theorem (the algebraic norm does not detect the zero divisors).** The block has no invertible element, so
no criterion can name one; and the algebraic norm does not decide the zero-divisor class either, the two
implications

$$
\boxed{\;
\langle\tilde Q\rangle_{\natural*}=0\ \Longrightarrow\ \tilde Q\text{ is a zero divisor},
\qquad
\tilde Q\text{ is a zero divisor}\ \Longrightarrow\ \langle\tilde Q\rangle_{\natural*}=0
\;}
$$

both failing.

*Proof.* $\langle e_t+\vec e_x\rangle_{\natural*}=|1|^2-|1|^2=0$ while the central square is $c(e_t+\vec e_x)=1+1=2\neq0$, so $e_t+\vec e_x$ is
regular and the first implication fails. $\langle \vec e_x\rangle_{\natural*}=-1\neq0$ while $\vec e_x$ is a pure zero divisor, since
$\vec e_x\star \vec e_y=0$, so the second fails.

**Remark (what carries the class).** The algebraic norm vanishes on the regular isotropic elements and does
not vanish on the pure zero divisors, so the zero-divisor class is carried by the scalar part $Q_t$ and the
central square $C$, and not by $\langle\cdot\rangle_{\natural*}$. The isotropic elements of $\langle\cdot\rangle_{\natural*}$ are computed in *The Isotropic Structure of
the General Quaternionic Sesqualgebra* and its restriction to the block in *The Krein Form as a Product on
the Symmetric Quaternionic Sesqualgebra*.

## Worked Examples

**A value with no inverse.** $\tilde Q=\vec e_x$: the equation $\vec e_x\star\tilde Q_2=\tilde E$ has no solution with a
unit $\tilde E$, since there is no unit; and $\tilde Q$ is a pure zero divisor, so its left multiplication
has rank four and is not injective.

**A regular element whose left multiplication is a bijection.** $\tilde Q=e_t+\vec e_x$: $Q_t=1$ and
$C=2\neq0$, so it is regular; $L^{\star}_{\tilde Q}$ is a conjugate-linear bijection, though $\tilde Q$ has
no inverse.

**A multiplicativity failure.** $\tilde Q_1=\vec e_z$, $\tilde Q_2=\vec e_y$: the algebraic norm gives
$0\neq1$ and the square map gives $0\neq e_t$.

**The unit candidate.** $\tilde Q=e_t$: $e_t\star(e_t+\vec e_x)=e_t-\vec e_x$, so the element $e_t$ does not fix the
block; it is an idempotent and a root of $+1$ and not a unit.

## Summary

The block has no unit, so no element has an inverse and the group of units is empty; the unit candidate $e_t$
acts by the two conjugations instead, $e_t\star\tilde Q_1=\tilde Q_1^{*}$ and
$\tilde Q_1\star e_t=\tilde Q_1^{\natural}$. It carries one algebraic norm, the diagonal of its scalar-part form,
the symmetric quaternionic sesquilinear algebraic norm

$$
\langle\tilde Q\rangle_{\natural*}=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\lvert Q_\mu\rvert^{2}
=\lvert Q_t\rvert^{2}-\lvert Q_x\rvert^{2}-\lvert Q_y\rvert^{2}-\lvert Q_z\rvert^{2},
$$

real, indefinite of signature $(2,6)$, also called the Krein form, with the $\langle\cdot,\cdot\rangle_{\natural*}$-isotropic cone as its
vanishing set; it is **not multiplicative**, the pair $\vec e_z,\vec e_y$ separating the two sides,
$\langle \vec e_z\star \vec e_y\rangle_{\natural*}=\langle 0\rangle_{\natural*}=0$ against $\langle \vec e_z\rangle_{\natural*}\langle \vec e_y\rangle_{\natural*}=1$, and the square map is not multiplicative either.
Invertibility is replaced by regularity: the left multiplication of $\tilde Q$ is injective exactly when
$\tilde Q$ is regular, $Q_t\neq0$ and $C(\tilde Q)\neq0$, and has rank eight, six and four on the regular
elements, the non-pure zero divisors and the pure zero divisors, and rank zero at the origin. The article
records the **absence of a criterion**: the algebraic norm does not detect the zero divisors, vanishing on
the regular $e_t+\vec e_x$ and not on the pure zero divisor $\vec e_x$; the class is carried by the scalar part and the
central square, not by $\langle\cdot\rangle_{\natural*}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde E\star\tilde Q_1=\tilde Q_1$ (left), $\tilde Q_1\star\tilde E=\tilde Q_1$ (right) | the unit equations; the block has no solution |
| $\tilde Q\star\tilde Q^{-1}=\tilde Q^{-1}\star\tilde Q=\tilde E$ | the inverse equation; empty without a unit |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)=\sum_\mu\varepsilon_\mu Q_{1,\mu}\overline{Q_{2,\mu}}$ | the Krein form, the scalar-part form of the product |
| $\langle\tilde Q\rangle_{\natural*}=\langle\tilde Q,\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ | the algebraic norm of the block, one of the four algebraic norms of the space |
| $\tilde Q\star\tilde Q=\langle\tilde Q\rangle_{\natural*}e_t-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q$ | the square, a real quaternion with scalar part $\langle\tilde Q\rangle_{\natural*}$ |
| $\langle\tilde Q_1\star\tilde Q_2\rangle_{\natural*}\neq \langle\tilde Q_1\rangle_{\natural*}\langle\tilde Q_2\rangle_{\natural*}$ | the failure of multiplicativity |
| $Q_t\neq0,\ C(\tilde Q)\neq0$ | the regular elements, the substitute for the invertible ones |
| $\mathrm{rank}\,L^{\star}_{\tilde Q}\in\{8,6,4,0\}$ | the ranks: regular, non-pure divisor, pure divisor, origin |

## Further Reading

- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the definition of the algebraic norm as the form at the two equal arguments and the four algebraic norms of the space.
- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the general quaternionic sesquilinear form $\langle\cdot,\cdot\rangle_{\natural*}$ and the table of the four forms.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), §*The Unit and the Inverse*, for the definitions relative to a general product and for the unit tables.
- [The Two One-Sided Actions and the Absence of a Unit](the-two-one-sided-actions-and-the-absence-of-a-unit.html), for the two actions of $e_t$ and the proof that no element is a unit.
- [Norm and Invertibility in the Biquaternion Algebra](norm-and-invertibility-in-the-biquaternion-algebra.html), for the algebraic norm $\langle\cdot\rangle$ of the plain product, which is not the form $\langle\cdot,\cdot\rangle_{\natural*}$ of this article.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the criterion of the zero divisors and the regular elements.
- [The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra](the-multiplication-operators-of-the-symmetric-quaternionic-sesqualgebra.html), for the operators whose kernels give the ranks.
- [The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra](the-krein-form-as-a-product-on-the-symmetric-quaternionic-sesqualgebra.html), for the form that is the scalar part of the square.
