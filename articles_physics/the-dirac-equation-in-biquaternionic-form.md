# __The Dirac Equation in Biquaternionic Form__

## Introduction

The Dirac equation is the relativistic wave equation for spin-$\frac{1}{2}$ particles. It was discovered by Paul Dirac in 1928 as an attempt to reconcile quantum mechanics with special relativity, and it predicted the existence of antimatter. It is one of the foundational equations of quantum field theory, and it is the equation that governs electrons, quarks, and all fermions.

The Dirac equation is usually written in terms of the **gamma matrices** $\gamma^\mu$, which satisfy the anticommutation relations

$$
\gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2g^{\mu\nu} I,
$$

where $g^{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$ is the Clifford metric of the generators and $I$ is the identity matrix. The gamma matrices generate the Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{R})$, and the Dirac equation is the statement that the Dirac operator $\not\partial = \gamma^\mu \partial_\mu$ annihilates the spinor field.

This article develops the biquaternionic formulation of the Dirac equation. The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is isomorphic, as a real algebra, to the **even subalgebra** of the Clifford algebra $\mathrm{Cl}_{1,3}$, and the biquaternionic gradient $\tilde{\nabla}$ plays the role of the Dirac operator. The Dirac equation in biquaternionic form is therefore a first-order equation on the biquaternion algebra.

The article is organized as follows. First the standard Dirac equation is reviewed, then the biquaternion algebra and its relation to $\mathrm{Cl}_{1,3}$ are recalled, then the biquaternionic Dirac operator is defined, and finally the biquaternionic Dirac equation is stated and solved. The article closes with the relativistic kinematics (four-velocity, four-momentum, mass-shell relation), the relation to the Maxwell equation, the plane-wave solutions, and the mass term.

The conventions are those of the companion articles: the biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, the scalar imaginary is $i$, and the biquaternionic gradient is $\tilde{\nabla} = e_0 \partial_{ict} + e_1 \partial_x + e_2 \partial_y + e_3 \partial_z$. The Minkowski metric has signature $(-,+,+,+)$, so that $\partial_{ict}^2 = -\partial_t^2/c^2$. Throughout this article, the symbol $c$ denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ denotes the **vacuum speed of light**, $c_0 = 1/\sqrt{\epsilon_0\mu_0}$. In vacuum, $c = c_0$. The symbol $v$ is reserved for particle and frame velocities.

## The Standard Dirac Equation

### The Gamma Matrices

The **gamma matrices** $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ are $4\times 4$ complex matrices satisfying the anticommutation relations

$$
\gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2g^{\mu\nu} I_4,
$$

where $g^{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$ is the Clifford metric of the generators and $I_4$ is the $4\times 4$ identity. They generate the Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{R})$, which has real dimension $16$; in standard counting $\mathrm{Cl}_{p,q}$ carries $p$ generators squaring to $+1$ and $q$ squaring to $-1$, so $(\gamma^0)^2 = +I_4$, $(\gamma^k)^2 = -I_4$, and $\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$. The metric $\eta = \mathrm{diag}(-1,+1,+1,+1)$ of the $ict$ gradient is a separate object and is unchanged; the two differ by the sign of the generators' square.

In the **Dirac representation**, the gamma matrices are

$$
\gamma^0 = \begin{pmatrix} I_2 & 0 \\ 0 & -I_2 \end{pmatrix}, \qquad
\gamma^k = \begin{pmatrix} 0 & \sigma^k \\ -\sigma^k & 0 \end{pmatrix}, \quad k = 1, 2, 3,
$$

where $\sigma^k$ are the Pauli matrices. These are the usual **mostly-minus** Dirac representation, and they satisfy the metric declared above: $(\gamma^0)^2 = +I_4$ and $(\gamma^k)^2 = -I_4$, so squaring reproduces $(\gamma^\mu)^2 = g^{\mu\mu} I_4$ and the anticommutation relation holds as stated.

### The Dirac Equation

The **Dirac equation** for a free fermion of mass $m$ is

$$
(i\not\partial - m)\psi = 0,
$$

where $\not\partial = \gamma^\mu \partial_\mu$ is the **Dirac operator**, $\psi$ is a four-component complex **Dirac spinor**, and $m$ is the mass. With the mostly-minus generators the factor of $i$ is explicit, as in the standard treatment; in natural units $\hbar = c = 1$ the equation is

$$
(i\gamma^\mu \partial_\mu - m)\psi = 0.
$$

For a massless fermion ($m = 0$), the equation reduces to

$$
i\not\partial\psi = 0.
$$

Squaring the Dirac operator gives the Klein–Gordon operator:

$$
(i\not\partial)^2 = -\not\partial^2 = -g^{\mu\nu}\partial_\mu\partial_\nu = \eta^{\mu\nu}\partial_\mu\partial_\nu = \Box,
$$

where $\Box = \eta^{\mu\nu} \partial_\mu \partial_\nu = -\partial_t^2/c^2 + \Delta$ is the d'Alembertian, with $\eta = -g$ the $ict$ metric of the material sector. So every solution of the massless Dirac equation is a solution of the wave equation.

### Spinors and the Lorentz Group

The Dirac spinor $\psi$ is not a vector under the Lorentz group; it transforms in the **spinor representation** of the Lorentz group. The spinor representation is a double cover of the vector representation: a rotation by $2\pi$ in the vector representation corresponds to a rotation by $2\pi$ in the spinor representation, but a rotation by $4\pi$ is the identity in the spinor representation, not $2\pi$.

The spinor representation is two-dimensional over $\mathbb{C}$ (for the **Weyl spinor**), and the Dirac spinor is a pair of Weyl spinors:

$$
\psi = \begin{pmatrix} \psi_L \\ \psi_R \end{pmatrix},
$$

where $\psi_L$ and $\psi_R$ are the left- and right-handed Weyl spinors. The Dirac equation couples $\psi_L$ and $\psi_R$ through the mass term.

## The Biquaternion Algebra and $\mathrm{Cl}_{1,3}$

### The Isomorphism

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is isomorphic, as a **real algebra**, to the **even subalgebra** $\mathrm{Cl}_{1,3}^+$ of the real Clifford algebra $\mathrm{Cl}_{1,3}$. The even subalgebra consists of products of an even number of gamma matrices: the identity $I$, the six bivectors $\gamma^\mu\gamma^\nu$ with $\mu < \nu$, and the pseudoscalar $\gamma^0\gamma^1\gamma^2\gamma^3$. It has real dimension $8$, matching the real dimension of $\mathbb{B}$.

**A note on the convention.** It is important to keep two things distinct. The biquaternion algebra $\mathbb{B}$ is a **real algebra of dimension 8**, and it is the even part of the **real** Clifford algebra. It is **not** the even part of the **complexified** Clifford algebra $\mathbb{C}\otimes \mathrm{Cl}_{1,3}$, which has complex dimension 8 (real dimension 16) and is isomorphic to $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$.

**The isomorphism.** The bivectors of $\mathrm{Cl}_{1,3}^+$ span a 6-dimensional real space. Three of them are timelike-spacelike, $\gamma^0\gamma^k$, and have square $+I$. Three are spacelike-spacelike, $\gamma^j\gamma^k$ with $j,k \in \{1,2,3\}$, and have square $-I$. The three spacelike bivectors generate a copy of the quaternions $\mathbb{H}$ inside $\mathrm{Cl}_{1,3}^+$. The isomorphism is given by mapping the quaternion units to three mutually anticommuting spacelike bivectors, oriented so that $e_1 e_2 = e_3$. Concretely, one valid assignment is

$$
e_1 \mapsto \gamma^2\gamma^3, \qquad e_2 \mapsto \gamma^3\gamma^1, \qquad e_3 \mapsto \gamma^1\gamma^2.
$$

The choice of which bivector corresponds to which quaternion unit is a convention; different choices are related by rotations of the spatial frame. With the mostly-minus generators the three signs can be taken positive simultaneously, since $(\gamma^2\gamma^3)(\gamma^3\gamma^1) = \gamma^1\gamma^2$ and $e_1e_2 = e_3$; under the opposite sign of the metric that is impossible, and one of the three bivectors must be reversed.

The scalar imaginary $i$ of $\mathbb{B}$ corresponds to the pseudoscalar $\gamma^0\gamma^1\gamma^2\gamma^3$ of $\mathrm{Cl}_{1,3}$, up to a sign. This correspondence is what makes the complexification of the quaternions inside $\mathbb{B}$ match the complexification of the even Clifford algebra.

### The Gamma Matrices from the Biquaternion Units

The biquaternion units give an explicit set of gamma matrices. Write the biquaternion algebra as $M_2(\mathbb{C})$ by $e_0 \mapsto I_2$, $e_k \mapsto -i\sigma^k$, $i \mapsto iI_2$, so that $ie_k \leftrightarrow \sigma^k$, and arrange the units in $2 \times 2$ blocks:

$$
\gamma^0 = \begin{pmatrix} 0 & e_0 \\ e_0 & 0 \end{pmatrix}, \qquad
\gamma^k = \begin{pmatrix} 0 & i e_k \\ -i e_k & 0 \end{pmatrix}, \qquad k = 1,2,3 ,
$$

that is, $\gamma^0 = \begin{pmatrix} 0 & I_2 \\ I_2 & 0 \end{pmatrix}$ and $\gamma^k = \begin{pmatrix} 0 & \sigma^k \\ -\sigma^k & 0 \end{pmatrix}$. The Clifford relations are then the quaternion relations in disguise. From the multiplication table and $i^2 = -1$, $e_k^2 = -e_0$,

$$
(\gamma^0)^2 = e_0^2 = +I_4, \qquad (\gamma^k)^2 = (ie_k)(-ie_k) = -i^2 e_k^2 = -I_4 .
$$

The mixed products are block diagonal: $\gamma^0\gamma^k = \mathrm{diag}(-ie_k,\, ie_k)$ and $\gamma^k\gamma^0 = -\gamma^0\gamma^k$, while $\gamma^j\gamma^k = \mathrm{diag}(e_je_k,\, e_je_k)$ and $\gamma^k\gamma^j = -\, \gamma^j\gamma^k$ because $e_je_k = -e_ke_j$. Hence

$$
\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu} I_4, \qquad g = \mathrm{diag}(+1,-1,-1,-1),
$$

and the verification uses nothing beyond the quaternion multiplication table and $i^2 = -1$. This is the declared metric of the introduction and of the section above. The overall sign of the metric is a convention: replacing every generator by $i\gamma^\mu$ flips the sign of $g$ and leaves the Clifford algebra unchanged, so the mostly-plus set is $i$ times the set displayed here.

### The Dirac Operator in Biquaternion Form

The biquaternionic gradient

$$
\tilde{\nabla} = e_0 \partial_{ict} + e_1 \partial_x + e_2 \partial_y + e_3 \partial_z
$$

is the biquaternion form of the Dirac operator. The correspondence with the gamma-matrix Dirac operator $\not\partial = \gamma^\mu \partial_\mu$ is through the isomorphism $\mathbb{B} \cong \mathrm{Cl}_{1,3}^+$: the biquaternion units $e_k$ correspond to spacelike bivectors, and the scalar unit $e_0$ corresponds to the identity $I$.

The biquaternionic gradient satisfies the factorization

$$
\tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \Box,
$$

which is the biquaternion form of the factorization $\not\partial^2 = \Box$. The two factorizations use the same algebraic relation between the basis elements and the metric.

### The Difference from the Matrix Form

The matrix Dirac operator $\not\partial$ acts on four-component complex spinors (the Dirac spinors), while the biquaternionic gradient $\tilde{\nabla}$ acts on biquaternions. The two formulations are related by the isomorphism

