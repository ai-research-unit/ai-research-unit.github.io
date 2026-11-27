# __Hamiltonian Field Theory in Biquaternionic Form__

## Introduction

The companion article *The Lagrangian and Hamiltonian Mechanics* ends where the finite-dimensional theory ends: one configuration biquaternion $\tilde q$, one momentum biquaternion $\tilde p$, one phase-space biquaternion $\tilde q+i\tilde p$, and a Poisson bracket on the functions of that finite collection of numbers. A field is not a finite collection of numbers. Its configuration is a *function* of the position, and the variational derivative replaces the partial derivative: the Legendre transform acts on a density, the momentum conjugate to the field is itself a function of the position, and the bracket that survives is a bracket on functionals. This article performs that transcription twice: **once in general**, for a field valued in a module over the algebra, where the transform, its regularity and the bracket are stated with no carrier named; and **once in full for the central scalar field** of the Klein–Gordon articles, which is the Klein–Gordon column of the dictionary's five and the case three later sections of this category take as given.

The order is deliberate. **The general case is what the slot owes; the scalar is what is worked.** A reader who needs the scalar formulas reads from §*The Scalar Column: The Standard Hamiltonian Field Theory* onward, and loses nothing by starting there; a reader who needs to know what the slot means at another rung reads §*The Generic Case* and §*The Other Four Columns*, and finds in them the two statements the scalar case cannot supply — that regularity is a property of a Hessian on a module, and that the failure of regularity is a constraint whose count the later sections quote.

Two objects are built here, and they answer two different questions. The first is the **Hamiltonian density** $\mathcal H$, the Legendre transform of the Lagrangian density, which is also the energy density of the companion article on stress–energy; the second is the **field Poisson bracket**, the bracket on functionals of the field and its conjugate momentum, together with the continuity equation that the density satisfies along the motion. Their sum is the classical Hamiltonian field theory in biquaternion form. The article then says where the algebra's contribution stops: at a rung whose Hessian is a multiple of the identity the bracket is the standard one, and the biquaternion content is the packaging of the density and the flux rather than a change of the bracket — and at the rungs whose Hessian is not, the bracket is the Dirac bracket and the count of constraints is what the change costs. The genuinely different Hamiltonian formalism for a field — the covariant one, in which the conjugate object is a *quadruple* of momenta rather than one momentum field — is named at the end and developed in the mathematical corpus.

The conventions are those of the read list: the algebra, the invertibles, the sectors, the material coordinate, the $i r'_t$ metric, the d'Alembertian and the conjugations are those of *Algebra and Element Conventions*, *Physics Units and Common Elements Conventions* and *Operator and Calculus Conventions*, and none is restated here. The central scalar field is $\tilde{Ξ}(\tilde R_\Phi)=\xi(\tilde R_\Phi)e_t$ with $\tilde R_\Phi\in\mathbb{B}_{\Phi}$, its Lagrangian density is the one fixed by *Noether's Theorem in Biquaternionic Form* and used by *Canonical Quantization of the Biquaternion Klein–Gordon Field*,

$$
\mathcal{L}=-\mathrm{Sc}\!\left[((\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}^{*})(\tilde\nabla_\Phi\tilde{Ξ})\right]-4\pi^{2}\nu_m^{2}\,\mathrm{Sc}\!\left[\tilde{Ξ}^{*}\tilde{Ξ}\right]
=|\partial\xi/\partial r'_t|^2-|\vec\nabla_\Phi\xi|^2-4\pi^{2}\nu_m^{2}|\xi|^2,
\qquad \nu_m=\frac{mc}{h},
$$

