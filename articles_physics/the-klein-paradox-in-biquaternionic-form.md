# __The Klein Paradox in Biquaternionic Form__

## Introduction

The **Klein paradox** is the failure of the Dirac equation, read as a one-particle theory, at a sufficiently steep electrostatic potential step. Oskar Klein found in 1929 that an electron incident on a step of height $ϙV$ greater than twice its rest energy is not exponentially reflected as the non-relativistic theory requires: the reflection coefficient stays bounded, a substantial fraction of the wave penetrates the strong-potential region, and in the limit $ϙV \to \infty$ the transmission does not vanish. The one-particle theory cannot describe what happens in the step, because the resolution requires particle–antiparticle creation, which only a quantized field provides. The effect is now called **Klein tunnelling**, and its massless-limit form is observed in graphene $p$–$n$ junctions.

This article treats the Klein step in the biquaternion framework. The framework does not resolve the paradox — no one-particle equation can — but it locates the three structures the paradox involves. The electrostatic potential enters through the minimal coupling of the companion article and is **central**: it multiplies the field by a scalar times $e_t$ and does not act on the state module. The mass is the linear, chirality-off-diagonal term of the parent, and the mass shell $\frac{k_m^{2}\,\tilde{P}_{\Phi}\,\tilde{P}_{\Phi}^{\natural}}{m^{2}\,c^{2}}= -k_m^{2}$ has two roots, the two signs of frequency. The Klein region is exactly where the potential shifts the frequency past zero, so that the branch that is positive-frequency on the incident side continues into the negative-frequency root on the far side. That branch exchange, not any failure of the algebra, is what the paradox is about. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

The article is organised as follows. The next section writes the Dirac equation at a step and reduces it along one axis. The third section does the standard matching and gives the reflection and transmission coefficients, with the exact current conservation checked. The fourth states the paradox and its quantum-field-theoretic resolution. The fifth gives the biquaternion interpretation and separates what the algebra supplies from what it only transcribes. The sixth reports a worked numerical case and the massless limit. The closing sections are the open questions, the summary, the notation table and the literature.

The conventions are those of the companion articles. The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with units $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, $\vec e_\eta^2 = -e_t$, central scalar imaginary $i$; $\mathbb{B}_{\Psi}$ is the Hermitian and $\mathbb{B}_{\Phi}$ the anti-Hermitian subspace; the gradient is $\tilde\nabla = e_t\partial/\partial R_t + \vec e_x\partial/\partial R_x + \vec e_y\partial/\partial R_y + \vec e_z\partial/\partial R_z$; the biquaternion Dirac equation is the linear chiral pair $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R}$; and the minimal coupling replaces $\tilde\nabla$ by $D = \tilde\nabla +\frac{k_m\,i\,ϙ}{m\,c}\tilde{A}_{\Phi}$, acting by left multiplication.

## The Dirac Equation at a Potential Step

### Minimal coupling and the step

A static electrostatic potential $\xi(x)$ is the time component of the four-potential, $\tilde{A}_{\Phi} = i\,a'_te_t$ in the corpus's convention for the potential biquaternion, with no magnetic part. Inserted into the minimal-coupling prescription of the companion article, the covariant derivative is

$$
D = \tilde\nabla +\frac{k_m\,i\,ϙ}{m\,c}\tilde{A}_{\Phi} = \tilde\nabla +\frac{k_m\,i\,ϙ}{m\,c}\cdoti\,a'_te_t = \tilde\nabla -\frac{k_m\,ϙ\,a'_{t}}{m\,c}e_t .
$$

The added term is a **central scalar multiple of $e_t$**. This is the algebraic statement that an electrostatic potential couples to the scalar slot and not to the state module: it cannot rotate, mix or relatively phase the two chiral components of the field. The one-dimensional-scattering article makes the same point for the Schrödinger case, and the mechanism is identical here.

A **step** is the potential

$$
ϙ\xi(x) = V_0\,\mathrm{H}_{\mathrm{hvs}}(x),
$$

constant on each half-line and discontinuous at $x = 0$, with $V_0 > 0$ for a barrier that repels the electron. On each half-line the covariant derivative is a constant-shift of the gradient, so the equation has plane-wave solutions there and the problem reduces to matching across $x = 0$.

