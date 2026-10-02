# __The Transfer Map__

## Introduction

A covering $p : E \to B$ is a map in the direction $E \to B$, and the functoriality of homology of *Simplicial and Singular Homology* carries it to a homomorphism $p_* : H_n(E;R) \to H_n(B;R)$ in the same direction. The **transfer** is a homomorphism in the opposite direction,

$$
\tau_* : H_n(B;R) \longrightarrow H_n(E;R),
$$

built by summing a singular simplex of the base over all its lifts. It is the archetype of an operator that is *not* induced by a continuous map of spaces — there is generally no continuous section $B \to E$ — and this is what makes it useful: it records the multiplicity of the covering at the level of chains, it turns the homology of a free quotient into the fixed part of the homology of the cover, and it is the map through which the Euler class and the Gysin sequence of a two-fold covering are later written.

The article does two things, matching the two clauses of its scope. It constructs the transfer on chains and on homology, and it studies its two composition laws: with the boundary operator, which commutes with it and gives a map of the long exact sequences of a pair, and with the projection, where the composites are $p_* \tau_* = d$ and $\tau_* p_* = \sum_{g} g_*$. The first law says the transfer is a chain map; the second says it is a retraction of the projection up to the degree $d$ and identifies the homology of the base with the fixed part of the homology of the cover whenever $d$ is invertible in the coefficient ring.

The covering theory used here — evenly covered sets, path and homotopy lifting, deck transformations, the correspondence between connected coverings and subgroups of the fundamental group — is that of *The Fundamental Group and Covering Spaces*, and the singular theory, its boundary operator and its functoriality are those of *Simplicial and Singular Homology*; neither is re-derived. The long exact sequence of a pair and the snake lemma are those of *Exact Sequences*; the general algebra of chain complexes over a ring, of which the singular complex is an instance, is the planned *Homological Algebra* of Part I, written in parallel, and is cited only for what it supplies.

Throughout, $p : E \to B$ is a covering, $B$ is path-connected, locally path-connected and semilocally simply connected, $E$ is path-connected, and the covering is **regular**: its deck group $G = \operatorname{Deck}(E/B)$ acts transitively on each fibre, so that $B = E/G$ and the fibre over each point is a free $G$-orbit. The group $G$ is finite of order $d$, the covering has $d$ sheets, and $R$ is a commutative ring with identity $1 \neq 0$ in which the degree makes sense; the interesting case is $d$ invertible in $R$, in particular $R$ a field of characteristic not dividing $d$. Coefficients are written after a semicolon and are suppressed when no confusion arises. The article treats the regular finite case; the general finite covering is recorded as a remark in the section on the projection.

## The Transfer on Chains

### The Setting

**Definition.** A **covering of pairs** $p : (E, E_A) \to (B, A)$ consists of a covering $p : E \to B$ and a subspace $A \subseteq B$ with $E_A = p^{-1}(A)$; the deck group $G$ acts on $E$ preserving $E_A$, so that $A = E_A/G$ and the restriction $p : E_A \to A$ is a covering with the same deck group.

The singular chain complex $C_*(E;R)$ is a complex of $R[G]$-modules: a deck transformation $g$ induces the chain map $g_\# : C_n(E;R) \to C_n(E;R)$ by $g_\#(\eta) = g \circ \eta$, and $p_\# g_\# = p_\#$. The deck action commutes with the boundary, $g_\# \partial = \partial g_\#$, because $g$ is a homeomorphism.

**Definition.** Let $F$ be the fixed part of a complex of $R[G]$-modules $M$,

$$
M^{G} = \{m \in M : g\,m = m \text{ for all } g \in G\},
$$

the **invariant subcomplex**; the **coinvariant complex** is the quotient $M_G = M / \langle gm - m\rangle_{g \in G, m \in M}$.

The singular complex of the base is the coinvariant complex of the cover. The reason is that a singular simplex of $B$ need not lift to a $G$-invariant simplex — it lifts to $d$ of them, one in each sheet — but the average does, and the assignment that sends a simplex to the sum of its lifts passes to the quotient.

