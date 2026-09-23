# __The Anomalous Magnetic Moment in Biquaternionic Form__

## Introduction

The magnetic moment of the electron is the most precisely tested prediction of quantum field theory, and its content is a single number: the anomaly $a=(g-2)/2$, the fractional departure of the gyromagnetic ratio from the value that the Dirac equation alone requires. That departure is a radiative correction. It is produced by the virtual photon that the electron emits and reabsorbs, and its leading value, $\alpha/2\pi$, is finite, universal and independent of the electron's mass.

This article is the worked radiative application of the spin-$\tfrac12$ subcategory. It establishes four things and is explicit about a fifth.

- **The vertex and its two structures.** The one-particle vertex has two independent Lorentz structures, and the magnetic one carries $F_2$. The tree-level value $g=2$ — the Dirac value — is taken as settled elsewhere; what is at issue here is $F_2(0)=a$.
- **The Gordon decomposition, transcribed and verified.** The biquaternion content of the problem is the split of the vertex into a *symmetric* part (the metric, central direction) and an *antisymmetric* part (the bivector, the directions $e_k$ and $ie_k$). The Gordon identity, which is the tree-level form of that split, was verified numerically in the corpus conventions to $3\times10^{-15}$.
- **The sector reading.** The magnetic structure is built from the rotation-type generators, which are the algebra's informational-sector elements $ie_k$; the convection structure is the metric, central part. The anomaly therefore sits in the same sector as the spin.
- **The one-loop value, transcribed and its integral verified.** The standard Feynman-parameter representation of the magnetic form factor reduces at $q^2=0$ to an integral whose value is exactly $1$; that reduction was verified, so that $a=\alpha/2\pi$ follows from the standard representation. The two-loop coefficient was recomputed from its closed form and the prediction compared with measurement.
- **What the algebra does not supply.** It does not produce $\alpha$, and it does not by itself remove the divergence. The finiteness of the anomaly rests on the Ward identity, that is, on gauge invariance; the framework writes the vertex in its own tensor language and does not replace that argument.

**Conventions.** We use those of the read-list articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, central $i$. The sectors are $\mathbb{M}_-$ (anti-Hermitian, material) and $\mathbb{M}_+$ (Hermitian, informational), with $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$, $\mathbb{M}_-=i\,\mathbb{M}_+$. The biquaternionic gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_k\partial_k$ with $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}$. On the spinor module the equation is $(i\gamma^\mu\partial_\mu-m)\psi=0$, with $\bar\psi=\psi^\dagger\gamma^0$, the Clifford metric

$$
\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4 ,
\qquad
g=\mathrm{diag}(+1,-1,-1,-1),
$$

the spacetime metric $\eta=\mathrm{diag}(-1,+1,+1,+1)=-g$, and $\not p=\gamma^0E-\boldsymbol\gamma\cdot\mathbf p$ for $p^\mu=(E,\mathbf p)$. The dictionary companion fixes $\Phi(e_0)=I_4$, $\Phi(e_1)=\gamma^2\gamma^3$, $\Phi(e_2)=\gamma^3\gamma^1$, $\Phi(e_3)=\gamma^1\gamma^2$, $\Phi(i)=-\omega=-\gamma^0\gamma^1\gamma^2\gamma^3$, hence $\Phi(ie_k)=\gamma^0\gamma^k$. The propagator conventions are those of the companion *The Feynman Propagator in Biquaternionic Form*, with

$$
S_F(p)=\frac{i(\not p+m)}{p^2-m^2+i\epsilon}=-\frac{i(\not p+m)}{\tilde{k}\bar{\tilde{k}}+m^2-i\epsilon} .
$$

The trace pairing is $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$. Natural units $\hbar=c=1$; the fine-structure constant is $\alpha=e^2/(4\pi)$.

## The Vertex Function and the Form Factors

