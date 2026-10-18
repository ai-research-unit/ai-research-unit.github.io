# __The Eigenspinor: The Lorentz Rotor as a Function of Proper Time__

## Introduction

The companion articles use the Lorentz rotor as a **fixed** transformation. *The Lorentz Transformation as a Biquaternionic Rotation* builds the boost biquaternion $\tilde U$ once, from the four-velocity, and applies the same rotor conjugation to every four-vector of the problem. *The Spinor Module in Biquaternionic Form and Its Lorentz Action* treats the module on which rotors act one-sidedly. In both, the rotor is a constant of the motion, an object that labels a frame rather than one that evolves.

This article gives the rotor a **proper-time dependence**. For each event $\tau$ on the worldline of a particle there is a rotor $\tilde U(\tau)$ that carries the particle's rest frame to the laboratory, in the sense

$$
\tilde{P}(\tau) = \tilde U(\tau)\,\bigl(imc\,e_t\bigr)\,\tilde U(\tau)^{*},
$$

where $\tilde{P} = m\tilde{V}$ is the four-momentum. The rotor is called the particle's **eigenspinor**, after W. E. Baylis, and it is the natural dynamical variable of the worldline: the four-momentum is a quadratic function of it, so the three independent components of the velocity are carried by the eight parameters of the rotor, of which four are fixed by unit norm and one by the rest-frame gauge. The eigenspinor obeys a single linear equation,

$$
\frac{d\tilde U}{d\tau} = \tfrac12\,\tilde{\Omega}\,\tilde U,
$$

with $\tilde{\Omega}$ the spacetime rotation rate, and the Lorentz force follows from it in one line. The identification $\tilde{\Omega} = -(ϙ/m)\tilde{F}^{*}$ then makes the equation the covariant equation of motion.

Three things are worth separating at the outset, and the article keeps them apart.

- **What is standard and what is a translation.** The eigenspinor is standard relativistic mechanics in a geometric-algebra dress; Baylis, Hestenes and their school use it, and this article transcribes rather than re-derives. What the transcription adds is the $ict$ convention of this series and the dictionary to the companion articles.
- **What the algebra supplies.** The linearity of the evolution equation, the closure of the rotor under the flow, the one-sided spinor law, and the fact that the force is the anti-Hermitian projection of the rate times the momentum are algebraic identities, and they are checked below.
- **Where the earlier articles stop.** *The Lorentz Force in Biquaternion Form* records that the force is **not** a clean product of $\tilde{F}$ with $\tilde{V}$, and names the obstruction. The eigenspinor does not remove that obstruction; it offers a different, *differential* route to the same force. The two routes agree, and the agreement is checked.

The article is organised as follows. The next section defines the eigenspinor and recovers the four-momentum and the four-velocity from it. The section after that derives the evolution equation and the conservation of the norm. The following section identifies the rotation rate with the field and recovers the Lorentz four-force. The next two sections record the eigenframe and the closed form in a uniform field. A short section separates what the framework supplies from what it only transcribes, and the article closes with open questions.

## The Eigenspinor of a Worldline

The four-momentum of a particle of rest mass $m$ is $\tilde{P} = m\tilde{V}$, with $\tilde{V} = \gamma(ic\,e_t + \vec v)$ the four-velocity. It lies in the material sector $\mathbb{M}_-$ and its biquaternion norm is fixed,

$$
\tilde{P} \in \mathbb{M}_-, \qquad \langle\tilde{P}\rangle_{\natural} = \langle\tilde{P},\tilde{P}\rangle_{\natural} = \tilde{P}\tilde{P}^{\natural} = -m^2c^2 .
$$

**Definition.** The **eigenspinor** of the worldline is the rotor $\tilde U(\tau)$ that carries the rest four-momentum $imc\,e_t$ to the lab four-momentum,

$$
\boxed{\;\tilde{P}(\tau) = \tilde U(\tau)\,\bigl(imc\,e_t\bigr)\,\tilde U(\tau)^{*}\;}
$$

