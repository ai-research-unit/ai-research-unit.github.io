# __Norm and Invertibility in the General Quaternionic Sesqualgebra__

## Introduction

A **unit** of a product $\star$ is an element $\tilde E$ with $\tilde E\star\tilde Q_1 = \tilde Q_1\star\tilde E = \tilde Q_1$ for every $\tilde Q_1$, an **inverse** of $\tilde Q_1$ is an element $\tilde Q_2$ with $\tilde Q_1\star\tilde Q_2 = \tilde Q_2\star\tilde Q_1 = \tilde E$, and $\tilde Q_1$ is **invertible** when it has an inverse; the definitions are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. This article fixes the product to the **general quaternionic sesquilinear product**

$$
\tilde Q_1 \star \tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2^{*}
$$

of *Introduction to the General Quaternionic Sesqualgebra*, and it answers the two questions of its title.

The answer is a **double absence**, stated as a law, together with the one algebraic norm that the block does carry. The two actions of $e_t$ are the natural conjugation and the star, $\tilde Q\star e_t = \tilde Q^{\natural}$ and $e_t\star\tilde Q = \tilde Q^{*}$, so no element is a two-sided unit and the block has **no unit, no inverse and no invertible element**. The algebraic norm of the block is the diagonal of its scalar-part form,

$$
\langle\tilde Q\rangle_{\natural*}=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\lvert Q_\mu\rvert^{2}=\lvert Q_t\rvert^{2}-\lvert Q_x\rvert^{2}-\lvert Q_y\rvert^{2}-\lvert Q_z\rvert^{2},
$$

the general quaternionic sesquilinear algebraic norm of *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*, real, **indefinite**, of signature $(2,6)$, and **not** multiplicative. The article states the absence of the inverse, defines $\langle\cdot\rangle_{\natural*}$, proves the failure of multiplicativity, and records the **absence of a criterion**: $\langle\cdot\rangle_{\natural*}$ does not decide invertibility, and the block has no invertibility of its own to decide.

**The results.** The general quaternionic sesquilinear product $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2^{*}$ has **no unit, no inverse and no invertible element**: the two actions of $e_t$ are the star and the natural conjugation, so no element is a two-sided unit. It carries one algebraic norm, the general quaternionic sesquilinear algebraic norm $\langle\tilde Q_2\rangle_{\natural*}=\lvert Q_{2t}\rvert^{2}-\lvert Q_{2x}\rvert^{2}-\lvert Q_{2y}\rvert^{2}-\lvert Q_{2z}\rvert^{2}$, real, indefinite of signature $(2,6)$, with the $\langle\cdot\rangle_{\natural*}$-isotropic cone as its vanishing set, and $\langle\cdot\rangle_{\natural*}$ is **not multiplicative**. Because the block has no invertible element, $\langle\cdot\rangle_{\natural*}$ has no invertibility of the block to decide, and it does not decide the invertibility of the plain product either: the plain unit $e_t+\vec e_x$ has $\langle\cdot\rangle_{\natural*}=0$ and the plain zero divisor $\vec e_x+i\vec e_y$ has $\langle\cdot\rangle_{\natural*}=-2$. Each section below states its result first and then proves it.

## The Double Absence

**The product $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2^{*}$ has no left unit, no right unit and no two-sided unit, so no element has an inverse and the set of invertible elements is empty.**

**Proposition (the two one-sided actions of $e_t$).** For every $\tilde Q$,

$$
\boxed{\; e_t\star\tilde Q = \tilde Q^{*} , \qquad \tilde Q\star e_t = \tilde Q^{\natural} \;},
$$

so the left action of $e_t$ is the star and the right action is the natural conjugation.

**Proof.** $e_t\star\tilde Q = e_t^{\natural}\tilde Q^{*} = e_t\tilde Q^{*} = \tilde Q^{*}$, and $\tilde Q\star e_t = \tilde Q^{\natural}e_t^{*} = \tilde Q^{\natural}$.

**Theorem (no unit, no inverse, no invertible element).** The product $\star$ has no left unit, no right unit and no two-sided unit; no element has an inverse; and the set of invertible elements of $\star$ is empty.

