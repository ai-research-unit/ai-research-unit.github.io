# __Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$__

## Introduction

This article reads the reduced biquaternion space with its two scalar systems. Over the complex numbers it is a **two-dimensional** vector space on the basis $1,j$, and an element is a pair of complex coordinates; over the real numbers it is a **four-dimensional** space on the basis $1,i,j,ij$, and an element is a quadruple of real coordinates. The two readings are the same set, and the passage from one to the other is the **change of scalars**: the complex reading is the real reading together with a distinguished real-linear operator $J$, the multiplication by the central imaginary $i$, of square $-\mathrm{id}$, and the real space is the realification of the complex one.

The article keeps the space and drops the product. Addition, the two scalar actions, the coordinate systems and the linear or antilinear character of the conjugations are what it fixes; the product is *Introduction to the Algebra of the Reduced Biquaternions*, and the four general products and the forms they carry are *The Four Products, Their Forms and Their Algebraic Norms*. The glyphs and the element $\breve Q=Q_++jQ_-$ are those of *Conventions in Mathematics*, §*The Elements and their Coefficients*, and of *Reduced Biquaternion Space*, above this article in this category.

**The results.** Over $\mathbb{C}$ the space has dimension two on the basis $1,j$, with the scalar action $\lambda(Q_++jQ_-)=\lambda Q_++j\lambda Q_-$; the two coordinates $Q_+$ and $Q_-$ are the **scalar part** and the **$j$-part**, the coefficients of $1$ and of $j$. Over $\mathbb{R}$ the space has dimension four on the basis $1,i,j,ij$, and the multiplication by $i$ is a real-linear operator $J$ with $J^{2}=-\mathrm{id}$ whose existence is what makes the complex reading possible. The realification multiplies the dimension by two, and the restriction of scalars halves it; the real reading carries two commuting square roots of $-\mathrm{id}$ behaving as diagonalisable-simultaneously operators only through the idempotent basis, and it carries the hyperbolic involution of the multiplication by $j$. Of the four conjugations, the **natural sign** is complex-linear and the **bar**, the **star** and the **flat** are complex-antilinear; this is the clause that separates the first slot of the four products from the second.

**Boundaries.** The conjugations, their fixed and anti-fixed spaces and the group they generate are *The Two Involutions and the Group of Involutions*, below this article in this category, and the fixed spaces as subspaces are *Introduction to the Remarkable Subspaces*, below this article in this category. The element representations — the four-vector, the $2\times2$ matrix and the polar forms — are the representation articles of the category. No form appears here; the four forms and their algebraic norms are *The Four Products, Their Forms and Their Algebraic Norms*, below this article. The module readings over the ring $\mathbb{B}_{\mathrm{r}}$ itself are not part of this article.

## The Complex Vector Space

### Definition and Basis

**The reduced biquaternion space over $\mathbb{C}$ is two-dimensional, and its natural complex basis is the pair $1,j$.**

**Definition.** The reduced biquaternion space, read over the complex scalars, is the set
$$
\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}=\{\breve Q=Q_++jQ_-:Q_+,Q_-\in\mathbb{C}\},
$$
with the addition of the algebra and the scalar action
$$
\lambda(Q_++jQ_-)=\lambda Q_++j\lambda Q_-,\qquad\lambda\in\mathbb{C}.
$$

The space is **two-dimensional** over $\mathbb{C}$: the basis $\{1,j\}$ is complex-linearly independent, and every element is a unique complex combination of its two members. The scalar action is the multiplication by the central imaginary $i$ extended by $\mathbb{C}$-linearity, and it is compatible with the product of the algebra, which is $\mathbb{C}$-bilinear.

**Proposition (the complex coordinates).** Every element has a unique expression $\breve Q=Q_++jQ_-$ with $Q_+,Q_-\in\mathbb{C}$; the pair $(Q_+,Q_-)$ is the **complex coordinate pair**, $Q_+$ is the **$\mathbb{C}$ scalar part** and $jQ_-$ the **$j$-part**; the algebra has no vector part.

*Proof.* Uniqueness is the linear independence of $1$ and $j$ over $\mathbb{C}$: if $Q_++jQ_-=0$ then, applying the natural sign of *The Two Involutions and the Group of Involutions*, $Q_+-jQ_-=0$, and adding the two gives $2Q_+=0$ and subtracting them gives $2jQ_-=0$, so $Q_+=Q_-=0$. Existence is the definition of the space, and the naming of the two coordinates is that of *Conventions in Mathematics*.

