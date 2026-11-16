# __Classification of the Structures of the Biquaternion Algebra__

## Introduction

The biquaternion algebra is one multiplication on one underlying set, and that set can be read over $\mathbb{R}$ and over $\mathbb{C}$. The two readings are not the same algebra: the first has real dimension eight, the second complex dimension four, and the second is a full matrix algebra over its own scalars. The structures that connect the two readings, a **real structure** on the complex algebra and a **complex structure** on the real algebra, are the subject of this article, and the article classifies them.

Three results are established. The complex algebra has exactly two real forms up to isomorphism, and their fixed sets are the algebra of the quaternions and the algebra of the real $2\times2$ matrices. The real algebra has exactly one complex structure up to isomorphism, and the corresponding complex algebra is the biquaternion algebra itself. The two questions are asked in opposite directions, and neither answers the other.

The word **structure** is used here in the technical sense of an involution or a scalar action that changes the ground field, and in no other sense. It is not the form of a product: the four forms $P$, $N$, $H$ and $\mathrm{Kr}$ are the scalar parts of the four general products and are classified in [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html). It is not the six remarkable subspaces, which are classified in [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html). And it is not the Lie structure, which reads the commutator as a bracket and belongs to [Biquaternion Lie Group and Exponential Structure](biquaternion-lie-group-and-exponential-structure.html). The distinction is stated once here and used throughout: a structure in this article changes the field of scalars or fixes an involution, and it leaves the multiplication alone.

The general theory of the two operations belongs to [Real Forms and the Descent of an Algebra](real-forms-and-the-descent-of-an-algebra.html), which treats the complexification, the conjugations and the descent of the structure for an arbitrary real algebra. This article does not reproduce it. It states the two notions, cites that article for the general statements, and then does the one thing that article does not do: it computes the classification for $\mathbb{B}$ and identifies the fixed sets by explicit formulas in the corpus coordinates.

The order is as follows. The next section fixes the algebra and the two readings. The third section states the two notions of structure and separates them. The fourth classifies the real structures and proves that the two fixed sets are the quaternions and $M_2(\mathbb{R})$. The fifth classifies the complex structures. The sixth and seventh sections relate the structures to the six subspaces and to the Lie subalgebras. The eighth states what the classification does not decide.

## The Algebra and the Two Ground Fields

**The algebra.** The **biquaternion algebra** $\mathbb{B}$ is the four-dimensional complex algebra with base $e_t,\vec e_x,\vec e_y,\vec e_z$, where $e_t$ is the unit and the three vector units satisfy

$$
\vec e_x^{\,2}=\vec e_y^{\,2}=\vec e_z^{\,2}=-e_t,\qquad
\vec e_x\vec e_y=\vec e_z,\quad \vec e_y\vec e_z=\vec e_x,\quad \vec e_z\vec e_x=\vec e_y .
$$

The construction, the multiplication table and the coordinate rule are in [Introduction to the Algebra of Biquaternions](the-biquaternion-algebra.html). An element is written

$$
\tilde Q=Q_t e_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\qquad Q_\mu\in\mathbb{C},
$$

with scalar part $Q_te_t$ and vector part $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$; a pure element is one with $Q_t=0$, written $\vec Q$. The element, its coordinates and the three coordinate systems are in [The Element, the Coordinates and the Conjugations in the Biquaternion Algebra](the-element-the-coordinates-and-the-conjugations.html).

**The centre.** The centre of $\mathbb{B}$ is the scalar line $\mathbb{C}e_t$, and $\mathbb{B}$ is central simple over $\mathbb{C}$. Both statements are in [Introduction to the Algebra of Biquaternions](the-biquaternion-algebra.html), and both are used below: the centre is what a complex structure must act on, and central simplicity is what makes the classification short.

**The two readings.** The same multiplication with the same structure constants, the constants being integers, is defined over $\mathbb{R}$. Write

$$
\mathbb{B}_{\mathbb{R}}=\mathbb{B}\ \text{read over}\ \mathbb{R},
$$

the eight-dimensional real algebra obtained from $\mathbb{B}$ by forgetting the complex scalars and keeping the multiplication. The two algebras have the same elements, the same products and the same unit, and they differ in the field of scalars. Throughout, $\mathbb{B}$ without a subscript is the complex algebra, which is the corpus convention; the subscripted symbol $\mathbb{B}_{\mathbb{R}}$ is introduced here and used only in this article.

**Remark (the scalar action).** Reading $\mathbb{B}$ over $\mathbb{C}$ means carrying an action of $\mathbb{C}$ that commutes with the multiplication, the action being $\lambda\cdot\tilde Q=\lambda\tilde Q$ on the coefficients. Reading it over $\mathbb{R}$ means forgetting that action and keeping only the real scalars. The operator that carries the action is multiplication by $i e_t$, written $J$ in the corpus and used below.

**The dictionary.** The algebra is the matrix algebra $M_2(\mathbb{C})$ in the base

$$
e_t\mapsto \mathrm{I}_2,\qquad
\vec e_x\mapsto -i\sigma_1,\qquad
\vec e_y\mapsto -i\sigma_2,\qquad
\vec e_z\mapsto -i\sigma_3 ,
$$

where $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices. This is a **dictionary** between two descriptions of one algebra, and not a construction of an operator algebra; the matrices are a display of the multiplication, and every statement below is a statement about elements. The dictionary appears in [$M_2(\mathbb{C})$ Pauli Representation](m2c-pauli-representation.html).

**The three algebras.** The data are collected once.

