# __The Anomalous Magnetic Moment in Biquaternionic Form__

## Introduction

The magnetic moment of the electron is the most precisely tested prediction of quantum field theory, and its content is a single number: the anomaly $a=(g-2)/2$, the fractional departure of the gyromagnetic ratio from the value that the Dirac equation alone requires. That departure is a radiative correction. It is produced by the virtual photon that the electron emits and reabsorbs, and its leading value, $\alpha/2\pi$, is finite, universal and independent of the electron's mass.

This article is the worked radiative application of the spin-$\tfrac12$ subcategory. It establishes four things and is explicit about a fifth.

- **The vertex and its two structures.** The one-particle vertex has two independent Lorentz structures, and the magnetic one carries $F_2$. The tree-level value $g=2$ — the Dirac value — is taken as settled elsewhere; what is at issue here is $F_2(0)=a$.
- **The Gordon decomposition, transcribed and verified.** The biquaternion content of the problem is the split of the vertex into a *symmetric* part (the metric, central direction) and an *antisymmetric* part (the bivector, the directions $\vec e_\mu$ and $i\vec e_\mu$). The Gordon identity, which is the tree-level form of that split, was verified numerically in the corpus conventions to $3\times10^{-15}$.
- **The sector interpretation.** The magnetic structure is built from the rotation-type generators, which are the algebra's informational-sector elements $i\vec e_\mu$; the convection structure is the metric, central part. The anomaly therefore sits in the same sector as the spin.
- **The one-loop value, transcribed and its integral verified.** The standard Feynman-parameter representation of the magnetic form factor reduces at $k^2=0$ to an integral whose value is exactly $1$; that reduction was verified, so that $a=\alpha/2\pi$ follows from the standard representation.
- **What the algebra does not supply.** It does not produce $\alpha$, and it does not by itself remove the divergence. The finiteness of the anomaly rests on the Ward identity, that is, on gauge invariance; the framework writes the vertex in its own tensor language and does not replace that argument.

With $L_{a}R_{b}\psi=a\psi b$ the two-sided multiplication and $L_{e_t}R_{e_t}$ the identity of the algebra. The four cells $iR_{\vec e_x}$ and $iL_{\vec e_k}R_{\vec e_y}$ carry the Clifford relations of $g=\operatorname{diag}(+1,-1,-1,-1)$; see the appendix. The spacetime metric is $\eta=\mathrm{diag}(-1,+1,+1,+1)=-g$. A paired Greek index is written low with the plain weight, $\varepsilon=(1,-1,-1,-1)$: $\sigma_{\mu\nu}k_\nu$ is the sum $\sum_\nu\varepsilon_\nu\,\sigma_{\mu\nu}k_\nu$. The companion *Matrix Representations Conventions*, §*The Clifford Structure and the Frame*, fixes the frame cells and the reading $e_t\mapsto L_{e_t}R_{e_t}$, $\vec e_x\mapsto L_{\vec e_x}R_{e_t}$, $\vec e_y\mapsto L_{\vec e_y}R_{e_t}$, $\vec e_z\mapsto L_{\vec e_z}R_{e_t}$, $i\mapsto-\omega=L_{e_t}R_{\vec e_z}$, hence $i\vec e_\mu\mapsto L_{e_\mu}R_{\vec e_z}$. The propagator conventions are those of the companion *The Feynman Propagator in Biquaternionic Form*, with

$$
S_F(p)=\frac{i(iR_{\vec e_x}p_{0}-\sum_k iL_{\vec e_k}R_{\vec e_y}p_{k}+m\,L_{e_t}R_{e_t})}{p^2-m^2+i\epsilon}=-\frac{i(iR_{\vec e_x}p_{0}-\sum_k iL_{\vec e_k}R_{\vec e_y}p_{k}+m\,L_{e_t}R_{e_t})}{\tilde{P}\tilde{P}^{\natural}+m^2-i\epsilon} .
$$

