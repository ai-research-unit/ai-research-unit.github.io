# __Unitary Operators and the Spectral Measure__

## Introduction

A unitary operator is a surjective isometry, equivalently an operator with $U^*U=UU^*=I$, and its spectrum lies on the unit circle; a unitary is the operator form of a symmetry of the Hilbert space. The spectral theorem for a unitary is the spectral theorem for a normal operator read on the circle: there is a projection-valued measure $E$ on the Borel subsets of the circle with $U=\int z\,dE(z)$, and the functional calculus is the calculus of bounded Borel functions on the circle. The analytic content beyond the self-adjoint case is the link with dynamics: a strongly continuous one-parameter group of unitaries has a self-adjoint generator, and **Stone's theorem** identifies the group with $e^{itA}$; the Cayley transform connects the two spectral theories by a Möbius map and makes the self-adjoint spectral theorem and the unitary one two readings of a single fact.

This article fixes the unitary operators and their spectra, the unitary group with its topologies, the spectral theorem for unitaries and its functional calculus, Stone's theorem with the generator, and the Cayley transform connecting the two cases. The self-adjoint case is *Self-Adjoint Operators and the Spectral Theorem*; the multiplication model of the spectral theorem is *The Spectral Operator*; the operator topologies are *Bounded Operators on a Hilbert Space*; the one-parameter semigroups and their generators are *Dirichlet Forms and the Hermitian Dirichlet Principle*, where the contraction semigroup is treated. The Hilbert-space background is *Hilbert Spaces*, and the integration is *Measure Theory and Integration*.

Throughout, $H$ is a complex Hilbert space with inner product linear in the first argument, $U\in B(H)$ is bounded, $U^*$ is its adjoint, and $\mathbb{T}=\{z\in\mathbb{C}:|z|=1\}$ is the unit circle. The **unitary group** is $U(H)=\{U:U^*U=UU^*=I\}$, and the spectral measure of a unitary is a projection-valued measure on the Borel subsets of $\mathbb{T}$.

## Unitary Operators

**Definition.** $U\in B(H)$ is **unitary** if $U^*U=UU^*=I$, equivalently if it is an isometric linear bijection, equivalently if $\langle Ux,Uy\rangle=\langle x,y\rangle$ for all $x,y$.

**Proposition (characterisation).** For $U\in B(H)$ the following are equivalent:

(i) $U$ is unitary;

(ii) $U$ is an isometry and surjective;

(iii) $U^*$ is unitary and $U^{-1}=U^*$;

(iv) $U$ is normal and $\sigma(U)\subseteq\mathbb{T}$.

*Proof.* An isometry is injective and its range is closed; surjectivity makes it a bijection with $U^*U=UU^*=I$, giving (i) $\iff$ (ii). The inverse of a unitary is its adjoint, whence (iii). A unitary is normal, and its spectrum lies on the unit circle because $\|U\|=1$ and $\|U^{-1}\|=1$ give $|\lambda|\le1$ and $|\lambda^{-1}|\le1$ for $\lambda\in\sigma(U)$; conversely a normal operator with spectrum on the circle has $U^*U=I$ by the functional calculus.

**Proposition (the unitary group is a group of isometries).** The unitaries form a group under composition, closed under the adjoint, $U(H)$; the map $U\mapsto U^{-1}=U^*$ is a group antiautomorphism, and every unitary is an isometry of $H$ onto itself, so $U(H)$ is a subgroup of the isometry group of $H$ consisting of the surjective isometries.

*Proof.* The product of two unitaries is unitary and the inverse of a unitary is unitary; the group axioms are those of composition; the isometry statement is the definition.

**Proposition (the topologies of the unitary group).** The unitary group carries the norm, strong operator and weak operator topologies, and

$$
\text{norm}\ \subsetneq\ \text{SOT}\ \subsetneq\ \text{WOT}
$$

with the SOT and WOT coinciding on the unitary group; it is SOT- and WOT-compact, so $U(H)$ is a compact Hausdorff topological group in the strong topology, and it is metrisable there when $H$ is separable.

*Proof.* On the unitary group strong convergence implies weak convergence and the converse holds because $\|U_\alpha x-Ux\|^2=2\|x\|^2-2\operatorname{Re}\langle U_\alpha x,Ux\rangle$; compactness is the compactness of the unit ball of $B(H)$ together with the closedness of the group, by the continuity of the multiplication and the adjoint; metrisability is the separability.

## The Spectral Theorem for Unitaries

