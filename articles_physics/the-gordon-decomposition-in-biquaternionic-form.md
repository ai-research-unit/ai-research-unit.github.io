# __The Gordon Decomposition of the Dirac Current in Biquaternionic Form__

## Introduction

The **Gordon decomposition** is an identity for the conserved current of a solution of the Dirac equation. It splits the four components of the current, $\bar\psi\gamma_\mu\psi$, into two pieces of different physical character: a **convection** part, which is the orbital current of a charged particle carried by the momentum, and a **spin** part, which is the divergence of a spin density and is the source of the magnetization. The identity is due to Walter Gordon (1926) and is used wherever the magnetic behaviour of the electron is extracted from the Dirac equation: the spin part is the term whose coefficient fixes the tree-level gyromagnetic factor at $g = 2$, and whose radiative correction is the anomalous magnetic moment.

The decomposition is **on shell**. It uses the Dirac equation for the field and for its adjoint, and it therefore holds for solutions and not for arbitrary spinor functions. It also requires a nonzero mass in its Lorentz-covariant form, because the mass appears in the denominator of both terms; the massless case has a separate, energy-normalised reading, in which the spin term survives as the curl of the spin density and only the scale changes from $m$ to $E$.

This article states the identity, proves it, gives its momentum-space form and its massless limit, and reports the two companion objects — the angular-momentum (Belinfante–Rosenfeld) split and the stress tensor — that come with it. It then gives the biquaternion interpretation. The framework's contribution here is a matter of **naming the two structures**: the split is the split of a product of two Clifford generators into its symmetric part, which is the metric and is central in the algebra, and its antisymmetric part, which is a bivector and lies in the algebra's six-dimensional bivector subspace. The convection current is the central, metric direction; the spin current is the bivector. What the framework does **not** supply is a pure biquaternion product that equals the current, for the same representation-theoretic reason recorded in the companion article on minimal coupling: the Dirac adjoint carries the Clifford-odd cell $iR_{\vec e_x} = iL_{e_t}R_{\vec e_x}$, which is outside the left copy $\mathbb{B}_L$ of the biquaternion algebra.

The article is organised as follows. The next section fixes the conventions: the algebra, the generator cells, the two Dirac equations and the current. The section after it states the identity and proves it. A section gives the momentum-space form used in scattering. A section reads the two terms physically. A section gives the massless limit and says what survives it. A section records the angular-momentum and stress-tensor relatives and the electromagnetic (Pauli-moment) consequence. A section gives the biquaternion interpretation. The closing sections are the open questions, the gamma formulation, the summary, the notation table and the literature.

## Conventions

### The Algebra and the Cells

A **cell** is the two-sided operator $L_{a}R_{b}$, with $L_a\psi = a\psi$ and $R_b\psi = \psi b$; $L_{e_t}R_{e_t}$ is the identity and $L_{a}R_{b}L_{c}R_{d} = L_{ac}R_{db}$. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with units $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, $\vec e_k^2 = -e_t$, central scalar imaginary $i$, and the dictionary $\mathsf{M}_2$ of the companion articles.

The **generators** are the four cells of the canonical frame, written $\gamma_\mu$ and read as cells:

$$
\gamma_\mu=iL_{e_\mu}R_{\delta_\mu},
\qquad
\delta_t=\vec e_x,\quad\delta_k=\vec e_y,
\qquad
L_{e_\mu}R_{\delta_\mu}=-i\gamma_\mu .
$$

They split into two families:

| family | cell | square |
|---|---|---|
| temporal | $L_{e_t}R_{\vec e_x}$ | $+L_{e_t}R_{e_t}$ |
| spatial | $L_{\vec e_k}R_{\vec e_y}$ | $-L_{e_t}R_{e_t}$ |

The two families anticommute, so the four generators carry the Clifford relations of $g=\mathrm{diag}(+1,-1,-1,-1)$,

$$
\left\{\gamma_\mu,\gamma_\nu\right\}=2g_{\mu\nu}L_{e_t}R_{e_t}.
$$

**The rule $i^2=-1$.** The scalar imaginary is a unit, so a second factor of $i$ is never carried through a display: it multiplies out into a sign. Three collapses are used below,

$$
i\gamma_\mu=-L_{e_\mu}R_{\delta_\mu},
\qquad
\left(iR_{\vec e_x}\right)^2=L_{e_t}R_{e_t},
\qquad
i\sigma_{\mu\nu}=\tfrac12\left[L_{e_\mu}R_{\delta_\mu},L_{e_\nu}R_{\delta_\nu}\right],
$$

the first because $\gamma_\mu$ already carries one factor of $i$, the second because the two factors of $i$ and the two factors of $\vec e_x$ cancel in pairs, and the third because the commutator of two real cells is $2i\sigma_{\mu\nu}$.

**Chirality.** The chirality cell is

$$
\gamma_5=-iR_{\vec e_z}=-iL_{e_t}R_{\vec e_z},
\qquad
\gamma_5^2=L_{e_t}R_{e_t},
\qquad
\left\{\gamma_\mu,\gamma_5\right\}=0 .
$$

**Bivectors.** The bivector is $\sigma_{\mu\nu}=\frac{i}{2}\left[\gamma_\mu,\gamma_\nu\right]$, one cell per pair, and the spin generator of the Lorentz transformations is its half, $\Sigma_{\mu\nu}=\frac12\sigma_{\mu\nu}$, whose imaginary multiple is a commutator of real cells,

