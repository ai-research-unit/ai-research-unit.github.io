# __Hermitian Metrics and the Levi-Civita Connection__

## Introduction

A Riemannian metric makes a smooth manifold into a space on which lengths and angles are defined, and its fundamental theorem produces from it a single connection, the **Levi-Civita connection**, that is compatible with the metric and has no torsion. When the manifold also carries an **involution** of its tangent spaces — an almost complex structure $J$ with $J^2=-\mathrm{id}$ — a metric is **Hermitian** for it when $J$ is an isometry, and the two data interact: the Levi-Civita connection need not preserve $J$, and it does exactly when the metric form is closed, the **Kähler** case.

The article develops the metric and the connection as the involution layer of the group. It recalls the Riemannian metric and the fundamental theorem in the form fixed by the operator group, then develops the Hermitian condition $g(JX,JY)=g(X,Y)$, its equivalent skew-adjointness of $J$, and the **fundamental form** $\omega(X,Y)=g(JX,Y)$. It proves that a metric-compatible connection preserves $J$ exactly when it preserves the fundamental form, characterises the Kähler condition by four equivalent statements — the closedness of $\omega$, the parallelism of $J$ under the Levi-Civita connection, the torsion-freeness of the Chern connection, and the coincidence of the two connections — and identifies the difference between the Levi-Civita and the Chern connections as the tensor $\nabla^{LC}J$.

The article assumes the Riemannian metrics, the musical isomorphisms, the volume form and the Hodge star of the operator group and of Part IV; the metric-compatible connections, the torsion, the Koszul formula and the fundamental theorem of *The Covariant Derivative* in this category, where the theorem is proved; the almost complex structure, the type decomposition, the Nijenhuis tensor and the Hermitian metrics as geometric objects of *Hermitian Geometry and Almost Complex Structures* in Part IV; and the Chern connection of a holomorphic Hermitian bundle of *Hermitian Vector Bundles and the Chern Connection*, the previous entry of this group. The Kähler manifold — the metric, the symplectic form, the curvature and the Hodge theory of the Kähler case — is *Kähler Geometry* and *Symplectic Geometry* in Part IV; the metric geometry of geodesics and curvature is *Riemannian Geometry* there. No physics is invoked.

## Riemannian Metrics

**Definition.** A **Riemannian metric** on a smooth manifold $M$ is a smooth family of inner products, that is, a smooth section $g$ of $S^2T^*M$ that is positive definite on each fibre: $g(X,Y)=g(Y,X)$ and $g(X,X)>0$ for $X\neq0$.

The metric provides the musical isomorphisms $\flat : TM \to T^*M$, $X \mapsto g(X,\cdot)$ and its inverse $\sharp$, the metric volume form $\mathrm{vol}_g$ in the chosen orientation, the Hodge star $\star$, the codifferential and the Laplace–Beltrami operator of the operator group, and the length of a curve. All of these are the metric **used as a tool**; the metric as an object — its curvature, its geodesics, its isometries — is *Riemannian Geometry* and *Curvature and Geodesics* in Part IV, and is not developed here.

**Example.** On $\mathbb{R}^n$ the **Euclidean metric** has $g = \sum_i dx^i\otimes dx^i$ in the standard coordinates; on a submanifold of $\mathbb{R}^n$ the **induced metric** is the restriction of the Euclidean metric to the tangent spaces; on a Lie group the **bi-invariant metrics** come from an invariant inner product on the Lie algebra, as in *Lie Groups* in this Part. The flat torus and the round sphere are the two basic closed examples.

## The Fundamental Theorem

**Theorem (fundamental theorem of Riemannian geometry).** On a Riemannian manifold $(M,g)$ there is exactly one connection $\nabla$ on the tangent bundle that is metric-compatible and torsion-free, the **Levi-Civita connection**. It is determined by the Koszul formula

$$
2g(\nabla_XY, Z) = X\,g(Y,Z) + Y\,g(X,Z) - Z\,g(X,Y) - g(X,[Y,Z]) - g(Y,[X,Z]) + g(Z,[X,Y]),
$$

and in a coordinate chart its components are the Christoffel symbols

$$
\Gamma^i_{jk} = \tfrac12 \sum_l g^{il}\bigl(\partial_j g_{kl} + \partial_k g_{jl} - \partial_l g_{jk}\bigr).
$$

