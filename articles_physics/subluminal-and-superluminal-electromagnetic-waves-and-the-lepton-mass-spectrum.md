# __Subluminal and Superluminal Electromagnetic Waves in Biquaternionic Form__

## Introduction

This article records an external programme, that of Waldyr Alves Rodrigues Jr. and Jayme Vaz Jr. as presented in *Subluminal and Superluminal Electromagnetic Waves and the Lepton Mass Spectrum* (arXiv:hep-th/9607231, 1996). It works in the **Clifford bundle of differential forms** $C\ell(M)$ and studies the single equation

$$
\partial F = 0
$$

for a 2-form field $F$, together with the spinor sector of the same algebra. From that starting point it claims two things. The first is that the free Maxwell equation has **subluminal and superluminal** solutions that are **undistorted progressive waves** and carry **non-null field invariants** and longitudinal field components — a family larger than the transverse plane waves of the textbook account. The second is that, writing the field as a **spinor bilinear** $F=-\psi\vec e_z\psi^{\mathrm{c}}$, the free Maxwell equation is equivalent to a **non-linear Dirac–Hestenes equation** for $\psi$, and that this non-linear equation **linearises** exactly when the **Takabayasi angle** $\beta$ is constant; the same section shows the massless Dirac equation to be a Maxwell equation with an **axial (magnetic) current**.

The corpus records the programme and does not endorse it. Its value to this corpus is twofold. The structural part — the spinor representation of the field, the criterion that selects the linear equation, and the axial-current form of the massless equation — is **rigorous and checkable**, and it bears directly on questions the corpus states elsewhere: the invariant classification of *The Field-Strength Biquaternion and Its Invariants*, which classifies the field by its two invariants and notes that they are not conserved by the free evolution, but does not exhibit the family of free solutions that carry non-null invariants; the Dirac–Hestenes formulation of *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form*, which already carries the Yvon–Takabayasi angle as an "angle zero for a pure electron state" but not the criterion that makes the equation linear; and the axial-current form of the massless equation, which the spinor bilinear reproduces.

One convention differs from the corpus and is flagged once, so that formulas are not misread between the two. The source works in the **Clifford bundle** $C\ell(M)$ with the metric $g=\mathrm{diag}(+1,-1,-1,-1)$, the convention the corpus itself adopts for its frame cells. Write $L_a\psi=a\psi$ and $R_b\psi=\psi b$ for the left and the right multiplication of a spinor $\psi$; the units are $e_t$, the identity of the algebra, and $\vec e_x,\vec e_y,\vec e_z$ with $\vec e_k^2=-1$. The corpus's five frame cells are $iR_{\vec e_x}=R_{i\vec e_x}$, $iL_{\vec e_k}R_{\vec e_y}=L_{i\vec e_k}R_{\vec e_y}$ and $-iR_{\vec e_z}=R_{-i\vec e_z}$.

The source's **volume element** is the product of the four generators,

$$
\omega=iR_{\vec e_x}\,iL_{\vec e_x}R_{\vec e_y}\,iL_{\vec e_y}R_{\vec e_y}\,iL_{\vec e_z}R_{\vec e_y}=R_{-\vec e_z},
$$

the **pseudoscalar**, which satisfies $\omega^2=-1$, and the source sets $i\equiv\omega$: the "$i$" of its electric–magnetic notation $F=\vec E+i\vec B$ is therefore the **duality operator**, the module representative of the corpus's central imaginary unit, and not a second imaginary number. Every $\exp(\omega\beta)$ below is the exponential of that cell, that is, a duality rotation.

The source's fixed bivector, the product $iL_{\vec e_y}R_{\vec e_y}\,iL_{\vec e_x}R_{\vec e_y}=-\vec e_z$, is the **spin plane**, the role played in the corpus's Dirac–Hestenes article by the fixed element $I\sigma_3$. It needs a left/right check, because its two readings are different cells: as the printed product of frame cells it is $L_{e_ye_x}R_{e_ye_y}=-L_{\vec e_z}$, a **left** multiplication, while the **right** multiplication by the same bivector is $R_{-\vec e_z}$, which is the volume element $\omega$ itself, since the biquaternion unit $-\vec e_z$ is the dictionary's pseudoscalar. The two cells differ on every element that does not commute with $\vec e_z$, and the spinorial equation is written below with the printed composition, the left one.

