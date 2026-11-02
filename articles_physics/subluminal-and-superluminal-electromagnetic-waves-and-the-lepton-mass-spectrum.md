# __Subluminal and Superluminal Electromagnetic Waves in Biquaternionic Form__

## Introduction

This article records an external programme, that of Waldyr Alves Rodrigues Jr. and Jayme Vaz Jr. as presented in *Subluminal and Superluminal Electromagnetic Waves and the Lepton Mass Spectrum* (arXiv:hep-th/9607231, 1996). It works in the **Clifford bundle of differential forms** $C\ell(M)$ and studies the single equation

$$
\partial F = 0
$$

for a 2-form field $F$, together with the spinor sector of the same algebra. From that starting point it claims two things. The first is that the free Maxwell equation has **subluminal and superluminal** solutions that are **undistorted progressive waves** and carry **non-null field invariants** and longitudinal field components — a family larger than the transverse plane waves of the textbook account. The second is that, writing the field as a **spinor bilinear** $F=-\psi\vec e_z\psi^{\mathrm{c}}$, the free Maxwell equation is equivalent to a **non-linear Dirac–Hestenes equation** for $\psi$, and that this non-linear equation **linearises** exactly when the **Takabayasi angle** $\beta$ is constant; the same section shows the massless Dirac equation to be a Maxwell equation with an **axial (magnetic) current**.

The corpus records the programme and does not endorse it. Its value to this corpus is twofold. The structural part — the spinor representation of the field, the criterion that selects the linear equation, and the axial-current form of the massless equation — is **rigorous and checkable**, and it bears directly on questions the corpus states elsewhere: the invariant classification of *The Field-Strength Biquaternion and Its Invariants*, which classifies the field by its two invariants and notes that they are not conserved by the free evolution, but does not exhibit the family of free solutions that carry non-null invariants; the Dirac–Hestenes formulation of *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form*, which already carries the Yvon–Takabayasi angle as an "angle zero for a pure electron state" but not the criterion that makes the equation linear; and the axial-current form of the massless equation, which the spinor bilinear reproduces.

One convention differs from the corpus and is flagged once, so that formulas are not misread between the two. The source works in the **Clifford bundle** $C\ell(M)$ with the metric $g=\mathrm{diag}(+1,-1,-1,-1)$, the convention the corpus itself adopts for its frame cells. Write $L_a\psi=a\psi$ and $R_b\psi=\psi b$ for the left and the right multiplication of a spinor $\psi$; the units are $e_t$, the identity of the algebra, and $\vec e_x,\vec e_y,\vec e_z$ with $\vec e_k^2=-1$. The corpus's five frame cells are $iR_{e_x}=R_{i\vec e_x}$, $iL_{e_k}R_{e_y}=L_{i\vec e_k}R_{\vec e_y}$ and $-iR_{e_z}=R_{-i\vec e_z}$. The source's **volume element** is the product of the four generators, $\omega=iR_{e_x}\,iL_{e_x}R_{e_y}\,iL_{e_y}R_{e_y}\,iL_{e_z}R_{e_y}=R_{-\vec e_z}$, the **pseudoscalar**, which satisfies $\omega^2=-1$, and it sets $i\equiv\omega$: the source's "$i$" in the electric–magnetic notation $F=\vec E+i\vec B$ is therefore the **duality operator**, the module representative of the corpus's central imaginary unit, and not a second imaginary number. The source's fixed bivector, the product $iL_{e_y}R_{e_y}\,iL_{e_x}R_{e_y}=-\vec e_z$, is the **spin plane** that multiplies the spinor on the right, the role played in the corpus's Dirac–Hestenes article by the fixed element $I\sigma_3$. The even subalgebra $C\ell^+(M)$, in which the spinor $\psi$ lives, is the biquaternion algebra $\mathbb{B}$ under the corpus's dictionary; the source's route is nevertheless the **Clifford-bundle** one, and the corpus records it as a different technical road to the same structural equivalences, cross-referencing rather than merging.

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

The source takes the Hertz potential to be $\pi=\Phi\,iL_{e_x}R_{e_y}\,iL_{e_y}R_{e_y}$ with the scalar part separated as

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
\partial\psi\,iL_{e_y}R_{e_y}\,iL_{e_x}R_{e_y} = \frac{\exp(\omega\beta)}{2\rho}\,J\,\psi + \lambda\,\psi\,iR_{e_x} + \omega\kappa\,\psi\,iR_{e_x} ,
$$

