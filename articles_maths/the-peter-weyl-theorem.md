
# __The Peter–Weyl Theorem__

## Introduction

The Peter–Weyl theorem is the decomposition theorem of harmonic analysis on a compact group, and it is the exact analogue, for the regular representation, of the statement that the Fourier coefficients of a function on the circle form a complete orthonormal system. It says three things at once: that the matrix coefficients of the finite-dimensional irreducible unitary representations of a compact group $K$ span a dense subspace of the continuous functions in the supremum norm; that the functions $\sqrt{d_\pi}\,\pi_{ij}$ form an orthonormal basis of $L^2(K)$; and that every unitary representation of $K$ is a direct sum of finite-dimensional irreducible ones. The first is the approximation theorem, the second is the completeness of the Fourier expansion, and the third is **Weyl's theorem** on complete reducibility, which for a compact group is not a separate hypothesis but a consequence of the existence of the invariant probability measure.

The theorem was proved by F. Peter and H. Weyl in 1927 for compact Lie groups; the general compact case was obtained by extending the same argument to arbitrary compact groups through the compactness of the convolution operators. This article states the theorem in its several equivalent forms, gives the analytic proof in the standard sequence of steps, and draws the consequences that the rest of the compact theory uses. It develops the theorem; *Analysis on Compact Groups* develops the analysis built on it, and the two articles divide the material as follows: the orthogonality relations, the inversion and Plancherel formulas, the structure of the dual and the classical examples belong to that article, while the decomposition theorem, its proof, and its structural corollaries — finite-dimensionality, complete reducibility, separation of points, the bound on multiplicities — are here.

The boundaries of the block hold as stated in the two preceding articles. The **representation theory** — unitary representations, irreducibility, Schur's lemma, intertwiners, the unitary dual as an object of Part II, induced representations, Mackey theory, type classification, property (T) — is Part II's: *Representation Theory of Locally Compact Groups*, *Induced Representations of Locally Compact Groups*, *Mackey Theory*, *Type I Groups*. The **Haar measure** is *Locally Compact Groups and Haar Measure*. The **general measure theory** — the integral, $L^p$ spaces, Fubini, the Stone–Weierstrass theorem — is *Measure Theory and Integration* and *Modes of Convergence*, in the Foundations slot of this Part, and the **functional analysis** — the spectral theorem for compact self-adjoint operators, Hilbert–Schmidt operators — is standard and is quoted as it is used, its development in this Part belonging to the laterin the Analysis on Linear Spaces slot. The **abelian theory** is *Harmonic Analysis on Groups*, and the **general non-abelian theory** is not developed here.

Throughout, $K$ is a compact Hausdorff group with normalised Haar measure $dk$, $\int_K dk = 1$; $\operatorname{Irr}(K)$ is the set of equivalence classes of irreducible unitary representations, $\mathcal{H}_\pi$ the finite-dimensional representation space, $d_\pi = \dim\mathcal{H}_\pi$, $\pi_{ij}(k) = \langle\pi(k)e_j,e_i\rangle$ the matrix coefficients in an orthonormal basis, $\chi_\pi = \operatorname{Tr}\pi$ the character, $\lambda$ and $\rho$ the left and right regular representations on $L^2(K)$, and $A(K)$ the representative-function algebra. The unitary dual is written $\operatorname{Irr}(K)$, not $\widehat{K}$. No physics is invoked.

## The Statement

### The Main Theorem

**Theorem (Peter–Weyl).** Let $K$ be a compact Hausdorff group and let $A(K)$ be the linear span of the matrix coefficients $k \mapsto \langle\pi(k)u,v\rangle$ of all finite-dimensional continuous unitary representations of $K$. Then:

**(a) Density.** $A(K)$ is dense in $C(K)$ in the supremum norm, and dense in $L^p(K)$ for every $1 \leq p < \infty$.

**(b) Orthonormal basis.** For $\pi,\sigma \in \operatorname{Irr}(K)$ and orthonormal bases $(e_i)$ of $\mathcal{H}_\pi$, $(f_l)$ of $\mathcal{H}_\sigma$,

$$
\int_K \pi_{ij}(k)\,\overline{\sigma_{lm}(k)}\,dk = \frac{1}{d_\pi}\,\delta_{\pi\sigma}\,\delta_{il}\,\delta_{jm} ,
$$

