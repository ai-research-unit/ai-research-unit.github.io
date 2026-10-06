# __Electromagnetism in Media — The Local Complex Structure at Work__

## Introduction

Maxwell's equations in a material medium are usually introduced as a small modification of the vacuum equations: replace $\epsilon_0$ and $\mu_0$ by the permittivity $\epsilon$ and the permeability $\mu$ of the medium, and read off the consequences. In the biquaternionic formulation the emphasis is reversed. The medium is the general case and the vacuum is its limit, because the complex structure of the algebra is **local**. The material subspace $\mathbb{M}_-$ is coordinatised by $(ict,\,x,\,y,\,z)$, and the factor $i$ that marks the temporal direction is paired with the **speed of light in the medium**,
$$
c=\frac{1}{\sqrt{\epsilon\mu}},
$$
a property of the medium at each point rather than a constant of nature. The scalar imaginary $i$ is fixed by the algebra; the real scale attached to the imaginary time axis is supplied by the medium. This article develops electromagnetism in a medium with that reading in view.

The declared parent of this article is *The Field-Strength Biquaternion and Its Invariants*, which has fixed the canonical objects: the field-strength biquaternion
$$
\tilde{F}=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H},
$$
the electric and magnetic fields $\mathbf{E}$ and $\mathbf{H}$, the magnetic induction $\mathbf{B}=\mu\mathbf{H}$, the medium speed $c=1/\sqrt{\epsilon\mu}$, the Riemann–Silberstein vector $\mathbf{V}=\mathbf{E}+ic\mathbf{B}$, the invariants $I_1=\mathbf{E}^2-c^2\mathbf{B}^2$ and $I_2=\mathbf{E}\cdot\mathbf{B}$, and the energy density $W$ and Poynting vector $\mathbf{S}$. **Nothing in this list is redefined here.** The article fixes the conventions specific to a medium — the two medium parameters, the impedance, the dispersive data, and the boundary data — in enough detail that the later exercise on plane-wave propagation in a medium is a direct application of the objects fixed below.

The remaining conventions are those of the read-list articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ satisfying $e_k^2=-e_0$, and scalar imaginary $i$ commuting with the quaternion units. The two complementary four-dimensional real subspaces are $\mathbb{M}_-$ (anti-Hermitian: imaginary scalar, real vector) and $\mathbb{M}_+$ (Hermitian: real scalar, imaginary vector), with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$; the real-quaternion subspace is $\mathbb{H}_{\mathbb{B}}$ and the scalar subspace is $\mathbb{C}_{\mathbb{B}}$. The biquaternionic gradient and its quaternion conjugate are
$$
\tilde{\nabla}=e_0\,\partial_{ict}+e_1\,\partial_x+e_2\,\partial_y+e_3\,\partial_z,
\qquad
\tilde{\nabla}^{\natural}=e_0\,\partial_{ict}-e_1\,\partial_x-e_2\,\partial_y-e_3\,\partial_z,
$$
and the d'Alembertian is $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}$. Throughout, $c$ denotes the speed of light **in the medium** and $c_0$ the vacuum speed; the divergence and curl are written $\mathrm{div}$ and $\mathrm{rot}$.

## Constitutive Relations and the Two Parameters of a Medium

In a linear, isotropic medium the fields are related by the constitutive relations
$$
\mathbf{D}=\epsilon\,\mathbf{E},
\qquad
\mathbf{B}=\mu\,\mathbf{H},
$$
where $\mathbf{E}$ is the electric field, $\mathbf{H}$ the magnetic field, $\mathbf{D}$ the electric displacement and $\mathbf{B}$ the magnetic induction. These relations are inherited unchanged from the Maxwell article. The free charge and current densities $\rho$ and $\mathbf{J}$ obey the conservation law
$$
\mathrm{div}\,\mathbf{J}+\frac{\partial\rho}{\partial t}=0,
$$
which is the integrability condition of the Maxwell system and reappears below as a condition on the biquaternionic source.

For a homogeneous medium the two constants $\epsilon$ and $\mu$ combine into two quantities of independent physical meaning. The first is the wave speed
$$
c=\frac{1}{\sqrt{\epsilon\mu}},
$$
and the second is the wave impedance
$$
Z=\sqrt{\frac{\mu}{\epsilon}}.
$$
The pair $(c,Z)$ carries the same information as $(\epsilon,\mu)$: inverting,
$$
\epsilon=\frac{1}{cZ},
\qquad
\mu=\frac{Z}{c}.
$$
The speed $c$ controls propagation, while the impedance $Z$ controls the ratio of the electric to the magnetic amplitude of a wave. Together they carry everything the medium contributes to the linear problem, and they are the natural variables in terms of which the biquaternionic field strength is normalised.

The vacuum is the special case $\epsilon=\epsilon_0$, $\mu=\mu_0$, for which
$$
c_0=\frac{1}{\sqrt{\epsilon_0\mu_0}},
\qquad
Z_0=\sqrt{\frac{\mu_0}{\epsilon_0}}\approx 376.73\ \Omega .
$$
The vacuum speed $c_0$ is a global constant. The medium speed $c$ is not: in an inhomogeneous medium $\epsilon=\epsilon(\mathbf{x})$ and $\mu=\mu(\mathbf{x})$, so that $c=c(\mathbf{x})$ and $Z=Z(\mathbf{x})$ are fields, and in a dispersive medium they depend on frequency as well. The rest of this article treats the homogeneous non-dispersive case first, then relaxes these assumptions in turn.

## The Biquaternionic Gradient and the Local Complex Structure

The biquaternionic gradient is
$$
\tilde{\nabla}=e_0\,\partial_{ict}+e_1\,\partial_x+e_2\,\partial_y+e_3\,\partial_z,
\qquad
\partial_{ict}=\frac{\partial}{\partial(ict)}=-\frac{i}{c}\,\partial_t,
$$
and its quaternion conjugate negates the vector part. Multiplying them, the cross terms cancel and
$$
\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\tilde{\nabla}^{\natural}\tilde{\nabla}
=\partial_{ict}^2+\Delta
=\Delta-\frac{1}{c^2}\,\partial_t^2,
$$
the d'Alembertian of a medium with speed $c$. This is the same operator identity as in the vacuum, with $c$ in place of $c_0$.

The medium enters this operator in exactly one way: through $c$ in $\partial_{ict}$. The algebra — the quaternion units, the scalar imaginary $i$, the decomposition $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ — is fixed and medium-independent. What the medium changes is the **embedding of physical spacetime into the algebra**. The material time coordinate is $ict=i\,c\,t$, so the map from physical time to the imaginary scalar direction of $\mathbb{B}$ carries the local factor $c(\mathbf{x})$.

Because $c>0$ is real, the medium rescales the imaginary axis but does not rotate it. The phase of the complex structure is the fixed $i$; its scale is the local $c$. This is the precise sense in which the complex structure is local. In the language of the introduction to the framework, $c$ plays the role of the local scale factor of the complex structure, and the constant vacuum value $c_0$ is the special case in which that scale does not vary. The classical $ict$ convention of Minkowski space is the vacuum limit of the local structure.

Two comments are worth making. First, the factorization $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}$ holds for any real positive $c$, so the algebraic fact on which the biquaternionic Maxwell equation rests is insensitive to the medium. Second, passing from vacuum to medium does not change the algebra $\mathbb{B}$; a medium is not a deformation of the complex structure but a different local scale for its imaginary direction.

## The Field Strength and Its Two Halves

The parent article defines the field-strength biquaternion as the pure vector
$$
\tilde{F}=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}
=\sum_{k=1}^{3}F_k\,e_k,
\qquad
F_k=i\sqrt{\epsilon}\,E_k-\sqrt{\mu}\,H_k,
$$
with $\mathrm{Sc}(\tilde{F})=0$. We use that definition without change. Two features of it are specific to the medium.

**The normalisation.** The factors $\sqrt{\epsilon}$ and $\sqrt{\mu}$ are natural because $\epsilon\,\mathbf{E}^2$ and $\mu\,\mathbf{H}^2$ are both energy densities. Hence $\sqrt{\epsilon}\,\mathbf{E}$ and $\sqrt{\mu}\,\mathbf{H}$ have the common dimension of the square root of an energy density, the two halves of $\tilde{F}$ are dimensionally homogeneous, and the biquaternion norm $N(\tilde{F})$ has the dimension of an energy density. The normalisation is equivalent to the two medium parameters introduced above: since $\sqrt{\epsilon\mu}=1/c$ and $\sqrt{\mu/\epsilon}=Z$, the data $(\sqrt{\epsilon},\sqrt{\mu})$ and $(c,Z)$ determine each other. The medium therefore enters $\tilde{F}$ through the same two numbers that govern propagation.

The field strength is an overall constant multiple of the Riemann–Silberstein vector. Using $\mathbf{B}=\mu\mathbf{H}$ and $c=1/\sqrt{\epsilon\mu}$,
$$
i\sqrt{\epsilon}\,\mathbf{V}=i\sqrt{\epsilon}\left(\mathbf{E}+ic\mathbf{B}\right)
=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\epsilon}\,c\,\mathbf{B}
=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}
=\tilde{F},
$$
because $\sqrt{\epsilon}\,c\,\mu=\sqrt{\mu}$. Thus
$$
\tilde{F}=i\sqrt{\epsilon}\,\mathbf{V},
\qquad
\mathbf{V}=\mathbf{E}+ic\mathbf{B},
$$
exactly as in the parent article.

**The two halves.** Because the electric and magnetic fields are real, the two terms of $\tilde{F}$ land in the two complementary subspaces:
$$
\tilde{F}
=\underbrace{i\sqrt{\epsilon}\,\mathbf{E}}_{\in\,\mathbb{M}_+}
\;+\;
\underbrace{\left(-\sqrt{\mu}\,\mathbf{H}\right)}_{\in\,\mathbb{M}_-}.
$$
The electric half is a pure imaginary vector and is therefore Hermitian; the magnetic half is a pure real vector and is therefore anti-Hermitian. Equivalently,
$$
\tfrac{1}{2}\left(\tilde{F}+\tilde{F}^{*}\right)=i\sqrt{\epsilon}\,\mathbf{E},
\qquad
\tfrac{1}{2}\left(\tilde{F}-\tilde{F}^{*}\right)=-\sqrt{\mu}\,\mathbf{H},
$$
so the projection of $\tilde{F}$ onto the informational sector $\mathbb{M}_+$ measures the electric field, and its projection onto the material sector $\mathbb{M}_-$ measures the magnetic field.

The split into the two sectors is structural and does not depend on the medium: $i\sqrt{\epsilon}\,\mathbf{E}$ lies in $\mathbb{M}_+$ and $-\sqrt{\mu}\,\mathbf{H}$ lies in $\mathbb{M}_-$ for every real $\epsilon,\mu>0$. What the medium fixes is the **relative weight** of the two halves, through the ratio $\sqrt{\mu}/\sqrt{\epsilon}=Z$. This is one concrete sense in which the local complex structure is at work: the field strength is not a vector of a single sector but the sum of a Hermitian and an anti-Hermitian piece, and the medium sets their balance.

The energy is carried by the Hermitian form. In the parent article,
$$
\tilde{F}\tilde{F}^{*}=2W\,e_0+\frac{2i}{c}\,\mathbf{S},
\qquad
W=\frac{1}{2}\left(\epsilon\,\mathbf{E}^2+\mu\,\mathbf{H}^2\right)=\frac{1}{2}\left\|\tilde{F}\right\|_E^2,
\qquad
\mathbf{S}=\mathbf{E}\times\mathbf{H},
$$
so twice the energy density is the scalar part of the Hermitian form, and $\frac{2}{c}$ times the imaginary unit times the Poynting vector is its vector part. Both are medium-dependent through $\epsilon$ and $\mu$.

Finally, in an inhomogeneous medium $\epsilon=\epsilon(\mathbf{x})$ and $\mu=\mu(\mathbf{x})$, and the normalisation is applied pointwise:
$$
\tilde{F}(\mathbf{x},t)=i\sqrt{\epsilon(\mathbf{x})}\,\mathbf{E}(\mathbf{x},t)-\sqrt{\mu(\mathbf{x})}\,\mathbf{H}(\mathbf{x},t).
$$
The field strength is then assembled from the local complex structure, and it inherits the spatial variation of the medium.

## Maxwell's Equations in the Medium

With the definitions above, the four Maxwell equations in the medium collapse into the single biquaternionic equation of the parent article,
$$
\tilde{\nabla}\tilde{F}=-\tilde{R},
\qquad
\tilde{R}=R_0+\mathbf{R},
\qquad
R_0=\frac{i\rho}{\sqrt{\epsilon}},
\qquad
\mathbf{R}=\sqrt{\mu}\,\mathbf{J}.
$$
The purpose of this section is to display how the medium factors cancel, so that the single equation is manifestly the same equation in every medium.

For a pure-vector field $\tilde{F}=\mathbf{F}$, the biquaternionic gradient acts as
$$
\tilde{\nabla}\tilde{F}
=-\mathrm{div}\,\mathbf{F}+\partial_{ict}\mathbf{F}+\mathrm{rot}\,\mathbf{F},
$$
the scalar part being $-\mathrm{div}\,\mathbf{F}$ and the vector part $\partial_{ict}\mathbf{F}+\mathrm{rot}\,\mathbf{F}$. Substituting $\mathbf{F}=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}$ and $\partial_{ict}=-(i/c)\partial_t$, and separating the real and imaginary parts, the scalar equation gives
$$
\mathrm{div}\,\mathbf{E}=\frac{\rho}{\epsilon},
\qquad
\mathrm{div}\,\mathbf{H}=0,
$$
and the vector equation gives
$$
\mathrm{rot}\,\mathbf{H}=\frac{\partial\mathbf{D}}{\partial t}+\mathbf{J},
\qquad
\mathrm{rot}\,\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t}.
$$
The first pair is Gauss's law for $\mathbf{D}=\epsilon\mathbf{E}$ together with $\mathrm{div}\,\mathbf{B}=0$ (since $\mathbf{B}=\mu\mathbf{H}$ and $\mu$ is constant here), and the second pair is the Ampère–Maxwell law and Faraday's law. All four standard equations are recovered, with no residual $\epsilon$ or $\mu$.

The cancellation is the content of the normalisation. In the vector equation, for example, the term coupling $\partial_t\mathbf{E}$ to $\mathrm{rot}\,\mathbf{H}$ carries the coefficient
$$
\frac{\sqrt{\epsilon}}{c\sqrt{\mu}}=\epsilon,
$$
using $\sqrt{\epsilon\mu}=1/c$; likewise the term coupling $\partial_t\mathbf{H}$ to $\mathrm{rot}\,\mathbf{E}$ carries $\sqrt{\mu}/(c\sqrt{\epsilon})=\mu$. The factors $\sqrt{\epsilon}$ and $\sqrt{\mu}$ on the fields and the factors $1/\sqrt{\epsilon}$ and $\sqrt{\mu}$ on the source are exactly what is required for the medium to disappear from the equation. The biquaternionic Maxwell equation is therefore medium-independent in form; the medium is entirely in the definitions of $\tilde{F}$, $\tilde{R}$, and the operator $\partial_{ict}$.

Two companion statements from the Maxwell article carry over unchanged. The first is the integrability condition $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{R})=0$, which is the biquaternionic form of charge conservation. The second is the potential formulation: in the Lorenz gauge the potential biquaternion $\tilde{A}=i\phi/c+\mathbf{A}$ satisfies
$$
\Box\tilde{A}=-\mu\,\tilde{R}',
\qquad
\tilde{R}'=ic\rho+\mathbf{J},
$$
where the factor $\mu$ is now explicit. The field-strength formulation hides the medium in the normalisation; the potential formulation displays one of the medium parameters directly.

