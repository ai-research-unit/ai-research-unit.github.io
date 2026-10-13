# __Zero Divisors of the Symmetric Quaternionic Sesqualgebra__

## Introduction

This article characterizes the zero divisors of the block, the symmetric quaternionic sesquilinear
product
$\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$
of *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*. It follows *Norm and
Invertibility in the Symmetric Quaternionic Sesqualgebra*, which recorded that the block has no
unit and no inverse, and it opens the element theory of the block: the two families it separates
are read in full in *Idempotents of the Symmetric Quaternionic Sesqualgebra* and *Nilpotents of the
Symmetric Quaternionic Sesqualgebra*.

A divisor is relative to a product. The definition is stated once for a general product in
*Definitions for the Study of the 12 Algebraic Structures*, §*The Zero Divisor and the
Annihilator*, and read on the products of the space; the unqualified word means the zero divisor of
the block, and every other product is named. The four general products of the space share one
zero-divisor set, $\{\tilde Q\neq0: C(\tilde Q)=0\}$ with $C(\tilde Q)=\sum_\mu Q_\mu^2$, a
coincidence of the algebra proved in *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; the block is a symmetric
part of one of them and its set is **larger**, and the enlargement is the point of §*Comparison
with the Four General Products*.

The product itself, its two slot involutions and its two one-sided actions are *Introduction to the
Symmetric Quaternionic Sesqualgebra of Biquaternions*; the general construction of the sesqualgebra
parts is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the form $K$ is *The
Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*; the diagonal and the two
halves are *The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic
Sesqualgebra*; the operators are *The Multiplication Operators of the Symmetric Quaternionic
Sesqualgebra*; and the zero divisors of the plain product, whose criterion is the same central
square, are *Zero Divisors of the General Plain Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis
$e_0,e_1,e_2,e_3$, $e_1^2=e_2^2=e_3^2=-e_0$ and $e_1e_2=e_3$; $\tilde Q=\sum_\mu Q_\mu e_\mu$ with
$Q_\mu\in\mathbb{C}$ and central scalar imaginary $i$; $\mathbf{Q}=\sum_kQ_ke_k$;
$(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$ is the complex bilinear dot product; ${}^{\natural}$ fixes
$e_0$ and negates $e_1,e_2,e_3$ with the coefficients fixed, $\bar{\cdot}$ conjugates the
coefficients, and ${}^{*}={}^{\natural}\circ\bar{\cdot}$; and $\varepsilon=(1,-1,-1,-1)$. The
**central square** of an element is
$C(\tilde Q)=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^2=Q_0^2+(\mathbf Q,\mathbf Q)$, the product
of the plain bilinear product with the natural conjugation, as in *Zero Divisors of the General
Plain Algebra*. Throughout this article the product is the block, written $\star$.

## Definition

The word names a product, so the definition is stated for a general product and then read on the
block; it is stated once and for all in *Definitions for the Study of the 12 Algebraic Structures*,
§*The Zero Divisor and the Annihilator*.

**Definition (zero divisor of a product).** Let $\star$ be a product on $\mathbb{B}$ and let
$\tilde Q\in\mathbb{B}$. The element $\tilde Q$ is a **left zero divisor of $\star$** when
$\tilde Q\neq0$ and there is a nonzero $\tilde R$ with $\tilde Q\star\tilde R=0$; a **right zero
divisor of $\star$** when $\tilde Q\neq0$ and there is a nonzero $\tilde R$ with
$\tilde R\star\tilde Q=0$; and a **zero divisor of $\star$** when it is one or the other. An
element that is both is a **two-sided zero divisor of $\star$**.

Both elements are required to be nonzero, so the origin is not a zero divisor of any product. The
**annihilators** of $\tilde Q$ in $\star$ are
$A_\star(\tilde Q)=\{\tilde X:\tilde Q\star\tilde X=0\}$ and
$B_\star(\tilde Q)=\{\tilde X:\tilde X\star\tilde Q=0\}$.

**On the block.** Substituting $\star$ for the block, the two defining equations are
$\tilde Q\star\tilde R=0$ and $\tilde R\star\tilde Q=0$. On a general pair the scalar–vector form
of *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* reads

$$
\tilde Q\star\tilde R=\bigl[Q_0\overline{R_0}-(\mathbf Q,\overline{\mathbf R})\bigr]
-Q_0\overline{\mathbf R}-\overline{R_0}\,\mathbf Q ,
$$

so the equation $\tilde Q\star\tilde R=0$ is the pair

$$
Q_0\overline{R_0}=(\mathbf Q,\overline{\mathbf R}),
\qquad
Q_0\overline{\mathbf R}+\overline{R_0}\,\mathbf Q=\mathbf 0 .
$$

Unqualified, the product is the block for the rest of the article.

## The Criterion

**Theorem (the criterion of the block).** A nonzero biquaternion $\tilde Q$ is a zero divisor of
the block if and only if

$$
Q_0=0
\qquad\text{or}\qquad
C(\tilde Q)=Q_0^2+(\mathbf Q,\mathbf Q)=0 .
$$

*Proof.* Write the two defining equations for the unknown $\tilde R$.

**The case $Q_0=0$.** The vector equation
$Q_0\overline{\mathbf R}+\overline{R_0}\mathbf Q=\mathbf 0$ becomes
$\overline{R_0}\mathbf Q=\mathbf 0$, and since $\tilde Q\neq0$ has $\mathbf Q\neq0$, this forces
$R_0=0$. The scalar equation becomes $0=(\mathbf Q,\overline{\mathbf R})$, that is
$\sum_{k=1}^{3}Q_k\overline{R_k}=0$, a single complex equation in the three complex unknowns
$R_1,R_2,R_3$; it has a nonzero solution, and with $R_0=0$ that solution gives a nonzero $\tilde R$
with $\tilde Q\star\tilde R=0$. Hence every element of vanishing scalar part is a left zero
divisor.

**The case $Q_0\neq0$.** The vector equation gives $\overline{R_k}=-(\overline{R_0}/Q_0)Q_k$ for
each $k$. Substituting into the scalar equation,

$$
Q_0\overline{R_0}=\sum_kQ_k\overline{R_k}=-\frac{\overline{R_0}}{Q_0}\sum_kQ_k^2=-\frac{\overline{R_0}}{Q_0}\bigl(C(\tilde Q)-Q_0^2\bigr),
$$

which after multiplication by $Q_0$ reads $\overline{R_0}\,C(\tilde Q)=0$. If $C(\tilde Q)\neq0$
then $\overline{R_0}=0$, and the vector equation forces $\overline{\mathbf R}=\mathbf 0$, hence
$\tilde R=0$: there is no zero divisor. If $C(\tilde Q)=0$ then the scalar equation holds for every
$R_0$, the vector equation determines $\mathbf R$ from $R_0$, and any $R_0\neq0$ gives a nonzero
$\tilde R$ with $\tilde Q\star\tilde R=0$. Hence a non-pure element is a left zero divisor exactly
when $C(\tilde Q)=0$.

**The converse.** The two cases above cover every $\tilde Q\neq0$, and in each the existence of the
nonzero $\tilde R$ is exactly the displayed condition. So the left zero divisors are the set
stated.

**Corollary (the two families).** The zero-divisor set of the block is the disjoint union of the
**pure family** $\{Q_0=0,\ \tilde Q\neq0\}$, the nonzero elements of the vector subspace, and the
**non-pure family** $\{Q_0\neq0,\ C(\tilde Q)=0\}$, whose members have the same central square as
the non-pure zero divisors of the plain product.

*Proof.* The two conditions $Q_0=0$ and $Q_0\neq0$ are exclusive; on the first the criterion is
$Q_0=0$ alone, on the second it is $C(\tilde Q)=0$ alone. In the second family $\mathbf Q\neq0$,
since $C(\tilde Q)=Q_0^2+(\mathbf Q,\mathbf Q)=0$ would force $(\mathbf Q,\mathbf Q)=-Q_0^2\neq0$.

## The Two Sides and the Annihilators

The annihilator of an element is the kernel of the left or the right multiplication, the two
coinciding because the block is conjugate-commutative; it is a complex plane in the pure case and a
complex line in the non-pure case, so it separates the two families the criterion joins. The
annihilators, the rank table and the reading on the remarkable subspaces are the companion article
*Annihilators of the Symmetric Quaternionic Sesqualgebra*, below this article in this category.

## Comparison with the Four General Products

The four general products of $\mathbb{B}$ have one zero-divisor set,
$\{\tilde Q\neq0:C(\tilde Q)=0\}$, where $C$ is the central square (**Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space**). The block's set contains it, and it contains more.

**Theorem (the block's set contains the general one).** Every zero divisor of a general product is
a zero divisor of the block, and the inclusion is strict: the union of the block's two families is

$$
\{\tilde Q\neq0:Q_0=0\}\ \cup\ \{\tilde Q\neq0:C(\tilde Q)=0\}
\;\supsetneq\;
\{\tilde Q\neq0:C(\tilde Q)=0\} .
$$

*Proof.* The second family of the block is exactly the general set, so the general set is
contained. The enlargement is the set $\{Q_0=0,\ C(\tilde Q)\neq0\}$, nonempty: it contains $e_1$,
whose scalar part vanishes and whose central square is $c(e_1)=1$.

The difference is therefore the **pure non-isotropic vectors**: the elements of the vector subspace
whose central square does not vanish. On $e_1$ the general products give $e_1e_1=-e_0\neq0$, while
the block gives $e_1\star e_2=0$ at $e_2$; the general criterion is blind to $e_1$ and the block's
is not.

**Remark (why the symmetric part enlarges the set).** A general product of the row assigns to the
pair $(\tilde Q,\tilde R)$ a value whose first slot carries the natural conjugation; the block is
the half-sum of the two orders of its generating product, and the half-sum cancels the cross
product that the general products leave in the value (*Introduction to the Symmetric Quaternionic
Sesqualgebra of Biquaternions*). The cancellation removes one complex condition from the vanishing
equations of a pure pair, and one condition is the whole difference between the two rows.

## The Complement: the Regular Elements

**Definition.** A nonzero element of the block that is neither a left nor a right zero divisor is
**regular**. The origin is the only element excluded from both classes: an element is either the
origin, a zero divisor (on both sides), or regular.

**Theorem (the regular elements).** $\tilde Q$ is regular exactly when

$$
Q_0\neq0
\qquad\text{and}\qquad
C(\tilde Q)\neq0 .
$$

*Proof.* The complement of the block's two families is the negation of the criterion of §*The
Criterion*: $Q_0\neq0$ and $C(\tilde Q)\neq0$. By §*The Two Sides and the Annihilators* the left
and the right predicates coincide, so being neither is the same as being one of them is false.

The regular elements are exactly the elements whose left multiplication is injective, by the
corollary of §*The Two Sides and the Annihilators*; they are the largest class on which the
operator calculus of the block is faithful. They are not invertible: the block has no unit (*Norm
and Invertibility in the Symmetric Quaternionic Sesqualgebra*), so regularity is the substitute for
invertibility that the absence of a unit leaves.

**Remark (the Krein form does not detect the zero divisors).** The scalar part of the block's
square is the Krein form $K(\tilde Q,\tilde Q)=|Q_0|^2-\sum_k|Q_k|^2$. On $e_0+e_1$ it vanishes,
$K(e_0+e_1,e_0+e_1)=1-1=0$, while the element is regular, since $c(e_0+e_1)=1+1=2\neq0$; and on
$e_1$ it does not vanish, $K(e_1,e_1)=-1$, while $e_1$ is a zero divisor. So neither implication
$K(\tilde Q,\tilde Q)=0\Rightarrow$ zero divisor nor its converse holds, in contrast with the plain
product where the vanishing of the central square is the criterion. The form $K$ and its isotropic
cone are *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*.

## Worked Examples

**A pure zero divisor.** $\tilde Q=e_1$: $Q_0=0$, so it is a zero divisor, and $e_1\star e_2=0$
exhibits a nonzero annihilating partner. Its central square is $c(e_1)=1\neq0$, so it is not in the
general set.

**A regular element, not a zero divisor.** $\tilde Q=e_0$: $Q_0=1\neq0$ and $c(e_0)=1\neq0$, so it
is regular; it is the unit candidate and it is not a zero divisor, though it is not a unit.

**A non-pure zero divisor.** $\tilde Q=e_0+ie_1$: $C(\tilde Q)=1+i^2=1-1=0$ and $Q_0=1$, so it is a
zero divisor, and indeed $(e_0+ie_1)\star(e_0+ie_1)=0$, so it annihilates itself.

**A regular non-central element.** $\tilde Q=e_0+e_1$: $Q_0=1$ and $C(\tilde Q)=2$, so it is
regular; it is the witness that the Krein form does not detect the zero divisors.

**The annihilating partner of a non-pure zero divisor.** $\tilde Q=e_0+ie_1$, so $Q_0=1$, $Q_1=i$
and $C(\tilde Q)=0$. Choose $R_0=i$; the vector equation gives
$\overline{R_1}=-(\overline{R_0}/Q_0)Q_1=-((-i)/1)(i)=-1$, that is $R_1=-1$, and the partner is
$\tilde R=ie_0-e_1$; one checks $(e_0+ie_1)\star(ie_0-e_1)=0$.

## Summary

The zero divisor of the block is defined by an equation in the product, and the block's set is

$$
\{\tilde Q\neq0:Q_0=0\}\ \cup\ \{\tilde Q\neq0:C(\tilde Q)=0\},
\qquad C(\tilde Q)=Q_0^2+(\mathbf Q,\mathbf Q),
$$

the disjoint union of the pure family, the nonzero elements of the vector subspace, and the
non-pure family, the elements with nonzero scalar part and vanishing central square. The block is
conjugate-commutative, so the left and the right zero divisors coincide, the two annihilators of an
element are one set, and every zero divisor is two-sided. The annihilator is a complex plane in the
pure case and a complex line in the non-pure case, and the left multiplication of an element is
injective exactly on the regular elements $Q_0\neq0$, $C(\tilde Q)\neq0$, with rank eight, six and
four according to the class and rank zero at the origin.

The block's set strictly contains the single zero-divisor set $\mathcal{C}$ of the four general
products, the difference being the pure non-isotropic vectors: $e_1$ is a zero divisor of the block
with $c(e_1)=1$. The Krein form does not detect the zero divisors, vanishing on the regular
$e_0+e_1$ and not on the zero divisor $e_1$; the block has no unit, so the regular elements are the
substitute for the invertible ones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q\star\tilde R=\tfrac12(\tilde Q^{\natural}\tilde R^{*}+\tilde R^{*}\tilde Q^{\natural})$ | the symmetric quaternionic sesquilinear product, the block |
| $C(\tilde Q)=Q_0^2+(\mathbf Q,\mathbf Q)=\sum_\mu Q_\mu^2$ | the central square, deciding the criterion |
| $\{\tilde Q\neq0:Q_0=0\}$ | the pure family of the zero divisors |
| $\{\tilde Q\neq0:C(\tilde Q)=0\}$ | the non-pure family, the general set |
| $A_\star(\tilde Q)$ | the annihilator, of complex dimension two or one |
| $Q_0\neq0,\ C(\tilde Q)\neq0$ | the regular elements |
| $K(\tilde Q,\tilde Q)=|Q_0|^2-\sum_k|Q_k|^2$ | the Krein form, which does not detect the zero divisors |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), §*The Zero Divisor and the Annihilator*, for the definition relative to a general product and for the dictionary of the classes against the four general products.
- *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the single zero-divisor set of the four general products and the proof that the four definitions coincide.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the same class in the plain product, with the criterion, the two families and the annihilators.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product, its class and its conjugate-commutativity.
- *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-sesqualgebra.md`), for the operators whose kernels are the annihilators.
- *Norm and Invertibility in the Symmetric Quaternionic Sesqualgebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-quaternionic-sesqualgebra.md`), for the absence of a unit and the regularity that replaces invertibility.
- *Annihilators of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/annihilators-of-the-symmetric-quaternionic-sesqualgebra.md`), below this article in this category, the companion article, for the plane-or-line annihilator and the rank table
