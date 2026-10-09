# __Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products on its underlying complex space, and the fourth of them, the **general quaternionic sesquilinear product** $\tilde P^{\natural}\tilde Q^{*}$ of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, is conjugate-linear in its second argument. It therefore carries an exchange that keeps its class, the transposition of the arguments composed with the coefficientwise conjugation, and the exchange cuts the product into a fixed part and a negated part. The fixed part is the multiplication of this article,

$$
\tilde P\star\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural}\bigr)
=\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P},
$$

the **symmetric quaternionic sesquilinear product**, abbreviated $\mathrm{SQS}$. Its scalar part is the Krein form $K$ of the corpus and its vector part is the mixed term alone: the cross product $\mathbf{P}\times\overline{\mathbf{Q}}$ that separates the two orders cancels in the half-sum, so the two parts of the value, scalar and vector, sit side by side in one element and neither annihilates the other. What distinguishes the block is the shape of this value: of the four symmetric parts the quaternionic bilinear one, $\tilde Q^{\natural}\tilde Q=N(\tilde Q)e_0$, and the plain sesquilinear one, whose diagonal is the positive Hermitian form times $e_0$, have central diagonals, while $\mathrm{SPA}$, whose diagonal is the plain square and is $2e_1$ at $e_0+e_1$, and $\mathrm{SQS}$ keep a vector part; the block is the one whose scalar part is the form $K$ and whose vector part is the mixed term alone.

The general construction of the sesqualgebra parts is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the general quaternionic sesquilinear product, its two orders, its one-sided actions and its operators are *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*, *The Two One-Sided Actions and the Absence of a Unit* and *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*; the form $K$ is *The Krein Gram Matrix and the Restrictions of the Form*; and the two halves of the split, with the antisymmetric part $\mathbf{P}\times\overline{\mathbf{Q}}$, are *The 12 Products of the Biquaternion Complex Space*, whose table places the block among the twelve. This article owns the introduction of the block; the diagonal, the halves, the form, the six subspaces, the operators and the two matrix models are the five articles that follow.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity and $e_k^{2}=-e_0$; $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$; $i$ is the central scalar imaginary; $\mathrm{Sc}$ is the scalar part and $\mathbf{Q}=\sum_kQ_ke_k$ the vector part; ${}^{\natural}$ is the natural conjugation, negating $e_1,e_2,e_3$ and fixing the complex coefficients, and ${}^{*}={}^{\natural}\circ\bar{\cdot}$ is the Hermitian conjugation, the bar being the coefficientwise complex conjugation; $(\mathbf{P},\mathbf{Q})=\sum_kP_kQ_k$ is the bilinear dot product and $\times$ the bilinear cross product; $\varepsilon=(1,-1,-1,-1)$ is the sign vector. The product of this article is $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$.

## The Product

**Definition.** The **symmetric quaternionic sesquilinear product** of two biquaternions is

$$
\tilde P\star\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural}\bigr),
$$

the half-sum of the two orders of the general quaternionic sesquilinear product, the second order read with the conjugations in the same slots.

**Theorem (the scalar–vector form).** For all biquaternions,

$$
\tilde P\star\tilde Q=\bigl[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}.
$$

The scalar part is the Krein form $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ and the vector part is the mixed term $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$.

*Proof.* Write the plain product of two quaternions as $XY=[X_0Y_0-(\mathbf{X},\mathbf{Y})]+X_0\mathbf{Y}+Y_0\mathbf{X}+\mathbf{X}\times\mathbf{Y}$. For the first order put $X=\tilde P^{\natural}$, of scalar part $P_0$ and vector part $-\mathbf{P}$, and $Y=\tilde Q^{*}$, of scalar part $\overline{Q_0}$ and vector part $-\overline{\mathbf{Q}}$: the vector part of the product is $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}+\mathbf{P}\times\overline{\mathbf{Q}}$. For the second order the same computation with the factors exchanged gives $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}$, since $\overline{\mathbf{Q}}\times\mathbf{P}=-\mathbf{P}\times\overline{\mathbf{Q}}$. The two vector parts differ by the sign of the cross product, whose half-sum vanishes and whose half-difference is $\mathbf{P}\times\overline{\mathbf{Q}}$, and their scalar parts are equal, since $\mathrm{Sc}(XY)=\mathrm{Sc}(YX)$; the half-sum is the displayed value. $\square$