### The Transfer of a Simplex

**Definition.** Let $\sigma : \Delta_n \to B$ be a singular $n$-simplex and let $\tilde\sigma : \Delta_n \to E$ be a lift of $\sigma$. The **transfer** of $\sigma$ is the chain

$$
\tau_n(\sigma) = \sum_{g \in G} g_\#(\tilde\sigma) = \sum_{g \in G} g \circ \tilde\sigma \;\in\; C_n(E;R),
$$

and $\tau_n : C_n(B;R) \to C_n(E;R)$ is its $R$-linear extension.

A lift of $\sigma$ exists because $\Delta_n$ is contractible and, more precisely, simply connected: path lifting along $\sigma$ from a chosen lift of $\sigma(v_0)$ produces $\tilde\sigma$ and, by the homotopy lifting property of *The Fundamental Group and Covering Spaces*, the lift is unique. The image of $\tau_n$ is a sum over the whole fibre orbit, which is the surgical point of the definition.

**Lemma.** $\tau_n$ is well defined: it does not depend on the choice of the lift $\tilde\sigma$.

*Proof.* Let $\tilde\sigma'$ be a second lift. Both are lifts of $\sigma$ and have the same domain, so by uniqueness of lifts applied to the connected space $\Delta_n$ there is $h \in G$ with $\tilde\sigma' = h \circ \tilde\sigma$. Then

$$
\sum_{g \in G} g \circ \tilde\sigma' = \sum_{g \in G} g \circ h \circ \tilde\sigma = \sum_{g \in G} g \circ \tilde\sigma,
$$

the last equality because $g \mapsto gh$ is a bijection of $G$. $\square$

Note that no global section of $p$ and no choice of a basepoint of $E$ is involved: each simplex is handled separately, and the ambiguity is absorbed by the summation over the finite group.

**Proposition.** The transfer is natural for maps of the cover: a deck transformation $h \in G$ satisfies $h_\# \tau_n = \tau_n$, and the projection satisfies

$$
p_\#\, \tau_n = d \cdot \mathrm{id}_{C_n(B;R)}, \qquad\qquad
\tau_n\, p_\# = \sum_{g \in G} g_\# \quad \text{on } C_n(E;R).
$$

*Proof.* For the first, $h_\# \tau_n(\sigma) = \sum_g h g_\# \tilde\sigma = \sum_g (hg)_\# \tilde\sigma = \sum_g g_\# \tilde\sigma$, again because left multiplication by $h$ permutes $G$. For the second, $p_\# \tilde\sigma = \sigma$, so $p_\# \tau_n(\sigma) = \sum_g p_\# g_\# \tilde\sigma = \sum_g \sigma = d\,\sigma$. For the third, let $\eta : \Delta_n \to E$ be a simplex of the cover; then $p_\# \eta$ is a simplex of the base and $\eta$ is one of its lifts, so that $\tau_n(p_\# \eta) = \sum_g g_\# \eta$ by the definition; extending over the sum gives the identity. $\square$

The second identity is the **multiplicity** of the covering: the composite $p_\# \tau_n$ is multiplication by the number of sheets. The third is the **norm** operator $N = \sum_{g} g_\#$, whose image lies in the invariant subcomplex and whose square is $dN$.

### The Transfer is a Chain Map

**Theorem.** The transfer commutes with the boundary,

$$
\partial_n \tau_n = \tau_{n-1} \partial_n,
$$

so that $\tau_* = (\tau_n)$ is a chain map $C_*(B;R) \to C_*(E;R)$, and it induces the **homology transfer**

$$
\tau_* : H_n(B;R) \longrightarrow H_n(E;R).
$$

*Proof.* Let $\sigma : \Delta_n \to B$ and let $\tilde\sigma$ be a lift. The faces of $\tilde\sigma$ are the lifts of the corresponding faces of $\sigma$, and the deck action commutes with taking faces because $g \circ \sigma \circ \delta^i = (g \circ \sigma) \circ \delta^i$ with $\delta^i$ the face maps of *Simplicial and Singular Homology*. Hence

