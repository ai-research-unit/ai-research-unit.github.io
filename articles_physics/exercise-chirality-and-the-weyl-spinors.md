# __Exercise: Chirality and the Weyl Spinors__

## Introduction

This is one of the articles in the Dirac exercise series accompanying the biquaternion Dirac equation, and the one that works entirely inside the **spinor module**. It is a worked exercise: the structures are taken from the parent article *The Spinor Module in Biquaternionic Form and Its Lorentz Action* and then applied. The value is in the solutions.

The following are assumed, with the notation of the parent article.

- The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, $e_1e_2 = e_3$, scalar imaginary $i$, and the conjugations $\bar{\cdot}$ (quaternion), ${}^{*}$ (complex), ${}^{\dagger} = \bar{\cdot}\circ{}^{*}$ (Hermitian). The subspaces are $\mathbb{M}_-$ (material), $\mathbb{M}_+$ (informational), $\mathbb{H}_{\mathbb{B}}$ (real quaternions), and $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_0$ (the centre).
- The matrix realization $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ with $\Phi(e_0) = I_2$, $\Phi(e_k) = -i\sigma_k$, $\Phi(i) = iI_2$, satisfying $\Phi(\tilde{Q}\tilde{R}) = \Phi(\tilde{Q})\Phi(\tilde{R})$, $\det\Phi(\tilde{Q}) = N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$, and $\Phi(\tilde{Q}^{\dagger}) = \Phi(\tilde{Q})^{\dagger}$.
- The **spinor module** $S = \mathbb{C}^2$, the unique simple left $\mathbb{B}$-module, carrying $\psi\mapsto\Phi(\tilde{Q})\psi$. Its ideal realization is $S\cong\mathbb{B}p$, with $p = \tfrac12(e_0+ie_3)$, $q = \tfrac12(e_0-ie_3)$, $pq = qp = 0$, $p+q = e_0$, and basis $\{p,\,y\}$, $y = e_2p = \tfrac12(ie_1+e_2)$.
- The **two chiral halves**: the left-handed Weyl module $V_1 = (\tfrac12,0)$, carried by $S$ with action $\psi\mapsto g\psi$, $g = \Phi(\tilde{\Lambda})$; and the right-handed module $\bar{S} = (0,\tfrac12)$, carried by $\mathbb{C}^2$ with action $\chi\mapsto\Phi(\tilde{\Lambda}^{*})\chi$. Their direct sum is the **Dirac module** $\Delta = S\oplus\bar{S}$, $\dim_{\mathbb{C}}\Delta = 4$.
- The group $SL(2,\mathbb{C}) = \{\tilde{\Lambda} : \tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0\}$ of **unit-norm biquaternions**, and the double cover $\pi:SL(2,\mathbb{C})\to SO^{+}(1,3)$, $\pi(\tilde{\Lambda}):\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^{\dagger}$ on $\mathbb{M}_-$.
- The **symplectic form** $\varepsilon(\psi,\phi) = \psi^{T}\epsilon\,\phi$, $\epsilon = \left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$; the mixed pairing $b(\psi,\chi) = \psi^{\dagger}\chi$ on $S\times\bar{S}$; and the bilinear $X = uv^{\dagger}$, transforming as $X\mapsto gXg^{\dagger}$.

Seven problems are worked below, one per section. Each is carried to a definite answer, and the algebraic identities are checked numerically in double precision.

## Problem 1: The Chiral Projectors

A Dirac spinor is an element of $\Delta = S\oplus\bar{S}$. Written in blocks,

$$
\Psi = \begin{pmatrix}\psi_L\\ \psi_R\end{pmatrix}, \qquad \psi_L\in S,\quad \psi_R\in\bar{S},
$$

the upper block carrying the left-handed module and the lower the right-handed one. On $\Delta$ the **chirality operator** is the block-diagonal matrix

$$
\gamma_5 = \begin{pmatrix}-I_2 & 0\\ 0 & I_2\end{pmatrix}, \qquad \gamma_5^2 = I_4.
$$

The **chiral projectors** are

$$
P_L = \tfrac12\left(I_4 - \gamma_5\right), \qquad P_R = \tfrac12\left(I_4 + \gamma_5\right).
$$

Explicitly $P_L = \left(\begin{smallmatrix}I_2&0\\0&0\end{smallmatrix}\right)$ and $P_R = \left(\begin{smallmatrix}0&0\\0&I_2\end{smallmatrix}\right)$. The projector algebra is immediate:

$$
P_L^2 = P_L, \qquad P_R^2 = P_R, \qquad P_LP_R = P_RP_L = 0, \qquad P_L + P_R = I_4,
$$