The rest four-momentum $imc\,e_t$ is central, so the definition reads $\tilde{P} = imc\,\tilde U\tilde U^{*}$; the whole of the velocity is carried by the product $\tilde U\tilde U^{*}$.

A word on signs, because this is where the translation from the source is easiest to get wrong. For a pure boost of rapidity $\psi$ along $\vec u$ the eigenspinor is

$$
\tilde U = \cosh\frac{\psi}{2}\,e_t - i\sinh\frac{\psi}{2}\,\vec u .
$$

This is the **quaternion conjugate** of the boost biquaternion

$$
\tilde U_{\text{lab}\to\text{mov}} = \cosh\frac{\psi}{2}\,e_t + i\sinh\frac{\psi}{2}\,\vec u
$$

of *The Lorentz Transformation as a Biquaternionic Rotation*, which carries the laboratory to the moving frame. The sign is fixed by the definition: the eigenspinor carries the **rest frame to the laboratory**, so it is the inverse of the lab-to-moving rotor, and $\tilde U^{\natural} = \tilde U^{-1}$ for a unit rotor.

**The four-momentum and the four-velocity.** For this boost the rotor is Hermitian, $\tilde U^{*} = \tilde U$, and of unit biquaternion norm, $\langle\tilde U\rangle_{\natural} = 1$, so $\tilde U\tilde U^{*} = \tilde U^2 = \gamma(e_t - i\beta\vec u)$ with $\beta = v/c$. Hence

$$
\tilde{P} = imc\,\tilde U^2 = i\gamma mc\,(e_t - i\beta\vec u) = m\gamma(ic\,e_t + \vec v),
$$

which is $\tilde{P} = m\tilde{V}$ with $\vec v = c\beta\vec u$. The four-velocity, the Lorentz factor and the velocity are therefore read off the eigenspinor by

$$
\tilde{V} = ic\,\tilde U\tilde U^{*},
\qquad
\gamma = \mathrm{Sc}\bigl(\tilde U\tilde U^{*}\bigr),
$$

or, more usefully, component by component from $\tilde{P} = m\tilde{V}$ and the dictionary $\tilde{V} = \gamma(ic\,e_t + \vec v)$.

**Two gauges.** The eigenspinor is not unique. It is defined up to the two-element kernel $\tilde U\to-\tilde U$ of the covering map $SL(2,\mathbb{C})\to SO^+(1,3)$, already recorded in the group-structure section of the companion article, and up to a residual rotation of the rest frame, $\tilde U\to\tilde U\tilde u$ with $\tilde u$ a unit rotor built from the spatial units alone, which leaves $\tilde U\tilde U^{*}$ unchanged. The first is removed by the branch convention $\mathrm{Sc}(\tilde U) > 0$; the second is physical and is the freedom to orient the spin axes of the rest frame. Neither affects the four-momentum.

**The one-sided transformation law.** Under a change of Lorentz frame implemented by the fixed Lorentz rotor $\tilde U_{\mathrm L}$, a four-vector transforms as $\tilde{P}' = \tilde U_{\mathrm L}\tilde{P}\tilde U_{\mathrm L}^{*}$ and, by the definition, the eigenspinor transforms as

$$
\tilde U' = \tilde U_{\mathrm L}\,\tilde U,
$$

a **one-sided** multiplication. This is the spinor law, not the two-sided four-vector law, and it is the statement that the eigenspinor belongs to the left module on which the rotors act, exactly as *The Spinor Module in Biquaternionic Form and Its Lorentz Action* describes. The two laws are consistent: $\tilde{P}' = (\tilde U_{\mathrm L}\tilde U)(imc\,e_t)(\tilde U_{\mathrm L}\tilde U)^{*}$. The distinction between this active reading of the rotor, the passive reading, and the reading in which a rotor relates two physical frames is set out in *The Lorentz Transformation as a Biquaternionic Rotation*, where the relative rotor between two worldlines is written as the ratio of their eigenspinors.

