
# __The Cone of Positive Functionals__

## Introduction

The **positive functionals** of an ordered involutive algebra are the linear functionals that are Hermitian and nonnegative on the positive cone,

$$
\varphi(a^{*}a)\geq0 \quad \text{for every } a ,
$$

and they form the **dual cone** $A_+^{*}$ of $A_+$ in the space of the Hermitian functionals. Each positive functional satisfies the **Cauchy–Schwarz inequality** $\lvert\varphi(b^{*}a)\rvert^{2}\leq\varphi(a^{*}a)\varphi(b^{*}b)$, which makes the assignment $(a,b)\mapsto\varphi(b^{*}a)$ a positive semidefinite form; consequently $\varphi$ is automatically continuous in the order-unit norm, and its norm is $\varphi(1)$ when the algebra is unital. The **states** are the positive functionals normalised by $\varphi(1) = 1$, and they form a **base** of the dual cone: the map $\varphi\mapsto\varphi/\varphi(1)$ retracts the dual cone onto the state space, which is a **weak-$\ast$ compact convex subset** of the dual, metrisable when the algebra is separable.

The article describes the cone, its base, and its **extreme points**. The extreme points of the state space are the **pure states**, and they are the points at which the order and the representation theory meet: a state is pure exactly when its associated left ideal is maximal, and a pure state is multiplicative when the algebra is commutative, so that the pure states of a commutative involutive algebra are the characters. The **Krein–Milman theorem** gives the states as the closed convex hull of the pure states, and the **faces** of the state space are the annihilators of the closed left ideals, so that the order-theoretic structure of the cone of the functionals mirrors the ideal-theoretic structure of the algebra. This is the content of the article, and it is the reason the states are the correct notion of a geometric point of an involutive algebra.

The positive cone and the Cauchy–Schwarz inequality are *The Positive Cone of an Involutive Algebra*; the Hermitian elements, the order unit and the states as a dual base are *Hermitian Elements and the Order Unit*; the order and the order unit are *Ordered Vector Spaces and the Order Unit*; the compact convex sets, the extreme points and the Krein–Milman theorem are *Compact Convex Sets and the Krein–Milman Theorem*; the faces and the facial structure are *Faces and Exposed Points of a Convex Set*; the ordered involutive algebra is *Ordered Involutive Algebras*; the Hilbert cone and its positivity are *The Hilbert Cone of an Involutive Algebra*; the self-adjoint model is *The Jordan Algebra of Self-Adjoint Elements*; and the $C^{*}$-theory is *Operator Algebras* and *The Gelfand–Naimark Theorem for C\*-Algebras*.

## The Dual Cone

**Definition.** A linear functional $\varphi$ on the involutive algebra is **Hermitian** when $\varphi(a^{*}) = \overline{\varphi(a)}$ and **positive** when $\varphi(a^{*}a)\geq0$ for every $a$; the set of the positive functionals is the **dual cone** $A_+^{*}$. A **state** is a positive functional with $\varphi(1) = 1$.

**Proposition (the dual cone is a cone).** The set $A_+^{*}$ is a convex cone in the space of the Hermitian functionals, closed in the weak-$\ast$ topology; it is **pointed** when the cone $A_+$ generates the Hermitian part, so that a positive functional vanishing on $A_+$ vanishes on the Hermitian part; and it is **generating** in the dual when $A$ is reduced and $1$ is an order unit.

*Proof.* The sum of two positive functionals and a nonnegative multiple of one are positive, so the set is a convex cone; it is the intersection of the weak-$\ast$ closed half-spaces $\{\varphi : \varphi(a^{*}a)\geq0\}$ over the generators of the cone, hence closed; the pointedness and the generation are the order-theoretic statements of the dual of an ordered space with order unit.

**Proposition (continuity and the norm).** Every positive functional satisfies the Cauchy–Schwarz inequality

$$
\lvert\varphi(b^{*}a)\rvert^{2}\leq\varphi(a^{*}a)\,\varphi(b^{*}b)
$$

and hence is continuous; in a unital algebra with the order-unit norm, $\lVert\varphi\rVert = \varphi(1)$ and the positivity of $\varphi$ is equivalent to the bound $\lvert\varphi(a)\rvert\leq\varphi(1)\lVert a\rVert$. In the unital case every positive functional is **self-adjoint**, $\varphi(a^{*}) = \overline{\varphi(a)}$, so the Hermitian hypothesis is redundant.

*Proof.* The inequality is that of *The Positive Cone of an Involutive Algebra*; it gives $\lvert\varphi(a)\rvert^{2}\leq\varphi(1)\varphi(a^{*}a)\leq\varphi(1)^{2}\lVert a\rVert^{2}$ using the order-unit norm, whence the continuity and the norm bound; the reverse bound is $\lvert\varphi(1)\rvert\leq\lVert\varphi\rVert$, and the self-adjointness follows by applying the Cauchy–Schwarz inequality to $a$ and $1$ and comparing the real and imaginary parts.

