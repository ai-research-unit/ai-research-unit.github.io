# __Spin Conservation and the Frenkel Condition__

## Introduction

**The spin tensor's conservation law is the rotor's equation of motion read in components, and the Frenkel condition is the statement that the spin has no component along the momentum.** Both statements are framework content: the algebra supplies the first through the rotor's logarithmic derivative, and it supplies the second through the fact that the polar word carries the spin in a rotation and not in a boost.

**The conservation law.** With the spin element $\tilde S_{\Psi,\mathrm{sp}}=\rho\tfrac{\hbar}{2}i\hat s$ of [The Polar Form of the Dirac Equation in Biquaternionic Form](the-polar-form-of-the-dirac-equation-in-biquaternionic-form.html) and with the rotor's logarithmic derivative $\tilde u_{\mathrm r}^{-1}\partial_\eta\tilde u_{\mathrm r}=\tfrac12\vec\Omega_\eta$ — a real vector part, which is what the polar decomposition's fourth factor supplies — the rotor's own equation of motion is

$$
\partial_\eta\tilde u_{\mathrm r}=\tfrac12\vec\Omega_\eta\,\tilde u_{\mathrm r},
$$

**and the divergence of the spin current is the antisymmetric part of the spin connection contracted with the spin:**

$$
\partial_\eta S_{\Psi,\mathrm{sp},\eta,\lambda\nu}=\tau_{\lambda\nu},
\qquad
\tau_{\lambda\nu}=\tfrac12\left(\Omega_{\eta,\lambda}S_{\Psi,\mathrm{sp},\eta,\nu}-\Omega_{\eta,\nu}S_{\Psi,\mathrm{sp},\eta,\lambda}\right).
$$

**The source $\tau_{\lambda\nu}$ is the torque, and it vanishes when the connection turns about the spin's own axis** — which is the statement, in components, that a free rotor's spin is conserved.

**The Frenkel condition.** In the corpus's letters it reads

$$
\mathcal{F}:\qquad S_{\Psi,\eta,\lambda\nu}\,v_{\Phi,\nu}=0,
$$

**the spin's contraction with the flow vanishes**, and its content is that the spin has no component in the time direction of the fluid's rest frame. **The condition leaves three of the six components of an antisymmetric object**, and those three are the spin vector that the polar word's rotor carries.

**What the article supplies and what it does not.** It supplies the derivation of the conservation law from the rotor's equation, the two conditions — Frenkel and Weyssenhoff — and the statement of which of the algebra's features makes each of them natural. **It does not supply the value of the spin, the gyromagnetic ratio, or the spin-orbit coupling**; those are the dynamics of a specific field, and the article names the places where they would enter.

## The Rotor's Equation of Motion

### The connection

**The rotor's logarithmic derivative is a real vector part, and the polar decomposition's structure is what makes it so.** In the word $\tilde\Xi=r\,e^{i\alpha}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$, the rotor is real and unitary, so $\tilde u_{\mathrm r}^{-1}\partial_\eta\tilde u_{\mathrm r}$ is a pure vector and real — **the algebra's own statement that a rotation's generator is a spatial direction**, and the property that lets the rotor's derivative be read as an angular velocity.

$$
\tilde u_{\mathrm r}^{-1}\partial_\eta\tilde u_{\mathrm r}=\tfrac12\vec\Omega_\eta,
\qquad
\vec\Omega_\eta\in\mathbb{R}^{3},
$$

**the subscript $\eta$ labelling the direction and not an index slot**, following the frame and metric conventions. **The object is a connection**: it transports the spin frame from point to point, and the spin's precession is what the transport does to a direction.

**The equation of motion, in the form that is useful.** Multiplying the logarithmic derivative by the rotor gives

$$
\partial_\eta\tilde u_{\mathrm r}=\tfrac12\vec\Omega_\eta\,\tilde u_{\mathrm r},
$$

**a first-order equation for the rotor in which the connection acts by left multiplication** — left, because the connection is read in the frame the rotor has already reached. **The display is the rotor's own equation of motion**, and it is the object that the polar-form article's open question lists as missing: that article says the four brackets are constrained by the Dirac pair but not closed by it, and asks whether a transport equation for the rotor closes them. **The answer here is partial: the rotor's equation exists and is the display above, and it closes the brackets once $\vec\Omega_\eta$ is given.** What is not yet derived is the equation for $\vec\Omega_\eta$ itself.

