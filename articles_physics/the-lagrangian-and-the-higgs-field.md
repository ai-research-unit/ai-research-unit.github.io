# __The Lagrangian and the Higgs Field__

## Introduction

**The question.** The electroweak sector's scalar is the one field in the corpus whose action is written twice in two places and never as a family article. *The Lagrangian and the Electroweak Theory* writes the full gauge action with the doublet inside it, and *Electroweak Symmetry Breaking* reads the masses and the couplings off the mass matrix. Neither asks the spin-zero question on its own: what is the action of the scalar field, what does its variation give, and what does the potential fix that the masses do not. This article asks it.

**The answer in five sentences.** The scalar action is the Klein–Gordon action for a complex doublet with a potential $V=-\mu^{2}\Phi^{\dagger}\Phi+\lambda(\Phi^{\dagger}\Phi)^{2}$, and the potential is a function of one variable, $r^{2}=2\Phi^{\dagger}\Phi$, so the four real components split into one radial direction that is curved and three angular directions that are flat. The variation gives $\Box\Phi=\mu^{2}\Phi-2\lambda(\Phi^{\dagger}\Phi)\Phi$, whose radial reading is the anharmonic oscillator and whose unitary reading is $\Box h+m_h^{2}h+3\lambda vh^{2}+\lambda h^{3}=0$. The mass is the curvature of the potential at its minimum, $m_h^{2}=2\lambda v^{2}$, and the same $\lambda$ fixes the cubic and quartic self-couplings at $6\lambda v$ and $6\lambda$, so one number is measured three times. The three flat directions are the would-be Goldstone modes, and that is the whole of what the scalar sector contributes to the breaking.

**Why this article exists apart from the sector article.** Because the sector article's subject is the gauge action and its two phases, and the scalar's own structure is a different claim. Here the gauge fields are spectators: the covariant derivative is replaced by the ordinary one, and the difference between the two actions is exactly the vector mass term, which the companion derives. What is left is a potential and its derivatives, and those are exact.

**What is not done.** No loop, no renormalisation, no running, no unitarity computation, no scattering amplitude and no decay rate. The value of $\lambda$ is taken from the measured mass and is not derived. Nothing here is the Standard Model's quantised scalar sector, and the article says so at the point where the reader would expect it.

**Declared omissions.** The reality of the action is settled inside *The Action*, term by term, so slot 5 is omitted, with its four subsections. The scalar imposes no constraint on the initial data beyond its own equation — it has no gauge symmetry and no Gauss law — so slot 6 is omitted. The second variation is not computed, so slot 8 is omitted. The two settings are not contrasted, so slot 10 is omitted. No limit is taken here, so slot 11 is omitted. No comparison with the textbook $\phi^{4}$ treatment is attempted, so slot 13 is omitted. The open questions are named in the ledger and not listed, so slot 14 is omitted.

## Conventions

**The conventions are the electroweak articles', with the gauge fields switched off.** The metric is mostly plus, the measure $\mathrm{d}^{4}x$, and $\hbar=c=1$ throughout. The doublet is a complex two-component column,

$$
\Phi=\frac{1}{\sqrt2}\begin{pmatrix}\phi_1+i\phi_2\\ \phi_3+i\phi_4\end{pmatrix},
$$

so that $\Phi$ carries four real components $\phi_A$ and $\Phi^{\dagger}\Phi=\frac12\sum_A\phi_A^{2}$. The potential is

$$
V(\Phi)=-\mu^{2}\Phi^{\dagger}\Phi+\lambda(\Phi^{\dagger}\Phi)^{2},
\qquad \mu^{2}>0,\quad \lambda>0,
$$

and its minimum sits at $\Phi^{\dagger}\Phi=\mu^{2}/2\lambda\equiv v^{2}/2$, so that $v^{2}=\mu^{2}/\lambda$ and $v\simeq246.22$ GeV.

**The radial variable, named once.** Write $r=\sqrt{2\Phi^{\dagger}\Phi}$, a real non-negative field with $\dim r=1$. Every statement in this article that is not about the phase is a statement about $V$ as a function of $r$, and the notation is used to make that visible.

