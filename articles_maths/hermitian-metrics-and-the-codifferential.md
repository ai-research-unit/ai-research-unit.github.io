# __Hermitian Metrics and the Codifferential__

## Introduction

On a Hermitian manifold the **codifferential** acquires a second reading: the exterior derivative splits by type as $d=\partial+\bar\partial$, and the codifferential — the formal adjoint of $d$ — splits with it as $\delta=\partial^*+\bar\partial^*$, into the formal adjoints of the two type components. The Hermitian metric is the datum that produces the Hodge star, hence $\delta$, hence the **Hodge Laplacian** $\Delta=d\delta+\delta d$ and the two **Dolbeault Laplacians** $\Delta_\partial$ and $\Delta_{\bar\partial}$ built from $\partial^*$ and $\bar\partial^*$. This is the last entry of the operator group, and the article closes the loop: the involution $J$ and its invariant metric act on the operators of the exterior algebra exactly as the metric of the previous group acted on the connections.

The article develops the Hermitian codifferential. It defines the real and the complex Hodge stars, the Hermitian pairing on the forms and the codifferential $\delta=-\star d\star$ of an even-dimensional manifold; it proves the adjointness of $d$ and $\delta$ in the Hermitian setting; it proves the **bidegree split** $\delta=\partial^*+\bar\partial^*$, with $\partial^*$ and $\bar\partial^*$ the formal adjoints of the type components; it defines the Dolbeault Laplacians, relates them to the Hodge Laplacian, and states the Kähler relation $\Delta=2\Delta_\partial=2\Delta_{\bar\partial}$ as a forward reference; and it reads the complex conjugation of the forms as the involution of the layer, commuting with $d$ and $\delta$.

The article assumes the exterior derivative, the Hodge star, the codifferential, the Laplace–de Rham operator and the Hodge theory of *Differential Forms and Stokes' Theorem*, *The Exterior Derivative* and *The Codifferential*, all in this category; the Hermitian metrics, the fundamental form and the Kähler conditions of *Hermitian Metrics and the Levi-Civita Connection*; the almost complex structure, the type decomposition, the operators $\partial,\bar\partial$ and the Dolbeault complex of *Hermitian Structures and the Almost Complex Structure*; the formal adjoint, the pairing and the Lagrange identity of *The Formal Adjoint of a Differential Operator*; and the global adjoint, the domain and the spectral theory of *The L2 Adjoint of a Differential Operator*, the previous entry of the group. The Hermitian Hodge decomposition and the Dolbeault cohomology, the Kähler identities and the Lefschetz decomposition are *Hermitian Metrics and the Hodge Theory* and *Kähler Geometry* in Part IV, and are named as forward references; the ellipticity and the Hodge theory of the de Rham complex are the operator group's. No physics is invoked.

## The Hodge Star of a Hermitian Metric

### The Real Star and the Complex Star

Let $(M,J,g)$ be a Hermitian manifold of complex dimension $m$, with real dimension $2m$, and let $\mathrm{vol}$ be the Riemannian volume form of $g$; the fundamental form satisfies $\omega^m = m!\,\mathrm{vol}$, a real $(m,m)$-form. The **Hodge star** $\star$ of the Riemannian metric is, on the real forms, the operator $\star : \Omega^k(M;\mathbb{R})\to\Omega^{2m-k}(M;\mathbb{R})$ characterised by $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle_{g}\,\mathrm{vol}$, and it is extended to the complex-valued and the complexified forms by $\mathbb{C}$-linearity.

**Proposition.** As a $\mathbb{C}$-linear operator on the complexified forms, the Hodge star respects the type decomposition by

$$
\star : \Omega^{p,q} \longrightarrow \Omega^{m-q,m-p}, \qquad \star(\alpha^{p,q}) \in \Omega^{m-q,m-p},
$$

