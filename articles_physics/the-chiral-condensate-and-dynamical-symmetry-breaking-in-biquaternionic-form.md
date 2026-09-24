# __The Chiral Condensate and Dynamical Symmetry Breaking in Biquaternionic Form__

## Introduction

A **chiral condensate** is a nonzero vacuum expectation value of a fermion bilinear, $\langle\bar{\psi}\psi\rangle\neq0$, in a theory whose Lagrangian contains no such term. It is the order parameter of a symmetry that the Lagrangian respects and the vacuum does not: the fermion field is massless as written, the vacuum pairs its two chiralities, and the fermion propagates with a mass it was never given. The mechanism is **dynamical symmetry breaking**, and it is the reason the proton is heavy and the pion is light — the two facts that first forced the idea on particle physics.

In the biquaternion framework the fermion is the Dirac field of the companion articles and its mass is the **linear, chirality-off-diagonal pair**

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L , \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R .
$$

This article asks what the framework supplies for the condensate. The answer is a short chain of algebraic facts and one large missing physical input, and it is stated at the outset in the corpus's three categories.

- **Established, and recomputed below.** The massless biquaternion equation $\tilde{\nabla}\tilde{\Psi}=0$ carries the axial symmetry $\tilde{\Psi}\mapsto e^{i\alpha\gamma_5}\tilde{\Psi}$, and the massive linear chiral pair breaks it: the vector central phase $e^{i\alpha}$ passes through the mass, the axial phase does not, and the axial current obeys $\partial_\mu j_5^\mu = 2im\bar{\psi}\gamma_5\psi$. A condensate $\langle\bar{\Psi}\Psi\rangle$ is the vacuum expectation of exactly the bilinear that the mass term multiplies, so a nonzero condensate is a dynamically generated coefficient of the *same* linear chiral pair — not of the algebra's antilinear real structure $\flat$, which is a different object.
- **Established, and recomputed below.** The bilinear $\bar{\Psi}\Psi=\psi_L^\dagger\psi_R+\psi_R^\dagger\psi_L$ is chirality-odd, Lorentz-invariant and parity-even; its vacuum expectation is a **central** (scalar) element of $\mathbb{B}$, it is the identity of the two kinds of mass, and it is what the framework's off-diagonal mass coupling is a coefficient of. The counting of broken generators, $N_f^2-1$ for $N_f$ massless flavours, is the standard one and is reproduced.
- **Standard, transcribed.** The Nambu–Jona-Lasinio gap equation, the critical coupling $G_c$, the mean-field condensate, and the Goldstone counting are textbook. They are stated here in the framework's notation because they are what a dynamical condensate is, and the article verifies the one numerical relation it quotes.
- **Gap, left visible.** The framework has **no colour group and no strong gauge dynamics**: the compact gauge algebra inside $\mathbb{B}$ is at most $\mathfrak{u}(2)$ of real dimension four, every $\mathbb{B}$-module has even complex dimension, and $SU(3)$ is absent. A QCD-like condensate therefore cannot be *derived* in the framework. The framework supplies the algebraic identity of the condensate with the coefficient of its linear chiral pair; the scale, and the interaction that produces it, are empirical input.

The article is organised as follows. A section fixes the chiral symmetry of the linear mass term and its axial current. A section shows that the condensate is the order parameter and identifies it algebraically. A section transcribes the gap equation and verifies its numbers. A section gives the biquaternion reading. A section records the Goldstone counting and where the pion is treated. A closing section separates what the framework supplies, transcribes, and does not supply.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$ and $e_1e_2=e_3$, and $i$ is the scalar imaginary, $i^2=-1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ is the complex scalar subspace, the center of the algebra. The biquaternionic gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_k\partial_k$, its quaternion conjugate is $\bar{\tilde{\nabla}}=e_0\partial_{ict}-e_k\partial_k$, and $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\bar{\tilde{\nabla}}\tilde{\nabla}=\partial_{ict}^2+\Delta$. The massless biquaternion Dirac equation is $\tilde{\nabla}\tilde{\Psi}=0$; the massive equation is the linear chiral pair above, and its spinor-module representative $\psi$ satisfies $(i\gamma^\mu\partial_\mu-m)\psi=0$. The Dirac module is $\Delta=S\oplus\bar{S}$ with $S=\mathbb{C}^2$, the chirality operator is $\gamma_5=\mathrm{diag}(-I_2,I_2)=i\omega$ with $\omega=\gamma^0\gamma^1\gamma^2\gamma^3$ the volume element, and the chiral projectors are $P_L=\tfrac12(I_4-\gamma_5)$, $P_R=\tfrac12(I_4+\gamma_5)$. We use the block representation