$$
i\Sigma_{\mu\nu}=\tfrac14\left[L_{e_\mu}R_{\delta_\mu},L_{e_\nu}R_{\delta_\nu}\right].
$$

The six bivectors are

$$
\sigma_{0k}=iL_{\vec e_k}R_{\vec e_z},
\qquad
\sigma_{12}=iL_{\vec e_z}R_{e_t},
\qquad
\sigma_{13}=-iL_{\vec e_y}R_{e_t},
\qquad
\sigma_{23}=iL_{\vec e_x}R_{e_t},
$$

with the antisymmetric partners.

**The adjoint.** The Dirac adjoint is the row $\bar\psi=\psi^\dagger\gamma_0$, that is $\psi^\dagger iR_{\vec e_x}$, the Hermitian conjugate of the column followed by the timelike generator. The generator is Hermitian under this conjugation and the real cell is not:

$$
\gamma_0\gamma_\mu^{\dagger}\gamma_0=\gamma_\mu,
\qquad
\gamma_0\left(L_{e_\mu}R_{\delta_\mu}\right)^{\dagger}\gamma_0=-L_{e_\mu}R_{\delta_\mu},
$$

and the minus sign is the one that the mass term inherits in the adjoint equation below.

### The Two Dirac Equations

Two equations are in play, and the decomposition uses both. The first is the **Dirac equation** on the spinor module,

$$
i\sum_\mu\varepsilon_\mu\gamma_\mu\nabla_\mu\psi=m\psi ,
\qquad
\varepsilon=(1,-1,-1,-1),
$$

and the rule $i\gamma_\mu=-L_{e_\mu}R_{\delta_\mu}$ writes the same equation without an imaginary unit,

$$
\sum_\mu\varepsilon_\mu L_{e_\mu}R_{\delta_\mu}\nabla_\mu\psi+m\psi=0 .
$$

The component form displays the two families at once, because $i\gamma_0=-R_{\vec e_x}$ and $i\gamma_k=-L_{\vec e_k}R_{\vec e_y}$:

$$
\sum_k\vec e_k\nabla_k\psi\,\vec e_y-\nabla_t\psi\,\vec e_x=m\psi .
$$

The temporal term is one right multiplication, by $\vec e_x$; the three spatial terms share the right multiplier $\vec e_y$, so the four-term contraction collapses to two. The weight $\varepsilon_\mu$ raises the index of the generator, so the contraction is the raised generator against a low-index derivative; it is not a second metric factor.

The same equation is the spinor-module representative of the **chiral pair** of the biquaternion series,

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,
\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R ,
$$

whose two members act by left multiplication on the algebra and whose mass term pairs the two chiral halves. The pair is the equation in $\mathbb{B}$; the cell equation above is its representative on the module, and the Gordon identity below is a statement about that representative.

The second equation is the **adjoint**. Taking the dagger of the real-cell equation and multiplying on the right by $\gamma_0$ gives

$$
-i\sum_\mu\varepsilon_\mu\left(\nabla_\mu\bar\psi\right)\gamma_\mu=m\bar\psi ,
\qquad
\sum_\mu\varepsilon_\mu\left(\nabla_\mu\bar\psi\right)L_{e_\mu}R_{\delta_\mu}-m\bar\psi=0 ,
$$

where the passage uses $\bar\psi=\psi^\dagger\gamma_0$ and the two conjugation signs of the conventions: the conjugation leaves $\gamma_\mu$ unchanged and reverses the sign of $L_{e_\mu}R_{\delta_\mu}$, and that reversal is why the mass term enters the adjoint with the other sign. The two equations are displayed separately because the proof below puts one factor on each side of the current.

### The Current

The **number current** of a solution is

$$
j_\mu=\bar\psi\gamma_\mu\psi ,
$$

and the temporal component is the density, with the two factors of $i$ multiplied out:

$$
j_0=\bar\psi\gamma_0\psi=\psi^\dagger\gamma_0^2\psi=\psi^\dagger\psi,
\qquad
\gamma_0^2=\left(iR_{\vec e_x}\right)^2=i^2R_{\vec e_x}R_{\vec e_x}=-R_{-e_t}=L_{e_t}R_{e_t}.
$$

The scalar $i^2=-1$ and the product $\vec e_x\vec e_x=-e_t$ give $+1$ together, and that is why the density is positive rather than a sign of the frame.

The four components are the four generators in the same expectation. The index $\mu$ labels the four cells; it is not the index of one object inside the algebra. No product in $\mathbb{B}$ turns the temporal cell into a spatial one, and the four components are four different expectations rather than four slots of a single element. For a solution the four are real, and $j_0$ is positive.

## The Identity

### Statement

Let $\psi$ be a solution of the Dirac equation of §*The Two Dirac Equations*. The Gordon decomposition splits the current into two terms of different character: a **convection** part, which carries the first derivative of the field itself, and a **spin** part, which is the divergence of the antisymmetric density $\bar\psi\Sigma_{\mu\nu}\psi$ built from the spin generator of the conventions.

