# __Relativistic Mechanics from the Dirac Wave: The Non-Quantum Limit in Biquaternionic Form__

## Introduction

The biquaternionic Dirac equation is first order and its solutions are waves. At short wavelength a wave stops being one in the sense that matters, and what remains is a particle with a momentum and a mass. This article carries that out: the relativistic Hamilton–Jacobi equation at leading order, the Lorentz force one step later.

The claim, stated narrowly. The mass shell is the leading term of a short-wavelength expansion of the Dirac wave. It is not predicted by the algebra nor created by the limit: $\nu_m=\frac{m\,c}{h}$ is already there. What the limit supplies is the reading of the phase gradient as the mechanical momentum, and with it the flow.

The parameter is the companion's. With $\tilde\Xi=A\exp\!\left(i\theta_{\mathrm{phs}}\right)\xi$, the spinor phase $\theta_{\mathrm{phs}}=\frac{2\pi S_{\tilde\Xi}}{h}$ real because the action of the field is real, the small quantity is $\epsilon=1/(2\pi\nu_{\Phi}L)=\frac{h}{2\pi pL}$, $L$ the length over which $A$ varies. The criterion and the error operator are established in *The Non-Quantum Limit of the Biquaternion Model* and are used here, not restated.

What this is not. It is not the $\beta\ll1$ limit of *The Dirac Equation in Biquaternionic Form: Solutions and the Non-Relativistic Limit*, which subtracts the rest phase and yields a non-relativistic wave; this yields a relativistic flow. The two compose, as §*Where the Two Limits Meet* says.

What is not new. The chiral pair is *The Dirac Equation in Biquaternionic Form*; the criterion, the companion *The Non-Quantum Limit of the Biquaternion Model*. Added here: the eikonal of the coupled pair, its gradient as the Lorentz force, and the observation that the leading eikonal is central and so cannot see a spinor.

## The Wave and the Expansion

Conventions. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$. The field is an element, the operator is an element multiplying on the left, and the dynamics is the pair

$$
\tilde\nabla_\Phi\tilde\Xi_{R}=2\pi\nu_m\tilde\Xi_{L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L}=2\pi\nu_m\tilde\Xi_{R},
\qquad
\nu_m=\frac{m\,c}{h}.
$$

The product $(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi$ is the central scalar $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_{t}}^{2}$, which with $r'_{t}=ct$ is $-\frac{1}{c^{2}}\partial_{t}^{2}+\vec\nabla_\Phi^{2}$, so each half obeys $\left(\Box_\Phi-4\pi^{2}\nu_m^{2}\right)\tilde\Xi=0$. The passage from the first-order pair to that second-order equation is the subject of *Klein–Gordon from the Dirac Square*; what matters here is that the operator is scalar, so the expansion never has to choose a chiral half.

The expansion. Write $\tilde\Xi=Ae^{i\theta_{\mathrm{phs}}}\xi$ with $A>0$ real, $S_{\tilde\Xi}$ real and $\xi$ slowly varying. The action carries the subscript of the field it belongs to because this article also carries the spin $\tilde S_{\Psi,k}$, and the bare letter would be read for either. Then

Throughout, $\theta_{\mathrm{phs}}:=\frac{2\pi S_{\tilde\Xi}}{h}$ is the spinor phase, a real angle: the polar form separates the amplitude $\lVert\tilde\Xi\rVert$ from the phase, so $S_{\tilde\Xi}$ is real and $\exp(i\theta_{\mathrm{phs}})$ has modulus one.

$$
\tilde\nabla_\Phi\tilde\Xi=\frac{2\pi}{h}\left(\frac{\partial_{t}S_{\tilde\Xi}}{c}e_{t}+i\nabla S_{\tilde\Xi}\right)\tilde\Xi+\mathcal{O}(\epsilon),
$$

so the gradient acts, to leading order, as multiplication by $2\pi i\tilde\Upsilon_{\Phi}$, with $\tilde\Upsilon_{\Phi}=\frac{\tilde P_{\Phi}}{h}$ the element of *The Three Wavenumbers of a Particle*. Its $e_{t}$ entry is real and its vector part imaginary, as the display shows. The limit is the statement that this term dominates.

