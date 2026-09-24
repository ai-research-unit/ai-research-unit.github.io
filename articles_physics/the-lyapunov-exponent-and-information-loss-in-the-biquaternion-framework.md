# __The Lyapunov Exponent and Information Loss in the Biquaternion Framework__

## Introduction

A Lyapunov exponent is the rate at which a dynamical system loses track of its initial condition. Two trajectories that start a distance $\epsilon$ apart separate as $\epsilon\,e^{\lambda t}$, and $\lambda$ is the exponent; a positive exponent means exponential divergence, that is, sensitivity to initial conditions, and a negative exponent means exponential contraction, that is, the erasure of a distinction. The exponents are the rates in the information budget of a flow.

This article computes the Lyapunov exponents of the informational sector $\mathbb{M}_+$ of the biquaternion algebra, and locates the information loss of the framework in the sign of those exponents. The sector's state space is the Bloch ball, $\tilde{\rho} = \tfrac{1}{2}(e_0+i\mathbf{r})$ with $|\mathbf{r}|\le1$, and the natural measure of a tangent vector is the sector's norm form: a tangent vector to the state space is a traceless element of $\mathbb{M}_+$, and its norm form is negative definite there, so $|N(\delta\tilde{\rho})|^{1/2}$ is the length of the tangent vector. The Lyapunov exponent of a tangent vector is

$$
\lambda(v) = \lim_{t\to\infty}\frac{1}{2t}\log\frac{\left|N\!\left(\delta\tilde{\rho}(t)\right)\right|}{\left|N\!\left(\delta\tilde{\rho}(0)\right)\right|},
$$

the factor $\tfrac{1}{2}$ being present because the norm form is quadratic.

Two classes of dynamics are natural on the sector, and they exhaust what the framework's linear structure supplies. The **reversible** class is rotor conjugation, $\tilde{\rho}\mapsto\tilde{R}\tilde{\rho}\tilde{R}^\dagger$ with $\tilde{R}\tilde{R}^\dagger = e_0$, which is an isometry of the norm form; and the **irreversible** class is a semigroup of coarse-graining or dephasing channels, whose Bloch action is an affine contraction. The article's central statement is that both classes have **non-positive** Lyapunov spectra. The reversible class is exactly Lyapunov-neutral — every exponent is zero — and the irreversible class is contracting, with exponents set by the contraction coefficients of the channel. In particular the dephasing semigroup of strength $\Gamma$ has the spectrum

$$
\{0,\,-\Gamma,\,-\Gamma\},
$$

with the zero along the pointer axis and the two negative exponents in the plane transverse to it. Information is lost at the rate $\Gamma$ in each transverse direction. Because the norm form is quadratic, the scalar $|N(\delta\tilde{\rho}(t))|$ decays at twice that rate, $e^{-2\Gamma t}$; the Lyapunov exponent defined above carries the compensating factor $\tfrac{1}{2}$, so it is the decay rate of the length $\sqrt{|N|}$ and equals the vector exponent $-\Gamma$. The factor of two is a property of the quadratic form, not of the exponent.

The article also states what the framework does **not** produce: positive Lyapunov exponents. A positive exponent from linear dynamics would require an expansion, and an expansion carries states out of the Bloch ball, so the linear dynamics of the sector — an isometry in the reversible class, a contraction in the irreversible one — has a non-positive spectrum. The remaining dynamics of the framework is nonlinear, and it lives on a phase space too small to host chaos. The compact coadjoint orbit of the framework is the two-sphere $|\mathbf{S}| = \text{const}$ — the Bloch sphere at the spin-$\tfrac{1}{2}$ radius — a two-dimensional symplectic manifold, and every Hamiltonian flow on a two-dimensional symplectic manifold is integrable, so its exponents vanish; for a Hamiltonian flow a positive exponent first becomes possible at four phase-space dimensions, which the material sector supplies and the informational sector does not. The information loss of the framework is therefore **contraction, not chaos**: the entropy produced in a coarse-graining is the deficit of the contracting directions, and the Kolmogorov–Sinai entropy of the framework's linear flows is zero.

