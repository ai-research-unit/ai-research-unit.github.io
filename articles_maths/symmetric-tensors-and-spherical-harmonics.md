# __Symmetric Tensors and Spherical Harmonics__

## Introduction

This article is the second application of the category, and it identifies the symmetric powers of *Symmetric Powers* with the harmonic layers of the polynomial algebra. The symmetric-tensor statements hold over a field $F$ of characteristic $0$, so that all factorials are invertible and the symmetric power is the module of invariants; the polynomial algebra is that of *The Symmetric Algebra*, and the symmetric powers are its graded pieces $\operatorname{Sym}^k$.

Let $V = \mathbb{R}^n$ with its standard inner product and let $P_k$ be the space of homogeneous polynomials of degree $k$ in $x_1, \ldots, x_n$. The **Laplacian** $\Delta = \sum_i \partial_i^2$ maps $P_k$ to $P_{k-2}$, and the **harmonic polynomials** of degree $k$ are

$$
\mathcal{H}_k = \{f \in P_k : \Delta f = 0\}.
$$

The two structures are the same up to a trace: symmetric powers of the dual are polynomials, and the harmonic polynomials are the symmetric tensors that are trace-free. The restriction of $\mathcal{H}_k$ to the unit sphere $S^{n-1}$ consists of eigenfunctions of the spherical Laplacian, and the resulting **spherical harmonics** decompose the functions on the sphere into orthogonal layers.

The article defines symmetric tensors and their contraction with the metric, develops the decomposition $P_k = \mathcal{H}_k \oplus r^2 P_{k-2}$, proves the orthogonality and eigenvalue properties of the spherical harmonics, and computes the dimension of each layer together with the trace-free interpretation. All mathematics is real; no physical interpretation of the harmonics is used.

## Symmetric Tensors

### Symmetric Powers and Symmetric Tensors

Let $V$ be a finite-dimensional vector space over a field $F$ of characteristic $0$ and let $V^*$ be its dual. By *Symmetric Powers*, the $k$-fold symmetric power $\operatorname{Sym}^k(V^*)$ is the quotient of the $k$-fold tensor power $(V^*)^{\otimes k}$ by the subspace spanned by the tensors $\varphi_1 \otimes \cdots \otimes \varphi_k - \varphi_{\sigma(1)}\otimes\cdots\otimes\varphi_{\sigma(k)}$ for $\sigma$ in the symmetric group $S_k$. An element of $\operatorname{Sym}^k(V^*)$ is a **symmetric tensor** of rank $k$, that is, a $k$-linear form $\varphi : V^k \to F$ invariant under permutation of its arguments. In characteristic $0$ the symmetric power is canonically the module of $S_k$-invariant elements of $(V^*)^{\otimes k}$, so this use of the term agrees with the invariants that *Symmetric Powers* calls symmetric tensors in the strict sense.

**Proposition.** If $V$ has basis $e_1, \ldots, e_n$ with dual basis $e^1, \ldots, e^n$ defined by $e^i(e_j) = \delta^i_j$, then the products $e^{i_1}\cdots e^{i_k}$ with $i_1 \leq \cdots \leq i_k$ are a basis of $\operatorname{Sym}^k(V^*)$. Hence

$$
\dim \operatorname{Sym}^k(V^*) = \binom{n+k-1}{k}.
$$

*Proof.* The monomials in the $e^i$ of degree $k$ span the symmetric power under the multiplication $\operatorname{Sym}^i\times\operatorname{Sym}^j\to\operatorname{Sym}^{i+j}$, and the commutative law identifies all orderings of the factors; the nondecreasing multi-indices parametrise the distinct monomials. Independence follows by evaluating on the symmetric tensors $e_{i_1}\cdots e_{i_k}$, whose coordinates are $\delta$-symbols. $\square$

**Example.** $\operatorname{Sym}^2(V^*)$ has dimension $\binom{n+1}{2}$ and is the space of quadratic forms; its basis is $e^ie^j$ for $i\leq j$. The space $\operatorname{Sym}^k(V^*)$ is canonically the space $P_k$ of homogeneous polynomials of degree $k$ in the coordinate functions, and this identification is used throughout.

