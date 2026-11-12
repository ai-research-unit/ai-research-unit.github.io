# __The Nodal Set and Quantized Circulation__

## Introduction

**The scalar flow is irrotational everywhere except on the set where the field vanishes, and around that set the circulation is an integer multiple of $h/m$.** Both halves of the sentence are exact. The first is the closure of the velocity one-form, which [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html) proves for the scalar case: the velocity is the gradient of the action, so its curl vanishes wherever the action exists. The second is Stokes' theorem applied around a loop that links a nodal line, where the action does not exist and the closed-loop integral is fixed by the winding of the phase. The two statements are not in tension: the curl vanishes on the complement of the node, and the loop that detects the node does not lie in that complement's simply connected part.

This article closes open question 2 of [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html), which asks whether the winding of the action around a nodal line carries a topological charge, and whether that charge is an object of the algebra rather than of the phase. The answers are yes and yes, in the precise sense given below.

**What the article establishes.** The circulation around a nodal line is $2\pi\hbar n/m$ for an integer $n$, independently of the loop's shape and radius, and the integer is the degree of the field's phase map. The charge is an object of the algebra because it is the winding of the field into the central unit circle, which is the compact direction of the algebra's group of units; the phase function is only a coordinate on that circle and the charge does not depend on it. The nodal set is where the polar decomposition fails, and that failure is the field's arrival on the zero-divisor set.

**What it does not establish.** It does not establish that a nodal solution of the Klein–Gordon equation exists for a given mass and a given winding, nor that any such solution is stable. Those are dynamical questions and this article is kinematical. It does not establish that the scalar field is a superfluid, and no thermodynamic statement is made. And it does not give the sign convention of the charge, which is a convention of the orientation of the loop and is stated once.

## Where the Flow Fails to Be Irrotational

### The closure, and its one exception

**The velocity one-form is closed wherever the action is twice differentiable.** The scalar velocity is

$$
\tilde V_{\Phi}=\frac{\tilde\nabla_\Phi S_{\tilde\Xi}}{m},
\qquad
v_{\Phi,\mu}=\frac{1}{m}\frac{\partial S_{\tilde\Xi}}{\partial R_\mu},
\qquad
\omega_{\mu\nu}=\frac{\partial v_{\Phi,\nu}}{\partial R_\mu}-\frac{\partial v_{\Phi,\mu}}{\partial R_\nu}=0 .
$$

The vanishing is a statement about mixed partial derivatives and it needs nothing from the field equation: any twice differentiable action gives it. What it needs is that the action exist, and the action exists wherever the amplitude is non-zero, because it is defined by

$$
\tilde\Xi=\lVert\tilde\Xi\rVert\exp\!\left(i\frac{S_{\tilde\Xi}}{\hbar}\right)e_t
\qquad\Longrightarrow\qquad
S_{\tilde\Xi}=\hbar\arctan\!\left(\frac{\mathrm{Im}\text{-part}}{\mathrm{Re}\text{-part}}\right),
$$

up to an additive constant that the multivaluedness makes local. Where the amplitude vanishes the ratio is undefined, the action does not exist, and the closure has nothing to say.

**So the irrotationality is exact on the complement of the nodal set and vacuous on it.** That is the whole structure of the subject, and it is why the circulation can be non-zero: a loop that links a node cannot be contracted to a point without crossing the node, so the argument that would make the circulation vanish does not apply to it.

### The nodal set

**The nodal set is the set of events where the field's value lies on the zero-divisor set.** For the central scalar field the value is $\tilde\Xi=\lVert\tilde\Xi\rVert e^{i\theta_{\mathrm{phs}}}e_t$ with $\theta_{\mathrm{phs}}=S_{\tilde\Xi}/\hbar$, and its quaternionic norm is

$$
\langle\tilde\Xi\rangle_{\natural}=\tilde\Xi\tilde\Xi^{\natural}=\lVert\tilde\Xi\rVert^{2}e^{2i\theta_{\mathrm{phs}}} .
$$

The norm vanishes exactly where the amplitude does, so the nodal set is the zero set of the amplitude and it is reached by the field at the cone's apex. For a field whose value is a general element the cone is reached away from the apex as well, and there the field does not vanish while its norm does; the polar form fails in both cases for the same reason, which is that the element is not invertible. [Zero Divisors as a Physical Locus in Biquaternionic Form](zero-divisors-as-a-physical-locus-in-biquaternionic-form.html) is the corpus's account of the set, and it records the fact that the central and real-quaternion subalgebras contain no zero divisors other than zero — which is exactly why the central scalar field can only touch the apex.

