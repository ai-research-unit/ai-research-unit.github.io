
# __Structure of Lie Algebras__

## Introduction

The companion article *Lie Algebras* introduces Lie algebras, the Jacobi identity, and the vocabulary of solvable, nilpotent and simple algebras. This article develops the structure theory that organises that vocabulary: the radical, the nilradical, the Killing form, and the two criteria of Cartan, which decide solvability and semisimplicity from a single bilinear form. The theory culminates in the Levi decomposition, which writes every finite-dimensional Lie algebra over a field of characteristic zero as a semidirect product of a semisimple algebra by a solvable one, and in the theorem that a semisimple algebra is a direct sum of simple ideals. Together with the classification of simple algebras by root systems, this is the structure theory of Lie algebras.

The theory is carried out over a field $K$ of characteristic zero; this is the setting in which the classical results hold cleanly, and where a result needs more than that — an algebraically closed field, or the finite dimension of the algebra — this is stated explicitly. Lie algebras are written in lowercase fraktur, so $\mathrm{G}$, $\mathrm{H}$ are Lie algebras, $\mathrm{I}$ is an ideal, $\mathrm{R}$ the radical, $\mathrm{N}$ the nilradical, and $\mathrm{Z}(\mathrm{G})$ the centre; the field is $K$, and $R$ is reserved for the commutative-ring statements of the earlier articles. No physics is invoked.

The general facts about Lie algebras used below — the definition, the Jacobi identity, ideals, quotients, homomorphisms, the centre, the derived subalgebra, and the elementary properties of solvable and nilpotent algebras — are assumed from *Lie Algebras*, and the representation-theoretic notions are developed further.

## Recapitulation and the Radical

### Ideals, Quotients and Homomorphisms

A **Lie algebra** over $K$ is a $K$-vector space $\mathrm{G}$ with a bilinear, alternating bracket $[\cdot, \cdot] : \mathrm{G} \times \mathrm{G} \to \mathrm{G}$ satisfying the Jacobi identity

