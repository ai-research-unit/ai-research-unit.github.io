
# __Hermitian Metrics and the Hodge Theory__

## Introduction

A complex manifold carries local coordinates $z^{j}$ and a decomposition of the complexified forms by the number of holomorphic and antiholomorphic differentials, and a **Hermitian metric** — a smoothly varying Hermitian inner product on each holomorphic tangent space — supplies the operator $\bar\partial$ with a formal adjoint and hence a **Dolbeault Laplacian** whose kernel represents the Dolbeault cohomology $H^{p,q}$. The Hermitian metric is a chosen form, and the whole of the complex Hodge theory is the geometry of that choice; when the metric satisfies the additional **Kähler condition** that its associated two-form is closed, the three Laplacians of $d$, $\partial$ and $\bar\partial$ become proportional, the de Rham cohomology acquires the **Hodge decomposition** into the pieces $H^{p,q}$, and the Lefschetz operator of the Kähler class makes the cohomology a representation of the Lie algebra $\mathfrak{sl}_2$ with the primitive decomposition and the Hodge–Riemann positivity.

The article develops the Hermitian metric and its associated form, the operators $\partial$ and $\bar\partial$, the Dolbeault complex and the Dolbeault theorem, the Kähler identities and the Hodge decomposition of the cohomology of a Kähler manifold, and the Lefschetz decomposition and Hodge–Riemann relations on the primitive cohomology. The de Rham side of the theory is *The Hodge Laplacian*; the polarisation and the Hodge–Riemann bilinear relations for an abstract Hodge structure are *Polarised Hodge Structures and the Hodge–Riemann Relations*; the Chern connection and the Chern classes are *Hermitian Vector Bundles and the Chern Connection* and *Chern Classes of a Hermitian Bundle*; and the Dolbeault index theorem is *The Hermitian Index Theorem and the Signature Operator*.

The prerequisites are *Smooth Manifolds and Differential Geometry* and *Differential Forms and Stokes' Theorem* for the manifolds, the forms and the exterior derivative; *Fibre Bundles, Connections and Curvature* and *Hermitian Metrics and the Levi-Civita Connection*, *Hermitian Manifolds and the Canonical Connection* for the Hermitian metrics and the connections; *Hermitian Structures and the Almost Complex Structure* for the almost complex structure and its integrability; *The Hodge Laplacian* for the de Rham Laplacian, the harmonic forms and the Hodge theorem; and *Transformation Groups and the Erlangen Program* and the Lie algebra articles for the $\mathfrak{sl}_2$-action of the Lefschetz decomposition. The Hodge conjecture and the algebraicity of the Hodge classes are named and deferred. No physics is invoked.

## Hermitian Metrics and the Operators

**Definition.** Let $X$ be a complex manifold of complex dimension $n$, with almost complex structure $J$ and holomorphic tangent bundle $T^{1,0}X$. A **Hermitian metric** on $X$ is a smooth family of positive definite Hermitian inner products $h_p$ on $T^{1,0}_pX$; it is equivalently a Riemannian metric $g$ with $g(Jv,Jw)=g(v,w)$ for all tangent vectors, through $g(v,w)=\operatorname{Re}h(v-iJv,w)$.

**Definition.** The **associated form** (or fundamental form) of a Hermitian metric is the real $(1,1)$-form

$$
\omega(v,w)=g(Jv,w),
$$

a positive form of bidegree $(1,1)$; the metric is **Kähler** when $\omega$ is closed, $d\omega=0$. The form $\omega$ is the datum that the Hermitian structure adds to the Riemannian one, and the Kähler condition is the integrability of that datum in the strongest sense.

**Definition.** On a complex manifold the complexified exterior algebra splits by bidegree,

$$
\Lambda^{k}T^{*}_{\mathbb{C}}X=\bigoplus_{p+q=k}\Lambda^{p,q}T^{*}X,
$$

and the exterior derivative splits accordingly as $d=\partial+\bar\partial$ with

$$
\partial:\Omega^{p,q}\to\Omega^{p+1,q},\qquad \bar\partial:\Omega^{p,q}\to\Omega^{p,q+1},\qquad \partial^{2}=\bar\partial^{2}=\partial\bar\partial+\bar\partial\partial=0 .
$$

A form of bidegree $(p,q)$ is **holomorphic** of type $p$ when $q=0$; the **Dolbeault complex** in a fixed $p$ is the complex $\Omega^{p,\bullet}(X)$ with the differential $\bar\partial$.

