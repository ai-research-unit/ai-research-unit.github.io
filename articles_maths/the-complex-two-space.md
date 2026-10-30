# __Complex Two-Space__

## Introduction

The complex two-space is the set of ordered pairs of complex numbers,
$$
\mathbb{C}^2=\{(Q_{\blacktriangle},Q_{\blacktriangledown}):Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{C}\},
$$
with its two scalar structures: the complex one, which makes it a complex vector space of dimension two, and the real one, which makes it a real vector space of dimension four. This article fixes the **space**: the set, the two structures, the bases, the complex structure $J$, the Hermitian form $H$ and the norm, and the three canonical forms $H$, $B$ and $\omega$ announced but not developed. It is the entry point of the category.

The article states the definitions and the elementary propositions that every later article assumes. It does not prove the properties of the three forms — their Gram matrices, their isotropy and their real pictures are *The Three Canonical Forms on $\mathbb{C}^2$* — and it does not treat the topology, the analysis or the geometry of the space, which are the articles that follow. The general theory of holomorphic functions of several variables is not restated here; it is *Several Complex Variables*, and this category reads its two-variable case on the space fixed below.

One warning is stated at once. **The number that measures the size of $\mathbb{C}^2$ is not a property of the set: it is $2$ over $\mathbb{C}$ and $4$ over $\mathbb{R}$.** The two numbers are both correct, they count different things, and no statement in this category is allowed to leave the field implicit.

The space is also the natural module of the matrix algebra. The algebra $M_2(\mathbb{C})$ acts on $\mathbb{C}^2$ by $TQ$, and $M_2(\mathbb{C})$ is the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$; the space is therefore the simple module, or the spinor module, of the biquaternion algebra (*The Endomorphisms of $\mathbb{C}^2$*, and *The Biquaternion Algebra*). Nothing of that reading is used below: the space is fixed first, and the operators come after.

## The Set and the Two Scalar Structures

**The set carries two scalar multiplications, one by the field $\mathbb{C}$ and one by its subfield $\mathbb{R}$, and the two are not interchangeable.**

**Definition.** The **complex two-space** is the set $\mathbb{C}^2$ with the addition
$$
(Q_{1\blacktriangle},Q_{1\blacktriangledown})+(Q_{2\blacktriangle},Q_{2\blacktriangledown})=(Q_{1\blacktriangle}+Q_{2\blacktriangle},\,Q_{1\blacktriangledown}+Q_{2\blacktriangledown})
$$
and the **complex scalar multiplication**
$$
\lambda\cdot(Q_{\blacktriangle},Q_{\blacktriangledown})=(\lambda Q_{\blacktriangle},\lambda Q_{\blacktriangledown}),\qquad \lambda\in\mathbb{C}.
$$

The same formula with $\lambda$ restricted to $\mathbb{R}$ makes $\mathbb{C}^2$ a real vector space. The second structure is the **restriction of scalars** of the first: every complex scalar is a real scalar, and the real multiplication is the complex one read on the subfield $\mathbb{R}\subset\mathbb{C}$.

**Proposition (the two dimensions).** The space $\mathbb{C}^2$ has dimension $2$ over $\mathbb{C}$ and dimension $4$ over $\mathbb{R}$.

*Proof.* The pair $e_1=(1,0)$, $e_2=(0,1)$ is a complex basis: every $Q$ is $Q_{\blacktriangle}e_1+Q_{\blacktriangledown}e_2$ with complex coefficients, and the two vectors are independent over $\mathbb{C}$. For the real reading, each complex coordinate splits, $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$ with real parameters, so
$$
Q=q_{\blacktriangle}e_1+q'_{\blacktriangle}(ie_1)+q_{\blacktriangledown}e_2+q'_{\blacktriangledown}(ie_2),
$$
and the four vectors $e_1,ie_1,e_2,ie_2$ are independent over $\mathbb{R}$: a real relation $a_1e_1+b_1ie_1+a_2e_2+b_2ie_2=0$ reads $(a_1+ib_1,a_2+ib_2)=0$, hence $a_1=b_1=a_2=b_2=0$. Hence $4=2\cdot 2$.

