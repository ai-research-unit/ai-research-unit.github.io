# __Introduction to the Algebra of the Reduced Biquaternions__

## Introduction

This article reads the reduced biquaternion space with its **multiplication** and fixes it as an **algebra**: the definition of the product, the data the algebra carries, the axioms it satisfies and the plan of the block of articles that study it. The multiplication is the general plain bilinear product $\breve Q_{1}\breve Q_{2}$ of *The Four Products, Their Forms and Their Algebraic Norms*, read as the product of the algebra and not as one of four products side by side; the other three general products are not associative and are not the product of the algebra.

The general plain algebra is the **associative** case of the reduced biquaternion layer, and it is the case the rest of the category is built on. It is commutative and unital, with the unit $1$; it is **not** a field and **not** a division algebra, because it has the two idempotent lines as zero divisors; and its invertibility is decided by the reduced norm $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$, which is the algebraic norm of the tessarine bilinear product and the determinant of the multiplication (*Norm and Invertibility in the Algebra of the Reduced Biquaternions*).

**The results.** The general plain algebra is the commutative unital associative $\mathbb{R}$-algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ with basis $1,i,j,ij$ and the multiplication table of *Reduced Biquaternion Space*. Its unit is $1$, its inverse is $\breve Q^{-1}=\langle \breve Q\rangle_{\mathrm{ts}}^{-1}(Q_{\blacktriangle}-jQ_{\blacktriangledown})$ when $\langle \breve Q\rangle_{\mathrm{ts}}\neq0$, and its zero divisors are the two punctured idempotent lines. The algebra is a direct product of two copies of $\mathbb{C}$, $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$, and its multiplication is componentwise in the idempotent coordinates.

## The Algebra

### The Definition

**The general plain algebra of the reduced biquaternions is the reduced biquaternion space with its multiplication, and its product is the general plain bilinear product.**

**Definition.** The **general plain algebra of the reduced biquaternions** is the set $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ with the addition of the space and the **multiplication**
$$
(Q_{1\blacktriangle}+jQ_{1\blacktriangledown})(Q_{2\blacktriangle}+jQ_{2\blacktriangledown})=(Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown})+(Q_{1\blacktriangle}Q_{2\blacktriangledown}+Q_{1\blacktriangledown}Q_{2\blacktriangle})j,
$$
extended to the whole space by bilinearity. The product is written by juxtaposition, $\breve Q_{1}\breve Q_{2}$.

The definition is the definition of the algebra of *Reduced Biquaternion Space*; the product here is read as **the** product and not as one of the four general products, and the article fixes it as the algebra product. The general plain bilinear product is its coordinate table; the general tessarine bilinear product, the general plain sesquilinear product and the general tessarine sesquilinear product are the other three, and none of them is associative (*The Four Products, Their Forms and Their Algebraic Norms*, §*The Comparison of the Four Products*).

### The Data

**The algebra is determined by four pieces of data: the space, the product, the unit and the scalar system.**

**The data of the general plain algebra** are:

- the **space**, the real four-dimensional vector space on $1,i,j,ij$, equivalently the complex two-dimensional space on $1,j$;
- the **product**, the bilinear multiplication $(Q_{1\blacktriangle}+jQ_{1\blacktriangledown})(Q_{2\blacktriangle}+jQ_{2\blacktriangledown})=(Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown})+(Q_{1\blacktriangle}Q_{2\blacktriangledown}+Q_{1\blacktriangledown}Q_{2\blacktriangle})j$;
- the **unit**, the element $1$, two-sided and unique;
- the **scalar system**, the field $\mathbb{R}$ with the compatible complex scalar action of $\mathbb{C}$.

The data determine the algebra, since a bilinear product on a basis determines the product everywhere. The element, its coordinates and its two parts are §*The Element*; the axioms the data satisfy are §*The Algebra Axioms*.

### The Product and Its Unit

**The product is commutative, associative and unital, and the unit is $1$.**

**Theorem (the algebra axioms).** For all $\breve Q_{1},\breve Q_{2},\breve Q_{3}$ and all $\lambda\in\mathbb{R}$ the multiplication satisfies
$$
(\breve Q_{1}\breve Q_{2})\breve Q_{3}=\breve Q_{1}(\breve Q_{2}\breve Q_{3}),\qquad \breve Q_{1}\breve Q_{2}=\breve Q_{2}\breve Q_{1},\qquad 1\breve Q_{1}=\breve Q_{1}1=\breve Q_{1},\qquad \lambda(\breve Q_{1}\breve Q_{2})=(\lambda \breve Q_{1})\breve Q_{2}=\breve Q_{1}(\lambda \breve Q_{2}),
$$
and it is distributive over the addition.

