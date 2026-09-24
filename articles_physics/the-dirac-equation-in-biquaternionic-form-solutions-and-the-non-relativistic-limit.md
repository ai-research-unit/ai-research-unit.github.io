# __The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit__

## Introduction

The companion article *The Dirac Equation in Biquaternionic Form* stated the biquaternionic Dirac equation

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R,
$$

together with its massless limit $\tilde{\nabla}\tilde{\Psi} = 0$ and the Klein–Gordon reduction $(\Box - m^2c^2/\hbar^2)\tilde{\Psi} = 0$. It established the algebraic setting — the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ as the even subalgebra of the Clifford algebra, the biquaternionic gradient $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$ as the biquaternion form of the Dirac operator, the action of the equation on the spinor module of $\mathbb{B}$, and the plane-wave ansatz $\tilde{\Psi} = \tilde{\Psi}_0\exp\!\left(i\,\mathrm{Sc}(\tilde{k}\bar{\tilde{X}})\right)$ with the mass-shell condition $\tilde{k}\bar{\tilde{k}} = -m^2c^2/\hbar^2$. It closed by noting that the massive solution space is four-dimensional over $\mathbb{C}$, corresponding to the four components of the Dirac spinor.

That article deliberately worked at a summary level. It identified the solution classes and the mass-shell condition, but it did not construct the solutions, did not fix their normalization, did not write the spinor bilinears, and did not carry the equation into the non-relativistic regime. The purpose of the present article is to supply exactly those four things.

The article is organized as follows. The next section fixes the field, the two natural spinor bases, and the conventions. The following section constructs the plane-wave solutions in full, separating the positive- and the negative-frequency branches and displaying the spinor structure in both bases. The section after that treats orthogonality and normalization and records the spin sums. The next section gives the biquaternion form of the spinor bilinears. The longest section performs the non-relativistic limit, reduces the equation to the Pauli equation, exhibits the two-component spinor, and shows how the gyromagnetic factor and the spin–magnetic coupling emerge. A short section records the massless case and chirality, and the article closes with a summary.

The material here is the declared foundation for two of the later exercises, on the plane-wave solutions and on the non-relativistic limit and the Pauli equation. The solutions and the limiting procedure are therefore worked out explicitly, with all intermediate steps that those exercises will need.

**Conventions.** The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and $i$ is the scalar imaginary with $i^2 = -1$. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$. The isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ used throughout is the one of the companion article *Quantum Mechanics in Biquaternionic Form*,

$$
e_0 \mapsto I_2, \qquad e_k \mapsto -i\sigma_k, \qquad i \mapsto i I_2,
$$

so that $i e_k \leftrightarrow \sigma_k$. The gamma matrices are the explicit block matrices built from the biquaternion units, in the mostly-minus convention used here; the companion Dirac article attaches $\eta$ to its generators, so its matrices are the $\gamma'^\mu = i\gamma^\mu$ of the paragraph below,

$$
\gamma^0 = \begin{pmatrix} 0 & I_2 \\ I_2 & 0 \end{pmatrix}, \qquad
\gamma^k = \begin{pmatrix} 0 & \sigma_k \\ -\sigma_k & 0 \end{pmatrix}, \qquad k = 1,2,3,
$$

which satisfy $\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu} I_4$ with $g = \mathrm{diag}(+1,-1,-1,-1)$; the metric sign is the convention noted in the companion article. These matrices constitute the **chiral (Weyl) representation**: the chirality operator

$$
\gamma_5 = i\,\gamma^0\gamma^1\gamma^2\gamma^3 = \begin{pmatrix} -I_2 & 0 \\ 0 & I_2 \end{pmatrix}, \qquad \gamma_5^2 = I_4,
$$

is diagonal, so the upper two-component block is left-handed and the lower is right-handed. We also use the **Dirac representation**, obtained by a unitary change of basis, in which $\gamma^0 = \mathrm{diag}(I_2,-I_2)$ and $\gamma^k = \begin{pmatrix} 0 & \sigma_k \\ -\sigma_k & 0 \end{pmatrix}$; the non-relativistic limit is simplest there. In the sections that construct the solutions we use natural units $\hbar = c = 1$; the dimensionally explicit forms are given where they carry physical meaning, namely in the mass-shell relation and in the Pauli equation.

The two metric symbols used in this article must not be interchanged. The Clifford metric $g = \mathrm{diag}(+1,-1,-1,-1)$ belongs to the generators, through the anticommutator; the spacetime metric $\eta = \mathrm{diag}(-1,+1,+1,+1)$ of the companion articles belongs to the $ict$ gradient, through $\Box$. They are the negatives of one another, and that relative sign is exactly the freedom the companion article flags as convention. The reconciliation is that the massless equation squares to

$$
-\gamma^\mu\gamma^\nu\,\partial_\mu\partial_\nu
= -g^{\mu\nu}\partial_\mu\partial_\nu
= \eta^{\mu\nu}\partial_\mu\partial_\nu
= \Box,
$$

