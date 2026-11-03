# __The Right Regular Operators on the Biquaternion Algebra__

## Introduction

**The subject.** The algebra $\mathbb{B}$ acts on itself by right multiplication. For an element $\tilde Q$, the map $X\mapsto X\tilde Q$ is complex-linear, so it is an operator of the ambient space of *The Endomorphisms of the Biquaternion Algebra*; it is written $R_{\tilde Q}$ and called the **right regular operator** of $\tilde Q$. This article studies the family of these operators on the algebra, without a frame.

**What the article proves.** Five things. The map $\tilde Q\mapsto R_{\tilde Q}$ is injective and complex-linear. It is anti-multiplicative, $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$, so its image is a copy of the opposite algebra inside the operator algebra. The kernel and the image of a single $R_{\tilde Q}$ are the left annihilator and the left ideal $\mathbb{B}\tilde Q$. The rank has the same three values as the left family, and the operator is invertible exactly when $N(\tilde Q)\neq0$, with inverse $R_{\tilde Q^{-1}}$. Finally, the right matrix is the transpose of the left one, conjugated by a fixed involution $S$.

**What the article does not do.** The matrix of $R_{\tilde Q}$ is the subject of *The Right Regular Operators on the Biquaternion Algebra*: this article proves the operator statements, and the matrix article computes them in a frame and verifies the exchange entry by entry. The commutant of the two families is *The Commutant of the Two Regular Families*. The association of the two families with the plain form is *The Four Adjoints of the Biquaternion Algebra in Examples*; this article states no adjoint identity.

**The letters.** The operator is $R_{\tilde Q}$, the element is $\tilde Q$, and the argument is $X$. The letter $R$ names the right family and nothing else in this group; the closed ray of the Hermitian sandwich is written without it. The conventions of the four letters, the slots and the matrix are *Operator Family Conventions*; this article uses them and defines none of them.

**Boundaries.** The algebra is *The Biquaternion Algebra*; the operator space is *The Endomorphisms of the Biquaternion Algebra*; the left family is *The Left Regular Operators on the Biquaternion Algebra*; the matrix units are *Special Element and Peirce Conventions*; the norm is *Norm and Unitary Conventions*; the invertibility criterion of an element is *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

## The Map $R_{\tilde Q}$

### Definition and Linearity

**Definition.** For $\tilde Q\in\mathbb{B}$, the **right regular operator** of $\tilde Q$ is

$$
R_{\tilde Q}:\mathbb{B}\longrightarrow\mathbb{B},\qquad R_{\tilde Q}(X)=X\tilde Q .
$$

The product is the algebra product, and the parameter is written on the right.

**Proposition (linearity).** $R_{\tilde Q}$ is complex-linear. The map $\tilde Q\mapsto R_{\tilde Q}$ is complex-linear as well:

$$
R_{\lambda\tilde Q+\mu\tilde P}=\lambda R_{\tilde Q}+\mu R_{\tilde P}.
$$

*Proof.* For the first, $R_{\tilde Q}(X+\lambda Y)=(X+\lambda Y)\tilde Q=X\tilde Q+\lambda Y\tilde Q$. For the second, $X(\lambda\tilde Q+\mu\tilde P)=\lambda X\tilde Q+\mu X\tilde P$ for every $X$.

**The unit.** $R_{e_t}=\mathrm{id}$, because $Xe_t=X$. The zero element gives the zero operator, $R_0=0$.

**The family.** The image of the map is the set $\operatorname{End}_R(\mathbb{B})=\{R_{\tilde Q}:\tilde Q\in\mathbb{B}\}$, named in *Operator Family Conventions*. It is a subset of the ambient operator space, and the map is a map from the algebra onto it.

### Injectivity

**Proposition (injectivity).** The map $\tilde Q\mapsto R_{\tilde Q}$ is injective: if $R_{\tilde Q}=R_{\tilde P}$, then $\tilde Q=\tilde P$. In particular $R_{\tilde Q}=0$ exactly when $\tilde Q=0$.

*Proof.* Evaluate at the unit: $R_{\tilde Q}(e_t)=e_t\tilde Q=\tilde Q$, and $R_{\tilde P}(e_t)=\tilde P$. If the operators are equal, their values at $e_t$ are equal, so $\tilde Q=\tilde P$.

**The reading.** The unit is a faithful probe on the right as well: an element is recovered from its right multiplication by reading the image of $e_t$. The two families are therefore two copies of the same algebra, one seen from each side, and neither copy is a quotient.

