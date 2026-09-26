
# __Analysis on Compact Groups__

## Introduction

A compact group is the one non-abelian case in which harmonic analysis is as explicit as in the abelian case. The Haar measure can be normalised to a probability measure, every irreducible unitary representation is finite-dimensional, and the regular representation is the direct sum of its irreducible constituents with finite multiplicity. The resulting theory — the operator-valued Fourier transform indexed by the unitary dual, the orthogonality relations for matrix coefficients and characters, the inversion and Plancherel formulas, the algebra of representative functions — is the compact half of non-commutative harmonic analysis, and it is where the general theory can be proved rather than quoted.

The article develops the analysis on a compact group: the function spaces, the convolution algebra, the transform, the orthogonality relations, the inversion and Plancherel formulas, the structure of the dual, and the classical examples. The decomposition theorem and its proof lie outside this article, which is not relied on here: the present article states that theorem as standard and reads it as analysis rather than as representation theory. The boundary with Part II is the one fixed for the whole block.

- The **representation theory** — unitary representations, irreducibility, intertwiners, induced representations, Mackey theory, the type classification, property (T) — belongs to Part II: *Representation Theory of Locally Compact Groups*, *Induced Representations of Locally Compact Groups*, *Mackey Theory* and *Type I Groups*. In particular, the fact that the compact group's irreducible representations are finite-dimensional and that every unitary representation is a direct sum of irreducibles is the **Peter–Weyl theorem**, proved in this category; it is quoted here.
- The **Haar measure**, its invariance and its uniqueness are *Locally Compact Groups and Haar Measure*; the general measure and integration theory is *Measure Theory and Integration*, and the comparison of modes of convergence is *Modes of Convergence*, both in the Foundations slot of this Part. The functional analysis — Hilbert spaces, orthonormal bases, the spectral theorem for compact self-adjoint operators, Hilbert–Schmidt operators — is standard and is quoted as it is used, later in the Analysis on Linear Spaces slot, being where this Part develops it.
- The general abelian theory, the transform and the dual group, is *Harmonic Analysis on Groups* in this category; the non-compact non-abelian theory and the general convolution algebra lie outside this article.

Throughout, $K$ is a compact Hausdorff group, $dk$ its Haar measure normalised by $\int_K dk = 1$, and $\operatorname{Irr}(K)$ the set of equivalence classes of irreducible unitary representations. For $\pi \in \operatorname{Irr}(K)$ the representation space is $\mathcal{H}_\pi$, of dimension $d_\pi = \dim\mathcal{H}_\pi < \infty$, the inner product is linear in the second variable, and the **matrix coefficient** is $c^\pi_{u,v}(k) = \langle \pi(k)u, v\rangle$; when an orthonormal basis $(e_i)$ of $\mathcal{H}_\pi$ is fixed we write $\pi_{ij}(k) = c^\pi_{e_j,e_i}(k) = \langle \pi(k)e_j, e_i\rangle$ and $\chi_\pi(k) = \operatorname{Tr}\pi(k)$ for the **character**. The unitary dual is written $\operatorname{Irr}(K)$ and not $\widehat{K}$, the hat being reserved for completions. No physics is invoked.

## Haar Measure and the Function Spaces

### Normalised Haar Measure and Unimodularity

A compact group is unimodular: the modular function $\Delta$ is a continuous homomorphism $K \to (0,\infty)$ and its image is a compact subgroup of $(0,\infty)$, hence $\{1\}$. Left Haar measure is therefore right-invariant, and it is finite, since $K$ is compact; dividing by the total mass gives the unique **normalised Haar measure** $dk$ with $\int_K dk = 1$. The measure is invariant under inversion as well: for $f \in C(K)$,

$$
\int_K f(k^{-1})\,dk = \int_K f(k)\,dk .
$$

**Proof.** The measure $d\tilde k$ defined by $\tilde k = k^{-1}$ is a right Haar measure; unimodularity makes it equal to a left Haar measure, hence to $dk$ times a positive constant, and the constant is $1$ because both measures are probabilities. $\square$

**Example (the classical compact groups).** For $K = S^1 = \mathbb{R}/\mathbb{Z}$ the normalised Haar measure is $d\theta$ of total mass $1$. For $K = T^n$ it is the product measure. For $K = SU(2)$ the normalised Haar measure is fixed by the **Weyl integration formula**

$$
\int_{SU(2)} f\,dk = \frac{2}{\pi}\int_0^\pi f(t_\theta)\,\sin^2\theta\,d\theta , \qquad t_\theta = \operatorname{diag}(e^{i\theta}, e^{-i\theta}),
$$

valid for class functions $f$, the conjugacy class of $t_\theta$ carrying the normalised invariant measure $\frac{2}{\pi}\sin^2\theta\,d\theta$; the constant $\frac{2}{\pi}$ records the total mass $1$, since $\frac{2}{\pi}\int_0^\pi\sin^2\theta\,d\theta = 1$, and the formula is checked against the character orthogonality of the last section.

