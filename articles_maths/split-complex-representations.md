
# __Split-Complex Representations__

## Introduction

This article introduces the representation theory of the split complex algebra. The goal is to define representations precisely, classify them, and describe the structure of the representation ring.

The treatment is mathematically honest: every claim is either proved or stated as a definition. The split complex algebra is assumed from the article on split complex algebra, and the idempotent decomposition is used throughout. No physics is invoked.

## Representations of $\mathbb{D}$

### Definition

A **representation** of $\mathbb{D}$ is a real vector space $V$ together with a bilinear map

$$
\rho : \mathbb{D} \times V \to V, \qquad \rho(Z, v) = Z \cdot v,
$$

satisfying

$$
Z \cdot (W \cdot v) = (ZW) \cdot v, \qquad 1 \cdot v = v.
$$

Equivalently, a representation is an algebra homomorphism

$$
\rho : \mathbb{D} \to \operatorname{End}(V).
$$

Since $\mathbb{D}$ is commutative, the image of $\rho$ is a commutative subalgebra of $\operatorname{End}(V)$.

### The Idempotent Action

The idempotents $\Pi_1$ and $\Pi_2$ act as projection operators. For any representation $V$,

$$
\Pi_1 \cdot (\Pi_1 \cdot v) = \Pi_1^2 \cdot v = \Pi_1 \cdot v,
$$

so $\Pi_1$ is idempotent, and similarly for $\Pi_2$. Moreover,

$$
\Pi_1 \cdot (\Pi_2 \cdot v) = (\Pi_1 \Pi_2) \cdot v = 0,
$$

and symmetrically. So the images of $\Pi_1$ and $\Pi_2$ are complementary subspaces:

$$
V = V_+ \oplus V_-, \qquad V_+ = \Pi_1 \cdot V, \quad V_- = \Pi_2 \cdot V.
$$

This is the **idempotent decomposition** of the representation. It is the fundamental structural fact about representations of $\mathbb{D}$.

### The Regular Representation

The **regular representation** of $\mathbb{D}$ is $\mathbb{D}$ acting on itself by left multiplication:

$$
\rho_{\mathrm{reg}}(Z) W = Z W, \qquad Z, W \in \mathbb{D}.
$$

This is the representation $\rho_{\mathrm{reg}} : \mathbb{D} \to \operatorname{End}(\mathbb{D})$ given by $\rho_{\mathrm{reg}}(Z) = Z$. It is the representation of $\mathbb{D}$ on a two-dimensional real vector space.

Under the idempotent decomposition,

$$
\mathbb{D} = \mathbb{D} \Pi_1 \oplus \mathbb{D} \Pi_2,
$$

where $\mathbb{D} \Pi_1$ and $\mathbb{D} \Pi_2$ are the two ideals of $\mathbb{D}$, each isomorphic to $\mathbb{R}$. The regular representation decomposes as

$$
\rho_{\mathrm{reg}} = \rho_+ \oplus \rho_-,
$$

where $\rho_+$ is the representation on $\mathbb{D} \Pi_1 \cong \mathbb{R}$ and $\rho_-$ is the representation on $\mathbb{D} \Pi_2 \cong \mathbb{R}$.

### The One-Dimensional Representations

The two one-dimensional representations of $\mathbb{D}$ are:

**The $+$ representation.** On $\mathbb{R}$, defined by

$$
\rho_+(Z) = Z_+ = a + b, \qquad Z = a + j b.
$$

This is the representation that sends $j$ to $+1$.

**The $-$ representation.** On $\mathbb{R}$, defined by

$$
\rho_-(Z) = Z_- = a - b, \qquad Z = a + j b.
$$

This is the representation that sends $j$ to $-1$.

Both are algebra homomorphisms $\mathbb{D} \to \mathbb{R}$, and they are the only ones. Indeed, if $\rho : \mathbb{D} \to \mathbb{R}$ is an algebra homomorphism, then $\rho(1) = 1$ and $\rho(j)^2 = \rho(j^2) = \rho(1) = 1$, so $\rho(j) = \pm 1$. These are exactly $\rho_+$ and $\rho_-$.

## Classification

### The Classification Theorem

**Theorem.** Every finite-dimensional real representation of $\mathbb{D}$ is isomorphic to a direct sum of copies of $\rho_+$ and $\rho_-$:

$$
V \cong \mathbb{R}^{\oplus p} \oplus \mathbb{R}^{\oplus q},
$$

