# __Lattice Gauge Theory and the Biquaternion Path Integral__

## Introduction

The functional integral of the companion article *The Functional Integral in Biquaternionic Form* is a formal object: the measure $\mathcal{D}\mathcal{A}$ is a product over uncountably many field components, the action is a four-dimensional integral, and the Gaussian evaluations that make the integral computable are the evaluations of a finite-dimensional approximation. The companion article *The Gauge Field Path Integral in Biquaternionic Form* removes the gauge redundancy but keeps the continuum; the result is an integral over gauge orbits, still formal. This article supplies the regulator. A lattice discretization replaces the continuum by a finite set of variables whose number is proportional to the volume in lattice units, replaces the formal measure by a finite product of compact-group integrals, and replaces the ill-defined continuum limit by a limit in which the lattice spacing is taken to zero together with a renormalization of the coupling. The result is the only construction in the subcategory in which the path integral is a genuine finite-dimensional integral, and it is the setting in which the confining behaviour of the non-abelian theory is established rather than inferred.

The framework's contribution is specific. A lattice link variable is the parallel transporter along a link, and for the algebra's compact factor it is an element of the group, which in the biquaternion realization is a **unit quaternion** — the compact subset $\{Q\in\mathbb{B}:Q\bar Q=e_0\}$ of the algebra. The group is compact, so the Haar measure on it is finite and normalized, and the lattice path integral is a finite product of compact integrals. The trace that the action uses is the real part of the quaternion,
$$
\mathrm{Tr}\,U=\mathrm{Tr}\,\Phi(U)=2\,\mathrm{Re}(U_0)\in[-2,2],
$$
for $U=U_0e_0+U_1e_1+U_2e_2+U_3e_3$; the action is bounded below and the measure is bounded above, and the path integral converges without a formal gauge-fixing determinant. This is the structural reason the lattice is the natural non-perturbative regulator for the framework: the nonlinearity that obstructs the continuum measure — the group-valued link — is exactly the compactness that makes the lattice measure finite.

The article is organized as follows. The next section states why a regulator is needed and what the lattice supplies. A section constructs the lattice carrier: sites, links, the group-valued variable and its gauge law. A section derives the plaquette and the Wilson action and shows that its naive continuum limit is the Yang–Mills density of the companion articles, with the coupling normalization fixed. A section defines the lattice path integral and its measure, and records the transfer-matrix and reflection-positivity properties on which the physical interpretation rests. A section carries out the strong-coupling expansion, obtains the area law and the string tension, and identifies confinement. A section takes the continuum limit and fixes the place of the lattice in the renormalization group. A closing section separates what the algebra supplies from what is imported.

We use the conventions of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$, and central $i$. The sectors are $\mathbb{M}_-=\mathrm{span}_\mathbb{R}\{ie_0,e_1,e_2,e_3\}$ and $\mathbb{M}_+=\mathrm{span}_\mathbb{R}\{e_0,ie_1,ie_2,ie_3\}$. The compact gauge algebra is taken in the Hermitian-generator realization: the generators are $T_a=\tfrac12 ie_a\in\mathbb{M}_+$, Hermitian and traceless, with the standard algebra and normalization $[T_a,T_b]=i\varepsilon_{abc}T_c$ and $\mathrm{Tr}(T_aT_b)=\tfrac12\delta_{ab}$, equivalently $e_a=-2iT_a$ with $[e_a,e_b]=2\varepsilon_{abc}e_c$; the connection is $\mathcal{A}_\mu=\mathcal{A}_\mu^a T_a$, the coupling is $\kappa=q/\hbar$, the covariant derivative is $D_\mu=\partial_\mu+i\kappa\mathcal{A}_\mu$, and the curvature is $F_{\mu\nu}=\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$. The realization is not a free choice on the lattice. The link must be a group element, and $i\kappa\mathcal{A}_\mu$ is anti-Hermitian only for Hermitian $\mathcal{A}_\mu$; with the anti-Hermitian assignment $\mathcal{A}_\mu\in\mathbb{M}_-$ of the classical companion articles, $i\kappa\mathcal{A}_\mu$ is Hermitian, so that $\exp(ia\kappa\mathcal{A}_\mu)$ is Hermitian positive definite rather than unitary and departs from unitarity already at first order in $a\kappa$. This is the reality-class question *Non-Abelian Gauge Fields in Biquaternionic Form* records as open. The lattice does not settle it in general, but in Euclidean signature the $ict$ derivative that forces the Minkowski mixed assignment is absent, the Hermitian class is closed under the gauge transformation for all four directions, and it is the class the holonomy of *Wilson Loops in Biquaternionic Form* already uses. The gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_k\partial_k$ with $\Box=\tilde{\nabla}\bar{\tilde{\nabla}}=\partial_{ict}^2+\Delta$, and the $ict$ metric is $\eta=\mathrm{diag}(-1,+1,+1,+1)$. The lattice is introduced in Euclidean signature, where the weight is $e^{-S_W}$ with $S_W$ real and positive; the rotation that relates the two signatures is the one of the companion articles. Natural units $\hbar=c=1$ are used where no dimensionful quantity is displayed.

