# __The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit__

## Introduction

The companion article *The Dirac Equation in Biquaternionic Form* stated the biquaternionic Dirac equation as a chiral pair,

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L,
$$

$$
\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R,
$$

with massless limit $\tilde\nabla\tilde\Psi_R = 0$, $\tilde\nabla^{\natural}\tilde\Psi_L = 0$ and Klein–Gordon reduction $(\Box - m^2c^2/\hbar^2)\tilde{\Psi} = 0$. It fixed the algebraic setting: the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ as the even subalgebra of the Clifford algebra, the biquaternionic gradient $\tilde{\nabla} = e_t\partial/\partial Q_t + \sum_\mu\vec e_\mu\partial/\partial Q_\mu$ as the biquaternion form of the Dirac operator, and the action of the pair on the spinor module of $\mathbb{B}$. It fixed the plane-wave ansatz too, $\tilde{\Psi} = \tilde{\Psi}_0\exp\!\left(i\,\mathrm{Sc}(\tilde P\tilde{Q}^{\natural})/\hbar\right)$, with the mass-shell condition $\tilde P\tilde P^{\natural}=-m^2c^2$. It closed by noting that the massive solution space is four-dimensional over $\mathbb{C}$, the four components of the Dirac spinor.

That article worked at a summary level. It identified the solution classes and the mass-shell condition, but it constructed no explicit spinor, fixed no normalization, wrote no bilinear, and did not carry the equation into the non-relativistic regime. The present article supplies those four things.

The next section fixes the cells, the two spinor bases and the two metrics. The following section states the two equations and describes the field. The section after that constructs the plane-wave solutions in full, separating the positive- and the negative-frequency branches and displaying the spinor structure in both bases. The next section treats orthogonality and normalization and records the spin sums. The next gives the biquaternion form of the spinor bilinears. The longest section performs the non-relativistic limit, reduces the equation to the Pauli equation, exhibits the two-component spinor, and shows how the gyromagnetic factor and the spin–magnetic coupling emerge. A short section records the massless case and chirality; a final section collects the gammas as one frame of the cell algebra.

The material here is the declared foundation for two of the later exercises, *Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation* and *Exercise: The Non-Relativistic Limit and the Pauli Equation*. The solutions and the limiting procedure are therefore worked out explicitly, with the intermediate steps those exercises need.

## The cells, the two bases and the two metrics

Every generator used in this article is a cell, a product of a left and a right multiplication. Write

$$
L_a\psi=a\psi,\qquad R_b\psi=\psi b,\qquad L_aR_b\psi=a\psi b,\qquad L_aR_bL_cR_d=L_{ac}R_{db},
$$

so that a cell prints both sides at once. A column of four components is the same biquaternion read in the cell frame, not a second object; the algebra element is primary. A squared three-vector such as $\vec p^2$ is always the Euclidean square $p_1^2+p_2^2+p_3^2$, never a quaternion square.

The biquaternion algebra is represented on $\mathbb{C}^2$ by

$$
e_t \mapsto I_2, \qquad \vec e_k \mapsto -i\sigma_k, \qquad i \mapsto i I_2,
$$

so that $i \vec e_k \leftrightarrow \sigma_k$. The factor $i$ is part of the dictionary: $\vec e_k$ alone is anti-Hermitian, and $i\vec e_k$ is the Hermitian $\sigma_k$.

The five cells of the frame, defined by their action on the state, are

$$
iR_{\vec e_x}\psi = i\,e_t\,\psi\,\vec e_x, \qquad
iL_{\vec e_k}R_{\vec e_y}\psi = i\,\vec e_k\,\psi\,\vec e_y, \qquad
-iR_{\vec e_z}\psi = -i\,e_t\,\psi\,\vec e_z .
$$

Since $L_{e_t}$ is the identity, these are $iL_{e_t}R_{\vec e_x}$, $iL_{\vec e_k}R_{\vec e_y}$ and $-iL_{e_t}R_{\vec e_z}$. The cells of the four coordinates are then

$$
\Gamma_0=iL_{e_t}R_{\vec e_x},\qquad \Gamma_k=iL_{\vec e_k}R_{\vec e_y},\qquad k=x,y,z,
$$

so the time cell is $\Gamma_0=iR_{\vec e_x}$ and the space cells are $\Gamma_k=iL_{\vec e_k}R_{\vec e_y}$.

**Each square is one use of $i^2=-1$.** From $i^2=-1$ and $\vec e_x^2=\vec e_y^2=-e_t$,

$$
(iR_{\vec e_x})^2=i^2L_{e_t}R_{\vec e_x^2}=(-1)L_{e_t}R_{-e_t}=L_{e_t}R_{e_t},
$$

$$
(iL_{\vec e_k}R_{\vec e_y})^2=i^2L_{\vec e_k^2}R_{\vec e_y^2}=(-1)L_{-e_t}R_{-e_t}=-L_{e_t}R_{e_t}.
$$

The mixed products anticommute: in a time–space pair the left factor $e_t$ commutes with every unit while the right factors $\vec e_x$ and $\vec e_y$ anticommute, and in a space–space pair the right factor $\vec e_y$ is common to both while the left factors $\vec e_k$ anticommute. Hence

$$
\{\Gamma_\mu,\Gamma_\nu\} = 2g_{\mu\nu}L_{e_t}R_{e_t}, \qquad g = \mathrm{diag}(+1,-1,-1,-1),
$$

the metric sign being the convention noted in the companion article.

**The two bases.** The frame above is the **chiral (Weyl) basis**. The chirality is the cell $-iR_{\vec e_z}=-iL_{e_t}R_{\vec e_z}$; on the Peirce planes $\mathbb{B}\tilde\Pi_\pm$, with $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$, it acts as $-1$ on $\mathbb{B}\tilde\Pi_+$ and as $+1$ on $\mathbb{B}\tilde\Pi_-$, so the upper two-component block is left-handed and the lower is right-handed. The **Dirac basis** is obtained by the $*$-unitary change of basis $R_{\tilde W}$ with $\tilde W=(e_t+\vec e_y)/\sqrt2$. It diagonalizes the timelike cell $\Gamma_0=iR_{\vec e_x}$, which becomes $+1$ on the upper block and $-1$ on the lower, and it mixes the two chiralities. The plane-wave spinors are simplest in the Dirac basis; the massless equations are simplest in the chiral one.

