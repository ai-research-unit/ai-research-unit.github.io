# __Operators Acting 1 Side__

## Introduction

**The subject.** The algebra $\mathbb{B}$ acts on itself in two ways. For an element $\tilde Q$, the maps

$$
L_{\tilde Q}:\mathbb{B}\longrightarrow\mathbb{B},\quad L_{\tilde Q}(X)=\tilde QX,
\qquad
R_{\tilde Q}:\mathbb{B}\longrightarrow\mathbb{B},\quad R_{\tilde Q}(X)=X\tilde Q
$$

are complex-linear, so they are operators of the ambient space of *The Endomorphisms of the Biquaternion Algebra*. They are the **left regular operator** and the **right regular operator** of $\tilde Q$. This article studies the two families together, without a frame.

**Why they are one subject.** The two families are the same construction read from the two sides, and every statement about the one is the mirror of a statement about the other: the same injectivity with the unit as probe, the same dimension, the same three ranks, the same invertibility criterion, the same inverse. The one place where the mirror fails is the law — one family is multiplicative and the other anti-multiplicative — and that failure is exactly what the last section measures, when the two families are put in one operator space and asked which operators commute with which.

**What the article proves.** Five things, in this order. The two maps are injective and complex-linear. The left one is multiplicative, $L_{\tilde Q}L_{\tilde Q_2}=L_{\tilde Q\tilde Q_2}$, and the right one is anti-multiplicative, $R_{\tilde Q}R_{\tilde Q_2}=R_{\tilde Q_2\tilde Q}$; the two images are copies of $\mathbb{B}$ and of $\mathbb{B}_{\mathrm{opp}}$, each of complex dimension four. The kernel and the image of a single operator are the annihilator and the ideal of the element, on the opposite side of the multiplication, and the rank takes the three values $4,2,0$. The operator is invertible exactly when $\langle\tilde Q\rangle_{\natural}\neq0$, and the inverse is the operator of the inverse element. Finally, the two families commute element by element, each is the exact commutant of the other, and they meet in the scalars.

**What the article does not do.** The matrices of the two families are the subject of the three matrix articles of the group, where the exchange of §*The Exchange $S$* is verified entry by entry. The products $L_{\tilde Q}R_{\tilde Q_2}$ are *Operators Acting 2 Side*; the sandwiches $\mathrm{Sd}_{\tilde Q}$ are Part V; the association of the two families with the four forms is *Adjoint Pair of $L$ and $R$ Operators*; the enveloping algebra in which the pair of actions lives is *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*. This article states no adjoint identity, no product of the two families and no form.

**The letters.** The left operator is $L_{\tilde Q}$, the right operator is $R_{\tilde Q_2}$, and the argument is $X$. The letter names the action and not a slot, and the subscript is the element with its own mark. The sets are written $\operatorname{End}_L(\mathbb{B})$ and $\operatorname{End}_R(\mathbb{B})$, abbreviated $L(\mathbb{B})$ and $R(\mathbb{B})$ where a set is used in an identity, and the prime is the commutant: for a set $\mathcal{S}$ of operators, $\mathcal{S}'=\{T:TS=ST\ \text{for every}\ S\in\mathcal{S}\}$. The letter $R$ names the right family and nothing else in this group; the closed ray of the Hermitian sandwich is written as a set and never with that letter. The conventions of the letters, the slots and the set names are *Operator Family Conventions*; this article uses them and defines none of them. **Two words for one object.** The family is **one-sided**, because each member multiplies on one side only, and the member is **regular**, because it is a multiplication of the regular module; the article is named for the family and calls its members the left and the right regular operators.

**Boundaries.** The algebra and its centre are *The Biquaternion Algebra*; the operator space is *The Endomorphisms of the Biquaternion Algebra*; the matrix units are *Special Element and Peirce Conventions*; the norm and the unitary convention are *Norm and Unitary Conventions*; the invertibility criterion of an element is *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the $2\times2$ model is *$M_2(\mathbb{C})$ Pauli Representation*.

## The Two Maps

### Definition and Linearity

**Definition.** For $\tilde Q\in\mathbb{B}$, the **left regular operator** and the **right regular operator** of $\tilde Q$ are

$$
L_{\tilde Q}(X)=\tilde QX,\qquad R_{\tilde Q}(X)=X\tilde Q .
$$

The product is the algebra product; in the left operator the parameter is written on the left of the argument, and in the right operator on the right.

**Proposition (linearity).** Both operators are complex-linear, and both assignments $\tilde Q\mapsto L_{\tilde Q}$ and $\tilde Q\mapsto R_{\tilde Q}$ are complex-linear:

$$
L_{\lambda\tilde Q+\mu\tilde Q_2}=\lambda L_{\tilde Q}+\mu L_{\tilde Q_2},\qquad
R_{\lambda\tilde Q+\mu\tilde Q_2}=\lambda R_{\tilde Q}+\mu R_{\tilde Q_2}.
$$

*Proof.* $\tilde Q(X+\lambda Y)=\tilde QX+\lambda\tilde QY$ and $(X+\lambda Y)\tilde Q=X\tilde Q+\lambda Y\tilde Q$, by distributivity and the complex bilinearity of the product. The two displays in the parameter are the same computation on the other side.

**The units.** $L_{e_t}=R_{e_t}=\mathrm{id}$, because $e_tX=Xe_t=X$, and the zero element gives the zero operator in both families.