$$
\boxed{\;\bar\psi\,\gamma_\mu\psi
= \frac{i}{2m}\left(\bar\psi\,\nabla_\mu\psi - \left(\nabla_\mu\bar\psi\right)\psi\right)
+ \frac{1}{m}\sum_\nu\varepsilon_\nu\,\nabla_\nu\left(\bar\psi\,\Sigma_{\mu\nu}\psi\right)\;}
$$

The convection term carries the derivative of the field and of the adjoint, and it is the piece that survives as the transport current. The spin term is a total divergence: $\Sigma_{\mu\nu}$ is antisymmetric, $\Sigma_{\mu\nu}=-\Sigma_{\nu\mu}$, so that the second term is the divergence of an antisymmetric tensor density.

### Proof

The proof uses the two equations, one factor on each side of the current. Write the real-cell equation as $\sum_\nu\varepsilon_\nu L_{e_\nu}R_{\delta_\nu}\nabla_\nu\psi=-m\psi$ and multiply it by $\bar\psi\gamma_\mu$ on the left:

$$
-m\,j_\mu=\sum_\nu\varepsilon_\nu\,\bar\psi\,\gamma_\mu L_{e_\nu}R_{\delta_\nu}\nabla_\nu\psi .
$$

Multiply the adjoint, $\sum_\nu\varepsilon_\nu\left(\nabla_\nu\bar\psi\right)L_{e_\nu}R_{\delta_\nu}=m\bar\psi$, by $\gamma_\mu\psi$ on the right:

$$
m\,j_\mu=\sum_\nu\varepsilon_\nu\left(\nabla_\nu\bar\psi\right)L_{e_\nu}R_{\delta_\nu}\gamma_\mu\psi .
$$

Adding the two eliminates the mass on the left, and the two mixed products that appear are

$$
\gamma_\mu L_{e_\nu}R_{\delta_\nu}=-ig_{\mu\nu}-\sigma_{\mu\nu},
\qquad
L_{e_\nu}R_{\delta_\nu}\gamma_\mu=-ig_{\mu\nu}+\sigma_{\mu\nu},
$$

which follow from $\gamma_\mu=iL_{e_\mu}R_{\delta_\mu}$ and the Clifford relation, with the imaginary unit multiplied out. Substituting and collecting the metric and bivector parts,

$$
2m\,j_\mu=\sum_\nu\varepsilon_\nu\left[\left(ig_{\mu\nu}+\sigma_{\mu\nu}\right)\bar\psi\,\nabla_\nu\psi
+\left(-ig_{\mu\nu}+\sigma_{\mu\nu}\right)\left(\nabla_\nu\bar\psi\right)\psi\right].
$$

The metric part carries the weight $\varepsilon_\nu g_{\mu\nu}$, which is $1$ at $\nu=\mu$ and $0$ otherwise, so that part reduces to the single term $\nu=\mu$. The bivector part keeps the sum, and its two terms combine into a total derivative because $\sigma_{\mu\nu}$ is constant and antisymmetric:

$$
2m\,j_\mu=i\left(\bar\psi\,\nabla_\mu\psi-\left(\nabla_\mu\bar\psi\right)\psi\right)
+\sum_\nu\varepsilon_\nu\,\nabla_\nu\left(\bar\psi\,\sigma_{\mu\nu}\psi\right).
$$

Since $\sigma_{\mu\nu}=2\Sigma_{\mu\nu}$, dividing by $2m$ gives the identity as stated.

The algebra was checked numerically in the conventions above. The Clifford relations, the four bivector components, the three collapses of $i^2=-1$, the conjugation signs $\gamma_0\gamma_\mu^{\dagger}\gamma_0=\gamma_\mu$ and $\gamma_0\left(L_{e_\mu}R_{\delta_\mu}\right)^{\dagger}\gamma_0=-L_{e_\mu}R_{\delta_\mu}$, and the two mixed products held with residual $0$; the two Dirac equations held to $8\times10^{-15}$ on a three-mode superposition. The position-space identity held to $4\times10^{-14}$ in all four components, the momentum-space form below to $1.6\times10^{-13}$ over $200$ random on-shell pairs, its parent identity to $5\times10^{-14}$, and its axial companion to $4\times10^{-14}$.

### A note on the total divergence

The spin term is a total divergence, and its own divergence vanishes identically: $\nabla_\mu\nabla_\nu$ is symmetric in the two indices while $\sigma_{\mu\nu}$ is antisymmetric, so the spin current is conserved without the field equation being used. It is a **bound** current rather than a transport current. It can be removed from the current at the price of a surface term, it contributes nothing to the total charge, and it cannot be removed from the magnetic moment, which is the integral of the spin density. The convection term is separately conserved on shell, by the two Dirac equations. What the decomposition separates is therefore not a conserved piece and a non-conserved one, but a transport current and a magnetisation current.

## The Momentum-Space Form

For plane-wave solutions the position-space identity becomes the form used in scattering amplitudes. Write the field of momentum $p$ as

$$
\psi=w(p)\exp\left(-i\sum_\mu p_\mu x_\mu\right),
$$

so that $\nabla_\mu\psi=-ip_\mu\psi$, and the Dirac equation becomes the on-shell condition

$$
\left(\sum_\mu\varepsilon_\mu\,\gamma_\mu\,p_\mu-m\right)w(p)=0 .
$$

