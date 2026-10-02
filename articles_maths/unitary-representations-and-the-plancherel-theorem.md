
# __Unitary Representations and the Plancherel Theorem__

## Introduction

The unitary representations of a group organise themselves into a dual object, and the group algebra acts on each of them by an integrated representation. When the dual is smooth enough — the type I case — the two structures are tied by a single measure: the Plancherel measure, with respect to which the group $L^2$ space is unitarily equivalent to the direct integral of the Hilbert–Schmidt spaces of the dual, and with respect to which the inversion formula reconstructs a function from its operator-valued transform. This article states the theorem in its representation-theoretic form, identifies the measure and its normalisation, gives the inversion formula, and records the two extreme cases, the compact group with its counting measure and the abelian group with the dual Haar measure.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the algebra $L^1(G)$, its involution and the correspondence between nondegenerate `*`-representations and continuous unitary representations from *The Convolution Algebra $L^1(G)$*; the involutive algebra, the positive cone and the completions from *The Group Algebra as an Involutive Algebra*; the positive definite functions, the GNS construction and the Gelfand–Raikov theorem from *Positive Definite Functions and the Gelfand–Raikov Theorem*; the spherical functions and the spherical spectrum from *Spherical Functions and the Zonal Spherical Function*, immediately preceding; the characters, the orthogonality relations and the discrete decomposition from *Analysis on Compact Groups* and *The Peter–Weyl Theorem*; the unitary dual, the direct integral decomposition, the type I property and the multiplicity theory from *Noncommutative Harmonic Analysis* and *Type I Groups*; the Pontryagin duality and the Fourier transform from *Harmonic Analysis on Groups*; the direct integrals, the traces, the trace class, the Hilbert–Schmidt class and the measurable fields of Hilbert spaces from *Operator Algebras*. The Plancherel theorem as a measure-theoretic statement and the existence of the measure are *The Plancherel Theorem*; the transform as a single operator and its unitary equivalence are *The Plancherel Operator*; the adjoint of a representation operator and the equality $\pi(f^*) = \pi(f)^*$ are *Unitary Representations and the Adjoint*, in the `- * Operator Theory` group; the Hermitian forms behind the unitary representations are *Hermitian Forms and the Group Algebra*, later in this group.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$ and modular function $\Delta$, and $\pi : G\to\mathcal{U}(\mathcal{H}_\pi)$ is a continuous **unitary representation**; its **integrated form** is

$$
\pi(f) = \int_G f(x)\,\pi(x)\,dx \in B(\mathcal{H}_\pi) \qquad (f\in L^1(G)),
$$

with $\|\pi(f)\|\leq\|f\|_1$, and $\hat G = \operatorname{Irr}(G)$ is the **unitary dual**, the set of unitary equivalence classes of irreducible unitary representations. The group is of **type I** when every unitary representation is a direct integral of irreducible ones and the dual carries a standard Borel structure; the **Plancherel measure** is written $\mu$ and the **operator-valued transform** is $\hat f(\pi) = \pi(f)$.

## The Integrated Representation

**Theorem (the integrated form is a `*`-representation).** For every continuous unitary representation $\pi$ the integrated form is a nondegenerate `*`-representation of the group algebra,

$$
\pi(f*g) = \pi(f)\,\pi(g), \qquad \pi(f^*) = \pi(f)^*, \qquad \|\pi(f)\|\leq\|f\|_1 ,
$$

and the assignment $\pi\mapsto(\pi(f))_{f\in L^1(G)}$ is a bijection, up to unitary equivalence, between the continuous unitary representations of $G$ and the nondegenerate `*`-representations of $L^1(G)$.