$$
\gamma^0=\begin{pmatrix}0&I_2\\ I_2&0\end{pmatrix},\qquad
\gamma^k=\begin{pmatrix}0&\sigma^k\\ -\sigma^k&0\end{pmatrix},\qquad
\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4,\qquad g=\mathrm{diag}(+1,-1,-1,-1),
$$

with $\gamma_5=\mathrm{diag}(-I_2,I_2)$ and the spacetime metric of the $ict$ gradient $\eta=-g$. The Clifford isomorphism identifies $\mathbb{B}$ with $\mathrm{Cl}_{1,3}^{+}$ by $e_1\mapsto\gamma^2\gamma^3$, $e_2\mapsto\gamma^3\gamma^1$, $e_3\mapsto\gamma^1\gamma^2$ and $i\mapsto\omega=\gamma^0\gamma^1\gamma^2\gamma^3$, so that $\gamma_5=i\omega$. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ the vacuum value; natural units $\hbar=c=1$ are used in the gap-equation section.
<!-- CONVENTION — the linear mass term: the massive biquaternion fermion is the chirality-off-diagonal pair ∇̃Ψ_R = mΨ_L, ∇̄̃Ψ_L = mΨ_R, and the axial transformation Ψ → e^{iαγ5}Ψ is the broken one. The algebra's antilinear real structure ♭ = −† is a separate object and is not this article's mass. Do not replace the linear pair by an antilinear single-field equation. -->

The framework results used here are those of the companion articles:

- Companion article *Chiral Fermions in the Biquaternion Framework*, for the chiral classification and the two halves of the Dirac module.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the massless equation, its chiral solutions and the fermion bilinears.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the axial current and its conservation law.
- Companion article *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, for the separation of the linear chiral pair from the real structure $\flat$.
- Companion article *Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda*, for the status of colour and the strong dynamics that a condensate requires.

## The Chiral Symmetry of the Linear Mass Term

**The massless equation and its two phases.** The massless biquaternion Dirac equation is $\tilde{\nabla}\tilde{\Psi}=0$, whose spinor-module representative is $i\gamma^\mu\partial_\mu\psi=0$. Two one-parameter phase symmetries act on it. The **vector** (central) phase

$$
V:\ \psi\ \longmapsto\ e^{i\alpha}\psi ,
$$

is multiplication by the central element $e^{i\alpha}\in\mathbb{C}_{\mathbb{B}}$; it rotates the two chiralities together. The **axial** phase

$$
A:\ \psi\ \longmapsto\ e^{i\alpha\gamma_5}\psi ,
\qquad\text{equivalently}\qquad
\psi_L\longmapsto e^{-i\alpha}\psi_L ,\quad \psi_R\longmapsto e^{+i\alpha}\psi_R ,
$$

rotates them oppositely. In the biquaternion statement of the companion article on chiral fermions, the two halves are the left-handed module $S$ and its conjugate $\bar{S}$, and the axial phase is the relative phase of the two.

Both are symmetries of the massless equation, because $\gamma_5$ anticommutes with every generator, $\{\gamma_5,\gamma^\mu\}=0$, and therefore commutes with the kinetic operator $i\gamma^\mu\partial_\mu$; the two transformations may be applied independently. Equivalently, the massless theory has the flavour-chiral symmetry

$$
U(1)_V\times U(1)_A ,
$$

and with $N_f$ massless flavours it enlarges to $SU(N_f)_L\times SU(N_f)_R\times U(1)_V$.

**The mass term and which phase it breaks.** The massive linear chiral pair is

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L , \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R ,
$$

whose module representative is $(i\gamma^\mu\partial_\mu-m)\psi=0$. The two phase transformations act on the mass term as follows. Under the **vector** phase both chiralities acquire the same factor, so the two sides of the first equation acquire $e^{i\alpha}$ and $e^{i\alpha}$: the equation is invariant. Under the **axial** phase the left side acquires $e^{-i\alpha}$ and the right side $e^{+i\alpha}$, and the equation is *not* invariant unless $m=0$. The algebraic statement is exact:

