# __The Complex Numbers as a Vector Space over $\mathbb{R}$__

## Introduction

The complex algebra is one additive group carrying two scalar readings. Read over $\mathbb{R}$ it is the real plane with basis $1, i$, of real dimension two; read over itself it is a complex line, of complex dimension one. This article fixes the two readings, the operator $J$ that is multiplication by $i$, the classification of the real-linear maps of the plane into the complex-linear and the conjugate-linear ones, the real forms, and the self-duality that the one-dimensional complex reading enjoys.

The article is purely linear. No form, no norm and no topology appear in it; the reading of the complex numbers as the realification of a form, with its signatures and its count of operations, is *The Realification and the Effect of the Change of Scalars*, below this article in this category. The multiplication itself is owned by *Complex Algebra* and the two distinguished subspaces by *Complex Subspaces*, both below this article in this category; both are cited here and neither is restated.

The reading of the marks is the corpus convention, stated once because the older complex articles use the words differently. The **bar** is complex conjugation, the one nontrivial involution of the algebra, and the **Hermitian star** coincides with the bar. The articles *Complex Algebra* and *Complex Subspaces*, below this article in this category, call these the "two conjugations" and the "two involutions" of the algebra, the identity and complex conjugation; those are the identity and the bar in the present vocabulary, and the two are the same two maps.

## The Two Interpretations of the One Space

**Definition.** The **complex space over $\mathbb{R}$** is the additive group of $\mathbb{C}$ with scalars restricted to $\mathbb{R}$. The **complex space over $\mathbb{C}$** is the same additive group with its full scalar action. The two are written $\mathbb{C}_{\mathbb{R}}$ and $\mathbb{C}_{\mathbb{C}}$ when the scalar domain has to be named.

In the real reading the basis is $1, i$,

$$
A = a\,1 + a'\,i, \qquad a, a' \in \mathbb{R},
$$

so $\dim_{\mathbb{R}} \mathbb{C}_{\mathbb{R}} = 2$. In the complex reading the basis is $1$ alone,

$$
A = A\,1, \qquad A \in \mathbb{C},
$$

so $\dim_{\mathbb{C}} \mathbb{C}_{\mathbb{C}} = 1$. The two readings have the same elements and the same addition; only the scalars differ, and the scalar domain has been cut from $\mathbb{C}$ to $\mathbb{R}$. This is the operation called restriction of scalars.

$$
\dim_{\mathbb{R}} \mathbb{C}_{\mathbb{R}} = 2 = 2 \dim_{\mathbb{C}} \mathbb{C}_{\mathbb{C}} .
$$

The complex reading is not the real reading with more scalars in another sense: the real reading is over the subfield $\mathbb{R}_{\mathbb{C}}$ of the fixed points of the bar, and the complex reading is over the whole field, so the same set is a two-dimensional space over a subfield and a one-dimensional space over the field that contains it.

## The Complex Structure

**Definition.** The **complex structure** of the plane is the real-linear map

$$
J : \mathbb{C} \to \mathbb{C}, \qquad J(A) = iA .
$$

**Proposition.** $J$ is real-linear, and $J^2 = -\operatorname{id}$.

**Proof.** Multiplication by $i$ is additive and commutes with real scalars, since the multiplication of $\mathbb{C}$ is bilinear and $\mathbb{R}$ lies in the centre; hence $J$ is real-linear. And $J(J(A)) = i(iA) = i^2 A = -A$, so $J^2 = -\operatorname{id}$.

The complex scalar action is the real action together with $J$: for $\lambda = a + ib$,

$$
\lambda A = aA + b\,J(A) .
$$

So the passage from the real reading to the complex one is the adjunction of the single operator $J$, and nothing else. In the basis $1, i$ the operator has the matrix

$$
J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix},
$$

which has no real eigenvector, since $J^2 = -\operatorname{id}$ has no real solution. There is therefore no real scalar $\mu$ with $J = \mu\operatorname{id}$, and the real reading does not by itself single out the element $i$: the complex structure is an extra operator, not a scalar of the real reading.