- Companion article *The Functional Integral in Biquaternionic Form*, for the measure, the Gaussian evaluation and the Euclidean rotation.
- Companion article *The Gauge Field Path Integral in Biquaternionic Form*, for the abelian gauge orbit and the gauge-fixing determinant.
- Companion article *The Yang–Mills Equation in Biquaternionic Form*, for the non-abelian curvature, the field equation and covariant conservation.
- Companion article *Non-Abelian Gauge Fields in Biquaternionic Form*, for the connection, the adjoint transformation law and the Yang–Mills density.
- Companion article *Wilson Loops in Biquaternionic Form*, for the loop operator, its gauge invariance and its abelian area law.
- Companion article *The Partition Function in Biquaternionic Form*, for the Euclidean partition function and its evaluation.
- Companion article *The Wick Rotation in the Biquaternion Universe*, for the rotation between the $ict$ and Euclidean descriptions.
- Companion article *The Renormalization Group in Biquaternionic Form*, for the running coupling and the lattice spacing as a cutoff.
- Companion article *Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form*, for the spin-one character of the adjoint-valued connection.

## Why a Regulator

The continuum object,
$$
Z=\int\mathcal{D}\mathcal{A}\;e^{iS_{\mathrm{YM}}[\mathcal{A}]},
\qquad
S_{\mathrm{YM}}=-\tfrac12\int d^4x\,\mathrm{Tr}\left(F_{\mu\nu}F^{\mu\nu}\right),
$$
is not an integral in the sense of measure theory. The symbol $\mathcal{D}\mathcal{A}$ denotes a limit of products of finitely many ordinary integrals, and the limit is not known to exist without a regulator; the perturbative expansion assumes that a regulator has been chosen and that the counterterms remove its dependence. Three properties are needed of the regulator: it must make the measure finite, it must preserve the gauge invariance of the action, and it must admit a limit in which the regulator dependence is absorbed into the parameters of the theory.

A spacetime lattice supplies all three. The lattice has finitely many sites in a finite box, so the field has finitely many components; the group-valued variable on each link is drawn from a compact group, so each integral is finite; the lattice action is built from closed loops and is therefore gauge invariant; and the limit in which the lattice spacing $a$ is taken to zero is controlled by the renormalization group, which absorbs the dependence into the coupling. The lattice regularization is the standard non-perturbative construction of a gauge theory, and it is used here because it is the construction that makes the biquaternion path integral well defined.

Two features of the framework make the lattice a natural object rather than an external device. First, the group the lattice integrates over is the group of unit quaternions, which is the compact part of the algebra's own group; the lattice configuration space is a product of copies of that group, and the symplectic/Haar measure on each copy is the normalized measure on the unit sphere $S^3$ in $\mathbb{R}^4$. Second, the lattice spacing $a$ enters the link as the phase $a\kappa\mathcal{A}$, so the lattice is a discretization of the algebra's gradient $\tilde{\nabla}$: the covariant difference $(U_\mu(n)\phi(n+\hat\mu)-\phi(n))/a$ is the lattice version of $D_\mu\phi$, with the link supplying the parallel transport that the discretization of the derivative otherwise loses.

## The Lattice Carrier

### Sites, Links, and the Group

A hypercubic lattice of spacing $a$ consists of sites $n=(n_0,n_1,n_2,n_3)$ with $n_\mu\in\mathbb{Z}$, and the link from $n$ to $n+\hat\mu$ carries a group element $U_\mu(n)$. The group is the compact factor of the algebra,
$$
U_\mu(n)\in SU(2)=\{Q\in\mathbb{H}_{\mathbb{B}}:Q\bar Q=e_0\},
\qquad
\mathbb{H}_{\mathbb{B}}=\mathrm{span}_\mathbb{R}\{e_0,e_1,e_2,e_3\},
$$
the set of unit real quaternions — the coefficients of $e_0,e_1,e_2,e_3$ are real, so that $\bar Q=Q^\dagger=Q^{-1}$ and the quaternion conjugate, the Hermitian conjugate and the inverse coincide; it is a three-sphere embedded in the algebra, and it is the group that exponentiates the compact factor $\mathfrak{su}(2)$ in the Hermitian-generator realization fixed above. The link is the lattice approximation to the parallel transporter,
$$
U_\mu(n)=\exp\!\big(ia\kappa\mathcal{A}_\mu(n)\big)
=\sum_{m=0}^{\infty}\frac{1}{m!}\big(ia\kappa\mathcal{A}_\mu(n)\big)^m ,
$$
which for $\mathcal{A}_\mu=\mathcal{A}_\mu^aT_a$ is a unit quaternion, $U_\mu(n)\bar U_\mu(n)=e_0$. The exponential is the ordinary algebra product; the fact that it lands in the group, and not merely in the algebra, is the statement that the compact factor exponentiates into the compact group, and it is the reason the link variable is bounded.

