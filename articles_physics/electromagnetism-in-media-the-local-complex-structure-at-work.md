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
\bar{\tilde{\nabla}}=e_0\,\partial_{ict}-e_1\,\partial_x-e_2\,\partial_y-e_3\,\partial_z,
$$
and the d'Alembertian is $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}$. Throughout, $c$ denotes the speed of light **in the medium** and $c_0$ the vacuum speed; the divergence and curl are written $\mathrm{div}$ and $\mathrm{rot}$.

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
\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\bar{\tilde{\nabla}}\tilde{\nabla}
=\partial_{ict}^2+\Delta
=\Delta-\frac{1}{c^2}\,\partial_t^2,
$$
the d'Alembertian of a medium with speed $c$. This is the same operator identity as in the vacuum, with $c$ in place of $c_0$.

The medium enters this operator in exactly one way: through $c$ in $\partial_{ict}$. The algebra — the quaternion units, the scalar imaginary $i$, the decomposition $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ — is fixed and medium-independent. What the medium changes is the **embedding of physical spacetime into the algebra**. The material time coordinate is $ict=i\,c\,t$, so the map from physical time to the imaginary scalar direction of $\mathbb{B}$ carries the local factor $c(\mathbf{x})$.

Because $c>0$ is real, the medium rescales the imaginary axis but does not rotate it. The phase of the complex structure is the fixed $i$; its scale is the local $c$. This is the precise sense in which the complex structure is local. In the language of the introduction to the framework, $c$ plays the role of the local scale factor of the complex structure, and the constant vacuum value $c_0$ is the special case in which that scale does not vary. The classical $ict$ convention of Minkowski space is the vacuum limit of the local structure.

Two comments are worth making. First, the factorization $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}$ holds for any real positive $c$, so the algebraic fact on which the biquaternionic Maxwell equation rests is insensitive to the medium. Second, passing from vacuum to medium does not change the algebra $\mathbb{B}$; a medium is not a deformation of the complex structure but a different local scale for its imaginary direction.

## The Field Strength and Its Two Halves

The parent article defines the field-strength biquaternion as the pure vector
$$
\tilde{F}=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}
=\sum_{k=1}^{3}F_k\,e_k,
\qquad
F_k=i\sqrt{\epsilon}\,E_k-\sqrt{\mu}\,H_k,
$$
with $\mathrm{Sc}(\tilde{F})=0$. We use that definition without change. Two features of it are specific to the medium.

**The normalisation.** The factors $\sqrt{\epsilon}$ and $\sqrt{\mu}$ are natural because $\epsilon\,\mathbf{E}^2$ and $\mu\,\mathbf{H}^2$ are both energy densities. Hence $\sqrt{\epsilon}\,\mathbf{E}$ and $\sqrt{\mu}\,\mathbf{H}$ have the common dimension of the square root of an energy density, the two halves of $\tilde{F}$ are dimensionally homogeneous, and the norm form $N(\tilde{F})$ has the dimension of an energy density. The normalisation is equivalent to the two medium parameters introduced above: since $\sqrt{\epsilon\mu}=1/c$ and $\sqrt{\mu/\epsilon}=Z$, the data $(\sqrt{\epsilon},\sqrt{\mu})$ and $(c,Z)$ determine each other. The medium therefore enters $\tilde{F}$ through the same two numbers that govern propagation.

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
\tfrac{1}{2}\left(\tilde{F}+\tilde{F}^\dagger\right)=i\sqrt{\epsilon}\,\mathbf{E},
\qquad
\tfrac{1}{2}\left(\tilde{F}-\tilde{F}^\dagger\right)=-\sqrt{\mu}\,\mathbf{H},
$$
so the projection of $\tilde{F}$ onto the informational sector $\mathbb{M}_+$ measures the electric field, and its projection onto the material sector $\mathbb{M}_-$ measures the magnetic field.

The split into the two sectors is structural and does not depend on the medium: $i\sqrt{\epsilon}\,\mathbf{E}$ lies in $\mathbb{M}_+$ and $-\sqrt{\mu}\,\mathbf{H}$ lies in $\mathbb{M}_-$ for every real $\epsilon,\mu>0$. What the medium fixes is the **relative weight** of the two halves, through the ratio $\sqrt{\mu}/\sqrt{\epsilon}=Z$. This is one concrete sense in which the local complex structure is at work: the field strength is not a vector of a single sector but the sum of a Hermitian and an anti-Hermitian piece, and the medium sets their balance.

The energy is carried by the Hermitian form. In the parent article,
$$
\tilde{F}\tilde{F}^\dagger=2W\,e_0+\frac{2i}{c}\,\mathbf{S},
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

Two companion statements from the Maxwell article carry over unchanged. The first is the integrability condition $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{R})=0$, which is the biquaternionic form of charge conservation. The second is the potential formulation: in the Lorenz gauge the potential biquaternion $\tilde{A}=i\phi/c+\mathbf{A}$ satisfies
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

## Summary