## The Evolution Equation and the Norm

Suppose the eigenspinor evolves linearly,

$$
\frac{d\tilde U}{d\tau} = \tfrac12\,\tilde{\Omega}\,\tilde U,
$$

with $\tilde{\Omega}$ a fixed element of the algebra, the **rotation rate** of the worldline. Differentiating the four-momentum then gives, since $imc\,e_t$ is central,

$$
\frac{d\tilde{P}}{d\tau}
= imc\left(d\tilde U/d\tau\tilde U^{*} + \tilde U\left(d\tilde U/d\tau\right)^{*}\right)
= \tfrac12\left(\tilde{\Omega}\tilde{P} + \tilde{P}\tilde{\Omega}^{*}\right).
$$

The right-hand side is exactly the material-sector projection of $\tilde{\Omega}\tilde{P}$:

$$
\tfrac12\left(\tilde{\Omega}\tilde{P} + \tilde{P}\tilde{\Omega}^{*}\right)
= P_{\mathbb{M}_-}\!\left(\tilde{\Omega}\tilde{P}\right),
\qquad
P_{\mathbb{M}_-}(\tilde{Q}) = \tfrac12\left(\tilde{Q} - \tilde{Q}^{*}\right),
$$

where the identification uses $\tilde{P}^{*} = -\tilde{P}$. Thus the evolution equation for the eigenspinor implies the covariant equation of motion

$$
\boxed{\;\frac{d\tilde{P}}{d\tau} = P_{\mathbb{M}_-}\!\left(\tilde{\Omega}\,\tilde{P}\right)\;}
$$

**Which rates are allowed.** A rate with a scalar part destroys the norm of the eigenspinor and with it the mass shell. Writing $\tilde{\Omega} = \tilde{\Omega}_0 + \vec V$ with $\tilde{\Omega}_0$ central and $\vec V$ a pure vector, the derivative of $\langle\tilde U\rangle_{\natural} = \tilde U\tilde U^{\natural}$ is

$$
\frac{d}{d\tau}\langle\tilde U\rangle_{\natural} = \tfrac12\left(\tilde{\Omega} + \tilde{\Omega}^{\natural}\right) = \tilde{\Omega}_0 + \tfrac12\left(\vec V + \vec V^{\natural}\right)
= \tilde{\Omega}_0,
$$

because a pure vector is anti-fixed by quaternion conjugation, $\vec V^{\natural} = -\vec V$. Norm preservation is therefore exactly the condition that **the rotation rate have no scalar part**,

$$
\langle\tilde U\rangle_{\natural} = \text{const} \iff \tilde{\Omega} \in \mathrm{Vect}(\mathbb{B}),
$$

and this is the same condition under which $\langle\tilde{P}\rangle_{\natural} = -m^2c^2$ is preserved along the flow. It is the biquaternion form of the Minkowski orthogonality $\tilde{K}\tilde{P}^{\natural} + \tilde{P}\tilde{K}^{\natural} = 0$ recorded in the Lorentz-force article.

## The Field as the Rotation Rate

The transcription to the Lorentz force is now a single identification. Recall that the field-strength biquaternion of the series is the pure vector

$$
\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H,
$$

so that $\vec E$ is the imaginary vector part and $\vec B = \mu\vec H$ the real vector part. The rotation rate of a charge $ϙ$ in this field is

$$
\boxed{\;\tilde{\Omega} = -\frac{ϙ}{m}\left(\frac{i}{c}\vec E + \vec B\right) = -\frac{ϙ}{m}\,\tilde{F}^{*}\;}
$$

in the units of the field-strength article with $\sqrt{\epsilon_0} = 1/c_0$ and $\sqrt{\mu_0} = 1$ (Heaviside–Lorentz units), where $\tilde{F}^{*} = i\sqrt{\epsilon}\vec E + \sqrt{\mu}\vec H = i\vec E/c + \vec B$. The rate is a pure vector, so it preserves the norm, and the minus sign is the one fixed by using the rest-to-lab eigenspinor; with the lab-to-moving rotor the sign is reversed. Substituting into the equation of motion gives

