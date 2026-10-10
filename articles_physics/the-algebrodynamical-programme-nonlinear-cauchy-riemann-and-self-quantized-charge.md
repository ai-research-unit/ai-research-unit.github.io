# __The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry__

## Introduction

The algebrodynamical programme of Vladimir Kassandrov and his collaborators takes the quaternion and biquaternion algebra as the **primary** object and asks what equation a differentiable function of an algebraic variable obeys. The answer is not the Fueter equation and not the Dirac equation. It is a **nonlinear** generalisation of the Cauchy–Riemann conditions, whose integrability conditions turn out to be the free Maxwell and Yang–Mills equations, and whose singular solutions the programme reads as particles — with their electric charge, in the programme's headline claim, **self-quantized**.

This article records the programme as presented in the source paper *Quaternionic Analysis and the Algebrodynamics* (arXiv:0710.2895), with the earlier parts of the series cited where they carry a result the paper only recalls — in particular the 1995 *Biquaternion Electrodynamics and the Weyl–Cartan Geometry of Space-Time* (arXiv:gr-qc/0007027), whose own text is the source of the geometric and Yang–Mills material in the two sections after *The Generating System and the Gauge Fields*, and the 1998 *Particles as Singularities within the Unified Algebraic Field Dynamics* (arXiv:gr-qc/9809056), the source of the dion solution, its multipole moments and the quadrupole prediction in the particle section; the closed-form static solution is the stereographic map of that section. One further paper of the series is the source of one further section: the 2016 conference note *Relativistic Algebra of Space-Time and Algebrodynamics* (arXiv:1612.02455, with J. A. Rizcallah), which supplies the **local** algebra of the section *The Local Algebra on a Curved Manifold, and the U-Field* — the covariant multiplication law and its isomorphism with $\mathbb{B}$, the tetrad and the required unit U-field, the effective metric and the metric built from the structure functions, and the curved differentiability condition with its induced connection. It is an **external programme**. The corpus records it and does not endorse it. It is recorded because three of its claims bear directly on questions this corpus states as open: whether charge quantisation can be **derived** rather than postulated, which *The Magnetic Monopole in Biquaternionic Form* currently records as imported from quantum physics rather than derived; whether the Lorentzian signature of spacetime can be read off the algebra rather than put in by hand, which *Why Complexify Spacetime?* states as a motivation and not a derivation; and what a genuinely **nonlinear** holomorphy over a noncommutative algebra looks like, which the linear Fueter theory of *Biquaternion Regular Functions* deliberately is not.

One convention differs from the corpus and is flagged once, so that formulas are not misread between the two. The source writes the holomorphic metric as $\det Z = (z_0)^2 - (z_1)^2 - (z_2)^2 - (z_3)^2$, with the time-like coordinate first; the corpus writes the biquaternion norm as $N(\tilde Q)=\sum_\mu Q_\mu^2$ with all-plus coefficients and the material identification $Q_0 = ict$. These are the same interval with the imaginary unit placed differently — they agree once $Q_0=z_0$ and $Q_k=iz_k$ for the spatial components — and both give the material signature $(3,1)$, so no physics depends on the difference; but a formula must not be transcribed from one to the other without that factor of $i$. Similarly, the source's coordinates $Z^{AB}$ are the four complex entries of a $2\times2$ matrix, so that the biquaternion algebra is $\mathbb{B}\cong\mathrm{Mat}(2,\mathbb{C})$ read as an algebra of coordinates; the corpus's $Q_\mu$ are the coefficients of the four units, and the two are related by the matrix element representation of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*.

The programme is large, and this article records it in one piece rather than scattering it. The order is the order of its logic: the failure of naive holomorphy, the two-sided replacement, the complex eikonal it produces, the twistor solution of that eikonal, the generating system and the gauge fields that are its integrability conditions, the Weyl–Cartan geometry and the local algebra that the later note attaches to a curved manifold, the Yang–Mills triplet that those conditions define, the Kerr equation and the shear-free congruences, the particle-like solutions with their quantised charge, the induced causal geometry, and finally the boundaries of what the programme claims.

## Why Naive Quaternionic Holomorphy Fails

The commutative case is the starting point, because it works. For a function $F$ of a variable $Z$ in a finite-dimensional associative **commutative** algebra, Scheffers' definition of differentiability is the proportionality of the differentials,

$$
dF = H(Z)\,dZ ,
$$

with $H\in A$. For an algebra with division this is equivalent to the existence and path-independence of the derivative $H=F'$, and for $A=\mathbb{C}$ it is the Cauchy–Riemann equation. Eliminating the components of $H$ gives a linear system for the components of $F$, and the whole of one-variable complex analysis has an analogue. The construction extends to commutative algebras with zero divisors, such as the double and dual numbers, when one demands that the differential take an invariant component-less form rather than that a derivative exist.

For $\mathbb{H}$ the naive transcription fails, and the source gives both of the standard reasons. The first is that noncommutativity erases the distinction between an element and its conjugate. In $\mathbb{H}$ the conjugate can be written using only the units,

$$
q^{*} = -\tfrac12\left(q + I^{*}q^{*}I + J^{*}q^{*}J + K^{*}q^{*}K\right),
$$

so "a function independent of the conjugated argument" — the definition of holomorphy in one complex variable — has no content here. The second is that the right derivative $F'=dF\,dZ^{-1}$ (or its left analogue) requires the limit to be independent of the path of $dZ$ to zero in the four-dimensional algebra, which is an over-determined system of partial differential equations; it is compatible only for linear functions $F = A Z + B$. This is the same obstruction the corpus records from Sudbery in *Biquaternion Regular Functions*: in four real dimensions there is no single complex variable, no invariant derivative, and the rich function theory of the plane does not transfer.

## The Two-Sided Derivative and Conformal Mappings

The source's replacement keeps the invariant-differential idea of Scheffers but allows a **factor on each side**:

$$
dF = L(Z)\,dZ\,R(Z) .
$$

The functions $L$ and $R$ are the **left and right semi-derivatives** of $F$; they are determined by $F$ only up to the equivalence $L\mapsto \alpha L$, $R\mapsto \alpha^{-1}R$ with $\alpha$ taking values in the centre of the algebra. The problem of "differentiable functions" becomes the enumeration of the triples $\{F,L,R\}$ obeying this condition up to that equivalence. For a commutative algebra the condition collapses back to $dF = (LR)\,dZ$, and if $R$ is the unit it collapses to the naive one-sided condition; it is exactly the two-sidedness that escapes the rigidity above.

For $\mathbb{H}$ the condition has a clean geometric meaning. Taking the quaternionic norm of both sides and using its multiplicativity, $N^2(pq)=N^2(p)N^2(q)$, gives

$$
ds^2 \equiv N^2(dF) = N^2(LR)\,N^2(dZ) \equiv \Lambda(Z)\,ds^2 ,
$$

so a $\mathbb{H}$-differentiable function is exactly a **conformal map of the Euclidean four-space** $E^4$, with scale factor $\Lambda=N^2(LR)$. The inversion $F=Z^{-1}$ has $dF = -Z^{-1}\,dZ\,Z^{-1}$, and translations, rotations and dilatations verify the condition directly. By Liouville's theorem the conformal maps of $E^4$ form a finite fifteen-parameter group, so the class is again too small to carry fundamental physics: an algebra with division is not enough.

**Physical reading.** This is the point at which the programme turns to the complexified algebra. The corpus's own Fueter theory keeps the linear operator $\tilde\nabla$ and asks for its kernel; the programme instead keeps the *definition of differentiability* and accepts that it is nonlinear. The two are different answers to the same obstruction. The corpus's linear answer is elliptic on the quaternion subspace and has a complete integral theory; the programme's nonlinear answer is the one that produces singular solutions, which is precisely why it can read them as particles.

## Complexification, Degenerate Conformality, and the Complex Eikonal

On the complexified algebra $\mathbb{B}\cong\mathrm{Mat}(2,\mathbb{C})$ the determinant replaces the norm. Taking determinants in the two-sided condition gives

$$
\det\lVert dF\rVert = \det\lVert L\rVert\det\lVert R\rVert \det\lVert dZ\rVert \equiv \lambda(Z)\det\lVert dZ\rVert ,
$$

which for invertible $L,R$ and $\lambda\neq0$ is again a conformal map, now of complexified Minkowski space $\mathbb{C}M$. The interesting case is the one the source calls **degenerate**: when $\det L=0$ (or $\det R=0$) the scale factor vanishes and the map takes its values in the **null divisors** of the algebra — the complex null cone. These degenerate conformal maps are the ones the programme identifies with physical fields, and complexification is what makes the class large.

In components the condition reads $\nabla_{AB}F_{CD}=L_{CA}R_{BD}$. Fixing a pair of function indices and writing $F_{CD}=\Sigma$, $L_{CA}=\varphi_A$, $R_{BD}=\psi_B$ gives

$$
\nabla_{AB}\Sigma = \varphi_A\psi_B .
$$

The matrix of derivatives of $\Sigma$ is therefore a product of a column and a row — it has rank one — so its determinant vanishes identically:

$$
\det\lVert\nabla_{AB}\Sigma\rVert = 0 .
$$

This is the central observation of the construction. The equation says that a component of a differentiable function has a **degenerate gradient matrix**, and it is a **nonlinear** equation because the degeneracy of the gradient is the residue of noncommutativity in the definition. It is the nonlinear analogue of the Laplace equation of complex analysis.

It becomes recognisable in coordinates. Writing the matrix entries as $Z^{00}=u$, $Z^{11}=v$, $Z^{01}=w$, $Z^{10}=p$ and computing the determinant gives

$$
(\nabla_u\Sigma)(\nabla_v\Sigma) - (\nabla_w\Sigma)(\nabla_p\Sigma) = 0 ,
$$

and in the Cartesian coordinates $z_0=(u+v)/2$, $z_3=(u-v)/2$, $z_1=(w+p)/2$, $z_2=i(w-p)/2$ this is

$$
\left(\frac{\partial\Sigma}{\partial z_0}\right)^2 - \left(\frac{\partial\Sigma}{\partial z_1}\right)^2 - \left(\frac{\partial\Sigma}{\partial z_2}\right)^2 - \left(\frac{\partial\Sigma}{\partial z_3}\right)^2 = 0 ,
$$

the **complex eikonal equation** of complexified Minkowski space. The verification of the coordinate change is one line of the chain rule and is confirmed by recomputation in this pass; the rank-one degeneracy is likewise confirmed on random complex matrices. Nothing in the derivation is special to four dimensions at the level of the determinant; what is special is that in the case $\mathbb{B}$ the nonlinear equation is a familiar one.

**Physical reading.** That the primary field equation is the eikonal is the programme's distinguishing feature. In the corpus the eikonal appears as the short-wavelength limit of a linear equation (*The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form*); here it is exact and primary, and the linear wave equation is recovered for the **derivatives** of its solution, not for the solution itself, as the next sections show.

## The Twistor Solution of the Complex Eikonal

The complex eikonal is solved algebraically, and the solution introduces the twistor. In the factorisation $\nabla_{AB}\Sigma=\varphi_A\psi_B$, choose one spinor, say $\psi=\{\psi_B\}$, and define the second by the Klein–Penrose incidence relation

$$
\tau = Z\psi , \qquad \tau^A = Z^{AB}\psi_B .
$$

The pair $\{\psi,\tau\}$ is a (projective) twistor of $\mathbb{C}M$ — the same incidence relation the corpus writes as $\omega^A=ix^{AA'}\pi_{A'}$ in *Twistor Theory and Biquaternions* and *The Spinor-Helicity Formalism and Biquaternions*, with the modulus of the projective equivalence being the freedom to rescale $\psi$. Choosing the gauge $\psi_0=1$ and writing $G=\psi_1/\psi_0$ gives the three projective components

$$
G,\qquad \kappa_0 = wG+u,\qquad \kappa_1 = vG+p .
$$

Now take an arbitrary holomorphic function $\Pi$ of the three twistor arguments, $\Pi(G,\kappa_0,\kappa_1)\equiv\Pi(G,wG+u,vG+p)$, and impose

$$
\Pi = 0 .
$$

Resolving this algebraic equation for $G(u,v,w,p)$ gives a solution of the complex eikonal — the **class I** solutions. Resolving instead $d\Pi/dG=0$ for $G$ and substituting back gives the **class II** solutions, conjugate to the first. According to the source's earlier work on the eikonal, these two classes exhaust all almost-everywhere analytic solutions. For a general **world function** $\Pi$, the joint system $\Pi=0$, $d\Pi/dG=0$ defines the locus on which $G(\Pi)$ branches — that is, the set on which the four-gradient of the eikonal blows up. Resolving that algebraic system gives the singular set even when $G$ has no closed form, and it is the same locus that carries the singularities of the associated gauge and curvature fields.

**Physical reading.** The twistor is thus not imported from twistor theory; it arises inside the programme as the algebraic variable in which the nonlinear eikonal linearises. This is a genuine structural agreement with the corpus's twistor article at the level of the incidence relation and the spinor, and a genuine divergence at the level of aim: the programme's twistor labels a solution of a **nonlinear** primary equation, whereas Penrose's twistor transform encodes linear massless fields and the conformal group.

## The Generating System and the Gauge Fields

The physically relevant class of differentiable functions is obtained by a **spinor splitting** of the two-sided condition. Writing the function matrix as $F=\{\eta_1,\eta_2\}$ and the right semi-derivative as $R=\{\xi_1,\xi_2\}$ reduces the matrix condition to two equations of the same type,

$$
d\eta_a = \Phi\, dZ\, \xi_a , \qquad a=1,2 ,
$$

with a common field $\Phi$ (the left semi-derivative) transforming as a complex four-vector and $\eta,\xi$ as $SL(2,\mathbb{C})$-spinors. Every solution of the full condition can be built from a solution of a **single** such spinor system with constant proportionality between the two pairs, so the physically nontrivial solutions all come from the **fundamental spinor system**

$$
d\eta = \Phi\, dZ\, \xi .
$$

On the real slice $Z\mapsto X=X^{\dagger}$ with the Minkowski metric this is the **generating system of equations** (GSE) of the programme. It is a system of eight differential equations for six unknown functions — the two spinor components and the four components of $\Phi$ — and is therefore **over-determined**, which is the source of everything that follows.

The over-determination is not a defect but the mechanism. Differentiating the equation and using it again gives an integrability condition whose natural object is a connection. The field $\Phi$ defines a $\mathbb{B}$-valued connection one-form

$$
\Omega = \Psi\, dZ ,
$$