**Proof.** The multiplicativity is the convolution theorem in integrated form, obtained by writing $\pi(f*g) = \int\!\!\int f(y)g(y^{-1}x)\pi(x)\,dy\,dx$ and substituting $x = yz$; the involution identity uses $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ together with unitarity, $\pi(x^{-1}) = \pi(x)^{-1} = \pi(x)^*$, so that the modular factor and the inverse conspire to give the adjoint. Nondegeneracy is the density of $\pi(L^1(G))\mathcal{H}_\pi$, and the converse recovery of $\pi(x)$ from the integrated form by an approximate identity is the correspondence of *The Convolution Algebra $L^1(G)$*. $\square$

**Corollary (the transform of the group algebra).** The **operator-valued Fourier transform** $f\mapsto\hat f$, $\hat f(\pi) = \pi(f)$, satisfies

$$
\widehat{f*g}(\pi) = \hat f(\pi)\,\hat g(\pi), \qquad \widehat{f^*}(\pi) = \hat f(\pi)^* ,
$$

so it is a `*`-homomorphism from the group algebra into the direct product of the algebras $B(\mathcal{H}_\pi)$ over the dual, with the uniform bound $\|\hat f(\pi)\|\leq\|f\|_1$.

**Proof.** Immediate from the theorem, the representation being read factorwise over $\pi\in\hat G$. $\square$

**Remark (why the `*`-property is the hinge).** The involution on the group algebra is chosen so that the integrated form is a `*`-representation: the modular factor in $f^*$ is exactly what makes $\pi(x^{-1})$ into the adjoint of $\pi(x)$ in the integrated formula. Without it the transform would be only a homomorphism, and no positivity, no Plancherel and no inversion would follow. The adjoint computations that make this precise are *Unitary Representations and the Adjoint*, in the `- * Operator Theory` group.

## The Plancherel Theorem

**Theorem (Plancherel, representation-theoretic form).** Let $G$ be unimodular and of type I. There is a measure $\mu$ on the unitary dual $\hat G$, unique up to normalisation, called the **Plancherel measure**, such that for every $f\in L^1(G)\cap L^2(G)$

$$
\int_G |f(x)|^2\,dx = \int_{\hat G} \operatorname{tr}\!\bigl(\hat f(\pi)\,\hat f(\pi)^*\bigr)\,d\mu(\pi) = \int_{\hat G} \bigl\|\hat f(\pi)\bigr\|_{\mathrm{HS}}^2\,d\mu(\pi) ,
$$

and the transform $f\mapsto\hat f$ extends to a unitary equivalence

$$
L^2(G) \;\xrightarrow{\ \cong\ }\; \int_{\hat G}^{\oplus} \mathrm{HS}(\mathcal{H}_\pi)\,d\mu(\pi)
$$

between the group $L^2$ space and the direct integral of the Hilbert–Schmidt spaces of the dual, intertwining the left regular representation with the direct integral of the representations $\pi$.

**Proof.** That such a measure exists, and that the transform extends to an isometry onto the direct integral, is the Plancherel theorem of *The Plancherel Theorem*; the identification of the summand with the Hilbert–Schmidt class uses that $\hat f(\pi)$ is Hilbert–Schmidt for $f\in L^1\cap L^2$ and that the integrated form is a `*`-representation, so that $\operatorname{tr}(\hat f\hat f^*) = \|\hat f\|_{\mathrm{HS}}^2\geq0$. Uniqueness of the normalisation is the irreducibility of the action: two measures giving the same formula agree on the cylinder sets generating the Borel structure of $\hat G$. $\square$

**Corollary (the inversion formula).** For $f$ whose transform is of trace class for $\mu$-almost every $\pi$ and integrable against the measurable field of trace norms, one has, for almost every $x\in G$ and in the sense of distributions in general,

$$
f(x) = \int_{\hat G} \operatorname{tr}\!\bigl(\hat f(\pi)\,\pi(x)^{*}\bigr)\,d\mu(\pi) , \qquad \pi(x)^* = \pi(x^{-1}) .
$$

**Proof.** The identity is Plancherel polarised, $\langle f,g\rangle_{L^2} = \int_{\hat G}\operatorname{tr}(\hat f(\pi)\hat g(\pi)^*)d\mu(\pi)$, with $g$ taken as an approximate identity concentrated at $x$; continuity of the pairings gives the pointwise statement where the integrand is integrable, and the distributional statement otherwise. $\square$

