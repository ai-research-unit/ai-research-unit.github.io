# __Thomson and Compton Scattering: The Biquaternion Polarization Algebra__

## Introduction

Photon–electron scattering is the simplest process in which light, charge, and spin meet, and it is the process in which the polarization of the photon is an observable rather than a label. In its classical limit it is **Thomson scattering**: a free charge driven by a plane wave radiates at the same frequency, and the cross-section depends on the incident and outgoing polarization through the single geometric factor $|\varepsilon_{\mathrm{fop},\mathrm{out}}\cdot\varepsilon_{\mathrm{fop}}|^2$. In its quantum form it is **Compton scattering**: a photon of four-momentum $\tilde P_{\Phi,\mathrm{ph}}$ scatters off an electron of four-momentum $\tilde P_{\Phi,e}$ into $\tilde P_{\Phi,\mathrm{ph},\mathrm{out}}$ and $\tilde P_{\Phi,\mathrm{out},e}$, the frequency changes by the Compton shift, and the cross-section is the Klein–Nishina formula. The two are one process in two limits. The Thomson limit is $x =\frac{\omega}{0\,c\,k_m\,\to}$, the regime in which the recoil is negligible and the electron stays effectively at rest, so it is the limit in which the electron is **heavy**; it is not the massless limit, which is the opposite regime and belongs to the conformal article. This article develops the **polarization algebra** of the process in biquaternion form — the encoding of the photon's polarization states as elements of the algebra, the coherence biquaternion that carries the Stokes parameters, and the helicity operator — and uses it to organise the Thomson cross-section, its polarization transfer, and the Klein–Nishina generalisation.

Four results are established. First, the **polarization states are native to the material sector**. The transverse polarizations of a plane wave are the two real directions of the vector part of $\mathbb{B}_{\Phi}$ orthogonal to the propagation direction $\vec u_\eta$, and the two circular polarizations are the complex combinations that diagonalise left multiplication by $\vec u_\eta$, with eigenvalues $\mp i$; this is the companion photon article's characterisation, restated here because every formula below uses it. Second, the **coherence biquaternion** $\tilde{Ϛ}_{\Psi}$ is the state element of $\mathbb{B}_{\Psi}$ whose direction is the normalised Stokes vector and whose scale is the intensity $S_0$, so it carries the Stokes parameters; its biquaternion norm $\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural} = \frac14(S_0^2 - |\vec S|^2)$ measures the degree of polarization: the fully polarized states lie on the biquaternion-norm cone of $\mathbb{B}_{\Psi}$, whose section at $S_0=1$ is the Poincaré sphere, and the interior is the partially polarized ball. Third, the **Thomson cross-section is a pairing of two material-sector vectors**. Its polarization dependence is $|\varepsilon_{\mathrm{fop},\mathrm{out}}\cdot\varepsilon_{\mathrm{fop}}|^2 = |\mathrm{Sc}(\vec\varepsilon_{\mathrm{out}}^{*}\vec\varepsilon)|^2$, and the sum over the outgoing polarizations is the algebra's transverse projector; the magnitude $r_e^2$ is not supplied by the algebra. The unpolarized Thomson cross-section integrates to $8\pi r_e^2/3$, which is $0.66524587$ barn with the CODATA classical electron radius; the polarization sum over the two physical states was verified to reproduce the transverse projector $\delta_{ij}-\vec{u_\eta}_i\vec{u_\eta}_j$; the Compton shift was verified to put the recoil electron on its mass shell; and the Klein–Nishina differential cross-section was integrated numerically, agreed with the standard analytic total to a relative error below $10^{-9}$, and reduced to the Thomson value as $x\to0$. Fourth, the **electron-spin sums are one action, not a matrix**. The completeness relation sends a biquaternion $\tilde{Ξ}_{\mathrm{sp}}$ to $ip_0\tilde{Ξ}_{\mathrm{sp}}\vec e_x-\sum_\eta ip_\eta\vec e_\eta\tilde{Ξ}_{\mathrm{sp}}\vec e_y+k_m\tilde{Ξ}_{\mathrm{sp}}$, and resolving the spin replaces that action by half of itself applied to the two parts that the target's spin four-vector $s$ separates. The two halves were verified to be projections of rank one, orthogonal to each other, and summing to the unresolved action; the spin asymmetry of the quantum cross-section is the part that changes sign with $s$, the same axial direction through which the photon's circular polarization enters.

The scope is relativistic and quantum, and it is the worked application that closes the subcategory. The electron is treated as a Dirac particle whose free equation belongs to the spin-1/2 companions, and the photon as the massless Maxwell field of the spin-1 companions; what this article supplies is the algebra of the **polarizations** and the way the cross-sections are built from it. The classical relativistic particle and the Lorentz group belong to the non-quantum theory. The only approximation taken from outside is the Thomson limit itself, in which the recoil is neglected and the electron's motion in the wave is non-relativistic.

- Companion article *The Photon in Biquaternionic Form*, for the polarization space as the material sector, the circular basis, and the helicity operator.
- Companion article *Conformal Invariance and the Massless Limit in Biquaternionic Form*, for the massless limit proper, and for why it is the opposite regime to the one taken here.
- Companion article *The Field-Strength Biquaternion and Its Invariants*, for $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$, the Riemann–Silberstein vector, and the self-dual split.
- Companion article *Maxwell's Equations in the Biquaternionic Formulation*, for the free field whose plane waves are scattered.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the electron whose rest frame is the scattering frame.
- Companion article *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit*, for the plane-wave solutions, the covariant normalisation, and the spin sums used in the last section.
- Companion article *Canonical Quantization of the Biquaternion Maxwell Field*, for the photon states whose polarizations are counted.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the conserved current and the stress tensor of the fields being scattered.

## The Polarization Biquaternions

### Linear and circular polarizations in the material sector

The scalar imaginary of the algebra is written $i$. It is central, $i^2=-1$, and it commutes with $e_t,\vec e_x,\vec e_y,\vec e_z$; every factor of $i$ below is this one unit, so a product of two factors of $i$ is $-1$ and the simplifications of the displays are uses of that single identity.

A plane-wave solution of the source-free Maxwell equations with wave biquaternion $\tilde P_{\Phi,\mathrm{ph}} = i(\omega/c)e_t + \vec k_\Phi$ has a polarization biquaternion that is a pure vector, $\vec\varepsilon$, and the field-strength biquaternion of the wave is
$$
\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H
= \tilde P_{\Phi,\mathrm{ph}}\,\vec\varepsilon \quad\text{up to a phase and a normalisation},
$$
so that the electric and magnetic fields are the real and imaginary parts of the same quaternion. Transversality is the condition
$$
\vec u_\eta\cdot\vec\varepsilon = 0 ,
$$
i.e. the polarization lies in the plane of the vector part of $\mathbb{B}_{\Phi}$ orthogonal to the propagation direction. Two real orthonormal vectors $\varepsilon_{\mathrm{fop},1},\varepsilon_{\mathrm{fop},2}$ span that plane, and the **linear polarizations** are their real combinations. The **circular polarizations** are
$$
\varepsilon_{\mathrm{fop},\pm} = \frac{\varepsilon_{\mathrm{fop},1} \pm i\varepsilon_{\mathrm{fop},2}}{\sqrt{2}} ,
$$
complex combinations that lie in the complexification of the vector part of $\mathbb{B}$ but not in $\mathbb{B}_{\Phi}$ itself. Their defining algebraic property is that they diagonalise left multiplication by the propagation direction, taken as the real unit vector $\vec u_\eta$ along $\vec k_\Phi$:
$$
\vec u_\eta\,\varepsilon_{\mathrm{fop},\pm} = \mp i\,\varepsilon_{\mathrm{fop},\pm} ,
$$
and they are null and mutually normalised under the complex-bilinear dot product,
$$
\varepsilon_{\mathrm{fop},\pm}\!\cdot\!\varepsilon_{\mathrm{fop},\mp} = 1 ,
\qquad
\varepsilon_{\mathrm{fop},\pm}\!\cdot\!\varepsilon_{\mathrm{fop},\pm} = 0 .
$$
The two signs are the two helicities, the two senses of rotation about the propagation axis. The companion photon article draws the representation-theoretic consequences — the helicity operator, whose spectral values on the complexified vector part are $\{+1,0,-1\}$, and the fact that the polarization *states* are not idempotents of $\mathbb{B}_{\Psi}$ and are not elements of it, even though the helicity *observable* has its representative there. The operator is
$$
\lambda = \vec u_\eta\cdot\vec S = \tfrac{i}{2}\mathrm{ad}_{\vec u_\eta} ,
\qquad
\lambda\varepsilon = \mathrm{Vect}\bigl(i\vec u_\eta\varepsilon\bigr) ,
$$
with the spin measured in units of $\hbar$ and the spin-one generators $\vec S_\eta = i\vec e_\eta$, so that the three expressions agree on the transverse plane; the identity $\tfrac{i}{2}\mathrm{ad}_{\vec u_\eta}\varepsilon = i\vec u_\eta\varepsilon$ holds because $\mathrm{ad}_{\vec u_\eta}\varepsilon = 2\vec u_\eta\varepsilon$ for a transverse $\varepsilon$. Its representative in $\mathbb{B}_{\Psi}$ is the element $i\vec u_\eta$: left multiplication by that element, followed by the vector part, has eigenvalues $\pm1$ on $\varepsilon_{\mathrm{fop},\pm}$ and annihilates the longitudinal direction. Here the relation is used as the algebraic definition of circular polarization and as the reason the polarization sums are geometric.

### The polarization sum