**The unitary chart.** Where a component reading is needed the chart is $\Phi=\frac{1}{\sqrt2}\binom{0}{v+h}$ with $h$ real. It is a chart on the same action and not a different theory; the companion article states what it costs and what it buys.

**Two conventions are warnings.** The first: $\mu^{2}$ has the dimensions of a mass squared and is not a mass. The curvature at the minimum is $2\mu^{2}$, and the difference matters — the free Klein–Gordon article's $k_m^{2}$ is the coefficient of $-\tilde\Xi^{*}\tilde\Xi$ with a fixed sign, whereas here the sign is negative and the coefficient is not the mass. The second: $\lambda$ in this normalisation is the coefficient of $(\Phi^{\dagger}\Phi)^{2}$, so the quartic term in the unitary chart is $\frac{\lambda}{4}h^{4}$. A reader who imports $\frac{\lambda}{4!}\phi^{4}$ from the scalar-field literature will find the self-couplings wrong by a factor of six.

## The Action in Element Form

**The scalar block of the electroweak action, with the connection removed.**

$$
S[\Phi,\Phi^{\dagger}]=\int\mathrm{d}^{4}x\;\Bigl\{\partial_\mu\Phi^{\dagger}\,\partial^{\mu}\Phi-V(\Phi)\Bigr\}
=\int\mathrm{d}^{4}x\;\Bigl\{\tfrac12\partial_\mu r\,\partial^{\mu}r+\tfrac{r^{2}}{2}\partial_\mu\theta_A\partial^{\mu}\theta_A+\tfrac{\mu^{2}}{2}r^{2}-\tfrac{\lambda}{4}r^{4}\Bigr\},
$$

where the second form uses the three angular coordinates of the four-sphere $r=\mathrm{const}$ and is written to show the structure and not to be varied in.

**The same action in the unitary chart.**

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{\tfrac12\partial_\mu h\,\partial^{\mu}h-\tfrac12 m_h^{2}h^{2}-\lambda vh^{3}-\tfrac{\lambda}{4}h^{4}\Bigr\},
\qquad m_h^{2}=2\lambda v^{2}.
$$

The chart is the expansion about one point of the circle of minima, and the three terms after the mass term are the same $\lambda$ read at third and fourth order.

**It is real, term by term.** The kinetic term is $\partial_\mu\Phi^{\dagger}\partial^{\mu}\Phi=\sum_A(\partial_\mu\phi_A)^{2}/2$, a sum of squares with a fixed sign. The mass term is $-\mu^{2}\Phi^{\dagger}\Phi=-\mu^{2}\sum_A\phi_A^{2}/2$, real and negative. The quartic is $\lambda(\Phi^{\dagger}\Phi)^{2}=\lambda(\sum_A\phi_A^{2})^{2}/4$, real and positive for $\lambda>0$. The potential is therefore bounded below, and the bound is what makes a minimum exist at all.

**Why the sign of $\mu^{2}$ is the whole content.** With $\mu^{2}<0$ the potential has a single stationary point, at $\Phi=0$, and it is a minimum; the four components are degenerate and each has mass $\sqrt{-\mu^{2}}$. With $\mu^{2}>0$ the origin is a maximum and the minimum is the three-sphere $\Phi^{\dagger}\Phi=v^{2}/2$. Nothing else in the action changes. The article's subject is the second case, and the first is named here only because the same display covers both.

**What the display is not.** It is not the electroweak action: three of the four derivatives are not there, and putting them back turns the three flat directions into the longitudinal polarisations of $W^{\pm}$ and $Z$. It is not a quantised action: there is no gauge fixing, no ghost and no loop. And it is not a claim that the scalar is elementary — the potential is a renormalisable truncation, and the corpus's effective-potential article treats what the truncation costs.

## The Variation

**Varying the conjugate.**

$$
\delta S=\int\mathrm{d}^{4}x\;\Bigl\{-\partial_\mu\partial^{\mu}\Phi^{\dagger}\,\delta\Phi-\frac{\partial V}{\partial\Phi^{\dagger}}\delta\Phi^{\dagger}\Bigr\}+\text{(boundary)},
$$

and holding $\delta\Phi^{\dagger}$ arbitrary gives

