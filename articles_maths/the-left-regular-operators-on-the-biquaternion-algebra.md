# __The Left Regular Operators on the Biquaternion Algebra__

## Introduction

**The subject.** The algebra $\mathbb{B}$ acts on itself by left multiplication. For an element $\tilde Q$, the map $X\mapsto\tilde QX$ is complex-linear, so it is an operator of the ambient space of *The Endomorphisms of the Biquaternion Algebra*; it is written $L_{\tilde Q}$ and called the **left regular operator** of $\tilde Q$. This article studies the family of these operators on the algebra, without a frame.

**What the article proves.** Four things, in this order. The map $\tilde Q\mapsto L_{\tilde Q}$ is injective and complex-linear. It is multiplicative, $L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P}$, so its image is a copy of the algebra inside the operator algebra. The kernel and the image of a single $L_{\tilde Q}$ are the right annihilator and the right ideal $\tilde Q\mathbb{B}$. The operator $L_{\tilde Q}$ is invertible exactly when $\tilde Q$ is a unit, and its inverse is $L_{\tilde Q^{-1}}$.

**What the article does not do.** The matrix of $L_{\tilde Q}$ is the subject of *$M_4(\mathbb{C})_{\mathbb{B}_L}$ Representation : The Left Regular Operators on the Biquaternion Algebra*: this article proves the operator statements, and the matrix article computes them in a frame. The right family is the subject of Part III, the two-sided family of Part IV. The left family alone is treated here.

**The letters.** The operator is $L_{\tilde Q}$, the element is $\tilde Q$, and the argument is $X$. The letter $L$ names left multiplication and is not an index. The conventions of the four letters, the slots and the matrix are *Operator Family Conventions*; this article uses them and defines none of them.

**Boundaries.** The algebra is *The Biquaternion Algebra*; the operator space is *The Endomorphisms of the Biquaternion Algebra*; the matrix units are *Special Element and Peirce Conventions*; the norm is *Norm and Unitary Conventions*; the invertibility criterion of an element is *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

## The Map $L_{\tilde Q}$

### Definition and Linearity

**Definition.** For $\tilde Q\in\mathbb{B}$, the **left regular operator** of $\tilde Q$ is

$$
L_{\tilde Q}:\mathbb{B}\longrightarrow\mathbb{B},\qquad L_{\tilde Q}(X)=\tilde QX .
$$

The product is the algebra product, and the argument is written on the right.

**Proposition (linearity).** $L_{\tilde Q}$ is complex-linear. The map $\tilde Q\mapsto L_{\tilde Q}$ is complex-linear as well:

$$
L_{\lambda\tilde Q+\mu\tilde P}=\lambda L_{\tilde Q}+\mu L_{\tilde P}.
$$

*Proof.* For the first, $L_{\tilde Q}(X+\lambda Y)=\tilde Q(X+\lambda Y)=\tilde QX+\lambda\tilde QY$, by distributivity and the complex bilinearity of the product. For the second, $((\lambda\tilde Q+\mu\tilde P)X)=\lambda\tilde QX+\mu\tilde PX$ for every $X$.

**The unit.** $L_{e_t}=\mathrm{id}$, because $e_tX=X$. The zero element gives the zero operator, $L_0=0$.

**The family.** The image of the map is the set $\operatorname{End}_L(\mathbb{B})=\{L_{\tilde Q}:\tilde Q\in\mathbb{B}\}$, named in *Operator Family Conventions*. It is a subset of the ambient operator space, and the map is a map from the algebra onto it.

### Injectivity

**Proposition (injectivity).** The map $\tilde Q\mapsto L_{\tilde Q}$ is injective: if $L_{\tilde Q}=L_{\tilde P}$, then $\tilde Q=\tilde P$. In particular $L_{\tilde Q}=0$ exactly when $\tilde Q=0$.

*Proof.* Evaluate at the unit: $L_{\tilde Q}(e_t)=\tilde Qe_t=\tilde Q$, and $L_{\tilde P}(e_t)=\tilde P$. If the operators are equal, their values at $e_t$ are equal, so $\tilde Q=\tilde P$. The second statement is the case $\tilde P=0$.

