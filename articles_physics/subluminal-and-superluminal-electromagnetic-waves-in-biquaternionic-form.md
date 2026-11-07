# __Subluminal and Superluminal Electromagnetic Waves in Biquaternionic Form__

## Introduction

This article records an external programme, that of Waldyr Alves Rodrigues Jr. and Jayme Vaz Jr. as presented in *Subluminal and Superluminal Electromagnetic Waves and the Lepton Mass Spectrum* (arXiv:hep-th/9607231, 1996). It works in the **bundle of differential forms** over Minkowski spacetime and studies the single equation

$$
\tilde\nabla\tilde F = 0
$$

for the field $\tilde F$, together with the spinor sector of the same algebra. From that starting point it claims two things. The first is that the free Maxwell equation has **subluminal and superluminal** solutions that are **undistorted progressive waves** and carry **non-null field invariants** and longitudinal field components — a family larger than the transverse plane waves of the textbook account. The second is that, writing the field as a **spinor bilinear** $F=-\tilde{Ξ}_{\mathrm{sp}}\vec e_z\tilde{Ξ}_{\mathrm{sp}}^{\natural}$, the free Maxwell equation is equivalent to a **non-linear Dirac–Hestenes equation** for $\tilde{Ξ}_{\mathrm{sp}}$, and that this non-linear equation **linearises**: its two coefficients collapse into one real coefficient once the source's constraints hold, and that coefficient is a constant mass when the current is conserved; the same section shows the massless Dirac equation to be a Maxwell equation with an **axial (magnetic) current**.

A third claim follows, and it is the other half of the paper's title. The family of projections attached to the **Takabayasi angle** is what produces the **lepton mass spectrum**: at $\theta_{\mathrm{dua}}=\pi/2$ the muon mass comes out of the fine-structure constant and a magnetic quantum number, with no adjustable parameter left except that number itself.

The corpus records the programme and does not endorse it. Its value here lies in the structural part: the spinor representation of the field, the criterion that selects the linear equation, and the axial-current form of the massless equation. That part is **rigorous and checkable**, and it bears directly on questions the corpus states elsewhere: the invariant classification of *The Field-Strength Biquaternion and Its Invariants*, which classifies the field by its two invariants and notes that they are not conserved by the free evolution, but does not exhibit the family of free solutions that carry non-null invariants; the Dirac–Hestenes formulation of *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form*, which already carries the Yvon–Takabayasi angle as an "angle zero for a pure electron state" but not the criterion that makes the equation linear; and the axial-current form of the massless equation, which the spinor bilinear reproduces.

The source's conventions are close to the corpus's, and the places where they part are flagged as they come up, so that formulas are not misread between the two. The units, the central $i$ and the sign vector $\varepsilon=(1,-1,-1,-1)$ are those of *Conventions in the Biquaternion Universe*; the field $\tilde F$, the spinor $\tilde{Ξ}_{\mathrm{sp}}$ and the volume element $\omega$ are elements of the biquaternion algebra $\mathbb{B}$.

**The calculus.** Everything below is written with the biquaternionic gradient of *Operator and Calculus Conventions*,

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial R_\mu}
=e_t\frac{\partial}{\partial R_t}+\vec e_x\frac{\partial}{\partial R_x}+\vec e_y\frac{\partial}{\partial R_y}+\vec e_z\frac{\partial}{\partial R_z},
$$

with its quaternion conjugate $\tilde\nabla^{\natural}=\sum_\mu\varepsilon_\mu e_\mu\,\partial/\partial R_\mu$ and the d'Alembertian $\Box=\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla=\partial^2/\partial R_t^2+\Delta_Q$, which on the material sector reads $\Delta-\partial^2/\partial{r'_{t}}^2$. The gradient is an element with derivative coefficients. It acts by left multiplication, on one field, and it uses no matrix and no second side.

The free field equation is the corpus's Maxwell equation of *Maxwell's Equations in the Biquaternionic Formulation*,

$$
\tilde\nabla\tilde F=0,\qquad \tilde F=i\sqrt\epsilon\,\vec E-\sqrt\mu\,\vec H ,
$$

which in vacuum reads $\tilde F=i\vec E-\vec B$. Its scalar part carries the two divergences and its vector part the two curls, so the one equation is the four Maxwell equations. It is first order in one field and needs no operator beyond the gradient. What it cannot do is carry a mass: the square of the gradient is not scalar, $\tilde\nabla^2\ne\Box$, because $e_t$ commutes with the spatial units and the mixed derivatives add instead of cancelling. The corpus's massive equation is therefore the chiral pair

$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=\frac{k_m}{\tilde{Ξ}_{\mathrm{sp},L}},\qquad  \tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=\frac{k_m}{\tilde{Ξ}_{\mathrm{sp},R}},
$$

two first-order equations in two chiral halves, and the spinorial part below is read in that form. Here $\hbar/(mc)$ is the mass length.

**The source's letter.** The source writes its calculus with one letter for a first-order operator of its own, one generator per coordinate. That operator is not one of the corpus's conventions, and this article neither uses it nor displays it. The free-field content of the source is carried here by $\tilde\nabla$; the massive content by the chiral pair. Where the source's own equation is translated, the translation is stated once, and no cell appears.

**Worked action.** The operator is read off the multiplication table of the units. With $c=1$, constants die, and a coordinate times a unit returns the product of that coordinate's unit with the unit.

| $\tilde{Ξ}_{\mathrm{sp}}$ | $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}$ |
|---|---|
| $\vec e_z$ | $0$ |
| $q_x\vec e_y$ | $\vec e_z$ |
| $r'_t\vec e_x$ | $-i\vec e_x$ |
| $\sin q_x\,\vec e_x$ | $-\cos q_x\,e_t$ |

The time entry carries the $-i$ of $\partial/\partial R_t=-i\,\partial/\partial r'_t$; the spatial entries carry the multiplication table, $\vec e_x\vec e_y=\vec e_z$ and $\vec e_x\vec e_x=-e_t$. These are the values of the gradient, not of the source's own operator, and they are the only ones used below.

The source's **volume element** is the product of its four frame generators. In the algebra it acts on the field as right multiplication by $-\vec e_z$, so the element is

$$
\omega=-\vec e_z,\qquad \omega^2=\vec e_z^2=-e_t,
$$

the **pseudoscalar** of the source's display, and a root of $-e_t$. Its signs against the units are fixed once: it anticommutes with $\vec e_x$ and $\vec e_y$ and commutes with $\vec e_z$ and $e_t$. The source writes its duality generator as $i$ and sets $i\equiv\omega$; that letter is this element, not the central $i$ of the corpus, and the two agree only in the source's display. The article keeps $\omega$ for it, so that the central $i$ stays the corpus's central $i$. Every $\exp(\omega\theta_{\mathrm{dua}})$ below is $\cos\theta_{\mathrm{dua}}+\omega\sin\theta_{\mathrm{dua}}$, the source's duality rotation.

The source's fixed bivector is $-\vec e_z$, and it is the **spin plane**: it plays in the source's equation the role the corpus's Dirac–Hestenes equation gives to its own fixed bivector, and it multiplies the spinor on the **right**. As an element it *is* the volume element $\omega$ displayed just above, so the spin plane and the source's duality generator are one element, which is why one symbol does both jobs in the source.

The spinor $\tilde{Ξ}_{\mathrm{sp}}$ is an element of the biquaternion algebra $\mathbb{B}$, which is the corpus's own algebra. The source reaches the same structural equivalences from its bundle of forms, and the corpus records it as a different technical road to them, cross-referencing rather than merging.

## Maxwell's Equation

### The plane wave and the duality

The free equation $\tilde\nabla\tilde F=0$ is solved by the plane wave

$$
\tilde F = f\,\exp(i\theta_{\mathrm{pha}}),\qquad \theta_{\mathrm{pha}}=k_0x_0-\vec k\cdot\vec q ,
$$

with $f$ a constant element and $k$ the propagation vector. The gradient acts on the phase through the symbol

$$
\tilde K=k_0-i\vec k,\qquad \vec k=\sum_k\vec e_k k_k ,
$$

so the equation is $\tilde Kf=0$. Applying $\tilde K^{\natural}$ on the left gives $\tilde K^{\natural}\tilde Kf=(k_0^2-|\vec k|^2)f=0$, and the propagation vector is **null**,

$$
k^2=0\quad\Longleftrightarrow\quad k_0=\pm|\vec k| .
$$

The condition $\tilde Kf=0$ is four independent complex conditions on the six complex components of $f$. On a null $k$ its kernel is two-dimensional, the two polarizations, and on the whole kernel $f^2=0$: the plane wave has **null invariants**. The step is not a cancellation, because a null $\tilde K$ has no inverse; it is the rank of left multiplication by a null element. Checked on the six components for several null $k$, the kernel is two-dimensional and $f^2=0$ on it. The invariant $\tilde F^2=f^2\exp(2i\theta_{\mathrm{pha}})$ vanishes with it.

