# __The Variational Principle and the Klein–Gordon Equation in Biquaternionic Form__

## Introduction

*The Klein–Gordon Equation in Biquaternionic Form* writes the equation as

$$
\left(\Box_\Phi-k_m^{2}\right)\tilde\Xi=0,
\qquad
\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Delta_\Phi-\frac{\partial^{2}}{\partial r'^{2}_{t}},
\qquad
k_m=\frac{mc}{\hbar},
$$

with $\tilde\Xi=\Xi_t e_t+\Xi_x\vec e_x+\Xi_y\vec e_y+\Xi_z\vec e_z$ one element of $\mathbb{B}$ and four complex coefficients. The operator is central with real coefficients, so the one biquaternion equation is the four complex equations $\left(\Box_\Phi-k_m^{2}\right)\Xi_\mu=0$, one per coefficient. The present article asks which action has this equation as its Euler–Lagrange equation, and what the symmetries of that action give.

The answer has four parts. One action has the equation as its Euler–Lagrange equation. Its two continuous symmetries give the charge and the energy, and a third gives the stress. The action separates exactly into four scalar actions, one per coefficient, so the biquaternion form adds no coupling that the scalar form does not have. And the kinetic term of that action is the Hermitian bilinear $\mathrm{Sc}(\cdot^{*}\cdot)$, not the quaternionic bilinear $\mathrm{Sc}(\cdot^{\natural}\cdot)$; the second is complex and indefinite, and the difference is the first computation of the article.

Two boundaries are stated first, because both are ways of overclaiming.

**This is the element-form variational principle.** The field is the element $\tilde\Xi$ and the variation is over that element. The polar variational principle, in which the scale, the angle and the six frame parameters are the variables, is the companion article *The Variational Principle and the Klein–Gordon Equation in Biquaternionic Polar Variables*. The two actions are the same functional written in two coordinate systems, and the two articles differ in what can be computed in each.

**Nothing here is new in the physics.** The action is the standard action of a complex scalar field, rewritten in the algebra. It predicts nothing the parent does not predict. What it supplies is a compact statement of the equation, one derivation of three currents, one exact structural statement about the coefficients, and one statement about which bilinear makes the action real.

**The two settings, and a correction to the Schrödinger case.** For the Schrödinger equation the corpus distinguishes a constant coefficient (an ordinary differential equation in time, with a closed-form exponential for its solution) from an operator coefficient (a partial differential equation). The Klein–Gordon equation has no constant-coefficient ordinary case: every member of the family is a field equation, because the operator carries the spatial Laplacian whatever the mass term is. The distinction therefore survives only in a weaker form, between a constant mass wave number and a coefficient that varies in space and time, and §*The Two Settings* states it in that form. The closed-form exponential does not disappear; it moves to the conjugate pair, where it exists for the constant coefficient and only there.

**What survives, and at what size.** One ordinary differential equation does exist for every $\vec k_\Phi$: on a Fourier mode of fixed wave vector the conjugate pair of §*The Conjugate Pair* obeys a $2\times2$ system with constant coefficients and a closed-form block. What does not exist is an ODE for the field, because a general field is a superposition of modes with different $k'_t$ and no single exponential propagates all of them. The distinction is the one the Schrödinger article draws, moved from the field to the mode.

The formalism is that of *Lagrangian and Hamiltonian Mechanics in Biquaternionic Form*, and the action principle is that of *The Action Principle and the Non-Quantum Limit in Biquaternionic Form*; this article applies the principle to the Klein–Gordon equation in its element form.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $e_t=1$ and $\vec e_\mu^{2}=-e_t$; $i$ is the central scalar imaginary, $i^{2}=-e_t$; $\mathbb{B}_{C}=\operatorname{span}_{\mathbb{R}}\{e_t,ie_t\}$ is the centre; $\mathbb{B}_{\Psi}$ is the Hermitian fixed subspace and $\mathbb{B}_{\Phi}$ the anti-Hermitian one. The asterisk is Hermitian conjugation, the superscript $\natural$ is quaternion conjugation, $\mathrm{Sc}$ is the coefficient of $e_t$, and $\mathrm{Tr}=2\,\mathrm{Sc}$. The measure is $\mathrm{d}^{4}x=\mathrm{d}r'_t\,\mathrm{d}r_x\,\mathrm{d}r_y\,\mathrm{d}r_z$ with $r'_t=c\,t'$, so the material time is a length and no $c$ appears beside a temporal derivative. The four-position is $\tilde R_\Phi=i r'_t e_t+r_x\vec e_x+r_y\vec e_y+r_z\vec e_z$. Each symbol is defined where it first appears, and all of them are collected in §*Summary of Notation*.

## The Equation and Its Operator

Two conventions of the parent are fixed here once, because every sign below follows from them.

**The d'Alembertian.** The gradient is $\tilde\nabla_\Phi=e_t\,\partial/\partial R_t+\sum_\eta\vec e_\eta\,\partial/\partial r_\eta$ with $R_t=i r'_t$, and $\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Delta_\Phi-\partial^{2}/\partial r'^{2}_{t}$ on the material sector. On a plane wave $\exp\big(-i(\omega r'_t/c-\vec k_\Phi\cdot\vec r)\big)$ the operator returns $\omega^{2}-c^{2}k_\Phi^{2}$ times the wave, so the equation requires $\omega^{2}=c^{2}k_\Phi^{2}+c^{2}k_m^{2}$. That is the parent's dispersion relation, and it fixes the sign of the mass term in the action below.