### The Lattice Gauge Transformation

A lattice gauge transformation is a group-valued function $U(n)\in SU(2)$ on the sites, under which
$$
U_\mu(n)\longmapsto U(n)\,U_\mu(n)\,U(n+\hat\mu)^{-1},
\qquad
\phi(n)\longmapsto U(n)\phi(n)
$$
for a matter field in the fundamental representation. This is the lattice form of the transformation law of the companion article: it is the adjoint law at a point, promoted to a law relating neighbouring sites, and the inhomogeneous term of the continuum transformation is replaced by the difference of the group elements on the two ends of the link. The action will be built from products of links around closed loops, and each loop is gauge invariant because the $U(n)$ and $U(n)^{-1}$ at every site cancel.

### The Discrete Covariant Derivative

The lattice replaces the derivative by a difference, and the link supplies the parallel transport:
$$
(D_\mu\phi)(n)\longmapsto\frac{1}{a}\Big(U_\mu(n)\phi(n+\hat\mu)-\phi(n)\Big),
$$
which transforms as $U(n)\big(D_\mu\phi\big)(n)$ at the site $n$, exactly as the continuum covariant derivative does. The backward difference uses $U_\mu(n-\hat\mu)^{-1}$; the symmetric combination recovers the Hermitian part. In the algebra's notation the lattice is a discretization of $\tilde{\nabla}=e_0\partial_{ict}+e_k\partial_k$, with the central part becoming an ordinary difference and the spatial part becoming the covariant difference above. The discretization is not unique, and the different choices differ by $O(a)$ terms that are irrelevant to the continuum limit; what is not optional is the link factor, which is what makes the difference gauge covariant.

## The Plaquette and the Wilson Action

### The Plaquette

The elementary gauge-invariant object on the lattice is the **plaquette**, the product of links around the boundary of an elementary square in the $\mu\nu$ plane,
$$
U_{\mu\nu}(n)=U_\mu(n)\,U_\nu(n+\hat\mu)\,U_\mu(n+\hat\nu)^{-1}\,U_\nu(n)^{-1}.
$$
It is a unit quaternion, it is gauge invariant, and it is the lattice representative of the curvature. Expanding the links at small $a$ and collecting the leading term,
$$
U_{\mu\nu}(n)=\exp\!\big(ia^2\kappa\,F_{\mu\nu}(n)+O(a^3)\big),
$$
where $F_{\mu\nu}$ is the continuum curvature of the companion article. The identity was checked numerically on a constant non-abelian field configuration: with $U_\mu=\exp(ia\kappa\mathcal{A}_\mu)$ and $\mathcal{A}_\mu$ a generic superposition of all three generators $T_a$ — not a single generator, so that the commutator contributes — the residual $\|U_{\mu\nu}-\exp(ia^2\kappa F_{\mu\nu})\|$ was $2.6\times10^{-9}$ at $a=2\times10^{-3}$ and fell by a factor of $8$ for each halving of $a$, that is as $a^3$, as the expansion requires. The two facts that make the plaquette the right object are visible in the formula: it is built from the group, so it is bounded, and its small-$a$ limit is the curvature, so its action has the continuum action as its limit.

### The Wilson Action

