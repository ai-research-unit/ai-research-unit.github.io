# __The Anomalous Magnetic Moment in Biquaternionic Form__

## Introduction

The magnetic moment of the electron is the most precisely tested prediction of quantum field theory, and its content is a single number: the anomaly $a=(g-2)/2$, the fractional departure of the gyromagnetic ratio from the value that the Dirac equation alone requires. That departure is a radiative correction. It is produced by the virtual photon that the electron emits and reabsorbs, and its leading value, $\alpha/2\pi$, is finite, universal and independent of the electron's mass.

This article is the worked radiative application of the spin-$\tfrac12$ subcategory. It establishes four things and is explicit about a fifth.

- **The vertex and its two structures.** The one-particle vertex has two independent Lorentz structures, and the magnetic one carries $F_2$. The tree-level value $g=2$, the Dirac value, is taken as settled by the companion *The Classical Origin of $g=2$ in Biquaternionic Form*; what is at issue here is $F_2(0)=a$.
- **The Gordon decomposition, in the algebra's own objects.** The biquaternion content of the problem is the split of the vertex into a *symmetric* part and an *antisymmetric* part. The symmetric part is the metric, one number per pair of directions and the central direction $e_t$; the antisymmetric part is the bivector of the pair, which is $i\vec e_m$ for two spatial directions and a two-sided operator for a timelike pair. The Gordon identity, which is the on-shell form of that split, was verified numerically in the algebra's own objects, with a residual of order $10^{-15}$.
- **The sector interpretation.** The magnetic structure is the rotation-type bivector, the element $i\vec e_m$: the informational sector $\mathbb{B}_{\Psi}$, the same sector as the spin. The convection structure is the metric, central part; the electric (timelike-pair) bivector is anti-Hermitian and belongs to the material sector $\mathbb{B}_{\Phi}$.
- **The one-loop value, transcribed and its integral verified.** The standard Feynman-parameter representation of the magnetic form factor reduces at $k^2=0$ to an integral whose value is exactly $1$; that reduction was verified, so that $a=\alpha/2\pi$ follows from the standard representation.
- **What the algebra does not supply.** It does not produce $\alpha$, and it does not by itself remove the divergence. The finiteness of the anomaly rests on the Ward identity, that is, on gauge invariance; the framework writes the vertex in its own objects and does not replace that argument.

**The state.** The field of this article is an element $w$ of $\mathbb{B}$, never a list of components. The incoming state is $w$ and the outgoing one is $w_2$; their momenta are $p$ and $p_2$, and $k=p_2-p$ is the momentum the photon carries. An amplitude is the **pairing** of the outgoing state with the element the vertex carries into the incoming one,
$$\bar w_2\,X:=\mathrm{Sc}\big(w_2^{*}\,i\,X\,\vec e_x\big),$$
a scalar part of a product of three factors, written here as in the companion *The Gordon Decomposition of the Dirac Current in Biquaternionic Form*. The one datum of the frame it carries is the right multiplier $\vec e_x$, the adjoint's unit. Plane waves are $e^{+i(p\cdot x)/\hbar}$, so the on-shell condition below carries the sign it carries; a change of that convention flips the sign of the mass in the second display of §*The Vertex Function and the Form Factors* and the sign of the bivector term with it.

**The directions.** A direction of the frame acts on a state by a product on both sides. That is a derived form of the frame's four directions of *Matrix Representations Conventions*, used throughout: the timelike direction carries $X$ to $iX\vec e_x$, and the direction $k$ carries it to $i\vec e_kX\vec e_y$. The two multipliers are $\vec e_x$ and $\vec e_y$, and $\vec e_z$ is their product, $\vec e_x\vec e_y=\vec e_z$; the frame is the canonical one of the companion articles, and the two multipliers are what declares it. The weight is $\varepsilon=(1,-1,-1,-1)$, one and the same for the directions and for the states: a paired index is written low and carries that weight, so a contraction over $\nu$ carries $\varepsilon_\nu$, and no index is ever raised.

**The factor $i$ and the two signs.** Every direction carries one factor $i$, and the two families square to opposite signs on a state:
$$\big(i\,X\,\vec e_x\big)^2=+X ,\qquad \big(i\,\vec e_k\,X\,\vec e_y\big)^2=-X .$$
The first square has two minus signs, one from $i^2=-1$ and one from $\vec e_x^2=-e_t$; the second has three, the third from $\vec e_k^2=-e_t$. Nothing else produces the two signs, and nothing else is needed: the weight $\varepsilon$ is the statement that the timelike direction is the one whose square on a state is positive.

**Products of two directions.** A product of two directions is again a single product of elements, and the metric part is visible in it. Two spacelike directions give a left multiplication,
$$i\vec e_j\big(i\vec e_kX\vec e_y\big)\vec e_y=+\vec e_j\vec e_kX ,$$
a timelike direction followed by a spacelike one gives a product on both sides,
$$i\big(i\vec e_kX\vec e_y\big)\vec e_x=+\vec e_kX\vec e_z ,$$
and the reverse order gives the opposite sign,
$$i\vec e_k\big(iX\vec e_x\big)\vec e_y=-\vec e_kX\vec e_z .$$
Two minus signs cancel in the second display, one from $i^2$ and one from $\vec e_y\vec e_x=-\vec e_z$; the third display carries one of them. The product of a direction with itself is the metric, $+e_t$ or $-e_t$; the product of two distinct directions has no metric part, and what is left is the bivector.

