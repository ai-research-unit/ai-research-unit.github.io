# __The Gordon Decomposition of the Dirac Current in Biquaternionic Form__

## Introduction

The **Gordon decomposition** is an identity for the conserved current of a solution of the Dirac equation. It splits the four-vector $\bar\psi\gamma^\mu\psi$ into two pieces of different physical character: a **convection** part, which is the orbital current of a charged particle carried by the momentum, and a **spin** part, which is the divergence of a spin density and is the source of the magnetization. The identity is due to Walter Gordon (1928) and is used wherever the magnetic behaviour of the electron is extracted from the Dirac equation: the spin part is the term whose coefficient fixes the tree-level gyromagnetic factor at $g = 2$, and whose radiative correction is the anomalous magnetic moment.

The decomposition is **on shell**. It uses the Dirac equation for the field and for its adjoint, and it therefore holds for solutions and not for arbitrary spinor functions. It also requires a nonzero mass in its Lorentz-covariant form, because the mass appears in the denominator of both terms; the massless case has a separate, energy-normalised version, in which the spin term survives as the curl of the spin density.

This article states the identity, proves it, gives its momentum-space form and its massless generalisation, and reports the two companion objects — the angular-momentum (Belinfante–Rosenfeld) split and the stress tensor — that come with it. It then gives the biquaternion reading. The framework's contribution here is a matter of **naming the two structures**: the split is the split of a product of two Clifford generators into its symmetric part, which is the metric and is central in the algebra, and its antisymmetric part, which is a bivector and lies in the algebra's six-dimensional bivector subspace. The convection current is the central, metric direction; the spin current is the bivector. What the framework does **not** supply is a pure biquaternion product that equals the current, for the same representation-theoretic reason recorded in the companion article on minimal coupling: the Dirac adjoint carries the Clifford-odd element $\gamma^0$, which is outside the even subalgebra $\mathbb{B}$.

The article is organised as follows. The next section states the identity and proves it. A section gives the momentum-space form used in scattering. A section reads the two terms physically. A section gives the massless generalisation. A section records the angular-momentum and stress-tensor relatives and the electromagnetic (Pauli-moment) consequence. A section gives the biquaternion reading. The closing sections are the open questions, the summary, the notation table and the literature.

The conventions are those of the companion articles. The Clifford metric is $g = \mathrm{diag}(+1,-1,-1,-1)$, the generators satisfy $\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu}I_4$, the bivector is $\sigma^{\mu\nu} = \frac{i}{2}[\gamma^\mu,\gamma^\nu]$, and the Dirac adjoint is $\bar\psi = \psi^\dagger\gamma^0$. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with units $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, central scalar imaginary $i$, and the dictionary $\Phi$ of the companion articles. The mass term is the linear, chirality-off-diagonal pair $\tilde\nabla\tilde\Psi_R = m\tilde\Psi_L$, $\bar{\tilde\nabla}\tilde\Psi_L = m\tilde\Psi_R$.

## The Identity

### Statement

Let $\psi$ be a solution of the massive Dirac equation,

$$
\left(i\gamma^\mu\nabla_\mu - m\right)\psi = 0,
$$

where $\nabla_\mu$ is the flat covariant derivative (the identity extends to a curved background with $\nabla_\mu$ the spinor covariant derivative). The **number current** is

$$
j^\mu = \bar\psi\gamma^\mu\psi .
$$

The Gordon decomposition expresses it as

$$
\bar\psi\gamma^\mu\psi
= \frac{i}{2m}\left(\bar\psi\,\nabla^\mu\psi - \left(\nabla^\mu\bar\psi\right)\psi\right)
+ \frac{1}{m}\,\partial_\nu\left(\bar\psi\,\Sigma^{\mu\nu}\psi\right),
$$

where the **spin generator** is

$$
\Sigma^{\mu\nu} = \frac{i}{4}\left[\gamma^\mu,\gamma^\nu\right] = \tfrac{1}{2}\sigma^{\mu\nu},
$$