**Corollary (the parity with the abelian and compact cases).** The theorem specialises as follows. If $G$ is abelian then every irreducible representation is one-dimensional, the Hilbert–Schmidt class is the complex numbers, $\hat G$ is the Pontryagin dual and $\mu$ is Haar measure on it, so the formula is the ordinary Parseval identity. If $G$ is compact then the dual is discrete, $\mu$ is the counting measure weighted by the dimensions, $\mu = \sum_{\pi\in\hat G}d_\pi\,\delta_\pi$, and the formula is the Plancherel identity of the Peter–Weyl theory,

$$
\int_G|f|^2\,dx = \sum_{\pi\in\hat G} d_\pi\,\bigl\|\hat f(\pi)\bigr\|_{\mathrm{HS}}^2 .
$$

**Proof.** Both are specialisations of the general formula. An abelian group is unimodular and of type I, its irreducible representations have $\mathcal{H}_\pi = \mathbb{C}$, so $\mathrm{HS}(\mathbb{C}) = \mathbb{C}$ and $\operatorname{tr}$ is the identity, and the measure is the dual Haar measure of *Harmonic Analysis on Groups*; for a compact group the dual is discrete, the trace of the integrated form is $d_\pi\|\hat f(\pi)\|_{\mathrm{HS}}^2$ by the orthogonality relations, and the measure of the singleton $\pi$ is $d_\pi$. $\square$

## The Measure on the Dual

**Theorem (the measure and the von Neumann algebra).** For $f\in L^1(G)\cap L^2(G)$ the operator $\lambda(f)$ is Hilbert–Schmidt, with

$$
\bigl\|\lambda(f)\bigr\|_{\mathrm{HS}}^2 = \int_{\hat G}\bigl\|\hat f(\pi)\bigr\|_{\mathrm{HS}}^2\,d\mu(\pi) = \int_G|f(x)|^2\,dx ,
$$

and the Plancherel measure is exactly the measure for which the centre $Z(G) = L(G)\cap L(G)'$ of the group von Neumann algebra diagonalises as the direct integral of the scalar multiples of the identity,

$$
Z(G) \;\cong\; \int_{\hat G}^{\oplus} \mathbb{C}\,1_{\mathcal{H}_\pi}\; d\mu(\pi) .
$$

**Proof.** The first identity is Plancherel read on the operator $\lambda(f) = \hat f(\lambda)$, combined with the fact that $\int_{\hat G}\|\hat f(\pi)\|_{\mathrm{HS}}^2d\mu$ is finite for $f\in L^2$. For the second, a type I von Neumann algebra decomposes over its centre, and the von Neumann algebra generated by the regular representation is a direct integral of the factors $B(\mathcal{H}_\pi)$; its centre is the algebra of scalar fields, and the measure entering the direct integral is the one that makes the trace statement of the first identity hold, that is the Plancherel measure. $\square$

**Corollary (the spherical part).** If $(G,K)$ is a Gelfand pair with $G$ of type I, then the restriction of the Plancherel measure to the spherical dual $\operatorname{Irr}(G,K)$ is the spherical Plancherel measure of *Spherical Functions and the Zonal Spherical Function*, and the multiplicity-one decomposition of the invariant $L^2$ space there is the restriction of the decomposition above to the $K$-fixed part.

**Proof.** The invariant $L^2$ space is the $K$-fixed part of the direct integral, and the spherical representations are the irreducible representations with $\mathcal{H}_\pi^K\neq0$; the measure restricted to them is the spectral measure of the commutative invariant algebra, which is the spherical Plancherel measure. $\square$

