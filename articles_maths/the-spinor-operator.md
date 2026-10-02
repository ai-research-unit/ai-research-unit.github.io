
# __The Spinor Operator__

## Introduction

A spin manifold carries a spinor bundle, and the geometric datum that differentiates its sections is the **spin connection**, the lift of the Levi-Civita connection along the double covering $\operatorname{Spin}(n)\to SO(n)$. This article treats the spin connection as an operator and the first-order operator it defines, the **spinor operator**, whose contraction with the Clifford multiplication is the Cauchy–Riemann operator of the manifold. The distinction from the structure article is deliberate: *Spin Geometry* constructs the spin structure, the spinor bundle and the operator, and the present article separates the two operators that make it up, states their compatibility, and reads the geometry that the chosen metric forces on them.

The spin connection is the unique connection on the spinor bundle that is compatible with the Levi-Civita connection, with the Hermitian form on the spinors and with the Clifford multiplication. Its curvature is the lift of the Riemann curvature to the spin bundle, a two-form with values in the bivectors, and it is the object that the Weitzenböck identity of *Spin Geometry* evaluates on the spinors. The operator it defines is elliptic with symbol the Clifford multiplication, it is formally self-adjoint for a closed manifold, and it is odd for the chirality grading in even dimension. Its square is the connection Laplacian plus a quarter of the scalar curvature, the Lichnerowicz formula, and the formula shows that the operator is a distance-reading: the curvature term is the scalar curvature of the chosen metric, so the whole analytic behaviour of the operator is decided by the metric and not by the topology alone.

**The boundaries.** The spin structure, its obstruction and the spinor bundle are *Spin Geometry*, and the Lichnerowicz formula, the index theorem and the $\operatorname{Spin}^c$ refinement are quoted from it rather than proved again. The analytic theory of the operator — its self-adjointness as an unbounded operator, its spectrum and the completeness of the eigenspinors — belongs to Part III, where the measure and the limit are available, and is cited. The conformal covariance of the operator and the first-order operator built from its kernel are the subject of *The Twistor Operator* and *The Penrose Operator*, written in parallel in this category; the conformal model of Euclidean space is *The Conformal Model of Euclidean Space*. The Riemannian metric, the Levi-Civita connection and the curvature are *Riemannian Geometry*; the associated bundles and the connection forms are *Fibre Bundles, Connections and Curvature*. The base is a smooth Riemannian manifold $(M,g)$ of dimension $n$, and the Clifford convention is the one of *Spin Geometry*, $c(v)^2=-g(v,v)\operatorname{id}$.

## The Spin Connection

### The Lift of the Levi-Civita Connection

**Definition.** Let $(M,g)$ be an oriented Riemannian manifold with spin structure $P_{\operatorname{Spin}}(M)$ and spinor bundle $\mathcal{S}=P_{\operatorname{Spin}}(M)\times_{\operatorname{Spin}(n)}\Delta_n$. The **spin connection** is the connection $\nabla^{\mathcal{S}}$ on $\mathcal{S}$ induced by the Levi-Civita connection $\nabla$ of $g$ through the spin structure: in a local orthonormal frame $(e_1,\dots,e_n)$ it is

$$
\nabla^{\mathcal{S}}_X\sigma = X(\sigma) + \tfrac14\sum_{i,j=1}^{n}\omega_{ij}(X)\,c(e_i)c(e_j)\sigma ,
\qquad
\omega_{ij} = g(\nabla_X e_i, e_j) .
$$

The one-form $\omega^{\mathcal{S}} = \tfrac14\sum_{i,j}\omega_{ij}c(e_i)c(e_j)$, with values in the bivectors $\Lambda^2TM \subseteq \mathrm{Cl}(TM)$, is the **spin connection form**; it is the image of the Levi-Civita connection form under the Lie-algebra isomorphism $\mathfrak{so}(n)\to\mathfrak{spin}(n)$, $e_i\wedge e_j\mapsto \tfrac12 c(e_i)c(e_j)$.

**Proposition.** The spin connection is the unique connection on $\mathcal{S}$ whose connection form takes values in the image of $\mathfrak{spin}(n)$ inside the Clifford algebra; it is the associated connection of the principal $\operatorname{Spin}(n)$-bundle $P_{\operatorname{Spin}}(M)$ under the representation $\Delta_n$.