The treatment is classical and non-relativistic. The exponents are those of a classical flow on a state space, measured with the algebra's norm form. The tools imported are the standard ones of smooth dynamical systems: the multiplicative ergodic theorem, the contraction of completely positive trace-preserving maps, Pesin's formula, and the integrability of two-dimensional Hamiltonian flows. The connexion to the notion of information used elsewhere in the subcategory is direct: the entropy functional of the companion article *Coarse-Graining and the Biquaternion Entropy Functional* is a function of the norm form, and the Lyapunov exponent is the rate of decay of the logarithm of the norm form of a tangent vector; the two are the same quantity read at a point and along a flow.

The conventions are those of the companion articles. The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$; the scalar imaginary $i$ is central; the sectors are $\mathbb{M}_+$ (Hermitian, informational) and $\mathbb{M}_-$ (anti-Hermitian, material); the trace is $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$ with $\mathrm{Tr}(e_0) = 2$; the norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$; and a state is $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$.

## Lyapunov Exponents: The Standard Setting

### Definition for a Flow

Let $\phi_t$ be a smooth flow on a manifold $M$ and let $x(t) = \phi_t(x_0)$ be a trajectory. The linearisation of the flow about the trajectory is the family of tangent maps

$$
D\phi_t : T_{x_0}M \longrightarrow T_{x(t)}M ,
$$

and for a tangent vector $v\in T_{x_0}M$ the **Lyapunov exponent** is

$$
\lambda(v) = \lim_{t\to\infty}\frac{1}{t}\log\frac{\left\|D\phi_t\,v\right\|}{\left\|v\right\|},
$$

whenever the limit exists. The **multiplicative ergodic theorem** of Oseledets guarantees that, for an invariant measure, the limit exists for almost every initial condition and takes finitely many values $\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_n$, the **Lyapunov spectrum** of the flow. A positive exponent is exponential divergence of nearby trajectories; a negative exponent is exponential contraction; a zero exponent is neutrality, and the direction of the flow itself is always neutral.

### Three Standard Facts

Three facts are used below, and each is transcribed from the standard theory rather than re-derived.

**Divergence and volume.** The sum of the exponents is the average rate of change of the volume element,

$$
\sum_k \lambda_k = \lim_{t\to\infty}\frac{1}{t}\log\left|\det D\phi_t\right| = \left\langle \nabla\cdot f\right\rangle ,
$$

where $f$ is the vector field of the flow. For a Hamiltonian flow the divergence vanishes, the flow is volume-preserving, and the exponents come in pairs $\pm\lambda$ with the total zero. For a dissipative flow the sum is negative and the volume contracts.

**Pesin's formula.** For a smooth flow with an invariant measure, the Kolmogorov–Sinai entropy equals the sum of the positive exponents,

$$
h_{\rm KS} = \sum_{\lambda_k>0}\lambda_k .
$$

This is the precise sense in which positive Lyapunov exponents are the rate of *information production* of a chaotic flow: they are the rate at which the flow generates new distinctions.

**Two-dimensional Hamiltonian flows are integrable.** On a two-dimensional symplectic manifold the Hamiltonian is the only independent invariant, its level sets are curves, and the motion is periodic or quasi-periodic on them. Every Lyapunov exponent of such a flow vanishes. For a Hamiltonian flow, chaos — and with it a positive exponent — requires a phase space of dimension four or more, because the exponents pair as $\pm\lambda$ and sum to zero, so two dimensions force them all to vanish. The restriction to Hamiltonian flows matters: a dissipative flow need not pair its exponents, and three dimensions already suffice for chaos there.

## Reversible Rotor Flow Is Lyapunov-Neutral

The reversible evolution of the informational sector is rotor conjugation. Let $\tilde{R}(t)$ be a one-parameter family of matrix-unitary elements,

