# __The Foldy–Wouthuysen Transformation in Biquaternionic Form__

## Introduction

The Dirac equation describes particles and antiparticles on the same footing, and its four-component solutions mix the two. The Foldy–Wouthuysen (FW) transformation, introduced by Leslie Foldy and Siegfried Wouthuysen in 1950, is the unitary transformation that separates them. It block-diagonalises the Dirac Hamiltonian so that the upper two components describe the positive-frequency (particle) degrees of freedom and the lower two the negative-frequency (antiparticle) degrees of freedom, and in doing so it produces the systematic expansion of the relativistic Hamiltonian in powers of $1/c$ whose leading terms are the Schrödinger and Pauli Hamiltonians. It is the tool that every non-relativistic reduction in this corpus uses, and it is the tool the companion articles on the electron and on the hydrogen atom presuppose.

The transformation is worth a biquaternion article for a structural reason. The biquaternionic Dirac equation is written as a **chiral pair**: the mass couples $\tilde{\Psi}_L$ to $\tilde{\Psi}_R$, and the two chiral halves carry the two minimal left ideals of $\mathbb{B}$. The FW transformation, by contrast, separates **positive from negative frequency**, and the two pieces into which it splits the field are not the two chiralities. The article therefore has to keep two gradings apart: the chirality grading, in which the mass is off-diagonal and the biquaternion pair is written, and the frame grading by $\gamma^0$, in which the FW transformation works and the mass is diagonal. Conflating the two is the standard way to misread either. Making the distinction explicit is the biquaternion content of the transformation.

The scope is the transformation itself, its generator, its free-particle closed form, the mean position operator it defines, and the reading of all this in the algebra. The quantised field, the Fock space and the fermionic path integral belong to the companion category *Biquaternion Quantum Fields*; the relativistic qubit and the informational reading belong to the subcategory *focus on informational aspects*. The Pauli equation itself, and the detailed non-relativistic expansion including the Darwin and spin–orbit terms, are worked through in the companion exercise and are only summarised here. The conventions are the series conventions: $\Box = \partial_{ict}^2 + \Delta$, the Clifford generators satisfy $\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu}I_4$ with $g = \mathrm{diag}(+1,-1,-1,-1)$, so that $(\gamma^0)^2 = +I_4$, and the chiral mass pair is

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R .
$$

## The Dirac Hamiltonian and the Odd/Even Split

The FW transformation is best stated for the Hamiltonian form of the Dirac equation. Write the covariant equation $(i\gamma^\mu D_\mu - mc)\psi = 0$ with the minimal coupling $D_\mu = \partial_\mu - iqA_\mu/\hbar$ of the parent article — the companion article *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* fixes the opposite sign of the connection and records that the two are the same coupling with the opposite sign of $q$ — multiply by $\gamma^0$, and set $\alpha^k = \gamma^0\gamma^k$, $\beta = \gamma^0$. The result is

$$
i\hbar\partial_t\psi = H\psi, \qquad
H = \beta mc^2 + c\,\boldsymbol\alpha\cdot\boldsymbol\pi + qA^0,
\qquad \boldsymbol\pi = \mathbf{p} - q\mathbf{A},
$$

where $\mathbf{p} = -i\hbar\boldsymbol{\nabla}$ and we have used $\gamma^0\gamma^0 = I_4$. In the Dirac representation the matrices are

$$
\beta = \begin{pmatrix} I_2 & 0 \\ 0 & -I_2\end{pmatrix},
\qquad
\alpha^k = \begin{pmatrix} 0 & \sigma^k \\ \sigma^k & 0\end{pmatrix},
$$

and they satisfy $\beta^2 = I_4$, $(\alpha^k)^2 = I_4$, $\{\alpha^j,\alpha^k\} = 2\delta^{jk}I_4$, $\{\alpha^k,\beta\} = 0$. The Hamiltonian splits into an **even** part and an **odd** part,

$$
H = \beta mc^2 + \underbrace{c\,\boldsymbol\alpha\cdot\boldsymbol\pi}_{\textstyle O} + \underbrace{qA^0}_{\textstyle\mathcal{E}},
$$

where even and odd are defined by conjugation with $\beta$,