Both facts are the standard ones, and the source's point in restating them is the contrast with what follows — the plane waves of the free equation sit on the special null case, and the source then exhibits solutions that do not.

The role of the volume element is worth one paragraph, because the source insists on it. Since $\omega^2=-1$, the source's exponential splits as $\exp(\omega\theta_{\mathrm{pha}})=\cos\theta_{\mathrm{pha}}+\omega\sin\theta_{\mathrm{pha}}$, and the electric and magnetic parts of its field are a quarter period apart. That is the source's display. The corpus writes the same plane wave with the central $i$, and its **duality rotation** is $F\mapsto\exp(i\theta)F$, as in *The Field-Strength Biquaternion and Its Invariants*. The source's $\omega$ and the corpus's central $i$ are different elements; both square to $-1$ and both generate a phase, and the article keeps them apart. The duality parameter is the one that governs the non-linear equation below.

### The Hertz potential

The solutions of the next two sections are generated by a **Hertz potential**. The source's theorem is that a 2-form $\pi$ satisfying the wave equation $\Box\pi=0$ produces, through the potential $A=-\delta\pi$ and the field $F=dA$, a field satisfying the free equation $\tilde\nabla\tilde F=0$. In the corpus's operators the input is $\Box\pi=0$ and the output is $\tilde\nabla\tilde F=0$. The two steps between them belong to the source's form calculus, where $d\delta+\delta d=\Box$ makes the proof one line; they are not reproduced here, and no operator beyond $\Box$ and $\tilde\nabla$ is needed to state the result. The device converts a scalar solution of the wave equation into an electromagnetic field with the desired properties.

## Subluminal Solutions

### The stationary solution

Throughout, the time coordinate is written $r'_t$ — the source's $t$ — for the frame in which a given solution is written.

The source takes the Hertz potential to be the bivector $\pi=Ξ\,\vec e_z$; the factor $\vec e_z$ multiplies on the **left**, and $Ξ$ is a function of the phase $\omega\Omega r'_t$ alone, so it commutes with the bivector. The scalar part is separated as

$$
Ξ(r'_t, r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) = \xi(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\,\exp(\omega\Omega r'_t),
$$

so that the wave equation becomes the Helmholtz equation $\nabla^2\xi+\Omega^2\xi=0$. The simplest solution is the spherical one $\xi(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)=C\,\sin(\Omega r)/r$, and the resulting stationary field $F_0$ is **regular at the origin** and **vanishes at infinity** — a localised field configuration at rest in the adapted frame. Written in the electric–magnetic split $F_0=\vec E_0+\omega\vec B_0$ it is

$$
\vec E_0=-\vec W\sin\Omega r'_t, \qquad \vec B_0=\vec W\cos\Omega r'_t,
$$

with $\vec W(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)$ a fixed vector field, given explicitly in the source in terms of $\alpha=\Omega r\cos\Omega r-\sin\Omega r$ and $\theta_{\mathrm{dua}}=3\alpha+\Omega^2r^2\sin\Omega r$, with the angular dependence of the lowest spherical harmonics.

Three of its properties are the point of the construction. First, the invariant $I_1=\vec E_0^2-c^2\vec B_0^2$ and the pseudo-invariant $I_2=\vec E_0\cdot\vec B_0$ of *The Field-Strength Biquaternion and Its Invariants* are **not zero**. Here $\vec E_0^2$ is the sum of squared components, as in that article: the source's $\vec E$ and $\vec B$ are three-vectors whose units square to $+1$, as in the vector calculus, not spatial units $\vec e_k$, which square to $-1$. Both fields are parallel to $\vec W$ and a quarter period apart, so in the source's units $c=1$

$$
I_2=-\tfrac12|\vec W|^2\sin 2\Omega r'_t,\qquad I_1=-|\vec W|^2\cos 2\Omega r'_t,
$$

and $I_1$ takes both signs while $I_2$ vanishes only at the quarter periods. The field is of the **generic electric–magnetic-parallel type**, not the null type: a solution of the source-free Maxwell equation that carries a **non-null** field. Second, the field is **not transverse**: in the moving member of the family below the propagation vector is no longer orthogonal to the field, in contrast to the plane wave. That is why its construction matters to claims about longitudinal electromagnetic waves, for which the source cites Evans. Third, $\vec W$ satisfies the **Beltrami (force-free) equation**

$$
\mathrm{rot}\,\vec W = -\Omega\,\vec W,
$$

so that the configuration is a helical force-free field, the object that appears in plasma physics and in the earlier "force-free" literature the source cites. The sign is convention-laden and worth one warning: the source's frame carries a raised index, so the minus in its (3.21) is its convention and not a dynamical statement. Checked in Cartesian components, the printed $\vec W$ returns $\mathrm{curl}\,\vec W=+\Omega\vec W$, and that is the Beltrami equation in the corpus's gradient, whose spatial part is the Cartesian $\nabla$. The energy integral of $F_0$ alone diverges, and the source notes that finite-energy wave packets over a distribution of frequencies can be formed instead.

### The moving subluminal solution

The stationary field is the $v=0$ member of a moving family. For the family the source takes the Hertz potential