What a $k$ may stand for, and nothing else. Three wave numbers occur in this article, and each divides $\frac{h}{2\pi}$ out of a mass, a momentum or an energy: $\nu_m=\frac{m\,c}{h}$, $\vec\nu_{\Phi}=\frac{\vec p}{h}$, and the temporal one $\frac{\omega}{c}=\frac{2\pi E}{h\,c}$, which occurs once, in §*Case Checked*. No fourth use is made of one. The rewriting $\frac{2\pi}{h}=2\pi\nu_m/(m\,c)$ is available, and the companion uses it for the phase; it is not used here, because the mass cancels in that ratio for every $m$, so nothing is absorbed into the $\nu_m$ and the wave number would be decoration over a bare $\frac{h}{2\pi}$. A wave number appears below only where a mass, a momentum or an energy waits to be absorbed by it. The one place where the source's writing is quoted is the charge coupling, and §*The Gauge Field, and the Lorentz Force* says what the cancellation carries there.

## Order Zero: the Mass Shell

Substitute and separate. Multiplying $\left(\Box_\Phi-4\pi^{2}\nu_m^{2}\right)\tilde\Xi=0$ by $-\frac{h^{2}}{4\pi^{2}}$ and dividing by $\tilde\Xi$ gives, exactly,

$$
-\left[\frac{(\partial_{t}S_{\tilde\Xi})^{2}}{c^{2}}-\lvert\nabla S_{\tilde\Xi}\rvert^{2}-m^{2}c^{2}\right]
+\frac{h^{2}}{4\pi^{2}}\left[\frac{1}{c^{2}}\frac{\partial_{t}^{2}A}{A}-\frac{\vec\nabla_\Phi^{2}A}{A}\right]
+\frac{i h}{2\pi A^{2}}\left[\frac{1}{c^{2}}\partial_{t}\!\left(A^{2}\partial_{t}S_{\tilde\Xi}\right)-\vec\nabla_\Phi\cdot\left(A^{2}\vec\nabla_\Phi S_{\tilde\Xi}\right)\right]=0 .
$$

No line is dropped and no order taken: one identity in the two real functions $A$ and $S_{\tilde\Xi}$.

Three lines, three orders. The first is a difference of energies, of scale $p^{2}$, with no $\frac{h}{2\pi}$ in it. The second, over the first, is $\frac{h^{2}}{(2\pi)^{2} p^{2}L^{2}}=\epsilon^{2}$; its bracket is the companion's quantum potential. The third, over the first, is $\frac{h}{2\pi pL}=\epsilon$. The identity reads $1:\epsilon^{2}:\epsilon$, and $\frac{h}{2\pi}$ is never set to zero.

Order zero. Dropping the $\epsilon^{2}$ line leaves the first line zero, which with $E=-\partial_{t}S_{\tilde\Xi}$ and $\vec p=\vec\nabla_\Phi S_{\tilde\Xi}$ reads

$$
\boxed{\;\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}=m^{2}c^{2}\;}
$$

which is the mass shell and the relativistic Hamilton–Jacobi equation: the phase is a complete integral and its gradient the four-momentum. **The limit discards the quantum potential; the $\epsilon$ line is not an error but the next order's equation**, as §*Order One* shows. The relative error is $\epsilon^{2}$.

The mass is recovered, not derived. The first line carries $m$ because $\nu_m$ did; the expansion adds only $E=-\partial_{t}S_{\tilde\Xi}$, $\vec p=\vec\nabla_\Phi S_{\tilde\Xi}$.

## The Gauge Field, and the Lorentz Force

Minimal coupling replaces the gradient. The corpus's prescription of *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* is $\tilde\nabla_\Phi\mapsto\tilde\nabla_{\mathrm{gco},\Phi}$ with

$$
\tilde\nabla_{\mathrm{gco},\Phi,\imath}=\frac{\partial}{\partial R_{\imath}}+\frac{2\pi i\,ϙ}{h}A_{\imath},
$$

$ϙ$ the charge and $\tilde A_{\Phi}=\sum_{\imath}A_{\imath}e_{\imath}$ the potential, whose temporal entry is $A_{t}=i\phi/c$. The source article writes the same coefficient as $\frac{2\pi i\,ϙ}{h}$, and the two agree, both being one over an action. The mass cancels in that ratio, and that cancellation is the physical content: the coefficient is $\frac{2\pi}{h}$ and not a function of $m$, because the charge couples the same way whatever the mass. Written with $\nu_m$ beside the $m$ it was made from, the coefficient would read as one that grows with the mass, whereas it is the same number for the electron and for the proton. The cancellation is what makes that visible, and it is the reason $\frac{h}{2\pi}$ is the form written here. Acting on $A\exp(i\theta_{\mathrm{phs}})$ the entries become $\frac{2\pi}{h c}(\partial_{t}S_{\tilde\Xi}-ϙ\phi)$ and $\frac{2\pi i}{h}(\vec\nabla_\Phi S_{\tilde\Xi}-q\vec A)$, the two shifts being opposite, which is the gauge-invariant content.