## Complexification and the Two Real Spaces

The **complexification** of the real reading is the tensor product $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C}$, taken over $\mathbb{R}$.

**Proposition.** $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{C} \times \mathbb{C}$ as $\mathbb{C}$-algebras, the isomorphism being $z \otimes w \mapsto (zw, z\bar w)$.

**Proof.** The map is $\mathbb{R}$-bilinear, so it factors through the tensor product; it is multiplicative, $(z_1 \otimes w_1)(z_2 \otimes w_2) \mapsto (z_1 z_2 w_1 w_2, z_1 z_2 \bar w_1 \bar w_2)$, which is the product of the images; it is $\mathbb{C}$-linear, $(\lambda z)\otimes w \mapsto \lambda(z w, z\bar w)$; and it carries the real basis $1\otimes1, i\otimes1, 1\otimes i, i\otimes i$ to $(1,1), (i,i), (i,-i), (-1,1)$, four real-independent vectors, so it is an isomorphism of real vector spaces, of complex dimension two on each side.

The complexification is therefore not the complex reading. It is the sum of the space and its conjugate, $\mathbb{C} \oplus \bar{\mathbb{C}}$, of complex dimension two, while the complex reading $\mathbb{C}_{\mathbb{C}}$ has complex dimension one. The two spaces that a reader may confuse are these:

| space | scalar field | dimension |
|---|---|---|
| the complex reading $\mathbb{C}_{\mathbb{C}}$ | $\mathbb{C}$ | $1$ over $\mathbb{C}$ |
| the complexification $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C}$ | $\mathbb{C}$ | $2$ over $\mathbb{C}$ |

What returns the complex reading from the real one is the operator $J$, not a scalar extension. The extension of scalars produces the two-dimensional space $\mathbb{C} \oplus \bar{\mathbb{C}}$, in which the original space and its conjugate sit as the two factors, and it is the doubling of the complex dimension that the extension adds.

## Linear and Conjugate-Linear Maps

Let $T : \mathbb{C} \to \mathbb{C}$ be real-linear. It is **complex-linear** when $T(\lambda A) = \lambda T(A)$ for every $\lambda \in \mathbb{C}$, and **conjugate-linear** when $T(\lambda A) = \bar\lambda T(A)$ for every $\lambda$.

**Proposition.** A real-linear $T$ is complex-linear if and only if $TJ = JT$, and conjugate-linear if and only if $TJ = -JT$.

**Proof.** Since $\mathbb{C}$ is generated over $\mathbb{R}$ by $1$ and $i$, the identity $T(\lambda A) = \lambda T(A)$ for all $\lambda$ is equivalent to its two instances $\lambda = 1$ and $\lambda = i$; the first is automatic and the second is $T(iA) = iT(A)$, that is $TJ = JT$. The conjugate-linear case is the same with $\lambda = i$ giving $T(iA) = -iT(A)$, that is $TJ = -JT$.

The two classes are read on the matrix in the basis $1, i$:

| kind of real-linear map | condition | matrix shape |
|---|---|---|
| complex-linear | $TJ = JT$ | $\begin{pmatrix} p & -q \\ q & p \end{pmatrix} = pI + qJ$ |
| conjugate-linear | $TJ = -JT$ | $\begin{pmatrix} p & q \\ q & -p \end{pmatrix}$ |

**Proposition.** A complex-linear map is multiplication by a complex number, and a conjugate-linear map is the bar followed by a multiplication. In the shapes above,

$$
T(A) = (p + iq)A \quad \text{(complex-linear)}, \qquad S(A) = \bar A\,(p+iq) \quad \text{(conjugate-linear)} .
$$

**Proof.** A map commuting with $J$ is $\mathbb{C}$-linear, so it is determined by $T(1) = p + iq$ and is $A \mapsto (p+iq)A$. A map anticommuting with $J$ is written $S = T \circ \bar{\cdot}$ with $T$ complex-linear, and $\bar\cdot$ is the bar; then $S(1) = p+iq = w$ and $S(A) = \bar A w$.