$$
\pi_<=C\,\frac{\sin\Omega\zeta_<}{\zeta_<}\,\exp\!\left[\omega(\varpi r'_t-q r_z)\right]\vec e_x\vec e_y,
\qquad
\zeta_<^2=r_x^2+r_y^2+\frac{(r_z-vr'_t)^2}{1-v^2},
$$

with the frequency $\varpi$, the axial wavenumber $q$, and the **massive dispersion relation**

$$
\varpi^2-q^2=\Omega^2,\qquad v=\frac{d\varpi}{dq}.
$$

That relation is what the word "subluminal" means here. Since $\varpi^2-q^2>0$, the group velocity obeys $|d\varpi/dq|=|q|/\varpi<1$ and the envelope travels slower than light, while the phase velocity is faster than light, $\varpi/q=\sqrt{1+\Omega^2/q^2}>1$. The envelope is therefore subluminal while the carrier phase it modulates runs ahead of $c$. The source's three summary statements are then these: a subluminal solution obeys the massive dispersion relation; its invariants are non-null; and it is **not a transverse wave**, which the source verifies by applying a Lorentz transformation of parameter $v$ to the stationary field.

### Purely electromagnetic particles

The subluminal solutions bear on a question older than the formalism. Einstein, following Poincaré and Ehrenfest, asked whether a **purely electromagnetic particle** can exist: a field configuration $F_p$ with current $J_p$ obeying $\tilde\nabla\tilde F_p=\tilde J_{\Phi,p}$ — the source's own equation — and the subsidiary condition $J_p\cdot F_p=0$. The contraction $J_p\cdot F_p$ is a vector. With the field written $F_p=\vec E_p+\omega\vec B_p$ and the current split into charge density and spatial current, its vanishing has one time component and three spatial ones:

$$
J_p\cdot F_p=0
\quad\Longleftrightarrow\quad
\vec j_p\cdot\vec E_p=0,\qquad \rho_p\vec E_p+\vec j_p\times\vec B_p=0 .
$$

The condition therefore says two things: the current exchanges **no power** with the field, and it feels **no force**.

The source presents a stronger triple as what (3.24) implies, with the electric and the magnetic force densities set to zero **separately**,

$$
\rho_p\vec E_p=0,\qquad \vec j_p\cdot\vec E_p=0,\qquad \vec j_p\times\vec B_p=0,
$$

the first being the electric force density, the second the power density, and the third the magnetic force density on the current. The triple implies the pair above, but not conversely, so the source's implication runs the wrong way; the two forms coincide in each of the frames the argument goes on to use. For a **time-like** $J_p$ the frame is the rest frame, $\vec j_p=0$, where the condition reduces to $\rho_p\vec E_p=0$ and hence $\vec E_p=0$; then the time component of $\tilde\nabla\tilde F_p=\tilde J_{\Phi,p}$, which is $\operatorname{div}\vec E_p=\rho_p$, forces $\rho_p=0$. No time-like configuration survives, and that is Einstein's conclusion. What carries the argument is the rest-frame form, not the printed triple.

For a **space-like** $J_p$ there is a frame with $\rho_p=0$ and $\vec j_p\ne0$, and the condition reduces to the remaining two components. A current parallel to the magnetic field, $\vec j_p=kC\,\vec B_p$ with $k=\pm1$ a sign and $C$ real, satisfies both: $\vec j_p\times\vec B_p=0$ because $\vec B_p$ is parallel to itself, and $\vec j_p\cdot\vec E_p=0$ provided $\vec E_p\cdot\vec B_p=0$.

The connection with the subluminal family is that the free stationary field $F_0$ can be **split** as a field plus a current, $\tilde\nabla\tilde F_0=0$ being equivalent to $\tilde\nabla\tilde F_p=\tilde J_{\Phi,p}$ for a suitable space-like $J_p$; the free equation then models a standing purely electromagnetic particle. This is the source's route into the older programme of Waite, Barut and Zeni, which it cites; it is recorded here as a programme item, not as an established particle model.

## Superluminal Solutions: the X-Wave

The same Hertz-potential device produces **superluminal** solutions. The scalar seed is taken from the family of **X-waves**,

$$
Ξ_{X_n}(r'_t, r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) = \exp(in\theta)\int_0^\infty B(k)\,J_n(k\rho\sin\theta_{\mathrm{axc}})\,\exp(-k[a_0-i(r_z\cos\theta_{\mathrm{axc}}-r'_t)])\,dk,
$$

with $\theta_{\mathrm{axc}}$ the **axicon angle** and $J_n$ the Bessel function. With $B(k)=a_0$ the integral is elementary, and the source's closed form is

$$
Ξ_{XBB_n}=a_0\,\frac{(\rho\sin\theta_{\mathrm{axc}})^n e^{in\theta}}{\sqrt M\left(\tau+\sqrt M\right)^n},\qquad M=(\rho\sin\theta_{\mathrm{axc}})^2+\tau^2,\qquad \tau=a_0-i(r_z\cos\theta_{\mathrm{axc}}-r'_t).
$$

Used as the Hertz potential, this gives a **closed-form superluminal electromagnetic X-wave** (SEXW): a localised beam-like solution of the field equation in which $r_z\cos\theta_{\mathrm{axc}}-r'_t$ replaces the plane-wave phase, so that the pattern advances at speed $1/\cos\theta_{\mathrm{axc}}$ along the axis, faster than $c$. That is a pattern speed: the Bessel factor $J_n(k\rho\sin\theta_{\mathrm{axc}})$ is an azimuthal superposition of plane waves inclined at the axicon angle, and each of those still travels at $c$. The source treats these as valid solutions of the free Maxwell equation and points to Rodrigues and Lu for the physical devices that would generate them.

The superluminality must be read with the corpus's usual care, and the source's own phrasing invites the mistake. The X-wave is a **localised pattern** whose amplitude profile advances superluminally; this is the **pattern (or phase) speed** of a finite wave packet and is not a speed of energy, information or signal. A free-field solution with a superluminal pattern is not in conflict with causality, and the corpus records the claim in that sense only. The same construction yields **subluminal and superluminal** solutions of the Weyl equation, and the source remarks that these obey $p^2=\Omega^2>0$ and $p^2=-\Omega^2<0$ respectively — a massless equation producing a massive-looking dispersion — which it offers as a possible reading of the neutrino puzzles. That part is speculative and is not carried.

## The Field as a Spinor Bilinear

### Two constraints, six degrees of freedom

The structural heart of the paper is the representation of the field as a **spinor bilinear**. With $\tilde{Ξ}_{\mathrm{sp}}$ an element of $\mathbb{B}$ — a Dirac–Hestenes spinor in the source's terms — the field is written

$$
\boxed{\;F = -\tilde{Ξ}_{\mathrm{sp}}\,\vec e_z\,\tilde{Ξ}_{\mathrm{sp}}^{\natural}\;}
$$

where $\tilde{Ξ}_{\mathrm{sp}}^{\natural}$ is the **reverse** of $\tilde{Ξ}_{\mathrm{sp}}$: the corpus's natural conjugation $\natural$, which the source writes $\tilde{Ξ}_{\mathrm{sp}}$. The counting matters: a general $\tilde{Ξ}_{\mathrm{sp}}$ has **eight** real degrees of freedom, while the field $F$ has **six**, so two constraints must be imposed on $\tilde{Ξ}_{\mathrm{sp}}$ for the correspondence to be one-to-one up to a normalisation. The source chooses them as $\langle\tilde\nabla,\tilde j\rangle=0$ and $\langle\tilde\nabla,\tilde g\rangle=0$, where $j$ and $g$ are the vector and axial-vector currents it builds from the derivative of $\tilde{Ξ}_{\mathrm{sp}}$. This is the same eight-versus-six counting the corpus records in its Dirac–Hestenes article, which reaches it through the parameters of the rotor decomposition; the constraints are the source's extra data.

Substituting $F=-\tilde{Ξ}_{\mathrm{sp}}\vec e_z\tilde{Ξ}_{\mathrm{sp}}^{\natural}$ into the generalised Maxwell equation $\tilde\nabla\tilde F=\tilde J_{\Phi}$ — the source's own equation — and using the canonical decomposition $\tilde{Ξ}_{\mathrm{sp}}=\rho^{1/2}\exp(\omega\theta_{\mathrm{dua}}/2)R$ — the rotor $R$, the density $\rho$, and the **Takabayasi angle** $\theta_{\mathrm{dua}}$ — turns the field equation into a spinorial equation for $\tilde{Ξ}_{\mathrm{sp}}$, with two scalar coefficients:

$$
(\tilde\nabla\tilde{Ξ}_{\mathrm{sp}})(-\vec e_z)
=\left(\Lambda+\omega\,\mathcal{Q}_{\mathrm{sig}}\right)\tilde{Ξ}_{\mathrm{sp}}\,i\vec e_x\exp(\omega\theta_{\mathrm{dua}})
+\frac{1}{2\rho}\exp(\omega\theta_{\mathrm{dua}})J\,\tilde{Ξ}_{\mathrm{sp}} ,
$$

with $\Lambda=\Omega\cdot S$ and $\\mathcal{Q}_{\\mathrm{sig}}=\Omega\cdot(\omega S)$ built from the bivector $\Omega=\sum_\mu g_{\mu\mu}v_\mu\Omega_\mu$ and the spin bivector $S=-\tfrac12\tilde{Ξ}_{\mathrm{sp}}\vec e_z\tilde{Ξ}_{\mathrm{sp}}^{-1}=-\tfrac12R\vec e_zR^{-1}$, in which the phase cancels. The bivectors $\Omega_\mu$ are those of the rotor's derivative, $\partial \tilde{Ξ}_{\mathrm{sp}}/\partial x_\mu=\tfrac12(\partial/\partial x_\mu\ln\rho+\omega\,\partial \theta_{\mathrm{dua}}/\partial x_\mu+\Omega_\mu)\tilde{Ξ}_{\mathrm{sp}}$ with $\Omega_\mu=2(\partial R/\partial x_\mu)R^{-1}$, so $\Omega$ is the directional derivative of the rotor along the four-velocity. The source prints the two scalar terms separately; they are one, because both multiply the same product on the right, and they add into the single coefficient $\Lambda+\\omega\\,\\mathcal{Q}_{\\mathrm{sig}}$, a complex number in $\omega$.

The source also carries the pair $(\lambda,\kappa)$, with $\lambda=\Lambda\cos\theta_{\mathrm{dua}}+\\mathcal{Q}_{\\mathrm{sig}}\\sin\theta_{\mathrm{dua}}$ and $\kappa=\\mathcal{Q}_{\\mathrm{sig}}\\cos\theta_{\mathrm{dua}}-\Lambda\sin\theta_{\mathrm{dua}}$, and writes the same equation with it and no phase in front: the phase-free display is the same equation, because
$$
\lambda+\omega\kappa=\left(\Lambda+\omega\,\mathcal{Q}_{\mathrm{sig}}\right)\exp(-\omega\theta_{\mathrm{dua}}).
$$
Both spellings are used below; $(\\Lambda,\\mathcal{Q}_{\\mathrm{sig}})$ carries the geometry, since the two numbers are projections of $\Omega$ on the spin bivector, and $(\lambda,\kappa)$ is the pair that the free-field constraints act on.

The spin-plane factor needs a second look, because the source builds it as a product of two of its frame generators and the side is easy to mistake. Composed, that pair acts on the **left** by the fixed bivector $-\vec e_z$, that is $\tilde{Ξ}_{\mathrm{sp}}\mapsto-\vec e_z\tilde{Ξ}_{\mathrm{sp}}$. The equation applies the bivector on the **right**, $\tilde{Ξ}_{\mathrm{sp}}\mapsto-\tilde{Ξ}_{\mathrm{sp}}\vec e_z$, which is the volume element $\omega$ of the introduction. The two are different: one bivector on opposite sides, and only the right one is used below, because it is the one that anticommutes with $\vec e_x$.

The element $\omega$ carries the two signs of the phase against the algebra: it **commutes** with every function of itself, its half-rotation included, and it **anticommutes** with $\vec e_x$, because $\vec e_x\vec e_z=-\vec e_z\vec e_x$; the central $i$ passes through on both sides:

$$
\omega\,\vec e_x=-\vec e_x\,\omega .
$$

The free case $J=0$ is therefore

$$
(\tilde\nabla\tilde{Ξ}_{\mathrm{sp}})(-\vec e_z)=\left(\Lambda+\omega\,\mathcal{Q}_{\mathrm{sig}}\right)\tilde{Ξ}_{\mathrm{sp}}\,i\vec e_x\exp(\omega\theta_{\mathrm{dua}}),
$$

which has the shape of the Dirac–Hestenes equation but with a coefficient that is a **complex number in $\omega$** rather than a mass.

### Linearisation: the two Dirac equations

The equation above is non-linear because its coefficients depend on the field: $\Lambda$ and $\\mathcal{Q}_{\\mathrm{sig}}$ are built from the spin bivector $S$, which is a function of $\tilde{Ξ}_{\mathrm{sp}}$, and $\theta_{\mathrm{dua}}$ is a function of $x$ as well. Two steps reduce it, and they give the two displays of the same equation. A third condition is needed for the reduction to end in a **mass**, and it is stated separately below.

**The constraint step.** The currents are $j=\lambda\rho v$ and $g=\kappa\rho v$ with $v=J/\rho$ the four-velocity, so the two constraints read $\rho\dot\lambda+\lambda\,\langle\tilde\nabla,\tilde J_{\Phi}\rangle=0$ and $\rho\dot\kappa+\kappa\,\langle\tilde\nabla,\tilde J_{\Phi}\rangle=0$, the dot being the derivative along the velocity, $\dot\lambda$ the derivative of $\lambda$ along the velocity. Eliminating $\langle\tilde\nabla,\tilde J_{\Phi}\rangle$ between them leaves $\kappa\dot\lambda=\lambda\dot\kappa$, so the ratio of the coefficients is constant,
$$
\frac{\kappa}{\lambda}=-\tan\theta_{\mathrm{dua},0}
\qquad\Longleftrightarrow\qquad
\frac{K}{\Lambda}=\tan(\theta_{\mathrm{dua}}-\theta_{\mathrm{dua},0}),
$$
with $\theta_{\mathrm{dua},0}$ a constant. Since $\theta_{\mathrm{dua}}$ is the angle of the duality rotation that produced $F$, a further rotation by $\theta_{\mathrm{dua},0}$ shifts $\theta_{\mathrm{dua}}\mapsto\theta_{\mathrm{dua}}+\theta_{\mathrm{dua},0}$, so $\theta_{\mathrm{dua},0}=0$ may be chosen and
$$
\frac{K}{\Lambda}=\tan\theta_{\mathrm{dua}},\qquad
\lambda=\Lambda\cos\theta_{\mathrm{dua}}+\Lambda\tan\theta_{\mathrm{dua}}\sin\theta_{\mathrm{dua}}=\frac{\Lambda}{\cos\theta_{\mathrm{dua}}},\qquad
\kappa=\Lambda\tan\theta_{\mathrm{dua}}\cos\theta_{\mathrm{dua}}-\Lambda\sin\theta_{\mathrm{dua}}=0 .
$$
The $\omega$-part is gone and the coefficient is a real scalar. For the free field,
$$
\boxed{\;(\tilde\nabla\tilde{Ξ}_{\mathrm{sp}})(-\vec e_z)=\lambda\,\tilde{Ξ}_{\mathrm{sp}}\,i\vec e_x\;}
$$
which has the **shape** of the Dirac–Hestenes equation, with a single real coefficient $\lambda$ — in units of inverse length, since restoring $\frac{m\,c}{k_m}$ and $c$ gives $\lambda=k_m$. The coefficient has become real; whether it is a **mass** is the next question. In the unrotated pair the same coefficient reads $\Lambda+\omega\,\mathcal{Q}_{\mathrm{sig}}=\lambda\exp(\omega\theta_{\mathrm{dua}})$, the real coefficient times the duality phase, which is why the phase-carrying display and this one are one equation.

**The mass is a constant only for a conserved current.** Nothing so far makes $\lambda=\Lambda/\cos\theta_{\mathrm{dua}}$ constant, and neither factor need be. What the first constraint does give is $\rho\dot\lambda+\lambda\,\langle\tilde\nabla,\tilde J_{\Phi}\rangle=0$, so that

$$
\langle\tilde\nabla,\tilde J_{\Phi}\rangle=0\quad\Longleftrightarrow\quad \lambda=\text{const}.
$$

The source states it that way round: the current $J$ is not conserved unless $\lambda$ is constant, so it assumes $\langle\tilde\nabla,\tilde J_{\Phi}\rangle=0$ explicitly. That assumption is the third condition, and it is the one that turns a Dirac–Hestenes-shaped equation into a Dirac–Hestenes equation with a mass. Without it the display above is exact but its coefficient drifts from point to point.

**The rescaling step.** The same content reads as a statement about the spinor. Put $\tilde{Ξ}_{\mathrm{sp}}=\xi\exp(\omega\theta_{\mathrm{dua}}/2)$ with $\xi=\sqrt\rho\,R$ and $\theta_{\mathrm{dua}}$ constant. The rotation $\exp(\omega\theta_{\mathrm{dua}}/2)$ does not depend on $x$, so it passes through the derivative on the left side, and the anticommutation with $i\vec e_x$ merges the two phases on the right side into the same half rotation:
$$
(\tilde\nabla\tilde{Ξ}_{\mathrm{sp}})(-\vec e_z)=(\tilde\nabla\xi)(-\vec e_z)\exp(\omega\theta_{\mathrm{dua}}/2),
$$
$$
\left(\Lambda+\omega\,\mathcal{Q}_{\mathrm{sig}}\right)\tilde{Ξ}_{\mathrm{sp}}\,i\vec e_x\exp(\omega\theta_{\mathrm{dua}})
=\left(\Lambda+\omega\,\mathcal{Q}_{\mathrm{sig}}\right)\xi\,i\vec e_x\exp(\omega\theta_{\mathrm{dua}}/2).
$$
The common right factor cancels — it is the **last** factor on both sides, and it is invertible — leaving the same equation with the phase gone,

$$
(\tilde\nabla\xi)(-\vec e_z)=\lambda\,\xi\,i\vec e_x,
$$

with $\Lambda$ and $\\mathcal{Q}_{\\mathrm{sig}}$ unchanged, since the phase cancels in the spin bivector. A constant angle is thus not a parameter of the dynamics but a phase carried by the spinor, and solutions with different constant $\theta_{\mathrm{dua}}$ are the same solution multiplied on the right.

The half angle is not a convention. The source prints the full one in one place, where its (5.15) is said to follow from $\tilde{Ξ}_{\mathrm{sp}}=\xi\exp(\theta_{\mathrm{dua}}\omega)$. With that exponent the phase does not cancel: the left side of the source's (5.7) carries one power of it, the right side none. The reason is that on the right the phase enters twice — once from $\tilde{Ξ}_{\mathrm{sp}}$ and once from the equation itself — and the two annihilate after the inner one passes the odd factor, $\exp(\omega\theta_{\mathrm{dua}})\,i\vec e_x=i\vec e_x\exp(-\omega\theta_{\mathrm{dua}})$. What follows with the full exponent is $(\tilde\nabla\xi)(-\vec e_z)=m\xi\,i\vec e_x\exp(-\omega\theta_{\mathrm{dua}})$, with the phase moved to the other side rather than removed. The rest of the paper uses the half angle: the solutions (5.16) and (5.17) carry $\exp(\theta_{\mathrm{dua}}\omega/2)$, and the mass-spectrum decomposition (6.6) is $\tilde{Ξ}_{\mathrm{sp}}=\exp(\omega\theta_{\mathrm{dua}}/2)\xi$.

**The narrower case $J=0$, $K=0$.** With the constraints imposed the two displays are one equation, the coefficient $\Lambda+\omega\,\mathcal{Q}_{\mathrm{sig}}=\lambda\exp(\omega\theta_{\mathrm{dua}})$ being the real coefficient times the phase. The source also studies this narrower case, where the coefficient is $\Lambda$ alone and the phase stands in front; it notes that this form was studied extensively by Daviau. It is non-linear as it stands, it reduces to the Dirac–Hestenes equation by the rescaling above at every constant $\theta_{\mathrm{dua}}$, and it is *identical* to that equation only at $\theta_{\mathrm{dua}}=0$ and $\theta_{\mathrm{dua}}=\pi$ — the two angles the source assigns to the electron and the positron, through the family of the next section.

The plane-wave solutions of *The Dirac Equation in Biquaternionic Form* have a constant spinor coefficient, so their $\theta_{\mathrm{dua}}$ is constant, and *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form* calls $\theta_{\mathrm{dua}}=0$ the pure electron state. They therefore sit on this linearisable class, and the source supplies the general reason why.

Two consequences the source draws from the same algebra are worth recording. The first is a **superselection rule**: the superposition principle survives only for spinors of the same $\theta_{\mathrm{dua}}$, because the coefficients depend on that angle, so a sum of solutions with different angles is not a solution; the source reads this as particles and antiparticles forming separate superselection sectors. The second is the **momentum relation**. Multiplying the non-linear equation by $\tilde{Ξ}_{\mathrm{sp}}^{-1}$ gives $p=mv$ for every angle $\theta_{\mathrm{dua}}$, whereas the linear Dirac–Hestenes equation gives $p=\exp(\omega\theta_{\mathrm{dua}})mv$, which for $p$ and $v$ real forces $\theta_{\mathrm{dua}}=0$ or $\theta_{\mathrm{dua}}=\pi$ and thus the choice between positive and negative energy. In the non-linear interpretation there is no negative-energy problem to interpret: the equation gives $p=mv$ throughout, and the source proposes to reinterpret the energy projector as a **particle projector** instead.

The **Tetrode tensor** is what backs that reinterpretation. Its trace for the non-linear equation is

$$
T=m\,\bigl\langle\tilde{Ξ}_{\mathrm{sp}}\,\tilde{Ξ}_{\mathrm{sp}}^{\natural}\exp(-\omega\theta_{\mathrm{dua}})\bigr\rangle_0=m\rho ,
$$

positive for every solution, so every solution has positive energy; the linear equation gives $T_{\mathrm{Dirac}}=m\rho\cos\theta_{\mathrm{dua}}$, and the two differ by the factor $\cos\theta_{\mathrm{dua}}$, coinciding only at the two endpoints. The source adds one structural remark that the corpus records as a curiosity: the Tetrode energy–momentum one-form is a kind of **square root** of the Maxwell energy–momentum one-form $S_\mu=\tfrac12\,i\,Fe_\mu F\vec e_{\nu(\mu)}$. The overall sign is not fixed by the print: a 2-form reverses to minus itself, $\tilde F=-F$, so the same object written with the reverse in the middle differs only in that sign.

Here $e_\mu$ and $\vec e_{\nu(\mu)}$ are the unit of the coordinate $x_\mu$ and its partner, with $\nu(t)=x$ and $\nu(k)=y$, and the two act on the middle factor of $F$.

### The projection operators

The family that carries the mass spectrum is a family of projections on the algebra, and it is stated precisely here, including the one printed relation that cannot hold.

**The pair.** The source builds it from the **conjugation** by its time vector, which in the algebra is the element $i\vec e_x$: an element $\tilde{Ξ}_{\mathrm{sp}}$ is carried to $i\vec e_x\,\tilde{Ξ}_{\mathrm{sp}}\,i\vec e_x$. The two members of the pair are the two values

$$
\tilde{Ξ}_{\mathrm{sp},+}=\tfrac12\left(\tilde{Ξ}_{\mathrm{sp}}+i\vec e_x\,\tilde{Ξ}_{\mathrm{sp}}\,i\vec e_x\right),\qquad
\tilde{Ξ}_{\mathrm{sp},-}=\tfrac12\left(\tilde{Ξ}_{\mathrm{sp}}-i\vec e_x\,\tilde{Ξ}_{\mathrm{sp}}\,i\vec e_x\right),
$$

so that $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},+}+\tilde{Ξ}_{\mathrm{sp},-}$ is the same element written as their sum. The conjugating element squares to $+e_t$, $(i\vec e_x)^2=i^2\vec e_x^2=(-1)(-1)=+1$ by the sign rule of the introduction, so conjugating twice returns every element,

$$
i\vec e_x\left(i\vec e_x\,\tilde{Ξ}_{\mathrm{sp}}\,i\vec e_x\right)i\vec e_x=\tilde{Ξ}_{\mathrm{sp}} .
$$

Two consequences follow, one line each. The conjugated value of $\tilde{Ξ}_{\mathrm{sp},+}$ is $+\tilde{Ξ}_{\mathrm{sp},+}$ and that of $\tilde{Ξ}_{\mathrm{sp},-}$ is $-\tilde{Ξ}_{\mathrm{sp},-}$,

$$
i\vec e_x\,\tilde{Ξ}_{\mathrm{sp},+}\,i\vec e_x=+\tilde{Ξ}_{\mathrm{sp},+},\qquad i\vec e_x\,\tilde{Ξ}_{\mathrm{sp},-}\,i\vec e_x=-\tilde{Ξ}_{\mathrm{sp},-} ,
$$

and each of the two values is fixed by its own map and annihilated by the other, because the second term of the map then reproduces the first term or cancels it.

**The conjugation is not the identity, and it is not an idempotent.** It takes both values on the algebra, each on four of the eight real dimensions, so the pair splits the algebra into two fours. The corpus's Dirac–Hestenes article splits the same algebra by an **idempotent applied on one side**, an idempotent built from a unit that article declares; that is a different split. The source uses no idempotent here, and the element it conjugates by is the time vector of its own frame.

**The one-parameter family.** The family is the same projection seen from a duality-rotated frame. With the volume element $\omega$,

$$
\tilde{Ξ}_{\mathrm{sp},\mathrm{dua},\theta}=\tfrac12\left(\tilde{Ξ}_{\mathrm{sp}}+\exp(\omega\theta_{\mathrm{dua}})\,i\vec e_x\,\tilde{Ξ}_{\mathrm{sp}}\,i\vec e_x\right)
=\exp\!\left(\tfrac{\omega\theta_{\mathrm{dua}}}{2}\right)\tfrac12\left(\zeta+i\vec e_x\,\zeta\,i\vec e_x\right),
\qquad
\zeta=\exp\!\left(-\tfrac{\omega\theta_{\mathrm{dua}}}{2}\right)\tilde{Ξ}_{\mathrm{sp}} ,
$$

that is, rotate the element, project it, rotate the result back. The right-hand display holds for two reasons. The inner half phase passes the conjugating element with a change of sign,

$$
\exp\!\left(-\tfrac{\omega\theta_{\mathrm{dua}}}{2}\right)i\vec e_x=i\vec e_x\exp\!\left(\tfrac{\omega\theta_{\mathrm{dua}}}{2}\right),
$$

because $\omega$ anticommutes with $\vec e_x$; and the two half phases add into the full $\exp(\omega\theta_{\mathrm{dua}})$, both being powers of the one element $\omega$. That is the source's (5.28) as printed.

**The family projects for every $\theta_{\mathrm{dua}}$.** The conjugating element of the family is $\\mathcal{Q}_{\\mathrm{sig}}=\exp(\omega\theta_{\mathrm{dua}})\,i\vec e_x$, and

$$
K^2=\exp(\omega\theta_{\mathrm{dua}})\,i\vec e_x\,\exp(\omega\theta_{\mathrm{dua}})\,i\vec e_x=(i\vec e_x)^2=+1 .
$$

The inner $\exp(\omega\theta_{\mathrm{dua}})$ passes $\vec e_x$ with a change of sign and cancels the outer one. So conjugating twice by $\\mathcal{Q}_{\\mathrm{sig}}$ returns every element, and every member of the family is a projection, not only the two ends.

The list the source prints is then read on the values. The value at $\theta_{\mathrm{dua}}$ put through the map at $\theta_{\mathrm{dua}}$ again is the same value; the map at $\theta_{\mathrm{dua}}+\pi$ complements it, so $\tilde{Ξ}_{\mathrm{sp},\mathrm{dua},\theta}+\tilde{Ξ}_{\mathrm{sp},\theta_{\mathrm{dua}}+\pi}=\tilde{Ξ}_{\mathrm{sp}}$ and the map at $\theta_{\mathrm{dua}}+\pi$ applied to $\tilde{Ξ}_{\mathrm{sp},\mathrm{dua},\theta}$ gives zero; and $\tilde{Ξ}_{\mathrm{sp},\mathrm{dua},\theta}$ is $\tilde{Ξ}_{\mathrm{sp},+}$ for every element only at $\theta_{\mathrm{dua}}\equiv0$ modulo $2\pi$. On the two values of the split the family reads

$$
\tilde{Ξ}_{\mathrm{sp},+}\longmapsto\cos\tfrac{\theta_{\mathrm{dua}}}{2}\,\exp\!\left(\tfrac{\omega\theta_{\mathrm{dua}}}{2}\right)\tilde{Ξ}_{\mathrm{sp},+},\qquad
\tilde{Ξ}_{\mathrm{sp},-}\longmapsto-\omega\sin\tfrac{\theta_{\mathrm{dua}}}{2}\,\exp\!\left(\tfrac{\omega\theta_{\mathrm{dua}}}{2}\right)\tilde{Ξ}_{\mathrm{sp},-},
$$

which is where the cosine and sine weights of the family come from, and it is why the family returns $\tilde{Ξ}_{\mathrm{sp},\pm}$ to itself only at the endpoints: at $\theta_{\mathrm{dua}}=\pi$ the second line returns $\tilde{Ξ}_{\mathrm{sp},-}$, because $\exp(\omega\pi/2)=\omega$ and $\omega^2=-1$.

**The printed relation that cannot hold is the middle one of the three.** The source lists that the family is a projection, that the angle $\theta_{\mathrm{dua}}+\pi$ gives the same map as $\theta_{\mathrm{dua}}$, and that the two maps at $\theta_{\mathrm{dua}}$ and $\theta_{\mathrm{dua}}+\pi$ have zero product. The first two make the third say that the value at $\theta_{\mathrm{dua}}$ is zero for every element, which no projection gives. The relation that holds, and the one the printed line must be a slip for, is the sum

$$
\tilde{Ξ}_{\mathrm{sp},\mathrm{dua},\theta}+\tilde{Ξ}_{\mathrm{sp},\theta_{\mathrm{dua}}+\pi}=\tilde{Ξ}_{\mathrm{sp}} .
$$

That is the correction the corpus records: the printed $=$ is missing a $+$ and a $\tilde{Ξ}_{\mathrm{sp}}$.

## The Lepton Mass Spectrum

The family of the previous section is introduced for the mass spectrum, and the construction is short. The **electron** is the free field, $\tilde\nabla\tilde F_e=0$ with $F_e^2\ne0$, written $F_e=-\tilde{Ξ}_{\mathrm{sp},e}\vec e_z\tilde{Ξ}_{\mathrm{sp},e}^{\natural}$; by the linearisation above, $\tilde{Ξ}_{\mathrm{sp},e}$ obeys the Dirac–Hestenes equation with the electron mass at $\theta_{\mathrm{dua}}=0$, and the positron sits at $\theta_{\mathrm{dua}}=\pi$. The source prints the spin plane in both terms of its (6.2); as printed that equation puts the spin plane on both terms and is not a Dirac–Hestenes equation; the mass term must carry the time vector, as in the linearised form above. The **muon** is taken to be that free field **plus the field of the $+$ branch**, $F=F_e+F_+$ — the field of a massless spinor with a magnetic current, the object of the next section.

The magnetic current re-enters the sourced spinorial equation, and for the phase-free spinor the equation keeps the Dirac form with two coefficients — masses in inverse-length units, hence the $\frac{k_m}{m}$:

$$
(\tilde\nabla\xi)(-\vec e_z)=\frac{k_m\,M}{m}\,\xi\,i\vec e_x+\frac{k_m\,\omega\,N}{m}\,\xi\,i\vec e_x,
\qquad
M=m+3m\,\frac{q_{\mathrm{m}}}{e}\sin\theta_{\mathrm{dua}},\qquad
N=-3m\,\frac{q_{\mathrm{m}}}{e}\cos\theta_{\mathrm{dua}} ,
$$

with $q_{\mathrm{m}}$ the magnetic charge. The $3$ carries the normalisation, and the source does not display the step: it fixes $F=-k\,(\frac{e}{k_m})\,\tilde{Ξ}_{\mathrm{sp}}\vec e_z\tilde{Ξ}_{\mathrm{sp}}^{\natural}$ with $k=2\pi/3$ and states only that (6.5) follows "as in section 4". The natural reading is the Gaussian $4\pi/c$ on the current, with the $\tfrac12$ of the spinorial Maxwell equation, against $k$: $4\pi/(2k)=3$. That reconstruction is not printed, so the coefficient stands or falls with (6.5) as it appears. What $k$ does **not** do is fix the dimensions — $[F]=QL^{-2}$ and $[\frac{e}{k_m}]=QL$ already force $[\tilde{Ξ}_{\mathrm{sp}}]=L^{-3/2}$ — so its value is chosen for the spectrum. The equation is a Dirac–Hestenes equation exactly when $N=0$, that is at $\theta_{\mathrm{dua}}=\pi/2$ and $\theta_{\mathrm{dua}}=3\pi/2$ — the two angles of the family that the source assigns to the muon and the antimuon. Then $M=m+3mq_{\mathrm{m}}/e$, and the Dirac quantisation condition for a monopole, $\frac{k_m\,eq_{\mathrm{m}}}{m\,c^{2}}=n/2$, gives $q_{\mathrm{m}}=en/2\alpha$ with $\alpha=\frac{k_m\,e^{2}}{m\,c^{2}}$ the fine-structure constant, so

$$
M=m\left(1+\frac{3n}{2\alpha}\right),\qquad n=1:\quad M=206.55\,m_e=105.5\ \mathrm{MeV},
$$

against the measured $105.66$ MeV.

The status of the numbers is the point. Nothing in the algebra fixes $n=1$; the source takes it, and the muon mass follows. The **tau** needs a further hypothesis, which the source states as such: that it is an excited state of the muon carrying $16=2^4$ further units of magnetic charge — the hypothesis $n=p^4$ at $p=2$. The units add to the muon's one, so the total is $17$ and not $16$,

$$
M_\tau=m+\frac{3}{2\alpha}m\left(1+16\right)=m\left(1+17\cdot\frac{3}{2\alpha}\right)=3495\,m_e,
$$

which is $1786$ MeV at $m_ec^2=0.511$ MeV — the source prints $1785$ — against the measured $1777$. The distinction matters arithmetically: $16$ units alone give $3290\,m_e=1681$ MeV, which is not the tau.

Beyond the tau the pattern is a proposal, not a derivation, and its arithmetic does not close. The source states the spectrum as

$$
M_p=m+\frac{3}{2\alpha}m\sum_{l=0}^{p}4^l
$$

and reads off $M_0=m$, $M_1=m_\mu$, $M_2=m_\tau$, $M_3=20090\,m_e=10291$ MeV. The formula gives none of those numbers. What reproduces the tau is the **last term alone**, $1+4^p$ at $p=2$, which is the $1+16$ of the tau paragraph above; $1+4^p$ and the sum coincide only at $p=1$:

| $p$ | printed | $\sum_{l=0}^{p}4^l$ | from the sum | $1+4^p$ | from the last term |
|---|---|---|---|---|---|
| 0 | $m_e$ | $1$ | $206.55\,m_e$ | $2$ | $412\,m_e$ |
| 1 | $206.55\,m_e$ | $5$ | $1029\,m_e$ | $5$ | $1029\,m_e$ |
| 2 | $3495\,m_e$ | $21$ | $4318\,m_e$ | $17$ | $3495\,m_e$ |
| 3 | $20090\,m_e$ | $85$ | $17473\,m_e$ | $65$ | $13362\,m_e$ |

Neither column matches the print. The **sum** shifts the whole sequence by one: it gives the muon where the print gives the electron, so $M_0\ne m$ and every later entry is one step ahead. The **last term** is right at the tau and wrong everywhere else, offering $412\,m_e=211$ MeV and $1029\,m_e=526$ MeV as leptons at $p=0$ and $p=1$, and $13362\,m_e=6828$ MeV at $p=3$. The muon's own number comes from the **separate** formula $M=m(1+3n/2\alpha)$ at $n=1$, and the tau's from the last term at $p=2$; no single reading of (6.24) gives both.

Two entries of the table are unreadable rather than wrong, and the table carries the corrected values. The scan shows the tau coefficient as $3845\,m_e$, where $1+17\cdot\frac{3}{2\alpha}=3495\,m_e$; the $1785$ MeV printed beside it belongs to $3495\,m_e$, while $3845\,m_e$ is $1965$ MeV, so a digit has slipped between the two numbers and $3495$ is the intended coefficient. The $M_3$ entry, $20090\,m_e$, is $10266$ MeV at $m_ec^2=0.511$ MeV, not the $10291$ MeV printed beside it — the two entries would need different electron rest energies to agree with their own MeV figures. What the table above rests on is the **formula** rather than the digits, and the formula does not reproduce the sequence it is said to give. The hypothesis itself is called ad hoc in the paper.

## Maxwell and the Massless Dirac Equation

The equivalence runs in the other direction as well, and that direction carries the axial current. The **massless** Dirac equation $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}=0$ for an element $\tilde{Ξ}_{\mathrm{sp}}$ of $\mathbb{B}$ is equivalent to a **generalised Maxwell equation**, $\tilde\nabla\tilde F=\tilde J_{\Phi}$ with the current written out:

$$
\tilde\nabla\tilde F = \tilde J_{\Phi,\mathrm{e}} - \omega \tilde J_{\Phi,\mathrm{m}} = \tilde J_{\Phi} ,
$$

with both an electric current $J_{\mathrm{e}}$ and an **axial (magnetic) current** $-\omega J_{\mathrm{m}}$. For $\tilde{Ξ}_{\mathrm{sp},+}$, the $+$ branch of the split by $i\vec e_x$, the electric current vanishes, $j_{\mathrm{e}}=0$, and the equivalent Maxwell equation reads

$$
\boxed{\;\tilde\nabla\tilde F_+ = -\omega\tilde J_{\Phi,\mathrm{m}}\;}
$$

that is, a **massless Dirac field is a Maxwell field with a magnetic current and no electric current**. The current is not external. It is read off the spinor's own components: writing the $L$ value of the $+$ branch as $s+F-\omega p$, with $s$ and $p$ real and $F$ the field bivector, the source finds $\tilde\nabla\tilde F_+=-\omega\,\tilde\nabla p$, so $J_{\mathrm{m}}=\tilde\nabla p$ and the Maxwell equation is **self-sourced**. The mechanism is the split by $i\vec e_x$: the source shows that $\tilde{Ξ}_{\mathrm{sp},+}$ decouples into a pair of Weyl fields of opposite charge, $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},+R}+g\omega B\tilde{Ξ}_{\mathrm{sp},+R}=0$ and $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},+L}-g\omega B\tilde{Ξ}_{\mathrm{sp},+L}=0$ — the spin-plane factor absorbed in each by the Weyl condition, and the subscript naming the value, $L$ the minus value and $R$ the plus one — so that a single $\tilde{Ξ}_{\mathrm{sp},+}$ coupled to a potential carries a particle of charge $+g$ and a particle of charge $-g$ at once. This is a further route in the corpus by which a magnetic current appears in a spinorial or quaternionic reformulation of Maxwell's equations.