**Proposition (the states form a base).** The states are the base of the dual cone at the order unit: every nonzero positive functional is a unique positive multiple of a state, the state space

$$
S(A) = \{\varphi\in A_+^{*} : \varphi(1) = 1\}
$$

is convex, and it is compact in the weak-$\ast$ topology and metrisable when $A$ is separable.

*Proof.* The rescaling $\varphi\mapsto\varphi/\varphi(1)$ is well defined and positive because $\varphi(1)>0$ for a nonzero positive functional with the order unit; the uniqueness is the normalisation; the convexity is immediate; the compactness is the Banach–Alaoglu theorem applied to the weak-$\ast$ closed bounded set $\{\lVert\varphi\rVert\leq1\}$, in which the states are cut out by the continuous equation $\varphi(1) = 1$.

## The States and the Order

**Proposition (the states determine the order).** For Hermitian $h,k$,

$$
h\leq k \iff \varphi(h)\leq\varphi(k) \ \text{ for every state } \varphi ,
$$

so the order of the Hermitian part is recovered from the state space, and the order isomorphism classes of unital reduced involutive algebras are determined by the order-theoretic structure of their state spaces.

*Proof.* One direction is the positivity of the states on the cone. Conversely, if $k - h\notin A_+$, then by the Hahn–Banach theorem there is a Hermitian functional $\psi$ with $\psi(k - h)<0$ and $\psi$ bounded by the order unit; adding a large positive multiple of the identity functional makes it positive and a state, and it still separates $h$ and $k$ by construction; this is the separation theorem in the ordered space with order unit.

**Proposition (the states are an order ideal of the dual).** The order on the functionals defined by $\varphi\leq\psi\iff\psi - \varphi\in A_+^{*}$ makes the dual cone an ordered cone, and the states are an order interval $[0,1]$ of the dual; a positive functional $\varphi$ with $\varphi\leq1$ is a state exactly when $\varphi(1) = 1$, and the interval $[0,1]$ of the dual is the set of the **substates**.

*Proof.* The order is the dual order of the cone; the identification is the definition of the states and the substates.

## The Extreme Points

**Definition.** A state $\varphi$ is **pure** when it is an extreme point of the state space $S(A)$, that is, when $\varphi = t\varphi_1 + (1 - t)\varphi_2$ with $\varphi_1,\varphi_2$ states and $0<t<1$ forces $\varphi_1 = \varphi_2 = \varphi$.

**Theorem (Krein–Milman).** The state space is the closed convex hull of its extreme points,

$$
S(A) = \overline{\mathrm{conv}}\ \mathrm{ext}\,S(A) ,
$$

so every state is a weak-$\ast$ limit of convex combinations of pure states; the extreme points are nonempty, and when $S(A)$ is metrisable they form a $G_\delta$ set.

*Proof.* The state space is a compact convex subset of a locally convex space, and the Krein–Milman theorem applies; the nonemptiness of the set of the extreme points is part of that theorem, the description of the set of the extreme points in the metrisable case is the Choquet theory of *Faces and Exposed Points of a Convex Set*.

**Theorem (the pure states and the maximal left ideals).** In a unital C\*-algebra the pure states are exactly the states whose associated left ideals $N_\varphi = \{a : \varphi(a^{*}a) = 0\}$ are maximal; equivalently, the pure states are the states whose Gelfand–Naimark–Segal representation is irreducible, and the equivalence classes of the pure states are the unitary equivalence classes of the irreducible representations.

*Proof.* The Gelfand–Naimark–Segal construction associates to a state $\varphi$ a representation $\pi_\varphi$ with cyclic vector $\xi$ and $N_\varphi$ as its kernel; the representation is irreducible exactly when $N_\varphi$ is maximal, and a state is a convex combination of two states exactly when its representation is a direct sum, so the irreducibility is equivalent to the purity. This is the standard theorem of the theory, and the details belong to *Operator Algebras*.

**Corollary (the commutative case).** When $A$ is a commutative unital C\*-algebra the pure states are exactly the **characters**, the multiplicative functionals; the state space is the set of the probability measures on the Gelfand spectrum $X$ of $A$, and the pure states are the point masses,

$$
\varphi_x(a) = a(x) ,
$$

so that the Gelfand–Naimark theorem identifies $A$ with $C(X)$ and the states with the Radon probability measures on $X$.

*Proof.* A pure state in the commutative case has a maximal left ideal, and the quotient is a field-like quotient which for a commutative C\*-algebra is a character; conversely a character is extreme because it is multiplicative and the multiplicativity forces the purity; the identification of the states with the probability measures is the Riesz representation theorem, and the point masses are extreme among the measures.

**Theorem (the faces are the annihilators of the left ideals).** The faces of the state space are the sets

$$
F_I = \{\varphi\in S(A) : \varphi(a^{*}a) = 0 \ \text{for all } a\in I\}
$$

for the closed left ideals $I$ of $A$; the correspondence reverses inclusions, the extreme points correspond to the maximal left ideals, and the facial structure of $S(A)$ is therefore the ideal lattice of $A$ read in the dual.

