# __Hermitian Structures and the Almost Complex Structure__

## Introduction

An **almost complex structure** on a smooth manifold is a bundle endomorphism $J$ of the tangent bundle with $J^2 = -\mathrm{id}$, the pointwise datum of a multiplication by $\sqrt{-1}$ on each tangent space. A **Hermitian structure** is the pair of that involution with a Riemannian metric for which $J$ is an isometry; it is the structure whose bundle-theoretic form the previous entries of the group developed, and whose operator form — the type decomposition of the complexified forms, the operators $\partial$ and $\bar\partial$, and the **Nijenhuis tensor** that decides the integrability — is the content of the present article.

The article develops the almost complex structure and the Hermitian structure through their **operators**. It defines the involution, the $\pm i$-eigenbundles and the type decomposition of the complexified differential forms; it defines the partial derivatives $\partial$ and $\bar\partial$ as the type components of the exterior derivative, proves that $d = \partial + \bar\partial$ exactly when the almost complex structure is integrable, and proves that this is equivalent to the vanishing of the Nijenhuis tensor $N_J$ — the theorem of Newlander and Nijenhuis; it derives $\partial^2 = \bar\partial^2 = 0$ and $\partial\bar\partial + \bar\partial\partial = 0$, so that the forms become the **Dolbeault double complex**; and it identifies the Hermitian structure as the pair of the involution with an invariant metric, with the fundamental form as its operator shadow.

The article assumes the almost complex structures, the Nijenhuis tensor, the integrability, the Hermitian metrics, the fundamental form and the Dolbeault complex as geometric objects of *Hermitian Geometry and Almost Complex Structures* in Part IV; the metric, the fundamental form and the Kähler conditions of *Hermitian Metrics and the Levi-Civita Connection*; the Chern connection and its coefficients of *Hermitian Vector Bundles and the Chern Connection* and *Hermitian Manifolds and the Canonical Connection*; the exterior derivative, the forms and the type decomposition of *Differential Forms and Stokes' Theorem* and *The Exterior Derivative*; and the de Rham complex of the operator group. The Dolbeault cohomology as a complex and the $\bar\partial$-Poincaré lemma are stated here as operator consequences and their analytic theory is *Partial Differential Equations* and *The L2 Adjoint of a Differential Operator*. No physics is invoked.

## The Almost Complex Structure and the Type Decomposition

### The Involution and Its Eigenbundles

**Definition.** An **almost complex structure** on a smooth manifold $M$ is a bundle endomorphism $J : TM \to TM$ with $J^2 = -\mathrm{id}_{TM}$; the pair $(M,J)$ is an **almost complex manifold**. It exists only in even dimensions, where it reduces the structure group of the tangent bundle from $GL(2n,\mathbb{R})$ to $GL(n,\mathbb{C})$, as in *Hermitian Geometry and Almost Complex Structures*.

**Proposition.** The complexified tangent bundle $T_{\mathbb{C}}M = TM\otimes_{\mathbb{R}}\mathbb{C}$ splits into the eigenbundles of $J$ with eigenvalues $\pm i$,

$$
\boxed{\;T_{\mathbb{C}}M = T^{1,0}M \oplus T^{0,1}M, \qquad T^{1,0}M = \{v : Jv = iv\}, \quad T^{0,1}M = \{v : Jv = -iv\}\;},
$$

with $T^{0,1}M = \overline{T^{1,0}M}$; the projection onto $T^{1,0}M$ is $\tfrac12(\mathrm{id}-iJ)$. Dually, the complexified cotangent bundle splits as $T^*_{\mathbb{C}}M = \Lambda^{1,0}M\oplus\Lambda^{0,1}M$, and the complexified $k$-forms decompose into the **forms of type $(n,m)$**,

$$
\Lambda^kT^*_{\mathbb{C}}M = \bigoplus_{n+m=k}\Lambda^{n,m}M, \qquad \Omega^k(M;\mathbb{C}) = \bigoplus_{n+m=k}\Omega^{n,m}(M),
$$