**The asymmetry.** The left regular operator is recovered from the image of $e_t$ on the left, $L_{\tilde Q}(e_t)=\tilde Qe_t$, and the right one from the image on the right. The two readings agree at the unit, but the operators differ, because the algebra is not commutative. The mirror statements of this article are in *The Left Regular Operators on the Biquaternion Algebra*, and the two are compared in *The Commutant of the Two Regular Families*.

## The Law $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$

### The Anti-Representation

**Theorem (the law).** For all $\tilde Q,\tilde P\in\mathbb{B}$,

$$
R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}.
$$

*Proof.* For every $X$, $(R_{\tilde Q}R_{\tilde P})(X)=R_{\tilde Q}(X\tilde P)=(X\tilde P)\tilde Q=X(\tilde P\tilde Q)=R_{\tilde P\tilde Q}(X)$, by associativity.

**The anti-representation.** The law says that the assignment $\tilde Q\mapsto R_{\tilde Q}$ reverses the order of the product, so it is an **anti-homomorphism** of complex algebras from $\mathbb{B}$ to $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. It is injective by §*Injectivity*, so it is an anti-isomorphism onto its image. The order is reversed, not the multiplication table: in $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$ the operator applied first is the rightmost, $R_{\tilde P}$, and its parameter stands on the right of the subscript.

**The repair.** The assignment $\tilde Q\mapsto R_{\tilde Q^{\natural}}$ is a representation, because $R_{\tilde Q^{\natural}}R_{\tilde P^{\natural}}=R_{\tilde P^{\natural}\tilde Q^{\natural}}=R_{(\tilde Q\tilde P)^{\natural}}$. The conjugation converts the anti-representation into a representation at the cost of one more map; the article that uses the repair says so, and this one keeps the anti-representation because the order is the point.

**The unit and the powers.** $R_{e_t}=\mathrm{id}$ and $R_{\tilde Q^n}=(R_{\tilde Q})^n$ for every $n\geq0$. For a unit $\tilde Q$, the inverse law of §*Invertibility* extends the identity to the negative powers.

### The Opposite Algebra

**Definition.** The **opposite algebra** $\mathbb{B}^{\mathrm{opp}}$ is the algebra with the same underlying vector space and the product

$$
\tilde Q\cdot\tilde P=\tilde P\tilde Q .
$$

**Theorem (the image).** The image $\operatorname{End}_R(\mathbb{B})$ is a subalgebra of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, anti-isomorphic to $\mathbb{B}$ and isomorphic to $\mathbb{B}^{\mathrm{opp}}$. Its complex dimension is $4$.

*Proof.* The image is closed under addition and scalar multiplication by the linearity of $\tilde Q\mapsto R_{\tilde Q}$, and under composition by the law. It contains the identity $R_{e_t}$. The map $\tilde Q\mapsto R_{\tilde Q}$ is an injective anti-homomorphism, so it is an anti-isomorphism onto its image; composing with the identity map on the underlying space turns the anti-homomorphism into a homomorphism $\mathbb{B}^{\mathrm{opp}}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. The complex dimension is that of $\mathbb{B}$, which is $4$.

**What the copy preserves.** The copy preserves every polynomial relation of the algebra, with the order of the factors reversed: a relation holds in $\mathbb{B}$ exactly when the reversed relation holds in the image. It does not preserve the trace, the determinant or the spectrum of an element; the operator has its own invariants, computed in the matrix article.

**What the copy does not contain.** The copy has complex dimension four, while the ambient space has complex dimension sixteen. It is not the whole operator space, and it is not the left copy: the two copies meet only in the scalars, a statement proved in *The Commutant of the Two Regular Families*. The containment of the copy in the two-sided family is proper, and it is read in Part IV.

## Kernel and Image

### The Left Annihilator

**Definition.** For $\tilde Q\in\mathbb{B}$, the **left annihilator** of $\tilde Q$ is

$$
\operatorname{Ann}_l(\tilde Q)=\{X\in\mathbb{B}:X\tilde Q=0\}.
$$

It is a complex subspace of $\mathbb{B}$.

**Proposition (the kernel).** $\ker R_{\tilde Q}=\operatorname{Ann}_l(\tilde Q)$.

*Proof.* $R_{\tilde Q}(X)=0$ is $X\tilde Q=0$, which is the defining condition of the left annihilator.

**The three cases.** In the $2\times2$ model of *$M_2(\mathbb{C})$ Pauli Representation*, $X\tilde Q=0$ says that every row of $X$ is a left null vector of $\tilde Q$:

- if $\tilde Q$ is a unit, the left annihilator is $0$, of complex dimension $0$;
- if $\tilde Q\neq0$ and $N(\tilde Q)=0$, the matrix has rank one, its left null space is a line, and the left annihilator is the complex two-dimensional space of matrices whose rows lie in that line;
- if $\tilde Q=0$, the annihilator is the whole algebra, of complex dimension $4$.

**The two annihilators.** The left annihilator is the kernel of $R_{\tilde Q}$ and the right annihilator is the kernel of $L_{\tilde Q}$. They coincide at the units, where both are zero, and at the zero element, where both are the whole algebra; for a general zero divisor they are different spaces, and the article keeps the two words apart.

### The Left Ideal $\mathbb{B}\tilde Q$

**Definition.** The image of $R_{\tilde Q}$ is the set

$$
\mathbb{B}\tilde Q=\{X\tilde Q:X\in\mathbb{B}\},
$$

the **left ideal generated by $\tilde Q$**. It is a complex subspace of $\mathbb{B}$, and it is the image of the operator.

**Proposition (the image).** $\operatorname{im}R_{\tilde Q}=\mathbb{B}\tilde Q$.

*Proof.* The image is the set of the values $X\tilde Q$, which is the definition of $\mathbb{B}\tilde Q$.

**The three cases.** In the same $2\times2$ model:

- if $\tilde Q$ is a unit, $\mathbb{B}\tilde Q=\mathbb{B}$, of complex dimension $4$;
- if $\tilde Q\neq0$ and $N(\tilde Q)=0$, the left ideal is the complex two-dimensional space of matrices whose rows lie in the row line of $\tilde Q$;
- if $\tilde Q=0$, the image is $0$.

**The left ideal is not the algebra.** For a zero divisor the left ideal is a proper subspace, and it is a left ideal in the sense that $\mathbb{B}(\mathbb{B}\tilde Q)\subseteq\mathbb{B}\tilde Q$. The side is the side of the ideal, not the side of the multiplication: a right multiplication generates a left ideal, and the mirror statement is in *The Left Regular Operators on the Biquaternion Algebra*.

### The Rank

**Theorem (the rank).** The rank of $R_{\tilde Q}$ is

$$
\operatorname{rank}R_{\tilde Q}=
\begin{cases}
4, & \tilde Q\ \text{a unit},\\
2, & \tilde Q\neq0\ \text{and}\ N(\tilde Q)=0,\\
0, & \tilde Q=0.
\end{cases}
$$

*Proof.* The rank is the dimension of the image, computed in §*The Left Ideal $\mathbb{B}\tilde Q$*: four, two and zero in the three cases. Equivalently, the rank is $4-\dim\operatorname{Ann}_l(\tilde Q)$ by rank-nullity, and the three annihilator complex dimensions are $0$, $2$ and $4$.

**The middle case.** The value two is the signature of the biquaternion algebra: a nonzero zero divisor has a complex two-dimensional left ideal and a complex two-dimensional left annihilator, and the two complex dimensions add to four. The left and the right families have the same three ranks, because the rank depends on the element and not on the side.

**The rank is not the norm.** The rank takes three values, the norm is a complex number, and the two are related only by the criterion: the rank is four exactly when the norm is nonzero. A zero norm leaves the two values two and zero, and whether the element is zero decides between them.

## Invertibility

### The Criterion $N(\tilde Q)\neq0$

**Theorem (the criterion).** The operator $R_{\tilde Q}$ is invertible exactly when $N(\tilde Q)\neq0$.

*Proof.* If $R_{\tilde Q}$ is invertible, it is surjective, so there is an $X$ with $X\tilde Q=e_t$; then $\tilde Q$ has a left inverse, and in a finite-dimensional algebra a left inverse is a two-sided inverse, so $\tilde Q$ is a unit and $N(\tilde Q)\neq0$. Conversely, if $N(\tilde Q)\neq0$, then $\tilde Q$ is a unit, and $R_{\tilde Q}$ has the inverse $R_{\tilde Q^{-1}}$ by the law.

**The criterion read on the element.** The condition $N(\tilde Q)\neq0$ is the invertibility criterion of the algebra, fixed in *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, §*Regular and Degenerate Biquaternions*: the units are exactly the elements of nonzero quaternionic norm. The operator criterion and the element criterion are the same criterion, read on the two objects.

**The determinant reading.** In the matrix article the determinant of $R_{\tilde Q}$ is $N(\tilde Q)^2$, so the criterion is also $\det R_{\tilde Q}\neq0$. The square is the square of the $2\times2$ determinant, as it is for the left family, and the operator is invertible exactly when that determinant is nonzero.

### The Inverse $R_{\tilde Q^{-1}}$