*Proof.* A face is determined by the set of the positive elements on which all of its members vanish, which is a closed left ideal by the Cauchy–Schwarz inequality; conversely the annihilator of a left ideal is a face because the vanishing on the generators defines it as an intersection of exposed faces. This is the standard correspondence of the theory.

## Worked Cases

### The Continuous Functions

For $A = C(X,\mathbb{C})$ the positive functionals are the positive Radon measures, the states are the probability measures, the pure states are the point masses, and the facial structure of the state space is the face lattice of the probability simplex, whose faces are the measures supported in the closed subsets of $X$. This is the commutative model, and it shows that the pure states are the "points" of the space.

### The Matrix Algebra

For $A = M_n(\mathbb{C})$ the positive functionals are the positive semidefinite trace functionals, the states are the density matrices $\rho$ with $\rho\geq0$, $\operatorname{tr}\rho = 1$, the pure states are the **rank-one projections**, and every state is a convex combination of these with the coefficients the eigenvalues of $\rho$; the facial structure is the lattice of the subspaces of $\mathbb{C}^{n}$, a face being the set of the states supported in a subspace. This is the finite-dimensional model, and it is the origin of the quantum-mechanical reading of the states.

### The Group Algebra

For $A = \mathbb{C}[G]$ with $g^{*} = g^{-1}$ the positive functionals are the positive-definite forms on the group, the states are the positive-definite functions normalised at the identity, and the pure states are the extreme points of the set of the positive-definite functions, which by the Gelfand–Raikov theory correspond to the irreducible unitary representations. The facial structure of the state space is the ideal lattice of the group algebra, and it is the origin of the theory of the unitary representations.

## Summary

The **positive functionals** of an ordered involutive algebra form the **dual cone** $A_+^{*}$ of the positive cone, a weak-$\ast$ closed convex cone in the space of the Hermitian functionals, satisfying the **Cauchy–Schwarz inequality** and hence continuous; in the unital algebra the norm is $\varphi(1)$ and every positive functional is self-adjoint. The **states** are the positive functionals with $\varphi(1) = 1$; they form the **base** of the dual cone, a weak-$\ast$ **compact convex set**, and they **determine the order** of the Hermitian part. The **extreme points** of the state space are the **pure states**; the state space is the closed convex hull of them by **Krein–Milman**; in a C\*-algebra the pure states are exactly the states with a **maximal left ideal**, equivalently the states with an **irreducible** GNS representation; in the commutative case they are the **characters** and the states are the probability measures; and the **faces** of the state space are the annihilators of the **closed left ideals**, so the facial structure is the ideal lattice of the algebra read in the dual. The positive cone is *The Positive Cone of an Involutive Algebra*; the Hermitian elements and the order unit are *Hermitian Elements and the Order Unit*; the order is *Ordered Vector Spaces and the Order Unit*; the compact convex theory is *Compact Convex Sets and the Krein–Milman Theorem* and *Faces and Exposed Points of a Convex Set*; the ordered involution is *Ordered Involutive Algebras*; the Hilbert cone is *The Hilbert Cone of an Involutive Algebra*; and the C\*-theory is *Operator Algebras* and *The Gelfand–Naimark Theorem for C\*-Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A_+^{*}$ | Dual cone of the positive functionals |
| $\varphi(a^{*}a)\geq0$ | Positivity of a functional |
| $\lvert\varphi(b^{*}a)\rvert^{2}\leq\varphi(a^{*}a)\varphi(b^{*}b)$ | Cauchy–Schwarz inequality |
| $\lVert\varphi\rVert = \varphi(1)$ | Norm of a positive functional |
| $S(A) = \{\varphi\in A_+^{*} : \varphi(1) = 1\}$ | State space, the base of the dual cone |
| $\mathrm{ext}\,S(A)$ | Pure states |
| $S(A) = \overline{\mathrm{conv}}\,\mathrm{ext}\,S(A)$ | Krein–Milman theorem |
| $N_\varphi = \{a : \varphi(a^{*}a) = 0\}$ | Left ideal of a state; maximal for a pure state |
| $F_I$ | Face of the state space, the annihilator of the left ideal $I$ |

## Further Reading

- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the states, the purity and the left ideals.
- Gert K. Pedersen, *C\*-Algebras and their Automorphism Groups* (Academic Press, 1979), for the Gelfand–Naimark–Segal construction and the irreducible representations.
- Shoichiro Sakai, *C\*-Algebras and W\*-Algebras* (Springer, 1971), for the positive functionals, the states and the extreme points.
- Erik M. Alfsen and Frederik W. Shultz, *State Spaces of Operator Algebras* (Birkhäuser, 2001), for the state spaces, their faces and the Jordan-theoretic characterisation.
- Robert R. Phelps, *Lectures on Choquet's Theorem* (Van Nostrand, 1966), for the Krein–Milman theorem, the Choquet theory and the extreme points.