$$
\tilde{R}(t)\tilde{R}(t)^\dagger = \tilde{R}(t)^\dagger\tilde{R}(t) = e_0 ,
$$

generated by a skew-Hermitian element, $\tilde{R}(t) = \exp(t\tilde{G})$ with $\tilde{G}^\dagger = -\tilde{G}$. The state evolves by

$$
\tilde{\rho}(t) = \tilde{R}(t)\,\tilde{\rho}(0)\,\tilde{R}(t)^\dagger ,
$$

and the tangent map is the same conjugation acting on the traceless part,

$$
\delta\tilde{\rho}(t) = \tilde{R}(t)\,\delta\tilde{\rho}(0)\,\tilde{R}(t)^\dagger .
$$

The norm form is invariant under this action, because the rotor is unitary and the norm form is multiplicative:

$$
N\!\left(\tilde{R}\,\tilde{X}\,\tilde{R}^\dagger\right)
= \tilde{R}\,\tilde{X}\,\tilde{R}^\dagger\,\overline{\tilde{R}\,\tilde{X}\,\tilde{R}^\dagger}
= \tilde{R}\,\tilde{X}\,\bar{\tilde{X}}\,\tilde{R}^\dagger
= N(\tilde{X})\,\tilde{R}\tilde{R}^\dagger
= N(\tilde{X}) .
$$

The same computation applies to the trace pairing, $\mathrm{Tr}((\tilde{R}\tilde{X}\tilde{R}^\dagger)^2) = \mathrm{Tr}(\tilde{X}^2)$, since the conjugation is an algebra automorphism. Therefore

$$
\left|N\!\left(\delta\tilde{\rho}(t)\right)\right| = \left|N\!\left(\delta\tilde{\rho}(0)\right)\right|
\quad\text{for all } t ,
$$

and every Lyapunov exponent vanishes identically:

$$
\boxed{\;\lambda(v) = 0 \quad\text{for every tangent vector } v \text{ of a reversible rotor flow.}\;}
$$

No averaging is needed; the invariance is exact. In Bloch coordinates the rotor conjugations are the rotations of the ball, $|\mathbf{r}(t)| = |\mathbf{r}(0)|$, and the tangent flow is the corresponding rotation of the tangent plane. The result is the biquaternion form of the statement that a Hamiltonian flow preserves phase-space volume and, more strongly, preserves the metric of the state space: reversible classical dynamics is **information-preserving** in the strictest sense, and its information loss is zero.

The coadjoint-orbit picture of the companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow* gives the same conclusion from the Hamiltonian side. On the orbit $|\mathbf{S}| = \text{const}$ with the Lie–Poisson bracket the Hamiltonian flow preserves the Casimir $\mathbf{S}^2$, so the motion is an area-preserving flow on a sphere; the tangent vectors are advected by the flow without change of length, and the exponents vanish. The two descriptions — rotor conjugation on the algebra and Hamiltonian flow on the orbit — agree on this invariant, which is exactly the invariant the similitude preserves.

## Irreversible Dynamics: Channel Semigroups Are Contractions

Irreversibility enters the sector through coarse-graining, and the general form of a coarse-graining semigroup is known. A one-parameter semigroup $\Phi_t$, $t\ge0$, of completely positive trace-preserving maps with $\Phi_0 = \mathrm{id}$ and $\Phi_{s+t} = \Phi_s\circ\Phi_t$ acts on the Bloch vector affinely,

$$
\mathbf{r} \longmapsto \mathbf{r}(t) = L(t)\,\mathbf{r}(0) + \mathbf{t}(t),
$$

with $L(t)$ a real $3\times3$ matrix and $\mathbf{t}(t)$ a translation; the translation vanishes for a unital semigroup, which is the case for a coarse-graining. The tangent map is the linear part alone,

$$
\delta\mathbf{r}(t) = L(t)\,\delta\mathbf{r}(0),
$$

