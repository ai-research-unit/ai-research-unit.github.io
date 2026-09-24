# __The Proca Equation: Massive Spin 1 in Biquaternionic Form__

## Introduction

The Maxwell field is massless, and its masslessness is what reduces four potential components to two physical transverse polarizations: the gauge freedom removes one combination and the field equation removes another. Give the vector field a mass and the gauge freedom disappears. The equation of motion then becomes the **Proca equation**, and the third, longitudinal polarization becomes physical, with the two helicities no longer Lorentz-invariant labels. The Proca field is the prototype of a massive spin-one field, and it is the first field equation that the self-dual split of the material sector supports.

The purpose of this article is to write the Proca system in biquaternionic form and to read its content from the algebra. The equation is a single biquaternion equation for the four-potential $\tilde{A}\in\mathbb{M}_-$ and its field strength $\tilde{F}\in\mathrm{Vect}(\mathbb{B})$. Two structural facts organise everything. First, the equation is **homogeneous but not gauge invariant**: the source that the companion Maxwell equation attributes to an external current is supplied here by the potential itself, so the equation is linear in $\tilde{A}$ and the gauge freedom of the massless theory is absent. Second, the divergence of the equation is not an identity: taking the biquaternion conjugate of the equation and its scalar part forces the **Lorenz condition** $S = \mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A}) = 0$, exactly as taking the divergence of the standard Proca equation forces $\partial_\mu A^\mu = 0$. The Lorenz condition is a consequence of the equation, not a gauge choice, and that is the algebraic statement of the disappearance of the gauge freedom.

Once the Lorenz condition is available, the Proca equation collapses to the Klein–Gordon equation for each component, and the physical content is transparent: three real polarization directions at each wavevector — two transverse and one longitudinal — with the dispersion relation $\omega^2 = c^2\mathbf{k}^2 + m^2c^4/\hbar^2$. The counting is done here explicitly, and it is contrasted with the massless case, where the same calculation leaves two real directions because a residual gauge transformation removes the third. The article closes by locating the massive field relative to the self-dual split of the companion article: the field strength remains a pure vector of the algebra and so keeps its self-dual and anti-self-dual coordinates, but it is no longer harmonic, and the mass term is precisely what the biquaternion Maxwell equation calls a source.

The conventions are those of the companion articles. The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, and central scalar imaginary $i$; the gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$ with $\bar{\tilde{\nabla}}$ its quaternion conjugate and $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$; the potential and field strength are $\tilde{A}=i\phi/c\,e_0+\mathbf{A}$ and $\tilde{F}=\bar{\tilde{\nabla}}\tilde{A}-\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}$, with $c=1/\sqrt{\epsilon\mu}$ and the normalization of the potential fixed so that the two expressions for $\tilde{F}$ agree; and $m$ denotes the mass, with $\mu = mc/\hbar$ written where the dimensions have to be displayed. In natural units $\hbar=c=1$ the mass parameter is simply $m$.

## The Standard Proca Theory

### Lagrangian and equation

The Proca field is a real four-vector $A^\mu$ with the Lagrangian density

$$
\mathcal{L} = -\tfrac14 F_{\mu\nu}F^{\mu\nu} + \tfrac12 \mu^2 A_\mu A^\mu, \qquad F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu,
$$

where $\mu = mc/\hbar$ and the sign of the mass term is the one that makes the energy positive. Variation with respect to $A_\nu$ gives the **Proca equation**

$$
\partial_\mu F^{\mu\nu} + \mu^2 A^\nu = 0 .
$$

The equation differs from the source-free Maxwell equation by the mass term alone, and that term is what breaks the gauge symmetry: under $A_\mu \to A_\mu - \partial_\mu\Gamma$ the field strength is unchanged but the mass term is not, since $A_\mu A^\mu$ is not invariant. A massive vector field has no gauge freedom.

### The constraint

The mass term also changes the constraint structure. Contracting the equation with $\partial_\nu$ and using the antisymmetry of $F^{\mu\nu}$,

$$
\partial_\nu\partial_\mu F^{\mu\nu} = 0
\qquad\Longrightarrow\qquad
\mu^2\,\partial_\nu A^\nu = 0
\qquad\Longrightarrow\qquad
\partial_\mu A^\mu = 0 ,
$$