| Algebra | Ground field | Dimension | Centre |
|---|---|---|---|
| $\mathbb{B}\cong M_2(\mathbb{C})$ | $\mathbb{C}$ | $4$ | $\mathbb{C}e_t$ |
| $\mathbb{B}_{\mathbb{R}}\cong M_2(\mathbb{C})_{\mathbb{R}}$ | $\mathbb{R}$ | $8$ | $\mathbb{C}e_t$ |
| $\mathbb{B}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$ | $\mathbb{C}$ | $8$ | $\mathbb{C}\oplus\mathbb{C}$ |

The third row is the complexification, which is a larger algebra than $\mathbb{B}$ and is treated in the next section only to be distinguished from the complex structure.

## The Two Notions of Structure

### Real Structures of the Complex Algebra

**Definition.** A **real structure** on a complex algebra $A$ is a conjugate-linear map $\sigma:A\to A$ with

$$
\sigma^2=\mathrm{id},\qquad \sigma(XY)=\sigma(X)\sigma(Y),\qquad \sigma(\lambda X)=\bar\lambda\,\sigma(X).
$$

Its **real form** is the fixed set

$$
A^{\sigma}=\{X\in A:\sigma(X)=X\},
$$

a real subalgebra of $A$ whose complexification is $A$:

$$
A^{\sigma}\otimes_{\mathbb{R}}\mathbb{C}\cong A .
$$

The correspondence is a bijection: every real subalgebra $A_0$ of $A$ with $A_0\otimes_{\mathbb{R}}\mathbb{C}\cong A$ is the fixed set of exactly one real structure, namely the conjugate-linear map that is the identity on $A_0$ and minus the identity on $iA_0$. The general statement, with the descent of ideals, quotients, automorphisms and derivations, is [Real Forms and the Descent of an Algebra](real-forms-and-the-descent-of-an-algebra.html).

**Remark (the two terms are not the same).** A real structure is a map; a real form is a subalgebra. The map determines the subalgebra as its fixed set, and the subalgebra determines the map because $A=A_0\oplus iA_0$. The word **form** in the literature is used for both, and this article names the map whenever the distinction matters.

### Complex Structures of the Real Algebra

**Definition.** A **complex structure** on a real algebra $A_0$ is a unital $\mathbb{R}$-algebra homomorphism

$$
\kappa:\mathbb{C}\longrightarrow Z(A_0),
$$

that is, a point of the centre isomorphic to $\mathbb{C}$ through which $\mathbb{C}$ acts on $A_0$ by multiplication. Equivalently, it is a real-linear map $J:A_0\to A_0$ with

$$
J^2=-\mathrm{id},\qquad J(XY)=J(X)Y=XJ(Y),
$$

the second condition saying that $J$ is multiplication by a central scalar. The **complex form** attached to $\kappa$ is $A_0$ with the scalars of $\mathbb{C}$ acting through $\kappa$; it is a complex algebra whose restriction of scalars is $A_0$.

**Remark (why centrality is in the definition).** The equation $J(XY)=J(X)Y$ fails for an operator that is not central, and such an operator defines a real-linear endomorphism and not a change of scalars. The complex structure of the biquaternion algebra is the operator $J(\tilde Q)=i\tilde Q$, which is central because $i$ is a central scalar; the operator $\tilde Q\mapsto i\tilde Q$ read on the eight real coordinates is the operator $J$ of [The Element, the Coordinates and the Conjugations in the Biquaternion Algebra](the-element-the-coordinates-and-the-conjugations.html), §*The Complex Structure*.

### The Two Questions Are Not Inverse

The two operations run in opposite directions and are not inverse to each other.

| Question | Input | Output |
|---|---|---|
| Real structures of $\mathbb{B}$ | complex algebra, dimension $4$ | real algebras, dimension $4$ |
| Complex structures of $\mathbb{B}_{\mathbb{R}}$ | real algebra, dimension $8$ | complex algebras, dimension $4$ |

$$
\mathbb{B}\ \xrightarrow{\ \sigma\ }\ \mathbb{B}^{\sigma}\ \xrightarrow{\ \otimes_{\mathbb{R}}\mathbb{C}\ }\ \mathbb{B},
\qquad
\mathbb{B}_{\mathbb{R}}\ \xrightarrow{\ \kappa\ }\ \mathbb{B}\ \xrightarrow{\ \text{forget the scalars}\ }\ \mathbb{B}_{\mathbb{R}} .
$$

A real structure acts on $\mathbb{B}$ and produces a real algebra of half the real dimension; the complexification of that real algebra returns $\mathbb{B}$. A complex structure acts on $\mathbb{B}_{\mathbb{R}}$ and produces a complex algebra of half the real dimension; forgetting its scalars returns $\mathbb{B}_{\mathbb{R}}$. Each operation halves the real dimension, and the complexification of a real form returns the algebra it came from, so the two operations are not one operation read in two directions. The two classifications cannot be matched term by term either: there are two real forms and one complex form.

**Warning (a real form is not a real subalgebra).** A real form of $\mathbb{B}$ is the fixed set of a conjugate-linear involution, and its complexification recovers $\mathbb{B}$. An arbitrary real subalgebra of $\mathbb{B}$ need not be a real form: it is a real form exactly when the complex-linear span of its elements is all of $\mathbb{B}$ and its real dimension is four. The subspace $\mathbb{B}_V$ of pure elements is the readiest counterexample, and it fails on both counts. Its real dimension is six and not four. And it is closed under the commutator and not under the product: the product of two pure elements carries a scalar part,

