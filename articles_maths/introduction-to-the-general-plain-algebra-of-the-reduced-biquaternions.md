# __Introduction to the General Plain Algebra of the Reduced Biquaternions__

## Introduction

This article reads the reduced biquaternion space with its **multiplication** and fixes it as an **algebra**: the definition of the product, the data the algebra carries, the axioms it satisfies and the plan of the block of articles that study it. The multiplication is the general plain bilinear product $TW$ of *The Four Products, Their Forms and Their Algebraic Norms*, read as the product of the algebra and not as one of four products side by side; the other three general products are not associative and are not the product of the algebra.

The general plain algebra is the **associative** case of the reduced biquaternion layer, and it is the case the rest of the category is built on. It is commutative and unital, with the unit $1$; it is **not** a field and **not** a division algebra, because it has the two idempotent lines as zero divisors; and its invertibility is decided by the reduced norm $\langle T\rangle_{\natural}=A^{2}-B^{2}$, which is the algebraic norm of the quaternionic bilinear product and the determinant of the multiplication (*Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions*).

**The results.** The general plain algebra is the commutative unital associative $\mathbb{R}$-algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ with basis $1,i,j,ij$ and the multiplication table of *Reduced Biquaternion Space*. Its unit is $1$, its inverse is $T^{-1}=\langle T\rangle_{\natural}^{-1}(A-Bj)$ when $\langle T\rangle_{\natural}\neq0$, and its zero divisors are the two punctured idempotent lines. The algebra is a direct product of two copies of $\mathbb{C}$, $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2}$, and its multiplication is componentwise in the idempotent coordinates.

**Boundaries.** The space and its two scalar systems are *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$*, above this article in this category; the involutions are *The Two Involutions and the Group of Involutions*; the four products and their forms and norms are *The Four Products, Their Forms and Their Algebraic Norms*. The algebraic norm of the multiplication and the invertibility criterion are *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions*, below this article; the zero divisors are *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*; the annihilators are *Annihilators of the General Plain Algebra of the Reduced Biquaternions*; the roots of one and the idempotents are *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions*; and the roots of zero and the nilpotents are *Square Roots of Zero and the Nilpotents of the General Plain Algebra of the Reduced Biquaternions*. The element representations, the multiplication operators, the remarkable subspaces, the topology, the analysis, the geometry and the fractals are the later blocks of the category, listed in §*The Plan of the Block*.

## The Algebra

### The Definition

**The general plain algebra of the reduced biquaternions is the reduced biquaternion space with its multiplication, and its product is the general plain bilinear product.**

**Definition.** The **general plain algebra of the reduced biquaternions** is the set $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ with the addition of the space and the **multiplication**
$$
(A+Bj)(C+Dj)=(AC+BD)+(AD+BC)j,
$$
extended to the whole space by bilinearity. The product is written by juxtaposition, $TW$.

The definition is the definition of the algebra of *Reduced Biquaternion Space*; the product here is read as **the** product and not as one of the four general products, and the article fixes it as the algebra product. The general plain bilinear product is its coordinate table; the general quaternionic bilinear product, the general plain sesquilinear product and the general quaternionic sesquilinear product are the other three, and none of them is associative (*The Four Products, Their Forms and Their Algebraic Norms*, §*The Comparison of the Four Products*).

### The Data

**The algebra is determined by four pieces of data: the space, the product, the unit and the scalar system.**

**The data of the general plain algebra** are:

- the **space**, the real four-dimensional vector space on $1,i,j,ij$, equivalently the complex two-dimensional space on $1,j$;
- the **product**, the bilinear multiplication $(A+Bj)(C+Dj)=(AC+BD)+(AD+BC)j$;
- the **unit**, the element $1$, two-sided and unique;
- the **scalar system**, the field $\mathbb{R}$ with the compatible complex scalar action of $\mathbb{C}$.

The data determine the algebra, since a bilinear product on a basis determines the product everywhere. The element, its coordinates and its two parts are §*The Element*; the axioms the data satisfy are §*The Algebra Axioms*.

### The Product and Its Unit

**The product is commutative, associative and unital, and the unit is $1$.**

**Theorem (the algebra axioms).** For all $T,W,V$ and all $\lambda\in\mathbb{R}$ the multiplication satisfies
$$
(TW)V=T(WV),\qquad TW=WT,\qquad 1T=T1=T,\qquad \lambda(TW)=(\lambda T)W=T(\lambda W),
$$
and it is distributive over the addition.

*Proof.* The product is the product of the algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$, which is associative, commutative and unital, and bilinear over $\mathbb{R}$ (*Reduced Biquaternion Space*). The distributivity is the bilinearity.

The algebra is therefore an **associative commutative unital $\mathbb{R}$-algebra**, and with the complex scalar action it is also a **$\mathbb{C}$-algebra**. It is the same algebra as the complexification of the split-complex numbers, $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{D}$.

