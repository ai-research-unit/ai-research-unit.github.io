# __Hermitian Vector Bundles and the Chern Connection__

## Introduction

A **Hermitian vector bundle** is a complex vector bundle whose fibres carry Hermitian inner products, varying smoothly with the base point. The metric is the datum that makes the fibres into Hilbert spaces of finite dimension; it is a conjugate-linear identification of the bundle with its dual, and it reduces the structure group of the bundle from $GL(k,\mathbb{C})$ to the unitary group $U(k)$. A **connection** on the bundle is compatible with the metric when it differentiates the inner product by the Leibniz rule; on a *holomorphic* bundle the metric and the holomorphic structure together single out exactly one such connection, the **Chern connection**.

The article develops the Hermitian bundles and their connections. It defines the Hermitian metric, reads it as the conjugate-linear isomorphism $\bar E \to E^*$ — the involution on the fibres that the group of this Part records — and identifies the unitary reductions of the structure group. It develops the metric-compatible connections, the affine space they form, and the naive adjointness interpretation that the operator group of this category uses. It then defines the holomorphic structure as a $\bar\partial$-operator, states the existence and uniqueness of the connection compatible with the metric and the holomorphic structure — the Chern connection — and computes its local form and its curvature.

The article assumes the complex vector bundles, the frames, the connections, the connection form, the curvature and the reduction of the structure group of *Fibre Bundles, Connections and Curvature*; the metric-compatible connection, the covariant derivative and the curvature as an operator of *The Covariant Derivative*, *Hermitian Connections and the Adjoint* and the rest of the operator group in this category. The complex structure of the base manifold, the almost complex structure, the type decomposition of the forms and the Dolbeault operator are *Hermitian Geometry and Almost Complex Structures* in Part IV, and are used here only through the $(0,1)$-part of the complexified cotangent bundle, with that forward reference named where the holomorphic structure is defined. The Chern classes of a Hermitian bundle are computed in the next article of this group, and the Chern connection of the tangent bundle of a Hermitian manifold is *Hermitian Manifolds and the Canonical Connection*, also in this Part. No physics is invoked.

## Hermitian Vector Bundles

### Hermitian Metrics and the Conjugate Bundle

Let $E \to M$ be a complex vector bundle of rank $k$ over a smooth manifold $M$, with fibres complex vector spaces. A **Hermitian metric** on $E$ is a smooth family $h = (h_x)$ of Hermitian inner products,

$$
h_x : E_x \times E_x \to \mathbb{C}, \qquad h_x(\lambda s + \mu s', t) = \bar\lambda\,h_x(s,t) + \bar\mu\,h_x(s',t),
$$

conjugate-linear in the first variable and complex-linear in the second, with $h_x(t,s) = \overline{h_x(s,t)}$ and $h_x(s,s) > 0$ for $s \neq 0$. In a local frame $e_1, \ldots, e_k$ the metric is the smooth positive-definite matrix function $H = (h_{ab})$ with $h_{ab} = h(e_a, e_b)$, and for sections $s = \sum_a s^a e_a$, $t = \sum_b t^b e_b$,

$$
h(s,t) = \sum_{a,b} \bar s^a\, h_{ab}\, t^b = \bar s^{\,T} H\, t .
$$

Under a change of frame $e' = eg$ the matrix transforms by $H' = g^* H g$, the transformation rule of a Hermitian form, and the bundles with a Hermitian metric are exactly the bundles whose structure group is reducible to the unitary group $U(k)$.

**Proposition (the metric as a conjugate-linear isomorphism).** The Hermitian metric induces a conjugate-linear bundle isomorphism

$$
\flat : \bar E \longrightarrow E^*, \qquad s \longmapsto h(s, \cdot),
$$

where $\bar E$ is the **conjugate bundle**, the bundle with the same underlying real vector bundle and the opposite complex structure, $\lambda \cdot_{\bar E} s = \bar\lambda s$. The isomorphism is conjugate-linear, its inverse is the metric dual, and in frames the matrix of $\flat$ is $H$, read from the frame of $\bar E$ to the dual frame of $E^*$.

*Proof.* For a fixed $s$, $h(s,\cdot)$ is complex-linear by the second-variable linearity of the metric; the map $s \mapsto h(s,\cdot)$ is conjugate-linear by the first-variable conjugate-linearity; and it is a fibrewise isomorphism because the metric is nondegenerate. This is the content of the **Riesz representation** for the finite-dimensional fibres, made smooth. The transformation rule $H' = g^*Hg$ is the invariance of the form under the two frame changes.