**The reading.** The unit is a faithful probe: an element is recovered from its left multiplication by reading the image of $e_t$. This is the reason the left family can be treated as a copy of the algebra, and the reason the map has an inverse on its image.

**A consequence.** Two different elements give two different operators, so the family has as many members as the algebra. The family is not a quotient and the letter $\tilde Q$ in $L_{\tilde Q}$ is the element itself, not a class.

## The Law $L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P}$

### The Left Regular Representation

**Theorem (the law).** For all $\tilde Q,\tilde P\in\mathbb{B}$,

$$
L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P}.
$$

*Proof.* For every $X$, $(L_{\tilde Q}L_{\tilde P})(X)=L_{\tilde Q}(\tilde PX)=\tilde Q(\tilde PX)=(\tilde Q\tilde P)X=L_{\tilde Q\tilde P}(X)$, by associativity.

**The representation.** The law says that the assignment $\tilde Q\mapsto L_{\tilde Q}$ is a homomorphism of complex algebras from $\mathbb{B}$ to $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. It is injective by §*Injectivity*, so it is an isomorphism onto its image. It is the **left regular representation** of the algebra.

**The order.** The order of the factors is preserved: $L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P}$, and the element on the left of the product is the one applied last. A representation that reverses the order is the right one, and it is the subject of Part III.

**The unit and the powers.** $L_{e_t}=\mathrm{id}$ and $L_{\tilde Q^n}=(L_{\tilde Q})^n$ for every $n\geq0$. For a unit $\tilde Q$, the inverse law of §*Invertibility* extends the identity to the negative powers.

### The Image as a Copy of the Algebra

**Theorem (the image).** The image $\operatorname{End}_L(\mathbb{B})$ is a subalgebra of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, isomorphic to $\mathbb{B}$ as a complex algebra. Its complex dimension is $4$.

*Proof.* The image is closed under addition and scalar multiplication by the linearity of $\tilde Q\mapsto L_{\tilde Q}$, and under composition by the law. It contains the identity $L_{e_t}$. The map is an injective algebra homomorphism, so it is an isomorphism onto its image. The complex dimension is that of $\mathbb{B}$, which is $4$.

**What the copy preserves.** The copy preserves every polynomial relation of the algebra: a relation between elements holds between their left multiplications and conversely. It does not preserve the trace, the determinant or the spectrum of an element, because those are not algebra relations; the operator has its own invariants, computed in the matrix article.

**What the copy does not contain.** The copy is not the whole operator space: it has complex dimension four, while the ambient space has complex dimension sixteen. An operator outside it is not a left multiplication, and the articles that produce such operators are Part IV and Part V.

## Kernel and Image

### The Right Annihilator

**Definition.** For $\tilde Q\in\mathbb{B}$, the **right annihilator** of $\tilde Q$ is

$$
\operatorname{Ann}_r(\tilde Q)=\{X\in\mathbb{B}:\tilde QX=0\}.
$$

It is a complex subspace of $\mathbb{B}$.

**Proposition (the kernel).** $\ker L_{\tilde Q}=\operatorname{Ann}_r(\tilde Q)$.

*Proof.* $L_{\tilde Q}(X)=0$ is $\tilde QX=0$, which is the defining condition of the right annihilator.

**The three cases.** The complex dimension of the annihilator is read in the $2\times2$ model of *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*, where $\tilde Q$ is a $2\times2$ matrix:

- if $\tilde Q$ is a unit, $\operatorname{Ann}_r(\tilde Q)=0$, of complex dimension $0$;
- if $\tilde Q\neq0$ and $N(\tilde Q)=0$, the matrix has rank one, its kernel is a line, and the right annihilator is the complex two-dimensional space of matrices whose columns lie in that line;
- if $\tilde Q=0$, the annihilator is the whole algebra, of complex dimension $4$.

In the second case the annihilator is not a line: a rank-one matrix annihilates a complex two-dimensional space on the right, one complex dimension for each column. The distinction between the left and the right annihilator is the distinction between the kernel of $L_{\tilde Q}$ and the kernel of $R_{\tilde Q}$, and the two spaces need not coincide.

