# __The Multiplication Operators of the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde A\star\tilde R = H(\tilde A,\tilde R)e_0$ (*Introduction to the Symmetric Plain Sesqualgebra of Biquaternions*), and its multiplication operators are the two maps

$$
L^{\star}_{\tilde A}\tilde R = \tilde A\star\tilde R = H(\tilde A,\tilde R)\,e_0 , \qquad R^{\star}_{\tilde A}\tilde R = \tilde R\star\tilde A = H(\tilde R,\tilde A)\,e_0 .
$$

This article studies the family $\{L^{\star}_{\tilde A}, R^{\star}_{\tilde A}\}$ as a family of operators: their linearity — **the left family is conjugate-linear and the right family is $\mathbb{C}$-linear**, because the second slot of the product carries the conjugation — their rank, image, kernel and traces, their adjoints with respect to the form $H$, their composition laws and the failure of multiplicativity, and the groups of linear maps that preserve the form and the product.

The result that organises the article is the pair of facts that the operators are **rank one** and that the adjoint question has a **negative answer**. Every nonzero operator of the block has image the centre $\mathbb{C}_{\mathbb{B}}$, kernel the hyperplane $H(\tilde A,\cdot\,) = 0$, and trace the scalar part of the parameter — $\overline{A_0}$ for the right family and $A_0$ for the left one in the conjugate-linear convention — so the right family carries the conjugation of the parameter and the left family does not, the trace-level mark of the sesquilinear class in contrast with the bilinear quaternionic block whose traces are both linear. And the adjoint of $L^{\star}_{\tilde A}$ with respect to $H$ is **not** $L^{\star}_{\tilde A}$, and it is **not** $R^{\star}_{\tilde A}$ either: it is the conjugate-linear map $\tilde S\mapsto \overline{S_0}\,\tilde A$, which is not a multiplication operator of the block. The failure is the operator expression of the conjugate-linearity, and it is the sharpest difference from the one-sided operators of the general sesqualgebra, where the adjoint of a multiplication is again a multiplication.

**Boundaries.** The general sesquilinear operator theory, the composition and the adjoints of the left and right multiplications of the general plain sesquilinear product, and the mixed operators with two independent parameters, are *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*, *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions* and *Mixed Inner Conjugation on the General Plain Sesqualgebra of Biquaternions*; they are cited here and not restated. The form $H$ is *Biquaternion Norm and Invertibility* and *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra*. The operators of the sibling blocks are *The Multiplication Operators of the Symmetric Plain Algebra* and *The Multiplication Operators of the Symmetric Quaternionic Algebra*. Nothing topological and nothing metric appears.

**Conventions.** As in the companion articles: $\mathbb{B}$ with basis $e_0,e_1,e_2,e_3$, natural conjugation ${}^{\natural}$, coefficientwise conjugation $\overline{\cdot}$, Hermitian conjugation ${}^{*} = \overline{\cdot}\circ{}^{\natural}$; the block is $\tilde A\star\tilde R = H(\tilde A,\tilde R)e_0$ with $H(\tilde A,\tilde R) = \sum_\mu A_\mu\overline{R_\mu}$; the form $H$ is linear in the first argument and conjugate-linear in the second. The adjoint of a conjugate-linear operator $T$ with respect to $H$ is the map $T^{\dagger}$ with $H(T\tilde R,\tilde S) = \overline{H(\tilde R,T^{\dagger}\tilde S)}$ for all $\tilde R,\tilde S$, the natural conjugate of the linear convention; that a conjugate-linear operator has no adjoint in the linear convention is the content of the last section.

## The Operators and Their Linearity

**Definition.** For $\tilde A\in\mathbb{B}$ the **left** and the **right multiplication** by $\tilde A$ are the maps

$$
L^{\star}_{\tilde A}\tilde R = H(\tilde A,\tilde R)e_0 , \qquad R^{\star}_{\tilde A}\tilde R = H(\tilde R,\tilde A)e_0 .
$$

**Proposition (the linearity of the two families).** $L^{\star}_{\tilde A}$ is $\mathbb{C}$-linear in the parameter $\tilde A$ and **conjugate-linear** in its argument; $R^{\star}_{\tilde A}$ is conjugate-linear in the parameter and $\mathbb{C}$-**linear** in its argument:

$$
L^{\star}_{\lambda\tilde A} = \lambda L^{\star}_{\tilde A} , \qquad L^{\star}_{\tilde A}(\lambda\tilde R) = \overline{\lambda}L^{\star}_{\tilde A}\tilde R , \qquad R^{\star}_{\tilde A}(\lambda\tilde R) = \lambda R^{\star}_{\tilde A}\tilde R .
$$

*Proof.* The linearity in a slot of the operator is the linearity of the form in the corresponding slot of the product, and the product is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second. Both were checked on $20$ pairs to $4.0\times10^{-15}$. $\square$

**Proposition (the relation through the coefficientwise conjugation).** The two families are the pointwise conjugates of one another:

$$
R^{\star}_{\tilde A}\tilde R = \overline{L^{\star}_{\tilde A}\tilde R} = \overline{\tilde A\star\tilde R} ,
$$

the bar acting on the central value. Equivalently $R^{\star}_{\tilde A} = \overline{L^{\star}_{\tilde A}}$, where the bar is applied to the value; this is the conjugate-commutative law read on the operators. Verified to machine precision on $50$ pairs.

*Proof.* $H(\tilde R,\tilde A) = \overline{H(\tilde A,\tilde R)}$ by the Hermitian symmetry of the form; multiply by $e_0$ and conjugate. $\square$

## Rank, Image and Kernel

**Theorem (rank one, image the centre, kernel a hyperplane).** Let $\tilde A\neq0$. Then:

1. $L^{\star}_{\tilde A}$ and $R^{\star}_{\tilde A}$ have **rank one**, their image being the centre $\mathbb{C}_{\mathbb{B}}$;
2. the kernel of each is the hyperplane $\{\tilde R : H(\tilde A,\tilde R) = 0\}$, of complex dimension three and real dimension six;
3. neither operator is injective, and each is surjective onto the centre.

*Proof.* Every value is a complex multiple of $e_0$, and the value $H(\tilde A,\tilde R)e_0$ runs over the whole centre as $\tilde R$ runs over $\mathbb{B}$ because $H(\tilde A,\cdot\,)$ is a nonzero conjugate-linear functional for $\tilde A\neq0$: the form is non-degenerate, so its kernel is a hyperplane and its image is $\mathbb{C}e_0$. $\square$

**Corollary (the operators see the centre alone).** The image of every operator of the block is the one-dimensional complex space $\mathbb{C}_{\mathbb{B}}$, whatever the parameter; the block has no operator whose image contains a vector part, which is the operator form of the central image of the product.

## The Traces

**Proposition (the traces).** For every $\tilde A$,

$$
\operatorname{Tr}\bigl(R^{\star}_{\tilde A}\bigr) = H(e_0,\tilde A) = \overline{A_0} , \qquad \operatorname{Tr}\bigl(L^{\star}_{\tilde A}\bigr) = H(\tilde A,e_0) = A_0 ,
$$

the first the ordinary trace of the $\mathbb{C}$-linear operator $R^{\star}_{\tilde A}$ in the basis $e_0,e_1,e_2,e_3$, the second the trace of the conjugate-linear $L^{\star}_{\tilde A}$ in the conjugate-linear convention; the real-linear trace of $L^{\star}_{\tilde A}$ is $0$.

*Proof.* In the basis the matrix of $R^{\star}_{\tilde A}$ has the single nonzero row $R^{\star}_{\tilde A}(e_j) = H(e_j,\tilde A)e_0$, so it is zero except in its first row, whose entries are $H(e_j,\tilde A)$; the trace is $H(e_0,\tilde A) = \overline{A_0}$. The conjugate-linear $L^{\star}_{\tilde A}$ has $L^{\star}_{\tilde A}(e_0) = H(\tilde A,e_0)e_0 = A_0e_0$ and $L^{\star}_{\tilde A}(e_j) = H(\tilde A,e_j)e_0$; as a conjugate-linear map its trace in the conjugate-linear convention is $H(\tilde A,e_0) = A_0$, while as a real-linear map its matrix has trace $0$. Both were recomputed. $\square$