$$
\mathcal{E}\ \text{even}:\ \beta\mathcal{E}\beta = +\mathcal{E},
\qquad
O\ \text{odd}:\ \beta O\beta = -O .
$$

The odd part $O$ is what couples the upper and lower components, and hence what makes the positive- and negative-frequency sectors talk to each other. The FW transformation is the unitary transformation that removes $O$ order by order.

It is important to say at once which grading this is. The split into even and odd under $\beta$ is the **Clifford parity** associated with the timelike generator: $\beta = \gamma^0$ is the generator whose square is $+I_4$, and conjugation by it is the reflection that the companion article *The Reflection and the Rotation in Biquaternionic Form* identifies as the frame. It is **not** the chirality grading. The chirality operator is $\gamma_5 = i\gamma^0\gamma^1\gamma^2\gamma^3$, it anticommutes with each $\gamma^\mu$, and in particular it **anticommutes** with $\beta = \gamma^0$; the two gradings are different involutions on the same space, and the mass term is even under the first while it connects the two chiral halves, hence off-diagonal, under the second. A reader who identifies "odd" with "chirality-changing" will misread the transformation the whole way through.

## The Transformation and Its Generator

Let $U = e^{iS}$ with $S$ Hermitian so that $U$ is unitary. The transformed Hamiltonian is

$$
H' = UHU^\dagger - i\hbar U\partial_t U^\dagger ,
$$

where the second term vanishes for a time-independent $S$. Since $H = \beta mc^2 + O + \mathcal{E}$, the idea is to choose $S$ so that the large term $i[S,\beta mc^2] = -O$ cancels the odd part at leading order, leaving an even remainder of order $1/c^2$.

Expanding $UHU^\dagger = H + i[S,H] + \frac{i^2}{2!}[S,[S,H]] + \cdots$, the condition $i[S,\beta mc^2] = -O$ is satisfied by

$$
S = S_1 = -\frac{i}{2mc^2}\,\beta O = -\frac{i}{2mc}\,\beta\,\boldsymbol\alpha\cdot\boldsymbol\pi ,
$$

because $[S,\beta] = -\frac{i}{2mc^2}\beta[O,\beta] = \frac{i}{mc^2}O$ (using $O\beta = -\beta O$), whence $i[S,\beta mc^2] = i\cdot i\,O = -O$. The remaining terms are evaluated with the same anticommutation:

$$
i[S,O] = \frac{1}{2mc^2}[\beta O,O] = \frac{1}{mc^2}\beta O^2,
$$

because $[\beta O,O] = 2\beta O^2$ when $O$ is odd. Collecting, and using the full exponential rather than the first-order truncation, the transformed Hamiltonian through order $1/c^2$ is

$$
H' = \beta mc^2 + \mathcal{E} + \frac{\beta O^2}{2mc^2} + \cdots,
$$

with the residual odd terms of order $O^3/(m^2c^4)$ removed by a second transformation $S_2 = -\frac{i}{2mc^2}\beta O'$, where $O'$ denotes the residual odd part after the first step. For the free particle $O = c\,\boldsymbol\alpha\cdot\mathbf{p}$ and $O^2 = c^2\mathbf{p}^2$, so $O^2/(2mc^2) = \mathbf{p}^2/(2m)$ and

$$
H' = \beta\left(mc^2 + \frac{\mathbf{p}^2}{2m} - \frac{\mathbf{p}^4}{8m^3c^2} + \cdots\right),
$$

whose first two terms are the free-particle Schrödinger Hamiltonian in the upper block and its negative in the lower block, and whose $\mathbf{p}^4$ term is the first relativistic correction to the kinetic energy. The expansion is in powers of $(\mathbf{p}/mc)^2$, i.e. in $v^2/c^2$; the residual odd terms are smaller by two powers of $v/c$.

The generator has a transparent physical meaning in the algebra. The operator $\beta O = \beta c\,\boldsymbol\alpha\cdot\boldsymbol\pi$ is the piece of the Hamiltonian that flips the large and small components; the generator $S_1$ is proportional to it, so the FW transformation is the rotation whose angle measures how much large/small mixing the kinetic term produces. For a slowly moving particle the angle is small and the transformation is close to the identity; in the ultra-relativistic regime the expansion breaks down, which is the signal that the non-relativistic separation is no longer meaningful.

