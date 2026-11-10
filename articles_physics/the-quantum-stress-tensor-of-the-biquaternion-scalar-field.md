# __The Quantum Stress Tensor of the Biquaternion Scalar Field__

## Introduction

**The energy, the energy flux and the stress of the biquaternion scalar field assemble into one Hermitian element, and the quantum potential is the trace of the amplitude stress inside it.** The element is

$$
\tilde\Sigma_{\Psi}=w_{\mathrm{fl}}\,e_t+\frac{i}{c}\,\vec S_{\mathrm P},
$$

with $w_{\mathrm{fl}}$ the energy density and $\vec S_{\mathrm P}$ the energy flux. Its scalar part is the energy density. Its quaternionic norm is the difference between the square of the energy density and the square of the flux over $c$, so the norm is the dominant-energy condition. Its scalar divergence is the energy law. And when the field is written in amplitude and phase, the part of the energy density that carries the quantum potential integrates to a positive quantity, the squared logarithmic gradient of the density. That last statement is the precise content of "the quantum potential is the divergence of the quantum stress".

The derivation of the tensor is not repeated here. The canonical energy–momentum tensor of the translation current is derived in [Noether's Theorem in Biquaternionic Form](noethers-theorem-in-biquaternionic-form.html), and the field-theoretic tensor with its positive energy density, its improvement and its conservation is derived in [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html). Both are cited and neither is reproduced. What this article adds is the element, its $\natural$ reading, its polar decomposition, and the negative claim of the closing sections: the quantum stress is not a thermal pressure.

The polar variables are those of [The Polar Form of the Klein–Gordon Equation in Biquaternionic Form](the-polar-form-of-the-klein-gordon-equation-in-biquaternionic-form.html). The field is $\tilde\Xi=\lVert\tilde\Xi\rVert\exp(iS_{\tilde\Xi}/\hbar)e_t$ with $\lVert\tilde\Xi\rVert>0$ real, the four-momentum is $\tilde P_{\Phi}=\tilde\nabla S_{\tilde\Xi}$, the four-velocity is $\tilde V_{\Phi}=\tilde P_{\Phi}/m$, and the quantum potential is

$$
Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Box\lVert\tilde\Xi\rVert}{\lVert\tilde\Xi\rVert},
\qquad
\frac{E^{2}}{c^{2}}-\lvert\vec p\rvert^{2}=m^{2}c^{2}+2mQ_{\mathrm{qnt}} .
$$

The mass shell is written with $Q_{\mathrm{qnt}}$ and never without it, because the shift is the only place the amplitude enters that equation. The proper density is $\rho_{\mathrm{num}}=\lVert\tilde\Xi\rVert^{2}$, and no single letter is used for it.

Four results are established below.

