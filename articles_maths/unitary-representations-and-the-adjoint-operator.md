
# __Unitary Representations and the Adjoint Operator__

## Introduction

A unitary representation is a representation by operators whose adjoint is their inverse, and the whole infinitesimal theory is the statement of that identity in differentiated form: the derived operators $\pi(X)$ are **skew-adjoint**, and after multiplication by $i$ they become the **self-adjoint generators** of the one-parameter groups of the representation. The unitarity condition is therefore a condition on the adjoint operator, and it can be read either on the group, as $\pi(g)^{*} = \pi(g)^{-1}$, or on the algebra, as the skew-adjointness of the generators, or on the enveloping algebra, as the star identity. The self-adjoint generators carry the spectral theory of the representation, and the Casimir element becomes a positive self-adjoint operator.

This article treats unitary representations and the adjoint operator, the unitarity of the representation and the self-adjoint generators. It is the second article of the `- * Operator Theory` group of the category; the invariant forms are *Hermitian Forms on a Lie Algebra*, the star structure of the enveloping algebra is *The Involution on the Enveloping Algebra of a Lie Group*, the representations and their decomposition are *Unitary Representations of a Lie Group*, and the operators built from the adjoint are *The Signed Adjoint Sandwich on a Lie Algebra*, *The Signed Adjoint of the Reflection on a Lie Algebra*, *The Signed Adjoint of the Left Multiplication on a Lie Algebra* and *The Graded Adjoint Action on a Module over a Lie Algebra*, below in this group.

The article assumes the Hilbert space, the bounded operator and its adjoint from *Hilbert Spaces* and *Bounded Operators on a Hilbert Space*, the self-adjoint operator, its spectrum and the spectral theorem from *Self-Adjoint Operators and the Spectral Theorem*, the one-parameter unitary groups and Stone's theorem from *Unitary Operators and the Spectral Measure*, the derived representation of a unitary representation from *Unitary Representations of a Lie Group*, and the invariant Hermitian form and its adjoint from *Hermitian Forms on a Lie Algebra*. The analytic details of the domains and the spectral decomposition are cited from those articles and not repeated; no physics vocabulary occurs and no interpretation of the generators is made.

## The Adjoint Operator

### The Unitarity of the Representation

**Definition.** Let $\mathcal{H}$ be a complex Hilbert space with inner product $\langle\cdot,\cdot\rangle$, linear in the first argument. The **adjoint** of a bounded operator $A$ is the bounded operator $A^{*}$ with

$$
\langle Av, w\rangle = \langle v, A^{*}w\rangle \qquad (v,w\in\mathcal{H}) ,
$$

and $A$ is **unitary** when $A^{*} = A^{-1}$, equivalently when $A$ is surjective and preserves the inner product; $A$ is **self-adjoint** when $A^{*} = A$ and **skew-adjoint** when $A^{*} = -A$.

**Proposition.** A unitary representation is a homomorphism $\pi : G\to U(\mathcal{H})$; equivalently a representation of $G$ by invertible operators with $\pi(g)^{*} = \pi(g)^{-1}$ for every $g$, and equivalently a representation preserving the inner product, $\langle \pi(g)v,\pi(g)w\rangle = \langle v,w\rangle$ for all $g$ and all $v,w$.

*Proof.* The equivalences are immediate from the definition of the adjoint and the invertibility of the operators; the preservation of the inner product is the defining property of the unitary group.

### The Adjoint of the Whole Representation

**Theorem.** Let $\pi$ be a strongly continuous unitary representation. Then

$$
\pi(g)^{*} = \pi(g)^{-1} = \pi(g^{-1}) \qquad (g\in G),
$$

and the map $g\mapsto \pi(g)^{*}$ is again a strongly continuous unitary representation, the **contragredient**; it is equivalent to $\pi$ through the conjugate-linear identification of $\mathcal{H}$ with its dual. The commutant of an irreducible $\pi$ is the scalars, by Schur's lemma.

*Proof.* The first identity is the unitarity; the second representation is the composition of $\pi$ with the inversion, which is continuous and a homomorphism; the equivalence with the contragredient is the standard conjugate-linear isomorphism; Schur's lemma is that of *Unitary Representations of a Lie Group*.

## The Self-Adjoint Generators

### The Derived Representation

**Theorem.** Let $\pi$ be a strongly continuous unitary representation and let $\pi_*$ be its derived representation on the smooth vectors. Then for every $X\in\mathrm{G}$ the operator $\pi_*(X)$ is skew-adjoint on the dense invariant domain $\mathcal{H}^\infty$,

$$
\pi_*(X)^{*} = -\pi_*(X) ,
$$

and the operator $A_X = i\,\pi_*(X)$ is self-adjoint; the map $X\mapsto A_X$ is real-linear and satisfies the commutation relation

$$
[A_X, A_Y] = -i\,A_{[X,Y]} \qquad (X,Y\in\mathrm{G}) .
$$

