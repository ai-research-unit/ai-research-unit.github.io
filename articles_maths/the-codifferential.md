# __The Codifferential__

## Introduction

The **codifferential** $\delta$ is the operator that lowers the degree of a differential form by one and is the formal adjoint of the exterior derivative with respect to the $L^2$ inner product of a metric. It is the second operator of the Hodge theory of forms, and with $d$ it assembles the **Laplace–de Rham operator** $\Delta = d\delta + \delta d$, whose kernel — the harmonic forms — represents the de Rham cohomology.

The Hodge star, the codifferential $\delta = (-1)^{n(k+1)+1}\star d\star$, the Laplace–de Rham operator and the Hodge theorem are defined and used in *Differential Forms and Stokes' Theorem*; this article reads them as operators. It develops the codifferential through its local formula $\delta\omega = -\sum_i\iota_{e_i}\nabla_{e_i}\omega$, which exhibits it as minus the divergence and makes its order and symbol visible; it proves the adjointness $\int\langle d\alpha,\beta\rangle = \int\langle\alpha,\delta\beta\rangle$ by integration by parts; it develops the Laplace–de Rham operator, its self-adjointness and its nonnegativity, the Weitzenböck formula that expresses it through the covariant derivative and a curvature term, and its ellipticity; and it states the Hodge decomposition that the ellipticity yields. It closes with the relations of $\delta$ to the Cartan calculus.

The article assumes the differential forms, the wedge product, exterior derivative, the de Rham complex, integration, Stokes' theorem and the statement of the Hodge theorem of *Differential Forms and Stokes' Theorem*; the Hodge star and its properties of the same article; the exterior derivative as an operator, its symbol and the ellipticity of the de Rham complex of *The Exterior Derivative* in this category; and the covariant derivative and its curvature of *The Covariant Derivative*. The $L^2$ realisation, the domain and the boundary conditions are *The L2 Adjoint of a Differential Operator*; the metric structure of the manifold as an object is Part IV's; the Hermitian refinement of the codifferential is *Hermitian Metrics and the Codifferential*, the last entry of this group. The article does not redefine the Hodge star or reprove the Hodge theorem. No physics is invoked.

## The Codifferential as an Operator

### Definition and Local Formula

Let $(M,g)$ be an oriented Riemannian manifold of dimension $n$, with the metric volume form $\mathrm{vol}_g$ and the Hodge star $\star : \Omega^k(M) \to \Omega^{n-k}(M)$ characterised by $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle_g\,\mathrm{vol}_g$ for the metric on forms induced by $g$. The star satisfies $\star\star = (-1)^{k(n-k)}$ on $\Omega^k(M)$.

**Definition.** The **codifferential** is the operator

$$
\delta = (-1)^{n(k+1)+1}\,\star\, d\, \star \ : \ \Omega^k(M) \longrightarrow \Omega^{k-1}(M),
$$

with the sign convention fixed by the requirement that $\delta$ be the formal adjoint of $d$, the convention of *Differential Forms and Stokes' Theorem*.

**Proposition.** The codifferential is a first-order differential operator; its value on forms is

$$
\delta\omega = -\sum_{i=1}^{n}\iota_{e_i}\nabla_{e_i}\omega
$$

over a local orthonormal frame $e_1, \ldots, e_n$, the covariant derivative $\nabla$ being the Levi–Civita connection extended to the forms; in particular for a $1$-form $\alpha$,

$$
\delta\alpha = -\operatorname{div}\alpha^\sharp,
$$

minus the divergence of the metric dual field. Its principal symbol is $\sigma_1(\delta)(x,\xi) = -\iota_{\xi^\flat}$, minus the contraction with the metric dual of $\xi$.

