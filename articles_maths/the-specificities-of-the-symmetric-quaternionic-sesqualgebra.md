# __The Specificities of the Symmetric Quaternionic Sesqualgebra__

## Introduction

This article isolates the block among the twelve structures of the biquaternion complex space by a single
law, the law of being **$K$-Hermitian**, and it runs the eleven comparisons. The block is the symmetric
quaternionic sesquilinear product
$\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ of
*Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*; the twelve structures and their
four general products are the subject of *The 12 Products of the Biquaternion Complex Space*, and the model
of the method is *The Specificities of the General Plain Algebra*, which isolates the plain product by left
alternativity and runs the same eleven comparisons. The twin articles are
*The Specificities of the General Quaternionic Algebra* and *The Specificities of the Symmetric Quaternionic
Algebra*.

The law has two clauses, and each is an identity in the product. The first is the **conjugate-symmetry**
$\tilde P\star\tilde Q=\overline{\tilde Q\star\tilde P}$, which is to say that the product is fixed by the
adapted exchange of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the second is that
the **scalar part is the Krein form**, $\mathrm{Sc}(\tilde P\star\tilde Q)=K(\tilde P,\tilde Q)$, the form
of *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* and *The Krein Gram Matrix and
the Restrictions of the Form*. The theorem of the article is that among the twelve structures the block is
the only one satisfying both clauses, each clause alone being satisfied by another structure: the plain
sesquilinear symmetric part satisfies the first and not the second, and the general quaternionic sesquilinear
product satisfies the second and not the first. The law is therefore sharp, and the two structures that
border it are named and used as the witnesses of the sharpness.

The product is *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*; its diagonal is
*The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic Sesqualgebra*; its element theory
is *Norm and Invertibility in the Symmetric Quaternionic Sesqualgebra*, *Zero Divisors of the Symmetric
Quaternionic Sesqualgebra*, *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic
Sesqualgebra*, *Square Roots of a General Element in the Symmetric Quaternionic Sesqualgebra*,
*Idempotents of the Symmetric Quaternionic Sesqualgebra* and *Nilpotents of the Symmetric Quaternionic
Sesqualgebra*; and its operators are *The Multiplication Operators of the Symmetric Quaternionic
Sesqualgebra*, where the $K$-adjointness that the law delivers is computed.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$,
$e_k^2=-e_0$ and $e_1e_2=e_3$; $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$ and central
scalar imaginary $i$; $\mathbf Q=\sum_kQ_ke_k$; $(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$; ${}^{\natural}$ negates
$e_1,e_2,e_3$ and fixes the coefficients, $\bar{\cdot}$ conjugates the coefficients, and
${}^{*}={}^{\natural}\circ\bar{\cdot}$; $\mathrm{Sc}(\tilde X)=X_0$ is the scalar part;
$\varepsilon=(1,-1,-1,-1)$; and

$$
K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}
=P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})
$$

is the Krein form. The twelve structures are the four general products
$\mathrm{GPA},\mathrm{GQA},\mathrm{GPS},\mathrm{GQS}$, their four symmetric parts
$\mathrm{SPA},\mathrm{SQA},\mathrm{SPS},\mathrm{SQS}$ and their four antisymmetric parts
$\mathrm{APA},\mathrm{AQA},\mathrm{APS},\mathrm{AQS}$, with the two first rows bilinear and the two last
rows sesquilinear, as in *The 12 Products of the Biquaternion Complex Space*.
Throughout, the block is $\mathrm{SQS}$, and the products of the twelve are written with their three-letter
names.

## The Law: Being $K$-Hermitian

**Definition ($K$-Hermitian product).** A product $\circ$ on $\mathbb{B}$ is **$K$-Hermitian** when the two
identities

$$
\text{(C1)}\quad \tilde P\circ\tilde Q=\overline{\tilde Q\circ\tilde P},
\qquad
\text{(C2)}\quad \mathrm{Sc}\bigl(\tilde P\circ\tilde Q\bigr)=K(\tilde P,\tilde Q)
$$