**Proof.** A left unit $\tilde E$ would satisfy $\tilde E\star\tilde Q = \tilde Q$ for every $\tilde Q$, and at $\tilde Q = e_t$ this reads $\tilde E\star e_t = e_t$, that is $\tilde E^{\natural} = e_t$ by the proposition, so $\tilde E = e_t$; but $e_t\star\tilde Q = \tilde Q^{*}$ is not $\tilde Q$ for every $\tilde Q$, for instance at $\tilde Q = \vec e_x$, so there is no left unit. The same computation at $\tilde Q = e_t$ for a right unit gives $\tilde E^{*} = e_t$, hence $\tilde E = e_t$, and $e_t$ is not a right unit because $\tilde Q\star e_t = \tilde Q^{\natural}$ is not $\tilde Q$ at $\tilde Q = \vec e_x$. A two-sided unit would be both, so there is none. An inverse requires a unit in its definition, so no inverse exists, and the set of invertible elements is empty. The same statements, with the monoid and the one-sided families, are *The Two One-Sided Actions and the Absence of a Unit*, where the left and the right multiplications of the block are computed as well.

**Corollary (the absence and the element classes).** The concepts of *Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra*, *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra* and the roots of a central value of the block are read **without** a unit: an idempotent is an element equal to its square and not a projection onto the unit, a nilpotent is an element of vanishing square and not a multiple of a unit, and a root of $\lambda$ is an element of square $\lambda e_t$ and not the product of a unit with a root of $\lambda$ in the plain algebra.

**Proof.** Each definition names only the product and $e_t$, and none of them names a unit; the corollary is the reading of *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* with the theorem above.

## The Algebraic Norm of the Block

**The block carries exactly one algebraic norm, the diagonal of its scalar-part form, $\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}=\lvert Q_t\rvert^{2}-\lvert Q_x\rvert^{2}-\lvert Q_y\rvert^{2}-\lvert Q_z\rvert^{2}$, real and indefinite of signature $(2,6)$, with the nonzero $\langle\cdot\rangle_{\natural*}$-isotropic cone as its vanishing set.**

**Definition.** The **algebraic norm of the block** is the diagonal of the scalar-part form of the product,

$$
\langle\tilde Q\rangle_{\natural*}=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\lvert Q_\mu\rvert^{2}=\lvert Q_t\rvert^{2}-\lvert Q_x\rvert^{2}-\lvert Q_y\rvert^{2}-\lvert Q_z\rvert^{2},
$$

equivalently $\langle\tilde Q\rangle_{\natural*}=\langle\tilde Q,\tilde Q\rangle_{\natural*}$ for the form

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}\bigl(\tilde Q_1\star\tilde Q_2\bigr)=\mathrm{Sc}\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}},
$$

the general quaternionic sesquilinear form of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, also called the **Krein form** of the block, whose Gram matrix and restrictions are computed in *The Krein Gram Matrix and the Restrictions of the Form*.

**Basic properties.** Each is a direct reading of the definition.

- $\langle\tilde Q\rangle_{\natural*}$ is **real**, and **indefinite**: the four entries $1,-1,-1,-1$ on the real and the imaginary parts of the four coefficients give the inertia $(2,6)$ on the realification $\mathbb{B}\cong\mathbb{R}^{8}$.
- $\langle\cdot\rangle_{\natural*}$ is **homogeneous of degree two over the reals**, $\langle\lambda\tilde Q\rangle_{\natural*}=\lvert\lambda\rvert^{2}\langle\tilde Q\rangle_{\natural*}$ for $\lambda\in\mathbb{C}$.
- Its polarisation is the sesquilinear form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$, and $\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*}=\overline{\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}}$: the form is Hermitian.
- Its **vanishing set** is the $\langle\cdot,\cdot\rangle_{\natural*}$-isotropic cone, a nonzero cone: $\langle e_t+\vec e_x\rangle_{\natural*}=1-1=0$, so the algebraic norm vanishes on nonzero elements.

## The Algebraic Norm Is Not Multiplicative

**The algebraic norm of the block is not multiplicative, $\langle\tilde Q_1\star\tilde Q_2\rangle_{\natural*}\neq \langle\tilde Q_1\rangle_{\natural*}\langle\tilde Q_2\rangle_{\natural*}$ in general, the pair $\tilde Q_1=\tilde Q_2=e_t+\vec e_x$ separating the two sides.**

