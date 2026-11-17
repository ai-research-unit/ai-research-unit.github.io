# __The Massless Fluid: The One Wave Where Both Charts Fail__

## Introduction

**This article separates two statements about mass that are easy to run together, and it keeps them apart throughout.** The first is about a fluid that exists. The second is about what is left when the fluid's own variables have gone to zero or to infinity. **They are not the same statement, and the difference is not a matter of emphasis: in the first the fluid equations hold everywhere, and in the second there is no fluid at all.**

**At every positive mass the fluid is fully defined.** The four-factor word exists because every value has a nonzero norm; the density is the field's own scale, $\rho_{\mathrm{num}}=\varrho^{2}$; the four-velocity is invertible at a mode and departs from the unit by $2Q_{\mathrm{qnt}}/m$ otherwise; the quantum potential, the quantum stress and the acceleration are finite at that $m$; and the first-order symbol is invertible. **Nothing in that regime is a limit and nothing in it is singular**, and no section of this article changes any of it.

**At zero mass, on the label cone, the fluid description stops.** The word has no value, the logarithm does not exist, the generator diverges, the inverse does not exist, and the density, the quantum potential and the stress are either zero or divergent there. **What remains is a direction, an intensity and the sign of the energy**: a null current, not a fluid. **Calling that object a fluid at zero density is a manner of speaking, and the cone is not an inhabited state of the fluid.**

**Between the two regimes the passage is a limit, and the limit can be counted.** Two families are involved and they approach two different sets: a four-momentum, whose invariant mass $m^{2}c^{2}$ vanishes as its speed reaches $c$, and a field, whose density does not move while its quantum layer diverges as $1/m$. **Both counts are made of values of a fluid that exists at that mass**, which is what distinguishes this article's subject from a fluid on the cone.

**What is proved here** is that at $k_m=0$ the label's null cone and the pole set are one level set, and that the two charts' failures are one object because the kernel of a null symbol is a right ideal every element of which has zero norm. **The containment is the theorem; the approach is its physical reading; the absence of a fluid at the cone is its consequence.**

## Conventions and Notation

**The element and its two norms.** $\tilde Q=Q_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with $Q_\mu\in\mathbb{C}$, the product fixed by $\vec e_x\vec e_y=\vec e_z$ cyclically and $\vec e_k^{2}=-e_t$, with $i$ central. $N(\tilde Q)=\sum_\mu Q_\mu^{2}$ is the **quaternionic norm**, complex and multiplicative, vanishing exactly on the zero divisors; $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ is the **Euclidean size**, real and definite. **The modulus is the invariant and the size is the frame-dependent number** [The Two Scales of the Field](../articles_physics/the-two-scales-of-the-field-the-proper-density-and-the-euclidean-size.html).

**The label.** The corpus writes a four-vector with an imaginary time coefficient, $\tilde K_\Phi=ik_t'e_t+\vec k_\Phi$, so that

$$
N(\tilde K_\Phi)=-k_t'^{2}+\lvert\vec k_\Phi\rvert^{2}\in\mathbb{R},
$$

the mass shell being $N(\tilde K_\Phi)=-k_m^{2}$, that is $k_t'^{2}=\lvert\vec k_\Phi\rvert^{2}+k_m^{2}$ [Four-Vectors and the Interval](four-vectors-and-the-interval.html). **$k_m$ is the mass in wave-number units**, the block's $mc/\hbar$. The **label cone** is $N(\tilde K_\Phi)=0$, that is $k_t'=\lvert\vec k_\Phi\rvert$.

**The two symbols.** The scalar rung's operator $\Box_\Phi-k_m^{2}$ has the scalar symbol

$$
\mathcal N(\tilde K_\Phi)=k_t'^{2}-\lvert\vec k_\Phi\rvert^{2}-k_m^{2},
$$

which is the single number the propagator inverts, and which equals $-N(\tilde K_\Phi)-k_m^{2}$ by the definition of the label's norm. **The two glyphs are visually close and are different objects**: $N$ is the quaternionic norm of an element, script $\mathcal N$ is the symbol of an operator, and the sign between them is a minus. A reader who drops the script from $\mathcal N$ sees the self-reference $\mathcal N=-N-k_m^{2}$ where there is none, so the definition is given above in components and the relation to $N$ second.

The first-order rung has the algebra-valued symbol $\Sigma(\tilde K_\Phi)$, an element of the algebra to be left-multiplied. **For the massless case $\Sigma(\tilde K_\Phi)=\tilde K_\Phi$ and the equation is the Weyl one.** For the massive case this article evaluates nothing: the only property used is that the symbol is invertible wherever the label is off the pole set, and **the rung table of §*What Each Rung Loses* records that property and no formula**. Stating the massive symbol in closed form would require committing to a chiral convention that the corner does not test, and the corner is the only case examined here. **The distinction matters at the corner and is the subject of §*What Each Rung Loses*.**

**The null label and the projector.** The only spatial axis this article uses is $\vec u$, a unit real pure quaternion, and it is **the direction of the null momentum and not a choice of notation**: for the physical family $\vec u=-\vec u_p$, with $\vec u_p=\vec k_\Phi/\lvert\vec k_\Phi\rvert$. A null label along it is $\tilde K_\Phi=k\bigl(ie_t+\vec u\bigr)$ with $k\neq0$ real, whose norm is $N=-k^{2}+k^{2}=0$. The projector $\tilde\Pi=\tfrac12\bigl(e_t+i\vec u\bigr)$ and $\tilde\Pi_{-}=\tfrac12\bigl(e_t-i\vec u\bigr)$. Both are **idempotent**, $\tilde\Pi^{2}=\tilde\Pi$, both have $N(\tilde\Pi)=0$, and both have Euclidean size $\tfrac12$. **They are the two helicities of a null direction, and they are the simplest nonzero elements of the value cone.**

