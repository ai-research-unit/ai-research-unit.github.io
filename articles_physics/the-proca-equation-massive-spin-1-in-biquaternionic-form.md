# __The Proca Equation: Massive Spin 1 in Biquaternionic Form__

## Introduction

The Maxwell field is massless, and its masslessness is what reduces four potential components to two physical transverse polarizations: the gauge freedom removes one combination and the field equation removes another. Give the vector field a mass and the gauge freedom disappears. The equation of motion then becomes the **Proca equation**, and the third, longitudinal polarization becomes physical, with the two helicities no longer Lorentz-invariant labels. The Proca field is the prototype of a massive spin-one field, and it is the first field equation that the self-dual split of the material sector supports.

The purpose of this article is to write the Proca system in biquaternionic form and to read its content from the algebra. The equation is a single biquaternion equation for the four-potential $\tilde{A}_{\Phi}\in\mathbb{B}_{\Phi}$ and its field strength $\tilde{F}\in\mathbb{B}_{V}$. Two structural facts organise everything. First, the equation is **homogeneous but not gauge invariant**: the source that the companion Maxwell equation attributes to an external current is supplied here by the potential itself, so the equation is linear in $\tilde{A}_{\Phi}$ and the gauge freedom of the massless theory is absent. Second, the divergence of the equation is not an identity: applying the conjugate gradient to the equation and taking its scalar part forces the **Lorenz condition** $S = \mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}) = 0$, exactly as taking the divergence of the standard Proca equation forces $\langle\tilde\nabla_\Phi,\tilde A_{\Phi}\rangle_{\natural} = 0$. The Lorenz condition is a consequence of the equation, not a gauge choice, and that is the algebraic statement of the disappearance of the gauge freedom.

Once the Lorenz condition is available, the Proca equation collapses to the Klein–Gordon equation for each component, and the physical content is transparent: three real polarization directions at each wavevector — two transverse and one longitudinal — with the dispersion relation $\omega^2 = 4\pi^{2}c^{2}\left(\vec\nu_\Phi^{2} + \nu_m^{2}\right)$. The counting is done here explicitly, and it is contrasted with the massless case, where the same calculation leaves two real directions because a residual gauge transformation removes the third. The article closes by locating the massive field relative to the self-dual split of the companion article: the field strength remains a pure vector of the algebra and so keeps its self-dual and anti-self-dual coordinates, but it is no longer harmonic, and the mass term is precisely what the biquaternion Maxwell equation calls a source. The limit $m\to0$ is then proved rather than asserted. §*The Massless Limit: Proca at m = 0 Is Maxwell* shows that the Proca system at $\nu_m=0$ is the Maxwell system by substitution, term for term, and that what changes at the limit is the constraint and the solution space rather than the equation: the Lorenz condition falls from a consequence to a choice, the count of polarisations falls from three to two, and gauge invariance appears. Here $\nu_m=\frac{m\,c}{h}$ is the mass wave number, the inverse of the mass length.

**The carrier: this article works on *Introduction to the Spin-One Anti-Hermitian Subspace*.** The spin fixes the subspace: a spin-one potential needs a four-vector, and the four-vectors of the algebra are the material sector $\mathbb{B}_{\Phi}$, of real dimension four. The restriction is not a choice of taste; it is the statement that the potential is anti-Hermitian, which is what makes its quaternionic norm real and its vector square non-negative. The subspace, its two namings — the triple for the spin and the sector for the amplitude — and the counting are [Introduction to the Spin-One Anti-Hermitian Subspace](the-spin-one-anti-hermitian-subspace.html), and nothing about it is derived below. Two consequences follow, and both are proved there. First, the sector is closed under the Proca operator for **every** material potential, because the residual of the equation is a material element times a central scalar; the Lorenz condition makes that scalar vanish and is not what makes the residual material. Second, the sector is a real form, $i\mathbb{B}_{\Phi}=\mathbb{B}_{\Psi}$, so a continuous phase destroys it and the restriction is a restriction to the neutral field. The scalar-free part carries the field strength and the spin itself, and the Lorenz condition removes the time slot that separates the four-vector from the three states of the spin.

The conventions are those of the companion articles. The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_{\imath}^2=-e_t$, and central scalar imaginary $i$; the gradient is $\tilde\nabla_\Phi=e_t\partial/\partial R_t+\vec e_x\partial/\partial R_x+\vec e_y\partial/\partial R_y+\vec e_z\partial/\partial R_z$ with $(\tilde\nabla_\Phi)^{\natural}$ its quaternion conjugate and $\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2$; the potential and field strength are $\tilde{A}_{\Phi}=i\,a'_t\,e_t+\vec A$ and $\tilde{F}=(\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}-\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi})=i\vec E-c\vec B$, with $c=1/\sqrt{\epsilon\mu}$ and the normalization of the potential fixed so that the two expressions for $\tilde{F}$ agree; and the mass enters as the wave number $\nu_m=\frac{m\,c}{h}$, whose reciprocal $1/(2\pi\nu_m)$ is the mass length written where the dimensions have to be displayed.

## The Standard Proca Theory

### Lagrangian and equation

The Proca field is a real four-vector $A_{\imath}$ with the Lagrangian density

$$
\mathcal{L} = -\tfrac14\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath} + 2\pi^{2}\nu_m^{2}\sum_{\imath} A_{\imath} A_{\imath}, \qquad F_{\imath\jmath} = \partial/\partial R_{\imath} A_{\jmath} - \partial/\partial R_{\jmath} A_{\imath},
$$

where $1/(2\pi\nu_m)$ is the mass length and $\nu_m=\frac{m\,c}{h}$ is its reciprocal, and the sign of the mass term is the one that makes the energy positive. Variation with respect to $A_{\jmath}$ gives the **Proca equation**

$$
\tilde\nabla_\Phi\tilde F-4\pi^{2}\nu_m^{2}\tilde A_{\Phi}=0 .
$$

The equation differs from the source-free Maxwell equation by the mass term alone, and that term is what breaks the gauge symmetry: under $A_{\imath} \to A_{\imath} - \partial/\partial R_{\imath}\,\Gamma$ the field strength is unchanged but the mass term is not, since $\sum_{\imath} A_{\imath} A_{\imath}$ is not invariant. A massive vector field has no gauge freedom.

### The constraint

The mass term also changes the constraint structure. Contracting the equation with $\partial/\partial R_{\jmath}$ and using the antisymmetry of $F_{\imath\jmath}$,

$$
\sum_{\imath,\jmath}\partial^2/\partial R_{\imath}\partial R_{\jmath}\,F_{\imath\jmath} = 0
\qquad\Longrightarrow\qquad
4\pi^{2}\nu_m^{2}\langle\tilde\nabla_\Phi,\tilde A_{\Phi}\rangle_{\natural}=0
\qquad\Longrightarrow\qquad
\langle\tilde\nabla_\Phi,\tilde A_{\Phi}\rangle_{\natural}=0 ,
$$

for a finite mass, $\nu_m\neq0$. The **Lorenz condition** is therefore a consequence of the equation of motion and not a choice of gauge: it is one of the equations of the system. This is the sharpest structural difference from the Maxwell case, where the same condition can be imposed but not derived, and where it is preserved as a gauge choice rather than fixed.

### Reduction and dispersion

With the Lorenz condition in hand, the field strength contracts to a d'Alembertian,