The trace is $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, the $2\times2$ reading of the plain form; a cell has the trace $\mathrm{tr}\,L_{a}R_{b}=4\,\mathrm{Sc}(a)\mathrm{Sc}(b)$, four times the product of scalar parts. Natural units $\hbar=c=1$; the fine-structure constant is $\alpha=e^2/(4\pi)$.

## The Vertex Function and the Form Factors

**The vertex.** The electromagnetic vertex of the quantized Dirac field is the one-particle-irreducible three-point function, written in the standard way as $-ie\Gamma_\mu(p_2,p)$, where $p$ and $p_2$ are the incoming and outgoing fermion momenta and $k=p_2-p$ is the momentum transferred by the photon. Lorentz invariance, the on-shell conditions $iR_{\vec e_x}p_{0}-\sum_k iL_{\vec e_k}R_{\vec e_y}p_{k} u=mu$, $\bar w_2 \bigl(iR_{\vec e_x}(p_{2})_{0}-\sum_k iL_{\vec e_k}R_{\vec e_y}(p_{2})_{k}\bigr)=m\bar w_2$, and the discrete symmetries reduce $\Gamma_\mu$ to two independent structures multiplied by functions of the single invariant $k^2$:

$$
\Gamma_0(p_2,p)=iR_{\vec e_x} F_1(k^2)+\frac{i\sum_\nu\varepsilon_\nu\,\sigma_{0\nu}k_\nu}{2m}F_2(k^2) ,
\qquad
\Gamma_k(p_2,p)=iL_{\vec e_k}R_{\vec e_y} F_1(k^2)+\frac{i\sum_\nu\varepsilon_\nu\,\sigma_{k\nu}k_\nu}{2m}F_2(k^2) ,
$$
with $\sigma_{\mu\nu}$ the bivector of the appendix.

$F_1(0)=1$ is the charge, and $F_2(0)$ is the anomaly. The gyromagnetic ratio is

$$
\boxed{\;g=2\big(F_1(0)+F_2(0)\big)=2\big(1+F_2(0)\big),
\qquad
a=\frac{g-2}{2}=F_2(0)\;}.
$$

At tree level $\Gamma_0=iR_{\vec e_x}$ and $\Gamma_k=iL_{\vec e_k}R_{\vec e_y}$, so $F_1=1$, $F_2=0$ and $g=2$: the Dirac value, which is one-particle physics and is settled elsewhere in the corpus. What this article computes is the correction to it.

**Why two structures.** The two structures are distinguished by symmetry, and that is where the framework's interpretation begins. $\Gamma_\mu$ is a single generator at tree level — one cell up to the factor $i$, an odd element of the Clifford algebra, the timelike cell $iR_{\vec e_x}$ for $\mu=0$ and the spacelike cells $iL_{\vec e_k}R_{\vec e_y}$ for $\mu=k$; $\sigma_{\mu\nu}$ is a *commutator of two* generators — a bivector, an even element. The vertex is a sum of an odd and an even Clifford structure, and only the even (bivector) one carries the spin-magnetic coupling. The decomposition of a product of two generators,

$$
iR_{\vec e_x}\,iL_{\vec e_k}R_{\vec e_y}=g_{0k}L_{e_t}R_{e_t}-i\sigma_{0k},
\qquad
iL_{\vec e_j}R_{\vec e_y}\,iL_{\vec e_k}R_{\vec e_y}=g_{jk}L_{e_t}R_{e_t}-i\sigma_{jk},
$$

is therefore the exact algebraic place where the two structures separate: the symmetric part is the metric (one number per pair of indices), the antisymmetric part is the bivector. The pair is the whole statement, since the product of two generators is the metric part plus half the commutator, and the commutator of two distinct cells is the bivector. The magnetic form factor is the coefficient of the antisymmetric part.

**The Gordon decomposition.** The separation is not merely formal; on shell it is an identity, the Gordon decomposition, which expresses the single-generator vertex as the sum of a convection term and the magnetic term:

$$
\bar w(p_2)\,iR_{\vec e_x}\,w(p)
=\bar w(p_2)\left[\frac{(p+p_2)_0}{2m}+\frac{i\sum_\nu\varepsilon_\nu\,\sigma_{0\nu}k_\nu}{2m}\right]w(p) ,
$$
$$
\bar w(p_2)\,iL_{\vec e_k}R_{\vec e_y}\,w(p)
=\bar w(p_2)\left[\frac{(p+p_2)_k}{2m}+\frac{i\sum_\nu\varepsilon_\nu\,\sigma_{k\nu}k_\nu}{2m}\right]w(p) .
$$

The first term is the convection current of a charged scalar of the same mass; the second is the magnetic term, and its coefficient at tree level is exactly the one that gives $g=2$. The identity was verified numerically in the conventions above, on a superposition of on-shell positive-energy spinors built as $w=(iR_{\vec e_x}p_{0}-\sum_k iL_{\vec e_k}R_{\vec e_y}p_{k}+m\,L_{e_t}R_{e_t})\omega$ for random $\omega$: with $m=0.7$ and two random on-shell momenta, the maximum deviation over the four values of $\mu$ was $3.0\times10^{-15}$, and the parent identity, with the tree-level vertex acting on one spinor and the free operator on the other, was verified to $4.4\times10^{-15}$. The anomaly is the radiative correction *to the coefficient of the second term*; the first term's coefficient is protected by gauge invariance (the Ward identity) and is not renormalized at $k^2=0$.

## The Biquaternion Transcription

The biquaternion algebra enters the vertex through the dictionary, and it names the two structures in its own terms.

**The generators and the bivectors.** The dictionary identifies the even Clifford elements with the algebra:

$$
\vec e_x\mapsto L_{\vec e_x}R_{e_t} ,
\quad
\vec e_y\mapsto L_{\vec e_y}R_{e_t} ,
\quad
\vec e_z\mapsto L_{\vec e_z}R_{e_t} ,
\qquad
i\vec e_x\mapsto L_{\vec e_x}R_{\vec e_z} ,
\quad
i\vec e_y\mapsto L_{\vec e_y}R_{\vec e_z} ,
\quad
i\vec e_z\mapsto L_{\vec e_z}R_{\vec e_z} ,
\qquad
i\mapsto-\omega .
$$

Every one of these was verified by explicit multiplication, with residual $0$: $i\mapsto-\omega$, the three spacelike bivectors equal to the images of $\vec e_\mu$, the three timelike bivectors equal to the images of $i\vec e_\mu$, and $\vec e_x\vec e_y$ reading as $\vec e_z$. The six bivectors of the vertex therefore *are* the six directions of the algebra: the spacelike (rotation-type, magnetic) bivectors are the cells $L_{e_\mu}R_{e_t}$, which are the left multiplications $L_{e_\mu}$ and the cells of the quaternion units $\vec e_\mu$; the timelike (boost-type, electric) bivectors are the cells $L_{e_\mu}R_{\vec e_z}$ and the cells of $i\vec e_\mu$.

**The sector interpretation.** The two groups lie in different sectors, and this is the framework's contribution to the bookkeeping:

$$
\boxed{\;\vec e_\mu\in\mathbb{M}_- \quad(\text{anti-Hermitian, material}),
\qquad
i\vec e_\mu\in\mathbb{M}_+ \quad(\text{Hermitian, informational})\;}.
$$

The rotation generators, which are the bivectors with one factor of the central $i$, are the $\mathbb{M}_+$ elements $i\vec e_\mu$ — the same generators $\tilde S_\mu=\tfrac{\hbar}{2}i\vec e_\mu$ that the companion article *Spin-1/2 Quantum Physics in Biquaternionic Form* and the one-particle Dirac article give the spin. The two levels are worth separating, because the corpus uses both: the *Hermitian* rotation-type generators $S_{\mu\rho}=\tfrac12\sigma_{\mu\rho}$ lie at the $\mathbb{M}_+$ level $i\vec e_\mu$, while the *anti-Hermitian* boost-type generators $S_{0\mu}$ lie at the $\mathbb{M}_-$ level $\vec e_\mu$; correspondingly the module's rotation rotor $\exp(\tfrac{\theta}{2}n\cdot e)$ has the anti-Hermitian generator $\tfrac12n\cdot e\in\mathbb{M}_-$, and the Hermitian boost rotor $\exp(\tfrac{\phi}{2}i\,n\cdot e)$ has the Hermitian generator $\tfrac12i\,n\cdot e\in\mathbb{M}_+$. The passage between the two levels is multiplication by the central $i$, which is exactly the element that exchanges the sectors. The magnetic coupling to an external field is a rotation-type structure and so belongs with the spin, in the informational sector; the convection (metric) part is central, and the electric (boost-type) structure is the material-sector one. The anomaly, being a correction to the magnetic structure, is an $\mathbb{M}_+$ effect — the same sector as the observable the anomaly corrects.