**Corollary (the two projections of the value).** The scalar part of the value is a complex multiple of $e_0$, and the vector part of the value is a complex vector in $\mathbf{e}=\mathrm{span}_{\mathbb{C}}\{e_1,e_2,e_3\}$; concretely

$$
\mathrm{Sc}(\tilde P\star\tilde Q)=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}}),
\qquad
\mathrm{Vect}(\tilde P\star\tilde Q)=-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}.
$$

*Proof.* The scalar part is the scalar part of the value, the first display; the vector part is read in the second. $\square$

**Proposition (the class).** The product $\star$ is additive in each argument, $\mathbb{C}$-linear in the first and $\bar{\cdot}$-semilinear in the second:

$$
(\lambda\tilde P)\star\tilde Q=\lambda\,(\tilde P\star\tilde Q),
\qquad
\tilde P\star(\lambda\tilde Q)=\bar\lambda\,(\tilde P\star\tilde Q).
$$

*Proof.* Both orders of the general quaternionic sesquilinear product are sesquilinear of the same size in their slots, and $\star$ is their half-sum; the linearity in the first slot is that of $\tilde P^{\natural}\tilde Q^{*}$ and the conjugate-linearity in the second is that of both orders, since ${}^{*}$ is conjugate-linear. The two rules are the two scalar rules of *Sesqualgebras* read on $\star$. $\square$

**Theorem (conjugate-commutativity).** The product is conjugate-commutative:

$$
\tilde P\star\tilde Q=\overline{\tilde Q\star\tilde P}.
$$

*Proof.* The coefficientwise conjugation satisfies $\overline{\tilde P^{\natural}}=\tilde P^{*}$ and $\overline{\tilde Q^{*}}=\tilde Q^{\natural}$, so $\overline{\tilde Q\star\tilde P}=\tfrac12\bigl(\overline{\tilde Q^{\natural}\tilde P^{*}}+\overline{\tilde P^{*}\tilde Q^{\natural}}\bigr)=\tfrac12\bigl(\tilde Q^{*}\tilde P^{\natural}+\tilde P^{\natural}\tilde Q^{*}\bigr)=\tilde P\star\tilde Q$. $\square$

**Remark.** The conjugate-commutativity is the symmetry the block inherits from its construction, and it is *not* commutativity: the product is not commutative, and it is not associative either. The block is the one of the four symmetric parts that is neither central nor commutative, and its diagonal is the subject of *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra*.

**Proposition (the two orders of the plain product).** The two orders whose half-sum is the block are the natural conjugates of the two orders of the plain product of $\overline{\tilde Q}$ and $\tilde P$:

$$
\tilde P^{\natural}\tilde Q^{*}=(\overline{\tilde Q}\tilde P)^{\natural},
\qquad
\tilde Q^{*}\tilde P^{\natural}=(\tilde P\overline{\tilde Q})^{\natural},
\qquad
\tilde P\star\tilde Q=\bigl[\mathrm{SPA}(\overline{\tilde Q},\tilde P)\bigr]^{\natural},
$$

where $\mathrm{SPA}(\tilde X,\tilde Y)=\tfrac12(\tilde X\tilde Y+\tilde Y\tilde X)$ is the symmetric plain product.

*Proof.* The natural conjugation is an anti-automorphism, so $(\overline{\tilde Q}\tilde P)^{\natural}=\tilde P^{\natural}(\overline{\tilde Q})^{\natural}=\tilde P^{\natural}\tilde Q^{*}$, since $(\overline{\tilde Q})^{\natural}=\tilde Q^{*}$; the second identity is the same with the factors exchanged. Averaging gives $\tilde P\star\tilde Q=\bigl[\tfrac12(\overline{\tilde Q}\tilde P+\tilde P\overline{\tilde Q})\bigr]^{\natural}=\bigl[\mathrm{SPA}(\overline{\tilde Q},\tilde P)\bigr]^{\natural}$. $\square$