so the same $\Box$ results whichever way the sign is assigned. With the Clifford metric fixed at $g$, the slash of a four-momentum $p^\mu = (E,\mathbf{p})$ is $\not{p} = \gamma^\mu p_\mu = \gamma^0 E - \boldsymbol{\gamma}\cdot\mathbf{p}$, since $p_\mu = (E,-\mathbf{p})$ in this signature. A reader who prefers instead to attach $\eta$ to the generators must set $\gamma'^\mu = i\gamma^\mu$, which flips the Clifford metric to $\eta$ and rewrites the equation as $(\gamma'^\mu\partial_\mu - m)\psi = 0$; the physics is unchanged, only the placement of the signs differs.

## The Dirac field and its two bases

In the spinor module, the biquaternionic Dirac equation is the standard Dirac equation

$$
(i\hbar\gamma^\mu\partial_\mu - mc)\psi = 0,
$$

or, in natural units,

$$
(i\gamma^\mu\partial_\mu - m)\psi = 0,
$$

with $\psi$ a four-component complex Dirac spinor. The biquaternion field $\tilde{\Psi}$ of the companion article is the algebra-level representative of this spinor: it is the element of $\mathbb{B} \cong M_2(\mathbb{C})$ that acts on, and encodes, the two-component spinor module, and the operator $\tilde{\nabla}$ is its Dirac operator. The mass term of the companion article is the linear, chirality-off-diagonal coupling of its chiral pair — the algebra-level representative of the spinor mass term above. The conjugation $\tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger$ is a separate object, the algebra's real structure (the fixed space of $\flat$ is the anti-Hermitian sector $\mathbb{M}_-$), and is *not* the mass term.

Because $\mathbb{B} \cong M_2(\mathbb{C})$ acts naturally on a two-dimensional complex module, the biquaternion field carries two two-component spinors. In the chiral representation these are the left- and right-handed Weyl spinors,

$$
\psi = \begin{pmatrix} \psi_L \\ \psi_R \end{pmatrix}, \qquad \psi_L, \psi_R \in \mathbb{C}^2.
$$

This is the structure that the companion article referred to when it described the biquaternion field as a pair of Weyl spinors. The two representations are related by a change of basis, and the physics is independent of the choice; but each makes a different structure manifest. The **chiral basis** diagonalizes $\gamma_5$ and therefore exhibits chirality, which is the natural language for the massless case. The **Dirac basis** diagonalizes $\gamma^0 = \beta$ and therefore separates the upper "large" and lower "small" components in the non-relativistic limit. We give the plane-wave solutions in both.

The Dirac adjoint is

$$
\bar{\psi} = \psi^\dagger\gamma^0,
$$

so that $\bar{\psi}\psi$ is a Lorentz scalar. The amplitude equation for a plane wave follows by substituting; we carry this out in the next section.

## Plane-wave solutions

### Positive-frequency branch

Take the positive-frequency plane wave

$$
\psi(x) = u(\mathbf{p})\, e^{-i(Et - \mathbf{p}\cdot\mathbf{x})}, \qquad E = +\sqrt{\mathbf{p}^2 + m^2},
$$

where $u(\mathbf{p})$ is a four-component constant spinor. Substituting into $(i\gamma^\mu\partial_\mu - m)\psi = 0$ gives the momentum-space Dirac equation

$$
(\not{p} - m)\,u(\mathbf{p}) = 0, \qquad \not{p} = \gamma^\mu p_\mu = \gamma^0 E - \boldsymbol{\gamma}\cdot\mathbf{p},
$$

using the mostly-minus metric, so that the spatial part enters with a minus sign. Squaring gives the mass-shell condition $p^2 = E^2 - \mathbf{p}^2 = m^2$.

The spinor structure is most transparent in the **Dirac basis**. Writing $u = (u_A, u_B)$ with $u_A, u_B \in \mathbb{C}^2$, the momentum-space equation becomes the pair

$$
(E - m)\,u_A = \boldsymbol{\sigma}\cdot\mathbf{p}\, u_B, \qquad (E + m)\,u_B = \boldsymbol{\sigma}\cdot\mathbf{p}\, u_A,
$$

so that $u_B = \dfrac{\boldsymbol{\sigma}\cdot\mathbf{p}}{E+m} u_A$ and the upper component $u_A$ is free. With the covariant normalization, the two positive-energy solutions are

$$
u^{(r)}(\mathbf{p}) = \begin{pmatrix} \sqrt{E+m}\,\xi^{(r)} \\[2pt] \sqrt{E-m}\,(\boldsymbol{\sigma}\cdot\hat{\mathbf{p}})\,\xi^{(r)} \end{pmatrix}, \qquad r = 1,2,
$$

where $\hat{\mathbf{p}} = \mathbf{p}/|\mathbf{p}|$ and $\xi^{(1)}, \xi^{(2)}$ are the standard orthonormal two-spinors, $\xi^{(r)\dagger}\xi^{(s)} = \delta^{rs}$. At rest this reduces to $u^{(r)}(0) = \sqrt{2m}\begin{pmatrix}\xi^{(r)}\\ 0\end{pmatrix}$.