so the Lyapunov exponents of the tangent dynamics are read from $L(t)$. Writing $\sigma_1\ge\sigma_2\ge\sigma_3$ for the singular values of $L(t)$, the exponents are

$$
\lambda_k = \lim_{t\to\infty}\frac{1}{t}\log\sigma_k\!\left(L(t)\right),
$$

and for a semigroup $L(t) = \exp(tA)$, $\lambda_k$ are the real parts of the eigenvalues of the generator $A$.

The physical constraint now does the work. Every completely positive trace-preserving map is a **contraction in the trace distance**, $\|\Phi(\rho)-\Phi(\sigma)\|_1 \le \|\rho-\sigma\|_1$, and for a qubit the trace distance is half the Euclidean distance between Bloch vectors, $\tfrac{1}{2}\|\rho-\sigma\|_1 = \tfrac{1}{2}|\mathbf{r}-\mathbf{s}|$. Hence

$$
\left|L(t)\left(\mathbf{r}-\mathbf{s}\right)\right| \le \left|\mathbf{r}-\mathbf{s}\right| \quad\text{for all } t\ge0 ,
$$

that is, $L(t)$ is a Euclidean contraction, $\sigma_1(L(t))\le1$, and therefore

$$
\boxed{\;\lambda_k \le 0 \quad\text{for every completely positive trace-preserving semigroup.}\;}
$$

The same conclusion follows from the Kadison–Schwarz inequality for the unital case, and it is the dynamical form of the contraction used in the companion article *Coarse-Graining and the Biquaternion Entropy Functional* to prove the monotonicity of the entropy. It has a sharp reading: **the framework's physical, memoryless irreversible dynamics cannot amplify a distinction.** Information is lost, never gained, along such a flow; the exponents are the rates of loss.

## The Dephasing Semigroup

### The Spectrum