$$
\mathrm{Cl}_{1,3} \cong M_4(\mathbb{C}),
$$

under which the even subalgebra $\mathrm{Cl}_{1,3}^+$ corresponds to a subalgebra of $M_4(\mathbb{C})$ isomorphic to $M_2(\mathbb{C})$. The biquaternion algebra $\mathbb{B}$ is then isomorphic to $M_2(\mathbb{C})$ (article 5), and the action of $\tilde{\nabla}$ on the biquaternion algebra corresponds to the action of $\not\partial$ on a two-dimensional complex spinor module.

So the biquaternion formulation of the Dirac equation is expressed in terms of the biquaternion algebra, whose elements can be viewed as **pairs of two-component Weyl spinors**. The full four-component Dirac spinor is recovered by taking the direct sum of the two-component spinor module with its complex conjugate.

### An Explicit Dictionary with Conjugation in the Mass Term

The route to the algebra used so far is the framework's own: the biquaternion field is a pair of Weyl spinors, the two chiral components are the two minimal left ideals, and the mass couples them. There is a second route, due to V. V. Kravchenko (1995), which is a **dictionary** rather than a decomposition. It is an explicit real-linear bijection $A$ from the four-component bispinors onto the biquaternion-valued functions under which the Dirac equation becomes one biquaternionic equation; its interest for this article is that it is $\mathbb{R}$-linear rather than $\mathbb{C}$-linear, and that its mass term carries complex conjugation.

**The dictionary.** On the field side the dictionary pairs the four Dirac generators with the four operators the algebra offers: the spatial generators act by left multiplication by the imaginary units, the timelike generator by complex conjugation, and the central imaginary acts on the right,

$$
A(\gamma_0\Phi) = \bigl(A(\Phi)\bigr)^{*}, \qquad A(i\Phi) = -A(\Phi)\,i_3 ,
$$

the second of which is the statement that $A$ is $\mathbb{R}$-linear and not $\mathbb{C}$-linear. Under it the Dirac equation becomes the single biquaternionic equation

$$
\mathcal{N}F := \left(i\partial_0 + D - m\,i\,C M_{i_3}\right)F = 0, \qquad D = i\sum_{k=1}^{3} e_k\partial_k ,
$$

where $C$ is componentwise complex conjugation and $M_{i_3}$ is right multiplication by $i_3$; following the source, $i_1,i_2,i_3$ denote the quaternion units — the $e_1,e_2,e_3$ of this article — alongside the scalar imaginary $i$.

**The generators, one by one.** The source states the dictionary on the whole Clifford basis and not only on the timelike generator, and it is those further entries that fix the spatial assignment. On the field side it is given in components,

$$
A(\Phi) = \bigl(\mathrm{Re}\,\Phi_0 + i\,\mathrm{Im}\,\Phi_2\bigr)i_0
+ \bigl(\mathrm{Im}\,\Phi_1 - i\,\mathrm{Re}\,\Phi_3\bigr)i_1
- \bigl(\mathrm{Re}\,\Phi_1 + i\,\mathrm{Im}\,\Phi_3\bigr)i_2
- \bigl(\mathrm{Im}\,\Phi_0 - i\,\mathrm{Re}\,\Phi_2\bigr)i_3 ,
$$

with $i_0 = 1$: the eight real coordinates $\mathrm{Re}\,\Phi_\mu,\mathrm{Im}\,\Phi_\mu$ are carried to eight independent real coordinates, which is the sense in which $A$ is a real-linear **bijection** of $\mathbb{C}^4$ onto $\mathbb{B}$. On the generators it reads

$$
A(\gamma_0\gamma_1\Phi) = -i\,i_1A(\Phi), \qquad
A(\gamma_0\gamma_2\Phi) = -i\,i_2A(\Phi), \qquad
A(\gamma_0\gamma_3\Phi) = +i\,i_3A(\Phi),
$$

$$
A(\gamma_5\Phi) = -i\,A(\Phi)\,i_3 , \qquad \gamma_5 := -i\,\gamma_0\gamma_1\gamma_2\gamma_3 .
$$

Each of the three bivector entries is a left multiplication by a unit of the algebra composed with the scalar imaginary, so the spatial generators are complex-linear and the timelike generator alone is antilinear; the entry for the volume element is a **right** multiplication, on the side and through the unit that the mass term of $\mathcal{N}$ already carries. The signs of the three bivectors are not uniform — two take $-i$ and the third $+i$ — and the exception falls on the third axis, the unit $i_3$ of the mass term. That pattern is a property of the definition of $A$ and not of the Clifford relations, which do not distinguish the three spatial directions among themselves: the dictionary singles out the third axis on its own, and it is the same axis that the mass term couples to from the right.

**The chirality sign.** The source's volume element is the negative of the corpus's: it sets $\gamma_5 = -i\gamma_0\gamma_1\gamma_2\gamma_3$, whereas the chirality operator of *Chirality and the Gamma-Five Operator* below is $\gamma_5 = +i\gamma^0\gamma^1\gamma^2\gamma^3$. In the corpus's convention the last identity above therefore reads $A(\gamma_5\Phi) = +iA(\Phi)\,i_3$, and the sign has to be carried along whenever the two are compared. What does not depend on that one sign is the structure the entry states: the volume element of the dictionary acts by a right multiplication through the unit $i_3$, exactly as the mass term does, and not by a left multiplication like the three spatial generators.

**Recomputed.** The algebra facts that make the dictionary possible are that $C$ is an antilinear involution, $C^2 = I$; that left multiplication by each $ie_k$ is a complex-linear involution of the algebra, $L_{ie_k}^2 = I$; that the three anticommute pairwise, $L_{ie_k}L_{ie_l} + L_{ie_l}L_{ie_k} = 2\delta_{kl}I$; and that $C$ anticommutes with every one of them, $C L_{ie_k} + L_{ie_k} C = 0$. The three complex-linear left multiplications together with the antilinear conjugation therefore satisfy the Clifford anticommutation relations, and the timelike generator is the only one of the four that is antilinear. This is the algebraic content of the statement that the Dirac matrices can be built from the algebra's units together with its complex conjugation.

**Which conjugation.** The $C$ of the dictionary is the algebra's **complex conjugation** $\bar{\cdot}$, not the algebra's real structure $\flat$. They are different maps with different fixed spaces — $\bar{\cdot}$ fixes the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$, $\flat$ fixes the material sector $\mathbb{M}_-$ — and the corpus keeps them apart (*Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, and the convention remark of *The Massive Case* above). The distinction has teeth here, because the dictionary's mass term is antilinear and the framework has already found that not every antilinear mass term is admissible. The retired single-field equation $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^{\flat}$ fails on the dispersion, whereas the Lanczos form $\tilde{\nabla}D = mD^{*}i\vec{\nu}$ of *The Lanczos Route* is exact. Kravchenko's mass term is of the second kind: its conjugation is $\bar{\cdot}$, and it is accompanied by a right multiplication by a spatial direction, its $M_{i_3}$ standing where the Lanczos unit vector $\vec{\nu}$ stands. The corpus reads the two as one structure — a conjugation together with a direction, rather than the algebra's real structure — and the dictionary is the second explicit instance of it.

**The price, and its refund.** Because $C$ is antilinear, $\mathcal{N}$ is not left multiplication by an element of the algebra, so the Cauchy kernel, the Teodorescu transform and the boundary-value theory do not apply to it as it stands. The conjugation is removed by factoring $\mathcal{N}$ into two complex-linear equations and changing variable; the time-harmonic amplitude then obeys a **shifted** equation with a biquaternionic parameter, $D_\alpha\tilde{p} = 0$, treated in *Biquaternion Regular Functions* and used in *Confinement and the Loss of Partonic Information in Biquaternionic Form*. The conjugation is thus the cost of shrinking a four-component spinor to a single biquaternion, and it is refunded whenever the boundary-value theory is what is wanted.

### The Conjugation-Free Operator, Its Reality, and the Involutive Symmetry

The dictionary above pays for its compactness with the conjugation: $\mathcal{N}$ carries $C$, and that is what obstructs the Cauchy theory. The same source takes the conjugation off the operator and puts it into the change of variable. With $M_a$ the right multiplication $f\mapsto f a$, and with the complementary idempotents

$$
P_k^{\pm} := \tfrac12 M_{(1 \pm i\,i_k)}, \qquad k = 1,2,3 ,
$$

the operator

$$
R := P_1^{+}\bigl(i\partial_t + D\bigr) + P_1^{-}\bigl(-i\partial_t + D\bigr) - m\,M_{i_2}
$$

is related to $\mathcal{N}$ by

$$
\mathcal{N} = u^{+} R\, u^{-},
$$

where $u^{\pm}$ are built from the same idempotents and the same conjugation. The conjugation has not been removed, only moved: it now sits in the two factors that surround the operator, and the operator itself is free of it.

**The reality of $R$, recomputed.** The two projectors collapse, because $P_1^{+}+P_1^{-}=1$ and $P_1^{+}-P_1^{-}=i\,i_1$. Their definitions therefore give

$$
R = D - \partial_t M_{i_1} - m\,M_{i_2} ,
$$

whose coefficients are the three quaternion units and the right multiplications by $i_1$ and $i_2$ — all real quaternions, and no central imaginary. The collapse was checked here on the multiplication table, in this right-multiplication reading of $P_k^{\pm}$ and in the left-multiplication one; both give an operator with coefficients in $\mathbb{H}$. So $R$ contains **no complex conjugation**, and that is the property the 2003 paper names when it calls the quaternionic Dirac operator **real**.

**Real and imaginary parts are separately solutions.** Since no coefficient of $R$ carries the central imaginary, $R$ commutes with the dictionary's complex conjugation,

$$
R\bigl[\overline{F}\bigr] = \overline{R[F]} ,
$$

the bar being componentwise. Writing $F = \mathrm{Re}\,F + i\,\mathrm{Im}\,F$ and using that commutation, a solution of $R F = 0$ splits into two solutions:

$$
R\bigl[\mathrm{Re}\,F\bigr] = 0, \qquad R\bigl[\mathrm{Im}\,F\bigr] = 0 .
$$

One quaternionic solution therefore carries two Dirac solutions. This doubling is the paper's stated purpose: the real operator is offered as a contribution to a *real* Dirac theory, and it is obtained without the conjugation operator, in the real quaternion algebra rather than in the complexified one.

**The current, and the modulus.** For a real $F$ the quaternionic conjugate of the equation is the equation of the conjugate field, and from the pair the paper derives the conservation law

$$
\partial_t|F|^2 = -\hbar\bigl[(DF^{\dagger})F + F^{*}(DF)\bigr],
\qquad |F|^2 := F\bar{F},
$$

which is the quaternionic form of the current-conservation equation of the Dirac field. The modulus that appears in it is not an independent object: the dictionary carries it to the Dirac density, $|F|^2 = |\Phi|^2 = \sum_\mu|\Phi_\mu|^2$, so that the algebraic norm of the biquaternionic field *is* the probability density of the spinor. That is the paper's Remark 2, and it is the same norm that the corpus reads as the biquaternion norm $N$ in the kinematic sections above — here computed on the real representative of the solution.

**The involutive symmetry.** Carried back through the dictionary, the splitting becomes a symmetry of the Dirac equation: if $\Phi$ solves the Dirac equation, then $A^{-1}[\mathrm{Re}\,F]$ solves it again. The paper states that second solution in the Dirac matrices as

$$
\Phi' = i Z_c \Phi ,
$$