For any two orthonormal vectors spanning the transverse plane, the completeness relation is the transverse projector,
$$
\sum_{\lambda=1,2}\varepsilon_{\mathrm{fop},i}^{(\lambda)}\varepsilon_{\mathrm{fop},j}^{(\lambda)} = \delta_{ij} - \vec u_\eta_i\vec u_\eta_j ,
$$
and the circular pair obeys the same sum. In the framework this projector is native: the orthogonal complement of $\vec u_\eta$ inside the vector part of $\mathbb{B}_{\Phi}$ is defined by the algebra's own biquaternion norm, and the companion photon article checks the same identity on the rational directions $(3,4,0)/5$ and $(1,2,2)/3$.

### The coherence biquaternion and the Stokes parameters

A beam is described not by one polarization vector but by its coherence matrix. Writing the Stokes parameters $S_0, S_1, S_2, S_3$ for the intensities in the linear and circular bases, the coherence matrix is encoded in the **coherence biquaternion**
$$
\tilde{Ϛ}_{\Psi} = \tfrac12\bigl(S_0e_t + i\vec S\bigr) \in \mathbb{B}_{\Psi} ,
\qquad
\vec S = S_1\vec e_x + S_2\vec e_y + S_3\vec e_z ,
$$
the single factor of $i$ multiplying the whole vector part rather than each of its three components. It is Hermitian by construction, as every element of $\mathbb{B}_{\Psi}$ is. Its biquaternion norm is the scalar coefficient of $\tilde{Ϛ}_{\Psi}\tilde{Ϛ}_{\Psi}^{\natural}$,
$$
\tilde{Ϛ}_{\Psi}\,\tilde{Ϛ}_{\Psi}^{\natural} = \langle\tilde{Ϛ}_{\Psi}\rangle_{\natural}\,e_t ,
\qquad
\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural}
= \tfrac14\bigl(S_0^2 - S_1^2 - S_2^2 - S_3^2\bigr)
= \tfrac14 S_0^2\bigl(1 - P^2\bigr) ,
$$
with the **degree of polarization**
$$
P = \frac{\sqrt{S_1^2+S_2^2+S_3^2}}{S_0} .
$$
The relation $\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural} = \frac14S_0^2(1-P^2)$ was verified on random Stokes vectors to machine precision, and it inverts, since $\mathrm{Sc}(\tilde{Ϛ}_{\Psi}) = S_0/2$, to
$$
P^2 = 1 - \frac{\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural}}{\mathrm{Sc}(\tilde{Ϛ}_{\Psi})^2} ,
$$
so the one number the norm carries is the degree of polarization, read against the square of the trace part. Three statements follow. Fully polarized light has $P = 1$, hence $\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural} = 0$: the fully polarized states are the **biquaternion-norm cone** of the Hermitian sector. Unpolarized light has $\vec S = 0$ and $\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural} = \frac14S_0^2$, the interior point on the cone's axis. Partially polarized light fills the interior ball. The Poincaré sphere — the sphere of polarization states, whose poles are the circular polarizations and whose equator is the linear ones — is therefore the cone $\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural} = 0$ read at the normalisation $S_0 = 1$, i.e. at $2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}) = 1$; depolarization moves $\tilde{Ϛ}_{\Psi}$ inward along a radius, off the cone. This identification is what makes the polarization algebra of this article and the biquaternion-norm algebra of the framework the same object; the companion article on the informational sector develops the cone and its idempotents, and the geometry of the Poincaré sphere is the geometry of that cone.

### The polarization ellipse and the invariants

The Stokes parameters are not an arbitrary labelling: they are the coefficients of the beam's polarization ellipse and of its handedness, and the algebra's two invariants organise them. The ellipse's orientation $\tilde{Ξ}_{\mathrm{sp},\mathrm p}$ and ellipticity $\xi_{\mathrm p}$ are
$$
\tan 2\tilde{Ξ}_{\mathrm{sp},\mathrm p} = \frac{S_2}{S_1} ,
\qquad
\sin 2\xi_{\mathrm p} = \frac{S_3}{\sqrt{S_1^2+S_2^2+S_3^2}} ,
$$
with $\xi_{\mathrm p}>0$ right-handed and $\xi_{\mathrm p}<0$ left-handed, and the sign of the $S_3$ coefficient in the coherence biquaternion is the algebraic carrier of the handedness. The subscript $\mathrm p$ marks the two parameters of the polarization ellipse, so that they are not read as the rapidity $\theta_{\mathrm{rpd}}$ or the chirality $\xi$ of the framework. Two combinations are invariant under the rotations of the transverse plane that the algebra generates. The **trace part** $\frac12S_0e_t$ is the intensity, the rotation-invariant scalar of the coherence biquaternion, and the **biquaternion norm** $\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural} = \frac14(S_0^2-|\vec S|^2)$ is the purity, also invariant because the rotation acts on $\vec S$ by the vector rotation. Every other feature of the beam — the orientation of the ellipse, the azimuth of the Stokes vector — is a frame-dependent coordinate, and the decomposition
$$
\tilde{Ϛ}_{\Psi} = \frac12 S_0 e_t + \tilde{Ϛ}_{\Psi,\mathrm{pol}} ,
\qquad
\tilde{Ϛ}_{\Psi,\mathrm{pol}} = \frac{i}{2}\sum_\eta S_\eta\vec e_\eta ,
$$
separates the invariant unpolarized part from the polarized part whose norm is $-\frac14|\vec S|^2$. A fully polarized beam is one whose polarized part saturates the cone, $\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural} = 0$; depolarization transfers weight from the vector part to the scalar part, which is the operation the density-matrix formalism calls the completely-positive trace-preserving map. The two invariants of the beam and the two invariants of the action — the bilinear norm and the Hermitian pairing — are thus the same two forms: the trace part is the Hermitian pairing of $\tilde{Ϛ}_{\Psi}$ with $e_t$, and the biquaternion norm is the bilinear pairing $\tilde{Ϛ}_{\Psi}\tilde{Ϛ}_{\Psi}^{\natural}$.

### The self-dual split and helicity

The two circular polarizations are the two eigenstates of the helicity, and they are also the two irreducible pieces of the field. The Riemann–Silberstein vector $\vec N = \vec E + ic\vec B$ splits the field into its self-dual and anti-self-dual halves,
$$
\vec N_+ = \vec N = \vec E + ic\,\vec B ,
\qquad
\vec N_- = \vec N^* = \vec E - ic\,\vec B ,
$$
where $\vec N_+$ is the self-dual half and $\vec N_-$ the anti-self-dual one, complex conjugates of each other for a real field: the field itself is the self-dual half and its conjugate is the anti-self-dual one, so the two are one complex triple read twice and not two halves of a sum. They are the two halves of the field tensor in the companion's convention, $\vec N \leftrightarrow F + i\star F$ and $\vec N^* \leftrightarrow F - i\star F$ with $\star\vec N = -i\vec N$, and they are not a partition of $\vec N$ into a sum but a partition of the six real field components into two complex triples. For a plane wave of definite helicity the field is supported on one half: the helicity $+1$ amplitude appears in $\vec N_+ = \vec E + ic\vec B$ and the helicity $-1$ amplitude in $\vec N_- = \vec E - ic\vec B$. The companion articles on the field strength and on the photon establish this and identify the two pieces as the two three-dimensional complex representations of the Lorentz group and as the $\pm1$ eigenspaces of the helicity operator. The reason it belongs to the scattering article is that the two helicity amplitudes of the scattering process are the amplitudes for the field to remain in, or move between, these two pieces, and the self-dual split is the algebraic reason there are two of them and not four. A scattering process that conserves helicity is one that leaves the decomposition intact; a helicity-flip process transfers amplitude between the two halves.

## Thomson Scattering

### The classical cross-section