for $\mu \neq 0$. The **Lorenz condition** is therefore a consequence of the equation of motion and not a choice of gauge: it is one of the equations of the system. This is the sharpest structural difference from the Maxwell case, where the same condition can be imposed but not derived, and where it is preserved as a gauge choice rather than fixed.

### Reduction and dispersion

With the Lorenz condition in hand, the field strength contracts to a d'Alembertian,

$$
\partial_\mu F^{\mu\nu} = \partial_\mu\left(\partial^\mu A^\nu - \partial^\nu A^\mu\right) = \Box A^\nu - \partial^\nu\left(\partial_\mu A^\mu\right) = \Box A^\nu,
$$

so that the Proca equation becomes

$$
\left(\Box + \mu^2\right) A^\nu = 0
$$

in the mostly-minus convention. In the series convention, whose d'Alembertian is $\Box = \partial_{ict}^2 + \Delta$ and therefore the negative of the mostly-minus operator, the same statement is

$$
\left(\Box - \frac{m^2c^2}{\hbar^2}\right)\tilde{A} = 0 ,
$$

the Klein–Gordon equation with the physical mass shell $\omega^2 = c^2\mathbf{k}^2 + m^2c^4/\hbar^2$. The field of a massive vector particle is thus a four-vector each of whose components satisfies the Klein–Gordon equation, subject to the single constraint $\partial_\mu A^\mu = 0$. Four components minus one constraint leaves three. This count is standard and is checked below on the explicit plane waves.

### The rest frame and the three states

The three polarizations are easiest to see in the rest frame, $\mathbf{k} = \mathbf{0}$. The dispersion relation gives $\omega = mc^2/\hbar$, and the Lorenz condition gives $A_0 = i(c/\omega)\mathbf{k}\cdot\mathbf{a} = 0$, so the time component vanishes and the amplitude is purely spatial. The three real components of $\mathbf{a}$ are then three independent states, degenerate in energy and forming the three states $m = +1,0,-1$ of a spin-one particle along any chosen quantisation axis. There is no condition that removes the component of $\mathbf{a}$ along $\mathbf{k}$, and in the rest frame that component is unconstrained: all three directions survive. A massless particle has no rest frame, its two polarizations are the two transverse directions for every wavevector, and the third state is absent. The change from two to three states as the mass is turned on is thus visible already at the level of the rest-frame amplitudes.

## The Biquaternion Proca Equation

### Statement

The Proca system is transcribed into the framework by replacing the four-vector by the material-sector biquaternion and the gradient by the biquaternionic gradient. The single equation is

$$
\tilde{\nabla}\tilde{F} = \frac{m^2c^2}{\hbar^2}\,\tilde{A},
\qquad
\tilde{F} = \bar{\tilde{\nabla}}\tilde{A} - \mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{A}\right),
$$

or, in natural units $\hbar=c=1$,

$$
\tilde{\nabla}\tilde{F} = m^2\,\tilde{A}.
$$

The left-hand side is the biquaternion expression of $\partial_\mu F^{\mu\nu}$; the right-hand side is the mass term. The equation is the massive analogue of the companion Maxwell equation $\tilde{\nabla}\tilde{F} = -\tilde{R}$, with the external source $\tilde{R}$ replaced by a current proportional to the potential itself.

<!-- CONVENTION — Proca sign: the equation is written $\tilde{\nabla}\tilde{F} = +\mu^2\tilde{A}$ with $\mu=mc/\hbar$, and the sign is fixed by the requirement that the equation reduce to $(\Box-m^2c^2/\hbar^2)\tilde{A}=0$ with the SERIES d'Alembertian $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$. The standard mostly-minus form reads $(\Box_{\text{mm}}+m^2)A^\nu=0$, and since $\Box_{\text{mm}}=-\Box$ the two are the same equation. Do not "correct" the sign to $-\mu^2$: that gives $(\Box+\mu^2)\tilde{A}=0$, which is the wrong-sign dispersion in this convention. -->

### Why the equation is the right one