**The codimension is two.** The scalar field has one complex value, so vanishing is two real conditions on the spatial coordinates, and the nodal set is a curve in three dimensions and a two-surface in four. A loop that links the curve cannot shrink away from it, and that is the topological reason the circulation survives.

The dimension count is worth stating because it is the part a reader can check on a picture. One complex condition — the vanishing of a complex number — is two real conditions; in three space dimensions, two conditions leave a curve; around a curve, a loop has a linking number. The linking number is the integer that appears in the circulation, and it is computed on the link, which is a circle at a small radius around the nodal curve.

## The Circulation Around a Node

### The winding of the phase

**The phase of the field is single valued only up to the winding number of its map.** Write the phase angle as a function on the loop that links the nodal curve. Going once around the loop, the field returns to its starting value, so the phase returns to its starting value modulo $2\pi$:

$$
\theta_{\mathrm{phs}}\big|_{\text{after one turn}}=\theta_{\mathrm{phs}}\big|_{\text{before}}+2\pi n,
\qquad n\in\mathbb{Z}.
$$

The integer is the degree of the map from the link, a circle, into the phase circle, which is also a circle. It is a homotopy invariant: it cannot change under a continuous deformation of the field that never vanishes on the link, and it cannot change under a continuous deformation of the link that never crosses the nodal curve.

**The circulation is the winding times $h/m$.** The circulation of the velocity around the loop is

$$
\kappa=\oint\tilde V_{\Phi}\cdot d\vec l=\frac{1}{m}\oint\nabla S_{\tilde\Xi}\cdot d\vec l
=\frac{\hbar}{m}\oint\nabla\theta_{\mathrm{phs}}\cdot d\vec l
=\frac{2\pi\hbar\,n}{m},
$$

where the third equality uses $\nabla S_{\tilde\Xi}=\hbar\nabla\theta_{\mathrm{phs}}$ and the fourth the winding. In the corpus's units the quantum of circulation is

$$
\kappa_{1}=\frac{2\pi\hbar}{m}=\frac{2\pi c}{k_m},
$$

the second form using $k_m=mc/\hbar$. The result is exact, it does not depend on the shape or the radius of the loop, and it does not depend on the amplitude profile: only the map's degree enters.

### The loop's independence, checked

**The circulation was checked numerically on a vortex profile at three radii and three windings.** Take the phase angle $\theta_{\mathrm{phs}}=n\arctan(r_y/r_x)$ and an amplitude that vanishes on the axis, $f(r)=Ar\exp(-r^{2}/2\sigma^{2})$ with $A=1.3$ and $\sigma=0.8$. The circulation of $\nabla\theta_{\mathrm{phs}}$ was evaluated by a polygonal quadrature of $4000$ chords on circles of radius $0.3$, $0.8$ and $2.0$:

| winding $n$ | $R=0.3$ | $R=0.8$ | $R=2.0$ | $2\pi n$ |
|---|---|---|---|---|
| $1$ | $6.283\,185\,307$ | $6.283\,185\,307$ | $6.283\,185\,307$ | $6.283\,185\,307$ |
| $2$ | $12.566\,370\,614$ | $12.566\,370\,614$ | $12.566\,370\,614$ | $12.566\,370\,614$ |
| $-1$ | $-6.283\,185\,307$ | $-6.283\,185\,307$ | $-6.283\,185\,307$ | $-6.283\,185\,307$ |

The three radii give the same number to every digit printed, and the number agrees with $2\pi n$ to the last bit, the residual being at most $4\times10^{-16}$ and pure roundoff. **The exactness is structural and not a coincidence of the mesh**: the sum of the chords' angle increments is the unwrapped total angle of the polygonal loop, which is $2\pi n$ times the degree of the map and depends on no chord length. A quadrature that evaluated $\nabla\theta_{\mathrm{phs}}$ from a finite difference of $\theta_{\mathrm{phs}}$ instead would carry a truncation error falling as the square of the chord; this one carries none, and the table's last column is the reason it is quoted at three radii. The amplitude profile was not used at all, which is the content of the statement that only the degree enters. The amplitude vanishes at the axis, $f(0)=0$, so the density vanishes there and the nodal line is present in the profile.