### Reduction along one axis

Take the particle to move along $x$ and to be in a spin state along the direction of motion. The spinor-module transcription of the biquaternion equation then reduces, as in the standard treatment of the step, to the two-component system

$$
\frac{m\,c^{2}\,i}{k_m}\,\frac{\partial\tilde{Ξ}_{\mathrm{sp},2}}{\partial x}=\left[E - mc^2 - V(x)\right]\tilde{Ξ}_{\mathrm{sp},1},
\qquad
\frac{m\,c^{2}\,i}{k_m}\,\frac{\partial\tilde{Ξ}_{\mathrm{sp},1}}{\partial x}=\left[E + mc^2 - V(x)\right]\tilde{Ξ}_{\mathrm{sp},2},
$$

in which $E$ is the total energy, $V(x) = V_0\mathrm{H}_{\mathrm{hvs}}(x)$ the potential energy, and the pair $(\tilde{Ξ}_{\mathrm{sp},1}, \tilde{Ξ}_{\mathrm{sp},2})$ is the two-component spinor of the reduced equation. This is the same two-component form the Klein paradox is usually solved in; the reduction is the one-dimensional instance of the parent's spinor-module picture, and the biquaternion field is recovered from the pair by the standing dictionary. The essential feature is already visible: the potential appears as the combination $E - V(x)$ multiplying the mass term, so a large $V$ drives that combination through zero and past $-m$.

## The Matching Problem

### The two regions

On the incident side, $x < 0$, the potential vanishes and the momentum is

$$
k_\Phi =\frac{\sqrt{E^2 -m^{2}\,c^{4}}}{\frac{m\,c^{2}}{k_m}},
$$

which is real for $E > mc^2$. The solution is an incident wave plus a reflected wave,

$$
\tilde{Ξ}_{\mathrm{sp},\mathrm{I}} = \exp(ikx)\begin{pmatrix}1\\ \alpha\end{pmatrix} + r\,\exp(-ikx)\begin{pmatrix}1\\ -\alpha\end{pmatrix},
\qquad
\alpha = \sqrt{\frac{E - mc^2}{E + mc^2}},
$$

so $0 < \alpha < 1$ for a massive particle, and $\alpha \to 1$ in the massless limit. On the far side, $x > 0$, the potential is $V_0$ and the momentum is

$$
k_2 = -\frac{\sqrt{(V_0 - E)^2 -m^{2}\,c^{4}}}{\frac{m\,c^{2}}{k_m}},
\qquad
\tilde{Ξ}_{\mathrm{sp},\mathrm{II}} = t\,\exp(ik_2x)\begin{pmatrix}1\\ 1/\beta\end{pmatrix},
\qquad
\beta = \sqrt{\frac{V_0 - E - mc^2}{V_0 - E + mc^2}} .
$$

The sign of $k_2$ is chosen so that the transmitted wave carries current to the right when $V_0 - E > mc^2$; this is the **Klein region**, where the energy measured from the top of the step is more negative than $-mc^2$ and the local state is a negative-frequency one. Both $\alpha$ and $\beta$ lie in $(0,1)$ for a massive particle in the Klein region.

### Reflection and transmission

Continuity of the two components at $x = 0$ gives the two matching conditions

$$
1 + r = t, \qquad \alpha(1 - r) = \frac{t}{\beta},
$$

whose solution is

$$
\boxed{\;r = \frac{\alpha\beta - 1}{\alpha\beta + 1},
\qquad
R = r^2 = \left(\frac{\alpha\beta - 1}{\alpha\beta + 1}\right)^2,
\qquad
T = 1 - R = \frac{4\alpha\beta}{(\alpha\beta + 1)^2}\;}.
$$

The current of the reduced equation is $j^x \propto \mathrm{Re}(\tilde{Ξ}_{\mathrm{sp},1}^*\tilde{Ξ}_{\mathrm{sp},2})$, so the incident flux is $2\alpha$, the reflected flux $2\alpha r^2$ and the transmitted flux $2t^2/\beta$. The matching conditions make current conservation an identity,

