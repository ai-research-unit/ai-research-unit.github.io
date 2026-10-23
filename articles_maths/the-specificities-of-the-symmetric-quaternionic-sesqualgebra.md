# __The Specificities of the Symmetric Quaternionic Sesqualgebra__

## Introduction

This article isolates the block among the twelve structures of the biquaternion complex space by a single
law, the law of being **$\langle\cdot,\cdot\rangle_{\natural*}$-Hermitian**. The block is the symmetric
quaternionic sesquilinear product
$\tilde Q_1\star\tilde Q_2=\tfrac12(\tilde Q_1^{\natural}\tilde Q_2^{*}+\tilde Q_2^{*}\tilde Q_1^{\natural})$ of
*Introduction to the Symmetric Quaternionic Sesqualgebra*; the twelve structures and their
four general products are the subject of *The 12 Products of the Biquaternion Complex Space*, and the model
of the method is *The Specificities of the Biquaternion Algebra*, which isolates the plain product by left
alternativity. The twin articles are
*The Specificities of the General Quaternionic Algebra* and *The Specificities of the Symmetric Quaternionic
Algebra*.

The law has two clauses, and each is an identity in the product. The first is the **conjugate-symmetry**
$\tilde Q_1\star\tilde Q_2=\overline{\tilde Q_2\star\tilde Q_1}$, which is to say that the product is fixed by the
adapted exchange of *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; the second is that
the **scalar part is the Krein form**, $\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$, the form
of *Introduction to the General Quaternionic Sesqualgebra* and *The Krein Gram Matrix and
the Restrictions of the Form*. The theorem of the article is that among the twelve structures the block is
the only one satisfying both clauses, each clause alone being satisfied by another structure: the plain
sesquilinear symmetric part satisfies the first and not the second, and the general quaternionic sesquilinear
product satisfies the second and not the first. The law is therefore sharp, and the two structures that
border it are named and used as the witnesses of the sharpness.

The product is *Introduction to the Symmetric Quaternionic Sesqualgebra*; its diagonal is
*The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic Sesqualgebra*; its element theory
is *Norm and Invertibility in the Symmetric Quaternionic Sesqualgebra*, *Zero Divisors of the Symmetric
Quaternionic Sesqualgebra*, *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic
Sesqualgebra*, *Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*,
*Idempotents of the Symmetric Quaternionic Sesqualgebra* and *Nilpotents of the Symmetric Quaternionic
Sesqualgebra*; and its operators are *The Multiplication Operators of the Symmetric Quaternionic
Sesqualgebra*, where the $\langle\cdot,\cdot\rangle_{\natural*}$-adjointness that the law delivers is computed.

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\sum_\mu\varepsilon_\mu Q_{1,\mu}\overline{Q_{2,\mu}}
=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})
$$

is the Krein form. The twelve structures are the four general products
$\mathrm{GPA},\mathrm{GQA},\mathrm{GPS},\mathrm{GQS}$, their four symmetric parts
$\mathrm{SPA},\mathrm{SQA},\mathrm{SPS},\mathrm{SQS}$ and their four antisymmetric parts
$\mathrm{APA},\mathrm{AQA},\mathrm{APS},\mathrm{AQS}$, with the two first rows bilinear and the two last
rows sesquilinear, as in *The 12 Products of the Biquaternion Complex Space*.
Throughout, the block is $\mathrm{SQS}$, and the products of the twelve are written with their three-letter
names.

## The Law: Being $\langle\cdot,\cdot\rangle_{\natural*}$-Hermitian

**Definition ($\langle\cdot,\cdot\rangle_{\natural*}$-Hermitian product).** A product $\circ$ on $\mathbb{B}$ is **$\langle\cdot,\cdot\rangle_{\natural*}$-Hermitian** when the two
identities

$$
\text{(C1)}\quad \tilde Q_1\circ\tilde Q_2=\overline{\tilde Q_2\circ\tilde Q_1},
\qquad
\text{(C2)}\quad \mathrm{Sc}\bigl(\tilde Q_1\circ\tilde Q_2\bigr)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}
$$