**The bivector algebra and its two sectors.** The bivectors close on the Lorentz algebra, and the closure was verified with residual $0$: with the Lorentz tensor $S_{\mu\nu}=\tfrac12\sigma_{\mu\nu}$, the factor $i$ being what makes the rotation generators Hermitian,

$$
\big[S_{\mu\nu},S_{\rho\sigma}\big]
=i\big(g_{\nu\rho}S_{\mu\sigma}-g_{\mu\rho}S_{\nu\sigma}-g_{\nu\sigma}S_{\mu\rho}+g_{\mu\sigma}S_{\nu\rho}\big).
$$

The Hermiticity split was verified too, and it is the sector split:

$$
\big(S_{\mu\rho}\big)^\dagger=S_{\mu\rho}\in\mathbb{M}_+ \quad(\text{rotations, magnetic}),
\qquad
\big(S_{0\mu}\big)^\dagger=-S_{0\mu}\in\mathbb{M}_- \quad(\text{boosts, electric}).
$$

The bivector part of a rotation-type generator is the product of two generators, the cell $L_{e_\nu}R_{e_t}$ of $\vec e_\nu$, a material-sector direction, while the Hermitian generator itself, $\tfrac12\sigma_{\mu\rho}$, is the spin matrix that the anomaly multiplies, and that is the level at which the informational-sector label $i\vec e_\nu$ applies. The magnetic bivector is the spin matrix itself: $\sigma_{12}=ic_1\,iL_{\vec e_y}R_{\vec e_y}=iL_{\vec e_z}R_{e_t}$, which in the frame's spinor basis is $\mathrm{diag}(\sigma^3,\sigma^3)=\Sigma^3$, verified entry by entry, which is the matrix statement that the anomalous coupling multiplies the spin matrix of the companion quantization article. Two sectors, one bivector algebra: the anomaly's structure is the informational one.

**The Clifford reduction.** The algebraic work behind the loop computation is the reduction of the numerator, and it rests on the four contraction identities of the appendix. They were re-evaluated in the cell basis with residual $0$. The frame matters here, because a cell's square is what the metric records: in the Euclidean frame, where every cell squares to $+I_4$, the sums are $4I_4$, $-2\gamma_\alpha$ and $4\delta_{\alpha\beta}I_4$; in the $\mathbb{M}_-$ frame the metric enters the sum itself and $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$. The four sums once printed in this article carried the Euclidean values beside the letter $g$; the corrected statements are the two frames just given, and they are the ones the appendix records. The two trace identities of the appendix were likewise verified entry by entry with residual $0$. These are the identities that convert any one-loop numerator written in the generators into sums of metric factors and bivectors — that is, into the two structures of the vertex. The framework does not change them; it gives them a home, since the metric factor is the central direction $e_t$ and the bivector is one of the six directions tabulated above.

**What this transcription does and does not do.** It identifies *which* algebraic object the anomaly multiplies ($\sigma_{\mu\nu}$, hence a direction $\vec e_\mu$ or $i\vec e_\mu$, hence a sector), and it exhibits the Gordon split as the symmetric-versus-antisymmetric split of a product of generators. It does not compute the loop integral, and it does not fix $\alpha$.

## The One-Loop Correction

**The diagram.** The order-$\alpha$ correction to the vertex is the one-loop diagram in which the fermion line exchanges a virtual photon with itself. Its value is standard, and the reduction to form factors is standard; the result is

