
# __Unitary Representations of a Lie Group__

## Introduction

A **unitary representation** of a Lie group is a strongly continuous action on a Hilbert space by unitary operators, and it is the object whose decomposition is the harmonic analysis of the group; the left regular representation is the model, its decomposition is the Plancherel theorem, and the irreducible summands are the points of the unitary dual. The infinitesimal form is a representation of the Lie algebra by skew-adjoint operators, so that the generators are self-adjoint after multiplication by $i$; the Casimir element becomes a self-adjoint operator whose sign and spectrum are the first invariants of the representation.

This article treats unitary representations of a Lie group, the irreducible decomposition and the Plancherel measure. It is the second article of the `- * Theory` group of the category; the regular representation and its derived form are from *The Regular Representation of a Lie Group*, the Casimir operator is *The Casimir Operator of a Lie Group*, the invariant forms are *Hermitian Forms on a Lie Algebra* and *Unitary Representations and the Adjoint Operator* of the `- * Operator Theory` group, and the detailed analysis is *Harmonic Analysis on Groups*, written and cited.

The article assumes the Hilbert space, the bounded operators and the spectral theorem from *Hilbert Spaces* and *Bounded Operators on a Hilbert Space*, the strongly continuous one-parameter groups and Stone's theorem from *Unitary Operators and the Spectral Measure*, the Haar integral and the convolution from *Locally Compact Groups and Haar Measure* and *The Convolution Algebra $L^1(G)$*, and the representation theory of Lie algebras from *Representations of Lie Algebras*. The Plancherel theory for the general semisimple case uses the invariant integral and the discrete series; its detailed computation belongs to *Harmonic Analysis on Groups*, and the orbit-theoretic description to *Unitary Representations and the Orbit Method* below in the category. No physics vocabulary occurs, and no interpretation of the representations is made.

## Unitary Representations

### The Definition

**Definition.** A **unitary representation** of $G$ on a complex Hilbert space $\mathcal{H}$ is a homomorphism $\pi : G \to U(\mathcal{H})$ into the unitary group such that for every $v \in \mathcal{H}$ the map $g \mapsto \pi(g)v$ is continuous. Two unitary representations are **unitarily equivalent** when there is a unitary $U$ with $U\pi_1(g) = \pi_2(g)U$ for all $g$.

**Definition.** A unitary representation is **irreducible** when it has no non-trivial closed invariant subspace, and **topologically irreducible** when the only closed invariant subspaces are $0$ and $\mathcal{H}$; for unitary representations the two notions coincide, and the representation is a **direct sum** of representations when $\mathcal{H}$ is the orthogonal direct sum of invariant subspaces.

**Definition.** The **unitary dual** $\widehat{G}$ is the set of equivalence classes of irreducible unitary representations of $G$, with the topology of the Fell topology; for a compact group it is discrete, for a vector group it is the dual vector space, and in general it is a measure-theoretic object rather than a manifold.