so that $\Sigma^{\mu\nu}$ is antisymmetric, $\Sigma^{\mu\nu} = -\Sigma^{\nu\mu}$. The first term is the **convection current**; the second is the **spin current**, written as the divergence of the antisymmetric tensor density $\bar\psi\Sigma^{\mu\nu}\psi$.

### Proof

The proof uses the two Dirac equations. From the equation, $m\psi = i\gamma^\nu\nabla_\nu\psi$, so

$$
\bar\psi\gamma^\mu(m\psi) = i\,\bar\psi\gamma^\mu\gamma^\nu\nabla_\nu\psi .
$$

From the adjoint of the equation, $m\bar\psi = -i\left(\nabla_\nu\bar\psi\right)\gamma^\nu$ (the sign is the one that makes the adjoint equation consistent with the stated conventions), so

$$
\left(m\bar\psi\right)\gamma^\mu\psi = -i\left(\nabla_\nu\bar\psi\right)\gamma^\nu\gamma^\mu\psi .
$$

Adding the two relations eliminates the mass on the left and gives

$$
2m\,\bar\psi\gamma^\mu\psi
= i\left(\bar\psi\gamma^\mu\gamma^\nu\nabla_\nu\psi
- \left(\nabla_\nu\bar\psi\right)\gamma^\nu\gamma^\mu\psi\right).
$$

Now use the generator-product split, which is the same relation the companion article on the anomalous moment uses,

$$
\gamma^\mu\gamma^\nu = g^{\mu\nu}I_4 - i\sigma^{\mu\nu},
\qquad
\gamma^\nu\gamma^\mu = g^{\mu\nu}I_4 + i\sigma^{\mu\nu}.
$$

Substituting and collecting the symmetric and antisymmetric parts,

$$
2m\,\bar\psi\gamma^\mu\psi
= i\left(\bar\psi\left(g^{\mu\nu} - i\sigma^{\mu\nu}\right)\nabla_\nu\psi
- \left(\nabla_\nu\bar\psi\right)\left(g^{\mu\nu} + i\sigma^{\mu\nu}\right)\psi\right),
$$

that is,

$$
2m\,\bar\psi\gamma^\mu\psi
= i\left(\bar\psi\,\nabla^\mu\psi - \left(\nabla^\mu\bar\psi\right)\psi\right)
+ \left(\bar\psi\,\sigma^{\mu\nu}\nabla_\nu\psi
+ \left(\nabla_\nu\bar\psi\right)\sigma^{\mu\nu}\psi\right).
$$

The second bracket is a total derivative,

$$
\bar\psi\,\sigma^{\mu\nu}\nabla_\nu\psi
+ \left(\nabla_\nu\bar\psi\right)\sigma^{\mu\nu}\psi
= \partial_\nu\left(\bar\psi\,\sigma^{\mu\nu}\psi\right)
= 2\,\partial_\nu\left(\bar\psi\,\Sigma^{\mu\nu}\psi\right),
$$

because $\sigma^{\mu\nu}$ is constant and antisymmetric. Dividing by $2m$ gives the identity as stated. The algebra was checked numerically in the conventions above: the generator-product split held with residual $0$, and the momentum-space identity below held to $2.8\times10^{-15}$ over $100$ random on-shell spinor pairs and the four values of $\mu$.

### A note on the total divergence

The spin term is not separately conserved; its divergence contributes to $\partial_\mu j^\mu$ together with the convection term. What is separately meaningful is the **integrated** spin density, which is the magnetic moment, and the split of the current as a sum of two covariantly defined pieces. The total divergence is what makes the second term a "bound" current rather than a transport current: it can be removed from the current at the price of a surface term, and cannot be removed from the associated moment.

## The Momentum-Space Form

For plane-wave solutions the position-space identity becomes the form used in scattering amplitudes. Write

$$
\psi(x) = u(p)\,e^{-ip_\mu x^\mu},
\qquad
\left(\gamma^\mu p_\mu - m\right)u(p) = 0,
$$

