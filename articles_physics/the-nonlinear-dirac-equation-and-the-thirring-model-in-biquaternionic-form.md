# __The Nonlinear Dirac Equation and the Thirring Model in Biquaternionic Form__

## Introduction

A **nonlinear Dirac equation** is a Dirac equation with a self-interaction term. The free equation is linear in the field, so that solutions superpose; a term built from the field itself destroys that superposability and makes the equation describe a fermion that acts on itself. The best-motivated case is geometric. In the **Einstein–Cartan–Sciama–Kibble** extension of general relativity, the spin of matter is the source of the antisymmetric part of the connection, the torsion; that torsion couples to the spinor's axial current, and when it is eliminated from the field equations it leaves an effective **axial-axial spin–spin self-interaction** that is cubic in the spinor. The resulting equation is the standard example of a nonlinearly self-interacting Dirac field, and it is a toy model for the idea that the fermion's self-interaction regulates its own short-distance behaviour.

Two models dominate the literature, and they fill the two channels other than the axial one. The **Thirring model** (Thirring 1958) is a $1+1$-dimensional theory whose interaction is the square of the vector current, contracted with the metric, $-\frac{g}{2}\sum_\mu\varepsilon_\mu V_\mu V_\mu$; it is exactly solvable and is the field-theory side of the bosonisation correspondence with the sine-Gordon model. The **Soler model** (Soler 1970) is a $3+1$-dimensional theory whose interaction is the square of the scalar bilinear, $\frac{g}{2}\left(\bar\psi\psi\right)^2$; it is the mean-field relative of the Nambu–Jona-Lasinio four-fermion interaction, and it is the model in which exact closed-form solutions have been found.

Here $V_\mu=\bar\psi\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\psi$, where $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ is the **generator cell** of the coordinate $x_\mu$, with $\nu(t)=x$ and $\nu(k)=y$, and $\varepsilon_\mu=g_{\mu\mu}$ is the signature sign, $+1$ on the time index and $-1$ on the three spatial ones in the $\mathbb{M}_-$ frame of the conventions article. The contraction is written as a sum because no index is summed silently in this corpus, and the sign on the time component is what makes $\sum_\mu\varepsilon_\mu V_\mu V_\mu$ a Lorentz scalar rather than a sum of squares.

This article states these equations, gives the Einstein–Cartan route that produces one of them from geometry, organises the possible interactions by the fermion bilinears they use, and gives the biquaternion interpretation. The framework's contribution is a **placement of the channels**: each quartic interaction is built from one of the local bilinears — the scalar density $S = \bar\psi\psi$, the vector current $V_\mu = \bar\psi\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\psi$, the axial current $A_\mu = \bar\psi\,c^{(5)}_\mu\psi$ — and each of these has a definite place in the framework's structure. $S$ is the mass channel, the object whose expectation is the dynamical mass of the companion article on the chiral condensate. $V_\mu$ is the material-sector current, the object of the companion articles on minimal coupling and on the Gordon decomposition. $A_\mu$ is the axial current, and the framework's linear mass is precisely what breaks its conservation; an axial-axial self-interaction is therefore a coupling in the channel conjugate to the mass. A quartic interaction is also **bosonic**: it is even in the fermion field and carries zero fermion number, so it passes through the framework's central phase untouched, which is why a self-interaction is compatible with the exact vector symmetry.

What the framework does **not** supply is equally definite, and follows from the minimal-coupling article. Every one of the bilinears above is a spinor-module object: the Dirac adjoint $\bar\psi = i\psi^\dagger L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ carries the Clifford-odd cell $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ — $L_{a}R_{b}$ is the two-sided multiplication, $L_{a}R_{b}\psi = a\psi b$ — and the axial cells are the generator cells times the chirality cell $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$; none of these is in the left copy $\mathbb{B}_L$, because each is a two-sided cell of $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$. The framework names the channels and places them in its sectors; it does not derive the self-interaction from a product in the algebra, and it adds no solution, coupling or prediction of its own.

The article is organised as follows. The next section fixes the cells and the two writings of the free equation. A section then explains why a self-interaction is cubic and how geometry produces one. A section states the Thirring and Soler models. A section writes the Hehl–Datta equation in cells and fixes its coefficient. A section lists the local bilinears and the channel each model uses. A section gives the biquaternion interpretation. A section records the two-dimensional relations verified here in exact arithmetic. A later section states the same objects in the matrix notation of the sources, so that the two can be compared term by term. The closing sections are the open questions, the summary, the notation table and the literature.

## The Cells and the Two Equations

The conventions are those of the companion articles. A two-sided multiplication is written once for all, $L_{a}R_{b}\psi = a\psi b$, with $L_{a}R_{b}L_{c}R_{d}=L_{ac}R_{db}$ and identity $L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$; the short form $iR_{\vec e_x}^{\mathrm{axf}}$ stands for $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$.

### The Generator Cells

The four cells $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ are the generators, and their squares are the squares of the units times $i^2 = -1$:

$$
\left(iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}\right)^2=i^2L_{e_t}^{\mathrm{axf}}R_{\vec e_x^2}^{\mathrm{axf}}=-L_{e_t}^{\mathrm{axf}}R_{-e_t}^{\mathrm{axf}}=+L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\qquad
\left(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\right)^2=i^2L_{\vec e_k^2}^{\mathrm{axf}}R_{\vec e_y^2}^{\mathrm{axf}}=(-1)\left(-L_{e_t}^{\mathrm{axf}}\right)\left(-R_{e_t}^{\mathrm{axf}}\right)=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}.
$$

So the timelike generator squares to $+L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ and the three spatial ones to $-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$. The timelike generator anticommutes with each spatial one, because the left factor $e_t$ contributes no sign while the right factors $\vec e_x$ and $\vec e_y$ anticommute. The whole set therefore satisfies

$$
\left\{iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},iL_{e_\rho}^{\mathrm{axf}}R_{\vec e_{\nu(\rho)}}^{\mathrm{axf}}\right\}=2g_{\mu\rho}L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
\qquad g=\mathrm{diag}(+1,-1,-1,-1).
$$

This is the sign the frame of the cells carries, the $\mathbb{M}_-$ frame of the conventions article. The interval reads the same numbers with the opposite overall sign, $g'=-g=(-1,+1,+1,+1)$, so that $s^2=g'_{\mu\nu}x^\mu x^\nu=-g_{\mu\nu}x^\mu x^\nu$; which of the two tuples is called $g$ is a convention, and no result depends on it.

### The Chirality and the Axial Cells

The chirality cell is $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, and its square is again $i^2$:

$$
\left(-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\right)^2=(-i)^2L_{e_t}^{\mathrm{axf}}R_{\vec e_z^2}^{\mathrm{axf}}=-L_{e_t}^{\mathrm{axf}}R_{-e_t}^{\mathrm{axf}}=+L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
$$

so the chirality is an involution of the cell algebra, and it anticommutes with each generator: the two imaginary factors multiply to $-i^2=+1$, and the units supply the minus, $\vec e_z\vec e_x=\vec e_y$ on one side against $\vec e_x\vec e_z=-\vec e_y$ on the other. The **axial cells** are the generators times the chirality cell,

$$
c^{(5)}_\mu:=\left(iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\right)\left(-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\right)=-i^2L_{e_\mu}^{\mathrm{axf}}R_{\vec e_z\vec e_{\nu(\mu)}}^{\mathrm{axf}}=+L_{e_\mu}^{\mathrm{axf}}R_{\vec e_z\vec e_{\nu(\mu)}}^{\mathrm{axf}},
$$

so that $c^{(5)}_0=L_{e_t}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ and $c^{(5)}_k=-L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$, on using $\vec e_z\vec e_x=\vec e_y$ and $\vec e_z\vec e_y=-\vec e_x$. One difference from the generators is worth recording: each axial cell is a generator cell times the chirality cell, so two of them anticommute to $-2g_{\mu\rho}$ rather than $+2g_{\mu\rho}$,

$$
\left\{c^{(5)}_\mu,c^{(5)}_\rho\right\}=-2g_{\mu\rho}L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
$$

and the axial cells generate the same Clifford algebra as the generators with the overall sign of the metric reversed. The Dirac adjoint is

$$
\bar\psi = i\psi^\dagger L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},
$$

and the cell $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ that it carries is what makes a bilinear a two-sided object.

### The Two Writings of the Free Equation

The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with $\vec e_k^2=-e_t$ and central imaginary $i$, and the free field obeys the linear, chirality-off-diagonal chiral pair

$$
\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L,
\qquad
\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R,
$$

in which the gradient acts by **left** multiplication on the field and the mass couples the two chiral halves; collected in the pair operator of the conventions article, this is the **one-sided** writing, with $\mathbb{D}^2=\Box I$ and $\Box=\sum_\mu\varepsilon_\mu\partial^2/\partial x_\mu^2=\partial^2/\partial t^2-\nabla^2$ in this frame. The **two-sided** writing is the cell operator $i\sum_\mu L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\partial/\partial x_\mu$ acting on the module, and it is the one this article needs, because every bilinear and every interaction below is a two-sided cell between $\bar\psi$ and $\psi$. The two writings describe one dynamics: each is first order, and each squares to the d'Alembertian, $\left(i\sum_\mu L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\partial/\partial x_\mu\right)^2=\Box\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, with the same $\Box$. The spinor equations used in the sections that follow are the representatives in which the literature models are defined. The biquaternionic transcription of each interaction is the open point, and the first item of *Open Questions* names it.

## Why the Dirac Equation Becomes Nonlinear

### Self-Interaction and the Cubic Form

The free Dirac equation is linear, and its solutions form a vector space. A self-interaction is a term built from the field itself. Lorentz covariance and the absence of derivatives leave only the local quartic combinations of the Lorentz-covariant bilinears, a finite set because the bilinears themselves are finite in number. A bilinear is quadratic in $\psi$, so a product of two bilinears is quartic in the field, and a quartic term of the Lagrangian varies into a term cubic in the field: varying one of the two bilinears leaves the other standing as the coefficient. Writing $B(\psi)$ for the bilinear built from the field, the equation keeps the shape

$$
\left(i\sum_\mu L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\partial/\partial x_\mu - m\right)\psi + B(\psi)\,\psi = 0,
$$

in which $B$ is quadratic in $\psi$ and the explicit field supplies the third power. The equation is nonlinear in the field and no worse than cubic: the word names the self-coupling, not a higher degree.

