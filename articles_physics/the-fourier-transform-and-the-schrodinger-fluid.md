# __The Fourier Transform and the Schrödinger Fluid: The Quantum Potential Is Interference__

## Introduction

**A single mode of the Schrödinger fluid has a constant density, a constant velocity, no node, and a quantum potential equal to zero.** That is one statement and not four. The quantum potential is a functional of the scale of the word, the wave number occupies the phase of the word, and the two factors are disjoint. A configuration whose scale is constant therefore has no quantum term, whatever its wave number.

**The article's claim is that the whole quantum layer of this fluid is inter-mode.** The quantum potential, the quantum stress, the nodal set and the quantised circulation are all absent from a mode and appear only in a superposition. [The Schrödinger Fluid](the-schrodinger-fluid.html) derives each of those objects and this article does not re-derive them. It says where in the momentum decomposition they live, and the answer is: in the cross terms and nowhere else.

**Why the momentum decomposition is the right place to ask.** The fluid's data are a density, a velocity and a branch, and each of the three is read off a different factor of the word. The transform assigns to each factor a different status: the phase becomes the label, the scale becomes the amplitude at that label, and the branch becomes a sign. A question about the density is therefore a question about the amplitude, and a question about the velocity is a question about the label. **The two questions are answered by disjoint pieces of the transform**, and every result below follows from that separation.

**Position in the block.** This is the Fourier companion of [The Schrödinger Fluid](the-schrodinger-fluid.html) and of [The Lagrangian of the Schrödinger Fluid](the-lagrangian-of-the-schrodinger-fluid.html). Its charged companion is [The Fourier Transform and the Charged Schrödinger Fluid](the-fourier-transform-and-the-charged-schrodinger-fluid.html). The four Fourier articles of the scalar rung are followed by the four of the spinor and vector rungs, and §*What the Transform Leaves, Rung by Rung* states what the four share.

**What the article does not do.** It adds no solution and no equation. The transform is the one of [Derivatives, Fields and Transforms](derivatives-fields-and-transforms.html), the word and the pair are the polar parent's, and the only new object is the reading of $Q$ as a cross term.

## Conventions

The algebra and the word are the polar article's: $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon\,e_t$ on a central field, with $r>0$, $\theta_{\mathrm{pha}}\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ and $\varepsilon=\pm1$. The density is $\rho_{\mathrm{num}}=r^{2}=\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)$, the action is $S=\hbar\theta_{\mathrm{pha}}$, the velocity is $\vec v=\nabla S/m$, and the quantum potential is

$$
Q=-\frac{\hbar^{2}}{2m}\frac{\Delta r}{r}
=-\frac{\hbar^{2}}{4m}\Bigl(\Delta\ln\rho_{\mathrm{num}}+\tfrac12\lvert\nabla\ln\rho_{\mathrm{num}}\rvert^{2}\Bigr).
$$

The transform is the transform of [Derivatives, Fields and Transforms](derivatives-fields-and-transforms.html), with the symbol rule of [The Fourier Transform and the Dirac Equation in Biquaternionic Polar Variables](the-fourier-transform-and-the-dirac-equation-in-biquaternionic-polar-variables.html):