**Why the axis is named and not written as a basis unit.** Every identity below is built from $e_t$, from $\vec u$ and from the two relations $\vec u^{2}=-e_t$ and $e_t\vec u=\vec u e_t=\vec u$, which hold for **every** unit real $\vec u$. Under the automorphism $u\mapsto sus^{-1}$ for a unit versor $s$ each identity therefore returns itself with $\vec u$ replaced, so none of them privileges a spatial direction. **A display that wrote the same formulas with an unmarked basis unit would state a fact about the page and not about the algebra**, and the test applied here is the one in [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html) §*The Test Is Covariance*. The direction is the momentum's, it is carried by an object of the sentence, and the reader can rotate it.

**Units and conventions.** All statements are algebraic and hold at one event or at one label; none is an equation of motion. **No claim is made that a massless field of Nature is a null wave**; the conditional is examined, not the physics.

## Two Charts, Two Domains

**The fluid chart is a chart on values.** Given $\tilde\Xi$, it extracts $\varrho$, $\theta_{\mathrm{pha}}$, $\theta_{\mathrm{rpd}}$ and the two axes. The extraction is total off the value cone and undefined on it, because the word needs $\varrho^{2}=\lvert N(\tilde\Xi)\rvert$ and the norm vanishes there.

**The Fourier chart is a chart on labels.** Given a mode, it names a point $\tilde K_\Phi$ and writes the mode's weight as the reciprocal of the symbol at that point. The extraction is total off the pole set and undefined on it, because the reciprocal needs $\mathcal N(\tilde K_\Phi)\neq0$ and the symbol vanishes there.

**Nothing in either chart refers to the other's variable.** One is a condition on the field at an event, the other a condition on a label; the first is two real equations on eight real coordinates, the second is one real equation on four. **The two failures differ in codimension before they differ in anything else.**

| | fluid chart | Fourier chart |
| --- | --- | --- |
| variable | the value $\tilde\Xi(X)$ | the label $\tilde K_\Phi$ |
| fails when | $N(\tilde\Xi)=0$ | the symbol has no inverse |
| the set | the value cone, real codimension two | the pole set, real codimension one |
| what is lost | the word: $\varrho$, the phase, the velocity | the weight: the reciprocal symbol |
| what survives | the pair $\bigl(\rho_{\mathrm{num}},\langle\tilde\Xi\rangle_{*}\bigr)$ | a least-squares inverse, and the homogeneous solutions |

**The two "what survives" entries are the useful ones.** A failure of a chart is not a failure of the object: the field keeps its two numbers, and the operator keeps its kernel. **The corner is the place where those two survivals are the same set.**

## One Parameter Separates Them

**Both failures are level sets of one function, read in two spaces.** The label's norm is real, so its level sets are genuine hypersurfaces, and the two that matter are

$$
\underbrace{N(\tilde K_\Phi)=0}_{\text{label cone}}\qquad\text{and}\qquad \underbrace{N(\tilde K_\Phi)=-k_m^{2}}_{\text{pole set}} .
$$

**The mass is their spacing, and nothing else is.** For $k_m\neq0$ no label satisfies both equations, since the two require $N(\tilde K_\Phi)$ to be two different numbers; for $k_m=0$ the two level sets are one set. **This is the whole content of the parameter**: not that the mass term shifts the dispersion, which is obvious, but that it is the only quantity in the block whose vanishing makes the two failures coincide in the label space.

**Checked at four labels.** The third column is the scalar symbol, the fourth says whether the propagator exists:

| $k_t'$ | $\lvert\vec k_\Phi\rvert$ | $k_m$ | $N(\tilde K_\Phi)$ | $\mathcal N$ | propagator |
| --- | --- | --- | --- | --- | --- |
| $1$ | $0$ | $1$ | $-1$ | $0$ | pole, on shell |
| $2$ | $\sqrt3$ | $1$ | $-1$ | $0$ | pole, on shell |
| $1$ | $1$ | $0$ | $0$ | $0$ | no inverse |
| $1$ | $1$ | $0.5$ | $0$ | $-0.25$ | exists |

**The last row is the point of the table.** A label on the cone with a nonzero mass has an invertible symbol: the label chart does not fail there at all. **The cone is where the label chart fails only when the mass is zero**, and the failure of the value chart has nothing to do with the label, so the coincidence of the two is a property of one parameter value and not of the algebra.

## The Two Families That Approach Two Different Sets

**"Massless" names two different things in this block, and they are kept apart here.** The first is a four-momentum whose invariant mass has gone to zero. The second is a field whose equation has lost its mass term. **They approach different sets, they carry different fluid data, and only the first has a density that vanishes.**

| the family | family one: the four-momentum | family two: the field |
| --- | --- | --- |
| what is varied | $m$, at fixed energy $E$ | $m$, at fixed density and fixed shape |
| the element | $\tilde P_\Phi$, with $\varrho=mc$ | $\tilde\Xi$, with $\varrho$ the field's own scale |
| the set it approaches | the label cone, since $N(\tilde P_\Phi)=-m^{2}c^{2}\to0$ | none: $N(\tilde\Xi)$ does not contain $m$ |
| $\rho_{\mathrm{num}}$ | $m^{2}c^{2}\to0$ | fixed by the field |
| $\gamma=E/(mc^{2})$ | $\to\infty$ | $\to\infty$ |
| $Q_{\mathrm{qnt}}$ | $\propto1/m$ | $\propto1/m$ |
| what the fluid loses | the rest frame | the quantum layer |

**The fourth row is the correction the reader is owed.** The field does not thin as its mass vanishes: $\rho_{\mathrm{num}}=\varrho^{2}$ is the field's own scale, and the mass is a parameter of the equation and not of the value. **A fixed field keeps its density at every mass**, and what the vanishing mass destroys is the quantum layer, not the density.

### The Momentum's Approach, and the Frame That Pays

**Family one at fixed energy, with $c=1$.** Every row is a momentum at the mass it names, and no row is a limit:

| $m$ | $\lvert N(\tilde P_\Phi)\rvert=m^{2}$ | $1/\lvert N\rvert$ | $\gamma=E/m$ | $\lvert\vec v\rvert/c$ |
| --- | --- | --- | --- | --- |
| $1$ | $1$ | $1$ | $1$ | $0$ |
| $0.3$ | $0.09$ | $11.111$ | $3.333$ | $0.953939$ |
| $0.1$ | $0.01$ | $100$ | $10$ | $0.994987$ |
| $0.01$ | $10^{-4}$ | $10^{4}$ | $100$ | $0.999950$ |

**The columns are one fact read four times**: the invariant mass squared, its reciprocal, the frame factor that pays for it, and the speed that follows. **The density of this family is not a number of anything**: $\lvert N(\tilde P_\Phi)\rvert=m^{2}c^{2}$ is the invariant mass, and its vanishing is the statement that there is no rest frame, not that a medium has emptied.

**The speed rises from below and the rise is a square root.** At fixed energy, $\lvert\vec v\rvert/c=\sqrt{1-m^{2}c^{4}/E^{2}}$, which is $0$ at $m=E/c^{2}$, $0.995$ at a tenth of it and $0.99995$ at a hundredth. **The last decade of mass is the only one in which the speed is measurably below $c$**, so the corner is not a place a massive momentum visits; it is a limit it recedes towards.

### The Field's Approach, and the Quantum Layer

**Family two holds the field fixed and varies the mass, and the mass appears in exactly one place: as $1/m$ in the quantum potential.** Since $\Box_\Phi\varrho/\varrho$ is a functional of the shape alone,

$$
Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Box_\Phi\varrho}{\varrho}\ \propto\ \frac{1}{m},
\qquad
p_{\mathrm{qnt}}=\rho_{\mathrm{num}}Q_{\mathrm{qnt}}\ \propto\ \frac{1}{m},
$$

and the quantum stress $\sigma^{Q}_{ij}$ carries the same factor. **So the whole quantum layer of a fixed field diverges as the mass vanishes.** Checked on the two-mode superposition $\rho_{\mathrm{num}}=1+\eta^{2}+2\eta\cos(\Delta k\,x)$ with $\eta=0.2$, $\Delta k=1$ and $\hbar=1$:

| $m$ | $Q_{\mathrm{qnt}}$ | $mQ_{\mathrm{qnt}}$ |
| --- | --- | --- |
| $1$ | $-0.010417$ | $-0.010417$ |
| $0.5$ | $-0.020833$ | $-0.010417$ |
| $0.25$ | $-0.041667$ | $-0.010417$ |

**The third column is constant, and that constancy is the $1/m$ law.** Halving the mass doubles the potential, and no refinement of the arithmetic changes the exponent.

**The force is the exception, and it is the whole of the physics.** The acceleration law is $\mathrm{d}\vec p/\mathrm{d}t=-\gamma^{-1}\nabla Q_{\mathrm{qnt}}$, and $\gamma^{-1}=m/E$ cancels the $1/m$:

$$
\frac{\mathrm{d}\vec p}{\mathrm{d}t}=\frac{\hbar^{2}}{2E}\,\nabla\Bigl(\frac{\Box_\Phi\varrho}{\varrho}\Bigr),
$$

**which contains no mass at all.** At fixed energy the rate of momentum transfer is the same at every mass: **the Bohm potential diverges and the Bohm force does not.** A reader who quotes "$Q_{\mathrm{qnt}}$ diverges" as the statement that the guidance fails near the wall has quoted the potential and not the force.

**The velocity defect is the fastest divergence in the block.** Since $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}-2Q_{\mathrm{qnt}}/m$ and $Q_{\mathrm{qnt}}\propto1/m$, the defect grows as $1/m^{2}$: $-0.021$ at $m=1$, $-0.083$ at $m=0.5$ and $-0.333$ at $m=0.25$, a factor four for each halving. **So the velocity is invertible only at a mode, and its departure from the unit is the quantity that fails first.**

### What the Approach Does, Said in Fluid Words

- **The fluid does not thin.** The density is the field's own scale, and the mass does not enter it.
- **The frame degrades.** The rest frame exists at every $m>0$, costs a factor $\gamma\propto1/m$, and has no value at $m=0$.
- **The quantum layer goes first.** $Q_{\mathrm{qnt}}$, $p_{\mathrm{qnt}}$ and $\sigma^{Q}_{ij}$ diverge as $1/m$: the Bohm reading needs a mass, and a massless equation supplies none.
- **The guidance is last and it does not go.** The momentum rate is mass-free, so a massless field still pushes.
- **The momentum's frame goes, and nothing else about it does.** The direction, the intensity and the sign are untouched.

## At Zero Mass the Fluid Description Stops

**Set $m=0$ and every quantity above stops being a value of a fluid.** Each item, and its reason:

| what stops | why |
| --- | --- |
| the density as a fluid density | $\rho_{\mathrm{num}}=0$ at every event, and $\gamma$ has no value, so there is no rest volume to divide by |
| $Q_{\mathrm{qnt}}$, $p_{\mathrm{qnt}}$, $\sigma^{Q}_{ij}$ | $1/m$ against a fixed field |
| $\gamma$, and with it the rest frame | $E/(mc^{2})$ at $m=0$ |
| the three-velocity | its limit is $c$, and there is no frame in which to measure it |
| the four-factor word | $N=0$ |
| the logarithm and the generator | $\ln\varrho\to-\infty$ against a divergent rapidity |
| the inverse | $\tilde Q^{\natural}/N$ at $N=0$ |

**The first row decides the question, and it is not a limit.** At $m=0$ the amplitude is not driven to zero by a path: it is forced into the kernel of a null symbol, and the kernel is the right ideal $\tilde\Pi\mathbb{B}$, every element of which has $N=0$. **The field is null because the equation says so at $m=0$, not because a family of fields shrank.**

**What survives is three data and none of them is a density**: a unit direction $\vec u$, an intensity $\lvert\varkappa\rvert^{2}$, and the sign of the energy. That is the data of a current,

$$
j_\mu=\frac{c}{2}\lvert\varkappa\rvert^{2}\bigl(1,\vec u\bigr),
$$

