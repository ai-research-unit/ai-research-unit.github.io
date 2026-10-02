
# __The Dirac Operator on a Manifold__

## Introduction

A spin manifold carries a bundle of spinors on which the Clifford algebra of each tangent space acts, and the Riemannian metric then determines a first-order differential operator, the **Cauchy–Riemann operator of the spinor bundle**, $D=\sum_ie_i\cdot\nabla^{\mathcal{S}}_{e_i}$, assembled from the spin connection and the Clifford multiplication. Its square is computed by the **Lichnerowicz formula**, $D^{2}=\nabla^{*}\nabla+\tfrac14\operatorname{scal}$, the connection Laplacian plus a quarter of the scalar curvature; the formula makes the operator a curvature instrument, and it closes the circle between the metric, the topology and the index. The operator is formally self-adjoint and elliptic, it exchanges the two half-spinor bundles in even dimensions, and the index of its positive half is the **$\hat A$-genus** $\int_M\hat A(TM)$ of the Atiyah–Singer theorem.

The article treats the operator as an object of the geometry: it records the spin structure and the spinor bundle, defines the operator and its chiral parts, states the Lichnerowicz formula and the vanishing theorem it gives for positive scalar curvature, and states the index theorem in the spin case and its twisted form. The spin structures, the spin representations and the Lichnerowicz formula itself belong to the form theory of *Spin Geometry* and to the Clifford-module article *Clifford Modules and the Twisted Cauchy–Riemann Operator*, and are cited here rather than rederived; what this article develops is the operator as a differential operator on a manifold, its self-adjointness and ellipticity, its chiral splitting, and the index and vanishing theorems that follow. The classical name of the operator is the **Dirac operator**, which gives this article its menu title; the corpus name is the Cauchy–Riemann operator, and the two are the same operator.

The prerequisites are *Spin Geometry* and *Spin Representations and Clifford Modules with Inner Conjugation* for the spin structures, the spinor bundle and the spin representations; *Clifford Modules and the Twisted Cauchy–Riemann Operator* for the twisted operator, its symbol and its index; *Fibre Bundles, Connections and Curvature* for the bundles, the connections and the curvature; *Riemannian Geometry* and *Curvature and Geodesics* for the metric, its connection and its scalar curvature; *The Hodge Laplacian* for the Laplacian and the Weitzenböck formula of which the Lichnerowicz formula is the spin form; and *The Atiyah–Singer Index Theorem and K-Theory* for the general index theorem and the $\hat A$-genus. The formal adjoint of the operator and its relation to the inner conjugation are treated in *The Dirac Operator and Its Adjoint*, *Dirac Operators with Hermitian Adjoint* and *Spinor Adjoints and the Dirac Adjoint with Inner Conjugation*, written in this category or cited. Part III owns the analytic completion — the domains, the closed extensions and the heat kernel — and this article states the self-adjointness and the spectrum with that citation. No physics is invoked.

## The Spin Structure and the Spinor Bundle

Let $(M,g)$ be an oriented Riemannian manifold of dimension $n$, with orthonormal frame bundle $P_{\mathrm{SO}}\to M$, a principal $\mathrm{SO}(n)$-bundle.

**Definition.** A **spin structure** on $(M,g)$ is a principal $\mathrm{Spin}(n)$-bundle $P_{\mathrm{Spin}}\to M$ with an equivariant two-fold covering $P_{\mathrm{Spin}}\to P_{\mathrm{SO}}$ over the covering $\mathrm{Spin}(n)\to\mathrm{SO}(n)$; a **spin manifold** is an oriented Riemannian manifold equipped with one, and the spin structure exists exactly when $w_{2}(TM)=0$, the spin structures being then a torsor over $H^{1}(M;\mathbb{Z}/2)$.

**Definition.** The **spinor bundle** $\mathcal{S}\to M$ is the associated bundle $P_{\mathrm{Spin}}\times_{\Delta}\Delta$ for the complex spin representation $\Delta$ of $\mathrm{Spin}(n)$; it carries the **Clifford multiplication**