hold for all $\tilde Q_1,\tilde Q_2\in\mathbb{B}$. The first is the **conjugate-symmetry** of the product, the
second is the **scalar-part identity**.

**Remark (the two clauses read one at a time).** The clause (C1) says that the product is fixed by the
adapted exchange $f\mapsto\overline{f\circ E}$, the transposition composed with the coefficientwise
conjugation, which is the exchange that keeps the sesqualgebra class
(*The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*). The clause (C2) says that the scalar
part of the product is the form $\langle\cdot,\cdot\rangle_{\natural*}$ and not another of the four forms of the row, the complex bilinear form,
the plain Hermitian form or the plain bilinear form. Each clause is an identity in $\tilde Q_1,\tilde Q_2$ and
each is invariant under the change of the product, so they can be tested one structure at a time.

**Theorem (the block is $\langle\cdot,\cdot\rangle_{\natural*}$-Hermitian).** The block satisfies (C1) and (C2).

*Proof.* The scalar–vector form of *Introduction to the Symmetric Quaternionic Sesqualgebra of
Biquaternions* is

$$ \boxed{\; \tilde Q_1\star\tilde Q_2=\bigl[Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})\bigr]-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1 \;}; $$

the bracket is $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$ and is the scalar part, which is (C2). For (C1), conjugate the product with the arguments exchanged and use that the two
conjugations are anti-automorphisms of the plain product: the scalar bracket is fixed because $\langle\cdot,\cdot\rangle_{\natural*}$ is
Hermitian, and the vector part $-Q_{2t}\overline{\vec Q_1}-\overline{Q_{2t}}\vec Q_1$ is the same as the vector
part of $\tilde Q_1\star\tilde Q_2$. So $\overline{\tilde Q_2\star\tilde Q_1}=\tilde Q_1\star\tilde Q_2$.

## The Criterion

**Theorem (the specificity).** Among the twelve structures of the biquaternion complex space, the block
$\mathrm{SQS}$ is the only $\langle\cdot,\cdot\rangle_{\natural*}$-Hermitian product.

*Proof.* The block is $\langle\cdot,\cdot\rangle_{\natural*}$-Hermitian by the theorem of §*The Law: Being $\langle\cdot,\cdot\rangle_{\natural*}$-Hermitian*; the other eleven are disposed of in
§*The Isolation among the Twelve*, each failing at least one of the two clauses on a named pair.

## The Isolation among the Twelve

**Theorem (the isolation).** Among the twelve structures of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, the block is the only $\langle\cdot,\cdot\rangle_{\natural*}$-Hermitian product.

*Proof.* The block satisfies both clauses by §*The Law: Being $\langle\cdot,\cdot\rangle_{\natural*}$-Hermitian*. The other eleven each fail at least one clause. The three bilinear general products GPA and the bilinear parts SPA, SQA fail conjugate-symmetry at $(i\vec e_x,\vec e_x)$, where a bilinear product reverses the imaginary unit, and fail the scalar-part identity at the elements $\vec e_x$ and $i\vec e_x$, where the bilinear form differs from $\langle\cdot,\cdot\rangle_{\natural*}$; the two sesquilinear general products GPS and GQS fail conjugate-symmetry at $(\vec e_x,\vec e_y)$, where the two sides are opposite signs of $\vec e_z$, GQS satisfying the scalar-part identity while GPS fails it at $\vec e_x$; the symmetric plain sesquilinear part SPS satisfies conjugate-symmetry and fails the scalar-part identity at $\vec e_x$, its scalar part being the definite form $|Q_{1t}|^2+\lVert\vec Q_1\rVert^2$ and not $\langle\cdot,\cdot\rangle_{\natural*}$; and the four antisymmetric parts fail both, being skew-conjugate-symmetric — so conjugate-symmetry would force them to vanish — and having identically vanishing scalar part.

| family | structures | conjugate-symmetry | scalar part $\langle\cdot,\cdot\rangle_{\natural*}$ |
|---|---|---|---|
| the four general products | GPA, GQA | no | no |
| | GPS | no | no |
| | GQS | no | **yes** |
| the symmetric parts | SPA, SQA | no | no |
| | SPS | **yes** | no |
| | **SQS** | **yes** | **yes** |
| the antisymmetric parts | APA, AQA, APS, AQS | no | no |