$$
\Box\Phi=-\frac{\partial V}{\partial\Phi^{\dagger}}=\mu^{2}\Phi-2\lambda(\Phi^{\dagger}\Phi)\Phi .
$$

**The same equation in the radial variable.** Since $\Phi^{\dagger}\Phi=r^{2}/2$ and $V(r)=-\frac{\mu^{2}}{2}r^{2}+\frac{\lambda}{4}r^{4}$,

$$
\Box r=-V'(r)=\mu^{2}r-\lambda r^{3},
$$

an equation in one real field. It is the anharmonic oscillator with the sign that makes $r=v$ a stable point, and it is the whole of the scalar's dynamics when the angular coordinates are frozen.

**The same equation in the unitary chart.**

$$
\Box h+m_h^{2}h+3\lambda vh^{2}+\lambda h^{3}=0 ,
$$

which is the radial equation expanded about $r=v+h$ with the linear term removed by the minimum condition. The three terms after the mass term are the nonlinearity, and their coefficients are fixed: there is no freedom left in them once $\lambda$ and $v$ are chosen.

**The boundary term, and why it is not an obstacle.** The equation is second order in time, so the variation needs $\Phi$ and its normal derivative fixed on the boundary — the same condition the Klein–Gordon article imposes, and the surface term vanishes under it. The scalar's variation is the simplest in the family for this reason: no gauge parameter, no constraint, no identity.

**What the variation does not give.** It does not give the masses of the vectors, the Goldstone modes, or the count. Those come from the same action with the covariant derivative restored and the vacuum chosen, and they are the companion article's subject. What the variation gives here is the scalar's equation and, through it, the statement that the potential's derivatives are the couplings.

## The Structural Consequence: One Variable, One Number, Three Measurements

**The claim.** The potential is a function of $r$ alone, so the four real components of the doublet split into one radial field with a curved potential and three angular fields with a flat one. The radial field's mass is the curvature at the minimum, and the same curvature's third and fourth derivatives are its self-couplings. One number determines three measured quantities.

**The split, in one line.** $V$ depends on the four $\phi_A$ through $\sum_A\phi_A^{2}$ and on nothing else, so the symmetry group of the potential alone is $O(4)$, acting by rotations of the four-vector. A minimum at $r=v$ breaks $O(4)$ to $O(3)$, and the count of flat directions is $4-1=3$. Those three are the would-be Goldstone modes. Nothing about the gauge fields entered this paragraph, and that is the point: the breaking is a property of the potential.

**The curvature check.** Expand $V$ about $r=v$:

$$
V(v+h)=V(v)+\tfrac12V''(v)h^{2}+\tfrac16V'''(v)h^{3}+\tfrac1{24}V''''(v)h^{4}+\cdots ,
$$