### The Idempotent Reading

**The same complex space is the direct sum of its two idempotent lines, and the idempotent coordinates are a second complex coordinate system on it.**

Because $\Pi_++\Pi_-=1$ and $\Pi_+-\Pi_-=j$ (*Reduced Biquaternion Space*), the basis $\{1,j\}$ and the basis $\{\Pi_+,\Pi_-\}$ of the complex space are related by the invertible complex-linear change
$$
1=\Pi_++\Pi_-,\qquad j=\Pi_+-\Pi_-,\qquad
\Pi_+=\tfrac12(1+j),\qquad \Pi_-=\tfrac12(1-j).
$$
In the idempotent basis the element $\breve Q=Q_++jQ_-$ is
$$
\breve Q=Q_{++}\Pi_++Q_{--}\Pi_-,\qquad Q_{++}=Q_++Q_-,\qquad Q_{--}=Q_+-Q_-,
$$
and the pair $(Q_{++},Q_{--})$ is the **idempotent coordinate pair**. Both pairs are complex coordinate systems on the same two-dimensional complex space; they are exchanged by the invertible matrix $\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right)$, and the choice between them is a choice of basis and not of structure. The two idempotent lines $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$ are complex lines of complex dimension one and real dimension two; they are the components of the direct product $\mathbb{C}\oplus\mathbb{C}$ of *Reduced Biquaternion Space*.

## The Real Vector Space

### The Real Basis

**Read over the real scalars the space is four-dimensional, and its natural real basis is the quadruple $1,i,j,ij$.**

**Definition.** The reduced biquaternion space, read over the real scalars, is the set
$$
\mathbb{B}_{\mathrm{r}}=\{q_++q'_+i+q_-j+q'_-ij:q_+,q'_+,q_-,q'_-\in\mathbb{R}\},
$$
with the addition of the algebra and the scalar action $\lambda(Q_++jQ_-)=\lambda Q_++j\lambda Q_-$ for $\lambda\in\mathbb{R}$.

**Proposition (the real coordinates).** Every element is a unique real combination of $1,i,j,ij$,
$$
\breve Q=q_++q'_+i+q_-j+q'_-ij,\qquad q_+,q'_+,q_-,q'_-\in\mathbb{R},
$$
and the quadruple $(q_+,q'_+,q_-,q'_-)$ is the **real coordinate quadruple**, which is the four-vector representation of *The Four-Vector Element Representation of the Reduced Biquaternions*.

*Proof.* The four elements $1,i,j,ij$ are real-linearly independent, since a real relation among them gives, in the complex coordinates, $Q_+=q_++iq'_+=0$ and $Q_-=q_-+iq'_-=0$, hence the four reals vanish; and they span, because $Q_+$ and $Q_-$ are complex. The dimension is therefore four over $\mathbb{R}$.

### The Complex Structure

**The multiplication by the central imaginary $i$ is a real-linear operator $J$ of square $-\mathrm{id}$, and it is the operator that lets the four-dimensional real space be read as a complex plane.**

**Definition.** Let $J$ be the multiplication by $i$,
$$
J(\breve Q)=i\breve Q=iQ_++ijQ_-.
$$

**Proposition.** $J$ is $\mathbb{R}$-linear, it is $\mathbb{C}$-linear as well — it is the scalar action of $i$ itself and no new operator over $\mathbb{C}$ — and
$$
J^{2}=-\mathrm{id}.
$$

*Proof.* For $\lambda\in\mathbb{R}$, $J(\lambda \breve Q)=i\lambda \breve Q=\lambda i\breve Q=\lambda J(\breve Q)$, so $J$ is real-linear; and $J^{2}(\breve Q)=i(i\breve Q)=i^{2}\breve Q=-\breve Q$. It is $\mathbb{C}$-linear as well, $J(i\breve Q)=i^{2}\breve Q=-\breve Q=iJ(\breve Q)$, since $i$ is central and commutes with the scalar action; the point is that $i$ is the **scalar** imaginary, and $J$ **is** the scalar action of $i$, so as a complex map it is the scalar $i$ and not a new operator. The operator $J$ is the complex structure of the real reading.