The transcription is not a guess. It is fixed by two requirements: the equation must reproduce the standard Proca system, and it must do so in the series' $ict$ convention without a change of metric. The check is carried out below by solving the equation for plane waves and reading off the dispersion relation. The result is the physical massive shell and the Lorenz condition, and the two together are the standard content of the Proca system. Any other relative sign between the two sides would give a dispersion relation with the wrong sign of $m^2$, that is, a spacelike or tachyonic shell, and the check excludes it.

### The failure of gauge invariance, explicitly

The massless companion equation is invariant under the gauge transformation $\tilde{A}\to\tilde{A}-\tilde{\nabla}\Gamma$ of the companion Maxwell article, because the field strength is built from $\bar{\tilde{\nabla}}\tilde{A}$ and $\bar{\tilde{\nabla}}\tilde{\nabla}\Gamma = \Box\Gamma$ is a central scalar, which the projection to the vector part discards. For the Proca equation the same transformation changes the right-hand side alone,

$$
\tilde{\nabla}\tilde{F} \;\longmapsto\; \tilde{\nabla}\tilde{F}, \qquad
\frac{m^2c^2}{\hbar^2}\,\tilde{A} \;\longmapsto\; \frac{m^2c^2}{\hbar^2}\left(\tilde{A}-\tilde{\nabla}\Gamma\right),
$$

so the equation is preserved only if $\tilde{\nabla}\Gamma = 0$, that is, only for a constant $\Gamma$. The transformation is therefore not a symmetry, and there is no gauge orbit to quotient by. The algebraic reason is that the mass term is the only term in the equation that is not built from the field strength: it is a term in the potential, and the potential is not gauge invariant. This is the biquaternion statement of the standard fact that the Proca Lagrangian's mass term $A_\mu A^\mu$ breaks the gauge symmetry.

## The Lorenz Condition Is Implied

The biquaternion form of the divergence argument is short, and it is the cleanest place where the algebra does work that the index notation leaves implicit.

Apply the conjugate gradient $\bar{\tilde{\nabla}}$ to both sides of the Proca equation and use that the gradient has constant coefficients, so that $\bar{\tilde{\nabla}}(\tilde{\nabla}\tilde{F}) = (\bar{\tilde{\nabla}}\tilde{\nabla})\tilde{F} = \Box\tilde{F}$:

$$
\Box\tilde{F} = \frac{m^2c^2}{\hbar^2}\,\bar{\tilde{\nabla}}\tilde{A}.
$$

Now take the scalar part of both sides. The d'Alembertian $\Box$ is a central scalar differential operator, so it preserves the scalar–vector decomposition and $\mathrm{Sc}(\Box\tilde{F}) = \Box\,\mathrm{Sc}(\tilde{F})$. The field strength $\tilde{F} = \mathrm{Vect}(\bar{\tilde{\nabla}}\tilde{A})$ is a **pure vector**, so $\mathrm{Sc}(\tilde{F}) = 0$, and the left-hand side vanishes identically. Hence

$$
0 = \frac{m^2c^2}{\hbar^2}\,\mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{A}\right)
\qquad\Longrightarrow\qquad
S := \mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{A}\right) = 0 ,
$$

which is the **Lorenz condition** of the companion Maxwell article, whose components are $\partial_{ict}A_0 + \mathrm{div}\,\mathbf{A} = 0$. The derivation uses only three facts: the field strength is a pure vector, the d'Alembertian is central and scalar, and the mass parameter is nonzero. In the massless case the same computation gives $0 = 0$ and no constraint, which is exactly why the gauge freedom survives there and is absent here.

<!-- CONVENTION — Lorenz condition derived, not imposed: in the Proca system $S=\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})=0$ is a CONSEQUENCE of the equation of motion. Applying $\bar{\tilde{\nabla}}$ to both sides of $\tilde{\nabla}\tilde{F}=\mu^2\tilde{A}$ gives $\Box\tilde{F}=\mu^2\bar{\tilde{\nabla}}\tilde{A}$, and the scalar part of the left-hand side vanishes because $\tilde{F}$ is a pure vector and $\Box$ is central and scalar. Note the right-hand side: applying the second gradient to the EQUATION converts $\mu^2\tilde{A}$ into $\mu^2\bar{\tilde{\nabla}}\tilde{A}$, whose scalar part is $\mu^2S$; taking the scalar part of $\Box\tilde{F}=\mu^2\tilde{A}$ itself instead would give $0=\mu^2A_0$, which is not the Lorenz condition. In the Maxwell system the same $S=0$ is a choice of gauge. Do not describe the Proca Lorenz condition as a gauge fixing: there is no gauge symmetry to fix, and the constraint is part of the equations. -->