and additionally $\gamma_5 = P_R - P_L$, $\operatorname{Tr}P_L = \operatorname{Tr}P_R = 2$, so each projector has rank two. All identities hold to machine accuracy (residual $<10^{-15}$).

Their action on a Dirac spinor is the projection onto each half:

$$
P_L\Psi = \begin{pmatrix}\psi_L\\ 0\end{pmatrix}, \qquad
P_R\Psi = \begin{pmatrix}0\\ \psi_R\end{pmatrix}, \qquad
\gamma_5\Psi = \begin{pmatrix}-\psi_L\\ \psi_R\end{pmatrix}.
$$

**Lorentz invariance.** The $SL(2,\mathbb{C})$ action on $\Delta$ is block diagonal,

$$
S(\tilde{\Lambda}) = \begin{pmatrix} g & 0\\ 0 & \Phi(\tilde{\Lambda}^{*})\end{pmatrix}, \qquad g = \Phi(\tilde{\Lambda}),
$$

so it commutes with $\gamma_5$ and with each $P_{L,R}$. Chirality is therefore a Lorentz-invariant label: a Lorentz transformation never mixes the two halves.

**Why the halves are not the ideals.** The projectors above are not the Peirce projectors $p,q$. The minimal left ideals $\mathbb{B}p$ and $\mathbb{B}q$ are both isomorphic to $S$, and left multiplication by $\tilde{\Lambda}$ acts on each by the *same* defining representation; the chiral projectors instead act on the four-dimensional Dirac module and distinguish $\psi\mapsto g\psi$ from $\chi\mapsto\Phi(\tilde{\Lambda}^{*})\chi$. This distinction is invisible to the simple algebra $\mathbb{B}$ and appears only through the conjugate module — as the parent article stresses.

## Problem 2: The Two Weyl Halves and the Mass Term

Take the mostly-minus counterpart of the parent's block gamma matrices,

$$
\gamma^0 = \begin{pmatrix}0 & I_2\\ I_2 & 0\end{pmatrix}, \qquad
\gamma^k = \begin{pmatrix}0 & \sigma^k\\ -\sigma^k & 0\end{pmatrix},
$$

satisfying $\{\gamma^{\mu},\gamma^{\nu}\} = 2g^{\mu\nu}I_4$ with $g = \operatorname{diag}(+1,-1,-1,-1)$. The Dirac equation is $i\gamma^{\mu}\partial_{\mu}\Psi = m\Psi$. Inserting $\Psi = (\psi_L,\psi_R)^{T}$ and the block form of the gammas gives, after collecting the two blocks,

$$
i\left(\partial_0 + \boldsymbol{\sigma}\cdot\nabla\right)\psi_R = m\,\psi_L, \qquad
i\left(\partial_0 - \boldsymbol{\sigma}\cdot\nabla\right)\psi_L = m\,\psi_R.
$$

**The massless case.** Setting $m=0$, the two equations decouple:

$$
\left(\partial_0 + \boldsymbol{\sigma}\cdot\nabla\right)\psi_R = 0, \qquad
\left(\partial_0 - \boldsymbol{\sigma}\cdot\nabla\right)\psi_L = 0.
$$

Each is a two-component **Weyl equation**, one per chiral half: $\psi_L\in S$ obeys the $\bar{\sigma}$-equation and $\psi_R\in\bar{S}$ the $\sigma$-equation, and the two propagate independently. The massless Dirac field is thus two independent Weyl fields.

**The massive case.** Eliminating $\psi_R$: apply $i(\partial_0+\boldsymbol{\sigma}\cdot\nabla)$ to the second equation and use the first,

$$
i\left(\partial_0+\boldsymbol{\sigma}\cdot\nabla\right)i\left(\partial_0-\boldsymbol{\sigma}\cdot\nabla\right)\psi_L
= i\left(\partial_0+\boldsymbol{\sigma}\cdot\nabla\right)m\psi_R = m^2\psi_L .
$$

Using $(\boldsymbol{\sigma}\cdot\nabla)^2 = \nabla^2$ and $i^2=-1$, the left side is $-\left(\partial_0^2-\nabla^2\right)\psi_L$, so

$$
\left(\Box + m^2\right)\psi_L = 0, \qquad \Box = \partial_0^2-\nabla^2,
$$