Electromagnetism in a material medium is developed here as the general case, with the vacuum as its limit. The constitutive relations $\mathbf{D}=\epsilon\mathbf{E}$ and $\mathbf{B}=\mu\mathbf{H}$ supply the two parameters of a homogeneous medium, which may be taken as the speed $c=1/\sqrt{\epsilon\mu}$ and the impedance $Z=\sqrt{\mu/\epsilon}$, or equivalently as $\epsilon=1/(cZ)$ and $\mu=Z/c$.

The medium enters the biquaternionic structure in two places and nowhere else. First, through $c$ in the gradient, $\partial_{ict}=-(i/c)\partial_t$, so that the map from physical time to the imaginary scalar direction of $\mathbb{B}$ carries the local scale $c$; this is the sense in which the complex structure is local, the algebra being fixed while its embedding in physical spacetime is not. Second, through the normalisations $\sqrt{\epsilon},\sqrt{\mu}$ of the field strength and the corresponding $1/\sqrt{\epsilon},\sqrt{\mu}$ of the source biquaternion
$$
\tilde{F}=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H},
$$
which is fixed by the parent article and splits $\tilde{F}$ into a Hermitian electric half in $\mathbb{M}_+$ and an anti-Hermitian magnetic half in $\mathbb{M}_-$; the medium sets the relative weight $Z=\sqrt{\mu/\epsilon}$ of the two halves.

The single biquaternionic Maxwell equation $\tilde{\nabla}\tilde{F}=-\tilde{R}$ is medium-independent in form, the factors $\sqrt{\epsilon}$ and $\sqrt{\mu}$ cancelling through $\sqrt{\epsilon}/(c\sqrt{\mu})=\epsilon$ and $\sqrt{\mu}/(c\sqrt{\epsilon})=\mu$. Dispersion makes the local complex structure spectral: each frequency carries its own speed $c(\omega)=1/\sqrt{\epsilon(\omega)\mu(\omega)}$, refractive index $n(\omega)=c_0/c(\omega)$, dispersion relation $k^2=\omega^2\epsilon(\omega)\mu(\omega)$, and group velocity $v_g=c_0/(n+\omega\,dn/d\omega)$, at least while the normalisation is real. At an interface the local complex structure jumps, and the field strength is discontinuous even though the physical fields satisfy the standard tangential and normal continuity conditions. The vacuum limit $c\to c_0$, $Z\to Z_0$ recovers every object of the parent article, and the zero-divisor cone of the algebra coincides with the wave cone of the medium at every value of $c$.

For a plane wave in the medium, the conventions fixed above are: complex amplitudes in the $e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)}$ convention, transversality $\mathbf{k}\cdot\mathbf{E}_0=\mathbf{k}\cdot\mathbf{H}_0=0$, the relations $\mathbf{k}\times\mathbf{E}_0=\omega\mu\mathbf{H}_0$ and $\mathbf{k}\times\mathbf{H}_0=-\omega\epsilon\mathbf{E}_0$, the dispersion relation $k=\omega/c(\omega)=n(\omega)\omega/c_0$, and the impedance relation $\mathbf{H}_0=Z^{-1}\hat{\mathbf{k}}\times\mathbf{E}_0$. In these conventions $|\mathbf{E}_0|=Z|\mathbf{H}_0|=c|\mathbf{B}_0|$, the two normalised halves of $\tilde{F}_0$ have equal magnitude, and $N(\tilde{F}_0)=0$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{C}_{\mathbb{B}},\mathbb{H}_{\mathbb{B}}$ | Scalar subspace, real-quaternion subspace |
| $\mathbb{M}_+,\mathbb{M}_-$ | Hermitian and anti-Hermitian subspaces |
| $\tilde{\nabla},\bar{\tilde{\nabla}}$ | Biquaternionic gradient and its quaternion conjugate |
| $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\Delta-c^{-2}\partial_t^2$ | d'Alembertian in the medium |
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
| $N(\tilde{F})=\tilde{F}\bar{\tilde{F}}$ | Norm form (complex scalar) |
| $W=\tfrac{1}{2}(\epsilon\mathbf{E}^2+\mu\mathbf{H}^2)$ | Electromagnetic energy density |
| $\mathbf{S}=\mathbf{E}\times\mathbf{H}$ | Poynting vector |
| $\mathbf{k},\omega$ | Wavevector and angular frequency |
| $\hat{\mathbf{k}}=\mathbf{k}/|\mathbf{k}|$ | Unit wavevector |

## Further Reading

- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for Maxwell's equations in media, dispersion, and the standard boundary conditions.
- L. D. Landau and E. M. Lifshitz, *Electrodynamics of Continuous Media* (Pergamon, 1984), for the constitutive relations, the Brillouin energy density in dispersive media, and the boundary conditions at an interface.
- M. Born and E. Wolf, *Principles of Optics* (Cambridge, 1999), for dispersion, phase and group velocity, and the Fresnel coefficients.
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the invariant classification of the electromagnetic field.
- Ludwik Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung", *Annalen der Physik* 22 (1907) 579–586, for the original complex-vector formulation.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* 46 (2013) 053001, for the modern account of the complex vector.
- A. Waser, "Application of Bi-Quaternions in Physics" (2000, updated 2007), for the biquaternionic treatment of the field and its energy–momentum.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions" (2016), for the biquaternionic formulation of the field equations in a medium.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of the field strength and its Lorentz transformations.