$$
V:\ e^{i\alpha}\ \text{central, passes through } m \ \Longrightarrow\ \text{conserved};
\qquad
A:\ e^{i\alpha\gamma_5}\ \text{does not} \ \Longrightarrow\ \text{broken by } m .
$$

This is the framework form of the standard fact that a Dirac mass breaks the axial symmetry while preserving the vector one. It is also the statement recorded in the companion articles on Noether's theorem and on chiral fermions, and it fixes what a condensate can do: a nonzero vacuum value of a chirality-odd bilinear will break $U(1)_A$ and nothing else at this level.

**The axial current.** For the module representative the axial current is

$$
j_5^\mu = \bar{\psi}\gamma^\mu\gamma_5\psi ,
$$

and its divergence is the textbook anomaly-free identity for a massive free field,

$$
\partial_\mu j_5^\mu = 2im\,\bar{\psi}\gamma_5\psi ,
$$

which vanishes exactly when $m=0$. The mass is the sole explicit breaking, and the identity is exact at the classical level. The quantum correction to it — the axial anomaly, which adds a term even at $m=0$ — is the subject of the companion articles; here it is noted only for completeness, and the *spontaneous* breaking that a condensate produces is a separate phenomenon from that anomaly.

**Two symmetries, two currents.** For later use we record the vector and axial bilinears:

$$
j^\mu = \bar{\psi}\gamma^\mu\psi , \qquad j_5^\mu = \bar{\psi}\gamma^\mu\gamma_5\psi ,
\qquad
\partial_\mu j^\mu = 0 , \qquad \partial_\mu j_5^\mu = 2im\,\bar{\psi}\gamma_5\psi .
$$

The scalar bilinear $S=\bar{\psi}\psi$ is the one that will acquire a vacuum expectation value.

## The Condensate as an Order Parameter

**The bilinear.** In the block basis of the Conventions the scalar bilinear is

$$
\bar{\Psi}\Psi = \Psi^{\dagger}\gamma^0\Psi = \psi_L^{\dagger}\psi_R + \psi_R^{\dagger}\psi_L ,
$$

the **Dirac mass bilinear**. It is off-diagonal in the chiral blocks, it is a Lorentz scalar and parity-even, and under the axial transformation it is not invariant:

$$
A:\ \bar{\Psi}\Psi\ \longmapsto\ \cos(2\alpha)\,\bar{\Psi}\Psi+\sin(2\alpha)\,i\bar{\Psi}\gamma_5\Psi ,
$$

using $e^{2i\alpha\gamma_5}=\cos(2\alpha)+i\sin(2\alpha)\gamma_5$ and $\gamma_5^2=I_4$. The scalar bilinear therefore rotates into the pseudoscalar bilinear $i\bar{\Psi}\gamma_5\Psi$: the pair $(\bar{\Psi}\Psi,\,i\bar{\Psi}\gamma_5\Psi)$ carries the two-dimensional rotation of the axial group, exactly as a two-component order parameter should.

**The order parameter.** A **chiral condensate** is a nonzero vacuum expectation value

$$
\langle\bar{\Psi}\Psi\rangle = -v^3 \neq 0 ,
$$

where the mass dimension and the sign are fixed by the dynamics and the sign convention. Because the vacuum expectation distinguishes the axial rotation above — $\langle\bar{\Psi}\Psi\rangle$ at $\alpha=0$ is not equal to its value at $\alpha\neq0$ unless it vanishes — a nonzero condensate **spontaneously breaks** the axial symmetry: the Lagrangian is invariant, the vacuum is not, and the Goldstone modes of the broken generator follow. The condensate is the order parameter of the transition.

**The algebraic identity with the mass coupling.** The point the biquaternion framework makes is an identification, and it is clean. The condensate $\langle\bar{\Psi}\Psi\rangle$ is the vacuum expectation of precisely the bilinear that the linear chiral pair multiplies: the mass equation $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$ is the statement that the left and right chiralities are coupled by the coefficient $m$, and $\bar{\Psi}\Psi=\psi_L^\dagger\psi_R+\psi_R^\dagger\psi_L$ is that same coupling written as a bilinear of the field. A dynamically generated mass is therefore the statement

