# __The Multiplication Operators of the Symmetric Plain Sesqualgebra__

## Introduction

The symmetric plain sesqualgebra is the operation $\tilde Q_3\star\tilde{Q}_2 = \langle\tilde Q_3,\tilde{Q}_2\rangle_{*}e_t$ (*Introduction to the Symmetric Plain Sesqualgebra*), and its multiplication operators are the two maps

$$
L^{\star}_{\tilde Q_3}\tilde{Q}_2 = \tilde Q_3\star\tilde{Q}_2 = \langle\tilde Q_3,\tilde{Q}_2\rangle_{*}\,e_t , \qquad R^{\star}_{\tilde Q_3}\tilde{Q}_2 = \tilde{Q}_2\star\tilde Q_3 = \langle\tilde{Q}_2,\tilde Q_3\rangle_{*}\,e_t .
$$

This article studies the family $\{L^{\star}_{\tilde Q_3}, R^{\star}_{\tilde Q_3}\}$ as a family of operators: their linearity — **the left family is conjugate-linear and the right family is $\mathbb{C}$-linear**, because the second slot of the product carries the conjugation — their rank, image, kernel and traces, their adjoints with respect to the form $H$, their composition laws and the failure of multiplicativity, and the groups of linear maps that preserve the form and the product.

The result that organises the article is the pair of facts that the operators are **rank one** and that the adjoint question has a **negative answer**. Every nonzero operator of the block has image the centre $\mathbb{C}_{\mathbb{B}}$, kernel the hyperplane $H(\tilde Q_3,\cdot\,) = 0$, and trace the scalar part of the parameter — $\overline{Q_{3t}}$ for the right family and $Q_{3t}$ for the left one in the conjugate-linear convention — so the right family carries the conjugation of the parameter and the left family does not, the trace-level mark of the sesquilinear class in contrast with the bilinear quaternionic block whose traces are both linear. And the adjoint of $L^{\star}_{\tilde Q_3}$ with respect to $H$ is **not** $L^{\star}_{\tilde Q_3}$, and it is **not** $R^{\star}_{\tilde Q_3}$ either: it is the conjugate-linear map $\tilde S\mapsto \overline{S_t}\,\tilde Q_3$, which is not a multiplication operator of the block. The failure is the operator expression of the conjugate-linearity, and it is the sharpest difference from the one-sided operators of the general sesqualgebra, where the adjoint of a multiplication is again a multiplication.

**Boundaries.** The general sesquilinear operator theory, the composition and the adjoints of the left and right multiplications of the general plain sesquilinear product, and the mixed operators with two independent parameters, are *One-Sided Operators on the General Plain Sesqualgebra*, *Two-Sided Operators on the General Plain Sesqualgebra* and *Mixed Inner Conjugation on the General Plain Sesqualgebra*; they are cited here and not restated. The form $H$ is *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* and *The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra*. The operators of the sibling blocks are *The Multiplication Operators of the Symmetric Plain Algebra* and *The Multiplication Operators of the Symmetric Quaternionic Algebra*. Nothing topological and nothing metric appears.

**Conventions.** As in the companion articles: $\mathbb{B}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, natural conjugation ${}^{\natural}$, coefficientwise conjugation $\overline{\cdot}$, Hermitian conjugation ${}^{*} = \overline{\cdot}\circ{}^{\natural}$; the block is $\tilde Q_3\star\tilde{Q}_2 = \langle\tilde Q_3,\tilde{Q}_2\rangle_{*}e_t$ with $\langle\tilde Q_3,\tilde{Q}_2\rangle_{*} = \sum_\mu Q_{3\mu}\overline{R_\mu}$; the form $H$ is linear in the first argument and conjugate-linear in the second. The adjoint of a conjugate-linear operator $T$ with respect to $H$ is the map $T^{\dagger}$ with $\langle T\tilde{Q}_2,\tilde S\rangle_{*} = \overline{\langle\tilde{Q}_2,T^{\dagger}\tilde S\rangle_{*}}$ for all $\tilde{Q}_2,\tilde S$, the natural conjugate of the linear convention; that a conjugate-linear operator has no adjoint in the linear convention is the content of the last section.

## The Operators and Their Linearity

**Definition.** For $\tilde Q_3\in\mathbb{B}$ the **left** and the **right multiplication** by $\tilde Q_3$ are the maps

