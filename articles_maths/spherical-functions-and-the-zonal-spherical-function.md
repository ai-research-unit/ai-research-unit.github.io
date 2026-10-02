
# __Spherical Functions and the Zonal Spherical Function__

## Introduction

When a compact group acts on a group and the algebra of the invariant functions happens to be commutative, the harmonic analysis of the pair collapses to a theory of functions of one variable: the characters of that commutative algebra are the spherical functions, and the one attached to an irreducible representation with an invariant vector is the zonal spherical function, the matrix coefficient of that vector. The decomposition of the invariant $L^2$ space becomes a decomposition in a single spectral parameter, and the transform is an ordinary Gelfand transform of a commutative Banach algebra. This article fixes the Gelfand pair, defines the spherical and the zonal spherical functions, proves the correspondence between them, and states the decomposition and the spherical transform with its involution.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the algebra $L^1(G)$, its involution and its convolution from *The Convolution Algebra $L^1(G)$*; the involution, the positive cone and the positive functionals from *The Group Algebra as an Involutive Algebra*; the positive definite functions and the GNS construction from *Positive Definite Functions and the Gelfand–Raikov Theorem*, immediately preceding; the Haar measure on a compact group, the characters, the orthogonality relations and the duality from *Analysis on Compact Groups* and *The Peter–Weyl Theorem*; the irreducible unitary representations, the unitary dual and the multiplicity theory from *Noncommutative Harmonic Analysis*; the commutative Banach algebras, their characters and the Gelfand transform from *Operator Algebras*, and the abstract Gelfand theory from *Commutative Banach Algebras*; and the bounded operators and the `*`-representations from *Operator Algebras*. The Plancherel measure on the spherical dual is *Unitary Representations and the Plancherel Theorem*, below; the induced representations and the Mackey theory are *Induced Representations of Locally Compact Groups* and *Mackey Theory*, which are not used; the Hermitian forms attached to the unitary representations are *Hermitian Forms and the Group Algebra*, later in this group.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$ and modular function $\Delta$, and $K\leq G$ is a compact subgroup with normalised Haar measure $dk$, $\int_K dk = 1$. A function on $G$ is **bi-$K$-invariant** when $f(k_1xk_2) = f(x)$ for all $k_1,k_2\in K$; the space of bi-$K$-invariant elements of $L^1(G)$ is written $L^1(K\backslash G/K)$, and it is a closed subalgebra of $L^1(G)$ for convolution. The pair $(G,K)$ is a **Gelfand pair** when this subalgebra is commutative. A **spherical function** is a continuous bi-$K$-invariant function $\omega\ne0$ with

$$
\int_K \omega(xky)\,dk = \omega(x)\,\omega(y) \qquad (x,y\in G) ;
$$

the **spherical dual** $\operatorname{Irr}(G,K)$ is the set of irreducible unitary representations $\pi$ of $G$ with $\mathcal{H}_\pi^K\ne0$.

## The Invariant Algebra

**Proposition (the subalgebra).** The space $L^1(K\backslash G/K)$ of bi-$K$-invariant elements of $L^1(G)$ is a closed subalgebra of $L^1(G)$ under convolution, and it contains a normalised approximate identity consisting of bi-$K$-invariant functions.

**Proof.** Bi-invariance is preserved by convolution because $K$ is a subgroup and $dk$ is invariant: if $f,h$ are bi-$K$-invariant then $(f*h)(k_1xk_2) = (f*h)(x)$, which is checked by translating the integration variable. Closedness is the closedness of the fixed-point subspace of the compact group $K\times K$ acting continuously by isometries on $L^1(G)$; the approximate identity is found by averaging any approximate identity over $K\times K$, the average again being normalised. $\square$

**Theorem (the Gelfand-pair criterion).** The following are equivalent: (i) $L^1(K\backslash G/K)$ is commutative; (ii) $C_c(K\backslash G/K)$ is commutative; (iii) the algebra $L^1(K\backslash G/K)$ is a commutative Banach `*`-algebra, so that its Gelfand transform is a `*`-homomorphism with dense image in $C_0$ of its spectrum. The condition is the definition of a Gelfand pair, and when it holds the Gelfand theory of a commutative Banach `*`-algebra applies to the invariant algebra.