### The Spaces $L^p(K)$ and the Regular Representation

For $1 \leq p < \infty$ the space $L^p(K)$ is with respect to $dk$; since $dk$ is a probability, Hölder's inequality gives $L^q(K) \subseteq L^p(K)$ for $q \geq p$, and $L^\infty(K)\subseteq L^p(K)$ for every $p$. The **left regular representation** $\lambda$ acts on functions by $(\lambda(k)f)(x) = f(k^{-1}x)$, and it is a unitary representation of $K$ on $L^2(K)$; the right regular representation $\rho$, $(\rho(k)f)(x) = f(xk)$, commutes with it, and on $L^2(K)$ the two combine into the action $(\lambda\otimes\rho)(k_1,k_2)f(x) = f(k_1^{-1}xk_2)$ of $K \times K$.

**Theorem (unitarity).** The left regular representation is a continuous unitary representation of $K$ on $L^2(K)$: for every $f \in L^2(K)$ the map $k \mapsto \lambda(k)f$ is continuous, and $\|\lambda(k)f\|_2 = \|f\|_2$.

**Proof.** Unitarity is the left-invariance of $dk$. Continuity follows by density of $C(K)$ in $L^2(K)$ and the uniform continuity of a continuous function on the compact group: for $f \in C(K)$, $\|\lambda(k)f - f\|_\infty \to 0$ as $k \to e$. $\square$

### Convolution and the Banach Algebra $L^1(K)$

**Definition.** For $f, g \in L^1(K)$ the **convolution** is $(f*g)(x) = \int_K f(y)g(y^{-1}x)\,dy$.

Because $K$ is unimodular and $dy$ is a probability measure, $L^1(K)$ is a Banach algebra with $\|f*g\|_1 \leq \|f\|_1\|g\|_1$; the general theory of the convolution algebra lies outside this article, and the compact case adds two features. First, $L^1(K)$ has a two-sided identity-like element only when $K$ is discrete, but it always has the approximate identity given by the normalised indicator functions of shrinking neighbourhoods of $e$; second, the transform below diagonalises convolution completely.

**Proposition.** $L^1(K)$ is a commutative Banach algebra if and only if $K$ is abelian, and it is a Banach $*$-algebra for the involution $f^*(k) = \overline{f(k^{-1})}$, with $\|f^*\|_1 = \|f\|_1$ and $(f*g)^* = g^* * f^*$.

**Proof.** The norm identity is unimodularity and the invariance of $dk$ under inversion; the involution identity is a change of variable. Commutativity fails for a non-abelian $K$ by the two-element computation of *Harmonic Analysis on Groups*, §Convolution and the Convolution Theorem. $\square$

**Example (convolution on a finite group).** If $K$ is finite with the normalised counting measure, $L^1(K)$ is the group algebra $\mathbb{C}[K]$ with the multiplication of the group algebra scaled by $|K|^{-1}$, and the transform of the next section is the Wedderburn decomposition of $\mathbb{C}[K]$ into full matrix algebras. For $K = S_3$ this is $\mathbb{C}[S_3] \cong \mathbb{C}\oplus\mathbb{C}\oplus M_2(\mathbb{C})$, of dimension $1+1+4=6$.

## The Fourier Transform on a Compact Group

### Definition and the Operator-Valued Transform

**Definition.** For $f \in L^1(K)$ and $\pi \in \operatorname{Irr}(K)$ the **Fourier transform** of $f$ at $\pi$ is the operator

$$
\hat f(\pi) = \int_K f(k)\,\pi(k)\,dk \in \operatorname{End}(\mathcal{H}_\pi) .
$$

Since $\pi(k)$ is unitary and $\|\pi(k)\| = 1$, the integral converges absolutely in the finite-dimensional norm and $\|\hat f(\pi)\| \leq \|f\|_1$. The transform is a map $f \mapsto (\hat f(\pi))_{\pi\in\operatorname{Irr}(K)}$ from functions on $K$ to operator fields on the dual, and it is the compact case of the matrix-valued transform of *Harmonic Analysis on Groups*, §The Matrix-Valued Transform.

**Proposition (elementary properties).** For $f, g \in L^1(K)$, $x \in K$ and $\pi \in \operatorname{Irr}(K)$:

**(a)** the transform is linear and $\|\hat f(\pi)\| \leq \|f\|_1$, with $\|\hat f(\pi)\|_{\mathrm{HS}} \leq \sqrt{d_\pi}\,\|f\|_1$;

**(b)** $\widehat{\lambda(x)f}(\pi) = \pi(x)\hat f(\pi)$ and $\widehat{\rho(x)f}(\pi) = \hat f(\pi)\pi(x)^{-1}$;