$$
\partial_n \tau_n(\sigma) = \partial_n \sum_g g_\#(\tilde\sigma) = \sum_g g_\# \partial_n(\tilde\sigma) = \sum_g g_\#\Bigl(\sum_i (-1)^i \tilde\sigma \circ \delta^i\Bigr) = \tau_{n-1}\partial_n(\sigma),
$$

so the two sides agree on the generators and therefore on all chains. A chain map carries cycles to cycles and boundaries to boundaries, whence the induced map on homology. $\square$

The proof uses only that the deck action is by homeomorphisms and that lifts of faces are faces of lifts; no smoothness and no analytic structure is involved.

**Corollary (reduced homology).** The transfer descends to reduced homology, $\tau_* : \tilde H_n(B;R) \to \tilde H_n(E;R)$, and the identities of the previous proposition hold with $\tilde H$ in place of $H$.

*Proof.* The augmentation $\varepsilon : C_0 \to R$ of *Simplicial and Singular Homology* satisfies $\varepsilon p_\# = \varepsilon$ on $C_0(E;R)$, so $\tau$ carries the augmented complex of the base to the augmented complex of the cover; the induced map is the reduced transfer. $\square$

## The Transfer on Homology

### The Fixed Part and the Multiplicity

**Theorem.** On homology the two composites are

$$
p_*\, \tau_* = d \cdot \mathrm{id}, \qquad\qquad \tau_*\, p_* = N_* := \sum_{g \in G} g_* .
$$

Consequently the image of $\tau_*$ is contained in the fixed part $H_n(E;R)^G = \{x : g_* x = x \ \forall g\}$.

*Proof.* The first two identities are the homology of the chain-level identities of the previous section, a chain map inducing the induced map. For the third, if $x = \tau_* y$ then $g_* x = g_* \tau_* y = \tau_* y = x$ by $g_\# \tau = \tau$; hence the image is fixed. $\square$

The composite $\tau_* p_*$ need not be the identity; it is the norm $N_*$, which is multiplication by $d$ on the fixed part and zero on the part where $G$ acts through a non-trivial module in characteristic not dividing $d$.

### The Isomorphism with the Fixed Part

**Theorem.** Suppose $d = |G|$ is invertible in $R$. Then the restriction

$$
p_* : H_n(E;R)^G \longrightarrow H_n(B;R)
$$

is an isomorphism, with inverse $d^{-1}\tau_*$. In particular the transfer is injective and

$$
H_n(B;R) \;\cong\; H_n(E;R)^G, \qquad\qquad H_n(E;R) \;\cong\; H_n(B;R) \oplus \ker p_* .
$$

*Proof.* Both maps $p_*$ and $d^{-1}\tau_*$ carry the fixed part to the fixed part: $p_*$ commutes with the deck action because $p \circ g = p$, and $\tau_*$ lands in the fixed part by the theorem. On the fixed part, $p_* d^{-1}\tau_* = d^{-1} (d\,\mathrm{id}) = \mathrm{id}$ and $d^{-1}\tau_* p_* = d^{-1} N_* = d^{-1}(d\,\mathrm{id}) = \mathrm{id}$, the last because every element of the fixed part is fixed by each $g_*$, so $N_* = d\cdot\mathrm{id}$ there. Hence the two maps are inverse isomorphisms. The splitting is the standard splitting of a linear map with a section up to the invertible scalar $d$; on the fixed part the sequence $0 \to H_n(E;R)^G \to H_n(E;R) \to \ker p_* \to 0$ is split by $d^{-1}\tau_* p_*$. $\square$

The theorem is the precise sense in which a finite covering does not lose the homology of the cover: rationally, the homology of the base is the invariant part, and the complementary part is the kernel of the projection. It also shows that the transfer contains all the information of the covering at the level of homology when the degree is invertible.