## Dispersion and the Frequency-Dependent Local Structure

So far $\epsilon$ and $\mu$ have been taken constant. A real medium responds with a delay, and its permittivity and permeability depend on frequency: $\epsilon=\epsilon(\omega)$, $\mu=\mu(\omega)$. In a monochromatic field the constitutive relations are evaluated at the frequency of the field, so the medium speed becomes
$$
c(\omega)=\frac{1}{\sqrt{\epsilon(\omega)\mu(\omega)}}.
$$
The refractive index relative to vacuum is
$$
n(\omega)=\frac{c_0}{c(\omega)}
=c_0\sqrt{\epsilon(\omega)\mu(\omega)}
=\sqrt{\frac{\epsilon(\omega)\mu(\omega)}{\epsilon_0\mu_0}},
$$
and the dispersion relation of a plane wave in the medium is
$$
k^2=\omega^2\,\epsilon(\omega)\mu(\omega),
\qquad
k=\frac{\omega}{c(\omega)}=\frac{n(\omega)\,\omega}{c_0}.
$$
The phase velocity is $v_p=\omega/k=c(\omega)$, and the group velocity is
$$
v_g=\frac{d\omega}{dk}=\left(\frac{dk}{d\omega}\right)^{-1}
=\frac{c_0}{n(\omega)+\omega\,\dfrac{dn}{d\omega}}.
$$
All of this is standard, and it is what fixes the meaning of a "plane wave in a medium" for the later exercise.

The biquaternionic reading is that each Fourier component carries its own local complex structure. The algebra $\mathbb{B}$ is the same at every frequency; what changes is the scale that maps physical time to the imaginary coordinate. For a monochromatic wave the scalar component of the gradient acts as
$$
\partial_{ict}=-\frac{i}{c}\,\partial_t\;\longrightarrow\;-\frac{\omega}{c(\omega)},
$$
so the imaginary time axis is scaled differently at each frequency. The local complex structure is thus **spectral** as well as spatial: it is indexed by the frequency at which the medium is probed.

Two caveats delimit what the framework as written supports.

First, the normalisation $\sqrt{\epsilon(\omega)}$, $\sqrt{\mu(\omega)}$ is real only in a transparent frequency window, away from absorption lines. As long as it is real, the split of $\tilde{F}$ into a Hermitian electric half and an anti-Hermitian magnetic half survives at each frequency, and the invariants are defined at each frequency with $c(\omega)$. Near a resonance, however, $\epsilon$ and $\mu$ become complex, and with them $\sqrt{\epsilon}$ and $\sqrt{\mu}$. The electric and magnetic contributions are then no longer purely imaginary and purely real, the two halves of $\tilde{F}$ no longer lie in $\mathbb{M}_+$ and $\mathbb{M}_-$ separately, and $\tilde{F}$ becomes fully complex. The complexified extension of the parent article, in which the coefficients of $\tilde{F}$ are unrestricted complex numbers, is the natural arena for that case; but the identification of the physical field with a particular real slice is a further choice which the framework as written does not fix. The absorbing case is therefore not pursued here.

Second, the energy density of the parent, $W=\tfrac{1}{2}(\epsilon\,\mathbf{E}^2+\mu\,\mathbf{H}^2)$, is the non-dispersive expression. For a monochromatic field in a dispersive medium the standard energy density is the Brillouin expression
$$
W=\frac{1}{2}\left(\frac{d(\omega\epsilon)}{d\omega}\,\mathbf{E}^2+\frac{d(\omega\mu)}{d\omega}\,\mathbf{H}^2\right),
$$
which reduces to the parent's form when the dispersion is negligible. This is a boundary of what the framework as stated supports; it leaves the field strength, the invariants, and the propagation conventions untouched.

## A Chiral Medium: One Quaternionic Equation

The constitutive relations used so far, $\mathbf{D}=\epsilon\,\mathbf{E}$ and $\mathbf{B}=\mu\,\mathbf{H}$, are the simplest a linear medium can have: each field couples to its own partner and to nothing else. A **chiral** medium couples them. In the Drude–Born–Fedorov form used by Grudsky, Khmelnytskaya and Kravchenko,
$$
\mathbf{B}=\mu\left(\mathbf{H}+\beta\,\mathrm{rot}\,\mathbf{H}\right),
\qquad
\mathbf{D}=\epsilon\left(\mathbf{E}+\beta\,\mathrm{rot}\,\mathbf{E}\right),
$$
where $\beta$ is the **chirality measure** of the medium, a real scalar of the dimension of a length, and $\epsilon,\mu,\beta$ are constants. At $\beta=0$ these are the relations of the preceding sections. The magnetoelectric coupling is what makes the reduction below a different problem rather than a relabelling of the same one.

**A name collision.** Everywhere else in this framework "chiral" means the chirality of a Dirac field, the eigenvalue of the fifth gamma matrix; for that sense see *Chiral Fermions in the Biquaternion Framework*. "Chiral medium" is the older use of the same word for an optically active material. The two senses are unrelated and are distinguished by context alone; the medium sense occurs only in this section and its two companions below. The physical motivation for the medium sense — organic molecules such as DNA at some frequencies, the pupil of the eye, and manufactured chiral materials — is recorded by the authors of the time-harmonic treatment cited below.

**The reduction, and why it is not the same reduction.** Substituting the two relations into Faraday's and Ampère–Maxwell's laws and keeping the two divergence equations gives the chiral system
$$
\mathrm{rot}\,\mathbf{H}=\epsilon\left(\partial_t\mathbf{E}+\beta\,\partial_t\,\mathrm{rot}\,\mathbf{E}\right)+\mathbf{J},
\qquad
\mathrm{rot}\,\mathbf{E}=-\mu\left(\partial_t\mathbf{H}+\beta\,\partial_t\,\mathrm{rot}\,\mathbf{H}\right),
\qquad
\mathrm{div}\,\mathbf{E}=\frac{\rho}{\epsilon},
\qquad
\mathrm{div}\,\mathbf{H}=0 ,
$$
the last of which is unchanged because $\mathrm{div}\,\mathrm{rot}=0$ and $\mu$ is constant. The magnetoelectric terms do not disturb charge conservation either: eliminating $\mathrm{div}\,\mathrm{rot}\,\mathbf{H}=0$ against the two divergence equations, or equivalently taking the divergence of Ampère–Maxwell's law, gives $i\omega\rho+\mathrm{div}\,\mathbf{J}=0$ in the frequency domain, the law $\partial_t\rho+\mathrm{div}\,\mathbf{J}=0$ in the time domain, exactly as for an ordinary medium. Applying $\mathrm{rot}$ separates the fields and gives the chiral wave equations
$$
\mathrm{rot}\,\mathrm{rot}\,\mathbf{E}+\epsilon\mu\,\partial_t^2\mathbf{E}
+2\beta\epsilon\mu\,\partial_t^2\,\mathrm{rot}\,\mathbf{E}
+\beta^2\epsilon\mu\,\partial_t^2\,\mathrm{rot}\,\mathrm{rot}\,\mathbf{E}
=-\mu\,\partial_t\mathbf{J}-\beta\mu\,\partial_t\,\mathrm{rot}\,\mathbf{J},
$$
and the corresponding equation for $\mathbf{H}$ with $\mathrm{rot}\,\mathbf{J}$ as its source. At $\beta=0$ these are the ordinary second-order wave equations of the medium. For $\beta\neq0$ the last term makes them **fourth order**: the chiral generalisation is not the non-chiral wave equation with a small term added, it is an equation of a different order.

The chiral system nevertheless collapses into one equation, carried by a new operator. With $D=i_1\partial_{x_1}+i_2\partial_{x_2}+i_3\partial_{x_3}$ the **Moisil–Teodoresco** operator of quaternionic analysis, the operator is
$$
M=\beta\sqrt{\epsilon\mu}\;\partial_t D+\sqrt{\epsilon\mu}\;\partial_t-iD ,
$$
and it acts on the purely vectorial biquaternionic field
$$
\mathbf{V}=\mathbf{E}-i\sqrt{\frac{\mu}{\epsilon}}\,\mathbf{H},
\qquad
M\mathbf{V}=-\sqrt{\frac{\mu}{\epsilon}}\,\mathbf{J}
-\beta\sqrt{\frac{\mu}{\epsilon}}\,\partial_t\rho+\frac{i\rho}{\epsilon}.
$$
The equivalence is exact and two-way, not a weak-coupling approximation in $\beta$: the physical fields solve the chiral system if and only if $\mathbf{V}$ solves this one (the source's Proposition 1). For $\beta=0$ the operator reduces to $\sqrt{\epsilon\mu}\,\partial_t-iD$, which is the reduction of the non-chiral case, and the authors are explicit that the chiral operator is *essentially different* from it.

**Conventions.** The source's objects and the parent's are related by two conjugations, and recording them makes the agreement between the two reductions exact rather than approximate. First, the source's vectorial field pairs $\mathbf{E}$ with $-\sqrt{\mu/\epsilon}\,\mathbf{H}$, whereas the parent's field strength is $\tilde{F}=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}$; the two are related by
$$
\tilde{F}=i\sqrt{\epsilon}\,\overline{\mathbf{V}},
$$
the complex conjugate of the source's field, so the magnetic-half sign is the only difference. Second, the source's $D$, with its quaternion units $i_k$, is the spatial part of the parent's gradient: writing $\tilde{\nabla}=\partial_{ict}+\sum_ke_k\partial_k$ and its quaternion conjugate $\tilde{\nabla}^{\natural}=\partial_{ict}-\sum_ke_k\partial_k$ (the vector part negated, the object whose product with $\tilde{\nabla}$ gives $\Box$), the source's non-chiral operator is
$$
M_0=\left.M\right|_{\beta=0}=\sqrt{\epsilon\mu}\,\partial_t-iD=i\,\tilde{\nabla}^{\natural},
$$
verified to machine zero: $i$ times the **quaternion conjugate** of the parent's gradient. Neither conjugation changes the content of the Maxwell system — the parent's own product $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\tilde{\nabla}^{\natural}\tilde{\nabla}$ is independent of which factor comes first — which is why the two single-equation reductions agree where they overlap. What has no counterpart in the parent, and what no conjugation removes, is the chiral term $\beta\sqrt{\epsilon\mu}\,\partial_tD$: the *product* of the scalar time derivative with the vector part of the gradient, a second-order differential operator and not a multiple of $\tilde{\nabla}^{\natural}$.

**The non-chiral limit in the framework's own symbols.** At $\beta=0$ the operator is $M_0=\sqrt{\epsilon\mu}\,\partial_t-iD$, and composed with its complex conjugate it is the d'Alembertian. Because $D^2=-\Delta$ (verified to $1.8\times10^{-15}$ on random wave vectors) and $\partial_t$ commutes with $D$,
$$
\left(\sqrt{\epsilon\mu}\,\partial_t-iD\right)\left(\sqrt{\epsilon\mu}\,\partial_t+iD\right)
=\epsilon\mu\,\partial_t^2-\Delta=-\Box ,
$$
which is the parent article's factorization read with the opposite overall sign for $\Box$. The source cites the same identity as the factorization of the non-chiral wave operator on which the earlier quaternionic reformulation rests. Read together, the two statements say that the parent's reduction is the $\beta=0$ member of a one-parameter family, and the member whose single equation is *first* order.

**A degenerate frequency in the frequency domain.** A Fourier transform in $t$ replaces $\partial_t$ by $i\omega$ and turns $M$ into $\beta\sqrt{\epsilon\mu}\,i\omega D+\sqrt{\epsilon\mu}\,i\omega-iD$, which factors exactly:
$$
M(\omega)=i\left(\beta\sqrt{\epsilon\mu}\,\omega-1\right)\bigl(D+\alpha(\omega)\bigr),
\qquad
\alpha(\omega)=\frac{\sqrt{\epsilon\mu}\,\omega}{\beta\sqrt{\epsilon\mu}\,\omega-1}
$$
(verified to $4.4\times10^{-16}$ over random wave vectors and frequencies). So *at each frequency* the chiral operator is again a Moisil–Teodoresco operator $D+\alpha$, with a parameter $\alpha$ that is not small and depends on the frequency: this is why the fundamental solution of the chiral operator is obtainable from the known fundamental solution of $D+\alpha$, and also why it is not obtainable from the non-chiral one by substitution. The prefactor **vanishes** at
$$
\omega=\frac{1}{\beta\sqrt{\epsilon\mu}}=\frac{c}{\beta},
$$
the frequency whose wavelength is $2\pi\beta$. There $M(\omega)$ annihilates every field: the chiral reduction carries a distinguished frequency at which its operator degenerates, and the non-chiral reduction carries none.

**The birefringence is in the same equation.** A chiral medium is optically active — the two circular polarisations propagate with different wave numbers — and that too is a consequence of the fourth-order equation, not a separate input. For a transverse plane wave with the two helicities labelled by $\tau=\pm1$, the two branches of the wave equation above are
$$
\left(1-\beta^2\epsilon\mu\,\omega^2\right)k^2-2\tau\beta\epsilon\mu\,\omega^2k-\epsilon\mu\,\omega^2=0 ,
\qquad\text{i.e.}\qquad
n_\tau(\omega)=\frac{c\,k_\tau}{\omega}=\frac{1}{1-\tau\beta\omega/c}
$$
on the propagating branch. Both were checked to $2.2\times10^{-16}$ against the wave equation evaluated on the corresponding circular polarisation, and at $\beta=0$ the two branches collapse to the single $k=\sqrt{\epsilon\mu}\,\omega$ of the non-chiral medium. The two refractive indices are the optical activity, and they come with no free constant beyond the one $\beta$ that entered the constitutive relations.

**The fundamental solution and the causality principle.** The source constructs the fundamental solution of $M$ using quaternionic analysis. Writing
$$
\Theta_\alpha(\mathbf{x})=-\frac{e^{i\alpha|\mathbf{x}|}}{4\pi|\mathbf{x}|},
\qquad
K_\alpha(\mathbf{x})=-\mathrm{grad}\,\Theta_\alpha(\mathbf{x})+\alpha\,\Theta_\alpha(\mathbf{x})
=\left(\alpha+\frac{\mathbf{x}}{|\mathbf{x}|^2}-\frac{i\alpha\,\mathbf{x}}{|\mathbf{x}|}\right)\Theta_\alpha(\mathbf{x}),
$$
the object $K_\alpha$ is a fundamental solution of the shifted operator in the source's own normalisation, $D_\alpha K_\alpha=\delta$ with $D_\alpha=D+\alpha$, and it satisfies at infinity the radiation condition
$$
\left(1+\frac{i\mathbf{x}}{|\mathbf{x}|}\right)K_\alpha(\mathbf{x})=o\!\left(\frac{1}{|\mathbf{x}|}\right),
$$
which the source identifies as the quaternionic form of the Silver–Müller condition. The factor $1+i\mathbf{x}/|\mathbf{x}|$ is a zero divisor of the algebra — its norm vanishes while its scalar part is $1$ — so the condition may not be divided by it and no decay rate follows from it alone; the caveat, and the extra decay hypothesis the literature attaches to it in the isotropic case, are recorded in *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation*. **The minus sign in $\Theta_\alpha$ is the source's and is not decorative.** The bracketed form of $K_\alpha$ factors $\Theta_\alpha$ out, so it reads identically with either sign; the sign is fixed by the kernel's defining property, and it is the minus that makes $D_\alpha K_\alpha=+\delta$ rather than $-\delta$ — checked numerically, the surface integral of $\mathbf{n}K_\alpha$ over a sphere surrounding the origin tending to $+1$ for the source's sign and to $-1$ for the other. It is fixed independently by the classical limit: at $\alpha=0$ the source's sign gives $K_0=-\mathbf{x}/(4\pi|\mathbf{x}|^{3})$, the Cauchy kernel of $D$, which is also the kernel the article's inhomogeneous-media section arrives at, whereas the other sign would give its negative. The two expressions for $K_\alpha$ agree (the gradient identity was verified to $3\times10^{-9}$, the finite-difference floor). After the time Fourier transform, the chiral operator's fundamental solution acquires the denominator $\omega-a$ with $a=1/(\beta\sqrt{\epsilon\mu})$, the same degenerate frequency as above — together with a double pole there, and an essential singularity through a factor $\exp(ic(\mathbf{x})/(\omega-a))$. For $\beta\neq0$, therefore, the fundamental solution is not a finite combination of the customary kernels; the source expands the exponential and reduces the problem to a series of residues.

