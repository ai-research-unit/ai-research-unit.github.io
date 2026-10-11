# __The Realification of the Symmetric Quaternionic Sesqualgebra__

## Introduction

The Symmetric Quaternionic Sesqualgebra is one of the twelve algebraic structures that the biquaternion space of $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ carries, the structure carried by the block
$$
\tilde P\star\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural}\bigr)
=\bigl[P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q})\bigr]-P_0\overline{\mathbf Q}-\overline{Q_0}\mathbf P,
$$
which over $\mathbb{C}$ is the symmetric quaternionic sesquilinear structure $\mathrm{SQS}$ of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. Read over $\mathbb{R}$, the same product on the same set is an $\mathbb{R}$-algebra on the eight-dimensional real space $\mathbb{R}^8$, and this article owns that real reading.

The general construction is not repeated here. The realification of a vector space, of a linear map and of a form, the doubling of the dimension, the complex structure $J$ and the table of the four effects are *The Realification and the Effect of the Change of Scalars*; This article gives what is specific to the block: its real bilinear reading, the law of its second slot over the centre, the realification of the Krein form it carries with the signature that follows, its real operators, and the three objects that exist only in the real reading.

## The Product Read over $\mathbb{R}$

The product is symmetric quaternionic sesquilinear over $\mathbb{C}$ and $\mathbb{R}$-bilinear over $\mathbb{R}$, by §*The Effect on the Twelve Algebraic Structures* of *The Realification and the Effect of the Change of Scalars*; it is therefore an **$\mathbb{R}$-algebra** on $\mathbb{R}^8$ in the broad sense, the sense of a module with a bilinear multiplication.

Every ring-theoretic property is the same in the two readings, by the dictionary of the same article: a condition written with the addition, the product, $e_0$ and quantification over the elements is a statement about the **ring** and does not move when the scalars are restricted to $\mathbb{R}$ — the product is unchanged, so every identity of the ring, with its fixed element maps, holds in both readings. For the block these are: conjugate-commutativity, $\tilde P\star\tilde Q=\kappa(\tilde Q\star\tilde P)$ with $\kappa$ the coefficientwise conjugation, an identity of the ring and not of the field; the failure of associativity, read at the triple $(e_0,e_0,e_1)$, where the two sides are $-e_1$ and $e_1$; the failure of the Jordan identity at $x=y=e_1$, whose quartic sides $(x^{2}\star x)\star x$ and $x^{2}\star(x\star x)$ are $-e_0$ and $e_0$; and the absence of a unit on either side. What moves is every notion that names the field: the space, of complex dimension four and real dimension eight; the linear structure, in which the conjugate-linear operators appear; and the forms.

The block's values are not confined to the centre, unlike those of the sibling $\mathrm{SPS}$. Its scalar part is the form $K(\tilde P,\tilde Q)$ and its vector part is the mixed term $-P_0\overline{\mathbf Q}-\overline{Q_0}\mathbf P$, which does not vanish for a general pair: the values are not confined to any subspace of the remarkable subspaces, and their real span is the whole $\mathbb{R}^8$, as *Remarkable Subspaces under the Symmetric Quaternionic Sesqualgebra of Biquaternions* computes.

## The Second Slot and the Centre

