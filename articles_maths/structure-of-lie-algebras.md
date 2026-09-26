
# __Structure of Lie Algebras__

## Introduction

The companion article *Lie Algebras* introduces Lie algebras, the Jacobi identity, and the vocabulary of solvable, nilpotent and simple algebras. This article develops the structure theory that organises that vocabulary: the radical, the nilradical, the Killing form, and the two criteria of Cartan, which decide solvability and semisimplicity from a single bilinear form. The theory culminates in the Levi decomposition, which writes every finite-dimensional Lie algebra over a field of characteristic zero as a semidirect product of a semisimple algebra by a solvable one, and in the theorem that a semisimple algebra is a direct sum of simple ideals. Together with the classification of simple algebras by root systems, this is the structure theory of Lie algebras.

The theory is carried out over a field $K$ of characteristic zero; this is the setting in which the classical results hold cleanly, and where a result needs more than that — an algebraically closed field, or the finite dimension of the algebra — this is stated explicitly. Lie algebras are written in lowercase fraktur, so $\mathfrak{g}$, $\mathfrak{h}$ are Lie algebras, $\mathfrak{i}$ is an ideal, $\mathfrak{r}$ the radical, $\mathfrak{n}$ the nilradical, and $\mathfrak{z}(\mathfrak{g})$ the centre; the field is $K$, and $R$ is reserved for the commutative-ring statements of the earlier articles. No physics is invoked.

The general facts about Lie algebras used below — the definition, the Jacobi identity, ideals, quotients, homomorphisms, the centre, the derived subalgebra, and the elementary properties of solvable and nilpotent algebras — are assumed from *Lie Algebras*, and the representation-theoretic notions are developed further .

## Recapitulation and the Radical

### Ideals, Quotients and Homomorphisms

A **Lie algebra** over $K$ is a $K$-vector space $\mathfrak{g}$ with a bilinear, alternating bracket $[\cdot, \cdot] : \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$ satisfying the Jacobi identity