### One Dirac Equation or Two

The corpus has two spellings of the massive Dirac equation, and the source's equation is the second of them.

**The one-sided pair.** Two equations, one per value of the subscript, both gradients acting from the left:

$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=\frac{k_m}{\tilde{Ξ}_{\mathrm{sp},L}}$$

$$
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=\frac{k_m}{\tilde{Ξ}_{\mathrm{sp},R}}.
$$

The second gradient is the quaternion conjugate of the first, and it is the conjugation, not a side, that distinguishes them. The mass is the only term that couples the two values, and at $m=0$ the pair splits into $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=0$ and $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=0$, one Weyl equation per value.

**The two-sided single equation.** The same physics has a representation on the whole algebra, as one equation for one field:

$$
\tilde\nabla^{\natural}F=m\,\bar F\,i\omega ,
$$

with the derivative on the left and the mass on the right through the element $i\omega=-i\vec e_z$ that exchanges the two values, applied to the coefficient conjugate $\bar F$. The pair is the definition; the two-sided form is the representation in which the mass is a right multiplication, and it is antilinear in that term.

**The source's equation has that shape.** Its Dirac–Hestenes equation

$$
(\tilde\nabla\tilde{Ξ}_{\mathrm{sp}})(-\vec e_z)=\frac{k_m}{\tilde{Ξ}_{\mathrm{sp}}\,i\,\vec e_{x}}$$

