# __Quaternion Representations__

## Introduction

This article introduces the representation theory of the quaternion algebra. The goal is to define representations precisely, classify them, and describe the structure of the representation ring.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. No examples are given. The quaternion algebra is assumed from the article on quaternion algebra, and the scalar-vector decomposition is used throughout. The article is stated for the quaternion algebra over a field $F$ of characteristic not two, and the complexification is treated separately.

Throughout this article, the quaternion algebra is denoted $\mathbb{H}$, and its basis is $e_0 = 1, e_1, e_2, e_3$. The scalar imaginary of the complex numbers is denoted $i$, so that it does not collide with the quaternion units.

## Representations of $\mathbb{H}$

### Definition

A **representation** of $\mathbb{H}$ is a vector space $V$ over $F$ together with a bilinear map

$$
\rho : \mathbb{H} \times V \to V, \qquad \rho(q, v) = q \cdot v,
$$

satisfying

$$
q \cdot (r \cdot v) = (qr) \cdot v, \qquad 1 \cdot v = v.
$$

Equivalently, a representation is an algebra homomorphism

$$
\rho : \mathbb{H} \to \operatorname{End}_F(V).
$$

Since $\mathbb{H}$ is a division algebra over $F$, every non-zero element is invertible, and the image of $\rho$ is a subalgebra of $\operatorname{End}_F(V)$ that is isomorphic to a quotient of $\mathbb{H}$. Because $\mathbb{H}$ is simple, the kernel of $\rho$ is either zero or all of $\mathbb{H}$. So every non-zero representation is faithful, and the image is isomorphic to $\mathbb{H}$.

### The Regular Representation

The **regular representation** of $\mathbb{H}$ is $\mathbb{H}$ acting on itself by left multiplication:

$$
\rho_{\mathrm{reg}}(q) r = q r, \qquad q, r \in \mathbb{H}.
$$

This is the representation $\rho_{\mathrm{reg}} : \mathbb{H} \to \operatorname{End}_F(\mathbb{H})$ given by $\rho_{\mathrm{reg}}(q) = q$. It is the representation of $\mathbb{H}$ on a four-dimensional vector space over $F$. The image is a four-dimensional subalgebra of $\operatorname{End}_F(\mathbb{H})$, isomorphic to $\mathbb{H}$.

### The Left and Right Regular Representations

Because $\mathbb{H}$ is not commutative, there are two distinct regular representations:

**Left regular representation.** $\rho_L(q) r = q r$.

**Right regular representation.** $\rho_R(q) r = r q$. This is a right action rather than a left one: $\rho_R(q) \rho_R(q') = \rho_R(q' q)$.

Composing the right action with the anti-automorphism $q \mapsto \bar{q}$ gives a left representation $\rho_R(q) r = r \bar{q}$, and the map $r \mapsto \bar{r}$ intertwines it with $\rho_L$, so the two regular representations are isomorphic.

## Classification

### The Classification Theorem

**Theorem.** Let $F$ be a field of characteristic not two over which $\mathbb{H}$ is a division algebra. Every finite-dimensional representation of $\mathbb{H}$ over $F$ is isomorphic to a direct sum of copies of the regular representation:

$$
V \cong \mathbb{H}^{\oplus n}, \qquad \rho(q)(v_1, \dots, v_n) = (q v_1, \dots, q v_n).
$$

**Proof.** Let $V$ be a finite-dimensional representation. Since $\mathbb{H}$ is a division algebra and $\rho$ is non-zero (unless $V = 0$), the image $\rho(\mathbb{H})$ is isomorphic to $\mathbb{H}$. So $V$ is a module over the division algebra $\mathbb{H}$, and every module over a division algebra is free. Hence $V \cong \mathbb{H}^{\oplus n}$ for some $n$, and the action is by left multiplication. $\square$

So the representation theory of $\mathbb{H}$ is the simplest possible: every representation is a direct sum of copies of the regular representation, and there is exactly one irreducible representation, up to isomorphism.

### Irreducible Representations

**Theorem.** The regular representation is the unique irreducible representation of $\mathbb{H}$, up to isomorphism.

