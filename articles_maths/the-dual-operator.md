
# __The Dual Operator__

## Introduction

A continuous linear operator $T : E \to F$ acts on the duals by composition: a continuous functional on $F$, read after $T$, is a continuous functional on $E$. The resulting map $T' : F' \to E'$ is the **transpose**, also called the **dual operator**, and the assignment $T \mapsto T'$ is linear, reverses composition, preserves the operator norm in the normed case, and is characterised by continuity for the weak-star topologies: a linear map of duals is a transpose exactly when it is weak-star continuous. Iterating gives the **double dual** $T''$, and the canonical embeddings intertwine $T$ and $T''$, so that a reflexive space recovers the operator from its transpose.

This article treats the transpose at the level of the duality of locally convex spaces. The weak and the weak-star topologies and the compatibility of an operator with them are the subject of *The Dual Operator and the Weak Topology*; the adjoint defined by a dual pairing, the reflexive cases and the comparison with the Hilbert-space adjoint are *The Dual Pairing and the Adjoint*; the operator involution it induces on the bounded operators is *Involutions of the Bounded Operators*. The duality theory that supplies the dual pairs, the weak-star topology, the polar calculus and the canonical embedding is *Duality Theory*; the operator norm and the completeness of the operator space are *Bounded Operators on a Topological Vector Space* and *Bounded Operators and the Operator Norm*. Nothing analytic and nothing geometric is used.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ and $E, F, G$ are Hausdorff locally convex spaces over $\mathbb{K}$, with duals $E', F', G'$. The **weak-star topology** on a dual is $\sigma(E', E)$ and the **weak topology** on a space is $\sigma(E, E')$; the canonical map into the strong bidual is $\iota_E : E \to (E'_{b})'_{b}$, $\iota_E(x)(x') = x'(x)$. For $T \in \mathcal{L}(E, F)$ the **transpose** is $T' : F' \to E'$ and the **double dual** is $T'' = (T')' : E'' \to F''$.

## The Transpose

**Definition.** For $T \in \mathcal{L}(E, F)$ the **transpose** is the map

$$
T' : F' \longrightarrow E', \qquad (T'y')(x) = y'(Tx) \qquad (y' \in F', \ x \in E),
$$

that is, $T'y' = y' \circ T$.

**Proposition (the transpose is a continuous operator).** For every $T \in \mathcal{L}(E, F)$ the transpose $T'$ is linear and continuous, so $T' \in \mathcal{L}(F', E')$.

**Proof.** Linearity is the linearity of $y'$ and of the composition. For continuity, a basic neighbourhood of $0$ in $E'$ for the topology inherited from the dual pair $\langle E', E\rangle$ is $\{x' : \lvert x'(x)\rvert \leq 1\}$ for $x \in E$; its preimage under $T'$ is $\{y' : \lvert y'(Tx)\rvert \leq 1\}$, a basic neighbourhood of $0$ in $F'$, so $T'$ is continuous at $0$, hence continuous. The statement for the given topology of $E'$ is the definition of the topological dual read with the dual pair; in the locally convex setting the topology of $E'$ is the one of the pairing.

**Proposition (the transpose is linear and reverses composition).** For $S, T \in \mathcal{L}(E, F)$, $R \in \mathcal{L}(F, G)$ and $\lambda \in \mathbb{K}$,

$$
(S + T)' = S' + T', \qquad (\lambda T)' = \lambda T', \qquad (\mathrm{id}_{E})' = \mathrm{id}_{E'}, \qquad (RT)' = T'R' .
$$

Hence $T \mapsto T'$ is a linear map $\mathcal{L}(E, F) \to \mathcal{L}(F', E')$ that is a unital algebra anti-homomorphism $\mathcal{L}(E) \to \mathcal{L}(E')$ on the endomorphisms.

**Proof.** All four are the associativity and the linearity of composition: $((S+T)'y')(x) = y'((S+T)x) = y'(Sx) + y'(Tx)$, and likewise for the scalar; $(\mathrm{id}_{E})'y' = y'$; and $((RT)'z')(x) = z'(RTx) = (T'z')(Rx) = (T'R'z')(x)$.

**Corollary (the transpose is injective and involutive on endomorphisms).** If $T' = 0$ then $T = 0$ when $E'$ separates the points of $F$, which holds when $F$ is locally convex and $T(E)$ is separated; the assignment $T \mapsto T'$ is therefore injective, and $T'' = T$ after the canonical identifications in the reflexive case.

