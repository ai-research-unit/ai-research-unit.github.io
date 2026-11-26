# __The Lagrangian and the Higgs Field__

## Introduction

The question. The electroweak sector's scalar is the one field in the corpus whose action is written twice in two places and never as a family article. *The Lagrangian and the Electroweak Theory* writes the full gauge action with the doublet inside it, and *Electroweak Symmetry Breaking* reads the masses and the couplings off the mass matrix. Neither asks the spin-zero question on its own: what is the action of the scalar field, what does its variation give, and what does the potential fix that the masses do not. This article asks it.

The answer in five sentences. The scalar action is the Klein–Gordon action for a complex doublet with a potential $V=-\mu^{2}\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}+\varpi_{\mathrm{cpl}}(\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}})^{2}$, and the potential is a function of one variable, $r^{2}=2\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}$, so the four real components split into one radial direction that is curved and three angular directions that are flat. The variation gives $\Box\omicron_{\mathrm{hgs}}=\mu^{2}\omicron_{\mathrm{hgs}}-2\varpi_{\mathrm{cpl}}(\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}})\omicron_{\mathrm{hgs}}$, whose radial reading is the anharmonic oscillator and whose unitary reading is $\Box h+m_h^{2}h+3\varpi_{\mathrm{cpl}} vh^{2}+\varpi_{\mathrm{cpl}} h^{3}=0$. The mass is the curvature of the potential at its minimum, $m_h^{2}=2\varpi_{\mathrm{cpl}} v^{2}$, and the same $\varpi_{\mathrm{cpl}}$ fixes the cubic and quartic self-couplings at $6\varpi_{\mathrm{cpl}} v$ and $6\varpi_{\mathrm{cpl}}$, so one number is measured three times. The three flat directions are the would-be Goldstone modes, and that is the whole of what the scalar sector contributes to the breaking.

Why this article exists apart from the sector article. Because the sector article's subject is the gauge action and its two phases, and the scalar's own structure is a different claim. Here the connections are spectators: the covariant derivative is replaced by the ordinary one, and the difference between the two actions is exactly the vector mass term, which the companion derives. What is left is a potential and its derivatives, and those are exact.

What is not done. No loop, no renormalisation, no running, no unitarity computation, no scattering amplitude and no decay rate. The value of $\varpi_{\mathrm{cpl}}$ is taken from the measured mass and is not derived. Nothing here is the Standard Model's quantised scalar sector, and the article says so at the point where the reader would expect it.

## Conventions

The measure is $\mathrm{d}^{4}x$, with $c$ and $h$ carried; a repeated low index is summed with the weight $\varepsilon=(1,-1,-1,-1)$, so $\partial_{\imath}\omicron_{\mathrm{hgs}}^{\dagger}\partial_{\imath}\omicron_{\mathrm{hgs}}=\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}\omicron_{\mathrm{hgs}}^{\dagger}\partial_{\imath}\omicron_{\mathrm{hgs}}$ carries the sign the mostly-minus literature carries. The doublet is a complex two-component column,

$$
\omicron_{\mathrm{hgs}}=\frac{1}{\sqrt2}\begin{pmatrix}\xi_{\mathrm{pot},1}+i\xi_{\mathrm{pot},2}\\ \xi_{\mathrm{pot},3}+i\xi_{\mathrm{pot},4}\end{pmatrix},
$$

so that $\omicron_{\mathrm{hgs}}$ carries four real components $\xi_{\mathrm{pot},A}$ and $\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}=\frac12\sum_A\xi_{\mathrm{pot},A}^{2}$. The potential is

$$
V(\omicron_{\mathrm{hgs}})=-\mu^{2}\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}+\varpi_{\mathrm{cpl}}(\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}})^{2},
\qquad \mu^{2}>0,\quad \varpi_{\mathrm{cpl}}>0,
$$

and its minimum sits at $\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}=\mu^{2}/2\varpi_{\mathrm{cpl}}\equiv v^{2}/2$, so that $v^{2}=\mu^{2}/\varpi_{\mathrm{cpl}}$ and $v\simeq3.9449\times10^{-8}\ \mathrm{J}$.

**The radial variable, named once.** Write $r=\sqrt{2\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}}$, a real non-negative field with $\dim r=1$. Every statement in this article that is not about the phase is a statement about $V$ as a function of $r$, and the notation is used to make that visible.