### The Einstein–Cartan Route

The reason the axial-axial channel is the physically motivated one is geometric, and it is worth stating because it removes the arbitrariness of the model-building. In Einstein–Cartan theory the affine connection is not required to be symmetric. Its antisymmetric part is the **torsion** $T_\mu{}_{\nu\lambda}$, and it is an independent variable in the action, sourced algebraically by the spin tensor of the matter. Because the torsion appears in the covariant derivative of a spinor through the spin connection, a Dirac field minimally coupled to a torsionful connection acquires a direct coupling between its spin (its axial current) and the torsion. Eliminating the torsion through its own algebraic field equation leaves an effective four-fermion term, the **Hehl–Datta interaction** (Hehl and Datta 1971), which is exactly an axial-axial spin–spin contact term. No new coupling constant is introduced; the strength is fixed by the gravitational constant, which is why the effect is unobservably small at ordinary densities and interesting only in the extreme.

## The Two Standard Models

### The Thirring Model

The Thirring model is defined in $1+1$ dimensions by the Lagrangian density

$$
\boxed{\;
\begin{aligned}
\mathcal{L} &= \bar\psi\,i\sum_\mu L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\partial \psi/\partial x_\mu - m\,\bar\psi\psi
- \frac{g}{2}\sum_\mu\varepsilon_\mu V_\mu V_\mu ,\\[4pt]
V_\mu &= \bar\psi\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\psi ,
\end{aligned}
\;}
$$

with $\psi=\left(\psi_+,\psi_-\right)$ a two-component spinor, one component per chirality, $g$ the coupling and $m$ the mass. The sums over $\mu$ run over $t$ and $x$ only, and the two-dimensional generator cells are $iR_{\vec e_x}^{\mathrm{axf}}=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ and $iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$. The kinetic part is the cell operator restricted to the two coordinates $t$ and $x$, and the mass term is the scalar density $\bar\psi\psi$, which in the one-sided reading is the off-diagonal pairing of the two chiral halves; the two writings are the two-sided and the one-sided form of one dynamics.

The quartic terms of the two-dimensional theory are not independent. The spinor has four real components, and the Fierz rearrangement identities of the two-dimensional Clifford algebra relate the quartic terms to one another. In particular the vector–vector and axial–axial combinations are the same operator up to sign, because the axial current is the two-dimensional Hodge dual of the vector current — the identity verified in exact arithmetic at the end of this article, where the two-dimensional chirality cell is the one the axial current of this model must use — so a single coupling $g$ covers the current–current model.

The **massless** Thirring model is exactly solvable: the multipoint correlation functions are known in closed form (Hagen; Klaiber), and the theory satisfies the Osterwalder–Schrader axioms, so it is a genuine quantum field theory and not merely a Lagrangian. The **massive** model is solvable by the Bethe ansatz, which gives the exact mass spectrum and scattering matrix; multi-particle production cancels on shell. The massive Thirring model is exactly equivalent to the quantum **sine-Gordon** model, with the fundamental fermions of the one corresponding to the solitons of the other — the Coleman–Mandelstam equivalence, which the companion article on bosonisation develops in the framework's notation.

### The Soler Model

The Soler model is defined in $3+1$ dimensions by

$$
\boxed{\;\mathcal{L} = \bar\psi\,i\sum_\mu L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\partial \psi/\partial x_\mu - m\,\bar\psi\psi
+ \frac{g}{2}\left(\bar\psi\psi\right)^2\;},
$$

with $\psi$ a four-component spinor and the sums over all four $\mu$: the generator cells are the four of the conventions above, $\nu(t)=x$ and $\nu(k)=y$. Its interaction is the square of the **scalar** bilinear, the same channel in which a fermion mass lives, and its sign convention makes a sufficiently strong coupling favour a nonzero $\langle\bar\psi\psi\rangle$. It is the single-particle relative of the Nambu–Jona-Lasinio model, in which the same quartic term is the interaction whose mean-field treatment produces a dynamical mass and a chiral condensate; the companion article on the chiral condensate owns the gap equation, the critical coupling and the Goldstone counting. A pseudoscalar variant replaces $S^2$ by $P_5^2$, the square of the parity-odd density of the bilinear table. The two belong together because the axial phase rotates $S$ into its partner: the companion article on the chiral condensate writes the rotation as multiplication by $\exp\left(2i\alpha\left(-iR_{\vec e_z}^{\mathrm{axf}}\right)\right)$, that is $S\mapsto\cos 2\alpha\,S+\sin 2\alpha\,P_5$, and reads the pair as a two-component order parameter. $S^2+P_5^2$ is the combination that rotation leaves fixed, which is why the pair of squares is the chirally invariant NJL interaction.

## The Hehl–Datta Interaction from Torsion

The geometric route of the earlier section gives the equation

$$
\boxed{\;\Big(i\sum_\mu L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\nabla_\mu - m\Big)\psi
+ \frac{3\kappa}{8}\sum_\mu\varepsilon_\mu A_\mu\,c^{(5)}_\mu\psi = 0\;},
$$

in which the kinetic operator is the cell operator of *The Cells and the Two Equations*, and its single factor $i$ multiplies the whole sum, so that