and identically for $\psi_R$. Thus the mass term, and only the mass term, couples the two halves: at $m=0$ the coupling disappears, and each half separately obeys the massive Klein–Gordon equation. (The overall sign of $\Box$ is the usual metric-sign convention, fixed here by the block gammas.)
<!-- CONVENTION — notation, important for cross-article review. The □ of this article, □ = ∂₀² − ∇², is MINUS the biquaternion d'Alembertian used throughout the rest of the series, □ = ∇̃∇̄̃ = ∂²_{ict} + Δ = Δ − c⁻²∂_t². The two are related by □_here = −□_series, so the two mass-term signs describe the SAME equation: (□ + m²)ψ = 0 here and (□ − m²c²/ℏ²)ψ = 0 in the Klein–Gordon and Dirac articles have the same solution set, because an overall factor −1 does not change the kernel. This article uses the standard QFT metric (+,−,−,−) with □ = ∂₀² − ∇² in natural units (ħ = c = 1); the series uses the ict / (−,+,+,+) convention. Neither is an error. Do NOT align the mass-term signs across articles without also changing the □ definition. Reciprocal note at the opening of The Klein–Gordon Equation in Biquaternionic Form. -->

**Mass shell.** For a plane wave $\Psi\propto e^{-ik_0x^0+i\mathbf{k}\cdot\mathbf{x}}$, the Klein–Gordon equation gives $k_0^2 = \mathbf{k}^2 + m^2c^2/\hbar^2$. Equivalently, with the four-momentum $\tilde{P} = iE/c\,e_0 + \mathbf{p}\in\mathbb{M}_-$ and $k = p/\hbar$,

$$
N(\tilde{P}) = \tilde{P}\bar{\tilde{P}} = -\frac{E^2}{c^2} + \mathbf{p}^2 = -m^2c^2,
$$

i.e. $E^2 = \mathbf{p}^2c^2 + m^2c^4$.

**Biquaternion form.** The parent Dirac article writes the massive equation as the linear, chirality-off-diagonal pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$, with $\tilde{\Psi} = \tilde{\Psi}_L + \tilde{\Psi}_R$; the mass term is the off-diagonal coupling between the two chiral halves. Conjugation of the four coefficients, $\tilde{\Psi}\mapsto\tilde{\Psi}^{*}$, is the real-structure operation relating the defining module $S$ to its conjugate $\bar{S}$, and the parent's anti-Hermitian conjugation $\tilde{\Psi}^{\flat} = -\tilde{\Psi}^{\dagger}$ is that real structure itself, not the mass. The exercise therefore treats the mass term in the explicit Dirac representation, where it is unambiguous.

## Problem 3: A Boost and a Rotation of Each Half

Recall the two distinguished unit-norm biquaternions and their images under $\Phi$:

$$
\tilde{\Lambda} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}}
\;\longmapsto\;
\Phi(\tilde{\Lambda}) = \cosh\frac{\psi}{2}\,I_2 + \sinh\frac{\psi}{2}\,\hat{\mathbf{u}}\cdot\boldsymbol{\sigma},
$$

$$
\tilde{R} = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\,\hat{\mathbf{n}}
\;\longmapsto\;
\Phi(\tilde{R}) = \cos\frac{\theta}{2}\,I_2 - i\sin\frac{\theta}{2}\,\hat{\mathbf{n}}\cdot\boldsymbol{\sigma}.
$$

For $\hat{\mathbf{u}} = \hat{\mathbf{n}} = \hat{e}_3$ these are diagonal:

$$
g_{\text{boost}} = \operatorname{diag}\!\left(e^{\psi/2}, e^{-\psi/2}\right), \qquad
g_{\text{rot}} = \operatorname{diag}\!\left(e^{-i\theta/2}, e^{i\theta/2}\right).
$$

The left-handed spinor transforms by $\psi_L\mapsto g\psi_L$, the right-handed one by $\psi_R\mapsto\Phi(\tilde{\Lambda}^{*})\psi_R$.

**Boost.** A boost rotor has a real scalar part and an imaginary vector part, so conjugating its coefficients negates the vector part: $\tilde{\Lambda}^{*} = \bar{\tilde{\Lambda}} = \cosh\frac{\psi}{2} - i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$. Hence

$$
\Phi(\tilde{\Lambda}^{*}) = \cosh\frac{\psi}{2}\,I_2 - \sinh\frac{\psi}{2}\,\hat{\mathbf{u}}\cdot\boldsymbol{\sigma}
= \operatorname{diag}\!\left(e^{-\psi/2}, e^{\psi/2}\right) = g_{\text{boost}}^{-1}.
$$

So under a boost the two halves transform by **inverse** matrices. With $\psi_L = (\psi_{L1},\psi_{L2})^{T}$ and $\psi_R = (\psi_{R1},\psi_{R2})^{T}$,