$$
\tilde\nabla_\Phi\tilde F = \Box_\Phi\tilde A_{\Phi}-\tilde\nabla_\Phi\langle\tilde\nabla_\Phi,\tilde A_{\Phi}\rangle_{\natural} = \Box_\Phi\tilde A_{\Phi},
$$

so that the Proca equation becomes

$$
\left(\Box_\Phi + 4\pi^{2}\nu_m^{2}\right) A_{\jmath} = 0
$$

in the mostly-minus convention. In the series convention, whose d'Alembertian is $\Box_\Phi = \partial^2/\partial R_t^2 + \Delta_\Phi$ and therefore the negative of the mostly-minus operator, the same statement is

$$
\left(\Box_\Phi-4\pi^{2}\nu_m^{2}\right)\tilde{A}_{\Phi} = 0 ,
$$

the Klein–Gordon equation with the physical mass shell $\omega^2 = 4\pi^{2}c^{2}\left(\vec\nu_\Phi^{2} + \nu_m^{2}\right)$. The field of a massive vector particle is thus a four-vector each of whose components satisfies the Klein–Gordon equation, subject to the single constraint $\langle\tilde\nabla_\Phi,\tilde A_{\Phi}\rangle_{\natural} = 0$. Four components minus one constraint leaves three. This count is standard and is checked below on the explicit plane waves.

### The rest frame and the three states

The three polarizations are easiest to see in the rest frame, $\vec\nu_\Phi = \mathbf{0}$. The dispersion relation gives $\omega = 2\pi c\,\nu_m$, and the Lorenz condition gives $A_t = 2\pi i(c/\omega)\vec\nu_\Phi\cdot\vec a = 0$, so the time component vanishes and the amplitude is purely spatial. The three real components of $\vec a$ are then three independent states, degenerate in energy and forming the three states $m_s = +1,0,-1$ of a spin-one particle along any chosen quantisation axis. There is no condition that removes the component of $\vec a$ along $\vec\nu_\Phi$, and in the rest frame that component is unconstrained: all three directions survive. A massless particle has no rest frame, its two polarizations are the two transverse directions for every wavevector, and the third state is absent. The change from two to three states as the mass is turned on is thus visible already at the level of the rest-frame amplitudes.

## The Biquaternion Proca Equation

### Statement

The Proca system is transcribed into the framework by replacing the four-vector by the material-sector biquaternion and the gradient by the biquaternionic gradient. The replacement is a change of kind, not of notation: $\tilde A_\Phi\in\mathbb{B}_\Phi$ is an **anti-Hermitian** element of the algebra, whereas the "real four-vector" of the section above names the component field $A_{\imath}$ of the standard theory. Under $\mathbb{B}=\mathbb{B}_\Psi\oplus\mathbb{B}_\Phi$ the potential sits in the material summand and the field strength $\tilde F$ in its vector part, and every statement below is a statement about those summands. The single equation is

$$
\boxed{\;\tilde\nabla_\Phi\tilde{F} = 4\pi^{2}\nu_m^{2}\,\tilde{A}_{\Phi},
\qquad
\tilde{F} = (\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi} - \mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}\right)\;},
$$

or, with the mass carried by the mass length,

$$
\tilde\nabla_\Phi\tilde{F} = m^2\,\tilde{A}_{\Phi}.
$$

The left-hand side is $\tilde\nabla_\Phi\tilde F$; the right-hand side is the mass term. The equation is the massive analogue of the companion Maxwell equation $\tilde\nabla_\Phi\tilde{F} = -Z\,\tilde{J}_{\Phi}$, with the external source $Z\,\tilde{J}_{\Phi}$ replaced by a current proportional to the potential itself.

### Why the equation is the right one

The transcription is not a guess. It is fixed by two requirements: the equation must reproduce the standard Proca system, and it must do so in the series' $i r'_t$ convention without a change of metric. The check is carried out below by solving the equation for plane waves and reading off the dispersion relation. The result is the physical massive shell and the Lorenz condition, and the two together are the standard content of the Proca system. Any other relative sign between the two sides would give a dispersion relation with the wrong sign of $m^2$, that is, a spacelike or tachyonic shell, and the check excludes it.

### The failure of gauge invariance, explicitly

The massless companion equation is invariant under the gauge transformation $\tilde{A}_{\Phi}\to\tilde{A}_{\Phi}-\tilde\nabla_\Phi\Gamma$ of the companion Maxwell article, because the field strength is built from $(\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}$ and $(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi\Gamma = \Box_\Phi\Gamma$ is a central scalar, which the projection to the vector part discards. For the Proca equation the same transformation changes the right-hand side alone,

$$
\tilde\nabla_\Phi\tilde{F} \;\longmapsto\; \tilde\nabla_\Phi\tilde{F}, \qquad
4\pi^{2}\nu_m^{2}\,\tilde{A}_{\Phi} \;\longmapsto\; 4\pi^{2}\nu_m^{2}\left(\tilde{A}_{\Phi}-\tilde\nabla_\Phi\Gamma\right),
$$

so the equation is preserved only if $\tilde\nabla_\Phi\Gamma = 0$, that is, only for a constant $\Gamma$. The transformation is therefore not a symmetry, and there is no gauge orbit to quotient by. The algebraic reason is that the mass term is the only term in the equation that is not built from the field strength: it is a term in the potential, and the potential is not gauge invariant. This is the biquaternion statement of the standard fact that the Proca Lagrangian's mass term $\sum_{\imath} A_{\imath} A_{\imath}$ breaks the gauge symmetry.

## The Lorenz Condition Is Implied

The biquaternion form of the divergence argument is short, and it is the cleanest place where the algebra does work that the index notation leaves implicit.

Apply the conjugate gradient $(\tilde\nabla_\Phi)^{\natural}$ to both sides of the Proca equation and use that the gradient has constant coefficients, so that $(\tilde\nabla_\Phi)^{\natural}(\tilde\nabla_\Phi\tilde{F}) = ((\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi)\tilde{F} = \Box_\Phi\tilde{F}$:

$$
\Box_\Phi\tilde{F} = 4\pi^{2}\nu_m^{2}\,(\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}.
$$

Now take the scalar part of both sides. The d'Alembertian $\Box_\Phi$ is a central scalar differential operator, so it preserves the scalar–vector decomposition and $\mathrm{Sc}(\Box_\Phi\tilde{F}) = \Box_\Phi\,\mathrm{Sc}(\tilde{F})$. The field strength $\tilde{F} = \mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi})$ is a **pure vector**, so $\mathrm{Sc}(\tilde{F}) = 0$, and the left-hand side vanishes identically. Hence

$$
\boxed{\;0 = 4\pi^{2}\nu_m^{2}\,\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}\right)
\qquad\Longrightarrow\qquad
S := \mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}\right) = 0\;},
$$

which is the **Lorenz condition** of the companion Maxwell article, whose components are $\partial/\partial R_t\,A_t + \mathrm{div}\,\vec A = 0$. The derivation uses only three facts: the field strength is a pure vector, the d'Alembertian is central and scalar, and the mass parameter is nonzero. In the massless case the same computation gives $0 = 0$ and no constraint, which is exactly why the gauge freedom survives there and is absent here.

## The Massless Limit: Proca at m = 0 Is Maxwell

**Theorem.** The Proca system at $m=0$ is the Maxwell system, and each of the three statements below is an exact substitution rather than an approximation.