The unitary chart. Where a component reading is needed the chart is $\omicron_{\mathrm{hgs}}=\frac{1}{\sqrt2}\binom{0}{v+h}$ with $h$ real. It is a chart on the same action and not a different theory; the companion article states what it costs and what it buys.

Two conventions are warnings. The first: $\mu^{2}$ has the dimensions of a mass squared and is not a mass. The curvature at the minimum is $2\mu^{2}$, and the difference matters — the free Klein–Gordon article's $\nu_m^{2}$ is the coefficient of $-\tilde\Xi^{*}\tilde\Xi$ with a fixed sign, whereas here the sign is negative and the coefficient is not the mass. The second: $\varpi_{\mathrm{cpl}}$ in this normalisation is the coefficient of $(\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}})^{2}$, so the quartic term in the unitary chart is $\frac{\varpi_{\mathrm{cpl}}}{4}h^{4}$. A reader who imports $\frac{\varpi_{\mathrm{cpl}}}{4!}\xi_{\mathrm{pot}}^{4}$ from the scalar-field literature will find the self-couplings wrong by a factor of six.

## The Action in Element Form

The scalar block of the electroweak action, with the connection removed.

$$
S[\omicron_{\mathrm{hgs}},\omicron_{\mathrm{hgs}}^{\dagger}]=\int\mathrm{d}^{4}x\;\Bigl\{\partial_{\imath}\omicron_{\mathrm{hgs}}^{\dagger}\,\partial_{\imath}\omicron_{\mathrm{hgs}}-V(\omicron_{\mathrm{hgs}})\Bigr\}
=\int\mathrm{d}^{4}x\;\Bigl\{\tfrac12\partial_{\imath} r\,\partial_{\imath}r+\tfrac{r^{2}}{2}\partial_{\imath}\theta_A\partial_{\imath}\theta_A+\tfrac{\mu^{2}}{2}r^{2}-\tfrac{\varpi_{\mathrm{cpl}}}{4}r^{4}\Bigr\},
$$

where the second form uses the three angular coordinates of the four-sphere $r=\mathrm{const}$ and is written to show the structure and not to be varied in.

The same action in the unitary chart.

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{\tfrac12\partial_{\imath} h\,\partial_{\imath}h-\tfrac12 m_h^{2}h^{2}-\varpi_{\mathrm{cpl}} vh^{3}-\tfrac{\varpi_{\mathrm{cpl}}}{4}h^{4}\Bigr\},
\qquad m_h^{2}=2\varpi_{\mathrm{cpl}} v^{2}.
$$

The chart is the expansion about one point of the circle of minima, and the three terms after the mass term are the same $\varpi_{\mathrm{cpl}}$ read at third and fourth order.

It is real, term by term. The kinetic term is $\partial_{\imath}\omicron_{\mathrm{hgs}}^{\dagger}\partial_{\imath}\omicron_{\mathrm{hgs}}=\sum_A(\partial_{\imath}\xi_{\mathrm{pot},A})^{2}/2$, a sum of squares with a fixed sign. The mass term is $-\mu^{2}\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}=-\mu^{2}\sum_A\xi_{\mathrm{pot},A}^{2}/2$, real and negative. The quartic is $\varpi_{\mathrm{cpl}}(\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}})^{2}=\varpi_{\mathrm{cpl}}(\sum_A\xi_{\mathrm{pot},A}^{2})^{2}/4$, real and positive for $\varpi_{\mathrm{cpl}}>0$. The potential is therefore bounded below, and the bound is what makes a minimum exist at all.

**Why the sign of $\mu^{2}$ is the whole content.** With $\mu^{2}<0$ the potential has a single stationary point, at $\omicron_{\mathrm{hgs}}=0$, and it is a minimum; the four components are degenerate and each has mass $\sqrt{-\mu^{2}}$. With $\mu^{2}>0$ the origin is a maximum and the minimum is the three-sphere $\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}=v^{2}/2$. Nothing else in the action changes. The article's subject is the second case, and the first is named here only because the same display covers both.

