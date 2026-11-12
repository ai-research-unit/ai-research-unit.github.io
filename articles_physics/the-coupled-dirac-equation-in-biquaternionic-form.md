# __The Coupled Dirac Equation in Biquaternionic Form__

## Introduction

The **coupled Dirac equation** is the biquaternion Dirac equation with the gradient replaced by the covariant derivative of *The Gauge Principle in Biquaternionic Form*. The connection is the potential biquaternion $\tilde A_{\Phi}$ of *Maxwell's Equations in the Biquaternionic Formulation*, its gauge law is

$$
\tilde A_{\Phi,2}=\tilde A_{\Phi}-\tilde\nabla_\Phi\Gamma,
$$

and the covariant derivative is

$$
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi},
$$

acting by left multiplication. Here $\Gamma$ is a real gauge function and $ϙ$ is the charge. The coupling is not an addition: it is the term the localization of the algebra's central phase forces.

**The equation.**

$$
\boxed{\;\tilde\nabla_{\mathrm{gco}}\tilde\Xi_R=k_m\tilde\Xi_L,
\qquad
\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\Xi_L=k_m\tilde\Xi_R\;}
$$

with $\tilde\nabla_{\mathrm{gco}}^{\natural}=(\tilde\nabla_\Phi)^{\natural}+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}^{\natural}$ the quaternion conjugate of the operator, and with $k_m=mc/\hbar$ the mass wave number. In the massless case the two members decouple, $\tilde\nabla_{\mathrm{gco}}\tilde\Xi_R=0$ and $\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\Xi_L=0$.

**Three things are established here.**

*First, the prescription attaches to the pair and not to the two-sided form.* The two-sided form of the parent carries its mass in a conjugation and a right multiplication, so it has no continuous central phase to localize, and minimal coupling cannot be transferred to it. This is a theorem about the two displays, and it is the reason the corpus's coupled equation has the shape it has.

*Second, the coupled equation is exactly gauge covariant, massive as well as massless.* The mass term is linear in the field and the local phase is one central scalar multiplying the field from the left, so the mass acquires the same factor as the derivative. The mass breaks the *relative* phase of the two parts and leaves the common one intact.

*Third, the conserved current exists and it is not a product of the field with its conjugate.* The algebra supplies the current as a pairing with two fixed frame units; its vector part is the difference of the two parts' currents, not their sum. The naive bilinear $i\tilde\Xi\tilde\Xi^{*}$ is gauge invariant and of the density sign, and it is not conserved, because it carries the sum. The derivation, the counterexample and the repaired object are *The Variational Principle and the Coupled Dirac Equation in Biquaternionic Form*, and this article states the result once and cites it.

What this article does **not** do is derive the polar form or the action. Those are the companion articles, and each stands on its own statements:

- *The Coupled Dirac Equation in Biquaternionic Polar Variables* substitutes the polar word into the equation and reads the kinetic momentum, the kinetic velocity and the spin transport in the background.
- *The Variational Principle and the Coupled Dirac Equation in Biquaternionic Form* states the action, derives the Noether currents, and settles the current question.
- *The Variational Principle and the Coupled Dirac Equation in Biquaternionic Polar Variables* substitutes the word into the *coupled action* and reads the constraint structure.

**What is new here, and what is inherited.** The equation, the gauge law and the covariance proof are the gauge principle's, read as an operator statement on the Dirac field. Inherited from *The Dirac Equation in Biquaternionic Form* are the field, the pair and the value. New in this article are the solutions in a constant potential, the constants of motion for a static connection, the Larmor rate of the frame, and the theorem that separates the pair from the two-sided form. The article is therefore a structural hub and not a restatement.

## The Field and Its Phase Symmetry

**The field.** $\tilde\Xi(\tilde Q)$ is one element of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with four complex coefficients, that is eight real numbers. It satisfies the free pair

$$
\tilde\nabla_\Phi\tilde\Xi_R=k_m\tilde\Xi_L,
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_L=k_m\tilde\Xi_R,
$$

the two members acting on the two parts of the one element. The subscript names one of two parts and no more: a product takes the letter of its right factor and a left multiplication keeps the letter, so the letters are a bookkeeping device for the two sides of the algebra and not a second carrier. The parent states this in full and nothing is repeated here.

**The real structure.** The antilinear involution

$$
\tilde\Xi^{\flat}=-\tilde\Xi^{*}=-\overline{\tilde\Xi^{\natural}}
$$

has the material sector $\mathbb{B}_{\Phi}$ as its fixed space. It is the algebra's real structure and it is not the mass. A mass term built on $\flat$ would acquire the factor $\lambda^{2}$ under a local central phase and would be form-invariant only for $\lambda=\pm1$; the parent's mass term pairs $\tilde\Xi_L$ with $\tilde\Xi_R$ and acquires $\lambda$.

**The symmetry to be localized.** A constant central phase

$$
\tilde\Xi\longmapsto\exp(i\theta_{\mathrm{cen}})\tilde\Xi
$$

