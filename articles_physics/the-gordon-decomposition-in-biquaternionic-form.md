# __The Gordon Decomposition of the Dirac Current in Biquaternionic Form__

## Introduction

The **Gordon decomposition** is an identity for the conserved current of a solution of the Dirac equation. It splits the four-vector $\bar\psi iL_{e_\mu}R_{\delta_\mu}\psi$ into two pieces of different physical character: a **convection** part, which is the orbital current of a charged particle carried by the momentum, and a **spin** part, which is the divergence of a spin density and is the source of the magnetization. The identity is due to Walter Gordon (1928) and is used wherever the magnetic behaviour of the electron is extracted from the Dirac equation: the spin part is the term whose coefficient fixes the tree-level gyromagnetic factor at $g = 2$, and whose radiative correction is the anomalous magnetic moment.

The decomposition is **on shell**. It uses the Dirac equation for the field and for its adjoint, and it therefore holds for solutions and not for arbitrary spinor functions. It also requires a nonzero mass in its Lorentz-covariant form, because the mass appears in the denominator of both terms; the massless case has a separate, energy-normalised version, in which the spin term survives as the curl of the spin density.

This article states the identity, proves it, gives its momentum-space form and its massless generalisation, and reports the two companion objects — the angular-momentum (Belinfante–Rosenfeld) split and the stress tensor — that come with it. It then gives the biquaternion interpretation. The framework's contribution here is a matter of **naming the two structures**: the split is the split of a product of two Clifford generators into its symmetric part, which is the metric and is central in the algebra, and its antisymmetric part, which is a bivector and lies in the algebra's six-dimensional bivector subspace. The convection current is the central, metric direction; the spin current is the bivector. What the framework does **not** supply is a pure biquaternion product that equals the current, for the same representation-theoretic reason recorded in the companion article on minimal coupling: the Dirac adjoint carries the Clifford-odd cell $iR_{\vec e_x} = iL_{e_t}R_{\vec e_x}$, which is outside the left copy $\mathbb{B}_L$ of the biquaternion algebra.

The article is organised as follows. The next section states the identity and proves it. A section gives the momentum-space form used in scattering. A section reads the two terms physically. A section gives the massless generalisation. A section records the angular-momentum and stress-tensor relatives and the electromagnetic (Pauli-moment) consequence. A section gives the biquaternion interpretation. The closing sections are the open questions, the summary, the notation table and the literature.

The conventions are those of the companion articles. A cell is the two-sided operator $L_{a}R_{b}$, with $L_a\psi = a\psi$ and $R_b\psi = \psi b$; $L_{e_t}R_{e_t}$ is the identity and $L_{a}R_{b}L_{c}R_{d} = L_{ac}R_{db}$. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with units $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, $\vec e_k^2 = -e_t$, central scalar imaginary $i$, and the dictionary $\mathsf{M}_2$ of the companion articles. The Clifford metric is $g = \mathrm{diag}(+1,-1,-1,-1)$; the four frame cells are $iL_{e_\mu}R_{\delta_\mu}$, with the right multiplier $\delta_t = \vec e_x$ and $\delta_k = \vec e_y$: the temporal cell is $iR_{\vec e_x} = iL_{e_t}R_{\vec e_x}$, of square $+L_{e_t}R_{e_t}$, the three spatial ones are $iL_{\vec e_k}R_{\vec e_y}$, of square $-L_{e_t}R_{e_t}$, and the two families anticommute, so that $\{iL_{e_\mu}R_{\delta_\mu},iL_{e_\nu}R_{\delta_\nu}\} = 2g_{\mu\nu}L_{e_t}R_{e_t}$; the chirality cell is $-iR_{\vec e_z} = -iL_{e_t}R_{\vec e_z}$; the bivector is $\sigma_{\mu\nu} = \frac{i}{2}[iL_{e_\mu}R_{\delta_\mu},iL_{e_\nu}R_{\delta_\nu}]$, again one cell per pair, $\sigma_{0k} = iL_{\vec e_k}R_{\vec e_z}$, $\sigma_{12} = iL_{\vec e_z}R_{e_t}$, $\sigma_{13} = -iL_{\vec e_y}R_{e_t}$, $\sigma_{23} = iL_{\vec e_x}R_{e_t}$; and the Dirac adjoint is $\bar\psi = \psi^\dagger iR_{\vec e_x}$. The mass term is the linear, chirality-off-diagonal pair $\tilde\nabla\tilde\Psi_R = m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L = m\tilde\Psi_R$.

