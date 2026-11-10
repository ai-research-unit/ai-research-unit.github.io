# __The Spin Fluid of the Biquaternion Dirac Field__

## Introduction

**The fluid of the Dirac field carries three data at each event — a density, a frame element, and a spin direction — and the frame element is what makes it a spin fluid rather than a dust.** The density is $\rho_{\mathrm{num}}$. The frame element is the boost of the polar form, whose square is the four-velocity. The spin direction is the rotor's image of the declared axis. The current is the density times the frame element, the spin is the density times the rotor, and the angle of the word is read by neither.

The article assembles two results that already exist and derives neither. The polar form of the Dirac equation, with its four factors, its velocity and its spin, is [The Polar Form of the Dirac Equation in Biquaternionic Form](the-polar-form-of-the-dirac-equation-in-biquaternionic-form.html). The split of the current into a convection part and a spin part is [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](the-gordon-decomposition-of-the-dirac-current-in-biquaternionic-form.html). Both are cited at the point of use, and the displays below that repeat their formulas are quotations, marked as such.

Three results are new here.

- **The flow is not a gradient.** The scalar field's velocity is the gradient of its action, exactly, so its velocity one-form is closed. The Dirac field's velocity is a unit element squared, so its one-form is closed only in the rigid case. The difference is the whole content of the word "spin fluid".
- **The vorticity is the frame's curl.** Written on the component spelling of the element, the vorticity 2-form is the antisymmetrised gradient of the frame element, and it vanishes exactly where the frame is constant. A spatially varying rapidity is enough to make it non-zero, and the check below exhibits a shear flow with a circulation of $0.434\,556$ against a closed form that agrees to fifteen digits.
- **The scalar case is the frozen-frame sector.** The scalar field has no frame element to vary. Freezing the Dirac frame gives a rigid flow, and a rigid flow is locally a gradient flow. So the gradient sector is the frozen sector, and the Dirac field leaves it as soon as its rapidity or its direction varies.

Two cautions are stated once and used throughout. The first is that *closure* and *rigidity* are different conditions: closure is the vanishing of the antisymmetric part of the velocity's gradient, rigidity the vanishing of the symmetric part. This article is about closure. [Covariant Local Equilibrium and Tolman Temperature](covariant-local-equilibrium-and-tolman-temperature.html) is about rigidity, and a reader who conflates them will read the two articles as contradicting each other. The second is that *rotor* in this article's title names the frame element $\tilde U$ of the word, which the polar article splits into a boost and a spatial rotor. Where the split matters, the two factors are named separately and the frame element is not called a rotor.

The word of the field is

$$
\tilde\Xi=\rho\,\tilde U,
\qquad
\rho=\sqrt{\langle\tilde\Xi\rangle_{\natural}},
\qquad
r=\lvert\rho\rvert>0,
\qquad
\tilde U=\frac{\tilde\Xi}{\rho},
$$

with $r$ the scale, $\tilde U$ a unit element, and the four parameters of the word the scale, the central angle, the rapidity and the spatial rotor's angle. The proper density of this category is $\rho_{\mathrm{num}}=\langle\tilde\Xi\rangle_{\natural}=r^{2}$. **The polar article writes that density as $\rho$ and its root as $r$, so the two letters are interchanged between the two articles**: this article's $\rho$ is the polar article's $r$, and this article's $\rho_{\mathrm{num}}$ is the polar article's $\rho$. The reason for the interchange is that the density of this category is never a bare letter, while the polar word's scale is one, and the two cannot both take $\rho$. Every statement below is about a direction or a ratio, so the difference never enters a conclusion. That is the notational translation this article makes once and does not repeat.

## The Polar Data of the Fluid

### The frame element is the velocity's square root

**The four-velocity is the inverse square of the frame element, and that is the fact the whole article turns on.** The polar article proves

$$
\tilde V_{\Phi}=ic\,\tilde U_{\Psi,\mathrm b}^{-2}=\gamma\bigl(ic\,e_t+\vec v\bigr),
\qquad
\vec v=c\tanh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b},
\qquad
\gamma=\cosh\theta_{\mathrm{rpd}},
\qquad
\langle\tilde V_{\Phi}\rangle_{\natural}=-c^{2}.
$$

The square is not decoration and it is not an error of the display. A velocity is bilinear in the spinor, so the frame enters it twice; the word deposits the boost once in the frame and twice in the four-vector. The conventions record the factor of two as the commonest error in the corpus, and the polar article's §*The boost is the four-velocity* is where the factors are counted. This article takes the display as given.