*Proof.* The product is the product of the algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$, which is associative, commutative and unital, and bilinear over $\mathbb{R}$ (*Reduced Biquaternion Space*). The distributivity is the bilinearity.

The algebra is therefore an **associative commutative unital $\mathbb{R}$-algebra**, and with the complex scalar action it is also a **$\mathbb{C}$-algebra**. It is the same algebra as the complexification of the split-complex numbers, $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{D}$.

## The Element

**A general element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$, with a scalar part $Q_{\blacktriangle}$ and a $j$-part $jQ_{\blacktriangledown}$, and its idempotent coordinates $Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $Q_{\blacktriangle}-Q_{\blacktriangledown}$ are the pair that carries the product.**

**Definition.** The **$\mathbb{C}$ scalar part** of $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ is $Q_{\blacktriangle}$, the **$j$-part** is $jQ_{\blacktriangledown}$, and the **idempotent coordinates** are $Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $Q_{\blacktriangle}-Q_{\blacktriangledown}$,
$$
\breve Q=(Q_{\blacktriangle}+Q_{\blacktriangledown})\Pi_++(Q_{\blacktriangle}-Q_{\blacktriangledown})\Pi_-,\qquad \Pi_{\pm}=\tfrac12(1\pm j).
$$

The algebra has no vector part: it has no vector subspace, and the two terms are the coefficients of the scalar unit $1$ and of the hyperbolic unit $j$, both complex.

**Proposition (the multiplication in the idempotent coordinates).** For $\breve Q_{1}=(Q_{1+},Q_{1-})$ and $\breve Q_{2}=(Q_{2+},Q_{2-})$ in the idempotent coordinates $Q_{1+}=Q_{1\blacktriangle}+Q_{1\blacktriangledown}$, $Q_{1-}=Q_{1\blacktriangle}-Q_{1\blacktriangledown}$ and $Q_{2+}=Q_{2\blacktriangle}+Q_{2\blacktriangledown}$, $Q_{2-}=Q_{2\blacktriangle}-Q_{2\blacktriangledown}$,
$$
\breve Q_{1}\breve Q_{2}=(Q_{1+}Q_{2+},\;Q_{1-}Q_{2-}),
$$
the product being componentwise.

*Proof.* The idempotents are orthogonal, $\Pi_+\Pi_-=0$, and idempotent, $\Pi_\pm^{2}=\Pi_\pm$ (*Reduced Biquaternion Space*); expanding $(Q_{1+}\Pi_++Q_{1-}\Pi_-)(Q_{2+}\Pi_++Q_{2-}\Pi_-)$ kills the crossed terms and gives $Q_{1+}Q_{2+}\Pi_++Q_{1-}Q_{2-}\Pi_-$.

The proposition is the reason every question about the algebra splits into two questions about the complex numbers, and it is used in every article of the block.

## The Algebra Axioms

### Associativity

**The product is associative: $\breve Q_{1}(\breve Q_{2}\breve Q_{3})=(\breve Q_{1}\breve Q_{2})\breve Q_{3}$, and a triple of elements has a single product.**

*Proof.* In the idempotent coordinates the product is $(Q_{1+}Q_{2+},Q_{1-}Q_{2-})$, and the complex multiplication is associative in each coordinate, so $((Q_{1+}Q_{2+})Q_{3+},(Q_{1-}Q_{2-})Q_{3-})$ agrees in the two groupings; the associativity of the complex multiplication is the one fact used.

### Commutativity

**The product is commutative: $\breve Q_{1}\breve Q_{2}=\breve Q_{2}\breve Q_{1}$, and the algebra is not the quaternion algebra.**

*Proof.* The idempotent coordinates of $\breve Q_{1}\breve Q_{2}$ are $(Q_{1+}Q_{2+},Q_{1-}Q_{2-})$ and those of $\breve Q_{2}\breve Q_{1}$ are $(Q_{2+}Q_{1+},Q_{2-}Q_{1-})$, equal because the complex multiplication is commutative. In the real basis the commutativity is $ji=ij$, which is the third defining relation of *Reduced Biquaternion Space*; the product is therefore not the quaternion product, and the algebra is not $\mathbb{H}$ or $\mathbb{B}$.