The same solutions in the **chiral basis** are indexed by helicity. Let $\chi_\pm$ be eigenspinors of the helicity operator,

$$
\boldsymbol{\sigma}\cdot\hat{\mathbf{p}}\,\chi_\pm = \pm\,\chi_\pm .
$$

Then

$$
u_\pm(\mathbf{p}) = \begin{pmatrix} \sqrt{E \mp |\mathbf{p}|}\; \chi_\pm \\[2pt] \sqrt{E \pm |\mathbf{p}|}\; \chi_\pm \end{pmatrix},
$$

with the upper block left-handed and the lower block right-handed. One checks directly that this satisfies $(\not{p}-m)u_\pm = 0$: the upper equation is $(E\mp|\mathbf{p}|)\sqrt{E\pm|\mathbf{p}|} = m\sqrt{E\mp|\mathbf{p}|}$, which reduces to $E^2 - \mathbf{p}^2 = m^2$. At high energy the coefficient $E \mp |\mathbf{p}|$ of the upper component tends to zero for the matching sign, so each helicity-eigenstate solution becomes dominated by a single chirality — the statement that a massless fermion has definite handedness. The two bases are related by a fixed unitary transformation, and the two spin states may equally be labelled by helicity or by the index $r$; the labelling is a convention.

The general positive-energy solution is an arbitrary linear combination $u = a_1 u^{(1)} + a_2 u^{(2)}$, so the positive-frequency solution space at fixed $\mathbf{p}$ is two-dimensional over $\mathbb{C}$.

### Negative-frequency branch

The negative-frequency plane waves are

$$
\psi(x) = v(\mathbf{p})\, e^{+i(Et - \mathbf{p}\cdot\mathbf{x})}, \qquad E = +\sqrt{\mathbf{p}^2 + m^2}.
$$

Substituting gives the momentum-space equation

$$
(\not{p} + m)\,v(\mathbf{p}) = 0,
$$

with the same $\not{p} = \gamma^0 E - \boldsymbol{\gamma}\cdot\mathbf{p}$. In the Dirac basis the pair reads $(E+m)v_A = \boldsymbol{\sigma}\cdot\mathbf{p}\,v_B$ and $(E-m)v_B = \boldsymbol{\sigma}\cdot\mathbf{p}\,v_A$, and the two solutions are

$$
v^{(r)}(\mathbf{p}) = \begin{pmatrix} \sqrt{E-m}\,(\boldsymbol{\sigma}\cdot\hat{\mathbf{p}})\,\eta^{(r)} \\[2pt] \sqrt{E+m}\,\eta^{(r)} \end{pmatrix}, \qquad r = 1,2,
$$

with $\eta^{(r)\dagger}\eta^{(s)} = \delta^{rs}$; at rest $v^{(r)}(0) = \sqrt{2m}\begin{pmatrix} 0 \\ \eta^{(r)} \end{pmatrix}$. The negative-frequency solution space is again two-dimensional. In the standard reading, these modes describe antiparticles: the sign of the frequency is reversed by the charge-conjugation operation, which exchanges $u$ and $v$. Together, then, the amplitude equations have a four-dimensional complex solution space at fixed $\mathbf{p}$, exactly as the companion article stated.

### The biquaternion mass shell

The plane-wave ansatz of the companion article, $\tilde{\Psi} = \tilde{\Psi}_0\exp\!\left(i\,\mathrm{Sc}(\tilde{k}\bar{\tilde{X}})\right)$, carries the wave biquaternion $\tilde{k}$.

With the four-wavevector of the companion article written as $\tilde{K} = i\omega/c\,e_0 + \mathbf{k}$, the norm form is

$$
N(\tilde{K}) = \tilde{K}\bar{\tilde{K}} = \left(\frac{i\omega}{c}\right)^2 + \mathbf{k}^2 = -\frac{\omega^2}{c^2} + \mathbf{k}^2 .
$$

The mass shell $\omega^2 = c^2\mathbf{k}^2 + m^2c^4/\hbar^2$, which is $E^2 = \mathbf{p}^2c^2 + m^2c^4$ under $E = \hbar\omega$, $\mathbf{p} = \hbar\mathbf{k}$, is therefore exactly the companion article's condition

$$
\tilde{k}\bar{\tilde{k}} = -\frac{m^2c^2}{\hbar^2}.
$$

The two roots $\omega = \pm\sqrt{c^2\mathbf{k}^2 + m^2c^4/\hbar^2}$ are the two frequency branches, so the positive- and negative-frequency solutions above are the two branches of the single biquaternionic mass-shell condition. The polarization equations $i\tilde{k}\tilde{\Psi}_0^R = m\tilde{\Psi}_0^L$, $i\bar{\tilde{k}}\tilde{\Psi}_0^L = m\tilde{\Psi}_0^R$ are the algebraic form of the momentum-space equation; their solution space is the four-dimensional space spanned by the $u^{(r)}$ and $v^{(r)}$ — two spin states for each of the two frequency branches.

### Spin structure and helicity