under which the spinor is covariantly constant, $d\xi=\Omega\xi$. This connection corresponds in the four-vector representation to an affine connection of Weyl–Cartan type, in which the Weyl non-metricity vector and the pseudotrace of the torsion are both expressed through $\Psi$. Exterior differentiation gives the integrability condition $R\xi\equiv(d\Omega-\Omega\wedge\Omega)\xi=0$, with the curvature two-form $R$.

The curvature is not zero. For a connection of this special form it is $R=(d\Psi-\Psi dZ\Psi)\wedge dZ$, and requiring $R\xi=0$ for the non-trivial spinor forces the **self-dual part of the curvature to vanish**,

$$
\vec E + i\vec H = 0 ,
$$

on the solutions of the GSE — a property the source calls **weak (anti)self-duality**. The Bianchi identity then implies the free equations for the two pieces of the curvature: Maxwell's equations for its trace part, the electromagnetic field, and Yang–Mills equations for its trace-free part. In this sense the linear field equations are not postulated; they are the **integrability conditions of the primary nonlinear system**. Because the field is $\mathbb{C}$-valued but self-dual, it reduces to an ordinary real electromagnetic field by the algebraic relations $\Im\vec H=\Re\vec E$ and $\Im\vec E=-\Re\vec H$, which is a recomputation-verified equivalence, so the number of degrees of freedom is that of the real field.

Two further features are worth recording because they differ from the standard theory. The GSE is not invariant under the ordinary $U(1)$ gauge transformations $\xi\mapsto e^{i\alpha}\xi$, $\Psi\mapsto\Psi-i\nabla\ln\alpha$; it has instead a **weak gauge symmetry** in which the parameter depends on the coordinates only through the twistor components of the transformed spinor. And the trace-free gauge field is not independent of the electromagnetic one and the spinor; it is expressible through them, and its real and imaginary parts separately do not obey free Yang–Mills equations, because those are nonlinear.

**Physical reading.** This is the part of the programme most directly comparable with the corpus's gauge articles. The corpus derives the Maxwell and Yang–Mills equations from a **postulated** gauge principle, with the connection and curvature put in by hand (*The Gauge Principle in Biquaternionic Form*, *Gauge Curvature and the Bianchi Identity in Biquaternionic Form*). The programme reverses the direction of explanation: the connection and its self-duality are forced by the over-determined nonlinear system, and the linear gauge equations are consequences. Whether that reversal is an advance or a reformulation is a judgement the corpus does not make; it is recorded as the programme's structural claim.

## The Weyl–Cartan Geometry of the Programme

The programme's first full presentation, Kassandrov's 1995 paper *Biquaternion Electrodynamics and the Weyl–Cartan Geometry of Space-Time*, states the same construction geometrically, and it carries three results the later survey only recalls. Its setting is the spinor form of the primary equation. The fundamental spinor system is a parallel-transport condition,

$$
\partial_\nu\psi = \Gamma_\nu(x)\,\psi(x), \qquad \Gamma_\nu(x) = G(x)\,\varsigma_\nu ,
$$

