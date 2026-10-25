# __Introduction to the Symmetric Quaternionic Sesqualgebra__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products on its underlying complex space, and the fourth of them, the **general quaternionic sesquilinear product** $\tilde Q_1^{\natural}\tilde Q_2^{*}$ of *The Four General Products and Their Relations over the Biquaternion Algebra*, is conjugate-linear in its second argument. It therefore carries an exchange that keeps its class, the transposition of the arguments composed with the coefficientwise conjugation, and the exchange cuts the product into a fixed part and a negated part. The fixed part is the multiplication of this article,

$$
\tilde Q_1\star\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}+\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr)
=\bigl[Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1,
$$

the **symmetric quaternionic sesquilinear product**, abbreviated $\mathrm{SQS}$. Its scalar part is the Krein form $\langle\cdot,\cdot\rangle_{\natural*}$ of the corpus and its vector part is the mixed term alone: the cross product $\vec Q_1\times\overline{\vec Q_2}$ that separates the two orders cancels in the half-sum, so the two parts of the value, scalar and vector, sit side by side in one element and neither annihilates the other. What distinguishes the block is the shape of this value: of the four symmetric parts the quaternionic bilinear one, $\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t$, and the plain sesquilinear one, whose diagonal is the positive Hermitian form times $e_t$, have central diagonals, while $\mathrm{SPA}$, whose diagonal is the plain square and is $2\vec e_x$ at $e_t+\vec e_x$, and $\mathrm{SQS}$ keep a vector part; the block is the one whose scalar part is the form $\langle\cdot,\cdot\rangle_{\natural*}$ and whose vector part is the mixed term alone.

The general construction of the sesqualgebra parts is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the general quaternionic sesquilinear product, its two orders, its one-sided actions and its operators are *Introduction to the General Quaternionic Sesqualgebra*, *The Two One-Sided Actions and the Absence of a Unit* and *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*; the form $\langle\cdot,\cdot\rangle_{\natural*}$ is *The Krein Norm of the Biquaternion Algebra*; and the two halves of the split, with the antisymmetric part $\vec Q_1\times\overline{\vec Q_2}$, are *Symmetric and Antisymmetric Decomposition of the Four General Products*, whose table places the block among the twelve. This article owns the introduction of the block; the diagonal, the halves, the form, the remarkable subspaces, the operators and the two matrix models are the five articles that follow.

## The Product

**Definition (the class and its two slot involutions).** Let $\star$ be a product on the complex space $\mathbb{B}$ that is $\mathbb{C}$-linear in its first argument and $\bar{\cdot}$-semilinear in its second, so that $(\lambda\tilde Q_1)\star\tilde Q_2=\lambda(\tilde Q_1\star\tilde Q_2)$ and $\tilde Q_1\star(\lambda\tilde Q_2)=\overline{\lambda}(\tilde Q_1\star\tilde Q_2)$; such a product is a **sesquilinear product over $(\mathbb{C},\bar{\cdot}\,)$**, and the definition is stated once and for all in *The Sesquilinear Product*. The four general products of the space are *The Four General Products and Their Relations over the Biquaternion Algebra*, and the product of the fourth general row carries the two slot involutions that the class uses, the natural conjugation ${}^{\natural}$ in the first slot and the Hermitian conjugation ${}^{*}$ in the second; the block is the part of that product that the adapted exchange fixes, and the exchange is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*. The definition below fixes the two slot involutions and the two orders, and the tables that follow are read from it.

**Definition.** The **symmetric quaternionic sesquilinear product** of two biquaternions is

$$
\tilde Q_1\star\tilde Q_2=\tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}+\tilde Q_2^{*}\tilde Q_1^{\natural}\bigr),
$$

the half-sum of the two orders of the general quaternionic sesquilinear product, the second order read with the conjugations in the same slots.

**Theorem (the scalar–vector form).** For all biquaternions,