and the equation of motion is $\left(\Box_\Phi-4\pi^{2}\nu_m^{2}\right)\tilde{Ξ}=0$, that is $\partial^2\xi/\partial {r'_{t}}^2=c^2(\Delta_\Phi\xi-4\pi^{2}\nu_m^{2}\xi)$.

The companion articles are:

- Companion article *The Lagrangian and Hamiltonian Mechanics*, for the finite-dimensional Legendre transform, the phase-space biquaternion and the Poisson bracket that this article extends to a density.
- Companion article *The Non-Quantum Limit of the Action Principle and the Lagrangian*, for the action and its first variation, and for the boundary term that the field case reproduces as a flux.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the Lagrangian density, the conserved currents, and the canonical energy–momentum tensor.
- Companion article *Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form*, for the energy–momentum biquaternion and the electromagnetic packaging that the scalar field's density and flux repeat.
- Companion article *Canonical Quantization of the Biquaternion Klein–Gordon Field*, for the quantum theory that takes this classical canonical structure over without modification, and for the constraint analysis of the Dirac and Maxwell fields that this article contrasts with.

## The Generic Case: The Legendre Transform on a Module

**The carrier is a module, and the transform is a map between a module and its dual.** At every rung of the ladder the field takes its values in some space $\mathcal M$ over the algebra — the centre for the scalar rungs, the spinor module for the Dirac rung, the four-component complex vector space for the Proca rung, the Hermitian matrices for the matrix rung — and the Lagrangian density is a real function of the field, of its four derivatives and of the position. **The conjugate momentum is then not a number but an element of the dual module**, defined by the variational derivative

$$
\Pi=\frac{\delta L}{\delta\left(\partial_{t}X\right)}\in\mathcal M^{*},
\qquad
\left\langle\Pi,\delta X\right\rangle=\frac{d}{d\epsilon}L\left[X,\partial_{t}X+\epsilon\,\delta X\right]\Big|_{\epsilon=0},
$$

where $\left\langle\cdot,\cdot\right\rangle$ is the pairing the rung supplies — the Hermitian form for the scalar rungs, the spinor form for the Dirac rung, the weighted sum for the Proca rung, the trace for the matrix rung, exactly the row the dictionary calls *the pairing*. **The Legendre transform is the same display at every rung**,

$$
\mathcal H=\left\langle\Pi,\partial_{t}X\right\rangle-L,
$$

and so is the pair of Hamilton equations, $\partial_{t}X=\delta H/\delta\Pi$ and $\partial_{t}\Pi=-\delta H/\delta X$. What differs between the rungs is not the transform but the **Hessian**,

$$
\mathbb H=\frac{\delta^{2}L}{\delta\left(\partial_{t}X\right)\delta\left(\partial_{t}X\right)}:\ \mathcal M\longrightarrow\mathcal M^{*},
$$

and the transform is called **regular** when $\mathbb H$ is an isomorphism of modules. **That is the whole of the generic statement, and it is worth stating in this abstract form because the scalar case makes it look automatic.** At the central rung $\mathbb H$ is the identity map on $\mathbb C$ and regularity is invisible; at four of the five rungs it is not, and the failure is the constraint.

### The Regularity Table

**The table records, for each rung, what the Hessian is, whether it is invertible, and what replaces the inverse when it is not.** The constraint counts are the ones [The Dirac–Bergmann Algorithm](the-dirac-bergmann-algorithm-first-and-second-class-constraints.html) derives; the momentum entries are the ones each band's article writes.

| rung | value space $\mathcal M$ | conjugate momentum | Hessian | constraint structure | bracket |
|---|---|---|---|---|---|
| Schrödinger | $\mathbb C$ (central) | $i\frac{h}{2\pi}\tilde\Xi^{*}$ | rank zero: the density is first order in the velocity | none; four word momenta vanish identically | the canonical bracket on $(\tilde\Xi,\tilde\Pi_{\mathrm{id}})$ |
| Klein–Gordon | $\mathbb C$ (central) | $\pi=\left(\partial\xi/\partial r'_{t}\right)^{*}$ | the identity: **regular** | none | the field Poisson bracket |
| Dirac | the spinor module | the first-order bilinear; $\pi-i\tilde\Xi^{\dagger}\approx0$ | rank zero: first order throughout | eight second-class, four degrees of freedom | the Dirac bracket, then the anticommutator |
| Proca | the complex vector part | $\pi^{0}=0$; $\pi^{\imath}=-F^{0\imath*}$ | rank three of four | two second-class, three degrees of freedom | the Dirac bracket |
| $\mathrm{SU}(4)$ | Hermitian $4\times4$ and the connection | $\Pi=\left(D_{t}\Xi\right)^{\dagger}$; the connection's momenta constrained | regular on the sixteen matter directions, singular on the fifteen connection directions | fifteen first-class Gauss laws, fifteen degrees of freedom | the bracket with the trace pairing, projected by the Gauss laws |

**Read the table by column and the four failures are four different things, and only one of them is a gauge symmetry.** The Schrödinger rung's vanishing Hessian is a *first-order* action: the density is a coordinate and its conjugate is fixed by the action rather than by a constraint, and the Legendre transform is carried by the kinetic matrix instead of the second variation — which is why the Schrödinger articles speak of a kinetic metric and not of a mass matrix. **The Dirac rung's vanishing Hessian is also first order, and there the consequence is a genuine constraint pair**, because the spinor's conjugate is not free to be eliminated: the four components carry eight real second-class conditions. **The Proca rung's rank-three Hessian is a constraint of the same second-class kind**, and its two conditions are the primary $\pi^{0}=0$ and the Gauss law, which is why the Proca fluid's Euler equation is two of the frame's components and not all four. **The connection's rank-three Hessian is the one first-class failure**: its kernel is the gauge orbit, the Gauss laws generate the gauge transformations, and no gauge-invariant quantity depends on the eliminated direction. **A reader who treats all four as "the Legendre transform is singular" has the right formal statement and the wrong physics**, and the table is the four-way split.

### The Bracket Without a Carrier

**The canonical bracket is the inverse of the Hessian read as a bivector on the phase space.** For a module-valued field the phase space is the space of pairs $(X,\Pi)$ with $\Pi\in\mathcal M^{*}$, and the bracket of two functionals is

$$
\{A,B\}=\int d^{3}r\left(
\left\langle\frac{\delta A}{\delta X},\frac{\delta B}{\delta\Pi}\right\rangle
-\left\langle\frac{\delta A}{\delta\Pi},\frac{\delta B}{\delta X}\right\rangle
\right),
$$

with the pairing evaluated at the point. **Three consequences, and the third is the one a reader is most likely to get wrong.**

- **Where the Hessian is a multiple of the identity the bracket is the standard one**, and its value on two linear functionals is the pairing itself. The scalar column is this case, and it is why the scalar canonical structure can be handed to the quantization article untouched.
- **Where the Hessian is singular the display above is not a bracket on the whole phase space**; the Dirac–Bergmann algorithm restricts it to the constraint surface, and the restricted object is the Dirac bracket. **The second-class cases are where the Dirac bracket is a genuine replacement** — the Dirac and Proca rungs — and the first-class case is where a gauge fixing is needed before a bracket exists at all.
- **The bracket is not the commutator.** The commutator is the algebra's product defect, and it enters the *equation of motion* of a matrix-valued observable, as [A Matrix-Valued Charge Cannot Be Contracted](a-matrix-valued-charge-cannot-be-contracted-three-couplings-and-the-inner-derivation.html) shows. It enters the bracket only through the non-commutativity of the two variational derivatives inside the pairing. **A reader who writes "the matrix bracket is the commutator" has conflated the force slot with the bracket slot**, and the dictionary keeps them as separate rows for that reason.

**What the module statement buys, in three items.** First, *regularity* has a definite meaning at every rung — invertibility of a module map — so the phrase "the Legendre transform is regular" is a claim and not a formula. Second, *the constraint count is the kernel of the Hessian*, so the Dirac–Bergmann table is not an independent piece of bookkeeping but the rank statement of this section's $\mathbb H$. Third, *the scalar column's completeness is explained*: its Hessian is the identity, its kernel is empty, its bracket is the standard one, and the algebra's contribution there is the packaging rather than the dynamics. **The rest of the article fills that column.**

## The Scalar Column: The Standard Hamiltonian Field Theory

**The column this section fills is the Klein–Gordon column of the dictionary's five, and the one every later section of this category uses.** Its Hessian is the identity and its bracket is unconstrained, so the standard formalism transcribes without qualification; the other four columns are named in §*The Other Four Columns* and computed in their bands.

### The Conjugate Momentum Field

The Legendre transform of a field theory is performed pointwise in the position and acts on the Lagrangian *density*. Write $\partial\xi/\partial r'_t$ for the time derivative at fixed position and define the **conjugate momentum field** by the partial derivative of the density with respect to the velocity field,

$$
\pi=\frac{\partial\mathcal{L}}{\partial\left(\partial\xi/\partial r'_t\right)}=\left(\partial\xi/\partial r'_t\right)^{\,*},
\qquad
\pi^\dagger=\frac{\partial\mathcal{L}}{\partial\left(\partial\xi/\partial r'_t\right)^{\,*}}=\partial\xi/\partial r'_t .
$$

The second formula is the conjugate of the first, and both are needed because the field is complex; on the real field $\xi=\xi^*$ the two agree. The transform is **regular**: $\pi$ determines $\partial\xi/\partial r'_t$ and conversely, since $\partial\xi/\partial r'_t=c^2\pi^\dagger$, so the phase space of the theory is the full space of pairs $(\xi,\pi)$ at each position and there is no constraint. This is the first structural fact of the transcription, and it is the point at which the scalar field differs from the two fields whose quantization the corpus treats alongside it. The Dirac field, being first order in time, carries a second-class constraint $\pi-i\tilde{Ξ}^{\dagger}\approx0$; the Maxwell field, being a connection, carries the two first-class constraints $\pi^0\approx0$ and $\mathrm{div}\,\vec\pi\approx0$; the scalar field carries neither. A regular Legendre transform is what makes the phase space unconstrained, and an unconstrained phase space is what makes the Hamiltonian transcription a transposition with nothing added.

### The Hamiltonian Density

The Legendre transform of the density is the **Hamiltonian density**

$$
\mathcal{H}=\pi\partial\xi/\partial r'_t+\pi^\dagger\left(\partial\xi/\partial r'_t\right)^{\,*}-\mathcal{L},
$$

and the **total Hamiltonian** is its integral over space, $H=\int\mathcal{H}\,d^3r$. Substituting the density and the momentum field gives

$$
\mathcal{H}=|\partial\xi/\partial r'_t|^2+|\vec\nabla_\Phi\xi|^2+4\pi^{2}\nu_m^{2}|\xi|^2,
$$

the sum of three squares. Two remarks fix the sign bookkeeping. First, **the Hamiltonian density is not minus the Lagrangian density**, although it is so for a mechanical Lagrangian whose kinetic energy is quadratic in the velocities: here $-\mathcal{L}=|\partial\xi/\partial r'_t|^2-|\vec\nabla_\Phi\xi|^2-4\pi^{2}\nu_m^{2}|\xi|^2$, which differs from $\mathcal{H}$ by the kinetic term again, since the Legendre transform of a complex field pairs $\pi$ with $\partial\xi/\partial r'_t$ *and* $\pi^\dagger$ with $\left(\partial\xi/\partial r'_t\right)^{*}$. Second, **the density is the energy density**: the expression above is exactly the time–time component $T_{00}$ that *Noether's Theorem in Biquaternionic Form* obtains from translation invariance, positive because it is a sum of squares. The Hamiltonian of the field and the energy of the field are the same functional, and that is not a coincidence of the conventions but the content of the Legendre transform for a Lagrangian with no explicit time dependence.

### The Hamiltonian Field Equations

Hamilton's equations for the field are the pair

$$
\partial\xi/\partial r'_t=\frac{\delta H}{\delta\pi^\dagger}=c^2\pi^\dagger,
\qquad
\partial\pi/\partial r'_t=-\frac{\delta H}{\delta\xi^\dagger}=-c^2(\Delta_\Phi\xi-4\pi^{2}\nu_m^{2}\xi),
$$

where $\delta/\delta$ is the variational derivative and the second equation uses the first to eliminate $\pi$. Eliminating $\pi$ between them returns $\partial^2\xi/\partial {r'_{t}}^2=c^2(\Delta_\Phi\xi-4\pi^{2}\nu_m^{2}\xi)$, the Klein–Gordon equation: the Hamiltonian field equations and the Euler–Lagrange equation are the same equations, exactly as in the finite-dimensional case. The only new feature is that the conjugate equation is a *PDE for a density* rather than an ODE for a number, and the variational derivative is what makes the pairing between them work.

### The Field Poisson Bracket

The bracket of the finite-dimensional theory is replaced by a bracket on functionals. For functionals $A[\xi,\pi]$, $B[\xi,\pi]$ of the field and its conjugate momentum,

$$
\{A,B\}=\int d^3r\left(
\frac{\delta A}{\delta\xi}\frac{\delta B}{\delta\pi}
+\frac{\delta A}{\delta\xi^{\,*}}\frac{\delta B}{\delta\pi^\dagger}
-\frac{\delta A}{\delta\pi}\frac{\delta B}{\delta\xi}
-\frac{\delta A}{\delta\pi^\dagger}\frac{\delta B}{\delta\xi^{\,*}}
\right),
$$

so that the canonical brackets are the distributional relations

$$
\boxed{\ \{\xi(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),\pi(\vec y)\}=\delta^3(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z-\vec y)\ },
\qquad
\{\xi(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),\xi(\vec y)\}=\{\pi(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),\pi(\vec y)\}=0,
$$

with the conjugates carrying the mirrored signs. The bracket is antisymmetric and satisfies the Jacobi identity, and it does so **locally**: the Jacobi sum of three functionals is an integral of a sum of terms each of which is the Jacobi sum of the corresponding local expression in $(\xi,\pi)$ at a point, which vanishes because the finite-dimensional bracket of the canonical pair vanishes. The field bracket is therefore not a new algebraic structure; it is the same bracket applied at every point and integrated, and the delta functions are the statement that distinct points do not interact through the bracket. The Hamiltonian flow of the total Hamiltonian along the bracket is the field equation: for any functional $A$, $\partial A/\partial r'_t=\{A,H\}$, which on the canonical pair returns the pair of equations above.

### The Continuity Equation and the Energy Flux

The energy density is conserved along the motion by a local conservation law. Differentiating $\mathcal{H}$ in time and using the equation of motion gives

$$
\boxed{\ \partial/\partial r'_t\mathcal{H}+\vec\nabla_\Phi\cdot\vec S=0\ },
\qquad
\vec S=-(\left(\partial\xi/\partial r'_t\right)^{\,*}\vec\nabla_\Phi\xi+\partial\xi/\partial r'_t\,\vec\nabla_\Phi\xi^{\,*})=-c^2(\pi\nabla\xi+\pi^\dagger\nabla\xi^{\,*});
$$

the mass terms cancel between the time derivative of $\nu_m^{2}|\xi|^2$ and the equation of motion, and the surviving terms are a divergence. The vector $\vec S$ is the **energy flux**. For a single plane wave $\xi=\xi_0\exp(i\theta_{\mathrm{pwp}})$ one has $\vec S=2\omega2\pi\vec\nu_\Phi|\xi_0|^2$, directed along the wavevector, so the energy travels the way the wave travels. Integrating the conservation law over a volume and using the vanishing of the flux at infinity makes the four-momentum

Here $\theta_{\mathrm{pwp}}:=2\pi\vec\nu_\Phi\cdot\vec r-\omega r'_t/c\in\mathbb{R}$ is the plane-wave angle: $\omega$ and $\vec\nu_\Phi$ are real, so the exponent is $i$ times a real number and the wave form is $\exp(i\theta_{\mathrm{pwp}})$ wherever it is quoted.

$$
P_{\jmath}=\frac{1}{c}\int T_{t\jmath}\,d^3r
$$

time-independent, the statement that the flux of the companion stress–energy article is a conserved current.

## The Scalar Column in the Algebra

### The Field and Its Conjugate Momentum

The field is central-valued, $\tilde{Ξ}=\xi e_t$, and its conjugate momentum is central-valued for the same reason: the momentum field is obtained from the field by a central operation, so it lives in the centre. Writing

$$
\tilde\Pi_{\mathrm{id}}=\pi e_t\in\mathbb{B}_{C},
$$

the pair $(\tilde{Ξ},\tilde\Pi_{\mathrm{id}})$ is the field-theoretic analogue of the pair $(\tilde q,\tilde p)$ of the finite-dimensional article, with one difference that is worth stating: $\tilde q$ was a real quaternion in $\mathbb{B}_{H}$ and $\tilde p$ its conjugate momentum in the same subspace, while $\tilde{Ξ}$ and $\tilde\Pi_{\mathrm{id}}$ are central, in $\mathbb{B}_{C}$. The value space is smaller because the spin of the field is zero. A field that carried a spinor index would take its values in the spinor module, and its conjugate momentum would carry the same index; the central scalar is the case in which the index is absent, and in that case the momentum field is a second complex number at each point rather than a second biquaternion.

### The Hamiltonian Density as a Hermitian Bilinear

The density is the sum of two Hermitian forms. With $\tilde\nabla_\Phi\tilde{Ξ}$ the biquaternionic gradient of the field — its four coefficients are the four partial derivatives, $(\partial/\partial R_t\,\xi,\partial/\partial R_x\xi,\partial/\partial R_y\xi,\partial/\partial R_z\xi)$ —

$$
\boxed{\;\mathcal{H}=\mathrm{Sc}\!\left[(\tilde\nabla_\Phi\tilde{Ξ})^{*}(\tilde\nabla_\Phi\tilde{Ξ})\right]+4\pi^{2}\nu_m^{2}\,\mathrm{Sc}\!\left[\tilde{Ξ}^{*}\tilde{Ξ}\right]\;}.
$$

The second term is the mass form, positive and central. The first is the **kinetic-plus-gradient form**, and the identity $\mathrm{Sc}[(\tilde\nabla_\Phi\tilde{Ξ})^{*}(\tilde\nabla_\Phi\tilde{Ξ})]=|\partial\xi/\partial r'_t|^2+|\vec\nabla_\Phi\xi|^2$ is where the $i r'_t$ convention does its quiet work: the time coefficient of the gradient is $\partial/\partial R_t\,\xi=-ic^{-1}\partial\xi/\partial r'_t$, so $|\partial/\partial R_t\,\xi|^2=|\partial\xi/\partial r'_t|^2$ and the kinetic term is *positive*, not negative. This is the same sign that makes the norm of a material four-vector have inertia $(3,1)$ and the d'Alembertian $\Box_\Phi=\partial^2/\partial R_t^2+\Delta_\Phi$; a reader who computes $|\partial/\partial R_t\,\xi|^2$ as $-|\partial\xi/\partial r'_t|^2$ has conjugated the operator instead of the field, and will find the kinetic energy negative. The form $\tilde Q_1^{*}\tilde Q_1$ is of course positive definite on the algebra — that is the Hermitian form of $\mathbb{B}_{\Psi}$ — and it is *this* form, not the holomorphic norm $\langle\tilde Q_1\rangle_{\natural} = \langle\tilde Q_1,\tilde Q_1\rangle_{\natural}=\tilde Q_1\tilde Q_1^{\natural}$ of inertia $(3,1)$, that the energy density uses. The distinction matters: the norm's vanishing set is the light cone, the Hermitian form's is only the origin.

### The Energy–Momentum Biquaternion

The density and the flux are the scalar and vector parts of one Hermitian biquaternion:

$$
\tilde\Sigma_{\Psi}=\mathcal{H}\,e_t+\frac{i}{c}\vec S\in\mathbb{B}_{\Psi},
\qquad
\tilde\nabla_\Phi\tilde\Sigma_{\Psi}=0
\ \ \text{on shell}.
$$

The scalar part of the biquaternion divergence is the continuity equation. This is the *same packaging* that the companion article on stress–energy gives the electromagnetic field, $\tilde\Sigma_{\Psi}=\frac{1}{2}\tilde F\tilde F^{*}=W\,e_t+\frac{i}{c}\vec S$, whose scalar part is the Poynting theorem; the scalar field's energy density sits in the scalar direction of the informational sector and its flux in the three vector directions $i\vec e_{\imath}$, so the two fields' energy–momentum biquaternions are elements of the same sector in the same arrangement. The one difference is that the electromagnetic $\tilde\Sigma_{\Psi}$ is bilinear in the field strength whereas the scalar $\tilde\Sigma_{\Psi}$ is bilinear in the gradient of the field, which is the field-theoretic way of saying that the scalar field carries no spin and its energy comes entirely from the derivatives.

The static limit makes the arrangement visible. For a time-independent field the flux vanishes, $\tilde\Sigma_{\Psi}=\mathcal{H}e_t$, and the conservation law reduces to $\vec\nabla_\Phi\cdot\vec S=0$, which is empty; the energy is conserved trivially. For a running wave it is the other way: $\mathcal{H}$ and $|\vec S|/c$ are equal and the biquaternion has the null-field pattern of a single travelling wave, exactly as the companion stress–energy article records for the massless scalar and for the electromagnetic wave.

### The Brackets in the Algebra

The canonical bracket is read in the algebra as the scalar part of a pairing. Since $\xi$ and $\pi$ are the coefficients of central elements, the bracket of the algebra's central directions is the bracket of the two complex numbers, and the field bracket above is its integral over space. The biquaternion content of the brackets is therefore not a new bracket but the **sector bookkeeping** of the fields being bracketed: $\tilde{Ξ}\in\mathbb{B}_{C}$ while its gradient is not, and the momentum $\tilde\Pi_{\mathrm{id}}$ is central whereas the momentum of a bivector-valued field would lie in $\mathbb{B}_{\Phi}$ or $\mathbb{B}_{\Psi}$. The scalar field brackets with itself in the centre, and this is the classical face of the fact, recorded by the quantization article, that the scalar field's canonical structure is taken over from the classical theory without modification.

## The Other Four Columns

**The other four columns of the dictionary are named here and computed in their bands; none of them is derived in this article.** The reason to name them is that the scalar column's three results — a density that is a Hermitian form, equations that are the field equation, a bracket that is the standard one — are *not* transported by substitution, and a reader who assumes they are will get each of the three wrong at the rungs where the Hessian fails.

- **The Schrödinger column.** The field is first order, so the conjugate is $i\frac{h}{2\pi}\tilde\Xi^{*}$ and the density is the coordinate rather than a function of it. The density and the phase are the pair, the bracket is the canonical one on that pair, and the four momenta of the polar word $r$, $\theta_{\mathrm{rpd}}$, $\varrho$ and $\theta_{\mathrm{rpa}}$ vanish identically — the vanishing is a property of the chart and not a constraint. The polar Lagrangian article writes the chart and the vanishing momenta; the energy is the Hamiltonian of the parent equation.
- **The Dirac column.** The first-order action gives eight real second-class conditions, the Dirac bracket replaces the Poisson bracket, and the promotion of that bracket is the *anticommutator* and not the commutator. The Hamiltonian, the normal-ordering constant and the mode algebra are *Canonical Quantization of the Biquaternion Dirac Field*'s, and the constraint analysis is the Dirac–Bergmann article's; the present article contributes only the row.
- **The Proca column.** Rank three of four: the primary $\pi^{0}=0$ and the Gauss law are second class, the Dirac bracket is the replacement, and the three remaining degrees of freedom are the two transverse and one longitudinal mode. The Hamiltonian and the constraint structure are *Canonical Quantization of the Biquaternion Proca Field*'s.
- **The connection column.** For the Maxwell field the two constraints per generator are first class, the Gauss laws generate the gauge transformations, and the bracket exists only after a gauge fixing or as a Dirac bracket on the gauge-invariant functionals. *Canonical Quantization of the Biquaternion Maxwell Field* owns the construction.
- **The matrix column.** The matter directions are regular and the fifteen connection directions are not: the Gauss laws are first class, and the count is the Dirac–Bergmann table's sixty phase-space components, fifteen primary and fifteen secondary, fifteen degrees of freedom. **The corpus does not write the $\mathrm{SU}(4)$ Hamiltonian, and nothing in this category needs it** — the matrix rung's equations are used in their Euler–Lagrange form, and the Hamiltonian appears only as the count. That is a gap and it is recorded as one, not concealed by a substitution.

**What is not claimed, stated once.** This article does not claim that the scalar column's formulas hold at the other four; it claims that the *slot* has a definite meaning at each of them, and that the meaning is the Hessian and the bracket. **A reader who wants a column's formula goes to the article named in its bullet; a reader who wants to know what the column's slot is reads the table.**

## The Sector Reading of the Hamiltonian Density

The field of spin zero is the field of the centre, and the centre is the direct sum of the two sectors' scalar lines, $\mathbb{B}_{C}=T_{\mathrm i}\oplus T_{\mathrm m}$ with $T_{\mathrm i}=\mathbb{R}e_t$ and $T_{\mathrm m}=\mathbb{R}(ie_t)$. Writing the complex scalar as two real scalars, one in each sector's scalar direction,

$$
\tilde{Ξ}=\frac{1}{\sqrt2}\left(\underbrace{\xi_1\,e_t}_{\in\,\mathbb{B}_{\Psi}}+\underbrace{\xi_2\,ie_t}_{\in\,\mathbb{B}_{\Phi}}\right),
\qquad
\mathrm{Sc}\!\left[\tilde{Ξ}^{*}\tilde{Ξ}\right]=\frac12\left(\xi_1^2+\xi_2^2\right),
$$

the Hamiltonian density splits accordingly,

$$
\mathcal{H}=\frac12\left[
\left(\left(\partial\xi_{1}/\partial r'_t\right)^{2}+\left(\partial\xi_{2}/\partial r'_t\right)^{2}\right)
+|\vec\nabla_\Phi\xi_1|^2+|\vec\nabla_\Phi\xi_2|^2
+4\pi^{2}\nu_m^{2}\left(\xi_1^2+\xi_2^2\right)
\right],
$$

the sum of the two sectors' kinetic, gradient and mass terms. Three features of this split are the ones the informational articles use. First, **both sectors contribute to the energy with the same sign**, so the energy is positive whichever sector carries the field. Second, the split is not the charge: the energy is the sum of the sector contributions, positive definite, whereas the charge is the pairing of the two sectors' fields that is antisymmetric in them, $j_0\propto\mathrm{Im}(\xi^*\partial\xi/\partial r'_t)\propto\xi_1\partial\xi_{2}/\partial r'_t-\xi_2\partial\xi_{1}/\partial r'_t$, and its sign is not fixed. The same two readings appear in the phase-space biquaternion of the companion symplectic article as the real and imaginary parts of the Hermitian pairing: the real part is the metric and is additive over the sectors, the imaginary part is the symplectic form and is antisymmetric. Third, **the split is a split of the kinetic and gradient terms as well as the mass term**, so the sector exchange that the oscillator article realises as a quarter-period advance is, in the field, an exchange of the two real scalars at every point.

## Covariant Hamiltonian Field Theory

The formalism so far is the **instantaneous** one: it singles out a time direction, differentiates with respect to it, and conjugate to the field there is one momentum field. It is the formalism in which the equal-time brackets of the quantization article are written, and it is the one in which the constraint analysis of the connection can be performed at all. It is not, however, the only Hamiltonian formalism for a field, and its relation to the covariant one is worth stating here because the connections' Hamiltonian structure lives on the other side.

In the **covariant** formalism, all four derivatives of the field are treated on the same footing and conjugate to the field there is a *quadruple* of momenta, the **polymomentum** $p_{\imath}=\partial\mathcal{L}/\partial(\partial/\partial R_{\imath}\,\xi)$, one per direction of differentiation. The Legendre transform is performed on the quadruple, and the resulting **De Donder–Weyl Hamiltonian** is $H=\sum_{\imath} p_{\imath}\partial/\partial R_{\imath}\,\xi-\mathcal{L}$, a function of the field and the four momenta. For the scalar field the polymomentum is the gradient, $p_{\imath}=\partial/\partial R_{\imath}\xi$, and the De Donder–Weyl Hamiltonian is $\frac12\sum_{\imath} p_{\imath} p_{\imath}+\frac12\nu_m^{2}\xi^2$, so the covariant equations

$$
\partial/\partial R_{\imath}\,\xi=\frac{\partial H}{\partial p_{\imath}},
\qquad
\sum_{\imath}\partial/\partial R_{\imath}\,p_{\imath}=-\frac{\partial H}{\partial\xi}
$$

are the four-fold statement of the Klein–Gordon equation. Nothing is singled out and nothing is split, which is the formalism's virtue and its price: there is no unique pairing of the momenta with a single time, so there is **no covariant Poisson bracket**. The bracket of this article is the instantaneous one, and it exists because a time direction was chosen. The polymomentum formalism is the multisymplectic one; its geometry, its relation to the instantaneous formalism, and the theorem that its equations agree with the Euler–Lagrange equations for a hyperregular density belong to the mathematical corpus, in *Multisymplectic and Covariant Hamiltonian Field Theory*, and the present article only records the point of contact: the instantaneous Hamiltonian density is the time component of the conserved multimomentum current of the covariant formalism, $\mathcal{H}=J_{00}$, which is why the two descriptions agree on the energy.

## What the Transcription Does and Does Not Give

**For this column**, what the algebra gives the Hamiltonian field theory is short and definite. The generic statement above is the other half of the answer and is column-independent: regularity is invertibility of the Hessian, and the constraint count is its kernel.

- **The Hamiltonian density is a Hermitian form.** The kinetic, gradient and mass contributions are each the scalar part of a form built from the field and its gradient, and the assembled density is $\mathrm{Sc}[(\tilde\nabla_\Phi\tilde{Ξ})^{*}(\tilde\nabla_\Phi\tilde{Ξ})]+4\pi^{2}\nu_m^{2}\mathrm{Sc}[\tilde{Ξ}^{*}\tilde{Ξ}]$. The form is the algebra's own Hermitian pairing, not a transcription of a foreign object, and the $i r'_t$ convention makes its kinetic term positive.
- **The energy density and the flux are one sector element.** They are the scalar and vector parts of the Hermitian biquaternion $\tilde\Sigma_{\Psi}=\mathcal{H}e_t+\frac{i}{c}\vec S\in\mathbb{B}_{\Psi}$, with $\tilde\nabla_\Phi\tilde\Sigma_{\Psi}=0$ on shell — the same element, in the same sector and the same arrangement, that the electromagnetic field's energy–momentum occupies.
- **The sector split is the energy–charge split.** The two real scalars in the two sectors' scalar directions contribute to the energy with the same sign and to the charge with opposite signs, and the split of the density is the field version of the phase-space biquaternion's real and imaginary parts.

What the algebra does not give, and what a reader should not expect, is a modification of the bracket. The scalar field is central, its conjugate momentum is central, and the bracket on functionals of the pair is the standard one; the Jacobi identity holds for the same local reason it holds for a finite system, and no algebraic anomaly appears. **This is a statement about the Klein–Gordon column and not about the slot**: the brackets in which the algebra's non-commutativity and the sector structure are load-bearing are those of the fields that carry an index — the Dirac field on the spinor module, whose conjugate momentum is constrained, and the connections, whose conjugate momenta are constrained — and those columns are the ones §*The Other Four Columns* names, each with the article that computes it. The scalar field is the case in which the Hamiltonian transcription is complete and uninteresting, which is exactly why it is the case in which the classical canonical structure can be handed to the quantization article untouched.

## Summary

**The generic statement.** A field takes its values in a module $\mathcal M$ over the algebra; its conjugate momentum is an element of the dual module defined by the variational derivative against the rung's pairing; the Legendre transform is $\mathcal H=\left\langle\Pi,\partial_{t}X\right\rangle-L$ at every rung; and the transform is regular when the Hessian $\mathbb H:\mathcal M\to\mathcal M^{*}$ is an isomorphism. **The five columns are read off one table**: the Klein–Gordon column is the regular one, the Schrödinger and Dirac columns are first order with a vanishing Hessian, the Proca column is rank three of four, and the connection columns are singular exactly on the gauge directions. Where the Hessian is singular the bracket is the Dirac bracket, and the constraint count is the kernel's dimension — the Dirac–Bergmann table, not a separate bookkeeping.

**The Klein–Gordon column** is built from three objects.

**The conjugate momentum and the density.** The momentum field is $\pi=\left(\partial\xi/\partial r'_t\right)^{\,*}$ and its conjugate $\pi^\dagger=\partial\xi/\partial r'_t$; the Legendre transform is regular, so the phase space is unconstrained. The Hamiltonian density is $\mathcal{H}=\pi\partial\xi/\partial r'_t+\pi^\dagger\left(\partial\xi/\partial r'_t\right)^{\,*}-\mathcal{L}=|\partial\xi/\partial r'_t|^2+|\vec\nabla_\Phi\xi|^2+4\pi^{2}\nu_m^{2}|\xi|^2$, which is not minus the Lagrangian density and is the energy density $T_{00}$ of the translation current. In the algebra it is the Hermitian form $\mathcal{H}=\mathrm{Sc}[(\tilde\nabla_\Phi\tilde{Ξ})^{*}(\tilde\nabla_\Phi\tilde{Ξ})]+4\pi^{2}\nu_m^{2}\mathrm{Sc}[\tilde{Ξ}^{*}\tilde{Ξ}]$, positive because the $i r'_t$ convention puts the kinetic term in with a plus.

**The equations and the bracket.** Hamilton's field equations, $\partial\xi/\partial r'_t=\delta H/\delta\pi^\dagger$ and $\partial\pi/\partial r'_t=-\delta H/\delta\xi^\dagger$, are the Klein–Gordon equation; the field Poisson bracket is the integral over space of the local canonical bracket, with $\{\xi(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),\pi(\vec y)\}=\delta^3(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z-\vec y)$, and its Jacobi identity is inherited locally from the canonical pair. The density satisfies the continuity equation $\partial/\partial r'_t\mathcal{H}+\vec\nabla_\Phi\cdot\vec S=0$ with flux $\vec S=-(\left(\partial\xi/\partial r'_t\right)^{\,*}\vec\nabla_\Phi\xi+\partial\xi/\partial r'_t\nabla\xi^{\,*})=-c^2(\pi\nabla\xi+\pi^\dagger\nabla\xi^{\,*})$, positive-directed along the wavevector for a plane wave.

**The packaging and the sector interpretation.** Density and flux are the scalar and vector parts of the Hermitian biquaternion $\tilde\Sigma_{\Psi}=\mathcal{H}e_t+\frac{i}{c}\vec S\in\mathbb{B}_{\Psi}$, with $\tilde\nabla_\Phi\tilde\Sigma_{\Psi}=0$ on shell — the electromagnetic arrangement. Splitting the central field into its two sector scalars, the energy is the sum of the two sectors' kinetic, gradient and mass terms with the same sign, whereas the charge is their difference with opposite signs.

The formalism is the instantaneous one. The covariant formalism treats the four derivatives alike, conjugates to the field a quadruple of polymomenta, and has no unique bracket and no unique pairing with a time; it is the multisymplectic geometry of the mathematical corpus, and the instantaneous density is its time component.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal M$, $\mathcal M^{*}$ | the value space of a field and its dual, the rung's pairing understood (the dictionary's columns) |
| $\Pi=\delta L/\delta\left(\partial_{t}X\right)$ | the conjugate momentum as an element of the dual module; a number only where the pairing is the standard one |
| $\mathbb H=\delta^{2}L/\delta\left(\partial_{t}X\right)^{2}$ | the Hessian; the transform is regular when it is an isomorphism, and its kernel is the constraint count |
| $\tilde{Ξ}=\xi\,e_t$ | The central scalar field, $\xi:\mathbb{R}^{1,3}\to\mathbb{C}$, $\tilde R_\Phi=i r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z\in\mathbb{B}_{\Phi}$ |
| $\mathcal{L}=|\partial\xi/\partial r'_t|^2-|\vec\nabla_\Phi\xi|^2-4\pi^{2}\nu_m^{2}|\xi|^2$ | The Lagrangian density, the sign fixed by *Noether's Theorem in Biquaternionic Form* |
| $1/(2\pi\nu_m)$ | The length of one radian of the mass phase, $\frac{1}{2\pi\nu_m}$, the range of the force; its reciprocal $2\pi\nu_m=\frac{2\pi mc}{h}$ is the angular mass wave number, the mass parameter of the Klein–Gordon equation |
| $\pi=\partial\mathcal{L}/\partial\left(\partial\xi/\partial r'_t\right)=\left(\partial\xi/\partial r'_t\right)^{\,*}$ | The conjugate momentum field, and $\pi^\dagger=\partial\xi/\partial r'_t$ its conjugate |
| $\tilde\Pi_{\mathrm{id}}=\pi\,e_t\in\mathbb{B}_{C}$ | The conjugate momentum field as a central biquaternion |
| $\mathcal{H}=\pi\partial\xi/\partial r'_t+\pi^\dagger\left(\partial\xi/\partial r'_t\right)^{\,*}-\mathcal{L}$ | The Hamiltonian density; it is $|\partial\xi/\partial r'_t|^2+|\vec\nabla_\Phi\xi|^2+4\pi^{2}\nu_m^{2}|\xi|^2$ and equals the energy density $T_{00}$ |
| $H=\int\mathcal{H}\,d^3r$ | The total Hamiltonian |
| $\mathcal{H}=\mathrm{Sc}[(\tilde\nabla_\Phi\tilde{Ξ})^{*}(\tilde\nabla_\Phi\tilde{Ξ})]+4\pi^{2}\nu_m^{2}\mathrm{Sc}[\tilde{Ξ}^{*}\tilde{Ξ}]$ | The Hamiltonian density as the sum of two Hermitian forms |
| $\{\xi(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),\pi(\vec y)\}=\delta^3(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z-\vec y)$ | The canonical field bracket, with the mirrored brackets for the conjugates |
| $\{A,B\}$ | The field Poisson bracket on functionals, the integral over space of the local canonical bracket |
| $\vec S=-(\left(\partial\xi/\partial r'_t\right)^{\,*}\vec\nabla_\Phi\xi+\partial\xi/\partial r'_t\nabla\xi^{\,*})=-c^2(\pi\nabla\xi+\pi^\dagger\nabla\xi^{\,*})$ | The energy flux; $\partial/\partial r'_t\mathcal{H}+\vec\nabla_\Phi\cdot\vec S=0$ |
| $\tilde\Sigma_{\Psi}=\mathcal{H}e_t+\frac{i}{c}\vec S\in\mathbb{B}_{\Psi}$ | The energy–momentum biquaternion of the field, with $\tilde\nabla_\Phi\tilde\Sigma_{\Psi}=0$ on shell |
| $p_{\imath}=\partial\mathcal{L}/\partial(\partial/\partial R_{\imath}\,\xi)=\partial/\partial R_{\imath}\xi$ | The polymomentum of the covariant (De Donder–Weyl) formalism |
| $H_{DW}=\sum_{\imath} p_{\imath}\partial/\partial R_{\imath}\,\xi-\mathcal{L}=\frac12\sum_{\imath} p_{\imath} p_{\imath}+2\pi^{2}\nu_m^{2}\xi^2$ | The De Donder–Weyl Hamiltonian of the scalar field |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_{\imath}\lvert Q_{2\imath}\rvert^{2}$ |

## Further Reading

- H. Goldstein, C. P. Poole and J. L. Safko, *Classical Mechanics* (3rd ed., Addison-Wesley, 2002), for the continuum Lagrangian, the field Hamiltonian and the transition from the discrete to the continuous phase space.
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (4th ed., Pergamon, 1975), for the canonical energy–momentum tensor and the energy density of the scalar field.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the canonical formalism, the equal-time brackets and the constraint analysis of the connection.
- James D. Bjorken and Sidney D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the scalar-field canonical quantization and the Klein–Gordon momentum field.
- Paul A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for the first-class and second-class constraint analysis of the Maxwell and Dirac fields.
- Jerrold E. Marsden and Tudor S. Ratiu, *Introduction to Mechanics and Symmetry* (2nd ed., Springer, 1999), for the field-theoretic Poisson bracket and its relation to the multisymplectic structure.
- Mark J. Gotay, James Isenberg, Jerrold E. Marsden and Richard Montgomery, "Momentum maps and classical relativistic fields," *Physics Reports* (2004), for the covariant Hamiltonian formalism of field theory and the polymomentum.
- [The Non-Quantum Limit of the Action Principle and the Lagrangian](the-non-quantum-limit-of-the-action-principle-and-the-lagrangian.html), companion article, for the finite-dimensional Legendre transform, the phase-space biquaternion, the bracket that this article extends to a density, the action, its first variation and the boundary term.
- [Noether's Theorem in Biquaternionic Form](noethers-theorem-in-biquaternionic-form.html), companion article, for the Lagrangian density and the canonical energy–momentum tensor.
- [Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form](stress-energy-conservation-laws-and-the-field-action-in-biquaternionic-form.html), companion article, for the energy–momentum biquaternion of the electromagnetic field and the conservation law for field and matter.
- [Canonical Quantization of the Biquaternion Klein–Gordon Field](canonical-quantization-of-the-biquaternion-klein-gordon-field.html), companion article, for the quantization of the classical structure built here.
- [Multisymplectic and Covariant Hamiltonian Field Theory](../articles_maths/multisymplectic-and-covariant-hamiltonian-field-theory.html), companion article in the mathematical corpus, for the polymomentum, the De Donder–Weyl equations and the multisymplectic form.
