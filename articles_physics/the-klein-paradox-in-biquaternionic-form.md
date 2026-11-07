# __The Klein Paradox in Biquaternionic Form__

## Introduction

The **Klein paradox** is the failure of the Dirac equation, read as a one-particle theory, at a sufficiently steep electrostatic potential step. Oskar Klein found in 1929 that an electron incident on a step of height $V_0$ greater than twice its rest energy is not exponentially reflected as the non-relativistic theory requires: the reflection coefficient stays bounded, a substantial fraction of the wave penetrates the strong-potential region, and in the limit $V_0 \to \infty$ the transmission does not vanish. The one-particle theory cannot describe what happens in the step, because the resolution requires particle–antiparticle creation, which only a quantized field provides. The effect is now called **Klein tunnelling**, and its massless-limit form is observed in graphene $p$–$n$ junctions.

This article treats the Klein step in the biquaternion framework. The framework does not resolve the paradox — no one-particle equation can — but it locates the three structures the paradox involves. The electrostatic potential enters through the minimal coupling of the companion article and is **central**: it multiplies the field by a scalar times $e_t$ and does not act on the state module. The mass is the linear, chirality-off-diagonal term of the parent, and the mass shell of the wave element $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar$, that is $\langle\tilde K_{\Phi}\rangle_{\natural}=-k_m^{2}$, has two roots, the two signs of frequency. The Klein region is exactly where the potential shifts the frequency past zero, so that the branch that is positive-frequency on the incident side continues into the negative-frequency root on the far side. That branch exchange, not any failure of the algebra, is what the paradox is about. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

The article is organised as follows. The next section writes the Dirac equation at a step and reduces it along one axis. The third section does the standard matching and gives the reflection and transmission coefficients, with the exact current conservation checked. The fourth states the paradox and its quantum-field-theoretic resolution. The fifth gives the biquaternion interpretation and separates what the algebra supplies from what it only transcribes. The sixth reports a worked numerical case and the massless limit. The closing sections are the open questions, the summary, the notation table and the literature.

The conventions are those of the companion articles. The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with units $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, $\vec e_k^2 = -e_t$, central scalar imaginary $i$; $\mathbb{B}_{\Psi}$ is the Hermitian and $\mathbb{B}_{\Phi}$ the anti-Hermitian subspace; the gradient is $\tilde\nabla = e_t\partial/\partial R_t + \vec e_x\partial/\partial R_x + \vec e_y\partial/\partial R_y + \vec e_z\partial/\partial R_z$; the biquaternion Dirac equation is the linear chiral pair $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R}$; and the minimal coupling replaces $\tilde\nabla$ by $D = \tilde\nabla +\frac{k_m\,i\,ϙ}{m\,c}\tilde{A}_{\Phi}$, acting by left multiplication. The wave element of a plane wave is one division of the four-momentum, $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar=i k_{t}^{\prime}e_t+\vec k_{\Phi}$ with $k_{t}^{\prime}=\omega/c=E/(\hbar c)$ and $\vec k_{\Phi}=\vec p/\hbar$, both coordinates inverse lengths; the gradient on such a wave is left multiplication by $i\tilde K_{\Phi}$, and every coefficient displayed below is read off $\tilde K_{\Phi}$ and its norm $\langle\tilde K_{\Phi}\rangle_{\natural}$ rather than off the momentum it was divided from.

## The Dirac Equation at a Potential Step

### Minimal coupling and the step

A static electrostatic potential $\xi(x)$ is the time component of the four-potential, $\tilde{A}_{\Phi} = i\,a'_te_t$ in the corpus's convention for the potential biquaternion, its temporal coefficient $a'_t=\xi/c$ carrying the potential divided by $c$ so that $\varrho\,a'_t$ is a momentum, with no magnetic part. Inserted into the minimal-coupling prescription of the companion article, the covariant derivative is

$$
D = \tilde\nabla +\frac{k_m\,i\,ϙ}{m\,c}\tilde{A}_{\Phi} = \tilde\nabla +\frac{k_m\,i\,ϙ}{m\,c}\,i\,a'_te_t = \tilde\nabla -\frac{ϙ\,a'_{t}}{\hbar}e_t = \tilde\nabla +\frac{V}{c\,\hbar}e_t .
$$