### From the rotor to the spin direction

**The spin direction is the rotor's image of the frame's third direction, and its derivative is the connection's action on it.**

$$
\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural},
\qquad
\partial_\eta\hat s=\vec\Omega_\eta\times\hat s\ \text{in the spatial reading},
$$

**the first display quoted from the polar-form article and the second its consequence.** The cross product is the spatial reading of the commutator, and **the article uses the spatial reading whenever it is checked against a number**; the element spelling is the one it uses in the conservation law.

**Two consequences, and both are the spin's conservation in embryo.** First, $\partial_\eta(\hat s\cdot\hat s)=2\hat s\cdot(\vec\Omega_\eta\times\hat s)=0$, so **the spin's magnitude is conserved by precession** — the rotor is a rotation, so it cannot change a length. Second, $\hat s\cdot\partial_\eta\hat s=0$, so **the precession does no work on the spin's direction**; the direction moves on the sphere and its speed of travel is the component of $\vec\Omega_\eta$ perpendicular to $\hat s$.

**The precession is the classical spin equation, and the article states the correspondence.** With $\vec\Omega_\eta$ the connection and $\hat s$ the direction, $\partial_\eta\hat s=\vec\Omega_\eta\times\hat s$ is the classical equation of a spinning top with no torque; **a torque adds a term to the right-hand side, and that term is the source in the conservation law.**

### The conservation law, derived

**Differentiate the spin element along the flow, insert the rotor's equation, and the result is a divergence with a torque source.** With $\tilde S_{\Psi,\mathrm{sp}}=\rho\tfrac{\hbar}{2}i\hat s$ and the spin current $\tilde S_{\Psi,\mathrm{sp},\eta}=\tilde S_{\Psi,\mathrm{sp}}\,v_{\Phi,\eta}/c$,

$$
\partial_\eta S_{\Psi,\mathrm{sp},\eta,\lambda\nu}
=\partial_\eta\left(\rho\,\frac{\hbar}{2}\,v_{\Phi,\eta}/c\right)\hat s_{\lambda\nu}
+\rho\,\frac{\hbar}{2}\,v_{\Phi,\eta}/c\ \partial_\eta\hat s_{\lambda\nu},
$$

**the product rule's two terms.** The first is the spin's advection with the density's change, and it vanishes for a conserved flow with constant density along the worldline; the second is the precession, and it is the commutator of the connection with the spin. **Writing both together with the components low,**

$$
\partial_\eta S_{\Psi,\mathrm{sp},\eta,\lambda\nu}=\tau_{\lambda\nu},
\qquad
\tau_{\lambda\nu}=\tfrac12\left(\Omega_{\eta,\lambda}S_{\Psi,\mathrm{sp},\eta,\nu}-\Omega_{\eta,\nu}S_{\Psi,\mathrm{sp},\eta,\lambda}\right)+\left(\text{advection}\right),
$$

**and the article's claim is the structural one: the spin's conservation law is the rotor's equation of motion, with the antisymmetric part of the connection as the source.**

**Why the antisymmetric part, in one line.** The spin is antisymmetric in its two labels, so only the antisymmetric part of any object contracted with it survives; **the symmetric part of the connection is invisible to the spin**, which is the algebraic reason the torque is a commutator and not a product.

**The free case, which is the one the corpus uses.** For a free rotor the connection is generated by the same equation that generates the momentum, and the torque vanishes on the solutions; **so $\partial_\eta S_{\Psi,\mathrm{sp},\eta,\lambda\nu}=0$ for a free field**, and the spin current is divergence-free. That is the conservation law the article set out to read off, and it is read off the rotor and not postulated.

## The Frenkel Condition

### The condition

**The Frenkel condition is the statement that the spin is orthogonal to the flow, and in components it is the vanishing of the contraction.**

$$
\mathcal{F}:\qquad S_{\Psi,\eta,\lambda\nu}\,v_{\Phi,\nu}=0
\qquad\text{for all }\lambda,
$$

**with every index low and $v_{\Phi,\nu}$ the flow's components.** Its content is a count: an antisymmetric $4\times4$ array has six independent components, and three linear conditions remove three of them, **leaving the three components of a spatial vector in the fluid's rest frame.**