**Proposition.** The algebraic norm of the block is **not** multiplicative:

$$
\boxed{\; \langle\tilde Q_1\star\tilde Q_2\rangle_{\natural*}\neq \langle\tilde Q_1\rangle_{\natural*}\,\langle\tilde Q_2\rangle_{\natural*}\quad\text{in general.} \;}
$$

*Proof.* The pair $\tilde Q_1=\tilde Q_2=e_t+\vec e_x$ separates the two sides. Here $\langle\tilde Q_1\rangle_{\natural*}=\langle\tilde Q_2\rangle_{\natural*}=1-1=0$, so $\langle\tilde Q_1\rangle_{\natural*}\langle\tilde Q_2\rangle_{\natural*}=0$, while $\tilde Q_1\star\tilde Q_2=(e_t-\vec e_x)(e_t+\vec e_x)=e_t+\vec e_x-\vec e_x-\vec e_x^{2}=2e_t$ and $\langle 2e_t\rangle_{\natural*}=4$. The two values differ, so no multiplicativity holds.

**Remark (the failure belongs to the block).** The block, whose two slots carry the two conjugations, does not respect its own algebraic norm $\langle\cdot\rangle_{\natural*}$ under its product.

## The Absence of a Criterion from the Algebraic Norm

**The algebraic norm does not decide invertibility: the set of invertible elements of the block is empty, so $\langle\cdot\rangle_{\natural*}$ has nothing to decide for the block, and $\langle\cdot\rangle_{\natural*}=0$ does not force a plain non-unit while $K\neq0$ does not force a plain unit.**

The algebraic norm of a product would decide invertibility if the invertible elements were exactly the elements of non-vanishing algebraic norm. For the block that statement has no content in one direction and fails in the other, and the article records the absence rather than a criterion.

**Theorem (the algebraic norm does not decide invertibility).** The set of invertible elements of the block is empty, so no criterion in terms of $\langle\cdot\rangle_{\natural*}$ can name it; and $\langle\cdot\rangle_{\natural*}$ does not decide the one invertibility that is available, the invertibility of the **plain** product either:

$$
\boxed{\; \langle\tilde Q\rangle_{\natural*}=0\ \not\Longrightarrow\ \tilde Q\text{ not a plain unit},
\qquad
\langle\tilde Q\rangle_{\natural*}\neq0\ \not\Longrightarrow\ \tilde Q\text{ is a plain unit} \;}.
$$

*Proof.* The first clause is the theorem on the double absence: there is no invertible element, so $\langle\cdot\rangle_{\natural*}$ has nothing to decide for the block. For the two implications, the element $\tilde Q=e_t+\vec e_x$ has $\langle\tilde Q\rangle_{\natural*}=1-1=0$ and is a unit of the plain product, $(e_t+\vec e_x)(e_t-\vec e_x)=2e_t$; the element $\tilde Q=\vec e_x+i\vec e_y$ has $\langle\tilde Q\rangle_{\natural*}=-1-1=-2\neq0$ and is a zero divisor of the plain product, $(\vec e_x+i\vec e_y)(\vec e_x-i\vec e_y)=\vec e_x^{2}-(i\vec e_y)^{2}=-e_t+e_t=0$.

**Remark (the two witnesses).** The element $e_t+\vec e_x$ is a plain unit with vanishing algebraic norm, so $\langle\cdot\rangle_{\natural*}$ is not necessary; the element $\vec e_x+i\vec e_y$ is a plain non-unit with non-vanishing algebraic norm, so $\langle\cdot\rangle_{\natural*}$ is not sufficient. The vanishing set of $\langle\cdot\rangle_{\natural*}$ is the $\langle\cdot\rangle_{\natural*}$-isotropic cone and the zero-divisor set is the cone of a different quadratic form; the two cones meet, as at $e_t+\vec e_x$ in the first and at the idempotents in the second, and neither contains the other.

**Remark (what replaces the criterion).** The block is not left without an element theory: the idempotents, the nilpotents and the square roots of the block are computed in their articles, and the plain product has its own invertibility theory. What the article records is that this theory is **not** read from $\langle\cdot\rangle_{\natural*}$, which is the one algebraic norm the block carries.

## Summary