is a symmetry of the pair, massive or massless, because a central constant commutes with the units and with the derivatives and so passes through both members. Here $\theta_{\mathrm{cen}}$ is real: it is the argument of a unit complex number. One and the same $\lambda$ multiplies both members, so the pair scales uniformly and the linear mass term is invariant.

**What the mass breaks is the relative phase.** With $\varsigma$ a nonzero central constant, the massless pair is invariant under

$$
\tilde\Xi_R\longmapsto\varsigma\,\tilde\Xi_R,
\qquad
\tilde\Xi_L\longmapsto\varsigma^{-1}\tilde\Xi_L,
$$

because each member acquires $\varsigma\varsigma^{-1}=1$. The massive pair is not: its two sides acquire $\varsigma$ and $\varsigma^{-1}$, so it is form-invariant only for $\varsigma^{2}=1$. A *local* $\varsigma$ fails already at $k_m=0$, since the derivative acts on $\varsigma$ and the two derivative terms do not cancel. The mass therefore keeps the common phase and breaks the relative one.

**The charge.** $ϙ$ is a parameter of the field. The algebra fixes neither its value, nor its sign, nor its quantization. For the electron $ϙ=-e$, and the value is inserted rather than derived.

## The Coupling Prescription

**The prescription.** Replace the gradient by the covariant derivative,

$$
\tilde\Xi\longmapsto\tilde\nabla_\Phi\tilde\Xi+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}\tilde\Xi,
$$

that is, $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}$ acting from the left. The term $\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}\tilde\Xi$ is the **interaction term**, and it is exactly the term the localized central phase forces.

**The conjugate entry is not the negative of the entry.** Since $\natural$ fixes $e_t$ and negates the three spatial units, a potential with real coefficients has

$$
\tilde A_{\Phi}^{\natural}=A_te_t-\sum_\eta A_\eta\vec e_\eta .
$$

For a purely electric potential $\tilde A_{\Phi}^{\natural}=+\tilde A_{\Phi}$, so the two members carry opposite entries; for a purely magnetic one $\tilde A_{\Phi}^{\natural}=-\tilde A_{\Phi}$, so they carry the same entry; for a general potential it is neither. The second member is the conjugate of the first and not the first with $ϙ\to-ϙ$.

**The asymmetry is not a decomposition.** It is tempting to read the electric and magnetic parts as two couplings sharing a coefficient, since each is self-conjugate up to a sign. The gauge law rules this out: the entry absorbs $-\tilde\nabla_\Phi\Gamma$, which has a time part and a space part, so a purely electric potential does not stay purely electric under a general gauge function. Purity is a property of a gauge and not of the entry. Only the whole covector is covariant.

**Component form.** Write $\tilde A_{\Phi}=\sum_\mu A_\mu e_\mu$ with complex scalar coefficients $A_\mu$ — the abelian case, in which the connection coefficients are central scalars and commute with one another and with the units. Since each $A_\mu$ is central, the covariant derivative separates:

$$
\tilde\nabla_{\mathrm{gco}}=\sum_\mu e_\mu\,\tilde\nabla_{\mathrm{gco},\mu},
\qquad
\tilde\nabla_{\mathrm{gco},\mu}=\frac{\partial}{\partial R_\mu}+\frac{i\,ϙ}{\hbar}A_\mu,
$$

with $\partial/\partial R_t=-i\,\partial/\partial r'_t$ and $\partial/\partial R_\eta=\partial/\partial x_\eta$. Each $\tilde\nabla_{\mathrm{gco},\mu}$ is a central scalar operator: the derivative acts on the coefficients only and the $A_\mu$ are complex numbers, so every component commutes with every element of $\mathbb{B}$ and with every unit.

**That one line is the whole of the polar reading.** Because each component is central, the interaction term passes through the field and can be written on either side of it. It cannot rotate a non-central factor; it multiplies the whole word. The polar companion draws every consequence of that sentence, and this article uses it once, in §*Larmor Precession and the Gyromagnetic Ratio*.

**The connection is a material-sector object.** For a real gauge function $\Gamma$, the gauge law keeps $\tilde A_{\Phi}$ in $\mathbb{B}_{\Phi}$. The coupling is therefore the coupling of the Dirac field to a material-sector connection, and the ingredient $\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}$ is Hermitian,

$$
\bigl(i\tilde A_{\Phi}\bigr)^{*}=-i\,\tilde A_{\Phi}^{*}=i\tilde A_{\Phi},
$$

since $\tilde A_{\Phi}^{*}=-\tilde A_{\Phi}$ on $\mathbb{B}_{\Phi}$. The factor $i$ is what converts the anti-Hermitian connection into a Hermitian coupling.

**Sign convention.** The pair of signs is the gauge principle's: $\tilde A_{\Phi,2}=\tilde A_{\Phi}-\tilde\nabla_\Phi\Gamma$ with $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}$ and $\lambda=\exp(i\theta_{\mathrm{gau}})$. Here

$$
\theta_{\mathrm{gau}}:=\frac{ϙ\,\Gamma}{\hbar}
$$