$$
(Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z)(P_x\vec e_x+P_y\vec e_y+P_z\vec e_z)
=-(Q_xP_x+Q_yP_y+Q_zP_z)e_t+\text{(pure part)},
$$

so $\mathbb{B}_V$ is a real Lie subalgebra and a real subspace, and not a real subalgebra of the associative algebra.

## The Two Real Structures

**Theorem.** Up to isomorphism, the complex algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has exactly two real forms, the split algebra and the division algebra:

$$
M_2(\mathbb{R})\qquad\text{and}\qquad \mathbb{H}.
$$

*Proof.* A real structure $\sigma$ is conjugate-linear and involutive, so its fixed algebra $A^{\sigma}$ is a real algebra with $A^{\sigma}\otimes_{\mathbb{R}}\mathbb{C}=\mathbb{B}$; such an algebra is central simple over $\mathbb{R}$ of dimension $4$. By the Wedderburn structure theorem a finite-dimensional central simple algebra over $\mathbb{R}$ is $M_n(D)$ for a division algebra $D$, and by the theorem of Frobenius $D$ is $\mathbb{R}$, $\mathbb{C}$ or $\mathbb{H}$; the case $D=\mathbb{C}$ is excluded because $\mathbb{C}$ is not central over $\mathbb{R}$, and dimension $4$ then leaves $M_2(\mathbb{R})$ and $\mathbb{H}$. So there are at most two. Both occur, as the two structures computed below, and they are not isomorphic, the first having zero divisors and the second not having any. The full argument, including the Skolem–Noether step that every real structure is conjugate to one of the two standard ones, is [The Split Real Form: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$](the-split-real-form-mnr-inside-mnc.html), §*The Two Real Structures*.

**The compact structure.** The **coefficient conjugation** is

$$
\sigma_{\mathrm{comp}}(\tilde Q)=\overline{Q_t}e_t+\overline{Q_x}\vec e_x+\overline{Q_y}\vec e_y+\overline{Q_z}\vec e_z ,
$$

the conjugation $\overline{\phantom{Q}}$ of [The Element, the Coordinates and the Conjugations in the Biquaternion Algebra](the-element-the-coordinates-and-the-conjugations.html). It is conjugate-linear, multiplicative and involutive, and its fixed set is the set of elements with real coefficients,

$$
\mathbb{B}_H=\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_x,\vec e_y,\vec e_z\},
$$

the quaternion subspace, of real dimension four. Every element of $\mathbb{B}_H$ is $\tilde q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ with real coefficients, and $\tilde q\tilde q^{\natural}=(q_t^2+q_x^2+q_y^2+q_z^2)e_t$ is zero only at $\tilde q=0$; the algebra is a division algebra, isomorphic to $\mathbb{H}$, and the isomorphism is the identity on the base. The real form attached to $\sigma_{\mathrm{comp}}$ is therefore the compact one, and its fixed set is one of the six remarkable subspaces.

**The split structure.** The **inner twist** of the coefficient conjugation is

$$
\sigma_{\mathrm{split}}(\tilde Q)=\vec e_y\,\sigma_{\mathrm{comp}}(\tilde Q)\,\vec e_y^{-1}=-\vec e_y\,\overline{\tilde Q}\,\vec e_y ,
$$

using $\vec e_y^{-1}=-\vec e_y$. It is conjugate-linear, multiplicative and involutive, because $\vec e_y$ is invertible and conjugation by an invertible element is an algebra automorphism. Its action on the base is

$$
e_t\mapsto e_t,\qquad \vec e_x\mapsto-\vec e_x,\qquad \vec e_y\mapsto\vec e_y,\qquad \vec e_z\mapsto-\vec e_z,
$$

the coefficients being conjugated at the same time; hence $e_t$, $\vec e_y$, $i\vec e_x$ and $i\vec e_z$ are fixed and the other four basis elements are not. Its fixed set is

$$
\mathbb{B}_{\mathbb{R}}^{\sigma_{\mathrm{split}}}=\operatorname{span}_{\mathbb{R}}\{e_t,\ \vec e_y,\ i\vec e_x,\ i\vec e_z\},
$$

of real dimension four, and it is the algebra $M_2(\mathbb{R})$ in the dictionary of the previous section: the image of these four elements under $\tilde Q\mapsto \mathsf M_2(\tilde Q)$ is $\mathrm{I}_2,\ -i\sigma_2,\ \sigma_1,\ \sigma_3$, a real basis of $M_2(\mathbb{R})$.

**Proof.** The four elements are fixed: $\vec e_y$ commutes with itself, and the conjugation by $\vec e_y$ negates $\vec e_x$ and $\vec e_z$ while fixing $\vec e_y$, as the products $\vec e_y\vec e_x=-\vec e_z$ and $\vec e_y\vec e_z=\vec e_x$ give. The elements $i\vec e_x$ and $i\vec e_z$ are therefore fixed, since the coefficient conjugation negates the $i$ and the inner twist negates the vector unit. The four elements are linearly independent over $\mathbb{R}$ and their span is closed under products, because

$$
\vec e_y\,(i\vec e_x)=-i\vec e_z,\qquad (i\vec e_x)(i\vec e_z)=\vec e_y,\qquad (i\vec e_z)\vec e_y=-i\vec e_x ,
$$