**Proof.** This is the general construction of an associated connection from a principal connection and a representation, applied to the spin structure of *Spin Geometry*; the connection form of the associated bundle is the image of the principal connection form, and a principal connection on $P_{\operatorname{Spin}}(M)$ has a connection form with values in the Lie algebra $\mathfrak{spin}(n)$, identified with the bivectors by the isomorphism above. Uniqueness is the uniqueness of the lift of the Levi-Civita connection along the double covering.

**Proposition (the local form as a derivation).** For a local orthonormal frame the connection form is $\omega^{\mathcal{S}}=\tfrac12\sum_{i<j}\omega_{ij}c(e_i)c(e_j)$, and the covariant derivative is a derivation over the Clifford multiplication,

$$
\nabla^{\mathcal{S}}_X\bigl(c(v)\sigma\bigr) = c(\nabla_X v)\sigma + c(v)\,\nabla^{\mathcal{S}}_X\sigma ,
$$

for every vector field $v$ and every spinor field $\sigma$.

**Proof.** The diagonal terms of the sum vanish because $\omega_{ii}=g(\nabla_Xe_i,e_i)=0$, which holds since $\nabla$ is metric-compatible and $g(e_i,e_i)=1$ is constant; so $\tfrac14\sum_{i,j}\omega_{ij}c(e_i)c(e_j)=\tfrac12\sum_{i<j}\omega_{ij}c(e_i)c(e_j)$. For the Leibniz rule, both sides are local in the frame and $X$-linear; on a frame field with constant coefficients $v=\sum v^ie_i$, the left side is $X(\sum v^i\,c(e_i)\sigma)$ and the right side is $\sum v^i\,c(\nabla_Xe_i)\sigma+\sum v^i c(e_i)X(\sigma)$. The difference is $\sum v^i\bigl(c(\nabla_Xe_i)+\tfrac12\sum_{j<k}\omega_{jk}(X)c(e_j)c(e_k)c(e_i)-c(e_i)\tfrac12\sum_{j<k}\omega_{jk}(X)c(e_j)c(e_k)\bigr)\sigma$; writing $\nabla_Xe_i=\sum_j\omega_{ij}(X)e_j$ and using $\tfrac12[c(e_j)c(e_k),c(e_i)]=\delta_{ik}c(e_j)-\delta_{ij}c(e_k)$, the inner sum telescopes to $c(\nabla_Xe_i)$, and the two sides agree.

**Definition.** The **curvature of the spin connection** is the two-form $R^{\mathcal{S}}$ on spinors, defined by

$$
R^{\mathcal{S}}(X,Y)\sigma = \nabla^{\mathcal{S}}_X\nabla^{\mathcal{S}}_Y\sigma - \nabla^{\mathcal{S}}_Y\nabla^{\mathcal{S}}_X\sigma - \nabla^{\mathcal{S}}_{[X,Y]}\sigma .
$$

**Proposition (the lift of the Riemann curvature).** With $R$ the Riemann curvature tensor of $(M,g)$ and $R_{ij}(X,Y)=g(R(X,Y)e_i,e_j)$ its components in an orthonormal frame,

$$
R^{\mathcal{S}}(X,Y)\sigma = \tfrac14\sum_{i,j}R_{ij}(X,Y)\,c(e_i)c(e_j)\sigma ;
$$

the spin curvature is the image of the curvature form of the Levi-Civita connection under the same Lie-algebra isomorphism that sends the connection to its spin value. In particular the spin connection is flat exactly when the metric is flat.

**Proof.** The curvature of an associated connection is the image of the curvature form of the principal connection; the curvature form of the Levi-Civita connection is $\Omega_{ij}=d\omega_{ij}+\sum_k\omega_{ik}\wedge\omega_{kj}$, whose value is the Riemann components, and applying the isomorphism $e_i\wedge e_j\mapsto\tfrac12c(e_i)c(e_j)$ and using the antisymmetry of the components gives the display.

### Compatibility with the Metric and the Clifford Action

**Given.** The spinor bundle carries a Hermitian form $h$ for which the Clifford multiplication is skew-adjoint, $c(v)^*=-c(v)$, as in *Spin Geometry* and *Adjoints on a Clifford Module*; the form is induced from a Hermitian form on the spin module $\Delta_n$ invariant under $\operatorname{Spin}(n)$, and it is positive definite.

**Proposition.** The spin connection is compatible with the Hermitian form,

