# __Unitary Operators__

## Introduction

The unitary operators are the operators built from the involution in the simplest possible way: an operator is unitary when its adjoint is its inverse, $U^*=U^{-1}$. The condition says that the adjoint, which is the involution on the operators, and the inverse, which is the operation of the group of invertible operators, agree on the element, and the unitaries are exactly the elements on which the two agree. This article studies the unitary operators from that starting point: the characterisations of unitarity through the involution, the group they form and its two natural topologies, the inner automorphisms by unitaries and their relation to the adjoint, the unitary group of a Hilbert space as a topological group, the standard subgroups of commuting unitaries and of finite-dimensional unitaries, and the spectral theorem of the unitary case. The companion article *Unitary Operators and the Spectral Measure* develops the spectral theory of a single unitary with its measure on the circle and Stone's theorem, and the present article is the group-theoretic and involution-theoretic side of the same class; the self-adjoint part of the involution-built operators is *Self-Adjoint Operators*.

This article fixes the unitary operators and their characterisations through the involution, the unitary group with its algebraic and topological structure, the conjugation action and the inner automorphisms, the classes of unitaries, and the statement of the spectral theorem in the unitary case with its consequences for the group. The spectral measure on the circle and the strongly continuous one-parameter groups are *Unitary Operators and the Spectral Measure*; the adjoint and the operator topologies are *Bounded Operators on a Hilbert Space*; the equivalence of norms and the topological group structure are *Normed and Banach Spaces* and *Topological Groups*; the inner automorphisms and the centre are *The Operators on an Algebra*.

Throughout, $H$ is a complex Hilbert space with inner product linear in the first argument, $B(H)$ is the algebra of bounded operators, $U^*$ is the adjoint, and $U(H)=\{U\in B(H):U^*U=UU^*=I\}$ is the unitary group.

## The Unitary Operators and the Involution

**Theorem (characterisations through the adjoint).** For $U\in B(H)$ the following are equivalent:

(i) $U^*U=UU^*=I$;

(ii) $U$ is invertible with $U^{-1}=U^*$;

(iii) $U$ is an isometry with dense range, hence surjective;

(iv) $U$ preserves the inner product and is surjective;

(v) $U$ is normal and $\sigma(U)\subseteq\mathbb{T}$.

*Proof.* (i) $\Leftrightarrow$ (ii) is the definition of invertibility with the prescribed inverse. (ii) $\Rightarrow$ (iii): $U^*U=I$ makes $U$ an isometry and $UU^*=I$ makes the range dense and closed, hence all of $H$. (iii) $\Rightarrow$ (iv): an isometry preserves the inner product by polarisation, and it is surjective by hypothesis. (iv) $\Rightarrow$ (i): a surjective isometry is injective, so $U$ is bijective and $U^*U=UU^*=I$. (i) $\Leftrightarrow$ (v): a unitary is normal with $\|U\|=1$ and $\|U^{-1}\|=1$, so $|\lambda|=1$ on the spectrum, and conversely a normal operator with spectrum on the circle has $U^*U=I$ by the spectral theorem.

**Proposition (the involution fixes the unitaries as a group).** The unitary group is closed under the adjoint, $(U^*)^*=U$ with $U^*\in U(H)$, it is closed under inverses and products, and $U(H)$ is exactly the set of elements of $B(H)^\times$ on which the involution agrees with the group inverse; the involution restricted to $U(H)$ is a group automorphism of order two.

*Proof.* If $U$ is unitary then $U^*=U^{-1}$ is unitary; the product of unitaries is unitary because $(UV)^*=V^*U^*=V^{-1}U^{-1}=(UV)^{-1}$; the identity $I$ is unitary, so the set is a group. The agreement of the adjoint and the inverse on $U(H)$ is the defining condition, and the involution is then a group homomorphism whose square is the identity.

**Proposition (spectral radius and the norm).** Every unitary has $\|U\|=1$, $\|U^{-1}\|=1$, and $U$ is an extreme point of the unit ball of $B(H)$; the unitaries are the isometries of $H$ onto itself, so $U(H)$ is the group of surjective isometries.

*Proof.* The norm identity is immediate from $U^*U=UU^*=I$; an extreme-point argument or a two-dimensional direct computation shows extremality; the isometry statement is the definition read through the polarisation identity.

## The Unitary Group