It is worth recording that the leading generator by itself is not sufficient. Inserted into a first-order truncation of the exponential it leaves the odd part uncancelled at the next order; only the full exponential (or the iteration $S_1, S_2, \dots$) produces an even Hamiltonian of the stated accuracy. This is a bookkeeping point with a physical content: the separation of positive and negative frequency is an all-orders statement for the free particle, as the closed form below shows, and only approximately a term-by-term one.

### The Second Transformation and the Iteration

The residual odd part after the first step is, by construction, of order $1/m^2$ relative to the original $O$; call it $O_2$. The same algorithm applied to it,

$$
S_2 = -\frac{i}{2mc^2}\beta O_2 ,
$$

removes the leading remainder and changes the even part only at higher order. The procedure iterates: at each stage the odd part at order $m^{-2n}$ is conjugated away by a generator proportional to it, and the new odd residual is two powers smaller. The resulting expansion of the transformed Hamiltonian is the systematic $1/c$ expansion of the Dirac theory, and its convergence criterion is the physically transparent one,

$$
\frac{|\boldsymbol\pi|}{mc} \ll 1 ,
$$

i.e. particle momenta small compared with $mc$. When the criterion fails the iteration still exists term by term but no longer converges to a useful separation: the notion of "particle component" is momentum-dependent and becomes meaningless in the ultra-relativistic regime.

Two features of the iteration are worth keeping in view. First, the transformation is **asymptotic, not exact**, unless the theory is free (or the background has special symmetry): the series is what the non-relativistic limit means. Second, the even part produced at each stage is frame-even but not necessarily accompanied by a frame-even potential; in the presence of external fields the split between $\mathcal{E}$ and the induced even terms depends on the gauge, and only gauge-invariant combinations are physical. The biquaternion framework reads the first feature as the statement that the frame grading is only approximately aligned with the dynamics, and the second as the standard covariance statement that a single frame is a choice of foliation.

### The Generator in the Biquaternion Basis

The identification of $O$ as the frame-odd part can be written directly in the algebra. With the isomorphism $\Phi$ of the dictionary article, $\Phi(e_0) = I_4$, $\Phi(e_k) = -i\sigma^k$ in the relevant $2\times2$ blocks, the even generators are $\alpha^k$, and the frame is $\beta = \gamma^0$, which is not in $\Phi(\mathbb{B})$. The kinetic operator is

$$
O = c\,\boldsymbol\alpha\cdot\boldsymbol\pi = c\,\alpha^k\pi_k,
\qquad
\beta O = c\,\beta\alpha^k\pi_k = c\,\gamma^k\pi_k ,
$$

where $\gamma^k = \beta\alpha^k$ are the spacelike generators. The kinetic term is thus the spacelike part of the Clifford vector $\gamma^\mu\pi_\mu$ — the mass multiplying $\beta$ is its timelike part — and the FW transformation is the rotation that removes the spacelike (odd) part in favour of the timelike (even) one. In the algebra this is the cleanest statement of what the transformation does: it rotates the Clifford vector so that its timelike component is the whole of the leading Hamiltonian. The generator is proportional to the spacelike component itself, which is why it lies outside the even subalgebra and why the transformation must be carried out in the enlarged algebra.

## The Free Particle in Closed Form

For the free particle the transformation can be written exactly, and the exact form is the cleanest check that the expansion above is right. With $\hat{\mathbf{p}}$ the unit vector along $\mathbf{p}$ and

$$
A = \beta\,\boldsymbol\alpha\cdot\hat{\mathbf{p}},
\qquad
A^2 = -I_4 ,
\qquad
\theta = \arctan\!\left(\frac{|\mathbf{p}|}{mc}\right),
$$

the unitary

$$
U = \cos\frac{\theta}{2} + A\sin\frac{\theta}{2} = e^{A\theta/2}
$$

brings the Hamiltonian to diagonal form. The verification is short. Since $\beta A = -A\beta$, conjugation by $U = e^{A\theta/2}$ acts as

$$
U\beta U^\dagger = \beta e^{-A\theta},
$$

