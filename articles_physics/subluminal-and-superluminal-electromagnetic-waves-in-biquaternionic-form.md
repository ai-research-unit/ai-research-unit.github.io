# __Subluminal and Superluminal Electromagnetic Waves in Biquaternionic Form__

## Introduction

This article records an external programme, that of Waldyr Alves Rodrigues Jr. and Jayme Vaz Jr. as presented in *Subluminal and Superluminal Electromagnetic Waves and the Lepton Mass Spectrum* (arXiv:hep-th/9607231, 1996). It works in the **bundle of differential forms** over Minkowski spacetime and studies the single equation

$$
\partial F = 0
$$

for a 2-form field $F$, together with the spinor sector of the same algebra. From that starting point it claims two things. The first is that the free Maxwell equation has **subluminal and superluminal** solutions that are **undistorted progressive waves** and carry **non-null field invariants** and longitudinal field components — a family larger than the transverse plane waves of the textbook account. The second is that, writing the field as a **spinor bilinear** $F=-\psi\vec e_z\psi^{\natural}$, the free Maxwell equation is equivalent to a **non-linear Dirac–Hestenes equation** for $\psi$, and that this non-linear equation **linearises**: its two coefficients collapse into one real coefficient once the source's constraints hold, and that coefficient is a constant mass when the current is conserved; the same section shows the massless Dirac equation to be a Maxwell equation with an **axial (magnetic) current**.

A third claim follows, and it is the other half of the paper's title. The family of projections attached to the **Takabayasi angle** is what produces the **lepton mass spectrum**: at $\beta=\pi/2$ the muon mass comes out of the fine-structure constant and a magnetic quantum number, with no adjustable parameter left except that number itself.

The corpus records the programme and does not endorse it. Its value here lies in the structural part: the spinor representation of the field, the criterion that selects the linear equation, and the axial-current form of the massless equation. That part is **rigorous and checkable**, and it bears directly on questions the corpus states elsewhere: the invariant classification of *The Field-Strength Biquaternion and Its Invariants*, which classifies the field by its two invariants and notes that they are not conserved by the free evolution, but does not exhibit the family of free solutions that carry non-null invariants; the Dirac–Hestenes formulation of *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form*, which already carries the Yvon–Takabayasi angle as an "angle zero for a pure electron state" but not the criterion that makes the equation linear; and the axial-current form of the massless equation, which the spinor bilinear reproduces.

The source's conventions are close to the corpus's, and the places where they part are flagged as they come up, so that formulas are not misread between the two. The units, the central $i$ and the sign vector $\varepsilon=(1,-1,-1,-1)$ are those of *Conventions in the Biquaternion Universe*; the field $F$, the spinor $\psi$ and the volume element $\omega$ are elements of the biquaternion algebra $\mathbb{B}$.

The source writes its whole calculus with one letter, $\partial$, the Dirac operator of its bundle of forms, $d-\delta$, with $d$ the exterior derivative and $\delta$ the coderivative. That letter is not a symbol of the series, and the article says exactly what it buys before using it, because it is the one place where the two notations meet.

**It is not one of the series' operators, and it cannot be replaced by one.** The series' derivative operators are the gradient $\tilde\nabla$ and the d'Alembertian $\Box$ (*Operator and Calculus Conventions*). The gradient is a single left multiplication, $\tilde\nabla\psi=-\frac{i}{c}\frac{\partial\psi}{\partial t'}+\sum_k\vec e_k\frac{\partial\psi}{\partial x_k}$ on the material sector, and the d'Alembertian is its norm, second order and scalar. The source's $\partial$ is first order and **two-sided**: its time term multiplies the differentiated field on the right by $\vec e_x$, and its three spatial terms multiply on the left by $\vec e_k$ and on the right by $\vec e_y$. No left multiplication by the gradient, composed with one right multiplier, gives it, and the check is two lines. On $\psi=\vec e_x t'$ both sides are constant, and the right multiplier is forced to be $-\vec e_x$; on $\psi=\vec e_y x$ the operator gives $i\vec e_x$ and the forced multiplier gives $-\vec e_y$. One multiplier cannot serve, because the source's operator carries two.

**Written out, it is the four frame cells of the Pauli display.** Its four terms are four cells: the time term multiplies on the right by $\vec e_x$ alone; each spatial term multiplies on the left by the spatial unit of its own coordinate and on the right by $\vec e_y$. The right multiplier $\vec e_y$ is therefore common to the three spatial terms, and $\vec e_x$ is the right multiplier of the time term — which is exactly the pair of jobs the closing block's five frame cells give to $\vec e_y$ and to $\vec e_x$ (§*The Legacy Pauli Gamma Formulation*). The symbol therefore does not buy an operator: it buys back the defect of the display, and the body does not compute with it.

**So the article splits its uses.** The four field equations are the series' own, and are written as such: the free field equation is $\tilde\nabla\tilde F=0$; the potential equation $\partial^2\pi=0$ is $\Box\pi=0$, since $\partial^2=-\Box$; the sourced equation $\partial F=J$ is $\tilde\nabla\tilde F=\tilde J$; and the contractions $\partial\cdot j$, $\partial\cdot g$, $\partial\cdot J$ are the series' contractions of the gradient with the three currents. The one equation that stays in the source's letter is the spinorial one of §*The Field as a Spinor Bilinear*, $\partial\psi\,\omega=\ldots$, because there the operator is the subject: it is two-sided, and its right factor is the whole content of the equation. Even there the letter is read through the cells above, never as a black box.

For the record, its action on an element is the four products, one per coordinate. With the time coordinate written $t'$ — the source's $t$ — and in units $c=1$,

