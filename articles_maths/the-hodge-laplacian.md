
# __The Hodge Laplacian__

## Introduction

A Riemannian metric turns the exterior algebra of a manifold into an inner product space, and the inner product singles out a Laplace operator: the **Hodge Laplacian** $\Delta=dd^{*}+d^{*}d$, the sum of the exterior derivative and its formal adjoint. Its kernel is the space of **harmonic forms**, and the theorem of Hodge identifies the harmonic $k$-forms with the de Rham cohomology in degree $k$; the identification decomposes every form into a harmonic part and two exact pieces, and it exhibits the cohomology as the kernel of an elliptic operator that the metric constructs. The Laplacian is the geometric form of the cohomology: it depends on the chosen metric, while the dimension of its kernel is the Betti number, which the metric does not change.

This article defines the codifferential, the Laplacian and the harmonic forms, states the **Hodge decomposition** and the **Hodge theorem**, records the compatibility of the Laplacian with the Hodge star and the resulting form of Poincaré duality, and develops the **Weitzenböck formula**, which expresses the Laplacian through the covariant derivative and the curvature and gives the Bochner vanishing theorems. The metric is used throughout; a change of metric changes the operator, its harmonic forms and the splitting, and the invariance of the dimension of the kernel is the theorem that separates the topology from the metric.

The prerequisites are *Differential Forms and Stokes' Theorem* for the exterior algebra, the exterior derivative and Stokes' theorem; *Riemannian Geometry* and *Curvature and Geodesics* for the metric, its connection, its curvature and the Laplace–Beltrami operator on functions; *The Volume Element, Duality and the Hodge Star* for the star and its square; and *The Codifferential*, a Part III article of the same shape as this one but with the analytic emphasis, for the construction of the codifferential as the formal adjoint of $d$. The Laplacian is the square of the **signature operator** of *The Signature Operator*, and it is the operator whose index the Atiyah–Singer theorem computes in *The Atiyah–Singer Index Theorem and K-Theory*. The Hodge theory of an arbitrary elliptic complex and the heat-kernel proof of the index theorem belong to Part III and are cited; the Hermitian refinement of the theory belongs to *Hermitian Metrics and the Hodge Theory*, written beside this article. No physics is invoked.

## The Codifferential

Let $(M,g)$ be a closed oriented Riemannian manifold of dimension $n$, with volume form $\mathrm{vol}_g$, with $\Omega^{k}(M)$ the smooth complexified $k$-forms, and with the $L^{2}$ inner product

$$
(\alpha,\beta)=\int_M\alpha\wedge\star\bar\beta ,
$$

for the Hodge star $\star$ of *The Volume Element, Duality and the Hodge Star*. The exterior derivative $d:\Omega^{k}\to\Omega^{k+1}$ has a formal adjoint, the **codifferential**

$$
d^{*}:\Omega^{k+1}(M)\longrightarrow\Omega^{k}(M),\qquad
(d\alpha,\beta)=(\alpha,d^{*}\beta),
$$

given on forms by $d^{*}=(-1)^{k}\star^{-1}d\star$ up to a sign that depends on the degree and the dimension, or equivalently $d^{*}=-\tau d\tau^{-1}$ for the chirality $\tau$ of *The Signature Operator*. The codifferential is also defined by the local formula

$$
d^{*}\Bigl(\sum_{I}\omega_I\,dx^{I}\Bigr)=-\sum_{i,I}\nabla_{i}\omega_{iI}\,dx^{I},
$$

the negative of the divergence of the form read as an alternating tensor; its construction as the formal adjoint of $d$, the sign conventions and the equivalent local formula are the subject of *The Codifferential*. Here the two properties that matter are recorded.

**Theorem.** The codifferential is $\mathbb{C}$-linear, it lowers the degree by one, and it is **nilpotent**, $(d^{*})^2=0$; it is the formal adjoint of $d$, so $(d\alpha,\beta)=(\alpha,d^{*}\beta)$ for compactly supported forms, and the pair $(d,d^{*})$ forms a two-term complex in each direction that vanishes on composition.

**Proof.** The nilpotency is the adjoint of $d^2=0$; the adjointness is the definition, and the sign in $d^{*}=(-1)^{k}\star^{-1}d\star$ is that of the identity $\star\,d\,\star^{-1}=\pm d^{*}$ of the Hodge star. $\square$

## The Laplacian and the Harmonic Forms

**Definition.** The **Hodge Laplacian** (or Laplace–de Rham operator) is the operator on forms

$$
\Delta=dd^{*}+d^{*}d:\Omega^{\bullet}(M)\longrightarrow\Omega^{\bullet}(M) .
$$

It preserves the degree, $\Delta:\Omega^{k}\to\Omega^{k}$. A form $\omega$ is **harmonic** if $\Delta\omega=0$, and the space of harmonic $k$-forms is written $\mathcal{H}^{k}(M)=\ker(\Delta|_{\Omega^{k}})$.