$$ \boxed{\; \tilde Q_1\star\tilde Q_2=\bigl[Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1 \;}. $$

The scalar part is the Krein form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$ and the vector part is the mixed term $-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1$.

*Proof.* Write the plain product of two quaternions as $\tilde Q_1\tilde Q_2=[Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)]+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2$. For the first order the factors are $\tilde Q_1^{\natural}$, of scalar part $Q_{1t}$ and vector part $-\vec Q_1$, and $\tilde Q_2^{*}$, of scalar part $\overline{Q_{2t}}$ and vector part $-\overline{\vec Q_2}$: the vector part of the product is $-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2}$. For the second order the same computation with the factors exchanged gives $-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$, since $\overline{\vec Q_2}\times\vec Q_1=-\vec Q_1\times\overline{\vec Q_2}$. The two vector parts differ by the sign of the cross product, whose half-sum vanishes and whose half-difference is $\vec Q_1\times\overline{\vec Q_2}$, and their scalar parts are equal, since $\mathrm{Sc}(\tilde Q_1\tilde Q_2)=\mathrm{Sc}(\tilde Q_2\tilde Q_1)$; the half-sum is the displayed value.

**Corollary (the two projections of the value).** The scalar part of the value is a complex multiple of $e_t$, and the vector part of the value is a complex vector in $\mathbf{e}=\mathrm{span}_{\mathbb{C}}\{\vec e_x,\vec e_y,\vec e_z\}$; concretely

$$
\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2}),
\qquad
\mathrm{Vect}(\tilde Q_1\star\tilde Q_2)=-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1.
$$

*Proof.* The scalar part is the scalar part of the value, the first display; the vector part is read in the second.

**Proposition (the class).** The product $\star$ is additive in each argument, $\mathbb{C}$-linear in the first and $\bar{\cdot}$-semilinear in the second:

$$
(\lambda\tilde Q_1)\star\tilde Q_2=\lambda\,(\tilde Q_1\star\tilde Q_2),
\qquad
\tilde Q_1\star(\lambda\tilde Q_2)=\bar\lambda\,(\tilde Q_1\star\tilde Q_2).
$$

*Proof.* Both orders of the general quaternionic sesquilinear product are sesquilinear of the same size in their slots, and $\star$ is their half-sum; the linearity in the first slot is that of $\tilde Q_1^{\natural}\tilde Q_2^{*}$ and the conjugate-linearity in the second is that of both orders, since ${}^{*}$ is conjugate-linear. The two rules are the two scalar rules of *Sesqualgebras* read on $\star$.

**Theorem (conjugate-commutativity).** The product is conjugate-commutative:

$$ \boxed{\; \tilde Q_1\star\tilde Q_2=\overline{\tilde Q_2\star\tilde Q_1} \;}. $$

*Proof.* The coefficientwise conjugation satisfies $\overline{\tilde Q_1^{\natural}}=\tilde Q_1^{*}$ and $\overline{\tilde Q_2^{*}}=\tilde Q_2^{\natural}$, so $\overline{\tilde Q_2\star\tilde Q_1}=\tfrac12\bigl(\overline{\tilde Q_2^{\natural}\tilde Q_1^{*}}+\overline{\tilde Q_1^{*}\tilde Q_2^{\natural}}\bigr)=\tfrac12\bigl(\tilde Q_2^{*}\tilde Q_1^{\natural}+\tilde Q_1^{\natural}\tilde Q_2^{*}\bigr)=\tilde Q_1\star\tilde Q_2$.

**Remark.** The conjugate-commutativity is the symmetry the block inherits from its construction, and it is *not* commutativity: the product is not commutative, and it is not associative either. The block is the one of the four symmetric parts that is neither central nor commutative, and its diagonal is the subject of *The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic Sesqualgebra*.

**Proposition (the two orders of the plain product).** The two orders whose half-sum is the block are the natural conjugates of the two orders of the plain product of $\overline{\tilde Q_2}$ and $\tilde Q_1$:

$$
\tilde Q_1^{\natural}\tilde Q_2^{*}=(\overline{\tilde Q_2}\tilde Q_1)^{\natural},
\qquad
\tilde Q_2^{*}\tilde Q_1^{\natural}=(\tilde Q_1\overline{\tilde Q_2})^{\natural},
\qquad
\tilde Q_1\star\tilde Q_2=\bigl[\mathrm{SPA}(\overline{\tilde Q_2},\tilde Q_1)\bigr]^{\natural},
$$

where $\mathrm{SPA}(\tilde Q_1,\tilde Q_2)=\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ is the symmetric plain product.