The added term is a **central scalar multiple of $e_t$**, and it is an inverse length, as every coefficient added to the gradient must be. Two conversions and no others carry the units: $k_m/(mc)=1/\hbar$ turns the momentum $\varrho a'_t$ into an inverse length, and $a'_t=\xi/c$ turns the potential into a momentum. Write $V:=-\varrho\xi$ for the potential energy of the particle as the corpus's coupling carries it, the sign being a convention fixed once here, so that a barrier that repels the electron has $V_0>0$. The added term is then $+V/(c\hbar)e_t$, and on a plane wave it lowers the temporal wave number from $k_{t}^{\prime}$ to $k_{t}^{\prime}-V/(c\hbar)$, which is the shift the section on the mass shell reads. This is the algebraic statement that an electrostatic potential couples to the scalar slot and not to the state module: it cannot rotate, mix or relatively phase the two chiral components of the field. The one-dimensional-scattering article makes the same point for the Schrödinger case, and the mechanism is identical here.

A **step** is the potential

$$
V(x) = -\varrho\,\xi(x) = V_0\,\mathrm{H}_{\mathrm{hvs}}(x),
$$

constant on each half-line and discontinuous at $x = 0$, with $V_0 > 0$ for a barrier that repels the electron. On each half-line the covariant derivative is a constant-shift of the gradient, so the equation has plane-wave solutions there and the problem reduces to matching across $x = 0$.

### Reduction along one axis

Take the particle to move along $x$ and to be in a spin state along the direction of motion. The spinor-module transcription of the biquaternion equation then reduces, as in the standard treatment of the step, to the two-component system

$$
-i\,c\hbar\,\frac{\partial\tilde{Ξ}_{\mathrm{sp},2}}{\partial x} = \left[E - mc^2 - V(x)\right]\tilde{Ξ}_{\mathrm{sp},1},\qquad
-i\,c\hbar\,\frac{\partial\tilde{Ξ}_{\mathrm{sp},1}}{\partial x} = \left[E + mc^2 - V(x)\right]\tilde{Ξ}_{\mathrm{sp},2},
$$

in which $E$ is the total energy, $V(x) = V_0\mathrm{H}_{\mathrm{hvs}}(x)$ the potential energy, and the pair $(\tilde{Ξ}_{\mathrm{sp},1}, \tilde{Ξ}_{\mathrm{sp},2})$ is the two-component spinor of the reduced equation. The factor $c\hbar$ is the product that turns one inverse length into one energy, $c\hbar=mc^{2}/k_m$; the earlier display wrote it as a division by $k_mx$, which buried the derivative, and it carried the bare $+i$, which with the incident wave $e^{ikx}$ and $\alpha>0$ satisfies neither line: the derivative term is $-i c\hbar\,\partial_x$, the sign that makes the pair the standard Dirac matrix $c\vec\alpha\cdot\vec p$ with $\beta=\mathrm{diag}(1,-1)$ on the two parts. This is the same two-component form the Klein paradox is usually solved in; the reduction is the one-dimensional instance of the parent's spinor-module picture, and the biquaternion field is recovered from the pair by the standing dictionary. The essential feature is already visible: the potential appears as the combination $E - V(x)$, that is the temporal wave number $k_{t}^{\prime}-V(x)/(\hbar c)$ measured from the local potential, so a large $V$ drives that wave number through zero and past $-k_m$.

## The Matching Problem

### The two regions

On the incident side, $x < 0$, the potential vanishes and the wave number is

$$
k_{x}=\sqrt{k_{t}^{\prime\,2}-k_m^{2}}=\frac{\sqrt{E^2-m^{2}\,c^{4}}}{\hbar\,c},
$$

which is real for $E > mc^2$. The solution is an incident wave plus a reflected wave,

$$
\tilde{Ξ}_{\mathrm{sp},\mathrm{I}} = \exp(ik_{x}x)\begin{pmatrix}1\\ \alpha\end{pmatrix} + r\,\exp(-ik_{x}x)\begin{pmatrix}1\\ -\alpha\end{pmatrix},
\qquad
\alpha = \sqrt{\frac{E - mc^2}{E + mc^2}},
$$

