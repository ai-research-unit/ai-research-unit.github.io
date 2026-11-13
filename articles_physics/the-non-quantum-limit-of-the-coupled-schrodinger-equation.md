# __The Non-Quantum Limit of the Coupled Schrödinger Equation__

## Introduction

**What changes when a connection is present.** Three things and no more. The phase gradient becomes the kinetic momentum, the potential energy enters the phase equation, and the transport equation carries the kinetic velocity. The quantum potential is untouched, the amplitude stays real and central, and the algebra of the limit does not grow a single new object.

**Why so little changes.** The connection is a central-imaginary number in every slot, so in the polar chart it joins the phase bracket and nothing else. *The Coupled Schrödinger Equation in Biquaternionic Polar Variables* proves this from the four-bracket split of the logarithmic derivative: the scale bracket receives nothing, the boost bracket receives nothing, the rotor bracket receives nothing. The limit is built from the scale and the phase gradient, so it receives the connection in exactly one place.

**The parameter.** $\epsilon=1/(k_{\Phi}L)$, with $k_{\Phi}$ the wave number of the phase and $L$ the length over which the amplitude varies. The connection does not enter the criterion: a magnetic field bends the rays and does not change the length over which an amplitude varies, and an electric potential shifts the phase's rate uniformly and does not touch the scale.

**What the article establishes, in four sentences.** The coupled pair is exact. The eikonal is the free eikonal with the kinetic momentum, and its characters are the trajectories of a charge. The transport equation is exact and its current is the kinetic one. The circulation quantum $2\pi\hbar n+ϙ\Phi_B$ is exact and survives the limit unchanged, because it is a statement about a loop and not about a length.

**What is not new.** The covariant Madelung pair is standard quantum hydrodynamics, and the Lorentz force from the eikonal is the standard optical–mechanical derivation. Added here: the ordering by $\epsilon$ with the connection in place, the proof that the connection cannot enter the quantum potential, the location of the gauge direction in the limit, and the statement that the circulation is an exact invariant of the pair rather than a result of the limit.

**Conventions.** Those of the polar companion, unchanged. Time is $t'$; the connection is $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$ with $\varphi=c\,a'_t$; $ϙ$ is minus the electric charge, so the mechanical momentum is $\vec\pi=-i\hbar\nabla+ϙ\vec A$ and the potential energy is $-ϙ\varphi$; the density is $n=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)=r^{2}\cosh\theta_{\mathrm{rpd}}$, which for the central field is $r^{2}$. The mass wave number is $k_m=mc/\hbar$.

## The State and the Connection

**The word.** For the central field the state collapses to three parameters,

$$
\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\,\epsilon_{\pm}\,e_t ,
\qquad
r>0,
\qquad
S=\hbar\,\theta_{\mathrm{pha}},
$$

with $\epsilon_\pm=\pm1$ the branch. The boost is trivial and the rotor is trivial, so the word is a scale, a phase and a sign, and the two invariants of the coupled theory are