*Proof.* The Hodge star is a pointwise algebraic operator and the exterior derivative is first order, so the composition is first order; the local formula is the standard identity obtained by expanding the star in an orthonormal frame, and it is checked on a $1$-form by comparing with $\star d\star\alpha$ and using $\star\star=\pm1$ and the sign of the top-degree formula. For the symbol, the star is zeroth order, so $\sigma_1(\delta)(\xi)$ is the composition of the symbol of $d$ with the star; on the exterior algebra the star intertwines the multiplication by $\xi$ with the contraction by $\xi^\flat$ up to the sign $(-1)^{k(n-k)}$, which is the displayed $-\iota_{\xi^\flat}$.

**Corollary.** $\delta^2 = 0$, so the codifferential is a coboundary of the **dual complex**

$$
0 \longrightarrow \Omega^n(M) \xrightarrow{\ \delta\ } \Omega^{n-1}(M) \xrightarrow{\ \delta\ } \cdots \xrightarrow{\ \delta\ } \Omega^0(M) \longrightarrow 0,
$$

and it is a first-order operator of the same order as $d$, not a zeroth-order correction.

*Proof.* The star is invertible and $d^2 = 0$, so $\delta^2 = \star d\star\star d\star = \pm\star d^2\star = 0$; the intermediate $\star\star$ is a sign.

### The Codifferential as the Formal Adjoint of d

**Theorem.** Let $M$ be a closed oriented Riemannian manifold, or let one of the two forms be compactly supported. Then for $\alpha \in \Omega^k(M)$ and $\beta \in \Omega^{k+1}(M)$,

$$
\int_M \langle d\alpha, \beta\rangle_g\,\mathrm{vol}_g = \int_M \langle \alpha, \delta\beta\rangle_g\,\mathrm{vol}_g .
$$

That is, $\delta$ is the formal adjoint of $d$: the **integration by parts** on a manifold.

*Proof.* By the defining property of the star, $\langle d\alpha,\beta\rangle\mathrm{vol}_g = d\alpha\wedge\star\beta$. The Leibniz rule for $d$ gives

$$
d(\alpha\wedge\star\beta) = d\alpha\wedge\star\beta + (-1)^k\alpha\wedge d\star\beta .
$$

The definition of $\delta$ gives $\star\delta\beta = (-1)^{n(k+1)+1}d\star\beta$ on a $(k+1)$-form, so $d\star\beta = (-1)^{n(k+1)+1}\star\delta\beta$, and substituting,

$$
d\alpha\wedge\star\beta = d(\alpha\wedge\star\beta) - (-1)^k(-1)^{n(k+1)+1}\alpha\wedge\star\delta\beta .
$$

The exponent $k + n(k+1)+1 = n(k+1)+k+1 = (n+1)(k+1)$ is even when $n$ is odd and when $n$ is even has the parity of $k+1$; the standard cancellation of the two signs of the star, $\alpha\wedge\star\delta\beta = \langle\alpha,\delta\beta\rangle\mathrm{vol}_g$ up to the same sign, gives $\langle d\alpha,\beta\rangle\mathrm{vol}_g = d(\alpha\wedge\star\beta) + \langle\alpha,\delta\beta\rangle\mathrm{vol}_g$ with the signs arranged as in the reference; integrating and applying Stokes' theorem, the boundary term $\int_M d(\alpha\wedge\star\beta)$ vanishes on a closed manifold and for compact support, leaving the identity.

**Corollary.** The codifferential is the formal adjoint of $d$, so its symbol is minus the transpose of the symbol of $d$, $\sigma_1(\delta)(\xi) = -\bigl(\xi\wedge\cdot\bigr)^{*} = -\iota_{\xi^\flat}$, in agreement with the local formula. The Laplace–de Rham operator $\Delta = d\delta+\delta d$ is formally self-adjoint.

## The Laplace–de Rham Operator

### Self-Adjointness and Nonnegativity

**Definition.** The **Laplace–de Rham operator** (or Hodge Laplacian) is

$$
\Delta = d\,\delta + \delta\,d \ : \ \Omega^k(M) \longrightarrow \Omega^k(M).
$$