$$
[x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0.
$$

The centre of $\mathfrak{g}$ is

$$
\mathfrak{z}(\mathfrak{g}) = \{x \in \mathfrak{g} : [x, y] = 0 \text{ for all } y \in \mathfrak{g}\},
$$

and the derived subalgebra is $[\mathfrak{g}, \mathfrak{g}] = \operatorname{span}\{[x, y] : x, y \in \mathfrak{g}\}$. A subspace $\mathfrak{i} \subseteq \mathfrak{g}$ is an **ideal** if $[\mathfrak{g}, \mathfrak{i}] \subseteq \mathfrak{i}$; the centre and the derived subalgebra are ideals, and the quotient $\mathfrak{g}/\mathfrak{i}$ inherits a bracket. A linear map $\varphi : \mathfrak{g} \to \mathfrak{h}$ is a **homomorphism** if $\varphi([x, y]) = [\varphi(x), \varphi(y)]$; its kernel is an ideal and its image is a subalgebra, and the first isomorphism theorem holds. All of this is the content of *Lie Algebras*.

Recall also that the bracket of ideals is an ideal, so the derived subalgebra of an ideal is again an ideal; iterating this observation produces the derived series below.

### Solvable and Nilpotent Algebras

**Definition.** The **derived series** of $\mathfrak{g}$ is

$$
\mathfrak{g}^{(0)} = \mathfrak{g}, \qquad \mathfrak{g}^{(k+1)} = [\mathfrak{g}^{(k)}, \mathfrak{g}^{(k)}],
$$

and the **lower central series** is

$$
\mathfrak{g}_0 = \mathfrak{g}, \qquad \mathfrak{g}_{k+1} = [\mathfrak{g}, \mathfrak{g}_k].
$$

The algebra $\mathfrak{g}$ is **solvable** if $\mathfrak{g}^{(k)} = 0$ for some $k$, and **nilpotent** if $\mathfrak{g}_k = 0$ for some $k$. The least such $k$ is the **derived length**, respectively the **nilpotency class**.

**Proposition.** Every nilpotent Lie algebra is solvable, but not conversely. Subalgebras and quotients of solvable algebras are solvable, and the same holds for nilpotent algebras.

**Proof.** $\mathfrak{g}^{(k)} \subseteq \mathfrak{g}_k$ by induction, so nilpotency implies solvability. The two-dimensional nonabelian Lie algebra with basis $x, y$ and $[x, y] = x$ is solvable, since $[\mathfrak{g}, \mathfrak{g}] = \langle x\rangle$ is abelian, but it is not nilpotent, since $\mathfrak{g}_k = \langle x\rangle$ for all $k \geq 1$. The claims about subalgebras and quotients follow from the definitions. $\square$

**Proposition.** Let $\mathfrak{i}$ be an ideal of $\mathfrak{g}$. If $\mathfrak{i}$ and $\mathfrak{g}/\mathfrak{i}$ are solvable, then so is $\mathfrak{g}$; the analogous statement holds for nilpotency. Consequently the sum of two solvable ideals is solvable, and the sum of two nilpotent ideals is nilpotent.

**Proof.** If $\mathfrak{g}/\mathfrak{i}$ is solvable, then $\mathfrak{g}^{(k)} \subseteq \mathfrak{i}$ for some $k$; if $\mathfrak{i}$ is solvable, then $\mathfrak{i}^{(l)} = 0$ for some $l$, and since $\mathfrak{i}$ is an ideal the derived series of $\mathfrak{g}$ satisfies $\mathfrak{g}^{(k+l)} \subseteq \mathfrak{i}^{(l)} = 0$. For nilpotency the argument is the same with the lower central series: the ideal property gives $\mathfrak{g}_{k+l} \subseteq \mathfrak{i}_l$. For the sums, note that $(\mathfrak{i} + \mathfrak{a})/\mathfrak{a} \cong \mathfrak{i}/(\mathfrak{i} \cap \mathfrak{a})$ is solvable, and apply the extension statement. $\square$

### The Radical and the Nilradical

**Definition.** Because the sum of solvable ideals is solvable, the solvable ideals of $\mathfrak{g}$ have a largest element, the **radical**

$$
\mathfrak{r}(\mathfrak{g}) = \sum_{\mathfrak{a} \text{ solvable ideal}} \mathfrak{a}.
$$

It is a solvable ideal containing every solvable ideal. Similarly the **nilradical** $\mathfrak{n}(\mathfrak{g})$ is the largest nilpotent ideal, and it is contained in the radical.

**Definition.** The Lie algebra $\mathfrak{g}$ is **semisimple** if $\mathfrak{r}(\mathfrak{g}) = 0$, equivalently if it has no nonzero solvable ideal; it is **simple** if it is nonabelian and has no nonzero proper ideal; and it is **reductive** if $\mathfrak{r}(\mathfrak{g}) = \mathfrak{z}(\mathfrak{g})$.

**Proposition.** $\mathfrak{g}$ is semisimple if and only if it has no nonzero abelian ideal. In particular every simple Lie algebra is semisimple, and the semisimple algebras are exactly the direct sums of simple algebras.

**Proof.** If $\mathfrak{g}$ has a nonzero solvable ideal $\mathfrak{a} \neq 0$, then the last nonzero term of its derived series is a nonzero abelian ideal of $\mathfrak{g}$, because it is a characteristic ideal of $\mathfrak{a}$ and $\mathfrak{a}$ is an ideal. Conversely a nonzero abelian ideal is solvable, so its presence contradicts semisimplicity. The remaining statements follow from the decomposition theorem proved below. $\square$

## The Adjoint Representation and Derivations

### The Adjoint Map

**Definition.** For $x \in \mathfrak{g}$ the **adjoint map** is $\operatorname{ad}_x : \mathfrak{g} \to \mathfrak{g}$, $\operatorname{ad}_x(y) = [x, y]$. The Jacobi identity is equivalent to

$$
\operatorname{ad}_x([y, z]) = [\operatorname{ad}_x(y), z] + [y, \operatorname{ad}_x(z)],
$$

so each $\operatorname{ad}_x$ is a derivation of the bracket, and

$$
\operatorname{ad}_{[x, y]} = [\operatorname{ad}_x, \operatorname{ad}_y].
$$

Hence $\operatorname{ad} : \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$ is a Lie algebra homomorphism, the **adjoint representation**, whose kernel is the centre:

$$
\ker(\operatorname{ad}) = \mathfrak{z}(\mathfrak{g}), \qquad \operatorname{ad}(\mathfrak{g}) \cong \mathfrak{g}/\mathfrak{z}(\mathfrak{g}).
$$

### Derivations of a Lie Algebra

**Definition.** A **derivation** of $\mathfrak{g}$ is a linear map $D : \mathfrak{g} \to \mathfrak{g}$ satisfying the Leibniz rule with respect to the bracket,

$$
D([x, y]) = [D(x), y] + [x, D(y)].
$$

The derivations form a Lie algebra $\operatorname{Der}(\mathfrak{g})$ under the commutator $[D_1, D_2] = D_1 D_2 - D_2 D_1$; the **inner derivations** are those of the form $\operatorname{ad}_x$, and they form the subspace $\operatorname{Inn}(\mathfrak{g}) = \operatorname{ad}(\mathfrak{g})$.

**Proposition.** $\operatorname{Inn}(\mathfrak{g})$ is an ideal of $\operatorname{Der}(\mathfrak{g})$, and the quotient $\operatorname{Out}(\mathfrak{g}) = \operatorname{Der}(\mathfrak{g})/\operatorname{Inn}(\mathfrak{g})$ is the Lie algebra of **outer derivations**. For a semisimple $\mathfrak{g}$ over a field of characteristic zero, $\operatorname{Der}(\mathfrak{g}) = \operatorname{Inn}(\mathfrak{g})$; every derivation is inner.

**Proof.** For $D \in \operatorname{Der}(\mathfrak{g})$ and $x \in \mathfrak{g}$ one computes

$$
[D, \operatorname{ad}_x](y) = D([x, y]) - [x, D(y)] = [D(x), y] = \operatorname{ad}_{D(x)}(y),
$$

so $[D, \operatorname{ad}_x] = \operatorname{ad}_{D(x)} \in \operatorname{Inn}(\mathfrak{g})$, which is the ideal property. The vanishing of $\operatorname{Out}(\mathfrak{g})$ for semisimple algebras is a standard theorem of the structure theory, proved by showing that a derivation orthogonal to the inner ones annihilates the Killing form and hence vanishes; the result is the infinitesimal form of the statement that the automorphism group of a semisimple algebra has Lie algebra $\operatorname{Der}(\mathfrak{g}) = \mathfrak{g}$. $\square$

## The Killing Form

### Definition and Symmetry

**Definition.** The **Killing form** of a finite-dimensional Lie algebra $\mathfrak{g}$ is the bilinear form

$$
\kappa(x, y) = \operatorname{tr}\bigl(\operatorname{ad}_x \circ \operatorname{ad}_y\bigr), \qquad x, y \in \mathfrak{g}.
$$

**Proposition.** $\kappa$ is a symmetric bilinear form on $\mathfrak{g}$, and it is **invariant** in the sense that

$$
\kappa([x, y], z) = \kappa(x, [y, z])
$$

for all $x, y, z \in \mathfrak{g}$; equivalently, $\kappa(\operatorname{ad}_y(x), z) + \kappa(x, \operatorname{ad}_y(z)) = 0$.

**Proof.** Bilinearity is immediate, and symmetry follows from the trace identity $\operatorname{tr}(AB) = \operatorname{tr}(BA)$. For invariance, use the identity $\operatorname{ad}_{[x,y]} = [\operatorname{ad}_x, \operatorname{ad}_y]$ and the trace identity $\operatorname{tr}([A, B]C) = \operatorname{tr}(A[B, C])$:

$$
\kappa([x, y], z) = \operatorname{tr}(\operatorname{ad}_{[x,y]}\operatorname{ad}_z) = \operatorname{tr}([\operatorname{ad}_x, \operatorname{ad}_y]\operatorname{ad}_z) = \operatorname{tr}(\operatorname{ad}_x[\operatorname{ad}_y, \operatorname{ad}_z]) = \operatorname{tr}(\operatorname{ad}_x \operatorname{ad}_{[y,z]}) = \kappa(x, [y, z]).
$$

$\square$

**Corollary.** Every algebra automorphism of $\mathfrak{g}$ preserves $\kappa$, and every derivation of $\mathfrak{g}$ is skew with respect to $\kappa$: $\kappa(D(x), y) + \kappa(x, D(y)) = 0$.

### The Radical of the Killing Form

**Definition.** The **radical** of $\kappa$ is

$$
\mathfrak{g}^{\perp} = \{x \in \mathfrak{g} : \kappa(x, y) = 0 \text{ for all } y \in \mathfrak{g}\},
$$

and $\kappa$ is **nondegenerate** if $\mathfrak{g}^{\perp} = 0$.

**Proposition.** $\mathfrak{g}^{\perp}$ is an ideal of $\mathfrak{g}$. The form $\kappa$ is nondegenerate if and only if the pairing $\mathfrak{g} \times \mathfrak{g} \to K$ it induces identifies $\mathfrak{g}$ with its dual $\mathfrak{g}^*$.

**Proof.** If $x \in \mathfrak{g}^{\perp}$ then for all $y, z$ invariance gives $\kappa([x, y], z) = \kappa(x, [y, z]) = 0$, so $[x, y] \in \mathfrak{g}^{\perp}$; hence $\mathfrak{g}^{\perp}$ is an ideal. The second statement is the definition of nondegeneracy for a bilinear form. $\square$

## Cartan's Criteria

### Cartan's Criterion for Solvability

**Theorem (Cartan's criterion for solvability).** Let $\mathfrak{g}$ be a finite-dimensional Lie algebra over a field of characteristic zero. Then $\mathfrak{g}$ is solvable if and only if

$$
\kappa(\mathfrak{g}, [\mathfrak{g}, \mathfrak{g}]) = 0,
$$

that is, $\kappa(x, y) = 0$ for all $x \in \mathfrak{g}$ and all $y \in [\mathfrak{g}, \mathfrak{g}]$.

**Proof sketch.** If $\mathfrak{g}$ is solvable, then over an algebraic closure of $K$ the algebra $\mathfrak{g}$ is isomorphic to a subalgebra of the upper triangular matrices by Lie's theorem, so each $\operatorname{ad}_x$ is upper triangular and each commutator $\operatorname{ad}_y$ with $y \in [\mathfrak{g}, \mathfrak{g}]$ is strictly upper triangular; the product $\operatorname{ad}_x \operatorname{ad}_y$ is then strictly upper triangular, hence has trace zero. Conversely, if $\kappa(\mathfrak{g}, [\mathfrak{g}, \mathfrak{g}]) = 0$, one shows that $[\mathfrak{g}, \mathfrak{g}]$ is nilpotent by applying Engel's theorem, which forces $\mathfrak{g}$ to be solvable. The second implication is the substance of the theorem and is standard. $\square$

**Theorem (Engel).** A finite-dimensional Lie algebra $\mathfrak{g}$ is nilpotent if and only if $\operatorname{ad}_x$ is nilpotent for every $x \in \mathfrak{g}$.

**Theorem (Lie).** Let $\mathfrak{g} \subseteq \mathfrak{gl}(V)$ be a solvable Lie subalgebra over an algebraically closed field of characteristic zero. Then there is a basis of $V$ in which every element of $\mathfrak{g}$ is upper triangular.

Engel's and Lie's theorems are used in the proof of Cartan's criterion and are stated here for reference; both are proved in the standard texts listed under Further Reading.

### Cartan's Criterion for Semisimplicity

**Theorem (Cartan's criterion for semisimplicity).** Let $\mathfrak{g}$ be a finite-dimensional Lie algebra over a field of characteristic zero. Then $\mathfrak{g}$ is semisimple if and only if the Killing form $\kappa$ is nondegenerate.

**Proof.** Suppose first that $\mathfrak{g}^{\perp} \neq 0$. The radical $\mathfrak{g}^{\perp}$ is an ideal, and the Killing form of the algebra $\mathfrak{g}^{\perp}$, computed in $\mathfrak{g}^{\perp}$ itself, is the restriction of $\kappa$ to it. For $x \in \mathfrak{g}^{\perp}$ and $y \in \mathfrak{g}^{\perp}$ the trace $\operatorname{tr}(\operatorname{ad}_x\operatorname{ad}_y)$ taken in $\mathfrak{g}$ equals the trace taken in $\mathfrak{g}^{\perp}$: indeed $\operatorname{ad}_x$ maps $\mathfrak{g}$ into $\mathfrak{g}^{\perp}$, and on $\mathfrak{g}^{\perp}$ the endomorphism $\operatorname{ad}_x$ is the same whether computed in $\mathfrak{g}$ or in $\mathfrak{g}^{\perp}$ because $\mathfrak{g}^{\perp}$ is an ideal. Since $x, y \in \mathfrak{g}^{\perp}$ the trace is zero by definition of the radical, so $\kappa|_{\mathfrak{g}^{\perp}} = 0$. By Cartan's solvability criterion applied to $\mathfrak{g}^{\perp}$, whose Killing form vanishes on the whole algebra and hence on $(\mathfrak{g}^{\perp}, [\mathfrak{g}^{\perp}, \mathfrak{g}^{\perp}])$, the ideal $\mathfrak{g}^{\perp}$ is solvable and nonzero, contradicting semisimplicity. Hence $\kappa$ is nondegenerate.

Conversely, suppose $\mathfrak{a} \neq 0$ is an abelian ideal of $\mathfrak{g}$. For $x \in \mathfrak{a}$ and $y \in \mathfrak{g}$, the endomorphism $\operatorname{ad}_x \operatorname{ad}_y$ maps $\mathfrak{g}$ into $\mathfrak{a}$, because $\mathfrak{a}$ is an ideal, and maps $\mathfrak{a}$ to zero, because $\mathfrak{a}$ is abelian and $x \in \mathfrak{a}$; hence $(\operatorname{ad}_x\operatorname{ad}_y)^2 = 0$ and $\kappa(x, y) = 0$. Therefore $x \in \mathfrak{g}^{\perp}$, so $\mathfrak{g}^{\perp} \neq 0$ and $\kappa$ is degenerate. Contrapositively, nondegeneracy of $\kappa$ forbids nonzero abelian ideals, hence forbids nonzero solvable ideals, so $\mathfrak{g}$ is semisimple. $\square$

## Semisimple Lie Algebras

### The Decomposition into Simple Ideals

**Theorem.** Let $\mathfrak{g}$ be a finite-dimensional semisimple Lie algebra over a field of characteristic zero. Then $\mathfrak{g}$ is the direct sum of its minimal nonzero ideals,

$$
\mathfrak{g} = \mathfrak{g}_1 \oplus \cdots \oplus \mathfrak{g}_r,
$$

and each $\mathfrak{g}_i$ is simple. The ideals $\mathfrak{g}_i$ are pairwise orthogonal with respect to $\kappa$, the direct sum is orthogonal, and the decomposition is unique up to order.

**Proof.** Let $\mathfrak{g}_1$ be a minimal nonzero ideal. Its orthogonal complement $\mathfrak{g}_1^{\perp}$ with respect to the nondegenerate form $\kappa$ is an ideal, because $\kappa$ is invariant, and $\mathfrak{g} = \mathfrak{g}_1 \oplus \mathfrak{g}_1^{\perp}$ as vector spaces. The ideal $\mathfrak{g}_1$ is simple: if $\mathfrak{a} \subseteq \mathfrak{g}_1$ is a nonzero ideal of $\mathfrak{g}_1$, then $[\mathfrak{a}, \mathfrak{g}] \subseteq [\mathfrak{a}, \mathfrak{g}_1] + [\mathfrak{a}, \mathfrak{g}_1^{\perp}] \subseteq \mathfrak{a} + [\mathfrak{g}_1, \mathfrak{g}_1^{\perp}] = \mathfrak{a}$, because $\mathfrak{g}_1^{\perp}$ is an ideal and $[\mathfrak{g}_1, \mathfrak{g}_1^{\perp}] \subseteq \mathfrak{g}_1 \cap \mathfrak{g}_1^{\perp} = 0$; so $\mathfrak{a}$ is an ideal of $\mathfrak{g}$ and equals $\mathfrak{g}_1$ by minimality. The orthogonal complement $\mathfrak{g}_1^{\perp}$, being a summand, is an ideal that is semisimple with nondegenerate Killing form; induction on the dimension applies to it, and uniqueness follows because the minimal ideals are the simple summands. $\square$

**Corollary.** A semisimple Lie algebra satisfies $[\mathfrak{g}, \mathfrak{g}] = \mathfrak{g}$: it is perfect. Every ideal of a semisimple algebra is a sum of some of the simple summands, and is itself semisimple; the only abelian ideal is zero.

### Weyl's Complete Reducibility

**Theorem (Weyl).** Let $\mathfrak{g}$ be a finite-dimensional semisimple Lie algebra over a field of characteristic zero. Then every finite-dimensional representation of $\mathfrak{g}$ is completely reducible: every invariant subspace has an invariant complement, and every representation is a direct sum of irreducible representations.

**Proof sketch.** One proves the vanishing of the first cohomology $H^1(\mathfrak{g}, V) = 0$ for every finite-dimensional module $V$, using the Casimir element of the representation. Given a submodule $W \subseteq V$, the short exact sequence $0 \to W \to V \to V/W \to 0$ has a splitting over the field, and the Casimir element corrects that linear splitting to a $\mathfrak{g}$-equivariant one; the corrected splitting exists because the Casimir element acts invertibly on the relevant space for a semisimple $\mathfrak{g}$. $\square$

**Corollary.** Every finite-dimensional representation of a semisimple Lie algebra is a direct sum of irreducible representations, and these are classified by their highest weights, as developed.

## The Levi Decomposition

**Theorem (Levi).** Let $\mathfrak{g}$ be a finite-dimensional Lie algebra over a field of characteristic zero, with radical $\mathfrak{r} = \mathfrak{r}(\mathfrak{g})$. Then there is a semisimple subalgebra $\mathfrak{s} \subseteq \mathfrak{g}$, a **Levi factor**, such that $\mathfrak{g}$ is the semidirect sum

$$
\mathfrak{g} = \mathfrak{r} \rtimes \mathfrak{s},
$$

that is, $\mathfrak{g} = \mathfrak{r} + \mathfrak{s}$ with $\mathfrak{r} \cap \mathfrak{s} = 0$ and $[\mathfrak{r}, \mathfrak{s}] \subseteq \mathfrak{r}$. The radical $\mathfrak{r}$ is an ideal, $\mathfrak{s}$ is a subalgebra isomorphic to $\mathfrak{g}/\mathfrak{r}$, and any two Levi factors are conjugate by an element of the group generated by the inner automorphisms corresponding to nilpotent elements of $\mathfrak{r}$.

**Proof sketch.** The quotient $\mathfrak{g}/\mathfrak{r}$ is semisimple. One shows by induction on $\dim\mathfrak{r}$ that the extension splits: the semisimple quotient has vanishing second cohomology with coefficients in $\mathfrak{r}$, $H^2(\mathfrak{g}/\mathfrak{r}, \mathfrak{r}) = 0$, and a splitting of the extension is exactly a Levi factor. The conjugacy statement is the theorem of Malcev–Harish-Chandra. $\square$

**Corollary.** Every finite-dimensional Lie algebra over a field of characteristic zero is built from a semisimple algebra and a solvable ideal, and every solvable Lie algebra is an iterated extension of abelian algebras.

## Examples

**The general linear algebra.** For $\mathfrak{gl}(n, K)$ with $K$ of characteristic zero, the Killing form is

$$
\kappa(X, Y) = 2n \operatorname{tr}(XY) - 2 \operatorname{tr}(X)\operatorname{tr}(Y).
$$

For $\mathfrak{sl}(n, K) \subseteq \mathfrak{gl}(n, K)$ the restriction is $\kappa(X, Y) = 2n\operatorname{tr}(XY)$, which is nondegenerate on the traceless matrices; hence $\mathfrak{sl}(n, K)$ is semisimple for $n \geq 2$. It has no nonzero proper ideals: $\mathfrak{sl}(n, K)$ is simple for $n \geq 2$.

**The Heisenberg algebra.** Let $\mathfrak{n}$ have basis $x, y, z$ with $[x, y] = z$ and $z$ central. Then $\mathfrak{n}$ is nilpotent of class $2$, with derived subalgebra and centre both equal to $\langle z\rangle$. The Killing form vanishes identically, since every $\operatorname{ad}_u$ is nilpotent and so every product $\operatorname{ad}_u\operatorname{ad}_v$ has zero trace; the form is maximally degenerate, and $\mathfrak{n}$ is neither semisimple nor reductive. This is the standard example in which Cartan's criterion detects solvability: $\kappa(\mathfrak{n}, [\mathfrak{n}, \mathfrak{n}]) = 0$.

**The orthogonal algebra.** For $\mathfrak{so}(n, K)$ with $n \geq 3$ and $K$ of characteristic zero, the Killing form is a nonzero multiple of the trace form $\operatorname{tr}(XY)$, and $\mathfrak{so}(n)$ is simple for $n \neq 4$; for $n = 4$ it is the direct sum of two copies of $\mathfrak{sl}(2, K)$, the exceptional isogeny $\mathfrak{so}(4) \cong \mathfrak{sl}(2) \oplus \mathfrak{sl}(2)$.

**A solvable non-nilpotent algebra.** The two-dimensional algebra with basis $x, y$ and $[x, y] = x$ has radical equal to itself, radical series $\mathfrak{g}^{(1)} = \langle x\rangle$, $\mathfrak{g}^{(2)} = 0$, and lower central series $\mathfrak{g}_1 = \langle x\rangle = \mathfrak{g}_k$ for all $k \geq 1$; it is solvable of derived length $2$ and not nilpotent. Its Killing form is nonzero but degenerate, and the Levi decomposition is trivial, $\mathfrak{g} = \mathfrak{g} \rtimes 0$.

## Summary

A finite-dimensional Lie algebra over a field of characteristic zero has a largest solvable ideal, the radical $\mathfrak{r}$, and a largest nilpotent ideal contained in it, the nilradical; the algebra is semisimple when the radical is zero, and simple when it is nonabelian with no nonzero proper ideal. Solvability and nilpotency are detected by the derived series and the lower central series, and the classes of solvable and nilpotent algebras are closed under subalgebras, quotients, and extensions.

The adjoint map $x \mapsto \operatorname{ad}_x$ is a representation with kernel the centre, and its image is the ideal of inner derivations inside the Lie algebra of all derivations; for a semisimple algebra every derivation is inner. The Killing form $\kappa(x, y) = \operatorname{tr}(\operatorname{ad}_x\operatorname{ad}_y)$ is symmetric and invariant, its radical is an ideal, and Cartan's criteria give the two decisive tests: $\mathfrak{g}$ is solvable exactly when $\kappa(\mathfrak{g}, [\mathfrak{g}, \mathfrak{g}]) = 0$, and $\mathfrak{g}$ is semisimple exactly when $\kappa$ is nondegenerate. A semisimple algebra is a direct sum of simple ideals, pairwise orthogonal for $\kappa$ and unique up to order, it is perfect, and by Weyl's theorem all its finite-dimensional representations are completely reducible. Every finite-dimensional Lie algebra of characteristic zero is a semidirect sum $\mathfrak{r} \rtimes \mathfrak{s}$ of its radical and a semisimple Levi factor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | Field of characteristic zero for the structure theory |
| $\mathfrak{g}, \mathfrak{h}$ | Lie algebras over $K$ |
| $\mathfrak{i}, \mathfrak{a}$ | Ideals of a Lie algebra |
| $\mathfrak{z}(\mathfrak{g})$ | Centre, $\{x : [x, y] = 0 \ \forall y\}$; equals $\ker(\operatorname{ad})$ |
| $[\mathfrak{g}, \mathfrak{g}]$ | Derived subalgebra |
| $\mathfrak{g}^{(k)}, \mathfrak{g}_k$ | Derived series and lower central series |
| $\mathfrak{r}(\mathfrak{g})$ | Radical, the largest solvable ideal |
| $\mathfrak{n}(\mathfrak{g})$ | Nilradical, the largest nilpotent ideal |
| Semisimple, simple, reductive | $\mathfrak{r} = 0$; nonabelian with no nonzero proper ideal; $\mathfrak{r} = \mathfrak{z}(\mathfrak{g})$ |
| $\operatorname{ad}_x(y) = [x, y]$ | Adjoint map; $\operatorname{ad}_{[x,y]} = [\operatorname{ad}_x, \operatorname{ad}_y]$ |
| $\operatorname{Der}(\mathfrak{g})$ | Lie algebra of derivations |
| $\operatorname{Inn}(\mathfrak{g}) = \operatorname{ad}(\mathfrak{g})$ | Inner derivations, an ideal of $\operatorname{Der}(\mathfrak{g})$ |
| $\operatorname{Out}(\mathfrak{g})$ | Outer derivations, $\operatorname{Der}(\mathfrak{g})/\operatorname{Inn}(\mathfrak{g})$ |
| $\kappa(x, y) = \operatorname{tr}(\operatorname{ad}_x\operatorname{ad}_y)$ | Killing form; symmetric, invariant |
| $\mathfrak{g}^{\perp}$ | Radical of $\kappa$; an ideal; nonzero iff $\mathfrak{g}$ not semisimple |
| $\mathfrak{g} = \mathfrak{r} \rtimes \mathfrak{s}$ | Levi decomposition; $\mathfrak{s}$ a semisimple Levi factor |
| $\mathfrak{gl}(n), \mathfrak{sl}(n), \mathfrak{so}(n)$ | General linear, special linear, orthogonal Lie algebras |





## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the structure theory, Killing form, and Cartan's criteria.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the radical, nilradical, and the Levi decomposition developed in full.
- Karin Erdmann and Mark J. Wildon, *Introduction to Lie Algebras* (Springer, 2006), for an elementary treatment of solvable, nilpotent and semisimple algebras.
- Jean-Pierre Serre, *Complex Semisimple Lie Algebras* (Springer, 1987), for the structure theory over the complex numbers and the route to the classification.
- Nathan Jacobson, *Lie Algebras* (Interscience, 1962), for Engel's theorem, Lie's theorem, and Cartan's criteria with complete proofs.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2nd ed. 2002), for the structure theory in the setting of Lie groups.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2nd ed. 2015), for Cartan's criteria and complete reducibility with proofs.