*Proof.* This is the theorem of *The Covariant Derivative* in this category, where the existence, the uniqueness and the Koszul formula are proved; the coordinate formula is the same computation written in a chart. The article cites the theorem and uses it.

**Proposition (properties of the Levi-Civita connection).** Its parallel transport preserves the metric, hence the length and the angle; its geodesics are the autoparallel curves $\nabla_{\dot\gamma}\dot\gamma=0$ of the metric; its curvature satisfies the symmetries of the Riemann curvature tensor; and it is the connection used throughout the operator group. The geodesics, the exponential map and the curvature as geometry are Part IV's.

## Hermitian Metrics and the Involution

### The Hermitian Condition

**Definition.** An **almost complex structure** on $M$ is a bundle endomorphism $J : TM \to TM$ with $J^2 = -\mathrm{id}_{TM}$; it is an involution of the tangent spaces whose square is minus the identity, and the pair $(M,J)$ is an almost complex manifold. A Riemannian metric $g$ is **Hermitian** for $J$ if $J$ is an isometry of each tangent space:

$$
g(JX, JY) = g(X, Y) \qquad \text{for all } X, Y \in \mathrm{X}(M).
$$

The triple $(M, J, g)$ is a **Hermitian manifold**; the almost complex structures, their integrability by the Newlander–Nijenhuis theorem and the Nijenhuis tensor are *Hermitian Geometry and Almost Complex Structures* in Part IV, where the geometry of the pair is developed.

**Proposition.** The Hermitian condition is equivalent to the skew-adjointness of $J$ with respect to $g$:

$$
g(JX, Y) = -g(X, JY), \qquad \text{that is,} \qquad J^* = -J \ \text{for } g .
$$

In particular $g(JX,X) = 0$ for every $X$, so no tangent vector is $g$-orthogonal to nothing; $J$ is a $g$-antisymmetric endomorphism, and $g$ makes the complexified tangent bundle $T_{\mathbb{C}}M$ a Hermitian space with respect to the $\mathbb{C}$-bilinear extension of $g$ and the conjugation.

*Proof.* If $g(JX,JY)=g(X,Y)$, then $g(JX,Y) = g(JX,-J(JY)) = -g(JX,J(JY)) = -g(X,JY)$, using the invariance with the two arguments $X$ and $JY$. Conversely, $g(JX,Y)=-g(X,JY)$ gives $g(JX,JY) = -g(X,J(JY)) = g(X,Y)$ by $J^2=-1$. Setting $Y=X$ in the first form gives $g(JX,X)=-g(X,JX)=-g(JX,X)$, hence $g(JX,X)=0$.

### The Fundamental Form

**Definition.** The **fundamental form** (or Kähler form) of a Hermitian manifold is the $2$-form

$$
\omega(X, Y) = g(JX, Y), \qquad X, Y \in \mathrm{X}(M).
$$

**Proposition.** The fundamental form is a real $2$-form; it is antisymmetric because $g$ is symmetric and $J$ is $g$-skew: $\omega(Y,X)=g(JY,X)=-g(X,JY)=-g(JX,Y)=-\omega(X,Y)$; it is nondegenerate, because $\omega(X,Y)=0$ for all $Y$ forces $JX=0$ and hence $X=0$; and it is of type $(1,1)$ for the complexified metric, $\omega(JX,JY)=\omega(X,Y)$.

*Proof.* The antisymmetry and the nondegeneracy are immediate from the definitions and the invertibility of $J$; the type statement is the invariance of $g$ and $J$. A nondegenerate $2$-form is a **symplectic form** when it is closed, and the closedness of $\omega$ is the Kähler condition of the next section; the symplectic form as an object is *Symplectic Geometry* in Part IV.

## The Levi-Civita Connection of a Hermitian Metric

### Metric Compatibility and the Involution

**Proposition.** Let $\nabla$ be a metric-compatible connection on the tangent bundle, $\nabla g = 0$. Then $\nabla$ preserves the fundamental form, $\nabla\omega=0$, if and only if it preserves the involution, $\nabla J = 0$; and a metric-compatible connection with $\nabla J = 0$ has $\nabla\omega = 0$ automatically, so the two conditions are the same condition on the connection.