### The Unit and the Inverse

**The unit is $1$, it is two-sided and unique, and an element is invertible exactly when its reduced norm $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ is nonzero, with the inverse $\breve Q^{-1}=\langle \breve Q\rangle_{\mathrm{ts}}^{-1}(Q_{\blacktriangle}-jQ_{\blacktriangledown})$.**

*Proof.* The unit is $1=1+0j$, and $1\,\breve Q=\breve Q\,1=\breve Q$. Uniqueness: if $e$ is a unit then $e=e1=1$. The criterion $\langle \breve Q\rangle_{\mathrm{ts}}\neq0$ and the inverse are *The Four Products, Their Forms and Their Algebraic Norms*, §*The Multiplicative Norm*, and the full treatment is *Norm and Invertibility in the Algebra of the Reduced Biquaternions*, below this article. In the idempotent coordinates the inverse of $(Q_{+},Q_{-})$ is $(Q_{+}^{-1},Q_{-}^{-1})$, which exists exactly when both coordinates are nonzero, that is when $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{+}Q_{-}\neq0$.

### The Absence of Division

**The algebra is not a field and not a division algebra: it has zero divisors, and the invertible elements form a proper subset of the nonzero elements.**

*Proof.* The idempotents are orthogonal and nonzero, $\Pi_+\Pi_-=0$, so $\Pi_+$ and $\Pi_-$ are zero divisors (*Reduced Biquaternion Space*); the element $(1,0)$ annihilates $(0,1)$ in the idempotent coordinates, and both are nonzero. An element whose one idempotent coordinate vanishes is a nonzero zero divisor, so the group of units is a proper subset of $\mathbb{B}_{\mathrm{r}}\setminus\{0\}$.

The zero divisors, their two families and their geometry are *Zero Divisors of the Algebra of the Reduced Biquaternions*, below this article; their annihilators are *Annihilators of the Algebra of the Reduced Biquaternions*. The **absence of division** is stated here because it bears on every statement of an inverse: an element must be tested against $\langle \breve Q\rangle_{\mathrm{ts}}\neq0$ before it is inverted.

## The Structure

**The algebra is the direct product of two copies of $\mathbb{C}$, and its maximal ideals are the two idempotent lines.**

**Theorem (the structure).** The component map $\varphi(\breve Q)=(Q_{+},Q_{-})$ is an isomorphism of $\mathbb{C}$-algebras
$$
\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-\cong\mathbb{C}\oplus\mathbb{C},
$$
and the ring is a direct product of two fields; it is not simple, its maximal ideals are the two idempotent lines $\mathbb{C}\Pi_-$ and $\mathbb{C}\Pi_+$ read as kernels of the two projections, and its only idempotents are $0,1,\Pi_+,\Pi_-$.

*Proof.* The isomorphism is *Reduced Biquaternion Space*, §*The Isomorphism with the Direct Product*; a direct product of two fields has exactly two maximal ideals, the kernels of the two projections, which are $\mathbb{C}\Pi_-$ and $\mathbb{C}\Pi_+$. The idempotents of a direct product of two fields are the four pairs of $0$ and $1$, which correspond to $0,1,\Pi_+,\Pi_-$; the computation is *Square Roots of One and the Idempotents of the Algebra of the Reduced Biquaternions*, below this article.

## The Plan of the Block

**The general plain algebra is studied in thirteen articles, and the plan is the list below.**

The block of the general plain algebra is the thirteen articles below, in the order the category follows, and its articles are:

| article | content |
|---|---|
| *Introduction to the Algebra* (this article) | the definition, the data and the plan |
| *Norm and Invertibility in the Algebra* | the algebraic norm, the invertibility criterion and the group of units |
| *Zero Divisors of the Algebra* | the null cone and its structure |
| *Annihilators of the Algebra* | the annihilators of an element and the two-sided annihilator of the structure |
| *Square Roots of One and the Idempotents* | the roots of $1$, the idempotents and the projections they carry |
| *Square Roots of Zero and the Nilpotents* | the roots of $0$ and the nilpotents, product by product |
| *Square Roots of a General Element* | the square roots of a general element |
| *The Specificities of the Algebra* | the specificities of the algebra |
| *Ideals and Peirce Decomposition* | the ideals and the Peirce decomposition |
| *The Group of Units of the Algebra* | the structure of the group of units |
| *The Forms of the Algebra* | the forms of the algebra |
| *The Multiplication Operators of the Algebra* | the left and the right multiplication maps |
| *The Algebra in the $2\times2$ Matrix Element Representation* | the $2\times2$ matrix model |