**The two families.** The images of the two maps are the sets $\operatorname{End}_L(\mathbb{B})=\{L_{\tilde Q}\}$ and $\operatorname{End}_R(\mathbb{B})=\{R_{\tilde Q}\}$, named in *Operator Family Conventions*. Each is a subset of the ambient operator space, and each map is a map from the algebra onto its set.

### Injectivity

**Proposition (injectivity, both families).** Each map is injective: $L_{\tilde Q}=L_{\tilde Q_2}$ forces $\tilde Q=\tilde Q_2$, and $R_{\tilde Q}=R_{\tilde Q_2}$ forces $\tilde Q=\tilde Q_2$. In particular $L_{\tilde Q}=0$ exactly when $\tilde Q=0$, and the same for $R$.

*Proof.* Evaluate at the unit: $L_{\tilde Q}(e_t)=\tilde Qe_t=\tilde Q$, and $R_{\tilde Q}(e_t)=e_t\tilde Q=\tilde Q$. In each family the operator returns its parameter at $e_t$, so equal operators have equal values there.

**The reading.** The unit is a faithful probe on both sides, and this single observation carries the article: it makes each family a copy of the algebra rather than a quotient of it, it gives the inverse map on the image, and it is the step that identifies a commuting operator in §*The Two Centralisers*.

### The Two Readings Are Not the Same Operator

**The asymmetry.** The two probes agree at the unit and nowhere else in general, because the algebra is not commutative. For a noncentral $\tilde Q$ the operators $L_{\tilde Q}$ and $R_{\tilde Q}$ differ, and they differ in the strongest available way: their difference is the inner derivation $\operatorname{ad}_{\tilde Q}=L_{\tilde Q}-R_{\tilde Q}$ of *The Endomorphisms of the Biquaternion Algebra*, which is nonzero for a noncentral $\tilde Q$ and vanishes exactly on the centre $\mathbb{C}\cdot e_t$.

**What the readings recover.** A left multiplication is recovered from its value at the unit read on the left, and a right multiplication from the same value read on the right. The two readings recover the same element, so the two families carry the same four complex parameters; the operators they carry are different, and the difference is the noncommutativity.

## The Two Laws

### $L_{\tilde Q}L_{\tilde Q_2}=L_{\tilde Q\tilde Q_2}$ and $R_{\tilde Q}R_{\tilde Q_2}=R_{\tilde Q_2\tilde Q}$

**Theorem (the two laws).** For all $\tilde Q,\tilde Q_2\in\mathbb{B}$,

$$
L_{\tilde Q}L_{\tilde Q_2}=L_{\tilde Q\tilde Q_2},\qquad R_{\tilde Q}R_{\tilde Q_2}=R_{\tilde Q_2\tilde Q}.
$$

*Proof.* For every $X$, $(L_{\tilde Q}L_{\tilde Q_2})(X)=\tilde Q(\tilde Q_2X)=(\tilde Q\tilde Q_2)X=L_{\tilde Q\tilde Q_2}(X)$, and $(R_{\tilde Q}R_{\tilde Q_2})(X)=(X\tilde Q_2)\tilde Q=X(\tilde Q_2\tilde Q)=R_{\tilde Q_2\tilde Q}(X)$. Both are associativity and nothing else.

**The representation and the anti-representation.** The first law says that $\tilde Q\mapsto L_{\tilde Q}$ is a homomorphism of complex algebras, the **left regular representation** of $\mathbb{B}$. The second says that $\tilde Q\mapsto R_{\tilde Q}$ reverses the order of the product, so it is an **anti-homomorphism**, an anti-isomorphism onto its image by §*Injectivity*. The order is reversed, not the multiplication table: in $R_{\tilde Q}R_{\tilde Q_2}=R_{\tilde Q_2\tilde Q}$ the operator applied first is the rightmost, and its parameter stands on the right of the subscript.

**The repair.** The assignment $\tilde Q\mapsto R_{\tilde Q^{\natural}}$ is a representation, because $R_{\tilde Q^{\natural}}R_{\tilde Q_2^{\natural}}=R_{\tilde Q_2^{\natural}\tilde Q^{\natural}}=R_{(\tilde Q\tilde Q_2)^{\natural}}$. The natural conjugation converts the anti-representation into a representation at the cost of one more map. This article keeps the anti-representation, because the reversal is the point: it is the reversal that the composition law of the two-sided family inherits, and it is the reason the second factor of the enveloping algebra carries an $\mathrm{opp}$.

**The unit and the powers.** $L_{e_t}=R_{e_t}=\mathrm{id}$, and $L_{\tilde Q^n}=(L_{\tilde Q})^n$ and $R_{\tilde Q^n}=(R_{\tilde Q})^n$ for every $n\geq0$. For a unit $\tilde Q$ the inverse law of §*The Inverse* extends both identities to the negative powers.

### The Two Copies

**Theorem (the two images).** $\operatorname{End}_L(\mathbb{B})$ is a subalgebra of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ isomorphic to $\mathbb{B}$, and $\operatorname{End}_R(\mathbb{B})$ is a subalgebra isomorphic to $\mathbb{B}_{\mathrm{opp}}$. Each has complex dimension four.

*Proof.* Each image is closed under addition and scalar multiplication by the linearity of the two maps, and under composition by its law; each contains the identity $L_{e_t}=R_{e_t}$; each map is injective, so it is an isomorphism onto its image. The complex dimension is that of the algebra, which is four.