hold for all $\tilde P,\tilde Q\in\mathbb{B}$. The first is the **conjugate-symmetry** of the product, the
second is the **scalar-part identity**.

**Remark (the two clauses read one at a time).** The clause (C1) says that the product is fixed by the
adapted exchange $f\mapsto\overline{f\circ E}$, the transposition composed with the coefficientwise
conjugation, which is the exchange that keeps the sesqualgebra class
(*The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*). The clause (C2) says that the scalar
part of the product is the form $K$ and not another of the four forms of the row, the complex bilinear form,
the plain Hermitian form or the plain bilinear form. Each clause is an identity in $\tilde P,\tilde Q$ and
each is invariant under the change of the product, so they can be tested one structure at a time.

**Theorem (the block is $K$-Hermitian).** The block satisfies (C1) and (C2).

*Proof.* The scalar–vector form of *Introduction to the Symmetric Quaternionic Sesqualgebra of
Biquaternions* is

$$
\tilde P\star\tilde Q=\bigl[P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})\bigr]-P_0\overline{\mathbf Q}-\overline{Q_0}\mathbf P;
$$

the bracket is $K(\tilde P,\tilde Q)$ and is the scalar part, which is (C2). For (C1), conjugate the product with the arguments exchanged and use that the two
conjugations are anti-automorphisms of the plain product: the scalar bracket is fixed because $K$ is
Hermitian, and the vector part $-Q_0\overline{\mathbf P}-\overline{Q_0}\mathbf P$ is the same as the vector
part of $\tilde P\star\tilde Q$. So $\overline{\tilde Q\star\tilde P}=\tilde P\star\tilde Q$.

## The Criterion

**Theorem (the specificity).** Among the twelve structures of the biquaternion complex space, the block
$\mathrm{SQS}$ is the only $K$-Hermitian product.

*Proof.* The block is $K$-Hermitian by the theorem of §*The Law*, so it remains to test the eleven others,
which is done one structure at a time in §*The Eleven Comparisons*; each fails at least one of the two
clauses, and the failure is exhibited by a named pair.

The remainder of the article is the comparison. The verdict is collected in the table of §*The Table of the
Twelve*.

## The Eleven Comparisons

Every comparison is a computation with the multiplication table
$e_0\circ e_0=e_0$, $e_0\circ e_k=e_k\circ e_0=-e_k$, $e_k\circ e_k=-e_0$ and
$e_j\circ e_k=0$ for distinct $j,k\in\{1,2,3\}$ of the block,
together with the analogous tables of the eleven other structures read from *The 12 Products of the
Biquaternion Complex Space*; only the values needed for the failure are recorded. Three witnesses suffice
throughout: the pair $(ie_1,e_1)$, where a bilinear product reverses the imaginary unit and the two sides of
(C1) are $\mp ie_0$; the pair $(e_1,e_2)$, where the two sides of (C1) are the opposite signs of $e_3$; and
the elements $ie_1$ and $e_1$, where the bilinear and the definite forms differ from $K$.

**The four general products.**

- $\mathrm{GPA}(\tilde P,\tilde Q)=\tilde P\tilde Q$: (C1) fails at $(ie_1,e_1)$, where
  $\mathrm{GPA}(ie_1,e_1)=-ie_0$ while $\overline{\mathrm{GPA}(e_1,ie_1)}=ie_0$; (C2) fails, since
  $\mathrm{GPA}$ is bilinear, at $ie_1$, where $\mathrm{Sc}(\mathrm{GPA}(ie_1,ie_1))=1$ while
  $K(ie_1,ie_1)=-1$.
- $\mathrm{GQA}(\tilde P,\tilde Q)=\tilde P^{\natural}\tilde Q$: (C1) fails at $(ie_1,e_1)$, the two sides
  being $ie_0$ and $-ie_0$; (C2) fails at $e_1$, where $\mathrm{Sc}(\mathrm{GQA}(e_1,e_1))=1$ while
  $K(e_1,e_1)=-1$.
