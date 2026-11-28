# __Relativistic Mechanics in Biquaternionic Form__

## Introduction

The equations of relativistic mechanics — the four-position, the invariant interval, the four-velocity, the four-momentum, the mass-shell relation, the four-force, the action, the conserved current, and the relativistic wave equations — are usually written in the language of four-vectors and Minkowski tensors. This article expresses them in the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H}$, using the $i r'_t$ convention in which the complex time coordinate absorbs the minus sign of the Minkowski metric.

The purpose is not to derive new physics. The purpose is to rewrite the established equations of relativistic mechanics in the biquaternion language, so that the algebraic structure of the theory is manifest. The biquaternion formulation makes the following structural facts explicit:

- The invariant interval is the biquaternion norm of the displacement biquaternion.
- The four-velocity and four-momentum are biquaternions of the anti-Hermitian subspace $\mathbb{B}_{\Phi}$.
- The mass-shell relation is the statement that the biquaternion norm of the four-momentum is a fixed negative constant.
- The conserved current is characterized by the scalar part of the quaternion-conjugate gradient vanishing.

These identities are algebraic, not physical. They are the reason the biquaternion algebra is the natural home of relativistic mechanics.

The conventions are those of the companion articles: the biquaternion algebra is $\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H}$, the quaternion basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_{\imath}^2 = -e_t$, the scalar imaginary is $i$, and the biquaternionic gradient is $\tilde\nabla_\Phi = e_t \partial/\partial R_t + \vec e_x \partial/\partial R_x + \vec e_y \partial/\partial R_y + \vec e_z \partial/\partial R_z$. Its quaternion conjugate is $(\tilde\nabla_\Phi)^{\natural} = e_t \partial/\partial R_t - \vec e_x \partial/\partial R_x - \vec e_y \partial/\partial R_y - \vec e_z \partial/\partial R_z$. The interval on the material sector has inertia $(3,1)$, the minus carried by the $i$ of $R_t=i r'_t$, so that $\partial^2/\partial R_t^2 = -\partial^2/\partial {r'_{t}}^2$. Throughout, the symbol $c$ denotes the speed of light in the medium, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ denotes the vacuum speed of light, $c_0 = 1/\sqrt{\epsilon_0\mu_0}$. In vacuum, $c = c_0$. The symbol $v$ (or $\vec v$) is reserved for particle and frame velocities.

## The Four-Position

The **four-position biquaternion** is

$$
\tilde R_\Phi = i r'_{t}\,e_t + r_x\,\vec e_x + r_y\,\vec e_y + r_z\,\vec e_z,
$$

where $r'_t \in \mathbb{R}$ is the temporal coordinate and $r_x, r_y, r_z \in \mathbb{R}$ the three spatial coordinates, all four lengths. The scalar part of $\tilde R_\Phi$ is the imaginary time coordinate $i r'_t$, and the vector part is the spatial position $r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$. In compact form,

$$
\tilde R_\Phi = i r'_{t}\,e_t + (r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z).
$$

