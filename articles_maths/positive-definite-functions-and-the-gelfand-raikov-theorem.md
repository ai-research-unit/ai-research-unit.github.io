
# __Positive Definite Functions and the Gelfand–Raikov Theorem__

## Introduction

The involution on the group algebra turns a scalar function on the group into a functional on the algebra, and the positivity of the functional is exactly the classical positive definiteness of the function. Every positive definite function is therefore the matrix coefficient of a unitary representation, and the collection of them is rich enough to separate the points of the group: the Gelfand–Raikov theorem says that a locally compact group has no nonzero unitary representation which is trivial on a given nontrivial element, so that the group embeds in the unitary group of its group algebra. This article fixes positive definiteness, builds the representation by the GNS construction, proves the separation theorem, and reads the embedding of the group in the unitaries as the operator form of the statement.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the algebra $L^1(G)$, its involution, its positive cone and its positive functionals from *The Convolution Algebra $L^1(G)$* and *The Group Algebra as an Involutive Algebra*; the correspondence between nondegenerate `*`-representations of $L^1(G)$ and continuous unitary representations of $G$ from *The Convolution Algebra $L^1(G)$*; the characters, Pontryagin duality and the abelian transform from *Harmonic Analysis on Groups*; the unitary representations, irreducibility, the unitary dual and the direct integral from *Noncommutative Harmonic Analysis*; the abstract GNS construction from *The GNS Construction* (Topology on Algebras); and the Hilbert spaces, the bounded operators, the `*`-representations and the $\mathrm{C}^*$-algebras from *Operator Algebras*. The Plancherel measure is *Unitary Representations and the Plancherel Theorem*, below; the adjoint of a representation operator is *Unitary Representations and the Adjoint*, in the `- * Operator Theory` group; the extension of the theory to a Gelfand pair is *Spherical Functions and the Zonal Spherical Function*, next.

Throughout, $G$ is a locally compact Hausdorff group with identity $e$ and left Haar measure $dx$, and $\Delta$ is its modular function; $\phi : G\to\mathbb{C}$ is **continuous** and **positive definite**, written $\phi\gg0$, when

$$
\sum_{i,j=1}^n c_i\,\overline{c_j}\,\phi(x_i^{-1}x_j) \geq 0
$$

for every finite family $x_1,\dots,x_n\in G$ and scalars $c_1,\dots,c_n\in\mathbb{C}$. A unitary representation is a continuous homomorphism $\pi : G\to\mathcal{U}(\mathcal{H})$ into the unitary operators of a Hilbert space $\mathcal{H}$; its **matrix coefficients** are the functions $x\mapsto\langle\pi(x)\xi,\eta\rangle$.

## The Positive Definite Functions

**Theorem (elementary properties).** A continuous $\phi$ is positive definite if and only if the function $\tilde\phi(x) = \overline{\phi(x^{-1})}$ is, and then

$$
\phi(x^{-1}) = \overline{\phi(x)}, \qquad |\phi(x)| \leq \phi(e), \qquad \phi(e)\geq0 ;
$$

if $\phi(e) = 0$ then $\phi\equiv0$, and every positive definite function is bounded with $\|\phi\|_\infty = \phi(e)$.

**Proof.** The $2\times2$ case of the defining inequality with $(x_1,x_2) = (e,x)$ gives the Hermitian symmetry $\phi(x^{-1}) = \overline{\phi(x)}$ and $\phi(e)\geq0$; the $n$-tuple $(e,x_1,\dots,x_n)$ with the phase of $c_0$ adjusted gives $|\phi(x)|\leq\phi(e)$; the norm statement follows. The $\tilde\phi$ statement is the defining sum rewritten with the $x_i$ replaced by their inverses. $\square$

**Proposition (the functional on the algebra).** A bounded continuous $\phi$ is positive definite if and only if the functional

$$
\omega_\phi(f) = \int_G f(x)\,\phi(x)\,dx
$$