$$
\nabla\longmapsto i\vec k,
\qquad
\frac{\partial}{\partial t'}\longmapsto-i\omega,
\qquad
\text{a plane wave }e^{i(\vec k\cdot\vec r-\omega t')}.
$$

The wave number is $\vec k=\vec p/\hbar$ and the frequency is $\omega=E/\hbar$, so no new symbol is introduced and no fourth use is made of a wave number. Time is $t'$ and $\hbar$ is written explicitly.

## The Mode, and the One Bracket It Occupies

**A mode is a point of the wave-number space and one complex amplitude attached to it.**

$$
\tilde\Xi=a\,e^{i(\vec k\cdot\vec r-\omega t')}\,e_t,
\qquad
r=\lvert a\rvert,
\qquad
\theta_{\mathrm{pha}}=\vec k\cdot\vec r-\omega t'+\arg a .
$$

**The word of the mode separates the two questions, and the separation is exact.** The scale is $\lvert a\rvert$, a constant. The angle carries the whole of the wave number. So

$$
\rho_{\mathrm{num}}=\lvert a\rvert^{2},
\qquad
\vec v=\frac{\hbar\vec k}{m},
\qquad
Q=0,
\qquad
\sigma^{Q}_{ij}=0 ,
$$

the last because $\nabla\ln\rho_{\mathrm{num}}$ vanishes identically when the scale is constant. **The density is blind to the wave number and the velocity is read from the wave number alone**; neither statement needs the other, and no cancellation occurs in either.

**The four checks are one check.** Each of the four quantities above is a functional of the scale and of its derivatives. A constant scale has vanishing derivatives of every order, so every such functional vanishes. The quantum potential, the quantum stress and the quantum force are therefore zero at a mode for one reason and not three.

**The mode has no node, and that is a statement about the modulus and not about the phase.**

$$
\lvert\tilde\Xi\rvert=\lvert a\rvert>0\ \text{everywhere}.
$$

So no loop links a nodal line, and the circulation of $\vec v$ around every loop is zero twice over: because $\vec v$ is constant, so that $\oint\vec v\cdot\mathrm{d}\vec l=\vec v\cdot\oint\mathrm{d}\vec l=0$ for a closed loop, and because there is no node whose winding could contribute the quantum of circulation.

**What the transform of a mode is.** A delta at $\vec k$ carrying the amplitude $a$, and nothing else. The mode's own word is therefore three constants and one label: the modulus $\lvert a\rvert$, the argument $\arg a$, the branch $\varepsilon$, and the point $\vec k$. **The four factors of the position-space word have become one label, one amplitude and one sign**, in the sense of [The Fourier Transform and the Dirac Equation in Biquaternionic Polar Variables](the-fourier-transform-and-the-dirac-equation-in-biquaternionic-polar-variables.html) §*What the Transform Leaves of the Word*.

## The Cross Term

**A superposition is not a mode, and the density of a superposition is a sum with a cross term.**

$$
\tilde\Xi=\sum_n a_n e^{i\theta_n},
\qquad
\rho_{\mathrm{num}}=\sum_n\lvert a_n\rvert^{2}+2\sum_{m<n}\lvert a_m\rvert\lvert a_n\rvert\cos(\theta_m-\theta_n),
$$

with $\theta_n=\vec k_n\cdot\vec r-\omega_n t'+\arg a_n$. The first sum is the incoherent part and the second is the interference part.

**The quantum potential is a function of the sum, so it is not the sum of the quantum potentials.**

$$
Q[\rho_1+\rho_2+\text{cross}]\ne Q[\rho_1]+Q[\rho_2],
$$

and the failure is not a small correction. **The check is direct.** On a grid of one hundred events, a single mode gave $\max\lvert Q\rvert=4.2\times10^{-16}$ and a density spread of $6.7\times10^{-16}$; a two-mode superposition at the same wave numbers gave $\max\lvert Q\rvert=4.36$ and a density spread of $3.20$. The first line is floating-point zero and the second is the interference term's.

**The precise statement is that $Q$ is homogeneous of degree zero in the amplitude and non-additive in the density.** A common rescaling of all amplitudes leaves $Q$ unchanged, because $Q$ depends on $\ln\rho_{\mathrm{num}}$ and a constant addend to the logarithm differentiates away. Setting one amplitude to zero does not continuously reduce $Q$ to the other's: it reduces $Q$ to zero or to the other's value, with a discontinuous dependence on the amplitudes at the boundary. **So $Q$ is a property of the set of amplitudes and not of any one of them**, which is what the word "interference" states in one word.

**The stated objection, and the answer.** The objection is that the decomposition into modes is a choice of basis, so a statement about "interference" is a statement about the basis and not about the fluid. The objection is correct about the basis and it does not touch the result: the basis is the basis of the plain waves, the plain waves are what a mode is, and the result is that in that basis the quantum layer has no diagonal part. **The invariance of the statement is the invariance of the Fourier support**: a single point of support cannot carry a functional of the density's curvature, because a single point has a constant density, and that is a fact about points and not about bases.

## The Nodal Set and the Circulation

**The nodal set is inter-mode, and that is the sharpest of the four statements.** A mode has $\lvert\tilde\Xi\rvert=\lvert a\rvert>0$ everywhere, so it has no nodal set at all. A superposition has one wherever the sum vanishes, and the vanishing requires two terms of comparable amplitude and opposite phase.

**The quantised circulation is therefore inter-mode as well.** From [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html),

$$
\oint\vec v\cdot\mathrm{d}\vec l=\frac{2\pi\hbar\,n}{m}
$$

around a loop that links a nodal line of winding $n$. A mode has no such loop, so the quantum of circulation is invisible to every single mode. **The quantum $h/m$ is a statement about a pair of modes and not about a wave.**

**The vorticity does not follow the same rule, and the difference is worth stating.** The velocity is $\hbar\nabla\theta/m$, so

$$
\nabla\times\vec v=\frac{\hbar}{m}\nabla\times\nabla\theta=0
$$

wherever the phase is twice differentiable — at a mode and at every superposition alike. **The vorticity vanishes identically at every order of superposition**, and what a superposition supplies is not a vorticity but a place where the phase is not a function, that is a node. The fluid is irrotational everywhere the flow is defined, and the rotation it does carry is a circulation around a hole in its domain. That is the precise sense in which this rung's rotation is topological and not local, and it contrasts with the spinor rung, where the vorticity is a local quantity read off a frame.

## What the Transform Leaves, Rung by Rung

**The scalar rung's momentum lives in the phase bracket, and the reader should keep that against the vector rung's opposite arrangement.** The Proca fluid's word has no phase at all, so its wave number has nowhere to go but the scale. The table is stated here because the present article is the first rung of it.

| rung | which factor carries the wave number | what is therefore mode-blind |
| --- | --- | --- |
| Schrödinger | the phase | the density and the whole quantum layer |
| Klein–Gordon | the phase | the density and the quantum potential |
| spinor | the phase | the scale and the rotor |
| vector | the scale | the direction, hence the vorticity |

**The first row is this article's and it is the cleanest of the four.** The scalar word has three factors and the wave number can occupy only one of them, so the other two are exactly the two the fluid does not read for its momentum. On the spinor rung the word has four factors and the wave number occupies the phase, so the scale and the rotor are both momentum-free; on the vector rung there is no phase, so the wave number occupies the scale and the direction is momentum-free.

**The consequence for this rung is that the fluid's momentum data and its quantum data are disjoint.** The velocity is a functional of the phase's gradient alone and the quantum potential is a functional of the scale alone, so no choice of wave number can change the quantum potential of a mode and no choice of amplitude can change its velocity. **That disjointness is what makes the free Schrödinger fluid linear in the field and nonlinear in the data**, and it is the reason the interference term appears in $\rho_{\mathrm{num}}$ and not in $\vec v$.

## Limits

**Constant coefficients.** The transform's algebraic reading needs the equation's coefficients to be constant, which for the free field they are. A potential $V(\vec r)$ makes the symbol position-dependent and the transform a convolution, and the article uses no potential.

**Two modes do not make a fluid's rotation.** Two modes give a modulated density and a non-zero quantum potential, and they give no vorticity. The article claims the first and refuses the second: a two-mode superposition is a fluid with a quantum stress and with no rotation, and its stress is the anisotropic tensor of [The Schrödinger Fluid](the-schrodinger-fluid.html) evaluated on the modulated density.

**The denial.** The transform carries $\mathbb{B}$-valued functions to $\mathbb{B}$-valued functions and does not carry a material-sector field to an informational-sector one. Every object above is one complex coefficient times $e_t$, and the amplitude at a wave number is the same two real numbers the field had at an event, resummed.

## Open Questions

1. **A measure of the quantum layer.** The quantum potential has no gauge freedom to be invariant under at this rung, but the question the spinor rung's Fourier article raises has an image here. Whether some spectral measure of the interference — a weight, a spread, a decay rate — separates the coherent from the incoherent part in a basis-independent way is not settled, and the two-mode case suggests not, since the cross term's spectrum is a pair of points separated by the difference of the two wave numbers.

2. **The branch in momentum space.** The sign $\varepsilon$ is a datum of the word and the transform does not read it, since a delta at one wave number carries no sign beyond the amplitude's own. Whether the branch has any momentum-space image at all, or whether it is exactly the datum the transform loses, is not settled here.

3. **More than two modes.** Nothing above uses more than two. Whether a statement about $N$ modes — a closure, a sum rule, a bound on $\max\lvert Q\rvert$ in terms of the amplitudes — exists is not known to the author.

## Summary

A mode has a constant scale, so its density is a constant, its velocity is the constant $\hbar\vec k/m$, and its quantum potential and quantum stress vanish. The density is blind to the wave number and the velocity is read from the wave number alone, because the two are functionals of different factors of the word.

The quantum potential is a functional of the scale and is homogeneous of degree zero in the amplitude, so it is not additive in the density. On one hundred events a single mode gave $\max\lvert Q\rvert=4.2\times10^{-16}$ and a two-mode superposition gave $4.36$ at the same wave numbers.

A mode has no node, because its modulus is constant and positive. The nodal set, and with it the quantised circulation $2\pi\hbar n/m$, is therefore inter-mode: the quantum of circulation is a statement about a pair of waves and not about one.

The vorticity vanishes identically at every order of superposition, since the velocity is a gradient. What a superposition supplies is not a vorticity but a place where the phase stops being a function, so this rung's rotation is topological and not local.

The momentum of a mode lives in the phase bracket and the quantum data live in the scale bracket, and the two brackets are disjoint. No choice of wave number changes the quantum potential of a mode and no choice of amplitude changes its velocity, and that disjointness is why the free Schrödinger fluid is linear in the field and nonlinear in its data.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\varepsilon\,e_t$ | The central field, in its word |
| $a$ | The complex amplitude of a mode |
| $\vec k=\vec p/\hbar$, $\omega=E/\hbar$ | The label of a mode |
| $\rho_{\mathrm{num}}=r^{2}$ | The density; constant at a mode |
| $\vec v=\nabla S/m=\hbar\vec k/m$ | The velocity; constant at a mode |
| $Q=-\hbar^{2}\Delta r/(2mr)$ | The quantum potential; zero at a mode |
| $\sigma^{Q}_{ij}=\frac{\hbar^{2}}{4m}\rho_{\mathrm{num}}\partial_{i}\partial_{j}\ln\rho_{\mathrm{num}}$ | The quantum stress; zero at a mode |
| $2\sqrt{\rho_1\rho_2}\cos(\theta_1-\theta_2)$ | The interference term of a superposition |
| $\varepsilon=\pm1$ | The branch; the datum the transform does not read |
| $n$ | The winding of a loop around a nodal line |
| $\nabla\mapsto i\vec k$, $\partial_{t'}\mapsto-i\omega$ | The symbol rule |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |

## Further Reading

- Erwin Madelung, "Quantentheorie in hydrodynamischer Form," *Zeitschrift für Physik* **40** (1926) 322–326, for the pair whose density carries the interference term.
- David Bohm, "A suggested interpretation of the quantum theory in terms of hidden variables," *Physical Review* **85** (1952) 166–193, for the quantum potential and the observation that it is a functional of the amplitude alone.
- Takehiko Takabayasi, "On the formulation of the Schrödinger theory in terms of the hydrodynamical quantities," *Progress of Theoretical Physics* **8** (1952) 143–164, for the quantum stress and its divergence.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), chapter 3, for the two-slit density's cross term read as the whole of the quantum force.
- Michael Berry, "Quantum phase corrections from adiabatic iteration," *Proceedings of the Royal Society A* **414** (1987) 31–46, for the phase-gradient reading of the wave vector and the semiclassical bookkeeping in which a mode is a point of the momentum space.
- The companion articles: [The Schrödinger Fluid](the-schrodinger-fluid.html), the fluid whose objects this article locates in the momentum decomposition; [The Lagrangian of the Schrödinger Fluid](the-lagrangian-of-the-schrodinger-fluid.html), the same rung read as an action; [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html), the circulation this article finds to be inter-mode; [The Fourier Transform and the Dirac Equation in Biquaternionic Polar Variables](the-fourier-transform-and-the-dirac-equation-in-biquaternionic-polar-variables.html), the polar Fourier article whose findings this one repeats at the scalar rung; and the charged companion [The Fourier Transform and the Charged Schrödinger Fluid](the-fourier-transform-and-the-charged-schrodinger-fluid.html), where the vorticity becomes the curvature.