whose $\Gamma_\nu$ is a two-spinor connection of a special type: it is built from the field $G$ alone. (The source's basis is $\sigma_\nu$; it is written $\varsigma_\nu$ here because $\sigma$ is already the principal invariant of the complex three-space below.) Its opening geometric observation is Clifford-theoretic. The biquaternion algebra is the Clifford algebra $\mathrm{Cl}_{3,0}$ — the corpus's own identification, in *The Clifford Algebra Representation* — of real dimension eight, and the source argues that it, and not the sixteen-dimensional $\mathrm{Cl}_{1,3}$, is the natural space-time algebra: the reduction from the full Clifford algebra to a physical four-dimensional space is, in its word, voluntaristic, and the signature of the generator space may be chosen in more than one way. (The corpus's Clifford article makes the same identification and records the competing labelling; what the source adds is the argument for $\mathrm{Cl}_{3,0}$ as primary rather than as the even part of $\mathrm{Cl}_{1,3}$.)

Writing the same equation for the matrix field $F$ and passing to a four-vector representation turns the spinor condition into a covariant-constancy condition $\partial_\nu F^\mu = \Gamma^\mu_{\ \nu\rho}(x)F^\rho$ with the affine connection

$$
\Gamma^\mu_{\ \nu\rho}(x) = 2\bigl(A_\nu\delta^\mu_\rho + A_\rho\delta^\mu_\nu - A^\mu\eta_{\nu\rho} - i\,\varepsilon^\mu{}_{\cdot\nu\rho\alpha}A^\alpha\bigr),
$$

where $A_\mu = 2G_\mu$ is the electromagnetic four-potential identified in the preceding section and the potential fixes the whole connection: its Weyl part and its torsion alike. In this language the integrability condition of the spinor equation is $R_{\mu\nu}\psi = 0$ with $R_{\mu\nu} = \partial_{[\mu}\Gamma_{\nu]} - [\Gamma_\mu,\Gamma_\nu]$, and the weak self-duality of the preceding section is the statement that the self-dual part of $R_{\mu\nu}$ vanishes.

**The unitary field, and why the geometry is real.** The connection just written is complex. Squaring the matrix field to the *unitary field* $U(x)=F(x)F^{*}(x)$ replaces it by a real one. If $F$ obeys the covariant-constancy condition then $U$ obeys the same-shaped condition,

$$
\partial_\nu U^\mu = \Delta^\mu_{\ \nu\rho}(x)\,U^\rho(x), \qquad
\Delta^\mu_{\ \nu\rho}(x) = 2\bigl(a_\nu\delta^\mu_\rho + a_\rho\delta^\mu_\nu - a^\mu\eta_{\nu\rho} - \varepsilon^\mu{}_{\cdot\nu\rho\alpha}b^\alpha\bigr),
$$

where $a_\mu=\Re A_\mu$ and $b_\mu=\Im A_\mu$ are the real and imaginary parts of the potential. Two things happen at once: the Hermitian squaring discards the imaginary part of the connection, leaving a **real** affine connection on space-time; and the imaginary part reappears beside it as a separate field, so that the connection carries a Weyl non-metricity vector $a_\mu$ *and* a torsion pseudotrace $b_\mu$. The source reads the pair physically. The Weyl part $a_\mu$ is the ordinary Coulomb field — which is the reason the electromagnetic field was identified with the real part of $A_\mu$ in the first place — and the torsion part $b_\mu$ is the **magnetic monopole**: for the static solution below, $b_0=b_r=b_\theta=0$ and $b_\phi$ is its potential. Since torsion does not enter the equations of geodesics, the source concludes that a monopole built this way would have **no effect on test-particle motion** and would be "entirely unobservable". That reading of the monopole problem runs the other way from the corpus's *The Magnetic Monopole in Biquaternionic Form*, where the monopole is a source in Maxwell's equation and a charge in the ordinary sense; the two are recorded side by side, neither adopted.

The connection is not idle. The source notes that the same connection had been obtained earlier from physical requirements by Obukhov, Krechet and Ponomariev, and that Stepanov showed it to be the **only** space-time connection compatible with a spinor-bundle structure carrying the conventional covariant spinor derivative. In the algebrodynamical reading that uniqueness is not an input: the connection, its Weyl part, its torsion, and the identification of the parts with the electric and magnetic fields all follow from the generalized Cauchy–Riemann condition alone. It is worth recording that the central object here is one the corpus already uses — the spin connection of *The Covariant Derivative and Gauge Connection in Biquaternionic Form* — reached from the other end.

**The inhomogeneous Lorentz condition.** The integrability conditions of the primary system include, beside the self-duality $\vec P\equiv\vec E+i\vec B=0$, the condition

$$
D \equiv \partial_\mu A^\mu + 2A_\mu A^\mu = 0 ,
$$

an **inhomogeneous Lorentz condition**: not the usual gauge choice $\partial_\mu A^\mu = 0$ but a nonlinear condition with a term quadratic in the potential, and part of the system rather than a gauge. The source observes that $D$ is proportional to the curvature invariant $6\eta^{\mu\nu}R^\alpha_{\ \mu\alpha\nu}$ — so the condition says the effective space has **zero scalar curvature**, and together with the self-duality that it is self-dual. Both the proportionality and the self-duality of the curvature are the source's statements about the solutions of its system; the second is the weak self-duality already recorded above, and neither the proportionality nor the explicit form of the connection was recomputed in this pass, because it holds on the solutions of the primary system and no such solution was constructed here.

**Rigidity, null divisors, and the signature.** The geometric reading also exposes why the non-trivial solutions must be degenerate. If the spinor equation has two linearly independent solutions then $R_{\mu\nu}=0$ — the effective geometry is flat and the field strengths vanish. Non-trivial dynamics therefore requires the two spinors of the splitting to be proportional, and proportionality means $\det F(x)=0$: the primary field takes its values on the **null divisors** of the algebra, the complex light cone, exactly as the degeneracy of the two-sided condition already required. The null fields, the source observes, exist **only on manifolds of indefinite metric signature**. That is the sharpest form of a claim the corpus meets elsewhere as a motivation: in the programme the pseudo-Euclidean signature is **not postulated** but is a necessary condition for a non-trivial field to exist at all, which is the boundary stated in *Why Complexify Spacetime?*. Two further exact facts were used here and verified: the determinant of the matrix variable reproduces the interval, $\det\bigl(\begin{smallmatrix}u&w\\p&v\end{smallmatrix}\bigr)=uv-pw=(z_0)^2-(z_1)^2-(z_2)^2-(z_3)^2$ for $u=z_0+z_3$, $v=z_0-z_3$, $p=z_1+iz_2$, $w=z_1-iz_2$ (checked exactly and on a hundred random complex draws, maximum deviation $4\times10^{-15}$).

## The Local Algebra on a Curved Manifold, and the U-Field

The programme's later conference note *Relativistic Algebra of Space-Time and Algebrodynamics* (Kassandrov and Rizcallah, arXiv:1612.02455, 2016, five pages) adds one ingredient the presentation above does not have: the **local** form of the algebra, in which the multiplication itself becomes a structure attached to a point of a manifold. Everything the note recovers from the 1995 presentation — the generating system, the weak self-duality, the inhomogeneous Lorentz condition, the Weyl–Cartan reading of the connection, the free Maxwell, Yang–Mills and Weyl equations as its consequences — is already recorded above and is not repeated. What is new is the algebra, and it is the part of the programme in which the algebra is treated as a **ring extension** of the kind studied outside it.

**The covariant multiplication law.** The note starts from the four-dimensional associative algebra $G$ proposed by E. Grgin (*Physics Letters B* **431** (1998) 15), whose multiplication is written in the manifestly covariant form

$$
(a\circ b)_\mu = a_\mu\,(b^\rho e_\rho) + b_\mu\,(a^\rho e_\rho) - e_\mu\,(a^\rho b_\rho) \pm i\,\varepsilon_{\mu\nu\rho\lambda}\,a^\nu b^\rho e^\lambda ,
$$

with the Minkowski metric $\eta_{\mu\nu}$, the Levi-Civita symbol $\varepsilon$, and a **distinguished element** $e=\{e_\mu\}$ of $G$ constrained by $e^\mu e_\mu=1$, so that $a\circ e=e\circ a=a$ and $e$ is the unit. The note's point about the record is that with $e=(1,0,0,0)$ this law *is* the multiplication of the biquaternion algebra $\mathbb{B}$, so that Grgin's $G$ is isomorphic to $\mathbb{B}$ — an identification, the note says, overlooked in the paper that introduced the algebra. It was checked here and it is exact. Representing the algebra on $\mathbb{C}^2$ by $\sigma_0=I$ and the Pauli matrices, with $\eta=\mathrm{diag}(1,-1,-1,-1)$ and $\varepsilon_{0123}=+1$: on a hundred random complex pairs the law with the **lower** sign reproduces the $2\times2$ matrix product to $2\times10^{-15}$, and the law with the **upper** sign reproduces the *reversed* product $b\cdot a$ to the same accuracy. The two signs are therefore the algebra and its opposite — in the source's words the signs "correspond to the left or right forms of the (bi)quaternion algebra" — and the isomorphism with $\mathbb{B}$ holds either way.

Two readings in the printed note must be fixed before the law can be used. First, the $\pm$ of the general law and of the space-like block $\sigma_a\circ\sigma_b=\delta_{ab}e\pm i\varepsilon_{abc}\sigma_c$ are **not** synchronized: the block with the upper sign is the Pauli product $\sigma_a\sigma_b=\delta_{ab}e+i\varepsilon_{abc}\sigma_c$, and the law produces it with the **lower** sign (checked exactly on all nine pairs of space-like units; the upper sign gives the negative of it). Second, the last term must be read with $e^\lambda$ **contravariant** — the reading under which the note's own Lorentz-covariance claim is true — and not with $e_\lambda$. On a hundred random Lorentz transformations — boosts, three-rotations and their products — acting on $a$, $b$ and $e$ together, the product transforms as a covector with residual $8\times10^{-15}$ when the contraction is with $e^\lambda$, and fails by order $20$ when the symbol is misread as $e_\lambda$. The law is thus "manifestly Lorentz invariant" in the precise sense that its coefficients are the invariant tensors $\eta$ and $\varepsilon$ and its last contraction is with the contravariant unit; the covariance of the product follows, and was verified in that strong form. Its automorphisms at fixed $e$ include the three-rotations, as the source states (checked on a hundred rotations).

**The local algebra and the U-field.** The covariant form is what allows the algebra to be attached to a manifold. Introduce a tetrad $h^\alpha_{\ \mu}(x)$, $\alpha=0,1,2,3$, and the **local $L$-algebra** whose basis vectors are the tetrad legs in the abstract basis $\sigma_\alpha$,

$$
\Sigma_\mu(x) := h^\alpha_{\ \mu}(x)\,\sigma_\alpha ,
$$

so that the multiplication table keeps the shape of the flat one, with the Minkowski metric replaced by the metric the tetrad induces,

$$
g_{\mu\nu}(x) := h^\alpha_{\ \mu}(x)\,h^\beta_{\ \nu}(x)\,\eta_{\alpha\beta} ,
$$

and the unit element replaced by the unit **field** $E_\mu(x) := h^\alpha_{\ \mu}(x)\,e_\alpha$, constrained by $g^{\mu\nu}E_\mu E_\nu=1$. The construction exposes a fact the flat presentation hides: the existence of the local algebra on a four-manifold requires, beside the metric, a **unit time-like vector field** — the source's *U-field* — because the unit element of the algebra is a field. The source reads the U-field physically as the flow of matter ("its physical interpretation may be related to the flow of matter") and observes that the same data appear in Weyl geometry, where a metric is accompanied by a non-metricity one-form. The U-field here is not the corpus's **unitary field** of the section above: there $U=FF^\dagger$ is built *from* the primary field and the geometry follows; here the U-field belongs to the geometry and the algebra is attached to it. Associativity of the local algebra was checked here for arbitrary unit U-fields (residual $1.3\times10^{-13}$ over a hundred random draws, both signs), which is what makes the structure functions below well defined.

**The effective metric, and a metric built from the multiplication table.** Two metrics accompany the local algebra. The first the note calls the **effective metric**,

$$
\tilde g_{\rho\lambda} := 2E_\rho E_\lambda - g_{\rho\lambda} ,
$$

whose flat case the source calls "rather surprising" and which is exact: for $g=\eta$ and $E=(1,0,0,0)$, $\tilde g=\mathrm{diag}(1,1,1,1)$ — the effective metric of the flat limit is the **four-dimensional Euclidean** metric, not the Minkowski one, and the note observes that the Euclidean structure survives the generalization to a curved manifold. Two elementary properties follow from the definition and fix what the object is: the map $g\mapsto 2E\otimes E-g$ is an **involution**, so $\tilde g$ is the reflection of $g$ in the $E$ direction; and $\tilde g=g$ would require $g_{\mu\nu}=E_\mu E_\nu$, a rank-one form, so no metric is a fixed point and the two are never degenerate together.

The second metric is algebraic. The **structure functions** of the local algebra are defined by $\Sigma_\mu\circ\Sigma_\nu=C^\rho_{\ \mu\nu}\Sigma_\rho$, so that, reading the last term with the raised symbol,

$$
C^\rho_{\ \mu\nu} = \delta^\rho_\mu E_\nu + \delta^\rho_\nu E_\mu - E^\rho g_{\mu\nu} \pm i\sqrt{-g}\,\varepsilon^\rho{}_{\cdot\mu\nu\lambda}E^\lambda ,
$$

and from them the source forms

$$
g^*_{\mu\nu} := \tfrac14\, C^\beta_{\ \mu\alpha} C^\alpha_{\ \nu\beta} .
$$

The note's "**remarkable coincidence**" is that $g^*$ is the same tensor as the effective metric $\tilde g$. The check made here is stronger than the source's own hedge: the source states the equality "at least in the case $g=|g_{\mu\nu}|=|\eta_{\mu\nu}|=-1$", whereas for $g=\eta$ and an **arbitrary** unit U-field — a hundred random draws, both signs of the $\varepsilon$ term — the identity $g^*_{\mu\nu}=\tilde g_{\mu\nu}$ holds to $4\times10^{-15}$. The check pins the reading once more: it holds with $\varepsilon^\rho{}_{\cdot\mu\nu\lambda}E^\lambda$, the raised symbol contracted with the contravariant $E^\lambda$, and fails by order $4$ if either index is read the other way. The content of the coincidence is that $\tilde g$ is also the metric the connection below is built from, while $g^*$ is computed from the multiplication table alone: the same tensor arrives twice, once from the geometry and once from the algebra. The source reads its invariance under the automorphisms of $L$ as the reason it can, and draws the suggestion that the local algebra already knows the effective metric the fields live on. This is a mathematical identity, not a dynamical statement: nothing in the note makes $\tilde g$ the physical metric.

**The induced connection, and its non-metricity.** The note's remaining new ingredient is the curved form of the differentiability condition. Where the flat case writes $dF=\Phi(X)\circ dX\circ F(X)$ with the ordinary differential, the curved case writes

$$
\mathrm{D}F = \Phi(Z)\circ dX\circ F(Z) ,
$$

with $\mathrm{D}$ the covariant differential with respect to $g$ — that is, with respect to the Levi-Civita connection $\gamma$ — and then, exactly as in the flat case, the condition says that a vector field is **covariantly constant** with respect to an induced connection $\Gamma$, which splits as

$$
\Gamma = \gamma + G ,
$$

with $G$ of the same shape as the flat connection recorded above, $E$ and $g$ replacing $e$ and $\eta$:

$$
G^\rho_{\ \nu\mu} = \delta^\rho_\nu A^\alpha(2E_\mu E_\alpha - g_{\mu\alpha}) - A_\nu g^{\beta\rho}(2E_\mu E_\beta - g_{\mu\beta}) \pm i\sqrt{-g}\bigl\{\varepsilon^\rho{}_{\cdot\alpha\nu\gamma}E_\mu + \varepsilon^\rho{}_{\cdot\alpha\mu\gamma}E_\nu - \varepsilon^\rho{}_{\cdot\nu\mu\gamma}E_\alpha + \varepsilon_{\alpha\nu\mu\gamma}E^\rho\bigr\}E^\gamma A^\alpha + A^\rho(2E_\nu E_\mu - g_{\nu\mu}) .
$$

Two of its properties are already familiar from the 1995 paper and are now seen to be the general case. First, $G$ is **not symmetric in its lower indices**, so the induced connection has **torsion** — the totally skew-symmetric part carried by the $\varepsilon$ terms, which is the part the preceding section reads as the magnetic monopole. Second, the covariant derivative of the metric does not vanish:

$$
\nabla_\rho g_{\mu\nu} = -2\,g_{\mu\nu}\,\tilde A_\rho , \qquad \tilde A_\rho := (2E_\rho E_\lambda - g_{\rho\lambda})A^\lambda = \tilde g_{\rho\lambda}A^\lambda ,
$$

a **Weyl-type non-metricity** whose vector is not the potential $A_\rho$ itself but the potential read through the effective metric, $\tilde A=\tilde g A$. In the flat case this was checked exactly — residual $0$ over ten random potentials — with one convention pinned: the printed connection must be read with the derivative index in the **last** position, and with the lower pair transposed the identity fails, which it must, since the connection's failure of symmetry in that pair is precisely its torsion. For $E=(1,0,0,0)$ the effective metric is Euclidean, so $\tilde A$ is the covariant potential with the signs of its three space-like components reversed, and the Weyl vector of the induced geometry is not the potential the primary equation is written with. The comparison with the 1995 reading is the reason for recording the formula: there the non-metricity vector is the potential $A_\mu$ itself, here it is $A_\mu$ contracted with the metric into which the U-field deforms $g$, and the flat case is the case in which the difference is visible.

**What the note leaves open.** The note states its own programme for the construction: the integrability conditions of the $L$-differentiability equations "might impose restrictions not only on the vector field $A_\mu$, but also on the metric $g_{\mu\nu}$ as well as the unit vector field $E_\mu$", and if they do, the physical geometry would be determined "in a purely algebraic way". That analysis is explicitly "left for future work". The corpus records the hope and not the result: the local algebra, as the note uses it, is a language in which a given metric and a given U-field may be written, and the note exhibits no condition that selects either. The section records an extension of the programme's algebra rather than a new physical claim, and it changes nothing in the corpus's reading of the programme.

## The Yang–Mills Triplet and the Electromagnetic Modulus

The trace-free part of the spinor connection is a gauge field in its own right, and the source exhibits it explicitly. Splitting

$$
\Gamma_\nu(x) = \tfrac12 A_\nu(x) + N_\nu(x)
$$

into trace and trace-free parts, the trace-free part $N_\nu = N^a_{\ \nu}\varsigma_a$ is expressed **linearly** in the electromagnetic potential:

$$
N^a_{\ 0} = A_a, \qquad N^a_{\ b} = \delta_{ab}A_0 - i\varepsilon_{abc}A_c .
$$

A single complex four-vector $A_\mu$ therefore carries both the electromagnetic potential and a complex triplet of matrix potentials. The strength of the triplet field is $L_{\mu\nu}=L^a_{\ \mu\nu}\varsigma_a=\partial_{[\mu}N_{\nu]}-[N_\mu,N_\nu]$, and it inherits the self-duality, $L_{\mu\nu}+\tfrac{i}{2}\varepsilon_{\mu\nu\rho\lambda}L^{\rho\lambda}=0$ on the solutions, from which the Bianchi identity gives the Yang–Mills equation $\partial_\nu L^{\mu\nu}=[N_\nu,L^{\mu\nu}]$.

The link between the two fields is a determinant. The curvature matrix splits as $R_{\mu\nu}=(\text{trace part})+L_{\mu\nu}$, with the trace part proportional to the electromagnetic field strength $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ (the index-carrying strength, to be read apart from the matrix field $F$ itself), and the condition $\det R_{\mu\nu}=0$ — which holds because the non-trivial spinor lies in its kernel — becomes an algebraic relation between the two invariants. In components the source writes it as

$$
L^a_{\ \mu\nu}L^a_{\ \mu\nu} = (F_{\mu\nu})^2 ,
$$

so the electromagnetic field strength is the **modulus of the Yang–Mills triplet** in the complexified isotopic three-space: the abelian field is not a separate object but the length of the non-abelian one. The determinant identity behind this is elementary and exact — for a $2\times2$ matrix $\lambda I + L$ with $L$ traceless, $\det(\lambda I+L)=\lambda^2-(L^1)^2-(L^2)^2-(L^3)^2$, verified symbolically here — so the relation is one of proportionality, the coefficient being fixed only once the antisymmetrisation convention and the normalisations of the potentials and the field strength are fixed. Substituting the source's own definitions, $R_{\mu\nu}=\partial_{[\mu}\Gamma_{\nu]}-[\Gamma_\mu,\Gamma_\nu]$ with $\Gamma_\nu=\tfrac12A_\nu I+N_\nu$ and $\partial_{[\mu}\Gamma_{\nu]}$ read as $\tfrac12(\partial_\mu\Gamma_\nu-\partial_\nu\Gamma_\mu)$, gives the trace part $\tfrac14F_{\mu\nu}I$ and hence $\sum_a(L^a_{\ \mu\nu})^2=\tfrac1{16}(F_{\mu\nu})^2$, whereas the source prints coefficient one; the printed coefficient is therefore read here as a statement of the **modulus relation** and not as a numerically normalised identity, and the factor between the two is left unreconciled. Unlike the electromagnetic field, the source observes, a complex Yang–Mills field cannot be split into real and imaginary parts, because the Yang–Mills equation is nonlinear; the reality that self-duality supplies to electromagnetism is not available to the non-abelian field.

**Physical reading.** This is the most concrete of the programme's unification statements, and the most literal: the electromagnetic potential is the trace part of a biquaternion connection and the gauge triplet is its trace-free part, with the abelian and non-abelian field strengths tied by a determinant. It is not the corpus's *The Yang–Mills Equation in Biquaternionic Form*, where a Yang–Mills field is packaged after being given independently; here the non-abelian field has no independent existence, and the electromagnetic field is the modulus of the triplet. The claim is the source's, conditional on the primary system, and it is recorded as the programme's rather than as a result of this corpus.

## The Kerr Equation and the Shear-Free Congruences

Eliminating the potentials from the GSE leaves a system for the principal spinor alone. Multiplying the GSE by the orthogonal spinor and using the skew symmetry of the spinor norm gives a system whose restriction to the real slice is the classical equation of a **shear-free null congruence** of rays,

$$
\xi^B\xi^C\nabla_{AB}\xi_C = 0 .
$$

The source notes that the GSE system is more rigid than the shear-free condition only in the gauge fixing of the spinor, and equivalent to it for the ratio of the spinor components. The general solution of the shear-free condition on Minkowski space is the **Kerr theorem**: the congruence is given by an arbitrary homogeneous function of the twistor arguments, through the implicit algebraic equation $\Pi(\xi,Z\xi)=0$. For the GSE the corresponding equation for the ratio $G$ of spinor components is the **Kerr equation**

$$
\Pi(G,\,wG+u,\,vG+p) = 0 ,
$$

in which $\Pi$ is an arbitrary holomorphic function of three complex twistor variables. This is the same $\Pi$ as in the eikonal section seen from the field side, and the equivalence is exact: the solutions satisfy the pair of partial differential equations

$$
\nabla_wG = G\,\nabla_uG , \qquad \nabla_vG = G\,\nabla_pG ,
$$

and multiplying them gives back the complex eikonal, while differentiating them gives the linear wave equation for $G$,

$$
(\nabla_u\nabla_v - \nabla_w\nabla_p)\,G = 0 .
$$

Consequently every $C^2$ function $\lambda(G)$ is harmonic on the solutions, since the eikonal supplies the quadratic term and the wave equation the linear one. In this pass the whole chain was recomputed on an explicit solution of the quadratic Kerr equation $\Pi=wG^2+(u-v)G-p$: the two first-order equations, the complex eikonal, the wave equation, and the harmonicity of $\ln G$ all hold to finite-difference accuracy.

The electromagnetic field strengths are then the second derivatives of $\ln G$,

$$
F_{00}=\nabla_u\nabla_p\ln G,\quad F_{11}=\nabla_v\nabla_w\ln G,\quad F_{01}=\nabla_w\nabla_p\ln G ,
$$

so that Maxwell's equations for the field follow from the harmonicity of $\ln G$. The sharpest form of the result is the source's representation of the field through the twistor variables,

$$
F_{AB} = \frac{1}{P}\,\Pi_{AB} - \frac{1}{P}\,\frac{d}{dG}\left(\frac{\Pi_A\Pi_B}{P}\right), \qquad P := \frac{d\Pi}{dG},
$$

which the source presents as having no analogue in the literature: the field of a solution is computed from the **generating function alone**, without solving the Kerr equation.

A further structure attaches to the congruence. The flat metric can be deformed into a **Kerr–Schild metric** $g_{\mu\nu}=\eta_{\mu\nu}+h\,k_\mu k_\nu$ with the null congruence $k$ as its repeated principal direction, and for generating functions linear in the twistor arguments the metric satisfies the **electrovacuum Einstein–Maxwell** equations of Debney, Kerr and Schild. The locus on which the congruence's $G$ branches — the condition $P=d\Pi/dG=0$ — is simultaneously the singularity of the effective curvature, of the electromagnetic field, and of the Yang–Mills field. The programme reads this coincidence as the statement that a **particle is a common singularity of all the associated fields**, and it is the geometric heart of the particle reading.

**Physical reading.** The Kerr–Schild deformation and the Kerr theorem are classical general-relativistic objects, and the corpus's *Curved Spacetime and the Biquaternion Framework* describes the framework's own relation to curvature separately. What is new here is not the geometry but the **generation**: the metric, the electromagnetic field and the Yang–Mills field all descend from one holomorphic function of a twistor, and their singularities coincide.

## Particle-Like Solutions and the Self-Quantized Charge

The programme's headline claim is that the singular solutions of the GSE have **quantised electric charge**. The mechanism is explicit and rests on the self-duality of the curvature together with the weak gauge invariance of the GSE: the two conditions restrict the admissible charge of the electromagnetic field associated with any GSE solution to

$$
q = \frac{N}{4}, \qquad N\in\mathbb{Z},
$$

in the dimensionless units of the programme. The source states that the quantization has both topological and dynamical reasons, the dynamical one being the over-determined structure of the GSE itself, and it points to the general theorem proved in its own later papers.

The **fundamental static solution** is the one that makes the claim concrete. It is generated by the function

$$
\Pi = G\,\kappa_0 - \kappa_1 + 2ia, \qquad a=\mathrm{const}\in\mathbb{R},
$$

which contains no time coordinate. Resolving the quadratic Kerr equation and restricting to real Minkowski space gives an explicit $G$, and the associated electromagnetic field has a **ring singularity** of radius $a$, the only admissible value of electric charge $|q|=\tfrac14$, and magnetic and electric moments proportional to $qa$ and $qa^2$. For $a=0$ the solution degenerates to the stereographic projection $S^2\to\mathbb{C}$, and the field is the Coulomb field with the Reissner–Nordström metric. For $a\neq0$ the field and metric reproduce those of the **Kerr–Newman** solution. With the known gyromagnetic ratio $g=2$ of that solution, the ring singularity is the programme's classical model of the electron.

**The static solution in closed form, and the stereographic reading.** The 1995 presentation gives the static solution explicitly, and it is the stereographic map written as a function. The two static eikonal solutions are

$$
f^+ = \frac{x_1+ix_2}{r+x_3} = \tan\frac{\theta}{2}\,e^{i\phi}, \qquad
f^- = \frac{x_1-ix_2}{r-x_3} = \cot\frac{\theta}{2}\,e^{-i\phi},
$$

the stereographic projection $S^2\to\mathbb{C}$ from the south and the north pole respectively. Each satisfies the static eikonal exactly, and this was recomputed: for $f^+$ the sum $(\partial_1 f)^2+(\partial_2 f)^2+(\partial_3 f)^2$ vanishes identically (verified symbolically in the present pass, together with $\lvert f^+\rvert^2=(r-x_3)/(r+x_3)$). Integrating the spinor system with $h=(f^\pm)^2$ gives the complex potential

$$
A_0 = \pm\frac{1}{2r}, \qquad A_r = -\frac{1}{2r}, \qquad A_\theta = \mp i A_\phi = -\frac{1}{2r}\cot\theta \pm \frac{3}{2r\sin\theta},
$$

whose physical (real) part is the Coulomb field: the angular and magnetic components cancel and $E_r$ is the only non-vanishing component, with the charge fixed at $q=\pm1$ in this paper's normalisation. (The later papers of the programme write the elementary value as $\tfrac14$ in their own normalisation, and the 1998 restatement below makes that normalisation self-consistent; the two normalisations are kept apart and are not merged.) The source prints $E_r=\pm1/r$; the printed potential decays as $1/(2r)$, whose negative radial derivative is $\pm1/(2r^2)$, so the printed power of $r$ is one lower than the derivative of the printed potential, while the physical content — the Coulomb $1/r^2$ decay — is unaffected. The mechanism of the quantisation appears in this paper in its plainest form: the generalized Cauchy–Riemann equations are **not** invariant under the scaling $A\to\lambda A$ that the linear Maxwell equations admit, so the admissible potentials come in a fixed discrete set of scales, and the source expects the deeper reason to be topological.

**The dion, and the normalisation of the charge.** The 1998 presentation of the same solution gives the potentials in a form that is self-consistent and fixes the elementary value. In the coordinates of the preceding paragraph the unisingular solution is

$$
A_0 = \pm\frac{1}{4r}, \qquad A_r = -\frac{1}{4r}, \qquad A_\phi = \pm i A_\theta = \frac{i}{4r}\tan^{\pm1}\frac{\theta}{2} ,
$$

with $A_r$ and $A_\theta$ of pure-gauge type, and the complex field strengths are

$$
E_r = \pm\frac{1}{4r^2}, \qquad H_r = \pm\frac{i}{4r^2} ,
$$

the electric field being **pure real** and the magnetic field **pure imaginary**. This is the Coulomb field of a charge $q=\pm\tfrac14$, and the potential now differentiates to the strength printed, $-\partial_r(\pm1/(4r))=\pm1/(4r^2)$, exactly. The 1995 presentation's printed pair $A_0=\pm1/(2r)$ with $E_r=\pm1/r$ — the one the paragraph above flags as inconsistent — carries the same solution in a different scale, and the 1998 presentation recorded here removes the printed inconsistency: with $A_0=q/r$ and $q=\pm\tfrac14$ the potential and the strength agree exactly. It is the value $\tfrac14$ that the later papers of the programme carry, and the two normalisations are kept apart rather than merged (a factor two separates the two potentials, so a formula must not be moved between them). The magnetic charge is $m=\pm i/4$: the singular solutions of the self-dual system are **dions**, carrying electric and magnetic charge of equal magnitude, and the source states this as a necessity and not an option — "charged singular solutions, if they exist, should be dions".

**The two sectors, and why the second is invisible.** The complex field splits into a real part and an imaginary part, and the split is the sharpest physical statement in the 1998 paper. The real-part fields carry the Coulomb field, the magnetic dipole moment and the electric quadrupole moment; the imaginary part carries the **magnetic charge** and the **electric dipole moment**, and the source calls these terms "phantom". Geometrically the imaginary sector contributes only to the torsion of the "Minkowski projection" of the complex connection, and because that torsion is totally skew-symmetric (of Rodichev type) it does not enter the equations of geodesics. The conclusion is that magnetic charges and electric dipole moments built this way would be **unobservable** — the same conclusion the programme draws for the monopole alone in the article *The Magnetic Monopole in Biquaternionic Form*, here extended to the electric dipole. It is a strong claim and the corpus does not adopt it; it is recorded because it is the programme's answer to why a self-dual system, which produces magnetic charge whether or not it is wanted, is not in conflict with the absence of observed magnetic charge.

The same mechanism produces other particle-like solutions: an axisymmetric solution generated by $\Pi=\kappa_0\kappa_1+b^2G^2$ describes two point-like singularities of opposite elementary charge in **uniformly accelerated** (hyperbolic) counter-motion, with the field of the classical Born solution; for imaginary $b=ia$ the singular locus is a neutral ring of radius $a$ that expands into a self-intersecting torus. More complicated generating functions give figure-eight singularities, a helix-like singular locus, the annihilation of a pair of oppositely charged point singularities, and a photon-like singularity in the form of crossed rings moving uniformly at the speed of light. The singular locus of a general solution is one-dimensional — a string or a collection of closed curves — and for particle-like solutions it is bounded in the physical three-space.

**The ring family.** The ring of the fundamental solution is the first of an explicit one-parameter family. For the static generating functions $\Pi=G^n/H$, with $H=wG^2+2(z+ia)G-\bar w$ and $w=x-iy$, $\bar w=x+iy$ (the $w,p$ of the notation table, $p=\bar w$; here $z$ is the third Cartesian coordinate, the table's $z_3$), the class-II singular locus is obtained by eliminating $G$ from $P=0$ together with the class-II branching condition

$$
\Lambda:=\frac{d^2\Pi}{dG^2}=0 .
$$

For this $\Pi$ the pair reduces to $f:=nH-GH'=0$ and $f'=(n-1)H'-GH''=0$, and eliminating $G$ between them gives

$$
(n-1)^2(z+ia)^2+n(n-2)(x^2+y^2)=0 .
$$

The imaginary part forces $z=0$ and the real part gives $x^2+y^2=R_n^2$ with

$$
R_n=\frac{a(n-1)}{\sqrt{n(n-2)}},\qquad n\ge3 .
$$

So the family is a sequence of rings, $R_3=2a/\sqrt3$ decreasing to $R_\infty=a$. The elimination and the radius were recomputed symbolically here for $3\le n\le7$ and hold. The two lowest cases are exceptional. For $n=1$ the solution has a pole on the ring $z=0$, $x^2+y^2=a^2$ but branches only at the origin, so it is a point singularity. For $n=2$ one gets $\Pi=\bar w/r_*^2$ with $r_*^2=x^2+y^2+(z+ia)^2$, which has no branching point on the real slice at all; for $a=-1$ it reads

$$
\Pi=\frac{i\,(x+iy)}{2z+i\,(r^2-1)},\qquad r^2=x^2+y^2+z^2 ,
$$

which was checked here to be the standard **Hopf map**. The Hopf fibration therefore enters the programme as the second member of this family of eikonal solutions, not as an inserted topological construction; its bundle-theoretic reading belongs to *The Hopf Fibration and the Biquaternion Gauge Bundle*.

**The complex-shifted ring, its moments, and the programme's one numerical prediction.** The ring is not found by solving a new system: it is the point solution translated in the complex direction, $z\mapsto z+ia$, which is a symmetry of the UEqs. Applied to the Coulomb potential this gives the **Appel solution**

$$
A_0 = \frac{q}{r_*}, \qquad r_*^2 = x^2+y^2+(z+ia)^2 ,
$$

the same $r_*$ that governs the $n=2$ member of the ring family. Writing $z=r\cos\theta$ and expanding in $a/r$, the real part of the potential is

$$
\Re A_0 = \frac{q}{r}\left(1 - \frac{a^2}{2r^2}\bigl(3\cos^2\theta-1\bigr)\right) + O(a^4) ,
$$

which was recomputed here symbolically to this order; it is exactly the potential of a point charge $q$ carrying an axisymmetric **electric quadrupole**. The source's asymptotic field components, in the present article's notation for the field radius $r$, are

$$
E_r \simeq \frac{q}{r^2}\left(1 - \frac{3a^2}{2r^2}(3\cos^2\theta-1)\right), \qquad
E_\theta \simeq -\frac{3qa^2}{r^4}\cos\theta\sin\theta , \qquad
H_r \simeq \frac{2qa}{r^3}\cos\theta , \qquad
H_\theta \simeq \frac{qa}{r^3}\sin\theta .
$$

The two electric expressions and the quadrupole coefficient were checked here and hold; the magnetic pair is exactly the dipole field of a moment $\mu=qa$ ($H_r=2\mu\cos\theta/r^3$, $H_\theta=\mu\sin\theta/r^3$). Reading the multipole moments off the potential, $\Phi=q/r+\vartheta(3\cos^2\theta-1)/(4r^3)$, gives

$$
\mu = qa, \qquad \vartheta = -2qa^2 .
$$

The last step is the programme's only numerical prediction, and it is a single algebraic identity. If the ring radius is fixed by requiring the magnetic moment to take the Dirac value, $|a|=\hbar/2Mc$ and $\mu=qa=e\hbar/2Mc$, then the quadrupole moment is forced to

$$
\vartheta = \frac{e\hbar^2}{2M^2c^2} .
$$

The source states this as a conjecture and explicitly calls it speculative, while noting that the possibility of an experimental test could be discussed; the corpus records it in that status. It is placed here because it is the one place in the programme where a free parameter is used up by a known quantity and what remains is a number rather than a structure.

**A worked multiparticle example.** The source's test case for the dynamics uses the fourth-order generating function

$$
\Pi=G^2\kappa_0^2+\kappa_1^2-b^2G^2=0,\qquad b=\mathrm{const}\in\mathbb{R},
$$

whose four modes make the caustic structure explicit. At $t=0$ the singular locus is a pair of point singularities of opposite and equal elementary charge together with a neutral two-surface that encloses them — the intersection of all four branches, which the source calls a cocoon — while each point charge is formed by the intersection of a particular pair of the locally radial, Coulomb-like congruences. At $t=b/\sqrt2$ the two point singularities meet at the origin and cancel, modelling annihilation, and the event is accompanied by the emission of a singular light-like wavefront, a further two-dimensional component of the caustic set. This is the programme's clearest demonstration that the caustics can be bounded, singly charged and able to merge and disappear. The source states the example as an analytic computation; it is recorded here as the source's, not recomputed in this pass.

**The catastrophe-theory reading.** The source frames this part of the picture in the language of **catastrophe theory**: what evolves is the caustic set, and a *perestroika* of that set — a change of its topological type, such as the cocoon's collapse to a pair of points and their cancellation — is read as a **mutual transmutation of particles**. The bisingular solution, in which two oppositely charged point singularities interact axisymmetrically with the elementary charge of the unisingular solution, is presented as the evidence that the framework admits such processes; the general interaction problem, together with the intermediate toroidal resonance, is announced as future work. This is the furthest the programme is from anything the corpus can compare with: the corpus has no dynamics of particle transmutation, and the reading is recorded as the programme's programme, not as a result.

**The quadratic family, the figure-eight, and the wave-like helix.** The particle-like solutions have closed forms, and the source proves one exhaustiveness statement about them: for generating functions **quadratic** in $G$ the axisymmetric solutions are, up to Poincaré transformations, the static Kerr-like solution of the preceding section and the nonstationary bisingular solution generated by $\Pi=\kappa_0\kappa_1+b^2G^2$, together with its toroidal or double-ring modifications. The **figure-"8"** is the remaining quadratic member, generated by $\Pi=\kappa_0\kappa_1-a^2G^2$: eliminating $G$ from $\Pi=0$ and the caustic condition $P=0$ gives a singular set whose $t=0$ section is a flat figure-eight curve, and its field is **neutral** (total charge zero) and **null**, $\vec E^2-\vec H^2=0$ with $\vec E\cdot\vec H=0$, falling as $r^{-4}$ away from the singularity. It is the programme's most explicit "particle" that is not a ring.

The wave-like solutions give the most concrete object in the material. When the generating function depends on a single twistor argument, $F(G,\kappa_0)=0$, the initial distribution $G(u)$ is free on the axis, and the monochromatic choice

$$
G-A\exp\!\left[i\varpi\,\kappa_0\right]=0
$$

is solved in closed form by the **Lambert function**,

$$
G=\frac{i\,W\!\left(-iA\varpi\,w\,e^{i\varpi u}\right)}{\varpi w},
$$

with $W$ the principal branch of $W(z)e^{W(z)}=z$. (The source's frequency $\Omega$ is written $\varpi$ here, because $\Omega$ denotes the connection in this article; the source also writes the twistor argument as $\bar wG+u$, its $\bar w$ being this article's $w$, part of the convention clash flagged once above.) The singular set of this solution is a **neutral helix of radius $1/(\varpi A e)$ and lead $2\pi/\varpi$**, propagating along the $z$-axis at the speed of light, with mutually orthogonal transverse fields that fall as $1/r$ from the axis and are defined only up to an overall sign. The radius and the lead follow from the caustic condition in one line. On the solution the defining equation gives $A\exp[i\varpi\kappa_0]=G$, so

$$
\frac{dF}{dG}=1-i\varpi w\,G=1+W ,
$$

and $P=0$ therefore forces $W=-1$, whence $|w|=1/(eA\varpi)$. The closed form and the caustic consequence were recomputed here and hold to better than $5\times10^{-15}$ over a hundred random parameter draws. A helix of definite radius and pitch in closed form is the sharpest answer the material gives to the question of what a biquaternionic "particle" looks like, and it is recorded here as a solution of the programme's primary system, not as a physical electron model.

The source is careful about what this does and does not mean, and the corpus should be too. The quantization is **not postulated but derived**, which is the programme's strongest claim and the one that addresses the corpus's stated open boundary; but the derivation fixes the charge **given the singularity structure**, and it is the *over-determined primary system plus self-duality* that does the work, not a new dynamics. In the version of the theory invariant under the duality transformations it is the *effective magneto-electric* charge that is quantized, and the programme states that in that accounting the **magnetic monopole problem also receives a natural solution**. The elementary charge is identified with the minimal admissible value $|q|=\tfrac14$ of the fundamental static solution, which is weaker than deriving the numerical value of the electron's charge from nothing, and the corpus must not read the phrase "self-quantized" as more than that.

Three further consequences are recorded because they mark the programme as genuinely non-standard. The primary system is **not Lagrangian** and its solutions are subject to **selection rules** — constraints on admissible charge, spin and other characteristics — that do not follow from the linear field equations. The **superposition principle breaks**: a sum of GSE solutions satisfies the linear Maxwell equations but not the primary GSE. And the over-determined primary system is **not invariant under spatial reflection** nor, perhaps, under time reversal; these symmetries are restored only at the level of the integrability conditions, that is, at the level of Maxwell and Yang–Mills. The source presents this as an ability to describe parity violation and time irreversibility in principle.

**Contrast with the corpus.** *The Magnetic Monopole in Biquaternionic Form* ends its quantisation discussion by saying that the biquaternion framework is "silent where the standard theory is silent" — it re-expresses the Dirac condition $eg=2\pi n\hbar c$ but does not derive the existence of the quantum of charge. The algebrodynamical programme claims exactly that missing derivation, for a nonlinear equation that this corpus does not use. The honest reading is therefore: the corpus's silence is a property of the **linear** framework it writes, and the programme's claim is a claim about a **different, nonlinear** primary equation. It is the clearest example in the material of a programme that addresses the charge-quantisation boundary, and it should be recorded as such — and as the programme's claim, not as a result of this corpus.

## Multivalued Fields and the World Function

To describe the Universe as a whole the programme must choose a representative solution, and it chooses a class-I solution generated by the Kerr constraint, because that is the class carrying the geometric and gauge structures. The choice pulls the class-II conjugate back into the scheme. Taking $G$ from $d\Pi/dG=0$ and substituting it into $\Pi=0$ makes the function $\Pi(G(X))$ vanish on the singular locus of the class-I field — that is, on its characteristic hypersurface — and, being a class-II solution, it satisfies the eikonal. The eikonal field therefore plays two roles at once: it is the fundamental physical field as a class-I solution, and the characteristic field as a class-II solution, describing the locus at which the derivatives of the fundamental field are discontinuous. This double role is why the source calls $\Pi$ the **world function**.

The second structural point is that the principal field $G$ is not single-valued. If $\Pi$ is irreducible, its defining algebraic equation has in general more than one root, and the generic solution is a multivalued complex function; a locally chosen continuous branch is a **mode**, and each mode carries its own null congruence and its own set of associated fields. For a world function that is an algebraic surface in projective twistor space the number of modes is finite, and a finite number of locally distinct null congruences then exists at each point of space-time. The programme insists that this multivaluedness is not a defect. It argues that in a theory where the fields *constitute* the particles rather than merely describing them, fields need not be univalued; that univaluedness is the exception rather than the rule for solutions of partial differential equations, the familiar $\delta$-type distributions being the more artificial object; and that imposing univaluedness of a *locally chosen mode* of $G$ and of the electromagnetic field, away from the branch points, is precisely what yields the quantisation of the charge of the singularities. That is a second, more topological route to the $q=N/4$ of the preceding section, distinct from the self-duality argument, and the source attributes it to its own later papers. The resulting picture is what the source calls a dualistic *corpuscular–field complex*, in which all the particles of the Universe belong to a single object.

Recording this is worth doing because it marks an assumption the corpus has never had to state: the corpus's own articles use single-valued fields on $\mathbb{B}$, the one multivalued object in its repertoire being the biquaternionic logarithm. A neighbouring programme *requires* multivaluedness for its particle picture to hold together, and turns the requirement into the source of a discrete spectrum rather than an embarrassment. The corpus takes no position on the claim; the multivaluedness, the univaluedness argument for quantisation and the corpuscular–field reading are the source's, and are recorded here because they are what makes the programme's particle picture self-consistent, not because the corpus adopts them.

## The Induced Causal Minkowski Geometry with Phase

The last structural claim is geometric, and it is the one that connects most directly to *Why Complexify Spacetime?*. The complexified Minkowski space $\mathbb{C}M$ arises in the programme as the full vector space of the biquaternion algebra, and the restriction of coordinates to the real slice $M$ is, in the source's words, artificial: the real slice is not a subalgebra and is invariant neither under the algebra automorphisms nor under the full symmetry group. The natural group is the automorphism group $SO(3,\mathbb{C})$, of six real parameters, double-covering the Lorentz group $SO(3,1)$.

The Minkowski geometry is then **induced**, not postulated. The principal invariant of the complex three-space is

$$
\sigma = (z_1)^2 + (z_2)^2 + (z_3)^2 ,
$$

and it splits into a modulus-like part and a phase-like part. The modulus part is the real non-negative invariant $S^2 = \sigma\sigma^{*}$. The claim is that this invariant can be written identically as a Minkowski-like interval,

$$
S^2 = \sigma\sigma^{*} \equiv T^2 - \lvert\vec X\rvert^2 ,
\qquad
T := \vec z\cdot\vec z^{*},
\qquad
\vec X := i\,[\vec z\times\vec z^{*}] ,
$$

where the brackets are the scalar and vector products of complex three-vectors. The quantities $T$ and $\vec X$ are real, and under the $SO(3,\mathbb{C})$ automorphisms they transform as the time and space coordinates of Minkowski space under Lorentz transformations. The identity is an instance of the Lagrange identity relating the modulus of the complex quadratic form to the dot and cross products; it is recomputation-verified on random complex vectors in this pass, together with the reality of $\vec X$. What it gives is exactly what *Why Complexify Spacetime?* describes as a motivation and not a derivation: an algebraic origin for the Lorentzian signature, here written as an identity between the complex invariant $\sigma\sigma^{*}$ and a Minkowski interval built from the same vector.

The programme goes further than the signature. Because $\sigma$ also has a **phase**, the modulus identity leaves a phase invariant of the same Lorenz-transformation group, an internal fibre-like variable over the physical macro-geometry. The source suggests, without claiming to have shown it, that this phase is related to universal quantum properties of matter and to interference. The construction is the same induced-geometry mechanism the corpus cites in *Curved Spacetime and the Biquaternion Framework* and, in that article's language, it is the most complete statement of the mechanism.

Writing the complex three-vector as $\vec z=\vec p+i\vec q$ with **real** three-vectors $\vec p$ and $\vec q$ (the source's $p,q$; the arrows distinguish them from the scalar twistor coordinate $p$ of the notation table), the source separates the primary complex space linearly into a pair of real vectors — a splitting it calls "demonstrative" but explicitly not the fundamental one, since the geometry it uses is the modulus-and-phase one. In this splitting $\sigma=S e^{i\alpha}$, and the invariants above acquire the elementary forms

$$
\sigma = (\lvert\vec p\rvert^2-\lvert\vec q\rvert^2) + 2i\,\vec p\cdot\vec q ,
\qquad
T = \lvert\vec p\rvert^2+\lvert\vec q\rvert^2 ,
\qquad
\vec X = 2\,\vec p\times\vec q .
$$

Both $T$ and $\vec X$ are manifestly real in this form, a second and elementary confirmation of the reality asserted above, and the sign $\vec X=+2\,\vec p\times\vec q$ is the one fixed by recomputation on random complex vectors in this pass. The source observes that the real and imaginary parts of $\sigma$ are formally the two invariants of the electromagnetic field, with $\vec p$ and $\vec q$ read as its electric and magnetic strengths; it offers the resemblance as "much suggesting" and requiring "thorough analysis", not as an identification. The effective time coordinate is positive definite, $T=\lvert\vec p\rvert^2+\lvert\vec q\rvert^2\ge0$, while the spatial $\vec X$ is an axial vector, so a choice of sign corresponds to a frame of definite chirality. The source connects the positivity of $T$ to the irreversibility of physical time, recorded in the last section below.

The source also records a relation between the velocity of a material point in the induced space and the invariants of the primary one. With $V$ the magnitude of the velocity $\delta\vec X/\delta T$ and $\theta$ the angle between $\vec p$ and $\vec q$,

$$
\cos^2\theta = \frac{1-V^2}{1+V^2\coth^2\alpha} .
$$

At the fundamental velocity $V=1$ it forces $\theta=\pi/2$, so $\vec p$ and $\vec q$ are orthogonal to each other and to the direction of motion, as for an electromagnetic wave, while $\sigma$ vanishes and the phase $\alpha$ becomes indefinite; for a point at rest $V=0$ it gives $\theta=0$ or $\pi$, two admissible relative orientations that the source compares with the two projections of a spin vector onto a fixed direction. The relation is recorded as the source's: unlike the identities above, it was not recomputed in this pass.

On this background the programme develops a picture of particles and time that is speculative and is recorded as such. Any GSE solution corresponds to a shear-free null congruence of rays, which the source calls the **Prelight flow**, the primordial flow of light; matter, represented by the particle-like singularities, appears as the set of caustics or focal lines of that flow. The time coordinate on the real slice is the parameter along the rays, so the defining property of time in the programme is the preservation of the primordial twistor field along the congruence — "time as an automorphism of the primary field" — while the variability of matter defines a second function of time. In the complex space, Newman's representation of the shear-free congruences by a complexified Liénard–Wiechert field makes the complex null cone equation have many roots, so a particle is correlated with its own other positions along its world line; the source calls the resulting ensemble of identical yet differently located particles the ensemble of **duplicons**, and suggests that its stochasticity, once complex time is allowed to vary, is related to quantum uncertainty in Feynman's formulation. This is programmatic. The corpus neither adopts the vocabulary nor endorses the reading; it records that the programme states these as hopes and not as results.

## The Light-Formed Aether and the Flow of Time

The paper's last layer is its account of time, and it is the most speculative. The rays of the congruence densely fill space, and at each point they consist of a superposition of branches, all propagating in different directions at the same universal speed in every branch and every frame. The programme's reading is that there is nothing in the Universe but this primordial light flow, and that ordinary matter is born at its caustic regions of condensation. On that picture the Flow of Time is identified with the Flow of Prelight: the "River of Time" becomes the "River of Light", and the subjective uniformity and homogeneity of time is read as a reflection of the universality of the speed of light. The aether that the picture reintroduces is Lorentz invariant and structureless, explicitly not the old elastic light-carrying medium, so the source presents it as consonant with special relativity rather than opposed to it.

Because the underlying field is multivalued, each point carries a set of locally distinct subflows, and the time flow is therefore multi-directional; the source suggests that the local direction is unobservable precisely because of this multiplicity, and that a stochastic component in the world solution would hide it further. The programme's time is non-material. Unlike Kozyrev's "active time", which the source explicitly sets aside for want of any known mechanism of interaction with matter, this time does not interact with matter but forms it, and the source summarises the scheme as a single entity, "preLight–Time–Matter". These are programme statements, not results; the paper offers them as a picture to be developed. The corpus records them beside its own time material in *The Quantum-Classical Divide in the Biquaternion Framework*, and adopts neither the vocabulary nor the reading.

## The Dimerous Electron and Quantum Interference

The reading of the electron is the sharpest of the programme's particle claims, and the source states it as a conjecture. A duplicon is a pre-element of matter; the source proposes that an elementary object — an electron — is not one duplicon but a **pair**, the **dimerous electron**. The pair is invisible most of the time: its two members are separated in complex space, do not radiate, and can be detected by no observer. Only when their positions coincide does an act of interaction occur — a caustic, a null complex line of the generating congruence, carrying a signal towards the observer — and at that instant the pair is registered as a single particle. The source conjectures that the two pre-elements correlate with the observed fractional charges, and that this fusion picture replaces the wave-particle dualism instead of standing beside it. It also notes that the concept cannot be realised on the real Minkowski background, where the retardation equation has only the trivial root.

The interference argument is geometric. Let a pair of duplicons diverge and pass through different "slits" of an idealised interference experiment, then fuse again. Between the two fusions each member acquires a phase lag, namely the phase $\alpha$ of the principal complex invariant "attached" at each point of the generating world line and altering along it. Equality of the two complex coordinates at the fusion forces $\Delta\alpha=2\pi N$, $N\in\mathbb{Z}$: a discrete set of re-fusion points, which the source reads as the analogue of the preparation of a state and its later measurement. Only the modulus $S$ of the complex time is the ordinary Minkowski proper time; its phase $\alpha$ is the source's candidate for the phase of the wave function, and the picture contains no physical de Broglie wave.

The argument is made quantitative by one further assumption, that the physically infinitesimal increments of modulus and phase are proportional, $d\alpha=\mathrm{Const}\cdot dS$. Choosing the scale factor as the inverse of half the electron Compton length, $\mathrm{Const}=(\lambda_0/2)^{-1}=2Mc/\hbar$ — the source identifies this with the quantum of complex time, the **chronon**, and notes that it comes out of Compton order and not of Planck order — the fusion condition gives

$$
\Delta\alpha = \frac{2Mc}{\hbar}\int dS = \frac{\Delta A}{\hbar} = 2\pi N ,
$$

the condition for maxima of interference in the relativistic case, with the phase lag proportional to the path difference and the Minkowski interval as the invariant measure. The source notes its correspondence with Feynman's $\Psi=R\exp(iA/\hbar)$, whose phase is proportional to the classical action — for a free particle, to the proper time — and, expanding $dS$ in powers of $V/c$ and using the integrability of the zeroth-order term, recovers the ordinary de Broglie relation

$$
\Delta\int\frac{dL}{\lambda}=N ,
\qquad
\lambda:=\frac{h}{Mv} ,
$$

with the path difference of the two duplicons an integer number of de Broglie wavelengths. The claim is therefore not a new interference formula: the standard condition is reproduced, and what the programme adds is a reading of it, in which the phase and its integrality are geometric and no physical wave is introduced. The corpus records the reading as the source's and does not adopt its vocabulary; the Feynman phase-of-the-action structure it uses is the corpus's own subject in *The Path Integral in Biquaternionic Form*.

## Random Complex Time and the Irreversibility of Physical Time

The last layer is the account of time, and it is explicitly a conjecture. In the complex picture the evolution parameter $\tau$ of a generating world line $z_\mu(\tau)$ is complex, so the next position of the world line under $\tau\mapsto\tau+d\tau$ is indefinite: the phase of $\tau$ is free. The source calls the curve $\tau=\tau(t)$, with $t$ a monotonically increasing real parameter, the **evolution curve**, and insists that only after the curve is specified can one order events and distinguish past from future — the curve *is* the arrow of time. It conjectures that the universal evolution curve is "extremely complicated and entangled", probably of a fractal-like nature, and that the walk of the complex parameter is effectively a random walk; if the walk is discrete there arise quanta of time, the chronons, again of Compton order. The source argues that the parameter that preserves both the primary twistor field and the caustic structure is the principal invariant $\sigma$ of complex proper time itself, so that complex "proper" time plays the role of a universal global time.

The mechanism by which the random complex time yields a definite arrow is a small piece of algebra, and it is the source's only stated reason for the irreversibility. With $T=\lvert\vec p\rvert^2+\lvert\vec q\rvert^2$ and increments $d\vec p,d\vec q$, the finite increment of the effective time coordinate is

$$
\Delta T = 2\,(\vec p\cdot d\vec p+\vec q\cdot d\vec q) + (d\vec p\cdot d\vec p+d\vec q\cdot d\vec q) .
$$

Under the averaging procedure the mixed term — which can have either sign — vanishes, and the averaged increment

$$
\delta T = d\vec p\cdot d\vec p+d\vec q\cdot d\vec q \equiv \Delta T
$$

is non-negative and behaves at a "physically infinitesimal" scale as a full differential, a holonomic quantity. The source's conclusion is that any macroscopic change of the particles' positions in the primary complex space necessarily increases the effective time coordinate, so irreversibility is kinematical and statistical in nature and the time coordinate resembles an entropy-like quantity, a probability measure. On top of the initially deterministic classical dynamics there then arises an unremovable and globally universal randomness in the evolution of an observable ensemble, tied to the conjectural stochastic character of the complex-time parameter. The source presents the phase $\alpha$ as at once the measure of the uncertainty of that evolution and the measure of the wave properties of matter, with a geometric origin and no appeal to the wave-particle-dualism paradigm.

These are programme statements and hopes, and the source offers them as a picture to be developed. The corpus records them beside its own time material in *The Quantum-Classical Divide in the Biquaternion Framework*, and the entropy-like reading beside *Coarse-Graining and the Biquaternion Entropy Functional*, adopting neither the vocabulary nor the reading. The source's arrow is kinematic and statistical, arising from the positivity of $\delta T$; the corpus's own second-law material obtains its asymmetry from coarse-graining, and the two accounts are not merged.

## Status, Contrasts, and Boundaries

The algebrodynamical programme is an ambitious and internally coherent proposal, and its boundaries should be stated as plainly as its claims.

**What it genuinely adds.** It supplies (i) a **nonlinear** primary equation over the biquaternion algebra, distinct from the corpus's linear Fueter theory, whose integrability conditions reproduce the linear gauge equations; (ii) a mechanism — over-determination plus self-duality plus weak gauge invariance — that **restricts electric charge to multiples of a quarter** and identifies the elementary charge with the minimal value, which addresses the corpus's charge-quantisation boundary; (iii) an **explicit algebraic origin of the Minkowski interval** from the complex invariant of the algebra, which for *Why Complexify Spacetime?* is the derived signature it currently only motivates; and (iv) a generation mechanism in which the metric, the electromagnetic field and the Yang–Mills field descend from one twistor function with coincident singularities. Two further items were added to this article after the arXiv version of the source paper was read in full: (v) an explicit **ring family** $\Pi=G^n/H$ with radii $R_n=a(n-1)/\sqrt{n(n-2)}$, recomputation-verified here, whose $n=2$ member is the **Hopf map**, so the Hopf fibration appears as a member of the eikonal family; and (vi) the **multivaluedness** thesis — that the principal field is multivalued by construction, that a mode's univaluedness is the source of charge quantisation, and that the eikonal field is at once the fundamental field (class I) and a characteristic field (class II). A further pass, on the 2009 survey *Algebrodynamics over Complex Space and Phase Extension of the Minkowski Geometry*, added: (vii) the **explicit phase-extension invariants** of the induced geometry — with $\vec z=\vec p+i\vec q$ and $\vec p,\vec q$ real, $\sigma=(\lvert\vec p\rvert^2-\lvert\vec q\rvert^2)+2i\,\vec p\cdot\vec q$, $T=\lvert\vec p\rvert^2+\lvert\vec q\rvert^2\ge0$ and $\vec X=2\,\vec p\times\vec q$ with the sign fixed by recomputation, the source's reading of the real and imaginary parts of $\sigma$ as the electromagnetic invariants, and the velocity–orientation relation $\cos^2\theta=(1-V^2)/(1+V^2\coth^2\alpha)$; and (viii) the **dimerous-electron** reading of charge and interference — an electron as a pair of duplicons whose fusions are the interaction acts, the geometric phase of complex time as the interference phase, the fusion condition $\Delta\alpha=2\pi N$ and the recovered de Broglie relation — together with the **random complex time** and the kinematic-statistical irreversibility from the positivity of $\delta T$. The 1995 paper *Biquaternion Electrodynamics and the Weyl–Cartan Geometry of Space-Time*, whose text became available in this pass, added (ix) the **Weyl–Cartan geometry and the Yang–Mills triplet**: the complex spinor connection $\Gamma_\nu=G\varsigma_\nu$, whose four-vector form $\Gamma^\mu_{\ \nu\rho}=2(A_\nu\delta^\mu_\rho+A_\rho\delta^\mu_\nu-A^\mu\eta_{\nu\rho}-i\varepsilon^\mu{}_{\cdot\nu\rho\alpha}A^\alpha)$ is determined by the potential $A_\mu=2G_\mu$; the **unitary field** $U=FF^\dagger$, whose condition is carried by the **real** connection $\Delta^\mu_{\ \nu\rho}=2(a_\nu\delta^\mu_\rho+a_\rho\delta^\mu_\nu-a^\mu\eta_{\nu\rho}-\varepsilon^\mu{}_{\cdot\nu\rho\alpha}b^\alpha)$ with $a=\Re A$, $b=\Im A$, so that the Weyl non-metricity is the Coulomb field and the torsion pseudotrace is the **magnetic monopole**, which would be unobservable because torsion is absent from the geodesic equation, together with the observation that this connection had been shown by Stepanov to be the unique one compatible with a conventional covariant spinor derivative; the **inhomogeneous Lorentz condition** $D=\partial_\mu A^\mu+2A_\mu A^\mu=0$ beside the self-duality; the rigidity argument by which two independent spinor solutions force $R_{\mu\nu}=0$ and non-triviality therefore forces $\det F=0$, so that the field takes its values on the null divisors and an **indefinite signature** is a necessary condition of non-trivial dynamics rather than a postulate; and the explicit **complex gauge triplet** $N^a_{\ 0}=A_a$, $N^a_{\ b}=\delta_{ab}A_0-i\varepsilon_{abc}A_c$, whose self-dual strength obeys the Yang–Mills equation and whose modulus is the electromagnetic field strength, $\sum_a(L^a_{\ \mu\nu})^2\propto(F_{\mu\nu})^2$. The closed-form static solution $f^\pm=(x_1\pm ix_2)/(r\pm x_3)=\tan^{\pm1}(\theta/2)e^{\pm i\phi}$, the stereographic map $S^2\to\mathbb{C}$, and its complex potential $A_0=\pm1/(2r)$ with charge $q=\pm1$ were recomputed here; the connection, the curvature-invariant proportionality and the triplet-modulus constant were not, because they hold on the solutions of the primary system. The 1998 conference paper *Particles as Singularities within the Unified Algebraic Field Dynamics* (arXiv:gr-qc/9809056) added (x) the physical flesh of the particle reading, all of it recomputed here where it is checkable. It gives the unisingular solution in a **self-consistent normalisation**, $A_0=\pm1/(4r)$ differentiating to $E_r=\pm1/(4r^2)$, with the electric field pure real and the magnetic field pure imaginary, so that the printed inconsistency of the 1995 pair is superseded and the elementary charge is fixed at $\tfrac14$; the singular solutions are **dions**, $q=\pm\tfrac14$ with magnetic charge $m=\pm i/4$ of equal magnitude; the imaginary sector — magnetic charge and electric dipole moment — is "phantom", entering only the totally skew-symmetric torsion and therefore not the geodesic equations. It obtains the ring as the **complex translation** $z\mapsto z+ia$ of the point solution, the Appel potential $A_0=q/r_*$, whose far field was recomputed here to be that of a charge with magnetic dipole moment $\mu=qa$ and electric quadrupole moment $\vartheta=-2qa^2$; and it draws from those two moments the programme's **only numerical prediction**, that fixing $|a|=\hbar/2Mc$ to reproduce the Dirac moment forces $\vartheta=e\hbar^2/(2M^2c^2)$ — an algebraic identity, verified here, which the source itself calls speculative while noting it might be testable. Finally it reads the evolution of the singular loci through **catastrophe theory**, with the perestroika of a caustic set as a mutual transmutation of particles. The 2016 conference note *Relativistic Algebra of Space-Time and Algebrodynamics* added (xi) the **local algebra**: the covariant multiplication law of Grgin's algebra, verified here to be the biquaternion multiplication for one sign of its $\varepsilon$ term and the reversed multiplication for the other; the **local $L$-algebra** on a curved manifold, whose existence requires a tetrad and a **unit time-like U-field** beside the metric; the **effective metric** $\tilde g_{\rho\lambda}=2E_\rho E_\lambda-g_{\rho\lambda}$, whose flat case is the four-dimensional *Euclidean* metric, and the identity $g^*_{\mu\nu}=\tfrac14C^\beta_{\ \mu\alpha}C^\alpha_{\ \nu\beta}=\tilde g_{\mu\nu}$, which extracts the same metric from the structure functions of the local algebra alone — a coincidence the source calls remarkable and which the recomputation made here strengthens from the source's hedge to an arbitrary unit U-field; and the induced connection $\Gamma=\gamma+G$, of the same Weyl–Cartan type, whose non-metricity is $\nabla_\rho g_{\mu\nu}=-2g_{\mu\nu}\tilde A_\rho$ with $\tilde A_\rho=(2E_\rho E_\lambda-g_{\rho\lambda})A^\lambda$, so that the Weyl vector is the potential read through the effective metric rather than the potential itself. All four items were verified here where they are checkable; the note's expectation that the same conditions will determine the metric and the U-field is left by the source as future work and is recorded as a hope.

**What it does not supply.** It is classical: the algebra contains no $\hbar$, and the quantum interpretation is programmatic. It is non-Lagrangian and over-determined, so it has no standard canonical quantisation, and the source itself says that quantising an over-determined system requires new methods. The charge quantisation is conditional on the singularity structure and is not a derivation of the numerical value of the electron charge. The induced geometry is developed for the complex three-space and its identification with the physical macro-geometry is a mapping into the causal domain, not a dynamical construction. And the duplicon, dimerous-electron, chronon and complex-time ideas are explicitly hopes: the dimerous-electron argument recovers the standard interference condition rather than replacing it, and the phase–modulus proportionality $d\alpha=\mathrm{Const}\cdot dS$ that turns it quantitative is an assumption of the source, not a consequence of the algebra.

**The other external claim to the same boundary.** This programme is not the corpus's only external source that claims to *derive* charge quantisation, and the two should be named together, because they do it on opposite kinds of equation. This one works on a **nonlinear, over-determined** primary equation and obtains the quantisation from over-determination, self-duality and weak gauge invariance, with the additional topological route through the univaluedness of a mode of the multivalued field; the charge comes out as a multiple of a quarter, and the elementary charge is identified with the minimal admissible value. The other is the claim of Gsponer and Hurni (*Lanczos's Equation to Replace Dirac's Equation?*, Lanczos centenary, 1994; arXiv:hep-ph/0112317), on the **linear** Einstein–Mayer generalized-mass system, where the solutions are classified into quarks and leptons and the electric charges — fractional and integral as required — and the baryonic charge are read off the classification, with the neutrino and the u-quark masses zero by eigenvalue equations. Neither is a result of this corpus, and the corpus's linear framework is silent on both; what the pair establishes is that the boundary is attacked from two directions and by two different mechanisms, one nonlinear-dynamical and one linear-algebraic. The distinction is worth keeping because the corpus's own statement of the boundary — that the biquaternion framework re-expresses the Dirac condition but does not derive the quantum of charge — is a statement about the **linear** framework, and a reader who meets either claim should see the other beside it and see which equation it rests on. Both are recorded as claims: the second is four pages with no derivation exhibited, and the first is conditional on the singularity structure and does not derive the numerical value of the electron charge.

**The corpus's relation to it.** The corpus records the programme and does not endorse it. Where the programme overlaps corpus material — the Klein–Penrose incidence, the spinor module, the null cone as zero divisors, the Fueter theory, the Kerr–Schild metric, the electromagnetic invariants — the overlap is noted and the corpus's own treatment is not displaced. Where the programme is genuinely distinct — the nonlinear primary equation, the self-quantized charge, the induced interval with phase — it is recorded once, here, with cross-references, in the same spirit as the other external programmes in *Biquaternion Electromagnetism*.

**A note on the source text.** The PDF of the source paper used here has a degraded text layer in which the letter "c" is systematically dropped, so verbatim quotation is unreliable and the paper's own theorem numbers could not be read with confidence. No theorem number of the source is cited for that reason, and every algebraic statement that could be checked independently was recomputed before it was written: the rank-one degeneracy of the gradient, the transformation to the complex eikonal, the imaginary-part relations of the self-dual field, the Kerr solution's first-order system, its complex eikonal, its wave equation and the harmonicity of $\ln G$, and the identity behind the induced interval all pass.

## Summary

The algebrodynamical programme replaces the naive derivative of a quaternionic function — which exists only for linear functions — by the **two-sided** condition $dF=L\,dZ\,R$, which for $\mathbb{H}$ characterises the conformal maps of $E^4$ and, after complexification, admits **degenerate** conformal maps into the null divisors of the algebra. Fixing a component $\Sigma$, the condition says that the matrix of derivatives of $\Sigma$ has rank one, so its determinant vanishes: this is a **nonlinear analogue of the Laplace equation**, which in biquaternion coordinates is the complex eikonal of complexified Minkowski space.

The eikonal is solved algebraically by a twistor, through the Kerr equation $\Pi(G,wG+u,vG+p)=0$ for an arbitrary holomorphic world function $\Pi$; the two classes $\Pi=0$ and $d\Pi/dG=0$ exhaust the analytic solutions. The physically relevant solutions come from a spinor splitting of the two-sided condition, the **generating system of equations**, which is over-determined (eight equations for six unknowns). Its integrability conditions force the curvature of an associated Weyl–Cartan connection to be **weakly self-dual**, and the Bianchi identity then yields the free Maxwell and Yang–Mills equations for the trace and trace-free parts of the curvature. The linear field equations are thus consequences of the primary nonlinear system.

The geometry behind those integrability conditions is explicit in the programme's 1995 presentation, and it is recorded here because it supplies four further claims. The spinor connection $\Gamma_\nu=G\varsigma_\nu$ is a complex affine connection of Weyl–Cartan type, determined by the electromagnetic potential $A_\mu=2G_\mu$ alone; passing to the **unitary field** $U=FF^\dagger$ replaces it by a **real** connection whose Weyl non-metricity $a_\mu=\Re A_\mu$ is the Coulomb field and whose torsion pseudotrace $b_\mu=\Im A_\mu$ is the **magnetic monopole**, so that in this reading the monopole is torsion, which does not enter the geodesic equation and would be unobservable — the opposite of the corpus's monopole article, and recorded beside it, neither adopted. The same connection is the one Stepanov showed to be the unique space-time connection compatible with a spinor-bundle structure carrying the conventional spinor derivative, which makes the programme's central geometric object one the corpus already uses. The integrability conditions include, beside the self-duality, the **inhomogeneous Lorentz condition** $D\equiv\partial_\mu A^\mu+2A_\mu A^\mu=0$, a nonlinear condition with a term quadratic in the potential, which the source relates to the vanishing scalar curvature of the effective space. Non-triviality forces $\det F=0$ — the primary field takes its values on the **null divisors**, the complex light cone — and null fields exist only on **indefinite-signature** manifolds, the programme's sharpest statement that the Lorentzian signature is forced rather than postulated, the boundary stated in *Why Complexify Spacetime?*. Finally the trace-free part of the connection is a complex gauge triplet $N_\nu$, fixed linearly by the same potential through $N^a_{\ 0}=A_a$, $N^a_{\ b}=\delta_{ab}A_0-i\varepsilon_{abc}A_c$, whose self-dual strength obeys the Yang–Mills equation; the curvature splits into a trace part proportional to $F_{\mu\nu}$ and this triplet strength, and $\det R_{\mu\nu}=0$ makes the electromagnetic field strength the **modulus of the Yang–Mills triplet**, $\sum_a(L^a_{\ \mu\nu})^2\propto(F_{\mu\nu})^2$ — a proportionality whose constant is convention-dependent and is not reconciled here.

The 2016 conference note extends the geometry in one direction, from the flat case to a manifold. Its starting point is the **covariant multiplication law** proposed by Grgin, written with the Minkowski metric, the Levi-Civita symbol and a distinguished unit element $e$ with $e^\mu e_\mu=1$: with $e=(1,0,0,0)$ it is the biquaternion multiplication for one sign of its $\varepsilon$ term and the reversed multiplication for the other — the identification, overlooked in Grgin's own paper, that the note supplies, verified here on random pairs. On a curved manifold the same table defines a **local algebra** whose basis vectors are a tetrad, $\Sigma_\mu=h^\alpha_{\ \mu}\sigma_\alpha$, so that the metric arises from the tetrad, $g_{\mu\nu}=h^\alpha_{\ \mu}h^\beta_{\ \nu}\eta_{\alpha\beta}$, and the unit element becomes a **unit time-like vector field**, the **U-field** $E_\mu=h^\alpha_{\ \mu}e_\alpha$: the existence of the local algebra therefore requires a U-field beside the metric, and the note reads it as the flow of matter. It is not the corpus's unitary field $U=FF^\dagger$, which is built from the primary field; here it belongs to the geometry. Two metrics follow from the construction. The **effective metric** $\tilde g_{\rho\lambda}=2E_\rho E_\lambda-g_{\rho\lambda}$ has the flat case $\tilde g=\mathrm{diag}(1,1,1,1)$ — the flat limit's effective metric is **Euclidean**, which the source calls surprising and which is exact — and is the reflection of $g$ in the $E$ direction; and the metric built from the **structure functions** of the local algebra, $g^*_{\mu\nu}=\tfrac14C^\beta_{\ \mu\alpha}C^\alpha_{\ \nu\beta}$ with $C^\rho_{\ \mu\nu}=\delta^\rho_\mu E_\nu+\delta^\rho_\nu E_\mu-E^\rho g_{\mu\nu}\pm i\sqrt{-g}\,\varepsilon^\rho{}_{\cdot\mu\nu\lambda}E^\lambda$, is the *same tensor*: the identity $g^*=\tilde g$ holds here for an arbitrary unit U-field, verified on random draws, where the source states it only for $g=\eta$. The connection the curved differentiability condition induces, $\Gamma=\gamma+G$ with the Levi-Civita $\gamma$, is of the same Weyl–Cartan type as the 1995 one — non-symmetric in its lower pair, hence with torsion — and its non-metricity is $\nabla_\rho g_{\mu\nu}=-2g_{\mu\nu}\tilde A_\rho$ with $\tilde A_\rho=(2E_\rho E_\lambda-g_{\rho\lambda})A^\lambda$, an identity verified in the flat case: the Weyl vector is the potential read through the effective metric, not the potential itself, which is the one place the note's geometry differs from the 1995 geometry rather than merely restating it. The note expects the integrability conditions to restrict the metric and the U-field as well as the potential, and determines none of them; the corpus records the expectation as a hope.

The solutions of the primary system are generated from $\Pi$ alone. Their singular locus — the branch set $d\Pi/dG=0$ — is simultaneously the singularity of the effective curvature, the electromagnetic field and the Yang–Mills field, which the programme reads as the statement that a particle is a common singularity of all the associated fields. The **headline claim** is that these singular solutions have **self-quantized electric charge**: self-duality together with the weak gauge invariance of the primary system restricts the charge to $q=N/4$, the fundamental static solution has the minimal value $|q|=\tfrac14$ with a ring singularity of radius $a$, it reproduces the Kerr–Newman field and metric with $g=2$, and it is the programme's classical model of the electron. In the 1998 presentation the same solution carries $A_0=\pm1/(4r)$ with $E_r=\pm1/(4r^2)$ — a potential and a strength that are mutually consistent, fixing the elementary charge at $\tfrac14$ — and it is a **dion**, with magnetic charge $m=\pm i/4$ of the same magnitude as the electric one; the imaginary sector of the complex field carries the magnetic charge and the electric dipole moment, is called "phantom" by the source, and enters only the longitudinal (totally skew-symmetric) torsion, so that it does not enter the geodesic equation and would be unobservable. The ring itself is the **complex translation** $z\mapsto z+ia$ of the point solution, with the Appel potential $A_0=q/r_*$; its far field, recomputed here, is that of a charge $q$ with **magnetic dipole moment $\mu=qa$** and **electric quadrupole moment $\vartheta=-2qa^2$**. Requiring $\mu$ to take the Dirac value forces $|a|=\hbar/2Mc$ and hence $\vartheta=e\hbar^2/(2M^2c^2)$, the programme's only numerical prediction — a one-line algebraic identity, verified here, which the source states as a conjecture and calls speculative. And the evolution of the singular loci is read through **catastrophe theory**: a perestroika of a caustic set is a mutual transmutation of particles, for which the bisingular solution is the evidence. The claim is the programme's, conditional on the singularity structure, and it engages the corpus's stated open boundary on charge quantisation without settling it.

The scheme is organised by a **world function** $\Pi$: the class-I solution is the fundamental field, and the class-II conjugate, built from $d\Pi/dG=0$, is the characteristic field whose vanishing marks the branching locus. For an irreducible $\Pi$ the principal field is **multivalued**, and each locally chosen branch is a mode carrying its own congruence and fields; the source holds that this multivaluedness is required rather than tolerated, that fields which constitute particles need not be univalued, and that univaluedness of a single mode is itself the source of the charge quantisation — a second route to $q=N/4$ beside self-duality. The singular loci of the static family $\Pi=G^n/H$ are the rings $z=0$, $x^2+y^2=R_n^2$ with $R_n=a(n-1)/\sqrt{n(n-2)}$ ($n\ge3$), recomputation-verified here, and the $n=2$ member is the Hopf map; a fourth-order generating function gives the corpus's clearest multiparticle example, two opposite elementary charges inside a neutral cocoon that cancels at $t=b/\sqrt2$ and emits a light-like wavefront. The quadratic family is exhausted, up to Poincaré transformations, by the Kerr-like static solution and the nonstationary bisingular one, with the neutral, null figure-eight as a member; and the wave-like solutions give a closed form in the **Lambert function** whose singular set is a **neutral helix of radius $1/(\varpi A e)$ and lead $2\pi/\varpi$**, the most concrete particle-like object in the material. In the conclusion the source states the purpose of the construction as the corpus states its own: one abstract structure — the biquaternion algebra with its generalised Cauchy–Riemann conditions — successively expressed in several equivalent geometric languages, *covariantly constant fields, twistor geometry, shear-free congruences*, and the source's last layer identifies the Flow of Time with the Flow of Prelight.

The programme's geometry is **induced**: the complex invariant $\sigma=(z_1)^2+(z_2)^2+(z_3)^2$ has a modulus part obeying the identity $\sigma\sigma^{*}=T^2-\lvert\vec X\rvert^2$, so the Minkowski interval and the Lorentz action arise from the algebra rather than being postulated, with the phase of $\sigma$ as an extra internal variable. On this background the programme builds a speculative picture of particles as caustics of a primordial light flow, of time as an automorphism of the primary twistor field, and of an ensemble of complex-space "duplicons" related to quantum uncertainty. A later survey pass made three additions, all recorded as the source's. The induced geometry's invariants are given explicitly in the real splitting $\vec z=\vec p+i\vec q$: $\sigma=(\lvert\vec p\rvert^2-\lvert\vec q\rvert^2)+2i\,\vec p\cdot\vec q$, $T=\lvert\vec p\rvert^2+\lvert\vec q\rvert^2\ge0$, $\vec X=2\,\vec p\times\vec q$, with the source's reading of the real and imaginary parts of $\sigma$ as the electromagnetic invariants and the velocity–orientation relation $\cos^2\theta=(1-V^2)/(1+V^2\coth^2\alpha)$. The **dimerous electron** is read as a pair of duplicons whose fusion events are the interaction acts; the geometric phase of complex time supplies the interference phase, and the fusion condition $\Delta\alpha=2\pi N$ reproduces the relativistic interference condition and, in the nonrelativistic limit, the de Broglie relation. And **random complex time** yields the arrow of time: the averaged increment $d\vec p\cdot d\vec p+d\vec q\cdot d\vec q\ge0$ makes irreversibility kinematic and statistical, with the "chronon" of complex time conjectured to be of Compton order. These are hopes, recorded as such. The programme is an external programme: the corpus records it, does not endorse it, and does not adopt its vocabulary.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong\mathrm{Mat}(2,\mathbb{C})$ | Biquaternion algebra, read in the programme as an algebra of coordinates |
| $Z$, $Z^{AB}$ | Complex matrix variable and its four entries |
| $u,v,w,p$ | The entries $Z^{00},Z^{11},Z^{01},Z^{10}$ |
| $z_0,z_1,z_2,z_3$ | Cartesian coordinates, $z_0=(u+v)/2$, $z_3=(u-v)/2$, $z_1=(w+p)/2$, $z_2=i(w-p)/2$ |
| $\det Z=(z_0)^2-\dots-(z_3)^2$ | Source's holomorphic metric; the corpus's $N$ once $Q_0=z_0$, $Q_k=iz_k$ |
| $dF=L\,dZ\,R$ | Two-sided $A$-differentiability; $L,R$ the semi-derivatives |
| $\Sigma$ | A component of a differentiable function; the eikonal potential |
| $\nabla_u,\dots$ | Partial derivatives with respect to $u,v,w,p$ |
| $\det\lVert\nabla_{AB}\Sigma\rVert=0$ | The nonlinear (complex-eikonal) equation |
| $\psi,\tau$ | Spinor and incident twistor, $\tau=Z\psi$ |
| $G=\psi_1/\psi_0$ | The principal spinor ratio |
| $\kappa_0=wG+u$, $\kappa_1=vG+p$ | Projective twistor components |
| $\Pi(G,\kappa_0,\kappa_1)$ | Generating (world) function; the Kerr equation is $\Pi=0$ |
| $P=d\Pi/dG$ | Singular-locus condition, $P=0$ |
| $\Lambda=d^2\Pi/dG^2$ | Class-II branching condition; with $P=0$ it gives the singular locus |
| $H=wG^2+2(z+ia)G-\bar w$ | Static twistor generator; $w=x-iy$, $\bar w=x+iy$, $z$ the third Cartesian coordinate |
| $r_*^2=x^2+y^2+(z+ia)^2$ | The $r_*$ of the static Kerr solution, of its $n=2$ class-II partner, and of the Appel potential $A_0=q/r_*$ |
| $R_n=a(n-1)/\sqrt{n(n-2)}$ | Ring radii of the class-II family $\Pi=G^n/H$, $n\ge3$ |
| $A_0=q/r_*$ | Appel potential: the complex translation $z\mapsto z+ia$ of the point solution |
| $\mu=qa$, $\vartheta=-2qa^2$ | Magnetic dipole and electric quadrupole moments of the complex-shifted ring |
| $\vartheta=e\hbar^2/(2M^2c^2)$ | Quadrupole forced when $\lvert a\rvert=\hbar/2Mc$ gives the Dirac moment; the programme's one numerical prediction |
| $\kappa_0\kappa_1-a^2G^2$ | Generating function of the neutral, null figure-eight solution |
| $W(z),\ W e^W=z$ | Lambert function; solves $G=A\exp[i\varpi\kappa_0]$ in closed form |
| $\varpi$, $A$ | Frequency and amplitude of the wave-like solution; the source writes the frequency $\Omega$, reserved here for the connection |
| $1/(\varpi A e)$, $2\pi/\varpi$ | Radius and lead of the wave-like neutral-helix singular set |
| $G^2\kappa_0^2+\kappa_1^2-b^2G^2$ | Generating function of the four-mode two-charge example, annihilating at $t=b/\sqrt2$ |
| $\eta,\xi,\Phi$ | Biquaternion spinors and the complex four-vector of the fundamental spinor system |
| $\Omega=\Psi\,dZ$ | $\mathbb{B}$-valued connection; $\Psi$ the gauge potential |
| $R=d\Omega-\Omega\wedge\Omega$ | Curvature; weakly self-dual on GSE solutions |
| $\vec E+i\vec H=0$ | Self-duality condition; gives $\Im\vec H=\Re\vec E$, $\Im\vec E=-\Re\vec H$ |
| $A_\mu=2G_\mu$ | Electromagnetic four-potential of the programme |
| $\Gamma_\nu=G\varsigma_\nu$, $\Gamma^\mu_{\ \nu\rho}$ | Complex spinor connection and its four-vector form, of Weyl–Cartan type; $\varsigma_a$ the spin-matrix basis, distinct from the invariant $\sigma$ |
| $U=FF^\dagger$, $\Delta^\mu_{\ \nu\rho}$ | Unitary field and the real connection it obeys |
| $a_\mu=\Re A_\mu$, $b_\mu=\Im A_\mu$ | Weyl non-metricity (Coulomb field) and torsion pseudotrace (magnetic monopole) |
| $e$, $e^\mu e_\mu=1$ | Distinguished unit element of the covariant multiplication law of Grgin's algebra $G\cong\mathbb{B}$ |
| $h^\alpha_{\ \mu}$, $\Sigma_\mu=h^\alpha_{\ \mu}\sigma_\alpha$ | Tetrad and the basis vectors of the **local $L$-algebra** |
| $E_\mu=h^\alpha_{\ \mu}e_\alpha$, $g^{\mu\nu}E_\mu E_\nu=1$ | The **unit U-field** the local algebra requires; *not* the unitary field $U=FF^\dagger$ |
| $\tilde g_{\rho\lambda}=2E_\rho E_\lambda-g_{\rho\lambda}$ | Effective metric; $\mathrm{diag}(1,1,1,1)$ when $g=\eta$, $E=(1,0,0,0)$ |
| $C^\rho_{\ \mu\nu}$ | Structure functions of the local algebra, $\Sigma_\mu\circ\Sigma_\nu=C^\rho_{\ \mu\nu}\Sigma_\rho$ |
| $g^*_{\mu\nu}=\tfrac14C^\beta_{\ \mu\alpha}C^\alpha_{\ \nu\beta}$ | Metric built from the structure functions alone; equals $\tilde g$ |
| $\Gamma=\gamma+G$, $\tilde A_\rho=(2E_\rho E_\lambda-g_{\rho\lambda})A^\lambda$ | Induced connection (Levi-Civita plus algebraic part) and its Weyl non-metricity vector, $\nabla_\rho g_{\mu\nu}=-2g_{\mu\nu}\tilde A_\rho$ |
| $D=\partial_\mu A^\mu+2A_\mu A^\mu$ | Inhomogeneous Lorentz condition; the source relates it to the scalar-curvature invariant |
| $N_\nu=N^a_{\ \nu}\varsigma_a$, $L_{\mu\nu}$ | Trace-free complex gauge triplet and its strength |
| $f^\pm$, $A_0=\pm1/(2r)$ | Static eikonal solution (stereographic map) and its 1995 complex potential; charge $q=\pm1$ in that normalisation |
| $A_0=\pm1/(4r)$, $E_r=\pm1/(4r^2)$, $H_r=\pm i/(4r^2)$ | Same solution in the 1998 normalisation: consistent potential and strengths, electric real, magnetic imaginary |
| $q=\pm\tfrac14$, $m=\pm i/4$ | Electric and magnetic (dion) charges of the unisingular solution; the imaginary sector is phantom |
| $g_{\mu\nu}=\eta_{\mu\nu}+h\,k_\mu k_\nu$ | Kerr–Schild metric; $k$ the null congruence |
| $q=N/4$, $N\in\mathbb{Z}$ | Self-quantized electric charge |
| $a$ | Ring radius of the fundamental static solution |
| $\kappa_0\kappa_1+b^2G^2$ | Generating function of the Born-type two-charge solution |
| $\sigma=(z_1)^2+(z_2)^2+(z_3)^2$ | Principal invariant of the complex three-space |
| $T=\vec z\cdot\vec z^{*}$, $\vec X=i[\vec z\times\vec z^{*}]$ | Induced time and space; $S^2=T^2-\lvert\vec X\rvert^2$ |
| $\vec z=\vec p+i\vec q$, $\vec p,\vec q$ real | Real/imaginary split of the complex three-vector (the source's $p,q$; renamed to clear the twistor coordinate $p$) |
| $\sigma=S e^{i\alpha}$ | Modulus $S$ (ordinary proper time) and phase $\alpha$ (internal) of the principal invariant |
| $T=\lvert\vec p\rvert^2+\lvert\vec q\rvert^2$, $\vec X=2\,\vec p\times\vec q$ | Induced time and space in the $\vec p,\vec q$ split; $T\ge0$; sign $\vec X=+2\,\vec p\times\vec q$ recomputation-fixed |
| $\Delta\alpha=2\pi N$, $\lambda=h/(Mv)$ | Dimerous-electron fusion condition; nonrelativistic de Broglie relation recovered from it |
| $\delta T=d\vec p\cdot d\vec p+d\vec q\cdot d\vec q$ | Averaged time increment; non-negative, the source's kinematic arrow |
| $SO(3,\mathbb{C})$ | Automorphism group; six real parameters, double cover of the Lorentz group |

## Further Reading

- V. V. Kassandrov, "Quaternionic Analysis and the Algebrodynamics", arXiv:0710.2895 [math-ph] (2007), the source paper of this article: the nonlinear Cauchy–Riemann conditions, the complex eikonal, the generating system, the gauge and twistor structures, the self-quantized charge, and the induced causal geometry.
- V. V. Kassandrov, "Singular Sources of Maxwell Fields with Self-Quantized Electric Charge", in *Has the Last Word Been Said on Classical Electrodynamics?* (Rinton Press, 2004), 42–66, arXiv:physics/0308045, for the general theorem on charge quantization and the singular sources.
- V. V. Kassandrov, "Biquaternion Electrodynamics and the Weyl–Cartan Geometry of Space-Time", *Gravitation & Cosmology* **1** (1995) 216, arXiv:gr-qc/0007027, for the material recorded from the paper itself in *The Weyl–Cartan Geometry of the Programme* and *The Yang–Mills Triplet and the Electromagnetic Modulus*: the Clifford-theoretic argument for $\mathrm{Cl}_{3,0}$ over $\mathrm{Cl}_{1,3}$, the spinor connection $\Gamma_\nu=G\varsigma_\nu$, the complex Weyl–Cartan connection $\Gamma^\mu_{\ \nu\rho}$ determined by the potential, the **unitary field** $U=FF^\dagger$ and the real connection $\Delta^\mu_{\ \nu\rho}$, the identification of the Weyl non-metricity with the Coulomb field and of the torsion pseudotrace with the magnetic monopole, the note that this connection is the unique one compatible with a conventional covariant spinor derivative (Stepanov), the inhomogeneous Lorentz condition $D=\partial_\mu A^\mu+2A_\mu A^\mu=0$, the rigidity that forces $\det F=0$ and an indefinite signature, and the complex gauge triplet $N_\nu$ whose self-dual strength obeys the Yang–Mills equation with the electromagnetic field strength as its modulus. Also the closed-form static solution $f^\pm=(x_1\pm ix_2)/(r\pm x_3)$ with the potential $A_0=\pm1/(2r)$ and charge $q=\pm1$.
- V. V. Kassandrov and J. A. Rizcallah, "Relativistic Algebra of Space-Time and Algebrodynamics", arXiv:1612.02455 [physics.gen-ph] (2016), five pages, for the material recorded in *The Local Algebra on a Curved Manifold, and the U-Field*: the covariant multiplication law of Grgin's algebra and its isomorphism with the biquaternion algebra — the identification the note says was overlooked in the paper that introduced the algebra, verified here on random pairs, with the one sign of its $\varepsilon$ term giving the ordinary product and the other the reversed product; the **local $L$-algebra**, whose basis vectors are the tetrad, $\Sigma_\mu=h^\alpha_{\ \mu}\sigma_\alpha$, with the induced metric $g_{\mu\nu}=h^\alpha_{\ \mu}h^\beta_{\ \nu}\eta_{\alpha\beta}$ and the required **unit U-field** $E_\mu=h^\alpha_{\ \mu}e_\alpha$ (distinct from the 1995 paper's unitary field $U=FF^\dagger$); the **effective metric** $\tilde g_{\rho\lambda}=2E_\rho E_\lambda-g_{\rho\lambda}$, Euclidean in the flat case, and the "remarkable coincidence" $g^*_{\mu\nu}=\tfrac14C^\beta_{\ \mu\alpha}C^\alpha_{\ \nu\beta}=\tilde g_{\mu\nu}$, in which the metric the connection is built from is obtained again from the structure functions of the local algebra alone — verified here for an arbitrary unit U-field, where the source states it only for $g=\eta$; and the induced connection $\Gamma=\gamma+G$ of Weyl–Cartan type, with torsion and with the Weyl-type non-metricity $\nabla_\rho g_{\mu\nu}=-2g_{\mu\nu}\tilde A_\rho$, $\tilde A_\rho=(2E_\rho E_\lambda-g_{\rho\lambda})A^\lambda$, verified here in the flat case. The note's expectation that the integrability conditions of the $L$-differentiability equations will restrict the metric and the U-field as well as the potential is left by it as future work.
- V. V. Kassandrov and J. A. Rizcallah, "Particles as Singularities within the Unified Algebraic Field Dynamics", Proceedings of the International Conference "Geometrization of Physics III" (Kazan State University, 1997), arXiv:gr-qc/9809056, for the material recorded in *Particle-Like Solutions and the Self-Quantized Charge*: the universal (generating) equations and their origin in Sheffers's $A$-differentiability, the reduction to the shear-free geodesic null congruence, self-duality and the inhomogeneous Lorentz condition as their integrability conditions, the Yang–Mills triplet with the modulus relation $\det\lVert R_{\mu\nu}\rVert\equiv F_{\mu\nu}^2-L^a_{\mu\nu}L^a_{\mu\nu}=0$, the unisingular **dion** with $A_0=\pm1/(4r)$, $E_r=\pm1/(4r^2)$ real and $H_r=\pm i/(4r^2)$ imaginary, the "phantom" imaginary sector carrying the magnetic charge and the electric dipole moment through the Rodichev-type torsion, the **complex translation** $z\mapsto z+ia$ giving the Appel potential $A_0=q/r_*$ with magnetic dipole moment $\mu=qa$ and electric quadrupole moment $\vartheta=-2qa^2$, the prediction $\vartheta=e\hbar^2/(2M^2c^2)$, and the catastrophe-theory reading of singularity perestroikas as mutual transmutations of particles.
- V. V. Kassandrov, "General Solution of the Complex 4-Eikonal Equation and the Algebrodynamical Field Theory", *Gravitation & Cosmology* **8** Suppl. 2 (2002) 57, for the two classes of eikonal solutions.
- V. V. Kassandrov and V. N. Trishin, "Particle-like Singular Solutions in Einstein–Maxwell Theory and in Algebraic Dynamics", *Gravitation & Cosmology* **5** (1999) 272, arXiv:gr-qc/0007026, for the reduction chain to the Einstein–Maxwell electrovacuum, the exhaustiveness of the quadratic family, the neutral figure-eight and toroidal singular loci, and the closed-form wave-like solution whose singular set is the neutral Lambert-function helix.
- V. V. Kassandrov, "On the Structure of General Solution of the Equations of Shear-Free Null Congruences", arXiv:gr-qc/0602046, and "On a quaternionic induced geometry with phase", arXiv:gr-qc/0602088, for the shear-free congruence structure and the induced geometry.
- V. V. Kassandrov, "Algebrodynamics over Complex Space and Phase Extension of the Minkowski Geometry", arXiv:0907.5425 [physics.gen-ph] (2009), the survey of the programme: the explicit phase-extension invariants of the induced geometry in the real splitting $\vec z=\vec p+i\vec q$, the dimerous-electron reading of charge and interference with the fusion condition $\Delta\alpha=2\pi N$, the random complex time and the kinematic-statistical irreversibility, and the comparison of programmes that derive or deform the Minkowski geometry cited in *Why Complexify Spacetime?*.
- V. V. Kassandrov, "The Algebrodynamics: Primordial Light, Particles-Caustics and the Flow of Time", *Hypercomplex Numbers in Geometry and Physics* **1** (2004) 84, arXiv:hep-th/0312278 (the arXiv version is titled "Nature of Time and Particles-Caustics: Physical World in Algebrodynamics and in Twistor Theory"), for the Prelight flow, the caustic reading of particles, the duplicons, the world function and the multivaluedness of the principal field, the class-II branching condition $\Lambda=d^2\Pi/dG^2=0$, the ring family $\Pi=G^n/H$ and the Hopf-map case, the four-mode two-charge example with its cocoon and its annihilation, and the identification of the Flow of Time with the Flow of Prelight. The arXiv PDF of this paper reads cleanly, unlike that of the 2007 source paper above.
- G. C. Debney, R. P. Kerr and A. Schild, "Solutions of the Einstein and Einstein–Maxwell Equations", *Journal of Mathematical Physics* **10** (1969) 1842–1854, for the Kerr–Schild electrovacuum metric.
- E. T. Newman, "Maxwell's Equations and Complex Minkowski Space", *Journal of Mathematical Physics* **14** (1973) 102–107, and R. W. Lind and E. T. Newman, "Complexification of the Algebraically Special Gravitational Fields", *Journal of Mathematical Physics* **15** (1974) 1103–1112, for the complexified Liénard–Wiechert representation behind the duplicon picture.
- A. Sudbery, "Quaternionic Analysis", *Mathematical Proceedings of the Cambridge Philosophical Society* **85** (1979) 199–225, for the obstruction to naive quaternionic holomorphy.
- G. Scheffers, "Verallgemeinerung der Grundlagen der gewöhnlichen komplexen Funktionen", *Berichte der Sächsischen Akademie der Wissenschaften* **45** (1893) 828–842, for commutative hypercomplex differentiability.
- A. Gsponer and J.-P. Hurni, "Lanczos's Equation to Replace Dirac's Equation?", *Proceedings of the Cornelius Lanczos International Centenary Conference* (SIAM, 1994) 509–512 (arXiv:hep-ph/0112317), the second external claim to the charge-quantisation boundary, made on the linear Einstein–Mayer generalized-mass system rather than on a nonlinear equation; recorded for that contrast in *Status, Contrasts, and Boundaries*. Four pages, no derivation exhibited.