$$
\boxed{\ m \;\longleftrightarrow\; -2G\,\langle\bar{\Psi}\Psi\rangle\ }
$$

with $G$ the coupling of the four-fermion interaction that produces the condensate: the coefficient of the framework's linear chiral pair is the condensate, up to the coupling. This is not a new dynamics; it is the reason the framework's mass term is the right carrier for the condensate, and it is why the condensate is not a pairing built on the algebra's real structure $\flat$.

**Sector placement.** The scalar bilinear $\bar{\Psi}\Psi$ is Hermitian and its vacuum expectation is real; as an element of the algebra it lies in the **center** $\mathbb{C}_{\mathbb{B}}$ on the scalar line, which is the fixed space of quaternion conjugation. That placement is the algebraic content of two physical facts at once: the condensate is a Lorentz scalar (it carries no vector index), and it is neutral under the vector central phase (it is central). The chirality-odd property is the module statement that it pairs $S$ with $\bar{S}$; the centrality is the algebra statement that its value is a number. The two are consistent and neither is derived from the other.

**Why not the real structure.** The framework's antilinear real structure $\tilde{\Psi}^{\flat}=-\tilde{\Psi}^{\dagger}$ pairs a field with its own conjugate, and a coupling built on it has the signature of a Majorana-type term; the companion articles keep it strictly separate from the linear chiral pair. The condensate is a *chiral* pairing of two independent halves, so it belongs to the linear pair and not to $\flat$. A reader who attempts to read the condensate through $\flat$ will obtain the wrong object: the fixed space of $\flat$ is the four-real-dimensional material sector $\mathbb{M}_-$, which is not the chiral-pair carrier. The distinction is the subject of the companion on antilinear structure, and the present article uses it without re-deriving it.

## The Gap Equation and the Critical Coupling

**The model.** The standard mean-field model of a dynamical fermion mass is the Nambu–Jona-Lasinio (NJL) Lagrangian, a four-fermion interaction

$$
\mathcal{L} = \bar{\psi}\big(i\gamma^\mu\partial_\mu\big)\psi + G\left[(\bar{\psi}\psi)^2+(\bar{\psi}i\gamma_5\psi)^2\right],
$$

in which $G$ has mass dimension $-2$. The interaction is chirally invariant: the combination $(\bar{\psi}\psi)^2+(\bar{\psi}i\gamma_5\psi)^2$ is the invariant of the axial rotation noted above, because the pair $(\bar{\psi}\psi,\,i\bar{\psi}\gamma_5\psi)$ rotates as a two-vector. The framework carries the same structure: the four-fermion interaction pairs the bilinears, and it does not need the algebra beyond the chiral pairing that the bilinears already are.

**The mean-field mass.** Linearising the interaction about the condensate replaces the four-fermion term by a mass term with

$$
m = -2G\langle\bar{\psi}\psi\rangle ,
$$

and the condensate in turn is computed in the mean-field vacuum of a fermion of mass $m$. For $N_c$ colours and a sharp ultraviolet cutoff $\Lambda$ the self-consistency condition is the **gap equation**

$$
m = 4N_c\,G\,m\,I_1(m) ,
\qquad
I_1(m) = \int_0^{\Lambda}\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{\mathbf{p}^2+m^2}} .
$$

The equation always has the **chiral** solution $m=0$. Dividing by $m$, a nontrivial solution requires $1 = 4N_cG\,I_1(m)$, and since $I_1$ decreases with $m$ the threshold is set at $m=0$:

$$
1 = 4N_c\,G\,I_1(0) = 4N_c\,G\,\frac{\Lambda^2}{4\pi^2}
\qquad\Longrightarrow\qquad
G_c = \frac{\pi^2}{N_c\,\Lambda^2} .
$$

For $G>G_c$ the chiral solution is unstable and the nontrivial one appears; the transition is second order in the mean-field approximation. Both the gap equation and the threshold are standard and are transcribed here.

**The condensate.** At the nontrivial solution the condensate is

$$
\langle\bar{\psi}\psi\rangle = -2N_c\,m\,I_1(m) \approx -\frac{N_c\,m\,\Lambda^2}{2\pi^2}\Big|_{\text{leading}} ,
$$