$$
L^{\star}_{\tilde Q_3}\tilde{Q}_2 = \langle\tilde Q_3,\tilde{Q}_2\rangle_{*}e_t , \qquad R^{\star}_{\tilde Q_3}\tilde{Q}_2 = \langle\tilde{Q}_2,\tilde Q_3\rangle_{*}e_t .
$$

**Proposition (the linearity of the two families).** $L^{\star}_{\tilde Q_3}$ is $\mathbb{C}$-linear in the parameter $\tilde Q_3$ and **conjugate-linear** in its argument; $R^{\star}_{\tilde Q_3}$ is conjugate-linear in the parameter and $\mathbb{C}$-**linear** in its argument:

$$
L^{\star}_{\lambda\tilde Q_3} = \lambda L^{\star}_{\tilde Q_3} , \qquad L^{\star}_{\tilde Q_3}(\lambda\tilde{Q}_2) = \overline{\lambda}L^{\star}_{\tilde Q_3}\tilde{Q}_2 , \qquad R^{\star}_{\tilde Q_3}(\lambda\tilde{Q}_2) = \lambda R^{\star}_{\tilde Q_3}\tilde{Q}_2 .
$$

*Proof.* The linearity in a slot of the operator is the linearity of the form in the corresponding slot of the product, and the product is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second.

**Proposition (the relation through the coefficientwise conjugation).** The two families are the pointwise conjugates of one another:

$$
R^{\star}_{\tilde Q_3}\tilde{Q}_2 = \overline{L^{\star}_{\tilde Q_3}\tilde{Q}_2} = \overline{\tilde Q_3\star\tilde{Q}_2} ,
$$

the bar acting on the central value. Equivalently $R^{\star}_{\tilde Q_3} = \overline{L^{\star}_{\tilde Q_3}}$, where the bar is applied to the value; this is the conjugate-commutative law read on the operators.

*Proof.* $\langle\tilde{Q}_2,\tilde Q_3\rangle_{*} = \overline{\langle\tilde Q_3,\tilde{Q}_2\rangle_{*}}$ by the Hermitian symmetry of the form; multiply by $e_t$ and conjugate.

## Rank, Image and Kernel

**Theorem (rank one, image the centre, kernel a hyperplane).** Let $\tilde Q_3\neq0$. Then:

1. $L^{\star}_{\tilde Q_3}$ and $R^{\star}_{\tilde Q_3}$ have **rank one**, their image being the centre $\mathbb{C}_{\mathbb{B}}$;
2. the kernel of each is the hyperplane $\{\tilde{Q}_2 : \langle\tilde Q_3,\tilde{Q}_2\rangle_{*} = 0\}$, of complex dimension three and real dimension six;
3. neither operator is injective, and each is surjective onto the centre.

*Proof.* Every value is a complex multiple of $e_t$, and the value $\langle\tilde Q_3,\tilde{Q}_2\rangle_{*}e_t$ runs over the whole centre as $\tilde{Q}_2$ runs over $\mathbb{B}$ because $H(\tilde Q_3,\cdot\,)$ is a nonzero conjugate-linear functional for $\tilde Q_3\neq0$: the form is non-degenerate, so its kernel is a hyperplane and its image is $\mathbb{C}e_t$.

**Corollary (the operators see the centre alone).** The image of every operator of the block is the one-dimensional complex space $\mathbb{C}_{\mathbb{B}}$, whatever the parameter; the block has no operator whose image contains a vector part, which is the operator form of the central image of the product.

## The Traces

**Proposition (the traces).** For every $\tilde Q_3$,

$$
\operatorname{Tr}\bigl(R^{\star}_{\tilde Q_3}\bigr) = \langle e_t,\tilde Q_3\rangle_{*} = \overline{Q_{3t}} , \qquad \operatorname{Tr}\bigl(L^{\star}_{\tilde Q_3}\bigr) = \langle\tilde Q_3,e_t\rangle_{*} = Q_{3t} ,
$$

the first the ordinary trace of the $\mathbb{C}$-linear operator $R^{\star}_{\tilde Q_3}$ in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, the second the trace of the conjugate-linear $L^{\star}_{\tilde Q_3}$ in the conjugate-linear convention; the real-linear trace of $L^{\star}_{\tilde Q_3}$ is $0$.