1. The Proca Lagrangian density loses its mass term, and what remains is the Maxwell Lagrangian density, term for term.
2. The Proca equation $\sum_{\imath}\varepsilon_{\imath}\partial_{\imath} F_{\imath\jmath}+4\pi^{2}\nu_m^{2}A_{\jmath}=0$ becomes the source-free Maxwell equation $\sum_{\imath}\varepsilon_{\imath}\partial_{\imath} F_{\imath\jmath}=0$.
3. The biquaternion Proca equation $\tilde\nabla_\Phi\tilde{F}=4\pi^{2}\nu_m^{2}\tilde{A}_{\Phi}$ becomes the source-free biquaternion Maxwell equation $\tilde\nabla_\Phi\tilde{F}=0$.

No approximation enters any of the three: setting a parameter to zero deletes a term and leaves the rest unchanged. What changes at $\nu_m=0$ is not the equation but the **constraint structure** and the **solution space**. The equation is continuous in $m$; the solution space is not, and the rest of this section separates the two.

### The Lagrangian reduction

The Proca density for a real four-vector with $F_{\imath\jmath}=\partial_{\imath} A_{\jmath}-\partial_{\jmath} A_{\imath}$ is

$$
\mathcal{L}_{P}[A]=-\tfrac14\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}+2\pi^{2}\nu_m^{2}\sum_{\imath} A_{\imath} A_{\imath} ,
\qquad \nu_m=\frac{m\,c}{h}.
$$

The first term is the Maxwell density and the second is the mass term. At $\nu_m=0$ the second vanishes identically and

$$
\mathcal{L}_{P}[A]\big|_{\nu_m=0}=-\tfrac14\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}=\mathcal{L}_{M}[A],
$$

which is the Maxwell density, term for term. With an external current the densities gain the same coupling $-\sum_{\imath} J_{\imath} A_{\imath}$ on both sides, and the coupling is untouched by the mass, so the identity survives: $\mathcal{L}_{P,J}|_{\nu_m=0}=\mathcal{L}_{M,J}$.

Two things are worth naming. The mass term is the only term in the density that is quadratic in the **potential** rather than in the field strength, and that is exactly why it is the only term the substitution touches. And the substitution is not a limit: no sequence is taken, no term is dropped as small, and the identity is an algebraic identity between two densities at $\nu_m=0$.

### The equation of motion

Varying the density with respect to $A_{\jmath}$ gives $\partial\mathcal{L}_P/\partial A_{\jmath}=4\pi^{2}\nu_m^{2}A_{\jmath}$ and $\partial\mathcal{L}_P/\partial(\partial_{\imath} A_{\jmath})=-F_{\imath\jmath}$, so the Euler–Lagrange equation is

$$
\sum_{\imath}\varepsilon_{\imath}\partial_{\imath} F_{\imath\jmath}+4\pi^{2}\nu_m^{2}A_{\jmath}=0 .
$$

At $\nu_m=0$ this is $\sum_{\imath}\varepsilon_{\imath}\partial_{\imath} F_{\imath\jmath}=0$, the source-free Maxwell equation; with the current it is $\sum_{\imath}\varepsilon_{\imath}\partial_{\imath} F_{\imath\jmath}=J_{\jmath}$, the sourced one.

**The mass sits in the zeroth-order term, and that is the whole content of the continuity.** The principal symbol of the Proca operator — the part that decides the characteristics and therefore the propagation — is $\sum_{\imath}\varepsilon_{\imath}\partial_{\imath} F_{\imath\jmath}$ and does not contain $\nu_m$ at all. There is no singular perturbation: the differential operator is not deformed, a lower-order term is deleted. That is the precise sense in which the equation depends continuously on the mass, and it is what licenses the substitution at the level of the equation.

The claim was checked on plane waves rather than asserted. With $\nu_m=1.3$ and $\vec\nu_\Phi=(0.4,-0.9,1.1)$, so that $\omega^{2}=4\pi^{2}c^{2}\left(\vec\nu_\Phi^{2}+\nu_m^{2}\right)$, one hundred random real amplitudes projected on the Lorenz surface satisfy the Proca equation with a maximum residual of $2.7\times10^{-15}$ in units of the amplitude; at $\nu_m=0$ the same amplitudes, on the null shell $\omega=2\pi\lvert\vec\nu_\Phi\rvert$, satisfy $\sum_{\imath}\varepsilon_{\imath}\partial_{\imath} F_{\imath\jmath}=0$ with a maximum residual of $1.5\times10^{-15}$.

### The biquaternion reduction

The Proca article writes the system as the single equation

$$
\tilde\nabla_\Phi\tilde{F}=4\pi^{2}\nu_m^{2}\,\tilde{A}_{\Phi},
\qquad
\tilde{F}=\mathrm{Vect}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}\right),
$$

with $\tilde{A}_{\Phi}\in\mathbb{B}_{\Phi}$ and $\tilde{F}\in\mathbb{B}_{V}$. At $\nu_m=0$,

$$
\tilde\nabla_\Phi\tilde{F}=0 ,
$$

which is the source-free biquaternion Maxwell equation of the companion article, and with a source it is $\tilde\nabla_\Phi\tilde{F}=-Z\,\tilde{J}_{\Phi}$.

**The reduction is exact here for a structural reason.** The field strength is defined by the same formula in both articles, so the left-hand side of the equation is one expression and not two, and only the right-hand side loses its shift. Nothing about the algebra changes at $\nu_m=0$: the operator is the same operator, acting on the same carrier, and the equation it satisfies loses its potential term.

The algebra also states the constraint of §*What is discontinuous, first* once, in a form that costs no indices. Since $(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi=\Box_\Phi$ is central and scalar and $\mathrm{Sc}(\tilde{F})=0$ for a pure vector, $\mathrm{Sc}(\Box_\Phi\tilde{F})=0$ identically — checked exactly on one hundred random pure-vector fields — and applying $(\tilde\nabla_\Phi)^{\natural}$ to the equation and taking the scalar part gives

$$
0=4\pi^{2}\nu_m^{2}\,\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}\right)=4\pi^{2}\nu_m^{2}S .
$$

The identity $\mathrm{Sc}(\Box_\Phi\tilde{A}_{\Phi})=N(\tilde\nabla_\Phi)\,\mathrm{Sc}(\tilde{A}_{\Phi})$ used in passing was verified to $4.0\times10^{-15}$ on one hundred random elements.

### What is continuous

Three things survive the limit, and they are of three different kinds.

- **The principal symbol.** It is the same operator for every $\nu_m$, and the mass is a constant added to the d'Alembertian rather than a change of the derivative structure.
- **The left-hand side.** $\tilde\nabla_\Phi\tilde{F}$ is one expression, written once, in both equations.
- **The carrier.** [Introduction to the Spin-One Anti-Hermitian Subspace](the-spin-one-anti-hermitian-subspace.html) shows that the residual of the Proca equation is a material element times a central scalar, so $\mathbb{B}_{\Phi}$ is closed under the Proca operator for **every** material potential, at every $\nu_m$ including zero. The home of the field is therefore continuous in the mass, and the Lorenz condition is not what closes it.

The third of these is the one that matters for the framework, because it is the statement that the massless limit is not a change of kind. The Proca and Maxwell potentials live in the same sector; the difference between the two theories is a constraint and not a home.

### What is discontinuous, first: the constraint changes status

Contract the sourced equation with $\partial_{\jmath}$. The first term vanishes identically, because $\partial_{\jmath}\partial_{\imath}$ is symmetric in the pair while $F_{\imath\jmath}$ is antisymmetric, so