The norm being $-c^{2}$ is stronger than the corresponding statement for the scalar field. There the four-velocity is a unit element only where the quantum potential vanishes, because the scalar velocity is a gradient and a gradient of a solution is not automatically on the mass shell; here the frame element is a unit by construction, so the velocity is a unit wherever the field is non-zero. The density is a separate factor and carries no part of the normalisation.

### The spin is the rotor's image of the axis

**The spin element is the density times $\hbar/2$ times the rotor's image of the declared axis.** The polar article proves

$$
\tilde S_{\Psi,\mathrm{sp}}=\rho\,\frac{\hbar}{2}\,i\,\hat s,
\qquad
\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural},
\qquad
\hat s^{2}=-e_t,
$$

with $\tilde u_{\mathrm r}$ the spatial rotor. In this category's letters the prefactor is $\rho_{\mathrm{num}}^{1/2}$, the scale; the spin direction $\hat s$ is a unit real vector, the element is Hermitian because of the central $i$, and the declared axis $\vec e_z$ does not survive: only its image does.

Three absences are exact and each has a reason. The central angle is absent, because $\natural$ does not conjugate it and the product cancels it. The boost is absent, because a boost does not rotate a spin direction in the rest frame, and the word respects that by putting the spin in the factor the boost leaves alone. And the declared axis is absent, because the rotor's image is what the field carries; a reader who wants a preferred axis of the algebra will not find one, and the absence is the algebra's way of saying that the axis is a convention of the frame and not a property of the field.

### The current, and the bilinear that is not the current

**The current is the density times the frame element.** The polar article proves

$$
\tilde J_{\Phi}=\rho_{\mathrm{num}}\,\tilde V_{\Phi}=ic\gamma\rho_{\mathrm{num}}\,e_t+\rho_{\mathrm{num}}\gamma\vec v,
$$

so the temporal slot is the charge density $ic\gamma\rho_{\mathrm{num}}$ and the spatial part is the current density $\rho_{\mathrm{num}}\gamma\vec v$. The current reads four parameters — the scale, the rapidity and the two angles of the direction — and it reads neither the central angle nor the spatial rotor.

The algebra's own bilinear is not this current, and the polar article proves why: $i\tilde\Xi\tilde\Xi^{*}$ leaves the boost in place and cancels the rotor, so it carries the velocity twice; the outer $i$ then reverses the spatial part, so the bilinear is the current of the mirror image of the motion. The conserved current needs the velocity once and a fixed timelike direction once, and the fixed direction is the odd element the even algebra does not contain. That is a negative result about the algebra and not about the physics: the standard theory has its conserved current, and the word exhibits it as the density times a frame factor.

### The Gordon split

**The current separates into a transport part and a magnetisation part.** The Gordon article proves, for a solution,

$$
\bar{\tilde\Xi}_{\mathrm{sp}}\,i\,e_\mu\,\tilde\Xi_{\mathrm{sp}}\,\vec e_{\nu(\mu)}
=\frac{i}{2k_m}\Big(\bar{\tilde\Xi}_{\mathrm{sp}}\,\partial_\mu\tilde\Xi_{\mathrm{sp}}-\overline{\partial_\mu\tilde\Xi_{\mathrm{sp}}}\,\tilde\Xi_{\mathrm{sp}}\Big)
+\frac{1}{k_m}\sum_\nu\varepsilon_\nu\,\partial_\nu\Big(\bar{\tilde\Xi}_{\mathrm{sp}}\,\Sigma_{\mu\nu}\tilde\Xi_{\mathrm{sp}}\Big),
$$

with $\Sigma_{\mu\nu}$ the spin generator. The first term is the convection current and carries the field's own first derivative; the second is the divergence of the antisymmetric spin density and is a **bound** current: it is conserved by antisymmetry alone, contributes nothing to the total charge, and cannot be removed from the magnetic moment. The article's own words are that the split separates a transport current from a magnetisation current, and not a conserved piece from a non-conserved piece.

For the fluid this is the statement that the density times the frame element is not the whole story. Part of what flows is the spin's own circulation, and the next sections show that the spin's circulation and the frame's vorticity are the same object read twice.

## The Flow Is Not a Gradient

### The scalar case is a gradient, exactly

