# __Reduced Biquaternion Other Algebraic Element Representations__

## Introduction

Beside the four-vector, the matrix and the polar readings, the reduced biquaternion element is written in three algebraic presentations that name its structure rather than its numbers: the **Clifford identification**, which builds the algebra from the two two-dimensional real Clifford algebras; the **idempotent-coordinate representation**, which sends the element to the pair $(Q_{++},Q_{--})$ of complex numbers; and the **quotient presentation**, which reads the algebra as a quotient of a polynomial ring. To these this article adds the **array representation**, which sends a matrix of reduced biquaternions to a pair of complex matrices. The four are stated, their relations are recorded, and the choices they involve are named. The multiplication is **commutative**, so all four presentations are commutative; it **has zero divisors**, so none of them is a division ring; and the algebra is **not a division algebra**.

**Conventions.** The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$ and $ji=ij$; the element is $Q_\pm=Q_++jQ_-$ with $Q_+=q_++iq'_+$, $Q_-=q_-+iq'_-$; the idempotents are $\Pi_{\pm}=\tfrac12(1\pm j)$ and the idempotent coordinates are $Q_{++}=Q_++Q_-$, $Q_{--}=Q_+-Q_-$, with $Q_\pm=Q_{++}\Pi_++Q_{--}\Pi_-$. The element glyph is $Q_\pm$, without a tilde, the reduced algebra having no quaternionic factor.

**Boundaries.** The four-vector and matrix readings are *The Four-Vector Element Representation of the Reduced Biquaternions* and *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions*; the umbrella is *Introduction to Reduced Biquaternion Element Representations*; the polar reading is *Reduced Biquaternions Polar Element Representation*; the operators are *Operators on the Reduced Biquaternions*; and the idempotent splitting is *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*. The biquaternion counterpart is *Biquaternion Other Algebraic Element Representations*.

## The Clifford Identification

**The algebra is the tensor product of the two two-dimensional real Clifford algebras, one definite and one split.**

### Definition

**Definition.** Let $Cl_{1,0}$ be the real Clifford algebra of one generator $f$ with $f^{2}=+1$, and $Cl_{0,1}$ the real Clifford algebra of one generator $e$ with $e^{2}=-1$. The **Clifford identification** of the reduced biquaternions is
$$
\mathbb{B}_{\mathrm{r}}\cong Cl_{1,0}\otimes_{\mathbb{R}}Cl_{0,1},
$$
the tensor product of the split-complex and the complex Clifford algebras.

### Theorem

**Theorem (the identification).** The map on the generators
$$
f\otimes 1\mapsto j,\qquad 1\otimes e\mapsto i,\qquad f\otimes e\mapsto ij
$$
extends to an isomorphism of real algebras $\mathbb{B}_{\mathrm{r}}\cong Cl_{1,0}\otimes_{\mathbb{R}}Cl_{0,1}$.

*Proof.* $f\otimes1$ and $1\otimes e$ square to $f^{2}\otimes1=+1$ and $1\otimes e^{2}=-1$, matching $j^{2}=+1$ and $i^{2}=-1$, and they commute because they sit in the two different tensor factors; the tensor product is spanned by $1\otimes1$, $f\otimes1$, $1\otimes e$ and $f\otimes e$, four real dimensions, and so is $\mathbb{B}_{\mathrm{r}}$; the map is an algebra homomorphism on the generators and a bijection on a spanning set, hence an isomorphism.

**Corollary (the factorisation of the algebra).** $Cl_{1,0}\cong\mathbb{R}[f]/(f^{2}-1)\cong\mathbb{R}\times\mathbb{R}$, split by $f\mapsto(1,-1)$, and $Cl_{0,1}\cong\mathbb{R}[e]/(e^{2}+1)\cong\mathbb{C}$; the tensor product is
$$
(\mathbb{R}\times\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}.
$$
This is the isomorphism $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\oplus\mathbb{C}$ read on the Clifford side, and the zero divisors of the algebra are the Clifford elements one of whose two components vanishes.

*Proof.* The two factors are the standard presentations of the split-complex numbers and the complex numbers; the tensor product of $\mathbb{R}\times\mathbb{R}$ with $\mathbb{C}$ is $\mathbb{C}\times\mathbb{C}$; and a product ring has zero divisors exactly at the elements with a vanishing component, which are the images of the two idempotent lines.

### The Dictionary of the Basis

| $\mathbb{B}_{\mathrm{r}}$ | $Cl_{1,0}\otimes Cl_{0,1}$ | square |
|---|---|---|
| $1$ | $1\otimes1$ | $+1$ |
| $i$ | $1\otimes e$ | $-1$ |
| $j$ | $f\otimes1$ | $+1$ |
| $ij$ | $f\otimes e$ | $-1$ |