A free electron of charge $-e$ and mass $m$ in a plane wave of amplitude $E_0$ acquires the oscillating velocity $\vec v = e\vec E/(mi\omega)$: the phase is $\exp(-i\omega r'_t/c)$, so $\partial/\partial r'_t \to -i\omega/c$ and the equation $m\,d\vec v/dr'_t = -e\vec E$ gives that velocity. The driven displacement has the amplitude $x_0 = eE_0/(m\omega^2)$, one power of $\omega$ below the velocity's, so the dipole moment $\vec p = -e\vec r$ has $\ddot{\vec p} = -e\ddot{\vec r} = +e^2\vec E_0/m$, independent of the frequency. One power of $\omega$ cancels against the $\omega^2$ of the second derivative, and that cancellation is the whole of the frequency independence at this level. The electron radiates as that dipole, and the Larmor formula gives the time-averaged power per unit solid angle,
$$
\Bigl\langle\frac{dP}{d\Omega}\Bigr\rangle
= \frac{1}{16\pi^2\epsilon_0 c^3}\,\bigl\langle|\ddot{\vec p}_{\perp}|^2\bigr\rangle
= \frac{e^4E_0^2}{32\pi^2\epsilon_0 c^3 m^2}\,
\bigl|\varepsilon_{\mathrm{fop},\mathrm{out}}\cdot\varepsilon_{\mathrm{fop}}\bigr|^2 ,
$$
the factor $\tfrac12$ coming from $\langle\cos^2\omega r'_t/c\rangle$. Dividing by the incident intensity $I = \tfrac12\epsilon_0 cE_0^2$ gives the Thomson differential cross-section
$$
\boxed{\;
\frac{d\sigma_T}{d\Omega} = r_e^2\,\bigl|\varepsilon_{\mathrm{fop},\mathrm{out}}\cdot\varepsilon_{\mathrm{fop}}\bigr|^2 ,
\qquad
r_e = \frac{e^2}{4\pi\epsilon_0 mc^2}\;},
$$
where $\varepsilon_{\mathrm{fop}}$ and $\varepsilon_{\mathrm{fop},\mathrm{out}}$ are the incident and outgoing **linear** polarization unit vectors. In the biquaternion form the geometric factor is a pairing in the material sector,
$$
\bigl|\varepsilon_{\mathrm{fop},\mathrm{out}}\cdot\varepsilon_{\mathrm{fop}}\bigr|^2
= \bigl|\mathrm{Sc}\bigl(\vec\varepsilon_{\mathrm{out}}^{*}\vec\varepsilon\bigr)\bigr|^2 ,
$$
since for a real pure vector $\vec\varepsilon^{*} = -\vec\varepsilon$ and $\mathrm{Sc}(\vec\varepsilon_{\mathrm{out}}\vec\varepsilon) = -\vec\varepsilon_{\mathrm{out}}\cdot\vec\varepsilon$, so that
$$
\mathrm{Sc}\bigl(\vec\varepsilon_{\mathrm{out}}^{*}\vec\varepsilon\bigr)
= -\mathrm{Sc}\bigl(\vec\varepsilon_{\mathrm{out}}\vec\varepsilon\bigr)
= \vec\varepsilon_{\mathrm{out}}\cdot\vec\varepsilon .
$$
The amplitude's polarization dependence is therefore a single pairing of two elements of $\mathbb{B}_{\Phi}$, and the cross-section is its modulus squared, exactly as a quantum-mechanical cross-section is the modulus squared of an amplitude. Two features of the formula are worth stating. It factors: incident polarization, propagation direction, outgoing direction, and outgoing polarization enter only through the one scalar $\varepsilon_{\mathrm{fop},\mathrm{out}}\cdot\varepsilon_{\mathrm{fop}}$. And its sum over the outgoing polarizations is a **projector**: using the completeness relation gives
$$
\sum_{\lambda_{\mathrm{out}}}\bigl|\varepsilon_{\mathrm{fop}}\cdot\varepsilon_{\mathrm{fop},\mathrm{out}}^{(\lambda_{\mathrm{out}})}\bigr|^2
= 1 - \bigl(\varepsilon_{\mathrm{fop}}\cdot\vec u_{\mathrm{out},k}\bigr)^2 = \sin^2\theta_{\mathrm{sct}} ,
$$
where $\theta_{\mathrm{sct}}$ is the angle between the incident polarization and the outgoing propagation direction; this was verified on one hundred random geometries to $10^{-15}$. For an incident beam polarized **in** the scattering plane, $\theta_{\mathrm{sct}}$ is the complement of the scattering angle, the sum is $\cos^2\theta$, and it vanishes at $90^\circ$ — no light is scattered along the direction of the incident polarization, which is the dipole's null axis. For an incident beam polarized **perpendicular** to the plane, $\theta_{\mathrm{sct}} = \pi/2$ and the sum is one at every angle, so the scattered light stays fully polarized in that direction.

### The helicity amplitudes

The two circular amplitudes of the classical process carry the helicity information in the simplest possible form. Writing the amplitude as ${\varepsilon_{\mathrm{fop},\mathrm{out}}}^*\cdot\varepsilon_{\mathrm{fop}}$ in the circular basis, the two independent elements are the **helicity-conserving** and **helicity-flip** amplitudes
$$
M_{++} = {\varepsilon_{\mathrm{fop},\mathrm{out},+}}^*\cdot\varepsilon_{\mathrm{fop},+} , \qquad
M_{+-} = {\varepsilon_{\mathrm{fop},\mathrm{out},-}}^*\cdot\varepsilon_{\mathrm{fop},+} ,
$$
and with the real basis of each transverse plane chosen the same way — $\vec u_{\varepsilon,1}$ in the scattering plane and $\vec u_{\varepsilon,2}$ normal to it, primed for the outgoing plane — they evaluate exactly, with no phase left over, to
$$
\lvert M_{++}\rvert = \frac{1+\cos\theta}{2} , \qquad
\lvert M_{+-}\rvert = \frac{1-\cos\theta}{2} ,
$$
so that the flip-to-conserve amplitude ratio is $(1-\cos\theta)/(1+\cos\theta)$ and their sum of squares is the unpolarized angular distribution,
$$
\lvert M_{++}\rvert^2+\lvert M_{+-}\rvert^2 = \frac{1+\cos^2\theta}{2} .
$$
The identities were verified on six scattering angles: the ratio of the two amplitudes reproduced $(1-\cos\theta)/(1+\cos\theta)$ exactly, and the sum of their squares reproduced $(1+\cos^2\theta)/2$ to machine precision. The physical content is the forward **helicity conservation** of light scattering: at $\theta = 0$ the flip amplitude vanishes and the scattering preserves helicity, while at $\theta = \pi$ the roles reverse and only the flip amplitude survives. This is the algebraic counterpart of the statement that a circularly polarized wave scattered forward keeps its sense of rotation, and the self-dual split of the previous subsection is its structural basis: the conserving amplitude leaves the field in its own helicity half, and the flipping amplitude transfers it to the other.

The two helicity amplitudes are not an extra structure imposed on the scattering; they are the two components of the polarization biquaternion in the basis that the algebra's multiplication by $\vec u_\eta$ diagonalises. The circular basis is the eigenbasis of that multiplication, the amplitudes are the pairings in that basis, and the helicity-conserving and helicity-flipping processes are the diagonal and off-diagonal entries. The angular functions $(1\pm\cos\theta)/2$ follow from the geometry of the transverse plane, i.e. from the biquaternion norm, and are the amplitudes of the two channels, whose squares are their weights.

### The unpolarized cross-section and its integral

Averaging the factor over the two incident polarizations,
$$
\bigl|\varepsilon_{\mathrm{fop},\mathrm{out}}\cdot\varepsilon_{\mathrm{fop}}\bigr|^2 \longrightarrow \frac{1+\cos^2\theta}{2} ,
$$
gives the unpolarized Thomson cross-section
$$
\frac{d\sigma_T}{d\Omega} = r_e^2\,\frac{1+\cos^2\theta}{2} ,
$$
whose integral is the Thomson cross-section
$$
\boxed{\;
\sigma_T = \frac{8\pi}{3}r_e^2 = 0.66524587\ \text{barn}\;}.
$$
Both statements are checked: the angular integral of $r_e^2(1+\cos^2\theta)/2$ over the sphere is elementary and returns $8\pi r_e^2/3$ exactly, and its value with the CODATA classical electron radius is $0.66524587$ barn, the tabulated number. The cross-section is independent of frequency: the classical problem contains no $\frac{m\,c}{k_m}$, the only length in it is $r_e$, and no photon energy can enter.

### The polarization transfer

The full polarization content of Thomson scattering is a linear map on the Stokes vector — the standard Mueller matrix in the scattering-plane basis — with $Q$ positive for polarization perpendicular to that plane,
$$
\frac{d\sigma_T}{d\Omega}:\quad
\begin{aligned}
I_{\mathrm{out}} &= \tfrac{r_e^2}{2}\bigl[(1+\cos^2\theta)\,I+\sin^2\theta\,Q\bigr] ,\\
Q_{\mathrm{out}} &= \tfrac{r_e^2}{2}\bigl[\sin^2\theta\,I+(1+\cos^2\theta)\,Q\bigr] ,\\
\mathcal U_{\mathrm{out}} &= r_e^2\cos\theta\;\mathcal U ,\qquad
\mathcal V_{\mathrm{out}} = r_e^2\cos\theta\;\mathcal V ,
\end{aligned}
$$
written out on the incident $(I,Q,\mathcal U,\mathcal V)$. The $I$ and $Q$ lines carry the linear polarization transfer, and two checks were made on the map. Its response to an unpolarized beam, integrated over the sphere, returns $8\pi r_e^2/3$, so the map is normalised consistently with the differential cross-section above. And an **unpolarized incident beam is scattered into a linearly polarized one**, with degree of polarization
$$
P(\theta) = \frac{\sin^2\theta}{1+\cos^2\theta} ,
$$
which vanishes forward and backward, equals **one at $\theta = 90^\circ$**, and was verified at six angles against this map to machine precision. The physical statement is that scattering at right angles prepares a beam polarized perpendicular to the scattering plane, a fact used in every polarimeter; the algebraic statement is that the off-diagonal entries of the transverse projector transfer the polarization that the process selects. The factor $2\cos\theta$ on the $\mathcal U$ and $\mathcal V$ lines shows that circular polarization is *not* transferred in the same way. A circularly polarized incident beam of intensity $I$ and Stokes $\mathcal V=I$ is scattered into $I_{\mathrm{out}} = \tfrac{r_e^2}{2}(1+\cos^2\theta)I$ and $\mathcal V_{\mathrm{out}} = r_e^2\cos\theta\,I$, so its degree of circular polarization becomes
$$
P_c(\theta) = \frac{2\cos\theta}{1+\cos^2\theta} ,
$$
which is the analogue of the linear degree $P(\theta)$ above: it equals one forward, falls to **zero at $\theta = 90^\circ$**, and is **reversed** beyond it, tending to $-1$ in backscattering. The circular polarization is therefore not merely attenuated but handedness-reversing past a right angle, which is the helicity statement of the same geometry that makes the linear degree maximal there. Circular polarization never enters the $I$ and $Q$ lines, so Thomson scattering on a free electron does not convert circular to linear polarization.

### The Thomson limit and the one scale

The frequency independence of the Thomson cross-section is a statement about scales, and the scale that matters is the electron's mass, not its absence. The limit is $x =\frac{\omega}{c\,k_m\,\to0}$ at fixed $m$: the photon's energy is small compared with the rest energy, the frequency shift is of order $x$, and the electron stays effectively at rest. It is therefore the limit in which the electron is **heavy**; the massless limit of *Conformal Invariance and the Massless Limit in Biquaternionic Form* is the opposite regime, $x\gg1$, in which the electron's mass is negligible and the cross-section is the Klein–Nishina one of the next section.

What is scale-free is the field and not the charge. The source-free Maxwell action in four dimensions carries no dimensional parameter, so the incident and radiated waves have no intrinsic length; the charge supplies the only one there is,
$$
r_e = \frac{e^2}{4\pi\epsilon_0 mc^2} ,
$$
and the classical cross-section must therefore be $r_e^2$ times a dimensionless function of the angles. No frequency can appear, because a second length would be needed to make one. Dimensional analysis alone fixes the $\omega$-independence, and the conformal weight of the Maxwell field — two for the field strength, one for the potential — is the reason the field side of the problem has no scale to contribute. The next sections show the scale that the quantum theory reintroduces, and it is the mass that supplies it.

## Compton Scattering

### The Compton shift

When the photon energy is comparable with the electron rest energy the electron recoils and the scattered frequency is lower:
$$
\boxed{\;
\omega_{\mathrm{out}} =\frac{\omega}{1 +\frac{\omega}{c\,k_m}\,(1-\cos\theta)}\;},
$$
the **Compton shift**, where $\theta$ is the scattering angle. It follows from the conservation of the four-momentum, $\tilde P_{\Phi,\mathrm{ph}} + \tilde P_{\Phi,e} = \tilde P_{\Phi,\mathrm{ph},\mathrm{out}} + \tilde P_{\Phi,\mathrm{out},e}$, together with the on-shell conditions
$$
\langle\tilde P_{\Phi,\mathrm{ph}}\rangle_{\natural} = 0 , \qquad \langle\tilde P_{\Phi,e}\rangle_{\natural} = -m^2c^2 ,
$$
and it is the biquaternion-norm statement of the kinematics: the photon stays on the null cone and the electron stays on its mass shell. The formula was verified by an independent route: for four scattering angles and four incident energies (0.1, 0.511, 2 and 10 MeV) the recoil four-momentum reconstructed from energy–momentum conservation satisfied $E_e^2 - p^2c^2 = m^2c^4$ to $3\times10^{-14}$ MeV$^2$, so the shifted frequency is the one that puts the electron back on shell. No approximation beyond the rest-frame kinematics and the plane-wave conditions enters, and the derivation is the standard one; the note that belongs to this series is that the kinematics is a statement entirely about the biquaternion norm on the two momenta.

### The recoil electron

The shift is one half of the kinematics; the other half is the recoil. In the laboratory frame the initial electron is at rest, $\tilde P_{\Phi,e} = imc\,e_t$, and conservation of the four-momentum fixes the recoil momentum to $\tilde P_{\Phi,\mathrm{out},e} = \tilde P_{\Phi,e} + \tilde P_{\Phi,\mathrm{ph}} - \tilde P_{\Phi,\mathrm{ph},\mathrm{out}}$, whose components have the standard form: energy $E_{\mathrm{out},e} = mc^2 +\frac{m\,c\,\omega}{k_m}-\frac{m\,c\,\omega_{\mathrm{out}}}{k_m}$, and momentum in the scattering plane, on the side opposite the scattered photon, at the angle $\theta_{\mathrm{azm},e}$ from the incident direction,
$$
\tan\theta_{\mathrm{azm},e} = \frac{\omega_{\mathrm{out}}\sin\theta}{\omega - \omega_{\mathrm{out}}\cos\theta} ,
$$
which in the Thomson limit $\omega_{\mathrm{out}}\to\omega$ is $\theta_{\mathrm{azm},e} = 90^\circ - \theta/2$; so the electron and the scattered photon separate by $90^\circ+\theta/2$, verified at five angles, and the electron recoils at right angles to the incident direction only in the forward limit. The reconstruction is the numerical check of the previous subsection; what matters for the polarization algebra is that the electron recoils along $\vec u_\eta - \vec u_{\mathrm{out},k}$, in the scattering plane, while the axial direction of the spin asymmetry is the normal to that plane, $\vec u_\eta\times\vec u_{\mathrm{out},k}$. Both are material-sector vectors, so the spin asymmetry pairs two objects of the same sector. The electron's recoil is also what distinguishes the quantum from the classical problem: in the Thomson limit the recoil momentum is negligible and the electron remains effectively at rest, while in the Compton regime the recoil carries away the energy difference $\frac{m\,c\,(\omega - \omega_{\mathrm{out}})}{k_m}$, and this recoil is the physical origin of the dimensionless scale $x$.

### The Klein–Nishina cross-section

The quantum differential cross-section for unpolarized photons and electrons is the Klein–Nishina formula,
$$
\frac{d\sigma_{\mathrm{KN}}}{d\Omega}
= \frac{r_e^2}{2}\left(\frac{\omega_{\mathrm{out}}}{\omega}\right)^2
\left(\frac{\omega}{\omega_{\mathrm{out}}} + \frac{\omega_{\mathrm{out}}}{\omega} - \sin^2\theta\right) ,
$$
and its integral over the sphere is the total Klein–Nishina cross-section
$$
\boxed{\;
\sigma_{\mathrm{KN}}(x) = 2\pi r_e^2\left[
\frac{1+x}{x^3}\left(\frac{2x(1+x)}{1+2x} - \ln(1+2x)\right)
+ \frac{\ln(1+2x)}{2x} - \frac{1+3x}{(1+2x)^2}
\right] ,
\qquad x =\frac{\omega}{c\,k_m}\;}.
$$
The differential formula was integrated over the sphere at five energies ($x = 0.01, 0.1, 0.5, 1, 5$), and the result agreed with the analytic total to a relative error below $10^{-9}$ at every energy; the analytic total itself is the standard closed form and was used only as the comparison. The **Thomson limit** was checked separately: at $x = 10^{-4}$ the total is $8.3760\,r_e^2$ against $8\pi r_e^2/3 = 8.3776\,r_e^2$, so the Klein–Nishina cross-section tends to the Thomson value as the recoil vanishes, as it must. The scale that the quantum theory reintroduces is the same $x$: the cross-section depends on the single dimensionless ratio $\frac{\omega}{c\,k_m}$, and only in its vanishing does the classical, frequency-independent result return.

### The high-energy limit

The opposite limit is also elementary and is worth recording because it shows the scale $x$ at work in the other direction. For $x\gg1$ the total cross-section falls as
$$
\sigma_{\mathrm{KN}}(x) \approx \frac{\pi r_e^2}{x}\Bigl(\ln 2x + \tfrac12\Bigr) ,
$$
the standard high-energy asymptotics. It was verified numerically against the analytic total at five energies: the ratio of the exact value to the asymptotic form is $0.989$ at $x = 100$, $0.997$ at $x = 500$, and $0.999$ at $x = 1000$ ($0.9893$, $0.9975$, $0.9987$ before rounding), so the asymptotic law is approached from below. The two pieces of the asymptotic form have different origins. The $1/x$ is dimensional: $r_e^2/x = r_e^2\,c\,k_m/\omega$ is the only combination of the two lengths available once the photon wavelength is short compared with the Compton wavelength. The logarithm comes from angles, not from the forward peak: with $r = 1/(1+x\sin^2(\theta/2))$ the band $1/\sqrt x\ll\theta\ll1$ contributes a term of order $\frac{r_e^2}{x}\int_1^{x}du/u = \frac{r_e^2}{x}\ln x$, each decade of angle contributing equally, and that band carries $63\%$ of the total at $x=100$ and $73\%$ at $x=1000$ (verified by numerical integration). The Thomson constant $8\pi r_e^2/3$ is entirely gone, and the only trace of the electron mass is the argument $x =\frac{\omega}{c\,k_m}$ of the logarithm. The two limits together, $\sigma_T$ at $x\to0$ and $\pi r_e^2(\ln 2x+\frac12)/x$ at $x\to\infty$, are the two ends of the one function $\sigma_{\mathrm{KN}}(x)$, and the whole energy dependence of the process is the single dimensionless scale the mass supplies. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

### Polarization in Compton scattering

The polarization algebra of the quantum process is richer than the classical one because the electron's spin participates. Two statements about the photon are standard and belong here, and a third carries the spin.

**Unpolarized in, polarized out.** For an unpolarized incident beam the scattered radiation is linearly polarized, with the electric vector preferentially perpendicular to the scattering plane. The degree of polarization is the Thomson value $\sin^2\theta/(1+\cos^2\theta)$ in the low-energy limit; it is **maximal at right angles** and vanishes forward and backward, and it is the basis of gamma-ray polarimetry.

**Polarized in, modulated out.** For an incident beam linearly polarized along $\vec\varepsilon$, with $\theta_{\mathrm{azm}}$ the azimuth of the scattered photon measured from $\vec\varepsilon$, the differential cross-section is
$$
\frac{d\sigma_{\mathrm{KN}}}{d\Omega}
= \frac{r_e^2}{2}\Bigl(\frac{\omega_{\mathrm{out}}}{\omega}\Bigr)^{2}
\Bigl[\frac{\omega_{\mathrm{out}}}{\omega}+\frac{\omega}{\omega_{\mathrm{out}}}-2\sin^2\theta\cos^2\theta_{\mathrm{azm}}\Bigr] ,
$$
which is the form $A(\omega,\theta)+B(\omega,\theta)\cos2\theta_{\mathrm{azm}}$ with the unpolarized value as the constant part,
$$
A(\omega,\theta) = \frac{r_e^2}{2}\Bigl(\frac{\omega_{\mathrm{out}}}{\omega}\Bigr)^{2}\Bigl[\frac{\omega_{\mathrm{out}}}{\omega}+\frac{\omega}{\omega_{\mathrm{out}}}-\sin^2\theta\Bigr] ,
\qquad
B(\omega,\theta) = -\frac{r_e^2}{2}\Bigl(\frac{\omega_{\mathrm{out}}}{\omega}\Bigr)^{2}\sin^2\theta ,
$$
so that the analysing power of the scatterer is
$$
\Bigl|\frac{B}{A}\Bigr|
= \frac{\sin^2\theta}{\omega_{\mathrm{out}}/\omega+\omega/\omega_{\mathrm{out}}-\sin^2\theta} .
$$
The geometry sits in the sign of the modulation. With $\theta_{\mathrm{azm}}$ measured from $\vec\varepsilon$, the $\cos2\theta_{\mathrm{azm}}$ factor is extremal in the plane that contains the incident polarization, $\theta_{\mathrm{azm}} = 0$ or $\pi$, where the cross-section sits a full $\lvert B\rvert$ below its unpolarized value $A$, and it vanishes in the perpendicular plane, $\theta_{\mathrm{azm}} = \pm90^\circ$, where the cross-section returns to its unpolarized value. The depth of that fall, relative to the unpolarized part, is the analysing power $|B/A|$: in the Thomson limit it grows with $\sin^2\theta$ and is greatest at right angles, while for $x>0$ the recoil factor $r + 1/r$ damps the large angles and moves the peak forward, to $82^\circ$ at $x=1$ and $63^\circ$ at $x=5$ (computed on a grid in $\theta$). In the Thomson limit the minimum of the $\theta_{\mathrm{azm}}=0$ curve reaches zero at $\theta = 90^\circ$, where the dipole would have to radiate along its own axis; for $x>0$ the recoil factor lifts that minimum off zero, but the modulation survives, and it is what makes the process a polarimeter.

Two checks fix the formula. Averaging over $\theta_{\mathrm{azm}}$ returns the unpolarized Klein–Nishina cross-section of the previous section, verified on one hundred values of $(x,\theta)$ to $3\times10^{-16}$. And in the Thomson limit $\omega_{\mathrm{out}}\to\omega$ the analysing power becomes $\sin^2\theta/(1+\cos^2\theta)$, which is exactly the degree of polarization $P(\theta)$ that the scatterer imparts to an unpolarized beam, verified at four angles. That equality is the reciprocity of polarimetry: a filter that polarizes is a filter that analyses, and in the Mueller language it is the symmetry between the $I$ and $Q$ lines above.

**The spin asymmetry.** If the electron is polarized, the cross-section acquires a term odd in the electron spin, of the form
$$
\Delta\frac{d\sigma_{\mathrm{KN}}}{d\Omega} \propto \vec s\cdot\bigl(\vec u_\eta\times\vec u_{\mathrm{out},k}\bigr)\,f(\omega,\theta) ,
$$
the magnetic Compton asymmetry; the electron spin enters through the spin-dependent part of the Dirac current, and the geometric factor is the normal to the scattering plane. The precise coefficients of the Klein–Nishina polarized cross-section are the standard Heitler result and are cited rather than re-derived; the next section states how the spin is encoded in the algebra.

## The Electron Spin Biquaternion

### The spin as a Hermitian biquaternion

The electron's spin enters the scattering through the same algebra as the photon's polarization, and the correspondence is worth stating. A spin-$\tfrac12$ state is encoded in a Hermitian biquaternion
$$
\tilde{Ϛ}_{\Psi,e} = \tfrac12\bigl(e_t + i\vec s\bigr) \in \mathbb{B}_{\Psi} ,
\qquad
\langle\tilde{Ϛ}_{\Psi,e}\rangle_{\natural} = \tfrac14\bigl(1 - \lvert\vec s\rvert^2\bigr) ,
\qquad
\vec s = \sum_\eta s_\eta\vec e_\eta ,
$$
the $i$ being what puts the vector part in the imaginary-vector direction that membership in $\mathbb{B}_{\Psi}$ requires, and with the normalisation $\mathrm{Sc}(\tilde{Ϛ}_{\Psi,e}) = \tfrac12$ that a density matrix carries. At $\lvert\vec s\rvert = 1$ it is a pure state, the idempotent the cone carries along its own axis; so the identification here is the companion article's, read on the spin instead of on the boost. Here $\vec s$ is the Bloch vector of the spin; the pure spin states have $|\vec s| = 1$ and lie on the biquaternion-norm cone of $\mathbb{B}_{\Psi}$, the mixed states fill the interior, and the spin-up and spin-down states along any axis are the two idempotents on the cone. The structure is formally identical to the coherence biquaternion of the beam: $\tilde{Ϛ}_{\Psi}$ and $\tilde{Ϛ}_{\Psi,e}$ are both elements of $\mathbb{B}_{\Psi}$ whose biquaternion norm measures purity, the Stokes vector playing the role of the Bloch vector. The photon's *polarization* states, by contrast, are vectors of $\mathbb{B}_{\Phi}$; the spin-$\tfrac12$ *states* are elements of $\mathbb{B}_{\Psi}$. The scattering problem therefore pairs an element of $\mathbb{B}_{\Phi}$ (the photon polarization) with an element of $\mathbb{B}_{\Psi}$ (the electron spin), and the amplitude is a pairing across the two sectors — a structural feature that index notation hides, because an index carries no sector.

### The spin sum is one written action

Averaging over the electron spin replaces the spin biquaternion by its trace part, $\tilde{Ϛ}_{\Psi,e}\to\tfrac12 e_t$ for the unpolarized ensemble, so the spin-dependent terms of the amplitude integrate to zero. The corresponding statement on the state side is the completeness relation of the plane waves, and written out it is one action on a biquaternion.

Write $D(p)$ for the action that sends a biquaternion $\tilde{Ξ}_{\mathrm{sp}}$ to
$$
\tilde{Ξ}_{\mathrm{sp}}\longmapsto i p_{0}\,\tilde{Ξ}_{\mathrm{sp}}\vec e_x-\sum_\eta i p_{\eta}\,\vec e_\eta\tilde{Ξ}_{\mathrm{sp}}\vec e_y+k_m\,\tilde{Ξ}_{\mathrm{sp}} ,
$$
with $p_0 = E/c$ and $k$ running over $x,y,z$, and read it as three terms. The first carries the energy: it multiplies the state on its right side by $\vec e_x$, with coefficient $ip_0$. The second carries the momentum: three components, each multiplying on the left by $\vec e_\eta$ and on the right by $\vec e_y$, with coefficient $-ip_\eta$. The third carries the mass, and no unit stands between its coefficient and the state. The completeness relation is the statement that this one action is the spin sum:
$$
\sum_{r=1}^{2}\tilde w^{(r)}(\vec p)\,\bigl\langle \tilde w^{(r)}(\vec p),\tilde{Ξ}_{\mathrm{sp}}\bigr\rangle_{\mathrm D}=D(p)\tilde{Ξ}_{\mathrm{sp}} .
$$
The left side is a sum of two pairings, each multiplied by the solution it pairs, and the two sides agree for every $\tilde{Ξ}_{\mathrm{sp}}$; the equality is therefore a statement about one action on the algebra, and it can be checked term by term.

Here $\langle\tilde w,\tilde w\rangle_{\mathrm D}=2m\,c$ is the covariant normalisation, and $\langle\tilde{Ξ}_{\mathrm{sp}},\tilde{Ξ}\rangle_{\mathrm D}=\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}\,i\vec e_x)$ is the Dirac pairing of the companion Solutions article. This is the **momentum-space** completeness relation: it sends every state into the two-dimensional space of the positive-frequency solutions of the one-sided pair, on which $D(p)\tilde{Ξ}_{\mathrm{sp}} = 2m\,c\tilde{Ξ}_{\mathrm{sp}}$, and applying it twice returns $2m\,c$ times itself,
$$
D(p)\bigl(D(p)\tilde{Ξ}_{\mathrm{sp}}\bigr)=2m\,c\,D(p)\tilde{Ξ}_{\mathrm{sp}} \qquad\text{on shell}.
$$
It is not the two-sided dictionary equation of *The Dirac Equation in Biquaternionic Form*; the two are separated in the Gamma Formulation below. Divided by $2m\,c$ the action is a projection of rank two, and its complement $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}}-\frac{1}{2\,m}D(p)\tilde{Ξ}_{\mathrm{sp}}$ is the negative-frequency projection; the two sum to the identity action. The averaged spin is therefore one projection, and its three terms are the whole of it.