**The opposite algebra.** The **opposite algebra** $\mathbb{B}_{\mathrm{opp}}$ is the algebra with the same underlying vector space and the product $\tilde Q\cdot\tilde Q_2=\tilde Q_2\tilde Q$. The identity map on the underlying space turns the anti-homomorphism $\tilde Q\mapsto R_{\tilde Q}$ into a homomorphism $\mathbb{B}_{\mathrm{opp}}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, and the second half of the theorem is the first half read through it.

**What a copy preserves.** Each copy preserves every polynomial relation of its algebra, with the order of the factors reversed in the right copy: a relation holds in $\mathbb{B}$ exactly when the relation with the factors reversed holds in $\operatorname{End}_R(\mathbb{B})$. Neither copy preserves the trace or the determinant of an element: both regular matrices have trace $2\operatorname{tr}\mathsf M_2(\tilde Q)$ and determinant $\langle\tilde Q\rangle_{\natural}^{2}$, because each is the identity on one tensor factor and the $2\times2$ model on the other. The spectrum is the one invariant that survives, as a set with every multiplicity doubled, and the matrix articles compute the rest.

**What a copy does not contain.** Each copy has complex dimension four, while the ambient space has complex dimension sixteen. Neither is the whole space, and neither is the other: the two copies meet only in the scalars, a statement proved in §*The Intersection*.

## Kernel and Image

### The Two Annihilators

**Definition.** For $\tilde Q\in\mathbb{B}$, the **right annihilator** and the **left annihilator** are

$$
\operatorname{Ann}_r(\tilde Q)=\{X:\tilde QX=0\},\qquad
\operatorname{Ann}_l(\tilde Q)=\{X:X\tilde Q=0\}.
$$

Each is a complex subspace of $\mathbb{B}$.

**Proposition (the two kernels).** $\ker L_{\tilde Q}=\operatorname{Ann}_r(\tilde Q)$ and $\ker R_{\tilde Q}=\operatorname{Ann}_l(\tilde Q)$.

*Proof.* $L_{\tilde Q}(X)=0$ is $\tilde QX=0$, and $R_{\tilde Q}(X)=0$ is $X\tilde Q=0$; each is the defining condition of its annihilator.

**The three cases.** The complex dimension of either annihilator is read in the $2\times2$ model of *$M_2(\mathbb{C})$ Pauli Representation*, where $\tilde Q$ is a $2\times2$ matrix and $X\tilde Q=0$ says that every row of $X$ is a left null vector of $\tilde Q$:

- if $\tilde Q$ is a unit, both annihilators are $0$, of complex dimension $0$;
- if $\tilde Q\neq0$ and $\langle\tilde Q\rangle_{\natural}=0$, the matrix has rank one, its null space is a line, and each annihilator is the complex two-dimensional space of matrices whose rows, respectively columns, lie in that line;
- if $\tilde Q=0$, both annihilators are the whole algebra, of complex dimension $4$.

**The annihilators are not a line.** In the middle case each annihilator has complex dimension two, one complex dimension for each row or column. The kernel of a rank-one matrix acting on the right is a two-dimensional space of matrices, not a line of vectors.

**The two annihilators differ.** They coincide at the units and at the zero element, and they differ for a general zero divisor. At $\tilde Q=\tilde\Pi_+$ the left annihilator is the space of matrices with first column zero and the right annihilator the space of matrices with first row zero: the matrix unit $E_{21}$ lies in the second and not in the first. The two words are therefore kept apart: the name of an annihilator records the side on which the argument stands, which is opposite to the side of the multiplication.

### The Two Ideals

**Definition.** The images of the two operators are

$$
\operatorname{im}L_{\tilde Q}=\tilde Q\mathbb{B}=\{\tilde QX:X\in\mathbb{B}\},\qquad
\operatorname{im}R_{\tilde Q}=\mathbb{B}\tilde Q=\{X\tilde Q:X\in\mathbb{B}\},
$$

the **right ideal** and the **left ideal** generated by $\tilde Q$.

**Proposition (the two images).** $\operatorname{im}L_{\tilde Q}=\tilde Q\mathbb{B}$ and $\operatorname{im}R_{\tilde Q}=\mathbb{B}\tilde Q$.

*Proof.* Each image is the set of the values of its operator, which is the definition of the corresponding ideal.

**The three cases.** In the same $2\times2$ model:

- if $\tilde Q$ is a unit, both ideals are $\mathbb{B}$, of complex dimension $4$;
- if $\tilde Q\neq0$ and $\langle\tilde Q\rangle_{\natural}=0$, each ideal is the complex two-dimensional space of matrices whose columns, respectively rows, lie in the line of $\tilde Q$;
- if $\tilde Q=0$, both images are $0$.

**The side of the ideal is not the side of the multiplication.** A left multiplication generates a right ideal, $(\tilde Q\mathbb{B})\mathbb{B}\subseteq\tilde Q\mathbb{B}$, and a right multiplication generates a left ideal, $\mathbb{B}(\mathbb{B}\tilde Q)\subseteq\mathbb{B}\tilde Q$. The two ideals differ for a general zero divisor, as the two annihilators do, and the mirror of every statement of this subsection is the statement of the other side.

### The Rank

**Theorem (the rank).** For every element, the two operators have the same rank:

$$
\operatorname{rank}L_{\tilde Q}=\operatorname{rank}R_{\tilde Q}=
\begin{cases}
4, & \tilde Q\ \text{a unit},\\
2, & \tilde Q\neq0\ \text{and}\ \langle\tilde Q\rangle_{\natural}=0,\\
0, & \tilde Q=0.
\end{cases}
$$