$$
4\pi^{2}\nu_m^{2}\,\sum_{\jmath}\varepsilon_{\jmath}\partial_{\jmath} A_{\jmath}=\sum_{\jmath}\varepsilon_{\jmath}\partial_{\jmath} J_{\jmath} .
$$

The antisymmetry was checked on one hundred random amplitudes and wavevectors to $2.9\times10^{-15}$. Two cases follow, and they are different statements.

- **For $\nu_m\neq0$ and $J=0$:** the identity forces $\sum_{\jmath}\varepsilon_{\jmath}\partial_{\jmath} A_{\jmath}=0$. The Lorenz condition is a **consequence of the equation of motion**, not a choice of gauge.
- **For $\nu_m=0$:** the identity reads $\sum_{\jmath}\varepsilon_{\jmath}\partial_{\jmath} J_{\jmath}=0$, which is the conservation of the source and the integrability condition of the Maxwell equation. The Lorenz condition is **not** forced; it becomes a **choice of gauge**.

The biquaternion form of the same dichotomy is the boxed identity of the section above, $0=4\pi^{2}\nu_m^{2}S$. The mass is the coefficient that converts an identity into a constraint, and at $\nu_m=0$ the identity carries no information at all.

### Second: the count falls from three to two

For $\nu_m\neq0$, the potential has four components and the forced Lorenz condition removes one, leaving three: the two transverse directions and the longitudinal one. For $\nu_m=0$, the Lorenz condition must be imposed rather than derived, which again leaves three, and then the residual gauge transformation $\tilde{A}_{\Phi}\to\tilde{A}_{\Phi}-\tilde\nabla_\Phi\Gamma$ with $\Box_\Phi\Gamma=0$ removes one more, leaving two. The count jumps from three to two at the limit.

**Why the massless case loses one more, in one line.** For a timelike wavevector, $\nu_t^{\prime\,2}-\vec\nu_{\Phi}^{2}=\nu_m^{2}\neq0$, the wavevector is not orthogonal to itself, so it does not lie in its own Lorenz hyperplane, and no shift along $\vec\nu_{\Phi}$ preserves both the field strength and the Lorenz scalar. For a null wavevector, $\nu_t^{\prime\,2}-\vec\nu_{\Phi}^{2}=0$, and the opposite holds: the wavevector lies in its own Lorenz hyperplane, and the shift $A\mapsto A+\digamma_{\mathrm{gau}}\tilde\Upsilon_{\Phi}$ preserves the field strength **and** preserves $\partial\cdot A$. One direction of the three-dimensional Lorenz space is therefore a gauge orbit, and three minus one is two.

The two numbers were checked. On the null shell $\lvert\nu_t^{\prime\,2}-\nu_{\Phi}^{2}\rvert=2.3\times10^{-16}$; the shift leaves the field strength invariant to $1.3\times10^{-15}$ and the Lorenz scalar invariant to $1.4\times10^{-15}$. On the massive shell $\nu_t^{\prime\,2}-\nu_{\Phi}^{2}=\nu_m^{2}=1.69$; the same shift moves the Lorenz scalar by $\digamma_{\mathrm{gau}} \nu_m^{2}$, at least $1.1\times10^{-2}$ over one hundred draws, so it is not a symmetry and no orbit forms.

**The algebra's form of the drop is a rank.** Left multiplication by the on-shell symbol $2\pi i\tilde\Upsilon_{\Phi}$ is an invertible linear map at $\nu_m\neq0$ and a singular map of rank two on the null shell: the computed rank is four for the massive momentum and two for the massless one, which reproduces the companion article's statement in *Conformal Invariance and the Massless Limit in Biquaternionic Form* that the drop from four to two is the algebraic form of the massless limit.

### Third: gauge invariance emerges

The mass term is the only non-invariant piece of the density. Under $A_{\imath}\mapsto A_{\imath}-\partial_{\imath}\Gamma$ the field strength is unchanged and the mass term moves by

$$
2\pi^{2}\nu_m^{2}\sum_{\imath} A_{\imath} A_{\imath} \longmapsto 2\pi^{2}\nu_m^{2}\sum_{\imath} A_{\imath} A_{\imath}
+2\pi^{2}\nu_m^{2}\left(-2\sum_{\imath} A_{\imath}\,\partial_{\imath}\Gamma+\sum_{\imath}\partial_{\imath}\Gamma\,\partial_{\imath}\Gamma\right),
$$

which is $3.45$ at $\nu_m=1\ \mathrm{fm^{-1}}$ for a random configuration of order one and **exactly zero** at $m=0$. The biquaternion statement is the same and shorter: $\mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi})$ is invariant under $\tilde{A}_{\Phi}\mapsto\tilde{A}_{\Phi}-\tilde\nabla_\Phi\Gamma$ for a scalar $\Gamma$, verified to $4.1\times10^{-15}$ on one hundred random elements, while $4\pi^{2}\nu_m^{2}\tilde{A}_{\Phi}$ is not, because the potential is not gauge invariant.

Gauge invariance is therefore not a property that the massive theory already has and the massless theory retains. It is a property that **appears** at $\nu_m=0$ and was broken at every nonzero mass, and the algebra says why in one line: the mass term is the only term in the equation built from the potential instead of from the field strength.

### The Stueckelberg form, and the continuity of the parametrisation

The discontinuity in the solution space can be removed by a field redefinition. Introduce a real scalar $\xi$ and build the mass term from the combination

$$
\tilde{A}_{\Phi}\;\longmapsto\;\tilde{A}_{\Phi}+\frac{1}{2\pi\nu_m}\tilde\nabla_\Phi\xi ,
$$

so that the density becomes $\mathcal{L}_{S}[\tilde{A}_{\Phi},\xi]$ with $2\pi^{2}\nu_m^{2}\langle\tilde{A}_{\Phi}+\tfrac{1}{2\pi\nu_m}\tilde\nabla_\Phi\xi\rangle_{\natural}$ in place of $2\pi^{2}\nu_m^{2}\langle\tilde{A}_{\Phi}\rangle_{\natural}$. Under the simultaneous transformations

$$
\tilde{A}_{\Phi}\longmapsto\tilde{A}_{\Phi}-\tilde\nabla_\Phi\Gamma ,
\qquad
\xi\longmapsto\xi+2\pi\nu_m\Gamma ,
$$

the combination is invariant — an algebraic identity, since the two shifts cancel in $\tilde{A}_{\Phi}+\tfrac{1}{2\pi\nu_m}\tilde\nabla_\Phi\xi$ — and the density is gauge invariant again. The scalar $\xi$ is the **Stueckelberg field**. On a plane wave it contributes a piece along the wavevector, so it carries the longitudinal state; its coupling to the potential is proportional to $\nu_m$, so it decouples as $\nu_m\to0$ and takes the third state with it.

**What the device shows.** It is a rewriting of the same theory by a field redefinition, not a second theory, and it shows that the discontinuity of the solution space is a discontinuity of the **parametrisation**. In the parametrisation with $\xi$ the limit is continuous; in the parametrisation without it, the limit is a jump. The equation does not know about either, which is why the theorem could be stated for the equation alone.

### The readings

**The mass is the order parameter of a constraint.** Read on the theory, the theorem says that the Lorenz condition is not a property of the vector field but a property of the massive vector field. Add a mass and a gauge choice becomes a law; remove it and the law becomes a choice again. The direction of the implication is what carries the physics, and it is the reason the counting goes three to two rather than the other way round.