**Theorem.** A Hermitian metric determines formal adjoints $\partial^{*}$ and $\bar\partial^{*}$ of $\partial$ and $\bar\partial$ with respect to the $L^{2}$ inner product, and the **Dolbeault Laplacian**

$$
\Delta_{\bar\partial}=\bar\partial\bar\partial^{*}+\bar\partial^{*}\bar\partial
$$

is self-adjoint, nonnegative and elliptic; the same construction with $\partial$ gives $\Delta_\partial$, and the de Rham Laplacian is $\Delta_{d}=dd^{*}+d^{*}d$.

**Proof.** The adjoints are those of the operators of bidegree $(0,1)$ and $(1,0)$ with respect to the Hermitian metric on forms; the ellipticity and the self-adjointness are those of a Laplace operator of a first-order elliptic complex, as in *The Hodge Laplacian*, and the split of $d$ into $\partial+\bar\partial$ is the bidegree decomposition of the exterior derivative on a complex manifold. $\square$

## The Dolbeault Complex and Its Cohomology

**Definition.** The **Dolbeault cohomology** of $X$ is the cohomology of the Dolbeault complex,

$$
H^{p,q}_{\bar\partial}(X)=\frac{\ker\bigl(\bar\partial:\Omega^{p,q}\to\Omega^{p,q+1}\bigr)}{\operatorname{im}\bigl(\bar\partial:\Omega^{p,q-1}\to\Omega^{p,q}\bigr)} .
$$

**Theorem (Dolbeault).** For a complex manifold $X$ the Dolbeault cohomology of the sheaf $\Omega^{p}$ of holomorphic $p$-forms is the sheaf cohomology,

$$
H^{p,q}_{\bar\partial}(X)\cong H^{q}(X,\Omega^{p}),
$$

and the two may be identified; the identification is the complex analogue of the de Rham theorem, with $\bar\partial$ in place of $d$ and the holomorphic structure in place of the smooth one.

**Proof sketch.** The Dolbeault complex is a resolution of the sheaf $\Omega^{p}$ — locally, a $\bar\partial$-closed $(p,q)$-form is $\bar\partial$-exact for $q>0$ by the Dolbeault–Grothendieck lemma, the complex analogue of the Poincaré lemma — and the hypercohomology of the resolution computes the sheaf cohomology. The argument is that of *Sheaves and the de Rham Complex* carried over to the $\bar\partial$-operator, and the Dolbeault–Grothendieck lemma is the local statement. $\square$

**Theorem (Hodge representation for $\bar\partial$).** On a compact complex manifold with a Hermitian metric the kernel of the Dolbeault Laplacian,

$$
\mathcal{H}^{p,q}(X)=\ker\Delta_{\bar\partial}\cap\Omega^{p,q}(X),
$$

consists of the **harmonic $(p,q)$-forms**, and the **Hodge isomorphism** $\mathcal{H}^{p,q}(X)\cong H^{p,q}_{\bar\partial}(X)$ holds; in particular the Dolbeault cohomology is finite-dimensional and $h^{p,q}=\dim H^{p,q}_{\bar\partial}(X)<\infty$. The Hodge decomposition of the Dolbeault complex is

$$
\Omega^{p,q}(X)=\mathcal{H}^{p,q}\oplus\bar\partial\Omega^{p,q-1}\oplus\bar\partial^{*}\Omega^{p,q+1},
$$

the orthogonal direct sum of the harmonic, the $\bar\partial$-exact and the $\bar\partial^{*}$-exact parts.

**Proof.** The argument is the Hodge theorem of *The Hodge Laplacian* applied to the elliptic self-adjoint operator $\Delta_{\bar\partial}$; the decomposition is the spectral decomposition of the self-adjoint operator, and the harmonic forms are closed and coclosed for $\bar\partial$, hence represent the cohomology. $\square$

**Remark.** The Hermitian metric is used here in an essential way: the adjoint $\bar\partial^{*}$, the Laplacian $\Delta_{\bar\partial}$ and the harmonic representatives all depend on it, while the Dolbeault cohomology $H^{p,q}_{\bar\partial}$ and its dimension do not. The decomposition of each Dolbeault group by the metric is the complex analogue of the Hodge theorem, and it holds for every Hermitian metric and not only for the Kähler ones.

## The Kähler Condition and the Kähler Identities