acts with the derivative on the left and multiplies on the right by the fixed bivector and by the mass — a left action and two right factors, no second field. That is the shape of the corpus's own Dirac–Hestenes equation too, in which the mass also multiplies on the right, at a fixed bivector; the pair of values is a different spelling of the same physics, and the two-sided form is the one both the corpus's equation and the source's take. What it does not have is a second equation for the other value. The two values are the two halves of the one spinor under the source's **Weyl conditions**, which pair the volume element on one side with the fixed bivector on the other. Written as a condition on the one spinor it is $\tilde{Ξ}_{\mathrm{sp},L}\omega=-\omega\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde{Ξ}_{\mathrm{sp},R}\omega=+\omega\tilde{Ξ}_{\mathrm{sp},R}$, that is $\tilde{Ξ}_{\mathrm{sp},L}\vec e_z=-\vec e_z\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde{Ξ}_{\mathrm{sp},R}\vec e_z=+\vec e_z\tilde{Ξ}_{\mathrm{sp},R}$: the bivector enters twice, once as a product on the right and once as a product on the left. The condition is therefore a genuine constraint, and its two branches are the two four-dimensional halves of the algebra — the spinor commuting with $\vec e_z$ and the one anticommuting. What effects the split is the **pseudoscalar**, not a second field; and because in this frame the volume element and the spin plane are written with the one bivector, the source needs the single symbol $i$ for both jobs. The symbols are those of *Special Element Conventions*.