**The scalar field's velocity is the gradient of its action at every event, so its velocity one-form is closed identically.** In the polar form of the Klein–Gordon equation the momentum is

$$
\tilde P_{\Phi}=\tilde\nabla S_{\tilde\Xi},
\qquad
\tilde V_{\Phi}=\frac{\tilde P_{\Phi}}{m},
\qquad
v_{\Phi,\mu}=\frac{1}{m}\frac{\partial S_{\tilde\Xi}}{\partial R_\mu},
$$

and the last display is the component spelling of the element, on the pattern of $k_{\Phi,\mu}$. The index stays low and labels a direction. Since partial derivatives commute,

$$
\frac{\partial v_{\Phi,\mu}}{\partial R_\nu}-\frac{\partial v_{\Phi,\nu}}{\partial R_\mu}
=\frac{1}{m}\left(\frac{\partial^{2}S_{\tilde\Xi}}{\partial R_\nu\partial R_\mu}-\frac{\partial^{2}S_{\tilde\Xi}}{\partial R_\mu\partial R_\nu}\right)=0 .
$$

The scalar flow is therefore **closed**: it is the gradient of a single function, and every closed-loop integral of it is fixed by the winding of the action. That is the fact [The Nodal Set and Quantized Circulation](the-nodal-set-and-quantized-circulation.html) uses, and it is exact for every solution and not only for a plane wave. The qualification the scalar article carries is that the four-velocity is a unit only where the quantum potential vanishes; the closure does not depend on that qualification and holds everywhere the action is defined.

### The Dirac case is a frame

**The Dirac velocity is a unit element squared, and the square of a unit element is not the derivative of anything.** The display quoted above says $\tilde V_{\Phi}=ic\tilde U_{\Psi,\mathrm b}^{-2}$. There is no scalar function whose gradient this is, for a reason of counting: a unit timelike element has three independent parameters, the rapidity and the two angles of its axis, and a gradient $\partial_\mu S$ has one function of the four coordinates. Four equations cannot be solved by one function unless the four are tied by three conditions, and the conditions are exactly the vanishing of the vorticity.

The counting is worth writing out because it is the whole obstruction. A closed one-form on four coordinates has, at each event, four components subject to the six conditions $\partial_\mu v_\nu=\partial_\nu v_\mu$; the solution set is one function. The velocity of the word has four components subject to one condition, $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}$, so it has three functions of the four coordinates. The gap between three and one is two functions at each event, and those two functions are what the word "spin fluid" names. The scalar field has one function, its action, and no gap.

### The closure test, written out

**The Dirac velocity is closed only in the rigid case.** Take the component spelling of the element, $v_{\Phi,t}=ic\gamma$ and $v_{\Phi,\eta}=\gamma v_\eta$, with $\gamma=\cosh\theta_{\mathrm{rpd}}$ and $\vec v=c\tanh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}$. Closure requires $\partial_\eta v_{\Phi,t}=\partial_t v_{\Phi,\eta}$, that is,

