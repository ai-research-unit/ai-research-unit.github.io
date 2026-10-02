
# __Unitary Representations and the Adjoint__

## Introduction

A unitary representation is a representation by operators whose adjoint is their inverse, and that single condition is the source of every adjoint identity of the theory: the integrated form of the representation is a `*`-representation, the invariants are the kernel of the adjoint-summed projection, and the intertwining operators are the commutant of the image. This article takes the unitarity condition, derives the adjoint identities it forces, and reads off the invariants and the commutant. It is the operator form of the correspondence between the unitary representations and the `*`-representations of the group algebra.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the group algebra $L^1(G)$ and the correspondence between nondegenerate `*`-representations and continuous unitary representations from *The Convolution Algebra $L^1(G)$*; the involution, the positive functionals and the completions from *The Group Algebra as an Involutive Algebra*; the positive definite functions, the GNS construction and the Gelfand–Raikov theorem from *Positive Definite Functions and the Gelfand–Raikov Theorem*; the Plancherel theorem and the unitary dual from *Unitary Representations and the Plancherel Theorem* and *Noncommutative Harmonic Analysis*; the compact averaging and the orthogonality relations from *Analysis on Compact Groups* and *The Peter–Weyl Theorem*; the adjoint on the group algebra and the elementary adjoints from *Hermitian Operators on a Group Algebra*, immediately preceding; the Hilbert spaces, the adjoint, the projections, the commutant and Schur's lemma from *Operator Algebras*. The adjoint of a convolution operator on its own terms is *The Adjoint of a Convolution Operator*, later in this group; the adjoint of a two-sided operator on a Hilbert algebra is *Two-Sided Operators on a Hilbert Algebra with Signed Hermitian Adjoint*.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$ and modular function $\Delta$; $\pi : G\to\mathcal{U}(\mathcal{H})$ is a continuous **unitary representation** on a Hilbert space $\mathcal{H}$, with $\pi(x)^* = \pi(x)^{-1} = \pi(x^{-1})$; its **integrated form** is $\pi(f) = \int_G f(x)\pi(x)\,dx$, $f\in L^1(G)$; and the **invariant subspace** is $\mathcal{H}^G = \{\xi : \pi(x)\xi = \xi\ \forall x\}$, with $P$ the projection onto it.

## The Unitarity Condition

**Theorem (the forms of unitarity).** For a homomorphism $\pi : G\to B(\mathcal{H})$ the following are equivalent: (i) $\pi(x)^*\pi(x) = 1$ for all $x$; (ii) $\pi(x)\pi(x)^* = 1$ for all $x$; (iii) $\pi(x)$ is an isometry for every $x$; (iv) $\pi$ preserves the inner product, $\langle\pi(x)\xi,\pi(x)\eta\rangle = \langle\xi,\eta\rangle$; and when these hold $\pi(x)^* = \pi(x)^{-1} = \pi(x^{-1})$ and $\pi(x)^*$ is again unitary.

**Proof.** For a homomorphism, (i) says $\pi(x)$ is an isometry, (ii) says it is a co-isometry; in a Hilbert space an isometry of the whole space is onto, so (i) implies (ii); (iii) is (i) by the polarisation identity, and (iv) is (iii) expanded. Then $\pi(x)^{-1} = \pi(x)^*$ and $\pi(x^{-1}) = \pi(x)^{-1}$ by the homomorphism property, and a unitary operator has unitary adjoint. $\square$

**Theorem (the integrated form is a `*`-representation).** For every continuous unitary representation $\pi$ and every $f\in L^1(G)$,

$$
\pi(f)^* = \pi(f^*), \qquad \pi(f*g) = \pi(f)\pi(g), \qquad \|\pi(f)\|\leq\|f\|_1 ,
$$

with $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$, for every locally compact $G$.

**Proof.** The adjoint of the operator-valued integral is the integral of the adjoints, $\pi(f)^* = \int\overline{f(x)}\pi(x)^*dx = \int\overline{f(x)}\pi(x^{-1})dx$, and the substitution $x = y^{-1}$ with the inversion identity $dx = \Delta(y)^{-1}dy$ turns this into $\int\overline{f(y^{-1})}\Delta(y)^{-1}\pi(y)dy = \pi(f^*)$. The multiplicativity is the convolution theorem in integrated form, and the norm bound is $\|\pi(f)\|\leq\int|f(x)|\|\pi(x)\|dx\leq\|f\|_1$. $\square$

**Corollary (positivity is automatic).** For every $f\in L^1(G)$ the operator $\pi(f^*\!*f) = \pi(f)^*\pi(f)$ is positive, and the functional $f\mapsto\langle\pi(f)\xi,\xi\rangle$ is a positive functional on the group algebra for every $\xi\in\mathcal{H}$; conversely every positive functional of norm one is of this form for some cyclically represented $\pi$. This is the operator statement of the correspondence between positive functionals and positive definite functions.