The dictionary makes the two complex structures visible: the generator $i$ is definite ($i^{2}=-1$) and the generator $j$ is split ($j^{2}=+1$), and the product $ij$ is again definite, $(ij)^{2}=i^{2}j^{2}=-1$.

### Why the Identification Is Useful

It places the reduced biquaternions in the Clifford family as the commutative square, the tensor product of the two smallest Clifford algebras, and it exhibits the difference from the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, which carries the non-commutative quaternion factor. The four products and their forms, *The Four Products, Their Forms and Their Algebraic Norms*, are the Clifford products read through the two gradings.

## The Idempotent-Coordinate Representation

**The element is the pair of its two idempotent coordinates, and this is the algebra isomorphism $\mathbb{C}\times\mathbb{C}$.**

**Definition.** The **idempotent-coordinate representation** is
$$
\iota(Q_\pm)=(Q_{++},Q_{--}),\qquad Q_\pm=Q_{++}\Pi_++Q_{--}\Pi_-,
$$
a map $\mathbb{B}_{\mathrm{r}}\to\mathbb{C}\times\mathbb{C}$.

**Theorem.** $\iota$ is an isomorphism of $\mathbb{C}$-algebras onto $\mathbb{C}\times\mathbb{C}$: it is $\mathbb{C}$-linear, bijective, $\iota(1)=(1,1)$, and $\iota(Q_{\pm,1}Q_{\pm,2})=(Q_{1++}Q_{2++},\,Q_{1--}Q_{2--})=\iota(Q_{\pm,1})\iota(Q_{\pm,2})$, where $Q_{i++}$ and $Q_{i--}$ are the two coordinates of $Q_{\pm,i}$.

*Proof.* The map is linear; it is bijective because every pair $(Q_{++},Q_{--})$ is the image of $Q_\pm=\tfrac12\bigl((Q_{++}+Q_{--})+(Q_{++}-Q_{--})j\bigr)$; and the product is componentwise because the idempotents satisfy $\Pi_{i}\Pi_{j}=\delta_{ij}\Pi_{i}$.

**Corollary (the two characters are its coordinates).** The two coordinates of $\iota$ are the two characters $\lambda_+(Q_\pm)=Q_{++}$ and $\lambda_-(Q_\pm)=Q_{--}$ of *Introduction to Reduced Biquaternion Element Representations*; the idempotent-coordinate representation is the representation in which the algebra is the visible direct product, and every other representation of the block is this one in another alphabet.

*Proof.* The coordinate maps are exactly the two characters, and the remaining representations read the same pair $(Q_{++},Q_{--})$ as a quadruple, a matrix, a Clifford element or a polar pair.

## The Quotient Presentation

**The algebra is the quotient of the polynomial ring in two commuting variables by the two relations.**

**Definition.** Let $\mathbb{R}[x,y]$ be the polynomial ring in two commuting indeterminates. The **quotient presentation** of the reduced biquaternions is
$$
\mathbb{B}_{\mathrm{r}}\cong\mathbb{R}[x,y]\big/\bigl(x^{2}+1,\ y^{2}-1\bigr),
$$
the classes of $x$ and $y$ being $i$ and $j$.

**Theorem.** The quotient is a four-dimensional real algebra isomorphic to $\mathbb{B}_{\mathrm{r}}$.

*Proof.* The relations are exactly the defining relations $i^{2}=-1$ and $j^{2}=+1$ of the basis $1,i,j,ij$, and the commutativity of the polynomial ring is $ji=ij$; the classes of $1,x,y,xy$ form a real basis of the quotient, four-dimensional.

**Corollary (the factorisation of the quotient).** $x^{2}+1$ is irreducible over $\mathbb{R}$ and $y^{2}-1=(y-1)(y+1)$ splits, so
$$
\mathbb{B}_{\mathrm{r}}\cong\mathbb{R}[x]/(x^{2}+1)\otimes_{\mathbb{R}}\mathbb{R}[y]/(y^{2}-1)\cong\mathbb{C}\otimes_{\mathbb{R}}(\mathbb{R}\times\mathbb{R})\cong\mathbb{C}\times\mathbb{C},
$$
the definite factor giving the field and the split factor giving the two idempotent lines. The ring is **commutative** and **has zero divisors**, and it is **not a domain**; it is the same algebra as the Clifford identification of §*The Clifford Identification*, written with indeterminates.

*Proof.* The Chinese remainder theorem applied to $y^{2}-1$ gives $\mathbb{R}[y]/(y^{2}-1)\cong\mathbb{R}\times\mathbb{R}$; the tensor product with $\mathbb{C}$ is $\mathbb{C}\times\mathbb{C}$; and a product of two or more fields has zero divisors.