$$
ic\,\frac{\partial\gamma}{\partial r_\eta}
=\frac{\partial}{\partial r'_t}\bigl(\gamma v_\eta\bigr),
\qquad
\text{and}\qquad
\frac{\partial}{\partial r_j}\bigl(\gamma v_\eta\bigr)=\frac{\partial}{\partial r_\eta}\bigl(\gamma v_j\bigr).
$$

The first pair is the statement that the rapidity does not vary in space unless it also varies in time in a compensating way; for a static flow it forces $\partial_\eta\gamma=0$. The second triple is the ordinary statement that the spatial current density $\gamma\vec v$ is curl free. Neither is implied by the Dirac equation. So the general solution has a velocity that is not closed, and the two conditions are the two functions of the counting above.

**A rigid flow is closed.** If $\tilde U$ is constant then $\tilde V_\Phi$ is constant, and a constant one-form is exact: it is the gradient of a linear function. So the frozen-frame sector sits inside the gradient sector, and the inclusion is strict in the other direction only for the scalar field, which has no frame at all.

## Vorticity and Its Source

### The vorticity 2-form

**The vorticity is the antisymmetrised gradient of the velocity's component spelling.** Define

$$
\omega_{\mu\nu}=\frac{\partial v_{\Phi,\nu}}{\partial R_\mu}-\frac{\partial v_{\Phi,\mu}}{\partial R_\nu},
$$

with both indices low, as the frame conventions require, and with the four directions the four coordinates. The definition is the component spelling of the element and not a tensor's slot: the four numbers $v_{\Phi,\mu}$ are the four coefficients read in the frame, and $\omega$ is their curl. The three purely spatial components are the curl of the current density $\gamma\vec v$ up to the sign of the metric, and the three mixed components are the time derivative of the current density less the spatial gradient of the energy slot $ic\gamma$.

**The vorticity vanishes for the scalar flow and need not vanish for the Dirac flow.** For the scalar field the first display of the previous section gives $\omega_{\mu\nu}=0$ identically. For the Dirac field the general field gives $\omega\ne0$, and the content of this section is to name its source.

### The frame's gradient is the source

**The vorticity is the frame element's logarithmic derivative, read through the velocity.** Write $\tilde V_{\Phi}=ic\tilde U^{-2}$ with $\tilde U$ the boost factor. Differentiating,

$$
\frac{\partial\tilde V_{\Phi}}{\partial R_\mu}
=-ic\left(\tilde U^{-1}\frac{\partial\tilde U}{\partial R_\mu}\tilde U^{-2}
+\tilde U^{-2}\frac{\partial\tilde U}{\partial R_\mu}\tilde U^{-1}\right),
$$

using $\partial_\mu\tilde U^{-1}=-\tilde U^{-1}(\partial_\mu\tilde U)\tilde U^{-1}$ twice. Each bracket is a product of the frame element with its own logarithmic derivative $\tilde U^{-1}\partial_\mu\tilde U$, which is the object a connection is made of. So the gradient of the velocity is built from the frame's connection and nothing else: where the frame is constant, the velocity is constant and the vorticity vanishes; where the frame varies, the vorticity is the antisymmetrised image of that variation.

That is the precise sense in which **the vorticity is sourced by the frame's gradients**. The source is not the density — the density cancels out of the velocity entirely — and it is not the central angle, which no bilinear reads. It is the variation of the frame element, and the frame element carries the rapidity and the direction between them.

### The shear flow, and the check

**A spatially varying rapidity is enough.** Take a frame whose axis is fixed along $\vec e_y$ and whose rapidity varies with $r_x$ only:

$$
\theta_{\mathrm{rpd}}(r_x)=0.4+0.2\sin(1.3\,r_x),
\qquad
\vec u_{\mathrm b}=\vec e_y,
\qquad
v_{\Phi,y}(r_x)=c\sinh\theta_{\mathrm{rpd}}(r_x),
$$

the last equality being $\gamma v_y=c\cosh\theta_{\mathrm{rpd}}\tanh\theta_{\mathrm{rpd}}=c\sinh\theta_{\mathrm{rpd}}$. Then

$$
\omega_{xy}=\frac{\partial v_{\Phi,y}}{\partial r_x}=c\cosh\theta_{\mathrm{rpd}}\,\frac{\partial\theta_{\mathrm{rpd}}}{\partial r_x}\ne0,
$$

and the flow has a circulation around any loop in the $xy$ plane that spans a difference of rapidity. The check was run with $c=2$ and the rapidity profile above. At $r_x=0.2$, $0.7$ and $1.1$ the difference quotient of $v_{\Phi,y}$ and the closed form $c\cosh\theta\,\partial\theta/\partial r_x$ agreed to $1.1\times10^{-10}$ or better, with two of the three agreeing to the last bit. The circulation of the flow, $\oint v_{\Phi,y}\,dr_x$ around the unit square $0\le r_x\le1$, $0\le r_y\le1$ and equal by Stokes to $\int\!\int\omega_{xy}\,dr_xdr_y$ over it, was $0.434\,555\,977\,568\,337$ against the closed form $c[\sinh\theta(1)-\sinh\theta(0)]=0.434\,555\,977\,568\,337$, agreeing to all fifteen digits printed. The same loop on the scalar flow of a quadratic action gave a curl of exactly zero.

So the vorticity is real, it is produced by the frame's gradient alone, and the scalar sector cannot produce it. That is the difference the title of this article names.

### What the vorticity is not

**It is not the spin.** The spin direction is the rotor's image of the axis, and the vorticity is the curl of the velocity. The two are independent parameters of the word, and the field equation is what ties them; this article does not solve that tie, and the articles on spin hydrodynamics and on the Frenkel condition take it up. What can be said without solving it is that a fluid whose vorticity and whose spin direction are unrelated at each event is a legitimate solution of the kinematics, and that a hydrodynamic closure has to add the relation.

**It is not the magnetic field.** The Gordon spin term is a magnetisation current and the vorticity is a flow property. The two meet in the antisymmetric part of the stress, which is where a spin fluid differs from a dust; the stress element of [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html) is symmetric by construction, so the antisymmetric part is a genuinely new ingredient of the Dirac case, and [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html) is where it is identified.

## The Frozen-Frame Sector

### Freezing the frame

**Set the frame element to a constant and the spin fluid degenerates to a rigid flow.** With $\tilde U$ constant, $\tilde V_\Phi$ is constant, $\omega_{\mu\nu}=0$, the spin direction is constant, and the Gordon spin term is a divergence whose bilinear is constant. What remains is a dust: a density and a constant velocity, with a spin direction that does not vary. Every statement of the previous sections is then either trivially satisfied or trivially false: the vorticity vanishes, the circulation vanishes, and the current is a constant times the density.

The degeneration is not a physical limit in which interesting physics is lost. It is the kinematic statement that a spin fluid whose frame does not vary has nothing left that a scalar fluid lacks. The spin element is still there — it is a constant direction — but a constant spin direction is a property of the state and not of the flow, and it enters no equation of motion. That is why the corpus's polar form gives the spin a whole section and the scalar article gives it none.

### The scalar field is the sector with no frame to freeze

**The scalar polar form has a scale and a phase and nothing else, so its velocity is a gradient by construction.** The word is $\tilde\Xi=\lVert\tilde\Xi\rVert\exp(iS_{\tilde\Xi}/\hbar)e_t$, and the two parameters are the amplitude and the action. There is no third factor, so there is no frame element, so there is nothing whose gradient could make the flow non-closed. The scalar field is therefore the frozen-frame sector in the precise sense that it is the sector with no frame: a frame that does not exist cannot vary.

The identification is worth stating as an inclusion rather than as an analogy. Every scalar solution, read through the Dirac polar form, has a velocity that is a gradient and a spin direction that is a constant — and the constant is not arbitrary, since the axis is the declared one. Conversely, a Dirac solution whose frame is constant and whose central angle carries the phase gradient is a scalar solution up to the spin direction. So the scalar sector is the intersection of two conditions, and the Dirac sector is what the second condition removes.

### What the limit loses

**Four things are lost when the frame is frozen, and each is individually checkable.**

- **The vorticity.** A closed one-form has zero curl, so the circulation around every loop vanishes. The shear flow of the check above has a circulation of $0.434\,556$; the scalar flow on the same loop has exactly zero.
- **The spin part of the current.** The Gordon spin term is the divergence of an antisymmetric bilinear. With a constant frame and a constant spin direction the bilinear is constant, so its divergence vanishes and the whole current is the convection part.
- **The magnetic moment.** The spin density is still non-zero, but its divergence contributes nothing to the current, so a static spin density produces no magnetisation current. That is the right statement for a uniformly magnetised medium and the wrong one for a bounded sample, which is why the frozen sector is the sector of bulk statements.
- **The antisymmetric stress.** The stress element of the scalar field is symmetric in its two slots, because it is built from a single gradient. The Dirac field's stress has an antisymmetric part whenever the spin direction varies, and that part is the torque density. [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html) has no place for it.

## The Spin Fluid at a Point

### The triple

**At each event the fluid is a triple: a density, a frame element, and a spin direction.** In the letters of this category,

$$
\rho_{\mathrm{num}}(x),
\qquad
\tilde V_{\Phi}(x)=ic\,\tilde U_{\Psi,\mathrm b}^{-2}(x),
\qquad
\hat s(x)=\tilde u_{\mathrm r}(x)\,\vec e_z\,\tilde u_{\mathrm r}^{\natural}(x),
$$

with $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}$ and $\hat s^{2}=-e_t$. The frame element is an element of $\mathbb{B}_\Phi$ and is written with its indices low, as the frame conventions require; the spin direction is a real unit vector and the spin element is $\rho_{\mathrm{num}}^{1/2}(\hbar/2)i\hat s$ in $\mathbb{B}_\Psi$.