and it satisfies $\star^2 = (-1)^{k(2m-k)}$ on $\Omega^k$ with $k=p+q$. The Hermitian metric enters through the volume form and through the fibrewise metric on the forms.

*Proof.* The metric pairing of two complexified forms, $\alpha\wedge\star\beta=g(\alpha,\beta)\mathrm{vol}$, is nonzero only when the bidegrees of $\alpha$ and $\beta$ are transposed, that is, it pairs $\Omega^{p,q}$ with $\Omega^{q,p}$ into $\mathbb{C}$: the Hermitian metric pairs a $(1,0)$-form with a $(0,1)$-form and vanishes on two $(1,0)$-forms, so the pairing of the forms of two bidegrees is nondegenerate exactly between the transposed bidegrees. Since $\mathrm{vol}$ has bidegree $(m,m)$, the identity forces the bidegree of $\star\beta$ to be the complement, $(m-q,m-p)$, when $\beta$ has bidegree $(p,q)$; and the identity $\star^2=(-1)^{k(2m-k)}$ is the real formula for the $2m$-dimensional manifold, extended $\mathbb{C}$-linearly.

**Definition.** The **Hermitian pairing** of two complex-valued forms is

$$
\langle\alpha,\beta\rangle_{L^2} = \int_M \langle\alpha,\beta\rangle_g\, \mathrm{vol} = \int_M \bar\alpha\wedge\star\beta,
$$

conjugate-linear in the first variable and complex-linear in the second, where the fibrewise Hermitian inner product $\langle\alpha,\beta\rangle_g$ on the cotangent spaces is the one induced by the metric; the identity with the star uses the complex conjugate $\bar\alpha$ and is the standard expression of the Hermitian inner product through the Hodge operator, since $g(\bar\alpha,\beta)$ is conjugate-linear in $\alpha$ and linear in $\beta$.

### The Codifferential of the Hermitian Metric

**Theorem.** On the Hermitian manifold, where the real dimension is even, $2m$, the **codifferential**

$$
\delta = (-1)^{2m(k+1)+1}\,\star\,d\,\star = -\,\star\,d\,\star \ : \ \Omega^k(M;\mathbb{C})\longrightarrow\Omega^{k-1}(M;\mathbb{C})
$$

is the formal adjoint of the exterior derivative for the Hermitian pairing,

$$
\langle d\alpha,\beta\rangle_{L^2} = \langle\alpha,\delta\beta\rangle_{L^2}, \qquad \alpha,\beta \ \text{compactly supported},
$$

and it is the same operator as the Riemannian codifferential of *The Codifferential*, its sign convention fixed by the even dimension.

*Proof.* The general formula $\delta=(-1)^{r(k+1)+1}\star d\star$ of the codifferential in real dimension $r$ becomes $\delta=-\star d\star$ when $r=2m$ is even, because $(-1)^{2m(k+1)+1}=(-1)^{\text{even}+1}=-1$. The adjointness is the integration by parts proved in *The Codifferential*, and the Hermitian pairing induces the same $L^2$ inner product as the Riemannian one on the complex-valued forms, so the adjoint operator is the same. The local formula $\delta\omega=-\sum_i\iota_{e_i}\nabla_{e_i}\omega$ of *The Codifferential* holds as well.

**Example.** On $\mathbb{C}$ with the Euclidean metric, $m=1$, $2m=2$, and $\delta = -\star d\star$ on the forms of the plane: on a function $f$, $\delta f=0$; on the $1$-form $\alpha = a\,dx + b\,dy$, $\delta\alpha = -(\partial_x a + \partial_y b)$, the negative divergence; on the $2$-form $h\,dx\wedge dy$, $\delta = 0$. The signs are those of the Euclidean Hodge theory.

## The Bidegree Split of the Codifferential

**Theorem.** On an integrable almost complex structure, with $d=\partial+\bar\partial$, the codifferential decomposes by type,