**The two metrics, and the two sectors.** Two metric symbols appear, and they carry the same information with opposite sign. The Clifford metric $g=\mathrm{diag}(+1,-1,-1,-1)$ is the one in the anticommutator of the cells. The spacetime metric $\eta=\mathrm{diag}(-1,+1,+1,+1)$ is its negative, $\eta=-g$, and it is the metric of the $ict'$ gradient. The relative sign is the freedom the companion article flags as convention.

Two sectors recur. The material sector $\mathbb{M}_-$ is the anti-Hermitian part of $\mathbb{B}$, the fixed space of $\flat$; the informational sector $\mathbb{M}_+$ is its Hermitian partner, and it is where the spin observables of this article live.

On the momentum cell the sign difference of the two metrics is the relative minus between the time and the space terms. With $p_0=E$ and $\vec p=(p_1,p_2,p_3)$,

$$
P=\Gamma_0p_0-\sum_k\Gamma_kp_k=iR_{\vec e_x}E-\sum_k iL_{\vec e_k}R_{\vec e_y}p_k .
$$

The square follows from the two squares above and from the anticommutation of the cells; the cross terms cancel because the components commute,

$$
P^2=\Gamma_0^2p_0^2+\sum_k\Gamma_k^2p_k^2=p_0^2-\vec p^2 .
$$

The last expression is $g^{\mu\nu}p_\mu p_\nu$, and equally $-\eta^{\mu\nu}p_\mu p_\nu$; the two metrics differ only in which of them carries the minus.

On derivatives the same cells give the wave operator of the material sector. On a plane wave $p_0\to i\partial/\partial t'$ and $p_k\to-i\partial/\partial Q_k$, so $P\to\slashed p$ with