The triple is not a set of independent fields. The Dirac equation ties the three, and the tie is what the polar article leaves open in its §*What the general field leaves open*: the equation relates the two parts' words, and the algebra supplies no canonical rule fixing one from the other. A hydrodynamic reading of the Dirac field has therefore to impose the tie as a closure, exactly as the non-relativistic spin-fluid literature does, and the articles on spin hydrodynamics do that.

### What the triple closes

**Three of the four conservation laws of the fluid are already fixed by the triple, and the fourth is the spin's.** The density and the frame element give the number current and its conservation; the frame element gives the stress element's symmetric part; the spin direction gives the antisymmetric part. The sentence is a summary of the corpus rather than a new derivation: the current is quoted above, the stress is the imported tensor of [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html), and the antisymmetric part is the subject of [Spin Conservation and the Frenkel Condition](spin-conservation-and-the-frenkel-condition.html).

The accounting explains why the Dirac fluid needs one more equation than the scalar fluid. A scalar fluid at a point has a density, a pressure and a velocity: one thermodynamic function and a direction, with the velocity normalised. A spin fluid has in addition a direction that is not the velocity's, so it needs an equation for that direction's transport. The equation is not optional, because without it the antisymmetric part of the stress is undetermined and the fluid's angular momentum is not conserved.