$$
\delta = \partial^* + \bar\partial^*, \qquad \partial^* : \Omega^{p,q}\to\Omega^{p-1,q}, \quad \bar\partial^* : \Omega^{p,q}\to\Omega^{p,q-1},
$$

where $\partial^*$ and $\bar\partial^*$ are the formal adjoints of the type components for the Hermitian pairing:

$$
\langle\partial\alpha,\beta\rangle_{L^2} = \langle\alpha,\partial^*\beta\rangle_{L^2}, \qquad \langle\bar\partial\alpha,\beta\rangle_{L^2} = \langle\alpha,\bar\partial^*\beta\rangle_{L^2}.
$$

Consequently $\delta$ is the sum of an operator lowering $p$ and an operator lowering $q$, and it preserves the total degree by lowering it by one.

*Proof.* The adjoint of a sum is the sum of the adjoints, so $d^*=\partial^*+\bar\partial^*$; and $d^*=\delta$. The bidegrees of $\partial^*$ and $\bar\partial^*$ are those of $\partial$ and $\bar\partial$ with the degree reversed, because the Hermitian pairing is nondegenerate on each bidegree $\Omega^{p,q}\times\Omega^{p,q}\to\mathbb{C}$ and vanishes across different bidegrees; hence $\partial^*$ lowers $p$ and $\bar\partial^*$ lowers $q$. The two adjoint identities are the definitions.

**Remark.** The two adjoints satisfy $\partial^{*2}=0$ and $\bar\partial^{*2}=0$ and anticommute, since they are the adjoints of operators with those properties; the pair $(\partial^*,\bar\partial^*)$ is the adjoint of the Dolbeault double complex, the mirror of $(\partial,\bar\partial)$, exactly as $\delta$ mirrors $d$.

## The Laplacians of a Hermitian Metric

### The Hodge and Dolbeault Laplacians

**Definition.** The **Hodge Laplacian** (Laplace–de Rham operator) and the **Dolbeault Laplacians** are

$$
\Delta = d\delta+\delta d, \qquad \Delta_\partial = \partial\partial^*+\partial^*\partial, \qquad \Delta_{\bar\partial} = \bar\partial\bar\partial^*+\bar\partial^*\bar\partial .
$$

**Theorem.** The four operators are formally self-adjoint, nonnegative on the compactly supported forms,

$$
\langle\Delta\alpha,\alpha\rangle_{L^2} = \lVert d\alpha\rVert_{L^2}^2 + \lVert\delta\alpha\rVert_{L^2}^2 \ge 0, \qquad \langle\Delta_{\bar\partial}\alpha,\alpha\rangle_{L^2} = \lVert\bar\partial\alpha\rVert_{L^2}^2 + \lVert\bar\partial^*\alpha\rVert_{L^2}^2 \ge 0,
$$

and they preserve the bidegree; $\Delta$ commutes with $d$ and $\delta$, and $\Delta_{\bar\partial}$ commutes with $\bar\partial$ and $\bar\partial^*$. Expanding $d=\partial+\bar\partial$ and $\delta=\partial^*+\bar\partial^*$ gives the decomposition

$$
\Delta = \Delta_\partial + \Delta_{\bar\partial} + \bigl(\partial\bar\partial^* + \bar\partial^*\partial\bigr) + \bigl(\bar\partial\partial^* + \partial^*\bar\partial\bigr),
$$

whose last two terms, the **cross terms**, vanish when the Hermitian metric is Kähler.

*Proof.* The self-adjointness and the nonnegativity are the adjointness of $d$ and $\delta$ and the identities $\langle\alpha,\partial^*\beta\rangle=\langle\partial\alpha,\beta\rangle$, applied as in the Riemannian case of *The Codifferential*; the preservation of the bidegree is the bidegree of the constituents. The expansion is the substitution and the collection of the terms by type. The vanishing of the cross terms on a Kähler manifold is the Kähler identity $\partial\bar\partial^*+\bar\partial^*\partial=0$, the content of *Kähler Geometry* in Part IV.