**(c)** $\widehat{f^*}(\pi) = \hat f(\pi)^*$, where ${}^*$ is the conjugate transpose;

**(d)** for a **class function** $f$ — one with $f(xkx^{-1}) = f(k)$ for all $x, k\in K$ — the operator $\hat f(\pi)$ is a scalar multiple of the identity, $\hat f(\pi) = \lambda_\pi(f)\,I$ with

$$
\lambda_\pi(f) = \frac{1}{d_\pi}\int_K f(k)\,\chi_\pi(k)\,dk .
$$

**Proof.** (a) is the triangle inequality and the finite-dimensional bound $\|\pi(k)\|_{\mathrm{HS}} = \sqrt{d_\pi}$. (b) is the change of variable $k \mapsto x^{-1}k$, respectively $k\mapsto kx^{-1}$, and the multiplicativity of $\pi$. (c) is $(f*g)^*$ with $\pi(k)^* = \pi(k)^{-1} = \pi(k^{-1})$. For (d): for every $x \in K$, $\pi(x)^{-1}\hat f(\pi)\pi(x) = \int f(k)\pi(x^{-1}kx)\,dk = \int f(xkx^{-1})\pi(k)\,dk = \hat f(\pi)$, since $f$ is a class function and $dk$ is invariant; so $\hat f(\pi)$ commutes with every $\pi(x)$, and since $\pi$ is irreducible Schur's lemma gives $\hat f(\pi) = \lambda I$ for some scalar. Taking traces, $\operatorname{Tr}\hat f(\pi) = \int f\operatorname{Tr}\pi = \int f\chi_\pi$ and also $=\lambda d_\pi$, whence $\lambda = d_\pi^{-1}\int f\chi_\pi$. $\square$

**Remark ($\hat f$ is compact).** For $f \in L^2(K)$ the operator $\hat f(\pi)$ is determined and the map $f \mapsto (\hat f(\pi))$ is a Hilbert–Schmidt transform; the compactness of the integral operator $T_f : L^2(K) \to L^2(K)$, $T_f h = f * h$, follows from the finite-dimensionality of the constituents, and it is the mechanism of the Peter–Weyl proof. The operator algebra generated by the transforms is the direct sum of the full matrix algebras $\operatorname{End}(\mathcal{H}_\pi)$, and its weak completion is the group von Neumann algebra $L(K),$ which for compact $K$ is a direct sum of type I factors (see *Operator Algebras* and *Type I Groups*).

### The Convolution Theorem

**Theorem.** For $f, g \in L^1(K)$ and every $\pi \in \operatorname{Irr}(K)$,

$$
\widehat{f*g}(\pi) = \hat f(\pi)\,\hat g(\pi) .
$$

*Proof.* As in the abelian case, substituting $x = yz$ and using the left-invariance of $dz$ and the multiplicativity of $\pi$,

$$
\widehat{f*g}(\pi) = \int_K\int_K f(y)g(z)\,\pi(yz)\,dz\,dy = \left(\int_K f(y)\pi(y)\,dy\right)\left(\int_K g(z)\pi(z)\,dz\right) = \hat f(\pi)\hat g(\pi). \qquad \square
$$

Thus the transform is a homomorphism of the Banach algebra $L^1(K)$ into the algebra of operator fields on the dual with pointwise multiplication, and convolution is diagonalised by the transform exactly as in the abelian case, with the scalar product replaced by operator multiplication.

### Characters

**Definition.** The **character** of $\pi \in \operatorname{Irr}(K)$ is the continuous class function $\chi_\pi(k) = \operatorname{Tr}\pi(k)$.

**Proposition.** The character satisfies $\chi_\pi(e) = d_\pi$, $\chi_\pi(k^{-1}) = \overline{\chi_\pi(k)}$, $|\chi_\pi(k)| \leq d_\pi$, and $\chi_{\pi\oplus\sigma} = \chi_\pi + \chi_\sigma$, $\chi_{\pi\otimes\sigma} = \chi_\pi\chi_\sigma$. The map $\pi \mapsto \chi_\pi$ is injective: two irreducible representations with the same character are equivalent.

**Proof.** The first three statements are the trace, unitarity and the spectral bound; the tensor product formula is multiplicativity of the trace; injectivity is the standard fact that the character determines the representation up to equivalence, proved from the orthogonality relations below together with the decomposition of the tensor product into irreducibles. $\square$

## The Orthogonality Relations

### Matrix Coefficients

The matrix coefficients of the irreducible representations, correctly normalised, form an orthonormal basis of $L^2(K)$. This is the analytic content of the Peter–Weyl theorem, and it is the compact analogue of the statement that the characters form an orthonormal basis of $L^2(G^\vee)$ in the abelian case.

**Theorem (orthogonality).** Let $\pi, \sigma \in \operatorname{Irr}(K)$ and fix orthonormal bases. Then

