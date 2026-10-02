
# __The Adjoint of the Twistor Operator__

## Introduction

The twistor operator $\mathcal{T}=\pi\circ\nabla^{\mathcal{S}}$ is not an operator on one bundle: it maps the spinor sections to the one-form valued spinors, $\Gamma(\mathcal{S})\to\Gamma(T^*M\otimes\mathcal{S})$, and it is the projection of the covariant derivative onto the kernel of the Clifford contraction. Its adjoint for the $L^2$ form is therefore an operator in the reverse direction, and the shape of the answer is simple: the adjoint of the projection is the projection, and the adjoint of the covariant derivative is the covariant divergence, so

$$
\mathcal{T}^{*} = \nabla^{*}\circ\pi ,
$$

with $\nabla^*$ the adjoint connection of *The Codifferential on a Spinor Bundle*. The article computes the adjoint, derives the orthogonal decomposition of the connection Laplacian that it produces,

$$
\nabla^{*}\nabla = \mathcal{T}^{*}\mathcal{T}+\tfrac1n D^{2} ,
$$

with $D$ the self-adjoint Cauchy–Riemann operator, and reads from it the consequences for the twistor equation $\mathcal{T}\sigma=0$: the equivalent form $\nabla_X\sigma=-\frac1nc(X)D\sigma$ of the equation and the scalar identity satisfied by the twistor spinors.

**The boundaries.** The operator, its projection $\pi$ and the contraction $c$ are *The Twistor Operator*; the Cauchy–Riemann operator, its self-adjointness $D^*=D$ and the Lichnerowicz formula are *The Spinor Operator*; the adjoint connection and its calculus are *The Codifferential on a Spinor Bundle*; the Clifford multiplication and its adjoint are *The Clifford Multiplication Operator* and *The Adjoint of the Clifford Multiplication*. The involutions, the conjugate symmetry and the Hermitian pairing of the kernel are *Involutions of the Twistor Operator*, the preceding entry of the group. The spectral theory of $\mathcal{T}^*\mathcal{T}$ is Part III's. The body is a Riemannian spin manifold with the fibre form $h$, $c(v)^*=-c(v)$ and the twistor operator of *The Twistor Operator*.

## The Formal Adjoint

**Definition.** The **formal adjoint** $\mathcal{T}^*$ of the twistor operator is the differential operator $\Gamma(T^*M\otimes\mathcal{S})\to\Gamma(\mathcal{S})$ with

$$
\int_M h(\mathcal{T}\sigma,\psi)\,\mu_g = \int_M h(\sigma,\mathcal{T}^{*}\psi)\,\mu_g
$$

for all compactly supported smooth sections, $h$ extended to the twisted bundle by the metric on the cotangent factor.

**Theorem.** $\mathcal{T}^{*}=\nabla^{*}\circ\pi$, where $\pi=\mathrm{id}-\frac1nc^*c$ is the $h$-orthogonal projection onto $\ker c$ and $\nabla^*$ is the adjoint of the covariant derivative; the principal symbol of $\mathcal{T}^*$ is the adjoint Clifford contraction, and $\mathcal{T}$ and $\mathcal{T}^*$ are elliptic of order one.

**Proof.** The adjoint of a composite is the composite of the adjoints in the reverse order, so $\mathcal{T}^*=(\pi\nabla)^*=\nabla^*\pi^*$, and $\pi$ is an orthogonal projection for the pointwise form, hence $\pi^*=\pi$. The symbol statements are the symbol of the contraction and of its adjoint, and the ellipticity is the invertibility of the symbol of $\mathcal{T}$ on the trace-free part, which is the content of the symbol computation of *The Twistor Operator*.

**Proposition (the components).** Writing a twisted section as $\psi=\sum_i\theta^i\otimes\psi_i$ with $\psi_i\in\Gamma(\mathcal{S})$, the projection acts by

$$
\pi\psi = \sum_i\theta^i\otimes\Bigl(\psi_i+\tfrac1n c(e_i)(c\psi)\Bigr) , \qquad c\psi=\sum_j c(e_j)\psi_j ,
$$

and the adjoint is $\mathcal{T}^{*}\psi=-\sum_i\nabla_i\bigl(\psi_i+\tfrac1nc(e_i)(c\psi)\bigr)$ up to the lower-order terms of $\nabla^*$; in particular $\mathcal{T}^*\psi$ depends on $\psi$ through its trace-free part and the divergence of its components.

**Proof.** The formula for $\pi$ is the definition $\pi\psi=\psi-\frac1nc^*c\psi$ with the adjoint contraction $c^*\sigma=-\sum_i\theta^i\otimes c(e_i)\sigma$ of *The Adjoint of the Clifford Multiplication*; the divergence is the leading part of $\nabla^*$, which is $-\sum_i\nabla_i$ on the components plus the curvature terms recorded in *The Codifferential on a Spinor Bundle*.

**Remark (the pairing as the twistor form).** The $L^2$ pairing of the definition is the integrated form of the pointwise Hermitian form of *Hermitian Clifford Structures*; the anti-linearity in the second argument and the reality of $\nabla$ make the pairing conjugate-symmetric, which is the **conjugate symmetry** of *Involutions of the Twistor Operator* read at the level of the adjoint.

