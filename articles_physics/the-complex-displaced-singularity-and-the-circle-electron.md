# __The Complex-Displaced Singularity and the Circle Electron__

## Introduction

In the biquaternion interpretation of electrodynamics, the vacuum Maxwell equation $\tilde\nabla_\Phi\tilde{F}=0$ is the four-dimensional Cauchy–Riemann condition, and a charged particle is a **singularity** of the field rather than a source (*Maxwell's Equations in the Biquaternionic Formulation*, *Radiation from Accelerated Charges in Biquaternionic Form*). Lanczos, in the doctoral dissertation of 1919, took that interpretation one step further and asked a question that the source-free equation makes natural: if the field is a function of the biquaternionic position, what fixes the **position of the singularity**? Nothing in the vacuum equation does. The second half of his chapter on the electron as a singularity therefore perturbs the singularity's position off the material slice, into what he calls complexified space, and shows that the perturbation does not destroy the field theory — it replaces the point charge by a **ring**.

This article develops that construction in the corpus conventions. It is the one place in the corpus where a singularity is deliberately displaced off the material subspace $\mathbb{B}_{\Phi}$, and it is the classical, linear counterpart of the **algebrodynamical ring**, which the corpus records on a nonlinear primary equation (*The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry*). The rings are different objects on different equations, and the contrast is drawn below; a third ring, the same object as Lanczos's but in motion, is added in *The Ring in Imaginary Motion*.

The article is in three steps. It fixes the singular set of the displaced potential, which is a circle rather than a point. It reads the field of the ring, which acquires an intrinsic magnetic-type component that Gsponer and Hurni call **mesomagnetic**. And it records Lanczos's self-energy result, the finite difference of two separately divergent energies, which is the reason he believed the circle electron escaped the divergence of the point model. The result is a source claim of 1919, recorded here with the formula by which Lanczos reached it and with the numerical check of that formula. A fourth step follows, and it belongs to a different source: the displacement need not be constant, and letting it move along the informational axis turns the ring into a contracting and re-expanding one. That construction is recorded with its verification, its one structural point, and the caveat its author draws from it.

## The Displaced Potential and Its Singular Set

### The Coulomb Kernel and the Position of the Singularity

In the stationary sector the field is carried by the scalar potential alone, and the four-potential is a material element with a purely imaginary scalar part,

$$
\tilde{A}_{\Phi} = i\,a'_t\,e_t \in \mathbb{B}_{\Phi}, \qquad Ξ(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) = \frac{ϙ}{4\pi\epsilon}\,\frac{1}{\|r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z-\vec r_0\|},
$$

where $\vec r_0$ is the position of the point charge, $\epsilon$ is the permittivity of the medium, and $\|(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\|$ is the ordinary Euclidean length of the vector part. The potential is singular on the set $r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z=\vec r_0$, a single point, and it is the kernel $1/\|r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z-\vec r_0\|$ whose geometry the construction uses; the charge and the permittivity enter only as the overall factor $ϙ/4\pi\epsilon$ and are set aside below.

Lanczos introduces potential and field strength as **complex** quantities. If the potential is complex-valued, then in his interpretation there is no reason for the constants $(\zeta,\eta,\upsilon)$ that locate the singularity to be real, and the natural generalisation is to let them range over the complex numbers. A rotation and a translation of the coordinates bring the singularity to

$$
\zeta = 0, \qquad \eta = 0, \qquad \upsilon = -i\varrho, \qquad \varrho \in \mathbb{R}_{>0},
$$

so that the whole displacement of the singularity from the origin is

$$
\Delta\tilde{Q} = \upsilon\,\vec e_z = -i\varrho\,\vec e_z .
$$

**The displacement is informational.** The element $-i\varrho \vec e_z$ has a purely imaginary vector coefficient, so it is an element of the informational sector $\mathbb{B}_{\Psi}$, and in that sector's own coordinates it is the displacement $h'_{z} = -\varrho$ along the third informational axis. Lanczos's phrase "displacing the electron into complexified space" is, in the corpus's terms, displacing the singularity along an **imaginary direction of the vector coefficient** — that is, along $\mathbb{B}_{\Psi}$. The field points themselves remain material: they are the real elements $r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$, and the potential is evaluated on them. The construction therefore places the singularity in one sector and reads its field in the other.

### The Square of the Distance and the Ring

With $\vec r_0 = -i\varrho \vec e_z$ the squared Euclidean separation is

$$
\|r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z-\vec r_0\|^2 = r_x^2 + r_y^2 + (r_z+i\varrho)^2 = \bigl(r_x^2+r_y^2+r_z^2-\varrho^2\bigr) + 2i\,r_z\varrho ,
$$

a **complex** number, and the potential is the reciprocal square root of it,

$$
Ξ(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) = \frac{1}{\sqrt{\,r_x^2 + r_y^2 + (r_z+i\varrho)^2}} .
$$

The singular set is the zero set of the radicand. Writing the radicand as $A+iB$ with $A=r_x^2+r_y^2+r_z^2-\varrho^2$ and $B=2r_z\varrho$, the zero set is $A=0$ together with $B=0$. The second condition gives $r_z=0$, and with $r_z=0$ the first gives $r_x^2+r_y^2=\varrho^2$. Hence the singular set of the real coordinates is the **circle**

$$
\boxed{\;\Gamma : \qquad r_z = 0, \qquad r_x^2 + r_y^2 = \varrho^2\;}
$$

a ring of radius $\varrho$ in the plane $r_z=0$, centred on the third axis. This is Lanczos's **circle electron**, *Kreiselektron*. A point singularity of the real potential has been opened into a ring by displacing its position into the informational sector. The radius of the ring is the magnitude of the imaginary part of the displacement, $\varrho=|\upsilon|$, and the point electron is recovered in the limit $\varrho\to0$.

## The Branch Disk and the Two Sheets

The circle is not the only distinguished set. Because $Ξ$ is built from a square root, the circle bounds a **branch disk** on which the two determinations of the root meet and the function fails to be single-valued:

$$
D : \qquad r_z=0, \qquad r_x^2+r_y^2 < \varrho^2 .
$$

Across the disk the square root reverses sign, so $Ξ$ changes sign. On the disk itself the radicand is real and negative, $r_x^2+r_y^2-\varrho^2<0$, so the root is purely imaginary and $Ξ$ is purely imaginary there; outside the ring, on the same plane, the radicand is real and positive and $Ξ$ is real. The potential therefore interpolates, as the plane $r_z=0$ is crossed, between the real and the purely imaginary determinations, and the whole of the disk, and not only its boundary, is a locus of the multi-valuedness.

**Kerr's two sheets are the two determinations of the root.** The identity recorded below in *Relation to the Algebrodynamical Ring*, with its $a$ written $\varrho$, gives the displaced distance in the oblate coordinates of the Kerr solution (Burinskii, arXiv:1701.01025, eq. 7) as $r_*=r+i\varrho\cos\theta$, with $r_*^2=r_x^2+r_y^2+(r_z+i\varrho)^2$. Its zero set is $r=0$ together with $\cos\theta=0$, which is the ring $\Gamma$. On the disk $r=0$ its square is $-\varrho^2\cos^2\theta$, real and negative, so $r_*$ is purely imaginary there and its two determinations are $\pm i\varrho\lvert\cos\theta\rvert$: the branch disk $D$ is Kerr's disk, and the two signs are the two sheets. The sheets meet on the ring, and their interchange is the reversal of the branch — the map $(r,\theta)\mapsto(-r,\pi-\theta)$ sends $r_*$ to $-r_*$, verified symbolically. Read in these coordinates the displacement is therefore not the constant $\varrho$ of the preceding sections: it is $\varrho\cos\theta$, up to sign, the fixed axial displacement weighted by the cosine of the oblate angle, largest on the axis and zero at the rim. No gravitational statement is added by the reading. What the identity says is that the coordinates in which the Kerr–Newman solution is written carry the displaced kernel of this article as their squared radial distance, and that the singular ring, the branch disk and the two sheets of that solution are the ring $\Gamma$, the disk $D$ and the two determinations of the square root.

This is the point at which the two interpretations of the displacement differ. **In Lanczos's own interpretation** the sign change of $Ξ$ is harmless for the field theory: the field strength $\tilde{F}$ is built from the potential by differentiation and changes sign in the same way, so the **product** of the potential and the field strength is continuous across the disk, and Lanczos integrates over the disk "above and below" and finds the contribution regular. The disk is thus a defect of the potential's single-valuedness and not of the field's regularity in his sense. **In the corpus's interpretation** the potential is a function on the biquaternion algebra, the displacement $\Delta\tilde{Q}$ is an element of $\mathbb{B}_{\Psi}$, and the disk is the locus where the branch of the kernel must be chosen; the single-valued object is the field strength, not the potential, and the choice of branch is what a Cauchy-theoretic treatment would have to fix. In both interpretations the disk carries the branch structure and the circle carries the singularity.

The single-valued physical statement that survives is this: **the singular locus of the circle electron is the ring $\Gamma$, and the ring is thin — a line in space, not a surface.** The disk is a multi-valuedness of the potential, visible in the sign of the field strength but not a set on which the field strength itself diverges.

## The Field of the Ring: the Mesomagnetic Component

### The Field Strength Is Complex

Because the potential is complex, its gradient is complex, and the field of the configuration

$$
\vec E(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) = -\mathrm{grad}\,Ξ(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) = -\bigl(\partial/\partial r_xΞ\,\vec e_x + \partial/\partial r_yΞ\,\vec e_y + \partial/\partial r_zΞ\,\vec e_z\bigr)
$$

has both a real and an imaginary part at every point off the ring and off the disk. Writing $Ξ=Ξ_R+iΞ_I$, the real part $-\mathrm{grad}\,Ξ_R$ is the electric field of the configuration and the imaginary part $-\mathrm{grad}\,Ξ_I$ is a second field that survives from the displacement into $\mathbb{B}_{\Psi}$. The imaginary part is not an artefact of the bookkeeping: it is nonzero at generic points, as it must be whenever $\varrho\neq0$, and it vanishes identically at $\varrho=0$, where the point electron is recovered and the field is purely electric.

Away from the singular set the potential remains harmonic, since it is the analytic continuation of the harmonic Coulomb kernel in the parameter $\upsilon$; each of the two parts $Ξ_R,Ξ_I$ therefore satisfies the three-dimensional Laplace equation separately, and the two fields are divergence- and curl-free where they are defined. The ring is the only singularity of the field. The check is direct: the Laplacian of $Ξ$ computed by central differences at a hundred points off the ring is below $10^{-7}$, the level of the finite-difference error.

### Why the Second Field Is Mesomagnetic, Not Magnetic

An electric field that acquires an imaginary component under a displacement of the source looks at first like an electric field accompanied by a magnetic field, and Lanczos's calculation treats it that way: the second field of the displaced configuration is what supplies the compensating energy of the next section. Gsponer and Hurni record a correction that the corpus keeps with the claim. The second component is **not** an ordinary magnetic field. The magnetic field of electromagnetism is an axial vector, the field of a circulation, and it reverses under a space reflection while the electric field — a polar vector — does not. The imaginary component of the displaced field transforms as a **polar** vector, exactly as the electric field does, so it cannot be the magnetic field. Gsponer and Hurni name it a **mesomagnetic** field, and they note that the transformation properties of improper Lorentz transformations such as space reflection were not understood in 1919 and cannot be charged to Lanczos.

The corpus records both statements and keeps them apart. What is certain is the algebra: the displacement into $\mathbb{B}_{\Psi}$ produces a second field whose transformation character differs from that of the ordinary magnetic field. Whether it is called magnetic, mesomagnetic, or a mere imaginary part of a complexified electric field is a question of **physical interpretation** that the algebra does not decide.

**The far field is the point field.** The mesomagnetic forces are appreciable only near the ring. At distances large compared with $\varrho$ the displacement is a small perturbation of the position, and the field of the circle electron differs from that of the point electron by a quantity that vanishes with $\varrho/\|(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\|$. The ring is invisible from far away.

## The Ring in Imaginary Motion

The displacement $\Delta\tilde{Q}=-i\varrho\,\vec e_z$ of the preceding sections is a constant, and the ring it produces is stationary. A second construction of the same ring, due to Kassandrov, lets the displacement vary with the real time and obtains a ring that contracts to a point and re-expands [Kassandrov 2009]. The construction belongs to the programme the corpus records in *The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry*: the ring is the caustic locus of a shear-free null congruence generated by a "virtual" charge moving along a complex world line, and the electromagnetic field is the one the congruence carries. No biquaternion algebra enters it. It is recorded here because the object it produces is the object this article owns, and because the deformation is a motion along the informational axis.

The signature is the paper's own, $(+,-,-,-)$, and the time is the article's $r'_t=c\,t'$, a length, so the light-cone condition below is already $c$-carried and a speed is quoted as the ratio $V/c$; every inequality on a speed is an inequality on that ratio. **Two letters must be kept apart.** The paper writes $\rho$ for the ring radius in its final formula; this article reserves $\rho=\sqrt{r_x^2+r_y^2}$ for the cylindrical radius and writes $\varrho(r'_t)$ for the ring radius.

### The Complex World Line

The virtual charge moves uniformly along the informational axis,

$$
z_0(r'_t) = -i\,a + i\,v\,r'_t, \qquad a\in\mathbb{R}_{>0},\ v\in\mathbb{R},
$$

so that its displacement from the material slice is $-i(a-vr'_t)\vec e_z$: the same element of $\mathbb{B}_{\Psi}$ as the static displacement, with $\varrho$ replaced by $a-vr'_t$. The paper calls $v$ the imaginary velocity of the virtual charge. It is a parameter of the complex world line, not a speed, and no body moves at $v\vec e_z$; what it measures is the rate at which the displacement along the informational axis changes.

### The Caustic Condition and the Radius

The rays of the congruence are the generators of the complex null cone of the moving charge, $S=0$ with

$$
S=(r'_t-\sigma)^2-(r_z+i a-i v\sigma)^2-\rho^2 ,
$$

where $\sigma$ is the complex retarded time, and the caustics are the locus on which the retarded distance vanishes, $S'(\sigma)=0$. Solving the two conditions together, and restricting to the plane $r_z=0$ on which the solution is real, gives

$$
\varrho(r'_t)^2=\frac{(v r'_t-a)^2}{1+v^2}, \qquad \sigma=\frac{r'_t+a v}{1+v^2},
$$

and the singular set is the ring $\Gamma(r'_t): r_z=0$, $r_x^2+r_y^2=\varrho(r'_t)^2$. The elimination was recomputed symbolically here, and the branching points of the distance $r_b$ below were checked to coincide with it. The paper prints the radius as $-\frac{a}{\sqrt{1+v^2}}+\frac{v}{\sqrt{1+v^2}}r'_t$, which is negative on one side of $r'_t=a/v$; it is a signed coordinate, and the radius is its absolute value. For $v>0$ the ring contracts and then expands; for $v<0$ the order is reversed.

| $r'_t$ (for $v>0$) | $\varrho(r'_t)$ | The ring |
|---|---|---|
| $r'_t<a/v$ | $(a-vr'_t)/\sqrt{1+v^2}$, decreasing | contracting |
| $r'_t=a/v$ | $0$ | a point at the origin |
| $r'_t>a/v$ | $(vr'_t-a)/\sqrt{1+v^2}$, increasing | expanding |

The speed of the ring is the rate of $\varrho$,

$$
\frac{V}{c}=\frac{v}{\sqrt{1+v^2}}<1 ,
$$

for every finite $v$, however large. This is the source's application of Bateman's result that all singularities of a solution of the complex eikonal equation lie on a surface that propagates more slowly than light. The corpus records it in that status. Its content for this article is a sharpening of the reading of $v$: the parameter of the complex world line may be arbitrarily large, while the speed of the material image of the motion may not exceed $c$. Two values are worth fixing. At $r'_t=0$ the ring has radius $a/\sqrt{1+v^2}$, so the displaced motion starts from a ring smaller than the static one. And at $v=0$ the radius is $a$ at every $r'_t$, which is the stationary construction of the preceding sections: **the Lanczos ring is the member $v=0$ of this family.**

### The Field, and the Two Readings of the Imaginary Part

The field carried by the congruence is, in cylindrical coordinates,

$$
E_\rho=\pm\tilde ϙ\,\frac{\rho}{r_b^3}, \qquad E_z=\pm\tilde ϙ\,\frac{r_z-z_0}{r_b^3}, \qquad E_{\mathrm{azm}}=-v\,E_\rho ,
\qquad r_b^2=(r_z-r_{0z})^2+\rho^2(1+v^2), \qquad \tilde ϙ=ϙ(1+v^2),
$$

with $r_{0z}=r_{0z}(r'_t)$ and $r_b$ complex. At $v=0$ this is $ϙ$ times the unit field of the preceding section: with $r_b^2=\rho^2+(r_z+ia)^2$ the three components are $ϙ$ times the gradient of $-1/r_b$, which was checked by differentiation. The ring is the branch locus of $r_b$, the field is two-valued and the branches exchange under a circuit of the ring, it diverges as $\delta^{-3/2}$ at distance $\delta$ from the ring, and at the instant of the collapse the vortex component $E_{\mathrm{azm}}$ falls off only as $1/r^2$. Those are the paper's statements, recorded and not recomputed here.

The split of the complex field is read differently by the two sources, and the difference must not be smoothed. The paper takes $\Re\vec E$ as the electric field and $\Im\vec E$ as the magnetic one, and remarks that the result is formally the field of a charge moving uniformly along $OZ$ with an imaginary velocity, obtainable from the Coulomb field by a complex boost. **This article's reading is the one of the preceding section**: the imaginary part is the mesomagnetic component, which is polar under space reflection and therefore is not the magnetic field. The two readings name the same complex object; the test that separates them is the transformation character, and it favours the second. The source's identification is recorded and not adopted.

Two further properties of the field are the ones that bear on the rest of the corpus. The electric charge is **time-independent** — it is the flow of the electric field through a surrounding sphere, it does not depend on $v$ or on $r'_t$, and it takes the elementary value $|ϙ|=\tfrac14$ that the programme's quantisation fixes, so that the freedom Lanczos's construction leaves in the charge is removed by the congruence. The **magnetic moment is not**: it is proportional to the current radius of the ring, so it vanishes at the collapse and equals $ϙa$ in the static limit. This is the source's reading of the metric sector, and he states it as a conjecture to be confirmed by an exact electrovacuum solution.

### The Principal Spinor

The congruence is generated by the principal spinor, and its ratio of components is

$$
g=(1+i v)\,\frac{r_x+ir_y}{(r_z-r_{0z})\pm r_b},
$$

whose two signs are the two sheets of the ring, as in the static case. It satisfies both the complex eikonal equation and the wave equation, $(\partial g/\partial r'_t)^2-(\partial g/\partial r_x)^2-(\partial g/\partial r_y)^2-(\partial g/\partial r_z)^2=0$ and $(\partial^2/\partial {r'_t}^2-\partial^2/\partial r_x^2-\partial^2/\partial r_y^2-\partial^2/\partial r_z^2)g=0$, which were verified here by finite differences on both branches at $v=0$, $0.4$, $1.5$ and $3$, the residual falling as the square of the step as it should. At $v=0$ it is the spinor of the static complex-shifted congruence, and for $a\to0$ it reduces to the stereographic projection $S^2\to\mathbb{C}$, $g=(r_x+ir_y)/(r_z\pm r)$.

The reason the spinor is worth recording is that it is where the deformation is visible most cheaply: the only change from the static case is the complex time dependence of $z_0$ and the factor $(1+iv)$. The eikonal equation, the wave equation and the algebraic structure of the congruence are the same in the two cases, and so is the reading of the eikonal as the null condition on the gradient — the vanishing of the biquaternion norm of the gradient, which is the zero-divisor cone of the algebra.

### The Instability

The static congruence is one member of the family, and the source draws a strong conclusion from that. An arbitrary small change of the parameters of the static congruence turns it into a contracting or expanding member, so the congruence is unstable with respect to its scale, and the ring expands without bound instead of remaining at radius $a$. He infers that the Kerr–Schild metric built on the congruence is likely unstable in the same way, and he conjectures a continuous transition in which a naked ring singularity, contracting, acquires a horizon and becomes a rotating black hole, and then, expanding, throws the horizon off again. That is stated as a conjecture, to be settled by an exact solution of the Einstein–Maxwell equations, and the source says so.

Two consequences follow for this article, and they are the reason the section exists. The first is a **qualification of the ring's radius**: the free constant $\varrho$ is the $v=0$ value of a function of time, so a fixed radius is a property of the static configuration and not of the construction as a whole. The second is a **qualification of the electron reading**, which the source states himself: if a small deformation of the static congruence lets the ring expand indefinitely, then the identification of the ring with a particle of fixed size is not stable within the model, and the successes of the static member — the finite difference of the two divergent energies, the Dirac value of the gyromagnetic ratio, the quadrupole prediction — belong to that member.

### What the Section Changes and What It Does Not

It does not change the preceding sections. They treat the member $v=0$, and their results — the ring, the branch disk, the complex field with its mesomagnetic component, and the vanishing Hamiltonian function — are statements about that member. The self-energy calculation in particular is a computation in the stationary field, and the stationary field is exactly the case $v=0$.

Nor is anything here a result of the biquaternion framework. The field is a solution of the linear Maxwell equations obtained by a complex boost of the Coulomb field, the congruence belongs to the external programme, and the instability and the ring-to-black-hole transition are the source's argument and conjecture. The section's one structural point for the corpus is the identification it makes visible: the displacement of the singularity along the informational axis and the radius of the ring in the material sector are **one parameter read in two sectors**, related by the factor $1/\sqrt{1+v^2}$ that the null-cone condition supplies. When the displacement passes through zero, the ring in the material sector shrinks to a point.

## The Self-Energy: the Difference That Vanishes

### The Hamilton Function in the Stationary Field

Lanczos's reason for the construction is the self-energy. In the stationary field the density of the action integrand — his **Hamiltonian function** — is the difference of the electric and the magnetic energy densities. For a point electron the field is purely electric, and the self-energy integral of the Coulomb field diverges at the position of the charge: the energy of a point charge is infinite in the classical theory. For the circle electron the field is complex and carries the second, mesomagnetic component, and Lanczos finds that **the electric energy still diverges, but the mesomagnetic energy diverges in the opposite direction and cancels it**, so that the difference of the two tends to zero. The Hamiltonian function of the circle electron is therefore not necessarily infinite. This is the statement that the divergence of the point-charge self-energy is not forced by the field theory, but is a property of the point idealisation; moving the singularity into $\mathbb{B}_{\Psi}$ removes it.

The electric and the mesomagnetic energies are each divergent at the ring, and the claim is about their difference. Lanczos computes the difference by a limiting procedure. Because of the symmetry about the third axis he works in the plane $r_y=0$ and multiplies by $2\pi\varrho$; he integrates over the disk "above and below" from the radius $\varrho-\varepsilon$ inward — that part contributes nothing, the product of the potential and the field strength being regular there — and then over a small torus of radius $\varepsilon$ threaded on the ring,

$$
\rho = \varrho + \varepsilon\cos\theta_{\mathrm{azm}}, \qquad r_z = \varepsilon\sin\theta_{\mathrm{azm}} ,
$$

where $\rho=\sqrt{r_x^2+r_y^2}$ and $\theta_{\mathrm{azm}}$ is the azimuth, and lets $\varepsilon\to0$. The Hamiltonian function of the ring is then

$$
H = \frac{2\pi\varrho}{\varepsilon}\int_0^{2\pi} \frac{\varepsilon+\varrho\,(\cos\theta_{\mathrm{azm}}+i\sin\theta_{\mathrm{azm}})}{\bigl[\varepsilon+2\varrho\,(\cos\theta_{\mathrm{azm}}+i\sin\theta_{\mathrm{azm}})\bigr]^2}\,d\theta_{\mathrm{azm}}
$$

### The Vanishing of the Integral

The integral vanishes, and it vanishes for every $\varepsilon$ in the range $0<\varepsilon<2\varrho$ in which it is taken. The reason is elementary and is worth recording because it is the whole content of the self-energy claim. Setting $u=\exp(i\theta_{\mathrm{azm}})$ turns the integral into a contour integral over the unit circle,

$$
\int_0^{2\pi}\frac{\varepsilon+\varrho \exp(i\theta_{\mathrm{azm}})}{\bigl[\varepsilon+2\varrho \exp(i\theta_{\mathrm{azm}})\bigr]^2}\,d\theta_{\mathrm{azm}}
= \frac{1}{i}\oint \frac{\varepsilon+\varrho u}{u\,(\varepsilon+2\varrho u)^2}\,du ,
$$

whose integrand has a simple pole at $u=0$ and a double pole at $u=-\varepsilon/2\varrho$. For $\varepsilon<2\varrho$ both lie inside the contour. The residues are $+1/\varepsilon$ at $u=0$ and $-1/\varepsilon$ at $u=-\varepsilon/2\varrho$, and they cancel exactly, so the contour integral, and with it $H$, is zero. The cancellation of the two residues is the exact echo, at the level of the integral, of the cancellation of the electric and mesomagnetic energies at the level of the field: one divergent term and one oppositely divergent term, in the ratio that makes their difference finite, and in fact zero. The result has been recomputed here directly from the formula, by summing the integrand over a hundred equally spaced values of $\theta_{\mathrm{azm}}$ for several $\varepsilon$ and $\varrho$: the integral is zero to machine precision, at the $10^{-16}$ level, in every case tried.

Two qualifications belong with the result. The vanishing is the statement of Lanczos's model at the level of the stationary field; it is not a derivation that the physical electron has zero electromagnetic mass. And the cancellation is exact only because the electric and mesomagnetic contributions are computed from the same complex potential, so that their divergences are tied together; a deformation of the model that breaks the complex structure — for instance a real deformation of the ring — would spoil it. The corpus records the result as the source's, with the formula, and does not promote it into a framework result.

### Relation to the Finite-Mass Programme

The circle electron is the static, singularity-side member of the family of constructions by which the Lanczos line confronts the self-energy divergence. The later programme of Gsponer and Hurni works on the **retarded** singularity and derives the standard action of electrodynamics from Lanczos's, finding a finite electromagnetic mass for a boundary tube of finite retarded radius; that result is recorded in *Radiation from Accelerated Charges in Biquaternionic Form*, together with its own limits. The two share the same structural move — the divergence is not assumed but traced to the idealisation — and differ in what is deformed: the retarded radius there, the position of the singularity here. Neither is the Abraham–Lorentz extended electron, and neither is a result of the corpus's own framework.

## Relation to the Algebrodynamical Ring

The corpus records other ring-shaped electrons, and they must be kept apart.

| | Circle electron (Lanczos, 1919) | Algebrodynamical ring | Ring in imaginary motion (Kassandrov) |
|---|---|---|---|
| Equation | linear vacuum Maxwell, $\tilde\nabla_\Phi\tilde{F}=0$ | nonlinear primary Cauchy–Riemann system | linear vacuum Maxwell, field read off a shear-free null congruence |
| Ring arises from | complex displacement of a point singularity into $\mathbb{B}_{\Psi}$ | self-dual solution of the nonlinear system | caustic of the complex null cone of a charge moving along the informational axis |
| Radius | free, equal to the imaginary displacement $\varrho$ | fixed by the equation, the admissible family $R_n$ | free and time-dependent, $\lvert vr'_t-a\rvert/\sqrt{1+v^2}$, collapsing at $r'_t=a/v$ |
| Charge | arbitrary | self-quantised, minimal value $|ϙ|=\tfrac14$ | fixed at the elementary value, independent of $v$ and $r'_t$ |
| Gravity | none | Kerr–Newman metric, $g=2$ | Kerr–Schild deformation, conjectural; $g=2$ and $\mu=ea$ only in the static member $v=0$ |

The shift of a singularity by a constant imaginary amount, $r_z\mapsto r_z+i\lambda$, is one device with three uses, and what distinguishes them is the status of $\lambda$: in the Kerr ring it is fixed by the source's angular momentum, $\lambda=a=J/(Mc)$; in the algebrodynamical ring it is fixed only by requiring the Dirac moment, $\lvert\lambda\rvert=\lvert  a\rvert=\frac{\hbar}{2\,c\,M}$; and in Lanczos's construction it is free, $\lambda=\varrho$, the length of a displacement into $\mathbb{B}_{\Psi}$. The Kerr member is the same kernel and not merely the same device: in the oblate coordinates of the Kerr–Newman solution $(r+ia\cos\theta)^2=r_x^2+r_y^2+(r_z+ia)^2$, so that Lanczos's shifted distance is $r+ia\cos\theta$ itself, its squared modulus is $\Sigma=r^2+a^2\cos^2\theta$, and the Kerr singular ring $r=\cos\theta=0$ is the circle electron at $\varrho=a$ (Burinskii, arXiv:1212.5595, sec. 2). **The congruence is tangent to the ring, and on it the null vector reduces to $k=dt-a\,d\theta_{\mathrm{azm}}$.** The auxiliary metric restricted to the $(t,\theta_{\mathrm{azm}})$ plane of the ring is $dt^2-a^2d\theta_{\mathrm{azm}}{}^2$, so the direction $\partial/\partial h_t+a^{-1}\partial/\partial\theta_{\mathrm{azm}}$ is lightlike, and the ring is traversed along it at the speed of light. The singular locus of the congruence is therefore its own null locus: a **closed lightlike curve**, not a spatial circle on which the field merely diverges.

The third column is the same ring as the first, seen at a different member of a family, and it is not a new model: its field is the complex boost of the Coulomb field, and its equation is linear. What it adds is the time dependence, and with it the caveat recorded in *The Instability* above.

Both are classical models in which the electron is a ring rather than a point, and both are recorded in the corpus as external programmes rather than as results. The decisive difference is the equation. Lanczos's ring lives on the **linear** Cauchy–Riemann equation, where the complex displacement is a symmetry of the equation and the ring is its image; the algebrodynamical ring lives on a **nonlinear, over-determined** primary equation, where the ring, the quantised charge and the induced metric are consequences of the nonlinearity. The linear ring has a free radius and no quantisation; the nonlinear ring has a fixed radius, a quantised charge and a metric. The corpus's linear framework reaches the first and is silent on the second, which is the boundary the algebrodynamical article states.

## Summary

Lanczos's circle electron is the displacement of a point singularity of the vacuum field off the material subspace $\mathbb{B}_{\Phi}$ and into the informational sector $\mathbb{B}_{\Psi}$. With the displacement $\Delta\tilde{Q}=-i\varrho \vec e_z$, the singular set of the displaced Coulomb potential $Ξ=1/\sqrt{r_x^2+r_y^2+(r_z+i\varrho)^2}$ is the ring $\Gamma: r_z=0$, $r_x^2+r_y^2=\varrho^2$, of radius equal to the magnitude of the imaginary displacement; the disk it bounds is a branch locus, not a second singularity, and the point electron is the limit $\varrho\to0$. The field of the ring is complex, carrying a second component that is polar under space reflection and that Gsponer and Hurni call mesomagnetic; it is appreciable only near the ring, and the far field is the point field.

The construction's purpose is the self-energy. In the stationary field the Hamiltonian function is the difference of the electric and the mesomagnetic energies; each diverges at the ring, and their difference does not. Lanczos's limiting integral over a small torus threaded on the ring vanishes, and the vanishing is the exact cancellation of the two residues of an elementary contour integral, $+1/\varepsilon$ at $u=0$ and $-1/\varepsilon$ at $u=-\varepsilon/2\varrho$. The result is a claim of the source's, checked here by direct quadrature to machine precision and recorded with the later retarded-radii programme of Gsponer and Hurni as the two sides of the same structural move. The corpus's own linear framework reaches the construction and does not endorse its **physical interpretation**; the ring on the nonlinear algebrodynamical equation is a different object, on a different equation, with different consequences.

The ring is also the static member of a family. Kassandrov's congruence construction displaces the singularity along the informational axis at a constant rate, $z_0(r'_t)=-ia+i\,vr'_t$, and the caustic is a ring of radius $\varrho(r'_t)=\lvert vr'_t-a\rvert/\sqrt{1+v^2}$ that collapses to a point at $r'_t=a/v$ and re-expands at the speed $v/\sqrt{1+v^2}$ in the units of the check, which is below $c$ for every finite $v$. The static circle electron is the member $v=0$, and the deformation leaves the charge fixed while the magnetic moment tracks the current radius. The construction is recorded for one structural reason — the displacement and the radius are one parameter read in two sectors, related by the null-cone factor $1/\sqrt{1+v^2}$ — and for one caveat, which the source states: the static congruence is unstable under small deformation, so the fixed radius, the Dirac gyromagnetic ratio and the quadrupole prediction are properties of the static member. The ring-to-black-hole transition the source conjectures from that instability is not a result. Throughout, the field is a solution of the linear Maxwell equations.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Ξ$ | Scalar potential; the displaced Coulomb potential $1/\sqrt{r_x^2+r_y^2+(r_z+i\varrho)^2}$, up to the charge factor |
| $\vec r_0 = -i\varrho \vec e_z$ | Position of the singularity, displaced into the informational sector |
| $\Delta\tilde{Q} = -i\varrho \vec e_z$ | The displacement itself; an element of $\mathbb{B}_{\Psi}$ with $h'_{z}=-\varrho$ |
| $\varrho$ | Magnitude of the imaginary displacement; radius of the circle electron |
| $r_*=r+i\varrho\cos\theta$ | Displaced distance in the oblate spheroidal coordinates $(r,\theta)$ of the Kerr solution, $r_*^2=r_x^2+r_y^2+(r_z+i\varrho)^2$; its two signs are Kerr's two sheets |
| $\lambda$ | Length of a constant imaginary shift $r_z\mapsto r_z+i\lambda$; $a=J/(Mc)$ for the Kerr ring, $\lvert  a\rvert=\frac{\hbar}{2\,c\,M}$ in the algebrodynamical ring, $\varrho$ here |
| $\Gamma$ | Singular set: the ring $r_z=0$, $r_x^2+r_y^2=\varrho^2$ |
| $D$ | Branch disk $r_z=0$, $r_x^2+r_y^2<\varrho^2$, where the square root changes sign |
| $\rho=\sqrt{r_x^2+r_y^2}$ | Cylindrical radius, used in the torus parametrisation |
| $\theta_{\mathrm{azm}}$ | Azimuth on the torus threaded on the ring |
| $\rho=\varrho+\varepsilon\cos\theta_{\mathrm{azm}},\ r_z=\varepsilon\sin\theta_{\mathrm{azm}}$ | Small torus threaded on the ring; the integration surface |
| $\varepsilon$ | Radius of the torus threaded on the ring (Lanczos's $\epsilon$, renamed to avoid the permittivity) |
| $H$ | Hamiltonian function (action density) of the ring; the difference of electric and mesomagnetic energy |
| $\vec E = -\mathrm{grad}\,Ξ$ | Complexified electric field of the displaced configuration; real part electric, imaginary part mesomagnetic |
| $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$ | Material and informational sectors |
| $z_0(r'_t)=-ia+ivr'_t$ | Complex world line of the virtual charge; a displacement $a-vr'_t$ along the informational axis |
| $v$ | Parameter of the complex world line (the paper's "imaginary velocity"); not a speed |
| $\varrho(r'_t)=\lvert vr'_t-a\rvert/\sqrt{1+v^2}$ | Radius of the ring in imaginary motion; collapses at $r'_t=a/v$ |
| $V=v/\sqrt{1+v^2}$ | Speed of the contracting or expanding ring, in the units of the check; below $c$ for every finite $v$ |
| $\sigma=(r'_t+av)/(1+v^2)$ | Complex retarded time on the caustic |
| $r_b^2=(r_z-r_{0z})^2+\rho^2(1+v^2)$ | Complex distance; its branch locus is the ring |
| $\tilde ϙ=ϙ(1+v^2)$ | Charge factor of the field in imaginary motion |
| $\epsilon$ | Permittivity of the medium (Coulomb factor only) |

## Further Reading

- Cornelius Lanczos, *The Functional Theoretical Relationships of the Maxwell Aether Equations* (doctoral dissertation, Budapest, handwritten 1919; English typescript arXiv:physics/0408079), Chapter 7, *Das Kreiselektron*, for the displaced potential, the ring, the branch disk, and the vanishing Hamiltonian function of the ring.
- V. V. Kassandrov, "A non-stationary generalization of the Kerr congruence", arXiv:0908.1123 [gr-qc] (2009), for the ring in imaginary motion: the complex world line $z_0(r'_t)=-ia+ivr'_t$, the caustic radius $\lvert vr'_t-a\rvert/\sqrt{1+v^2}$, the field of the congruence with its fixed elementary charge and variable magnetic moment, the instability argument, and the conjectured naked-ring–black-hole transition.
- Alexander Burinskii, "Kerr-Newman electron as spinning soliton," arXiv:1410.2888 [physics.gen-ph] (2014), for the same ring read in gravity: the spinning particle is over-rotating, its horizon is absent, and the naked Kerr singular ring of radius $a=J/(mc)$ — half the reduced Compton wavelength when $J=\frac{\hbar}{2}$ — is regularised by a bubble whose interior is flat. This is where the free radius $\varrho$ of the sections above acquires a value, and the value is the one the Zitterbewegung amplitude already gives. The construction is general-relativistic and contains no biquaternion algebra; it is the gravitational counterpart of the ring, not a second model of it. Its sequel, "Stability of the lepton bag model based on the Kerr–Newman solution," arXiv:1706.02979, gives the flat-inside, Kerr–Newman-outside split a stability argument: with three chiral superfields added, the bubble is a BPS-saturated soliton whose boundary, fixed by a first-order equation, sits at $r=R=e^2/2m$, a ratio $R/a=\alpha$ to the ring radius.
- Alexander Burinskii, "What tells Gravity on the shape and size of an electron," arXiv:1212.2920 [physics.gen-ph] (2012), SPIN2012 talk, the earlier and more explicit statement of the construction above: the matching condition $H=0$, which puts the bubble wall at $r=e^2/2m$ and shapes the source as an oblate bubble of radius $a$ and thickness $2r_e=e^2/m$; the Higgs winding on the rim, $\xi_{,\mu}+e\alpha_\mu=0$, whose loop integral $2\pi n=-4\pi J$ returns $\lvert J\rvert=n/2$; the interior phase oscillating at $\dot\xi=2m$; and the null-circle property of the ring used in *Relation to the Algebrodynamical Ring*. Recorded for those statements only: it is a general-relativistic construction with no biquaternion algebra, and its numerical details belong to the Kerr–Newman model, not to the framework.
- H. Bateman, *The Mathematical Analysis of Electrical and Optical Wave-Motion* (Cambridge University Press, 1915; Dover reprint 1955), for the result that the singularities of a solution of the complex eikonal equation lie on a surface propagating more slowly than light, which is what bounds the ring's speed $V$ below $c$.
- Alexander Burinskii, "New Path to Unification of Gravity with Particle Physics," arXiv:1701.01025 [physics.gen-ph] (2016), for the oblate spheroidal coordinates of the Kerr–Newman solution, $r_x+ir_y=(r+ia)e^{i\theta_{\mathrm{azm}}}\sin\theta$ and $r_z=r\cos\theta$, whose radial coordinate $r+ia\cos\theta$ is the displaced distance of this article, and for the explicit treatment of the $r<0$ sheet, reached through the ring at $r=0$; the two sheets are the two determinations of the square root. Only that coordinate reading is taken from it. Its own construction is the supersymmetric form of the bag already recorded above, and it carries no element of the algebra.
- [Radiation from Accelerated Charges in Biquaternionic Form](radiation-from-accelerated-charges-in-biquaternionic-form.html), and the sources there, for the retarded-radii programme in which the standard action is derived from Lanczos's and the electromagnetic mass is finite for a boundary tube of finite retarded radius.
- [The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry](the-algebrodynamical-programme-nonlinear-cauchy-riemann-conditions-self-quantized-charge-and-induced-causal-geometry.html), for the second ring, on a nonlinear primary equation, with its self-quantised charge and its Kerr–Newman metric.
- [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html), for the interpretation of the vacuum equation as a four-dimensional Cauchy–Riemann condition and for the stationary limit whose Coulomb kernel is the starting point here.
- E. T. Newman, "Maxwell's equations and ideal null coordinates" and the complex-Minkowski-space literature, for the modern use of a complex shift of a real singularity; the construction above is the same displacement read as a map from a point to a ring rather than as a coordinate change.