*Proof.* The natural conjugation is an anti-automorphism, so $(\overline{\tilde Q_2}\tilde Q_1)^{\natural}=\tilde Q_1^{\natural}(\overline{\tilde Q_2})^{\natural}=\tilde Q_1^{\natural}\tilde Q_2^{*}$, since $(\overline{\tilde Q_2})^{\natural}=\tilde Q_2^{*}$; the second identity is the same with the factors exchanged. Averaging gives $\tilde Q_1\star\tilde Q_2=\bigl[\tfrac12(\overline{\tilde Q_2}\tilde Q_1+\tilde Q_1\overline{\tilde Q_2})\bigr]^{\natural}=\bigl[\mathrm{SPA}(\overline{\tilde Q_2},\tilde Q_1)\bigr]^{\natural}$.

**Remark (the orders are not conjugate to each other).** The second order $\tilde Q_2^{*}\tilde Q_1^{\natural}$ is not $\overline{\tilde Q_1^{\natural}\tilde Q_2^{*}}$; the two differ by the cross product, $(\tilde Q_1^{\natural}\tilde Q_2^{*})-(\tilde Q_2^{*}\tilde Q_1^{\natural})=2\,\vec Q_1\times\overline{\vec Q_2}$, so the cross-product cancellation in the half-sum is not a conjugation but a genuine cancellation of two independent orders.

## The Absence of a Unit and the Two One-Sided Actions

**Theorem (the two actions of $e_t$).** For every biquaternion,

$$
\boxed{\;
e_t\star\tilde Q=\tilde Q^{*},
\qquad
\tilde Q\star e_t=\tilde Q^{\natural}
\;}.
$$

*Proof.* $e_t\star\tilde Q=\tfrac12\bigl(e_t^{\natural}\tilde Q^{*}+\tilde Q^{*}e_t^{\natural}\bigr)=\tfrac12(\tilde Q^{*}+\tilde Q^{*})=\tilde Q^{*}$, since $e_t^{\natural}=e_t$ is the unit of the plain product; the second is the conjugate-commutative mirror, or the same computation with the factors exchanged.

**Corollary (no unit on either side).** There is no element $\tilde E$ with $\tilde E\star\tilde Q=\tilde Q$ for all $\tilde Q$, and none with $\tilde Q\star\tilde E=\tilde Q$ for all $\tilde Q$.

*Proof.* A left unit would satisfy $\tilde E\star e_t=e_t$, that is $\tilde E^{\natural}=e_t$, whence $\tilde E=e_t$; but $e_t\star \vec e_x=\vec e_x^{*}=-\vec e_x\neq \vec e_x$, so $e_t$ is not a left unit. The right case is the mirror, through $\tilde Q\star e_t=\tilde Q^{\natural}$, and $\tilde Q^{\natural}\neq\tilde Q$ for $\tilde Q=\vec e_x$.

**Remark.** The two actions are the two conjugations of the algebra, so the unit candidate $e_t$ acts as the star conjugation on the left and as the natural conjugation on the right; the same computation shows that no other element can do better, since it must already fail at $\vec e_x$. The one-sided actions are *The Two One-Sided Actions and the Absence of a Unit*, read on the general quaternionic sesquilinear product; here they are the actions of the block, and they agree with the general ones.

## The Sixteen Products of the Basis

**Theorem (the multiplication table).** On the four real quaternion directions the product is the table

| $\star$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $-\vec e_x$ | $-\vec e_y$ | $-\vec e_z$ |
| $\vec e_x$ | $-\vec e_x$ | $-e_t$ | $0$ | $0$ |
| $\vec e_y$ | $-\vec e_y$ | $0$ | $-e_t$ | $0$ |
| $\vec e_z$ | $-\vec e_z$ | $0$ | $0$ | $-e_t$ |

and it is symmetric, the table being symmetric across its diagonal.

*Proof.* The entries are read from the definition. For the first row and column, $e_t\star \vec e_\mu=\vec e_\mu^{*}=-\vec e_\mu$ and $\vec e_\mu\star e_t=\vec e_\mu^{\natural}=-\vec e_\mu$. For the diagonal, $\vec e_\mu\star \vec e_\mu=\tfrac12\bigl(\vec e_\mu^{\natural}\vec e_\mu^{*}+\vec e_\mu^{*}\vec e_\mu^{\natural}\bigr)=\tfrac12\bigl((-\vec e_\mu)(-\vec e_\mu)+(-\vec e_\mu)(-\vec e_\mu)\bigr)=\vec e_\mu^{2}=-e_t$. For two distinct vector directions, $\vec e_\nu\star \vec e_\lambda=\tfrac12\bigl((-\vec e_\nu)(-\vec e_\lambda)+(-\vec e_\lambda)(-\vec e_\nu)\bigr)=\tfrac12(\vec e_\nu \vec e_\lambda+\vec e_\lambda \vec e_\nu)=0$ by the anti-commutation of the quaternion units. The symmetry is the conjugate-commutativity read on real elements.