$$
\slashed p=i\Gamma_0\,\partial/\partial t'+\sum_k i\Gamma_k\,\partial/\partial Q_k,
\qquad
\slashed p^2=-\Gamma_0^2\frac{\partial^2}{\partial {t'}^2}-\sum_k\Gamma_k^2\frac{\partial^2}{\partial Q_k^2}
=\Delta-\frac{\partial^2}{\partial {t'}^2}
=\Box\big|_{\mathbb{M}_-}.
$$

Since $Q_k=x,y,z$, the two writings $\partial/\partial Q_k$ and $\partial/\partial x_k$ name the same derivative, and the display is $\slashed p=i\Gamma_\mu\partial_\mu$ with $\partial_\mu=(\partial_{t'},\partial_x,\partial_y,\partial_z)$. No sign enters beyond $i^2=-1$ and the two cell squares.

A reader who prefers to attach $\eta$ to the generators multiplies the frame by $i$. Since $i^2=-1$,

$$
i\Gamma_0=i^2L_{e_t}R_{\vec e_x}=-L_{e_t}R_{\vec e_x},\qquad
i\Gamma_k=i^2L_{\vec e_k}R_{\vec e_y}=-L_{\vec e_k}R_{\vec e_y},
$$

and the anticommutator flips sign,

$$
\{i\Gamma_\mu,i\Gamma_\nu\}=2\eta_{\mu\nu}L_{e_t}R_{e_t}.
$$

The physics is unchanged; only the placement of the signs differs.

In the sections that construct the solutions we use natural units $\hbar = c = 1$; the dimensionally explicit forms are given where they carry physical meaning, namely in the mass-shell relation, in the Pauli equation and in the Weyl equations.

## The Dirac field and the Dirac adjoint

**The two equations.** In the algebra the biquaternionic Dirac equation is the chiral pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L,
$$

$$
\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R,
$$

with massless limit $\tilde\nabla\tilde\Psi_R=0$, $\tilde\nabla^{\natural}\tilde\Psi_L=0$. The two lines are two distinct equations: the first acts on the right-handed half and the second on the left-handed half, and the second carries the conjugate gradient $\tilde{\nabla}^{\natural}$ because the left-handed half is the conjugate representation of the right-handed one. The pair is **one-sided**: both gradients act on the left, and the mass is the off-diagonal pairing of the two chiral halves. The companion article also records a **two-sided** form of the same physics, a single equation on the whole algebra in which the mass acts from the right through a spatial unit and a componentwise conjugation supplies an antilinear part. The two forms are related by a change of representation, but they are different operators, and the solutions below are those of the one-sided pair; the two-sided equation is not used here.

**The field.** On the spinor module the pair acts on a four-component column $\psi$; the two equations it becomes are the dynamics. A biquaternion has four complex components; in the chiral frame they split into the two Weyl spinors,

$$
\psi=\begin{pmatrix}\psi_L\\ \psi_R\end{pmatrix},\qquad \psi_L,\psi_R\in\mathbb{C}^2 .
$$

The biquaternion field $\tilde{\Psi}$ of the companion article is the algebra-level representative of this column: the element of $\mathbb{B}\cong M_2(\mathbb{C})$ read in the cell frame. The Dirac operator on the column is the carrier form $\slashed p$ of the algebra-level $\tilde{\nabla}$, and it is the operator whose plane-wave solutions are constructed below. The mass of the companion article is the linear, chirality-off-diagonal coupling of the pair — the algebra-level representative of the spinor mass term. The conjugation $\tilde{\Psi}^\flat=-\tilde{\Psi}^{*}$ is a separate object, the algebra's real structure (the fixed space of $\flat$ is $\mathbb{M}_-$), and is *not* the mass term.

The two bases fixed above are the ones used throughout: the chiral basis for the massless case, and the Dirac basis, where $\Gamma_0=iR_{\vec e_x}=\beta$ is diagonal and the upper and lower blocks play the parts of the large and the small component in the non-relativistic limit. The plane-wave solutions below are given in both.

The Dirac adjoint is the Hermitian pairing twisted by the timelike cell,

$$
\bar{\psi}\phi = \langle\psi,\phi\rangle_{\mathrm D} = \mathrm{Tr}\bigl(\tilde\Psi^{*}\tilde\Phi\,i\vec e_x\bigr)
= \psi_L^\dagger\phi_R + \psi_R^\dagger\phi_L ,
$$

so that $\bar{\psi}\psi$ is a Lorentz scalar. The amplitude equation for a plane wave follows by substituting; we carry this out in the next section.

## Plane-wave solutions

### Positive-frequency branch

Take the positive-frequency plane wave

$$
\psi(x) = w(\vec p)\, \exp(-i(Et' - \vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z))), \qquad E = +\sqrt{\vec p^2 + m^2},
$$

where $w(\vec p)$ is a four-component constant spinor. Substituting into the pair gives the single four-component equation

$$
(P-m)\,w(\vec p)=0,\qquad P=iR_{\vec e_x}E-\sum_k iL_{\vec e_k}R_{\vec e_y}p_k ,
$$

with the momentum cell $P$ defined in the cells section. The four-component equation is the pair written once; the pair itself is the statement in the algebra, and in the chiral basis it splits into the two equations

$$
(E-\boldsymbol{\sigma}\cdot\vec p)\,w_R=m\,w_L,\qquad
(E+\boldsymbol{\sigma}\cdot\vec p)\,w_L=m\,w_R ,
$$

one for each chirality. Eliminating $w_L$ or $w_R$ gives the mass-shell condition $E^2-\vec p^2=m^2$, which is $P^2=m^2$.

The spinor structure is most transparent in the **Dirac basis**. Writing $w = (w_A, w_B)$ with $w_A, w_B \in \mathbb{C}^2$, the momentum-space equation becomes the pair

$$
(E - m)\,w_A = \boldsymbol{\sigma}\cdot\vec p\, w_B, \qquad (E + m)\,w_B = \boldsymbol{\sigma}\cdot\vec p\, w_A,
$$

so that $w_B = \dfrac{\boldsymbol{\sigma}\cdot\vec p}{E+m} w_A$ and the upper component $w_A$ is free. With the covariant normalization, the two positive-energy solutions are

$$
\boxed{\;w^{(r)}(\vec p) = \begin{pmatrix} \sqrt{E+m}\,\xi^{(r)} \\[2pt] \sqrt{E-m}\,(\boldsymbol{\sigma}\cdot\vec u_p)\,\xi^{(r)} \end{pmatrix}, \qquad r = 1,2\;},
$$

where $\vec u_p = \vec p/|\vec p|$ and $\xi^{(1)}, \xi^{(2)}$ are the standard orthonormal two-spinors, $\xi^{(r)\dagger}\xi^{(s)} = \delta_{rs}$. At rest this reduces to $w^{(r)}(0) = \sqrt{2m}\begin{pmatrix}\xi^{(r)}\\ 0\end{pmatrix}$.

The same solutions in the **chiral basis** are indexed by helicity. Let $\chi_\pm$ be eigenspinors of the helicity operator,

$$
\boldsymbol{\sigma}\cdot\vec u_p\,\chi_\pm = \pm\,\chi_\pm ,
$$

with the upper sign of the paired symbols below attached to $\chi_+$. Then

$$
w_\pm(\vec p) = \begin{pmatrix} \sqrt{E \mp |\vec p|}\; \chi_\pm \\[2pt] \sqrt{E \pm |\vec p|}\; \chi_\pm \end{pmatrix},
$$

with the upper block left-handed and the lower block right-handed. The solution $w_+$ therefore has its small component in the left-handed block, and $w_-$ in the right-handed one. One checks directly that this satisfies $(P-m)w_\pm=0$. In the chiral pair the upper, left-handed equation is $(E\pm|\vec p|)\sqrt{E\mp|\vec p|} = m\sqrt{E\pm|\vec p|}$ and the lower, right-handed one is $(E\mp|\vec p|)\sqrt{E\pm|\vec p|} = m\sqrt{E\mp|\vec p|}$; both reduce to $E^2 - \vec p^2 = m^2$. At high energy the coefficient $\sqrt{E \mp |\vec p|}$ of the upper component tends to zero for the matching sign, so each helicity-eigenstate solution becomes dominated by a single chirality — the statement that a massless fermion has definite handedness. The two bases are related by a fixed $*$-unitary transformation, and the two spin states may equally be labelled by helicity or by the index $r$; the labelling is a convention.

The general positive-energy solution is an arbitrary linear combination $w = a_1 w^{(1)} + a_2 w^{(2)}$, so the positive-frequency solution space at fixed $\vec p$ is two-dimensional over $\mathbb{C}$.

### Negative-frequency branch

The negative-frequency plane waves are

$$
\psi(x) = v(\vec p)\, \exp(+i(Et' - \vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z))), \qquad E = +\sqrt{\vec p^2 + m^2}.
$$

Substituting gives the momentum-space equation

$$
(P+m)\,v(\vec p) = 0,
$$

with the same momentum cell $P$. In the Dirac basis the pair reads $(E+m)v_A = \boldsymbol{\sigma}\cdot\vec p\,v_B$ and $(E-m)v_B = \boldsymbol{\sigma}\cdot\vec p\,v_A$, and the two solutions are

$$
\boxed{\;v^{(r)}(\vec p) = \begin{pmatrix} \sqrt{E-m}\,(\boldsymbol{\sigma}\cdot\vec u_p)\,\eta^{(r)} \\[2pt] \sqrt{E+m}\,\eta^{(r)} \end{pmatrix}, \qquad r = 1,2\;},
$$

with $\eta^{(r)\dagger}\eta^{(s)} = \delta_{rs}$; at rest $v^{(r)}(0) = \sqrt{2m}\begin{pmatrix} 0 \\ \eta^{(r)} \end{pmatrix}$. The negative-frequency solution space is again two-dimensional. In the standard reading, these modes describe antiparticles: charge conjugation exchanges the $w$ family with the $v$ family, and with it the sign of the frequency. Together, then, the amplitude equations have a four-dimensional complex solution space at fixed $\vec p$, exactly as the companion article stated.

### The biquaternion mass shell

The plane-wave ansatz of the companion article, $\tilde{\Psi} = \tilde{\Psi}_0\exp\!\left(i\,\mathrm{Sc}(\tilde P\tilde{Q}^{\natural})/\hbar\right)$ with $\tilde Q=e_t\,ict'+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$, carries the wave biquaternion $\tilde{P}/\hbar$.

With the four-wavevector of the companion article written as $\tilde P/\hbar = i\omega/c\,e_t + \vec k$, the biquaternion norm is

$$
\langle\tilde P/\hbar\rangle_{\natural} = \tilde P\tilde P^{\natural}/\hbar^{2}
= \left[\left(\frac{i\omega}{c}\right)^2 + \vec k^2\right]e_t
= \left(-\frac{\omega^2}{c^2} + \vec k^2\right)e_t .
$$

The mass shell $\omega^2 = c^2\vec k^2 + m^2c^4/\hbar^2$, which is $E^2 = \vec p^2c^2 + m^2c^4$ under $E = \hbar\omega$, $\vec p = \hbar\vec k$, is therefore exactly the companion article's condition

$$
\tilde P\tilde P^{\natural}=-m^2c^2.
$$

The two roots $\omega = \pm\sqrt{c^2\vec k^2 + m^2c^4/\hbar^2}$ are the two frequency branches, so the positive- and negative-frequency solutions above are the two branches of the single biquaternionic mass-shell condition. The polarization equations $(i\tilde{P}/\hbar)\tilde{\Psi}_0^R = m\tilde{\Psi}_0^L$ and $(i\tilde{P}^{\natural}/\hbar)\tilde{\Psi}_0^L = m\tilde{\Psi}_0^R$ are the algebraic form of the momentum-space equation; their solution space is the four-dimensional space spanned by the $w^{(r)}$ and $v^{(r)}$ — two spin states for each of the two frequency branches.

### Spin structure and helicity

Two features of the spinor structure deserve emphasis, because the later exercises depend on them.

First, the **spin label**. The two independent solutions at fixed momentum can be chosen as eigenstates of any maximal commuting spin observable. The standard choices are the spin projection along a fixed axis (the two-spinor index $r$) and the helicity $\boldsymbol{\sigma}\cdot\vec u_p$ (the labels $\pm$). Helicity is the natural label for a massless particle, because it is then Lorentz invariant; for a massive particle it is frame-dependent, and the spin index $r$ is the more convenient label.

Second, the **chirality–helicity relation**. In the chiral basis, positive-helicity positive-energy states are dominated by the right-handed component and negative-helicity states by the left-handed component. This is the precise sense in which "massless fermions of definite helicity have definite chirality", and it is the bridge to the Weyl equations below.

## Orthogonality and normalization

The Dirac adjoint $\bar{w}\phi = \langle w,\phi\rangle_{\mathrm D}$ of the field section makes the bilinear $\bar{w}w$ a Lorentz scalar. A direct computation from the explicit solutions gives the normalization

$$
\bar{w}^{(r)}(\vec p)\,w^{(s)}(\vec p) = 2m\,\delta_{rs}, \qquad
\bar{v}^{(r)}(\vec p)\,v^{(s)}(\vec p) = -2m\,\delta_{rs},
$$

the relative minus sign being the standard signature of the negative-frequency branch. The cross terms vanish at equal momentum,

$$
\bar{w}^{(r)}(\vec p)\,v^{(s)}(\vec p) = 0,
$$

and the Hermitian (non-covariant) products are

$$
w^{(r)\dagger}(\vec p)\,w^{(s)}(\vec p) = 2E\,\delta_{rs}, \qquad
v^{(r)\dagger}(\vec p)\,v^{(s)}(\vec p) = 2E\,\delta_{rs}, \qquad
w^{(r)\dagger}(\vec p)\,v^{(s)}(-\vec p) = 0,
$$

the last relation requiring the opposite momentum, as usual. Three normalization conventions are in common use — $\bar{w}w = 2m$, $\bar{w}w = 1$, and $w^\dagger w = 1$ — and they differ by momentum-dependent factors; the covariant convention $\bar{w}w = 2m$ is the one used here, because it makes the spin sums below manifestly covariant.

The **spin sums** (completeness relations) close the solution set over the spin index:

$$
\sum_{r=1}^{2} w^{(r)}(\vec p)\,\langle w^{(r)}(\vec p),\,\cdot\,\rangle_{\mathrm D} = P + m, \qquad
\sum_{r=1}^{2} v^{(r)}(\vec p)\,\langle v^{(r)}(\vec p),\,\cdot\,\rangle_{\mathrm D} = P - m .
$$

These are the algebraic statement that the four solutions at fixed momentum form a basis of the amplitude space, and they are the ingredient that later exercises will need in order to sum over spins.

The **conserved current** of the Dirac field is

$$
j_\mu = \langle\psi,\Gamma_\mu\psi\rangle_{\mathrm D}, \qquad \mathrm{Sc}\bigl(\tilde\nabla^{\natural}\tilde J\bigr)=0,
$$

with $j_0= \psi^\dagger\psi \ge 0$ and real spatial components. The second statement is the continuity equation, and on the material sector it reads $\partial j_0/\partial t'+\nabla\cdot\vec j=0$. In the series' notation, the current is the four-vector biquaternion

$$
\tilde{J} = ic\,j_0\,e_t + \vec j \in \mathbb{M}_- ,
$$

with imaginary scalar part $ic\,j_0$ and real vector part $\vec j = (j^1,j^2,j^3)$. This is exactly the form required of a four-vector in the material sector $\mathbb{M}_-$: the Dirac current is a material-space object, as it must be.

## Spinor bilinears in biquaternion form

### The five bilinears

From a spinor and its adjoint one forms the standard bilinears, classified by their Lorentz character:

| Bilinear | Lorentz character |
|---|---|
| $\bar{\psi}\psi$ | scalar |
| $i\,\bar{\psi}\,(-iR_{\vec e_z})\psi$ | pseudoscalar |
| $\bar{\psi}\,\Gamma_\mu\psi$ | four-vector |
| $\bar{\psi}\,\Gamma_\mu(-iR_{\vec e_z})\psi$ | axial four-vector (pseudovector) |
| $\bar{\psi}\sigma_{\mu\nu}\psi$, $\ \sigma_{\mu\nu} = \tfrac{i}{2}[\Gamma_\mu,\Gamma_\nu]$ | antisymmetric rank-two tensor |

The pseudoscalar is written with the explicit factor of $i$ because, in the convention used here, $\bar{\psi}\,-iR_{\vec e_z}\psi$ is purely imaginary and $i\bar{\psi}\,-iR_{\vec e_z}\psi$ is real. The vector bilinear is the conserved current of the preceding section; the tensor bilinear governs the spin contribution to the current and, as shown below, the magnetic moment.

### The chiral components

In the chiral basis the bilinears separate into the two Weyl spinors, and the identities are worth recording because they are the ones the chirality exercise will use. With $\psi = (\psi_L,\psi_R)$ one has

$$
\bar{\psi}\psi = \psi_L^\dagger\psi_R + \psi_R^\dagger\psi_L = 2\,\mathrm{Re}\!\left(\psi_L^\dagger\psi_R\right),
$$

$$
\bar{\psi}\,-iR_{\vec e_z}\psi = \psi_L^\dagger\psi_R - \psi_R^\dagger\psi_L = 2i\,\mathrm{Im}\!\left(\psi_L^\dagger\psi_R\right),
$$

and the vector current has components

$$
j_0= \psi_L^\dagger\psi_L + \psi_R^\dagger\psi_R, \qquad
\vec j = -\,\psi_L^\dagger\boldsymbol{\sigma}\psi_L + \psi_R^\dagger\boldsymbol{\sigma}\psi_R .
$$

The axial current similarly has

$$
j_5^0 = \psi_R^\dagger\psi_R - \psi_L^\dagger\psi_L, \qquad
\vec j_5 = \psi_L^\dagger\boldsymbol{\sigma}\psi_L + \psi_R^\dagger\boldsymbol{\sigma}\psi_R .
$$

The scalar and pseudoscalar pair are seen to be the real and imaginary parts of the chirality-flipping bilinear $\psi_L^\dagger\psi_R$: a purely left-handed or purely right-handed field has $\bar{\psi}\psi = 0$. The vector and axial vector similarly recombine the same two Weyl currents with relative signs, which is the algebraic content of the chiral decomposition of the Dirac current.

### The spin bilinear and the informational sector

There is a second, distinct bilinear that is genuinely biquaternionic in character: the rank-one Hermitian form built from a single two-component spinor. For $\psi \in \mathbb{C}^2$ normalized by $\psi^\dagger\psi = 1$, define

$$
\rho = \psi\psi^\dagger = \tfrac{1}{2}\left(I_2 + \vec u\cdot\boldsymbol{\sigma}\right), \qquad
\vec u = \psi^\dagger\boldsymbol{\sigma}\psi .
$$

Because $\vec u$ satisfies $|\vec u| = \psi^\dagger\psi = 1$ (the standard Pauli identity), $\rho$ is a rank-one Hermitian projector: $\rho^2 = \rho$, $\mathrm{Tr}\,\rho = 1$. Under the isomorphism $\sigma_\mu \leftrightarrow i \vec e_\mu$, this maps to

$$
\rho \;\longmapsto\; \tfrac{1}{2}\left(e_t + i\,\vec u\right), \qquad \vec u = w_1 \vec e_x + w_2 \vec e_y + w_3 \vec e_z,
$$

which is exactly the idempotent $\tilde\Pi_1(\vec u)$ of the informational sector $\mathbb{M}_+$ in the companion quantum article. The unit vector $\vec u$ is the Bloch vector, and its normalization is a consequence of the algebra rather than an added condition. So a normalized two-component spinor is, in the biquaternion framework, precisely a pure state of $\mathbb{M}_+$, and the spinor bilinear $\psi\psi^\dagger$ is its representative idempotent. This is the sharpest sense in which the Dirac spinor structure and the informational sector are the same algebraic object, and it is the bridge between the present article and the qubit formalism.

### The Gordon decomposition

The vector bilinear admits the standard Gordon decomposition, derived in *The Gordon Decomposition of the Dirac Current in Biquaternionic Form*:

$$
\bar{w}(p_2)\,\Gamma_\mu\,w(p) = \bar{w}(p_2)\left[ \frac{(p+p_2)_\mu}{2m} + \frac{i\sum_\nu\sigma_{\mu\nu}(p_2-p)_\nu}{2m} \right] w(p),
$$

which splits the current into a **convection** part, proportional to $(p+p_2)_\mu$, and a **spin** part, proportional to the momentum transfer $(p_2-p)_\nu$ and to the tensor bilinear. The convection term is the orbital current of a charged particle; the spin term is the source of the magnetic coupling, and its coefficient $1/2m$ is what fixes the gyromagnetic factor at the tree level, as the next section shows. (The index $\nu$ is contracted in its lowered position, $(p_2-p)_\nu=(E_2-E,-\vec p_2+\vec p)$; contracted with the contravariant components the spin term would change sign. The overall sign also depends on the convention chosen for $\sigma_{\mu\nu}$ and for the metric; the identity is standard in the convention stated.)

## The non-relativistic limit

### Removing the rest energy

The non-relativistic limit is most transparent in the Dirac basis, where $\beta = \Gamma_0 = iR_{\vec e_x}$ is diagonal with opposite signs on the upper and the lower two-component part, and the spinor splits into an upper ("large") and a lower ("small") two-component part. Minimal coupling replaces the four-momentum by $p_\mu-ϙA_\mu$, with $A_\mu = (\Phi,-\vec A)$ and $ϙ$ the charge of the field; in natural units this is

$$
\vec p \;\longrightarrow\; \vec p - ϙ\vec A, \qquad i\partial/\partial t' \;\longrightarrow\; i\partial/\partial t' - ϙ\Phi .
$$

The Dirac equation becomes $i\partial/\partial t'\psi = H\psi$ with

$$
H = \sum_k\alpha_k(p_k - ϙA_k) + m\Gamma_0 + ϙ\Phi, \qquad
\alpha_k = \Gamma_0\Gamma_k = L_{\vec e_k}R_{\vec e_z}.
$$

The last equality is one use of $i^2=-1$: $\Gamma_0\Gamma_k=(iR_{\vec e_x})(iL_{\vec e_k}R_{\vec e_y})=i^2L_{\vec e_k}R_{\vec e_y\vec e_x}=-L_{\vec e_k}R_{-\vec e_z}=L_{\vec e_k}R_{\vec e_z}$. In the Dirac basis $\alpha_k$ exchanges the upper and lower two-component part and multiplies each by $\sigma_k$, which is what produces the coupled pair below.

The rest energy dominates the dynamics, so we factor it out by writing

$$
\psi = \exp(-imt')\begin{pmatrix} \phi \\ \chi \end{pmatrix}.
$$

Substituting and cancelling the common phase gives the two coupled equations

$$
i\,\partial/\partial t'\phi = \boldsymbol{\sigma}\cdot\vec\pi\,\chi + ϙ\Phi\,\phi,
\qquad
i\,\partial/\partial t'\chi = \boldsymbol{\sigma}\cdot\vec\pi\,\phi - 2m\,\chi + ϙ\Phi\,\chi,
$$

where $\vec\pi = \vec p - ϙ\vec A$ is the kinetic momentum. The small component is the one multiplied by the large rest energy $2m$.

### Eliminating the small component

If the fields and the kinetic energy are small compared with the rest energy $m$ and vary slowly, the term $2m\chi$ dominates the right-hand side of the second equation, and $\partial/\partial t'\chi$ is negligible by comparison:

$$
0 \approx \boldsymbol{\sigma}\cdot\vec\pi\,\phi - 2m\,\chi
\quad\Longrightarrow\quad
\chi \approx \frac{\boldsymbol{\sigma}\cdot\vec\pi}{2m}\,\phi.
$$

This is the algebraic statement that the small component is generated from the large one by the velocity operator $\boldsymbol{\sigma}\cdot\vec\pi/2m$. Substituting into the first equation eliminates $\chi$ entirely and leaves an equation for the two-component spinor $\phi$:

$$
i\,\partial/\partial t'\phi = \left[ \frac{(\boldsymbol{\sigma}\cdot\vec\pi)^2}{2m} + ϙ\Phi \right]\phi.
$$

### The Pauli equation

It remains to evaluate the square of the Pauli operator. The standard identity $(\boldsymbol{\sigma}\cdot\vec a)(\boldsymbol{\sigma}\cdot\vec b) = \vec a\cdot\vec b + i\boldsymbol{\sigma}\cdot(\vec a\times\vec b)$ gives

$$
(\boldsymbol{\sigma}\cdot\vec\pi)^2 = \vec\pi^2 + i\,\boldsymbol{\sigma}\cdot(\vec\pi\times\vec\pi).
$$

The cross product must be computed with the operator ordering kept, since $\vec p$ and $\vec A$ do not commute. In natural units, where $\vec p = -i\nabla$, and with $\vec\pi = \vec p - ϙ\vec A$,

$$
\vec\pi\times\vec\pi = -ϙ\left(\vec p\times\vec A + \vec A\times\vec p\right) = -ϙ\left(-i\,\vec B\right) = iϙ\,\vec B,
$$

where $\vec B = \nabla\times\vec A$ is the magnetic field. Therefore

$$
(\boldsymbol{\sigma}\cdot\vec\pi)^2 = \vec\pi^2 - ϙ\,\boldsymbol{\sigma}\cdot\vec B,
$$

and the two-component equation in natural units reads

$$
i\,\partial/\partial t'\phi = \left[ \frac{\vec\pi^2}{2m} + ϙ\Phi - \frac{ϙ}{2m}\,\boldsymbol{\sigma}\cdot\vec B \right]\phi.
$$

Restoring the explicit factors of $\hbar$ and writing $\vec\pi = \vec p - ϙ\vec A$ with $\vec p = -i\hbar\nabla$ gives the **Pauli equation**

$$
\boxed{\;i\hbar\,\partial/\partial t'\phi = \left[ \frac{(\vec p - ϙ\vec A)^2}{2m} + ϙ\Phi - \frac{ϙ\hbar}{2m}\,\boldsymbol{\sigma}\cdot\vec B \right]\phi\;}.
$$

The first two terms are the ordinary non-relativistic Hamiltonian of a charged particle; the third is the spin–magnetic coupling. This is the announced reduction of the biquaternionic Dirac equation to the Pauli equation: the four-component spinor has been reduced to a two-component spinor, and the spin has become an explicit dynamical variable.

### The g-factor and the spin–magnetic coupling

The spin term is a magnetic dipole coupling. Writing it as $-\vec\mu\cdot\vec B$ identifies

$$
\vec\mu = \frac{ϙ\hbar}{2m}\,\boldsymbol{\sigma} = \frac{ϙ}{m}\,\vec S, \qquad \vec S = \frac{\hbar}{2}\boldsymbol{\sigma}.
$$

Comparing with the general form $\vec\mu = g\,\dfrac{ϙ}{2m}\,\vec S$ gives, at the tree level,

$$
\boxed{\; g = 2 \;}
$$

The gyromagnetic factor is not put in by hand: it follows from the coefficient $1/2m$ produced by eliminating the small component. This is the Dirac equation's celebrated prediction of $g=2$ for a structureless spin-$\tfrac{1}{2}$ particle, here obtained as a property of the biquaternionic mass term. For the electron, $ϙ = -e$ and

$$
\vec\mu_e = -\frac{e}{m_e}\,\vec S = -g\,\frac{e}{2m_e}\,\vec S, \qquad g = 2,
$$

with magnitude one Bohr magneton $\mu_B = e\hbar/2m_e$ for $\vec S$ aligned with $\vec B$ (at $S_z = \hbar/2$). The observed value differs from $2$ by the anomalous part $a = (g-2)/2 \approx \alpha/2\pi$; that is a radiative correction and lies outside the classical equation treated here. The tree-level result $g=2$ is what the limit contains.

The biquaternion form of the spin coupling is immediate. Under the isomorphism, the magnetic-field combination maps as $\boldsymbol{\sigma}\cdot\vec B \leftrightarrow i\,\vec B$ with $\vec B = \sum_k B_k \vec e_k$, so the spin term is the Hermitian element

$$
-\frac{ϙ\hbar}{2m}\,\boldsymbol{\sigma}\cdot\vec B \;\longleftrightarrow\; -\frac{ϙ\hbar}{2m}\,i\,\vec B \;\in\; \mathbb{M}_+ .
$$

The spin–magnetic coupling is therefore an observable of the informational sector $\mathbb{M}_+$, in the sense of the companion quantum article, and the spin state evolves by the rotor conjugation generated by it. This is the point of contact between the Dirac solutions of this article and the qubit formalism of the informational sector.

### The two-component spinor and its evolution

The Pauli spinor $\phi$ is a two-component object, and its associated spin state is the idempotent

$$
\tilde{Ϛ}_\phi = \frac{\phi\,\phi^{\dagger}}{\phi^{\dagger}\phi} = \tfrac{1}{2}\left(e_t + i\,\vec u\right) \in \mathbb{M}_+ ,
$$

with $\vec u$ the Bloch vector of the spin. The Pauli Hamiltonian is a Hermitian element $\tilde{H}_P = \frac{(\vec p-ϙ\vec A)^2}{2m} + ϙ\Phi - \frac{ϙ\hbar}{2m} i\vec B \in \mathbb{M}_+$, and the spin precesses by the corresponding rotor conjugation. For a uniform magnetic field, only the last term contributes to the spin motion, and the precession frequency is the Larmor frequency $\omega_L = g\,ϙB/2m = ϙB/m$ at $g=2$ in natural units; up to the sign of $ϙ$ this is the familiar spin precession. The two-component spinor description, the Pauli equation, and the precession are thus all consequences of the single biquaternionic Dirac equation.

## Massless case: the Weyl equations and chirality

Setting $m = 0$ decouples the two chiral components. In the chiral basis the Dirac equation becomes the pair of **Weyl equations**

$$
\boxed{\;i\hbar\,\partial/\partial t'\psi_R = c\,\boldsymbol{\sigma}\cdot\vec p\,\psi_R\;}
$$

for the right-handed field, and

$$
\boxed{\;i\hbar\,\partial/\partial t'\psi_L = -\,c\,\boldsymbol{\sigma}\cdot\vec p\,\psi_L\;}
$$

for the left-handed field. In covariant form, with $\sigma^\mu=(1,\boldsymbol\sigma)$, $\bar\sigma^\mu=(1,-\boldsymbol\sigma)$ and $\partial_\mu=(\partial_t,\nabla)$, they read $i\sigma^\mu\partial_\mu\psi_R = 0$ and $i\bar\sigma^\mu\partial_\mu\psi_L = 0$ in natural units. Each equation carries a single chirality. For the positive-frequency modes chirality and helicity coincide, so the right-handed field has positive helicity and the left-handed field negative helicity; for the negative-frequency modes, the antiparticles, the assignment reverses. The mass term is exactly what couples the two, and it is the only term in the equation that does so. The projectors

$$
P_L = \tfrac{1}{2}\bigl(1 - (-iR_{\vec e_z})\bigr), \qquad P_R = \tfrac{1}{2}\bigl(1 + (-iR_{\vec e_z})\bigr)
$$

select the two components; on the four-component carrier they act as the Peirce right multiplications $R_{\tilde\Pi_+}$ and $R_{\tilde\Pi_-}$. The algebraic counterparts of $P_L$ and $P_R$ are the central idempotents $e_\pm=\tfrac12(1\pm\chi)$ of the complexification, with $\chi=i\tilde\Xi_{\mathrm{ad}}$ the central grading of the Gamma section; the Peirce idempotents $\tilde\Pi_\pm$ are not central, and the two pairs are different objects. The Weyl spinors are thus the $m \to 0$ limit of the solutions constructed above, and the biquaternionic Dirac operator reduces in that limit to the pair of Weyl operators.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5=-iL_{e_t}R_{\vec e_z} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $-iR_{\vec e_z}$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

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

## Summary

The biquaternionic Dirac equation, on its spinor module, has plane-wave solutions in two branches. The positive-frequency branch is spanned by $w^{(r)}(\vec p)\exp(-i(Et'-\vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)))$ and the negative-frequency branch by $v^{(r)}(\vec p)\exp(+i(Et'-\vec p\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)))$, with $E = +\sqrt{\vec p^2+m^2}$; both branches are the two roots of the single biquaternionic mass-shell condition $\tilde P\tilde P^{\natural}=-m^2c^2$. The pair is one-sided, with both gradients acting on the left; the two-sided form of the companion article is a different operator and is not used here. The spinors have an explicit two-component structure, displayed here in both the Dirac and the chiral bases. They satisfy the covariant normalizations $\bar{w}w = 2m$, $\bar{v}v = -2m$, the orthogonality $\bar{w}v = 0$, and the spin sums $\sum_r w\,\langle w,\cdot\rangle_{\mathrm D} = P+m$, $\sum_r v\,\langle v,\cdot\rangle_{\mathrm D} = P-m$.

The spinor bilinears have a clean biquaternion interpretation. The conserved vector current is the four-vector $\tilde{J} = ic\,j_0e_t + \vec j$ in the material sector $\mathbb{M}_-$, while the rank-one Hermitian form built from a single two-component spinor is exactly the idempotent $\tfrac{1}{2}(e_t + i\vec u)$ of the informational sector $\mathbb{M}_+$, so a Weyl spinor is a pure state of the informational sector. The scalar and pseudoscalar bilinears are the real and imaginary parts of the chirality-flipping bilinear $\psi_L^\dagger\psi_R$.

In the non-relativistic limit, factoring out the rest energy and eliminating the small component reduces the four-component equation to the Pauli equation

$$
i\hbar\,\partial/\partial t'\phi = \left[ \frac{(\vec p - ϙ\vec A)^2}{2m} + ϙ\Phi - \frac{ϙ\hbar}{2m}\,\boldsymbol{\sigma}\cdot\vec B \right]\phi,
$$

whose spin term is the Hermitian observable $-\frac{ϙ\hbar}{2m} i\vec B \in \mathbb{M}_+$. The coefficient produced by the elimination is exactly the one required by $\vec\mu = g\frac{ϙ}{2m}\vec S$ with $g = 2$, so the gyromagnetic factor and the spin–magnetic coupling are consequences of the biquaternionic mass term rather than separate postulates. In the massless limit the equation splits into the two Weyl equations, with chirality locked to helicity, which is the starting point for the treatment of chirality with Weyl spinors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\tilde{\nabla} = e_t\partial/\partial Q_t + \sum_\mu\,\vec e_\mu\partial/\partial Q_\mu$ | Biquaternionic gradient (Dirac operator) |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$ | d'Alembertian |
| $\tilde{\Psi}$ | Biquaternion-valued Dirac field |
| $\tilde{\Psi}^\flat = -\tilde{\Psi}^{*}$ | Anti-Hermitian conjugate (the algebra's real structure; not the mass term) |
| $\tilde{P}/\hbar = i k_0 e_t + \vec k$, $k_0 = \omega/c$ | Wave biquaternion |
| $\tilde P\tilde P^{\natural}=-m^2c^2$ | Biquaternionic mass-shell condition |
| $\psi = (\psi_L,\psi_R)$ | Dirac spinor in the chiral basis |
| $L_a$, $R_b$, $L_{a}R_{b}$ | Left and right multiplication, $L_a\psi=a\psi$, $R_b\psi=\psi b$, $L_{a}R_{b}\psi=a\psi b$; $L_{a}R_{b}L_{c}R_{d}=L_{ac}R_{db}$ |
| $\Gamma_0=iR_{\vec e_x}$, $\Gamma_k=iL_{\vec e_k}R_{\vec e_y}$ | Generator cells of the frame |
| $\beta = \Gamma_0 = iR_{\vec e_x}$ | Timelike cell in the Dirac basis; $+1$ on the upper block, $-1$ on the lower |
| $-iR_{\vec e_z}=-iL_{e_t}R_{\vec e_z}$ | Chirality cell; $-1$ on $\mathbb{B}\tilde\Pi_+$, $+1$ on $\mathbb{B}\tilde\Pi_-$ |
| $\tilde\Pi_\pm = \tfrac12(e_t\pm i\vec e_z)$ | Peirce idempotents; on the four-component carrier $P_{L,R}$ act as $R_{\tilde\Pi_\pm}$ |
| $P = \Gamma_0p_0-\sum_k\Gamma_kp_k$ | Momentum cell; $P^2=p_0^2-\vec p^2$ |
| $\vec\pi = \vec p - ϙ\vec A$ | Kinetic momentum under minimal coupling |
| $\slashed p = i\Gamma_0\partial/\partial t'+\sum_k i\Gamma_k\partial/\partial Q_k$ | Dirac operator on the material sector; $\slashed p^2=\Box$ on $\mathbb{M}_-$ |
| $\alpha_k = \Gamma_0\Gamma_k = L_{\vec e_k}R_{\vec e_z}$ | Velocity operator of the non-relativistic limit |
| $\sigma_{\mu\nu} = \tfrac{i}{2}[\Gamma_\mu,\Gamma_\nu]$ | Antisymmetric product of two generators; operator of the tensor bilinear |
| $g = \mathrm{diag}(+1,-1,-1,-1)$ | Clifford metric of the generators; note $g = -\eta$ |
| $\eta = \mathrm{diag}(-1,+1,+1,+1)$ | Spacetime metric of the $ict'$ gradient |
| $\bar{\psi}\phi = \langle\psi,\phi\rangle_{\mathrm D} = \psi_L^\dagger\phi_R+\psi_R^\dagger\phi_L$ | Dirac adjoint, the Hermitian pairing twisted by $\Gamma_0$ |
| $w^{(r)}(\vec p),\, v^{(r)}(\vec p)$ | Positive- and negative-frequency spinors |
| $\xi^{(r)}$, $\eta^{(r)}$, $\chi_\pm$, $\vec u_p = \vec p/\lvert\vec p\rvert$ | Rest spinors, helicity eigenspinors and momentum direction |
| $\phi$, $\chi$ | Large and small two-component parts in the non-relativistic limit |
| $P_L$, $P_R$ | Chirality projectors, $R_{\tilde\Pi_+}$ and $R_{\tilde\Pi_-}$ |
| $p_0 = E$, $\vec p = (p_1,p_2,p_3)$ | Four-momentum components |
| $j_\mu = \langle\psi,\Gamma_\mu\psi\rangle_{\mathrm D}$ | Conserved Dirac current |
| $\tilde{J} = ic\,j_0e_t + \vec j \in \mathbb{M}_-$ | Current as a material-sector biquaternion |
| $\rho = \psi\psi^\dagger \mapsto \tfrac{1}{2}(e_t + i\vec u)$ | Spin bilinear as an $\mathbb{M}_+$ idempotent |
| $ϙ$ | Charge of the field under minimal coupling |
| $\vec S = \tfrac{\hbar}{2}\boldsymbol{\sigma}$, $\vec\mu = g\frac{ϙ}{2m}\vec S$ | Spin and magnetic moment |
| $g = 2$ | Gyromagnetic factor in the non-relativistic limit |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original Dirac equation and the prediction of $g = 2$.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the plane-wave solutions, the Dirac bilinears, and the Gordon decomposition in the standard notation.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the spin sums, the charge-conjugation and chirality structure, and the non-relativistic reduction.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the chiral and Dirac representations, the spinor normalization, and the spin sums.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the non-relativistic limit of the Dirac equation and the emergence of the Pauli equation.
- W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 2000), for a detailed step-by-step treatment of the Foldy–Wouthuysen and Pauli limits.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford-algebraic background to the biquaternion and spinor structures.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra formulation of the Dirac and Weyl equations.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original spacetime-algebra treatment of the Dirac spinor.