The isolation is sharp, and each clause alone is satisfied by another structure: deleting conjugate-symmetry admits the general quaternionic sesquilinear product GQS, and deleting the scalar-part identity admits the symmetric plain sesquilinear part SPS. The two are the companions of the block in the sesquilinear row: GQS is the product of which the block is the symmetric part, and SPS is the symmetric part of the plain sesquilinear product. The block is their meeting point, carrying the scalar part of the first and the symmetry of the second.

## What the Criterion Delivers

**The scalar part is the form, not a value.** The clause (C2) makes the scalar projection of the product the
Krein form, so the diagonal of the block is
$\tilde Q\star\tilde Q=\langle\tilde Q,\tilde Q\rangle_{\natural*}e_t-Q_t\overline{\vec Q}-\overline{Q_t}\vec Q$; the
non-centrality of the diagonal, the shape of the idempotents and the square-zero cone all follow from that
one formula, as in *The Non-Central Algebraic Norm and the Two Halves of the Symmetric Quaternionic
Sesqualgebra*, *Idempotents of the Symmetric Quaternionic Sesqualgebra* and *Nilpotents of the Symmetric
Quaternionic Sesqualgebra*.

**The $\langle\cdot,\cdot\rangle_{\natural*}$-adjoint of the multiplication.** The clause (C1), together with the natural conjugation as the
compatibility involution, gives the operator identity

$$
\boxed{\;
K\bigl(L^{\star}_{\tilde Q_3}\tilde Q_1,\tilde Q_2\bigr)
=\overline{K\bigl(\tilde Q_1,L^{\star}_{\tilde Q_3^{\natural}}\tilde Q_2\bigr)}
\;},
$$

so the adjoint of the left multiplication by $\tilde Q_3$ with respect to $\langle\cdot,\cdot\rangle_{\natural*}$ is the left multiplication by
$\tilde Q_3^{\natural}$; the identity is computed in *The Multiplication Operators of the Symmetric
Quaternionic Sesqualgebra*, and it is the operator form of the law.

**The element theory is governed by the law.** The two clauses fix the scalar part and the exchange; the
class of an element of the block — regular, pure zero divisor, non-pure zero divisor — is then decided by
the scalar coordinate $Q_t$ and the central square $C(\tilde Q)$, and not by the form $\langle\cdot,\cdot\rangle_{\natural*}$, as in *Zero
Divisors of the Symmetric Quaternionic Sesqualgebra*.

**The boundary.** A product with the scalar part $\langle\cdot,\cdot\rangle_{\natural*}$ but without the symmetry, such as $\mathrm{GQS}$, has a
diagonal whose vector part carries the cross product in addition to the mixed term; a product with the
symmetry but without the scalar part $\langle\cdot,\cdot\rangle_{\natural*}$, such as $\mathrm{SPS}$, has a central diagonal. The block is the
unique product whose diagonal keeps the mixed term and the form at once, with neither the extra cross term
of the first boundary nor the vanishing vector part of the second.

## Worked Examples

**The block at the witness $(e_t,\vec e_x)$.** $\mathrm{SQS}(e_t,\vec e_x)=-\vec e_x$ and $\overline{\mathrm{SQS}(\vec e_x,e_t)}=\overline{-\vec e_x}=-\vec e_x$, so conjugate-symmetry holds; and $\mathrm{Sc}(\mathrm{SQS}(e_t,\vec e_x))=0=\langle e_t,\vec e_x\rangle_{\natural*}$, so the scalar-part identity holds.

**The scalar-part identity at a complex element.** $\mathrm{Sc}(\mathrm{SQS}(i\vec e_x,i\vec e_x))=\langle i\vec e_x,i\vec e_x\rangle_{\natural*}=-1$, the Hermitian form reading the modulus of the complex coefficient; a bilinear product cannot see it. This is the clause that separates the block from the bilinear structures, and the reason the block's scalar part is $\langle\cdot,\cdot\rangle_{\natural*}$ and not the complex bilinear form.