**Proof.** The equivalence of (i) and (ii) is the density of $C_c$ in $L^1$ together with the continuity of the product; that (i) implies (iii) is the general theorem that a commutative Banach `*`-algebra with isometric involution is symmetric and has a `*`-preserving Gelfand transform, so that every character is Hermitian. The details are in the references. $\square$

**Remark (why commutativity is the whole content).** Once the invariant algebra is commutative, its Gelfand theory applies: the characters are multiplicative functionals, the Gelfand transform is a `*`-homomorphism, and the spectral decomposition is a measure on the spectrum. The Gelfand pair condition is exactly what makes the invariant algebra commutative, and it is the hypothesis of everything below.

## Spherical Functions

**Theorem (the spherical-function identities).** Let $\omega$ be a spherical function. Then

$$
\omega(e) = 1, \qquad \omega(x^{-1}) = \overline{\omega(x)}, \qquad |\omega(x)|\leq1,
$$

and $\omega$ is positive definite; conversely a normalised positive definite bi-$K$-invariant function satisfying the integral equation is spherical.

**Proof.** Setting $x = y = e$ in the integral equation and using $\omega\ne0$ gives $\omega(e) = \omega(e)^2$, so $\omega(e) = 1$ or $\omega(e) = 0$; the second forces $\omega\equiv0$ by the equation, so $\omega(e) = 1$. Positivity is Godement's theorem that a spherical function is a matrix coefficient of a spherical representation, quoted from the references; the Hermitian property $\omega(x^{-1}) = \overline{\omega(x)}$ and the bound $|\omega(x)|\leq1$ are then the elementary properties of a positive definite function, established in *Positive Definite Functions and the Gelfand–Raikov Theorem*. $\square$

**Theorem (spherical functions are the characters of the invariant algebra).** The assignment

$$
\omega \longmapsto \chi_\omega, \qquad \chi_\omega(f) = \int_G f(x)\,\omega(x)\,dx ,
$$

is a bijection between the bounded spherical functions and the characters of the commutative Banach algebra $L^1(K\backslash G/K)$; the bounded spherical functions are exactly the positive definite ones, and they form a locally compact space, the **spherical spectrum** $\Sigma(G,K)$, in the weak-`*` topology.

**Proof.** A character $\chi$ of the invariant algebra satisfies the functional equation $\chi(f*g) = \chi(f)\chi(g)$; representing it by a bounded measurable $\omega$ through the Riesz theorem and using the invariance, one recovers the integral equation, so $\chi$ is the functional of a bounded spherical function. Conversely the integral equation makes $\chi_\omega$ multiplicative. Positivity and boundedness are equivalent for a spherical function by the theorem above, and the topology is the weak-`*` topology of the unit ball of $L^\infty(G)$, compact by Banach–Alaoglu and locally compact after the removal of the zero functional. $\square$

## The Zonal Spherical Function

**Definition.** Let $\pi\in\operatorname{Irr}(G,K)$ and let $\xi\in\mathcal{H}_\pi^K$ be a unit $K$-fixed vector. The **zonal spherical function** of $\pi$ is

$$
\omega_\pi(x) = \langle\pi(x)\xi,\xi\rangle .
$$

It is bi-$K$-invariant, because both the vector and the inner product are $K$-invariant, and it is normalised, $\omega_\pi(e) = 1$.

**Theorem (the zonal spherical function is spherical).** For $\pi\in\operatorname{Irr}(G,K)$ and a $K$-fixed unit vector $\xi$, the zonal spherical function satisfies the integral equation

$$
\int_K\omega_\pi(xky)\,dk = \omega_\pi(x)\omega_\pi(y),
$$

and $\omega_\pi$ is positive definite; the representation $\pi$ is recovered from $\omega_\pi$ as its GNS representation, and the pair $(\pi,\xi)$ is determined by $\omega_\pi$ up to unitary equivalence.