The canonical irreversible dynamics of the sector is dephasing along an axis $\hat{\mathbf{n}}$, with transverse components decaying at rate $\Gamma$ and the axial component untouched. In the frame $(\hat{\mathbf{n}}_\perp,\hat{\mathbf{n}}'_\perp,\hat{\mathbf{n}})$ the Bloch action is

$$
\mathbf{r}(t) = \left(e^{-\Gamma t}r_1,\; e^{-\Gamma t}r_2,\; r_3\right),
\qquad
L(t) = \mathrm{diag}\!\left(e^{-\Gamma t},\,e^{-\Gamma t},\,1\right).
$$

The singular values are the diagonal entries, so the **Lyapunov spectrum** is

$$
\lambda_1 = 0, \qquad \lambda_2 = \lambda_3 = -\Gamma .
$$

The zero exponent is the pointer axis, along which the state is unchanged; the two negative exponents are the transverse directions, in which distinctions decay at rate $\Gamma$. The sum of the exponents gives the volume contraction,

$$
\sum_k\lambda_k = -2\Gamma = \frac{d}{dt}\log\det L(t),
$$

so the Bloch ball shrinks in volume at rate $2\Gamma$ and the state is driven onto the pointer diameter.

### The Norm-Form Exponent

The tangent vector of the sector is a traceless element of $\mathbb{M}_+$. Writing a tangent displacement as $\delta\tilde{\rho} = \tfrac{i}{2}\,\delta\mathbf{r}$, its norm form is

$$
N\!\left(\delta\tilde{\rho}\right) = -\frac{1}{4}\left|\delta\mathbf{r}\right|^2 e_0 ,
$$

the identity established in the companion article *Fisher Information and the Biquaternion Norm Form*. Under the dephasing semigroup the transverse displacement decays, so

$$
\left|N\!\left(\delta\tilde{\rho}(t)\right)\right| = \frac{1}{4}\left|\delta\mathbf{r}(t)\right|^2 ,
$$

and a transverse tangent vector has

$$
\lim_{t\to\infty}\frac{1}{2t}\log\frac{\left|N(\delta\tilde{\rho}(t))\right|}{\left|N(\delta\tilde{\rho}(0))\right|}
= \lim_{t\to\infty}\frac{1}{2t}\log e^{-2\Gamma t}
= -\Gamma .
$$

The value is the same as the vector exponent, as it must be: $\lambda$ is the decay rate of the length $\sqrt{|N(\delta\tilde{\rho})|} = \tfrac{1}{2}|\delta\mathbf{r}|$, which is proportional to the displacement itself. The factor of two is real but it belongs to the **quadratic form**, not to the exponent. The un-normalised logarithm of the norm form decays at twice the vector rate,

$$
\frac{1}{t}\log\frac{\left|N(\delta\tilde{\rho}(t))\right|}{\left|N(\delta\tilde{\rho}(0))\right|} = -2\Gamma ,
$$

and the factor $\tfrac{1}{2}$ in the definition of $\lambda$ removes it. **The exponent of the length is the vector exponent; the logarithm of the quadratic form decays at twice that rate.**

<!-- CONVENTION — norm-form versus vector exponent: the norm form N is quadratic, so the scalar |N(delta rho)| decays at twice the rate of the vector it measures. In the dephasing semigroup the transverse vector exponent is -Gamma and the logarithm of the quadratic form decays at -2Gamma. The Lyapunov exponent is defined with a compensating factor 1/2, lambda = lim (1/2t) log |N(t)/N(0)|, and therefore equals the vector exponent -Gamma. Both -Gamma and -2Gamma are correct at their own level; do not "fix" this by dropping the 1/2 from lambda, and do not quote -2Gamma as the Lyapunov exponent. -->

Both numbers were verified numerically on the transverse tangent element $\delta\tilde{\rho} = \tfrac{i}{2}e_1$, taken as a tangent to the interior superposition state $\tilde{\rho} = \tfrac{1}{2}(\tilde{P}_+(e_1)+\tilde{P}_+(e_2))$ rather than to a single idempotent, under the semigroup with $\Gamma = 0.7$. At $t = 0.5$, $1.0$ and $2.0$ the displacement ratio $|\delta\mathbf{r}(t)|/|\delta\mathbf{r}(0)| = e^{-\Gamma t}$ gives the Lyapunov exponent $\lambda = -0.7000000000 = -\Gamma$, while the logarithm of the quadratic form gives $\tfrac{1}{t}\log|N(t)/N(0)| = -1.4000000000 = -2\Gamma$; the two differ by exactly the factor of two that the definition of $\lambda$ absorbs. The representation used is the four-complex-coefficient basis $(e_0,e_1,e_2,e_3)$ with the algebra's product.

### Information Loss and Entropy Production

The exponents are the rates, and the entropy functional of the companion article *Coarse-Graining and the Biquaternion Entropy Functional* is the stock. With $r = |\mathbf{r}(t)|$ and $r_\perp(t) = e^{-\Gamma t}\sqrt{r_1(0)^2 + r_2(0)^2}$ the **instantaneous** transverse component in the frame of the dephasing display above, the entropy production rate of the dephasing semigroup is

$$
\frac{d}{dt}\mathcal{S} = \Gamma\,\frac{r_\perp(t)^2}{r(t)}\,\mathrm{artanh}\,r(t) \;\ge\; 0 ,
$$

as derived there. The rate is quadratic in the transverse component and carries the full factor $e^{-2\Gamma t}$ of the contraction; writing the initial $r_\perp(0)$ instead of $r_\perp(t)$ would overstate it for every $t>0$, and the two agree only at $t = 0$ or when the state has no axial part. The expression organises the bookkeeping: the rate is proportional to the contraction coefficient $\Gamma$, it is supported entirely by the transverse component that the negative exponents act on, and it vanishes when $r_\perp(t) = 0$, that is, when the state already lies on the pointer axis and the tangent vector has no contracting component. The total entropy produced over the whole relaxation is $\mathcal{S}(\infty)-\mathcal{S}(0) = h(|r_3|) - h(|\mathbf{r}(0)|)$, the entropy of the retained classical bit less the entropy of the state.

The stock-and-rate relation can be written in general form. Since $\mathcal{S} = h(r)$ and $h'(r) = -\mathrm{artanh}\,r$,

$$
\frac{d\mathcal{S}}{dt} = -\mathrm{artanh}\,r \cdot \frac{d r}{dt},
$$

and $dr/dt$ is the rate of the tangent flow along the radius, which is a weighted average of the exponents: since $r = |\mathbf{r}(t)|$ and $\partial_i r = \hat{r}_i$, with $\hat{\mathbf{r}} = \mathbf{r}(t)/r(t)$ the **instantaneous** direction, the chain rule gives $\dot{r} = r\sum_k\lambda_k\hat{r}_k^2$ in the dephasing case, so the weights are the instantaneous squared components of $\hat{\mathbf{r}}$, and the result is the formula above. The information loss of the flow is therefore the negative exponents **weighted by how much of the state lies in the directions they contract**, not the bare sum of the exponents. The two are different objects: the bare sum $\sum_k\lambda_k = -2\Gamma$ is the volume contraction, a constant of the semigroup and independent of the state, while the weighted sum $\sum_k\lambda_k\hat{r}_k^2 = -\Gamma(\hat{r}_1^2+\hat{r}_2^2)$, in the frame above, whose first two directions are transverse to the pointer axis, is state-dependent, is carried entirely by the directions with negative exponents, and vanishes on the pointer axis, where the weights of the contracting pair are zero.

## Positive Exponents: Where They Cannot Come From

The framework's linear dynamics has no positive exponent, and it is worth being precise about why, and about what would be needed.

**Contraction forbids them for channels.** The trace-distance contractivity of completely positive trace-preserving maps gives $\sigma_1(L(t))\le1$ and hence $\lambda_k\le0$ for every exponent, without exception. A hypothetical positive exponent would require a map that increases the trace distance, and no completely positive trace-preserving map does. A positive exponent therefore cannot be manufactured from a channel, however the channel is chosen; the loss of information is forced.

**Isometry forbids them for rotor flow.** The reversible class has $\lambda_k = 0$ exactly, as derived above.

**The compact orbit is too small for chaos.** The framework's natural nonlinear classical system is a Hamiltonian flow on the coadjoint orbit, and the compact orbit is the two-sphere $|\mathbf{S}| = \text{const}$. A Hamiltonian flow on a two-dimensional symplectic manifold is integrable, so its exponents vanish. A positive exponent requires, for a Hamiltonian flow, at least four phase-space dimensions, that is, two degrees of freedom; the informational sector's state space supplies three dimensions in total and only the sphere's two for a fixed radius, so it cannot host chaos.

The last point locates the boundary precisely. Positive Lyapunov exponents are a property of a **nonlinear** flow on a **sufficiently large** phase space; the framework's single-qubit informational sector is linear and small, and its information loss is therefore contraction rather than chaos. A nonlinear Hamiltonian on a larger algebra, or on the four-dimensional material sector, can in principle have positive exponents, but that is a statement about the particular Hamiltonian, not about the biquaternion algebra. The algebra supplies the norm form with which the exponents are measured; it does not supply the nonlinearity. By Pesin's formula the Kolmogorov–Sinai entropy of every flow considered here is zero, so the framework's linear classical dynamics generates no information by chaos — a point to keep distinct from the entropy it produces by coarse-graining.

## What Is Derived and What Is Imported

**Derived from the algebra.** The invariance of the norm form and the trace pairing under rotor conjugation, and therefore the vanishing of every Lyapunov exponent of a reversible flow — this is proved directly from the multiplicativity of the norm form, not assumed; the affine Bloch action of a channel semigroup and the identification of its exponents with the singular values of $L(t)$; the dephasing spectrum $\{0,-\Gamma,-\Gamma\}$ and the volume contraction rate $2\Gamma$; the relation between the decay of the quadratic norm form and the vector exponent, including the exact factor of two between them; the identity $N(\delta\tilde{\rho}) = -\tfrac{1}{4}|\delta\mathbf{r}|^2e_0$; and the entropy production rate of the dephasing semigroup. The numerical checks use the four-complex-coefficient representation of $\mathbb{B}$ and a transverse tangent vector, that is, a superposition-level object rather than a single plane wave.

**Imported from standard dynamical-systems theory.** The definition of the Lyapunov exponent and the multiplicative ergodic theorem; the divergence identity $\sum_k\lambda_k = \langle\nabla\cdot f\rangle$; Pesin's formula $h_{\rm KS} = \sum_{\lambda_k>0}\lambda_k$; the integrability of two-dimensional Hamiltonian flows; and the trace-distance contractivity of completely positive trace-preserving maps. These are transcribed as standard.

**Not supplied.** The framework does not derive the dephasing rate $\Gamma$; it does not select which channel is realised; it has no positive exponent and therefore no chaos in its linear sector; and it makes no prediction that differs from the standard Lyapunov analysis of a two-level system. What it supplies is the geometric quantity — the norm form — in terms of which the exponents and the entropy production are one accounting.

## Summary

The Lyapunov exponent of a tangent vector of the informational sector is measured by the sector's norm form,

$$
\lambda(v) = \lim_{t\to\infty}\frac{1}{2t}\log\frac{\left|N(\delta\tilde{\rho}(t))\right|}{\left|N(\delta\tilde{\rho}(0))\right|},
$$

the factor $\tfrac{1}{2}$ reflecting the quadratic character of $N$. Since $N(\delta\tilde{\rho}) = -\tfrac{1}{4}|\delta\mathbf{r}|^2e_0$ for a tangent vector, this is the Euclidean growth rate of the Bloch displacement.

**Reversible rotor flow is Lyapunov-neutral.** Conjugation by a matrix-unitary rotor leaves the norm form and the trace pairing invariant, so every exponent is exactly zero and no information is lost. This is the biquaternion form of the volume preservation of a Hamiltonian flow, and it agrees with the conservation of the Casimir on the coadjoint orbit.

**Irreversible channel semigroups are contractions.** The affine Bloch action $\mathbf{r}\mapsto L(t)\mathbf{r}+\mathbf{t}(t)$ has tangent map $L(t)$, whose singular values are the exponential rates; trace-distance contractivity of completely positive trace-preserving maps gives $\sigma_1(L(t))\le1$, hence every exponent is non-positive. The dephasing semigroup has the spectrum $\{0,-\Gamma,-\Gamma\}$, sum $-2\Gamma$ equal to the volume contraction rate, and entropy production rate $\Gamma(r_\perp(t)^2/r(t))\,\mathrm{artanh}\,r(t)$, with $r_\perp(t)$ the instantaneous transverse component. The quadratic norm form of a transverse tangent vector decays at $e^{-2\Gamma t}$, twice the vector rate $e^{-\Gamma t}$, because the norm form is quadratic; the Lyapunov exponent $\lambda$, defined with the compensating factor $\tfrac{1}{2}$, is the vector exponent $-\Gamma$ itself.

**No positive exponents are available.** Isometry forbids them for rotor flow, contraction forbids them for channels, and the compact coadjoint orbit is a two-dimensional symplectic manifold, where Hamiltonian flows are integrable. Chaos in a Hamiltonian flow needs four phase-space dimensions and a nonlinearity, neither of which the single-qubit informational sector has. The information loss of the framework is therefore contraction, not chaos, and the Kolmogorov–Sinai entropy of its linear flows is zero by Pesin's formula.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) subspaces |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary |
| $\tilde{\rho} = \tfrac{1}{2}(e_0+i\mathbf{r})$ | State, Bloch vector $\mathbf{r}$, $|\mathbf{r}|\le1$ |
| $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$ | Trace, $\mathrm{Tr}(e_0)=2$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form |
| $\delta\tilde{\rho} = \tfrac{i}{2}\delta\mathbf{r}$ | Tangent vector (traceless element of $\mathbb{M}_+$) |
| $N(\delta\tilde{\rho}) = -\tfrac{1}{4}|\delta\mathbf{r}|^2 e_0$ | Norm form of a tangent vector (negative definite) |
| $\lambda(v) = \lim_t \tfrac{1}{2t}\log|N(\delta\tilde{\rho}(t))/N(\delta\tilde{\rho}(0))|$ | Lyapunov exponent in the norm form |
| $\lambda_1\ge\lambda_2\ge\lambda_3$ | Lyapunov spectrum |
| $\tilde{R}(t)$, $\tilde{R}\tilde{R}^\dagger = e_0$ | Matrix-unitary rotor (reversible flow) |
| $\tilde{\rho}\mapsto\tilde{R}\tilde{\rho}\tilde{R}^\dagger$ | Rotor conjugation; isometry, $\lambda_k=0$ |
| $\Phi_t$, $L(t)$, $\mathbf{t}(t)$ | Channel semigroup and its affine Bloch action |
| $\mathbf{r}\mapsto L(t)\mathbf{r}+\mathbf{t}(t)$ | Affine Bloch action of a channel |
| $\sigma_k(L(t))$ | Singular values; $\lambda_k = \lim_t\tfrac{1}{t}\log\sigma_k$ |
| $\sigma_1(L(t))\le1$ | Contraction (trace-distance contractivity of CPTP maps) |
| $\lambda_k\le0$ | No positive exponent for a channel semigroup |
| $L(t) = \mathrm{diag}(e^{-\Gamma t},e^{-\Gamma t},1)$ | Dephasing semigroup |
| $\{0,-\Gamma,-\Gamma\}$ | Dephasing Lyapunov spectrum |
| $\sum_k\lambda_k = -2\Gamma$ | Volume contraction rate |
| $\lambda = -\Gamma$, $|N|\propto e^{-2\Gamma t}$ | Transverse tangent vector: length exponent $-\Gamma$, quadratic form decaying at $-2\Gamma$ |
| $\dot{\mathcal{S}} = \Gamma(r_\perp(t)^2/r(t))\,\mathrm{artanh}\,r(t)$ | Entropy production rate (instantaneous $r_\perp$) |
| $h_{\rm KS} = \sum_{\lambda_k>0}\lambda_k$ | Pesin's formula (standard) |
| $|\mathbf{S}| = \text{const}$ | Coadjoint orbit (Bloch sphere); Hamiltonian flows integrable |

## Further Reading

- A. M. Lyapunov, *The General Problem of the Stability of Motion* (Kharkov, 1892; English translation Taylor & Francis, 1992), for the original definition of the characteristic exponents.
- V. I. Oseledets, "A multiplicative ergodic theorem: Lyapunov characteristic numbers for dynamical systems," *Transactions of the Moscow Mathematical Society* **19** (1968) 197–231, for the existence of the spectrum.
- Ya. B. Pesin, "Characteristic Lyapunov exponents and smooth ergodic theory," *Russian Mathematical Surveys* **32** (1977) 55–114, for Pesin's formula relating the exponents to the Kolmogorov–Sinai entropy.
- J.-P. Eckmann and D. Ruelle, "Ergodic theory of chaos and strange attractors," *Reviews of Modern Physics* **57** (1985) 617–656, for the standard account of Lyapunov exponents, volume contraction and information loss.
- V. I. Arnold, *Mathematical Methods of Classical Mechanics* (Springer, 1989), for Hamiltonian flows, Liouville's theorem, and the integrability of two-dimensional Hamiltonian systems.
- R. Alicki and M. Fannes, *Quantum Dynamical Systems* (Oxford, 2001), for contractive semigroups and the contraction of completely positive trace-preserving maps.
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the monotonicity of the trace distance under completely positive trace-preserving maps.
- R. Bhatia, *Matrix Analysis* (Springer, 1997), for singular values and the logarithmic norm of a matrix exponential.