The even subalgebra $C\ell^+(M)$, in which the spinor $\psi$ lives, is the biquaternion algebra $\mathbb{B}$ under the corpus's dictionary. The source's route is nevertheless the **Clifford-bundle** one, and the corpus records it as a different technical road to the same structural equivalences, cross-referencing rather than merging.

## Maxwell's Equations in the Clifford Bundle

### The plane wave and the duality operator

The free equation $\partial F=0$ is solved by the plane wave

$$
F = f\,\exp(\omega kx),
$$

with $f$ a constant 2-form and $k$ the propagation vector. Applying $k$ on the left gives $kF=0$, and applying $k$ again gives $k^2F=0$, so the propagation vector is **null**,

$$
k^2=0 \quad\Longleftrightarrow\quad k_0=\pm|\vec k| .
$$

Multiplying $kF=0$ on the right by $F$ gives $F^2=0$: the plane wave has **null invariants**. Both facts are the standard ones, and the source's point in restating them is the contrast with what follows — the plane waves of the free equation sit on the special null case, and the source then exhibits solutions that do not.

The role of the volume element is worth one paragraph, because the source insists on it. Since $\omega^2=-1$, the exponential splits as $\exp(\omega kx)=\cos kx+\omega\sin kx$, so

$$
F = f\cos kx + \omega f\sin kx .
$$

Writing $F=\vec E+\omega\vec B$ and $f=\mathbf e$, this is $\vec E+\omega\vec B=\mathbf e\cos kx+\omega\mathbf e\sin kx$: the electric and magnetic parts are **out of phase by a quarter period**, and the "$i$" of the standard complex formulation is precisely the $\omega$ that produces that phase, not a formal device. The source calls this the "secret" that the complex notation hides, and it is the observation on which the rest of its plane-wave discussion is built. That $\omega$ is the duality operator is also why the **duality rotation** $F\mapsto \exp(\omega\beta)F$ of *Exercise: Duality Rotation and the Riemann–Silberstein Vector* appears below as the parameter that governs the non-linear equation.

### The Hertz potential

The solutions of the next two sections are generated by a **Hertz potential**. The source's theorem is that if a 2-form $\pi$ satisfies the wave equation $\partial^2\pi=0$ and the vector potential is taken as $A=-\delta\pi$ with $\delta$ the coderivative, then $F=\partial A$ solves the Maxwell equation $\partial F=0$. The proof is short — $\delta A=-\delta^2\pi=0$, so $F=dA$ and $\partial F=(d-\delta)(d-\delta)A=-(d\delta+\delta d)A=0$ since $d\delta\pi=-\delta d\pi$ follows from $\partial^2\pi=0$ — and it is the technical device that converts a scalar solution of the wave equation into an electromagnetic field with the desired properties.

## Subluminal Solutions

### The stationary solution

The source takes the Hertz potential to be $\pi=\Phi\,iL_{\vec e_x}R_{\vec e_y}\,iL_{\vec e_y}R_{\vec e_y}$ with the scalar part separated as

$$
\Phi(t',x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \varphi(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\,\exp(\omega\Omega t'),
$$

so that the wave equation becomes the Helmholtz equation $\nabla^2\varphi+\Omega^2\varphi=0$. The simplest solution is the spherical one $\varphi(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)=C\,\sin(\Omega r)/r$, and the resulting stationary field $F_0$ is **regular at the origin** and **vanishes at infinity** — a localised field configuration at rest in the adapted frame. Written in the electric–magnetic split $F_0=\vec E_0+\omega\vec B_0$ it is

$$
\vec E_0=-\vec W\sin\Omega t', \qquad \vec B_0=\vec W\cos\Omega t',
$$