$$
\int_K \pi_{ij}(k)\,\overline{\sigma_{lm}(k)}\,dk = \frac{1}{d_\pi}\,\delta_{\pi\sigma}\,\delta_{il}\,\delta_{jm} ,
$$

where $\delta_{\pi\sigma} = 1$ if $\pi \cong \sigma$ and $0$ otherwise.

**Proof sketch.** The proof is an application of Schur's lemma to the operator $A = \int_K \sigma(k)^{-1}B\pi(k)\,dk$ for $B \in \operatorname{Hom}(\mathcal{H}_\pi, \mathcal{H}_\sigma)$: the invariance $A\pi(x) = \sigma(x)A$ forces $A = 0$ when $\pi\not\cong\sigma$ and $A = \lambda I$ when $\pi = \sigma$, and taking $B$ a matrix unit and traces gives the display. The computation is the standard one; the representation-theoretic input (Schur's lemma, complete reducibility) is Part II's, and the explicit constant $d_\pi^{-1}$ follows from the normalisation $\int_K dk = 1$ by evaluating at $\pi = \sigma$, $i = l$, $j = m$ and summing over $i,j$ against $\chi_\pi(e) = d_\pi$. $\square$

**Corollary (orthonormal basis).** The functions $e^\pi_{ij} = \sqrt{d_\pi}\,\pi_{ij}$, for $\pi \in \operatorname{Irr}(K)$ and $1 \leq i,j \leq d_\pi$, form an orthonormal family in $L^2(K)$. They form an orthonormal **basis** of $L^2(K)$, and this is the Peter–Weyl theorem; consequently

$$
L^2(K) \cong \bigoplus_{\pi\in\operatorname{Irr}(K)} \bigl(\mathcal{H}_\pi \otimes \mathcal{H}_\pi^*\bigr),
$$

the irreducible $\pi$ appearing with multiplicity $d_\pi = \dim\mathcal{H}_\pi$, realised on the span of the coefficients $\pi_{ij}$ for fixed $\pi$.

**Remark (completeness).** The expansion is over all of $\operatorname{Irr}(K)$, and the series converges in $L^2$; for $f \in L^2(K)$ the **Plancherel series** is

$$
f = \sum_{\pi\in\operatorname{Irr}(K)} d_\pi \sum_{i,j=1}^{d_\pi} \langle f, \pi_{ij}\rangle\,\pi_{ij} ,
$$

where $\langle f, \pi_{ij}\rangle = \int_K f(k)\overline{\pi_{ij}(k)}\,dk$. The convergence is unconditional in $L^2$, and for $f$ in the representative-function algebra of the next section the sum is finite, hence pointwise and uniform.

### Characters and Class Functions

Summing the orthogonality relations over the diagonal gives the orthogonality of characters.

**Corollary (orthogonality of characters).** For $\pi, \sigma \in \operatorname{Irr}(K)$,

$$
\int_K \chi_\pi(k)\,\overline{\chi_\sigma(k)}\,dk = \delta_{\pi\sigma} , \qquad \int_K \chi_\pi(k)\,\chi_\sigma(k)\,dk = \delta_{\pi\bar\sigma},
$$

where $\bar\sigma$ is the contragredient of $\sigma$. In particular the characters form an orthonormal family in $L^2(K)$, and they form an orthonormal basis of the subspace $L^2(K)^K$ of class functions.

**Proof.** The first identity is the orthogonality of matrix coefficients summed over $i = l$ and $j = m$. For the second, $\overline{\chi_\sigma(k)} = \chi_{\bar\sigma}(k)$ because the eigenvalues of $\sigma(k)$ are inverted under conjugation of the representation; the first identity applied to $\pi$ and $\bar\sigma$ gives the display. The characters span the class functions: a class function orthogonal to every $\chi_\pi$ is orthogonal to every matrix coefficient, since averaging over conjugacy classes expresses the projection onto class functions as a combination of characters, so it vanishes by the completeness of the coefficients. $\square$

**Corollary (the character transform).** For a class function $f \in L^2(K)$ the expansion is diagonal,

$$
f = \sum_{\pi\in\operatorname{Irr}(K)} \lambda_\pi(f)\,\chi_\pi , \qquad \lambda_\pi(f) = \int_K f(k)\,\overline{\chi_\pi(k)}\,dk ,
$$

and the Plancherel identity for class functions reads $\|f\|_2^2 = \sum_\pi |\lambda_\pi(f)|^2$. For $f = \chi_\pi$ one has $\lambda_\rho(\chi_\pi) = \delta_{\rho\bar\pi}$.

**Proof.** Combine the scalar form of the transform for class functions with the character orthogonality. $\square$

### The Convolution of Characters and the Coefficient Algebra

**Theorem.** For $\pi, \sigma \in \operatorname{Irr}(K)$ the convolution of characters is

