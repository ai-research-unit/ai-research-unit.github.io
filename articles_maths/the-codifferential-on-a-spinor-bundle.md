
# __The Codifferential on a Spinor Bundle__

## Introduction

A connection on a vector bundle is a first-order operator $\nabla : \Gamma(E)\to\Gamma(T^*M\otimes E)$, and every such operator has a **formal adjoint** for the $L^2$ pairing of the bundle with its fibre metric. The adjoint of the spin connection is a first-order operator that lowers the form degree by one, and it is the **codifferential** of the spinor bundle:

$$
\delta = \nabla^{*} : \Gamma(T^*M\otimes\mathcal{S})\longrightarrow\Gamma(\mathcal{S}), \qquad \delta = -\operatorname{tr}_g\nabla .
$$

The name is taken from the exterior calculus, where the codifferential $d^*$ is the adjoint of the exterior derivative, and the analogy is exact but limited: the codifferential of a bundle-valued connection is the adjoint of the connection, so it is not in general a square-zero operator, and it is not a differential on a complex of forms. This article treats the codifferential of the spinor bundle, its relation to the adjoint of the spin connection, and its relation to the Cauchy–Riemann operator; the connection Laplacian $\delta\nabla=\nabla^*\nabla$ that appears in the Lichnerowicz formula is its most important application.

The two adjoint relations that organise the account are the following. First, $\delta$ is to $\nabla$ what the divergence is to the gradient: it is the metric contraction of the covariant derivative, and it satisfies $\langle\nabla\sigma,\alpha\rangle = \langle\sigma,\delta\alpha\rangle$ on a closed manifold. Second, the Cauchy–Riemann operator $D=c\circ\nabla$ is the composition of the connection with the Clifford contraction $c$, and its formal adjoint is $\delta\circ c^*$ together with the derivative of the frame; for the spin connection the result is the same operator, $D^*=D$, and this self-adjointness is the reason the codifferential is the natural adjoint partner of the operator of *The Spinor Operator*.

**The boundaries.** The spin connection and the Cauchy–Riemann operator are *The Spinor Operator*; the Clifford multiplication and the contraction $c$ are *The Clifford Multiplication Operator*; the analytic theory of the adjoint operator — the domains, the boundary conditions and the self-adjoint extensions — belongs to Part III, where the measure and the limit are available, and is cited. The exterior codifferential $d^*$ of a Riemannian manifold and the Hodge Laplacian are *The Hodge Laplacian and Harmonic Forms*; the general formal adjoint of a differential operator and the Green formula are *Formal Adjoints and Green's Formula*. The base is a closed Riemannian spin manifold $(M,g)$ with spinor bundle $\mathcal{S}$ and spin connection $\nabla^{\mathcal{S}}$; the fibre form $h$ is positive definite and $c(v)^*=-c(v)$.

## The Adjoint of the Spin Connection

### Definition

**Definition.** The **codifferential** of the spinor bundle is the formal adjoint of the spin connection, the first-order operator

$$
\delta : \Gamma(T^*M\otimes\mathcal{S})\longrightarrow\Gamma(\mathcal{S}), \qquad
\delta(\alpha\otimes s) = -\sum_{i=1}^{n}\Bigl(\bigl(\nabla^{\mathcal{S}}_{e_i}\alpha\bigr)(e_i)\,s + \alpha(e_i)\,\nabla^{\mathcal{S}}_{e_i}s\Bigr),
$$

in a local orthonormal frame $(e_1,\dots,e_n)$, where the first term contracts the derivative of the form factor and the second contracts the form with the derivative of the spinor. Equivalently $\delta = -\operatorname{tr}_g\nabla^{\mathcal{S}}$, the negative of the metric trace of the connection.

**Proposition.** Let $\alpha\in\Gamma(T^*M\otimes\mathcal{S})$ and $s\in\Gamma(\mathcal{S})$, and take $M$ closed. Then

$$
\int_M h(\nabla^{\mathcal{S}}s,\alpha)\,d\text{vol}_g = \int_M h(s,\delta\alpha)\,d\text{vol}_g ,
$$

where the pairing of $T^*M\otimes\mathcal{S}$ is the tensor product of $g^{-1}$ and $h$; so $\delta$ is the formal adjoint of $\nabla^{\mathcal{S}}$.