The exponent carries no weight $\varepsilon_\mu$. The weight belongs to the contraction of the cell with the momentum, where it raises the cell's index, and the derivative returns $p_\mu$ with the same sign for all four components. A weight in the exponent would flip the sign of the three spatial derivatives and would make the position-space identity and the momentum-space identity below disagree on the sign of the spatial convection current.

Let $\bar w(p_2)$ be the adjoint spinor of an on-shell momentum $p_2$, which satisfies the same condition on the other side,

$$
\bar w(p_2)\left(\sum_\mu\varepsilon_\mu\,\gamma_\mu\,p_{2,\mu}-m\right)=0 .
$$

Between such spinors the Gordon decomposition reads

$$
\boxed{\;\bar w(p_2)\,\gamma_\mu\,w(p)
= \bar w(p_2)\left[
\frac{(p+p_2)_\mu}{2m}
+ \frac{i\sum_\nu\varepsilon_\nu\,\sigma_{\mu\nu}(p_2-p)_\nu}{2m}
\right]w(p)\;}
$$

Equivalently, with the momentum transfer $k = p_2 - p$ and the average momentum $P = \tfrac12(p+p_2)$,

$$
\bar w(p_2)\,\gamma_\mu\,w(p)
= \frac{1}{m}\left[P_\mu\,\bar w_2w
+ i\sum_\nu\varepsilon_\nu\,\bar w_2\Sigma_{\mu\nu}w\,k_\nu\right],
\qquad
\Sigma_{\mu\nu} = \tfrac12\sigma_{\mu\nu} .
$$

The first term is proportional to the scalar bilinear $\bar w_2w$, the second to the tensor bilinear $\bar w_2\Sigma_{\mu\nu}w$. The two coefficients are fixed: the first is $P_\mu/m$, the second is $i k_\nu/m$. This is the form in which the vertex decomposition of the companion article on the anomalous magnetic moment is stated, and it is the identity that was verified numerically there and here.

### Parent identity

Both momentum-space statements are consequences of the simpler **parent identity**, valid for any cell $\Gamma$ and any on-shell pair,

$$
2m\,\bar w(p_2)\,\Gamma\,w(p)
= \bar w(p_2)\left(\sum_\mu\varepsilon_\mu\,\gamma_\mu\,p_{2,\mu}\,\Gamma
+ \Gamma\sum_\mu\varepsilon_\mu\,\gamma_\mu\,p_\mu\right)w(p),
$$

which follows from the two on-shell conditions on $w(p_2)$ and on $\bar w(p_2)$, and is the form in which the companion article on the anomalous magnetic moment states it. With $\Gamma = \gamma_\mu$ the parent identity gives the Gordon form.

The **axial companion** takes $\Gamma = \gamma_\mu\gamma_5$, the product of the generator and the chirality cell. The axial vertex is one product, not a difference of two cells. Because the chirality cell anticommutes with every generator, the term that carries the metric changes sign relative to the term that carries the bivector, and the roles of the average momentum and of the transfer are exchanged:

$$
\bar w(p_2)\,\gamma_\mu\gamma_5\,w(p)
= \bar w(p_2)\,\gamma_5\left[
\frac{(p_2-p)_\mu}{2m}
+ \frac{i\sum_\nu\varepsilon_\nu\,\sigma_{\mu\nu}(p_2+p)_\nu}{2m}
\right]w(p).
$$

The two products of the parent identity are read off from the Clifford relation, with the momentum contracted into the generators and the imaginary unit multiplied out:

$$
\sum_\rho\varepsilon_\rho\gamma_\rho p_{2,\rho}\,\gamma_\mu=p_{2,\mu}+i\sum_\nu\varepsilon_\nu\sigma_{\mu\nu}p_{2,\nu},
\qquad
\gamma_\mu\sum_\rho\varepsilon_\rho\gamma_\rho p_{1,\rho}=p_{1,\mu}-i\sum_\nu\varepsilon_\nu\sigma_{\mu\nu}p_{1,\nu},
$$

for the vector vertex, and, because $\gamma_5$ anticommutes with every generator,

$$
\sum_\rho\varepsilon_\rho\gamma_\rho p_{2,\rho}\,\gamma_\mu\gamma_5=\gamma_5\left(p_{2,\mu}+i\sum_\nu\varepsilon_\nu\sigma_{\mu\nu}p_{2,\nu}\right),
\qquad
\gamma_\mu\gamma_5\sum_\rho\varepsilon_\rho\gamma_\rho p_{1,\rho}=\gamma_5\left(-p_{1,\mu}+i\sum_\nu\varepsilon_\nu\sigma_{\mu\nu}p_{1,\nu}\right),
$$

for the axial one. The sum of the two vector products is $(p+p_2)_\mu+i\sum_\nu\varepsilon_\nu\sigma_{\mu\nu}(p_2-p)_\nu$, which is $2m$ times the bracket of the vector identity; the sum of the two axial products is $\gamma_5\left[(p_2-p)_\mu+i\sum_\nu\varepsilon_\nu\sigma_{\mu\nu}(p_2+p)_\nu\right]$, which is $2m$ times the bracket of the axial identity. The transfer sits in the convection slot of one and in the spin slot of the other, and the average momentum does the opposite, because the chirality cell reverses the sign of the metric part while leaving the bivector part alone.