$$
2\alpha\left(1 - r^2\right) = \frac{2}{\beta}\,t^2 ,
$$

which was verified exactly on the cases below, so that $T$ as defined above is the genuine current transmission and no flux is lost.

### The Klein region and the paradox

Two features distinguish this from the non-relativistic step. First, **the reflection does not tend to one as the step grows**. The parameter $\beta$ is bounded above by one and increases to one as $V_0 \to \infty$; hence $r$ tends to the finite limit $(\alpha - 1)/(\alpha + 1)$, and

$$
\boxed{\;\lim_{V_0\to\infty} R = \left(\frac{\alpha - 1}{\alpha + 1}\right)^2, \qquad
\lim_{V_0\to\infty} T = \frac{4\alpha}{(\alpha + 1)^2}\;},
$$

both strictly between zero and one for $0 < \alpha < 1$. The step becomes more transparent as it grows, not less. Second, in the **massless limit** $\alpha = \beta = 1$ exactly, so $r = 0$ and $T = 1$ for every step height: a massless Dirac particle passes through any electrostatic step with unit transmission. This is Klein tunnelling in its cleanest form, and it is the reason the effect is seen in graphene.

The resolution of the apparent paradox is a matter of particle number, not of the algebra. A current conservation law with the transmitted current carried by a state of negative frequency relative to the far side means that the far side is not reached by the incident electron alone; the potential step, if steep enough over a Compton wavelength, creates electron–positron pairs, and the transmitted current is a positron current flowing away from the step. The one-particle calculation above is a bookkeeping of a current, not a history of one particle, and it is exactly consistent once pair creation is allowed. In a quantized field the step is a source of pairs, and the reflection coefficient computed in the single-particle theory is the elastic amplitude in the presence of that source.

## The Biquaternion Reading

### The potential acts on the centre, the mass on the chiralities

Two algebraic facts organise the problem, and they were established in the companion articles. The potential term is central — a scalar multiple of $e_t$ — so it acts trivially on the state module and only shifts the mass shell. The mass term is the linear, chirality-off-diagonal pair $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R}$, the one term of the equation that relates its two components. The two ingredients of the Klein problem therefore act in orthogonal places: the potential is a central shift, the mass is a chirality mixing. The paradox is not caused by either alone but by the fact that the central shift can move the frequency past the mass gap, into the region where the two mass-shell roots exchange their roles.

**The converse step.** A step in the mass is the other case: the mass is the chirality-mixing term of the pair, so a position-dependent mass shifts no frequency and cannot exchange the two mass-shell roots. When the local mass exceeds the energy the transmitted wave is evanescent rather than negative-frequency, the reflection is total, and the field penetrates the region of large mass only to a depth $1/\sqrt{M^2c^4-E^2}$, an inverse length. That is the confinement mechanism of the bag models of Bardeen, Chanowitz, Drell, Weinstein and Yan (1975), which use a scalar mass step rather than an electrostatic one for exactly this reason: a scalar step has no Klein threshold.

### The mass shell and the exchange of branches

The free mass shell is

$$
\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}= -m^{2}\,c^{2},
\qquad
\tilde K_{\Phi} = i\frac{\omega}{c}e_t + \vec e_x k_\Phi ,
$$

whose two roots $\omega = \pm\sqrt{k^2c^2 +m^{2}\,c^{4}}\frac{k_m}{m\,c}$ are the two frequency branches of the parent: the particle and the antiparticle. Under the central shift the covariant wave biquaternion acquires the constant shift from the potential, and the on-shell condition reads, on each half-line, the same relation with the frequency measured from the local potential. On the incident side the incident wave lies on the positive root. On the far side of a Klein step the same wave has $E - V_0 < -mc^2$, so it lies on the **negative root** of the local mass shell. The step has taken the propagating branch and exchanged it with its conjugate:

$$
\boxed{\;\omega \;\longmapsto\; \omega -\frac{k_m\,ϙ\,\xi}{m\,c} \quad\text{with}\quad  \omega -\frac{k_m\,ϙ\,\xi}{m\,c} < 0\;}.
$$