The table is the plan of the block and not a set of definitions: each row is defined in its own article, and the order of the rows is the order the category follows. The articles of the later blocks — the remarkable subspaces, the representations and operators, the topology, the analysis, the geometry and the fractals — are listed in the menu of the category and are not part of this block.

## Summary

The general plain algebra of the reduced biquaternions is the space $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ with the multiplication
$$
(Q_{1\blacktriangle}+jQ_{1\blacktriangledown})(Q_{2\blacktriangle}+jQ_{2\blacktriangledown})=(Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown})+(Q_{1\blacktriangle}Q_{2\blacktriangledown}+Q_{1\blacktriangledown}Q_{2\blacktriangle})j,
$$
the general plain bilinear product read as the product of the algebra. Its data are the space, the product, the unit and the scalar system; it is an associative, commutative, unital $\mathbb{R}$-algebra and $\mathbb{C}$-algebra, with unit $1$ and with the multiplication in the idempotent coordinates componentwise, $\breve Q_{1}\breve Q_{2}=(Q_{1+}Q_{2+},Q_{1-}Q_{2-})$ for $\breve Q_{1}=(Q_{1+},Q_{1-})$ and $\breve Q_{2}=(Q_{2+},Q_{2-})$.

An element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with scalar part $Q_{\blacktriangle}$ and $j$-part $jQ_{\blacktriangledown}$; its inverse exists exactly when the reduced norm $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ is nonzero, and it is $\breve Q^{-1}=\langle \breve Q\rangle_{\mathrm{ts}}^{-1}(Q_{\blacktriangle}-jQ_{\blacktriangledown})$. The algebra is the direct product $\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$ of two copies of $\mathbb{C}$, its maximal ideals are the two idempotent lines, its only idempotents are $0,1,\Pi_+,\Pi_-$, and it **has zero divisors and is not a field and not a division algebra**. The block of the general plain algebra is the thirteen articles of §*The Plan of the Block*, of which this article is the first.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\breve Q_{1}\breve Q_{2}$ | the multiplication, the general plain bilinear product |
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | a general element, $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$ |
| $Q_{\blacktriangle}$, $jQ_{\blacktriangledown}$ | the scalar part and the $j$-part |
| $Q_{\blacktriangle}+Q_{\blacktriangledown}$, $Q_{\blacktriangle}-Q_{\blacktriangledown}$ | the idempotent coordinates of $\breve Q=(Q_{\blacktriangle}+Q_{\blacktriangledown})\Pi_++(Q_{\blacktriangle}-Q_{\blacktriangledown})\Pi_-$ |
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | the two idempotents |
| $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ | the reduced norm and the invertibility criterion |
| $\breve Q^{-1}=\langle \breve Q\rangle_{\mathrm{ts}}^{-1}(Q_{\blacktriangle}-jQ_{\blacktriangledown})$ | the inverse |
| $\mathbb{C}\Pi_+\oplus\mathbb{C}\Pi_-$ | the structure of the algebra as a direct product |

## Further Reading

- [Reduced Biquaternion Space](reduced-biquaternion-space.html), above this article in this category, for the multiplication table, the idempotents and the isomorphism $\mathbb{C}\oplus\mathbb{C}$.
- [The Four Products, Their Forms and Their Algebraic Norms](the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.html), above this article, for the four general products and the norms they carry.
- [Norm and Invertibility in the Algebra of the Reduced Biquaternions](norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.html), below this article, for the algebraic norm of the multiplication and the criterion of invertibility.
- [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), below this article, for the null cone and its structure.
- [Introduction to the Biquaternion Algebra](introduction-to-the-biquaternion-algebra.html), the non-commutative counterpart, for the same data of an algebra with a division-adjacent structure absent here.
- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), for the definitions of the unit, the inverse and the group of units used in the block.