**The two pairings.** The bilinear $\mathrm{Sc}(A^{*}B)$ is the Hermitian form and the bilinear $\mathrm{Sc}(A^{\natural}B)$ is the quaternionic one. They agree on real coefficients and differ on complex ones, and the difference is not cosmetic. For $A=\sum_\mu a_\mu e_\mu$ with $a_\mu$ complex,

$$
\mathrm{Sc}(A^{*}A)=\sum_{\mu}\lvert a_\mu\rvert^{2},
\qquad
\mathrm{Sc}(A^{\natural}A)=\sum_{\mu}a_\mu^{2},
$$

the first real and equal to the Hermitian norm, the second complex in general. The two expressions are checked by the one computation $\vec e_\mu^{*}\vec e_\mu=-\vec e_\mu^{2}=e_t$ for a spatial unit and $\vec e_\mu^{\natural}\vec e_\mu=+\vec e_t$, the two signs of the two conjugations. The first sum is a sum of squares of moduli; the second is a sum of squares of complex numbers, whose real part is $\sum_\mu(u_\mu^{2}-v_\mu^{2})$ for $a_\mu=u_\mu+i v_\mu$ and is negative whenever the imaginary parts dominate.

## The Action in Element Form

The action is

$$
S[\tilde\Xi,\tilde\Xi^{*}]=\int\mathrm{d}^{4}x\;\mathrm{Sc}\Big[(\partial_{r'_t}\tilde\Xi)^{*}\partial_{r'_t}\tilde\Xi-\sum_{\eta}(\partial_{r_\eta}\tilde\Xi)^{*}\partial_{r_\eta}\tilde\Xi-k_m^{2}\tilde\Xi^{*}\tilde\Xi\Big].
$$

The signature is written out in the display, and that is deliberate. A compact form $\mathrm{Sc}\big[(\partial_\mu\tilde\Xi)^{*}(\partial^{\mu}\tilde\Xi)-k_m^{2}\tilde\Xi^{*}\tilde\Xi\big]$ is available, but only if the index $\mu$ runs over the complex coordinates $R_\mu$ with $\partial_{R_t}=-i\partial_{r'_t}$ and the temporal slot raised by that factor. The reason is the one already met: the Hermitian conjugation carries the central $i$ with it, so $(\partial_{R_t}\tilde\Xi)^{*}\partial_{R_t}\tilde\Xi=(+i)(-i)(\partial_{r'_t}\tilde\Xi)^{*}\partial_{r'_t}\tilde\Xi$ is the temporal term with a plus, and the four-slot contraction over $R$ gives $+\lvert\partial_{r'_t}\tilde\Xi\rvert^{2}+\sum_\eta\lvert\partial_{r_\eta}\tilde\Xi\rvert^{2}$ with no relative sign. The relative sign of the two terms is therefore a property of the metric, not of the conjugation, and it is stated in the display rather than hidden in a symbol. Three properties of the action are now checked.

### The kinetic term is real

Every term of the display has the form $\mathrm{Sc}(A^{*}A)$ with $A$ one of the derivatives, and $\mathrm{Sc}(A^{*}A)=\sum_\mu\lvert a_\mu\rvert^{2}$ is real and non-negative. The kinetic part of the Lagrangian is the difference of two such sums, real term by term. Its temporal part is positive and its spatial part enters with a minus, which is the metric and not an ambiguity: a boost of the four-gradient reverses one sign and not the other.

### The potential term is real

Write the coefficient as $\tilde M\in\mathbb{B}_{\Psi}$, Hermitian, with $\tilde M=k_m^{2}e_t$ for the free field. Then

$$
(\tilde\Xi^{*}\tilde M\tilde\Xi)^{*}=\tilde\Xi^{*}\tilde M^{*}\tilde\Xi=\tilde\Xi^{*}\tilde M\tilde\Xi,
$$

using $(\tilde\Xi^{*})^{*}=\tilde\Xi$ and $\tilde M^{*}=\tilde M$. So the density is Hermitian, and a Hermitian element has a real scalar part, because $\mathbb{B}_{\Psi}$ is the real-linear span of $e_t$ and $i\vec e_\eta$. The potential density is therefore real for every Hermitian coefficient, central or not. With $\tilde M=k_m^{2}e_t$ it is $k_m^{2}\sum_\mu\lvert\Xi_\mu\rvert^{2}$, and the action is real.

### The pairing: why Hermitian and not quaternionic

The action above uses $\mathrm{Sc}(\cdot^{*}\cdot)$. The alternative is $\mathrm{Sc}(\cdot^{\natural}\cdot)$, and it fails in two ways that are worth separating.