**The limit is a boundary and not an interior point.** The archive states the same thing twice in different variables. *The Massless Limit as a Boundary Value of the Polar Word* shows that the massless shell is the zero-divisor cone and that the limit is therefore taken to the boundary of the group of invertibles, where the polar word has no value: no sequence of parameters converges, because the limit point is not in the interior. The rank drop from four to two is the linear form of the same statement. A reader who expects a smooth family of solutions across $\nu_m=0$ is expecting the interior to be compact, and it is not.

**The restored symmetry is larger than gauge.** Gauge invariance is the visible restoration at $\nu_m=0$, and it is not the only one. The companion article *Conformal Invariance and the Massless Limit in Biquaternionic Form* shows that the mass is the single scale in $\Box_\Phi-4\pi^{2}\nu_m^{2}$, that it breaks the five additional conformal transformations, and that the massless limit is the limit in which a symmetry is restored with the mass as its order parameter. The gauge restoration proved above is one member of that family, and it is the one that the vector field exhibits without leaving the algebra.

**The equation is continuous and the kernel is not.** The principal symbol is independent of $\nu_m$, so the characteristic set — the cone — is the same at every mass. The support of the retarded kernel is therefore the same at every mass, while the number of states that can sit on the cone changes. This is the sharpest way to see why the theorem is about the equation: a propagation is a solution, and the solutions are what jump.

**The carrier does not move, the constraint does.** This is the framework's own reading, and it is the archive's. The sector $\mathbb{B}_{\Phi}$ is closed under the Proca operator for every material potential, so the massless and massive potentials share a home; what changes is which slice of that home the field is confined to. The category can therefore carry one entry for both theories, and it does: the Proca entry owns the massive constraint and the Maxwell entry owns the massless one, and the limit is the boundary between two entries of the same carrier.

**The limit says nothing about the particles.** The theorem relates two equations. Whether a given physical field is described by Proca or by Maxwell is a question about its mass, and the mass is empirical. The passage from the $W$ and $Z$ bosons to the photon is not a consequence of this section; what the section supplies is the equation that a massless spin-one field obeys, and the observation that its gauge freedom is not inherited but restored.

### What the theorem does not say

**It does not say that a sequence of Proca solutions converges to a Maxwell solution.** The limit of the equation is exact and the limit of the solutions is not, because the solution spaces have different dimensions. A sequence of Proca fields with $m_n\to0$ need not converge to a Maxwell field unless the longitudinal mode is controlled, and controlling it is what the Stueckelberg parametrisation does.

**It does not say that gauge invariance was already present at $\nu_m\neq0$.** It says that the symmetry appears at $\nu_m=0$ and is broken at every nonzero mass, and the breaking is the mass term.

**It does not say that the two theories are the same at $\nu_m\neq0$.** For every nonzero mass the Proca equation is not the Maxwell equation, the Lorenz condition is not a gauge choice, and the third polarisation is physical. The theorem is a statement about one point of the parameter space and about what is continuous through it.

**It does not decide the sign conventions.** The reduction is exact in the series convention and in the mostly-minus convention, because it deletes a term rather than moving one; the sign of the mass term and the sign of the d'Alembertian are fixed elsewhere, in *Algebra and Element Conventions*, and the theorem is insensitive to both.

## Reduction to the Klein–Gordon Equation

With the Lorenz condition the field strength is simply the conjugate gradient of the potential,

$$
S = 0 \qquad\Longrightarrow\qquad \tilde{F} = (\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi},
$$

and the Proca equation becomes

$$
\tilde\nabla_\Phi\tilde{F} = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi} = \Box_\Phi\tilde{A}_{\Phi} = 4\pi^{2}\nu_m^{2}\,\tilde{A}_{\Phi}.
$$

Hence

$$
\left(\Box_\Phi-4\pi^{2}\nu_m^{2}\right)\tilde{A}_{\Phi} = 0 ,
$$

the Klein–Gordon equation for the material potential. Because $\Box_\Phi$ is central and scalar, it acts on the four real coefficients of $\tilde{A}_{\Phi}$ separately, and the equation is the statement that each of them satisfies the scalar Klein–Gordon equation. **The four are the sector's, not the algebra's.** They are the time slot and the three vector slots of $\mathbb{B}_\Phi$; a potential with an informational part is not a solution of the Proca equation, and the count four is the carrier's count and not a freedom left over. The reduction is therefore exact and reversible: the Proca equation for $\tilde{A}_{\Phi}$ and the pair

$$
\boxed{\;\left(\Box_\Phi-4\pi^{2}\nu_m^{2}\right)\tilde{A}_{\Phi} = 0, \qquad \mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}\right) = 0\;}
$$

are equivalent. This is the biquaternion transcription of the standard statement that the Proca equation is equivalent to the Klein–Gordon equation together with the Lorenz condition.

### The component form

The same reduction can be followed component by component, which shows that nothing is hidden in the biquaternion product. Write $\tilde{A}_{\Phi} = A_te_t + \vec a$ and compute the scalar and vector parts of $\tilde\nabla_\Phi\tilde{F}$ with $\tilde{F}$ a pure vector of components $(F_x,F_y,F_z)$ obtained from $(\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}$. The scalar part is

$$
\mathrm{Sc}\!\left(\tilde\nabla_\Phi\tilde{F}\right) = \Delta_\Phi A_t - \partial/\partial R_t\,\mathrm{div}\,\vec a,
$$

and the vector part is

$$
\mathrm{Vect}\!\left(\tilde\nabla_\Phi\tilde{F}\right) = \left(\Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2\right)\vec a - \partial/\partial R_t\,\vec\nabla_\Phi A_t - \vec\nabla_\Phi\,\mathrm{div}\,\vec a.
$$

The Proca equation equates the first to $4\pi^{2}\nu_m^{2}A_t$ and the second to $4\pi^{2}\nu_m^{2}\vec a$. The Lorenz condition $\mathrm{div}\,\vec a = -\partial/\partial R_t\,A_t$ turns the scalar equation into $\Box_\Phi A_t = 4\pi^{2}\nu_m^{2}A_t$, and it makes the two gradient terms of the vector equation cancel one another, leaving $\Box_\Phi\vec a = 4\pi^{2}\nu_m^{2}\vec a$. Both components therefore reduce to the Klein–Gordon equation, and no residual term survives. The computation is the explicit check that the two routes to the reduction agree.

## Plane Waves and the Three Polarizations

### Dispersion relation

Write a plane-wave potential

$$
\tilde{A}_{\Phi} = \tilde{A}_{\Phi,0}\,\exp(-i\theta_{\mathrm{pwp}}), \qquad
\tilde{A}_{\Phi,0} = A_te_t + \vec a, \qquad
\tilde\Upsilon_{\Phi} = i\frac{\omega}{2\pi c}\,e_t + \vec\nu_\Phi,
$$

where $\tilde{A}_{\Phi,0}$ is a constant element of the material sector $\mathbb{B}_\Phi$, so that $A_t$ is purely imaginary and $\vec a$ is real, and $\theta_{\mathrm{pwp}}=\omega r'_t/c-2\pi\vec\nu_\Phi\cdot\vec r$ is the phase. Differentiation gives $\tilde\nabla_\Phi\tilde{A}_{\Phi} = 2\pi i\tilde\Upsilon_{\Phi}\tilde{A}_{\Phi}$ and $(\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi} = 2\pi i\tilde\Upsilon_{\Phi}^{\natural}\tilde{A}_{\Phi}$, and the Klein–Gordon operator acts as