*Proof.* The rank is the complex dimension of the image, computed in §*The Two Ideals*: four, two and zero in the three cases. Equivalently it is $4-\dim\operatorname{Ann}$, by rank-nullity, and the three annihilator dimensions are $0$, $2$ and $4$.

**The two complex dimensions add up.** A nonzero zero divisor has a complex two-dimensional ideal and a complex two-dimensional annihilator on each side, and the two complex dimensions add to four. A general element is a unit, so the generic rank is four and the degenerate ranks are two and zero.

**One rank, two operators.** The rank depends on the element and not on the side, so the two families carry the same trichotomy. It is not the norm: the rank takes three values, the norm is a complex number, and the two are related only by the criterion of §*The Criterion*.

## Invertibility

### The Criterion $\langle\tilde Q\rangle_{\natural}\neq0$

**Theorem (the criterion, both families).** $L_{\tilde Q}$ is invertible exactly when $\langle\tilde Q\rangle_{\natural}\neq0$, and so is $R_{\tilde Q}$.

*Proof.* If $L_{\tilde Q}$ is invertible it is surjective, so there is an $X$ with $\tilde QX=e_t$; then $\tilde Q$ has a right inverse, and in a finite-dimensional algebra a one-sided inverse is two-sided, so $\tilde Q$ is a unit and $\langle\tilde Q\rangle_{\natural}\neq0$. The converse is the inverse law of §*The Inverse*. The proof for $R_{\tilde Q}$ uses $X\tilde Q=e_t$ and a left inverse, and is otherwise the same.

**The letter of the norm.** The norm is the letter $N$ of *Norm and Unitary Conventions*, and its value at the element is written $\langle\tilde Q\rangle_{\natural}$ in the computations below, as in the three matrix articles of the group.

**The criterion read on the element.** The condition $\langle\tilde Q\rangle_{\natural}\neq0$ is the invertibility criterion of the algebra, fixed in *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, §*Regular and Degenerate Biquaternions*: the units are exactly the elements of nonzero quaternionic norm. The operator criterion and the element criterion are one criterion, read on two objects, and the same sentence serves the two families.

**The determinant reading.** In the matrix articles the determinant of each operator is $\langle\tilde Q\rangle_{\natural}^{2}$, so the criterion is also $\det L_{\tilde Q}=\det R_{\tilde Q}\neq0$. The square is not an accident: each regular matrix is the identity on one tensor factor and the $2\times2$ model on the other, and its determinant is the square of the $2\times2$ determinant.

### The Inverse

**Theorem (the inverse, both families).** If $\tilde Q$ is a unit, then

$$
(L_{\tilde Q})^{-1}=L_{\tilde Q^{-1}},\qquad (R_{\tilde Q})^{-1}=R_{\tilde Q^{-1}}.
$$

*Proof.* $L_{\tilde Q}L_{\tilde Q^{-1}}=L_{\tilde Q\tilde Q^{-1}}=L_{e_t}=\mathrm{id}$ and $R_{\tilde Q}R_{\tilde Q^{-1}}=R_{\tilde Q^{-1}\tilde Q}=R_{e_t}=\mathrm{id}$, with the other side in each case by the law of its family.

**The inverse is in the family.** The inverse of a regular operator is the regular operator of the inverse element, so each family is closed under inversion and the operator inverse is the algebra inverse read on the operator. The norm of the inverse is $\langle\tilde Q^{-1}\rangle_{\natural}=1/\langle\tilde Q\rangle_{\natural}$, which shows that the inverse element exists exactly where the criterion holds.

## The Exchange $S$

The two families are not related by a conjugation that keeps the parameter, because one is a representation and the other an anti-representation. They are related by a **transpose** in a frame adapted to the matrix units, and each is carried onto the other by a fixed involution of the carrier that belongs to neither family.

### The Operator $S$

**Definition.** The **exchange** is the linear involution of $\mathbb{B}$ that fixes the two idempotents and exchanges the two mixed Peirce units:

$$
S\tilde\Pi_\pm=\tilde\Pi_\pm,\qquad S\vec\Upsilon_+=\vec\Upsilon_-,\qquad S\vec\Upsilon_-=\vec\Upsilon_+ .
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

**The glyph.** The matrix articles and *Matrix Representations Conventions* write the same involution $\mathsf P$, and call it the exchange; the letter $S$ is kept here because $P$ is the letter of the plain norm in *Product and Form Conventions*, and because the article needs one glyph for the operator and another for its two displays.

**The invariants.** $S^2=\mathrm{id}$, $S^{\mathsf T}=S=S^{-1}$, $\operatorname{tr}S=2$ and $\det S=-1$. The trace is the complex dimension of the fixed space, the span of $\tilde\Pi_+$ and $\tilde\Pi_-$; the determinant is $-1$ because the two mixed coordinates are exchanged.

### The Flip of the Two Mixed Units

**The tensor reading.** In the Peirce frame the carrier is the tensor product of the two Peirce columns,

$$
\tilde\Pi_+=e_1\otimes e_1,\quad \vec\Upsilon_+=e_2\otimes e_1,\quad \vec\Upsilon_-=e_1\otimes e_2,\quad \tilde\Pi_-=e_2\otimes e_2,
$$

and $S$ is the flip of the two factors: it fixes $e_1\otimes e_1$ and $e_2\otimes e_2$ and exchanges $e_1\otimes e_2$ with $e_2\otimes e_1$. The two mixed units are exactly the two off-diagonal tensor basis elements, and the exchange of the two mixed units is the flip. The name of the operator records the two elements it moves.