The two structures are collected in one table.

| Structure | Field | Dimension | Basis | Endomorphisms |
|---|---|---|---|---|
| complex | $\mathbb{C}$ | $2$ | $e_1,e_2$ | $M_2(\mathbb{C})$, real dimension $8$ |
| real | $\mathbb{R}$ | $4$ | $e_1,ie_1,e_2,ie_2$ | $M_4(\mathbb{R})$, real dimension $16$ |

**Remark (the restriction is not reversible).** Every complex vector space is a real vector space by restriction, but a real vector space of even dimension is not a complex one until a complex structure is chosen. **The passage from the complex reading to the real reading loses information, and the information lost is exactly $J$.** The real space $\mathbb{R}^4$ carries many complex structures, not one (*The Realification of $\mathbb{C}^2$*).

## The Basis and the Coordinates

**The complex basis has two vectors, the real basis four, and the coordinates of a point carry the same triangle in the two bases.**

**Definition.** The **standard complex basis** is $e_1=(1,0)$ and $e_2=(0,1)$. A point is written
$$
Q=Q_{\blacktriangle}e_1+Q_{\blacktriangledown}e_2,\qquad Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle},\quad Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown},
$$
with the four parameters real. The **standard real basis** is
$$
e_1=(1,0),\qquad ie_1=(i,0),\qquad e_2=(0,1),\qquad ie_2=(0,i),
$$
in this order, and the same point is
$$
Q=q_{\blacktriangle}e_1+q'_{\blacktriangle}(ie_1)+q_{\blacktriangledown}e_2+q'_{\blacktriangledown}(ie_2).
$$

**Remark (the real basis is not a complex basis).** The four real basis vectors are dependent over $\mathbb{C}$, since $ie_1=i\,e_1$ and $ie_2=i\,e_2$. **The real basis has four elements and the complex basis two; the complex basis is a sublist of the real one, but it is a basis only over $\mathbb{C}$, and the real basis is a basis only over $\mathbb{R}$.**

The coordinates are gathered below. **The triangles label the two coordinates and the digits label the basis.** The ascending triangle marks the first coordinate and the descending triangle the second; the real and imaginary parts of a coordinate carry its triangle, $q_{\blacktriangle}$ and $q'_{\blacktriangle}$ for the first and $q_{\blacktriangledown}$ and $q'_{\blacktriangledown}$ for the second, and the prime marks the imaginary part.

| Point | Complex coordinates | Real coordinates |
|---|---|---|
| $Q$ | $(Q_{\blacktriangle},Q_{\blacktriangledown})$ | $(q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown})$ |
| $e_1$ | $(1,0)$ | $(1,0,0,0)$ |
| $ie_1$ | $(i,0)$ | $(0,1,0,0)$ |
| $e_2$ | $(0,1)$ | $(0,0,1,0)$ |
| $ie_2$ | $(0,i)$ | $(0,0,0,1)$ |

## The Complex Structure $J$

**The complex structure is the real operator of multiplication by $i$; it is the single datum that distinguishes the complex reading of $\mathbb{R}^4$ from the real one.**

**Definition.** The **complex structure** is the map
$$
J:\mathbb{C}^2\longrightarrow\mathbb{C}^2,\qquad J(Q_{\blacktriangle},Q_{\blacktriangledown})=(iQ_{\blacktriangle},iQ_{\blacktriangledown}).
$$

In the real coordinates $(q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown})$ of the standard basis it is
$$
J(q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown})=(-q'_{\blacktriangle},q_{\blacktriangle},-q'_{\blacktriangledown},q_{\blacktriangledown}),
$$
with matrix
$$
J=\begin{pmatrix}0&-1&0&0\\ 1&0&0&0\\ 0&0&0&-1\\ 0&0&1&0\end{pmatrix}.
$$

**Proposition (the defining identity).** The operator $J$ is real-linear, it satisfies $J^2=-I$, and it is complex-linear.