$$
[x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0.
$$

The centre of $\mathrm{G}$ is

$$
\mathrm{Z}(\mathrm{G}) = \{x \in \mathrm{G} : [x, y] = 0 \text{ for all } y \in \mathrm{G}\},
$$

and the derived subalgebra is $[\mathrm{G}, \mathrm{G}] = \operatorname{span}\{[x, y] : x, y \in \mathrm{G}\}$. A subspace $\mathrm{I} \subseteq \mathrm{G}$ is an **ideal** if $[\mathrm{G}, \mathrm{I}] \subseteq \mathrm{I}$; the centre and the derived subalgebra are ideals, and the quotient $\mathrm{G}/\mathrm{I}$ inherits a bracket. A linear map $\varphi : \mathrm{G} \to \mathrm{H}$ is a **homomorphism** if $\varphi([x, y]) = [\varphi(x), \varphi(y)]$; its kernel is an ideal and its image is a subalgebra, and the first isomorphism theorem holds. All of this is the content of *Lie Algebras*.

Recall also that the bracket of ideals is an ideal, so the derived subalgebra of an ideal is again an ideal; iterating this observation produces the derived series below.

### Solvable and Nilpotent Algebras

**Definition.** The **derived series** of $\mathrm{G}$ is

$$
\mathrm{G}^{(0)} = \mathrm{G}, \qquad \mathrm{G}^{(k+1)} = [\mathrm{G}^{(k)}, \mathrm{G}^{(k)}],
$$

and the **lower central series** is

$$
\mathrm{G}_0 = \mathrm{G}, \qquad \mathrm{G}_{k+1} = [\mathrm{G}, \mathrm{G}_k].
$$

The algebra $\mathrm{G}$ is **solvable** if $\mathrm{G}^{(k)} = 0$ for some $k$, and **nilpotent** if $\mathrm{G}_k = 0$ for some $k$. The least such $k$ is the **derived length**, respectively the **nilpotency class**.

**Proposition.** Every nilpotent Lie algebra is solvable, but not conversely. Subalgebras and quotients of solvable algebras are solvable, and the same holds for nilpotent algebras.

**Proof.** $\mathrm{G}^{(k)} \subseteq \mathrm{G}_k$ by induction, so nilpotency implies solvability. The two-dimensional nonabelian Lie algebra with basis $x, y$ and $[x, y] = x$ is solvable, since $[\mathrm{G}, \mathrm{G}] = \langle x\rangle$ is abelian, but it is not nilpotent, since $\mathrm{G}_k = \langle x\rangle$ for all $k \geq 1$. The claims about subalgebras and quotients follow from the definitions.

**Proposition.** Let $\mathrm{I}$ be an ideal of $\mathrm{G}$. If $\mathrm{I}$ and $\mathrm{G}/\mathrm{I}$ are solvable, then so is $\mathrm{G}$; the analogous statement holds for nilpotency. Consequently the sum of two solvable ideals is solvable, and the sum of two nilpotent ideals is nilpotent.

**Proof.** If $\mathrm{G}/\mathrm{I}$ is solvable, then $\mathrm{G}^{(k)} \subseteq \mathrm{I}$ for some $k$; if $\mathrm{I}$ is solvable, then $\mathrm{I}^{(l)} = 0$ for some $l$, and since $\mathrm{I}$ is an ideal the derived series of $\mathrm{G}$ satisfies $\mathrm{G}^{(k+l)} \subseteq \mathrm{I}^{(l)} = 0$. For nilpotency the argument is the same with the lower central series: the ideal property gives $\mathrm{G}_{k+l} \subseteq \mathrm{I}_l$. For the sums, note that $(\mathrm{I} + \mathrm{A})/\mathrm{A} \cong \mathrm{I}/(\mathrm{I} \cap \mathrm{A})$ is solvable, and apply the extension statement.

### The Radical and the Nilradical

**Definition.** Because the sum of solvable ideals is solvable, the solvable ideals of $\mathrm{G}$ have a largest element, the **radical**

$$
\mathrm{R}(\mathrm{G}) = \sum_{\mathrm{A} \text{ solvable ideal}} \mathrm{A}.
$$

It is a solvable ideal containing every solvable ideal. Similarly the **nilradical** $\mathrm{N}(\mathrm{G})$ is the largest nilpotent ideal, and it is contained in the radical.

**Definition.** The Lie algebra $\mathrm{G}$ is **semisimple** if $\mathrm{R}(\mathrm{G}) = 0$, equivalently if it has no nonzero solvable ideal; it is **simple** if it is nonabelian and has no nonzero proper ideal; and it is **reductive** if $\mathrm{R}(\mathrm{G}) = \mathrm{Z}(\mathrm{G})$.

**Proposition.** $\mathrm{G}$ is semisimple if and only if it has no nonzero abelian ideal. In particular every simple Lie algebra is semisimple, and the semisimple algebras are exactly the direct sums of simple algebras.

**Proof.** If $\mathrm{G}$ has a nonzero solvable ideal $\mathrm{A} \neq 0$, then the last nonzero term of its derived series is a nonzero abelian ideal of $\mathrm{G}$, because it is a characteristic ideal of $\mathrm{A}$ and $\mathrm{A}$ is an ideal. Conversely a nonzero abelian ideal is solvable, so its presence contradicts semisimplicity. The remaining statements follow from the decomposition theorem proved below.

## The Adjoint Representation and Derivations

### The Adjoint Map

**Definition.** For $x \in \mathrm{G}$ the **adjoint map** is $\operatorname{ad}_x : \mathrm{G} \to \mathrm{G}$, $\operatorname{ad}_x(y) = [x, y]$. The Jacobi identity is equivalent to

$$
\operatorname{ad}_x([y, z]) = [\operatorname{ad}_x(y), z] + [y, \operatorname{ad}_x(z)],
$$

so each $\operatorname{ad}_x$ is a derivation of the bracket, and

$$
\operatorname{ad}_{[x, y]} = [\operatorname{ad}_x, \operatorname{ad}_y].
$$

Hence $\operatorname{ad} : \mathrm{G} \to \mathrm{GL}(\mathrm{G})$ is a Lie algebra homomorphism, the **adjoint representation**, whose kernel is the centre:

$$
\ker(\operatorname{ad}) = \mathrm{Z}(\mathrm{G}), \qquad \operatorname{ad}(\mathrm{G}) \cong \mathrm{G}/\mathrm{Z}(\mathrm{G}).
$$

### Derivations of a Lie Algebra

**Definition.** A **derivation** of $\mathrm{G}$ is a linear map $D : \mathrm{G} \to \mathrm{G}$ satisfying the Leibniz rule with respect to the bracket,

$$
D([x, y]) = [D(x), y] + [x, D(y)].
$$

The derivations form a Lie algebra $\operatorname{Der}(\mathrm{G})$ under the commutator $[D_1, D_2] = D_1 D_2 - D_2 D_1$; the **inner derivations** are those of the form $\operatorname{ad}_x$, and they form the subspace $\operatorname{Inn}(\mathrm{G}) = \operatorname{ad}(\mathrm{G})$.

**Proposition.** $\operatorname{Inn}(\mathrm{G})$ is an ideal of $\operatorname{Der}(\mathrm{G})$, and the quotient $\operatorname{Out}(\mathrm{G}) = \operatorname{Der}(\mathrm{G})/\operatorname{Inn}(\mathrm{G})$ is the Lie algebra of **outer derivations**. For a semisimple $\mathrm{G}$ over a field of characteristic zero, $\operatorname{Der}(\mathrm{G}) = \operatorname{Inn}(\mathrm{G})$; every derivation is inner.

**Proof.** For $D \in \operatorname{Der}(\mathrm{G})$ and $x \in \mathrm{G}$ one computes

$$
[D, \operatorname{ad}_x](y) = D([x, y]) - [x, D(y)] = [D(x), y] = \operatorname{ad}_{D(x)}(y),
$$

so $[D, \operatorname{ad}_x] = \operatorname{ad}_{D(x)} \in \operatorname{Inn}(\mathrm{G})$, which is the ideal property. The vanishing of $\operatorname{Out}(\mathrm{G})$ for semisimple algebras is a standard theorem of the structure theory, proved by showing that a derivation orthogonal to the inner ones annihilates the Killing form and hence vanishes; the result is the infinitesimal form of the statement that the automorphism group of a semisimple algebra has Lie algebra $\operatorname{Der}(\mathrm{G}) = \mathrm{G}$.

## The Killing Form

### Definition and Symmetry

**Definition.** The **Killing form** of a finite-dimensional Lie algebra $\mathrm{G}$ is the bilinear form

$$
\kappa(x, y) = \operatorname{tr}\bigl(\operatorname{ad}_x \circ \operatorname{ad}_y\bigr), \qquad x, y \in \mathrm{G}.
$$

**Proposition.** $\kappa$ is a symmetric bilinear form on $\mathrm{G}$, and it is **invariant** in the sense that

$$
\kappa([x, y], z) = \kappa(x, [y, z])
$$

for all $x, y, z \in \mathrm{G}$; equivalently, $\kappa(\operatorname{ad}_y(x), z) + \kappa(x, \operatorname{ad}_y(z)) = 0$.

**Proof.** Bilinearity is immediate, and symmetry follows from the trace identity $\operatorname{tr}(AB) = \operatorname{tr}(BA)$. For invariance, use the identity $\operatorname{ad}_{[x,y]} = [\operatorname{ad}_x, \operatorname{ad}_y]$ and the trace identity $\operatorname{tr}([A, B]C) = \operatorname{tr}(A[B, C])$:

$$
\kappa([x, y], z) = \operatorname{tr}(\operatorname{ad}_{[x,y]}\operatorname{ad}_z) = \operatorname{tr}([\operatorname{ad}_x, \operatorname{ad}_y]\operatorname{ad}_z) = \operatorname{tr}(\operatorname{ad}_x[\operatorname{ad}_y, \operatorname{ad}_z]) = \operatorname{tr}(\operatorname{ad}_x \operatorname{ad}_{[y,z]}) = \kappa(x, [y, z]).
$$

**Corollary.** Every algebra automorphism of $\mathrm{G}$ preserves $\kappa$, and every derivation of $\mathrm{G}$ is skew with respect to $\kappa$: $\kappa(D(x), y) + \kappa(x, D(y)) = 0$.

### The Radical of the Killing Form

**Definition.** The **radical** of $\kappa$ is

$$
\mathrm{G}^{\perp} = \{x \in \mathrm{G} : \kappa(x, y) = 0 \text{ for all } y \in \mathrm{G}\},
$$

and $\kappa$ is **nondegenerate** if $\mathrm{G}^{\perp} = 0$.

**Proposition.** $\mathrm{G}^{\perp}$ is an ideal of $\mathrm{G}$. The form $\kappa$ is nondegenerate if and only if the pairing $\mathrm{G} \times \mathrm{G} \to K$ it induces identifies $\mathrm{G}$ with its dual $\mathrm{G}^*$.

**Proof.** If $x \in \mathrm{G}^{\perp}$ then for all $y, z$ invariance gives $\kappa([x, y], z) = \kappa(x, [y, z]) = 0$, so $[x, y] \in \mathrm{G}^{\perp}$; hence $\mathrm{G}^{\perp}$ is an ideal. The second statement is the definition of nondegeneracy for a bilinear form.

## Cartan's Criteria

### Cartan's Criterion for Solvability

**Theorem (Cartan's criterion for solvability).** Let $\mathrm{G}$ be a finite-dimensional Lie algebra over a field of characteristic zero. Then $\mathrm{G}$ is solvable if and only if

$$
\kappa(\mathrm{G}, [\mathrm{G}, \mathrm{G}]) = 0,
$$

that is, $\kappa(x, y) = 0$ for all $x \in \mathrm{G}$ and all $y \in [\mathrm{G}, \mathrm{G}]$.

**Proof sketch.** If $\mathrm{G}$ is solvable, then over an algebraic closure of $K$ the algebra $\mathrm{G}$ is isomorphic to a subalgebra of the upper triangular matrices by Lie's theorem, so each $\operatorname{ad}_x$ is upper triangular and each commutator $\operatorname{ad}_y$ with $y \in [\mathrm{G}, \mathrm{G}]$ is strictly upper triangular; the product $\operatorname{ad}_x \operatorname{ad}_y$ is then strictly upper triangular, hence has trace zero. Conversely, if $\kappa(\mathrm{G}, [\mathrm{G}, \mathrm{G}]) = 0$, one shows that $[\mathrm{G}, \mathrm{G}]$ is nilpotent by applying Engel's theorem, which forces $\mathrm{G}$ to be solvable. The second implication is the substance of the theorem and is standard.

**Theorem (Engel).** A finite-dimensional Lie algebra $\mathrm{G}$ is nilpotent if and only if $\operatorname{ad}_x$ is nilpotent for every $x \in \mathrm{G}$.

**Theorem (Lie).** Let $\mathrm{G} \subseteq \mathrm{GL}(V)$ be a solvable Lie subalgebra over an algebraically closed field of characteristic zero. Then there is a basis of $V$ in which every element of $\mathrm{G}$ is upper triangular.

Engel's and Lie's theorems are used in the proof of Cartan's criterion and are stated here for reference; both are proved in the standard texts listed under Further Reading.

### Cartan's Criterion for Semisimplicity

**Theorem (Cartan's criterion for semisimplicity).** Let $\mathrm{G}$ be a finite-dimensional Lie algebra over a field of characteristic zero. Then $\mathrm{G}$ is semisimple if and only if the Killing form $\kappa$ is nondegenerate.

**Proof.** Suppose first that $\mathrm{G}^{\perp} \neq 0$. The radical $\mathrm{G}^{\perp}$ is an ideal, and the Killing form of the algebra $\mathrm{G}^{\perp}$, computed in $\mathrm{G}^{\perp}$ itself, is the restriction of $\kappa$ to it. For $x \in \mathrm{G}^{\perp}$ and $y \in \mathrm{G}^{\perp}$ the trace $\operatorname{tr}(\operatorname{ad}_x\operatorname{ad}_y)$ taken in $\mathrm{G}$ equals the trace taken in $\mathrm{G}^{\perp}$: indeed $\operatorname{ad}_x$ maps $\mathrm{G}$ into $\mathrm{G}^{\perp}$, and on $\mathrm{G}^{\perp}$ the endomorphism $\operatorname{ad}_x$ is the same whether computed in $\mathrm{G}$ or in $\mathrm{G}^{\perp}$ because $\mathrm{G}^{\perp}$ is an ideal. Since $x, y \in \mathrm{G}^{\perp}$ the trace is zero by definition of the radical, so $\kappa|_{\mathrm{G}^{\perp}} = 0$. By Cartan's solvability criterion applied to $\mathrm{G}^{\perp}$, whose Killing form vanishes on the whole algebra and hence on $(\mathrm{G}^{\perp}, [\mathrm{G}^{\perp}, \mathrm{G}^{\perp}])$, the ideal $\mathrm{G}^{\perp}$ is solvable and nonzero, contradicting semisimplicity. Hence $\kappa$ is nondegenerate.

Conversely, suppose $\mathrm{A} \neq 0$ is an abelian ideal of $\mathrm{G}$. For $x \in \mathrm{A}$ and $y \in \mathrm{G}$, the endomorphism $\operatorname{ad}_x \operatorname{ad}_y$ maps $\mathrm{G}$ into $\mathrm{A}$, because $\mathrm{A}$ is an ideal, and maps $\mathrm{A}$ to zero, because $\mathrm{A}$ is abelian and $x \in \mathrm{A}$; hence $(\operatorname{ad}_x\operatorname{ad}_y)^2 = 0$ and $\kappa(x, y) = 0$. Therefore $x \in \mathrm{G}^{\perp}$, so $\mathrm{G}^{\perp} \neq 0$ and $\kappa$ is degenerate. Contrapositively, nondegeneracy of $\kappa$ forbids nonzero abelian ideals, hence forbids nonzero solvable ideals, so $\mathrm{G}$ is semisimple.

## Semisimple Lie Algebras

### The Decomposition into Simple Ideals

**Theorem.** Let $\mathrm{G}$ be a finite-dimensional semisimple Lie algebra over a field of characteristic zero. Then $\mathrm{G}$ is the direct sum of its minimal nonzero ideals,

$$
\mathrm{G} = \mathrm{G}_1 \oplus \cdots \oplus \mathrm{G}_r,
$$

and each $\mathrm{G}_i$ is simple. The ideals $\mathrm{G}_i$ are pairwise orthogonal with respect to $\kappa$, the direct sum is orthogonal, and the decomposition is unique up to order.

**Proof.** Let $\mathrm{G}_1$ be a minimal nonzero ideal. Its orthogonal complement $\mathrm{G}_1^{\perp}$ with respect to the nondegenerate form $\kappa$ is an ideal, because $\kappa$ is invariant, and $\mathrm{G} = \mathrm{G}_1 \oplus \mathrm{G}_1^{\perp}$ as vector spaces. The ideal $\mathrm{G}_1$ is simple: if $\mathrm{A} \subseteq \mathrm{G}_1$ is a nonzero ideal of $\mathrm{G}_1$, then $[\mathrm{A}, \mathrm{G}] \subseteq [\mathrm{A}, \mathrm{G}_1] + [\mathrm{A}, \mathrm{G}_1^{\perp}] \subseteq \mathrm{A} + [\mathrm{G}_1, \mathrm{G}_1^{\perp}] = \mathrm{A}$, because $\mathrm{G}_1^{\perp}$ is an ideal and $[\mathrm{G}_1, \mathrm{G}_1^{\perp}] \subseteq \mathrm{G}_1 \cap \mathrm{G}_1^{\perp} = 0$; so $\mathrm{A}$ is an ideal of $\mathrm{G}$ and equals $\mathrm{G}_1$ by minimality. The orthogonal complement $\mathrm{G}_1^{\perp}$, being a summand, is an ideal that is semisimple with nondegenerate Killing form; induction on the dimension applies to it, and uniqueness follows because the minimal ideals are the simple summands.

**Corollary.** A semisimple Lie algebra satisfies $[\mathrm{G}, \mathrm{G}] = \mathrm{G}$: it is perfect. Every ideal of a semisimple algebra is a sum of some of the simple summands, and is itself semisimple; the only abelian ideal is zero.

### Weyl's Complete Reducibility

**Theorem (Weyl).** Let $\mathrm{G}$ be a finite-dimensional semisimple Lie algebra over a field of characteristic zero. Then every finite-dimensional representation of $\mathrm{G}$ is completely reducible: every invariant subspace has an invariant complement, and every representation is a direct sum of irreducible representations.

**Proof sketch.** One proves the vanishing of the first cohomology $H^1(\mathrm{G}, V) = 0$ for every finite-dimensional module $V$, using the Casimir element of the representation. Given a submodule $W \subseteq V$, the short exact sequence $0 \to W \to V \to V/W \to 0$ has a splitting over the field, and the Casimir element corrects that linear splitting to a $\mathrm{G}$-equivariant one; the corrected splitting exists because the Casimir element acts invertibly on the relevant space for a semisimple $\mathrm{G}$.

**Corollary.** Every finite-dimensional representation of a semisimple Lie algebra is a direct sum of irreducible representations, and these are classified by their highest weights, as developed.

## The Levi Decomposition

**Theorem (Levi).** Let $\mathrm{G}$ be a finite-dimensional Lie algebra over a field of characteristic zero, with radical $\mathrm{R} = \mathrm{R}(\mathrm{G})$. Then there is a semisimple subalgebra $\mathrm{S} \subseteq \mathrm{G}$, a **Levi factor**, such that $\mathrm{G}$ is the semidirect sum

$$
\mathrm{G} = \mathrm{R} \rtimes \mathrm{S},
$$

that is, $\mathrm{G} = \mathrm{R} + \mathrm{S}$ with $\mathrm{R} \cap \mathrm{S} = 0$ and $[\mathrm{R}, \mathrm{S}] \subseteq \mathrm{R}$. The radical $\mathrm{R}$ is an ideal, $\mathrm{S}$ is a subalgebra isomorphic to $\mathrm{G}/\mathrm{R}$, and any two Levi factors are conjugate by an element of the group generated by the inner automorphisms corresponding to nilpotent elements of $\mathrm{R}$.

**Proof sketch.** The quotient $\mathrm{G}/\mathrm{R}$ is semisimple. One shows by induction on $\dim\mathrm{R}$ that the extension splits: the semisimple quotient has vanishing second cohomology with coefficients in $\mathrm{R}$, $H^2(\mathrm{G}/\mathrm{R}, \mathrm{R}) = 0$, and a splitting of the extension is exactly a Levi factor. The conjugacy statement is the theorem of Malcev–Harish-Chandra.

**Corollary.** Every finite-dimensional Lie algebra over a field of characteristic zero is built from a semisimple algebra and a solvable ideal, and every solvable Lie algebra is an iterated extension of abelian algebras.

## Examples

**The general linear algebra.** For $\mathrm{GL}(n, K)$ with $K$ of characteristic zero, the Killing form is

$$
\kappa(X, Y) = 2n \operatorname{tr}(XY) - 2 \operatorname{tr}(X)\operatorname{tr}(Y).
$$

For $\mathrm{SL}(n, K) \subseteq \mathrm{GL}(n, K)$ the restriction is $\kappa(X, Y) = 2n\operatorname{tr}(XY)$, which is nondegenerate on the traceless matrices; hence $\mathrm{SL}(n, K)$ is semisimple for $n \geq 2$. It has no nonzero proper ideals: $\mathrm{SL}(n, K)$ is simple for $n \geq 2$.

**The Heisenberg algebra.** Let $\mathrm{N}$ have basis $x, y, z$ with $[x, y] = z$ and $z$ central. Then $\mathrm{N}$ is nilpotent of class $2$, with derived subalgebra and centre both equal to $\langle z\rangle$. The Killing form vanishes identically, since every $\operatorname{ad}_u$ is nilpotent and so every product $\operatorname{ad}_u\operatorname{ad}_v$ has zero trace; the form is maximally degenerate, and $\mathrm{N}$ is neither semisimple nor reductive. This is the standard example in which Cartan's criterion detects solvability: $\kappa(\mathrm{N}, [\mathrm{N}, \mathrm{N}]) = 0$.

**The orthogonal algebra.** For $\mathrm{SO}(n, K)$ with $n \geq 3$ and $K$ of characteristic zero, the Killing form is a nonzero multiple of the trace form $\operatorname{tr}(XY)$, and $\mathrm{SO}(n)$ is simple for $n \neq 4$; for $n = 4$ it is the direct sum of two copies of $\mathrm{SL}(2, K)$, the exceptional isogeny $\mathrm{SO}(4) \cong \mathrm{SL}(2) \oplus \mathrm{SL}(2)$.

**A solvable non-nilpotent algebra.** The two-dimensional algebra with basis $x, y$ and $[x, y] = x$ has radical equal to itself, radical series $\mathrm{G}^{(1)} = \langle x\rangle$, $\mathrm{G}^{(2)} = 0$, and lower central series $\mathrm{G}_1 = \langle x\rangle = \mathrm{G}_k$ for all $k \geq 1$; it is solvable of derived length $2$ and not nilpotent. Its Killing form is nonzero but degenerate, and the Levi decomposition is trivial, $\mathrm{G} = \mathrm{G} \rtimes 0$.

## Summary

A finite-dimensional Lie algebra over a field of characteristic zero has a largest solvable ideal, the radical $\mathrm{R}$, and a largest nilpotent ideal contained in it, the nilradical; the algebra is semisimple when the radical is zero, and simple when it is nonabelian with no nonzero proper ideal. Solvability and nilpotency are detected by the derived series and the lower central series, and the classes of solvable and nilpotent algebras are closed under subalgebras, quotients, and extensions.

The adjoint map $x \mapsto \operatorname{ad}_x$ is a representation with kernel the centre, and its image is the ideal of inner derivations inside the Lie algebra of all derivations; for a semisimple algebra every derivation is inner. The Killing form $\kappa(x, y) = \operatorname{tr}(\operatorname{ad}_x\operatorname{ad}_y)$ is symmetric and invariant, its radical is an ideal, and Cartan's criteria give the two decisive tests: $\mathrm{G}$ is solvable exactly when $\kappa(\mathrm{G}, [\mathrm{G}, \mathrm{G}]) = 0$, and $\mathrm{G}$ is semisimple exactly when $\kappa$ is nondegenerate. A semisimple algebra is a direct sum of simple ideals, pairwise orthogonal for $\kappa$ and unique up to order, it is perfect, and by Weyl's theorem all its finite-dimensional representations are completely reducible. Every finite-dimensional Lie algebra of characteristic zero is a semidirect sum $\mathrm{R} \rtimes \mathrm{S}$ of its radical and a semisimple Levi factor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | Field of characteristic zero for the structure theory |
| $\mathrm{G}, \mathrm{H}$ | Lie algebras over $K$ |
| $\mathrm{I}, \mathrm{A}$ | Ideals of a Lie algebra |
| $\mathrm{Z}(\mathrm{G})$ | Centre, $\{x : [x, y] = 0 \ \forall y\}$; equals $\ker(\operatorname{ad})$ |
| $[\mathrm{G}, \mathrm{G}]$ | Derived subalgebra |
| $\mathrm{G}^{(k)}, \mathrm{G}_k$ | Derived series and lower central series |
| $\mathrm{R}(\mathrm{G})$ | Radical, the largest solvable ideal |
| $\mathrm{N}(\mathrm{G})$ | Nilradical, the largest nilpotent ideal |
| Semisimple, simple, reductive | $\mathrm{R} = 0$; nonabelian with no nonzero proper ideal; $\mathrm{R} = \mathrm{Z}(\mathrm{G})$ |
| $\operatorname{ad}_x(y) = [x, y]$ | Adjoint map; $\operatorname{ad}_{[x,y]} = [\operatorname{ad}_x, \operatorname{ad}_y]$ |
| $\operatorname{Der}(\mathrm{G})$ | Lie algebra of derivations |
| $\operatorname{Inn}(\mathrm{G}) = \operatorname{ad}(\mathrm{G})$ | Inner derivations, an ideal of $\operatorname{Der}(\mathrm{G})$ |
| $\operatorname{Out}(\mathrm{G})$ | Outer derivations, $\operatorname{Der}(\mathrm{G})/\operatorname{Inn}(\mathrm{G})$ |
| $\kappa(x, y) = \operatorname{tr}(\operatorname{ad}_x\operatorname{ad}_y)$ | Killing form; symmetric, invariant |
| $\mathrm{G}^{\perp}$ | Radical of $\kappa$; an ideal; nonzero iff $\mathrm{G}$ not semisimple |
| $\mathrm{G} = \mathrm{R} \rtimes \mathrm{S}$ | Levi decomposition; $\mathrm{S}$ a semisimple Levi factor |
| $\mathrm{GL}(n), \mathrm{SL}(n), \mathrm{SO}(n)$ | General linear, special linear, orthogonal Lie algebras |





## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the structure theory, Killing form, and Cartan's criteria.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the radical, nilradical, and the Levi decomposition developed in full.
- Karin Erdmann and Mark J. Wildon, *Introduction to Lie Algebras* (Springer, 2006), for an elementary treatment of solvable, nilpotent and semisimple algebras.
- Jean-Pierre Serre, *Complex Semisimple Lie Algebras* (Springer, 1987), for the structure theory over the complex numbers and the route to the classification.
- Nathan Jacobson, *Lie Algebras* (Interscience, 1962), for Engel's theorem, Lie's theorem, and Cartan's criteria with complete proofs.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2nd ed. 2002), for the structure theory in the setting of Lie groups.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2nd ed. 2015), for Cartan's criteria and complete reducibility with proofs.