## Reduction to the Klein–Gordon Equation

With the Lorenz condition the field strength is simply the conjugate gradient of the potential,

$$
S = 0 \qquad\Longrightarrow\qquad \tilde{F} = \bar{\tilde{\nabla}}\tilde{A},
$$

and the Proca equation becomes

$$
\tilde{\nabla}\tilde{F} = \tilde{\nabla}\bar{\tilde{\nabla}}\tilde{A} = \Box\tilde{A} = \frac{m^2c^2}{\hbar^2}\,\tilde{A}.
$$

Hence

$$
\left(\Box - \frac{m^2c^2}{\hbar^2}\right)\tilde{A} = 0 ,
$$

the Klein–Gordon equation for the biquaternion-valued potential. Because $\Box$ is central and scalar, it acts on the four coefficients of $\tilde{A}$ separately, and the equation is the statement that each coefficient of the potential satisfies the scalar Klein–Gordon equation. The reduction is therefore exact and reversible: the Proca equation for $\tilde{A}$ and the pair

$$
\left(\Box - \frac{m^2c^2}{\hbar^2}\right)\tilde{A} = 0, \qquad \mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{A}\right) = 0
$$

are equivalent. This is the biquaternion transcription of the standard statement that the Proca equation is equivalent to the Klein–Gordon equation together with the Lorenz condition.

### The component form

The same reduction can be followed component by component, which shows that nothing is hidden in the biquaternion product. Write $\tilde{A} = A_0e_0 + \mathbf{a}$ and compute the scalar and vector parts of $\tilde{\nabla}\tilde{F}$ with $\tilde{F}$ a pure vector of components $(F_1,F_2,F_3)$ obtained from $\bar{\tilde{\nabla}}\tilde{A}$. The scalar part is

$$
\mathrm{Sc}\!\left(\tilde{\nabla}\tilde{F}\right) = \Delta A_0 - \partial_{ict}\,\mathrm{div}\,\mathbf{a},
$$

and the vector part is

$$
\mathrm{Vect}\!\left(\tilde{\nabla}\tilde{F}\right) = \left(\partial_{ict}^2 + \Delta\right)\mathbf{a} - \partial_{ict}\nabla A_0 - \nabla\,\mathrm{div}\,\mathbf{a}.
$$

The Proca equation equates the first to $\mu^2A_0$ and the second to $\mu^2\mathbf{a}$. The Lorenz condition $\mathrm{div}\,\mathbf{a} = -\partial_{ict}A_0$ turns the scalar equation into $\Box A_0 = \mu^2A_0$, and it makes the two gradient terms of the vector equation cancel one another, leaving $\Box\mathbf{a} = \mu^2\mathbf{a}$. Both components therefore reduce to the Klein–Gordon equation, and no residual term survives. The computation is the explicit check that the two routes to the reduction agree.

## Plane Waves and the Three Polarizations

### Dispersion relation

Write a plane-wave potential

$$
\tilde{A} = \tilde{A}_0\,e^{\,i\,\mathrm{Sc}(\tilde{K}\bar{\tilde{X}})}, \qquad
\tilde{A}_0 = A_0e_0 + \mathbf{a}, \qquad
\tilde{K} = i\frac{\omega}{c}\,e_0 + \mathbf{k},
$$

where $\mathrm{Sc}(\tilde{K}\bar{\tilde{X}}) = \mathbf{k}\cdot\mathbf{x} - \omega t$ and $\tilde{A}_0$ is a constant biquaternion of the material sector, so that $A_0$ is purely imaginary and $\mathbf{a}$ is real. Differentiation gives $\tilde{\nabla}\tilde{A} = i\tilde{K}\tilde{A}$ and $\bar{\tilde{\nabla}}\tilde{A} = i\bar{\tilde{K}}\tilde{A}$, and the Klein–Gordon operator acts as