$Z_c$ being componentwise complex conjugation. Since $iZ_c$ is antilinear with $(iZ_c)^2 = 1$, the map is an **involution**: applying it twice returns the spinor. The paper records that such a symmetry had been obtained before by other methods (Niederle and Nikitin, 1997), and it claims the route rather than the result — the reality of the conjugation-free operator is what produces the symmetry here.

**What is quoted, and what is verified.** The factors $u^{\pm}$ of the factorisation $\mathcal{N} = u^{+}Ru^{-}$, and with them the explicit action of $A^{-1}$ on $\mathrm{Re}\,F$, stand in the source in formulas the scan does not resolve; they are quoted, not reproduced. The operator $R$, its collapse to $D-\partial_t M_{i_1}-mM_{i_2}$, the commutation of $R$ with complex conjugation, and the involution property $(iZ_c)^2=1$ are legible, and all four are verified here.

### The Harmonic Spinor Field: Two Projections, and the Helicity Reading

The same source carries the dictionary one step further, to the field that oscillates in time, and that is where the algebra is read physically. For the free massive Dirac equation (the section above) and the time-harmonic ansatz $\Psi(t,\mathbf{x}) = \psi(\mathbf{x})e^{i\omega t}$ with $\omega\in\mathbb{R}$, the dictionary image of the general solution is a **sum of two exponentials with opposite signs**,

$$
F(t,\mathbf{x}) = P_+f(\mathbf{x})\,e^{i\omega t} + P_-f(\mathbf{x})\,e^{-i\omega t},
$$

where the $P_\pm$ are the two projectors of the shifted-operator theory — $P_\pm = (2\gamma)^{-1}M(\gamma\pm\alpha)$, right multiplication by the complementary idempotents, with the parameter split as in the algebra lemma of *Biquaternion Regular Functions* — and $f$ is a solution of the shifted amplitude equation $D_\alpha f = 0$. The pair of signs of the frequency and the pair of projectors are the same pairing: each half of the field is a projected shifted equation.

**The reading the source attaches to it.** The source states that its projectors are *closely related to particle helicity*, and on that reading the two projected halves of the harmonic field are the two helicity components, the component $P_+F$ being the **neutrino** and $P_-F$ the **antineutrino**. In the massless case the equation they come from is

$$
i\partial_tF + DF = 0,
$$

which for a field equal to its own conjugate is a known reformulation of the vacuum Maxwell equations, attributed by the source to Imaeda [1976]. The algebra thus supplies, in one object, the two helicities as the two minimal left ideals of the shifted pair — which is the framework's own statement (*The Biquaternion Vacuum as a Minimal Idempotent*) that a helicity state is a rank-one projector of the algebra, here with the parameter's direction in place of the vacuum's.

**Which pair, and which splitting.** The projectors $P_\pm$ are **not** the chirality projectors of the following subsection. The chirality pair is built from the volume element, $\tfrac12(1\pm\gamma_5)$, and it is Hermitian and orthogonal; the pair $P_\pm$ is built from the shift parameter and acts by right multiplication, so its elements are non-Hermitian and, as the algebra requires, not orthogonal. Helicity and chirality coincide only for a massless field; at $m\neq0$ the two pairs are genuinely different splittings of the same space, and the neutrino or antineutrino identification is a statement about the helicity pair and not about $\gamma_5$. The corpus records the identification as the source's reading rather than as a derivation: what the algebra contributes to it is the shape — two complementary null idempotents, one for each sign of the frequency — and the name *neutrino* is the source's, not the algebra's.

### The Integral Representation of the Harmonic Spinor Field

Removing the conjugation is what buys the analytic theory back, and for the harmonic spinor field the source's announcement states what is bought. The time-harmonic amplitude obeys the first-order equation

$$
D_\omega\psi := i\omega\,\gamma_0\psi + \sum_{k=1}^{3}\gamma_k\,\partial_k\psi = 0 ,
$$

whose dictionary image lies in the kernel of the shifted operator $D_\alpha$ at the pure parameter $\alpha = -i\omega\,e_1$. The source derives its spinor results in this massless case — the case it calls the neutrino — while the massive parameter $\alpha = -(i\omega e_1 + m e_2)$ is the one carried by the boundary-value treatment of the bag in *Confinement and the Loss of Partonic Information in Biquaternionic Form*. The Cauchy-type operator of the algebra transfers to the spinor equation by conjugation with the dictionary,

$$
K_\omega := A^{-1} K A ,
$$

and with that one remark the three theorems of the hyperholomorphic theory hold for the harmonic spinor field in the same shape as for the electromagnetic field of the companion *The Time-Harmonic Maxwell Operator and the Quaternionic Cauchy Integral*: a **Cauchy integral formula**, $\psi = K_\omega\psi$ in $\Omega$ for a field of $\ker D_\omega$ continuous up to the boundary; the **Plemelj–Sokhotski formulas**, which express the one-sided boundary limits of $K_\omega\psi$ for Hölder data through the principal-value integral; and a **boundary-value criterion**, that a Hölder function on $\Gamma$ is the boundary value of a solution of the amplitude equation in $\Omega$ if and only if $\psi = K_\omega\psi$ on $\Gamma$. This is the refund of the price recorded in *An Explicit Dictionary with Conjugation in the Mass Term*: the conjugation obstructs the Cauchy kernel on the dictionary image, and conjugating the spinor equation back to the algebra by $A$ hands the kernel over. It is also the whole content of the second half of the source's title, and it is the spinor half of the source's thesis — the same parametric equation, at one value of its parameter, is the time-harmonic Maxwell system and, at another, the time-harmonic Dirac system, so that one Cauchy theory serves both. The spinor case is an instance of the general boundary-value criterion $P_\alpha f = f$ of *Biquaternion Regular Functions*; what the physics register adds to the general statement is the identification of the parameter and the fields.

### Chirality and the Gamma-Five Operator

The volume element $\omega = \gamma^0\gamma^1\gamma^2\gamma^3$ of the Clifford algebra is minus the image of the biquaternion scalar imaginary, $\Phi(i) = -\omega$, and satisfies $\omega^2 = -1$. The chirality operator is

$$
\gamma_5 = i\,\omega = i\,\gamma^0\gamma^1\gamma^2\gamma^3, \qquad \gamma_5^2 = i^2 \omega^2 = (-1)(-1) = 1 .
$$

It anticommutes with every generator, $\gamma_5\gamma^\mu = -\gamma^\mu\gamma_5$, and therefore commutes with every even element, the biquaternion algebra among them. In the block representation of the preceding subsection it is diagonal,

$$
\gamma_5 = \begin{pmatrix} -I_2 & 0 \\ 0 & I_2 \end{pmatrix},
$$

acting as $-1$ on the upper two-component block and $+1$ on the lower. Since $\gamma_5^2 = 1$, the Dirac spinor space splits into its eigenspaces,

$$
\mathbb{C}^4 = \Delta_+\oplus\Delta_-, \qquad \Delta_\pm = \{\psi : \gamma_5\psi = \pm\psi\}, \qquad \tilde\Pi_{L,R} = \tfrac12(1\pm\gamma_5),
$$

each of complex dimension two; the elements of $\Delta_\pm$ are the Weyl spinors of the preceding section, left- and right-handed up to the labelling convention for the sign. Correspondingly the central idempotents $\tfrac12(1\pm i\omega)$ split the complexified even algebra, $\mathbb{C}\otimes_{\mathbb{R}}\mathrm{Cl}_{1,3}^+ \cong M_2(\mathbb{C})\oplus M_2(\mathbb{C})$, which is the algebraic form of the same decomposition. The $i$ in $\gamma_5$ and in the projectors is the scalar imaginary of the complexified Clifford algebra; the biquaternion imaginary is the element whose image under $\Phi$ is $\omega$ itself.

## Relativistic Kinematics in Biquaternionic Form

Before developing the biquaternionic Dirac equation, it is useful to collect the basic relativistic kinematic quantities in biquaternion form. These are the objects that appear in the Dirac equation and its solutions, and they are established physics rewritten in biquaternion notation.

### The Four-Position

The **four-position biquaternion** is

$$
\tilde{Q} = ic t\, e_0 + x\, e_1 + y\, e_2 + z\, e_3,
$$

with $x_0 = ict$. The scalar part is the complex time coordinate, and the vector part is the ordinary spatial position.

### The Invariant Interval

The invariant interval is the square of the biquaternion displacement:

$$
ds^2 = N(d\tilde{Q}) = d\tilde{Q} \circ \overline{d\tilde{Q}} = (ic\,dt)^2 + dx^2 + dy^2 + dz^2 = -c^2 dt^2 + d\mathbf{x}^2.
$$

This is the biquaternion form of the Minkowski interval. The Lorentzian signature emerges algebraically from $i^2 = -1$, as discussed in the companion article on the $ict$ convention.

### The Four-Velocity

The **four-velocity biquaternion** is

$$
\tilde{U} = \gamma(ic\, e_0 + \mathbf{v}),
$$

where $\mathbf{v}$ is the ordinary three-velocity of the particle and

$$
\gamma = \frac{1}{\sqrt{1 - \mathbf{v}^2/c^2}}
$$

is the Lorentz factor. The four-velocity satisfies the **normalization condition**

$$
\tilde{U}\tilde{U}^{\natural} = \gamma^2\big(-c^2 + \mathbf{v}^2\big) = -c^2.
$$

This is the biquaternion form of the standard relativistic normalization $u^\mu u_\mu = -c^2$.

### The Four-Momentum

The **four-momentum biquaternion** is

$$
\tilde{P} = m\tilde{U} = \gamma m(ic\, e_0 + \mathbf{v}) = i\,\frac{E}{c}\, e_0 + \mathbf{p},
$$

where $E = \gamma m c^2$ is the relativistic energy and $\mathbf{p} = \gamma m\mathbf{v}$ is the relativistic three-momentum. The scalar part of $\tilde{P}$ is $iE/c$, and the vector part is $\mathbf{p}$.

The four-momentum satisfies the **mass-shell relation**

$$
\tilde{P}\tilde{P}^{\natural} = m^2 \tilde{U}\tilde{U}^{\natural} = -m^2 c^2.
$$

This is the biquaternion form of the standard relativistic energy-momentum relation

$$
E^2 = \mathbf{p}^2 c^2 + m^2 c^4,
$$

which is obtained by expanding $-m^2 c^2 = -(E/c)^2 + \mathbf{p}^2$.

### The Four-Acceleration and Four-Force

The **four-acceleration biquaternion** is $\tilde{A} = d\tilde{U}/d\tau$, where $\tau$ is the proper time. The **four-force biquaternion** is $\tilde{F} = d\tilde{P}/d\tau = m\tilde{A}$. The four-acceleration satisfies $\tilde{A}\tilde{U}^{\natural} + \tilde{U}\tilde{A}^{\natural} = 0$, which is the biquaternion form of the orthogonality condition $a^\mu u_\mu = 0$.

### Summary of Relativistic Kinematics

| Quantity | Biquaternion | Constraint |
|---|---|---|
| Four-position | $\tilde{Q} = ict\, e_0 + \mathbf{x}$ | — |
| Interval | $ds^2 = N(d\tilde{Q}) = d\tilde{Q}\circ\overline{d\tilde{Q}}$ | $= -c^2 dt^2 + d\mathbf{x}^2$ |
| Four-velocity | $\tilde{U} = \gamma(ic\, e_0 + \mathbf{v})$ | $\tilde{U}\tilde{U}^{\natural} = -c^2$ |
| Four-momentum | $\tilde{P} = m\tilde{U}$ | $\tilde{P}\tilde{P}^{\natural} = -m^2 c^2$ |
| Four-force | $\tilde{F} = d\tilde{P}/d\tau$ | — |

These kinematic relations are the biquaternion form of standard relativistic mechanics, and they are the natural setting for the biquaternionic Dirac equation.