so the functions $e^\pi_{ij} = \sqrt{d_\pi}\,\pi_{ij}$ form an orthonormal basis of $L^2(K)$. Consequently

$$
L^2(K) = \bigoplus_{\pi\in\operatorname{Irr}(K)}^{\oplus}\ \bigoplus_{i,j=1}^{d_\pi}\ \mathbb{C}\,e^\pi_{ij}
\;\cong\; \bigoplus_{\pi\in\operatorname{Irr}(K)}^{\oplus}\ \bigl(\mathcal{H}_\pi \otimes \mathcal{H}_\pi^*\bigr),
$$

the orthogonal direct sum being a Hilbert-space direct sum, and each irreducible $\pi$ occurring with multiplicity $d_\pi$.

**(c) Complete reducibility.** Every continuous unitary representation of $K$ on a Hilbert space is a direct sum of finite-dimensional irreducible unitary representations; equivalently, every closed invariant subspace has a closed invariant complement. In particular every irreducible unitary representation of $K$ is finite-dimensional.

**(d) Characters.** The characters $\chi_\pi$ form an orthonormal basis of the subspace $L^2(K)^K$ of class functions.

Part (a) is the approximation form, (b) the Fourier-expansion form, (c) Weyl's theorem, and (d) the class-function form. The four are proved together in the next two sections: (a) and (b) are the hard analytic content, (c) and (d) are corollaries.

**Remark (the isometry form).** The map

$$
\mathcal{F} : L^2(K) \longrightarrow \bigoplus_{\pi\in\operatorname{Irr}(K)}^{\oplus}\bigl(\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*\bigr), \qquad
f \mapsto \bigl(\hat f(\pi)\bigr)_{\pi\in\operatorname{Irr}(K)},\quad
\hat f(\pi) = \int_K f(k)\pi(k)\,dk,
$$

is a unitary equivalence of Hilbert spaces; this is the polarised form of (b), and it is the compact case of the Plancherel theorem, stated as standard. The finite-dimensional summand $\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*$ is precisely the space of matrix coefficients of $\pi$, and the transform is the identity between the two descriptions.

### The Theorem is the Completeness of the Fourier Expansion

For the circle, $A(S^1)$ is the set of trigonometric polynomials and Peter–Weyl is the classical theorem that they are dense in $C(S^1)$ and that $\{e^{2\pi i n\theta}\}_{n\in\mathbb{Z}}$ is an orthonormal basis of $L^2(S^1)$; the density is the Weierstrass approximation theorem for periodic functions, and the completeness is the uniqueness of Fourier series. For a finite group the theorem is the Wedderburn decomposition of the group algebra, $\mathbb{C}[K] \cong \bigoplus_{\pi\in\operatorname{Irr}(K)}\operatorname{End}(\mathcal{H}_\pi)$, with $\sum_\pi d_\pi^2 = |K|$. For a compact group the theorem is the statement that these two facts are one fact, and that the reason is the existence of the invariant probability measure.

## The Analytic Input

### Compact and Hilbert–Schmidt Operators

The proof uses one analytic theorem of standard functional analysis: a self-adjoint compact operator on a Hilbert space has an orthonormal basis of eigenvectors, its nonzero eigenvalues are real and have finite multiplicity, and they accumulate only at $0$. Recall that an operator $T$ is **compact** if the image of the unit ball has compact closure, that a **Hilbert–Schmidt** operator on $L^2(K)$ is one with square-integrable kernel, and that every Hilbert–Schmidt operator is compact and every compact operator is the norm limit of finite-rank operators.

**Lemma (Hilbert–Schmidt).** For $f \in L^2(K)$ the operator $T_f : L^2(K) \to L^2(K)$,

$$
T_f h = f * h = \int_K f(y)\,\lambda(y)h\,dy ,
$$

is Hilbert–Schmidt, hence compact, with $\|T_f\|_{\mathrm{HS}} = \|f\|_2$, and $\|T_f\| \leq \|f\|_1$.

**Proof.** The kernel of $T_f$ with respect to the measure $dk$ is $K_f(x,y) = f(y^{-1}x)$, and a change of variable shows $\int\int|K_f(x,y)|^2\,dx\,dy = \int|f|^2$. The elementary bound $\|f*h\|_2 \leq \|f\|_1\|h\|_2$ is Young's inequality for the compact case. $\square$

### The Convolution Operator and the Invariance of its Eigenspaces