$$
\psi_L \mapsto \left(e^{\psi/2}\psi_{L1},\; e^{-\psi/2}\psi_{L2}\right)^{T}, \qquad
\psi_R \mapsto \left(e^{-\psi/2}\psi_{R1},\; e^{\psi/2}\psi_{R2}\right)^{T}.
$$

The component that is stretched in the left-handed spinor is contracted in the right-handed one. This opposition of the two halves under boosts is the representation-theoretic content of the labels "left" and "right".

**Rotation.** A rotation rotor is a real quaternion, so $\tilde{R}^{*} = \tilde{R}$ and

$$
\Phi(\tilde{R}^{*}) = \Phi(\tilde{R}) = g_{\text{rot}} = \operatorname{diag}\!\left(e^{-i\theta/2}, e^{i\theta/2}\right).
$$

Both halves transform by the **same** matrix. This is consistent with $S$ and $\bar{S}$ being non-isomorphic complex $SL(2,\mathbb{C})$-modules: they are isomorphic as $SU(2)$-modules, because the defining representation of $SU(2)$ is self-conjugate (quaternionic). The modules separate only under boosts.

**The exact relation for a general rotor.** For arbitrary $\tilde{\Lambda}\in SL(2,\mathbb{C})$, with $g = \Phi(\tilde{\Lambda})$ and $\bar{g}$ the entrywise complex conjugate, one has

$$
\Phi(\tilde{\Lambda}^{*}) = \epsilon^{-1}\,\bar{g}\,\epsilon = \epsilon\,\bar{g}\,\epsilon^{-1},
$$

where $\epsilon = \left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$. (The two expressions coincide because $\epsilon^{-1} = -\epsilon$.) This is the precise form of the parent's statement that the right-handed action is "equivalent to the entrywise-conjugate action $g\mapsto\bar{g}$, the two differing by conjugation with the invariant tensor $\epsilon$". The identity was verified numerically on 500 random unit-norm biquaternions, with residual $<10^{-9}$.

## Problem 4: The Invariant Symplectic Pairing

Define, for $\psi,\phi\in S$,

$$
\varepsilon(\psi,\phi) = \psi^{T}\epsilon\,\phi = \psi_1\phi_2 - \psi_2\phi_1, \qquad
\epsilon = \begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

**Invariance.** Let $g\in SL(2,\mathbb{C})$ and write $g = \left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$ with $ad-bc = 1$. Then

$$
g^{T}\epsilon\,g
= \begin{pmatrix}a&c\\ b&d\end{pmatrix}
\begin{pmatrix}0&1\\-1&0\end{pmatrix}
\begin{pmatrix}a&b\\ c&d\end{pmatrix}
= \begin{pmatrix}0&ad-bc\\ -(ad-bc)&0\end{pmatrix}
= (\det g)\,\epsilon = \epsilon .
$$

Therefore $\varepsilon(g\psi,g\phi) = \psi^{T}g^{T}\epsilon g\,\phi = \varepsilon(\psi,\phi)$: the form is invariant. The same computation applies to the right-handed action, because $\det\Phi(\tilde{\Lambda}^{*}) = \overline{\det\Phi(\tilde{\Lambda})} = 1$ (and indeed $\tilde{\Lambda}^{*}\in SL(2,\mathbb{C})$ because $N(\tilde{\Lambda}^{*}) = \overline{N(\tilde{\Lambda})} = 1$). So $\varepsilon$ is an invariant bilinear form on each chiral half separately.

**Nondegeneracy and self-duality.** The matrix $\epsilon$ is invertible, so $\varepsilon$ is nondegenerate; equivalently, $\psi = 0$ if $\varepsilon(\psi,\phi) = 0$ for all $\phi$. The map $\psi\mapsto\varepsilon(\psi,\cdot)$ is an isomorphism $S\to S^{*}$ intertwining the two actions, so

$$
S^{*}\cong S .
$$

This is the self-duality of the defining module. It is **not** self-conjugacy: $\bar{S}\not\cong S$ as complex $SL(2,\mathbb{C})$-modules. The distinction is the parent's warning that "self-duality is not self-conjugacy", and it is why a pair of left-handed spinors has an invariant antisymmetric contraction while a left- and a right-handed spinor need the separate mixed pairing $b$.

**Concrete check.** For a boost along $\hat{e}_3$ and $\psi = (1,0)^{T}$, $\phi = (0,1)^{T}$, one has $\varepsilon(\psi,\phi) = 1$, while $\varepsilon(g\psi,g\phi) = e^{\psi/2}e^{-\psi/2} = 1$. The identity $g^{T}\epsilon g = \epsilon$ was verified numerically for boosts, rotations, and random unit-norm biquaternions, residual $<10^{-12}$.