**The propagator.** The conventions of the internal fermion line are those of the companion *The Feynman Propagator in Biquaternionic Form*, and there it is written as an action on a state,
$$S_F(p):\quad w\,\longmapsto\frac{-p_0\,w\,\vec e_x+\sum_k  p_k\,\vec e_k\,w\,\vec e_y+im\,w}{p^2-m^{2}\,c^{2}+i\epsilon} ,$$
with $p^2=p_0^2-\sum_kp_k^2$. The factor $i$ of the numerator is what shortens it: distributing the outer $i$ of the companion's display turns $i\cdot i$ into $-1$ in each of the first two terms and leaves $i\,m$ in the third. The denominator $p^2-m^{2}\,c^{2}$ is $-\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}-m^2$ for the wave biquaternion $\tilde P_{\Phi}=ip_0e_t+\vec p$ of that companion, whose norm is $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}=-p^2$.

**The traces.** Two traces are used, and they are not the same one. On the algebra the trace of a product is twice the scalar part, $\mathrm{Tr}_2(\tilde Q_1\tilde Q_2)=2\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, the plain form. On the operators the trace is four-by-four and factorizes, $\mathrm{tr}(L_aR_b)=4\mathrm{Sc}(a)\mathrm{Sc}(b)$, the two multipliers contributing separately; both are conventions of *Matrix Representations Conventions* and are cited, not derived. The fine-structure constant is $\alpha=e^2/(\frac{4\,m\,c^{2}\,\pi\,\epsilon_{0}}{k_m})$, and every mass enters through the mass wave number $k_m=mc/\hbar$.

## The Vertex Function and the Form Factors

**The vertex.** The electromagnetic vertex is the one-particle-irreducible three-point function, written $-ie\Gamma_\mu(p_2,p)$, with $p$ the incoming and $p_2$ the outgoing fermion momentum and $k=p_2-p$ the momentum transferred by the photon. Lorentz invariance, the on-shell condition of the state,
$$i\,p_0\,w\,\vec e_x-\sum_k i\,p_k\,\vec e_k\,w\,\vec e_y=m\,w ,$$
the same condition carried by the adjoint, whose equation the companion writes with the mass on the other side, and the discrete symmetries reduce $\Gamma_\mu$ to two independent structures multiplied by functions of the single invariant $k^2$. The timelike and the spacelike components are written separately, because they act differently:
$$\Gamma_0\,w=i\,w\,\vec e_x\,F_1(k^2)+\frac{1}{2\,m}\sum_k  k_k\,\vec e_k\,w\,\vec e_z\,F_2(k^2) ,$$
$$\Gamma_j\,w=i\,\vec e_j\,w\,\vec e_y\,F_1(k^2)+\frac{1}{2\,m}\Big(k_{t}^{\prime}\,\vec e_j\,w\,\vec e_z+\sum_{k\ne j} k_k\,\vec e_j\vec e_k\,w\Big)F_2(k^2) .$$
The first term of each line is the direction $\mu$ acting on the state; the second is the bivector of the pair $(\mu,\nu)$, and its shape is the content of the Gordon decomposition below.

Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

$F_1(0)=1$ is the charge, and $F_2(0)$ is the anomaly. The gyromagnetic ratio is
$$\boxed{\;g=2\big(F_1(0)+F_2(0)\big)=2\big(1+F_2(0)\big),
\qquad
a=\frac{g-2}{2}=F_2(0)\;}.$$
At tree level only the first term of each line is present, so $F_1=1$, $F_2=0$ and $g=2$: the Dirac value, which is one-particle physics and is settled in the companion article. What this article computes is the correction to it.

**Why two structures.** The two are distinguished by symmetry, and that is where the interpretation begins. At $\mu=0$ the direction acts by a single right multiplication, by $i\vec e_x$; at $\mu=k$ it acts by a left multiplication, by $i\vec e_k$, and a right one, by $\vec e_y$. The bivector is $i$ times the product of two directions, so it carries one factor of $i$ more than the direction does. The vertex is therefore the sum of a structure with a single factor of $i$ and a structure with two, and only the second carries the spin-magnetic coupling.

The split is a property of the product of two directions. Two distinct directions multiply to a single direction of the algebra, the signs from $i^2$ and from $\vec e_y^2$ combining to $+$,
$$i\vec e_j\big(i\vec e_kX\vec e_y\big)\vec e_y=\vec e_j\vec e_kX ,\qquad \vec e_j\vec e_k=\pm\vec e_m ,$$
and the bivector of the pair is that product with one further factor $i$. For a pair of two spatial directions it is the single element $i\vec e_m$, a left multiplication; for a timelike pair it is two-sided, because the timelike direction supplies a right multiplier $\vec e_x$ and the spatial one supplies $\vec e_y$, whose product is the third unit. Nothing else appears in the product: the metric part is $\varepsilon_\mu$ on the diagonal, it is zero off it, and it is the central direction $e_t$, one number per pair.