The real space carries a second square root of $-\mathrm{id}$ that is not the scalar action: the multiplication by $ij$, written $J_{ij}$. It satisfies $J_{ij}^{2}=-\mathrm{id}$ and commutes with $J$, $JJ_{ij}=J_{ij}J=-\text{(multiplication by }j)$, and the product $JJ_{ij}$ is an involution. The two operators are the two square roots of $-\mathrm{id}$ that the algebra supplies, and they are simultaneous only through the idempotent basis, where the multiplication by $i$ acts as $i$ on each idempotent line; this is why the complex structure $J$ is unique as the **scalar** structure, while $J_{ij}$ is a second, non-scalar, complex structure.

### The Hyperbolic Involution

**The multiplication by $j$ is a real-linear involution of square $+\mathrm{id}$, and its fixed and anti-fixed spaces are the two idempotent lines $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$.**

**Proposition.** Let $S$ be the multiplication by $j$, $S(\breve Q)=j\breve Q=jQ_++Q_-$. Then $S$ is $\mathbb{R}$-linear, $S^{2}=+\mathrm{id}$, and $S$ is the multiplication itself by the unit $j$.

*Proof.* $S^{2}(\breve Q)=j(j\breve Q)=j^{2}\breve Q=\breve Q$. The operator is the restriction to the space of the left multiplication of *The Multiplication Operators of the Algebra of the Reduced Biquaternions*, below this article in this category, at the element $j$.

The involution $S$ is **not** a conjugation in the sense of the four marks of the next article: it is the multiplication by a unit of the algebra and not an involution of the coefficient ring. The four conjugations — the bar, the natural sign, the star and the flat — are the subject of *The Two Involutions and the Group of Involutions*; here only their linear or antilinear character is used, and it is stated in §*Linear and Antilinear Maps*.

### The Realification and the Change of Scalars

**The passage from the complex reading to the real reading is the realification, it multiplies the dimension by two, and the passage back is the restriction of scalars, which halves it and keeps the complex structure.**

**Definition.** The **realification** of the complex space is the same set with the scalar action restricted to the reals; the **restriction of scalars** from $\mathbb{C}$ to $\mathbb{R}$ is that passage, and its inverse, the complexification of the real space, is the passage that inserts the operator $J$.

**Proposition (the dimensions).** The realification has real dimension twice the complex dimension,
$$
\dim_{\mathbb{R}}\mathbb{B}_{\mathrm{r}}=2\dim_{\mathbb{C}}\mathbb{B}_{\mathrm{r}}=4,
$$
and the passage is exactly the reading of the complex basis $\{1,j\}$ on the real basis $\{1,i,j,ij\}$, namely $1=1$ and $j=j$ with the two complex scalar coordinates split into four real ones by $Q_+=q_++iq'_+$ and $Q_-=q_-+iq'_-$.

*Proof.* The real basis is obtained from the complex one by replacing each complex basis element by its real and imaginary parts: $1$ is already real, and $j$ gives $j$ and $ij$. The two complex coordinates $Q_+,Q_-$ give the four real coordinates $(q_+,q'_+,q_-,q'_-)$ of the proposition on the real coordinates. The inverse passage is the insertion of $J$, which reads two real directions as one complex one.

**Remark (the ring-based readings are not this).** The realification and the complexification are passages between the two **field-based** readings of the same set. The set read as a module over the ring $\mathbb{B}_{\mathrm{r}}$ itself, with the scalar action the multiplication of the algebra, is a different object, and it is not part of this article. The warning is the one of the introduction, and the distinction is the same as in the biquaternion category between the complex vector space and the module over the algebra.

## The Coordinate Systems

**The same element is written in three coordinate systems, of four, two and four real or complex numbers, and they are the real, the complex and the idempotent readings of the space.**

| reading | basis | count | scalars | coordinates of $\breve Q$ |
|---|---|---|---|---|
| real | $1,i,j,ij$ | $4$ | $\mathbb{R}$ | $(q_+,q'_+,q_-,q'_-)$ |
| complex | $1,j$ | $2$ | $\mathbb{C}$ | $(Q_+,Q_-)$ |
| idempotent | $\Pi_+,\Pi_-$ | $2$ | $\mathbb{C}$ | $(Q_{++},Q_{--})$ |

