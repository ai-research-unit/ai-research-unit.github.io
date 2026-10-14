
# __Quaternion Automorphisms and Derivations__

## Introduction

Two invariants of an algebra are its group of automorphisms and its Lie algebra of derivations, and for the quaternion algebra both can be computed completely: the automorphism group is the rotation group of the imaginary subspace, and the derivation algebra is the imaginary subspace itself under the commutator bracket. Here the ground field is $\mathbb{R}$ throughout, and the algebra is central simple over it.

The article uses *Quaternion Algebra* for the algebra and its centre, *Quaternion Ideals and Simplicity* for the central-simplicity of $\mathbb{H}$ over $\mathbb{R}$, *Quaternion Norm and Invertibility* for the unit group, and *Quaternion Rotations and Reflections* for the identification of the unit sphere with the rotation group.

The results are the case of the standard structure theory of a central simple algebra: over a field $k$, every $k$-algebra automorphism of a finite-dimensional central simple algebra is inner, and every derivation is inner. Those two theorems are cited as standard; the specific computations for $\mathbb{H}$ are shown.

Throughout, $\mathbb{H}$ is the quaternion algebra over $\mathbb{R}$ with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$; a quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with centre $\mathbb{R}_{\mathbb{H}} = \mathbb{R}e_0$, conjugate $\tilde{q}^{\natural}$, and norm $N(\tilde q) = \tilde q\tilde{q}^{\natural}$; the unit group is $\mathbb{H}^{\times} = \mathbb{H}\setminus\{0\}$ and the unit sphere is $Sp(1) = \{\tilde q : N(\tilde q) = 1\}$. The scalar part of a commutator gives $\mathrm{Sc}([\tilde q,\tilde p]) = 0$, so $[\tilde q,\tilde p]\in\operatorname{Im}\mathbb{H}$ always.

## Automorphisms of the Quaternion Algebra

**Definition.** An **automorphism** of $\mathbb{H}$ is a bijective $\mathbb{R}$-linear map $\sigma : \mathbb{H}\to\mathbb{H}$ with $\sigma(\tilde q\tilde p) = \sigma(\tilde q)\sigma(\tilde p)$ and $\sigma(1) = 1$. The automorphisms form a group under composition, written $\operatorname{Aut}_{\mathbb{R}}(\mathbb{H})$.

**Definition.** For a unit $u\in\mathbb{H}$ the map $\iota_u(\tilde q) = u\tilde qu^{-1}$ is the **inner automorphism** determined by $u$. Since the centre is $\mathbb{R}$, one has $\iota_u = \iota_{\lambda u}$ for every non-zero real $\lambda$, so $\iota_u$ depends only on the class of $u$ in $Sp(1)/\{\pm1\}$.

**Proposition.** $\iota_u$ is an automorphism for every unit $u$, the assignment $u\mapsto\iota_u$ is a group homomorphism $Sp(1)\to\operatorname{Aut}_{\mathbb{R}}(\mathbb{H})$, and its kernel is $\{\pm1\}$.

*Proof.* For units $u,v$, $\iota_u\iota_v = \iota_{uv}$, and $\iota_u^{-1} = \iota_{u^{-1}}$, so the assignment is a homomorphism into bijective $\mathbb{R}$-algebra maps. Its kernel consists of the units with $u\tilde qu^{-1} = \tilde q$ for all $\tilde q$, namely the units of the centre $\mathbb{R}$, that is $\{\pm1\}$.

**Theorem (Skolem–Noether for $\mathbb{H}$).** Every $\mathbb{R}$-algebra automorphism of $\mathbb{H}$ is inner. Consequently the homomorphism $Sp(1)\to\operatorname{Aut}_{\mathbb{R}}(\mathbb{H})$ is surjective and

$$
\operatorname{Aut}_{\mathbb{R}}(\mathbb{H})\cong Sp(1)/\{\pm1\} .
$$

*Proof.* The algebra $\mathbb{H}$ is central simple over $\mathbb{R}$ by *Quaternion Ideals and Simplicity*, and the Skolem–Noether theorem states that every $k$-algebra automorphism of a finite-dimensional central simple $k$-algebra is inner; quoting it as standard gives surjectivity of $u\mapsto\iota_u$ onto the automorphism group. The kernel is $\{\pm1\}$ by the proposition, so the first isomorphism theorem gives the displayed isomorphism.