**Remark (the orders are not conjugate to each other).** The second order $\tilde Q^{*}\tilde P^{\natural}$ is not $\overline{\tilde P^{\natural}\tilde Q^{*}}$; the two differ by the cross product, $(\tilde P^{\natural}\tilde Q^{*})-(\tilde Q^{*}\tilde P^{\natural})=2\,\mathbf{P}\times\overline{\mathbf{Q}}$, so the cross-product cancellation in the half-sum is not a conjugation but a genuine cancellation of two independent orders.

## The Absence of a Unit and the Two One-Sided Actions

**Theorem (the two actions of $e_0$).** For every biquaternion,

$$
e_0\star\tilde Q=\tilde Q^{*},
\qquad
\tilde Q\star e_0=\tilde Q^{\natural}.
$$

*Proof.* $e_0\star\tilde Q=\tfrac12\bigl(e_0^{\natural}\tilde Q^{*}+\tilde Q^{*}e_0^{\natural}\bigr)=\tfrac12(\tilde Q^{*}+\tilde Q^{*})=\tilde Q^{*}$, since $e_0^{\natural}=e_0$ is the unit of the plain product; the second is the conjugate-commutative mirror, or the same computation with the factors exchanged. $\square$

**Corollary (no unit on either side).** There is no element $\tilde E$ with $\tilde E\star\tilde Q=\tilde Q$ for all $\tilde Q$, and none with $\tilde Q\star\tilde E=\tilde Q$ for all $\tilde Q$.

*Proof.* A left unit would satisfy $\tilde E\star e_0=e_0$, that is $\tilde E^{\natural}=e_0$, whence $\tilde E=e_0$; but $e_0\star e_1=e_1^{*}=-e_1\neq e_1$, so $e_0$ is not a left unit. The right case is the mirror, through $\tilde Q\star e_0=\tilde Q^{\natural}$, and $\tilde Q^{\natural}\neq\tilde Q$ for $\tilde Q=e_1$. $\square$

**Remark.** The two actions are the two conjugations of the algebra, so the unit candidate $e_0$ acts as the star conjugation on the left and as the natural conjugation on the right; the same computation shows that no other element can do better, since it must already fail at $e_1$. The one-sided actions are *The Two One-Sided Actions and the Absence of a Unit*, read on the general quaternionic sesquilinear product; here they are the actions of the block, and they agree with the general ones.

## The Sixteen Products of the Basis

**Theorem (the multiplication table).** On the four real quaternion directions the product is the table

| $\star$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $-e_1$ | $-e_2$ | $-e_3$ |
| $e_1$ | $-e_1$ | $-e_0$ | $0$ | $0$ |
| $e_2$ | $-e_2$ | $0$ | $-e_0$ | $0$ |
| $e_3$ | $-e_3$ | $0$ | $0$ | $-e_0$ |

and it is symmetric, the table being symmetric across its diagonal.

*Proof.* The entries are read from the definition. For the first row and column, $e_0\star e_k=e_k^{*}=-e_k$ and $e_k\star e_0=e_k^{\natural}=-e_k$. For the diagonal, $e_k\star e_k=\tfrac12\bigl(e_k^{\natural}e_k^{*}+e_k^{*}e_k^{\natural}\bigr)=\tfrac12\bigl((-e_k)(-e_k)+(-e_k)(-e_k)\bigr)=e_k^{2}=-e_0$. For two distinct vector directions, $e_i\star e_j=\tfrac12\bigl((-e_i)(-e_j)+(-e_j)(-e_i)\bigr)=\tfrac12(e_ie_j+e_je_i)=0$ by the anti-commutation of the quaternion units. The symmetry is the conjugate-commutativity read on real elements. $\square$

**Remark (the table is the real symmetric product of the basis).** The same sixteen entries are the values of the symmetric part of the general quaternionic sesquilinear product on the real basis. The block is not an algebra with a unit, since the first row and column carry the two conjugations rather than the identity, and it is not the quaternion multiplication, since $e_i\star e_j$ vanishes for distinct vector directions instead of giving the third unit.