$$
\frac{d\tilde{P}}{d\tau} = -\frac{ϙ}{m}\,P_{\mathbb{M}_-}\!\left(\tilde{F}^{*}\tilde{P}\right)
= -ϙ\,P_{\mathbb{M}_-}\!\left(\left(\frac{i}{c}\vec E + \vec B\right)\tilde{V}\right),
$$

and this is the Lorentz four-force

$$
\tilde{K} = i\,\frac{\gamma ϙ}{c}\left(\vec E\cdot\vec v\right)e_t + \gamma ϙ\left(\vec E + \vec v\times\vec B\right)
$$

of the component-form section of *The Lorentz Force in Biquaternion Form*.

**Consistency with the product formula.** The companion articles write the force as

$$
\tilde{K} = -ϙ\sqrt{\mu}\,P_{\mathbb{M}_-}\!\left(\tilde{V}\tilde{F}\right),
$$

with the velocity on the **left** and $\tilde{F}$ itself rather than $\tilde{F}^{*}$. The eigenspinor route puts the field on the left and uses the conjugate. The two expressions are different-looking but equal; both reproduce the component $\tilde{K}$, and their difference is a genuine algebraic identity, not an approximation. What the eigenspinor supplies is not a new formula for the force but the **linear object** — the rotor — whose quadratic product is the four-momentum and whose rate is the field.

## The Eigenframe

The eigenspinor carries the rest frame of the particle, so its images of the rest-frame axes are the particle's own frame in the laboratory. With $\mathcal{E}_0 = ie_t$ and $\mathcal{E}_k = \vec e_k$ the basis of $\mathbb{M}_-$,

$$
\tilde{E}_{(\mu)}(\tau) = \tilde U(\tau)\,\mathcal{E}_\mu\,\tilde U(\tau)^{*} \in \mathbb{M}_- ,
$$

and the four-vector $\tilde{E}_{(0)} = i\tilde U\tilde U^{*}$ is the four-velocity direction, $c\,\tilde{E}_{(0)} = \tilde{V}$. The three spatial images $\tilde{E}_{(k)}$ are the boosted axes, orthonormal in the sense of the Minkowski form, and they rotate along the worldline with the same rate $\tilde{\Omega}$. The eigenspinor is therefore a **tetrad** in which the time axis is the four-velocity: it is a frame field along the worldline, and the four-momentum is its time leg rescaled by $mc$.

This is the interpretation that separates the eigenspinor from the ordinary Lorentz rotor. A fixed rotor gives one tetrad; the eigenspinor gives a tetrad at every event, tied to the orientation of the particle's rest frame, and the equation of motion is the statement that the tetrad turns at the rate $\tilde{\Omega}$.

## The Closed Form in a Uniform Field

When the field is constant the rate $\tilde{\Omega}$ is constant, and the evolution equation integrates immediately:

$$
\tilde U(\tau) = \exp\!\left(\tfrac12\tilde{\Omega}\,\tau\right)\tilde U(0),
\qquad
\tilde{P}(\tau) = \tilde U(\tau)\bigl(imc\,e_t\bigr)\tilde U(\tau)^{*} .
$$

Both factors are rotors: $\tilde{\Omega}$ is a pure vector, so $\exp(\tfrac12\tilde{\Omega}\tau)$ is a unit rotor, and the flow stays on the norm shell. In a purely electric or purely magnetic field the exponential is a boost or a rotation; in a general uniform field it is a boost composed with a rotation, and the worldline is the corresponding screw. The companion articles on the purely electric and purely magnetic cases of *The Relativistic Particle in an External Field* are the two degenerate limits of this one closed form.

## What the Framework Supplies and What It Only Transcribes