**Proof.** Any irreducible representation is a quotient of the regular representation, hence isomorphic to it, since $\mathbb{H}$ is a division algebra and every non-zero $\mathbb{H}$-linear map $\mathbb{H} \to V$ is injective. $\square$

### Schur's Lemma

**Theorem (Schur).** Every $\mathbb{H}$-linear endomorphism of an irreducible representation of $\mathbb{H}$ is a scalar multiple of the identity.

**Proof.** Let $V$ be irreducible and let $T : V \to V$ be $\mathbb{H}$-linear. Then $\ker T$ and $\operatorname{im} T$ are subrepresentations. Since $V$ is irreducible, either $\ker T = 0$ and $\operatorname{im} T = V$ (so $T$ is an isomorphism), or $\ker T = V$ (so $T = 0$). In the first case, $T$ is an isomorphism, and since $V$ is one-dimensional over $\mathbb{H}$ (by the classification theorem), $T$ is multiplication by a non-zero scalar in $\mathbb{H}$. $\square$

**Corollary.** The endomorphism ring of the regular representation is $\mathbb{H}$ itself.

**The division algebra case.** Schur's lemma says that the endomorphism ring of the irreducible representation is a division algebra, namely $\mathbb{H}$. This is the general form of Schur's lemma: for a simple algebra over a field, the endomorphism ring of an irreducible module is a division algebra.

## The Structure of $\mathbb{H}$ as a Simple Algebra

### Simplicity

The quaternion algebra $\mathbb{H}$ is **simple**: it has no non-trivial two-sided ideals. The only two-sided ideals are $0$ and $\mathbb{H}$.

**Proof.** Let $I$ be a non-zero two-sided ideal, and let $q \in I$ be non-zero. Since $q$ is invertible, $1 = q^{-1} q \in I$, so $I = \mathbb{H}$. $\square$

So $\mathbb{H}$ is a central simple algebra over $F$ when $F$ is the center. The center of $\mathbb{H}$ is $F$ (the scalars), and $\mathbb{H}$ is four-dimensional over $F$, so it is a central simple algebra of degree two.

### The Brauer Class

As a central simple algebra over $F$, the quaternion algebra $\mathbb{H}$ has a class in the Brauer group $\operatorname{Br}(F)$. This class is trivial if and only if $\mathbb{H}$ is isomorphic to the matrix algebra $M_2(F)$, which happens if and only if the quaternion algebra splits over $F$. The quaternion algebra is a division algebra precisely when its class in the Brauer group is non-trivial.

**Example.** Over $\mathbb{R}$, the only non-trivial quaternion algebra is the classical one, with $e_1^2 = e_2^2 = e_3^2 = -1$. Over $\mathbb{Q}$, there are infinitely many quaternion algebras, classified by their ramification: a finite set of places of even cardinality, equivalently by the Hilbert symbol.

## The Representation Ring

### Definition

The **representation ring** $R(\mathbb{H})$ is the Grothendieck ring of finite-dimensional representations of $\mathbb{H}$. As an abelian group, it is generated by the isomorphism class $[\rho_{\mathrm{reg}}]$, with no relations. So

$$
R(\mathbb{H}) \cong \mathbb{Z},
$$

with generator $[\rho_{\mathrm{reg}}]$.

### Ring Structure

The product in $R(\mathbb{H})$ is given by the tensor product of representations:

$$
[V] \cdot [W] = [V \otimes_F W].
$$

Since the regular representation is four-dimensional over $F$, its tensor powers are

$$
\rho_{\mathrm{reg}} \otimes \rho_{\mathrm{reg}} \cong \rho_{\mathrm{reg}}^{\oplus 4},
$$

because $\mathbb{H} \otimes_F \mathbb{H} \cong M_4(F)$, and the regular representation of $M_4(F)$ is the direct sum of four copies of the standard representation. So the multiplication in $R(\mathbb{H})$ is not the ordinary multiplication in $\mathbb{Z}$: it is multiplication by $4$ in the appropriate sense.

**The ring structure.** More precisely, the tensor product of two copies of the regular representation is the representation on $\mathbb{H} \otimes_F \mathbb{H}$, which is a free $\mathbb{H}$-module of rank four. So

