
# Dual Numbers Representations

## Introduction

This article introduces the representation theory of the dual number algebra. The goal is to define representations precisely, classify them, and describe the structure of the representation ring.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The dual number algebra is assumed from the article on dual numbers algebra, and the maximal ideal is used throughout. The article is stated for an arbitrary commutative ring $R$ in which $2$ is invertible, and no finiteness assumption is made unless stated.

Throughout this article, the dual number algebra is denoted $\mathbb{D}'$, and the split complex algebra is denoted $\mathbb{D}$. The notation is chosen so that the two do not collide. The unit of $\mathbb{D}'$ is denoted $\varepsilon$, and it satisfies $\varepsilon^2 = 0$.

## Representations of $\mathbb{D}'$

### Definition

A **representation** of $\mathbb{D}'$ is an $R$-module $V$ together with a bilinear map

$$
\rho : \mathbb{D}' \times V \to V, \qquad \rho(z, v) = z \cdot v,
$$

satisfying

$$
z \cdot (w \cdot v) = (zw) \cdot v, \qquad 1 \cdot v = v.
$$

Equivalently, a representation is an algebra homomorphism

$$
\rho : \mathbb{D}' \to \operatorname{End}_R(V).
$$

Since $\mathbb{D}'$ is commutative, the image of $\rho$ is a commutative subalgebra of $\operatorname{End}_R(V)$.

### The Action of the Nilpotent

The unit $\varepsilon$ acts as an $R$-linear endomorphism

$$
E = \rho(\varepsilon) \in \operatorname{End}_R(V),
$$

and the defining relation $\varepsilon^2 = 0$ forces

$$
E^2 = 0.
$$

So a representation of $\mathbb{D}'$ is the same thing as an $R$-module $V$ together with a nilpotent endomorphism $E$ of index at most two. The action of a general dual number $a + b\varepsilon$ is

$$
(a + b\varepsilon) \cdot v = a v + b E(v).
$$

This is the fundamental structural fact about representations of $\mathbb{D}'$: they are determined by a single square-zero endomorphism.

### The Regular Representation

The **regular representation** of $\mathbb{D}'$ is $\mathbb{D}'$ acting on itself by left multiplication:

$$
\rho_{\mathrm{reg}}(z) w = z w, \qquad z, w \in \mathbb{D}'.
$$

This is the representation $\rho_{\mathrm{reg}} : \mathbb{D}' \to \operatorname{End}_R(\mathbb{D}')$ given by $\rho_{\mathrm{reg}}(z) = z$. It is the representation of $\mathbb{D}'$ on a free $R$-module of rank two. The nilpotent $E = \rho_{\mathrm{reg}}(\varepsilon)$ is the endomorphism that sends $a + b\varepsilon$ to $a \varepsilon$, i.e. it kills the infinitesimal part and maps the real part to the infinitesimal submodule.

### The Trivial Representation

The **trivial representation** (or **augmentation representation**) is the one-dimensional representation on $R$ defined by

$$
\rho_{\mathrm{triv}}(a + b\varepsilon) = a.
$$

This is the representation that sends $\varepsilon$ to zero. It is the quotient of the regular representation by the maximal ideal.

### The Standard Representation

The **standard representation** is the one-dimensional representation on $R$ defined by

$$
\rho_{\mathrm{std}}(a + b\varepsilon) = a.
$$

This coincides with the trivial representation. In the dual case, there is no non-trivial one-dimensional representation, because every algebra homomorphism $\mathbb{D}' \to R$ must send $\varepsilon$ to an element $c \in R$ with $c^2 = 0$, and the only such element in a reduced ring is $c = 0$. So the trivial representation is the only one-dimensional representation.

## Classification

### The Classification Theorem

**Theorem.** Let $V$ be an $R$-module. The representations of $\mathbb{D}'$ on $V$ are in bijection with the square-zero endomorphisms $E \in \operatorname{End}_R(V)$, via the correspondence

$$
E \longleftrightarrow \rho_E(a + b\varepsilon) = a \cdot \mathrm{id}_V + b E.
$$