- $\mathrm{GPS}(\tilde P,\tilde Q)=\tilde P\tilde Q^{*}$: (C1) fails at $(e_1,e_2)$, the two sides being
  $-e_3$ and $e_3$; (C2) fails at $e_1$, where $\mathrm{Sc}(\mathrm{GPS}(e_1,e_1))=1\neq-1$.
- $\mathrm{GQS}(\tilde P,\tilde Q)=\tilde P^{\natural}\tilde Q^{*}$: (C1) fails at $(e_1,e_2)$, the two
  sides being $e_3$ and $-e_3$; (C2) holds, since $\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=K(\tilde P,\tilde Q)$ by the multiplication table.

**The four symmetric parts.**

- $\mathrm{SPA}(\tilde P,\tilde Q)=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$: (C1) fails at $(ie_1,e_1)$,
  the two sides being $-ie_0$ and $ie_0$; (C2) fails at $ie_1$, with $1\neq-1$.
- $\mathrm{SQA}(\tilde P,\tilde Q)=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$: (C1)
  fails at $(ie_1,e_1)$, the two sides being $ie_0$ and $-ie_0$; (C2) fails at $e_1$, with $1\neq-1$.
- $\mathrm{SPS}(\tilde P,\tilde Q)=\tfrac12(\tilde P\tilde Q^{*}+\overline{\tilde Q\tilde P^{*}})$: (C1)
  holds, the product being a symmetric part under the adapted exchange; (C2) fails at $e_1$, where the
  scalar part of $\mathrm{SPS}$ is the definite form $|P_0|^2+\lVert\mathbf P\rVert^2$, equal to $1$ there,
  while $K(e_1,e_1)=-1$.
- $\mathrm{SQS}$: both clauses, by the theorem of §*The Law*.

**The four antisymmetric parts.** Each is the skew-conjugate-symmetric companion of its general product,
$\mathrm{A}(P,Q)=-\overline{\mathrm{A}(Q,P)}$; if (C1) held as well then the two relations would give
$\mathrm{A}(P,Q)=0$ for all pairs, which is false, so (C1) fails for all four. And each fails (C2), since
the scalar part of all four vanishes identically: for $\mathrm{APA}$ and $\mathrm{AQA}$ because
$\mathrm{Sc}(\tilde P\tilde Q)=\mathrm{Sc}(\tilde Q\tilde P)$; for $\mathrm{APS}$ because the two halves
$PQ^*$ and $\overline{QP^*}$ have the same scalar part,
$\mathrm{Sc}(\overline{\tilde Q\tilde P^*})=\mathrm{Sc}(\tilde P\tilde Q^*)$; for $\mathrm{AQS}$ because
$\mathrm{Sc}(\mathrm{GQS})$ is the Hermitian form $K$ and
$\mathrm{Sc}(\mathrm{AQS})=\tfrac12\bigl(K(P,Q)-\overline{K(Q,P)}\bigr)=0$. In every case the value at
$e_1$ is $0$ while $K(e_1,e_1)=-1$.

## The Table of the Twelve

| structure | (C1) conjugate-symmetry | (C2) scalar part $K$ | $K$-Hermitian |
|---|---|---|---|
| $\mathrm{GPA}$ | fails at $(ie_1,e_1)$ | fails at $ie_1$ | no |
| $\mathrm{GQA}$ | fails at $(ie_1,e_1)$ | fails at $e_1$ | no |
| $\mathrm{GPS}$ | fails at $(e_1,e_2)$ | fails at $e_1$ | no |
| $\mathrm{GQS}$ | fails at $(e_1,e_2)$ | holds | no |
| $\mathrm{SPA}$ | fails at $(ie_1,e_1)$ | fails at $ie_1$ | no |
| $\mathrm{SQA}$ | fails at $(ie_1,e_1)$ | fails at $e_1$ | no |
| $\mathrm{SPS}$ | holds | fails at $e_1$ | no |
| $\mathrm{SQS}$ | holds | holds | **yes** |
| $\mathrm{APA}$ | fails (skew) | fails at $e_1$ | no |
| $\mathrm{AQA}$ | fails (skew) | fails at $e_1$ | no |
| $\mathrm{APS}$ | fails (skew) | fails at $e_1$ | no |
| $\mathrm{AQS}$ | fails (skew) | fails at $e_1$ | no |

