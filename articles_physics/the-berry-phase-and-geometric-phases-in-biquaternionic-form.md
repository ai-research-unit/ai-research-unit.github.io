# __The Berry Phase and Geometric Phases in Biquaternionic Form__

## Introduction

A quantum system whose Hamiltonian is varied slowly around a closed loop in a parameter space need not return to its original state: beside the **dynamical phase** $-\frac{1}{\hbar}\int E_n\,dt$, which grows with the duration of the journey, an eigenstate can acquire a **geometric phase** that depends only on the loop. This is the **Berry phase**. Its two defining features are that it is a functional of the path rather than of the speed, and that for a closed path it is defined only modulo $2\pi$.

The phase is computed by two routes. The first integrates the **Berry connection** $\mathcal{A}$ — a $U(1)$ connection on the parameter space — around the loop; the second integrates the **Berry curvature** $\mathcal{F} = d\mathcal{A}$ over a surface that the loop bounds. Both routes are used below and checked against one another on an explicit example, because their agreement is the content of the statement that the phase is geometric.

This article carries that construction into the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ of the companion articles, and asks what the algebra contributes. The read-list notation is inherited unchanged: the algebra $\mathbb{B}$ with basis $e_0 = 1, e_1, e_2, e_3$ and $e_k^2 = -e_0$; the scalar imaginary $i$; the fixed-point subspaces $\mathbb{M}_+$ (Hermitian, the informational sector), $\mathbb{M}_-$ (anti-Hermitian, the material sector), $\mathbb{H}_{\mathbb{B}}$ (real quaternions), and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ (the center); the Hermitian observable $\tilde{H} = h_0 e_0 + i\mathbf{h}$; the idempotent $\tilde{P}_\pm(\hat{\mu}) = \tfrac12(e_0 \pm i\hat{\mu})$; the spinor $\psi$ in a minimal left ideal $\mathbb{B}\tilde{P}$ of the state module; and the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$.

The article's findings are stated here in advance, so that the reader can hold them against the text.

1. **The Berry connection is not visible in the state of $\mathbb{M}_+$.** The instantaneous eigenstate of a Hermitian Hamiltonian is an idempotent $\tilde{P}_\pm(\hat{\mathbf{h}})$, but $\mathrm{Tr}(\tilde{P}\,\partial_\mu\tilde{P}) = 0$ identically, so no Berry connection can be built from the idempotent alone. The connection lives on the **spinor** $\psi$ of the state module, and its definition uses the same trace pairing that gives the Born rule. This is the framework's sharpest statement about the Berry phase: the phase is carried by the spinor, which the Bloch-ball state discards.
2. **The connection is a $U(1)$ gauge connection on parameter space**, transforming as $\mathcal{A} \mapsto \mathcal{A} - d\alpha$ under a rephasing of the eigenstate, with curvature $\mathcal{F} = d\mathcal{A}$. Its structure group is the unitary part of the center $\mathbb{C}_{\mathbb{B}}$ — the same $U(1)$ that *The Gauge Principle in Biquaternionic Form* attaches to the algebra.
3. **The two routes agree** on spin-1/2 in a slowly rotating field: the line integral of the connection and the surface integral of the curvature both give $-\Omega/2$, where $\Omega$ is the solid angle subtended by the loop, for every loop in a one-parameter family.
4. **The curvature is quantised only on a closed surface.** The cap flux $-\pi(1-\cos\theta_0)$ is continuous in the loop; only the integral over the closed Bloch sphere is quantised, giving the Chern number $\mp 1$ for the two bands, whose sum is zero. The closed surface must avoid the degeneracy point, which is where the gap closes.
5. **The Berry connection is not the framework's spacetime connection.** It is literally the standard Berry connection, rewritten through the trace pairing. Its relation to the abelian connection $\tilde{A}$ of the gauge-principle article is an **analogy**: same structure group, same transformation law, same curvature definition, but a different base space and a different kind of object. It is not claimed to be the same field.

**Which case.** Throughout the article the level is **non-degenerate** and the Berry phase is **abelian** (a $U(1)$ number). For the two-level Hamiltonian the gap is $\Delta = 2|\mathbf{h}|$, and it is required to stay bounded away from zero along the path; at $\mathbf{h} = 0$ the two levels become degenerate, the gap closes, and the adiabatic theorem fails. The non-abelian (degenerate-level) case is not available in a single-qubit framework; the section *Degenerate Levels and the Abelian Case* states exactly why, and leaves it as a gap.

## The Adiabatic Setting and the Two Phases

Let the Hamiltonian depend on a set of real parameters $R = (R^1, R^2, \dots)$ taking values in a parameter space $\mathcal{P}$, and let $\tilde{H}(R) \in \mathbb{M}_+$ be Hermitian with instantaneous eigenvalues $E_n(R)$ and eigenvectors $|n(R)\rangle$. The **adiabatic theorem** states that if the gap

$$
\Delta(R) = \min_{m \neq n}\bigl|E_m(R) - E_n(R)\bigr|
$$

is bounded below by a positive constant along the traversed path, and if the path is traversed slowly enough compared with that gap, then a system started in $|n(R(0))\rangle$ remains in the instantaneous eigenstate up to a phase:

$$
|\psi(t)\rangle = e^{i\gamma_n(t)}\,e^{-\frac{i}{\hbar}\int_0^t E_n(R(t'))dt'}\,|n(R(t))\rangle .
$$

Substituting into the Schrödinger equation $i\hbar\,\partial_t|\psi\rangle = \tilde{H}|\psi\rangle$, the dynamical factor cancels, and what remains is

$$
\dot{\gamma}_n = i\,\langle n(R(t))|\frac{d}{dt}|n(R(t))\rangle ,
\qquad\text{so}\qquad
\gamma_n = i\int_{\mathcal{C}}\langle n|\nabla_R n\rangle\cdot dR .
$$

The right-hand side is a line integral of a one-form on parameter space; it does not refer to the rate at which the path is traversed. Replacing $R(t)$ by a reparametrization of the same curve leaves $\gamma_n$ unchanged, while the dynamical phase $-\frac{1}{\hbar}\int E_n\,dt$ scales with the duration. This is the precise sense in which the second phase is **geometric** and the first is not; the speed-independence is checked explicitly on the example below.

The eigenstate is defined only up to a phase, so the integrand is not a gauge-invariant object by itself. Writing $|n\rangle \mapsto e^{i\alpha(R)}|n\rangle$ for a real function $\alpha$ whose phase factor $e^{i\alpha}$ is single-valued, the phase acquired around a **closed** loop shifts by

$$
\oint \nabla_R\alpha\cdot dR = 2\pi k , \qquad k \in \mathbb{Z},
$$

an integer multiple of $2\pi$. The closed-loop phase is therefore well defined **modulo $2\pi$**, and that is the most that the geometry alone can say. The connection and its curvature, introduced in the next two sections, are the objects that make the statement precise.

For a two-level system in the biquaternion framework, the relevant Hamiltonian is

$$
\tilde{H}(\mathbf{R}) = \tfrac12\, i\,\mathbf{R} = \tfrac12\, i\,(R_1 e_1 + R_2 e_2 + R_3 e_3) \in \mathbb{M}_+ ,
\qquad \mathbf{R} \in \mathbb{R}^3 ,
$$

which under the isomorphism $e_0 \mapsto I$, $e_j \mapsto -i_{\mathrm{mat}}\sigma_j$ (where $i_{\mathrm{mat}}$ is the matrix imaginary, the image of the scalar imaginary $i$) maps to the standard spin Hamiltonian $\tfrac12\mathbf{R}\cdot\boldsymbol{\sigma}$. Its spectral decomposition is the one inherited from the parent article,

$$
\tilde{H} = \tfrac{R}{2}\,\tilde{P}_+(\hat{\mathbf{R}}) - \tfrac{R}{2}\,\tilde{P}_-(\hat{\mathbf{R}}) ,
\qquad
\tilde{P}_\pm(\hat{\mathbf{R}}) = \tfrac12\bigl(e_0 \pm i\hat{\mathbf{R}}\bigr) ,
\qquad
\hat{\mathbf{R}} = \mathbf{R}/R ,
$$

with $R = |\mathbf{R}|$. The eigenvalues are $\pm R/2$, so the **gap is $\Delta = R$**, and it closes exactly at $\mathbf{R} = 0$. Both the spectral decomposition and the eigenvalue formula are verified below by direct biquaternion multiplication.

**Parameter space.** The eigenstate $\tilde{P}_\pm(\hat{\mathbf{R}})$ depends on $\mathbf{R}$ only through the unit direction $\hat{\mathbf{R}}$, and on the scalar part $h_0$ not at all (the parent article shows that a central phase cancels from the state). The magnitude $R$ sets the gap but not the eigenstate. The parameter space that matters is therefore the unit sphere

$$
\mathcal{P} = \{\hat{\mathbf{R}} \in \mathbb{R}^3 : |\hat{\mathbf{R}}| = 1\} = S^2 ,
$$

which is exactly the **Bloch sphere** of pure states of $\mathbb{M}_+$. This is a structural feature of the two-level framework: the parameter space of the Hamiltonians modulo their trivial parts is the space of idempotents of the informational sector, i.e. the state space of the qubit itself.

## The Eigenstate Is a Spinor, Not an Idempotent

The instantaneous eigenstate of $\tilde{H} = \tfrac12 i\mathbf{R}$ is the idempotent $\tilde{P}_\pm(\hat{\mathbf{R}})$. It is natural to try to build the Berry connection out of it. One cannot, and the reason is worth stating as a lemma, because it is the first place the framework's two notions of "state" separate.

**Lemma (the idempotent is blind to the connection).** Let $\tilde{P}(\lambda)$ be a smooth family of idempotents with $\mathrm{Tr}(\tilde{P}) = 1$. Then

$$
\mathrm{Tr}\!\left(\tilde{P}\,\partial_\mu\tilde{P}\right) = 0
\qquad\text{for every parameter } \lambda^\mu .
$$

**Proof.** Since $\tilde{P}^2 = \tilde{P}$, differentiating gives $\partial_\mu\tilde{P} = (\partial_\mu\tilde{P})\tilde{P} + \tilde{P}(\partial_\mu\tilde{P})$. Taking the trace and using cyclicity of the trace on $\mathbb{B} \cong M_2(\mathbb{C})$,

$$
\mathrm{Tr}(\partial_\mu\tilde{P}) = 2\,\mathrm{Tr}\!\left(\tilde{P}\,\partial_\mu\tilde{P}\right).
$$

But $\mathrm{Tr}(\tilde{P}) = 1$ is constant, so $\mathrm{Tr}(\partial_\mu\tilde{P}) = 0$, and hence $\mathrm{Tr}(\tilde{P}\partial_\mu\tilde{P}) = 0$. $\square$

The lemma is not special to the qubit: it is the algebraic statement that a rank-one projector carries no phase information. For the idempotent $\tilde{P}_+(\hat{\mathbf{R}}) = \tfrac12(e_0 + i\hat{\mathbf{R}})$ it can also be checked directly, since $\partial_\mu\tilde{P}_+ = \tfrac12 i\,\partial_\mu\hat{\mathbf{R}}$ and $\mathrm{Sc}\bigl((e_0 + i\hat{\mathbf{R}})\,\partial_\mu\hat{\mathbf{R}}\bigr) = \mathrm{Sc}(\partial_\mu\hat{\mathbf{R}}) + i\,\mathrm{Sc}(\hat{\mathbf{R}}\,\partial_\mu\hat{\mathbf{R}}) = 0$, using $\hat{\mathbf{R}}\cdot\partial_\mu\hat{\mathbf{R}} = 0$ from $|\hat{\mathbf{R}}| = 1$. Both the general proof and the direct computation return zero.

The carrier of the Berry connection is therefore the **spinor** of the state module, not the density matrix. In the minimal left ideal $\mathbb{B}\tilde{P}_3$ generated by $\tilde{P}_3 = \tfrac12(e_0 + ie_3)$, the spin-up eigenstate of $\tfrac12 i\mathbf{R}$ is

$$
\psi_+(\theta,\phi) = \cos\tfrac{\theta}{2}\,E_{11} + e^{i\phi}\sin\tfrac{\theta}{2}\,E_{21}
\;\;\longleftrightarrow\;\;
\psi_+ = \tfrac12\cos\tfrac{\theta}{2}\bigl(e_0 + ie_3\bigr) + \tfrac12 e^{i\phi}\sin\tfrac{\theta}{2}\bigl(ie_1 + e_2\bigr) ,
$$

where $\hat{\mathbf{R}} = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$ and $E_{11}, E_{21}$ are the matrix units of the isomorphism. The right-hand expression is an element of $\mathbb{B}$, the left-hand expression its matrix image; the two are the same object written in two notations. That $\psi_+$ does lie in the ideal, that it is normalized, that it reproduces the idempotent, and that it is the eigenvector, are all verified by direct multiplication below.

**The bilinear relation.** The two notions of state are related by

$$
\tilde{P}_+(\hat{\mathbf{R}}) = \frac{\psi_+(\theta,\phi)\,\psi_+(\theta,\phi)^\dagger}{\mathrm{Tr}\!\left(\psi_+^\dagger\psi_+\right)} ,
$$

which is the parent article's $\tilde{\rho} = \psi\psi^\dagger/\mathrm{Tr}(\psi^\dagger\psi)$. The density matrix forgets the phase of $\psi_+$; the lemma says precisely that this forgotten phase is what the Berry connection measures. So the Berry phase is a property of the **state module** of the framework, not of the Bloch ball.

## The Berry Connection in Biquaternion Form

With the spinor in hand, the connection is defined by the trace pairing of the framework. For a normalized spinor $\psi(R) \in \mathbb{B}\tilde{P}$ depending smoothly on the parameters,

$$
\boxed{\;
\mathcal{A}_\mu(R) \;=\; i\;\frac{\mathrm{Tr}\!\left(\psi^\dagger\,\partial_\mu\psi\right)}{\mathrm{Tr}\!\left(\psi^\dagger\psi\right)}
\;}
\qquad\text{with}\qquad \partial_\mu = \frac{\partial}{\partial R^\mu}.
$$

This is the standard Berry connection, written through the trace. Under the isomorphism, the quotient is the column-vector inner product $\langle\psi|\partial_\mu\psi\rangle$ divided by $\langle\psi|\psi\rangle$; in the algebra it is the same number, computed by the trace formula $\mathrm{Tr}(X) = 2\,\mathrm{Sc}(X)$ inherited from the read list. The definition uses the pairing that gives the Born rule, which is a structural point and not a coincidence of notation: the connection and the Born rule are two readings of one bilinear form on the state module.

**Reality.** For normalized $\psi$, $\mathrm{Tr}(\psi^\dagger\psi) = 1$ is constant, so differentiating gives

$$
\mathrm{Tr}\!\left(\partial_\mu\psi^\dagger\,\psi\right) + \mathrm{Tr}\!\left(\psi^\dagger\partial_\mu\psi\right) = 0 .
$$

The first term is the conjugate of the second (complex conjugation in $\mathbb{C}_{\mathbb{B}}$ reverses the order under the trace), so $\mathrm{Tr}(\psi^\dagger\partial_\mu\psi)$ is purely imaginary and $i$ times it is real. The connection is therefore a **real one-form** on parameter space. It is not an element of $\mathbb{M}_-$ and not a biquaternion: it is a real number attached to each direction in parameter space.

**Gauge transformation.** Let $\alpha(R)$ be a real function and let $\psi \mapsto \psi' = e^{i\alpha}\psi$. Because $e^{i\alpha}$ is central and unitary, it multiplies $\psi$ from the left without ordering ambiguity, and

$$
\begin{aligned}
\mathrm{Tr}\!\left(\psi'^\dagger\partial_\mu\psi'\right)
&= \mathrm{Tr}\!\left(e^{-i\alpha}\psi^\dagger\left(i\,\partial_\mu\alpha\,e^{i\alpha}\psi + e^{i\alpha}\partial_\mu\psi\right)\right) \\
&= i\,\partial_\mu\alpha\;\mathrm{Tr}\!\left(\psi^\dagger\psi\right) + \mathrm{Tr}\!\left(\psi^\dagger\partial_\mu\psi\right).
\end{aligned}
$$

Dividing by the norm and multiplying by $i$ gives

$$
\boxed{\;\mathcal{A}'_\mu = \mathcal{A}_\mu - \partial_\mu\alpha\;}
\qquad\text{for}\qquad \psi' = e^{i\alpha}\psi .
$$

This is the transformation law of an **abelian gauge connection**. It is the same law as the electromagnetic gauge transformation $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ of *The Gauge Principle in Biquaternionic Form*, and the same law as the electromagnetic Berry connection of the standard theory. The rest of this section makes the analogy precise and states its limits.

### Why the Analogy Is Structural and Not Decorative

The gauge-principle article derives its abelian connection from a precise algebraic object: the **center** $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ of the algebra, whose unitary part is $U(1) = \{e^{i\theta}\}$. The phase $\lambda = e^{iq\Gamma/\hbar}$ it localizes is a **central unitary element**. The rephasing $e^{i\alpha}$ of the eigenstate is also a central unitary element, of the same group. The two constructions therefore select the same structure group inside the same algebra,

$$
U(1) = U(\mathbb{C}_{\mathbb{B}}) \subset \mathbb{C}_{\mathbb{B}} \subset \mathbb{B} ,
$$

and the same additive transformation law. In this precise sense the Berry connection is a gauge connection **of the same type** as the one the framework supplies for electromagnetism. What differs is everything else:

| | Gauge-principle connection $\tilde{A}$ | Berry connection $\mathcal{A}$ |
|---|---|---|
| Base space | spacetime (the material sector) | parameter space $\mathcal{P} = S^2$ (the Bloch sphere) |
| Kind of object | a biquaternion in $\mathbb{M}_-$ | a real scalar one-form on $\mathcal{P}$ |
| Structure group | $U(1) = U(\mathbb{C}_{\mathbb{B}})$ | $U(1) = U(\mathbb{C}_{\mathbb{B}})$ |
| Origin | localizing the central phase symmetry of a field equation | the rephasing freedom of an instantaneous eigenstate |
| Transformation | $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ | $\mathcal{A}' = \mathcal{A} - d\alpha$ |
| Curvature | $\tilde{F} = \mathrm{Vect}\!\left(\bar{\tilde{\nabla}}\tilde{A}\right)$, $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ | $\mathcal{F}_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu$ |

The two connections share their structure group, their transformation law, and their definition of curvature; they are not the same field. The Berry connection is not obtained from $\tilde{A}$, does not live on spacetime, and is not $\mathbb{M}_-$-valued. It is literally the standard Berry connection, and its relation to the framework's electromagnetic connection is an analogy — an exact analogy of gauge-theoretic type, but an analogy nonetheless. The question is returned to in the section *What the Framework Supplements and What Is Only Analogy*.

### The Integer Ambiguity

The transformation law has an immediate consequence for the holonomy. For a closed loop $\mathcal{C}$,

$$
\gamma = \oint_{\mathcal{C}}\mathcal{A}_\mu\,dR^\mu
\;\longmapsto\;
\gamma - \oint_{\mathcal{C}}\partial_\mu\alpha\,dR^\mu
= \gamma - \oint_{\mathcal{C}} d\alpha .
$$

If $e^{i\alpha}$ is single-valued on the loop, the last integral is $2\pi k$ for some integer $k$, the winding number of $e^{i\alpha}$ around the loop. A single-valued rephasing of the eigenstate therefore shifts the closed-loop phase by $2\pi k$ and nothing more, so the **gauge-invariant content is the phase modulo $2\pi$**. This is the first of the article's traps, and it is now a statement about the transition functions of a $U(1)$ bundle rather than about the arbitrariness of a wave function. The curvature below is the object that removes the ambiguity at the level of the integrand.

## The Berry Curvature

The **Berry curvature** is the exterior derivative of the connection,

$$
\mathcal{F}_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu .
$$

It is invariant under the rephasing, because the added term is a gradient:

$$
\mathcal{F}'_{\mu\nu} = \mathcal{F}_{\mu\nu} - \left(\partial_\mu\partial_\nu\alpha - \partial_\nu\partial_\mu\alpha\right) = \mathcal{F}_{\mu\nu} .
$$

This is the same abelian curvature $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ that appears in the gauge-principle article as the field strength of the connection, now on parameter space rather than on spacetime. For a three-dimensional parameter space, as here, the curvature is naturally a vector via the Hodge dual, $\mathcal{F}_k = \tfrac12\epsilon_{kij}\mathcal{F}_{ij}$.

**The two routes to the phase.** For a closed loop $\mathcal{C} = \partial\mathcal{S}$ bounding a surface $\mathcal{S}$ on which the connection is smooth, Stokes' theorem gives

$$
\oint_{\mathcal{C}}\mathcal{A}_\mu\,dR^\mu = \int_{\mathcal{S}}\mathcal{F}_{\mu\nu}\,dS^{\mu\nu} .
$$

The left-hand route integrates the connection; the right-hand route integrates the curvature. Both are used on the example below, and their agreement is what the phrase "the phase is the flux of the curvature" means. The smoothness qualification is not cosmetic: on the sphere the connection has a Dirac-string singularity in any single coordinate patch, and the surface must be chosen in a patch where the connection is regular. The next section exhibits this explicitly, because it is also the mechanism by which the $2\pi$ ambiguity of the previous section appears.

It is worth recording that the curvature is a **local** object while the connection is not. The lemma of the previous section says that the curvature cannot be written as $\mathrm{Tr}(\tilde{P}\,d\tilde{P})$ either — like the connection, it requires the spinor. What the idempotent loses is the connection; what it never had is the phase.

## The Two-Level Example: Spin-1/2 in a Slowly Rotating Field

Take a spin-1/2 in a magnetic field whose direction rotates at a fixed polar angle, so that in the biquaternion framework

$$
\tilde{H}(t) = \tfrac12\,i\,\mathbf{R}(t) , \qquad
\mathbf{R}(t) = R\bigl(\sin\theta_0\cos\omega t,\ \sin\theta_0\sin\omega t,\ \cos\theta_0\bigr) ,
$$

with $R > 0$ and $\theta_0 \in (0,\pi)$ fixed. The path is the circle $\theta = \theta_0$ on the Bloch sphere, traversed once per period $T = 2\pi/\omega$, and the gap is $\Delta = R$ everywhere on the path, so the adiabatic theorem applies provided the rotation is slow compared with the gap, $\hbar\omega \ll R$. The parameter $\phi = \omega t$ runs from $0$ to $2\pi$.

The spin-up spinor is $\psi_+$ of the previous section with $\theta = \theta_0$. Its connection is computed by direct application of the definition, and the result is

$$
\mathcal{A}_\theta = 0 , \qquad
\mathcal{A}_\phi = -\sin^2\frac{\theta}{2} = -\frac{1-\cos\theta}{2} .
$$

The component $\mathcal{A}_\theta$ vanishes because $\psi_+$ depends on $\theta$ only through the real factors $\cos(\theta/2)$ and $\sin(\theta/2)$, whose contributions to $\langle\psi|\partial_\theta\psi\rangle$ cancel; the component $\mathcal{A}_\phi$ comes from the phase $e^{i\phi}$, giving $\langle\psi|\partial_\phi\psi\rangle = i\sin^2(\theta/2)$ and hence $\mathcal{A}_\phi = -\sin^2(\theta/2)$. Written as a one-form,

$$
\mathcal{A} = -\frac{1-\cos\theta}{2}\,d\phi ,
$$

which is regular at the north pole $\theta = 0$ and singular at the south pole. The singularity is the **Dirac string** of this connection: no single expression for $\mathcal{A}$ is smooth on the whole sphere, and a second patch is needed near the south pole. The curvature needs no patch:

$$
\mathcal{F} = d\mathcal{A} = -\frac{1}{2}\sin\theta\; d\theta \wedge d\phi ,
\qquad
\mathcal{F}_{\theta\phi} = \partial_\theta\mathcal{A}_\phi = -\frac{\sin\theta}{2} .
$$

**Route 1: the line integral.** The loop is at fixed $\theta_0$, so

$$
\gamma_+ = \oint_{\mathcal{C}}\mathcal{A}_\mu\,dR^\mu = \int_0^{2\pi}\mathcal{A}_\phi\big|_{\theta_0}\,d\phi
= -\frac{1-\cos\theta_0}{2}\cdot 2\pi
= -\frac{\Omega}{2} ,
$$

where

$$
\Omega = 2\pi\bigl(1-\cos\theta_0\bigr)
$$

is the solid angle of the spherical cap bounded by the loop.

**Route 2: the surface integral.** The same loop bounds the north cap $0 \le \theta \le \theta_0$, on which the connection above is regular. Integrating the curvature,

$$
\int_{\mathcal{S}}\mathcal{F} = \int_0^{\theta_0}\!\!\int_0^{2\pi} -\frac{\sin\theta}{2}\,d\theta\,d\phi
= -\frac{1}{2}\cdot 2\pi\bigl(1-\cos\theta_0\bigr) = -\frac{\Omega}{2} .
$$

The two routes agree, and they agree for **every** $\theta_0$, not merely at the value used to construct either expression. The agreement is a check of the pair of formulas against each other on a one-parameter family of loops; written out numerically for five values of $\theta_0$,

| $\theta_0$ | $30^\circ$ | $60^\circ$ | $90^\circ$ | $120^\circ$ | $150^\circ$ |
|---|---|---|---|---|---|
| $\gamma_+$ (line) | $-0.4209$ | $-1.5708$ | $-3.1416$ | $-4.7124$ | $-5.8623$ |
| $\gamma_+$ (surface) | $-0.4209$ | $-1.5708$ | $-3.1416$ | $-4.7124$ | $-5.8623$ |

The equator, $\theta_0 = \pi/2$, is the case $\gamma_+ = -\pi$; the half-angle form $-\Omega/2$ is the standard spin-1/2 result, with the sign convention that the spin-up branch is the one followed.

**Speed independence.** Replacing the uniform rotation $\phi = \omega t$ by a non-uniform $\phi(t) = 2\pi(t/T)^3$ with the same endpoints changes nothing in either route: the line integral is $\int_0^{2\pi}\mathcal{A}_\phi\,d\phi$ once the substitution is made, and the numerical value is again $-\pi$ at the equator and $-\Omega/2$ generally. The dynamical phase over the same period is $-\frac{1}{\hbar}\int_0^T \frac{R}{2}\,dt = -\frac{RT}{2\hbar}$, which scales with $T$; the geometric phase does not. The contrast is the definition of the word "geometric".

**The $2\pi$ ambiguity, exhibited.** The spin-down branch makes the patch structure visible. In the gauge adapted to the north pole the spin-down connection is

$$
\mathcal{A}^{(-)}_\phi = +\frac{1-\cos\theta}{2} ,
$$

giving $\gamma_- = +\Omega/2$. In the gauge adapted to the south pole the same band has $\mathcal{A}^{(-)}_\phi = -\cos^2(\theta/2)$, which differs from the first by exactly $1$. Around the equator loop the two expressions give phases differing by $2\pi$: $+\pi$ against $-\pi$. Both are legitimate local descriptions of the same band, they differ by the non-single-valued phase $e^{-i\phi}$ on the overlap, and they define the same curvature, $+\tfrac12\sin\theta\,d\theta\wedge d\phi$. The physical content is the pair of statements $\gamma_- - \gamma_+ = \Omega$ and $\gamma_\pm$ defined modulo $2\pi$; stating either phase as a single absolute real number requires choosing a patch, and the choice is not physical. This is the first trap of the introduction, made concrete.

**What was checked, and on what case.** The spinor normalization $\mathrm{Tr}(\psi_+^\dagger\psi_+) = 1$; the reproduction $\psi_+\psi_+^\dagger = \tilde{P}_+(\hat{\mathbf{R}})$ of the idempotent; the eigenvalue equation $\tilde{H}\psi_+ = \tfrac{R}{2}\psi_+$; the spectral decomposition $\tilde{H} = \tfrac{R}{2}\tilde{P}_+ - \tfrac{R}{2}\tilde{P}_-$; the connection components above; the curvature; the two routes and their agreement on the five loops; the speed independence on a non-uniform reparametrization; and the $2\pi$ shift between the two patches of the spin-down band. All were recomputed in exact arithmetic from the quaternion multiplication rules, and the two-route agreement was in addition recomputed independently by numerical quadrature. No formula in this article rests on a single case chosen to fit it.

## Quantisation on a Closed Surface

The example of the previous section computed a flux over a **cap** and found it continuous in the loop: $-\pi(1-\cos\theta_0)$, which ranges continuously from $0$ to $-2\pi$ as $\theta_0$ goes from $0$ to $\pi$. An open surface therefore does not quantise anything — the phase on a loop is a continuous geometric quantity, and that is all.

The situation is different for a **closed** surface. Integrating the spin-up curvature over the whole Bloch sphere,

$$
\int_{S^2}\mathcal{F} = \int_0^{\pi}\!\!\int_0^{2\pi} -\frac{\sin\theta}{2}\,d\theta\,d\phi = -2\pi ,
$$

so the **first Chern number** of the spin-up eigenbundle is the integer

$$
C_+ = \frac{1}{2\pi}\int_{S^2}\mathcal{F} = -1 .
$$

For the spin-down branch, in the gauge adapted to the north pole, the curvature is $+\tfrac12\sin\theta\,d\theta\wedge d\phi$ and $C_- = +1$. The two curvatures are equal and opposite at every point,

$$
\mathcal{F}^{(+)} + \mathcal{F}^{(-)} = 0 ,
$$

and the Chern numbers sum to zero. This is required: a rank-two bundle over $S^2$ whose two eigenlines are complementary has total first Chern number zero, because its determinant line is trivial. The check on the second band is a case that the first band did not supply, and it is the two-band completeness relation, not the single-band computation, that fixes the relative sign.

**Why the closed surface matters, and why it can be closed.** The closed-surface integral is a **topological** statement, not a statement about the loop. The curvature is the field of a point source at the origin of parameter space. Writing $\hat{\mathbf{R}} = \mathbf{R}/R$, the spin-up curvature three-vector is

$$
\boldsymbol{\mathcal{F}} = -\frac{1}{2}\,\frac{\hat{\mathbf{R}}}{R^2} ,
$$

the field of a **monopole of charge $g = -1/2$** located at $\mathbf{R} = 0$, and the Chern number is twice the charge, $C_+ = 2g = -1$. But $\mathbf{R} = 0$ is exactly where the two levels become degenerate and the gap closes; the connection and the adiabatic theorem both fail there. The Bloch sphere at a fixed magnitude $R$ avoids the origin, which is why the integral over it is well defined, and the integer it computes counts the degeneracies enclosed. If the surface were allowed to pass through $\mathbf{R} = 0$, or if the gap closed anywhere on it, the integral would not be defined. Quantisation, closedness, and the non-closing gap are therefore one requirement, not three.

**Robustness under deformation.** The integer cannot change under a deformation of the Hamiltonian that keeps the gap open. To see this within the two-level family, let the direction field be distorted by a monotone function $\Theta(\theta)$ with $\Theta(0) = 0$ and $\Theta(\pi) = \pi$. The connection is again $\mathcal{A}_\phi = -\sin^2(\Theta/2)$ and the curvature is

$$
\mathcal{F} = -\frac{1}{2}\sin\Theta\;\frac{d\Theta}{d\theta}\; d\theta\wedge d\phi ,
$$

whose integral over the sphere is

$$
-\frac{1}{2}\cdot 2\pi\int_0^{\pi}\sin\Theta\,\frac{d\Theta}{d\theta}\,d\theta
= -\frac{1}{2}\cdot 2\pi\bigl[-\cos\Theta\bigr]_0^{\pi}
= -\frac{1}{2}\cdot 2\pi\cdot 2 = -2\pi ,
$$

independent of $\Theta$. The specific family $\Theta(\theta) = \theta + s\sin\theta$, monotone for $|s| < 1$, was checked at $s = 0, \tfrac12, -\tfrac34, \tfrac{9}{10}$ and gives $C_+ = -1$ at every value. Equivalently, for a general nonvanishing smooth $\mathbf{b}(\hat{\mathbf{R}})$, the spin-up curvature is $-\tfrac12$ times the pullback of the area form of $S^2$ by the map $\hat{\mathbf{b}} : S^2 \to S^2$, and its integral is $-2\pi$ times the degree of that map. The degree is an integer that a continuous deformation cannot change without the map passing through zero somewhere — that is, without the gap closing. The quantisation is thus protected by the same condition that makes the adiabatic theorem valid.

**Relation to the spacetime monopole, and its limit.** The algebraic shape here — a $U(1)$ curvature whose flux over a closed surface is quantised, with the integral counting a singularity — is the same shape that *The Magnetic Monopole in Biquaternionic Form* exhibits for the Dirac quantisation condition. The two are not the same statement, and the difference is the base space. There the monopole is a magnetic charge in space, its flux is an electromagnetic flux, and the quantisation condition $eg = 2\pi n\hbar c$ constrains the product of electric and magnetic charges. Here the "monopole" is a degeneracy point in the space of Hamiltonians, its flux is a Berry flux, and the integer is the degree of a map from the parameter sphere to itself. The two invocations of the same $U(1)$ curvature structure carry no established relation; the resemblance is recorded, and nothing is claimed to follow from it.

## Degenerate Levels and the Abelian Case

Every phase computed so far is a single real number modulo $2\pi$. That is the **abelian** case, and it holds because the traversed level is non-degenerate: the two eigenvalues $\lambda_\pm = h_0 \pm |\mathbf{h}|$ of the Hamiltonian are distinct, the eigenprojectors $\tilde{P}_\pm(\hat{\mathbf{h}})$ are rank one, and the adiabatic evolution acquires one phase, not a matrix of phases. The general adiabatic theorem for a degenerate level replaces the connection by a matrix-valued one-form and the phase by a unitary matrix on the degenerate subspace; that is the non-abelian, or Wilczek–Zee, case, and it is a genuinely different object.

**Which case is available here.** For a single-qubit Hamiltonian the degeneracy condition is $h_0 + |\mathbf{h}| = h_0 - |\mathbf{h}|$, i.e. $|\mathbf{h}| = 0$, i.e. $\mathbf{h} = 0$. So the only degenerate Hamiltonian in $\mathbb{M}_+$ is a multiple of the identity, $\tilde{H} = h_0 e_0$, for which the two levels coincide and the eigenprojectors are not defined at all. That is the same point at which the gap closes and the adiabatic theorem fails. There is therefore **no non-degenerate level with a degeneracy** in a single-qubit framework: degeneracy and gap closing coincide, and the abelian case is the only case. The non-abelian Berry phase requires a level of dimension greater than one separated from the rest of the spectrum, which in this framework means at least three levels, hence at least $\mathbb{B}^{\otimes n}$ for $n \geq 2$. The parent article leaves the tensor product $\mathbb{B}^{\otimes_\mathbb{C} n} \cong M_{2^n}(\mathbb{C})$ as an open question, so the non-abelian case is out of reach of the present article and is recorded as a gap rather than approximated.

This is a case where the framework's smallness is informative rather than limiting: the reason the Berry phase is abelian here is not a choice of convenience but a fact about a two-level algebra, and the reason it cannot be made non-abelian is the same fact.

## What the Framework Supplements and What Is Only Analogy

The question left open in the introduction can now be answered precisely. **The biquaternion framework's connection is not the Berry connection, and the Berry connection is not its connection.** The two statements are different and both matter.

**The Berry connection is literally the standard one.** Written in the algebra it is

$$
\mathcal{A}_\mu = i\,\frac{\mathrm{Tr}\!\left(\psi^\dagger\partial_\mu\psi\right)}{\mathrm{Tr}\!\left(\psi^\dagger\psi\right)} ,
$$

and under the isomorphism this is the standard expression $i\langle\psi|\partial_\mu\psi\rangle/\langle\psi|\psi\rangle$ on $\mathbb{C}^2$. No new field is introduced and no new phase is predicted: the biquaternion article and the standard article compute the same numbers, as the two-route check on the rotating field demonstrates. The framework's contribution to the *object* is notational.

**The relation to the framework's own connection is an analogy.** The abelian connection $\tilde{A}$ of *The Gauge Principle in Biquaternionic Form* is a biquaternion-valued field on spacetime, obtained from localizing the central phase symmetry of a field equation. The Berry connection is a real one-form on parameter space, obtained from the rephasing freedom of an instantaneous eigenstate. They are of the same *gauge type* — same structure group $U(1) = U(\mathbb{C}_{\mathbb{B}})$, same transformation law, same curvature definition — but they are different objects on different base spaces, and the framework does not identify them. Anyone who reads the shared $U(1)$ as an identity has read more than is there.

What the framework does supply, beyond the rewriting, is a set of structural placements.

- **The parameter space is the state space.** For the two-level Hamiltonian the effective parameter space is the Bloch sphere $S^2$, which is the manifold of idempotents $\tilde{P}_+(\hat{\mu})$ of $\mathbb{M}_+$ — the pure states of the informational sector. The Berry connection is thus a connection on a bundle over the space of pure states, and the Chern number is a property of that space's topology. This is a genuine placement: the framework names both the state space and the parameter space as the same canonical object.
- **One pairing for the Born rule and the connection.** Both $\mathrm{Tr}(\tilde{P}\tilde{H})$ and $\mathcal{A}_\mu$ are built from the trace pairing of the state module; the framework makes it visible that the Born rule and the Berry connection are two readings of one bilinear form.
- **The structure group is already in the algebra.** The $U(1)$ of the Berry phase is the unitary part of the center $\mathbb{C}_{\mathbb{B}}$ — the same group, in the same algebra, that the gauge-principle article attaches to electromagnetism. The framework does not have to be supplied with a phase group; it has one.
- **The connection requires the spinor, not the density matrix.** The lemma $\mathrm{Tr}(\tilde{P}\partial_\mu\tilde{P}) = 0$ is the cleanest form of the statement that the geometric phase is a property of the state vector's phase, not of the Bloch-ball point. The framework forces the distinction between the spinor and the idempotent that the algebraic formulation otherwise leaves implicit.
- **The same scalar imaginary.** The $i$ in $\mathcal{A} = i\langle\psi|d\psi\rangle$ is the central scalar imaginary that also appears in $ict$, in the gauge phase $e^{iq\Gamma/\hbar}$, and as the complex structure of the state module. The gauge-principle article flagged the shared generator as possibly vacuous because the phase is central; the Berry connection adds a third appearance without resolving the question. It is recorded as an observation, not a result.

**What is only transcribed.** The adiabatic theorem, the Berry phase formula, the Stokes relation, and the Chern-number quantisation are standard results carried into the algebra. The framework supplies the $\hbar$ from outside, as the monopole article notes: until the single-valuedness of a phase is imposed, the algebra is a classical complexified structure. The integer $C = \pm 1$ is a fact about the degree of a map of $S^2$, not a fact about $\mathbb{B}$. For a single qubit this article reports a reformulation and no new physics.

## Open Questions

1. **The non-abelian case.** The Wilczek–Zee phase needs a degenerate level separated from the rest of the spectrum. In a single qubit this is impossible; it requires $\mathbb{B}^{\otimes_\mathbb{C} n}$, whose tensor product the parent article leaves open. Does the framework's own non-commutativity supply a natural matrix-valued connection on a many-qubit state module, and if so is it the standard one?

2. **A $\mathbb{B}$-valued geometric phase.** The connection defined here is $U(1)$-valued because the eigenstate's rephasing freedom is central. Could a non-central, $\mathbb{B}$-valued connection on the state module define a geometric phase intrinsic to the algebra, without tensor products? The non-abelian gauge structure of the gauge-principle article suggests the algebra has the wherewithal; nothing here constructs it.

3. **Parameter-space and spacetime monopoles.** The Berry curvature is the field of a point degeneracy in parameter space, and the monopole article treats a magnetic charge in space. Both produce quantised $U(1)$ flux. Is there a relation beyond the shared algebraic shape? None is established; it is recorded as a question.

4. **The local complex structure.** The series makes the spacetime complex structure local through $c = 1/\sqrt{\epsilon\mu}$, while the scalar imaginary $i$ of the state module is a global central element. If the complex structure is local, does the Berry phase — which uses $i$ as the complex structure of the state module — see the local structure? *The Schrödinger Equation in Biquaternionic Form* records the same tension as an open question, and this article inherits it.

5. **The relativistic Berry phase.** The spinor module of $\mathbb{B}$ carries a Lorentz action and the framework contains a biquaternion Dirac equation. What is the geometric phase of a relativistic spinor under an adiabatic Lorentz transformation, and does the boost (non-unitary) part contribute? Not addressed here.

6. **Empirical content.** The Berry phase is observable in interference experiments. The reformulation predicts exactly what the standard theory predicts; whether the framework's additional structure implies any deviation is, as everywhere in the series, the open question.

## Summary

The Berry phase is the geometric phase acquired by an adiabatic eigenstate around a closed loop in parameter space. It is computed by two equivalent routes, the line integral of the **Berry connection** and the surface integral of the **Berry curvature**, and it is defined modulo $2\pi$ because a rephasing of the eigenstate is a gauge transformation.

In the biquaternion framework the instantaneous eigenstate of $\tilde{H} = \tfrac12 i\mathbf{R}$ is the idempotent $\tilde{P}_\pm(\hat{\mathbf{R}})$, but the idempotent is **blind** to the connection: $\mathrm{Tr}(\tilde{P}\partial_\mu\tilde{P}) = 0$ identically. The connection is carried by the **spinor** $\psi$ of the minimal left ideal $\mathbb{B}\tilde{P}$, and is defined by the trace pairing of the state module,

$$
\mathcal{A}_\mu = i\,\frac{\mathrm{Tr}\!\left(\psi^\dagger\partial_\mu\psi\right)}{\mathrm{Tr}\!\left(\psi^\dagger\psi\right)} ,
\qquad
\mathcal{A}'_\mu = \mathcal{A}_\mu - \partial_\mu\alpha
\quad\text{for}\quad \psi' = e^{i\alpha}\psi ,
\qquad
\mathcal{F}_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu .
$$

The structure group is the unitary part of the center $\mathbb{C}_{\mathbb{B}}$, the same $U(1)$ that the gauge-principle article attaches to the algebra, and the transformation law is the same additive law as $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$. The relation between the two connections is an exact **analogy of gauge type**, not an identity: they live on different base spaces, are objects of different kinds, and the framework does not equate them.

On spin-1/2 in a slowly rotating field with the loop at polar angle $\theta_0$, the connection is $\mathcal{A} = -\tfrac{1-\cos\theta}{2}d\phi$, the curvature is $\mathcal{F} = -\tfrac12\sin\theta\,d\theta\wedge d\phi$, and both routes give $\gamma_+ = -\Omega/2$ for every $\theta_0$, where $\Omega = 2\pi(1-\cos\theta_0)$ is the solid angle of the loop. The phase is independent of the speed of traversal, unlike the dynamical phase. The two spin branches have equal and opposite curvatures and Chern numbers $C_\pm = \mp 1$, summing to zero. Over a **closed** surface the flux is quantised as the Chern number and is robust under gap-preserving deformations; over an open cap it is the continuous solid angle, so the quantisation is specifically a closed-surface statement, and the surface must avoid the degeneracy point $\mathbf{R} = 0$ where the gap closes and the connection is singular. That point is the parameter-space monopole, distinct from the spacetime monopole of the companion article, though the two share the algebraic shape of a quantised $U(1)$ flux.

The level is non-degenerate throughout, so the phase is abelian; the non-abelian (degenerate-level) case is unavailable in a single-qubit framework, where degeneracy and gap closing coincide, and it is left as a gap together with the many-qubit tensor product. For a single qubit the article is a reformulation; its structural content is that the parameter space is the Bloch sphere of $\mathbb{M}_+$, that the connection and the Born rule come from one trace pairing, that the connection requires the spinor rather than the density matrix, and that the $U(1)$ of the phase is the center of the algebra rather than an imported group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, central; complex structure of the state module |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Center of the algebra; $U(1) = U(\mathbb{C}_{\mathbb{B}})$ its unitary part |
| $\mathbb{M}_+, \mathbb{M}_-$ | Hermitian (informational) and anti-Hermitian (material) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\tilde{H} = h_0 e_0 + i\mathbf{h}$ | Hermitian Hamiltonian (observable) |
| $\tilde{P}_\pm(\hat{\mu}) = \tfrac12(e_0 \pm i\hat{\mu})$ | Idempotent (pure state / eigenprojector) |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (Born rule and the pairing used for the connection) |
| $\mathbb{B}\tilde{P}$ | Minimal left ideal; the state module of spinors $\psi$ |
| $\psi_\pm$ | Normalized instantaneous eigen-spinor |
| $\tilde{\rho} = \psi\psi^\dagger/\mathrm{Tr}(\psi^\dagger\psi)$ | Density matrix associated to a spinor |
| $\mathbf{R}$, $R = \lvert\mathbf{R}\rvert$, $\hat{\mathbf{R}}$ | Parameter vector, its magnitude, its direction; $\hat{\mathbf{R}} \in S^2$ |
| $\mathcal{P} = S^2$ | Parameter space = Bloch sphere of $\mathbb{M}_+$ |
| $\theta, \phi$ | Polar and azimuthal angles on the Bloch sphere |
| $\mathcal{A}_\mu$ | Berry connection, $i\,\mathrm{Tr}(\psi^\dagger\partial_\mu\psi)/\mathrm{Tr}(\psi^\dagger\psi)$ |
| $\mathcal{A}'_\mu = \mathcal{A}_\mu - \partial_\mu\alpha$ | Gauge transformation of the Berry connection |
| $\mathcal{F}_{\mu\nu} = \partial_\mu\mathcal{A}_\nu - \partial_\nu\mathcal{A}_\mu$ | Berry curvature |
| $\gamma_\pm$ | Berry phase of the spin-up / spin-down band |
| $\Omega = 2\pi(1-\cos\theta_0)$ | Solid angle of the cap bounded by the loop |
| $\Delta = R$ | Spectral gap; closes at $\mathbf{R} = 0$ |
| $C_\pm = \mp 1$ | First Chern numbers of the two bands over $S^2$ |
| $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ | Gauge-principle connection and its transformation (for contrast) |

## Further Reading

- M. V. Berry, "Quantal phase factors accompanying adiabatic changes," *Proceedings of the Royal Society of London A* **392** (1984) 45–57, for the original geometric phase.
- B. Simon, "Holonomy, the quantum adiabatic theorem, and Berry's phase," *Physical Review Letters* **51** (1983) 2167–2170, for the fibre-bundle formulation and the connection.
- F. Wilczek and A. Zee, "Appearance of gauge structure in simple dynamical systems," *Physical Review Letters* **52** (1984) 2111–2114, for the non-abelian phase of a degenerate level.
- Y. Aharonov and J. Anandan, "Phase change during a cyclic quantum evolution," *Physical Review Letters* **58** (1987) 1593–1596, for the non-adiabatic generalisation.
- A. Shapere and F. Wilczek, *Geometric Phases in Physics* (World Scientific, 1989), for the collected theory and its applications.
- M. Nakahara, *Geometry, Topology and Physics* (Institute of Physics, 2003), for connections, curvature, Chern numbers, and the monopole analogy.
- The companion articles of this series: *Introduction to the Biquaternion Universe*, *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, *Quantum Mechanics in Biquaternionic Form*, *The Schrödinger Equation in Biquaternionic Form*, *Spin-1/2 Quantum Mechanics in Biquaternionic Form*, *Exercise: Spin Precession in a Magnetic Field*, *The Gauge Principle in Biquaternionic Form*, *The Covariant Derivative and Gauge Connection in Biquaternionic Form*, *The Magnetic Monopole in Biquaternionic Form*, and *Quantum Gates and Circuits in Biquaternionic Form*.