**Theorem.** The Laplacian is formally self-adjoint, $\Delta^{*}=\Delta$, and nonnegative, $(\Delta\omega,\omega)=\|d\omega\|^{2}+\|d^{*}\omega\|^{2}\geq0$; a form is harmonic if and only if it is closed and coclosed,

$$
\Delta\omega=0\iff d\omega=0\ \text{and}\ d^{*}\omega=0 .
$$

**Proof.** The self-adjointness is the adjointness of $d$ and $d^{*}$ together with the self-adjointness of each term $dd^{*}$ and $d^{*}d$; the quadratic form is the expanded product, and it is a sum of two norms, vanishing exactly when both vanish. $\square$

**Theorem (ellipticity and discreteness).** The Laplacian is elliptic, of order two, with principal symbol $\sigma_\Delta(\xi)=|\xi|^2\mathrm{id}$; on a closed manifold its spectrum is discrete, real and nonnegative, it accumulates only at infinity, and the heat semigroup $e^{-t\Delta}$ is a smoothing operator for $t>0$. Consequently $\mathcal{H}^{k}(M)$ is finite-dimensional and $\Omega^{k}(M)=\mathcal{H}^{k}\oplus\Delta\Omega^{k}$.

**Proof.** The symbol is the squared length of the covector, hence invertible for $\xi\neq0$; the spectral theory of a self-adjoint elliptic operator on a closed manifold gives the rest, and the smoothness of the heat kernel is the standard parabolic regularity. $\square$

## The Hodge Decomposition and the Hodge Theorem

**Theorem (Hodge decomposition).** On a closed oriented Riemannian manifold the space of $k$-forms splits as an orthogonal direct sum

$$
\Omega^{k}(M)=\mathcal{H}^{k}(M)\oplus d\,\Omega^{k-1}(M)\oplus d^{*}\,\Omega^{k+1}(M),
$$

the **harmonic**, **exact** and **coexact** parts, and the decomposition is unique. Equivalently the closed forms split as $\ker(d|_{\Omega^{k}})=\mathcal{H}^{k}\oplus d\Omega^{k-1}$.

**Proof.** The three summands are mutually orthogonal: $(\Delta\omega,\eta)=0$ for a harmonic $\omega$ and $\eta$ exact or coexact because the Laplacian is self-adjoint and exact/coexact forms are orthogonal to the kernel of a self-adjoint operator; and $\Omega^{k}=\ker\Delta\oplus\mathrm{im}\,\Delta$ by the spectral theorem for the self-adjoint elliptic operator. Since $\mathrm{im}\,\Delta=\mathrm{im}\,dd^{*}+\mathrm{im}\,d^{*}d=d\Omega^{k-1}+d^{*}\Omega^{k+1}$, the decomposition follows; uniqueness is the orthogonality. $\square$

**Theorem (Hodge).** The map that assigns to a harmonic form its de Rham class is an isomorphism

$$
\mathcal{H}^{k}(M)\;\xrightarrow{\ \cong\ }\;H^{k}_{dR}(M;\mathbb{C}),\qquad
\dim\mathcal{H}^{k}(M)=b_{k}(M),
$$

so every de Rham class has a unique harmonic representative, and the Betti numbers are the dimensions of the kernels of the Laplacian.

**Proof.** A harmonic form is closed, so the map is defined; it is injective, since an exact harmonic form is orthogonal to the harmonic forms and hence zero; it is surjective, since a closed form differs from its harmonic part by an exact form, by the decomposition of $\ker d$. The dimension statement is the finite-dimensionality of the kernel. $\square$

**Remark.** The decomposition and the isomorphism depend on the metric through the Laplacian, but the dimension $b_{k}$ does not: the same cohomology is presented by the kernels of different operators. This is the content of the Hodge theorem read geometrically — the metric supplies a canonical representative of every class, and the choice of representative changes with the metric while the class and the dimension do not.

## The Star, Duality and the Middle Form

**Theorem.** The Hodge star commutes with the Laplacian up to the degree sign, $\Delta\star=\star\Delta$; it therefore maps harmonic forms to harmonic forms and gives an isomorphism

$$
\star:\mathcal{H}^{k}(M)\xrightarrow{\ \cong\ }\mathcal{H}^{n-k}(M),
$$

which is, under the Hodge isomorphism, the Poincaré duality pairing $H^{k}\times H^{n-k}\to\mathbb{C}$, $\langle u\cup v,[M]\rangle$, up to the metric normalization. In particular $b_{k}=b_{n-k}$, and for a closed oriented manifold the pairing is nondegenerate.