**so the object at the corner is a null current, and the word "fluid" is a shorthand that stops being true at $m=0$.** A current has a direction and a flux and no state; a fluid has a state, a stress and a quantum potential, and none of those exists here.

$\gamma$ and $\lvert\vec v\rvert$ do not belong among the quantities of the corner. Both are family one's, they are limits and not values, and the table carries neither. **That difference is the whole difference between a fluid approaching a wall and the wall itself.**

**This is neither a failure of the reading nor a defect of the algebra.** $\rho_{\mathrm{num}}$, $Q_{\mathrm{qnt}}$ and $\sigma^{Q}_{ij}$ are functions of $\varrho$ and of $m$, and at the corner $\varrho=0$ and $m=0$: a quantity whose definition divides by either has no value there. **No change of chart produces a fluid where the fluid's own variables have gone**, which is why the corner is examined here as the end of a limit and not as a state.

## The Label Chart at Zero Mass

**At $k_m=0$ and on the cone, the first-order symbol is a null element, and left multiplication by a null element is not invertible in a measured way.** With $\tilde K_\Phi=ik e_t+k\vec u$ for a null label of frequency $k$,

$$
N(\tilde K_\Phi)=0,\qquad \tilde K_\Phi\neq0,\qquad \operatorname{rank}L_{\tilde K_\Phi}=4\ \text{of}\ 8,
$$

where $L_{\tilde Q}$ is left multiplication by $\tilde Q$ as a real linear map on the eight real coordinates. **Half the space is annihilated and half is not**, and that is the precise sense in which a null symbol fails: not by vanishing, but by halving.

**The kernel is a right ideal and it is named by an idempotent.** For the label $\tilde K_\Phi=k(ie_t+\vec u)$,

$$
\tilde K_\Phi\tilde\Pi=0,\qquad \tilde K_\Phi\tilde\Pi_{-}=\tilde K_\Phi\neq0,
$$

so the kernel is $\tilde\Pi\,\mathbb{B}$, the set of right multiples of $\tilde\Pi$: four real parameters, two complex. **The wrong chirality is not annihilated at all — it is passed through unchanged**, which is a stronger statement than "not in the kernel": the mirror projector leaves the symbol's action untouched. **The mirror label annihilates the mirror idempotent and nothing else**, which is the algebraic form of the statement that helicity is locked to momentum [Spin-Velocity Locking on the Degenerate Sector](spin-velocity-locking-on-the-degenerate-sector.html).

**Checked.** At $k=1$ and $k=2.7$ the singular values of $L_{\tilde K_\Phi}$ are $\{2,2,2,2,0,0,0,0\}$ and $\{5.4,5.4,5.4,5.4,0,0,0,0\}$; the span of the four generators $\tilde\Pi\vec e_\mu$ has rank four and is annihilated to zero; and the mirror product $\tilde K_\Phi\tilde\Pi_{-}$ equals $\tilde K_\Phi$ to $0$ exactly. *Proof and residuals: §*Appendix: The Algebra*.*

## The Inverse It Keeps

**A rank drop of four is not a catastrophe, and the label chart's residue is a number.** The singular values of $L_{\tilde K_\Phi}$ are $2\lvert k\rvert$ four times and zero four times, so the least-squares inverse exists, has rank four, and its norm is

$$
\bigl\lVert L_{\tilde K_\Phi}^{+}\bigr\rVert=\frac{1}{2\lvert k\rvert} .
$$

**The least-squares problem therefore has a solution for every right-hand side**, unique modulo the kernel and bounded by $\lVert W\rVert/(2\lvert k\rvert)$. **The nonzero singular values are $2\lvert k\rvert$ and not $\lvert k\rvert$**, so the factor of two is part of the algebra and not a normalisation: the row at $k=0.5$ is the check, its singular values being $1$ and its bound $1$, twice the frequency. Checked at four frequencies:

| $k$ | nonzero singular values | $\lVert L^{+}\rVert$ | $1/(2k)$ |
| --- | --- | --- | --- |
| $0.5$ | $1,1,1,1$ | $1.000000$ | $1.000000$ |
| $1$ | $2,2,2,2$ | $0.500000$ | $0.500000$ |
| $2.7$ | $5.4,5.4,5.4,5.4$ | $0.185185$ | $0.185185$ |
| $10$ | $20,20,20,20$ | $0.050000$ | $0.050000$ |

**The measure of the failure is the measure of the survival.** The four dimensions the symbol loses are the four its least-squares inverse leaves undetermined, and the undetermined part is the wave — **which is the exact sense of the slogan**: the least-squares inverse determines everything except the kernel, and the kernel is what the corner leaves free. **So the label chart at the corner does not fail as the scalar chart fails**: it fails like a projection, losing one half and inverting the other half with a bound.

**The contrast is itself a number.** The scalar propagator's factor $1/\mathcal N$ has no bound as the pole is approached, which is the usual divergence; the first-order least-squares inverse is bounded at every $k\neq0$ and diverges only as $k\to0$. **Two failures, two behaviours, and the difference is again the rank** — this time read as a condition number rather than as a dimension count.

## What Each Rung Loses

**The rank lost at the corner is the rung's, and the earlier article's sentence conflates two rungs.** At the first-order rung the symbol is an algebra element and its failure is a rank drop of four. At the scalar rung the symbol is one number $\mathcal N$, and its failure at the corner is total. **The "rank" column below is the rank of a multiplication in both rows, but not of the same multiplication**: in the scalar row it is the rank of multiplication by the central element $\mathcal N(\tilde K_\Phi)$, in the first-order row that of left multiplication by the symbol itself.

| rung | symbol | label on the cone, $k_m\neq0$ | label on the cone, $k_m=0$ |
| --- | --- | --- | --- |
| scalar, Klein–Gordon | the number $\mathcal N(\tilde K_\Phi)$ | $=-k_m^{2}$, nonzero, so invertible | $=0$, the operator is lost |
| first order | the map $\Sigma(\tilde K_\Phi)$ | the pole is off the cone, so invertible | it becomes $\tilde K_\Phi$, null, real rank $4$ of $8$ |