**The Gordon decomposition.** Write $w$ for the incoming state and $w_2$ for the outgoing one, both on shell, and write $\mathcal G_{\mu\nu}:=-i\,c_\mu c_\nu$ for the bivector of the pair, $c_\mu$ being the direction $\mu$; the minus is the reversal of the right multipliers, $\vec e_y\vec e_x=-\vec e_z$, and it is the whole of the sign. The identity is
$$\bar w_2\big(c_\mu w\big)=\frac{(p+p_2)_\mu}{2m}\,\bar w_2w+\frac{i}{2\,m}\sum_{\nu\neq\mu}\varepsilon_\nu\,k_\nu\,\bar w_2\big(\mathcal  G_{\mu\nu}w\big),$$
the coefficient of the second term carrying the $i$ by which the bivector differs from the plain product of its two directions. Written out in the two families it reads, for the timelike component,
$$\bar w_2\big(i\,w\,\vec e_x\big)=\frac{(p+p_2)_0}{2m}\,\bar w_2w+\frac{1}{2\,m}\sum_k  k_k\,\bar w_2\big(\vec e_k\,w\,\vec e_z\big),$$
and for the spacelike component $j$,
$$\bar w_2\big(i\,\vec e_j\,w\,\vec e_y\big)=\frac{(p+p_2)_j}{2m}\,\bar w_2w+\frac{1}{2\,m}\Big(k_{t}^{\prime}\,\bar w_2\big(\vec e_j\,w\,\vec e_z\big)+\sum_{k\ne j} k_k\,\bar w_2\big(\vec e_j\vec e_k\,w\big)\Big),$$
where the $i$ of the generic form has been absorbed: $\frac{i}{2\,m}\varepsilon_k\mathcal  G_{0k}=\frac{1}{2\,m}\vec e_k$ on the right, and $\frac{i}{2\,m}\varepsilon_k\mathcal  G_{jk}=\frac{1}{2\,m}\vec e_j\vec e_k$. The three were verified on random on-shell pairs at $m=0.7$, with a deviation of order $10^{-15}$.

Read the right-hand sides. The first term is the convection: the momentum sum $(p+p_2)_\mu$ multiplies the central direction, and it is the term the charge multiplies. The second is the bivector: the momentum difference $k_\nu$ multiplies a product of two directions, and it is the term the magnetic moment multiplies. There is no third term, and the split is exact, not an approximation.

The coefficient $1/2m$ is the same one that fixes $g=2$ at the tree level, and it is untouched by the renormalisation. The Ward identity $k_\mu\Gamma_\mu=0$ is gauge invariance at the vertex. It forces the divergent part of $\Gamma_\mu$ to be proportional to the first structure, so nothing divergent reaches the second, and the anomaly is finite: no counterterm is needed for it.

**What this transcription does and does not do.** It names *which* object the anomaly multiplies: the bivector of the pair, hence the element $i\vec e_m$ for a rotation pair and the two-sided operator for a timelike one, hence a sector. It exhibits the Gordon split as the symmetric-versus-antisymmetric split of a product of two directions. It does not compute the loop integral, and it does not fix $\alpha$.

## The Six Directions

**The bivectors.** The six bivectors are $\mathcal G_{\mu\nu}=-i\,c_\mu c_\nu$: $i$ times the product of the two directions, with the sign that the reversed right multipliers give. On a state the two families act differently, and the difference is the frame's:
$$X\longmapsto i\vec e_m\,X\quad\text{(rotations)},\qquad X\longmapsto i\vec e_k\,X\,\vec e_z\quad\text{(boosts)} ,$$
with $\vec e_m$ the third spatial unit of the pair $\{j,k\}$, $\vec e_j\vec e_k=\pm\vec e_m$, and $\vec e_x\vec e_y=\vec e_z$ supplying the right multiplier of a timelike pair. The rotation bivector is a left multiplication by one direction; the boost bivector is a left multiplication by one direction and a right multiplication by the third. All six were verified direction by direction, and none of the six is a single element except the three rotations.

**The sector reading.** A left multiplication is Hermitian exactly when its multiplier is, and the rotation bivector multiplies by $i\vec e_m$, which is fixed by the star, $(i\vec e_m)^{*}=i\vec e_m$. The rotation bivectors therefore lie in the informational sector $\mathbb{B}_{\Psi}$. A timelike bivector multiplies by $i\vec e_k$ on the left and by $\vec e_z$ on the right, and the star reverses the order and conjugates each factor, $(aQb)^{*}=b^{*}Q^{*}a^{*}$; with $(i\vec e_k)^{*}=i\vec e_k$ and $\vec e_z^{*}=-\vec e_z$ the two classes are opposite, so the insertion is anti-Hermitian and lies in the material sector $\mathbb{B}_{\Phi}$. The rule is the one of the companion *The Electric Dipole Moment and the Biquaternion Anti-Hermitian Structure*, where the four insertions are classified by it:
$$\boxed{\;\text{magnetic: }i\vec e_m\in\mathbb{B}_{\Psi}\ \text{(Hermitian, informational)},
\qquad
\text{electric: }i\vec e_k(\cdot)\vec e_z\in\mathbb{B}_{\Phi}\ \text{(anti-Hermitian, material)}\;}.$$
Both classes were verified: $(i\vec e_m)^{*}=i\vec e_m$ and $\vec e_z^{*}=-\vec e_z$, and the products of the two classes come out opposite.