*Proof.* Since $\omega(X,Y)=g(JX,Y)$ and $\nabla g=0$, differentiating gives $(\nabla_Z\omega)(X,Y) = g((\nabla_ZJ)X,Y)$, so $\nabla\omega=0$ is equivalent to $\nabla J=0$. Reading the two tensor fields as sections of the appropriate bundles, the Leibniz rule and the metric compatibility convert one into the other.

**Corollary.** A metric-compatible connection preserves the type decomposition of the complexified tangent bundle, $T_{\mathbb{C}}M = T^{1,0}M\oplus T^{0,1}M$ into the eigenbundles of $J$, if and only if $\nabla J = 0$; it then preserves the Dolbeault decomposition of the forms. The connection is therefore compatible with the almost complex structure exactly when the structure is parallel for it, and this is a strictly stronger condition than metric compatibility.

### The Kähler Condition and the Comparison of the Connections

The Levi-Civita connection is torsion-free but need not preserve $J$; the Chern connection of *Hermitian Vector Bundles and the Chern Connection* is metric-compatible and compatible with the holomorphic structure, but it has torsion in general and it need not preserve $J$. The precise relation between the two conditions is the subject of the following theorem, which is the bridge between this article and the Kähler geometry of Part IV.

**Theorem (the Kähler conditions).** Let $(M,J,g)$ be a Hermitian manifold, with $J$ integrable, and let $\nabla^{LC}$ be the Levi-Civita connection and $\nabla^{Ch}$ the Chern connection. The following are equivalent:

**(a)** the fundamental form is closed, $d\omega = 0$;

**(b)** $J$ is parallel for the Levi-Civita connection, $\nabla^{LC}J = 0$;

**(c)** the fundamental form is parallel, $\nabla^{LC}\omega = 0$;

**(d)** the Chern connection is torsion-free;

**(e)** the Chern connection equals the Levi-Civita connection, $\nabla^{Ch} = \nabla^{LC}$;

and when any of them holds, the manifold is a **Kähler manifold**.

*Proof.* The equivalence of (b) and (c) is the previous proposition applied to $\nabla^{LC}$, which is metric-compatible. The equivalence of (a) and (b) is the classical computation: for a torsion-free metric connection, $d\omega$ is the antisymmetrisation of $\nabla^{LC}\omega$, so $d\omega=0$ if and only if $\nabla^{LC}\omega=0$, and by the proposition this is $\nabla^{LC}J=0$. The Chern connection is metric-compatible by definition, so by the fundamental theorem it is torsion-free exactly when it equals the Levi-Civita connection; this is (d) $\Leftrightarrow$ (e). Finally, if $\nabla^{LC}J=0$ then $\nabla^{LC}$ is metric-compatible and has $(0,1)$-part $\bar\partial$, so it satisfies the two defining properties of the Chern connection and the two coincide by uniqueness; conversely, if $\nabla^{Ch}=\nabla^{LC}$ then the Levi-Civita connection preserves the holomorphic structure, hence $\nabla^{LC}J=0$, and the claim follows; the detailed computation of the torsion of the Chern connection is that of *Kähler Geometry* in Part IV. Each of the five statements therefore implies the others, and the Kähler condition is their common content.

**Corollary.** In the non-Kähler case the Levi-Civita and the Chern connections differ by a tensor field built from $\nabla^{LC}J$, and this tensor vanishes exactly in the Kähler case; the Levi-Civita connection is the torsion-free one and does not preserve the involution, the Chern connection preserves the metric and the holomorphic structure and does not have zero torsion, and neither condition implies the other outside the Kähler case.

*Proof.* The two connections are both metric-compatible, so their difference is an $\mathfrak{so}(TM,g)$-valued $1$-form; it vanishes exactly when the Levi-Civita connection has $\nabla^{LC}J=0$, by the theorem, and the difference is built from the covariant derivative of $J$ by the failure of $J$ to be parallel. The two normalisations are the standard ones.

## Examples

**Example (the flat case).** On $\mathbb{C}^n$ with the standard complex structure $J$ and the Euclidean metric, $J$ is parallel for the flat Levi-Civita connection, so the manifold is Kähler; the fundamental form is $\omega = \sum_j dx_j\wedge dy_j$, closed, and the Chern connection of the tangent bundle is the flat connection.

**Example (the round sphere).** On $S^2$ with its standard complex structure and the round metric, the fundamental form is the area form, which is closed because it is a top form; hence the round sphere is Kähler, and the Levi-Civita connection preserves the complex structure.