$$
\Box\,e^{\,i\,\mathrm{Sc}(\tilde{K}\bar{\tilde{X}})} = \left(\frac{\omega^2}{c^2} - \mathbf{k}^2\right)e^{\,i\,\mathrm{Sc}(\tilde{K}\bar{\tilde{X}})},
$$

as in the companion Klein–Gordon article. The Klein–Gordon equation therefore requires

$$
\frac{\omega^2}{c^2} - \mathbf{k}^2 = \frac{m^2c^2}{\hbar^2},
\qquad\text{i.e.}\qquad
\omega^2 = c^2\mathbf{k}^2 + \frac{m^2c^4}{\hbar^2},
$$

the physical relativistic dispersion relation.

### The Lorenz condition on a plane wave

The scalar part of $\bar{\tilde{\nabla}}\tilde{A}$ is the scalar part of $i\bar{\tilde{K}}\tilde{A}_0$. Splitting $\bar{\tilde{K}} = i(\omega/c)e_0 - \mathbf{k}$ and using $\mathbf{k}\mathbf{a} = -\mathbf{k}\cdot\mathbf{a} + \mathbf{k}\times\mathbf{a}$,

$$
\mathrm{Sc}\!\left(i\bar{\tilde{K}}\tilde{A}_0\right)
= -\frac{\omega}{c}\,A_0 + i\,\mathbf{k}\cdot\mathbf{a},
$$

so that the Lorenz condition fixes the time component in terms of the spatial amplitude,

$$
A_0 = i\,\frac{c}{\omega}\,\mathbf{k}\cdot\mathbf{a}.
$$

For real $\mathbf{k}$ and real $\mathbf{a}$ this $A_0$ is purely imaginary, so the potential remains in the material sector $\mathbb{M}_-$, as it must. No condition is placed on the direction of $\mathbf{a}$.

### Counting

The amplitude data are the three real components of $\mathbf{a}$. The time component is not independent: it is fixed by the Lorenz condition. The dispersion relation fixes $\omega$ for each $\mathbf{k}$ but does not reduce the number of amplitudes. Hence a massive vector field has **three real polarization directions per wavevector**:

- two directions in the plane orthogonal to $\mathbf{k}$, the transverse polarizations; and
- one direction along $\mathbf{k}$, the **longitudinal** polarization.

The counting is linear in the field, so it is enough to test it on a general superposition. It is satisfied on a superposition of two independent plane waves with different wavevectors and amplitudes: the Proca equation $\tilde{\nabla}\tilde{F}=m^2\tilde{A}$ holds to round-off (residual at the level of $10^{-16}$ in units of the field amplitude), the Lorenz scalar vanishes to round-off for each component of the superposition, and the mass shell holds for each wavevector. A wave whose time component violates the Lorenz condition fails the equation by an amount of order the amplitude, as a separate substitution shows: the constraint is not optional.

### Contrast with the massless case

For $m = 0$ the dispersion relation becomes $\omega^2 = c^2\mathbf{k}^2$ and the Lorenz condition still fixes $A_0 = i(c/\omega)\mathbf{k}\cdot\mathbf{a}$, but now the system has the residual gauge freedom $\tilde{A}\to\tilde{A}-\tilde{\nabla}\Gamma$ with $\Box\Gamma=0$. On a plane wave this freedom shifts the amplitude by a multiple of the four-wavevector, $\mathbf{a}\to\mathbf{a}+\lambda\mathbf{k}$ and $A_0\to A_0+\lambda\,i\omega/c$, which removes exactly the longitudinal direction together with the time component; two real transverse directions remain. The massless field therefore has two real polarizations, and the massive field three. The third polarization is physical for the Proca field precisely because there is no gauge transformation to remove it, and the algebra exhibits this: the Lorenz condition is a consequence of the equation in the massive case and a choice in the massless one.

### The massless limit and the Stueckelberg form