The magnetic coupling to an external field is a rotation-type structure, and its direction $i\vec e_m$ is the very object that carries the spin, $\tilde S_{\Psi,m}=\frac{m\,c}{2\,k_m}i\vec e_m$, in the companion *Angular Momentum and Spin in Biquaternionic Form*. The anomaly, being a correction to the magnetic structure, is an $\mathbb{B}_{\Psi}$ effect: the same sector as the observable it corrects. The electric (boost-type) structure is the material-sector one, and the convection (metric) part is central, in neither sector.

**The spin.** The rotation bivector acts on a state as a left multiplication by $i\vec e_m$, which is twice the spin generator, $\frac{2\,k_m\,\tilde{S}_{\Psi,m}}{m\,c}$. At the first direction, $\mathcal G_{12}$ acts as multiplication by $i\vec e_z=\frac{2\,k_m\,\tilde{S}_{\Psi,3}}{m\,c}$. Two sectors, one bivector algebra, and the anomaly's structure is the informational one.

**The bivector algebra.** The Lorentz generator of the pair is half the operator of the pair, and the closure of the six on the Lorentz algebra is a statement about the operators and not about the elements. It is therefore stated where the operators are written out, in §*The Reduction of a Numerator*; what the objects show without the operators is the Hermiticity split just read: the three rotations are single elements and their class is read off them, and the three timelike pairs are two-sided and their class is read off the two multipliers.

## The Reduction of a Numerator

**Why operators here.** The algebraic work behind the loop computation is the reduction of the numerator, and it is a statement about the operators that act on the state rather than about the elements. This section therefore writes them as cells, $L_aR_b$ with $L_aR_b\,X=aXb$, and the cell of the direction $\mu$ as $iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$, $\nu(t)=x$, $\nu(k)=y$. It is the one section of the article that does, and the reason is that the operators are its subject; in the algebra's own objects the same four sums are read off the products of the units, and the correspondence between the two readings is stated in the closing section.

**The closure.** The generator of the pair is half the operator of the pair,
$$S_{\mu\nu}=\tfrac{i}{2}\big(iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\big)\big(iL_{e_\nu}R_{\vec e_{\nu(\nu)}}\big),$$
and the six close on the Lorentz algebra, with residual $0$:
$$\big[S_{\mu\nu},S_{\rho\sigma}\big]
=i\big(g_{\nu\rho}S_{\mu\sigma}-g_{\mu\rho}S_{\nu\sigma}-g_{\nu\sigma}S_{\mu\rho}+g_{\mu\sigma}S_{\nu\rho}\big).$$
The sign is the one the normalisation carries: the conventions' generator is half the commutator of the two cells, and this section's is $S_{\mu\nu}=\tfrac12\mathcal G_{\mu\nu}$, which is that generator times $-i$; the extra $i$ is accounted for in the closing section.

**The four contractions.** The reduction rests on four sums over the direction index, verified with residual $0$ on every index combination:
$$\sum_\mu\varepsilon_\mu\,\big(iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\big)\big(iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\big)=4e_t ,$$
$$\sum_\mu\varepsilon_\mu\,\big(iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\big)\big(iL_{e_\alpha}R_{\vec e_{\nu(\alpha)}}\big)\big(iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\big)=-2\,iL_{e_\alpha}R_{\vec e_{\nu(\alpha)}} ,$$
$$\sum_\mu\varepsilon_\mu\,\big(iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\big)\big(iL_{e_\alpha}R_{\vec e_{\nu(\alpha)}}\big)\big(iL_{e_\beta}R_{\vec e_{\nu(\beta)}}\big)\big(iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\big)=4\varepsilon_\alpha\delta_{\alpha\beta}\,e_t ,$$
$$\sum_\mu\varepsilon_\mu\,\big(iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\big)\big(iL_{e_\alpha}R_{\vec e_{\nu(\alpha)}}\big)\big(iL_{e_\beta}R_{\vec e_{\nu(\beta)}}\big)\big(iL_{e_\rho}R_{\vec e_{\nu(\rho)}}\big)\big(iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\big)=-2\,iL_{e_\rho}R_{\vec e_{\nu(\rho)}}\,iL_{e_\beta}R_{\vec e_{\nu(\beta)}}\,iL_{e_\alpha}R_{\vec e_{\nu(\alpha)}} .$$
Read off in order: the cell of a direction squares to the weight, $+1$ timelike and $-1$ spacelike; sandwiching one cell gives minus twice that cell, the minus being the reversal of a product of odd length; sandwiching two gives the metric and nothing else; sandwiching three gives the three in reverse order. The unit $e_t$ on the right of the first and the third is the identity on every state. The four are what convert a one-loop numerator, which is a product of an even number of directions, into sums of metric factors and bivectors: precisely the two structures of the vertex.