where the second form keeps the leading term for $m\ll\Lambda$. The numbers were recomputed directly from the integral, in units of GeV, for $N_c=3$ and $\Lambda=0.65$:

| quantity | value (recomputed) |
|---|---|
| $I_1(0)=\Lambda^2/(4\pi^2)$ | $1.070\times10^{-2}\ \mathrm{GeV}^2$ |
| $G_c=\pi^2/(N_c\Lambda^2)$ | $7.79\ \mathrm{GeV}^{-2}$ |
| $I_1(m)$ at $m=0.3$ | $8.33\times10^{-3}\ \mathrm{GeV}^2$ |
| $1/(4N_cI_1(m))$ | $10.00\ \mathrm{GeV}^{-2}$ |
| $\langle\bar{\psi}\psi\rangle$ at $m=0.3$ | $-1.50\times10^{-2}\ \mathrm{GeV}^3 = -(247\ \mathrm{MeV})^3$ |

The last number is the point of the table: a constituent mass of order $300$ MeV with a cutoff of order $650$ MeV produces a condensate of order $-(250\ \mathrm{MeV})^3$, which is the accepted size of the quark condensate. Nothing in the computation is the framework's; it is the standard NJL mean field, reproduced to fix the size of the object the framework is naming.

**Which symmetry is broken, and where.** The nonzero condensate breaks $U(1)_A$ for one flavour and $SU(N_f)_A$ for $N_f$ flavours, down to the vector subgroup $SU(N_f)_V$. The vector symmetry — the one the framework's central phase generates, and the one the linear chiral pair preserves — is *not* broken. This is the exact pattern the biquaternion mass term produces: the mass conserves the central phase and breaks the axial one, and the condensate does the same spontaneously.

## The Effective Potential and the Physical Mass Shell

**The mass shell.** The coefficient the condensate supplies is a genuine mass, and the framework shows it in two lines. Apply the conjugate gradient to the first member of the linear chiral pair and use the second:

$$
\bar{\tilde{\nabla}}\big(\tilde{\nabla}\tilde{\Psi}_R\big)
=\bar{\tilde{\nabla}}\big(m\tilde{\Psi}_L\big)
=m\,\bar{\tilde{\nabla}}\tilde{\Psi}_L
=m\,(m\tilde{\Psi}_R)=m^2\tilde{\Psi}_R .
$$

Since $\Box=\bar{\tilde{\nabla}}\tilde{\nabla}$, the right-handed field satisfies

$$
\Box\tilde{\Psi}_R = m^2\tilde{\Psi}_R ,
\qquad\text{and, symmetrically,}\qquad
\Box\tilde{\Psi}_L = m^2\tilde{\Psi}_L .
$$

The dynamical coefficient is therefore a common mass for the two chiralities: the off-diagonal coupling has rotated into the mass-shell condition of each half. This is the framework's positive statement that a condensate-generated $m$ is a physical mass and not a bookkeeping device, and it uses no more than the factorisation of the d'Alembertian on which the linear mass pair rests.

**The effective potential.** The mean-field energy of the condensate is the standard one. Writing $\sigma=-2G\langle\bar{\psi}\psi\rangle$ for the order parameter and $m=\sigma$ at the minimum, the effective potential at zero temperature is

$$
V(\sigma) \;=\; \frac{\sigma^2}{4G} \;-\; 2N_c\int^{\Lambda}\frac{d^3p}{(2\pi)^3}\,\sqrt{\mathbf{p}^2+\sigma^2}
\;=\; \frac{m^2}{4G} \;-\; 2N_c\int^{\Lambda}\frac{d^3p}{(2\pi)^3}\sqrt{\mathbf{p}^2+m^2},
$$

where the normalization of the first term is tied to the $(\bar{\psi}\psi)^2$ coupling convention used above. Its stationarity condition

$$
\frac{dV}{dm} = \frac{m}{2G} - 2N_c\,m\,I_1(m) = 0
\qquad\Longrightarrow\qquad
1 = 4N_cG\,I_1(m)
$$