**Spelled out in operators**: the scalar row's rank is that of $\mathcal N(\tilde K_\Phi)L_{e_t}$, which is $8$ when $\mathcal N\neq0$ and $0$ when $\mathcal N=0$; the first-order row's is that of $L_{\tilde K_\Phi}$ itself, which drops from $8$ to $4$. **Both rows are about left multiplication, which is why they can be compared at all**, and the comparison is the point: one symbol loses all eight dimensions and the other loses half.

**The scalar rung loses the operator, the first-order rung loses half of it.** Both failures are "no inverse", and they are not equally severe: a scalar symbol that vanishes leaves no inverse and no kernel worth the name, while a null symbol leaves a four-dimensional kernel which is exactly the set of solutions.

**That asymmetry is why the corner is inhabited.** If both rungs lost everything, the coincidence of the two cones would be a coincidence of two empty sets. **The first-order rung loses half, and the half it keeps is the half the value chart refuses.**

## The Value Chart at Zero Mass

**Take the amplitude the label chart keeps.** With $\varkappa$ a complex constant and $\theta=-k_t't'+\vec k_\Phi\cdot\vec X$,

$$
\tilde\Xi(X)=\varkappa\,\tilde\Pi\,e^{i\theta},\qquad \tilde K_\Phi\,\tilde\Pi=0,\qquad N(\tilde K_\Phi)=0,
$$

which solves the massless first-order equation exactly, because the symbol annihilates the amplitude.

**The field is a zero divisor at every event.** $N$ is multiplicative, $N(\tilde\Pi)=0$, so

$$
N\bigl(\tilde\Xi(X)\bigr)=\varkappa^{2}e^{2i\theta}N(\tilde\Pi)=0\quad\text{for every }X ,
$$

and the polar word fails at every event of the wave, not at a set of events and not on a hypersurface: **the whole world line is off the chart's domain.** The label chart fails at one point of label space and the value chart fails everywhere in spacetime, which is what "the two charts fail on one wave" has to mean if it is to mean anything.

**The field is not small and it is not nothing.** The Euclidean size is constant and nonzero:

$$
\langle\tilde\Xi\rangle_{*}=\lvert\varkappa\rvert^{2}\langle\tilde\Pi\rangle_{*}=\tfrac12\lvert\varkappa\rvert^{2},
\qquad
\rho_{\mathrm{num}}=\lvert N(\tilde\Xi)\rvert=0 ,
\qquad
j^{0}=c\,\langle\tilde\Xi\rangle_{*}=\tfrac{c}{2}\lvert\varkappa\rvert^{2}\neq0 .
$$

**A current with no density.** The time component is finite while the proper density vanishes, so the product $\gamma\rho_{\mathrm{num}}c$ is finite with $\gamma$ without a value and $\rho_{\mathrm{num}}$ zero: **the wave carries a current and has no rest frame, which is the same statement twice.** The pair $(\rho_{\mathrm{num}},\langle\tilde\Xi\rangle_{*})$ is continuous at the corner, exactly as the first article proved, and the corner is the case $\rho_{\mathrm{num}}\to0$ at fixed size.

**The vanishing density is a counting statement and not a cancellation.** A density is quadratic in the field, so the only labels it can carry are differences of the labels the amplitude carries: two modes at $k_1$ and $k_2$ beat at $k_2-k_1$ and at nothing else. **The corner has one label, so it has no pair and no difference**, and $\rho_{\mathrm{num}}=0$ there is the absence of the second label rather than a sum of two terms that happen to cancel. **Hence the wave has no interference structure at all**, which is why every quantity in this section is constant along it, and why no refinement of the arithmetic can recover a density from it.

| quantity | the null wave |
| --- | --- |
| $N(\tilde\Xi(X))$ | $0$ at every event, forced by the kernel |
| $\langle\tilde\Xi\rangle_{*}$ | $\tfrac12\lvert\varkappa\rvert^{2}$, constant |
| $\rho_{\mathrm{num}}$ | $0$ |
| $j^{0}$ | $\tfrac{c}{2}\lvert\varkappa\rvert^{2}$ |
| $\gamma$ | no value |
| $\lvert\vec v\rvert$ | no value |

**The first four rows are values and the last two are not, and the split is the whole table.** The pair $(\rho_{\mathrm{num}},\langle\tilde\Xi\rangle_{*})$ is defined at the corner, which is why the corner is describable at all; every ratio that divides by $\varrho$ is not, which is why the corner is not a state of the fluid. **The two rows that are not values are family one's, and neither is a value.**

**The wave does not move its own state, up to the overall phase.** The amplitude is a fixed projector, so every value of the field is that projector up to a phase and a scale: **the only thing that changes along the world line is the phase $e^{i\theta}$**, and a change of phase changes nothing that this article measures, since $N$ and $\langle\cdot\rangle_{*}$ are both invariant under it. That is the algebraic content of a mode with no rest frame.

## One Factorisation, Two Failures

**Here is the theorem the corner rests on, and it is one line.** $N$ is multiplicative, so for every $\tilde B$,

$$
N\bigl(\tilde\Pi\tilde B\bigr)=N(\tilde\Pi)\,N(\tilde B)=0 .
$$

**The kernel of the null symbol is contained in the value cone.** That is the sentence. The set the label chart keeps is a subset of the set the value chart refuses, so the two failures are not two accidents that happen to coincide: **the surviving amplitudes are the failing values, and the same idempotent names both.**

**Checked on two thousand random right multiples.** The largest $\lvert N(\tilde\Pi\tilde B)\rvert$ is $9.2\times10^{-16}$, which is the arithmetic's zero and not a small number. *Proof: §*Appendix: The Algebra*, §*The Containment*.*

**The containment is strict, and the strictness is the codimension count.** The kernel is four real dimensional; the value cone is six real dimensional, being two real equations on eight coordinates. So the kernel is a four-dimensional slice of the cone and not the cone. **The corner is a point of the label space crossed with a four-dimensional family of amplitudes, and the product is the wave.**