with $\vec W(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$ a fixed vector field built from spherical harmonics and powers of $1/r$.

Three of its properties are the point of the construction. First, the invariant $I_1=\vec E_0^2-c^2\vec B_0^2$ and the pseudo-invariant $I_2=\vec E_0\cdot\vec B_0$ are **not zero**: $\vec E_0$ and $\vec B_0$ are both parallel to $\vec W$ and oscillate a quarter period apart, so $I_2=\vec E_0\cdot\vec B_0$ is generally non-zero while $I_1=-|\vec W|^2\cos 2\Omega t'$ oscillates between the two signs. The field is of the **generic electric–magnetic-parallel type**, not the null type, and it is a free solution of the source-free Maxwell equation that carries a **non-null** field. Second, the field is **not transverse**: the source shows by boosting the stationary solution to a moving subluminal one that the propagation vector is no longer orthogonal to the field, in contrast to the plane wave. That is why its construction matters to claims about longitudinal electromagnetic waves, for which the source cites Evans. Third, $\vec W$ satisfies the **Beltrami (force-free) equation**

$$
\mathrm{rot}\,\vec W = -\Omega\,\vec W,
$$

so that the configuration is a helical force-free field, the object that appears in plasma physics and in the earlier "force-free" literature the source cites. The energy integral of $F_0$ alone diverges, and the source notes that finite-energy wave packets over a distribution of frequencies can be formed instead.

### Purely electromagnetic particles

The subluminal solutions bear on a question older than the formalism. Einstein, following Poincaré and Ehrenfest, asked whether a **purely electromagnetic particle** can exist: a field configuration $F_p$ with current $J_p$ obeying $\partial F_p=J_p$ and the subsidiary condition $J_p\cdot F_p=0$. In vector form the condition reads $\rho_p\vec E_p=0$, $\vec j_p\cdot\vec E_p=0$, $\vec j_p\times\vec B_p=0$, and Einstein concluded that the only solution is $J_p=0$ — but, the source observes, only if $J_p$ is **time-like**. If $J_p$ is allowed to be **space-like** there is a frame in which $\rho_p=0$, and a solution with $\vec E_p\cdot\vec B_p=0$ and $\vec j_p=kC\,\vec B_p$ exists, with $k=\pm1$ a chirality. The connection with the section above is that the free stationary field $F_0$ can be **split** as a field plus a current, $\partial F_0=0$ being equivalent to $\partial F_p=J_p$ for a suitable space-like $J_p$; the free equation then models a standing purely electromagnetic particle. This is the source's route into the older programme of Waite, Barut and Zeni, which it cites; it is recorded here as a programme item, not as an established particle model.

## Superluminal Solutions: the X-Wave

The same Hertz-potential device produces **superluminal** solutions. The scalar seed is taken from the family of **X-waves**,

$$
\Phi_{X_n}(t',x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \exp(in\theta)\int_0^\infty B(k)\,J_n(k\rho\sin\eta)\,\exp(-k[a_0-i(z\cos\eta-t')])\,dk,
$$

with $\eta$ the **axicon angle** and $J_n$ the Bessel function. With $B(k)=a_0$ the integral is elementary and gives a **closed-form superluminal electromagnetic X-wave** (SEXW), a localised beam-like solution of the wave equation in which $z\cos\eta-t'$ replaces the plane-wave phase — the field pattern travels faster than $c$ along the axis while the individual wave fronts do not. The source treats these as valid solutions of the free Maxwell equation and points to Rodrigues and Lu for the physical devices that would generate them.

The superluminality must be read with the corpus's usual care, and the source's own phrasing invites the mistake. The X-wave is a **localised pattern** whose amplitude profile advances superluminally; this is the **pattern (or phase) speed** of a finite wave packet and is not a speed of energy, information or signal. A free-field solution with a superluminal pattern is not in conflict with causality, and the corpus records the claim in that sense only. The same construction yields superluminal solutions of the Weyl equation, which the source offers as a possible interpretation of neutrino puzzles; that part is speculative and is not carried.

## The Field as a Spinor Bilinear

### Two constraints, six degrees of freedom

The structural heart of the paper is the representation of the field as a **spinor bilinear**. With $\psi$ a Dirac–Hestenes spinor, an element of the even subalgebra $C\ell^+(M)$, the field is written

$$
\boxed{\;F = -\psi\,\vec e_z\,\psi^{\mathrm{c}}\;}
$$