This is the algebraic content of the phrase "the far side is reached by an antiparticle". The exchange of the two roots is the same operation that the corpus's conjugation articles study as charge conjugation and the real structure $\flat$; here it is produced not by conjugation of the field but by a central shift of the momentum, which is why the framework can describe it without leaving the algebra. What the framework cannot do is change the particle number; that is the second-quantized statement, and it belongs to the companion articles on the Dirac sea and on pair creation. Here $k_{\Phi}=\frac{k_m\,p}{m\,c}$ is the momentum wave number.

### The same exchange for a bound level

**The step and the well are one mechanism.** In the step the exchanged branch belongs to a scattering state, and the pair it signals leaves the step for infinity. Confine the strong-potential region instead, and the exchange becomes a statement about a **bound level**: the level descends as the well deepens, and at a definite depth it reaches the lower edge of the gap, $E=-mc^{2}$. That depth is exact and elementary, and it is the one-particle face of the threshold computed here. The second-quantized reading, including the charged vacuum that the emission leaves behind, is that of *Pair Creation in a Bounded Region in Biquaternionic Form*; here only the level is computed.

**The well and its two conditions.** Take $ϙ\xi(r_x)=-V_0$ for $\lvert r_x\rvert<L/2$ and zero outside, and write $a=L/2$. On each region the reduced pair of §*Reduction along one axis* holds with $E\to E+V_0$ inside the well, so the solution is oscillatory there with the wave number $k_{\Phi,\mathrm{w}}=\frac{\sqrt{(E+V_0)^{2}-m^{2}c^{4}}}{\hbar c}$ and evanescent outside with the decay constant $k_{\Phi,\mathrm{ev}}=\frac{\sqrt{m^{2}c^{4}-E^{2}}}{\hbar c}$. Continuity of the ratio of the two components at the wall gives, for the even and the odd solution,

$$
\frac{k_{\Phi,\mathrm{ev}}}{E+mc^{2}}=\frac{k_{\Phi,\mathrm{w}}\tan(k_{\Phi,\mathrm{w}}a)}{E+V_0+mc^{2}},
\qquad
\frac{k_{\Phi,\mathrm{ev}}}{E+mc^{2}}=-\frac{k_{\Phi,\mathrm{w}}\cot(k_{\Phi,\mathrm{w}}a)}{E+V_0+mc^{2}},
$$

which is the continuity statement that this article writes for the transmitted amplitude, read at a wall instead of at a discontinuity, with the exponential tail kept. No approximation enters.

**The threshold.** At the lower edge the decay constant vanishes while the factor $E+mc^{2}$ vanishes faster, so the left side diverges and the two conditions reduce to $\cos(k_{\Phi,\mathrm{w}}a)=0$ and $\sin(k_{\Phi,\mathrm{w}}a)=0$. Both give $k_{\Phi,\mathrm{w}}a=n_{\mathrm{w}}\pi/2$, with $n_{\mathrm{w}}=1,2,3,\dots$ counting half-wavelengths across the well; odd $n_{\mathrm{w}}$ is the even solution, and the nodeless state is $n_{\mathrm{w}}=1$. At that energy $k_{\Phi,\mathrm{w}}^{2}=((V_0-mc^{2})^{2}-m^{2}c^{4})/(\hbar c)^{2}$, so the depth follows:

$$
\boxed{\;V_0^{\mathrm{cr}}=mc^{2}\left[1+\sqrt{1+\left(\frac{n_{\mathrm{w}}\pi}{k_mL}\right)^{2}}\;\right]\;}
$$

**What the formula says.** The threshold depends on $n_{\mathrm{w}}$ and $L$ only through the ratio $n_{\mathrm{w}}/(k_mL)$, so the $n_{\mathrm{w}}$-th level of a well of width $L$ dives at the depth of the first level of a well of width $L/n_{\mathrm{w}}$. It lies above $2mc^{2}$ for every finite width, and the excess is the confinement energy of the standing wave, $\frac{n_{\mathrm{w}}^{2}\pi^{2}\hbar^{2}}{2mL^{2}}$ at leading order, so a bounded region needs a deeper potential than a step by the price of confining the charge to it. And as $L\to\infty$ the threshold tends to $2mc^{2}$. That floor is the same number as this article's critical height, $V_0>E+mc^{2}$ with $E\to mc^{2}$, and the agreement is in the number only: $2mc^{2}$ is the least potential that brings an edge of one branch onto an edge of the other, and the well reaches it with a bound level at the lower edge of the gap while the step reaches it with a scattering state at the upper edge. The threshold of a finite well is that floor plus the confinement energy of the standing wave.