is exactly the gap equation, so the two descriptions — self-consistent mass and minimised energy — are the same statement. The symmetric point $m=0$ is a local minimum for $G<G_c$ and a maximum for $G>G_c$, which is what makes the transition second order in this approximation; $G_c=\pi^2/(N_c\Lambda^2)$ is where the curvature at the origin changes sign. The curvature about the nontrivial minimum in the radial (sigma) direction is the mass of the scalar partner of the condensate; in the angular (Goldstone) directions it vanishes before explicit breaking, which is the effective-potential face of the counting in the next section. All of this is standard; it is transcribed because it is what the phrase "the condensate's value" means, and because it exhibits the framework's identification $m\leftrightarrow\sigma$ as a stationarity condition rather than a definition.

**The scale.** The condensate and $G_c$ depend on the cutoff $\Lambda$; only combinations fixed by the renormalised dynamics are physical. The framework has no dynamics from which to fix the combination, so the table of the previous section is a demonstration of size, not a prediction.

## The Biquaternion Reading of the Condensate

Four statements, in decreasing order of strength.

- **The condensate is the coefficient of the framework's mass.** The linear chiral pair couples $\tilde{\Psi}_L$ and $\tilde{\Psi}_R$ with the coefficient $m$; the bilinear $\bar{\Psi}\Psi$ is that coupling's expectation; and the mean-field relation $m=-2G\langle\bar{\Psi}\Psi\rangle$ makes the identification exact at the level of the equation. The framework does not merely "host" the condensate; the off-diagonal mass coupling *is* the object whose coefficient the condensate supplies.
- **The broken symmetry is the axial one, and the framework's mass breaks it explicitly.** The central phase passes through the linear chiral pair and is conserved; the axial phase does not and is broken. A condensate reproduces the same breaking pattern spontaneously, and the axial current identity $\partial_\mu j_5^\mu=2im\bar{\psi}\gamma_5\psi$ is the framework's statement of it. Neither the identity nor the pattern is special to the biquaternion algebra; what the algebra supplies is the sector placement of the bilinears — the scalar condensate in the center, the pseudoscalar partner beside it — and the identification of the condensate with the central scalar coefficient.
- **The order parameter is a central scalar.** As an algebra element the condensate sits on the real scalar direction $\mathbb{R}e_0\subset\mathbb{C}_{\mathbb{B}}$. That is the framework's way of saying it is a Lorentz scalar and vector-neutral, and it is exact.
- **The second kind of mass is not involved.** The condensate is a chiral pairing, so it is linear and built on the chiral off-diagonal coupling; it is not the antilinear self-pairing built on $\flat$. The framework's two-mass distinction, established in the companion on antilinear structure, is what keeps the two from being conflated here.

**What is genuinely missing.** The framework has no colour group, no confinement, and no strong-coupling dynamics. The compact gauge algebra inside $\mathbb{B}$ is at most $\mathfrak{u}(2)$ of real dimension four; every $\mathbb{B}$-module has even complex dimension, so no three-dimensional colour module exists; and the strong-interaction agenda records that $SU(3)$ is an obstacle with no route. A condensate of the NJL type can therefore be *written down* in the framework — its bilinears and its symmetry pattern are the framework's — but it cannot be *derived* from a framework interaction, because the interaction that produces it in nature is the colour gauge theory the framework does not contain. The four-fermion coupling $G$ is an effective parameter in the framework in exactly the way it is in NJL.

## Goldstone Counting, and Where the Pion Lives

**The counting.** When a continuous symmetry group $G_{\mathrm{ch}}$ is spontaneously broken to a subgroup $H$, the number of Goldstone modes is $\dim G_{\mathrm{ch}}-\dim H$. For $N_f$ massless flavours the chiral symmetry is $G_{\mathrm{ch}}=SU(N_f)_L\times SU(N_f)_R$ of real dimension $2(N_f^2-1)$, broken to the diagonal vector subgroup $H=SU(N_f)_V$ of dimension $N_f^2-1$. Hence

$$
N_{\mathrm{Goldstone}} = 2(N_f^2-1)-(N_f^2-1)=N_f^2-1 ,
$$

which is $3$ for $N_f=2$ (the pions) and $8$ for $N_f=3$ (the octet). The Goldstone modes are pseudoscalars: they are the pseudoscalar partner $i\bar{\Psi}\gamma_5\Psi$ rotated by the broken axial generators, and the counting is standard. The Goldstone theorem itself is standard, and the framework transcribes it in the same way it transcribes the gap equation.