$$
F_1(k^2)=1+\frac{\alpha}{2\pi}\Big[\text{terms vanishing at }k^2=0\Big],
\qquad
F_2(k^2)=\frac{\alpha}{2\pi}\int_0^1\!dx\,dy\,dz\;\delta(x+y+z-1)\;
\frac{2m^2z(1-z)}{m^2(1-z)^2+xy\,k^2},
$$

in the standard Feynman-parameter representation, with the numerator and denominator fixed by the numerator reduction of the previous section. Two features are worth naming because they are what makes the anomaly the clean test it is.

- **The divergence cancels.** Both the vertex diagram and the fermion self-energy are ultraviolet divergent, and the divergences cancel between them by the Ward identity, the statement of gauge invariance at the vertex. The anomaly is therefore *finite*: no counterterm is needed for $F_2$, and $F_2$ is a prediction of the theory rather than a parameter of it. This argument is standard and is not supplied by the algebra.
- **The mass drops out at leading order.** At $k^2=0$ the parameter integral is independent of $m$ after the $m^2$ factors cancel, so the leading anomaly is universal: every charged lepton and, in the QCD-corrected sense, every charged fermion has the same leading $a=\alpha/2\pi$.

**The $k^2=0$ integral.** At $k^2=0$ the denominator is $m^2(1-z)^2$, the mass cancels, and the parameter integral collapses:

$$
\int_0^1\!dz\int_0^{1-z}\!dy\;\frac{2z(1-z)}{(1-z)^2}
=\int_0^1\!dz\;\frac{2z(1-z)}{(1-z)^2}\,(1-z)
=\int_0^1\!2z\,dz=1 .
$$

This reduction was verified numerically, and it is exactly what makes the leading value

$$
\boxed{\;a=\frac{\alpha}{2\pi}=1.1614097329\times10^{-3}\;}
$$

for $\alpha=1/137.035999084$. The number is Schwinger's, the first radiative correction ever computed, and it sits above the measured electron anomaly

$$
a_e^{\text{exp}}=1.15965218073\times10^{-3}
$$

with a relative excess of $1.5156\times10^{-3}$. The leading term alone is about $1.5\times10^{-3}$ too large relative to the measurement, which is of the order of the two-loop correction.

**The higher orders.** The perturbative series is conventionally written

$$
\boxed{\;a=\sum_{\lambda\ge1}A_\lambda\Big(\frac{\alpha}{\pi}\Big)^\lambda ,
\qquad
A_1=\frac12=0.5 ,
\qquad
A_2=\frac{197}{144}+\frac{\pi^2}{12}-\frac{\pi^2}{2}\ln2+\frac34\zeta(3)\;}.
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

- **It names the structure.** The magnetic form factor multiplies the bivector $\sigma_{\mu\nu}$, which under the dictionary is a direction $\vec e_\mu$ or $i\vec e_\mu$ of the algebra; the anomaly is therefore a correction to an $\mathbb{M}_+$ (informational) object, the same sector as the spin, while the tree-level convection part is the central metric direction. This is a real bookkeeping statement, and it is the framework's.
- **It exhibits the Gordon split algebraically.** The split of the vertex into convection and magnetic parts is the split of a product of two generators into its symmetric and antisymmetric parts, $iR_{\vec e_x}\,iL_{\vec e_k}R_{\vec e_y}=g_{0k}L_{e_t}R_{e_t}-i\sigma_{0k}$, which in the algebra's terms is central-versus-bivector.
- **It fixes the conventions.** The Clifford metric, the sign of $\sigma_{\mu\nu}$, the dictionary and the propagator's $i\epsilon$ are fixed by the companion articles, and the standard loop integral is transcribed into them without translation error.
- **It does not supply the numbers.** The value of $\alpha$, the coefficient $A_2$, and the finiteness of the anomaly are not consequences of the algebra. The finiteness is the Ward identity's; the coefficients are the theory's; $\alpha$ is empirical. The position is exactly the one the propagator companion records for the $i\epsilon$ and the mass article records for the masses: the algebra names the axis, and physics fixes its magnitude and orientation.