$$
\chi_\pi * \chi_\sigma = \sum_{\tau\in\operatorname{Irr}(K)} m_{\pi\sigma}^{\tau}\,\frac{\chi_\tau}{d_\tau} ,
$$

where $m^\tau_{\pi\sigma}$ is the multiplicity of $\tau$ in the tensor product $\pi\otimes\sigma$. In particular $\chi_\pi * \chi_\sigma = 0$ if and only if the tensor product contains no irreducible constituent, and the coefficient algebra below is closed under convolution.

**Proof.** By the convolution theorem, $\widehat{\chi_\pi * \chi_\sigma}(\tau) = \hat\chi_\pi(\tau)\hat\chi_\sigma(\tau)$; for the class functions $\chi_\pi$, $\chi_\sigma$ these transforms are scalars, and the computation of $\hat\chi_\pi(\tau)$ from the orthogonality relations gives the display, the multiplicities entering through the decomposition of $\pi\otimes\sigma$. The statement is the compact form of the algebra structure of the representation ring, treated in Part II's representation theory. $\square$

**Definition.** The **representative-function algebra** (or coefficient algebra) $A(K)$ is the linear span of all matrix coefficients of the finite-dimensional continuous representations of $K$.

**Theorem.** $A(K)$ is a subalgebra of $C(K)$ closed under conjugation and under convolution, it is invariant under left and right translation, and it is dense in $C(K)$ in the supremum norm and in $L^p(K)$ for every $1 \leq p < \infty$. Its completion as a Banach algebra under the norm

$$
\|f\|_{A} = \sum_{\pi\in\operatorname{Irr}(K)} d_\pi\,\|\hat f(\pi)\|_1
$$

is a Banach $*$-algebra isomorphic to the algebraic direct sum $\bigoplus_{\pi}\operatorname{End}(\mathcal{H}_\pi)$ completed appropriately; in particular $A(K)$ is closed under convolution and the convolution theorem holds inside it without convergence problems.

**Proof.** The set of matrix coefficients is closed under products because $\pi_{ij}\sigma_{lm} = (\pi\otimes\sigma)_{ij,lm}$ is a matrix coefficient of the tensor product, and closed under conjugation because $\overline{\pi_{ij}}$ is a coefficient of the contragredient. Invariance under translation is (b) of the elementary properties. Density in $C(K)$ is the Stone–Weierstrass theorem: $A(K)$ is an algebra containing the constants and closed under conjugation, and it separates points of $K$ because for $x \neq y$ some matrix coefficient of the regular representation separates them. Density in $L^p$ follows from density in $C(K)$ and the finiteness of the measure. $\square$

## The Inversion and Plancherel Formulas

### Inversion

**Theorem (Fourier inversion).** For $f$ in the coefficient algebra $A(K)$ the function is recovered from its transform pointwise and uniformly by

$$
f(k) = \sum_{\pi\in\operatorname{Irr}(K)} d_\pi\,\operatorname{Tr}\bigl(\hat f(\pi)\,\pi(k)^{-1}\bigr) ,
$$

the sum being finite. For $f \in L^2(K)$ the same series converges to $f$ in $L^2(K)$.

**Proof.** For $f$ a matrix coefficient $\pi_{ij}$ one verifies directly from the orthogonality relations; the general case follows by linearity, and the $L^2$ statement by continuity of the transform and the density of $A(K)$ in $L^2(K)$. The finite sum is exact because only finitely many matrix coefficients occur. $\square$

**Corollary (inversion for characters).** For a class function $f = \sum_\pi \lambda_\pi\chi_\pi$ in $A(K)\cap L^2(K)^K$ one has $f(k) = \sum_\pi \lambda_\pi\chi_\pi(k)$, and the transform is scalar; the "Fourier coefficients" of a class function are the numbers $\lambda_\pi = \int_K f\overline{\chi_\pi}\,dk$.

### Plancherel

**Theorem (Plancherel for compact $K$).** For every $f \in L^2(K)$,

$$
\|f\|_2^2 = \int_K |f(k)|^2\,dk = \sum_{\pi\in\operatorname{Irr}(K)} d_\pi\,\|\hat f(\pi)\|_{\mathrm{HS}}^2 ,
$$

where $\|\hat f(\pi)\|_{\mathrm{HS}}^2 = \operatorname{Tr}\bigl(\hat f(\pi)\hat f(\pi)^*\bigr)$. Equivalently, the transform extends to a unitary equivalence of Hilbert spaces

$$
\mathcal{F} : L^2(K) \longrightarrow \bigoplus_{\pi\in\operatorname{Irr}(K)}^{\oplus} \bigl(\mathcal{H}_\pi \otimes \mathcal{H}_\pi^*\bigr),
$$

where the direct summand $\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*$ carries the Hilbert–Schmidt inner product.