The general quaternionic sesquilinear product $\tilde Q_1\star\tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2^{*}$ has no unit, no inverse and no invertible element: the left action of $e_t$ is the star, $e_t\star\tilde Q_2 = \tilde Q_2^{*}$, and the right action is the natural conjugation, $\tilde Q_2\star e_t = \tilde Q_2^{\natural}$, so no element is a two-sided unit.

It carries one algebraic norm, the diagonal of its scalar-part form, the general quaternionic sesquilinear algebraic norm

$$
\langle\tilde Q\rangle_{\natural*}=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\lvert Q_\mu\rvert^{2}=\lvert Q_t\rvert^{2}-\lvert Q_x\rvert^{2}-\lvert Q_y\rvert^{2}-\lvert Q_z\rvert^{2},
$$

real, indefinite of signature $(2,6)$, with the $\langle\cdot\rangle_{\natural*}$-isotropic cone as its vanishing set, also called the Krein form; it is **not multiplicative**, the pair $\tilde Q_1=\tilde Q_2=e_t+\vec e_x$ separating the two sides, $\langle\tilde Q_1\star\tilde Q_2\rangle_{\natural*}=\langle 2e_t\rangle_{\natural*}=4$ against $\langle\tilde Q_1\rangle_{\natural*}\langle\tilde Q_2\rangle_{\natural*}=0$. The algebraic norm does **not** decide invertibility: the plain unit $e_t+\vec e_x$ has $\langle\cdot\rangle_{\natural*}=0$ and the plain zero divisor $\vec e_x+i\vec e_y$ has $\langle\cdot\rangle_{\natural*}=-2$, so the non-vanishing of the algebraic norm is neither necessary nor sufficient. The article records that absence, and the block has no criterion of its own to state.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q_1\star\tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2^{*}$ | the general quaternionic sesquilinear product |
| unit, inverse, invertible | relative to a product; the block has none |
| $e_t\star\tilde Q = \tilde Q^{*}$, $\tilde Q\star e_t = \tilde Q^{\natural}$ | the two actions of $e_t$, star and natural conjugation |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | the general quaternionic sesquilinear form, the Krein form |
| $\langle\tilde Q\rangle_{\natural*}=\langle\tilde Q,\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ | the algebraic norm of the block, real, indefinite of signature $(2,6)$ |
| $\{\langle\tilde Q\rangle_{\natural*}=0\}$ | the $\langle\cdot\rangle_{\natural*}$-isotropic cone, the vanishing set of the algebraic norm |
| $\langle\tilde Q_1\star\tilde Q_2\rangle_{\natural*}\neq \langle\tilde Q_1\rangle_{\natural*}\langle\tilde Q_2\rangle_{\natural*}$ | the failure of multiplicativity |
| $e_t+\vec e_x$, $\vec e_x+i\vec e_y$ | the witnesses: plain unit with $\langle\cdot\rangle_{\natural*}=0$, and plain zero divisor with $\langle\cdot\rangle_{\natural*}=-2$ |

## Further Reading

- [The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space](the-4-algebraic-norms-over-the-biquaternion-c-space.html), for the definition of the algebraic norm as the form at the two equal arguments and the four algebraic norms of the space.
- [The 4 Forms over the Biquaternion $\mathbb{C}$ Space](the-4-forms-over-the-biquaternion-c-space.html), for the general quaternionic sesquilinear form $\langle\cdot,\cdot\rangle_{\natural*}$ and the table of the four forms.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), for the unit, the inverse and the invertible element relative to a product.
- [The Two One-Sided Actions and the Absence of a Unit](the-two-one-sided-actions-and-the-absence-of-a-unit.html), for the proof of the absence and the two one-sided families of the block.
- [The Krein Gram Matrix and the Restrictions of the Form](the-krein-gram-matrix-and-the-restrictions-of-the-form.html), for $\langle\cdot,\cdot\rangle_{\natural*}$, its Gram matrix and its signatures.

- [Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra](square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-sesqualgebra.html), for the nontrivial idempotents of the block.
- [Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra](square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-sesqualgebra.html) and [Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra](square-roots-of-zero-and-the-nilpotents-of-the-general-quaternionic-sesqualgebra.html), for the roots of the block.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation and the article format.