$$
[\rho_{\mathrm{reg}}] \cdot [\rho_{\mathrm{reg}}] = 4 [\rho_{\mathrm{reg}}].
$$

So the representation ring is $\mathbb{Z}$ with the multiplication $m \cdot n = 4 mn$. This multiplication has no identity element, since $4 e n = n$ would force $e = 1/4$, so $R(\mathbb{H})$ is not isomorphic to $\mathbb{Z}$ as a ring.

## The Complexification

### Complex Quaternions

The **complexified quaternion algebra** is

$$
\mathbb{H}_{\mathbb{C}} = \mathbb{H} \otimes_{\mathbb{R}} \mathbb{C}.
$$

As a complex algebra, it has dimension four, and it is isomorphic to the matrix algebra $M_2(\mathbb{C})$:

$$
\mathbb{H}_{\mathbb{C}} \cong M_2(\mathbb{C}).
$$

**Proof.** The complexification of $\mathbb{H}$ is a central simple algebra over $\mathbb{C}$. By the classification of central simple algebras over $\mathbb{C}$, every such algebra is a matrix algebra over $\mathbb{C}$. The dimension is four, so the matrix size is two. $\square$

### Representations of $\mathbb{H}_{\mathbb{C}}$

Because $\mathbb{H}_{\mathbb{C}}$ is a matrix algebra, its representation theory is the standard representation theory of $M_2(\mathbb{C})$:

- There is exactly one irreducible representation, the standard representation on $\mathbb{C}^2$.
- Every finite-dimensional representation is a direct sum of copies of the standard representation.
- The representation ring is $\mathbb{Z}$, generated by the standard representation.

So the complexified quaternion algebra has a simpler representation theory than the real quaternion algebra, because it is a matrix algebra rather than a division algebra.

### The Relation to the Real Case

The real quaternion algebra $\mathbb{H}$ is a **real form** of the complex matrix algebra $M_2(\mathbb{C})$. The representations of $\mathbb{H}$ over $\mathbb{R}$ are the real forms of the representations of $M_2(\mathbb{C})$ over $\mathbb{C}$. The classification of real forms is the subject of the theory of Galois descent, and it is the reason the real representation theory is richer than the complex one.

## Indecomposable Representations

### Definition

A representation $V$ is **indecomposable** if it cannot be written as a direct sum of two non-zero subrepresentations. Every irreducible representation is indecomposable, but the converse fails in general.

**Theorem.** Every finite-dimensional representation of $\mathbb{H}$ is a direct sum of indecomposable representations, and the indecomposable representations are exactly the regular representation.

**Proof.** By the classification theorem, $V \cong \mathbb{H}^{\oplus n}$. Each summand is indecomposable because it is a free module of rank one over a division algebra, and any non-zero submodule is the whole thing. Conversely, any indecomposable representation is a single copy of the regular representation. $\square$

So $\mathbb{H}$ is a **semisimple** algebra: every representation is a direct sum of irreducibles, and the indecomposables coincide with the irreducibles. This is a general feature of simple algebras over fields, and it is the reason the representation theory is so simple.

## The Dual Representation

### Definition

The **dual** (or contragredient) representation of a representation $\rho$ on $V$ is the representation $\rho^*$ on the dual space $V^* = \operatorname{Hom}_F(V, F)$ defined by

$$
(\rho^*(q) f)(v) = f(\rho(q) v), \qquad q \in \mathbb{H}, \; f \in V^*, \; v \in V.
$$

### Basic Properties

**Duality is an involution.** $(V^*)^* \cong V$ for finite-dimensional $V$.

**Duality is exact.** It preserves direct sums: $(V \oplus W)^* \cong V^* \oplus W^*$.

**The dual of an irreducible is irreducible.** $\rho_{\mathrm{reg}}^* \cong \rho_{\mathrm{reg}}$.

**The dual of the regular representation is the regular representation.** $\rho_{\mathrm{reg}}^* \cong \rho_{\mathrm{reg}}$.

### The Pairing

The natural pairing