What the display is not. It is not the electroweak action: three of the four derivatives are not there, and putting them back turns the three flat directions into the longitudinal polarisations of $W^{\pm}$ and $Z$. It is not a quantised action: there is no fixing the representative, no ghost and no loop. And it is not a claim that the scalar is elementary — the potential is a renormalisable truncation, and the corpus's effective-potential article treats what the truncation costs.

## The Variation

Varying the conjugate.

$$
\delta S=\int\mathrm{d}^{4}x\;\Bigl\{-\partial_{\imath}\partial_{\imath}\omicron_{\mathrm{hgs}}^{\dagger}\,\delta\omicron_{\mathrm{hgs}}-\frac{\partial V}{\partial\omicron_{\mathrm{hgs}}^{\dagger}}\delta\omicron_{\mathrm{hgs}}^{\dagger}\Bigr\}+\text{(boundary)},
$$

and holding $\delta\omicron_{\mathrm{hgs}}^{\dagger}$ arbitrary gives

$$
\Box\omicron_{\mathrm{hgs}}=-\frac{\partial V}{\partial\omicron_{\mathrm{hgs}}^{\dagger}}=\mu^{2}\omicron_{\mathrm{hgs}}-2\varpi_{\mathrm{cpl}}(\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}})\omicron_{\mathrm{hgs}} .
$$

The same equation in the radial variable. Since $\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}=r^{2}/2$ and $V(r)=-\frac{\mu^{2}}{2}r^{2}+\frac{\varpi_{\mathrm{cpl}}}{4}r^{4}$,

$$
\Box r=-V'(r)=\mu^{2}r-\varpi_{\mathrm{cpl}} r^{3},
$$

an equation in one real field. It is the anharmonic oscillator with the sign that makes $r=v$ a stable point, and it is the whole of the scalar's dynamics when the angular coordinates are frozen.

The same equation in the unitary chart.

$$
\Box h+m_h^{2}h+3\varpi_{\mathrm{cpl}} vh^{2}+\varpi_{\mathrm{cpl}} h^{3}=0 ,
$$

which is the radial equation expanded about $r=v+h$ with the linear term removed by the minimum condition. The three terms after the mass term are the nonlinearity, and their coefficients are fixed: there is no freedom left in them once $\varpi_{\mathrm{cpl}}$ and $v$ are chosen.

The boundary term, and why it is not an obstacle. The equation is second order in time, so the variation needs $\omicron_{\mathrm{hgs}}$ and its normal derivative fixed on the boundary — the same condition the Klein–Gordon article imposes, and the surface term vanishes under it. The scalar's variation is the simplest in the family for this reason: no parameter, no constraint, no identity.

**What the variation does not give.** It does not give the masses of the vectors, the Goldstone modes, or the count. Those come from the same action with the covariant derivative restored and the vacuum chosen, and they are the companion article's subject. What the variation gives here is the scalar's equation and, through it, the statement that the potential's derivatives are the couplings.

## The Constraints the Action Imposes: The Stationary Point Is Not a Constraint

The count. One real function in the radial chart, $r$ with $\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}=r^{2}/2$, one second-order equation, and a momentum that is the velocity. The map is invertible wherever $r\neq0$, so there is no primary constraint, no Gauss law and no constraint surface.

**The potential fixes a value and does not restrict the data.** The stationary points of $V(r)=-\tfrac{\mu^{2}}{2}r^{2}+\tfrac{\varpi_{\mathrm{cpl}}}{4}r^{4}$ are $r=0$ and $r^{2}=\mu^{2}/\varpi_{\mathrm{cpl}}$, and the sign of $\mu^{2}$ decides whether the second lies on the real branch. That is a statement about which configuration has stationary energy; a configuration away from it is a solution with a different energy, and the action admits it.

The two notions are routinely conflated and they are different objects. A constraint restricts initial data and cannot be removed by the equations; a stationary point selects a state and is left by moving away from it. Reading the second minimum as a constraint produces the claim that the action forbids the field from sitting at the origin, and it does not: it makes the origin unstable, which is a statement about the spectrum.

What the section does not claim. It does not claim the vacuum is undetermined: the potential selects it and the chart's constants fix its value. It claims that the selection is by energy and not by admissibility, and that distinction is what lets the structural consequence count the excitations around the minimum.

## The Structural Consequence: One Variable, One Number, Three Measurements