**Proof.** $\pi(f)^*\pi(f)\geq0$ in $B(\mathcal{H})$; the functional $\omega_\xi(f) = \langle\pi(f)\xi,\xi\rangle = \int f(x)\langle\pi(x)\xi,\xi\rangle dx$ has the positive definite function $\phi_\xi(x) = \langle\pi(x)\xi,\xi\rangle$ as its kernel, and the converse is the GNS construction of *Positive Definite Functions and the Gelfand–Raikov Theorem*. $\square$

## Invariants and the Averaging Projection

**Definition.** The **projection onto the invariants** of $\pi$ is the strong limit

$$
P = \text{strong-}\!\lim_{\alpha}\pi(u_\alpha), \qquad \mathcal{H}^G = P\mathcal{H},
$$

where $u_\alpha$ is a normalised approximate identity of $L^1(G)$; equivalently $P\xi$ is the unique invariant element closest to $\xi$.

**Theorem (the averaging identities).** The projection $P$ onto $\mathcal{H}^G$ is the strong limit of $\pi(u_\alpha)$ over a normalised approximate identity, is self-adjoint and idempotent, and commutes with every $\pi(x)$ in the strong sense $P\pi(x) = \pi(x)P = P$ for $x\in G$. If $G$ is compact with $\int_G dx = 1$ then $P = \int_G\pi(x)\,dx$, and a vector $\xi$ is invariant if and only if $\pi(f)\xi = \bigl(\int_G f\bigr)\xi$ for every $f\in L^1(G)$.

**Proof.** If $\xi\in\mathcal{H}^G$ then $\pi(f)\xi = \int f(x)\xi\,dx = (\int f)\xi$; for compact $G$ with total mass one this is $(\int f)\xi$, and conversely the identity for all $f$, tested against a bump approximate identity concentrated at $x$, gives $\pi(x)\xi = \xi$. For a general group, $P$ is the strong limit of $\pi(u_\alpha)$ (the approximate identity converges to the identity of the multiplier algebra and its integrated images converge to the projection on the fixed space), and $\pi(x)\pi(u_\alpha) = \pi(L_xu_\alpha)$ converges strongly to $P$ for each fixed $x$, so $P\pi(x) = \pi(x)P$; on $\mathcal{H}^G$ one has $P = 1$ and the stated identity follows. Self-adjointness and idempotence of $\pi(u_\alpha)$ hold in the limit because $\pi(u_\alpha)^* = \pi(u_\alpha^*)$ with $u_\alpha$ symmetric and $\pi(u_\alpha*u_\beta) = \pi(u_\alpha)\pi(u_\beta)$. $\square$

**Corollary (the compact case is averaging).** If $G = K$ is compact with normalised Haar measure then $P = \pi(\mathbf{1}_K) = \int_K\pi(k)\,dk$ is the orthogonal projection onto the $K$-fixed vectors, and the adjoint of the averaging operator is itself, $P^* = P$, with $P^2 = P$.

