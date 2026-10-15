# __The Realification of the Symmetric Plain Sesqualgebra__

## Introduction

The Symmetric Plain Sesqualgebra is one of the twelve algebraic structures that the biquaternion space of $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ carries, the structure carried by the product
$$
\tilde P\star\tilde Q=\tfrac12\bigl(\tilde P\tilde Q^{*}+\overline{\tilde Q}\tilde P^{\natural}\bigr)=H(\tilde P,\tilde Q)e_0,
\qquad
H(\tilde P,\tilde Q)=\mathrm{Sc}\bigl(\tilde P\tilde Q^{*}\bigr)=P_0\overline{Q_0}+(\vec P,\overline{\vec Q}),
$$
which over $\mathbb{C}$ is the symmetric plain sesquilinear structure of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, and the only one of the twelve that is Hermitian (*The Specificities of the Symmetric Plain Sesqualgebra*). Read over $\mathbb{R}$, the same product on the same set is an $\mathbb{R}$-algebra on the eight-dimensional real space $\mathbb{R}^8$, and this article owns that real reading.

The general construction is not repeated here. The realification of a vector space, of a linear map and of a form, the doubling of the dimension, the complex structure $J$, the two rules of the realification of a form and the table of the four effects are *The Realification and the Effect of the Change of Scalars*; This article gives what is specific to this product: its real bilinear reading, the law of its second slot over the centre, the realification of the form it carries and the signature that follows, its real operators, and the four objects of the real reading that the Hermitian block adds.

## The Product Read over $\mathbb{R}$

The product is symmetric plain sesquilinear over $\mathbb{C}$ and $\mathbb{R}$-bilinear over $\mathbb{R}$, by §*The Effect on the Twelve Algebraic Structures* of *The Realification and the Effect of the Change of Scalars*. It is therefore an **$\mathbb{R}$-algebra** on $\mathbb{R}^8$ in the broad sense, the sense of a module with a bilinear multiplication. In that algebra conjugate-commutativity holds, $\tilde P\star\tilde Q=\overline{\tilde Q\star\tilde P}$; the square is central and definite, $\tilde Q\star\tilde Q=H(\tilde Q,\tilde Q)e_0=\lVert\tilde Q\rVert_E^{2}e_0$ with $\lVert\tilde Q\rVert_E^{2}=\sum_\mu\lvert Q_\mu\rvert^{2}>0$ off the origin; associativity fails, at the triple $(e_1,e_1,e_0)$ already, the Jordan identity fails with the witness $x=y=e_1$, and there is no unit.

Every ring-theoretic property is the same in the two readings, by the dictionary of the same article: a condition written with the addition, the product, $e_0$ and quantification over the elements is a statement about the ring and does not move when the scalars are restricted to $\mathbb{R}$. In particular the idempotents stay $\{0,e_0\}$, the nilpotents stay the vector subspace $\mathrm{Vect}(\mathbb{B})=\{P_0=0\}$ with index three, the zero divisors stay the complement of the origin, there is no unit, and there is no root of $-1$ (*Square Roots of One and the Idempotents of the Symmetric Plain Sesqualgebra*, *Square Roots of Zero and the Nilpotents of the Symmetric Plain Sesqualgebra* and *Zero Divisors of the Symmetric Plain Sesqualgebra*). What moves is what names the field: an image that is a complex line over $\mathbb{C}$ is a real plane over $\mathbb{R}$, and a scalar that is one complex number over $\mathbb{C}$ is two real numbers over $\mathbb{R}$.

The product is special by its image: it is **central-valued**, $\tilde P\star\tilde Q\in\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, of real dimension two, and the whole product collapses onto that plane. Over $\mathbb{C}$ this centrality is the second clause of the Hermitian criterion and is shared with the central sibling $\mathrm{SQA}$; the block is the one structure that adds conjugate-commutativity to it (*The Specificities of the Symmetric Plain Sesqualgebra*). Over $\mathbb{R}$ the collapse is the statement that the whole product is the form $H$ read as a multiplication, its image the real plane $\mathbb{C}_{\mathbb{B}}$; it is this collapse that makes the block's real reading at once the thinnest and the sharpest of the twelve.

## The Second Slot and the Centre

Over $\mathbb{C}$ the product is $\mathbb{C}$-sesquilinear: linear in the first slot and conjugate-linear in the second, the second slot being read through the coefficientwise conjugation $\bar{\cdot}$, whose restriction to the centre is $i\mapsto-i$, the Galois conjugation of $\mathbb{C}$ over $\mathbb{R}$; in the formula the conjugation enters through the Hermitian star ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The structure is therefore a **sesqualgebra over $(\mathbb{C},\bar{\cdot}\,)$**, one of the eight sesquilinear structures of the twelve, and not an algebra.