**Remark (the table is the real symmetric product of the basis).** The same sixteen entries are the values of the symmetric part of the general quaternionic sesquilinear product on the real basis. The block is not an algebra with a unit, since the first row and column carry the two conjugations rather than the identity, and it is not the quaternion multiplication, since $\vec e_\nu\star \vec e_\lambda$ vanishes for distinct vector directions instead of giving the third unit.

## The Square and Its Polarisation

**Theorem (the diagonal).** For every biquaternion,

$$
\tilde Q\star\tilde Q=\langle\tilde Q,\tilde Q\rangle_{\natural*}\,e_t-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q,
\qquad
\langle\tilde Q,\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu|Q_\mu|^{2}=|Q_t|^{2}-\sum_{k\in\{x,y,z\}}|Q_k|^{2}.
$$

The scalar part is real, and the vector part vanishes exactly when the mixed term does.

*Proof.* Put $\tilde Q_1=\tilde Q_2=\tilde Q$ in the scalar–vector form: the scalar part is $\langle\tilde Q,\tilde Q\rangle_{\natural*}=|Q_t|^{2}-\sum_\mu|Q_\mu|^{2}$, a sum of real squares with signs, and the vector part is $-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q=-2\mathrm{Re}(Q_t\overline{\vec Q})$, a real vector.

**Theorem (the polarisation).** For all biquaternions,

$$
\tilde Q_1\star\tilde Q_2=\tfrac12\bigl((\tilde Q_1+\tilde Q_2)\star(\tilde Q_1+\tilde Q_2)-\tilde Q_1\star\tilde Q_1-\tilde Q_2\star\tilde Q_2\bigr)+\tfrac12\bigl(\tilde Q_1\star\tilde Q_2-\tilde Q_2\star\tilde Q_1\bigr),
$$

so the block is the sum of the polarisation of its square and the half-difference of its two orders, the two parts being the conjugate-even and the conjugate-odd part of the value.

*Proof.* Expand the square by additivity: $(\tilde Q_1+\tilde Q_2)\star(\tilde Q_1+\tilde Q_2)=\tilde Q_1\star\tilde Q_1+\tilde Q_1\star\tilde Q_2+\tilde Q_2\star\tilde Q_1+\tilde Q_2\star\tilde Q_2$. The first summand of the display is therefore $\tfrac12(\tilde Q_1\star\tilde Q_2+\tilde Q_2\star\tilde Q_1)$, and adding the half-difference $\tfrac12(\tilde Q_1\star\tilde Q_2-\tilde Q_2\star\tilde Q_1)$ recovers $\tilde Q_1\star\tilde Q_2$. Since $\tilde Q_2\star\tilde Q_1=\overline{\tilde Q_1\star\tilde Q_2}$ by conjugate-commutativity, the two parts are $\tfrac12(\tilde Q_1\star\tilde Q_2+\overline{\tilde Q_1\star\tilde Q_2})$ and $\tfrac12(\tilde Q_1\star\tilde Q_2-\overline{\tilde Q_1\star\tilde Q_2})$, the conjugate-even and conjugate-odd parts.

**Remark.** The polarisation separates the conjugate-even part of the value, which is the polarisation of the square, from the conjugate-odd half-difference $\tfrac12(\tilde Q_1\star\tilde Q_2-\tilde Q_2\star\tilde Q_1)$. The antisymmetric companion of the *general* quaternionic sesquilinear product is a different object: from $\mathrm{GQS}=\mathrm{SQS}+\mathrm{AQS}$ one reads $\tilde Q_1^{\natural}\tilde Q_2^{*}=\tilde Q_1\star\tilde Q_2+\vec Q_1\times\overline{\vec Q_2}$, the cross product $\vec Q_1\times\overline{\vec Q_2}$ being the product of Block 8 of the batch, and that reconstruction is the one of *Symmetric and Antisymmetric Decomposition of the Four General Products*.