**Remark.** The anti-automorphism $\tilde q\mapsto\tilde q^{\natural}$ is not an automorphism, since it reverses products, and it is not the identity $\iota_u$ for any unit; it is excluded from the automorphism group. There is no second coset of automorphisms here, because the centre of $\mathbb{H}$ is $\mathbb{R}$, which has no non-trivial field automorphism.

## The Automorphism Group as the Rotation Group

**Theorem.** The inner automorphisms are exactly the automorphisms that act on the imaginary subspace as rotations, and there is a canonical isomorphism

$$
\operatorname{Aut}_{\mathbb{R}}(\mathbb{H})\cong SO(3),
$$

the rotation group of the three-dimensional space $\operatorname{Im}\mathbb{H}$.

*Proof.* An automorphism $\sigma$ fixes the centre $\mathbb{R}e_0$ and preserves squares, so it preserves the set $\operatorname{Im}\mathbb{H} = \{\vec q : \vec q^2\in\mathbb{R}e_0,\ \vec q^2\leq0\}$: a quaternion has real square exactly when it is real or pure, and the square is non-positive exactly when it is pure (or zero). On that set the quaternion norm is $N(\vec q) = -\vec q^2$, whence $\sigma$ preserves the quaternion norm. Thus every automorphism restricts to an orthogonal map of $\operatorname{Im}\mathbb{H}$; since by Skolem–Noether every automorphism is inner and every inner automorphism is the adjoint action of a unit, the restriction has determinant $+1$ by *Quaternion Rotations and Reflections*. Conversely every rotation of $\operatorname{Im}\mathbb{H}$ extends to an automorphism — it is the adjoint action of a unit quaternion — and the extension is unique because $\mathbb{H}$ is generated by $\operatorname{Im}\mathbb{H}$. Identifying the cover $Sp(1)\to SO(3)$ with $u\mapsto\iota_u$ gives the isomorphism.

**Corollary.** As a real manifold, $\operatorname{Aut}_{\mathbb{R}}(\mathbb{H})$ is diffeomorphic to the projective space $\mathbb{RP}^3$ and has dimension $3$; it is connected and compact, and it is isomorphic to the group of orientation-preserving isometries of $\operatorname{Im}\mathbb{H}$ fixing the origin.

*Proof.* $Sp(1)/\{\pm1\}\cong S^3/\{\pm1\}\cong\mathbb{RP}^3$, of dimension three; $SO(3)$ is connected and compact.

**Example.** For $u = e_1$ the inner automorphism $\iota_{e_1}$ fixes $e_1$ and the centre and reverses the signs of $e_2$ and $e_3$: indeed $e_1e_2e_1^{-1} = -(e_1e_2)e_1 = -e_3e_1 = -e_2$, using $e_1e_2 = e_3$ and $e_3e_1 = e_2$. It is the half-turn about the axis $e_1$.

**Remark.** The automorphisms of order two are exactly the halfturns about the axes. An inner automorphism $\iota_u$ satisfies $\iota_u^2 = \iota_{u^2} = \mathrm{id}$ exactly when $u^2$ is real, that is when $u$ is real or pure imaginary; a real $u$ gives the identity, and a pure $u$ is $u = t\nu$ with $t\neq0$ real and $\nu$ a unit vector, giving $\iota_u = \iota_\nu$, which fixes the plane $\operatorname{span}(e_0,\nu)$ and is the half-turn about the axis line $\mathbb{R}\nu$. There is thus one non-trivial automorphism of order two for each axis line of $\operatorname{Im}\mathbb{H}$, and they are the involutions of *Quaternion Involutions and Projections*.

## Derivations of the Quaternion Algebra

**Definition.** A **derivation** of $\mathbb{H}$ is an $\mathbb{R}$-linear map $D : \mathbb{H}\to\mathbb{H}$ satisfying the Leibniz rule $D(\tilde q\tilde p) = D(\tilde q)\tilde p+\tilde q D(\tilde p)$ for all $\tilde q,\tilde p$. The derivations form a real vector space $\operatorname{Der}_{\mathbb{R}}(\mathbb{H})$, a Lie algebra under the commutator bracket $[D_1,D_2] = D_1D_2-D_2D_1$.

**Proposition.** Every derivation annihilates $1$ and maps the centre into itself.