$$
i\sum_\mu L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\nabla_\mu\psi
=i\Big(\left(\nabla_t\psi\right)\vec e_x + \sum_k \vec e_k\left(\nabla_k\psi\right)\vec e_y\Big),
$$

the $t$ term being the right multiplication of $\nabla_t\psi$ by $\vec e_x$ and the three spatial terms the left multiplication of $\nabla_k\psi$ by $\vec e_k$ followed by the right multiplication by $\vec e_y$. The factor $i^2=-1$ enters one power later, not here: the sum without it squares to $-\Box L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, because the time cell squares to $+L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ and each spatial one to $-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, so the square of the operator as written is $+\Box L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$. Here $\nabla_\mu$ is the general-relativistic covariant derivative of a spinor, $\kappa = 8\pi G/c^4$ is the Einstein gravitational constant, and the interaction is the axial-axial contact term produced by the torsion of the spinor's own spin. The coefficient $3\kappa/8$ is fixed by the geometry, not chosen. Since $\kappa$ has the dimensions of an inverse mass squared and $A_\mu$ has those of a number density, the cubic term matches $m\psi$ only when $\kappa A_\mu\sim m$, that is at densities $\bar\psi\psi\sim m/\kappa\sim m\,M_P^2$ with $M_P$ the Planck mass — some forty orders of magnitude above nuclear density for a nucleon, so the interaction is a high-density effect and nothing else.

If the torsion is allowed to propagate rather than to be eliminated algebraically, the same nonlinear structure survives with the coefficient replaced by a term of magnitude $X^2/M^2$, with $X$ the spinor–torsion coupling and $M$ the torsion mass. The sign is the one the convention gives: with the natural sign the axial-axial interaction is **repulsive**, so it cannot by itself condense the field, and the scale is set by the torsion mass. The two routes — a non-propagating torsion fixed by gravity, and a propagating torsion with its own mass — therefore give the same axial-axial channel with different coefficients, which is the reason the channel is regarded as the generic one rather than a special choice.

## The Local Channels and Their Sectors

### The Bilinears

A single Dirac field has five types of local bilinear, classified by their Lorentz transformation:

| Bilinear | Name | Lorentz type | Behaviour under parity |
|---|---|---|---|
| $S = \bar\psi\psi$ | Scalar | scalar | even |
| $P_5 = \bar\psi\left(-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\right)\psi$ | Pseudoscalar | pseudoscalar | odd |
| $V_\mu = \bar\psi\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\psi$ | Vector (current) | four-vector | $V_0$ even, $V_k$ odd |
| $A_\mu = \bar\psi\,c^{(5)}_\mu\psi$ | Axial vector | four-vector | $A_0$ odd, $A_k$ even |
| $T_{\mu\nu} = \bar\psi\sigma_{\mu\nu}\psi$ | Tensor | antisymmetric rank 2 | $T_{0k}$ odd, $T_{jk}$ even |

The last column is the reason the axial vector is the parity partner of the vector: their time parts carry opposite parity, and so do their space parts. The two-dimensional form of the same statement is the Hodge duality verified at the end of the article. Each bilinear is quadratic in the field. The tensor entry is the antisymmetric product of two generator cells,

$$
\sigma_{\mu\rho} = \tfrac{i}{2}\left[iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}},iL_{e_\rho}^{\mathrm{axf}}R_{\vec e_{\nu(\rho)}}^{\mathrm{axf}}\right]
$$

acting between the adjoint and the field, with $\sigma_{0k}\psi = i\,\vec e_k\,\psi\,\vec e_z$ and $\sigma_{jk}\psi = i\,\vec e_j \vec e_k\,\psi$ for $j\ne k$, so that $\sigma_{0k}$ multiplies on both sides and $\sigma_{jk}$ on the left only, while $\sigma_{\mu\mu}=0$. A local quartic interaction without derivatives is a Lorentz-covariant product of two bilinears, and only a few combinations are independent because the Fierz identities relate them. The parity-odd entry is a density, and its representative in the cell dictionary is the quaternion $P=\bar\psi\,\psi\,\vec e_z$, the object that appears on the right of the axial divergence below. A Lagrangian term squares the densities and not the quaternions: the quaternion product squares the unit as well, $P\cdot P=S^2\vec e_z^2=-S^2$, so it carries the opposite sign and would cancel the scalar term instead of adding to it. What enters the interaction is the density square $P_5^2$.

### Which Channel Each Model Uses

| Model | Dimensions | Interaction | Channel | Framework home |
|---|---|---|---|---|
| Thirring | $1+1$ | $-\frac{g}{2}\sum_\mu\varepsilon_\mu V_\mu V_\mu$ | vector current | material sector $\mathbb{M}_-$ |
| Soler | $3+1$ | $+\frac{g}{2}\left(\bar\psi\psi\right)^2$ | scalar density | the mass channel |
| NJL / pseudoscalar variant | $3+1$ | $\frac{g}{2}\left(S^2 + P_5^2\right)$ | scalar–pseudoscalar | the mass channel, chirally paired |
| Hehl–Datta (torsion) | $3+1$ | $+\frac{3\kappa}{16}\sum_\mu\varepsilon_\mu A_\mu A_\mu$ | axial current | the axial channel |

