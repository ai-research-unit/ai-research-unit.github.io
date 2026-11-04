# __Exercise: Chirality and the Weyl Spinors__

## Introduction

This is one of the articles in the Dirac exercise series accompanying the biquaternion Dirac equation, and the one that works entirely inside the **spinor module**. It is a worked exercise: the structures are taken from the parent article *The Spinor Module in Biquaternionic Form and Its Lorentz Action* and then applied. The value is in the solutions.

The following are assumed, with the notation of the parent article.

- The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, $\vec e_k^2 = -e_t$, $\vec e_x \vec e_y = \vec e_z$, scalar imaginary $i$, and the conjugations ${}^{\natural}$ (quaternion), $\bar{\cdot}$ (complex), ${}^{*} = {}^{\natural}\circ\bar{\cdot}$ (Hermitian). The subspaces are $\mathbb{M}_-$ (material), $\mathbb{M}_+$ (informational), $\mathbb{H}_{\mathbb{B}}$ (real quaternions), and $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_t$ (the centre).
- The matrix realization $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ with $\mathsf{M}_2(e_t) = I_2$, $\mathsf{M}_2(\vec e_k) = -i\sigma_k$, $\mathsf{M}_2(i) = iI_2$, satisfying $\mathsf{M}_2(\tilde{Q}\tilde u_{\mathrm r}) = \mathsf{M}_2(\tilde{Q})\mathsf{M}_2(\tilde u_{\mathrm r})$, $\det\mathsf{M}_2(\tilde{Q}) = \langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$, and $\mathsf{M}_2(\tilde{Q}^{*}) = \mathsf{M}_2(\tilde{Q})^{\dagger}$.
- The **spinor module** $S = \mathbb{C}^2$, the unique simple left $\mathbb{B}$-module, carrying $\psi\mapsto\mathsf{M}_2(\tilde{Q})\psi$. Its ideal realization is $S\cong\mathbb{B}\tilde\Pi_+$, with $\tilde\Pi_+ = \tfrac12(e_t+i\vec e_z)$ and $\tilde\Pi_- = \tfrac12(e_t-i\vec e_z)$, the two idempotents associated with the root of $+1$ $i\vec e_z$, $(i\vec e_z)^2 = e_t$; $\tilde\Pi_+\tilde\Pi_- = \tilde\Pi_-\tilde\Pi_+ = 0$, $\tilde\Pi_++\tilde\Pi_- = e_t$, and basis $\{\tilde\Pi_+,\,y\}$, $y = \vec e_y\tilde\Pi_+ = \tfrac12(i\vec e_x+\vec e_y)$.
- The **two chiral halves**: the left-handed Weyl module $V_1 = (\tfrac12,0)$, carried by $S$ with action $\psi\mapsto g\psi$, $g = \mathsf{M}_2(\tilde U^{\mathrm{lor}})$ with $\tilde U^{\mathrm{lor}}$ the unit-norm biquaternion that implements the Lorentz transformation; and the right-handed module $\bar{S} = (0,\tfrac12)$, carried by $\mathbb{C}^2$ with action $\chi\mapsto\mathsf{M}_2(\bar{\tilde U}^{\mathrm{lor}})\chi$, the coefficientwise conjugate, which is $(g^{\dagger})^{-1}$ and not $g^{\dagger}$ (Problem 3). Their direct sum is the **Dirac module** $\Delta = S\oplus\bar{S}$, $\dim_{\mathbb{C}}\Delta = 4$.
- The group $SL(2,\mathbb{C}) = \{\tilde U^{\mathrm{lor}} : \tilde U^{\mathrm{lor}}\tilde U^{\mathrm{lor}}{}^{\natural} = e_t\}$ of **unit-norm biquaternions**, and the double cover $\pi:SL(2,\mathbb{C})\to SO^{+}(1,3)$, $\pi(\tilde U^{\mathrm{lor}}):\tilde{Q}\mapsto\tilde U^{\mathrm{lor}}\tilde{Q}\tilde U^{\mathrm{lor}}{}^{*}$ on $\mathbb{M}_-$.
- The **symplectic form** $\varepsilon(\psi,\phi) = \psi^{T}\epsilon\,\phi$, $\epsilon = \left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$; the mixed pairing $\mathfrak{b}(\psi,\chi) = \psi^{\dagger}\chi$ on $S\times\bar{S}$; and the bilinear $\tilde{Q} = wv^{\dagger}$, whose matrix representative $X=\mathsf{M}_2(\tilde{Q})$ transforms as $X\mapsto gXg^{\dagger}$.

Seven problems are worked below, one per section.

## Problem 1: The Chiral Projectors

A Dirac spinor is an element of $\Delta = S\oplus\bar{S}$. Written in blocks,

$$
\Psi = \begin{pmatrix}\psi_L\\ \psi_R\end{pmatrix}, \qquad \psi_L\in S,\quad \psi_R\in\bar{S},
$$

the upper block carrying the left-handed module and the lower the right-handed one. On $\Delta$ the **chirality operator** is the block-diagonal matrix

$$
\Gamma = \begin{pmatrix}-I_2 & 0\\ 0 & I_2\end{pmatrix}, \qquad \Gamma^2 = I_4.
$$

The **chiral projectors** are

$$
P_L = \tfrac12\left(I_4 - \Gamma\right), \qquad P_R = \tfrac12\left(I_4 + \Gamma\right).
$$

Explicitly $P_L = \left(\begin{smallmatrix}I_2&0\\0&0\end{smallmatrix}\right)$ and $P_R = \left(\begin{smallmatrix}0&0\\0&I_2\end{smallmatrix}\right)$. The projector algebra is immediate:

$$
\boxed{\;P_L^2 = P_L, \qquad P_R^2 = P_R, \qquad P_LP_R = P_RP_L = 0, \qquad P_L + P_R = I_4\;},
$$

and additionally $\Gamma = P_R - P_L$, $\operatorname{Tr}P_L = \operatorname{Tr}P_R = 2$, so each projector has rank two. All identities hold to machine accuracy (residual $<10^{-15}$).