$$
X\bigl(h(\sigma,\tau)\bigr) = h(\nabla^{\mathcal{S}}_X\sigma,\tau) + h(\sigma,\nabla^{\mathcal{S}}_X\tau),
$$

and with the Clifford multiplication in the sense of the derivation identity above. These two compatibilities characterise it among the connections on $\mathcal{S}$.

**Proof.** Compatibility with $h$ holds for the associated connection of any connection whose structure group acts by isometries of the fibre form, since $\operatorname{Spin}(n)$ acts unitarily on $\Delta_n$; concretely, the spin connection form is skew-adjoint because $c(e_i)c(e_j)$ is skew-adjoint for $i\neq j$, so the defining first-order operator is skew-adjoint for $h$. Compatibility with the Clifford action is the derivation identity, and the two properties characterise the connection because their difference is a one-form with values in the endomorphisms of $\mathcal{S}$ annihilated by the Clifford algebra, which is zero on an irreducible spinor bundle.

**Remark (why the spin connection is the geometric operator of the article).** The spin structure is a choice of a lift of the frame bundle, and the spin connection is what that choice buys: the Levi-Civita connection alone is defined on tensors, and its action on spinors is not defined until the structure group is lifted. Once lifted, the spin connection is the unique differentiation compatible with the metric, the Clifford action and the module form; every other operator of the spin geometry is built from it and the Clifford multiplication, and no further choice enters.

## The Spinor Operator

### Definition and Symbol

**Definition.** The **spinor operator** is the first-order differential operator

$$
D = c\circ\nabla^{\mathcal{S}} : \Gamma(\mathcal{S}) \longrightarrow \Gamma(\mathcal{S}),
\qquad
D\sigma = \sum_{i=1}^{n} c(e_i)\,\nabla^{\mathcal{S}}_{e_i}\sigma ,
$$

the contraction of the spin connection with the Clifford multiplication in a local orthonormal frame. It is also called the **Cauchy–Riemann operator** of the spin manifold; the classical name for it is the Dirac operator, and the corpus keeps the flat case of the same family in *Clifford Modules and the Twisted Cauchy–Riemann Operator*.

**Proposition (the frame independence).** The expression for $D$ is independent of the orthonormal frame, and $D$ is a first-order differential operator whose principal symbol is the Clifford multiplication,

$$
\sigma_D(x,\xi)\sigma = c(\xi)\sigma , \qquad \xi\in T_x^*M ,
$$

the tangent vector being identified with the cotangent vector through $g$. The symbol is invertible for $\xi\neq0$, so $D$ is elliptic, and its square is a Laplace-type operator of order two.

**Proof.** A change of orthonormal frame acts by a pointwise orthogonal transformation $a$, which sends $\sum_ic(e_i)\nabla_{e_i}$ to $\sum_i c(ae_i)\nabla_{ae_i}=\sum_ic(e_i)\nabla_{e_i}$ because the Clifford action is isometric and the connection is the associated one; the symbol is the highest-order part, computed by freezing the coefficients; $c(\xi)^2=-g(\xi,\xi)\operatorname{id}$ is invertible for $\xi\neq0$; and the square of a first-order operator with invertible symbol is elliptic of order two.

**Proposition (parity).** The operator $D$ is a graded operator of odd parity with respect to the chirality grading: for $n$ even the spinor bundle splits as $\mathcal{S}=\mathcal{S}^+\oplus\mathcal{S}^-$ with $c(v)$ exchanging the summands, and $D$ splits as

$$
D = \begin{pmatrix} 0 & D^- \\ D^+ & 0\end{pmatrix},
\qquad D^\pm : \Gamma(\mathcal{S}^\pm) \longrightarrow \Gamma(\mathcal{S}^\mp) .
$$

For $n$ odd there is no such splitting over the Clifford algebra, and $D$ carries the single spinor bundle to itself.

**Proof.** The statement is the module theory of the spin representations of *Spin Geometry*: the chirality operator is central in even dimension and acts on $\Delta_n$ with eigenvalues $\pm1$, and $c(v)$ anticommutes with it, so it exchanges the eigenspaces; in odd dimension $c(v)$ commutes with the volume element, which is then a scalar on the irreducible module and gives no splitting.

### Self-Adjointness and the Square

**Proposition (formal self-adjointness).** For a closed manifold $M$ the spinor operator is formally self-adjoint with respect to the $L^2$ form of $h$, $\int_M h(D\sigma,\tau)\,d\text{vol}_g=\int_M h(\sigma,D\tau)\,d\text{vol}_g$, and the operator $D$ is symmetric on the smooth sections.