**Remark (coefficients where $d$ is not invertible).** Nothing in the construction requires $d$ invertible, and the identities $p_*\tau_* = d$ and $\tau_* p_* = N_*$ hold over every $R$. What fails is only the isomorphism: over $R$ where $d$ is zero or a zero divisor, the transfer need not be injective and $\ker p_*$ may meet the fixed part; the torsion this produces is what the transfer for integral coefficients sees, and it is the mechanism behind the Smith theory of the `*` articles of this category.

## The Relation to the Boundary

### Naturality with Respect to Pairs

**Theorem.** Let $p : (E, E_A) \to (B, A)$ be a covering of pairs. The transfer maps the relative chains to the relative chains, $\tau_n : C_n(B,A;R) \to C_n(E,E_A;R)$, commutes with the quotient boundary, and induces

$$
\tau_* : H_n(B,A;R) \longrightarrow H_n(E,E_A;R),
$$

with $p_* \tau_* = d$ and $\tau_* p_* = \sum_g g_*$ on relative homology.

*Proof.* A singular simplex of $A$ lifts to a simplex of $E_A$, so $\tau_n$ carries $C_n(A;R)$ into $C_n(E_A;R)$ and descends to the quotient of the relative complexes; the boundary of the quotient is induced by the boundary of the complexes, and $\partial \tau = \tau \partial$ descends. The two composites are computed as before. $\square$

### The Map of Long Exact Sequences

**Theorem.** The transfer is compatible with the connecting homomorphism. Write the long exact sequences of *Simplicial and Singular Homology* for the pair $(B,A)$ and for the pair $(E,E_A)$ in the same degrees; the transfer acts on the four absolute and relative homology groups in each degree, and every square of the resulting ladder commutes. In particular the connecting homomorphisms satisfy

$$
\partial \,\tau_*^{\mathrm{rel}} = \tau_*^{A}\,\partial ,
$$

where $\tau_*^{A}$ is the transfer of the restricted covering on $A$ and $\tau_*^{\mathrm{rel}}$ is the relative transfer. The absolute and relative transfers are the one chain map $\tau$ restricted to the appropriate complex.

*Proof.* The chain-level squares commute because $\tau$ is a chain map of the complexes of the pairs and the inclusions of the two pairs are natural; the snake lemma of *Exact Sequences* is natural in a map of short exact sequences of complexes, so the induced connecting maps commute with the induced maps on homology. Concretely, a relative cycle in $H_n(B,A;R)$ is represented by a chain whose boundary lies in $A$; its transfer has boundary the transfer of that boundary, which lies in $E_A$, so the transfer of a relative cycle is a relative cycle, and the two ways of taking the connecting class agree. $\square$

**Remark.** This is the sense in which the transfer is compatible with the boundary: it commutes with the boundary operator $\partial$, so it is a chain map, and it therefore commutes with every map built formally from $\partial$, of which the connecting homomorphism of a pair is the first. The same statement for the connecting map of a short exact sequence of coefficient systems, and for the differential of the Leray–Serre spectral sequence of the covering as a fibration, follows by naturality. The transfer for the two-fold covering, where $d = 2$ and the connecting homomorphism is cup product with the Euler class, is the subject of the sibling article *The Gysin Sequence of a Two-Fold Covering*, written below in this Part.

## The Composition with the Projection

### The Two Composites

The two composite identities are the whole of the interaction of the transfer with the projection, and they are worth reading as an adjointness pair. On the one hand $p_* \tau_* = d \cdot \mathrm{id}$, so $\tau_*$ is a section of $p_*$ up to the scalar $d$; on the other hand $\tau_* p_* = N_*$, the norm, whose image is the fixed part. When $d$ is invertible the scalar is harmless and the two identities say

$$
p_* \circ (d^{-1}\tau_*) = \mathrm{id}, \qquad (d^{-1}\tau_*) \circ p_*|_{H_*(E)^G} = \mathrm{id},
$$

that is, $p_*$ restricted to the fixed part is an isomorphism with inverse the averaged transfer $d^{-1}\tau_*$.