**The numbers.** The matching conditions were solved numerically and the closed form confirmed. For $k_mL=10$ the formula gives $V_0^{\mathrm{cr}}=2.048187\,mc^{2}$; the lowest even level sits at $E=-0.990625\,mc^{2}$ at $V_0=2.038187\,mc^{2}$ and at $E=-0.999185\,mc^{2}$ at $V_0=2.047187\,mc^{2}$, approaching the edge without a jump; at $V_0^{\mathrm{cr}}$ the even condition vanishes at $E=-mc^{2}$ to $3\times10^{-10}$; and above it no even level remains in the gap, the lowest one there being the next state up, at $E=-0.697067\,mc^{2}$ for $V_0=V_0^{\mathrm{cr}}+10^{-3}mc^{2}$. The odd level crosses at $n_{\mathrm{w}}=2$, $V_0^{\mathrm{cr}}=2.181010\,mc^{2}$ for $k_mL=10$, which is the $n_{\mathrm{w}}=1$ depth of $k_mL=5$; the scaling is exact to the printed digits. The table gives the depths.

| $k_mL$ | $n_{\mathrm{w}}=1$ | $n_{\mathrm{w}}=2$ | $n_{\mathrm{w}}=3$ | excess at $n_{\mathrm{w}}=1$ |
|---|---|---|---|---|
| $5$ | $2.181010$ | $2.605969$ | $3.133789$ | $0.181010$ |
| $10$ | $2.048187$ | $2.181010$ | $2.374141$ | $0.048187$ |
| $20$ | $2.012262$ | $2.048187$ | $2.105471$ | $0.012262$ |
| $40$ | $2.003080$ | $2.012262$ | $2.027383$ | $0.003080$ |
| $\infty$ | $2$ | $2$ | $2$ | $0$ |

**What the crossing means.** Below the threshold the level is a normalizable state of the well. At the threshold it is degenerate with the lower continuum, and above it there is no normalizable state of that parity in the gap at all: the level has dived. The one-particle equation has not failed, since it still has solutions; what has failed is that any of them is normalisable, and with it the identification of a solution with the ground state of one electron. That is the same failure this article finds at the step. The difference is the bookkeeping. At the step the pair is emitted as a current and the account is closed at infinity; in a bounded region the same emission leaves a charge behind, held by one level, and it stays there for as long as the depth is maintained. That is why the bounded case, and not the step, is where the phrase *charged vacuum* becomes exact.

### The current lives in the material sector

The conserved current of the framework is the material-sector object $\tilde J_{\Phi} = ic\,j_0e_t + \vec j \in \mathbb{B}_{\Phi}$, as in the parent and the scattering articles. The matching problem solved here is the statement of the continuity of that current across the step. In the Klein region the sign of the transmitted current is not the sign of the incident charge current; the biquaternion current is conserved, and it is the identification of that current with the transport of one electron that fails. The algebra records the conservation faithfully and leaves the particle interpretation to the field theory.

### What the biquaternion form does not supply

Stated plainly: the biquaternion framework **transcribes** the Klein problem and locates its three ingredients — the central potential, the chirality-mixing mass, the two-rooted mass shell — but it does **not** resolve the paradox. The resolution is pair creation, which requires a many-particle Hilbert space and cannot be stated by a one-particle wave equation in any algebra. Any claim that the complexification or the sector split dissolves the paradox would be false; the one-particle equation has the same coefficients here as in the standard treatment, and they are the ones that show the paradox. What the framework adds is the sharp statement of *why* the resolution is needed: the potential is central and the mass is chiral, so the step can move a state from one mass-shell root to the other while leaving the algebra's structure untouched, and only the occupation of the roots — a field-theoretic datum — can say what that means.