**Where the two presentations diverge.** They agree at $m=0$, each giving Weyl equations, and part ways once a mass is present. The corpus's mass couples the two values, in two fields, and is antilinear; the source's mass is linear and multiplies the one spinor on the right by a fixed element with a scalar coefficient. That is why the coefficient of the sourced equation is a complex number in $\omega$ rather than a real mass — a mass times a duality phase — and why its linearisation needs both of the steps of *Linearisation* above: the constraints, which turn the imaginary part into a pure phase, and the rescaling, which removes it.

## Status, Contrasts, and Boundaries

What the programme establishes is the **structural half**. That the free Maxwell equation has solutions with non-null invariants is true and is a genuine correction to the reflex that "free electromagnetic waves are null transverse plane waves"; the classification of *The Field-Strength Biquaternion and Its Invariants* admits such fields but does not exhibit them, and the subluminal construction here supplies the missing example. That the field is a spinor bilinear and that the Maxwell equation for the field is a non-linear Dirac–Hestenes equation which linearises, under its two constraints, to a single real coefficient — and to one real mass once the current is conserved — is likewise a clean structural statement, and it explains from a second direction why the corpus's plane-wave Dirac solutions are simple. That the massless Dirac equation is a Maxwell equation with an axial current is the third, and it reproduces the corpus's axial-current form.

The boundaries are these. The source's route through the bundle of forms is an **external formalism**; the corpus's own treatment is the biquaternion one, and the two are related through the dictionary between the forms and the algebra rather than identified. The "superluminal" of the X-wave is a pattern speed of a localised solution, not a signalling speed, and must not be read otherwise. The **purely electromagnetic particle** is a programme item revived from Einstein and Waite, not a constructed particle. The **mass spectrum** is a proposal, not a derivation. The muon comes out of one algebra with the monopole quantum number $n=1$; nothing in the algebra fixes that number; the tau needs a further hypothesis on it; and the arithmetic of the states beyond the muon, as the mass-spectrum section shows, does not close.

## Summary