Over $\mathbb{C}$ the block is a **sesqualgebra over $(\mathbb{C},\varsigma)$**, linear in the first slot and conjugate-linear in the second, the involution $\varsigma={}^{*}$ acting on the centre as the Galois conjugation $i\mapsto-i$; it is not an algebra over $\mathbb{C}$. Read over $\mathbb{R}$ the involution disappears — the only automorphism of $\mathbb{R}$ is the identity, and a sesquilinear law with the identity involution is a bilinear law — so the block is an $\mathbb{R}$-algebra, and the $A$/$S$ distinction migrates from the field to the centre $\mathbb{C}_{\mathbb{B}}$, where it is the criterion
$$
LJ=\pm JL
$$
for the left multiplications by central elements. For the block the sign is $-$: the second slot is $\mathbb{C}_{\mathbb{B}}$-conjugate-linear, so every left multiplication anticommutes with the complex structure,
$$
L^{\star}_{\tilde A}J=-JL^{\star}_{\tilde A},
\qquad
R^{\star}_{\tilde A}J=+JR^{\star}_{\tilde A},
$$
and in the real basis the two families have the block shapes
$$
\begin{pmatrix}A&B\\ B&-A\end{pmatrix}
\qquad\text{and}\qquad
\begin{pmatrix}A&-B\\ B&A\end{pmatrix},
$$
the first the shape of the conjugate-linear maps and the second the shape of the $\mathbb{C}_{\mathbb{B}}$-linear ones. The composite $L^{\star}_{\tilde A}L^{\star}_{\tilde B}$ is therefore $\mathbb{C}_{\mathbb{B}}$-linear while a single $L^{\star}_{\tilde A}$ has no $\mathbb{C}_{\mathbb{B}}$-linear reading, which is the parity of *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*.

## The Realified Form

The block carries the Krein form
$$
K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\star\tilde Q)=P_0\overline{Q_0}-(\mathbf P,\overline{\mathbf Q}),
$$
Hermitian of complex inertia $(1,3)$. The realification of a Hermitian form doubles its inertia, by §*The Realification of a Form* of *The Realification and the Effect of the Change of Scalars*, so the form $\Phi_{\mathbb{R}}=\operatorname{Re}K$ is the real symmetric bilinear form on $\mathbb{R}^8$ of signature
$$
(2,6),\qquad\text{Gram matrix }\operatorname{diag}(1,-1,-1,-1,1,-1,-1,-1),
$$
and the complex structure preserves it, $\Phi_{\mathbb{R}}(JP,JQ)=+\Phi_{\mathbb{R}}(P,Q)$. The instance is the row general quaternionic sesquilinear, the Krein $K$ of the table of *The Realification of the Four Forms*, §*The Four Gram Matrices*.

The compatibility of $K$ with the left multiplications realifies with the form. Over $\mathbb{C}$ it is
$$
K\bigl(L^{\star}_{\tilde A}\tilde X,\tilde Y\bigr)=\overline{K\bigl(\tilde X,L^{\star}_{\tilde A^{\natural}}\tilde Y\bigr)},
$$
a relation with a conjugation on the right. Taking real parts the conjugation disappears and the identity reads
$$
\Phi_{\mathbb{R}}\bigl(L^{\star}_{\tilde A}\tilde X,\tilde Y\bigr)=\Phi_{\mathbb{R}}\bigl(\tilde X,L^{\star}_{\tilde A^{\natural}}\tilde Y\bigr),
$$
so $L^{\star}_{\tilde A^{\natural}}$ is the **$\Phi_{\mathbb{R}}$-adjoint** of $L^{\star}_{\tilde A}$ in the ordinary sense of a real symmetric form: the adjoint relation survives the passage and loses its conjugation, and the block's operators are adjoint with respect to the indefinite form of signature $(2,6)$. The relation over $\mathbb{C}$ is the compatibility theorem of *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*, quoted here and specialising the theorem of *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*.

## The Real Operators

The left and the right multiplications,
$$
L^{\star}_{\tilde A}(\tilde X)=\tilde A\star\tilde X,\qquad R^{\star}_{\tilde A}(\tilde X)=\tilde X\star\tilde A,
$$
are $\mathbb{R}$-linear endomorphisms of $\mathbb{R}^8$, by §*The Realification of a Linear Map* of *The Realification and the Effect of the Change of Scalars*, related by $L^{\star}_{\tilde A}\tilde X=\overline{R^{\star}_{\tilde A}\tilde X}$. Their ranks are $0$ at $\tilde A=0$, $4$ for $\tilde A$ in the vector subspace, $8$ when $A_0\neq0$ and $N(\tilde A)\neq0$, and $6$ when $A_0\neq0$ and $N(\tilde A)=0$; their traces are $0$ for the left family and $-4\operatorname{Re}(A_0)$ for the right; and the image of a left multiplication by a vector element is a four-dimensional real subspace that is not one of the remarkable subspaces. These are the numbers of *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*, read in the real basis;

