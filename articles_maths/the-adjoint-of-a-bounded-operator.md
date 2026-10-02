
# __The Adjoint of a Bounded Operator__

## Introduction

The adjoint of a bounded operator on a Hilbert space is defined by the identity $\langle Tx, y\rangle = \langle x, T^{*}y\rangle$, and the assignment $T \mapsto T^{*}$ is an **isometric involutive anti-automorphism** of the algebra $B(H)$ of bounded operators: it is conjugate-linear, reverses the order of a product, is its own inverse, and preserves the norm, so $B(H)$ is an involutive Banach algebra and the identity $\lVert T^{*}T\rVert = \lVert T\rVert^{2}$ holds. Topologically, the adjoint is continuous for the norm, the weak, the strong and the weak-star topologies, and it is the transpose of $T$ read through the Riesz identification of $H$ with its dual, $T^{*} = R^{-1}T'R$; the spectrum transforms by $\sigma(T^{*}) = \overline{\sigma(T)}$, and on a finite-dimensional space the adjoint is the conjugate transpose of the matrix.

The existence of the adjoint and its basic identities are *Banach and Hilbert Spaces*, which supply the inner product, the Riesz representation theorem, the projection theorem and the bounded operators; the present article develops the operator $T^{*}$ as an element of the involutive algebra $B(H)$, its topological continuity and its identification with the transpose. The transposition of a continuous operator is *The Dual Operator*; the adjoint defined by an abstract pairing is *The Dual Pairing and the Adjoint*; the involutions of $B(H)$ and the classical groups they define are *Involutions of the Bounded Operators*; the abstract involutive Banach algebras are *Involutive Banach Algebras and the Gelfand–Naimark Theorem*. The forms and the indefinite adjoints are Part III, and no analysis is used beyond the inner product.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ and $H$ is a Hilbert space over $\mathbb{K}$ with inner product $\langle\cdot,\cdot\rangle$ linear in the first argument, norm $\lVert\cdot\rVert$ and dual $H'$; the **Riesz map** is $R : H \to H'$, $(Ry)(x) = \langle x, y\rangle$, a conjugate-linear isometric isomorphism; $B(H)$ is the algebra of bounded operators with the operator norm; and $T' : H' \to H'$ is the transpose of $T$.

## The Adjoint as an Involution of the Operator Algebra

**Theorem (existence and the defining properties).** For every $T \in B(H)$ there is a unique $T^{*} \in B(H)$ with

$$
\langle Tx, y\rangle = \langle x, T^{*}y\rangle \qquad (x, y \in H),
$$

and $\lVert T^{*}\rVert = \lVert T\rVert$, $(S+T)^{*} = S^{*}+T^{*}$, $(\lambda T)^{*} = \overline{\lambda}T^{*}$, $(\mathrm{id})^{*} = \mathrm{id}$ and $T^{**} = T$.

**Proof.** The existence, the uniqueness, the norm equality and the algebraic identities are established in *Banach and Hilbert Spaces* from the Riesz representation theorem; they are quoted here and not reproved.

**Theorem (the anti-automorphism).** For all $S, T \in B(H)$,

$$
(ST)^{*} = T^{*}S^{*} ,
$$

so $T \mapsto T^{*}$ is an involutive anti-automorphism of $B(H)$: it reverses products, is conjugate-linear, is its own inverse, and fixes the identity. Consequently $B(H)$ is an involutive Banach algebra, and the adjoint is isometric.

**Proof.** For $x, y \in H$, $\langle STx, y\rangle = \langle Tx, S^{*}y\rangle = \langle x, T^{*}S^{*}y\rangle$, and the uniqueness of the adjoint gives $(ST)^{*} = T^{*}S^{*}$; the remaining statements are the theorem above.

**Proposition (the $C^{*}$-identity).** For every $T \in B(H)$,

$$
\lVert T^{*}T\rVert = \lVert T\rVert^{2} ,
$$

and this identity exhibits $B(H)$ as a $C^{*}$-algebra for the adjoint involution.

**Proof.** For $\lVert x\rVert \leq 1$, $\lVert Tx\rVert^{2} = \langle Tx,Tx\rangle = \langle T^{*}Tx,x\rangle \leq \lVert T^{*}T\rVert\lVert x\rVert^{2}$, so $\lVert T\rVert^{2} \leq \lVert T^{*}T\rVert$; the reverse inequality is the submultiplicativity $\lVert T^{*}T\rVert \leq \lVert T^{*}\rVert\lVert T\rVert = \lVert T\rVert^{2}$. The abstract theory of the $C^{*}$-algebras that the identity defines is *Involutive Banach Algebras and the Gelfand–Naimark Theorem* and *Operator Algebras*, named here and not developed.