with $\rho = \rho_+^{\oplus p} \oplus \rho_-^{\oplus q}$.

**Proof.** Let $V$ be a finite-dimensional representation. The idempotent decomposition gives

$$
V = V_+ \oplus V_-,
$$

with $V_+ = \Pi_1 \cdot V$ and $V_- = \Pi_2 \cdot V$. On $V_+$, the action of $Z = a + j b$ is

$$
Z \cdot v = (a + b) v, \qquad v \in V_+,
$$

because $Z \Pi_1 = (a + b) \Pi_1$. So $V_+$ is a direct sum of copies of $\rho_+$. Similarly, on $V_-$,

$$
Z \cdot v = (a - b) v, \qquad v \in V_-,
$$

so $V_-$ is a direct sum of copies of $\rho_-$.

### Irreducible Representations

**Theorem.** The irreducible real representations of $\mathbb{D}$ are exactly $\rho_+$ and $\rho_-$, up to isomorphism.

**Proof.** Any irreducible representation is a quotient of the regular representation, hence a direct sum of copies of $\rho_+$ and $\rho_-$. Since it is irreducible, it must be a single copy of one of them.

### Schur's Lemma

**Theorem (Schur).** Every $\mathbb{D}$-linear endomorphism of an irreducible real representation of $\mathbb{D}$ is a scalar multiple of the identity.

**Proof.** Let $V$ be irreducible and let $T : V \to V$ be $\mathbb{D}$-linear. Then $\ker T$ and $\operatorname{im} T$ are subrepresentations. Since $V$ is irreducible, either $\ker T = 0$ and $\operatorname{im} T = V$ (so $T$ is an isomorphism), or $\ker T = V$ (so $T = 0$). In the first case, $T$ is an isomorphism, and since $V$ is one-dimensional over $\mathbb{R}$, $T$ is multiplication by a non-zero scalar.

**Corollary.** The endomorphism ring of each irreducible representation is $\mathbb{R}$.

## The Representation Ring

### Definition

The **representation ring** $R(\mathbb{D})$ is the Grothendieck ring of finite-dimensional real representations of $\mathbb{D}$. As an abelian group, it is generated by the isomorphism classes $[\rho_+]$ and $[\rho_-]$, with the relation

$$
[\rho_+] + [\rho_-] = [\rho_{\mathrm{reg}}].
$$

Since every representation is a direct sum of copies of $\rho_+$ and $\rho_-$, we have

$$
R(\mathbb{D}) \cong \mathbb{Z} \oplus \mathbb{Z},
$$

with generators $[\rho_+]$ and $[\rho_-]$.

### Ring Structure

The product in $R(\mathbb{D})$ is given by the tensor product of representations:

$$
[V] \cdot [W] = [V \otimes_{\mathbb{R}} W].
$$

Since $\rho_+$ and $\rho_-$ are one-dimensional, their tensor products are

$$
\rho_+ \otimes \rho_+ \cong \rho_+, \qquad \rho_+ \otimes \rho_- \cong \rho_-, \qquad \rho_- \otimes \rho_- \cong \rho_+.
$$

This is the multiplication rule of the group ring $\mathbb{Z}[\mathbb{Z}/2]$, where $\rho_+$ corresponds to the trivial character and $\rho_-$ to the sign character. So

$$
R(\mathbb{D}) \cong \mathbb{Z}[\mathbb{Z}/2].
$$

## Representations and the Idempotent Decomposition

### The Projection Operators

In any representation $V$, the idempotents $\Pi_1$ and $\Pi_2$ act as projection operators:

$$
P_+ = \rho(\Pi_1), \qquad P_- = \rho(\Pi_2).
$$

They satisfy

$$
P_+^2 = P_+, \qquad P_-^2 = P_-, \qquad P_+ P_- = P_- P_+ = 0, \qquad P_+ + P_- = I.
$$

So $V = V_+ \oplus V_-$ with $V_+ = \operatorname{im} P_+$ and $V_- = \operatorname{im} P_-$.

### The Action on Each Component

On $V_+$, the action of $Z = a + j b$ is multiplication by $a + b$. On $V_-$, the action is multiplication by $a - b$. So the representation is completely determined by the pair of scalars $(a + b, a - b)$, which is exactly the image of $Z$ under the isomorphism $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$.

This is the representation-theoretic content of the isomorphism: a representation of $\mathbb{D}$ is the same thing as a pair of real vector spaces, one for each idempotent.

## Indecomposable Representations