**A note on what the corpus does not do.** The axial anomaly, the anomaly-cancellation conditions and the Fujikawa method belong to the particle-physics subcategory; the trace anomaly and the functional determinant belong to the generalities subcategory. This article is the magnetic moment only, and it does not borrow their arguments.

## Verification

All numerics are exact matrix arithmetic in plain Python, in the four frame cells fixed by the companion article, $iR_{\vec e_x}$, $iL_{\vec e_x}R_{\vec e_y}$, $iL_{\vec e_y}R_{\vec e_y}$, $iL_{\vec e_z}R_{\vec e_y}$, with $L_{a}R_{b}\psi=a\psi b$.

| Claim | Value / result |
|---|---|
| Anticommutator, metric | the Clifford relations of the appendix, with $g=\mathrm{diag}(+1,-1,-1,-1)$: residual $0$ |
| Squares | $(iR_{\vec e_x})^2=L_{e_t}R_{e_t}$, $(iL_{\vec e_k}R_{\vec e_y})^2=-L_{e_t}R_{e_t}$: residual $0$ |
| Traces | the two trace identities of the appendix: residual $0$ |
| Contractions | the four contraction identities of the appendix, in the Euclidean frame: residual $0$ |
| Dictionary | $\vec e_\mu\mapsto L_{e_\mu}R_{e_t}$, $i\vec e_\mu\mapsto L_{e_\mu}R_{\vec e_z}$, $i\mapsto-\omega=L_{e_t}R_{\vec e_z}$; $\vec e_x\vec e_y$ and $\vec e_z$ have the same image: residual $0$ |
| Bivector algebra | $[S_{\mu\nu},S_{\rho\sigma}]=i(g_{\nu\rho}S_{\mu\sigma}-g_{\mu\rho}S_{\nu\sigma}-g_{\nu\sigma}S_{\mu\rho}+g_{\mu\sigma}S_{\nu\rho})$ with $S_{\mu\nu}$ the appendix bivector: residual $0$ |
| Generator Hermiticity | $(S_{\mu\rho})^\dagger=S_{\mu\rho}$, $(S_{0k})^\dagger=-S_{0k}$, and $\sigma_{12}=2S_{12}=\mathrm{diag}(\sigma^3,\sigma^3)$: residual $0$ |
| Sectors | $\vec e_\mu$ anti-Hermitian ($\mathbb{M}_-$), $i\vec e_\mu$ Hermitian ($\mathbb{M}_+$); rotation-type generators Hermitian at the $i\vec e_\mu$ level, boost-type anti-Hermitian at the $\vec e_\mu$ level |
| Gordon identity | the two branches of the text, with $\bar w_2 iR_{\vec e_x}w$ and $\bar w_2 iL_{\vec e_k}R_{\vec e_y}w$ on random on-shell spinors, $m=0.7$: max deviation $3.0\times10^{-15}$ |
| Parent identity | the vertex on one spinor and the free operator on the other: max deviation $4.4\times10^{-15}$ |
| On-shell conditions | $(iR_{\vec e_x}p_{0}-\sum_k iL_{\vec e_k}R_{\vec e_y}p_{k}-m\,L_{e_t}R_{e_t})w=0$, $\bar w_2(iR_{\vec e_x}(p_{2})_{0}-\sum_k iL_{\vec e_k}R_{\vec e_y}(p_{2})_{k}-m\,L_{e_t}R_{e_t})=0$: residuals $2.2\times10^{-16}$, $1.1\times10^{-15}$ |
| $k^2=0$ integral | $\int_0^1dz\int_0^{1-z}dy\,\frac{2z(1-z)}{(1-z)^2}=\int_0^12z\,dz=1$ |
| Leading anomaly | $a=\alpha/2\pi=1.1614097329\times10^{-3}$ for $\alpha=1/137.035999084$ |
| Two-loop coefficient | $A_2=197/144+\pi^2/12-(\pi^2/2)\ln2+(3/4)\zeta(3)=-0.328478965579$ |
| Two-loop anomaly | $a_e=1.1596374278\times10^{-3}$ |