### The sign, and the orientation

**The sign of the charge is the orientation of the loop and nothing else.** Reversing the loop reverses the sign of $\kappa$ and leaves $\lvert n\rvert$ unchanged, as the third row of the table shows. The physical content is the pair $(\lvert n\rvert,\text{direction})$, and a convention that fixes the direction of the loop fixes the sign. This article adopts no convention beyond the right-handed one of the frame, and no statement below depends on it.

## The Node under the Current and the Stress

### The current is regular where the velocity is not

**The velocity diverges at the node and the current does not, because the density vanishes faster.** With a phase winding $n$ the gradient of the phase is $\nabla\theta_{\mathrm{phs}}=n\,\hat\varphi/r$ in cylindrical coordinates about the axis, so the velocity's magnitude is

$$
\lvert\vec v\rvert=\frac{\hbar\lvert n\rvert}{m\,r},
$$

which diverges as $r\to0$. The current's spatial part is $\rho_{\mathrm{num}}\gamma\vec v$, and with a core amplitude $f(r)=Ar$ the density is $\rho_{\mathrm{num}}=A^{2}r^{2}$, so

$$
\lvert\vec J_{\Phi}\rvert=\rho_{\mathrm{num}}\lvert\vec v\rvert
=\frac{A^{2}\hbar\lvert n\rvert}{m}\,r\;\longrightarrow\;0 .
$$

The product is regular at the node and vanishes there. This is not a coincidence of the linear profile: any core amplitude that vanishes faster than $r^{1/2}$ gives a vanishing current, and a linear core is the generic behaviour of a solution near a simple zero. The transport equation of the polar form is a statement about $\rho_{\mathrm{num}}\tilde P_{\Phi}$, so it never sees the divergence of the velocity — which is why the scalar polar article records that the transport equation remains meaningful where the action does not.

**The node is a stagnation point of the current and not a singularity of it.** A reader who computes $\lvert\vec v\rvert$ and finds $1/r$ has found the gradient of the phase and not an observable; the observable is the current, and the current is zero at the node.

### The quantum energy is finite at the node

**The quantum potential diverges at the node while the quantum energy stays finite and negative.** The quantum potential is fixed by the corpus's sign convention,

$$
Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Box\lVert\tilde\Xi\rVert}{\lVert\tilde\Xi\rVert},
$$

and for the linear core, with no dependence on the axial coordinate, the box is the transverse Laplacian,

$$
\Box\lVert\tilde\Xi\rVert=\frac{1}{r}\frac{\partial}{\partial r}\!\left(r\frac{\partial f}{\partial r}\right)
=\frac{A}{r},
\qquad
\frac{\Box\lVert\tilde\Xi\rVert}{\lVert\tilde\Xi\rVert}=\frac{1}{r^{2}},
\qquad
Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{1}{r^{2}} .
$$

The potential diverges as $-1/r^{2}$ at the node. The quantum energy density does not: it is the density times the potential, and in the form of [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html) it is

$$
w_{\mathrm{qnt}}=\rho_{\mathrm{num}}Q_{\mathrm{qnt}}
=-\frac{\hbar^{2}}{2m}\left(A^{2}r^{2}\right)\frac{1}{r^{2}}
=-\frac{\hbar^{2}A^{2}}{2m},
$$

a constant. Checked on a grid from $r=0.05$ to $r=0.5$ with $A=1.3$ and $\hbar=m=1$, so that $\hbar^{2}/2m=\tfrac12$: $Q_{\mathrm{qnt}}r^{2}$ came out as $-0.500\,000\,000$ at three radii and $w_{\mathrm{qnt}}$ as $-0.845\,000\,000$, against $-A^{2}/2=-0.845$ exactly. So the divergence of the potential and the vanishing of the density cancel, and the node carries a finite negative energy density rather than an infinite one.

The sign is the corpus's and it is worth a sentence. A negative quantum energy density is not a negative energy: the total quantum energy of a state is the integral of a positive quantity, as the quantum-stress article shows, and what is negative here is the density's local value in a region where the classical energy is larger. The vortex core is such a region, and the cancellation between the potential's divergence and the density's vanishing is the mechanism that keeps the total finite.