**Theorem (adjointness).** Let $\langle-,-\rangle$ be the evaluation pairing between cohomology and homology of *Cohomology and the Universal Coefficient Theorem*, and let $\tau^* : H^n(E;R) \to H^n(B;R)$ be the dual of the transfer, the **cohomology transfer**. Then for $\varphi \in H^n(E;R)$ and $c \in H_n(B;R)$,

$$
\langle \tau^*\varphi,\, c\rangle_{B} = \langle \varphi,\, \tau_* c\rangle_{E},
$$

so that $\tau^*$ is the adjoint of $\tau_*$ with respect to the evaluation pairings. Consequently $p^* \tau^* = d$ and $\tau^* p^* = \sum_g g^*$, and when $d$ is invertible $H^n(B;R) \cong H^n(E;R)^G$.

*Proof.* The first identity is the definition of the dual map; the composite identities are the duals of those for $\tau_*$, since $(p_* \tau_*)^* = \tau^* p^*$ and $(\tau_* p_*)^* = p^* \tau^*$. The fixed-part isomorphism is the dual of the homology statement. $\square$

**Remark (the general finite covering).** For a covering that is not regular the deck group need not act transitively on the fibres, and the transfer cannot be written as a sum over a group; it is then defined by summing a simplex over the $d$ points of its fibre with local choices of lift, the sum being independent of the choices, and it satisfies $p_*\tau_* = d$ with $\tau_*$ landing in the part of $H_*(E;R)$ fixed by the finite-index subgroup $p_*\pi_1(E)$ of $\pi_1(B)$. The regular case above is the one used later in the corpus, and the general case is quoted.

## Examples

**Example (the $n$-sheeted covering of the circle).** Let $p : S^1 \to S^1$, $p(z) = z^n$, with deck group $\mathbb{Z}/n$ acting by the standard generator. Then $H_1(S^1;\mathbb{Z}) \cong \mathbb{Z}$, $p_*$ is multiplication by $n$, and the transfer $\tau_*$ is the identity, consistently with $p_*\tau_* = n$ and $\tau_* p_* = N_* = n$ (the norm of the group ring acts on $\mathbb{Z}$ by $n$). Rationally, $H_1(S^1;\mathbb{Q})^{\mathbb{Z}/n} \cong \mathbb{Q}$ and $p_*$ is an isomorphism, as the theorem requires.

**Example (the double cover of the projective space).** Let $p : S^n \to \mathbb{RP}^n$ for $n \geq 1$, the two-sheeted covering with deck group $\mathbb{Z}/2$ generated by the antipodal map $T$. Over $\mathbb{Z}$, the top homology is $H_n(\mathbb{RP}^n;\mathbb{Z}) \cong \mathbb{Z}$ for $n$ odd and $0$ for $n$ even, while $H_n(S^n;\mathbb{Z}) \cong \mathbb{Z}$; for $n$ odd, $p_*$ is multiplication by $2$ and $\tau_*$ is an isomorphism onto $H_n(S^n;\mathbb{Z})^{T}$, on which $T_* = \mathrm{id}$ because $T$ is the antipodal map of odd sphere degree $(-1)^{n+1} = 1$. For $n$ even the antipodal map has degree $-1$, the fixed part of $H_n(S^n;\mathbb{Z})$ is zero, and $p_* = 0$, in agreement with $H_n(\mathbb{RP}^n;\mathbb{Z}) = 0$. Over $\mathbb{F}_2$ the identities read $p_*\tau_* = 2 = 0$ and $\tau_* p_* = 1 + T_* = 0$, both sides being zero, so the transfer carries no information over $\mathbb{F}_2$; this vanishing is exactly the mechanism of the mod-2 Smith theory.