**Where the pion is treated.** The Goldstone modes of this breaking are spin-$0$ objects, and their effective description — the chiral Lagrangian, the nonlinear sigma model, the pion, and the relation of the Goldstone decay constant to the condensate — belongs to the spin-$0$ subcategory of this series and is not developed here. This article stops where the fermion sector stops: the order parameter, the broken symmetry, and the identification of the condensate with the coefficient of the linear chiral pair. The Gell-Mann–Oakes–Renner relation, which ties the pion mass to the explicit quark masses and the condensate, is likewise a spin-$0$ statement and is used here only as a consistency check on the size of the condensate, not derived.

**The explicit breaking.** With a nonzero bare quark mass $m_q$ the axial symmetry is broken explicitly as well as spontaneously, the Goldstone modes acquire a mass, and the condensate tilts. The framework's linear chiral pair carries the explicit breaking by construction — its coefficient is the mass — so the explicit and spontaneous breakings act on the same coupling. This is the structural reason the two are naturally discussed together, and it is why the condensate, once present, makes the mass term self-consistent rather than merely added.

## What the Framework Supplies and What It Does Not Supply

**Supplied.** The linear chiral pair, and with it the carrier of the condensate; the chirality-odd scalar bilinear and its rotation into the pseudoscalar partner; the axial current identity and the pattern of preserved vector and broken axial symmetry; the centrality of the order parameter; and the algebraic identification $m\leftrightarrow-2G\langle\bar{\Psi}\Psi\rangle$. The framework's mass term is not merely compatible with a condensate; it is the term whose coefficient a condensate fixes, and the companion on antilinear structure explains why the condensate is not to be sought in the real structure $\flat$.

**Transcribed.** The NJL model, the mean-field gap equation, the critical coupling $G_c$, the condensate's size, the Goldstone counting, and the Goldstone theorem. These are standard and are used here in the framework's notation.

**Not supplied.** The colour gauge dynamics that produces the condensate in nature; the value of the coupling $G$; the scale $\Lambda$; and therefore the numerical value of $\langle\bar{\Psi}\Psi\rangle$ and of the constituent mass. The framework is scale-free until these are supplied, exactly as the companion articles record for the masses elsewhere. No biquaternion prediction distinguishes this account from the standard one.

## Summary

The chiral condensate in biquaternionic form is the vacuum expectation of the chirality-odd scalar bilinear,

$$
\langle\bar{\Psi}\Psi\rangle = \langle\psi_L^\dagger\psi_R+\psi_R^\dagger\psi_L\rangle ,
$$

and it is the order parameter of the axial symmetry that the framework's **linear chiral mass pair** $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L=m\tilde{\Psi}_R$ breaks. The massless equation $\tilde{\nabla}\tilde{\Psi}=0$ carries both the vector and the axial phase; the mass term preserves the vector central phase and breaks the axial one, with $\partial_\mu j_5^\mu=2im\bar{\psi}\gamma_5\psi$. A nonzero condensate reproduces exactly this breaking, spontaneously, and its value is the coefficient of the same linear chiral pair: $m=-2G\langle\bar{\Psi}\Psi\rangle$. The order parameter is a central scalar and is not the antilinear pairing built on the algebra's real structure $\flat$.

The standard mean-field account was verified. With $N_c$ colours and cutoff $\Lambda$ the gap equation is $1=4N_cG\,I_1(m)$, the critical coupling is $G_c=\pi^2/(N_c\Lambda^2)$, and for $N_c=3$, $\Lambda=0.65$ GeV, and a constituent mass $m=0.3$ GeV the condensate is $-(247\ \mathrm{MeV})^3$ — the accepted order of magnitude. The Goldstone count is $N_f^2-1$, giving three pions for $N_f=2$ and eight modes for $N_f=3$; the spin-$0$ effective description of those modes belongs to another subcategory and is not developed here.