**Proof.** The formal adjoint of the covariant derivative is the negative of the metric contraction, $(\nabla^{\mathcal{S}})^*=-\operatorname{tr}_g\nabla^{\mathcal{S}}$, because $\nabla^{\mathcal{S}}$ is metric-compatible; the adjoint of the Clifford multiplication is $(c(e_i))^*=-c(e_i)$; and the composition of the two adjoints is the same operator $D$, the two signs cancelling. The boundary term vanishes on a manifold without boundary.

**Theorem (Lichnerowicz, quoted).** Let $D$ be the spinor operator of a spin manifold $(M,g)$ with the spin connection. Then

$$
D^2 = \nabla^{*}\nabla + \tfrac14\operatorname{scal},
$$

where $\nabla^{*}\nabla$ is the connection Laplacian on spinors and $\operatorname{scal}$ is the scalar curvature of $g$.

**Proof sketch.** The Weitzenböck computation of *Spin Geometry*, cited: the second-order terms of $D^2$ assemble into the connection Laplacian, and the zeroth-order remainder is evaluated by expanding $c(e_i)c(e_j)R^{\mathcal{S}}(e_i,e_j)$, which the spin-curvature proposition turns into the scalar curvature through the symmetries of the Riemann tensor. The identity is the geometric content of the article: the operator is the chosen metric read through the spin connection, and the curvature is the field of the metric.

**Corollary (the metric dependence).** A closed spin manifold of positive scalar curvature has no harmonic spinors, $D\sigma=0$ implies $\sigma=0$: the integral of $h(D^2\sigma,\sigma)$ is the sum of the non-negative term $\int|\nabla^{\mathcal{S}}\sigma|^2$ and the positive term $\tfrac14\int\operatorname{scal}|\sigma|^2$, so both must vanish.

**Proof.** Integrate the identity $h(D^2\sigma,\sigma)=|\nabla^{\mathcal{S}}\sigma|^2+\tfrac14\operatorname{scal}|\sigma|^2$, which follows from the formula and the compatibility of the spin connection, against the volume form; the left side is $\int|D\sigma|^2$ for a closed manifold, and both terms on the right are non-negative.

### The Conformal Change of the Operator

**Proposition (the operator under a conformal change).** Let $\hat g=\Omega^2g$ be a metric conformal to $g$ with $\Omega>0$, with the spinor bundles identified by the conformal factor in the standard way. Then the operator transforms as

$$
\hat D\bigl(\Omega^{-(n-1)/2}\sigma\bigr) = \Omega^{-(n+1)/2}\,D\sigma + \Omega^{-(n+1)/2}\,c(\operatorname{grad}\log\Omega)\,\sigma ,
$$

so that the operator is not conformally invariant but acquires a zeroth-order term; the combination that removes the term is the subject of *The Penrose Operator*.

**Proof sketch.** The conformal change of the Levi-Civita connection and of the spin connection is standard, and the two terms come from the change of the frame and of the volume element; the computation is the conformal covariance of the Cauchy–Riemann operator recorded in the references. This is a forward reference to the conformal operator, and the invariance statement there is the reason the twistor and Penrose operators exist.

## Worked Cases

### The Flat Space

For $M=\mathbb{R}^n$ with the Euclidean metric and the trivial spin structure, the spin connection is the ordinary derivative and the spinor operator is the constant-coefficient operator $D=\sum_ic(e_i)\partial_i$, with $D^2=-\Delta$ on spinor-valued functions and with kernel the monogenic spinors of *Clifford Analysis*. The flat case is the model for the symbol and the elliptic regularity of the general operator.

### The Round Sphere

For $M=S^n$ with the round metric the scalar curvature is $n(n-1)$ and the Lichnerowicz formula forces $D^2\ge\tfrac{n(n-1)}{4}$. The spectrum of $D$ is the set $\pm(k+n/2)$, $k\ge0$, with multiplicities the dimensions of the spin representations, as *Spin Geometry* records; the operator is self-adjoint with compact resolvent, and the positivity of its square is the scalar curvature read by the operator.

### A Surface