where $\psi^{\mathrm{c}}$ is the **reverse** of $\psi$. The counting matters: a general even spinor has **eight** real degrees of freedom, while the field $F$ has **six**, so two constraints must be imposed on $\psi$ for the correspondence to be one-to-one up to a normalisation. The source chooses them as $\partial\cdot j=0$ and $\partial\cdot g=0$, where $j$ and $g$ are the vector and axial-vector currents read off the derivatives of $\psi$. This is the same eight-versus-six counting the corpus records in its Dirac–Hestenes article, which reaches it through the parameters of the rotor decomposition; the constraints are the source's extra data.

Substituting $F=-\psi\vec e_z\psi^{\mathrm{c}}$ into the generalised Maxwell equation $\partial F=J$ and using the canonical decomposition $\psi=\rho^{1/2}\exp(\omega\beta/2)R$ — the rotor $R$, the density $\rho$, and the **Takabayasi angle** $\beta$ — turns the field equation into a spinorial equation for $\psi$:

$$
\begin{aligned}
\partial\psi\;iL_{\vec e_y}R_{\vec e_y}\,iL_{\vec e_x}R_{\vec e_y}
&=\lambda\,\psi\,iR_{\vec e_x}\exp(\omega\beta)+\omega\kappa\,\psi\,iR_{\vec e_x}\exp(\omega\beta)\\
&\quad+\frac{1}{2\rho}\exp(\omega\beta)J\,\psi ,
\end{aligned}
$$

with $\lambda$ and $\kappa$ the two real scalars built from the bivector $\Omega=\sum_\mu g_{\mu\mu}\,v_\mu\Omega_\mu$. The source also prints the pair as $\Lambda$ and $K$ once the phase is factored; one spelling, $\lambda$ and $\kappa$, is kept here.

**Three checks, because this display is where a transcription of the source goes wrong.** Each is a one-line computation, and each decides a sign or a side.

*The left side is one cell, not two.* Frame cells compose by $L_aR_bL_cR_d=L_{ac}R_{db}$, so

$$
iL_{\vec e_y}R_{\vec e_y}\,iL_{\vec e_x}R_{\vec e_y}=L_{e_ye_x}R_{e_ye_y}=-L_{\vec e_z},
$$

the **left** multiplication by the spin-plane bivector. The **right** multiplication by the same bivector is a different cell, the pseudoscalar $R_{-\vec e_z}=\omega$, and $L_{-\vec e_z}\neq R_{-\vec e_z}$ on every element that does not commute with $\vec e_z$. The display keeps the printed composition, the left one. The choice is not cosmetic: with the right-hand cell the two sides of the linearisation below come out carrying opposite half-rotations and nothing cancels, so the printed side is the one the argument needs.

*The phase is the pseudoscalar cell.* $\exp(\omega\beta)$ is the exponential of $R_{-\vec e_z}$, that is, right multiplication by $e^{-\beta\vec e_z}$: a duality rotation of angle $\beta$, the operator the source writes $e^{\beta\omega}$ with its $\omega$ the volume element. Two products with it are needed. It commutes with every right multiplication, hence with the phase cell $\exp(\omega\beta/2)$ of the decomposition, because $R_aR_b=R_{ba}$ and $\vec e_z$ commutes with itself. And it **anticommutes** with $iR_{\vec e_x}$, because $\vec e_x\vec e_z=-\vec e_z\vec e_x$:

$$
\omega\,iR_{\vec e_x}=-iR_{\vec e_x}\,\omega .
$$

*The phase sits on all three terms.* The source prints it once, on the current; carried, it stands to the right of $iR_{\vec e_x}$ in the two scalar terms, which is where the next subsection cancels it. Attached to the current alone it would leave the two sides of the linearised equation carrying opposite half-rotations, and nothing would cancel.

The free case $J=0$ is therefore

$$
\partial\psi\;iL_{\vec e_y}R_{\vec e_y}\,iL_{\vec e_x}R_{\vec e_y}
=\left(\lambda+\omega\kappa\right)\psi\,iR_{\vec e_x}\exp(\omega\beta),
$$