### The two-fluid reading is not available here

**The Dirac field does not split into a condensate and a normal part.** The split of [The Two-Fluid Model in Biquaternionic Form](the-two-fluid-model-in-biquaternionic-form.html) is a split of the state's entropy content, and the Dirac field of a pure plane wave carries none. A reader who wants a two-fluid reading of the Dirac field has to add a thermal component, which is what the partition function of [Equilibrium Partition Function in a Moving Frame](equilibrium-partition-function-in-a-moving-frame.html) supplies. This article's fluid is the zero-entropy component of that construction, and its spin is the spin of the condensate.

## What Is Established and What Is Interpretation

**Established.** The polar data of the Dirac field — the frame element, its square as the velocity, the rotor's image as the spin, the current as the density times the frame — imported from the polar article. The Gordon split into convection and magnetisation parts, imported from the Gordon article. The closure of the scalar velocity one-form, which is exact and follows from $\tilde P_\Phi=\tilde\nabla S_{\tilde\Xi}$. The non-closure of the Dirac velocity, with the counting and the closure conditions displayed. The vorticity as the antisymmetrised frame gradient, with the shear-flow check. The frozen-frame sector and the four losses.

**Interpretation.** That the Dirac fluid is *a* spin fluid in the sense of the non-relativistic spin-hydrodynamics literature. The correspondence is by structure — a density, a velocity and an independent spin direction, with the spin entering the current as a bound current — and not by derivation: nothing here shows that the corpus's spin direction obeys the literature's transport equation. What the corpus supplies is the exact kinematic triple and its algebra; the transport equation is a closure that the later articles add.

**Not claimed.** It is not claimed that the vorticity and the spin direction are tied at each event. They are independent parameters of the word, and the tie is the field equation's, not the kinematics'. It is not claimed that the frozen-frame sector is the non-relativistic limit: the non-relativistic limit of the polar article is a different reduction, in which the frame loses its boost and the rotor precesses, and a reader who wants that limit should read it there.

## Summary

The Dirac field's fluid is a triple at each event: the proper density $\rho_{\mathrm{num}}$, the frame element $\tilde V_\Phi=ic\tilde U_{\Psi,\mathrm b}^{-2}=\gamma(ic e_t+\vec v)$ with $\langle\tilde V_\Phi\rangle_{\natural}=-c^{2}$, and the spin direction $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$. The current is the density times the frame element, the spin is the density's square root times $(\hbar/2)i\hat s$, and the central angle is read by neither. The Gordon decomposition splits the current into a convection part and a bound spin part, which is a magnetisation current and contributes nothing to the total charge.

The flow is not a gradient. The scalar field's velocity is $\tilde\nabla S_{\tilde\Xi}/m$, so its one-form is closed identically; the Dirac field's velocity is a unit element squared, so its one-form is closed only when the frame is constant. The counting makes the obstruction visible: a unit timelike element carries three functions of the coordinates and a gradient carries one, so two functions at each event are unaccounted for, and those two are the frame's variation. The vorticity $\omega_{\mu\nu}=\partial_\mu v_{\Phi,\nu}-\partial_\nu v_{\Phi,\mu}$ is the antisymmetrised gradient of the frame element, read through the velocity; it vanishes for the scalar flow, it is non-zero for a shear flow with a varying rapidity, and the check gave a circulation of $0.434\,555\,977\,568\,337$ against the same closed form to fifteen digits.