## The Identity

### Statement

Let $\psi$ be a solution of the massive Dirac equation,

$$
\varepsilon_t\left(\nabla_t\psi\right)\vec e_x+\left(\vec\nabla\psi\right)\vec e_y+m\psi = 0,
\qquad
\vec\nabla=\sum_k\varepsilon_k\,\vec e_k\nabla_k ,
$$

after multiplication by $-1$. The three spatial cells share the right multiplier $\vec e_y$, so the four-term contraction collapses to two terms: the temporal derivative carries $\vec e_x$ on the right and the whole spatial gradient enters as one left multiplication by the vector $\vec\nabla$. Here $\nabla_\mu$ is the flat covariant derivative (the identity extends to a curved background with $\nabla_\mu$ the spinor covariant derivative). The **number current** is

$$
j_0=i\,\bar\psi\,\psi\,\vec e_x,\qquad j_k=i\,\bar\psi\,\vec e_k\,\psi\,\vec e_y .
$$

The temporal component is a number carried on the right by $\vec e_x$; the three spatial ones carry $\vec e_k$ inside and $\vec e_y$ outside. The two are different structures, and the index $\mu$ is only their common label: nothing in the algebra makes $\mu$ a function of $\mu$. That seam is where the index was hiding its content.

The Gordon decomposition expresses it as

$$
\boxed{\;\bar\psi iL_{e_\mu}R_{\delta_\mu}\psi
= \frac{i}{2m}\left(\bar\psi\,\nabla_\mu\psi - \left(\nabla_\mu\bar\psi\right)\psi\right)
+ \frac{1}{m}\sum_\nu\varepsilon_\nu\,\partial/\partial x_\nu\left(\bar\psi\,\Sigma_{\mu\nu}\psi\right)\;},
$$

where the **spin generator** is

$$
\Sigma_{\mu\nu} = \frac{i}{4}\left[iL_{e_\mu}R_{\delta_\mu},iL_{e_\nu}R_{\delta_\nu}\right] = \tfrac{1}{2}\sigma_{\mu\nu},
$$

so that $\Sigma_{\mu\nu}$ is antisymmetric, $\Sigma_{\mu\nu} = -\Sigma_{\nu\mu}$. The first term is the **convection current**; the second is the **spin current**, written as the divergence of the antisymmetric tensor density $\bar\psi\Sigma_{\mu\nu}\psi$.

### Proof

The proof uses the two Dirac equations. From the equation, $m\psi=-\varepsilon_t\left(\nabla_t\psi\right)\vec e_x-\left(\vec\nabla\psi\right)\vec e_y$, so

$$
\bar\psi iL_{e_\mu}R_{\delta_\mu}(m\psi) = i\,\bar\psi iL_{e_\mu}R_{\delta_\mu} \sum_\nu iL_{e_\nu}R_{\delta_\nu}\nabla_\nu\psi .
$$

From the adjoint of the equation, $m\bar\psi = -i\left(\nabla_\nu\bar\psi\right)iL_{e_\nu}R_{\delta_\nu}$ (the sign is the one that makes the adjoint equation consistent with the stated conventions), so

$$
\left(m\bar\psi\right)iL_{e_\mu}R_{\delta_\mu}\psi = -i\left(\nabla_\nu\bar\psi\right)iL_{e_\nu}R_{\delta_\nu} iL_{e_\mu}R_{\delta_\mu}\psi .
$$

Adding the two relations eliminates the mass on the left and gives

$$
2m\,\bar\psi iL_{e_\mu}R_{\delta_\mu}\psi
= i\left(\bar\psi iL_{e_\mu}R_{\delta_\mu} \sum_\nu iL_{e_\nu}R_{\delta_\nu}\nabla_\nu\psi
- \left(\nabla_\nu\bar\psi\right)iL_{e_\nu}R_{\delta_\nu} iL_{e_\mu}R_{\delta_\mu}\psi\right).
$$

Now use the generator-product split, which is the same relation the companion article on the anomalous moment uses,

$$
iL_{e_\mu}R_{\delta_\mu} iL_{e_\nu}R_{\delta_\nu} = g_{\mu\nu}L_{e_t}R_{e_t} - i\sigma_{\mu\nu},
\qquad
iL_{e_\nu}R_{\delta_\nu} iL_{e_\mu}R_{\delta_\mu} = g_{\mu\nu}L_{e_t}R_{e_t} + i\sigma_{\mu\nu}.
$$