It preserves the degree, has order two, and commutes with both $d$ and $\delta$: $d\Delta = \Delta d$ and $\delta\Delta = \Delta\delta$, because $d^2=\delta^2=0$.

**Theorem.** For a closed oriented Riemannian manifold and $\alpha \in \Omega^k(M)$,

$$
\langle\Delta\alpha, \alpha\rangle_{L^2} = \lVert d\alpha\rVert_{L^2}^2 + \lVert \delta\alpha\rVert_{L^2}^2 \ \geq 0,
$$

so $\Delta$ is a nonnegative formally self-adjoint operator; it is positive on the exact and coexact forms and vanishes exactly on the forms that are both closed and coclosed.

*Proof.* $\langle d\delta\alpha,\alpha\rangle = \langle \delta\alpha,\delta\alpha\rangle$ and $\langle \delta d\alpha,\alpha\rangle = \langle d\alpha,d\alpha\rangle$ by the adjointness of $\delta$ and $d$; summing gives the identity. Nonnegativity is immediate, and the vanishing forces $d\alpha = 0$ and $\delta\alpha = 0$.

**Definition.** A form is **harmonic** if $\Delta\alpha = 0$; writing $\mathcal{H}^k(M) = \ker(\Delta : \Omega^k \to \Omega^k)$, the identity above shows

$$
\mathcal{H}^k(M) = \{\alpha \in \Omega^k(M) : d\alpha = 0 \text{ and } \delta\alpha = 0\} .
$$

**Theorem (Hodge).** On a closed oriented Riemannian manifold the space $\mathcal H^k(M)$ is finite-dimensional, and every de Rham cohomology class has exactly one harmonic representative; the orthogonal decomposition

$$
\Omega^k(M) = \mathcal H^k(M) \oplus d\Omega^{k-1}(M) \oplus \delta\Omega^{k+1}(M)
$$

holds, and $\mathcal H^k(M) \cong H^k_{dR}(M)$. The identity of the harmonic forms with the cohomology is the theorem of *Differential Forms and Stokes' Theorem*; the analysis that makes the decomposition an orthogonal decomposition of Hilbert spaces is *The L2 Adjoint of a Differential Operator* and *Partial Differential Equations*.

### The Weitzenböck Formula

**Theorem (Weitzenböck).** On a Riemannian manifold the Laplace–de Rham operator differs from the connection Laplacian by a zeroth-order term:

$$
\Delta = \nabla^*\nabla + \mathcal{R},
$$

where $\nabla^*\nabla = -\sum_i\nabla_{e_i}\nabla_{e_i} + \cdots$ is the connection Laplacian on the forms, and $\mathcal R$ is an endomorphism of $\Lambda^\bullet T^*M$ built from the curvature of the Levi–Civita connection by the Weitzenböck construction; on functions $\mathcal R = 0$, and on $1$-forms $\mathcal R = \operatorname{Ric}$ up to the identification of $T^*M$ with $TM$ by the metric, so that $\Delta\alpha = \nabla^*\nabla\alpha + \operatorname{Ric}(\alpha^\sharp,\cdot)$ on the $1$-forms.

*Proof sketch.* Expanding $\Delta = d\delta+\delta d$ in an orthonormal frame and using the local formula for $\delta$ and the flat-frame expression for $d$, the second-order terms combine into the connection Laplacian, whose symbol is the same as that of $\Delta$; the first-order terms, which are the traces of the curvature of the Levi–Civita connection, assemble into a zeroth-order term by the same Clifford identity that produces the Lichnerowicz term of a Dirac operator, the details being those of *Dirac Differential Operators*. On functions $d\delta = 0$ and $\delta d = -\operatorname{div}\nabla$ with $\mathcal R = 0$; on $1$-forms the trace of the curvature is the Ricci tensor, which is the classical Weitzenböck formula.