with $\lambda$ and $\kappa$ the two scalars built from the bivector $\Omega=\sum_\mu g_{\mu\mu}\,v_\mu\Omega_\mu$. Its free case $J=0$ is

$$
\partial\psi\,iL_{e_y}R_{e_y}\,iL_{e_x}R_{e_y} = \lambda\,\psi\,iR_{e_x} + \omega\kappa\,\psi\,iR_{e_x} ,
$$

which has the shape of the Dirac–Hestenes equation but with **two** scalar coefficients instead of one mass. The two-constraint condition forces their ratio to a constant, and after a duality rotation by that constant the relation becomes $\kappa/\Lambda=\tan\beta$, i.e. the two coefficients are the single mass times the cosine and sine of the Takabayasi angle.

### The non-linear Dirac–Hestenes equation

Written in full, the equation for $\psi$ is a **non-linear Dirac–Hestenes equation**

$$
\partial\psi\,iL_{e_y}R_{e_y}\,iL_{e_x}R_{e_y} = \Lambda\,\psi\,iR_{e_x} \exp(\beta\omega) + \omega K\,\psi\,iR_{e_x} \exp(\beta\omega) + \frac{1}{2\rho}\,\exp(\beta\omega) J\,\psi .
$$

The non-linearity is exactly the factor $\exp(\beta\omega)$: when $\beta$ is **constant** the factor is a constant duality rotation and the equation becomes linear. Concretely, with $\psi=\varphi\,\exp(\omega\beta/2)$ and $\varphi=\sqrt{\rho}\,R$, the phase factor on the right is cancelled by the phase factor of the decomposition — $\exp(\omega\beta/2)iR_{e_x}=iR_{e_x}\exp(-\omega\beta/2)$ because $\omega$ anticommutes with $iR_{e_x}$ — and the free equation reduces to the **linear Dirac–Hestenes equation**

$$
\boxed{\;\partial\varphi\,iL_{e_y}R_{e_y}\,iL_{e_x}R_{e_y} = m\,\varphi\,iR_{e_x}\;}
$$

with $\Lambda=m$ identified as the mass. The criterion is therefore sharp, and it is the source's key structural statement: **the Maxwell equation for the field is equivalent to the linear Dirac equation for the spinor exactly when the Takabayasi angle is constant**, and the particular values $\beta=0$ and $\beta=\pi$ select the electron and the positron. The plane-wave solutions of the corpus's own Dirac exercise have constant $\beta$ — zero for the positive-energy ones — so they sit on precisely this linearisable class, and the source supplies the general reason why.

Two consequences the source draws from the same algebra are worth recording. The first is a **superselection rule**: the superposition principle survives only for spinors of the same $\beta$, because $\exp(\beta\omega)$ is not linear across different angles; the source reads this as particles and antiparticles forming separate superselection sectors. The second is the **momentum relation**. Multiplying the non-linear equation by $\psi^{-1}$ gives $p=mv$ for every angle $\beta$, whereas the linear Dirac–Hestenes equation gives $p=\exp(\beta\omega)mv$, which for $p$ and $v$ real forces $\beta=0$ or $\beta=\pi$ and thus the choice between positive and negative energy. In the non-linear interpretation there is no negative-energy problem to interpret: the equation gives $p=mv$ throughout, and the source proposes to reinterpret the energy projector as a **particle projector** instead.

### The projection operators

The framework of projectors is what carries the mass spectrum, so it is stated precisely. The energy projector of the linear theory is

$$
\Lambda_\pm(\psi) = \tfrac12\left(\psi \pm iR_{e_x}\psi\,iR_{e_x}\right),
$$

and the source introduces the one-parameter family

$$
\Lambda_\beta(\psi) = \tfrac12\left(\psi + \exp(\omega\beta)iR_{e_x}\psi\,iR_{e_x}\right),
$$

which reduces to $\Lambda_+$ at $\beta=0$ and to $\Lambda_-$ at $\beta=\pi$. It is a projector for every $\beta$. The reason is a single identity: the map $\psi\mapsto \exp(\omega\beta)iR_{e_x}\psi\,iR_{e_x}$ squares to the identity, because $\omega$ anticommutes with $iR_{e_x}$ and $(iR_{e_x})^{2}=1$, so that $\tfrac12(1+T)$ is a projector whenever $T^2=1$. The shift $\beta\mapsto\beta+\pi$ negates $T$ and therefore exchanges the projector with its complement:

$$
\Lambda_\beta + \Lambda_{\beta+\pi} = 1, \qquad \Lambda_\beta\,\Lambda_{\beta+\pi} = 0 .
$$

This is the projector statement the next section uses, and it is the corrected form of the relation printed in the source (which reads $\Lambda_\beta=\Lambda_{\beta+\pi}$; see the companion `.context` for the check).

## Maxwell and the Massless Dirac Equation

The equivalence runs in the other direction as well, and that direction carries the axial current. The **massless** Dirac equation $\partial\psi=0$ for $\psi$ in the even subalgebra is equivalent to a **generalised Maxwell equation**

$$
\partial F = J_e - \omega J_m = J ,
$$

with both an electric current $J_e$ and an **axial (magnetic) current** $-\omega J_m$. For the positive-parity eigenstate $\psi^\uparrow$ the electric current vanishes, $j_e=0$, and the equivalent Maxwell equation reads

$$
\boxed{\;\partial F^\uparrow = -\omega J_m\;}
$$

that is, a **massless Dirac field is a Maxwell field with a magnetic current and no electric current**. The mechanism is the parity split: the source shows that $\psi^\uparrow$ decouples into a pair of Weyl fields of opposite charge, $\partial\psi^\uparrow_+ + g\omega B\psi^\uparrow_+=0$ and $\partial\psi^\uparrow_- - g\omega B\psi^\uparrow_-=0$, so that a single $\psi^\uparrow$ coupled to a potential describes a particle of charge $+g$ and a particle of charge $-g$ — which the source reads as a pair of opposite charges. This is a further route in the corpus by which a magnetic current appears in a spinorial or quaternionic reformulation of Maxwell's equations. The source adds one structural remark that the corpus records as a curiosity: the Tetrode energy–momentum one-form of the non-linear equation is a kind of **square root** of the Maxwell energy–momentum one-form $S_\mu=\tfrac12 FiL_{e_\mu}R_{e_{\nu(\mu)}} F$.

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
| $iL_{e_\mu}R_{e_{\nu(\mu)}}$ | Frame cells, $iR_{e_x}=R_{i\vec e_x}$ and $iL_{e_k}R_{e_y}=L_{i\vec e_k}R_{\vec e_y}$ |
| $L_a$, $R_b$ | Left and right multiplication of a spinor, $L_a\psi=a\psi$ and $R_b\psi=\psi b$ |
| $\omega=iR_{e_x}\,iL_{e_x}R_{e_y}\,iL_{e_y}R_{e_y}\,iL_{e_z}R_{e_y}=R_{-\vec e_z}$ | Volume element, the pseudoscalar; $\omega^2=-1$; the source's "$i$", which the corpus identifies with its central imaginary unit |
| $iL_{e_y}R_{e_y}\,iL_{e_x}R_{e_y}=-\vec e_z$ | Fixed spin-plane bivector, multiplying the spinor on the right |
| $\partial=iR_{e_x}\partial/\partial x_0-\sum_k iL_{e_k}R_{e_y}\partial/\partial x_k$ | Dirac operator, a cell acting on the spinor; $\delta$ the coderivative, $d$ the exterior derivative |
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
| $\Lambda_\pm,\ \Lambda_\beta$ | Energy projector $\tfrac12(\psi\pm\,iR_{e_x}\psi\,iR_{e_x})$; one-parameter projector family |
| $S=-\tfrac12\psi\vec e_z\psi^{-1}$ | Bivector of the canonical analysis; $S_\mu=\tfrac12 FiL_{e_\mu}R_{e_{\nu(\mu)}} F$ the Maxwell energy–momentum |
| $\lambda,\kappa,\Lambda,K$ | Scalar coefficients of the spinorial Maxwell and non-linear equations |

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
\gamma_0=iL_tR_x,\quad \gamma_1=iL_xR_y,\quad \gamma_2=iL_yR_y,\quad \gamma_3=iL_zR_y,\quad \gamma_5=-iL_tR_z .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The article's frame is the source's: its volume element, the product $\gamma_0\gamma_1\gamma_2\gamma_3$, is the pseudoscalar $\omega=-i\gamma_5$ of this dictionary, the symbol the body writes; its fixed bivector is $\gamma_2\gamma_1=-\vec e_z$, the source's $\gamma_{21}$.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.