The table is the article's organising object, and its entries are **Lagrangian** terms. The Hehl–Datta row is the one that has to be read carefully: varying $\tfrac{3\kappa}{16}\sum_\mu\varepsilon_\mu A_\mu A_\mu$ with respect to $\bar\psi$ gives $\tfrac{3\kappa}{8}\sum_\mu\varepsilon_\mu A_\mu\,c^{(5)}_\mu\psi$, the factor two coming from the two equal factors of the square, and $\tfrac{3\kappa}{8}$ is exactly the coefficient of the equation of the previous section. The Soler and NJL models act in the channel where the mass lives; the Thirring model acts in the channel where the current lives, which in two dimensions is the same channel as the axial one; the torsion-induced model acts in the axial channel, which is the channel the mass **breaks**.

## The Biquaternion Reading

### The Interaction Is Bosonic, So the Central Phase Passes Through It

A quartic product of two bilinears is even in the fermion field, so it carries fermion number zero and is invariant under the central phase $\tilde\Psi \mapsto \exp(i\alpha)\tilde\Psi$. It therefore does not disturb the exact vector $\mathrm{U}(1)$ the companion articles emphasise: the symmetry the mass breaks is the axial one, and the phase symmetry survives even a strong self-interaction. This is why a self-interaction can generate a mass dynamically without conflicting with the conservation of fermion number, and it is the part of the NJL mechanism that the symmetry statement covers.

### The Three Channels in the Framework's Sectors

The three channels of the table map onto three different structures the framework already carries, and the mapping is the article's main observation.

- **The scalar density $S$ is the mass channel.** The framework's mass term is the linear, chirality-off-diagonal pair $\tilde\nabla\tilde\Psi_R = m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L = m\tilde\Psi_R$. An interaction in the $S$ channel adds to that term, so the Soler and NJL models are, in the framework's terms, models in which the mass is allowed to be a function of the state rather than a fixed parameter. The companion article on the chiral condensate states the consequence: the condensate $\langle S\rangle$ is the order parameter and the self-consistent mass is the gap equation.
- **The vector current $V_\mu$ is the material-sector current.** The companion articles on minimal coupling and on the Gordon decomposition place the conserved current in $\mathbb{M}_-$, the material sector; the Thirring interaction is the square of that object. Its being the same channel as the axial one in two dimensions is the two-dimensional accident (the Hodge duality of the currents) that makes the Thirring model a one-coupling theory.
- **The axial current $A_\mu$ is the channel the mass breaks.** The linear mass breaks the axial symmetry and makes the axial current fail to be conserved: its divergence $\sum_\mu\varepsilon_\mu\,\partial A_\mu/\partial Q_\mu=2m\,\bar\psi\,\psi\,\vec e_z$ is $2m$ times the pseudoscalar bilinear, the quaternion representative $P$ of the density $P_5$ of the table, so the axial charge is not conserved once the mass is nonzero. The right-hand side carries no $i$, and that is a cancellation worth noting: the axial current carries one $i$ through the generator cell and the chirality cell supplies the other, $i\cdot(-i)=+1$, so the two factors of $i$ annihilate and the divergence is real. The torsion-induced interaction is built from $A_\mu$ directly. A coupling there therefore acts in the channel whose conserved charge the mass destroys, the channel conjugate to the mass. It is not the channel in which a condensate forms: the interaction the geometry supplies is repulsive, and the dynamical mass of the companion article is generated in the scalar channel, where the mass term itself lives.

### What the Framework Does Not Supply

The identification above is a placement, not a derivation, and the boundary should be stated in the same terms as the companion articles. Each bilinear in the table is a spinor-module object. The scalar and vector bilinears require the Clifford-odd cell $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ of the Dirac adjoint; the pseudoscalar and axial bilinears require the chirality cell $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ as well; neither cell lies in the left copy $\mathbb{B}_L \cong \mathbb{C}\ell_{1,3}^+$. The consequence is the one recorded in the minimal-coupling article: a bilinear built only from $\tilde\Psi$ and $\tilde\Psi^{*}$ inside $\mathbb{B}$ cannot supply these objects, and the self-interaction, like the current, is irreducibly a spinor-module statement. The framework transcribes the models, verifies the two-dimensional algebra of their channels, and locates each channel in its sectors. It supplies no coupling, no solution, no spectrum, and no prediction.

Two further limits are inherited from other gaps. The Einstein–Cartan route needs a torsionful connection with a field equation; the companion article on curved spacetime records that the framework can carry the connection as an object of its own Lie subspace but generates no dynamics for it, so a biquaternion torsion is in that agenda and not in the constructed part. And the exact solubility of the massless Thirring model is a property of two-dimensional quantum field theory with no biquaternion counterpart: the framework can write the two-component reduction in its own cells, and it does not reproduce the solution.

## Verified Two-Dimensional Relations

The two-dimensional identities on which the Thirring model's one coupling rests were checked directly, in exact arithmetic on the cell algebra over the Gaussian integers, so every residual below is exactly $0$ and not merely small. The frame is the $\mathbb{M}_-$ frame of the conventions article, $g=\mathrm{diag}(+1,-1)$: the generators are the cells $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ and $iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, and the two-dimensional chirality is their product, the cell $L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$.

### The Clifford Relations

The two generators form the two-dimensional Clifford algebra, and their product is the chirality:

$$
\left(iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}\right)^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\qquad
\left(iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\right)^2=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\qquad
\left\{iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\right\}=0,\qquad
iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}\,iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},\qquad
\left(L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\right)^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}.
$$

### The Current Duality

The axial current of the two-dimensional theory is built with the two-dimensional chirality, $A_\mu=\bar\psi\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\,\chi_{\mathrm{2D}}\,\psi$ with $\chi_{\mathrm{2D}}=L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, and not with the four-dimensional cell $c^{(5)}_\mu$ of the earlier section, which is built from the chirality of four dimensions: the chirality cell is a property of the dimension, so each dimension uses its own. With $\chi_{\mathrm{2D}}$ the duality is an identity of cells, with no free constant:

$$
A_0=V_1,\qquad A_1=V_0 ,
\qquad\text{that is}\qquad
A_\mu=\sum_\nu\epsilon_{\mu\nu}\varepsilon_\nu V_\nu ,
$$

with $\epsilon^{01}=+1$, hence $\epsilon_{01}=-1$. The signature sign on the summed index is part of the statement, because $\epsilon_{\mu\nu}\varepsilon_\nu$ is what the dual of a covector carries.

### The Single Coupling

Consequently

$$
\sum_\mu\varepsilon_\mu A_\mu A_\mu=\varepsilon_0A_0^2+\varepsilon_1A_1^2=V_1^2-V_0^2=-\left(V_0^2-V_1^2\right)=-\sum_\mu\varepsilon_\mu V_\mu V_\mu ,
$$

so the vector–vector and axial–axial quartic terms differ only by sign and a single coupling covers the current–current interactions. The plain sums of squares are equal instead, $A_0^2+A_1^2=V_0^2+V_1^2$, which is exactly why the signature signs cannot be dropped: without them the two invariants would coincide rather than being opposite. No cross term mixes the two currents either, but the statement has to be made about numbers rather than about cells. Because $\epsilon_{\mu\nu}\varepsilon_\mu\varepsilon_\nu V_\nu V_\mu$ is antisymmetric in $\mu$ and $\nu$ while the product of two components is symmetric, $\sum_\mu\varepsilon_\mu A_\mu V_\mu=0$ once the currents are evaluated between $\bar\psi$ and $\psi$; the cells themselves anticommute, $\{V_0,V_1\}=0$, so the same contraction read as an operator is $2V_1V_0$ and not zero.

The duality is the exact reason the two-dimensional model has one coupling, and it is a property of the Clifford algebra and not of the framework.

## Open Questions

1. **A biquaternion-natural self-interaction.** Is there a functional of $\mathbb{B}$-valued bilinears whose variation reproduces the Soler or Thirring interaction without the Clifford-odd adjoint cell and the chirality cell? This is the question of the minimal-coupling article met from the interaction side. The pseudoscalar square of the NJL combination belongs to the same question: the quaternion $P=\bar\psi\,\psi\,\vec e_z$ squares to $-S^2$, so the parity-odd density $P_5$ and an invariant built from two quaternions are not the same object, and no biquaternion form of $S^2+P_5^2$ is written here.

2. **Torsion in the framework's own notation.** The curved-spacetime article carries the connection in the Lie subspace but gives it no equation. The antisymmetric (torsion) part of that connection, and the algebraic elimination that produces the Hehl–Datta term, are not written in the framework's notation.

3. **The condensate and the nonlinear equation.** A strong coupling in the scalar channel generates a mass; the axial channel, where the geometry puts its interaction, is repulsive and does not condense on its own. Is the biquaternion form of the self-consistent (gap) equation the same statement as the framework's linear mass term with $m$ promoted to an expectation, and can the two be written as one equation?

4. **Two dimensions and the central charge.** The bosonisation article matches the central charges $c_{\mathrm{Dirac}} = 1 = c_{\mathrm{boson}}$. Does the nonlinear (massive Thirring) case add a biquaternion statement about the interacting central charge, or is it entirely the bosonic side's renormalisation?

5. **The exact solutions.** Closed-form solutions of the Soler model exist, and the massive Thirring model is Bethe-ansatz solvable. Neither has been transcribed into the framework's notation, and it is not known whether the biquaternion form of the equations makes either more transparent.

## The Gamma Formulation

This section writes the same cells in the $\gamma$ notation, so that each formula the sources state can be checked against the cell it names. The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$.

$$
\begin{aligned}
\gamma_0 &= iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}, &\gamma_1 &= iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\\[2pt]
\gamma_2 &= iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}, &\gamma_3 &= iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\\[2pt]
\gamma_5 &= -iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
\end{aligned}
$$

The same in the axis-free display:

$$
\begin{aligned}
\gamma_0 &= iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}, &\gamma_1 &= iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\\[2pt]
\gamma_2 &= iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}, &\gamma_3 &= iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\\[2pt]
\gamma_5 &= -iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}.
\end{aligned}
$$

A single product $L_{a}R_{b}$ is a pure tensor $a\otimes b$; the single products form a seven-dimensional cone, of rank at most one, and a general element of the algebra is a sum of at most four of them.