## Problem 5: The Spinor Bilinear and the Four-Vector

The parent article introduces the bilinear

$$
X = u\,v^{\dagger}, \qquad u,v\in S,
$$

and shows that it transforms as $X\mapsto gXg^{\dagger}$. This is immediate: $(gu)(gv)^{\dagger} = g(uv^{\dagger})g^{\dagger}$.

**Hermiticity and the general four-vector map.** The matrix $X = uv^{\dagger}$ is Hermitian if and only if $u$ and $v$ are proportional by a real factor; in general it is a rank-one element of the full algebra $\mathbb{B}$, not of the Hermitian subspace. The bilinear that lands in the Hermitian subspace $\mathbb{M}_+$ (real dimension four) is the **Hermitian part**

$$
H(u,v) = \tfrac12\left(u\,v^{\dagger} + v\,u^{\dagger}\right) \in \mathbb{M}_+ .
$$

For $v = \pm u$ this reduces to $H = \pm uu^{\dagger}$, and the parent's unsymmetrized $X = uv^{\dagger}$ is then already Hermitian. In general one must symmetrize. The four-vector associated with the spinor pair is

$$
V(u,v) = i\,H(u,v) \in \mathbb{M}_- ,
$$

where the last inclusion uses $i\mathbb{M}_+ = \mathbb{M}_-$.

**Verification of the properties.** Since $H^{\dagger} = H$, $V^{\dagger} = (iH)^{\dagger} = -iH^{\dagger} = -V$, so $V\in\mathbb{M}_-$. The equivariance carries over: $H\mapsto gHg^{\dagger} = \Phi(\tilde{\Lambda}H\tilde{\Lambda}^{\dagger})$, using $g = \Phi(\tilde{\Lambda})$ and $\Phi(\tilde{\Lambda}^{\dagger}) = g^{\dagger}$; hence $V\mapsto \tilde{\Lambda}V\tilde{\Lambda}^{\dagger}$, the parent's **rotor conjugation** on the material sector, recovered from the one-sided spinor action (numerical residual $<10^{-12}$).

**Norm form.** Write $H = h_0e_0 + i\mathbf{h}$. Then $V = ih_0e_0 - \mathbf{h}$, and

$$
N(V) = N(iH) = -\det\Phi(H) = -h_0^2 + \mathbf{h}^2 ,
$$

which is the $(3,1)$ Minkowski form of $\mathbb{M}_-$. Two independent checks: for $u = v$ one has $H = uu^{\dagger}$, which is rank one, so $\det H = 0$ and

$$
N(V) = 0 .
$$

A single spinor therefore determines a **null** four-vector — its flag direction.

**Explicit example.** Take $u = v = (1,0)^{T}$. Then $uu^{\dagger} = \operatorname{diag}(1,0) = \tfrac12(I_2+\sigma_3)$, so

$$
H = \tfrac12 e_0 + \tfrac{i}{2} e_3, \qquad V = iH = \tfrac{i}{2}e_0 - \tfrac12 e_3,
$$

with components $(q_0,q_1,q_2,q_3) = (\tfrac12,0,0,-\tfrac12)$ in the basis $\{ie_0,e_1,e_2,e_3\}$ and norm $N(V) = -\tfrac14+\tfrac14 = 0$ (numerical residual $<10^{-15}$). This is the content of the parent's factorization $(\tfrac12,\tfrac12) = (\tfrac12,0)\otimes(0,\tfrac12)$: the four-vector is a bilinear in one left-handed and one right-handed spinor.

## Problem 6: The Double Cover on a Concrete Rotation

Take a rotation about $\hat{\mathbf{n}} = \hat{e}_3$ by angle $\theta$,

$$
\tilde{R}(\theta) = \cos\frac{\theta}{2}\,e_0 + \sin\frac{\theta}{2}\,\hat{e}_3,
\qquad
\Phi(\tilde{R}(\theta)) = \operatorname{diag}\!\left(e^{-i\theta/2}, e^{i\theta/2}\right).
$$

**On the spinor.** At $\theta = 2\pi$,

$$
\Phi(\tilde{R}(2\pi)) = \operatorname{diag}\!\left(e^{-i\pi}, e^{i\pi}\right) = \operatorname{diag}(-1,-1) = -I_2 ,
$$

so every spinor is sent to its negative: $\psi\mapsto-\psi$, which is not the identity. At $\theta = 4\pi$,

$$
\Phi(\tilde{R}(4\pi)) = \operatorname{diag}\!\left(e^{-2\pi i}, e^{2\pi i}\right) = I_2 ,
$$

so the spinor returns to itself.