**What the containment buys.** It turns "both charts fail there" from a remark into a factorisation: the label chart's failure and the value chart's failure are the same element $\tilde\Pi$, read once as the annihilator of the symbol and once as the vanishing of the norm. **A reader who wants a single object for the corner should take the idempotent**: it is the projector that survives the symbol and the projector that has no norm.

## Two Waves, Not One

**The earlier article says "the one-sided wave", and both halves of that phrase need repair.** The first half first.

**At a given null label the solutions are a family, not a single wave.** The kernel $\tilde\Pi\mathbb{B}$ has four real parameters, so the amplitudes at that label are $\varkappa\tilde\Pi\tilde B$ for a fixed projector and an arbitrary right multiplyer; only the scale and phase of $\varkappa$ are visible in the quantities of this article. **The corner is one label and a family, and calling it "one wave" is shorthand for "one label".**

**The chiralities are two waves at two labels.** The check is explicit:

| label | amplitude | $\tilde K_\Phi\tilde\Xi_0$ |
| --- | --- | --- |
| $k(ie_t+\vec u)$ | $\tfrac12(e_t+i\vec u)$ | $0$ |
| $k(ie_t-\vec u)$ | $\tfrac12(e_t-i\vec u)$ | $0$ |
| $k(ie_t+\vec u)$ | $\tfrac12(e_t-i\vec u)$ | $=\tilde K_\Phi\neq0$ |
| $k(ie_t-\vec u)$ | $\tfrac12(e_t+i\vec u)$ | $=\tilde K_\Phi\neq0$ |

**The mirror comparison is exact and worth stating as an identity.** Since $\tilde\Pi_{-}=\tfrac12(e_t-i\vec u)$,

$$
2ik\,\tilde\Pi_{-}=ik\bigl(e_t-i\vec u\bigr)=k\bigl(ie_t+\vec u\bigr)=\tilde K_\Phi ,
$$

so the entry $2ik\tilde\Pi_{-}$ in the earlier sentence is $\tilde K_\Phi$ itself, and the mirror projector passes the symbol through unchanged.

**So the label selects the chirality and the chirality does not select the label.** There is **one surviving wave per future-null momentum**, and the mirror momentum carries the mirror idempotent; the two are opposite momenta and not two labels on one direction. **The count is one label, one chirality, one wave**, which is helicity-momentum locking stated as a rank count rather than as a kinematic fact: the annihilated projector is determined by the sign of the spatial momentum, so a null direction taken as an unoriented axis carries both, and a momentum carries one.

**The second half of the phrase is a collision.** "One-sided" already means the Dirac chiral pair in this corpus, where the two one-sided equations are the two factors of the two-sided one. **A reader who carries that meaning into the corner will read "one-sided wave" as "one of a chiral pair", which is not what the earlier article meant.** This article uses **null wave**: the wave whose label is null, whose amplitude is null, and whose value is null at every event.

## What Survives in Both Charts

**Both charts fail as charts, and both leave a usable residue.** The value chart leaves the pair $(\rho_{\mathrm{num}},\langle\tilde\Xi\rangle_{*})$, continuous at the corner by §*The Two Scales*; the label chart leaves the kernel, four real dimensional, and a least-squares inverse on its complement. **Neither residue needs the other, and together they describe the corner completely.**

**The action is not what fails, and the point is worth one sentence.** The Lagrangian evaluates to zero on the wave for the same reason it evaluates to zero on every solution, the dispersion being satisfied there; the zero is the stationarity of a solution and not a pathology of the corner. **What fails at the corner is the reading of the field and the inversion of the symbol, not the writing of either.**

**The corner is one point of a one-parameter family of corners.** Every null label is a corner at $k_m=0$, so the set is the whole label cone crossed with the amplitudes of §*One Factorisation, Two Failures*. **What is special is not a single wave but the collapse of two level sets into one**, and that collapse is the mass's absence.

## Limits

**The identity is algebraic and its subject is a conditional.** If $k_m=0$ and the label is null, then the symbol is null, the kernel is a right ideal of an idempotent, and every surviving value is on the cone. **No statement is made about any particular field of Nature.**

**The rank is the rung's.** At the first order the symbol keeps four of its eight dimensions; at the scalar order it keeps none. A reader who quotes "rank four" without the rung will be wrong half the time.

**The codimensions differ and always did.** The value cone is two real equations, the label cone one, so the two sets were never the same kind of object and only their level sets can coincide. **"The same cone" is a shorthand for "one level set of one function", and this article does not use it in any other sense.**

**The corner is measure zero in the parameters and not in the labels.** Every null label is a corner at $k_m=0$, so the corner is a whole cone of labels and a single value of the mass; **the rarity is in the mass, not in the mode.**

**The helicities are two and the family is four-dimensional.** Neither count is a physical degeneracy statement; both are dimensions of real vector spaces, computed from the algebra.

**The cone is not a state of the fluid.** Every entry of §*The Two Families That Approach Two Different Sets* is the value of a fluid at the mass it names. The cone has no density per rest volume, no quantum potential and no word, and the object there is a null current. **"Massless fluid" is a shorthand for "the limit of a fluid" and not a name for a thing on the cone.**

## Summary

**Two statements and one limit.** At every positive mass the fluid exists in full; at zero mass on the cone it does not, and what the corner holds is a null current with a direction, an intensity and a sign. **The mass carries the first into the second, and the passage is a limit and not a value.**

**The two failures are level sets of one function $k_m^{2}$ apart.** The fluid chart fails on the value cone $N(\tilde\Xi)=0$; the Fourier chart fails on the pole set $N(\tilde K_\Phi)=-k_m^{2}$; the mass is the height between them and $k_m=0$ is the one value at which they are one set.

**At that value the two failures are one factorisation.** The null symbol's kernel is $\tilde\Pi\mathbb{B}$, and because $N$ is multiplicative and $N(\tilde\Pi)=0$, every element of the kernel is on the value cone: **the set the label chart keeps is inside the set the value chart refuses.** Verified to $9.2\times10^{-16}$ on two thousand random multiples, and proved in one line.