**Definition.** A Hermitian metric is **Kähler** when its associated form is closed, $d\omega=0$; equivalently when the parallel transport of the Levi-Civita connection preserves the complex structure, so that the holonomy is contained in the unitary group, equivalently when $\nabla J=0$ for the Levi-Civita connection. A **Kähler manifold** is a complex manifold with a Kähler metric; the class $[\omega]\in H^{2}(X;\mathbb{R})$ is the **Kähler class**, and a manifold is Kähler when it admits a Kähler metric.

**Theorem (Kähler identities).** On a Kähler manifold the operators of bidegree $\pm1$ satisfy

$$
[\Lambda,\partial]=i\,\bar\partial^{*},\qquad
[\Lambda,\bar\partial]=-i\,\partial^{*},\qquad
[\Lambda,L]=\text{the degree operator},
$$

where $L\omega=\omega\wedge\cdot$ is the Lefschetz operator of the associated form, $\Lambda=L^{*}$ is its adjoint and the last identity holds on every complex manifold. Consequently the three Laplacians are proportional,

$$
\Delta_{d}=2\Delta_{\partial}=2\Delta_{\bar\partial},
$$

and each is **bigraded**, $\Delta_{d}(\Omega^{p,q})\subseteq\Omega^{p,q}$.

**Proof sketch.** The first identity is the computation of the Kähler form with the Hodge star and the operator $\Lambda$; the proportionality of the Laplacians follows from it and from $d=\partial+\bar\partial$, $d^{2}=0$; the identity $[\Lambda,L]=$ degree is the standard $\mathfrak{sl}_2$-relation, proved from the exterior algebra and the positivity of $\omega$. The identities are those of the Kähler geometry of *Hermitian Manifolds and the Canonical Connection*. $\square$

**Corollary.** On a compact Kähler manifold the de Rham Laplacian preserves the bidegree, so a harmonic form decomposes into harmonic pieces of pure bidegree, and the kernel of $\Delta_d$ in the total degree $k$ is the direct sum of the kernels of $\Delta_{\bar\partial}$ in the bidegrees $(p,q)$ with $p+q=k$.

## The Hodge Decomposition of a Kähler Manifold

**Theorem (Hodge decomposition).** Let $X$ be a compact Kähler manifold. Then

$$
H^{k}(X;\mathbb{C})=\bigoplus_{p+q=k}H^{p,q}(X),\qquad
H^{p,q}(X)=\ker\Delta_{\bar\partial}\cap\Omega^{p,q}(X),
$$

the **Hodge decomposition** of the de Rham cohomology, with $\overline{H^{p,q}}=H^{q,p}$; the complex conjugation is the conjugation of the coefficients. The pieces depend on the Kähler metric through their representatives but not through their dimensions, and the **Hodge numbers** satisfy

$$
h^{p,q}=h^{q,p}=h^{n-p,n-q},\qquad
b_{k}=\sum_{p+q=k}h^{p,q},
$$

where the third symmetry is **Serre duality**, $h^{n-p,n-q}=h^{p,q}$, or equivalently the nondegenerate pairing $H^{p,q}(X)\times H^{n-p,n-q}(X)\to\mathbb{C}$ given by the wedge product and the trace.

**Proof.** The bidegree is preserved by the Kähler Laplacian by the Kähler identities, so a harmonic representative of a class of degree $k$ splits into harmonic pieces of bidegree $(p,k-p)$, and the conjugation of the coefficients exchanges $(p,q)$ with $(q,p)$; Serre duality is the nondegeneracy of the pairing $H^{p,q}\times H^{n-p,n-q}\to\mathbb{C}$ given by the wedge product and the trace, which is the complex form of Poincaré duality. $\square$

**Remark.** The Hodge decomposition is what distinguishes a Kähler manifold from an arbitrary complex manifold: the Dolbeault cohomology $H^{p,q}$ exists for every complex manifold, but the sum $\bigoplus_{p+q=k}H^{p,q}$ equals the de Rham group $H^{k}$ only when the metric can be chosen Kähler, or equivalently when the manifold satisfies the $\partial\bar\partial$-lemma. The complex structure and the metric are compatible in the strongest sense in the Kähler case, and the compatibility is exactly what the bigrading of the Laplacian detects.

## The Lefschetz Decomposition and the Hodge–Riemann Relations

**Theorem ($\mathfrak{sl}_2$-action).** On a compact Kähler manifold of complex dimension $n$ the operators $L=\omega\wedge\cdot$, $\Lambda=L^{*}$ and $H=[L,\Lambda]$ acting on the cohomology satisfy the relations

$$
[H,L]=2L,\qquad [H,\Lambda]=-2\Lambda,\qquad [L,\Lambda]=H ,
$$