The programme of Rodrigues and Vaz works in a bundle of differential forms and presses the free Maxwell equation $\tilde\nabla\tilde F=0$ in two directions. It exhibits **subluminal and superluminal undistorted progressive wave solutions with non-null invariants and longitudinal components**, built from a Hertz potential and a spherical Helmholtz solution, and connects the free stationary solution to the old question of purely electromagnetic particles. It represents the field as the **spinor bilinear** $F=-\tilde{Ξ}_{\mathrm{sp}}\vec e_z\tilde{Ξ}_{\mathrm{sp}}^{\natural}$ and shows the Maxwell equation to be a **non-linear Dirac–Hestenes equation**, with the **Takabayasi angle** as the knob: the two constraints collapse its two coefficients into a single real one for every $\theta_{\mathrm{dua}}$, a conserved current makes that coefficient the mass, and $0$ and $\pi$ then give the electron and the positron, while $\pi/2$ and $3\pi/2$ make it the muon and the antimuon once a magnetic current is added, with $M=m(1+3n/2\alpha)$ at $n=1$. In the other direction the **massless Dirac equation is a Maxwell equation with an axial (magnetic) current**, which is the route by which a magnetic current appears.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra, of which the field and the spinor are elements |
| $\varepsilon=(1,-1,-1,-1)$ | sign vector of the layer |
| $\omega=-\vec e_z$ | Volume element, the pseudoscalar; $\omega^2=-e_t$; the source's "$i$", its duality generator, not the corpus's central $i$ |
| $-\vec e_z$ | Fixed spin-plane bivector; as the element $\omega$ it multiplies the spinor on the right |
| $\tilde\nabla$ | The biquaternionic gradient, $e_t\partial/\partial R_t+\vec e_x\partial/\partial R_x+\vec e_y\partial/\partial R_y+\vec e_z\partial/\partial R_z$; an element with derivative coefficients, acting on the left |
| $\tilde\nabla^{\natural}$, $\Box$ | The quaternion conjugate, $\sum_\mu\varepsilon_\mu e_\mu\partial/\partial R_\mu$, and the d'Alembertian $\Box=\tilde\nabla\tilde\nabla^{\natural}=\Delta-\partial^2/\partial{r'_{t}}^2$ |
| $\tilde F$, $\tilde F_0$, $\tilde F_e$, $\tilde F_+$ | Field biquaternion; the stationary subluminal solution; the electron field; the field of the $+$ branch |
| $\pi$, $A$ | Hertz potential; vector potential, $A=-\delta\pi$ |
| $f$, $k$, $x$ | Constant 2-form; propagation vector ($k^2=0$); position |
| $\vec E_0,\vec B_0,\vec W$ | Fields of the stationary solution and their common vector, $\mathrm{curl}\,\vec W=+\Omega\vec W$ in the corpus's gradient |
| $\Omega$ | Intrinsic frequency of the subluminal solution ($\Omega$ in the Helmholtz equation $\nabla^2\xi+\Omega^2\xi=0$); the letter is reused, as in the source, for the bivector $\Omega=\sum_\mu g_{\mu\mu}v_\mu\Omega_\mu$ of the spinorial section |
| $\varpi,\ q,\ \zeta_<$ | Frequency and axial wavenumber of the moving subluminal solution, with $\varpi^2-q^2=\Omega^2$ and group velocity $v=d\varpi/dq$; $\zeta_<$ is its oblate radial coordinate |
| $Ξ_{X_n},\ Ξ_{XBB_n}$ | Scalar X-wave seed and its closed form, with $\theta_{\mathrm{axc}}$ the axicon angle and $a_0$ the constant that regularises the seed |
| $\tilde{Ξ}_{\mathrm{sp}}$, $\tilde{Ξ}_{\mathrm{sp}}^{\natural}$ | The spinor, an element of $\mathbb{B}$, and its reverse, the corpus's $\natural$ conjugation; the source writes the reverse $\tilde{Ξ}_{\mathrm{sp}}$ |
| $\tilde{Ξ}_{\mathrm{sp},\pm}$ | The two values of the split by $i\vec e_x$, $i\vec e_x\,\tilde{Ξ}_{\mathrm{sp},\pm}\,i\vec e_x=\pm\tilde{Ξ}_{\mathrm{sp},\pm}$, with $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},+}+\tilde{Ξ}_{\mathrm{sp},-}$ |
| $\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{Ξ}_{\mathrm{sp},R}$ | The two values of the subscript, $L$ the minus value and $R$ the plus one; $\tilde{Ξ}_{\mathrm{sp},+L}$ and $\tilde{Ξ}_{\mathrm{sp},+R}$ are the two values of the $+$ branch |
| $\tilde{Ξ}_{\mathrm{sp}}=\rho^{1/2}\exp(\omega\theta_{\mathrm{dua}}/2)R$ | Canonical decomposition: rotor $R$, density $\rho$, angle $\theta_{\mathrm{dua}}$; the letter $\rho$ is reused in the X-wave for the cylindrical radius |
| $\theta_{\mathrm{dua}}$ | Takabayasi (Yvon–Takabayasi) angle; $0,\pi$ electron/positron, $\pi/2,3\pi/2$ muon/antimuon |
| $\xi$ | Spinor with the phase divided out, $\tilde{Ξ}_{\mathrm{sp}}=\xi\exp(\omega\theta_{\mathrm{dua}}/2)$; the linear Dirac equation is for $\xi$ |
| $m$, $M$, $N$ | Electron mass; the two coefficients of the sourced equation, $M=m+3mq_{\mathrm{m}}\sin\theta_{\mathrm{dua}}/e$ and $N=-3mq_{\mathrm{m}}\cos\theta_{\mathrm{dua}}/e$, the second vanishing at $\theta_{\mathrm{dua}}=\pi/2$ and $3\pi/2$; the letter $M$ is reused, as in the source, for the radial factor of the X-wave |
| $q_{\mathrm{m}}$, $\alpha$ | Magnetic charge, $q_{\mathrm{m}}=en/2\alpha$ from the Dirac quantisation condition $\frac{k_m\,eq_{\mathrm{m}}}{m\,c^{2}}=n/2$; $\alpha=\frac{k_m\,e^{2}}{m\,c^{2}}$ the fine-structure constant |
| $j$, $g$, $J=J_{\mathrm{e}}-\omega J_{\mathrm{m}}$ | Vector current, axial current, total current with electric and magnetic parts; the contractions $\langle\tilde\nabla,\tilde j\rangle$ and $\langle\tilde\nabla,\tilde g\rangle$ are the series' contractions of the gradient with the two currents |
| $\tilde{Ξ}_{\mathrm{sp},\mathrm{dua},\theta}$ | The family of the source, $\tfrac12(\tilde{Ξ}_{\mathrm{sp}}+e^{\omega\theta_{\mathrm{dua}}}i\vec e_x\,\tilde{Ξ}_{\mathrm{sp}}\,i\vec e_x)$, which is the projection at $\theta_{\mathrm{dua}}$ in a duality-rotated frame; $\tilde{Ξ}_{\mathrm{sp},\mathrm{dua},\theta}+\tilde{Ξ}_{\mathrm{sp},\theta_{\mathrm{dua}}+\pi}=\tilde{Ξ}_{\mathrm{sp}}$ replaces the printed $\Lambda_{\mathrm{dua},\theta}=\Lambda_{\theta_{\mathrm{dua}}+\pi}$ |
| $S=-\tfrac12\tilde{Ξ}_{\mathrm{sp}}\vec e_z\tilde{Ξ}_{\mathrm{sp}}^{-1}$ | Bivector of the canonical analysis; $S_\mu=\tfrac12\,i\,Fe_\mu F\vec e_{\nu(\mu)}$ the Maxwell energy–momentum one-form, $e_\mu$ the unit of the coordinate $x_\mu$ |
| $\\Lambda,\\ \\mathcal{Q}_{\\mathrm{sig}}$ | The two scalars of the spinorial Maxwell equation, $\Lambda=\Omega\cdot S$ and $\\mathcal{Q}_{\\mathrm{sig}}=\Omega\cdot(\omega S)$, projections of $\Omega$ on the spin bivector; they add into the single coefficient $\Lambda+\omega\,\mathcal{Q}_{\mathrm{sig}}=\lambda e^{\omega\theta_{\mathrm{dua}}}$ |
| $\lambda,\ \kappa$ | The source's rotated pair, $\lambda=\Lambda\cos\theta_{\mathrm{dua}}+\\mathcal{Q}_{\\mathrm{sig}}\\sin\theta_{\mathrm{dua}}$ and $\kappa=\\mathcal{Q}_{\\mathrm{sig}}\\cos\theta_{\mathrm{dua}}-\Lambda\sin\theta_{\mathrm{dua}}$, with $\lambda+\omega\kappa=(\Lambda+\\omega\\,\\mathcal{Q}_{\\mathrm{sig}})e^{-\omega\theta_{\mathrm{dua}}}$; the constraints force $\kappa=0$ and $\lambda=\Lambda/\cos\theta_{\mathrm{dua}}$ real, and $\langle\tilde\nabla,\tilde J_{\Phi}\rangle=0$ then makes $\lambda$ a constant mass |

## Further Reading

- [The Gradient, the D'Alembertian and the Cell Operator](the-gradient-the-dalembertian-and-the-cell-operator.html), for the gradient, its conjugate and the d'Alembertian, and for the names of the other operators.
- Waldyr Alves Rodrigues Jr. and Jayme Vaz Jr., "Subluminal and Superluminal Electromagnetic Waves and the Lepton Mass Spectrum", arXiv:hep-th/9607231 (1996), the source of this article.
- J. Vaz Jr. and W. A. Rodrigues Jr., "Maxwell and Dirac Theories as an Already Unified Theory", *Advances in Applied Clifford Algebras* (1995), for the equivalence of the Maxwell and massless Dirac equations underlying the spinor representation.
- W. A. Rodrigues Jr. and J.-Y. Lu, "On the Existence of Undistorted Progressive Waves (UPWs) of Arbitrary Speeds $0\le|v|\le\infty$ in Nature", RP 12/96, IMECC-UNICAMP (1996), for the UPW and X-wave family and their generation.
- J.-y. Lu and J. F. Greenleaf, "Nondiffracting X waves", *IEEE Trans. Ultrason. Ferroelectr. Freq. Control* **39** (1992) 19–31, for the scalar X-wave solutions used as Hertz potentials.
- D. Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), and D. Hestenes and G. Sobczyk, *Clifford Algebra to Geometric Calculus* (Reidel, 1987), for the spacetime-algebra formulation and the bilinear covariants.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the projector operators and the spinor classification.
- M. W. Evans, "The present status of the Einstein–de Broglie–Vigier model", *Foundations of Physics* **24** (1994) 1971, cited by the source for evidence of longitudinal electromagnetic fields.