The vector identity has the average momentum in the convection slot and the transfer in the spin slot; the axial identity has the transfer in the convection slot and the average momentum in the spin slot. That exchange is the algebraic content of the axial version, and it is what leaves the axial current with a spin coefficient that the anomaly can correct.

## The Physical Reading

### Convection and spin

The two terms of the momentum-space identity have a direct interpretation, and it is the reason the decomposition is useful.

The **convection term** $\bar w_2\frac{(p+p_2)_\mu}{2m}w$ is the current of a charged scalar of mass $m$ and momentum $\tfrac12(p+p_2)$. It is the orbital part: it depends on the average four-momentum, it reduces to $\bar w_2\gamma_\mu w\to\bar w_2w\,v_\mu$ in the non-relativistic limit, and it is the piece protected by gauge invariance.

The **spin term** $\bar w_2\frac{i\sum_\nu\varepsilon_\nu\,\sigma_{\mu\nu}(p_2-p)_\nu}{2m}w$ depends on the momentum **transfer** $k_\nu$ and on the tensor bilinear. It is the piece that couples to the field strength rather than to the potential: contracted with the momentum-space photon, it produces an effective Pauli moment term. Its coefficient is exactly the one that gives $g = 2$, as the next subsection shows.

The identification of the second term with the spin density is not a metaphor. In position space the second term is $\frac{1}{m}\sum_\nu\varepsilon_\nu\nabla_\nu\left(\bar\psi\Sigma_{\mu\nu}\psi\right)$; the spatial components of the tensor density are the spin angular-momentum density, and the magnetic moment is its integral.

### The magnetic moment and $g=2$

Contract the spin term with the photon field. The interaction is $-\sum_\mu\varepsilon_\mu A_\mu j_\mu$, and the spin-dependent part contributes, up to a total divergence,

$$
-\frac{e\hbar}{2mc}\sum_{\mu,\nu}\varepsilon_\mu\varepsilon_\nu\,\nabla_\nu A_\mu\,\bar\psi\sigma_{\nu\mu}\psi
= -\frac{e\hbar}{2mc}\cdot\tfrac12\sum_{\mu,\nu}\varepsilon_\mu\varepsilon_\nu\,F_{\mu\nu}\,\bar\psi\sigma_{\mu\nu}\psi,
$$

which is an effective **Pauli moment term** $-\frac{e\hbar}{2mc}\,\vec B\cdot\psi^\dagger\boldsymbol\sigma\psi$. Its coefficient is the Dirac value $g = 2$. The companion article on the anomalous magnetic moment splits the same vertex as

$$
\Gamma_\mu=\gamma_\mu\,F_1(k^2)+\frac{i\sum_\nu\varepsilon_\nu\,\sigma_{\mu\nu}k_\nu}{2m}F_2(k^2),
\qquad
g=2\left(1+F_2(0)\right),
$$

with $F_1(0)=1$ and $F_2(0)=0$ at tree level. The tree vertex is the generator alone; the Gordon identity rewrites that one structure as the sum of the convection and spin terms with equal coefficients, and that rewriting is the statement $g=2$. The anomaly is the part of the spin coefficient that the identity does not force, that is, the radiative correction to $F_2(0)$; the convection coefficient is protected by the Ward identity.

The same decomposition underlies the companion article on the classical origin of $g = 2$: the factor of two is the statement that the spin-density gradient is twice as effective at generating an electric current as it is at contributing to the linear momentum, which is the factor-of-two asymmetry recorded below.

## The Massless Limit

The covariant identity needs $m \neq 0$, because both terms carry $1/m$. A massless field has no mass to divide by, and the energy $E$ is the only scale available. The **structure** of the decomposition survives this step, and only the normalisation changes: one term is still a transport current, the other is still a total divergence.

Two statements can be made without a new derivation. The convection term, for a near plane wave of finite extent, is the charge transported at the group velocity, $e\rho\,\vec k/E = e\rho\,\vec v$ with $\rho = \psi^\dagger\psi$ and $\vec v = \vec k/E$; this reading uses only $\psi^\dagger\psi$ and the momentum, and it is the same in both regimes. The spin term is the divergence of the spin density, and in three dimensions the divergence of the antisymmetric pair of spatial indices is the curl of the spin three-vector,

$$
\vec S = \psi^\dagger\vec\Sigma\,\psi,
\qquad
\vec\Sigma = \left(\Sigma_{23},\Sigma_{31},\Sigma_{12}\right),
\qquad
\Sigma_{jk} = \tfrac12\sigma_{jk},
$$

so that the spin term is a curl in the massless case exactly as it is in the massive one. What changes is the coefficient: $1/m$ in the massive identity, and $1/E$ in the massless regime, where $E$ is the only scale that can multiply a density to give a current.

For a massless right-handed Weyl particle the spin is locked to the direction $\vec u_k$ of the kinetic momentum, and the moment reads $\vec\mu = (e/E)(\hbar\vec u_k/2)$: the massless limit removes the separation scale $m$ in favour of the energy $E$, and it does not remove the spin current. The rest-frame statement, where $E = m$ and the coefficient of the curl is $1/m$, is the one that fixes $g = 2$, and it is the statement of the next section.

## The Angular-Momentum and Stress-Tensor Relatives

The same split appears in the energy–momentum tensor, and the comparison is instructive because the numerical coefficients differ.