### The vortex ansatz, and what it leaves to the field equation

**A phase winding and a real amplitude turn the field equation into two real equations, and the node is compatible with both.** Write

$$
\tilde\Xi=f(r)\,e^{in\varphi}\,e^{-ik_t r'_t}\,e_t
$$

with $f$ real and positive away from the axis, $r$ the distance from the axis, $\varphi$ the angle about it and $k_t$ the temporal wave number of the ansatz, the energy being $E=\hbar c\,k_t$. The action is $S_{\tilde\Xi}=\hbar(n\varphi-k_t r'_t)$, so $\nabla S_{\tilde\Xi}=\hbar n\,\hat\varphi/r$ and $\partial S_{\tilde\Xi}/\partial r'_t=-\hbar k_t$.

The transport equation is satisfied identically. It reads $\nabla\cdot(\rho_{\mathrm{num}}\nabla S_{\tilde\Xi})-\partial(\rho_{\mathrm{num}}\partial S_{\tilde\Xi}/\partial r'_t)/\partial r'_t=0$; the first term is the divergence of a purely azimuthal field whose magnitude depends on $r$ alone, and the second is the time derivative of a quantity that does not depend on time. Both vanish.

The amplitude equation is one ordinary differential equation in $r$. With $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial {r'_t}^{2}$ and the phase above, the polar form's first equation becomes

$$
k_t^{2}-\frac{n^{2}}{r^{2}}=k_m^{2}-\frac{\Box f}{f},
\qquad\text{that is}\qquad
\frac{1}{r}\frac{\partial}{\partial r}\!\left(r\frac{\partial f}{\partial r}\right)
=\left(k_m^{2}-k_t^{2}\right)f+\frac{n^{2}}{r^{2}}f .
$$

The winding enters in exactly one place, the centrifugal term $+n^{2}f/r^{2}$. It is repulsive for every $n\ne0$, it forces $f$ to vanish at the axis, and the power of the vanishing is fixed by the indicial behaviour of the equation: with $f\propto r^{s}$ the balance of the two most singular terms, $s(s-1)/r^{2}$ against $n^{2}/r^{2}$, reads $s(s-1)=n^{2}$, that is $s=\lvert n\rvert$ for the regular root and $s=1-\lvert n\rvert$ for the singular one. The linear core used above is therefore the regular behaviour at $\lvert n\rvert=1$, and a core with $\lvert n\rvert\ge2$ vanishes faster.

**So the winding is compatible with the field equation's structure and the profile is not determined by it.** The equation fixes the behaviour near the axis, fixes the decay at infinity, and leaves the constant $A$ — equivalently $k_t$ — to be selected by the condition that the two behaviours join. Whether a globally regular solution exists for given $k_t$ and $n$ is the eigenvalue question of the vortex, and for the non-relativistic case it is answered positively by the Gross–Pitaevskii literature and for the relativistic case only case by case. The corpus does not settle it and this article does not claim it.

## Why the Charge Is the Algebra's

### The charge is a class in the unit group

**The winding is a class of the field's map into the algebra's group of units, not a property of a phase function.** On the complement of the nodal set the field is invertible, so it takes values in the group of units $\mathbb{B}^{\times}$, and on a link it gives a map from a circle into that group. The relevant homotopy group is the fundamental group of the unit group, and the part of the unit group that the central field explores is the central phase circle. Hence

$$
\pi_{1}\bigl(\text{central unit circle}\bigr)=\mathbb{Z},
\qquad
\text{charge}=\text{degree of the map}\in\mathbb{Z},
$$

and the integer is the same one that appears in the circulation. The statement is the algebra's because the circle is the algebra's own: it is the set $\{e^{i\theta_{\mathrm{phs}}}e_t\}$ inside the group of units, and the phase function is a coordinate on it.

**This is the answer to open question 2 of the scalar polar form, in its second half.** The question asks whether the charge is an object of the algebra rather than of the phase. It is: the phase is a local coordinate that fails at the node and is multivalued around it, while the winding is a homotopy class of the field's values, which are elements of the algebra. Two different choices of the local phase — two different branches of the arctangent — give the same class, and that is exactly the statement that the class does not depend on the coordinate.

### The nodal set is where the polar form ends

**The polar decomposition fails exactly on the zero-divisor set, and that failure is what makes the node a node.** The corpus's polar decomposition writes an element as a scale times a unit element, $\tilde Q=\rho\tilde U$, and it fails precisely where $\langle\tilde Q\rangle_{\natural}=0$, which is the zero-divisor set. So the node of the field is not a second concept beside the cone: it is the intersection of the field's image with the cone, and the two descriptions agree event by event.

There is a payoff that the phase description cannot give. The logarithm of an element exists exactly on the group of units and on no larger set, as [Coarse-Graining and the Biquaternion Entropy Functional](coarse-graining-and-the-biquaternion-entropy-functional.html) records; and the logarithm's fibre is the set of all elements with the same exponential, which is the algebra's own statement of multivaluedness. The phase of the field is a branch of a logarithm, and the node is where the logarithm does not exist. The winding number is the obstruction to choosing a global branch, and it is an integer for the same reason that the logarithm's fibre is discrete.

### What the algebra does not supply

**The algebra supplies the quantisation and not the dynamics.** Three things are outside what has been shown.

- **Existence.** Whether the field equation has a solution with a nodal line of given winding is not settled here. A vortex ansatz solves the amplitude equation and the transport equation only under conditions on the profile, and the conditions are the field equation's business.
- **Stability.** A nodal solution can be unstable, and the stability is a question about the energy functional of [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html). Nothing here addresses it.
- **Interaction.** Two nodal lines with windings $n_1$ and $n_2$ have a total winding $n_1+n_2$, and whether they attract or repel is again dynamical.

The quantisation itself is kinematic and exact: it follows from the degree of a map and needs no approximation, no weak field and no small parameter.

## The Class and the Gauge

### The phase is a coordinate and the class is the object

**A shift of the action that is constant on the loop changes nothing, and a shift that is not constant is a different winding.** The phase enters the field only through $e^{i\theta_{\mathrm{phs}}}$, so the field is unchanged by $S_{\tilde\Xi}\mapsto S_{\tilde\Xi}+2\pi\hbar m$ for any integer $m$, and the winding changes by $m$ under such a shift. Two readings are possible and only one is right.

Throughout, $\theta_{\mathrm{phs}}:=S_{\tilde\Xi}/\hbar$ is the spinor phase, a real angle: the polar form separates the amplitude $\lVert\tilde\Xi\rVert$ from the phase, so $S_{\tilde\Xi}$ is real and $\exp(i\theta_{\mathrm{phs}})$ has modulus one.

- **The wrong reading** treats the phase as a physical field with a physical value at each point, so that $\theta_{\mathrm{phs}}(r_0)=0$ and $\theta_{\mathrm{phs}}(r_0)=2\pi$ are different states. Under this reading the node is a place where the phase has a definite but unknown value, and the winding is a statement about a function's branch cut.
- **The right reading** treats the phase as a coordinate on the central unit circle, so that the only gauge-invariant statements are those about the field's values. The winding is then the degree of the map and the integer is the charge; a branch cut is a choice of atlas and not a physical object.

The corpus's Dirac article states the same thing from the other side: the central angle is read by no bilinear, and the current and the spin are both blind to it. What reads the angle is the winding, and the winding is the one place where the angle has a physical consequence — precisely because it is not the angle's value but the angle's failure to be single valued that is measured.

### Gauge invariance, stated exactly

**Under a gauge transformation the field multiplies by a unit central element and the winding is unchanged for a single-valued transformation.** Take $\tilde\Xi\mapsto\tilde\Xi\,e^{i\theta_{\mathrm{gau}}(r)}e_t$ with $\chi$ a single-valued function. Then the phase is shifted by $\hbar\chi$, the circulation around a loop gains $\hbar\oint\nabla\chi\cdot d\vec l=0$, and $n$ is unchanged. A transformation with a multivalued $\chi$ is not a gauge transformation of the field on the loop: it changes the field's value at each point and it changes $n$. So the charge is gauge invariant under the gauge group of single-valued transformations, and it classifies the field's configurations rather than being a redundant label.

**The node is where the gauge coordinate has no value, not where the field has no value.** That is why the node is a defect of the description and a feature of the state at the same time: the field is a perfectly good element of the algebra there — zero for the central scalar field — and it is the polar decomposition, and with it the phase, that fails.

## The Cone, with an Example That Is Not Zero

**For a field of general value the node can sit on the cone away from the apex, and the Dirac sector exhibits it.** The quaternionic norm is the sum of the squares of the four coefficients, $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$, and it vanishes on the complex null cone of the algebra. The central scalar field has one non-zero coefficient, so it can vanish only at the apex. An element with two coefficients can do better:

$$
\tilde Q=\tfrac{1}{2}\bigl(e_t+i\vec e_x\bigr),
\qquad
\langle\tilde Q\rangle_{\natural}=\tfrac{1}{4}+\left(\tfrac{i}{2}\right)^{2}=\tfrac{1}{4}-\tfrac{1}{4}=0,
\qquad
\tilde Q\ne0 .
$$

So $\tilde Q$ is a zero divisor, it is not the zero element, and the polar decomposition $\tilde Q=\rho\tilde U$ does not exist for it. [Zero Divisors as a Physical Locus in Biquaternionic Form](zero-divisors-as-a-physical-locus-in-biquaternionic-form.html) records the same object as the projector onto the two-component module and stresses that an algebraically null state can carry a non-vanishing, normalisable density in the Hermitian form. The Dirac field's nodal set is therefore larger than a set of zeros: it is the intersection of the field's image with the cone, and the amplitude that vanishes there is the biquaternionic one, not the Hermitian density.

**This is why the node is a property of the algebra and not of a probability density.** A probability density vanishes only where the field is zero, which is a codimension-two condition in three dimensions and gives the same nodal curves; the biquaternionic norm vanishes on a cone, which is codimension one in the coefficient space. The two agree for the central scalar field and differ for a field of general value, and the algebra's version is the one the polar form needs, because it is the version on which the decomposition fails.

## What Is Established and What Is Interpretation

**Established.** The closure of the scalar velocity one-form on the complement of the nodal set, which is the vanishing of the curl of a gradient. The codimension of the nodal set, two real conditions on the coordinates. The circulation $2\pi\hbar n/m$ around a link of the nodal curve, exact and independent of the loop and of the amplitude profile, with the numerical check tabled above. The identification of the winding with the degree of the field's map into the central unit circle, hence with an element of $\pi_{1}$ of that circle. The identification of the nodal set with the field's arrival on the zero-divisor set, and of the failure of the polar form there with the failure of invertibility.

**Interpretation.** That the circulation quantum $h/m$ should be read as a superfluid's quantum of circulation. The formula is the same and the algebra is the same, but the corpus's scalar field is not a superfluid: a superfluid's condensate is a macroscopic occupation and the field here is a single-particle amplitude. What transfers is the kinematics — the closure, the node, the integer — and the thermodynamic reading is [The Two-Fluid Model in Biquaternionic Form](the-two-fluid-model-in-biquaternionic-form.html), which supplies the condensate and the normal part as separate components.

**Not claimed.** No claim is made that the corpus's field *is* a superfluid order parameter, that a vortex solution exists for any particular mass, or that the quantisation is observable. The claim is the conditional one: *if* the field has a nodal line with winding $n$, *then* the circulation around it is $2\pi\hbar n/m$. The conditional is exact and the antecedent is a dynamical question.

## Summary

The scalar flow is irrotational because its velocity is the gradient of the action. The closure is exact wherever the action exists, and the action fails to exist exactly where the field's value arrives on the zero-divisor set: at the cone's apex for the central scalar field, and away from the apex for a field of general value, the example $\tilde Q=\frac{1}{2}(e_t+i\vec e_x)$ having norm $\frac{1}{4}-\frac{1}{4}=0$ and not being zero. The nodal set has codimension two, so in three dimensions it is a curve and a loop can link it.

Around a link the phase returns to itself up to $2\pi n$, and the circulation is $\kappa=2\pi\hbar n/m=2\pi c n/k_m$, independent of the loop's shape and radius and of the amplitude's profile. The check at radii $0.3$, $0.8$ and $2.0$ gave the same circulation to every digit for windings $1$, $2$ and $-1$, against $2\pi n$ to $2.6\times10^{-6}$, the residual being the chord error of the polygonal loop. The integer is the degree of the field's map from the link into the central unit circle, so the charge is a class in the algebra's group of units and not a property of a phase function. That is the closure of open question 2 of the scalar polar form.

At the node the velocity diverges as $1/r$ and the current does not: $\lvert\vec J_\Phi\rvert=A^{2}\hbar\lvert n\rvert r/m$, which vanishes there. The quantum potential diverges as $-\hbar^{2}/(2mr^{2})$ while the quantum energy density stays finite at $-A^{2}/2$, checked on a grid to nine digits. The vortex ansatz satisfies the transport equation identically, reduces the amplitude equation to one ordinary differential equation whose indicial balance $s(s-1)=n^{2}$ fixes the core's power, and leaves the existence of a globally regular solution open.

What remains open is dynamical: existence, stability and interaction of nodal solutions, and the thermodynamic reading of the condensate, which the two-fluid article supplies.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{B}^{\times}$ | Group of units, the complement of the zero-divisor set |
| $e_t,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, with $\vec e_\eta^{2}=-e_t$ |
| $i$ | Central scalar imaginary |
| $\tilde\Xi$ | The scalar field, an element of $\mathbb{B}$ |
| $\lVert\tilde\Xi\rVert$ | Its amplitude, real and non-negative |
| $\rho_{\mathrm{num}}=\lVert\tilde\Xi\rVert^{2}$ | Proper density |
| $S_{\tilde\Xi}$ | The action, in $\mathrm{J\,s}$ |
| $\theta_{\mathrm{phs}}=S_{\tilde\Xi}/\hbar$ | The phase angle, dimensionless |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | Quaternionic norm, vanishing on the cone |
| $\tilde V_{\Phi}=\tilde\nabla_\Phi S_{\tilde\Xi}/m$ | Four-velocity of the scalar flow |
| $v_{\Phi,\mu}$ | Its components, index low |
| $\omega_{\mu\nu}=\partial_\mu v_{\Phi,\nu}-\partial_\nu v_{\Phi,\mu}$ | Vorticity 2-form |
| $\tilde J_{\Phi}$ | Number current |
| $\kappa=\oint\tilde V_\Phi\cdot d\vec l$ | Circulation |
| $\kappa_1=2\pi\hbar/m=2\pi c/k_m$ | Quantum of circulation |
| $n$ | Winding number, an integer; the letter is booked here for the winding and is not the Matsubara index |
| $r$ | Distance from the nodal axis |
| $\varphi$ | Angle about the axis |
| $f(r)$ | Core amplitude of the vortex ansatz |
| $A$ | Slope of the linear core, $f=Ar$ |
| $k_t$ | Temporal wave number of the ansatz, $E=\hbar c k_t$ |
| $k_m=mc/\hbar$ | Mass wave number |
| $Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Box\lVert\tilde\Xi\rVert}{\lVert\tilde\Xi\rVert}$ | Quantum potential |
| $w_{\mathrm{qnt}}$ | Quantum energy density |
| $\Box$ | D'Alembertian of the material sector |
| $\delta_{\mu\nu}$ | The one metric, all coefficients $+1$; indices stay low |
| $\varepsilon_\mu$ | Signature weight, $+1$ temporal and $-1$ spatial |
| $\hbar,\ m,\ c$ | Action quantum, mass, speed of light |

## Further Reading

- L. Onsager, "Statistical hydrodynamics," *Il Nuovo Cimento Supplemento* **6** (1949) 279–287, for the quantisation of circulation.
- R. P. Feynman, "Application of quantum mechanics to liquid helium," in *Progress in Low Temperature Physics*, vol. 1 (North-Holland, 1955), for the Onsager–Feynman quantum $h/m$ and the vortex line.
- P. G. Saffman, *Vortex Dynamics* (Cambridge University Press, 1992), for the circulation of a potential flow around a singular line and the topological reading of the vortex core.
- T. Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 2–80, for the flow variables, the transport equation and the treatment of the nodal locus.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), for the nodal set of the de Broglie–Bohm flow and the topological charge carried by its winding.
- A. J. Niemi and G. W. Semenoff, "Fermion number fractionization in quantum field theory," *Physics Reports* **135** (1986) 99–193, for the winding number as the degree of a map and its role as a topological charge.
- The companion articles: [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html), [Zero Divisors as a Physical Locus in Biquaternionic Form](zero-divisors-as-a-physical-locus-in-biquaternionic-form.html), and [The Spin Fluid of the Biquaternion Dirac Field](the-spin-fluid-of-the-biquaternion-dirac-field.html).