**Proof.** If $T' = 0$ then $y'(Tx) = 0$ for all $y' \in F'$ and all $x$, so $Tx$ lies in the kernel of every continuous functional; on a locally convex space the functionals separate the points, so $Tx = 0$. The reflexive statement is the definition of reflexivity in *Duality Theory*.

## Weak-Star Continuity and the Double Dual

**Theorem (characterisation by weak-star continuity).** Let $R : F' \to E'$ be linear. Then $R$ is continuous for the weak-star topologies, $R : (F', \sigma(F', F)) \to (E', \sigma(E', E))$, if and only if $R = T'$ for a unique $T \in \mathcal{L}(E, F)$. In that case

$$
\langle x, R y'\rangle = \langle Tx, y'\rangle \qquad (x \in E, \ y' \in F').
$$

**Proof.** If $R = T'$ then $\langle x, Ry'\rangle = \langle x, T'y'\rangle = \langle Tx, y'\rangle$, and weak-star continuity follows from the continuity of $T$, as in the proposition above. Conversely, weak-star continuity of $R$ says that for each $x \in E$ the functional $y' \mapsto \langle x, Ry'\rangle$ on $F'$ is weak-star continuous; since the dual of $(F', \sigma(F', F))$ is $F$ for a locally convex $F$, this functional is $\langle Tx, y'\rangle$ for a unique $Tx \in F$, and $x \mapsto Tx$ is linear by the linearity of $R$; that $T$ is continuous follows because it is continuous for the weak topology $\sigma(E, E')$, and a linear map of locally convex spaces is continuous exactly when it is weakly continuous. Uniqueness is the separating property of $F'$.