is the gauge angle. The parent's open question writes the standard physics convention $\partial/\partial R_\mu\to\partial/\partial R_\mu-\frac{i\,ϙA_\mu}{\hbar}$, with the opposite sign; that is the same coupling with the opposite sign of $ϙ$, and this article inherits the gauge principle's sign and does not flip it. *Relativistic Mechanics from the Dirac Wave* writes $\vec p-ϙ\vec A$ for the same reason, and the two writings are one coupling.

**Left action, and the mirror through $\natural$.** Every coupling used here acts on the left. The mirror — derivative and connection both on the right — is not a second prescription. The renaming theorem gives

$$
\bigl(\tilde\Xi\,\tilde\nabla_{\mathrm{gco}}\bigr)^{\natural}=\tilde\nabla_{\mathrm{gco}}^{\natural}\,\tilde\Xi^{\natural},
$$

so the right-action equation on $\tilde\Xi$ is the left-action equation on $\tilde\Xi^{\natural}$, with the operator the second member already carries. The side is given by position, and $\natural$ is what changes it.

**What is not covariant is the mixed insertion.** The left gradient with the connection inserted on the right gives, on a gauge-transformed field,

$$
\frac{i\,ϙ}{\hbar}\,\lambda\bigl[\tilde\nabla_\Phi\Gamma,\ \tilde\Xi\bigr],
$$

which vanishes for every field only when $\tilde\nabla_\Phi\Gamma$ is central, that is, only for a constant gauge function. The two consistent constructions are the two sides on which the algebra can act, and the choice between them is a choice of matter representation. This article states the left-action form, records the mirror, and leaves the choice where the action makes it (§*Open Questions* and the variational companion).

## Which Equation the Prescription Attaches To

Two forms are in circulation, and the prescription attaches to one of them. That is a theorem and not a preference.

**The pair.** The field is one element and $\lambda$ is one central element multiplying it from the left. The pair is covariant because $\lambda$ is central: it passes through both gradients and through the mass. §*Gauge Covariance* computes it.

**The two-sided form.** The parent also carries a single equation on a general element in which the derivative acts on the left and the mass on the right,

$$
-(\tilde\nabla_\Phi)^{\natural}F-k_m\,i\,\overline{F}\,\vec u=0,
$$

with the bar the complex conjugation of the coefficients and $\vec u$ the declared unit of the frame. The mass term combines a conjugation, the central $i$ and a right multiplication. It is not a scalar multiple of the field.

**Under a constant central phase the two terms scale differently.**

$$
-(\tilde\nabla_\Phi)^{\natural}\bigl(\lambda F\bigr)=\lambda\bigl(-(\tilde\nabla_\Phi)^{\natural}F\bigr),
\qquad
-k_m\,i\,\overline{\lambda F}\,\vec u=\bar\lambda\bigl(-k_m\,i\,\overline{F}\,\vec u\bigr),
$$

and $\bar\lambda\ne\lambda$ for non-real $\lambda$. The two-sided form therefore has **no continuous central phase symmetry**; its symmetry group is the real rescalings $F\mapsto rF$ with $r\in\mathbb{R}^{\times}$.

**The theorem.** There is no phase to localize, so there is no covariant derivative to build, so the minimal-coupling prescription cannot be transferred to the two-sided form. Coupling that form would be a different construction and this set of articles does not attempt it.

**The two forms carry the same operator content and are not the same statement.** The difference is located in the mass term, which is where a conjugation and a right multiplication replace a scalar. That is why the biquaternion form of the coupling is not fixed by the free equation alone, and why the question "which equation?" has to be asked before "what coupling?".

## Gauge Covariance

The gauge transformation is

$$
\tilde\Xi_2=\lambda\,\tilde\Xi,
\qquad
\lambda=\exp\bigl(i\theta_{\mathrm{gau}}\bigr),
\qquad
\tilde A_{\Phi,2}=\tilde A_{\Phi}-\tilde\nabla_\Phi\Gamma,
\qquad
\Gamma\ \text{real},
$$

with $\lambda$ central and of unit modulus.

**The chain rules.** Because $\lambda$ is a central scalar function, each derivative acts on it coefficient by coefficient:

$$
\tilde\nabla_\Phi\lambda=\frac{i\,ϙ}{\hbar}\bigl(\tilde\nabla_\Phi\Gamma\bigr)\lambda,
\qquad
(\tilde\nabla_\Phi)^{\natural}\lambda=\frac{i\,ϙ}{\hbar}\bigl((\tilde\nabla_\Phi)^{\natural}\Gamma\bigr)\lambda .
$$

**The first member.**