The framework supplies the carrier of the condensate, the broken-symmetry pattern, and the sector placement of the order parameter. It does not supply the dynamics: it has no colour group, no confinement, and no strong-coupling interaction, so a QCD-like condensate cannot be derived in it. The coupling, the cutoff, the scale, and the numerical value of the condensate are empirical input, and the algebra's role is structural.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$ | Center; home of the scalar condensate |
| $\tilde{\nabla}=e_0\partial_{ict}+e_k\partial_k$ | Biquaternionic gradient |
| $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$ | d'Alembertian, series convention |
| $\tilde{\nabla}\tilde{\Psi}=0$ | Massless biquaternion Dirac equation |
| $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L=m\tilde{\Psi}_R$ | Linear chiral mass pair (canonical form) |
| $S=\mathbb{C}^2=(\tfrac12,0)$, $\bar{S}=(0,\tfrac12)$, $\Delta=S\oplus\bar{S}$ | Weyl, conjugate Weyl, and Dirac modules |
| $\gamma_5=\mathrm{diag}(-I_2,I_2)=i\omega$, $\omega=\gamma^0\gamma^1\gamma^2\gamma^3$ | Chirality operator; the volume element under the Clifford isomorphism |
| $P_L=\tfrac12(I_4-\gamma_5)$, $P_R=\tfrac12(I_4+\gamma_5)$ | Chiral projectors |
| $\bar{\Psi}\Psi=\psi_L^\dagger\psi_R+\psi_R^\dagger\psi_L$ | Chirality-odd scalar bilinear; the condensate's carrier |
| $i\bar{\Psi}\gamma_5\Psi$ | Pseudoscalar partner; rotates with the condensate under the axial phase |
| $j^\mu=\bar{\psi}\gamma^\mu\psi$, $j_5^\mu=\bar{\psi}\gamma^\mu\gamma_5\psi$ | Vector and axial currents |
| $\partial_\mu j_5^\mu=2im\bar{\psi}\gamma_5\psi$ | Axial divergence (explicit breaking by $m$) |
| $\langle\bar{\Psi}\Psi\rangle=-v^3$ | Chiral condensate, the order parameter |
| $m=-2G\langle\bar{\psi}\psi\rangle$ | Mean-field relation between mass and condensate |
| $G$, $G_c=\pi^2/(N_c\Lambda^2)$ | Four-fermion coupling and critical coupling |
| $I_1(m)=\int^\Lambda\frac{d^3p}{(2\pi)^3}(\mathbf{p}^2+m^2)^{-1/2}$ | Gap-equation integral |
| $N_f$, $N_c$, $\Lambda$ | Flavours, colours, ultraviolet cutoff |
| $N_f^2-1$ | Number of Goldstone modes of the broken chiral symmetry |
| $SU(N_f)_L\times SU(N_f)_R\to SU(N_f)_V$ | Chiral symmetry breaking pattern |
| $\flat=-\dagger$ | The algebra's real structure (not the condensate's pairing) |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- Y. Nambu and G. Jona-Lasinio, "Dynamical model of elementary particles based on an analogy with superconductivity. I," *Physical Review* **122** (1961) 345–358, and II, *Physical Review* **124** (1961) 246–254, for the four-fermion mechanism of dynamical mass generation.
- J. Goldstone, "Field theories with superconductor solutions," *Nuovo Cimento* **19** (1961) 154–164, for the Goldstone theorem and the counting of broken generators.
- S. Coleman and E. Weinberg, "Radiative corrections as the origin of spontaneous symmetry breaking," *Physical Review D* **7** (1973) 1888–1910, for dynamical symmetry breaking in the effective-potential language.
- M. Gell-Mann, R. J. Oakes, and B. Renner, "Behavior of current divergences under $SU(3)\times SU(3)$," *Physical Review* **175** (1968) 2195–2199, for the relation of the pion mass to the quark masses and the condensate.
- T. Banks and A. Casher, "Chiral symmetry breaking in confining theories," *Nuclear Physics B* **169** (1980) 103–125, for the relation between confinement and chiral symmetry breaking.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the chiral bilinears, the axial current, and the symmetry-breaking pattern.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 2 (Cambridge, 1996), for the Goldstone theorem and the effective chiral Lagrangian.
- E. V. Shuryak, *The QCD Vacuum, Hadrons and Superdense Matter* (World Scientific, 2004), for the quark condensate and its value.
- S. P. Klevansky, "The Nambu–Jona-Lasinio model of quantum chromodynamics," *Reviews of Modern Physics* **64** (1992) 649–708, for the gap equation, the critical coupling, and the mean-field condensate.
- V. A. Miransky, *Dynamical Symmetry Breaking in Quantum Field Theories* (World Scientific, 1993), for the nonperturbative treatment of the condensate.