**Theorem (the inverse).** If $\tilde Q$ is a unit, then $R_{\tilde Q}$ is invertible and

$$
(R_{\tilde Q})^{-1}=R_{\tilde Q^{-1}}.
$$

*Proof.* $R_{\tilde Q}R_{\tilde Q^{-1}}=R_{\tilde Q^{-1}\tilde Q}=R_{e_t}=\mathrm{id}$, and the same on the other side, by the law of §*The Anti-Representation*.

**The inverse is in the family.** The inverse of a right multiplication is a right multiplication, by the inverse element. The right family is therefore closed under inversion, and the inverse is the one of the algebra. The operator inverse and the element inverse are the same operation, read on the two objects.

**The norm of the inverse.** $N(\tilde Q^{-1})=1/N(\tilde Q)$, by the multiplicativity of the norm. The identity shows that the inverse element is defined exactly where the criterion holds, and it is the same identity for the left family.

## The Exchange $S L_{\tilde Q}^{\mathsf T}S^{-1}$

### The Operator $S$

**Definition.** The **exchange** $S$ is the linear involution of $\mathbb{B}$ that fixes the two idempotents and exchanges the two mixed Peirce units:

$$
S\tilde\Pi_\pm=\tilde\Pi_\pm,\qquad S\vec\Upsilon_+=\vec\Upsilon_-,\qquad S\vec\Upsilon_-=\vec\Upsilon_+.
$$

**The two displays.** In the Peirce frame $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$ the matrix of $S$ is the permutation of the second and third coordinates,

$$
S=\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{pmatrix},
$$

symmetric and involutive. In the coefficient frame $(e_t,\vec e_x,\vec e_y,\vec e_z)$ the same operator is the reflection

$$
S=\operatorname{diag}(1,1,-1,1),
$$

which fixes $e_t,\vec e_x,\vec e_z$ and negates $\vec e_y$.

**The invariants of $S$.** $S^2=\mathrm{id}$, $S^{\mathsf T}=S=S^{-1}$, $\operatorname{tr}S=2$ and $\det S=-1$. The trace is the complex dimension of the fixed space, the span of $\tilde\Pi_+$ and $\tilde\Pi_-$; the determinant is $-1$ because the two mixed coordinates are exchanged.

**What $S$ is not.** $S$ is a linear involution of the carrier, not an algebra map and not a one-sided multiplication. It is not multiplicative: $S(\vec e_x\vec e_y)=S(\vec e_z)=\vec e_z$, while $S(\vec e_x)S(\vec e_y)=\vec e_x(-\vec e_y)=-\vec e_z$. It is not a left or a right multiplication: a multiplication that fixes $e_t$ is the identity, because $L_{\tilde Q}(e_t)=\tilde Q$ and $R_{\tilde Q}(e_t)=\tilde Q$, and $S$ is not the identity. It is also not the natural conjugation, which negates all three vector units; $S$ negates only $\vec e_y$.

### The Two Mixed Units

**The flip.** In the Peirce frame the carrier is the tensor product of the two Peirce columns, and the four elements are

$$
\tilde\Pi_+=e_1\otimes e_1,\quad
\vec\Upsilon_+=e_2\otimes e_1,\quad
\vec\Upsilon_-=e_1\otimes e_2,\quad
\tilde\Pi_-=e_2\otimes e_2 .
$$

The operator $S$ is the flip of the two tensor factors: it fixes $e_1\otimes e_1$ and $e_2\otimes e_2$, and it exchanges $e_1\otimes e_2$ with $e_2\otimes e_1$. The two mixed units are exactly the two off-diagonal tensor basis elements, and the exchange of the two mixed units is the flip. The name of the operator records the two elements it moves.

**Theorem (the exchange).** In the Peirce frame, for every $\tilde Q\in\mathbb{B}$,

$$
[R_{\tilde Q}]=S\,[L_{\tilde Q}]^{\mathsf T}\,S^{-1}.
$$

The transpose is the matrix transpose in the Peirce frame.

*Proof.* In the Peirce frame $[L_{\tilde Q}]=I_2\otimes\mathsf M_2(\tilde Q)$, by *The Left Regular Operators on the Biquaternion Algebra*, §*The Rule*. The transpose of a tensor product is the tensor product of the transposes, and $I_2^{\mathsf T}=I_2$, so $[L_{\tilde Q}]^{\mathsf T}=I_2\otimes\mathsf M_2(\tilde Q)^{\mathsf T}$. The flip $S$ conjugates $A\otimes B$ to $B\otimes A$, so

$$
S\,[L_{\tilde Q}]^{\mathsf T}\,S^{-1}=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2 .
$$