### Symmetric Tensors under the Orthogonal Group

Assume $F = \mathbb{R}$ and let $V = \mathbb{R}^n$ carry the standard positive definite inner product $g$, with $g_{ij} = \delta_{ij}$. The **orthogonal group** $O(n)$ acts on $\operatorname{Sym}^k(V^*)$ by $(g\varphi)(v_1,\ldots,v_k) = \varphi(g^{-1}v_1,\ldots,g^{-1}v_k)$, and this action determines the structure of the layer. Inside $\operatorname{Sym}^k(V^*)$ sits the image of the **contraction** with the metric,

$$
\operatorname{Sym}^{k-2}(V^*) \longrightarrow \operatorname{Sym}^k(V^*), \qquad \varphi \longmapsto g\,\varphi,
$$

which lowers the rank by two by summing over a pair of indices with the metric and its inverse. The **trace-free** or **harmonic** symmetric tensors are the kernel of a dual contraction; when the metric is the identity the contraction is the Laplacian and the trace-free tensors are exactly the harmonic polynomials defined below.

**Proposition.** The trace-free symmetric tensors of rank $k$ on $\mathbb{R}^n$ form a subspace of dimension $\binom{n+k-1}{k} - \binom{n+k-3}{k-2}$ for $k \geq 2$, and this is the dimension of $\mathcal{H}_k$.

The equality of dimensions is established in the last section together with the decomposition; it is the tensor form of the isomorphism between harmonic polynomials and trace-free symmetric tensors.

## Harmonic Polynomials

### The Laplacian

Let $P_k$ be the space of homogeneous polynomials of degree $k$ in $x_1, \ldots, x_n$ over $\mathbb{R}$, and let

$$
\Delta = \sum_{i=1}^{n}\frac{\partial^2}{\partial x_i^2} : P_k \longrightarrow P_{k-2}
$$

be the Laplacian; it is a linear map decreasing the degree by two. A polynomial is **harmonic** if $\Delta f = 0$, and

$$
\mathcal{H}_k = \ker\bigl(\Delta : P_k \to P_{k-2}\bigr) .
$$

**Example.** Every element of $P_0$ and of $P_1$ is harmonic, so $\mathcal{H}_0 = P_0$ and $\mathcal{H}_1 = P_1$. In $P_2$ the harmonic polynomials are the traceless quadratic forms; for $n = 3$ a basis is $xy$, $yz$, $zx$, $x^2 - y^2$, $x^2 - z^2$, so $\dim\mathcal{H}_2 = 5$.

### The Fundamental Decomposition

Write $r^2 = x_1^2 + \cdots + x_n^2$ for the squared distance from the origin.

**Lemma.** For any polynomial $h$, the Laplacian of $r^2 h$ is

$$
\Delta(r^2 h) = 4\,x\cdot\nabla h + 2n\,h + r^2\,\Delta h .
$$

*Proof.* The product rule gives $\Delta(r^2 h) = (\Delta r^2)h + 2\nabla r^2 \cdot \nabla h + r^2 \Delta h$, and $\nabla r^2 = 2x$, $\Delta r^2 = 2n$, so $2\nabla r^2\cdot\nabla h = 4\,x\cdot\nabla h$. $\square$

If $h$ is homogeneous of degree $k - 2$, then $x \cdot \nabla h = (k-2)h$ by Euler's relation, and the lemma reads

$$
\Delta(r^2 h) = \bigl(2n + 4(k-2)\bigr) h + r^2 \Delta h , \qquad h \in P_{k-2} .
$$

**Theorem (harmonic decomposition).** For each $k \geq 0$,

$$
P_k = \mathcal{H}_k \oplus r^2 P_{k-2},
$$

and iterating,

$$
P_k = \bigoplus_{j=0}^{\lfloor k/2\rfloor} r^{2j}\,\mathcal{H}_{k-2j} .
$$

*Proof.* Put $m = k - 2$ and filter $P_m$ by the submodules $F_j = r^{2j}P_{m-2j}$, $j \geq 0$, a descending chain with $F_0 = P_m$ and $F_j = 0$ for $2j > m$. The operator