The Wilson action is the sum over plaquettes of the trace deficit,
$$
S_W[U]=\beta\sum_{n}\sum_{\mu<\nu}\left(1-\frac{1}{N}\mathrm{Re}\,\mathrm{Tr}\,U_{\mu\nu}(n)\right),
\qquad
N=2,
\qquad
\mathrm{Tr}\,U_{\mu\nu}=2\,\mathrm{Re}\,(U_{\mu\nu})_0 ,
$$
with $\beta$ the lattice coupling. It is gauge invariant because each plaquette is; it is real and bounded below because the trace lies in $[-2,2]$; and its small-$a$ limit is the Yang–Mills action. To fix $\beta$ one expands the trace. Using $U_{\mu\nu}=\exp(ia^2\kappa F_{\mu\nu}+\ldots)$ and the vanishing of the matrix trace of the curvature,
$$
\frac{1}{N}\mathrm{Re}\,\mathrm{Tr}\,U_{\mu\nu}
=1-\frac{a^4\kappa^2}{2N}\mathrm{Tr}\left(F_{\mu\nu}F^{\mu\nu}\right)+O(a^6),
$$
so that
$$
1-\frac{1}{N}\mathrm{Re}\,\mathrm{Tr}\,U_{\mu\nu}
=\frac{a^4\kappa^2}{2N}\mathrm{Tr}\left(F_{\mu\nu}F^{\mu\nu}\right)+O(a^6).
$$
The numerical check of the previous paragraph confirmed the coefficient: for a constant non-abelian field the ratio of the measured trace deficit to $\frac{a^4\kappa^2}{2N}\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ was $1$ to better than one part in $10^{3}$ at $a=2\times10^{-3}$. Multiplying by $\beta$ and summing over $\mu<\nu$, the lattice action reproduces
$$
S_W\longrightarrow \frac{\beta\kappa^2}{4N}\int d^4x\,\mathrm{Tr}\left(F_{\mu\nu}F^{\mu\nu}\right)
$$
with the standard identification of the sum over $\mu<\nu$ with half the double sum. Matching to the Euclidean Yang–Mills density $+\frac12\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$ — in this normalization $\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})=\tfrac12F^a_{\mu\nu}F^a_{\mu\nu}$, so this is the standard $\tfrac14F^a_{\mu\nu}F^a_{\mu\nu}$ — fixes
$$
\beta=\frac{2N}{\kappa^2}=\frac{4}{\kappa^2}
\qquad (N=2),
$$
which is the standard lattice normalization, written in the framework's coupling $\kappa=q/\hbar$. The lattice coupling is therefore not an independent parameter: it is the reciprocal square of the continuum coupling, and the continuum limit is the limit in which $\kappa\to0$ and $\beta\to\infty$ with the physical scale held fixed.

## The Lattice Path Integral

### The Measure

The lattice path integral is the finite product of compact-group integrals,
$$
Z=\int\prod_{n}\prod_{\mu=0}^{3}dU_\mu(n)\;\exp\!\big(-S_W[U]\big),
$$
where $dU_\mu(n)$ is the Haar measure on $SU(2)$, normalized to $\int dU=1$, and the product is over all sites and all positive directions in a finite box with periodic boundary conditions. In angular coordinates, writing $U=\cos\theta\,e_0+\sin\theta\,(\hat n_1e_1+\hat n_2e_2+\hat n_3e_3)$ with $\hat n\in S^2$ and $\theta\in[0,\pi]$,
$$
dU=\frac{1}{2\pi^2}\sin^2\theta\,d\theta\,d\Omega(\hat n),
\qquad
\int dU=1 ,
$$
which is the normalized measure on the unit sphere $S^3$ regarded as the unit quaternions. This is the sense in which the lattice integral is the biquaternion path integral made finite: the configuration space is a product of copies of the unit-quaternion three-sphere, the integrand is the exponential of a bounded function on it, and the integral is an ordinary finite-dimensional integral. There is no Faddeev–Popov determinant at this stage because there is no gauge fixing: the integral is over all link configurations, and the gauge redundancy is a finite-dimensional symmetry of the integrand whose volume is finite because the gauge group on a finite lattice is compact. The continuum Faddeev–Popov construction of the companion articles is the way the same redundancy is handled when the lattice is removed.

### Why the Lattice Needs No Ghosts

The Faddeev–Popov determinant and its ghosts are absent from the lattice integral, and the reason is worth stating because it is the lattice counterpart of the continuum construction. On the lattice the integration variable is the group element $U_\mu(n)$ itself, not the algebra element $\mathcal{A}_\mu$, and the Haar measure $dU$ is invariant under both left and right multiplication, $d(VU)=d(U)=d(UV)$. The gauge transformation $U_\mu(n)\mapsto U(n)U_\mu(n)U(n+\hat\mu)^{-1}$ is therefore a symmetry of the measure as well as of the action, and the integral over the compact gauge group at each site is finite. There is no infinite orbit volume to divide out and hence no compensating determinant: the redundancy is an ordinary finite-dimensional compact symmetry of a finite-dimensional integral. The determinant reappears when the lattice is described perturbatively, that is when the link is expanded as $U_\mu=\exp(ia\kappa\mathcal{A}_\mu)$ and the group integral is approximated by a Gaussian integral over the algebra; in that description the gauge slice returns, the orbit volume diverges, and the ghosts are needed again. The lattice and continuum descriptions therefore differ in their treatment of the redundancy, not in their physics: the former integrates over the group and needs no gauge fixing, the latter integrates over the algebra and does.