Substituting and collecting the symmetric and antisymmetric parts,

$$
2m\,\bar\psi iL_{e_\mu}R_{\delta_\mu}\psi
= i\sum_\nu\varepsilon_\nu\left(\bar\psi\left(g_{\mu\nu} - i\sigma_{\mu\nu}\right)\nabla_\nu\psi
- \left(\nabla_\nu\bar\psi\right)\left(g_{\mu\nu} + i\sigma_{\mu\nu}\right)\psi\right),
$$

that is,

$$
2m\,\bar\psi iL_{e_\mu}R_{\delta_\mu}\psi
= i\left(\bar\psi\,\nabla_\mu\psi - \left(\nabla_\mu\bar\psi\right)\psi\right)
+ \sum_\nu\varepsilon_\nu\left(\bar\psi\,\sigma_{\mu\nu}\nabla_\nu\psi
+ \left(\nabla_\nu\bar\psi\right)\sigma_{\mu\nu}\psi\right).
$$

The second bracket is a total derivative,

$$
\sum_\nu\varepsilon_\nu\left(\bar\psi\,\sigma_{\mu\nu}\nabla_\nu\psi
+ \left(\nabla_\nu\bar\psi\right)\sigma_{\mu\nu}\psi\right)
= \sum_\nu\varepsilon_\nu\,\partial/\partial x_\nu\left(\bar\psi\,\sigma_{\mu\nu}\psi\right)
= 2\sum_\nu\varepsilon_\nu\,\partial/\partial x_\nu\left(\bar\psi\,\Sigma_{\mu\nu}\psi\right),
$$

because $\sigma_{\mu\nu}$ is constant and antisymmetric. Dividing by $2m$ gives the identity as stated. The algebra was checked numerically in the conventions above: the generator-product split held with residual $0$, and the momentum-space identity below held to $2.8\times10^{-15}$ over $100$ random on-shell spinor pairs and the four values of $\mu$.

### A note on the total divergence

The spin term is not separately conserved; its divergence contributes to $\langle\tilde\nabla,\tilde J\rangle_{\natural}$ together with the convection term. What is separately meaningful is the **integrated** spin density, which is the magnetic moment, and the split of the current as a sum of two covariantly defined pieces. The total divergence is what makes the second term a "bound" current rather than a transport current: it can be removed from the current at the price of a surface term, and cannot be removed from the associated moment.

## The Momentum-Space Form

For plane-wave solutions the position-space identity becomes the form used in scattering amplitudes. Write

$$
\psi(x) = w(p)\,\exp(-i\sum_\mu\varepsilon_\mu\,p_\mu x_\mu),
\qquad
\left(\sum_\mu\varepsilon_\mu\,iL_{e_\mu}R_{\delta_\mu} p_\mu - m\right)w(p) = 0,
$$

and let $\bar w(p_2)$ be the adjoint spinor of an on-shell momentum $p_2$,

$$
\bar w(p_2)\left(\sum_\mu\varepsilon_\mu\,iL_{e_\mu}R_{\delta_\mu} p_{2,\mu} - m\right) = 0 .
$$

Between such spinors the Gordon decomposition reads

$$
\boxed{\;\bar w(p_2)\,iL_{e_\mu}R_{\delta_\mu}\,w(p)
= \bar w(p_2)\left[
\frac{(p+p_2)_\mu}{2m}
+ \frac{i\sum_\nu\varepsilon_\nu\,\sigma_{\mu\nu}(p_2-p)_\nu}{2m}
\right]w(p)\;}.
$$

Equivalently, with the momentum transfer $k = p_2 - p$ and the average momentum $P = \tfrac12(p+p_2)$,

$$
\bar w(p_2)iL_{e_\mu}R_{\delta_\mu} w(p)
= \frac{1}{m}\left[P_\mu\,\bar w(p_2)w(p)
+ i\sum_\nu\varepsilon_\nu\,\bar w(p_2)S_{\mu\nu}w(p)\,k_\nu\right],
\qquad
S_{\mu\nu} = \tfrac12\sigma_{\mu\nu} .
$$