$$
\Box_\Phi\,\exp(-i\theta_{\mathrm{pwp}}) = \left(\frac{\omega^2}{c^2} - 4\pi^{2}\vec\nu_\Phi^2\right)\exp(-i\theta_{\mathrm{pwp}}),
$$

as in the companion Klein–Gordon article. The Klein–Gordon equation therefore requires

$$
\boxed{\;\frac{\omega^2}{c^2} - 4\pi^{2}\vec\nu_\Phi^2 = 4\pi^{2}\nu_m^{2},
\qquad\text{i.e.}\qquad
\omega^2 = 4\pi^{2}c^{2}\left(\vec\nu_\Phi^{2} + \nu_m^{2}\right)\;},
$$

the physical relativistic dispersion relation.

The angle is $\theta_{\mathrm{pwp}}=\frac{2\pi p\cdot x}{h}=(\omega/c)r'_t-\vec\nu_\Phi\cdot\vec r$: the material four-wave-number paired with the material position. It is real, so the exponent is a phase and not a decay, and the plane wave is the corpus's $i r'_t$ convention applied to a free mode.

### The Lorenz condition on a plane wave

The scalar part of $(\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}$ is the scalar part of $2\pi i\tilde\Upsilon_{\Phi}^{\natural}\tilde{A}_{\Phi,0}$. Splitting $\tilde\Upsilon_{\Phi}^{\natural} = i\frac{\omega}{2\pi c}e_t - \vec\nu_\Phi$ and using $\vec\nu_\Phi\vec a = -\vec\nu_\Phi\cdot\vec a + \vec\nu_\Phi\times\vec a$,

$$
\mathrm{Sc}\!\left(2\pi i\tilde\Upsilon_{\Phi}^{\natural}\tilde{A}_{\Phi,0}\right)
= -\frac{\omega}{c}\,A_t + 2\pi i\,\vec\nu_\Phi\cdot\vec a,
$$

so that the Lorenz condition fixes the time component in terms of the spatial amplitude,

$$
A_t = 2\pi i\,\frac{c}{\omega}\,\vec\nu_\Phi\cdot\vec a.
$$

For real $\vec\nu_\Phi$ and real $\vec a$ this $A_t$ is purely imaginary, so the potential remains in the material sector $\mathbb{B}_{\Phi}$, as it must. No condition is placed on the direction of $\vec a$.

### Counting

The amplitude data are the three real components of $\vec a$. The time component is not independent: it is fixed by the Lorenz condition. The dispersion relation fixes $\omega$ for each $\vec\nu_\Phi$ but does not reduce the number of amplitudes. Hence a massive vector field has **three real polarization directions per wavevector**:

- two directions in the plane orthogonal to $\vec\nu_\Phi$, the transverse polarizations; and
- one direction along $\vec\nu_\Phi$, the **longitudinal** polarization.

The counting is linear in the field, so it is enough to test it on a general superposition. It is satisfied on a superposition of two independent plane waves with different wavevectors and amplitudes: the Proca equation $\tilde\nabla_\Phi\tilde{F}=4\pi^{2}\nu_m^{2}\tilde{A}_{\Phi}$ holds to round-off (residual at the level of $10^{-16}$ in units of the field amplitude), the Lorenz scalar vanishes to round-off for each component of the superposition, and the mass shell holds for each wavevector. A wave whose time component violates the Lorenz condition fails the equation by an amount of order the amplitude, as a separate substitution shows: the constraint is not optional.

### Contrast with the massless case

For $m = 0$ the dispersion relation becomes $\omega^2 = 4\pi^{2}c^{2}\vec\nu_\Phi^2$ and the Lorenz condition still fixes $A_t = 2\pi i(c/\omega)\vec\nu_\Phi\cdot\vec a$, but now the system has the residual gauge freedom $\tilde{A}_{\Phi}\to\tilde{A}_{\Phi}-\tilde\nabla_\Phi\Gamma$ with $\Box_\Phi\Gamma=0$. On a plane wave this freedom shifts the amplitude by a multiple of the four-wavevector, $\vec a\to\vec a+\digamma_{\mathrm{gau}}\vec\nu_\Phi$ and $A_t\to A_t+\digamma_{\mathrm{gau}}\,i\omega/c$, which removes exactly the longitudinal direction together with the time component; two real transverse directions remain. The massless field therefore has two real polarizations, and the massive field three. The third polarization is physical for the Proca field precisely because there is no gauge transformation to remove it, and the algebra exhibits this: the Lorenz condition is a consequence of the equation in the massive case and a choice in the massless one.

### The massless limit on a plane wave

The theorem of §*The Massless Limit: Proca at m = 0 Is Maxwell* is stated for the operator; on a plane wave it reads as a single sentence. An amplitude that satisfies the Proca equation at $\nu_m$ satisfies the Maxwell equation at $\nu_m=0$ once the mass shell is set to the null one, and the third direction that the mass makes physical is the direction that the residual gauge transformation removes at $\nu_m=0$. The Stueckelberg field of §*The Stueckelberg form, and the continuity of the parametrisation* is the device that keeps the count continuous across the jump, and it is treated there once.

## The Massive Field Strength and the Self-Dual Split

The companion article of this subcategory shows that the field-strength biquaternion lies in the complex three-dimensional vector part of the algebra and that the Hodge dual acts on it as $\star\tilde{F} = -i\tilde{F}$; the field-strength biquaternion of a real field carries the self-dual coordinate $\vec N = \vec E+ic\vec B$, on which the dual is $-i$, and the anti-self-dual coordinate is the conjugate combination $\vec N^* = \vec E-ic\vec B$, on which it is $+i$. That statement is a property of the vector part and holds for the Proca field as much as for the Maxwell field: the massive field strength is still a pure vector of the algebra, and the split is still available.

What the mass changes is not the split but the equation that the field strength satisfies. In the Maxwell case the source-free equation $\tilde\nabla_\Phi\tilde{F}=0$ makes the field strength harmonic, and the two helicities are the two halves. In the Proca case the equation is

$$
\tilde\nabla_\Phi\tilde{F} = 4\pi^{2}\nu_m^{2}\,\tilde{A}_{\Phi},
$$

so the field strength is not harmonic, and the potential — a material-sector four-vector, not a pure vector — appears on the right. The mass term is exactly a source term in the biquaternion Maxwell equation: it is the current that the massive field generates for itself. This is the algebraic form of the standard statement that the Proca field strength is not divergence-free and that the longitudinal mode is sourced by the mass.

The two helicities of the massless field are the labels of the two self-dual halves. For the massive field the two transverse polarizations survive as helicity $\pm1$ in the rest frame, but helicity is no longer a Lorentz-invariant label, because a boost can rotate a transverse polarization into the longitudinal one. The algebra does not decide this: it represents both the massless and the massive case on the same footing, and the presence or absence of the third polarization is an input, the value of $m$. This is the same structural situation that the companion article on the photon records for the massless case, read in the opposite direction.

## The Conserved Current and the Energy–Momentum Tensor

The massive field carries a conserved current and an energy–momentum tensor, and the review writes both in the same closed form in terms of the field strength and the potential:

$$
2\tilde{J}_{\Phi} = \tilde{A}_{\Phi}^{+}\tilde{F} + \tilde{F}^{+}\tilde{A}_{\Phi} + (\cdots)^{\sim},
\qquad
8\pi\,\mathcal{T}(\;) = \tilde{F}^{+}[\;]\tilde{F} + 4\pi^{2}\nu_m^{2}\,\tilde{A}_{\Phi}^{+}[\;]\tilde{A}_{\Phi} + (\cdots)^{\sim},
$$