$$
\begin{aligned}
\tilde\nabla_{\mathrm{gco},2}\bigl(\lambda\tilde\Xi_R\bigr)
&=\tilde\nabla_\Phi\bigl(\lambda\tilde\Xi_R\bigr)+\frac{i\,ϙ}{\hbar}\bigl(\tilde A_{\Phi}-\tilde\nabla_\Phi\Gamma\bigr)\bigl(\lambda\tilde\Xi_R\bigr)\\
&=\lambda\,\tilde\nabla_\Phi\tilde\Xi_R+\frac{i\,ϙ}{\hbar}\bigl(\tilde\nabla_\Phi\Gamma\bigr)\lambda\tilde\Xi_R+\frac{i\,ϙ}{\hbar}\lambda\,\tilde A_{\Phi}\tilde\Xi_R-\frac{i\,ϙ}{\hbar}\bigl(\tilde\nabla_\Phi\Gamma\bigr)\lambda\tilde\Xi_R\\
&=\lambda\,\tilde\nabla_{\mathrm{gco}}\tilde\Xi_R .
\end{aligned}
$$

The two $\tilde\nabla_\Phi\Gamma$ terms cancel and the central $\lambda$ moves to the left past $\tilde A_{\Phi}$ and past the field.

**The second member** repeats the computation with $\natural$ throughout, using $\tilde A_{\Phi,2}^{\natural}=\tilde A_{\Phi}^{\natural}-(\tilde\nabla_\Phi)^{\natural}\Gamma$, and gives

$$
\tilde\nabla_{\mathrm{gco},2}^{\natural}\bigl(\lambda\tilde\Xi_L\bigr)=\lambda\,\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\Xi_L .
$$

**Both members are homogeneous with the same factor.**

$$
\tilde\nabla_{\mathrm{gco},2}\tilde\Xi_{R,2}=\lambda\,\tilde\nabla_{\mathrm{gco}}\tilde\Xi_R,
\qquad
\tilde\nabla_{\mathrm{gco},2}^{\natural}\tilde\Xi_{L,2}=\lambda\,\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\Xi_L .
$$

The common factor follows from $\lambda$ being a central *scalar*: $\natural$ negates the three spatial units and fixes the coefficients, so it leaves $\lambda$ alone. Consequently the coupled equation holds in every gauge when it holds in one, and the phase of the field is not observable on its own.

**The second-order consequence.** The covariant derivative satisfies the operator identity

$$
\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}=\sum_{\mu}\tilde\nabla_{\mathrm{gco},\mu}^{2}+\frac{i\,ϙ}{\hbar}\tilde F
$$

(*The Covariant Derivative and Gauge Connection in Biquaternionic Form*), the scalar part being the covariant d'Alembertian and the vector part the curvature. Applying $\tilde\nabla_{\mathrm{gco}}^{\natural}$ to the first member and using the second gives

$$
\Bigl(\sum_{\mu}\tilde\nabla_{\mathrm{gco},\mu}^{2}+\frac{i\,ϙ}{\hbar}\tilde F-k_m^{2}\Bigr)\tilde\Xi_R=0,
$$

a covariant wave equation with a curvature term. The corresponding statement for $\tilde\Xi_L$ carries $\tilde\nabla_{\mathrm{gco}}\tilde\nabla_{\mathrm{gco}}^{\natural}$ in place of $\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}$. The curvature is the part of the connection that no phase can absorb: a gradient can be gauged away and a field strength cannot.

## The Massive Case

Suppose the coupled massive pair holds in one gauge. The left-hand side of the transformed first member is $\lambda\,\tilde\nabla_{\mathrm{gco}}\tilde\Xi_R$, and the right-hand side is

$$
k_m\tilde\Xi_{L,2}=k_m\lambda\,\tilde\Xi_L,
$$

because a linear mass term carries the same factor. The two sides transform identically, with $\lambda$ and not $\bar\lambda$. The massive coupled equation is therefore form-invariant under the local phase, exactly as the massless one is.

**This is the biquaternion form of a standard fact.** A mass term linear in the field is compatible with a gauged continuous $\mathrm{U}(1)$. The two parts acquire the same phase; what the mass forbids is the *opposite* assignment of the two, which is the relative phase of §*The Field and Its Phase Symmetry*.

**What the article does not claim.** It does not declare the standard minimal coupling deficient, and with a linear mass term it does not need to. The massive sector is gauge covariant on the same footing as the massless one. What the biquaternion form adds is the location of the coupling in the algebra: a covariant derivative acting from the left, with the central phase passing through the linear mass and the relative phase broken instead.

**The alternative reading.** A mass term built on the real structure $\flat$, with no continuously charged massive field, remains available — but only for a different equation, one genuinely built on $\flat$. That is a statement about the algebra's real structure and not about this pair, and it belongs to *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form* and to the neutrino article.

## Solutions in a Constant Potential

A constant potential is the one background in which the coupled equation is solved in closed form, and it settles the two things a solution is asked to settle: what the spectrum does and what it does not do.

**A constant potential is pure gauge.** On flat space, constant $A_\mu$ is a gradient: with $\Gamma=-\sum_\mu A_\mu R_\mu$ one has $\partial_\mu\Gamma=-A_\mu$, so $\tilde A_{\Phi}=-\tilde\nabla_\Phi\Gamma$ up to the constant part that adds nothing. Hence the coupled equation with constant $\tilde A_{\Phi}$ is carried to the free equation by the transformation

$$
\tilde\Xi\longmapsto\exp\Bigl(-i\frac{ϙ}{\hbar}\sum_\mu A_\mu R_\mu\Bigr)\tilde\Xi,
$$