Two features of the spinor structure deserve emphasis, because the later exercises depend on them.

First, the **spin label**. The two independent solutions at fixed momentum can be chosen as eigenstates of any maximal commuting spin observable. The standard choices are the spin projection along a fixed axis (the two-spinor index $r$) and the helicity $\boldsymbol{\sigma}\cdot\hat{\mathbf{p}}$ (the labels $\pm$). Helicity is the natural label for a massless particle, because it is then Lorentz invariant; for a massive particle it is frame-dependent, and the spin index $r$ is the more convenient label.

Second, the **chirality–helicity relation**. In the chiral basis, positive-helicity positive-energy states are dominated by the right-handed component and negative-helicity states by the left-handed component. This is the precise sense in which "massless fermions of definite helicity have definite chirality", and it is the bridge to the Weyl equations of the closing sections.

## Orthogonality and normalization

The Dirac adjoint $\bar{\psi} = \psi^\dagger\gamma^0$ makes the bilinear $\bar{u}u$ a Lorentz scalar. A direct computation from the explicit solutions gives the normalization

$$
\bar{u}^{(r)}(\mathbf{p})\,u^{(s)}(\mathbf{p}) = 2m\,\delta^{rs}, \qquad
\bar{v}^{(r)}(\mathbf{p})\,v^{(s)}(\mathbf{p}) = -2m\,\delta^{rs},
$$

the relative minus sign being the standard signature of the negative-frequency branch. The cross terms vanish at equal momentum,

$$
\bar{u}^{(r)}(\mathbf{p})\,v^{(s)}(\mathbf{p}) = 0,
$$

and the Hermitian (non-covariant) products are

$$
u^{(r)\dagger}(\mathbf{p})\,u^{(s)}(\mathbf{p}) = 2E\,\delta^{rs}, \qquad
v^{(r)\dagger}(\mathbf{p})\,v^{(s)}(\mathbf{p}) = 2E\,\delta^{rs}, \qquad
u^{(r)\dagger}(\mathbf{p})\,v^{(s)}(-\mathbf{p}) = 0,
$$

the last relation requiring the opposite momentum, as usual. Three normalization conventions are in common use — $\bar{u}u = 2m$, $\bar{u}u = 1$, and $u^\dagger u = 1$ — and they differ by momentum-dependent factors; the covariant convention $\bar{u}u = 2m$ is the one used here, because it makes the spin sums below manifestly covariant.

The **spin sums** (completeness relations) close the solution set over the spin index:

$$
\sum_{r=1}^{2} u^{(r)}(\mathbf{p})\,\bar{u}^{(r)}(\mathbf{p}) = \not{p} + m, \qquad
\sum_{r=1}^{2} v^{(r)}(\mathbf{p})\,\bar{v}^{(r)}(\mathbf{p}) = \not{p} - m .
$$

These are the algebraic statement that the four solutions at fixed momentum form a basis of the amplitude space, and they are the ingredient that later exercises will need in order to sum over spins.

The **conserved current** of the Dirac field is

$$
j^\mu = \bar{\psi}\gamma^\mu\psi, \qquad \partial_\mu j^\mu = 0,
$$

with $j^0 = \psi^\dagger\psi \ge 0$ and real spatial components. In the series' notation, the current is the four-vector biquaternion

$$
\tilde{J} = ic\,j^0\,e_0 + \mathbf{j} \in \mathbb{M}_- ,
$$

with imaginary scalar part $ic\,j^0$ and real vector part $\mathbf{j} = (j^1,j^2,j^3)$. This is exactly the form required of a four-vector in the material sector $\mathbb{M}_-$: the Dirac current is a material-space object, as it must be.

## Spinor bilinears in biquaternion form

### The five bilinears

From a spinor and its adjoint one forms the standard bilinears, classified by their Lorentz character:

| Bilinear | Lorentz character |
|---|---|
| $\bar{\psi}\psi$ | scalar |
| $i\,\bar{\psi}\gamma_5\psi$ | pseudoscalar |
| $\bar{\psi}\gamma^\mu\psi$ | four-vector |
| $\bar{\psi}\gamma^\mu\gamma_5\psi$ | axial four-vector (pseudovector) |
| $\bar{\psi}\sigma^{\mu\nu}\psi$, $\ \sigma^{\mu\nu} = \tfrac{i}{2}[\gamma^\mu,\gamma^\nu]$ | antisymmetric rank-two tensor |

The pseudoscalar is written with the explicit factor of $i$ because, in the convention used here, $\bar{\psi}\gamma_5\psi$ is purely imaginary and $i\bar{\psi}\gamma_5\psi$ is real. The vector bilinear is the conserved current of the preceding section; the tensor bilinear governs the spin contribution to the current and, as shown below, the magnetic moment.

### The chiral components

In the chiral basis the bilinears separate into the two Weyl spinors, and the identities are worth recording because they are the ones the chirality exercise will use. With $\psi = (\psi_L,\psi_R)$ one has