*Proof.* In the basis the matrix of $R^{\star}_{\tilde Q_3}$ has the single nonzero row $R^{\star}_{\tilde Q_3}(e_\mu) = \langle e_\mu,\tilde Q_3\rangle_{*}e_t$, so it is zero except in its first row, whose entries are $\langle e_\mu,\tilde Q_3\rangle_{*}$; the trace is $\langle e_t,\tilde Q_3\rangle_{*} = \overline{Q_{3t}}$. The conjugate-linear $L^{\star}_{\tilde Q_3}$ has $L^{\star}_{\tilde Q_3}(e_t) = \langle\tilde Q_3,e_t\rangle_{*}e_t = Q_{3t}e_t$ and $L^{\star}_{\tilde Q_3}(e_\mu) = \langle\tilde Q_3,e_\mu\rangle_{*}e_t$; as a conjugate-linear map its trace in the conjugate-linear convention is $\langle\tilde Q_3,e_t\rangle_{*} = Q_{3t}$, while as a real-linear map its matrix has trace $0$.

**Remark (the trace and the parameter).** The trace of the block's right multiplication is $\operatorname{Tr}(R^{\star}_{\tilde Q_3}) = \overline{Q_{3t}}$, conjugate-linear in the parameter, and the trace of the left multiplication is $\operatorname{Tr}(L^{\star}_{\tilde Q_3}) = Q_{3t}$ in the conjugate-linear convention, linear in the parameter; the real-linear trace of $L^{\star}_{\tilde Q_3}$ is $0$. The trace-level mark of the sesquilinear class is the **conjugate** $\overline{Q_{3t}}$ where the bilinear quaternionic block has the plain $Q_{3t}$: the right multiplication of the symmetric quaternionic block has the linear trace $Q_{3t}$, and the right multiplication of the block of this article has the conjugate trace $\overline{Q_{3t}}$.

## The Adjoint of the Left Multiplication

**Theorem (the adjoint, and it is neither family).** Let $\tilde Q_3\in\mathbb{B}$ and let $L^{\star}_{\tilde Q_3}$ be the left multiplication, of conjugate-linear kind. Its adjoint with respect to $H$ in the conjugate-linear convention is the conjugate-linear map

$$
\bigl(L^{\star}_{\tilde Q_3}\bigr)^{\dagger}\tilde S = \overline{S_t}\,\tilde Q_3 ,
$$

which is **neither** $L^{\star}_{\tilde Q_3}$ nor $R^{\star}_{\tilde Q_3}$.

*Proof.* For all $\tilde{Q}_2,\tilde S$,

$$
H\bigl(L^{\star}_{\tilde Q_3}\tilde{Q}_2,\tilde S\bigr) = H\bigl(\langle\tilde Q_3,\tilde{Q}_2\rangle_{*}e_t,\tilde S\bigr) = \langle\tilde Q_3,\tilde{Q}_2\rangle_{*}\,\overline{S_t} ,
$$

and, with $\tilde S\mapsto\overline{S_t}\tilde Q_3$ on the right,

$$
\overline{H\bigl(\tilde{Q}_2,\overline{S_t}\tilde Q_3\bigr)} = \overline{S_t\,H\bigl(\tilde{Q}_2,\tilde Q_3\bigr)} = \overline{S_t}\,\langle\tilde Q_3,\tilde{Q}_2\rangle_{*} .
$$

The two agree because $\langle\tilde Q_3,\tilde{Q}_2\rangle_{*}\overline{S_t} = \overline{S_t}\langle\tilde Q_3,\tilde{Q}_2\rangle_{*}$, the two scalars commuting; the Hermitian symmetry of the form is what puts $\langle\tilde Q_3,\tilde{Q}_2\rangle_{*}$ in place of $\langle\tilde{Q}_2,\tilde Q_3\rangle_{*}$. The candidate is conjugate-linear, as the adjoint of a conjugate-linear map must be. It is not $L^{\star}_{\tilde Q_3}\tilde S = \langle\tilde Q_3,\tilde S\rangle_{*}e_t$, which is central, and it is not $R^{\star}_{\tilde Q_3}\tilde S = \langle\tilde S,\tilde Q_3\rangle_{*}e_t$, which is central; the map $\tilde S\mapsto\overline{S_t}\tilde Q_3$ is neither central-valued nor a multiplication of the block.

