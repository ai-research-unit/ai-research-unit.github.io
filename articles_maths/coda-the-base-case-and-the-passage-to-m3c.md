# __Coda: the Base Case and the Passage to $M_3(\mathbb{C})$__

## Introduction

**Order two is the base case of the family $M_n(\mathbb{C})$: everything the series proves in general is visible there in coordinates, and everything that the general theory cannot see is confined to the small numbers that order two makes small, the one-dimensional antisymmetric part, the single rotation plane, the sphere of Hermitian idempotents and the projective line of flags.**

The article collects the shape of the base case, separates the statements that hold at every order from the accidents of order two, records where order three departs from the pattern, and hands the reader to the series on $M_3(\mathbb{C})$. It assumes the whole preceding sequence, in particular *The Frame, the Simple Nilpotent and the Gauge of $M_2(\mathbb{C})$*, *The Polar Decomposition from the Two Halves at $n=2$* and *The Symmetric Space $\mathrm{GL}_2/O(2)$ and Its Complex Twin*.

It follows the biquaternion article *Introduction to the Algebra of Biquaternions* for the same base case in the older language.

## The Shape of the Base Case

**The base case has eight real dimensions, four complex dimensions, two halves in each of the two base fields, and one spectral invariant beyond the trace.**

**Proposition.** The algebra has real dimension eight and complex dimension four; the symmetric and antisymmetric halves have dimensions three and one over the reals, and the Hermitian and anti-Hermitian halves have dimensions four and four.

**Proof.** These are the counts of the independent real and imaginary parts of the four entries, split by the transposition and the conjugate transposition.

**Corollary.** The product rule, the trace, the determinant and the rank determine every spectral statement of the base case.

**Proof.** The characteristic polynomial has degree two, so its two coefficients are the trace and the determinant, and the rank is read from the vanishing of the determinant.

**Corollary.** The Peirce decomposition has two idempotents, four corners and a gauge of one reciprocal rescaling.

**Proof.** The corners of a pair of complementary idempotents are the four blocks of the matrix in the corresponding basis, and the freedom in the choice of the basis is a single rescaling of one block against its partner.

## What Holds at Every Order

**Every statement of the base case that mentions only the trace, the determinant and the bracket extends to all orders without change.**

**Proposition.** For every order the bracket of two symmetric matrices is antisymmetric, the trace form pairs the symmetric half with the antisymmetric half in duality, and the transposition is an involution whose eigenspaces are those halves.

**Proof.** The transpose of a commutator of symmetric matrices is the negative of the commutator, the trace of a product of a symmetric with an antisymmetric matrix vanishes, and the transposition squares to the identity.

**Corollary.** The triangular decomposition, the Peirce decomposition and the corner recursion hold at every order with the same proofs.

**Proof.** The proofs use only the product rule, the trace and the idempotents, none of which depends on the order.

**Corollary.** The polar decomposition, the Cartan decomposition and the identification of the positive cone with a symmetric space hold at every order.

**Proof.** The polar decomposition is proved by the spectral theorem, and the symmetric space statement follows from the decomposition.

## What Is Special about Order Two

**Four accidents of order two are responsible for the simplicity of the base case.**

**Proposition.** The antisymmetric part of order two is one-dimensional, so it is abelian, so every rotation is a rotation in a single plane with a single angle.

**Proof.** An antisymmetric matrix of order two is a multiple of the single unit, and the exponential of a multiple of that unit is a rotation in the plane.

**Corollary.** Every rotation at order two is simple, and its angle is the modulus of the single coordinate.

**Proof.** The rotation plane is the plane orthogonal to the axis of the antisymmetric matrix, and there is only one such plane.

**Corollary.** The Hermitian idempotents form a two-sphere, and the rank-one idempotents form the projective line with a point at infinity.

**Proof.** A Hermitian idempotent of rank one is a projection onto a line, and the lines of the complex plane form the projective line; the Hermitian ones of trace one form the sphere of the Bloch section.

**Proposition.** The positive semidefinite cone is a Lorentz cone, so its section by the trace hyperplane is a ball and its extreme rays form a sphere.

**Proof.** The determinant on the Hermitian half has inertia $(1,3)$, so the cone is Lorentzian.

**Corollary.** The symmetry of the base case is the product of two circles at the level of the maximal torus, and the Weyl group has two elements.