## The Biquaternionic Dirac Equation

### Statement

Let $\tilde{\Psi}$ be a biquaternion-valued field, and let $\tilde{\nabla}$ be the biquaternionic gradient. The **biquaternionic Dirac equation** for a massless field is

$$
\tilde{\nabla}\tilde{\Psi} = 0.
$$

For a field of mass $m$ the equation is **linear** in $\tilde{\Psi}$ and **off-diagonal in chirality**. Writing the field as a pair of chiral components, $\tilde{\Psi} = \tilde{\Psi}_L + \tilde{\Psi}_R$, the massive equation is the pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R .
$$
<!-- CONVENTION — the massive equation, canonical form. This linear, chirality-off-diagonal pair IS the biquaternionic Dirac equation for m ≠ 0; the derived articles state it in this orientation (∇̃ acting on Ψ_R, ∇̃^♮ on Ψ_L), and this article is its definitional home. Two standing facts. (i) The mass term is LINEAR: the continuous central phase (fermion number) passes through it, so the vector U(1) is exact for the massive field, and what the mass breaks is the AXIAL symmetry, ∂_μ j_5^μ = 2im Ψ̄γ_5Ψ. (ii) It is NOT the antilinear single-field equation ∇̃Ψ = mΨ♭: that belongs to the algebra's real structure ♭ and is a different equation (see the remark on ♭ in The Massive Case). Do not restore mΨ♭ as the mass term. -->

Applying $\tilde{\nabla}^{\natural}$ to the first equation and using the second, together with $\tilde{\nabla}^{\natural}\tilde{\nabla} = \Box$, gives $\Box\tilde{\Psi}_R = m^2\tilde{\Psi}_R$, and likewise for $\tilde{\Psi}_L$; the pair therefore implies the Klein–Gordon equation for each chirality. On the spinor module the same statement is the matrix equation $(\not\partial - m)\psi = 0$ of the first section, with $\psi = (\psi_L, \psi_R)$ the pair of Weyl spinors.

A **single-string form** of the same pair is recorded in *The Chiral Algebra of Biquaternions and the Cyclic Representation of the Dirac Equation*. Writing the wave function in the light-cone coordinates and using that article's outer and inner products, the chiral pair becomes one expression, $F^- \odot \bar D + D \otimes F^+ = im\overset{⤺}{F}$, in which the two products carry the two chiralities and the cyclic conjugation $\overset{⤺}{\phantom{x}}$ carries the mass term. The equivalence of that expression with the Weyl system is verified row by row there. The pair above remains the definitional home of the biquaternionic Dirac equation; the single-string form is a repackaging in a different product, not a different equation.

The mass term is the term that breaks the exact correspondence between the biquaternionic Dirac equation and the biquaternionic Maxwell equation. It is linear in the field, the biquaternion transcription of the mass term $m\psi$ of the matrix Dirac equation.

### The Massless Case

The massless biquaternionic Dirac equation $\tilde{\nabla}\tilde{\Psi} = 0$ is identical in form to the **homogeneous biquaternion Maxwell equation** for the field-strength biquaternion $\tilde{F}$. The two equations have the same form:

$$
\tilde{\nabla}\tilde{\Psi} = 0 \quad \text{(massless Dirac)}, \qquad \tilde{\nabla}\tilde{F} = 0 \quad \text{(source-free Maxwell)}.
$$

The solutions are also the same in form: the kernel of the biquaternionic gradient consists of plane waves, spherical waves, and cylindrical waves (as in the companion article on Maxwell). The physical interpretation differs: $\tilde{\Psi}$ is a fermion field (spin-$\frac{1}{2}$), and $\tilde{F}$ is a boson field (spin-1).

The structural identity of the two equations is the algebraic content of the statement that the biquaternion algebra is the same for both. The difference is not in the operator but in the representation: the Maxwell field-strength biquaternion lives in the vector part of the algebra, and the Dirac biquaternion lives in the full algebra (with the two-component structure that corresponds to the pair of Weyl spinors).

### The Massive Case

The massive biquaternionic Dirac equation is the chiral pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R .
$$

The mass term is **linear** in the field and **off-diagonal** between the two chiralities: it is the biquaternion transcription of the mass term $m\psi$ of the matrix Dirac equation, and it is what couples the left- and right-handed Weyl spinors.

The coupling has to be off-diagonal. Left multiplication by an element of $\mathbb{B}$ *preserves* each chiral component — the minimal left ideals of $\mathbb{B} \cong M_2(\mathbb{C})$ are the two chiralities, and left multiplication maps each into itself — so no combination of the form $a\tilde{\Psi}_L + b\tilde{\Psi}_R$ relates them. A mass term that couples the chiralities therefore has to act as a *right* multiplication, which is what the pair above does; equivalently, on the strict spinor module (a single minimal left ideal) the mass is simply linear. This is the structural reason why the spinor module, and not the whole algebra, is the natural carrier of the Dirac field.

**A remark on the anti-Hermitian conjugation $\flat$.** The algebra carries, besides the quaternion conjugate and the Hermitian conjugation ${}^{*}$, a further antilinear involution:

$$
\tilde{\Psi}^\flat = -\tilde{\Psi}^{*} = -\overline{\tilde{\Psi}^{\natural}},
$$

the **anti-Hermitian conjugate** $\flat = -{}^{*}$. It is a $\mathbb{C}$-**antilinear** involution, and it is order-reversing with a twist,

$$
\left(\tilde{A}\tilde{B}\right)^\flat = -\,\tilde{B}^\flat\tilde{A}^\flat ,
$$

the sign being the only difference from an ordinary anti-automorphism, and it acts by a sign on the two Hermitian sectors,

$$
\tilde{\Psi}^\flat = +\tilde{\Psi}\ \ (\tilde{\Psi}\in\mathbb{M}_-), \qquad \tilde{\Psi}^\flat = -\tilde{\Psi}\ \ (\tilde{\Psi}\in\mathbb{M}_+),
$$

so that the **fixed space of $\flat$ is the anti-Hermitian sector $\mathbb{M}_-$**.

The convention is worth a remark, because the more familiar one takes the *Hermitian* part as the real one, and here the *anti*-Hermitian part plays that role. The two differ only by the central factor $i$: anti-Hermitian elements are $i$ times Hermitian ones, and anti-Hermitian generators are the standard choice for the Lie algebra of a unitary group (in the companion quantum article the Lie algebra of the unitary group is $\mathbb{M}_-$). What is unusual here is not the sign convention as such, but that it is applied to the *field* rather than to the generators: it is $\mathbb{M}_-$ that is fixed, and that is what makes $\mathbb{M}_-$ the framework's "material" sector (the companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* takes $\mathbb{M}_-$ as the fixed space of $\flat$).

The map $\flat$ is the algebra's **real structure**, and its shape is that of a charge-conjugation (Majorana) pairing: it relates the field to its own conjugate. It is *not* the mass term. A coupling built on $\flat$ pairs $\tilde{\Psi}$ with $\tilde{\Psi}^\flat$ rather than relating two independent chiralities, and because $\flat$ is antilinear such a coupling is not invariant under the continuous central phase — precisely the two differences between a Majorana-type pairing and an ordinary Dirac mass. The single-field equation $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat$ is a real-linear equation of that type; it is a different equation from the one studied here, and its central-phase plane waves sit on the *spacelike* locus, not on the physical mass shell. The map $\flat$ is retained in the framework for what it is genuinely for — conjugation, the $\mathbb{M}_\pm$ split, the trace and bilinear pairings, and the real-form question of Dirac versus Majorana fermions, which the companion articles on chirality, the neutrino, and the CPT theorem develop. In the present article $\flat$ is used only for conjugation, never as the mass.
<!-- CONVENTION — verified, do not "fix". The claim that the antilinear companion ∇̃Ψ = mΨ♭ has its central-phase plane waves on the SPACELIKE locus is deliberate and was re-derived independently (pure real arithmetic, no libraries): the two-frequency system for a single-mode field has nullity 0 on the timelike shell k₀² = k² + m² and nullity 4 on the spacelike shell k² = k₀² + m². So the spacelike dispersion is a property of that equation, not a typo, and it is exactly why that equation is not the Dirac equation and was retired as the mass term. Do not relocate it to the physical mass shell. -->

**The associated Klein–Gordon equation.** Applying $\tilde{\nabla}^{\natural}$ to the first of the pair and substituting the second gives

$$
\tilde{\nabla}^{\natural}\tilde{\nabla}\tilde{\Psi}_R = \Box\tilde{\Psi}_R = m\,\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m^2\tilde{\Psi}_R ,
$$

and likewise for $\tilde{\Psi}_L$, so each chiral component satisfies the **Klein–Gordon equation**

$$
\left(\Box - m^2c^2/\hbar^2\right)\tilde{\Psi} = 0 ,
$$

in agreement with the companion article on the Klein–Gordon equation, whose operator is $\Box - m^2c^2/\hbar^2$. This is the biquaternion form of the standard statement that the square of the Dirac operator is the Klein–Gordon operator, $(\not\partial + m)(\not\partial - m) = \Box - m^2$.

## Plane-Wave Solutions

### The Massless Case

Plane-wave solutions of the massless biquaternionic Dirac equation are

$$
\tilde{\Psi}(\tilde{Q}) = \tilde{\Psi}_0 \exp\!\left(i\,\mathrm{Sc}\!\left(\tilde{k}\tilde{Q}^{\natural}\right)\right)
= \tilde{\Psi}_0\,e^{\,i(\mathbf{k}\cdot\mathbf{x}-\omega t)},
$$

where $\tilde{\Psi}_0 \in \mathbb{B}$ is a constant biquaternion, $\tilde{k} = i k_0 e_0 + e_1 k_1 + e_2 k_2 + e_3 k_3$ (with $k_0 = \omega/c$) is the wave biquaternion, and $\tilde{Q} = e_0 (ict) + e_1 x + e_2 y + e_3 z$ is the four-position biquaternion. The scalar part $\mathrm{Sc}(\tilde{k}\tilde{Q}^{\natural}) = \mathbf{k}\cdot\mathbf{x} - \omega t$ is real, so the exponent $i\,\mathrm{Sc}(\tilde{k}\tilde{Q}^{\natural})$ is a purely imaginary central element; the exponential therefore commutes with $\tilde{\Psi}_0$ and differentiates to left multiplication by $i\tilde{k}$,

$$
\tilde{\nabla}\tilde{\Psi} = i\,\tilde{k}\,\tilde{\Psi},
$$

so the equation $\tilde{\nabla}\tilde{\Psi} = 0$ becomes

$$
\tilde{k}\tilde{\Psi}_0 = 0,
$$

i.e., the polarization biquaternion $\tilde{\Psi}_0$ is annihilated by the wave biquaternion $\tilde{k}$. This is the biquaternion form of the **Weyl equation** $\not k\psi_0 = 0$.

Nonzero solutions of $\tilde{k}\tilde{\Psi}_0 = 0$ exist only when $\tilde{k}$ is a zero divisor in $\mathbb{B}$, that is, when $\tilde{k}$ is null: $\tilde{k}\tilde{k}^{\natural} = 0$, equivalently $k_0^2 = \|\mathbf{k}\|^2$, the massless dispersion relation. In that case the kernel is a two-dimensional complex vector space, corresponding to the two spin states of a massless fermion; for non-null $\tilde{k}$ the kernel is trivial. This matches the two-component structure of the Weyl spinor.

### The Massive Case

For the massive equation a single central-phase plane wave,