**Proof.** The $K$-fixed subspace $\mathcal{H}_\pi^K$ is one-dimensional when $\pi$ is irreducible and spherical and the pair is a Gelfand pair (multiplicity one), so the projection $P_\xi$ onto $\mathbb{C}\xi$ is the unique $K$-invariant rank-one projection and $\int_K\pi(k)dk = P_\xi$; hence $\int_K\omega_\pi(xky)dk = \int_K\langle\pi(x)\pi(k)\pi(y)\xi,\xi\rangle dk = \langle\pi(x)P_\xi\pi(y)\xi,\xi\rangle$, and $\pi(y)\xi = \omega_\pi(y)\xi + $ (a vector orthogonal to $\xi$). Squaring the projection gives the equation. Positive definiteness is the matrix-coefficient property of *Positive Definite Functions and the Gelfand–Raikov Theorem*, and the recovery is the GNS correspondence there. $\square$

**Corollary (the correspondence).** The map $\pi\mapsto\omega_\pi$ is a bijection from the spherical dual onto the positive definite spherical functions; through the identification with the characters it is the identification of the spherical dual with the spherical spectrum, $\operatorname{Irr}(G,K)\cong\Sigma(G,K)$.

**Proof.** Injectivity: $\omega_\pi$ determines $\pi$ by the theorem. Surjectivity: given a positive definite spherical $\omega$, its GNS representation has a $K$-fixed cyclic vector, the integral equation forces the representation to be irreducible and spherical, and the cyclic vector is $K$-fixed; the recovery of $\omega$ is the matrix coefficient. The identification with the spectrum is the previous theorem. $\square$

## The Decomposition and the Spherical Transform

**Definition.** The **spherical transform** of $f\in L^1(K\backslash G/K)$ is the function on the spherical spectrum

$$
\hat f(\omega) = \int_G f(x)\,\omega(x)\,dx = \chi_\omega(f),
$$

which is the Gelfand transform of the commutative Banach algebra $L^1(K\backslash G/K)$.

**Theorem (the transform is a `*`-homomorphism).** The spherical transform satisfies

$$
\widehat{f*h}(\omega) = \hat f(\omega)\,\hat h(\omega), \qquad \widehat{f^*}(\omega) = \overline{\hat f(\omega)} ,
$$

and it is injective with dense image in $C_0(\Sigma(G,K))$; the spherical functions are the evaluations at the points of the spectrum.

**Proof.** The multiplicativity is the multiplicativity of the Gelfand transform; the involution identity uses that every character of a commutative Banach `*`-algebra with isometric involution is Hermitian, which is condition (ii) of the Gelfand-pair criterion. Injectivity is semisimplicity and density is the Gelfand–Naimark theorem for commutative Banach `*`-algebras. $\square$

**Theorem (decomposition of the invariant $L^2$ space).** On the invariant Hilbert space $L^2(K\backslash G/K)$ the representation of $G$ by left translation decomposes as a direct integral of the spherical representations over the spherical spectrum,

$$
L^2(K\backslash G/K) \;\cong\; \int_{\Sigma(G,K)}^{\oplus} \mathcal{H}_{\pi_\omega}\,\mu(\omega) ,
$$

with multiplicity one at each point, where $\mu$ is the **spherical Plancherel measure**; the subspace of $K$-fixed vectors is $L^2(\Sigma(G,K),\mu)$ and the spherical transform is the unitary equivalence onto it, with

$$
\int_G |f(x)|^2\,dx = \int_{\Sigma(G,K)} |\hat f(\omega)|^2\,d\mu(\omega) .
$$

**Proof.** For a Gelfand pair with $G$ of type I the left regular representation restricted to the invariant vectors is multiplicity-free, and the decomposition is the spectral decomposition of the commutative algebra acting on the invariant space; the plancherel identity is the statement that the Gelfand transform extends to a unitary from the invariant $L^2$ to the $L^2$ of the spectral measure, which is the general Plancherel theorem of *The Plancherel Theorem* specialised to the multiplicity-free part. $\square$

**Example (the symmetric pairs and the Gegenbauer case).** Let $K$ be the fixed subgroup of an involutive automorphism of $G$, so that $(G,K)$ is a symmetric pair and a Gelfand pair; then the spherical dual is the set of irreducible representations with a $K$-fixed vector, the zonal spherical functions are the matrix coefficients of those vectors, $\operatorname{Irr}(G,K)\cong\Sigma(G,K)$, and the spherical Plancherel measure is a measure on the spherical dual. For $G = SO(n+1)$ and $K = SO(n)$ the spherical functions are the Gegenbauer functions, but their explicit form is not needed here; the structure above is the content, and the explicit computation is the subject of the literature.