**The traces of the operators.** Since a product of cells is again a cell, the trace factorizes at every length, $\mathrm{tr}(c_{\mu_1}\cdots c_{\mu_n})=4\mathrm{Sc}(a_{\mu_1}\cdots a_{\mu_n})\mathrm{Sc}(b_{\mu_n}\cdots b_{\mu_1})$ for $c_\mu=L_{a_\mu}R_{b_\mu}$, a convention of *Matrix Representations Conventions*. Two consequences are used under every numerator: $\mathrm{tr}\big((iL_{e_\mu}R_{\vec e_{\nu(\mu)}})(iL_{e_\nu}R_{\vec e_{\nu(\nu)}})\big)=4g_{\mu\nu}$, and a single direction is traceless, one of its two multipliers being a vector unit of vanishing scalar part.

## The One-Loop Correction

**The diagram.** The order-$\alpha$ correction to the vertex is the one-loop diagram in which the fermion line exchanges a virtual photon with itself. Its value is standard: the numerator is reduced with the contraction identities of the previous section, and the result is
$$F_1(k^2)=1+\frac{\alpha}{2\pi}\Big[\text{terms vanishing at }k^2=0\Big] ,$$
$$F_2(k^2)=\frac{\alpha}{2\pi}\int_0^1\!dx\,dy\,dz\;\delta(x+y+z-1)\;
\frac{2m^2z(1-z)}{m^2(1-z)^2-xy\,k^2} ,$$
in the standard Feynman-parameter representation. The sign of the $k^2$ term is fixed by analyticity: the denominator vanishes first at $k^2=4m^2$, the pair-production threshold, and with the opposite sign the branch point would sit at $k^2=-4m^2$, where there is no threshold. Two features make the anomaly the clean test it is.

- **The divergence stays in $F_1$.** The Ward identity $k_\mu\Gamma_\mu=0$ is gauge invariance at the vertex, and it forces the divergent part of $\Gamma_\mu$ to be proportional to the tree vertex, that is to the $F_1$ structure. The divergence of the vertex is the same one the fermion self-energy carries, $Z_1=Z_2$, and the same counterterm removes both. Nothing divergent reaches $F_2$, so the anomaly is *finite*: no counterterm is needed for it, and it is a prediction of the theory rather than a parameter of it. This argument is standard and is not supplied by the algebra.
- **The mass drops out at leading order.** At $k^2=0$ the parameter integral is independent of $m$ after the $m^2$ factors cancel, so the leading anomaly is universal: every charged lepton has the same leading $a=\alpha/2\pi$, and every charged fermion does after the appropriate QCD corrections.

**The $k^2=0$ integral.** At $k^2=0$ the denominator is $m^2(1-z)^2$, the mass cancels, and the parameter integral collapses:
$$\int_0^1\!dz\int_0^{1-z}\!dy\;\frac{2z(1-z)}{(1-z)^2}
=\int_0^1\!dz\;\frac{2z}{1-z}\big[(1-z)-0\big]
=\int_0^1\!2z\,dz=1 ,$$
the inner parameter running over an interval of length $1-z$.

This reduction was verified numerically, and it is exactly what makes the leading value
$$\boxed{\;a=\frac{\alpha}{2\pi}=1.1614097329\times10^{-3}\;}$$
for $\alpha=1/137.035999084$. The number is Schwinger's, the first radiative correction ever computed, and it sits above the measured electron anomaly
$$a_{\mathrm{exp},e}=1.15965218073\times10^{-3}$$
with a relative excess of $1.5156\times10^{-3}$, of the order of the two-loop correction.

**The higher orders.** The perturbative series is conventionally written
$$\boxed{\;a=\sum_{\lambda\ge1}A_\lambda\Big(\frac{\alpha}{\pi}\Big)^\lambda ,
\qquad
A_1=\frac12=0.5 ,
\qquad
A_2=\frac{197}{144}+\frac{\pi^2}{12}-\frac{\pi^2}{2}\ln2+\frac34\zeta(3)\;}.$$
The two-loop coefficient was recomputed from this closed form:
$$A_2=-0.328478965579\ldots ,$$
in agreement with the standard value. With $A_3=1.181241456\ldots$ the electron prediction becomes
$$a_e=1.1596522320\times10^{-3}$$
against the measured $1.15965218073\times10^{-3}$: agreement to $5\times10^{-11}$ in $a_e$, nine significant figures. That comparison tests the standard calculation and not this framework; it is reproduced here because it is the numerical reference the conventions are checked against. With the two-loop term alone the prediction is $1.1596374278\times10^{-3}$, short by about $1.5\times10^{-8}$, which is the size of the three-loop term. Beyond QED, the same decomposition organizes the muon anomaly into its QED, electroweak and hadronic parts; that is particle physics and lies outside this subcategory.

## What the Algebra Supplies and What It Does Not

**Standard, transcribed.** The vertex decomposition into $F_1$ and $F_2$; the tree-level $g=2$; the Gordon decomposition; the one-loop diagram and its Feynman-parameter representation; the Ward-identity confinement of the divergence to the $F_1$ structure; the value $a=\alpha/2\pi$; the higher-order coefficients; the comparison with the measured electron anomaly; the trace and contraction identities of the operators; and the four directions with their squares.

**The algebra's own.**