## The Decomposition of the Connection Laplacian

**Theorem (the orthogonal decomposition).** The connection Laplacian decomposes as

$$
\nabla^{*}\nabla = \mathcal{T}^{*}\mathcal{T}+\tfrac1n D^{2} ,
$$

where $D$ is the Cauchy–Riemann operator of *The Spinor Operator*; both summands are non-negative operators on the compactly supported sections, and the decomposition is orthogonal for the $L^2$ form.

**Proof.** Let $\pi=\mathrm{id}-\frac1nc^*c$ be the projection onto $\ker c$ and write the identity $\mathrm{id}=\pi+\frac1nc^*c$. Then

$$
\nabla^{*}\nabla=\nabla^{*}\bigl(\pi+\tfrac1nc^{*}c\bigr)\nabla = (\nabla^{*}\pi)\nabla+\tfrac1n\nabla^{*}c^{*}c\nabla = \mathcal{T}^{*}\mathcal{T}+\tfrac1n\nabla^{*}c^{*}c\nabla .
$$

Now $\nabla^*c^*=(c\nabla)^*$, because the adjoint of a composite is the composite of the adjoints and $(\nabla^*)^*=\nabla$; and $(c\nabla)^*=D^*=D$ by the formal self-adjointness of the Cauchy–Riemann operator of *The Spinor Operator*. Hence $\nabla^*c^*c\nabla=D\circ D=D^2$, which gives the identity. The non-negativity is $\langle\nabla^{*}\nabla\sigma,\sigma\rangle=\lVert\nabla\sigma\rVert^2\ge0$ and the corresponding statements for the two summands, since each is a composite of an operator with its adjoint: $\mathcal{T}^*\mathcal{T}=(\mathcal{T})^*(\mathcal{T})$ and $D^2=D^*D$.

**Corollary.** The kernel of $\mathcal{T}$ is the kernel of $\mathcal{T}^*\mathcal{T}$, and it is a subspace of the kernel of $\nabla^*\nabla$; the twistor spinors are the parallel spinors of the decomposition's first summand, and the identity shows how the twistor equation sits inside the equation $\nabla^*\nabla\sigma=\frac1nD^2\sigma$.

**Proof.** For a compactly supported section, $\langle\mathcal{T}^*\mathcal{T}\sigma,\sigma\rangle=\lVert\mathcal{T}\sigma\rVert^2$, so $\mathcal{T}\sigma=0$ exactly when $\mathcal{T}^*\mathcal{T}\sigma=0$; the identity gives the second statement.

## The Twistor Equation

**Theorem.** For a spinor $\sigma$ the twistor equation $\mathcal{T}\sigma=0$ is equivalent to

$$
\nabla_X\sigma = -\tfrac1n c(X)D\sigma \qquad\text{for all vector fields } X ,
$$

and then $\sigma$ satisfies the scalar identity

$$
\nabla^{*}\nabla\sigma = \frac{\operatorname{scal}}{4(n-1)}\,\sigma , \qquad D^{2}\sigma = \frac{n}{4(n-1)}\,\operatorname{scal}\,\sigma ,
$$

where $\operatorname{scal}$ is the scalar curvature.

**Proof.** $\mathcal{T}\sigma=0$ means that $\nabla\sigma$, a one-form valued spinor, lies in the kernel of the contraction $c$, that is in the image of $c^*$, and the component form of that membership is $\nabla_X\sigma=-\frac1nc(X)D\sigma$: indeed $c(\nabla\sigma)=0$ means $\sum_ic(e_i)\nabla_i\sigma=0$, and the trace-free condition identifies $\nabla_X\sigma+\frac1nc(X)D\sigma$ as the orthogonal projection onto the trace-free part. For the scalar identity, substitute into the decomposition of the connection Laplacian: $\nabla^*\nabla\sigma=\frac1nD^2\sigma$ because the first summand vanishes, and the Lichnerowicz formula $D^2=\nabla^*\nabla+\frac14\operatorname{scal}$ of *The Spinor Operator* gives $\nabla^*\nabla\sigma=\frac1n\nabla^*\nabla\sigma+\frac{\operatorname{scal}}{4n}\sigma$, which is the display.

**Corollary (the domain of the solutions).** A twistor spinor is determined by $\sigma(x)$ and $\nabla\sigma(x)$ at one point, so the space of twistor spinors has dimension at most $2^{\lfloor n/2\rfloor+1}$; the bound is attained on the conformally flat manifolds by *The Penrose Operator*, where the space is a representation of the conformal algebra.

**Proof.** The equation $\nabla_X\sigma=-\frac1nc(X)D\sigma$ is a first-order system whose initial data are the values of $\sigma$ and of $\nabla\sigma$ modulo the relation; the dimension of the spinor fibre gives $2^{\lfloor n/2\rfloor}$, and the one-form constrained to be the image of $c^*$ contributes one further spinor, whence $2^{\lfloor n/2\rfloor+1}$; the attainment is the quoted statement of *The Penrose Operator*.