## The Form and the Product

The scalar part of the block is the Krein form, and this section reads the two relations between the product and the form: the form is not invariant under the product, and what holds in place of invariance is an adjoint relation.

**Theorem (the scalar part).** For all biquaternions,
$$
\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2}).
$$
In the coefficient basis the Gram matrix of the form is $E=\mathrm{diag}(1,-1,-1,-1)$, of determinant $-1$; in the real basis the realified form is $\mathrm{diag}(1,-1,-1,-1,1,-1,-1,-1)$, of signature $(2,6)$. The null set, the isotropic structure and the cone are *The Krein Norm of the Biquaternion Algebra*.

*Proof.* The scalar part of the value is the first term of the scalar–vector form, and the Gram matrix is computed from $\langle e_\mu,e_\nu\rangle_{\natural*}=\varepsilon_\mu\delta_{\mu\nu}$.

**Theorem (the invariance fails).** The form is not invariant under the block: there are biquaternions with
$$
\langle\tilde Q_3\star\tilde Q_1,\tilde Q_3\star\tilde Q_2\rangle_{\natural*}\neq\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}.
$$
Explicitly,
$$
\langle\tilde Q_3\star\tilde Q_1,\tilde Q_3\star\tilde Q_2\rangle_{\natural*}
=\mathrm{Sc}\bigl(\mathrm{SPA}(\overline{\tilde Q_1},\tilde Q_3)\,\mathrm{SPA}(\tilde Q_2,\overline{\tilde Q_3})\bigr),
$$
and the defect is this value minus $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$.

*Proof.* The two identities
$$
(\tilde Q_3\star\tilde Q_1)^{\natural}=\mathrm{SPA}(\overline{\tilde Q_1},\tilde Q_3),
\qquad
(\tilde Q_3\star\tilde Q_1)^{*}=\mathrm{SPA}(\tilde Q_1,\overline{\tilde Q_3})
$$
follow from the definition of the block and the anti-automorphism properties of ${}^{\natural}$ and ${}^{*}$. Then $\langle\tilde Q_3\star\tilde Q_1,\tilde Q_3\star\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}\bigl((\tilde Q_3\star\tilde Q_1)^{\natural}(\tilde Q_3\star\tilde Q_2)^{*}\bigr)$, which is the displayed value. On $\tilde Q_3=\tilde Q_1=e_t+\vec e_x$ and $\tilde Q_2=\vec e_x$ one has $\tilde Q_3\star\tilde Q_1=-2\vec e_x$ and $\tilde Q_3\star\tilde Q_2=-e_t-\vec e_x$, so the value is $-2$ against $\langle e_t+\vec e_x,\vec e_x\rangle_{\natural*}=-1$: the defect is $-1$ and the invariance fails.

**Theorem (the adjoint relation).** The block and the form are tied by
$$
\boxed{\;\langle\tilde Q_3\star\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\overline{\langle\tilde Q_1,\tilde Q_3^{\natural}\star\tilde Q_2\rangle_{\natural*}}\; }.
$$

*Proof.* Use the two identities of the preceding theorem and $\mathrm{Sc}(U)=\mathrm{Sc}(U^{\natural})$. On the one hand
$$
\langle\tilde Q_3\star\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}\bigl((\tilde Q_3\star\tilde Q_1)^{\natural}\tilde Q_2^{*}\bigr)=\tfrac12\,\mathrm{Sc}\bigl((\overline{\tilde Q_1}\tilde Q_3+\tilde Q_3\overline{\tilde Q_1})\tilde Q_2^{*}\bigr),
$$
and on the other, at the element $\tilde Q_3^{\natural}$,
$$
\langle\tilde Q_3^{\natural}\star\tilde Q_2,\tilde Q_1\rangle_{\natural*}=\mathrm{Sc}\bigl((\tilde Q_3^{\natural}\star\tilde Q_2)^{\natural}\tilde Q_1^{*}\bigr)=\tfrac12\,\mathrm{Sc}\bigl((\overline{\tilde Q_2}\tilde Q_3^{\natural}+\tilde Q_3^{\natural}\overline{\tilde Q_2})\tilde Q_1^{*}\bigr).
$$
The natural conjugation carries the two summands of the first display onto the two of the second, since $(\overline{\tilde Q_1})^{\natural}=\tilde Q_1^{*}$ and $(\tilde Q_2^{*})^{\natural}=\overline{\tilde Q_2}$, and the scalar part is invariant under it; the cyclic invariance $\mathrm{Sc}(UV)=\mathrm{Sc}(VU)$ then matches the terms. Hermitian symmetry of the form gives the conjugate on the right.