**The wave carries a current and has no density.** $N(\tilde\Xi)=0$ and $\langle\tilde\Xi\rangle_{*}=\tfrac12\lvert\varkappa\rvert^{2}$ at every event, so $\rho_{\mathrm{num}}=0$ and $j^{0}=\tfrac{c}{2}\lvert\varkappa\rvert^{2}$: the corner is the place where article one's two numbers separate completely while the current stays finite.

**"One wave" is one label, two helicities and a four-real-dimensional family.** Each null label annihilates exactly one idempotent and the mirror label the mirror one, so helicity is locked to momentum by a rank count. **And the wave is the null wave, not the one-sided one**, since that word is already the Dirac chiral pair's.

**The corner is inhabited because the first-order rung loses only half.** The scalar symbol vanishes outright at $k_m=0$ on the cone, so its multiplication operator drops from rank $8$ to rank $0$; the first-order symbol becomes null, dropping from $8$ to $4$, and the half it keeps is the half the value chart refuses. **A rank count, not a coincidence.**

**The label chart's failure is a projection and not a divergence.** Its least-squares inverse exists at every nonzero frequency with norm $1/(2\lvert k\rvert)$, so the four dimensions the symbol loses are the four that inverse leaves undetermined: **the measure of the failure is the measure of the survival**, and the surviving part is the wave.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ | the quaternionic norm, $\sum_\mu Q_\mu^{2}$, complex, multiplicative |
| $\langle\tilde Q\rangle_{*}$ | the Euclidean size, $\sum_\mu\lvert Q_\mu\rvert^{2}$ |
| $\tilde K_\Phi=ik_t'e_t+\vec k_\Phi$ | the label, with imaginary time coefficient |
| $k_m$ | the mass in wave-number units, the block's $mc/\hbar$ |
| $N(\tilde K_\Phi)=-k_t'^{2}+\lvert\vec k_\Phi\rvert^{2}$ | the label's norm (plain $N$); the mass shell is $-k_m^{2}$ |
| $\mathcal N(\tilde K_\Phi)$ | the scalar symbol (script $\mathcal N$), $k_t'^{2}-\lvert\vec k_\Phi\rvert^{2}-k_m^{2}$, equal to $-N-k_m^{2}$ |
| $\Sigma(\tilde K_\Phi)$ | the algebra-valued symbol of the first-order rung |
| $L_{\tilde Q}$ | left multiplication by $\tilde Q$ as a real map on eight coordinates |
| $\tilde\Pi$, $\tilde\Pi_{-}$ | $\tfrac12(e_t\pm i\vec u)$, idempotents on the value cone |
| $\varkappa$ | the complex amplitude of the null wave |
| $\vec u$ | the unit direction of the null momentum, $-\vec u_p$; the only spatial axis used, named so that every statement rotates |
| $\vec u_p=\vec k_\Phi/\lvert\vec k_\Phi\rvert$ | the direction of the momentum |
| $\gamma=E/(mc^{2})$ | the time-dilation factor; finite at $m>0$, absent at the cone |
| $j_\mu$ | the current; $\tfrac{c}{2}\lvert\varkappa\rvert^{2}(1,\vec u)$ at the corner |
| $\rho_{\mathrm{num}}=\lvert N\rvert$ | the proper density, the invariant length over $c$ |
| $j^{0}=c\langle\tilde\Xi\rangle_{*}$ | the current's time component |

## Appendix: The Algebra

### The Rank of a Null Symbol

**Claim.** Let $\tilde Q\neq0$ with $N(\tilde Q)=0$. Then $L_{\tilde Q}$, left multiplication by $\tilde Q$ on the eight real coordinates, has rank four and kernel of real dimension four.

*Proof.* $\mathbb{B}$ is the complex $2\times2$ matrices, and left multiplication by $\tilde Q$ is left multiplication by a $2\times2$ matrix $M_{\tilde Q}$. The determinant of $M_{\tilde Q}$ is $N(\tilde Q)$ up to a convention, so $N(\tilde Q)=0$ with $\tilde Q\neq0$ says exactly that $M_{\tilde Q}$ is a nonzero singular matrix. **Count the kernel of the multiplication map, not of the matrix.** Writing $X\in M_2(\mathbb{C})$ as a pair of columns, $L_{\tilde Q}X=M_{\tilde Q}X$ acts on the columns separately, so

$$
L_{\tilde Q}X=0\quad\Longleftrightarrow\quad \text{both columns of }X\text{ lie in }\ker M_{\tilde Q} .
$$

**Since $M_{\tilde Q}$ is nonzero and singular, $\ker M_{\tilde Q}$ is one complex dimensional**, so each of the two columns contributes one free complex parameter: the kernel of $L_{\tilde Q}$ has complex dimension $2$ and **real dimension $4$**. The eight real dimensions of $M_2(\mathbb{C})$ minus four is four, so the real rank is $4$. **The image count is a consequence and not an extra input**: left multiplication by a rank-one matrix has image inside the one-dimensional $\operatorname{im}M_{\tilde Q}$ spanned over the two columns, which is two complex dimensions, the same four real dimensions.

**The kernel is a right ideal.** If $M_{\tilde Q}\tilde\Pi=0$ then $M_{\tilde Q}(\tilde\Pi\tilde B)=0$ for every $\tilde B$, so the kernel is closed under right multiplication and is the right ideal generated by the idempotent projector onto $\ker M_{\tilde Q}$. **That the projector is itself null is the containment of the next subsection, not an extra hypothesis.**

### The Idempotents and the Annihilation

**Claim.** $\tilde\Pi=\tfrac12(e_t+i\vec u)$ satisfies $\tilde\Pi^{2}=\tilde\Pi$, $N(\tilde\Pi)=0$, $\langle\tilde\Pi\rangle_{*}=\tfrac12$, and $\tilde K_\Phi\tilde\Pi=0$ for the null label $\tilde K_\Phi=k(ie_t+\vec u)$ with $k\neq0$ real.

*Proof.* **The square.** Expand term by term, keeping the two cross terms and the two squares separate:

$$
(e_t+i\vec u)^{2}=e_t^{2}+i e_t\vec u+i\vec u e_t+i^{2}\vec u^{2}=e_t+i\vec u+i\vec u+e_t=2e_t+2i\vec u ,
$$

using $e_t^{2}=e_t$, $e_t\vec u=\vec u e_t=\vec u$, $\vec u^{2}=-e_t$ and therefore $i^{2}\vec u^{2}=(-1)(-e_t)=+e_t$. **The sign there is the place an expansion goes wrong**: $i^{2}\vec u^{2}$ is $+\vec e_t$ and not $-\vec e_t$, and it is what makes the two $e_t$ terms add rather than cancel. The result is $2(e_t+i\vec u)$, so halving gives $\tilde\Pi^{2}=\tilde\Pi$. **The norm** is $N(\tilde\Pi)=\tfrac14\bigl(1^{2}+i^{2}\bigr)=0$ and **the size** is $\tfrac14(1+1)=\tfrac12$. **The annihilation** is the product

$$
(ie_t+\vec u)(e_t+i\vec u)=ie_t^{2}+i^{2}e_t\vec u+\vec u e_t+i\vec u^{2}=ie_t-\vec u+\vec u-ie_t=0 ,
$$

using $e_t\vec u=\vec u$, $\vec u e_t=\vec u$ and $i^{2}\vec u^{2}=(-1)(-e_t)=e_t$. **Every term cancels pairwise and no null condition is used**: the product is zero for the factorisation $k(ie_t+\vec u)$ at any $k$, and the label's nullity is what makes that factorisation the label of a massless mode. **The mirror** is $(ie_t+\vec u)(e_t-i\vec u)=ie_t+\vec u+\vec u+ie_t=2(ie_t+\vec u)$, so $\tilde K_\Phi\tilde\Pi_{-}=\tilde K_\Phi$ and the mirror projector is in the kernel of nothing.

### The Containment

**Claim.** $\tilde\Pi\mathbb{B}\subseteq\{\tilde Q: N(\tilde Q)=0\}$, with strict inclusion.

*Proof.* $N(\tilde\Pi\tilde B)=N(\tilde\Pi)N(\tilde B)=0$ by multiplicativity and $N(\tilde\Pi)=0$. **Strictness**: the kernel is four real dimensional by the rank claim and the value cone is six real dimensional, being the vanishing of the complex number $N$, which is two real equations on eight coordinates with independent gradients off the origin.

### The Scalar Symbol at the Corner

**Claim.** The scalar symbol $\mathcal N(\tilde K_\Phi)=k_t'^{2}-\lvert\vec k_\Phi\rvert^{2}-k_m^{2}$ vanishes on the label cone exactly when $k_m=0$, and equals $-k_m^{2}$ there otherwise.

*Proof.* On the cone $k_t'^{2}=\lvert\vec k_\Phi\rvert^{2}$, so $\mathcal N=-k_m^{2}$. **A central element $-k_m^{2}e_t$ is invertible whenever $k_m\neq0$**, its inverse being $(-1/k_m^{2})e_t$, so $L$ has rank eight; and at $k_m=0$ the symbol is the zero element and $L$ has rank zero. **This is why the scalar rung loses the whole operator and the first-order rung only half of it.**

### The Numerical Checks

| check | statement | residual |
| --- | --- | --- |
| the null symbol is null | $N(\tilde K_\Phi)$ for $k=1$ and $k=2.7$ | $0$ identically |
| the rank | singular values of $L_{\tilde K_\Phi}$ | $\{2,2,2,2,0,0,0,0\}$ and $\{5.4,5.4,5.4,5.4,0,0,0,0\}$ |
| the annihilation | $\tilde K_\Phi\tilde\Pi$ | $0$ |
| the mirror mismatch | $\tilde K_\Phi\tilde\Pi_{-}$ against $2ik\tilde\Pi_{-}$ | $0$ |
| the idempotent | $\tilde\Pi^{2}-\tilde\Pi$ | $0$ |
| the containment | $\max\lvert N(\tilde\Pi\tilde B)\rvert$ over $2000$ random $\tilde B$ | $9.2\times10^{-16}$ |
| the least-squares inverse | $\lVert L^{+}\rVert$ against $1/(2k)$ at four frequencies | $0$ |
| the KG symbol | $\mathcal N$ on the cone at $k_m\in\{0,0.5,2\}$ | $0$, $-0.25$, $-4$ |

**These are checks and not proofs.** The proofs are the four claims above; the numbers confirm that the claims were transcribed into the corpus's conventions.

## Further Reading

**The two integrals.** [The Two Integrals: the Action and the Transform Confronted Rung by Rung](../articles_internal/the-two-integrals-the-action-and-the-transform-confronted-rung-by-rung.html) states the two cones and the mass between them, and this article proves the containment its last paragraph asserts. [The Massless Regime](the-massless-regime.html) takes the limit at infinite rapidity; [The Domain of the Fluid Reading](the-domain-of-the-fluid-reading.html) states the chart's domain and its codimension.

**The cone.** [The Group of Invertibles, the Cone and the Orders](the-group-of-invertibles-the-cone-and-the-orders.html) and [The Massless Regime](the-massless-regime.html) describe what lives on it; [The Partition: Two Invariants and Four Regimes](the-partition-two-invariants-and-four-regimes.html) proves multiplicativity; [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) is the algebraic statement of the rank drop.

**The two numbers.** [The Two Scales of the Field](../articles_physics/the-two-scales-of-the-field-the-proper-density-and-the-euclidean-size.html) proves that the pair is continuous at the corner and that the size is the current's time component.

**Outside.** P. A. M. Dirac, "The quantum theory of the electron", *Proc. R. Soc. A* **117** (1928), for the null projector and the helicity lock; R. Penrose and W. Rindler, *Spinors and Space-Time*, vol. 2, Cambridge University Press (1986), for the correspondence between the null cone, the rank-one projectors and the lightlike directions that §*Two Waves, Not One* uses.