*Proof.* The skew-adjointness is the derivative at $t = 0$ of the unitarity identity $\pi(\exp tX)^{*}\pi(\exp tX) = \mathrm{id}$, which gives $\pi_*(X)^{*} + \pi_*(X) = 0$; the self-adjointness of $A_X$ follows from that of $i$ times a skew-adjoint operator, and the commutation relation from $[\pi_*(X),\pi_*(Y)] = \pi_*([X,Y])$ multiplied by $i^2 = -1$.

### The One-Parameter Groups

**Theorem (Stone).** For every $X\in\mathrm{G}$ the operators $A_X = i\pi_*(X)$ are the self-adjoint generators of the strongly continuous one-parameter unitary groups

$$
t\longmapsto\pi(\exp tX) = e^{-itA_X} ,
$$

the domain of $A_X$ is the set of $v\in\mathcal{H}$ for which the derivative of the group at $t = 0$ exists, and the spectral theorem for $A_X$ decomposes the representation of the one-parameter subgroup. The common domain of the operators $A_X$ is the intersection of their domains, on which the commutation relations above hold in the sense of the commutator of unbounded operators.

*Proof.* The group $t\mapsto\pi(\exp tX)$ is strongly continuous and unitary, so Stone's theorem of *Unitary Operators and the Spectral Measure* gives a self-adjoint generator $B_X$ with $\pi(\exp tX) = e^{itB_X}$; the derivative at the origin is $\pi_*(X)$, so $B_X = -i\pi_*(X) = A_X$. The domain and the commutation statements are the standard ones for the generators of a representation.

### The Analytic Vectors

**Theorem (Nelson).** The set of analytic vectors of $\pi$ — the vectors $v$ for which the map $g\mapsto\pi(g)v$ is real analytic — is dense in $\mathcal{H}$, each $A_X$ is essentially self-adjoint on the analytic vectors of the enveloping algebra, and the representation is determined on them by the algebraic relations. The Gårding domain, the span of the vectors $\pi(f)v$ with $f\in C_c^\infty(G)$, is dense, contained in $\mathcal{H}^\infty$, and stable under every $\pi_*(u)$, $u\in U(\mathrm{G})$.

*Proof.* The analytic vectors are dense by the analytic-vector theorem of Nelson, which uses the elliptic regularity of the Casimir operator; the essential self-adjointness on them is the commutation theorem for the analytic vectors, and the Gårding domain is dense by the approximate identity of the convolution algebra of *Operators on a Lie Group*. The proofs are in the references.

## The Unitarity Condition

### The Infinitesimal Form

**Theorem.** A representation $\pi$ of $G$ by operators on a dense invariant domain is unitary if and only if the infinitesimal condition

$$
\langle \pi(X)v, w\rangle + \langle v, \pi(X)w\rangle = 0 \qquad (X\in\mathrm{G},\ v,w\in\mathcal{H}^\infty)
$$

holds on the smooth vectors, equivalently if and only if the derived representation is a star-representation of the enveloping algebra, $\pi(u^{\star}) = \pi(u)^{*}$, for the principal anti-automorphism $\sigma(u) = u^{\star}$.

*Proof.* The infinitesimal condition is the differentiated form of the preservation of the inner product and it holds for all smooth vectors exactly when the group action is unitary, by the connectedness of the exponential image and the continuity; the equivalence with the star identity is that both are generated on the first order by $\pi(X)^{*} = -\pi(X)$, and the star of *The Involution on the Enveloping Algebra of a Lie Group* is the adjoint operation.

### The Form and the Representation

**Theorem.** Let $H$ be an invariant Hermitian form on $\mathrm{G}$ with $H([X,Y],Z) + H(Y,[X,Z]) = 0$, and let $\pi$ be a star-representation by skew-adjoint operators. Then the sesquilinear form

$$
\langle v,w\rangle_\pi = \langle v,w\rangle
$$

is invariant under $\pi$, the operators $\pi_*(X)$ are skew-adjoint for it, and the derived representation is a representation by the skew-Hermitian operators attached to $H$; the representation is unitarisable exactly when the form it defines on the module is positive definite.

*Proof.* The invariance of $H$ gives the skew-Hermitian character of the operators $\operatorname{ad}_X$ of the algebra, and the star-representation transports it to the representation on the Hilbert space; the positivity of the invariant form is the passage from the algebraic to the Hilbert structure, and when it fails the representation is only pre-unitary. This is *Hermitian Forms on a Lie Algebra* read on the representation.

## The Casimir Operator

**Theorem.** Let $\Omega = \sum_i X_iX^i$ be the Casimir element of a semisimple algebra, formed with a basis and the dual basis of the Killing form. In a unitary representation the operator

$$
\pi_*(\Omega) = \sum_i\pi_*(X_i)\pi_*(X^i)
$$

is self-adjoint on the smooth vectors and commutes with the representation; for a compact real form the operator $-\pi_*(\Omega) = \sum_i A_{X_i}A_{X^i}$ is positive, and on an irreducible summand the Casimir acts by the scalar $\langle\lambda,\lambda+2\varrho\rangle$.