**Theorem (the group and its topologies).** $U(H)$ is a group under composition with identity $I$ and inverse $U\mapsto U^*$, and it carries the norm, strong and weak operator topologies, with

$$
\text{norm}\ \subsetneq\ \text{strong}\ =\ \text{weak} .
$$

It is a topological group in each of these topologies, it is compact and Hausdorff in the strong topology, the strong and weak topologies coincide on it, and it is metrisable there when $H$ is separable.

*Proof.* The group axioms are those of composition and the previous proposition. The inclusions of the topologies are the general inclusions on $B(H)$; the coincidence of strong and weak convergence for a net of unitaries is $\|U_\alpha x-Ux\|^2=2\|x\|^2-2\operatorname{Re}\langle U_\alpha x,Ux\rangle$, which vanishes exactly when the scalar products converge. Continuity of multiplication and inversion in the strong topology is the continuity of the operations on the unit ball; compactness is the compactness of the unit ball together with the closedness of $U(H)$, and metrisability is separability.

**Proposition (subgroups of the unitary group).** The central unitary group is $\mathbb{T}I=\{e^{i\theta}I\}$; a family of commuting unitaries generates a commutative subgroup isomorphic to a quotient of a power of the circle, and its closure is a compact group; the stabiliser of a subspace or a vector under the conjugation action is a closed subgroup, and the orbit of a rank-one projection is the projective space of $H$.

*Proof.* The scalars of modulus one are the central unitaries because they are the unitaries commuting with every operator; the commutative subgroup acts as the pointwise multiplication on a common spectral representation, and its closure is compact as a closed subgroup of the compact group. The stabiliser is closed because the action is continuous, and the orbit statement identifies the rank-one projections with the lines of $H$.

**Proposition (finite-dimensional case and the determinant).** For $H=\mathbb{C}^n$ the unitary group is a compact connected Lie group of real dimension $n^2$, the determinant is a homomorphism $U(n)\to\mathbb{T}$ with kernel the special unitary group $SU(n)$, and $U(n)\cong SU(n)\times\mathbb{T}$ up to a finite central subgroup; the centre is $\mathbb{T}I$.

*Proof.* The group is closed and bounded in the matrix space, hence compact, and the exponential of the skew-adjoint matrices fills a neighbourhood of the identity, giving connectivity and the dimension; the determinant has modulus one on unitaries and its kernel is the special unitary group, and the product decomposition is the standard one, with the intersection the $n$-th roots of unity.

## The Conjugation Action and the Inner Automorphisms

**Proposition (conjugation by a unitary is an isometric $*$-automorphism).** For $U\in U(H)$ the map

$$
\iota_U(T)=UTU^*=UTU^{-1}
$$

is an isometric $*$-automorphism of $B(H)$ with norm and Hilbert–Schmidt norm preserved, whose inverse is $\iota_{U^*}$; the map $U\mapsto\iota_U$ is a group homomorphism $U(H)\to\operatorname{Aut}^*(B(H))$ with kernel $\mathbb{T}I$, so the group of inner $*$-automorphisms is $U(H)/\mathbb{T}I$.

*Proof.* The map is multiplicative, preserves the adjoint because $(UTU^*)^*=UT^*U^*$, and is isometric by the isometry of $U$; the composition rule $\iota_U\iota_V=\iota_{UV}$ is associativity; the kernel consists of the unitaries with $UTU^*=T$ for all $T$, which are the central unitaries.

**Proposition (the conjugations that move the self-adjoint part).** The conjugation action of $U(H)$ preserves the order and the cone of positive operators, acts transitively on the rank-one projections and on the unitaries themselves, and its restriction to the self-adjoint part is an isometry of the order-unit space; the fixed points of $\iota_U$ are the operators commuting with $U$.

*Proof.* The $*$-automorphism preserves the positivity and hence the order, transitivity on the projections follows by sending a unit vector to another, and the fixed-point statement is the definition of the commutant.

**Example (the conjugation and the transforms).** The Fourier transform on $L^2(\mathbb{R})$ is a unitary of order four, and its conjugation gives the exchange of the position and frequency multiplications; the operator $U=\Gamma$ of the grading is a unitary with $U^2=I$, and the conjugation by it is the grade involution used throughout the signed operator theory of *The Signed Sandwich on a Hilbert Space*.

## The Spectral Theorem in the Unitary Case