**Proof.** The star intertwines $d$ and $d^{*}$ up to sign, so it conjugates $\Delta=dd^{*}+d^{*}d$ to itself; the induced map on cohomology is the composition of the Hodge isomorphism with the Poincaré pairing, and the nondegeneracy of the latter is Poincaré duality. $\square$

**Corollary (the middle form and the signature).** For a closed oriented manifold of dimension $4k$ the star acts on the middle harmonic forms as the chirality, and the pairing

$$
\beta(u,v)=\int_Mu\wedge v\qquad(u,v\in\mathcal{H}^{2k}(M))
$$

is a nondegenerate symmetric bilinear form whose positive and negative parts are the self-dual and anti-self-dual harmonic forms; its signature is $b_{+}-b_{-}=\sigma(M)$, the index of the positive half of the signature operator. The relation of the Laplacian to the intersection form is thus the reason the signature is the index of an operator built from the metric.

## The Weitzenböck Formula

The Laplacian can be written through the Levi-Civita connection $\nabla$ and the curvature, and the resulting identity is the source of the vanishing theorems.

**Theorem (Weitzenböck formula).** For a $k$-form $\omega$ on a Riemannian manifold,

$$
\Delta\omega=\nabla^{*}\nabla\omega+\mathcal{R}_k\,\omega ,
$$

where $\nabla^{*}\nabla=-\operatorname{tr}_g\nabla^2$ is the **rough Laplacian** and $\mathcal{R}_k$ is the endomorphism of $\Lambda^{k}T^{*}M$ built from the curvature tensor by contraction,

$$
\langle\mathcal{R}_k\omega,\omega\rangle
=\sum_{i<j}\bigl\langle \omega,\ R(e_i,e_j)\cdot\omega\bigr\rangle
$$

in a $g$-orthonormal frame $(e_i)$, the natural action of the curvature on forms; for $k=1$ the endomorphism is the Ricci tensor, $\mathcal{R}_1=\operatorname{Ric}$, and for $k=0$ it vanishes, so on functions $\Delta f=-\operatorname{tr}_g\nabla^2f=\nabla^{*}\nabla f$.

**Proof sketch.** The identity is the Weitzenböck decomposition of the second-order operator $\Delta$: the two operators have the same principal symbol, and their difference is the zeroth-order curvature term computed from the commutator $[\nabla_i,\nabla_j]$ on forms, which is the curvature; the case $k=1$ traces the curvature to the Ricci tensor. The argument is the standard one of the Bochner technique. $\square$

**Theorem (Bochner vanishing).** Let $(M,g)$ be closed and oriented, and let $\operatorname{Ric}\geq0$ on $M$. Then every harmonic $1$-form is parallel, $\nabla\omega=0$; if $\operatorname{Ric}>0$ at some point, there is no nonzero harmonic $1$-form and $b_{1}(M)=0$. More generally, if the curvature endomorphism $\mathcal{R}_k$ is nonnegative on $\Lambda^{k}T^{*}M$, every harmonic $k$-form is parallel and $b_{k}\leq\binom{n}{k}$ with equality forcing $\mathcal{R}_k=0$.

**Proof.** For a harmonic $\omega$ the Weitzenböck formula gives $0=(\Delta\omega,\omega)=\|\nabla\omega\|^2+(\mathcal{R}_k\omega,\omega)$; under the curvature assumption both terms are nonnegative, so both vanish; a parallel form is determined by its value at one point, which gives the rank bound, and the strict positivity forces $\omega=0$. $\square$

**Corollary.** A closed Riemannian manifold of positive Ricci curvature has $b_1=0$; the round sphere $S^n$ of dimension $n\geq2$ has $b_1=0$, and the flat torus has $\operatorname{Ric}=0$ and harmonic $1$-forms $dx^i$ that are parallel.

## Examples

**Example (the flat torus).** On $T^{n}=\mathbb{R}^{n}/\mathbb{Z}^{n}$ with the flat metric the harmonic forms are the constant-coefficient forms, $\mathcal{H}^{k}$ has basis $dx^{I}$ for $|I|=k$, and $b_k=\binom{n}{k}$; the Weitzenböck term vanishes, every harmonic form is parallel, and the Laplacian is the ordinary Euclidean one acting coefficient by coefficient.

**Example (the spheres).** On $S^{n}$ with the round metric the Laplacian on functions has eigenvalues $k(k+n-1)$ with the spherical harmonics as eigenfunctions, and the harmonic forms are the constant functions in degree $0$ and the volume form in degree $n$, so $b_0=b_n=1$ and the remaining Betti numbers vanish; the positive curvature gives the vanishing of the intermediate harmonic forms, in agreement with the Bochner theorem and with the computation of the cohomology. The spectrum of the Laplacian is the geometric invariant that carries more information than the Betti numbers: it detects the radius, which the cohomology does not.