$$
T = \Delta \circ (r^2\,\cdot) : P_{m} \longrightarrow P_{m}, \qquad T(h) = c_k h + r^2\,\Delta h, \qquad c_k = 2n + 4(k-2),
$$

preserves the filtration. Indeed, for $g \in P_{m-2j}$ and $u = r^{2j}g$, the product rule applied to $r^{2(j+1)}g$ gives

$$
\Delta\bigl(r^{2j+2}g\bigr) = \beta_j\, r^{2j} g + r^{2j+2}\Delta g, \qquad \beta_j = 2(j+1)\bigl(n + 2k - 4 - 2j\bigr),
$$

using $x\cdot\nabla g = (m-2j)g$; the second summand lies in $F_{j+1}$, so $T$ induces the scalar $\beta_j$ on each graded piece $F_j/F_{j+1}$. For $0 \leq j \leq m/2$ one has $n + 2k - 4 - 2j \geq n + k - 2 \geq 1$, so every $\beta_j$ is nonzero over $\mathbb{R}$, and a triangular operator with nonzero diagonal is invertible. Hence $T$ is invertible, so

$$
\Delta\bigl(r^2 P_{k-2}\bigr) = P_{k-2}
$$

and $\Delta : P_k \to P_{k-2}$ is surjective; therefore $\dim\mathcal{H}_k = \dim P_k - \dim P_{k-2}$. The intersection $r^2P_{k-2}\cap\mathcal{H}_k$ is zero, because $r^2h\in\mathcal{H}_k$ means $T(h) = \Delta(r^2h) = 0$, and $T$ is invertible. Hence the sum $\mathcal{H}_k + r^2P_{k-2}$ is direct of dimension $\dim P_k$, so it equals $P_k$. Iterating the identity gives the second formula. $\square$

**Remark.** The first graded diagonal is $\beta_0 = c_k$, recovering the lemma; the later ones differ from it, since $\Delta$ does not respect the decomposition by harmonic degree but only the filtration by powers of $r^2$.

**Corollary.** $\dim\mathcal{H}_k = \dim P_k - \dim P_{k-2}$ for $k \geq 2$, and $\mathcal{H}_0 = P_0$, $\mathcal{H}_1 = P_1$.

## Spherical Harmonics

### Restriction to the Sphere

Let $S^{n-1} = \{x \in \mathbb{R}^n : r^2 = 1\}$ be the unit sphere with surface measure $d\sigma$. The restriction of a polynomial to the sphere is not injective on $P_k$ if $k \geq 2$, because $r^2 - 1$ vanishes there; the following theorem shows that it is injective on each harmonic layer and identifies the images.

**Theorem.** The restriction map $\mathcal{H}_k \to C^{\infty}(S^{n-1})$, $f \mapsto f|_{S^{n-1}}$, is injective.

*Proof.* Suppose $f \in \mathcal{H}_k$ vanishes on the sphere. Since $f$ is homogeneous of degree $k$, the identity $f(x) = r^k f(x/r)$ holds for $x \neq 0$, and the right hand side vanishes whenever $r = 1$; by homogeneity $f$ vanishes on every sphere $r = \rho$, hence on all of $\mathbb{R}^n$ except possibly the origin, and by continuity everywhere. $\square$

The images of the layers are the **spherical harmonics**. The elements of $\mathcal{H}_k|_{S^{n-1}}$ are eigenfunctions of the spherical Laplacian.

**Theorem.** Let $\Delta_{S}$ be the Laplace–Beltrami operator of $S^{n-1}$. For $f \in \mathcal{H}_k$,

$$
\Delta_S f = -k(k + n - 2)\, f .
$$

*Proof.* In polar coordinates the Euclidean Laplacian is $\Delta = \partial_r^2 + \frac{n-1}{r}\partial_r + \frac{1}{r^2}\Delta_S$. For a homogeneous harmonic $f$ of degree $k$ one has $\partial_r^2 f = k(k-1)r^{k-2}\tilde f$ and $\frac{n-1}{r}\partial_r f = (n-1)k r^{k-2}\tilde f$, where $\tilde f = f|_{S^{n-1}}$. Hence