The first and the third are real- or complex-based readings of the same four real coordinates; the second and the third are two complex bases of the same two-dimensional complex space. The table is the reduced biquaternion instance of the coordinate table of *The Biquaternion Algebra as a Vector Space over $\mathbb{C}$ and $\mathbb{R}$*, with the quaternionic coordinate system absent because the algebra has no quaternionic factor.

## Linear and Antilinear Maps

**Of the four conjugations the natural sign is $\mathbb{C}$-linear and the bar, the star and the flat are $\mathbb{C}$-antilinear, and this is the clause that decides which slot of a product carries a conjugation.**

The conjugations are defined in *The Two Involutions and the Group of Involutions*; here only their action on the scalars is recorded. For $\lambda\in\mathbb{C}$ and $\breve Q=Q_++jQ_-$:
$$
\overline{\lambda \breve Q}=\bar\lambda\,\overline{\breve Q},\qquad
(\lambda \breve Q)^{\natural}=\lambda\,\breve Q^{\natural},\qquad
(\lambda \breve Q)^{*}=\bar\lambda\,\breve Q^{*},\qquad
(\lambda \breve Q)^{\flat}=\bar\lambda\,\breve Q^{\flat}.
$$

**Proof.** The bar conjugates the two complex coordinates, and the conjugate of a product of complex numbers is the product of the conjugates, so it is antilinear; the natural sign negates the second coordinate and leaves the first, $(\lambda Q_+)-(\lambda Q_-)j=\lambda(Q_+-jQ_-)$, so it is linear; the star is the composite of the bar and the natural sign and is antilinear as the composite of an antilinear and a linear map; and the flat is $-{}^{*}$, which is antilinear as well since $-1$ is real.

**Corollary (which slot carries which conjugation).** A product whose first slot carries the natural sign and whose second slot carries the star,
$$
\breve Q_{1}^{\natural}\breve Q_{2}\quad\text{and}\quad \breve Q_{1}^{\natural}\breve Q_{2}^{*},
$$
is $\mathbb{C}$-**linear in the first** variable and, for the star, $\mathbb{C}$-**antilinear in the second**; a product whose first slot carries the identity is $\mathbb{C}$-linear in the first variable. This is the definitional clause of *The Four Products, Their Forms and Their Algebraic Norms*, and it is the reason the two sesquilinear products are the ones carrying the star.

The map $J$ of §*The Complex Structure* is the other side of the same coin: it is the real-linear operator of the complex structure, and it is the scalar action that the antilinear maps fail to commute with. The distinction *linear against antilinear* over $\mathbb{C}$ and the distinction *real structure against complex structure* are two readings of the same fact, and the corpus keeps both.

## The Remarkable Subspaces, Named

**The conjugations of the next article cut the real space into fixed and anti-fixed spaces, and this article names them only.**

The six fixed and anti-fixed spaces of the bar, the natural sign and the star are the **remarkable subspaces** of the space, and they are defined one to a section in *Introduction to the Remarkable Subspaces*, with the two decompositions they produce in *Decompositions Along the Remarkable Subspaces* and the table of all of them in *Comparison of the Remarkable Subspaces*. Three of them are read from the coordinates already fixed here:

- the fixed space of the **natural sign** is the **scalar line** $\mathbb{C}=\{A:A\in\mathbb{C}\}$, of real dimension two, spanned by $1,i$;
- the anti-fixed space of the **natural sign** is the **$j$-line**, of real dimension two, spanned by $j,ij$;
- the fixed space of the **bar** is the **real subalgebra** $\{a+bj:a,b\in\mathbb{R}\}$, of real dimension two, the split-complex numbers inside $\mathbb{B}_{\mathrm{r}}$.

**Remark (the algebra is commutative, so its ring centre is not a proper subspace).** Unlike the biquaternion algebra, whose centre is the scalar line $\mathbb{C}e_t$ and one of its remarkable subspaces, the reduced biquaternion algebra is commutative, so its **ring centre is the whole algebra** and the scalar line is not its centre but its scalar line. Where the biquaternion category reads a *central* subspace, this category reads the **scalar line**, and the difference is taken up in *Comparison of the Remarkable Subspaces*. The warning is stated here because it bears on every later use of the word *central*: in this category *central* names an element of the scalar line $\mathbb{C}$, or the property of commuting with everything, which here is shared by every element.

## Summary