**Remark.** The isomorphism $\flat : \bar E \to E^*$ is the **involution** that this group of Part III records: it is the antilinear structure on the bundle, the bundle-level analogue of the conjugation of a complex vector space, and every construction below is invariant under the induced operation on the frames. Passing to the adjoint of a linear map, $A \mapsto A^* = \flat^{-1}\circ A^*\circ\flat$, is the operation that the operator group of this Part uses, and it is the same operation as the metric adjoint of *Hermitian Connections and the Adjoint*.

### The Unitary Frame Bundle

**Proposition.** The Hermitian metrics on $E$ are in bijective correspondence with the reductions of the structure group of $E$ from $GL(k,\mathbb{C})$ to $U(k)$, that is, with the subbundles of the frame bundle whose structure group is the unitary group.

*Proof.* A reduction to $U(k)$ is an atlas of frames whose transition functions take values in $U(k)$; in such a frame the matrix of $h$ is the identity, and two frames of the reduction are related by a unitary matrix, so the metric is well defined. Conversely, given $h$, the Gram–Schmidt process applied to any frame produces a local $h$-orthonormal frame, and the transition functions between two such frames are unitary because both are orthonormal for the same metric. The two constructions are inverse.

## Metric-Compatible Connections

### The Condition and the Affine Space

Let $\nabla$ be a connection on the complex bundle $E$, with connection form $\omega$ in a frame. The connection is **metric-compatible** with $h$ if

$$
d\,h(s,t) = h(\nabla s, t) + h(s, \nabla t)
$$

for all sections $s,t$, equivalently $X\,h(s,t) = h(\nabla_Xs,t) + h(s,\nabla_Xt)$ for all vector fields $X$; this is the condition of *The Covariant Derivative* and *Hermitian Connections and the Adjoint*, rewritten for a Hermitian rather than a real metric.

**Proposition.** In a frame the metric-compatibility condition reads

$$
dH = \omega^{*}H + H\,\omega, \qquad \omega^* = \bar\omega^{\,T},
$$

where $\omega^*$ is the conjugate transpose of the matrix of $1$-forms. The metric-compatible connections on $E$ form an affine space modelled on the sections of $T^*M \otimes \mathfrak{u}(E,h)$, the $h$-anti-Hermitian endomorphism-valued $1$-forms:

$$
\omega' = \omega + \theta, \qquad \theta^* = -\theta .
$$

*Proof.* Differentiating $h(s,t) = \bar s^T H t$ and substituting $\nabla = d+\omega$ gives $dh(s,t) = \overline{(ds+\omega s)}^T H t + \bar s^T H(dt + \omega t)$, and comparing with $h(\nabla s,t)+h(s,\nabla t)$ the terms $ds, dt$ cancel and leave $dH = \omega^*H + H\omega$. If $\omega'$ is another metric-compatible form, then $\theta = \omega'-\omega$ satisfies $\theta^*H + H\theta = 0$, that is, $H^{-1}\theta^* H = -\theta$, which is the anti-Hermitian condition for the $\theta$ read through the metric; and every such $\theta$ preserves the equation.

### The Adjoint Interpretation

**Remark.** Metric compatibility is the **self-adjointness** of the connection with respect to the fibrewise inner product: reading $h$ as the conjugate-linear isomorphism $\flat:\bar E\to E^*$, the condition $d\,h(s,t) = h(\nabla s,t)+h(s,\nabla t)$ says that the connection on $\bar E$ induced by the metric is the dual (transpose) of $\nabla$ with a sign, so $\nabla$ is its own adjoint up to the metric. The precise statement, the adjoint connection $\nabla^*$ on the dual bundle, the self-adjointness of the connection Laplacian and the computation of the adjoint of $\nabla_X$ as $-\operatorname{div}\nabla_X$ are *Hermitian Connections and the Adjoint* in this group and *The L2 Adjoint of a Differential Operator* in this Part; what the present article records is that the metric-compatibility condition is exactly the condition for the adjoint connection to be the conjugate connection.

## The Chern Connection

### The Holomorphic Structure and the Dolbeault Operator

Suppose now that the base $M$ carries an almost complex structure, so that the complexified cotangent bundle splits and the forms acquire a **type decomposition**; the almost complex structure, its integrability and the type decomposition of the forms are *Hermitian Geometry and Almost Complex Structures* in Part IV, and the notation of the $(p,q)$-forms is used here with that reference.

**Definition.** A **holomorphic structure** on a complex vector bundle $E$ over an almost complex manifold $(M,J)$ is a first-order differential operator