**It is not real.** For $\partial_{r'_t}\tilde\Xi=(1+i)e_t$ at one event, $\mathrm{Sc}(A^{\natural}A)=(1+i)^{2}=2i$, whose real part is zero while the field's rate of change is not. A Lagrangian that vanishes on a nonzero rate of change is not a Lagrangian for that rate of change.

**Its real part is not positive.** For $A=(1+i)e_t$ and $A'=(1-i)e_t$ the two values $2i$ and $-2i$ differ only in sign, so no choice of overall sign makes $\mathrm{Re}\,\mathrm{Sc}(A^{\natural}A)$ a sum of squares. The kinetic energy of the resulting theory would be indefinite already for one coefficient, before any interaction is added and before the spatial part is counted.

**Why the quaternionic reading looks right.** For a field with real quaternionic coefficients the two readings coincide, $a_\mu^{2}=\lvert a_\mu\rvert^{2}$, and $\mathrm{Sc}(A^{\natural}A)$ is then a genuine sum of squares. The Klein–Gordon field of this corpus has complex coefficients: it is $\mathbb{C}^{4}$-valued, and the parent's scalar case is the one complex coefficient $\Xi_t$. With four complex coefficients the equality $a^{2}=\lvert a\rvert^{2}$ fails for every coefficient whose phase is not $0$ or $\pi$, which is almost every field. The Hermitian pairing is the one that survives, and it is also the pairing the parent uses for the density, $\rho_{\mathrm{num}}=\mathrm{Sc}(\tilde\Xi\tilde\Xi^{*})=\sum_\mu\lvert\Xi_\mu\rvert^{2}$.

### The variation

Vary $\tilde\Xi$ and treat $\tilde\Xi^{*}$ as independent, which is legitimate over $\mathbb{C}$ and is the standard device for a first-order-in-the-conjugate action. The two kinetic terms are complex conjugates, $\mathrm{Sc}(A^{*}B)=\big(\mathrm{Sc}(B^{*}A)\big)^{*}$, so they sum to twice the real part, and after one integration by parts

$$
S[\tilde\Xi+\delta\tilde\Xi]-S[\tilde\Xi]
=2\,\mathrm{Re}\int\mathrm{d}^{4}x\;\mathrm{Sc}\big[\delta\tilde\Xi^{*}\left(\Box_\Phi-k_m^{2}\right)\tilde\Xi\big].
$$

The bracket must vanish for every variation, and $\mathrm{Sc}$ is non-degenerate on $\mathbb{B}$, so

$$
\boxed{\;\left(\Box_\Phi-k_m^{2}\right)\tilde\Xi=0\;}
$$

as an element of $\mathbb{B}$, which is eight real equations. The step is exact for every variation: the two kinetic halves are conjugates, so their sum is twice a real part, and the integration by parts moves the derivatives onto the bracket without a boundary term for a variation of compact support.

**The three signs, from one plane wave.** Write the action with coefficients $(a,b,c)$ in front of the temporal kinetic, the spatial kinetic and the mass term. Its Euler–Lagrange equation is $-a\,\partial^{2}_{r'^{2}_t}\tilde\Xi-b\,\Delta_\Phi\tilde\Xi-c\,k_m^{2}\tilde\Xi=0$. On a mode $\tilde\Xi_0\exp(i(\vec k_\Phi\cdot\vec r-k'_t r'_t))$ the bracket becomes $\big(a k'^{2}_t+b k_\Phi^{2}-c k_m^{2}\big)\tilde\Xi$, so the mode condition is

$$
a\,k'^{2}_t+b\,k_\Phi^{2}=c\,k_m^{2}.
$$

The convention fixed in §*The Equation and Its Operator* is $\Box_\Phi=\Delta_\Phi-\partial^{2}_{r'^{2}_t}$, so the equation must read $k'^{2}_t-k_\Phi^{2}=+k_m^{2}$, and the coefficients are $(a,b,c)=(1,-1,1)$: the temporal term with a plus, the spatial term with a minus, the mass term with a minus. Each choice fails on its own: $c=-1$ gives $k'^{2}_t-k_\Phi^{2}=-k_m^{2}$, the wrong branch of the hyperbola, spacelike where the physical branch is timelike; $b=+1$ gives $k'^{2}_t+k_\Phi^{2}=k_m^{2}$, which forces $k'^{2}_t<k_m^{2}$ and makes the spatial gradient a negative contribution to the energy; and $a=-1$ gives $-k'^{2}_t-k_\Phi^{2}=k_m^{2}$, which has no real solution at all. The minus on the mass term is also what makes the potential energy positive, and that is the same statement as the branch being the physical one.

**No factor of one half.** The overall normalization is a convention and this article fixes it once: the action above has no $\tfrac12$, so the charge and the energy below carry the constants written and no others. A factor of $\tfrac12$ in front of $S$ multiplies every Noether current by $\tfrac12$ and changes no equation.

## The Four Scalar Actions

The action is not merely real: it separates into four copies of one scalar action, and that is the structural fact of the element form.

**The separation.** By $\mathrm{Sc}(A^{*}A)=\sum_\mu\lvert a_\mu\rvert^{2}$ applied to $A=\partial\tilde\Xi$, and by the same identity applied to $\tilde\Xi$ itself, every term of the Lagrangian is a sum over the four coefficients,

$$
\mathrm{Sc}\big[(\partial\tilde\Xi)^{*}\partial\tilde\Xi\big]=\sum_{\mu}\partial\Xi_\mu^{*}\,\partial\Xi_\mu,
\qquad
\mathrm{Sc}(\tilde\Xi^{*}\tilde\Xi)=\sum_{\mu}\lvert\Xi_\mu\rvert^{2},
$$

with the metric signs of the display above understood in each summand. Hence

$$
S[\tilde\Xi]=\sum_{\mu}S[\Xi_\mu],
$$

where $S$ on the right is the scalar action of one complex coefficient. There are no cross terms, because the four units are orthogonal for the Hermitian pairing and every off-diagonal product $\vec e_\mu^{*}\vec e_\nu$ with $\mu\neq\nu$ is a spatial unit and has no scalar part.

**What follows for the equation.** The four coefficients are independent, the solution space is $\mathbb{C}^{4}\otimes_{\mathbb{C}}S$ with $S$ the set of complex scalar solutions, and the parent's §*General Fields* is the same statement read on the equation. The variational form adds the reason: the independence is the orthogonality of the four units under the pairing, so no choice of coefficients can produce a coupling that the Lagrangian does not contain.

**What breaks it.** A non-central Hermitian coefficient $\tilde M$ in the potential term does couple the coefficients. Left multiplication by $\tilde M$ is a real-linear map of $\mathbb{B}$, Hermitian for the $\mathrm{Sc}$ pairing when $\tilde M$ is Hermitian, so the potential term is still real, but it is now a Hermitian $4\times4$ matrix in the basis $e_\mu$ rather than four numbers. The equation keeps its form, $\left(\Box_\Phi-\tilde M\right)\tilde\Xi=0$, and the four copies become four coupled channels. For a constant $\tilde M$ the plane-wave problem becomes the eigenvalue problem $(\omega^{2}-c^{2}k_\Phi^{2})\tilde\Xi_0=\tilde M\tilde\Xi_0$, whose four branches are the four eigenvalues. The free field is the case in which $\tilde M$ is central and the branches coincide.

## The Conjugate Pair

The equation is second order in the material time, so the action is second order in the velocity and the canonical momentum is not the field but its conjugate. This section states the Legendre transform, because it is the closest analogue in this problem of the parent Schrödinger article's two writings, and because it is where the closed-form exponential survives.

**The momentum and the Hamiltonian.** With $\Pi_\Xi=(\partial_{r'_t}\tilde\Xi)^{*}$ the conjugate in the sense $\delta L=2\,\mathrm{Re}\,\mathrm{Sc}(\Pi_\Xi\,\delta\tilde\Xi)$, the Hamiltonian is

$$
H=\int\mathrm{d}^{3}x\;\mathrm{Sc}\Big[\Pi_\Xi^{*}\Pi_\Xi+\sum_{\eta}(\partial_{r_\eta}\tilde\Xi)^{*}\partial_{r_\eta}\tilde\Xi+k_m^{2}\tilde\Xi^{*}\tilde\Xi\Big],
$$

which is a sum of three non-negative terms and is non-negative for every field. The first-order action is

$$
S[\tilde\Xi,\Pi_\Xi]=\int\mathrm{d}^{4}x\;\mathrm{Sc}\big[\Pi_\Xi^{*}\partial_{r'_t}\tilde\Xi+(\partial_{r'_t}\tilde\Xi)^{*}\Pi_\Xi\big]-H .
$$

**Its equations.** Varying $\Pi_\Xi^{*}$ gives $\partial_{r'_t}\tilde\Xi=\Pi_\Xi$ and varying $\tilde\Xi^{*}$ gives $\partial_{r'_t}\Pi_\Xi=\sum_\eta\partial^{2}_{r_\eta}\tilde\Xi-k_m^{2}\tilde\Xi$, and the two together return the Klein–Gordon equation on elimination. The elimination is exact: differentiating the first equation in $r'_t$ and substituting the second gives $\partial^{2}_{r'^{2}_t}\tilde\Xi=\Delta_\Phi\tilde\Xi-k_m^{2}\tilde\Xi$, which is $\left(\Box_\Phi-k_m^{2}\right)\tilde\Xi=0$.

**Why there is no second writing of the element.** The parent's Schrödinger article has two writings of one equation, with $\tilde H_\Psi$ and with $\tilde H_\Phi=-i\tilde H_\Psi$, and both are linear in the field. The Klein–Gordon operator admits no such pair, and the parent says why in §*The Lanczos Family and the Spin-0 Member*: a first-order operator $\tilde\nabla_\Phi+\tilde F$ squares to $\Box_\Phi+(\tilde F,\tilde F)+2i(\tilde F,\nabla)$, and the cross term cannot be removed while the mass is kept. The first-order readings that do exist are two and neither is a rewriting of one element: the conjugate pair above, which doubles the state, and the spinor square root of the Dirac article, which doubles the carrier. The two doublings are different in kind. The pair keeps one element per coefficient and adds its rate, so the carrier is unchanged and the state space doubles. The root keeps one datum per coefficient and enlarges the carrier to a minimal left ideal and its conjugate, so the number of data per coefficient is unchanged. A second writing of the same element would be neither. The variational principle displays the first of them, since $\Pi_\Xi$ is a second element and the pair $(\tilde\Xi,\Pi_\Xi)$ is the pair the equation needs.

**The closed form.** For a constant $k_m$ and a constant coefficient the pair propagates in closed form. On a plane-wave component of wave vector $\vec k_\Phi$ the pair obeys $\partial_{r'_t}\tilde\Xi=\Pi_\Xi$ and $\partial_{r'_t}\Pi_\Xi=-(\kappa^{2}+k_m^{2})\tilde\Xi$ with $\kappa^{2}=k_\Phi^{2}$, so with $k'_t=\sqrt{\kappa^{2}+k_m^{2}}$,

$$
\begin{pmatrix}\tilde\Xi(r'_t)\\ \Pi_\Xi(r'_t)\end{pmatrix}
=
\begin{pmatrix}\cos(k'_t r'_t) & \sin(k'_t r'_t)/k'_t\\ -k'_t\sin(k'_t r'_t) & \cos(k'_t r'_t)\end{pmatrix}
\begin{pmatrix}\tilde\Xi(0)\\ \Pi_\Xi(0)\end{pmatrix},
$$

which is the parent's two frequency branches $e^{\pm i k'_t r'_t}$ recombined into a real block. The single element alone has no such closed form, and that is the precise sense in which the second-order equation needs the doubling.

## The Noether Currents

Three symmetries are treated, and for each the transformation, the current and the check of conservation are stated.

### The phase symmetry: the charge

The transformation is $\tilde\Xi\mapsto e^{i\alpha}\tilde\Xi$, $\tilde\Xi^{*}\mapsto e^{-i\alpha}\tilde\Xi^{*}$ with $\alpha$ a constant real number. The central $i$ commutes with the whole algebra, so the Lagrangian is invariant identically and not merely up to a divergence. The Noether current is

$$
j_{r'_t}=2\,\mathrm{Re}\,\mathrm{Sc}\big[i(\partial_{r'_t}\tilde\Xi)^{*}\tilde\Xi\big],
\qquad
j_\eta=-2\,\mathrm{Re}\,\mathrm{Sc}\big[i(\partial_{r_\eta}\tilde\Xi)^{*}\tilde\Xi\big],
$$