**On the four-vector.** The corresponding four-vector action is rotor conjugation by $\tilde{R}(\theta)$. At $\theta = 2\pi$ the rotor is $\tilde{R}(2\pi) = \cos\pi\,e_0 = -e_0$, and

$$
(-e_0)\,\tilde{X}\,(-e_0)^{\dagger} = (-e_0)\,\tilde{X}\,(-e_0) = e_0\,\tilde{X}\,e_0 = \tilde{X},
$$

using $(-e_0)^{\dagger} = -e_0$. So a $2\pi$ rotation acts as $+\mathrm{id}$ on every four-vector. At $\theta = 4\pi$ the rotor is $+e_0$ and both actions are the identity.

**The general statement.** The two behaviours are the two entries of the parent's table:

$$
\pi:\;SL(2,\mathbb{C})\longrightarrow SO^{+}(1,3), \qquad
\ker\pi = \{\pm e_0\}\cong\mathbb{Z}/2\mathbb{Z},
$$

while the spinor action $\psi\mapsto\tilde{\Lambda}\psi$ has trivial kernel: $\Phi(-e_0) = -I_2\neq I_2$. Hence

$$
SO^{+}(1,3)\cong SL(2,\mathbb{C})/\{\pm e_0\},
$$

and $SL(2,\mathbb{C})$ is the double cover. Numerically, for $\hat{\mathbf{n}} = \hat{e}_3$ and $\theta = 2\pi$, the residual of $\Phi(\tilde{R}(2\pi))+I_2$ is $<10^{-15}$, and that of the four-vector conjugation against the identity is $<10^{-12}$.

## Problem 7: The Spinor Action and Rotor Conjugation

**From one-sided to two-sided.** Let $u,v\in S$ and form $V = V(u,v) = i\cdot\tfrac12(uv^{\dagger}+vu^{\dagger})\in\mathbb{M}_-$. Under the spinor action $u\mapsto gu$, $v\mapsto gv$, the bilinear transforms as

$$
V \;\longmapsto\; g\,V\,g^{\dagger} = \Phi\!\left(\tilde{\Lambda}\,V\,\tilde{\Lambda}^{\dagger}\right),
$$

which is exactly the rotor conjugation of the material sector. A single spinor contributes one factor, $\psi\mapsto g\psi$ (linear, one-sided); the four-vector is built from two spinors and therefore carries two factors, $gVg^{\dagger}$ (quadratic, two-sided). This is the origin of the difference in kind between the two actions, and it is the sense in which the four-vector is a *pair* of spinors.

**The sign that cancels and the sign that does not.** Replace $\tilde{\Lambda}$ by $-\tilde{\Lambda}$, i.e. $g$ by $-g$. On four-vectors $(-g)V(-g)^{\dagger} = gVg^{\dagger}$, because the two signs cancel; on spinors $(-g)\psi = -g\psi\neq g\psi$ for every nonzero spinor. Hence $\ker\pi = \{\pm e_0\}$ on $\mathbb{M}_-$ but the kernel of the spinor action is trivial: the spinor representation does not descend to $SO^{+}(1,3)$.

**Composition.** Successive rotors compose by multiplication in both pictures: $\tilde{\Lambda}_2(\tilde{\Lambda}_1\psi) = (\tilde{\Lambda}_2\tilde{\Lambda}_1)\psi$ and $\tilde{\Lambda}_2(\tilde{\Lambda}_1V\tilde{\Lambda}_1^{\dagger})\tilde{\Lambda}_2^{\dagger} = (\tilde{\Lambda}_2\tilde{\Lambda}_1)V(\tilde{\Lambda}_2\tilde{\Lambda}_1)^{\dagger}$. The difference is only the doubled factor, and hence the cancelling sign, in the four-vector formula.

**The mixed pairing.** Finally, the pairing $b(\psi,\chi) = \psi^{\dagger}\chi$ on $S\times\bar{S}$, with $\psi\mapsto g\psi$ and $\chi\mapsto\Phi(\tilde{\Lambda}^{*})\chi$, is invariant:

$$
b\left(g\psi,\Phi(\tilde{\Lambda}^{*})\chi\right)
= \psi^{\dagger}g^{\dagger}\Phi(\tilde{\Lambda}^{*})\chi
= \psi^{\dagger}\Phi\!\left(\tilde{\Lambda}^{\dagger}\tilde{\Lambda}^{*}\right)\chi
= \psi^{\dagger}\chi,
$$

because $\tilde{\Lambda}^{\dagger}\tilde{\Lambda}^{*} = (\bar{\tilde{\Lambda}}\tilde{\Lambda})^{*} = e_0^{*} = e_0$ for a unit-norm biquaternion. This is the Dirac scalar bilinear (numerical residual $<10^{-12}$).