## What Is Specific to the Real Reading

**The trace form.** The composite of two left multiplications is $\mathbb{C}_{\mathbb{B}}$-linear, so
$$
\tau(\tilde P,\tilde Q)=\operatorname{Tr}_{\mathbb{R}}\bigl(L^{\star}_{\tilde P}L^{\star}_{\tilde Q}\bigr)
$$
is a real symmetric bilinear form on $\mathbb{R}^8$, of signature
$$
(8,0),\qquad\text{Gram matrix }\operatorname{diag}(8,4,4,4,8,4,4,4)
$$
on $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$. The trace of a $\mathbb{C}$-linear map is twice the real part of its complex trace, so $\tau=2\operatorname{Re}\Theta$ with
$$
\Theta(\tilde P,\tilde Q)=\operatorname{Tr}_{\mathbb{C}}\bigl(L^{\star}_{\tilde P}L^{\star}_{\tilde Q}\bigr)=4P_0\overline{Q_0}+2\sum_{k=1}^{3}P_k\overline{Q_k},
$$
a **positive definite** Hermitian form of complex inertia $(4,0)$. This is the trace form of the left regular representation of the block, the analogue of $\operatorname{Tr}_{\mathbb{R}}(L_{\tilde P}L_{\tilde Q})$ for the parent; The block therefore carries two real forms over $\mathbb{R}$, of opposite kinds: the indefinite $\Phi_{\mathbb{R}}$, of signature $(2,6)$, attached to the product, and the definite $\tau$, of signature $(8,0)$, attached to its left multiplications; the definite one is no multiple of the indefinite one.

**The Galois twist.** The four conjugations of the ring — the identity, the natural conjugation ${}^{\natural}$, the coefficientwise conjugation $\kappa$ and the Hermitian star ${}^{*}=\kappa\circ{}^{\natural}$ — are $\mathbb{R}$-linear and are automorphisms of the block,
$$
T(\tilde P\star\tilde Q)=T(\tilde P)\star T(\tilde Q),
$$
so the group of $\mathbb{R}$-algebra automorphisms of the block contains the Klein four group $\{\mathrm{id},{}^{\natural},\kappa,{}^{*}\}$. Of the four, $\mathrm{id}$ and ${}^{\natural}$ are $\mathbb{C}_{\mathbb{B}}$-linear while $\kappa$ and ${}^{*}$ are conjugate-linear, the Galois twist of the centre: the real reading acquires conjugate-linear symmetries that are not $\mathbb{C}_{\mathbb{B}}$-linear. The four are the group recorded as the structure group of the block in *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra*; whether they exhaust the automorphism group is left undecided there, and no attempt is made here to extend it.

**The real subalgebras.** Over $\mathbb{C}$ a subalgebra is a complex subspace, of even real dimension; over $\mathbb{R}$ there are others. The real quaternion subspace $\mathbb{H}_{\mathbb{B}}=\mathbb{R}e_0+\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$ and the Hermitian subspace $\mathbb{M}_{+}=\mathbb{R}e_0+\mathbb{R}ie_1+\mathbb{R}ie_2+\mathbb{R}ie_3$ are four-dimensional real subalgebras of the block — two of the three closed subspaces of *Remarkable Subspaces under the Symmetric Quaternionic Sesqualgebra of Biquaternions* — and neither is a complex subspace: the complex span of each is the whole block. The real line $\mathbb{R}e_0$ is a one-dimensional unital subalgebra inside the centre $\mathbb{C}e_0$, and the complex reading, whose subalgebras have even real dimension, has no subalgebra of dimension one.