which has the shape of the Dirac–Hestenes equation but with **two** scalar coefficients instead of one mass. The two-constraint condition forces their ratio to a constant, and after a duality rotation by that constant the relation becomes $\kappa/\lambda=\tan\beta$, i.e. the two coefficients are the single mass times the cosine and the sine of the Takabayasi angle.

### The non-linear Dirac–Hestenes equation

The non-linearity is exactly the factor $\exp(\omega\beta)$: when $\beta$ is **constant** the factor is a constant duality rotation and the equation becomes linear. Concretely, put $\psi=\varphi\exp(\omega\beta/2)$ with $\varphi=\sqrt\rho\,R$. The phase of the decomposition passes $iR_{\vec e_x}$ with a change of sign, $\exp(\omega\beta/2)iR_{\vec e_x}=iR_{\vec e_x}\exp(-\omega\beta/2)$ — the anticommutation above — and then meets the full rotation $\exp(\omega\beta)$ of the equation, so that each side is left with the **same** half rotation on the right:

$$
\partial\psi\;iL_{\vec e_y}R_{\vec e_y}\,iL_{\vec e_x}R_{\vec e_y}
=\Bigl(\partial\varphi\;iL_{\vec e_y}R_{\vec e_y}\,iL_{\vec e_x}R_{\vec e_y}\Bigr)\exp(\omega\beta/2),
$$

$$
\left(\lambda+\omega\kappa\right)\psi\,iR_{\vec e_x}\exp(\omega\beta)
=\left(\lambda+\omega\kappa\right)\varphi\,iR_{\vec e_x}\exp(\omega\beta/2).
$$

Cancelling that common right factor, and with the combination $\lambda+\omega\kappa$ reduced by the constant duality rotation to the real $m$, the free equation reduces to the **linear Dirac–Hestenes equation**

$$
\boxed{\;\partial\varphi\;iL_{\vec e_y}R_{\vec e_y}\,iL_{\vec e_x}R_{\vec e_y}=m\,\varphi\,iR_{\vec e_x}\;}
$$

with $m$ identified as the mass. The criterion is therefore sharp, and it is the source's key structural statement: **the Maxwell equation for the field is equivalent to the linear Dirac equation for the spinor exactly when the Takabayasi angle is constant**, and the particular values $\beta=0$ and $\beta=\pi$ select the electron and the positron. The plane-wave solutions of the corpus's own Dirac exercise have constant $\beta$ — zero for the positive-energy ones — so they sit on precisely this linearisable class, and the source supplies the general reason why.

Two consequences the source draws from the same algebra are worth recording. The first is a **superselection rule**: the superposition principle survives only for spinors of the same $\beta$, because $\exp(\omega\beta)$ is not linear across different angles; the source reads this as particles and antiparticles forming separate superselection sectors. The second is the **momentum relation**. Multiplying the non-linear equation by $\psi^{-1}$ gives $p=mv$ for every angle $\beta$, whereas the linear Dirac–Hestenes equation gives $p=\exp(\omega\beta)mv$, which for $p$ and $v$ real forces $\beta=0$ or $\beta=\pi$ and thus the choice between positive and negative energy. In the non-linear interpretation there is no negative-energy problem to interpret: the equation gives $p=mv$ throughout, and the source proposes to reinterpret the energy projector as a **particle projector** instead.

### The projection operators

The framework of projectors is what carries the mass spectrum, so it is stated precisely. The energy projectors of the linear theory are the two minimal right ideals of the even subalgebra,

$$
\Lambda_\pm(\psi) = \tfrac12\left(\psi \pm \psi\,i\vec e_x\right)=\psi\,\tfrac12\left(1\pm i\vec e_x\right),
$$

which the source writes with its frame cell on both sides, $\tfrac12(\psi\pm iR_{\vec e_x}\psi\,iR_{\vec e_x})$. The two forms are not the same expression. The source introduces the one-parameter family

$$
\Lambda_\beta(\psi) = \tfrac12\left(\psi + \exp(\omega\beta)iR_{\vec e_x}\psi\,iR_{\vec e_x}\right),
$$