so $0 < \alpha < 1$ for a massive particle, and $\alpha \to 1$ in the massless limit. In wave numbers $\alpha=\sqrt{(k_{t}^{\prime}-k_m)/(k_{t}^{\prime}+k_m)}$, the same number, because numerator and denominator are both multiplied by the single factor $\hbar c$. On the far side, $x > 0$, the potential is $V_0$ and the wave number is

$$
k_{2x} = -\sqrt{\left(\frac{V_0}{\hbar\,c}-k_{t}^{\prime}\right)^{2}-k_m^{2}}=-\frac{\sqrt{(V_0-E)^2-m^{2}\,c^{4}}}{\hbar\,c},
\qquad
\tilde{Ξ}_{\mathrm{sp},\mathrm{II}} = t\,\exp(ik_{2x}x)\begin{pmatrix}1\\ 1/\beta\end{pmatrix},
\qquad
\beta = \sqrt{\frac{V_0 - E - mc^{2}}{V_0 - E + mc^{2}}}=\sqrt{\frac{k_V-k_m}{k_V+k_m}} .
$$

The sign of $k_{2x}$ is chosen so that the transmitted wave carries current to the right when $V_0 - E > mc^2$; this is the **Klein region**, where $k_V:=V_0/(\hbar c)-k_{t}^{\prime}$ is the magnitude of the local temporal wave number, larger than $k_m$, so that the energy measured from the top of the step is more negative than $-mc^{2}$ and the local state is a negative-frequency one. Both $\alpha$ and $\beta$ lie in $(0,1)$ for a massive particle in the Klein region.

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

Two algebraic facts organise the problem, and they were established in the companion articles. The potential term is central — a scalar multiple of $e_t$ — so it acts trivially on the state module and only shifts the mass shell. The mass term is the linear, chirality-off-diagonal pair $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R}$, the one term that couples the two minimal left ideals. The two ingredients of the Klein problem therefore act in orthogonal places: the potential is a central shift, the mass is a chirality mixing. The paradox is not caused by either alone but by the fact that the central shift can move the frequency past the mass gap, into the region where the two mass-shell roots exchange their roles.

**The converse step.** A step in the mass is the other case: the mass is the chirality-mixing term of the pair, so a position-dependent mass shifts no frequency and cannot exchange the two mass-shell roots. When the local mass exceeds the energy the transmitted wave is evanescent rather than negative-frequency, the reflection is total, and the field penetrates the region of large mass only to a depth $\hbar c/\sqrt{M^{2}c^{4}-E^{2}}=1/\sqrt{k_M^{2}-k_{t}^{\prime\,2}}$, with $k_M=Mc/\hbar$, an inverse length. That is the confinement mechanism of the bag models of Bardeen, Chanowitz, Drell, Weinstein and Yang (1974), which use a scalar mass step rather than an electrostatic one for exactly this reason: a scalar step has no Klein threshold.

### The mass shell and the exchange of branches

The wave element of a plane wave is one division of the four-momentum,

$$
\tilde K_{\Phi}=\frac{\tilde P_{\Phi}}{\hbar}=i\,k_{t}^{\prime}e_t+\vec e_x\,k_{\Phi},
\qquad
k_{t}^{\prime}=\frac{\omega}{c}=\frac{E}{\hbar\,c},
\qquad
k_{\Phi}=\frac{p}{\hbar},
$$

an element of the material sector whose two coordinates are inverse lengths, the temporal one and the magnitude of the spatial three-vector. The free mass shell is one line on it,

$$
\langle\tilde K_{\Phi}\rangle_{\natural}=-k_{t}^{\prime\,2}+k_{\Phi}^{2}=-k_m^{2},
\qquad\text{that is}\qquad
k_{t}^{\prime\,2}=k_{\Phi}^{2}+k_m^{2},
$$