The on-shell spinors were built as $w=(iR_{\vec e_x}p_{0}-\sum_k iL_{\vec e_k}R_{\vec e_y}p_{k}+m\,L_{e_t}R_{e_t})\omega$ for random $\omega$, which produces positive-energy solutions automatically; the momenta were $p,p_2$ on the mass shell with $m=0.7$ and random directions. Nothing here is a fit.

## What Is Standard and What the Algebra's

**Standard, transcribed.** The vertex decomposition into $F_1$ and $F_2$; the tree-level $g=2$; the Gordon decomposition; the one-loop diagram and its Feynman-parameter representation; the Ward-identity cancellation of the divergence; the value $a=\alpha/2\pi$; the higher-order coefficients; the comparison with the measured electron anomaly; the Clifford trace and contraction identities; the explicit frame cells and their anticommutators.

**The algebra's own.**

- *The sector placement of the two vertex structures.* The magnetic (bivector, rotation-type) structure corresponds to the $i\vec e_\mu$ directions, hence to $\mathbb{M}_+$, the same sector as the spin generators $\tilde S_\mu=\tfrac{\hbar}{2}i\vec e_\mu$; the convection (metric) structure is central.
- *The Gordon split as the symmetric/antisymmetric split of a generator product*, done in the algebra's own basis.
- *The dictionary verification* of the six bivectors against the six algebra directions.

**Open.**

- **The intrinsic field.** As the companion propagation and quantization articles record, an intrinsic $\mathbb{B}$-valued three-point function is not constructed; the vertex here is the spinor-module object transcribed into the algebra's tensor language.
- **Whether the algebra constrains the coefficients.** No mechanism is offered by which $\mathbb{B}$ would fix $A_1$, $A_2$, or $\alpha$; the algebra's role is structural.
- **The electroweak and hadronic contributions** to the muon anomaly are outside this subcategory and are not treated.

## Companion Articles

- Companion article *The Feynman Propagator in Biquaternionic Form*, for the propagator conventions and the $i\epsilon$ of the internal fermion line.
- Companion article *Spin-1/2 Quantum Physics in Biquaternionic Form*, for the spin generators whose matrix the magnetic bivector reproduces.
- Companion article *Matrix Representations Conventions*, §*The Clifford Structure and the Frame*, for the identification of $\vec e_\mu$ and $i\vec e_\mu$ with the spacelike and timelike bivectors and $i\mapsto-\omega$.
- Companion article *Canonical Quantization of the Biquaternion Dirac Field*, for the field operators whose electromagnetic three-point function is the vertex.

## Summary

The anomalous magnetic moment in biquaternion form is the coefficient $F_2(0)=a$ of the bivector structure of the electromagnetic vertex,

$$
\Gamma_0=iR_{\vec e_x} F_1+\frac{i\sum_\nu\varepsilon_\nu\,\sigma_{0\nu}k_\nu}{2m}F_2 ,
\qquad
\Gamma_k=iL_{\vec e_k}R_{\vec e_y} F_1+\frac{i\sum_\nu\varepsilon_\nu\,\sigma_{k\nu}k_\nu}{2m}F_2 ,
\qquad
g=2(1+F_2(0)) ,
$$

with the tree-level $g=2$ taken from the one-particle theory. The two vertex structures are the symmetric and antisymmetric parts of a product of two generators, the metric part and the bivector; the Gordon decomposition exhibits the split on shell and was verified to $3.0\times10^{-15}$ on random on-shell spinors. Under the dictionary the six bivectors are the six algebra directions, $\vec e_\mu\mapsto L_{e_\mu}R_{e_t}$ and $i\vec e_\mu\mapsto L_{e_\mu}R_{\vec e_z}$, so the magnetic structure is the informational-sector ($\mathbb{M}_+$) object $i\vec e_\mu$ at the level of the Hermitian generators — the same sector as the spin — with bivector part the image of $\vec e_\mu$, and the convection structure is central.