which reduces to $\Lambda_+$ at $\beta=0$ and to $\Lambda_-$ at $\beta=\pi$. **The printed composition collapses, and the correction matters for the mass spectrum.** The cell $iR_{\vec e_x}$ multiplies on the right by $i\vec e_x$, and $(i\vec e_x)^2=+1$; applied on both sides it is therefore an involution, $\psi\mapsto iR_{\vec e_x}\psi\,iR_{\vec e_x}=\psi$ on the even subalgebra, so the family reads

$$
\Lambda_\beta(\psi)=\tfrac12\left(1+\exp(\omega\beta)\right)\psi=\cos\tfrac{\beta}{2}\,\exp\!\left(\tfrac{\omega\beta}{2}\right)\psi ,
$$

a duality rotation with the scalar weight $\cos(\beta/2)$. It is $\psi$ at $\beta=0$ and $0$ at $\beta=\pi$, and those are exactly the printed endpoints, $\Lambda_+=\psi$ and $\Lambda_-=0$; the interior is a rotation of the field rather than a projection of it, so the family interpolates between the two projectors instead of being one. The projector property needs the cell once, not twice: with $T\psi=\psi\,i\vec e_x$ one has $T^2=I_4$ and $\Lambda=\tfrac12(\psi+T\psi)=\tfrac12\psi(1+i\vec e_x)$ is idempotent, since $(1+i\vec e_x)^2=2(1+i\vec e_x)$. In that reading the Hestenes projectors are the two minimal right ideals of the even subalgebra, $\Lambda_+$ and $\Lambda_-$ separate the two spin planes, and the shift $\beta\mapsto\beta+\pi$ negates the cell and exchanges them:

$$
\Lambda_\beta + \Lambda_{\beta+\pi} = \psi, \qquad \Lambda_\beta\,\Lambda_{\beta+\pi} = 0 .
$$

The corpus records the printed display, the collapse of the two-sided composition, and the one-sided form that restores the projection; the source's own relation reads $\Lambda_\beta=\Lambda_{\beta+\pi}$, which is the degenerate statement this replacement removes.

## Maxwell and the Massless Dirac Equation

The equivalence runs in the other direction as well, and that direction carries the axial current. The **massless** Dirac equation $\partial\psi=0$ for $\psi$ in the even subalgebra is equivalent to a **generalised Maxwell equation**

$$
\partial F = J_e - \omega J_m = J ,
$$

with both an electric current $J_e$ and an **axial (magnetic) current** $-\omega J_m$. For the positive-parity eigenstate $\psi^\uparrow$ the electric current vanishes, $j_e=0$, and the equivalent Maxwell equation reads

$$
\boxed{\;\partial F^\uparrow = -\omega J_m\;}
$$

that is, a **massless Dirac field is a Maxwell field with a magnetic current and no electric current**. The mechanism is the parity split: the source shows that $\psi^\uparrow$ decouples into a pair of Weyl fields of opposite charge, $\partial\psi^\uparrow_+ + g\omega B\psi^\uparrow_+=0$ and $\partial\psi^\uparrow_- - g\omega B\psi^\uparrow_-=0$, so that a single $\psi^\uparrow$ coupled to a potential describes a particle of charge $+g$ and a particle of charge $-g$ — which the source reads as a pair of opposite charges. A word is needed here on why the source writes **one** Dirac equation where the corpus writes **two**. The corpus's equation is the chiral pair $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$ and $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$: the left and the right multiplications are separate operators, one per side, and the mass term is what couples the two chiralities. The source works with a single operator on a spinor that carries both chiralities, and its equation is the **massless** member of the pair, where the two sides decouple and the chirality labels may be dropped. The two presentations agree on the massless content and diverge as soon as a mass is present, which is why the spinorial equation of the previous section carries two scalar coefficients rather than one.

This is a further route in the corpus by which a magnetic current appears in a spinorial or quaternionic reformulation of Maxwell's equations. The source adds one structural remark that the corpus records as a curiosity: the Tetrode energy–momentum one-form of the non-linear equation is a kind of **square root** of the Maxwell energy–momentum one-form $S_\mu=\tfrac12 F\,iL_{e_\mu}R_{e_{\nu(\mu)}} F$.

Here $iL_{e_\mu}R_{e_{\nu(\mu)}}$ is the generator cell of the coordinate $x_\mu$, with $\nu(t)=x$ and $\nu(k)=y$.