The symmetric **Belinfante–Rosenfeld** tensor is

$$
T_{\mu\nu}^{\rm BR}
= \frac{i}{4}\left(\bar\psi\,\gamma_\mu\nabla_\nu\psi
- \left(\nabla_\nu\bar\psi\right)\gamma_\mu\psi
+ \bar\psi\,\gamma_\nu\nabla_\mu\psi
- \left(\nabla_\mu\bar\psi\right)\gamma_\nu\psi\right),
$$

and on shell its time components give the energy density $\mathcal E = E\,\psi^\dagger\psi$ and the momentum density

$$
\vec P = \frac{1}{2i}\left(\psi^\dagger\nabla\psi - \left(\nabla\psi^\dagger\right)\psi\right)
+ \frac12\nabla\times\vec S .
$$

Compare this with the spin term of the Gordon identity: the spin contribution to the momentum density carries the coefficient $\tfrac12$, while the spin contribution to the electric current carries $1$. The spin-density gradient is therefore **twice as effective** at producing an electric current as at contributing to the linear momentum, and that factor of two is the Dirac value $g = 2$ seen from the angular-momentum side.

The canonical (non-symmetric) tensor

$$
T_{\mu\nu}^{\rm canonical}
= \frac{i}{2}\left(\bar\psi\,\gamma_\mu\nabla_\nu\psi
- \left(\nabla_\nu\bar\psi\right)\gamma_\mu\psi\right)
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
\gamma_\mu\gamma_\nu=g_{\mu\nu}L_{e_t}R_{e_t}-i\sigma_{\mu\nu},
$$

the two pieces being respectively the **metric** (one number per pair of indices, symmetric, and in the algebra's terms central) and the **bivector** (antisymmetric, and in the algebra's terms the six-dimensional subspace spanned by the directions $\vec e_k$ and $i\vec e_k$). The Gordon decomposition is the statement that on shell the current splits in exactly this way: the convection term is the metric–central direction, and the spin term is the bivector direction. This is the same identification the companion article on the anomalous magnetic moment records: the anomaly multiplies $\sigma_{\mu\nu}$, a bivector, and is therefore an informational-sector object, while the tree-level convection term is central.

The comparison map of *Matrix Representations Conventions*, §*The Clifford Structure and the Frame*, reads the real units in the canonical frame as $e_\mu\mapsto L_{e_\mu}R_{e_t}$ and $i\mapsto L_{e_t}R_{\vec e_z}$. On the eight real units it sends the three vector units to the spacelike bivectors and the three imaginary units to the timelike ones,

$$
\vec e_k\longmapsto L_{\vec e_k}R_{e_t},
\qquad
i\vec e_k\longmapsto L_{e_t}R_{\vec e_z}L_{\vec e_k}R_{e_t}=L_{\vec e_k}R_{\vec e_z}.
$$

The **rotation-type** generators — the magnetic, spin-like ones, which are the timelike bivectors — sit therefore at the elements $i\vec e_k \in \mathbb{M}_+$, the informational sector, and the **boost-type** generators, the spacelike bivectors, at $\vec e_k \in \mathbb{M}_-$, the material sector. In the frame used here the magnetic bivectors are the cells $\sigma_{0k}=iL_{\vec e_k}R_{\vec e_z}$ listed in the conventions, which are exactly the timelike ones, and the boosts are the three $\sigma_{jk}$; the frame cells of this article carry the right multiplier $\vec e_y$ in place of $e_t$, which is a change of frame and not a change of the dictionary. The magnetic (spin) part of the Gordon split is therefore an $\mathbb{M}_+$ structure — the same sector as the spin itself — and the convection part is the central metric direction. The sector labels are not decoration: they are the algebraic form of the statement that the convection term is the orbital transport and the spin term is the intrinsic moment.

### What the framework does not supply

The current $\bar\psi\gamma_\mu\psi=j_\mu$ is not a pure biquaternion product. This is the negative result of the companion minimal-coupling article: the Dirac adjoint $\bar\psi = \psi^\dagger iR_{\vec e_x}$ carries the Clifford-odd cell $iR_{\vec e_x} = iL_{e_t}R_{\vec e_x}$, which is not a left multiplier of $\mathbb{B}$, and a bilinear built only from $\tilde\Psi$ and $\tilde\Psi^{*}$ inside $\mathbb{B}$ cannot supply it. Consequently the Gordon decomposition is a statement about the **spinor-module** current. The framework transcribes it, names its two structures in the algebra's own sectors, and verifies the algebra of the split; it does not derive the identity from a product in $\mathbb{B}$. The same caveat applies to the axial companion identity, which carries $-iR_{\vec e_z}$ in addition to $iR_{\vec e_x}$.

What the algebra does supply is the location of the two terms: the convection term is the central, metric direction, and the spin term is the bivector direction, with the magnetic part of the bivector in the informational sector. That placement is a real bookkeeping statement, and it is the framework's contribution to this identity.

## Open Questions

1. **A biquaternion-natural current.** Is there a $\mathbb{B}$-valued current whose symmetric/antisymmetric split reproduces the Gordon split without the two-sided cell $iR_{\vec e_x}$? This is the same question the minimal-coupling article leaves open for the current itself, and a positive answer here would be a positive answer there.