**Proof.** The claim is local, so fix a frame and a point. Both sides are first-order in $\alpha$ and $s$, and the identity is the integration by parts: writing $h(\nabla^{\mathcal{S}}s,\alpha)=\sum_i h(\nabla^{\mathcal{S}}_{e_i}s,\alpha(e_i))$ in an orthonormal frame and integrating the derivative of the product, the boundary term vanishes on a closed manifold, and the derivative of the frame and of the volume form contribute exactly the first term of the definition of $\delta$. The computation is the standard formal-adjoint calculation; the general statement for a connection with a metric-compatible structure group is *Formal Adjoints and Green's Formula*.

**Remark (the name and the limits of the analogy).** On the exterior bundle with the Levi-Civita connection, the same construction gives the codifferential $d^*$ of differential forms, and there $\delta$ is a first-order operator of square zero. For a general spinor bundle the square $\delta^2$ is not zero — the codifferential lives on the single degree-one piece of a graded complex that does not exist here — and the operator is simply the adjoint of the connection. The name is kept for the exterior analogy, and no square-zero property is asserted.

### The Symbol of the Codifferential

**Proposition.** The principal symbol of the codifferential at a covector $\xi$ is

$$
\sigma_{\delta}(x,\xi) = -\operatorname{contr}_{\xi} : T_x^*M\otimes\mathcal{S}_x\longrightarrow\mathcal{S}_x ,
$$

the metric contraction of the form factor with $\xi$; it is a surjection for $\xi\ne0$, it is not injective, and its kernel is the subspace of $\xi$-trace-free elements of $T^*M\otimes\mathcal{S}$.

**Proof.** The symbol of the covariant derivative in the direction $X$ is $\xi(X)$ acting on the value, so the symbol of $\delta$ is $-\sum_i\xi(e_i)$ acting by the contraction on the $i$-th component of the form, which is the contraction with $\xi$; its image is $\mathcal{S}$ because $\xi$ has a nonzero component, and its kernel consists of the elements $\alpha$ with $\sum_i\xi(e_i)\alpha(e_i)=0$, the $\xi$-trace-free ones. The contraction map has rank $\dim\mathcal{S}$ and its kernel has dimension $(n-1)\dim\mathcal{S}$.

**Remark (the two contractions).** The codifferential is the contraction of the connection in the form variable, while the Cauchy–Riemann operator is the Clifford contraction of the connection. On the spinor bundle both contractions appear, and they are different operators: one is the adjoint of the other's connection, and the relation between them is the adjoint of the Clifford contraction, treated next.

## The Adjoint of the Cauchy–Riemann Operator

### The Relation Through the Clifford Contraction

**Given.** The Clifford contraction $c : T^*M\otimes\mathcal{S}\to\mathcal{S}$, $c(\xi\otimes\sigma)=\xi^{\sharp}\cdot\sigma$, with adjoint $c^* : \mathcal{S}\to T^*M\otimes\mathcal{S}$, $c^*\sigma=-\sum_i\theta^i\otimes(e_i\cdot\sigma)$, and the orthogonality of the two first-order operators built from the connection: $D=c\circ\nabla^{\mathcal{S}}$ and $\mathcal{T}=\pi\circ\nabla^{\mathcal{S}}$ with $\pi=\operatorname{id}-\frac1n c^*c$, as in *The Clifford Multiplication Operator* and *The Twistor Operator*.

**Proposition (the flat model).** For the flat connection on $\mathbb{R}^n$, with $c^*\sigma=-\sum_i\theta^i\otimes(e_i\cdot\sigma)$ and $\delta\alpha=-\sum_i(\partial_{e_i}\alpha)(e_i)$, one has

$$
(\delta\circ c^*)\sigma = D\sigma ,
\qquad\text{hence}\qquad D^* = c\circ\nabla^{\mathcal{S}} = D ,
$$

since in the flat case the derivative of the frame vanishes.