Read over $\mathbb{R}$, the involution disappears: the only automorphism of $\mathbb{R}$ is the identity, and a sesquilinear law with the identity involution is a bilinear law. The product is therefore an **$\mathbb{R}$-algebra**, and its second slot is $\mathbb{C}_{\mathbb{B}}$-conjugate-linear, by §*The Realification of a Linear Map* of *The Realification and the Effect of the Change of Scalars*: the left multiplication $L_{\tilde X}$ anticommutes with the complex structure, $L_{\tilde X}J=-JL_{\tilde X}$, the criterion for conjugate-linearity, while the right multiplication $R_{\tilde X}$ commutes, $R_{\tilde X}J=JR_{\tilde X}$, its slot being the linear one. The passage therefore **changes the kind** of this product — sesqualgebra over $\mathbb{C}$, algebra over $\mathbb{R}$ — and the distinction migrates from the field to the centre.

In the real basis the two criteria take the two block forms
$$
L:\begin{pmatrix}A&B\\ B&-A\end{pmatrix}\quad(\text{anticommuting with }J),\qquad
R:\begin{pmatrix}A&-B\\ B&A\end{pmatrix}\quad(\text{commuting with }J),
$$
the first the shape of the conjugate-linear maps and the second the shape of the $\mathbb{C}$-linear ones, by the same §*The Realification of a Linear Map*. The block is the instance in which the two shapes are carried by the two halves of one operator family, $L$ and $R$, and not by two unrelated maps.

## The Realified Form

The product carries the general plain sesquilinear, the Hermitian $H$ form, the scalar part of the general product of its family, quoted from *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*:
$$
H(\tilde P,\tilde Q)=\mathrm{Sc}\bigl(\tilde P\tilde Q^{*}\bigr)=P_0\overline{Q_0}+(\vec P,\overline{\vec Q}).
$$
Over $\mathbb{C}$ it is a Hermitian form of complex inertia $(4,0)$; the realification of a Hermitian form is not split but the **doubling** of its inertia, by §*The Realification of a Form* of *The Realification and the Effect of the Change of Scalars*: the form is real on the diagonal, the realification keeps its real part $\operatorname{Re}H$, and the realified signature is
$$
(8,0),
$$
with Gram matrix $\mathrm{I}_8$ on the basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$. The discarded imaginary part is not a second independent form: it is the alternating companion of the Hermitian structure, the Kähler form, and it is determined by the real part through $\operatorname{Im}H(\tilde P,\tilde Q)=\operatorname{Re}H(\tilde P,i\tilde Q)$, so that a Hermitian form needs **one** real form where a bilinear form needs two. On the realifications the complex structure preserves the form,
$$
\Phi_{\mathbb{R}}(JP,JQ)=+\Phi_{\mathbb{R}}(P,Q),
$$
the opposite of the bilinear case. The instance is the general plain sesquilinear form $H$, the Hermitian form, whose row in the table of *The Realification of the Four Forms*, §*The Four Gram Matrices*, is the Hermitian one. Because the block's product is exactly this form read as a multiplication, the form's realification is also the realification of the product: the signature $(8,0)$, the Gram matrix $\mathrm{I}_8$ and the null set $\{0\}$ belong to the block as much as to the form it carries, and they are the definite row of the four.

## The Real Operators

The left and the right multiplications by an element are the maps
$$
L_{\tilde X}:\tilde Y\mapsto\tilde X\star\tilde Y,\qquad R_{\tilde X}:\tilde Y\mapsto\tilde Y\star\tilde X,
$$
and over $\mathbb{R}$ they are $\mathbb{R}$-linear endomorphisms of $\mathbb{R}^8$, by §*The Realification of a Linear Map* of *The Realification and the Effect of the Change of Scalars*. By the criterion of the previous section, $L_{\tilde X}$ is $\mathbb{C}_{\mathbb{B}}$-conjugate-linear, of the anticommuting shape and of **real trace zero**, while $R_{\tilde X}$ is $\mathbb{C}_{\mathbb{B}}$-linear, of the commuting shape; their traces are the ones of *The Multiplication Operators of the Symmetric Plain Sesqualgebra*, $\operatorname{Tr}(L^{\star}_{\tilde X})=X_0$ in the conjugate-linear convention and $\operatorname{Tr}(R^{\star}_{\tilde X})=\overline{X_0}$, so that as real-linear endomorphisms they have traces $0$ and $2\operatorname{Re}X_0$, the second twice the real part of the complex trace.