**Remark (why no adjoint in the linear convention).** The defining identity of the linear convention, $\langle L^{\star}_{\tilde Q_3}\tilde{Q}_2,\tilde S\rangle_{*} = \langle\tilde{Q}_2,T^{\dagger}\tilde S\rangle_{*}$, is impossible for a conjugate-linear $L^{\star}_{\tilde Q_3}$: the left-hand side is conjugate-linear in $\tilde{Q}_2$, while the right-hand side is linear in $\tilde{Q}_2$ for every additive $T^{\dagger}$. The adjoint therefore exists only in the conjugate-linear convention, where it is the map above. This is the operator expression of the conjugate-linearity of the second slot, and the reason the one-sided theory of the general sesqualgebra, which is written for linear multiplications, does not apply to this family without the conjugate.

## The Composition and the Failure of Multiplicativity

**Theorem (the four composition laws).** For all $\tilde Q_3,\tilde Q_1$,

$$
L^{\star}_{\tilde Q_3}L^{\star}_{\tilde Q_1} = Q_{3t}\,R^{\star}_{\tilde Q_1} , \qquad R^{\star}_{\tilde Q_3}R^{\star}_{\tilde Q_1} = \overline{Q_{3t}}\,R^{\star}_{\tilde Q_1} , \qquad L^{\star}_{\tilde Q_3}R^{\star}_{\tilde Q_1} = Q_{3t}\,L^{\star}_{\tilde Q_1} , \qquad R^{\star}_{\tilde Q_3}L^{\star}_{\tilde Q_1} = \overline{Q_{3t}}\,L^{\star}_{\tilde Q_1} .
$$

In particular the family of operators is closed under composition; the composition of two operators is again a rank-one operator of the family, scaled by the scalar part of the first parameter.

*Proof.* $L^{\star}_{\tilde Q_3}L^{\star}_{\tilde Q_1}\tilde{Q}_2 = L^{\star}_{\tilde Q_3}\bigl(\langle\tilde Q_1,\tilde{Q}_2\rangle_{*}e_t\bigr) = H\bigl(\tilde Q_3,\langle\tilde Q_1,\tilde{Q}_2\rangle_{*}e_t\bigr)e_t = \overline{\langle\tilde Q_1,\tilde{Q}_2\rangle_{*}}\,Q_{3t}e_t = \langle\tilde{Q}_2,\tilde Q_1\rangle_{*}Q_{3t}e_t = Q_{3t}R^{\star}_{\tilde Q_1}\tilde{Q}_2$; the other three are the same computation with the other slot, using $\langle e_t,\tilde Q_3\rangle_{*} = \overline{Q_{3t}}$ for the right family.

**Corollary (the failure of multiplicativity).** The assignment $\tilde Q_3\mapsto L^{\star}_{\tilde Q_3}$ is **not** multiplicative:

$$
L^{\star}_{\tilde Q_3}L^{\star}_{\tilde Q_1} \neq L^{\star}_{\tilde Q_3\star\tilde Q_1}
$$

in general, the left-hand side being $Q_{3t}R^{\star}_{\tilde Q_1}$ and the right-hand side the operator of the central product $\tilde Q_3\star\tilde Q_1 = \langle\tilde Q_3,\tilde Q_1\rangle_{*}e_t$, namely $\tilde{Q}_2\mapsto \langle\tilde Q_3,\tilde Q_1\rangle_{*}\overline{R_t}e_t$.

*Proof.* The two sides have the forms displayed in the two displays and differ already at generic $\tilde Q_3,\tilde Q_1$.