The four-position biquaternion lives in the anti-Hermitian subspace $\mathbb{B}_{\Phi}$ (imaginary scalar part, real vector part), matching the structure of the four-vector $x_{\imath} = (i r'_t, r_x, r_y, r_z)$ in the $i r'_t$ convention.

It is a material element; it is what is observed. Its observable is the Hermitian representative $i\tilde R_\Phi\in\mathbb{B}_{\Psi}$, whose eigenvalues are the readings.

## The Invariant Interval

The **invariant interval** between two nearby events in spacetime is the **biquaternion norm** of the displacement biquaternion $d\tilde R_\Phi \in \mathbb{B}_{\Phi}$:

$$
\boxed{\;ds^2 = d\tilde R_\Phi\,d\tilde R_\Phi^{\natural} = (i\,dr'_t)^2 + dr_x^2+dr_y^2+dr_z^2 = -d{r'_{t}}^2 +dr_x^2+dr_y^2+dr_z^2\;}
$$

Here $d\tilde R_\Phi^{\natural} = i\,dr'_t\,e_t - d(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)$ is the quaternion conjugate of the displacement. This is the biquaternion form of the Minkowski interval. The minus sign in the time–time component arises algebraically from $i^2 = -1$, not from an independently postulated metric.

The displacement $d\tilde R_\Phi$ is a material element, and the interval is its norm; a spacelike distance is read from that norm.

The biquaternion norm on $\mathbb{B}_{\Phi}$. For a general element of the anti-Hermitian subspace, $\tilde{Q} = Q_t e_t + \vec Q$ with $Q_t=i q'_t$ imaginary and $\vec Q = r_x \vec e_x + r_y \vec e_y + r_z \vec e_z$ real, the biquaternion norm is

$$
\langle\tilde{Q}\rangle_{\natural} = Q_t^2 + |\vec Q|^2 = -{r'_{t}}^2 + r_x^2 + r_y^2 + r_z^2,
$$

which is a real scalar of inertia $(3, 1)$. This is the quadratic form used throughout this article, for the interval and for the four-vector normalizations.

The interval is invariant under the Lorentz group, which in the biquaternion framework is the group of rotor conjugations (see the companion article on the Lorentz transformation).

## The Four-Velocity

The **four-velocity biquaternion** of a particle with velocity $\vec v$ is

$$
\tilde{V}_{\Phi} = \gamma\left(ic\,e_t + \vec v\right),
$$

where

$$
\gamma = \frac{1}{\sqrt{1 - \vec v^2/c^2}}
$$

is the Lorentz factor. The scalar part of $\tilde{V}_{\Phi}$ is imaginary ($i\gamma c$) and the vector part is real ($\gamma\vec v$), so $\tilde{V}_{\Phi}$ lies in the anti-Hermitian subspace $\mathbb{B}_{\Phi}$, like the four-position. In compact form,

$$
\tilde{V}_{\Phi} = ic\,\gamma\,e_t + \gamma\vec v.
$$

The four-velocity satisfies the normalization condition

$$
\tilde{V}_{\Phi}\tilde{V}_{\Phi}^{\natural} = \gamma^2\left(-c^2 + \vec v^2\right) = -c^2,
$$

which is the biquaternion form of the standard relativistic normalization $v_{\imath} v_{\imath} = -c^2$. The normalization is the statement that the four-velocity has a fixed negative norm determined by the speed of light. It is a constraint, not an identity: not every biquaternion satisfies it, only the four-velocities of physical particles.

## The Four-Momentum

The **four-momentum biquaternion** is

$$
\tilde{P}_{\Phi} = m\tilde{V}_{\Phi} = \gamma m\left(ic\,e_t + \vec v\right) = i\frac{E}{c}\,e_t + \vec p,
$$

where $m$ is the rest mass, $E = \gamma m c^2$ is the relativistic energy, and $\vec p = \gamma m\vec v$ is the relativistic three-momentum. The scalar part of $\tilde{P}_{\Phi}$ is $iE/c$ and the vector part is $\vec p$, so $\tilde{P}_{\Phi}$ also lies in the anti-Hermitian subspace $\mathbb{B}_{\Phi}$.

## The Mass-Shell Relation

The four-momentum satisfies the mass-shell relation

$$
\boxed{\;\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = m^2 \tilde{V}_{\Phi}\tilde{V}_{\Phi}^{\natural} = -m^2 c^2\;}
$$

Expanding in components,

$$
\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = \left(i\frac{E}{c}\right)^2 + \vec p^2 = -\frac{E^2}{c^2} + \vec p^2 = -m^2 c^2,
$$

which is the standard relativistic energy–momentum relation

$$
E^2 = \vec p^2 c^2 + m^2 c^4.
$$

The mass-shell relation is the **constraint that defines the physical four-momenta**. In the biquaternion language, it is the statement that the **biquaternion norm of the four-momentum is a fixed negative constant**, determined by the rest mass and the speed of light. Particles of different masses lie on different shells (different values of $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural}$); massless particles lie on the **null shell** $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = 0$, corresponding to the light cone.

## The Four-Force

The **four-force biquaternion** is the proper-time derivative of the four-momentum:

$$
\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = \frac{d\tilde{P}_{\Phi}}{d\tau},
$$

where $\tau$ is the proper time of the particle, defined by $d\tau = dr'_t/(c\gamma)$. The four-force biquaternion lies in the anti-Hermitian subspace $\mathbb{B}_{\Phi}$, like $\tilde{P}_{\Phi}$.

Since $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = -m^2c^2$ is constant along the worldline, differentiating gives

$$
\tilde{\mathcal F}_{\Phi,\mathrm{frc}}\tilde{P}_{\Phi}^{\natural} + \tilde{P}_{\Phi}\tilde{\mathcal F}_{\Phi,\mathrm{frc}}^{\natural} = 0,
$$

which is the biquaternion form of the standard orthogonality condition $f_{\imath} p_{\imath} = 0$: the four-force is orthogonal to the four-momentum. This is the reason the four-force can change the direction of the four-momentum but not its norm, and hence not the rest mass.

For a charged particle in an electromagnetic field, the four-force in component form is

$$
\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = i\gamma\frac{ϙ}{c}\left(\vec E\cdot\vec v\right)e_t + \gamma ϙ\left(\vec E + \vec v\times\vec B\right),
$$

where $ϙ$ is the charge, $\vec E$ and $\vec B$ are the electric and magnetic fields, and $\vec v$ is the particle velocity. The scalar part is the power delivered to the particle (imaginary, as required by the $i r'_t$ convention for a four-vector), and the vector part is the relativistic three-force $\gamma ϙ(\vec E + \vec v\times\vec B)$.

Note on the biquaternion expression. The component formula above is standard and unambiguous. The expression of the same four-force as a biquaternion product of the field-strength biquaternion $\tilde F$ and the four-velocity $\tilde{V}_{\Phi}$ is not simply the real part of $\tilde F\tilde{V}_{\Phi}$; the correct expression involves the representation theory of $\mathbb{B}$ in the even subalgebra of $\mathrm{Cl}_{1,3}$, and it needs to be worked out carefully. This is left as an open question, to be addressed when the relevant literature on the biquaternion formulation of the Lorentz force is reviewed. The structural fact — that the four-force is an element of $\mathbb{B}_{\Phi}$ built from the field strength and the four-velocity — is correct; the explicit formula in terms of $\tilde F$ and $\tilde{V}_{\Phi}$ is deferred.

## The Action

The action is one of the eight formulas listed at the end of this article and it is derived nowhere in it. The derivation, the variation that produces the worldline equation, and the Euler–Lagrange machinery are in [The Relativistic Particle and the Lagrangian: The Stationary-Action Principle](the-relativistic-particle-and-the-lagrangian-the-stationary-action-principle.html), §*The Relativistic Particle*. **Relativity states the objects and their motion; the action principle is apparatus**, and this article takes $\tilde P_{\Phi} = m\tilde V_{\Phi}$ as the definition of the four-momentum rather than as a consequence.

## The Conserved Current

The **four-current biquaternion** is

$$
\tilde{J}_{\Phi} = ic\,\rho\,e_t + \vec j,
$$

where $\rho$ is the charge density and $\vec j$ is the current density. The current biquaternion lies in $\mathbb{B}_{\Phi}$ (imaginary scalar part, real vector part). The conservation of charge is expressed by the biquaternion equation

$$
\boxed{\;\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}\right) = 0\;}
$$