### The resolved spin

Resolving the spin replaces that one action by two, one for each sign of the target's spin four-vector. The $\vec s$ of the previous subsection is the Bloch vector of a state, of length one when the state is pure; the object here is the same spin written covariantly, the four-vector $s$ of the target, with $s\cdot p=0$, $s^2=-1$, and rest-frame value $(0,\vec s)$.

Two actions carry the split. The first is the spin action, the shell's pattern with $s$ in place of $p$ and with the mass term dropped,
$$
\Sigma_s:\qquad \tilde{Ξ}_{\mathrm{sp}}\longmapsto i s_{0}\,\tilde{Ξ}_{\mathrm{sp}}\vec e_x-\sum_\eta i s_\eta\,\vec e_\eta\tilde{Ξ}_{\mathrm{sp}}\vec e_y ,
$$
and its square is $s\cdot s$ times the identity, which is $-1$: the cross terms cancel, because the coefficients are symmetric where the two units anticommute, and what remains is $s\cdot s$. The second is the bracket
$$
B_s:\qquad \tilde{Ξ}_{\mathrm{sp}}\longmapsto \tilde{Ξ}_{\mathrm{sp}}+s_{0}\,\tilde{Ξ}_{\mathrm{sp}}\vec e_y+\sum_\eta s_\eta\,\vec e_\eta\tilde{Ξ}_{\mathrm{sp}}\vec e_x ,
$$
half of which is a projection, because applying the bracket twice and halving twice returns the same bracket; and the brackets of $s$ and of $-s$ add to twice the identity, so the two halves are complementary projections. The resolved sums are the two compositions
$$
D_s(p):\quad \tilde{Ξ}_{\mathrm{sp}}\longmapsto \tfrac12\,D(p)\bigl(B_s\tilde{Ξ}_{\mathrm{sp}}\bigr),
\qquad
D_{-s}(p):\quad \tilde{Ξ}_{\mathrm{sp}}\longmapsto \tfrac12\,D(p)\bigl(B_{-s}\tilde{Ξ}_{\mathrm{sp}}\bigr),
$$
and they add term by term to $D(p)\tilde{Ξ}_{\mathrm{sp}}$, because $B_s\tilde{Ξ}_{\mathrm{sp}}+B_{-s}\tilde{Ξ}_{\mathrm{sp}}=2\tilde{Ξ}_{\mathrm{sp}}$. The spin enters the bracket in all four slots, so the split names the target's spin direction: the axial direction it uses is $s$ itself, no unit of the coefficient basis is singled out as its axis, and writing $-s$ for $s$ exchanges the two sums and changes nothing else.