**Remark (the contrast with the row's one-sided operators).** The one-sided operators of the general plain sesqualgebra satisfy $L_{\tilde Q_3}L_{\tilde Q_1} = L_{\tilde Q_3\tilde Q_1}$, a genuine multiplicativity (*One-Sided Operators on the General Plain Sesqualgebra*); the block's operators satisfy the composition laws above because the product is central and the parameter enters through its scalar part alone. The failure of multiplicativity, the conjugate-linearity and the rank-one image are three readings of the same collapse of the product onto the centre.

## The Group of Linear Maps Preserving the Form, and Its Lie Algebra

**Definition.** Let $G_H$ be the group of $\mathbb{C}$-linear bijections $T$ of $\mathbb{B}$ that **preserve the form**,

$$
G_H = \{\,T\in GL_{\mathbb{C}}(\mathbb{B}) : \langle T\tilde Q,T\tilde{Q}_2\rangle_{*} = \langle\tilde Q,\tilde{Q}_2\rangle_{*}\ \text{for all }\tilde Q,\tilde{Q}_2\,\} .
$$

In the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, whose Gram matrix for $H$ is the identity, the condition on the matrix $T$ of the map is

$$
T^{\mathsf H}T = I_4 ,
$$

and the group is named by its invariance condition and by nothing metric.

**Theorem (the Lie algebra).** The Lie algebra of $G_H$ is the space of the $\mathbb{C}$-linear endomorphisms $X$ of $\mathbb{B}$ with

$$
\langle X\tilde Q,\tilde{Q}_2\rangle_{*} + \langle\tilde Q,X\tilde{Q}_2\rangle_{*} = 0 \quad\text{for all }\tilde Q,\tilde{Q}_2 , \qquad\text{that is}\qquad X^{\mathsf H} + X = 0 ,
$$

the endomorphisms **skew with respect to $H$**.

*Proof.* Extend the scalars to the ring of dual numbers $\mathbb{C}[\varepsilon]/(\varepsilon^2)$ and put $S = I + \varepsilon X$ in $G_H$: the invariance $\langle S\tilde Q,S\tilde{Q}_2\rangle_{*} = \langle\tilde Q,\tilde{Q}_2\rangle_{*}$ reads $\langle\tilde Q,\tilde{Q}_2\rangle_{*} + \varepsilon\bigl(\langle X\tilde Q,\tilde{Q}_2\rangle_{*} + \langle\tilde Q,X\tilde{Q}_2\rangle_{*}\bigr) = \langle\tilde Q,\tilde{Q}_2\rangle_{*}$, the terms of order $\varepsilon^2$ vanishing because $\varepsilon^2 = 0$. The order-one part is $\langle X\tilde Q,\tilde{Q}_2\rangle_{*} + \langle\tilde Q,X\tilde{Q}_2\rangle_{*}$, which therefore vanishes identically, and in the basis this is $X^{\mathsf H} + X = 0$. The same computation read backwards gives the converse, so the two conditions cut out the same space.

**Theorem (the automorphisms of the block).** A $\mathbb{C}$-linear bijection $T$ is an automorphism of the product, $T(\tilde Q\star\tilde{Q}_2) = T\tilde Q\star T\tilde{Q}_2$, if and only if it preserves the form and fixes the idempotent $e_t$:

$$
\operatorname{Aut}(\star) = \{\,T\in G_H : Te_t = e_t\,\} .
$$

*Proof.* If $T\in G_H$ with $Te_t = e_t$, then $T(\tilde Q\star\tilde{Q}_2) = \langle\tilde Q,\tilde{Q}_2\rangle_{*}Te_t = \langle\tilde Q,\tilde{Q}_2\rangle_{*}e_t$ and $T\tilde Q\star T\tilde{Q}_2 = \langle T\tilde Q,T\tilde{Q}_2\rangle_{*}e_t = \langle\tilde Q,\tilde{Q}_2\rangle_{*}e_t$, so $T$ is an automorphism. Conversely, let $T$ be an automorphism. Applying it to the identity exhibited in the central form gives $\langle\tilde Q,\tilde{Q}_2\rangle_{*}Te_t = \langle T\tilde Q,T\tilde{Q}_2\rangle_{*}e_t$ for all $\tilde Q,\tilde{Q}_2$; comparing the vector part gives $Te_t = c_te_t$ a central element, and comparing the scalar part then gives $\langle T\tilde Q,T\tilde{Q}_2\rangle_{*} = c_t\langle\tilde Q,\tilde{Q}_2\rangle_{*}$; taking $\tilde Q = \tilde{Q}_2 = e_t$ gives $c_t = \lvert c_t\rvert^{2}$, so $c_t\in\{0,1\}$, and the invertibility of $T$ forces $c_t = 1$. Hence $T\in G_H$ and $Te_t = e_t$.

**Remark (the structure group).** The group that preserves the product **up to a scalar** is the group of $\mathbb{C}$-linear maps $T$ for which $T(\tilde Q\star\tilde{Q}_2) = \chi(T)(T\tilde Q\star T\tilde{Q}_2)$ for a nonzero scalar $\chi(T)$; the same computation shows that $T$ must be a **similarity** of $H$, $\langle T\tilde Q,T\tilde{Q}_2\rangle_{*} = r(T)\langle\tilde Q,\tilde{Q}_2\rangle_{*}$ with $r(T)$ a nonzero scalar, and must send $e_t$ into the line $\mathbb{C}e_t$, with the two scalars related by $Te_t = \chi(T)r(T)e_t$. The automorphism group above is the part with $\chi = r = 1$; the structure group is the bundle of similarities of $H$ that fix the line of the idempotent.

## Worked Examples

**The identity and the central parameter.** For $\tilde Q_3 = \lambda e_t$ the two operators are $L^{\star}_{\lambda e_t}\tilde{Q}_2 = \lambda\,\overline{R_t}e_t$ and $R^{\star}_{\lambda e_t}\tilde{Q}_2 = \overline{\lambda}\,R_te_t$; for $\lambda = 1$ these are $L^{\star}_{e_t}\tilde{Q}_2 = \overline{R_t}e_t$ and $R^{\star}_{e_t}\tilde{Q}_2 = R_te_t$, the two projections of the centre, and neither is the identity because the product has no unit.

**A vector parameter.** For $\tilde Q_3 = \vec e_x$, $L^{\star}_{\vec e_x}\tilde{Q}_2 = \langle \vec e_x,\tilde{Q}_2\rangle_{*}e_t = \overline{R_x}e_t$ and $R^{\star}_{\vec e_x}\tilde{Q}_2 = \langle\tilde{Q}_2,\vec e_x\rangle_{*}e_t = R_xe_t$; the operators are rank one, with kernel the hyperplane $R_x = 0$, and their traces are $0$ and $0$ respectively.

**The adjoint.** For $\tilde Q_3 = \vec e_x + i\vec e_y$, the identity $\langle L^{\star}_{\tilde Q_3}\tilde{Q}_2,\tilde S\rangle_{*} = \overline{\langle\tilde{Q}_2,\overline{S_t}\tilde Q_3\rangle_{*}}$ holds for all $\tilde{Q}_2,\tilde S$, while the candidate $R^{\star}_{\tilde Q_3}$ does not satisfy it; the adjoint of $L^{\star}_{\tilde Q_3}$ is therefore the conjugate-linear map $\tilde S\mapsto\overline{S_t}\tilde Q_3$.

**A composition.** The operators $L^{\star}_{\tilde Q_3}L^{\star}_{\tilde Q_1}$ and $Q_{3t}R^{\star}_{\tilde Q_1}$ are equal, while $L^{\star}_{\tilde Q_3}L^{\star}_{\tilde Q_1}$ and $L^{\star}_{\tilde Q_3\star\tilde Q_1}$ differ in general; the composition of two operators of the family is not the operator of the product of their parameters.

## Summary

The multiplication operators of the block are $L^{\star}_{\tilde Q_3}\tilde{Q}_2 = \langle\tilde Q_3,\tilde{Q}_2\rangle_{*}e_t$ and $R^{\star}_{\tilde Q_3}\tilde{Q}_2 = \langle\tilde{Q}_2,\tilde Q_3\rangle_{*}e_t$; the left family is **conjugate-linear** in its argument and the right family is **$\mathbb{C}$-linear**, and the two are the pointwise conjugates of one another, $R^{\star}_{\tilde Q_3} = \overline{L^{\star}_{\tilde Q_3}}$. Every nonzero operator has **rank one**, image the centre and kernel the hyperplane $H(\tilde Q_3,\cdot\,) = 0$ of real dimension six. The **traces** are $\operatorname{Tr}(R^{\star}_{\tilde Q_3}) = \overline{Q_{3t}}$, conjugate-linear in the parameter, and $\operatorname{Tr}(L^{\star}_{\tilde Q_3}) = Q_{3t}$ in the conjugate-linear convention, the trace-level mark of the sesquilinear class against the bilinear quaternionic block. The **adjoint** of $L^{\star}_{\tilde Q_3}$ with respect to $H$ is the conjugate-linear map $\tilde S\mapsto\overline{S_t}\tilde Q_3$, which is **neither** $L^{\star}_{\tilde Q_3}$ nor $R^{\star}_{\tilde Q_3}$; a conjugate-linear operator has no adjoint in the linear convention, and the failure is the operator expression of the conjugate-linearity. The **composition** laws are $L^{\star}_{\tilde Q_3}L^{\star}_{\tilde Q_1} = Q_{3t}R^{\star}_{\tilde Q_1}$, $R^{\star}_{\tilde Q_3}R^{\star}_{\tilde Q_1} = \overline{Q_{3t}}R^{\star}_{\tilde Q_1}$, $L^{\star}_{\tilde Q_3}R^{\star}_{\tilde Q_1} = Q_{3t}L^{\star}_{\tilde Q_1}$ and $R^{\star}_{\tilde Q_3}L^{\star}_{\tilde Q_1} = \overline{Q_{3t}}L^{\star}_{\tilde Q_1}$, so the family is closed under composition but the assignment is **not multiplicative**, $L^{\star}_{\tilde Q_3}L^{\star}_{\tilde Q_1}\neq L^{\star}_{\tilde Q_3\star\tilde Q_1}$. Finally the group $G_H$ of $\mathbb{C}$-linear maps preserving $H$ has the matrix condition $T^{\mathsf H}T = I_4$ and the Lie algebra $X^{\mathsf H} + X = 0$, the skew endomorphisms; the **automorphisms** of the block are the elements of $G_H$ fixing $e_t$, and the **structure group** is the group of similarities of $H$ fixing the line of the idempotent.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L^{\star}_{\tilde Q_3}\tilde{Q}_2 = \langle\tilde Q_3,\tilde{Q}_2\rangle_{*}e_t$ | the left multiplication; conjugate-linear |
| $R^{\star}_{\tilde Q_3}\tilde{Q}_2 = \langle\tilde{Q}_2,\tilde Q_3\rangle_{*}e_t$ | the right multiplication; $\mathbb{C}$-linear |
| $R^{\star}_{\tilde Q_3} = \overline{L^{\star}_{\tilde Q_3}}$ | the two families are pointwise conjugate |
| $\mathbb{C}_{\mathbb{B}}$, $\{H(\tilde Q_3,\cdot\,) = 0\}$ | the image and the kernel of a nonzero operator; rank one |
| $\operatorname{Tr}(R^{\star}_{\tilde Q_3}) = \overline{Q_{3t}}$, $\operatorname{Tr}(L^{\star}_{\tilde Q_3}) = Q_{3t}$ | the traces |
| $(L^{\star}_{\tilde Q_3})^{\dagger}\tilde S = \overline{S_t}\tilde Q_3$ | the adjoint in the conjugate-linear convention |
| $L^{\star}_{\tilde Q_3}L^{\star}_{\tilde Q_1} = Q_{3t}R^{\star}_{\tilde Q_1}$, etc. | the four composition laws |
| $L^{\star}_{\tilde Q_3}L^{\star}_{\tilde Q_1}\neq L^{\star}_{\tilde Q_3\star\tilde Q_1}$ | the failure of multiplicativity |
| $G_H$, $T^{\mathsf H}T = I_4$ | the group of linear maps preserving $H$ |
| $X^{\mathsf H} + X = 0$ | its Lie algebra, the skew endomorphisms |
| $\operatorname{Aut}(\star) = \{T\in G_H : Te_t = e_t\}$ | the automorphisms of the block |

## Further Reading

- [Introduction to the Symmetric Plain Sesqualgebra](introduction-to-the-symmetric-plain-sesqualgebra.html), for the product and its central image.
- [The Hermitian Form as a Product on the Symmetric Plain Sesqualgebra](the-hermitian-form-as-a-product-on-the-symmetric-plain-sesqualgebra.html), for the form $H$ and the rank-one structure of the product.
- [One-Sided Operators on the General Plain Sesqualgebra](one-sided-operators-on-the-general-plain-sesqualgebra.html), for the general one-sided theory, the composition laws and the adjoints of the linear multiplications.
- [Two-Sided Operators on the General Plain Sesqualgebra](two-sided-operators-on-the-general-plain-sesqualgebra.html), for the two-sided operators of the general product.
- [Mixed Inner Conjugation on the General Plain Sesqualgebra](mixed-inner-conjugation-on-the-general-plain-sesqualgebra.html), for the operators with two independent one-sided parameters.
- [The 4 Forms over the Biquaternion $\mathbb{C}$ Space](the-4-forms-over-the-biquaternion-c-space.html), for the form $H$ and its non-degeneracy.
- [The Multiplication Operators of the Symmetric Plain Algebra](the-multiplication-operators-of-the-symmetric-plain-algebra.html), the sibling with the Jordan identity on the operators.
- [The Multiplication Operators of the Symmetric Quaternionic Algebra](the-multiplication-operators-of-the-symmetric-quaternionic-algebra.html), the bilinear central sibling with linear traces.