$$
\bar\partial_E : \Gamma(E) \longrightarrow \Omega^{0,1}(M;E)
$$

satisfying the Leibniz rule $\bar\partial_E(fs) = (\bar\partial f)\otimes s + f\,\bar\partial_E s$ over the complex-valued functions, and the integrability condition $\bar\partial_E^2 = 0$. A frame in which $\bar\partial_E$ is the componentwise $\bar\partial$ is a **holomorphic frame**; the transition functions of a holomorphic frame are holomorphic, and a vector bundle with a holomorphic structure is a **holomorphic vector bundle**.

The operator $\bar\partial_E$ is the $(0,1)$-part of a connection when the base is complex; the integrability $\bar\partial_E^2 = 0$ is the Newlander–Nijenhuis condition for the bundle, and the pair $(E, \bar\partial_E)$ is the bundle version of the complex structure of the base, as in *Hermitian Geometry and Almost Complex Structures*.

### Existence and Uniqueness

**Theorem (the Chern connection).** Let $E$ be a holomorphic vector bundle with a Hermitian metric $h$. Then there is exactly one connection $\nabla$ on $E$ that is metric-compatible and has $(0,1)$-part equal to the holomorphic structure,

$$
\nabla^{0,1} = \bar\partial_E .
$$

It is the **Chern connection**, also called the metric connection of the holomorphic bundle.

*Proof.* The two conditions decompose by type. Metric compatibility is the equation $dH = \omega^*H+H\omega$ of the previous section, whose $(1,0)$- and $(0,1)$-parts are conjugate and equivalent, $\partial H = \omega^{1,0*}H + H\omega^{1,0}$; the condition $\nabla^{0,1}=\bar\partial_E$ fixes the $(0,1)$-part of $\omega$ to be that of the holomorphic frame, namely zero in a holomorphic frame, so in a holomorphic frame the equation reduces to

$$
\partial H = \omega^{1,0*}H + H\,\omega^{1,0},
$$

which, with the anti-Hermitian condition and the reality of the metric, has the unique solution $\omega^{1,0} = H^{-1}\partial H$. Hence the connection form is determined in every holomorphic frame, and the local determinations patch because the transition functions are holomorphic: the operators they define agree on the overlaps. Existence is the formula; uniqueness is the determination.

### The Local Form

**Corollary.** In a holomorphic frame the Chern connection has the connection form

$$
\omega = H^{-1}\partial H
$$

of type $(1,0)$, that is, $\nabla = \partial + \bar\partial + H^{-1}\partial H$ read on the components of a section in the holomorphic frame; it is the unique solution of the metric-compatibility equation with vanishing $(0,1)$-part, and it therefore satisfies $dH = \omega^*H + H\omega$ with this $\omega$.

*Proof.* The $(0,1)$-part of the connection vanishes in a holomorphic frame, so $\omega = \omega^{1,0}$; the metric-compatibility equation $dH = \omega^*H+H\omega$ then has the unique solution $\omega = H^{-1}\partial H$, as the existence-and-uniqueness theorem shows.

### The Curvature

**Theorem.** The curvature of the Chern connection is

$$
\Theta = d\omega + \omega\wedge\omega = \bar\partial\bigl(H^{-1}\partial H\bigr),
$$

it has no component of type $(0,2)$, and it is of type $(1,1)$ and $h$-skew-Hermitian,

$$
\Theta = \Theta^{1,1}, \qquad \Theta^* = -\Theta .
$$

*Proof.* The $(0,2)$-part of $d\omega+\omega\wedge\omega$ is $\bar\partial\omega^{0,1}+\omega^{0,1}\wedge\omega^{0,1}$, and in a holomorphic frame $\omega^{0,1}=0$, so only $\bar\partial(H^{-1}\partial H)$ survives, which is of type $(1,1)$ because it is $\bar\partial$ of a $(1,0)$-form. For the skew-Hermitian property, differentiate the metric-compatibility equation $dH = \omega^*H+H\omega$ and use the definition of the curvature to obtain $\Theta^*H + H\Theta = 0$, which is the anti-Hermitian condition; the details are the standard computation of the curvature of a metric connection, as in *Fibre Bundles, Connections and Curvature*.

**Corollary.** On a holomorphic line bundle, the curvature is $\Theta = \bar\partial\partial\log h = -\partial\bar\partial\log h$ with $h$ the metric in a holomorphic frame; the form $\frac{i}{2\pi}\Theta$ is real and closed, so it defines a real cohomology class, the first Chern class of the Hermitian line bundle, and the computation of the Chern classes from this curvature is the next article of the group.