where a $(n,m)$-form is a section of $\Lambda^{n,m}M = \Lambda^n\Lambda^{1,0}M\otimes\Lambda^m\Lambda^{0,1}M$.

*Proof.* The first two statements are the eigenbundle decomposition of the complexification of a real involution with eigenvalues $\pm i$, proved in *Hermitian Geometry and Almost Complex Structures*; the type decomposition of the exterior powers is the algebraic decomposition of the exterior algebra of a direct sum, applied fibrewise and made smooth.

### The Nijenhuis Tensor

**Definition.** The **Nijenhuis tensor** of an almost complex structure is the assignment

$$
N_J(X,Y) = [JX,JY] - J[X,JY] - J[JX,Y] - [X,Y], \qquad X, Y \in \mathrm{X}(M).
$$

**Theorem.** The Nijenhuis tensor is a well-defined tensor, antisymmetric and $C^\infty(M)$-bilinear, so it is a section of $\Lambda^2T^*M\otimes TM$; it satisfies $N_J(X,JX)=0$ and vanishes identically when $J$ comes from a complex atlas. The statement that $N_J$ is the only obstruction to $J$ being integrable is the theorem of Newlander and Nijenhuis, quoted from *Hermitian Geometry and Almost Complex Structures*: an almost complex structure is integrable, that is, it comes from a holomorphic atlas, if and only if $N_J = 0$.

*Proof.* The tensoriality is the classical computation of *Hermitian Geometry and Almost Complex Structures*: the terms with derivatives of the coefficient functions cancel because $J$ is a tensor and the bracket is tensorial in the appropriate sense; antisymmetry and the identity $N_J(X,JX)=0$ reduce to the Jacobi identity of the bracket and to $J^2=-1$. The integrability theorem is quoted.

## The Operators of an Almost Complex Structure

### The Partial Derivatives

**Definition.** The **partial derivatives** of the exterior derivative are the type components

$$
\partial = \pi^{n+1,m}\circ d \ : \ \Omega^{n,m}(M) \to \Omega^{n+1,m}(M), \qquad \bar\partial = \pi^{n,m+1}\circ d \ : \ \Omega^{n,m}(M) \to \Omega^{n,m+1}(M),
$$

where $\pi^{n+1,m}$ and $\pi^{n,m+1}$ are the projections onto the two types; they are the **$(1,0)$-part** and the **$(0,1)$-part** of $d$, and the remaining components of $d$ on a $(n,m)$-form are the projections onto the other bidegrees.

**Proposition.** The exterior derivative decomposes as

$$
\boxed{\;d = \partial + \bar\partial \quad \text{on the complexified forms}\;},
$$

that is, $d$ preserves the bidegree in the sense $d\,\Omega^{n,m}\subseteq\Omega^{n+1,m}\oplus\Omega^{n,m+1}$, if and only if the almost complex structure is integrable, $N_J = 0$.

*Proof.* The type of $d\omega$ is determined by the Leibniz rule and the fact that $d$ of a function is a $(1,0)$-form plus a $(0,1)$-form; the failure of $d$ to preserve the bidegree is measured by the $(0,2)$- and $(2,0)$-components of $d$ of the $(1,0)$- and $(0,1)$-forms, and these components are precisely the Nijenhuis tensor. The identification is the theorem of Newlander and Nijenhuis in its operator form, quoted from *Hermitian Geometry and Almost Complex Structures*; for an integrable structure the Dolbeault complex is the standard complex of a complex manifold.

### The Dolbeault Double Complex

**Theorem.** Suppose $J$ is integrable, so $d = \partial + \bar\partial$. Then

$$
\boxed{\;\partial^2 = 0, \qquad \bar\partial^2 = 0, \qquad \partial\bar\partial + \bar\partial\partial = 0\;},
$$

so the forms carry a **double complex**: for each $m$ the operators $\bar\partial$ make the rows $\Omega^{\bullet,m}$ into cochain complexes, for each $n$ the operators $\partial$ make the columns $\Omega^{n,\bullet}$ into cochain complexes, and the two commute with the sign, giving the anticommutation.