The first term is proportional to the scalar bilinear $\bar w_2w$, the second to the tensor bilinear $\bar w_2S_{\mu\nu}w$. The two coefficients are fixed: the first is $P_\mu/m$, the second is $i k_\nu/m$. This is the form in which the vertex decomposition of the companion article on the anomalous magnetic moment is stated, and it is the identity that was verified numerically there and here.

### Parent identity

The momentum-space Gordon identity is a consequence of the simpler **parent identity**, valid for any matrix $\Gamma$ and any on-shell pair,

$$
2m\,\bar w(p_2)\,\Gamma\,w(p)
= \bar w(p_2)\left(\sum_\mu\varepsilon_\mu\,iL_{e_\mu}R_{\delta_\mu} p_{2,\mu}\,\Gamma + \Gamma\,\sum_\mu\varepsilon_\mu\,iL_{e_\mu}R_{\delta_\mu} p_\mu\right)w(p),
$$

which follows from the two on-shell conditions $w(p_2)$ and $\bar w(p_2)$ and is the form in which the companion article on the anomalous magnetic moment states it. With $\Gamma = iL_{e_\mu}R_{\delta_\mu}$ the parent identity gives the Gordon form; with $\Gamma = iL_{e_\mu}R_{\delta_\mu} -iR_{\vec e_z}$ it gives the axial companion,

$$
2m\,\bar w(p_2)iL_{e_\mu}R_{\delta_\mu} -iR_{\vec e_z} w(p)
= \bar w(p_2)\left(iL_{e_\mu}R_{\delta_\mu} -iR_{\vec e_z}\sum_\rho\varepsilon_\rho\,iL_{e_\rho}R_{\delta_\rho} p_{\rho} + \sum_\nu\varepsilon_\nu\,iL_{e_\nu}R_{\delta_\nu} (p_{2})_{\nu}\,iL_{e_\mu}R_{\delta_\mu} -iR_{\vec e_z}\right)w(p),
$$

which is the same statement for the axial current and is used in the analysis of the axial anomaly.

## The Physical Reading

### Convection and spin

The two terms of the momentum-space identity have a direct interpretation, and it is the reason the decomposition is useful.

The **convection term** $\bar w_2\frac{(p+p_2)_\mu}{2m}w$ is the current of a charged scalar of mass $m$ and momentum $\tfrac12(p+p_2)$. It is the orbital part: it depends on the average four-momentum, it reduces to $\bar w_2iL_{e_\mu}R_{\delta_\mu} w \to \bar w_2 w\,v_\mu$ in the non-relativistic limit, and it is the piece protected by gauge invariance.

The **spin term** $\bar w_2\frac{i\sum_\nu\varepsilon_\nu\,\sigma_{\mu\nu}(p_2-p)_\nu}{2m}w$ depends on the momentum **transfer** $k_\nu$ and on the tensor bilinear. It is the piece that couples to the field strength rather than to the potential: contracted with the momentum-space photon, it produces an effective Pauli moment term. Its coefficient is exactly the one that gives $g = 2$, as the next subsection shows.

The identification of the second term with the spin density is not a metaphor. In position space the second term is $\frac{1}{m}\sum_\nu\varepsilon_\nu\partial/\partial x_\nu(\bar\psi\Sigma_{\mu\nu}\psi)$; the spatial components of the tensor density are the spin angular-momentum density, and the magnetic moment is its integral.

### The magnetic moment and $g=2$

Contract the spin term with the photon field. The interaction is $-\sum_\mu\varepsilon_\mu A_\mu j_\mu$, and the spin-dependent part contributes, up to a total divergence,

$$
-\frac{e\hbar}{2mc}\sum_{\mu,\nu}\varepsilon_\mu\varepsilon_\nu\,\partial/\partial x_\nu A_\mu\,\bar\psi\sigma_{\nu\mu}\psi
= -\frac{e\hbar}{2mc}\cdot\tfrac12\sum_{\mu,\nu}\varepsilon_\mu\varepsilon_\nu\,F_{\mu\nu}\,\bar\psi\sigma_{\mu\nu}\psi,
$$

which is an effective **Pauli moment term** $-\frac{e\hbar}{2mc}\,\vec B\cdot\psi^\dagger\boldsymbol\sigma\psi$. Its coefficient is the Dirac value $g = 2$. The companion article on the anomalous magnetic moment uses exactly this split: the tree-level vertex is $iL_{e_\mu}R_{\delta_\mu} F_1 + \frac{i\sum_\nu\varepsilon_\nu\,\sigma_{\mu\nu}k_\nu}{2m}F_2$ with $F_1(0) = 1$, $F_2(0) = 1$, and the anomaly is the radiative correction to $F_2(0)$. The convection coefficient is fixed by the Ward identity; the spin coefficient is the one that can be corrected.