$$
\bar{\psi}\psi = \psi_L^\dagger\psi_R + \psi_R^\dagger\psi_L = 2\,\mathrm{Re}\!\left(\psi_L^\dagger\psi_R\right),
$$

$$
\bar{\psi}\gamma_5\psi = \psi_L^\dagger\psi_R - \psi_R^\dagger\psi_L = 2i\,\mathrm{Im}\!\left(\psi_L^\dagger\psi_R\right),
$$

and the vector current has components

$$
j^0 = \psi_L^\dagger\psi_L + \psi_R^\dagger\psi_R, \qquad
\mathbf{j} = -\,\psi_L^\dagger\boldsymbol{\sigma}\psi_L + \psi_R^\dagger\boldsymbol{\sigma}\psi_R .
$$

The axial current similarly has

$$
j_5^0 = \psi_R^\dagger\psi_R - \psi_L^\dagger\psi_L, \qquad
\mathbf{j}_5 = \psi_L^\dagger\boldsymbol{\sigma}\psi_L + \psi_R^\dagger\boldsymbol{\sigma}\psi_R .
$$

The scalar and pseudoscalar pair are seen to be the real and imaginary parts of the chirality-flipping bilinear $\psi_L^\dagger\psi_R$: a purely left-handed or purely right-handed field has $\bar{\psi}\psi = 0$. The vector and axial vector similarly recombine the same two Weyl currents with relative signs, which is the algebraic content of the chiral decomposition of the Dirac current.

### The spin bilinear and the informational sector

There is a second, distinct bilinear that is genuinely biquaternionic in character: the rank-one Hermitian form built from a single two-component spinor. For $\psi \in \mathbb{C}^2$ normalized by $\psi^\dagger\psi = 1$, define

$$
\rho = \psi\psi^\dagger = \tfrac{1}{2}\left(I_2 + \mathbf{n}\cdot\boldsymbol{\sigma}\right), \qquad
\mathbf{n} = \psi^\dagger\boldsymbol{\sigma}\psi .
$$

Because $\mathbf{n}$ satisfies $|\mathbf{n}| = \psi^\dagger\psi = 1$ (the standard Pauli identity), $\rho$ is a rank-one Hermitian projector: $\rho^2 = \rho$, $\mathrm{Tr}\,\rho = 1$. Under the isomorphism $\sigma_k \leftrightarrow i e_k$, this maps to

$$
\rho \;\longmapsto\; \tfrac{1}{2}\left(e_0 + i\,\hat{\mathbf{n}}\right), \qquad \hat{\mathbf{n}} = n_1 e_1 + n_2 e_2 + n_3 e_3,
$$

which is exactly the idempotent $\tilde{P}_+(\hat{\mathbf{n}})$ of the informational sector $\mathbb{M}_+$ in the companion quantum article. The unit vector $\mathbf{n}$ is the Bloch vector, and its normalization is a consequence of the algebra rather than an added condition. So a normalized two-component spinor is, in the biquaternion framework, precisely a pure state of $\mathbb{M}_+$, and the spinor bilinear $\psi\psi^\dagger$ is its representative idempotent. This is the sharpest sense in which the Dirac spinor structure and the informational sector are the same algebraic object, and it is the bridge between the present article and the qubit formalism.

### The Gordon decomposition

The vector bilinear admits the standard Gordon decomposition,

$$
\bar{u}(p')\gamma^\mu u(p) = \bar{u}(p')\left[ \frac{(p+p')^\mu}{2m} + \frac{i\sigma^{\mu\nu}(p'-p)_\nu}{2m} \right] u(p),
$$

which splits the current into a **convection** part, proportional to $(p+p')^\mu$, and a **spin** part, proportional to the momentum transfer $(p'-p)_\nu$ and to the tensor bilinear. The convection term is the orbital current of a charged particle; the spin term is the source of the magnetic coupling, and its coefficient $1/2m$ is what fixes the gyromagnetic factor at the tree level, as the next section shows. (The sign of the spin term depends on the convention chosen for $\sigma^{\mu\nu}$ and for the metric; the identity is standard in the convention stated.)

## The non-relativistic limit

### Removing the rest energy

The non-relativistic limit is most transparent in the Dirac basis, where $\beta = \gamma^0 = \mathrm{diag}(I_2,-I_2)$ and the spinor splits into an upper ("large") and a lower ("small") two-component part. Coupling to the electromagnetic four-potential $A^\mu = (\Phi,\mathbf{A})$ is by the minimal coupling $D_\mu = \partial_\mu + iqA_\mu$ for a field of charge $q$ (so $A_\mu = (\Phi,-\mathbf{A})$), which is equivalent to

$$
\hat{\mathbf{p}} \;\longrightarrow\; \hat{\mathbf{p}} - q\mathbf{A}, \qquad i\partial_t \;\longrightarrow\; i\partial_t - q\Phi
$$

in natural units. The Dirac equation becomes $i\partial_t\psi = \hat{H}\psi$ with