## The Element

**A general element is $T=A+Bj$, with a scalar part $A$ and a vector part $Bj$, and its idempotent coordinates $A+B$ and $A-B$ are the pair that carries the product.**

**Definition.** The **scalar part** of $T=A+Bj$ is $A$, the **vector part** is $Bj$, and the **idempotent coordinates** are $A+B$ and $A-B$,
$$
T=(A+B)\Pi_{1}+(A-B)\Pi_{2},\qquad \Pi_{1,2}=\tfrac12(1\pm j).
$$

**Proposition (the multiplication in the idempotent coordinates).** For $T=(q_1,q_2)$ and $W=(q_1',q_2')$ in the idempotent coordinates $q_1=A+B$, $q_2=A-B$,
$$
TW=(q_1q_1',\;q_2q_2'),
$$
the product being componentwise.

*Proof.* The idempotents are orthogonal, $\Pi_{1}\Pi_{2}=0$, and idempotent, $\Pi_{i}^{2}=\Pi_{i}$ (*Reduced Biquaternion Space*); expanding $(q_1\Pi_{1}+q_2\Pi_{2})(q_1'\Pi_{1}+q_2'\Pi_{2})$ kills the crossed terms and gives $q_1q_1'\Pi_{1}+q_2q_2'\Pi_{2}$.

The proposition is the reason every question about the algebra splits into two questions about the complex numbers, and it is used in every article of the block.

## The Algebra Axioms

### Associativity

**The product is associative: $T(WV)=(TW)V$, and a triple of elements has a single product.**

*Proof.* In the idempotent coordinates the product is $(q_1q_1',q_2q_2')$, and the complex multiplication is associative in each coordinate, so $((q_1q_1')q_1'',(q_2q_2')q_2'')$ agrees in the two groupings; the associativity of the complex multiplication is the one fact used.

### Commutativity

**The product is commutative: $TW=WT$, and the algebra is not the quaternion algebra.**

*Proof.* The idempotent coordinates of $TW$ are $(q_1q_1',q_2q_2')$ and those of $WT$ are $(q_1'q_1,q_2'q_2)$, equal because the complex multiplication is commutative. In the real basis the commutativity is $ji=ij$, which is the third defining relation of *Reduced Biquaternion Space*; the product is therefore not the quaternion product, and the algebra is not $\mathbb{H}$ or $\mathbb{B}$.

### The Unit and the Inverse

**The unit is $1$, it is two-sided and unique, and an element is invertible exactly when its reduced norm $\langle T\rangle_{\natural}=A^{2}-B^{2}$ is nonzero, with the inverse $T^{-1}=\langle T\rangle_{\natural}^{-1}(A-Bj)$.**

*Proof.* The unit is $1=1+0j$, and $1\,T=T\,1=T$. Uniqueness: if $e$ is a unit then $e=e1=1$. The criterion $\langle T\rangle_{\natural}\neq0$ and the inverse are *The Four Products, Their Forms and Their Algebraic Norms*, §*The Multiplicative Norm*, and the full treatment is *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions*, below this article. In the idempotent coordinates the inverse of $(q_1,q_2)$ is $(q_1^{-1},q_2^{-1})$, which exists exactly when both coordinates are nonzero, that is when $\langle T\rangle_{\natural}=q_1q_2\neq0$.

### The Absence of Division

**The algebra is not a field and not a division algebra: it has zero divisors, and the invertible elements form a proper subset of the nonzero elements.**

*Proof.* The idempotents are orthogonal and nonzero, $\Pi_{1}\Pi_{2}=0$, so $\Pi_{1}$ and $\Pi_{2}$ are zero divisors (*Reduced Biquaternion Space*); the element $(1,0)$ annihilates $(0,1)$ in the idempotent coordinates, and both are nonzero. An element whose one idempotent coordinate vanishes is a nonzero zero divisor, so the group of units is a proper subset of $\mathbb{B}_{\mathrm{r}}\setminus\{0\}$.

The zero divisors, their two families and their geometry are *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*, below this article; their annihilators are *Annihilators of the General Plain Algebra of the Reduced Biquaternions*. The **absence of division** is stated here because it bears on every statement of an inverse: an element must be tested against $\langle T\rangle_{\natural}\neq0$ before it is inverted.

## The Structure

**The algebra is the direct product of two copies of $\mathbb{C}$, and its maximal ideals are the two idempotent lines.**

**Theorem (the structure).** The component map $\varphi(T)=(A+B,A-B)$ is an isomorphism of $\mathbb{C}$-algebras
$$
\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2}\cong\mathbb{C}\oplus\mathbb{C},
$$
and the ring is a direct product of two fields; it is not simple, its maximal ideals are the two idempotent lines $\mathbb{C}\Pi_{2}$ and $\mathbb{C}\Pi_{1}$ read as kernels of the two projections, and its only idempotents are $0,1,\Pi_{1},\Pi_{2}$.