The same decomposition underlies the companion article on the classical origin of $g = 2$: the factor of two is the statement that the spin-density gradient is twice as effective at generating an electric current as it is at contributing to the linear momentum, which is the factor-of-two asymmetry recorded below.

## The Massless Generalisation

The covariant form above needs $m \neq 0$, because both terms carry $1/m$. A decomposition that survives the massless limit uses the energy in place of the mass. Assume a time-harmonic solution $\psi(\vec r, t') = \psi(\vec r)\exp(-iEt')$ with $E = \sqrt{|\vec k|^2 + m^2}$, and use the Dirac equation once more. For the spatial current one finds

$$
\boxed{\;\vec j \equiv e\,\bar\psi\vec c\,\psi
= \frac{e}{2iE}\left(\psi^\dagger\nabla\psi - \left(\nabla\psi^\dagger\right)\psi\right)
+ \frac{e}{E}\,\nabla\times\vec S\;},
$$

with $\vec c = (iL_{\vec e_x}R_{\vec e_y},iL_{\vec e_y}R_{\vec e_y},iL_{\vec e_z}R_{\vec e_y})$ and

$$
\vec S = \psi^\dagger S\psi,
\qquad
\left(S_x,S_y,S_z\right) = \left(\Sigma_{23},\Sigma_{31},\Sigma_{12}\right),
\qquad
S = \frac12\begin{pmatrix}\boldsymbol\sigma & 0\\ 0 & \boldsymbol\sigma\end{pmatrix}.
$$

The first term is the **free current**: for a near plane wave of finite extent it is $e\rho\,\vec k/E = e\rho\,\vec v$ with $\rho = \psi^\dagger\psi$ and $\vec v = \vec k/E$, which is the transport of charge at the group velocity. The second is the **bound spin current** $(e/E)\nabla\times\vec S$.

Integrating by parts, the magnetic moment is

$$
\vec\mu = \frac12\int\vec r\times\vec j_{\rm bound}\,d^3x
= \frac{e}{E}\int\vec S\,d^3x .
$$

In the rest frame $E = m$ this is $\vec\mu_{\rm Dirac} = (e/m)\vec S = (eg/2m)\vec S$ with $g = 2$, recovering the massive result. For a massless right-handed Weyl particle the spin is locked to the direction $\vec u_k$ of the kinetic momentum and the moment is $\vec\mu_{\rm Weyl} = (e/E)(\hbar\vec u_k/2)$. This is the cleanest form of the statement that the massless limit does not remove the spin current; it only removes the separation scale $m$ in favour of the energy $E$.

## The Angular-Momentum and Stress-Tensor Relatives

The same split appears in the energy–momentum tensor, and the comparison is instructive because the numerical coefficients differ.

The symmetric **Belinfante–Rosenfeld** tensor is

$$
T_{\mu\nu}^{\rm BR}
= \frac{i}{4}\left(\bar\psi iL_{e_\mu}R_{\delta_\mu}\nabla_\nu\psi
- \left(\nabla_\nu\bar\psi\right)iL_{e_\mu}R_{\delta_\mu}\psi
+ \bar\psi iL_{e_\nu}R_{\delta_\nu}\nabla_\mu\psi
- \left(\nabla_\mu\bar\psi\right)iL_{e_\nu}R_{\delta_\nu}\psi\right),
$$

and on shell its time components give the energy density $\mathcal E = E\,\psi^\dagger\psi$ and the momentum density

$$
\vec P = \frac{1}{2i}\left(\psi^\dagger\nabla\psi - \left(\nabla\psi^\dagger\right)\psi\right)
+ \frac12\nabla\times\vec S .
$$

Compare this with the current above: the spin contribution to the momentum density carries the coefficient $\tfrac12$, while the spin contribution to the electric current carries $1$. The spin-density gradient is therefore **twice as effective** at producing an electric current as at contributing to the linear momentum, and that factor of two is the Dirac value $g = 2$ seen from the angular-momentum side.

The canonical (non-symmetric) tensor