### The Right Ideal $\tilde Q\mathbb{B}$

**Definition.** The image of $L_{\tilde Q}$ is the set

$$
\tilde Q\mathbb{B}=\{\tilde QX:X\in\mathbb{B}\},
$$

the **right ideal generated by $\tilde Q$**. It is a complex subspace of $\mathbb{B}$, and it is the image of the operator.

**Proposition (the image).** $\operatorname{im}L_{\tilde Q}=\tilde Q\mathbb{B}$.

*Proof.* The image is the set of the values $\tilde QX$, which is the definition of $\tilde Q\mathbb{B}$.

**The three cases.** In the same $2\times2$ model:

- if $\tilde Q$ is a unit, $\tilde Q\mathbb{B}=\mathbb{B}$, of complex dimension $4$;
- if $\tilde Q\neq0$ and $N(\tilde Q)=0$, the right ideal is the complex two-dimensional space of matrices whose columns lie in the image line of $\tilde Q$;
- if $\tilde Q=0$, the image is $0$.

**The right ideal is not the algebra.** For a zero divisor the right ideal is a proper subspace, and it is a right ideal in the sense that $(\tilde Q\mathbb{B})\mathbb{B}\subseteq\tilde Q\mathbb{B}$. The side is the side of the ideal, not the side of the multiplication: a left multiplication generates a right ideal, and the mirror statement is in *The Right Regular Operators on the Biquaternion Algebra*.

### The Rank

**Theorem (the rank).** The rank of $L_{\tilde Q}$ is

$$
\operatorname{rank}L_{\tilde Q}=
\begin{cases}
4, & \tilde Q\ \text{a unit},\\
2, & \tilde Q\neq0\ \text{and}\ N(\tilde Q)=0,\\
0, & \tilde Q=0.
\end{cases}
$$

*Proof.* The rank is the dimension of the image, computed in §*The Right Ideal $\tilde Q\mathbb{B}$*: four, two and zero in the three cases. Equivalently, the rank is $4-\dim\operatorname{Ann}_r(\tilde Q)$ by rank-nullity, and the three annihilator complex dimensions are $0$, $2$ and $4$.

**The middle case.** The value two is the signature of the biquaternion algebra: a nonzero zero divisor has a complex two-dimensional right ideal and a complex two-dimensional right annihilator, and the two complex dimensions add to four. A general element of the algebra is a unit, so the generic rank is four; the degenerate ranks are two and zero.

**The rank is not the norm.** The rank takes three values, the norm is a complex number, and the two are related only by the criterion: the rank is four exactly when the norm is nonzero. A zero norm leaves the two values two and zero, and whether the element is zero decides between them.

## Invertibility

### The Criterion $N(\tilde Q)\neq0$

**Theorem (the criterion).** The operator $L_{\tilde Q}$ is invertible exactly when $N(\tilde Q)\neq0$.

*Proof.* If $L_{\tilde Q}$ is invertible, it is surjective, so there is an $X$ with $\tilde QX=e_t$; then $\tilde Q$ has a right inverse, and in a finite-dimensional algebra a right inverse is a two-sided inverse, so $\tilde Q$ is a unit and $N(\tilde Q)\neq0$. Conversely, if $N(\tilde Q)\neq0$, then $\tilde Q$ is a unit, and $L_{\tilde Q}$ has the inverse $L_{\tilde Q^{-1}}$ by the law.

**The criterion read on the element.** The condition $N(\tilde Q)\neq0$ is the invertibility criterion of the algebra, fixed in *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, §*Regular and Degenerate Biquaternions*: the units are exactly the elements of nonzero quaternionic norm. The operator criterion and the element criterion are therefore the same criterion, read on the two objects.

**The determinant reading.** In the matrix article the determinant of $L_{\tilde Q}$ is $N(\tilde Q)^2$, so the criterion is also $\det L_{\tilde Q}\neq0$. The square is not an accident: the left regular matrix is the identity on one tensor factor and the $2\times2$ model on the other, and its determinant is the square of the $2\times2$ determinant. The operator is invertible exactly when that determinant is nonzero.