## The Square and Its Polarisation

**Theorem (the diagonal).** For every biquaternion,

$$
\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)\,e_0-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q},
\qquad
K(\tilde Q,\tilde Q)=\sum_\mu\varepsilon_\mu|Q_\mu|^{2}=|Q_0|^{2}-\sum_{k=1}^{3}|Q_k|^{2}.
$$

The scalar part is real, and the vector part vanishes exactly when the mixed term does.

*Proof.* Put $\tilde P=\tilde Q$ in the scalar–vector form: the scalar part is $K(\tilde Q,\tilde Q)=|Q_0|^{2}-\sum_k|Q_k|^{2}$, a sum of real squares with signs, and the vector part is $-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q}=-2\mathrm{Re}(Q_0\overline{\mathbf{Q}})$, a real vector. $\square$

**Theorem (the polarisation).** For all biquaternions,

$$
\tilde P\star\tilde Q=\tfrac12\bigl((\tilde P+\tilde Q)\star(\tilde P+\tilde Q)-\tilde P\star\tilde P-\tilde Q\star\tilde Q\bigr)+\tfrac12\bigl(\tilde P\star\tilde Q-\tilde Q\star\tilde P\bigr),
$$

so the block is the sum of the polarisation of its square and the half-difference of its two orders, the two parts being the conjugate-even and the conjugate-odd part of the value.

*Proof.* Expand the square by additivity: $(\tilde P+\tilde Q)\star(\tilde P+\tilde Q)=\tilde P\star\tilde P+\tilde P\star\tilde Q+\tilde Q\star\tilde P+\tilde Q\star\tilde Q$. The first summand of the display is therefore $\tfrac12(\tilde P\star\tilde Q+\tilde Q\star\tilde P)$, and adding the half-difference $\tfrac12(\tilde P\star\tilde Q-\tilde Q\star\tilde P)$ recovers $\tilde P\star\tilde Q$. Since $\tilde Q\star\tilde P=\overline{\tilde P\star\tilde Q}$ by conjugate-commutativity, the two parts are $\tfrac12(\tilde P\star\tilde Q+\overline{\tilde P\star\tilde Q})$ and $\tfrac12(\tilde P\star\tilde Q-\overline{\tilde P\star\tilde Q})$, the conjugate-even and conjugate-odd parts. $\square$

**Remark.** The polarisation separates the conjugate-even part of the value, which is the polarisation of the square, from the conjugate-odd half-difference $\tfrac12(\tilde P\star\tilde Q-\tilde Q\star\tilde P)$. The antisymmetric companion of the *general* quaternionic sesquilinear product is a different object: from $\mathrm{GQS}=\mathrm{SQS}+\mathrm{AQS}$ one reads $\tilde P^{\natural}\tilde Q^{*}=\tilde P\star\tilde Q+\mathbf{P}\times\overline{\mathbf{Q}}$, the cross product $\mathbf{P}\times\overline{\mathbf{Q}}$ being the product of Block 8 of the batch, and that reconstruction is the one of *The 12 Products of the Biquaternion Complex Space*.

## The Failure of the Jordan Identity

**Theorem (the Jordan identity fails).** With $x=y=e_1$ the two sides of the Jordan identity $(x^{2}\star x)\star x=x^{2}\star(x\star x)$, where $x^{2}=x\star x$, are

$$
(x^{2}\star x)\star x=-e_0,
\qquad
x^{2}\star(x\star x)=e_0,
$$

and they differ by $-2e_0$. The product satisfies no Jordan identity.