**The element-level display.** The flip is the transpose of the $2\times2$ model: for every $\tilde Q$,

$$
\mathsf M_2(S\tilde Q)=\mathsf M_2(\tilde Q)^{\mathsf T},
$$

so the element $S\tilde Q$ is the element whose matrix is the transpose of the matrix of $\tilde Q$. The norm is unchanged, $\langle S\tilde Q\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}$, because a determinant does not see the transpose.

### The Matrix Identity $\mathsf P\,L_{\mathrm{pau}}(\tilde Q)^{\mathsf T}\mathsf P^{-1}=R_{\mathrm{pau}}(\tilde Q)$

**Theorem (the exchange).** In the canonical Peirce frame, for every $\tilde Q\in\mathbb{B}$,

$$
R_{\mathrm{pau}}(\tilde Q)=\mathsf P\,L_{\mathrm{pau}}(\tilde Q)^{\mathsf T}\,\mathsf P^{-1},
$$

with $\mathsf P$ the Peirce display of the exchange, the permutation of the second and third coordinates.

*Proof.* In this frame $L_{\mathrm{pau}}(\tilde Q)=\mathrm I_2\otimes\mathsf M_2(\tilde Q)$, by §*The One-Sided Operators* of *$M_4(\mathbb{C})$ Pauli Representation : Operators*. The transpose of a tensor product is the tensor product of the transposes, and $\mathrm I_2^{\mathsf T}=\mathrm I_2$, so $L_{\mathrm{pau}}(\tilde Q)^{\mathsf T}=\mathrm I_2\otimes\mathsf M_2(\tilde Q)^{\mathsf T}$. The flip conjugates $A\otimes B$ to $B\otimes A$, so

$$
\mathsf P\,L_{\mathrm{pau}}(\tilde Q)^{\mathsf T}\,\mathsf P^{-1}=\mathsf M_2(\tilde Q)^{\mathsf T}\otimes\mathrm I_2=R_{\mathrm{pau}}(\tilde Q),
$$

the last equality being the matrix of a right multiplication in the same frame.

**The transpose is a frame-dependent reading.** A transpose is not an invariant of an operator: it depends on the frame. Each frame of the group carries its own involution and its own stitch, and the two pairs are the two readings of one fact:

$$
L_{\mathrm{pau}}(\tilde X)^{\mathsf T}=L_{\mathrm{pau}}(S\tilde X),\qquad
L_{\mathrm{axf}}(\tilde X)^{\mathsf T}=L_{\mathrm{axf}}(\tilde X^{\natural}),
$$

and

$$
R_{\mathrm{pau}}(\tilde Q)=\mathsf P\,L_{\mathrm{pau}}(\tilde Q)^{\mathsf T}\,\mathsf P^{-1},\qquad
R_{\mathrm{axf}}(\tilde Q)=D\,L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}D,
$$

with $\mathsf P$ the permutation above and $D=\operatorname{diag}(1,-1,-1,-1)$ the display of the natural conjugation in the coefficient basis. **The conjugating matrix is the involution that the transpose implements there:** the Peirce transpose implements the exchange and conjugates by $\mathsf P$, the coefficient transpose implements the natural conjugation and conjugates by $D$. The coefficient frame therefore does not serve the exchange, because $\operatorname{diag}(1,1,-1,1)$ is the display of $S$ there and not the matrix of the coefficient transpose. The matrix articles call this passage the stitch; §*The Stitch Between the Copies* of *$M_4(\mathbb{C})$ Axis-Free Representation : Operators* proves the coefficient pair entry by entry, and §*The One-Sided Operators* of *$M_4(\mathbb{C})$ Pauli Representation : Operators* proves the Peirce pair.

**The sign on the $y$ generator.** With $\mathsf M_2(\vec e_y)=-i\sigma_2=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, the transpose is

$$
\mathsf M_2(\vec e_y)^{\mathsf T}=+i\sigma_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$

and the right regular matrix is $R_{\vec e_y}=+i\sigma_2\otimes\mathrm I_2$, with no minus. The sign comes from $\sigma_2^{\mathsf T}=-\sigma_2$: the transpose of $-i\sigma_2$ is $-i\sigma_2^{\mathsf T}=+i\sigma_2$.

### What the Exchange Does to the Families

**Proposition (the conjugation).** For every $\tilde Q\in\mathbb{B}$,

$$
S\,L_{\tilde Q}\,S^{-1}=R_{S\tilde Q}.
$$

*Proof.* In the Peirce frame the display of $S$ is the permutation $\mathsf P$, and the flip conjugates $A\otimes B$ to $B\otimes A$, so $\mathsf P\,L_{\mathrm{pau}}(\tilde Q)\,\mathsf P^{-1}=\mathsf M_2(\tilde Q)\otimes\mathrm I_2$. The matrix of $S\tilde Q$ is $\mathsf M_2(\tilde Q)^{\mathsf T}$ by §*The Flip of the Two Mixed Units*, so $\mathsf M_2(\tilde Q)\otimes\mathrm I_2=\mathsf M_2(S\tilde Q)^{\mathsf T}\otimes\mathrm I_2=R_{\mathrm{pau}}(S\tilde Q)$.

**The reading.** The exchange carries the left family onto the right family and back, conjugating each left multiplier into a right multiplier of the transposed element. It is a conjugacy of the two sets and not of the two algebras: it does not turn the representation into the anti-representation by an algebra map, and $S\tilde Q$ is not $\tilde Q$ in general. The two families are therefore the same set of operators seen through a fixed involution of the carrier.