2. **The massless spinor-helicity form.** In the massless case the spin term is a curl and the transport term is an energy-weighted derivative. Does the biquaternion algebra, whose two Peirce carriers, minimal left ideals here, are the two chiralities, write the massless decomposition more naturally than the four-component spinor does, and does the helix of a Weyl particle appear as an idempotent of $\mathbb{M}_+$?

3. **The factor of two.** The $g = 2$ asymmetry between the current and the momentum density is a mismatch between two coefficients of the same bivector, one in the current and one in the momentum density. Is there an algebraic statement that fixes the factor of two, or is it one more coefficient the algebra transcribes?

4. **The Belinfante improvement in the framework's notation.** The passage from the canonical to the symmetric tensor is a shift by the divergence of an antisymmetric (spin) tensor. The corpus's Noether-theorem article gives the canonical currents; the biquaternion form of the improvement term, and of the spin part of the angular momentum, is not written.

5. **The exact energy-normalised form.** The identity is proved for $m\ne0$, and the massless section replaces $m$ by $E$ as a matter of scale. Whether the decomposition can be written with $E$ in every coefficient, without passing through the massive form, is not settled here; the natural test is a stationary superposition, where the spin bilinear varies in space and the energy is common.

6. **Berry's spin for light.** The electromagnetic analogue identifies the intrinsic spin density with a curl of an $E$–$B$ cross product. The framework's field-strength biquaternion and its Riemann–Silberstein partner are the natural place to test whether this spin is the same object as the photon's helicity in the framework.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5=-iL_{e_t}R_{\vec e_z} .
$$

These are the generator cells of the conventions under their usual names: $\gamma_\mu$ is $iL_{e_\mu}R_{\delta_\mu}$, and $\gamma_5$ is the chirality cell. The two spellings name one set of cells, and $\varepsilon_\mu\gamma_\mu=\gamma^\mu$ is the raised generator used in the contraction of the Dirac equation.

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

The reference-frame cell of the chirality operator is $\gamma_5$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

## Summary

The Gordon decomposition splits the on-shell Dirac current as

$$
\bar\psi\,\gamma_\mu\psi
= \frac{i}{2m}\left(\bar\psi\,\nabla_\mu\psi - \left(\nabla_\mu\bar\psi\right)\psi\right)
+ \frac{1}{m}\sum_\nu\varepsilon_\nu\,\nabla_\nu\left(\bar\psi\Sigma_{\mu\nu}\psi\right),
\qquad
\Sigma_{\mu\nu} = \tfrac{i}{4}\left[\gamma_\mu,\gamma_\nu\right] = \tfrac12\sigma_{\mu\nu},
$$

into a convection part and the divergence of a spin density. In momentum space it is

$$
\bar w(p_2)\,\gamma_\mu\,w(p)
= \bar w(p_2)\left[\frac{(p+p_2)_\mu}{2m}
+ \frac{i\sum_\nu\varepsilon_\nu\,\sigma_{\mu\nu}(p_2-p)_\nu}{2m}\right]w(p),
$$

where the first term is the current of a charged scalar and the second is the spin term whose coefficient gives $g = 2$. The decomposition requires $m \neq 0$ because both terms carry $1/m$; in the massless regime the energy $E$ replaces the mass as the scale of both terms, the spin term remains the curl $(e/m)\nabla\times\vec S$ of the spin density in the rest frame and $(e/E)\nabla\times\vec S$ in the massless one, and the locked Weyl moment $(e/E)(\hbar\vec u_k/2)$ is what remains of the Dirac moment when the rest frame is lost. The Belinfante–Rosenfeld tensor contains the same spin term with coefficient $\tfrac12$ in the momentum density, and the mismatch between that $\tfrac12$ and the current's $1$ is the angular-momentum face of $g = 2$. The axial companion is the same parent identity at $\Gamma=\gamma_\mu\gamma_5$, and there the transfer and the average momentum exchange their slots.