**Remark (adjointness, not multiplicativity).** The product is conjugate-linear in one slot, so its left multiplications do not preserve the form the way a group of linear maps does. The defect measures the failure, and the adjoint relation is the compatibility that survives; in operator form it is the $K$-adjointness of *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*.

**Remark (the four scalar parts).** The scalar parts of the four symmetric parts are
$$
\mathrm{Sc}(\mathrm{SPA})=Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2),
\qquad
\mathrm{Sc}(\mathrm{SQA})=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2),
$$
$$
\mathrm{Sc}(\mathrm{SPS})=Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})=\langle\tilde Q_1,\tilde Q_2\rangle_{*},
\qquad
\mathrm{Sc}(\mathrm{SQS})=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}.
$$
The first two are bilinear and the last two Hermitian, with opposite signs in the vector term; on a real element the Krein form coincides with the first bilinear form, $\mathrm{SPA}$.


## The Failure of the Jordan Identity

**Theorem (the Jordan identity fails).** With $x=y=\vec e_x$ the two sides of the Jordan identity $(x^{2}\star x)\star x=x^{2}\star(x\star x)$, where $x^{2}=x\star x$, are

$$
(x^{2}\star x)\star x=-e_t,
\qquad
x^{2}\star(x\star x)=e_t,
$$

and they differ by $-2e_t$. The product satisfies no Jordan identity.

*Proof.* $\vec e_x\star \vec e_x=-e_t$ by the table. Then $x^{2}\star x=(-e_t)\star \vec e_x=-e_t^{\natural}\vec e_x^{*}$ composed as the half-sum: $-e_t^{\natural}=-e_t$ and $\vec e_x^{*}=-\vec e_x$, so $(-e_t)\star \vec e_x=\tfrac12\bigl((-e_t)(-\vec e_x)+(-\vec e_x)(-e_t)\bigr)=\vec e_x$; hence $(x^{2}\star x)\star x=\vec e_x\star \vec e_x=-e_t$. The right side is $x^{2}\star(x\star x)=(-e_t)\star(-e_t)=\tfrac12\bigl((-e_t)^{\natural}(-e_t)^{*}+(-e_t)^{*}(-e_t)^{\natural}\bigr)=\tfrac12(e_t+e_t)=e_t$.

**Remark (the shape of the failure).** The failure of the block is a **central shift**: the two sides are $-e_t$ and $e_t$, and their difference $-2e_t$ lies in the centre. The sibling $\mathrm{SPS}$ fails on the same witness differently: there one side vanishes and the other is $e_t$, so the failure is an outright vanishing rather than a shift. The two failures are the two ways a symmetric sesquilinear product can miss the Jordan identity, and they are recorded side by side in *Symmetric and Antisymmetric Decomposition of the Four General Products*.

## The Block among the Twelve

**Theorem (the placement).** The twelve operations of the biquaternion complex space are the four general products and their symmetric and antisymmetric parts. The block $\mathrm{SQS}$ is the symmetric part of the general quaternionic sesquilinear product $\mathrm{GQS}$ under the conjugate transpose, and

$$
\mathrm{GQS}=\mathrm{SQS}+\mathrm{AQS},
\qquad
\mathrm{AQS}(\tilde Q_1,\tilde Q_2)=\vec Q_1\times\overline{\vec Q_2},
$$

the two halves being sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$ and valued, the first in no subspace of the remarkable subspaces and the second in the vector subspace.

*Proof.* The split is the conjugate-transpose split of $\tilde Q_1^{\natural}\tilde Q_2^{*}$: the exchange of the product is $\overline{\tilde Q_2^{\natural}\tilde Q_1^{*}}=\tilde Q_2^{*}\tilde Q_1^{\natural}$, and the fixed and negated halves are the two displayed operations. The value of $\mathrm{AQS}$ is the cross product by the vector-part computation of §*The Product*, and its image is the vector subspace by definition. The placement is the row $\mathrm{SQS}$ and the row $\mathrm{AQS}$ of the table of *Symmetric and Antisymmetric Decomposition of the Four General Products*.