*Proof.* $e_1\star e_1=-e_0$ by the table. Then $x^{2}\star x=(-e_0)\star e_1=-e_0^{\natural}e_1^{*}$ composed as the half-sum: $-e_0^{\natural}=-e_0$ and $e_1^{*}=-e_1$, so $(-e_0)\star e_1=\tfrac12\bigl((-e_0)(-e_1)+(-e_1)(-e_0)\bigr)=e_1$; hence $(x^{2}\star x)\star x=e_1\star e_1=-e_0$. The right side is $x^{2}\star(x\star x)=(-e_0)\star(-e_0)=\tfrac12\bigl((-e_0)^{\natural}(-e_0)^{*}+(-e_0)^{*}(-e_0)^{\natural}\bigr)=\tfrac12(e_0+e_0)=e_0$. $\square$

**Remark (the shape of the failure).** The failure of the block is a **central shift**: the two sides are $-e_0$ and $e_0$, and their difference $-2e_0$ lies in the centre. The sibling $\mathrm{SPS}$ fails on the same witness differently: there one side vanishes and the other is $e_0$, so the failure is an outright vanishing rather than a shift. The two failures are the two ways a symmetric sesquilinear product can miss the Jordan identity, and they are recorded side by side in *The 12 Products of the Biquaternion Complex Space*.

## The Block among the Twelve

**Theorem (the placement).** The twelve operations of the biquaternion complex space are the four general products and their symmetric and antisymmetric parts. The block $\mathrm{SQS}$ is the symmetric part of the general quaternionic sesquilinear product $\mathrm{GQS}$ under the conjugate transpose, and

$$
\mathrm{GQS}=\mathrm{SQS}+\mathrm{AQS},
\qquad
\mathrm{AQS}(\tilde P,\tilde Q)=\mathbf{P}\times\overline{\mathbf{Q}},
$$

the two halves being sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$ and valued, the first in no subspace of the six and the second in the vector subspace.

*Proof.* The split is the conjugate-transpose split of $\tilde P^{\natural}\tilde Q^{*}$: the exchange of the product is $\overline{\tilde Q^{\natural}\tilde P^{*}}=\tilde Q^{*}\tilde P^{\natural}$, and the fixed and negated halves are the two displayed operations. The value of $\mathrm{AQS}$ is the cross product by the vector-part computation of §*The Product*, and its image is the vector subspace by definition. The placement is the row $\mathrm{SQS}$ and the row $\mathrm{AQS}$ of the table of *The 12 Products of the Biquaternion Complex Space*. $\square$

**Remark.** Together with $\mathrm{SPA}$, $\mathrm{SQA}$ and $\mathrm{SPS}$ the block is one of the four symmetric parts of the four general products. The two sesquilinear symmetric parts separate the block from the plain sesquilinear one: $\mathrm{SPS}$ collapses to the centre, with the central diagonal that is the positive Hermitian form times $e_0$, while $\mathrm{SQS}$ images the whole algebra and has a non-central diagonal. Among the two bilinear symmetric parts $\mathrm{SQA}$ collapses to the centre too, while $\mathrm{SPA}$ shares with the block the whole-algebra image and the non-central square, the plain square of $e_0+e_1$ being $2e_1$; the block is singled out by its value, the form $K$ in the scalar part and the mixed term alone in the vector part, the cross product having cancelled. The value of a general pair generates the whole algebra, a fact read in *The Six Subspaces under the Symmetric Quaternionic Sesqualgebra of Biquaternions*; the diagonal and the idempotents are read in *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra*.

## Worked Examples

**An axis square.** $\tilde Q=e_1$: $\tilde Q\star\tilde Q=-e_0$, since $K(e_1,e_1)=-1$ and the vector part $-0\cdot\overline{\mathbf{Q}}-0\cdot\mathbf{Q}$ vanishes; the diagonal is the central element $-e_0$.

**A null square.** $\tilde Q=e_1+ie_2$: $\tilde Q\star\tilde Q=-2e_0$, since $K=-|1|^{2}-|i|^{2}=-2$ and again the vector part vanishes; the diagonal is central even though the element is not in the centre, because its scalar coefficient is zero.

**A non-central diagonal.** $\tilde Q=e_0+e_1$: $K(\tilde Q,\tilde Q)=1-1=0$ and the vector part is $-1\cdot e_1-1\cdot e_1=-2e_1$, so $\tilde Q\star\tilde Q=-2e_1$, an element of the vector subspace: the diagonal is not central.