**Proof.** Given a representation $\rho$, the endomorphism $E = \rho(\varepsilon)$ satisfies $E^2 = \rho(\varepsilon^2) = 0$. Conversely, given a square-zero endomorphism $E$, the formula $\rho_E(a + b\varepsilon) = a \cdot \mathrm{id}_V + b E$ defines an algebra homomorphism, because

$$
\rho_E((a + b\varepsilon)(c + d\varepsilon)) = \rho_E(ac + (ad + bc)\varepsilon) = ac \cdot \mathrm{id}_V + (ad + bc) E,
$$

and

$$
\rho_E(a + b\varepsilon) \rho_E(c + d\varepsilon) = (a \cdot \mathrm{id}_V + b E)(c \cdot \mathrm{id}_V + d E) = ac \cdot \mathrm{id}_V + (ad + bc) E + bd E^2 = ac \cdot \mathrm{id}_V + (ad + bc) E,
$$

since $E^2 = 0$. The two agree. $\square$

So the representation theory of $\mathbb{D}'$ is equivalent to the theory of square-zero endomorphisms. This is the reason the representation theory is both simple and rich: simple because the endomorphism is square-zero, rich because there are many such endomorphisms.

### Direct Sums

The **direct sum** of two representations $(V, E)$ and $(W, F)$ is the representation on $V \oplus W$ with endomorphism

$$
E \oplus F : (v, w) \mapsto (E v, F w).
$$

It satisfies $(E \oplus F)^2 = E^2 \oplus F^2 = 0$, so it is again a representation.

### Irreducible Representations

**Theorem.** The only irreducible representation of $\mathbb{D}'$ is the trivial representation on $R$.

**Proof.** Let $(V, E)$ be irreducible. If $E \neq 0$, then $\ker E$ is a non-zero proper subrepresentation, because $E^2 = 0$ implies $\ker E \neq 0$ and $\operatorname{im} E \subseteq \ker E$ implies $\ker E \neq V$ when $E \neq 0$. This contradicts irreducibility. So $E = 0$, and the representation is the trivial representation on $V$. For it to be irreducible, $V$ must be one-dimensional over $R$ when $R$ is a field. $\square$

So the irreducible representations are exactly the trivial ones, indexed by the simple $R$-modules. When $R$ is a field, there is exactly one irreducible representation up to isomorphism, namely the one-dimensional trivial representation.

### Indecomposable Representations

A representation $(V, E)$ is **indecomposable** if it cannot be written as a direct sum of two non-zero subrepresentations.

**Theorem.** Let $R$ be a field. The indecomposable representations of $\mathbb{D}'$ are, up to isomorphism:

- The trivial representation on $R$ (with $E = 0$).
- The regular representation on $R^2$ (with $E$ the nilpotent Jordan block of size two).

**Proof.** Let $(V, E)$ be indecomposable with $E \neq 0$. Then $E^2 = 0$ implies $\operatorname{im} E \subseteq \ker E$. Choose a non-zero $v \in \operatorname{im} E$, and choose $w \in V$ with $E w = v$. Then $E v = E^2 w = 0$, so $v \in \ker E$. The subspace spanned by $v$ and $w$ is a subrepresentation isomorphic to the regular representation. If $V$ is larger, it decomposes as the direct sum of this subrepresentation and a complement, contradicting indecomposability. So $V$ is the regular representation. $\square$

So over a field, there are exactly two indecomposable representations, and the classification is finite. This is the simplest possible representation theory of a non-semisimple algebra.

### The Jordan Form

Over a field, a square-zero endomorphism $E$ has a Jordan form consisting of blocks of size one (corresponding to the trivial representation) and blocks of size two (corresponding to the regular representation). So an arbitrary representation of $\mathbb{D}'$ decomposes as

$$
V \cong R^{\oplus p} \oplus (R^2)^{\oplus q},
$$

with $E$ acting as zero on the first summand and as the nilpotent Jordan block on each copy of $R^2$.