**Example (a non-Kähler Hermitian manifold).** On the product of the three-sphere with the circle, and on the Hopf surface, there are Hermitian metrics whose fundamental form is not closed; there the Levi-Civita connection does not preserve $J$, the Chern connection has torsion, and the two connections differ. The construction of such metrics and the Kähler/non-Kähler dichotomy are the subject of *Hermitian Geometry and Almost Complex Structures* and *Kähler Geometry* in Part IV.

**Example (the induced metric on a complex submanifold).** A complex submanifold of a Kähler manifold, with the induced metric, is Kähler; the fundamental form is the restriction of the ambient one; this is the Kähler-case instance of the induced-metric construction of the first section.

## Summary

A Riemannian metric is a smooth family of inner products; it supplies the musical isomorphisms, the volume form, the Hodge star and the codifferential, and the fundamental theorem produces the unique metric-compatible torsion-free connection, the Levi-Civita connection, determined by the Koszul formula and locally by the Christoffel symbols. A metric is Hermitian for an almost complex structure $J$ when $J$ is an isometry, equivalently when $J$ is $g$-skew-adjoint, and then the fundamental form $\omega(X,Y)=g(JX,Y)$ is a nondegenerate real $2$-form of type $(1,1)$.

For a metric-compatible connection, preserving the fundamental form, preserving the involution $J$ and preserving the type decomposition are one and the same condition, $\nabla J=0$. The Levi-Civita connection satisfies it exactly when the Hermitian manifold is Kähler, and the Kähler condition has the five equivalent forms: $d\omega=0$; $\nabla^{LC}J=0$; $\nabla^{LC}\omega=0$; the Chern connection is torsion-free; the two connections coincide. Outside the Kähler case the Levi-Civita connection is torsion-free but does not preserve $J$, the Chern connection preserves the metric and the holomorphic structure but has torsion, and they differ by a tensor built from $\nabla^{LC}J$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $g$, $g(X,X)>0$ | Riemannian metric, a smooth family of inner products |
| $\flat, \sharp$ | Musical isomorphisms $TM \leftrightarrow T^*M$ |
| $\mathrm{vol}_g$, $\star$, $\delta$ | Metric volume form, Hodge star, codifferential |
| Fundamental theorem, Koszul formula | The unique metric-compatible torsion-free connection |
| $\Gamma^i_{jk} = \tfrac12g^{il}(\partial_jg_{kl}+\partial_kg_{jl}-\partial_lg_{jk})$ | Christoffel symbols |
| $J$, $J^2=-\mathrm{id}$ | Almost complex structure; the involution of the tangent spaces |
| $g(JX,JY)=g(X,Y)$ | Hermitian condition; equivalently $g(JX,Y)=-g(X,JY)$, $J^*=-J$ |
| $(M,J,g)$ | Hermitian manifold |
| $\omega(X,Y)=g(JX,Y)$ | Fundamental form; nondegenerate, of type $(1,1)$ |
| $\nabla^{LC}$, $\nabla^{Ch}$ | Levi-Civita and Chern connections |
| $\nabla J = 0 \Leftrightarrow \nabla\omega = 0$ | Metric-compatible connection preserves the involution |
| $d\omega=0$, $\nabla^{LC}J=0$, $\nabla^{LC}\omega=0$ | Equivalent forms of the Kähler condition |
| $\nabla^{Ch}$ torsion-free, $\nabla^{Ch}=\nabla^{LC}$ | The remaining equivalent forms; Kähler |
| Non-Kähler | $\nabla^{LC}J \neq 0$; the two connections differ |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, vol. II (Interscience, 1969), for Hermitian metrics, the fundamental form, the Kähler condition and the comparison of the Hermitian and Levi-Civita connections.
- Werner Ballmann, *Lectures on Kähler Manifolds* (European Mathematical Society, 2006), for the equivalence of the Kähler conditions and the Chern connection.
- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed. (Springer, 2018), for the Riemannian metric, the fundamental theorem and the Koszul formula.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Hermitian metrics, the Kähler form and the complex geometry of the non-Kähler case.
- Sigmundur Gudmundsson, *An Introduction to Riemannian Geometry* (Lund, 2020), for the metric compatibility, the torsion and the Levi-Civita connection with the sign conventions used here.