**The membership.** $S$ is in neither family. If it were a left multiplication it would be $L_{S e_t}$ by the unit probe, that is $L_{e_t}=\mathrm{id}$, which it is not; the same argument on the right gives the same conclusion. The exchange is an operator of the ambient space outside both copies, and it is the reason the two copies are described as mirror images rather than as equal sets.

### What $S$ Is Not

**Not an algebra map.** $S$ is a linear involution of the carrier and it is not multiplicative: $S(\vec e_x\vec e_y)=S(\vec e_z)=\vec e_z$, while $S(\vec e_x)S(\vec e_y)=\vec e_x(-\vec e_y)=-\vec e_z$.

**Not a one-sided multiplication.** A left multiplication that fixes $e_t$ is the identity, because $L_{\tilde Q}(e_t)=\tilde Q$; so is a right multiplication, because $R_{\tilde Q}(e_t)=\tilde Q$. The operator $S$ fixes $e_t$ and is not the identity, so it is neither.

**Not the natural conjugation.** The natural conjugation negates all three vector units; the exchange negates only $\vec e_y$. The two are different involutions of the carrier: the natural conjugation is an anti-automorphism, and the exchange is not multiplicative at all.

## The Two Families Together

### The Commutation $L_{\tilde Q}R_{\tilde Q_2}=R_{\tilde Q_2}L_{\tilde Q}$

**Theorem (the commutation).** For all $\tilde Q,\tilde Q_2\in\mathbb{B}$,

$$
L_{\tilde Q}R_{\tilde Q_2}=R_{\tilde Q_2}L_{\tilde Q}.
$$

*Proof.* For every $X$, $(L_{\tilde Q}R_{\tilde Q_2})(X)=\tilde Q(X\tilde Q_2)=\tilde QX\tilde Q_2$ and $(R_{\tilde Q_2}L_{\tilde Q})(X)=(\tilde QX)\tilde Q_2=\tilde QX\tilde Q_2$. The two values are equal by associativity.

**The reading.** The identity is associativity and nothing else: the left multiplication acts on the left factor, the right multiplication on the right factor, and the two actions do not interfere. With the two laws it says that the algebra is a bi-module over the pair, with the left copy acting on the left and the right copy on the right; the module axiom is exactly this commutation, and it is the reason a two-sided operator can be built from two independent parameters without a compatibility condition between them.

**The order of a mixed product.** A product of a left and a right operator may be written in either order, so it is determined by the pair of parameters and not by the order of the two factors.

### The Two Centralisers

**Theorem (the commutant of the left copy).** An operator $T\in\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ commutes with every left multiplication exactly when it is a right multiplication:

$$
L(\mathbb{B})'=R(\mathbb{B}).
$$

*Proof.* If $T=R_{\tilde Q_2}$, then $TL_{\tilde Q}=R_{\tilde Q_2}L_{\tilde Q}=L_{\tilde Q}R_{\tilde Q_2}=L_{\tilde Q}T$ by the commutation, so $R(\mathbb{B})\subseteq L(\mathbb{B})'$. Conversely let $T$ commute with every $L_{\tilde Q}$. For every $\tilde Q$,

$$
T(\tilde Q)=T(L_{\tilde Q}e_t)=L_{\tilde Q}T(e_t)=\tilde Q\,T(e_t),
$$

so with $\tilde Q_2=T(e_t)$ one has $T(\tilde Q)=\tilde Q\tilde Q_2=R_{\tilde Q_2}(\tilde Q)$ for every $\tilde Q$, and $T=R_{\tilde Q_2}$.

**Theorem (the commutant of the right copy).** The same statement with the sides exchanged:

$$
R(\mathbb{B})'=L(\mathbb{B}).
$$

*Proof.* If $T=L_{\tilde Q}$ then $TR_{\tilde Q_2}=L_{\tilde Q}R_{\tilde Q_2}=R_{\tilde Q_2}L_{\tilde Q}=R_{\tilde Q_2}T$. Conversely, if $T$ commutes with every $R_{\tilde Q_2}$, then

$$
T(\tilde Q_2)=T(R_{\tilde Q_2}e_t)=R_{\tilde Q_2}T(e_t)=T(e_t)\tilde Q_2,
$$

so with $\tilde Q=T(e_t)$ one has $T=L_{\tilde Q}$.

**The proof read once.** The unit is the probe and the identity is the same in both directions: an operator that commutes with a whole family is determined by its value at $e_t$, and that value is a parameter of the other family. The two proofs are one proof with the sides exchanged.

**The exactness.** The two equalities are exact, not containments up to a scalar, and they hold for every element, including the zero divisors. The two families are as large as two commuting families can be: an operator commuting with both is a scalar, by §*The Intersection*.

### The Intersection $L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\cdot\mathrm I_4$

**Theorem (the intersection).** An operator that is both a left multiplication and a right multiplication is a scalar multiple of the identity:

$$
L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\cdot\mathrm I_4 .
$$

*Proof.* Let $L_{\tilde Q}=R_{\tilde Q_2}$. Evaluating at the unit gives $\tilde Q=L_{\tilde Q}(e_t)=R_{\tilde Q_2}(e_t)=\tilde Q_2$, so the operator is $L_{\tilde Q}=R_{\tilde Q}$, and then $\tilde QX=X\tilde Q$ for every $X$: the element $\tilde Q$ is central. The centre of the biquaternion algebra is $\mathbb{C}\cdot e_t$ by *The Biquaternion Algebra*, §*The Scalars Are the Centre*, so $\tilde Q=\lambda e_t$ and the operator is $\lambda\mathrm I_4$. Conversely every $\lambda\mathrm I_4$ is $L_{\lambda e_t}$ and $R_{\lambda e_t}$.