**Remark.** Together with $\mathrm{SPA}$, $\mathrm{SQA}$ and $\mathrm{SPS}$ the block is one of the four symmetric parts of the four general products. The two sesquilinear symmetric parts separate the block from the plain sesquilinear one: $\mathrm{SPS}$ collapses to the centre, with the central diagonal that is the positive Hermitian form times $e_t$, while $\mathrm{SQS}$ images the whole algebra and has a non-central diagonal. Among the two bilinear symmetric parts $\mathrm{SQA}$ collapses to the centre too, while $\mathrm{SPA}$ shares with the block the whole-algebra image and the non-central square, the plain square of $e_t+\vec e_x$ being $2\vec e_x$; the block is singled out by its value, the form $\langle\cdot,\cdot\rangle_{\natural*}$ in the scalar part and the mixed term alone in the vector part, the cross product having cancelled. The value of a general pair generates the whole algebra, a fact read in *Remarkable Subspaces under the Symmetric Quaternionic Sesqualgebra*; the diagonal and the idempotents are read in *The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic Sesqualgebra*.

## Worked Examples

**An axis square.** $\tilde Q=\vec e_x$: $\tilde Q\star\tilde Q=-e_t$, since $\langle \vec e_x,\vec e_x\rangle_{\natural*}=-1$ and the vector part $-0\cdot\overline{\vec Q}-0\cdot\vec Q$ vanishes; the diagonal is the central element $-e_t$.

**A null square.** $\tilde Q=\vec e_x+i\vec e_y$: $\tilde Q\star\tilde Q=-2e_t$, since $\langle\cdot,\cdot\rangle_{\natural*}=-|1|^{2}-|i|^{2}=-2$ and again the vector part vanishes; the diagonal is central even though the element is not in the centre, because its scalar coefficient is zero.

**A non-central diagonal.** $\tilde Q=e_t+\vec e_x$: $\langle\tilde Q,\tilde Q\rangle_{\natural*}=1-1=0$ and the vector part is $-1\cdot \vec e_x-1\cdot \vec e_x=-2\vec e_x$, so $\tilde Q\star\tilde Q=-2\vec e_x$, an element of the vector subspace: the diagonal is not central.

**An isotropic element for the form.** $\tilde Q=e_t+\vec e_x$: $\langle\tilde Q,\tilde Q\rangle_{\natural*}=0$, so the scalar part of $\tilde Q\star\tilde Q$ vanishes while the vector part $-2\vec e_x$ does not; the element is isotropic for $\langle\cdot,\cdot\rangle_{\natural*}$ and not a zero divisor.

**A basis product.** $\tilde Q_1=\vec e_y$, $\tilde Q_2=\vec e_x$: $\tilde Q_1\star\tilde Q_2=\tfrac12\bigl((-\vec e_y)(-\vec e_x)+(-\vec e_x)(-\vec e_y)\bigr)=\tfrac12(\vec e_y\vec e_x+\vec e_x\vec e_y)=0$, the two orders cancelling; the antisymmetric companion is $\vec Q_1\times\overline{\vec Q_2}=-\vec e_z$.

**The two actions at a vector.** $\tilde Q=\vec e_x$: $e_t\star \vec e_x=\vec e_x^{*}=-\vec e_x$ and $\vec e_x\star e_t=\vec e_x^{\natural}=-\vec e_x$; the two conjugations agree on a real vector and differ on a general element, for instance on $\vec e_x+ie_t$, where $e_t\star\tilde Q=\tilde Q^{*}=-\vec e_x-ie_t$ and $\tilde Q\star e_t=\tilde Q^{\natural}=-\vec e_x+ie_t$.

## Summary

