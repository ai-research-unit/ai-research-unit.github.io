
# __The Dual Pairing and the Adjoint__

## Introduction

A dual pairing $\langle E, F\rangle$ turns a weakly continuous operator $T$ of $E$ into a second operator $T^{*}$ of $F$, the **adjoint**, by moving $T$ from one side of the pairing to the other, $\langle Tx, y\rangle = \langle x, T^{*}y\rangle$, and the article is about that operator and its relation to the **transpose**. The two operations are different bookkeeping for one map: the transpose $T'$ always exists on the dual, being defined by composition, while the adjoint $T^{*}$ requires the pairing to identify the second space with the dual, and the identification is available precisely in the reflexive case, where the adjoint becomes the transpose brought back by the canonical embedding. For a Hilbert space the pairing is the inner product, the adjoint is the Hilbert adjoint of *The Adjoint of a Bounded Operator*, and the Riesz map is the identification that makes the two agree; for a reflexive Banach space it is the canonical identification of $E$ with $E''$.

This article develops the adjoint defined by a dual pairing and its identification with the transpose. The dual pairs, the weak topologies, the polar calculus and the reflexivity are *Duality Theory*; the transpose and its weak-star continuity are *The Dual Operator* and *The Dual Operator and the Weak Topology*; the transpose of an involution is *The Involution and the Dual Pairing*; the Hilbert adjoint is *The Adjoint of a Bounded Operator*; the involutions of $B(H)$ are *Involutions of the Bounded Operators*. No form, no norm for its own sake and no spectral theory is used.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $(E, F)$ is a dual pair over $\mathbb{K}$ with pairing $\langle\cdot,\cdot\rangle$, $\mathcal{L}(E)$ is the algebra of continuous operators and $\mathcal{L}_{\sigma}(E)$ the algebra of weakly continuous ones, $\sigma(E,F)$ is the weak topology, $T' : F' \to E'$ is the transpose and $\iota_{E} : E \to E''$ the canonical embedding.

## The Adjoint of a Weakly Continuous Operator

**Definition.** For $T \in \mathcal{L}_{\sigma}(E)$ the **adjoint** is the operator $T^{*} \in \mathcal{L}_{\sigma}(F)$ with

$$
\langle Tx, y\rangle = \langle x, T^{*}y\rangle \qquad (x \in E, \ y \in F).
$$

**Theorem (existence and uniqueness).** Every weakly continuous $T$ has a unique adjoint $T^{*}$; the assignment $T \mapsto T^{*}$ is linear, reverses composition, $(ST)^{*} = T^{*}S^{*}$, fixes the identity, and is an algebra anti-isomorphism

$$
\mathcal{L}_{\sigma}(E) \longrightarrow \mathcal{L}_{\sigma}(F) .
$$

**Proof.** For fixed $y \in F$ the functional $x \mapsto \langle Tx, y\rangle$ is continuous for $\sigma(E,F)$, because $T$ is, so it is $\langle x, y^{*}\rangle$ for a unique $y^{*} \in F$ by the non-degeneracy of the pairing; set $T^{*}y = y^{*}$. Linearity in $y$ is the bilinearity of the pairing, continuity of $T^{*}$ for $\sigma(F,E)$ is the same computation with the roles exchanged, and the composition rule is $\langle STx, y\rangle = \langle Tx, S^{*}y\rangle = \langle x, T^{*}S^{*}y\rangle$.

**Proposition (the adjoint preserves the annihilator calculus).** For $T \in \mathcal{L}_{\sigma}(E)$,

$$
\ker T^{*} = (\mathrm{im}\,T)^{\circ}, \qquad \overline{\mathrm{im}\,T^{*}} = (\ker T)^{\circ} ,
$$

the closures being in the weak topology; in particular $T$ is injective exactly when $T^{*}$ has dense image and $T^{*}$ is injective exactly when $T$ has dense image.

**Proof.** $y \in \ker T^{*}$ means $\langle Tx, y\rangle = 0$ for all $x$, which is the definition of the annihilator of the image; the second identity is the first applied to $T^{*}$ together with the bipolar theorem of *Duality Theory*, and injectivity is the vanishing of the kernel.

## The Two Adjoints and the Transpose