**The three steps.** Equality at the unit gives the same parameter; the equality of the two operators then gives a central element; the centre of the algebra gives a scalar. Each step is a different statement, and the third uses the structure of the algebra and not only its multiplication.

**The scalar is the only freedom.** The intersection is the line spanned by $\mathrm I_4$, of complex dimension one, which is the complex dimension of the centre. The parameter is the central element $\lambda e_t$, the same number on both sides.

### The Incomparability and the Sum

**Neither copy contains the other.** For a noncentral $\tilde Q$, the left multiplication $L_{\tilde Q}$ is not a right multiplication and conversely, by §*The Intersection*. The two copies are therefore incomparable, and the distinction between them is the noncommutativity of the algebra.

**The sum.** The two copies are each of complex dimension four and meet in a line, so their linear sum has complex dimension seven. The sum is a subspace and is not a subalgebra: the product $L_{\vec e_x}R_{\vec e_x}$ is not of the form $L_{\tilde A}+R_{\tilde B}$, as *Operators Acting 2 Side*, §*The Sum Is Not a Subalgebra* proves. The two families generate, under addition, a seven-dimensional subspace, and under composition they generate the whole sixteen-dimensional operator space.

**The lattice of the family.** The scalars, the two one-sided families, the seven-dimensional sum and the ambient space form the chain

$$
\mathbb{C}\cdot\mathrm I_4\ \subset\ \operatorname{End}_L(\mathbb{B}),\ \operatorname{End}_R(\mathbb{B})\ \subset\ \operatorname{End}_L(\mathbb{B})+\operatorname{End}_R(\mathbb{B})\ \subset\ \operatorname{End}_{\mathbb{C}}(\mathbb{B}),
$$

of complex dimensions $1$, $4$ (twice, incomparable), $7$ and $16$. Beyond the chain sit the cone of the two-sided operators, which is not a subspace, and the envelope of the pair of actions; both are the subject of the following articles of the group.

## A Worked Example at a Zero Divisor

**The element.** Take $\tilde Q=\tilde\Pi_+$, the idempotent whose matrix is $E_{11}$ in the Peirce frame $(\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-)$. Its norm is zero and it is not the zero element, so every statement of the article is in its middle case.

**The two matrices.** Left multiplication by $E_{11}$ keeps the first row of $X$ and kills the second; right multiplication keeps the first column and kills the second. In the Peirce frame,

$$
[L_{\tilde\Pi_+}]=\operatorname{diag}(1,0,1,0),\qquad [R_{\tilde\Pi_+}]=\operatorname{diag}(1,1,0,0).
$$

Both are diagonal and their diagonals differ, so the two operators agree on $\tilde\Pi_+$ and on no other basis element.

**The kernels and the images.** The kernel of the left operator is the space of matrices with first row zero, $\operatorname{span}\{\vec\Upsilon_+,\tilde\Pi_-\}$, and its image is the right ideal $\tilde\Pi_+\mathbb{B}$ of the matrices whose only possible nonzero row is the first, $\operatorname{span}\{\tilde\Pi_+,\vec\Upsilon_-\}$. The kernel of the right operator is the space of matrices with first column zero, $\operatorname{span}\{\vec\Upsilon_-,\tilde\Pi_-\}$, and its image is the left ideal $\operatorname{span}\{\tilde\Pi_+,\vec\Upsilon_+\}=\mathbb{B}\tilde\Pi_+$.

**The two kernels differ.** The mixed unit $\vec\Upsilon_+$ is in the kernel of the left operator, because $\tilde\Pi_+\vec\Upsilon_+=0$, and it is not in the kernel of the right operator, because $\vec\Upsilon_+\tilde\Pi_+=\vec\Upsilon_+$. This is the example of §*The Two Annihilators* in the Peirce frame instead of the matrix frame, and it shows that the two annihilators are different subspaces of the same complex dimension two.

**The rank and the inverse.** Both matrices have rank $2$ and determinant $0$, consistent with $\operatorname{rank}=2$ and $\langle\tilde\Pi_+\rangle_{\natural}=0$; nullity and rank add to $4$ on each side. Neither operator is invertible, and neither has an inverse in its family, because the element is not a unit.

**The exchange on the example.** The element is fixed by $S$, so the conjugation of §*What the Exchange Does to the Families* reads $SL_{\tilde\Pi_+}S^{-1}=R_{\tilde\Pi_+}$. On the matrices the same statement is the exchange of the second and third diagonal entries: $S\operatorname{diag}(1,0,1,0)S^{-1}=\operatorname{diag}(1,1,0,0)$, which is the transpose identity of §*The Matrix Identity $R_{\mathrm{pau}}(\tilde Q)=\mathsf P\,L_{\mathrm{pau}}(\tilde Q)^{\mathsf T}\mathsf P^{-1}$* on a diagonal matrix.

## Summary

The two regular operators of $\tilde Q$ are $L_{\tilde Q}(X)=\tilde QX$ and $R_{\tilde Q}(X)=X\tilde Q$. Each assignment is complex-linear and injective, the unit returning the parameter; the left one is multiplicative and the right one anti-multiplicative, so the images are copies of $\mathbb{B}$ and of $\mathbb{B}_{\mathrm{opp}}$, each of complex dimension four, preserving the algebra relations and nothing else.