and its divergence is the equation itself,

$$
\partial_{r'_t}j_{r'_t}+\sum_{\eta}\partial_{r_\eta}j_\eta=-2\,\mathrm{Im}\,\mathrm{Sc}\big[\tilde\Xi^{*}\left(\Box_\Phi-k_m^{2}\right)\tilde\Xi\big],
$$

which vanishes on every solution. The identity is exact off shell: its right side is the equation contracted with $\tilde\Xi^{*}$ and projected on the scalar part, so it is zero exactly when the bracket is.

**Where the factor comes from.** On the positive-frequency mode $\Xi_t=A\exp(-ik'_t r'_t)$ the derivative is $\partial_{r'_t}\Xi_t=-ik'_t\Xi_t$ with $k'_t=\omega/c$, so $i(\partial_{r'_t}\Xi_t)^{*}\Xi_t=-k'_t\lvert A\rvert^{2}$ and the temporal component is $j_{r'_t}=-2k'_t\lvert A\rvert^{2}$. The parent's density on the same mode is

$$
\rho_{\mathrm{chg}}=\frac{i}{2k_m}\big(\Xi_t^{*}\partial_{r'_t}\Xi_t-\Xi_t\partial_{r'_t}\Xi_t^{*}\big)
=\frac{i}{2k_m}\left(-2ik'_t\right)\lvert A\rvert^{2}=\frac{k'_t}{k_m}\lvert A\rvert^{2},
$$