$$
\hat{H} = \boldsymbol{\alpha}\cdot(\hat{\mathbf{p}} - q\mathbf{A}) + \beta m + q\Phi, \qquad
\boldsymbol{\alpha}^k = \gamma^0\gamma^k = \begin{pmatrix} 0 & \sigma_k \\ \sigma_k & 0 \end{pmatrix}.
$$

The rest energy dominates the dynamics, so we factor it out by writing

$$
\psi = e^{-imt}\begin{pmatrix} \tilde{\phi} \\ \tilde{\chi} \end{pmatrix}.
$$

Substituting and cancelling the common phase gives the two coupled equations

$$
i\,\partial_t\tilde{\phi} = \boldsymbol{\sigma}\cdot\boldsymbol{\pi}\,\tilde{\chi} + q\Phi\,\tilde{\phi},
\qquad
i\,\partial_t\tilde{\chi} = \boldsymbol{\sigma}\cdot\boldsymbol{\pi}\,\tilde{\phi} - 2m\,\tilde{\chi} + q\Phi\,\tilde{\chi},
$$

where $\boldsymbol{\pi} = \hat{\mathbf{p}} - q\mathbf{A}$ is the kinetic momentum. The small component is the one multiplied by the large rest energy $2m$.

### Eliminating the small component

If the fields and the kinetic energy are small compared with $mc^2$ and vary slowly, the term $2m\tilde{\chi}$ dominates the right-hand side of the second equation, and $\partial_t\tilde{\chi}$ is negligible by comparison:

$$
0 \approx \boldsymbol{\sigma}\cdot\boldsymbol{\pi}\,\tilde{\phi} - 2m\,\tilde{\chi}
\quad\Longrightarrow\quad
\tilde{\chi} \approx \frac{\boldsymbol{\sigma}\cdot\boldsymbol{\pi}}{2m}\,\tilde{\phi}.
$$

This is the algebraic statement that the small component is generated from the large one by the velocity operator $\boldsymbol{\sigma}\cdot\boldsymbol{\pi}/2m$. Substituting into the first equation eliminates $\tilde{\chi}$ entirely and leaves an equation for the two-component spinor $\tilde{\phi}$:

$$
i\,\partial_t\tilde{\phi} = \left[ \frac{(\boldsymbol{\sigma}\cdot\boldsymbol{\pi})^2}{2m} + q\Phi \right]\tilde{\phi}.
$$

### The Pauli equation

It remains to evaluate the square of the Pauli operator. The standard identity $(\boldsymbol{\sigma}\cdot\mathbf{a})(\boldsymbol{\sigma}\cdot\mathbf{b}) = \mathbf{a}\cdot\mathbf{b} + i\boldsymbol{\sigma}\cdot(\mathbf{a}\times\mathbf{b})$ gives

$$
(\boldsymbol{\sigma}\cdot\boldsymbol{\pi})^2 = \boldsymbol{\pi}^2 + i\,\boldsymbol{\sigma}\cdot(\boldsymbol{\pi}\times\boldsymbol{\pi}).
$$

The cross product must be computed with the operator ordering kept, since $\hat{\mathbf{p}}$ and $\mathbf{A}$ do not commute. In natural units, where $\hat{\mathbf{p}} = -i\nabla$, and with $\boldsymbol{\pi} = \hat{\mathbf{p}} - q\mathbf{A}$,

$$
\boldsymbol{\pi}\times\boldsymbol{\pi} = -q\left(\hat{\mathbf{p}}\times\mathbf{A} + \mathbf{A}\times\hat{\mathbf{p}}\right) = -q\left(-i\,\mathbf{B}\right) = iq\,\mathbf{B},
$$

where $\mathbf{B} = \nabla\times\mathbf{A}$ is the magnetic field. Therefore

$$
(\boldsymbol{\sigma}\cdot\boldsymbol{\pi})^2 = \boldsymbol{\pi}^2 - q\,\boldsymbol{\sigma}\cdot\mathbf{B},
$$

and the two-component equation in natural units reads

$$
i\,\partial_t\tilde{\phi} = \left[ \frac{\boldsymbol{\pi}^2}{2m} + q\Phi - \frac{q}{2m}\,\boldsymbol{\sigma}\cdot\mathbf{B} \right]\tilde{\phi}.
$$

Restoring the explicit factors of $\hbar$ and writing $\boldsymbol{\pi} = \hat{\mathbf{p}} - q\mathbf{A}$ with $\hat{\mathbf{p}} = -i\hbar\nabla$ gives the **Pauli equation**

$$
i\hbar\,\partial_t\tilde{\phi} = \left[ \frac{(\hat{\mathbf{p}} - q\mathbf{A})^2}{2m} + q\Phi - \frac{q\hbar}{2m}\,\boldsymbol{\sigma}\cdot\mathbf{B} \right]\tilde{\phi}.
$$

The first two terms are the ordinary non-relativistic Hamiltonian of a charged particle; the third is the spin–magnetic coupling. This is the announced reduction of the biquaternionic Dirac equation to the Pauli equation: the four-component spinor has been reduced to a two-component spinor, and the spin has become an explicit dynamical variable.

### The g-factor and the spin–magnetic coupling