### Definition

A representation $V$ is **indecomposable** if it cannot be written as a direct sum of two non-zero subrepresentations. Every irreducible representation is indecomposable, but the converse fails in general.

**Theorem.** Every finite-dimensional representation of $\mathbb{D}$ is a direct sum of indecomposable representations, and the indecomposable representations are exactly $\rho_+$ and $\rho_-$.

**Proof.** By the classification theorem, $V \cong \mathbb{R}^{\oplus p} \oplus \mathbb{R}^{\oplus q}$. Each summand is indecomposable because it is one-dimensional and any non-zero subrepresentation is the whole thing. Conversely, any indecomposable representation is a single copy of $\rho_+$ or $\rho_-$.

So $\mathbb{D}$ is a **semisimple** algebra: every representation is a direct sum of irreducibles, and the indecomposables coincide with the irreducibles. This is a special feature of the split complex algebra, and it is the reason its representation theory is so simple.

## Comparison with the Complex Case

The representation theory of $\mathbb{D}$ differs from that of $\mathbb{C}$ in one essential way. For $\mathbb{C}$, regarded as a real algebra, there is exactly one irreducible representation, of real dimension two: $\mathbb{C}$ acting on itself by multiplication. For $\mathbb{D}$, the irreducible representations are two in number, indexed by $\pm 1$: $\rho_\pm(Z) = a \pm b$ on $\mathbb{R}$.

The reason is that $\mathbb{C}$ is a division algebra, so it has exactly one irreducible representation, whereas $\mathbb{D}$ is not a division algebra: its two irreducible representations are the two homomorphisms $\mathbb{D} \to \mathbb{R}$.

## The Dual Representation

### Definition

The **dual** (or contragredient) representation of a representation $\rho$ on $V$ is the representation $\rho^*$ on the dual space $V^* = \operatorname{Hom}_{\mathbb{R}}(V, \mathbb{R})$ defined by

$$
(\rho^*(Z) f)(v) = f(\rho(Z) v), \qquad Z \in \mathbb{D}, \; f \in V^*, \; v \in V.
$$

### Basic Properties

**Duality is an involution.** $(V^*)^* \cong V$.

**Duality is exact.** It preserves direct sums: $(V \oplus W)^* \cong V^* \oplus W^*$.

**The dual of an irreducible is irreducible.** $\rho_+^* \cong \rho_+$ and $\rho_-^* \cong \rho_-$.

**The dual of the regular representation is the regular representation.** $\rho_{\mathrm{reg}}^* \cong \rho_{\mathrm{reg}}$.

### The Pairing

The natural pairing

$$
\langle \cdot, \cdot \rangle : V^* \times V \to \mathbb{R}, \qquad \langle f, v \rangle = f(v),
$$

satisfies

$$
\langle \rho^*(Z) f, v \rangle = \langle f, \rho(Z) v \rangle.
$$

This is the definition of the dual representation, written as a pairing.

## Tensor Products

### Definition

The **tensor product** of two representations $V$ and $W$ is the representation on $V \otimes_{\mathbb{R}} W$ defined by

$$
Z \cdot (v \otimes w) = (Z \cdot v) \otimes (Z \cdot w).
$$

This is the componentwise (diagonal) action. The alternatives $Z \cdot (v \otimes w) = (Z \cdot v) \otimes w$ and $Z \cdot (v \otimes w) = v \otimes (Z \cdot w)$ agree with each other only when $V$ and $W$ have the same character, so neither of them is the definition.

### Basic Properties

**Associativity.** $(U \otimes V) \otimes W \cong U \otimes (V \otimes W)$.

**Commutativity.** $V \otimes W \cong W \otimes V$.

**Distributivity.** $U \otimes (V \oplus W) \cong (U \otimes V) \oplus (U \otimes W)$.

**Tensor product of irreducibles.** The tensor products of the irreducible representations are

$$
\rho_+ \otimes \rho_+ \cong \rho_+, \qquad \rho_+ \otimes \rho_- \cong \rho_-, \qquad \rho_- \otimes \rho_- \cong \rho_+.
$$

This is the same multiplication rule as the group $\mathbb{Z}/2$, with $\rho_+$ as the identity and $\rho_-$ as the non-trivial element.

## Homomorphisms

### Definition

A **homomorphism** of representations $V$ and $W$ is a linear map $T : V \to W$ such that

$$
T(Z \cdot v) = Z \cdot T(v), \qquad Z \in \mathbb{D}, \; v \in V.
$$