the commutation relations of $\mathfrak{sl}_2(\mathbb{C})$; the operator $H$ acts on $H^{k}(X)$ by $k-n$, and the **hard Lefschetz theorem** states that

$$
L^{\,n-k}:H^{k}(X;\mathbb{R})\xrightarrow{\ \cong\ }H^{2n-k}(X;\mathbb{R})
$$

is an isomorphism for every $k\leq n$.

**Proof sketch.** The commutation relations are those of the exterior algebra of the Kähler form; the hard Lefschetz theorem follows from the representation theory of $\mathfrak{sl}_2$ together with the positivity of the operator $[\Lambda,L]$ on the primitive part, and the argument is the one used for the nilpotent orbit of a semisimple Lie algebra. The Lefschetz package is developed with the Kähler identities of *Hermitian Manifolds and the Canonical Connection*. $\square$

**Definition.** A class in $H^{k}(X)$ is **primitive** when $\Lambda\alpha=0$; the primitive part $P^{k}(X)$ is the kernel of $\Lambda$ on $H^{k}(X)$, and the **Lefschetz decomposition** writes

$$
H^{k}(X)=\bigoplus_{r\geq0}L^{\,r}P^{k-2r}(X),
$$

the irreducible $\mathfrak{sl}_2$-pieces.

**Theorem (Hodge–Riemann relations).** On the primitive cohomology of a compact Kähler manifold the pairing

$$
Q(\alpha,\beta)=\int_{X}L^{\,n-k}\alpha\wedge\beta\qquad\bigl(\alpha,\beta\in P^{k}(X)\bigr)
$$

is a polarisation: it is $(-1)^{k}$-symmetric and satisfies the Hodge–Riemann relations

$$
i^{\,p-q}\,Q(\alpha,\bar\alpha)>0\qquad\text{for }\alpha\in P^{p,q}(X)\setminus\{0\} ,
$$

so that $Q(C\alpha,\bar\alpha)>0$ for the Weil operator $C=i^{p-q}$; the form is a polarisation of the Hodge structure of the primitive cohomology in the sense of *Polarised Hodge Structures and the Hodge–Riemann Relations*.

**Proof sketch.** The symmetry is the graded commutativity of the wedge product; the positivity is the Hodge–Riemann bilinear relation, proved by the Lefschetz decomposition and the $\mathfrak{sl}_2$-structure together with the positivity of the metric on the primitive forms. The relation is the precise positivity behind the Hodge index theorem and the signature of the middle intersection form of *The Signature Operator*. $\square$

## Examples

**Example (the projective space).** For $\mathbb{CP}^{n}$ with the Fubini–Study metric the cohomology is one-dimensional in each even degree, $h^{p,p}=1$ and $h^{p,q}=0$ for $p\neq q$; the Kähler class is the generator of $H^{2}$, the Lefschetz operator is multiplication by its powers, and the cohomology is a single irreducible $\mathfrak{sl}_2$-module, the primitive part being one-dimensional in the middle degree only.

**Example (a compact Riemann surface).** A Riemann surface is Kähler for every metric in its conformal class, of complex dimension one; the Hodge decomposition is $H^{1}=H^{1,0}\oplus H^{0,1}$ with $h^{1,0}=h^{0,1}=g$, so $b_{1}=2g$, and the Kähler class gives the hard Lefschetz isomorphism $L^{0}=\mathrm{id}$ on $H^{0}$ and $H^{2}$.

**Example (a $K3$ surface).** For a $K3$ surface $h^{0,0}=h^{2,2}=1$, $h^{2,0}=h^{0,2}=1$, $h^{1,1}=20$ and $b_{2}=22$; the primitive middle cohomology has dimension $21$, the Kähler class is one of the $(1,1)$-classes, and the Hodge–Riemann relations give the signature $\sigma=2-20+2=-16$ and the negative definite part of the intersection form on the primitive $(1,1)$-classes. The Kähler structure and the Hodge numbers of the $K3$ surface are the standard checks of the theory.

**Example (the Hopf surface).** The Hopf surface, a compact complex surface homeomorphic to $S^{1}\times S^{3}$ with $b_{1}=1$, is **not** Kähler: a Kähler manifold has even $b_{1}$, since $b_{1}=h^{1,0}+h^{0,1}=2h^{1,0}$, whereas the Hopf surface has $b_{1}=1$. The Dolbeault cohomology $H^{p,q}$ still exists, but the sum $\bigoplus_{p+q=k}H^{p,q}$ does not compute the de Rham group $H^{k}$, and the Hodge decomposition fails. The example shows that the Dolbeault decomposition is available on every complex manifold and the Hodge decomposition only on the Kähler ones.