**Proof.** With $\alpha=c^*\sigma=-\sum_i\theta^i\otimes(e_i\cdot\sigma)$ the components of $\alpha$ are constant in the frame and $\delta c^*\sigma = -\sum_i\partial_{e_i}(-e_i\cdot\sigma) = \sum_i e_i\cdot\partial_{e_i}\sigma = D\sigma$, using $e_i\cdot e_i=-1$ in the Riemannian convention and the constancy of the frame. The adjoint of a composition is the composition of the adjoints in reverse order, $D^*=(\nabla^{\mathcal{S}})^*c^*=\delta c^*$, and the display gives $D^*=D$.

**Theorem (the curved case, quoted).** On a closed spin manifold with the spin connection and the fibre form $h$, the Cauchy–Riemann operator is formally self-adjoint,

$$
D^* = D, \qquad \int_M h(D\sigma,\tau)\,d\text{vol}_g = \int_M h(\sigma,D\tau)\,d\text{vol}_g ,
$$

equivalently $\delta\circ c^* = c\circ\nabla^{\mathcal{S}}$ as operators on $\mathcal{S}$ after the derivative of the frame is included.

**Proof sketch.** The derivative of the orthonormal frame in the adjoint computation contributes a term that is the Clifford contraction of the connection form, and it cancels against the corresponding term in $c\circ\nabla^{\mathcal{S}}$ because the spin connection is metric-compatible and preserves the Clifford multiplication; equivalently, the formal adjoint of $D=\sum_ic(e_i)\nabla^{\mathcal{S}}_{e_i}$ is computed by moving both factors, and the two first-order terms recombine. This is the formal self-adjointness of *The Spinor Operator*, and it is quoted with the same argument.

### The Connection Laplacian

**Definition.** The **connection Laplacian** of the spinor bundle is the composition of the connection with its adjoint,

$$
\nabla^{*}\nabla = \delta\circ\nabla^{\mathcal{S}} : \Gamma(\mathcal{S})\longrightarrow\Gamma(\mathcal{S}),
$$

the negative of the trace of the second covariant derivative; it is a symmetric non-negative second-order operator.

**Proposition.** In a local frame, $\nabla^{*}\nabla\sigma = -\sum_i\bigl(\nabla^{\mathcal{S}}_{e_i}\nabla^{\mathcal{S}}_{e_i}\sigma-\nabla^{\mathcal{S}}_{\nabla_{e_i}e_i}\sigma\bigr)$ and

$$
\int_M h(\nabla^{*}\nabla\sigma,\sigma)\,d\text{vol}_g = \int_M \lvert\nabla^{\mathcal{S}}\sigma\rvert^2\,d\text{vol}_g \ge 0 ,
$$

so the connection Laplacian is non-negative and its kernel consists of the parallel spinors.

**Proof.** The first display is the definition of $\delta$ applied to $\nabla^{\mathcal{S}}\sigma$, with the contraction of the derivative of the connection; the second is the adjoint relation of the first proposition applied to $\alpha=\nabla^{\mathcal{S}}\sigma$, and the integrand is the pointwise square length of $\nabla^{\mathcal{S}}\sigma$ in the tensor product metric. The kernel statement is the vanishing of a non-negative integral.

**Theorem (the Lichnerowicz identity, quoted).** The Cauchy–Riemann operator and the connection Laplacian are related by

$$
D^2 = \nabla^{*}\nabla + \tfrac14\operatorname{scal},
$$

as *The Spinor Operator* records; the codifferential enters through the term $\nabla^{*}\nabla=\delta\nabla^{\mathcal{S}}$.

**Proof sketch.** The second-order terms of $D^2$ are the trace of the second covariant derivative, which is $-\nabla^{*}\nabla$, and the zeroth-order remainder is the Clifford contraction of the spin curvature; the identity is the Weitzenböck computation quoted from *Spin Geometry*.

## Worked Cases

### The Flat Torus

On the flat torus $\mathbb{T}^n$ with the trivial spin structure, the Fourier modes diagonalise the connection and the codifferential acts on the mode with frequency $\xi$ as the contraction with $\xi$: on the component $\theta^i\otimes s$ it is multiplication by $-\xi_i$, and $\delta\nabla^{\mathcal{S}}$ is multiplication by $|\xi|^2$ on the mode. The kernel of $\nabla^{*}\nabla$ is the constant spinors, and the codifferential of a spinor-valued one-form is its mode-wise contraction with the frequency.

### The Circle