## A Worked Case

The formulas were checked on cases chosen here rather than on the step that motivated the paradox. Take $E=2mc^2$ and measure masses in units of $m$, momenta in units of $mc$ and energies in units of $mc^2$, so that every entry below is a pure number; then $\alpha = \sqrt{1/3} = 0.577350$. Current conservation held to machine precision on every case below, and the limits were confirmed.

| $V_0/m$ | $\beta$ | $r$ | $R$ | $T$ |
|---|---|---|---|---|
| $5$ | $0.707107$ | $-0.420204$ | $0.176571$ | $0.823429$ |
| $10$ | $0.881917$ | $-0.325227$ | $0.105773$ | $0.894227$ |
| $100$ | $0.989847$ | $-0.272679$ | $0.074354$ | $0.925646$ |
| $\infty$ | $1$ | $-0.267949$ | $0.071797$ | $0.928203$ |

The reflection **decreases** as the step rises, from $0.177$ at $V_0 = 5m$ to $0.072$ in the infinite-step limit, instead of approaching one. For $m = 0$ the same computation gives $\alpha = \beta = 1$, $r = 0$, $R = 0$, $T = 1$ exactly, independent of $V_0$: perfect transmission. Both statements are the standard ones, reproduced in the framework's notation.

## Open Questions

1. **The biquaternion form of the pair-creation source.** The resolution of the paradox is that the step creates pairs. The scalar analogue is treated in the companion article on scalar pair creation; the fermionic biquaternion treatment of a step as a pair source, with the anomalous occupation of the two mass-shell roots, is not yet written. The bounded case is the one place where the question is reduced to a single number rather than to a flux: *Pair Creation in a Bounded Region in Biquaternionic Form* computes the depth at which the level crosses into the lower continuum, and what remains is the occupation of that level, which is still a second-quantized datum.

2. **The steepness.** Sauter showed that a step smoothed over a Compton wavelength removes the paradox. How does the smoothing enter the biquaternion equation — as a position-dependent central shift of the mass shell, or as a modification of the gradient itself?

3. **The sector of the transmitted component.** In the material-sector picture the current is $\mathbb{B}_{\Phi}$-valued. The transmitted "antiparticle" component of the far-side wave is a negative-frequency solution; is there a sector statement that distinguishes it from the incident component, or is the distinction purely one of the sign of $\omega$?

4. **The graphene transcription.** In graphene the Dirac points are massless and the potential step is a $p$–$n$ junction. The massless limit here is a clean $T = 1$; whether the biquaternion framework supplies anything beyond the massless Weyl equation for the two Dirac points is the question taken up in the companion article on Dirac matter.

5. **The strong-field scale.** The field required for the paradox with electrons is enormous, of order $10^{16}$ V/cm, and is realized only for very heavy nuclei or near horizons. Whether any of the framework's constants supplies a natural scale for the onset is open.

## Summary

The Klein step is the Dirac equation with a central potential $ϙ\xi(x) = V_0\mathrm{H}_{\mathrm{hvs}}(x)$, solved by matching two-component plane waves. The reflection coefficient is $R = ((\alpha\beta - 1)/(\alpha\beta + 1))^2$ and the transmission $T = 4\alpha\beta/(\alpha\beta + 1)^2$, with $\alpha = \sqrt{(E - mc^2)/(E + mc^2)}$ and $\beta = \sqrt{(V_0 - E - mc^2)/(V_0 - E + mc^2)}$; current conservation is an identity, checked on the cases tabulated. In the Klein region $V_0 - E > mc^2$ the transmitted wave is a negative-frequency state, and $R$ tends to the finite value $((\alpha - 1)/(\alpha + 1))^2$ as $V_0\to\infty$ rather than to one; in the massless limit $\alpha = \beta = 1$ and $T = 1$ for every step height.