Causality is then imposed, not assumed: among the regularisations of the inverse transform the source selects the one that vanishes for $t<0$, by displacing the frequency into the upper half-plane, $\omega\mapsto\omega-i0$, "in agreement with the condition $\mathrm{Im}\,\alpha\geq0$". For a simple pole this gives the retarded factor
$$
\frac{1}{2\pi i}\oint\frac{e^{i\omega t}\,d\omega}{\omega-a_y}
=\Theta(t)\,e^{i a_y t},
$$
with $a_y=a+iy$ and $\Theta$ the Heaviside function, and the higher-order poles give $\Theta(t)\,e^{ia_yt}(it)^{n}/n!$; the residue formula was checked to $3.2\times10^{-9}$ for pole orders 1–3. For $t<0$ the same integrand must be closed in the lower half-plane, where the displaced pole is not enclosed, so the contour integral vanishes: that is the content of the causality principle here, and it is exactly the statement that the displaced pole lies in the upper half-plane. Convolution of the resulting kernel with the quaternionic source then solves the inhomogeneous chiral system in whole space.

**The residue series resums.** The source's interchange of the summation of the expanded exponential with the contour integration is justified, not formal — it checks the uniform convergence that licenses it — and the two residue series it produces are the Bessel series themselves:
$$
I_1=i\Theta(t)\,e^{ia_yt}J_0\!\left(2\sqrt{c(\mathbf{x})\,t}\right),
\qquad
I_2=-\Theta(t)\sqrt{\frac{t}{c(\mathbf{x})}}\,e^{ia_yt}J_1\!\left(2\sqrt{c(\mathbf{x})\,t}\right),
$$
where $c(\mathbf{x})=|\mathbf{x}|/(\beta^2\sqrt{\epsilon\mu})$ is the coefficient of the essential singularity, so that $2\sqrt{c(\mathbf{x})t}=2\sqrt{t|\mathbf{x}|}/(\beta(\epsilon\mu)^{1/4})$. Both identifications were checked to $6\times10^{-13}$ against the standard series of $J_0$ and $J_1$. The time dependence of the chiral fundamental solution is therefore a **closed form** in two Bessel functions, and the source writes it out in that form: the kernel is built from $K_{1/\beta}$ and $\Theta_{1/\beta}$, the parameter $1/\beta$ being the limit of $\alpha(\omega)$ as $\omega\to\infty$, that is the frequency-independent part of the exponent, multiplied by $J_0$ and $J_1$ of $2\sqrt{t|\mathbf{x}|}/(\beta(\epsilon\mu)^{1/4})$ and by the retarded factor $\Theta(t)e^{iat}/(\beta\sqrt{\epsilon\mu})$. What fails for $\beta\neq0$ is thus not the existence of a causal fundamental solution but its expression through the customary Cauchy and Helmholtz kernels alone; the essential singularity of the frequency-domain kernel resums into Bessel functions of the retarded variable $\sqrt{c(\mathbf{x})t}$, one order up from the non-chiral case, where the kernel is $\Theta(t)\delta(|\mathbf{x}|-t/\sqrt{\epsilon\mu})/(4\pi|\mathbf{x}|)$ and no Bessel function appears.

**What the addition is, and what it is not.** The Drude–Born–Fedorov relations are a standard constitutive model, and everything above is a mathematical result about it: a reduction to one equation, a factorization, a degeneracy, a birefringence and a causal fundamental solution. Nothing in it is evidence for the biquaternion framework, and the framework's own epistemic standard applies. What it does supply is a precise structural statement about the framework's own reduction: that reduction is the $\beta=0$ member of a family, and the family's other members are *not* deformations of it — the operator changes order, acquires a degenerate frequency, and loses the expression of its fundamental solution as a finite combination of the customary kernels (it resums to Bessel functions instead, as recorded above). That is the reason the authors' remark that the chiral operator is "essentially different" is a statement about the algebra and not a figure of speech.

**A note on the two time-dependence problems.** This paper treats the **time-dependent** chiral problem. The companion work on the same topic, *On a Quaternionic Reformulation of Maxwell's Equations for Chiral Media and its Applications*, treats the **time-harmonic** chiral problem and integral representations; the series' further items treat time-harmonic operators for inhomogeneous media with numerical fundamental solutions. The organising fact is that the two problems need different operators and different solution methods, so a reader should choose by whether the time dependence is resolved or transformed away.

**Where the time-harmonic problem is treated.** The time-harmonic chiral problem — the diagonalization into the two circular combinations $\Phi,\Psi$ with the two wavenumbers $\alpha_1,\alpha_2$, the integral representations, the complete solution of the *extendability* problem, the electromagnetic energy balance, and the inhomogeneous (slowly varying, stratified) chiral medium — is recorded in the dedicated article *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation*, whose source is the companion paper of Kravchenko and Oviedo. That material is deliberately not repeated here: this article keeps the time-dependent reduction, and the dedicated article carries the time-harmonic theory, so each definite description still has one referent.

## Arbitrary Inhomogeneous Media: The Carrier Function and the Vekua Equation

Every medium so far has had constant $\epsilon$ and $\mu$. Let them now be differentiable positive functions of position, $\epsilon=\epsilon(\mathbf{x})$ and $\mu=\mu(\mathbf{x})$, and keep the Maxwell system in the form

$$
\mathrm{rot}\,\mathbf{H}=\epsilon\,\partial_t\mathbf{E}+\mathbf{j},
\qquad
\mathrm{rot}\,\mathbf{E}=-\mu\,\partial_t\mathbf{H},
\qquad
\mathrm{div}(\epsilon\mathbf{E})=\rho,
\qquad
\mathrm{div}(\mu\mathbf{H})=0 ,
$$

which is the system of the preceding sections with the two parameters no longer constant. Nothing in the system is new. What is new is that the two divergence equations now produce the terms $\langle\mathrm{grad}\,\epsilon/\epsilon,\mathbf{E}\rangle$ and $\langle\mathrm{grad}\,\mu/\mu,\mathbf{H}\rangle$, so a reduction to a single quaternionic equation can no longer have constant coefficients.

**The carrier identity.** The reduction rests on one algebraic fact. Let $\phi\neq0$ be a scalar function and $g$ biquaternion-valued. Since $D$ is a first-order differential operator and $\phi$ is a scalar, hence commutes with the quaternion units,

$$
D[\phi\,g]=(D\phi)\,g+\phi\,Dg ,
$$

and since $D\phi=\mathrm{grad}\,\phi$, dividing by $\phi\neq0$ gives the two equivalent forms

$$
\left(D+\frac{\mathrm{grad}\,\phi}{\phi}\right)g=\frac{1}{\phi}\,D(\phi\,g),
\qquad
\left(D-\frac{\mathrm{grad}\,\phi}{\phi}\right)f=\phi\,D\!\left(\frac{f}{\phi}\right).
$$

The second form is the striking one: the variable-coefficient operator $D-\mathrm{grad}\,\phi/\phi$ is the constant-coefficient operator $D$ conjugated by multiplication by $\phi$. A coefficient of exactly the form $\mathrm{grad}\,\phi/\phi$ is therefore **removable**, and this is why the fields below are normalised by $\sqrt{\epsilon}$ and $\sqrt{\mu}$: the gradients the divergence equations produce are $\mathrm{grad}\,\epsilon/\epsilon=2\,\mathrm{grad}\sqrt{\epsilon}/\sqrt{\epsilon}$, so the square root is the factor that absorbs them. We call $\phi$ a **carrier function** and the identity the **carrier identity**.

**A scalar-product identity.** The divergence equations enter the reduction through scalar products, which have to be exchanged for products. For real vectors $\mathbf{p},\mathbf{q}$ the products $\mathbf{p}\mathbf{q}$ and $\mathbf{q}\mathbf{p}$ have a common scalar part and opposite vector parts, so

$$
\langle\mathbf{p},\mathbf{q}\rangle=-\tfrac{1}{2}\left(\mathbf{p}\mathbf{q}+\mathbf{q}\mathbf{p}\right),
$$

the sign being fixed by $e_je_k+e_ke_j=-2\delta_{jk}$. This is the identity that lets a scalar product be written as a sum of the left and right products that the carrier identity can absorb.

**The doubled pair.** Write $\vec{\epsilon}$ and $\vec{\mu}$ for the two half-gradients,

$$
\vec{\epsilon}:=\frac{\mathrm{grad}\sqrt{\epsilon}}{\sqrt{\epsilon}}=\frac{1}{2}\frac{\mathrm{grad}\,\epsilon}{\epsilon},
\qquad
\vec{\mu}:=\frac{\mathrm{grad}\sqrt{\mu}}{\sqrt{\mu}}=\frac{1}{2}\frac{\mathrm{grad}\,\mu}{\mu},
$$

and $u_\epsilon:=\mathrm{grad}\,\epsilon/\epsilon=2\vec{\epsilon}$, with $u_\mu$ defined the same way. Combining the two divergence equations with the two curl equations gives the pair

$$
D\,\mathbf{E}=\langle u_\epsilon,\mathbf{E}\rangle-\mu\,\partial_t\mathbf{H}-\frac{\rho}{\epsilon},
\qquad
D\,\mathbf{H}=\langle u_\mu,\mathbf{H}\rangle+\epsilon\,\partial_t\mathbf{E}+\mathbf{j},
$$

and the scalar-product identity turns each of them into a gradient-corrected operator. For the electric field, adding $\vec{\epsilon}\,\mathbf{E}$ and using $\langle u_\epsilon,\mathbf{E}\rangle=-(\vec{\epsilon}\,\mathbf{E}+\mathbf{E}\,\vec{\epsilon})$,

$$
\left(D+M_{\vec{\epsilon}}\right)\mathbf{E}
=-\tfrac{1}{2}\,\mathbf{E}\,u_\epsilon-\mu\,\partial_t\mathbf{H}-\frac{\rho}{\epsilon},
$$

and for the magnetic field

$$
\left(D+M_{\vec{\mu}}\right)\mathbf{H}
=-\tfrac{1}{2}\,\mathbf{H}\,u_\mu+\epsilon\,\partial_t\mathbf{E}+\mathbf{j},
$$

where $M_\alpha$ denotes left multiplication by $\alpha$, so that the coefficient stands on the left as written, while the two corrections on the right-hand sides are **right** products. The order is not cosmetic: exchanging $\mathbf{E}u_\epsilon$ for $u_\epsilon\mathbf{E}$ changes the remainder by $2\,\mathbf{E}\times u_\epsilon$.

**The reformulation.** The carrier identity with $\phi=\sqrt{\epsilon}$ says that $\frac{1}{\sqrt{\epsilon}}D(\sqrt{\epsilon}\mathbf{E})=(D+M_{\vec{\epsilon}})\mathbf{E}$, and with $\phi=\sqrt{\mu}$ the analogous statement holds for $\mathbf{H}$. Introducing the normalised fields and the medium speed,

$$
\vec{\mathbf{E}}:=\sqrt{\epsilon}\,\mathbf{E},
\qquad
\vec{\mathbf{H}}:=\sqrt{\mu}\,\mathbf{H},
\qquad
c=\frac{1}{\sqrt{\epsilon\mu}},
$$

the pair becomes

$$
D\,\vec{\mathbf{E}}+\vec{\mathbf{E}}\,\vec{\epsilon}
=-\frac{1}{c}\,\partial_t\vec{\mathbf{H}}-\frac{\rho}{\sqrt{\epsilon}},
\qquad
D\,\vec{\mathbf{H}}+\vec{\mathbf{H}}\,\vec{\mu}
=\frac{1}{c}\,\partial_t\vec{\mathbf{E}}+\sqrt{\mu}\,\mathbf{j},
$$

the corrections now being right products, as the dots record. In the time-harmonic convention $e^{i\omega t}$ of the preceding sections, with $k=\omega\sqrt{\epsilon\mu}$,

$$
D\,\vec{\mathbf{E}}+\vec{\mathbf{E}}\,\vec{\epsilon}=-ik\,\vec{\mathbf{H}}-\frac{\rho}{\sqrt{\epsilon}},
\qquad
D\,\vec{\mathbf{H}}+\vec{\mathbf{H}}\,\vec{\mu}=ik\,\vec{\mathbf{E}}+\sqrt{\mu}\,\mathbf{j}.
$$

These are exact equivalents of the Maxwell system for arbitrary $\epsilon(\mathbf{x})$ and $\mu(\mathbf{x})$. "Exact" is meant literally: this is neither a weak-inhomogeneity nor a slowly-varying approximation, and no term has been dropped. At constant $\epsilon,\mu$ the vectors $\vec{\epsilon},\vec{\mu}$ vanish and the pair collapses to $D\vec{\mathbf{E}}=-ik\vec{\mathbf{H}}-\rho/\sqrt{\epsilon}$ and $D\vec{\mathbf{H}}=ik\vec{\mathbf{E}}+\sqrt{\mu}\,\mathbf{j}$, which is the constant-coefficient reduction of the earlier sections written in the normalisation of this one.

**Two conventions meet here, and they should be separated.** The vacuum operator of the source's reduction is $\frac{1}{c}\partial_t+iD$, while the non-chiral reduction recorded in the chiral section above is $M_0=\frac{1}{c}\partial_t-iD$. The two are complex conjugates of one another and not rivals. The field $f$ used below is $\sqrt{\epsilon}$ times the Riemann–Silberstein vector, that is, $\sqrt{\epsilon}$ times the conjugate of the chiral section's purely vectorial field $\mathbf{V}=\mathbf{E}-iZ\mathbf{H}$; conjugating a reduction built on $M_0$ replaces $-iD$ by $+iD$, so the sign of the $iD$ term is carried by which field one starts from. The sections below use the source's convention throughout, and the dictionary to the corpus's field strength is given at the end of this section.

**The single equation, and why it is a Vekua equation.** One further combination collapses the pair. Set

$$
f:=\vec{\mathbf{E}}+i\,\vec{\mathbf{H}},
\qquad
\vec{c}:=\frac{\mathrm{grad}\sqrt{c}}{\sqrt{c}}=\frac{1}{2}\,\mathrm{grad}\ln c,
\qquad
\vec{Z}:=\frac{\mathrm{grad}\sqrt{Z}}{\sqrt{Z}}=\frac{1}{2}\,\mathrm{grad}\ln Z ,
$$