One relabelling, stated once. Those entries carry the coupling, whose sign is opposite the electric charge, so that as they stand they are not the kinetic momentum of ordinary notation, $\vec\pi=\vec p-q\vec A$. Writing $-ϙ$ for the coupling throughout, which makes $ϙ$ the charge $q$, sends them to $\frac{2\pi}{h c}(\partial_{t}S_{\tilde\Xi}+ϙ\phi)$ and $\frac{2\pi i}{h}(\vec\nabla_\Phi S_{\tilde\Xi}-ϙ\vec A)$, and the article uses that writing, in which $\Pi_{t}$ and $\vec\pi$ carry their usual signs.

The norm is the coupled eikonal. The norm is the sum of the squares of the entries, so at order zero

$$
\boxed{\;\frac{1}{c^{2}}\left(\partial_{t}S_{\tilde\Xi}+ϙ\phi\right)^{2}-\left\lvert\nabla S_{\tilde\Xi}-ϙ\vec A\right\rvert^{2}=m^{2}c^{2}\;}
$$

**The relative sign is not a choice.** Under $S_{\tilde\Xi}\mapsto S_{\tilde\Xi}-ϙ\chi$, $\phi\mapsto\phi+\partial_{t}\chi$, $\vec A\mapsto\vec A-\vec\nabla_\Phi\chi$ only this pairing is invariant under one gauge function; the alternative fails by $-2ϙ\vec\nabla_\Phi\chi$. Gauge invariance fixes that the shifts enter with opposite signs.

Two combinations, and they are the mechanical ones. In that writing $\Pi_{t}=\partial_{t}S_{\tilde\Xi}+ϙ\phi$ and $\vec\pi=\vec\nabla_\Phi S_{\tilde\Xi}-ϙ\vec A$, so $\mathcal{E}=-\Pi_{t}=E-ϙ\phi$ is the kinetic energy and the eikonal says $\frac{1}{c^{2}}\mathcal{E}^{2}-\lvert\vec\pi\rvert^{2}=m^{2}c^{2}$. The flow is therefore

$$
\vec v=\frac{c^{2}\vec\pi}{\mathcal{E}},
$$

which is $\vec\pi=\gamma m\vec v$ and $\mathcal{E}=\gamma mc^{2}$ read backwards, and not $\vec\pi/m$ — the whole distance between this article and the Newtonian end.

The gradient is the Lorentz force. Differentiate the coupled eikonal with respect to $x^{i}$ and use $\partial_{i}\partial_{t}S_{\tilde\Xi}=\partial_{t}\partial_{i}S_{\tilde\Xi}$:

$$
\frac{\Pi_{t}}{c^{2}}\left(\partial_{t}\partial_{i}S_{\tilde\Xi}+ϙ\partial_{i}\phi\right)
=\pi_{j}\left(\partial_{i}\partial_{j}S_{\tilde\Xi}-ϙ\partial_{i}A_{j}\right).
$$

Solving for $\partial_{t}\partial_{i}S_{\tilde\Xi}$ and substituting $\vec v=-c^{2}\vec\pi/\Pi_{t}$, the two second-derivative terms cancel because partial derivatives commute, and what survives is

$$
\frac{d\pi_{i}}{dt}=ϙ\left(-\partial_{i}\phi-\partial_{t}A_{i}\right)+ϙ\,v_{j}\left(\partial_{i}A_{j}-\partial_{j}A_{i}\right),
$$

that is

$$
\boxed{\;\frac{d\vec\pi}{dt}=ϙ\left(\vec E+\vec v\times\vec B\right),
\qquad
\vec E=-\vec\nabla_\Phi\phi-\partial_{t}\vec A,
\qquad
\vec B=\vec\nabla_\Phi\times\vec A\;}
$$

with $d/dt=\partial_{t}+\vec v\cdot\nabla$ along the flow. The identity $(\vec v\times\vec B)_{i}=\epsilon_{\imath\jmath\ell}v_{j}B_{\imath}=v_{j}\partial_{i}A_{j}-v_{j}\partial_{j}A_{i}$ turns the last term into the cross product. The magnetic part is the curl of the potential, and both parts come out of a gradient of a scalar equation.

What this is, precisely. Minimal coupling supplies the charge and the potentials; the limit supplies the force. Nothing else enters, not the spin and not $m$ beyond the flow.

## Order One: the Transport Equation, and the Spin

The $\epsilon$ line is the current. Vanishing of the third line of the identity above is