so the span is a real subalgebra contained in the fixed set. For a conjugate-linear involution on an eight-dimensional real space the fixed set has dimension four, since $\sigma(iX)=-i\sigma(X)$ puts $i\,A^{\sigma}$ in the anti-fixed space and $\mathbb{B}_{\mathbb{R}}=A^{\sigma}\oplus iA^{\sigma}$; a four-dimensional subspace of the fixed set is therefore the fixed set. The image under the dictionary is computed on the four basis elements, and the four matrices $\mathrm{I}_2$, $\sigma_1$, $-i\sigma_2$, $\sigma_3$ are real and linearly independent over $\mathbb{R}$.

**Corollary (twisting by an invertible element and the sign).** Let $u\in\mathbb{B}^{\times}$ satisfy $u\bar u\in\mathbb{C}e_t$. Write $u\bar u=\lambda e_t$ with $\lambda\in\mathbb{R}^{\times}$. Then $\operatorname{Ad}_u\circ\sigma_{\mathrm{comp}}$ is a real structure, and its real form is isomorphic to $\mathbb{H}$ when $\lambda>0$ and to $M_2(\mathbb{R})$ when $\lambda<0$. In particular $\sigma_{\mathrm{split}}$ is the twist by $u=\vec e_y$, and $\vec e_y\overline{\vec e_y}=\vec e_y^{2}=-e_t$, so $\lambda=-1$ and the case is the split one; the twist by $u=e_t+\tfrac{i}{2}\vec e_x$ has $u\bar u=\tfrac34e_t$, so $\lambda=\tfrac34$ and the case is the compact one.

*Proof.* In the dictionary, $\sigma_{\mathrm{comp}}$ is the map $A\mapsto \vec e_y\bar A\vec e_y^{-1}$, so the twist by $u$ is the map $A\mapsto v\bar A v^{-1}$ with $v=u\vec e_y$. The conjugating unit is therefore $v$, and the scalar attached to it is

$$
v\bar v=(u\vec e_y)(\bar u\,\bar{\vec e_y})=u\bar u\,\vec e_y\bar{\vec e_y}=-u\bar u=-\lambda e_t ,
$$

using $\vec e_y\bar{\vec e_y}=\vec e_y^{2}=-e_t$. By the criterion of [The Split Real Form: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$](the-split-real-form-mnr-inside-mnc.html), §*The Two Real Structures*, the class is $\mathbb{H}$ when $v\bar v$ is a negative multiple of $e_t$ and $M_2(\mathbb{R})$ when it is a positive multiple. Since $v\bar v=-\lambda e_t$, the first case is $\lambda>0$ and the second is $\lambda<0$. The two witnesses are computed by the products displayed.

**Remark (an inner twist is not a conjugacy of the forms).** The two real structures are related by an inner automorphism, and their real forms are still not isomorphic. The reason is that the fixed set of $\operatorname{Ad}_u\circ\sigma$ is not the image of the fixed set of $\sigma$ under $\operatorname{Ad}_u$: for a conjugate-linear $\sigma$ the relation reads

$$
(\operatorname{Ad}_u\circ\sigma)(X)=X\iff \sigma(X)=u^{-1}Xu ,
$$

and applying $\sigma$ turns the right-hand side into $\sigma(X)=\bar uX\bar u^{-1}$, which is the fixed equation of a different real structure. The twist is therefore invisible on the pair of structures and visible on the pair of forms, and the classification is made by computing the forms.

**The distinguishing test.** The two fixed algebras are separated by an idempotent, and the witness is one element. In the split form the element

$$
P=\tfrac12(e_t+i\vec e_x)
$$

satisfies $P^2=P$ and $P\neq0,e_t$, and the complementary element $e_t-P$ satisfies $P(e_t-P)=0$, so $P$ is a zero divisor. In the compact form the two relations $P^2=P$ and $P(P-e_t)=0$ force $P=0$ or $P=e_t$, because a product of nonzero elements of a division algebra is nonzero. No computation with coordinates is needed for the second statement, and the first is a product of two elements.

**Remark (the obvious guess is wrong).** The coefficient conjugation is the compact structure and not the split one: its fixed set $\mathbb{B}_H$ is the division algebra. The split structure is the coefficient conjugation followed by the inner automorphism of $\vec e_y$, and its fixed set contains $i\vec e_x$ and $i\vec e_z$ rather than $\vec e_x$ and $\vec e_z$. Reading the split form as "the real-coefficient elements" is the standard error, and it is the reason the two structures are computed here rather than quoted.

**Remark (the general pattern).** For $M_n(\mathbb{C})$ the same argument gives the real forms $M_n(\mathbb{R})$ and, for even $n$, $M_{n/2}(\mathbb{H})$; the identification of the second with a fixed set of a twisted conjugation is [The Quaternionic Structure and the Real Forms of $M_4(\mathbb{C})$](the-quaternionic-structure-and-the-real-forms-of-m4c.html) at $n=4$. At $n=2$ the second form is $\mathbb{H}$, which is the compact fixed set above.

## The One Complex Structure

**Theorem.** Up to isomorphism, the real algebra $\mathbb{B}_{\mathbb{R}}$ has exactly one complex structure, and the corresponding complex form is

$$
\mathbb{B}=M_2(\mathbb{C}).
$$