The table is the whole content of the theorem: the block is the single row with both entries present.

## The Boundary of the Criterion

The criterion is sharp, and the sharpness is named.

**Theorem (each clause alone is satisfied by another structure).** Deleting (C1) admits the general
quaternionic sesquilinear product $\mathrm{GQS}$; deleting (C2) admits the symmetric plain sesquilinear part
$\mathrm{SPS}$.

*Proof.* $\mathrm{GQS}$ satisfies (C2) and fails (C1) (§*The Eleven Comparisons*), and $\mathrm{SPS}$
satisfies (C1) and fails (C2).

The two boundary structures are the companions of the block in the sesquilinear row: $\mathrm{GQS}$ is the
product of which the block is the symmetric part, and $\mathrm{SPS}$ is the symmetric part of the plain
sesquilinear product. The block is their meeting point: it has the scalar part of the first and the symmetry
of the second.

## What the Criterion Delivers

**The scalar part is the form, not a value.** The clause (C2) makes the scalar projection of the product the
Krein form, so the diagonal of the block is
$\tilde Q\star\tilde Q=K(\tilde Q,\tilde Q)e_0-Q_0\overline{\mathbf Q}-\overline{Q_0}\mathbf Q$; the
non-centrality of the diagonal, the shape of the idempotents and the square-zero cone all follow from that
one formula, as in *The Non-Central Diagonal and the Two Halves of the Symmetric Quaternionic
Sesqualgebra*, *Idempotents of the Symmetric Quaternionic Sesqualgebra* and *Nilpotents of the Symmetric
Quaternionic Sesqualgebra*.

**The $K$-adjoint of the multiplication.** The clause (C1), together with the natural conjugation as the
compatibility involution, gives the operator identity

$$
K\bigl(L^{\star}_{\tilde A}\tilde X,\tilde Y\bigr)
=\overline{K\bigl(\tilde X,L^{\star}_{\tilde A^{\natural}}\tilde Y\bigr)} ,
$$

so the adjoint of the left multiplication by $\tilde A$ with respect to $K$ is the left multiplication by
$\tilde A^{\natural}$; the identity is computed in *The Multiplication Operators of the Symmetric
Quaternionic Sesqualgebra*, and it is the operator form of the law.

**The element theory is governed by the law.** The two clauses fix the scalar part and the exchange; the
class of an element of the block — regular, pure zero divisor, non-pure zero divisor — is then decided by
the scalar coordinate $Q_0$ and the central square $c(\tilde Q)$, and not by the form $K$, as in *Zero
Divisors of the Symmetric Quaternionic Sesqualgebra*.

**The boundary.** A product with the scalar part $K$ but without the symmetry, such as $\mathrm{GQS}$, has a
diagonal whose vector part carries the cross product in addition to the mixed term; a product with the
symmetry but without the scalar part $K$, such as $\mathrm{SPS}$, has a central diagonal. The block is the
unique product whose diagonal keeps the mixed term and the form at once, with neither the extra cross term
of the first boundary nor the vanishing vector part of the second.

## Worked Examples

**The block at the witness $e_0,e_1$.** $\mathrm{SQS}(e_0,e_1)=-e_1$ and
$\overline{\mathrm{SQS}(e_1,e_0)}=\overline{-e_1}=-e_1$, so (C1) holds; and
$\mathrm{Sc}(\mathrm{SQS}(e_0,e_1))=0=K(e_0,e_1)$, so (C2) holds.