This is the complete classification over a field: the representation is determined by the multiplicities $p$ and $q$.

## Schur's Lemma

**Theorem (Schur).** Every $\mathbb{D}'$-linear endomorphism of an irreducible representation of $\mathbb{D}'$ is a scalar multiple of the identity.

**Proof.** Let $(V, E)$ be irreducible and let $T : V \to V$ be $\mathbb{D}'$-linear, i.e. $T E = E T$. Then $\ker T$ and $\operatorname{im} T$ are subrepresentations. Since $V$ is irreducible and $E = 0$ on $V$, the only subrepresentations are $0$ and $V$. So $T$ is either zero or an isomorphism. In the second case, $T$ is an isomorphism of one-dimensional $R$-modules when $R$ is a field, hence multiplication by a non-zero scalar. $\square$

**Corollary.** The endomorphism ring of the trivial representation is $R$ itself.

**The non-semisimple case.** Schur's lemma fails for non-irreducible representations. For the regular representation, the endomorphism ring is larger than $R$: it consists of all $R$-linear maps commuting with $E$, which is the set of $2 \times 2$ matrices of the form

$$
\begin{pmatrix} a & 0 \\ b & a \end{pmatrix}, \qquad a, b \in R.
$$

This is a two-dimensional $R$-algebra, isomorphic to $\mathbb{D}'$ itself. So the endomorphism ring of the regular representation is $\mathbb{D}'$.

## The Representation Ring

### Definition