whose two roots $k_{t}^{\prime}=\pm\sqrt{k_{\Phi}^{2}+k_m^{2}}$, that is $\omega=\pm c\sqrt{k_{\Phi}^{2}+k_m^{2}}$, are the two frequency branches of the parent: the particle and the antiparticle. In the one-dimensional problem of the two preceding sections the spatial coordinate of $\vec k_{\Phi}$ is $k_{x}$ on the incident side and $|k_{2x}|$ on the far side, so that the two shells read $k_{t}^{\prime\,2}=k_{x}^{2}+k_m^{2}$ and $(k_{t}^{\prime}-V_0/(\hbar c))^{2}=k_{2x}^{2}+k_m^{2}$. Under the central shift the wave element acquires the constant shift of the potential, $\tilde K_{\Phi}\mapsto\tilde K_{\Phi}-i\frac{V}{c\hbar}e_t$, so that its temporal coordinate is $k_{t}^{\prime}-V/(c\hbar)$ and the on-shell condition reads, on each half-line, the same relation with the wave number measured from the local potential. On the incident side the incident wave lies on the positive root. On the far side of a Klein step the same wave has $E-V_0<-mc^{2}$, so its local temporal wave number is below $-k_m$ and it lies on the **negative root** of the local mass shell. The step has taken the propagating branch and exchanged it with its conjugate:

$$
\boxed{\;k_{t}^{\prime}\;\longmapsto\;k_{t}^{\prime}-\frac{V}{c\,\hbar}=\frac{E-V}{c\,\hbar}
\quad\text{with}\quad
\frac{E-V}{c\,\hbar}<0\;},
$$

equivalently $\omega\mapsto\omega-V/\hbar$, a shift of a frequency by an energy over $\hbar$ and of a wave number by the same energy over $c\hbar$. This is the algebraic content of the phrase "the far side is reached by an antiparticle". The exchange of the two roots is the same operation that the corpus's conjugation articles study as charge conjugation and the real structure $\flat$; here it is produced not by conjugation of the field but by a central shift of the wave element, which is why the framework can describe it without leaving the algebra. What the framework cannot do is change the particle number; that is the second-quantized statement, and it belongs to the companion articles on the Dirac sea and on pair creation.

**What the earlier display did.** It gave the mass shell as $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}=-m^{2}c^{2}$ beside a second line $\tilde P_{\Phi}\,k_{\mathrm{mo}}=i\frac{\omega}{c}e_t+\vec e_xk$ with $k_{\mathrm{mo}}=k_mp/(mc)$ called the momentum length, and it wrote the roots as $\omega=\pm\sqrt{k^{2}c^{2}+m^{2}c^{4}}\,\frac{k_m}{mc}$. Three errors follow. The factor $k_{\mathrm{mo}}=k_mp/(mc)=p/\hbar$ is the magnitude of the wave number, an inverse length, so it is neither a momentum nor a length. The product $\tilde P_{\Phi}k_{\mathrm{mo}}$ therefore carries a momentum per length, and cannot be the inverse-length element written on its right. And $\frac{k_m}{mc}=1/\hbar$, so the roots carried a disguised division by $\hbar$ in place of the one division the wave element makes. The two lines are now one line, on $\tilde K_{\Phi}$.

### The current lives in the material sector

The conserved current of the framework is the material-sector object $\tilde J_{\Phi} = ic\,j_0e_t + \vec j \in \mathbb{B}_{\Phi}$, as in the parent and the scattering articles. The matching problem solved here is the statement of the continuity of that current across the step. In the Klein region the sign of the transmitted current is not the sign of the incident charge current; the biquaternion current is conserved, and it is the identification of that current with the transport of one electron that fails. The algebra records the conservation faithfully and leaves the particle interpretation to the field theory.

### What the biquaternion form does not supply

Stated plainly: the biquaternion framework **transcribes** the Klein problem and locates its three ingredients — the central potential, the chirality-mixing mass, the two-rooted mass shell — but it does **not** resolve the paradox. The resolution is pair creation, which requires a many-particle Hilbert space and cannot be stated by a one-particle wave equation in any algebra. Any claim that the complexification or the sector split dissolves the paradox would be false; the one-particle equation has the same coefficients here as in the standard treatment, and they are the ones that show the paradox. What the framework adds is the sharp statement of *why* the resolution is needed: the potential is central and the mass is chiral, so the step can move a state from one mass-shell root to the other while leaving the algebra's structure untouched, and only the occupation of the roots — a field-theoretic datum — can say what that means.