**Supplied by the algebra.** The linear evolution equation, the closure of the flow under a scalar-part-free rate, the one-sided spinor law, the identity $d\tilde{P}/d\tau = P_{\mathbb{M}_-}(\tilde{\Omega}\tilde{P})$, the norm conservation, and the closed form in a uniform field are all algebraic, and each was checked above.

**Transcribed.** The eigenspinor is not this series' invention. Baylis uses it throughout *Electrodynamics: A Modern Geometric Approach* and in the paravector lecture that is the source of this article; Hestenes uses the same object as the "rotor part" of the Dirac spinor in spacetime algebra. What the series adds is the $ict$ convention, the dictionary to the companion articles, and the checks.

**Where the earlier articles stop, and what changes.** *The Lorentz Force in Biquaternion Form* shows that $\tilde{K}$ is **not** $\mathrm{Re}(\tilde{F}\tilde{V})$ or any single product of $\tilde{F}$ with $\tilde{V}$, and locates the obstruction in the two duality halves of the field. The eigenspinor does not contradict that finding and does not remove the obstruction. It gives the force a clean *linear* source instead: the rate $\tilde{\Omega}$ and the rotor $\tilde U$. Whether the series should present the eigenspinor as the primary formulation of the relativistic particle, with the product formula as a derived corollary, is a matter of taste and is left open below; the two statements are consistent.

## Open Questions

1. **Intrinsic spin.** The eigenspinor used here carries only the orbital frame. A particle with intrinsic spin needs a second rotor, or a spinor variable, coupled to the same rate; the Bargmann–Michel–Telegdi equation and the spin-four-vector of the companion articles are the classical limit of that coupling. What is the joint eigenspinor of the orbit and the spin, and does it factorise?

2. **The quantum eigenspinor.** In the geometric-algebra interpretation of the Dirac equation the Dirac spinor is a rotor times a density and an angle. Is the classical eigenspinor the $\hbar\to0$ limit of that object, and does the series' spinor module supply the density factor?

3. **Non-uniform fields.** The closed form holds for constant $\tilde{\Omega}$. For a varying field the equation of motion is still linear in $\tilde U$, but the direction of the rate turns with the position, and the rotor is a path-ordered exponential. What is the series' natural language for the path ordering, and does the gradient $\tilde{\nabla}$ of *The Biquaternion D'Alembertian* supply it?

4. **The gauge of the rest frame.** The residual rotation $\tilde U\to\tilde U\tilde u$ is a gauge freedom in the classical problem and a physical degree of freedom once spin is included. Is there a series convention for fixing it, and does it correspond to the Thomas–Wigner rotation of the companion exercise?

5. **The rate as a connection.** The rate $\tilde{\Omega}$ is an element of $\mathrm{Vect}(\mathbb{B})$, the same subspace that carries the field strength. Is the eigenspinor flow a parallel transport in a connection whose curvature is the field, and does that interpretation connect to the curved-spacetime articles?

These questions are open.

## Summary

The **eigenspinor** $\tilde U(\tau)$ is the Lorentz rotor that carries the rest four-momentum to the lab four-momentum,

$$
\tilde{P} = \tilde U\,\bigl(imc\,e_t\bigr)\,\tilde U^{*},
$$

and it is the natural dynamical variable of a relativistic worldline. For a pure boost of rapidity $\psi$ along $\vec u$ it is $\tilde U = \cosh\frac{\psi}{2}e_t - i\sinh\frac{\psi}{2}\vec u$, the quaternion conjugate of the lab-to-moving boost biquaternion of the companion article.

It obeys the linear equation

$$
\frac{d\tilde U}{d\tau} = \tfrac12\,\tilde{\Omega}\,\tilde U,
$$

whose rate $\tilde{\Omega}$ must be a pure vector, $\tilde{\Omega}\in\mathrm{Vect}(\mathbb{B})$, for the norm — and with it the mass shell — to be preserved. The implied equation of motion is