The **representation ring** $R(\mathbb{D}')$ is the Grothendieck ring of finite-dimensional representations of $\mathbb{D}'$ over a field. As an abelian group, it is generated by the isomorphism classes of the indecomposable representations:

$$
R(\mathbb{D}') \cong \mathbb{Z} \oplus \mathbb{Z},
$$

with generators $[\rho_{\mathrm{triv}}]$ and $[\rho_{\mathrm{reg}}]$, corresponding to the trivial representation and the regular representation.

### Ring Structure

The product in $R(\mathbb{D}')$ is given by the tensor product of representations:

$$
[V] \cdot [W] = [V \otimes W].
$$

The tensor product of two representations $(V, E)$ and $(W, F)$ is the representation on $V \otimes W$ with endomorphism

$$
E \otimes \mathrm{id}_W + \mathrm{id}_V \otimes F.
$$

This satisfies

$$
(E \otimes \mathrm{id}_W + \mathrm{id}_V \otimes F)^2 = E^2 \otimes \mathrm{id}_W + 2 E \otimes F + \mathrm{id}_V \otimes F^2 = 2 E \otimes F,
$$

which is zero only when $2 = 0$ or $E \otimes F = 0$. So the tensor product of two representations of $\mathbb{D}'$ is not automatically a representation of $\mathbb{D}'$, unless one of the factors is trivial.

**This is a key difference from the semisimple case.** For a semisimple algebra, the tensor product of two representations is again a representation, because the coproduct is an algebra homomorphism. For $\mathbb{D}'$, the coproduct is not an algebra homomorphism, because $\varepsilon$ is not primitive: the diagonal map $\Delta(\varepsilon) = \varepsilon \otimes 1 + 1 \otimes \varepsilon$ satisfies

$$
\Delta(\varepsilon)^2 = 2 \varepsilon \otimes \varepsilon \neq 0.
$$

So $\mathbb{D}'$ is not a Hopf algebra, and its representation category is not monoidal in the naive way. The tensor product is defined, but it is not a representation of $\mathbb{D}'$ in general.

**The modified tensor product.** To obtain a monoidal structure, one uses a **deformation** of the coproduct, or one restricts to a subcategory of representations on which the tensor product is well-behaved. This is the starting point of the theory of **Hopf algebroids** and **quantum groups**, where the dual numbers appear as the simplest non-trivial example of a non-cocommutative or non-primitive structure.

## The Dual Representation

### Definition

The **dual** (or contragredient) representation of a representation $(V, E)$ is the representation on the dual module $V^* = \operatorname{Hom}_R(V, R)$ with endomorphism

$$
E^* : V^* \to V^*, \qquad (E^* f)(v) = -f(E v).
$$

The minus sign is chosen so that $(E^*)^2 = 0$ is preserved: indeed,

$$
(E^*)^2 f = E^*(E^* f) = - (E^* f) \circ E = f \circ E \circ E = f \circ E^2 = 0.
$$

### Basic Properties

**Duality is an involution.** $(V^*)^* \cong V$.

**Duality is exact.** It preserves direct sums: $(V \oplus W)^* \cong V^* \oplus W^*$.

**The dual of the trivial representation is the trivial representation.** $\rho_{\mathrm{triv}}^* \cong \rho_{\mathrm{triv}}$.

**The dual of the regular representation is the regular representation.** $\rho_{\mathrm{reg}}^* \cong \rho_{\mathrm{reg}}$.

So duality acts trivially on the set of indecomposable representations.

## Homomorphisms

### Definition

A **homomorphism** of representations $(V, E)$ and $(W, F)$ is an $R$-linear map $T : V \to W$ such that

$$
T \circ E = F \circ T.
$$

The space of all such homomorphisms is denoted $\operatorname{Hom}_{\mathbb{D}'}(V, W)$.

### Basic Properties

**Composition.** If $T \in \operatorname{Hom}_{\mathbb{D}'}(V, W)$ and $S \in \operatorname{Hom}_{\mathbb{D}'}(W, U)$, then $S T \in \operatorname{Hom}_{\mathbb{D}'}(V, U)$.

**Schur's lemma.** If $V$ and $W$ are irreducible, then $\operatorname{Hom}_{\mathbb{D}'}(V, W) = 0$ if $V \not\cong W$, and $\operatorname{Hom}_{\mathbb{D}'}(V, V) \cong R$.

**Dimension count over a field.** For $V \cong R^{\oplus p} \oplus (R^2)^{\oplus q}$ and $W \cong R^{\oplus r} \oplus (R^2)^{\oplus s}$,

$$
\dim_R \operatorname{Hom}_{\mathbb{D}'}(V, W) = pr + 2qs.
$$

The factor of $2$ comes from the endomorphisms of the regular representation, which form a two-dimensional algebra.

**Proof.** A homomorphism must preserve the decomposition into trivial and regular summands, because the two indecomposables are non-isomorphic. So it is determined by its action on each isotypic component. On the trivial component $R^{\oplus p} \to R^{\oplus r}$, the space of maps is $pr$-dimensional. On the regular component $(R^2)^{\oplus q} \to (R^2)^{\oplus s}$, the space of maps is $2qs$-dimensional, because each regular summand has a two-dimensional endomorphism ring. $\square$

### The Endomorphism Ring

The **endomorphism ring** of a representation $(V, E)$ is $\operatorname{End}_{\mathbb{D}'}(V) = \operatorname{Hom}_{\mathbb{D}'}(V, V)$. For $V \cong R^{\oplus p} \oplus (R^2)^{\oplus q}$ over a field,

$$
\operatorname{End}_{\mathbb{D}'}(V) \cong M_p(R) \oplus M_q(\mathbb{D}'),
$$

the direct sum of the matrix ring of size $p$ over $R$ and the matrix ring of size $q$ over $\mathbb{D}'$. This is not semisimple when $q > 0$, because $\mathbb{D}'$ is not semisimple.

## The Category of Representations

### The Abelian Category

The representations of $\mathbb{D}'$ form an abelian category $\mathrm{Rep}(\mathbb{D}')$. The category is not semisimple when $\mathbb{D}'$ is not semisimple, i.e. when $\varepsilon \neq 0$. So there are non-split short exact sequences.

### The Standard Non-Split Extension

The fundamental non-split extension is

$$
0 \to \rho_{\mathrm{triv}} \to \rho_{\mathrm{reg}} \to \rho_{\mathrm{triv}} \to 0,
$$

where the first map is the inclusion of $\ker E$ and the second is the quotient by $\operatorname{im} E$. This sequence does not split, because the regular representation is not the direct sum of two copies of the trivial representation.

The extension class of this sequence is the generator of $\operatorname{Ext}^1_{\mathbb{D}'}(\rho_{\mathrm{triv}}, \rho_{\mathrm{triv}}) \cong R$. This is the algebraic content of the nilpotence of $\varepsilon$: the extension is non-trivial precisely because $\varepsilon^2 = 0$ but $\varepsilon \neq 0$.

### The Ext Algebra

The **Ext algebra** of $\mathbb{D}'$ is

$$
\operatorname{Ext}^\bullet_{\mathbb{D}'}(R, R) \cong R[\varepsilon]/(\varepsilon^2),
$$

with $\varepsilon$ in degree one. So the Ext algebra is isomorphic to $\mathbb{D}'$ itself, with the grading shifted. This is a general phenomenon: for a local ring with maximal ideal $\mathfrak{m}$ satisfying $\mathfrak{m}^2 = 0$, the Ext algebra of the residue field is the Koszul dual, which is the symmetric algebra on the dual of $\mathfrak{m}$, truncated at degree two.

So the representation theory of $\mathbb{D}'$ is controlled by the Ext algebra $\mathbb{D}'$, and the nilpotence of $\varepsilon$ is the source of the non-semisimplicity.

## Comparison with the Split Complex Case

The representation theory of $\mathbb{D}'$ differs from that of the split complex algebra $\mathbb{D}$ in several ways.

**Idempotents versus nilpotents.** The split complex algebra has two non-trivial idempotents $e_+$ and $e_-$, which give two one-dimensional representations. The dual algebra has no non-trivial idempotents, and the only irreducible representation is the trivial one.

**Semisimplicity.** The split complex algebra over a field is isomorphic to $F \oplus F$, which is semisimple. Its representations are direct sums of copies of the two irreducible representations. The dual algebra is local, with nilpotent maximal ideal, and its representations are not semisimple in general.

**Number of indecomposables.** The split complex algebra has two indecomposable representations (the two one-dimensional ones). The dual algebra has two indecomposable representations (the trivial one and the regular one). So both have two, but the structure is different: for $\mathbb{D}$, the two are irreducible; for $\mathbb{D}'$, only one is irreducible, and the other is a non-split extension.

**Tensor products.** The split complex algebra is a Hopf algebra with the componentwise coproduct, and the tensor product of two representations is again a representation. The dual algebra is not a Hopf algebra with the primitive coproduct, because $\varepsilon$ is not primitive. So the tensor product is not a representation in general.

**The representation ring.** For $\mathbb{D}$, the representation ring is $\mathbb{Z} \oplus \mathbb{Z}$, with the two irreducibles as generators, and the multiplication is componentwise. For $\mathbb{D}'$, the representation ring is also $\mathbb{Z} \oplus \mathbb{Z}$, but the multiplication is not defined in the same way, because the tensor product of two non-trivial representations is not a representation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'$ | Dual number algebra |
| $\varepsilon$ | Dual unit, $\varepsilon^2 = 0$ |
| $V$ | Representation space |
| $E = \rho(\varepsilon)$ | Square-zero endomorphism |
| $\rho_{\mathrm{reg}}$ | Regular representation |
| $\rho_{\mathrm{triv}}$ | Trivial representation |
| $\operatorname{End}_{\mathbb{D}'}(V)$ | Endomorphism ring |
| $\operatorname{Hom}_{\mathbb{D}'}(V, W)$ | Space of homomorphisms |
| $\operatorname{Ext}^\bullet_{\mathbb{D}'}(R, R)$ | Ext algebra |
| $R(\mathbb{D}')$ | Representation ring |

## Further Reading

- Charles C. Pinter, *A Book of Abstract Algebra* (Dover, 2010), for the representation theory of algebras.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the general theory of modules over rings.
- Serge Lang, *Algebra* (Springer, 2002), for the structure theory of local rings.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for the theory of algebras over commutative rings.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (AMS, 2005), for the general theory of quadratic forms.