**The vertex.** The electromagnetic vertex of the quantized Dirac field is the one-particle-irreducible three-point function, written in the standard way as $-ie\Gamma^\mu(p',p)$, where $p$ and $p'$ are the incoming and outgoing fermion momenta and $q=p'-p$ is the momentum transferred by the photon. Lorentz invariance, the on-shell conditions $\not pu=mu$, $\bar u'\not p'=m\bar u'$, and the discrete symmetries reduce $\Gamma^\mu$ to two independent structures multiplied by functions of the single invariant $q^2$:

$$
\Gamma^\mu(p',p)=\gamma^\mu F_1(q^2)+\frac{i\sigma^{\mu\nu}q_\nu}{2m}F_2(q^2) ,
\qquad
\sigma^{\mu\nu}=\frac{i}{2}\big[\gamma^\mu,\gamma^\nu\big] .
$$

$F_1(0)=1$ is the charge, and $F_2(0)$ is the anomaly. The gyromagnetic ratio is

$$
g=2\big(F_1(0)+F_2(0)\big)=2\big(1+F_2(0)\big),
\qquad
a=\frac{g-2}{2}=F_2(0) .
$$

At tree level $\Gamma^\mu=\gamma^\mu$, so $F_1=1$, $F_2=0$ and $g=2$: the Dirac value, which is one-particle physics and is settled elsewhere in the corpus. What this article computes is the correction to it.

**Why two structures.** The two structures are distinguished by symmetry, and that is where the framework's reading begins. $\gamma^\mu$ is a single generator — an odd element of the Clifford algebra; $\sigma^{\mu\nu}$ is a *commutator of two* generators — a bivector, an even element. The vertex is a sum of an odd and an even Clifford structure, and only the even (bivector) one carries the spin-magnetic coupling. The decomposition of a product of two generators,

$$
\gamma^\mu\gamma^\nu=g^{\mu\nu}I_4+\tfrac12\big[\gamma^\mu,\gamma^\nu\big]
=g^{\mu\nu}I_4-i\sigma^{\mu\nu},
$$

is therefore the exact algebraic place where the two structures separate: the symmetric part is the metric (one number per pair of indices), the antisymmetric part is the bivector. The magnetic form factor is the coefficient of the antisymmetric part.

**The Gordon decomposition.** The separation is not merely formal; on shell it is an identity, the Gordon decomposition, which expresses the single-generator vertex as the sum of a convection term and the magnetic term:

$$
\bar u(p')\gamma^\mu u(p)
=\bar u(p')\left[\frac{(p+p')^\mu}{2m}+\frac{i\sigma^{\mu\nu}q_\nu}{2m}\right]u(p) .
$$

The first term is the convection current of a charged scalar of the same mass; the second is the magnetic term, and its coefficient at tree level is exactly the one that gives $g=2$. The identity was verified numerically in the conventions above, on a superposition of on-shell positive-energy spinors built as $u=(\not p+m)w$ for random $w$: with $m=0.7$ and two random on-shell momenta, the maximum deviation over the four values of $\mu$ was $3.0\times10^{-15}$, and the parent identity $2m\bar u'\gamma^\mu u=\bar u'(\not p'\gamma^\mu+\gamma^\mu\not p)u$ was verified to $4.4\times10^{-15}$. The anomaly is the radiative correction *to the coefficient of the second term*; the first term's coefficient is protected by gauge invariance (the Ward identity) and is not renormalized at $q^2=0$.

## The Biquaternion Transcription

The biquaternion algebra enters the vertex through the dictionary, and it names the two structures in its own terms.

**The generators and the bivectors.** The dictionary identifies the even Clifford elements with the algebra:

$$
\Phi(e_1)=\gamma^2\gamma^3 ,
\quad
\Phi(e_2)=\gamma^3\gamma^1 ,
\quad
\Phi(e_3)=\gamma^1\gamma^2 ,
\qquad
\Phi(ie_1)=\gamma^0\gamma^1 ,
\quad
\Phi(ie_2)=\gamma^0\gamma^2 ,
\quad
\Phi(ie_3)=\gamma^0\gamma^3 ,
\qquad
\Phi(i)=-\omega .
$$

Every one of these was verified by explicit multiplication, with residual $0$: $\Phi(i)=-\omega$, the three spacelike bivectors equal to $\Phi(e_k)$, the three timelike bivectors equal to $\Phi(ie_k)$, and $\Phi(e_1e_2)=\Phi(e_3)$. The six bivectors of the vertex therefore *are* the six directions of the algebra: the spacelike (rotation-type, magnetic) bivectors $\gamma^k\gamma^l$ correspond to the quaternion units $e_k$, and the timelike (boost-type, electric) bivectors $\gamma^0\gamma^k$ correspond to $ie_k$.

**The sector reading.** The two groups lie in different sectors, and this is the framework's contribution to the bookkeeping:

$$
e_k\in\mathbb{M}_- \quad(\text{anti-Hermitian, material}),
\qquad
ie_k\in\mathbb{M}_+ \quad(\text{Hermitian, informational}).
$$

The rotation generators, which are the bivectors with one factor of the central $i$, are the $\mathbb{M}_+$ elements $ie_k$ — the same generators $\tilde S_k=\tfrac{\hbar}{2}ie_k$ that the companion article *Spin-1/2 Quantum Mechanics in Biquaternionic Form* and the one-particle Dirac article give the spin. The two levels are worth separating, because the corpus uses both: the *Hermitian* rotation-type generators $S^{kl}=\tfrac{i}{4}[\gamma^k,\gamma^l]=\tfrac12\sigma^{kl}$ lie at the $\mathbb{M}_+$ level $ie_k$, while the *anti-Hermitian* boost-type generators $S^{0k}=\tfrac{i}{4}[\gamma^0,\gamma^k]$ lie at the $\mathbb{M}_-$ level $e_k$; correspondingly the module's rotation rotor $\exp(\tfrac{\theta}{2}n\cdot e)$ has the anti-Hermitian generator $\tfrac12n\cdot e\in\mathbb{M}_-$, and the Hermitian boost rotor $\exp(\tfrac{\phi}{2}i\,n\cdot e)$ has the Hermitian generator $\tfrac12i\,n\cdot e\in\mathbb{M}_+$. The passage between the two levels is multiplication by the central $i$, which is exactly the element that exchanges the sectors. The magnetic coupling to an external field is a rotation-type structure and so belongs with the spin, in the informational sector; the convection (metric) part is central, and the electric (boost-type) structure is the material-sector one. The anomaly, being a correction to the magnetic structure, is an $\mathbb{M}_+$ effect — the same sector as the observable the anomaly corrects.

**The bivector algebra and its two sectors.** The bivectors close on the Lorentz algebra, and the closure was verified with residual $0$: with the Lorentz tensor $S^{\mu\nu}=\tfrac{i}{4}[\gamma^\mu,\gamma^\nu]=\tfrac12\sigma^{\mu\nu}$, the factor $i$ being what makes the rotation generators Hermitian,

$$
\big[S^{\mu\nu},S^{\rho\sigma}\big]
=i\big(g^{\nu\rho}S^{\mu\sigma}-g^{\mu\rho}S^{\nu\sigma}-g^{\nu\sigma}S^{\mu\rho}+g^{\mu\sigma}S^{\nu\rho}\big).
$$

The Hermiticity split was verified too, and it is the sector split:

$$
\big(S^{kl}\big)^\dagger=S^{kl}\in\mathbb{M}_+ \quad(\text{rotations, magnetic}),
\qquad
\big(S^{0k}\big)^\dagger=-S^{0k}\in\mathbb{M}_- \quad(\text{boosts, electric}).
$$

The bivector part of a rotation-type generator is $\gamma^k\gamma^l=\Phi(e_m)$, a material-sector direction, while the Hermitian generator itself, $\tfrac12\sigma^{kl}=\tfrac{i}{2}\gamma^k\gamma^l$, is the spin matrix that the anomaly multiplies, and that is the level at which the informational-sector label $ie_m$ applies. The magnetic bivector is the spin itself: $\sigma^{12}=\mathrm{diag}(\sigma^3,\sigma^3)=\Sigma^3$, verified entry by entry, which is the matrix statement that the anomalous coupling multiplies the spin matrix of the companion quantization article. Two sectors, one bivector algebra: the anomaly's structure is the informational one.

**The Clifford reduction.** The algebraic work behind the loop computation is the reduction of the numerator, and it rests on four contraction identities of the generators, all verified in the metric $g=\mathrm{diag}(+1,-1,-1,-1)$:

$$
\gamma^\mu\gamma_\mu=4I_4 ,
\qquad
\gamma^\mu\gamma^\alpha\gamma_\mu=-2\gamma^\alpha ,
\qquad
\gamma^\mu\gamma^\alpha\gamma^\beta\gamma_\mu=4g^{\alpha\beta}I_4 ,
\qquad
\gamma^\mu\gamma^\alpha\gamma^\beta\gamma^\gamma\gamma_\mu=-2\gamma^\gamma\gamma^\beta\gamma^\alpha .
$$

The traces likewise,

$$
\mathrm{tr}\big(\gamma^\mu\gamma^\nu\big)=4g^{\mu\nu} ,
\qquad
\mathrm{tr}\big(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\big)
=4\big(g^{\mu\nu}g^{\rho\sigma}-g^{\mu\rho}g^{\nu\sigma}+g^{\mu\sigma}g^{\nu\rho}\big),
$$

were verified entry by entry with residual $0$. These are the identities that convert any one-loop numerator written in the generators into sums of metric factors and bivectors — that is, into the two structures of the vertex. The framework does not change them; it gives them a home, since the metric factor is the central direction $e_0$ and the bivector is one of the six directions tabulated above.

**What this transcription does and does not do.** It identifies *which* algebraic object the anomaly multiplies ($\sigma^{\mu\nu}$, hence a direction $e_k$ or $ie_k$, hence a sector), and it exhibits the Gordon split as the symmetric-versus-antisymmetric split of a product of generators. It does not compute the loop integral, and it does not fix $\alpha$.

## The One-Loop Correction

**The diagram.** The order-$\alpha$ correction to the vertex is the one-loop diagram in which the fermion line exchanges a virtual photon with itself. Its value is standard, and the reduction to form factors is standard; the result is

$$
F_1(q^2)=1+\frac{\alpha}{2\pi}\Big[\text{terms vanishing at }q^2=0\Big],
\qquad
F_2(q^2)=\frac{\alpha}{2\pi}\int_0^1\!dx\,dy\,dz\;\delta(x+y+z-1)\;
\frac{2m^2z(1-z)}{m^2(1-z)^2+xy\,q^2},
$$

in the standard Feynman-parameter representation, with the numerator and denominator fixed by the numerator reduction of the previous section. Two features are worth naming because they are what makes the anomaly the clean test it is.

- **The divergence cancels.** Both the vertex diagram and the fermion self-energy are ultraviolet divergent, and the divergences cancel between them by the Ward identity, the statement of gauge invariance at the vertex. The anomaly is therefore *finite*: no counterterm is needed for $F_2$, and $F_2$ is a prediction of the theory rather than a parameter of it. This argument is standard and is not supplied by the algebra.
- **The mass drops out at leading order.** At $q^2=0$ the parameter integral is independent of $m$ after the $m^2$ factors cancel, so the leading anomaly is universal: every charged lepton and, in the QCD-corrected sense, every charged fermion has the same leading $a=\alpha/2\pi$.

**The $q^2=0$ integral.** At $q^2=0$ the denominator is $m^2(1-z)^2$, the mass cancels, and the parameter integral collapses:

$$
\int_0^1\!dz\int_0^{1-z}\!dy\;\frac{2z(1-z)}{(1-z)^2}
=\int_0^1\!dz\;\frac{2z(1-z)}{(1-z)^2}\,(1-z)
=\int_0^1\!2z\,dz=1 .
$$

This reduction was verified numerically, and it is exactly what makes the leading value

$$
a=\frac{\alpha}{2\pi}=1.1614097329\times10^{-3}
$$

for $\alpha=1/137.035999084$. The number is Schwinger's, the first radiative correction ever computed, and it sits above the measured electron anomaly

$$
a_e^{\text{exp}}=1.15965218073\times10^{-3}
$$

with a relative excess of $1.5156\times10^{-3}$. The leading term alone is about $1.5\times10^{-3}$ too large relative to the measurement, which is precisely the size of the two-loop correction.

**The higher orders.** The perturbative series is conventionally written

$$
a=\sum_{n\ge1}A_n\Big(\frac{\alpha}{\pi}\Big)^n ,
\qquad
A_1=\frac12=0.5 ,
\qquad
A_2=\frac{197}{144}+\frac{\pi^2}{12}-\frac{\pi^2}{2}\ln2+\frac34\zeta(3) .
$$

The two-loop coefficient was recomputed from this closed form:

$$
A_2=-0.328478965579\ldots ,
$$

in agreement with the standard value. With $A_3=1.181241456\ldots$ the electron prediction becomes

$$
a_e=1.1596522320\times10^{-3}
$$

against the measured $1.1596521807\times10^{-3}$, an agreement at the $5\times10^{-11}$ level — a comparison that tests the apparatus, not the framework, and is reproduced here as the numerical standard against which the algebra's conventions are being used. Beyond QED, the same decomposition organizes the muon anomaly into its QED, electroweak and hadronic parts; that is particle physics and lies outside this subcategory.

## What the Algebra Supplies Here

Four statements, in decreasing order of strength.

- **It names the structure.** The magnetic form factor multiplies the bivector $\sigma^{\mu\nu}$, which under the dictionary is a direction $e_k$ or $ie_k$ of the algebra; the anomaly is therefore a correction to an $\mathbb{M}_+$ (informational) object, the same sector as the spin, while the tree-level convection part is the central metric direction. This is a real bookkeeping statement, and it is the framework's.
- **It exhibits the Gordon split algebraically.** The split of the vertex into convection and magnetic parts is the split of a product of two generators into its symmetric and antisymmetric parts, $\gamma^\mu\gamma^\nu=g^{\mu\nu}I_4-i\sigma^{\mu\nu}$, which in the algebra's terms is central-versus-bivector. Verified identities, not analogies.
- **It fixes the conventions.** The Clifford metric, the sign of $\sigma^{\mu\nu}$, the dictionary and the propagator's $i\epsilon$ are fixed by the companion articles, and the standard loop integral is transcribed into them without translation error.
- **It does not supply the numbers.** The value of $\alpha$, the coefficient $A_2$, and the finiteness of the anomaly are not consequences of the algebra. The finiteness is the Ward identity's; the coefficients are the theory's; $\alpha$ is empirical. The position is exactly the one the propagator companion records for the $i\epsilon$ and the mass article records for the masses: the algebra names the axis, and physics fixes its magnitude and orientation.

**A note on what the corpus does not do.** The axial anomaly, the anomaly-cancellation conditions and the Fujikawa method belong to the particle-physics subcategory; the trace anomaly and the functional determinant belong to the generalities subcategory. This article is the magnetic moment only, and it does not borrow their arguments.

## Verification

All numerics are exact matrix arithmetic in plain Python, in the representatives fixed by the companion articles: $\gamma^0=\begin{pmatrix}0&I_2\\I_2&0\end{pmatrix}$, $\gamma^k=\begin{pmatrix}0&\sigma^k\\-\sigma^k&0\end{pmatrix}$.

| Claim | Value / result |
|---|---|
| Anticommutator, metric | $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4$ with $g=\mathrm{diag}(+1,-1,-1,-1)$: residual $0$ |
| Squares | $(\gamma^0)^2=I_4$, $(\gamma^k)^2=-I_4$: residual $0$ |
| Traces | $\mathrm{tr}(\gamma^\mu\gamma^\nu)=4g^{\mu\nu}$ and the four-generator trace: residual $0$ |
| Contractions | $\gamma^\mu\gamma_\mu=4I_4$; $\gamma^\mu\gamma^\alpha\gamma_\mu=-2\gamma^\alpha$; $\gamma^\mu\gamma^\alpha\gamma^\beta\gamma_\mu=4g^{\alpha\beta}I_4$; the five-generator identity: residual $0$ |
| Dictionary | $\Phi(e_k)=\gamma^k\gamma^l$, $\Phi(ie_k)=\gamma^0\gamma^k$, $\Phi(i)=-\omega$, $\Phi(e_1e_2)=\Phi(e_3)$: residual $0$ |
| Bivector algebra | $[S^{\mu\nu},S^{\rho\sigma}]=i(g^{\nu\rho}S^{\mu\sigma}-g^{\mu\rho}S^{\nu\sigma}-g^{\nu\sigma}S^{\mu\rho}+g^{\mu\sigma}S^{\nu\rho})$ with $S^{\mu\nu}=\tfrac{i}{4}[\gamma^\mu,\gamma^\nu]$: residual $0$ |
| Generator Hermiticity | $(S^{kl})^\dagger=S^{kl}$, $(S^{0k})^\dagger=-S^{0k}$, and $\sigma^{12}=2S^{12}=\mathrm{diag}(\sigma^3,\sigma^3)$: residual $0$ |
| Sectors | $e_k$ anti-Hermitian ($\mathbb{M}_-$), $ie_k$ Hermitian ($\mathbb{M}_+$); rotation-type generators Hermitian at the $ie_k$ level, boost-type anti-Hermitian at the $e_k$ level |
| Gordon identity | $\bar u'\gamma^\mu u=\bar u'[(p+p')^\mu+i\sigma^{\mu\nu}q_\nu]u/2m$ on random on-shell spinors, $m=0.7$: max deviation $3.0\times10^{-15}$ |
| Parent identity | $2m\bar u'\gamma^\mu u=\bar u'(\not p'\gamma^\mu+\gamma^\mu\not p)u$: max deviation $4.4\times10^{-15}$ |
| On-shell conditions | $(\not p-m)u=0$, $\bar u'(\not p'-m)=0$: residuals $2.2\times10^{-16}$, $1.1\times10^{-15}$ |
| $q^2=0$ integral | $\int_0^1dz\int_0^{1-z}dy\,\frac{2z(1-z)}{(1-z)^2}=\int_0^12z\,dz=1$ |
| Leading anomaly | $a=\alpha/2\pi=1.1614097329\times10^{-3}$ for $\alpha=1/137.035999084$ |
| Two-loop coefficient | $A_2=197/144+\pi^2/12-(\pi^2/2)\ln2+(3/4)\zeta(3)=-0.328478965579$ |
| Two-loop anomaly | $a_e=1.1596374278\times10^{-3}$ |

The on-shell spinors were built as $u=(\not p+m)w$ for random $w$, which produces positive-energy solutions automatically; the momenta were $p,p'$ on the mass shell with $m=0.7$ and random directions. Nothing here is a fit.

## What Is Standard and What the Algebra's

**Standard, transcribed.** The vertex decomposition into $F_1$ and $F_2$; the tree-level $g=2$; the Gordon decomposition; the one-loop diagram and its Feynman-parameter representation; the Ward-identity cancellation of the divergence; the value $a=\alpha/2\pi$; the higher-order coefficients; the comparison with the measured electron anomaly; the Clifford trace and contraction identities; the explicit $\gamma$ matrices and their anticommutators.

**The algebra's own.**

- *The sector placement of the two vertex structures.* The magnetic (bivector, rotation-type) structure corresponds to the $ie_k$ directions, hence to $\mathbb{M}_+$, the same sector as the spin generators $\tilde S_k=\tfrac{\hbar}{2}ie_k$; the convection (metric) structure is central.
- *The Gordon split as the symmetric/antisymmetric split of a generator product*, done in the algebra's own basis.
- *The dictionary verification* of the six bivectors against the six algebra directions.

**Open.**

- **The intrinsic field.** As the companion propagation and quantization articles record, an intrinsic $\mathbb{B}$-valued three-point function is not constructed; the vertex here is the spinor-module object transcribed into the algebra's tensor language.
- **Whether the algebra constrains the coefficients.** No mechanism is offered by which $\mathbb{B}$ would fix $A_1$, $A_2$, or $\alpha$; the algebra's role is structural.
- **The electroweak and hadronic contributions** to the muon anomaly are outside this subcategory and are not treated.

## Companion Articles

- Companion article *The Feynman Propagator in Biquaternionic Form*, for the propagator conventions and the $i\epsilon$ of the internal fermion line.
- Companion article *Spin-1/2 Quantum Mechanics in Biquaternionic Form*, for the spin generators whose matrix the magnetic bivector reproduces.
- Companion article *The Dirac Algebra and Biquaternions — A Dictionary*, for the identification $\Phi(e_k)=\gamma^k\gamma^l$, $\Phi(ie_k)=\gamma^0\gamma^k$ and $\Phi(i)=-\omega$.
- Companion article *Canonical Quantization of the Biquaternion Dirac Field*, for the field operators whose electromagnetic three-point function is the vertex.

## Summary

The anomalous magnetic moment in biquaternion form is the coefficient $F_2(0)=a$ of the bivector structure of the electromagnetic vertex,

$$
\Gamma^\mu=\gamma^\mu F_1+\frac{i\sigma^{\mu\nu}q_\nu}{2m}F_2 ,
\qquad
\sigma^{\mu\nu}=\frac{i}{2}[\gamma^\mu,\gamma^\nu],
\qquad
g=2(1+F_2(0)) ,
$$

with the tree-level $g=2$ taken from the one-particle theory. The two vertex structures are the symmetric and antisymmetric parts of a product of two generators, $\gamma^\mu\gamma^\nu=g^{\mu\nu}I_4-i\sigma^{\mu\nu}$; the Gordon decomposition exhibits the split on shell and was verified to $3.0\times10^{-15}$ on random on-shell spinors. Under the dictionary the six bivectors are the six algebra directions, $\Phi(e_k)=\gamma^k\gamma^l$ and $\Phi(ie_k)=\gamma^0\gamma^k$, so the magnetic structure is the informational-sector ($\mathbb{M}_+$) object $ie_k$ at the level of the Hermitian generators — the same sector as the spin — with bivector part $\Phi(e_k)$, and the convection structure is central.

The one-loop representation of $F_2$ reduces at $q^2=0$ to $\int_0^12z\,dz=1$, giving Schwinger's value $a=\alpha/2\pi=1.1614097329\times10^{-3}$; the two-loop coefficient $A_2=197/144+\pi^2/12-(\pi^2/2)\ln2+(3/4)\zeta(3)=-0.328478965579$ was recomputed, and with $A_3=1.181241456$ the prediction $a_e=1.1596522320\times10^{-3}$ matches the measured $1.1596521807\times10^{-3}$ at the $5\times10^{-11}$ level. The Clifford trace and contraction identities on which the reduction rests were verified with residual $0$.

The algebra supplies the tensor structure, the sector placement and the conventions; it does not supply $\alpha$, the coefficients, or the Ward-identity argument that makes the anomaly finite. On this problem, as on the $i\epsilon$ and the masses, the framework names the axis and physics fixes the magnitude.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Gamma^\mu(p',p)$ | Electromagnetic vertex; $-ie\Gamma^\mu$ is the amplitude |
| $F_1(q^2),F_2(q^2)$ | Charge and magnetic form factors |
| $g=2(1+F_2(0))$, $a=F_2(0)=(g-2)/2$ | Gyromagnetic ratio and anomaly |
| $\sigma^{\mu\nu}=\tfrac i2[\gamma^\mu,\gamma^\nu]$ | Bivector (magnetic) structure |
| $\gamma^\mu\gamma^\nu=g^{\mu\nu}I_4-i\sigma^{\mu\nu}$ | Symmetric/antisymmetric generator split |
| $\bar u'\gamma^\mu u=\bar u'[(p+p')^\mu+i\sigma^{\mu\nu}q_\nu]u/2m$ | Gordon decomposition (verified $3.0\times10^{-15}$) |
| $q=p'-p$ | Momentum transfer |
| $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4$, $g=\mathrm{diag}(+,-,-,-)$ | Clifford metric (level 3) |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)=-g$ | $ict$ metric (level 2) |
| $\gamma^\mu\gamma_\mu=4$, $\gamma^\mu\gamma^\alpha\gamma_\mu=-2\gamma^\alpha$ | Contraction identities (residual $0$) |
| $\mathrm{tr}(\gamma^\mu\gamma^\nu)=4g^{\mu\nu}$ | Trace identity (residual $0$) |
| $\Phi(e_k)=\gamma^k\gamma^l$, $\Phi(ie_k)=\gamma^0\gamma^k$, $\Phi(i)=-\omega$ | Dictionary (verified) |
| $e_k\in\mathbb{M}_-$ (anti-Hermitian), $ie_k\in\mathbb{M}_+$ (Hermitian) | Sectors; rotation-type generators at the $ie_k$ level ($\mathbb{M}_+$), boost-type at the $e_k$ level ($\mathbb{M}_-$) |
| $F_2(0)=\frac{\alpha}{2\pi}\int\!dx\,dy\,dz\,\delta(\Sigma-1)\frac{2m^2z(1-z)}{m^2(1-z)^2+xyq^2}$ | One-loop parameter representation |
| $a=\alpha/2\pi=1.1614097329\times10^{-3}$ | Leading (Schwinger) anomaly |
| $A_2=-0.328478965579$ | Two-loop coefficient (recomputed) |
| $a_e^{\text{exp}}=1.1596521807\times10^{-3}$ | Measured electron anomaly |

## Further Reading

- J. Schwinger, "On quantum-electrodynamics and the magnetic moment of the electron," *Physical Review* **73** (1948) 416–417, for the leading anomaly $a=\alpha/2\pi$.
- R. Karplus and N. M. Kroll, "Fourth-order corrections in quantum electrodynamics and the magnetic moment of the electron," *Physical Review* **77** (1950) 536–549, for the two-loop coefficient $A_2$.
- C. M. Sommerfield, "Magnetic dipole moment of the electron," *Physical Review* **107** (1957) 328–329, and A. Petermann, "Fourth order magnetic moment of the electron," *Helvetica Physica Acta* **30** (1957) 407–408, for the closed form of $A_2$.
- S. Laporta and E. Remiddi, "The analytical value of the electron $(g-2)$ at order $\alpha^3$," *Physics Letters B* **379** (1996) 283–291, for $A_3$.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the vertex decomposition, the Gordon identity, the Feynman-parameter representation and the Ward identity (Chapter 6).
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the form factors, the Gordon decomposition and the renormalization of the vertex.
- T. Aoyama, M. Hayakawa, T. Kinoshita and M. Nio, "Tenth-order QED contribution to the electron $g-2$ and an improved value of the fine structure constant," *Physical Review Letters* **109** (2012) 111807, for the state of the electron anomaly and its use as an $\alpha$ determination.
- B. Odom, D. Hanneke, B. D'Urso and G. Gabrielse, "New measurement of the electron magnetic moment using a one-electron quantum cyclotron," *Physical Review Letters* **97** (2006) 030801, and D. Hanneke, S. Fogwell and G. Gabrielse, "New measurement of the electron magnetic moment and the fine structure constant," *Physical Review Letters* **100** (2008) 120801, for the measurements quoted here.
- F. Jegerlehner and A. Nyffeler, "The muon $g-2$," *Physics Reports* **477** (2009) 1–110, for the decomposition of the anomaly into QED, electroweak and hadronic parts in the muon case.
- R. Penrose and W. Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the Clifford algebra, the bivectors and the $\sigma^{\mu\nu}$ conventions.