- **The element exists and is Hermitian.** Four real numbers enter it — one energy density and three flux components — and they are the four that the algebra can carry. The remaining six components of the symmetric tensor are not lost; they are simply not in this object, which is why [Noether's Theorem in Biquaternionic Form](noethers-theorem-in-biquaternionic-form.html) writes the full tensor as a bigeneral bilinear and calls the element its energy–flux part.
- **The $\natural$ norm is the energy condition.** $\langle\tilde\Sigma_\Psi\rangle_{\natural}=w_{\mathrm{fl}}^{2}-\lvert\vec S_{\mathrm P}\rvert^{2}/c^{2}$, which is non-negative exactly when the flux does not exceed $c$ times the energy density. A single traveling wave saturates it and lies on the zero-divisor cone.
- **The energy law is one scalar divergence.** $\mathrm{Sc}(\tilde\nabla\tilde\Sigma_\Psi)=-i\left[\partial w_{\mathrm{fl}}/\partial r'_t+(1/c)\nabla\cdot\vec S_{\mathrm P}\right]$, and the bracket vanishes on shell.
- **The quantum part of the energy is a divergence plus a positive square.** Pointwise it is indefinite in sign; in the total of a static localised state it is positive and equals the squared logarithmic gradient of the density, up to the factor the logarithm carries.

## Why the Stress Is an Element

### The count: ten against eight

**A symmetric rank-two tensor in four dimensions has ten independent components, and an element of $\mathbb{B}$ has eight real ones.** No element can therefore be the whole stress–energy tensor, and the corpus does not pretend otherwise. The element carries the four components that the energy law needs: the energy density and the three components of the energy flux. That is the content of the remark in [Noether's Theorem in Biquaternionic Form](noethers-theorem-in-biquaternionic-form.html) that the framework's energy–momentum biquaternion is the energy–flux part of the Noether current and not the current itself.

The restriction is not a defect for the purposes of this category. Thermodynamics needs the energy density and the energy flux. It does not need the three momentum densities, because they are the flux in the other slot of a symmetric tensor, and it does not need the six stresses except through the pressure, which is the trace of the spatial block. The pressure is recovered below from the flux and the density, in the fluid's own frame.

**The element is Hermitian.** With $w_{\mathrm{fl}}$ real and $\vec S_{\mathrm P}$ a real vector, the coefficient of $e_t$ is real and the three coefficients of $\vec e_\eta$ are $iS_{\mathrm P,\eta}/c$, purely imaginary. That is the defining property of $\mathbb{B}_\Psi$, the informational sector. The stress element of a material field therefore lives in the other sector. The placement is not an accident of the convention: it follows from the single $i$ in the definition, and it is the same placement that [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html) records for the electromagnetic energy–momentum biquaternion $\tilde W_\Psi=W e_t+(i/c)\vec S$.

### The definition, and the one $i$

The definition is fixed as

$$
\boxed{\;\tilde\Sigma_{\Psi}=w_{\mathrm{fl}}\,e_t+\frac{i}{c}\,\vec S_{\mathrm P}\;}
$$

and the letter $\Psi$ marks the sector, not a second field. The factor $i$ is the algebra's central $i$ and it is not free: without it the element would not be Hermitian, and the scalar divergence below would not be a single complex number with a common factor. The factor $1/c$ converts the flux, which is an energy per area per time, into the same dimension as an energy density times the length unit the sector uses. Both factors are forced by the two requirements — Hermiticity and a real energy law — and neither is a convention to be chosen.

**The same element covers both fields.** For the electromagnetic field $w_{\mathrm{fl}}$ is $\tfrac12(\epsilon\vec E^{2}+\mu\vec H^{2})$ and $\vec S_{\mathrm P}$ is the Poynting vector $\vec E\times\vec H$. For the scalar field of this article $w_{\mathrm{fl}}$ is the time–time component of the imported tensor and $\vec S_{\mathrm P}$ is its energy flux. The element is one object and the fields differ in its value, which is why the definition is worth stating once for the category.

## The Three Readings of the Element

### The scalar part is the energy density

**The scalar extraction returns the energy density and nothing else.** For an element of the shape above, $\mathrm{Sc}(\tilde\Sigma_\Psi)=w_{\mathrm{fl}}$, because the three vector coefficients are not in the centre. This is the reading the trace gives: $\mathrm{Tr}(\tilde\Sigma_\Psi)=2w_{\mathrm{fl}}$, the factor two being the one that [Norm and Pairing Conventions](norm-and-pairing-conventions.html) fixes and that cancels in every ratio. The energy density is therefore the first coefficient in the basis, and the flux is the rest.

The reading is basis-fixed. A change of basis inside $\mathbb{B}$ mixes the four coefficients, so a reader who wants the energy density must stay in the basis in which $e_t$ is the temporal unit. That is the same requirement that the frame conventions impose on every display, and the element does not escape it.

### The $\natural$ reading is the energy condition

**The quaternionic norm of the element is the dominant-energy condition.** Multiply the element by its quaternion conjugate, $\tilde\Sigma_\Psi^{\natural}=w_{\mathrm{fl}}e_t-(i/c)\vec S_{\mathrm P}$, and use $\vec S_{\mathrm P}\vec S_{\mathrm P}=-\lvert\vec S_{\mathrm P}\rvert^{2}e_t$:

$$
\langle\tilde\Sigma_\Psi\rangle_{\natural}=\tilde\Sigma_\Psi\tilde\Sigma_\Psi^{\natural}
=w_{\mathrm{fl}}^{2}-\frac{\lvert\vec S_{\mathrm P}\rvert^{2}}{c^{2}} .
$$

The two cross terms cancel, because the temporal unit commutes with the vector part and the two products differ by a sign. The result is central and real on a Hermitian element, so it is a number at each event.

**A non-negative norm is a statement about the field.** Write $w_{\mathrm{fl}}=\lvert\vec S_{\mathrm P}\rvert/c$ as the boundary case. Below it the norm is positive; above it the norm is negative and the element is on the far side of the cone. The condition $w_{\mathrm{fl}}\ge\lvert\vec S_{\mathrm P}\rvert/c$ is the statement that no energy flows faster than $c$ relative to the energy density that carries it, which is what the dominant-energy condition says. The algebra states it as positivity of its own quadratic form, and no extra vector inequality has to be imposed by hand.

### The null case and the cone

**A single traveling wave has a stress element on the zero-divisor cone.** For a massless field of the form $f(r_x-r'_t)$ the energy density and the flux satisfy $w_{\mathrm{fl}}=\lvert\vec S_{\mathrm P}\rvert/c$ identically, so the norm vanishes at every event and the element is a zero divisor. That is not a pathology: it is the algebra's way of saying that a null field carries no rest frame. The corpus's algebraic account of the cone is in [Zero Divisors as a Physical Locus in Biquaternionic Form](zero-divisors-as-a-physical-locus-in-biquaternionic-form.html), and the stress element is one more member of that locus, this one built from a physical density rather than from a field value.

The statement is checkable in one line. Take $\xi=f(k r_x-\omega r'_t/c)$ with $\omega=ck$ so that the mode is massless. Then $\partial\xi/\partial r'_t=-k f'$ and $\nabla\xi=kf'\,\vec e_x$, so $w_{\mathrm{fl}}=\tfrac12 k^{2}f'^{2}+\tfrac12 k^{2}f'^{2}=k^{2}f'^{2}$ and $\vec S_{\mathrm P}=-c\,(\partial\xi/\partial r'_t)\nabla\xi=c k^{2}f'^{2}\vec e_x$. Hence $\lvert\vec S_{\mathrm P}\rvert=c\,w_{\mathrm{fl}}$ and $\langle\tilde\Sigma_\Psi\rangle_{\natural}=0$. For a massive mode the same computation gives $w_{\mathrm{fl}}=k^{2}f'^{2}+\tfrac12 k_m^{2}f^{2}$ against $\lvert\vec S_{\mathrm P}\rvert=c\,k\lvert f'\rvert^{2}\sqrt{k^{2}+k_m^{2}}$, and the norm is positive for every amplitude that is not identically zero. The cone is reached by the massless case and by no other.

## The Imported Tensor in Polar Variables

### The canonical tensor, quoted

The canonical tensor of the real scalar component $\xi$ is derived in [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html), with the sign that makes the energy density positive. Read in the one length unit of the material sector, where the temporal derivative is $\partial/\partial r'_t$ and no power of $c$ multiplies it, its three relevant entries are

$$
w_{\mathrm{fl}}=\tfrac12\left(\frac{\partial\xi}{\partial r'_t}\right)^{2}+\tfrac12\lvert\nabla\xi\rvert^{2}+\tfrac12 k_m^{2}\xi^{2},
\qquad
\vec S_{\mathrm P}=-c\,\frac{\partial\xi}{\partial r'_t}\,\nabla\xi,
$$

$$
T_{j\eta}=\frac{\partial\xi}{\partial r_j}\frac{\partial\xi}{\partial r_\eta}
+\delta_{j\eta}\left(\tfrac12\left(\frac{\partial\xi}{\partial r'_t}\right)^{2}-\tfrac12\lvert\nabla\xi\rvert^{2}-\tfrac12 k_m^{2}\xi^{2}\right).
$$

Three statements about this display. The energy density is a sum of three squares and is positive for every configuration. The flux carries the one $c$ of the sector, because a flux is an energy per area per time and $r'_t$ is a length. And the conservation law is

$$
\frac{\partial w_{\mathrm{fl}}}{\partial r'_t}+\frac{1}{c}\nabla\cdot\vec S_{\mathrm P}=0
\qquad\text{on shell},
$$

which is the content of the imported statement $\sum_\mu\partial T_{\mu\nu}/\partial R_\mu=0$ at $\nu=t$, read in the real coordinates. The first two entries are the ones the element keeps.

### The polar components

**The element's two entries separate into an amplitude part and a phase part.** The central field has two real components, $\xi_1=\lVert\tilde\Xi\rVert\cos\theta_{\mathrm{phs}}$ and $\xi_2=\lVert\tilde\Xi\rVert\sin\theta_{\mathrm{phs}}$ with $\theta_{\mathrm{phs}}=S_{\tilde\Xi}/\hbar$. The energy density is the sum of the two, and the cross terms cancel:

$$
w_{\mathrm{fl}}=\tfrac12\left[\left(\frac{\partial\lVert\tilde\Xi\rVert}{\partial r'_t}\right)^{2}+\lvert\nabla\lVert\tilde\Xi\rVert\rvert^{2}\right]
+\tfrac12\rho_{\mathrm{num}}\left[\left(\frac{\partial\theta_{\mathrm{phs}}}{\partial r'_t}\right)^{2}+\lvert\nabla\theta_{\mathrm{phs}}\rvert^{2}\right]
+\tfrac12k_m^{2}\rho_{\mathrm{num}} .
$$

The same substitution in the flux gives

$$
\vec S_{\mathrm P}=-\,c\left[\frac{\partial\lVert\tilde\Xi\rVert}{\partial r'_t}\nabla\lVert\tilde\Xi\rVert+\rho_{\mathrm{num}}\frac{\partial\theta_{\mathrm{phs}}}{\partial r'_t}\nabla\theta_{\mathrm{phs}}\right].
$$

The verification is one multiplication. Writing $\xi_1=\lVert\tilde\Xi\rVert\cos\theta_{\mathrm{phs}}$ and $\xi_2=\lVert\tilde\Xi\rVert\sin\theta_{\mathrm{phs}}$, the sum $\dot\xi_1^{2}+\dot\xi_2^{2}$ is $\dot{\lVert\tilde\Xi\rVert}^{2}+\rho_{\mathrm{num}}\dot\theta_{\mathrm{phs}}^{2}$, and the sum $\nabla\xi_1\cdot\nabla\xi_1+\nabla\xi_2\cdot\nabla\xi_2$ is $\lvert\nabla\lVert\tilde\Xi\rVert\rvert^{2}+\rho_{\mathrm{num}}\lvert\nabla\theta_{\mathrm{phs}}\rvert^{2}$; the flux is minus $c$ times the same two sums with one derivative of each factor.

**The phase part is the flow.** Using $\nabla\theta_{\mathrm{phs}}=\vec p/\hbar$ and $\partial\theta_{\mathrm{phs}}/\partial r'_t=-E/(\hbar c)$,

$$
\vec S_{\mathrm P}=-\,c\,\frac{\partial\lVert\tilde\Xi\rVert}{\partial r'_t}\nabla\lVert\tilde\Xi\rVert+\frac{\rho_{\mathrm{num}}E}{\hbar^{2}}\,\vec p,
$$

$$
w_{\mathrm{fl}}=\tfrac12\left[\left(\frac{\partial\lVert\tilde\Xi\rVert}{\partial r'_t}\right)^{2}+\lvert\nabla\lVert\tilde\Xi\rVert\rvert^{2}\right]
+\frac{\rho_{\mathrm{num}}}{2\hbar^{2}}\left(\frac{E^{2}}{c^{2}}+\lvert\vec p\rvert^{2}\right)+\tfrac12k_m^{2}\rho_{\mathrm{num}} .
$$

The momentum term of the flux is $\rho_{\mathrm{num}}E\vec p/\hbar^{2}$, which is the momentum density $\rho_{\mathrm{num}}\vec p/\hbar^{2}$ carried at the energy $E$: the flux of a relativistic flow is the momentum density times the energy per momentum, and $E$ is that ratio up to the units. The amplitude-gradient term is the one with no classical counterpart, and the next two sections read it.

### The mass shell inside the energy density

Substituting the mass shell $E^{2}/c^{2}=\lvert\vec p\rvert^{2}+m^{2}c^{2}+2mQ_{\mathrm{qnt}}$ into the phase part and using $k_m=mc/\hbar$ separates the energy density into three pieces:

$$
w_{\mathrm{fl}}=\tfrac12\left[\left(\frac{\partial\lVert\tilde\Xi\rVert}{\partial r'_t}\right)^{2}+\lvert\nabla\lVert\tilde\Xi\rVert\rvert^{2}\right]
+\rho_{\mathrm{num}}k_m^{2}+\frac{\rho_{\mathrm{num}}}{\hbar^{2}}\lvert\vec p\rvert^{2}
+\frac{\rho_{\mathrm{num}}\,m}{\hbar^{2}}Q_{\mathrm{qnt}} .
$$

The arithmetic is: $\rho_{\mathrm{num}}(E^{2}/c^{2}+\lvert\vec p\rvert^{2})/(2\hbar^{2})=\rho_{\mathrm{num}}\lvert\vec p\rvert^{2}/\hbar^{2}+\rho_{\mathrm{num}}m^{2}c^{2}/(2\hbar^{2})+\rho_{\mathrm{num}}mQ_{\mathrm{qnt}}/\hbar^{2}$, and the middle term plus the $\tfrac12k_m^{2}\rho_{\mathrm{num}}$ of the previous display is $\rho_{\mathrm{num}}k_m^{2}$. The factor of two on the mass term is not an error: the central field has two real components and each contributes $\tfrac12 k_m^{2}\xi_i^{2}$, so the complex field's mass term carries no half.

**The three pieces have three different behaviours.** The amplitude-gradient piece is positive and vanishes for a plane wave. The imported classical piece is what a dust of proper density $\rho_{\mathrm{num}}$ and momentum $\vec p$ would carry. The quantum piece is of indefinite sign, because $Q_{\mathrm{qnt}}$ is.

## The Divergence and the Quantum Potential

### The energy law is one scalar divergence

**The divergence of the element is the energy law, up to the factor $i$ that the temporal slot carries.** With $\tilde\nabla=e_t\partial/\partial R_t+\sum_\eta\vec e_\eta\partial/\partial R_\eta$ and $\partial/\partial R_t=-i\partial/\partial r'_t$, $\partial/\partial R_\eta=\partial/\partial r_\eta$ on the material sector,

$$
\tilde\nabla\tilde\Sigma_\Psi
=e_t\frac{\partial\tilde\Sigma_\Psi}{\partial R_t}+\sum_\eta\vec e_\eta\frac{\partial\tilde\Sigma_\Psi}{\partial r_\eta},
\qquad
\mathrm{Sc}\!\left(\tilde\nabla\tilde\Sigma_\Psi\right)
=-i\left[\frac{\partial w_{\mathrm{fl}}}{\partial r'_t}+\frac{1}{c}\nabla\cdot\vec S_{\mathrm P}\right].
$$

*Proof.* The temporal term contributes $-i\,e_t\partial_{r'_t}$ acting on $w_{\mathrm{fl}}e_t+(i/c)\vec S_{\mathrm P}$. Its scalar part is $-i\partial w_{\mathrm{fl}}/\partial r'_t$, and the term in $\vec S_{\mathrm P}$ is a vector because $e_t\vec e_\eta=\vec e_\eta$. The three spatial terms have scalar parts $-(i/c)\partial_\eta S_{\mathrm P,\eta}\,\vec e_\eta\vec e_\eta$, and $\vec e_\eta\vec e_\eta=-e_t$, so each contributes $+(i/c)\partial_\eta S_{\mathrm P,\eta}$. The sum is the bracket times $-i$.

The factor $i$ is uniform across the two terms, and that is the test of the definition: a definition that put $i$ on one term only would fail it. The corpus records the failure explicitly for the "real form" $\tilde W_\Psi=W+(1/c)\vec S$ of the electromagnetic element, whose scalar divergence on a free plane wave is $\frac{1-i}{c}\partial W/\partial r'_t$ and not zero. The $i$ on the flux is what makes the two terms one complex number.

**On shell the bracket vanishes.** That is the imported conservation law, and its verification is the substitution of the field equation. In the polar variables it is not an independent equation: the transport equation of the polar form is exactly this bracket, up to the density factor and the mass, and the polar article proves the identity. So the energy law, the continuity equation of the four-current and the imaginary part of the Klein–Gordon equation are one equation read three ways, and the stress element is the object whose divergence makes that visible.

### The amplitude stress and its trace

**The quantum potential is the trace of the amplitude's second-derivative tensor.** Define

$$
\mathcal{Q}_{\mu\nu}=-\frac{\hbar^{2}}{2m}\frac{1}{\lVert\tilde\Xi\rVert}\frac{\partial^{2}\lVert\tilde\Xi\rVert}{\partial R_\mu\partial R_\nu},
\qquad
Q_{\mathrm{qnt}}=\sum_\mu\mathcal{Q}_{\mu\mu},
$$

the sum running over the four directions because the metric is $\delta_{\mu\nu}$ and the index stays low. The tensor is the stress the amplitude itself carries: it is symmetric, it is built from the amplitude and its second derivatives, and its trace is the quantum potential. The identification is exact and needs no expansion.

**The trace is a divergence plus a square.** With $u=\ln\lVert\tilde\Xi\rVert$, so that $\partial_\mu\lVert\tilde\Xi\rVert/\lVert\tilde\Xi\rVert=\partial_\mu u$,

$$
\frac{\Box\lVert\tilde\Xi\rVert}{\lVert\tilde\Xi\rVert}=\Box u+(\partial u)^{2},
\qquad
(\partial u)^{2}=\lvert\nabla u\rvert^{2}-\left(\frac{\partial u}{\partial r'_t}\right)^{2},
$$

and since $\sum_\mu\partial_\mu(\partial_\mu u)=\Box u$,

$$
Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\left[\sum_\mu\frac{\partial}{\partial R_\mu}\left(\frac{1}{\lVert\tilde\Xi\rVert}\frac{\partial\lVert\tilde\Xi\rVert}{\partial R_\mu}\right)+(\partial u)^{2}\right].
$$

The first term is a total divergence of the amplitude's own gradient over the amplitude, which is the divergence of the amplitude stress divided by the amplitude. The second is the square of the logarithmic gradient, and it is what remains when the divergence is removed. This is the sense in which the quantum potential is a divergence: it is the divergence of the amplitude's gradient, plus the term that the divergence leaves behind. The identity is the same as the logarithmic identity of [The Polar Form of the Klein–Gordon Equation in Biquaternionic Form](the-polar-form-of-the-klein-gordon-equation-in-biquaternionic-form.html), written now with the divergence displayed rather than suppressed.

### The divergence of the quantum stress is the quantum force

**The quantum potential enters the momentum balance as the divergence of a stress, and the stress is fixed by the identity that the divergence reproduce the force.** Write the spatial block, on the pattern of the imported tensor and with every index low,

$$
\sigma_{j\eta}=\frac{\hbar^{2}}{4m}\left[\frac{\partial^{2}\rho_{\mathrm{num}}}{\partial r_j\partial r_\eta}
-\frac{1}{\rho_{\mathrm{num}}}\frac{\partial\rho_{\mathrm{num}}}{\partial r_j}\frac{\partial\rho_{\mathrm{num}}}{\partial r_\eta}\right],
$$

which is symmetric in the pair and vanishes for a uniform density. Then

$$
\sum_\eta\frac{\partial\sigma_{j\eta}}{\partial r_\eta}
=-\,\rho_{\mathrm{num}}\frac{\partial Q_{\mathrm{qnt}}}{\partial r_j},
$$

**so the force density that the quantum potential exerts is the divergence of $\sigma$, and the sign is the one the mass shell carries.** The identity is the reason the quantum potential can be called a stress at all: a force that is a divergence produces no net momentum for an isolated state, which is why the quantum stress does not move a localised packet's centre even though it acts at every point inside it.

**The two-line derivation, because the identity is used below.** With $\rho_{\mathrm{num}}=f^{2}$ and $u=\ln f$, the bracket is $f^{2}(2\partial_j\partial_\eta u+4\partial_ju\,\partial_\eta u)-f^{2}(4\partial_ju\,\partial_\eta u)=2\rho_{\mathrm{num}}\partial_j\partial_\eta u$, so

$$
\sigma_{j\eta}=\frac{\hbar^{2}}{2m}\rho_{\mathrm{num}}\frac{\partial^{2}u}{\partial r_j\partial r_\eta},
$$

and its divergence is $\tfrac{\hbar^{2}}{2m}[\rho_{\mathrm{num}}\partial_j\Box u+2\rho_{\mathrm{num}}\sum_\eta\partial_\eta u\,\partial_j\partial_\eta u]$. The right-hand side is $-\rho_{\mathrm{num}}\partial_jQ_{\mathrm{qnt}}=\tfrac{\hbar^{2}}{2m}\rho_{\mathrm{num}}\partial_j[\Box u+(\partial u)^{2}]$, and the two agree term by term after one use of $\partial_j(\partial u)^{2}=2\sum_\eta\partial_\eta u\,\partial_j\partial_\eta u$.

**The check is exact for a Gaussian, and it is the one case where every number can be written down.** With $\rho_{\mathrm{num}}=A^{2}\exp(-r^{2}/\sigma^{2})$, the bracket collapses: $\partial_j\partial_\eta\rho_{\mathrm{num}}=(r_jr_\eta/\sigma^{4}-\delta_{j\eta}/\sigma^{2})\rho_{\mathrm{num}}$ and $\partial_j\rho_{\mathrm{num}}\partial_\eta\rho_{\mathrm{num}}/\rho_{\mathrm{num}}=(r_jr_\eta/\sigma^{4})\rho_{\mathrm{num}}$, so

$$
\sigma_{j\eta}=-\,\frac{\hbar^{2}}{2m\sigma^{2}}\,\rho_{\mathrm{num}}\,\delta_{j\eta},
$$

**isotropic, and negative in its diagonal.** The sign reads as a *pressure* and not as a tension, because the article's convention puts the force at $+\partial_\eta\sigma_{j\eta}$ while a fluid's force is $-\partial_jp$: a negative diagonal is $\sigma_{j\eta}=-p\,\delta_{j\eta}$ with $p>0$, which is the outward push a spreading packet requires. At the centre that pressure is $p=\hbar^{2}\rho_{\mathrm{num}}/(2m\sigma^{2})$, and it is one third of the quantum pressure $\rho_{\mathrm{num}}Q_{\mathrm{qnt}}=3\hbar^{2}\rho_{\mathrm{num}}/(2m\sigma^{2})$ that [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html) defines. **The factor one third is the trace discrepancy recorded above, and it follows from the two normalisations**: $\sigma$ is the stress whose *divergence* is the force, so it is fixed up to the trace, and at the centre, where the squared logarithmic gradient vanishes, $\mathrm{tr}\,\sigma=-\rho_{\mathrm{num}}Q_{\mathrm{qnt}}$ distributes over three spatial directions as $-3p$. Off the centre the two differ by $(\hbar^{2}/2m)\rho_{\mathrm{num}}(\partial u)^{2}$, which is the same square. **The two objects part company away from the centre**: the diagonal never changes sign for a Gaussian, while $\rho_{\mathrm{num}}Q_{\mathrm{qnt}}$ does, which is the difference recorded above between the divergence-carrying stress and the trace. With $\hbar=m=1$, $\sigma=0.8$ and $A=1.3$, at $(r_x,r_y,r_z)=(0.31,-0.22,0.17)$ the density is $\rho_{\mathrm{num}}=1.288\,902$ and the two sides of the divergence identity are $+0.975\,488$, $-0.692\,282$ and $+0.534\,945$ for $j=x,y,z$, and they agree to all six digits printed, the calculation being exact rather than a quadrature. $\sigma_{xx}$ at that point is $-1.006\,955$, the isotropic value, and it is $\hbar^{2}\rho_{\mathrm{num}}/(2m\sigma^{2})$ with the numbers above: $1.288\,902/(2\times0.64)=1.006\,955$. **The coefficient is $1/(2m\sigma^{2})$ and not $1/(4m\sigma^{2})$**, because $\sigma$ here is the width of the *amplitude*, $\rho_{\mathrm{num}}$ is its square, and the density therefore falls on the scale $\sigma$ — the amplitude on $\sqrt2\,\sigma$. **A reader comparing this paragraph with [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html) must watch the convention**: that article writes $\rho_{\mathrm{num}}=\rho_{0}\exp(-r^{2}/(2\sigma^{2}))$, so its $\sigma$ is this one divided by $\sqrt2$, and its central quantum pressure $\tfrac{3\hbar^{2}\rho_{\mathrm{num}}}{4m\sigma^{2}}$ is the same number as the trace here. A reader who equates the two letters without the $\sqrt2$ finds a discrepancy of a factor two that is not there.

**What the identity does not say.** $\sigma$ is the divergence-carrying stress, and its trace is not $\rho_{\mathrm{num}}Q_{\mathrm{qnt}}$: the trace is $\tfrac{\hbar^{2}}{2m}\rho_{\mathrm{num}}\Box u$, while $\rho_{\mathrm{num}}Q_{\mathrm{qnt}}=-\tfrac{\hbar^{2}}{2m}\rho_{\mathrm{num}}[\Box u+(\partial u)^{2}]$, and the difference is the square of the logarithmic gradient — the same square that makes the total quantum energy positive above. **So the object whose divergence is the force and the object whose trace is the pressure are two different stresses, and the difference between them is precisely the term that has no thermal analogue.** [The Equation of State in Biquaternion Form](the-equation-of-state-in-biquaternion-form.html) states the resulting caution: $\partial_\eta p_{\mathrm{qnt}}\neq\rho_{\mathrm{num}}\partial_\eta Q_{\mathrm{qnt}}$, and a fluid equation written as if it were would be wrong.

**The quantum energy density is the density times the quantum potential, and no normalising factor belongs in between.** A density is an energy density when it is multiplied by an energy, and $Q_{\mathrm{qnt}}$ is that energy: the mass shell's $2mQ_{\mathrm{qnt}}$ carries the same dimension as $m^{2}c^{2}$. So with $\rho_{\mathrm{num}}=\lVert\tilde\Xi\rVert^{2}$,

$$
w_{\mathrm{qnt}}=\rho_{\mathrm{num}}Q_{\mathrm{qnt}}
=-\tfrac{\hbar^{2}}{2m}\rho_{\mathrm{num}}\,\Box u-\tfrac{\hbar^{2}}{2m}\rho_{\mathrm{num}}(\partial u)^{2}.
$$

The sign of the first term is not fixed, because $\Box u$ changes sign where the density's curvature changes sign. The second term carries the sign of $(\partial u)^{2}$, which is not negative definite on the material sector either. So the quantum energy density is indefinite pointwise. The next subsection shows that its total is not.

### The quantum energy is positive in the total

**For a static localised state the total quantum energy is positive and equals a squared logarithmic gradient.** Take the amplitude stationary in the material time, so that $u$ does not depend on $r'_t$, and integrate $w_{\mathrm{qnt}}$ over a volume that contains the state. The divergence term integrates to a surface term and is dropped, the surface being outside the state where the density vanishes. Two integrations by parts give $\int\rho_{\mathrm{num}}\Box u\,d^{3}r=-2\int\rho_{\mathrm{num}}\lvert\nabla u\rvert^{2}d^{3}r$, because $\nabla u=\nabla\rho_{\mathrm{num}}/(2\rho_{\mathrm{num}})$ and $\int\rho_{\mathrm{num}}\lvert\nabla u\rvert^{2}=\tfrac14\int\lvert\nabla\rho_{\mathrm{num}}\rvert^{2}/\rho_{\mathrm{num}}$. With $u$ stationary, $(\partial u)^{2}=\lvert\nabla u\rvert^{2}$, so

$$
\int w_{\mathrm{qnt}}\,d^{3}r
=-\tfrac{\hbar^{2}}{2m}\left(-2\int\rho_{\mathrm{num}}\lvert\nabla u\rvert^{2}d^{3}r\right)
-\tfrac{\hbar^{2}}{2m}\int\rho_{\mathrm{num}}\lvert\nabla u\rvert^{2}d^{3}r
=\tfrac{\hbar^{2}}{2m}\int\rho_{\mathrm{num}}\lvert\nabla u\rvert^{2}d^{3}r .
$$

In terms of the density,

$$
\boxed{\;\int w_{\mathrm{qnt}}\,d^{3}r=\tfrac{\hbar^{2}}{2m}\int\rho_{\mathrm{num}}\lvert\nabla u\rvert^{2}d^{3}r
=\frac{\hbar^{2}}{8m}\int\rho_{\mathrm{num}}\lvert\nabla\ln\rho_{\mathrm{num}}\rvert^{2}d^{3}r\;}
$$

The two forms are the same functional, because $\lvert\nabla u\rvert^{2}=\tfrac14\lvert\nabla\ln\rho_{\mathrm{num}}\rvert^{2}$ with $u=\tfrac12\ln\rho_{\mathrm{num}}$. **The factor $\hbar^{2}/2m$ is the only constant that survives in the total**, and it multiplies a pure functional of the density's shape; a corpus that set it to one would be hiding the mass of the field the total belongs to. The check reported below confirms both forms against a closed form, with $\hbar^{2}/m=1$ in the check's own units, as it states.

**The display is the statement of the section.** The quantum potential is a divergence up to a square. When the divergence is integrated away, the square remains, and the square is positive. So the quantum stress has a positive total energy although its pointwise density has neither sign. The integrand is the squared logarithmic gradient of the proper density, which is the Fisher information of the density up to a factor — the same quantity that appears in the de Broglie–Bohm reading of the quantum potential as an information term, and the same one that [Coarse-Graining and the Biquaternion Entropy Functional](coarse-graining-and-the-biquaternion-entropy-functional.html) meets in the informational sector.

## What the Quantum Stress Is Not

### It is not a function of the temperature

**A thermal pressure is a function of the state's temperature and chemical potential; the quantum stress is a function of the density's derivatives.** The two objects answer different questions and neither reduces to the other. Three tests separate them.

The first test is the temperature. Nothing in $Q_{\mathrm{qnt}}$ carries $T$, and nothing in it needs to: for a plane wave it vanishes identically at every temperature, so a thermal state that is a superposition of plane waves has a quantum stress fixed by the superposition and not by $\beta$. A thermal pressure at the same temperature is non-zero and is fixed by the equation of state.

The second test is the response to a change of volume. A pressure is the derivative of a free energy with respect to a volume, $p=-\partial F/\partial V$ at fixed $T$. The quantum stress has no such derivative, because it is not a function of a volume: it is a function of the shape of the density, and a uniform dilation of a localised state changes the density's derivatives without changing any thermodynamic variable. A dilation changes $Q_{\mathrm{qnt}}$ as the inverse square of the scale, which is not the scaling of any thermal pressure.

The third test is the sign. A pressure of a stable system at positive temperature is non-negative in the ordinary case, and the quantum stress's pointwise density is of either sign. The pointwise negativity is not a small correction: for a Gaussian amplitude it occurs outside the scale of the Gaussian, where the density's curvature reverses, and the check below exhibits it.

### It is not isotropic

**A pressure is the trace of a spatial block; the quantum stress is not.** The imported tensor's spatial block is displayed above as $T_{j\eta}$, and its trace at an event is the pressure a comoving observer would measure. The quantum part of that block is not proportional to $\delta_{j\eta}$: it is built from second derivatives of the amplitude, so it has the anisotropy of the amplitude's own curvature. A quantum stress is therefore a stress in the literal sense — a directional object — and calling it a pressure would name only its trace.

The trace is what a fluid keeps, and the quantum potential is what that trace carries. That is why the quantum potential appears in the fluid's equation of state at all, and why the equation of state of the following articles carries the quantum part as a gradient correction rather than as a thermodynamic pressure. The object is a stress; its trace enters the pressure; the two are not the same claim.

### It does not close a local equation of state

**A local equation of state relates the pressure to the density and the temperature at the same event.** The quantum part cannot be written that way, because it depends on second derivatives of the density at the event, that is, on the density in a neighbourhood. It is therefore a non-local object in the language of thermodynamics, and a local equation of state can carry it only as a gradient expansion, term by term. That is exactly what the following articles do: the pressure is $p_{\mathrm{th}}+p_{\mathrm{qnt}}$, the first a genuine thermodynamic function and the second a gradient correction whose leading term is proportional to $\Box\ln\rho_{\mathrm{num}}$.

The distinction is not pedantic. A local equation of state fixes the sound speed and the stability of the fluid. A gradient correction changes both, and it can change the sign of the stability criterion at short wavelengths. That is the standard situation of a Korteweg-type stress, and the quantum stress is of that type.

## Verification

### The divergence on a two-mode superposition

**The energy law was checked numerically on a superposition of two on-shell modes.** Take $c=2$ in the check's own units — no setting of $c$ to unity is used — $k_m=1.3$ in inverse length, and

$$
\xi=\cos(\vec k_1\cdot\vec r-k'_{1t}r'_t)+0.6\cos(\vec k_2\cdot\vec r-k'_{2t}r'_t),
\qquad
\vec k_1=(1.1,0,0),\quad \vec k_2=(0,0.9,0),
$$

with $k'_{it}=\sqrt{\lvert\vec k_i\rvert^{2}+k_m^{2}}$, so that both modes are on shell simultaneously and the superposition is a solution. **No factor of $c$ enters that dispersion, and the reason is the one the units carry**: the temporal coordinate is a length, so $k'_{it}$ is a wave number in inverse length like the spatial ones, and the rest mass enters through $k_m=mc/\hbar$, which already holds the $c$. Evaluating $\partial w_{\mathrm{fl}}/\partial r'_t$ and $\nabla\cdot\vec S_{\mathrm P}$ by centred differences at $r'_t=0.7$ and $(r_x,r_y,r_z)=(0.3,-0.5,0.2)$, the sum of the two was $-3.7\times10^{-5}$ at step $2.5\times10^{-3}$, $-1.5\times10^{-4}$ at step $5\times10^{-3}$, and $-5.9\times10^{-4}$ at step $10^{-2}$. The residual falls by a factor four at each halving, which is the signature of the second-order truncation of the difference and not of a failed identity. The energy density at the same event was $w_{\mathrm{fl}}=3.374$ and the flux had modulus $\lvert\vec S_{\mathrm P}\rvert=4.458$, so the dominant-energy inequality $w_{\mathrm{fl}}\ge\lvert\vec S_{\mathrm P}\rvert/c$ held with the margin $3.374$ against $2.229$.

The cross terms between the two modes are the content of the check. Each mode alone satisfies the energy law identically, by the computation of §*The null case and the cone*; the superposition does not, except through the cancellation of the cross terms, and the cancellation is what the residual measures. A check on a single mode would have tested nothing.

### The quantum energy of a localised state

**The total quantum energy was checked on a Gaussian amplitude in three dimensions.** Take $\rho_{\mathrm{num}}=A^{2}\exp(-r^{2}/\sigma^{2})$ with $A=1.3$ and $\sigma=0.8$, and evaluate $w_{\mathrm{qnt}}=-\tfrac12\rho_{\mathrm{num}}[\Box u+(\partial u)^{2}]$ with $u=\tfrac12\ln\rho_{\mathrm{num}}$ on a $400^{3}$ grid of extent $8\sigma$, the second derivatives by centred differences and the time derivatives zero. The result was

$$
\int w_{\mathrm{qnt}}\,d^{3}r=5.646281,
\qquad
\tfrac12\int\rho_{\mathrm{num}}\lvert\nabla u\rvert^{2}d^{3}r=5.646281,
\qquad
\frac{3}{4\sigma^{2}}\int\rho_{\mathrm{num}}\,d^{3}r=5.646284,
$$

**the three numbers being in the check's units, in which $\hbar^{2}/m=1$ and the boxed factor is $\tfrac12$.** The two algebraic forms are the ones boxed above with that factor divided out; restoring it multiplies each of the three by $\hbar^{2}/2m$, and the agreement among them is unaffected.

The first two agree to seven digits and both agree with the closed form to five, the small difference being the grid's cut-off of the Gaussian tail. The pointwise density was positive at the centre, $w_{\mathrm{qnt}}=3.959$ at $r=0$, negative in the tail, $w_{\mathrm{qnt}}=-0.0044$ at $r=8\sigma/3$, with a minimum of $-0.0242$ on the grid, and the full energy density $w_{\mathrm{fl}}$ was positive at every grid point tested. So the indefinite pointwise density and the positive total are both confirmed, and the positivity of the full energy density is not disturbed by the quantum part.

The closed form is worth deriving because it gives the scale. For a Gaussian of width $\sigma$ in three dimensions, $\lvert\nabla\ln\rho_{\mathrm{num}}\rvert^{2}=4r^{2}/\sigma^{4}$, so $\tfrac{\hbar^{2}}{8m}\int\rho_{\mathrm{num}}\lvert\nabla\ln\rho_{\mathrm{num}}\rvert^{2}=\tfrac{\hbar^{2}}{2m\sigma^{4}}\int r^{2}\rho_{\mathrm{num}}=\tfrac{3\hbar^{2}}{8m\sigma^{2}}\int\rho_{\mathrm{num}}$, using $\int r^{2}\rho_{\mathrm{num}}=3\sigma^{2}\int\rho_{\mathrm{num}}/2$ for a Gaussian. **The quantum energy is therefore of order the total density times $\hbar^{2}/(2m\sigma^{2})$**: negligible for a state broad against the Compton length, dominant for a state narrow against it.

## What Is Established and What Is Interpretation

**Established.** The canonical tensor and its conservation, imported from the two cited articles. The element $\tilde\Sigma_\Psi=w_{\mathrm{fl}}e_t+(i/c)\vec S_{\mathrm P}$ with its scalar part, its $\natural$ norm and its scalar divergence. The polar decomposition of its two entries into an amplitude part, an imported classical part and a quantum part. The identity $\langle\tilde\Sigma_\Psi\rangle_{\natural}=w_{\mathrm{fl}}^{2}-\lvert\vec S_{\mathrm P}\rvert^{2}/c^{2}$, and the vanishing of the norm for a massless traveling wave. The trace identity for the quantum potential, the divergence identity $\partial_\eta\sigma_{j\eta}=-\rho_{\mathrm{num}}\partial_jQ_{\mathrm{qnt}}$ with its exact Gaussian value, the divergence-plus-square form of the quantum energy density, and the positivity of its total for a static localised state. The two numerical checks reported above.

**Interpretation.** That the element is *the* stress object of the category, rather than the energy–flux part of a larger one. The count of components decides this and it is not interpretation: the element has eight real components and the tensor has ten, so the element is a part by arithmetic. What is interpretation is the choice to build the thermodynamics of the following articles on the part rather than on the whole. The choice is made because thermodynamics needs the energy density and the flux, and because the two of them close the energy law. A reader who wanted the full tensor would use the bigeneral bilinear of [Noether's Theorem in Biquaternionic Form](noethers-theorem-in-biquaternionic-form.html) and would find that the thermodynamics of the following articles is unchanged, since every relation below uses only the time row.

**Not claimed.** The quantum stress is not claimed to be a thermal pressure, and no equation of state is claimed to exist for it at a point. The claim is the negative one of §*What the Quantum Stress Is Not* and the positive one of §*The quantum energy is positive in the total*: an indefinite density whose integral is a positive square. Nor is the element claimed to be conserved off shell: the divergence vanishes on shell only, and the source that appears off shell is the field equation's residual.

## Summary

The stress element of the biquaternion scalar field is $\tilde\Sigma_\Psi=w_{\mathrm{fl}}e_t+(i/c)\vec S_{\mathrm P}$, Hermitian, with the energy density in its scalar part and the energy flux in its vector part. It carries four of the ten components of the symmetric tensor, which is all that thermodynamics needs; the full tensor is the bigeneral bilinear of the cited Noether article. Its quaternionic norm is $w_{\mathrm{fl}}^{2}-\lvert\vec S_{\mathrm P}\rvert^{2}/c^{2}$, so positivity of the norm is the dominant-energy condition, and a massless traveling wave saturates it and lies on the zero-divisor cone. Its scalar divergence is $-i[\partial w_{\mathrm{fl}}/\partial r'_t+(1/c)\nabla\cdot\vec S_{\mathrm P}]$, and the bracket vanishes on shell: the energy law, the continuity equation and the imaginary part of the Klein–Gordon equation are one equation.

In amplitude and phase the two entries separate into an amplitude-gradient piece, an imported classical piece and a quantum piece, the last being $\rho_{\mathrm{num}}Q_{\mathrm{qnt}}$ with $Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\Box\lVert\tilde\Xi\rVert/\lVert\tilde\Xi\rVert$. The quantum potential is the trace of the amplitude's second-derivative tensor, $\mathcal{Q}_{\mu\nu}=-(\hbar^{2}/2m)\partial_\mu\partial_\nu\lVert\tilde\Xi\rVert/\lVert\tilde\Xi\rVert$. The force it exerts is the divergence of a second stress, $\sigma_{j\eta}=(\hbar^{2}/4m)[\partial_j\partial_\eta\rho_{\mathrm{num}}-\partial_j\rho_{\mathrm{num}}\partial_\eta\rho_{\mathrm{num}}/\rho_{\mathrm{num}}]$, with $\partial_\eta\sigma_{j\eta}=-\rho_{\mathrm{num}}\partial_jQ_{\mathrm{qnt}}$; for a Gaussian $\sigma_{j\eta}=-(\hbar^{2}/2m\sigma^{2})\rho_{\mathrm{num}}\delta_{j\eta}$, isotropic and negative, and the identity then holds exactly. The trace of $\mathcal{Q}$ is a total divergence of the amplitude's gradient plus the square of the logarithmic gradient. Integrated over a static localised state the divergence drops and the square remains, so the total quantum energy is $\tfrac{\hbar^{2}}{2m}\int\rho_{\mathrm{num}}\lvert\nabla u\rvert^{2}d^{3}r=\tfrac{\hbar^{2}}{8m}\int\rho_{\mathrm{num}}\lvert\nabla\ln\rho_{\mathrm{num}}\rvert^{2}d^{3}r$; the check on a Gaussian, in units with $\hbar^{2}/m=1$, gave $5.646281$ against a closed form of $5.646284$.

The quantum stress is not a thermal pressure. It does not depend on the temperature, it is not the derivative of a free energy with respect to a volume, its pointwise density has either sign, it is anisotropic, and it depends on second derivatives of the density at the event and so cannot close a local equation of state except as a gradient expansion. Those negatives are what the following articles must respect when they write $p_{\mathrm{eff}}=p_{\mathrm{th}}+p_{\mathrm{qnt}}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, with $\vec e_\eta^{2}=-e_t$ |
| $i$ | Central scalar imaginary of $\mathbb{B}$ |
| $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\delta_{\mu\nu}$ | The one metric, all four coefficients $+1$; the index stays low |
| $\tilde\nabla$ | Biquaternionic gradient, $e_t\partial/\partial R_t+\sum_\eta\vec e_\eta\partial/\partial R_\eta$ |
| $\Box=\tilde\nabla\tilde\nabla^{\natural}$ | d'Alembertian; $\Delta-\partial^{2}/\partial{r'_{t}}^{2}$ on the material sector |
| $r'_t$ | Material time, a length |
| $\tilde\Xi=\lVert\tilde\Xi\rVert\exp(iS_{\tilde\Xi}/\hbar)e_t$ | The central scalar field in polar form |
| $\lVert\tilde\Xi\rVert$ | The amplitude, positive real |
| $\rho_{\mathrm{num}}=\lVert\tilde\Xi\rVert^{2}$ | Proper density |
| $S_{\tilde\Xi}$ | Action of the field |
| $\theta_{\mathrm{phs}}=S_{\tilde\Xi}/\hbar$ | Phase angle |
| $\tilde P_{\Phi}=i(E/c)e_t+\vec p$ | Four-momentum, the gradient of the action |
| $\tilde V_{\Phi}=\tilde P_{\Phi}/m$ | Four-velocity of the fluid |
| $E,\ \vec p$ | Energy and momentum of the flow |
| $m$ | Mass of the field quantum |
| $k_m=mc/\hbar$ | Mass wave number |
| $Q_{\mathrm{qnt}}=-\frac{\hbar^{2}}{2m}\frac{\Box\lVert\tilde\Xi\rVert}{\lVert\tilde\Xi\rVert}$ | Quantum potential, always written with the mass shell it shifts |
| $u=\ln\lVert\tilde\Xi\rVert$ | Logarithm of the amplitude |
| $(\partial u)^{2}$ | $\lvert\nabla u\rvert^{2}-(\partial u/\partial r'_t)^{2}$ |
| $\tilde\Sigma_{\Psi}=w_{\mathrm{fl}}e_t+\frac{i}{c}\vec S_{\mathrm P}$ | Stress element, Hermitian |
| $w_{\mathrm{fl}}$ | Energy density, the time–time component of the imported tensor |
| $\vec S_{\mathrm P}=-c\,\frac{\partial\xi}{\partial r'_t}\nabla\xi$ | Energy flux |
| $w_{\mathrm{qnt}}=\rho_{\mathrm{num}}Q_{\mathrm{qnt}}$ | Quantum part of the energy density |
| $\mathcal{Q}_{\mu\nu}=-\frac{\hbar^{2}}{2m}\frac{1}{\lVert\tilde\Xi\rVert}\frac{\partial^{2}\lVert\tilde\Xi\rVert}{\partial R_\mu\partial R_\nu}$ | Amplitude stress, whose trace is $Q_{\mathrm{qnt}}$ |
| $\sigma_{j\eta}=\frac{\hbar^{2}}{4m}\bigl[\partial_j\partial_\eta\rho_{\mathrm{num}}-\partial_j\rho_{\mathrm{num}}\partial_\eta\rho_{\mathrm{num}}/\rho_{\mathrm{num}}\bigr]$ | Divergence-carrying quantum stress, $\partial_\eta\sigma_{j\eta}=-\rho_{\mathrm{num}}\partial_jQ_{\mathrm{qnt}}$ |
| $p_{\mathrm{th}}$, $p_{\mathrm{qnt}}$, $p_{\mathrm{eff}}=p_{\mathrm{th}}+p_{\mathrm{qnt}}$ | The thermal and quantum parts of the pressure and their sum, named here and defined in the equation-of-state article |
| $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ | Quaternionic norm |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part |
| $\mathrm{Tr}(\tilde Q)=2\,\mathrm{Sc}(\tilde Q)$ | Trace reading |
| $\xi$ | A real scalar component of the central field |
| $\xi_1,\xi_2$ | Its components, $\lVert\tilde\Xi\rVert\cos\theta_{\mathrm{phs}}$ and $\lVert\tilde\Xi\rVert\sin\theta_{\mathrm{phs}}$ |
| $T_{j\eta}$ | Spatial block of the imported tensor |
| $\vec k_1,\vec k_2$ | Wave vectors of the two modes of the check |
| $k'_{it}=\sqrt{\lvert\vec k_i\rvert^{2}+k_m^{2}}$ | Temporal wave numbers of the two modes; no factor of $c$, since $k_m$ carries it |
| $\sigma$ | Width of the Gaussian amplitude of the check |
| $A$ | Its peak amplitude |
| $c$ | Speed of light in the medium |

## Further Reading

- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the canonical stress–energy tensor, its improvement, and the dominant-energy condition.
- A. O. Barut, *Electrodynamics and Classical Theory of Fields and Particles* (Dover, 1980), for the energy–momentum tensor of a complex scalar field and its polar reading.
- T. Takabayasi, "Relativistic hydrodynamics of the Dirac matter," *Progress of Theoretical Physics Supplement* **4** (1957) 2–80, for the stress of the polar variables and the quantum potential as a stress term.
- D. Bohm, "A suggested interpretation of the quantum theory in terms of 'hidden' variables I," *Physical Review* **85** (1952) 166–179, for the quantum potential and the information reading of its gradient.
- Peter R. Holland, *The Quantum Theory of Motion* (Cambridge University Press, 1993), for the stress tensor of the quantum fluid and the status of the quantum pressure.
- B. R. Frieden, *Physics from Fisher Information* (Cambridge University Press, 1998), for the identification of the squared logarithmic gradient of a density with a Fisher information and for what that identification does and does not license.
- The companion articles: [Noether's Theorem in Biquaternionic Form](noethers-theorem-in-biquaternionic-form.html), [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html), [The Polar Form of the Klein–Gordon Equation in Biquaternionic Form](the-polar-form-of-the-klein-gordon-equation-in-biquaternionic-form.html), and [Zero Divisors as a Physical Locus in Biquaternionic Form](zero-divisors-as-a-physical-locus-in-biquaternionic-form.html).