**Proof.** The expansion of $f$ in the orthonormal basis $e^\pi_{ij} = \sqrt{d_\pi}\pi_{ij}$ gives $\|f\|_2^2 = \sum_{\pi, i, j} |\langle f, e^\pi_{ij}\rangle|^2$. On the other hand $\langle f, e^\pi_{ij}\rangle = \sqrt{d_\pi}\,\overline{\hat f(\pi)_{ij}}$ from the definition of $\hat f$ and the unitarity of $\pi$, so $\sum_{i,j}|\langle f, e^\pi_{ij}\rangle|^2 = d_\pi\sum_{i,j}|\hat f(\pi)_{ij}|^2 = d_\pi\|\hat f(\pi)\|_{\mathrm{HS}}^2$. Summing over $\pi$ gives the identity; the unitarity statement is its polarised form. $\square$

**Corollary (multiplicity of the regular representation).** In the decomposition of the left regular representation on $L^2(K)$, the irreducible $\pi$ occurs with multiplicity $\dim\mathcal{H}_\pi = d_\pi$, on the span of the coefficients $\pi_{ij}$ for fixed $\pi$; hence $\lambda \cong \bigoplus_{\pi\in\operatorname{Irr}(K)} \pi^{\oplus d_\pi}$.

**Corollary (the trivial trace).** For $f \in L^2(K)$, $\hat f(\pi)$ is the operator whose entries are the Fourier coefficients, and $f(e) = \sum_\pi d_\pi\operatorname{Tr}\hat f(\pi)$ whenever the right-hand side converges absolutely; this is the inversion formula at the identity.

## The Structure of the Dual

### The Dual is Discrete

**Theorem.** For a compact group $K$ the unitary dual $\operatorname{Irr}(K)$ is a discrete set in the Fell topology, every irreducible representation is finite-dimensional, and the group von Neumann algebra $L(K) = \lambda(K)''$ is a direct sum of the matrix algebras $\operatorname{End}(\mathcal{H}_\pi)$ over $\pi \in \operatorname{Irr}(K)$. In particular compact groups are of type I.

**Proof.** Finite-dimensionality and complete reducibility are Peter–Weyl; discreteness of the dual is the isolation of each finite-dimensional irreducible in the Fell topology, since a small perturbation of a finite-dimensional representation retains an irreducible subrepresentation by the character orthogonality; the description of $L(K)$ follows because the coefficients of distinct irreducibles are mutually orthogonal in $L^2$ and each irreducible contributes a full matrix algebra of operators on the corresponding summand. The type-I statement is then Part II's *Type I Groups*, §Examples and Non-Examples. $\square$

**Example (compact abelian).** If $K$ is compact abelian, every irreducible is one-dimensional, $d_\pi = 1$, $\operatorname{Irr}(K) = K^\vee$ is a discrete abelian group, and the formulas above reduce to the abelian inversion and Plancherel of *Harmonic Analysis on Groups*. The circle is the model: $\operatorname{Irr}(S^1) = \mathbb{Z}$ with $\chi_n(\theta) = e^{2\pi i n\theta}$ and $L^2(S^1) \cong \bigoplus_{n\in\mathbb{Z}}\mathbb{C}\chi_n$.

### Products, Tensor Products and Restrictions

**Theorem (the dual of a product).** If $K_1, K_2$ are compact groups then $\operatorname{Irr}(K_1\times K_2) = \operatorname{Irr}(K_1)\times\operatorname{Irr}(K_2)$, with $\pi_1\boxtimes\pi_2(k_1,k_2) = \pi_1(k_1)\otimes\pi_2(k_2)$, $d_{\pi_1\boxtimes\pi_2} = d_{\pi_1}d_{\pi_2}$ and $\chi_{\pi_1\boxtimes\pi_2} = \chi_{\pi_1}\chi_{\pi_2}$. Consequently $L^2(K_1\times K_2)\cong L^2(K_1)\widehat\otimes L^2(K_2)$ under the von Neumann tensor product.

**Theorem (tensor products).** For $\pi, \sigma \in \operatorname{Irr}(K)$ the tensor product decomposes with finite multiplicities,

$$
\pi\otimes\sigma \cong \bigoplus_{\tau\in\operatorname{Irr}(K)} m^{\tau}_{\pi\sigma}\,\tau , \qquad m^\tau_{\pi\sigma} = \int_K \chi_\pi\chi_\sigma\overline{\chi_\tau}\,dk ,
$$

and only finitely many multiplicities are nonzero; the characters multiply as $\chi_{\pi\otimes\sigma} = \chi_\pi\chi_\sigma$. The multiplicities are the structure constants of the representation ring of $K$, whose algebraic theory belongs to Part II.