The **trace form** of the real regular representation is the symmetric bilinear form
$$
\tau(\tilde P,\tilde Q)=\operatorname{Tr}_{\mathbb{R}}\bigl(L_{\tilde P}L_{\tilde Q}\bigr),
$$
the analogue for this block of $\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})$ of the general plain algebra. The composition law $L^{\star}_{\tilde P}L^{\star}_{\tilde Q}=P_0R^{\star}_{\tilde Q}$ of *The Multiplication Operators of the Symmetric Plain Sesqualgebra* evaluates it: $L_{\tilde P}L_{\tilde Q}=P_0R_{\tilde Q}$ has complex trace $P_0\overline{Q_0}$, so that
$$
\tau(\tilde P,\tilde Q)=2\operatorname{Re}\bigl(P_0\overline{Q_0}\bigr).
$$
The trace form is **degenerate**: its radical is the vector subspace $\mathrm{Vect}(\mathbb{B})$, of real dimension six, its rank is two, and it sees the real and the imaginary parts of the central coordinate $P_0$ alone. in the block's own terms it is the conjugate-linear map $\tilde S\mapsto\overline{S_0}\tilde X$, which is neither multiplication, as *The Multiplication Operators of the Symmetric Plain Sesqualgebra* computes.

## What Is Specific to This Product Read over $\mathbb{R}$

Four objects of the real reading are proper to the Hermitian block.

**The real subalgebras that are not complex.** Over $\mathbb{C}$ a subalgebra is a complex subspace, of even real dimension; over $\mathbb{R}$ there are subalgebras that no complex reading produces, because the product is central-valued and a real subspace closed under it need not be a complex subspace. The **quaternion subspace** $\mathbb{H}_{\mathbb{B}}=\mathbb{R}\{e_0,e_1,e_2,e_3\}$ and the **Hermitian subspace** $\mathbb{M}_{+}=\mathbb{R}\{e_0,ie_1,ie_2,ie_3\}$ are two real forms of real dimension four, and
$$
\mathbb{R}\{e_0,e_1,e_2\}
$$
is a real subalgebra of real dimension three: the odd dimension is the mark of the real reading. The vector subspace $\mathrm{Vect}(\mathbb{B})$ is **not** a subalgebra, because $e_1\star e_1=H(e_1,e_1)e_0=e_0$ leaves it; closure is a condition on the product, not on the coordinate span.

**The Galois-twisted automorphisms.** The coefficientwise conjugation $c=\overline{\cdot}$ is an $\mathbb{R}$-linear algebra automorphism of the block, because $\overline{\tilde P\star\tilde Q}=\overline{\tilde P}\star\overline{\tilde Q}$, an identity which is conjugate-commutativity read on the involution, and $c$ is not $\mathbb{C}$-linear, since it induces the Galois conjugation $\kappa$ on the centre. Hence the real automorphism group of the block is **twice** the complex one,
$$
\operatorname{Aut}_{\mathbb{R}}(\star)=\operatorname{Aut}_{\mathbb{C}}(\star)\cup c\,\operatorname{Aut}_{\mathbb{C}}(\star),
$$
the extra coset conjugate-linear: the complex automorphisms are the elements of $G_H$ fixing $e_0$ (*The Multiplication Operators of the Symmetric Plain Sesqualgebra*), and the passage to $\mathbb{R}$ adds the Galois twist of $\mathbb{C}/\mathbb{R}$.

**The real-quaternion coincidence.** On the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ the block **coincides with the symmetric quaternionic algebra** $\mathrm{SQA}$ of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*:
$$
\tilde P\star\tilde Q=\mathrm{SQA}(\tilde P,\tilde Q)\qquad(\tilde P,\tilde Q\in\mathbb{H}_{\mathbb{B}}),
$$
because on the real quaternions the Hermitian form $H$ agrees with the quaternionic form $N$ and the vector part of the quaternionic product is antisymmetric, hence killed by the symmetrisation. Over $\mathbb{C}$ the two structures are distinct on the whole space; the real reading makes them meet on a real form, and the coincidence is a statement of the real reading and not of the products.