## A Worked Case

The formulas were checked on cases chosen here rather than on the step that motivated the paradox. Take $E=2mc^2$, and measure energies in units of $mc^2$ and wave numbers in units of $k_m=mc/\hbar$; every entry below is then a pure number, the two wave numbers of the case are $k_{t}^{\prime}=2k_m$ and $k_{x}=\sqrt3\,k_m$, and the step height is read as $k_V=V_0/(\hbar c)$ in the same unit. Then $\alpha = \sqrt{(k_{t}^{\prime}-k_m)/(k_{t}^{\prime}+k_m)} = \sqrt{1/3} = 0.577350$. Current conservation held to machine precision on every case below, and the limits were confirmed.

| $V_0/(mc^{2})$ | $\beta$ | $r$ | $R$ | $T$ |
|---|---|---|---|---|
| $5$ | $0.707107$ | $-0.420204$ | $0.176571$ | $0.823429$ |
| $10$ | $0.881917$ | $-0.325227$ | $0.105773$ | $0.894227$ |
| $100$ | $0.989847$ | $-0.272679$ | $0.074354$ | $0.925646$ |
| $\infty$ | $1$ | $-0.267949$ | $0.071797$ | $0.928203$ |

The reflection **decreases** as the step rises, from $0.177$ at $V_0 = 5mc^{2}$ to $0.072$ in the infinite-step limit, instead of approaching one. For $m = 0$ the same computation gives $\alpha = \beta = 1$, $r = 0$, $R = 0$, $T = 1$ exactly, independent of $V_0$: perfect transmission. Both statements are the standard ones, reproduced in the framework's notation.

## Open Questions

1. **The biquaternion form of the pair-creation source.** The resolution of the paradox is that the step creates pairs. The scalar analogue is treated in the companion article on scalar pair creation; the fermionic biquaternion treatment of a step as a pair source, with the anomalous occupation of the two mass-shell roots, is not yet written.

2. **The steepness.** Sauter showed that a step smoothed over a Compton wavelength removes the paradox. How does the smoothing enter the biquaternion equation — as a position-dependent central shift of the mass shell, or as a modification of the gradient itself?

3. **The sector of the transmitted component.** In the material-sector picture the current is $\mathbb{B}_{\Phi}$-valued. The transmitted "antiparticle" component of the far-side wave is a negative-frequency solution; is there a sector statement that distinguishes it from the incident component, or is the distinction purely one of the sign of $k_{t}^{\prime}$?

4. **The graphene transcription.** In graphene the Dirac points are massless and the potential step is a $p$–$n$ junction. The massless limit here is a clean $T = 1$; whether the biquaternion framework supplies anything beyond the massless Weyl equation for the two Dirac points is the question taken up in the companion article on Dirac matter.

5. **The strong-field scale.** The field required for the paradox with electrons is enormous, of order $10^{16}$ V/cm, and is realized only for very heavy nuclei or near horizons. Whether any of the framework's constants supplies a natural scale for the onset is open.

## Summary

The Klein step is the Dirac equation with a central potential $V(x) = V_0\mathrm{H}_{\mathrm{hvs}}(x)$, that is $-\varrho\xi(x)$, solved by matching two-component plane waves. The reflection coefficient is $R = ((\alpha\beta - 1)/(\alpha\beta + 1))^2$ and the transmission $T = 4\alpha\beta/(\alpha\beta + 1)^2$, with $\alpha = \sqrt{(E - mc^2)/(E + mc^2)}=\sqrt{(k_{t}^{\prime}-k_m)/(k_{t}^{\prime}+k_m)}$ and $\beta = \sqrt{(V_0 - E - mc^2)/(V_0 - E + mc^2)}=\sqrt{(k_V-k_m)/(k_V+k_m)}$, $k_V=V_0/(\hbar c)-k_{t}^{\prime}$; current conservation is an identity, checked on the cases tabulated. In the Klein region $V_0 - E > mc^2$ the transmitted wave is a negative-frequency state, and $R$ tends to the finite value $((\alpha - 1)/(\alpha + 1))^2$ as $V_0\to\infty$ rather than to one; in the massless limit $\alpha = \beta = 1$ and $T = 1$ for every step height.