$$
\psi\mapsto i\,\frac{\partial\psi}{\partial t'}\vec e_x-\sum_k i\,\vec e_k\frac{\partial\psi}{\partial x_k}\vec e_y ,
$$

the spatial terms multiplying on both sides and the time term on the right. That the four right multipliers are the two just named is the whole of the check that the operator is two-sided.

The source's **volume element** is the product of its four generators, and the bookkeeping is short. The four $i$'s are central and give $i^4=+1$, so only the units matter. The left factors multiply in their printed order to $\vec e_x\vec e_y\vec e_z=\vec e_x\vec e_x=-e_t$, and the right factors, which compose in the reverse order, to $\vec e_y\vec e_y\vec e_y\vec e_x=-\vec e_y\vec e_x=+\vec e_z$. The two pieces give $-\vec e_z$, with no scalar left over, so the volume element is the element

$$
\omega=-\vec e_z,\qquad \omega^2=\vec e_z^2=-e_t ,
$$

the **pseudoscalar** of the source's display, and a root of $-e_t$. Its signs against the units are fixed here once: it anticommutes with $\vec e_x$ and $\vec e_y$ and commutes with $\vec e_z$ and $e_t$. Multiplied on the right, it anticommutes with each of the four terms of $\partial$: the right factors there are $\vec e_x$ once and $\vec e_y$ three times, and $\omega$ anticommutes with both. The source sets $i\equiv\omega$, so the "$i$" of its electric–magnetic notation $F=\vec E+i\vec B$ is that element — the **duality** — and not a second imaginary number: the two obey the one rule $i^2=-1$. Every $\exp(\omega\beta)$ below is the exponential of that element, $\cos\beta+\omega\sin\beta$, that is, a duality rotation.

The source's fixed bivector is $-\vec e_z$, the product of its second generator with its first, and it is the **spin plane**: it plays in the source's equation the role the corpus's Dirac–Hestenes equation gives to its own fixed bivector, and it multiplies the spinor on the **right**, as it does there. As an element it *is* the volume element $\omega$ displayed just above, so the spin plane and the duality generator are one element, which is why one symbol does both jobs in the source.

The spinor $\psi$ is an element of the biquaternion algebra $\mathbb{B}$, which is the corpus's own algebra. The source reaches the same structural equivalences from its bundle of forms, and the corpus records it as a different technical road to them, cross-referencing rather than merging.

## Maxwell's Equation in the Bundle of Forms

### The plane wave and the duality

The free equation $\tilde\nabla\tilde F=0$ — the source's $\partial F=0$ — is solved by the plane wave

$$
F = f\,\exp(\omega kx),
$$

with $f$ a constant 2-form and $k$ the propagation vector. Applying $k$ on the left gives $kF=0$, and applying $k$ again gives $k^2F=0$, so the propagation vector is **null**,

$$
k^2=0 \quad\Longleftrightarrow\quad k_0=\pm|\vec k| .
$$

The same equation forces $F^2=0$: the plane wave has **null invariants**. The step is not a cancellation, because a null $k$ has no inverse and multiplying $kF=0$ by $F$ gives only $kF^2=0$. The work is done by the decomposition. From $kF=0$ both the inner and the outer products vanish, so $f=k\wedge a$ for some vector $a$, and

$$
k\cdot f=k^2a-(k\cdot a)\,k=-(k\cdot a)\,k=0
$$

forces $k\cdot a=0$. A bivector joining a null vector to one orthogonal to it squares to zero,

$$
f^2=(k\cdot a)^2-k^2a^2=0,
$$

and the invariant $F^2=f^2\exp(2\omega kx)$ vanishes with it.

Both facts are the standard ones, and the source's point in restating them is the contrast with what follows — the plane waves of the free equation sit on the special null case, and the source then exhibits solutions that do not.

The role of the volume element is worth one paragraph, because the source insists on it. Since $\omega^2=-1$, the exponential splits as $\exp(\omega kx)=\cos kx+\omega\sin kx$, so

$$
F = f\cos kx + \omega f\sin kx .
$$

Writing $F=\vec E+\omega\vec B$ and $f=\mathbf e$, this is $\vec E+\omega\vec B=\mathbf e\cos kx+\omega\mathbf e\sin kx$: the electric and magnetic parts are **out of phase by a quarter period**, and the "$i$" of the standard complex formulation is precisely the $\omega$ that produces that phase, not a formal device. The source calls this the "secret" that the complex notation hides, and it is the observation on which the rest of its plane-wave discussion is built. That $\omega$ is what carries the duality is also why the **duality rotation** $F\mapsto \exp(\omega\beta)F$ of *Exercise: Duality Rotation and the Riemann–Silberstein Vector* appears below as the parameter that governs the non-linear equation.

### The Hertz potential

The solutions of the next two sections are generated by a **Hertz potential**. The source's theorem is that if a 2-form $\pi$ satisfies the wave equation $\partial^2\pi=0$ and the vector potential is taken as $A=-\delta\pi$ with $\delta$ the coderivative, then $F=\partial A$ solves the free field equation. In the series' notation that wave equation is $\Box\pi=0$ and that field equation is $\tilde\nabla\tilde F=0$, because $\partial^2=-\Box$. The proof is one line: $\partial F=\partial^2A$, and $\partial^2(-\,\delta\pi)=-\delta\,\partial^2\pi=0$, so the wave equation on $\pi$ is the only input. It is the technical device that converts a scalar solution of the wave equation into an electromagnetic field with the desired properties.

## Subluminal Solutions

### The stationary solution

Throughout, the time coordinate is written $t'$ — the source's $t$ — for the frame in which a given solution is written.

The source takes the Hertz potential to be $\pi=\Phi\,\vec e_z$, printed as a product of two of the generators of $\partial$; composed, the pair acts on the **left** by the bivector $\vec e_z$, and $\Phi$ is a function of the phase $\omega\Omega t'$ alone, so it commutes with the bivector and the left and the right readings of $\pi$ agree. The scalar part is separated as

$$
\Phi(t',x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \varphi(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\,\exp(\omega\Omega t'),
$$

so that the wave equation becomes the Helmholtz equation $\nabla^2\varphi+\Omega^2\varphi=0$. The simplest solution is the spherical one $\varphi(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)=C\,\sin(\Omega r)/r$, and the resulting stationary field $F_0$ is **regular at the origin** and **vanishes at infinity** — a localised field configuration at rest in the adapted frame. Written in the electric–magnetic split $F_0=\vec E_0+\omega\vec B_0$ it is

$$
\vec E_0=-\vec W\sin\Omega t', \qquad \vec B_0=\vec W\cos\Omega t',
$$

with $\vec W(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$ a fixed vector field, given explicitly in the source in terms of $\alpha=\Omega r\cos\Omega r-\sin\Omega r$ and $\beta=3\alpha+\Omega^2r^2\sin\Omega r$, with the angular dependence of the lowest spherical harmonics.

Three of its properties are the point of the construction. First, the invariant $I_1=\vec E_0^2-c^2\vec B_0^2$ and the pseudo-invariant $I_2=\vec E_0\cdot\vec B_0$ of *The Field-Strength Biquaternion and Its Invariants* are **not zero**. Here $\vec E_0^2$ is the sum of squared components, as in that article: the source's $\vec E$ and $\vec B$ are three-vectors whose units square to $+1$, as in the vector calculus, not spatial units $\vec e_k$, which square to $-1$. Both fields are parallel to $\vec W$ and a quarter period apart, so in the source's units $c=1$

$$
I_2=-\tfrac12|\vec W|^2\sin 2\Omega t',\qquad I_1=-|\vec W|^2\cos 2\Omega t',
$$

and $I_1$ takes both signs while $I_2$ vanishes only at the quarter periods. The field is of the **generic electric–magnetic-parallel type**, not the null type: a solution of the source-free Maxwell equation that carries a **non-null** field. Second, the field is **not transverse**: in the moving member of the family below the propagation vector is no longer orthogonal to the field, in contrast to the plane wave. That is why its construction matters to claims about longitudinal electromagnetic waves, for which the source cites Evans. Third, $\vec W$ satisfies the **Beltrami (force-free) equation**

$$
\mathrm{rot}\,\vec W = -\Omega\,\vec W,
$$

so that the configuration is a helical force-free field, the object that appears in plasma physics and in the earlier "force-free" literature the source cites. The sign is convention-laden and worth one warning: the four generators of $\partial$ carry a raised index, so the spatial part of $\partial$ is the negative of the Cartesian $\nabla$ and the curl it defines is the negative of the Cartesian one. Checked in Cartesian components, the printed $\vec W$ returns $\mathrm{curl}\,\vec W=+\Omega\vec W$; the minus in (3.21) is what this convention produces. The energy integral of $F_0$ alone diverges, and the source notes that finite-energy wave packets over a distribution of frequencies can be formed instead.

### The moving subluminal solution

The stationary field is the $v=0$ member of a moving family. For the family the source takes the Hertz potential

$$
\pi_<=C\,\frac{\sin\Omega\xi_<}{\xi_<}\,\exp\!\left[\omega(\varpi t'-q z)\right]\vec e_x\vec e_y,
\qquad
\xi_<^2=x^2+y^2+\frac{(z-vt')^2}{1-v^2},
$$

with the frequency $\varpi$, the axial wavenumber $q$, and the **massive dispersion relation**

$$
\varpi^2-q^2=\Omega^2,\qquad v=\frac{d\varpi}{dq}.
$$

That relation is what the word "subluminal" means here. Since $\varpi^2-q^2>0$, the group velocity obeys $|d\varpi/dq|=|q|/\varpi<1$ and the envelope travels slower than light, while the phase velocity is faster than light, $\varpi/q=\sqrt{1+\Omega^2/q^2}>1$. The envelope is therefore subluminal while the carrier phase it modulates runs ahead of $c$. The source's three summary statements are then these: a subluminal solution obeys the massive dispersion relation; its invariants are non-null; and it is **not a transverse wave**, which the source verifies by applying a Lorentz transformation of parameter $v$ to the stationary field.

### Purely electromagnetic particles

The subluminal solutions bear on a question older than the formalism. Einstein, following Poincaré and Ehrenfest, asked whether a **purely electromagnetic particle** can exist: a field configuration $F_p$ with current $J_p$ obeying $\tilde\nabla\tilde F_p=\tilde J_p$ — the source's $\partial F_p=J_p$ — and the subsidiary condition $J_p\cdot F_p=0$. The contraction $J_p\cdot F_p$ is a vector. With the field written $F_p=\vec E_p+\omega\vec B_p$ and the current split into charge density and spatial current, its vanishing has one time component and three spatial ones:

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

the first being the electric force density, the second the power density, and the third the magnetic force density on the current. The triple implies the pair above, but not conversely, so the source's implication runs the wrong way; the two forms coincide in each of the frames the argument goes on to use. For a **time-like** $J_p$ the frame is the rest frame, $\vec j_p=0$, where the condition reduces to $\rho_p\vec E_p=0$ and hence $\vec E_p=0$; then the time component of $\tilde\nabla\tilde F_p=\tilde J_p$, which is $\operatorname{div}\vec E_p=\rho_p$, forces $\rho_p=0$. No time-like configuration survives, and that is Einstein's conclusion. What carries the argument is the rest-frame form, not the printed triple.

For a **space-like** $J_p$ there is a frame with $\rho_p=0$ and $\vec j_p\ne0$, and the condition reduces to the remaining two components. A current parallel to the magnetic field, $\vec j_p=kC\,\vec B_p$ with $k=\pm1$ a sign and $C$ real, satisfies both: $\vec j_p\times\vec B_p=0$ because $\vec B_p$ is parallel to itself, and $\vec j_p\cdot\vec E_p=0$ provided $\vec E_p\cdot\vec B_p=0$.

The connection with the subluminal family is that the free stationary field $F_0$ can be **split** as a field plus a current, $\tilde\nabla\tilde F_0=0$ being equivalent to $\tilde\nabla\tilde F_p=\tilde J_p$ for a suitable space-like $J_p$; the free equation then models a standing purely electromagnetic particle. This is the source's route into the older programme of Waite, Barut and Zeni, which it cites; it is recorded here as a programme item, not as an established particle model.

## Superluminal Solutions: the X-Wave

The same Hertz-potential device produces **superluminal** solutions. The scalar seed is taken from the family of **X-waves**,

$$
\Phi_{X_n}(t',x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \exp(in\theta)\int_0^\infty B(k)\,J_n(k\rho\sin\eta)\,\exp(-k[a_0-i(z\cos\eta-t')])\,dk,
$$

with $\eta$ the **axicon angle** and $J_n$ the Bessel function. With $B(k)=a_0$ the integral is elementary, and the source's closed form is

$$
\Phi_{XBB_n}=a_0\,\frac{(\rho\sin\eta)^n e^{in\theta}}{\sqrt M\left(\tau+\sqrt M\right)^n},\qquad M=(\rho\sin\eta)^2+\tau^2,\qquad \tau=a_0-i(z\cos\eta-t').
$$

Used as the Hertz potential, this gives a **closed-form superluminal electromagnetic X-wave** (SEXW): a localised beam-like solution of the field equation in which $z\cos\eta-t'$ replaces the plane-wave phase, so that the pattern advances at speed $1/\cos\eta$ along the axis, faster than $c$. That is a pattern speed: the Bessel factor $J_n(k\rho\sin\eta)$ is an azimuthal superposition of plane waves inclined at the axicon angle, and each of those still travels at $c$. The source treats these as valid solutions of the free Maxwell equation and points to Rodrigues and Lu for the physical devices that would generate them.

The superluminality must be read with the corpus's usual care, and the source's own phrasing invites the mistake. The X-wave is a **localised pattern** whose amplitude profile advances superluminally; this is the **pattern (or phase) speed** of a finite wave packet and is not a speed of energy, information or signal. A free-field solution with a superluminal pattern is not in conflict with causality, and the corpus records the claim in that sense only. The same construction yields **subluminal and superluminal** solutions of the Weyl equation, and the source remarks that these obey $p^2=\Omega^2>0$ and $p^2=-\Omega^2<0$ respectively — a massless equation producing a massive-looking dispersion — which it offers as a possible reading of the neutrino puzzles. That part is speculative and is not carried.

## The Field as a Spinor Bilinear

### Two constraints, six degrees of freedom

The structural heart of the paper is the representation of the field as a **spinor bilinear**. With $\psi$ an element of $\mathbb{B}$ — a Dirac–Hestenes spinor in the source's terms — the field is written

$$
\boxed{\;F = -\psi\,\vec e_z\,\psi^{\natural}\;}
$$

where $\psi^{\natural}$ is the **reverse** of $\psi$: the corpus's natural conjugation $\natural$, which the source writes $\tilde\psi$. The counting matters: a general $\psi$ has **eight** real degrees of freedom, while the field $F$ has **six**, so two constraints must be imposed on $\psi$ for the correspondence to be one-to-one up to a normalisation. The source chooses them as $\partial\cdot j=0$ and $\partial\cdot g=0$, where $j$ and $g$ are the vector and axial-vector currents it builds from the derivative of $\psi$. This is the same eight-versus-six counting the corpus records in its Dirac–Hestenes article, which reaches it through the parameters of the rotor decomposition; the constraints are the source's extra data.

Substituting $F=-\psi\vec e_z\psi^{\natural}$ into the generalised Maxwell equation $\tilde\nabla\tilde F=\tilde J$ — the source's $\partial F=J$ — and using the canonical decomposition $\psi=\rho^{1/2}\exp(\omega\beta/2)R$ — the rotor $R$, the density $\rho$, and the **Takabayasi angle** $\beta$ — turns the field equation into a spinorial equation for $\psi$, with two scalar coefficients:

$$
\partial\psi\,\omega
=\left(\Lambda+\omega K\right)\psi\,i\vec e_x\exp(\omega\beta)
+\frac{1}{2\rho}\exp(\omega\beta)J\,\psi ,
$$

with $\Lambda=\Omega\cdot S$ and $K=\Omega\cdot(\omega S)$ built from the bivector $\Omega=\sum_\mu g_{\mu\mu}v_\mu\Omega_\mu$ and the spin bivector $S=-\tfrac12\psi\vec e_z\psi^{-1}=-\tfrac12R\vec e_zR^{-1}$, in which the phase cancels. The bivectors $\Omega_\mu$ are those of the rotor's derivative, $\partial \psi/\partial x_\mu=\tfrac12(\partial/\partial x_\mu\ln\rho+\omega\,\partial \beta/\partial x_\mu+\Omega_\mu)\psi$ with $\Omega_\mu=2(\partial R/\partial x_\mu)R^{-1}$, so $\Omega$ is the directional derivative of the rotor along the four-velocity. The source prints the two scalar terms separately; they are one, because both multiply the same product on the right, and they add into the single coefficient $\Lambda+\omega K$, a complex number in $\omega$.

The source also carries the pair $(\lambda,\kappa)$, with $\lambda=\Lambda\cos\beta+K\sin\beta$ and $\kappa=K\cos\beta-\Lambda\sin\beta$, and writes the same equation with it and no phase in front: the phase-free display is the same equation, because
$$
\lambda+\omega\kappa=\left(\Lambda+\omega K\right)\exp(-\omega\beta).
$$
Both spellings are used below; $(\Lambda,K)$ carries the geometry, since the two numbers are projections of $\Omega$ on the spin bivector, and $(\lambda,\kappa)$ is the pair that the free-field constraints act on.

The spin-plane factor needs a second look, because the source prints it as a product of two of its generators and the side is easy to mistake. Composed, that pair acts on the **left** by the fixed bivector $-\vec e_z$, that is $\psi\mapsto-\vec e_z\psi$. The equation applies the bivector on the **right**, $\psi\mapsto-\psi\vec e_z$, which is the volume element $\omega$ of the introduction. The two are different: one bivector on opposite sides, and only the right one is used below, because it is the one that anticommutes with $\vec e_x$.

The element $\omega$ carries the two signs of the phase against the algebra: it **commutes** with every function of itself, its half-rotation included, and it **anticommutes** with $\vec e_x$, because $\vec e_x\vec e_z=-\vec e_z\vec e_x$; the central $i$ passes through on both sides:

$$
\omega\,\vec e_x=-\vec e_x\,\omega .
$$

The free case $J=0$ is therefore

$$
\partial\psi\,\omega=\left(\Lambda+\omega K\right)\psi\,i\vec e_x\exp(\omega\beta),
$$

which has the shape of the Dirac–Hestenes equation but with a coefficient that is a **complex number in $\omega$** rather than a mass.

### Linearisation: the two Dirac equations

The equation above is non-linear because its coefficients depend on the field: $\Lambda$ and $K$ are built from the spin bivector $S$, which is a function of $\psi$, and $\beta$ is a function of $x$ as well. Two steps reduce it, and they give the two displays of the same equation. A third condition is needed for the reduction to end in a **mass**, and it is stated separately below.

**The constraint step.** The currents are $j=\lambda\rho v$ and $g=\kappa\rho v$ with $v=J/\rho$ the four-velocity, so the two constraints read $\rho\dot\lambda+\lambda\,\partial\cdot J=0$ and $\rho\dot\kappa+\kappa\,\partial\cdot J=0$, the dot being the derivative along the velocity, $\dot\lambda=(v\cdot\partial)\lambda$. Eliminating $\partial\cdot J$ between them leaves $\kappa\dot\lambda=\lambda\dot\kappa$, so the ratio of the coefficients is constant,
$$
\frac{\kappa}{\lambda}=-\tan\beta_0
\qquad\Longleftrightarrow\qquad
\frac{K}{\Lambda}=\tan(\beta-\beta_0),
$$
with $\beta_0$ a constant. Since $\beta$ is the angle of the duality rotation that produced $F$, a further rotation by $\beta_0$ shifts $\beta\mapsto\beta+\beta_0$, so $\beta_0=0$ may be chosen and
$$
\frac{K}{\Lambda}=\tan\beta,\qquad
\lambda=\Lambda\cos\beta+\Lambda\tan\beta\sin\beta=\frac{\Lambda}{\cos\beta},\qquad
\kappa=\Lambda\tan\beta\cos\beta-\Lambda\sin\beta=0 .
$$
The $\omega$-part is gone and the coefficient is a real scalar. For the free field,
$$
\boxed{\;\partial\psi\,\omega=\lambda\,\psi\,i\vec e_x\;}
$$
which has the **shape** of the Dirac–Hestenes equation, with a single real coefficient $\lambda$ — in units of inverse length, since restoring $\hbar$ and $c$ gives $\lambda=mc/\hbar$. The coefficient has become real; whether it is a **mass** is the next question. In the unrotated pair the same coefficient reads $\Lambda+\omega K=\lambda\exp(\omega\beta)$, the real coefficient times the duality phase, which is why the phase-carrying display and this one are one equation.

**The mass is a constant only for a conserved current.** Nothing so far makes $\lambda=\Lambda/\cos\beta$ constant, and neither factor need be. What the first constraint does give is $\rho\dot\lambda+\lambda\,\partial\cdot J=0$, so that

$$
\partial\cdot J=0\quad\Longleftrightarrow\quad \lambda=\text{const}.
$$

The source states it that way round: the current $J$ is not conserved unless $\lambda$ is constant, so it assumes $\partial\cdot J=0$ explicitly. That assumption is the third condition, and it is the one that turns a Dirac–Hestenes-shaped equation into a Dirac–Hestenes equation with a mass. Without it the display above is exact but its coefficient drifts from point to point.

**The rescaling step.** The same content reads as a statement about the spinor. Put $\psi=\varphi\exp(\omega\beta/2)$ with $\varphi=\sqrt\rho\,R$ and $\beta$ constant. The rotation $\exp(\omega\beta/2)$ does not depend on $x$, so it passes through the derivative on the left side, and the anticommutation with $i\vec e_x$ merges the two phases on the right side into the same half rotation:
$$
\partial\psi\,\omega=\partial\varphi\,\omega\exp(\omega\beta/2),
$$
$$
\left(\Lambda+\omega K\right)\psi\,i\vec e_x\exp(\omega\beta)
=\left(\Lambda+\omega K\right)\varphi\,i\vec e_x\exp(\omega\beta/2).
$$
The common right factor cancels — it is the **last** factor on both sides, and it is invertible — leaving the same equation with the phase gone,

$$
\partial\varphi\,\omega=\lambda\,\varphi\,i\vec e_x,
$$

with $\Lambda$ and $K$ unchanged, since the phase cancels in the spin bivector. A constant angle is thus not a parameter of the dynamics but a phase carried by the spinor, and solutions with different constant $\beta$ are the same solution multiplied on the right.

The half angle is not a convention. The source prints the full one in one place, where its (5.15) is said to follow from $\psi=\varphi\exp(\beta\omega)$. With that exponent the phase does not cancel: the left side of the source's (5.7) carries one power of it, the right side none. The reason is that on the right the phase enters twice — once from $\psi$ and once from the equation itself — and the two annihilate after the inner one passes the odd factor, $\exp(\omega\beta)\,i\vec e_x=i\vec e_x\exp(-\omega\beta)$. What follows with the full exponent is $\partial\varphi\,\omega=m\varphi\,i\vec e_x\exp(-\omega\beta)$, with the phase moved to the other side rather than removed. The rest of the paper uses the half angle: the solutions (5.16) and (5.17) carry $\exp(\beta\omega/2)$, and the mass-spectrum decomposition (6.6) is $\psi=\exp(\omega\beta/2)\varphi$.

**The narrower case $J=0$, $K=0$.** With the constraints imposed the two displays are one equation, the coefficient $\Lambda+\omega K=\lambda\exp(\omega\beta)$ being the real coefficient times the phase. The source also studies this narrower case, where the coefficient is $\Lambda$ alone and the phase stands in front; it notes that this form was studied extensively by Daviau. It is non-linear as it stands, it reduces to the Dirac–Hestenes equation by the rescaling above at every constant $\beta$, and it is *identical* to that equation only at $\beta=0$ and $\beta=\pi$ — the two angles the source assigns to the electron and the positron, through the family of the next section.

The plane-wave solutions of *The Dirac Equation in Biquaternionic Form* have a constant spinor coefficient, so their $\beta$ is constant, and *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form* calls $\beta=0$ the pure electron state. They therefore sit on this linearisable class, and the source supplies the general reason why.

Two consequences the source draws from the same algebra are worth recording. The first is a **superselection rule**: the superposition principle survives only for spinors of the same $\beta$, because the coefficients depend on that angle, so a sum of solutions with different angles is not a solution; the source reads this as particles and antiparticles forming separate superselection sectors. The second is the **momentum relation**. Multiplying the non-linear equation by $\psi^{-1}$ gives $p=mv$ for every angle $\beta$, whereas the linear Dirac–Hestenes equation gives $p=\exp(\omega\beta)mv$, which for $p$ and $v$ real forces $\beta=0$ or $\beta=\pi$ and thus the choice between positive and negative energy. In the non-linear interpretation there is no negative-energy problem to interpret: the equation gives $p=mv$ throughout, and the source proposes to reinterpret the energy projector as a **particle projector** instead.

The **Tetrode tensor** is what backs that reinterpretation. Its trace for the non-linear equation is

$$
T=m\,\bigl\langle\psi\,\psi^{\natural}\exp(-\omega\beta)\bigr\rangle_0=m\rho ,
$$

positive for every solution, so every solution has positive energy; the linear equation gives $T_{\mathrm{Dirac}}=m\rho\cos\beta$, and the two differ by the factor $\cos\beta$, coinciding only at the two endpoints. The source adds one structural remark that the corpus records as a curiosity: the Tetrode energy–momentum one-form is a kind of **square root** of the Maxwell energy–momentum one-form $S_\mu=\tfrac12\,i\,Fe_\mu F\vec e_{\nu(\mu)}$. The overall sign is not fixed by the print: a 2-form reverses to minus itself, $\tilde F=-F$, so the same object written with the reverse in the middle differs only in that sign.

Here $e_\mu$ and $\vec e_{\nu(\mu)}$ are the unit of the coordinate $x_\mu$ and its partner, with $\nu(t)=x$ and $\nu(k)=y$, and the two act on the middle factor of $F$.

### The projection operators

The family that carries the mass spectrum is a family of projections on the algebra, and it is stated precisely here, including the one printed relation that cannot hold.

**The pair.** The source builds it from the **conjugation** by its time vector, which in the algebra is the element $i\vec e_x$: an element $\psi$ is carried to $i\vec e_x\,\psi\,i\vec e_x$. The two members of the pair are the two values

$$
\psi_+=\tfrac12\left(\psi+i\vec e_x\,\psi\,i\vec e_x\right),\qquad
\psi_-=\tfrac12\left(\psi-i\vec e_x\,\psi\,i\vec e_x\right),
$$

so that $\psi=\psi_++\psi_-$ is the same element written as their sum. The conjugating element squares to $+e_t$, $(i\vec e_x)^2=i^2\vec e_x^2=(-1)(-1)=+1$ by the sign rule of the introduction, so conjugating twice returns every element,

$$
i\vec e_x\left(i\vec e_x\,\psi\,i\vec e_x\right)i\vec e_x=\psi .
$$

Two consequences follow, one line each. The conjugated value of $\psi_+$ is $+\psi_+$ and that of $\psi_-$ is $-\psi_-$,

$$
i\vec e_x\,\psi_+\,i\vec e_x=+\psi_+,\qquad i\vec e_x\,\psi_-\,i\vec e_x=-\psi_- ,
$$

and each of the two values is fixed by its own map and annihilated by the other, because the second term of the map then reproduces the first term or cancels it.

**The conjugation is not the identity, and it is not an idempotent.** It takes both values on the algebra, each on four of the eight real dimensions, so the pair splits the algebra into two fours. The corpus's Dirac–Hestenes article splits the same algebra by an **idempotent applied on one side**, an idempotent built from a unit that article declares; that is a different split. The source uses no idempotent here, and the element it conjugates by is the time vector of its own frame.

**The one-parameter family.** The family is the same projection seen from a duality-rotated frame. With the volume element $\omega$,

$$
\psi_\beta=\tfrac12\left(\psi+\exp(\omega\beta)\,i\vec e_x\,\psi\,i\vec e_x\right)
=\exp\!\left(\tfrac{\omega\beta}{2}\right)\tfrac12\left(\xi+i\vec e_x\,\xi\,i\vec e_x\right),
\qquad
\xi=\exp\!\left(-\tfrac{\omega\beta}{2}\right)\psi ,
$$

that is, rotate the element, project it, rotate the result back. The right-hand display holds for two reasons. The inner half phase passes the conjugating element with a change of sign,

$$
\exp\!\left(-\tfrac{\omega\beta}{2}\right)i\vec e_x=i\vec e_x\exp\!\left(\tfrac{\omega\beta}{2}\right),
$$

because $\omega$ anticommutes with $\vec e_x$; and the two half phases add into the full $\exp(\omega\beta)$, both being powers of the one element $\omega$. That is the source's (5.28) as printed.

**The family projects for every $\beta$.** The conjugating element of the family is $K=\exp(\omega\beta)\,i\vec e_x$, and

$$
K^2=\exp(\omega\beta)\,i\vec e_x\,\exp(\omega\beta)\,i\vec e_x=(i\vec e_x)^2=+1 .
$$

The inner $\exp(\omega\beta)$ passes $\vec e_x$ with a change of sign and cancels the outer one. So conjugating twice by $K$ returns every element, and every member of the family is a projection, not only the two ends.

The list the source prints is then read on the values. The value at $\beta$ put through the map at $\beta$ again is the same value; the map at $\beta+\pi$ complements it, so $\psi_\beta+\psi_{\beta+\pi}=\psi$ and the map at $\beta+\pi$ applied to $\psi_\beta$ gives zero; and $\psi_\beta$ is $\psi_+$ for every element only at $\beta\equiv0$ modulo $2\pi$. On the two values of the split the family reads

$$
\psi_+\longmapsto\cos\tfrac{\beta}{2}\,\exp\!\left(\tfrac{\omega\beta}{2}\right)\psi_+,\qquad
\psi_-\longmapsto-\omega\sin\tfrac{\beta}{2}\,\exp\!\left(\tfrac{\omega\beta}{2}\right)\psi_-,
$$

which is where the cosine and sine weights of the family come from, and it is why the family returns $\psi_\pm$ to itself only at the endpoints: at $\beta=\pi$ the second line returns $\psi_-$, because $\exp(\omega\pi/2)=\omega$ and $\omega^2=-1$.

**The printed relation that cannot hold is the middle one of the three.** The source lists that the family is a projection, that the angle $\beta+\pi$ gives the same map as $\beta$, and that the two maps at $\beta$ and $\beta+\pi$ have zero product. The first two make the third say that the value at $\beta$ is zero for every element, which no projection gives. The relation that holds, and the one the printed line must be a slip for, is the sum

$$
\psi_\beta+\psi_{\beta+\pi}=\psi .
$$

That is the correction the corpus records: the printed $=$ is missing a $+$ and a $\psi$.

## The Lepton Mass Spectrum

The family of the previous section is introduced for the mass spectrum, and the construction is short. The **electron** is the free field, $\tilde\nabla\tilde F_e=0$ with $F_e^2\ne0$, written $F_e=-\psi_e\vec e_z\psi_e^{\natural}$; by the linearisation above, $\psi_e$ obeys the Dirac–Hestenes equation with the electron mass at $\beta=0$, and the positron sits at $\beta=\pi$. The source prints the spin plane in both terms of its (6.2); as printed that equation is $(\partial\psi_e+m\psi_e)\vec e_z=0$, which is not a Dirac–Hestenes equation, and the mass term must carry the time vector, as in the linearised form above. The **muon** is taken to be that free field **plus the field of the $+$ branch**, $F=F_e+F_+$ — the field of a massless spinor with a magnetic current, the object of the next section.

The magnetic current re-enters the sourced spinorial equation, and for the phase-free spinor the equation keeps the Dirac form with two coefficients — masses in inverse-length units, hence the $c/\hbar$:

$$
\partial\varphi\,\omega=\frac{Mc}{\hbar}\,\varphi\,i\vec e_x+\omega\,\frac{Nc}{\hbar}\,\varphi\,i\vec e_x,
\qquad
M=m+3m\,\frac{q_{\mathrm{m}}}{e}\sin\beta,\qquad
N=-3m\,\frac{q_{\mathrm{m}}}{e}\cos\beta ,
$$

with $q_{\mathrm{m}}$ the magnetic charge. The $3$ carries the normalisation, and the source does not display the step: it fixes $F=-k\,(e\hbar/mc)\,\psi\vec e_z\psi^{\natural}$ with $k=2\pi/3$ and states only that (6.5) follows "as in section 4". The natural reading is the Gaussian $4\pi/c$ on the current, with the $\tfrac12$ of the spinorial Maxwell equation, against $k$: $4\pi/(2k)=3$. That reconstruction is not printed, so the coefficient stands or falls with (6.5) as it appears. What $k$ does **not** do is fix the dimensions — $[F]=QL^{-2}$ and $[e\hbar/mc]=QL$ already force $[\psi]=L^{-3/2}$ — so its value is chosen for the spectrum. The equation is a Dirac–Hestenes equation exactly when $N=0$, that is at $\beta=\pi/2$ and $\beta=3\pi/2$ — the two angles of the family that the source assigns to the muon and the antimuon. Then $M=m+3mq_{\mathrm{m}}/e$, and the Dirac quantisation condition for a monopole, $eq_{\mathrm{m}}/\hbar c=n/2$, gives $q_{\mathrm{m}}=en/2\alpha$ with $\alpha=e^2/\hbar c$ the fine-structure constant, so

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

The equivalence runs in the other direction as well, and that direction carries the axial current. The **massless** Dirac equation $\partial\psi=0$ for an element $\psi$ of $\mathbb{B}$ is equivalent to a **generalised Maxwell equation**, $\tilde\nabla\tilde F=\tilde J$ with the current written out:

$$
\tilde\nabla\tilde F = \tilde J_{\mathrm{e}} - \omega \tilde J_{\mathrm{m}} = \tilde J ,
$$

with both an electric current $J_{\mathrm{e}}$ and an **axial (magnetic) current** $-\omega J_{\mathrm{m}}$. For $\psi_+$, the $+$ branch of the split by $i\vec e_x$, the electric current vanishes, $j_{\mathrm{e}}=0$, and the equivalent Maxwell equation reads

$$
\boxed{\;\tilde\nabla\tilde F_+ = -\omega\tilde J_{\mathrm{m}}\;}
$$

that is, a **massless Dirac field is a Maxwell field with a magnetic current and no electric current**. The current is not external. It is read off the spinor's own components: writing the $L$ value of the $+$ branch as $s+F-\omega p$, with $s$ and $p$ real and $F$ the field bivector, the source finds $\tilde\nabla\tilde F_+=-\omega\,\tilde\nabla p$, so $J_{\mathrm{m}}=\partial p$ and the Maxwell equation is **self-sourced**. The mechanism is the split by $i\vec e_x$: the source shows that $\psi_+$ decouples into a pair of Weyl fields of opposite charge, $\partial\psi_{+R}+g\omega B\psi_{+R}=0$ and $\partial\psi_{+L}-g\omega B\psi_{+L}=0$ — the spin-plane factor absorbed in each by the Weyl condition, and the subscript naming the value, $L$ the minus value and $R$ the plus one — so that a single $\psi_+$ coupled to a potential carries a particle of charge $+g$ and a particle of charge $-g$ at once. This is a further route in the corpus by which a magnetic current appears in a spinorial or quaternionic reformulation of Maxwell's equations.

### One Dirac Equation or Two

The corpus has two spellings of the massive Dirac equation, and the source's equation is the second of them.

**The one-sided pair.** Two equations, one per value of the subscript, both gradients acting from the left:

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L
$$

$$
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R .
$$

The second gradient is the quaternion conjugate of the first, and it is the conjugation, not a side, that distinguishes them. The mass is the only term that couples the two values, and at $m=0$ the pair splits into $\tilde\nabla\tilde\Psi_R=0$ and $\tilde\nabla^{\natural}\tilde\Psi_L=0$, one Weyl equation per value.

**The two-sided single equation.** The same physics has a representation on the whole algebra, as one equation for one field:

$$
\tilde\nabla^{\natural}F=m\,\bar F\,i\omega ,
$$

with the derivative on the left and the mass on the right through the element $i\omega=-i\vec e_z$ that exchanges the two values, applied to the coefficient conjugate $\bar F$. The pair is the definition; the two-sided form is the representation in which the mass is a right multiplication, and it is antilinear in that term.

**The source's equation has that shape.** Its Dirac–Hestenes equation

$$
\partial\psi\,\omega=m\,\psi\,i\vec e_x
$$

acts with the derivative on the left and multiplies on the right by the fixed bivector and by the mass — a left action and two right factors, no second field. That is the shape of the corpus's own Dirac–Hestenes equation too, in which the mass also multiplies on the right, at a fixed bivector; the pair of values is a different spelling of the same physics, and the two-sided form is the one both the corpus's equation and the source's take. What it does not have is a second equation for the other value. The two values are the two halves of the one spinor under the source's **Weyl conditions**, which pair the volume element on one side with the fixed bivector on the other. Written as a condition on the one spinor it is $\psi_{L}\omega=-\omega\psi_{L}$ and $\psi_{R}\omega=+\omega\psi_{R}$, that is $\psi_{L}\vec e_z=-\vec e_z\psi_{L}$ and $\psi_{R}\vec e_z=+\vec e_z\psi_{R}$: the bivector enters twice, once as a product on the right and once as a product on the left. The condition is therefore a genuine constraint, and its two branches are the two four-dimensional halves of the algebra — the spinor commuting with $\vec e_z$ and the one anticommuting. What effects the split is the **pseudoscalar**, not a second field; and because in this frame the volume element and the spin plane are written with the one bivector, the source needs the single symbol $i$ for both jobs. The symbols are written out in *The Legacy Pauli Gamma Formulation*.

**Where the two presentations diverge.** They agree at $m=0$, each giving Weyl equations, and part ways once a mass is present. the corpus's mass couples the two values, in two fields, and is antilinear; the source's mass is linear and multiplies the one spinor on the right by a fixed element with a scalar coefficient. That is why the coefficient of the sourced equation is a complex number in $\omega$ rather than a real mass — a mass times a duality phase — and why its linearisation needs both of the steps of *Linearisation* above: the constraints, which turn the imaginary part into a pure phase, and the rescaling, which removes it.


## Status, Contrasts, and Boundaries

What the programme establishes is the **structural half**. That the free Maxwell equation has solutions with non-null invariants is true and is a genuine correction to the reflex that "free electromagnetic waves are null transverse plane waves"; the classification of *The Field-Strength Biquaternion and Its Invariants* admits such fields but does not exhibit them, and the subluminal construction here supplies the missing example. That the field is a spinor bilinear and that the Maxwell equation for the field is a non-linear Dirac–Hestenes equation which linearises, under its two constraints, to a single real coefficient — and to one real mass once the current is conserved — is likewise a clean structural statement, and it explains from a second direction why the corpus's plane-wave Dirac solutions are simple. That the massless Dirac equation is a Maxwell equation with an axial current is the third, and it reproduces the corpus's axial-current form.

The boundaries are these. The source's route through the bundle of forms is an **external formalism**; the corpus's own treatment is the biquaternion one, and the two are related through the dictionary between the forms and the algebra rather than identified. The "superluminal" of the X-wave is a pattern speed of a localised solution, not a signalling speed, and must not be read otherwise. The **purely electromagnetic particle** is a programme item revived from Einstein and Waite, not a constructed particle. The **mass spectrum** is a proposal, not a derivation. The muon comes out of one algebra with the monopole quantum number $n=1$; nothing in the algebra fixes that number; the tau needs a further hypothesis on it; and the arithmetic of the states beyond the muon, as the mass-spectrum section shows, does not close.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. Each is a **cell**, a left multiplication times a right one, with $L_a\psi=a\psi$ and $R_b\psi=\psi b$:

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$. The gammas then obey the cell relations of $\varepsilon=(1,-1,-1,-1)$:

$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k[\mathbb{M}_-])^2=-I_4,\qquad
\gamma_5[\mathbb{M}_-]^2=I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5[\mathbb{M}_-]\}=0,
\qquad \varepsilon=(1,-1,-1,-1),$$
$$
[\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]]=2\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\quad(\mu\ne\nu),\qquad
[\gamma_a[\mathbb{M}_-],S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d[\mathbb{M}_-]-\varepsilon_a\delta_{ad}\gamma_c[\mathbb{M}_-],\qquad
S_{cd}=\tfrac14[\gamma_c[\mathbb{M}_-],\gamma_d[\mathbb{M}_-]],
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-])=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$

**The symbol $\gamma_5[\mathbb{M}_-]$ is the one place where the two notations collide.** The source's $\gamma_5[\mathbb{M}_-]$ is its volume element, the product of the four generators, and that product is the cell $\omega$ itself; the corpus's own $\gamma_5[\mathbb{M}_-]$ is the reference-frame cell of the chirality $\Gamma$, which is $i\omega$. The two differ by the central $i$, and that is the whole of the difference:

$$
\omega=-i\gamma_5[\mathbb{M}_-],\qquad \omega^2=-1,\qquad \gamma_5[\mathbb{M}_-]^2=i^2\omega^2=+1 .
$$

Every $\omega$ in the body is the source's $\gamma_5[\mathbb{M}_-]$. The central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi_{\mathrm{ad}}^2=e_t$ — is a third object again, represented by $\gamma_5[\mathbb{M}_-]$ on the Dirac module.

The article's frame is the source's: the volume element above is the body's $\omega$, and the fixed bivector is $\gamma_2[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]=-\vec e_z$, the source's $\gamma_{21}[\mathbb{M}_-]$. The cell identities the body uses are

$$
\gamma_2[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]=L_{-\vec e_z}^{\mathrm{pau}},\qquad \gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-i\gamma_5[\mathbb{M}_-]=R_{-\vec e_z}^{\mathrm{pau}},\qquad (iR_{\vec e_x}^{\mathrm{pau}})^2=R_{i^2\vec e_x^2}^{\mathrm{pau}}=R_{(-1)(-1)}=I_4,
$$

In the axis-free display:

$$
\gamma_2[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]=L_{-\vec e_z}^{\mathrm{axf}},\qquad \gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]=-i\gamma_5[\mathbb{M}_-]=R_{-\vec e_z}^{\mathrm{axf}},\qquad (iR_{\vec e_x}^{\mathrm{axf}})^2=R_{i^2\vec e_x^2}^{\mathrm{axf}}=R_{(-1)(-1)}=I_4,
$$