**Theorem (spectral theorem for a unitary).** For every unitary $U$ there is a spectral measure $E$ on the Borel subsets of $\mathbb{T}$ with

$$
U=\int_{\mathbb{T}}z\,dE(z),
$$

and the support of $E$ is $\sigma(U)\subseteq\mathbb{T}$; for every bounded Borel function $f$ on $\mathbb{T}$ the operator $f(U)=\int f\,dE$ is bounded with $\|f(U)\|=\sup_{z\in\mathbb{T}}|f(z)|$, the map $f\mapsto f(U)$ is an isometric $*$-homomorphism, and $U$ is unitarily equivalent to a multiplication by the independent variable on a direct sum of $L^2(\mathbb{T},\mu_j)$.

*Proof.* The unitary is normal with spectrum on the circle, so the normal spectral theorem of *Self-Adjoint Operators and the Spectral Theorem* applies verbatim, with the plane replaced by the circle; the multiplication model is the spectrum-as-multiplication statement of *The Spectral Operator*.

**Proposition (the functional calculus on the circle).** For $f\in L^\infty(\mathbb{T})$ the operator $f(U)$ is defined, the calculus is continuous for the weak operator topology on bounded sets, it carries the Fourier monomials $z^n$ to $U^n$ for $n\in\mathbb{Z}$, and the kernel of the calculus is the functions vanishing on $\sigma(U)$.

*Proof.* The calculus is the integral against $E$; the monomials are computed by the multiplicativity of the measure, $z^n\mapsto U^n$, and $z^{-n}\mapsto U^{-n}=(U^*)^n$; the kernel is the vanishing of $E$ off the support.

**Corollary (spectral mapping and eigenvalues).** $\sigma(f(U))=f(\sigma(U))$ for continuous $f$, the point spectrum of $U$ is the set of atoms of $E$, and an eigenvalue $\lambda$ has eigenspace $E(\{\lambda\})H$.

*Proof.* The spectral mapping theorem for the calculus and the identification of atoms with eigenvalues are the same as in the self-adjoint case, applied on the circle.

## Stone's Theorem and One-Parameter Groups

**Definition.** A **strongly continuous one-parameter unitary group** is a map $t\mapsto U(t)$ from $\mathbb{R}$ to $U(H)$ with $U(s+t)=U(s)U(t)$, $U(0)=I$, and $U(t)x\to x$ as $t\to0$ for every $x$.

**Theorem (Stone).** For every strongly continuous one-parameter unitary group $t\mapsto U(t)$ there is a self-adjoint operator $A$, generally unbounded, with

$$
U(t)=e^{itA}\quad(t\in\mathbb{R}),
$$

and $A$ is the generator of the group, determined by $A=\lim_{t\to0}(U(t)-I)/it$ on its domain;

$$
D(A)=\Bigl\{x:\lim_{t\to0}\frac{U(t)x-x}{it}\ \text{exists}\Bigr\}.
$$

Conversely every self-adjoint $A$ defines a strongly continuous one-parameter unitary group by the formula.

*Proof.* The spectral theorem for the unitary $U(t)$ furnishes the calculus, and the group law $U(s+t)=U(s)U(t)$ forces the spectrum of $U(t)$ to move additively with $t$; writing the spectral variable as $e^{it\lambda}$ assembles the measures into a single spectral measure of a self-adjoint $A$ whose calculus is the group; conversely the spectral theorem for a self-adjoint $A$ makes $e^{itA}$ a strongly continuous unitary group, and the two constructions are inverse.

**Proposition (the generator and the functional calculus).** The generator $A$ is self-adjoint and satisfies $U(t)=e^{itA}$ in the sense of the Borel calculus; it commutes with every $U(t)$, and $A$ is bounded exactly when $t\mapsto U(t)$ is norm-continuous, in which case the group is uniformly continuous and $U(t)$ is entire in $t$.

*Proof.* The commutativity is the statement that $A$ is the generator of the group, by the multiplicativity of the calculus; boundedness of $A$ makes $e^{itA}$ norm-continuous with $\|e^{itA}-I\|\le|t|\|A\|e^{|t|\|A\|}$, and conversely norm-continuity forces the group to be differentiable at $0$ in norm, which makes the generator bounded.

**Example (the translation group and the rotation group).** On $L^2(\mathbb{R})$ the group $U(t)f(x)=f(x-t)$ is unitary and strongly continuous with generator $A=i\,d/dx$; on $L^2(\mathbb{T})$ the group $U(t)f(\zeta)=f(e^{-it}\zeta)$ has generator the dilation by the rotation, whose spectrum is $\mathbb{Z}$ and whose spectral measure is atomic at the Fourier modes. These are the two standard pictures in which Stone's theorem is the statement that a continuous symmetry has an infinitesimal generator.