**Corollary (the Kähler case).** On a Kähler manifold the cross terms vanish and moreover $\Delta_\partial=\Delta_{\bar\partial}$, so

$$
\Delta = 2\Delta_\partial = 2\Delta_{\bar\partial},
$$

and a form is harmonic for $\Delta$ exactly when it is harmonic for $\Delta_{\bar\partial}$. The identities producing this coincidence, the Lefschetz decomposition and the Hodge–Riemann relations are *Kähler Geometry* and *Hermitian Metrics and the Hodge Theory* in Part IV, and are named as forward references; the present article supplies only the operators and the split.

**Corollary.** A form of type $(p,q)$ is harmonic for $\Delta_{\bar\partial}$ exactly when it is $\bar\partial$-closed and $\bar\partial^*$-closed; the space of such forms is the **harmonic representative** of its Dolbeault class. The finiteness of the space, the Hodge decomposition of the Dolbeault complex and the identification of the harmonic representatives with the Dolbeault cohomology require the ellipticity of $\Delta_{\bar\partial}$ and the analysis of the previous entry, and the resulting theorem is *Hermitian Metrics and the Hodge Theory* in Part IV.

*Proof.* The vanishing of $\Delta_{\bar\partial}\alpha = \bar\partial\bar\partial^*\alpha+\bar\partial^*\bar\partial\alpha$ paired with $\alpha$ gives $\lVert\bar\partial\alpha\rVert^2+\lVert\bar\partial^*\alpha\rVert^2=0$, hence the two closedness conditions, by the nonnegativity of the terms. The remaining assertions are the elliptic Hodge theory, deferred.

### The Involution on the Forms

**Proposition (the conjugation).** The complex conjugation of the complex-valued forms, $\alpha\mapsto\bar\alpha$, maps $\Omega^{p,q}$ to $\Omega^{q,p}$, commutes with the exterior derivative, $d\bar\alpha=\overline{d\alpha}$, and with the Hodge star, $\star\bar\alpha=\overline{\star\alpha}$; consequently it commutes with the codifferential, $\delta\bar\alpha=\overline{\delta\alpha}$, and exchanges the two types of the differential, $\overline{\partial\alpha}=\bar\partial\bar\alpha$ and $\overline{\bar\partial\alpha}=\partial\bar\alpha$.

*Proof.* The conjugation of the coefficients is well defined on the complexified forms, and it exchanges the $(1,0)$- and the $(0,1)$-parts, hence the bidegrees $(p,q)$ and $(q,p)$. The commutation with the real operator $d$ is immediate from the reality of the exterior derivative; the Hodge star of the Riemannian metric is a real operator, so it commutes with the conjugation; the codifferential is built from $d$ and $\star$, so it commutes too. The exchange of $\partial$ and $\bar\partial$ is the conjugate of the type decomposition.

**Remark.** The conjugation is the involution of the layer, and $\delta$ is the operator that the involution and the metric jointly produce; the fixed forms of the involution are the real forms, and the Hermitian pairing is the involution-compatible pairing of the complex forms. This closes the group: the almost complex structure $J$ gives the type decomposition and the operators $\partial$ and $\bar\partial$, the Hermitian metric gives the fundamental form, the Hodge star, the codifferential and the Laplacians, and the adjoints $\partial^*$ and $\bar\partial^*$ are the involution-side mirrors of the two type components, exactly as the metric connection of the previous group was the metric-side mirror of the connection.

## Summary

On a Hermitian manifold of complex dimension $m$ the Hodge star maps $\Omega^{p,q}$ to $\Omega^{m-q,m-p}$ and the codifferential of the even-dimensional manifold is $\delta=-\star d\star$, the formal adjoint of $d$ for the Hermitian pairing $\langle\alpha,\beta\rangle_{L^2}=\int\alpha\wedge\star\bar\beta$. The exterior derivative splits by type, $d=\partial+\bar\partial$, and the codifferential splits with it, $\delta=\partial^*+\bar\partial^*$, into the formal adjoints of the type components, with bidegrees $(p-1,q)$ and $(p,q-1)$; this is the mirror of the Dolbeault double complex.