*Proof.* A complex structure is a unital $\mathbb{R}$-algebra homomorphism $\kappa:\mathbb{C}\to Z(\mathbb{B}_{\mathbb{R}})$, and $Z(\mathbb{B}_{\mathbb{R}})=\mathbb{C}e_t$ is a copy of $\mathbb{C}$ as a real algebra. A unital map $\mathbb{C}\to\mathbb{C}$ of real algebras is either the identity or the conjugation, and the two give complex algebras that are isomorphic, the conjugation being an isomorphism of $\mathbb{C}$ over $\mathbb{R}$. So there is one isomorphism class, and its representative is $\mathbb{B}$ itself, since $\mathbb{B}_{\mathbb{R}}$ is $\mathbb{B}$ with the scalars forgotten.

**Remark (the two structures of $\mathbb{C}$).** The identity and the conjugation are distinct complex structures on $\mathbb{C}$ read over $\mathbb{R}$, and they are not equal as maps; they give the same complex algebra because the conjugation is an automorphism of $\mathbb{C}$. The smallest instance is $\mathbb{C}$ itself read over $\mathbb{R}$: the identity and the conjugation are the two maps, and both give $\mathbb{C}$ as the complex form, because the conjugation is an automorphism of $\mathbb{C}$. The count of complex structures is therefore two and the count of complex forms is one, and the two numbers must not be confused; the analogous statement for $\mathbb{C}$ itself, with its two idempotents under scalar extension, is [The Scalar Extension of the Complex Numbers and Its Two Idempotents](the-scalar-extension-of-the-complex-numbers-and-its-two-idempotents.html).

**Warning (the complex structure is not the complexification).** The complex form of $\mathbb{B}_{\mathbb{R}}$ is $\mathbb{B}$, of complex dimension four. The complexification is

$$
\mathbb{B}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C}),
$$

of complex dimension eight, and it is a larger algebra obtained by adjoining a second central copy of $\mathbb{C}$ that is linearly independent of the first over $\mathbb{R}$. The form and the complexification are different objects, they have different dimensions over $\mathbb{C}$, and a statement about one is not a statement about the other. This is the most frequent error in the literature on the algebra.

## The Six Subspaces and the Structures

The six remarkable subspaces are the fixed and anti-fixed spaces of the three involutions $\natural$, $\overline{\phantom{Q}}$ and ${}^{*}=\overline{\phantom{Q}}\circ\natural$. Their definitions, bases, dimensions and the full table of intersections are in [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html); only the list and the relation to the structures is recorded here.

| Subspace | Condition | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathbb{B}_C$ centre | $\tilde Q^{\natural}=\tilde Q$ | $2$ |
| $\mathbb{B}_V$ vector | $\tilde Q^{\natural}=-\tilde Q$ | $6$ |
| $\mathbb{B}_H$ quaternion | $\overline{\tilde Q}=\tilde Q$ | $4$ |
| $\mathbb{B}_{iH}$ antiquaternion | $\overline{\tilde Q}=-\tilde Q$ | $4$ |
| $\mathbb{B}_{\Psi}$ Hermitian | $\tilde Q^{*}=\tilde Q$ | $4$ |
| $\mathbb{B}_{\Phi}$ anti-Hermitian | $\tilde Q^{\flat}=\tilde Q$ | $4$ |

**The compact fixed set is one of the six.** The fixed set of $\sigma_{\mathrm{comp}}$ is $\mathbb{B}_H$, and the condition in the table is exactly the definition of the coefficient conjugation used above. The anti-fixed space $\mathbb{B}_{iH}$ is the eigenspace of $\sigma_{\mathrm{comp}}$ for the eigenvalue $-1$, so the first real structure is the decomposition

$$
\mathbb{B}=\mathbb{B}_H\oplus\mathbb{B}_{iH}
$$

read as a pair of eigenspaces.

**The split fixed set is not one of the six.** The fixed set of $\sigma_{\mathrm{split}}$ is $\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_y,i\vec e_x,i\vec e_z\}$, and it is not among the six: it differs from $\mathbb{B}_{\Psi}=\operatorname{span}_{\mathbb{R}}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$ by the exchange of $i\vec e_y$ for $\vec e_y$, and from $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{iH}$ by more than one element. The six subspaces are the fixed and anti-fixed spaces, that is the $\pm1$-eigenspaces, of the three involutions of the group $\{\mathrm{id},\natural,\overline{\phantom{Q}},{}^{*}\}$, and $\sigma_{\mathrm{split}}$ is not in that group, being the coefficient conjugation composed with an inner automorphism. The group of involutions, its Cayley table and the three splittings are [The Group of Involutions of the Biquaternion Algebra](the-group-of-involutions.html).

**The complex structure acts on the six.** The operator $J(\tilde Q)=i\tilde Q$ preserves $\mathbb{B}_C$ and $\mathbb{B}_V$, which are complex subspaces of complex dimensions one and three, and exchanges the two four-dimensional pairs: $J\mathbb{B}_H=\mathbb{B}_{iH}$ and $J\mathbb{B}_{\Psi}=\mathbb{B}_{\Phi}$. A real structure and a complex structure therefore act on the list in different ways, the first fixing a member of the list and the second permuting the list.

**Remark (why $\mathbb{B}_{\Psi}$ is not a real form).** The subspace $\mathbb{B}_{\Psi}$ is the fixed set of the involution ${}^{*}$, which is an anti-automorphism and not an automorphism, so $\mathbb{B}_{\Psi}$ is not closed under products: the elements $i\vec e_x$ and $i\vec e_y$ are Hermitian and their product is $-\vec e_z$, which is not. A real form requires a multiplicative involution, and ${}^{*}$ is not one. Of the four maps of the group only the identity and the coefficient conjugation are multiplicative; the quaternion conjugation $\natural$ and the Hermitian conjugation ${}^{*}$ reverse the product, so their fixed sets are not closed under products and cannot be real forms at all. The two remaining fixed sets are $\mathbb{B}$ itself and $\mathbb{B}_H$, and only the second has half the real dimension, so only the second is a real form.