The scalar case is the frozen-frame sector: with no frame element there is nothing whose gradient could open the one-form, and with a constant frame the flow is rigid and a rigid one-form is exact. Freezing the frame loses the vorticity, the spin part of the current, the magnetisation current and the antisymmetric stress. What remains is a dust with a constant spin direction, which is the scalar fluid of the polar-form article up to the phase.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, with $\vec e_\eta^{2}=-e_t$ |
| $i$ | Central scalar imaginary |
| $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\delta_{\mu\nu}$ | The one metric, all coefficients $+1$; indices stay low |
| $\tilde\Xi=\rho\tilde U$ | The Dirac field as scale times frame element |
| $\rho=\sqrt{\langle\tilde\Xi\rangle_{\natural}}$ | The scale; the polar article calls it $r$ |
| $r=\lvert\rho\rvert$ | Its modulus |
| $\tilde U$ | The frame element, a unit element of $\mathbb{B}$ |
| $\rho_{\mathrm{num}}=\langle\tilde\Xi\rangle_{\natural}=r^{2}$ | Proper density |
| $\theta_{\mathrm{rpd}}$ | Rapidity of the boost |
| $\gamma=\cosh\theta_{\mathrm{rpd}}$ | Lorentz factor |
| $\vec u_{\mathrm b}$ | Unit vector of the boost axis |
| $\vec v=c\tanh\theta_{\mathrm{rpd}}\vec u_{\mathrm b}$ | Three-velocity |
| $\tilde V_{\Phi}=ic\tilde U_{\Psi,\mathrm b}^{-2}$ | Four-velocity of the fluid |
| $\tilde U_{\Psi,\mathrm b}$ | The boost factor of the frame |
| $\tilde u_{\mathrm r}$ | The spatial rotor |
| $\hat s=\tilde u_{\mathrm r}\vec e_z\tilde u_{\mathrm r}^{\natural}$ | Spin direction, with $\hat s^{2}=-e_t$ |
| $\tilde S_{\Psi,\mathrm{sp}}=\rho_{\mathrm{num}}^{1/2}\frac{\hbar}{2}i\hat s$ | Spin element, Hermitian |
| $\tilde J_{\Phi}=\rho_{\mathrm{num}}\tilde V_{\Phi}$ | Number current |
| $v_{\Phi,\mu}$ | Components of $\tilde V_\Phi$, index low |
| $\omega_{\mu\nu}=\partial_\mu v_{\Phi,\nu}-\partial_\nu v_{\Phi,\mu}$ | Vorticity 2-form |
| $\tilde P_{\Phi}=\tilde\nabla S_{\tilde\Xi}$ | Four-momentum of the scalar field |
| $S_{\tilde\Xi}$ | Action of the scalar field |
| $\theta_{\mathrm{phs}}$ | Unused here; the scalar phase is $S_{\tilde\Xi}/\hbar$ |
| $k_m=mc/\hbar$ | Mass wave number |
| $\Sigma_{\mu\nu}$ | Spin generator of the Gordon decomposition |
| $\varepsilon_\mu$ | Signature weight, $+1$ temporal and $-1$ spatial |
| $\langle\tilde Q\rangle_{\natural}$ | Quaternionic norm |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |
| $c$ | Speed of light in the medium |

## Further Reading

- T. Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 2–80, for the spin fluid, its vorticity and the spin's contribution to the current.
- David Hestenes, "Space–time structure of the Dirac theory," in *Clifford Algebras and their Applications in Mathematical Physics* (Reidel, 1986), for the rotor reading of the Dirac spinor and the velocity as a bilinear of the frame.
- F. Halbwachs, P. Hillion and J.-P. Vigier, "Lagrangian formulation of the rotational hydrodynamical model of spinning particles," *Il Nuovo Cimento* **33** (1964) 221, for the spin fluid's kinematics.
- Walter Gordon, "Der Comptoneffekt nach der Schrödingerschen Theorie," *Zeitschrift für Physik* **40** (1926) 117–133, for the decomposition of the current.
- W. Israel, "Relativistic thermodynamics, thermofield statistics and superfluids," *Journal of Non-Equilibrium Thermodynamics* **11** (1986) 295, for the thermodynamic reading of a fluid with an internal degree of freedom.
- The companion articles: [The Polar Form of the Dirac Equation in Biquaternionic Form](the-polar-form-of-the-dirac-equation-in-biquaternionic-form.html), [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](the-gordon-decomposition-of-the-dirac-current-in-biquaternionic-form.html), and [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html).