- *The sector placement of the two vertex structures.* The magnetic (bivector, rotation-type) structure is the $\mathbb{B}_{\Psi}$ direction $i\vec e_m$, the same sector as the spin generators $\tilde S_{\Psi,m}=\frac{m\,c}{2\,k_m}i\vec e_m$; the electric (timelike-pair) structure is the two-sided insertion $i\vec e_k(\cdot)\vec e_z$, anti-Hermitian, in $\mathbb{B}_{\Phi}$; the convection (metric) structure is central.
- *The Gordon split as the symmetric/antisymmetric split of a product of two directions*, done in the algebra's own objects.
- *The six bivectors.* Three are single elements, $i\vec e_m$, and three are two-sided; the class of each names its sector.

**It fixes the conventions.** The signs of the frame, the sign of the bivector, the adjoint state and the propagator's $i\epsilon$ are fixed by the companion articles, and the standard loop integral is transcribed into them without translation error.

**It does not supply the numbers.** The value of $\alpha$, the coefficient $A_2$, and the finiteness of the anomaly are not consequences of the algebra. The finiteness is the Ward identity's; the coefficients are the theory's; $\alpha$ is empirical. The position is exactly the one the propagator companion records for the $i\epsilon$ and the mass article records for the masses: the algebra names the axis, and physics fixes its magnitude and orientation.

## Open Questions

- **The intrinsic field.** As the companion propagation and quantization articles record, an intrinsic $\mathbb{B}$-valued three-point function is not constructed; the vertex here is the one-particle object transcribed into the algebra's own objects.
- **Whether the algebra constrains the coefficients.** No mechanism is offered by which $\mathbb{B}$ would fix $A_1$, $A_2$, or $\alpha$; the algebra's role is structural.
- **The electroweak and hadronic contributions** to the muon anomaly are outside this subcategory and are not treated.
- **The axial anomaly, the anomaly-cancellation conditions and the Fujikawa method** belong to the particle-physics subcategory; the trace anomaly and the functional determinant belong to the generalities subcategory. This article is the magnetic moment only, and it does not borrow their arguments.

## Verification

All numerics are machine-precision arithmetic in the biquaternion algebra, with the four directions $X\mapsto i\vec e_\mu X\vec e_{\nu(\mu)}$ of §*The Six Directions*, and in the four-by-four operators where a section is about the operators.

| Claim | Value / result |
|---|---|
| Squares of the directions | $(iX\vec e_x)^2=+X$, $(i\vec e_kX\vec e_y)^2=-X$: residual $0$ |
| Mixed products | $i(i\vec e_kX\vec e_y)\vec e_x=+\vec e_kX\vec e_z$ and $i\vec e_k(iX\vec e_x)\vec e_y=-\vec e_kX\vec e_z$: residual $0$ |
| Product of two spacelike directions | $i\vec e_j(i\vec e_kX\vec e_y)\vec e_y=+\vec e_j\vec e_kX$, with $\vec e_x\vec e_y=\vec e_z$: residual $0$ |
| On-shell condition | $ip_0w\vec e_x-\sum_kip_k\vec e_kw\vec e_y=mw$ on states built as $w=i\,p_0\,w_0\vec e_x-\sum_ki\,p_k\,\vec e_k\,w_0\vec e_y+m\,w_0$: residual $\sim10^{-16}$ |
| Pairing | $\bar wX=\mathrm{Sc}(w^{*}iX\vec e_x)$: linear in $X$ and conjugate-linear in $w$, residual $0$; the bra mass relation needs the frame multipliers moved, so it is not restated here |
| Vertex | the two lines of §*The Vertex Function and the Form Factors* against the direction plus the bivector sums: residual $\sim10^{-16}$ |
| Gordon identity | the generic form with $\mathcal G_{\mu\nu}$ and the two branches, over thirty random on-shell momentum pairs at $m=0.7$: deviation $\le4\times10^{-15}$ |
| Six bivectors | $\mathcal G_{12}$ acts as left multiplication by $i\vec e_z$, $\mathcal G_{23}$ by $i\vec e_x$, $\mathcal G_{31}$ by $i\vec e_y$; $\mathcal G_{01}$, $\mathcal G_{02}$, $\mathcal G_{03}$ act as $i\vec e_x(\cdot)\vec e_z$, $i\vec e_y(\cdot)\vec e_z$, $i\vec e_z(\cdot)\vec e_z$: residual $0$ |
| Hermiticity | $(i\vec e_m)^{*}=i\vec e_m$ and $\vec e_z^{*}=-\vec e_z$, so the rotations are Hermitian and the timelike pairs anti-Hermitian: residual $0$ |
| Bivector algebra | $S_{\mu\nu}=\tfrac12\mathcal G_{\mu\nu}$ and $\big[S_{\mu\nu},S_{\rho\sigma}\big]=i(g_{\nu\rho}S_{\mu\sigma}-g_{\mu\rho}S_{\nu\sigma}-g_{\nu\sigma}S_{\mu\rho}+g_{\mu\sigma}S_{\nu\rho})$: residual $0$ |
| Contractions | the four weighted sums of §*The Reduction of a Numerator*: residual $0$ on every index combination |
| Traces | $\mathrm{tr}L_aR_b=4\mathrm{Sc}(a)\mathrm{Sc}(b)$ and $\mathrm{Tr}_2(\tilde Q_1\tilde Q_2)=2\mathrm{Sc}(\tilde Q_1\tilde Q_2)$: residual $\le10^{-12}$ at word lengths one to four |
| Trace of two directions | the operator of the direction $\mu$ is traceless, and the operator of two directions has trace $4g_{\mu\nu}$: residual $0$ |
| $k^2=0$ integral | $\int_0^1dz\int_0^{1-z}dy\,\frac{2z(1-z)}{(1-z)^2}=\int_0^12z\,dz=1$ |
| Leading anomaly | $a=\alpha/2\pi=1.1614097329\times10^{-3}$ for $\alpha=1/137.035999084$ |
| Two-loop coefficient | $A_2=197/144+\pi^2/12-(\pi^2/2)\ln2+(3/4)\zeta(3)=-0.328478965579$ |
| Two-loop anomaly | $a_e=1.1596374278\times10^{-3}$ |
| Three-loop anomaly | $a_e=1.1596522320\times10^{-3}$ against the measured $1.15965218073\times10^{-3}$ |