**The trivial null set against the punctured zero-divisor set.** The realified form is positive definite, so the block's **null set** — the isotropic set of $H$ — is the origin alone, and the block has no isotropic line and no hyperbolic plane (*The Realification of the Four Forms*). The **zero-divisor set** of the ring is the complement of the origin, every nonzero element being a zero divisor because the form is non-degenerate and its orthogonal hyperplanes are nonzero (*Zero Divisors of the Symmetric Plain Sesqualgebra*). The two sets are the two extremes of $\mathbb{R}^8$, one point and its complement, and they are **disjoint**: the diagonal of $H$ is definite. Over an indefinite sibling the realified form has signature $(4,4)$ and a null set of real dimension seven, a genuine cone instead of a point; the definiteness of the Hermitian diagonal is what reduces the null set to the origin.

## Summary

The Symmetric Plain Sesqualgebra read over $\mathbb{R}$ is the same product on the same elements, an $\mathbb{R}$-algebra on $\mathbb{R}^8$ in which conjugate-commutativity holds, the square is the central element $H(\tilde Q,\tilde Q)e_0=\lVert\tilde Q\rVert_E^{2}e_0$, associativity and the Jordan identity fail, and there is no unit; every ring-theoretic property, the idempotents, the nilpotents, the zero divisors and the absent root of $-1$ included, is unchanged. Its second slot is $\mathbb{C}_{\mathbb{B}}$-conjugate-linear, so the left multiplications anticommute with the complex structure $J$, have real trace zero, and carry the anticommuting block shape, while the right multiplications commute and carry the commuting one. It carries the Hermitian form $H$, whose realification is positive definite of signature $(8,0)$ and is preserved by $J$. The trace form of the real regular representation is degenerate, of rank two, its radical the vector subspace, against the non-degenerate $(4,4)$ of the general plain algebra. Four objects are proper to the real reading of the block: the real subalgebras that are not complex, among them the odd-dimensional $\mathbb{R}\{e_0,e_1,e_2\}$; the Galois-twisted automorphism group, twice the complex one; the coincidence with the symmetric quaternionic algebra on the real quaternions; and the contrast between the trivial null set of the form and the punctured zero-divisor set of the ring.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tfrac12\bigl(\tilde P\tilde Q^{*}+\overline{\tilde Q}\tilde P^{\natural}\bigr)=H(\tilde P,\tilde Q)e_0$ | the product of the Symmetric Plain Sesqualgebra |
| $\mathbb{R}^8$ | the realification of $\mathbb{B}$, the eight real basis elements $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre, the field of scalars carried by the ring, of real dimension two |
| $J$ | the complex structure, multiplication by $i$, of square $-1$, $=\operatorname{Res}_{\mathbb{C}/\mathbb{R}}(i\,\cdot\,)$ |
| $L_{\tilde X}$, $R_{\tilde X}$ | the left and the right multiplications, conjugate-linear and linear, $\mathbb{R}$-linear on $\mathbb{R}^8$ |
| $\Phi_{\mathbb{R}}=\operatorname{Re}H$ | the realification of the form $H$, of signature $(8,0)$ and Gram matrix $\mathrm{I}_8$ |
| $\tau(\tilde P,\tilde Q)=2\operatorname{Re}(P_0\overline{Q_0})$ | the trace form of the real regular representation, degenerate of rank two, radical $\mathrm{Vect}(\mathbb{B})$ |
| $c=\overline{\cdot}$ | the coefficientwise conjugation, an $\mathbb{R}$-linear algebra automorphism of the block, the Galois twist, inducing $\kappa$ on the centre |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_{+}$ | the quaternion and the Hermitian subspaces, real forms of real dimension four closed under the product |
| $\mathbb{R}\{e_0,e_1,e_2\}$ | a real subalgebra of odd real dimension three, with no complex counterpart |

## Further Reading

- *The Realification and the Effect of the Change of Scalars* (`articles_maths/the-realification-and-the-effect-of-the-change-of-scalars.md`), for the general construction, the two rules of the realification of a form and the table of the four effects.
- *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-algebraic-structures-over-the-biquaternion-c-space.md`), for the twelve structures and the columns of the table of the twelve, of which this article is the real reading of one row.
- *The Specificities of the Symmetric Plain Sesqualgebra* (`articles_maths/the-specificities-of-the-symmetric-plain-sesqualgebra.md`), for the Hermitian criterion and for the centrality shared with the symmetric quaternionic algebra.
- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`) and *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the Hermitian form $H$ and for its realified Gram matrix, signature $(8,0)$ and null set $\{0\}$.
- *The Multiplication Operators of the Symmetric Plain Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-plain-sesqualgebra.md`), for the conjugate-linearity of the left family, the traces, the composition law and the adjoint, of which this article is the real reading.
- *The Realification of the Symmetric Quaternionic Algebra* (`articles_maths/the-realification-of-the-symmetric-quaternionic-algebra.md`), the central sibling, on which the block coincides on the real quaternions.