So the complex-linear maps are the two-real-dimensional space $\operatorname{End}_{\mathbb{C}}(\mathbb{C}) \cong \mathbb{C}$, the conformal shape in the matrix algebra, and the conjugate-linear maps form the complementary two-real-dimensional space, on which $1$ is sent to the arbitrary complex number $w$. The two together fill the whole of $\operatorname{End}_{\mathbb{R}}(\mathbb{C}) \cong M_2(\mathbb{R})$, of real dimension four:

$$
\operatorname{End}_{\mathbb{R}}(\mathbb{C}) = \operatorname{End}_{\mathbb{C}}(\mathbb{C}) \oplus \{\text{conjugate-linear maps}\}, \qquad 4 = 2 + 2 .
$$

The splitting is the $\pm 1$ eigenspace decomposition of the involution $T \mapsto JTJ^{-1}$ of the endomorphism algebra, the operator $T \mapsto JTJ^{-1}$ being the conjugation by $J$.

## The Real Forms

**Definition.** A **real form** of the complex space is a real subspace $V$ such that $\mathbb{C} = V \oplus JV$; equivalently, $V \cap JV = 0$ and the two together span.

The name is the algebra sense — a real subspace complementing its own image under the complex structure — and it is not a bilinear or Hermitian form.

**Proposition.** Every real line of $\mathbb{C}$ is a real form.

**Proof.** Let $V = \mathbb{R}v$ with $v \neq 0$. If $V \cap JV$ were nonzero then $Jv = \mu v$ for some real $\mu$, and $J^2v = \mu^2 v$ against $J^2v = -v$, so $\mu^2 = -1$, which has no real solution; hence $V \cap JV = 0$. Both are one-dimensional, so $V + JV$ has dimension two and is $\mathbb{C}$.

The two distinguished lines are the real subspace $\mathbb{R}_{\mathbb{C}}$ and the imaginary subspace $i\mathbb{R}_{\mathbb{C}}$, of real dimension one each; they are exchanged by $J$, and they are the fixed and the anti-fixed subspaces of the bar.

Every real form $V$ gives an isomorphism $\mathbb{C} \otimes_{\mathbb{R}} V \cong \mathbb{C}$, obtained by sending $\lambda \otimes v$ to $\lambda v$; on a line $V = \mathbb{R}v$ the map sends $\lambda \otimes v$ to $\lambda v$ and its inverse sends $w$ to $w/v \otimes v$, so the construction names the form $V$ and describes the space as built from it. For the two distinguished lines the isomorphisms read $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{R}_{\mathbb{C}} \cong \mathbb{C}$ and $\mathbb{C} \otimes_{\mathbb{R}} i\mathbb{R}_{\mathbb{C}} \cong \mathbb{C}$, the second sending $\lambda \otimes ia'$ to $i\lambda a'$.

## Self-Duality and the Absence of a Proper Complex Subspace

Read over itself, the space is one-dimensional, and a one-dimensional space over a field has only the two subspaces $\{0\}$ and the whole space: the only $\mathbb{C}$-subspaces of $\mathbb{C}_{\mathbb{C}}$ are the zero subspace and the space itself, because a $\mathbb{C}$-subspace is an ideal of the field $\mathbb{C}$.

**Proposition.** The dual of the complex reading is the complex reading, $\operatorname{Hom}_{\mathbb{C}}(\mathbb{C}, \mathbb{C}) \cong \mathbb{C}$, canonically, and the space is self-dual.

**Proof.** A $\mathbb{C}$-linear map $\mathbb{C} \to \mathbb{C}$ is determined by its value at $1$, so $\operatorname{Hom}_{\mathbb{C}}(\mathbb{C}, \mathbb{C}) \cong \mathbb{C}$ by evaluation at $1$, and the identification is natural because $1$ is the only basis vector.