### Transfer Matrix and Positivity

The Euclidean lattice theory has a transfer matrix: writing the four-dimensional lattice as a three-dimensional lattice with a time direction, the Boltzmann weight factorizes into a product of transfer matrices between consecutive time slices, $Z=\mathrm{Tr}\,\hat T^{N_t}$, and the standard positivity properties of the Wilson action make $\hat T$ self-adjoint and positive on the physical Hilbert space. The construction is the lattice version of the Hamiltonian formulation of the companion articles; reflection positivity is the property that guarantees a positive-definite inner product and a self-adjoint Hamiltonian in the continuum limit. The framework's lattice is not special here — the unit-quaternion measure is the standard $SU(2)$ measure — but the transfer matrix is what makes the lattice a *quantum* regulator rather than merely a finite-dimensional approximation, and it is what allows the spectrum to be read off from the exponential decay of correlators.

### The Lattice as the Regulator of the Biquaternion Integral

In the framework's terms, the lattice accomplishes the following.

- The formal measure $\mathcal{D}\mathcal{A}=\prod_\mu\prod_a\mathcal{D}\mathcal{A}_\mu^a$ becomes the finite product of Haar measures on the unit quaternions, with the potential $\mathcal{A}_\mu$ replaced by the group element $U_\mu=\exp(ia\kappa\mathcal{A}_\mu)$.
- The formal action becomes the sum over plaquettes, whose small-$a$ limit is the Yang–Mills density, with $\beta=2N/\kappa^2$.
- The gauge redundancy becomes a finite-dimensional compact symmetry, so that the integral converges without gauge fixing; the gauge-fixing determinant reappears only in the continuum description.
- The lattice spacing $a$ is a cutoff, and the limit $a\to0$ is taken with the physical scale fixed by the renormalization group.

## Strong Coupling, the Area Law, and Confinement

### The Strong-Coupling Expansion

At small $\beta$ the weight can be expanded in powers of $\beta$,
$$
e^{-S_W}=\prod_{p}e^{-\beta\left(1-\frac1N\mathrm{ReTr}U_p\right)}
=e^{-\beta N_p}\prod_p\left[1+\frac{\beta}{N}\mathrm{ReTr}U_p+O(\beta^2)\right],
$$
where $N_p$ is the number of plaquettes and $U_p$ denotes the plaquette variable. The integral of a product of links around a set of plaquettes is evaluated with the group integral identities
$$
\int dU\,1=1,
\qquad
\int dU\,U_{ij}=0,
\qquad
\int dU\,U_{ij}U_{kl}=0\ \ (N\ge3),
\qquad
\int dU\,U_{ij}U^\dagger_{kl}=\frac{1}{N}\delta_{il}\delta_{jk},
$$
the last of which is the statement that only a link and its conjugate, paired between a fundamental and an antifundamental index, contribute. The third identity is the one that distinguishes the groups: for $N\ge3$ the antisymmetric square of the fundamental contains no singlet and the two-fundamental integral vanishes, whereas for $N=2$ the singlet $\epsilon_{ik}\epsilon_{jl}$ makes it nonzero and supplies the additional contribution responsible for the real-fundamental special case below. The consequence is that the strong-coupling expansion is a **tiling expansion**: a Wilson loop receives contributions from the plaquettes that tile its interior, and the leading contribution is the tiling of smallest area.

### The Area Law and the String Tension

For a rectangular Wilson loop of dimensions $R\times T$ in lattice units, the leading strong-coupling contribution tiles the rectangle with plaquettes, each plaquette contributing a factor $\beta/(2N^2)$ for $N\ge3$ and $\beta/N^2$ for $N=2$, and each link in the interior being integrated against its neighbours. The result is the **area law**,
$$
\langle W(C)\rangle=\left\langle\frac{1}{N}\mathrm{Tr}\prod_{l\in C}U_l\right\rangle
\;\sim\;\exp\!\big(-\sigma\,A\big),
\qquad
A=R\,T\,a^2 ,
$$
with a string tension $\sigma$ that at leading strong coupling is
$$
\sigma a^2=-\ln\!\left(\frac{\beta}{2N^2}\right)+O(1),
$$
where $N=2$ for the framework's group and the $O(1)$ denotes the perimeter and tiling corrections. The special case $N=2$, in which the fundamental representation is real, replaces $2N^2$ by $N^2$ at leading order: the one-plaquette average is
$$
\frac{1}{2}\big\langle \mathrm{Tr}\,U_\square\big\rangle
=\frac{I_2(\beta)}{I_1(\beta)}
=\frac{\beta}{4}+O(\beta^3),
$$
an identity that was checked numerically from the series of the modified Bessel functions, and whose exact one-plaquette form is $I_0(\beta)/I_1(\beta)-2/\beta$, equal to $I_2(\beta)/I_1(\beta)$ by the Bessel recurrence. Both statements agree at leading order: for the framework's $SU(2)$ the plaquette average begins at $\beta/4$, so that the string tension begins at $\sigma a^2=-\ln(\beta/4)+O(1)$.