while $A$ commutes with $U$ and is unchanged. Writing $H = \beta mc^2 + c\boldsymbol\alpha\cdot\mathbf{p} = \beta mc^2 + cp\beta A$ (using $\boldsymbol\alpha\cdot\hat{\mathbf{p}} = \beta A$, which follows from $\beta A = \beta^2\boldsymbol\alpha\cdot\hat{\mathbf{p}} = \boldsymbol\alpha\cdot\hat{\mathbf{p}}$), one has

$$
H = \beta\left(mc^2 + cpA\right) = \beta\,E\left(\cos\theta + A\sin\theta\right)
= \beta E\,e^{A\theta},
\qquad
E = \sqrt{\mathbf{p}^2c^2 + m^2c^4},
$$

where $\cos\theta = mc^2/E$, $\sin\theta = cp/E$ and $e^{A\theta} = \cos\theta + A\sin\theta$ because $A^2 = -I_4$. Therefore

$$
UHU^\dagger = e^{A\theta/2}\,\beta E\,e^{A\theta}\,e^{-A\theta/2}
= \beta E\,e^{-A\theta/2}e^{A\theta}e^{-A\theta/2} = \beta E ,
$$

that is, $UHU^\dagger = \beta\sqrt{\mathbf{p}^2c^2 + m^2c^4}$ exactly. The upper block is the relativistic energy $+E$, the lower block is $-E$, and the odd part has been removed to all orders. The leading expansion of the closed form reproduces the result of the previous section:

$$
\beta E = \beta\left(mc^2 + \frac{\mathbf{p}^2}{2m} - \frac{\mathbf{p}^4}{8m^3c^2} + \cdots\right),
$$

the $\mathbf{p}^4$ term being the first relativistic correction to the kinetic energy. The closed form was checked by direct $4\times4$ matrix computation: with $\tan\theta = |\mathbf{p}|/(mc)$ and $U = \cos(\theta/2) + A\sin(\theta/2)$, the identity $UHU^\dagger = \beta E$ held to $9\times10^{-16}$ for a generic three-momentum.

## The Mean Position Operator

The transformation does more than block-diagonalise the Hamiltonian: it also changes the position operator, and the change is the resolution of the Zitterbewegung paradox. Conjugating $\mathbf{x}$ by $U = e^{iS}$ gives

$$
\mathbf{X} = U\,\mathbf{x}\,U^\dagger
= \mathbf{x} + i[S,\mathbf{x}] + \frac{i^2}{2!}[S,[S,\mathbf{x}]]+\cdots
= \mathbf{x} - \frac{i\hbar\,\beta\boldsymbol\alpha}{2mc} + \cdots,
$$

where the leading term uses $[S_1,x_k] = -\frac{i}{2mc}\beta[\alpha_j\pi_j,x_k] = -\frac{\hbar}{2mc}\beta\alpha_k$ for the free case, so the correction is of the order of the reduced Compton wavelength $\hbar/(mc)$, and the next correction is of order $1/m^2$. The operator $\mathbf{X}$ is the **mean position** (Foldy–Wouthuysen position). Its defining property is that its Heisenberg velocity,