is positive on $L^1(G)$, that is $\omega_\phi(f^*\!*f)\geq0$ for all $f$, and if and only if the sesquilinear form

$$
\langle Sf, Sg\rangle_\phi = \int_G\int_G \phi(y^{-1}x)\,f(x)\,\overline{g(y)}\,dx\,dy
$$

is positive semidefinite on $C_c(G)$.

**Proof.** The sesquilinear form on step functions $f = \sum c_i\delta_{x_i}$ reduces to the defining double sum, so positive definiteness is precisely its positive semidefiniteness on $C_c(G)$; the equivalence with the positivity of $\omega_\phi$ is the standard computation relating the two expressions by Fubini and the definition of $f^*\!*f$, and is in the references. $\square$

**Corollary (the cone and its closure).** The positive definite functions form a convex cone, closed under the involution $\phi\mapsto\tilde\phi$, and closed under pointwise limits of locally bounded families and under the product of two bounded positive definite functions; the normalised ones, with $\phi(e) = 1$, are the **states** of the group.

**Proof.** Convexity is the linearity of the defining sum in $\phi$; closure under pointwise limits is the closedness of the non-negative reals. Closure under products follows from the representation-theoretic description below via the tensor product, and the normalisation is the statement $\|\phi\|_\infty = \phi(e)$. $\square$

## The GNS Construction for a Positive Definite Function

**Theorem (every positive definite function is a matrix coefficient).** Let $\phi\gg0$ and let $N = \{f\in C_c(G) : \langle Sf,Sf\rangle_\phi = 0\}$. Then the quotient $\mathcal{H}_\phi = C_c(G)/N$ completes to a Hilbert space on which there is a unique unitary representation $\pi_\phi$ with

$$
\pi_\phi(x)(Sf) = S(L_xf), \qquad (L_xf)(y) = f(x^{-1}y),
$$

and a cyclic vector $\xi_\phi = S(\text{normalised approximate identity})$ with

$$
\phi(x) = \langle\pi_\phi(x)\xi_\phi, \xi_\phi\rangle , \qquad \|\xi_\phi\|^2 = \phi(e) .
$$

**Proof.** The quotient by the null space of the positive semidefinite form is a pre-Hilbert space, and its completion is $\mathcal{H}_\phi$. The left translation $L_x$ is isometric for the form, $\langle SL_xf, SL_xg\rangle_\phi = \langle Sf,Sg\rangle_\phi$, because $\phi$ is invariant under this substitution in its argument; hence $L_x$ descends to a unitary operator $\pi_\phi(x)$ on $\mathcal{H}_\phi$, and $\pi_\phi(xy) = \pi_\phi(x)\pi_\phi(y)$ because $L_{xy} = L_xL_y$. Continuity of $x\mapsto\pi_\phi(x)$ follows from the continuity of translation in $C_c(G)$ and the bound $\|S(L_xf) - Sf\|^2 = 2\|Sf\|^2 - 2\,\mathrm{Re}\langle S(L_xf),Sf\rangle_\phi$, whose last term is continuous in $x$. The vector $\xi_\phi = S(u)$ for a normalised approximate identity $u$ of $L^1(G)$ is cyclic because $S(C_c(G))$ is dense, and $\langle\pi_\phi(x)\xi_\phi,\xi_\phi\rangle_\phi = \langle S(L_xu), S(u)\rangle_\phi\to\phi(x)$. $\square$

**Corollary (the correspondence).** The assignment $\phi\mapsto(\pi_\phi,\xi_\phi)$ is a bijection, up to unitary equivalence fixing the vector, between the continuous positive definite functions and the pairs $(\pi,\xi)$ consisting of a continuous unitary representation with a cyclic vector; irreducibility of $\pi_\phi$ corresponds to $\phi$ being an extreme point of the normalised cone.

**Proof.** Given a cyclic pair $(\pi,\xi)$, the function $\langle\pi(x)\xi,\xi\rangle$ is positive definite by the defining sum, and the GNS construction recovers $(\pi,\xi)$ from it; the two constructions are inverse. The irreducibility statement is the standard description of the extreme points of the state space as the pure states, whose GNS representations are irreducible. $\square$