**Remark (the non-abelian dual is not a group).** Unlike the abelian dual $K^\vee$, the set $\operatorname{Irr}(K)$ carries no group structure for non-abelian $K$: the tensor product of two irreducibles is generally reducible, the "product" of equivalence classes is set-valued, and the identity class is the trivial representation. The dual is a discrete set with the extra structure of a tensor category, and its analysis is the content of this article; the failure is already visible for $K = S_3$, where the tensor product of the two-dimensional irreducible with itself is $\chi_1\oplus\chi_{\mathrm{sgn}}\oplus\rho$ (checked by the dimension count $2\cdot2 = 1+1+2$).

### The Classical Groups

**The circle and the torus.** $\operatorname{Irr}(S^1) = \{\chi_n : n \in \mathbb{Z}\}$ with $\chi_n(\theta) = e^{2\pi i n\theta}$ and $d_n = 1$; the transform is the Fourier series of *Harmonic Analysis on Groups*, §The Standard Cases, and the orthogonality relation is the elementary $\int_0^1 e^{2\pi i(n-m)\theta}d\theta = \delta_{nm}$. For $T^n$ the dual is $\mathbb{Z}^n$ with characters $\chi_m(x) = e^{2\pi i\langle m,x\rangle}$ and the theory is the multiple Fourier series.

**$SU(2)$ and $SO(3)$.** The irreducible unitary representations of $K = SU(2)$ are the symmetric powers $V_j$ of the defining two-dimensional representation, indexed by the **spin** $j \in \frac{1}{2}\mathbb{Z}_{\geq 0}$, of dimension $d_j = 2j+1$. The character is determined by the conjugacy class of the diagonal element $t_\theta = \operatorname{diag}(e^{i\theta},e^{-i\theta})$:

$$
\chi_j(t_\theta) = \frac{\sin\bigl((2j+1)\theta\bigr)}{\sin\theta} , \qquad 0 \leq \theta \leq \pi ,
$$

the sum of the $2j+1$ eigenvalues $e^{2ij\theta}, e^{2i(j-1)\theta}, \dots, e^{-2ij\theta}$. The class functions on $SU(2)$ are the functions of $\theta$, and $L^2(K)^K$ has orthonormal basis $(\chi_j)$ by the character orthogonality, with

$$
\int_{SU(2)} |\chi_j|^2\,dk = \frac{2}{\pi}\int_0^\pi \frac{\sin^2((2j+1)\theta)}{\sin^2\theta}\,\sin^2\theta\,d\theta = \frac{2}{\pi}\int_0^\pi \sin^2((2j+1)\theta)\,d\theta = 1 ,
$$

which is equivalent to $\frac{2}{\pi}\int_0^\pi \sin((2j+1)\theta)\sin((2l+1)\theta)\,d\theta = \delta_{jl}$, and it fixes the normalisation of the Haar measure displayed above. The representations of $SO(3) = SU(2)/\{\pm I\}$ are the $V_j$ with $j \in \mathbb{Z}_{\geq0}$, since the centre acts by $(-1)^{2j}$; the half-integer spins descend to projective representations of $SO(3)$, that is, to genuine representations of its double cover. The matrix coefficients relative to a weight basis $(v_{j,m})_{m=-j,\dots,j}$ of $\mathcal{H}_j$ are the **Wigner $D$-functions** $D^j_{mn}$, and Peter–Weyl says that the functions $\sqrt{2j+1}\,D^j_{mn}$ form an orthonormal basis of $L^2(SU(2))$, the analytic form of the decomposition of the tensor product of two irreducibles.

**Finite groups.** For a finite group $K$ the normalised counting measure makes the theory discrete: $\operatorname{Irr}(K)$ is finite, the orthogonality relation is $\frac{1}{|K|}\sum_{k\in K}\pi_{ij}(k)\overline{\sigma_{lm}(k)} = d_\pi^{-1}\delta_{\pi\sigma}\delta_{il}\delta_{jm}$, and the transform of the group algebra is the decomposition $\mathbb{C}[K] \cong \bigoplus_\pi \operatorname{End}(\mathcal{H}_\pi)$ of Wedderburn–Artin. For $K = S_3$ the dual consists of the trivial, the sign and the two-dimensional reflection representation, of dimensions $1,1,2$, with $\sum_\pi d_\pi^2 = 6 = |K|$; the Plancherel identity is the Parseval identity of the discrete Fourier analysis on $S_3$.

## Summary