The identity was verified at $m=1.3$ and $\vec p=(0.4,-0.7,0.9)$, with $s$ a unit spacelike four-vector orthogonal to $p$. Each of the two, divided by $2m\,c$, is a projection of rank one and trace one; the two are mutually orthogonal; and they sum to $D(p)$ to below $10^{-15}$. Spin resolution is therefore a decomposition of the shell into two orthogonal projections, and the unpolarized average is the trace part of the spin biquaternion, exactly as before.

Two further features of the split are properties of the algebra. Each term of $D(p)$ is a state multiplied by one unit on each side, and multiplying the state once more on either side composes the units of that side and multiplies the coefficients; the result is again a term of that shape. A split built from such multiplications therefore stays inside the algebra's own multiplication, and each resolved sum is a sum of terms shaped like the shell's three. And the cross-section difference between the two is twice the part of the squared amplitude that changes sign with $s$, which is why the asymmetry is a spin observable and why the photon's circular polarization and the electron's spin enter through the same axial direction.

That difference is the magnetic Compton asymmetry of the previous section, and its geometric factor is the normal to the scattering plane, $\vec u_\eta\times\vec u_{\mathrm{out},k}$, an element of the material sector. The axial direction of the split is what turns the two transverse photon directions into a vector, and the spin contracts with it; the asymmetry vanishes when the electron spin is not resolved, and it is the observable that polarized-target Compton experiments measure. In the framework the geometric factor and the photon polarization are elements of the same sector, and the spin biquaternion is the element of the other sector that the asymmetry pairs with; the structure of the spin-dependent cross-section is thus the same trilinear pattern — two material-sector vectors and one informational-sector element — that the photon polarimetry exhibits with the coherence biquaternion.