## The Structures and the Lie Algebra

**The bracket.** The commutator $[\tilde X,\tilde Y]=\tilde X\tilde Y-\tilde Y\tilde X$ turns $\mathbb{B}_{\mathbb{R}}$ into a real Lie algebra of dimension eight, with brackets on the base

$$
[\vec e_x,\vec e_y]=2\vec e_z,\qquad [\vec e_y,\vec e_z]=2\vec e_x,\qquad [\vec e_z,\vec e_x]=2\vec e_y,
$$

and with $i e_t$ central. The Lie theory of the algebra is [Biquaternion Lie Group and Exponential Structure](biquaternion-lie-group-and-exponential-structure.html); this section only records which real subalgebras the structures produce, because a real structure is the natural source of them: the fixed set of a multiplicative involution is a subalgebra, and its traceless part is a Lie subalgebra.

**The dictionary.** The table lists the subalgebras that the two real structures and the complex structure produce. The last column is the signature of the Killing form $K(\tilde X,\tilde Y)=\operatorname{tr}(\operatorname{ad}_{\tilde X}\operatorname{ad}_{\tilde Y})$, computed in the eight-dimensional algebra $\mathbb{B}_{\mathbb{R}}$ and not in the subalgebra; a common rescaling of the basis rescales $K$ by a positive factor and leaves the signature unchanged, so the column carries no normalisation beyond that.

| Lie algebra | in $\mathbb{B}_{\mathbb{R}}$ | $\dim_{\mathbb{R}}$ | simply connected group | $K$ |
|---|---|---|---|---|
| $\mathfrak{su}(2)$ | $\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}=\mathbb{B}_V\cap\mathbb{B}_H$ | $3$ | $SU(2)$ | $(-,-,-)$ |
| $\mathfrak u(1)$ | $\mathbb{R}\,i e_t=\mathbb{B}_C\cap\mathbb{B}_{\Phi}$ | $1$ | $\mathbb{R}$ | $(0)$ |
| $\mathfrak{sl}(2,\mathbb{R})$ | $\operatorname{span}_{\mathbb{R}}\{i\vec e_x,\vec e_y,i\vec e_z\}=\mathbb{B}_V\cap\mathbb{B}_{\mathbb{R}}^{\sigma_{\mathrm{split}}}$ | $3$ | $\widetilde{SL_2(\mathbb{R})}$ | $(+,+,-)$ |
| $\mathfrak u(2)$ | $\mathbb{B}_{\Phi}=\operatorname{span}_{\mathbb{R}}\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$ | $4$ | $SU(2)\times\mathbb{R}$ | $(0,-,-,-)$ |
| $\mathfrak{gl}(2,\mathbb{R})$ | $\mathbb{B}_{\mathbb{R}}^{\sigma_{\mathrm{split}}}=\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_y,i\vec e_x,i\vec e_z\}$ | $4$ | $\widetilde{GL_2^+}(\mathbb{R})$ | $(+,+,-,0)$ |
| $\mathfrak{so}(3,1)\cong\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$ | $\mathbb{B}_V=\{\tilde Q:Q_t=0\}$ | $6$ | $SL_2(\mathbb{C})$ | $(+,+,+,-,-,-)$ |
| $\mathfrak{gl}(2,\mathbb{C})_{\mathbb{R}}$ | $\mathbb{B}_{\mathbb{R}}$ | $8$ | $\widetilde{GL_2}(\mathbb{C})$ | not definite |

**Corollary (the compact form is the vector part).** The fixed set of $\sigma_{\mathrm{comp}}$ is $\mathbb{B}_H$, of dimension four, and its traceless part is the vector part $\mathbb{B}_V\cap\mathbb{B}_H=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$, which is $\mathfrak{su}(2)$ in the rescaled base $\vec e_k/2$. Its Killing form is $-2$ times the identity, so the algebra is compact, and the group $SU(2)$ is compact. These three elements are the real slice of the vector subspace, $\mathbb{B}_H\cap\mathbb{B}_V$, so the traceless part of the quaternion fixed set and the real part of the pure elements are the same three-dimensional space; the coincidence is special to dimension two.

**Corollary (the split form is the real matrices).** The fixed set of $\sigma_{\mathrm{split}}$ is $M_2(\mathbb{R})$, whose traceless part is $\operatorname{span}_{\mathbb{R}}\{i\vec e_x,\vec e_y,i\vec e_z\}$, that is $\mathfrak{sl}(2,\mathbb{R})$. Its Killing form has signature $(2,1)$: positive on the two-dimensional space of traceless symmetric matrices and negative on the line of antisymmetric ones, the line being $\mathbb{R}\,\vec e_y$. The three signatures of $\mathfrak{sl}(2)$ and their meanings are [The Killing Form of $\mathfrak{sl}_2$ and Its Three Signatures](the-killing-form-of-sl-2-and-its-three-signatures.html).