## The Gelfand–Raikov Theorem

**Theorem (the representations separate the points).** For every $x\neq e$ in $G$ there is a continuous unitary representation $\pi$ with $\pi(x)\neq 1$. Equivalently, the map

$$
j : G\longrightarrow \prod_{\pi}\mathcal{U}(\mathcal{H}_\pi), \qquad j(x) = (\pi(x))_\pi ,
$$

the product over the continuous unitary representations, is injective, and the Gelfand–Raikov topology on $G$ is the original one.

**Proof.** Choose a symmetric open neighbourhood $V$ of $e$ with $x\notin V^2$, and $f\in C_c(G)$ supported in $V$ with $f\geq0$ and $f(e)>0$; set $\phi = f^*\!*f$, which is positive definite by the proposition. Then $\phi(y) = \int_G \overline{f(z^{-1})}\,\Delta(z)^{-1}\,f(z^{-1}y)\,dz$, whose integrand is supported where $z\in V$ and $z^{-1}y\in V$, hence where $y = z\,(z^{-1}y)\in V^2$; so $\phi$ vanishes off $V^2$ and $\phi(x) = 0$, while $\phi(e) = \int_G |f|^2 > 0$. For the GNS pair $(\pi_\phi,\xi_\phi)$ the matrix coefficient at $x$ is $\phi(x) = 0$, so $\langle\pi_\phi(x)\xi_\phi,\xi_\phi\rangle = 0\neq\|\xi_\phi\|^2 = \phi(e)$ and $\pi_\phi(x)\neq1$. The product map is then injective because every nontrivial element is separated from the identity by some factor; continuity of $j$ is the continuity of each $\pi$, and the topology it induces on $G$ is the quotient topology of the same family, which is the original group topology. $\square$

**Corollary (the embedding in the unitaries of the group algebra).** The left regular representation already separates the points: the map

$$
j_G : G\longrightarrow \mathcal{U}\bigl(L^2(G)\bigr), \qquad j_G(x) = \lambda(x), \qquad (\lambda(x)\xi)(y) = \xi(x^{-1}y),
$$

is a topological isomorphism of $G$ onto its image, and the image lies in the unitary group of the multiplier algebra of the reduced group algebra, $j_G(G)\subseteq\mathcal{U}(M(C^*_r(G)))$.

**Proof.** Injectivity is faithfulness of the regular representation on $L^2(G)$: $\lambda(x) = 1$ gives $\xi(x^{-1}y) = \xi(y)$ for all $\xi$, hence $x = e$. The map is multiplicative and each $\lambda(x)$ is unitary by left invariance of $dx$; it is a homeomorphism onto its image in the strong operator topology because $\|\lambda(x)\xi - \xi\|\to0$ as $x\to e$ for every $\xi$ (continuity of translation), and conversely convergence of $\lambda(x_\alpha)$ to $\lambda(x)$ in the strong topology forces $x_\alpha\to x$ by testing on a bump supported in a small neighbourhood. The left translation is a `*`-automorphism of the group algebra, so $\lambda(x)$ is a unitary multiplier of $C^*_r(G)$. $\square$