where $Z=\sqrt{\mu/\epsilon}$ is the intrinsic impedance fixed earlier. Then the two equations are together equivalent to the single equation

$$
\left(\frac{1}{c}\,\partial_t+iD\right)f-f\,(i\vec{c})-f^{*}\,(i\vec{Z})
=-\left(\sqrt{\mu}\,\mathbf{j}+\frac{i\rho}{\sqrt{\epsilon}}\right),
$$

with $f^{*}$ the coefficientwise complex conjugate of $f$ — the scalar imaginary conjugated, the quaternion units untouched — and the two products again right products. The source writes the impedance $W$ and the two coefficient vectors $\vec{c}$ and $\vec{W}$, the letters $\vec{c},\vec{W}$ standing for $\frac12\mathrm{grad}\ln c$ and $\frac12\mathrm{grad}\ln W$; we keep this article's letter $Z$ for the impedance, and we keep the source's symbol $\vec{c}$ for the first coefficient vector, which is a *vector field built from the speed* and not the speed $c$. The two coefficient vectors are not independent of the pair above: because

$$
\vec{\epsilon}+\vec{\mu}=-\frac{\mathrm{grad}\,c}{c}=-2\vec{c},
\qquad
\vec{\epsilon}-\vec{\mu}=-\frac{\mathrm{grad}\,Z}{Z}=-2\vec{Z},
$$

the symmetric and antisymmetric combinations of the two medium gradients are precisely the two coefficients that appear.

The structure of the equation is what matters. The operator acting on $f$ is the vacuum operator $\frac{1}{c}\partial_t+iD$ of the earlier sections; the inhomogeneity adds two **zeroth-order** terms with variable coefficients, one multiplying $f$ and one multiplying $f^{*}$. A first-order equation whose coefficients act on both $f$ and its conjugate is a **Vekua equation** — the prototype being $w_{\bar z}=Aw+B\bar w$ in one complex variable — and the Vekua equation is the governing equation of generalized analytic, or **pseudoanalytic**, functions. The result is that **Maxwell's equations for an arbitrary inhomogeneous medium are equivalent to a single quaternionic equation of Vekua type**, so that the theory of pseudoanalytic functions becomes available for electromagnetism in arbitrary media: its integral representations, its similarity principle, its Liouville-type theorems, and its existence and solvability results. The corpus now carries the first layer of that theory — the generating quartet of the Vekua-type equation, the reduction of the equation to a condition on the coefficients, the equivalent Vekua equation for their combination, and the inverse of the reduction — in the section *The Generating Quartet, the Pseudoanalytic Equation, and the Inverse of the Reduction* below; the four items listed in the previous sentence are what that section does not yet supply, and they are supplied for the linear theory by the integral-representations and Riemann–Hilbert material of the analysis cluster — the boundary value problem with a jump and the singular integral equation of Cauchy type of *Riemann Boundary Value Problems and Singular Integral Equations*, whose Plemelj formulas, canonical factor and solvability criteria are the general form of the four items.

Two limitations belong with the result. The equivalence relocates the difficulty rather than removing it: the reduction is exact, but it is a reduction to an equation that must then be solved. And the reduction is not a closed-form solution of the time-dependent inhomogeneous problem. What the framework delivers in closed form is the time-dependent problem for homogeneous media, including the chiral ones, and the static problem for inhomogeneous media; the arbitrary inhomogeneous case reaches the equivalent single equation and stops there.

**The dictionary with this article's field strength.** The field $f=\sqrt{\epsilon}\,\mathbf{E}+i\sqrt{\mu}\,\mathbf{H}$ is not the field strength $\tilde{F}$ fixed earlier, but it is a fixed multiple of it:

$$
\tilde{F}=i\,f .
$$

The field-strength biquaternion of this article is therefore $i$ times this paper's $f$; the two differ by the conjugation that exchanges the electric and magnetic halves, and both describe the same Maxwell system in the normalisation that makes the medium gradient removable. In this dictionary the equation above is the inhomogeneous-medium member of the family whose constant-coefficient member is the single equation $\tilde{\nabla}\tilde{F}=-\tilde{R}$ of the earlier sections.

**The same reduction read from the Dirac side.** The carrier identity of this section has a counterpart that reads it as a Dirac potential. The massive Dirac equation with an electric potential, or separately with a scalar potential, becomes after Kravchenko's dictionary a first-order equation whose only position dependence is a coefficient multiplying one basis direction — the shape the carrier identity produces — and matching the two shapes identifies each such Dirac solution with the static sourceless Maxwell field of a medium whose permittivity is the exponential of the accumulated potential,

$$
\epsilon = e^{\,2G(x_1)}, \qquad G(x_1) = \int g(x_1)\,dx_1 ,
$$

$g$ being the potential: the potential is the logarithmic derivative of the square root of the permittivity, which is the carrier function of the normalisation above. The correspondence is recorded in *The Dirac Equation in Biquaternionic Form*, section *The Static Maxwell Field of an Inhomogeneous Medium as a Dirac Potential*. It belongs here because the two ends are this section's carrier function and that article's potential coupling, and the statement is a dictionary between them rather than a new solution; it is a static statement, and it does not extend to the time-dependent inhomogeneous case, where the reduction is the Vekua equation and no such identification is available.

## The Operator $D+M_{\vec{\alpha}}$, the Reduction to the Schrödinger Equation, and a Fundamental Solution

In the static case the reformulation reads

$$
D\,\vec{\mathbf{E}}+\vec{\mathbf{E}}\,\vec{\epsilon}=-\frac{\rho}{\sqrt{\epsilon}},
\qquad
D\,\vec{\mathbf{H}}+\vec{\mathbf{H}}\,\vec{\mu}=\sqrt{\mu}\,\mathbf{j},
$$

and both are instances of one operator problem: solve

$$
\left(D+M^{\vec{\alpha}}\right)\vec{F}=\vec{G},
\qquad
\vec{\alpha}=\frac{\mathrm{grad}\,\phi}{\phi},
$$

for some scalar $\phi\neq0$. The operator with the coefficient on the right has a complete and explicit theory, and its fundamental solution turns out to be an object already met in this article.

**Which side the coefficient multiplies.** The carrier identity disposes of one of the two possibilities at once. With the coefficient on the **left**, $D+M_{\vec{\alpha}}:g\mapsto Dg+\vec{\alpha}g$, the carrier identity applied to $\phi\to1/\phi$ gives $(D-M_{\vec{\alpha}})f=\phi\,D(f/\phi)$, so $D+M_{\vec{\alpha}}$ is $D$ conjugated by division by $\phi$ and is no harder than $D$. With the coefficient on the **right**, $D+M^{\vec{\alpha}}:g\mapsto Dg+g\vec{\alpha}$, no such conjugation exists. It is the right-multiplication operator that the reformulation produces, and it is the one with the Schrödinger connection.

**The reduction to the Schrödinger equation.** Let $\phi\neq0$ be a scalar, $\vec{\alpha}=\mathrm{grad}\,\phi/\phi$ and $v=\Delta\phi/\phi$, and let $\psi$ solve the Schrödinger equation

$$
-\Delta\psi+v\psi=0 .
$$

Then

$$
\vec{F}:=\left(D-\vec{\alpha}\right)\psi
$$

solves $(D+M^{\vec{\alpha}})\vec{F}=0$, that is $D\vec{F}+\vec{F}\vec{\alpha}=0$. Moreover, if $\psi$ is a *fundamental* solution of the operator $-\Delta+v$, then $\vec{F}$ is a fundamental solution of $D+M^{\vec{\alpha}}$. A first-order quaternionic operator with a gradient coefficient is thus reduced to a scalar Schrödinger equation, and the potential is not free: it is built from the same $\phi$ that produces the coefficient.

**The factorisation, and the Riccati equation.** The corresponding operator identity is a factorisation of the Schrödinger operator. For a scalar function $u$,

$$
\left(D+M^{\vec{\alpha}}\right)\left(D-M_{\vec{\alpha}}\right)u=(-\Delta+v)u
\qquad\text{provided}\qquad
D\vec{\alpha}+\vec{\alpha}^{2}=-v ,
$$

and $\vec{\alpha}=\mathrm{grad}\,\phi/\phi$ with $v=\Delta\phi/\phi$ satisfies that condition identically, the relation $D\vec{\alpha}+\vec{\alpha}^2=-v$ being equivalent to $-\Delta\phi+v\phi=0$. The relation is the quaternionic generalisation of the Riccati equation, and it is the same relation that appears in the corpus's treatment of the quaternionic Riccati equation. The factorisation is again a right-multiplication statement: with the coefficient on the left, the product $(D+M_{\vec{\alpha}})(D-M_{\vec{\alpha}})$ acquires the first-order remainder $2\sum_k(\partial_ku)(e_k\times\vec{\alpha})$, which vanishes only when $\vec{\alpha}$ is scalar, whereas the mixed operator above reproduces $(-\Delta+v)u$ exactly for scalar $u$. The asymmetry between the two sides is a property of the algebra, not of the notation.

**The same factorisation covers a whole family of operators — including the conductivity equation.** The factorisation above is the particular case $p=1$, $q=v$ of a more general identity, and the general identity is what connects the framework to the rest of mathematical physics. Let $p,q,u_0$ be complex-valued with $p\in C^2(\Omega)$, $p\neq0$ in $\Omega$, and let $u_0$ be a nonvanishing particular solution of the second-order equation

$$
(\mathrm{div}\,p\,\mathrm{grad}+q)u=0\qquad\text{in }\Omega .
$$

Put $f=p^{1/2}u_0$ and $\vec{\alpha}_f=\mathrm{grad}\,f/f$. Then for every scalar $\phi\in C^2(\Omega)$,

$$
(\mathrm{div}\,p\,\mathrm{grad}+q)\phi=-p^{1/2}\left(D+M^{\vec{\alpha}_f}\right)\left(D-M_{\vec{\alpha}_f}\right)p^{1/2}\phi ,
$$

with the same convention as in the paragraph above — the coefficient on the right in the factor carrying the plus sign, on the left in the factor carrying the minus sign; the source writes both factors with the one symbol $M_f$ and its $f$ is the carrier $p^{1/2}u_0$, not the coefficient. The identity was checked symbolically here in two cases, one with $p\neq1$ (the conductivity case $p=e^{2x_1}$, $q=0$, $f=e^{x_1}$) and one with a non-constant coefficient ($p=1$, $f=x_1^2+1$, $q=-\Delta f/f$); reversing the two multiplication sides makes the identity fail. So the second-order operator is *the same biquaternionic factorisation* for every choice of $p$ and $q$: the Schrödinger operator $-\Delta+v$ is the case $p=1$, $q=-v$; the **conductivity equation** $\mathrm{div}\,\sigma\,\mathrm{grad}\,u=0$ of a medium with conductivity $\sigma$ is the case $p=\sigma$, $q=0$ and $f=\sqrt{\sigma}\,u_0$; and each is carried by one and the same pair of first-order operators $D\pm M^{\vec{\alpha}_f}$. This is the precise sense in which the biquaternionic formulation is *one algebra, many equations*: not an analogy between separate reformulations but a single factorisation that specialises to each of them, with the carrier $f$ built from the zeroth-order coefficient in every case. The corpus had previously carried the Schrödinger member of this family and the riccati condition that selects its carrier; the general $(\mathrm{div}\,p\,\mathrm{grad}+q)$ member, and with it the conduction problem, is what the survey's operator-relation theme adds.

**The one-dimensional general solution: one particular solution generates them all.** The factorisation says what the carrier $f=p^{1/2}u_0$ *is*; it does not say what the solutions of the factorised equation are. In one dimension they are known explicitly, and the construction is precisely what the account above leaves open. Take the equation in Sturm–Liouville form,