## Summary

A **Hermitian metric** on a complex manifold is a smoothly varying Hermitian inner product on the holomorphic tangent spaces, equivalently a Riemannian metric compatible with the almost complex structure, and it has an **associated form** $\omega$ of bidegree $(1,1)$; it determines the formal adjoints of $\partial$ and $\bar\partial$ and the Laplacians $\Delta_\partial$, $\Delta_{\bar\partial}$ and $\Delta_d$. The **Dolbeault complex** of $\bar\partial$ has the **Dolbeault cohomology** $H^{p,q}_{\bar\partial}(X)\cong H^{q}(X,\Omega^{p})$, and on a compact manifold the **Hodge representation** identifies it with the kernel of $\Delta_{\bar\partial}$. When $\omega$ is closed the metric is **Kähler**, the **Kähler identities** give $\Delta_d=2\Delta_\partial=2\Delta_{\bar\partial}$ and the bigrading of the Laplacian, and the de Rham cohomology acquires the **Hodge decomposition** $H^{k}=\bigoplus_{p+q=k}H^{p,q}$ with the symmetries $h^{p,q}=h^{q,p}=h^{n-p,n-q}$ and $b_{k}=\sum h^{p,q}$. The Kähler class makes the cohomology a representation of $\mathfrak{sl}_2$ through $L$, $\Lambda$ and $H$, the **hard Lefschetz theorem** making $L^{n-k}:H^{k}\cong H^{2n-k}$ an isomorphism, and the **Hodge–Riemann relations** make the form $Q(\alpha,\beta)=\int L^{n-k}\alpha\wedge\beta$ a polarisation of the primitive cohomology. The Hermitian metric is a chosen form, and the Hodge theory is the geometry of that choice; the Hopf surface shows how much is lost outside the Kähler class.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$, $n$, $J$, $T^{1,0}X$ | Complex manifold, complex dimension, almost complex structure, holomorphic tangent bundle |
| $h$, $g$, $\omega(v,w)=g(Jv,w)$ | Hermitian metric, Riemannian metric, associated $(1,1)$-form |
| $d=\partial+\bar\partial$ | Splitting of the exterior derivative by bidegree |
| $\Omega^{p,q}$, $L$, $\Lambda$ | Forms of bidegree $(p,q)$; Lefschetz operator $\omega\wedge\cdot$ and its adjoint |
| $H^{p,q}_{\bar\partial}\cong H^{q}(X,\Omega^{p})$ | Dolbeault cohomology |
| $\Delta_{\bar\partial}=\bar\partial\bar\partial^{*}+\bar\partial^{*}\bar\partial$ | Dolbeault Laplacian |
| Kähler, $d\omega=0$ | The Kähler condition |
| $\Delta_d=2\Delta_\partial=2\Delta_{\bar\partial}$ | Kähler identities |
| $H^{k}=\bigoplus_{p+q=k}H^{p,q}$ | Hodge decomposition; $h^{p,q}=h^{q,p}=h^{n-p,n-q}$ |
| $L^{n-k}:H^{k}\cong H^{2n-k}$ | Hard Lefschetz; primitive part $P^{k}=\ker\Lambda$ |
| $Q(\alpha,\beta)=\int L^{n-k}\alpha\wedge\beta$ | Polarisation of the primitive cohomology; Hodge–Riemann relations |

## Further Reading

- Phillip A. Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for Hermitian and Kähler metrics, the Hodge decomposition and the Hodge–Riemann relations.
- Kunihiko Kodaira, *Complex Manifolds and Deformation of Complex Structures* (Springer, 1986), for the Dolbeault theorem and the Hodge theory of complex manifolds.
- Shiing-Shen Chern, *Complex Manifolds without Potential Theory* (Springer, 2nd ed. 1979), for the Hermitian metric, the associated form and the Kähler condition.
- W. V. D. Hodge, *The Theory and Applications of Harmonic Integrals* (Cambridge University Press, 1941), for the Hodge decomposition and the harmonic integrals.
- Raymond O. Wells, *Differential Analysis on Complex Manifolds*, Graduate Texts in Mathematics 65 (Springer, 3rd ed. 2008), for the Dolbeault complex, the Hodge theory and the Kähler identities.
- Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I, II* (Cambridge University Press, 2002–2003), for the Hodge decomposition, the Lefschetz decomposition and the Hodge–Riemann relations.