Their action on a Dirac spinor is the projection onto each half:

$$
P_L\Psi = \begin{pmatrix}\psi_L\\ 0\end{pmatrix}, \qquad
P_R\Psi = \begin{pmatrix}0\\ \psi_R\end{pmatrix}, \qquad
\Gamma\Psi = \begin{pmatrix}-\psi_L\\ \psi_R\end{pmatrix}.
$$

**Lorentz invariance.** The $SL(2,\mathbb{C})$ action on $\Delta$ is block diagonal,

$$
S(\tilde U^{\mathrm{lor}}) = \begin{pmatrix} g & 0\\ 0 & \mathsf{M}_2(\bar{\tilde U}^{\mathrm{lor}})\end{pmatrix}, \qquad g = \mathsf{M}_2(\tilde U^{\mathrm{lor}}),
$$

so it commutes with $\Gamma$ and with each $P_{L,R}$. Chirality is therefore Lorentz-invariant: the cell commutes with every Lorentz generator, so a Lorentz transformation never mixes the two halves.

**Why the halves are not the ideals.** The projectors above are not the Peirce idempotents $\tilde\Pi_+,\tilde\Pi_-$. The minimal left ideals $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$ are both isomorphic to $S$, and left multiplication by $\tilde U^{\mathrm{lor}}$ acts on each by the *same* defining representation; the chiral projectors instead act on the four-dimensional Dirac module and distinguish $\psi\mapsto g\psi$ from $\chi\mapsto\mathsf{M}_2(\bar{\tilde U}^{\mathrm{lor}})\chi$. This distinction is invisible to the simple algebra $\mathbb{B}$ and appears only through the conjugate module — as the parent article stresses.

**A second route to the same two halves.** The source recorded in *The Chiral Algebra of Biquaternions and the Cyclic Representation of the Dirac Equation* splits the biquaternion wave function itself, in the light-cone basis, into its **positive and negative signed parts** with respect to the null idempotents $N = \tfrac12(1,\vec u)$ and $\bar N$, and identifies the sign of the signed part with the chirality, $F^+\sim\psi_R$, $F^-\sim\psi_L$. That split is a Peirce split of the wave function, not the projector $\tfrac12(I_4\pm\Gamma)$ on the Dirac module used in this problem. The two labellings agree only after the correspondence between that chiral algebra and the Weyl system, which that article verifies row by row; the projectors here act on $\Delta = S\oplus\bar S$, whereas the signed parts live in $\mathbb{B}$.

## Problem 2: The Two Weyl Halves and the Mass Term

This problem works in the natural units $\hbar=c=1$; the factors of $\hbar$ and $c$ are restored in the mass-shell paragraph.

**The four cells.** Write $L_a$ and $R_b$ for left and right multiplication, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, so that $L_aR_b\,L_cR_d=L_{ac}R_{db}$. The generator cells of the reference frame are

$$
C_t := iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}}, \qquad
C_k := iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\quad(k=x,y,z),
$$

$C_\mu$ is the cell of the coordinate $x_\mu$. Since $e_t=1$, the timelike cell is a pure right multiplication. Each cell carries one factor of $i$, so a product of two cells spends $i^2=-1$ once. The cells satisfy

$$
C_\mu C_\nu + C_\nu C_\mu = 2g_{\mu\nu}I_4, \qquad g=\operatorname{diag}(+1,-1,-1,-1),
$$

so that $C_t^2=I_4$ and $C_k^2=-I_4$. On the chiral pair $(\psi_L,\psi_R)$ they act as

$$
C_t(\psi_L,\psi_R)=(\psi_R,\psi_L), \qquad
C_k(\psi_L,\psi_R)=(\sigma_k\psi_R,\,-\sigma_k\psi_L),
$$

where $\sigma_k=\mathsf{M}_2(i\vec e_k)$; the block arrays of the five cells are recorded in *The Legacy Gamma Formulation*.

**The chiral pair.** The dynamics is the **one-sided** chiral pair of the parent article: two equations, one per chirality,

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L ,
$$

$$
\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R .
$$

The first acts on the right-handed half, the second on the left-handed one, and the second is the quaternion conjugate of the first. In the chiral basis, after collecting the two blocks, they read