**Example.** Let $M = \mathbb{C}$ with the standard complex structure and let $E$ be the trivial line bundle with the metric $h(z) = e^{-\lvert z\rvert^2}$. In the holomorphic frame the Chern connection form is $\omega = h^{-1}\partial h = -\bar z\,dz$, the curvature is $\Theta = \bar\partial(-\bar z\,dz) = dz\wedge d\bar z$, and the first Chern form is $\frac{i}{2\pi}dz\wedge d\bar z$, the area form of the plane carried by the bundle metric; the curvature measures the failure of the metric to be the constant one, and it is the local model of the Fubini–Study connection.

## Summary

A Hermitian metric on a complex vector bundle is a smooth family of inner products, locally a positive-definite Hermitian matrix $H$ transforming by $H'=g^*Hg$; it is equivalent to a reduction of the structure group to $U(k)$, and it is a conjugate-linear isomorphism $\flat:\bar E\to E^*$, the involution that this group of the Part records. A connection is metric-compatible when $d\,h(s,t)=h(\nabla s,t)+h(s,\nabla t)$, equivalently $dH=\omega^*H+H\omega$; the metric-compatible connections form an affine space modelled on the $h$-anti-Hermitian endomorphism-valued $1$-forms, and the condition is the self-adjointness of the connection with respect to the fibrewise metric.

A holomorphic structure is a $\bar\partial$-operator with $\bar\partial_E^2=0$, the integrability condition; a holomorphic frame is one in which it is the componentwise $\bar\partial$. On a holomorphic Hermitian bundle there is a unique connection compatible with both the metric and the holomorphic structure, the Chern connection; in a holomorphic frame its connection form is $\omega=H^{-1}\partial H$, of type $(1,0)$, and its curvature is $\Theta=\bar\partial(H^{-1}\partial H)$, of type $(1,1)$ and skew-Hermitian. On a line bundle $\Theta=\bar\partial\partial\log h$, the local model of the first Chern form, and the general Chern forms of the Hermitian bundle are the subject of the next article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E, k$ | Complex vector bundle over $M$ and its complex rank |
| $h$, $h(s,t)=\bar s^{\,T}Ht$ | Hermitian metric, conjugate-linear in the first variable |
| $H = (h_{ab})$, $H' = g^*Hg$ | Metric matrix in a frame and its change of frame |
| $\bar E$ | Conjugate bundle; the opposite complex structure on the same real bundle |
| $\flat : \bar E \to E^*$, $s\mapsto h(s,\cdot)$ | Conjugate-linear isomorphism given by the metric |
| $U(k)$, unitary frame bundle | Reduction of the structure group by a Hermitian metric |
| $d\,h(s,t) = h(\nabla s,t)+h(s,\nabla t)$ | Metric compatibility |
| $dH = \omega^*H + H\omega$ | Metric compatibility in a frame; $\omega^*=\bar\omega^{\,T}$ |
| $\mathfrak{u}(E,h)$, $\theta^*=-\theta$ | The affine space of metric connections; anti-Hermitian difference |
| $\bar\partial_E$, $\bar\partial_E^2=0$ | Holomorphic structure and its integrability |
| $(p,q)$-forms, $\Omega^{0,1}(M;E)$ | Type decomposition; forward reference to Part IV |
| Chern connection | The unique $\nabla$ with $\nabla^{0,1}=\bar\partial_E$ and $\nabla$ metric-compatible |
| $\omega = H^{-1}\partial H$ | Chern connection form in a holomorphic frame; type $(1,0)$ |
| $\Theta = d\omega+\omega\wedge\omega = \bar\partial(H^{-1}\partial H)$ | Curvature of the Chern connection; type $(1,1)$, skew-Hermitian |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, vol. II (Interscience, 1969), for Hermitian metrics, holomorphic bundles and the Chern connection.
- Shiing-Shen Chern, *Complex Manifolds Without Potential Theory* (Springer, 2nd ed. 1979), for the connection and curvature forms of a holomorphic Hermitian bundle.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Chern connection, the curvature of a line bundle and the first Chern class.
- Jean-Pierre Demailly, *Complex Analytic and Differential Geometry* (OpenContent, 2012), for the Chern connection, the curvature and the positivity of Hermitian bundles.
- Werner Ballmann, *Lectures on Kähler Manifolds* (European Mathematical Society, 2006), for the Chern connection as the canonical connection of a Hermitian manifold, cited for the forward reference.
