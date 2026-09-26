
# __Soliton Theory__

## Introduction

A soliton is a localised wave that travels without change of shape and re-emerges unchanged, apart from a phase shift, after colliding with another wave of the same kind. The defining phenomenon is the elastic collision: two such waves pass through one another as if they were independent particles, and the only trace of the interaction is a displacement of each wave from the position it would have occupied in isolation. The name records this particle-like behaviour, and the theory explains it through the inverse scattering transform of the preceding article, in which the solitons are the reflectionless part of the scattering data and the interaction is the nonlinear superposition performed by the inverse problem.

The subject has two layers. There is the theory of the **solitary wave**, a solution of an evolution equation that is a localised travelling wave of permanent form; such a wave exists in a wide class of equations and solves an ordinary differential equation obtained from the travelling-wave ansatz. There is then the theory of the **soliton**, a solitary wave with the additional property of surviving collisions; this is a property of integrable equations, and it is detected by the inverse scattering transform. The distinction matters: a solitary wave of a dissipative or non-integrable equation generally radiates on collision and loses energy, whereas the soliton of an integrable equation does not. The first explicit collision of two solitons was computed numerically by Zabusky and Kruskal, who also observed that the interaction of the waves was elastic, and it was this computation that led to the inverse scattering solution of the Korteweg–de Vries equation.

The article treats the definition of a solitary wave and of a soliton; the KdV soliton in the convention fixed by the preceding article, with its amplitude-speed relation, its $N$-soliton solutions and the phase shift of a collision; the soliton of the nonlinear Schrödinger equation, where it is an envelope rather than a pulse and where its dispersion relation is derived; the kink and the breather of the sine-Gordon equation, which show that a soliton can carry a topological charge and that two solitons can bind into a localised oscillation; the peakon of the Camassa–Holm equation, in which the profile has a corner; the asymptotic resolution of a general solution into solitons plus radiation; and the stability theory of solitary waves, which is what remains of the theory outside integrability. The inverse scattering transform itself is the subject of the preceding article and is used here rather than repeated.

## Solitary Waves and Solitons

**Definition.** Let $u_t = F(u)$ be an evolution equation on the line. A **solitary wave** is a solution of the form $u(x,t) = \phi(x-ct)$ with $\phi$ a nonzero function decaying at infinity and $c$ a constant velocity; the profile $\phi$ then solves the ordinary differential equation

$$
\phi'' = F_1(\phi,\phi') , \qquad F(\phi,-c\phi') = -c\phi' ,
$$

the second being the travelling-wave reduction of the equation. The solitary wave is a **soliton** if it survives collisions with other solitary waves of the same equation asymptotically unchanged in form and speed.

**Remark (why the distinction is real).** The travelling-wave reduction is an ordinary differential equation with a homoclinic orbit at the origin, and the existence of a solitary wave is a question about homoclinic bifurcation; the equation is not required to be integrable. The stability against collision, by contrast, is a rigid property. For a general equation a solitary wave interacting with another emits radiation, loses energy and is deformed; for an integrable equation the interaction is exactly elastic, because the inverse scattering transform writes the solution as a sum of asymptotically free pieces, and no energy can be transferred to the continuous spectrum in the reflectionless case.