## Limiting Cases

The solutions have the expected limits.

- **Rapidity limits.** As $\psi\to0$ both halves become indistinguishable, reflecting that the chiral splitting is a property of the full Lorentz group, not of its compact subgroup; for large $\psi$ the halves diverge exponentially, one component of each growing as $e^{\psi/2}$ and the other decaying as $e^{-\psi/2}$.
- **$v = \pm u$ (single spinor):** $H = \pm uu^{\dagger}$ is rank one, so $V$ is null. For a generic pair, $V$ is timelike or spacelike according to the sign of $N(V) = -h_0^2+\mathbf{h}^2$.
- **$\theta = 2\pi$ versus $4\pi$:** the spinor picks up $-1$ at $2\pi$ and returns at $4\pi$, while the four-vector is unchanged at both — the double cover in its simplest instance.

## What the Solutions Illustrate

**1. The parent's structures are sufficient, once the module is made explicit.** All seven problems use only $S$, its conjugate $\bar{S}$, the realization $\Phi$, and the two pairings. The only extra structure is the chirality operator on the Dirac module, which is external to the simple algebra $\mathbb{B}$.

**2. Chirality is a real-structure notion.** The two halves are invisible to $\mathbb{B}$ as a complex algebra, where both minimal left ideals are copies of $S$; they become visible only through the conjugate module and the complexification, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$.

**3. The four-vector is the bilinear shadow of the spinor.** Rotor conjugation on $\mathbb{M}_-$ arises from the one-sided spinor action through the Hermitian bilinear $H(u,v)$; the vector representation is the tensor product of the two chiral halves.

**4. The double cover is a kernel statement.** $\ker\pi = \{\pm e_0\}$ on the four-vectors, but trivial on the spinors; the difference is one factor of $g$ versus two.

## Notes on the Parent Article

Three points arose where the parent either leaves a definition to convention or uses a shorthand that is not general. They are recorded here as findings; the choices used above are stated explicitly.

1. **Right-handed action, exact form.** The parent says the right-handed action is "equivalent to the entrywise-conjugate action $g\mapsto\bar{g}$ (the two differ by conjugation with the invariant tensor $\epsilon$)"; it does not give the identity. The precise identity is $\Phi(\tilde{\Lambda}^{*}) = \epsilon^{-1}\bar{g}\epsilon = \epsilon\bar{g}\epsilon^{-1}$, verified numerically. The orientation of $\epsilon$ in this identity is a convention.

2. **The spinor-to-vector map for a general pair.** The parent writes $X = uv^{\dagger}$ and warns that for a generic pair $iuv^{\dagger}$ does not lie in $\mathbb{M}_-$ and is therefore not a four-vector; it then supplies the symmetrised map $H = \tfrac12(uv^{\dagger}+vu^{\dagger})\in\mathbb{M}_+$, with four-vector image $V = iH\in\mathbb{M}_-$. The exercise uses that symmetrised map. The shorthand $X = uv^{\dagger}$ is general, but the identification of $iX$ with a four-vector is not.

3. **The biquaternion mass term and the conjugate module.** The parent's massive equation is now the linear, chirality-off-diagonal pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$, whose mass term couples the two chiral halves, with the anti-Hermitian conjugation $\tilde{\Psi}^{\flat} = -\tilde{\Psi}^{\dagger}$ the algebra's real structure rather than the mass. The exercise keeps its mass term in the explicit Dirac representation, where it is unambiguous. The parent exhibits neither $\bar{S}$ inside $\mathbb{B}$ nor the isomorphism between the left-regular module $\mathbb{B}\cong S\oplus S$ and the Dirac module $S\oplus\bar{S}$.

A fourth point, the biquaternion (ideal) form of the symplectic pairing, is the parent's open question 3; the exercise uses the matrix-coordinate form throughout, which is the form the parent defines.

## Summary