$$
c:TM\otimes\mathcal{S}\longrightarrow\mathcal{S},\qquad c(v)^{2}=-|v|^{2}\,\mathrm{id},
$$

and the **spin connection** $\nabla^{\mathcal{S}}$ induced by the Levi-Civita connection of $g$, which is metric for the spinor inner product and compatible with the Clifford multiplication. In even dimension the spinor bundle splits by the chirality of the complex volume element into the **half-spinor bundles**

$$
\mathcal{S}=\mathcal{S}^{+}\oplus\mathcal{S}^{-},\qquad c(v)\mathcal{S}^{\pm}=\mathcal{S}^{\mp},
$$

and the splitting is preserved by the spin connection. The construction, the obstruction $w_2$, the classification of spin structures, the chirality and the reality structure of the spinors are the subject of *Spin Geometry* and of *Spin Representations and Clifford Modules with Inner Conjugation*; the twisted operator with coefficients in a Clifford module, and the curvature of the twisting connection, are those of *Clifford Modules and the Twisted Cauchy–Riemann Operator*.

## The Operator and Its Chirality

**Definition.** The **Cauchy–Riemann operator** (classically the **Dirac operator**) of a spin manifold is the first-order differential operator

$$
D=\sum_{i=1}^{n}c(e_i)\,\nabla^{\mathcal{S}}_{e_i}:\Gamma(\mathcal{S})\longrightarrow\Gamma(\mathcal{S}),
$$

for a local $g$-orthonormal frame $(e_i)$ of tangent vector fields; in even dimension its restrictions to the half-spinor bundles are written $D^{\pm}:\Gamma(\mathcal{S}^{\pm})\to\Gamma(\mathcal{S}^{\mp})$.

**Theorem.** The operator $D$ is formally self-adjoint for the spinor inner product, $D^{*}=D$; it is elliptic with principal symbol the Clifford multiplication

$$
\sigma_D(\xi)=i\,c(\xi),\qquad \sigma_D(\xi)^{2}=|\xi|^{2}\,\mathrm{id},
$$

invertible for $\xi\neq0$; and it anticommutes with the chirality, so in even dimensions it maps $\mathcal{S}^{\pm}$ to $\mathcal{S}^{\mp}$ and the two chiral halves $D^{+}$ and $D^{-}$ are formally adjoint.

**Proof.** The formal self-adjointness is the compatibility of the spin connection with the spinor metric and the skew-adjointness of the Clifford multiplication, together with the divergence identity for the connection; the symbol is the Clifford multiplication, whose square is $-|\xi|^{2}$, up to the normalising factor $i$ that makes the symbol of a real first-order operator; the anticommutation with the chirality is the property $c(v)\omega_{\mathbb{C}}=-\omega_{\mathbb{C}}c(v)$ of the complex volume element, whence $D$ exchanges the two halves. $\square$

**Remark.** The operator is the curved-space member of the family of Cauchy–Riemann operators of the corpus, the flat member being the operator $e_\mu\partial_\mu$ of the Clifford algebra; the classical name is the Dirac operator. It is a first-order self-adjoint elliptic operator whose square is a second-order operator, exactly as the signature operator $d+d^{*}$ is, and it is the model of the operators of this category. The analytic theory of the operator — the precise domain, the closed extensions, the completeness of the eigenspinors and the heat kernel — belongs to Part III, where the measure and the limit are available, and the statements above are the formal identities that Part III completes.

## The Lichnerowicz Formula

**Theorem (Lichnerowicz).** The square of the operator satisfies

$$
D^{2}=\nabla^{*}\nabla+\tfrac14\operatorname{scal}\cdot\mathrm{id},
$$

where $\nabla^{*}\nabla=-\operatorname{tr}_g(\nabla^{\mathcal{S}})^2$ is the connection Laplacian on the spinors and $\operatorname{scal}$ is the scalar curvature of $(M,g)$.

