# __Explicit Solutions of the Biquaternionic Dirac Equation__

## Introduction

**The question.** *The Dirac Equation in Biquaternionic Form* states the equation, its two components and the value of an element, and derives the Klein–Gordon equation for each half. It solves nothing. This article solves it: plane waves in the massless and in the massive case, the completion that turns harmonic scalars into solutions, the spherical and cylindrical families that follow from it, and the reading of the field itself as the gradient of a scalar potential, with its shifted operator, its nullness on the shifted cone and the constrained shift of the potential that leaves the field unchanged.

**What is used.** The boxed pair of that article,

$$
\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp},R}=k_m\,\tilde{Ξ}_{\mathrm{sp},L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\,\tilde{Ξ}_{\mathrm{sp},R},
$$

with $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ one element of $\mathbb{B}$ and $k_m$ the mass wave number. The gradient, its conjugate and their product $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Box$ are those of *Operator and Calculus Conventions*, and the coordinates, the frame and the four-position are those of *Frame and Metric Conventions*. Nothing of the three is repeated.

**The frame, and what it costs.** One frame is declared for the article, because the value of a part is read by the frame's third direction. The plane waves use it, the spherical and cylindrical families use it, and no second choice is made anywhere. The cost is visible in one place and nowhere else: a solution of definite value is a solution in a frame, and the helicity reading of the massless case is the frame-free statement, because there the third direction is the momentum's.

**The order.** Plane waves first, the massless before the massive, because the massless kernel fixes the shape of the massive one. The scalar-potential reading follows, since it is where the shift appears and where the nullness of the elementary field is read. The spherical and cylindrical families close the sequence, and they are built by the same completion.

**Two readings of one equation.** Every section below reads one equation in one of two ways: as an equation for an element, and as the same equation for its plane-wave coefficients in momentum space. Both are kept, because the kernel statement — a polarization biquaternion annihilated by the wave biquaternion — is visible only in the second, while nullness and the cone are visible only in the first.

## Plane-Wave Solutions

### Massless Plane Waves

Plane-wave solutions of the massless member written $R$ are

$$
\boxed{\;\tilde{Ξ}_{\mathrm{sp}}(\tilde R_\Phi) = \tilde{Ξ}_{\mathrm{sp},0} \exp\!\left(i\,\mathrm{Sc}\!\left(\tilde{K}_{\Phi}\tilde{R}_\Phi^{\natural}\right)\right)
= \tilde{Ξ}_{\mathrm{sp},0}\,\exp\!\big(i(\vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-k_{t}^{\prime} r'_t)\big)\;},
$$

where $\tilde{Ξ}_{\mathrm{sp},0} \in \mathbb{B}$ is a constant biquaternion, $\tilde{K}_{\Phi}=\frac{\tilde{P}_{\Phi}}{\hbar}= i k_{t}^{\prime} e_t + \vec e_x k_1 + \vec e_y k_2 + \vec e_z k_3$ (with $k_{t}^{\prime} = \omega/c$) is the wave biquaternion, and $\tilde R_\Phi = e_t (i r'_t) + \vec e_x r_x + \vec e_y r_y + \vec e_z r_z$ is the four-position biquaternion. The scalar part $\mathrm{Sc}(\tilde{K}_{\Phi}\tilde{R}_\Phi^{\natural}) = \vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) - k_{t}^{\prime} r'_t$ is real, so the exponent $i\,\mathrm{Sc}(\tilde{K}_{\Phi}\tilde{R}_{\Phi}^{\natural})$ is a purely imaginary central element; the exponential therefore commutes with $\tilde{Ξ}_{\mathrm{sp},0}$ and differentiates to left multiplication by $i\tilde{K}_{\Phi}$,

$$
\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp}} = i\tilde{K}_{\Phi}\,\tilde{Ξ}_{\mathrm{sp}},
$$

so the equation $\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp}} = 0$ becomes

$$
\tilde{K}_{\Phi}\tilde{Ξ}_{\mathrm{sp},0} = 0,
$$

i.e., the polarization biquaternion $\tilde{Ξ}_{\mathrm{sp},0}$ is annihilated by the wave biquaternion $\tilde{K}_{\Phi}$. This is the momentum-space massless equation in the algebra; its kernel has complex dimension two, and the basis operator acts on it with the two eigenvalues $+1$ and $-1$, one state each. Those two states are the two helicities in the frame whose third direction is the momentum's, one of each value, so the full massless field is the pair of this equation and its conjugate.

Nonzero solutions of $\tilde{K}_{\Phi}\tilde{Ξ}_{\mathrm{sp},0} = 0$ exist only when $\tilde{K}_{\Phi}$ is a zero divisor in $\mathbb{B}$, that is, when $\tilde{K}_{\Phi}$ is null: $\tilde{K}_{\Phi}\tilde{K}_{\Phi}^{\natural}= \tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural}/\hbar^{2}= 0$, equivalently $k_{t}^{\prime\,2} = k_\Phi^{2}$, the massless dispersion relation. In that case the kernel is a two-dimensional complex vector space, one state of each value; for non-null $\tilde{K}_{\Phi}$ the kernel is trivial.