The biquaternion framework locates the three ingredients: the potential is central and shifts the mass shell without acting on the module; the mass is the linear chirality-off-diagonal term; and the mass shell $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural} = -m^{2}\,c^{2}$ has two roots, which the step exchanges. In a bounded region the same shift is read on a bound level, and the level reaches the lower edge of the gap at $V_0^{\mathrm{cr}}=mc^{2}[1+\sqrt{1+(n_{\mathrm{w}}\pi/(k_mL))^{2}}\,]$, which exceeds $2mc^{2}$ by the confinement energy and tends to the common floor $2mc^{2}$ as the width grows; the details are in *Pair Creation in a Bounded Region in Biquaternionic Form*. The exchange of roots is the algebraic face of the passage to the antiparticle branch, and it is produced by a central shift rather than by a conjugation of the field. The framework does not resolve the paradox, because the resolution is pair creation, a second-quantized statement; the one-particle coefficients are the standard ones. What the framework supplies is the clean separation of a central potential, a chiral mass and a two-rooted mass shell, which is exactly the structure the paradox tests.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\eta^2 = -e_t$ |
| $\tilde\nabla = e_t\partial/\partial R_t + \sum_{\eta=x,y,z}\vec e_\eta\,\partial/\partial R_\eta$ | Biquaternionic gradient |
| $D = \tilde\nabla +\frac{k_m\,i\,ϙ}{m\,c}\tilde{A}_{\Phi}$ | Covariant derivative (minimal coupling) |
| $\tilde{A}_{\Phi} = i\,a'_te_t$ | Electrostatic potential biquaternion |
| $V_0$, $ϙ\xi(x) = V_0\mathrm{H}_{\mathrm{hvs}}(x)$ | Step height and potential energy |
| $E$, $k_\Phi$, $k_{\Phi,2}$ | Energy, incident momentum, transmitted momentum |
| $\alpha = \sqrt{(E - mc^2)/(E + mc^2)}$ | Incident-side spinor parameter |
| $\beta = \sqrt{(V_0 - E - mc^2)/(V_0 - E + mc^2)}$ | Far-side spinor parameter |
| $r$, $t$, $R$, $T$ | Reflection and transmission amplitudes and probabilities |
| $\tilde K_{\Phi}$, $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural} = -m^{2}\,c^{2}$ | Wave biquaternion and mass shell |
| $V_0^{\mathrm{cr}}=mc^{2}[1+\sqrt{1+(n_{\mathrm{w}}\pi/(k_mL))^{2}}\,]$ | Depth at which a bound level of a well of width $L$ reaches $E=-mc^{2}$ |
| $n_{\mathrm{w}}$, $k_{\Phi,\mathrm{w}}$, $k_{\Phi,\mathrm{ev}}$ | Half-wavelengths across the well; wave number in the well; decay constant outside it |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian (material) sector; home of the current |

## Further Reading

- O. Klein, "Die Reflexion von Elektronen an einem Potentialsprung nach der relativistischen Dynamik von Dirac," *Zeitschrift für Physik* **53** (1929) 157–165, for the original paradox.
- F. Sauter, "Über das Verhalten eines Elektrons im homogenen elektrischen Feld nach der relativistischen Theorie Diracs," *Zeitschrift für Physik* **69** (1931) 742–764, for the smoothed step and the removal of the paradox.
- A. Calogeracos and N. Dombey, "History and physics of the Klein paradox," *Contemporary Physics* **40** (1999) 313–321, for the history and the modern account.
- A. Hansen and F. Ravndal, "Klein's paradox and its resolution," *Physica Scripta* **23** (1981) 1036–1042, for the field-theoretic treatment.
- B. R. Holstein, "Klein's paradox," *American Journal of Physics* **66** (1998) 507–512, for a pedagogical derivation.
- M. I. Katsnelson, K. S. Novoselov and A. K. Geim, "Chiral tunnelling and the Klein paradox in graphene," *Nature Physics* **2** (2006) 620–625, for the massless-limit realization.
- W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 2000), for the step, the barrier and the Klein region in detail.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the potential-step problem and the hole-theoretic interpretation.
- The companion articles of this series: [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), [One-Dimensional Scattering in Biquaternionic Form](one-dimensional-scattering-in-biquaternionic-form.html), and [The Dirac Sea, Hole Theory and Antimatter in Biquaternionic Form](the-dirac-sea-hole-theory-and-antimatter-in-biquaternionic-form.html).