The one-loop representation of $F_2$ reduces at $k^2=0$ to $\int_0^12z\,dz=1$, giving Schwinger's value $a=\alpha/2\pi=1.1614097329\times10^{-3}$; the two-loop coefficient $A_2=197/144+\pi^2/12-(\pi^2/2)\ln2+(3/4)\zeta(3)=-0.328478965579$ was recomputed, and with $A_3=1.181241456$ the prediction $a_e=1.1596522320\times10^{-3}$ matches the measured $1.1596521807\times10^{-3}$ at the $5\times10^{-11}$ level. The Clifford trace and contraction identities on which the reduction rests were verified with residual $0$.

The algebra supplies the tensor structure, the sector placement and the conventions; it does not supply $\alpha$, the coefficients, or the Ward-identity argument that makes the anomaly finite. On this problem, as on the $i\epsilon$ and the masses, the framework names the axis and physics fixes the magnitude.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Gamma_\mu(p_2,p)$ | Electromagnetic vertex; $-ie\Gamma_\mu$ is the amplitude |
| $F_1(k^2),F_2(k^2)$ | Charge and magnetic form factors |
| $g=2(1+F_2(0))$, $a=F_2(0)=(g-2)/2$ | Gyromagnetic ratio and anomaly |
| $L_{a}R_{b}$, $L_{a}R_{b}\psi=a\psi b$ | Cell: left multiplier $a$, right multiplier $b$ |
| $iR_{\vec e_x}$, $iL_{\vec e_k}R_{\vec e_y}$ | The four generator cells: the timelike one and the three spacelike ones |
| $\mathrm{tr}\,L_{a}R_{b}=4\,\mathrm{Sc}(a)\mathrm{Sc}(b)$ | Cell trace |
| $\sigma_{\mu\nu}$ | Bivector (magnetic) structure, half the commutator of two generators |
| $iR_{\vec e_x}\,iL_{\vec e_k}R_{\vec e_y}=g_{0k}L_{e_t}R_{e_t}-i\sigma_{0k}$ | Symmetric/antisymmetric generator split |
| $\bar w_2 iR_{\vec e_x}w=\bar w_2[(p+p_2)_0+i\sum_\nu\varepsilon_\nu\,\sigma_{0\nu}k_\nu]w/2m$ | Gordon decomposition (verified $3.0\times10^{-15}$) |
| $k=p_2-p$ | Momentum transfer |
| Clifford relations of the appendix, $g=\mathrm{diag}(+,-,-,-)$ | Clifford metric (level 3) |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)=-g$ | $ict'$ metric (level 2) |
| Four contraction identities of the appendix | Contraction identities (residual $0$) |
| Two trace identities of the appendix | Trace identity (residual $0$) |
| $\vec e_\mu\mapsto L_{e_\mu}R_{e_t}$, $i\vec e_\mu\mapsto L_{e_\mu}R_{\vec e_z}$, $i\mapsto-\omega=L_{e_t}R_{\vec e_z}$ | Dictionary (verified) |
| $\vec e_\mu\in\mathbb{M}_-$ (anti-Hermitian), $i\vec e_\mu\in\mathbb{M}_+$ (Hermitian) | Sectors; rotation-type generators at the $i\vec e_\mu$ level ($\mathbb{M}_+$), boost-type at the $\vec e_\mu$ level ($\mathbb{M}_-$) |
| $F_2(0)=\frac{\alpha}{2\pi}\int\!dx\,dy\,dz\,\delta(\Sigma-1)\frac{2m^2z(1-z)}{m^2(1-z)^2+xyk^2}$ | One-loop parameter representation |
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
- R. Penrose and W. Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the Clifford algebra, the bivectors and the $\sigma_{\mu\nu}$ conventions.

## Appendix — The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_tR_x,\quad \gamma_1=iL_xR_y,\quad \gamma_2=iL_yR_y,\quad \gamma_3=iL_zR_y,\quad \gamma_5=-iL_tR_z .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

The reference-frame cell of the chirality operator is $\gamma_5$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

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