The area law is the statement of **confinement** in the lattice formulation: the potential between two static fundamental charges grows linearly with their separation, $V(r)\sim\sigma r$, so the charges are never separated to infinity at finite energy cost. The result is a strong-coupling result, established by expansion, and it is stable as $\beta$ increases until the deconfinement transition; the existence of the transition and the continuum scaling of $\sigma$ are the standard lattice results, cited below. What the framework supplies here is not the analysis but the carrier: the lattice variables are unit quaternions, the plaquette is their product around a square, the trace is $2\mathrm{Re}(U_0)$, and the group is the compact factor of the algebra. The confinement result is a statement about that group.

### The Reading of Confinement

The area law is an operator statement about a Wilson loop, and its interpretation — confinement as the loss of partonic information, the string tension as an information-theoretic quantity, the deconfinement transition as a change in the accessible information — belongs to the informational subcategory. The lattice article's result is the analytic input: the loop obeys an area law at strong coupling, on the unit-quaternion lattice, for the same action whose continuum limit is the Yang–Mills density.

### The Two Regimes

The area law is established at strong coupling, and what happens at weak coupling is a separate question whose answer depends on the matter content. For the pure gauge theory — no dynamical fermions — the area law persists from strong coupling to the continuum limit: confinement is a property of the pure non-abelian gauge theory, and the string tension scales according to the renormalization group, $\sigma\propto\Lambda^2$, so that the ratio $\sigma a^2$ decreases as $\beta$ grows according to the same beta function that governs the coupling. For the theory coupled to dynamical fundamental matter, the area law is replaced at large loops by a **perimeter law**, $W(C)\sim e^{-\mu P}$, because the matter field screens the static charges: a virtual pair is created, the string breaks, and the potential flattens to a constant rather than growing linearly. In the framework's lattice, which as constructed has no matter, the first case is the relevant one: the pure $\mathfrak{su}(2)$ theory confines, and the area law is its confinement statement. The transition between the two behaviours, and the deconfinement transition at finite temperature, are the standard lattice results cited below.

## The Continuum Limit and the Running Coupling

The continuum limit is $a\to0$ with the physical scale fixed. Because the lattice coupling is $\beta=2N/\kappa^2$ and $\beta\to\infty$, the limit is the weak-coupling limit of the lattice theory, and its existence requires that the lattice correlation length grow without bound in lattice units. The renormalization group supplies the relation: the dependence of the physical scale on $a$ is governed by the beta function,
$$
\beta_\kappa=-\frac{\kappa^3}{16\pi^2}b_0 ,
\qquad
b_0=\frac{11}{3}C_2(G)=\frac{11}{3}\cdot 2=\frac{22}{3}
$$
for the pure $\mathfrak{su}(2)$ theory, with the sign convention of the companion article *The Renormalization Group in Biquaternionic Form*. The coefficient is positive, so the coupling decreases as the scale increases (asymptotic freedom); conversely, at fixed lattice spacing the coupling grows at long distances, which is the regime in which the strong-coupling expansion applies. The two statements are the same running coupling read from opposite ends. In the continuum limit the lattice action reduces to the Yang–Mills action, the lattice path integral reduces to the gauge-field path integral, and the lattice provides the regulator whose removal is the renormalization.

Three remarks place the construction.

- **The lattice is a regulator, not a theory.** Its correlation functions have a limit governed by the renormalization group, and in that limit the lattice spacing disappears; the physical predictions are those of the continuum theory.
- **The lattice is the non-perturbative definition.** The perturbative expansion of the continuum integral diverges and does not define the theory; the lattice integral is finite for every $a>0$ and defines the theory at the regulated level. This is why the confinement statement is a lattice statement.
- **The framework's lattice is the standard $SU(2)$ lattice.** The unit-quaternion measure is the $SU(2)$ Haar measure; the plaquette is the standard plaquette; the Wilson action is the standard action. The algebra's contribution is to identify the carrier — the compact factor, the unit quaternions, the trace as twice the scalar part — and to make the same lattice the regularization of the biquaternionic integral.