which is a multiplication by one central phase with a linear argument.

**What that does to a plane wave.** Write $\tilde\Xi=\tilde\Xi_0\exp(i\theta)$ with $\theta$ linear and $\tilde\Xi_0$ constant, and let $\tilde K_\Phi=\tilde\nabla_\Phi\theta_{\mathrm{pha}}$ be the canonical wavevector. The gauge factor adds $-\frac{ϙ}{\hbar}\tilde A_{\Phi}$ to the wavevector of the field, so the canonical wavevector and the covariant one are related by

$$
\tilde K_{\Phi,\mathrm{gco}}=\tilde K_\Phi+\frac{ϙ}{\hbar}\tilde A_{\Phi},
$$

and the pair becomes the free pair with $\tilde K_{\Phi,\mathrm{gco}}$ in the place of $\tilde K_\Phi$:

$$
i\tilde K_{\Phi,\mathrm{gco}}\tilde\Xi_0^{R}=k_m\tilde\Xi_0^{L},
\qquad
i\tilde K_{\Phi,\mathrm{gco}}^{\natural}\tilde\Xi_0^{L}=k_m\tilde\Xi_0^{R},
\qquad
\tilde K_{\Phi,\mathrm{gco}}\tilde K_{\Phi,\mathrm{gco}}^{\natural}=-k_m^{2}.
$$

**The mass shell is translated and not resized.** Writing $\tilde K_{\Phi,\mathrm{gco}}=i\kappa_te_t+\vec\kappa$ with real $\kappa_t$ and real $\vec\kappa$, the third relation is

$$
\kappa_t^{2}-|\vec\kappa|^{2}=k_m^{2},
$$

and in terms of the canonical components $\tilde K_\Phi=i\pi_te_t+\vec\pi$ it is

$$
\Bigl(\pi_t+\frac{ϙ}{\hbar}A_t\Bigr)^{2}-\Bigl|\vec\pi+\frac{ϙ}{\hbar}\vec A\Bigr|^{2}=k_m^{2}.
$$

The two displays are one surface and two origins. The radius is $k_m$ in both, the shape is the same, and the potential moves the centre and nothing else. **The translation is the potential's and the gap is $k_m$'s**: a uniform $A_t$ moves every level by $ϙA_t$ and leaves every spacing unchanged, and no constant potential opens a gap.

**The reason, in one line.** A gauge transformation shifts a wavevector by a gradient, and a shift of a variable cannot change a radius. A gap would need a term with a scale of its own; the algebra has one scalar here, and it is the mass coefficient.

**The vector part of the curvature vanishes.** For constant $\tilde A_{\Phi}$ the field strength is zero, so the second-order operator of §*Gauge Covariance* is the free one with every component shifted at once. That is the same statement from the second-order side, and it agrees.

## Constants of Motion

A static connection gives the equation its translation and rotation symmetries, and the charges are the standard ones with the gradient made covariant.

**Energy.** If $\tilde A_{\Phi}$ does not depend on $r'_t$, the equation is invariant under $r'_t\mapsto r'_t+\epsilon$, and the conserved charge is