**Remark (what the article does not do).** The existence of the measure and its construction are *The Plancherel Theorem*; the transform as one operator, its unitary equivalence and the intertwining with the regular representation are *The Plancherel Operator*, in the `- Operator Theory` group. The adjoint of a representation operator is *Unitary Representations and the Adjoint*, in the `- * Operator Theory` group, and the Hermitian forms on the algebra that the unitary representations define are *Hermitian Forms and the Group Algebra*, later in this group. The completeness of the dual, the type I property and the multiplicity theory are *Noncommutative Harmonic Analysis* and *Type I Groups*.

## Summary

For a continuous unitary representation $\pi$ of $G$ the integrated form $\pi(f) = \int f(x)\pi(x)dx$ is a nondegenerate `*`-representation of the group algebra, with $\pi(f*g) = \pi(f)\pi(g)$, $\pi(f^*) = \pi(f)^*$ and $\|\pi(f)\|\leq\|f\|_1$, and the correspondence with the unitary representations of $G$ is a bijection up to unitary equivalence; the modular factor in the involution is exactly what makes the integrated form a `*`-representation. When $G$ is unimodular and of type I there is a Plancherel measure $\mu$ on the unitary dual, unique up to normalisation, such that for $f\in L^1\cap L^2$ the plancherel identity $\int_G|f|^2 = \int_{\hat G}\operatorname{tr}(\hat f\hat f^*)d\mu = \int_{\hat G}\|\hat f\|_{\mathrm{HS}}^2d\mu$ holds and the transform extends to a unitary $L^2(G)\cong\int_{\hat G}^{\oplus}\mathrm{HS}(\mathcal{H}_\pi)d\mu$ intertwining the regular representation with the direct integral of the $\pi$, with the inversion formula $f(x) = \int_{\hat G}\operatorname{tr}(\hat f(\pi)\pi(x)^*)d\mu(\pi)$. The measure is the one that expresses the centre of the group von Neumann algebra as the scalar fields over the dual; in the abelian case it is the dual Haar measure and in the compact case the dimension-weighted counting measure, recovering Parseval and Peter–Weyl. On a Gelfand pair the restriction to the spherical dual is the spherical Plancherel measure. The adjoint, the Hermitian forms and the operator form of the transform are the neighbouring articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\pi(f) = \int_G f(x)\pi(x)\,dx$ | The integrated form of a unitary representation |
| $\pi(f*g) = \pi(f)\pi(g)$, $\pi(f^*) = \pi(f)^*$ | The `*`-representation property |
| $\hat G = \operatorname{Irr}(G)$ | The unitary dual |
| $\hat f(\pi) = \pi(f)$ | The operator-valued Fourier transform |
| Type I | Every unitary representation is a direct integral of irreducible ones |
| $\mu$ | The Plancherel measure on $\hat G$ |
| $\int_G\|f\|^2dx = \int_{\hat G}\|\hat f(\pi)\|_{\mathrm{HS}}^2d\mu$ | The Plancherel identity |
| $L^2(G)\cong\int_{\hat G}^{\oplus}\mathrm{HS}(\mathcal{H}_\pi)d\mu$ | The unitary equivalence |
| $f(x) = \int_{\hat G}\operatorname{tr}(\hat f(\pi)\pi(x)^*)d\mu$ | The inversion formula |
| $\mu = \sum_\pi d_\pi\delta_\pi$ | The compact (Peter–Weyl) case |
| Haar measure on $\hat G$ | The abelian (Parseval) case |
| $Z(G)\cong\int_{\hat G}^{\oplus}\mathbb{C}\,1_{\mathcal{H}_\pi}d\mu$ | The centre diagonalised by the measure |

## Further Reading

- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the Plancherel measure, the direct integral decomposition and the trace formula.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the decomposition of a type I von Neumann algebra over its centre and the group von Neumann algebra.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the Plancherel theorem for unimodular type I groups and the inversion formula.
- George W. Mackey, *The Theory of Unitary Group Representations* (University of Chicago Press, 1976), for the unitary dual, the type I property and the multiplicity theory.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for direct integrals, measurable fields of Hilbert spaces and Hilbert–Schmidt operators.