**Remark.** The scalar identity is the reason a twistor spinor with a parallel $D\sigma$ off a zero of the scalar curvature is forced to vanish or to be special: integrating the identity against the volume form gives $\int\lvert\nabla\sigma\rvert^2=\frac1{4(n-1)}\int\operatorname{scal}\,\lvert\sigma\rvert^2$, and a definite sign of the scalar curvature then excludes or forces the solutions; the argument is the analytic counterpart of the Bochner method and its rigour is Part III's.

## Worked Cases

### The Flat Space

For $\mathbb{R}^n$ with the standard spin structure, $\mathcal{T}\sigma=0$ has the solutions $\sigma=\sigma_0+\sum_ix^ic(e_i)\sigma_0$ with $\sigma_0$ parallel, the dimension is $2^{\lfloor n/2\rfloor+1}$, and $\mathcal{T}^*\mathcal{T}$ is $-\Delta$ on the trace-free part; the identity $\nabla^*\nabla=\mathcal{T}^*\mathcal{T}+\frac1nD^2$ is the flat decomposition of the connection Laplacian, and the scalar identity is vacuous because $\operatorname{scal}=0$.

### The Round Sphere

For $S^n$ with the round metric, $\operatorname{scal}=n(n-1)$, the twistor spinors are the sums of the two Killing families, the dimension attains the bound $2^{\lfloor n/2\rfloor+1}$, and the scalar identity reads $\nabla^*\nabla\sigma=\frac n4\sigma$; the first eigenvalue of the connection Laplacian on the twistor spinors is $\frac n4$.

### A Compact Einstein Manifold

For a compact Einstein manifold of positive scalar curvature the twistor operator has finite-dimensional kernel by ellipticity, the identity gives the bound on the dimension in terms of the eigenvalue of the twistor Laplacian, and the rigidity statements — that a compact manifold with the maximal number of twistor spinors is conformally flat — are quoted from the literature.

## Summary

The **formal adjoint** of the twistor operator is $\mathcal{T}^{*}=\nabla^{*}\circ\pi$, the composition of the covariant divergence with the orthogonal projection onto $\ker c$; with the corpus's signs $c(v)^*=-c(v)$ and $D^*=D$, it yields the **orthogonal decomposition of the connection Laplacian**

$$
\nabla^{*}\nabla=\mathcal{T}^{*}\mathcal{T}+\tfrac1n D^{2} ,
$$

proved from $\mathrm{id}=\pi+\frac1nc^*c$ and $\nabla^*c^*=D$. There follows the equivalent form of the **twistor equation**, $\nabla_X\sigma=-\frac1nc(X)D\sigma$, the scalar identity $\nabla^*\nabla\sigma=\frac{\operatorname{scal}}{4(n-1)}\sigma$ with $D^2\sigma=\frac{n}{4(n-1)}\operatorname{scal}\sigma$, and the bound $2^{\lfloor n/2\rfloor+1}$ on the dimension of the space of twistor spinors, attained on the conformally flat manifolds. The operator is *The Twistor Operator*, its involutions and the conjugate symmetry of the pairing are *Involutions of the Twistor Operator*, the Cauchy–Riemann operator and the Lichnerowicz formula are *The Spinor Operator*, the adjoint connection is *The Codifferential on a Spinor Bundle*, and the spectral theory of $\mathcal{T}^*\mathcal{T}$ is Part III's.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{T}=\pi\circ\nabla$, $\pi=\mathrm{id}-\frac1nc^*c$ | Twistor operator |
| $\mathcal{T}^{*}=\nabla^{*}\pi$ | Formal adjoint |
| $D=c\circ\nabla$, $D^*=D$ | Self-adjoint Cauchy–Riemann operator |
| $\nabla^{*}\nabla=\mathcal{T}^{*}\mathcal{T}+\frac1nD^2$ | Orthogonal decomposition of the connection Laplacian |
| $\nabla_X\sigma=-\frac1nc(X)D\sigma$ | Equivalent form of the twistor equation |
| $\nabla^{*}\nabla\sigma=\frac{\operatorname{scal}}{4(n-1)}\sigma$ | Scalar identity for twistor spinors |
| $2^{\lfloor n/2\rfloor+1}$ | Bound on the dimension of the space of twistor spinors |

## Further Reading

- Helga Baum, Thomas Friedrich, Ralf Grunewald and Ines Kath, *Twistors and Killing Spinors on Riemannian Manifolds* (Teubner, 1991), for the twistor operator, its adjoint and the scalar identity for twistor spinors.
- Thomas Friedrich, *Dirac Operators in Riemannian Geometry* (American Mathematical Society, 2000), for the decomposition of the connection Laplacian, the Lichnerowicz formula and the Weitzenböck method.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the adjoint connections, the projection onto $\ker c$ and the elliptic complexes of the spinor bundle.
- Nicole Berline, Ezra Getzler and Michèle Vergne, *Heat Kernels and Dirac Operators* (Springer, 1992), for the symbol calculus of the twisted operators and the elliptic decomposition.