$$
\vec\pi=\nabla S+ϙ\vec A ,
\qquad
\mathcal E=-\partial_{t'}S+ϙ\varphi .
$$

**Both are gauge invariant and neither is separately natural.** Under $\theta_{\mathrm{pha}}\mapsto\theta_{\mathrm{pha}}+ϙ\Gamma/\hbar$ and $\vec A\mapsto\vec A-\nabla\Gamma$, the phase gradient shifts by $-\frac{ϙ}{\hbar}\nabla\Gamma$ and the two halves cancel. The phase rate alone is not invariant, and the article records that because the limit is written on the phase: an expansion that keeps only $\partial_{t'}\theta_{\mathrm{pha}}$ keeps a gauge artefact.

**The limit is therefore written on the invariants.** $\vec\pi$ in place of $\nabla S$, and $\mathcal E$ in place of $-\partial_{t'}S$. This is not a cosmetic choice. A truncated equation in $\partial_{t'}\theta_{\mathrm{pha}}$ alone would change its value under a gauge transformation that the untruncated equation ignores, so the truncated equation would not be gauge invariant even where the original is.

**The two momenta.** $\vec p=\nabla S$ is canonical and $\vec\pi=\vec p+ϙ\vec A$ is kinetic. The polar chart's flow statement is that the constant connection shifts the two coefficients of the element: $h_t\mapsto h_t-ϙ\varphi$ and $\vec h_\Psi\mapsto\vec h_\Psi+ϙ\vec A$. The second is the kinetic momentum and the first is the kinetic energy, so the two settings name the same pair.

## The Two Real Equations

**The covariant pair, exact.** Varying the phase and varying the scale of the coupled equation gives

$$
\partial_{t'}\left(r^{2}\right)+\nabla\cdot\left(r^{2}\,\frac{\nabla S+ϙ\vec A}{m}\right)=0 ,
$$

$$
\partial_{t'}S+\frac{\lvert\nabla S+ϙ\vec A\rvert^{2}}{2m}-ϙ\varphi+Q=0 ,
\qquad
Q=-\frac{\hbar^{2}}{2m}\,\frac{\Delta r}{r} .
$$

**Three changes from the free pair, and the list is complete.** The kinetic term carries $\vec\pi$ and not $\nabla S$; the phase equation carries $-ϙ\varphi$; the transport equation carries the kinetic velocity $\vec\pi/m$ and not $\nabla S/m$.

**The quantum potential is unchanged, and that is a theorem and not an observation.** $Q$ is built from $r$ and its ordinary Laplacian. The connection is central imaginary in every slot, so it cannot enter the scale gradient; the scale bracket of the logarithmic derivative is real, and the connection's addition is imaginary. **A gauge field cannot change the size of the quantum potential of a scalar state**, and the limit therefore drops the same term with and without a connection.

| object | free | coupled | changed by the connection |
|---|---|---|---|
| transport current | $r^{2}\nabla S/m$ | $r^{2}\vec\pi/m$ | yes |
| kinetic term of the eikonal | $\lvert\nabla S\rvert^{2}/2m$ | $\lvert\vec\pi\rvert^{2}/2m$ | yes |
| potential term | $0$ | $-ϙ\varphi$ | yes |
| quantum potential | $-\frac{\hbar^{2}}{2m}\frac{\Delta r}{r}$ | same | no |
| amplitude, real and positive | yes | yes | no |

**One asymmetry worth stating.** The connection moves the phase and only the phase, so the limit that reads the phase equation inherits the whole of the coupling, and the limit that reads the density inherits only the velocity. That is why the coupled limit is a mechanics of a charged fluid and not a new expansion.

## The Eikonal

**Drop the quantum potential.**

$$
\partial_{t'}S+\frac{\lvert\nabla S+ϙ\vec A\rvert^{2}}{2m}-ϙ\varphi=0 .
$$

**In the algebra it is a norm, shifted.** Writing $\vec\pi$ for the kinetic momentum,

$$
\frac{1}{2m}\langle\vec\pi\rangle_{\natural}=\mathcal E ,
\qquad
\mathcal E=-\partial_{t'}S+ϙ\varphi ,
$$

so the kinetic energy is the biquaternion norm of the kinetic momentum, exactly as in the free case with $\vec\pi$ in place of $\vec p$. The kinetic momentum is a real quaternion, its norm is the central kinetic energy, and the identity is the free one with the connection absorbed into the momentum.

**The characters are the trajectories of a charge.** The characteristic system is $\dot{\vec r}=\vec\pi/m$ and $\dot{\vec p}=-\nabla H$ with $H=\frac{\lvert\vec\pi\rvert^{2}}{2m}-ϙ\varphi$. Differentiating the eikonal and using that the curl of a gradient vanishes gives the Lorentz force in the article's convention,

$$
\frac{d\vec\pi}{dt'}=-ϙ\left(\vec E+\vec v\times\vec B\right),
\qquad
\vec v=\frac{\vec\pi}{m},
\qquad
\vec E=-\nabla\varphi-\partial_{t'}\vec A ,
$$

which is $q(\vec E+\vec v\times\vec B)$ with $q=-ϙ$. **The force is one step from the eikonal and needs no separate postulate**, and the step is the same gradient that produced the free Newton equation.

**Two structural readings.** The canonical flow is irrotational, $\nabla\times\nabla S=0$, and the kinetic flow is rotational exactly where the magnetic field is,

$$
\nabla\times\vec v=\frac{ϙ}{m}\,\vec B .
$$

So the magnetic field is the only source of vorticity in the limit, and a region with $\vec B=0$ has an irrotational kinetic flow there. That is the limit's statement of the Aharonov–Bohm structure: the vector potential is invisible in the local velocity's curl and visible on a loop.

**A uniform potential does nothing to the rays.** With $\vec A=0$ and $\varphi$ constant, the eikonal differs from the free one by a constant and the trajectories are identical; the phase's rate is shifted by $ϙ\varphi/\hbar$ and the scale is untouched. In the polar chart's flow language the constant potential translates the frequency and leaves the rapidity, the gap and the density exactly as they were.

## The Transport

**The equation is exact and it is not an expansion.** $\partial_{t'}(r^{2})+\nabla\cdot(r^{2}\vec\pi/m)=0$ says that the density is transported by the kinetic velocity. It never contained $\hbar$, so the limit neither produces it nor spoils it.

**Its content is one sentence.** The fluid moves with $\vec\pi/m$ and not with $\nabla S/m$; the difference is $ϙ\vec A/m$, and it is the whole of the coupling's effect on the density's motion.

**The current is gauge invariant.** $r^{2}\vec\pi/m$ is invariant term by term, while $r^{2}$ and $\vec\pi$ are separately invariant and $\vec A$ is not. The current is therefore a physical object and the vector potential is not, which is the standard statement read on the pair.

**The one-dimensional amplitude is the free one.** Where $\vec A$ can be gauged away locally and the field is stationary, the transport equation reduces to the free one and $A=C/\sqrt{\lvert\pi\rvert}$: the amplitude is large where the kinetic momentum is small. In three dimensions the van Vleck determinant carries the amplitude, with the ray congruence now the congruence of the Lorentz trajectories; the focusing of a magnetic field on a bundle of rays is what the determinant measures, and a caustic in a magnetic field is the place where it vanishes.

## The Circulation

**A loop, and the exact statement.** Let $\vec B=0$ in a region that is not simply connected, and let the field be central there. The phase is single valued on the field, so its gradient integrates to $2\pi\hbar n$ around the loop with $n$ the winding, and the kinetic circulation is

$$
\oint\vec v\cdot d\vec l=\frac{2\pi\hbar\,n+ϙ\,\Phi_B}{m},
\qquad
\Phi_B=\oint\vec A\cdot d\vec l=\int_\Sigma\vec B\cdot d\vec S .
$$

**This is exact and it is not a result of the limit.** It follows from the vorticity identity integrated over a surface, and it holds for any state of the polar form, semiclassical or not. The limit inherits it, and the reason it survives is that a circulation is a statement about a loop while the criterion is a statement about a length: no $\epsilon$ appears.

**Where it belongs in the reading.** It is a statement about the phase gradient, so it belongs to the operator setting, where a gradient exists. In the constant setting there is no loop, and the vector potential acts as a shift of the rotor's axis; the two readings agree on a plane wave, where the axis and the phase gradient are the same momentum.

**What it needs.** $\vec B=0$ on the surface and nothing else: not a weak field, not a slow field, not a field-free region. Where $\vec B\neq0$ the circulation is not quantised, because the phase's gradient need not be single valued there.

## The Error

**The error is the free error.** $Q$ is untouched by the connection, so $\rho=\lvert Q\rvert/\mathcal E$ is the free ratio with the kinetic energy in the denominator. For a Gaussian amplitude and a constant connection,

$$
\rho(x)=\epsilon^{2}\left\lvert\frac{x^{2}}{4\sigma^{2}}-\frac{1}{2}\right\rvert
$$

exactly as in the free case, and the table of *The Non-Quantum Limit of the Free Schrödinger Equation* applies unchanged.

**The connection can make the region smaller without appearing in the ratio.** A magnetic field focuses a bundle of rays, so $L$ shrinks along the bundle and $\epsilon$ grows; the ratio itself carries no $\vec A$. The two statements are consistent: the criterion is a property of the amplitude, and the field acts on the amplitude through the focusing of the congruence and not through the equation's coefficients.

**That is the sharpest difference between the two limits.** The relativistic limit's error is a number and the algebra's entries fix it. The non-quantum error is an operator that changes sign, and a connection can move its zeros by moving the amplitude and cannot change its shape.

## The Gauge Direction in the Limit

**The free chart has no gauge direction; the coupled one has exactly one.** In the free case the phase's rate is fixed and there is no freedom to fix. With the connection, $\theta_{\mathrm{pha}}$ acquires an additive function $\Gamma$ and the equation determines only $\mathcal E$.

**The limit keeps the gauge structure intact, and it must.** An expansion in $\epsilon$ that truncated $\partial_{t'}\theta_{\mathrm{pha}}$ alone would break gauge invariance, because the truncated object shifts while the exact one does not. Written on $\mathcal E$ and $\vec\pi$, as above, the truncated equations are gauge invariant order by order.

**One consequence for the twelve articles.** Every limit article in a coupled family has to state its expansion variable as an invariant combination and not as a bare derivative. That is a rule of the writing and not a theorem of the physics, and this article is where it is stated for the Schrödinger family.

## What the Biquaternion Form Adds

**Standard quantum hydrodynamics, transcribed.** The covariant pair, the kinetic momentum, the potential energy in the phase equation, the Lorentz force from the eikonal, the vorticity identity, the circulation quantum and the amplitude are all standard. The ordering by $\epsilon$ and the statement of the error are standard too.

**Four things the notation supplies.**

*The connection's destination is a type statement.* It is central imaginary in every slot, so it joins the phase bracket and cannot reach the scale, the boost or the rotor. That is not an approximation and not a smallness statement: it is a statement about which of the four brackets of the logarithmic derivative can receive an addition of that type. It is why the quantum potential is untouched, and it is one line in the polar chart where the element form needs an argument.

*The two invariants have a home.* $\vec\pi$ is a real quaternion and $\mathcal E$ is central, so the mechanical momentum and the mechanical energy sit in $\mathbb{B}_{H}$ and $\mathbb{B}_{C}$ in the same way the free $\vec p$ and $E$ do. The coupled limit therefore changes no sector assignment.

*The gauge group is one coordinate.* Seven of the eight parameters are inert and one is translated, by a function of the point. The limit's gauge problem is then visibly one-dimensional: one direction in the chart, and the truncation must be transverse to it.

*The loop is a chart statement.* The circulation is $\oint\nabla S\cdot d\vec l$ computed on the phase coordinate, with the connection added; the Aharonov–Bohm phase is the value of the phase coordinate around a loop, and the polar chart makes that the primitive object rather than a derived one.

**What it does not supply.** No new solution, no decoupling of the brackets from the parameters, and no second constant of motion. The word remains a chart in which the structure is visible, and not a solution method.

## Summary

The coupled limit is the free limit read on two invariant combinations. The state is $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\epsilon_\pm e_t$; the invariants are $\vec\pi=\nabla S+ϙ\vec A$ and $\mathcal E=-\partial_{t'}S+ϙ\varphi$. The exact pair is

$$
\partial_{t'}\left(r^{2}\right)+\nabla\cdot\left(r^{2}\frac{\vec\pi}{m}\right)=0 ,
\qquad
\partial_{t'}S+\frac{\lvert\vec\pi\rvert^{2}}{2m}-ϙ\varphi+Q=0 ,
\qquad
Q=-\frac{\hbar^{2}}{2m}\frac{\Delta r}{r} .
$$

Dropping $Q$ gives the eikonal $\frac{1}{2m}\langle\vec\pi\rangle_{\natural}=\mathcal E$, whose characters are the Lorentz trajectories with $\frac{d\vec\pi}{dt'}=-ϙ(\vec E+\vec v\times\vec B)$, and whose kinetic flow has $\nabla\times\vec v=\frac{ϙ}{m}\vec B$. The transport equation is exact and carries the kinetic velocity. The circulation $\oint\vec v\cdot d\vec l=(2\pi\hbar n+ϙ\Phi_B)/m$ is exact and no $\epsilon$ appears in it. The quantum potential is untouched by the connection, so the error of the approximation is the free error, and the connection can shrink the region only by focusing the rays. The gauge direction is one-dimensional and the truncation must be written on invariants, or it breaks the gauge symmetry the exact equation has.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\epsilon_\pm e_t$ | The central-field word; scale, phase, branch |
| $S=\hbar\,\theta_{\mathrm{pha}}$ | The action |
| $ϙ$ | The coupling; minus the electric charge |
| $\tilde A_\Phi=i(\varphi/c)e_t+\vec A$ | The material connection |
| $\vec p=\nabla S$ | Canonical momentum |
| $\vec\pi=\nabla S+ϙ\vec A$ | Kinetic momentum; real quaternion in $\mathbb{B}_{H}$ |
| $\mathcal E=-\partial_{t'}S+ϙ\varphi$ | Kinetic energy; central, gauge invariant |
| $\epsilon=1/(k_{\Phi}L)$ | The parameter of the limit |
| $Q=-\frac{\hbar^{2}}{2m}\Delta r/r$ | Quantum potential; unchanged by the connection |
| $\frac{1}{2m}\langle\vec\pi\rangle_{\natural}=\mathcal E$ | The eikonal, as a norm |
| $\nabla\times\vec v=\frac{ϙ}{m}\vec B$ | Vorticity of the kinetic flow |
| $\frac{d\vec\pi}{dt'}=-ϙ(\vec E+\vec v\times\vec B)$ | Lorentz force from the eikonal |
| $\oint\vec v\cdot d\vec l=\frac{2\pi\hbar n+ϙ\Phi_B}{m}$ | Circulation; exact |

## Further Reading

- L. D. Landau and E. M. Lifshitz, *Quantum Mechanics: Non-Relativistic Theory* (Pergamon, 1977), for the covariant Madelung pair and the circulation quantum.
- A. Messiah, *Quantum Mechanics* (North-Holland, 1961), for the amplitude–phase separation with a vector potential.
- E. Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1927) 322–326, for the hydrodynamic form of the Schrödinger equation.
- T. Takabayasi, "On the formulation of quantum mechanics associated with classical pictures," *Progress of Theoretical Physics* **8** (1952) 143–182, for the hydrodynamical reading with a connection.
- Y. Aharonov and D. Bohm, "Significance of electromagnetic potentials in the quantum theory," *Physical Review* **115** (1959) 485–491, for the loop statement.
- M. V. Berry, "Quantum phase corrections from adiabatic iteration," *Proceedings of the Royal Society A* **414** (1987) 31–46, for the geometric phase read as a phase-coordinate holonomy.