with $V'(v)=0$ by the minimum condition, $V''(v)=-\mu^{2}+3\lambda v^{2}=2\lambda v^{2}$, $V'''(v)=6\lambda v$ and $V''''(v)=6\lambda$. Comparing with the unitary display, $m_h^{2}=2\lambda v^{2}$, the $h^{3}$ coefficient is $\frac16\cdot 6\lambda v=\lambda v$, and the $h^{4}$ coefficient is $\frac{1}{24}\cdot 6\lambda=\frac{\lambda}{4}$ — which is the display, term for term.

**The three measurements.** In the normalisation where the cubic vertex is $\frac{g_{hhh}}{6}h^{3}$ and the quartic is $\frac{g_{hhhh}}{24}h^{4}$,

$$
g_{hhh}=6\lambda v=\frac{3m_h^{2}}{v},
\qquad
g_{hhhh}=6\lambda=\frac{3m_h^{2}}{v^{2}},
\qquad
\frac{g_{hhhh}}{g_{hhh}}=\frac1v .
$$

With $m_h\simeq125.25$ GeV and $v\simeq246.22$ GeV, $\lambda=m_h^{2}/2v^{2}\simeq0.129$, $g_{hhh}\simeq191$ GeV and $g_{hhhh}\simeq0.78$. The ratio is a number with the dimensions of an inverse energy and no free parameter: a reader who measures the triple coupling and the mass has tested the potential, not fitted it.

**What the claim forbids.** It forbids three things. A quartic coupling tuned independently of the mass, because the same $\lambda$ is both. A cubic coupling treated as a separate parameter, because the expansion of a quartic potential has no other cubic term. And a "Higgs mass" read as $\sqrt{2}\mu$ with $\mu$ chosen freely and $\lambda$ adjusted afterwards: the theory has $(\mu^{2},\lambda)$ and the observables are $(m_h,g_{hhh},g_{hhhh})$, three functions of two numbers, so one relation among the three is exact at this order.

**The consequence the article does not resolve.** The same display gives a vacuum energy. At the minimum $V(v)=-\lambda v^{4}/4=-m_h^{2}v^{2}/8\simeq-1.2\times10^{8}\ \mathrm{GeV}^{4}$, and nothing in the action makes it zero. That number is more than fifty orders of magnitude above the observed vacuum energy density when both are written as an energy density, and the corpus has no mechanism that removes it. It is recorded here because it is a consequence of the potential and not an assumption about it; the cosmology articles state the problem and do not solve it either.

## The Noether Currents and the Sign of the Charge

**The doublet's hypercharge current, and what becomes of it.** The action is invariant under the global phase $\Phi\mapsto e^{i\theta}\Phi$, whose current is

$$
J^{Y}_{\mu}=i\bigl(\Phi^{\dagger}\partial_\mu\Phi-\partial_\mu\Phi^{\dagger}\,\Phi\bigr),
$$

conserved by the equation of motion. In the unitary chart the doublet has one real non-zero component, and $J^{Y}_{\mu}$ vanishes identically there: $\Phi^{\dagger}\partial_\mu\Phi$ is real when $\Phi$ is real, so the two terms cancel. **The physical Higgs field carries no hypercharge.**

**Where the current went.** Into the three angular directions. A general chart writes $\Phi=\frac{1}{\sqrt2}\binom{0}{r}e^{i\theta^{a}\tau^{a}/2}$-style, and the phase directions carry $J^{Y}_{\mu}$ in proportion to their gradients. Those directions are the would-be Goldstones, and the gauge field that eats them inherits the coupling: the statement that the $Z$ has a hypercharge current is the same statement as the statement that the eaten Goldstones carried one. This is the mechanism read from the current side, and it agrees with the companion's count, which reads it from the degrees of freedom.

**The count of currents, from the potential alone.** The potential's symmetry is $O(4)$; the minimum breaks it to $O(3)$; the number of generators that do not annihilate the vacuum is $6-3=3$. So three currents are broken and one linear combination of the four electroweak generators survives — the electromagnetic one, whose charge is $Q=T^{3}+Y/2$, with the sign of the electron's charge fixed by the hypercharge assignment and not by anything in this article. The count of currents and the count of Goldstones are the same number for the same reason.

**The stress, and the sign of the energy.** With the flat directions frozen,

$$
T_{\mu\nu}=\partial_\mu h\,\partial_\nu h-\eta_{\mu\nu}\Bigl(\tfrac12\partial h^{2}-V(h)\Bigr),
\qquad
T_{00}=\tfrac12\dot h^{2}+\tfrac12(\nabla h)^{2}+V(h)-V(v),
$$

where the constant is subtracted so that the energy of the vacuum is zero by definition and the potential's depth is stated separately. Read without the subtraction, $T_{00}$ carries the constant $V(v)$ above. The kinetic and gradient terms are sums of squares; the potential's contribution is bounded below by its minimum; so the energy is bounded below and the sign is right. The indefinite-sign cross terms that appear when the Goldstones are kept are removed by the unitary chart, as the companion article states.

## What the Principle Adds and What It Relabels

**Adds.** One parameter, $\lambda$, for the whole scalar sector, with the mass as its curvature and the two self-couplings as its third and fourth derivatives. The relation $g_{hhhh}=g_{hhh}/v$. The vacuum energy as a number the potential produces. And the split into one curved and three flat directions, which is the breaking stated without the gauge fields.

**Relabels.** The corpus's Higgs-mechanism statements — the doublet, the potential, the circle of minima, the count, the masses — are all recoverable from this action, and it adds no number to them except $\lambda$, which they already contain in the form $m_h^{2}=2\lambda v^{2}$.

**What it does not reach, and this family does not either.** The loop-corrected potential, where the curvature at the minimum is not $2\lambda v^{2}$ but that number plus a correction the corpus's effective-potential article computes in outline. The running of $\lambda$ and the two bounds that follow from it — triviality at the ultraviolet end and stability at the infrared end — which the corpus's triviality article states as bounds and not as a computation inside this action. The hierarchy problem, which is the statement that the correction to $\mu^{2}$ is quadratically sensitive to the scale at which the truncation is imposed. And the value of $m_h$ itself, which the corpus takes from experiment.

**The honest sentence.** The corpus can write this action exactly, vary it exactly, and read three couplings from one number exactly. It cannot say why $\lambda$ has the value it has, and it cannot compute the correction to that value. The gap is the same gap the electroweak action article names: quantisation, and the renormalisation that comes with it.

## Summary

The scalar action is the Klein–Gordon action for a complex doublet with $V=-\mu^{2}\Phi^{\dagger}\Phi+\lambda(\Phi^{\dagger}\Phi)^{2}$, whose potential depends on one variable and whose minimum is a three-sphere. The variation gives $\Box\Phi=\mu^{2}\Phi-2\lambda(\Phi^{\dagger}\Phi)\Phi$, the radial anharmonic equation and, in the unitary chart, $\Box h+m_h^{2}h+3\lambda vh^{2}+\lambda h^{3}=0$. The curvature at the minimum is $m_h^{2}=2\lambda v^{2}$, the third and fourth derivatives give $g_{hhh}=3m_h^{2}/v$ and $g_{hhhh}=3m_h^{2}/v^{2}$, so one number is measured three times. Three directions are flat, they carry the hypercharge current, and the vectors that eat them inherit it. Nothing is quantised, and the value of $\lambda$ is not derived.

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{\partial_\mu\Phi^{\dagger}\partial^{\mu}\Phi+\mu^{2}\Phi^{\dagger}\Phi-\lambda(\Phi^{\dagger}\Phi)^{2}\Bigr\},
\qquad
m_h^{2}=2\lambda v^{2},\quad v^{2}=\frac{\mu^{2}}{\lambda}.
$$

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi$ | Complex doublet, four real components $\phi_A$ |
| $\mu^{2},\ \lambda$ | Mass-squared parameter and quartic coupling, both positive |
| $v=\sqrt{\mu^{2}/\lambda}$ | Magnitude of the vacuum expectation value, $\simeq246.22$ GeV |
| $r=\sqrt{2\Phi^{\dagger}\Phi}$ | Radial field, the potential's only argument |
| $h=r-v$ | Physical scalar fluctuation in the unitary chart |
| $m_h^{2}=2\lambda v^{2}$ | Curvature of the potential at the minimum |
| $g_{hhh}=3m_h^{2}/v$ | Cubic self-coupling, $=6\lambda v$ |
| $g_{hhhh}=3m_h^{2}/v^{2}$ | Quartic self-coupling, $=6\lambda$ |
| $J^{Y}_{\mu}$ | Hypercharge current of the doublet, vanishing on the radial direction |
| $V(v)=-m_h^{2}v^{2}/8$ | Depth of the potential at the minimum |

## Further Reading

- *The Lagrangian and the Electroweak Theory*, for the same scalar inside the full gauge action, its two phases and the vector masses.
- *Electroweak Symmetry Breaking: the Doublet, the Potential and the Gauge-Boson Masses*, for the mass matrix, the count and the couplings read from the masses rather than from the potential's derivatives.
- *The Higgs Mechanism in Biquaternionic Form*, for the central scalar and the covariant derivative in the biquaternion algebra.
- *The Effective Potential and the Coleman–Weinberg Mechanism in Biquaternionic Form*, for the one-loop correction this article does not compute.
- *The Landau Pole, Triviality and Vacuum Stability*, for the two bounds that follow from the running of $\lambda$.
- *The Lagrangian and the Interacting Scalar Field*, for the same quartic term without the negative mass squared, where the symmetry is unbroken.
- *The Lagrangian and the Goldstone Effective Action*, for the three flat directions treated as fields of their own.
- Chris Quigg, *Gauge Theories of the Strong, Weak and Electromagnetic Interactions*, for the classical potential and the self-couplings.