**Proposition (Schur's lemma).** An irreducible unitary representation has commutant the scalars: every bounded operator intertwining $\pi$ with itself is a scalar, and for a complex Hilbert space every such operator is automatically scalar, the field being algebraically closed.

*Proof.* The commutant of an irreducible representation is a von Neumann algebra; a self-adjoint operator in it has a spectral projection which is an invariant projection, hence $0$ or $\mathrm{id}$, so the operator is a scalar; applying this to the real and imaginary parts gives the general bounded case, and the conclusion is Schur's lemma for unitary representations.

### The Derived Representation

**Theorem (Stone).** Let $g : \mathbb{R} \to U(\mathcal{H})$ be a strongly continuous one-parameter unitary group. Then there is a self-adjoint operator $A$ on a dense domain such that $g(t) = e^{itA}$; conversely every self-adjoint $A$ defines such a group. The operator $A$ is determined by $g$ and is written $A = -i\,g'(0)$ in the sense of the derivative on the domain of analytic vectors.

*Proof.* Stone's theorem is the spectral theorem for the one-parameter group; the map $t\mapsto g(t)$ has a generator $B$ which is skew-adjoint with dense domain, and $A = -iB$ is self-adjoint with the same domain.

**Definition.** For a unitary representation $\pi$ the **derived representation** on the space of smooth vectors $\mathcal{H}^\infty$ is

$$
\pi_* : \mathrm{G} \to \operatorname{End}(\mathcal{H}^\infty), \qquad \pi_*(X)v = \frac{d}{dt}\Big|_{t=0}\pi(\exp tX)v .
$$

**Theorem.** The derived representation is a representation of the Lie algebra by skew-adjoint operators, $\pi_*(X)^* = -\pi_*(X)$ on $\mathcal{H}^\infty$, so that $i\pi_*(X)$ is self-adjoint and $\pi_*$ extends to a representation of the universal enveloping algebra; the space $\mathcal{H}^\infty$ is dense, invariant and carries a Fréchet structure on which every $\pi_*(u)$ is continuous.

*Proof.* The skew-adjointness is the derivative of the equality $\pi(\exp tX)^*\pi(\exp tX) = \mathrm{id}$ at $t = 0$; the bracket identity is the multiplicativity of $\pi$ and the group law; the density and the Fréchet structure are the standard Sobolev structure of a unitary representation, in which a vector is smooth when all the derived operators act, and the extension to $U(\mathrm{G})$ is the universal property.

**Corollary.** The Casimir element of *The Casimir Operator of a Lie Group* acts on $\mathcal{H}^\infty$ by the operator $\pi_*(\Omega) = \sum_i\pi_*(X_i)\pi_*(X^i)$; when the invariant form is such that $\pi_*(\Omega)$ is bounded below, it is essentially self-adjoint and its spectrum is a lowest eigenvalue when the representation is irreducible and has a lowest weight.

*Proof.* The operator is the sum of products of skew-adjoint operators, hence self-adjoint on the common analytic domain when the sum converges; the formula for the eigenvalue on a highest weight vector is that of *The Casimir Operator of a Lie Group*, and the self-adjointness is the standard ellipticity of the Casimir on the smooth vectors.

## The Irreducible Decomposition

### Direct Integrals

**Definition.** A **direct integral** of Hilbert spaces over a measure space $(S,\mu)$, written $\int_S^\oplus \mathcal{H}_s\,d\mu(s)$, is the space of measurable sections $s\mapsto v_s$ with $\int\|v_s\|^2\,d\mu(s) < \infty$, modulo sections vanishing almost everywhere; a representation is a **direct integral** of representations $\pi_s$ when it is the direct integral of the spaces and the action is the measurable field $s\mapsto\pi_s$.

**Theorem (decomposition).** A unitary representation of a separable locally compact group on a separable Hilbert space is a direct integral of irreducible unitary representations,

$$
\pi \cong \int_{\widehat{G}}^\oplus m(\lambda)\,\pi_\lambda\,d\mu(\lambda),
$$

where $\mu$ is a Borel measure on the unitary dual and $m$ is the multiplicity function; the statement is the spectral theorem for the von Neumann algebra generated by the representation, and the decomposition is unique up to the measure class.

*Proof.* The von Neumann algebra generated by the representation is abelian when the representation is multiplicity free, and the general decomposition is the reduction theory of a von Neumann algebra; the Hilbert space is decomposed along the centre of the algebra, whose spectral projections give the decomposition, and the fibres are the irreducible components. The reduction theory is stated and proved in the operator-algebra theory of *Von Neumann Algebras and the Hilbert Algebra Completeness*, and the present article uses its conclusion.

### The Compact Case

**Theorem (Peter--Weyl).** Let $G$ be compact. Then the non-trivial part of the previous decomposition is discrete: every irreducible unitary representation is finite dimensional, the unitary dual is countable, and

$$
L^2(G) \cong \bigoplus_{\pi\in\widehat{G}} V_\pi\otimes V_\pi^{*},
$$

each irreducible representation occurring with multiplicity its dimension $\dim V_\pi$. The matrix coefficients span a dense subspace of $C(G)$, the characters form an orthogonal family, and the orthogonality relations hold with respect to the normalised Haar measure.

*Proof.* The convolution operators by continuous functions are compact and normal on $L^2(G)$, the spectral theorem decomposes the space, and the compactness of the group makes each irreducible representation finite dimensional and gives the discrete sum; the multiplicities and the orthogonality relations are the standard computations, developed in *Harmonic Analysis on Groups*.

### The Plancherel Measure

**Theorem (Plancherel).** For a unimodular locally compact group of type I, the regular representation decomposes as the direct integral of the irreducible unitary representations with respect to a unique measure $\mu_{\mathrm{Pl}}$, the **Plancherel measure**, and for $f \in L^1(G)\cap L^2(G)$,

$$
\int_G|f(g)|^2\,dg = \int_{\widehat{G}}\|\pi_\lambda(f)\|_{\mathrm{HS}}^2\,d\mu_{\mathrm{Pl}}(\lambda),
$$

where $\pi_\lambda(f) = \int_G f(g)\pi_\lambda(g)\,dg$ is the integrated representation and the norm is the Hilbert--Schmidt norm.

*Proof.* The integrated representation $\pi(f)$ is a bounded operator on each irreducible summand, and the Plancherel formula is the computation of the trace of the spectral measure of the convolution algebra; for unimodular groups the algebra is symmetric, the Plancherel measure is the spectral measure of the commutative subalgebra, and the Hilbert--Schmidt norm is the density of the measure. The general theory is *Harmonic Analysis on Groups* and *The Convolution Algebra $L^1(G)$*.

**Corollary (the discrete series and the continuous spectrum).** The Plancherel measure may have atoms, the **discrete series** of the group, and a continuous part; for a semisimple group with a compact Cartan subgroup the discrete series is non-empty, and its formal degrees and characters are computed by the Harish-Chandra theory. The subset of the unitary dual that appears in the support of the Plancherel measure is the **tempered dual**, and the representations outside it are the complementary series and the Langlands quotients.

*Proof.* The atoms of the spectral measure are the irreducible subrepresentations of the regular representation, which are exactly the square-integrable ones, the discrete series; the continuous part is the remainder of the measure, and the dichotomy is the definition of the tempered dual. The detailed classification of the discrete series and the Plancherel density is the analysis of *Harmonic Analysis on Groups*.

## The Direct Integral and the Matrix Coefficients

### The Direct Integral Decomposition

**Definition.** Let $(Z,\mu)$ be a measure space and let $\lambda\mapsto\pi_\lambda$ be a measurable family of unitary representations on the Hilbert spaces $\mathcal{H}_\lambda$. The **direct integral** is the representation on

$$
\mathcal{H} = \int^{\oplus}_{Z}\mathcal{H}_\lambda\,d\mu(\lambda) , \qquad \pi(g) = \int^{\oplus}_{Z}\pi_\lambda(g)\,d\mu(\lambda) ,
$$

the space of the measurable sections $v$ with $\int_Z\lVert v(\lambda)\rVert^2\,d\mu(\lambda)<\infty$ and the action defined pointwise almost everywhere.

**Theorem.** Every unitary representation of a separable locally compact group on a separable Hilbert space is a direct integral of irreducible unitary representations over the unitary dual with a measure class canonically attached to the representation; the decomposition is unique up to the measure-theoretic identifications, the projections onto the invariant subspaces are the spectral projections of the centre of the von Neumann algebra generated by the representation, and the support of the measure is the **spectrum** of the representation.

*Proof.* The von Neumann algebra generated by the representation is the commutant of the representation's commutant, and its centre is abelian; the spectral theorem for the centre decomposes the Hilbert space over its spectrum, the fibres are invariant under the algebra because the centre is central, and the fibres are irreducible by the maximality of the centre. The uniqueness is the uniqueness of the central decomposition, which is the operator-algebra reduction theory of *Von Neumann Algebras and the Hilbert Algebra Completeness*.

### The Matrix Coefficients

**Definition.** The **matrix coefficient** of a unitary representation $\pi$ at the vectors $v,w$ is the function

$$
\pi_{v,w}(g) = \langle\pi(g)v,w\rangle ,
$$

which is bounded, continuous and uniformly continuous in each variable; it is **square-integrable** when it lies in $L^2(G)$ and then its $L^2$-norm is $\lVert v\rVert\lVert w\rVert/d_\pi$ for the formal degree $d_\pi$.

**Theorem.** The square-integrable matrix coefficients are exactly those of the discrete series, and the discrete series is the set of the atoms of the Plancherel measure; the representations with all matrix coefficients in $L^{2+\epsilon}(G)$ for every $\epsilon>0$ form the **tempered dual**, on which the Plancherel measure is continuous, and the tempered dual is the support of the continuous part of the measure.

*Proof.* The Schur orthogonality of the matrix coefficients gives the square-integrability exactly for the representations contributing an atom to the Plancherel formula; the characterisation of the tempered dual by the growth of the matrix coefficients is the standard criterion, and the identification of the two parts of the measure is the Plancherel theorem. The details are in the references.

**Corollary.** The regular representation of $G$ is the direct integral of the irreducible unitary representations with respect to the Plancherel measure, $\pi_{\mathrm{reg}}\cong\int^{\oplus}_{\widehat{G}}\pi_\lambda\,d\mu_{\mathrm{Pl}}(\lambda)$, and its spectrum is the support of the measure; the discrete series contributes the atoms and the tempered dual the continuous part.

*Proof.* The decomposition is the theorem applied to the regular representation, whose von Neumann algebra is the group von Neumann algebra; the Plancherel theorem identifies the measure of the decomposition with the Plancherel measure and therefore the spectrum with its support.

## Examples

### The Vector Group

For $G = \mathbb{R}^n$ the irreducible unitary representations are the characters $\chi_\xi(x) = e^{2\pi i\,\xi\cdot x}$ with $\xi \in \mathbb{R}^n$, the unitary dual is $\mathbb{R}^n$, and the Plancherel measure is Lebesgue measure; the decomposition of the regular representation is the Fourier transform, and the derived representation is $\pi_*(X)v = 2\pi i\,(\xi\cdot X)v$, skew-adjoint because the scalar is imaginary.

### A Compact Group

For $G = SU(2)$ the irreducible unitary representations are the symmetric powers of the defining representation on $\mathbb{C}^2$, indexed by the non-negative half-integers; the Plancherel measure is discrete with weights $(\dim V_\pi)^2$ on the representation $\pi$ up to the normalisation of the Haar measure, and the Casimir acts by the quadratic invariant $\langle\lambda,\lambda+2\varrho\rangle$; the decomposition is the classical spherical harmonic expansion.

### A Semisimple Group of Real Rank One

For $G = SL_2(\mathbb{R})$ the unitary dual consists of the principal series, the discrete series and the complementary series; the Plancherel measure is supported on the principal series with an explicit density, the discrete series contributes atoms, and the representations are realised on spaces of functions on the boundary of the hyperbolic plane, whose geometry belongs to Part IV and whose analysis is developed in *Harmonic Analysis on Groups*.

## Summary

A unitary representation of a Lie group is a strongly continuous homomorphism into the unitary group of a Hilbert space; it is irreducible when it has no non-trivial closed invariant subspace, and Schur's lemma identifies its commutant with the scalars. The derived representation on the smooth vectors is a Lie algebra representation by skew-adjoint operators, so the generators are self-adjoint after multiplication by $i$ by Stone's theorem; it extends to the universal enveloping algebra, and the Casimir element becomes a self-adjoint operator whose eigenvalue on an irreducible summand of highest weight is the quadratic invariant. Every unitary representation of a separable group is a direct integral of irreducible ones over the unitary dual, and the decomposition of the left regular representation is the Plancherel theorem, with a uniquely determined **Plancherel measure** and the formula $\int_G|f|^2 = \int_{\widehat{G}}\|\pi_\lambda(f)\|_{\mathrm{HS}}^2\,d\mu_{\mathrm{Pl}}(\lambda)$. The measure has atoms exactly at the discrete series and a continuous part on the tempered dual; for compact groups the decomposition is discrete and the multiplicities are the dimensions, and for a vector group it is the Fourier transform with Lebesgue measure. The detailed densities and the classification of the discrete series belong to the harmonic analysis of the group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\pi : G \to U(\mathcal{H})$ | a unitary representation |
| $\widehat{G}$ | the unitary dual |
| $\pi_*$ | the derived representation on the smooth vectors |
| $\pi_*(X)^* = -\pi_*(X)$ | skew-adjointness of the generators |
| $i\pi_*(X)$ | the self-adjoint generator, by Stone's theorem |
| $\int_S^\oplus\mathcal{H}_s\,d\mu(s)$ | a direct integral of Hilbert spaces |
| $L^2(G) \cong \bigoplus_\pi V_\pi\otimes V_\pi^*$ | the Peter--Weyl decomposition for compact $G$ |
| $d\mu_{\mathrm{Pl}}$ | the Plancherel measure |
| $\int_G|f|^2 = \int_{\widehat{G}}\|\pi_\lambda(f)\|_{\mathrm{HS}}^2\,d\mu_{\mathrm{Pl}}$ | the Plancherel formula |
| discrete series, tempered dual | the atomic and the continuous part |

## Further Reading

- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the unitary representations, the Peter--Weyl decomposition and the Plancherel theory.
- Anthony W. Knapp, *Representation Theory of Semisimple Groups* (Princeton University Press, 1986), for the discrete series, the tempered dual and the Plancherel density.
- Serge Lang, *$SL_2(\mathbb{R})$* (Springer, 1985), for the explicit unitary dual of the rank-one case.
- Jacques Dixmier, *von Neumann Algebras* (North-Holland, 1981), for the decomposition theory and the reduction of a representation.
- V. S. Varadarajan, *Geometry of Quantum Theory* (Springer, second edition, 1985), for the derived representation, the smooth vectors and Stone's theorem in the representation-theoretic setting.