**Definition and naturality.** The **double dual** of $T \in \mathcal{L}(E, F)$ is $T'' = (T')' : E'' \to F''$. The canonical embeddings intertwine:

$$
T'' \circ \iota_{E} = \iota_{F} \circ T .
$$

**Proof.** For $x \in E$ and $y' \in F'$, $\bigl(T''(\iota_{E}x)\bigr)(y') = (\iota_{E}x)(T'y') = (T'y')(x) = y'(Tx) = (\iota_{F}(Tx))(y')$.

**Corollary (the transpose on the reflexive spaces).** If $E$ and $F$ are reflexive then $\iota_{E}$ and $\iota_{F}$ are topological isomorphisms, and under the identifications $E'' = E$, $F'' = F$ the double dual $T''$ is $T$; the assignment $T \mapsto T'$ is then an involution-compatible bijection between $\mathcal{L}(E, F)$ and $\mathcal{L}(F', E')$.

**Proof.** The naturality identity read through the bijections $\iota_{E}, \iota_{F}$ gives $T'' = \iota_{F}T\iota_{E}^{-1} = T$.

## Norm and Algebra Properties

**Theorem (the transpose is an isometry on normed spaces).** Let $X, Y$ be normed spaces and $T \in B(X, Y)$. Then $T' \in B(Y^{*}, X^{*})$ and

$$
\lVert T'\rVert = \lVert T\rVert .
$$

Hence $T \mapsto T'$ is a linear isometry $B(X, Y) \to B(Y^{*}, X^{*})$, and $T'' = (T')'$ is an isometry extending $T$ under the canonical embeddings.

**Proof.** $\lVert T'y'\rVert = \sup_{\lVert x\rVert \leq 1}\lvert y'(Tx)\rvert \leq \lVert y'\rVert\lVert T\rVert$, so $\lVert T'\rVert \leq \lVert T\rVert$. For the reverse inequality and the existence of the norm, take $x$ with $\lVert x\rVert \leq 1$ and $Tx \neq 0$, and choose by Hahn–Banach $y' \in Y^{*}$ with $\lVert y'\rVert = 1$ and $y'(Tx) = \lVert Tx\rVert$; then $\lvert (T'y')(x)\rvert = \lVert Tx\rVert$, so $\lVert T'\rVert \geq \lVert Tx\rVert$, and taking the supremum over $x$ gives $\lVert T'\rVert \geq \lVert T\rVert$. The extension statement is the naturality identity and the fact that $\iota_{X}$ is isometric.

**Corollary (the transpose of an isometry and of a surjection).** If $T$ is an isometry then $T'$ is a quotient map onto its image in the sense of the norm; if $T$ is surjective then $T'$ is injective; if $T$ has dense range then $T'$ is injective. The adjoint passage sends a topological isomorphism onto a topological isomorphism.

**Proof.** For $T$ surjective, $T'y' = 0$ means $y'$ vanishes on $T(X) = Y$, so $y' = 0$. The dense-range case is the density observation applied to a nonzero $y'$. The isometric case is the equality of norms read with $\lVert Tx\rVert = \lVert x\rVert$.

## Examples

**Example (finite-dimensional matrices).** For $X = \mathbb{K}^{m}$, $Y = \mathbb{K}^{n}$ the transpose of the operator with matrix $A$ has matrix $A^{\mathsf{T}}$ in the dual bases, so the abstract transpose is the transpose of a matrix, and $\lVert A^{\mathsf{T}}\rVert_{\mathrm{op}} = \lVert A\rVert_{\mathrm{op}}$ because the singular values are unchanged.

**Example (the sequence spaces).** On $\ell^{p}$, $1 < p < \infty$, with $(\ell^{p})^{*} = \ell^{q}$ and $1/p + 1/q = 1$, the transpose of the diagonal operator $D_{\varphi}$ is again $D_{\varphi}$, because a diagonal matrix is its own transpose; the transpose of the right shift $R$ on $\ell^{p}$ is the left shift $L$ on $\ell^{q}$, and conversely, since $(Rx)_{k} = x_{k-1}$ dualises to $(R'y)_{k} = y_{k+1}$. On $\ell^{1}$ with dual $\ell^{\infty}$ and on $c_{0}$ with dual $\ell^{1}$ the same formulas hold with the appropriate dual, and the shift transposes are exchanged.

**Example (the transposed functional).** For $T \in \mathcal{L}(E, \mathbb{K}) = E'$ the transpose is the linear map $\mathbb{K} \to E'$, $\lambda \mapsto \lambda T$, so transposition of a functional recovers the functional as a scalar multiple; the zero-dimensional case shows that the transpose is best read on operators between spaces of positive dimension.

## Summary

The transpose of a continuous operator $T \in \mathcal{L}(E, F)$ is the operator $T' \in \mathcal{L}(F', E')$ defined by $(T'y')(x) = y'(Tx)$; the assignment $T \mapsto T'$ is linear, sends the identity to the identity, and reverses composition, $(RT)' = T'R'$, so it is a unital algebra anti-homomorphism $\mathcal{L}(E) \to \mathcal{L}(E')$, and it is injective. A linear map $R : F' \to E'$ is a transpose exactly when it is continuous for the weak-star topologies; equivalently when $\langle x, Ry'\rangle = \langle Tx, y'\rangle$ for some $T \in \mathcal{L}(E, F)$. The double dual $T''$ is intertwined with $T$ by the canonical embeddings, $T''\iota_{E} = \iota_{F}T$, and on reflexive spaces it is $T$ under the identifications. On normed spaces the transpose is an isometry, $\lVert T'\rVert = \lVert T\rVert$, and it is injective when $T$ has dense range; the finite-dimensional, diagonal and shift examples realise the abstract transpose as the transpose of a matrix or the exchange of the two shifts. The weak and weak-star compatibility of the transpose and the adjoint defined by a dual pairing are the subjects of *The Dual Operator and the Weak Topology* and *The Dual Pairing and the Adjoint*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E, F, G$ | Hausdorff locally convex spaces over $\mathbb{K}$ |
| $E'$ | Topological dual of $E$ |
| $T' : F' \to E'$ | Transpose (dual operator), $(T'y')(x) = y'(Tx)$ |
| $(RT)' = T'R'$ | Reversal of composition |
| $\sigma(E', E)$, $\sigma(E, E')$ | Weak-star and weak topologies |
| $\iota_{E} : E \to E''$ | Canonical embedding |
| $T'' = (T')'$ | Double dual, $T''\iota_{E} = \iota_{F}T$ |
| $\lVert T'\rVert = \lVert T\rVert$ | Isometry of the transpose on normed spaces |
| $A^{\mathsf{T}}$ | Transpose of a matrix |

## Further Reading

- Nicolas Bourbaki, *Topological Vector Spaces, Chapters 1–5* (Springer, 1987), for the transpose, the weak-star topology and the duality of a pair.
- Gottfried Köthe, *Topological Vector Spaces I* and *II* (Springer, 1969 and 1979), for the transposed operators and the bidual.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the transpose, its weak-star continuity and the duality of operators.
- Walter Rudin, *Functional Analysis* (McGraw–Hill, second edition, 1991), for the transpose of a bounded operator and the Hahn–Banach isometry $\lVert T'\rVert = \lVert T\rVert$.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the adjoint and transpose of an operator and the double dual.