**The boundary $\mathrm{GQS}$ at the witness $(e_1,e_2)$.**
$\mathrm{GQS}(e_1,e_2)=e_3$ while $\overline{\mathrm{GQS}(e_2,e_1)}=\overline{-e_3}=-e_3$, so (C1) fails and
the product is not $K$-Hermitian; its scalar part is $K$, as (C2) requires.

**The boundary $\mathrm{SPS}$ at the witness $e_1$.**
$\mathrm{Sc}(\mathrm{SPS}(e_1,e_1))=1$ while $K(e_1,e_1)=-1$, so (C2) fails; the product is
conjugate-symmetric, as (C1) requires. Its diagonal is central,
$\mathrm{SPS}(\tilde Q,\tilde Q)=\bigl(|Q_0|^2+\lVert\mathbf Q\rVert^2\bigr)e_0$.

**A bilinear structure at a complex witness.** $\mathrm{SPA}(ie_1,ie_1)=(ie_1)^2=e_0$, with scalar part
$1$, while $K(ie_1,ie_1)=-1$: a bilinear product cannot see the modulus of a complex coefficient, and its
scalar part is the complex bilinear form and never the Hermitian form $K$.

## Summary

The block is isolated among the twelve structures of the biquaternion complex space by the law of being
$K$-Hermitian: the product is conjugate-symmetric,
$\tilde P\star\tilde Q=\overline{\tilde Q\star\tilde P}$, and its scalar part is the Krein form,
$\mathrm{Sc}(\tilde P\star\tilde Q)=K(\tilde P,\tilde Q)$. The block satisfies both clauses; the eleven other
structures each fail at least one, the failures being read at the pairs $(ie_1,e_1)$ and $(e_1,e_2)$ and at
the elements $e_1$ and $ie_1$. The criterion is sharp: deleting the conjugate-symmetry admits the general quaternionic sesquilinear
product $\mathrm{GQS}$, and deleting the scalar-part identity admits the symmetric plain sesquilinear part
$\mathrm{SPS}$; the block is the meeting point of the two, with the scalar part of the first and the symmetry
of the second. The law delivers the diagonal formula with the Krein form in its scalar part, the
$K$-adjointness of the left multiplications, $L^{\star}_{\tilde A}{}^{\dagger}=L^{\star}_{\tilde A^{\natural}}$,
and the element theory in which the class of an element is decided by the scalar coordinate and the central
square.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{SQS}$ | the block, the symmetric quaternionic sesquilinear product |
| $\tilde P\circ\tilde Q=\overline{\tilde Q\circ\tilde P}$ | the clause (C1), conjugate-symmetry |
| $\mathrm{Sc}(\tilde P\circ\tilde Q)=K(\tilde P,\tilde Q)$ | the clause (C2), the scalar-part identity |
| $K(\tilde P,\tilde Q)=P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})$ | the Krein form, the scalar part of the block |
| $\mathrm{GQS}$ | the boundary of (C1): scalar part $K$, no symmetry |
| $\mathrm{SPS}$ | the boundary of (C2): conjugate-symmetric, definite scalar part |
| $K(L^{\star}_{\tilde A}\tilde X,\tilde Y)=\overline{K(\tilde X,L^{\star}_{\tilde A^{\natural}}\tilde Y)}$ | the $K$-adjointness delivered by the law |

## Further Reading

- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra.md`), the model of the method, where left alternativity isolates the plain product among the twelve.
- *The Specificities of the General Quaternionic Algebra* (`articles_maths/the-specificities-of-the-general-quaternionic-algebra.md`) and *The Specificities of the Symmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-symmetric-quaternionic-algebra.md`), the twin articles, for the operator laws of the two neighbouring structures.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the twelve structures, their four general products and their parts.
- *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.md`), for the adapted exchange that the clause (C1) names.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product, its scalar part and its diagonal.
- *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-sesqualgebra.md`), for the $K$-adjointness and the operators of the block.