### The Inverse $L_{\tilde Q^{-1}}$

**Theorem (the inverse).** If $\tilde Q$ is a unit, then $L_{\tilde Q}$ is invertible and

$$
(L_{\tilde Q})^{-1}=L_{\tilde Q^{-1}}.
$$

*Proof.* $L_{\tilde Q}L_{\tilde Q^{-1}}=L_{\tilde Q\tilde Q^{-1}}=L_{e_t}=\mathrm{id}$, and the same on the other side, by the law of §*The Left Regular Representation*.

**The inverse is in the family.** The inverse of a left multiplication is a left multiplication, by the inverse element. The left family is therefore closed under inversion, and the inverse is the one of the algebra. The operator inverse and the element inverse are the same operation, read on the two objects.

**The norm of the inverse.** $N(\tilde Q^{-1})=1/N(\tilde Q)$. The identity is the multiplicativity of the norm, $N(\tilde Q\tilde Q^{-1})=N(e_t)=1$, and it shows that the inverse element is defined exactly where the criterion holds.

## Summary

The left regular operator of $\tilde Q$ is $L_{\tilde Q}(X)=\tilde QX$. The assignment $\tilde Q\mapsto L_{\tilde Q}$ is complex-linear, injective, and multiplicative, $L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P}$; the unit goes to the identity, and the image is a copy of the algebra inside the operator space, of complex dimension four. The copy preserves the algebra relations and nothing else.

The kernel of $L_{\tilde Q}$ is the right annihilator of $\tilde Q$, and the image is the right ideal $\tilde Q\mathbb{B}$. The rank is four for a unit, two for a nonzero zero divisor, and zero for the zero element. The operator is invertible exactly when $N(\tilde Q)\neq0$, and then its inverse is $L_{\tilde Q^{-1}}$.

The three statements — the law, the rank trichotomy and the criterion — are the operator form of the multiplication of the algebra. The matrix form is the subject of *$M_4(\mathbb{C})_{\mathbb{B}_L}$ Representation : The Left Regular Operators on the Biquaternion Algebra*, where the same three statements are read entry by entry in the Peirce frame.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde Q}$ | The left regular operator, $X\mapsto\tilde QX$ |
| $\operatorname{End}_L(\mathbb{B})$ | The set of the left regular operators |
| $\operatorname{Ann}_r(\tilde Q)$ | The right annihilator, $\{X:\tilde QX=0\}$ |
| $\tilde Q\mathbb{B}$ | The right ideal generated by $\tilde Q$, the image of $L_{\tilde Q}$ |
| $\operatorname{rank}L_{\tilde Q}$ | $4$, $2$ or $0$ according to the three cases |
| $N(\tilde Q)$ | The quaternionic norm, the invertibility criterion |
| $L_{\tilde Q^{-1}}$ | The inverse of $L_{\tilde Q}$ |

## Further Reading

- [The Endomorphisms of the Biquaternion Algebra](the-endomorphisms-of-the-biquaternion-algebra.html), for the ambient operator space and the complex dimension sixteen.
- [$M_4(\mathbb{C})$ Representation : The General Endomorphisms](m4c-representation-the-general-endomorphisms.html), for the matrix of a general operator and the units.
- [$M_4(\mathbb{C})_{\mathbb{B}_L}$ Representation : The Left Regular Operators on the Biquaternion Algebra](m4c-representation-the-left-regular-operators-on-the-biquaternion-algebra.html), for the matrix $I_2\otimes\mathsf M_2(\tilde Q)$, the trace, the determinant and the spectrum.
- [The Right Regular Operators on the Biquaternion Algebra](the-right-regular-operators-on-the-biquaternion-algebra.html), for the other side and the exchange.
- [$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant](m2c-model-the-product-the-trace-and-the-determinant.html), for the $2\times2$ model, the determinant and the norm.
- [Norm and Unitary Conventions](conventions-of-the-norms-and-the-unitary-convention.html), for the norm and the invertibility criterion.
- [Operator Family Conventions](conventions-of-the-operator-families.html), for the letter $L$, the slots and the set names.