*Proof.* $D(1) = D(1\cdot1) = 2D(1)$, so $D(1) = 0$; if $c$ is central then $D(c)\tilde q = D(c\tilde q)-cD(\tilde q) = D(\tilde q c)-D(\tilde q)c = \tilde q D(c)$, so $D(c)$ is central.

**Definition.** For $a\in\mathbb{H}$ the **inner derivation** determined by $a$ is $\operatorname{ad}_a(\tilde q) = a\tilde q-\tilde q a = [a,\tilde q]$.

**Proposition.** $\operatorname{ad}_a$ is a derivation for every $a$, the map $\operatorname{ad} : \mathbb{H}\to\operatorname{Der}_{\mathbb{R}}(\mathbb{H})$ is $\mathbb{R}$-linear with kernel the centre $\mathbb{R}e_0$, and $[\operatorname{ad}_a,\operatorname{ad}_b] = \operatorname{ad}_{[a,b]}$.

*Proof.* The Jacobi identity in the form $[a,[\tilde q,\tilde p]] = [[a,\tilde q],\tilde p]+[\tilde q,[a,\tilde p]]$ is exactly the Leibniz rule for $\operatorname{ad}_a$; linearity is clear; $\operatorname{ad}_a = 0$ iff $a$ commutes with every quaternion, iff $a$ is central. The bracket identity is the Jacobi identity again.

**Theorem.** Every derivation of $\mathbb{H}$ is inner, so there is an isomorphism

$$
\operatorname{Der}_{\mathbb{R}}(\mathbb{H})\cong\mathbb{H}/\mathbb{R}e_0\cong\operatorname{Im}\mathbb{H},
$$

of real vector spaces and of Lie algebras, the bracket on the right being $[\vec q,\vec p] = 2(\vec q\times\vec p)$.

*Proof.* For a finite-dimensional central simple algebra over a field, every derivation is inner; quoting this as standard and applying it to $\mathbb{H}$, the map $\operatorname{ad}$ is surjective, and its kernel is the centre, so it induces the first isomorphism. A commutator is pure, and the space $\mathbb{H}/\mathbb{R}e_0$ is identified with the pure quaternions $\operatorname{Im}\mathbb{H}$; the bracket identity of the proposition becomes $[\vec q,\vec p] = \vec q\vec p-\vec p\vec q = 2(\vec q\times\vec p)$ for pure quaternions by the product rule $\vec p\vec q = -\langle\vec p,\vec q\rangle+\vec p\times\vec q$.

**Corollary.** $\operatorname{Der}_{\mathbb{R}}(\mathbb{H})$ has dimension $3$, with basis $\{D_1,D_2,D_3\}$, $D_k = \tfrac12\operatorname{ad}_{e_k}$, and the structure constants

$$
[D_1,D_2] = D_3, \qquad [D_2,D_3] = D_1, \qquad [D_3,D_1] = D_2 .
$$

*Proof.* The three inner derivations span $\operatorname{Im}\mathbb{H}/\mathbb{R}e_0$ modulo the centre, which is three-dimensional; the brackets follow from $[e_1,e_2] = 2e_3$, $[e_2,e_3] = 2e_1$, $[e_3,e_1] = 2e_2$ and $D_k = \tfrac12\operatorname{ad}_{e_k}$.

**Example.** $D_1 = \tfrac12\operatorname{ad}_{e_1}$ vanishes on $e_1$ and acts by $D_1(e_2) = e_3$, $D_1(e_3) = -e_2$: indeed $\tfrac12(e_1e_2-e_2e_1) = \tfrac12(e_3+e_3) = e_3$ and $\tfrac12(e_1e_3-e_3e_1) = \tfrac12(-e_2-e_2) = -e_2$. It is the infinitesimal generator of the half-turn about $e_1$.

## The Lie Algebra Statement

**Theorem.** The derivation Lie algebra is the orthogonal Lie algebra of the vector subspace,

$$
\operatorname{Der}_{\mathbb{R}}(\mathbb{H})\cong\operatorname{Im}\mathbb{H}\cong\mathrm{SO}(3)\cong\mathrm{SU}(2),
$$

and it is the Lie algebra of the automorphism group: $\operatorname{Lie}\operatorname{Aut}_{\mathbb{R}}(\mathbb{H}) = \operatorname{Der}_{\mathbb{R}}(\mathbb{H})$.