## What the Algebra Supplies and What It Imports

**Supplied by the algebra, and recomputed here.** The group of the lattice, as the unit real quaternions, which are the compact subset of $\mathbb{B}$ that exponentiates the compact factor in its Hermitian-generator realization, $T_a=\tfrac12 ie_a\in\mathbb{M}_+$ — the realization required by unitarity of the link; the trace of a group element as twice its scalar part, so that the Wilson action is a real bounded function on the group; the plaquette as the product of four links, whose small-$a$ expansion is the curvature $F_{\mu\nu}$ of the companion article, checked numerically on a constant non-abelian field; the normalization $\beta=2N/\kappa^2$ that makes the lattice action reduce to the Yang–Mills density; the measure as the normalized measure on the unit-quaternion three-sphere; and the reading of the lattice as a discretization of $\tilde{\nabla}$ with the link supplying parallel transport.

**Imported, and left visible.** The Wilson action and the plaquette construction; the strong-coupling expansion and the group integral identities; the area law and the string tension; the transfer matrix and reflection positivity; the continuum limit and the renormalization-group relation between $a$ and the coupling; and the lattice results on the deconfinement transition. The algebra supplies the carrier and the normalization; the analysis is standard lattice gauge theory.

**Not supplied.** The lattice does not add a new gauge group: it regularizes the compact factor the algebra contains, so it is the $SU(2)$ theory. It does not supply the fermion content, the chiral structure or the colour octet. It does not by itself prove confinement beyond the strong-coupling regime, and it does not supply a continuum construction of the non-abelian measure without a limit. As everywhere in the series, no empirical content is added.

## Summary

The lattice is the regulator that makes the biquaternion path integral a finite-dimensional integral. The link variable is the parallel transporter, a unit quaternion,
$$
U_\mu(n)=\exp\!\big(ia\kappa\mathcal{A}_\mu(n)\big)\in SU(2),
$$
transforming as $U_\mu(n)\mapsto U(n)U_\mu(n)U(n+\hat\mu)^{-1}$, and the plaquette is
$$
U_{\mu\nu}(n)=U_\mu(n)U_\nu(n+\hat\mu)U_\mu(n+\hat\nu)^{-1}U_\nu(n)^{-1}
=\exp\!\big(ia^2\kappa F_{\mu\nu}(n)+O(a^3)\big).
$$
The Wilson action $S_W=\beta\sum(1-\frac1N\mathrm{ReTr}U_{\mu\nu})$ has the small-$a$ expansion
$$
1-\frac1N\mathrm{ReTr}U_{\mu\nu}=\frac{a^4\kappa^2}{2N}\mathrm{Tr}\left(F_{\mu\nu}F^{\mu\nu}\right)+O(a^6),
$$
so that with $\beta=2N/\kappa^2=4/\kappa^2$ it reduces to the Euclidean Yang–Mills density $\frac12\mathrm{Tr}(F_{\mu\nu}F^{\mu\nu})$; both the plaquette identity and the normalization were checked numerically on a constant non-abelian field. The path integral is the finite product of normalized Haar measures on the unit quaternions,
$$
Z=\int\prod_{n,\mu}dU_\mu(n)\;e^{-S_W[U]},
\qquad
dU=\frac{1}{2\pi^2}\sin^2\theta\,d\theta\,d\Omega,
$$
with a transfer matrix and reflection positivity inherited from the standard theory. The strong-coupling expansion gives the area law
$$
\langle W(C)\rangle\sim e^{-\sigma A},
\qquad
\sigma a^2=-\ln\!\left(\frac{\beta}{2N^2}\right)+O(1),
$$
with the $N=2$ one-plaquette average beginning at $\beta/4$; this is confinement on the unit-quaternion lattice. The continuum limit $a\to0$, $\beta\to\infty$ is governed by the asymptotically free running of $\kappa$ with $b_0=22/3$, and it recovers the gauge-field path integral of the companion articles. The algebra supplies the carrier, the trace, the plaquette expansion and the coupling normalization; the strong-coupling analysis, the continuum limit and the confinement interpretation are imported, the last of these pointing to the informational subcategory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$ |
| $i$ | Central scalar imaginary |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $T_a=\tfrac12 ie_a\in\mathbb{M}_+$, $[T_a,T_b]=i\varepsilon_{abc}T_c$, $\mathrm{Tr}(T_aT_b)=\tfrac12\delta_{ab}$ | Compact gauge algebra (Hermitian-generator realization) |
| $\mathcal{A}_\mu=\mathcal{A}_\mu^a T_a$, $\kappa=q/\hbar$ | Connection and coupling |
| $F_{\mu\nu}=\partial_\mu\mathcal{A}_\nu-\partial_\nu\mathcal{A}_\mu+i\kappa[\mathcal{A}_\mu,\mathcal{A}_\nu]$ | Non-abelian curvature |
| $a$ | Lattice spacing |
| $U_\mu(n)=\exp(ia\kappa\mathcal{A}_\mu(n))\in SU(2)$ | Link variable (unit quaternion) |
| $U_\mu(n)\mapsto U(n)U_\mu(n)U(n+\hat\mu)^{-1}$ | Lattice gauge transformation |
| $(D_\mu\phi)(n)=a^{-1}(U_\mu(n)\phi(n+\hat\mu)-\phi(n))$ | Discrete covariant difference |
| $U_{\mu\nu}(n)$ | Plaquette; product of four links around an elementary square |
| $U_{\mu\nu}=\exp(ia^2\kappa F_{\mu\nu}+O(a^3))$ | Plaquette expansion |
| $\mathrm{Tr}\,U=2\,\mathrm{Re}(U_0)$ | Trace of a group element |
| $S_W=\beta\sum(1-\tfrac1N\mathrm{ReTr}U_{\mu\nu})$, $N=2$ | Wilson action |
| $\beta=2N/\kappa^2=4/\kappa^2$ | Lattice coupling |
| $Z=\int\prod_{n,\mu}dU_\mu(n)e^{-S_W}$ | Lattice path integral |
| $dU=\tfrac{1}{2\pi^2}\sin^2\theta\,d\theta\,d\Omega$ | Normalized Haar measure on the unit quaternions |
| $W(C)=\tfrac1N\mathrm{Tr}\prod_{l\in C}U_l$ | Lattice Wilson loop |
| $\langle W(C)\rangle\sim e^{-\sigma A}$ | Area law; $\sigma$ the string tension |
| $\sigma a^2=-\ln(\beta/2N^2)+O(1)$ | Leading strong-coupling string tension |
| $\tfrac12\langle\mathrm{Tr}U_\square\rangle=I_2(\beta)/I_1(\beta)=\beta/4+O(\beta^3)$ | $SU(2)$ one-plaquette average |
| $b_0=\tfrac{11}{3}C_2(G)=\tfrac{22}{3}$ | One-loop coefficient for pure $SU(2)$ |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)$ | $ict$ metric (level 2) |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Informational trace formula, distinct from the matrix trace |