Read over the complex scalars the reduced biquaternion space is two-dimensional on the basis $1,j$, with the scalar action $\lambda(Q_++jQ_-)=\lambda Q_++j\lambda Q_-$, and an element is the complex coordinate pair $(Q_+,Q_-)$ whose members are the scalar part $Q_+$ and the $j$-part $jQ_-$. Read over the real scalars it is four-dimensional on the basis $1,i,j,ij$, and an element is the real quadruple $(q_+,q'_+,q_-,q'_-)$. The two readings are the same set: the complex one is the real one together with the complex structure
$$
J(\breve Q)=i\breve Q,\qquad J^{2}=-\mathrm{id},
$$
and the passage between them is the realification and the restriction of scalars, which double and halve the dimension. The multiplication by $j$ is a real-linear involution $S$, $S^{2}=+\mathrm{id}$, with the two idempotent lines $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$ as fixed and anti-fixed space; and the multiplication by $ij$ is a second non-scalar square root of $-\mathrm{id}$ commuting with $J$.

A second complex coordinate system is the idempotent one, $(\Pi_+,\Pi_-)$, in which $\breve Q=Q_{++}\Pi_++Q_{--}\Pi_-$ and the space is the direct sum of the two complex idempotent lines. Of the four conjugations the **natural sign** is $\mathbb{C}$-linear and the **bar**, the **star** and the **flat** are $\mathbb{C}$-antilinear, and this is the clause that decides which slot of each of the four general products carries a conjugation. The remarkable subspaces are named and not developed; the scalar line $\mathbb{C}$ plays in this category the role the centre $\mathbb{C}e_t$ plays in the biquaternion category, the algebra being commutative.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\breve Q=Q_++jQ_-$ | an element in the complex reading, $Q_+,Q_-\in\mathbb{C}$ |
| $\lambda(Q_++jQ_-)=\lambda Q_++j\lambda Q_-$ | the complex scalar action |
| $(Q_+,Q_-)$ | the complex coordinate pair |
| $1,i,j,ij$ | the real basis |
| $(q_+,q'_+,q_-,q'_-)$ | the real coordinate quadruple, $Q_+=q_++iq'_+$, $Q_-=q_-+iq'_-$ |
| $J$ | the multiplication by $i$, the complex structure, $J^{2}=-\mathrm{id}$ |
| $S$ | the multiplication by $j$, the hyperbolic involution, $S^{2}=+\mathrm{id}$ |
| $J_{ij}$ | the multiplication by $ij$, a non-scalar complex structure, $J_{ij}^{2}=-\mathrm{id}$ |
| $\Pi_{\pm}=\tfrac12(1\pm j)$ | the idempotent basis, with $\breve Q=Q_{++}\Pi_++Q_{--}\Pi_-$ |
| $(Q_{++},Q_{--})$ | the idempotent coordinate pair |
| linear / antilinear | the action of the natural sign against that of the bar, the star and the flat |
| $\mathbb{C}$ | the scalar line, fixed space of the natural sign |

## Further Reading

- [Reduced Biquaternion Space](reduced-biquaternion-space.html), above this article in this category, for the algebra, the idempotents and the isomorphism $\mathbb{C}\oplus\mathbb{C}$.
- [The Two Involutions and the Group of Involutions](the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.html), below this article, for the bar, the natural sign, the star and the flat and the group they generate.
- [The Four Products, Their Forms and Their Algebraic Norms](the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.html), below this article, for the four general products and the clause that decides which slot carries a conjugation.
- [The Four-Vector Element Representation of the Reduced Biquaternions](the-four-vector-element-representation-of-the-reduced-biquaternions.html), for the real quadruple and the complex pair as element representations.
- [Conventions in Mathematics](conventions-in-mathematics.html), §*The Elements and their Coefficients*, for the scalar part, the $j$-part and the two complex coordinates.
- [The Biquaternion Algebra as a Vector Space over $\mathbb{C}$ and $\mathbb{R}$](the-biquaternion-algebra-as-a-vector-space-over-c-and-r.html), for the coordinate systems of the non-commutative companion, whose quaternionic row is absent here.
- [The Split-Complexoid as a Vector Space over $\mathbb{R}$](the-split-complexoid-as-a-vector-space-over-r.html), for the real companion $\mathbb{D}$ and its self-interpretation over the algebra.