The on-shell states were built as $w=i\,p_0\,w_0\vec e_x-\sum_ki\,p_k\,\vec e_k\,w_0\vec e_y+m\,w_0$ for a random $w_0$, which produces positive-energy solutions automatically; the momenta were on the mass shell with $m=0.7$ and random directions. Nothing here is a fit.

## Companion Articles

- Companion article *The Classical Origin of $g=2$ in Biquaternionic Form*, for the tree-level value $g=2$ that this article takes as given.
- Companion article *The Feynman Propagator in Biquaternionic Form*, for the propagator conventions and the $i\epsilon$ of the internal fermion line.
- Companion article *The Gordon Decomposition of the Dirac Current in Biquaternionic Form*, for the pairing and the two Dirac equations used in the identity.
- Companion article *Angular Momentum and Spin in Biquaternionic Form*, for the spin generators whose direction the magnetic bivector reproduces.
- Companion article *Canonical Quantization of the Biquaternion Dirac Field*, for the field operators whose electromagnetic three-point function is the vertex.

## The Legacy Pauli Gamma Formulation

**The older names.** A reader of the gamma literature meets the same operators under other names, and the translation is worth one paragraph, here, in the one place where this article writes them. The four directions of the frame are the four gammas of *Frame and Metric Conventions*, $\gamma_\mu=iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$, and the chirality cell is $\gamma_5=-iR_{\vec e_z}$; the arrays themselves are printed in *Matrix Representations Conventions*, §*The Legacy Pauli Gamma Formulation*, and this article prints none, because the object is the operator and the array is one display of it.

**The normalisation of the bivector.** The conventions article writes the Lorentz generator as half the commutator of the two cells, $\sigma_{\mu\nu}=\tfrac14\big[\gamma_\mu,\gamma_\nu\big]=\tfrac12c_\mu c_\nu$, and it takes twice that for the bivector of the pair. This article writes $\mathcal G_{\mu\nu}=-i\,c_\mu c_\nu=-2i\,\sigma_{\mu\nu}$ and $S_{\mu\nu}=\tfrac12\mathcal G_{\mu\nu}=-i\,\sigma_{\mu\nu}$: the conventions' objects times $-2i$ and $-i$, the minus being the reversal of the two right multipliers. What the factor buys is the Hermiticity of the class, $\mathcal G_{jk}=i\vec e_m$ fixed by the star, and it is what fixes the sign of the closure in §*The Reduction of a Numerator*. The two tables of six entries are one table read twice, the arithmetic of §*The Six Directions* reading the rotations against $i\vec e_m$ and the timelike pairs against $i\vec e_k$ on the left and $\vec e_z$ on the right.

**Why the display is not used.** The reason is the one given in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*: the gammas are a frame of one display and not a second algebra, the four directions are elements of one algebra, and every identity of this article is an identity of that algebra, unchanged by the display the reader writes it in.

## Summary

The anomalous magnetic moment in biquaternion form is the coefficient $F_2(0)=a$ of the bivector structure of the electromagnetic vertex,
$$\Gamma_0w=i\,w\,\vec e_xF_1+\frac{1}{2\,m}\sum_k k_k\,\vec e_k\,w\,\vec e_zF_2 ,\qquad
\Gamma_jw=i\,\vec e_j\,w\,\vec e_yF_1+\frac{1}{2\,m}\Big(k_{t}^{\prime}\,\vec e_j\,w\,\vec e_z+\sum_{k\ne j} k_k\,\vec e_j\vec e_k\,w\Big)F_2 ,$$
$$g=2\big(1+F_2(0)\big),\qquad a=F_2(0)=\frac{g-2}{2} ,$$
with the tree-level $g=2$ taken from the one-particle theory. The two vertex structures are the symmetric and antisymmetric parts of a product of two directions, the metric part and the bivector; the Gordon decomposition exhibits the split on shell and was verified with a deviation of order $10^{-15}$ on on-shell states. Of the six bivectors, the three rotations are the single elements $i\vec e_m$, in the informational sector $\mathbb{B}_{\Psi}$, the same sector as the spin, and the three timelike pairs are two-sided insertions, anti-Hermitian, in the material sector $\mathbb{B}_{\Phi}$. The convection structure is central.