**Example (the universal cover of a finite complex).** Let $X$ be a finite connected CW complex with finite fundamental group $\Gamma$ and universal cover $\tilde X$, so that $p : \tilde X \to X$ is a regular covering with deck group $\Gamma$ and $d = |\Gamma|$. If $\Gamma$ is finite and the coefficient ring is $\mathbb{Q}$, then $H_n(X;\mathbb{Q}) \cong H_n(\tilde X;\mathbb{Q})^\Gamma$ and the rational homology of $X$ is the invariant part of that of its universal cover. For the lens space $L(n;1) = S^3/(\mathbb{Z}/n)$ this reads $H_*(L(n;1);\mathbb{Q}) = H_*(S^3;\mathbb{Q})^{\mathbb{Z}/n}$, which is $\mathbb{Q}$ in degrees $0$ and $3$ and zero between, the rational homology of the sphere, as the integral computation of *Cohomology and the Universal Coefficient Theorem* confirms up to the torsion that the rational passage erases.

## Summary

The transfer of a regular finite covering $p : E \to B$ with deck group $G$ of order $d$ is the chain map $\tau : C_*(B;R) \to C_*(E;R)$ sending a singular simplex to the sum of its $d$ lifts, the sum over the deck group making the choice of lift irrelevant. It commutes with the boundary, so it is a chain map and induces $\tau_* : H_n(B;R) \to H_n(E;R)$; it satisfies the two composite laws $p_*\tau_* = d$ and $\tau_* p_* = \sum_g g_*$, so its image lies in the fixed part $H_n(E;R)^G$ and, when $d$ is invertible in $R$, the projection restricts to an isomorphism $H_n(E;R)^G \cong H_n(B;R)$ with inverse the averaged transfer $d^{-1}\tau_*$. On a pair it is a map of the long exact sequences, commuting with the connecting homomorphism; in cohomology the dual $\tau^*$ is the adjoint of $\tau_*$ under the evaluation pairing and satisfies the same composite laws. The construction uses only the covering theory and the singular complex; it uses no distance, no norm and no analysis, and its failure to be induced by a continuous map is what makes it the model of an operator on a chain complex that is not a map of spaces.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $p : E \to B$ | Regular covering, $B$ path-connected, locally path-connected, semilocally simply connected; $E$ path-connected |
| $G = \operatorname{Deck}(E/B)$ | Deck group, acting freely with $E/G = B$ |
| $d = |G|$ | Number of sheets; the degree of the covering |
| $R$ | Commutative ring with identity $1 \neq 0$; coefficient ring |
| $A, E_A$ | Subspace of $B$ and its preimage $p^{-1}(A)$; a covering of pairs |
| $C_n(X;R)$, $\partial_n$ | Singular chains and boundary, as in *Simplicial and Singular Homology* |
| $g_\#$, $g_*$ | Chain map and homology map induced by a deck transformation $g$ |
| $\tau_n$, $\tau_*$ | Transfer on chains and on homology: $\tau_n(\sigma) = \sum_{g \in G} g_\# \tilde\sigma$ |
| $N = \sum_{g \in G} g_\#$ | Norm (symmetrisation) operator; $N^2 = dN$ |
| $M^G$, $M_G$ | Invariant and coinvariant parts of a complex of $R[G]$-modules |
| $\tau^*$ | Cohomology transfer, the dual of $\tau_*$; adjoint under the evaluation pairing |
| $p_*$, $p^*$ | Projection on homology; pullback on cohomology |
| $\tilde H_n$ | Reduced homology; the transfer preserves the augmentation |
| $p_*\tau_* = d$, $\tau_* p_* = \sum_g g_*$ | The two composite laws; the composition with the projection |
| $\partial$ | Boundary operator and connecting homomorphism of a pair; $\partial\tau = \tau\partial$ |

## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the transfer of a covering and the fixed-point formula $H_*(B) \cong H_*(E)^G$ over a field of characteristic zero.
- Glen E. Bredon, *Topology and Geometry* (Springer, 1993), for the transfer, the Euler class and the relation to Smith theory.
- Edwin H. Spanier, *Algebraic Topology* (McGraw–Hill, 1966), for the transfer in singular theory with arbitrary coefficients and its naturality.
- James R. Munkres, *Elements of Algebraic Topology* (Addison-Wesley, 1984), for the transfer as a chain map and its behaviour on the exact sequences of a pair.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for the invariant and coinvariant complexes, the norm operator and the averaging argument over a ring in which the group order is invertible.