$$
0 = \Delta f = r^{k-2}\Bigl(k(k-1) + (n-1)k\Bigr)\tilde f + r^{k-2}\Delta_S \tilde f ,
$$

and $\Delta_S\tilde f = -k(k-1) - (n-1)k\,\tilde f = -k(k+n-2)\tilde f$. $\square$

**Example.** For $n = 3$ the eigenvalue is $-k(k+1)$, so the spherical harmonics of degrees $0, 1, 2$ have eigenvalues $0, -2, -6$. The polynomial $f = x^2 - y^2$ restricts to the sphere as $\sin^2\theta\cos2\varphi$, and a direct computation of $\Delta_{S^2}$ gives $\Delta_{S^2} f = -6f$, in agreement with the theorem.

### Orthogonality

**Theorem.** For $j \neq k$, the layers $\mathcal{H}_j$ and $\mathcal{H}_k$ are orthogonal in $L^2(S^{n-1}, d\sigma)$.

*Proof.* Let $f \in \mathcal{H}_j$, $h \in \mathcal{H}_k$ and consider the vector field $F = h\,\nabla f - f\,\nabla h$. Its divergence is

$$
\nabla\cdot F = h\,\Delta f - f\,\Delta h = 0 .
$$

Integrating over the unit ball $B$ and applying the divergence theorem,

$$
0 = \int_B \nabla\cdot F\,dV = \int_{S^{n-1}} \langle F, x\rangle\,d\sigma = \int_{S^{n-1}}\bigl(h\,\partial_r f - f\,\partial_r h\bigr)d\sigma ,
$$

because the outward normal to the ball on the sphere is $x$. Since $f$ and $h$ are homogeneous, Euler's relation gives $\partial_r f = j f$ and $\partial_r h = k h$, so

$$
0 = (j - k)\int_{S^{n-1}} f h\,d\sigma ,
$$

and $j \neq k$ gives the orthogonality. $\square$

**Corollary.** The restrictions of distinct harmonic layers are orthogonal on the sphere, and within each layer the $O(n)$-action is irreducible; the spaces $\mathcal{H}_k$ are the irreducible components of the natural action of $O(n)$ on the polynomial algebra.

The completeness of the spherical harmonics is the statement of Peter–Weyl for the compact group $O(n)$, or equivalently of the density of the polynomial algebra in $C(S^{n-1})$: every continuous function on the sphere can be uniformly approximated by polynomials, and the harmonic decomposition of the polynomials gives the orthogonal expansion. This is standard and is quoted.

### Zonal Harmonics and the Addition Theorem

Fix a unit vector $y \in S^{n-1}$. By the irreducibility of the $O(n)$-action on $\mathcal{H}_k$, the subspace fixed by the stabiliser $\mathrm{Stab}(y) \cong O(n-1)$ is one-dimensional; its generator is the **zonal harmonic** $Z_k(\cdot, y)$, characterised by the reproducing property

$$
f(y) = \int_{S^{n-1}} f(x)\, Z_k(x, y)\, d\sigma(x), \qquad f \in \mathcal{H}_k .
$$

The zonal harmonic depends only on the inner product $\langle x, y\rangle$, so it is a function $Z_k(t)$ of one variable $t = \cos\gamma$, where $\gamma$ is the geodesic distance between $x$ and $y$; up to normalisation it is the **Gegenbauer** or **ultraspherical polynomial** $C_k^{(n/2 - 1)}(t)$. For $n = 3$ this is the Legendre polynomial, and the reproducing kernel is $(2k+1)P_k(t)/(4\pi)$.

The reproducing property for an orthonormal basis $Y_{k1}, \ldots, Y_{kd}$ of $\mathcal{H}_k$ reads $Z_k(x,y) = \sum_{j} Y_{kj}(x)\overline{Y_{kj}(y)}$, and taking $n = 3$, where $d = 2k+1$, gives the classical **addition theorem**