$$
\tilde{\Psi}(\tilde{Q}) = \tilde{\Psi}_0 \exp\!\left(i\,\mathrm{Sc}\!\left(\tilde{k}\tilde{Q}^{\natural}\right)\right) = \tilde{\Psi}_0\,e^{i\theta}, \qquad \theta = \mathbf{k}\cdot\mathbf{x} - \omega t,
$$

does solve the pair, with one polarization biquaternion per chirality, $\tilde{\Psi}_0 = \tilde{\Psi}_0^L + \tilde{\Psi}_0^R$. Differentiating as in the massless case, $\tilde{\nabla}$ acts on $e^{i\theta}$ as left multiplication by $i\tilde{k}$ and $\tilde{\nabla}^{\natural}$ acts on it as left multiplication by $i\tilde{k}^{\natural}$, so the chiral pair becomes the momentum-space system

$$
i\tilde{k}\tilde{\Psi}_0^R = m\tilde{\Psi}_0^L, \qquad i\tilde{k}^{\natural}\tilde{\Psi}_0^L = m\tilde{\Psi}_0^R .
$$

Eliminating $\tilde{\Psi}_0^L$ gives

$$
\tilde{k}\tilde{k}^{\natural}\,\tilde{\Psi}_0^R = -m^2\,\tilde{\Psi}_0^R ,
$$

so a nonzero solution requires the **mass-shell condition**

$$
\tilde{k}\tilde{k}^{\natural} = -m^2 c^2/\hbar^2,
$$

i.e., $-k_0^2 + \|\mathbf{k}\|^2 = -m^2 c^2/\hbar^2$, which is the standard mass-shell relation $k_0^2 = \|\mathbf{k}\|^2 + m^2 c^2/\hbar^2$ (with $k_0 = E/\hbar c$). This is the biquaternion form of the standard relativistic energy-momentum relation $E^2 = \mathbf{p}^2 c^2 + m^2 c^4$ (with $\mathbf{p} = \hbar\mathbf{k}$), the same shell as the four-momentum kinematics of the preceding section. The two signs of $k_0$ are the two frequency branches — the particle and the antiparticle — and with the two spin states they give the four components of the Dirac spinor.

### Spinors as Bipotentials of a Scalar Field

The monogenic completion of the next section is the massless case of a construction the author's programme on generalised solutions uses to generate spinors, and it is the plane-wave version of the shifted operator of the companion *The Biquaternion D'Alembertian and Its Green's Functions*. With the **shifted gradient** $\tilde{\nabla}_\kappa = \tilde{\nabla} + \kappa$, a solution of the shifted scalar equation is a **potential** whose shifted conjugate gradient is a spinor:
$$
\left(\Box + 2\kappa\,\partial_{ict} + \kappa^2\right) u = 0
\quad\Longrightarrow\quad
\tilde{\nabla}_\kappa\left(\tilde{\nabla}^{\natural}_\kappa u\right) = 0 .
$$
The implication is the square of the shifted gradient, $\tilde{\nabla}_\kappa\tilde{\nabla}^{\natural}_\kappa = \Box + 2\kappa\partial_{ict} + \kappa^2$; at $\kappa = 0$ it is the completion $\psi\mapsto\tilde{\nabla}^{\natural}\psi$ of the next section, and for $\kappa \neq 0$ it is its shifted form. The source calls the scalar generator a **C-field** and takes the spinor to be the convolution of $\tilde{\nabla}^{\natural}_\kappa\psi_0$ with it, which is how the same construction produces extended rather than only elementary solutions; the convolution is the one developed in the companion article on distributions.

One property of the elementary spinor belongs to the corpus's own language. On the shifted cone the potential is a plane wave, and the spinor's biquaternion norm vanishes,
$$
N\!\left(\tilde{\nabla}^{\natural}_\kappa\, e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)}\right) = 0 ,
$$
which was checked numerically on the shifted cone: the elementary harmonic spinors are **null**, elements of the algebra's zero-divisor cone, exactly as the massless plane-wave spinors of the preceding subsection are. This is the massless statement once more — a spinor built from an on-shell potential is a zero divisor, and the zero-divisor cone is the light cone — and the shifted version says that the shifted cone is the norm-zero set of the shifted operator. The source normalises its representatives and records separate norm and pseudonorm values for them; the corpus keeps the invariant statement, that the element is null, and the dictionary between the source's mass $m$ and the corpus shift $\kappa$ — $\kappa = -im$, so that the source's imaginary $m$ is a real $\kappa$ — is the one recorded in the d'Alembertian companion.

## Spherical and Cylindrical Solutions

### Spherical Solutions

Spherical solutions of the biquaternionic Dirac equation can be constructed by the methods of Clifford analysis, adapted to the biquaternion algebra. The standard technique is the **monogenic completion** of scalar harmonic functions: given a harmonic scalar function on the sphere, the monogenic completion produces a biquaternion-valued function that lies in the kernel of the Dirac operator.

The construction is more involved than the corresponding construction for the Maxwell equation, because $\tilde{\nabla}$ is not the operator whose square is the scalar wave operator. One has

$$
\tilde{\nabla}^2 = \partial_{ict}^2 - \Delta + 2\,\partial_{ict}\boldsymbol{\nabla},
\qquad \boldsymbol{\nabla} = e_1\partial_x + e_2\partial_y + e_3\partial_z,
$$

whose first-order cross term does not vanish, so $\tilde{\nabla}^2 \neq \Box = \partial_{ict}^2 + \Delta$. It is the **conjugate** gradient that squares to the d'Alembertian, $\tilde{\nabla}\tilde{\nabla}^{\natural} = \Box$, so the completion operator is $\tilde{\nabla}^{\natural}$: for every harmonic scalar function $\psi$ with $\Box\psi = 0$, the function $\tilde{\nabla}^{\natural}\psi$ satisfies

$$
\tilde{\nabla}\left(\tilde{\nabla}^{\natural}\psi\right) = \Box\psi = 0
$$

and is a solution of the massless Dirac equation. This is the biquaternion form of the monogenic completion of the scalar harmonic functions, and it is the reason the spherical solutions are indexed by the scalar spherical harmonics.

For the massless case, the spherical solutions of the biquaternionic Dirac equation are the **monogenic spherical harmonics**, and they form a basis of the solution space. For the massive case, the construction is more involved: the solution is a combination of the monogenic spherical harmonics and their anti-Hermitian conjugates, with coefficients determined by the mass-shell condition.

The spherical solutions describe the **angular momentum states** of a relativistic fermion. The quantum numbers $(n, \ell, m)$ correspond to the radial, orbital, and magnetic quantum numbers of the standard hydrogen-like Dirac equation.

### Cylindrical Solutions

Cylindrical solutions are similarly constructed from cylindrical harmonics by the same monogenic completion technique. They describe **waveguide modes** of a fermion field in a cylindrical geometry, with the transverse-electric and transverse-magnetic modes corresponding to the two spin states.

## Relation to the Maxwell Equation

### Structural Identity

The massless biquaternionic Dirac equation and the homogeneous biquaternion Maxwell equation have the same form:

$$
\tilde{\nabla}\tilde{\Psi} = 0.
$$

The difference is the interpretation of the field $\tilde{\Psi}$:

- In the Maxwell case, $\tilde{\Psi}$ is the field-strength biquaternion $\tilde{F}$, which lives in the vector part of the algebra and describes the electromagnetic field.
- In the Dirac case, $\tilde{\Psi}$ is the fermion field, which lives in the full algebra and describes the spin-$\frac{1}{2}$ particle.

The structural identity is the algebraic content of the statement that both the photon and the electron are described by the same Clifford algebra $\mathrm{Cl}_{1,3}$. The two fields differ in the **representation** of the algebra: the photon field lives in the vector representation (spin-1), and the electron field lives in the spinor representation (spin-$\frac{1}{2}$).

### The Mass Term

The **mass term** is the term that distinguishes the massive Dirac equation from the massless case, and it does not appear in the Maxwell equation. In the biquaternion formulation it is the linear, chirality-off-diagonal coupling of the pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$ of the section *The Massive Case*; on the spinor module it is the term $m\psi$ of the matrix Dirac equation, which couples the left- and right-handed Weyl spinors. In the Standard Model the mass term arises from the **Higgs mechanism**: the fermion couples to the Higgs field, and the coupling generates an effective mass term.

The biquaternion framework does not derive the Higgs mechanism; it simply provides a compact notation for the mass term once the mechanism is assumed. The conjugation $\flat$ is a separate object — the algebra's real structure, discussed in the section *The Massive Case* — and is not the mass term.

### The Static Maxwell Field of an Inhomogeneous Medium as a Dirac Potential

The dictionary gives one more reading of the massive equation, in which its potential *is* a Maxwell medium. The static sourceless Maxwell system of an isotropic inhomogeneous medium,

$$
\mathrm{rot}\,\mathbf{H} = 0, \qquad \mathrm{rot}\,\mathbf{E} = 0, \qquad \mathrm{div}(\epsilon\mathbf{E}) = 0, \qquad \mathrm{div}(\mu\mathbf{H}) = 0 ,
$$

carries its position dependence only through the two divergence equations, and on the normalised fields $\tilde{\mathbf{E}} := \sqrt{\epsilon}\,\mathbf{E}$, $\tilde{\mathbf{H}} := \sqrt{\mu}\,\mathbf{H}$ it becomes the pair of first-order equations with constant-free leading part,