The Hodge Laplacian $\Delta=d\delta+\delta d$ and the Dolbeault Laplacians $\Delta_\partial=\partial\partial^*+\partial^*\partial$ and $\Delta_{\bar\partial}=\bar\partial\bar\partial^*+\bar\partial^*\bar\partial$ are formally self-adjoint, nonnegative and bidegree-preserving; the expansion of $\Delta$ in terms of the two Dolbeault Laplacians carries two cross terms, which vanish exactly on a Kähler manifold, where then $\Delta=2\Delta_\partial=2\Delta_{\bar\partial}$. The complex conjugation of the forms is the involution of the layer: it exchanges the bidegrees $(p,q)$ and $(q,p)$ and commutes with $d$, $\star$ and $\delta$, and it exchanges $\partial$ with $\bar\partial$. The Hodge decomposition of the Dolbeault complex, the finiteness of the harmonic spaces and the Kähler identities that make the cross terms vanish are *Hermitian Metrics and the Hodge Theory* and *Kähler Geometry* in Part IV.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $m$, $2m$ | Complex and real dimensions of the Hermitian manifold |
| $\omega$, $\omega^m=m!\,\mathrm{vol}$ | Fundamental form and the volume form |
| $\star : \Omega^{p,q}\to\Omega^{m-q,m-p}$ | Hodge star; $\star^2=(-1)^{k(2m-k)}$ on $\Omega^k$ |
| $\langle\alpha,\beta\rangle_{L^2}=\int\alpha\wedge\star\bar\beta$ | Hermitian pairing on the complex-valued forms |
| $\delta=-\star d\star$ | Codifferential; the sign from the even dimension $2m$ |
| $\partial$, $\bar\partial$ | Type components of $d$; $\partial\Omega^{p,q}\subset\Omega^{p+1,q}$, $\bar\partial\Omega^{p,q}\subset\Omega^{p,q+1}$ |
| $\partial^*$, $\bar\partial^*$; $\delta=\partial^*+\bar\partial^*$ | Formal adjoints of $\partial,\bar\partial$; the bidegree split |
| $\Delta=d\delta+\delta d$ | Hodge Laplacian (Laplace–de Rham operator) |
| $\Delta_\partial$, $\Delta_{\bar\partial}$ | Dolbeault Laplacians; self-adjoint, nonnegative |
| Cross terms $\partial\bar\partial^*+\bar\partial^*\partial$, $\bar\partial\partial^*+\partial^*\bar\partial$ | Vanishing exactly in the Kähler case |
| $\Delta=2\Delta_\partial=2\Delta_{\bar\partial}$ | Kähler case; forward reference to Part IV |
| $\alpha\mapsto\bar\alpha$ | Conjugation; $\Omega^{p,q}\leftrightarrow\Omega^{q,p}$, commutes with $d,\star,\delta$ |

## Further Reading

- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Hodge star, the codifferential, the Dolbeault Laplacians and the Kähler identities.
- Raymond O. Wells, *Differential Analysis on Complex Manifolds* (Springer, 3rd ed. 2008), for the Hermitian Hodge theory and the Dolbeault complex.
- Werner Ballmann, *Lectures on Kähler Manifolds* (European Mathematical Society, 2006), for the Laplacians, the Kähler identities and the Hodge decomposition.
- Frank W. Warner, *Foundations of Differentiable Manifolds and Lie Groups* (Springer, 1983), for the Hodge star, the codifferential and the Laplace–de Rham operator.
- Jean-Pierre Demailly, *Complex Analytic and Differential Geometry* (OpenContent, 2012), for the Hermitian metric, the complex Laplacians and the Hodge theory of the Dolbeault complex.