$$
P_k(\cos\gamma) = \frac{4\pi}{2k+1}\sum_{m=-k}^{k} Y_{km}(\theta, \phi)\,\overline{Y_{km}(\theta', \phi')} ,
$$

with $\cos\gamma = \cos\theta\cos\theta' + \sin\theta\sin\theta'\cos(\phi - \phi')$. The rewriting of the kernel in the single variable $t$ is the general addition theorem for the harmonic layers; it expresses the reproducing kernel of each irreducible summand of the polynomial algebra in terms of a single classical special function.

## Dimensions of the Layers

### The Dimension Formula

**Theorem.** For $k \geq 2$,

$$
\dim\mathcal{H}_k = \binom{n+k-1}{k} - \binom{n+k-3}{k-2} = \frac{(2k+n-2)\,(k+n-3)!}{k!\,(n-2)!} ,
$$

while $\dim\mathcal{H}_0 = 1$ and $\dim\mathcal{H}_1 = n$.

*Proof.* The first equality is the corollary of the decomposition theorem, and the second is the algebraic simplification of the difference of the two binomial coefficients, using $\binom{n+k-3}{k-2} = \frac{(n+k-3)!}{(k-2)!\,(n-1)!}$. $\square$

**Example.** For $n = 3$, $\dim\mathcal{H}_k = 2k+1$, the classical dimension of the degree-$k$ spherical harmonics on the two-sphere. For $n = 4$, $\dim\mathcal{H}_k = (k+1)^2$. For $n = 2$, $\dim\mathcal{H}_k = 2$ for every $k \geq 1$: the harmonic homogeneous polynomials of degree $k$ in two variables are spanned by the real and imaginary parts of $z^k$. The dimensions for small $n$ and $k$ are

| $k$ | $n = 2$ | $n = 3$ | $n = 4$ | $n = 5$ |
|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 1 |
| 1 | 2 | 3 | 4 | 5 |
| 2 | 2 | 5 | 9 | 14 |
| 3 | 2 | 7 | 16 | 30 |
| 4 | 2 | 9 | 25 | 55 |

**Corollary.** The restrictions to the sphere of the polynomials of degree at most $K$ span $\bigoplus_{k \leq K}\mathcal{H}_k|_{S^{n-1}}$, of dimension

$$
\sum_{k=0}^{K}\dim\mathcal{H}_k = \dim P_K + \dim P_{K-1} = \binom{n+K-1}{K} + \binom{n+K-2}{K-1},
$$

by telescoping, with the second term omitted for $K = 0$. For $n = 3$ this dimension is $(K+1)^2$, the classical count of the spherical harmonics of degree at most $K$ on the two-sphere.

### Trace-Free Tensors

The harmonic layers and the trace-free symmetric tensors are the same object, read through the metric.

**Theorem.** Under the identification of $P_k$ with $\operatorname{Sym}^k(V^*)$, the harmonic polynomials of degree $k$ correspond exactly to the symmetric tensors of rank $k$ that are trace-free with respect to $g$, and the trace-free symmetric tensors of rank $k$ form a subspace of dimension $\dim\mathcal{H}_k$.

*Proof.* The Laplacian on polynomials corresponds to the metric contraction on symmetric tensors: with the standard form, $\Delta$ is the contraction of two indices by $\delta^{ij}$, so $\Delta f = 0$ is exactly the trace-free condition. The dimensions agree by the formula above. $\square$

**Corollary.** The dimension of the space of quadratic forms on $\mathbb{R}^n$ is $\binom{n+1}{2} = \tfrac{n(n+1)}{2}$, and the trace-free part has dimension $\binom{n+1}{2} - 1 = \tfrac{n(n+1)}{2} - 1$, which for $n = 3$ is $5$, the number of independent harmonic quadratics. The decomposition $P_2 = \mathcal{H}_2 \oplus r^2 P_0$ separates the quadratic form into its trace part $\tfrac{\operatorname{tr} Q}{n}r^2$ and its trace-free part, and this is the spectral decomposition of a quadratic form into its mean and its traceless component.

## Summary

Let $V = \mathbb{R}^n$ with its standard inner product. The symmetric tensors of rank $k$ on $V^*$ are the symmetric powers $\operatorname{Sym}^k(V^*)$, of dimension $\binom{n+k-1}{k}$, and they are the homogeneous polynomials of degree $k$. The Laplacian $\Delta : P_k \to P_{k-2}$ defines the harmonic polynomials $\mathcal{H}_k = \ker\Delta$, and the fundamental decomposition is

$$
P_k = \mathcal{H}_k \oplus r^2 P_{k-2}, \qquad P_k = \bigoplus_{j=0}^{\lfloor k/2\rfloor} r^{2j}\mathcal{H}_{k-2j},
$$

proved from the identity $\Delta(r^2 h) = (2n+4(k-2))h + r^2\Delta h$ on $P_{k-2}$ and the downward induction on the degree. The restriction of $\mathcal{H}_k$ to the unit sphere is injective, its image consists of eigenfunctions of the spherical Laplacian with eigenvalue $-k(k+n-2)$, and distinct layers are orthogonal in $L^2(S^{n-1})$, proved by the divergence theorem applied to $h\nabla f - f\nabla h$ and Euler's relation. The dimension of the layer is

$$
\dim\mathcal{H}_k = \binom{n+k-1}{k} - \binom{n+k-3}{k-2} = \frac{(2k+n-2)(k+n-3)!}{k!(n-2)!},
$$

equal to $2k+1$ for $n=3$ and to $(k+1)^2$ for $n=4$, and the harmonic layers are exactly the trace-free symmetric tensors. The spherical harmonics are the images of the layers, and their orthogonality and completeness are the Fourier expansion on the sphere.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | Base field of characteristic $0$ |
| $V = \mathbb{R}^n$, $V^*$ | Euclidean space and its dual |
| $e_1, \ldots, e_n$; $e^1, \ldots, e^n$ | Basis of $V$ and its dual basis, $e^i(e_j) = \delta^i_j$ |
| $g$, $g_{ij} = \delta_{ij}$ | Standard positive definite inner product |
| $\operatorname{Sym}^k(V^*)$ | Symmetric tensors of rank $k$, dimension $\binom{n+k-1}{k}$ |
| $P_k$ | Homogeneous polynomials of degree $k$ |
| $\Delta = \sum_i\partial_i^2$ | Laplacian, $P_k \to P_{k-2}$ |
| $\mathcal{H}_k = \ker\Delta \cap P_k$ | Harmonic polynomials of degree $k$ |
| $r^2 = x_1^2 + \cdots + x_n^2$ | Squared norm |
| $S^{n-1}$, $d\sigma$ | Unit sphere and surface measure |
| $\Delta_S$ | Laplace–Beltrami operator; eigenvalue $-k(k+n-2)$ |
| $O(n)$ | Orthogonal group acting on each layer |
| $\binom{n+k-1}{k} - \binom{n+k-3}{k-2}$ | Dimension of $\mathcal{H}_k$ |
| Trace-free | Symmetric tensors in the kernel of metric contraction |
| $Z_k(x,y)$ | Zonal harmonic, reproducing kernel of $\mathcal{H}_k$ |
| $Y_{km}$ | Orthonormal basis of $\mathcal{H}_k$ on $S^2$ |
| $C_k^{(n/2-1)}(t)$ | Gegenbauer polynomial of the zonal harmonic |

## Further Reading

- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton University Press, 1971), for harmonic polynomials, spherical harmonics and the decomposition of $L^2(S^{n-1})$.
- Naum Ya. Vilenkin, *Special Functions and the Theory of Group Representations* (American Mathematical Society, 1968), for spherical harmonics and the orthogonal-group decomposition.
- Claus Müller, *Analysis of Spherical Symmetries in Euclidean Spaces* (Springer, 1998), for the addition theorem and the eigenvalue properties.
- Sheldon Axler, Paul Bourdon and Wade Ramey, *Harmonic Function Theory* (Springer, 2nd ed. 2001), for harmonic polynomials and the Kelvin transform.
- Sigurdur Helgason, *Groups and Geometric Analysis* (American Mathematical Society, 1984), for the representation-theoretic treatment of spherical harmonics.