The $j$-th column of $\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2$ acting on $X$ is $\sum_iX_{*i}\mathsf M_2(\tilde Q)_{ij}$, where $X_{*i}$ is the $i$-th column of $X$; the $j$-th column of $X\tilde Q$ is the same sum. Both sides are therefore the matrix of $X\mapsto X\tilde Q$, and the identity follows.

**The frame.** The transpose is not an invariant of an operator: it depends on the frame in which the matrix is written. The identity is a matrix identity in the Peirce frame, and the same operator $S$ has the coefficient display $\operatorname{diag}(1,1,-1,1)$. The matrix article states the identity in the frame it uses and verifies it entry by entry; the operator $S$ is the same object in both.

**The sign on the $y$ generator.** With $\mathsf M_2(\vec e_y)=-i\sigma_2=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, the transpose is

$$
\mathsf M_2(\vec e_y)^{\mathsf T}=+i\sigma_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$

and the right matrix is $R_{\vec e_y}=+i\sigma_2\otimes I_2$, with no minus. The minus that older displays carried came from transposing the Pauli matrix while keeping the factor $-i$; the factor is part of the generator and is transposed with it. The matrix article verifies the sign on the four generators, and the correction is uniform across the corpus.

## Summary

The right regular operator of $\tilde Q$ is $R_{\tilde Q}(X)=X\tilde Q$. The assignment $\tilde Q\mapsto R_{\tilde Q}$ is complex-linear, injective, and anti-multiplicative, $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$; the unit goes to the identity, and the image is a copy of the opposite algebra inside the operator space, of complex dimension four. The copy preserves the algebra relations with the order reversed and nothing else.

The kernel of $R_{\tilde Q}$ is the left annihilator of $\tilde Q$, and the image is the left ideal $\mathbb{B}\tilde Q$. The rank is four for a unit, two for a nonzero zero divisor, and zero for the zero element. The operator is invertible exactly when $N(\tilde Q)\neq0$, and then its inverse is $R_{\tilde Q^{-1}}$.

In the Peirce frame the right matrix is the transpose of the left one conjugated by the exchange $S$, the flip of the two mixed Peirce units: $[R_{\tilde Q}]=S[L_{\tilde Q}]^{\mathsf T}S^{-1}$. In the coefficient frame $S$ is the reflection $\operatorname{diag}(1,1,-1,1)$. The sign on the $y$ generator is positive, $R_{\vec e_y}=+i\sigma_2\otimes I_2$, and the matrix article verifies it entry by entry.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R_{\tilde Q}$ | The right regular operator, $X\mapsto X\tilde Q$ |
| $\operatorname{End}_R(\mathbb{B})$ | The set of the right regular operators |
| $\mathbb{B}^{\mathrm{opp}}$ | The opposite algebra, product $\tilde Q\cdot\tilde P=\tilde P\tilde Q$ |
| $\operatorname{Ann}_l(\tilde Q)$ | The left annihilator, $\{X:X\tilde Q=0\}$ |
| $\mathbb{B}\tilde Q$ | The left ideal generated by $\tilde Q$, the image of $R_{\tilde Q}$ |
| $\operatorname{rank}R_{\tilde Q}$ | $4$, $2$ or $0$ according to the three cases |
| $S$ | The exchange, fixing $\tilde\Pi_\pm$ and swapping $\vec\Upsilon_\pm$ |
| $[R_{\tilde Q}]=S[L_{\tilde Q}]^{\mathsf T}S^{-1}$ | The exchange in the Peirce frame |

## Further Reading

- [The Left Regular Operators on the Biquaternion Algebra](the-left-regular-operators-on-the-biquaternion-algebra.html), for the mirror family and the two annihilators.
- [The Right Regular Operators on the Biquaternion Algebra](the-right-regular-operators-on-the-biquaternion-algebra.html), for the matrix $\mathsf M_2(\tilde Q)^{\mathsf T}\otimes I_2$ and the verification of the exchange.
- [The Commutant of the Two Regular Families](the-commutant-of-the-two-regular-families.html), for the commutation and the two centralisers.
- [The Left Regular Operators on the Biquaternion Algebra](the-left-regular-operators-on-the-biquaternion-algebra.html), for the matrix $I_2\otimes\mathsf M_2(\tilde Q)$ transposed here.
- [The Endomorphisms of the Biquaternion Algebra](the-endomorphisms-of-the-biquaternion-algebra.html), for the ambient space and the natural conjugation.
- [Operator Family Conventions](operator-family-conventions.html), for the letter $R$, the slots and the set names.