The axial cells are the products of a generator and the chirality cell: $c^{(5)}_\mu=\gamma_\mu\gamma_5$, since $L_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}\cdot L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=L_{e_t}^{\mathrm{pau}}R_{\vec e_z\vec e_x}^{\mathrm{pau}}=L_{e_t}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ is exactly $c^{(5)}_0$, and the three spatial products agree the same way. That is the dictionary entry the sources need: the Hehl–Datta term of this article **is** the $\left(\bar\psi\gamma_\mu\gamma_5\psi\right)\gamma^\mu\gamma_5\psi$ of the torsion literature.

$\gamma_5$ is the reference-frame cell of the chirality operator; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The cell dictionary is complex-linear. With the central $i$ dropped, the four cells are real $4\times4$ matrices, and they square to $-g=(-1,+1,+1,+1)$: the timelike one to $-I_4$ and the three spacelike ones to $+I_4$. They span the full algebra $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$ of real $4\times4$ matrices. Restoring the $i$ flips every square, because $i^2=-1$, and the cells then square to $+g$ and span $M_4(\mathbb{C})\cong\mathrm{Cl}_{1,3}(\mathbb{C})$, which is the algebra the $\gamma$ notation uses. The whole difference between the real and the complex reading is that single factor of $-1$.

### The Identities the Sources Cite

The identities the literature quotes were written in the $\gamma$ notation, and they are recorded once here, in that notation, so that each can be checked against the sources. In the $\gamma$ reading, with $\epsilon_{0123}=+1$:

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

The weight $\varepsilon_\mu$ in the contractions below is exactly what raises the index, $\gamma^\mu=\varepsilon_\mu\gamma_\mu$, so the Hehl–Datta sum $\sum_\mu\varepsilon_\mu A_\mu c^{(5)}_\mu$ is the sources' $A_\mu\gamma^\mu\gamma_5$ with the sum written out.

$S_{cd}=\tfrac14[\gamma_c,\gamma_d]$ is the Lorentz generator in the $\gamma$ basis, and the $\sigma_{\mu\nu}$ of the bilinear table is the same generator rescaled, $\sigma_{\mu\nu}=\tfrac i2[\gamma_\mu,\gamma_\nu]=2iS_{\mu\nu}$; the factor $2i$ is the whole difference between the two, and it is a convention.

### The Four Contraction Sums

A cell's square is a frame statement, and every contraction of the frame inherits that. Written with the signature sign $\varepsilon_\mu$ on the summed index, the way every other contraction in this article is written, the four sums hold in either frame:

$$
\sum_\mu\varepsilon_\mu\gamma_\mu\gamma_\mu=4I_4,\qquad
\sum_\mu\varepsilon_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,\qquad
\sum_\mu\varepsilon_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4g_{\alpha\beta}I_4,\qquad
\sum_\mu\varepsilon_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\gamma\gamma_\mu=-2\gamma_\gamma\gamma_\beta\gamma_\alpha ,
$$

In each of the four the contracted generator is the same one on both sides, so it is never moved past another generator and no reordering sign enters. In the $\mathbb{B}$ frame, where every cell squares to $+I_4$ and $\varepsilon_\mu=+1$, the weights drop out and the sums read $4I_4$, $-2\gamma_\alpha$, $4\delta_{\alpha\beta}I_4$ and $-2\gamma_\gamma\gamma_\beta\gamma_\alpha$. In the $\mathbb{M}_-$ frame the weights are what keep the shape: without them the first sum is $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$, and the second is $4\gamma_\alpha$ on the time index and $0$ on each spatial one, so the unweighted form is a frame accident and not an identity.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

A nonlinear Dirac equation adds a self-interaction built from the field's bilinears to the free equation. The physically motivated case is geometric: in Einstein–Cartan theory the torsion sourced by the spinor's own spin, eliminated through its field equation, leaves the axial-axial Hehl–Datta term $\frac{3\kappa}{8}\sum_\mu\varepsilon_\mu A_\mu\,c^{(5)}_\mu\psi$ with a coefficient fixed by the gravitational constant. The two standard models use the other two channels: the Thirring model in $1+1$ dimensions uses the square of the vector current and is exactly solvable, with the massive case equivalent to sine-Gordon; the Soler model in $3+1$ dimensions uses the square of the scalar bilinear and is the mean-field relative of the NJL interaction.