The real reading retains the two real lines $\mathbb{R}_{\mathbb{C}}$ and $i\mathbb{R}_{\mathbb{C}}$, of real dimension one each. Neither is a complex subspace: each is closed under real scalars but not under multiplication by $i$, which exchanges the two. Against those two real subspaces, the complex reading has no proper nonzero subspace at all; the two real lines are the structure of the underlying real space, and the complex reading forgets them.

The complex space is its own **centre**, the subspace of the elements commuting with every element, of real dimension two; the identification is

$$
a + ia' \longmapsto a\,e_0 + a'\,(ie_0) .
$$

On it the two products $AC$ and $A\bar C$ act; the product theory is the subject of *The Two Products of the Complex Space*, below this article in this category.

## Summary

The complex algebra is one additive group read over two scalar fields. Over $\mathbb{R}$ it is the plane $\mathbb{C}_{\mathbb{R}}$ with basis $1, i$, of real dimension two, and over itself it is the line $\mathbb{C}_{\mathbb{C}}$ with basis $1$, of complex dimension one; the dimension doubles on restriction of scalars. The passage from the real reading to the complex one is the adjunction of the real-linear complex structure $J(A) = iA$, which satisfies $J^2 = -\operatorname{id}$ and has no real eigenvector, so the real reading does not single out $i$.

A real-linear map of the plane is complex-linear exactly when it commutes with $J$ and conjugate-linear exactly when it anticommutes, and the two classes have the matrix shapes $pI + qJ$ and its antisymmetric companion. The complex-linear maps are multiplication by a complex number and form $\operatorname{End}_{\mathbb{C}}(\mathbb{C}) \cong \mathbb{C}$; the conjugate-linear maps form the complementary plane, and the two fill $\operatorname{End}_{\mathbb{R}}(\mathbb{C}) \cong M_2(\mathbb{R})$ in the $\pm 1$ eigenspace splitting of conjugation by $J$.

The complexification $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{C} \times \mathbb{C}$ is the sum of the space and its conjugate and is not the complex reading; the two complex-dimension-two and complex-dimension-one spaces must be told apart, and what returns the complex reading is $J$, not a scalar extension. Every real line is a real form, $V \cap JV = 0$ and $\mathbb{C} = V \oplus JV$, the two distinguished lines being $\mathbb{R}_{\mathbb{C}}$ and $i\mathbb{R}_{\mathbb{C}}$. Read over itself the space is self-dual and has no proper nonzero subspace, and it is its own centre, on which the two products $AC$ and $A\bar C$ act.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}_{\mathbb{R}}$ | $\mathbb{C}$ read as a real vector space, basis $1, i$, dimension $2$ over $\mathbb{R}$ |
| $\mathbb{C}_{\mathbb{C}}$ | $\mathbb{C}$ read as a complex vector space, basis $1$, dimension $1$ over $\mathbb{C}$ |
| $A = a + ia'$ | a complex number, with $a, a' \in \mathbb{R}$ |
| $J(A) = iA$ | the complex structure, real-linear, $J^2 = -\operatorname{id}$ |
| $\lambda A = aA + bJ(A)$ | the complex action read on the real reading, $\lambda = a + ib$ |
| $TJ = JT$ | complex-linearity of a real-linear $T$ |
| $TJ = -JT$ | conjugate-linearity of a real-linear $S$ |
| $V$ with $\mathbb{C} = V \oplus JV$ | a real form |
| $\mathbb{R}_{\mathbb{C}}, i\mathbb{R}_{\mathbb{C}}$ | the distinguished real and imaginary lines |
| $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{C} \times \mathbb{C}$ | the complexification, the sum of the space and its conjugate |

## Further Reading

- Serge Lang, *Algebra*, 3rd edition (Springer, 2002), for restriction and extension of scalars, tensor products of fields, and the classification of linear maps commuting with a complex structure.
- Nathan Jacobson, *Lectures in Abstract Algebra*, Volume II (Van Nostrand, 1953), for the real vector space underlying a field extension and its linear endomorphisms.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the complex structure of a two-dimensional real algebra and its higher-dimensional analogues.