**Theorem (the adjoint is the transpose through Riesz).** With $R$ the Riesz map,

$$
T^{*} = R^{-1}\,T'\,R ,
$$

so the Hilbert adjoint is the transpose of *The Dual Operator* conjugated by the Riesz identification; consequently $T \mapsto T^{*}$ is the transpose read on $H$ and inherits the reversal of composition and, in the reflexive case, the symmetry $T^{**} = T$.

**Proof.** For $y \in H$ and $x \in H$, $(R^{-1}T'R\,y)(x) = R^{-1}(T'Ry)(x) = (T'Ry)(x) = (Ry)(Tx) = \langle Tx, y\rangle = \langle x, T^{*}y\rangle = (R T^{*} y)(x)$, so $R^{-1}T'Ry = T^{*}y$. The reversal and the symmetry are the corresponding properties of the transpose.

## Topological Continuity of the Adjoint

**Theorem (continuity for the operator topologies).** The involution $T \mapsto T^{*}$ of $B(H)$ is continuous, and in fact a homeomorphism, for the norm topology, the weak operator topology, the strong operator topology and the weak-star (ultraweak) topology; it is isometric for the norm.

**Proof.** Norm continuity and isometry are the theorem above. For the weak operator topology, the seminorms are $T \mapsto \lvert\langle Tx,y\rangle\rvert$, and $\lvert\langle T^{*}x,y\rangle\rvert = \lvert\langle x,Ty\rangle\rvert$ shows that the seminorms of $T^{*}$ are those of $T$ with the arguments exchanged; hence the involution is a homeomorphism. The strong operator topology is handled by $\lVert T^{*}x\rVert = \sup_{\lVert y\rVert\leq1}\lvert\langle T^{*}x,y\rangle\rvert = \sup_{\lVert y\rVert\leq1}\lvert\langle x,Ty\rangle\rvert$; the ultraweak topology is the weak-star topology on $B(H)$ as the dual of the trace-class operators, and the involution on the predual is the transpose of *The Dual Operator and the Weak Topology*, so it is continuous.

**Corollary (commutants and bicommutants).** The adjoint preserves the commutant, $T \in \{S\}' \Rightarrow T^{*} \in \{S\}'$ when $S$ is self-adjoint, and in general $\{S\}^{*} = \{S^{*}\}'$; hence a self-adjoint set of operators has a self-adjoint commutant, and the von Neumann bicommutant theorem applies to the self-adjoint algebras, which are owned by *Operator Algebras*.

**Proof.** If $TS = ST$ then $S^{*}T^{*} = (TS)^{*} = (ST)^{*} = T^{*}S^{*}$, so $T^{*}$ commutes with $S^{*}$; for self-adjoint $S$ this gives $T^{*} \in \{S\}'$, and the general identity follows by applying it to $S^{*}$.

## Spectral and Finite-Dimensional Properties

**Proposition (the spectrum transforms by conjugation).** For $T \in B(H)$,

$$
\sigma(T^{*}) = \overline{\sigma(T)} ,
$$

and $T$ is invertible exactly when $T^{*}$ is, with $(T^{-1})^{*} = (T^{*})^{-1}$; the involution therefore preserves invertibility and the unitary group.

**Proof.** $T - \lambda \mathrm{id}$ is invertible with bounded inverse exactly when its adjoint $T^{*} - \overline{\lambda}\,\mathrm{id}$ is, because the adjoint of an invertible operator is invertible with adjoint inverse; hence $\lambda \in \rho(T)$ iff $\overline{\lambda} \in \rho(T^{*})$. The inverse formula follows by taking adjoints in $T T^{-1} = \mathrm{id}$.

**Proposition (self-adjoint, skew, normal, unitary).** The involution splits $B(H)$ into the **self-adjoint** operators $T = T^{*}$ and the **skew-adjoint** operators $T = -T^{*}$, with

$$
B(H) = B(H)^{\mathrm{sa}} \oplus B(H)^{\mathrm{skew}} , \qquad T = \tfrac12(T+T^{*}) + \tfrac12(T-T^{*}) ,
$$

when $2$ is invertible; $T$ is **normal** when $TT^{*} = T^{*}T$ and **unitary** when $T^{*}T = TT^{*} = \mathrm{id}$. The self-adjoint and skew-adjoint parts are real vector subspaces, and the unitary operators form a group.

**Proof.** The averaging maps $\tfrac12(\mathrm{id}\pm\ast)$ are real-linear idempotents with the stated images, and the direct sum is the abstract decomposition of an involutive algebra; the unitary operators are closed under multiplication and inversion by the anti-automorphism property.

**Example (the finite-dimensional case).** For $H = \mathbb{K}^{n}$ with the standard inner product and $A$ the matrix of $T$ in the standard basis, the matrix of $T^{*}$ is the conjugate transpose $A^{*} = \overline{A}^{\mathsf{T}}$, the self-adjoint operators are the Hermitian matrices (symmetric in the real case), the unitary operators are the unitary matrices (orthogonal in the real case), and the $C^{*}$-identity is $\lVert A^{*}A\rVert = \lVert A\rVert^{2}$ for the spectral norm. The transpose through Riesz is the identity of the finite-dimensional duality $(\mathbb{K}^{n})' = \mathbb{K}^{n}$ up to the conjugate structure.

**Example (the sequence space).** On $H = \ell^{2}$ the adjoint of a bounded operator with matrix $(a_{ij})$ has matrix $(a_{ji}^{*})$; the unilateral shift has the backward shift as its adjoint, the shift being an isometry with $S^{*}S = \mathrm{id}$ and $SS^{*}$ the projection onto the closed span of the coordinate vectors $e_{2}, e_{3}, \dots$, a proper projection, so the shift is not unitary.

**Example (the multiplication operators).** On $H = L^{2}(\mu)$ the multiplication $M_{f}$ by an essentially bounded function $f$ has adjoint $M_{\bar f}$, the involution acting by conjugation of the symbol; $M_{f}$ is self-adjoint exactly when $f$ is real almost everywhere, unitary exactly when $\lvert f\rvert = 1$ almost everywhere, and normal always, the multiplication operators being the model commutative self-adjoint algebra.

## Summary

For a bounded operator $T$ on a Hilbert space there is a unique $T^{*}$ with $\langle Tx,y\rangle = \langle x,T^{*}y\rangle$, of the same norm, and the assignment $T \mapsto T^{*}$ is an isometric involutive anti-automorphism of $B(H)$, satisfying $(ST)^{*} = T^{*}S^{*}$, $T^{**} = T$ and the $C^{*}$-identity $\lVert T^{*}T\rVert = \lVert T\rVert^{2}$; it is the transpose of $T$ conjugated by the Riesz map, $T^{*} = R^{-1}T'R$. The involution is a homeomorphism for the norm, weak, strong and weak-star topologies of $B(H)$, it preserves commutants of self-adjoint sets, it sends the spectrum to the conjugate spectrum, $\sigma(T^{*}) = \overline{\sigma(T)}$, and it implements the splitting of $B(H)$ into the self-adjoint and the skew-adjoint operators, with the normal and the unitary operators defined by the involutive identities. In finite dimension the involution is the conjugate transpose of the matrix. The abstract involutions of $B(H)$ and the classical groups they define are *Involutions of the Bounded Operators*, and the adjoint defined by an abstract pairing is *The Dual Pairing and the Adjoint*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H$, $\langle\cdot,\cdot\rangle$ | Hilbert space and its inner product |
| $B(H)$ | bounded operators, an involutive Banach algebra |
| $T^{*}$ | adjoint, $\langle Tx,y\rangle = \langle x,T^{*}y\rangle$ |
| $(ST)^{*} = T^{*}S^{*}$ | reversing of products |
| $\lVert T^{*}T\rVert = \lVert T\rVert^{2}$ | the $C^{*}$-identity |
| $R : H \to H'$ | Riesz map, $T^{*} = R^{-1}T'R$ |
| $\sigma(T^{*}) = \overline{\sigma(T)}$ | conjugation of the spectrum |
| $B(H)^{\mathrm{sa}}$, $B(H)^{\mathrm{skew}}$ | self-adjoint and skew-adjoint operators |
| $T^{*}T = TT^{*} = \mathrm{id}$ | unitary operators |

## Further Reading

- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, second edition, 1982), for the adjoint, the operator topologies and the unilateral shift.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the Hilbert-space adjoint, the weak and strong operator topologies and the spectral theory.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the involutive algebra $B(H)$, its topologies and the commutant.
- Walter Rudin, *Functional Analysis* (McGraw-Hill, second edition, 1991), for the Riesz representation theorem, the adjoint and the weak-star topology.
- Gert K. Pedersen, *Analysis Now* (Springer, 1989), for the $C^{*}$-identity, the involutive Banach algebras and the adjoint.