**The two clauses at the boundaries.** The general quaternionic sesquilinear product $\mathrm{GQS}$ has scalar part $\langle\cdot,\cdot\rangle_{\natural*}$ and fails conjugate-symmetry, and the symmetric plain sesquilinear part $\mathrm{SPS}$ is conjugate-symmetric with a definite scalar part; the block is the one product that carries both, neither the extra cross term of the first nor the central diagonal of the second.

## Summary

The block is isolated among the twelve structures of the biquaternion complex space by the law of being
$\langle\cdot,\cdot\rangle_{\natural*}$-Hermitian: the product is conjugate-symmetric,
$\tilde Q_1\star\tilde Q_2=\overline{\tilde Q_2\star\tilde Q_1}$, and its scalar part is the Krein form,
$\mathrm{Sc}(\tilde Q_1\star\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$. The block satisfies both clauses; the eleven other
structures each fail at least one, the failures being read at the pairs $(i\vec e_x,\vec e_x)$ and $(\vec e_x,\vec e_y)$ and at
the elements $\vec e_x$ and $i\vec e_x$. The criterion is sharp: deleting the conjugate-symmetry admits the general quaternionic sesquilinear
product $\mathrm{GQS}$, and deleting the scalar-part identity admits the symmetric plain sesquilinear part
$\mathrm{SPS}$; the block is the meeting point of the two, with the scalar part of the first and the symmetry
of the second. The law delivers the diagonal formula with the Krein form in its scalar part, the
$\langle\cdot,\cdot\rangle_{\natural*}$-adjointness of the left multiplications, $L^{\star}_{\tilde Q_3}{}^{\dagger}=L^{\star}_{\tilde Q_3^{\natural}}$,
and the element theory in which the class of an element is decided by the scalar coordinate and the central
square.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{SQS}$ | the block, the symmetric quaternionic sesquilinear product |
| $\tilde Q_1\circ\tilde Q_2=\overline{\tilde Q_2\circ\tilde Q_1}$ | the clause (C1), conjugate-symmetry |
| $\mathrm{Sc}(\tilde Q_1\circ\tilde Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$ | the clause (C2), the scalar-part identity |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$ | the Krein form, the scalar part of the block |
| $\mathrm{GQS}$ | the boundary of (C1): scalar part $\langle\cdot,\cdot\rangle_{\natural*}$, no symmetry |
| $\mathrm{SPS}$ | the boundary of (C2): conjugate-symmetric, definite scalar part |
| $\langle L^{\star}_{\tilde Q_3}\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\overline{\langle\tilde Q_1,L^{\star}_{\tilde Q_3^{\natural}}\tilde Q_2\rangle_{\natural*}}$ | the $\langle\cdot,\cdot\rangle_{\natural*}$-adjointness delivered by the law |

## Further Reading

- [The Specificities of the Biquaternion Algebra](the-specificities-of-the-biquaternion-algebra.html), the model of the method, where left alternativity isolates the plain product among the twelve.
- [The Specificities of the General Quaternionic Algebra](the-specificities-of-the-general-quaternionic-algebra.html) and [The Specificities of the Symmetric Quaternionic Algebra](the-specificities-of-the-symmetric-quaternionic-algebra.html), the twin articles, for the operator laws of the two neighbouring structures.
- [The 12 Products of the Biquaternion Complex Space](the-12-products-of-the-biquaternion-complex-space.html), for the twelve structures, their four general products and their parts.
- [The Symmetric and Antisymmetric Parts of a Sesqualgebra Product](the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.html), for the adapted exchange that the clause (C1) names.
- [Introduction to the Symmetric Quaternionic Sesqualgebra](introduction-to-the-symmetric-quaternionic-sesqualgebra.html), for the product, its scalar part and its diagonal.
- [The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra](the-multiplication-operators-of-the-symmetric-quaternionic-sesqualgebra.html), for the $\langle\cdot,\cdot\rangle_{\natural*}$-adjointness and the operators of the block.