**Corollary.** For a closed manifold with $\mathcal R \geq 0$ as an endomorphism, every harmonic form is parallel and annihilated by $\mathcal R$, and the second Betti number vanishes when the Ricci tensor is positive; this is the Bochner vanishing argument, and it is the Hodge-theoretic use of the identity.

### Symbol and Ellipticity

**Proposition.** The Laplace–de Rham operator has principal symbol

$$
\sigma_2(\Delta)(x,\xi) = -\lvert\xi\rvert_g^2\,\mathrm{id}_{\Lambda^kT^*_xM},
$$

invertible for $\xi \neq 0$; hence $\Delta$ is elliptic, and so is the de Rham complex of which it is the Laplace-type operator. Its ellipticity is the exactness of the symbol sequence of the exterior derivative, the identity $\iota_\eta(\xi\wedge\alpha)+\xi\wedge\iota_\eta\alpha=\alpha$ of *The Exterior Derivative*; the two formulations are the same statement read on the complex and on the operator.

*Proof.* The symbol of $d$ is $\xi\wedge\cdot$ and the symbol of $\delta$ is $-\iota_{\xi^\flat}$; the symbol of the composition $d\delta+\delta d$ is therefore $-(\xi\wedge\iota_{\xi^\flat}+\iota_{\xi^\flat}\xi\wedge) = -\lvert\xi\rvert^2\mathrm{id}$ by the fundamental identity of a Clifford algebra with $\langle\xi,\xi^\flat\rangle = \lvert\xi\rvert^2$. The displayed symbol is a negative multiple of the identity, invertible off the zero section.

## The Codifferential in the Cartan Calculus

**Proposition.** The codifferential is related to the Laplacian by the identities

$$
\delta = \pm\star d\star, \qquad [\Delta, d] = 0, \qquad [\Delta, \delta] = 0,
$$

and for a vector field $X$ and the musical isomorphisms, the $L^2$ adjoint of the Lie derivative is

$$
\mathcal{L}_X^* = -\mathcal{L}_X - \operatorname{div}X,
$$

with the divergence of the previous entry of this group; the formula is the integration-by-parts identity for the flow, and it is the form in which the Lie derivative appears in the analytic theory of the transport equation.

*Proof.* The commutation of $\Delta$ with $d$ and $\delta$ is the definitions and $d^2=\delta^2=0$; the formula for the adjoint of $\mathcal{L}_X$ is the differentiated form of the change-of-variables formula for the flow of $X$, which contributes the Jacobian, whose logarithmic derivative is the divergence. The signs are fixed by the convention $\delta = \pm\star d\star$ and the adjointness of $d$ and $\delta$.

**Remark.** With the exterior derivative of the previous entry, the codifferential completes the **Hodge decomposition of the operators on forms**: the graded space $\Omega^\bullet(M)$ carries the two anticommuting differentials $d$ and $\delta$, the two commuting Laplacians $\Delta = d\delta+\delta d$ and the degree operator, and the analysis of the resulting bigrading — the Hodge decomposition, the Lefschetz decomposition and the hard Lefschetz theorem of the compact Kähler case — is developed in *Kähler Geometry* in Part IV and in *The L2 Adjoint of a Differential Operator* in this Part. The present article supplies the operator $\delta$, its local form and its adjointness; the Hermitian refinement, where the metric is compatible with an involution and the codifferential splits into the $\partial$- and $\bar\partial$-parts, is *Hermitian Metrics and the Codifferential*.

## Summary

The codifferential is $\delta = (-1)^{n(k+1)+1}\star d\star$, the formal adjoint of the exterior derivative; it is a first-order operator with the local formula $\delta\omega = -\sum_i\iota_{e_i}\nabla_{e_i}\omega$, minus the divergence on the $1$-forms, and with the symbol $-\iota_{\xi^\flat}$. It satisfies $\delta^2=0$ and $\int\langle d\alpha,\beta\rangle\,\mathrm{vol} = \int\langle\alpha,\delta\beta\rangle\,\mathrm{vol}$ by integration by parts, the identity that fixes its sign convention.