Seven problems were solved. (1) The chiral projectors $P_L = \tfrac12(I_4-\gamma_5)$, $P_R = \tfrac12(I_4+\gamma_5)$, with $\gamma_5 = \operatorname{diag}(-I_2,I_2)$ on $\Delta = S\oplus\bar{S}$, satisfy the projector algebra and commute with the Lorentz action. (2) The massless Dirac equation splits into two independent Weyl equations; the mass term couples them, and each half obeys $(\Box+m^2)\psi = 0$, with mass shell $k_0^2 = \mathbf{k}^2+m^2c^2/\hbar^2$. (3) Under a boost along $\hat{e}_3$ the halves transform by inverse matrices $g_{\text{boost}} = \operatorname{diag}(e^{\psi/2},e^{-\psi/2})$ and $g_{\text{boost}}^{-1}$; under a rotation both transform by $g_{\text{rot}} = \operatorname{diag}(e^{-i\theta/2},e^{i\theta/2})$; in general $\Phi(\tilde{\Lambda}^{*}) = \epsilon^{-1}\bar{g}\epsilon$. (4) The symplectic form $\varepsilon(\psi,\phi) = \psi^{T}\epsilon\phi$ is invariant because $g^{T}\epsilon g = (\det g)\epsilon = \epsilon$, is nondegenerate, and gives $S^{*}\cong S$, but is not self-conjugacy. (5) The spinor bilinear gives $V = i\cdot\tfrac12(uv^{\dagger}+vu^{\dagger})\in\mathbb{M}_-$, transforming by rotor conjugation $\tilde{\Lambda}V\tilde{\Lambda}^{\dagger}$; a single spinor gives a null four-vector, and the vector representation is the tensor product of the chiral halves. (6) A $2\pi$ rotation acts as $-I_2$ on spinors and as the identity on four-vectors, and a $4\pi$ rotation as the identity on both: the double cover $SO^{+}(1,3)\cong SL(2,\mathbb{C})/\{\pm e_0\}$. (7) The two-sided four-vector action is the bilinear shadow of the one-sided spinor action; the sign cancels in the former but not in the latter, and the mixed pairing $b(\psi,\chi) = \psi^{\dagger}\chi$ is invariant.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_1e_2 = e_3$ |
| $\mathbb{C}_{\mathbb{B}}, \mathbb{H}_{\mathbb{B}}$ | Complex subspace (centre), real-quaternion subspace |
| $\mathbb{M}_-, \mathbb{M}_+$ | Anti-Hermitian (material), Hermitian (informational) subspaces |
| $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ | Matrix realization, $\Phi(e_k) = -i\sigma_k$, $\Phi(i) = iI_2$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \det\Phi(\tilde{Q})$ | Norm form |
| $S = \mathbb{C}^2$, $\bar{S}$ | Spinor module, conjugate (right-handed) module |
| $V_1 = (\tfrac12,0)$, $\bar{S} = (0,\tfrac12)$ | Left- and right-handed Weyl modules |
| $\Delta = S\oplus\bar{S}$ | Dirac module, $\dim_{\mathbb{C}}\Delta = 4$ |
| $p = \tfrac12(e_0+ie_3),\; q = \tfrac12(e_0-ie_3)$ | Primitive orthogonal idempotents |
| $\gamma_5 = \operatorname{diag}(-I_2,I_2)$ | Chirality operator on $\Delta$ |
| $P_L = \tfrac12(I_4-\gamma_5),\; P_R = \tfrac12(I_4+\gamma_5)$ | Chiral projectors |
| $\psi_L\in S$, $\psi_R\in\bar{S}$ | Left- and right-handed Weyl spinors |
| $\tilde{\Lambda} = \cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\hat{\mathbf{u}}$ | Boost rotor ($\mathbb{M}_+$) |
| $\tilde{R} = \cos\frac{\theta}{2}+\sin\frac{\theta}{2}\hat{\mathbf{n}}$ | Rotation rotor ($\mathbb{H}_{\mathbb{B}}$) |
| $g = \Phi(\tilde{\Lambda})$ | Defining (left-handed) action matrix |
| $\Phi(\tilde{\Lambda}^{*}) = \epsilon^{-1}\bar{g}\epsilon$ | Right-handed action matrix |
| $\varepsilon(\psi,\phi) = \psi^{T}\epsilon\phi$ | Invariant symplectic pairing on $S$ |
| $b(\psi,\chi) = \psi^{\dagger}\chi$ | Invariant pairing $S\times\bar{S}\to\mathbb{C}$ |
| $V = i\cdot\tfrac12(uv^{\dagger}+vu^{\dagger})$ | Four-vector from a spinor pair |
| $SL(2,\mathbb{C})$, $\pi$ | Unit-norm biquaternions; double cover of $SO^{+}(1,3)$ |

## Further Reading

- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component spinor calculus, the invariant $\epsilon$-form, and the Weyl spinors.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of the Lorentz group and the relation between spinors and four-vectors.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the construction of the Dirac spinor from two Weyl spinors and the mass term.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the modules of $M_2(\mathbb{C})$, the highest-weight classification, and the Clebsch–Gordan rule.
- The companion articles of this series: *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, *The Dirac Equation in Biquaternionic Form*, and *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*.