where the slot in $\mathcal{T}$ takes an arbitrary biquaternion argument — marked by $[\;]$ inside the operator, as in the companion article on Maxwell's equations — the source's $+$ is the Hermitian conjugation, and $(\cdots)^{\sim}$ means that the expression is completed by adding the **reverse** of the part on the left. The completion is not decoration: it is what gives each object a definite order parity, since any part added to its own reversal is reversal-even by construction, and the source's conclusion is that the current and the energy–momentum are then "bireal and ordinal invariant four-vectors, as it should be". This is the same reversal-evenness that selects the Proca combination from the Lanczos parent below, and it is the object catalogued in *Comparison of the Remarkable Subspaces*.

Two points of notation, so that the display is not misread. The mass coefficient is the source's $m^2$, which is $4\pi^{2}\nu_m^{2}$ in the units of this article. And the same authors' 2001 comment prints the same current undoubled and with $\vec{b}$ — its name for the field strength — in place of $\tilde{F}$; the two formulas are one object in two notations.

The source adds one further statement, which the corpus records without re-deriving it: if the electromagnetic field is introduced — by either route, local gauge invariance or the minimum-coupling substitution — the divergence of the current still vanishes, while the divergence of $\mathcal{T}$ gives the **Lorentz force** acting on the particle. What is checked here is only the structure, that the completion rule makes the two objects reversal-even; that follows from the definition and needs no computation, whereas the two divergence statements are the source's.

## The Lanczos Parent and the Two Reversal Combinations

The Proca equation is one of four relativistic field equations that descend from a **single** first-order system. Lanczos's coupled system $\tilde\nabla_\Phi\tilde Q_1=m\tilde Q_2$, $\tilde\nabla_\Phi\tilde Q_2=m\tilde Q_1$ sits beneath the classical layer, and its descendants are reached by four different algebraic operations:

- the **Dirac** equation, by the idempotent superposition $D=\tilde Q_1\sigma+\tilde Q_2^{*}\bar{\sigma}$ of the standard-model article article, whose combined form is strictly equivalent to Dirac's equation;
- the **Proca** equation, by combining the second Lanczos equation with its **order reverse** (its ordinal conjugate), the potential being ordinal-invariant, $\tilde{A}_{\Phi}=\tilde{A}_{\Phi}^{\sim}$;
- the **Maxwell** equation, as the massless limit of Proca;
- the **Klein–Gordon** equation, as the spin-0 member, by restricting the pair to scalar fields (see *The Klein–Gordon Equation in Biquaternionic Form*: one-dimensional in its first-order form, the four-dimensional free scalar equation after the elimination).

The observation is due to Gsponer and Hurni, and it is sharper than the list suggests. Combining the equation with its own order reverse gives not two independent equations but the two **reversal parities** of one. In the source's notation, with $\vec\nabla_\Phi$ the biquaternionic gradient, $\tilde{F}^{\sim}$ the order reverse of the field strength and the second gradient acting to the right,

$$
\tfrac12\left(\vec\nabla_\Phi\tilde{F} + \tilde{F}^{\sim}\vec\nabla_\Phi\right) = 4\pi^{2}\nu_m^{2} A ,
\qquad
\tfrac12\left(\vec\nabla_\Phi\tilde{F} - \tilde{F}^{\sim}\vec\nabla_\Phi\right) = 0 .
$$

The **reversal-even** combination is Proca's equation; the **reversal-odd** combination is the vanishing of the odd source. The mass term is reversal-even and that constraint is reversal-odd, so the two are halves of one equation, and the Maxwell equation of the companion article is what remains when the even half is massless. The splitting requires the potential to be ordinal-invariant — this is the assumption the source notes is made silently when Maxwell's equation is first written — and it is the same assumption under which the field strength is the vector part of the conjugate gradient of the potential.

### The two parities and the two massive particles

The reversal split also classifies the massive particles, and it does so in the same breath as the classification of the massless ones. The source's assumption for Proca is that the potential is reversal-**even**, $\tilde{A}_{\Phi}=+\tilde{A}_{\Phi}^{\sim}$, which is the corpus's statement that $\tilde{A}_{\Phi}$ is a genuine four-vector. Taking instead $\tilde{A}_{\Phi}=-\tilde{A}_{\Phi}^{\sim}$ — a reversal-odd potential, the pseudovector case — gives another fully covariant equation differing from Proca's only in the **sign of the mass term**. The massive vector and the massive pseudovector are the two reversal parities of one descendant, exactly as their massless counterparts are.

This is Gürsey's theorem, restated: the wave equations of **all** scalar and vector particles, and of all pseudo-scalar and pseudo-vector particles, are degenerate cases of Lanczos's fundamental equation. The framework does not need a separate first-order system for each spin-and-parity assignment; the one system contains them, distinguished by the reversal parity of the potential and by which superposition of the two fields is taken.

### What the parent explains

Three things that look like separate axioms become one.

- **Why the Proca equation and the corpus's Maxwell equation share their left-hand side.** They are the same descendant in massive and massless form; the mass touches only the right-hand side, which is why the two equations differ there and nowhere else.
- **Why the vanishing of the odd source is not an independent law.** It is the reversal-odd part of the same equation, not a second equation imposed on the field from outside.
- **Why the classical layer has so few first-order systems.** Dirac, Proca, Maxwell and the massive pseudovector all reduce to Lanczos's pair; the algebra's classical equations are one family and not an unrelated list.

What the parent does **not** do is fix the mass. The Lanczos parameter $m$ and the Einstein–Mayer mass biquaternion of the companion article on the Petiau system are inputs of the parent system, and the algebra supplies no value for either.

## What Is Standard and What the Algebra Adds

The separation is worth stating explicitly, because the Proca equation is standard physics and the framework's contribution is a rewriting.

**The standard part.** The Proca Lagrangian, the equation of motion, the derivation of the Lorenz condition by contraction, the reduction to the Klein–Gordon equation, the dispersion relation, the count of three polarizations, and the conserved current and energy–momentum tensor are textbook field theory, transcribed here into the notation of the series. Nothing in the transcription changes them.

**The algebra's part.** The framework gives three compact statements that the index notation only implies. First, the field strength is the vector part of the conjugate gradient of the potential, and the Lorenz condition is the statement that the scalar part of that product vanishes; the constraint is thus the vanishing of the scalar part of a single biquaternion. Second, the divergence argument that derives the constraint is the observation that the d'Alembertian is central and scalar and that the field strength is a pure vector, so the scalar part of $\Box_\Phi\tilde{F}$ vanishes identically. Third, the Hodge dual is minus left multiplication by the scalar imaginary, so the self-dual split of the field strength is a statement about the algebra's complex structure and survives the addition of a mass.

**What is imported.** The identification of the field with a particle of spin one, the value of the mass, and the **physical interpretation** of the three polarizations are inputs. The framework represents them; it does not derive them. The canonical quantisation of the Proca field, its propagator, and its constraint algebra belong to the field-theoretic companion subcategory and are not treated here.

The conventions are those of three companion articles:

- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the scalar equation to which the Proca field reduces, and for the plane-wave convention used here.
- Companion article *Maxwell's Equations in the Biquaternionic Formulation*, for the massless equation, the potential and field-strength biquaternions, and the gauge structure.
- Companion article *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Bivector Plane*, for the Hodge dual and the split of the field strength on the vector part of the algebra.