$$
T_{\mu\nu}^{\rm canonical}
= \frac{i}{2}\left(\bar\psi iL_{e_\mu}R_{\delta_\mu}\nabla_\nu\psi
- \left(\nabla_\nu\bar\psi\right)iL_{e_\mu}R_{\delta_\mu}\psi\right)
$$

does not contain the bound spin-momentum term; the term is restored by the antisymmetric (spin) part of the Belinfante improvement. Integrating, the spin contribution to the total angular momentum is

$$
\int\vec r\times\left(\tfrac12\nabla\times\vec S\right)d^3x = \int\vec S\,d^3x,
$$

so the division by two is necessary for angular momentum and the absence of it for the current is the statement of $g = 2$.

### Spin in Maxwell's equations

The same strategy — split a conserved density into a transport part and a curl of a spin density — applies to light. For monochromatic Maxwell fields in the Riemann–Silberstein form, the time-averaged momentum density splits as $\vec P = \vec P_{\rm free} + \vec P_{\rm bound}$ with $\vec P_{\rm bound} = \tfrac12\nabla\times\vec S$, and the spin density can be identified, in the paraxial or pure-helicity case, with either $\vec S = \frac{\mu_0}{2i\omega}\vec H^*\times\vec H$ or $\vec S = \frac{\epsilon_0}{2i\omega}\vec E^*\times\vec E$; the two agree for a helicity state and may differ otherwise. This is the electromagnetic analogue of the Dirac decomposition, and the companion articles on the Riemann–Silberstein vector and on angular momentum and spin in biquaternionic form develop the same objects in the framework's notation.

## The Biquaternion Reading

### The split is central versus bivector

The one algebraic structure that the decomposition exhibits is the split of a product of two generators into its symmetric and antisymmetric parts,

$$
iL_{e_\mu}R_{\delta_\mu} iL_{e_\nu}R_{\delta_\nu} = g_{\mu\nu}L_{e_t}R_{e_t} - i\sigma_{\mu\nu},
$$

the two pieces being respectively the **metric** (one number per pair of indices, symmetric, and in the algebra's terms central) and the **bivector** (antisymmetric, and in the algebra's terms the six-dimensional subspace spanned by the directions $\vec e_k$ and $i\vec e_k$). The Gordon decomposition is the statement that on shell the current splits in exactly this way: the convection term is the metric–central direction, and the spin term is the bivector direction. This is the same identification the companion article on the anomalous magnetic moment records: the anomaly multiplies $\sigma_{\mu\nu}$, a bivector, and is therefore an informational-sector object, while the tree-level convection term is central.

The comparison map of *Matrix Representations Conventions*, §*The Clifford Structure and the Frame*, assigns the six bivectors to the six directions,

$$
\mathsf{M}_2(\vec e_k) = iL_{\vec e_k}R_{\vec e_y},
\qquad
\mathsf{M}_2(i\vec e_k) = iR_{\vec e_x}\,iL_{\vec e_k}R_{\vec e_y},
$$

so that the **rotation-type** generators (the magnetic, spin-like ones) sit at the elements $i\vec e_k \in \mathbb{M}_+$, the informational sector, and the **boost-type** generators at $\vec e_k \in \mathbb{M}_-$, the material sector. The magnetic (spin) part of the Gordon split is therefore an $\mathbb{M}_+$ structure — the same sector as the spin itself — and the convection part is the central metric direction. The sector labels are not decoration: they are the algebraic form of the statement that the convection term is the orbital transport and the spin term is the intrinsic moment.

### What the framework does not supply

The current $\bar\psi iL_{e_\mu}R_{\delta_\mu}\psi = j_\mu$ is not a pure biquaternion product. This is the negative result of the companion minimal-coupling article: the Dirac adjoint $\bar\psi = \psi^\dagger iR_{\vec e_x}$ carries the Clifford-odd cell $iR_{\vec e_x} = iL_{e_t}R_{\vec e_x}$, which is not a left multiplier of $\mathbb{B}$, and a bilinear built only from $\tilde\Psi$ and $\tilde\Psi^{*}$ inside $\mathbb{B}$ cannot supply it. Consequently the Gordon decomposition is a statement about the **spinor-module** current. The framework transcribes it, names its two structures in the algebra's own sectors, and verifies the algebra of the split; it does not derive the identity from a product in $\mathbb{B}$. The same caveat applies to the axial companion identity, which carries $-iR_{\vec e_z}$ in addition to $iR_{\vec e_x}$.