The kernel of $L_{\tilde Q}$ is the right annihilator and its image the right ideal $\tilde Q\mathbb{B}$; the kernel of $R_{\tilde Q}$ is the left annihilator and its image the left ideal $\mathbb{B}\tilde Q$. The annihilators have complex dimensions $0,2,4$ and so do the ideals, and the rank is $4$, $2$ or $0$, the same on both sides: four for a unit, two for a nonzero zero divisor, zero for the zero element. Each operator is invertible exactly when $\langle\tilde Q\rangle_{\natural}\neq0$, with inverse the operator of $\tilde Q^{-1}$, and $\det=\langle\tilde Q\rangle_{\natural}^{2}$.

In the Peirce frame the display of $S$ is the permutation $\mathsf P$ and the right matrix is the transpose of the left one conjugated by it: $R_{\mathrm{pau}}(\tilde Q)=\mathsf P\,L_{\mathrm{pau}}(\tilde Q)^{\mathsf T}\mathsf P^{-1}$. In the coefficient frame the display of $S$ is the reflection $\operatorname{diag}(1,1,-1,1)$, and there the transpose implements the natural conjugation instead, $R_{\mathrm{axf}}(\tilde Q)=D\,L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}D$ with $D=\operatorname{diag}(1,-1,-1,-1)$. The exchange is an involution of trace $2$ and determinant $-1$; it is not multiplicative, it is in neither family, and it conjugates each family onto the other, $SL_{\tilde Q}S^{-1}=R_{S\tilde Q}$.

The two families commute element by element, $L_{\tilde Q}R_{\tilde Q_2}=R_{\tilde Q_2}L_{\tilde Q}$, each is the exact commutant of the other, $L(\mathbb{B})'=R(\mathbb{B})$ and $R(\mathbb{B})'=L(\mathbb{B})$, and they meet in the scalars, $L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\cdot\mathrm I_4$. The two copies are incomparable and their sum is the complex seven-dimensional subspace that the two families span.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde Q}(X)=\tilde QX$ | The left regular operator |
| $R_{\tilde Q}(X)=X\tilde Q$ | The right regular operator |
| $\operatorname{End}_L(\mathbb{B})=L(\mathbb{B})$ | The set of the left regular operators, a copy of $\mathbb{B}$ |
| $\operatorname{End}_R(\mathbb{B})=R(\mathbb{B})$ | The set of the right regular operators, a copy of $\mathbb{B}_{\mathrm{opp}}$ |
| $\mathbb{B}_{\mathrm{opp}}$ | The opposite algebra, product $\tilde Q\cdot\tilde Q_2=\tilde Q_2\tilde Q$ |
| $\operatorname{Ann}_r(\tilde Q)$, $\operatorname{Ann}_l(\tilde Q)$ | The right and the left annihilators, the kernels of $L$ and $R$ |
| $\tilde Q\mathbb{B}$, $\mathbb{B}\tilde Q$ | The right and the left ideals, the images of $L$ and $R$ |
| $\operatorname{rank}L_{\tilde Q}=\operatorname{rank}R_{\tilde Q}$ | $4$, $2$ or $0$ according to the three cases |
| $S$ | The exchange, fixing $\tilde\Pi_\pm$ and swapping $\vec\Upsilon_\pm$; $\operatorname{diag}(1,1,-1,1)$ in the coefficient frame |
| $R_{\mathrm{pau}}(\tilde Q)=\mathsf P\,L_{\mathrm{pau}}(\tilde Q)^{\mathsf T}\mathsf P^{-1}$ | The exchange, in the Peirce frame |
| $SL_{\tilde Q}S^{-1}=R_{S\tilde Q}$ | The conjugation of the two families |
| $\mathcal{S}'$ | The commutant of the set $\mathcal{S}$ |
| $L(\mathbb{B})'=R(\mathbb{B})$ | The first centraliser |
| $R(\mathbb{B})'=L(\mathbb{B})$ | The second centraliser |
| $L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\cdot\mathrm I_4$ | The intersection, the scalar line |

## Further Reading

- [The Endomorphisms of the Biquaternion Algebra](the-endomorphisms-of-the-biquaternion-algebra.html), for the ambient space, the inner derivations and the natural conjugation.
- [The SVD Decomposition of Endomorphisms of the Biquaternion Algebra](the-svd-decomposition-of-endomorphisms-of-the-biquaternion-algebra.html), for the weights of a one-sided operator and the decomposition of a general endomorphism.
- [Adjoint Pair of $L$ and $R$ Operators](adjoint-pair-of-l-and-r-operators.html), for the association of the two families with the four forms.
- [Operators Acting 2 Side](operators-acting-2-side.html), for the products of the two families, the cone, the generation theorem and the ladder $1,4,7,16$.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the enveloping algebra in which the two copies sit and for the bi-module structure.
- [Hermitian pair of operators acting as 1 side](hermitian-pair-of-operators-acting-as-1-side.html), for the pair $(L_{\tilde Q},L_{\tilde Q^{\natural}})$, its two equations and its closure to a scalar.
- [Hermitian pair of operators acting as 2 side](hermitian-pair-of-operators-acting-as-2-side.html), for the sandwich family and its intersections with the two one-sided families.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the plain form and the invertibility criterion.
- [Matrix Representations Conventions](matrix-representations-conventions.html), for the $4\times4$ regular matrices, the canonical Peirce frame and the change between the frames.
- [Operator Family Conventions](operator-family-conventions.html), for the letters, the slots and the set names.