## The Polarization Algebra in One Place

Five objects carry the scattering problem — the photon's polarization, the beam's coherence, the helicity, the electron's spin, and the geometric factor — and each sits in a definite place in the algebra.

The **photon polarization** is a pure vector of $\mathbb{B}_{\Phi}$, either real (linear) or complexified (circular). It is not an idempotent and not in $\mathbb{B}_{\Psi}$; it is a direction in the transverse plane, and the two physical directions are the plane's basis.

The **coherence biquaternion** $\tilde{Ϛ}_{\Psi}$ **is an element of $\mathbb{B}_{\Psi}$** — the state element whose direction is the normalised Stokes vector and whose scale is the intensity $S_0$ — and it is the object that carries the beam's polarization state including partial coherence. Its biquaternion norm is the mass-shell-like invariant $\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural} = \frac14(S_0^2-|\vec S|^2)$, so the polarized states are the cone and the unpolarized state is the axis. The beam's coherence therefore lives on the same cone as the framework's spin-$\tfrac12$ idempotents and as the electron's spin biquaternion of the previous section — the Stokes vector playing the role of the Bloch vector — while the photon's own polarization vectors stay in $\mathbb{B}_{\Phi}$. That is the structural reason the Stokes algebra and the biquaternion-norm algebra agree.

The **helicity operator** is $\lambda = \tfrac{i}{2}\mathrm{ad}_{\vec u_\eta}$, the action $\lambda\varepsilon = \mathrm{Vect}(i\vec u_\eta\varepsilon)$, represented in $\mathbb{B}_{\Psi}$ by $i\vec u_\eta \in \mathbb{B}_{\Psi}$; the two physical polarizations are its $\pm1$ eigenvectors and the longitudinal direction is its zero eigenvector, and it is the generator of the circular-to-linear geometry: the azimuthal modulation $\cos2\theta_{\mathrm{azm}}$ of the Compton cross-section is a statement about this operator's eigenspaces.

The **geometric factor** of the scattering is the transverse projector $\delta_{ij}-\vec u_\eta_i\vec u_\eta_j$, which is the polarization sum, and the cross-section's polarization dependence is the pairing $|\mathrm{Sc}(\vec\varepsilon_{\mathrm{out}}^{*}\vec\varepsilon)|^2$ of two material-sector vectors. The unpolarized average replaces the squared pairing by the product of two projectors, $\tfrac{r_e^2}{2}P'_{ij}P_{ij}$ with $P'$ the incident and $P$ the outgoing transverse projector, and the integral of that product over the sphere is the total cross-section. For an incident beam along $\vec e_z$ the product is $P'_{ij}P_{ij} = 1+\cos^2\theta$, whose integral is $16\pi/3$, so the cross-section is $\tfrac{r_e^2}{2}\cdot\tfrac{16\pi}{3} = \tfrac{8\pi}{3}r_e^2$; it is the integral of the product of the two projectors, not of either trace alone.

Assembled, the amplitude of the Thomson process is a pairing of two material-sector vectors,
$$
\mathcal{M}\bigl(\vec\varepsilon_{\mathrm{out}},\vec\varepsilon\bigr)
= \mathrm{Sc}\bigl(\vec\varepsilon_{\mathrm{out}}^{*}\vec\varepsilon\bigr) ,
$$
the photon polarizations entering through this pairing and the electron spin through the trace part of its informational-sector element; when the spin is resolved the amplitude acquires the spin term and becomes trilinear in $(\vec\varepsilon,\vec\varepsilon_{\mathrm{out}},\vec s)$. The differential cross-section is the squared modulus of $\mathcal{M}$, summed over final and averaged over initial states exactly as in the operator formalism, and the sums are the two completeness relations the algebra supplies: the transverse projector $\delta_{ij}-\vec u_{\eta ,i}\vec u_{\eta ,j}$ for the photon, and the action $D(p)$ of §*The resolved spin* for the electron, replaced by the pair $D_{\pm s}(p)$ when the spin is resolved. This is the sense in which the polarization algebra of photon–electron scattering is a single algebraic object: the external states are the two sectors' elements, the free propagation supplies the two projectors, and the dynamics — the magnitude $r_e$ and the recoil factor $(\omega_{\mathrm{out}}/\omega)^2$ — is the standard field theory's contribution.

## The Biquaternion Structure of the Scattering

Four statements say what the framework contributes, and a fifth what it does not.

The polarization **states are native**: the transverse plane is the orthogonal complement of the propagation direction in the vector part of $\mathbb{B}_{\Phi}$, defined by the algebra's own biquaternion norm, and the circular basis is the eigenbasis of left multiplication by $\vec u_\eta$. This is not a reinterpretation of an external structure; it is the algebra's multiplication acting on its own vectors.

The polarization **purity is the biquaternion norm**: $P^2 = 1-\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural}/\mathrm{Sc}(\tilde{Ϛ}_{\Psi})^2$, the pure states are the cone, and depolarization is the interior. The beam's coherence and the framework's indefinite form are therefore the same object.

The scattering **amplitude is a pairing**: the Thomson amplitude is $\mathrm{Sc}(\vec\varepsilon_{\mathrm{out}}^{*}\vec\varepsilon)$, the cross-section is its modulus squared, and the polarization sum is the transverse projector. Every ingredient is one of the algebra's two pairings applied to polarization vectors, exactly as the action article's Lagrangians are pairings of fields and gradients.

The **mass enters as the one external scale**: the Klein–Nishina function depends only on $x =\frac{\omega}{c\,k_m}$, and the Thomson cross-section is its $x\to0$ limit, in which the recoil is negligible and the electron is effectively at rest. In the biquaternion-norm language the electron's mass is $\langle\tilde P_{\Phi,e}\rangle_{\natural} = -m^2c^2$ and the photon's is $\langle\tilde P_{\Phi,\mathrm{ph}}\rangle_{\natural} = 0$, so the kinematics joins a timelike momentum to a null one, and $x$ is the photon's energy in units of the electron's rest energy.

What the framework does **not** supply is the dynamics. The Thomson cross-section and the Klein–Nishina formula are consequences of the Maxwell–Dirac action and its quantisation, not of the algebra; the algebra organises the polarization bookkeeping and exhibits the states, the observables, and the geometric factors as elements of one structure, but the $r_e^2$ and the $(\omega_{\mathrm{out}}/\omega)^2$ come from the field theory. This is the same boundary the photon article draws: the framework transcribes the standard physics faithfully, and the specific facts attached to the photon and the electron are supplied from outside.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_\eta^2=-I_4$. The frame belongs to the coordinate, not to the array.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products. Each generator is one basis operator,
$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x}=iR_{\mathrm{pau},\vec e_x},\qquad
\gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\qquad
\gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\qquad
\gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\qquad
\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z},
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}=iR_{\mathrm{axf},\vec e_x},\qquad
\gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\qquad
\gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\qquad
\gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\qquad
\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z},
$$

with the interval and the orientation
$$
-{r'_{t}}^2+r_x^2+r_y^2+r_z^2,\qquad \epsilon_{0123}=+1 .
$$
The four directions carry the unit metric $\delta_{\mu\nu}$, and the one minus of the interval is the square of the $i$ in $Q_t=i r'_t$. The time generator is a **right** multiplication, the three spatial ones are **left-times-right**, and the mass unit $L_{\mathrm{pau},e_t}$ is the identity: the asymmetry is the frame, not a choice, and it is why the gradient $\tilde\nabla$ and the momentum $\tilde P_{\Phi}$ enter the basis operator formulation with one generator of each type.

Every factor of $i$ in these basis operators is the same central unit, so $i^2=-1$; the squares then come out with the weight's signs, and the two minus signs involved are distinct. For the time generator,
$$
(\gamma_0)^2 = i^2\,R_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_x} = i^2\,R_{\mathrm{pau},\vec e_x\vec e_x} = i^2\,R_{\mathrm{pau},-e_t} = (-1)(-1)\,I_4 = +I_4 ,
$$