**Example (the exponential of a self-adjoint operator).** For a self-adjoint $A$ the family $U(t)=e^{-itA}$ is a strongly continuous one-parameter unitary group, and the differential equation $du/dt=-iAu$ is the differential form of Stone's theorem; the self-adjointness of the generator is exactly what makes the group unitary, and the functional calculus turns the equation into the statement that $u(t)=U(t)u(0)$ solves it for every $u(0)$ in the domain of $A$.

## The Cayley Transform

**Proposition (the transform links the two spectra).** The **Cayley transform** $C(A)=(A-iI)(A+iI)^{-1}$ carries a bounded self-adjoint $A$ to a unitary $C(A)$ with $1\notin\sigma(C(A))$ and inverts to

$$
A=i(I+C(A))(I-C(A))^{-1},
$$

so the bounded self-adjoint operators are in bijection with the unitaries avoiding the point $1$; the map is continuous in the norm topology and its inverse is continuous.

*Proof.* The transform is the Möbius map $\lambda\mapsto(\lambda-i)/(\lambda+i)$ applied in the functional calculus, so it carries the real line to the circle and $1$ is the image of infinity, hence avoided; the inverse is the inverse Möbius map, and continuity is the continuity of the operations.

**Remark (why the two spectral theorems agree).** The Cayley transform sends the spectral measure of $A$ on the line to the spectral measure of $C(A)$ on the circle by the Möbius substitution, so the self-adjoint spectral theorem and the unitary spectral theorem are the same theorem read through one substitution of variable; Stone's theorem is the form this identity takes when the substitution is the exponential $\lambda\mapsto e^{it\lambda}$, and the unbounded self-adjoint operators correspond to the unitaries together with the choice of the point at infinity.

## Summary

A unitary operator is a surjective isometry, equivalently an operator with $U^*U=UU^*=I$, and it has spectrum on the unit circle; the unitaries form a compact topological group under the strong operator topology, which coincides with the weak operator topology there. The spectral theorem gives a projection-valued measure $E$ on the circle with $U=\int z\,dE(z)$, the functional calculus $f\mapsto f(U)=\int f\,dE$ is an isometric $*$-homomorphism sending $z^n$ to $U^n$, the spectrum is the support of $E$ and the point spectrum is the atomic part, and $U$ is unitarily equivalent to a multiplication by the variable on a direct sum of $L^2$ spaces on the circle. Stone's theorem identifies the strongly continuous one-parameter unitary groups with the self-adjoint operators through $U(t)=e^{itA}$, the generator being recovered as the derivative at the origin on its domain, so a continuous symmetry of a Hilbert space has an infinitesimal generator; the Cayley transform $C(A)=(A-iI)(A+iI)^{-1}$ is the Möbius substitution that carries the self-adjoint spectral measure on the line to the unitary spectral measure on the circle, and through it the two theorems are one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $U^*U=UU^*=I$ | unitarity |
| $U(H)$ | the unitary group, compact in the strong topology |
| $\sigma(U)\subseteq\mathbb{T}$ | spectrum on the unit circle |
| $U=\int_{\mathbb{T}}z\,dE(z)$ | spectral theorem for a unitary |
| $f(U)=\int f\,dE$ | functional calculus on the circle |
| $z^n\mapsto U^n$ | the calculus carries the Fourier monomials |
| $U(t)$ | strongly continuous one-parameter unitary group |
| $U(t)=e^{itA}$ | Stone's theorem |
| $A=\lim_{t\to0}(U(t)-I)/it$ | generator of the group |
| $C(A)=(A-iI)(A+iI)^{-1}$ | Cayley transform, links self-adjoint and unitary |

## Further Reading

- Marshall H. Stone, "On One-Parameter Unitary Groups in Hilbert Space", *Annals of Mathematics* **33** (1932), 643–648, for the original theorem.
- John B. Conway, *A Course in Functional Analysis* (Springer, 2nd ed. 1990), for the unitary spectral theorem and the Cayley transform.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for Stone's theorem and the generator of a unitary group.
- Paul R. Halmos, *Introduction to Hilbert Space* (Chelsea, 2nd ed. 1957), for the spectral theory of the unitary operator.
- Kôsaku Yosida, *Functional Analysis* (Springer, 6th ed. 1980), for the semigroups, their generators and the Hille–Yosida theory.