$$
E=\int\mathrm{d}^{3}r\;\mathrm{Re}\,\mathrm{Sc}\bigl[\tilde\Xi^{*}\,i\hbar c\,\partial_{r'_t}\tilde\Xi\bigr].
$$

On a plane wave it is $\hbar c\,\kappa_t$ in the covariant reading and $\hbar c\,\pi_t$ in the canonical one, and the two differ by $ϙA_t c$: the energy of the coupled system is the kinetic energy, and the canonical energy is the kinetic energy less the potential's share. That difference is the whole of the constant-potential shift of §*Solutions in a Constant Potential*.

**Momentum.** If $\tilde A_{\Phi}$ does not depend on $x_\eta$, the charge is the corresponding component of

$$
\vec P=\int\mathrm{d}^{3}r\;\mathrm{Re}\,\mathrm{Sc}\bigl[\tilde\Xi^{*}\,(-i\hbar)\nabla\tilde\Xi\bigr],
$$

and again the covariant momentum is the canonical one plus $\frac{ϙ}{\hbar}\vec A$ in units of $\hbar$. A uniform vector potential therefore shifts the momentum and not the dispersion.

**Angular momentum, and the gauge-covariant modification.** Under a spatial rotation the potential rotates with the field, so the conserved generator is the sum of the orbital part and the spin part, with the connection entering the orbital part through the covariant derivative:

$$
\vec J=\int\mathrm{d}^{3}r\Bigl\{\mathrm{Re}\,\mathrm{Sc}\bigl[\tilde\Xi^{*}\bigl(\vec r\times(-i\hbar\nabla_{\mathrm{gco}})\bigr)\tilde\Xi\bigr]+\vec S\Bigr\},
$$

where $\vec S$ is the spin of the polar companion. **The modification is not optional.** A rotation that moves the field and leaves the potential fixed is not a symmetry of the coupled equation; only the rotation that moves the potential with the field is. The covariant derivative is what makes the orbital generator transform as a vector under that rotation, and with the ordinary derivative the orbital part alone would not be conserved.

**What is not claimed.** The charges above are formal: they are the Noether charges of the constant setting, written with the covariant derivative in place of the gradient. Their convergence, their regularization and their agreement with the operator expressions are not examined here.

## Larmor Precession and the Gyromagnetic Ratio

The coupled equation contains the magnetic moment, and the place it sits is fixed by the algebra rather than chosen.

**The mechanism, in one sentence.** The factor of the field that carries the velocity also carries the magnetic moment, because both are read from the same boost; a substitution that acts on the gradient cannot give the two different coefficients.

**The polar statement.** In the word $\tilde\Xi=r\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\Psi,\mathrm{b}}\tilde u_{\mathrm r}$, the velocity is the boost, $\tilde V_{\Phi}=ic\,\tilde U_{\Psi,\mathrm{b}}^{-2}$, and the magnetic moment is the same boost multiplied by the rotor's direction. The connection is central in each component (§*The Coupling Prescription*), so it cannot touch the rotor and it cannot touch the boost either: it multiplies the whole word. What it does is shift the phase gradient, and the phase gradient is the momentum. The magnetic coupling therefore enters as a shift of the momentum and not as a torque on the frame.

**The Larmor rate, read off.** A frame whose boost axis precesses in a magnetic field precesses at

$$
\omega_{\mathrm{Lar}}=\frac{ϙB}{m},
$$

which is the classical Larmor frequency for a moment $\mu=ϙ\hbar/2m$ in the field $B$. The factor is the one the boost carries: the same $\hbar/2m$ that turns the gradient into a velocity turns the field strength into a rotation rate. No second coefficient is available, so the gyromagnetic ratio is two in the units where the orbital one is one.

**What this locates and what it does not derive.** It locates the coupling: the frame factor that carries the velocity also carries the magnetic moment, so a minimal substitution cannot produce two different coefficients. It does not derive the value from first principles, because the value is the statement that the two readings come from one factor, and *The Classical Origin of $g=2$ in Biquaternionic Form* carries the derivation with the expansion. What this article contributes is the reason the two cannot differ: there is one boost in the word, and both readings are functions of it.

**The limit that shows it.** In the non-relativistic limit the whole of the coupling is the substitution $\vec p\mapsto\vec p+ϙ\vec A$ and $E\mapsto E+ϙ\phi$, and the spin term appears at the same order because it comes from the same factor. A coupling that entered at a different order would have to come from a different place in the algebra, and the algebra has one place: the central imaginary bracket.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy, and the reasons are in *Why AXF Matrices instead of Pauli and Gamma Matrices*. The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra, and they are used in this section only, as the frame in which the algebra's own operators can be compared with the standard matrices.

**The frame.** Write $L_a\tilde\Xi=a\tilde\Xi$ and $R_b\tilde\Xi=\tilde\Xi b$ for left and right multiplication, and $c(M)$ for the matrix of a basis operator in the basis of the sixteen products. The four gammas and $\gamma_5$ are single basis operators:

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad
\gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad
\gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad
\gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad
\gamma_5=-iL_{e_t}R_{\vec e_z}.
$$

A single basis operator is a tensor $a\otimes b$ read through $L_aR_b$, so its coefficient matrix has rank one; the basis operators form the cone $\operatorname{rank}c(M)\le1$, and every element of $M_4(\mathbb{C})$ is a sum of at most four of them. $\gamma_5$ is a pure right multiplier, which is what makes it a chirality: its side is the right slot, and its eigenvalues are $\pm1$ with multiplicity two each.

**The current in the older spelling.** The conserved current of the older literature is the bilinear built with the generator of the coordinate and with the adjoint row,

$$
j_\mu=\tilde\Xi^{\dagger}iR_{\vec e_x}\,iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\tilde\Xi,
\qquad
\nu(t)=x,\ \nu(\eta)=y .
$$

Its time component is $\tilde\Xi^{\dagger}\tilde\Xi$ and its spatial components are $\tilde\Xi^{\dagger}\alpha_\eta\tilde\Xi$ with $\alpha_\eta=L_{\vec e_\eta}R_{\vec e_z}$.

**The dictionary, and the point of making it.** Every ingredient of that display is a basis operator of the algebra except one: the adjoint row is built on $iR_{\vec e_x}$, a one-sided operator. Read as a pairing, the same object is

$$
j_\mu=\mathrm{Sc}\bigl(\tilde\Xi^{*}\,i\,\bigl(i e_\mu\tilde\Xi\,\vec e_{\nu(\mu)}\bigr)\vec e_x\bigr),
$$

a scalar part of three factors: the field, a unit, the field again. **The adjoint row and the right multiplier $\vec e_x$ are the same datum in two spellings.** The older form hides it inside the adjoint; the pairing shows it as the last factor, and the last factor is a frame unit and not a field.

**Why this matters here.** It says that the conserved current is available inside the algebra, as a *triple* product with two fixed frame units, and that no fourth object and no second carrier is needed. It also says why the naive bilinear $i\tilde\Xi\tilde\Xi^{*}$ cannot be the current: a product of the field with its conjugate carries no fixed unit, so the two parts enter with the same sign, and the current needs them with opposite signs. The variational companion proves this, computes the repaired object, and shows the failure on an exact solution.

**The identities the corpus cites.** With $\varepsilon=(1,-1,-1,-1)$ the sign vector of the basis operators,

$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,
\qquad
(\gamma_\eta)^{2}=-I_4,
\qquad
\gamma_5^{2}=I_4,
\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$

$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\ \ (\mu\ne\nu),
\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,
\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},
\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$