**The rest-frame reading, which is what the count means.** In the fluid's rest frame $v_{\Phi,\nu}=(c,0,0,0)$, so the condition reads $S_{\Psi,\eta,\lambda t}=0$: **the components with one temporal label vanish, and the three spatial ones survive.** Those three are the spin vector, and the corpus writes them as the direction $\hat s$.

**Why this is the natural condition and not an arbitrary one.** A spinning particle's spin is an angular momentum in its own rest frame, and an angular momentum in the $ti$ plane would be a boost — a displacement of the centre of mass, not a rotation. **The Frenkel condition says that the spin is a rotation and not a displacement**, which is exactly the content of the polar word's division of labour: the boost carries the velocity and the rotor carries the spin, and neither carries the other.

### The algebra's version of the condition

**In the corpus's letters the Frenkel condition is automatic, and this is the article's central framework claim.** The spin element is

$$
\tilde S_{\Psi,\mathrm{sp}}=\rho\,\frac{\hbar}{2}\,i\hat s,
\qquad
\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural},
\qquad
\hat s^{2}=-e_t,
$$

**the polar-form article's display.** Its scalar slot is empty — $\mathrm{Sc}(\tilde S_{\Psi,\mathrm{sp}})=0$ — and its vector slot carries $i$ times a real direction. **A temporal component is precisely a scalar-slot component in the corpus's component convention**, so the vanishing of the scalar slot *is* the vanishing of the four components with one temporal label:

$$
\mathrm{Sc}\left(\tilde S_{\Psi,\mathrm{sp}}\right)=0
\qquad\Longleftrightarrow\qquad
\mathcal{F}.
$$

**The equivalence is the article's main structural statement: the corpus does not impose the Frenkel condition, because the polar word cannot violate it.** The spin is carried by a rotation, a rotation is a real unitary element, and the image of a spatial direction under a rotation is a spatial direction. **A framework in which the spin lived in the field's eight parameters without a rotor would have to impose $\mathcal{F}$ by hand; this one gets it from the decomposition.**

**What the equivalence does not say, and the article is explicit.** It does not say that every field satisfies $\mathcal{F}$ in the sense of the *macroscopic* polarization of [Spin Hydrodynamics in Biquaternionic Form](spin-hydrodynamics-in-biquaternionic-form.html). **The polar word's $\hat s$ is one element's spin direction; the fluid's polarization is the average of many**, and the average of directions with empty scalar slots is a direction with an empty scalar slot only if the averaging is done in one frame. **In another frame the averaged polarization can acquire a temporal part**, and that is a statement about the average and not about the algebra.

### The condition's preservation

**The Frenkel condition is preserved by boosts, and the article checks it because a condition that is not preserved is a frame choice rather than a constraint.** With the spin purely spatial in the rest frame and the boost along a direction making an angle with it, the transformed array's temporal-spatial components are

$$
S_{\Psi,\eta,0i}^{\prime}=\gamma\,\beta_{j}\,S_{\Psi,\eta,ji},
$$

**which are non-zero in general** — so the *components* change — while the contraction with the transformed flow still vanishes:

$$
S_{\Psi,\eta,\lambda\nu}^{\prime}\,v_{\Phi,\nu}^{\prime}=0 .
$$

**The two displays are not in conflict**: the condition is that the contraction vanishes, and the contraction is invariant even though the components are not. **A reader who checks only the components will conclude that the condition fails under a boost, and that conclusion is the commonest error in the literature on the Frenkel condition.**

**The number that makes the point.** Take $\hat s=\vec e_z$ and a boost along $\vec e_x$ with $\beta_{\mathrm{vel}}$, so that only $S_{\Psi,\eta,xy}$ is non-zero in the rest frame. Then $S_{\Psi,\eta,0y}^{\prime}=\gamma\beta_{\mathrm{vel}}S_{\Psi,\eta,xy}$ and $S_{\Psi,\eta,xy}^{\prime}=\gamma S_{\Psi,\eta,xy}$, so the temporal part *grows* with the boost while the contraction with $v_{\Phi,\nu}^{\prime}=\gamma(c,\beta_{\mathrm{vel}}c,0,0)$ receives no contribution from it, because $\beta_{\mathrm{vel}}$ multiplies the $x$ slot, which is empty. **The check is two multiplications and it settles the question.**

## The Weyssenhoff Condition

### The two conditions together