*Proof.* The map is real-linear because multiplication by $i$ is real-linear on each coordinate. Applying it twice returns $(i^2Q_{\blacktriangle},i^2Q_{\blacktriangledown})=(-Q_{\blacktriangle},-Q_{\blacktriangledown})$. It is complex-linear because $J(\lambda Q)=i\lambda Q=\lambda(iQ)=\lambda J(Q)$ for every $\lambda\in\mathbb{C}$.

**Theorem (a complex structure is an operator with square $-1$).** Let $W$ be a real vector space and $T:W\to W$ a real-linear map with $T^2=-I$. Then $W$ is a complex vector space under
$$
(\alpha+i\beta)\,w=\alpha w+\beta T w,\qquad \alpha,\beta\in\mathbb{R},
$$
and conversely the multiplication by $i$ of a complex vector space is such a $T$.

*Proof.* The addition is the given one. The scalar multiplication is real-linear in $w$ and satisfies $(1+0i)w=w$; it is additive in the scalar because $T$ is linear; and
$$
\bigl((\alpha+i\beta)(\gamma+i\delta)\bigr)w=(\alpha\gamma-\beta\delta)w+(\alpha\delta+\beta\gamma)Tw
=\alpha(\gamma w+\delta Tw)+\beta T(\gamma w+\delta Tw),
$$
using $T^2=-I$ in the second equality, which is the associativity of the action. The converse is the identity $i^2=-1$. The axioms of a complex vector space follow, and the two constructions are inverse because $T$ is multiplication by $i$ in the structure it defines.

**Proposition (the eigenvalues).** As a real operator, $J$ has no eigenvector. As a complex-linear operator on $\mathbb{C}^2$, it is the scalar $i$ and has the single eigenvalue $i$. On the complexification $\mathbb{C}^2\otimes_{\mathbb{R}}\mathbb{C}$ it has the eigenvalues $i$ and $-i$, each with eigenspace of complex dimension $2$.

*Proof.* A real eigenvector would satisfy $JQ=\lambda Q$ with $\lambda\in\mathbb{R}$, hence $-Q=J^2Q=\lambda^2Q$ and $\lambda^2=-1$, which has no real solution. Over $\mathbb{C}$, $J$ is multiplication by $i$ on the whole space, so the eigenvalue is $i$ and the eigenspace is the whole space. The complexification splits as $V\oplus\bar V$, and $J$ acts as $i$ on the first summand and as $-i$ on the second, by the definition of the conjugate structure.

**Remark (no real eigenvector is not a defect).** The absence of a real eigenvector is what makes $J$ a rotation by a quarter turn in each coordinate plane, and it is the reason a real-linear map that commutes with $J$ has a block structure rather than a diagonal one. **The operator $J$ is not diagonalisable over $\mathbb{R}$ and is diagonalisable over $\mathbb{C}$, with the two eigenvalues $\pm i$.**

## The Hermitian Form and the Norm

**The Hermitian form is the positive definite form of the space, and it is the only one of the three canonical forms that defines a norm.**

**Definition.** The **Hermitian form** is
$$
H(Q_1,Q_2)=Q_{1\blacktriangle}\overline{Q_{2\blacktriangle}}+Q_{1\blacktriangledown}\overline{Q_{2\blacktriangledown}}.
$$
The **norm** is $\lVert Q\rVert=\sqrt{H(Q,Q)}=\sqrt{\lvert Q_{\blacktriangle}\rvert^2+\lvert Q_{\blacktriangledown}\rvert^2}$, and the **distance** is $d(Q_1,Q_2)=\lVert Q_1-Q_2\rVert$.

The form is linear in its first slot and conjugate-linear in its second: $H(\lambda Q_1,Q_2)=\lambda H(Q_1,Q_2)$ and $H(Q_1,\lambda Q_2)=\overline{\lambda}H(Q_1,Q_2)$. It is **Hermitian**,
$$
H(Q_2,Q_1)=\overline{H(Q_1,Q_2)},
$$
and **positive definite**, $H(Q,Q)>0$ for $Q\neq0$.