**Proof sketch.** Expanding $D^{2}=\sum_{i,j}c(e_i)c(e_j)\nabla^{\mathcal{S}}_{i}\nabla^{\mathcal{S}}_{j}$ and splitting into the symmetric and antisymmetric parts, the Clifford relations $c(e_i)c(e_j)+c(e_j)c(e_i)=-2\delta_{ij}$ turn the symmetric part into the connection Laplacian, and the antisymmetric part is the curvature of the spin connection Clifford-multiplied; its trace over the spinorial indices is $\tfrac14\operatorname{scal}$, the identity of the Clifford algebra in dimension $n$. The computation is that of *Spin Geometry* and *Clifford Modules and the Twisted Cauchy–Riemann Operator*, and it is the spin form of the Weitzenböck formula $\Delta=\nabla^{*}\nabla+\mathcal{R}$ of *The Hodge Laplacian*. $\square$

**Corollary.** On a closed spin manifold the operator has compact resolvent, discrete spectrum and complete eigenspinors; its spectrum is real and symmetric about the origin, $\lambda\leftrightarrow-\lambda$ in even dimensions, because $D$ anticommutes with the chirality; and its kernel consists of the **harmonic spinors**, the spinors with $D\psi=0$ and $\nabla\psi=0$ whenever the scalar curvature is nonnegative.

## The Index and the $\hat A$-Genus

**Theorem (Atiyah–Singer, spin case).** Let $M$ be a closed spin manifold of even dimension. Then the chiral halves $D^{\pm}$ are Fredholm operators and the index of the positive half is the **$\hat A$-genus**

$$
\operatorname{ind}D^{+}=\dim\ker D^{+}-\dim\ker D^{-}=\int_{M}\hat A(TM)=\hat A[M],
$$

where $\hat A(TM)$ is the $\hat A$-class of the tangent bundle, the genus with the first terms

$$
\hat A=1-\frac{p_1}{24}+\frac{7p_1^{2}-4p_2}{5760}-\cdots
$$

in the Pontryagin classes $p_i$ of $TM$. In particular $\hat A[M]$ is an integer for a closed spin manifold.

**Proof sketch.** A harmonic spinor solves $D\psi=0$, and the self-adjointness identifies the kernel of $D$ with the direct sum $\ker D^{+}\oplus\ker D^{-}$, so the index is the difference of the two chiral kernel dimensions; the identification of the index with $\int_M\hat A(TM)$ is the Atiyah–Singer theorem for the spin symbol, whose symbol class is the Bott class with Chern character the $\hat A$-class. The general theorem and its heat-kernel proof are in *The Atiyah–Singer Index Theorem and K-Theory*; the integrality of the $\hat A$-genus on a spin manifold is the Borel–Hirzebruch integrality theorem, and in dimension four it yields Rökhlin's theorem, that the signature of a closed spin four-manifold is divisible by $16$. $\square$

**Corollary (the twisted operator).** For the operator twisted by a Hermitian vector bundle $E$ with connection, $D_E:\Gamma(\mathcal{S}\otimes E)\to\Gamma(\mathcal{S}\otimes E)$, the index of the positive half is

$$
\operatorname{ind}D_E^{+}=\int_{M}\hat A(TM)\operatorname{ch}(E),
$$

the $\hat A$-genus paired with the Chern character of the twisting bundle; the twisted operator, its Weitzenböck curvature $\mathcal{R}^{E}=\tfrac14\operatorname{scal}+c(F^{W})$ and its index are those of *Clifford Modules and the Twisted Cauchy–Riemann Operator*.

## Positive Scalar Curvature and Vanishing

**Theorem (Lichnerowicz vanishing).** Let $M$ be a closed spin manifold of strictly positive scalar curvature. Then the operator has no nonzero harmonic spinor, $\ker D=0$, and its index vanishes,

$$
\operatorname{scal}>0\ \text{on }M\quad\Longrightarrow\quad \hat A[M]=\operatorname{ind}D^{+}=0 .
$$