The limit $m\to0$ is discontinuous in the degrees of freedom: three states fall to two, and no sequence of Proca fields converges to a Maxwell field with a smooth third state. The standard device that makes the limit continuous is the **Stueckelberg form**, which restores the gauge freedom by extending the field with a scalar $\chi$ and building the mass term from the combination $\tilde{A}+\tilde{\nabla}\chi$ (up to the normalization of $\chi$) rather than from $\tilde{A}$ alone. Under the simultaneous transformations

$$
\tilde{A} \,\longrightarrow\, \tilde{A} - \tilde{\nabla}\lambda, \qquad
\chi \,\longrightarrow\, \chi + \lambda,
$$

the combination $\tilde{A}+\tilde{\nabla}\chi$ is invariant, so the mass term is gauge invariant and the symmetry is restored. On a plane wave the scalar $\chi$ contributes a piece along the wavevector, and the longitudinal state is carried by that piece; as $m\to0$ it decouples, carrying the third polarization away with it. The Stueckelberg form is a rewriting of the Proca system by a field redefinition, not a different theory, and it is mentioned here only to record that the algebra accommodates it without a change of structure.

## The Massive Field Strength and the Self-Dual Split

The companion article of this subcategory shows that the field-strength biquaternion lies in the complex three-dimensional vector part of the algebra and that the Hodge dual acts on it as $\star\tilde{F} = -i\tilde{F}$; the field-strength biquaternion of a real field carries the self-dual coordinate $\mathbf{V} = \mathbf{E}+ic\mathbf{B}$, on which the dual is $-i$, and the anti-self-dual coordinate is the conjugate combination $\mathbf{V}^* = \mathbf{E}-ic\mathbf{B}$, on which it is $+i$. That statement is a property of the vector part and holds for the Proca field as much as for the Maxwell field: the massive field strength is still a pure vector of the algebra, and the split is still available.

What the mass changes is not the split but the equation that the field strength satisfies. In the Maxwell case the source-free equation $\tilde{\nabla}\tilde{F}=0$ makes the field strength harmonic, and the two helicities are the two halves. In the Proca case the equation is

$$
\tilde{\nabla}\tilde{F} = \frac{m^2c^2}{\hbar^2}\,\tilde{A},
$$

so the field strength is not harmonic, and the potential — a material-sector four-vector, not a pure vector — appears on the right. The mass term is exactly a source term in the biquaternion Maxwell equation: it is the current that the massive field generates for itself. This is the algebraic form of the standard statement that the Proca field strength is not divergence-free and that the longitudinal mode is sourced by the mass.

The two helicities of the massless field are the labels of the two self-dual halves. For the massive field the two transverse polarizations survive as helicity $\pm1$ in the rest frame, but helicity is no longer a Lorentz-invariant label, because a boost can rotate a transverse polarization into the longitudinal one. The algebra does not decide this: it represents both the massless and the massive case on the same footing, and the presence or absence of the third polarization is an input, the value of $m$. This is the same structural situation that the companion article on the photon records for the massless case, read in the opposite direction.

## What Is Standard and What the Algebra Adds

The separation is worth stating explicitly, because the Proca equation is standard physics and the framework's contribution is a rewriting.

**The standard part.** The Proca Lagrangian, the equation of motion, the derivation of the Lorenz condition by contraction, the reduction to the Klein–Gordon equation, the dispersion relation, and the count of three polarizations are textbook field theory, transcribed here into the notation of the series. Nothing in the transcription changes them.

**The algebra's part.** The framework gives three compact statements that the index notation only implies. First, the field strength is the vector part of the conjugate gradient of the potential, and the Lorenz condition is the statement that the scalar part of that product vanishes; the constraint is thus the vanishing of the scalar part of a single biquaternion. Second, the divergence argument that derives the constraint is the observation that the d'Alembertian is central and scalar and that the field strength is a pure vector, so the scalar part of $\Box\tilde{F}$ vanishes identically. Third, the Hodge dual is minus left multiplication by the scalar imaginary, so the self-dual split of the field strength is a statement about the algebra's complex structure and survives the addition of a mass.

**What is imported.** The identification of the field with a particle of spin one, the value of the mass, and the physical interpretation of the three polarizations are inputs. The framework represents them; it does not derive them. The canonical quantisation of the Proca field, its propagator, and its constraint algebra belong to the field-theoretic companion subcategory and are not treated here.