**Corollary (the complex structure gives the realification).** Reading $\mathbb{B}_{\mathbb{R}}$ over $\mathbb{C}$ through $J$ returns $\mathbb{B}$, and the traceless part of $\mathbb{B}$ is the complex Lie algebra $\mathfrak{sl}(2,\mathbb{C})$, of complex dimension three. Forgetting the complex structure and keeping the real scalars gives $\mathbb{B}_{\mathbb{R}}$, whose traceless part is the pure part $\mathbb{B}_V$, of real dimension six, and $\mathbb{B}_V$ is $\mathfrak{sl}(2,\mathbb{C})$ read over $\mathbb{R}$, that is $\mathfrak{so}(3,1)$. The three real forms of $\mathfrak{sl}(2,\mathbb{C})$ therefore appear as three real subspaces of one algebra: the compact $\mathfrak{su}(2)$, the split $\mathfrak{sl}(2,\mathbb{R})$ and the complex one read over $\mathbb{R}$.

**The covers.** The two-to-one covers $SU(2)\to SO(3)$ and $SL_2(\mathbb{C})\to SO^+(3,1)$ are the quotients of the simply connected groups of the table by the central subgroup $\{\pm e_t\}$, and they are computed in [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), §*The Double Covers and the Lorentz Group*. The general statement that a connected group with a given Lie algebra is the quotient of the simply connected one by a discrete central subgroup, with the fundamental group equal to that subgroup, is [The Lie Correspondence and the Adjoint Representation](the-lie-correspondence-and-the-adjoint-representation.html); it is cited here and not used beyond the identification of the covers. The complete list of the connected groups for the two real forms, subalgebra by subalgebra, is in [Classification of the Real Structures of the Biquaternion Algebra, including Lie Algebras and Lie Groups](classification-of-the-real-structures-of-the-biquaternion-algebra.html).

**Warning (the structure fixes the algebra, not the group).** A real structure determines a real algebra and hence, up to isomorphism, one simply connected group; it does not determine the group. The algebra $\mathfrak{su}(2)$ is the algebra of both $SU(2)$ and $SO(3)$, and the algebra of $\mathfrak{sl}(2,\mathbb{R})$ is the algebra of the cover, of $SL_2(\mathbb{R})$ and of $PSL_2(\mathbb{R})$. The passage from the algebra to a group requires the choice of a discrete central subgroup, and that choice is not part of the structure.

## What the Structures Do Not Decide

**The structure does not classify the products.** A real structure is an involution, and the four products are bilinear or sesquilinear operations. The two are independent: the products are read with the scalar part, and a real structure changes the scalars. The four forms $P$, $N$, $H$ and $\mathrm{Kr}$ and their algebraic norms are classified in [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), and the word **form** there means the scalar part of a product and not the fixed set of an involution.

**The structure does not classify the subspaces.** The six subspaces are the fixed and anti-fixed spaces of the involutions of one group, and only one of them is the fixed set of a real structure. The classification of the subspaces is a classification of a lattice, with intersections and sums, and it is [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html).

**The structure does not classify the subalgebras.** The table of the previous section lists the subalgebras that the structures produce, and it is not a classification of the Lie subalgebras of $\mathbb{B}_{\mathbb{R}}$. The subalgebras of $\mathbb{B}_{\mathbb{R}}$ are classified by the linear algebra of the eight real coordinates, and that classification is not undertaken in this article; the table records only the ones that the two real structures and the complex structure single out. What is undertaken is the classification of the subalgebras of each of the two real forms, layer by layer, associative, Lie and Jordan, together with the Lie groups attached to the Lie layer: see [Classification of the Real Structures of the Biquaternion Algebra, including Lie Algebras and Lie Groups](classification-of-the-real-structures-of-the-biquaternion-algebra.html).

**The structure does not decide the topology.** The compact real form has a compact simply connected group, $SU(2)$, and the split real form has a non-compact one, $\widetilde{SL_2(\mathbb{R})}$. The difference in compactness is a difference between the two real structures, and not a difference that a single structure can vary: within one structure the simply connected group is fixed, and the quotient by a discrete central subgroup is a further choice, not a consequence of the structure.

**The complex structure does not select a real form.** A complex structure on $\mathbb{B}_{\mathbb{R}}$ and a real structure on $\mathbb{B}$ are independent data, and one does not choose the other. Both real structures of the article are conjugate-linear for the same operator $J(\tilde Q)=i\tilde Q$, that is

$$
\sigma(J\tilde X)=-J\sigma(\tilde X)
$$

for $\sigma=\sigma_{\mathrm{comp}}$ and for $\sigma=\sigma_{\mathrm{split}}$, so the complex structure is the same in the compact reading and in the split reading and only the real slice differs. Reading the algebra over $\mathbb{C}$ therefore says nothing about which slice is intended, and the slice is chosen separately.

**Remark (what a classification of structures is).** Two real structures are classified up to isomorphism when their fixed algebras are isomorphic as real algebras, and two complex structures when their complex forms are isomorphic as complex algebras. Both classifications here are by a single invariant, the isomorphism class of the fixed algebra and the isomorphism class of the complex form, and both answers are short: two and one. The length of the article is in the identification of the fixed sets and in the separation of the notions, not in the enumeration.

## Summary

A **real structure** on the complex algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is a conjugate-linear multiplicative involution, and its fixed set is a real subalgebra whose complexification is $\mathbb{B}$; a **complex structure** on the real algebra $\mathbb{B}_{\mathbb{R}}$ is a central action of $\mathbb{C}$, equivalently a real-linear $J$ with $J^2=-\mathrm{id}$ and $J(XY)=J(X)Y$. The two operations run in opposite directions and are not inverse to each other.