**Proof.** For a spinor $\psi$ the Lichnerowicz formula gives

$$
\|D\psi\|^{2}=(D^{2}\psi,\psi)=(\nabla^{*}\nabla\psi,\psi)+\tfrac14\int_M\operatorname{scal}|\psi|^{2}
=\|\nabla\psi\|^{2}+\tfrac14\int_M\operatorname{scal}|\psi|^{2},
$$

using the self-adjointness of the connection Laplacian; if $D\psi=0$ and $\operatorname{scal}>0$, the second term is strictly positive unless $\psi=0$, so $\psi=0$, and both chiral kernels vanish. $\square$

**Corollary (the obstruction).** A closed spin manifold with $\hat A[M]\neq0$ carries no metric of positive scalar curvature; the $K3$ surface, with $\hat A[K3]=2$, is the standard example, and the argument is the prototype of the index-theoretic obstructions to positive scalar curvature of Gromov–Lawson and of Schoen–Yau. The vanishing is one-way: $\hat A=0$ does not produce a positive-scalar-curvature metric, and the existence question is the subject of the surgery theory of *Differential Topology* and its analytic refinements. In dimension four the integrality of the $\hat A$-genus reads $-\sigma/8\in\mathbb{Z}$, and Rökhlin's theorem sharpens it to $16\mid\sigma$ for a closed spin four-manifold.

## Examples

**Example (the spheres).** The sphere $S^{n}$ with the round metric is spin, and its $\hat A$-genus vanishes: the tangent bundle is stably trivial, $TS^{n}\oplus\mathbb{R}\cong\mathbb{R}^{n+1}$, so all Pontryagin classes vanish, and in particular $\hat A[S^{4}]=0$. The round sphere has constant positive scalar curvature, so the vanishing theorem applies and the operator has no harmonic spinor; the spectrum of the operator on $S^{n}$ is symmetric and its eigenvalues are computed from the spin representations, the eigenspinors being the spinor spherical harmonics.

**Example (the flat torus).** The torus $T^{n}$ is spin and flat; the scalar curvature vanishes, the Lichnerowicz formula reduces to $D^{2}=\nabla^{*}\nabla$, and the harmonic spinors are the parallel spinors, of dimension the dimension of the spin representation. The twisted operator on the torus gives the theta-function computations of the index, and the example is the flat case against which the curved index theorem is checked.

**Example (a $K3$ surface).** The $K3$ surface is spin with $\hat A[K3]=2$, so the index of its operator is $2$, the difference of the two chiral kernel dimensions; by the vanishing theorem the surface admits no positive scalar curvature metric. The value $\hat A[K3]=2$ is the standard nonvanishing example and the obstruction that separates the simply connected spin four-manifolds from those admitting positive scalar curvature.

**Example (the complex projective plane).** The manifold $\mathbb{CP}^{2}$ is not spin, since $w_{2}\neq0$; the spin operator is therefore not defined on it, and its place is taken by the $\operatorname{Spin}^{c}$ operator, whose spinor bundle exists with a determinant line bundle and whose index is $\int_{M}e^{c_{1}(L)/2}\hat A(TM)$. In the Kähler case the $\operatorname{Spin}^{c}$ index is the holomorphic Euler characteristic and the formula is the Riemann–Roch–Hirzebruch theorem; the example shows that the spin condition is a genuine restriction and that the theory extends to the non-spin case by twisting.

## Summary