**Proof.** $P = \int_K\pi(k)dk$ is the strong (Bochner) integral of unitaries; $P^2 = \iint\pi(kk')dkdk' = P$ by invariance of $dk$, $P^* = \int_K\pi(k)^*dk = \int_K\pi(k^{-1})dk = P$, and the range is the fixed space. $\square$

## The Contragredient and Unitary Equivalence

**Definition.** The **contragredient** of $\pi$ acts on the conjugate Hilbert space $\bar{\mathcal H}$ by $\bar\pi(x) = (\pi(x)^{-1})^{\mathsf t}$, the transpose in a fixed orthonormal realisation; equivalently $\langle\bar\pi(x)\bar\xi,\bar\eta\rangle = \langle\pi(x)^{-1}\xi,\eta\rangle$. Two unitary representations $\pi,\sigma$ are **unitarily equivalent**, $\pi\cong\sigma$, when there is a unitary $U$ with $U\pi(x) = \sigma(x)U$.

**Theorem (the contragredient is unitary and involutive).** The contragredient $\bar\pi$ is a continuous unitary representation, the assignment $\pi\mapsto\bar\pi$ is an involution on the unitary dual up to equivalence, $\bar{\bar\pi}\cong\pi$, and the operator $U$ of a unitary equivalence is itself an intertwining unitary whose adjoint $U^*$ gives the reverse equivalence.

**Proof.** $\bar\pi$ is a composite of the anti-homomorphism $x\mapsto\pi(x)^{-1}$ with the transpose, and the transpose of a unitary is unitary, so $\bar\pi$ is unitary and continuous; applying the construction twice returns the transpose of the transpose, which is $\pi$ in the given realisation; the adjoint statement is $\langle U\pi(x)\xi,\eta\rangle = \langle\pi(x)\xi,U^*\eta\rangle = \langle\xi,\pi(x)^{-1}U^*\eta\rangle = \langle\xi,U^*\sigma(x)^{-1}\eta\rangle$. $\square$

**Corollary (the invariants).** Unitary equivalence is an equivalence relation on the unitary representations, the adjoint of any member of the intertwining space belongs to the intertwining space of the reverse pair, and the invariants of a representation under unitary equivalence are its dimension, its decomposition type and the multiplicities of its irreducible constituents.

**Proof.** Symmetry, reflexivity and transitivity of unitary equivalence are the identity, the adjoint and the composition of the intertwiners, each of which is unitary; the invariants are computed from the commutant and the decomposition, and are invariant because a unitary equivalence is an isomorphism of the module structures. $\square$

## The Commutant and the Adjoint

**Theorem (intertwiners and the commutant).** Let $\pi, \rho$ be unitary representations. A bounded operator $T : \mathcal{H}_\pi\to\mathcal{H}_\rho$ intertwines them, $T\pi(x) = \rho(x)T$ for all $x$, if and only if $T\pi(f) = \rho(f)T$ for all $f\in L^1(G)$; hence the commutant of the integrated algebra equals the commutant of the representation, $\pi(L^1(G))' = \pi(G)'$, and the adjoint of an intertwiner is an intertwiner in the reverse direction, $T^*\rho(x) = \pi(x)T^*$.

**Proof.** The equivalence uses the approximate identity to recover $\pi(x)$ from the integrated form and conversely; the adjoint statement is the identity $\langle T\pi(x)\xi,\eta\rangle = \langle\pi(x)\xi,T^*\eta\rangle = \langle\xi,\pi(x)^{-1}T^*\eta\rangle$ combined with $\rho(x)^* = \rho(x)^{-1}$. $\square$

**Corollary (Schur's lemma via the adjoint).** If $\pi$ is irreducible then $\pi(G)' = \mathbb{C}\cdot1$, and every self-adjoint operator commuting with $\pi$ is a real scalar; in particular the centre of the integrated algebra acts by scalars, and the irreducible representations are the extreme points of the normalised positive cone.

**Proof.** The commutant of an irreducible representation is the scalars; a self-adjoint element of the commutant has real spectrum, and its spectral projections commute with $\pi$, so by irreducibility they are $0$ or $1$, giving a scalar. $\square$

**Remark (what the article does not do).** The adjoint of a convolution operator on its own terms, its expression on $L^p$ and the involutive algebra of convolution operators are *The Adjoint of a Convolution Operator*, later in this group. The adjoint of a representation operator is given here only through the unitarity condition; the Plancherel measure and the inversion formula are *Unitary Representations and the Plancherel Theorem*. The adjoint of the two-sided operators of the signed block is *Two-Sided Operators on a Hilbert Algebra with Signed Hermitian Adjoint*, where the signed form appears.

## Summary

A unitary representation satisfies the equivalent conditions $\pi(x)^*\pi(x) = 1$, $\pi(x)\pi(x)^* = 1$, isometry, and preservation of the inner product, and then $\pi(x)^* = \pi(x)^{-1} = \pi(x^{-1})$. Its integrated form is a `*`-representation for every locally compact $G$, $\pi(f)^* = \pi(f^*)$, $\pi(f*g) = \pi(f)\pi(g)$, $\|\pi(f)\|\leq\|f\|_1$: the modular factor in $f^*$ is exactly what the substitution $x\to x^{-1}$ and the unitarity produce. Positivity is automatic, $\pi(f^*\!*f) = \pi(f)^*\pi(f)\geq0$, and the vector functionals $\langle\pi(f)\xi,\xi\rangle$ are the positive functionals of the group algebra, with the GNS construction as the converse. The invariants are the fixed space of the representation, in the compact case the range of the averaging projection $P = \int_K\pi(k)dk$, which is self-adjoint and idempotent; on a general group $P$ commutes with every $\pi(x)$. The intertwining operators of a pair of representations are the adjoint-stable commutant of the integrated algebra, $\pi(L^1(G))' = \pi(G)'$, and for an irreducible $\pi$ the commutant is the scalars, which is Schur's lemma read through the adjoint. The adjoint of a convolution operator and the Plancherel theory are the neighbouring articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\pi(x)^* = \pi(x)^{-1} = \pi(x^{-1})$ | The unitarity condition |
| $\pi(f) = \int_G f(x)\pi(x)\,dx$ | The integrated form |
| $\pi(f)^* = \pi(f^*)$, $\pi(f*g) = \pi(f)\pi(g)$ | The `*`-representation property, every $G$ |
| $\langle\pi(f)\xi,\xi\rangle = \omega_\xi(f)$ | The positive functional of a vector |
| $\mathcal{H}^G$, $P$ | The invariant space and the projection onto it |
| $P = \int_K\pi(k)\,dk$ | The compact averaging projection, $P^* = P = P^2$ |
| $\pi(L^1(G))' = \pi(G)'$ | The commutant of the integrated algebra |
| $T\pi(x) = \rho(x)T\iff T\pi(f) = \rho(f)T$ | Intertwiners |
| $\pi(G)' = \mathbb{C}\cdot1$ | Schur's lemma |

## Further Reading

- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the integrated form, the `*`-representation property and the commutant.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the adjoint, projections, invariants and Schur's lemma.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the unitarity condition, the integrated forms and the averaging over a compact group.
- George W. Mackey, *The Theory of Unitary Group Representations* (University of Chicago Press, 1976), for irreducibility, the commutant and the unitary invariants.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the commutant theorem and the structure of the intertwining operators.