where $(\tilde\nabla_\Phi)^{\natural} = e_t\partial/\partial R_t - \vec e_x\partial/\partial R_x - \vec e_y\partial/\partial R_y - \vec e_z\partial/\partial R_z$ is the quaternion conjugate of the biquaternionic gradient. Expanding the scalar part,

$$
\mathrm{Sc}\!\left((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}\right) = \partial/\partial R_t(ic\rho) + \mathrm{div}\,\vec j = c\,\frac{\partial \rho}{\partial r'_t} + \mathrm{div}\,\vec j,
$$

so the condition is the standard continuity equation

$$
c\,\frac{\partial \rho}{\partial r'_t} + \mathrm{div}\,\vec j = 0.
$$

The condition is the scalar part of $(\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi} = 0$. The full equation $(\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi} = 0$ is stronger, because the vector part of $(\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}$ does not vanish in general: it involves the spatial derivatives of $\rho$ and $\vec j$, and it does not correspond to a standard physical conservation law. So the continuity equation is the scalar projection of the biquaternion conservation law.

## The Wave Equations, and Where They Are Treated

The mechanics above closes without a field equation. The mass-shell relation $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural}=-m^{2}c^{2}$ is the kinematic statement, and it is what the four-momentum of a particle obeys whether or not a field is written for it.

The two free wave equations that a field of mass $m$ obeys, the Klein–Gordon equation for a scalar and the Dirac pair for a spinor, are not kinematics and are not stated here. They belong to *Biquaternion Universe Force-Free*, which writes them in *The Klein–Gordon Equation in Biquaternionic Form* and *The Dirac Equation in Biquaternionic Form*, together with their polar and momentum-space forms, their fluids and their propagators. This article uses none of them and fixes no mass coefficient.

## Summary of the Eight Formulas

| Quantity | Biquaternion formula | Constraint |
|---|---|---|
| Four-position | $\tilde R_\Phi = i r'_{t}\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | — |
| Invariant interval | $ds^2 = d\tilde R_\Phi\,d\tilde R_\Phi^{\natural}$ | $= -d{r'_{t}}^2 +dr_x^2+dr_y^2+dr_z^2$ |
| Four-velocity | $\tilde{V}_{\Phi} = \gamma(ic\,e_t + \vec v)$ | $\tilde{V}_{\Phi}\tilde{V}_{\Phi}^{\natural} = -c^2$ |
| Four-momentum | $\tilde{P}_{\Phi} = m\tilde{V}_{\Phi}$ | $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = -m^2c^2$ |
| Mass-shell relation | $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = -m^2c^2$ | — |
| Four-force | $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = d\tilde{P}_{\Phi}/d\tau$ | $\tilde{\mathcal F}_{\Phi,\mathrm{frc}}\tilde{P}_{\Phi}^{\natural} + \tilde{P}_{\Phi}\tilde{\mathcal F}_{\Phi,\mathrm{frc}}^{\natural} = 0$ |
| Action | $S = -mc\int\sqrt{-\,d\tilde R_\Phi\,d\tilde R_\Phi^{\natural}}$ | — |
| Current | $\tilde{J}_{\Phi} = ic\rho\,e_t + \vec j$ | $\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}) = 0$ |