**Theorem (the unitary spectral theorem, for the group's use).** A unitary $U$ is $U=\int_{\mathbb{T}}z\,dE(z)$ for a spectral measure $E$ on the circle, the functional calculus $f\mapsto f(U)$ is an isometric $*$-homomorphism of the bounded Borel functions, and $U^n=\int z^n\,dE(z)$ for every integer $n$, so the one-parameter family $U^n$, $n\in\mathbb{Z}$, is the Fourier transform of the measure.

*Proof.* This is the spectral theorem for a normal operator with spectrum on the circle, of *Self-Adjoint Operators and the Spectral Theorem* and *Unitary Operators and the Spectral Measure*; the statement about the powers is the multiplicativity of the calculus.

**Corollary (the group generated by a unitary).** The closure of the group $\{U^n:n\in\mathbb{Z}\}$ is the compact group generated by the range of $E$; it is isomorphic to a quotient of the circle when $U$ has a cyclic vector, and it is trivial exactly when $U=I$.

*Proof.* The powers of $U$ correspond under the calculus to the powers $z^n$ of the variable, and the closure of the group they generate is the closed subgroup of $\mathbb{T}$ generated by the support of $E$ acting on the cyclic subspace; the triviality statement is the injectivity of the calculus.

**Proposition (the spectral comparison with the self-adjoint case).** Via the Cayley transform a bounded self-adjoint operator $A$ corresponds to the unitary $C(A)=(A-iI)(A+iI)^{-1}$, and the conjugation by $U$ corresponds to the conjugation of the self-adjoint part by the same unitary; hence the inner automorphism groups of the two spectral pictures coincide, and the unitary group is the exponentiated form of the self-adjoint line.

*Proof.* The Cayley transform is a bijection from the self-adjoint operators onto the unitaries avoiding $1$, as in *Self-Adjoint Operators and the Spectral Theorem*, and it intertwines the conjugations by unitaries because it is built from the operator and the identity; the last statement is the exponentiation of the self-adjoint line.

## Summary

A unitary operator is one whose adjoint is its inverse, $U^*U=UU^*=I$; equivalently it is a surjective isometry, equivalently a normal operator with spectrum on the unit circle. The unitary group $U(H)$ is a group under composition closed under the adjoint, its elements are exactly those on which the involution agrees with the group inverse, and the involution restricted to it is a group automorphism of order two; every unitary has norm one and is an extreme point of the unit ball, and the group is the group of surjective isometries of $H$. Under the norm, strong and weak operator topologies the unitary group is a topological group, the strong and weak topologies coincide on it, and it is compact and metrisable in the strong topology for separable $H$; its centre is the circle of scalars, and a commuting family generates a compact commutative subgroup. Conjugation by a unitary is an isometric $*$-automorphism, the assignment $U\mapsto\iota_U$ has kernel $\mathbb{T}I$, and the inner $*$-automorphisms are $U(H)/\mathbb{T}I$; the action preserves the order and is transitive on the rank-one projections. The spectral theorem writes a unitary as the integral of the variable over a spectral measure on the circle, the functional calculus is an isometric $*$-homomorphism with $U^n=\int z^n\,dE$, and the Cayley transform identifies the unitary picture with the self-adjoint one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $U^*U=UU^*=I$ | unitarity |
| $U^{-1}=U^*$ | adjoint equals inverse |
| $U(H)$ | the unitary group |
| $\sigma(U)\subseteq\mathbb{T}$ | spectrum on the unit circle |
| $\|U\|=1$ | norm of a unitary |
| $\iota_U(T)=UTU^*$ | conjugation, an isometric $*$-automorphism |
| $U(H)/\mathbb{T}I$ | the inner $*$-automorphism group |
| $U=\int z\,dE(z)$ | unitary spectral theorem |
| $U^n=\int z^n\,dE$ | powers via the calculus |
| $C(A)=(A-iI)(A+iI)^{-1}$ | Cayley transform linking self-adjoint and unitary |

## Further Reading

- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 2nd ed. 1982), for the unitary operators, their topologies and the extreme-point property.
- John B. Conway, *A Course in Functional Analysis* (Springer, 2nd ed. 1990), for the unitary group, the inner automorphisms and the spectral theorem.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the unitary group of $B(H)$, its topologies and the automorphisms.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for the finite-dimensional unitary and special unitary groups, their centres and the determinant.
- Kôsaku Yosida, *Functional Analysis* (Springer, 6th ed. 1980), for the unitary groups and the representation of the circle.