**Proposition (the norm is the Euclidean norm of $\mathbb{R}^4$).** In the real coordinates,
$$
H(Q,Q)=q_{\blacktriangle}^2+{q'_{\blacktriangle}}^2+q_{\blacktriangledown}^2+{q'_{\blacktriangledown}}^2.
$$

*Proof.* $\lvert Q_{\blacktriangle}\rvert^2=q_{\blacktriangle}^2+{q'_{\blacktriangle}}^2$ and likewise for the descending triangle, and the sum is the displayed expression.

**Proposition (Cauchy–Schwarz and the triangle inequality).** For all $Q_1,Q_2\in\mathbb{C}^2$,
$$
\lvert H(Q_1,Q_2)\rvert\le\lVert Q_1\rVert\,\lVert Q_2\rVert,\qquad \lVert Q_1+Q_2\rVert\le\lVert Q_1\rVert+\lVert Q_2\rVert.
$$

*Proof.* The first is the Cauchy–Schwarz inequality for the positive definite Hermitian form: the discriminant of the non-negative quadratic $t\mapsto\lVert Q_1+tQ_2\rVert^2$ is non-positive. The second follows from the first applied to $\lVert Q_1+Q_2\rVert^2=\lVert Q_1\rVert^2+2\operatorname{Re}H(Q_1,Q_2)+\lVert Q_2\rVert^2$.

**Theorem (polarisation).** The form is recovered from its norm by
$$
H(Q_1,Q_2)=\tfrac14\Bigl(\lVert Q_1+Q_2\rVert^2-\lVert Q_1-Q_2\rVert^2+i\lVert Q_1+iQ_2\rVert^2-i\lVert Q_1-iQ_2\rVert^2\Bigr).
$$

*Proof.* Expanding the four squares and using the sesquilinearity of $H$, the real terms give $4\operatorname{Re}H(Q_1,Q_2)$ and the two imaginary terms give $4i\operatorname{Im}H(Q_1,Q_2)$; the sum is $4H(Q_1,Q_2)$.

**Remark (the product is not complex-bilinear).** The form $H$ cannot be $\mathbb{C}$-bilinear: $H(iQ_1,Q_2)=iH(Q_1,Q_2)$ but $H(Q_1,iQ_2)=-iH(Q_1,Q_2)$. **The asymmetry of the two slots is the mark of a Hermitian form, and it is the reason the real and imaginary parts of $H$ are two different real forms**, the Euclidean metric and a symplectic form (*The Realification of $\mathbb{C}^2$*).

## The Three Canonical Forms Announced

**The space carries three canonical forms, one Hermitian, one complex bilinear symmetric and one complex bilinear alternating; they are distinct objects, and only the first defines a norm.**

**Definition.** Besides $H$, the space carries
$$
B(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown},\qquad \omega(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangledown}-Q_{1\blacktriangledown}Q_{2\blacktriangle}.
$$

The three are collected below. The column *realified signature* records the signature of the real bilinear form obtained by taking the real or the imaginary part, as appropriate; the construction is *The Realification of $\mathbb{C}^2$*, and the signatures are proved in *The Three Canonical Forms on $\mathbb{C}^2$*.

| Form | Definition | Linearity | Symmetry | Realified signature | Vanishing set |
|---|---|---|---|---|---|
| $H$ | $Q_{1\blacktriangle}\overline{Q_{2\blacktriangle}}+Q_{1\blacktriangledown}\overline{Q_{2\blacktriangledown}}$ | sesquilinear, antilinear in the second slot | $H(Q_2,Q_1)=\overline{H(Q_1,Q_2)}$ | $(4,0)$ | $\{0\}$ |
| $B$ | $Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ | $\mathbb{C}$-bilinear | $B(Q_2,Q_1)=B(Q_1,Q_2)$ | $(2,2)$ for $\operatorname{Re}B$, $(2,2)$ for $\operatorname{Im}B$ | the two lines $Q_{\blacktriangle}=\pm iQ_{\blacktriangledown}$ |
| $\omega$ | $Q_{1\blacktriangle}Q_{2\blacktriangledown}-Q_{1\blacktriangledown}Q_{2\blacktriangle}$ | $\mathbb{C}$-bilinear | $\omega(Q_2,Q_1)=-\omega(Q_1,Q_2)$ | $\operatorname{Re}\omega$ and $\operatorname{Im}\omega$ symplectic | every complex line |

**Remark (three forms, three roles).** The form $H$ is **definite**: its only isotropic vector is $0$, and it carries the topology. The form $B$ is **symmetric and indefinite**: its isotropic set is a cone of two complex lines, and it is the form whose isometry group is the complex orthogonal group. The form $\omega$ is **alternating and nondegenerate**: every complex line is isotropic for it, and it is the holomorphic symplectic form, whose isometry group is $\mathrm{Sp}(2,\mathbb{C})$. **No one of the three may be substituted for another, and the same symbol is never used for two of them.**

The three are related by the complex structure and by the real and imaginary parts, and the relations are stated where they are proved. Two of them are needed at once. First, $B$ and $\omega$ satisfy
$$
B(Q_1,Q_2)^2+\omega(Q_1,Q_2)^2=B(Q_1,Q_1)\,B(Q_2,Q_2),
$$
the Lagrange identity for two complex variables. Second, $\operatorname{Im}H$ is not $\omega$: the first is a real alternating form of type $(1,1)$, invariant under $J$, and the second is a complex alternating form of type $(2,0)$, anti-invariant under $J$ in the sense that $\omega(JQ_1,JQ_2)=-\omega(Q_1,Q_2)$. **The Kähler form of the space is $-\operatorname{Im}H$, not $\omega$**, and the confusion of the two is the commonest error in the reading of the forms (*The Three Canonical Forms on $\mathbb{C}^2$*).

## The Distinctions of Notation

**Four different objects are written with the same letter $\mathbb{C}$ and the same exponent $2$, and only one of them is the space of this article.**

**Definition.** The four are the following.

- $\mathbb{C}^2$ is the set of ordered pairs of complex numbers, with the two scalar structures above. It is a complex vector space of dimension $2$, a real vector space of dimension $4$, and it is contractible.
- $\mathbb{C}^2(\Omega)$, for a domain $\Omega\subset\mathbb{C}^n$, is the space of holomorphic maps $\Omega\to\mathbb{C}^2$, that is $\mathcal{O}(\Omega)^2$. It is a module over the ring $\mathcal{O}(\Omega)$ and an infinite-dimensional complex vector space.
- $\mathbb{C}^2(X)$, for a space $X$, is the space of sections of the trivial complex vector bundle $X\times\mathbb{C}^2\to X$, equivalently the space of maps $X\to\mathbb{C}^2$ of the chosen regularity. It is a module over the functions on $X$, and it depends on $X$; for $X$ a point it is $\mathbb{C}^2$.
- $\mathbb{CP}^2$ is the set of complex lines through the origin of $\mathbb{C}^3$, that is $(\mathbb{C}^3\setminus\{0\})/\mathbb{C}^{\times}$. It is a compact real manifold of dimension $4$ and it is not a vector space.

| Notation | Object | Real dimension | Compact | Vector space |
|---|---|---|---|---|
| $\mathbb{C}^2$ | pairs of complex numbers | $4$ | no | yes, over $\mathbb{C}$ and over $\mathbb{R}$ |
| $\mathbb{C}^2(\Omega)$ | holomorphic maps $\Omega\to\mathbb{C}^2$ | infinite | no | yes, over $\mathbb{C}$ |
| $\mathbb{C}^2(X)$ | sections of $X\times\mathbb{C}^2$ | infinite in general | depends on $X$ | yes, over $\mathbb{C}$ |
| $\mathbb{CP}^2$ | complex lines in $\mathbb{C}^3$ | $4$ | yes | no |

**Remark (why $\mathbb{C}^2$ and $\mathbb{CP}^2$ are not homeomorphic).** The space $\mathbb{C}^2$ is contractible, so its homology is that of a point; the projective plane has $H_2(\mathbb{CP}^2;\mathbb{Z})=\mathbb{Z}$ and Euler characteristic $3$. **The exponent $2$ in the two symbols counts the same complex dimension and does not denote the same object**: $\mathbb{C}^2$ is the space, $\mathbb{CP}^2$ is its projectivisation, obtained by adding the line at infinity (*The Compactifications of $\mathbb{C}^2$*).

**Remark (the function spaces are not the space).** The notation $\mathbb{C}^2(\Omega)$ is read "the maps from $\Omega$ to $\mathbb{C}^2$", not "$\mathbb{C}^2$ evaluated at $\Omega$". **A function space is infinite-dimensional and carries a topology of its own, and its study is the subject of *Several Complex Variables*, not of this article.** The distinction matters because a statement about $\mathbb{C}^2$ is a statement about points, and a statement about $\mathbb{C}^2(\Omega)$ is a statement about functions.

## The Position Among the Objects of Part VI

**The space is not an algebra, and it is placed after the number systems for that reason: it is the first object of the synthetic part that is a module and not a ring.**

The categories that precede it are algebras: $\mathbb{C}$, the split-complex numbers, the dual numbers, and the variants gathered in the complexoid and split-complexoid categories, each with a product, a conjugation and a norm. The space $\mathbb{C}^2$ has none of these as part of its definition. Its product-like structures are the three forms, which take two arguments and return a scalar; its operators are the matrices, which are treated in the next two articles. **The reader who expects a multiplication table will not find one here, and the absence is the point.**

The space is nevertheless the module of the algebras that follow. The algebra $M_2(\mathbb{C})$ acts on $\mathbb{C}^2$ by matrix multiplication, and its group of units $\mathrm{GL}_2(\mathbb{C})$ acts faithfully and transitively on the nonzero vectors: for any two nonzero vectors there is an invertible matrix sending one to the other. The algebra $M_2(\mathbb{C})$ is isomorphic to the biquaternion algebra $\mathbb{B}$, so the space is the **simple module** of $\mathbb{B}$, and the classification of the simple modules of a matrix algebra, which is the contents of *The Endomorphisms of $\mathbb{C}^2$* and of the biquaternion category, has this space as its unique object up to isomorphism.

## Summary

The complex two-space is the set $\mathbb{C}^2$ of ordered pairs of complex numbers. It is a complex vector space of dimension $2$, with basis $e_1=(1,0)$ and $e_2=(0,1)$, and a real vector space of dimension $4$, with basis $e_1,ie_1,e_2,ie_2$; a point is $Q=Q_{\blacktriangle}e_1+Q_{\blacktriangledown}e_2$ with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$, and the two readings are related by the complex structure
$$
J(Q_{\blacktriangle},Q_{\blacktriangledown})=(iQ_{\blacktriangle},iQ_{\blacktriangledown}),\qquad J^2=-I,
$$
which is real-linear and complex-linear and has no real eigenvector.

The **Hermitian form** is $H(Q_1,Q_2)=Q_{1\blacktriangle}\overline{Q_{2\blacktriangle}}+Q_{1\blacktriangledown}\overline{Q_{2\blacktriangledown}}$, positive definite and conjugate-linear in the second slot; its norm is the Euclidean norm of $\mathbb{R}^4$, $\lVert Q\rVert^2=q_{\blacktriangle}^2+{q'_{\blacktriangle}}^2+q_{\blacktriangledown}^2+{q'_{\blacktriangledown}}^2$, and the form is recovered from the norm by polarisation. The space carries two further canonical forms, the complex bilinear symmetric form $B(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ and the complex bilinear alternating form $\omega(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangledown}-Q_{1\blacktriangledown}Q_{2\blacktriangle}$; only $H$ is definite, $B$ has the isotropic cone $Q_{\blacktriangle}=\pm iQ_{\blacktriangledown}$, and $\omega$ vanishes on every complex line. The Kähler form of the space is $-\operatorname{Im}H$, and it is not $\omega$.

The notation is distinguished four ways: $\mathbb{C}^2$ is the pair space, contractible and of real dimension $4$; $\mathbb{C}^2(\Omega)$ is the space of holomorphic maps on a domain, infinite-dimensional; $\mathbb{C}^2(X)$ is the space of sections of a trivial bundle over $X$; and $\mathbb{CP}^2$ is the compact projective plane, not a vector space. The space is the simple module of $M_2(\mathbb{C})\cong\mathbb{B}$, and it is the entry point of the category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}^2$ | the set of ordered pairs of complex numbers, with the complex and the real scalar structures |
| $Q=(Q_{\blacktriangle},Q_{\blacktriangledown})$ | a point, with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$ |
| $e_1,e_2$ | the standard complex basis, $e_1=(1,0)$, $e_2=(0,1)$ |
| $e_1,ie_1,e_2,ie_2$ | the standard real basis |
| $J$ | the complex structure, $JQ=iQ$, $J^2=-I$ |
| $H(Q_1,Q_2)=Q_{1\blacktriangle}\overline{Q_{2\blacktriangle}}+Q_{1\blacktriangledown}\overline{Q_{2\blacktriangledown}}$ | the Hermitian form |
| $\lVert Q\rVert=\sqrt{H(Q,Q)}$ | the norm, the Euclidean norm of $\mathbb{R}^4$ |
| $d(Q_1,Q_2)=\lVert Q_1-Q_2\rVert$ | the distance |
| $B(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ | the complex bilinear symmetric form |
| $\omega(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangledown}-Q_{1\blacktriangledown}Q_{2\blacktriangle}$ | the holomorphic symplectic form |
| $\Omega=-\operatorname{Im}H=dq_{\blacktriangle}\wedge dq'_{\blacktriangle}+dq_{\blacktriangledown}\wedge dq'_{\blacktriangledown}$ | the Kähler form |
| $\mathbb{C}^2(\Omega)$ | the space of holomorphic maps $\Omega\to\mathbb{C}^2$ |
| $\mathbb{C}^2(X)$ | the space of sections of $X\times\mathbb{C}^2\to X$ |
| $\mathbb{CP}^2$ | the projective plane, the complex lines of $\mathbb{C}^3$ |

## Further Reading

- [Conventions in Mathematics](conventions-in-mathematics.html), for the glyphs, the case rule of the elements and the typographic conventions of the corpus.
- [The Realification of $\mathbb{C}^2$](the-realification-of-the-complex-two-space.html), below in this category, for the real reading of the space, the linear and conjugate-linear maps and the dictionary.
- [The Three Canonical Forms on $\mathbb{C}^2$](the-three-canonical-forms-on-the-complex-two-space.html), below in this category, for the Gram matrices, the isotropy and the relations among $H$, $B$ and $\omega$.
- [The Subspaces of $\mathbb{C}^2$](the-subspaces-of-the-complex-two-space.html), below in this category, for the lines, the hyperplanes, the isotropic lines and the Lagrangian planes.
- [The Endomorphisms of $\mathbb{C}^2$](the-endomorphisms-of-the-complex-two-space.html), below in this category, for the matrix algebra $M_2(\mathbb{C})$ and the conjugate-linear maps.
- [The Topology of $\mathbb{C}^2$](the-topology-of-the-complex-two-space.html), below in this category, for the topology of the space, the sphere $S^3$ and the group $\mathrm{GL}_2(\mathbb{C})$.
- [The Compactifications of $\mathbb{C}^2$](the-compactifications-of-the-complex-two-space.html), below in this category, for the one-point compactification $S^4$ and the projective compactification $\mathbb{CP}^2$.
- [The Unit Sphere and the Hopf Fibration](the-unit-sphere-and-the-hopf-fibration.html), below in this category, for the Hopf bundle $S^1\to S^3\to S^2$.
- [Several Complex Variables](several-complex-variables.html), for the general theory of holomorphic functions of several variables, of which this category treats the case of two variables.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra $\mathbb{B}\cong M_2(\mathbb{C})$ whose simple module is this space.
- [Conway, *Functions of One Complex Variable*](https://link.springer.com/book/10.1007/978-1-4612-6313-5), for the one-variable facts that the two-variable theory inherits and those it does not.