## Structural Observations

The four-vectors live in $\mathbb{B}_{\Phi}$. The four-position, four-velocity, four-momentum, four-force, four-potential, and four-current all lie in the anti-Hermitian subspace $\mathbb{B}_{\Phi}$ (imaginary scalar part, real vector part). This subspace is the biquaternion image of the Minkowski four-vector space, and it is closed under the natural Lorentz-covariant operations (addition, scalar multiplication by real numbers, and rotor conjugation).

**The mass-shell relation is a norm condition.** The statement $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = -m^2c^2$ is the statement that the **biquaternion norm** of the four-momentum is a fixed negative constant. Massless particles satisfy $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = 0$, which is the condition that the four-momentum lies on the **zero divisor cone** of the algebra (see the companion article on biquaternion zero divisors). So the light cone of Minkowski space is, in the biquaternion language, the **material-sector part of the zero divisor set** of the algebra.

The conserved current is a scalar projection of the biquaternion conservation law. The continuity equation is the scalar part of $(\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi} = 0$. The full biquaternion equation is stronger, and the vector part of $(\tilde\nabla_\Phi)^{\natural}\tilde{J}_{\Phi}$ does not have an independent physical interpretation as a conservation law.

## The Tensor-Dynamics Reading, and the Question of Extra Terms

A later formulation puts the same relativistic mechanics into a biquaternion tensor language, and its interest for this article is a claim about the algebra itself. E. P. J. de Haas, *Biquaternion Formulation of Relativistic Tensor Dynamics* (arXiv:1401.4470v1 [physics.gen-ph], 2013), builds what he calls a biquaternion tensor calculus whose stated goal is to fuse the antisymmetric tensor dynamics of relativistic electrodynamics and the symmetric tensor dynamics of relativity into one formalism, in a language he describes as "very akin to the standard relativistic space-time language". He positions the work in the programme A. P. Yefremov sketched for quaternionic relativity (arXiv:math-ph/0501055), and the paper is deliberately mathematical physics: the Lorentz force law and the Lagrange equation are presented in a new formalism, not derived anew. It is recorded here as a representational result, not as a prediction.

The objects are those of this article, with a tensor index carried by the biquaternion. The mechanical stress–energy density is $T_{\jmath\imath} = \tilde V_{\Phi,\jmath} G_{\imath}$, the product of the four-velocity biquaternion and the momentum-density biquaternion; the stress–energy density of a charged particle in a potential field adds a current–potential term; the Lagrangian density is given as twice its scalar part; and the conservation statement is written as a general force equation,

$$
\partial/\partial R_{\jmath} T_{\jmath\imath} + \partial/\partial R_{\imath} \mathrm{Lag} = 0,
$$

which reduces to the Lorentz force law under continuity conditions on the four-current and the four-velocity. The tensor of this article and the tensor of that paper are the same object reached by different routes, and the companion exercise on the electromagnetic energy–momentum tensor takes the force equation up as a problem.