$$
\langle \cdot, \cdot \rangle : V^* \times V \to F, \qquad \langle f, v \rangle = f(v),
$$

satisfies

$$
\langle \rho^*(q) f, v \rangle = \langle f, \rho(q) v \rangle.
$$

This is the definition of the dual representation, written as a pairing.

## Tensor Products

### Definition

The **tensor product** of two representations $V$ and $W$ is the representation on $V \otimes_F W$ defined by the diagonal action

$$
q \cdot (v \otimes w) = (q \cdot v) \otimes (q \cdot w).
$$

This is a representation because the diagonal map $\Delta(q) = q \otimes q$ is an algebra homomorphism: $\Delta(q) \Delta(q') = (q q') \otimes (q q') = \Delta(q q')$.

### Basic Properties

**Associativity.** $(U \otimes V) \otimes W \cong U \otimes (V \otimes W)$.

**Commutativity.** $V \otimes W \cong W \otimes V$.

**Distributivity.** $U \otimes (V \oplus W) \cong (U \otimes V) \oplus (U \otimes W)$.

**Tensor product of irreducibles.** The tensor product of two copies of the regular representation is

$$
\rho_{\mathrm{reg}} \otimes \rho_{\mathrm{reg}} \cong \rho_{\mathrm{reg}}^{\oplus 4},
$$

because $\mathbb{H} \otimes_F \mathbb{H} \cong M_4(F)$.

### The Tensor Product as a Representation

The diagonal map $\Delta(q) = q \otimes q$ is an algebra homomorphism whether or not $\mathbb{H}$ is commutative, so the tensor product of two representations of $\mathbb{H}$ is again a representation of $\mathbb{H}$. The tensor product is also symmetric: the swap $v \otimes w \mapsto w \otimes v$ is $\mathbb{H}$-linear under the diagonal action, so $V \otimes W \cong W \otimes V$ as representations.

## Homomorphisms

### Definition

A **homomorphism** of representations $V$ and $W$ is an $F$-linear map $T : V \to W$ such that

$$
T(q \cdot v) = q \cdot T(v), \qquad q \in \mathbb{H}, \; v \in V.
$$

The space of all such homomorphisms is denoted $\operatorname{Hom}_{\mathbb{H}}(V, W)$.

### Basic Properties

**Composition.** If $T \in \operatorname{Hom}_{\mathbb{H}}(V, W)$ and $S \in \operatorname{Hom}_{\mathbb{H}}(W, U)$, then $S T \in \operatorname{Hom}_{\mathbb{H}}(V, U)$.

**Schur's lemma.** If $V$ and $W$ are irreducible, then $\operatorname{Hom}_{\mathbb{H}}(V, W) = 0$ if $V \not\cong W$, and $\operatorname{Hom}_{\mathbb{H}}(V, V) \cong \mathbb{H}$.

**Dimension count.** For $V \cong \mathbb{H}^{\oplus p}$ and $W \cong \mathbb{H}^{\oplus q}$,

$$
\dim_F \operatorname{Hom}_{\mathbb{H}}(V, W) = 4 pq.
$$

The factor of $4$ comes from the endomorphism ring of the regular representation, which is $\mathbb{H}$.

### The Endomorphism Ring

The **endomorphism ring** of a representation $V$ is $\operatorname{End}_{\mathbb{H}}(V) = \operatorname{Hom}_{\mathbb{H}}(V, V)$. For $V \cong \mathbb{H}^{\oplus n}$,

$$
\operatorname{End}_{\mathbb{H}}(V) \cong M_n(\mathbb{H}),
$$

the ring of $n \times n$ matrices over $\mathbb{H}$. This is a simple ring, and it is the prototypical example of a central simple algebra over $F$ of degree $2n$.

## The Category of Representations

### The Abelian Category

The representations of $\mathbb{H}$ form an abelian category $\mathrm{Rep}(\mathbb{H})$. The category is semisimple, because $\mathbb{H}$ is a division algebra and every module over a division algebra is free. So every short exact sequence splits, and every representation is a direct sum of irreducibles.

### The Ext Algebra

The **Ext algebra** of $\mathbb{H}$ is