For $n=2$ the spinor bundle has rank two and splits into two complex line bundles; the spin connection is the $\bar\partial$-type connection twisted by a square root of the canonical bundle, and the operator is the corresponding twisted $\bar\partial$-type operator. The Lichnerowicz term vanishes in dimension two, and the operator is conformally invariant on a surface with the appropriate weight, which is the origin of the string of conformal operators of this category.

## Summary

The **spin connection** $\nabla^{\mathcal{S}}$ is the unique connection on the spinor bundle induced by the Levi-Civita connection through the spin structure; its connection form is $\omega^{\mathcal{S}}=\tfrac14\sum_{i,j}\omega_{ij}c(e_i)c(e_j)$ with values in the bivectors, it is compatible with the Hermitian form and with the Clifford multiplication, and its curvature is the lift $R^{\mathcal{S}}=\tfrac14\sum_{i,j}R_{ij}c(e_i)c(e_j)$ of the Riemann curvature. The **spinor operator** is the contraction $D=c\circ\nabla^{\mathcal{S}}=\sum_ic(e_i)\nabla^{\mathcal{S}}_{e_i}$, a first-order elliptic operator with symbol the Clifford multiplication $c(\xi)$; it is formally self-adjoint on a closed manifold, and it is odd for the chirality grading in even dimension, splitting into the two chiral operators $D^\pm$. Its square satisfies the **Lichnerowicz formula** $D^2=\nabla^*\nabla+\tfrac14\operatorname{scal}$, so the operator reads the scalar curvature of the chosen metric and a closed spin manifold of positive scalar curvature has no harmonic spinors. The operator is not conformally invariant; under a conformal change it acquires a zeroth-order term, and the conformally invariant operator built from it is the subject of *The Twistor Operator* and *The Penrose Operator*. The analytic theory of the operator and the index of its chiral part belong to Part III and to the index theory of this part, and are cited.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(M,g)$, $n$ | Riemannian spin manifold and its dimension |
| $P_{\operatorname{Spin}}(M)$, $\mathcal{S}$ | Spin structure and spinor bundle |
| $\Delta_n$, $\mathcal{S}^\pm$ | Spin module and its chiral halves for $n$ even |
| $c(v)$ | Clifford multiplication, $c(v)^2=-g(v,v)\operatorname{id}$ |
| $\nabla$, $\omega_{ij}=g(\nabla e_i,e_j)$ | Levi-Civita connection and its connection form |
| $\nabla^{\mathcal{S}}$, $\omega^{\mathcal{S}}=\tfrac14\sum\omega_{ij}c(e_i)c(e_j)$ | Spin connection and spin connection form |
| $R$, $R^{\mathcal{S}}=\tfrac14\sum R_{ij}c(e_i)c(e_j)$ | Riemann curvature and spin curvature |
| $h$ | Hermitian form on the spinors, $c(v)^*=-c(v)$ |
| $D=c\circ\nabla^{\mathcal{S}}=\sum_ic(e_i)\nabla^{\mathcal{S}}_{e_i}$ | Spinor operator, the Cauchy–Riemann operator of the manifold |
| $D^\pm$ | Chiral parts for $n$ even |
| $\operatorname{scal}$, $\nabla^*\nabla$ | Scalar curvature and connection Laplacian |
| $\hat g=\Omega^2g$ | Conformal change of the metric |

## Further Reading

- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the spin connection, the Cauchy–Riemann operator, the Lichnerowicz formula and the index theory.
- Nicole Berline, Ezra Getzler and Michèle Vergne, *Heat Kernels and Dirac Operators* (Springer, 1992), for the Weitzenböck calculus and the heat-kernel proof of the index theorem.
- John W. Milnor and James D. Stasheff, *Characteristic Classes* (Princeton University Press, 1974), for the spin obstruction and the characteristic classes of the spinor bundle.
- Michael F. Atiyah and Isadore M. Singer, "The Index of Elliptic Operators III", *Annals of Mathematics* 87 (1968), 546–604, for the index of the chiral operator and the $\hat A$-genus.
- André Lichnerowicz, "Spineurs harmoniques", *Comptes Rendus de l'Académie des Sciences* 257 (1963), 7–9, for the formula $D^2=\nabla^*\nabla+\tfrac14\operatorname{scal}$ and the vanishing of the harmonic spinors.
- Helga Baum, *Spin-Strukturen und Dirac-Operatoren über pseudoriemannschen Mannigfaltigkeiten* (Teubner, 1981), for the spin connection in the indefinite setting and the derivation identities.