**Remark (the abelian case and Bochner's theorem).** If $G$ is abelian then $\Delta\equiv1$ and the positive definite functions are exactly the Fourier transforms $\hat\mu$ of the positive bounded Radon measures $\mu$ on the dual $G^\vee$: the GNS representation of $\hat\mu$ is the direct integral of the characters of $G^\vee$ over $\mu$, and Gelfand–Raikov reduces to the trivial statement that the characters separate the points. This is Bochner's theorem of *Harmonic Analysis on Groups*, §Positive Definite Functions, and the concrete case of the correspondence above.

**Remark (what the article does not do).** The article has used the correspondence between `*`-representations of $L^1(G)$ and unitary representations of $G$ as established in *The Convolution Algebra $L^1(G)$*; it has taken no adjoint, and the equality $\pi(f^*) = \pi(f)^*$ for a unitary representation belongs to *Unitary Representations and the Adjoint*, in the `- * Operator Theory` group. The Plancherel measure, which is the measure on the dual selected by the regular representation, is *Unitary Representations and the Plancherel Theorem*, below; the theory of the spherical functions of a Gelfand pair is the next article; the completeness of the family of irreducible representations is *Noncommutative Harmonic Analysis*.

## Summary

A continuous function $\phi$ on $G$ is positive definite when the defining finite sums are non-negative; then $\phi(x^{-1}) = \overline{\phi(x)}$, $|\phi(x)|\leq\phi(e) = \|\phi\|_\infty$, the positive definite functions form a convex cone closed under the involution $x\mapsto x^{-1}$, and $\phi$ is positive definite exactly when the functional $\omega_\phi(f) = \int f\phi$ is positive on $L^1(G)$, equivalently when the sesquilinear form $\langle Sf,Sg\rangle_\phi$ is positive semidefinite. The GNS construction gives, for each positive definite $\phi$, a unitary representation $\pi_\phi$ with cyclic vector $\xi_\phi$ and matrix coefficient $\phi(x) = \langle\pi_\phi(x)\xi_\phi,\xi_\phi\rangle$, and the assignment is a bijection with the cyclic unitary representations up to equivalence; the extreme points of the normalised cone are the irreducible representations. The Gelfand–Raikov theorem, proved by convolving a bump supported in a small symmetric neighbourhood with its involution to obtain a positive definite function vanishing at a prescribed nontrivial point, shows that the continuous unitary representations separate the points of $G$, equivalently that $G$ embeds topologically into the product of the unitary groups of its representation spaces, and in operator form that $x\mapsto\lambda(x)$ is a topological isomorphism of $G$ onto a closed subgroup of the unitary group of the multiplier algebra of $C^*(G)$. In the abelian case the positive definite functions are the transforms of positive measures on the dual (Bochner). The adjoint, the Plancherel measure, the Gelfand pairs and the completeness of the dual are the neighbouring articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\phi\gg0$ | $\phi$ is continuous positive definite |
| $\sum_{i,j}c_i\overline{c_j}\phi(x_i^{-1}x_j)\geq0$ | The defining inequality |
| $\tilde\phi(x) = \overline{\phi(x^{-1})}$ | The involuted function, positive definite with $\phi$ |
| $\phi(x^{-1}) = \overline{\phi(x)}$, $\|\phi\|_\infty = \phi(e)$ | The elementary properties |
| $\omega_\phi(f) = \int_G f\phi\,dx$ | The functional, positive iff $\phi\gg0$ |
| $\langle Sf,Sg\rangle_\phi$ | The positive semidefinite sesquilinear form |
| $\pi_\phi$, $\xi_\phi$ | The GNS representation and cyclic vector |
| $\phi(x) = \langle\pi_\phi(x)\xi_\phi,\xi_\phi\rangle$ | Every positive definite function is a matrix coefficient |
| $j(x) = (\pi(x))_\pi$ | The separating product map of Gelfand–Raikov |
| $j_G(x) = \lambda(x)\in\mathcal{U}(M(C^*(G)))$ | The embedding in the unitaries of the group algebra |
| $\hat\mu\gg0\iff\mu\geq0$ | Bochner's theorem, abelian case |

## Further Reading

- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis II* (Springer, 1970), for positive definite functions, the GNS construction on a group and the Gelfand–Raikov theorem.
- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the GNS construction of a positive functional and the correspondence of pure states with irreducible representations.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the Gelfand–Raikov theorem and the embedding of the group in its group algebra.
- Walter Rudin, *Fourier Analysis on Groups* (Wiley, 1962), for positive definite functions on an abelian group and Bochner's theorem.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the GNS representation and the extreme points of the state space.