The biquaternion interpretation places the channels. The scalar density is the mass channel, whose expectation is the dynamical mass of the chiral-condensate article. The vector current is the material-sector current of the minimal-coupling and Gordon articles. The axial current is the channel the linear mass breaks, so an axial-axial interaction couples in the channel conjugate to the mass; the interaction the geometry supplies is repulsive, and the dynamical mass itself is generated in the scalar channel, where the mass term lives. Every quartic interaction is bosonic, so it passes through the framework's central phase and leaves the exact vector symmetry intact. Each bilinear, however, requires the Clifford-odd adjoint cell $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$, and the pseudoscalar and axial ones the chirality cell $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ as well, neither of which is in the left copy $\mathbb{B}_L$; the framework transcribes the models and locates their channels, and supplies no coupling, solution or prediction. The one exact algebraic fact about the models that the article verifies is two-dimensional: the axial current is the Hodge dual of the vector current, so $\sum_\mu\varepsilon_\mu A_\mu A_\mu=-\sum_\mu\varepsilon_\mu V_\mu V_\mu$ and the Thirring model has a single coupling.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra; $\vec e_k^2 = -e_t$, central $i$ |
| $L_{a}R_{b}$, $L_{a}R_{b}\psi = a\psi b$ | Two-sided cell; $L_{a}R_{b}L_{c}R_{d} = L_{ac}R_{db}$, identity $L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ | Generator cells: $iR_{\vec e_x}^{\mathrm{axf}} = iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$, $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ |
| $i\sum_\mu L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\partial/\partial x_\mu$ | Cell operator of the Dirac equation; its square is $\Box\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, since $i^2=-1$ |
| $c^{(5)}_\mu$ | Axial cells: $c^{(5)}_0 = L_{e_t}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $c^{(5)}_k = -L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ |
| $\bar\psi = i\psi^\dagger L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ | Dirac adjoint (carries the Clifford-odd cell $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$) |
| $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell; its square is the identity cell $L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $S = \bar\psi\psi$ | Scalar density (mass channel) |
| $P_5$, $P=\bar\psi\,\psi\,\vec e_z$ | Pseudoscalar density, the parity-odd partner of $S$; $P$ is its quaternion representative, whose quaternion square $P\cdot P=-S^2$ is a different object from the density square $P_5^2$ |
| $V_\mu = \bar\psi\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\psi$ | Vector current (material sector in the framework) |
| $A_\mu = \bar\psi\,c^{(5)}_\mu\psi$ | Axial current (channel broken by the mass); in two dimensions built with $\chi_{\mathrm{2D}}$ |
| $\chi_{\mathrm{2D}} = L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell of two dimensions, the product of the two generators |
| $\sum_\mu\varepsilon_\mu J_\mu K_\mu$ | Metric contraction of two currents |
| $T_{\mu\nu} = \bar\psi\sigma_{\mu\nu}\psi$ | Tensor bilinear; $\sigma_{0k}\psi = i \vec e_k\psi \vec e_z$, $\sigma_{jk}\psi = i \vec e_j \vec e_k\psi$ for $j\ne k$, and $\sigma_{\mu\mu}=0$ |
| $\sigma_{\mu\nu}$, $S_{cd}$ | Generators of the Lorentz algebra, $\sigma_{\mu\nu}=2iS_{\mu\nu}$; their commutator form is in *The Gamma Formulation* |
| $\varepsilon_\mu = g_{\mu\mu}$ | Signature sign of the index $\mu$ |
| $g$ | Self-coupling of the Thirring and Soler models |
| $\kappa = 8\pi G/c^4$ | Einstein gravitational constant |
| $\frac{3\kappa}{8}\sum_\mu\varepsilon_\mu A_\mu\,c^{(5)}_\mu\psi$ | Hehl–Datta term in the equation ($\frac{3\kappa}{16}\sum_\mu\varepsilon_\mu A_\mu A_\mu$ as a Lagrangian term) |
| $X$, $M$ | Spinor–torsion coupling and torsion mass (propagating-torsion case) |
| $\sum_\mu\varepsilon_\mu A_\mu A_\mu = -\sum_\mu\varepsilon_\mu V_\mu V_\mu$ | Two-dimensional current duality (verified exactly) |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Informational and material sectors |

## Further Reading

- W. E. Thirring, "A soluble relativistic field theory," *Annals of Physics* **3** (1958) 91–112, for the original two-dimensional model.
- M. Soler, "Classical, stable, nonlinear spinor field with positive rest energy," *Physical Review D* **1** (1970) 2760–2765, for the scalar-interaction model in four dimensions.
- F. W. Hehl and B. K. Datta, "Nonlinear spinor equation and asymmetric connection in general relativity," *Journal of Mathematical Physics* **12** (1971) 1334–1339, for the torsion-induced axial-axial interaction.
- F. W. Hehl, P. von der Heyde, G. D. Kerlick and J. M. Nester, "General relativity with spin and torsion: foundations and prospects," *Reviews of Modern Physics* **48** (1976) 393–416, for the Einstein–Cartan–Sciama–Kibble theory and its matter couplings.
- S. Coleman, "Quantum sine-Gordon equation as the massive Thirring model," *Physical Review D* **11** (1975) 2088–2097, for the equivalence of the massive Thirring and sine-Gordon models.
- C. R. Hagen, "Quantum sine-Gordon equation and the Thirring model," and B. Klaiber, "The Thirring model," in *Lectures in Theoretical Physics* (Gordon and Breach, 1968), for the exact solution of the massless model.
- Y. Nambu and G. Jona-Lasinio, "Dynamical model of elementary particles based on an analogy with superconductivity," *Physical Review* **122** (1961) 345–358, for the four-fermion interaction whose mean field gives a dynamical mass.
- L. H. Ryder, *Quantum Field Theory* (Cambridge, 2nd ed. 1996), and W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 2000), for the nonlinear spinor equations and their soliton-like solutions.
- The companion articles of this series: [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](the-gordon-decomposition-of-the-dirac-current-in-biquaternionic-form.html), [The Chiral Condensate and Dynamical Symmetry Breaking in Biquaternionic Form](the-chiral-condensate-and-dynamical-symmetry-breaking-in-biquaternionic-form.html), [Bosonization in Biquaternionic Form](bosonization-in-biquaternionic-form.html), and [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html).