The spin term is a magnetic dipole coupling. Writing it as $-\boldsymbol{\mu}\cdot\mathbf{B}$ identifies

$$
\boldsymbol{\mu} = \frac{q\hbar}{2m}\,\boldsymbol{\sigma} = \frac{q}{m}\,\mathbf{S}, \qquad \mathbf{S} = \frac{\hbar}{2}\boldsymbol{\sigma}.
$$

Comparing with the general form $\boldsymbol{\mu} = g\,\dfrac{q}{2m}\,\mathbf{S}$ gives, at the tree level,

$$
\boxed{\; g = 2 \;}
$$

The gyromagnetic factor is not put in by hand: it follows from the coefficient $1/2m$ produced by eliminating the small component. This is the Dirac equation's celebrated prediction of $g=2$ for a structureless spin-$\tfrac{1}{2}$ particle, here obtained as a property of the biquaternionic mass term. For the electron, $q = -e$ and

$$
\boldsymbol{\mu}_e = -\frac{e}{m_e}\,\mathbf{S} = -g\,\frac{e}{2m_e}\,\mathbf{S}, \qquad g = 2,
$$

with magnitude one Bohr magneton $\mu_B = e\hbar/2m_e$ for $\mathbf{S}$ aligned with $\mathbf{B}$ (at $S_z = \hbar/2$). The observed value differs from $2$ by the anomalous part $a = (g-2)/2 \approx \alpha/2\pi$; that is a radiative correction and lies outside the classical equation treated here. The tree-level result $g=2$ is what the limit contains.

The biquaternion form of the spin coupling is immediate. Under the isomorphism, the magnetic-field combination maps as $\boldsymbol{\sigma}\cdot\mathbf{B} \leftrightarrow i\,\mathbf{B}$ with $\mathbf{B} = B_k e_k$, so the spin term is the Hermitian element

$$
-\frac{q\hbar}{2m}\,\boldsymbol{\sigma}\cdot\mathbf{B} \;\longleftrightarrow\; -\frac{q\hbar}{2m}\,i\,\mathbf{B} \;\in\; \mathbb{M}_+ .
$$

The spin–magnetic coupling is therefore an observable of the informational sector $\mathbb{M}_+$, in the sense of the companion quantum article, and the spin state evolves by the rotor conjugation generated by it. This is the point of contact between the Dirac solutions of this article and the qubit formalism of the informational sector.

### The two-component spinor and its evolution

The Pauli spinor $\tilde{\phi}$ is a two-component object, and its associated spin state is the idempotent

$$
\tilde{\rho}_\phi = \frac{\tilde{\phi}\,\tilde{\phi}^\dagger}{\tilde{\phi}^\dagger\tilde{\phi}} = \tfrac{1}{2}\left(e_0 + i\,\hat{\mathbf{n}}\right) \in \mathbb{M}_+ ,
$$

with $\hat{\mathbf{n}}$ the Bloch vector of the spin. The Pauli Hamiltonian is a Hermitian element $\tilde{H}_P = \frac{(\hat{\mathbf{p}}-q\mathbf{A})^2}{2m} + q\Phi - \frac{q\hbar}{2m} i\mathbf{B} \in \mathbb{M}_+$, and the spin precesses by the corresponding rotor conjugation. For a uniform magnetic field, only the last term contributes to the spin motion, and the precession frequency is the Larmor frequency $\omega_L = qB/m$ (natural units), or $\omega_L = g\,qB/2m$ in the g-form; up to the sign of $q$ this is the familiar spin precession. The two-component spinor description, the Pauli equation, and the precession are thus all consequences of the single biquaternionic Dirac equation.

## Massless case: the Weyl equations and chirality

Setting $m = 0$ decouples the two chiral components. In the chiral basis the Dirac equation becomes the pair of **Weyl equations**

$$
i\hbar\,\partial_t\psi_R = c\,\boldsymbol{\sigma}\cdot\hat{\mathbf{p}}\,\psi_R, \qquad
i\hbar\,\partial_t\psi_L = -\,c\,\boldsymbol{\sigma}\cdot\hat{\mathbf{p}}\,\psi_L,
$$

or, in covariant form, $\sigma^\mu\partial_\mu\psi_R = 0$ and $\bar{\sigma}^\mu\partial_\mu\psi_L = 0$ with the usual $\sigma^\mu = (I,\boldsymbol{\sigma})$, $\bar{\sigma}^\mu = (I,-\boldsymbol{\sigma})$ up to the metric convention. Each equation has a two-dimensional solution space, and each helicity is locked to a chirality: the right-handed field has positive helicity, the left-handed field negative helicity. The mass term is exactly what couples the two, and it is the only term in the equation that does so. The projectors

$$
P_L = \tfrac{1}{2}(1 - \gamma_5), \qquad P_R = \tfrac{1}{2}(1 + \gamma_5)
$$

select the two components, and the biquaternion algebra contains their algebraic counterparts as the central idempotents of the complexified even Clifford algebra discussed in the companion article. The Weyl spinors are thus the $m \to 0$ limit of the solutions constructed above, and the biquaternionic Dirac operator reduces in that limit to the pair of Weyl operators.