so the ratio is exactly $-2k_m$ and the two normalisations account for it: the current here is twice the real part of one product, and the parent's density carries the factor $i/(2k_m)$.

**The relation to the parent's current.** For a central field $\tilde\Xi=\Xi_t e_t$ the statement is uniform,

$$
j_{r'_t}=-2k_m\,\rho_{\mathrm{chg}} ,
$$

with the factor computed above and not fitted. The constant is a normalization convention. The sign is not: it is the sign of the action, and it is the same for every field.

**The defect is visible here.** The density of the action's Noether charge changes sign with the branch, exactly as the parent's does, and for the same reason. On $\tilde\Xi=A e^{-i\omega r'_t/c}$ with $\omega>0$ it is $-2(\omega/c)\lvert A\rvert^{2}$ and on the other branch it is $+2(\omega/c)\lvert A\rvert^{2}$. So the variational principle does not repair the negative-probability problem; it locates the problem in the symmetry current, where it is one line of computation. What the action adds is the converse: a symmetry whose charge is indefinite is a symmetry whose generator is not a number operator, and that is the algebraic content of the parent's §*The Conserved Current and the Two Defects*.

### Time translation: the energy

The transformation is $r'_t\mapsto r'_t+\epsilon$ with the coefficient constant in $r'_t$. The Noether current is the energy flux and the charge is

$$
E_{\mathrm{nrg}}=\int\mathrm{d}^{3}x\;\mathrm{Sc}\Big[(\partial_{r'_t}\tilde\Xi)^{*}\partial_{r'_t}\tilde\Xi+\sum_{\eta}(\partial_{r_\eta}\tilde\Xi)^{*}\partial_{r_\eta}\tilde\Xi+k_m^{2}\tilde\Xi^{*}\tilde\Xi\Big],
$$

which is the Hamiltonian of the previous section and is non-negative term by term.

**The contrast with the charge.** The energy is positive on both branches and the charge is not, and the difference is not a matter of normalization. The energy density is a sum of four moduli squared per coefficient; the charge density is a difference of two products of the field and its rate. A plane wave checks both: with $\tilde\Xi=A e^{-i\omega r'_t/c}$ at $\vec k_\Phi=0$ the energy density is $\big(\omega^{2}/c^{2}+k_m^{2}\big)\lvert A\rvert^{2}$, the same for $+\omega$ and $-\omega$, while the charge density flips sign. So the two defects of the parent are one defect: what fails is the charge, and the energy is what shows that the failure is not a failure of positivity of the theory.

**The factor of two, and the trace.** With the convention $\mathrm{Tr}=2\,\mathrm{Sc}$ the energy density is $\tfrac12\mathrm{Tr}\big[(\partial_{r'_t}\tilde\Xi)^{*}\partial_{r'_t}\tilde\Xi+\dots\big]$, which is the form the stress tensor article uses. The two expressions differ by the convention and by nothing else.

### Space translations and rotations: the stress

The remaining symmetries are the three translations $r_\eta\mapsto r_\eta+\epsilon_\eta$ and the three rotations of the spatial axes. Their Noether currents are the components of one tensor,

$$
T_{\mu\nu}=\mathrm{Sc}\big[(\partial_\mu\tilde\Xi)^{*}\partial_\nu\tilde\Xi+(\partial_\nu\tilde\Xi)^{*}\partial_\mu\tilde\Xi\big]-\eta_{\mu\nu}\mathcal{L},
$$

with $\eta$ the metric of the display in §*The Action in Element Form*, $\mathcal{L}$ the Lagrangian density, and the index pair read with that metric.

**Where the tensor comes from.** The Lagrangian depends on $\tilde\Xi$ and its first derivatives and on no coordinate, so it is invariant under $r_\mu\mapsto r_\mu+\epsilon_\mu$ with constant $\epsilon_\mu$, and the Noether current of that translation is

$$
T^{\mu}{}_{\nu}=\mathrm{Sc}\big[(\partial^{\mu}\tilde\Xi)^{*}\partial_\nu\tilde\Xi+(\partial_\nu\tilde\Xi)^{*}\partial^{\mu}\tilde\Xi\big]-\delta^{\mu}{}_{\nu}\mathcal{L},
$$

which is the display above with one index lowered. The two halves appear symmetrically because the Lagrangian is a real bilinear of the pair $(\tilde\Xi,\tilde\Xi^{*})$ and each half contributes one product. Its divergence is

$$
\partial_\mu T^{\mu}{}_{\nu}=-2\,\mathrm{Re}\,\mathrm{Sc}\big[(\partial_\nu\tilde\Xi)^{*}\left(\Box_\Phi-k_m^{2}\right)\tilde\Xi\big],
$$

which vanishes on solutions, so conservation of the stress is the equation and nothing else, exactly as for the charge. The improvement term and the trace belong to *The Quantum Stress Tensor of the Biquaternion Scalar Field*; the variational statement is that no separate construction is needed, since the tensor is the current of the four translations of the action.

**What is not here.** There is no spin current. The Klein–Gordon field of this article carries no spin index, the action has no spin term, and a spin current built from it would be a current of a symmetry the action does not have. The spin current of the Dirac field belongs to the Dirac article.

## The Two Settings

The parent distinguishes two objects and this article inherits the distinction in the form the second-order equation allows.

**The constant coefficient.** With $k_m$ a number and no other coefficient, the equation is translation invariant, the plane waves of the parent are the complete set of modes, and the pair propagator of §*The Conjugate Pair* is closed form. Every result of this article about a solution is a result of this case.

**The varying coefficient.** With $\tilde M=\tilde M(x)$ Hermitian and not constant, the equation keeps its form and loses its modes. There is no closed-form propagator, the Green's functions are those of *The Klein–Gordon Propagator and Its Green's Functions in Biquaternionic Form*, and the variational principle is unchanged: the same functional, with $\tilde M$ in place of $k_m^{2}e_t$, has the same Euler–Lagrange equation and the same Noether construction, and the currents are conserved with the same identity. What is lost is not the variational principle but the solubility.

**What does not transfer.** Two statements of the Schrödinger pair have no counterpart here and are not imported. There is no setting in which the equation is an ordinary differential equation, because the Laplacian is in the operator in every case. And there is no exponential $\exp(-\tfrac{i}{\hbar}\tilde H t')$ whose powers solve the equation, because the second-order equation needs two data per mode; the block of §*The Conjugate Pair* is what replaces it, and it exists for the constant coefficient only.

## What the Variational Principle Adds and What It Relabels

The ledger is short and it is the reason the article is worth writing.

**Adds.** One action whose Euler–Lagrange equation is the parent's equation, in eight real components at once. One derivation of three currents: the charge, the energy and the stress, the first two with their conservation proved by one identity. One exact structural statement: the action is the sum of four scalar actions, and the coupling of the coefficients is exactly the non-centrality of the potential coefficient and nothing else. One statement about the bilinear: the Hermitian pairing is the one that makes the action real and bounded, and the quaternionic pairing fails on both counts for complex coefficients.

**Relabels.** No new prediction, no new solution, no new physical principle. The action is the standard one for a complex scalar field, and the four-copy structure is the parent's independence of the coefficients read on the Lagrangian instead of on the equation.

**The distinction that matters.** The variational principle is integral in form and local in content. Its Euler–Lagrange equations are the local equation, so it is equivalent to the parent and not opposed to it. It is richer in what it delivers, and the deliverable that matters here is the pair of currents with their opposite signs.

## Open Questions

1. **The current of a general field.** The phase current above is a bilinear of the element, and it is additive over the four coefficients by the identity of §*The Four Scalar Actions*. The parent's §*General Fields* records a second reading, which puts the current in the vector slots of $\mathbb{B}_{\Phi}$ and finds no diagonal term there. The two readings cannot both be the conserved current of a sector-valued element, and this article's variational derivation does not decide between them: it produces the additive one because the action is additive. The choice is recorded as open in the polar companion and in the parent.

2. **The stress tensor and its improvement.** The tensor of §*Space Translations and Rotations* is the canonical one. Whether it agrees with the tensor of *The Quantum Stress Tensor of the Biquaternion Scalar Field*, and whether the massless case needs the improvement term that makes the trace vanish, is a comparison this article does not make. The conformal article's improved trace is the object to compare against.

3. **The carrier under a non-central coefficient.** The free equation preserves the carrier: it maps $\mathbb{B}$ to $\mathbb{B}$ and each minimal left ideal to itself, since the operator is central. A non-central Hermitian $\tilde M$ acts by left multiplication and does not commute with a right ideal, so a field started in a Peirce carrier leaves it. Whether the physical restriction to a carrier survives an external potential, and in which representation, is the Klein–Gordon form of the closure question the Schrödinger article raises.

## What Was Checked

**The variation.** The difference quotient of the action was compared with $2\,\mathrm{Re}\int\mathrm{Sc}[\delta\tilde\Xi^{*}(\Box_\Phi-k_m^{2})\tilde\Xi]$ on a periodic grid with a random biquaternion field and a random complex variation, and the two agreed to ten significant figures. The step is also exact on paper: the kinetic halves are conjugates and the boundary term of the integration by parts vanishes for a variation of compact support.

**The reality of the action.** The imaginary part of $S$ vanished identically on every field tried, which is the numerical form of the statement that both terms are Hermitian and that $\mathrm{Sc}$ of a Hermitian element is real.

**The current.** The identity $\partial_\mu j^{\mu}=-2\,\mathrm{Im}\,\mathrm{Sc}[\tilde\Xi^{*}(\Box_\Phi-k_m^{2})\tilde\Xi]$ was checked off shell on a grid with four modes, where the two sides agreed to $10^{-13}$ at every point, and on an exact solution, where the divergence was zero to machine precision. The ratio $j_{r'_t}/\rho_{\mathrm{chg}}=-2k_m$ was checked on the mode $\omega=2$, $k_x=1$, $k_m=\sqrt3$ in one length unit, where it came out $-2\sqrt3$ and the derivation of §*The Noether Currents* explains why.

**The stress.** On the exact plane wave the combination $\partial_{r'_t}T^{00}+\sum_\eta\partial_{r_\eta}T^{0\eta}$ vanished at the level of the finite-difference truncation, which is the numerical form of the divergence identity above.

**The signs.** A cosine of each sign of $\omega$ was substituted into $\Box_\Phi\tilde\Xi-k_m^{2}\tilde\Xi$ on the case $\omega=2$, $k_x=1$, $k_m=\sqrt3$, and both branches solved the equation, which is the check that the coefficient $(1,-1,1)$ of §*The Action in Element Form* is right and the wrong choices of sign are wrong.

## Summary

One action has the Klein–Gordon equation as its Euler–Lagrange equation,

$$
S=\int\mathrm{d}^{4}x\;\mathrm{Sc}\Big[(\partial_{r'_t}\tilde\Xi)^{*}\partial_{r'_t}\tilde\Xi-\sum_{\eta}(\partial_{r_\eta}\tilde\Xi)^{*}\partial_{r_\eta}\tilde\Xi-k_m^{2}\tilde\Xi^{*}\tilde\Xi\Big],
$$

and its variation returns $\left(\Box_\Phi-k_m^{2}\right)\tilde\Xi=0$ in eight real components. The pairing is the Hermitian one, $\mathrm{Sc}(\cdot^{*}\cdot)$, because $\mathrm{Sc}(A^{*}A)=\sum_\mu\lvert a_\mu\rvert^{2}$ is real and non-negative while $\mathrm{Sc}(A^{\natural}A)=\sum_\mu a_\mu^{2}$ is complex and its real part is indefinite; the two agree only for real quaternionic coefficients, and the Klein–Gordon field has complex ones.

The action is the sum of four scalar actions, one per coefficient, with no cross term, because the four units are orthogonal for the pairing. The independence of the four coefficients is therefore a property of the Lagrangian and not only of the equation. A non-central Hermitian coefficient couples them, and then the four branches are the four eigenvalues of one Hermitian matrix.

The phase symmetry gives the charge, whose density is $j_{r'_t}=-2k_m\rho_{\mathrm{chg}}$, proportional to the parent's with a constant that is a normalization and a sign that is the action's. The charge is indefinite: it flips between the two frequency branches. Time translation gives the energy, which is non-negative on both branches, and the contrast between the two is the content of the parent's two defects read as one. Space translations and rotations give the stress tensor, which is the current of the four translations and needs no separate construction.

The second-order structure appears in the variational principle as the conjugate pair. The momentum is the conjugate of the field, the first-order action is the Legendre transform, and its equations are $\partial_{r'_t}\tilde\Xi=\Pi_\Xi$ and $\partial_{r'_t}\Pi_\Xi=\Delta_\Phi\tilde\Xi-k_m^{2}\tilde\Xi$. The closed-form exponential survives only there, as the real $2\times2$ block of a constant coefficient, and not on the element alone. There is no counterpart of the Schrödinger equation's two writings, because the operator does not factor over the algebra: the two first-order readings available are the conjugate pair and the spinor square root, and each doubles something.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^{2}=-e_t$ |
| $i$ | Central scalar imaginary, $i^{2}=-e_t$ |
| $\mathbb{B}_{C}$ | Centre, $\operatorname{span}_{\mathbb{R}}\{e_t,ie_t\}$ |
| $\mathbb{B}_{\Psi},\ \mathbb{B}_{\Phi}$ | Hermitian (observable) and anti-Hermitian (generator) subspaces |
| $^{*}$ | Hermitian conjugation |
| $^{\natural}$ | Quaternion conjugation |
| $\mathrm{Sc}$ | Coefficient of $e_t$; $\mathrm{Tr}=2\,\mathrm{Sc}$ |
| $\tilde\nabla_\Phi$ | Biquaternionic gradient, $\partial/\partial R_t$ and $\partial/\partial r_\eta$ |
| $\Box_\Phi=\Delta_\Phi-\partial^{2}/\partial r'^{2}_{t}$ | d'Alembertian on the material sector |
| $r'_t=c\,t'$ | Material time, a length |
| $\tilde\Xi=\sum_\mu\Xi_\mu e_\mu$ | The Klein–Gordon field, four complex coefficients |
| $\Xi_\mu$ | Coefficient of $e_\mu$; the four are independent in the free theory |
| $k_m=mc/\hbar$ | Mass wave number |
| $\tilde M\in\mathbb{B}_{\Psi}$ | Hermitian potential coefficient; $k_m^{2}e_t$ when free |
| $S,\ \mathcal{L}$ | Action and Lagrangian density |
| $\Pi_\Xi=(\partial_{r'_t}\tilde\Xi)^{*}$ | Conjugate momentum, the second element of the pair |
| $H$ | Hamiltonian, the energy of the pair |
| $k'_t=\sqrt{k_\Phi^{2}+k_m^{2}}$ | Temporal wave number of a free mode, in one length unit |
| $j_{r'_t},\ j_\eta$ | Noether current of the phase symmetry |
| $\rho_{\mathrm{chg}}$ | The parent's charge density; $j_{r'_t}=-2k_m\rho_{\mathrm{chg}}$ |
| $E_{\mathrm{nrg}}$ | Noether charge of time translation; non-negative |
| $T_{\mu\nu}$ | Stress tensor, the current of translations and rotations |
| $\mathrm{Sc}(A^{*}A)=\sum_\mu\lvert a_\mu\rvert^{2}$ | Hermitian bilinear; real and non-negative |
| $\mathrm{Sc}(A^{\natural}A)=\sum_\mu a_\mu^{2}$ | Quaternionic bilinear; complex in general |

## Further Reading

- Walter Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the Klein–Gordon equation, its Lagrangian, its current and its two defects.
- James D. Bjorken and Sidney D. Drell, *Relativistic Quantum Fields* (McGraw–Hill, 1965), for the canonical stress tensor of a complex scalar field and its improvement.
- James D. Bjorken and Sidney D. Drell, *Relativistic Quantum Mechanics* (McGraw–Hill, 1964), for the Klein–Gordon action and the canonical quantization that follows from it.
- Paul A. M. Dirac, *Lectures on Quantum Mechanics* (Belfer Graduate School, 1964), for the constrained systems that a first-order reading of a second-order equation produces; the conjugate pair of §*The Conjugate Pair* is the unconstrained case.
- The companion articles: [The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html), for the equation, its operator, its plane waves and its currents; [The Klein–Gordon Equation in Biquaternionic Polar Variables](the-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the same equation in the eight parameters; [The Variational Principle and the Klein–Gordon Equation in Biquaternionic Polar Variables](the-variational-principle-and-the-klein-gordon-equation-in-biquaternionic-polar-variables.html), for the polar action; [The Variational Principle and the Schrödinger Equation in Biquaternionic Form](the-variational-principle-and-the-schrodinger-equation-in-biquaternionic-form.html), for the first-order case, whose action is linear in the velocity and whose Noether charge is the density; [The Quantum Stress Tensor of the Biquaternion Scalar Field](the-quantum-stress-tensor-of-the-biquaternion-scalar-field.html), for the tensor, its improvement and its trace; [The Klein–Gordon Propagator and Its Green's Functions in Biquaternionic Form](the-klein-gordon-propagator-and-its-greens-functions-in-biquaternionic-form.html), for the varying-coefficient case; [The Path Integral and the Klein–Gordon Equation in Biquaternionic Form](the-path-integral-and-the-klein-gordon-equation-in-biquaternionic-form.html), for the sum over configurations, which is a different object from the extremum; [The First-Order Root of the Biquaternion Klein–Gordon Operator](the-first-order-root-of-the-biquaternion-klein-gordon-operator.html), for why the operator does not factor over the algebra; [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the spinor square root and the first-order action that the doubled field admits. [The Fourier Transform and the Variational Principle and the Klein–Gordon Equation in Biquaternionic Form](the-fourier-transform-and-the-variational-principle-and-the-klein-gordon-equation-in-biquaternionic-form.html), for the eigenvalue problem that the four scalar actions state in one sentence, its spectrum and the $c^{2}$ the display omits.