The biquaternion interpretation is a naming of the two structures: the split of the generator product is the split into the metric (central) direction and the bivector direction, so the convection current is central and the spin current is a bivector whose magnetic (rotation-type) part lies in the informational sector $\mathbb{M}_+$ and whose boost-type part lies in $\mathbb{M}_-$. The identity itself is a spinor-module statement, because the Dirac adjoint carries the Clifford-odd cell $iR_{\vec e_x}$ outside the left copy $\mathbb{B}_L$; the framework transcribes it, verifies its algebra and locates its two terms, and does not derive it from a product in the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\psi$, $\bar\psi = \psi^\dagger\gamma_0$ | Dirac spinor (spinor-module representative) and its adjoint, $\gamma_0 = iR_{\vec e_x}$ |
| $\gamma_\mu = iL_{e_\mu}R_{\delta_\mu}$, $L_{e_\mu}R_{\delta_\mu} = -i\gamma_\mu$ | The four generators, $\gamma_0 = iR_{\vec e_x}$ and $\gamma_k = iL_{\vec e_k}R_{\vec e_y}$, and the same cells with $i^2=-1$ applied |
| $\left\{\gamma_\mu,\gamma_\nu\right\} = 2g_{\mu\nu}L_{e_t}R_{e_t}$ | Clifford relations; metric $g = \mathrm{diag}(+1,-1,-1,-1)$ |
| $\gamma_5 = -iR_{\vec e_z} = -iL_{e_t}R_{\vec e_z}$, $\gamma_5^2 = L_{e_t}R_{e_t}$ | Chirality cell, anticommuting with every generator |
| $L_{a}R_{b}$, $L_{a}R_{b}\psi = a\psi b$ | Cell; $L_{e_t}R_{e_t}$ is the identity, $L_{a}R_{b}L_{c}R_{d} = L_{ac}R_{db}$ |
| $\nabla_\mu = \partial/\partial x_\mu$ | Derivative of the real frame $x_0 = ct'$, $x_k = q_k$; spinor covariant derivative on a curved background |
| $i\sum_\mu\varepsilon_\mu\gamma_\mu\nabla_\mu\psi = m\psi$ | Dirac equation on the module; equivalently $\sum_\mu\varepsilon_\mu L_{e_\mu}R_{\delta_\mu}\nabla_\mu\psi + m\psi = 0$ |
| $-i\sum_\mu\varepsilon_\mu\left(\nabla_\mu\bar\psi\right)\gamma_\mu = m\bar\psi$ | Adjoint equation; equivalently $\sum_\mu\varepsilon_\mu\left(\nabla_\mu\bar\psi\right)L_{e_\mu}R_{\delta_\mu} - m\bar\psi = 0$ |
| $\tilde\nabla\tilde\Psi_R = m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L = m\tilde\Psi_R$ | Chiral pair, the biquaternion form of the same equation |
| $\sigma_{\mu\nu} = \frac{i}{2}\left[\gamma_\mu,\gamma_\nu\right]$, $i\sigma_{\mu\nu} = \frac12\left[L_{e_\mu}R_{\delta_\mu},L_{e_\nu}R_{\delta_\nu}\right]$ | Bivector (magnetic) generator, and its real form; $\sigma_{0k} = iL_{\vec e_k}R_{\vec e_z}$ |
| $\Sigma_{\mu\nu} = \frac12\sigma_{\mu\nu} = \frac{i}{4}\left[\gamma_\mu,\gamma_\nu\right]$ | Spin generator of the Lorentz transformations; $\vec S = \left(\Sigma_{23},\Sigma_{31},\Sigma_{12}\right)$ |
| $\gamma_\mu\gamma_\nu = g_{\mu\nu}L_{e_t}R_{e_t} - i\sigma_{\mu\nu}$ | Symmetric/antisymmetric generator split |
| $j_\mu = \bar\psi\gamma_\mu\psi$, $j_0 = \psi^\dagger\psi$ | Number current and its density |
| $p$, $p_2$, $k = p_2-p$, $P = \frac12(p+p_2)$ | Momenta, transfer and average |
| $\sum_\rho\varepsilon_\rho\gamma_\rho p_\rho$ | Generators contracted with a momentum, the corpus form of the contraction |
| $\bar w_2\,\gamma_\mu w = \bar w_2\left[(p+p_2)_\mu + i\sum_\nu\varepsilon_\nu\sigma_{\mu\nu}k_\nu\right]w/2m$ | Momentum-space Gordon identity |
| $\vec S = \psi^\dagger S\psi$, $S = \frac12\mathrm{diag}(\boldsymbol\sigma,\boldsymbol\sigma)$ | Spin density and spin matrix |
| $T_{\mu\nu}^{\rm BR}$, $T_{\mu\nu}^{\rm canonical}$ | Belinfante–Rosenfeld and canonical stress tensors |
| $\frac{e\hbar}{2mc}\cdot\frac12\sum_{\mu,\nu}\varepsilon_\mu\varepsilon_\nu F_{\mu\nu}\bar\psi\sigma_{\mu\nu}\psi$ | Effective Pauli moment term ($g = 2$) |
| $\gamma_\mu$, $\gamma_5$ | The generator cells and the chirality cell under their usual names |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Informational and material sectors; bivector magnetic and boost parts |

## Further Reading

- W. Gordon, "Der Comptoneffekt nach der Schrödingerschen Theorie," *Zeitschrift für Physik* **40** (1926) 117–133, for the origin of the current decomposition.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the Gordon decomposition, the bilinears and the $1/2m$ coefficient of the spin current.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the vertex decomposition into $F_1$ and $F_2$, the Gordon identity and the Ward identity.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the form factors, the Gordon decomposition and the renormalisation of the vertex.
- L. H. Ryder, *Quantum Field Theory* (Cambridge, 2nd ed. 1996), for the Gordon decomposition and its use in the magnetic moment.
- M. V. Berry, "Optical currents," *Journal of Optics A: Pure and Applied Optics* **11** (2009) 094001, for the Gordon strategy applied to Maxwell's equations and the intrinsic spin density of light.
- F. J. Belinfante, "On the spin angular momentum of mesons," *Physica* **6** (1939) 887–898, and L. Rosenfeld, "Sur le tenseur d'impulsion-énergie," *Mémoires de l'Académie Royale de Belgique* **18** (1940) 1–30, for the symmetric stress tensor and the spin improvement.
- The companion articles of this series: [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html), [The Anomalous Magnetic Moment in Biquaternionic Form](the-anomalous-magnetic-moment-in-biquaternionic-form.html), [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), *The Classical Origin of $g = 2$ in Biquaternionic Form*, and [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html).