The claim. The potential is a function of $r$ alone, so the four real components of the doublet split into one radial field with a curved potential and three angular fields with a flat one. The radial field's mass is the curvature at the minimum, and the same curvature's third and fourth derivatives are its self-couplings. One number determines three measured quantities.

The split, in one line. $V$ depends on the four $\xi_{\mathrm{pot},A}$ through $\sum_A\xi_{\mathrm{pot},A}^{2}$ and on nothing else, so the symmetry group of the potential alone is $O(4)$, acting by rotations of the four-vector. A minimum at $r=v$ breaks $O(4)$ to $O(3)$, and the count of flat directions is $4-1=3$. Those three are the would-be Goldstone modes. Nothing about the connections entered this paragraph, and that is the point: the breaking is a property of the potential.

The curvature check. Expand $V$ about $r=v$:

$$
V(v+h)=V(v)+\tfrac12V''(v)h^{2}+\tfrac16V'''(v)h^{3}+\tfrac1{24}V''''(v)h^{4}+\cdots ,
$$

with $V'(v)=0$ by the minimum condition, $V''(v)=-\mu^{2}+3\varpi_{\mathrm{cpl}} v^{2}=2\varpi_{\mathrm{cpl}} v^{2}$, $V'''(v)=6\varpi_{\mathrm{cpl}} v$ and $V''''(v)=6\varpi_{\mathrm{cpl}}$. Comparing with the unitary display, $m_h^{2}=2\varpi_{\mathrm{cpl}} v^{2}$, the $h^{3}$ coefficient is $\frac16\cdot 6\varpi_{\mathrm{cpl}} v=\varpi_{\mathrm{cpl}} v$, and the $h^{4}$ coefficient is $\frac{1}{24}\cdot 6\varpi_{\mathrm{cpl}}=\frac{\varpi_{\mathrm{cpl}}}{4}$ — which is the display, term for term.

**The three measurements.** In the normalisation where the cubic vertex is $\frac{g_{hhh}}{6}h^{3}$ and the quartic is $\frac{g_{hhhh}}{24}h^{4}$,

$$
g_{hhh}=6\varpi_{\mathrm{cpl}} v=\frac{3m_h^{2}}{v},
\qquad
g_{hhhh}=6\varpi_{\mathrm{cpl}}=\frac{3m_h^{2}}{v^{2}},
\qquad
\frac{g_{hhhh}}{g_{hhh}}=\frac1v .
$$

With $m_h\simeq2.0067\times10^{-8}\ \mathrm{J}$ and $v\simeq3.9449\times10^{-8}\ \mathrm{J}$, $\varpi_{\mathrm{cpl}}=m_h^{2}/2v^{2}\simeq0.129$, $g_{hhh}\simeq3.06\times10^{-8}\ \mathrm{J}$ and $g_{hhhh}\simeq0.78$. The ratio is a number with the dimensions of an inverse energy and no free parameter: a reader who measures the triple coupling and the mass has tested the potential, not fitted it.

What the claim forbids. It forbids three things. A quartic coupling tuned independently of the mass, because the same $\varpi_{\mathrm{cpl}}$ is both. A cubic coupling treated as a separate parameter, because the expansion of a quartic potential has no other cubic term. And a "Higgs mass" read as $\sqrt{2}\mu$ with $\mu$ chosen freely and $\varpi_{\mathrm{cpl}}$ adjusted afterwards: the theory has $(\mu^{2},\varpi_{\mathrm{cpl}})$ and the observables are $(m_h,g_{hhh},g_{hhhh})$, three functions of two numbers, so one relation among the three is exact at this order.

The consequence the article does not resolve. The same display gives a vacuum energy. At the minimum $V(v)=-\varpi_{\mathrm{cpl}} v^{4}/4=-m_h^{2}v^{2}/8\simeq-2.5\times10^{45}\ \mathrm{J\,m^{-3}}$, and nothing in the action makes it zero. That number is more than fifty orders of magnitude above the observed vacuum energy density when both are written as an energy density, and the corpus has no mechanism that removes it. It is recorded here because it is a consequence of the potential and not an assumption about it; the cosmology articles state the problem and do not solve it either.

## The Noether Currents and the Sign of the Charge

The doublet's hypercharge current, and what becomes of it. The action is invariant under the global phase $\omicron_{\mathrm{hgs}}\mapsto e^{i\theta}\omicron_{\mathrm{hgs}}$, whose current is

$$
J_{Y,\imath}=i\bigl(\omicron_{\mathrm{hgs}}^{\dagger}\partial_{\imath}\omicron_{\mathrm{hgs}}-\partial_{\imath}\omicron_{\mathrm{hgs}}^{\dagger}\,\omicron_{\mathrm{hgs}}\bigr),
$$

conserved by the equation of motion. In the unitary chart the doublet has one real non-zero component, and $J_{Y,\imath}$ vanishes identically there: $\omicron_{\mathrm{hgs}}^{\dagger}\partial_{\imath}\omicron_{\mathrm{hgs}}$ is real when $\omicron_{\mathrm{hgs}}$ is real, so the two terms cancel. **The physical Higgs field carries no hypercharge.**

Where the current went. Into the three angular directions. A general chart writes $\omicron_{\mathrm{hgs}}=\frac{1}{\sqrt2}\binom{0}{r}e^{i\theta_{a}\tau_{a}/2}$-style, and the phase directions carry $J_{Y,\imath}$ in proportion to their gradients. Those directions are the would-be Goldstones, and the connection that eats them inherits the coupling: the statement that the $Z$ has a hypercharge current is the same statement as the statement that the eaten Goldstones carried one. This is the mechanism read from the current side, and it agrees with the companion's count, which reads it from the degrees of freedom.

The count of currents, from the potential alone. The potential's symmetry is $O(4)$; the minimum breaks it to $O(3)$; the number of generators that do not annihilate the vacuum is $6-3=3$. So three currents are broken and one linear combination of the four electroweak generators survives — the electromagnetic one, whose charge is $Q=T_3+Y/2$, with the sign of the electron's charge fixed by the hypercharge assignment and not by anything in this article. The count of currents and the count of Goldstones are the same number for the same reason.

**The stress, and the sign of the energy.** With the flat directions frozen,

$$
T_{\imath\jmath}=\partial_{\imath} h\,\partial_{\jmath} h-\delta_{\imath\jmath}\Bigl(\tfrac12\partial h^{2}-V(h)\Bigr),
\qquad
T_{00}=\tfrac12\dot h^{2}+\tfrac12(\nabla h)^{2}+V(h)-V(v),
$$

where the constant is subtracted so that the energy of the vacuum is zero by definition and the potential's depth is stated separately. Read without the subtraction, $T_{00}$ carries the constant $V(v)$ above. The kinetic and gradient terms are sums of squares; the potential's contribution is bounded below by its minimum; so the energy is bounded below and the sign is right. The indefinite-sign cross terms that appear when the Goldstones are kept are removed by the unitary chart, as the companion article states.

## What the Principle Adds and What It Relabels

Adds. One parameter, $\varpi_{\mathrm{cpl}}$, for the whole scalar sector, with the mass as its curvature and the two self-couplings as its third and fourth derivatives. The relation $g_{hhhh}=g_{hhh}/v$. The vacuum energy as a number the potential produces. And the split into one curved and three flat directions, which is the breaking stated without the connections.

Relabels. The corpus's Higgs-mechanism statements — the doublet, the potential, the circle of minima, the count, the masses — are all recoverable from this action, and it adds no number to them except $\varpi_{\mathrm{cpl}}$, which they already contain in the form $m_h^{2}=2\varpi_{\mathrm{cpl}} v^{2}$.

**What it does not reach, and this family does not either.** The loop-corrected potential, where the curvature at the minimum is not $2\varpi_{\mathrm{cpl}} v^{2}$ but that number plus a correction the corpus's effective-potential article computes in outline. The running of $\varpi_{\mathrm{cpl}}$ and the two bounds that follow from it — triviality at the ultraviolet end and stability at the infrared end — which the corpus's triviality article states as bounds and not as a computation inside this action. The hierarchy problem, which is the statement that the correction to $\mu^{2}$ is quadratically sensitive to the scale at which the truncation is imposed. And the value of $m_h$ itself, which the corpus takes from experiment.

The honest sentence. The corpus can write this action exactly, vary it exactly, and read three couplings from one number exactly. It cannot say why $\varpi_{\mathrm{cpl}}$ has the value it has, and it cannot compute the correction to that value. The gap is the same gap the electroweak action article names: quantisation, and the renormalisation that comes with it.

## Summary

The scalar action is the Klein–Gordon action for a complex doublet with $V=-\mu^{2}\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}+\varpi_{\mathrm{cpl}}(\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}})^{2}$, whose potential depends on one variable and whose minimum is a three-sphere. The variation gives $\Box\omicron_{\mathrm{hgs}}=\mu^{2}\omicron_{\mathrm{hgs}}-2\varpi_{\mathrm{cpl}}(\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}})\omicron_{\mathrm{hgs}}$, the radial anharmonic equation and, in the unitary chart, $\Box h+m_h^{2}h+3\varpi_{\mathrm{cpl}} vh^{2}+\varpi_{\mathrm{cpl}} h^{3}=0$. The curvature at the minimum is $m_h^{2}=2\varpi_{\mathrm{cpl}} v^{2}$, the third and fourth derivatives give $g_{hhh}=3m_h^{2}/v$ and $g_{hhhh}=3m_h^{2}/v^{2}$, so one number is measured three times. Three directions are flat, they carry the hypercharge current, and the vectors that eat them inherit it. Nothing is quantised, and the value of $\varpi_{\mathrm{cpl}}$ is not derived.

$$
S=\int\mathrm{d}^{4}x\;\Bigl\{\partial_{\imath}\omicron_{\mathrm{hgs}}^{\dagger}\partial_{\imath}\omicron_{\mathrm{hgs}}+\mu^{2}\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}-\varpi_{\mathrm{cpl}}(\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}})^{2}\Bigr\},
\qquad
m_h^{2}=2\varpi_{\mathrm{cpl}} v^{2},\quad v^{2}=\frac{\mu^{2}}{\varpi_{\mathrm{cpl}}}.
$$

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\omicron_{\mathrm{hgs}}$ | Complex doublet, four real components $\xi_{\mathrm{pot},A}$ |
| $\mu^{2},\ \varpi_{\mathrm{cpl}}$ | Mass-squared parameter and quartic coupling, both positive |
| $v=\sqrt{\mu^{2}/\varpi_{\mathrm{cpl}}}$ | Magnitude of the vacuum expectation value, $\simeq3.9449\times10^{-8}\ \mathrm{J}$ |
| $r=\sqrt{2\omicron_{\mathrm{hgs}}^{\dagger}\omicron_{\mathrm{hgs}}}$ | Radial field, the potential's only argument |
| $h=r-v$ | Physical scalar fluctuation in the unitary chart |
| $m_h^{2}=2\varpi_{\mathrm{cpl}} v^{2}$ | Curvature of the potential at the minimum |
| $g_{hhh}=3m_h^{2}/v$ | Cubic self-coupling, $=6\varpi_{\mathrm{cpl}} v$ |
| $g_{hhhh}=3m_h^{2}/v^{2}$ | Quartic self-coupling, $=6\varpi_{\mathrm{cpl}}$ |
| $J_{Y,\imath}$ | Hypercharge current of the doublet, vanishing on the radial direction |
| $V(v)=-m_h^{2}v^{2}/8$ | Depth of the potential at the minimum |

## Further Reading

- *The Lagrangian and the Electroweak Theory*, for the same scalar inside the full gauge action, its two phases and the vector masses.
- *Electroweak Symmetry Breaking: the Doublet, the Potential and the Gauge-Boson Masses*, for the mass matrix, the count and the couplings read from the masses rather than from the potential's derivatives.
- *The Higgs Mechanism in Biquaternionic Form*, for the central scalar and the covariant derivative in the biquaternion algebra.
- *The Effective Potential and the Coleman–Weinberg Mechanism in Biquaternionic Form*, for the one-loop correction this article does not compute.
- *The Landau Pole, Triviality and Vacuum Stability*, for the two bounds that follow from the running of $\varpi_{\mathrm{cpl}}$.
- *The Lagrangian and the Interacting Scalar Field*, for the same quartic term without the negative mass squared, where the symmetry is unbroken.
- *The Lagrangian and the Goldstone Effective Action*, for the three flat directions treated as fields of their own.
- Chris Quigg, *Gauge Theories of the Strong, Weak and Electromagnetic Interactions*, for the classical potential and the self-couplings.