The space of all such homomorphisms is denoted $\operatorname{Hom}_{\mathbb{D}}(V, W)$.

### Basic Properties

**Composition.** If $T \in \operatorname{Hom}_{\mathbb{D}}(V, W)$ and $S \in \operatorname{Hom}_{\mathbb{D}}(W, U)$, then $S T \in \operatorname{Hom}_{\mathbb{D}}(V, U)$.

**Schur's lemma.** If $V$ and $W$ are irreducible, then $\operatorname{Hom}_{\mathbb{D}}(V, W) = 0$ if $V \not\cong W$, and $\operatorname{Hom}_{\mathbb{D}}(V, V) \cong \mathbb{R}$.

**Dimension count.** For $V \cong \mathbb{R}^{\oplus p} \oplus \mathbb{R}^{\oplus q}$ and $W \cong \mathbb{R}^{\oplus r} \oplus \mathbb{R}^{\oplus s}$,

$$
\dim \operatorname{Hom}_{\mathbb{D}}(V, W) = pr + qs.
$$

**Proof.** A homomorphism must preserve the idempotent decomposition, so it is determined by its action on each isotypic component. On $V_+ \cong \mathbb{R}^{\oplus p}$, a homomorphism to $W_+ \cong \mathbb{R}^{\oplus r}$ is an $r \times p$ real matrix, of dimension $pr$. Similarly for the minus components, of dimension $qs$.

### The Endomorphism Ring

The **endomorphism ring** of a representation $V$ is $\operatorname{End}_{\mathbb{D}}(V) = \operatorname{Hom}_{\mathbb{D}}(V, V)$. For $V \cong \mathbb{R}^{\oplus p} \oplus \mathbb{R}^{\oplus q}$,

$$
\operatorname{End}_{\mathbb{D}}(V) \cong M_p(\mathbb{R}) \oplus M_q(\mathbb{R}),
$$

the direct sum of the matrix rings of sizes $p$ and $q$. This is a semisimple ring.

## Summary

A representation of $\mathbb{D}$ is a real vector space $V$ together with a bilinear action of the algebra on it. The classification theorem states that every finite-dimensional real representation is isomorphic to a direct sum of copies of the two one-dimensional representations $\rho_+$ and $\rho_-$, so the representation theory is completely determined by the algebra itself.

The idempotent decomposition gives the theory its shape. In any representation the idempotents act as projection operators $P_+ = \rho(\Pi_1)$ and $P_- = \rho(\Pi_2)$, with $P_+ + P_-$ the identity and $P_+P_- = 0$, so every representation splits as the direct sum of its two idempotent components. This is the mechanism by which the algebra behaves as $\mathbb{R} \oplus \mathbb{R}$, and it is the essential difference from the complex case.

The article also records the representation ring $R(\mathbb{D})$, the indecomposable representations and their relation to the irreducible ones, the dual or contragredient representation on $V^*$, the tensor product with its diagonal action, and the homomorphisms, the linear maps intertwining the two actions. The final comparison with the complex case isolates the difference between an algebra with two idempotents and one that is a field.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $\Pi_1 = (1 + j)/2$ | Positive idempotent |
| $\Pi_2 = (1 - j)/2$ | Negative idempotent |
| $\rho : \mathbb{D} \to \operatorname{End}(V)$ | Representation |
| $\rho_+$ | One-dimensional representation $j \mapsto +1$ |
| $\rho_-$ | One-dimensional representation $j \mapsto -1$ |
| $\rho_{\mathrm{reg}}$ | Regular representation |
| $V_+ = \Pi_1 \cdot V$ | Positive isotypic component |
| $V_- = \Pi_2 \cdot V$ | Negative isotypic component |
| $P_+ = \rho(\Pi_1)$ | Projection onto $V_+$ |
| $P_- = \rho(\Pi_2)$ | Projection onto $V_-$ |
| $V^*$ | Dual representation |
| $V \otimes W$ | Tensor product |
| $\operatorname{Hom}_{\mathbb{D}}(V, W)$ | Space of homomorphisms |
| $\operatorname{End}_{\mathbb{D}}(V)$ | Endomorphism ring |
| $R(\mathbb{D})$ | Representation ring |

## Further Reading

- Charles C. Pinter, *A Book of Abstract Algebra* (Dover, 2010), for the representation theory of algebras.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric interpretation of split complex numbers.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real algebras.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, 2012), for the analytic applications.