$$
\bigl[D + M_{\vec{\nu}}\bigr]\tilde{\mathbf{E}} = 0, \qquad \bigl[D + M_{\vec{\nu}'}\bigr]\tilde{\mathbf{H}} = 0,
\qquad
\vec{\nu} := \frac{\mathrm{grad}\sqrt{\epsilon}}{\sqrt{\epsilon}}, \quad \vec{\nu}' := \frac{\mathrm{grad}\sqrt{\mu}}{\sqrt{\mu}} ,
$$

which is the **carrier identity** of *Electromagnetism in Media — The Local Complex Structure at Work*, read in the static case, where no time coordinate is present and the operator is the Moisil–Theodorescu operator $D$ alone. The Dirac side has the same shape: the massive equation with an electric potential, and separately with a scalar potential, becomes after the dictionary a first-order equation whose only position dependence is a coefficient multiplying one basis direction, as recorded in *The Dirac Operator with Potentials in Quaternionic Form* above. Matching the two shapes, the 2003 paper concludes that a solution of the Dirac equation with an electric or a scalar potential is a solution of the static Maxwell system of an isotropic inhomogeneous medium, the medium being the potential read as a parameter:

$$
\epsilon = e^{\,2G(x_1)}, \qquad G(x_1) = \int g(x_1)\,dx_1 ,
$$

with $g$ the Dirac potential. The identification is a statement about **coefficients** and not about fields: the potential is the logarithmic derivative of the square root of the permittivity, $\vec{\nu} = \mathrm{grad}\,G$, which is checked at once from $\sqrt{\epsilon} = e^{G}$. What the correspondence does not do is identify the Dirac field with the electromagnetic field — the Dirac biquaternion and the field-strength biquaternion are different objects, and the matching is at the level of the equations they solve, with the restriction $\mathrm{Sc} = 0$ on the Maxwell side. The corpus records it because both ends already exist here, the carrier function of the media article and the potential coupling of the Dirac article, and this is the statement that joins them.

**What is quoted.** The source's own forms of the two reduced operators, for the electric and for the scalar potential, are partly illegible in the scan. What is legible, and what is recorded above, is the shape of the reduction, the normalisation by $\sqrt{\epsilon}$, and the parameter $\epsilon = e^{2G}$ with $\vec\nu = \mathrm{grad}\,G$; the identification of the potential with an inhomogeneity of that form is the source's statement, carried here as such.

### The Mass Shell as the Condition on the Dirac–Maxwell Correspondence

The time-harmonic comparison is the paper's last section, and its conclusion is a condition rather than an identity. Let the massive quaternionic equation be read on a time-harmonic field, as in the harmonic-spinor subsection above: the amplitude obeys the shifted equation $D_\alpha f = 0$ at the parameter $\alpha = i\omega i_1 + mi_2$, and the massless case of the same equation is the vacuum Maxwell equation. The time-harmonic Maxwell field of a homogeneous isotropic medium is likewise a pair of Beltrami fields, and the projection identity that relates the two pairs,

$$
\bigl(D + M_\alpha\bigr) = P^{+}\bigl(D + M_k\bigr) + P^{-}\bigl(D - M_k\bigr),
\qquad
P^{\pm} := \tfrac12 M_{(1 \pm \alpha/k)} ,
$$

holds in both directions **if and only if** the Maxwell wave number and the Dirac parameter agree,

$$
k^2 = \alpha^2, \qquad k := \omega\sqrt{\epsilon\mu} .
$$

The parameter is the one the corpus already carries, and its square is computed at once: $\alpha^2 = (i\omega i_1 + mi_2)^2 = \omega^2 - m^2$, a central scalar. The condition is therefore

$$
k^2 = \omega^2 - m^2, \qquad \text{equivalently} \qquad \omega^2 = k^2 + m^2 ,
$$

which is the **mass shell** in the corpus's natural units and, with $\hbar$ and $c$ restored and the Planck and de Broglie relations used, the relativistic dispersion relation $E^2 = p^2c^2 + m^2c^4$. The paper draws attention to the agreement — the condition on which its Dirac–Maxwell equivalence rests is the same relation that defines the particle's mass — and the corpus records it as what ties the parametric statements together: the parameter that makes the shifted equation solvable is the parameter that puts the field on shell. The same reading is why the massless (neutrino) case of the harmonic-spinor subsection needs no condition at all: at $m = 0$ the parameter is $\alpha = i\omega i_1$ with $\alpha^2 = \omega^2$, and $k^2 = \alpha^2$ becomes the vacuum null-wave relation $\omega = k$ — the case the source calls the neutrino, and the one the corpus records as Imaeda's vacuum Maxwell equation.

**What is quoted.** The source's intermediate equations, which restore $c$ and $\hbar$ at a different point of the reduction, are quoted as its own; the printed power of $c$ in them could not be read from the scan. The two statements used above — the condition $k^2 = \alpha^2$ and the value $\alpha^2 = \omega^2 - m^2$ — are legible, and the mass-shell reading follows from them.

### The Lanczos Route: Maxwell with Feedback

The identity of form is not an artifact of the notation, and Lanczos read it as a statement about matter. In his 1929 articles he derived Dirac's equation from the coupled biquaternion system

$$
\tilde{\nabla}\tilde{A} = m\tilde{B}, \qquad \tilde{\nabla}\tilde{B} = m\tilde{A},
$$

comparing it with the biquaternion Maxwell equation $\tilde{\nabla}\tilde{F} = -4\pi\tilde{J}$ of the companion article. The first equation is then Maxwell's equation, and the second is a **feedback**: the field $\tilde{B}$ acts back on the object that generates it, with the strength $m$. The feedback is the mass; the massless case $m=0$ breaks the coupling and leaves two independent field equations, of which the Maxwell equation is one. This is the source's reading, and it answers the question at the end of this article: what the Dirac and Maxwell equations share is the **operator** — the single first-order operator $\tilde{\nabla}$, a square root of $\Box$ — and what separates them is the **closure**, the Dirac field obeying the operator in the closed, self-acting way and the Maxwell field in the sourced way.

The corpus's chiral pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$ is the same equation written in the other useful way: it displays the spinor split — the two minimal left ideals — but not the direction that the Lanczos form makes explicit. Lanczos reached the Dirac equation from the pair by the idempotent superposition

$$
D = \tilde{A}\sigma + \tilde{B}^{*}\bar{\sigma},
$$

with $\sigma$ the idempotent along a unit vector $\vec{\nu}$ and $\bar{\sigma}$ its conjugate, the two projecting onto the two minimal left ideals — so that one half of $\tilde{A}$ and half of the conjugate of $\tilde{B}$ land in **different** ideals, which is what makes the superposition a **bispinor** and not a one-sided spinor; the resulting single equation

$$
\tilde{\nabla}D = m\,D^{*}\,i\vec{\nu}
$$

is strictly equivalent to Dirac's equation. The unit vector on the right is the point of the display: it is the **spin quantization axis**, and it shows that Dirac's equation singles out an arbitrary but unique direction in ordinary space. The corpus's pair is written for a fixed frame and does not exhibit the axis; the Lanczos form shows that the axis is carried by the idempotent that performs the projection, and that any unit vector will do. The complex conjugation on the right-hand side is a second such fact: it is what makes the Dirac field **fermionic**, in contrast with the Maxwell and Proca fields, which are bosonic. The superposition is not unique: the source's second and equally covariant combination — Gürsey's, which the isospin reading makes the neutron to the proton above — is recorded in *The Standard Model under the Biquaternion Framework — A Research Agenda*; the fermionic character above is what the two share.

**The other road to the same halving.** The idempotent superposition is not the only way the doubled system becomes Dirac's, and the source records a second one. "One can go from (1) to (3) by simply requiring that $A$ and $B$ are singular quaternions" — an observation the authors attribute to Blaton (1935), where (3) is the two-component pair $\partial L = mR$, $\partial R = mL$. The two routes reach the same place by different means: the superposition projects each field onto one of the two minimal left ideals and adds the halves *across* the ideals, whereas the singularity condition degenerates the fields themselves. The destination, however, is the corpus's own object — a singular biquaternion is a zero divisor — so this reading of the reduction says that the Dirac field is what the doubled Lanczos system becomes when both of its fields are confined to the singular set. The source is careful about what the halving alone does not buy: Dirac's system "does not only involve half as many components as Lanczos's system (1), it also incorporates the ingredients that make fermions essentially different from bosons", which are the complex conjugation and the singled-out direction recorded just above. That distinction is why the corpus keeps *Biquaternion Zero Divisors* and this article apart: the halving is a fact about the algebra, while the fermionic character is a fact about the superposition.

## The Dirac Operator with Potentials in Quaternionic Form

Every equation of this article so far is free. The standard Dirac potentials — the **electric** (the time component of a four-vector), the **magnetic** (its spatial part), the **scalar**, and the **pseudoscalar** — are usually attached one at a time in the gamma-matrix formalism, each changing the operator differently. Kravchenko's monograph attaches all four in one place, and the result is a statement about the algebra rather than about the potentials. The free quaternionic operator and the free classical Dirac operator are related by **one constant linear transformation** — a change of basis; the monograph's Lemma 3 — and the *same* transformation, together with one permutation of the gamma indices, carries each of the four potentials into the corresponding quaternionic operator. The four potentials therefore do not enlarge the formalism. Each is an explicit coefficient function multiplying one of the algebra's basis directions, and the quaternionic Dirac equation with any one of them is the same first-order equation with a different coefficient.

The four directions are the four the algebra distinguishes. The scalar potential multiplies the identity $e_0$; the pseudoscalar potential multiplies the scalar imaginary $i$, which is the algebra's image of $\gamma^0\gamma^1\gamma^2\gamma^3$ under the dictionary above; the electric potential multiplies the timelike direction; and the magnetic potential enters through the spatial vector $\sum_k A_k e_k$. This is the same fourfold list that Gürsey reads as the degenerate cases of the Lanczos system, and here it is the list of the algebra's carrier directions for a *coupling* rather than for a field.

**The pseudoscalar potential.** Of the four, the pseudoscalar case is the one that reaches machinery the corpus already has. It is the coupling of the field to $i$ — the $\gamma^5$-type, chirality-sensitive coupling, not the minimal coupling of the companion article, which uses the four-vector direction. For a time-harmonic field the pseudoscalar-potential equation reduces to

$$
\bigl(D + \varphi(\mathbf{x})I + M\bigr)f(\mathbf{x}) = 0,
$$

where $\varphi$ is the potential, $I$ the identity of the algebra, and $M$ the constant frequency–mass shift; the only position dependence in the whole operator is the scalar coefficient $\varphi(\mathbf{x})$. That is exactly the corpus's shifted operator $D_\alpha = D + M_\alpha$ of *Biquaternion Regular Functions*, with the parameter no longer a constant but a function of position. The pseudoscalar-potential Dirac equation is therefore a shifted-operator equation, and the shift is the potential.

**The splitting.** The reduction is the monograph's Theorem 15. Let the constant biquaternion $\omega$ carry the frequency and the mass, so that $\omega^2 = \beta^2$, and suppose $\omega^2$ is not a zero divisor. Then the pseudoscalar equation is equivalent to a **pair** of scalar-coefficient equations,

$$
\bigl(D + (\varphi(\mathbf{x}) + \beta)I\bigr)f_+ = 0,
\qquad
\bigl(D + (\varphi(\mathbf{x}) - \beta)I\bigr)f_- = 0,
$$

the two components $f_\pm$ being the projections of $f$ by the idempotents $P_\pm$ that the shifted-operator theory supplies. Each of the two is an equation of the form $(D + \alpha(\mathbf{x}))u = 0$ with a **scalar** coefficient. That equation is the subject of the monograph's §4.1.5, and the corpus already carries its solution: the **zero-divisor device** recorded in *Maxwell's Equations in Chiral Media*, in which a solution of the eikonal equation $(\nabla\chi)^2 = \alpha^2$ conjugates $D + \alpha$ into $D + Q_+$ with $Q_+ = \nabla\chi$ a zero divisor, and the solutions are built from the exponentials $e^{\pm i\Theta}$ of the accumulated phase and analytic transverse functions. The chain therefore closes inside the corpus: pseudoscalar-potential Dirac equation $\to$ shifted operator with a scalar coefficient $\to$ eikonal conjugation by a zero divisor $\to$ explicit solutions. The exceptional case, $\omega^2$ a zero divisor (an isotropic $\omega$), is separate; the monograph handles it with a one-variable ansatz, because the idempotents $P_\pm$ degenerate there.

**What this does and does not add.** It adds the observation that the chirality-sensitive Dirac coupling is not new machinery: it is the shifted operator the corpus already possesses, read at a position-dependent parameter, and the corpus's zero-divisor device solves it. It does not supply solutions for the electric potential — the monograph reaches that case by the same conjugation, but the corpus treats electromagnetic coupling separately in *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* — and it claims no new physics: the coupling list is standard, and it is surveyed in the encyclopaedic compendium the monograph cites for the classification of exact Dirac solutions up to the late 1980s, now recorded in the Further Reading below.

## The Dirac Equation and the Biquaternion Algebra

### Why Biquaternions?

The Dirac equation is naturally expressed in terms of the Clifford algebra $\mathrm{Cl}_{1,3}$, which is the algebra generated by the gamma matrices. The biquaternion algebra $\mathbb{B}$ is isomorphic to the even subalgebra of $\mathrm{Cl}_{1,3}$, so the Dirac equation can be expressed in terms of $\mathbb{B}$ directly.

The advantage of the biquaternion formulation is that it is **more compact** than the matrix formulation: the biquaternion algebra has 8 real dimensions (or 4 complex dimensions), while the Clifford algebra $\mathrm{Cl}_{1,3}$ has 16 real dimensions. The biquaternion algebra is the minimal algebraic structure that contains the even part of the Clifford algebra, and it is sufficient for describing the spinor fields.

The disadvantage is that the biquaternion algebra $\mathbb{B} \cong M_2(\mathbb{C})$ acts naturally on a two-dimensional complex module, while the Clifford algebra $\mathrm{Cl}_{1,3} \cong M_4(\mathbb{C})$ acts on a four-dimensional complex module. The biquaternion formulation therefore requires an additional step to recover the four-component Dirac spinor: the Dirac spinor is a pair of Weyl spinors (one left-handed, one right-handed), and the complex conjugate of the pair gives the antiparticle components.

### What the Biquaternion Formulation Adds

The biquaternion formulation adds three things:

**1. A unified algebraic framework for Maxwell and Dirac.** The two equations have the same form in different representations of the same algebra. This is the algebraic content of the statement that the photon and the electron are both described by the Clifford algebra $\mathrm{Cl}_{1,3}$.

**2. A compact notation for the spinor structure.** The two-component structure of the Weyl spinor is naturally encoded in the biquaternion algebra, without the need for explicit spinor indices. The left- and right-handed spinors are the two chiral components of the field — the two minimal left ideals of $\mathbb{B}$ — and the mass term is the linear coupling between them.

**3. A natural language for relativistic kinematics.** The four-velocity $\tilde{U}$, the four-momentum $\tilde{P}$, and the mass-shell relation $\tilde{P}\tilde{P}^{\natural} = -m^2 c^2$ are all natural objects in the biquaternion algebra. The Dirac equation is naturally stated in terms of these objects, and the plane-wave solutions are naturally written in terms of the wave biquaternion $\tilde{k}$ and the four-position $\tilde{Q}$.

### The Mass as a Non-Integrable Phase

A different representation of the same spinor makes the mass look like a *phase*. Liu Yu-Fen's observation is that the mass term of the massive Dirac equation can be written as a coupling to a four-vector built from the field itself,

$$
m\,\bar\Psi\Psi = \bar\Psi\,K_\mu\gamma^\mu\Psi,
$$

with $K_\mu$ a unit complex four-vector. Read this way the massive equation is the massless equation with the ordinary derivative replaced by a "covariant" derivative along $K$, and the mass is a phase rather than a scalar. The phase is **non-integrable**: if $K_\mu = \partial_\mu\theta$ were a gradient, the change of variable $\Psi \mapsto e^{i\theta}\Psi$ would remove it and the field would be massless; the mass is exactly the statement that $K$ is not a gradient, and the obstruction is the field strength $\partial_\mu K_\nu - \partial_\nu K_\mu$.

The on-shell content of the reading is verified and simple: for a plane wave of momentum $p^\mu$ satisfying the mass shell $p^2 = m^2$, the vector

$$
K_\mu = \frac{p_\mu}{m}
$$

satisfies $K_\mu K^\mu = 1$. The momentum per unit mass is a unit vector, and the source reads it as the unit vector that carries the mass term.

This reading is the origin of the *triality construction* recorded in the companion articles. The two semi-spinors of the field, the vector they combine into, and the unit vector $K$ are the three spaces that the order-three map permutes; the mass term is the coupling that the order-three (cubic) form expresses. The reader who wants the construction itself is referred to *The s-Vector Representation of the Dirac Spinor in Biquaternionic Form*, *Triality and the Ding Construction for the Dirac Spinor in Biquaternionic Form*, and *Dual Equivalence of the Dirac and Topologically Massive Gauge Fields*. The present article records only the origin: the mass is a unit vector, a non-integrable phase, and it is the object the triality construction is built on.

## Open Questions

1. **The real structure $\flat$ and the electroweak interaction.** The conjugation $\flat = -{}^{*}$, whose fixed space is the anti-Hermitian sector $\mathbb{M}_-$ and which is the algebra's real structure, has the shape of a Majorana-type pairing. Does that real structure have a natural interpretation in terms of the electroweak interaction — in particular, does it supply the real form in which the neutrino is distinguished from the charged fermions?

2. **The relation to the Standard Model.** The Standard Model describes fermions in the spinor representation of the Lorentz group. How does the biquaternion framework extend to the full Standard Model, including the gauge fields?

3. **The non-abelian generalization.** The biquaternionic Dirac equation is abelian (the field is a single biquaternion). How does the framework extend to non-abelian gauge theories, where the fermion field is a vector in a representation of the gauge group?

4. **The relation to the twistor program.** Twistor theory uses the complexified spinor space $\mathbb{C}^4$, which is related to the biquaternion algebra. How do the biquaternion Dirac equation and the twistor equation relate?

5. **The quantization.** The Dirac equation is the classical equation of motion for a fermion field. How does the biquaternion framework extend to the quantized theory (quantum field theory), and what is the role of the biquaternion structure in the quantized case?

6. **The relation to the biquaternion Maxwell equation.** The two equations have the same form. Is there a deeper sense in which the photon and the electron are the same biquaternion field in different representations, or is the identity purely formal? **Partly answered**, in the section *The Lanczos Route: Maxwell with Feedback*: the shared object is the **operator** and the Dirac equation is the **closed** (feedback) way of obeying it, so the identity is structural rather than merely formal, and the fermionic statistics follow from the complex conjugation in the Lanczos form. What remains open is the feedback itself — the framework represents the mass feedback but does not derive it.

7. **The minimal coupling to electromagnetism.** The standard Dirac equation couples to the electromagnetic field through the minimal coupling $\partial_\mu \to \partial_\mu - iqA_\mu/\hbar$. How this coupling reads in the biquaternion framework, given the biquaternion form of the four-potential $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$, is treated in the companion article *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*.

These questions are open.

## Summary

The Dirac equation in biquaternionic form is the equation

$$
\tilde{\nabla}\tilde{\Psi} = 0
$$

in the massless case, and the chiral pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R
$$

for mass $m$, where $\tilde{\nabla}$ is the biquaternionic gradient, $\tilde{\Psi} = \tilde{\Psi}_L + \tilde{\Psi}_R$ is the spinor field with one component per chirality, and the mass term is linear. The massless equation has the same form as the source-free biquaternion Maxwell equation. The structural identity reflects the fact that both the photon and the electron are described by the same Clifford algebra $\mathrm{Cl}_{1,3}$, and the biquaternion algebra $\mathbb{B}$ is isomorphic to its even subalgebra. Each chiral component satisfies the Klein–Gordon equation $(\Box - m^2c^2/\hbar^2)\tilde{\Psi} = 0$.

The relativistic kinematic relations are naturally expressed in biquaternion form: the four-velocity $\tilde{U} = \gamma(ic\, e_0 + \mathbf{v})$ satisfies $\tilde{U}\tilde{U}^{\natural} = -c^2$, the four-momentum $\tilde{P} = m\tilde{U}$ satisfies the mass-shell relation $\tilde{P}\tilde{P}^{\natural} = -m^2 c^2$, and the four-position $\tilde{Q} = ict\, e_0 + \mathbf{x}$ gives the invariant interval $ds^2 = N(d\tilde{Q}) = d\tilde{Q}\circ\overline{d\tilde{Q}}$.

The plane-wave solutions of the massless equation are $\tilde{\Psi} = \tilde{\Psi}_0\exp\!\left(i\,\mathrm{Sc}(\tilde{k}\tilde{Q}^{\natural})\right) = \tilde{\Psi}_0\,e^{\,i(\mathbf{k}\cdot\mathbf{x}-\omega t)}$ with $\tilde{k}\tilde{\Psi}_0 = 0$ (nonzero solutions only for null $\tilde{k}$), giving the two spin states of a massless fermion. The massive plane waves satisfy the mass-shell condition $\tilde{k}\tilde{k}^{\natural} = -m^2 c^2/\hbar^2$; the two frequency branches are the particle and the antiparticle, and with the two spin states they give the four components of the Dirac spinor.

The spherical and cylindrical solutions are constructed by the methods of Clifford analysis, via the monogenic completion of harmonic functions. They describe the angular momentum states of the fermion field and the waveguide modes, respectively.

The biquaternion framework provides a compact and unified language for the Maxwell and Dirac equations, but it does not by itself derive the mass term or the electroweak structure. Those require additional physics beyond the algebraic framework.

There is also an explicit **dictionary** from the four-component bispinors onto the algebra, due to Kravchenko (1995). It is real-linear and not complex-linear: the spatial Dirac generators become left multiplication by the imaginary units, the timelike generator becomes the algebra's **complex conjugation** $\bar{\cdot}$, and the central imaginary acts on the right. The Dirac equation thereby becomes the single biquaternionic equation $\mathcal{N}F := (i\partial_0 + D - m\,i\,C M_{i_3})F = 0$, whose mass term carries the conjugation — the same complex conjugation, and the same coupling to a spatial direction, that the Lanczos route displays in $\tilde{\nabla}D = mD^{*}i\vec{\nu}$. The conjugation is the algebra's $\bar{\cdot}$ and not its real structure $\flat$; that distinction is what makes the dictionary consistent, since the retired $\flat$-based single-field mass term is the one that fails on the dispersion. The conjugation is removed by a change of variable, after which the time-harmonic amplitude obeys a shifted equation with a biquaternionic parameter — and that same conjugation-undone form carries the **integral representation of the harmonic spinor field**, with the Cauchy-type operator $K_\omega=A^{-1}KA$ and the Cauchy integral formula, Plemelj–Sokhotski formulas and boundary-value criterion that go with it.

The same construction has two consequences that belong to the equation rather than to its function theory. Removing the conjugation from the operator is possible: the operator is conjugate to $R = D-\partial_tM_{i_1}-mM_{i_2}$, whose coefficients are real quaternions and therefore carry no complex conjugation. Such an $R$ is **real**, and its reality means that the real and imaginary parts of any solution are separately solutions — one quaternionic solution gives two Dirac solutions, and the map $\Phi \mapsto iZ_c\Phi$ it produces is an involution. And the same dictionary relates the massive Dirac equation with an electric or scalar potential to the static sourceless Maxwell system of an inhomogeneous medium, $\epsilon = e^{2G}$ with $G' = g$; while on time-harmonic fields the Dirac field and the Maxwell field of a homogeneous medium share their projection identity exactly when $k^2 = \alpha^2$, the mass shell.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $i_1,i_2,i_3$ | The source's symbols for the quaternion units of the dictionary, the $e_1,e_2,e_3$ above; the scalar imaginary is its $i$ as here |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |
| $\mathbf{v}$ | Particle three-velocity |
| $\gamma = 1/\sqrt{1 - \mathbf{v}^2/c^2}$ | Lorentz factor |
| $\tilde{Q} = ict\,e_0 + \mathbf{x}$ | Four-position biquaternion |
| $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ | Four-velocity biquaternion |
| $\tilde{P} = m\tilde{U}$ | Four-momentum biquaternion |
| $\tilde{\nabla} = e_0\partial_{ict} + \sum_k e_k\partial_k$ | Biquaternionic gradient (Dirac operator) |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$ | d'Alembertian |
| $\tilde{\nabla}_\kappa = \tilde{\nabla} + \kappa$ | Shifted gradient, $\kappa \in \mathbb{C}$ central (companion d'Alembertian article) |
| $\tilde{\Psi} = \tilde{\Psi}_L + \tilde{\Psi}_R$ | Spinor field, one component per chirality |
| $\tilde{\Psi}^\flat = -\tilde{\Psi}^{*}$ | Anti-Hermitian conjugate (the algebra's real structure; not the mass term) |
| $A$ | Real-linear bijection from bispinors to biquaternion-valued functions (the explicit dictionary) |
| $C$, also written $^{*}$ | Componentwise complex conjugation; the timelike generator of that dictionary |
| $\mathcal{N} = i\partial_0 + D - m\,i\,C M_{i_3}$ | Biquaternionic Dirac operator with the conjugation in the mass term |
| $P_k^{\pm} = \tfrac12 M_{(1\pm i\,i_k)}$ | Complementary idempotents (right multiplications) of the source's factorisation $\mathcal{N}=u^{+}Ru^{-}$ |
| $R = P_1^{+}(i\partial_t+D)+P_1^{-}(-i\partial_t+D)-m\,M_{i_2} = D-\partial_tM_{i_1}-m\,M_{i_2}$ | The conjugation-free operator of the same source; *real*, with coefficients in $\mathbb{H}$, so $R[\mathrm{Re}\,F]=R[\mathrm{Im}\,F]=0$ |
| $\Phi' = iZ_c\Phi$ | The involutive symmetry of the Dirac equation that the reality of $R$ produces; $(iZ_c)^2=1$ |
| $\epsilon = e^{2G}$, $\vec{\nu} = \mathrm{grad}\,G$ | The Dirac potential $g=G'$ read as the inhomogeneity of a static Maxwell medium |
| $k = \omega\sqrt{\epsilon\mu}$ | Maxwell wave number; the Dirac–Maxwell correspondence holds iff $k^2=\omega^2-m^2$ |
| $D_\alpha\tilde{p} = 0$ | Shifted equation for the time-harmonic amplitude once $C$ is removed |
| $\varphi$ | Scalar (pseudoscalar-potential) coefficient of the shifted Dirac operator |
| $P_\pm$ | Right multiplication by the complementary null idempotents $\tfrac12(1\pm\alpha/\gamma)$; they split the pseudoscalar-potential equation into two scalar-coefficient equations, and they are the two helicity projectors of the time-harmonic field |
| $D_\omega = i\omega\gamma_0 + \sum_{k=1}^{3}\gamma_k\partial_k$ | Amplitude operator of the massless harmonic spinor field |
| $K_\omega = A^{-1} K A$ | Its Cauchy-type operator; the Cauchy integral formula, the Plemelj–Sokhotski formulas and the boundary-value criterion $\psi = K_\omega\psi$ on $\Gamma$ hold for it |
| $\tilde{k}$ | Wave biquaternion |
| $K_\mu$ | Unit complex four-vector carrying the mass term, $m\bar\Psi\Psi=\bar\Psi K_\mu\gamma^\mu\Psi$; $K_\mu=p_\mu/m$ on shell, $K_\mu K^\mu=1$ |
| $B^\mu, N^\mu$ | The two real four-vectors of the semi-spinors, $\Psi_1=B^\mu g_{\mu\nu}i\gamma^\nu v$, $\Psi_2=N^\mu g_{\mu\nu}i\gamma^\nu u$ |
| $G^\mu = B^\mu + iN^\mu$ | s-Vector, the vector representation of the same spinor |
| $m$ | Fermion mass |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original Dirac equation.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the foundational treatment of the Dirac equation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard physics treatment.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection between Clifford algebras and spinor fields.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric algebra approach to the Dirac equation.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of the Dirac equation in geometric algebra.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the spinor formulation of the Dirac equation.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the monogenic functions and the Clifford-analytic technique.
- L. A. Alexeyeva, "Differential algebra of biquaternions. Dirac equation and its generalized solutions," *Progress in Analysis, Proceedings of the 8th Congress of the ISAAC* (Moscow, 2013), pp. 153–161, for the biquaternion formulation of the Dirac equation.
- V. V. Kravchenko, "On a Biquaternionic Bag Model," *Zeitschrift für Analysis und ihre Anwendungen* **14** (1995), no. 1, 3–14, DOI 10.4171/ZAA/658, for the explicit real-linear dictionary from the four-component bispinors onto the biquaternions, with the timelike generator realized by complex conjugation — the images of the spatial generators, not readable from this source alone, are stated in the Doklady note of the next entry; for the biquaternionic Dirac operator $i\partial_0 + D - miCM_{i_3}$ whose mass term carries the conjugation; for the removal of the conjugation by a change of variable, realised as the factorisation $\mathcal{N}=u^{+}Ru^{-}$ with the conjugation-free operator $R=P_1^{+}(i\partial_t+D)+P_1^{-}(-i\partial_t+D)-mM_{i_2}=D-\partial_tM_{i_1}-mM_{i_2}$; and for the projectors $P_k^{\pm}=\tfrac12 M_{(1\pm i i_k)}$ of that factorisation.
- V. V. Kravchenko, "Quaternion-Valued Integral Representations of the Harmonic Electromagnetic and Spinor Fields," *Doklady Mathematics* **51** (1995), no. 2, 287–289 (translated from *Doklady Akademii Nauk* **341** (1995), no. 5, 603–605), for the dictionary of the preceding entry as a real-linear bijection with the mass term carrying complex conjugation, and for that dictionary in full — the components of $A$, and the images of the three timelike bivectors, $A(\gamma_0\gamma_1\Phi)=-i\,i_1A(\Phi)$, $A(\gamma_0\gamma_2\Phi)=-i\,i_2A(\Phi)$, $A(\gamma_0\gamma_3\Phi)=+i\,i_3A(\Phi)$, with the volume element carried by a right multiplication through $i_3$; for the bijection between the solutions of the Dirac equation and the solutions of the quaternionic equation $i\partial_tF+DF-\mathrm{Im}(F)\,i=0$; for the time-harmonic field $F = P_+f(\mathbf{x})e^{i\omega t}+P_-f(\mathbf{x})e^{-i\omega t}$ with the two projectors $P_\pm$ and the helicity reading of the two components; for the massless case $i\partial_tF+DF=0$, attributed there to Imaeda; and for the spinor-side integral representation recorded in the section *The Integral Representation of the Harmonic Spinor Field* — the amplitude operator $D_\omega\psi = i\omega\gamma_0\psi+\sum_{k=1}^{3}\gamma_k\partial_k\psi$, the Cauchy-type operator $K_\omega = A^{-1}KA$, and the three results that follow for it: the Cauchy integral formula, the Plemelj–Sokhotski formulas, and the boundary-value criterion $\psi = K_\omega\psi$ on $\Gamma$. The same note is the source of the unifying statement that one parametric system, at different values of its parameter, is the time-harmonic Maxwell system and the time-harmonic Dirac system; that statement is recorded in the companion *The Time-Harmonic Maxwell Operator and the Quaternionic Cauchy Integral*.
- K. Imaeda, "A new formulation of classical electrodynamics," *Il Nuovo Cimento B* **32** (1976) 138–162, for the quaternionic vacuum Maxwell equation $i\partial_tF+DF=0$, the equation the dictionary reduces to at vanishing mass.
- V. V. Kravchenko and M. V. Shapiro, *Integral Representations for Spatial Models of Mathematical Physics* (Pitman Research Notes in Mathematics 351, Addison-Wesley Longman, 1996), for the shifted operator $D_\alpha$ and its boundary-value theory, which is where the conjugated equation is taken once the conjugation has been removed.
- C. Lanczos, "Die tensoranalytischen Beziehungen der Diracschen Gleichung," *Zeitschrift für Physik* **57** (1929) 447–473, 474–483, 484–493 (arXiv:physics/0508002, physics/0508012, physics/0508013), for the coupled biquaternion system from which the Dirac equation descends and for the idempotent superposition that produces it.
- F. Gürsey, "Applications of Quaternions to Field Equations," PhD thesis, University of London, 1950, for the review of Lanczos's quaternionic theory and for the treatment of the scalar, vector, pseudoscalar and pseudovector equations as degenerate cases of it.
- A. Gsponer and J.-P. Hurni, "The physical heritage of Sir W. R. Hamilton," arXiv:math-ph/0201058, §8, for the reading of Lanczos's system as Maxwell's equation with feedback, for the spin-quantization-axis form $\tilde{\nabla}D=mD^{*}i\vec{\nu}$ of the Dirac–Lanczos equation, and for the complex-conjugation origin of the fermionic character.
- A. Gsponer and J.-P. Hurni, "Lanczos's Equation to Replace Dirac's Equation?", *Proceedings of the Cornelius Lanczos International Centenary Conference* (SIAM, 1994) 509–512 (arXiv:hep-ph/0112317), for Lanczos's coupled system as "Maxwell's equations with feed-back" and for the second route to Dirac's equation, the reduction by requiring the two fields to be singular quaternions, attributed there to J. Blaton, *Zeitschrift für Physik* **95** (1935) 337–354. Recorded as a claim: four pages, no derivation exhibited, and the title is a question; the arXiv version carries a *Note added in 1996* withdrawing the authors' charge-quantisation mechanism, which is recorded in *The Standard Model under the Biquaternion Framework — A Research Agenda*.
- V. V. Kravchenko, *Applied Quaternionic Analysis* (Research and Exposition in Mathematics 28, Heldermann, 2003), §§4.2.1–4.2.2.1, for the four standard Dirac potentials — electric, scalar, pseudoscalar, magnetic — in quaternionic form, for the single constant transformation that relates the classical and quaternionic Dirac operators with potentials, and for the reduction of the pseudoscalar-potential equation to a pair of scalar-coefficient equations.
- V. V. Kravchenko and M. P. Ramirez Tachiquin, "On a quaternionic reformulation of the Dirac equation and its relationship with Maxwell's system," *Bulletin de la Société des Sciences et des Lettres de Łódź* **53** (2003) 101–114, for the **reality** of the conjugation-free quaternionic Dirac operator — $R = D-\partial_tM_{i_1}-mM_{i_2}$, with coefficients in the real quaternion algebra, hence $R[\mathrm{Re}\,F]=R[\mathrm{Im}\,F]=0$ — and for the **involutive symmetry** $\Phi'=iZ_c\Phi$ that follows, the symmetry itself attributed there to J. Niederle and A. G. Nikitin, "Involutive symmetries, supersymmetries and reductions of the Dirac equation," *J. Phys. A: Math. Gen.* **30** (1997) 999–1010; for the correspondence between the massive Dirac equation with an electric or a scalar potential and the static sourceless Maxwell system of an isotropic inhomogeneous medium, with the permittivity $\epsilon=e^{2G(x_1)}$, $G'=g$; for the condition $k^2=\alpha^2$ under which the massive Dirac field and the time-harmonic Maxwell field share the same projection identity, that condition being the mass shell; and for the quaternionic current-conservation equation $\partial_t|F|^2 = -\hbar[(DF^{\dagger})F+F^{*}(DF)]$ with the identity $|F|^2=|\Phi|^2$ of the biquaternion modulus and the Dirac density. The paper's factors $u^{\pm}$ of the factorisation $\mathcal{N}=u^{+}Ru^{-}$ and its explicit action of $A^{-1}$ on $\mathrm{Re}\,F$ are quoted, not reproduced: the available copy is a scan without a text layer.
- V. G. Bagrov and D. M. Gitman, *Exact Solutions of Relativistic Wave Equations* (Kluwer, Dordrecht, 1990), for the encyclopaedic compendium and review of the known exact solutions of the Dirac equation up to the late 1980s.
- Liu Yu-Fen, "Triality, Biquaternion and Vector Representation of the Dirac Equation," arXiv:math-ph/0109008 (2001), for the reading of the mass term as a coupling $\bar\Psi K_\mu\gamma^\mu\Psi$ to a unit vector, hence as a non-integrable phase; and for the vector representation of the spinor built on it, recorded in the companion *The s-Vector Representation of the Dirac Spinor in Biquaternionic Form*.
- Liu Yu-Fen, "Triality and Dual Equivalence Between Dirac Field and Topologically Massive Gauge Field," arXiv:hep-th/0602275 (2006), for the same reading in the order-$\ell$ ding language, and for the parent-action duality recorded in *Dual Equivalence of the Dirac and Topologically Massive Gauge Fields*.