The biquaternion framework locates the three ingredients: the potential is central and shifts the mass shell without acting on the module; the mass is the linear chirality-off-diagonal term; and the mass shell $\langle\tilde K_{\Phi}\rangle_{\natural} = -m^{2}c^{2}/\hbar^{2} = -k_m^{2}$ on the wave element $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar$, whose coefficients $k_{t}^{\prime}=\omega/c$ and $k_{\Phi}=p/\hbar$ are inverse lengths, has two roots, which the step exchanges. The exchange of roots is the algebraic face of the passage to the antiparticle branch, and it is produced by a central shift rather than by a conjugation of the field. The framework does not resolve the paradox, because the resolution is pair creation, a second-quantized statement; the one-particle coefficients are the standard ones. What the framework supplies is the clean separation of a central potential, a chiral mass and a two-rooted mass shell, which is exactly the structure the paradox tests.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $\tilde\nabla = e_t\partial/\partial R_t + \sum_{k=x,y,z}\vec e_k\,\partial/\partial R_k$ | Biquaternionic gradient |
| $D = \tilde\nabla +\frac{k_m\,i\,ϙ}{m\,c}\tilde{A}_{\Phi} = \tilde\nabla +\frac{V}{c\hbar}e_t$ | Covariant derivative (minimal coupling); $k_m/(mc)=1/\hbar$ and the temporal coefficient $a'_t=\xi/c$ |
| $\tilde{A}_{\Phi} = i\,a'_te_t$ | Electrostatic potential biquaternion |
| $V_0$, $V(x) = V_0\mathrm{H}_{\mathrm{hvs}}(x) = -\varrho\,\xi(x)$ | Step height and potential energy of the particle; $\xi$ the scalar potential |
| $E$, $k_{x}$, $k_{2x}$ | Energy; incident and transmitted wave numbers, the spatial components of $\vec k_{\Phi}$ on the two half-lines, both inverse lengths |
| $\alpha = \sqrt{(E - mc^2)/(E + mc^2)} = \sqrt{(k_{t}^{\prime}-k_m)/(k_{t}^{\prime}+k_m)}$ | Incident-side spinor parameter |
| $\beta = \sqrt{(V_0 - E - mc^2)/(V_0 - E + mc^2)} = \sqrt{(k_V-k_m)/(k_V+k_m)}$ | Far-side spinor parameter, $k_V=V_0/(\hbar c)-k_{t}^{\prime}$ |
| $r$, $t$, $R$, $T$ | Reflection and transmission amplitudes and probabilities |
| $\tilde K_{\Phi} = \tilde P_{\Phi}/\hbar = i k_{t}^{\prime}e_t+\vec e_x k_{\Phi}$ | Wave element of the plane wave; $k_{t}^{\prime} = \omega/c = E/(\hbar c)$ and $k_{\Phi} = p/\hbar$, both inverse lengths |
| $\langle\tilde Q\rangle_{\natural}$ | Quaternionic norm, the scalar of *Algebra and Element Conventions* |
| $\langle\tilde K_{\Phi}\rangle_{\natural} = -k_m^{2}$ | Mass shell, $k_m^{2} = k_{t}^{\prime\,2}-k_{\Phi}^{2}$; equivalently $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural} = -m^{2}c^{2}$ |
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
- The three wave numbers used above: [The Three Wavenumbers of a Particle](the-three-wavenumbers-of-a-particle.html), for $k_m$, $k_{t}^{\prime}$ and the inverse length that a potential adds to the temporal one.
- The companion articles of this series: [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), [One-Dimensional Scattering in Biquaternionic Form](one-dimensional-scattering-in-biquaternionic-form.html), and [The Dirac Sea, Hole Theory and Antimatter in Biquaternionic Form](the-dirac-sea-hole-theory-and-antimatter-in-biquaternionic-form.html).