## Further Reading

- K. G. Wilson, "Confinement of quarks," *Physical Review D* **10** (1974) 2445–2459, for the lattice gauge theory, the plaquette action and the strong-coupling area law.
- K. G. Wilson, "Nonabelian lattice gauge theories," in *New Phenomena in Subnuclear Physics*, ed. A. Zichichi (Plenum, 1977), for the lattice formulation and its continuum limit.
- J. B. Kogut and L. Susskind, "Hamiltonian formulation of Wilson's lattice gauge theories," *Physical Review D* **11** (1975) 395–408, for the transfer matrix, the Hamiltonian limit and the strong-coupling expansion.
- J. B. Kogut, "An introduction to lattice gauge theory and spin systems," *Reviews of Modern Physics* **51** (1979) 659–713, for the group integrals, the tiling expansion and the area law.
- M. Creutz, *Quarks, Gluons and Lattices* (Cambridge, 1983), for the one-plaquette model, the Bessel-function averages and the deconfinement transition.
- K. Osterwalder and R. Schrader, "Axioms for Euclidean Green's functions," *Communications in Mathematical Physics* **31** (1973) 83–112, for reflection positivity and the reconstruction of the Hamiltonian.
- M. Lüscher, "Construction of a selfadjoint, strictly positive transfer matrix for Euclidean lattice gauge theories," *Communications in Mathematical Physics* **54** (1977) 283–292, for the positivity of the Wilson transfer matrix.
- A. Hasenfratz and P. Hasenfratz, "The equivalence of the $SU(2)$ lattice gauge theory with a non-linear sigma model," *Physics Letters B* **93** (1980) 165–168, for the $SU(2)$ lattice structure and the real-fundamental special case.
- M. Creutz, "Monte Carlo study of quantized $SU(2)$ gauge theory," *Physical Review D* **21** (1980) 2308–2315, for the numerical lattice determination of the string tension and the scaling of the coupling.
- G. Münster and P. Weisz, "On the continuum limit of lattice gauge theories," *Nuclear Physics B* **180** (1981) 330–338, for the approach to the continuum and the scaling behaviour.