In the axis-free display:

$$
(\gamma_0)^2 = i^2\,R_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_x} = i^2\,R_{\mathrm{axf},\vec e_x\vec e_x} = i^2\,R_{\mathrm{axf},-e_t} = (-1)(-1)\,I_4 = +I_4 ,
$$

the first minus from $i^2=-1$ and the second from $\vec e_x^2=-e_t$; for a spatial generator,
$$
(\gamma_\eta)^2 = i^2\,L_{\mathrm{pau},\vec e_\eta}L_{\mathrm{pau},\vec e_\eta}\,R_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y} = i^2\,(+I_4) = -I_4 ,
$$

The same identities in the axis-free display:

$$
(\gamma_\eta)^2 = i^2\,L_{\mathrm{axf},\vec e_\eta}L_{\mathrm{axf},\vec e_\eta}\,R_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y} = i^2\,(+I_4) = -I_4 ,
$$

because both quaternion squares are $-e_t$ and their product is $+I_4$. The squares carry the whole of the signs: the time basis operator squares to $+I_4$ and the spatial basis operators to $-I_4$, and the anticommutation relations below hold in every frame.

A product $M=ab$ of two elements has the coefficient matrix $c(M)_{ij}=a_ib_j$, of rank one: the products therefore fill the seven-dimensional cone $\operatorname{rank}c(M)\le1$ inside the sixteen-dimensional algebra, a general element is a sum of at most four of them, and $\ell(M)=\operatorname{rank}c(M)$ is that number.

The central grading of the complexified algebra, $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ with $\chi^2=e_t$, is a different object from $\gamma_5$: $\xi$ lives in the algebra, where the two central idempotents are $\tfrac12(e_t\pm\xi)$, while $\gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}$ is its representative on the Dirac module. That $\gamma_5$ is the same basis operator as the chirality basis operator $-iR_{\mathrm{pau},\vec e_z}$ of the spin section is why one factor separates the two helicities of the photon and the two spin states of the electron.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the basis operators span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the basis operators,
$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_\eta)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$, so that $\sum_\mu\gamma^\mu\gamma_\mu=-4I_4$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\mu=2\gamma_\alpha$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\beta\gamma_\mu=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu\gamma_\gamma\gamma_\beta\gamma_\alpha\gamma_\mu=-2\gamma_\gamma\gamma_\beta\gamma_\alpha$.

The fifth basis operator is $\gamma_0\gamma_1\gamma_2\gamma_3=-i\gamma_5=-R_{\mathrm{pau},\vec e_z}=-L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}$, the same basis operator written in the two displays.

The four contraction sums are statements about the squares, because a basis operator's square is. For generators that all square to $+I_4$ (written $\Gamma_\mu$ here), they take the textbook values,
$$
\sum_\mu\Gamma_\mu\Gamma_\mu=4I_4,\qquad
\sum_\mu\Gamma_\mu\Gamma_\alpha\Gamma_\mu=-2\Gamma_\alpha,\qquad
\sum_\mu\Gamma_\mu\Gamma_\alpha\Gamma_\beta\Gamma_\mu=4\delta_{\alpha\beta}I_4,\qquad
\sum_\mu\Gamma_\mu\Gamma_\alpha\Gamma_\beta\Gamma_\gamma\Gamma_\mu=-2\Gamma_\gamma\Gamma_\beta\Gamma_\alpha .
$$
For the basis operators of this article only the even one is a plain trace: $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$, since $\gamma_0^2=+I_4$ and the three spatial squares are $-I_4$. The odd ones depend on the signs as written, and the two that follow from the weight are worth recording, because the weight is not $\delta_{\mu\nu}$: with all indices down,
$$
\sum_\mu\gamma_\mu\gamma_0\gamma_\mu=4\gamma_0,\qquad
\sum_\mu\gamma_\mu\gamma_\eta\gamma_\mu=0 ,
$$
verified for the four directions. The covariant forms are recovered by raising one index, $\sum_\mu\gamma^\mu\gamma^\alpha\gamma_\mu=2\gamma^\alpha$, also verified.

**The two Dirac equations.** Two equations carry the name in this series, and the frame is what separates them. The first is the corpus's **one-sided** chiral pair,
$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L} ,\qquad
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R} ,
$$
in which the gradient acts by left multiplication only, the field is a section of $\Delta = S\oplus S^{\mathrm c}$, and the mass is the off-diagonal pairing of the two chiral halves. Its plane-wave reduction is the eigenvalue problem of the symbol basis operator of the spin section,
$$
D(p) = p_{0}\,\gamma_0-\sum_\eta p_{\eta}\,\gamma_\eta+m\,L_{\mathrm{pau},e_t}R_{\mathrm{pau},e_t} ,
\qquad
D(p)\tilde{Ξ}_{\mathrm{sp}} = 2m\,c\,\tilde{Ξ}_{\mathrm{sp}} \ \ \text{on the positive-frequency solutions},
$$

The same expressions, in the axis-free display:

$$
D(p) = p_{0}\,\gamma_0-\sum_\eta p_{\eta}\,\gamma_\eta+m\,L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t} ,
\qquad
D(p)\tilde{Ξ}_{\mathrm{sp}} = 2m\,c\,\tilde{Ξ}_{\mathrm{sp}} \ \ \text{on the positive-frequency solutions},
$$

and the basis operator obeys $D(p)^2 = 2m\,c\,D(p)$ on shell, so $D(p)/2m\,c$ is the projector of rank two that the previous section uses. The basis operator that carries its chirality is $\gamma_5=-iR_{\mathrm{axf},\vec e_z}$, a pure right multiplier, and its projectors $\tfrac12(1\pm\gamma_5)$ separate the chiral halves; the central sign $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ is the same operator written centrally, and $\tfrac12(e_t\pm\xi)$ are its central idempotents.

The second is Kravchenko's **two-sided** equation, the dictionary form on $\mathbb{B}$,
$$
\mathcal{N}F = \Bigl(i\frac{\partial}{\partial r'_t}+D_3\Bigr)F - k_mi\,\overline{F}\,\vec e_z = 0 ,
\qquad\text{that is}\qquad
-\tilde\nabla^{\natural}F - k_mi\,\overline{F}\,\vec e_z = 0
$$
where $D_3=\sum_\eta\vec e_\eta\,\partial/\partial R_\eta$ is the three-dimensional Cauchy–Riemann operator, the bar is the componentwise conjugation and $\vec e_z$ multiplies from the right. Its mass term is a conjugation together with a fixed direction rather than an off-diagonal pairing, the basis operator that carries its split is $\gamma_5=i\omega$ with $\omega=-L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}$, and its analytic machinery is the Cauchy theory of the dictionary article.

| Aspect | One-sided equation | Two-sided equation |
|---|---|---|
| Form | $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^\natural\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R}$ | $\mathcal{N}F=0$, that is $-\tilde\nabla^{\natural}F-k_mi\,\overline{F}\,\vec e_z=0$ |
| Multiplication | left, by $\tilde\nabla$ and $\tilde\nabla^\natural$ | left, plus right by $\vec e_z$ in the mass term, plus the antilinear bar |
| Mass | off-diagonal pairing of $S$ and $S^{\mathrm c}$ | $-k_mi\,\overline{F}\,\vec e_z$ |
| Chirality | the side: the right slot for a right multiplier, both slots for a central scalar | the basis operator that realises the split is $\gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}=i\omega$, with $\omega=-L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}$; in the axis-free display $\gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}=i\omega$, with $\omega=-L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}$ |
| Use | kinematics, spin sums, and this article | the dictionary, the Cauchy theory, the integral representation |

The two are related by the dictionary and are not the same operator; the scattering problem uses only the first, with the second entering exclusively through the identity of the basis operator.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a basis operator named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The polarization algebra of photon–electron scattering in the biquaternion framework places the photon's polarization in the vector part of the material sector, the beam's coherence in the Hermitian sector, and the scattering geometry in the transverse projector of the material sector.

Thomson scattering has the differential cross-section $d\sigma_T/d\Omega = r_e^2|\varepsilon_{\mathrm{fop},\mathrm{out}}\cdot\varepsilon_{\mathrm{fop}}|^2 = r_e^2|\mathrm{Sc}(\vec\varepsilon_{\mathrm{out}}^{*}\vec\varepsilon)|^2$, whose outgoing-polarization sum is $r_e^2\sin^2Ζ$ (verified to $10^{-15}$) and whose unpolarized average is $r_e^2(1+\cos^2\theta)/2$, integrating to $\sigma_T = 8\pi r_e^2/3$, which is $0.66524587$ barn with the CODATA classical electron radius. The Mueller matrix transfers linear polarization with degree $P(\theta) = \sin^2\theta/(1+\cos^2\theta)$, equal to one at $90^\circ$ (verified at six angles), carries circular polarization with degree $P_c(\theta) = 2\cos\theta/(1+\cos^2\theta)$, which vanishes at $90^\circ$ and reverses sign beyond it, and does not convert circular to linear polarization.