## The Tensor-Product Presentation

**The algebra is $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$, and the two complex factors are the two complex structures of the same space.**

**Theorem (the two complex structures and their product).** The real algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ carries two commuting complex structures, the multiplications by $i$ and by $ij$,
$$
J_{1}(Q_\pm)=iQ_\pm,\qquad J_{2}(Q_\pm)=ijQ_\pm,\qquad J_{1}^{2}=J_{2}^{2}=-\mathrm{id},\qquad J_{1}J_{2}=J_{2}J_{1},
$$
each a real-linear map with square $-\mathrm{id}$; their product
$$
J_{1}J_{2}=L_{i\cdot ij}=L_{i^{2}j}=L_{-j}
$$
is a **real structure**, $(J_{1}J_{2})^{2}=+\mathrm{id}$, the multiplication by $-j$, which is the same kind of map as the multiplication by $j$.

*Proof.* $i^{2}=-1$ and $(ij)^{2}=i^{2}j^{2}=-1$, so the multiplications by $i$ and by $ij$ square to $-\mathrm{id}$; they commute because the algebra is commutative. The product is the multiplication by $i\cdot ij=i^{2}j=-j$, and $(-j)^{2}=j^{2}=+1$, so the product squares to $+\mathrm{id}$: it is a real structure, not a third complex structure. The complex structures among the signed units are $\pm i$ and $\pm ij$, and the real structures are $\pm j$ and $\pm1$.

**Corollary (the tensor is not a field).** $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ is a product of two fields, not a field: it has zero divisors, and the two factors are the two coordinate copies $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$. This is the algebraic content of the fact that the reduced biquaternions are a split algebra, against the complex numbers, which are a field.

*Proof.* $\mathbb{C}$ is two-dimensional over $\mathbb{R}$ and a field, but the tensor product of two copies over $\mathbb{R}$ is $\mathbb{C}\times\mathbb{C}$, which is not a field; a product of rings has the idempotents $(1,0)$ and $(0,1)$, whose images are $\Pi_+$ and $\Pi_-$.

## Matrices of Several Elements

**A matrix of several reduced biquaternions is a pair of complex matrices, and the array ring is the product of two full matrix rings.**

**Definition.** A **reduced biquaternion array** is an $n\times n$ matrix $M=\bigl((Q_\pm)_{rs}\bigr)$ with entries in $\mathbb{B}_{\mathrm{r}}$. The **array representation** is the map
$$
M\mapsto\bigl(\iota(M_{rs})\bigr)=\bigl(M^{+},M^{-}\bigr),\qquad (M^{\pm})_{rs}=\lambda_{\pm}\bigl((Q_\pm)_{rs}\bigr),
$$
sending the array to a pair of $n\times n$ complex matrices, the $Q_{++}$-part and the $Q_{--}$-part.

**Theorem (the array ring).** The array representation is an isomorphism of rings
$$
M_{n}(\mathbb{B}_{\mathrm{r}})\cong M_{n}(\mathbb{C})\times M_{n}(\mathbb{C}),
$$
it is compatible with the product, with the identity, and with the determinant in the sense $\det M=(\det M^{+},\det M^{-})\in\mathbb{C}\times\mathbb{C}$; the array is invertible exactly when both complex matrices are.

*Proof.* The entries of $\mathbb{B}_{\mathrm{r}}$ are pairs of complex numbers and the operations are componentwise, so $M_{n}(\mathbb{B}_{\mathrm{r}})\cong M_{n}(\mathbb{C}\times\mathbb{C})\cong M_{n}(\mathbb{C})\times M_{n}(\mathbb{C})$; the determinant over the commutative ring $\mathbb{C}\times\mathbb{C}$ computes componentwise, whence the pair of determinants and the invertibility criterion.

**Corollary (the repeated-block form).** Through the regular representation each entry becomes a $2\times2$ complex matrix, so the array becomes a $2n\times2n$ complex matrix with the $\begin{smallmatrix}Q_+&Q_-\\ Q_-&Q_+\end{smallmatrix}$ blocks; the array representation by the pair $(M^{+},M^{-})$ is the diagonalised form of that matrix, the passage being the simultaneous change of basis of every entry of *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions*.

*Proof.* Substituting the matrix of each entry in the array gives the $2n\times2n$ matrix; block-diagonalising each $2\times2$ block by the common change $P$ gives the pair of $n\times n$ complex matrices.

## Relations Between the Representations

**The four presentations are the same isomorphism $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\times\mathbb{C}$ in four alphabets, and the table places them.**