## Summary

The Proca equation for a massive spin-one field is written in the biquaternion framework as the single equation

$$
\tilde\nabla_\Phi\tilde{F} = 4\pi^{2}\nu_m^{2}\,\tilde{A}_{\Phi},
\qquad
\tilde{F} = (\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi} - \mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}\right),
$$

with $\tilde{A}_{\Phi}\in\mathbb{B}_{\Phi}$ and $\tilde{F}\in\mathbb{B}_{V}$. Unlike the massless Maxwell equation, it is not gauge invariant: the mass term couples the potential to itself, and the gauge freedom of the massless theory is absent.

The divergence of the equation is not an identity. Applying $(\tilde\nabla_\Phi)^{\natural}$ and taking the scalar part, the d'Alembertian is central and scalar, the field strength is a pure vector, and the left-hand side vanishes identically; the mass then forces the **Lorenz condition** $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi})=0$ as a consequence of the equation of motion. With the constraint in hand, the field strength is the conjugate gradient of the potential and the equation reduces to the Klein–Gordon equation $(\Box_\Phi-4\pi^{2}\nu_m^{2})\tilde{A}_{\Phi}=0$ for each component. The two together — Klein–Gordon and Lorenz — are equivalent to the Proca equation.

The plane-wave solutions carry a real spatial amplitude and a time component fixed by the Lorenz condition, with the dispersion relation $\omega^2 = 4\pi^{2}c^{2}\left(\vec\nu_\Phi^{2} + \nu_m^{2}\right)$. The three real components of the spatial amplitude are the three polarizations: two transverse and one longitudinal. The longitudinal mode is physical because there is no gauge freedom to remove it; in the massless limit the residual gauge transformation removes exactly that mode and leaves the two transverse polarizations. The field strength remains a pure vector of the algebra and so retains the self-dual split of the companion article — it carries the self-dual coordinate $\vec N=\vec E+ic\vec B$ of the real field — but it is not harmonic, and the mass term is precisely the source that the biquaternion Maxwell equation requires.

The massless limit is an exact reduction and not an approximation. At $\nu_m=0$ the Proca density is the Maxwell density, the Proca equation is the source-free Maxwell equation, and the biquaternion equation $\tilde\nabla_\Phi\tilde{F}=4\pi^{2}\nu_m^{2}\tilde{A}_{\Phi}$ is $\tilde\nabla_\Phi\tilde{F}=0$, with the same field strength and the same operator on the left. What changes is the constraint structure: the Lorenz condition is forced by the equation for $\nu_m\neq0$ and becomes a gauge choice at $\nu_m=0$, the count of polarisations falls from three to two, and gauge invariance emerges as the mass term — the only term built from the potential — is deleted. The Stueckelberg form restores the continuity of the limit by carrying the longitudinal mode in a scalar that decouples as $\nu_m\to0$, which shows that the discontinuity lies in the parametrisation and not in the equation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_{\imath}^2=-e_t$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{B}_{V}$ | Complex three-dimensional vector part |
| $\tilde\nabla_\Phi, (\tilde\nabla_\Phi)^{\natural}$ | Biquaternionic gradient and conjugate, $\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Delta_\Phi - \partial^2/\partial {r^{\prime}_t}^2$ |
| $\tilde{A}_{\Phi} = i\,a'_t\,e_t + \vec A$ | Four-potential biquaternion in $\mathbb{B}_{\Phi}$ |
| $\tilde{F} = (\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi}-\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi})$ | Field-strength biquaternion, pure vector |
| $S = \mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{A}_{\Phi})$ | Gauge scalar; the Proca equation forces $S=0$ (Lorenz condition) |
| $1/(2\pi\nu_m)$ | The mass length, $\frac{1}{2\pi\nu_m}$; its reciprocal, up to the factor $2\pi$, is the mass wave number, $\nu_m=\frac{m\,c}{h}$, and the squared coefficient is $\nu_m^{2}=\frac{m^{2}c^{2}}{h^{2}}$ |
| $\tilde P_{\Phi} = h\left(i\frac{\omega}{2\pi c}\,e_t + \vec\nu_\Phi\right)$ | Four-wavevector biquaternion, $h\tilde\Upsilon_{\Phi}$ |
| $\omega^2 = 4\pi^{2}c^{2}\left(\vec\nu_\Phi^{2} + \nu_m^{2}\right)$ | Massive dispersion relation |
| $\vec a$, $A_t$ | Spatial amplitude (three real components) and time component fixed by Lorenz |
| $\star\tilde{F} = -i\tilde{F}$ | Hodge dual on the field strength (companion article) |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_{\imath}\lvert Q_{2\imath}\rvert^{2}$ |

## Further Reading

- [Introduction to the Spin-One Anti-Hermitian Subspace](the-spin-one-anti-hermitian-subspace.html), for the material sector as the carrier of the potential, the residual identity that closes it, and the charge that it cannot carry.
- [The Massless Regime](the-massless-regime.html), for the massless shell as the zero-divisor cone and the limit as a boundary value of the polar word rather than an interior limit.
- [Conformal Invariance and the Massless Limit in Biquaternionic Form](conformal-invariance-and-the-massless-limit-in-biquaternionic-form.html), for the mass as the single scale in $\Box_\Phi-4\pi^{2}\nu_m^{2}$, the five conformal symmetries that it breaks, and the rank drop of left multiplication by the on-shell symbol.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html), for the massless equation that the limit recovers and for the gauge transformation used in the reduction.
- Alexandre Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs", *Journal de Physique et le Radium* 7 (1936) 347–353, for the original massive vector field equation.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the massive vector field, its constraint, and the counting of its polarizations.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Proca Lagrangian, the propagator, and the massless limit.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the constraint analysis of massive vector fields and the role of the Lorenz condition.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the massive vector field in the classical theory and the physical third polarization.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the massless limit, the gauge freedom, and the transverse polarizations.
- Walter Greiner and Joachim Reinhardt, *Field Quantization* (Springer, 1996), for the canonical treatment of the Proca field and its three polarization states.
- A. Gsponer and J.-P. Hurni, "The physical heritage of Sir W. R. Hamilton," arXiv:math-ph/0201058, §9, for the derivation of Proca's equation from Lanczos's coupled system by the reversal-even combination, for the identification of the reversal-odd combination with the vanishing of the odd source, and for the conserved current and the energy–momentum tensor in closed quaternion form (46)–(47).
- A. Gsponer and J.-P. Hurni, "Comment on formulating and generalizing Dirac's, Proca's, and Maxwell's equations with biquaternions or Clifford numbers," arXiv:math-ph/0201049, *Foundations of Physics Letters* **14** (2001) 77–85, for the spin-0 and spin-1 members of the Lanczos family, the Einstein–Mayer hypercomplex mass, and the same current and energy–momentum tensor printed undoubled in the $\vec{b}$ notation.
- C. Lanczos, "Die tensoranalytischen Beziehungen der Diracschen Gleichung," *Zeitschrift für Physik* **57** (1929) 447–473, 474–483, 484–493 (arXiv:physics/0508002, physics/0508012, physics/0508013), for the coupled biquaternion system from which the Dirac and Proca equations both descend.
- F. Gürsey, "Applications of quaternions to field equations," PhD thesis, University of London, 1950, for the classification of the scalar, vector, pseudoscalar and pseudovector equations as degenerate cases of Lanczos's fundamental equation.