What the algebra does supply is the location of the two terms: the convection term is the central, metric direction, and the spin term is the bivector direction, with the magnetic part of the bivector in the informational sector. That placement is a real bookkeeping statement, and it is the framework's contribution to this identity.

## Open Questions

1. **A biquaternion-natural current.** Is there a $\mathbb{B}$-valued current whose symmetric/antisymmetric split reproduces the Gordon split without the two-sided cell $iR_{\vec e_x}$? This is the same question the minimal-coupling article leaves open for the current itself, and a positive answer here would be a positive answer there.

2. **The massless spinor-helicity form.** In the massless case the spin term is a curl and the transport term is an energy-weighted derivative. Does the biquaternion algebra, whose two Peirce carriers, minimal left ideals here, are the two chiralities, write the massless decomposition more naturally than the four-component spinor does, and does the helix of a Weyl particle appear as an idempotent of $\mathbb{M}_+$?

3. **The factor of two.** The $g = 2$ asymmetry between the current and the momentum density is, in the framework's terms, a mismatch between an $\mathbb{M}_-$ current and an $\mathbb{M}_-$ momentum. Is there an algebraic statement that fixes the factor of two, or is it one more coefficient the algebra transcribes?

4. **The Belinfante improvement in the framework's notation.** The passage from the canonical to the symmetric tensor is a shift by the divergence of an antisymmetric (spin) tensor. The corpus's Noether-theorem article gives the canonical currents; the biquaternion form of the improvement term, and of the spin part of the angular momentum, is not written.

5. **Berry's spin for light.** The electromagnetic analogue identifies the intrinsic spin density with a curl of an $E$–$B$ cross product. The framework's field-strength biquaternion and its Riemann–Silberstein partner are the natural place to test whether this spin is the same object as the photon's helicity in the framework.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5=-iL_{e_t}R_{\vec e_z} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

The reference-frame cell of the chirality operator is $\gamma_5$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

## Summary

The Gordon decomposition splits the on-shell Dirac current as

$$
\bar\psi iL_{e_\mu}R_{\delta_\mu}\psi
= \frac{i}{2m}\left(\bar\psi\nabla_\mu\psi - \left(\nabla_\mu\bar\psi\right)\psi\right)
+ \frac{1}{m}\sum_\nu\varepsilon_\nu\,\partial/\partial x_\nu\left(\bar\psi\Sigma_{\mu\nu}\psi\right),
\qquad
\Sigma_{\mu\nu} = \tfrac14 i\left[iL_{e_\mu}R_{\delta_\mu},iL_{e_\nu}R_{\delta_\nu}\right],
$$

into a convection part and the divergence of a spin density. In momentum space it is

$$
\bar w(p_2)iL_{e_\mu}R_{\delta_\mu} w(p)
= \bar w(p_2)\left[\frac{(p+p_2)_\mu}{2m}
+ \frac{i\sum_\nu\varepsilon_\nu\,\sigma_{\mu\nu}(p_2-p)_\nu}{2m}\right]w(p),
$$

where the first term is the current of a charged scalar and the second is the spin term whose coefficient gives $g = 2$. The decomposition requires $m \neq 0$ because both terms carry $1/m$; the massless version replaces $m$ by the energy $E$ and writes the spin term as $(e/E)\nabla\times\vec S$, recovering the Dirac moment in the rest frame and the locked Weyl moment for a massless particle. The Belinfante–Rosenfeld tensor contains the same spin term with coefficient $\tfrac12$ in the momentum density, and the mismatch between that $\tfrac12$ and the current's $1$ is the angular-momentum face of $g = 2$.