On $S^1$ with the flat metric and the trivial spin structure, the spinor bundle has rank one over $\mathbb{C}$, the connection is the derivative and the codifferential of the one-form $f(\theta)\,d\theta\otimes s(\theta)$ is $-f'(\theta)s(\theta)-f(\theta)s'(\theta)$ — the two terms of the definition, the first from the derivative of the form and the second from the derivative of the spinor. The connection Laplacian is $-d^2/d\theta^2$, whose kernel is the constants, and the Cauchy–Riemann operator of the circle is the self-adjoint operator $i\,d/d\theta$ of *Dirac Differential Operators* in Part III.

### The Exterior Bundle

On the exterior bundle of a Riemannian manifold the same construction with the Levi-Civita connection reproduces the codifferential $d^*$ of forms, and the codifferential of the spinor bundle is the value at degree one of the general construction for a bundle with a metric-compatible connection. The difference is the square-zero property: $(d^*)^2=0$ on forms, while $\delta^2$ on spinor-valued one-forms has no reason to vanish, and it does not.

## Summary

The **codifferential** of the spinor bundle is the formal adjoint of the spin connection, $\delta=(\nabla^{\mathcal{S}})^*=-\operatorname{tr}_g\nabla^{\mathcal{S}}$, a first-order operator from spinor-valued one-forms to spinors, satisfying $\int h(\nabla^{\mathcal{S}}s,\alpha)=\int h(s,\delta\alpha)$ on a closed manifold; its symbol is the contraction with $\xi$, so it is a surjection with kernel the $\xi$-trace-free spinor-valued forms. It is not square zero in general, unlike its exterior analogue $d^*$, and the name records only the analogy. Composed with itself it gives the **connection Laplacian** $\delta\nabla^{\mathcal{S}}=\nabla^{*}\nabla$, a non-negative operator whose kernel consists of the parallel spinors, and it is the second-order operator appearing in the Lichnerowicz formula $D^2=\nabla^{*}\nabla+\frac14\operatorname{scal}$. The adjoint of the Cauchy–Riemann operator is $\delta\circ c^*$, and for the metric-compatible spin connection it equals $D$ itself: the **self-adjointness** $D^*=D$. The general formal adjoint is *Formal Adjoints and Green's Formula*, the exterior case *The Hodge Laplacian and Harmonic Forms*, and the operators built from the connection are *The Spinor Operator* and *The Twistor Operator*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\nabla^{\mathcal{S}}$ | Spin connection, $\Gamma(\mathcal{S})\to\Gamma(T^*M\otimes\mathcal{S})$ |
| $\delta=(\nabla^{\mathcal{S}})^*=-\operatorname{tr}_g\nabla^{\mathcal{S}}$ | Codifferential of the spinor bundle |
| $\sigma_{\delta}(\xi)=-\operatorname{contr}_{\xi}$ | Symbol; contraction with $\xi$, a surjection |
| $c$, $c^*$ | Clifford contraction and its adjoint |
| $D=c\circ\nabla^{\mathcal{S}}$, $D^*=D$ | Cauchy–Riemann operator and its self-adjointness |
| $\nabla^{*}\nabla=\delta\nabla^{\mathcal{S}}$ | Connection Laplacian, non-negative |
| $D^2=\nabla^{*}\nabla+\tfrac14\operatorname{scal}$ | Lichnerowicz identity |
| $d^*$, $(d^*)^2=0$ | Exterior codifferential, the square-zero analogue |

## Further Reading

- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the spin connection, its formal adjoint and the Weitzenböck formula.
- Nicole Berline, Ezra Getzler and Michèle Vergne, *Heat Kernels and Dirac Operators* (Springer, 1992), for the connection Laplacian and the adjoint calculus of Dirac-type operators.
- Richard S. Palais, *Foundations of Global Non-Linear Analysis* (Benjamin, 1968), for the formal adjoint of a connection and the integration-by-parts formalism on bundles.
- Thomas Friedrich, *Dirac Operators in Riemannian Geometry* (American Mathematical Society, 2000), for the adjoint of the spin connection and the Lichnerowicz formula in the spinor setting.
- John Roe, *Elliptic Operators, Topology and Asymptotic Methods* (Longman, 2nd ed. 1998), for the codifferential of a Clifford module and its symbol.