*Proof.* The identity $d^2 = 0$ and the bidegree decomposition $d = \partial+\bar\partial$ give, by separating the bidegrees of $d^2 = \partial^2 + (\partial\bar\partial+\bar\partial\partial) + \bar\partial^2$, the three displays: the $(p+2,q)$-part of $d^2$ is $\partial^2$, the $(n+1,m+1)$-part is $\partial\bar\partial+\bar\partial\partial$, and the $(n,m+2)$-part is $\bar\partial^2$. Since $d^2=0$, each homogeneous part vanishes.

**Definition.** The **Dolbeault cohomology** of an integrable almost complex structure is

$$
H^{n,m}_{\bar\partial}(M) = \frac{\ker(\bar\partial : \Omega^{n,m} \to \Omega^{n,m+1})}{\bar\partial\,\Omega^{n,m-1}} .
$$

**Theorem ($\bar\partial$-Poincaré lemma).** On a polydisc in $\mathbb{C}^n$, a $\bar\partial$-closed form is locally $\bar\partial$-exact: for every $(n,m)$ with $m \geq 1$ there is an operator $K$ with $\bar\partial K + K\bar\partial = \mathrm{id}$ on the $(n,m)$-forms, obtained by integrating the contraction with the radial $(0,1)$-field along the complex lines. Consequently $H^{n,m}_{\bar\partial}(\mathbb{C}^n) = 0$ for $m \geq 1$, and the Dolbeault cohomology of a complex manifold is the local-global obstruction, exactly as the de Rham cohomology is for the exterior derivative.

*Proof.* The operator $K$ is the complex analogue of the homotopy operator of *The Exterior Derivative*: the radial vector field of the polydisc is replaced by its $(0,1)$-component, and the fundamental theorem of calculus along the complex lines through the origin gives the identity; the argument is the Poincaré lemma applied to the $\bar\partial$-complex. The identifications $H^{n,m}_{\bar\partial} \cong H^{n,m}_{\bar\partial}$ with the sheaf cohomology of the holomorphic forms are the Dolbeault theorem, developed in *Sheaves and the de Rham Complex*.

## The Hermitian Structure

### The Metric of the Involution

**Definition.** A **Hermitian structure** on an almost complex manifold $(M,J)$ is a Riemannian metric $g$ with $g(JX,JY)=g(X,Y)$; the triple $(M,J,g)$ is a **Hermitian manifold**. Equivalently, $J$ is $g$-skew, $g(JX,Y)=-g(X,JY)$, and the **fundamental form** is $\omega(X,Y)=g(JX,Y)$.

**Proposition.** The Hermitian structure is the pair of the involution $J$ with the invariant metric; the metric is the fixed point of the involution $g\mapsto J^*g$ acting on the Riemannian metrics, and the average $\tfrac12(g+J^*g)$ of any metric is the invariant metric in its conformal or linear class. The fundamental form is a real nondegenerate $(1,1)$-form, and it is closed exactly when the Hermitian manifold is Kähler; the type of $\omega$, the closedness condition and the comparison of the Chern and Levi-Civita connections are those of *Hermitian Metrics and the Levi-Civita Connection*.

*Proof.* The equation $g(JX,JY)=g(X,Y)$ is the invariance of $g$ under $J$, and the averaging of a metric is positive definite and invariant; the properties of $\omega$ and the Kähler condition are the results of the cited article.

### The Hermitian Structure as an Involution Layer

**Remark.** The pair $(J,g)$ is an **involution on the data of the manifold**: $J$ is an involution of the tangent bundle with $J^2=-1$, the metric is the fixed datum of the involution it generates on the metrics, and the constructions of the group — the conjugation on the fibres of a Hermitian bundle, the metric as the conjugate-linear isomorphism $\bar E\to E^*$, the self-adjointness of a metric connection, the codifferential with respect to a Hermitian metric — are all the same operation read at the level of the elements. The Hermitian structure is the source of the involution that the group records, and the operators $\partial$ and $\bar\partial$, the type decomposition and the Dolbeault complex are its operator form; the analytic refinement of the last of these, in which the Hermitian metric enters the adjoint of $\bar\partial$ and the Laplace operator splits, is *Hermitian Metrics and the Codifferential*, the last entry of the group, and *The L2 Adjoint of a Differential Operator*.