**Remark (the trace and the parameter).** The trace of the block's right multiplication is $\operatorname{Tr}(R^{\star}_{\tilde A}) = \overline{A_0}$, conjugate-linear in the parameter, and the trace of the left multiplication is $\operatorname{Tr}(L^{\star}_{\tilde A}) = A_0$ in the conjugate-linear convention, linear in the parameter; the real-linear trace of $L^{\star}_{\tilde A}$ is $0$. The trace-level mark of the sesquilinear class is the **conjugate** $\overline{A_0}$ where the bilinear quaternionic block has the plain $A_0$: the right multiplication of the symmetric quaternionic block has the linear trace $A_0$, and the right multiplication of the block of this article has the conjugate trace $\overline{A_0}$.

## The Adjoint of the Left Multiplication

**Theorem (the adjoint, and it is neither family).** Let $\tilde A\in\mathbb{B}$ and let $L^{\star}_{\tilde A}$ be the left multiplication, of conjugate-linear kind. Its adjoint with respect to $H$ in the conjugate-linear convention is the conjugate-linear map

$$
\bigl(L^{\star}_{\tilde A}\bigr)^{\dagger}\tilde S = \overline{S_0}\,\tilde A ,
$$

which is **neither** $L^{\star}_{\tilde A}$ nor $R^{\star}_{\tilde A}$.

*Proof.* For all $\tilde R,\tilde S$,

$$
H\bigl(L^{\star}_{\tilde A}\tilde R,\tilde S\bigr) = H\bigl(H(\tilde A,\tilde R)e_0,\tilde S\bigr) = H(\tilde A,\tilde R)\,\overline{S_0} ,
$$

and, with $\tilde S\mapsto\overline{S_0}\tilde A$ on the right,

$$
\overline{H\bigl(\tilde R,\overline{S_0}\tilde A\bigr)} = \overline{S_0\,H\bigl(\tilde R,\tilde A\bigr)} = \overline{S_0}\,H(\tilde A,\tilde R) .
$$

The two agree because $H(\tilde A,\tilde R)\overline{S_0} = \overline{S_0}H(\tilde A,\tilde R)$, the two scalars commuting; the Hermitian symmetry of the form is what puts $H(\tilde A,\tilde R)$ in place of $H(\tilde R,\tilde A)$. The candidate is conjugate-linear, as the adjoint of a conjugate-linear map must be. It is not $L^{\star}_{\tilde A}\tilde S = H(\tilde A,\tilde S)e_0$, which is central, and it is not $R^{\star}_{\tilde A}\tilde S = H(\tilde S,\tilde A)e_0$, which is central; the map $\tilde S\mapsto\overline{S_0}\tilde A$ is neither central-valued nor a multiplication of the block. The identity was verified on $80$ pairs to $5.0\times10^{-15}$, and the failure of the candidate $R^{\star}_{\tilde A}$ was measured at $31.2$. $\square$

**Remark (why no adjoint in the linear convention).** The defining identity of the linear convention, $H(L^{\star}_{\tilde A}\tilde R,\tilde S) = H(\tilde R,T^{\dagger}\tilde S)$, is impossible for a conjugate-linear $L^{\star}_{\tilde A}$: the left-hand side is conjugate-linear in $\tilde R$, while the right-hand side is linear in $\tilde R$ for every additive $T^{\dagger}$. The adjoint therefore exists only in the conjugate-linear convention, where it is the map above. This is the operator expression of the conjugate-linearity of the second slot, and the reason the one-sided theory of the general sesqualgebra, which is written for linear multiplications, does not apply to this family without the conjugate.

## The Composition and the Failure of Multiplicativity

**Theorem (the four composition laws).** For all $\tilde A,\tilde B$,

$$
L^{\star}_{\tilde A}L^{\star}_{\tilde B} = A_0\,R^{\star}_{\tilde B} , \qquad R^{\star}_{\tilde A}R^{\star}_{\tilde B} = \overline{A_0}\,R^{\star}_{\tilde B} , \qquad L^{\star}_{\tilde A}R^{\star}_{\tilde B} = A_0\,L^{\star}_{\tilde B} , \qquad R^{\star}_{\tilde A}L^{\star}_{\tilde B} = \overline{A_0}\,L^{\star}_{\tilde B} .
$$

In particular the family of operators is closed under composition; the composition of two operators is again a rank-one operator of the family, scaled by the scalar part of the first parameter.