*Proof.* The Casimir is a central Hermitian element, so its image is self-adjoint and commutes with the derived representation; the positivity is the sum of the squares of the self-adjoint generators $A_{X_i}$, and the scalar value is the eigenvalue formula of *The Casimir Operator of a Lie Group*.

**Corollary.** The self-adjoint operator $-\pi_*(\Omega)$ is the Laplace operator of the representation; it is essentially self-adjoint, its domain contains the Gårding domain, and its spectrum is bounded below when the representation is irreducible and has a lowest weight. The analytic vectors of the theorem of Nelson are exactly the vectors in the domain of all the powers of this operator.

*Proof.* The elliptic regularity of the Laplacian and the spectral theorem give the essential self-adjointness and the lower bound; the identification of the analytic vectors with the domain of the powers is the definition of the analytic vectors for the elliptic operator.

## Examples

### The Vector Group

For $G = \mathbb{R}$ with the representation $\pi(x) = e^{ixt}$ on $L^2(\mathbb{R})$ in the spectral variable, the generator is the self-adjoint multiplication by $t$, the derived representation is $\pi_*(\partial_t) = it$ which is skew-adjoint, and the exponential of the self-adjoint part is the translation; the unitarity condition is the identity $\langle i t v,w\rangle + \langle v, itw\rangle = 0$.

### The Rotation Group

For $G = SU(2)$ with the spin $j$ representation, the derived operators of the basis $E,F,H$ are skew-adjoint, the self-adjoint generators satisfy $[A_E,A_F] = -iA_H$, and the Casimir $-\pi_*(\Omega)$ has the single eigenvalue $j(j+1)$ on the irreducible representation; the spectral decomposition is the standard one, and the analytic vectors are the whole space because the representation is finite dimensional.

### The Real Rank-One Case

For $G = SL_2(\mathbb{R})$ the discrete series representations have a lowest weight vector on which the Casimir acts by the quadratic invariant, and the self-adjoint generators of the compact subgroup have a discrete spectrum; the quadratic form $\langle v,w\rangle_\pi$ is definite for the square-integrable representations and indefinite for the complementary series, which is the criterion of unitarisability of *Unitary Representations of a Lie Group*.

## Summary

A unitary representation of $G$ is a representation by operators with $\pi(g)^{*} = \pi(g)^{-1}$, equivalently one preserving the inner product; its contragredient is the representation composed with the inversion, and Schur's lemma is the commutant statement. The derived representation on the smooth vectors is by **skew-adjoint** operators, $\pi_*(X)^{*} = -\pi_*(X)$, and the operators $A_X = i\pi_*(X)$ are the **self-adjoint generators**, the generators of the one-parameter unitary groups $\pi(\exp tX) = e^{-itA_X}$ by Stone's theorem, satisfying $[A_X,A_Y] = -iA_{[X,Y]}$. The unitarity is read infinitesimally as $\langle\pi(X)v,w\rangle + \langle v,\pi(X)w\rangle = 0$ on the smooth vectors, equivalently as the star identity $\pi(u^{\star}) = \pi(u)^{*}$ in the enveloping algebra, and an invariant Hermitian form on the Lie algebra is the algebraic datum that makes the operators skew-Hermitian, the unitarisability being the positive definiteness of the induced form on the module. The Casimir element has a self-adjoint image commuting with the representation, its negative $-\pi_*(\Omega)$ is the positive Laplace operator of the representation, and its eigenvalue on an irreducible summand is the quadratic invariant. The analytic vectors of Nelson are dense and the Gårding domain is dense and stable, so the algebraic relations of the generators determine the representation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A^{*}$ | the adjoint of a bounded operator |
| $\pi(g)^{*} = \pi(g)^{-1}$ | the unitarity of the representation |
| $\pi_*(X)$ | the derived operator of $X$ on the smooth vectors |
| $\pi_*(X)^{*} = -\pi_*(X)$ | skew-adjointness |
| $A_X = i\pi_*(X)$ | the self-adjoint generator |
| $[A_X,A_Y] = -iA_{[X,Y]}$ | the commutation relation of the generators |
| $\pi(\exp tX) = e^{-itA_X}$ | Stone's theorem for the one-parameter group |
| $\langle\pi(X)v,w\rangle + \langle v,\pi(X)w\rangle = 0$ | the infinitesimal unitarity condition |
| $\pi(u^{\star}) = \pi(u)^{*}$ | the star-representation |
| $-\pi_*(\Omega)$ | the positive Laplace operator of the representation |

## Further Reading

- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the derived representation, the skew-adjoint generators and the Gårding domain.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for Stone's theorem, the self-adjoint generators and the analytic vectors of Nelson.
- Anthony W. Knapp, *Representation Theory of Semisimple Groups* (Princeton University Press, 1986), for the Casimir operator, its positivity and the lowest weight representations.
- Jacques Dixmier and Paul Malliavin, "Factorisations et vecteurs analytiques dans les représentations des groupes de Lie", *Bulletin de la Société Mathématique de France* **106** (1978), for the analytic vectors and the essential self-adjointness.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the infinitesimal unitarity condition and the invariant forms.