There are exactly two real forms up to isomorphism. The coefficient conjugation $\sigma_{\mathrm{comp}}(\tilde Q)=\overline{\tilde Q}$ has fixed set the quaternion subspace $\mathbb{B}_H=\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_x,\vec e_y,\vec e_z\}$, a division algebra isomorphic to $\mathbb{H}$, and it is the compact one. The inner twist $\sigma_{\mathrm{split}}(\tilde Q)=-\vec e_y\overline{\tilde Q}\vec e_y$ has fixed set $\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_y,i\vec e_x,i\vec e_z\}$, which is $M_2(\mathbb{R})$ in the dictionary, and it is the split one: the idempotent $\tfrac12(e_t+i\vec e_x)$ lies in it and is a zero divisor. The two are related by the inner twist of $\vec e_y$, and their real forms are still not isomorphic, because the sign of $u\bar u$ for the twist decides the class.

There is exactly one complex structure up to isomorphism, given by multiplication by $i e_t$, and its complex form is $\mathbb{B}$. The complex form is not the complexification: the form has complex dimension four, and the complexification $\mathbb{B}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$ has complex dimension eight.

The structures act on the six remarkable subspaces in two different ways. The compact structure has a fixed set among them, $\mathbb{B}_H$, and splits $\mathbb{B}=\mathbb{B}_H\oplus\mathbb{B}_{iH}$ by its eigenspaces; the split structure has no fixed set among them; and the complex structure preserves $\mathbb{B}_C$ and $\mathbb{B}_V$ and exchanges $\mathbb{B}_H$ with $\mathbb{B}_{iH}$ and $\mathbb{B}_{\Psi}$ with $\mathbb{B}_{\Phi}$. On the Lie algebra the two structures give $\mathfrak{su}(2)$, of compact type and Killing form $(-,-,-)$, and $\mathfrak{sl}(2,\mathbb{R})$, of signature $(2,1)$, while the complex structure gives the realification $\mathfrak{so}(3,1)$ of $\mathfrak{sl}(2,\mathbb{C})$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}\cong M_2(\mathbb{C})$ | The biquaternion algebra over $\mathbb{C}$, of complex dimension four, read in the Pauli dictionary |
| $\mathbb{B}_{\mathbb{R}}\cong M_2(\mathbb{C})_{\mathbb{R}}$ | The same multiplication read over $\mathbb{R}$, of real dimension eight |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | The base; $e_t$ the unit, $\vec e_k^2=-e_t$ |
| $\tilde Q=Q_te_t+\vec Q$ | An element; scalar part $Q_te_t$, vector part $\vec Q$ |
| $\overline{\tilde Q}$, $\natural$, ${}^{*}$, $\flat$ | The four conjugations; ${}^{*}=\overline{\phantom{Q}}\circ\natural$, $\flat=-{}^{*}$ |
| $\sigma$ | A real structure: conjugate-linear, multiplicative, involutive |
| $A^{\sigma}$ | Its real form, the fixed set |
| $\sigma_{\mathrm{comp}}(\tilde Q)=\overline{\tilde Q}$ | The compact real structure |
| $\sigma_{\mathrm{split}}(\tilde Q)=-\vec e_y\overline{\tilde Q}\vec e_y$ | The split real structure |
| $\mathbb{B}_H=\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_x,\vec e_y,\vec e_z\}$ | Fixed set of $\sigma_{\mathrm{comp}}$; the quaternions |
| $\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_y,i\vec e_x,i\vec e_z\}$ | Fixed set of $\sigma_{\mathrm{split}}$; the real matrices |
| $J(\tilde Q)=i\tilde Q$ | The complex structure; central, $J^2=-\mathrm{id}$ |
| $\kappa:\mathbb{C}\to Z(\mathbb{B}_{\mathbb{R}})$ | A complex structure as a map of centres |
| $\mathbb{B}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$ | The complexification, of complex dimension eight |
| $\mathbb{B}_C,\mathbb{B}_V,\mathbb{B}_H,\mathbb{B}_{iH},\mathbb{B}_{\Psi},\mathbb{B}_{\Phi}$ | The six remarkable subspaces |
| $[\tilde X,\tilde Y]=\tilde X\tilde Y-\tilde Y\tilde X$ | The bracket of the Lie algebra |
| $K(\tilde X,\tilde Y)=\operatorname{tr}(\operatorname{ad}_{\tilde X}\operatorname{ad}_{\tilde Y})$ | The Killing form |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involutions of the first and second kind and the real forms of a central simple algebra.
- Nicolas Bourbaki, *Algebra II* (Springer, 2003), for the scalar extension, the semilinear maps and the descent by a quadratic extension.
- Jean-Pierre Serre, *Galois Cohomology* (Springer, 1997), for the classification of the real forms by the first Galois cohomology of the conjugation.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for the theorem of Frobenius and the central simple algebras of dimension four over $\mathbb{R}$.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the Skolem–Noether theorem and the conjugacy of the real structures.
- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, 1853), and James Cockle, *On Systems of Algebra Involving More than One Imaginary* (Philosophical Magazine, 1849), for the historical forms of the algebra.
- Stephen J. Sangwine, Todd A. Ell and Nicolas Le Bihan, *Fundamental Representations and Algebraic Properties of Biquaternions or Complexified Quaternions* (Advances in Applied Clifford Algebras 21, 2011), for the matrix representations and the two readings.
- Soo-Chang Pei, Ja-Han Chang and Jian-Jiun Ding, *Commutative Reduced Biquaternions and Their Fourier Transform* (IEEE Transactions on Signal Processing 52, 2004), for the reduced system and its comparison with the biquaternions.