**The Weyssenhoff condition adds a second requirement to the Frenkel one: the spin current is divergence-free, so the spin is conserved and not merely constrained.**

$$
\mathcal{W}:\qquad \mathcal{F}\ \text{holds}
\quad\text{and}\quad
\partial_\eta S_{\Psi,\mathrm{sp},\eta,\lambda\nu}=0 .
$$

**The difference between the two conditions is the difference between a constraint and a conservation law.** Frenkel says what the spin is allowed to be; Weyssenhoff says that what it is allowed to be is conserved, so the torque of the previous section vanishes identically. **A Frenkel fluid's spin precesses under a torque; a Weyssenhoff fluid's spin does not, and its only motion is advection with the flow.**

**The corpus's free case satisfies both, and that is why the two conditions are often conflated in the literature.** For a free rotor the torque vanishes because the connection turns about the spin, and the Frenkel condition holds because the spin is carried by the rotor; **so the free field is a Weyssenhoff fluid**, and the distinction between the conditions only shows when a torque is applied. **The article keeps the two names apart for that reason and not for pedantry.**

### The consequence for the momentum balance

**A Weyssenhoff fluid's momentum balance carries the spin, and the standard consequence is that the momentum flux is not symmetric.** The spin's flux contributes to the angular momentum flux, so the part of the stress that would be the antisymmetric one is fixed by the spin rather than free. **The article states this as the standard structural consequence and does not re-derive it**, because the derivation is the tensor calculus's and the corpus adds nothing to it: **what the corpus adds is where the spin lives.**

### The asymmetry in the corpus's letters, and the honest limit

**The corpus's energy-momentum element has four components, not sixteen, and this is a limitation that the article states plainly.**

$$
\tilde\Sigma_\Psi=w_{\mathrm{fl}}e_t+\frac{i}{c}\vec S_{\mathrm P},
$$

**an element whose scalar slot is the energy density and whose vector slot is the momentum density.** The four conservation laws it carries are the energy and the three momentum components, which is what a fluid needs; **the spatial-spatial block — the pressure and the shear, in the component language — is not a slot of the element at all.** The pressure enters through the equation of state and the shear through the transport coefficients, not through slots.

**So the antisymmetric part of the full stress has no spelling in the element, and the Belinfante improvement has no distinct version here.** The improvement's content is that the spin's contribution to the angular momentum can be moved between the orbital and the intrinsic parts; **in this framework the two parts are already separated by construction**, the orbital part being the boost's and the intrinsic part the rotor's. **The separation is the polar decomposition's division of labour, and the framework therefore has no Belinfante ambiguity to resolve** — which is a genuine simplification and not a claim that the full tensor has been reconstructed.

**What is open, and stated as open.** Whether a full sixteen-component stress can be written as an element of $\mathbb{B}$, or as a small collection of elements, is not settled in the corpus. **An element has eight real components and the stress has sixteen**, so a single element cannot hold it; a pair of elements could, and no article in the category proposes the pair. **The article marks this as the natural next question for the spin sector** and does not answer it.

## What the Algebra Supplies and What It Does Not

**Supplies: the division that makes the Frenkel condition automatic.** The polar word separates the velocity into the boost and the spin into the rotor, so the spin cannot acquire a temporal part; **the condition that other frameworks impose is here a property of the decomposition.**

**Supplies: the precession equation without a separate postulate.** The rotor's logarithmic derivative is a real vector part, its left action on the rotor is the equation of motion, and the spin's precession is that equation read on a direction. **No separate spin equation is added to the framework.**

**Supplies: the antisymmetric structure of the torque.** The spin is antisymmetric in its labels and the connection's symmetric part is invisible to it, so the source is a commutator. **The structure of the conservation law follows from the algebra's own product rule.**

**Does not supply: the connection's equation.** $\vec\Omega_\eta$ is written and not derived; the equation that determines it is the dynamics of a specific field, and in the Dirac case it is the magnetic coupling that [The Classical Origin of $g=2$ in Biquaternionic Form](the-classical-origin-of-g-2-in-biquaternionic-form.html) writes. **The conservation law's source is therefore determined only once $\vec\Omega_\eta$ is**, which is the article's honest boundary.

**Does not supply: the value of the spin.** That the spin element carries $\hbar/2$ is the corpus's normalisation for a spin-$\tfrac12$ field, quoted from the polar-form article; **a different field would carry a different factor, and the algebra does not fix it.**