## Summary

An almost complex structure is an involution $J$ of the tangent bundle with $J^2=-\mathrm{id}$; it splits the complexified tangent and cotangent bundles, and hence the complexified forms, into types $(n,m)$. The Nijenhuis tensor is its integrability obstruction; the theorem of Newlander and Nijenhuis says that $J$ is integrable exactly when $N_J=0$. The exterior derivative of an integrable structure splits into the type components $d=\partial+\bar\partial$, the failure of the split being exactly the Nijenhuis tensor; from $d^2=0$ come $\partial^2=\bar\partial^2=0$ and $\partial\bar\partial+\bar\partial\partial=0$, so the forms form the Dolbeault double complex, with its Dolbeault cohomology and its local exactness on the polydiscs.

A Hermitian structure is a metric invariant under the involution, equivalently a fixed point of the induced involution on the metrics; its fundamental form is a real nondegenerate $(1,1)$-form, closed exactly in the Kähler case. The involution and its invariant metric are the source of the whole involution layer of the group: the conjugate bundle, the metric as a conjugate-linear isomorphism, the self-adjointness of a metric connection and the Hermitian codifferential are the same operation at the level of the elements, and the operators $\partial$ and $\bar\partial$ are its operator form. The heavy analysis of the Hermitian Laplacian, in which the metric enters the adjoint of $\bar\partial$, is *Hermitian Metrics and the Codifferential* and *The L2 Adjoint of a Differential Operator*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J$, $J^2=-\mathrm{id}$ | Almost complex structure; the involution of the tangent bundle |
| $T^{1,0}M$, $T^{0,1}M$ | The $\pm i$ eigenbundles; $T_{\mathbb{C}}M=T^{1,0}\oplus T^{0,1}$ |
| $\Omega^{n,m}(M)$, $\Lambda^{n,m}M$ | Forms of type $(n,m)$ and the bundle they section |
| $N_J(X,Y)=[JX,JY]-J[X,JY]-J[JX,Y]-[X,Y]$ | Nijenhuis tensor; a section of $\Lambda^2T^*M\otimes TM$ |
| $N_J=0 \Leftrightarrow$ integrable | Newlander–Nijenhuis theorem |
| $\partial$, $\bar\partial$ | Type components of $d$; $\partial\Omega^{n,m}\subset\Omega^{n+1,m}$, $\bar\partial\Omega^{n,m}\subset\Omega^{n,m+1}$ |
| $d=\partial+\bar\partial$ | Equivalent to integrability |
| $\partial^2=\bar\partial^2=0$, $\partial\bar\partial+\bar\partial\partial=0$ | Dolbeault double complex |
| $H^{n,m}_{\bar\partial}(M)$ | Dolbeault cohomology; quotient of the $\bar\partial$-closed forms |
| $\bar\partial K+K\bar\partial=\mathrm{id}$ | $\bar\partial$-Poincaré lemma; local exactness on a polydisc |
| $g(JX,JY)=g(X,Y)$ | Hermitian structure; $J$ is a $g$-isometry, $J^*=-J$ |
| $\omega(X,Y)=g(JX,Y)$ | Fundamental form; closed iff Kähler |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, vol. II (Interscience, 1969), for the almost complex structure, the Nijenhuis tensor, the integrability and the type decomposition.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the operators $\partial,\bar\partial$, the double complex and the Dolbeault cohomology.
- Shiing-Shen Chern, *Complex Manifolds Without Potential Theory* (Springer, 2nd ed. 1979), for the type decomposition, the operators and the integrability.
- August Newlander and Louis Nijenhuis, "Complex analytic coordinates in almost complex manifolds", *Annals of Mathematics* 65 (1957), 391–404, for the integrability theorem.
- Werner Ballmann, *Lectures on Kähler Manifolds* (European Mathematical Society, 2006), for the Hermitian structure, the fundamental form and the Kähler condition.