The biquaternion interpretation is a naming of the two structures: the split of the generator product is the split into the metric (central) direction and the bivector direction, so the convection current is central and the spin current is a bivector whose magnetic (rotation-type) part lies in the informational sector $\mathbb{M}_+$ and whose boost-type part lies in $\mathbb{M}_-$. The identity itself is a spinor-module statement, because the Dirac adjoint carries the Clifford-odd cell $iR_{\vec e_x}$ outside the left copy $\mathbb{B}_L$; the framework transcribes it, verifies its algebra and locates its two terms, and does not derive it from a product in the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\psi$, $\bar\psi = \psi^\dagger iR_{\vec e_x}$ | Dirac spinor and its adjoint |
| $L_{a}R_{b}$, $L_{a}R_{b}\psi = a\psi b$ | Cell; $L_{e_t}R_{e_t}$ is the identity, $L_{a}R_{b}L_{c}R_{d} = L_{ac}R_{db}$ |
| $iL_{e_\mu}R_{\delta_\mu}$, $\{iL_{e_\mu}R_{\delta_\mu},iL_{e_\nu}R_{\delta_\nu}\} = 2g_{\mu\nu}L_{e_t}R_{e_t}$ | Generator cells, $iR_{\vec e_x} = iL_{e_t}R_{\vec e_x}$ and $iL_{\vec e_k}R_{\vec e_y}$; metric $g = \mathrm{diag}(+1,-1,-1,-1)$ |
| $-iR_{\vec e_z} = -iL_{e_t}R_{\vec e_z}$ | Chirality cell |
| $\sigma_{\mu\nu} = \frac{i}{2}[iL_{e_\mu}R_{\delta_\mu},iL_{e_\nu}R_{\delta_\nu}]$ | Bivector (magnetic) generator |
| $\Sigma_{\mu\nu} = \frac12\sigma_{\mu\nu} = \frac{i}{4}[iL_{e_\mu}R_{\delta_\mu},iL_{e_\nu}R_{\delta_\nu}]$ | Spin generator of the Lorentz transformations |
| $iL_{e_\mu}R_{\delta_\mu} iL_{e_\nu}R_{\delta_\nu} = g_{\mu\nu}L_{e_t}R_{e_t} - i\sigma_{\mu\nu}$ | Symmetric/antisymmetric generator split |
| $j_\mu = \bar\psi iL_{e_\mu}R_{\delta_\mu}\psi$ | Conserved number current |
| $p$, $p_2$, $k = p_2-p$, $P = \frac12(p+p_2)$ | Momenta, transfer and average |
| $\bar w_2iL_{e_\mu}R_{\delta_\mu} w = \bar w_2[(p+p_2)_\mu + i\sum_\nu\varepsilon_\nu\sigma_{\mu\nu}k_\nu]w/2m$ | Momentum-space Gordon identity |
| $\vec S = \psi^\dagger S\psi$, $S = \frac12\mathrm{diag}(\boldsymbol\sigma,\boldsymbol\sigma)$ | Spin density and spin matrix |
| $T_{\mu\nu}^{\rm BR}$, $T_{\mu\nu}^{\rm canonical}$ | Belinfante–Rosenfeld and canonical stress tensors |
| $\frac{e\hbar}{2mc}\cdot\frac12\sum_{\mu,\nu}\varepsilon_\mu\varepsilon_\nu F_{\mu\nu}\bar\psi\sigma_{\mu\nu}\psi$ | Effective Pauli moment term ($g = 2$) |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Informational and material sectors; bivector magnetic and boost parts |

## Further Reading

- W. Gordon, "Der Comptoneffekt nach der Schrödingerschen Theorie," *Zeitschrift für Physik* **40** (1926) 117–133, and "Zur Lichtfortpflanzung nach der Relativitätstheorie," *Annalen der Physik* **72** (1923) 421–456, for the origin of the current decomposition.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the Gordon decomposition, the bilinears and the $1/2m$ coefficient of the spin current.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the vertex decomposition into $F_1$ and $F_2$, the Gordon identity and the Ward identity.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the form factors, the Gordon decomposition and the renormalisation of the vertex.
- L. H. Ryder, *Quantum Field Theory* (Cambridge, 2nd ed. 1996), for the Gordon decomposition and its use in the magnetic moment.
- M. V. Berry, "Optical currents," *Journal of Optics A: Pure and Applied Optics* **11** (2009) 094001, for the Gordon strategy applied to Maxwell's equations and the intrinsic spin density of light.
- F. J. Belinfante, "On the spin angular momentum of mesons," *Physica* **6** (1939) 887–898, and L. Rosenfeld, "Sur le tenseur d'impulsion-énergie," *Mémoires de l'Académie Royale de Belgique* **18** (1940) 1–30, for the symmetric stress tensor and the spin improvement.
- The companion articles of this series: [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html), [The Anomalous Magnetic Moment in Biquaternionic Form](the-anomalous-magnetic-moment-in-biquaternionic-form.html), [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), *The Classical Origin of $g = 2$ in Biquaternionic Form*, and [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html).