**Example (the KdV solitary wave).** In the convention of the preceding article, $u_t - 6uu_x + u_{xxx}=0$, the travelling-wave ansatz $u = \phi(x-ct)$ gives $-c\phi' - 6\phi\phi' + \phi'''=0$, which integrates once to $\phi'' = c\phi + 3\phi^2 + A$. Taking $A=0$ and seeking a solution decaying at infinity, the equation $\frac12(\phi')^2 = \frac c2\phi^2+\phi^3$ has the homoclinic solution

$$
\phi(\xi) = -\frac{c}{2}\operatorname{sech}^2\left(\frac{\sqrt{c}}{2}\xi\right),
$$

which is the one-soliton of the preceding article with $c = 4\kappa^2$ and amplitude $-\frac{c}{2} = -2\kappa^2$. The amplitude is therefore proportional to the speed, $|{\phi}|_{\max} = c/2$, and this amplitude-speed relation is the signature of the KdV soliton: taller waves travel faster, so a fast soliton overtakes a slow one.

**Example (the nonlinear Schrödinger soliton).** For the focusing nonlinear Schrödinger equation

$$
i\psi_t + \psi_{xx} + 2|\psi|^2\psi = 0 ,
$$

already mentioned as an AKNS reduction, the soliton is an **envelope** rather than a pulse: with $A>0$ and $v$ real,

$$
\psi(x,t) = A\operatorname{sech}\bigl(A(x-vt-x_0)\bigr)\exp\left(i\Bigl(\frac{v}{2}x + \omega t\Bigr)\right), \qquad \omega = A^2 - \frac{v^2}{4} .
$$

Its modulus is a localised hump of amplitude $A$ moving with speed $v$, and its phase oscillates under the envelope; the relation between the amplitude and the frequency, $\omega = A^2-v^2/4$, is the nonlinear dispersion relation, and it is what distinguishes the soliton from a Gaussian wave packet, whose envelope spreads. The formula is verified by substitution into the equation, the second derivative of the sech profile cancelling the nonlinear term against the dispersion.

**Remark (bright and dark solitons).** For the defocusing equation $i\psi_t+\psi_{xx}-2|\psi|^2\psi=0$, whose nonlinearity is repulsive, there is no localised hump of small amplitude; the distinguished localised solutions are instead the **dark solitons**, which are depletions of a nonzero background $\psi_0$, $\psi = \psi_0\tanh(\cdot)e^{i\phi}$, moving at less than the background sound speed. The two cases illustrate that the existence of a bright soliton is a property of the focusing equation, and that the nonlinear Schrödinger equation is the model in which the focusing/defocusing dichotomy is cleanest.

## The KdV Soliton and Its Interaction

### The N-Soliton and the Phase Shift

**Theorem (asymptotic form of the N-soliton).** In the convention $u_t-6uu_x+u_{xxx}=0$, the reflectionless solution with $N$ bound states $\kappa_1>\kappa_2>\dots>\kappa_N>0$ has the asymptotic form

$$
u(x,t) \sim -\sum_{n=1}^N 2\kappa_n^2\operatorname{sech}^2\Bigl(\kappa_n\bigl(x-4\kappa_n^2t-\delta_n^\pm\bigr)\Bigr)
$$

as $t\to\pm\infty$, uniformly on compact sets after the waves have separated; the amplitude and the speed of each wave are the same in the two limits, and only the centres $\delta_n^\pm$ differ. The difference $\delta_n^+-\delta_n^-$ is the **phase shift** of the $n$-th soliton, and it is nonzero whenever more than one soliton is present.

*Proof.* Quoted as standard; the determinantal formula of the preceding article is expanded asymptotically in the two time limits, and the off-diagonal entries of the matrix, which express the interaction, become negligible in the two limits and contribute only to the constant in the exponent. $\square$

**Example (the two-soliton collision).** For $N=2$ and $\kappa_1>\kappa_2$, the faster taller soliton approaches from the left of the slower shorter one, the two overlap in a single hump of double height, and they separate with unchanged shapes and speeds; the taller acquires a positive phase shift and the shorter a negative one, both proportional to

$$
\log\frac{(\kappa_1+\kappa_2)^2}{(\kappa_1-\kappa_2)^2} .
$$

The shift diverges as $\kappa_1\to\kappa_2$, which is the resonance in which the two solitons do not separate, and it is finite otherwise. The exact computation of the phase shift is the content of the standard determinant asymptotics.

### Conservation Laws and Localised-Wave Dynamics

**Proposition (the integrals of the N-soliton).** The conserved quantities $I_k = \int\rho_k\,dx$ of the preceding article evaluate on the $N$-soliton as sums over the individual solitons:

$$
I_1 = -4\sum_n\kappa_n, \qquad I_2 = \frac{16}{3}\sum_n\kappa_n^3, \qquad I_3 = -\frac{32}{5}\sum_n\kappa_n^5 ,
$$

where $I_1=\int u\,dx$, $I_2=\int u^2dx$ and $I_3=\int(u^3+\frac12u_x^2)dx$; the general $I_k$ is a sum of the odd powers $\kappa_n^{2k-1}$. Each integral is evaluated on the one-soliton by elementary integration — for instance $\int u\,dx = -2\kappa^2\int\operatorname{sech}^2(\kappa x)dx = -4\kappa$ — and the additivity over separated solitons, together with the conservation of $I_k$, transports the value to the $N$-soliton. The conservation of each $I_k$ during a collision is therefore the statement that the amplitudes and speeds of the individual waves are unchanged, and the interaction can only redistribute the phases among them.

*Proof.* Quoted as standard; the integrals of powers of a reflectionless potential are computed from the scattering data by the trace identities, which express $I_k$ as a polynomial in the $\kappa_n$. $\square$

**Remark (the particle picture and its limits).** The trace identities make precise the heuristic that the solitons behave as $N$ independent particles whose conserved energies are functions of the $\kappa_n$: the collision of two such particles conserves each energy and changes only the positions. The picture fails for the radiation, which is carried by the continuous spectrum and is not described by finitely many particles; and it fails for a non-integrable perturbation of the equation, where the collision transfers energy to radiation and the amplitudes slowly change. Both limits are part of the theory of soliton stability treated below.

**Theorem (asymptotic resolution for KdV).** For every sufficiently smooth, rapidly decaying initial datum, the solution of KdV decomposes as $t\to\infty$ into a sum of $N$ solitons, corresponding to the negative eigenvalues of the associated Schrödinger operator, plus a decaying dispersive part; $N$ is the number of bound states of the initial datum.

*Proof.* Quoted as standard. The scattering data evolve by the linear law of the preceding article; the reflection coefficient contributes the dispersive part, whose decay is by the stationary phase method for the oscillatory integral defining it, and the bound states contribute the solitons. $\square$

## Kinks, Breathers and Other Solitons

**Definition.** A **kink** is a solitary wave whose limits at infinity are two distinct constants, $u(-\infty)=u_-$ and $u(+\infty)=u_+$, with $u_-\neq u_+$; the difference of the limits is its **topological charge**, and a kink cannot be deformed continuously into the vacuum. An **antikink** is a kink with the two limits interchanged, and a **breather** is a localised oscillating solution that is periodic in time and decaying in space.

**Example (the sine-Gordon kink).** For the sine-Gordon equation $u_{tt}-u_{xx}+\sin u=0$, the kink

$$
u(x,t) = 4\arctan\exp\left(\frac{x-vt}{\sqrt{1-v^2}}\right)
$$

is an exact solution for every $|v|<1$; its limits are $0$ and $2\pi$, so its degree is $1$ and its topological charge is $2\pi$, and its width contracts by the factor $\sqrt{1-v^2}$ as the parameter increases. The equation is invariant under the linear transformations $(t,x)\mapsto(\gamma(t-vx),\gamma(x-vt))$, $\gamma=(1-v^2)^{-1/2}$, which preserve the quadratic form $t^2-x^2$ — the pseudo-Euclidean isometries of the plane — and the kink family is the orbit of the stationary kink under them; the parameter is confined to $|v|<1$ by the definiteness of the form, and the limiting value is not attained.

*Proof.* Substitute the ansatz. With $\gamma = (1-v^2)^{-1/2}$ and $\xi=\gamma(x-vt)$ one has $u_{tt}-u_{xx}=(v^2-1)\gamma^2u''(\xi) = -u''(\xi)$, because $v^2-1 = -\gamma^{-2}$. For $u(\xi)=4\arctan e^\xi$ one computes $u'(\xi)=2\operatorname{sech}\xi$ and $u''(\xi) = -2\operatorname{sech}\xi\tanh\xi$; on the other hand $\sin(4\arctan e^\xi) = \frac{4e^\xi(1-e^{2\xi})}{(1+e^{2\xi})^2} = -2\operatorname{sech}\xi\tanh\xi$, so $u''=\sin u$. Hence $u_{tt}-u_{xx}+\sin u = -u''+\sin u = 0$. The computation is verified directly. $\square$

**Example (the sine-Gordon breather).** The exact solution

$$
u(x,t) = 4\arctan\left(\frac{\sqrt{1-\omega^2}\,\sin(\omega t)}{\omega\,\cosh\bigl(\sqrt{1-\omega^2}\,x\bigr)}\right), \qquad 0<\omega<1,
$$

is localised in $x$, periodic in $t$ with frequency $\omega$, and is a **breather**: it is the bound state of a kink and an antikink oscillating about one another. The breather shows that a soliton need not be a travelling wave of permanent form, and that the soliton spectrum of an integrable equation can contain oscillatory bound states as well as translations.

**Example (the Camassa–Holm peakon).** The Camassa–Holm equation

$$
u_t - u_{xxt} + 3uu_x = 2u_xu_{xx} + uu_{xxx}
$$

has the **peakon** solution $u(x,t) = c\,e^{-|x-ct|}$ for $c\neq0$: a travelling wave whose profile has a corner at its crest and which solves the equation in the weak sense. Peakons are the analogue of solitons for this equation, they interact elastically, and they show that the soliton mechanism does not require the solution to be smooth; the equation is integrable, with a Lax pair and an inverse scattering transform of its own.

**Example (line solitons and lumps).** In two spatial dimensions the Kadomtsev–Petviashvili equation, the two-dimensional integrable relative of KdV, has **line solitons** $u=\phi(x+ay-ct)$ that are independent of one direction, and the Davey–Stewartson equation has **lumps**, rational localised solutions decaying algebraically in all directions. The higher-dimensional theory shows that the elastic interaction is not peculiar to one dimension, but the stability properties of the higher-dimensional solitons differ, as the next section records.

## Stability of Solitons

**Definition.** Let $\phi_c$ be a solitary wave of an evolution equation, and let $\tau_r\phi_c$ denote its translate by $r$. The wave is **orbitally stable** if for every $\varepsilon>0$ there is $\delta>0$ such that an initial datum within distance $\delta$ of the orbit $\{\tau_r\phi_c : r\in\mathbb{R}\}$ in the relevant norm generates a solution that remains within distance $\varepsilon$ of that orbit for all time; it is **asymptotically stable** if, in addition, the solution converges to some member of the orbit as $t\to\infty$.

**Theorem (orbital stability of the NLS soliton).** For the focusing nonlinear Schrödinger equation with a power nonlinearity $i\psi_t+\psi_{xx}+|\psi|^{p-1}\psi=0$ in the $L^2$-subcritical range $1<p<5$, the ground-state solitary wave is orbitally stable in $H^1$; for the supercritical range it is unstable, and the instability is by blow-up or by dispersion.

*Proof.* Quoted as standard (Weinstein, Cazenave–Lions). The proof combines the variational characterisation of the solitary wave as the minimiser of the energy at fixed $L^2$ mass, the coercivity of the second variation on the orthogonal complement of the orbit, and a Gronwall argument that controls the growth of the deviation; the critical exponent is the one at which the second variation loses its coercivity. $\square$

**Theorem (stability of the KdV soliton).** In the convention $u_t-6uu_x+u_{xxx}=0$, the one-soliton is orbitally stable in $H^1$, and every solution with initial datum sufficiently close to a soliton converges asymptotically to a soliton plus radiation (Martel–Merle).

*Proof.* Quoted as standard. The orbital stability is variational, as for NLS; the asymptotic statement is proved by the method of the nonlinear steepest descent applied to the inverse scattering transform, which linearises the perturbation problem and controls the radiation by the decay of an oscillatory integral. $\square$

**Remark (transverse instability and multidimensional solitons).** A line soliton of the Kadomtsev–Petviashvili equation of the "wrong" signature is transversely unstable: a perturbation periodic in the direction along the line grows, so the one-dimensional soliton is destroyed by a two-dimensional disturbance. The lump solutions of Davey–Stewartson are, by contrast, stable in a suitable sense. The comparison shows that the stability of a soliton is not a consequence of the elastic interaction alone but depends on the dimension and on the sign of the dispersion, and it is one of the places where the one-dimensional integrable theory does not extend without change.

## Solitons and Integrable Systems

**Remark (the soliton as a nonlinear normal mode).** The inverse scattering transform explains the soliton as the nonlinear analogue of a normal mode. For a linear dispersive equation, a wave packet of a single wavenumber travels at the group velocity and spreads; for an integrable equation, the bound states of the associated linear operator provide finitely many nonlinear modes that travel without spreading, while the continuous spectrum provides the dispersive radiation. The solitons are the discrete spectrum, and the resolution theorem is the statement that the nonlinear dynamics is diagonal in the scattering variables.

**Remark (the boundaries of the theory).** The theory of this article is the theory of solitons of integrable equations. The broader theory of solitary waves of non-integrable equations — their existence by dynamical systems methods, their stability by variational and spectral methods, and their role as coherent structures in a general evolution — is a subject of the analysis of partial differential equations; the finite-dimensional dynamics of the corresponding travelling-wave ordinary differential equations, and the stability of their homoclinic orbits, belong with the dynamical systems of this Part. What is peculiar to the integrable case, and what this article and its predecessor record, is the exact solvability: the reduction of the nonlinear flow to a linear one, the elastic interaction, and the explicit formulas for the solitons and their phase shifts.

## Summary

A solitary wave of an evolution equation is a localised travelling wave $u=\phi(x-ct)$ whose profile solves the travelling-wave reduction, and it is a soliton if it also survives collisions unchanged apart from a phase shift. For KdV in the convention $u_t-6uu_x+u_{xxx}=0$, the solitary wave is $\phi=-\frac c2\operatorname{sech}^2(\frac{\sqrt c}{2}\xi)$ with amplitude $c/2$ proportional to the speed, so taller solitons move faster; the reflectionless $N$-soliton is asymptotically $N$ separated one-solitons at both time infinities, and the elastic collision shifts each centre by a finite phase shift, proportional for two solitons to $\log\frac{(\kappa_1+\kappa_2)^2}{(\kappa_1-\kappa_2)^2}$, which diverges at the resonance $\kappa_1\to\kappa_2$. The conserved quantities of KdV evaluate on the $N$-soliton as sums of powers of the $\kappa_n$, which is the precise form of the particle picture, and every sufficiently smooth initial datum resolves asymptotically into finitely many solitons plus dispersive radiation. For the focusing nonlinear Schrödinger equation $i\psi_t+\psi_{xx}+2|\psi|^2\psi=0$ the soliton is an envelope $A\operatorname{sech}(A(x-vt))e^{i(vx/2+\omega t)}$ with $\omega=A^2-\frac{v^2}{4}$, and the defocusing equation possesses dark solitons instead. The sine-Gordon equation has the topological kink $4\arctan e^{\gamma(x-vt)}$, with $\gamma=(1-v^2)^{-1/2}$, and the breather, a kink–antikink bound state oscillating in time; the Camassa–Holm equation has the cornered peakon. Solitary waves that are not integrable solitons may still be orbitally stable, as the NLS and KdV stability theorems show, but their collisions radiate, and the multidimensional case introduces transverse instabilities that have no one-dimensional analogue.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $u(x,t)$, $\phi$ | Field and solitary-wave profile |
| $c$, $v$ | Speed of a solitary wave |
| KdV | $u_t - 6uu_x + u_{xxx} = 0$ |
| $\kappa_n$ | Bound-state wavenumbers of the $N$-soliton |
| $I_k$ | Conserved quantities, evaluated on the reflectionless data |
| $\delta_n^\pm$ | Asymptotic centres of the $n$-th soliton; phase shift $\delta_n^+-\delta_n^-$ |
| NLS | $i\psi_t+\psi_{xx}+2|\psi|^2\psi=0$ (focusing) |
| $A$, $\omega$ | Soliton amplitude and frequency, $\omega=A^2-v^2/4$ |
| sine-Gordon | $u_{tt}-u_{xx}+\sin u=0$ |
| $\gamma$ | Factor $(1-v^2)^{-1/2}$ in the pseudo-Euclidean symmetry of the kink |
| $2\pi$ | Topological charge of the sine-Gordon kink |
| peakon | $u=c\,e^{-|x-ct|}$, the cornered Camassa–Holm soliton |
| orbital stability | Stability of the orbit $\{\tau_r\phi_c\}$ under the flow |

## Further Reading

- John Scott Russell, "Report on Waves", *Report of the Fourteenth Meeting of the British Association for the Advancement of Science* (1844), for the original observation of the solitary wave.
- Norman J. Zabusky and Martin D. Kruskal, "Interaction of 'Solitons' in a Collisionless Plasma and the Recurrence of Initial States", *Physical Review Letters* 15 (1965), for the numerical discovery of the elastic soliton collision.
- Philip G. Drazin and Robin S. Johnson, *Solitons: An Introduction* (Cambridge University Press, 1989), for the KdV and NLS solitons and their interactions.
- Mark J. Ablowitz and Harvey Segur, *Solitons and the Inverse Scattering Transform* (SIAM, 1981), for the inverse scattering theory behind the soliton formulas.
- Vladimir E. Zakharov and Alexei B. Shabat, "Exact Theory of Two-Dimensional Self-Focusing and One-Dimensional Self-Modulation of Waves in Nonlinear Media", *Soviet Physics JETP* 34 (1972), for the NLS soliton and the Zakharov–Shabat scattering problem.
- Michael J. Ablowitz, David J. Kaup, Alan C. Newell and Harvey Segur, "The Inverse Scattering Transform — Fourier Analysis for Nonlinear Problems", *Studies in Applied Mathematics* 53 (1974), for the general scheme and the sine-Gordon solitons.
- Roberto Camassa and Darryl D. Holm, "An Integrable Shallow Water Equation with Peaked Solitons", *Physical Review Letters* 71 (1993), for the peakon.
- Michael I. Weinstein, "Modulational Stability of Ground States of Nonlinear Schrödinger Equations", *SIAM Journal on Mathematical Analysis* 16 (1985), for the orbital stability criterion.
- Yvan Martel and Frank Merle, "Asymptotic Stability of Solitons for Subcritical Generalized KdV Equations", *Archive for Rational Mechanics and Analysis* 157 (2001), for the asymptotic stability of the KdV soliton.
- Yuri S. Kivshar and Barry A. Malomed, "Dynamics of Solitons in Nearly Integrable Systems", *Reviews of Modern Physics* 61 (1989), for the perturbation theory of solitons.