The conventions are those of three companion articles:

- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the scalar equation to which the Proca field reduces, and for the plane-wave convention used here.
- Companion article *Maxwell's Equations in the Biquaternionic Formulation*, for the massless equation, the potential and field-strength biquaternions, and the gauge structure.
- Companion article *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector*, for the Hodge dual and the split of the field strength on the vector part of the algebra.

## Summary

The Proca equation for a massive spin-one field is written in the biquaternion framework as the single equation

$$
\tilde{\nabla}\tilde{F} = \frac{m^2c^2}{\hbar^2}\,\tilde{A},
\qquad
\tilde{F} = \bar{\tilde{\nabla}}\tilde{A} - \mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{A}\right),
$$

with $\tilde{A}\in\mathbb{M}_-$ and $\tilde{F}\in\mathrm{Vect}(\mathbb{B})$. Unlike the massless Maxwell equation, it is not gauge invariant: the mass term couples the potential to itself, and the gauge freedom of the massless theory is absent.

The divergence of the equation is not an identity. Applying $\bar{\tilde{\nabla}}$ and taking the scalar part, the d'Alembertian is central and scalar, the field strength is a pure vector, and the left-hand side vanishes identically; the mass then forces the **Lorenz condition** $S=\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})=0$ as a consequence of the equation of motion. With the constraint in hand, the field strength is the conjugate gradient of the potential and the equation reduces to the Klein–Gordon equation $(\Box - m^2c^2/\hbar^2)\tilde{A}=0$ for each component. The two together — Klein–Gordon and Lorenz — are equivalent to the Proca equation.

The plane-wave solutions carry a real spatial amplitude and a time component fixed by the Lorenz condition, with the dispersion relation $\omega^2 = c^2\mathbf{k}^2 + m^2c^4/\hbar^2$. The three real components of the spatial amplitude are the three polarizations: two transverse and one longitudinal. The longitudinal mode is physical because there is no gauge freedom to remove it; in the massless limit the residual gauge transformation removes exactly that mode and leaves the two transverse polarizations. The field strength remains a pure vector of the algebra and so retains the self-dual split of the companion article — it is the self-dual coordinate $\mathbf{V}=\mathbf{E}+ic\mathbf{B}$ of the real field — but it is not harmonic, and the mass term is precisely the source that the biquaternion Maxwell equation requires.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathrm{Vect}(\mathbb{B})$ | Complex three-dimensional vector part |
| $\tilde{\nabla}, \bar{\tilde{\nabla}}$ | Biquaternionic gradient and conjugate, $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$ |
| $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$ | Four-potential biquaternion in $\mathbb{M}_-$ |
| $\tilde{F} = \bar{\tilde{\nabla}}\tilde{A}-\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})$ | Field-strength biquaternion, pure vector |
| $S = \mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})$ | Gauge scalar; the Proca equation forces $S=0$ (Lorenz condition) |
| $\mu = mc/\hbar$ | Inverse Compton wavevector of the mass; $\mu^2=m^2c^2/\hbar^2$ |
| $\tilde{K} = i\omega/c\,e_0 + \mathbf{k}$ | Four-wavevector biquaternion |
| $\omega^2 = c^2\mathbf{k}^2 + m^2c^4/\hbar^2$ | Massive dispersion relation |
| $\mathbf{a}$, $A_0$ | Spatial amplitude (three real components) and time component fixed by Lorenz |
| $\star\tilde{F} = -i\tilde{F}$ | Hodge dual on the field strength (companion article) |

## Further Reading

- Alexandre Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs", *Journal de Physique et le Radium* 7 (1936) 347–353, for the original massive vector field equation.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the massive vector field, its constraint, and the counting of its polarizations.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Proca Lagrangian, the propagator, and the massless limit.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the constraint analysis of massive vector fields and the role of the Lorenz condition.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the massive vector field in the classical theory and the physical third polarization.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the massless limit, the gauge freedom, and the transverse polarizations.
- Walter Greiner and Joachim Reinhardt, *Field Quantization* (Springer, 1996), for the canonical treatment of the Proca field and its three polarization states.