**An isotropic element for the form.** $\tilde P=e_0+e_1$: $K(\tilde P,\tilde P)=0$, so the scalar part of $\tilde P\star\tilde P$ vanishes while the vector part $-2e_1$ does not; the element is isotropic for $K$ and not a zero divisor.

**A basis product.** $\tilde P=e_2$, $\tilde Q=e_1$: $\tilde P\star\tilde Q=\tfrac12\bigl((-e_2)(-e_1)+(-e_1)(-e_2)\bigr)=\tfrac12(e_2e_1+e_1e_2)=0$, the two orders cancelling; the antisymmetric companion is $\mathbf{P}\times\overline{\mathbf{Q}}=-e_3$.

**The two actions at a vector.** $\tilde Q=e_1$: $e_0\star e_1=e_1^{*}=-e_1$ and $e_1\star e_0=e_1^{\natural}=-e_1$; the two conjugations agree on a real vector and differ on a general element, for instance on $e_1+ie_0$, where $e_0\star\tilde Q=\tilde Q^{*}=-e_1-ie_0$ and $\tilde Q\star e_0=\tilde Q^{\natural}=-e_1+ie_0$.

## Summary

The symmetric quaternionic sesquilinear product is $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})=[P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})]-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$, with scalar part the Krein form $K$ and vector part the mixed term alone; the cross product of the two orders cancels in the half-sum. The product is sesquilinear over $(\mathbb{C},\bar{\cdot}\,)$, conjugate-commutative, and it has no unit on either side; the unit candidate $e_0$ acts as $\tilde Q^{*}$ on the left and as $\tilde Q^{\natural}$ on the right. On the four real basis directions the table is symmetric, with $e_k\star e_k=-e_0$ and $e_i\star e_j=0$ for $i\neq j$ among the vector directions. The square is $K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q}$, and the polarisation separates the conjugate-even part of the value from the conjugate-odd half-difference $\tfrac12(\tilde P\star\tilde Q-\tilde Q\star\tilde P)$, while the antisymmetric companion of the general product is the cross product $\mathbf{P}\times\overline{\mathbf{Q}}$. The Jordan identity fails on the witness $x=y=e_1$, with the two sides $-e_0$ and $e_0$: a central shift, where the sibling $\mathrm{SPS}$ fails by an outright vanishing. The block is one of the twelve operations of *The 12 Products of the Biquaternion Complex Space*, and it is the only one whose value has the Krein form $K$ as its scalar part and the mixed term alone as its vector part, the cross product having cancelled between the two orders.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ | the symmetric quaternionic sesquilinear product, the block $\mathrm{SQS}$ |
| $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the scalar part of the value, the Krein form |
| $-P_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{P}$ | the vector part of the value, the mixed term |
| $\mathbf{P}\times\overline{\mathbf{Q}}$ | the antisymmetric companion $\mathrm{AQS}$, the cross product |
| $\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf{Q}}-\overline{Q_0}\mathbf{Q}$ | the diagonal |
| $e_0\star\tilde Q=\tilde Q^{*}$, $\tilde Q\star e_0=\tilde Q^{\natural}$ | the two one-sided actions of $e_0$; no unit |
| $(x^{2}\star x)\star x$ versus $x^{2}\star(x\star x)$ at $x=e_1$ | the Jordan witness, the two sides $-e_0$ and $e_0$ |

## Further Reading

- *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.md`), for the general construction of the parts of a sesqualgebra product.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the table of the twelve operations and the placement of the block.
- *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the product that is split and its two orders.
- *The Two One-Sided Actions and the Absence of a Unit* (`articles_maths/the-two-one-sided-actions-and-the-absence-of-a-unit.md`), for the one-sided actions of the unit candidate.
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the four general products and the place of the general quaternionic sesquilinear product among them.
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`), for the form $K$.
- *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product* (`articles_maths/the-left-and-right-multiplications-of-the-quaternionic-sesquilinear-product.md`), for the operators of the product that is split.
- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six distinguished real subspaces named in the articles of the block.