**Theorem (the adjoint is the transpose read through the duality).** Let $E$ be reflexive and let $T \in \mathcal{L}(E)$. Then the transpose $T'' = (T')'$ acts on $E'' = E$ and equals the adjoint of $T$ with respect to the canonical pairing $\langle E, E'\rangle$:

$$
\iota_{E}\,T^{*} = T''\,\iota_{E}, \qquad T^{*} = \iota_{E}^{-1}T''\iota_{E} .
$$

Consequently the adjoint of $T$ with respect to the canonical pairing exists, is the double transpose under the identification, and is denoted by the same symbol $T^{*}$; for a general dual pair which is not the canonical one, the adjoint exists exactly when $T$ is weakly continuous.

**Proof.** For $x \in E$ and $y' \in E'$, $\langle T''\iota_{E}x, y'\rangle = \langle \iota_{E}x, T'y'\rangle = \langle x, T'y'\rangle = \langle Tx, y'\rangle = \langle \iota_{E}Tx, y'\rangle$, so $T''\iota_{E} = \iota_{E}T$; under the identification $E'' = E$ of reflexivity the left side is the transpose of $T$, and the adjoint with respect to the canonical pairing is $T^{*}$.

**Corollary (the transpose always exists, the adjoint needs reflexivity).** The transpose $T'$ is defined for every continuous $T$ and is an anti-homomorphism on the dual, while the adjoint $T^{*}$ on the space itself requires the identification of the space with its dual, which is the reflexivity; for a non-reflexive space the adjoint of a general continuous operator is defined only on the weakly continuous part and not by transposition alone.

**Proof.** The transpose is *The Dual Operator*; the adjoint is the theorem above, and the failure for a general continuous operator is the failure of the inclusion $\mathcal{L}(E) \subseteq \mathcal{L}_{\sigma}(E)$ in the non-reflexive case.

**Theorem (the two adjoints of a Hilbert-space operator).** Let $H$ be a Hilbert space and $R : H \to H'$ the Riesz map. Then the pairing adjoint with respect to the duality $\langle H, H'\rangle$ of the operator $T \in B(H)$ is the transpose, and the Hilbert adjoint of *The Adjoint of a Bounded Operator* is the pairing adjoint read on $H$,

$$
T^{*} = R^{-1}\,T'\,R ,
$$

so the Hilbert adjoint, the pairing adjoint and the double transpose are one operator under the Riesz identification; the identifications are natural and the involution is the same.

**Proof.** This is the Riesz-transpose identity of *The Adjoint of a Bounded Operator*; the pairing adjoint and the transpose coincide under the identification, and the Hilbert adjoint is the composite.

## Reflexive Cases and Duality of the Algebra

**Theorem (the double adjoint).** For $T \in \mathcal{L}_{\sigma}(E)$ the double adjoint $T^{**}$ acts on $E$ and equals $T$, so that

$$
(T^{*})^{*} = T ,
$$

and the adjoint operation is an involution exchanging the two sides, $\mathcal{L}_{\sigma}(E) \to \mathcal{L}_{\sigma}(F)$.

**Proof.** Read the pairing in the other order, $\langle y, x\rangle_{F,E} = \langle x, y\rangle_{E,F}$; then $T^{*}$ is defined by $\langle T^{*}y, x\rangle = \langle y, Tx\rangle$, so the adjoint of $T^{*}$ satisfies $\langle T^{*}y, x\rangle = \langle y, T^{**}x\rangle$ and hence $\langle y, Tx\rangle = \langle y, T^{**}x\rangle$ for all $y \in F$. Non-degeneracy gives $T^{**}x = Tx$ for every $x$, and $T^{**} = T$.

**Corollary (the commutant duality).** The adjoint exchanges the commutants, $\{T\}'^{*} = \{T^{*}\}'$, and an algebra $\mathcal{A} \subseteq \mathcal{L}_{\sigma}(E)$ is closed under the adjoint exactly when its commutant is; in the Hilbert case this is the self-adjointness of the commutant of a self-adjoint algebra, which is *Operator Algebras*.

**Proof.** $S$ commutes with $T$ iff $\langle STx, y\rangle = \langle TSx, y\rangle$ for all $x, y$, which by the definition of the adjoints is $S^{*}$ commuting with $T^{*}$; the Hilbert statement is the special case.

**Proposition (the pairing adjoint for an involution).** If the dual pair carries a $\varsigma$-semilinear involution $\theta$ of $E$, then the adjoint of $\theta$ with respect to the pairing is the transposed involution $\theta^{t}$ of *The Involution and the Dual Pairing*, of the same kind, and the adjoint of a weakly continuous operator that commutes with $\theta$ commutes with $\theta^{t}$; the pairing-adjoint operation and the transposed involution are compatible.

**Proof.** The defining relations $\langle\theta x, y\rangle = \varsigma(\langle x, \theta^{t}y\rangle)$ and $\langle\theta x, y\rangle = \langle x, \theta^{*}y\rangle$ agree, so $\theta^{*} = \theta^{t}$ up to the scalar involution; compatibility with the commuting is the commutant duality.

## Examples

**Example (the sequence spaces).** On the dual pair $(\ell^{p}, \ell^{q})$ with $1 < p,q < \infty$ and $1/p+1/q = 1$, an operator with matrix $(a_{ij})$ that acts continuously on both spaces has the transpose with matrix $(a_{ji})$; for $p = q = 2$ the pairing is the inner product and the adjoint is the conjugate transpose, the operator and its adjoint differing by the conjugation of the matrix entries.

**Example (the reflexive Banach space).** For a reflexive Banach space $E$ and $T \in \mathcal{L}(E)$ the adjoint is the double transpose under the canonical embedding, so the algebra $\mathcal{L}(E)$ is an involutive algebra when $E$ is reflexive and the pairing is the canonical one; in the non-reflexive case $c_{0}$ with dual $\ell^{1}$ and bidual $\ell^{\infty}$ shows that a continuous operator need not be weakly continuous, and then the adjoint is defined on $\ell^{1}$ but not on $c_{0}$ by transposition alone.

**Example (the Hilbert case).** On $H = \ell^{2}$ the Riesz map is the conjugate-linear identification of a sequence with the functional it defines, and the Hilbert adjoint of the unilateral shift is the backward shift; the pairing adjoint with respect to $\langle \ell^{2}, \ell^{2}\rangle$ is the same operator, and the double transpose is the shift again because $\ell^{2}$ is reflexive.

## Summary

For a dual pair $\langle E, F\rangle$ a weakly continuous operator $T$ of $E$ has a unique adjoint $T^{*}$ of $F$, defined by $\langle Tx, y\rangle = \langle x, T^{*}y\rangle$, the assignment being a linear anti-isomorphism $\mathcal{L}_{\sigma}(E) \to \mathcal{L}_{\sigma}(F)$ with $(ST)^{*} = T^{*}S^{*}$ and $T^{**} = T$; the adjoint preserves the annihilator calculus, $\ker T^{*} = (\mathrm{im}\,T)^{\circ}$ and $\overline{\mathrm{im}\,T^{*}} = (\ker T)^{\circ}$, and exchanges the commutants. The transpose $T'$ and the adjoint $T^{*}$ are different bookkeeping for one map: the transpose always exists on the dual, while the adjoint on the space requires the identification of the space with its dual, which is the reflexivity, and for a reflexive space the adjoint is the double transpose under the canonical embedding, $T^{*} = \iota_{E}^{-1}T''\iota_{E}$. For a Hilbert space both adjoints and the transpose are one operator under the Riesz map, $T^{*} = R^{-1}T'R$, in agreement with *The Adjoint of a Bounded Operator*; a transposed involution of the pair is the adjoint of the involution. The sequence spaces, the reflexive and the non-reflexive Banach spaces and the Hilbert case are the standard examples. The involutions of the algebra of bounded operators are *Involutions of the Bounded Operators*, and the one-sided adjoints on a topological algebra are the following articles of this group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle E, F\rangle$ | dual pair over $\mathbb{K}$ |
| $T^{*}$ | adjoint, $\langle Tx,y\rangle = \langle x,T^{*}y\rangle$ |
| $\mathcal{L}_{\sigma}(E)$ | weakly continuous operators |
| $(ST)^{*} = T^{*}S^{*}$, $T^{**} = T$ | anti-homomorphism and involution |
| $\ker T^{*} = (\mathrm{im}T)^{\circ}$ | annihilator calculus |
| $T'$ | transpose on the dual, always defined |
| $T^{*} = \iota_{E}^{-1}T''\iota_{E}$ | adjoint as double transpose in the reflexive case |
| $T^{*} = R^{-1}T'R$ | Hilbert case, Riesz identification |
| $\theta^{t}$ | transposed involution, the adjoint of an involution |

## Further Reading

- Nicolas Bourbaki, *Topological Vector Spaces, Chapters 1–5* (Springer, 1987), for the dual pairs, the weak topologies and the transposed maps.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the Hilbert adjoint, the Riesz map and the reflexive Banach spaces.
- Walter Rudin, *Functional Analysis* (McGraw-Hill, second edition, 1991), for the dual operators, the reflexivity and the adjoint.
- Gottfried Köthe, *Topological Vector Spaces I* and *II* (Springer, 1969 and 1979), for the duality of a pair and the adjoint operators.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the dual pairs, the adjoints and the weak topologies.