$$
\frac{1}{c^{2}}\partial_{t}\!\left(A^{2}\partial_{t}S_{\tilde\Xi}\right)-\vec\nabla_\Phi\cdot\left(A^{2}\vec\nabla_\Phi S_{\tilde\Xi}\right)=0,
$$

which is $\sum_{\imath}\partial_{\imath}(A^{2}\partial_{\imath} S_{\tilde\Xi})=0$, the relativistic continuity equation, with $j_{\imath}=A^{2}\partial_{\imath} S_{\tilde\Xi}$. Nothing here was approximated, so the limit delivers a flow and its density, not a trajectory.

Why the spin cannot appear at order zero. The leading multiplier is a single biquaternion and the eikonal is its norm, $\langle\tilde\Upsilon_{\Phi}\rangle_{\natural}$. A norm is central, so it commutes with $\xi$ and cannot act on it. **The spin is an order-one effect by construction, not by neglect.**

Where the spin sits, in the corpus's own terms. *From the Spin to the Carriers and the Closures* defines $\tilde S_{\Psi,k}=\frac{h}{4\pi}i\vec e_{\imath}$, Hermitian in $\mathbb{B}_{\Psi}$, with $\mathsf{M}_2(\tilde S_{\Psi,k})=\frac{h}{4\pi}\sigma_{\imath}$. Three consequences follow, and all three hold here. $\frac{h}{2\pi}$ is not sent to zero in this limit, only $\epsilon$, so $\frac{h}{4\pi}$ survives and the passage removes no spin. The leading eikonal being central, it commutes with every $\tilde S_{\Psi,k}$, which is why the force above carried none. And at order one the operator is the failure of the two orderings to commute, whose tangent form is the field strength contracted with $\sigma_{\imath\jmath}$; its space–space part is $\sum_{\imath\in\{x,y,z\}}\tilde S_{\Psi,k}B_{\imath}$, so the expected term is $-\frac{ϙ}{m}\sum_{\imath\in\{x,y,z\}}\tilde S_{\Psi,k}B_{\imath}$, which is $g=2$ as *The Classical Origin of $g=2$ in Biquaternionic Form* has it. This article locates that term rather than deriving it; *The Classical Spinning Particle* names it as open question four, and its $d\tilde P_{\Phi}/d\tau=ϙ\,\mathrm{F}(\tilde V_{\Phi})$ of *The Lorentz Force in Biquaternion Form* is the covariant form of the result above.

## Where the Two Limits Meet

The two limits compose. This one takes the relativistic wave to the relativistic flow; the companion's $\beta$ limit then subtracts the rest phase $e^{-ik_{m}ct}$, after which $\mathcal{E}\to mc^{2}$ and $\vec\pi\to m\vec v$. Composing them in that order gives $\vec v=\vec\pi/m$ and, from the same gradient,

$$
m\frac{d\vec v}{dt}=ϙ\left(\vec E+\vec v\times\vec B\right).
$$

The other order is the companion's. Subtracting the rest phase first gives the non-relativistic wave, whose eikonal is the non-relativistic Hamilton–Jacobi equation. They share no parameter: $\beta$ and $\epsilon$ are independent, four orders of magnitude apart at $\beta=0.01$.

## Case Checked

The electron at $\beta=0.01$. $2\pi\nu_m=2.589605\times10^{12}\ \mathrm{m^{-1}}$, $\frac{1}{2\pi\nu_m}=3.86159\times10^{-13}\ \mathrm{m}$ (the wavelength is $\lambda_m=2.426\times10^{-12}\ \mathrm{m}$), $mc^{2}=8.1871\times10^{-14}\ \mathrm{J}$, and $\gamma=1.0000500$, $\gamma-1=5.0004\times10^{-5}$.

| quantity | relativistic | Newtonian | ratio, Newtonian to relativistic |
|---|---|---|---|
| the velocity from the flow | $\vec p\,c^{2}/E$ | $\vec p/m$ | $\gamma=1.00005$ |
| the kinetic energy | $E-mc^{2}$ | $\lvert\vec p\rvert^{2}/2m$ | $\frac{\gamma+1}{2}=1.000025$ |

The first row is exact at every $\beta$, since $\vec p\,c^{2}/E=\gamma m\vec v\,c^{2}/(\gamma mc^{2})=\vec v$. The second is exact as a ratio, $\frac{\lvert\vec p\rvert^{2}/2m}{E-mc^{2}}=\frac{\gamma+1}{2}$, and the Newtonian value is high by $\frac{\gamma-1}{2}=2.5\times10^{-5}$.