With one index raised, $\gamma^{\mu}=-\varepsilon_\mu\gamma_\mu$, so $\sum_\mu\gamma^{\mu}\gamma_\mu=-4I_4$, $\sum_\mu\gamma^{\mu}\gamma_\alpha\gamma_\mu=2\gamma_\alpha$, $\sum_\mu\gamma^{\mu}\gamma_\alpha\gamma_\beta\gamma_\mu=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$, and $\sum_\mu\gamma^{\mu}\gamma_\gamma\gamma_\beta\gamma_\alpha\gamma_\mu=-2\gamma_\gamma\gamma_\beta\gamma_\alpha$.

**What this section does not do.** It does not use the gammas as a tool. The coupled equation, its covariance and its solutions are stated in the algebra throughout; the gammas appear here so that a reader who knows them can place the algebra's objects, and nowhere else.

## Open Questions

**The non-abelian extension.** When the connection is $\mathbb{B}$-valued it is no longer central, so it no longer commutes with the field, and the left/right question becomes sharp: the order of the factors is part of the statement. The companions on the covariant derivative, on non-abelian fields and on the Yang–Mills equation place the field, but the choice is made there and not forced. Whether the central connection is the *only* one for which the coupling is unambiguous is a question the abelian construction does not answer.

**Matter representation.** The action fixed by §*Which Equation the Prescription Attaches To* couples from the left, and the right-action mirror is the same construction seen through $\natural$. The mixed insertion is not covariant. Whether the physical field is the one the connection multiplies from the left or its $\natural$-image is a choice of representation, and the variational companion states where the choice is made. What is not settled is whether anything inside the algebra distinguishes the two.

**Empirical content.** As everywhere in the framework: does any of this yield a prediction that distinguishes it from standard gauge theory? The coupling as presented is a reformulation, and the framework-level question of empirical contact remains open.

**The relative phase.** The mass keeps the common central phase and breaks the relative one. Whether the relative one can be gauged, and whether the central-element structure supplies anything analogous to a Goldstone statement, is not settled. The polar companion computes the transformation of the angle and says why the chart has no parameter for it.

## Summary

The coupled Dirac equation of the biquaternion framework is

$$
\tilde\nabla_{\mathrm{gco}}\tilde\Xi_R=k_m\tilde\Xi_L,
\qquad
\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\Xi_L=k_m\tilde\Xi_R,
\qquad
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi},
$$

with the interaction term $\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}\tilde\Xi$ that the localized central phase forces. In the massless case the members decouple.

The prescription attaches to the one-sided pair and not to the two-sided form, because the two-sided form's mass term is a conjugation and a right multiplication and carries no continuous central phase to localize. That is a theorem about the two displays.

The coupled equation is exactly gauge covariant, massive as well as massless, with $\tilde\Xi_2=\lambda\tilde\Xi$ and $\tilde A_{\Phi,2}=\tilde A_{\Phi}-\tilde\nabla_\Phi\Gamma$: both members transform with the same $\lambda$, and the linear mass term acquires it too. The mass breaks the relative phase of the two parts and not the common one.

A constant potential is pure gauge, so a plane wave sees it as a shift of the wavevector: $\tilde K_{\Phi,\mathrm{gco}}=\tilde K_\Phi+\frac{ϙ}{\hbar}\tilde A_{\Phi}$, the mass shell $\kappa_t^{2}-|\vec\kappa|^{2}=k_m^{2}$ is translated and not resized, and no constant potential opens a gap. Squaring the pair gives the covariant wave equation with the curvature term $\frac{i\,ϙ}{\hbar}\tilde F$, and for constant $\tilde A_{\Phi}$ that term vanishes.

The constants of motion of a static connection are the energy, the momentum and the angular momentum, with the gradient made covariant in each. The angular momentum needs the covariant derivative and not the ordinary one, because a rotation that moves the field and leaves the potential fixed is not a symmetry.

The magnetic moment sits in the same factor as the velocity, so the Larmor rate is $ϙB/m$ and the gyromagnetic ratio is two; the article locates the coupling and cites the derivation of the value.

The conserved current is not a product of the field with its conjugate. It is a pairing with two fixed frame units, which is the older literature's adjoint row in the algebra's spelling:

$$
j_\mu=\mathrm{Sc}\bigl(\tilde\Xi^{*}\,i\,\bigl(i e_\mu\tilde\Xi\,\vec e_{\nu(\mu)}\bigr)\vec e_x\bigr).
$$