$$
i\left(\partial/\partial t' + \boldsymbol{\sigma}\cdot\nabla\right)\psi_R = m\,\psi_L ,
$$

$$
i\left(\partial/\partial t' - \boldsymbol{\sigma}\cdot\nabla\right)\psi_L = m\,\psi_R .
$$

**The massless case.** Setting $m=0$, the two equations decouple:

$$
\left(\partial/\partial t' + \boldsymbol{\sigma}\cdot\nabla\right)\psi_R = 0, \qquad
\left(\partial/\partial t' - \boldsymbol{\sigma}\cdot\nabla\right)\psi_L = 0.
$$

Each is a two-component **Weyl equation**, one per chiral half: $\psi_L\in S$ obeys the $\bar{\sigma}$-equation and $\psi_R\in\bar{S}$ the $\sigma$-equation, and the two propagate independently. The massless Dirac field is thus two independent Weyl fields.

**The massive case.** Eliminating $\psi_R$: apply $i(\partial/\partial t'+\boldsymbol{\sigma}\cdot\nabla)$ to the second equation and use the first. The two explicit $i$'s meet and collapse, $i\cdot i=-1$, so

$$
i\left(\partial/\partial t'+\boldsymbol{\sigma}\cdot\nabla\right)i\left(\partial/\partial t'-\boldsymbol{\sigma}\cdot\nabla\right)\psi_L
= -\left(\partial/\partial t'+\boldsymbol{\sigma}\cdot\nabla\right)\left(\partial/\partial t'-\boldsymbol{\sigma}\cdot\nabla\right)\psi_L ,
$$

and with $(\boldsymbol{\sigma}\cdot\nabla)^2 = \nabla^2$ the cross terms cancel and the left side is $\left(\nabla^2-\partial^2/\partial {t'}^2\right)\psi_L$. The right side is $i(\partial/\partial t'+\boldsymbol{\sigma}\cdot\nabla)m\psi_R = m^2\psi_L$, again by the first equation. Hence

$$
\left(\nabla^2-\frac{\partial^2}{\partial {t'}^2}\right)\psi_L = m^2\psi_L ,
$$

and identically for $\psi_R$. The operator is the **d'Alembertian**, in the series convention,

$$
\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \frac{\partial^2}{\partial Q_t^2} + \Delta = -\frac{\partial^2}{\partial {t'}^2} + \nabla^2
$$

with $Q_t=ict'$ and $\partial^2/\partial Q_t^2=-\partial^2/\partial {t'}^2$ at $c=1$; with $c$ restored the time term is $-c^{-2}\partial^2/\partial {t'}^2$. Hence

$$
\left(\Box - m^2\right)\psi_L = 0,
$$

and likewise for $\psi_R$; with $\hbar$ and $c$ restored the same statement is $(\Box - m^2c^2/\hbar^2)\psi = 0$. Thus the mass term, and only the mass term, couples the two halves: when $m=0$ each half separately obeys the massless wave equation; for $m\neq0$ it obeys the Klein–Gordon equation.

**Mass shell.** For a plane wave $\Psi\propto \exp(-ik_0x_0+i\vec k\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z))$ with $x_0 = ct'$, the Klein–Gordon equation gives $k_0^2 = \vec k^2 + m^2c^2/\hbar^2$. Equivalently, with the four-momentum $\tilde{P} = iE/c\,e_t + \vec p\in\mathbb{M}_-$ and $k = P/\hbar$, whose components are $(k_0,\vec k) = (E/(\hbar c),\vec p/\hbar)$,

$$
\langle\tilde{P}\rangle_{\natural} = \tilde{P}\tilde{P}^{\natural} = -\frac{E^2}{c^2} + \vec p^2 = -m^2c^2 \qquad(\vec p^2=|\vec p|^2),
$$

i.e. $E^2 = \vec p^2c^2 + m^2c^4$.

**The second Dirac equation.** Two equations carry the name, and they must not be read as one. The pair above is the **one-sided** form of the equation: both gradients act by left multiplication, the field lives in $\Delta=S\oplus\bar S$, and the mass is the scalar coupling between the two chiral halves. The **two-sided** form of the equation is a single field equation on $F\in\mathbb{B}$, Kravchenko's form,

$$
\left(i\frac{\partial}{\partial t'}+D_3\right)F - mi\,\bar F\,\vec e_z = 0, \qquad D_3=\sum_k\vec e_k\frac{\partial}{\partial Q_k},
$$

in which the derivative acts from the left, the coefficient conjugation $\bar{\cdot}$ acts with no side, and the mass term ends in a right multiplication by $\vec e_z$. The two are related by the dictionary and are not the same operator: the mass of the pair is a scalar coupling of $S$ to $\bar S$; the mass of the two-sided equation is a conjugation together with a spatial direction. Chirality is why the second side is needed at all: left multiplication preserves each chiral half, so no left multiplication, and no sum of left multiplications, carries one chirality into the other. The pair is the definition; the two-sided equation is its single-field compression, and the conjugation is the price of that compression. The chirality of the two-sided equation is the chirality cell of the frame, $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, which represents the central grading of the complexification on $\Delta$; the cell is recorded in *The Legacy Gamma Formulation*.

Three conjugations must not be confused. The coefficient conjugation $\tilde{\Psi}\mapsto\bar{\tilde{\Psi}}$ is the antilinear map that relates the defining module $S$ to its conjugate $\bar{S}$; the Hermitian star $\tilde{\Psi}^{*}=\bar{\tilde{\Psi}}^{\,\natural}$ is its composition with the quaternion conjugation; and the parent's anti-Hermitian conjugation $\tilde{\Psi}^{\flat} = -\tilde{\Psi}^{*}$ is the algebra's real structure, with fixed space $\mathbb{M}_-$. None of the three is the mass. The exercise therefore treats the mass term in the explicit Dirac module, where it is unambiguous.

## Problem 3: A Boost and a Rotation of Each Half

Recall the two distinguished unit-norm biquaternions and their images under $\mathsf{M}_2$:

$$
\tilde U_{\mathrm b} = \cosh\frac{\psi}{2} + i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b}
\;\longmapsto\;
\mathsf{M}_2(\tilde U_{\mathrm b}) = \cosh\frac{\psi}{2}\,I_2 + \sinh\frac{\psi}{2}\,\vec u_{\mathrm b}\cdot\boldsymbol{\sigma},
$$

$$
\tilde u_{\mathrm r} = \cos\frac{\theta}{2} + \sin\frac{\theta}{2}\,\vec u_{\mathrm r}
\;\longmapsto\;
\mathsf{M}_2(\tilde u_{\mathrm r}) = \cos\frac{\theta}{2}\,I_2 - i\sin\frac{\theta}{2}\,\vec u_{\mathrm r}\cdot\boldsymbol{\sigma}.
$$

In the first line the map sends the coefficient $i$ to $i$ and the unit $\vec u_{\mathrm b}$ to $-i\vec u_{\mathrm b}\cdot\boldsymbol{\sigma}$, so the two factors of $i$ meet and collapse, $i\cdot(-i)=+1$, by $i^2=-1$:

$$
\mathsf{M}_2(i\vec u_{\mathrm b}) = i\,\mathsf{M}_2(\vec u_{\mathrm b}) = i\,(-i)\,\vec u_{\mathrm b}\cdot\boldsymbol{\sigma} = \vec u_{\mathrm b}\cdot\boldsymbol{\sigma}.
$$

In the second line nothing collapses: a real quaternion has no coefficient $i$, and the matrix $i$ in front of $\boldsymbol{\sigma}$ is the only one.

For $\vec u_{\mathrm b} = \vec u_{\mathrm r} = \vec u_z$ these are diagonal:

$$
g_{\text{boost}} = \operatorname{diag}\!\left(\exp(\psi/2), \exp(-\psi/2)\right), \qquad
g_{\text{rot}} = \operatorname{diag}\!\left(\exp(-i\theta/2), \exp(i\theta/2)\right).
$$

The left-handed spinor transforms by $\psi_L\mapsto g\psi_L$, the right-handed one by $\psi_R\mapsto\mathsf{M}_2(\bar{\tilde U}^{\mathrm{lor}})\psi_R$, with $\tilde U^{\mathrm{lor}}=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ the rotor of the transformation ($\tilde u_{\mathrm r}=e_t$ for the boost above).

**Boost.** A boost rotor has a real scalar part and an imaginary vector part, so conjugating its coefficients negates the vector part: $\bar{\tilde U}_{\mathrm b} = \tilde U_{\mathrm b}^{\natural} = \cosh\frac{\psi}{2} - i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$. Hence

$$
\mathsf{M}_2(\bar{\tilde U}_{\mathrm b}) = \cosh\frac{\psi}{2}\,I_2 - \sinh\frac{\psi}{2}\,\vec u_{\mathrm b}\cdot\boldsymbol{\sigma}
= \operatorname{diag}\!\left(\exp(-\psi/2), \exp(\psi/2)\right) = g_{\text{boost}}^{-1}.
$$

The sign flips because the conjugation turns the coefficient $+i\sinh\frac{\psi}{2}$ into $-i\sinh\frac{\psi}{2}$, and the map then gives $-\sinh\frac{\psi}{2}\,\vec u_{\mathrm b}\cdot\boldsymbol{\sigma}$ by the same collapse $i\cdot(-i)=+1$; no second minus sign enters.

So under a boost the two halves transform by **inverse** matrices. With $\psi_L = (\psi_{L1},\psi_{L2})^{T}$ and $\psi_R = (\psi_{R1},\psi_{R2})^{T}$,

$$
\psi_L \mapsto \left(\exp(\psi/2)\psi_{L1},\; \exp(-\psi/2)\psi_{L2}\right)^{T}, \qquad
\psi_R \mapsto \left(\exp(-\psi/2)\psi_{R1},\; \exp(\psi/2)\psi_{R2}\right)^{T}.
$$

The component that is stretched in the left-handed spinor is contracted in the right-handed one. This opposition of the two halves under boosts is the representation-theoretic content of the labels "left" and "right".

**Rotation.** A rotation rotor is a real quaternion, so $\bar{\tilde u}_{\mathrm r} = \tilde u_{\mathrm r}$ and

$$
\mathsf{M}_2(\bar{\tilde u}_{\mathrm r}) = \mathsf{M}_2(\tilde u_{\mathrm r}) = g_{\text{rot}} = \operatorname{diag}\!\left(\exp(-i\theta/2), \exp(i\theta/2)\right).
$$

Both halves transform by the **same** matrix. This is consistent with $S$ and $\bar{S}$ being non-isomorphic complex $SL(2,\mathbb{C})$-modules: they are isomorphic as $SU(2)$-modules, because the defining representation of $SU(2)$ is self-conjugate (quaternionic). The modules separate only under boosts.

**The exact relation for a general rotor.** For arbitrary $\tilde U^{\mathrm{lor}}\in SL(2,\mathbb{C})$, with $g = \mathsf{M}_2(\tilde U^{\mathrm{lor}})$ and $\bar{g}$ the entrywise complex conjugate, one has

$$
\mathsf{M}_2(\bar{\tilde U}^{\mathrm{lor}}) = \epsilon^{-1}\,\bar{g}\,\epsilon = \epsilon\,\bar{g}\,\epsilon^{-1},
$$

where $\epsilon = \left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$. (The two expressions coincide because $\epsilon^{-1} = -\epsilon$.) This is the precise form of the parent's statement that the right-handed action is "equivalent to the entrywise-conjugate action $g\mapsto\bar{g}$, the two differing by conjugation with the invariant tensor $\epsilon$". The conjugation on the left is therefore the **coefficientwise (complex)** conjugation of the four coefficients, written $\bar{\cdot}$ throughout this exercise, and the identity says that it is the **inverse conjugate transpose**,

$$
\mathsf{M}_2(\bar{\tilde U}^{\mathrm{lor}}) = \epsilon^{-1}\bar{g}\epsilon = (g^{\dagger})^{-1} .
$$

The **Hermitian star** $\tilde U^{\mathrm{lor}}{}^{*}$ is a different conjugation and gives a different matrix, $\mathsf{M}_2(\tilde U^{\mathrm{lor}}{}^{*}) = g^{\dagger}$, because the realization satisfies $\mathsf{M}_2(\tilde{Q}^{*}) = \mathsf{M}_2(\tilde{Q})^{\dagger}$. The two agree exactly when $g$ is unitary — a rotation — and differ for a boost, where $g$ is real, so that $g^{\dagger} = g$ while $(g^{\dagger})^{-1} = g^{-1}$. Only $\bar{\cdot}$ serves as the right-handed action, and it is the symbol used here. (The parent states the same identity, in its section *The Two Chiral Halves*.)

## Problem 4: The Invariant Symplectic Pairing

Define, for $\psi,\phi\in S$,

$$
\varepsilon(\psi,\phi) = \psi^{T}\epsilon\,\phi = \psi_1\phi_2 - \psi_2\phi_1, \qquad
\epsilon = \begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

**Invariance.** Let $g\in SL(2,\mathbb{C})$ and write $g = \left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$ with $ad-bc = 1$. Then

$$
\boxed{\;g^{T}\epsilon\,g
= \begin{pmatrix}a&c\\ b&d\end{pmatrix}
\begin{pmatrix}0&1\\-1&0\end{pmatrix}
\begin{pmatrix}a&b\\ c&d\end{pmatrix}
= \begin{pmatrix}0&ad-bc\\ -(ad-bc)&0\end{pmatrix}
= (\det g)\,\epsilon = \epsilon\;}.
$$

Therefore $\varepsilon(g\psi,g\phi) = \psi^{T}g^{T}\epsilon g\,\phi = \varepsilon(\psi,\phi)$: the form is invariant. The same computation applies to the right-handed action, because $\det\mathsf{M}_2(\bar{\tilde U}^{\mathrm{lor}}) = \bigl(\overline{\det g}\bigr)^{-1} = 1$ (and indeed $\bar{\tilde U}^{\mathrm{lor}}\in SL(2,\mathbb{C})$ because $\langle\bar{\tilde U}^{\mathrm{lor}}\rangle_{\natural} = \overline{\langle\tilde U^{\mathrm{lor}}\rangle_{\natural}} = 1$). So $\varepsilon$ is an invariant bilinear form on each chiral half separately.

**Nondegeneracy and self-duality.** The matrix $\epsilon$ is invertible, so $\varepsilon$ is nondegenerate; equivalently, $\psi = 0$ if $\varepsilon(\psi,\phi) = 0$ for all $\phi$. The map $\psi\mapsto\varepsilon(\psi,\cdot)$ is an isomorphism $S\to S^{*}$ intertwining the two actions, so

$$
S^{*}\cong S .
$$

This is the self-duality of the defining module. It is **not** self-conjugacy: $\bar{S}\not\cong S$ as complex $SL(2,\mathbb{C})$-modules. The distinction is the parent's warning that "self-duality is not self-conjugacy", and it is why a pair of left-handed spinors has an invariant antisymmetric contraction while a left- and a right-handed spinor need the separate mixed pairing $\mathfrak{b}$.

**Concrete check.** For a boost along $\vec u_z$ and $\psi = (1,0)^{T}$, $\phi = (0,1)^{T}$, one has $\varepsilon(\psi,\phi) = 1$, while $\varepsilon(g\psi,g\phi) = \exp(\psi/2)\exp(-\psi/2) = 1$. The identity $g^{T}\epsilon g = \epsilon$ was verified numerically for boosts, rotations, and random unit-norm biquaternions, residual $<10^{-12}$.

## Problem 5: The Spinor Bilinear and the Four-Vector

The parent article introduces the bilinear

$$
\tilde{Q} = w\,v^{\dagger}, \qquad w,v\in S,
$$

and shows that its matrix representative $X=\mathsf{M}_2(\tilde{Q})$ transforms as $X\mapsto gXg^{\dagger}$. This is immediate: $(gw)(gv)^{\dagger} = g\,wv^{\dagger}\,g^{\dagger}$.

**Hermiticity and the general four-vector map.** The matrix $\tilde{Q} = wv^{\dagger}$ is Hermitian if and only if $w$ and $v$ are proportional by a real factor; in general it is a rank-one element of the full algebra $\mathbb{B}$, not of the Hermitian subspace. The bilinear that lands in the Hermitian subspace $\mathbb{M}_+$ (real dimension four) is the **Hermitian part**

$$
H(w,v) = \tfrac12\left(w\,v^{\dagger} + v\,w^{\dagger}\right) \in \mathbb{M}_+ .
$$

For $v = \pm w$ this reduces to $H = \pm ww^{\dagger}$, and the parent's unsymmetrized $\tilde{Q} = wv^{\dagger}$ is then already Hermitian. In general one must symmetrize. The four-vector associated with the spinor pair is

$$
V(w,v) = i\,H(w,v) \in \mathbb{M}_- ,
$$

where the last inclusion uses $i\mathbb{M}_+ = \mathbb{M}_-$.

**Biquaternion norm.** Write $H = h_te_t + i\vec h$. Then $V = ih_te_t - \vec h$, and

$$
\langle V\rangle_{\natural} = \langle iH\rangle_{\natural} = -\det\mathsf{M}_2(H) = -h_t^2 + \vec h^2 \qquad(\vec h^2=|\vec h|^2),
$$

which is the $(3,1)$ Minkowski form of $\mathbb{M}_-$. Two independent checks: for $w = v$ one has $H = ww^{\dagger}$, which is rank one, so $\det H = 0$ and

$$
\langle V\rangle_{\natural} = 0 .
$$

A single spinor therefore determines a **null** four-vector — its flag direction.

**Explicit example.** Take $w = v = (1,0)^{T}$. Then $ww^{\dagger} = \operatorname{diag}(1,0) = \tfrac12(I_2+\sigma_3)$, so

$$
H = \tfrac12 e_t + \tfrac{i}{2} \vec e_z, \qquad V = iH = \tfrac{i}{2}e_t - \tfrac12 \vec e_z,
$$

with components $(q_t,q_x,q_y,q_z) = (\tfrac12,0,0,-\tfrac12)$ in the basis $\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$ and norm $\langle V\rangle_{\natural} = -\tfrac14+\tfrac14 = 0$ (numerical residual $<10^{-15}$). This is the content of the parent's factorization $(\tfrac12,\tfrac12) = (\tfrac12,0)\otimes(0,\tfrac12)$: the four-vector is a bilinear in one left-handed and one right-handed spinor.

## Problem 6: The Double Cover on a Concrete Rotation

Take a rotation about $\vec u_{\mathrm r} = \vec u_z$ by angle $\theta$,

$$
\tilde u_{\mathrm r}(\theta) = \cos\frac{\theta}{2}\,e_t + \sin\frac{\theta}{2}\,\vec u_z,
\qquad
\mathsf{M}_2(\tilde u_{\mathrm r}(\theta)) = \operatorname{diag}\!\left(\exp(-i\theta/2), \exp(i\theta/2)\right).
$$

**On the spinor.** At $\theta = 2\pi$,

$$
\mathsf{M}_2(\tilde u_{\mathrm r}(2\pi)) = \operatorname{diag}\!\left(\exp(-i\pi), \exp(i\pi)\right) = \operatorname{diag}(-1,-1) = -I_2 ,
$$

so every spinor is sent to its negative: $\psi\mapsto-\psi$, which is not the identity. At $\theta = 4\pi$,

$$
\mathsf{M}_2(\tilde u_{\mathrm r}(4\pi)) = \operatorname{diag}\!\left(\exp(-2\pi i), \exp(2\pi i)\right) = I_2 ,
$$

so the spinor returns to itself.

**On the four-vector.** The corresponding four-vector action is rotor conjugation by $\tilde u_{\mathrm r}(\theta)$. At $\theta = 2\pi$ the rotor is $\tilde u_{\mathrm r}(2\pi) = \cos\pi\,e_t = -e_t$, and

$$
(-e_t)\,\tilde{Q}\,(-e_t)^{*} = (-e_t)\,\tilde{Q}\,(-e_t) = e_t\,\tilde{Q}\,e_t = \tilde{Q},
$$

using $(-e_t)^{*} = -e_t$. So a $2\pi$ rotation acts as $+\mathrm{id}$ on every four-vector. At $\theta = 4\pi$ the rotor is $+e_t$ and both actions are the identity.

**The general statement.** The two behaviours are the two entries of the parent's table:

$$
\pi:\;SL(2,\mathbb{C})\longrightarrow SO^{+}(1,3), \qquad
\ker\pi = \{\pm e_t\}\cong\mathbb{Z}/2\mathbb{Z},
$$

while the spinor action $\psi\mapsto\tilde U^{\mathrm{lor}}\psi$ has trivial kernel: $\mathsf{M}_2(-e_t) = -I_2\neq I_2$. Hence

$$
\boxed{\;SO^{+}(1,3)\cong SL(2,\mathbb{C})/\{\pm e_t\}\;},
$$

and $SL(2,\mathbb{C})$ is the double cover. Numerically, for $\vec u_{\mathrm r} = \vec u_z$ and $\theta = 2\pi$, the residual of $\mathsf{M}_2(\tilde u_{\mathrm r}(2\pi))+I_2$ is $<10^{-15}$, and that of the four-vector conjugation against the identity is $<10^{-12}$.

## Problem 7: The Spinor Action and Rotor Conjugation

**From the one-sided action to the two-sided action.** Let $w,v\in S$ and form $V = V(w,v) = i\cdot\tfrac12(wv^{\dagger}+vw^{\dagger})\in\mathbb{M}_-$. Under the spinor action $w\mapsto gw$, $v\mapsto gv$, the bilinear transforms as

$$
V \;\longmapsto\; g\,V\,g^{\dagger} = \mathsf{M}_2\!\left(\tilde U^{\mathrm{lor}}\,V\,\tilde U^{\mathrm{lor}}{}^{*}\right),
$$

which is exactly the rotor conjugation of the material sector. A single spinor contributes one factor, $\psi\mapsto g\psi$ (linear, one-sided); the four-vector is built from two spinors and therefore carries two factors, $gVg^{\dagger}$ (quadratic, two-sided). This is the origin of the difference in kind between the two actions, and it is the sense in which the four-vector is a *pair* of spinors.

**The sign that cancels and the sign that does not.** Replace $\tilde U^{\mathrm{lor}}$ by $-\tilde U^{\mathrm{lor}}$, i.e. $g$ by $-g$. On four-vectors $(-g)V(-g)^{\dagger} = gVg^{\dagger}$, because the two signs cancel; on spinors $(-g)\psi = -g\psi\neq g\psi$ for every nonzero spinor. Hence $\ker\pi = \{\pm e_t\}$ on $\mathbb{M}_-$ but the kernel of the spinor action is trivial: the spinor representation does not descend to $SO^{+}(1,3)$.

**Composition.** Successive rotors compose by multiplication in both pictures: $\tilde U^{\mathrm{lor}}_{2}(\tilde U^{\mathrm{lor}}_{1}\psi) = (\tilde U^{\mathrm{lor}}_{2}\tilde U^{\mathrm{lor}}_{1})\psi$ and $\tilde U^{\mathrm{lor}}_{2}(\tilde U^{\mathrm{lor}}_{1}V\tilde U^{\mathrm{lor}}_{1}{}^{*})\tilde U^{\mathrm{lor}}_{2}{}^{*} = (\tilde U^{\mathrm{lor}}_{2}\tilde U^{\mathrm{lor}}_{1})V(\tilde U^{\mathrm{lor}}_{2}\tilde U^{\mathrm{lor}}_{1})^{*}$. The difference is only the doubled factor, and hence the cancelling sign, in the four-vector formula.

**The mixed pairing.** Finally, the pairing $\mathfrak{b}(\psi,\chi) = \psi^{\dagger}\chi$ on $S\times\bar{S}$, with $\psi\mapsto g\psi$ and $\chi\mapsto\mathsf{M}_2\big(\bar{\tilde U}^{\mathrm{lor}}\big)\chi$, is invariant:

$$
\boxed{\;\mathfrak{b}\left(g\psi,\mathsf{M}_2\big(\bar{\tilde U}^{\mathrm{lor}}\big)\chi\right)
= \psi^{\dagger}g^{\dagger}\mathsf{M}_2\big(\bar{\tilde U}^{\mathrm{lor}}\big)\chi
= \psi^{\dagger}g^{\dagger}\,(g^{\dagger})^{-1}\chi
= \psi^{\dagger}\chi\;},
$$

because the conjugate of a unit-norm biquaternion is again of unit norm, $\bar{\tilde U}^{\mathrm{lor}}(\bar{\tilde U}^{\mathrm{lor}})^{\natural}=e_t$, so that the right-handed matrix is the inverse conjugate transpose, $\mathsf{M}_2\big(\bar{\tilde U}^{\mathrm{lor}}\big) = (g^{\dagger})^{-1} = \epsilon^{-1}\bar{g}\epsilon = \epsilon\bar{g}\epsilon^{-1}$. The action is not the Hermitian-star one, $\chi\mapsto\mathsf{M}_2(\tilde U^{\mathrm{lor}}{}^{*})\chi = g^{\dagger}\chi$: with $g^{\dagger}$ in place of $(g^{\dagger})^{-1}$ the pairing would read $\psi^{\dagger}(g^{\dagger})^{2}\chi$, and it would be invariant only when $g$ is unitary. This is the Dirac scalar bilinear (numerical residual $<10^{-12}$).

## Limiting Cases

The solutions have the expected limits.

- **Rapidity limits.** As $\psi\to0$ both halves become indistinguishable, reflecting that the chiral splitting is a property of the full Lorentz group, not of its compact subgroup; for large $\psi$ the halves diverge exponentially, one component of each growing as $\exp(\psi/2)$ and the other decaying as $\exp(-\psi/2)$.
- **$v = \pm w$ (single spinor):** $H = \pm ww^{\dagger}$ is rank one, so $V$ is null. For a generic pair, $V$ is timelike or spacelike according to the sign of $\langle V\rangle_{\natural} = -h_t^2+\vec h^2$.
- **$\theta = 2\pi$ versus $4\pi$:** the spinor picks up $-1$ at $2\pi$ and returns at $4\pi$, while the four-vector is unchanged at both — the double cover in its simplest instance.

## What the Solutions Illustrate

**1. The parent's structures are sufficient, once the module is made explicit.** All seven problems use only $S$, its conjugate $\bar{S}$, the realization $\mathsf{M}_2$, and the two pairings. The only extra structure is the chirality operator on the Dirac module, which is external to the simple algebra $\mathbb{B}$.

**2. Chirality is a real-structure notion.** The two halves are invisible to $\mathbb{B}$ as a complex algebra, where both minimal left ideals are copies of $S$; they become visible only through the conjugate module and the complexification, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$.

**3. The four-vector is the bilinear shadow of the spinor.** Rotor conjugation on $\mathbb{M}_-$ arises from the one-sided spinor action through the Hermitian bilinear $H(w,v)$; the vector representation is the tensor product of the two chiral halves.

**4. The double cover is a kernel statement.** $\ker\pi = \{\pm e_t\}$ on the four-vectors, but trivial on the spinors; the difference is one factor of $g$ versus two.

## Notes on the Parent Article

Three points arose where the parent either leaves a definition to convention or uses a shorthand that is not general. They are recorded here as findings; the choices used above are stated explicitly.

1. **Right-handed action, exact form.** The parent says the right-handed action is "equivalent to the entrywise-conjugate action $g\mapsto\bar{g}$ (the two differ by conjugation with the invariant tensor $\epsilon$)"; it does not give the identity. The precise identity is $\mathsf{M}_2(\bar{\tilde U}^{\mathrm{lor}}) = \epsilon^{-1}\bar{g}\epsilon = \epsilon\bar{g}\epsilon^{-1} = (g^{\dagger})^{-1}$, verified numerically. Two points of notation had to be settled for it. The conjugation that carries the conjugate representation is the **coefficientwise** one, $\bar{\tilde U}^{\mathrm{lor}} = (\tilde U^{\mathrm{lor}}{}^{*})^{\natural}$; the star by itself is the Hermitian conjugation and gives $g^{\dagger}$, which is the transpose of the conjugate rather than the inverse. And the inverse is what the module needs, since only $(g^{\dagger})^{-1}$ leaves the pairing $\psi^{\dagger}\chi$ invariant. The orientation of $\epsilon$ in the identity is a convention.

2. **The spinor-to-vector map for a general pair.** The parent writes $\tilde{Q} = uv^{\dagger}$ (its $u,v$ are the $w,v$ used here) and warns that for a generic pair $iuv^{\dagger}$ does not lie in $\mathbb{M}_-$ and is therefore not a four-vector; it then supplies the symmetrised map $H = \tfrac12(wv^{\dagger}+vw^{\dagger})\in\mathbb{M}_+$, with four-vector image $V = iH\in\mathbb{M}_-$. The exercise uses that symmetrised map. The shorthand $\tilde{Q} = wv^{\dagger}$ is general, but the identification of $i\tilde{Q}$ with a four-vector is not.

3. **The biquaternion mass term and the conjugate module.** The parent's massive equation is the linear, chirality-off-diagonal pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$, whose mass term couples the two chiral halves, with the anti-Hermitian conjugation $\tilde{\Psi}^{\flat} = -\tilde{\Psi}^{*}$ the algebra's real structure rather than the mass. The exercise keeps its mass term in the explicit Dirac module, where it is unambiguous. The parent exhibits neither $\bar{S}$ inside $\mathbb{B}$ nor the isomorphism between the left-regular module $\mathbb{B}\cong S\oplus S$ and the Dirac module $S\oplus\bar{S}$.

A fourth point, the biquaternion (ideal) form of the symplectic pairing, is the parent's open question 3; the exercise uses the matrix-coordinate form throughout, which is the form the parent defines.

## The Legacy Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

On the chiral pair $(\psi_L,\psi_R)$, with the left-handed block first, the same five objects are the matrices

$$
\gamma_0=\begin{pmatrix}0&I_2\\I_2&0\end{pmatrix},\qquad
\gamma_k=\begin{pmatrix}0&\sigma_k\\-\sigma_k&0\end{pmatrix},\qquad
\gamma_5=\begin{pmatrix}-I_2&0\\0&I_2\end{pmatrix},
$$

where $\sigma_k$ is the matrix of $i\vec e_k$, and these are the Peirce arrays. In the axis-free display, which is the display of the body, the same five are
$$
\gamma_0=\begin{pmatrix}0&-i&0&0\\i&0&0&0\\0&0&0&i\\0&0&-i&0\end{pmatrix},\qquad
\gamma_1=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&-i&0&0\\i&0&0&0\end{pmatrix},
$$
$$
\gamma_2=\begin{pmatrix}-i&0&0&0\\0&i&0&0\\0&0&-i&0\\0&0&0&i\end{pmatrix},\qquad
\gamma_3=\begin{pmatrix}0&-i&0&0\\-i&0&0&0\\0&0&0&-i\\0&0&-i&0\end{pmatrix},\qquad
\gamma_5=\begin{pmatrix}0&0&0&i\\0&0&-i&0\\0&i&0&0\\-i&0&0&0\end{pmatrix},
$$
the signed permutations $\gamma_0=iR_{\vec e_x}^{\mathrm{axf}}$ and $\gamma_k=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_{\nu(k)}}^{\mathrm{axf}}$, carried into the Peirce arrays by $C_{\Pi}$. These are the arrays of the four coordinate cells $C_\mu$ of Problem 2, $\gamma_0=C_t$ and $\gamma_k=C_k$, together with the chirality cell $\gamma_5$.

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The standard identities.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$:

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

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

Seven problems were solved. (1) The chiral projectors $P_L = \tfrac12(I_4-\Gamma)$, $P_R = \tfrac12(I_4+\Gamma)$, with $\Gamma = \operatorname{diag}(-I_2,I_2)$ on $\Delta = S\oplus\bar{S}$, satisfy the projector algebra and commute with the Lorentz action. (2) The massless Dirac equation splits into two independent Weyl equations; the mass term couples them, and each half obeys $(\Box-m^2)\psi = 0$, with mass shell $k_0^2 = \vec k^2+m^2c^2/\hbar^2$. The one-sided chiral pair is one of the two Dirac equations of the corpus; the two-sided form carries the same chirality coupling in a single equation, with the mass term a conjugation together with a right multiplication by $\vec e_z$. (3) Under a boost along $\vec u_z$ the halves transform by inverse matrices $g_{\text{boost}} = \operatorname{diag}(\exp(\psi/2),\exp(-\psi/2))$ and $g_{\text{boost}}^{-1}$; under a rotation both transform by $g_{\text{rot}} = \operatorname{diag}(\exp(-i\theta/2),\exp(i\theta/2))$; in general $\mathsf{M}_2(\bar{\tilde U}^{\mathrm{lor}}) = \epsilon^{-1}\bar{g}\epsilon$. (4) The symplectic form $\varepsilon(\psi,\phi) = \psi^{T}\epsilon\phi$ is invariant because $g^{T}\epsilon g = (\det g)\epsilon = \epsilon$, is nondegenerate, and gives $S^{*}\cong S$, but is not self-conjugacy. (5) The spinor bilinear gives $V = i\cdot\tfrac12(wv^{\dagger}+vw^{\dagger})\in\mathbb{M}_-$, transforming by rotor conjugation $\tilde U^{\mathrm{lor}}V\tilde U^{\mathrm{lor}}{}^{*}$; a single spinor gives a null four-vector, and the vector representation is the tensor product of the chiral halves. (6) A $2\pi$ rotation acts as $-I_2$ on spinors and as the identity on four-vectors, and a $4\pi$ rotation as the identity on both: the double cover $SO^{+}(1,3)\cong SL(2,\mathbb{C})/\{\pm e_t\}$. (7) The two-sided four-vector action is the bilinear shadow of the one-sided spinor action; the sign cancels in the former but not in the latter, and the mixed pairing $\mathfrak{b}(\psi,\chi) = \psi^{\dagger}\chi$ is invariant.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$, $\vec e_x \vec e_y = \vec e_z$ |
| $\mathbb{C}_{\mathbb{B}}, \mathbb{H}_{\mathbb{B}}$ | Complex subspace (centre), real-quaternion subspace |
| $\mathbb{M}_-, \mathbb{M}_+$ | Anti-Hermitian (material), Hermitian (informational) subspaces |
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | Matrix realization, $\mathsf{M}_2(\vec e_k) = -i\sigma_k$, $\mathsf{M}_2(i) = iI_2$ |
| $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \det\mathsf{M}_2(\tilde{Q})$ | Biquaternion norm |
| $S = \mathbb{C}^2$, $\bar{S}$ | Spinor module, conjugate (right-handed) module |
| $V_1 = (\tfrac12,0)$, $\bar{S} = (0,\tfrac12)$ | Left- and right-handed Weyl modules |
| $\Delta = S\oplus\bar{S}$ | Dirac module, $\dim_{\mathbb{C}}\Delta = 4$ |
| $\tilde\Pi_+ = \tfrac12(e_t+i\vec e_z),\; \tilde\Pi_- = \tfrac12(e_t-i\vec e_z)$ | Primitive orthogonal idempotents |
| $\Gamma = \operatorname{diag}(-I_2,I_2)$ | Chirality operator on $\Delta$ |
| $P_L = \tfrac12(I_4-\Gamma),\; P_R = \tfrac12(I_4+\Gamma)$ | Chiral projectors |
| $C_t=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=iR_{\vec e_x}^{\mathrm{axf}}$, $C_k=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | The four generator cells of the reference frame |
| $D_3=\sum_k\vec e_k\,\partial/\partial Q_k$ | Three-dimensional Cauchy–Riemann operator of the two-sided equation |
| $\psi_L\in S$, $\psi_R\in\bar{S}$ | Left- and right-handed Weyl spinors |
| $\tilde U_{\mathrm b} = \cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ | Boost rotor ($\mathbb{M}_+$) |
| $\tilde u_{\mathrm r} = \cos\frac{\theta}{2}+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ | Rotation rotor ($\mathbb{H}_{\mathbb{B}}$) |
| $g = \mathsf{M}_2(\tilde U^{\mathrm{lor}})$ | Defining (left-handed) action matrix |
| $\mathsf{M}_2(\bar{\tilde U}^{\mathrm{lor}}) = \epsilon^{-1}\bar{g}\epsilon$ | Right-handed action matrix |
| $\varepsilon(\psi,\phi) = \psi^{T}\epsilon\phi$ | Invariant symplectic pairing on $S$ |
| $\mathfrak{b}(\psi,\chi) = \psi^{\dagger}\chi$ | Invariant pairing $S\times\bar{S}\to\mathbb{C}$ |
| $V = i\cdot\tfrac12(wv^{\dagger}+vw^{\dagger})$ | Four-vector from a spinor pair |
| $SL(2,\mathbb{C})$, $\pi$ | Unit-norm biquaternions; double cover of $SO^{+}(1,3)$ |

## Further Reading

- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component spinor calculus, the invariant $\epsilon$-form, and the Weyl spinors.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of the Lorentz group and the relation between spinors and four-vectors.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the construction of the Dirac spinor from two Weyl spinors and the mass term.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the modules of $M_2(\mathbb{C})$, the highest-weight classification, and the Clebsch–Gordan rule.
- The companion articles of this series: [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html), [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), and [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html).