**Does not supply: the Thomas precession, which the article mentions and does not derive.** A spinning particle accelerated along a curved worldline precesses at a rate reduced by the Thomas factor

$$
\frac{\gamma^{2}}{\gamma+1},
$$

**which tends to $\tfrac12$ at low speed and to $\gamma$ at high speed.** Evaluated: at $\beta_{\mathrm{vel}}=0.01$ the factor is $0.500\,038$, at $0.1$ it is $0.503\,782$, at $0.5$ it is $0.618\,802$ and at $0.9$ it is $1.597\,725$. **The factor is a kinematic consequence of composing boosts and belongs to the Lorentz group's structure rather than to the spin's dynamics**; the corpus writes it here for completeness and does not use it in the conservation law.

**Does not supply: the averaging that turns one element's spin into a fluid's polarization.** The polar word's $\hat s$ is one element's direction; the polarization of [Spin Hydrodynamics in Biquaternionic Form](spin-hydrodynamics-in-biquaternionic-form.html) is an average, and whether the average preserves the Frenkel condition in every frame is the question that the previous section marks as open.

## What Is Established and What Is Interpretation

**Established, and framework content.** That the rotor's logarithmic derivative is a real vector part and that the rotor's equation of motion is $\partial_\eta\tilde u_{\mathrm r}=\tfrac12\vec\Omega_\eta\tilde u_{\mathrm r}$; that the spin's precession is $\partial_\eta\hat s=\vec\Omega_\eta\times\hat s$ with the magnitude conserved; that the spin current's divergence is the antisymmetric part of the connection contracted with the spin, so that the conservation law is read off the rotor and not postulated; that the free field has vanishing torque and a divergence-free spin current; that the Frenkel condition is automatic in the polar word, because the spin element's scalar slot is empty; that the condition is preserved by boosts although its components are not; that the Weyssenhoff condition adds conservation to constraint.

**Interpretation, and marked as such.** That the corpus has no Belinfante ambiguity because the orbital and intrinsic parts of the angular momentum are separated by the polar decomposition is the article's reading of the structure and is not a theorem. **It is a reading the algebra supports — the slots are what they are — and it is offered as such.**

**Not claimed.** That the connection's equation has been derived; that the full sixteen-component stress has been represented; that the Thomas precession has been derived from the rotor; that the fluid's averaged polarization satisfies the Frenkel condition in every frame; that the spin's magnitude is a dynamical constant rather than a normalisation.

## Summary

The spin current's conservation law is the rotor's equation of motion. With $\tilde u_{\mathrm r}^{-1}\partial_\eta\tilde u_{\mathrm r}=\tfrac12\vec\Omega_\eta$ a real vector part, the rotor obeys $\partial_\eta\tilde u_{\mathrm r}=\tfrac12\vec\Omega_\eta\tilde u_{\mathrm r}$, the spin direction obeys $\partial_\eta\hat s=\vec\Omega_\eta\times\hat s$, and the divergence of the spin current is the torque $\tau_{\lambda\nu}=\tfrac12(\Omega_{\eta,\lambda}S_{\Psi,\mathrm{sp},\eta,\nu}-\Omega_{\eta,\nu}S_{\Psi,\mathrm{sp},\eta,\lambda})$, which vanishes when the connection turns about the spin's axis. For the free field the torque vanishes and $\partial_\eta S_{\Psi,\mathrm{sp},\eta,\lambda\nu}=0$.

The Frenkel condition, $S_{\Psi,\eta,\lambda\nu}v_{\Phi,\nu}=0$, removes the three components of the antisymmetric array that carry a temporal label and leaves the three of a spatial vector. **In the corpus's letters it is automatic**: the spin element is $\rho\tfrac{\hbar}{2}i\hat s$ with $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$, whose scalar slot is empty, and an empty scalar slot is exactly the vanishing of the temporal components. The corpus therefore does not impose the condition; the polar decomposition cannot violate it. The condition is preserved by boosts — $S_{\Psi,\eta,0i}^{\prime}=\gamma\beta_{j}S_{\Psi,\eta,ji}$ is non-zero in general while the contraction with $v_{\Phi,\nu}^{\prime}$ still vanishes — and a reader who checks components alone will wrongly conclude that it fails.