The checks. The identity of §*Order Zero* was tested at five hundred values of $(x,t)$: its real line to $4.3\times10^{-14}$, its imaginary line to $3.6\times10^{-15}$, the latter equal to the continuity equation to $2.7\times10^{-15}$. The Lorentz force was derived symbolically for arbitrary $S_{\tilde\Xi}$, $\phi$, $\vec A$, with zero residual.

A plane wave is already there. For $\tilde\Xi=\xi e^{-i\theta_{\mathrm{pwp}}}$ the amplitude is constant and $\epsilon=0$, so the eikonal is the dispersion relation $\frac{\omega^{2}}{c^{2}}-\lvert2\pi\vec\nu_\Phi\rvert^{2}=4\pi^{2}\nu_m^{2}$ exactly. At the other end a caustic makes $A$ diverge, $\epsilon$ large, the expansion void.

The angle is $\theta_{\mathrm{pwp}}=\frac{p\cdot x}{h}=\omega r'_t-2\pi\vec\nu_\Phi\cdot\vec r$: a real four-momentum paired with a real position over $\frac{h}{2\pi}$, so the angle is real.

## Summary

The short-wavelength limit of the biquaternionic Dirac wave is relativistic mechanics. At order zero the phase satisfies $\frac{1}{c^{2}}(\partial_{t}S_{\tilde\Xi})^{2}-\lvert\nabla S_{\tilde\Xi}\rvert^{2}=m^{2}c^{2}$, which is the mass shell with $E=-\partial_{t}S_{\tilde\Xi}$ and $\vec p=\vec\nabla_\Phi S_{\tilde\Xi}$. With the connection present the same step gives $\frac{1}{c^{2}}(\partial_{t}S_{\tilde\Xi}+ϙ\phi)^{2}-\lvert\nabla S_{\tilde\Xi}-ϙ\vec A\rvert^{2}=m^{2}c^{2}$, whose flow is $\vec v=c^{2}\vec\pi/\mathcal{E}$ and whose gradient is $\frac{d\vec\pi}{dt}=ϙ(\vec E+\vec v\times\vec B)$.

The mass is recovered rather than derived: $\nu_m$ carried it. The spin is absent at order zero for a structural reason, the leading eikonal being a norm, and a norm is central and cannot act on a spinor; it belongs to order one, where the two orderings of the coupled gradient stop commuting, which is where the corpus's open problem about Bargmann–Michel–Telegdi points.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=A\exp\!\left(i\theta_{\mathrm{phs}}\right)\xi$ | The wave in amplitude and phase; $A>0$ real, $S_{\tilde\Xi}$ the action of the field, $\xi$ slowly varying; the companion writes the exponent $\frac{\nu_miS_{\tilde\Xi}}{m\,c}$, which is the same number |
| $\epsilon=\frac{1}{2\pi\nu_{\Phi}L}=\frac{h}{2\pi pL}$ | The parameter of the limit; $L$ the length over which $A$ varies |
| $\nu_m=\frac{m\,c}{h}$ | The mass wave number; the reciprocal of the Compton wavelength |
| $E=-\partial_{t}S_{\tilde\Xi}$, $\vec p=\vec\nabla_\Phi S_{\tilde\Xi}$ | Energy and momentum read off the phase |
| $\Pi_{t}=\partial_{t}S_{\tilde\Xi}+ϙ\phi$, $\vec\pi=\vec\nabla_\Phi S_{\tilde\Xi}-ϙ\vec A$ | The canonical and the kinetic momentum, minimally coupled |
| $\mathcal{E}=-\Pi_{t}=E-ϙ\phi$ | The kinetic energy; $\vec v=c^{2}\vec\pi/\mathcal{E}$ |
| $\tilde\nabla_{\mathrm{gco},\Phi,\imath}=\frac{\partial}{\partial R_{\imath}}+\frac{2\pi i\,ϙ}{h}A_{\imath}$ | The covariant derivative carrying the connection |
| $ϙ$ | The charge of the field the operator acts on |

## Further Reading

- Michael V. Berry and K. E. Mount, "Semiclassical approximations in wave mechanics," *Reports on Progress in Physics* 35 (1972) 315–397, for the eikonal method and its failure at caustics.
- Robert G. Littlejohn, "The semiclassical evolution of wave packets," *Physics Reports* 138 (1986) 193–291, for the transport equation and the spin connection at subleading order.
- Michel H. L. Pryce, "The mass-centre in the restricted theory of relativity and its connexion with the quantum theory of elementary particles," *Proceedings of the Royal Society A* 195 (1948) 62–81, for the classical limit of the Dirac equation and the origin of the spin supplementary condition.