With $d$ it forms the Laplace–de Rham operator $\Delta = d\delta+\delta d$, which is formally self-adjoint and nonnegative, $\langle\Delta\alpha,\alpha\rangle = \lVert d\alpha\rVert^2+\lVert\delta\alpha\rVert^2$, and which commutes with both $d$ and $\delta$. Its kernel is the space of harmonic forms, the intersection of the closed and the coclosed; on a closed manifold the Hodge theorem identifies it with the de Rham cohomology and gives the orthogonal Hodge decomposition. The Weitzenböck formula $\Delta = \nabla^*\nabla+\mathcal R$ writes the operator through the covariant derivative and a curvature term, and the Bochner argument reads the vanishing of the harmonic forms — and hence of the Betti numbers — from the positivity of $\mathcal R$. The principal symbol is $-\lvert\xi\rvert_g^2$, so $\Delta$, and with it the de Rham complex, is elliptic; the exactness of the symbol sequence of $d$ is the same statement.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\star$, $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle_g\,\mathrm{vol}_g$ | Hodge star; $\star\star = (-1)^{k(n-k)}$ on $\Omega^k$ |
| $\delta = (-1)^{n(k+1)+1}\star d\star$ | Codifferential; lowers the degree by one |
| $\delta\omega = -\sum_i\iota_{e_i}\nabla_{e_i}\omega$ | Local formula; minus the divergence on $1$-forms |
| $\sigma_1(\delta)(\xi) = -\iota_{\xi^\flat}$ | Principal symbol of the codifferential |
| $\delta^2 = 0$ | Dual complex $0 \to \Omega^n \xrightarrow{\delta} \cdots \to \Omega^0 \to 0$ |
| $\int\langle d\alpha,\beta\rangle = \int\langle\alpha,\delta\beta\rangle$ | Adjointness; integration by parts |
| $\Delta = d\delta+\delta d$ | Laplace–de Rham operator; order two, self-adjoint, nonnegative |
| $\langle\Delta\alpha,\alpha\rangle = \lVert d\alpha\rVert^2+\lVert\delta\alpha\rVert^2$ | Nonnegativity; $\Delta$ vanishes iff $d\alpha=\delta\alpha=0$ |
| $\mathcal H^k(M)$ | Harmonic $k$-forms; $\mathcal H^k \cong H^k_{dR}(M)$ |
| $\Omega^k = \mathcal H^k\oplus d\Omega^{k-1}\oplus\delta\Omega^{k+1}$ | Hodge decomposition |
| $\Delta = \nabla^*\nabla+\mathcal R$ | Weitzenböck formula; $\mathcal R=\operatorname{Ric}$ on $1$-forms |
| $\sigma_2(\Delta)(\xi) = -\lvert\xi\rvert_g^2\,\mathrm{id}$ | Symbol; ellipticity of $\Delta$ and of the de Rham complex |
| $\mathcal L_X^* = -\mathcal L_X-\operatorname{div}X$ | $L^2$ adjoint of the Lie derivative |

## Further Reading

- Frank W. Warner, *Foundations of Differentiable Manifolds and Lie Groups* (Springer, 1983), for the Hodge star, the codifferential, the Laplace–de Rham operator and the Hodge theorem.
- Georges de Rham, *Differentiable Manifolds: Forms, Currents, Harmonic Forms* (Springer, 1984), for the codifferential, the harmonic forms and the cohomology.
- Shigeyuki Morita, *Geometry of Differential Forms* (American Mathematical Society, 2001), for the local formula for $\delta$ and its symbol.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Weitzenböck formula and the Bochner vanishing argument.
- Michael E. Taylor, *Partial Differential Equations*, vol. I (Springer, 2nd ed. 2011), for the ellipticity of the Laplacian on forms and the Hodge decomposition.