| presentation | the element read as | dimension over $\mathbb{C}$ | coordinate ring |
|---|---|---|---|
| Clifford | $Cl_{1,0}\otimes Cl_{0,1}$ element | $2$ | $\mathbb{R}[f,e]/(f^{2}-1,e^{2}+1)$ |
| idempotent coordinates | the pair $(Q_{++},Q_{--})$ | $2$ | $\mathbb{C}\times\mathbb{C}$ |
| quotient | a class in $\mathbb{R}[x,y]/(x^{2}+1,y^{2}-1)$ | $2$ | $\mathbb{R}[x,y]/(x^{2}+1,y^{2}-1)$ |
| array | a pair $(M^{+},M^{-})$ of matrices | $2n^{2}$ | $M_{n}(\mathbb{C})\times M_{n}(\mathbb{C})$ |

**Theorem (they agree).** The four presentations agree on every element: the Clifford element, the pair $(Q_{++},Q_{--})$, the quotient class and the array all carry the same $Q_{++}$ and the same $Q_{--}$, and the maps between them are the identity on those two coordinates.

*Proof.* Each presentation assigns to $Q_\pm$ the pair of evaluations of its two coordinates; the Clifford identification evaluates on the two factors $\mathbb{R}\times\mathbb{R}$ of $Cl_{1,0}$, the idempotent-coordinate representation names the pair, the quotient evaluates $x$ and $y$, and the array applies the pair entrywise.

## The Role of Choices

**The presentations involve choices, and the choices do not change the algebra.**

The Clifford identification chooses which generator squares to $+1$ and which to $-1$; the quotient presentation chooses the names $x$ and $y$; the tensor presentation chooses which factor is the coefficient field; the array presentation chooses the size $n$. The first three choices are the choice of naming the two generators, and it does not change the algebra, only the order of the two factors of $\mathbb{C}\times\mathbb{C}$; the two factors can also be exchanged by the natural sign, which is the automorphism of *The Multiplication Operators of the Algebra of the Reduced Biquaternions*. The choice of $n$ changes the array ring but not the element representation, of which the array is the entrywise reading. No choice makes the algebra a division algebra: the zero divisors are present in every presentation, as the vanishing of one of the two coordinates.

## Summary

The reduced biquaternions carry three algebraic presentations beside the four-vector, the matrix and the polar readings: the **Clifford identification** $\mathbb{B}_{\mathrm{r}}\cong Cl_{1,0}\otimes_{\mathbb{R}}Cl_{0,1}$, with $Cl_{1,0}\cong\mathbb{R}\times\mathbb{R}$ split and $Cl_{0,1}\cong\mathbb{C}$ definite; the **idempotent-coordinate representation** $Q_\pm\mapsto(Q_{++},Q_{--})$, the algebra isomorphism onto $\mathbb{C}\times\mathbb{C}$ whose two coordinates are the two characters; and the **quotient presentation** $\mathbb{R}[x,y]/(x^{2}+1,y^{2}-1)\cong\mathbb{C}\times\mathbb{C}$. To these the **array representation** adds $M_{n}(\mathbb{B}_{\mathrm{r}})\cong M_{n}(\mathbb{C})\times M_{n}(\mathbb{C})$, with $\det M=(\det M^{+},\det M^{-})$ and the invertibility read on the two complex matrices. The four agree on the two coordinates $Q_{++}$ and $Q_{--}$; they involve only the choice of naming the two generators, which does not change the algebra, and the multiplication is **commutative**, **has zero divisors** and is **not a division algebra** in every presentation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Cl_{1,0}$, $Cl_{0,1}$ | the split-complex and the complex Clifford algebras, generated by $f$ and $e$ |
| $f\otimes1$, $1\otimes e$ | the Clifford generators identified with $j$ and $i$ |
| $\iota(Q_\pm)=(Q_{++},Q_{--})$ | the idempotent-coordinate representation |
| $\mathbb{R}[x,y]/(x^{2}+1,y^{2}-1)$ | the quotient presentation |
| $J_{1},J_{2}$ | the two commuting complex structures, the multiplications by $i$ and by $ij$ |
| $M^{+},M^{-}$ | the pair of complex matrices of an array |

## Further Reading

- *Introduction to Reduced Biquaternion Element Representations* (`articles_maths/introduction-to-reduced-biquaternion-element-representations.md`), for the representations and the two characters.
- *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the idempotent splitting.
- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), for the products and the forms.
- *The Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions* (`articles_maths/the-general-plain-algebra-in-the-2x2-matrix-element-representation-of-the-reduced-biquaternions.md`), for the diagonal model.
- *Biquaternion Other Algebraic Element Representations* (`articles_maths/biquaternion-other-algebraic-element-representations.md`), for the non-commutative companion and the Clifford identification there.