## Summary

The biquaternionic Dirac equation, in its spinor-module form $(i\gamma^\mu\partial_\mu - m)\psi = 0$, has plane-wave solutions in two branches. The positive-frequency branch is spanned by $u^{(r)}(\mathbf{p})e^{-i(Et-\mathbf{p}\cdot\mathbf{x})}$ and the negative-frequency branch by $v^{(r)}(\mathbf{p})e^{+i(Et-\mathbf{p}\cdot\mathbf{x})}$, with $E = +\sqrt{\mathbf{p}^2+m^2}$; both branches are the two roots of the single biquaternionic mass-shell condition $\tilde{k}\bar{\tilde{k}} = -m^2c^2/\hbar^2$. The spinors have an explicit two-component structure, displayed here in both the Dirac and the chiral bases. They satisfy the covariant normalizations $\bar{u}u = 2m$, $\bar{v}v = -2m$, the orthogonality $\bar{u}v = 0$, and the spin sums $\sum_r u\bar{u} = \not{p}+m$, $\sum_r v\bar{v} = \not{p}-m$.

The spinor bilinears have a clean biquaternion reading. The conserved vector current is the four-vector $\tilde{J} = ic\,j^0e_0 + \mathbf{j}$ in the material sector $\mathbb{M}_-$, while the rank-one Hermitian form built from a single two-component spinor is exactly the idempotent $\tfrac{1}{2}(e_0 + i\hat{\mathbf{n}})$ of the informational sector $\mathbb{M}_+$, so a Weyl spinor is a pure state of the informational sector. The scalar and pseudoscalar bilinears are the real and imaginary parts of the chirality-flipping bilinear $\psi_L^\dagger\psi_R$.

In the non-relativistic limit, factoring out the rest energy and eliminating the small component reduces the four-component equation to the Pauli equation

$$
i\hbar\,\partial_t\tilde{\phi} = \left[ \frac{(\hat{\mathbf{p}} - q\mathbf{A})^2}{2m} + q\Phi - \frac{q\hbar}{2m}\,\boldsymbol{\sigma}\cdot\mathbf{B} \right]\tilde{\phi},
$$

whose spin term is the Hermitian observable $-\frac{q\hbar}{2m} i\mathbf{B} \in \mathbb{M}_+$. The coefficient produced by the elimination is exactly the one required by $\boldsymbol{\mu} = g\frac{q}{2m}\mathbf{S}$ with $g = 2$, so the gyromagnetic factor and the spin–magnetic coupling are consequences of the biquaternionic mass term rather than separate postulates. In the massless limit the equation splits into the two Weyl equations, with chirality locked to helicity, which is the starting point for the treatment of chirality with Weyl spinors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\tilde{\nabla} = e_0\partial_{ict} + e_k\partial_k$ | Biquaternionic gradient (Dirac operator) |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$ | d'Alembertian |
| $\tilde{\Psi}$ | Biquaternion-valued Dirac field |
| $\tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger$ | Anti-Hermitian conjugate (the algebra's real structure; not the mass term) |

| $\tilde{k} = i k_0 e_0 + \mathbf{k}$ | Wave biquaternion |

| $\tilde{k}\bar{\tilde{k}} = -m^2c^2/\hbar^2$ | Biquaternionic mass-shell condition |
| $\psi = (\psi_L,\psi_R)$ | Dirac spinor in the chiral basis |
| $\gamma^\mu$, $\gamma_5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ | Gamma matrices and chirality operator |
| $g = \mathrm{diag}(+1,-1,-1,-1)$ | Clifford metric of the $\gamma^\mu$; note $g = -\eta$ |
| $\eta = \mathrm{diag}(-1,+1,+1,+1)$ | Spacetime metric of the $ict$ gradient |
| $\bar{\psi} = \psi^\dagger\gamma^0$ | Dirac adjoint |
| $u^{(r)}(\mathbf{p}),\, v^{(r)}(\mathbf{p})$ | Positive- and negative-frequency spinors |
| $p^\mu = (E,\mathbf{p})$, $\not{p} = \gamma^0E - \boldsymbol{\gamma}\cdot\mathbf{p}$ | Four-momentum and Feynman slash |
| $j^\mu = \bar{\psi}\gamma^\mu\psi$ | Conserved Dirac current |
| $\tilde{J} = ic\,j^0e_0 + \mathbf{j} \in \mathbb{M}_-$ | Current as a material-sector biquaternion |
| $\rho = \psi\psi^\dagger \mapsto \tfrac{1}{2}(e_0 + i\hat{\mathbf{n}})$ | Spin bilinear as an $\mathbb{M}_+$ idempotent |
| $q$ | Charge of the field under minimal coupling |
| $\mathbf{S} = \tfrac{\hbar}{2}\boldsymbol{\sigma}$, $\boldsymbol{\mu} = g\frac{q}{2m}\mathbf{S}$ | Spin and magnetic moment |
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