Compton scattering shifts the frequency to $\omega_{\mathrm{out}} = \omega/[1+(\frac{\omega}{c\,k_m})(1-\cos\theta)]$, verified to put the recoil electron on its mass shell to $3\times10^{-14}$ MeV$^2$; the Klein–Nishina differential cross-section integrates to the standard analytic total to a relative error below $10^{-9}$ at five energies and reduces to the Thomson value as $x\to0$ ($8.3760\,r_e^2$ at $x=10^{-4}$ against $8.3776\,r_e^2$). The polarized cross-section carries an azimuthal $\cos2\theta_{\mathrm{azm}}$ modulation and an electron-spin asymmetry $\propto\vec s\cdot(\vec u_\eta\times\vec u_{\mathrm{out},k})$, standard results cited rather than re-derived. In the framework the electron's spin sum is one action on a biquaternion, $D(p)$ sending $\tilde{Ξ}_{\mathrm{sp}}$ to $ip_0\tilde{Ξ}_{\mathrm{sp}}\vec e_x-\sum_\eta ip_\eta\vec e_\eta\tilde{Ξ}_{\mathrm{sp}}\vec e_y+k_m\tilde{Ξ}_{\mathrm{sp}}$, and its spin-resolved form is the pair of orthogonal projections
$$
D_{\pm s}(p):\quad \tilde{Ξ}_{\mathrm{sp}}\longmapsto \tfrac12\,D(p)\bigl(B_{\pm s}\tilde{Ξ}_{\mathrm{sp}}\bigr),
\qquad
B_{\pm s}:\quad \tilde{Ξ}_{\mathrm{sp}}\longmapsto \tilde{Ξ}_{\mathrm{sp}}\pm s_{0}\,\tilde{Ξ}_{\mathrm{sp}}\vec e_y\pm\sum_\eta s_\eta\,\vec e_\eta\tilde{Ξ}_{\mathrm{sp}}\vec e_x ,
$$
which sum back to $D(p)$, each being a projection of rank one; the asymmetry is the part of the cross-section that changes sign with $s$, the same axial direction that carries the photon's circular polarization. The electron's spin biquaternion is a Hermitian element with the same cone structure as the beam's coherence biquaternion. The Legacy Pauli Gamma Formulation names the frame in which all of this is written, and separates the two Dirac equations of the series: the one-sided chiral pair that the scattering uses, and the two-sided equation that belongs to the dictionary.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P_{\Phi,\mathrm{ph}} = i(\omega/c)e_t+\vec k_\Phi$ | Photon wave biquaternion; $\langle\tilde P_{\Phi,\mathrm{ph}}\rangle_{\natural} = 0$ |
| $\tilde P_{\Phi,e}$ | Electron four-momentum; $\langle\tilde P_{\Phi,e}\rangle_{\natural} = -m^2c^2$; at rest $\tilde P_{\Phi,e} = imc\,e_t$ |
| $\varepsilon_{\mathrm{fop}}, \varepsilon_{\mathrm{fop},\mathrm{out}}$ | Incident and outgoing linear polarization unit vectors |
| $\varepsilon_{\mathrm{fop},\pm} = (\varepsilon_{\mathrm{fop},1}\pm i\varepsilon_{\mathrm{fop},2})/\sqrt2$ | Circular polarizations; $\vec u_\eta\varepsilon_{\mathrm{fop},\pm} = \mp i\varepsilon_{\mathrm{fop},\pm}$ |
| $\lambda = \vec u_\eta\cdot\vec S = \tfrac{i}{2}\mathrm{ad}_{\vec u_\eta}$, with $\lambda\varepsilon = \mathrm{Vect}(i\vec u_\eta\varepsilon)$ | Helicity operator; spectral values $\{+1,0,-1\}$, representative $i\vec u_\eta\in\mathbb{B}_{\Psi}$ |
| $\delta_{ij}-\vec u_\eta_i\vec u_\eta_j$ | Transverse projector; the polarization sum |
| $S_0,\vec S$ | Stokes parameters |
| $\tilde{Ϛ}_{\Psi}$ | Coherence biquaternion, the state element of $\mathbb{B}_{\Psi}$ scaled by the intensity $S_0$; $\vec S=\sum_\eta S_\eta\vec e_\eta$ is its vector part |
| $\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural} = \frac14(S_0^2-\lvert\vec S\rvert^2)$ | Purity; the degree of polarization is $P = \lvert\vec S\rvert/S_0$ |
| cone $\langle\tilde{Ϛ}_{\Psi}\rangle_{\natural} = 0$ | Fully polarized states; its section at $2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}) = 1$ is the Poincaré sphere |
| $r_e = e^2/(4\pi\epsilon_0 mc^2)$ | Classical electron radius |
| $d\sigma_T/d\Omega = r_e^2\lvert\varepsilon_{\mathrm{fop},\mathrm{out}}\cdot\varepsilon_{\mathrm{fop}}\rvert^2$ | Thomson differential cross-section |
| $\sigma_T = 8\pi r_e^2/3$ | Thomson total cross-section; $0.66524587$ barn |
| Mueller matrix (scattering-plane basis) | $d\sigma_T/d\Omega$ as the linear map on $(I,Q,\mathcal U,\mathcal V)$; $Q$ positive for polarization perpendicular to the scattering plane |
| $P(\theta) = \sin^2\theta/(1+\cos^2\theta)$ | Degree of linear polarization of unpolarized Thomson-scattered light |
| $P_c(\theta) = 2\cos\theta/(1+\cos^2\theta)$ | Degree of circular polarization retained by a circularly polarized beam |
| $\omega_{\mathrm{out}} = \omega/[1+x(1-\cos\theta)]$ | Compton shift |
| $x =\frac{\omega}{c\,k_m}$ | The one dimensionless scale |
| $d\sigma_{\mathrm{KN}}/d\Omega$ | Klein–Nishina differential cross-section |
| $\sigma_{\mathrm{KN}}(x)\to\sigma_T$ | Thomson limit |
| $A(\omega,\theta)+B(\omega,\theta)\cos2\theta_{\mathrm{azm}}$ | Azimuthal modulation for a linearly polarized incident beam; $\lvert B/A\rvert$ is the analysing power |
| $\vec s\cdot(\vec u_\eta\times\vec u_{\mathrm{out},k})$ | Electron-spin asymmetry (magnetic Compton) |
| $\tilde{Ϛ}_{\Psi,e} = \frac12(e_t+i\vec s)\in\mathbb{B}_{\Psi}$ | Electron spin biquaternion; $\langle\tilde{Ϛ}_{\Psi,e}\rangle_{\natural} = \frac14(1-\lvert\vec s\rvert^2)$ |
| $D(p)$ | The shell action, $\tilde{Ξ}_{\mathrm{sp}}\mapsto ip_0\tilde{Ξ}_{\mathrm{sp}}\vec e_x-\sum_\eta ip_\eta\vec e_\eta\tilde{Ξ}_{\mathrm{sp}}\vec e_y+k_m\tilde{Ξ}_{\mathrm{sp}}$; the spin sum $\sum_r\tilde w^{(r)}\langle\tilde w^{(r)},\cdot\rangle_{\mathrm D}$, a projection of rank two when divided by $2m\,c$ |
| $\Sigma_s$ | Spin action, $\tilde{Ξ}_{\mathrm{sp}}\mapsto is_0\tilde{Ξ}_{\mathrm{sp}}\vec e_x-\sum_\eta is_k\vec e_\eta\tilde{Ξ}_{\mathrm{sp}}\vec e_y$; the shell's pattern with $s$ in place of $p$ and no mass term |
| $B_s$ | The bracket of the split, $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}}+s_0\tilde{Ξ}_{\mathrm{sp}}\vec e_y+\sum_\eta s_\eta\vec e_\eta\tilde{Ξ}_{\mathrm{sp}}\vec e_x$; half of it is a projection, and $B_s+B_{-s}$ is twice the identity action |
| $D_s(p)$ | The resolved shell, $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tfrac12 D(p)(B_s\tilde{Ξ}_{\mathrm{sp}})$; $\frac{1}{2\,m}D_s$ is a projection of rank one, and $D_s+D_{-s}=D(p)$ |
| $s$, $s\cdot p=0$, $s^2=-1$ | Spin four-vector of the target; rest frame $(0,\vec s)$, with $\vec s$ the Bloch vector of the state |
| $\langle\tilde{Ξ}_{\mathrm{sp}},\tilde{Ξ}\rangle_{\mathrm D}=\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^*\tilde{Ξ}\,i\vec e_x)$ | Dirac pairing; $\langle\tilde w,\tilde w\rangle_{\mathrm D}=2m\,c$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- Oskar Klein and Yoshio Nishina, "Über die Streuung von Strahlung durch freie Elektronen nach der neuen relativistischen Quantendynamik von Dirac", *Zeitschrift für Physik* **52** (1929), for the Klein–Nishina cross-section and its derivation.
- Walter Heitler, *The Quantum Theory of Radiation* (Oxford, 3rd edn, 1954), for the polarization of Compton-scattered radiation, the polarization asymmetry, and the electron-spin terms.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 3rd edn, 1998), for the classical Thomson scattering, the Larmor power, and the polarization dependence of dipole radiation.
- V. B. Berestetskii, E. M. Lifshitz, and L. P. Pitaevskii, *Quantum Electrodynamics* (Pergamon, 2nd edn, 1982), for the Compton effect, the polarization sum, and the spin-dependent cross-section.
- R. P. Feynman, *Quantum Electrodynamics* (Benjamin, 1961), for the spinor and polarization algebra of the scattering amplitude.
- M. Born and E. Wolf, *Principles of Optics* (Cambridge, 7th edn, 1999), for the Jones calculus, the Stokes parameters, the coherence matrix, and the Poincaré sphere.
- F. W. Byron and R. W. Fuller, *Mathematics of Classical and Quantum Physics* (Dover, 1992), for the completeness and projection relations of polarization vectors.
- The companion articles of this series: [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html), [Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation](exercise-plane-wave-solutions-of-the-biquaternion-dirac-equation.html), [Møller Scattering in Biquaternionic Form](moller-scattering-in-biquaternionic-form.html), [The Photon in Biquaternionic Form](the-photon-in-biquaternionic-form.html), and [The Field-Strength Biquaternion and Its Invariants](the-field-strength-biquaternion-and-its-invariants.html).