**The claim that matters here is negative.** The paper's conclusion is that this formulation "lacks the extra terms that usually arise in biquaternionic electrodynamics". The condition is stated in the body and is worth carrying exactly: the electromagnetic force biquaternion matches the standard force field only if the **Lorenz fixing condition** $F_0 = \partial/\partial R_{\jmath} A_{\jmath} = 0$ holds; if $F_0 \neq 0$, then the usual biquaternion expressions for the Lorentz force and the two inhomogeneous Maxwell equations carry extra terms, and the calculus of this paper does not. The paper's own account of where those terms come from is equally explicit: they arise when the tensor indices are rearranged "according to their biquaternion affiliation", an operation the author calls external to his system and alien to it, because it destroys the tensor arrangement of the terms.

This is a counterweight to a recurring theme of the corpus, and the two must be read together. In the electro-gravimagnetic programme the biquaternion formulation is said to require an added scalar — the field $a(\tau,r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)$, or $\alpha$ in the later papers — precisely because the reduction to the standard equations is held to fail without it (*The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis*, and the modification recorded in *Maxwell's Equations in Biquaternionic Form*). de Haas reports the opposite outcome for a formulation arranged differently, and ties it to the representative. The corpus's question then becomes a precise one: do the extra terms come from the algebra, or from the way the tensors are mapped onto it together with the representative one imposes? The answer the two sources jointly suggest is the second — that the extra terms are an artefact of the mapping and the representative rather than of the algebra — and that sits with the corpus's own line that the algebra supplies the home and not the object. The corpus records the two claims side by side and adopts neither.

Two cautions. The claim is relative to this particular calculus and must not be generalised to all biquaternionic electrodynamics; the paper says as much by calling the rearrangement external. And the paper's own bookkeeping is not internally consistent in the places this article would use it: its canonical-Lagrangian section prints $T_{\jmath\imath} = \tilde V_{\Phi,\jmath} G_{\imath} - \tilde J_{\Phi,\jmath} A_{\imath}$ together with $\mathrm{Lag} = -\tilde V_{\Phi,\jmath} G_{\jmath} + \tilde J_{\Phi,\jmath} A_{\jmath}$, so that $\mathrm{Lag} = -T_{\jmath}{}_{\jmath}$, while its conclusion prints $T_{\jmath\imath} = \tilde V_{\Phi,\jmath} G_{\jmath} + \tilde J_{\Phi,\jmath} A_{\jmath}$ with $\mathrm{Lag}$ "as its trace". The sign and the index placement of the two displays differ and the source is not corrected here: a reader using the force equation should take the shapes and re-derive the signs. The extraction of the paper's tensor layouts is also unreliable, so the displays above are the printed ones and not a reconstruction.

## Open Questions

1. The Lorentz transformation of four-vectors. The four-vectors in $\mathbb{B}_{\Phi}$ transform under the Lorentz group by a rotor conjugation involving the boost biquaternion. The precise form of this transformation, and its relation to the standard four-vector transformation, is the subject of the companion article on the Lorentz transformation.

2. The Lorentz force in biquaternion form. The four-force in component form is standard: $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = i\gamma ϙ(\vec E\cdot\vec v)/c\,e_t + \gamma ϙ(\vec E + \vec v\times\vec B)$. Its expression as a biquaternion product of the field-strength biquaternion $\tilde F$ and the four-velocity $\tilde{V}_{\Phi}$ is not simply the real part of $\tilde F\tilde{V}_{\Phi}$; the correct expression involves the representation theory of $\mathbb{B}$ in the even subalgebra of $\mathrm{Cl}_{1,3}$, and it remains to be worked out cleanly. This is left for a future revision, and it may be addressed by the scientific literature on the biquaternion formulation of the Lorentz force.

3. The Lagrangian formulation. The biquaternion action $S = -mc\int\sqrt{-d\tilde R_\Phi\,d\tilde R_\Phi^{\natural}}$ is a real Lorentz scalar. Can the full Lagrangian formulation of relativistic mechanics (including interactions) be expressed in biquaternion form? A later tensor-dynamics formulation (de Haas, arXiv:1401.4470v1) gives one: the Lagrangian density as the trace of the stress–energy tensor, and the conservation law as the general force equation $\partial/\partial R_{\jmath} T_{\jmath\imath} + \partial/\partial R_{\imath} \mathrm{Lag} = 0$. It is recorded, with its signs and its cautions, in *The Tensor-Dynamics Reading, and the Question of Extra Terms* above.

4. The Hamiltonian formulation. The biquaternion form of the relativistic Hamiltonian and the associated Hamilton equations have not been developed.

5. Field-theoretic generalizations. The biquaternion mechanics presented here describes a single particle. How does the formulation extend to fields and to many-particle systems?

6. Quantization. The biquaternion framework is classical. How does it extend to the quantized theory, and what is the role of the biquaternion algebra in quantization?

These questions are open.

## Summary

The eight basic formulas of relativistic mechanics, four-position, invariant interval, four-velocity, four-momentum, mass-shell relation, four-force, action and current, can all be expressed in the biquaternion algebra $\mathbb{B}$ using the $i r'_t$ convention. The biquaternion formulation makes the following structural facts explicit:

- The invariant interval is the biquaternion norm of the four-position displacement biquaternion.
- The four-velocity, four-momentum, four-force, four-potential, and four-current lie in the anti-Hermitian subspace $\mathbb{B}_{\Phi}$.
- The mass-shell relation is the biquaternion-norm condition $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = -m^2c^2$.
- The light cone is the material-sector part of the zero-divisor set of the algebra.
- The conserved current is characterized by the scalar part of the quaternion-conjugate gradient vanishing.

These identities are algebraic, not physical. They are the reason the biquaternion algebra is the natural home of relativistic mechanics, and they are the starting point for the biquaternion formulation of Lorentz transformations, fields, and interactions developed in the companion articles. The biquaternion expression of the Lorentz force remains to be worked out and is flagged as an open question.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian subspace (four-vectors) |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |
| $\vec v$ | Particle three-velocity |
| $\gamma = 1/\sqrt{1 - \vec v^2/c^2}$ | Lorentz factor |
| $\tilde R_\Phi = i r'_t\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | Four-position biquaternion |
| $\tilde{V}_{\Phi} = \gamma(ic\,e_t + \vec v)$ | Four-velocity biquaternion |
| $\tilde{P}_{\Phi} = m\tilde{V}_{\Phi}$ | Four-momentum biquaternion |
| $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = d\tilde{P}_{\Phi}/d\tau$ | Four-force biquaternion |
| $\tilde{J}_{\Phi} = ic\rho\,e_t + \vec j$ | Four-current biquaternion |
| $\tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm (scalar quadratic form) |
| $\tilde\nabla_\Phi = e_t\partial/\partial R_t + \vec e_x\partial/\partial R_x + \vec e_y\partial/\partial R_y + \vec e_z\partial/\partial R_z$ | Biquaternionic gradient |
| $(\tilde\nabla_\Phi)^{\natural} = e_t\partial/\partial R_t - \vec e_x\partial/\partial R_x - \vec e_y\partial/\partial R_y - \vec e_z\partial/\partial R_z$ | Quaternion-conjugate gradient |
| $\Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$ | d'Alembertian |
| $\tau$ | Proper time |
| $m$ | Rest mass |

## Further Reading

- Albert Einstein, "Zur Elektrodynamik bewegter Körper," *Annalen der Physik* **17** (1905) 891–921, for the original special relativity.
- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the four-dimensional formulation.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the standard relativistic mechanics.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the standard four-vector formulation.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the geometric algebra formulation of relativistic mechanics.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the modern geometric algebra treatment.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- L. A. Alexeyeva, "Differential algebra of biquaternions. Dirac equation and its generalized solutions," *Progress in Analysis, Proceedings of the 8th Congress of the ISAAC* (Moscow, 2013), pp. 153–161, for the biquaternion formulation of relativistic wave equations.
- E. P. J. de Haas, "Biquaternion Formulation of Relativistic Tensor Dynamics," arXiv:1401.4470v1 [physics.gen-ph] (2013), for the biquaternion tensor calculus that fuses antisymmetric and symmetric relativistic tensor dynamics, the stress–energy density $T_{\jmath\imath} = \tilde V_{\Phi,\jmath} G_{\imath}$, the general force equation $\partial/\partial R_{\jmath} T_{\jmath\imath} + \partial/\partial R_{\imath} \mathrm{Lag} = 0$ with the Lagrangian density as its trace, and the claim that the formulation carries no extra terms relative to the standard relativistic language when the Lorenz fixing condition holds. Recorded in *The Tensor-Dynamics Reading, and the Question of Extra Terms*.
- A. P. Yefremov, "Quaternions and Biquaternions: Algebra, Geometry, and Physical Theories," arXiv:math-ph/0501055 (2005), for the programme of quaternionic relativity in which the tensor-dynamics formulation situates itself.