A **spin structure** on an oriented Riemannian manifold is a two-fold cover of the frame bundle by a $\mathrm{Spin}(n)$-bundle, existing exactly when $w_{2}(TM)=0$, and it carries the **spinor bundle** $\mathcal{S}$ with its Clifford multiplication $c$, $c(v)^{2}=-|v|^{2}$, its metric spin connection and, in even dimensions, its chirality splitting $\mathcal{S}=\mathcal{S}^{+}\oplus\mathcal{S}^{-}$. The **Cauchy–Riemann operator** $D=\sum_ic(e_i)\nabla^{\mathcal{S}}_{e_i}$, classically the **Dirac operator**, is formally self-adjoint and elliptic with symbol $i\,c(\xi)$, and it exchanges the half-spinor bundles. The **Lichnerowicz formula** $D^{2}=\nabla^{*}\nabla+\tfrac14\operatorname{scal}$ expresses the square through the connection Laplacian and the scalar curvature, and it gives the **vanishing theorem**: a closed spin manifold of strictly positive scalar curvature has no harmonic spinor and vanishing $\hat A$-genus. The index of the positive half is the **$\hat A$-genus**, $\operatorname{ind}D^{+}=\int_M\hat A(TM)$, an integer for a closed spin manifold; the twisted version pairs $\hat A$ with the Chern character of the twisting bundle; and in dimension four the integrality gives Rökhlin's divisibility $16\mid\sigma$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_{\mathrm{SO}}$, $P_{\mathrm{Spin}}$ | Orthonormal frame bundle, spin structure |
| $w_{2}(TM)=0$ | The obstruction to a spin structure |
| $\mathcal{S}=\mathcal{S}^{+}\oplus\mathcal{S}^{-}$ | Spinor bundle and its chirality splitting |
| $c(v)$, $c(v)^2=-|v|^2$ | Clifford multiplication |
| $\nabla^{\mathcal{S}}$ | Spin connection (Levi-Civita lifted to the spinors) |
| $D=\sum_ic(e_i)\nabla^{\mathcal{S}}_{e_i}$ | Cauchy–Riemann operator (Dirac operator); $D^{\pm}:\Gamma(\mathcal{S}^{\pm})\to\Gamma(\mathcal{S}^{\mp})$ |
| $\sigma_D(\xi)=i\,c(\xi)$ | Principal symbol |
| $D^2=\nabla^{*}\nabla+\tfrac14\operatorname{scal}$ | Lichnerowicz formula |
| $\operatorname{scal}$ | Scalar curvature |
| $\hat A(TM)=1-p_1/24+\cdots$ | $\hat A$-class; $\operatorname{ind}D^{+}=\int_M\hat A(TM)$ |
| $\operatorname{ind}D_E^{+}=\int_M\hat A\operatorname{ch}(E)$ | Twisted index formula |
| $\operatorname{scal}>0\Rightarrow\hat A[M]=0$ | Lichnerowicz vanishing; $16\mid\sigma$ in dimension four (Rökhlin) |

## Further Reading

- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the spin structures, the spinor bundle, the Cauchy–Riemann operator, the Lichnerowicz formula and the index theory.
- André Lichnerowicz, "Spineurs harmoniques," *Comptes Rendus de l'Académie des Sciences* **257** (1963), 7–9, for the formula $D^{2}=\nabla^{*}\nabla+\tfrac14\operatorname{scal}$ and the vanishing theorem.
- Michael F. Atiyah and Isadore M. Singer, "The index of elliptic operators I, III," *Annals of Mathematics* **87** (1968), 484–530 and 546–604, for the index theorem and the $\hat A$-genus.
- Mikhael Gromov and H. Blaine Lawson, "Positive scalar curvature and the Dirac operator on complete Riemannian manifolds," *Publications Mathématiques de l'IHÉS* **58** (1983), 83–196, for the obstruction to positive scalar curvature.
- Jean-Pierre Bourguignon and Paul Gauduchon, "Spineurs, opérateurs de Dirac et variations de métriques," *Communications in Mathematical Physics* **144** (1992), 581–599, for the variation of the operator and the Lichnerowicz formula.
- Thomas Friedrich, *Dirac Operators in Riemannian Geometry*, Graduate Studies in Mathematics 25 (American Mathematical Society, 2000), for a systematic account of the operator and its applications.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works, Volume 2 (Springer, 1997), for the algebraic foundations of the spin representations.