$$
(pu')'+qu=\omega^2u,\qquad x\in[0,a],
$$

with $p,q,u$ complex-valued, $p\in C^1(0,a)$ bounded and nonvanishing, and $\omega$ an arbitrary complex number. Suppose that the auxiliary equation

$$
(pg_0')'+qg_0=0
$$

has a particular solution $g_0\in C^2(0,a)$ such that $g_0$ **and** $1/g_0$ are bounded on $[0,a]$ — nonvanishing, and nondegenerate at the endpoints — and put $g=\sqrt{pg_0}$. Then the general solution of the first equation is

$$
u=c_1u_1+c_2u_2,
\qquad
u_1=g_0\!\!\sum_{\substack{n=0\\ n\ \text{even}}}^{\infty}\!\!\frac{\omega^n\tilde X^{(n)}}{n!},
\qquad
u_2=g_0\!\!\sum_{\substack{n=1\\ n\ \text{odd}}}^{\infty}\!\!\frac{\omega^nX^{(n)}}{n!},
$$

where the coefficients are generated from $\tilde X^{(0)}=X^{(0)}\equiv1$ by two interleaved recursions,

$$
\tilde X^{(n)}(x)=
\begin{cases}
n\displaystyle\int_0^x\tilde X^{(n-1)}(\xi)\,g^{2}(\xi)\,d\xi, & n\ \text{odd},\\[6pt]
n\displaystyle\int_0^x\tilde X^{(n-1)}(\xi)\,g^{-2}(\xi)\,d\xi, & n\ \text{even},
\end{cases}
$$

$$
X^{(n)}(x)=
\begin{cases}
n\displaystyle\int_0^xX^{(n-1)}(\xi)\,g^{-2}(\xi)\,d\xi, & n\ \text{odd},\\[6pt]
n\displaystyle\int_0^xX^{(n-1)}(\xi)\,g^{2}(\xi)\,d\xi, & n\ \text{even}.
\end{cases}
$$

The two series are the even and the odd parts in $\omega$, and the coefficients are the initial data: $c_1=u(0)$ and $c_2=u'(0)$. The Wronskian of $u_1,u_2$ equals $1$ at $x=0$, because at zero every $\tilde X^{(n)}$ and $X^{(n)}$ with $n>0$ vanishes, so $u_1,u_2$ are linearly independent and the two series really do span the solution space. For the case $p=1$, which is the ordinary form $-u''+qu=0$, the same statement holds with $g$ absent and $q$ inserted in the recursion in place of $g^{\pm2}$: $\tilde X^{(n)}=n\int_0^x\tilde X^{(n-1)}d\xi$ for even $n$ and $n\int_0^x\tilde X^{(n-1)}q\,d\xi$ for odd $n$, and $X^{(n)}$ with the two cases exchanged. The recursion is the classical one — the series solution of a second-order linear equation was known in this form to Weyl, and it is the same representation used in inverse spectral theory — and what the paper contributes is the statement of the hypotheses under which it is uniformly usable, and the route to it through the theory of pseudoanalytic functions.

**The carrier of the series is the carrier of the factorisation.** The two carriers are the same function. The series is normalised by $g=\sqrt{pg_0}$ with $g_0$ a particular solution of $(pg_0')'+qg_0=0$; the factorisation above is carried by $f=p^{1/2}u_0$ with $u_0$ a nonvanishing particular solution of $(\mathrm{div}\,p\,\mathrm{grad}+q)u=0$. In one dimension the two equations are the same equation, so $g=f$ term by term. What the one-dimensional theory adds to the factorisation is the second boundedness condition: the factorisation needs only that $u_0$ be nonvanishing, while the series additionally needs $1/g_0$ bounded, and it is that reciprocal condition which makes the carrier and its square well behaved at both endpoints and hence makes the coefficients computable on the whole interval. The condition is concrete and checkable, and it is exactly the criterion a reader of the factorisation section would want and the section does not supply.

**Why $\omega$ is the right variable, and what the method is worth numerically.** The series is a power series in $\omega$ with coefficients independent of $\omega$. Once the $\tilde X^{(n)}$ and $X^{(n)}$ are computed to order $N$, an approximate solution is a polynomial in $\omega$ with those coefficients, so an initial-value problem is solved for all $\omega$ at once and a spectral problem in $\omega$ becomes root-finding for a polynomial. That is the property the older power-series representation of the same solution lacked: in the classical form the spectral parameter enters in a manner too complicated to be used quantitatively. The paper's motivating instance is electromagnetic, the equation $-u''+\omega^2q(x)u=0$ for different complex values of $\omega^2$ — the stratified-medium problem of Wait — which is the corpus's own frequency dependence, and the method returns the solution as a function of the wave number rather than one solution per wave number. The paper reports that the truncated series beats Matlab's adaptive solver `ode45` by several orders of magnitude on three test problems, and the figures are recorded as reported and not reproduced: for $q\equiv-c^2$ with initial data $u(0)=1$, $u'(0)=-1$ on $(0,1)$ it reports absolute and relative errors of order $10^{-16}$ and $10^{-14}$ for the series at $N=55$ to $58$ against $10^{-9}$ and $10^{-6}$ for `ode45` at $c=1$, and order $10^{-12}$ for both against $10^{-6}$ and $10^{-5}$ at $c=10$; for $q=c^2x^2+c$, where the exact solution is $u=e^{cx^2/2}\bigl(c_1+c_2\int_0^xe^{-ct^2}dt\bigr)$, the reported `ode45` absolute error at $c=30$ is $0.28$ against the series' $10^{-9}$. The comparison is the author's own, on Matlab 7, and it is a comparison with one adaptive solver rather than a benchmark; the corpus records it as an announced result. Two standing weaknesses of the paper are worth carrying with it. Every example is one-dimensional and the coefficients $p,q$ are smooth on a closed interval, so nothing here addresses a singular endpoint, where the boundedness of $1/g_0$ can fail; and the paper is a short announcement, so the convergence estimates are sketched through the Weierstrass test rather than developed.

**The three equations that follow from one solution.** The relations between the operators become relations between their solutions. Let the biquaternion-valued function $W$ solve the Vekua-type equation

$$
\left(D-\frac{Df}{f}\,\mathcal{C}\right)W=0 ,
$$

$\mathcal{C}$ being the conjugation operator of the algebra — the biquaternionic analogue of the $\bar{(\cdot)}$ in the prototype Vekua equation $w_{\bar z}=Aw+B\bar w$ discussed in the section above, which is why this is the same Vekua class and not merely a similar-looking equation. Write $W=W_0+\vec{W}$ for its scalar and vector parts. Then, as the source's Theorem 18 states, three consequences follow at once: the scalar part $W_0$ solves the **stationary Schrödinger equation**

$$
-\Delta W_0+\frac{\Delta f}{f}W_0=0 ,
$$

the function $u=f^{-1}W_0$ solves the **conductivity equation**

$$
\mathrm{div}\left(f^{2}\,\mathrm{grad}\,u\right)=0 ,
$$

and the vector part, rescaled as $v=f\vec{W}$, solves

$$
\mathrm{rot}\left(f^{-2}\,\mathrm{rot}\,v\right)=0 .
$$

One biquaternionic equation therefore carries a Schrödinger solution, a conductivity solution and a second-order curl equation at once, the three tied by the single carrier $f$. This is the operator-relation web the survey names in its abstract — "the Schrödinger, the Maxwell system, the conductivity equation and others" — and it is the reason the framework is worth the notation: the same first-order operator that reformulates Maxwell also factorises the conductivity equation, so a result about one is transferable to the others. The conduction member is the one this article had not carried; the corpus's treatment of the *lossy* Maxwell system in *The Time-Harmonic Maxwell Operator and the Quaternionic Cauchy Integral* uses a *constant* complex conductivity inside Maxwell, whereas the equation above is the *scalar, spatially varying* conductivity equation of a conduction problem, a different object reached by the same factorisation.

**An explicit fundamental solution.** The simplest case is a constant quotient. Let $\Delta\phi/\phi=-c^2$ throughout a domain, so that $\phi$ is a combination of exponentials $e^{ic\,\mathbf{n}\cdot\mathbf{x}}$ with $|\mathbf{n}|=1$. Then

$$
\psi(\mathbf{x})=\frac{e^{ic|\mathbf{x}|}}{4\pi|\mathbf{x}|}
$$

is the outgoing fundamental solution of $-\Delta-c^2$, and the construction gives the fundamental solution of $D+M^{\vec{\alpha}}$ in closed form,

$$
\vec{F}(\mathbf{x})
=\left(D-\frac{\mathrm{grad}\,\phi}{\phi}\right)\frac{e^{icr}}{4\pi r}
=-\left(\vec{\alpha}+\frac{\mathbf{x}}{r^{2}}-\frac{ic\,\mathbf{x}}{r}\right)\frac{e^{icr}}{4\pi r},
\qquad
r=|\mathbf{x}| .
$$

The authors remark that it is not clear how to obtain this result directly for the Maxwell operators $D+M^{\vec{\mu}}$ and $D+M^{\vec{\epsilon}}$ by other known methods.

**The recipe is the chiral recipe; the kernel is not the chiral kernel.** The bracketed factor has already appeared in this article, and it is worth saying exactly how far the resemblance goes. The fundamental solution of the chiral operator in *A Chiral Medium: One Quaternionic Equation* is

$$
\mathcal{K}_{\pm\alpha}=-(D_3\mp\alpha)\,\Theta_\alpha,
\qquad
\Theta_\alpha=-\frac{e^{i\alpha|\mathbf{x}|}}{4\pi|\mathbf{x}|},
$$

minus the first-order operator applied to the outgoing Helmholtz kernel of that same operator. The formula obtained above is the same display,

$$
\vec{F}(\mathbf{x})=-(D_3-\vec{\alpha})\,\Theta_c,
\qquad
\Theta_c=-\frac{e^{ic|\mathbf{x}|}}{4\pi|\mathbf{x}|},
$$

with the scalar shift $\alpha$ replaced by the vector coefficient $\vec{\alpha}$: indeed $-(D_3-\vec{\alpha})\Theta_c=-\nabla\Theta_c+\vec{\alpha}\Theta_c=(D-\vec{\alpha})\psi$ for $\psi=e^{icr}/4\pi r$. The two share the whole shape — the $\mathbf{x}/r^{2}$ and $i\alpha\mathbf{x}/r$ terms both come from differentiating $e^{i\alpha r}/4\pi r$ — and they differ in the one place that matters, namely the type of the coefficient. The chiral shift is a frequency-dependent *scalar*, so the chiral kernel is scalar-plus-vector, with scalar part $\alpha\Theta_\alpha$; the coefficient here is the *vector* $\mathrm{grad}\,\phi/\phi$ produced by an inhomogeneity, so this fundamental solution is a pure vector. The two are therefore **not** the same object, and the difference is not a sign: it is of order one. They coincide only in the degenerate case $\vec{\alpha}=0$, $c=0$, where both reduce to the classical spatial Cauchy kernel $-\mathbf{x}/(4\pi r^{3})$ of the unshifted operator. What is genuine, and worth keeping, is that one constructive recipe — apply the first-order operator to the outgoing Helmholtz kernel of the same operator — serves the chiral problem with a scalar shift and the inhomogeneous problem with a gradient coefficient alike; and that the recipe, not the kernel, is what the two have in common.

**What this adds, and what it does not.** The inhomogeneous branch of the framework now has four levels, and they should be kept apart. The exact reduction to a single Vekua-type equation holds for arbitrary $\epsilon(\mathbf{x})$ and $\mu(\mathbf{x})$ and for time-dependent fields, but it delivers an equation rather than a solution. The theory of the operator $D+M^{\vec{\alpha}}$ with a gradient coefficient is complete and explicit, and it delivers both the Schrödinger reduction and the closed-form fundamental solution, but only for coefficients of the carrier form $\mathrm{grad}\,\phi/\phi$, and, in the closed-form example, for the constant quotient $\Delta\phi/\phi=-c^2$. The general factorisation of $(\mathrm{div}\,p\,\mathrm{grad}+q)$, and with it the conductivity equation, is a third reading of the same first-order operators rather than a further level of the same branch: it is the widest statement of the factorisation, of which the Schrödinger reduction is the case $p=1$, and it is an operator identity rather than a solution. The one-dimensional general solution of the last of these is the fourth level, and it is where the chain finally closes on a formula: one bounded particular solution $g_0$ of the auxiliary equation, with $1/g_0$ bounded as well, generates the whole solution space of $(pu')'+qu=\omega^2u$ through two explicit recursions, so the reduction that stopped at an equation now ends at a solution — in one dimension, for smooth coefficients, and with the reciprocal boundedness as its price. What remains absent is the body of the general pseudoanalytic, or Vekua, function theory in more than one dimension that the Vekua reduction makes available — the corpus now carries its first layer, the generating quartet with the equation for $w$ and the inverse of the reduction, recorded in the next section, while the theory's own theorems, its similarity principle and its Liouville-type statements among them, are still not carried — a closed-form treatment of the time-dependent inhomogeneous problem, and any numerical work in this article beyond the one-dimensional series — the framework's other numerical method, the collocation scheme of the survey, is recorded in the chiral article where the scattering problem lives.

**A note on the two sources.** The material of these two sections is taken from V. V. Kravchenko, *Quaternionic reformulation of Maxwell's equations for inhomogeneous media and new solutions* (arXiv:math-ph/0104008) and *Quaternionic equation for electromagnetic fields in inhomogeneous media* (arXiv:math-ph/0202010), with one exception: the general $(\mathrm{div}\,p\,\mathrm{grad}+q)$ factorisation of the operator-relation web and the conductivity equation it carries are not in the 2001 paper, which stops at the Schrödinger member; they are cited in the Further Reading to the survey's reference $[29]$, V. V. Kravchenko, *J. Phys. A* **39** (2006) 12407–12425, which is also the primary source of the generating-quartet section below. Both papers write the Moisil–Teodoresco operator as $D=\sum_k i_k\partial_k$ with the quaternion units called $i_k$; the units $e_k$ of this article are the same objects, and their $D$ is the spatial part of the biquaternionic gradient fixed above. In the available text layer of both papers the distinction between the two multiplication operators $M_\alpha$ (left) and $M^\alpha$ (right) is not always preserved, so the multiplication order recorded here is not the printed order but the order that reproduces the equations: every statement above was checked numerically, and wherever the alternative order fails it fails by an $O(1)$ margin. One cross-article warning follows from this. In these two papers $M_{\vec\alpha}$ and $M^{\vec\alpha}$ are the left and the right multiplication operators, and that is the reading fixed in this article; in *Biquaternion Regular Functions* the symbol $M_\alpha$ of the shifted operator $D_\alpha=D+M_\alpha$ is a *right* multiplication, so the same letter carries the other side there.

## The Generating Quartet, the Pseudoanalytic Equation, and the Inverse of the Reduction

**The Vekua-type equation has four explicit solutions, and they generate all of them.** The operator-relation web above stops at an equation, and an equation is not a solution theory. The constructive half of that theory rests on a quartet. With $f\neq0$ the carrier and $Df/f=\mathrm{grad}\,f/f$ the coefficient, the four functions

$$
F_0=f,\qquad F_1=\frac{e_1}{f},\qquad F_2=\frac{e_2}{f},\qquad F_3=\frac{e_3}{f}
$$

all solve the Vekua-type equation $(D-\tfrac{Df}{f}\mathcal{C})W=0$. They solve it for one definite reading of $\mathcal{C}$ and of the side on which the coefficient multiplies. The algebra offers three conjugations — the **quaternion conjugation**, which keeps the scalar part and negates the vector part, the **complex conjugation** $i\mapsto-i$, and their composite — and to these the identity was added as a control, each of the four being tried on both sides. Only one of the eight cases makes all four members vanish, namely the quaternion conjugation multiplying on the left. Over sixty random carriers the residual of that case stays below $10^{-15}$, while the other seven lie between $7.4$ and $13.5$. The operator of the Vekua-type equation is therefore pinned by its own solutions, and the pinning has to be recorded because this question — which conjugation, which side — cannot be settled from the printed page: it is the same ambiguity that the two-source note at the end of the previous section raises for the multiplication side of $M_\alpha$.

**The quartet is a basis, and a generating one in the sense of Bers.** The four functions are independent over the constants, and *every* biquaternion-valued function $W$ can be written

$$
W=\sum_{k=0}^{3}\phi_kF_k
$$

with **complex**, not biquaternionic, coefficients. Those coefficients are forced: $F_1,F_2,F_3$ are purely vectorial and $F_0$ is scalar, so the scalar part of $W$ is $\phi_0f$ and its $e_k$-component is $\phi_k/f$, whence $\phi_0=W_0/f$ and $\phi_k=fW_k$ for $k=1,2,3$, and the expansion is unique. A solution space generated by four fixed functions, rather than described by a fundamental solution, is what the word *pseudoanalytic* names: this quartet is the three-dimensional counterpart of the generating pair $(F,G)$ of the plane theory, it is why the source records it "in complete analogy with the two-dimensional case" and cites Bers for the class, and it is the first layer of the theory that the Vekua paragraph above announced and left to the analysis cluster.

**The equation for $W$ becomes one equation for the coefficients.** Substituting the expansion into the Vekua-type equation gives an exact operator identity,

$$
\left(D-\frac{Df}{f}\,\mathcal{C}\right)\sum_{k=0}^{3}\phi_kF_k=\sum_{k=0}^{3}\bigl(D\phi_k\bigr)F_k ,
$$

true for arbitrary complex coefficients and not only for solutions of the equation. Hence $W$ solves the Vekua-type equation exactly when its coefficients satisfy the single biquaternionic relation

$$
\sum_{k=0}^{3}\bigl(D\phi_k\bigr)F_k=0 ,
$$

which, with the quartet written out, is $(D\phi_0)f+\frac{1}{f}\sum_{k=1}^{3}(D\phi_k)e_k=0$. The reduction has exchanged one first-order equation for a biquaternion-valued function for one first-order equation for four complex scalar functions — the same equation, counted the other way — and the second form is the one in which a Vekua equation is recognised: it relates the four coefficients to their first derivatives alone, with no algebraic unknown in between.

**And that condition is again a Vekua equation, now for the combination itself.** Put

$$
w=\phi_0+\phi_1e_1+\phi_2e_2+\phi_3e_3,
\qquad
\bar w=\phi_0-\phi_1e_1-\phi_2e_2-\phi_3e_3 ,
$$

the biquaternion assembled from the coefficients and its quaternion conjugate. Since $w+\bar w=2\phi_0$ and $w-\bar w=2(\phi_1e_1+\phi_2e_2+\phi_3e_3)$, the condition above reads $D(w+\bar w)f+\frac{1}{f}D(w-\bar w)=0$, which is equivalent to

$$
Dw=\frac{1-f^2}{1+f^2}\,D\bar w .
$$

This is the source's closing remark of the section, and it is the form in which the pseudoanalytic character of the problem is visible in one line: the two halves of $w$ appear side by side, the coefficient is a single scalar built from the carrier, and every trace of $\epsilon(\mathbf x)$ and $\mu(\mathbf x)$ has retreated into $f$. Two readings of the printed display have to be separated, because the bar is lost in its text layer and they are different equations. Read as a conjugation of the whole expression $Dw$, the right-hand side gives an equation that is **false**: for $f=3$ and the explicit solution $w=(x^2-y^2)+18yze_1+18xze_2$ of the condition above one has $Dw=-16x\,e_1+16y\,e_2$, and since $Dw$ is purely vectorial its quaternion conjugate is $-Dw$, so the two sides of that reading differ by $(1+\lambda)Dw$, that is by $-3.2x\,e_1+3.2y\,e_2$, where $\lambda=-4/5$ is the value of the coefficient at $f=3$. Read as a conjugation of the *function*, so that the right-hand side is $D\bar w$, the equation is exactly equivalent to the condition above — the two differ only by the proportionality factor $2f/(1+f^2)$, with residuals below $10^{-14}$ for arbitrary coefficients. The corpus records the second reading, and it is the one that matches the plane prototype $w_{\bar z}=Aw+B\bar w$, in which the conjugate always conjugates the function and never the derivative.

**The reduction also runs backwards, and its inverse is the classical recovery of a potential.** The local theory has an inverse as well as a forward map, and the inverse is the oldest construction in vector analysis rather than a new one. The forward map is $g\mapsto F=fD(f^{-1}g)$, the carrier identity read in the other direction: it sends every solution of the scalar equation $-\Delta g+\nu g=0$ to a solution of the first-order equation with the gradient coefficient carried on the operator, $(D+M^{\vec{\alpha}})F=0$ with $\vec{\alpha}=\mathrm{grad}\,f/f$, and it sends a fundamental solution of the scalar operator to a fundamental solution of the first-order one. The inverse is built from the operator

$$
A[G](\mathbf x)=\int_{x_0}^{x}G_1(\xi,y_0,z_0)\,d\xi+\int_{y_0}^{y}G_2(x,\zeta,z_0)\,d\zeta+\int_{z_0}^{z}G_3(x,y,\eta)\,d\eta+C ,
$$

the line integral along the three axis-parallel legs from a fixed base point to $\mathbf x$. For a gradient field $G=D\chi$ this integral is path-independent and returns $\chi(\mathbf x)-\chi(\mathbf x_0)$, so $A$ inverts $D$ on gradients: it is the standard recovery of a potential from its gradient, checked here to $10^{-15}$ on random polynomials. Since $f^{-1}F=D(f^{-1}g)$ is exactly such a gradient, the reconstruction $g=fA[f^{-1}F]$ returns the original scalar solution **up to an additive multiple of $f$**, and that multiple is precisely what the forward map cannot see, because $fD(f^{-1}cf)=fD(c)=0$ for every constant $c$. The two statements together make the correspondence between the scalar problem and the first-order problem a bijection up to the span of $f$; the same pair, with $u_0$ in place of the scalar solution and $f=p^{1/2}u_0$ as the carrier, does the same for the general $(\mathrm{div}\,p\,\mathrm{grad}+q)$ problem. What the reduction costs is therefore not information but one additive constant per solution — which is the sharpest available answer to the question whether the biquaternionic reformulation loses anything.

**Nothing in this section is three-dimensional.** The quartet, the condition on the coefficients, the equation for $w$ and the inverse all hold with the quaternion algebra replaced by the Clifford algebra $Cl_{0,n}$ of $n$-dimensional Euclidean space, the operator being read as $D=\sum_{j=1}^{n}e_j\,\partial_{x_j}$ in that algebra's units. The construction is dimensional rather than quaternionic: the quartet becomes a set of $n+1$ generating functions, the coefficients $\phi_k$ remain complex scalars, and the argument is unchanged. The source states this for its whole section, and it is the reason the framework is better described as a Clifford-analytic method with a distinguished four-dimensional case than as a quaternionic device.

**Provenance.** The quartet, the condition on the coefficients, the equation for $w$, the inverse theorem and the dimensional remark are the survey's restatement of its reference $[29]$, V. V. Kravchenko, "On a factorization of second order elliptic operators and applications", *Journal of Physics A: Mathematical and General* **39** (2006) 12407–12425, where they are its Theorems 15–18 and Remarks 19–20. The survey's own remarks place the earlier members of the chain: the Schrödinger factorisation in the Riccati form is in Bernstein (1996) and Bernstein–Gürlebeck (1999); the reduction of the biquaternionic Riccati equation to the carrier $Df/f$ is in Kravchenko–Kravchenko–Williams (2001); and the general $(\mathrm{div}\,p\,\mathrm{grad}+q)$ factorisation, with its three consequences, is $[29]$'s and **not** the 2001 paper's — that paper carries the Schrödinger reduction, the Riccati condition and the closed-form fundamental solution, and stops there. The general factorisation is cited to $[29]$ in the Further Reading below.

## Boundary Conditions at an Interface

At a surface separating two media, the fields are matched by the integral form of Maxwell's equations. Let $\hat{\mathbf{n}}$ be the unit normal pointing from medium $1$ to medium $2$. With no free surface charge and no free surface current,
$$
\hat{\mathbf{n}}\cdot(\mathbf{D}_2-\mathbf{D}_1)=0,
\qquad
\hat{\mathbf{n}}\cdot(\mathbf{B}_2-\mathbf{B}_1)=0,
$$
$$
\hat{\mathbf{n}}\times(\mathbf{E}_2-\mathbf{E}_1)=0,
\qquad
\hat{\mathbf{n}}\times(\mathbf{H}_2-\mathbf{H}_1)=0 .
$$
With a surface charge density $\sigma_s$ and a surface current density $\mathbf{K}_s$ the first and last become $\hat{\mathbf{n}}\cdot(\mathbf{D}_2-\mathbf{D}_1)=\sigma_s$ and $\hat{\mathbf{n}}\times(\mathbf{H}_2-\mathbf{H}_1)=\mathbf{K}_s$. In words: the normal component of $\mathbf{D}$ and the normal component of $\mathbf{B}$ are continuous up to surface sources, and the tangential components of $\mathbf{E}$ and $\mathbf{H}$ are continuous.

The biquaternionic field strength is assembled from the local values of $\epsilon$ and $\mu$, so it is **discontinuous** at an interface even though the physical fields obey the conditions above. Splitting off the tangential part, with unit normal $\hat{\mathbf{n}}$,
$$
\hat{\mathbf{n}}\times\tilde{F}
=i\sqrt{\epsilon}\,\left(\hat{\mathbf{n}}\times\mathbf{E}\right)
-\sqrt{\mu}\,\left(\hat{\mathbf{n}}\times\mathbf{H}\right).
$$
The tangential combinations $\hat{\mathbf{n}}\times\mathbf{E}$ and $\hat{\mathbf{n}}\times\mathbf{H}$ are continuous across the interface, but the coefficients $\sqrt{\epsilon}$ and $\sqrt{\mu}$ are not, so the left-hand side jumps. Similarly, for the normal part,
$$
\hat{\mathbf{n}}\cdot\tilde{F}
=i\sqrt{\epsilon}\,E_n-\sqrt{\mu}\,H_n
=\frac{i}{\sqrt{\epsilon}}\,D_n-\frac{1}{\sqrt{\mu}}\,B_n,
$$
in which $D_n$ and $B_n$ are continuous while $\sqrt{\epsilon}$ and $\sqrt{\mu}$ jump.

The jump in $\tilde{F}$ is therefore not a physical discontinuity of the fields; it is the expression of a change of the local complex structure. The same physical fields are written in the normalisation of the medium on each side, and the interface is where two local complex structures meet. No single biquaternionic continuity statement replaces the four standard conditions: the medium enters precisely as the discontinuity of the local normalisation.

For two homogeneous media the boundary conditions give Snell's law,
$$
n_1\sin\theta_1=n_2\sin\theta_2,
$$
and, at normal incidence, reflection and transmission coefficients determined by the impedance mismatch,
$$
r=\frac{Z_2-Z_1}{Z_2+Z_1},
\qquad
t=\frac{2Z_2}{Z_1+Z_2},
$$
with reflectance $R=|r|^2$ and transmittance $T=(Z_1/Z_2)|t|^2$ satisfying $R+T=1$. The mismatch $Z_2-Z_1$ is the quantity that controls the reflected wave, and in the variables of this article it is the mismatch between the two local normalisations $\sqrt{\mu_i/\epsilon_i}$. The general oblique-incidence Fresnel coefficients depend on the polarisation; the point for the framework is that the interface is where the local complex structure changes, and the boundary conditions are the matching data across that change.

## Conventions for a Plane Wave in the Medium

This section fixes the conventions for the later exercise on plane-wave propagation in a medium. Work in a homogeneous medium with real, possibly frequency-dependent, $\epsilon(\omega)$ and $\mu(\omega)$, and use the complex-amplitude convention
$$
\mathbf{E}(\mathbf{x},t)=\mathrm{Re}\!\left[\mathbf{E}_0\,e^{\,i(\mathbf{k}\cdot\mathbf{x}-\omega t)}\right],
\qquad
\mathbf{H}(\mathbf{x},t)=\mathrm{Re}\!\left[\mathbf{H}_0\,e^{\,i(\mathbf{k}\cdot\mathbf{x}-\omega t)}\right],
$$
with complex amplitude vectors $\mathbf{E}_0,\mathbf{H}_0$ and real $\omega>0$ and $\mathbf{k}$. This fixes the sign convention; the opposite choice $e^{-i(\mathbf{k}\cdot\mathbf{x}-\omega t)}$ is equivalent under $\mathbf{k}\to-\mathbf{k}$, $\omega\to-\omega$.

For a source-free plane wave, $\tilde{\nabla}\tilde{F}=0$ is equivalent to the four algebraic conditions
$$
\mathbf{k}\cdot\mathbf{E}_0=0,
\qquad
\mathbf{k}\cdot\mathbf{H}_0=0,
\qquad
\mathbf{k}\times\mathbf{E}_0=\omega\mu\,\mathbf{H}_0,
\qquad
\mathbf{k}\times\mathbf{H}_0=-\omega\epsilon\,\mathbf{E}_0,
$$
from which
$$
\mathbf{k}^2=\omega^2\epsilon\mu=\frac{\omega^2}{c^2},
\qquad
\mathbf{H}_0=\frac{1}{Z}\,\hat{\mathbf{k}}\times\mathbf{E}_0,
\qquad
Z=\sqrt{\frac{\mu}{\epsilon}},
$$
with $\hat{\mathbf{k}}=\mathbf{k}/|\mathbf{k}|$. In particular the amplitudes satisfy
$$
|\mathbf{E}_0|=Z\,|\mathbf{H}_0|,
\qquad
|\mathbf{E}_0|=c\,|\mathbf{B}_0|,
$$
and the field-strength amplitude is
$$
\tilde{F}_0=i\sqrt{\epsilon}\,\mathbf{E}_0-\sqrt{\mu}\,\mathbf{H}_0
=i\sqrt{\epsilon}\left(\mathbf{E}_0+i\,\hat{\mathbf{k}}\times\mathbf{E}_0\right)
=i\sqrt{\epsilon}\,\mathbf{V}_0,
$$
with $\mathbf{V}_0=\mathbf{E}_0+ic\mathbf{B}_0=\mathbf{E}_0+i\,\hat{\mathbf{k}}\times\mathbf{E}_0$. The two normalised contributions have equal magnitude,
$$
\left|\sqrt{\epsilon}\,\mathbf{E}_0\right|
=\left|\sqrt{\mu}\,\mathbf{H}_0\right|,
$$
and the field-strength amplitude is **null**,
$$
N(\tilde{F}_0)=\sum_{k=1}^{3}\left(F_{0k}\right)^2=0 .
$$
A free plane wave in the medium is therefore a zero divisor of $\mathbb{B}$, exactly as a radiation field is in vacuum; the zero-divisor cone of the algebra is the wave cone of the medium.

The time-averaged energy density and energy flux are
$$
\langle W\rangle=\frac{1}{4}\left(\epsilon\,|\mathbf{E}_0|^2+\mu\,|\mathbf{H}_0|^2\right),
\qquad
\langle\mathbf{S}\rangle=\frac{1}{2}\,\mathrm{Re}\!\left(\mathbf{E}_0\times\mathbf{H}_0^{*}\right),
$$
and in the non-dispersive case these satisfy $|\langle\mathbf{S}\rangle|=c\,\langle W\rangle$. These are the quantities in which the medium speed and impedance appear on the same footing as the fields.

## The Vacuum Limit

The vacuum is the special case $\epsilon=\epsilon_0$, $\mu=\mu_0$, $c=c_0$, $Z=Z_0$, and every formula above must reduce to the corresponding vacuum statement. The field strength becomes
$$
\tilde{F}=i\sqrt{\epsilon_0}\,\mathbf{E}-\sqrt{\mu_0}\,\mathbf{H},
$$
the gradient becomes $\tilde{\nabla}=e_0\partial_{ic_0t}+e_1\partial_x+e_2\partial_y+e_3\partial_z$, and the d'Alembertian becomes $\Box=\Delta-c_0^{-2}\partial_t^2$. The complex time coordinate becomes $ic_0t$, recovering the familiar $ict$ form with the vacuum speed of light, and the local complex structure becomes constant. The invariants become $I_1=\mathbf{E}^2-c_0^2\mathbf{B}^2$ and $I_2=\mathbf{E}\cdot\mathbf{B}$, the Riemann–Silberstein vector becomes $\mathbf{V}=\mathbf{E}+ic_0\mathbf{B}$, and the plane-wave conditions become $\mathbf{k}^2=\omega^2/c_0^2$, $|\mathbf{E}_0|=c_0|\mathbf{B}_0|$, and $N(\tilde{F}_0)=0$, all as in the parent article. The impedance becomes $Z_0=\sqrt{\mu_0/\epsilon_0}$, and the refractive index becomes $n=1$.

This is the check that the medium conventions are consistent. Every medium result is the general one, and the vacuum results are recovered by setting the two medium parameters to their vacuum values. In particular, the null condition and the zero-divisor structure of the field strength are not special to vacuum; they hold in every medium, with the medium speed defining the cone. The question of which of $c_0$ and $(\epsilon_0,\mu_0)$ is fundamental — whether the vacuum has electromagnetic properties in the same sense that a medium does — is discussed in the Maxwell article and is not settled here.

## Beyond the Linear Constitutive Relation

Everything above assumes a linear constitutive map. This article has already met two departures from it — the dispersive medium, where $\epsilon$ and $\mu$ depend on frequency, and the chiral medium, where the relations couple $\mathbf{E}$ and $\mathbf{H}$ — and there is a third, which the corpus should name because a deformed arena produces it. A constitutive relation can differ from $\mathbf{D}=\epsilon\mathbf{E}$, $\mathbf{B}=\mu\mathbf{H}$ in three ways, and the three behave differently.

**Rescale.** The parameters become functions of position or of frequency. The reduction keeps its order and its finite kernel, and the vacuum limit is recovered point by point. This is the bulk of the article and the bulk of the linear theory.

**Raise the order.** The chiral relations couple the two fields, and the reduced equation is no longer the same operator with new coefficients; this is the chiral section above, and it is why that case is developed separately.

**Lose linearity.** The displacement and the induction acquire terms quadratic in the fields. The equations keep their first order, but the theory is no longer linear, and the reduction that this article performs does not apply.

The third case is realized by the non-commutative vacuum of *Maxwell's Theory on Non-Commutative Spaces and Quaternions*: there the source-free equations have the same first-order form as above, with $\mathbf{D}=\mathbf{E}+\mathbf{d}$ and $\mathbf{H}=\mathbf{B}+\mathbf{h}$ where $\mathbf{d}$ and $\mathbf{h}$ are quadratic in the fields, so that the deformed vacuum behaves as a medium with **non-linear** properties. Two features of such a medium are general, and neither is visible in the two linear cases.

**Plane waves can survive the non-linearity.** In the deformed vacuum a plane wave still solves the field equations exactly. So "plane wave" does not imply a linear theory, and the use of plane waves elsewhere in the corpus as a probe of the linear regime carries that qualification. What fails is the superposition principle, not the plane-wave Ansatz.

**An energy density exists only if the constitutive map is integrable.** For a non-linear medium the combination $\mathbf E\cdot\delta\mathbf D+\mathbf H\cdot\delta\mathbf B$ must be an exact one-form, and when it is, the energy density is fixed by it; the deformed vacuum is such a case, and the energy density it gives is quoted in that article. A linear medium satisfies the condition trivially, which is why this article has never had to state it, and the Brillouin energy of the dispersive case is the same requirement with the frequency carried inside the constitutive map. A non-linear medium whose constitutive map is not integrable would have **no** energy density, which is a real restriction on which non-linear media are physical and not a technicality.

## Summary

Electromagnetism in a material medium is developed here as the general case, with the vacuum as its limit. The constitutive relations $\mathbf{D}=\epsilon\mathbf{E}$ and $\mathbf{B}=\mu\mathbf{H}$ supply the two parameters of a homogeneous medium, which may be taken as the speed $c=1/\sqrt{\epsilon\mu}$ and the impedance $Z=\sqrt{\mu/\epsilon}$, or equivalently as $\epsilon=1/(cZ)$ and $\mu=Z/c$.

The medium enters the biquaternionic structure in two places and nowhere else. First, through $c$ in the gradient, $\partial_{ict}=-(i/c)\partial_t$, so that the map from physical time to the imaginary scalar direction of $\mathbb{B}$ carries the local scale $c$; this is the sense in which the complex structure is local, the algebra being fixed while its embedding in physical spacetime is not. Second, through the normalisations $\sqrt{\epsilon},\sqrt{\mu}$ of the field strength and the corresponding $1/\sqrt{\epsilon},\sqrt{\mu}$ of the source biquaternion
$$
\tilde{F}=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H},
$$
which is fixed by the parent article and splits $\tilde{F}$ into a Hermitian electric half in $\mathbb{M}_+$ and an anti-Hermitian magnetic half in $\mathbb{M}_-$; the medium sets the relative weight $Z=\sqrt{\mu/\epsilon}$ of the two halves.

The single biquaternionic Maxwell equation $\tilde{\nabla}\tilde{F}=-\tilde{R}$ is medium-independent in form, the factors $\sqrt{\epsilon}$ and $\sqrt{\mu}$ cancelling through $\sqrt{\epsilon}/(c\sqrt{\mu})=\epsilon$ and $\sqrt{\mu}/(c\sqrt{\epsilon})=\mu$. Dispersion makes the local complex structure spectral: each frequency carries its own speed $c(\omega)=1/\sqrt{\epsilon(\omega)\mu(\omega)}$, refractive index $n(\omega)=c_0/c(\omega)$, dispersion relation $k^2=\omega^2\epsilon(\omega)\mu(\omega)$, and group velocity $v_g=c_0/(n+\omega\,dn/d\omega)$, at least while the normalisation is real. At an interface the local complex structure jumps, and the field strength is discontinuous even though the physical fields satisfy the standard tangential and normal continuity conditions. The vacuum limit $c\to c_0$, $Z\to Z_0$ recovers every object of the parent article, and the zero-divisor cone of the algebra coincides with the wave cone of the medium at every value of $c$.

For a plane wave in the medium, the conventions fixed above are: complex amplitudes in the $e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}$ convention, transversality $\mathbf{k}\cdot\mathbf{E}_0=\mathbf{k}\cdot\mathbf{H}_0=0$, the relations $\mathbf{k}\times\mathbf{E}_0=\omega\mu\mathbf{H}_0$ and $\mathbf{k}\times\mathbf{H}_0=-\omega\epsilon\mathbf{E}_0$, the dispersion relation $k=\omega/c(\omega)=n(\omega)\omega/c_0$, and the impedance relation $\mathbf{H}_0=Z^{-1}\hat{\mathbf{k}}\times\mathbf{E}_0$. In these conventions $|\mathbf{E}_0|=Z|\mathbf{H}_0|=c|\mathbf{B}_0|$, the two normalised halves of $\tilde{F}_0$ have equal magnitude, and $N(\tilde{F}_0)=0$.

A chiral medium is the one constitutive case recorded here that changes the *order* of the reduction rather than only its parameters. With the Drude–Born–Fedorov relations $\mathbf{D}=\epsilon(\mathbf{E}+\beta\,\mathrm{rot}\,\mathbf{E})$ and $\mathbf{B}=\mu(\mathbf{H}+\beta\,\mathrm{rot}\,\mathbf{H})$ the time-dependent Maxwell system still reduces to a single quaternionic equation, but its operator $M=\beta\sqrt{\epsilon\mu}\,\partial_tD+\sqrt{\epsilon\mu}\,\partial_t-iD$ is of second order, its wave equations are of fourth order, and its frequency symbol factors as $i(\beta\sqrt{\epsilon\mu}\,\omega-1)(D+\alpha(\omega))$ with a frequency-dependent $\alpha$ that degenerates at $\omega=c/\beta$. The non-chiral reduction $\sqrt{\epsilon\mu}\,\partial_t-iD$ is the $\beta=0$ member of that family. The same fourth-order equation carries the medium's birefringence, with the two refractive indices $n_\pm(\omega)=1/(1\mp\beta\omega/c)$; and the fundamental solution of $M$ is causal by construction, built from the retarded kernel $K_\alpha$ with a displaced pole in the upper half-frequency plane.

A third kind of constitutive law is not a case of the reduction at all. If $\mathbf{D}$ and $\mathbf{H}$ acquire terms quadratic in the fields, the equations keep their first order but the theory becomes non-linear: superposition fails, an energy density exists only when the constitutive one-form $\mathbf E\cdot\delta\mathbf D+\mathbf H\cdot\delta\mathbf B$ is integrable, and the reduction performed in this article does not apply — even though a plane wave can still be an exact solution. The non-commutative vacuum of *Maxwell's Theory on Non-Commutative Spaces and Quaternions* is the corpus's worked example, and the section *Beyond the Linear Constitutive Relation* states the general situation.

The time-harmonic companion of the chiral reduction — the diagonalization into the two circular combinations with the two wavenumbers, the integral representations, the extendability problem, the energy balance and the inhomogeneous chiral medium — is not repeated here; it is carried by the dedicated article *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation*.

Beyond the chiral case, inhomogeneity is now handled in two ways that are not the same kind of result. For a medium with arbitrary $\epsilon(\mathbf{x})$ and $\mu(\mathbf{x})$ and no small parameter, the Maxwell system has an exact quaternionic equivalent,
$$
D\,\vec{\mathbf{E}}+\vec{\mathbf{E}}\,\vec{\epsilon}
=-\frac{1}{c}\,\partial_t\vec{\mathbf{H}}-\frac{\rho}{\sqrt{\epsilon}},
\qquad
D\,\vec{\mathbf{H}}+\vec{\mathbf{H}}\,\vec{\mu}
=\frac{1}{c}\,\partial_t\vec{\mathbf{E}}+\sqrt{\mu}\,\mathbf{j},
$$
with the normalised fields $\vec{\mathbf{E}}=\sqrt{\epsilon}\,\mathbf{E}$, $\vec{\mathbf{H}}=\sqrt{\mu}\,\mathbf{H}$ and the half-gradients $\vec{\epsilon}=\mathrm{grad}\sqrt{\epsilon}/\sqrt{\epsilon}$, $\vec{\mu}=\mathrm{grad}\sqrt{\mu}/\sqrt{\mu}$; and in one line,
$$
\left(\frac{1}{c}\,\partial_t+iD\right)f-f\,(i\vec{c})-f^{*}\,(i\vec{Z})
=-\left(\sqrt{\mu}\,\mathbf{j}+\frac{i\rho}{\sqrt{\epsilon}}\right),
\qquad
f=\sqrt{\epsilon}\,\mathbf{E}+i\sqrt{\mu}\,\mathbf{H},
$$
which is a **Vekua equation** — a first-order equation whose coefficients act on both $f$ and its conjugate — and therefore the governing equation of the pseudoanalytic functions. The entire reduction rests on two identities: the **carrier identity** $(D\pm\mathrm{grad}\,\phi/\phi)\,g^{(\mp)}=\phi^{(\mp1)}D(\phi^{(\pm1)}g)$, which makes a coefficient of the form $\mathrm{grad}\,\phi/\phi$ removable by conjugation, and the scalar-product identity $\langle\mathbf{p},\mathbf{q}\rangle=-\tfrac12(\mathbf{p}\mathbf{q}+\mathbf{q}\mathbf{p})$, which converts the scalar products of the divergence equations into products the carrier can absorb. The carriers of the divergence equations are $\sqrt{\epsilon}$ and $\sqrt{\mu}$, which is why those square roots appear in the normalisation of the field strength and not only for dimensional reasons. The price is that this is a reduction to an equation and not to a solution: the time-dependent inhomogeneous problem in closed form is not part of the framework, and the closed form given below reaches only the stationary one-dimensional case.

The one instance of the reduced problem that is completely solvable is the operator $D+M^{\vec{\alpha}}$ with the gradient coefficient $\vec{\alpha}=\mathrm{grad}\,\phi/\phi$, and it is solvable by reduction to a scalar Schrödinger equation: with $v=\Delta\phi/\phi$, every solution $\psi$ of $-\Delta\psi+v\psi=0$ produces a solution $\vec{F}=(D-\vec{\alpha})\psi$ of $(D+M^{\vec{\alpha}})\vec{F}=0$, and a fundamental solution of $-\Delta+v$ produces a fundamental solution of $D+M^{\vec{\alpha}}$. The operator identity behind this is the factorisation $(D+M^{\vec{\alpha}})(D-M_{\vec{\alpha}})u=(-\Delta+v)u$ for scalar $u$, valid whenever $D\vec{\alpha}+\vec{\alpha}^2=-v$, which is the quaternionic generalisation of the Riccati equation. When $\Delta\phi/\phi=-c^2$ is constant the fundamental solution is explicit,
$$
\vec{F}(\mathbf{x})=-\left(\vec{\alpha}+\frac{\mathbf{x}}{r^{2}}-\frac{ic\,\mathbf{x}}{r}\right)\frac{e^{icr}}{4\pi r},
$$
and this is built by the same constructive recipe as the causal kernel of the chiral problem — minus the first-order operator applied to the outgoing Helmholtz kernel — with the vector gradient coefficient $\mathrm{grad}\,\phi/\phi$ standing where the chiral problem has the frequency-dependent scalar shift $\alpha(\omega)$. The two kernels therefore share their shape and not their value: the chiral one is scalar-plus-vector, this one is a pure vector, and they differ by an $O(1)$ amount that vanishes only in the degenerate unshifted case, where both are the classical Cauchy kernel. The multiplication side is not cosmetic here either: the factorisation holds with the coefficient on the right, and the left-handed version leaves a first-order remainder.

The same factorisation is not special to the Schrödinger operator. For scalar complex $p,q$ and a nonvanishing particular solution $u_0$ of $(\mathrm{div}\,p\,\mathrm{grad}+q)u=0$, with the carrier $f=p^{1/2}u_0$, the identity $(\mathrm{div}\,p\,\mathrm{grad}+q)\phi=-p^{1/2}(D+M^{\vec{\alpha}_f})(D-M_{\vec{\alpha}_f})p^{1/2}\phi$ holds for every scalar $\phi$, $\vec{\alpha}_f=\mathrm{grad}\,f/f$. The Schrödinger operator is the case $p=1$, and the **conductivity equation** $\mathrm{div}\,\sigma\,\mathrm{grad}\,u=0$ is the case $p=\sigma$, $q=0$ — so the conduction problem is factorised by the very same operators that reformulate Maxwell. One solution $W$ of the Vekua-type equation $(D-\tfrac{Df}{f}\mathcal{C})W=0$ carries three equations at once: its scalar part solves the stationary Schrödinger equation with potential $\Delta f/f$, the function $f^{-1}W_0$ solves the conductivity equation, and the rescaled vector part solves $\mathrm{rot}(f^{-2}\mathrm{rot}\,v)=0$. This is the survey's *one algebra, many equations* statement, and it is the reason the conduction operator and the Schrödinger operator are not separate reformulations but two readings of the same factorisation.

That factorisation is a statement about operators, and in one dimension it can be completed from a statement about operators into a formula. If the auxiliary equation $(pg_0')'+qg_0=0$ has a particular solution $g_0$ that is bounded on the interval together with $1/g_0$, then with $g=\sqrt{pg_0}$ the general solution of $(pu')'+qu=\omega^2u$ is $u=c_1u_1+c_2u_2$, where $u_1$ and $u_2$ are the even and odd parts in $\omega$ of a series normalised by $g_0$ whose coefficients are generated by two interleaved integral recursions, and $c_1=u(0)$, $c_2=u'(0)$. The carrier $g=\sqrt{pg_0}$ of the series is term by term the carrier $f=p^{1/2}u_0$ of the factorisation, and what the series adds to it is the requirement that the reciprocal be bounded, which is what makes the coefficients computable across the whole interval. The series is a power series in $\omega$, so the solution is delivered for all frequencies at once and a spectral problem becomes root-finding for a polynomial; the paper reports the truncated series more accurate than Matlab's adaptive solver on three test problems.

The equation that the reduction produces has a solution theory of its own, and it is not a theory of one fundamental solution. Four generating solutions, $F_0=f$ and $F_k=e_k/f$ for $k=1,2,3$, solve the Vekua-type equation — for one definite reading of the conjugation $\mathcal{C}$ and of the side on which the coefficient multiplies, neither of which the printed page fixes and both of which the numerics do — and every biquaternion-valued function is a **unique** combination $W=\sum_k\phi_kF_k$ with complex coefficients, so the solution space is generated by four fixed functions rather than described by a kernel. Substituting that expansion turns the equation for $W$ into the single condition $\sum_k(D\phi_k)F_k=0$ on the coefficients, which is in turn equivalent to the Vekua equation $Dw=\frac{1-f^2}{1+f^2}D\bar w$ for their combination $w=\sum_k\phi_ke_k$ — the operator relation of the factorisation, now written for the solution itself. The reduction also has an inverse: the operator $A[G]$ of the axis-parallel line integral recovers a potential from its gradient, so that the correspondence between the scalar problem and the first-order problem is a bijection up to the additive multiples of the carrier $f$, the only thing the forward map cannot see. The construction is dimensional rather than quaternionic, and holds with the quaternion algebra replaced by the Clifford algebra $Cl_{0,n}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{C}_{\mathbb{B}},\mathbb{H}_{\mathbb{B}}$ | Scalar subspace, real-quaternion subspace |
| $\mathbb{M}_+,\mathbb{M}_-$ | Hermitian and anti-Hermitian subspaces |
| $\tilde{\nabla},\tilde{\nabla}^{\natural}$ | Biquaternionic gradient and its quaternion conjugate |
| $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\Delta-c^{-2}\partial_t^2$ | d'Alembertian in the medium |
| $\epsilon,\mu$ | Permittivity and permeability of the medium |
| $\epsilon_0,\mu_0$ | Vacuum permittivity and permeability |
| $\mathbf{D}=\epsilon\mathbf{E},\ \mathbf{B}=\mu\mathbf{H}$ | Constitutive relations |
| $c=1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0=1/\sqrt{\epsilon_0\mu_0}$ | Vacuum speed of light |
| $Z=\sqrt{\mu/\epsilon}$ | Wave impedance of the medium; $Z_0=\sqrt{\mu_0/\epsilon_0}\approx376.73\,\Omega$ |
| $n(\omega)=c_0/c(\omega)$ | Refractive index |
| $\tilde{F}=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}=i\sqrt{\epsilon}\,\mathbf{V}$ | Field-strength biquaternion (pure vector) |
| $\tilde{A}=i\phi/c+\mathbf{A}$ | Potential biquaternion |
| $\tilde{R}=i\rho/\sqrt{\epsilon}+\sqrt{\mu}\,\mathbf{J}$ | Source biquaternion |
| $\tilde{R}'=ic\rho+\mathbf{J}$ | Source biquaternion of the potential equation |
| $\mathbf{V}=\mathbf{E}+ic\mathbf{B}$ | Riemann–Silberstein vector |
| $I_1=\mathbf{E}^2-c^2\mathbf{B}^2,\ I_2=\mathbf{E}\cdot\mathbf{B}$ | Lorentz invariants of the field |
| $N(\tilde{F}) = \langle\tilde{F},\tilde{F}\rangle_{\natural}=\tilde{F}\tilde{F}^{\natural}$ | Biquaternion norm (complex scalar) |
| $W=\tfrac{1}{2}(\epsilon\mathbf{E}^2+\mu\mathbf{H}^2)$ | Electromagnetic energy density |
| $\mathbf{S}=\mathbf{E}\times\mathbf{H}$ | Poynting vector |
| $\mathbf{k},\omega$ | Wavevector and angular frequency |
| $\hat{\mathbf{k}}=\mathbf{k}/|\mathbf{k}|$ | Unit wavevector |
| $\beta$ | Chirality measure of a Drude–Born–Fedorov medium (a length) |
| $D=i_1\partial_{x_1}+i_2\partial_{x_2}+i_3\partial_{x_3}$ | Moisil–Teodoresco operator of the chiral reduction |
| $M=\beta\sqrt{\epsilon\mu}\,\partial_tD+\sqrt{\epsilon\mu}\,\partial_t-iD$ | Quaternionic operator of the chiral Maxwell system |
| $\mathbf{V}=\mathbf{E}-i\sqrt{\mu/\epsilon}\,\mathbf{H}$ | Purely vectorial field of the chiral reduction |
| $\alpha(\omega)=\sqrt{\epsilon\mu}\,\omega/(\beta\sqrt{\epsilon\mu}\,\omega-1)$ | Frequency-dependent Moisil–Teodoresco parameter of $M(\omega)$ |
| $\omega=c/\beta$ | Degenerate frequency of the chiral reduction; $a=1/(\beta\sqrt{\epsilon\mu})$ |
| $\Theta_\alpha,K_\alpha$ | Helmholtz kernel and Moisil–Teodoresco fundamental solution |
| $n_\tau(\omega)=1/(1-\tau\beta\omega/c),\ \tau=\pm1$ | The two refractive indices of the chiral medium |
| $D=e_1\partial_x+e_2\partial_y+e_3\partial_z$ | Moisil–Teodoresco operator in the sources' normalisation, $D^2=-\Delta$ (the same object as the chiral row's $D=i_1\partial_{x_1}+i_2\partial_{x_2}+i_3\partial_{x_3}$) |
| $\epsilon(\mathbf{x}),\mu(\mathbf{x})$ | Inhomogeneous permittivity and permeability |
| $\vec{\epsilon}=\tfrac12\mathrm{grad}\,\epsilon/\epsilon,\ \vec{\mu}=\tfrac12\mathrm{grad}\,\mu/\mu$ | Half-gradients of the two medium parameters |
| $\vec{\mathbf{E}}=\sqrt{\epsilon}\,\mathbf{E},\ \vec{\mathbf{H}}=\sqrt{\mu}\,\mathbf{H}$ | Fields normalised by the carrier functions |
| $f=\vec{\mathbf{E}}+i\vec{\mathbf{H}}$ | Field of the Vekua equation; $\tilde{F}=if$ |
| $\vec{c}=\tfrac12\mathrm{grad}\ln c,\ \vec{Z}=\tfrac12\mathrm{grad}\ln Z$ | Coefficient vectors of the Vekua equation (the source's $\vec{c}$ and $\vec{W}$) |
| $\phi$ | Carrier function of the identity $(D\pm\mathrm{grad}\,\phi/\phi)g^{(\mp)}=\phi^{(\mp1)}D(\phi^{(\pm1)}g)$ |
| $\vec{\alpha}=\mathrm{grad}\,\phi/\phi$ | Gradient coefficient of the operator $D+M^{\vec{\alpha}}$ |
| $v=\Delta\phi/\phi,\ \psi$ | Schrödinger potential and solution, $-\Delta\psi+v\psi=0$ |
| $p,\ q,\ u_0$ | Coefficients of the general operator $\mathrm{div}\,p\,\mathrm{grad}+q$ and a nonvanishing particular solution |
| $f=p^{1/2}u_0$ | Carrier function of the general factorisation; $f=\sqrt{\sigma}\,u_0$ for the conductivity equation |
| $g_0,\ g=\sqrt{pg_0}$ | Bounded particular solution of the auxiliary equation $(pg_0')'+qg_0=0$ and the carrier of the one-dimensional series; $g_0$ and $1/g_0$ bounded |
| $\tilde X^{(n)},X^{(n)}$ | Coefficients of the two series of the one-dimensional general solution, generated by the interleaved recursions from $\tilde X^{(0)}=X^{(0)}=1$ |
| $\sigma=f^{2}$ | Conductivity of the conduction problem reached by the same factorisation |
| $\mathcal{C}$ | Quaternion conjugation of the Vekua-type equation $(D-\tfrac{Df}{f}\mathcal{C})W=0$: scalar part kept, vector part negated (the complex conjugation and the composite do not solve it) |
| $F_0=f,\ F_k=e_k/f$ | Generating quartet of the Vekua-type equation, $k=1,2,3$ |
| $\phi_k,\ w=\sum_k\phi_k e_k$ | Complex coefficients of the unique expansion $W=\sum_k\phi_kF_k$, and the biquaternion they assemble |
| $A[G]$ | Line integral along the three axis-parallel legs from a base point, the inverse of $D$ on gradient fields |
| $Cl_{0,n}$ | Clifford algebra in which the generating-quartet results hold in place of $\mathbb{B}$ |
| $M_\alpha,M^\alpha$ | Multiplication operators from the left, $\alpha g$, and from the right, $g\alpha$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the complex sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the complex bilinear form, the scalar part of the complex bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |

## Further Reading

- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for Maxwell's equations in media, dispersion, and the standard boundary conditions.
- L. D. Landau and E. M. Lifshitz, *Electrodynamics of Continuous Media* (Pergamon, 1984), for the constitutive relations, the Brillouin energy density in dispersive media, and the boundary conditions at an interface.
- M. Born and E. Wolf, *Principles of Optics* (Cambridge, 1999), for dispersion, phase and group velocity, and the Fresnel coefficients.
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the invariant classification of the electromagnetic field.
- Ludwik Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung", *Annalen der Physik* 22 (1907) 579–586, for the original complex-vector formulation.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* 46 (2013) 053001, for the modern account of the complex vector.
- A. Waser, "Application of Bi-Quaternions in Physics" (2000, updated 2007), for the biquaternionic treatment of the field and its energy–momentum.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions" (2016), for the biquaternionic formulation of the field equations in a medium.
- S. M. Grudsky, K. V. Khmelnytskaya and V. V. Kravchenko, "On a quaternionic Maxwell equation for the time-dependent electromagnetic field in a chiral medium", *Journal of Physics A: Mathematical and General* **37** (2004) 4641–4647, DOI 10.1088/0305-4470/37/16/013 (preprint arXiv:math-ph/0309062), for the Drude–Born–Fedorov chiral constitutive relations, the reduction of the time-dependent chiral Maxwell system to the single quaternionic equation $M\mathbf{V}=\tilde R$, the exact factorization of $M(\omega)$ with its degenerate frequency $c/\beta$, the two refractive indices, the kernel $K_\alpha$ of $D_\alpha=D+\alpha$ with its defining equation $D_\alpha K_\alpha=\delta$ (note the source's $\Theta_\alpha=-e^{i\alpha|\mathbf{x}|}/(4\pi|\mathbf{x}|)$), and the causal fundamental solution, whose residue series resums to Bessel functions $J_0$ and $J_1$ of $2\sqrt{c(\mathbf{x})t}$. This is the paper recorded in the section *A Chiral Medium: One Quaternionic Equation*.
- V. V. Kravchenko and H. Oviedo, "On a Quaternionic Reformulation of Maxwell's Equations for Chiral Media and its Applications", *Zeitschrift für Analysis und ihre Anwendungen (Journal for Analysis and its Applications)* **22** (2003), no. 3, 569–589, DOI 10.4171/ZAA/1163, for the time-harmonic reformulation, the diagonalization with the two wavenumbers $\alpha_1,\alpha_2$, the integral representations, the extendability problem and its complete solution, and the treatment of inhomogeneous (slowly varying, stratified) chiral media. This is the source of the dedicated article *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation*, where the reformulation and its applications are recorded.
- V. V. Kravchenko, "Quaternionic Reformulation of Maxwell Equations for Inhomogeneous Media and New Solutions", *Zeitschrift für Analysis und ihre Anwendungen (Journal for Analysis and its Applications)* (2001), DOI 10.4171/ZAA/1063 (preprint arXiv:math-ph/0104008), for the time-harmonic reformulation of the Maxwell system of an arbitrary inhomogeneous medium, the operator $D+M_{\vec{\alpha}}$ with the gradient coefficient $\vec{\alpha}=\mathrm{grad}\,\phi/\phi$, the reduction to the Schrödinger equation $-\Delta\psi+(\Delta\phi/\phi)\psi=0$, the factorisation with the quaternionic Riccati condition $D\vec{\alpha}+\vec{\alpha}^2=-v$, and the closed-form fundamental solution. This is the source of the section *The Operator $D+M_{\vec{\alpha}}$, the Reduction to the Schrödinger Equation, and a Fundamental Solution*. Its factorisation is the Schrödinger member ($p=1$) of the general family: the paper carries neither the general $(\mathrm{div}\,p\,\mathrm{grad}+q)$ factorisation, nor the conductivity equation, nor the inverse theorems, and those are cited below to the survey's reference $[29]$. The paper's own attribution of the Riccati form is to Bernstein (1996) and Bernstein–Gürlebeck (1999), and it names no conductivity problem.
- V. V. Kravchenko, "Quaternionic equation for electromagnetic fields in inhomogeneous media" (2002), DOI 10.1142/9789812794253_0042 (preprint arXiv:math-ph/0202010), for the carrier identity $(D\pm\mathrm{grad}\,\phi/\phi)g^{(\mp)}=\phi^{(\mp1)}D(\phi^{(\pm1)}g)$, the scalar-product identity, the exact reduction of the Maxwell system of an arbitrary inhomogeneous medium to the two gradient-corrected equations and then to a single Vekua-type quaternionic equation, and the identification of that equation with the governing equation of the pseudoanalytic functions. This is the source of the section *Arbitrary Inhomogeneous Media: The Carrier Function and the Vekua Equation*.
- V. V. Kravchenko, "On a general solution of the one-dimensional stationary Schrödinger equation", arXiv:0708.2491v2 [math-ph] (2007), for the general solution of $(pu')'+qu=\omega^2u$ generated by one particular solution $g_0$ of the auxiliary equation $(pg_0')'+qg_0=0$ that is bounded together with $1/g_0$: the two interleaved recursions for the coefficients $\tilde X^{(n)},X^{(n)}$, the normalisation $g=\sqrt{pg_0}$, the unit Wronskian at the origin, the equivalent statement for $p=1$, and the numerical comparison with Matlab's `ode45`. This is the source of the paragraphs *The one-dimensional general solution*, *The carrier of the series is the carrier of the factorisation* and *Why $\omega$ is the right variable*. The paper attributes its Theorem 1 to the companion paper it cites as its reference $[3]$, where the reduction of $(pu')'+qu=\omega^2u$ to the auxiliary equation is proved by pseudoanalytic-function methods; the series solution itself is older, going back to Weyl's 1910 paper and to the representation used in inverse spectral theory.
- V. V. Kravchenko, "On a factorization of second order elliptic operators and applications", *Journal of Physics A: Mathematical and General* **39** (2006) 12407–12425, the primary source of the survey's operator-relation theorems, where it is its reference $[29]$: the general factorisation $(\mathrm{div}\,p\,\mathrm{grad}+q)\phi=-p^{1/2}(D+M^{\vec{\alpha}_f})(D-M_{\vec{\alpha}_f})p^{1/2}\phi$ with $f=p^{1/2}u_0$, its three consequences for the Schrödinger, conductivity and curl equations, the generating quartet $F_0=f$, $F_k=e_k/f$ of the Vekua-type equation with the condition $\sum_k(D\phi_k)F_k=0$ on the coefficients and the equivalent equation $Dw=(1-f^2)/(1+f^2)\,D\bar w$ for their combination, the inverse reconstruction $g=fA[f^{-1}F]$ through the line integral $A[G]$, and the extension of the whole section to the Clifford algebra $Cl_{0,n}$. This is the source of the operator-relation web recorded in *The Operator $D+M_{\vec{\alpha}}$, the Reduction to the Schrödinger Equation, and a Fundamental Solution* and of the section *The Generating Quartet, the Pseudoanalytic Equation, and the Inverse of the Reduction*; the survey's numbering, from which the material above was taken, is its Theorems 15–18 and its Remarks 19–20.
- L. Bers, *Theory of Pseudo-Analytic Functions* (New York University, 1952), the classical source of the $(F,G)$-pseudoanalytic functions and of the Vekua-type system with variable coefficients that the section *Arbitrary Inhomogeneous Media* identifies as the governing equation of Maxwell's system in an arbitrary medium, and the theory in which the one-dimensional series solution above is derived. The corpus carries the first layer of that theory — the generating quartet, the condition on the coefficients and the inverse of the reduction, in the section *The Generating Quartet, the Pseudoanalytic Equation, and the Inverse of the Reduction* — while the theory's own apparatus, its integral representations, its similarity principle and its Liouville-type theorems, is what the corpus does not yet develop; this is its primary reference.
- K. V. Khmelnytskaya and V. V. Kravchenko, "Biquaternions for analytic and numerical solution of equations of electrodynamics", arXiv:0902.3490v1 [math-ph] (2009), for the survey of the programme that this article and *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation* draw on: constant and variable coefficients, integral representations of solutions, the relations between the Maxwell, Schrödinger and conductivity operators, and a collocation numerical method built on the fundamental solutions. The survey is the "start here" pointer to the applied Kravchenko series; it is recorded here as the overview, it is the source through which the operator-relation theorems of $[29]$ and the generating-quartet material of *The Generating Quartet, the Pseudoanalytic Equation, and the Inverse of the Reduction* enter this article, and it is cited for the numerical method in the chiral article — the theorems themselves being cited to their primary papers.
- C. Doran and A. Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of the field strength and its Lorentz transformations.