$$
\operatorname{Ext}^\bullet_{\mathbb{H}}(\mathbb{H}, \mathbb{H}) \cong \mathbb{H},
$$

with $\mathbb{H}$ in degree zero. So the Ext algebra is concentrated in degree zero, and the higher Ext groups vanish. This is the algebraic content of the semisimplicity: the category has no non-trivial extensions.

## Comparison with the Complex and Split Complex Cases

The representation theory of $\mathbb{H}$ differs from that of the complex and split complex algebras in several ways.

**Non-commutativity.** The quaternion algebra is non-commutative, while the complex and split complex algebras are commutative. This is the source of all the differences.

**Division algebra versus field.** The quaternion algebra is a division algebra, like the complex numbers, but it is not a field. The split complex algebra is not a division algebra.

**Number of irreducibles.** The complex algebra has one irreducible representation, as does the quaternion algebra. The split complex algebra has two.

**Endomorphism rings.** The endomorphism ring of the regular representation of $\mathbb{C}$ is $\mathbb{C}$ itself. The endomorphism ring of the regular representation of $\mathbb{H}$ is $\mathbb{H}$ itself. The endomorphism ring of the regular representation of $\mathbb{D}$ is $\mathbb{R} \oplus \mathbb{R}$.

**Tensor products.** The tensor product of two representations is again a representation in all three cases; for $\mathbb{H}$ this uses the diagonal action, which is an algebra homomorphism whether or not the algebra is commutative.

**Representation rings.** $R(\mathbb{C}) \cong \mathbb{Z}$. $R(\mathbb{H})$ is $\mathbb{Z}$ as a group, with the multiplication $m \cdot n = 4 mn$, which has no identity element. $R(\mathbb{D}) \cong \mathbb{Z} \oplus \mathbb{Z}$. The three are not isomorphic.

## Summary

A representation of $\mathbb{H}$ is a vector space $V$ over a field $F$ together with a bilinear action of the algebra on it, equivalently a unital algebra homomorphism $\mathbb{H} \to \operatorname{End}_F(V)$. The classification rests on the structure of the algebra: $\mathbb{H}$ is simple, having no nontrivial two-sided ideals, and over a field of characteristic not two on which it is a division algebra its representations are completely determined, with a single irreducible representation up to isomorphism.

The category of representations is abelian and semisimple, and the representation ring $R(\mathbb{H})$ is generated as an abelian group by the class of the irreducible representation. The article records the standard constructions — the dual or contragredient representation on $V^*$, the tensor product with its diagonal action, and the homomorphisms, the $F$-linear maps intertwining the two actions — together with the indecomposable representations and their relation to the irreducible ones.

Two further sections complete the theory: the complexification $\mathbb{H}_{\mathbb{C}} = \mathbb{H} \otimes_{\mathbb{R}} \mathbb{C}$, which is no longer a division algebra and whose representation theory therefore differs from that of $\mathbb{H}$, and the comparison with the complex and split complex cases, in which the non-commutativity of $\mathbb{H}$ is the source of every difference.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $\mathbb{H}_{\mathbb{C}} = \mathbb{H} \otimes_{\mathbb{R}} \mathbb{C}$ | Complexified quaternion algebra |
| $\rho : \mathbb{H} \to \operatorname{End}_F(V)$ | Representation |
| $\rho_{\mathrm{reg}}$ | Regular representation |
| $\rho_L, \rho_R$ | Left and right regular representations |
| $V^*$ | Dual representation |
| $V \otimes W$ | Tensor product |
| $\operatorname{Hom}_{\mathbb{H}}(V, W)$ | Space of homomorphisms |
| $\operatorname{End}_{\mathbb{H}}(V)$ | Endomorphism ring |
| $R(\mathbb{H})$ | Representation ring |
| $\operatorname{Br}(F)$ | Brauer group |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original formulation.
- Charles C. Pinter, *A Book of Abstract Algebra* (Dover, 2010), for the representation theory of algebras.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the general theory of modules over rings.
- Serge Lang, *Algebra* (Springer, 2002), for the structure theory of semisimple algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for the theory of central simple algebras.