**Remark (what the article does not do).** The article has used the Gelfand theory of a commutative Banach algebra, cited from *Commutative Banach Algebras* and *Operator Algebras*, and the Plancherel theorem, cited from *The Plancherel Theorem*; the spherical Plancherel measure is computed in *Unitary Representations and the Plancherel Theorem*, below. The induced representations that produce the spherical representations are *Induced Representations of Locally Compact Groups*, not used here; the Hermitian forms and the positive functionals behind the correspondence are *Hermitian Forms and the Group Algebra*, later in this group; no adjoint is taken.

## Summary

For a compact subgroup $K$ of $G$, the bi-$K$-invariant integrable functions form a closed subalgebra $L^1(K\backslash G/K)$ of the group algebra, and $(G,K)$ is a **Gelfand pair** exactly when it is commutative; a spherical function is a continuous bi-$K$-invariant $\omega\ne0$ with $\int_K\omega(xky)dk = \omega(x)\omega(y)$, and then $\omega(e)=1$, $\omega(x^{-1})=\overline{\omega(x)}$, $|\omega|\leq1$, and $\omega$ is positive definite. The bounded spherical functions are exactly the characters of the invariant algebra, $\chi_\omega(f) = \int f\omega$, and they form the spherical spectrum $\Sigma(G,K)$; the zonal spherical function $\omega_\pi(x) = \langle\pi(x)\xi,\xi\rangle$ of a spherical representation $\pi\in\operatorname{Irr}(G,K)$ with unit $K$-fixed vector $\xi$ is spherical, the map $\pi\mapsto\omega_\pi$ is a bijection $\operatorname{Irr}(G,K)\cong\Sigma(G,K)$, and $\pi$ is recovered from $\omega_\pi$ by the GNS construction. The spherical transform $f\mapsto\hat f(\omega) = \int f\omega$ is the Gelfand transform of the invariant algebra, multiplicative with $\widehat{f^*} = \overline{\hat f}$, and the invariant $L^2$ space decomposes with multiplicity one as a direct integral of the spherical representations against the spherical Plancherel measure, with the plancherel identity $\int|f|^2 = \int|\hat f|^2d\mu$. The adjoint, the measure on the spherical dual and the Hermitian forms are the neighbouring articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$, $dk$ | Compact subgroup and its normalised Haar measure, $\int_Kdk=1$ |
| $L^1(K\backslash G/K)$ | Closed subalgebra of bi-$K$-invariant integrable functions |
| Gelfand pair | The commutativity of $L^1(K\backslash G/K)$ |
| $\omega$ | Spherical function, $\int_K\omega(xky)dk = \omega(x)\omega(y)$ |
| $\Sigma(G,K)$ | Spherical spectrum, the characters of the invariant algebra |
| $\chi_\omega(f) = \int_G f\omega\,dx$ | The character attached to a bounded spherical function |
| $\operatorname{Irr}(G,K)$ | The spherical dual, irreducible $\pi$ with $\mathcal{H}_\pi^K\ne0$ |
| $\omega_\pi(x) = \langle\pi(x)\xi,\xi\rangle$ | The zonal spherical function |
| $\operatorname{Irr}(G,K)\cong\Sigma(G,K)$ | The correspondence $\pi\mapsto\omega_\pi$ |
| $\hat f(\omega) = \int_G f\omega\,dx$ | The spherical transform (a Gelfand transform) |
| $\mu$ | Spherical Plancherel measure on $\Sigma(G,K)$ |

## Further Reading

- Sigurdur Helgason, *Groups and Geometric Analysis* (American Mathematical Society, 2000), for spherical functions, the spherical transform and the zonal spherical functions of a symmetric pair.
- Garth Warner, *Harmonic Analysis on Semi-Simple Lie Groups I* (Springer, 1972), for the spherical functions, the spherical spectrum and multiplicity-one decompositions.
- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the Gelfand theory of a commutative Banach `*`-algebra and the characters.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis II* (Springer, 1970), for the Gelfand pairs of a locally compact group and the commutativity of the invariant algebra.
- Joseph A. Wolf, *Spaces of Constant Curvature* (American Mathematical Society, sixth edition, 2011), for the classification of the symmetric pairs and the spherical functions of the rank-one quotients, which are computed there and not here.