*Proof.* With the bracket $[\vec q,\vec p] = 2(\vec q\times\vec p)$ the vector subspace is the cross-product Lie algebra, isomorphic to $\mathrm{SO}(3)$, equivalently to $\mathrm{SU}(2)$; the two are isomorphic as real Lie algebras. The exponential identity $\exp(t\operatorname{ad}_a)(\tilde q) = e^{ta}\,\tilde q\,e^{-ta} = \iota_{e^{ta}}(\tilde q)$ holds by the standard series computation, so every inner derivation integrates to an inner automorphism and the Lie functor applied to $\operatorname{Aut}_{\mathbb{R}}(\mathbb{H})\cong SO(3)$ recovers the derivation algebra.

**Proposition.** Every element of $\operatorname{Im}\mathbb{H}$ gives an inner derivation, and $\operatorname{ad}_a$ depends only on the class of $a$ modulo the centre; the exponential of a derivation acts on the imaginary subspace as the rotation generated by the cross-product field of the corresponding vector.

*Proof.* The dependence only on the class modulo the centre is the kernel of $\operatorname{ad}$; the exponential statement is the identity quoted in the theorem.

## Summary

Every $\mathbb{R}$-algebra automorphism of the quaternion algebra is inner, by Skolem–Noether applied to the central simple algebra $\mathbb{H}$, and the inner automorphisms form the group $Sp(1)/\{\pm1\}\cong SO(3)$ of rotations of the imaginary subspace; the group is connected and compact, diffeomorphic to $\mathbb{RP}^3$, of dimension three, and the anti-automorphism of quaternion conjugation is not among its elements. There is no further coset of automorphisms, because the centre $\mathbb{R}$ has no non-trivial automorphism.

Every derivation of $\mathbb{H}$ is inner, so $\operatorname{Der}_{\mathbb{R}}(\mathbb{H})\cong\mathbb{H}/\mathbb{R}e_0\cong\operatorname{Im}\mathbb{H}$, a three-dimensional real Lie algebra with basis $D_k = \tfrac12\operatorname{ad}_{e_k}$ and brackets $[D_1,D_2] = D_3$ and cyclic; under the bracket $[\vec q,\vec p] = 2(\vec q\times\vec p)$ it is $\mathrm{SO}(3)\cong\mathrm{SU}(2)$, and $\exp(t\operatorname{ad}_a) = \iota_{e^{ta}}$ identifies it as the Lie algebra of the automorphism group.

The definite norm of $\mathbb{H}$ is what keeps its two groups compact, and the smallness of its centre leaves no further coset of automorphisms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra, central simple over $\mathbb{R}$ |
| $e_0 = 1, e_1, e_2, e_3$ | Basis, $e_k^2 = -e_0$ |
| ${}^{\natural}$ | Quaternion conjugation, an anti-automorphism, not in $\operatorname{Aut}$ |
| $\mathbb{R}_{\mathbb{H}} = \mathbb{R}e_0$ | Centre; kernel of every derivation |
| $Sp(1) = \{\tilde q : N(\tilde q) = 1\}$ | Unit quaternions |
| $\iota_u(\tilde q) = u\tilde qu^{-1}$ | Inner automorphism determined by the unit $u$ |
| $\operatorname{Aut}_{\mathbb{R}}(\mathbb{H})\cong Sp(1)/\{\pm1\}\cong SO(3)$ | Automorphism group, $\cong\mathbb{RP}^3$ |
| $\operatorname{ad}_a(\tilde q) = [a,\tilde q]$ | Inner derivation determined by $a$ |
| $\operatorname{Der}_{\mathbb{R}}(\mathbb{H})\cong\operatorname{Im}\mathbb{H}$ | Derivation algebra, dimension $3$ |
| $D_k = \tfrac12\operatorname{ad}_{e_k}$ | Basis with $[D_1,D_2] = D_3$ and cyclic |
| $[\vec q,\vec p] = 2(\vec q\times\vec p)$ | Bracket on $\operatorname{Im}\mathbb{H}$ |
| $\mathrm{SO}(3)\cong\mathrm{SU}(2)$ | Orthogonal and special unitary Lie algebras |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Skolem–Noether theorem and inner derivations of central simple algebras.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for automorphisms of simple rings and the inner derivation theorem.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for derivations of associative algebras and their Lie algebra structure.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the algebra automorphisms of quaternion algebras and their relations to rotations.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2nd ed. 2015), for the exponential map and the Lie algebra of a matrix group.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the identification of the imaginary subspace with $\mathrm{SO}(3)$.