**Lemma (existence of a finite-dimensional invariant subspace).** There exists a nonzero finite-dimensional subspace $V \subseteq L^2(K)$ invariant under both the left and the right regular representations.

**Proof.** Choose $h \in C(K)$ with $h \neq 0$ and put $f = h * h^{\#}$, where $h^{\#}(x) = \overline{h(x^{-1})}$. Then $f$ is a **class function**, $f(xkx^{-1}) = f(k)$, and $f^{\#} = f$; hence $T_f$ is self-adjoint, since the adjoint of $T_h$ is $T_{h^{\#}}$ by a change of variable. Moreover $T_f = T_h T_h^*$ is positive, and it is nonzero: the adjoint $T_h^* = T_{h^{\#}}$ gives $T_h^*(h) = h^{\#} * h$, and

$$
(h^{\#}*h)(e) = \int_K h^{\#}(y)\,h(y^{-1})\,dy = \int_K \overline{h(y^{-1})}\,h(y^{-1})\,dy = \|h\|_2^2 > 0 ,
$$

so $h^{\#}*h$ is not the zero function and $\langle T_f h, h\rangle = \|T_h^* h\|_2^2 = \|h^{\#}*h\|_2^2 > 0$. Thus $T_f$ is a nonzero compact self-adjoint operator. Let $\lambda \neq 0$ be an eigenvalue and $V = \ker(T_f - \lambda I)$ the eigenspace; $V$ is finite-dimensional because $T_f$ is compact, and it is nonzero. Because $f$ is a class function, $T_f$ commutes with both left and right translations:

$$
T_f\,\lambda(x) = \lambda(x)\,T_f, \qquad T_f\,\rho(x) = \rho(x)\,T_f \qquad (x \in K),
$$

the first from the change of variable $y \mapsto xyx^{-1}$ and the centrality of $f$, the second from the commutation of left and right translations. Hence $V$ is invariant under $\lambda(K)$ and under $\rho(K)$. $\square$

**Remark (why centrality is needed).** For a general $f$ the operator $T_f$ commutes only with the right regular representation, and the eigenspaces are only $\rho(K)$-invariant; the class-function choice of $f$ restores full $K \times K$ invariance, which is what makes $V$ a finite-dimensional representation of $K$ on both sides and what allows the argument to close. The approximate-identity form of the argument — averaging $f$ over conjugacy classes — is the standard alternative.

### Existence of Finite-Dimensional Irreducibles

**Corollary.** $K$ has at least one nontrivial finite-dimensional irreducible unitary representation if $K$ is nontrivial; more precisely, the nonzero finite-dimensional subspace $V$ of the lemma decomposes into finitely many irreducible $K$-invariant subspaces, each finite-dimensional, so the set of finite-dimensional irreducible representations of $K$ is nonempty.

**Proof.** The subspace $V$ is a finite-dimensional continuous unitary representation of $K$ under left translation. Every finite-dimensional unitary representation is a direct sum of irreducibles — this is the elementary case of complete reducibility available from the existence of an invariant inner product and the finiteness of the dimension — so $V$ contains an irreducible subrepresentation, which is finite-dimensional. If $K$ is nontrivial, an irreducible constituent of a nonzero finite-dimensional subspace can be taken nontrivial, since the trivial representation is one-dimensional. $\square$

## The Proof of the Theorem

### The Representative-Function Algebra

**Definition.** $A(K)$ is the linear span of the matrix coefficients of the finite-dimensional continuous unitary representations of $K$; equivalently, the union of the finite-dimensional $K\times K$-invariant subspaces of $C(K)$.

**Proposition (algebra structure).** $A(K)$ is a subalgebra of $C(K)$ containing the constants, closed under complex conjugation and under left and right translation; it is closed under convolution and under pointwise multiplication.

**Proof.** The product of matrix coefficients of $\pi$ and $\sigma$ is a matrix coefficient of the tensor product $\pi\otimes\sigma$; the conjugate $\overline{\pi_{ij}}$ is the $(j,i)$ coefficient of the contragredient $\bar\pi$; translation invariance is $(\lambda(x)\pi_{ij})(k) = \pi_{ij}(x^{-1}k) = (\pi(x)^{-1}\pi(k))_{ij}$, a linear combination of matrix coefficients of $\pi$. Convolution closure is the convolution theorem. $\square$

**Lemma (separation of points).** $A(K)$ separates the points of $K$; that is, for $x \neq y$ there is $f \in A(K)$ with $f(x) \neq f(y)$.

**Proof.** Let $W$ be the closure in $L^2(K)$ of the sum of all finite-dimensional $\lambda(K)$-invariant subspaces. Then $W$ is a closed $\lambda(K)$-invariant subspace of $L^2(K)$ and its orthogonal complement $W^\perp$ is also $\lambda(K)$-invariant. The operators $T_f$ for class functions $f$ commute with $\lambda(K)$, so they preserve both $W$ and $W^\perp$; moreover $W$ is dense in $L^2(K)$. Indeed, suppose $W^\perp \neq \{0\}$ and apply the existence lemma to the restricted representation $\lambda|_{W^\perp}$: choosing $h \in C(K)$ nonzero and approximating the identity, one obtains a nonzero finite-dimensional $\lambda(K)$-invariant subspace of $W^\perp$, contradicting the definition of $W$. Hence $W = L^2(K)$, so the sum of the finite-dimensional invariant subspaces is dense.

Now let $x \neq y$ and suppose $f(x) = f(y)$ for every $f \in A(K)$. Since $A(K)$ is the algebraic sum of the finite-dimensional invariant subspaces, its closure in $L^2(K)$ is $W = L^2(K)$, and the evaluation at a point is not continuous in $L^2$; the argument is therefore made on a single finite-dimensional invariant subspace. Choose a finite-dimensional $\lambda(K)$-invariant subspace $V$ with $\lambda(x)|_V \neq \lambda(y)|_V$; such $V$ exists because $\lambda(x) \neq \lambda(y)$ for $x \neq y$ (the left regular representation is faithful: if $\lambda(x) = \lambda(y)$ then $\lambda(xy^{-1}) = I$, and applying this to a continuous function supported in a small neighbourhood of $e$ forces $xy^{-1} = e$), and because the finite-dimensional invariant subspaces are cofinal in $L^2(K)$ by the previous paragraph. On $V$ the function $k \mapsto \langle\lambda(k)u, v\rangle$ is, for $u,v \in V$, a matrix coefficient of the finite-dimensional representation $\lambda|_V$, hence belongs to $A(K)$; since the matrix coefficients of a finite-dimensional representation separate operators — if two operators have all the same $\langle Tu,v\rangle$ they are equal — some such function takes different values at $x$ and $y$. $\square$

### Density and the Orthonormal Basis

**Proof of Peter–Weyl (a) and (b).** By the proposition above, $A(K)$ is a self-adjoint subalgebra of $C(K)$ containing the constants and separating points; the Stone–Weierstrass theorem therefore gives that $A(K)$ is dense in $C(K)$ in the supremum norm, which is (a). The density in $L^p(K)$ follows because $C(K)$ is dense in $L^p(K)$ for $p < \infty$ and the measure is finite.

For (b), the orthogonality relation is Schur's lemma applied to the operator $\int_K\sigma(k)^{-1}B\pi(k)dk$ for $B \in \operatorname{Hom}(\mathcal{H}_\pi,\mathcal{H}_\sigma)$: invariance forces the operator to be zero when $\pi \not\cong \sigma$ and a scalar when $\pi = \sigma$, and evaluating the scalar by taking traces gives the constant $d_\pi^{-1}$ from the normalisation $\int_K dk = 1$. Since $A(K)$ is dense in $L^2(K)$ and is the algebraic span of the orthonormal family $\{e^\pi_{ij}\}$, that family is complete, hence an orthonormal basis. The identification of the summand with $\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*$ is the definition of the matrix coefficients of $\pi$ in a basis. $\square$

### Complete Reducibility

**Proof of Peter–Weyl (c).** Let $\pi$ be a continuous unitary representation of $K$ on a Hilbert space $H$, and let $\mathcal{S}$ be the set of all finite-dimensional $\pi(K)$-invariant subspaces, directed by inclusion and closed under algebraic sum. Their algebraic span $V$ is $\pi(K)$-invariant and dense in $H$: if $\overline{V} \neq H$, the orthogonal complement $\overline{V}^\perp$ is a nonzero $\pi(K)$-invariant closed subspace, and applying the argument of the existence lemma to the representation restricted to $\overline{V}^\perp$ — using the compact self-adjoint operators $T_f$ built from $\pi$ by $\int_K f(k)\pi(k)dk$ — produces a nonzero finite-dimensional invariant subspace inside $\overline{V}^\perp$, contradicting the definition of $V$. Hence $H$ is the Hilbert-space direct sum of the members of a maximal orthogonal family of irreducible finite-dimensional invariant subspaces. Since each irreducible unitary representation of $K$ is a summand of $H = L^2(K)$ (by considering the regular representation, or by an irreducible being weakly contained and contained), each irreducible is finite-dimensional. This is Weyl's theorem. $\square$

**Proof of Peter–Weyl (d).** A character $\chi_\pi$ is a class function, and the orthogonality relation summed over $i = l$, $j = m$ gives $\int_K\chi_\pi\overline{\chi_\sigma} = \delta_{\pi\sigma}$. Completeness: a class function in $L^2(K)$ orthogonal to every $\chi_\pi$ is orthogonal to every matrix coefficient, because averaging a coefficient over conjugacy classes expresses the projection onto class functions as a combination of characters and the averaged coefficient is a multiple of a character; by (b) it is zero. Hence the characters are an orthonormal basis of the class functions. $\square$

**Remark (the count of constituents).** In the regular representation each irreducible $\pi$ occurs with multiplicity $d_\pi = \dim\mathcal{H}_\pi$, on the summand $\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*$; equivalently $\lambda \cong \bigoplus_{\pi\in\operatorname{Irr}(K)}\pi^{\oplus d_\pi}$. The multiplicity is finite because $d_\pi < \infty$, and it is exactly $d_\pi$ and not some other integer because the summand has dimension $d_\pi^2 = d_\pi\cdot d_\pi$ as a representation of $K$ under left translation. This is the statement that the coefficient space of $\pi$ is a full matrix algebra $\operatorname{End}(\mathcal{H}_\pi)$ under convolution.

## Consequences

### Finite Dimensionality and the Algebraic Structure of the Regular Representation

**Corollary (algebraic Peter–Weyl).** As an algebra under convolution, appropriately completed, the regular representation gives

$$
L^1(K) \;\widehat{\longrightarrow}\; \bigoplus_{\pi\in\operatorname{Irr}(K)} \operatorname{End}(\mathcal{H}_\pi)
$$

under $f \mapsto (\hat f(\pi))$, the target being the algebraic direct sum of full matrix algebras; equivalently the group von Neumann algebra $L(K) = \lambda(K)''$ is the direct sum $\bigoplus_\pi \operatorname{End}(\mathcal{H}_\pi)$, a type I von Neumann algebra.

**Proof.** The convolution theorem gives the homomorphism; injectivity is the completeness of the coefficient algebra (a function whose transform vanishes is orthogonal to every matrix coefficient); the image of the center of $L^1(K)$ consists of the scalar operators, and the whole map is onto the algebraic direct sum because the matrix units $e^\pi_{ij}$ have transforms supported on $\mathcal{H}_\pi$. The von Neumann algebra statement is the weak closure of the image, namely the direct sum of the finite-dimensional factors. $\square$

### Separation of Points and the Gelfand–Raĭkov Property

**Corollary (Gelfand–Raĭkov for compact groups).** The finite-dimensional representations of $K$ separate the points of $K$: for $x \neq y$ there is a finite-dimensional continuous representation $\pi$ with $\pi(x) \neq \pi(y)$. Consequently a compact group is isomorphic to a closed subgroup of a product of unitary groups, and a compact group is determined up to isomorphism by its finite-dimensional representation theory.

**Proof.** The separation statement is contained in the lemma on separation of points, since a matrix coefficient distinguishes $x$ and $y$ exactly when the underlying finite-dimensional representation does. The embedding is into $\prod_\pi U(\mathcal{H}_\pi)$ with the product topology, and it is a homeomorphism onto its image by compactness. $\square$

### Multiplicities and the Class-Function Expansion

**Corollary (class functions).** For a class function $f \in L^2(K)$,

$$
f = \sum_{\pi\in\operatorname{Irr}(K)} \lambda_\pi(f)\,\chi_\pi , \qquad \lambda_\pi(f) = \int_K f(k)\,\overline{\chi_\pi(k)}\,dk ,
$$

in $L^2$, with $\|f\|_2^2 = \sum_\pi|\lambda_\pi(f)|^2$. Consequently two class functions that have the same character transforms are equal.

**Corollary (Peter–Weyl for $K\times K$).** The representation $\lambda\otimes\rho$ of $K\times K$ on $L^2(K)$ decomposes as $\bigoplus_{\pi\in\operatorname{Irr}(K)}\pi\boxtimes\bar\pi$; each irreducible of $K\times K$ occurs with multiplicity at most one in the regular representation of $K\times K$. This is the basis of the theory of spherical functions and of the harmonic analysis on symmetric spaces, whose development belongs to *Symmetric Spaces* and to the harmonic analysis of manifolds.

### The Compact Lie Case and the Heat Kernel

Let $K$ be a compact connected Lie group with Lie algebra $\mathfrak{k}$ and $-\Delta$ the Laplace–Beltrami operator of a bi-invariant metric, a positive essentially self-adjoint operator on $L^2(K)$ commuting with both regular representations. By Peter–Weyl, $L^2(K)$ is the Hilbert sum of the finite-dimensional summands $\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*$, on each of which $-\Delta$ acts as a scalar $\lambda_\pi \geq 0$, the **Casimir eigenvalue** of $\pi$: $-\Delta f = \lambda_\pi f$ for $f$ in the summand of $\pi$. Hence the heat semigroup is

$$
e^{-t(-\Delta)} f = \sum_{\pi\in\operatorname{Irr}(K)} e^{-\lambda_\pi t}\, \Pi_\pi f ,
$$

where $\Pi_\pi$ is the orthogonal projection onto the coefficient space of $\pi$, and the **heat kernel** is

$$
p_t(x) = \sum_{\pi\in\operatorname{Irr}(K)} e^{-\lambda_\pi t}\,d_\pi\,\chi_\pi(x) ,
$$

the convergence for $t > 0$ being absolute and uniform because $\lambda_\pi \to \infty$ and $\chi_\pi$ is bounded by $d_\pi$, with the Weyl asymptotics controlling the growth. This is the analytic form of the same decomposition: the spectral resolution of the Laplacian is the Peter–Weyl expansion, and for $K = SU(2)$ it gives $p_t(t_\theta) = \sum_{j\geq0} e^{-j(j+1)t}(2j+1)\frac{\sin((2j+1)\theta)}{\sin\theta}$, with $-\Delta$ normalised so that the Casimir eigenvalue of $V_j$ is $j(j+1)$.

**Example (the circle and $SU(2)$).** For $K = S^1$ the Peter–Weyl basis is $\{e^{2\pi i n\theta}\}_{n\in\mathbb{Z}}$ and the heat kernel is the Jacobi theta function $\sum_{n\in\mathbb{Z}}e^{-4\pi^2n^2t}e^{2\pi in\theta}$. For $K = SU(2)$ the summands are the $V_j$ with $d_j = 2j+1$ and the characters $\chi_j(t_\theta) = \sin((2j+1)\theta)/\sin\theta$, and the summand $V_j\otimes V_j^*$ has dimension $(2j+1)^2$; the two examples are the two ends of the classification of the simply connected compact groups of rank one.

## The Abelian Case

**Theorem.** If $K$ is compact abelian, then every irreducible unitary representation is one-dimensional, $\operatorname{Irr}(K)$ is the discrete group $K^\vee$ of characters, Peter–Weyl reduces to the statement that the characters form an orthonormal basis of $L^2(K)$, and the expansion is the Fourier series of *Harmonic Analysis on Groups*, §The Standard Cases. The density statement is the completeness of the trigonometric system, and the multiplicity statement of the previous section becomes the statement that each character occurs once, $d_\pi = 1$.

**Proof.** A finite-dimensional irreducible unitary representation of an abelian group is one-dimensional by Schur's lemma applied to the commuting operators $\pi(k)$; the orthogonality relation becomes $\int_K\chi\overline{\sigma} = \delta_{\chi\sigma}$, and completeness of the characters in $L^2(K)$ is (b). The identification $\operatorname{Irr}(K) = K^\vee$ and the discreteness of the dual are the duality theory of *Abelian Topological Groups* and *Pontryagin Duality*, quoted. $\square$

**Remark (duality recovered).** Conversely, the abelian Peter–Weyl theorem together with the Gelfand theory of $L^1(K)$ proves that the dual of a compact abelian group is discrete and that $\operatorname{Irr}(K) = K^\vee$; this is one direction of Pontryagin duality, and it illustrates that the compact theory contains the abelian theory as its commutative case.

## Summary

The Peter–Weyl theorem states that for a compact group $K$ the representative-function algebra $A(K)$ is dense in $C(K)$ and in every $L^p(K)$, that the functions $\sqrt{d_\pi}\,\pi_{ij}$ form an orthonormal basis of $L^2(K)$ so that $L^2(K)\cong\bigoplus_{\pi}(\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*)$ with the irreducible $\pi$ of dimension $d_\pi$ occurring with multiplicity $d_\pi$, that every unitary representation of $K$ is a Hilbert direct sum of finite-dimensional irreducibles (**Weyl's theorem**), and that the characters form an orthonormal basis of the class functions. The proof is analytic: for $f \in L^2(K)$ the convolution operator $T_f h = f*h$ is Hilbert–Schmidt and hence compact; for a central $f = h*h^{\#}$ it is nonzero compact self-adjoint, and its eigenspaces are finite-dimensional and invariant under both regular representations, so $K$ has a finite-dimensional irreducible constituent; the coefficient space is then a self-adjoint algebra containing the constants, and it separates points because the left regular representation is faithful and the finite-dimensional invariant subspaces are cofinal; Stone–Weierstrass gives density, and Schur's lemma gives orthogonality and completeness. The consequences are the algebraic decomposition $L(K)\cong\bigoplus_\pi\operatorname{End}(\mathcal{H}_\pi)$, the separation of points by finite-dimensional representations and the Gelfand–Raĭkov property for compact groups, the class-function expansion in characters, the diagonalisation of the Laplacian on a compact Lie group and the trace of the heat semigroup, and — in the abelian case — the Fourier series of harmonic analysis on the circle and its dual group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | Compact Hausdorff group |
| $dk$, $\int_K dk = 1$ | Normalised Haar measure |
| $\operatorname{Irr}(K)$ | Equivalence classes of irreducible unitary representations |
| $\mathcal{H}_\pi$, $d_\pi$ | Representation space and its finite dimension |
| $\pi_{ij}(k) = \langle\pi(k)e_j,e_i\rangle$ | Matrix coefficients |
| $\chi_\pi = \operatorname{Tr}\pi$ | Character |
| $\lambda$, $\rho$ | Left and right regular representations on $L^2(K)$ |
| $T_f h = f*h$ | Convolution operator with $f$ |
| $h^{\#}(x) = \overline{h(x^{-1})}$ | The adjoint-producing involution |
| $A(K)$ | Representative-function algebra, span of matrix coefficients |
| $e^\pi_{ij} = \sqrt{d_\pi}\,\pi_{ij}$ | Orthonormal basis of $L^2(K)$ |
| $\hat f(\pi) = \int_K f(k)\pi(k)\,dk$ | Fourier transform |
| $\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*$ | Coefficient space of $\pi$, carrying $\pi\boxtimes\bar\pi$ |
| $\lambda_\pi(f) = \int_K f\overline{\chi_\pi}\,dk$ | Character transform of a class function |
| $-\Delta$, $\lambda_\pi$ | Laplace operator and Casimir eigenvalue |
| $p_t(x) = \sum_\pi e^{-\lambda_\pi t}d_\pi\chi_\pi(x)$ | Heat kernel on a compact Lie group |



## Further Reading

- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, 2nd ed. 2015), for the Peter–Weyl theorem, its proof through compact operators, and the compact-group transform.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis II* (Springer, 1970), for the general compact case and the historical development.
- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953; reprinted Dover, 2011), for the theorem in the form of a structure theorem for group algebras.
- Jean-Pierre Serre, *Linear Representations of Finite Groups* (Springer, 1977), for the finite-group case and the Wedderburn decomposition.
- Theodor Bröcker and Tammo tom Dieck, *Representations of Compact Lie Groups* (Springer, 1985), for the compact Lie case, the Casimir eigenvalues and the heat kernel.
- Kenneth R. Davidson, *$\mathrm{C}^*$-Algebras by Example* (Fields Institute Monographs, 1996), for the group algebra and the von Neumann algebra as completions of the transform image.
- M. A. Naimark, *Normed Algebras* (Wolters-Noordhoff, 1972), for the algebraic treatment of the decomposition and the structure of the group algebra.
- Walter Rudin, *Functional Analysis* (McGraw–Hill, 2nd ed. 1991), for the Hilbert-space spectral theory, the compact and Hilbert–Schmidt operators and the Banach-algebra foundations quoted as standard.