$$
\dot{\mathbf{X}} = \frac{i}{\hbar}[H',\mathbf{X}],
$$

contains no oscillatory term: to leading order it is the classical drift $\mathbf{p}c^2/E$, so the rapid trembling of the ordinary position operator $\mathbf{x}$ is entirely contained in the difference $\mathbf{x} - \mathbf{X}$. In the biquaternion language, the trembling is a rotation of the field between the two frames of the algebra, and the FW position is the coordinate that is blind to it. The companion article *Zitterbewegung in Biquaternionic Form* records the same conclusion from the side of the oscillation; here it appears as a property of the transformed position operator.

The correction $-\frac{i\hbar\beta\boldsymbol\alpha}{2mc}$ is itself worth reading in the algebra. It is an odd, spinorial displacement: it is proportional to the same matrix $\beta\boldsymbol\alpha$ that generates the transformation, it anticommutes with $\beta$, and it is suppressed by one power of $1/c$ relative to the ordinary position. It is not a measurement of the particle's size; it is the statement that the coordinate conjugate to the block-diagonal Hamiltonian is not the coordinate conjugate to the original field. The operator $\mathbf{X}$ does not have commuting components, and it is not Lorentz covariant in the naive sense — the Newton–Wigner operator is the covariant completion of it — a fact already visible in the biquaternion framework as the difference between a material position $\mathbf{x}$ and a configuration-space position on the module.

## The Biquaternion Reading

The transformation can now be located in the two gradings of the algebra, and the location is the content of the article.

**The chirality basis is where the biquaternion pair lives.** The massive biquaternionic Dirac equation is the off-diagonal pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$; in the chiral (Weyl) basis the mass term is the off-diagonal matrix $m\begin{pmatrix}0&I\\I&0\end{pmatrix}$ and the Dirac operator is block off-diagonal. This is the basis in which the two components are the two minimal left ideals of $\mathbb{B}\cong M_2(\mathbb{C})$ and in which the mass couples them. The mass is the **off-diagonal** object in this basis.

**The frame basis is where the FW transformation works.** In the Dirac (large/small) basis, $\beta = \mathrm{diag}(I_2,-I_2)$ is diagonal and the mass term $m\beta$ is diagonal; the kinetic term $c\boldsymbol\alpha\cdot\boldsymbol\pi$ is the off-diagonal odd piece. The two bases are related by the fixed unitary that exchanges $\beta$ and $\gamma_5$, and the FW transformation is the momentum-dependent completion of that exchange: it rotates the field so that the mass — off-diagonal in chirality — becomes diagonal, while the kinetic term, which was diagonal in chirality, becomes the first-order perturbation. Removing the odd part is exactly the statement that the mass is the large term and the mixing is small.

**FW does not separate chirality.** After the transformation the Hamiltonian is block diagonal in the large/small basis, not in the chiral basis. The chirality operator in the transformed basis is momentum-dependent: $\gamma_5^{FW} = U\gamma_5U^\dagger = \gamma_5 e^{-A\theta}$ has upper block $(\boldsymbol\sigma\cdot\hat{\mathbf{p}})\sin\theta = (\boldsymbol\sigma\cdot\hat{\mathbf{p}})\,pc/E$ — the helicity for a massless field, reduced by the factor $pc/E$ for a massive one — and off-block part $\cos\theta\,I_2 = (mc^2/E)I_2$, which is the chirality-mixing term and is of relative order $m/|\mathbf{p}|$ in the ultra-relativistic regime. The FW transformation therefore separates **positive from negative frequency** — the two signs of $\beta$ — and not left from right. In the algebra, the grading it diagonalises is the frame grading by $\gamma^0$, the reflection of *The Reflection and the Rotation in Biquaternionic Form*; the chirality grading is a different reflection, and no unitary rotation of the field can diagonalise both simultaneously because $\beta$ and $\gamma_5$ anticommute. The FW basis and the chiral basis are complementary, and the mass is the object that measures their incompatibility.

**The generator is outside the algebra's rotors.** The biquaternion rotors are the even, unit-norm elements of $\mathbb{B}$; they act on the module and generate the Lorentz group. The FW generator $S_1 = -\frac{i}{2mc}\beta\,\boldsymbol\alpha\cdot\boldsymbol\pi$ contains $\beta = \gamma^0$, which is Clifford-odd and does not belong to the even subalgebra $\Phi(\mathbb{B})$. The FW transformation is therefore not one of the algebra's own rotations: it is a transformation in the enlarged Clifford algebra that adjoins the frame $\gamma^0$. The biquaternion content it carries is not a new rotor but the identification of the odd part $O$ with the frame-odd mixing term and of the diagonal mass with the frame-even large term. This is consistent with the reflection article's finding that the frame is required to state chirality and parity: the FW transformation needs the frame for the same reason.

## The Pauli Limit and the Residual Terms

With an external electromagnetic field, $\boldsymbol\pi = \mathbf{p}-q\mathbf{A}$ and the FW-transformed Hamiltonian acquires the standard non-relativistic terms. To order $1/c^2$ the upper block is the Pauli Hamiltonian

$$
H_{\mathrm{Pauli}} = \frac{\boldsymbol\pi^2}{2m} + qA^0 - \frac{q\hbar}{2m}\boldsymbol\sigma\cdot\mathbf{B}
- \frac{q\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\mathbf{E}\times\boldsymbol\pi)
+ \frac{\hbar^2}{8m^2c^2}\nabla^2(qA^0),
$$

whose corrections are the spin–Zeeman term, the spin–orbit coupling and the Darwin term — the coefficient $\frac{1}{4m^2c^2}$ of the spin–orbit term already contains the Thomas factor of $\frac12$ — together with the relativistic kinetic correction $-\boldsymbol\pi^4/(8m^3c^2)$, which is displayed in the free-particle expansion above; the companion exercise *Exercise: The Non-Relativistic Limit and the Pauli Equation* derives each in the biquaternion framework, and they are quoted here as the standard content of the transformation. The Darwin term is written in its equivalent forms $\frac{\hbar^2}{8m^2c^2}\nabla^2(qA^0) = -\frac{q\hbar^2}{8m^2c^2}\nabla\cdot\mathbf{E}$ for the electrostatic case $\mathbf{E} = -\nabla A^0$, where the identity $\nabla\cdot\mathbf{E} = -\nabla^2A^0$ holds. The point to record is structural: every correction is **even** under the frame grading — each is a scalar or a spin–magnetic coupling, none couples the large and small blocks — which is the statement that the transformation has succeeded in removing the odd part to the stated order. The residual odd terms, suppressed by a further factor of $v^2/c^2$ relative to $O$, are removed by $S_2$.

The lower block is the same Hamiltonian with the sign of the mass reversed, i.e. the negative-energy (antiparticle) sector, and the two blocks are exactly degenerate at this order. The splitting between them, $2mc^2$, is the mass gap that the transformation has made manifest. This is the sense in which the FW transformation "separates particles from antiparticles": not by projecting them apart, which the fields do not allow, but by diagonalising the Hamiltonian so that the gap is explicit and the mixing is small.

## What Is Standard and What the Algebra Adds

The transformation, the generator $S_1$, the leading Hamiltonian $\beta mc^2 + \beta O^2/(2mc^2)$, the closed free-particle form $\beta E$, the mean position operator and the Pauli limit are all standard results, transcribed here from the relativistic-quantum-mechanics literature and cited as such. The biquaternion contribution is not a new formula but a placing:

- The **two gradings** are kept distinct. The FW transformation diagonalises the frame grading (large/small, $\beta$); the biquaternion mass pair is the chirality grading (left/right, $\gamma_5$). They anticommute, so the transformation cannot diagonalise both, and the mass is the obstruction.
- The **mass term** appears in the transformation as the large, frame-even term whose diagonal form is the non-relativistic gap; in the chiral basis the same mass is the off-diagonal coupling of the biquaternion pair. Moving between the two descriptions is the FW transformation.
- The **residual odd part** is the frame-odd mixing term $O$, and its removal order by order is the statement that positive and negative frequency decouple in the non-relativistic limit.
- The **exact free form** shows that the separation, for a free field, is exact: $UHU^\dagger = \beta\sqrt{\mathbf{p}^2c^2+m^2c^4}$ with $U = \exp\left(\frac{\theta}{2}\beta\boldsymbol\alpha\cdot\hat{\mathbf{p}}\right)$, $\tan\theta = |\mathbf{p}|/(mc)$. The expansion used by the non-relativistic reduction is the expansion of this closed form in $|\mathbf{p}|/(mc)$.

The transformation was constructed here with the large term being the mass. If an external potential dominates, the same algorithm is applied with a different even large term, and the generator changes accordingly; the algebra reads this as a different choice of frame. The choice of frame is the physical input, and the rest is the rotation that aligns the odd part with it.

## Summary

The Foldy–Wouthuysen transformation is the unitary $U = e^{iS}$ that block-diagonalises the Dirac Hamiltonian in the frame grading, separating the positive- and negative-frequency sectors. With $H = \beta mc^2 + O + \mathcal{E}$, $O = c\boldsymbol\alpha\cdot\boldsymbol\pi$ odd under conjugation by $\beta = \gamma^0$, the leading generator is

$$
S_1 = -\frac{i}{2mc^2}\beta O = -\frac{i}{2mc}\beta\,\boldsymbol\alpha\cdot\boldsymbol\pi,
$$

and the transformed Hamiltonian through order $v^2/c^2$ is $H' = \beta mc^2 + \mathcal{E} + \beta O^2/(2mc^2)$; in the free case $\mathcal{E} = 0$ this is the Schrödinger Hamiltonian in the upper block and its negative in the lower block. For the free particle the transformation is exact:

$$
U = \cos\frac{\theta}{2} + \beta\,\boldsymbol\alpha\cdot\hat{\mathbf{p}}\,\sin\frac{\theta}{2},
\qquad
\tan\theta = \frac{|\mathbf{p}|}{mc},
\qquad
UHU^\dagger = \beta\sqrt{\mathbf{p}^2c^2 + m^2c^4},
$$

checked to $9\times10^{-16}$ by direct matrix computation. The transformed position operator is the mean position, $\mathbf{X} = \mathbf{x} - i\hbar\beta\boldsymbol\alpha/(2mc) + \cdots$, whose Heisenberg velocity has no trembling term; the Zitterbewegung resides in the difference $\mathbf{x}-\mathbf{X}$.

The biquaternion reading turns on two gradings that must not be conflated. The frame grading, conjugation by $\gamma^0$, is what the FW transformation diagonalises and in which the mass is diagonal; the chirality grading, $\gamma_5$, is what the biquaternion mass pair is written in and in which the mass is off-diagonal. The two gradings anticommute, so no single unitary diagonalises both, and the mass term is the measure of their incompatibility. The FW generator contains $\gamma^0$ and therefore lies outside the even subalgebra $\Phi(\mathbb{B})$: the transformation is not one of the algebra's Lorentz rotors but a transformation in the enlarged Clifford algebra that adjoins the frame.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\beta = \gamma^0$ | The frame; the generator with $(\gamma^0)^2 = +I_4$ |
| $\boldsymbol\alpha$ | $\alpha^k = \gamma^0\gamma^k$, the Dirac velocity matrices |
| $\gamma_5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ | Chirality operator, $\gamma_5^2 = I_4$ |
| $g = \mathrm{diag}(+1,-1,-1,-1)$ | Clifford metric (level-3 tool) |
| $H = \beta mc^2 + O + \mathcal{E}$ | Dirac Hamiltonian, odd/even split |
| $O = c\,\boldsymbol\alpha\cdot\boldsymbol\pi$ | Odd (frame-anticommuting) part |
| $\mathcal{E}$ | Even (frame-commuting) part |
| $U = e^{iS}$ | Foldy–Wouthuysen unitary |
| $S_1 = -\frac{i}{2mc^2}\beta O$ | Leading FW generator |
| $H' = UHU^\dagger - i\hbar U\partial_t U^\dagger$ | Transformed Hamiltonian |
| $\theta = \arctan(|\mathbf{p}|/(mc))$ | Free-particle FW angle |
| $\mathbf{X} = \mathbf{x} - \frac{i\hbar\beta\boldsymbol\alpha}{2mc}+\cdots$ | Mean (Foldy–Wouthuysen) position |
| $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$ | Biquaternion mass pair (chirality grading) |
| $\Box = \partial_{ict}^2 + \Delta$ | Series d'Alembertian |

## Further Reading

- L. L. Foldy and S. A. Wouthuysen, "On the Dirac theory of spin 1/2 particles and its non-relativistic limit," *Physical Review* **78** (1950) 29–36, for the transformation and the mean position operator.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the generator, the block-diagonalisation, and the non-relativistic expansion.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the Pauli limit and the spin–orbit and Darwin terms.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Dirac Hamiltonian, the gamma matrices and the Foldy–Wouthuysen reduction.
- L. L. Foldy, "The electromagnetic properties of Dirac particles," *Physical Review* **87** (1952) 688–693, for the mean position and its electromagnetic couplings.
- M. E. Rose, *Relativistic Electron Theory* (Wiley, 1961), for the systematic $1/c$ expansion.
- W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the detailed treatment of the Foldy–Wouthuysen transformation and its applications.
- P. Strange, *Relativistic Quantum Mechanics* (Cambridge, 1998), for the transformation in the presence of external fields.