The symmetric quaternionic sesquilinear product is $\tilde Q_1\star\tilde Q_2=\tfrac12(\tilde Q_1^{\natural}\tilde Q_2^{*}+\tilde Q_2^{*}\tilde Q_1^{\natural})=[Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})]-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1$, with scalar part the Krein form $\langle\cdot,\cdot\rangle_{\natural*}$ and vector part the mixed term alone; the cross product of the two orders cancels in the half-sum. The product is sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$, conjugate-commutative, and it has no unit on either side; the unit candidate $e_t$ acts as $\tilde Q^{*}$ on the left and as $\tilde Q^{\natural}$ on the right. On the four real basis directions the table is symmetric, with $\vec e_\mu\star \vec e_\mu=-e_t$ and $\vec e_\nu\star \vec e_\lambda=0$ for $\nu \neq \lambda$ among the vector directions. The square is $\langle\tilde Q,\tilde Q\rangle_{\natural*}e_t-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q$, and the polarisation separates the conjugate-even part of the value from the conjugate-odd half-difference $\tfrac12(\tilde Q_1\star\tilde Q_2-\tilde Q_2\star\tilde Q_1)$, while the antisymmetric companion of the general product is the cross product $\vec Q_1\times\overline{\vec Q_2}$. The Jordan identity fails on the witness $x=y=\vec e_x$, with the two sides $-e_t$ and $e_t$: a central shift, where the sibling $\mathrm{SPS}$ fails by an outright vanishing. The block is one of the twelve operations of *Symmetric and Antisymmetric Decomposition of the Four General Products*, and it is the only one whose value has the Krein form $\langle\cdot,\cdot\rangle_{\natural*}$ as its scalar part and the mixed term alone as its vector part, the cross product having cancelled between the two orders. The form is read as a product: its Gram matrix in the coefficient basis is $E=\mathrm{diag}(1,-1,-1,-1)$, its realification has signature $(2,6)$, and the product is not invariant under the block; the norm defect is the value of the form on the two products minus the value on the two factors. The adjoint relation $\langle\tilde Q_3\star\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\overline{\langle\tilde Q_1,\tilde Q_3^{\natural}\star\tilde Q_2\rangle_{\natural*}}$ is the compatibility that survives.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\star\tilde Q_2=\tfrac12(\tilde Q_1^{\natural}\tilde Q_2^{*}+\tilde Q_2^{*}\tilde Q_1^{\natural})$ | the symmetric quaternionic sesquilinear product, the block $\mathrm{SQS}$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | the scalar part of the value, the Krein form |
| $-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1$ | the vector part of the value, the mixed term |
| $\vec Q_1\times\overline{\vec Q_2}$ | the antisymmetric companion $\mathrm{AQS}$, the cross product |
| $\tilde Q\star\tilde Q=\langle\tilde Q,\tilde Q\rangle_{\natural*}e_t-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q$ | the diagonal |
| $e_t\star\tilde Q=\tilde Q^{*}$, $\tilde Q\star e_t=\tilde Q^{\natural}$ | the two one-sided actions of $e_t$; no unit |
| $E=\mathrm{diag}(1,-1,-1,-1)$ | the Gram matrix of the form in the coefficient basis |
| $\langle\tilde Q_3\star\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\overline{\langle\tilde Q_1,\tilde Q_3^{\natural}\star\tilde Q_2\rangle_{\natural*}}$ | the adjoint relation tying the block to the form |
| $(x^{2}\star x)\star x$ versus $x^{2}\star(x\star x)$ at $x=\vec e_x$ | the Jordan witness, the two sides $-e_t$ and $e_t$ |

## Further Reading

- [The Symmetric and Antisymmetric Parts of a Sesqualgebra Product](the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.html), for the general construction of the parts of a sesqualgebra product.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the table of the twelve operations and the placement of the block.
- [Introduction to the General Quaternionic Sesqualgebra](introduction-to-the-general-quaternionic-sesqualgebra.html), for the product that is split and its two orders.
- [The Two One-Sided Actions and the Absence of a Unit](the-two-one-sided-actions-and-the-absence-of-a-unit.html), for the one-sided actions of the unit candidate.
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the four general products and the place of the general quaternionic sesquilinear product among them.
- [The Krein Norm of the Biquaternion Algebra](the-krein-norm-of-the-biquaternion-algebra.html), for the form, its null set, its isotropic structure and its cone.
- [The Left and Right Multiplications of the General Quaternionic Sesquilinear Product](the-left-and-right-multiplications-of-the-quaternionic-sesquilinear-product.html), for the operators of the product that is split.
- [Introduction to the Remarkable Subspaces](introduction-to-the-remarkable-subspaces.html), for the remarkable real subspaces named in the articles of the block.