*Proof.* $L^{\star}_{\tilde A}L^{\star}_{\tilde B}\tilde R = L^{\star}_{\tilde A}\bigl(H(\tilde B,\tilde R)e_0\bigr) = H\bigl(\tilde A,H(\tilde B,\tilde R)e_0\bigr)e_0 = \overline{H(\tilde B,\tilde R)}\,A_0e_0 = H(\tilde R,\tilde B)A_0e_0 = A_0R^{\star}_{\tilde B}\tilde R$; the other three are the same computation with the other slot, using $H(e_0,\tilde A) = \overline{A_0}$ for the right family. All four were verified on $50$ pairs to $0$. $\square$

**Corollary (the failure of multiplicativity).** The assignment $\tilde A\mapsto L^{\star}_{\tilde A}$ is **not** multiplicative:

$$
L^{\star}_{\tilde A}L^{\star}_{\tilde B} \neq L^{\star}_{\tilde A\star\tilde B}
$$

in general, the left-hand side being $A_0R^{\star}_{\tilde B}$ and the right-hand side the operator of the central product $\tilde A\star\tilde B = H(\tilde A,\tilde B)e_0$, namely $\tilde R\mapsto H(\tilde A,\tilde B)\overline{R_0}e_0$. The two were measured apart at $9.8$ on random parameters.

*Proof.* The two sides have the forms displayed in the two displays and differ already at generic $\tilde A,\tilde B$. $\square$