## Status, Contrasts, and Boundaries

What the programme establishes is the **structural half**. That the free Maxwell equation has free solutions with non-null invariants is true and is a genuine correction to the reflex that "free electromagnetic waves are null transverse plane waves"; the classification of *The Field-Strength Biquaternion and Its Invariants* admits such fields but does not exhibit them, and the subluminal construction here supplies the missing example. That the field is a spinor bilinear and that the Maxwell equation for the field is a non-linear Dirac–Hestenes equation which linearises precisely at constant Takabayasi angle is likewise a clean structural statement, and it explains from a second direction why the corpus's plane-wave Dirac solutions are simple. That the massless Dirac equation is a Maxwell equation with an axial current is the third, and it reproduces the corpus's axial-current form.

The boundaries are these. The Clifford-bundle route is an **external formalism**; the corpus's own treatment is the biquaternion one, and the two are related through the even-subalgebra dictionary rather than identified. The "superluminal" of the X-wave is a pattern speed of a localised solution, not a signalling speed, and must not be read otherwise. The **purely electromagnetic particle** is a programme item revived from Einstein and Waite, not a constructed particle. And the mass spectrum is an algebraic proposal whose extension to a full spectrum is a hypothesis, tested above against the two masses it does reproduce.

## Summary

The programme of Rodrigues and Vaz works in the Clifford bundle and presses the free Maxwell equation $\partial F=0$ in two directions. It exhibits **subluminal and superluminal undistorted progressive wave solutions with non-null invariants and longitudinal components**, built from a Hertz potential and a spherical Helmholtz solution, and connects the free stationary solution to the old question of purely electromagnetic particles. It represents the field as the **spinor bilinear** $F=-\psi\vec e_z\psi^{\mathrm{c}}$ and shows the Maxwell equation to be a **non-linear Dirac–Hestenes equation**, with the **Takabayasi angle** as the knob: constant $\beta$ makes it linear, $0$ and $\pi$ make it the electron and positron, $\pi/2$ and $3\pi/2$ make it the muon. In the other direction the **massless Dirac equation is a Maxwell equation with an axial (magnetic) current**, which is the route by which a magnetic current appears.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $C\ell(M)$ | Clifford bundle of differential forms over Minkowski spacetime |
| $C\ell^+(M)$ | Its even subalgebra; the biquaternion algebra $\mathbb{B}$ under the corpus's dictionary |
| $g=\mathrm{diag}(+1,-1,-1,-1)$ | Metric; the corpus's frame-cell convention |
| $iL_{e_\mu}R_{e_{\nu(\mu)}}$ | Frame cells, $iR_{\vec e_x}=R_{i\vec e_x}$ and $iL_{\vec e_k}R_{\vec e_y}=L_{i\vec e_k}R_{\vec e_y}$ |
| $L_a$, $R_b$ | Left and right multiplication of a spinor, $L_a\psi=a\psi$ and $R_b\psi=\psi b$ |
| $\omega=iR_{\vec e_x}\,iL_{\vec e_x}R_{\vec e_y}\,iL_{\vec e_y}R_{\vec e_y}\,iL_{\vec e_z}R_{\vec e_y}=R_{-\vec e_z}$ | Volume element, the pseudoscalar; $\omega^2=-1$; the source's "$i$", which the corpus identifies with its central imaginary unit |
| $iL_{\vec e_y}R_{\vec e_y}\,iL_{\vec e_x}R_{\vec e_y}=L_{e_ye_x}R_{e_ye_y}=-L_{\vec e_z}$ | Fixed spin-plane bivector; the printed product is the left multiplication, the right one is the cell $\omega$ |
| $\partial=iR_{\vec e_x}\partial/\partial x_0-\sum_k iL_{\vec e_k}R_{\vec e_y}\partial/\partial x_k$ | Dirac operator, a cell acting on the spinor; $\delta$ the coderivative, $d$ the exterior derivative |
| $F$, $F_0$, $F_e$, $F^\uparrow$ | Field 2-form; the stationary subluminal solution; the electron field; the positive-parity field |
| $\pi$, $A$ | Hertz potential; vector potential, $A=-\delta\pi$ |
| $f$, $k$, $x$ | Constant 2-form; propagation vector ($k^2=0$); position |
| $\vec E_0,\vec B_0,\vec W$ | Fields of the stationary solution and their common vector, $\mathrm{rot}\,\vec W=-\Omega\vec W$ |
| $\Omega$ | Intrinsic frequency of the subluminal solution ($\Omega$ in the Helmholtz equation $\nabla^2\varphi+\Omega^2\varphi=0$) |
| $\Phi_{X_n}$, $\eta$ | Scalar X-wave seed; axicon angle |
| $\psi$, $\psi^{\mathrm{c}}$ | Dirac–Hestenes spinor (even element) and its reverse |
| $\psi=\rho^{1/2}\exp(\omega\beta/2)R$ | Canonical decomposition: rotor $R$, density $\rho$, angle $\beta$ |
| $\beta$ | Takabayasi (Yvon–Takabayasi) angle; $0,\pi$ electron/positron, $\pi/2,3\pi/2$ muon/antimuon |
| $j$, $g$, $J=J_e-\omega J_m$ | Vector current, axial current, total current with electric and magnetic parts |
| $\Lambda_\pm,\ \Lambda_\beta$ | Energy projectors $\tfrac12\psi(1\pm i\vec e_x)$, the minimal right ideals of the even subalgebra; the one-parameter family of the source and its collapse |
| $S=-\tfrac12\psi\vec e_z\psi^{-1}$ | Bivector of the canonical analysis; $S_\mu=\tfrac12 F\,iL_{e_\mu}R_{e_{\nu(\mu)}} F$ the Maxwell energy–momentum |
| $\lambda,\kappa$ | Scalar coefficients of the spinorial Maxwell equation; the source's $\Lambda$ and $K$ are the same pair after the phase is factored |