The one-loop representation of $F_2$ reduces at $k^2=0$ to $\int_0^12z\,dz=1$, giving Schwinger's value $a=\alpha/2\pi=1.1614097329\times10^{-3}$; the two-loop coefficient $A_2=197/144+\pi^2/12-(\pi^2/2)\ln2+(3/4)\zeta(3)=-0.328478965579$ was recomputed, and with $A_3=1.181241456$ the prediction $a_e=1.1596522320\times10^{-3}$ matches the measured $1.15965218073\times10^{-3}$ to $5\times10^{-11}$. The trace and contraction identities on which the reduction rests were verified, the contractions at residual $0$ and the trace identity to rounding at every word length from one to four.

The algebra supplies the tensor structure, the sector placement and the conventions; it does not supply $\alpha$, the coefficients, or the Ward-identity argument that makes the anomaly finite. On this problem, as on the $i\epsilon$ and the masses, the framework names the axis and physics fixes the magnitude.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $w$, $w_2$ | Incoming and outgoing state, elements of $\mathbb{B}$ |
| $\bar wX=\mathrm{Sc}(w^{*}iX\vec e_x)$ | The pairing: an amplitude is $\bar w_2X$, a scalar part of three factors; the right multiplier $\vec e_x$ is the adjoint's unit |
| $p$, $p_2$, $k=p_2-p$ | Incoming momentum, outgoing momentum, momentum transfer |
| $iX\vec e_x$, $i\vec e_kX\vec e_y$ | The direction $t$ and the direction $k$ acting on a state $X$ |
| $(iX\vec e_x)^2=+X$, $(i\vec e_kX\vec e_y)^2=-X$ | The two signs of the frame, from $i^2=-1$ and $\vec e_x^2=\vec e_k^2=\vec e_y^2=-e_t$ |
| $\varepsilon=(1,-1,-1,-1)$ | Plain weight, the index rule; no index is raised |
| $\Gamma_\mu(p_2,p)$ | Electromagnetic vertex; $-ie\Gamma_\mu$ is the amplitude |
| $F_1(k^2),F_2(k^2)$ | Charge and magnetic form factors |
| $g=2(1+F_2(0))$, $a=F_2(0)=(g-2)/2$ | Gyromagnetic ratio and anomaly |
| $\mathcal G_{\mu\nu}=-i\,c_\mu c_\nu$ | Bivector of the pair $(\mu,\nu)$: $i$ times the product of the two directions, with the sign of the reversed right multipliers. $\mathcal G_{jk}$ is left multiplication by $i\vec e_m$; $\mathcal G_{0k}$ is two-sided, $i\vec e_k$ left and $\vec e_z$ right. $\mathcal G_{\mu\nu}=-2i\sigma_{\mu\nu}$ |
| $X\mapsto i\vec e_mX$, $X\mapsto i\vec e_kX\vec e_z$ | The two actions of the six bivectors, rotations and timelike pairs |
| $S_{\mu\nu}=\tfrac12\mathcal G_{\mu\nu}=-i\sigma_{\mu\nu}$ | Lorentz generator of the pair, half the bivector; the six close on the Lorentz algebra |
| Product of two directions | the metric $\varepsilon_\mu$ on the diagonal and nothing off it, plus the bivector |
| $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ | The two sectors, and $i\,\mathbb{B}_{\Psi}=\mathbb{B}_{\Phi}$ |
| $\tilde S_{\Psi,m}=\frac{m\,c}{2\,k_m}i\vec e_m$ | Spin generator; $\mathcal G_{12}$ acts as $\frac{2\,k_m\,\tilde{S}_{\Psi,3}}{m\,c}$ |
| $L_aR_b$, $L_aR_bX=aXb$ | The operator of the two multipliers, used in §*The Reduction of a Numerator* only |
| $iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$, $\nu(t)=x$, $\nu(k)=y$ | The operator of the direction $\mu$ |
| $\mathrm{tr}(L_aR_b)=4\mathrm{Sc}(a)\mathrm{Sc}(b)$ | Operator trace, factorized into the two multipliers |
| $\mathrm{Tr}_2(\tilde Q_1\tilde Q_2)=2\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Trace on the algebra, the plain form |
| Four contraction identities of §*The Reduction of a Numerator* | The four weighted sums (residual $0$) |
| $F_2(k^2)=\frac{\alpha}{2\pi}\int\!dx\,dy\,dz\,\delta(x+y+z-1)\frac{2m^2z(1-z)}{m^2(1-z)^2-xyk^2}$ | One-loop parameter representation |
| $a=\alpha/2\pi=1.1614097329\times10^{-3}$ | Leading (Schwinger) anomaly |
| $A_2=-0.328478965579$ | Two-loop coefficient (recomputed) |
| $a_{\mathrm{exp},e}=1.15965218073\times10^{-3}$ | Measured electron anomaly |

## Further Reading

- [The Classical Origin of g = 2 in Biquaternionic Form](the-classical-origin-of-g-2-in-biquaternionic-form.html), for the tree-level value this article takes as given.
- [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](the-gordon-decomposition-of-the-dirac-current-in-biquaternionic-form.html), for the pairing and the two Dirac equations.
- [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html), for the spin generators.
- [Matrix Representations Conventions](matrix-representations-conventions.html), for the frame's operators, their traces and the display of the closing section.
- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reason the closing section closes.