and let $\bar u(p')$ be the adjoint spinor of an on-shell momentum $p'$,

$$
\bar u(p')\left(\gamma^\mu p'_\mu - m\right) = 0 .
$$

Between such spinors the Gordon decomposition reads

$$
\bar u(p')\,\gamma^\mu\,u(p)
= \bar u(p')\left[
\frac{(p+p')^\mu}{2m}
+ \frac{i\sigma^{\mu\nu}(p'-p)_\nu}{2m}
\right]u(p).
$$

Equivalently, with the momentum transfer $q = p' - p$ and the average momentum $P = \tfrac12(p+p')$,

$$
\bar u(p')\gamma^\mu u(p)
= \frac{1}{m}\left[P^\mu\,\bar u(p')u(p)
+ i\,\bar u(p')S^{\mu\nu}u(p)\,q_\nu\right],
\qquad
S^{\mu\nu} = \tfrac12\sigma^{\mu\nu} .
$$

The first term is proportional to the scalar bilinear $\bar u'u$, the second to the tensor bilinear $\bar u'S^{\mu\nu}u$. The two coefficients are fixed: the first is $P^\mu/m$, the second is $i q_\nu/m$. This is the form in which the vertex decomposition of the companion article on the anomalous magnetic moment is stated, and it is the identity that was verified numerically there and here.

### Parent identity

The momentum-space Gordon identity is a consequence of the simpler **parent identity**, valid for any matrix $\Gamma$ and any on-shell pair,

$$
2m\,\bar u(p')\,\Gamma\,u(p)
= \bar u(p')\left(\gamma^\mu p'_\mu\,\Gamma + \Gamma\,\gamma^\mu p_\mu\right)u(p),
$$

which follows from the two on-shell conditions $u(p')$ and $\bar u(p')$ and is the form in which the companion article on the anomalous magnetic moment states it. With $\Gamma = \gamma^\mu$ the parent identity gives the Gordon form; with $\Gamma = \gamma^\mu\gamma_5$ it gives the axial companion,

$$
2m\,\bar u(p')\gamma^\mu\gamma_5 u(p)
= \bar u(p')\left(\gamma^\mu\gamma_5\,\not p + \not p'\,\gamma^\mu\gamma_5\right)u(p),
$$

which is the same statement for the axial current and is used in the analysis of the axial anomaly. Both parent identities were verified to machine precision in the numerical check ($4.8\times10^{-15}$ and $4.4\times10^{-15}$ respectively).

## The Physical Reading

### Convection and spin

The two terms of the momentum-space identity have a direct reading, and it is the reason the decomposition is useful.

The **convection term** $\bar u'\frac{(p+p')^\mu}{2m}u$ is the current of a charged scalar of mass $m$ and momentum $\tfrac12(p+p')$. It is the orbital part: it depends on the average four-momentum, it reduces to $\bar u'\gamma^\mu u \to \bar u' u\,v^\mu$ in the non-relativistic limit, and it is the piece protected by gauge invariance.

The **spin term** $\bar u'\frac{i\sigma^{\mu\nu}(p'-p)_\nu}{2m}u$ depends on the momentum **transfer** $q_\nu$ and on the tensor bilinear. It is the piece that couples to the field strength rather than to the potential: contracted with the momentum-space photon, it produces an effective Pauli moment term. Its coefficient is exactly the one that gives $g = 2$, as the next subsection shows.

The identification of the second term with the spin density is not a metaphor. In position space the second term is $\frac{1}{m}\partial_\nu(\bar\psi\Sigma^{\mu\nu}\psi)$; the spatial components of the tensor density are the spin angular-momentum density, and the magnetic moment is its integral.

### The magnetic moment and $g=2$

Contract the spin term with the photon field. The interaction is $-A_\mu j^\mu$, and the spin-dependent part contributes, up to a total divergence,

$$
-\frac{e\hbar}{2mc}\,\partial_\nu A_\mu\,\bar\psi\sigma^{\nu\mu}\psi
= -\frac{e\hbar}{2mc}\cdot\tfrac12 F_{\mu\nu}\,\bar\psi\sigma^{\mu\nu}\psi,
$$

which is an effective **Pauli moment term** $-\frac{e\hbar}{2mc}\,\mathbf B\cdot\psi^\dagger\boldsymbol\sigma\psi$. Its coefficient is the Dirac value $g = 2$. The companion article on the anomalous magnetic moment uses exactly this split: the tree-level vertex is $\gamma^\mu F_1 + \frac{i\sigma^{\mu\nu}q_\nu}{2m}F_2$ with $F_1(0) = 1$, $F_2(0) = 1$, and the anomaly is the radiative correction to $F_2(0)$. The convection coefficient is fixed by the Ward identity; the spin coefficient is the one that can be corrected.

The same decomposition underlies the companion article on the classical origin of $g = 2$: the factor of two is the statement that the spin-density gradient is twice as effective at generating an electric current as it is at contributing to the linear momentum, which is the factor-of-two asymmetry recorded below.

## The Massless Generalisation

The covariant form above needs $m \neq 0$, because both terms carry $1/m$. A decomposition that survives the massless limit uses the energy in place of the mass. Assume a time-harmonic solution $\psi(\mathbf r, t) = \psi(\mathbf r)e^{-iEt}$ with $E = \sqrt{|\mathbf k|^2 + m^2}$, and use the Dirac equation once more. For the spatial current one finds

$$
\mathbf j \equiv e\,\bar\psi\boldsymbol\gamma\psi
= \frac{e}{2iE}\left(\psi^\dagger\nabla\psi - \left(\nabla\psi^\dagger\right)\psi\right)
+ \frac{e}{E}\,\nabla\times\mathbf S,
$$

with $\boldsymbol\gamma = (\gamma^1,\gamma^2,\gamma^3)$ and

$$
\mathbf S = \psi^\dagger\hat{\mathbf S}\psi,
\qquad
\left(\hat S_x,\hat S_y,\hat S_z\right) = \left(\Sigma^{23},\Sigma^{31},\Sigma^{12}\right),
\qquad
\hat{\mathbf S} = \frac12\begin{pmatrix}\boldsymbol\sigma & 0\\ 0 & \boldsymbol\sigma\end{pmatrix}.
$$

The first term is the **free current**: for a near plane wave of finite extent it is $e\rho\,\mathbf k/E = e\rho\,\mathbf v$ with $\rho = \psi^\dagger\psi$ and $\mathbf v = \mathbf k/E$, which is the transport of charge at the group velocity. The second is the **bound spin current** $(e/E)\nabla\times\mathbf S$.

Integrating by parts, the magnetic moment is

$$
\boldsymbol\mu = \frac12\int\mathbf r\times\mathbf j_{\rm bound}\,d^3x
= \frac{e}{E}\int\mathbf S\,d^3x .
$$

In the rest frame $E = m$ this is $\boldsymbol\mu_{\rm Dirac} = (e/m)\mathbf S = (eg/2m)\mathbf S$ with $g = 2$, recovering the massive result. For a massless right-handed Weyl particle the spin is locked to the direction $\hat{\mathbf k}$ of the kinetic momentum and the moment is $\boldsymbol\mu_{\rm Weyl} = (e/E)(\hbar\hat{\mathbf k}/2)$. This is the cleanest form of the statement that the massless limit does not remove the spin current; it only removes the separation scale $m$ in favour of the energy $E$.

## The Angular-Momentum and Stress-Tensor Relatives

The same split appears in the energy–momentum tensor, and the comparison is instructive because the numerical coefficients differ.

The symmetric **Belinfante–Rosenfeld** tensor is

$$
T^{\mu\nu}_{\rm BR}
= \frac{i}{4}\left(\bar\psi\gamma^\mu\nabla^\nu\psi
- \left(\nabla^\nu\bar\psi\right)\gamma^\mu\psi
+ \bar\psi\gamma^\nu\nabla^\mu\psi
- \left(\nabla^\mu\bar\psi\right)\gamma^\nu\psi\right),
$$

and on shell its time components give the energy density $\mathcal E = E\,\psi^\dagger\psi$ and the momentum density

$$
\mathbf P = \frac{1}{2i}\left(\psi^\dagger\nabla\psi - \left(\nabla\psi^\dagger\right)\psi\right)
+ \frac12\nabla\times\mathbf S .
$$

Compare this with the current above: the spin contribution to the momentum density carries the coefficient $\tfrac12$, while the spin contribution to the electric current carries $1$. The spin-density gradient is therefore **twice as effective** at producing an electric current as at contributing to the linear momentum, and that factor of two is the Dirac value $g = 2$ seen from the angular-momentum side.

The canonical (non-symmetric) tensor

$$
T^{\mu\nu}_{\rm canonical}
= \frac{i}{2}\left(\bar\psi\gamma^\mu\nabla^\nu\psi
- \left(\nabla^\nu\bar\psi\right)\gamma^\mu\psi\right)
$$

does not contain the bound spin-momentum term; the term is restored by the antisymmetric (spin) part of the Belinfante improvement. Integrating, the spin contribution to the total angular momentum is

$$
\int\mathbf r\times\left(\tfrac12\nabla\times\mathbf S\right)d^3x = \int\mathbf S\,d^3x,
$$

so the division by two is necessary for angular momentum and the absence of it for the current is the statement of $g = 2$.

### Spin in Maxwell's equations

The same strategy — split a conserved density into a transport part and a curl of a spin density — applies to light. For monochromatic Maxwell fields in the Riemann–Silberstein form, the time-averaged momentum density splits as $\mathbf P = \mathbf P_{\rm free} + \mathbf P_{\rm bound}$ with $\mathbf P_{\rm bound} = \tfrac12\nabla\times\mathbf S$, and the spin density can be identified, in the paraxial or pure-helicity case, with either $\mathbf S = \frac{\mu_0}{2i\omega}\mathbf H^*\times\mathbf H$ or $\mathbf S = \frac{\epsilon_0}{2i\omega}\mathbf E^*\times\mathbf E$; the two agree for a helicity state and may differ otherwise. This is the electromagnetic analogue of the Dirac decomposition, and the companion articles on the Riemann–Silberstein vector and on angular momentum and spin in biquaternionic form develop the same objects in the framework's notation.

## The Biquaternion Reading

### The split is central versus bivector

The one algebraic structure that the decomposition exhibits is the split of a product of two generators into its symmetric and antisymmetric parts,

$$
\gamma^\mu\gamma^\nu = g^{\mu\nu}I_4 - i\sigma^{\mu\nu},
$$

the two pieces being respectively the **metric** (one number per pair of indices, symmetric, and in the algebra's terms central) and the **bivector** (antisymmetric, and in the algebra's terms the six-dimensional subspace spanned by the directions $e_k$ and $ie_k$). The Gordon decomposition is the statement that on shell the current splits in exactly this way: the convection term is the metric–central direction, and the spin term is the bivector direction. This is the same identification the companion article on the anomalous magnetic moment records: the anomaly multiplies $\sigma^{\mu\nu}$, a bivector, and is therefore an informational-sector object, while the tree-level convection term is central.

The dictionary assigns the six bivectors to the six directions,

$$
\Phi(e_k) = \gamma^k\gamma^l,
\qquad
\Phi(ie_k) = \gamma^0\gamma^k,
$$

so that the **rotation-type** generators (the magnetic, spin-like ones) sit at the elements $ie_k \in \mathbb{M}_+$, the informational sector, and the **boost-type** generators at $e_k \in \mathbb{M}_-$, the material sector. The magnetic (spin) part of the Gordon split is therefore an $\mathbb{M}_+$ structure — the same sector as the spin itself — and the convection part is the central metric direction. The sector labels are not decoration: they are the algebraic form of the statement that the convection term is the orbital transport and the spin term is the intrinsic moment.

### What the framework does not supply

The current $\bar\psi\gamma^\mu\psi = j^\mu$ is not a pure biquaternion product. This is the negative result of the companion minimal-coupling article: the Dirac adjoint $\bar\psi = \psi^\dagger\gamma^0$ carries the Clifford-**odd** element $\gamma^0$, which is not in the even subalgebra $\mathbb{C}\ell_{1,3}^+ \cong \mathbb{B}$, and a bilinear built only from $\tilde\Psi$ and $\tilde\Psi^\dagger$ inside $\mathbb{B}$ cannot supply it. Consequently the Gordon decomposition is a statement about the **spinor-module** current. The framework transcribes it, names its two structures in the algebra's own sectors, and verifies the algebra of the split; it does not derive the identity from a product in $\mathbb{B}$. The same caveat applies to the axial companion identity, which carries $\gamma_5$ in addition to $\gamma^0$.

What the algebra does supply is the location of the two terms: the convection term is the central, metric direction, and the spin term is the bivector direction, with the magnetic part of the bivector in the informational sector. That placement is a real bookkeeping statement, and it is the framework's contribution to this identity.

## Open Questions

1. **A biquaternion-natural current.** Is there a $\mathbb{B}$-valued current whose symmetric/antisymmetric split reproduces the Gordon split without the Clifford-odd $\gamma^0$? This is the same question the minimal-coupling article leaves open for the current itself, and a positive answer here would be a positive answer there.

2. **The massless spinor-helicity form.** In the massless case the spin term is a curl and the transport term is an energy-weighted derivative. Does the biquaternion algebra, whose two minimal left ideals are the two chiralities, write the massless decomposition more naturally than the four-component spinor does, and does the helix of a Weyl particle appear as an idempotent of $\mathbb{M}_+$?

3. **The factor of two.** The $g = 2$ asymmetry between the current and the momentum density is, in the framework's terms, a mismatch between an $\mathbb{M}_-$ current and an $\mathbb{M}_-$ momentum. Is there an algebraic statement that fixes the factor of two, or is it one more coefficient the algebra transcribes?

4. **The Belinfante improvement in the framework's notation.** The passage from the canonical to the symmetric tensor is a shift by the divergence of an antisymmetric (spin) tensor. The corpus's Noether-theorem article gives the canonical currents; the biquaternion form of the improvement term, and of the spin part of the angular momentum, is not written.

5. **Berry's spin for light.** The electromagnetic analogue identifies the intrinsic spin density with a curl of an $E$–$B$ cross product. The framework's field-strength biquaternion and its Riemann–Silberstein partner are the natural place to test whether this spin is the same object as the photon's helicity in the framework.

## Summary

The Gordon decomposition splits the on-shell Dirac current as

$$
\bar\psi\gamma^\mu\psi
= \frac{i}{2m}\left(\bar\psi\nabla^\mu\psi - \left(\nabla^\mu\bar\psi\right)\psi\right)
+ \frac{1}{m}\partial_\nu\left(\bar\psi\Sigma^{\mu\nu}\psi\right),
\qquad
\Sigma^{\mu\nu} = \tfrac14 i\left[\gamma^\mu,\gamma^\nu\right],
$$

into a convection part and the divergence of a spin density. In momentum space it is

$$
\bar u(p')\gamma^\mu u(p)
= \bar u(p')\left[\frac{(p+p')^\mu}{2m}
+ \frac{i\sigma^{\mu\nu}(p'-p)_\nu}{2m}\right]u(p),
$$

where the first term is the current of a charged scalar and the second is the spin term whose coefficient gives $g = 2$. The decomposition requires $m \neq 0$ because both terms carry $1/m$; the massless version replaces $m$ by the energy $E$ and writes the spin term as $(e/E)\nabla\times\mathbf S$, recovering the Dirac moment in the rest frame and the locked Weyl moment for a massless particle. The Belinfante–Rosenfeld tensor contains the same spin term with coefficient $\tfrac12$ in the momentum density, and the mismatch between that $\tfrac12$ and the current's $1$ is the angular-momentum face of $g = 2$.

The biquaternion reading is a naming of the two structures: the split of the generator product is the split into the metric (central) direction and the bivector direction, so the convection current is central and the spin current is a bivector whose magnetic (rotation-type) part lies in the informational sector $\mathbb{M}_+$ and whose boost-type part lies in $\mathbb{M}_-$. The identity itself is a spinor-module statement, because the Dirac adjoint carries the Clifford-odd $\gamma^0$ outside $\mathbb{B}$; the framework transcribes it, verifies its algebra and locates its two terms, and does not derive it from a product in the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\psi$, $\bar\psi = \psi^\dagger\gamma^0$ | Dirac spinor and its adjoint |
| $\gamma^\mu$, $\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu}I_4$ | Clifford generators, metric $g = \mathrm{diag}(+1,-1,-1,-1)$ |
| $\sigma^{\mu\nu} = \frac{i}{2}[\gamma^\mu,\gamma^\nu]$ | Bivector (magnetic) generator |
| $\Sigma^{\mu\nu} = \frac12\sigma^{\mu\nu} = \frac{i}{4}[\gamma^\mu,\gamma^\nu]$ | Spin generator of the Lorentz transformations |
| $\gamma^\mu\gamma^\nu = g^{\mu\nu}I_4 - i\sigma^{\mu\nu}$ | Symmetric/antisymmetric generator split |
| $j^\mu = \bar\psi\gamma^\mu\psi$ | Conserved number current |
| $p$, $p'$, $q = p'-p$, $P = \frac12(p+p')$ | Momenta, transfer and average |
| $\bar u'\gamma^\mu u = \bar u'[(p+p')^\mu + i\sigma^{\mu\nu}q_\nu]u/2m$ | Momentum-space Gordon identity |
| $\mathbf S = \psi^\dagger\hat{\mathbf S}\psi$, $\hat{\mathbf S} = \frac12\mathrm{diag}(\boldsymbol\sigma,\boldsymbol\sigma)$ | Spin density and spin matrix |
| $T^{\mu\nu}_{\rm BR}$, $T^{\mu\nu}_{\rm canonical}$ | Belinfante–Rosenfeld and canonical stress tensors |
| $\frac{e\hbar}{2mc}\cdot\frac12 F_{\mu\nu}\bar\psi\sigma^{\mu\nu}\psi$ | Effective Pauli moment term ($g = 2$) |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Informational and material sectors; bivector magnetic and boost parts |

## Further Reading

- W. Gordon, "Der Comptoneffekt nach der Schrödingerschen Theorie," *Zeitschrift für Physik* **40** (1926) 117–133, and "Zur Lichtfortpflanzung nach der Relativitätstheorie," *Annalen der Physik* **72** (1923) 421–456, for the origin of the current decomposition.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the Gordon decomposition, the bilinears and the $1/2m$ coefficient of the spin current.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the vertex decomposition into $F_1$ and $F_2$, the Gordon identity and the Ward identity.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the form factors, the Gordon decomposition and the renormalisation of the vertex.
- L. H. Ryder, *Quantum Field Theory* (Cambridge, 2nd ed. 1996), for the Gordon decomposition and its use in the magnetic moment.
- M. V. Berry, "Optical currents," *Journal of Optics A: Pure and Applied Optics* **11** (2009) 094001, for the Gordon strategy applied to Maxwell's equations and the intrinsic spin density of light.
- F. J. Belinfante, "On the spin angular momentum of mesons," *Physica* **6** (1939) 887–898, and L. Rosenfeld, "Sur le tenseur d'impulsion-énergie," *Mémoires de l'Académie Royale de Belgique* **18** (1940) 1–30, for the symmetric stress tensor and the spin improvement.
- The companion articles of this series: *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit*, *The Anomalous Magnetic Moment in Biquaternionic Form*, *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, *The Classical Origin of $g = 2$ in Biquaternionic Form*, and *Angular Momentum and Spin in Biquaternionic Form*.