so the pair the source prints composes to left multiplication by $-\vec e_z$, while the right multiplication by the same bivector is the volume element itself.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every cell in this section is written twice: in the Peirce display first, labelled $\mathrm{pau}$, which is the display the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. A frame label is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free form is the conjugate. The label names the display and not the operator.

## Summary

The programme of Rodrigues and Vaz works in a bundle of differential forms and presses the free Maxwell equation — $\partial F=0$ in the source's letter, $\tilde\nabla\tilde F=0$ in the series' — in two directions. It exhibits **subluminal and superluminal undistorted progressive wave solutions with non-null invariants and longitudinal components**, built from a Hertz potential and a spherical Helmholtz solution, and connects the free stationary solution to the old question of purely electromagnetic particles. It represents the field as the **spinor bilinear** $F=-\psi\vec e_z\psi^{\natural}$ and shows the Maxwell equation to be a **non-linear Dirac–Hestenes equation**, with the **Takabayasi angle** as the knob: the two constraints collapse its two coefficients into a single real one for every $\beta$, a conserved current makes that coefficient the mass, and $0$ and $\pi$ then give the electron and the positron, while $\pi/2$ and $3\pi/2$ make it the muon and the antimuon once a magnetic current is added, with $M=m(1+3n/2\alpha)$ at $n=1$. In the other direction the **massless Dirac equation is a Maxwell equation with an axial (magnetic) current**, which is the route by which a magnetic current appears.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra, of which the field and the spinor are elements |
| $\varepsilon=(1,-1,-1,-1)$ | sign vector of the layer |
| $\omega=-\vec e_z$ | Volume element, the pseudoscalar; $\omega^2=-e_t$; the source's "$i$", the duality |
| $-\vec e_z$ | Fixed spin-plane bivector, the source's product of its second generator with its first; as the element $\omega$ it multiplies the spinor on the right |
| $\partial$ | The source's letter for the Dirac operator $d-\delta$ of its bundle of forms, $d$ the exterior derivative and $\delta$ the coderivative. Not one of the series' two derivative operators: first order, and two-sided, its time term multiplying on the right by $\vec e_x$ and its three spatial terms on the left by $\vec e_k$ and on the right by $\vec e_y$. Its square is the wave operator, $\partial^2=-\Box$. Used below for the spinorial equation only; the field equations are written $\tilde\nabla\tilde F=\tilde J$ |
| $F$, $F_0$, $F_e$, $F_+$ | Field 2-form; the stationary subluminal solution; the electron field; the field of the $+$ branch |
| $\pi$, $A$ | Hertz potential; vector potential, $A=-\delta\pi$ |
| $f$, $k$, $x$ | Constant 2-form; propagation vector ($k^2=0$); position |
| $\vec E_0,\vec B_0,\vec W$ | Fields of the stationary solution and their common vector, $\mathrm{rot}\,\vec W=-\Omega\vec W$ in the source's raised-index convention |
| $\Omega$ | Intrinsic frequency of the subluminal solution ($\Omega$ in the Helmholtz equation $\nabla^2\varphi+\Omega^2\varphi=0$); the letter is reused, as in the source, for the bivector $\Omega=\sum_\mu g_{\mu\mu}v_\mu\Omega_\mu$ of the spinorial section |
| $\varpi,\ q,\ \xi_<$ | Frequency and axial wavenumber of the moving subluminal solution, with $\varpi^2-q^2=\Omega^2$ and group velocity $v=d\varpi/dq$; $\xi_<$ is its oblate radial coordinate |
| $\Phi_{X_n},\ \Phi_{XBB_n}$ | Scalar X-wave seed and its closed form, with $\eta$ the axicon angle and $a_0$ the constant that regularises the seed |
| $\psi$, $\psi^{\natural}$ | The spinor, an element of $\mathbb{B}$, and its reverse, the corpus's $\natural$ conjugation; the source writes the reverse $\tilde\psi$ |
| $\psi_\pm$ | The two values of the split by $i\vec e_x$, $i\vec e_x\,\psi_\pm\,i\vec e_x=\pm\psi_\pm$, with $\psi=\psi_++\psi_-$ |
| $\psi_{L}$, $\psi_{R}$ | The two values of the subscript, $L$ the minus value and $R$ the plus one; $\psi_{+L}$ and $\psi_{+R}$ are the two values of the $+$ branch |
| $\psi=\rho^{1/2}\exp(\omega\beta/2)R$ | Canonical decomposition: rotor $R$, density $\rho$, angle $\beta$; the letter $\rho$ is reused in the X-wave for the cylindrical radius |
| $\beta$ | Takabayasi (Yvon–Takabayasi) angle; $0,\pi$ electron/positron, $\pi/2,3\pi/2$ muon/antimuon |
| $\varphi$ | Spinor with the phase divided out, $\psi=\varphi\exp(\omega\beta/2)$; the linear Dirac equation is for $\varphi$ |
| $m$, $M$, $N$ | Electron mass; the two coefficients of the sourced equation, $M=m+3mq_{\mathrm{m}}\sin\beta/e$ and $N=-3mq_{\mathrm{m}}\cos\beta/e$, the second vanishing at $\beta=\pi/2$ and $3\pi/2$; the letter $M$ is reused, as in the source, for the radial factor of the X-wave |
| $q_{\mathrm{m}}$, $\alpha$ | Magnetic charge, $q_{\mathrm{m}}=en/2\alpha$ from the Dirac quantisation condition $eq_{\mathrm{m}}/\hbar c=n/2$; $\alpha=e^2/\hbar c$ the fine-structure constant |
| $j$, $g$, $J=J_{\mathrm{e}}-\omega J_{\mathrm{m}}$ | Vector current, axial current, total current with electric and magnetic parts; the source's contractions $\partial\cdot j$ and $\partial\cdot g$ are the series' contractions of the gradient with the two currents |
| $\psi_\beta$ | The family of the source, $\tfrac12(\psi+e^{\omega\beta}i\vec e_x\,\psi\,i\vec e_x)$, which is the projection at $\beta$ in a duality-rotated frame; $\psi_\beta+\psi_{\beta+\pi}=\psi$ replaces the printed $\Lambda_\beta=\Lambda_{\beta+\pi}$ |
| $S=-\tfrac12\psi\vec e_z\psi^{-1}$ | Bivector of the canonical analysis; $S_\mu=\tfrac12\,i\,Fe_\mu F\vec e_{\nu(\mu)}$ the Maxwell energy–momentum one-form, $e_\mu$ the unit of the coordinate $x_\mu$ |
| $\Lambda,\ K$ | The two scalars of the spinorial Maxwell equation, $\Lambda=\Omega\cdot S$ and $K=\Omega\cdot(\omega S)$, projections of $\Omega$ on the spin bivector; they add into the single coefficient $\Lambda+\omega K=\lambda e^{\omega\beta}$ |
| $\lambda,\ \kappa$ | The source's rotated pair, $\lambda=\Lambda\cos\beta+K\sin\beta$ and $\kappa=K\cos\beta-\Lambda\sin\beta$, with $\lambda+\omega\kappa=(\Lambda+\omega K)e^{-\omega\beta}$; the constraints force $\kappa=0$ and $\lambda=\Lambda/\cos\beta$ real, and $\partial\cdot J=0$ then makes $\lambda$ a constant mass |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- Waldyr Alves Rodrigues Jr. and Jayme Vaz Jr., "Subluminal and Superluminal Electromagnetic Waves and the Lepton Mass Spectrum", arXiv:hep-th/9607231 (1996), the source of this article.
- J. Vaz Jr. and W. A. Rodrigues Jr., "Maxwell and Dirac Theories as an Already Unified Theory", *Advances in Applied Clifford Algebras* (1995), for the equivalence of the Maxwell and massless Dirac equations underlying the spinor representation.
- W. A. Rodrigues Jr. and J.-Y. Lu, "On the Existence of Undistorted Progressive Waves (UPWs) of Arbitrary Speeds $0\le|v|\le\infty$ in Nature", RP 12/96, IMECC-UNICAMP (1996), for the UPW and X-wave family and their generation.
- J.-y. Lu and J. F. Greenleaf, "Nondiffracting X waves", *IEEE Trans. Ultrason. Ferroelectr. Freq. Control* **39** (1992) 19–31, for the scalar X-wave solutions used as Hertz potentials.
- D. Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), and D. Hestenes and G. Sobczyk, *Clifford Algebra to Geometric Calculus* (Reidel, 1987), for the spacetime-algebra formulation and the bilinear covariants.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the projector operators and the spinor classification.
- M. W. Evans, "The present status of the Einstein–de Broglie–Vigier model", *Foundations of Physics* **24** (1994) 1971, cited by the source for evidence of longitudinal electromagnetic fields.