### Massive Plane Waves

For the massive equation a single central-phase plane wave,

$$
\tilde{Ξ}_{\mathrm{sp}}(\tilde R_\Phi) = \tilde{Ξ}_{\mathrm{sp},0} \exp\!\left(i\,\mathrm{Sc}\!\left(\tilde{K}_{\Phi}\tilde{R}_\Phi^{\natural}\right)\right) = \tilde{Ξ}_{\mathrm{sp},0}\,\exp(i\theta), \qquad \theta = \vec k_\Phi\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) - k_{t}^{\prime} r'_t,
$$

does solve the pair, with one polarization biquaternion for each part, $\tilde{Ξ}_{\mathrm{sp},0} = \tilde{Ξ}_{\mathrm{sp},0}^L + \tilde{Ξ}_{\mathrm{sp},0}^R$. Differentiating as in the massless case, $\tilde\nabla_\Phi$ acts on $\exp(i\theta)$ as left multiplication by $i\tilde{K}_{\Phi}$ and $(\tilde\nabla_\Phi)^{\natural}$ as left multiplication by $i\tilde{K}_{\Phi}^{\natural}$, so the chiral pair becomes the momentum-space system

$$
i\tilde{K}_{\Phi}\,\tilde{Ξ}_{\mathrm{sp},0}^{R}= k_m\,\tilde{Ξ}_{\mathrm{sp},0}^L,
\qquad
i\tilde{K}_{\Phi}^{\natural}\,\tilde{Ξ}_{\mathrm{sp},0}^{L}= k_m\,\tilde{Ξ}_{\mathrm{sp},0}^R .
$$

Eliminating $\tilde{Ξ}_{\mathrm{sp},0}^L$ gives

$$\tilde{K}_{\Phi}\tilde{K}_{\Phi}^{\natural}\,\tilde{Ξ}_{\mathrm{sp},0}^R = -k_m^{2}\,\tilde{Ξ}_{\mathrm{sp},0}^R ,
$$

so a nonzero solution requires the **mass-shell condition**

$$\tilde{K}_{\Phi}\tilde{K}_{\Phi}^{\natural}=-k_m^{2},
$$

i.e., $-k_{t}^{\prime\,2} + \|\vec k_\Phi\|^2 = -k_m^{2}$, which is the standard mass-shell relation $k_{t}^{\prime\,2} = \|\vec k_\Phi\|^2 + k_m^{2}$ (with $k_{t}^{\prime}=\omega/c$ and $E=\hbar c\,k_{t}^{\prime}$). This is the biquaternion form of the standard relativistic energy-momentum relation $E^2 = \vec p^2 c^2 +m^{2}\,c^{4}$ (with $\vec p =\hbar\,\vec k_\Phi$), the same shell as the four-momentum kinematics of *The Dirac Equation in Biquaternionic Form*. The two signs of $k_{t}^{\prime}$ are the two frequency branches — the particle and the antiparticle — and with the two spin states they give the four solutions that the field carries.