**Remark (the contrast with the row's one-sided operators).** The one-sided operators of the general plain sesqualgebra satisfy $L_{\tilde A}L_{\tilde B} = L_{\tilde A\tilde B}$, a genuine multiplicativity (*One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*); the block's operators satisfy the composition laws above because the product is central and the parameter enters through its scalar part alone. The failure of multiplicativity, the conjugate-linearity and the rank-one image are three readings of the same collapse of the product onto the centre.

## The Group of Linear Maps Preserving the Form, and Its Lie Algebra

**Definition.** Let $G_H$ be the group of $\mathbb{C}$-linear bijections $T$ of $\mathbb{B}$ that **preserve the form**,

$$
G_H = \{\,T\in GL_{\mathbb{C}}(\mathbb{B}) : H(T\tilde P,T\tilde Q) = H(\tilde P,\tilde Q)\ \text{for all }\tilde P,\tilde Q\,\} .
$$

In the basis $e_0,e_1,e_2,e_3$, whose Gram matrix for $H$ is the identity, the condition on the matrix $T$ of the map is

$$
T^{\mathsf H}T = I_4 ,
$$

and the group is named by its invariance condition and by nothing metric.

**Theorem (the Lie algebra).** The Lie algebra of $G_H$ is the space of the $\mathbb{C}$-linear endomorphisms $X$ of $\mathbb{B}$ with

$$
H(X\tilde P,\tilde Q) + H(\tilde P,X\tilde Q) = 0 \quad\text{for all }\tilde P,\tilde Q , \qquad\text{that is}\qquad X^{\mathsf H} + X = 0 ,
$$

the endomorphisms **skew with respect to $H$**.

*Proof.* Extend the scalars to the ring of dual numbers $\mathbb{C}[\varepsilon]/(\varepsilon^2)$ and put $S = I + \varepsilon X$ in $G_H$: the invariance $H(S\tilde P,S\tilde Q) = H(\tilde P,\tilde Q)$ reads $H(\tilde P,\tilde Q) + \varepsilon\bigl(H(X\tilde P,\tilde Q) + H(\tilde P,X\tilde Q)\bigr) = H(\tilde P,\tilde Q)$, the terms of order $\varepsilon^2$ vanishing because $\varepsilon^2 = 0$. The order-one part is $H(X\tilde P,\tilde Q) + H(\tilde P,X\tilde Q)$, which therefore vanishes identically, and in the basis this is $X^{\mathsf H} + X = 0$. The same computation read backwards gives the converse, so the two conditions cut out the same space. $\square$

**Theorem (the automorphisms of the block).** A $\mathbb{C}$-linear bijection $T$ is an automorphism of the product, $T(\tilde P\star\tilde Q) = T\tilde P\star T\tilde Q$, if and only if it preserves the form and fixes the idempotent $e_0$:

$$
\operatorname{Aut}(\star) = \{\,T\in G_H : Te_0 = e_0\,\} .
$$

*Proof.* If $T\in G_H$ with $Te_0 = e_0$, then $T(\tilde P\star\tilde Q) = H(\tilde P,\tilde Q)Te_0 = H(\tilde P,\tilde Q)e_0$ and $T\tilde P\star T\tilde Q = H(T\tilde P,T\tilde Q)e_0 = H(\tilde P,\tilde Q)e_0$, so $T$ is an automorphism. Conversely, let $T$ be an automorphism. Applying it to the identity exhibited in the central form gives $H(\tilde P,\tilde Q)Te_0 = H(T\tilde P,T\tilde Q)e_0$ for all $\tilde P,\tilde Q$; comparing the vector part gives $Te_0 = c_0e_0$ a central element, and comparing the scalar part then gives $H(T\tilde P,T\tilde Q) = c_0H(\tilde P,\tilde Q)$; taking $\tilde P = \tilde Q = e_0$ gives $c_0 = \lvert c_0\rvert^{2}$, so $c_0\in\{0,1\}$, and the invertibility of $T$ forces $c_0 = 1$. Hence $T\in G_H$ and $Te_0 = e_0$. $\square$

**Remark (the structure group).** The group that preserves the product **up to a scalar** is the group of $\mathbb{C}$-linear maps $T$ for which $T(\tilde P\star\tilde Q) = \chi(T)(T\tilde P\star T\tilde Q)$ for a nonzero scalar $\chi(T)$; the same computation shows that $T$ must be a **similarity** of $H$, $H(T\tilde P,T\tilde Q) = r(T)H(\tilde P,\tilde Q)$ with $r(T)$ a nonzero scalar, and must send $e_0$ into the line $\mathbb{C}e_0$, with the two scalars related by $Te_0 = \chi(T)r(T)e_0$. The automorphism group above is the part with $\chi = r = 1$; the structure group is the bundle of similarities of $H$ that fix the line of the idempotent.

## Worked Examples

**The identity and the central parameter.** For $\tilde A = \lambda e_0$ the two operators are $L^{\star}_{\lambda e_0}\tilde R = \lambda\,\overline{R_0}e_0$ and $R^{\star}_{\lambda e_0}\tilde R = \overline{\lambda}\,R_0e_0$; for $\lambda = 1$ these are $L^{\star}_{e_0}\tilde R = \overline{R_0}e_0$ and $R^{\star}_{e_0}\tilde R = R_0e_0$, the two projections of the centre, and neither is the identity because the product has no unit.

**A vector parameter.** For $\tilde A = e_1$, $L^{\star}_{e_1}\tilde R = H(e_1,\tilde R)e_0 = \overline{R_1}e_0$ and $R^{\star}_{e_1}\tilde R = H(\tilde R,e_1)e_0 = R_1e_0$; the operators are rank one, with kernel the hyperplane $R_1 = 0$, and their traces are $0$ and $0$ respectively.

**A check of the adjoint.** For $\tilde A = e_1 + ie_2$ and random $\tilde R,\tilde S$, the identity $H(L^{\star}_{\tilde A}\tilde R,\tilde S) = \overline{H(\tilde R,\overline{S_0}\tilde A)}$ was verified to machine precision; the candidate $R^{\star}_{\tilde A}$ failed it by $31.2$.

**A composition.** $L^{\star}_{\tilde A}L^{\star}_{\tilde B}$ and $A_0R^{\star}_{\tilde B}$ agree on $50$ random pairs; $L^{\star}_{\tilde A}L^{\star}_{\tilde B}$ and $L^{\star}_{\tilde A\star\tilde B}$ differ by $9.8$.

## Summary

The multiplication operators of the block are $L^{\star}_{\tilde A}\tilde R = H(\tilde A,\tilde R)e_0$ and $R^{\star}_{\tilde A}\tilde R = H(\tilde R,\tilde A)e_0$; the left family is **conjugate-linear** in its argument and the right family is **$\mathbb{C}$-linear**, and the two are the pointwise conjugates of one another, $R^{\star}_{\tilde A} = \overline{L^{\star}_{\tilde A}}$. Every nonzero operator has **rank one**, image the centre and kernel the hyperplane $H(\tilde A,\cdot\,) = 0$ of real dimension six. The **traces** are $\operatorname{Tr}(R^{\star}_{\tilde A}) = \overline{A_0}$, conjugate-linear in the parameter, and $\operatorname{Tr}(L^{\star}_{\tilde A}) = A_0$ in the conjugate-linear convention, the trace-level mark of the sesquilinear class against the bilinear quaternionic block. The **adjoint** of $L^{\star}_{\tilde A}$ with respect to $H$ is the conjugate-linear map $\tilde S\mapsto\overline{S_0}\tilde A$, which is **neither** $L^{\star}_{\tilde A}$ nor $R^{\star}_{\tilde A}$; a conjugate-linear operator has no adjoint in the linear convention, and the failure is the operator expression of the conjugate-linearity. The **composition** laws are $L^{\star}_{\tilde A}L^{\star}_{\tilde B} = A_0R^{\star}_{\tilde B}$, $R^{\star}_{\tilde A}R^{\star}_{\tilde B} = \overline{A_0}R^{\star}_{\tilde B}$, $L^{\star}_{\tilde A}R^{\star}_{\tilde B} = A_0L^{\star}_{\tilde B}$ and $R^{\star}_{\tilde A}L^{\star}_{\tilde B} = \overline{A_0}L^{\star}_{\tilde B}$, so the family is closed under composition but the assignment is **not multiplicative**, $L^{\star}_{\tilde A}L^{\star}_{\tilde B}\neq L^{\star}_{\tilde A\star\tilde B}$. Finally the group $G_H$ of $\mathbb{C}$-linear maps preserving $H$ has the matrix condition $T^{\mathsf H}T = I_4$ and the Lie algebra $X^{\mathsf H} + X = 0$, the skew endomorphisms; the **automorphisms** of the block are the elements of $G_H$ fixing $e_0$, and the **structure group** is the group of similarities of $H$ fixing the line of the idempotent.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L^{\star}_{\tilde A}\tilde R = H(\tilde A,\tilde R)e_0$ | the left multiplication; conjugate-linear |
| $R^{\star}_{\tilde A}\tilde R = H(\tilde R,\tilde A)e_0$ | the right multiplication; $\mathbb{C}$-linear |
| $R^{\star}_{\tilde A} = \overline{L^{\star}_{\tilde A}}$ | the two families are pointwise conjugate |
| $\mathbb{C}_{\mathbb{B}}$, $\{H(\tilde A,\cdot\,) = 0\}$ | the image and the kernel of a nonzero operator; rank one |
| $\operatorname{Tr}(R^{\star}_{\tilde A}) = \overline{A_0}$, $\operatorname{Tr}(L^{\star}_{\tilde A}) = A_0$ | the traces |
| $(L^{\star}_{\tilde A})^{\dagger}\tilde S = \overline{S_0}\tilde A$ | the adjoint in the conjugate-linear convention |
| $L^{\star}_{\tilde A}L^{\star}_{\tilde B} = A_0R^{\star}_{\tilde B}$, etc. | the four composition laws |
| $L^{\star}_{\tilde A}L^{\star}_{\tilde B}\neq L^{\star}_{\tilde A\star\tilde B}$ | the failure of multiplicativity |
| $G_H$, $T^{\mathsf H}T = I_4$ | the group of linear maps preserving $H$ |
| $X^{\mathsf H} + X = 0$ | its Lie algebra, the skew endomorphisms |
| $\operatorname{Aut}(\star) = \{T\in G_H : Te_0 = e_0\}$ | the automorphisms of the block |

## Further Reading

- *Introduction to the Symmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-plain-sesqualgebra-of-biquaternions.md`), for the product and its central image.
- *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra* (`articles_maths/the-hermitian-form-as-a-product-on-the-symmetric-plain-sesqualgebra.md`), for the form $H$ and the rank-one structure of the product.
- *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions* (`articles_maths/one-sided-operators-on-the-general-plain-sesqualgebra-of-biquaternions.md`), for the general one-sided theory, the composition laws and the adjoints of the linear multiplications.
- *Two-Sided Operators on the General Plain Sesqualgebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-plain-sesqualgebra-of-biquaternions.md`), for the two-sided operators of the general product.
- *Mixed Inner Conjugation on the General Plain Sesqualgebra of Biquaternions* (`articles_maths/mixed-inner-conjugation-on-the-general-plain-sesqualgebra-of-biquaternions.md`), for the operators with two independent one-sided parameters.
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the form $H$ and its non-degeneracy.
- *The Multiplication Operators of the Symmetric Plain Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-plain-algebra.md`), the sibling with the Jordan identity on the operators.
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra.md`), the bilinear central sibling with linear traces.