The naive $i\tilde\Xi\tilde\Xi^{*}$ is gauge invariant and of the density sign, and the two parts enter it with the same sign, so it is not conserved. The variational companion proves the positive statement and exhibits the failure.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^{2}=-e_t$ |
| $i$ | Central scalar imaginary, $i^{2}=-e_t$ |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part, the coefficient of $e_t$; $\mathrm{Tr}=2\,\mathrm{Sc}$ |
| $\mathbb{B}_{\Phi},\ \mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\tilde\Xi=\tilde\Xi_L+\tilde\Xi_R$ | The field, one element of $\mathbb{B}$; the letters name the two parts |
| $\tilde\Xi^{\flat}=-\tilde\Xi^{*}$ | The anti-Hermitian conjugate; the algebra's real structure, not the mass |
| $\tilde\nabla_\Phi,\ (\tilde\nabla_\Phi)^{\natural}$ | The gradient and its quaternion conjugate |
| $k_m=mc/\hbar$ | Mass wave number |
| $\tilde A_{\Phi}=A_te_t+\sum_\eta A_\eta\vec e_\eta$ | Potential biquaternion, an element of $\mathbb{B}_{\Phi}$ |
| $\tilde A_{\Phi,2}=\tilde A_{\Phi}-\tilde\nabla_\Phi\Gamma$ | Gauge law of the connection; $\Gamma$ real |
| $\lambda=\exp(i\theta_{\mathrm{gau}})$ | Local central phase; $\theta_{\mathrm{gau}}=ϙ\Gamma/\hbar$ |
| $ϙ$ | Charge; the algebra fixes neither its value nor its sign |
| $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}$ | Covariant derivative, left action |
| $\tilde\nabla_{\mathrm{gco},\mu}=\partial/\partial R_\mu+\frac{i\,ϙ}{\hbar}A_\mu$ | Components; central scalars |
| $\tilde\nabla_{\mathrm{gco}}^{\natural}=(\tilde\nabla_\Phi)^{\natural}+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}^{\natural}$ | Its $\natural$-image; the operator of the second member |
| $\partial/\partial R_t=-i\,\partial/\partial r'_t$ | Material time derivative |
| $\tilde F$ | Field strength; $\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}=\sum_\mu\tilde\nabla_{\mathrm{gco},\mu}^{2}+\frac{i\,ϙ}{\hbar}\tilde F$ |
| $\tilde K_{\Phi,\mathrm{gco}}=\tilde K_\Phi+\frac{ϙ}{\hbar}\tilde A_{\Phi}$ | Covariant wavevector; gauge invariant; in $\mathbb{B}_{\Phi}$ |
| $\kappa_t,\vec\kappa$ | Components of $\tilde K_{\Phi,\mathrm{gco}}$; $\kappa_t^{2}-|\vec\kappa|^{2}=k_m^{2}$ |
| $\pi_t,\vec\pi$ | Components of the canonical $\tilde K_\Phi$; the mass shell is displaced by $-\frac{ϙ}{\hbar}\tilde A_{\Phi}$ |
| $j_\mu=\mathrm{Sc}\bigl(\tilde\Xi^{*}i(i e_\mu\tilde\Xi\vec e_{\nu(\mu)})\vec e_x\bigr)$ | The conserved current; two fixed frame units |
| $\tilde J_{\Phi,\mathrm{sp}}=i\tilde\Xi\tilde\Xi^{*}$ | The naive bilinear; gauge invariant, of the density sign, **not conserved** |
| $\gamma_\mu,\ \gamma_5$ | Basis operators of the legacy frame; used in one section only |

## Further Reading

- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the field, the pair and the value.
- [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html), for the localization of the central phase and the pair of signs.
- [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html), for the operator identity with the curvature.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html), for the potential biquaternion and the four-current.
- [The Coupled Dirac Equation in Biquaternionic Polar Variables](the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), for the word in the background.
- [The Variational Principle and the Coupled Dirac Equation in Biquaternionic Form](the-variational-principle-and-the-coupled-dirac-equation-in-biquaternionic-form.html), for the action, the Noether currents and the current crux.
- [The Variational Principle and the Coupled Dirac Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-coupled-dirac-equation-in-biquaternionic-polar-variables.html), for the coupled action in the chart.
- [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](the-gordon-decomposition-of-the-dirac-current-in-biquaternionic-form.html), for the pairing that the current is.
- [The Classical Origin of $g=2$ in Biquaternionic Form](the-classical-origin-of-g-2-in-biquaternionic-form.html), for the derivation of the gyromagnetic ratio.
- [Relativistic Mechanics from the Dirac Wave](relativistic-mechanics-from-the-dirac-wave.html), for the Lorentz force and the spin term at first order.
- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the legacy frame is a frame and not the algebra.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original equation and the minimal coupling.
- Hermann Weyl, "Elektron und Gravitation," *Zeitschrift für Physik* **56** (1929) 330–352, for the local phase.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard treatment of minimal coupling and the conserved current.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the gauge-theoretic reading of the covariant derivative in geometric algebra.