**Example (hyperbolic space forms).** On a closed hyperbolic manifold the Ricci curvature is negative and the Bochner argument gives no vanishing; the Hodge theorem still presents the cohomology by harmonic forms, and the Hodge numbers of a hyperbolic manifold are not determined by the curvature sign. The example shows that the Bochner vanishing is a one-way criterion: it excludes harmonic forms under positive curvature and says nothing under negative curvature.

**Example (the signature operator).** On a closed manifold the Hodge Laplacian is the square of the signature operator, $\Delta=(d+d^{*})^2$, and the harmonic forms are the kernel of $d+d^{*}$; the index of the positive half is the signature, by *The Signature Operator*, and the Euler characteristic is the index of the version graded by the total degree. The two indices are the two characteristic numbers that the de Rham complex computes, and both are computed by the Laplacian and its heat kernel.

## Summary

The **codifferential** $d^{*}$ is the formal adjoint of the exterior derivative with respect to the metric inner product $(\alpha,\beta)=\int_M\alpha\wedge\star\bar\beta$, and the **Hodge Laplacian** $\Delta=dd^{*}+d^{*}d$ is self-adjoint, nonnegative and elliptic; a form is harmonic exactly when it is closed and coclosed. On a closed oriented manifold the **Hodge decomposition** writes the $k$-forms as the orthogonal sum of the harmonic, exact and coexact parts, and the **Hodge theorem** identifies the harmonic forms with the de Rham cohomology, so that $\dim\mathcal{H}^{k}=b_{k}$; the metric supplies a canonical representative of every class, and the dimension is the topological invariant. The star commutes with the Laplacian and gives the Poincaré duality isomorphism $\mathcal{H}^{k}\cong\mathcal{H}^{n-k}$ and, in the middle degree of a $4k$-manifold, the intersection form whose signature is the index of the signature operator. The **Weitzenböck formula** $\Delta=\nabla^{*}\nabla+\mathcal{R}_k$ expresses the Laplacian through the connection and the curvature, and under a nonnegative curvature endomorphism the harmonic forms are parallel, which gives the **Bochner vanishing theorem**, $b_1=0$ for positive Ricci curvature. The flat torus, the round sphere and the closed hyperbolic manifolds illustrate the three regimes.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(M,g)$, $n$, $\mathrm{vol}_g$ | Closed oriented Riemannian manifold, dimension, volume form |
| $\star$ | Hodge star; $(\alpha,\beta)=\int_M\alpha\wedge\star\bar\beta$ |
| $d,d^{*}$ | Exterior derivative and codifferential (formal adjoints) |
| $\Delta=dd^{*}+d^{*}d$ | Hodge Laplacian, preserving the degree |
| $\mathcal{H}^{k}(M)=\ker\Delta|_{\Omega^{k}}$ | Harmonic $k$-forms |
| $\Omega^{k}=\mathcal{H}^{k}\oplus d\Omega^{k-1}\oplus d^{*}\Omega^{k+1}$ | Hodge decomposition |
| $\mathcal{H}^{k}\cong H^{k}_{dR}(M)$, $\dim=b_k$ | Hodge theorem |
| $\star:\mathcal{H}^{k}\cong\mathcal{H}^{n-k}$ | Poincaré duality from the star |
| $\beta(u,v)=\int_Mu\wedge v$ | Intersection form on $\mathcal{H}^{n/2}$; $\sigma=b_+-b_-$ |
| $\nabla^{*}\nabla$, $\mathcal{R}_k$ | Rough Laplacian and the curvature endomorphism |
| $\Delta=\nabla^{*}\nabla+\mathcal{R}_k$ | Weitzenböck formula; $\mathcal{R}_1=\operatorname{Ric}$ |
| Bochner vanishing | $\operatorname{Ric}\geq0$ ⇒ harmonic $1$-forms parallel; $\operatorname{Ric}>0$ ⇒ $b_1=0$ |

## Further Reading

- W. V. D. Hodge, *The Theory and Applications of Harmonic Integrals* (Cambridge University Press, 1941), for the original Hodge theory and the harmonic integrals.
- Georges de Rham, *Differentiable Manifolds: Forms, Currents, Harmonic Forms* (Springer, 1984), for the de Rham theorem and the harmonic representatives.
- Frank W. Warner, *Foundations of Differentiable Manifolds and Lie Groups*, Graduate Texts in Mathematics 94 (Springer, 1983), for the Hodge theorem, the Hodge decomposition and the Weitzenböck formula.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Hodge Laplacian, the Bochner technique and the Lichnerowicz formula.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Vol. I (Wiley, 1963), for the Laplacian on forms, the Weitzenböck identity and the Bochner vanishing theorems.
- Phillip A. Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Hodge decomposition on complex manifolds and the Hodge–Riemann relations, developed further in *Hermitian Metrics and the Hodge Theory*.