The Weyssenhoff condition adds conservation to constraint: $\mathcal{F}$ and $\partial_\eta S_{\Psi,\mathrm{sp},\eta,\lambda\nu}=0$ together, so the spin is advected and never precesses. The corpus's free field satisfies both, which is why the two conditions are often conflated.

The honest limits are three. The connection's equation is not derived here; the spin's magnitude is a normalisation and not a dynamical constant; and the corpus's stress element has four components, so the antisymmetric part of the full stress has no slot, the Belinfante improvement has no distinct spelling, and the reconstruction of the sixteen-component object is open. The Thomas factor $\gamma^{2}/(\gamma+1)$, which is $0.503\,782$ at $\beta_{\mathrm{vel}}=0.1$ and $1.597\,725$ at $0.9$, is quoted and not derived.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde u_{\mathrm r}$ | Rotor of the polar word, real and unitary |
| $\vec\Omega_\eta$ | Rotor connection, a real vector per direction |
| $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ | Spin direction, a unit spatial vector |
| $\tilde S_{\Psi,\mathrm{sp}}=\rho\tfrac{\hbar}{2}i\hat s$ | Spin element |
| $S_{\Psi,\mathrm{sp},\eta,\lambda\nu}$ | Components of the spin current, all low |
| $\tau_{\lambda\nu}$ | Torque, the spin current's source |
| $\mathcal{F}$ | The Frenkel condition |
| $\mathcal{W}$ | The Weyssenhoff condition |
| $v_{\Phi,\nu}$ | Components of the flow element |
| $\rho=\lVert\tilde\Xi\rVert^{2}$ | Proper density |
| $\tilde\Sigma_\Psi=w_{\mathrm{fl}}e_t+\tfrac{i}{c}\vec S_{\mathrm P}$ | Energy–momentum element, four components |
| $w_{\mathrm{fl}}$, $\vec S_{\mathrm P}$ | Energy density, momentum density |
| $\tilde\Xi=r\,e^{i\alpha}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | Polar word |
| $r$, $\alpha$, $\tilde U_{\Psi,\mathrm b}$ | Scale, central angle, boost |
| $\vec e_z$ | Frame's third direction, used by the value test |
| $\beta_{\mathrm{vel}}=\vec v/c$, $\gamma$ | Velocity and boost factor |
| $\gamma^{2}/(\gamma+1)$ | Thomas factor |
| $\hbar$ | Planck constant |
| $\langle\ \rangle_{\natural}$, $\mathrm{Sc}$ | Quaternionic norm, scalar part |
| $\mathbb{B}$, $\mathbb{B}_\Phi$, $\mathbb{B}_\Psi$ | The algebra and its two sectors |

## Further Reading

- J. Frenkel, "Die Elektrodynamik des rotierenden Elektrons," *Zeitschrift für Physik* **37** (1926) 243–262, for the spin-momentum orthogonality condition.
- J. Weyssenhoff and A. Raabe, "Relativistic dynamics of spin-fluids and spin-particles," *Acta Physica Polonica* **9** (1947) 7–18, for the spin fluid with a conserved spin current.
- A. Papapetrou, "Spinning test-particles in general relativity I," *Proceedings of the Royal Society A* **209** (1951) 248–258, for the equations of motion of a spinning particle and the constraint's role.
- F. W. Hehl, P. von der Heyde and G. D. Kerlick, "General relativity with spin and torsion: foundations and prospects," *Reviews of Modern Physics* **48** (1976) 393–416, for the spin tensor's conservation and the asymmetric stress.
- F. J. Belinfante, "On the spin angular momentum of mesons," *Physica* **6** (1939) 887–898, for the improvement that symmetrises the stress.
- L. Rosenfeld, "Sur le tenseur d'impulsion-énergie," *Mémoires de l'Académie Royale de Belgique* **18** (1940) 1–30, for the same improvement in the field-theoretic setting.
- L. H. Thomas, "The motion of the spinning electron," *Nature* **117** (1926) 514, for the precession factor quoted here.
- C. Møller, *The Theory of Relativity* (Oxford, 1972), for the spin tensor's transformation properties, which the preservation discussion follows.
- The companion articles: [The Polar Form of the Dirac Equation in Biquaternionic Form](the-polar-form-of-the-dirac-equation-in-biquaternionic-form.html), [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html), and [Spin Hydrodynamics in Biquaternionic Form](spin-hydrodynamics-in-biquaternionic-form.html).