## Summary

The Symmetric Quaternionic Sesqualgebra read over $\mathbb{R}$ is the same product on the same elements, an $\mathbb{R}$-algebra on $\mathbb{R}^8$ in which conjugate-commutativity holds, associativity fails, the Jordan identity fails and there is no unit; every ring-theoretic property is unchanged. Its second slot is $\mathbb{C}_{\mathbb{B}}$-conjugate-linear, so its left multiplications anticommute with $J$ and its right multiplications commute with it. It carries the Krein form $K$, whose realification $\Phi_{\mathbb{R}}$ has signature $(2,6)$ and whose adjoint relation realifies to the ordinary adjointness of $L^{\star}_{\tilde A}$ and $L^{\star}_{\tilde A^{\natural}}$. Three objects exist only in the real reading: the definite trace form $\tau$ of signature $(8,0)$, the conjugate-linear Galois-twisted automorphisms, and the real subalgebras that are not complex subspaces.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\star\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural}\bigr)$ | the product of the block |
| $\mathbb{R}^8$ | the realification of $\mathbb{B}$, the eight real basis elements $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre, the field of scalars carried by the ring, of real dimension two |
| $N(\tilde A)=A_0^{2}+A_1^{2}+A_2^{2}+A_3^{2}$ | the coefficient norm that thresholds the ranks $4$, $6$ and $8$ |
| $J$ | the complex structure, multiplication by $i$, of square $-1$ |
| $L^{\star}_{\tilde A}$, $R^{\star}_{\tilde A}$ | the left and the right multiplications, $\mathbb{R}$-linear on $\mathbb{R}^8$ |
| $\Phi_{\mathbb{R}}=\operatorname{Re}K$ | the realification of the Krein form, of signature $(2,6)$ |
| $\tau(\tilde P,\tilde Q)=\operatorname{Tr}_{\mathbb{R}}\bigl(L^{\star}_{\tilde P}L^{\star}_{\tilde Q}\bigr)$ | the trace form of the left regular representation, of signature $(8,0)$ |
| $\Theta(\tilde P,\tilde Q)=\operatorname{Tr}_{\mathbb{C}}\bigl(L^{\star}_{\tilde P}L^{\star}_{\tilde Q}\bigr)$ | the positive definite Hermitian form with $\tau=2\operatorname{Re}\Theta$ |
| ${}^{\natural}$, $\kappa$, ${}^{*}$ | the natural, the coefficientwise and the Hermitian conjugation, all $\mathbb{R}$-linear |

## Further Reading

- *The Realification and the Effect of the Change of Scalars* (`articles_maths/the-realification-and-the-effect-of-the-change-of-scalars.md`), for the general construction, the two rules of the realification of a form, the table of the four effects and the change of scalars from $\mathbb{C}$ to $\mathbb{R}$.
- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the four Gram matrices and signatures, of which the Krein row $(2,6)$ is the form of this article.
- *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-krein-form-as-a-product-on-the-symmetric-quaternionic-sesqualgebra.md`), for the form $K$, its Gram matrix, its inertia $(1,3)$ and the adjoint relation $K(L^{\star}_{\tilde A}\tilde X,\tilde Y)=\overline{K(\tilde X,L^{\star}_{\tilde A^{\natural}}\tilde Y)}$ read here on the real parts.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product, its scalar–vector form, its diagonal and the placement of the block among the twelve.
- *The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-sesqualgebra.md`), for the real operators of the block, their ranks, their traces and the $K$-adjointness that realifies here.
- *Remarkable Subspaces under the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the closed subspaces, the real quaternion and Hermitian subalgebras and the span of the values.
- *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-12-algebraic-structures-over-the-biquaternion-c-space.md`) and *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`), for the twelve structures and the four forms of which this article is the real reading.