## The Field as the Gradient of a Scalar Potential

The completion of the next section has a shifted form, and the shift is the operator of the companion *The Biquaternion D'Alembertian and Its Green's Functions*. With the **shifted gradient** $\tilde{\nabla}_\kappa = \tilde\nabla_\Phi + \kappa$,
$$
\tilde{\nabla}_\kappa(\tilde\nabla_\Phi)^{\natural}_\kappa = \Box + 2\kappa\,\partial/\partial R_t + \kappa^2 ,
$$
because the two spatial parts cancel in the sum of the operator and its conjugate, $\tilde\nabla_\Phi+(\tilde\nabla_\Phi)^{\natural}=2e_t\,\partial/\partial R_t=2\,\partial/\partial R_t$, since $e_t=1$. A **scalar** solution of that operator therefore produces a field of the algebra,
$$
\left(\Box + 2\kappa\,\partial/\partial R_t + \kappa^2\right) u = 0
\quad\Longrightarrow\quad
\tilde{\nabla}_\kappa\left((\tilde\nabla_\Phi)^{\natural}_\kappa u\right) = 0 ,
$$
and the field is the shifted conjugate gradient of a potential: one element of $\mathbb{B}$ built from another by differentiation, with no column and no second carrier. At $\kappa = 0$ it is the completion $\tilde{Ξ}_{\mathrm{sp}}\mapsto(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{\mathrm{sp}}$ of the next section, and for $\kappa \neq 0$ it is its shifted form. The source calls the scalar generator a **C-field** and takes the field to be the convolution of $(\tilde\nabla_\Phi)^{\natural}_\kappa\tilde{Ξ}_{\mathrm{sp},0}$ with it, which is how the same construction produces extended rather than only elementary solutions; the convolution is the one developed in the companion article on distributions.

**Why the elementary field is null.** For the elementary case the potential is a plane wave, $\xi_{\mathrm{scl}}=\exp(i(\vec k_\Phi\cdot(r_x\vec e_x+r_y\vec e_y+r_z\vec e_z)-\omega r'_t/c))$, and the field is read off by differentiating it. In the coordinate $Q_t=i q'_t$ the time derivative is $\partial\xi_{\mathrm{scl}}/\partial R_t=-\omega\xi_{\mathrm{scl}}$ and the three spatial ones are $\partial_k\xi_{\mathrm{scl}}=ik_k\xi_{\mathrm{scl}}$, so
$$
(\tilde\nabla_\Phi)^{\natural}_\kappa\,\xi_{\mathrm{scl}} = \bigl((\kappa-\omega)\,e_t - i k_x\vec e_x - i k_y\vec e_y - i k_z\vec e_z\bigr)\xi_{\mathrm{scl}} ,
$$
and its quaternion norm is the shifted symbol of the operator,
$$
\left\langle(\tilde\nabla_\Phi)^{\natural}_\kappa\,\xi_{\mathrm{scl}}\right\rangle_{\natural} = (\omega-\kappa)^2 - \|\vec k_\Phi\|^2 .
$$
The two lines are one statement in two languages: the norm of the field vanishes exactly when the potential solves the shifted scalar equation, so the field is a zero divisor on the shifted cone, as the massless plane-wave fields of the preceding subsection are on the light cone. The zero-divisor cone of the algebra is the light cone, and the shifted cone is the norm-zero set of the shifted operator. The source normalises its representatives and records separate norm and pseudonorm values for them; the corpus keeps the invariant statement, that the element is null, and the dictionary between the source's mass $m$ and the corpus shift $\kappa$ — $\kappa = -i\,k_m$, so that the source's imaginary mass is a real shift — is the one recorded in the d'Alembertian companion.

**The completion is exhaustive, and the mass takes the place of the shift.** The construction above is not only a way to manufacture examples. In the massive chiral pair the second half is the completion of the first,

$$
\tilde{Ξ}_{\mathrm{sp},L}=1/k_m\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp},R} ,
\qquad
\tilde{Ξ}_{\mathrm{sp},R}=1/k_m(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{\mathrm{sp},L} ,
$$

so a free Dirac field carries nothing that one part does not already carry, and the consistency of the pair is the Klein–Gordon equation $\Box\tilde{Ξ}_{\mathrm{sp},R}=\tilde{Ξ}_{\mathrm{sp},R}\,k_m^{2}$ of *Klein–Gordon from the Dirac Square in Biquaternionic Form*. The source states the same identity in its own variables, the second half computed from the first by differentiation. One structural difference separates this from the shifted completion above: the shift contributes the first-order-in-time term $2\kappa\,\partial/\partial R_t$ and so moves the cone, whereas the mass contributes a constant and leaves the cone where it is. The mass is not a central shift of the operator — it is the off-diagonal pairing of *The Massive Case* — and what the two share is only the shape of the implication, one half of the field being a gradient of the other.

**The potential is defined only up to a constrained shift.** The map $u\mapsto(\tilde\nabla_\Phi)^{\natural}_\kappa u$ is not injective. Any $u'$ with $(\tilde\nabla_\Phi)^{\natural}_\kappa u'=0$ leaves the field unchanged, and such $u'$ are supplied by the scalars: every $\zeta$ solving the shifted scalar equation gives one, $u'=\tilde{\nabla}_\kappa\zeta$, because $(\tilde\nabla_\Phi)^{\natural}_\kappa\tilde{\nabla}_\kappa=\Box+2\kappa\,\partial/\partial R_t+\kappa^2$. The potential is therefore fixed only up to

$$
u\longmapsto u+\tilde{\nabla}_\kappa\zeta ,
\qquad
\bigl(\Box+2\kappa\,\partial/\partial R_t+\kappa^2\bigr)\zeta=0 ,
$$

which was checked on both branches of the shifted cone. The gauge function is **constrained** by the scalar equation, and that is what separates this freedom from a local phase: no arbitrary function, no connection, no curvature, no gauge boson. What the freedom states is structural, and it is the electromagnetic analogy taken at its word: the field is the invariant object and the scalar is its potential, as the field strength is the invariant object of the Maxwell potential, so that the free Dirac field stands to its Klein–Gordon potential as a strength stands to a potential. The source states the same for the free massive field, whose Dirac field is invariant under a shift of its Klein–Gordon potentials by a solution of the conjugate Dirac equation; under the dictionary $\kappa=-i\,k_m$, that is $k_m=i\kappa$, that operator is $i(\tilde\nabla_\Phi)^{\natural}_\kappa$, the shifted conjugate gradient up to the unit $i$, so the corpus records the structure once. The source adds that its alternative, potential-based transformation of the Dirac field is nonlinear on the field and free of two-valuedness under a full rotation. The boundary is worth keeping explicit: that alternative is a solution-generating map, and the linear representation on the algebra, whose two-valuedness *The Spin–Statistics Theorem in Biquaternionic Form* uses, is untouched by it.


## Spherical and Cylindrical Solutions

### Spherical Solutions

Spherical solutions of the biquaternionic Dirac equation can be constructed by the methods of the shifted operator, adapted to the biquaternion algebra. The standard technique is the **completion** of scalar harmonic functions: given a harmonic scalar function on the sphere, the completion produces a biquaternion-valued function that lies in the kernel of the Dirac operator.

The construction is more involved than the corresponding construction for the Maxwell equation, because $\tilde\nabla_\Phi$ is not the operator whose square is the scalar wave operator. One has

$$
\tilde{\nabla}^2 = \frac{\partial^2}{\partial R_t^2} - \Delta + 2\,\frac{\partial}{\partial R_t}\,\vec\nabla ,
$$

a derived form, whose first-order cross term does not vanish, so $\tilde{\nabla}^2 \neq \Box$. It is the **conjugate** gradient that squares to the d'Alembertian, $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}= \Box$, so the completion operator is $(\tilde\nabla_\Phi)^{\natural}$: for every harmonic scalar function $\tilde{Ξ}_{\mathrm{sp}}$ with $\Box\tilde{Ξ}_{\mathrm{sp}} = 0$, the function $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{\mathrm{sp}}$ satisfies

$$
\tilde\nabla_\Phi\left((\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{\mathrm{sp}}\right) = \Box\tilde{Ξ}_{\mathrm{sp}} = 0
$$

and is a solution of the massless Dirac equation. This is the biquaternion form of the completion of the scalar harmonic functions, and it is the reason the spherical solutions are indexed by the scalar spherical harmonics.

For the massless case, the spherical solutions of the biquaternionic Dirac equation are the **completed spherical harmonics**, and they form a basis of the solution space. For the massive case, the construction is more involved: the solution is a combination of the completed spherical harmonics and their anti-Hermitian conjugates, with coefficients determined by the mass-shell condition.

The spherical solutions describe the **angular momentum states** of a relativistic fermion. The quantum numbers $(n, \ell, m)$ correspond to the radial, orbital, and magnetic quantum numbers of the standard hydrogen-like Dirac equation.

### Cylindrical Solutions

Cylindrical solutions are similarly constructed from cylindrical harmonics by the same completion technique. They describe **waveguide modes** of a fermion field in a cylindrical geometry, with the transverse-electric and transverse-magnetic modes corresponding to the two spin states.

## Summary

**Plane waves.** A plane wave $\tilde{Ξ}_{\mathrm{sp},0}\exp(i\,\mathrm{Sc}(\tilde K_\Phi\tilde R_\Phi^{\natural}))$ turns the gradient into left multiplication by $i\tilde K_\Phi$, so the massless member becomes $\tilde K_\Phi\tilde{Ξ}_{\mathrm{sp},0}=0$. A nonzero polarization exists only for null $\tilde K_\Phi$, that is on the light cone $k_t^{\prime\,2}=k_\Phi^{2}$, and the kernel is then two-dimensional with one state of each value. The massive case becomes the momentum-space pair $i\tilde K_\Phi\tilde{Ξ}_{\mathrm{sp},0}^{R}=k_m\tilde{Ξ}_{\mathrm{sp},0}^{L}$, $i\tilde K_\Phi^{\natural}\tilde{Ξ}_{\mathrm{sp},0}^{L}=k_m\tilde{Ξ}_{\mathrm{sp},0}^{R}$, whose solvability is the mass shell $\tilde K_\Phi\tilde K_\Phi^{\natural}=-k_m^{2}$, that is $k_t^{\prime\,2}=\|\vec k_\Phi\|^{2}+k_m^{2}$. The two signs of $k_t^{\prime}$ are the particle and the antiparticle, and with the two spin states they give the four solutions the field carries.

**Completion.** The operator whose square is the d'Alembertian is the conjugate gradient, $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Box$, so $\tilde{Ξ}_{\mathrm{sp}}\mapsto(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{\mathrm{sp}}$ carries every harmonic scalar into a solution. The spherical and cylindrical families are the completed harmonics, and the constancy of the construction is why they are indexed by the scalar harmonics of the same geometry.

**The field as a gradient.** With the shifted gradient $\tilde\nabla_\kappa=\tilde\nabla_\Phi+\kappa$ one has $\tilde\nabla_\kappa\tilde\nabla_\kappa^{\natural}=\Box+2\kappa\,\partial/\partial R_t+\kappa^{2}$, so a scalar solving the shifted equation produces the field $\tilde\nabla_\kappa^{\natural}u$. For a plane-wave potential the field is null exactly when the potential solves that equation, so the field is a zero divisor on the shifted cone; at $\kappa=0$ the cone is the light cone. In the massive pair the same shape holds with the mass in place of the shift, each half being the completion of the other, but the mass contributes a constant and leaves the cone where it is.

**The gauge freedom is constrained.** The potential is fixed only up to $u\mapsto u+\tilde\nabla_\kappa\zeta$ with $\zeta$ a solution of the shifted scalar equation. The gauge function obeys the same equation as the potential, and that is what separates the freedom from a local phase: no arbitrary function, no connection, no curvature, no gauge boson.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $\tilde{Ξ}_{\mathrm{sp}}$, $\tilde{Ξ}_{\mathrm{sp},L,R}$ | The field and its two components, as in *The Dirac Equation in Biquaternionic Form* |
| $\tilde K_\Phi=i k_t^{\prime}e_t+\vec k_\Phi=\tilde P_\Phi/\hbar$ | The wave biquaternion; $k_t^{\prime}=\omega/c$ |
| $\tilde R_\Phi=i r'_t\,e_t+r_x\vec e_x+r_y\vec e_y+r_z\vec e_z$ | The four-position biquaternion |
| $k_m=\dfrac{mc}{\hbar}$ | The mass wave number, the coefficient of the mass term |
| $k_\Phi=\omega\sqrt{\epsilon\mu}$ | The propagation wave number of the medium, equal to $k_t^{\prime}$ on the light cone |
| $\Box=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$ | The d'Alembertian, a central scalar |
| $\tilde\nabla_\kappa=\tilde\nabla_\Phi+\kappa$ | The shifted gradient, with $\kappa\in\mathbb{C}$ central |
| $\xi_{\mathrm{scl}}$ | The scalar (pseudoscalar-potential) coefficient, the potential of the elementary field |
| $u$, $\zeta$ | The scalar potential of the field and the gauge function of the constrained shift |
| $\vec\nabla$, $\Delta$ | The spatial gradient and the Laplacian; $\tilde\nabla^{2}=\partial_t^{2}-\Delta+2\,\partial_t\vec\nabla$ |

## Further Reading

- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the chiral pair, the value of an element and the two-sided dictionary that these solutions obey.
- [The Three Wavenumbers of a Particle](the-three-wavenumbers-of-a-particle.html), for $k_m$, $k_\Phi$ and $k_t^{\prime}$ and the unit argument that fixes the coefficient of the mass term.
- [The Biquaternion D'Alembertian and Its Green's Functions](the-biquaternion-dalembertian-and-its-greens-functions.html), for the shifted operator $\tilde\nabla_\kappa$ and its symbol.
- [Klein–Gordon from the Dirac Square in Biquaternionic Form](klein-gordon-from-the-dirac-square-in-biquaternionic-form.html), for the consistency condition that makes the two halves of the massive pair one field.

- V. V. Kassandrov and N. V. Markova, "New symmetries, conserved quantities and gauge nature of a free Dirac field," arXiv:2209.00460 (2022), for the free Dirac field read as the gauge-invariant strength of a quadruple of Klein–Gordon potentials fixed only up to a constrained gradient shift, for its own two-field form $b=(i/m)Wa$ in which one half is the derivative of the other, for the singular solutions of the shifted kernel — the spinorial Yukawa analogue, a string-like solution and a stationary solution of finite field charge — and for the remark that the potential-based transformation of the Dirac field is nonlinear and free of two-valuedness, recorded in §*The Field as the Gradient of a Scalar Potential* above as a boundary and not as a replacement of the canonical law.
- V. G. Bagrov and D. M. Gitman, *Exact Solutions of Relativistic Wave Equations* (Kluwer, Dordrecht, 1990), for the encyclopaedic compendium and review of the known exact solutions of the Dirac equation up to the late 1980s.