**Proof.** A maximal torus of the unitary group of order two is a product of two circles, and the Weyl group permutes the two eigenvalues.

## Where Order Three Differs

**At order three the antisymmetric part has three dimensions, so it is no longer abelian, and the rotations are no longer all simple.**

**Proposition.** The antisymmetric part of order three has dimension three and is isomorphic to the orthogonal Lie algebra of three-space, whose bracket is the cross product.

**Proof.** An antisymmetric matrix of order three is determined by three coordinates, and the commutator of two such matrices corresponds to the cross product of their coordinate vectors.

**Corollary.** The bracket of two symmetric matrices of order three still lands in the antisymmetric part, but the antisymmetric part is no longer one-dimensional, so the map from the bivectors to the antisymmetric part is an isomorphism rather than a single scalar.

**Proof.** The bracket is antisymmetric, and the dimensions of the bivectors and of the antisymmetric part agree at order three.

**Corollary.** Rotations of order three need not preserve a single plane, because the exponential of a general antisymmetric matrix has three coordinate angles.

**Proof.** An antisymmetric matrix of order three has three independent coordinates, and the exponential depends on all three.

**Proposition.** The positive semidefinite cone of order three is no longer Lorentzian, and its section by the trace hyperplane is no longer a ball.

**Proof.** The determinant on the Hermitian half of order three is a cubic form, not a quadratic one, so the cone is not the cone of a quadratic form.

**Corollary.** The Hermitian idempotents of order three have two ranks, so the space of idempotents is a union of two Grassmannians rather than a single sphere.

**Proof.** An idempotent of order three has rank one or rank two, and the Hermitian projections of each rank form a Grassmannian.

## The Passage

**The base case is the model that the higher orders imitate, with the accidents removed and the ranks multiplied.**

**Proposition.** Every construction of the base case has a counterpart at order three obtained by replacing the two eigenvalues by three, the single antisymmetric coordinate by three coordinates, and the projective line by the flag variety of a plane and a line.

**Proof.** The constructions use the spectral theorem, the idempotents and the Peirce corners, all of which are available at every order with more parameters.

**Corollary.** The reader can pass to order three by keeping the matrix side of the base case and enlarging the index set from two values to three.

**Proof.** The statements of the base case are indexed by the two eigenvalues, and the general statements are indexed by the eigenvalues in the same way.

**Corollary.** The accidents of order two are exactly the statements that fail at order three, so they must be re-examined rather than transplanted.

**Proof.** A statement that uses the one-dimensionality of the antisymmetric part or the Lorentzian nature of the cone has no analogue at order three.

## Summary

The base case is an algebra of real dimension eight with three-dimensional and one-dimensional real halves, four-dimensional complex halves, two eigenvalues and a single reciprocal rescaling in the gauge. Its product rule, trace, determinant and rank govern all of its spectral statements, and its Peirce decomposition has four corners.

The statements that use only the trace, the determinant and the bracket hold at every order, and include the Peirce decomposition, the triangular decomposition, the corner recursion and the polar decomposition. The accidents of order two are the one-dimensional antisymmetric part, the simplicity of every rotation, the Lorentzian cone and the sphere of Hermitian idempotents; at order three each of these fails, and the passage to the next case replaces them by the three-dimensional orthogonal algebra, non-simple rotations, a cubic cone and two Grassmannians of projections.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $n=2$ | the base case |
| $\operatorname{Skew}_2$ | the one-dimensional antisymmetric part |
| $\operatorname{Skew}_3$ | the three-dimensional antisymmetric part of the next case |
| $S^{2}$ | the sphere of Hermitian idempotents at order two |
| $\mathbb{P}^{1}$ | the projective line of flags at order two |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for Peirce decompositions in general.
- Pavel Etingof and others, *Introduction to Representation Theory* (American Mathematical Society, 2011), for the family of matrix algebras.
- [The Frame, the Simple Nilpotent and the Gauge of $M_2(\mathbb{C})$](the-frame-the-simple-nilpotent-and-the-gauge-of-m2c.html), for the frame and its gauge in the base case.
- [The Polar Decomposition from the Two Halves at $n=2$](the-polar-decomposition-from-the-two-halves-at-n-2.html), for the decomposition that generalises.
- [The Matrix Algebra $M_3(\mathbb{C})$](the-matrix-algebra-m3c.html), for the next case of the family.