$$
\frac{d\tilde{P}}{d\tau} = P_{\mathbb{M}_-}\!\left(\tilde{\Omega}\tilde{P}\right)
= \tfrac12\left(\tilde{\Omega}\tilde{P} + \tilde{P}\tilde{\Omega}^{*}\right).
$$

With the field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\vec E - \sqrt{\mu}\vec H$ and the identification $\tilde{\Omega} = -(ϙ/m)\tilde{F}^{*}$ (Heaviside–Lorentz units), this is the Lorentz four-force of the companion article, and it agrees with the companion's product form $-ϙ\sqrt{\mu}\,P_{\mathbb{M}_-}(\tilde{V}\tilde{F})$. Under a change of frame the eigenspinor transforms one-sidedly, $\tilde U\to\tilde U_{\mathrm L}\tilde U$, the spinor law of *The Spinor Module*. In a uniform field the evolution integrates to $\tilde U = \exp(\tfrac12\tilde{\Omega}\tau)\tilde U(0)$.

The eigenspinor does not remove the obstruction recorded in *The Lorentz Force in Biquaternion Form* to writing $\tilde{K}$ as a single product of $\tilde{F}$ with $\tilde{V}$. It offers a different route, in which the force has a **linear** source — the rotor and its rate — and the product formula is a derived corollary.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde U(\tau)$ | Eigenspinor: the rotor carrying the rest frame to the laboratory |
| $\tilde U_{\mathrm L}$ | Fixed Lorentz rotor acting on the eigenspinor; $\tilde U_{\mathrm L}\tilde U_{\mathrm L}^{\natural}=e_t$ |
| $\tilde{P} = m\tilde{V}$ | Four-momentum, in the material sector $\mathbb{M}_-$ |
| $imc\,e_t$ | Rest four-momentum (central) |
| $\tilde{\Omega}$ | Spacetime rotation rate, a pure vector, $\tilde{\Omega}^{\natural} = -\tilde{\Omega}$ |
| $\tilde{F} = i\sqrt{\epsilon}\vec E - \sqrt{\mu}\vec H$ | Field-strength biquaternion |
| $\tilde{F}^{*}$ | Its conjugate, $i\sqrt{\epsilon}\vec E + \sqrt{\mu}\vec H$ |
| $P_{\mathbb{M}_-}(\tilde{Q}) = \tfrac12(\tilde{Q}-\tilde{Q}^{*})$ | Projection onto the material sector |
| $\tilde{E}_{(\mu)} = \tilde U\mathcal{E}_\mu\tilde U^{*}$ | Eigenframe (tetrad) along the worldline |
| $\tilde{V} = \gamma(ic\,e_t + \vec v)$ | Four-velocity |
| $\tilde{K}$ | Lorentz four-force, $d\tilde{P}/d\tau$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |

## Further Reading

- W. E. Baylis, *Geometry of Paravector Space, with Applications to Relativistic Physics* (University of Windsor lecture, 2003), for the eigenspinor, the evolution equation $d\Lambda/d\tau = \frac12\Omega\Lambda$, the identity $dp/d\tau = \langle\Omega p\rangle_<$, the closed form in a uniform field and the identification $\Omega = eF/m$. This article is the series' transcription of that source into the $ict$ convention.
- W. E. Baylis, *Electrodynamics: A Modern Geometric Approach* (Birkhäuser, 1999), for the same formalism developed at book length, with the complex-quaternion algebra, the paravector space and the Hermitian subspaces.
- W. E. Baylis, "Relativity in introductory physics," *Canadian Journal of Physics* **82** (2004) 853, for the companion lecture.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the rotor-times-density interpretation of the Dirac spinor, of which the classical eigenspinor is the orbital part.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of Lorentz transformations and its use in classical relativistic dynamics.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the spinor module and the one-sided action of the rotors.
- William E. Baylis (ed.), *Clifford (Geometric) Algebras with Applications in Physics, Mathematics and Engineering* (Birkhäuser, 1996), for the broader context of the paravector and Pauli-algebra formulations.