## Further Reading

- Waldyr Alves Rodrigues Jr. and Jayme Vaz Jr., "Subluminal and Superluminal Electromagnetic Waves and the Lepton Mass Spectrum", arXiv:hep-th/9607231 (1996), the source of this article.
- J. Vaz Jr. and W. A. Rodrigues Jr., "Maxwell and Dirac Theories as an Already Unified Theory", *Advances in Applied Clifford Algebras* (1995), for the equivalence of the Maxwell and massless Dirac equations underlying the spinor representation.
- W. A. Rodrigues Jr. and J.-Y. Lu, "On the Existence of Undistorted Progressive Waves (UPWs) of Arbitrary Speeds $0\le|v|\le\infty$ in Nature" (IMECC-UNICAMP, 1996), for the UPW and X-wave family and their generation.
- J.-y. Lu and J. F. Greenleaf, "Nondiffracting X waves", *IEEE Trans. Ultrason. Ferroelectr. Freq. Control* **39** (1992) 19–31, for the scalar X-wave solutions used as Hertz potentials.
- D. Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), and D. Hestenes and G. Sobczyk, *Clifford Algebra to Geometric Calculus* (Reidel, 1987), for the spacetime-algebra formulation and the bilinear covariants.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the projector operators and the spinor classification.
- M. W. Evans, "The present status of the Einstein–de Broglie–Vigier model", *Foundations of Physics* **24** (1994) 1971, cited by the source for evidence of longitudinal electromagnetic fields.

## Appendix — The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5=-iL_{e_t}R_{\vec e_z} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The article's frame is the source's: its volume element, the product $\gamma_0\gamma_1\gamma_2\gamma_3$, is the pseudoscalar $\omega=-i\gamma_5$ of this dictionary, the symbol the body writes; its fixed bivector is $\gamma_2\gamma_1=-\vec e_z$, the source's $\gamma_{21}$.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=g_{ac}\gamma_d-g_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4g_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}\bigr).
$$
The four contraction sums are frame statements, because a cell's square is. In the Euclidean frame, where every cell squares to $+I_4$, they are $4I_4$, $-2\gamma_\alpha$, $4\delta_{\alpha\beta}I_4$ and $-2\gamma_\delta\gamma_\beta\gamma_\alpha$. In the $\mathbb{M}_-$ frame the metric enters and $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$.