*Proof.* The isomorphism is *Reduced Biquaternion Space*, §*The Isomorphism with the Direct Product*; a direct product of two fields has exactly two maximal ideals, the kernels of the two projections, which are $\mathbb{C}\Pi_{2}$ and $\mathbb{C}\Pi_{1}$. The idempotents of a direct product of two fields are the four pairs of $0$ and $1$, which correspond to $0,1,\Pi_{1},\Pi_{2}$; the computation is *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions*, below this article.

## The Plan of the Block

**The general plain algebra is studied in thirteen articles, and the plan is the list below.**

The block of the general plain algebra is the thirteen articles below, in the order the category follows, and its articles are:

| article | content |
|---|---|
| *Introduction to the General Plain Algebra* (this article) | the definition, the data and the plan |
| *Norm and Invertibility in the General Plain Algebra* | the algebraic norm, the invertibility criterion and the group of units |
| *Zero Divisors of the General Plain Algebra* | the null cone and its structure |
| *Annihilators of the General Plain Algebra* | the annihilators of an element and the two-sided annihilator of the structure |
| *Square Roots of One and the Idempotents* | the roots of $1$, the idempotents and the projections they carry |
| *Square Roots of Zero and the Nilpotents* | the roots of $0$ and the nilpotents, product by product |
| *Square Roots of a General Element* | the square roots of a general element |
| *The Specificities of the General Plain Algebra* | the specificities of the algebra |
| *Ideals and Peirce Decomposition* | the ideals and the Peirce decomposition |
| *The Group of Units of the General Plain Algebra* | the structure of the group of units |
| *The Forms of the General Plain Algebra* | the forms of the algebra |
| *The Multiplication Operators of the General Plain Algebra* | the left and the right multiplication maps |
| *The General Plain Algebra in the $2\times2$ Matrix Element Representation* | the $2\times2$ matrix model |

The table is the plan of the block and not a set of definitions: each row is defined in its own article, and the order of the rows is the order the category follows. The articles of the later blocks — the remarkable subspaces, the representations and operators, the topology, the analysis, the geometry and the fractals — are listed in the menu of the category and are not part of this block.

## Summary

The general plain algebra of the reduced biquaternions is the space $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ with the multiplication
$$
(A+Bj)(C+Dj)=(AC+BD)+(AD+BC)j,
$$
the general plain bilinear product read as the product of the algebra. Its data are the space, the product, the unit and the scalar system; it is an associative, commutative, unital $\mathbb{R}$-algebra and $\mathbb{C}$-algebra, with unit $1$ and with the multiplication in the idempotent coordinates componentwise, $TW=(q_1q_1',q_2q_2')$ for $T=(A+B,A-B)$ and $W=(C+D,C-D)$.

An element is $T=A+Bj$ with scalar part $A$ and vector part $Bj$; its inverse exists exactly when the reduced norm $\langle T\rangle_{\natural}=A^{2}-B^{2}$ is nonzero, and it is $T^{-1}=\langle T\rangle_{\natural}^{-1}(A-Bj)$. The algebra is the direct product $\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2}$ of two copies of $\mathbb{C}$, its maximal ideals are the two idempotent lines, its only idempotents are $0,1,\Pi_{1},\Pi_{2}$, and it **has zero divisors and is not a field and not a division algebra**. The block of the general plain algebra is the thirteen articles of §*The Plan of the Block*, of which this article is the first.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $TW$ | the multiplication, the general plain bilinear product |
| $T=A+Bj$ | a general element, $A=a+ia'$, $B=b+ib'$ |
| $A$, $Bj$ | the scalar part and the vector part |
| $A+B$, $A-B$ | the idempotent coordinates of $T=(A+B)\Pi_{1}+(A-B)\Pi_{2}$ |
| $\Pi_{1,2}=\tfrac12(1\pm j)$ | the two idempotents |
| $\langle T\rangle_{\natural}=A^{2}-B^{2}$ | the reduced norm and the invertibility criterion |
| $T^{-1}=\langle T\rangle_{\natural}^{-1}(A-Bj)$ | the inverse |
| $\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2}$ | the structure of the algebra as a direct product |

## Further Reading

- *Reduced Biquaternion Space* (`articles_maths/reduced-biquaternion-space.md`), above this article in this category, for the multiplication table, the idempotents and the isomorphism $\mathbb{C}\oplus\mathbb{C}$.
- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), above this article, for the four general products and the norms they carry.
- *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.md`), below this article, for the algebraic norm of the multiplication and the criterion of invertibility.
- *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), below this article, for the null cone and its structure.
- *Introduction to the Biquaternion Algebra* (`articles_maths/introduction-to-the-biquaternion-algebra.md`), the non-commutative counterpart, for the same data of an algebra with a division-adjacent structure absent here.
- *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the definitions of the unit, the inverse and the group of units used in the block.