On a compact group $K$ the normalised Haar measure $dk$, $\int_K dk = 1$, is bi-invariant and inversion-invariant, and $L^1(K)$ is a Banach $*$-algebra under convolution with the involution $f^*(k) = \overline{f(k^{-1})}$. The Fourier transform $\hat f(\pi) = \int_K f(k)\pi(k)\,dk$ takes values in the finite-dimensional operators $\operatorname{End}(\mathcal{H}_\pi)$, turns convolution into operator multiplication, $\widehat{f*g}(\pi) = \hat f(\pi)\hat g(\pi)$, and is a homomorphism of $L^1(K)$ into the algebra of operator fields on $\operatorname{Irr}(K)$. The orthogonality relations $\int_K\pi_{ij}\overline{\sigma_{lm}} = d_\pi^{-1}\delta_{\pi\sigma}\delta_{il}\delta_{jm}$ make the functions $\sqrt{d_\pi}\pi_{ij}$ an orthonormal basis of $L^2(K)$ (Peter–Weyl), and summing the diagonal gives $\int_K\chi_\pi\overline{\chi_\sigma} = \delta_{\pi\sigma}$ and $\int_K\chi_\pi\chi_\sigma = \delta_{\pi\bar\sigma}$, so that the characters form an orthonormal basis of the class functions. Inversion reads $f(k) = \sum_\pi d_\pi\operatorname{Tr}(\hat f(\pi)\pi(k)^{-1})$ on the coefficient algebra and in $L^2$, and Plancherel reads $\|f\|_2^2 = \sum_\pi d_\pi\|\hat f(\pi)\|_{\mathrm{HS}}^2$; equivalently $L^2(K)\cong\bigoplus_\pi(\mathcal{H}_\pi\otimes\mathcal{H}_\pi^*)$, each irreducible occurring with multiplicity $d_\pi$. The dual is discrete; products have product duals, tensor products decompose with multiplicities $\int\chi_\pi\chi_\sigma\overline{\chi_\tau}$, and the dual is not a group outside the abelian case. The examples are the Fourier series of the circle, the multiple series of the torus, the discrete Fourier analysis of a finite group with its Wedderburn decomposition, and the representation theory of $SU(2)$ and $SO(3)$ with characters $\sin((2j+1)\theta)/\sin\theta$ and the Wigner $D$-functions as the Peter–Weyl basis.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | Compact Hausdorff group |
| $dk$, $\int_K dk = 1$ | Normalised Haar measure |
| $e$ | Identity of $K$ |
| $\operatorname{Irr}(K)$ | Set of equivalence classes of irreducible unitary representations |
| $\mathcal{H}_\pi$, $d_\pi = \dim\mathcal{H}_\pi$ | Representation space and its finite dimension |
| $\pi_{ij}(k) = \langle\pi(k)e_j,e_i\rangle$ | Matrix coefficients in an orthonormal basis |
| $c^\pi_{u,v}(k) = \langle\pi(k)u,v\rangle$ | Matrix coefficient, basis-free |
| $\chi_\pi(k) = \operatorname{Tr}\pi(k)$ | Character |
| $\bar\pi$ | Contragredient of $\pi$ |
| $\lambda$, $\rho$ | Left and right regular representations on $L^2(K)$ |
| $(f*g)(x) = \int_K f(y)g(y^{-1}x)\,dy$ | Convolution |
| $f^*(k) = \overline{f(k^{-1})}$ | Involution of $L^1(K)$ |
| $\hat f(\pi) = \int_K f(k)\pi(k)\,dk$ | Operator-valued Fourier transform |
| $\|\hat f(\pi)\|_{\mathrm{HS}}$ | Hilbert–Schmidt norm |
| $e^\pi_{ij} = \sqrt{d_\pi}\,\pi_{ij}$ | Orthonormal basis of $L^2(K)$ |
| $A(K)$ | Representative-function (coefficient) algebra |
| $\lambda_\pi(f) = d_\pi^{-1}\int_K f\chi_\pi\,dk$ | Scalar transform of a class function |
| $m^\tau_{\pi\sigma}$ | Multiplicity of $\tau$ in $\pi\otimes\sigma$ |
| $D^j_{mn}$ | Wigner matrix coefficients of $SU(2)$ |
| $L(K) = \lambda(K)''$ | Group von Neumann algebra of $K$ |





## Further Reading

- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, 2nd ed. 2015), for the transform, orthogonality, inversion and Plancherel theorems on compact groups.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis II* (Springer, 1970), for the detailed theory of the compact case and its classical examples.
- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953; reprinted Dover, 2011), for the Peter–Weyl theorem and the algebra of representative functions.
- Jean-Pierre Serre, *Linear Representations of Finite Groups* (Springer, 1977), for the finite-group case in the form used here.
- Theodor Bröcker and Tammo tom Dieck, *Representations of Compact Lie Groups* (Springer, 1985), for the classification of the irreducible representations of the classical compact groups.
- Anthony W. Knapp, *Representation Theory of Semisimple Groups* (Princeton, 1986), for the analytic treatment of $SU(2)$, $SO(3)$ and their characters.
- Daniel Bump, *Lie Groups* (Springer, 2nd ed. 2013), for the character formulas and the Wigner coefficients of $SU(2)$.
- Walter Rudin, *Functional Analysis* (McGraw–Hill, 2nd ed. 1991), for the Hilbert-space spectral theory, the compact and Hilbert–Schmidt operators and the Banach-algebra foundations quoted as standard.
