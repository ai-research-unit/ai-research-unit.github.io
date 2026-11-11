# __The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry__

## Introduction

The algebrodynamical programme of Vladimir Kassandrov and his collaborators takes the quaternion and biquaternion algebra as the **primary** object and asks what equation a differentiable function of an algebraic variable obeys. The answer is not the Fueter equation and not the Dirac equation. It is a **nonlinear** generalisation of the Cauchy–Riemann conditions, whose integrability conditions turn out to be the free Maxwell and Yang–Mills equations, and whose singular solutions the programme reads as particles — with their electric charge, in the programme's headline claim, **self-quantized**.

This article records the programme as presented in the source paper *Quaternionic Analysis and the Algebrodynamics* (arXiv:0710.2895), with the earlier parts of the series cited where they carry a result the paper only recalls — in particular the 1995 *Biquaternion Electrodynamics and the Weyl–Cartan Geometry of Space-Time* (arXiv:gr-qc/0007027), whose own text is the source of the geometric and Yang–Mills material in the two sections after *The Generating System and the Gauge Fields*, and the 1998 *Particles as Singularities within the Unified Algebraic Field Dynamics* (arXiv:gr-qc/9809056), the source of the dion solution, its multipole moments and the quadrupole prediction in the particle section; the closed-form static solution is the stereographic map of that section. One further paper of the series is the source of one further section: the 2016 conference note *Relativistic Algebra of Space-Time and Algebrodynamics* (arXiv:1612.02455, with J. A. Rizcallah), which supplies the **local** algebra of the section *The Local Algebra on a Curved Manifold, and the Unit Field* — the covariant multiplication law and its isomorphism with $\mathbb{B}$, the tetrad and the required unit field, the effective metric and the metric built from the structure functions, and the curved differentiability condition with its induced connection. It is an **external programme**. The corpus records it and does not endorse it. It is recorded because three of its claims bear directly on questions this corpus states as open: whether charge quantisation can be **derived** rather than postulated, which the corpus currently records as imported from quantum physics rather than derived; whether the Lorentzian signature of spacetime can be read off the algebra rather than put in by hand, which *Why Complexify Spacetime?* states as a motivation and not a derivation; and what a genuinely **nonlinear** holomorphy over a noncommutative algebra looks like, which the linear Fueter theory of *Biquaternion Regular Functions* deliberately is not.

One convention differs from the corpus and is flagged once, so that formulas are not misread between the two. The source writes the holomorphic metric as $\det Z = (z_0)^2 - (z_1)^2 - (z_2)^2 - (z_3)^2$, with the time-like coordinate first; the corpus writes the biquaternion norm as $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ with all-plus coefficients and the material identification $Q_t=i q'_t$. These are the same interval with the imaginary unit placed differently — they agree once $Q_t=z_0$ and $Q_\eta=iz_\eta$ for the spatial components — and both give the material signature $(3,1)$, so no physics depends on the difference; but a formula must not be transcribed from one to the other without that factor of $i$. Similarly, the source's coordinates $Z_{AB}$ are the four complex entries of a $2\times2$ matrix, so that the biquaternion algebra is $\mathbb{B}\cong\mathrm{Mat}(2,\mathbb{C})$ read as an algebra of coordinates; the corpus's $Q_\mu$ are the coefficients of the four units, and the two are related by the matrix element representation of *The Element and Operator Representations*.

The programme is large, and this article records it in one piece rather than scattering it. The order is the order of its logic: the failure of naive holomorphy, the two-sided replacement, the complex eikonal it produces, the twistor solution of that eikonal, the generating system and the gauge fields that are its integrability conditions, the Weyl–Cartan geometry and the local algebra that the later note attaches to a curved manifold, the Yang–Mills triplet that those conditions define, the Kerr equation and the shear-free congruences, the particle-like solutions with their quantised charge, the induced causal geometry, and finally the boundaries of what the programme claims.

## Why Naive Quaternionic Holomorphy Fails

The commutative case is the starting point, because it works. For a function $F$ of a variable $Z$ in a finite-dimensional associative **commutative** algebra, Scheffers' definition of differentiability is the proportionality of the differentials,

$$
dF = H(Z)\,dZ ,
$$

with $H\in A$. For an algebra with division this is equivalent to the existence and path-independence of the derivative $H=dF/dZ$, and for $A=\mathbb{C}$ it is the Cauchy–Riemann equation. Eliminating the components of $H$ gives a linear system for the components of $F$, and the whole of one-variable complex analysis has an analogue. The construction extends to commutative algebras with zero divisors, such as the double and dual numbers, when one demands that the differential take an invariant component-less form rather than that a derivative exist.

For $\mathbb{H}$ the naive transcription fails, and the source gives both of the standard reasons. The first is that noncommutativity erases the distinction between an element and its conjugate. In $\mathbb{H}$ the conjugate can be written using only the units,

$$
\bar q = -\tfrac12\left(q+i\,q\,i+j\,q\,j+k\,q\,k\right),
$$

so "a function independent of the conjugated argument" — the definition of holomorphy in one complex variable — has no content here. The second is that the right derivative $H=dF\,dZ^{-1}$ (or its left analogue) requires the limit to be independent of the path of $dZ$ to zero in the four-dimensional algebra, which is an over-determined system of partial differential equations; it is compatible only for linear functions $F = A Z + B$. This is the same obstruction the corpus records from Sudbery in *Biquaternion Regular Functions*: in four real dimensions there is no single complex variable, no invariant derivative, and the rich function theory of the plane does not transfer.

## The Two-Sided Derivative and Conformal Mappings

The source's replacement keeps the invariant-differential idea of Scheffers but allows a **factor on each side**:

$$
dF = L(Z)\,dZ\,R(Z) .
$$

The functions $L$ and $R$ are the **left and right semi-derivatives** of $F$; they are determined by $F$ only up to the equivalence $L\mapsto \alpha L$, $R\mapsto \alpha^{-1}R$ with $\alpha$ taking values in the centre of the algebra. The problem of "differentiable functions" becomes the enumeration of the triples $\{F,L,R\}$ obeying this condition up to that equivalence. For a commutative algebra the condition collapses back to $dF = (LR)\,dZ$, and if $R$ is the unit it collapses to the naive one-sided condition; it is exactly the two-sidedness that escapes the rigidity above.

For $\mathbb{H}$ the condition has a clean geometric meaning. The norm is the determinant of the matrix model and the determinant is multiplicative, $N(pq)=N(p)N(q)$ with $N(\tilde Q)=\det\mathsf M_2(\tilde Q)$ as in the companion article, so taking it on both sides gives

$$
d\tilde s^2 \equiv N(dF) = N(LR)\,N(dZ) = \Lambda(Z)\,ds^2 ,
\qquad
ds^2 \equiv N(dZ),
$$

so a $\mathbb{H}$-differentiable function is exactly a **conformal map of the Euclidean four-space** $E^4$, with scale factor $\Lambda=N(LR)$. On the real quaternion slice $N$ is the all-plus sum of the four squared components, which is why the metric there is Euclidean. The inversion $F=Z^{-1}$ has $dF = -Z^{-1}\,dZ\,Z^{-1}$, and translations, rotations and dilatations verify the condition directly. By Liouville's theorem the conformal maps of $E^4$ form a finite fifteen-parameter group, so the class is again too small to carry fundamental physics: an algebra with division is not enough.

**Physical interpretation.** This is the point at which the programme turns to the complexified algebra. The corpus's own Fueter theory keeps the linear operator $\tilde\nabla_\Phi$ and asks for its kernel; the programme instead keeps the *definition of differentiability* and accepts that it is nonlinear. The two are different answers to the same obstruction. The corpus's linear answer is elliptic on the quaternion subspace and has a complete integral theory; the programme's nonlinear answer is the one that produces singular solutions, which is precisely why it can read them as particles.

## Complexification, Degenerate Conformality, and the Complex Eikonal

On the complexified algebra $\mathbb{B}\cong\mathrm{Mat}(2,\mathbb{C})$ the determinant is still the norm, but it is now a complex number and may vanish. Taking determinants in the two-sided condition gives

$$
\det\lVert dF\rVert = \det\lVert L\rVert\det\lVert R\rVert \det\lVert dZ\rVert \equiv \lambda(Z)\det\lVert dZ\rVert ,
$$

which for invertible $L,R$ and $\lambda\neq0$ is again a conformal map, now of complexified Minkowski space $\mathbb{C}M$. The interesting case is the one the source calls **degenerate**: when $\det L=0$ (or $\det R=0$) the scale factor vanishes and every differential $dF$ is a singular matrix, its values lying in the **null divisors** of the algebra — the complex null cone. These degenerate conformal maps are the ones the programme identifies with physical fields, and complexification is what makes the class large.

In components the condition reads $\nabla_{AB}F_{CD}=L_{CA}R_{BD}$. Fixing a pair of function indices and writing $F_{CD}=\Sigma$, $L_{CA}=\tilde{Ξ}_{\mathrm{sp},A}$, $R_{BD}=\tilde{Ξ}_{\mathrm{sp},B}$ gives

$$
\nabla_{AB}\Sigma = \tilde{Ξ}_{\mathrm{sp},A}\tilde{Ξ}_{\mathrm{sp},B} .
$$

The matrix of derivatives of $\Sigma$ is therefore a product of a column and a row — it has rank one — so its determinant vanishes identically:

$$
\det\lVert\nabla_{AB}\Sigma\rVert = 0 .
$$

This is the central observation of the construction. The equation says that a component of a differentiable function has a **degenerate gradient matrix**, and it is a **nonlinear** equation because the degeneracy of the gradient is the residue of noncommutativity in the definition. It is the nonlinear analogue of the Laplace equation of complex analysis.

It becomes recognisable in coordinates. Writing the matrix entries as $Z_{00}=\upsilon$, $Z_{11}=v$, $Z_{01}=w$, $Z_{10}=p$ and computing the determinant gives

$$
\frac{\partial\Sigma}{\partial\upsilon}\frac{\partial\Sigma}{\partial v}-\frac{\partial\Sigma}{\partial w}\frac{\partial\Sigma}{\partial p}=0 ,
$$

and in the Cartesian coordinates $z_0=(\upsilon+v)/2$, $z_3=(\upsilon-v)/2$, $z_1=(w+p)/2$, $z_2=i(w-p)/2$ this is

$$
\boxed{\;\left(\frac{\partial\Sigma}{\partial z_0}\right)^2 - \left(\frac{\partial\Sigma}{\partial z_1}\right)^2 - \left(\frac{\partial\Sigma}{\partial z_2}\right)^2 - \left(\frac{\partial\Sigma}{\partial z_3}\right)^2 = 0\;},
$$

the **complex eikonal equation** of complexified Minkowski space. The verification of the coordinate change is one line of the chain rule, and the rank-one degeneracy is confirmed on random complex matrices. The determinant identity is a chain-rule computation; what $\mathbb{B}$ supplies is the arrangement, four coordinates in a two-by-two array, and what that gives is the familiar eikonal of complexified Minkowski space.

**Physical interpretation.** That the primary field equation is the eikonal is the programme's distinguishing feature. In the corpus the eikonal appears as the short-wavelength limit of a linear equation (*The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form*); here it is exact and primary, and the linear wave equation holds for the **same function**, not for its derivatives and not only in a short-wavelength limit. The programme states the coincidence and calls it puzzling; it follows from the twistor factorisation, and §*The Kerr Equation and the Shear-Free Congruences* gives the mechanism. What is lost by making the eikonal primary is additivity — the solution set is not a vector space — and not the linear equation itself.

## The Twistor Solution of the Complex Eikonal

The complex eikonal is solved algebraically, and the solution introduces the twistor. In the factorisation $\nabla_{AB}\Sigma=\tilde{Ξ}_{\mathrm{sp},A}\tilde{Ξ}_{\mathrm{sp},B}$, choose one spinor, say $\tilde{Ξ}_{\mathrm{sp}}=\{\tilde{Ξ}_{\mathrm{sp},B}\}$, and define the second by the Klein–Penrose incidence relation

$$
\tau = Z\tilde{Ξ}_{\mathrm{sp}} , \qquad \tau_A = \sum_B Z_{AB}\tilde{Ξ}_{\mathrm{sp},B} .
$$

The pair $\{\tilde{Ξ}_{\mathrm{sp}},\tau\}$ is a (projective) twistor of $\mathbb{C}M$ — the same incidence relation the corpus writes in *Twistor Theory and Biquaternions* and *Helicity in Biquaternionic Form*, with the modulus of the projective equivalence being the freedom to rescale $\tilde{Ξ}_{\mathrm{sp}}$. Choosing the gauge $\tilde{Ξ}_{\mathrm{sp},0}=1$ and writing $G=\tilde{Ξ}_{\mathrm{sp},1}/\tilde{Ξ}_{\mathrm{sp},0}$ gives the three projective components

$$
G,\qquad \kappa_0 = wG+\upsilon,\qquad \kappa_1 = vG+p .
$$

Now take an arbitrary holomorphic function $\Pi$ of the three twistor arguments, $\Pi(G,\kappa_0,\kappa_1)\equiv\Pi(G,wG+\upsilon,vG+p)$, and impose

$$
\Pi = 0 .
$$

Resolving this algebraic equation for $G(\upsilon,v,w,p)$ gives a solution of the complex eikonal — the **class I** solutions. Resolving instead $d\Pi/dG=0$ for $G$ and substituting back gives the **class II** solutions, conjugate to the first. According to the source's earlier work on the eikonal, these two classes exhaust all almost-everywhere analytic solutions. For a general **world function** $\Pi$, the joint system $\Pi=0$, $d\Pi/dG=0$ defines the locus on which $G(\Pi)$ branches — that is, the set on which the four-gradient of the eikonal blows up. Resolving that algebraic system gives the singular set even when $G$ has no closed form, and it is the same locus that carries the singularities of the associated gauge and curvature fields.

**Both classes, from one differentiation.** The two procedures are one computation. Differentiate the identity $\Pi(G,wG+\upsilon,vG+p)=0$ with respect to each of the four twistor coordinates, and write $P=d\Pi/dG\equiv\Pi_G+w\Pi_1+v\Pi_2$, the quantity called $\Delta$ in the companion mathematical article, and $\Pi_1,\Pi_2$ for the derivatives of $\Pi$ with respect to its two remaining arguments; then

$$
P\frac{\partial G}{\partial\upsilon}=-\Pi_1,\qquad P\frac{\partial G}{\partial w}=-G\,\Pi_1,\qquad P\frac{\partial G}{\partial p}=-\Pi_2,\qquad P\frac{\partial G}{\partial v}=-G\,\Pi_2 .
$$

Multiplying the first by the fourth and the second by the third,

$$
\frac{\partial G}{\partial\upsilon}\,\frac{\partial G}{\partial v}=\frac{\partial G}{\partial w}\,\frac{\partial G}{\partial p}=\frac{G\,\Pi_1\Pi_2}{P^2},
$$

which is the complex eikonal in null coordinates: the class-I field is eikonal because the two products are one. For a class-II solution the same differentiation is done at $P=0$, where $G$ stays at the double root and it is $\Pi$, not $G$, that varies,

$$
\frac{\partial\Pi}{\partial\upsilon}=\Pi_1,\qquad \frac{\partial\Pi}{\partial w}=G\,\Pi_1,\qquad \frac{\partial\Pi}{\partial p}=\Pi_2,\qquad \frac{\partial\Pi}{\partial v}=G\,\Pi_2 ,
$$

whose product is the same $G\Pi_1\Pi_2$, so the function $\Pi$ of the coordinates satisfies the eikonal directly. The branch set of the class-II field lies one derivative higher, at the multiple root of $P=0$ rather than of $\Pi=0$, which is $\Lambda=d^2\Pi/dG^2=0$. Both products were checked here on the quadratic world function $\Pi=G\kappa_0-\kappa_1+2iaG$, by implicit differentiation at random points of the domain, where both residuals vanish to finite-difference accuracy.

**Physical interpretation.** The twistor is thus not imported from twistor theory; it arises inside the programme as the algebraic variable in which the nonlinear eikonal linearises. This is a genuine structural agreement with the corpus's twistor article at the level of the incidence relation and the spinor, and a genuine divergence at the level of aim: the programme's twistor labels a solution of a **nonlinear** primary equation, whereas Penrose's twistor transform encodes linear massless fields and the conformal group.

## The Generating System and the Gauge Fields

The physically relevant class of differentiable functions is obtained by a **spinor splitting** of the two-sided condition. Writing the function matrix as $F=\{\eta_1,\eta_2\}$ and the right semi-derivative as $R=\{\zeta_1,\zeta_2\}$ reduces the matrix condition to two equations of the same type,

$$
d\eta_a = Ξ\, dZ\, \zeta_a , \qquad a=1,2 ,
$$

with a common field $Ξ$ (the left semi-derivative) transforming as a complex four-vector and $\eta,\zeta$ as $SL(2,\mathbb{C})$-spinors. Every solution of the full condition can be built from a solution of a **single** such spinor system with constant proportionality between the two pairs, so the physically nontrivial solutions all come from the **fundamental spinor system**

$$
d\eta = Ξ\, dZ\, \zeta .
$$

On the real slice $Z\mapsto X=X^{\dagger}$ with the Minkowski metric this is the **generating system of equations** (GSE) of the programme. It is a system of eight differential equations for six unknown functions — the two spinor components and the four components of $Ξ$ — and is therefore **over-determined**, which is the source of everything that follows.

The over-determination is not a defect but the mechanism. Differentiating the equation and using it again gives an integrability condition whose natural object is a connection. The field $Ξ$ defines a $\mathbb{B}$-valued connection one-form

$$
\Omega = \tilde{Ξ}_{\mathrm{sp}}\, dZ ,
$$

under which the spinor is covariantly constant, $d\zeta=\Omega\zeta$. This connection corresponds in the four-vector representation to an affine connection of Weyl–Cartan type, in which the Weyl non-metricity vector and the pseudotrace of the torsion are both expressed through $\tilde{Ξ}_{\mathrm{sp}}$. Exterior differentiation gives the integrability condition $R\zeta\equiv(d\Omega-\Omega\wedge\Omega)\zeta=0$, with the curvature two-form $R$.

The curvature is not zero. For a connection of this special form it is $R=(d\tilde{Ξ}_{\mathrm{sp}}-\tilde{Ξ}_{\mathrm{sp}} dZ\tilde{Ξ}_{\mathrm{sp}})\wedge dZ$, and requiring $R\zeta=0$ for the non-trivial spinor forces the **self-dual part of the curvature to vanish**. On the trace part, the electromagnetic field, the condition is written $\vec N=\vec E+i\vec H=0$,

$$
\boxed{\;\vec N = 0\;},
$$

on the solutions of the GSE — a property the source calls **weak (anti)self-duality**. The Bianchi identity then implies the free equations for the two pieces of the curvature: Maxwell's equations for its trace part, the electromagnetic field, and Yang–Mills equations for its trace-free part. In this sense the linear field equations are not postulated; they are the **integrability conditions of the primary nonlinear system**. Because the field is $\mathbb{C}$-valued but self-dual, it reduces to an ordinary real electromagnetic field by the algebraic relations $\Im\vec H=\Re\vec E$ and $\Im\vec E=-\Re\vec H$, which is a recomputation-verified equivalence, so the number of degrees of freedom is that of the real field.

Two further features are worth recording because they differ from the standard theory. The GSE is not invariant under the ordinary $\mathrm{U}(1)$ gauge transformations $\zeta\mapsto \exp(i\alpha)\zeta$, $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}}-i\nabla\ln\alpha$; it has instead a **weak gauge symmetry** in which the parameter depends on the coordinates only through the twistor components of the transformed spinor. And the trace-free gauge field is not independent of the electromagnetic one and the spinor; it is expressible through them, and its real and imaginary parts separately do not obey free Yang–Mills equations, because those are nonlinear.

**Physical interpretation.** This is the part of the programme most directly comparable with the corpus's gauge articles. The corpus derives the Maxwell and Yang–Mills equations from a **postulated** gauge principle, with the connection and curvature put in by hand (*The Gauge Principle in Biquaternionic Form*, *Gauge Curvature and the Bianchi Identity in Biquaternionic Form*). The programme reverses the direction of explanation: the connection and its self-duality are forced by the over-determined nonlinear system, and the linear gauge equations are consequences. Whether that reversal is an advance or a reformulation is a judgement the corpus does not make; it is recorded as the programme's structural claim.

## The Weyl–Cartan Geometry of the Programme

The programme's first full presentation, Kassandrov's 1995 paper *Biquaternion Electrodynamics and the Weyl–Cartan Geometry of Space-Time*, states the same construction geometrically, and it carries three results the later survey only recalls. Its setting is the spinor form of the primary equation. The fundamental spinor system is a parallel-transport condition,

$$
\partial/\partial x_\nu\,\tilde{Ξ}_{\mathrm{sp}} = \Gamma_\nu(r_x)\,\tilde{Ξ}_{\mathrm{sp}}(r_x), \qquad \Gamma_\nu(r_x) = G(r_x)\,\varsigma_\nu ,
$$

whose $\Gamma_\nu$ is a two-spinor connection of a special type: it is built from the field $G$ alone. (The source's basis is $\sigma_\nu$; it is written $\varsigma_\nu$ here because $\sigma$ is already the principal invariant of the complex three-space below.) Its opening geometric observation is Clifford-theoretic. The biquaternion algebra is the Clifford algebra $\mathrm{Cl}_{3,0}$ — the corpus's own identification, in *The Number Systems as Clifford Algebras* — of real dimension eight, and the source argues that it, and not the sixteen-dimensional $\mathrm{Cl}_{1,3}$, is the natural space-time algebra: the reduction from the full Clifford algebra to a physical four-dimensional space is, in its word, voluntaristic, and the signature of the generator space may be chosen in more than one way. (The corpus's Clifford article makes the same identification and records the competing labelling; what the source adds is the argument for $\mathrm{Cl}_{3,0}$ as primary rather than as the even part of $\mathrm{Cl}_{1,3}$.)

Writing the same equation for the matrix field $F$ and passing to a four-vector representation turns the spinor condition into a covariant-constancy condition $\partial/\partial x_\nu F_\mu = \Gamma_{\mu\nu\rho}(r_x)F_\rho$, all slots low and the output slot first, with the affine connection

$$
\Gamma_{\mu\nu\rho}(x) = 2\bigl(A_\nu\delta_{\mu\rho} + A_\rho\delta_{\mu\nu} - A_\mu\delta_{\nu\rho} - i\,\varepsilon_{\mu\nu\rho\alpha}A_\alpha\bigr),
$$

where $A_\mu = 2G_\mu$ is the electromagnetic four-potential identified in the preceding section and the potential fixes the whole connection: its Weyl part and its torsion alike. In this language the integrability condition of the spinor equation is $\mathrm{Ric}_{\mu\nu}\tilde{Ξ}_{\mathrm{sp}} = 0$ with $\mathrm{Ric}_{\mu\nu} = \tfrac12\left(\partial/\partial x_\mu\,\Gamma_\nu-\partial/\partial x_\nu\,\Gamma_\mu\right) - [\Gamma_\mu,\Gamma_\nu]$, and the weak self-duality of the preceding section is the statement that the self-dual part of $\mathrm{Ric}_{\mu\nu}$ vanishes.

**The $*$-unitary field, and why the geometry is real.** The connection just written is complex. Squaring the matrix field to the *$*$-unitary field* $\mathcal{U}(x)=F(x)F^{*}(x)$ replaces it by a real one. If $F$ obeys the covariant-constancy condition then $\mathcal{U}$ obeys the same-shaped condition,

$$
\partial/\partial x_\nu \mathcal{U}_\mu = \Delta_{\mu\nu\rho}(r_x)\,\mathcal{U}_\rho(r_x), \qquad
\Delta_{\mu\nu\rho}(r_x) = 2\bigl(a_\nu\delta_{\mu\rho} + a_\rho\delta_{\mu\nu} - a_\mu\delta_{\nu\rho} - \varepsilon_{\mu\nu\rho\alpha}b_\alpha\bigr),
$$

where $a_\mu=\Re A_\mu$ and $b_\mu=\Im A_\mu$ are the real and imaginary parts of the potential. Two things happen at once: the Hermitian squaring discards the imaginary part of the connection, leaving a **real** affine connection on space-time; and the imaginary part reappears beside it as a separate field, so that the connection carries a Weyl non-metricity vector $a_\mu$ *and* a torsion pseudotrace $b_\mu$. The source reads the pair physically. The Weyl part $a_\mu$ is the ordinary Coulomb field — which is the reason the electromagnetic field was identified with the real part of $A_\mu$ in the first place — and the torsion part $b_\mu$ is a second field: for the static solution below, $b_0=b_r=b_\theta=0$ and $b_{\mathrm{azm}}$ is its potential. Since torsion does not enter the equations of geodesics, the source concludes that a field built this way would have **no effect on test-particle motion** and would be "entirely unobservable". The corpus records that claim and does not adopt it.

The connection is not idle. The source notes that the same connection had been obtained earlier from physical requirements by Obukhov, Krechet and Ponomariev, and that Stepanov showed it to be the **only** space-time connection compatible with a spinor-bundle structure carrying the conventional covariant spinor derivative. In the algebrodynamical interpretation that uniqueness is not an input: the connection, its Weyl part, its torsion, and the identification of the parts with the electric and magnetic fields all follow from the generalized Cauchy–Riemann condition alone. It is worth recording that the central object here is one the corpus already uses — the spin connection of *The Covariant Derivative and Gauge Connection in Biquaternionic Form* — reached from the other end.

**The inhomogeneous Lorentz condition.** The integrability conditions of the primary system include, beside the self-duality $\vec P\equiv\vec E+i\vec B=0$, the condition

$$
D \equiv \sum_\mu \partial/\partial x_\mu A_\mu + 2\sum_\mu A_\mu A_\mu = 0 ,
$$

an **inhomogeneous Lorentz condition**: not the usual gauge choice $\sum_\mu \partial/\partial x_\mu A_\mu = 0$ but a nonlinear condition with a term quadratic in the potential, and part of the system rather than a gauge. The source observes that $D$ is proportional to the curvature invariant $6\delta_{\mu\nu}\mathrm{Riem}_{\alpha\,\mu\alpha\nu}$ — so the condition says the effective space has **zero scalar curvature**, and together with the self-duality that it is self-dual. Both the proportionality and the self-duality of the curvature are the source's statements about the solutions of its system; the second is the weak self-duality already recorded above, and neither the proportionality nor the explicit form of the connection was recomputed in this pass, because it holds on the solutions of the primary system and no such solution was constructed here.

**Rigidity, null divisors, and the signature.** The geometric interpretation also exposes why the non-trivial solutions must be degenerate. If the spinor equation has two linearly independent solutions then $\mathrm{Ric}_{\mu\nu}=0$ — the effective geometry is flat and the field strengths vanish. Non-trivial dynamics therefore requires the two spinors of the splitting to be proportional, and proportionality means $\det F(x)=0$: the primary field takes its values on the **null divisors** of the algebra, the complex light cone, exactly as the degeneracy of the two-sided condition already required. The null fields, the source observes, exist **only on manifolds of indefinite metric signature**. That is the sharpest form of a claim the corpus meets elsewhere as a motivation: in the programme the pseudo-Euclidean signature is **not postulated** but is a necessary condition for a non-trivial field to exist at all, which is the boundary stated in *Why Complexify Spacetime?*.

## The Local Algebra on a Curved Manifold, and the Unit Field

The programme's later conference note *Relativistic Algebra of Space-Time and Algebrodynamics* (Kassandrov and Rizcallah, arXiv:1612.02455, 2016, five pages) adds one ingredient the presentation above does not have: the **local** form of the algebra, in which the multiplication itself becomes a structure attached to a point of a manifold. Everything the note recovers from the 1995 presentation — the generating system, the weak self-duality, the inhomogeneous Lorentz condition, the Weyl–Cartan interpretation of the connection, the free Maxwell, Yang–Mills and Weyl equations as its consequences — is already recorded above and is not repeated. What is new is the algebra, and it is the part of the programme in which the algebra is treated as a **ring extension** of the kind studied outside it.

**The covariant multiplication law.** The note starts from the four-dimensional associative algebra $G$ proposed by E. Grgin (*Physics Letters B* **431** (1998) 15), whose multiplication is written in the manifestly covariant form

$$
(a\circ b)_\mu = a_\mu\,(b_\rho e_\rho) + b_\mu\,(a_\rho e_\rho) - e_\mu\,(a_\rho b_\rho) \pm i\,\varepsilon_{\mu\nu\rho\lambda}\,a_\nu b_\rho \exp(\lambda) ,
$$

with the flat metric $g_{\mu\nu}=\varepsilon_\mu\delta_{\mu\nu}$ — the plain weight on the diagonal — the Levi-Civita symbol $\varepsilon$, and a **distinguished element** $e=\{e_\mu\}$ of $G$ constrained by $e_\mu e_\mu=1$, so that $a\circ e=e\circ a=a$ and $e$ is the unit. The note's point about the record is that with $e=(1,0,0,0)$ this law *is* the multiplication of the biquaternion algebra $\mathbb{B}$, so that Grgin's $G$ is isomorphic to $\mathbb{B}$ — an identification, the note says, overlooked in the paper that introduced the algebra. It was checked here and it is exact. Representing the algebra on $\mathbb{C}^2$ by $\sigma_0=I$ and the Pauli matrices, with $g_{\mu\nu}=\varepsilon_\mu\delta_{\mu\nu}$ and $\varepsilon_{0123}=+1$: on a hundred random complex pairs the law with the **lower** sign reproduces the $2\times2$ matrix product to $2\times10^{-15}$, and the law with the **upper** sign reproduces the *reversed* product $b\cdot a$ to the same accuracy. The two signs are therefore the algebra and its opposite — in the source's words the signs "correspond to the left or right forms of the (bi)quaternion algebra" — and the isomorphism with $\mathbb{B}$ holds either way.

Two interpretations in the printed note must be fixed before the law can be used. First, the $\pm$ of the general law and of the space-like block $\sigma_a\circ\sigma_b=\delta_{ab}e\pm i\varepsilon_{abc}\sigma_c$ are **not** synchronized: the block with the upper sign is the Pauli product $\sigma_a\sigma_b=\delta_{ab}e+i\varepsilon_{abc}\sigma_c$, and the law produces it with the **lower** sign (checked exactly on all nine pairs of space-like units; the upper sign gives the negative of it). Second, the last term must be read with the dual unit $\exp(\lambda)$ — the interpretation under which the note's own Lorentz-covariance claim is true — and not with $e_\lambda$. On a hundred random Lorentz transformations — boosts, three-rotations and their products — acting on $a$, $b$ and $e$ together, the product transforms as a covector with residual $8\times10^{-15}$ when the contraction is with $\exp(\lambda)$, and fails by order $20$ when the symbol is misread as $e_\lambda$. The law is thus "manifestly Lorentz invariant" in the precise sense that its coefficients are the invariant weight $\varepsilon_\mu\delta_{\mu\nu}$ and the Levi-Civita symbol, and its last contraction is with the dual unit; the covariance of the product follows, and was verified in that strong form. Its automorphisms at fixed $e$ include the three-rotations, as the source states (checked on a hundred rotations).

**The local algebra and the unit field.** The covariant form is what allows the algebra to be attached to a manifold. Introduce a tetrad $h_{\alpha\,\mu}(x)$, $\alpha=0,1,2,3$, and the **local $L$-algebra** whose basis vectors are the tetrad legs in the abstract basis $\sigma_\alpha$,

$$
\Sigma_\mu(x) := h_{\alpha\,\mu}(x)\,\sigma_\alpha ,
$$

so that the multiplication table keeps the shape of the flat one, with the flat metric replaced by the metric the tetrad induces,

$$
g_{\mu\nu}(x) := h_{\alpha\,\mu}(x)\,h_{\beta\,\nu}(x)\,\varepsilon_\alpha\delta_{\alpha\beta} ,
$$

and the unit element replaced by the unit **field** $E_\mu(x) := h_{\alpha\,\mu}(x)\,e_\alpha$, constrained by $(g^{-1})_{\mu\nu}E_\mu E_\nu=1$. The construction exposes a fact the flat presentation hides: the existence of the local algebra on a four-manifold requires, beside the metric, a **unit time-like vector field** — the source's *unit field* — because the unit element of the algebra is a field. The source reads the unit field physically as the flow of matter ("its **physical interpretation** may be related to the flow of matter") and observes that the same data appear in Weyl geometry, where a metric is accompanied by a non-metricity one-form. The unit field here is not the corpus's **$*$-unitary field** of the section above: there $\mathcal{U}=FF^\dagger$ is built *from* the primary field and the geometry follows; here the unit field belongs to the geometry and the algebra is attached to it.

**The effective metric, and a metric built from the multiplication table.** Two metrics accompany the local algebra. The first the note calls the **effective metric**,

$$
g_{\mathrm{eff},\rho\lambda} := 2E_\rho E_\lambda - g_{\rho\lambda} ,
$$

whose flat case the source calls "rather surprising" and which is exact: for $g_{\mu\nu}=\varepsilon_\mu\delta_{\mu\nu}$ and $E=(1,0,0,0)$, $g_{\mathrm{eff}}=\mathrm{diag}(1,1,1,1)$ — the effective metric of the flat limit is the **four-dimensional Euclidean** metric, not the Minkowski one, and the note observes that the Euclidean structure survives the generalization to a curved manifold. Two elementary properties follow from the definition and fix what the object is: the map $g\mapsto 2E\otimes E-g$ is an **involution**, so $g_{\mathrm{eff}}$ is the reflection of $g$ in the $E$ direction; and $g_{\mathrm{eff}}=g$ would require $g_{\mu\nu}=E_\mu E_\nu$, a rank-one form, so no metric is a fixed point and the two are never degenerate together.

The second metric is algebraic. The **structure functions** of the local algebra are defined by $\Sigma_\mu\circ\Sigma_\nu=C_{\rho\mu\nu}\Sigma_\rho$, with every slot low and the output slot written first,

$$
C_{\rho\mu\nu} = \delta_{\rho\mu} E_\nu + \delta_{\rho\nu} E_\mu - E_\rho g_{\mu\nu} \pm i\sqrt{-g}\,\varepsilon_{\rho\mu\nu\lambda}E_\lambda ,
$$

and from them the source forms

$$
g^*_{\mu\nu} := \tfrac14\, C_{\beta\,\mu\alpha} C_{\alpha\,\nu\beta} .
$$

The note's "**remarkable coincidence**" is that $g^*$ is the same tensor as the effective metric $g_{\mathrm{eff}}$, and the note hedges it: the equality is stated "at least in the case $g=|g_{\mu\nu}|=-1$", that is, for any metric of determinant $-1$. **The hedge cannot be removed.** The identity is exact, but it holds in the frame in which the unit field is the time leg and it fails as soon as $E$ is tilted, and the failure is exact too.

**What is exact.** In the rest frame of the unit field, where $E=(1,0,0,0)$, the tensor $g^*$ is the identity matrix $\mathrm{diag}(1,1,1,1)$, which is $g_{\mathrm{eff}}$ there. That holds for each of the eight ways of distributing lower and upper index positions among the three occurrences of $E$ in $C_{\rho\mu\nu}$, and for either sign of the $\varepsilon$ term. The $\varepsilon$ term does not drop out in that frame — for $E=(1,0,0,0)$ it is non-zero on six of the sixty-four entries of $C$ — it cancels; and it is needed, because dropping it leaves $g^*=\mathrm{diag}(1,\tfrac12,\tfrac12,\tfrac12)$ and the identity already fails in the rest frame. So the rest-frame identity is a statement about the two terms together, not about a metric part alone.

**What fails.** For a tilted unit field every one of those eight readings fails. With the printed form above, $g_{\mu\nu}=\varepsilon_\mu\delta_{\mu\nu}$ and $E=(a,b,c,0)$ with $a^2-b^2-c^2=1$, the difference is exactly

$$
g^*_{\mu\nu} - g_{\mathrm{eff},\mu\nu} =
\begin{pmatrix}
-b^2-c^2 & -ab & -ac & 0\\
-ab & 2(b^2+c^2) & 0 & 0\\
-ac & 0 & 2(b^2+c^2) & 0\\
0 & 0 & 0 & 2(b^2+c^2)
\end{pmatrix},
$$

the case $c=0$, $b=\tfrac43$, $a=\tfrac53$ giving $\mathrm{diag}(-\tfrac{16}{9},\tfrac{32}{9},\tfrac{32}{9},\tfrac{32}{9})$ with off-diagonal $-\tfrac{20}{9}$ at $(0,1)$, as checked in exact rational arithmetic. The discrepancy is quadratic in the spatial part of $E$ and vanishes identically only when that part vanishes. A boost tilts $E$ while leaving $g_{\mu\nu}=\varepsilon_\mu\delta_{\mu\nu}$, so a Lorentz-transformed rest frame is already a counterexample. The reading recorded in an earlier version of this article — that the identity holds for an arbitrary unit field to $4\times10^{-15}$ — was therefore wrong, and the likely cause is visible here: the random draws that supported it were rotations of the spatial frame, which leave $E=(1,0,0,0)$ untouched, so the identity was being checked where it is trivial.

**What the coincidence then amounts to.** It is the statement that in the rest frame of the unit field the trace form of the structure constants is the **Euclidean** metric. That is the same content as the flat case of $g_{\mathrm{eff}}=\mathrm{diag}(1,1,1,1)$ recorded in the paragraph above, so it is not a second, independent derivation of the effective metric: $C$ is built from $g$ and $E$, and $g^*$ returns them in one particular frame. Whether an added term built from $E$, $g$ and $\varepsilon$ restores the identity for tilted $E$ the note does not ask, and if one exists the computation above says it must be quadratic in the spatial part of $E$. The part of the reading that survives is structural and does not depend on the identity: $g_{\mathrm{eff}}$ is the metric the connection below is built from, while $g^*$ is computed from the multiplication table alone. What does not survive is the claim that the same tensor arrives twice for a general unit field. This is a mathematical identity in one frame, and not a dynamical statement: nothing in the note makes $g_{\mathrm{eff}}$ the physical metric, and nothing in it selects $E$.

**The induced connection, and its non-metricity.** The note's remaining new ingredient is the curved form of the differentiability condition. Where the flat case writes $dF=Ξ(X)\circ dX\circ F(X)$ with the ordinary differential, the curved case writes

$$
\mathrm{D}F = Ξ(Z)\circ dX\circ F(Z) ,
$$

with $\mathrm{D}$ the covariant differential with respect to $g$ — that is, with respect to the Levi-Civita connection $\gamma$ — and then, exactly as in the flat case, the condition says that a vector field is **covariantly constant** with respect to an induced connection $\Gamma$, which splits as

$$
\Gamma = \gamma + G ,
$$

with $G$ of the same shape as the flat connection recorded above, $e$ and the flat metric replaced by $E$ and $g$:

$$
G_{\rho\nu\mu} = \delta_{\rho\nu} A_\alpha(2E_\mu E_\alpha - g_{\mu\alpha}) - A_\nu g_{\beta\rho}(2E_\mu E_\beta - g_{\mu\beta}) \pm i\sqrt{-g}\bigl\{\varepsilon_{\rho\alpha\nu\gamma}E_\mu + \varepsilon_{\rho\alpha\mu\gamma}E_\nu - \varepsilon_{\rho\nu\mu\gamma}E_\alpha + \varepsilon_{\alpha\nu\mu\gamma}E_\rho\bigr\}E_\gamma A_\alpha + A_\rho(2E_\nu E_\mu - g_{\nu\mu}) .
$$

Two of its properties are already familiar from the 1995 paper and are now seen to be the general case. First, $G$ is **not symmetric under the exchange of its two last labels**, so the induced connection has **torsion** — the totally skew-symmetric part carried by the $\varepsilon$ terms, which is the part the preceding section reads as the torsion field. Second, the covariant derivative of the metric does not vanish:

$$
\nabla_\rho g_{\mu\nu} = -2\,g_{\mu\nu}\,\tilde A_{\Phi,\rho} , \qquad \tilde A_{\Phi,\rho} := (2E_\rho E_\lambda - g_{\rho\lambda})A_\lambda = g_{\mathrm{eff},\rho\lambda}A_\lambda ,
$$

a **Weyl-type non-metricity** whose vector is not the potential $A_\rho$ itself but the potential read through the effective metric, $\tilde A_{\Phi}=g_{\mathrm{eff}} A$. Read out in components the definition gives $\tilde A_{\Phi,\rho}=2E_\rho\sum_\lambda E_\lambda A_\lambda-\varepsilon_\rho A_\rho$, so $\tilde A_{\Phi}$ is $A$ carried by the same reflection that takes $g$ to $g_{\mathrm{eff}}$. It equals $A_\rho$ slot by slot precisely when $E$ is the time leg, $E=(\pm1,0,0,0)$ — the rest frame, where the effective metric is the unit metric and the contraction returns the potential's own components — and it departs from $A$ by $2E_\rho\sum_\lambda E_\lambda A_\lambda$ in the space-like slots and by $2\bigl(E_0\sum_\lambda E_\lambda A_\lambda-A_0\bigr)$ in the time-like one as soon as $E$ is tilted. The comparison with the 1995 interpretation is the reason for recording the formula: there the non-metricity vector is the potential $A_\mu$ itself, here it is $A_\mu$ read through the metric into which the unit field deforms $g$, and the note's geometry differs from the 1995 geometry in exactly those frames in which $E$ is not the time leg.

**What the note leaves open.** The note states its own programme for the construction: the integrability conditions of the $L$-differentiability equations "might impose restrictions not only on the vector field $A_\mu$, but also on the metric $g_{\mu\nu}$ as well as the unit vector field $E_\mu$", and if they do, the physical geometry would be determined "in a purely algebraic way". That analysis is explicitly "left for future work". The corpus records the hope and not the result: the local algebra, as the note uses it, is a language in which a given metric and a given unit field may be written, and the note exhibits no condition that selects either. The section records an extension of the programme's algebra rather than a new physical claim, and it changes nothing in the corpus's interpretation of the programme.

## The Yang–Mills Triplet and the Electromagnetic Modulus

The trace-free part of the spinor connection is a gauge field in its own right, and the source exhibits it explicitly. Splitting

$$
\Gamma_\nu(x) = \tfrac12 A_\nu(x) + N_\nu(x)
$$

into trace and trace-free parts, the trace-free part $N_\nu = \sum_a N_{\nu a}\varsigma_a$ is expressed **linearly** in the electromagnetic potential:

$$
N_{0a} = A_a, \qquad N_{ba} = \delta_{ab}A_0 - i\varepsilon_{abc}A_c .
$$

The triplet index is low and last, $N_{\nu a}$ and $L_{\mu\nu a}$, and every sum over it is written out. A single complex four-vector $A_\mu$ therefore carries both the electromagnetic potential and a complex triplet of matrix potentials. The strength of the triplet field is $L_{\mu\nu}=\sum_a L_{\mu\nu a}\varsigma_a=\tfrac12\left(\partial/\partial x_\mu\,N_\nu-\partial/\partial x_\nu\,N_\mu\right)-[N_\mu,N_\nu]$, and it inherits the self-duality, $L_{\mu\nu}+\tfrac{i}{2}\varepsilon_{\mu\nu\rho\lambda}L_{\rho\lambda}=0$ on the solutions, from which the Bianchi identity gives the Yang–Mills equation $\partial/\partial x_\nu L_{\mu\nu}=[N_\nu,L_{\mu\nu}]$.

The link between the two fields is a determinant. The curvature matrix splits as $\mathrm{Ric}_{\mu\nu}=(\text{trace part})+L_{\mu\nu}$, with the trace part proportional to the electromagnetic field strength $F_{\mu\nu}=\partial/\partial x_\mu A_\nu-\partial/\partial x_\nu A_\mu$ (the index-carrying strength, to be read apart from the matrix field $F$ itself), and the condition $\det \mathrm{Ric}_{\mu\nu}=0$ — which holds because the non-trivial spinor lies in its kernel — becomes an algebraic relation between the two invariants. In components the source writes it as

$$
\sum_a L_{\mu\nu a}L_{\mu\nu a} = (F_{\mu\nu})^2 ,
$$

so the electromagnetic field strength is the **modulus of the Yang–Mills triplet** in the complexified isotopic three-space: the abelian field is not a separate object but the length of the non-abelian one. The determinant identity behind this is elementary and exact — for a $2\times2$ matrix $\lambda I + L$ with $L$ traceless, $\det(\lambda I+L)=\lambda^2-(L_1)^2-(L_2)^2-(L_3)^2$, verified symbolically here — so the relation is one of proportionality, the coefficient being fixed only once the antisymmetrisation convention and the normalisations of the potentials and the field strength are fixed. Substituting the source's own definitions, $\mathrm{Ric}_{\mu\nu}=\tfrac12\left(\partial/\partial x_\mu\,\Gamma_\nu-\partial/\partial x_\nu\,\Gamma_\mu\right)-[\Gamma_\mu,\Gamma_\nu]$ with $\Gamma_\nu=\tfrac12A_\nu I+N_\nu$ and the antisymmetrised derivative read as $\tfrac12(\partial/\partial x_\mu\,\Gamma_\nu-\partial/\partial x_\nu\,\Gamma_\mu)$, gives the trace part $\tfrac14F_{\mu\nu}I$ and hence $\sum_a(L_{\mu\nu a})^2=\tfrac1{16}(F_{\mu\nu})^2$, whereas the source prints coefficient one. **The factor is not a discrepancy**: both are the determinant identity $\det(cF\,I+L)=(cF)^2-\sum_a(L_a)^2=0$, which returns $\sum_a(L_a)^2=c^2F^2$, evaluated with the two trace coefficients — $c=\tfrac14$ here and $c=1$ in the source — and $\tfrac{1}{16}=(\tfrac14)^2$ exactly. The source's coefficient is therefore a statement of the **modulus relation** in its own normalisation, and the two are one identity, not two numbers to be averaged. The closure is spelled out, with the triplet components that the identity needs, in *Congruence Twistors and the Fields They Generate*. Unlike the electromagnetic field, the source observes, a complex Yang–Mills field cannot be split into real and imaginary parts, because the Yang–Mills equation is nonlinear; the reality that self-duality supplies to electromagnetism is not available to the non-abelian field.

**Physical interpretation.** This is the most concrete of the programme's unification statements, and the most literal: the electromagnetic potential is the trace part of a biquaternion connection and the gauge triplet is its trace-free part, with the abelian and non-abelian field strengths tied by a determinant. It is not the corpus's *The Yang–Mills Equation in Biquaternionic Form*, where a Yang–Mills field is packaged after being given independently; here the non-abelian field has no independent existence, and the electromagnetic field is the modulus of the triplet. The claim is the source's, conditional on the primary system, and it is recorded as the programme's rather than as a result of this corpus.

## The Kerr Equation and the Shear-Free Congruences

Eliminating the potentials from the GSE leaves a system for the principal spinor alone. Multiplying the GSE by the orthogonal spinor and using the skew symmetry of the spinor norm gives a system whose restriction to the real slice is the classical equation of a **shear-free null congruence** of rays,

$$
\sum_{B,C}\zeta_B\zeta_C\nabla_{AB}\zeta_C = 0 .
$$

The source notes that the GSE system is more rigid than the shear-free condition only in the gauge fixing of the spinor, and equivalent to it for the ratio of the spinor components. The general solution of the shear-free condition on Minkowski space is the **Kerr theorem**: the congruence is given by an arbitrary homogeneous function of the twistor arguments, through the implicit algebraic equation $\Pi(\zeta,Z\zeta)=0$. For the GSE the corresponding equation for the ratio $G$ of spinor components is the **Kerr equation**

$$
\Pi(G,\,wG+\upsilon,\,vG+p) = 0 ,
$$

in which $\Pi$ is an arbitrary holomorphic function of three complex twistor variables. This is the same $\Pi$ as in the eikonal section seen from the field side, and the equivalence is exact: the solutions satisfy the pair of partial differential equations

$$
\frac{\partial G}{\partial w}=G\,\frac{\partial G}{\partial\upsilon} , \qquad \frac{\partial G}{\partial v}=G\,\frac{\partial G}{\partial p} ,
$$

and multiplying them gives back the complex eikonal, while differentiating them gives the linear wave equation for $G$,

$$
\left(\frac{\partial^2}{\partial\upsilon\,\partial v}-\frac{\partial^2}{\partial w\,\partial p}\right)G = 0 .
$$

Consequently every $C^2$ function $\lambda(G)$ is harmonic on the solutions, since the eikonal supplies the quadratic term and the wave equation the linear one. In this pass the whole chain was recomputed on an explicit solution of the quadratic Kerr equation $\Pi=wG^2+(\upsilon-v)G-p$: the two first-order equations, the complex eikonal, the wave equation, and the harmonicity of $\ln G$ all hold to finite-difference accuracy.

The electromagnetic field strengths are then the second derivatives of $\ln G$,

$$
F_{00}=\frac{\partial^2\ln G}{\partial\upsilon\,\partial p},\quad F_{11}=\frac{\partial^2\ln G}{\partial v\,\partial w},\quad F_{01}=\frac{\partial^2\ln G}{\partial w\,\partial p} ,
$$

so that Maxwell's equations for the field follow from the harmonicity of $\ln G$. The sharpest form of the result is the source's representation of the field through the twistor variables,

$$
F_{AB} = \frac{1}{P}\,\Pi_{AB} - \frac{1}{P}\,\frac{d}{dG}\left(\frac{\Pi_A\Pi_B}{P}\right), \qquad P := \frac{d\Pi}{dG},
$$

which the source presents as having no analogue in the literature: the field of a solution is computed from the **generating function alone**, without solving the Kerr equation.

A further structure attaches to the congruence. The flat metric can be deformed into a **Kerr–Schild metric** $g_{\mu\nu}=\delta_{\mu\nu}+h\,\ell_\mu \ell_\nu$ with the null congruence $k$ as its repeated principal direction, and for generating functions linear in the twistor arguments the metric satisfies the **electrovacuum Einstein–Maxwell** equations of Debney, Kerr and Schild. The locus on which the congruence's $G$ branches — the condition $P=d\Pi/dG=0$ — is simultaneously the singularity of the effective curvature, of the electromagnetic field, and of the Yang–Mills field. The programme reads this coincidence as the statement that a **particle is a common singularity of all the associated fields**, and it is the geometric heart of the particle interpretation. The source states one qualification: the associated Yang–Mills fields carry, generically, additional **string-like singularities**, so the coincidence of loci is exact for the curvature and electromagnetic fields and is not claimed for the non-abelian ones.

**The family, and what the congruence does not fix.** A congruence carries more than one Maxwell field, and the construction is a generation of the congruence rather than of its electromagnetic content. Let $\mathcal{D}:=\partial/\partial w-G\,\partial/\partial\upsilon$ be the ray derivative. The shear-free equation $\partial G/\partial w=G\,\partial G/\partial\upsilon$ makes $\mathcal{D}$ a derivative along the ray and gives $\mathcal{D}G=0$, hence

$$
\mathcal{D}F(G)=F'(G)\,\mathcal{D}G=0
$$

for every holomorphic $F$. Take the spinor from the pair $(\upsilon,w)$ — a different representation of the field from the $\ln G$ one above, which uses $(\upsilon,p)$, $(w,p)$ and $(v,w)$, so the two displays must not be read as the same components:

$$
\tilde{Ξ}_{\mathrm{sp},\upsilon\upsilon}=\frac{\partial^2F}{\partial\upsilon^2},\qquad \tilde{Ξ}_{\mathrm{sp},\upsilon w}=\frac{\partial^2F}{\partial w\,\partial\upsilon},\qquad \tilde{Ξ}_{\mathrm{sp},ww}=\frac{\partial^2F}{\partial w^2} .
$$

The alignment condition is then the vanishing of

$$
\tilde{Ξ}_{\mathrm{sp},ww}-2G\,\tilde{Ξ}_{\mathrm{sp},\upsilon w}+G^2\tilde{Ξ}_{\mathrm{sp},\upsilon\upsilon}=\mathcal{D}^2F ,
$$

which is the second derivative along the ray and vanishes because $\mathcal{D}F=0$ identically on the congruence: one application of the shear-free equation, with no further hypothesis. This is exactly the source's argument, whose quantity $M:=G\,\partial G/\partial\upsilon-\partial G/\partial w$ is $-\mathcal{D}G$. The Maxwell equations then hold for every $F$, on the eikonal and the wave equation displayed above; they were checked here at a numerical point for $F=G^{-1}$, $G$, $G^2$, $e^G$, $\tan G$ and $\ln G$. The choice $F=G^{-1}$ gives

$$
\tilde{Ξ}_{\mathrm{sp},\upsilon\upsilon}=\mp\frac{1}{4}\frac{w}{r^3},\qquad \tilde{Ξ}_{\mathrm{sp},\upsilon w}=\pm\frac{1}{4}\frac{z}{r^3},\qquad \tilde{Ξ}_{\mathrm{sp},ww}=\pm\frac{1}{4}\frac{p}{r^3},
$$

exactly, which is the Coulomb spinor of the elementary charge in the 1998 normalisation, and it is the only choice that inherits the spherical or axial symmetry of the congruence.

**The negative statement, and its positive face.** The congruence does not fix the field, and neither does a Kerr–Schild background. For $g_{\mu\nu}=\delta_{\mu\nu}+h\,\ell_\mu \ell_\nu$ with $k$ null one has $\det g=\det\delta$ and $g^{\mu\nu}=\delta_{\mu\nu}-h\,k^\mu k^\nu$, so the contravariant field strength is unchanged iff $F_{\mu\nu}k^\nu\propto \ell_\mu$, which is exactly the alignment above. One congruence therefore carries a whole holomorphic function's worth of Maxwell fields, each of them a solution of the homogeneous equations in the same Kerr–Schild background — the reason the Coulomb field is the same in Reissner–Nordström as in flat space, and the reason a Maxwell field cannot be read off its background. These fields are **not null**: for $F=G^{-1}$ the spinor determinant is $\tilde{Ξ}_{\mathrm{sp},\upsilon\upsilon}\tilde{Ξ}_{\mathrm{sp},ww}-\tilde{Ξ}_{\mathrm{sp},\upsilon w}^2=-1/(16r^4)$, so the family is disjoint from the null one of *Null Electromagnetic Fields and the Shear-Free Congruence*, where the determinant vanishes identically.

**Physical interpretation.** The Kerr–Schild deformation and the Kerr theorem are classical general-relativistic objects, and the corpus's *Curved Spacetime and the Biquaternion Framework* describes the framework's own relation to curvature separately. What is new here is not the geometry but the **generation**: the metric, the electromagnetic field and the Yang–Mills field all descend from one holomorphic function of a twistor, and their singularities coincide — with the qualifier of the preceding paragraph, that the twistor function fixes the congruence and the field only once $F$ is chosen.

## Particle-Like Solutions and the Self-Quantized Charge

The programme's headline claim is that the singular solutions of the GSE have **quantised electric charge**. The mechanism is explicit and rests on the self-duality of the curvature together with the weak gauge invariance of the GSE: the two conditions restrict the admissible charge of the electromagnetic field associated with any GSE solution to

$$
\boxed{\;ϙ = \frac{N}{4}, \qquad N\in\mathbb{Z}\;},
$$

in the dimensionless units of the programme. The source states that the quantization has both topological and dynamical reasons, the dynamical one being the over-determined structure of the GSE itself. The general theorem behind the claim, its proof, and the exact reason the fundamental solution sits at the quantum are recorded at the end of this section.
The **fundamental static solution** is the one that makes the claim concrete. It is generated by the function

$$
\Pi = G\,\kappa_0 - \kappa_1 + 2ia\,G, \qquad a=\mathrm{const}\in\mathbb{R},
$$

which contains no time coordinate. Resolving the quadratic Kerr equation and restricting to real Minkowski space gives an explicit $G$, and the associated electromagnetic field has a **ring singularity** of radius $a$, the only admissible value of electric charge $|ϙ|=\tfrac14$, and magnetic and electric moments proportional to $qa$ and $qa^2$. For $a=0$ the solution degenerates to the stereographic projection $S^2\to\mathbb{C}$, and the field is the Coulomb field with the Reissner–Nordström metric. For $a\neq0$ the field and metric reproduce those of the **Kerr–Newman** solution. With the known gyromagnetic ratio $g=2$ of that solution, the ring singularity is the programme's classical model of the electron.

**The static member, and the source's instability argument.** The ring of the fundamental solution is the static member of a family. In a separate paper the source deforms the congruence by letting the virtual charge move uniformly along the imaginary direction of complex space, $z_0=-ia+ivr'_t$ (the source's $v$, not the twistor coordinate $v$ of this article), and the caustic becomes a ring of radius $\lvert vr'_t-a\rvert/\sqrt{1+v^2}$ that collapses to a point at $r'_t=a/v$ and re-expands at the sub-light speed $v/\sqrt{1+v^2}$ (arXiv:0908.1123; recomputed here, and recorded with its field and its spinor in *The Complex-Displaced Singularity and the Circle Electron*). Two consequences bear on the claims recorded here. The electric charge stays fixed at the elementary value throughout the motion, but the magnetic moment does not: it is proportional to the current radius, so that $\mu=qa$, the gyromagnetic ratio $g=2$ and the prediction $\lvert\vartheta\rvert=\frac{\hbar^{2}\,q}{2\,c^{2}\,M^{2}}$ belong to the static member $v=0$ and hold at best for a slow deformation. And the source reads the static congruence as **unstable**, since a small change of its parameters turns it into the expanding family; he concludes that the ring-as-electron reading is problematic, and conjectures a continuous transition from a naked ring to a rotating black hole and back. The corpus records the deformation and the caveat as the source's, and not the conjecture: the transition is to be settled by an exact solution of the Einstein–Maxwell equations, which the source does not give. One exact electrovacuum solution with a regular source does exist — the over-rotating Kerr–Newman bag of Burinskii (arXiv:1505.03439), an external general-relativistic construction, flat inside a disk-like bubble whose boundary sits at the classical electron radius $r_e=e^2/2m$ and exactly Kerr–Newman outside — but it regularizes the static member only, it keeps the ring as a cut-off string of radius $r_e$, and it gives no transition.

**The ring is the corpus's circle electron, and the two derivations are complementary.** The radius $a$ is not a new parameter: $r_*^2=x^2+y^2+(z+ia)^2$ is, up to the letters of the coordinate lattice, the radicand of *The Complex-Displaced Singularity and the Circle Electron*, where the same ring appears from displacing the singular point of the Coulomb potential along the imaginary direction of the vector coefficient, $\vec r_0=-i\varrho\,\vec e_z$. The zero sets agree term by term — imaginary part zero forces $z=0$, and the real part then gives $x^2+y^2=a^2$, so the radius is $a=\varrho$ — and both are the same statement in two languages: a point singularity moved off the real slice becomes a ring, because the complexified distance is the square root of a quantity whose zero set is a circle. What the two accounts supply is different and the difference should be kept. The corpus derives the geometry from the informational-sector displacement alone, with the charge an independent overall factor $ϙ/4\pi\epsilon$ and the radius $\varrho$ free; the programme derives the charge, $\lvertϙ\rvert=\tfrac14$, from the twistor condition on the generating function, and leaves $a$ free. Neither derivation gives what the other does, and the corpus's $\mathbb{B}_{\Psi}$ displacement is the simpler route to the ring the programme reaches through the Kerr congruence.

**The static solution in closed form, and the stereographic interpretation.** The 1995 presentation gives the static solution explicitly, and it is the stereographic map written as a function. The two static eikonal solutions are

$$
f^+ = \frac{r_x+ir_y}{r+r_z} = \tan\frac{\theta}{2}\,\exp(i\theta_{\mathrm{azm}}), \qquad
f^- = \frac{r_x-ir_y}{r-r_z} = \cot\frac{\theta}{2}\,\exp(-i\theta_{\mathrm{azm}}),
$$

the stereographic projection $S^2\to\mathbb{C}$ from the south and the north pole respectively. Each satisfies the static eikonal exactly, and this was recomputed: for $f^+$ the sum $(\partial/\partial r_x f)^2+(\partial/\partial r_y f)^2+(\partial/\partial r_z f)^2$ vanishes identically (verified symbolically in the present pass, together with $\lvert f^+\rvert^2=(r-r_z)/(r+r_z)$). Satisfying the eikonal is not sufficient for a generating function, and the distinction is worth stating here because $f^-$ is the natural counterexample: it satisfies the eikonal, but it fails the programme's two nonlinear constraints $\partial G/\partial w=G\,\partial G/\partial u$ and $\partial G/\partial v=G\,\partial G/\partial\bar w$ by residuals of order the function itself, whereas $f^+$ satisfies them. The eikonal is quadratic and so blind to conjugation; the constraints are not. *The Complex Potential of a Self-Dual Maxwell Field* records the check. Integrating the spinor system with $h=(f^\pm)^2$ gives the complex potential

$$
A_0 = \pm\frac{1}{2r}, \qquad A_r = -\frac{1}{2r}, \qquad A_\theta = \mp i A_{\mathrm{azm}} = -\frac{1}{2r}\cot\theta \pm \frac{3}{2r\sin\theta},
$$

whose physical (real) part is the Coulomb field: the angular and magnetic components cancel and $E_r$ is the only non-vanishing component, with the charge fixed at $ϙ=\pm1$ in this paper's normalisation. (The later papers of the programme write the elementary value as $\tfrac14$ in their own normalisation, and the 1998 restatement below makes that normalisation self-consistent; the two normalisations are kept apart and are not merged.) The source prints $E_r=\pm1/r$; the printed potential decays as $1/(2r)$, whose negative radial derivative is $\pm1/(2r^2)$, so the printed power of $r$ is one lower than the derivative of the printed potential, while the physical content — the Coulomb $1/r^2$ decay — is unaffected. The mechanism of the quantisation appears in this paper in its plainest form: the generalized Cauchy–Riemann equations are **not** invariant under the scaling $A\to\lambda A$ that the linear Maxwell equations admit, so the admissible potentials come in a fixed discrete set of scales, and the source expects the deeper reason to be topological.

**The dion, and the normalisation of the charge.** The 1998 presentation of the same solution gives the potentials in a form that is self-consistent and fixes the elementary value. In the coordinates of the preceding paragraph the unisingular solution is

$$
A_0 = \pm\frac{1}{4r}, \qquad A_r = -\frac{1}{4r}, \qquad A_{\mathrm{azm}} = \pm i A_\theta = \frac{i}{4r}\tan^{\pm1}\frac{\theta}{2} ,
$$

with $A_r$ and $A_\theta$ of pure-gauge type, and the complex field strengths are

$$
E_r = \pm\frac{1}{4r^2}, \qquad H_r = \pm\frac{i}{4r^2} ,
$$

the electric field being **pure real** and the magnetic field **pure imaginary**. This is the Coulomb field of a charge $ϙ=\pm\tfrac14$, and the potential now differentiates to the strength printed, $-\partial/\partial r(\pm1/(4r))=\pm1/(4r^2)$, exactly. The 1995 presentation's printed pair $A_0=\pm1/(2r)$ with $E_r=\pm1/r$ — the one the paragraph above flags as inconsistent — carries the same solution in a different scale, and the 1998 presentation recorded here removes the printed inconsistency: with $A_0=ϙ/r$ and $ϙ=\pm\tfrac14$ the potential and the strength agree exactly. It is the value $\tfrac14$ that the later papers of the programme carry, and the two normalisations are kept apart rather than merged (a factor two separates the two potentials, so a formula must not be moved between them). The magnetic charge is $m=\pm i/4$: the singular solutions of the self-dual system are **dions**, carrying electric and magnetic charge of equal magnitude, and the source states this as a necessity and not an option — "charged singular solutions, if they exist, should be dions".

**The two sectors, and why the second is invisible.** The complex field splits into a real part and an imaginary part, and the split is the sharpest physical statement in the 1998 paper. The real-part fields carry the Coulomb field, the magnetic dipole moment and the electric quadrupole moment; the imaginary part carries the **electric dipole moment**, and the source calls this term "phantom". Geometrically the imaginary sector contributes only to the torsion of the "Minkowski projection" of the complex connection, and because that torsion is totally skew-symmetric (of Rodichev type) it does not enter the equations of geodesics. The conclusion is that an electric dipole moment built this way would be **unobservable**. It is a strong claim and the corpus does not adopt it; it is recorded because it is the programme's answer to why a self-dual system is not in conflict with observation.

The same mechanism produces other particle-like solutions: an axisymmetric solution generated by $\Pi=\kappa_0\kappa_1+b^2G$ describes two point-like singularities of opposite elementary charge in **uniformly accelerated** (hyperbolic) counter-motion, with the field of the classical Born solution; for imaginary $b=ia$ the singular locus is a neutral ring of radius $a$ that expands into a self-intersecting torus. More complicated generating functions give figure-eight singularities, a helix-like singular locus, the annihilation of a pair of oppositely charged point singularities, and a photon-like singularity in the form of crossed rings moving uniformly at the speed of light. The singular locus of a general solution need not be one-dimensional, and for particle-like solutions it is bounded in the physical three-space.

**The dimension of the singular locus is a property of the caustic, not of the construction.** For this generating function the caustic $d\Pi/dG=0$ reduces to

$$
\bigl(r'_t^2-r_z^2-(r_x^2+r_y^2)+b^2\bigr)^2+4b^2(r_x^2+r_y^2)=0 ,
$$

and its dimension follows from the arithmetic of that equation. For real $b$ it is a sum of two squares, so it vanishes only where both do, at the two points $x=y=0$, $r_z=\pm\sqrt{r'_t^2+b^2}$: dimension zero. For imaginary $b=ia$ it is a difference of squares and vanishes on the two tori written below: dimension two. For complex $b$ it is a complex equation, that is two real equations: the two circles $x^2+y^2=b_1^2$ with $r_z=\pm\sqrt{r'_t^2+b_0^2}$, of dimension one. So the same generating function yields singular loci of dimension zero, two and one, and the dimension is read from the caustic equation rather than fixed by the construction.

**The two sheets of the imaginary case.** For $b=ia$ the caustic factorises exactly,

$$
\bigl(r_z^2+(\sqrt{r_x^2+r_y^2}-\lvert a\rvert)^2-r'_t^2\bigr)\bigl(r_z^2+(\sqrt{r_x^2+r_y^2}+\lvert a\rvert)^2-r'_t^2\bigr)=0 ,
$$

which was verified here symbolically. The source records the first factor: the neutral ring of radius $\lvert a\rvert$ at $r'_t=0$, which expands at the speed of light and turns into a self-intersecting torus at $r'_t=\lvert a\rvert$. The second factor is a second torus, and both are caustics: at $r'_t=2$, $z=0$, $a=1$ the quadratic in $G$ has a double root at $x^2+y^2=9$ and again at $x^2+y^2=1$, checked numerically here. The second sheet meets the axis on $r_z^2=r'_t^2-a^2$, which is exactly where the two strings along the axis begin, so the string-like singularities that the source counts as additional to the electromagnetic one are attached to a second sheet of the same caustic. The electromagnetic field is singular there too, since its components carry inverse powers of the square root of the left-hand side of the caustic equation.

**Why these two quadratic solutions, and no others.** The two members of the quadratic family sit at the two sections of one symmetry. The group of **complex rotations about the third axis** has one complex parameter $\xi=\theta+i\tilde{Ξ}_{\mathrm{sp}}$ and acts on the twistor coordinates by

$$
G\mapsto e^{-i\xi}G,\qquad \upsilon\mapsto e^{\theta_{\mathrm{rpd}}}\upsilon,\qquad v\mapsto e^{-\tilde{Ξ}_{\mathrm{sp}}}v,\qquad w\mapsto e^{i\theta}w,\qquad p\mapsto e^{-i\theta}p ,
$$

with $\theta$ the rotation angle and $\theta_{\mathrm{rpd}}$ the rapidity, which are the real and the imaginary parts of $\xi$, the complex angle of the algebra (*The Exponential Word and Its Boundary*, *The Hamilton Pairing: Mass as Modulus and the Complex Angle*). The combination $\kappa_0\kappa_1/G$ is invariant under the whole group — verified here symbolically, and separately for $\theta$ and for $\theta_{\mathrm{rpd}}$ alone — so the bisingular generator, which is $\kappa_0\kappa_1/G+b^2=0$, is invariant under the complex rotation, while the Kerr generator $G\kappa_0-\kappa_1-2bG$ is invariant under its real part alone and not under the boost. Axial symmetry and boost invariance are therefore one symmetry read at two sections, and the two quadratic solutions are those two sections.

**The ring family.** The ring of the fundamental solution is the first of an explicit one-parameter family. For the static generating functions $\Pi=G^n/H$, with $H=wG^2+2(z+ia)G-\bar w$ and $w=x-iy$, $\bar w=x+iy$ (the $w,p$ of the notation table, $p=\bar w$; here $z$ is the third Cartesian coordinate, the table's $z_3$), the class-II singular locus is obtained by eliminating $G$ from $P=0$ together with the class-II branching condition

$$
\Lambda:=\frac{d^2\Pi}{dG^2}=0 .
$$

For this $\Pi$ the pair reduces to $f:=nH-G\,dH/dG=0$ and $df/dG=(n-1)\,dH/dG-G\,d^2H/dG^2=0$, and eliminating $G$ between them gives

$$
(n-1)^2(z+ia)^2+n(n-2)(x^2+y^2)=0 .
$$

The imaginary part forces $z=0$ and the real part gives $x^2+y^2=R_n^2$ with

$$
R_n=\frac{a(n-1)}{\sqrt{n(n-2)}},\qquad n\ge3 .
$$

So the family is a sequence of rings, $R_3=2a/\sqrt3$ decreasing to $R_\infty=a$. The elimination and the radius were recomputed symbolically here for $3\le n\le7$ and hold. The two lowest cases are exceptional. For $n=1$ the solution has a pole on the ring $z=0$, $x^2+y^2=a^2$ but branches only at the origin, so it is a point singularity. For $n=2$ one gets $\Pi=\bar w/r_*^2$ with $r_*^2=x^2+y^2+(z+ia)^2$, which has no branching point on the real slice at all; for $a=-1$ it reads

$$
\Pi=\frac{i\,(x+iy)}{2z+i\,(r^2-1)},\qquad r^2=r_x^2+r_y^2+r_z^2 ,
$$

which was checked here to be the standard **Hopf map**. The Hopf fibration therefore enters the programme as the second member of this family of eikonal solutions, not as an inserted topological construction; its bundle-theoretic interpretation belongs to *The Hopf Fibration and the Biquaternion Gauge Bundle*.

**The complex-shifted ring, its moments, and the programme's one numerical prediction.** The ring is not found by solving a new system: it is the point solution translated in the complex direction, $z\mapsto z+ia$, which is a symmetry of the UEqs. Applied to the Coulomb potential this gives the **Appel solution**

$$
A_0 = \frac{ϙ}{r_*}, \qquad r_*^2 = x^2+y^2+(z+ia)^2 ,
$$

the same $r_*$ that governs the $n=2$ member of the ring family. Writing $z=r\cos\theta$ and expanding in $a/r$, the real part of the potential is

$$
\Re A_0 = \frac{ϙ}{r}\left(1 - \frac{a^2}{2r^2}\bigl(3\cos^2\theta-1\bigr)\right) + O(a^4) ,
$$

which was recomputed here symbolically to this order; it is exactly the potential of a point charge $ϙ$ carrying an axisymmetric **electric quadrupole**. The source's asymptotic field components, in the present article's notation for the field radius $r$, are

$$
E_r \simeq \frac{ϙ}{r^2}\left(1 - \frac{3a^2}{2r^2}(3\cos^2\theta-1)\right), \qquad
E_\theta \simeq -\frac{3qa^2}{r^4}\cos\theta\sin\theta , \qquad
H_r \simeq \frac{2qa}{r^3}\cos\theta , \qquad
H_\theta \simeq \frac{qa}{r^3}\sin\theta .
$$

The two electric expressions and the quadrupole coefficient were checked here and hold; the magnetic pair is exactly the dipole field of a moment $\mu=qa$ ($H_r=2\mu\cos\theta/r^3$, $H_\theta=\mu\sin\theta/r^3$). Reading the multipole moments off the potential, $Ξ=ϙ/r+\vartheta(3\cos^2\theta-1)/(4r^3)$, gives

$$
\mu = qa, \qquad \vartheta = -2qa^2 .
$$

The last step is the programme's only numerical prediction, and it is a single algebraic identity. Because $\vartheta=-2qa^2$, fixing the ring radius by the Dirac moment, $|a|=\frac{\hbar}{2\,c\,M}$ and $\mu=qa=\frac{\hbar\,e}{2\,c\,M}$, forces the quadrupole to

$$
\boxed{\;\vartheta = -\frac{\hbar^{2}\,q}{2\,c^{2}\,M^{2}} = -\frac{\hbar^{2}\,q}{2\,c^{2}\,M^{2}}\;}.
$$

The sign is carried over from $\vartheta=-2qa^2$ and is negative for $q=+e$; the source states the result as a quadrupole *equal in magnitude* to $\frac{\hbar^{2}\,e}{2\,c^{2}\,M^{2}}$, and the magnitude is the whole of the comparison, since $\vartheta$ is measured against a sign convention fixed by $Ξ=q/r+\vartheta(3\cos^2\theta-1)/(4r^3)$. The source states this as a conjecture and explicitly calls it speculative, while noting that the possibility of an experimental test could be discussed; the corpus records it in that status. It is placed here because it is the one place in the programme where a free parameter is used up by a known quantity and what remains is a number rather than a structure.

**A worked multiparticle example.** The source's test case for the dynamics uses the fourth-order generating function

$$
\Pi=G^2\kappa_0^2+\kappa_1^2-b^2G^2=0,\qquad b=\mathrm{const}\in\mathbb{R},
$$

whose four modes make the caustic structure explicit. At $r'_t=0$ the singular locus is a pair of point singularities of opposite and equal elementary charge together with a neutral two-surface that encloses them — the intersection of all four branches, which the source calls a cocoon — while each point charge is formed by the intersection of a particular pair of the locally radial, Coulomb-like congruences. At $r'_t=b/\sqrt2$ the two point singularities meet at the origin and cancel, modelling annihilation, and the event is accompanied by the emission of a singular light-like wavefront, a further two-dimensional component of the caustic set. This is the programme's clearest demonstration that the caustics can be bounded, singly charged and able to merge and disappear. The source states the example as an analytic computation; it is recorded here as the source's, not recomputed in this pass.

**The catastrophe-theory interpretation.** The source frames this part of the picture in the language of **catastrophe theory**: what evolves is the caustic set, and a *perestroika* of that set — a change of its topological type, such as the cocoon's collapse to a pair of points and their cancellation — is read as a **mutual transmutation of particles**. The bisingular solution, in which two oppositely charged point singularities interact axisymmetrically with the elementary charge of the unisingular solution, is presented as the evidence that the framework admits such processes; the general interaction problem, together with the intermediate toroidal resonance, is announced as future work. This is the furthest the programme is from anything the corpus can compare with: the corpus has no dynamics of particle transmutation, and the interpretation is recorded as the programme's programme, not as a result.

**The quadratic family, the figure-eight, and the wave-like helix.** The particle-like solutions have closed forms, and the source proves one exhaustiveness statement about them: for generating functions **quadratic** in $G$ the axisymmetric solutions are, up to Poincaré transformations, the static Kerr-like solution of the preceding section and the nonstationary bisingular solution generated by $\Pi=\kappa_0\kappa_1+b^2G$, together with its toroidal or double-ring modifications. The **figure-"8"** is the remaining quadratic member, generated by $\Pi=\kappa_0\kappa_1-a^2G^2$: eliminating $G$ from $\Pi=0$ and the caustic condition $P=0$ gives a singular set whose $r'_t=0$ section is a flat figure-eight curve, and its field is **neutral** (total charge zero) and **null**, $\vec N\cdot\vec N=0$, falling as $r^{-4}$ away from the singularity. It is the programme's most explicit "particle" that is not a ring.

The wave-like solutions give the most concrete object in the material. When the generating function depends on a single twistor argument, $F(G,\kappa_0)=0$, the initial distribution $G(\upsilon)$ is free on the axis, and the monochromatic choice

$$
G-A\exp\!\left[i\varpi\,\kappa_0\right]=0
$$

is solved in closed form by the **Lambert function**,

$$
G=\frac{i\,W\!\left(-iA\varpi\,w\,\exp(i\varpi \upsilon)\right)}{\varpi w},
$$

with $W$ the principal branch of $W(z)\exp(W(z))=z$. (The source's frequency $\Omega$ is written $\varpi$ here, because $\Omega$ denotes the connection in this article; the source also writes the twistor argument as $\bar wG+\upsilon$, its $\bar w$ being this article's $w$, part of the convention clash flagged once above.) The singular set of this solution is a **neutral helix of radius $1/(\varpi A e)$ and lead $2\pi/\varpi$**, propagating along the $z$-axis at the speed of light, with mutually orthogonal transverse fields that fall as $1/r$ from the axis and are defined only up to an overall sign. The radius and the lead follow from the caustic condition in one line. On the solution the defining equation gives $A\exp[i\varpi\kappa_0]=G$, so

$$
\frac{dF}{dG}=1-i\varpi w\,G=1+W ,
$$

and $P=0$ therefore forces $W=-1$, whence $|w|=1/(eA\varpi)$. A helix of definite radius and pitch in closed form is the sharpest answer the material gives to the question of what a biquaternionic "particle" looks like, and it is recorded here as a solution of the programme's primary system, not as a physical electron model.

The source is careful about what this does and does not mean, and the corpus should be too. The quantization is **not postulated but derived**, which is the programme's strongest claim and the one that addresses the corpus's stated open boundary; but the derivation fixes the charge **given the singularity structure**, and it is the *over-determined primary system plus self-duality* that does the work, not a new dynamics. In the version of the theory invariant under the duality transformations it is the *effective magneto-electric* charge that is quantized, and the programme states that in that accounting the charge problem also receives a natural solution. The elementary charge is identified with the minimal admissible value $|ϙ|=\tfrac14$ of the fundamental static solution, which is weaker than deriving the numerical value of the electron's charge from nothing, and the corpus must not read the phrase "self-quantized" as more than that.

Three further consequences are recorded because they mark the programme as genuinely non-standard. The primary system is **not Lagrangian** and its solutions are subject to **selection rules** — constraints on admissible charge, spin and other characteristics — that do not follow from the linear field equations. The **superposition principle breaks**: a sum of GSE solutions satisfies the linear Maxwell equations but not the primary GSE. And the over-determined primary system is **not invariant under spatial reflection** nor, perhaps, under time reversal; these symmetries are restored only at the level of the integrability conditions, that is, at the level of Maxwell and Yang–Mills. The source presents this as an ability to describe parity violation and time irreversibility in principle.

**Contrast with the corpus.** The corpus's quantisation discussion ends by saying that the biquaternion framework is "silent where the standard theory is silent" — it re-expresses the Dirac condition $eg=2\,\pi\,\hbar\,c\,n$ but does not derive the existence of the quantum of charge. The algebrodynamical programme claims exactly that missing derivation, for a nonlinear equation that this corpus does not use. The honest interpretation is therefore: the corpus's silence is a property of the **linear** framework it writes, and the programme's claim is a claim about a **different, nonlinear** primary equation. It is the clearest example in the material of a programme that addresses the charge-quantisation boundary, and it should be recorded as such — and as the programme's claim, not as a result of this corpus.

**The theorem, and the scale that fixes the quantum.** The charge theorem is general: it does not depend on the generating system, on the twistor, or on the Kerr equation, but only on self-duality, gauge invariance and single-valuedness. It is the most explicit argument in the corpus for a value of the elementary charge derived from a field equation rather than fitted, so it is recorded in full here, followed by the separate and exact statement that places the fundamental solution at the minimum of its own family.

### The theorem

Let the complex potential $C_\mu$ be analytic except on a set of one-dimensional "Dirac strings", let the complex field be self-dual, and let the field $\tilde{Ξ}_{\mathrm{sp}}$ that the potential couples to be single-valued everywhere outside the singularities of the field strengths. Then the electric charge of any bounded singular source — a **singular particle-like** solution, in the source's phrase — is either zero or an integer multiple of $ϙ_{\min}=1/(2b)$, where $b$ is the coupling constant of the gauge invariance $\tilde{Ξ}_{\mathrm{sp}}\mapsto e^{\alpha}\tilde{Ξ}_{\mathrm{sp}}$, $C_\mu\mapsto C_\mu+b^{-1}\,\partial\alpha/\partial x_\mu$ of the theory in which the potential appears through the lengthened derivative $(\partial/\partial x_\mu-bC_\mu)\tilde{Ξ}_{\mathrm{sp}}$.

### The proof

Two steps, and neither uses the details of the primary system; the argument needs only self-duality, gauge invariance and single-valuedness.

**The two charges become one.** Integrate the self-duality condition $\vec N=0$ over a closed surface $\Sigma$ enclosing one or more bounded singularities and apply Gauss's theorem to each:

$$
4\piϙ=\oint_\Sigma\vec E\cdot d\vec\sigma=-i\oint_\Sigma\vec H\cdot d\vec\sigma\equiv -4\pi i m ,
$$

so that $ϙ=-im$ and $|ϙ|=|m|$: every bounded source is a **dion**, with electric and magnetic charge equal in modulus. This is the step recorded above for the static solution; here it is general, and it holds for any bounded source because it uses only the field equation and the boundedness that makes the surface integral pick out the enclosed charge.

**Dirac's string argument, in complex form.** Since $m\ne0$ the field is not solenoidal and the potential cannot be regular everywhere: it must be singular on one-dimensional strings. Cut the infinitesimal disks $\{D\}$ that the strings pierce out of $\Sigma$ and apply Stokes's theorem to the remainder $\Sigma'$. The fluxes are unchanged, because the field strengths themselves are regular on $\Sigma$ including the disks, so the flows through the disks are infinitesimal. What remains is a sum of line integrals over small loops $L$ encircling the strings,

$$
4\pi m=\oint_\Sigma\vec H\cdot d\vec\sigma=\sum_L\oint_L C\cdot d\ell .
$$

Only the singular part of $C$ contributes, and that part must be pure gauge, $C_{\text{sing}}=\nabla\Lambda$: otherwise $\vec H$ itself would be singular on $L$, contrary to the hypothesis. Each loop integral is therefore the increment $\Delta\Lambda$ of a multivalued complex function. Gauge invariance and single-valuedness of $\tilde{Ξ}_{\mathrm{sp}}$ then give

$$
\Delta\Lambda=b^{-1}\ln\Delta\tilde{Ξ}_{\mathrm{sp}}=b^{-1}\,2\pi i n,\qquad n\in\mathbb Z ,
$$

so the flux is $4\pi m=2\pi i N/b$ with $N=\sum_L n$, and

$$
ϙ=-im=\frac{N}{2b}.
$$

**The coupling constant, and the value $\tfrac14$.** The programme's gauge symmetry is the **weak**, or restricted, one: $\zeta\mapsto\alpha\zeta$, $\tau\mapsto\alpha\tau$ on the twistor and $C_\mu\mapsto C_\mu+2\,\partial\ln\alpha/\partial x_\mu$ on the potential, with the parameter allowed to depend on the coordinates only through the spinor and twistor components. The source states that a comparison of the two forms gives $b=2$, and with the theorem's $ϙ=N/(2b)$ that is $ϙ=N/4$. The comparison, however, needs the parameter to be identified, and it is not unique: if the field $\tilde{Ξ}_{\mathrm{sp}}$ of the general form is taken to be the spinor $\zeta$, the parameters are related by $\alpha_{(13)}=\ln\alpha_{(43)}$ and the matching of the potential terms gives $b^{-1}=2$, that is $b=\tfrac12$ and $ϙ_{\min}=1$; a field transforming with weight $k$, $\tilde{Ξ}_{\mathrm{sp}}\mapsto\alpha^{k}\tilde{Ξ}_{\mathrm{sp}}$, gives $b=k/2$, so the source's $b=2$ corresponds to weight four.

What is derived is therefore the **lattice** — the charge is an integer multiple of a minimal value $1/(2b)$ fixed by the coupling, and the minimal value is attained rather than only approached — while the number $\tfrac14$ is the normalisation of the source's later papers. The two normalisations are consistent with the theorem and not with each other's arithmetic: $b=\tfrac12$ gives $ϙ_{\min}=1$, which is the 1995 value $A_0=\pm1/(2r)$ with $ϙ=\pm1$, and $b=2$ gives $ϙ_{\min}=\tfrac14$, which is the 1998 value $A_0=\pm1/(4r)$. The corpus keeps the two apart, as it already does for the potentials themselves, and records $\tfrac14$ as the programme's own unit rather than as a number the theorem produces. The restricted character of the symmetry does not weaken the argument: the proof uses gauge invariance and single-valuedness only, and both are available, so the derivation of integrality stands whatever the coupling is called.

**The comparison with Dirac.** Dirac's condition is the special case in which $b$ is $\frac{i\,e}{\hbar\,c}$, for which $|ϙ|=\frac{\hbar\,c\,N}{(2|e|)}$ reproduces $|m||e|=(\frac{\hbar\,c}{2})N$; the magnitude is what the theorem fixes, and the sign difference belongs to the convention for the sign of the spatial potential, discussed in the Introduction of *The Complex Potential of a Self-Dual Maxwell Field*. The two statements differ in what they fix. Dirac's relates the electric charge of one object to the magnetic charge of another, and the $e$ in it is a coupling constant which has nothing to do with the charge of any particular solution; the programme's fixes the charge of the solution itself, given the coupling. The programme can then choose units in which $ϙ_{\min}$ is the electron charge; the value $\tfrac14$ is a statement about its units and not a prediction.

### Why the fundamental solution sits exactly at the quantum

That the minimal value is $\tfrac14$ rather than a multiple of it is a separate fact, worth separating from the theorem because it is where the nonlinearity does the work. The source states it and checks it directly on the Coulomb Ansatz; the reason is a mismatch of degree, and the check below makes it exact.

Write the static superpotential with a free scale, $G_{\mathrm{ϙ}}=\mathrm{ϙ}\,\bar w/(z+r)$, so that $\mathrm{ϙ}=4ϙ$. Three conditions are in play: the wave equation, the eikonal, and the two first-order constraints

$$
\frac{\partial G}{\partial w}=G\,\frac{\partial G}{\partial\upsilon},\qquad \frac{\partial G}{\partial v}=G\,\frac{\partial G}{\partial\bar w}
$$

that make $G$ come from a twistor through the Kerr equation. The first two are scale invariant — the wave equation is linear, the eikonal quadratic in the derivatives — so every $\mathrm{ϙ}$ passes them, and the Coulomb-like field exists for every charge. The constraints are not: they are linear in $G$ on the left and quadratic on the right. For the family above the derivatives are

$$
\frac{\partial G_{\mathrm{ϙ}}}{\partial w}=-\frac{\mathrm{ϙ}\bar w^2}{2r(r_z+r)^2},
\qquad
G_{\mathrm{ϙ}}\,\frac{\partial G_{\mathrm{ϙ}}}{\partial\upsilon}=-\frac{\mathrm{ϙ}^2\bar w^2}{2r(r_z+r)^2},
\qquad
\frac{\partial G_{\mathrm{ϙ}}}{\partial v}=\frac{\mathrm{ϙ}\bar w}{2r(r_z+r)},
\qquad
G_{\mathrm{ϙ}}\,\frac{\partial G_{\mathrm{ϙ}}}{\partial\bar w}=\frac{\mathrm{ϙ}^2\bar w}{2r(r_z+r)},
$$

so each constraint reads $\mathrm{ϙ}=\mathrm{ϙ}^2$ and the only nonzero solution is $\mathrm{ϙ}=1$, that is $|ϙ|=\tfrac14$; the four derivatives were recomputed here. **The elementary charge is the unique scale at which the two sides of a first-order constraint have the same degree.** At $\mathrm{ϙ}=1$ the superpotential is $\bar w/(z\pm r)$, the two signs being the two poles of the stereographic projection; the programme's static generating function reduces to it.

This is the sharp form of the statement made above, in the 1995 presentation, that the generalized Cauchy–Riemann conditions are not invariant under the scaling $A\to\lambda A$ that the linear Maxwell equations admit. It also localises the quantisation: the eikonal and the wave equation, which the programme treats as its primary content, are precisely the scale-invariant parts, and the charge is fixed by the part that is not.

### Plane waves, the monopole, and a printed factor

**No free radiation.** The constraints exclude plane waves, a consequence derived here and not a remark of the source. On $G=\exp i(\vec k_\Phi\cdot\vec r-\omega h_t)$ with $\omega^2=\vec k_\Phi\cdot\vec k_\Phi$, the first constraint reads $\tfrac{i}{2}(k_x+ik_y)G=\tfrac{i}{2}(k_z-\omega)G^2$ and forces $G$ to the constant ratio $(k_x+ik_y)/(k_z-\omega)$; apart from the degenerate case $k_z=\omega$ with $k_x=k_y=0$, where the first constraint is empty and the second forces $G=0$, no propagating plane wave is admissible. The quantised fields are therefore not a deformation of the linear radiation field, and the contrast with the corpus's free Maxwell fields is a contrast of solution classes and not of approximation.

**The monopole conjecture.** If only one species of singular source exists, with $ϙ=-im$, a duality rotation of the electric and magnetic fields turns it into a purely electric one, since the rotation multiplies the complex field by a phase and preserves self-duality; the source therefore **conjectures** that in a theory of this type magnetic monopoles do not manifest themselves at all, the dion being one charge seen from a rotated frame. The conjecture is recorded as a conjecture: it is an interpretation of the theorem and not a consequence of it, and the corpus's article on the other magnetic-charge programme, *The Electro-Gravimagnetic Field and the Magnetic-Charge–Mass Hypothesis*, records a different identification and is not evidence either way.

**A printed factor.** The Coulomb superpotential of the source's equation (29) is $G=4ϙ\bar w/(z+r)$ with $C_{\bar w}=-2ϙ\bar w/(z+r)$ and $C_v=2ϙ/r$. Differentiating the printed $G$ gives $C_{\bar w}=-2ϙ\bar w/\bigl(r(z+r)\bigr)$, so the printed component is missing a factor $1/r$. With the factor restored the Weyl system holds to $3\times10^{-11}$ at a generic point and the field strength is $\vec E=-i\vec H=ϙ\vec r/r^3$; with the printed component the two Weyl equations fail there by $4\times10^{-3}$ and $1.1\times10^{-1}$, where the field strengths are of order $0.35$. The charge, the field strength and the rigidity above are unaffected, since they come from $C_v$ and from the correct derivative; the error is confined to that one displayed intermediate quantity, and it is noted here because the same component is the starting point of the superpotential construction.

## Multivalued Fields and the World Function

To describe the Universe as a whole the programme must choose a representative solution, and it chooses a class-I solution generated by the Kerr constraint, because that is the class carrying the geometric and gauge structures. The choice pulls the class-II conjugate back into the scheme. Taking $G$ from $d\Pi/dG=0$ and substituting it into $\Pi=0$ makes the function $\Pi(G(X))$ vanish on the singular locus of the class-I field — that is, on its characteristic hypersurface — and, being a class-II solution, it satisfies the eikonal. The eikonal field therefore plays two roles at once: it is the fundamental physical field as a class-I solution, and the characteristic field as a class-II solution, describing the locus at which the derivatives of the fundamental field are discontinuous. This double role is why the source calls $\Pi$ the **world function**.

The second structural point is that the principal field $G$ is not single-valued. If $\Pi$ is irreducible, its defining algebraic equation has in general more than one root, and the generic solution is a multivalued complex function; a locally chosen continuous branch is a **mode**, and each mode carries its own null congruence and its own set of associated fields. For a world function that is an algebraic surface in projective twistor space the number of modes is finite, and a finite number of locally distinct null congruences then exists at each point of space-time. The programme insists that this multivaluedness is not a defect. It argues that in a theory where the fields *constitute* the particles rather than merely describing them, fields need not be univalued; that univaluedness is the exception rather than the rule for solutions of partial differential equations, the familiar $\delta$-type distributions being the more artificial object; and that imposing univaluedness of a *locally chosen mode* of $G$ and of the electromagnetic field, away from the branch points, is precisely what yields the quantisation of the charge of the singularities. That is a second, more topological route to the $ϙ=N/4$ of the preceding section, distinct from the self-duality argument, and the source attributes it to its own later papers. The resulting picture is what the source calls a dualistic *corpuscular–field complex*, in which all the particles of the Universe belong to a single object.

Recording this is worth doing because it marks an assumption the corpus has never had to state: the corpus's own articles use single-valued fields on $\mathbb{B}$, the one multivalued object in its repertoire being the biquaternionic logarithm. A neighbouring programme *requires* multivaluedness for its particle picture to hold together, and turns the requirement into the source of a discrete spectrum rather than an embarrassment. The corpus takes no position on the claim; the multivaluedness, the univaluedness argument for quantisation and the corpuscular–field interpretation are the source's, and are recorded here because they are what makes the programme's particle picture self-consistent, not because the corpus adopts them.

## The Induced Causal Minkowski Geometry with Phase

The last structural claim is geometric, and it is the one that connects most directly to *Why Complexify Spacetime?*. The complexified Minkowski space $\mathbb{C}M$ arises in the programme as the full vector space of the biquaternion algebra, and the restriction of coordinates to the real slice $M$ is, in the source's words, artificial: the real slice is not a subalgebra and is invariant neither under the algebra automorphisms nor under the full symmetry group. The natural group is the automorphism group $SO(3,\mathbb{C})$, of six real parameters, which is the proper orthochronous Lorentz group $SO_0(3,1)$ read in complex form: conjugation by $SL(2,\mathbb{C})$ acts on the traceless part faithfully modulo $\{\pm I\}$, so $SO(3,\mathbb{C})\cong PSL(2,\mathbb{C})\cong SO_0(3,1)$. The double cover is $SL(2,\mathbb{C})\to SO_0(3,1)$, one storey up, and the isomorphism here is not a covering.

The Minkowski geometry is then **induced**, not postulated. The principal invariant of the complex three-space is

$$
\sigma = (z_1)^2 + (z_2)^2 + (z_3)^2 ,
$$

and it splits into a modulus-like part and a phase-like part. The modulus part is the real non-negative invariant $S^2 = \sigma\sigma^{*}$. The claim is that this invariant can be written identically as a Minkowski-like interval,

$$
\boxed{\;
S^2 = \sigma\sigma^{*} \equiv T^2 - \lvert\vec X\rvert^2 ,
\qquad
T := \vec z\cdot\vec z^{*},
\qquad
\vec X := i\,[\vec z\times\vec z^{*}]\;},
$$

where the brackets are the scalar and vector products of complex three-vectors. The quantities $T$ and $\vec X$ are real, and under the $SO(3,\mathbb{C})$ automorphisms they transform as the time and space coordinates of Minkowski space under Lorentz transformations. The identity is an instance of the Lagrange identity relating the modulus of the complex quadratic form to the dot and cross products; it is recomputation-verified on random complex vectors in this pass, together with the reality of $\vec X$. What it gives is exactly what *Why Complexify Spacetime?* describes as a motivation and not a derivation: an algebraic origin for the Lorentzian signature, here written as an identity between the complex invariant $\sigma\sigma^{*}$ and a Minkowski interval built from the same vector.

One consequence of the identity should be stated with the identity, because it is a physical claim and not a formality. The left side is a modulus, so the interval is **non-negative identically**: $T^2-\lvert\vec X\rvert^2=\lvert\sigma\rvert^2\ge0$ for every point of the complex three-space, spacelike separation never occurs, and the induced arena is the closed interior of the light cone and nothing else. The source's reading is that events which are not causally connected "as if do not exist at all". That is a substantive difference from the corpus's own interval, which is indefinite on the real slice and admits both signs; and it is the geometric counterpart of the positive definiteness of $T$, which the section below connects with the irreversibility of physical time.

The programme goes further than the signature. Because $\sigma$ also has a **phase**, the modulus identity leaves a phase invariant of the same Lorentz-transformation group, an internal fibre-like variable over the physical macro-geometry. The source suggests, without claiming to have shown it, that this phase is related to universal quantum properties of matter and to interference. The construction is the same induced-geometry mechanism the corpus cites in *Curved Spacetime and the Biquaternion Framework* and, in that article's language, it is the most complete statement of the mechanism.

Writing the complex three-vector as $\vec z=\vec p+i\vec q$ with **real** three-vectors $\vec p$ and $\vec q$ (the source's $p,q$; the arrows distinguish them from the scalar twistor coordinate $p$ of the notation table), the source separates the primary complex space linearly into a pair of real vectors — a splitting it calls "demonstrative" but explicitly not the fundamental one, since the geometry it uses is the modulus-and-phase one. In this splitting $\sigma=S \exp(i\alpha)$, and the invariants above acquire the elementary forms

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
\cos^2\theta = \frac{1-V^2}{1+V^2\cot^2\alpha} .
$$

At the fundamental velocity $V=1$ it forces $\theta=\pi/2$, so $\vec p$ and $\vec q$ are orthogonal to each other and to the direction of motion, as for an electromagnetic wave, while $\sigma$ vanishes and the phase $\alpha$ becomes indefinite; for a point at rest $V=0$ it gives $\theta=0$ or $\pi$, two admissible relative orientations that the source compares with the two projections of a spin vector onto a fixed direction. The relation is the one derived in the 2006 paper *On a Quaternionic Induced Geometry with Phase* (arXiv:gr-qc/0602088, Eq. (18)); the 2009 survey prints $\coth^2$, a typo. It was verified here from the definitions and the Lagrange identity, and the derivation is given in *The Lorentz Group as Biquaternion Norm Automorphisms*.

On this background the programme develops a picture of particles and time that is speculative and is recorded as such. Any GSE solution corresponds to a shear-free null congruence of rays, which the source calls the **Prelight flow**, the primordial flow of light; matter, represented by the particle-like singularities, appears as the set of caustics or focal lines of that flow. The time coordinate on the real slice is the parameter along the rays, so the defining property of time in the programme is the preservation of the primordial twistor field along the congruence — "time as an automorphism of the primary field" — while the variability of matter defines a second function of time. In the complex space, Newman's representation of the shear-free congruences by a complexified Liénard–Wiechert field makes the complex null cone equation have many roots, so a particle is correlated with its own other positions along its world line; the source calls the resulting ensemble of identical yet differently located particles the ensemble of **duplicons**, and suggests that its stochasticity, once complex time is allowed to vary, is related to quantum uncertainty in Feynman's formulation. This is programmatic. The corpus neither adopts the vocabulary nor endorses the interpretation; it records that the programme states these as hopes and not as results.

## The Light-Formed Aether and the Flow of Time

The paper's last layer is its account of time, and it is the most speculative. The rays of the congruence densely fill space, and at each point they consist of a superposition of branches, all propagating in different directions at the same universal speed in every branch and every frame. The programme's interpretation is that there is nothing in the Universe but this primordial light flow, and that ordinary matter is born at its caustic regions of condensation. On that picture the Flow of Time is identified with the Flow of Prelight: the "River of Time" becomes the "River of Light", and the subjective uniformity and homogeneity of time is read as a reflection of the universality of the speed of light. The aether that the picture reintroduces is Lorentz invariant and structureless, explicitly not the old elastic light-carrying medium, so the source presents it as consonant with special relativity rather than opposed to it.

Because the underlying field is multivalued, each point carries a set of locally distinct subflows, and the time flow is therefore multi-directional; the source suggests that the local direction is unobservable precisely because of this multiplicity, and that a stochastic component in the world solution would hide it further. The programme's time is non-material. Unlike Kozyrev's "active time", which the source explicitly sets aside for want of any known mechanism of interaction with matter, this time does not interact with matter but forms it, and the source summarises the scheme as a single entity, "preLight–Time–Matter". These are programme statements, not results; the paper offers them as a picture to be developed. The corpus records them beside its own time material in *The Quantum-Classical Divide in the Biquaternion Framework*, and adopts neither the vocabulary nor the interpretation.

## The Ensemble of Duplicons

The programme's particle picture rests on one construction that the twistor article defers to this one, and it is one of the few parts of the paper's closing sections that can be checked exactly. A particle is a singularity of the field, and the curve that carries it is a **complex** world line $z_\mu(\tau)$ with $\tau\in\mathbb{C}$, of which the real trajectory is a shadow. (The parameter $\tau$ of this section is the world-line parameter, not the twistor component $\tau_A=Z_{AB}\tilde{Ξ}_{\mathrm{sp},B}$ of *The Twistor Solution of the Complex Eikonal*.) The source shows that the twistor field — and with it the principal spinor and the biquaternionic field — takes equal values at two points of that curve when the two are connected by a complex null line, the equality holding along that line. Every other point of the curve that lies on the complex null cone of a given one therefore carries the same field, and that is what makes it a copy. The copies are the **duplicons**, and the condition that selects them is the null-cone equation

$$
[z_1(\lambda)-z_1(\tau)]^2+[z_2(\lambda)-z_2(\tau)]^2+[z_3(\lambda)-z_3(\tau)]^2-[z_0(\lambda)-z_0(\tau)]^2=0 ,
$$

with $\tau$ the parameter of the "elementary observer" and $\lambda$ the parameter of the second position (the source's $\lambda$, not the de Broglie wavelength of *The Dimerous Electron and Quantum Interference* below). Each root of this equation is a partner of the observer, and the set of roots is the ensemble. The source reads the ensemble first in the Feynman–Wheeler spirit, in which "all of the electrons" are essentially one and the same electron at various locations on a unique world line, and then prefers the pair reading of the next section. In either reading no signal passes: the two are connected by a complex null line and by no real one, so the observer cannot see the duplicons.

**The count is a matter of degree.** Every difference $z_i(\lambda)-z_i(\tau)$ vanishes at $\lambda=\tau$, so $(\lambda-\tau)^2$ always divides the left side: the observer is always a root, and the root at $\lambda=\tau$ is the trivial solution the source finds on real Minkowski space. The order is exactly two when the tangent at $\tau$ is not complex-null, since the coefficient of $(\lambda-\tau)^2$ is $\sum_{i=1}^{3}\dot z_i(\tau)^2-\dot z_0(\tau)^2$. A complex-null tangent raises the order — the line $z_1=\lambda+\lambda^2$, $z_2=i\lambda+2\lambda^2$, $z_0=z_3=0$ has order three at $\tau=0$, checked symbolically — and a straight complex null line makes the left side vanish identically, so that every point of the line is in the ensemble. For a world line whose four components are polynomials of degree at most $d$, the left side has degree at most $2d$, and exactly $2d$ when the vector of degree-$d$ coefficients is not complex-null; the quotient by $(\lambda-\tau)^2$ then has degree $2d-2$, so a generic polynomial world line carries $2d-2$ partners besides the observer, counted with multiplicity and distinct for generic coefficients. The count is not a topological invariant: when the leading vector is complex-null, $\sum_{i=1}^{3}a_i^2=a_0^2$, the top term of the left side cancels, the degree falls by one, and the partners number $2d-3$ — unless the coefficient of the next power cancels as well: for $z_1=\lambda^3$, $z_2=i\lambda^3$, $z_3=\lambda^2$, $z_0=0$ the left side is exactly $\lambda^4$, the quotient is $\lambda^2$, and both surviving roots sit on the observer itself. The three degrees were checked exactly in this pass with symbolic coefficients — four for a generic cubic line, three under the null-leading condition, two in that last example — and the division by $(\lambda-\tau)^2$ leaves no remainder in any of them. Numerically, on random complex cubics, all four roots satisfy the equation to $10^{-12}$. The source's remark that the equation has "in general, a great (or even infinite) number of roots" is not in conflict with this: it covers the two cases outside the degree count, lines that are not polynomial and lines that lie in their own null cone.

**On the real slice the ensemble is empty.** Restricted to real Minkowski coordinates the equation is the retardation condition, and a strictly timelike world line never meets its own light cone. For a strictly timelike graph, $\lvert d\vec z/d\tau\rvert<1$ with $\tau$ real, the mean value *inequality* for the vector $\vec z$ — the componentwise theorem does not combine, since three components can each reach their own maximum at a different point — gives $\lvert\Delta\vec z\rvert<\lvert\Delta\tau\rvert$ for every $\lambda\neq\tau$. The left side is then strictly negative and $\lambda=\tau$ is the only root; the sign was checked numerically on helices of speed $0.9$, $0.999$ and $0.999999$, and at speed exactly $1$ it reaches zero, as it must. The source reaches the same conclusion from the retardation equation alone — the concept of duplicons "cannot be realized on the background of ordinary Minkowski space" — but the reason is the mean value inequality, and it is worth stating: the ensemble exists exactly to the extent that the world line leaves the real slice.

**What the construction gives.** For a polynomial line that is not itself null the ensemble is finite, and its size is bounded by the degree; the source claims only that the roots are many, and the bound is what makes the picture checkable. The dimerous electron of the next section is then a **pair of members of this ensemble** — two roots of the same equation, taken for the same observer — so "all electrons are one electron" becomes a statement about a single curve rather than a metaphor, and the invisibility of the pair is the complexness of its roots: they stand in no real light-cone relation to the observer, hence emit no signal. What the construction does not supply is the dynamics of those roots — the source keeps the primary dynamics in the same GSE as before and treats the ensemble as a consequence of the null-cone geometry, not as new equations of motion.

## The Dimerous Electron and Quantum Interference

The interpretation of the electron is the sharpest of the programme's particle claims, and the source states it as a conjecture. The duplicons of the preceding section are the programme's pre-elements of matter, and the source proposes that an elementary object — an electron — is not one of them but a **pair**, the **dimerous electron**. The pair is invisible most of the time: its two members are separated in complex space, do not radiate, and can be detected by no observer. Only when their positions coincide does an act of interaction occur — a caustic, a null complex line of the generating congruence, carrying a signal towards the observer — and at that instant the pair is registered as a single particle. The source conjectures that the two pre-elements correlate with the observed fractional charges, and that this fusion picture replaces the wave-particle dualism instead of standing beside it. It also notes that the concept cannot be realised on the real Minkowski background, for the reason given in the preceding section.

The interference argument is geometric. Let a pair of duplicons diverge and pass through different "slits" of an idealised interference experiment, then fuse again. Between the two fusions each member acquires a phase lag, namely the phase $\alpha$ of the principal complex invariant "attached" at each point of the generating world line and altering along it. Equality of the two complex coordinates at the fusion forces $\Delta\alpha=2\pi N$, $N\in\mathbb{Z}$: a discrete set of re-fusion points, which the source reads as the analogue of the preparation of a state and its later measurement. Only the modulus $S$ of the complex time is the ordinary Minkowski proper time; its phase $\alpha$ is the source's candidate for the phase of the wave function, and the picture contains no physical de Broglie wave.

The argument is made quantitative by one further assumption, that the physically infinitesimal increments of modulus and phase are proportional, $d\alpha=\mathrm{Const}\cdot dS$. Choosing the scale factor as the inverse of half the electron Compton length, $\mathrm{Const}=(\lambda_0/2)^{-1}=\frac{2\,c\,M}{\hbar}$ — the source's $\lambda_0$ being the reduced Compton length $\frac{\hbar}{c\,M}$, since only for that reading does $(\lambda_0/2)^{-1}$ equal $\frac{2\,c\,M}{\hbar}$; the source identifies this with the quantum of complex time, the **chronon**, and notes that it comes out of Compton order and not of Planck order — the fusion condition gives

$$
\Delta\alpha =\frac{2\,c\,M}{\hbar}\int  dS =\frac{\Delta\,A}{\hbar} = 2\pi N ,
$$

the condition for maxima of interference in the relativistic case, with the phase lag proportional to the path difference and the Minkowski interval as the invariant measure.

**The printed chain cannot hold as written, and the de Broglie endpoint decides which half of it is meant.** The two halves disagree by a factor two: with the free-particle action $A=Mc\int dS$ and $S$ the Minkowski interval, the condition $\frac{\Delta\,A}{\hbar}=2\pi N$ gives $\Delta\alpha=(\frac{c\,M}{\hbar})\int  dS$, not $(\frac{2\,c\,M}{\hbar})$ times it. Recomputed here, with $S=\sqrt{{r'_{t}}^2-L^2}$ for a path of length $L$ flown in a time $r'_t$ at speed $V=L/r'_t$, the derivative is $\partial S/\partial L=-V/(c\sqrt{1-V^2/c^2})$, so the fusion spacing at $\mathrm{Const}=\frac{2\,c\,M}{\hbar}$ is $\lambda=h\sqrt{1-V^2/c^2}/(2MV)$, half the de Broglie wavelength, and at $\mathrm{Const}=\frac{c\,M}{\hbar}$ it is $\lambda=h\sqrt{1-V^2/c^2}/(MV)$ exactly, the de Broglie wavelength, with non-relativistic limit $h/(MV)$. The corpus records the de Broglie relation as the source's claim and the factor as unreconciled: the printed $\mathrm{Const}=(\lambda_0/2)^{-1}$ and the printed $=\frac{\Delta\,A}{\hbar}$ cannot both be meant, and the chronon reading — a quantum of complex time of Compton order and not of Planck order — survives either way. The source notes its correspondence with Feynman's $\tilde{Ξ}_{\mathrm{sp}}=R\exp(\frac{i\,A}{\hbar})$, whose phase is proportional to the classical action — for a free particle, to the proper time — and, expanding $dS$ in powers of $V/c$ and using the integrability of the zeroth-order term, recovers the ordinary de Broglie relation

$$
\Delta\int\frac{dL}{\lambda}=N ,
\qquad
\lambda:=\frac{h}{Mv} ,
$$

with the path difference of the two duplicons an integer number of de Broglie wavelengths. The claim is therefore not a new interference formula: the standard condition is what the construction is built to reproduce, the factor above being the only thing standing between the two, and what the programme adds is an interpretation, in which the phase and its integrality are geometric and no physical wave is introduced. The corpus records the interpretation as the source's and does not adopt its vocabulary; the Feynman phase-of-the-action structure it uses is the corpus's own subject in *The Path Integral in Biquaternionic Form*.

The same fusion picture has a finite, fully worked realisation in a separate line of the programme's work, where the worldline is not parametrised but given **implicitly**, by a system of polynomial equations $F_A(r_x,r_y,s)=0$ in plane motion — *Algebraic Dynamics on a Single Worldline: Vieta Formulas and Conservation Laws* (arXiv:1402.6158). At each value of the parameter $s$ the solutions of that system are the positions of the copies, so here the copies **are** the roots. A real root is called an R-particle; a complex conjugate pair is a single C-particle, whose real part is the position visible in the plane and whose imaginary parts are a hidden tail, and whose effective mass is twice that of an R-particle because it is counted twice. A fusion or a creation is then a multiple root, so the event condition is the vanishing of the Jacobian, $\det(\partial F_A/\partial x_B)=0$ — the caustic condition this article meets elsewhere on a congruence, met here on a polynomial system. For the paper's nine-root example the events fall at $s\approx-97.3689$, $-4.0246$, $-3$, $-2.7784$, $-2.7669$ and $2932.49$; at $s=1$ the system has one real root, $x\approx2.3079$, and four conjugate pairs; and near $s=-3$ the count of real roots rises to seven inside a window of width about $3\times10^{-5}$, which is why that event is easy to miss.

What the model adds is less than it appears, and the reason is algebraic. Its conservation laws are **Vieta's formulas, not Noether charges**. In the frame where the coefficients of degree $N-1$ vanish, the sum of the roots is identically zero, hence so is the total momentum, and one further derivative gives the vanishing of the sum of the accelerations — which for two particles is Newton's third law. That argument needs the roots to be scalars summed in a commutative field. Over a noncommutative algebra it fails, and the counterexample is immediate: $X^2+bX=0$ with $b^2=0$ has the roots $0$, $b$ and $-b$, whose sum is $0$ and not $-b$, verified here. The source uses no hypercomplex algebra at all — the words quaternion, biquaternion and Clifford do not occur in it — and its relativisation replaces the Minkowski interval by the Euclidean one $c^2dt^2=c^2ds^2+dr_x^2+dr_y^2+dr_z^2$, of the opposite signature to $Q_t=i q'_t$. Two of its printed shifts are also mis-signed: the shift removing the degree-$N-1$ term is $-f_{N-1}/(N f_N)$ and not the printed $(N-1)f_{N-1}/f_N$, and the worked transformation is $y=\tilde y-s$ and not $y=\tilde y+s$; the numbers above were recomputed with the corrected shifts. The model therefore stands beside the fusion picture as a computable Newtonian toy: the corpus records it as the source's, and it supplies the framework with no equation.

**The 2023 sequel, and the one thing it adds.** *The algebrodynamics: super-conservative collective dynamics on a "Unique Worldline" and the Hubble's law* (arXiv:2309.14375) keeps the construction, takes the worldline as **implicit** in three spatial unknowns — resolved by Sylvester resultants into one equation $f(x,t)=0$ in $x$ and the parameter — and puts the relativisation on a twistor footing: any such worldline generates a **null shear-free congruence** through the twistor incidence $\tau=X\zeta$, so the light cone is **induced** by the construction rather than **imposed** by adding the cone equation that arXiv:2104.12490 appends. The source presents this as a correction of its earlier procedure. The gain is real and it is narrow: the congruence is null in the Minkowski metric, and the metric enters through the Hermitian slice $X=X^{+}$, so what the paper removes is the cone **equation** and not the cone. The signature is the Minkowski one of the Hermitian subspace throughout, which is the corpus's own point that $\mathbb{B}_{\Phi}$ is a sector and not a second frame, and the commutative-scalar obstruction recorded above is untouched. Against that, the closing section reads the uniform recession of the roots at large parameter as a Hubble law with $H=1/t$, universal for all roots. That is Milne kinematics in the parameter of a polynomial: flat space, no matter, no redshift law, no scale-factor equation, and $q_0=0$ by construction. It does not close the corpus's cosmological obstacle, and it supplies the framework with no equation either.

## Random Complex Time and the Irreversibility of Physical Time

The last layer is the account of time, and it is explicitly a conjecture. In the complex picture the evolution parameter $\tau$ of a generating world line $z_\mu(\tau)$ is complex, so the next position of the world line under $\tau\mapsto\tau+d\tau$ is indefinite: the phase of $\tau$ is free. The source calls the curve $\tau=\tau(r'_t)$, with $r'_t$ a monotonically increasing real parameter, the **evolution curve**, and insists that only after the curve is specified can one order events and distinguish past from future — the curve *is* the arrow of time. It conjectures that the universal evolution curve is "extremely complicated and entangled", probably of a fractal-like nature, and that the walk of the complex parameter is effectively a random walk; if the walk is discrete there arise quanta of time, the chronons, again of Compton order. The source argues that the parameter that preserves both the primary twistor field and the caustic structure is the principal invariant $\sigma$ of complex proper time itself, so that complex "proper" time plays the role of a universal global time.

The mechanism by which the random complex time yields a definite arrow is a small piece of algebra, and it is the source's only stated reason for the irreversibility. With $T=\lvert\vec p\rvert^2+\lvert\vec q\rvert^2$ and increments $d\vec p,d\vec q$, the finite increment of the effective time coordinate is

$$
\Delta T = 2\,(\vec p\cdot d\vec p+\vec q\cdot d\vec q) + (d\vec p\cdot d\vec p+d\vec q\cdot d\vec q) .
$$

Under the averaging procedure the mixed term — which can have either sign — vanishes, and the averaged increment

$$
\delta T = d\vec p\cdot d\vec p+d\vec q\cdot d\vec q \equiv \Delta T
$$

is non-negative and behaves at a "physically infinitesimal" scale as a full differential, a holonomic quantity. The source's conclusion is that any macroscopic change of the particles' positions in the primary complex space necessarily increases the effective time coordinate, so irreversibility is kinematical and statistical in nature and the time coordinate resembles an entropy-like quantity, a probability measure. On top of the initially deterministic classical dynamics there then arises an unremovable and globally universal randomness in the evolution of an observable ensemble, tied to the conjectural stochastic character of the complex-time parameter. The source presents the phase $\alpha$ as at once the measure of the uncertainty of that evolution and the measure of the wave properties of matter, with a geometric origin and no appeal to the wave-particle-dualism paradigm.

These are programme statements and hopes, and the source offers them as a picture to be developed. The corpus records them beside its own time material in *The Quantum-Classical Divide in the Biquaternion Framework*, and the entropy-like interpretation beside *Coarse-Graining and the Biquaternion Entropy Functional*, adopting neither the vocabulary nor the interpretation. The source's arrow is kinematic and statistical, arising from the positivity of $\delta T$; the corpus's own second-law material obtains its asymmetry from coarse-graining, and the two accounts are not merged.

## Status, Contrasts, and Boundaries

The algebrodynamical programme is an ambitious and internally coherent proposal, and its boundaries should be stated as plainly as its claims.

**What it genuinely adds.** It supplies (i) a **nonlinear** primary equation over the biquaternion algebra, distinct from the corpus's linear Fueter theory, whose integrability conditions reproduce the linear gauge equations; (ii) a mechanism — over-determination plus self-duality plus weak gauge invariance — that **restricts electric charge to integer multiples of a minimal value**, a quarter in the programme's later units, and identifies the elementary charge with that minimal value, which addresses the corpus's charge-quantisation boundary (the integrality is what the theorem gives; the number is a normalisation, as recorded in the proof above); (iii) an **explicit algebraic origin of the Minkowski interval** from the complex invariant of the algebra, which for *Why Complexify Spacetime?* is the derived signature it currently only motivates; and (iv) a generation mechanism in which the metric, the electromagnetic field and the Yang–Mills field descend from one twistor function with coincident singularities — though the twistor function fixes the congruence and not the field, since every holomorphic $F(G)$ carries its own Maxwell field on the same congruence and in the same Kerr–Schild background. Two further items were added to this article after the arXiv version of the source paper was read in full: (v) an explicit **ring family** $\Pi=G^n/H$ with radii $R_n=a(n-1)/\sqrt{n(n-2)}$, recomputation-verified here, whose $n=2$ member is the **Hopf map**, so the Hopf fibration appears as a member of the eikonal family; and (vi) the **multivaluedness** thesis — that the principal field is multivalued by construction, that a mode's univaluedness is the source of charge quantisation, and that the eikonal field is at once the fundamental field (class I) and a characteristic field (class II). A further pass, on the 2009 survey *Algebrodynamics over Complex Space and Phase Extension of the Minkowski Geometry*, added: (vii) the **explicit phase-extension invariants** of the induced geometry — with $\vec z=\vec p+i\vec q$ and $\vec p,\vec q$ real, $\sigma=(\lvert\vec p\rvert^2-\lvert\vec q\rvert^2)+2i\,\vec p\cdot\vec q$, $T=\lvert\vec p\rvert^2+\lvert\vec q\rvert^2\ge0$ and $\vec X=2\,\vec p\times\vec q$ with the sign fixed by recomputation, the source's interpretation of the real and imaginary parts of $\sigma$ as the electromagnetic invariants, and the velocity–orientation relation $\cos^2\theta=(1-V^2)/(1+V^2\cot^2\alpha)$; and (viii) the **dimerous-electron** interpretation of charge and interference — an electron as a pair of duplicons whose fusions are the interaction acts, the geometric phase of complex time as the interference phase, the fusion condition $\Delta\alpha=2\pi N$ and the recovered de Broglie relation — together with the **random complex time** and the kinematic-statistical irreversibility from the positivity of $\delta T$. The 1995 paper *Biquaternion Electrodynamics and the Weyl–Cartan Geometry of Space-Time*, whose text became available in this pass, added (ix) the **Weyl–Cartan geometry and the Yang–Mills triplet**: the complex spinor connection $\Gamma_\nu=G\varsigma_\nu$, whose four-vector form $\Gamma_{\mu\nu\rho}=2(A_\nu\delta_{\mu\rho}+A_\rho\delta_{\mu\nu}-A_\mu\delta_{\nu\rho}-i\varepsilon_{\mu\nu\rho\alpha}A_\alpha)$ is determined by the potential $A_\mu=2G_\mu$; the **$*$-unitary field** $\mathcal{U}=FF^\dagger$, whose condition is carried by the **real** connection $\Delta_{\mu\nu\rho}=2(a_\nu\delta_{\mu\rho}+a_\rho\delta_{\mu\nu}-a_\mu\delta_{\nu\rho}-\varepsilon_{\mu\nu\rho\alpha}b_\alpha)$ with $a=\Re A$, $b=\Im A$, so that the Weyl non-metricity is the Coulomb field and the torsion pseudotrace is a second field, which would be unobservable because torsion is absent from the geodesic equation, together with the observation that this connection had been shown by Stepanov to be the unique one compatible with a conventional covariant spinor derivative; the **inhomogeneous Lorentz condition** $D=\sum_\mu \partial/\partial x_\mu A_\mu+2\sum_\mu A_\mu A_\mu=0$ beside the self-duality; the rigidity argument by which two independent spinor solutions force $\mathrm{Ric}_{\mu\nu}=0$ and non-triviality therefore forces $\det F=0$, so that the field takes its values on the null divisors and an **indefinite signature** is a necessary condition of non-trivial dynamics rather than a postulate; and the explicit **complex gauge triplet** $N_{0a}=A_a$, $N_{ba}=\delta_{ab}A_0-i\varepsilon_{abc}A_c$, whose self-dual strength obeys the Yang–Mills equation and whose modulus is the electromagnetic field strength, $\sum_a(L_{\mu\nu a})^2\propto(F_{\mu\nu})^2$. The closed-form static solution $f^\pm=(r_x\pm ir_y)/(r\pm r_z)=\tan^{\pm1}(\theta/2)\exp(\pm i\theta_{\mathrm{azm}})$, the stereographic map $S^2\to\mathbb{C}$, and its complex potential $A_0=\pm1/(2r)$ with charge $ϙ=\pm1$ were recomputed here; the connection, the curvature-invariant proportionality and the triplet-modulus constant were not, because they hold on the solutions of the primary system. The 1998 conference paper *Particles as Singularities within the Unified Algebraic Field Dynamics* (arXiv:gr-qc/9809056) added (x) the physical flesh of the particle interpretation, all of it recomputed here where it is checkable. It gives the unisingular solution in a **self-consistent normalisation**, $A_0=\pm1/(4r)$ differentiating to $E_r=\pm1/(4r^2)$, with the electric field pure real and the magnetic field pure imaginary, so that the printed inconsistency of the 1995 pair is superseded and the elementary charge is fixed at $\tfrac14$; the singular solutions are **dions**, $ϙ=\pm\tfrac14$ with magnetic charge $m=\pm i/4$ of equal magnitude; the imaginary sector — the electric dipole moment — is "phantom", entering only the totally skew-symmetric torsion and therefore not the geodesic equations. It obtains the ring as the **complex translation** $z\mapsto z+ia$ of the point solution, the Appel potential $A_0=ϙ/r_*$, whose far field was recomputed here to be that of a charge with magnetic dipole moment $\mu=qa$ and electric quadrupole moment $\vartheta=-2qa^2$; and it draws from those two moments the programme's **only numerical prediction**, that fixing $|a|=\frac{\hbar}{2\,c\,M}$ to reproduce the Dirac moment forces $\lvert\vartheta\rvert=\frac{\hbar^{2}\,q}{2\,c^{2}\,M^{2}}$ — an algebraic identity, verified here, which the source itself calls speculative while noting it might be testable. Finally it reads the evolution of the singular loci through **catastrophe theory**, with the perestroika of a caustic set as a mutual transmutation of particles. The 2016 conference note *Relativistic Algebra of Space-Time and Algebrodynamics* added (xi) the **local algebra**: the covariant multiplication law of Grgin's algebra, verified here to be the biquaternion multiplication for one sign of its $\varepsilon$ term and the reversed multiplication for the other; the **local $L$-algebra** on a curved manifold, whose existence requires a tetrad and a **time-like unit field** beside the metric; the **effective metric** $g_{\mathrm{eff},\rho\lambda}=2E_\rho E_\lambda-g_{\rho\lambda}$, whose flat case is the four-dimensional *Euclidean* metric, and the identity $g^*_{\mu\nu}=\tfrac14C_{\beta\,\mu\alpha}C_{\alpha\,\nu\beta}=g_{\mathrm{eff},\mu\nu}$, which extracts the same metric from the structure functions of the local algebra alone — a coincidence the source calls remarkable, which the recomputation here reduces to the rest frame of the unit field: the identity is exact there and fails for a tilted $E$, so the source's hedge cannot be removed; and the induced connection $\Gamma=\gamma+G$, of the same Weyl–Cartan type, whose non-metricity is $\nabla_\rho g_{\mu\nu}=-2g_{\mu\nu}\tilde A_{\Phi,\rho}$ with $\tilde A_{\Phi,\rho}=(2E_\rho E_\lambda-g_{\rho\lambda})A_\lambda$, so that the Weyl vector is the potential read through the effective metric rather than the potential itself. All four items were verified here where they are checkable; the note's expectation that the same conditions will determine the metric and the unit field is left by the source as future work and is recorded as a hope.

**What it does not supply.** It is classical: the algebra contains no $\hbar$, and the quantum interpretation is programmatic. It is non-Lagrangian and over-determined, so it has no standard canonical quantisation, and the source itself says that quantising an over-determined system requires new methods. The charge quantisation is conditional on the singularity structure and is not a derivation of the numerical value of the electron charge. The induced geometry is developed for the complex three-space and its identification with the physical macro-geometry is a mapping into the causal domain, not a dynamical construction. And the duplicon, dimerous-electron, chronon and complex-time ideas are explicitly hopes: the dimerous-electron argument recovers the standard interference condition rather than replacing it, and the phase–modulus proportionality $d\alpha=\mathrm{Const}\cdot dS$ that turns it quantitative is an assumption of the source, not a consequence of the algebra.

**The other external claim to the same boundary.** This programme is not the corpus's only external source that claims to *derive* charge quantisation, and the two should be named together, because they do it on opposite kinds of equation. This one works on a **nonlinear, over-determined** primary equation and obtains the quantisation from over-determination, self-duality and weak gauge invariance, with the additional topological route through the univaluedness of a mode of the multivalued field; the charge comes out as a multiple of a quarter, and the elementary charge is identified with the minimal admissible value. The other is the claim of Gsponer and Hurni (*Lanczos's Equation to Replace Dirac's Equation?*, Lanczos centenary, 1994; arXiv:hep-ph/0112317), on the **linear** Einstein–Mayer generalized-mass system, where the solutions are classified into quarks and leptons and the electric charges — fractional and integral as required — and the baryonic charge are read off the classification, with the neutrino and the \mathrm u-quark masses zero by eigenvalue equations. Neither is a result of this corpus, and the corpus's linear framework is silent on both; what the pair establishes is that the boundary is attacked from two directions and by two different mechanisms, one nonlinear-dynamical and one linear-algebraic. The distinction is worth keeping because the corpus's own statement of the boundary — that the biquaternion framework re-expresses the Dirac condition but does not derive the quantum of charge — is a statement about the **linear** framework, and a reader who meets either claim should see the other beside it and see which equation it rests on. Both are recorded as claims: the second is four pages with no derivation exhibited, and the first is conditional on the singularity structure and does not derive the numerical value of the electron charge.

**The corpus's relation to it.** The corpus records the programme and does not endorse it. Where the programme overlaps corpus material — the Klein–Penrose incidence, the spinor module, the null cone as zero divisors, the Fueter theory, the Kerr–Schild metric, the electromagnetic invariants — the overlap is noted and the corpus's own treatment is not displaced. Where the programme is genuinely distinct — the nonlinear primary equation, the self-quantized charge, the induced interval with phase — it is recorded once, here, with cross-references, in the same spirit as the other external programmes in *Biquaternion Electromagnetism*.

**A note on the source text.** The PDF of the source paper used here has a degraded text layer in which the letter "c" is systematically dropped, so verbatim quotation is unreliable and the paper's own theorem numbers could not be read with confidence. No theorem number of the source is cited for that reason, and every algebraic statement that could be checked independently was recomputed before it was written: the rank-one degeneracy of the gradient, the transformation to the complex eikonal, the imaginary-part relations of the self-dual field, the Kerr solution's first-order system, its complex eikonal, its wave equation and the harmonicity of $\ln G$, and the identity behind the induced interval all pass. The PDF of arXiv:1105.3498 is degraded in a different way — its two columns are interleaved line by line and its displayed formulas are split across the gutter — so no equation number of that paper is cited either, and the statements taken from it were recomputed as listed in *The family, and what the congruence does not fix*.

## Summary

The algebrodynamical programme replaces the naive derivative of a quaternionic function — which exists only for linear functions — by the **two-sided** condition $dF=L\,dZ\,R$, which for $\mathbb{H}$ characterises the conformal maps of $E^4$ and, after complexification, admits **degenerate** conformal maps into the null divisors of the algebra. Fixing a component $\Sigma$, the condition says that the matrix of derivatives of $\Sigma$ has rank one, so its determinant vanishes: this is a **nonlinear analogue of the Laplace equation**, which in biquaternion coordinates is the complex eikonal of complexified Minkowski space.

The eikonal is solved algebraically by a twistor, through the Kerr equation $\Pi(G,wG+\upsilon,vG+p)=0$ for an arbitrary holomorphic world function $\Pi$; the two classes $\Pi=0$ and $d\Pi/dG=0$ exhaust the analytic solutions on the source's account. The physically relevant solutions come from a spinor splitting of the two-sided condition, the **generating system of equations**, which is over-determined (eight equations for six unknowns). Its integrability conditions force the curvature of an associated Weyl–Cartan connection to be **weakly self-dual**, and the Bianchi identity then yields the free Maxwell and Yang–Mills equations for the trace and trace-free parts of the curvature. The linear field equations are thus consequences of the primary nonlinear system.

The geometry behind those integrability conditions is explicit in the programme's 1995 presentation, and it is recorded here because it supplies four further claims. The spinor connection $\Gamma_\nu=G\varsigma_\nu$ is a complex affine connection of Weyl–Cartan type, determined by the electromagnetic potential $A_\mu=2G_\mu$ alone; passing to the **$*$-unitary field** $\mathcal{U}=FF^\dagger$ replaces it by a **real** connection whose Weyl non-metricity $a_\mu=\Re A_\mu$ is the Coulomb field and whose torsion pseudotrace $b_\mu=\Im A_\mu$ is a second field that does not enter the geodesic equation. The same connection is the one Stepanov showed to be the unique space-time connection compatible with a spinor-bundle structure carrying the conventional spinor derivative, which makes the programme's central geometric object one the corpus already uses. The integrability conditions include, beside the self-duality, the **inhomogeneous Lorentz condition** $D\equiv\sum_\mu \partial/\partial x_\mu A_\mu+2\sum_\mu A_\mu A_\mu=0$, a nonlinear condition with a term quadratic in the potential, which the source relates to the vanishing scalar curvature of the effective space. Non-triviality forces $\det F=0$ — the primary field takes its values on the **null divisors**, the complex light cone — and null fields exist only on **indefinite-signature** manifolds, the programme's sharpest statement that the Lorentzian signature is forced rather than postulated, the boundary stated in *Why Complexify Spacetime?*. Finally the trace-free part of the connection is a complex gauge triplet $N_\nu$, fixed linearly by the same potential through $N_{0a}=A_a$, $N_{ba}=\delta_{ab}A_0-i\varepsilon_{abc}A_c$, whose self-dual strength obeys the Yang–Mills equation; the curvature splits into a trace part proportional to $F_{\mu\nu}$ and this triplet strength, and $\det \mathrm{Ric}_{\mu\nu}=0$ makes the electromagnetic field strength the **modulus of the Yang–Mills triplet**, $\sum_a(L_{\mu\nu a})^2\propto(F_{\mu\nu})^2$ — a proportionality whose constant is convention-dependent and is not reconciled here.

The 2016 conference note extends the geometry in one direction, from the flat case to a manifold. Its starting point is the **covariant multiplication law** proposed by Grgin, written with the plain weight, the Levi-Civita symbol and a distinguished unit element $e$ with $e_\mu e_\mu=1$: with $e=(1,0,0,0)$ it is the biquaternion multiplication for one sign of its $\varepsilon$ term and the reversed multiplication for the other — the identification, overlooked in Grgin's own paper, that the note supplies, verified here on random pairs. On a curved manifold the same table defines a **local algebra** whose basis vectors are a tetrad, $\Sigma_\mu=h_{\alpha\,\mu}\sigma_\alpha$, so that the metric arises from the tetrad, $g_{\mu\nu}=h_{\alpha\,\mu}h_{\beta\,\nu}\varepsilon_\alpha\delta_{\alpha\beta}$, and the unit element becomes a **unit time-like vector field**, the **unit field** $E_\mu=h_{\alpha\,\mu}e_\alpha$: the existence of the local algebra therefore requires a unit field beside the metric, and the note reads it as the flow of matter. It is not the corpus's $*$-unitary field $\mathcal{U}=FF^\dagger$, which is built from the primary field; here it belongs to the geometry. Two metrics follow from the construction. The **effective metric** $g_{\mathrm{eff},\rho\lambda}=2E_\rho E_\lambda-g_{\rho\lambda}$ has the flat case $g_{\mathrm{eff}}=\mathrm{diag}(1,1,1,1)$ — the flat limit's effective metric is **Euclidean**, which the source calls surprising and which is exact — and is the reflection of $g$ in the $E$ direction; and the metric built from the **structure functions** of the local algebra, $g^*_{\mu\nu}=\tfrac14C_{\beta\,\mu\alpha}C_{\alpha\,\nu\beta}$ with $C_{\rho\mu\nu}=\delta_{\rho\mu} E_\nu+\delta_{\rho\nu} E_\mu-E_\rho g_{\mu\nu}\pm i\sqrt{-g}\,\varepsilon_{\rho\mu\nu\lambda}E_\lambda$, is the *same tensor*: the identity $g^*=g_{\mathrm{eff}}$ holds in the rest frame of the unit field and only there — it fails for a tilted $E$, by a discrepancy quadratic in the spatial part of $E$, where the source states it for any metric of determinant $-1$. The connection the curved differentiability condition induces, $\Gamma=\gamma+G$ with the Levi-Civita $\gamma$, is of the same Weyl–Cartan type as the 1995 one — non-symmetric in its lower pair, hence with torsion — and its non-metricity is $\nabla_\rho g_{\mu\nu}=-2g_{\mu\nu}\tilde A_{\Phi,\rho}$ with $\tilde A_{\Phi,\rho}=(2E_\rho E_\lambda-g_{\rho\lambda})A_\lambda$, an identity verified in the flat case: the Weyl vector is the potential read through the effective metric, which returns the potential itself in the rest frame of the unit field and departs from it under a boost, and that is the one place the note's geometry differs from the 1995 geometry rather than merely restating it. The note expects the integrability conditions to restrict the metric and the unit field as well as the potential, and determines none of them; the corpus records the expectation as a hope.

The solutions of the primary system are generated from $\Pi$ alone. Their singular locus — the branch set $d\Pi/dG=0$ — is simultaneously the singularity of the effective curvature, the electromagnetic field and the Yang–Mills field, which the programme reads as the statement that a particle is a common singularity of all the associated fields. The **headline claim** is that these singular solutions have **self-quantized electric charge**: self-duality together with the weak gauge invariance of the primary system restricts the charge to integer multiples of $1/(2b)$ — the dion relation from Gauss's theorem, then Dirac's string argument in complex form — and $b=2$ in the programme's later units gives $ϙ=N/4$, the fundamental static solution has the minimal value $|ϙ|=\tfrac14$, forced as the unique scale at which the two sides of a first-order constraint balance, with a ring singularity of radius $a$, it reproduces the Kerr–Newman field and metric with $g=2$, and it is the programme's classical model of the electron. In the 1998 presentation the same solution carries $A_0=\pm1/(4r)$ with $E_r=\pm1/(4r^2)$ — a potential and a strength that are mutually consistent, fixing the elementary charge at $\tfrac14$ — and it is a **dion**, with magnetic charge $m=\pm i/4$ of the same magnitude as the electric one; the imaginary sector of the complex field carries the magnetic charge and the electric dipole moment, is called "phantom" by the source, and enters only the longitudinal (totally skew-symmetric) torsion, so that it does not enter the geodesic equation and would be unobservable. The ring itself is the **complex translation** $z\mapsto z+ia$ of the point solution, with the Appel potential $A_0=ϙ/r_*$; its far field, recomputed here, is that of a charge $ϙ$ with **magnetic dipole moment $\mu=qa$** and **electric quadrupole moment $\vartheta=-2qa^2$**. Requiring $\mu$ to take the Dirac value forces $|a|=\frac{\hbar}{2\,c\,M}$ and hence $\lvert\vartheta\rvert=\frac{\hbar^{2}\,q}{2\,c^{2}\,M^{2}}$, the programme's only numerical prediction — a one-line algebraic identity, verified here, which the source states as a conjecture and calls speculative. Those values are properties of the **static** member: in the source's non-stationary generalization the ring contracts and re-expands, the charge stays fixed while the magnetic moment tracks the current radius, and the source himself reports the static congruence as unstable with respect to its scale. And the evolution of the singular loci is read through **catastrophe theory**: a perestroika of a caustic set is a mutual transmutation of particles, for which the bisingular solution is the evidence. The claim is the programme's, conditional on the singularity structure, and it engages the corpus's stated open boundary on charge quantisation without settling it.

The scheme is organised by a **world function** $\Pi$: the class-I solution is the fundamental field, and the class-II conjugate, built from $d\Pi/dG=0$, is the characteristic field whose vanishing marks the branching locus. For an irreducible $\Pi$ the principal field is **multivalued**, and each locally chosen branch is a mode carrying its own congruence and fields; the source holds that this multivaluedness is required rather than tolerated, that fields which constitute particles need not be univalued, and that univaluedness of a single mode is itself the source of the charge quantisation — a second route to $ϙ=N/4$ beside self-duality. The singular loci of the static family $\Pi=G^n/H$ are the rings $z=0$, $x^2+y^2=R_n^2$ with $R_n=a(n-1)/\sqrt{n(n-2)}$ ($n\ge3$), recomputation-verified here, and the $n=2$ member is the Hopf map; a fourth-order generating function gives the corpus's clearest multiparticle example, two opposite elementary charges inside a neutral cocoon that cancels at $r'_t=b/\sqrt2$ and emits a light-like wavefront. The quadratic family is exhausted, up to Poincaré transformations, by the Kerr-like static solution and the nonstationary bisingular one, with the neutral, null figure-eight as a member; and the wave-like solutions give a closed form in the **Lambert function** whose singular set is a **neutral helix of radius $1/(\varpi A e)$ and lead $2\pi/\varpi$**, the most concrete particle-like object in the material. In the conclusion the source states the purpose of the construction as the corpus states its own: one abstract structure — the biquaternion algebra with its generalised Cauchy–Riemann conditions — successively expressed in several equivalent geometric languages, *covariantly constant fields, twistor geometry, shear-free congruences*, and the source's last layer identifies the Flow of Time with the Flow of Prelight.

The programme's geometry is **induced**: the complex invariant $\sigma=(z_1)^2+(z_2)^2+(z_3)^2$ has a modulus part obeying the identity $\sigma\sigma^{*}=T^2-\lvert\vec X\rvert^2$, so the Minkowski interval and the Lorentz action arise from the algebra rather than being postulated, with the phase of $\sigma$ as an extra internal variable. On this background the programme builds a speculative picture of particles as caustics of a primordial light flow, of time as an automorphism of the primary twistor field, and of an ensemble of complex-space "duplicons" related to quantum uncertainty. A later survey pass made four additions, three of them recorded as the source's. The induced geometry's invariants are given explicitly in the real splitting $\vec z=\vec p+i\vec q$: $\sigma=(\lvert\vec p\rvert^2-\lvert\vec q\rvert^2)+2i\,\vec p\cdot\vec q$, $T=\lvert\vec p\rvert^2+\lvert\vec q\rvert^2\ge0$, $\vec X=2\,\vec p\times\vec q$, with the source's reading of the real and imaginary parts of $\sigma$ as the electromagnetic invariants and the velocity–orientation relation $\cos^2\theta=(1-V^2)/(1+V^2\cot^2\alpha)$. The **dimerous electron** is read as a pair of duplicons whose fusion events are the interaction acts; the geometric phase of complex time supplies the interference phase, and the fusion condition $\Delta\alpha=2\pi N$ reproduces the relativistic interference condition and, in the nonrelativistic limit, the de Broglie relation. The **ensemble of duplicons** is stated explicitly: the partners of a point of a complex world line are the roots of the complex null-cone equation, and $(\lambda-\tau)^2$ always divides that equation, so a generic polynomial line of degree $d$ carries $2d-2$ of them and a strictly timelike line carries none — a count supplied here and not by the source. And **random complex time** yields the arrow of time: the averaged increment $d\vec p\cdot d\vec p+d\vec q\cdot d\vec q\ge0$ makes irreversibility kinematic and statistical, with the "chronon" of complex time conjectured to be of Compton order. These are hopes, recorded as such. The programme is an external programme: the corpus records it, does not endorse it, and does not adopt its vocabulary.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong\mathrm{Mat}(2,\mathbb{C})$ | Biquaternion algebra, read in the programme as an algebra of coordinates |
| $Z$, $Z_{AB}$ | Complex matrix variable and its four entries |
| $\upsilon,v,w,p$ | The entries $Z_{00},Z_{11},Z_{01},Z_{10}$ |
| $z_0,z_1,z_2,z_3$ | Cartesian coordinates, $z_0=(\upsilon+v)/2$, $z_3=(\upsilon-v)/2$, $z_1=(w+p)/2$, $z_2=i(w-p)/2$ |
| $\det Z=(z_0)^2-\dots-(z_3)^2$ | Source's holomorphic metric; the corpus's $\langle\cdot\rangle_{\natural}$ once $Q_t=z_0$, $Q_\eta=iz_\eta$ |
| $dF=L\,dZ\,R$ | Two-sided $A$-differentiability; $L,R$ the semi-derivatives |
| $\Sigma$ | A component of a differentiable function; the eikonal potential |
| $\partial/\partial\upsilon,\dots$ | Partial derivatives with respect to $\upsilon,v,w,p$ |
| $\det\lVert\nabla_{AB}\Sigma\rVert=0$ | The nonlinear (complex-eikonal) equation |
| $\tilde{Ξ}_{\mathrm{sp}},\tau$ | Spinor and incident twistor, $\tau=Z\tilde{Ξ}_{\mathrm{sp}}$ |
| $z_\mu(\tau)$, $\lambda$ | Complex world line and the two parameters of the null-cone equation; here $\tau$ is the world-line parameter rather than the twistor component above, and $\lambda$ is neither the conformal scale factor of *The Two-Sided Derivative and Conformal Mappings* nor the de Broglie wavelength of *The Dimerous Electron and Quantum Interference* |
| $G=\tilde{Ξ}_{\mathrm{sp},1}/\tilde{Ξ}_{\mathrm{sp},0}$ | The principal spinor ratio |
| $\kappa_0=wG+\upsilon$, $\kappa_1=vG+p$ | Projective twistor components |
| $\Pi(G,\kappa_0,\kappa_1)$ | Generating (world) function; the Kerr equation is $\Pi=0$ |
| $P=d\Pi/dG$ | Singular-locus condition, $P=0$ |
| $\Lambda=d^2\Pi/dG^2$ | Class-II branching condition; with $P=0$ it gives the singular locus |
| $\mathcal{D}=\partial/\partial w-G\,\partial/\partial\upsilon$, $\tilde{Ξ}_{\mathrm{sp},\upsilon\upsilon},\tilde{Ξ}_{\mathrm{sp},\upsilon w},\tilde{Ξ}_{\mathrm{sp},ww}$ | Ray derivative, vanishing on $G$ by the shear-free equation; the Maxwell spinor $\tilde{Ξ}_{\mathrm{sp},\upsilon\upsilon}=\partial^2F/\partial\upsilon^2$, $\tilde{Ξ}_{\mathrm{sp},\upsilon w}=\partial^2F/\partial w\,\partial\upsilon$, $\tilde{Ξ}_{\mathrm{sp},ww}=\partial^2F/\partial w^2$ for a holomorphic $F(G)$, one field per $F$ on the same congruence |
| $H=wG^2+2(z+ia)G-\bar w$ | Static twistor generator; $w=x-iy$, $\bar w=x+iy$, $z$ the third Cartesian coordinate |
| $G_{\mathrm{ϙ}}=\mathrm{ϙ}\bar w/(z+r)$, $\mathrm{ϙ}=4ϙ$ | The Coulomb family of the static superpotential; the first-order constraints force $\mathrm{ϙ}=1$ |
| $r_*^2=x^2+y^2+(z+ia)^2$ | The $r_*$ of the static Kerr solution, of its $n=2$ class-II partner, and of the Appel potential $A_0=ϙ/r_*$; the radicand of the circle electron, with $a$ the corpus's $\varrho$ |
| $R_n=a(n-1)/\sqrt{n(n-2)}$ | Ring radii of the class-II family $\Pi=G^n/H$, $n\ge3$ |
| $A_0=ϙ/r_*$ | Appel potential: the complex translation $z\mapsto z+ia$ of the point solution |
| $\mu=qa$, $\vartheta=-2qa^2$ | Magnetic dipole and electric quadrupole moments of the complex-shifted ring |
| $\vartheta=-2qa^2=-\frac{\hbar^{2}\,q}{2\,c^{2}\,M^{2}}$ | Quadrupole forced when $\lvert  a\rvert=\frac{\hbar}{2\,c\,M}$ gives the Dirac moment; the programme's one numerical prediction |
| $\kappa_0\kappa_1-a^2G^2$ | Generating function of the neutral, null figure-eight solution |
| $W(z),\ W \exp(W)=z$ | Lambert function; solves $G=A\exp[i\varpi\kappa_0]$ in closed form |
| $\varpi$, $A$ | Frequency and amplitude of the wave-like solution; the source writes the frequency $\Omega$, reserved here for the connection |
| $1/(\varpi A e)$, $2\pi/\varpi$ | Radius and lead of the wave-like neutral-helix singular set |
| $G^2\kappa_0^2+\kappa_1^2-b^2G^2$ | Generating function of the four-mode two-charge example, annihilating at $r'_t=b/\sqrt2$ |
| $\eta,\zeta,Ξ$ | Biquaternion spinors and the complex four-vector of the fundamental spinor system |
| $\Omega=\tilde{Ξ}_{\mathrm{sp}}\,dZ$ | $\mathbb{B}$-valued connection; $\tilde{Ξ}_{\mathrm{sp}}$ the gauge potential |
| $R=d\Omega-\Omega\wedge\Omega$ | Curvature; weakly self-dual on GSE solutions |
| $\vec E$, $\vec H$ | Complex field strengths of the programme, the source's tilde; $\mathbb C$-valued throughout, and no real field appears in this article |
| $\vec N=\vec E+i\vec H$ | The complex field as one vector; $\vec N=0$ is the self-duality condition, and on its solutions $\Im\vec H=\Re\vec E$, $\Im\vec E=-\Re\vec H$ |
| $A_\mu=2G_\mu$ | Electromagnetic four-potential of the programme |
| $\Gamma_\nu=G\varsigma_\nu$, $\Gamma_{\mu\nu\rho}$ | Complex spinor connection and its four-vector form, of Weyl–Cartan type; $\varsigma_a$ the spin-matrix basis, distinct from the invariant $\sigma$ |
| $\mathcal{U}=FF^\dagger$, $\Delta_{\mu\nu\rho}$ | $*$-Unitary field and the real connection it obeys |
| $a_\mu=\Re A_\mu$, $b_\mu=\Im A_\mu$ | Weyl non-metricity (Coulomb field) and torsion pseudotrace |
| $e$, $e_\mu e_\mu=1$ | Distinguished unit element of the covariant multiplication law of Grgin's algebra $G\cong\mathbb{B}$ |
| $h_{\alpha\,\mu}$, $\Sigma_\mu=h_{\alpha\,\mu}\sigma_\alpha$ | Tetrad and the basis vectors of the **local $L$-algebra** |
| $E_\mu=h_{\alpha\,\mu}e_\alpha$, $(g^{-1})_{\mu\nu}E_\mu E_\nu=1$ | The **unit field** the local algebra requires; *not* the $*$-unitary field $\mathcal{U}=FF^\dagger$ |
| $g_{\mathrm{eff},\rho\lambda}=2E_\rho E_\lambda-g_{\rho\lambda}$ | Effective metric; $\mathrm{diag}(1,1,1,1)$ when $g_{\mu\nu}=\varepsilon_\mu\delta_{\mu\nu}$, $E=(1,0,0,0)$ |
| $C_{\rho\mu\nu}$ | Structure functions of the local algebra, $\Sigma_\mu\circ\Sigma_\nu=C_{\rho\mu\nu}\Sigma_\rho$ |
| $g^*_{\mu\nu}=\tfrac14C_{\beta\,\mu\alpha}C_{\alpha\,\nu\beta}$ | Metric built from the structure functions alone; equals $g_{\mathrm{eff}}$ in the rest frame of the unit field only |
| $\Gamma=\gamma+G$, $\tilde A_{\Phi,\rho}=(2E_\rho E_\lambda-g_{\rho\lambda})A_\lambda$ | Induced connection (Levi-Civita plus algebraic part) and its Weyl non-metricity vector, $\nabla_\rho g_{\mu\nu}=-2g_{\mu\nu}\tilde A_{\Phi,\rho}$ |
| $D=\sum_\mu \partial/\partial x_\mu A_\mu+2\sum_\mu A_\mu A_\mu$ | Inhomogeneous Lorentz condition; the source relates it to the scalar-curvature invariant |
| $N_\nu=\sum_a N_{\nu a}\varsigma_a$, $L_{\mu\nu}$ | Trace-free complex gauge triplet and its strength |
| $f^\pm$, $A_0=\pm1/(2r)$ | Static eikonal solution (stereographic map) and its 1995 complex potential; charge $ϙ=\pm1$ in that normalisation |
| $A_0=\pm1/(4r)$, $E_r=\pm1/(4r^2)$, $H_r=\pm i/(4r^2)$ | Same solution in the 1998 normalisation: consistent potential and strengths, electric real, magnetic imaginary |
| $ϙ=\pm\tfrac14$, $m=\pm i/4$ | Electric and magnetic (dion) charges of the unisingular solution; the imaginary sector is phantom |
| $g_{\mu\nu}=\delta_{\mu\nu}+h\,\ell_\mu \ell_\nu$ | Kerr–Schild metric; $k$ the null congruence |
| $ϙ=N/4$, $N\in\mathbb{Z}$ | Self-quantized electric charge |
| $a$ | Ring radius of the fundamental static solution |
| $\kappa_0\kappa_1+b^2G$ | Generating function of the Born-type two-charge solution; the source writes it $\tau_1\tau_2+b^2G=0$ |
| $\sigma=(z_1)^2+(z_2)^2+(z_3)^2$ | Principal invariant of the complex three-space |
| $T=\vec z\cdot\vec z^{*}$, $\vec X=i[\vec z\times\vec z^{*}]$ | Induced time and space; $S^2=T^2-\lvert\vec X\rvert^2$ |
| $\vec z=\vec p+i\vec q$, $\vec p,\vec q$ real | Real/imaginary split of the complex three-vector (the source's $p,q$; renamed to clear the twistor coordinate $p$) |
| $\sigma=S \exp(i\alpha)$ | Modulus $S$ (ordinary proper time) and phase $\alpha$ (internal) of the principal invariant |
| $T=\lvert\vec p\rvert^2+\lvert\vec q\rvert^2$, $\vec X=2\,\vec p\times\vec q$ | Induced time and space in the $\vec p,\vec q$ split; $T\ge0$; sign $\vec X=+2\,\vec p\times\vec q$ recomputation-fixed |
| $\Delta\alpha=2\pi N$, $\lambda=h\sqrt{1-V^2/c^2}/(MV)$ | Dimerous-electron fusion condition; the de Broglie relation it is meant to recover, exact at $\mathrm{Const}=\frac{c\,M}{\hbar}$ and off by two at the printed $\frac{2\,c\,M}{\hbar}$ |
| $\delta T=d\vec p\cdot d\vec p+d\vec q\cdot d\vec q$ | Averaged time increment; non-negative, the source's kinematic arrow |
| $SO(3,\mathbb{C})$ | Automorphism group; six real parameters, isomorphic to $SO_0(3,1)$ (the double cover is $SL(2,\mathbb{C})$) |

## Further Reading

- V. V. Kassandrov, "Quaternionic Analysis and the Algebrodynamics", arXiv:0710.2895 [math-ph] (2007), the source paper of this article: the nonlinear Cauchy–Riemann conditions, the complex eikonal, the generating system, the gauge and twistor structures, the self-quantized charge, and the induced causal geometry.
- V. V. Kassandrov, "Electromagnetic Fields in Kerr–Schild Space-Times", arXiv:1105.3498 [gr-qc] (2011), for the material recorded in *The family, and what the congruence does not fix*: the twistor construction of a Maxwell field from a shear-free null congruence, with the spinor built from the second derivatives of an arbitrary holomorphic $F(G)$ and aligned with the congruence, the infinite family of fields on each Kerr–Schild background, the Coulomb spinor with $\lvert q\rvert=\tfrac14$ for $F=G^{-1}$ as the only member inheriting the symmetry, the remark that a general $F$ weakens or destroys the symmetry of the congruence, the charge-quantisation theorem for the isolated singularities, and the contracting ring as the third example. Verified here: the Maxwell equations for six choices of $F$, the alignment contraction, and the exact Coulomb spinor with its determinant $-1/(16r^4)$; not verified: the Maxwell identity for general $F$ in closed form, only function by function.
- V. V. Kassandrov, "Singular Sources of Maxwell Fields with Self-Quantized Electric Charge", in *Has the Last Word Been Said on Classical Electrodynamics?* (Rinton Press, 2004), 42–66, arXiv:physics/0308045, for the material recorded in *The theorem*, *The proof* and *Why the fundamental solution sits exactly at the quantum*: the dion relation $ϙ=im$ from Gauss's theorem on the self-dual field, the complex form of Dirac's string argument giving $ϙ=N/(2b)$, the identification $b=2$ of the weak gauge transformation $C_\mu\mapsto C_\mu+2\,\partial\ln\alpha/\partial x_\mu$, the resulting $ϙ=N/4$, the comparison with Dirac's $me=(\frac{\hbar\,c}{2})N$, the statement that the Coulomb superpotential satisfies the eikonal for every scale and the two first-order constraints only at $ϙ=\tfrac14$, the exclusion of plane waves by the constraints, and the conjecture that magnetic monopoles do not manifest themselves; also the complex-potential and superpotential construction, and the printed factor $1/r$ missing from $C_{\bar w}$, both recorded in *The Complex Potential of a Self-Dual Maxwell Field*. Recomputed here: the $c=c^2$ rigidity of the constraints on $G_c=c\bar w/(z+r)$, the Weyl system and the field strength from the corrected potential, and the failure of the printed one.
- V. V. Kassandrov, "Biquaternion Electrodynamics and the Weyl–Cartan Geometry of Space-Time", *Gravitation & Cosmology* **1** (1995) 216, arXiv:gr-qc/0007027, for the material recorded from the paper itself in *The Weyl–Cartan Geometry of the Programme* and *The Yang–Mills Triplet and the Electromagnetic Modulus*: the Clifford-theoretic argument for $\mathrm{Cl}_{3,0}$ over $\mathrm{Cl}_{1,3}$, the spinor connection $\Gamma_\nu=G\varsigma_\nu$, the complex Weyl–Cartan connection $\Gamma_{\mu\nu\rho}$ determined by the potential, the **$*$-unitary field** $\mathcal{U}=FF^\dagger$ and the real connection $\Delta_{\mu\nu\rho}$, the identification of the Weyl non-metricity with the Coulomb field and of the torsion pseudotrace with a second field, the note that this connection is the unique one compatible with a conventional covariant spinor derivative (Stepanov), the inhomogeneous Lorentz condition $D=\sum_\mu \partial/\partial x_\mu A_\mu+2\sum_\mu A_\mu A_\mu=0$, the rigidity that forces $\det F=0$ and an indefinite signature, and the complex gauge triplet $N_\nu$ whose self-dual strength obeys the Yang–Mills equation with the electromagnetic field strength as its modulus. Also the closed-form static solution $f^\pm=(r_x\pm ir_y)/(r\pm r_z)$ with the potential $A_0=\pm1/(2r)$ and charge $ϙ=\pm1$.
- V. V. Kassandrov and J. A. Rizcallah, "Relativistic Algebra of Space-Time and Algebrodynamics", arXiv:1612.02455 [physics.gen-ph] (2016), five pages, for the material recorded in *The Local Algebra on a Curved Manifold, and the Unit Field*: the covariant multiplication law of Grgin's algebra and its isomorphism with the biquaternion algebra — the identification the note says was overlooked in the paper that introduced the algebra, verified here on random pairs, with the one sign of its $\varepsilon$ term giving the ordinary product and the other the reversed product; the **local $L$-algebra**, whose basis vectors are the tetrad, $\Sigma_\mu=h_{\alpha\,\mu}\sigma_\alpha$, with the induced metric $g_{\mu\nu}=h_{\alpha\,\mu}h_{\beta\,\nu}\varepsilon_\alpha\delta_{\alpha\beta}$ and the required **unit field** $E_\mu=h_{\alpha\,\mu}e_\alpha$ (distinct from the 1995 paper's $*$-unitary field $\mathcal{U}=FF^\dagger$); the **effective metric** $g_{\mathrm{eff},\rho\lambda}=2E_\rho E_\lambda-g_{\rho\lambda}$, Euclidean in the flat case, and the "remarkable coincidence" $g^*_{\mu\nu}=\tfrac14C_{\beta\,\mu\alpha}C_{\alpha\,\nu\beta}=g_{\mathrm{eff},\mu\nu}$, in which the metric the connection is built from is obtained again from the structure functions of the local algebra alone — verified here in the rest frame of the unit field, where it is exact, and falsified for a tilted unit field, where the discrepancy is quadratic in the spatial part of $E$, the source stating it for any metric of determinant $-1$; and the induced connection $\Gamma=\gamma+G$ of Weyl–Cartan type, with torsion and with the Weyl-type non-metricity $\nabla_\rho g_{\mu\nu}=-2g_{\mu\nu}\tilde A_{\Phi,\rho}$, $\tilde A_{\Phi,\rho}=(2E_\rho E_\lambda-g_{\rho\lambda})A_\lambda$, verified here in the flat case. The note's expectation that the integrability conditions of the $L$-differentiability equations will restrict the metric and the unit field as well as the potential is left by it as future work.
- V. V. Kassandrov and J. A. Rizcallah, "Particles as Singularities within the Unified Algebraic Field Dynamics", Proceedings of the International Conference "Geometrization of Physics III" (Kazan State University, 1997), arXiv:gr-qc/9809056, for the material recorded in *Particle-Like Solutions and the Self-Quantized Charge*: the universal (generating) equations and their origin in Sheffers's $A$-differentiability, the reduction to the shear-free geodesic null congruence, self-duality and the inhomogeneous Lorentz condition as their integrability conditions, the Yang–Mills triplet with the modulus relation $\det\lVert \mathrm{Ric}_{\mu\nu}\rVert\equiv (F_{\mu\nu})^2-\sum_a L_{\mu\nu a}L_{\mu\nu a}=0$, the unisingular **dion** with $A_0=\pm1/(4r)$, $E_r=\pm1/(4r^2)$ real and $H_r=\pm i/(4r^2)$ imaginary, the "phantom" imaginary sector carrying the magnetic charge and the electric dipole moment through the Rodichev-type torsion, the **complex translation** $z\mapsto z+ia$ giving the Appel potential $A_0=ϙ/r_*$ with magnetic dipole moment $\mu=qa$ and electric quadrupole moment $\vartheta=-2qa^2$, the prediction $\lvert\vartheta\rvert=\frac{\hbar^{2}\,q}{2\,c^{2}\,M^{2}}$, and the catastrophe-theory reading of singularity perestroikas as mutual transmutations of particles.
- V. V. Kassandrov and J. A. Rizcallah, "Algebrodynamical Approach in Field Theory: Bisingular Solution and its Modifications", arXiv:gr-qc/9809078 (1998), for the bisingular solution in full: the generating function $\tau_1\tau_2+b^2G=0$, which with $\kappa_0=wG+\upsilon$ and $\kappa_1=vG+p$ resolves to the quadratic $vwG^2+(r'_t^2-r_z^2+r_x^2+r_y^2+b^2)G+\upsilon p=0$, whose two roots were checked here to satisfy it identically (the $b^2G^2$ term the figure-eight $\kappa_0\kappa_1-a^2G^2$ carries does not), the roots coinciding where $(r'_t^2-r_z^2-r_x^2-r_y^2+b^2)^2+4b^2(r_x^2+r_y^2)=0$, which is the caustic; two point charges of opposite elementary charge in mirror hyperbolic motion, $r_z=\pm\sqrt{r'_t^2+b^2}$, for real $b$; two fixed-radius rings in the same motion for complex $b^2=\alpha+i\beta$; the ring–torus–bridge history for imaginary $b=ia$, a ring of radius $a$ at $r'_t=0$ that expands at the speed of light and, past $r'_t=\lvert a\rvert$, splits into two toroidal bridges on the axis, $x=y=0$, $r_z=\pm\sqrt{r'_t^2-a^2}$, the time-reversed branch reading as an annihilation; the identification of the real-$b$ field with the classical Born solution of two uniformly accelerated charges, with the source's argument that the pair does not radiate and that the second mirror charge is an inevitable consequence of the Maxwell equations; and the Kerr–Schild metric $g_{\mu\nu}=\delta_{\mu\nu}+h\,e_{3\mu}e_{3\nu}$ of the solution, with zero twist and null radiation $T_{\mu\nu}=P_{33}e_{3\mu}e_{3\nu}$, the electromagnetic field entering only as a test field because complex self-duality makes its energy–momentum tensor vanish.
- V. V. Kassandrov, J. A. Rizcallah and N. V. Markova, "Twistor structures and boost-invariant solutions to field equations", arXiv:1808.05280 [gr-qc] (2018), for the axially symmetric and boost-invariant solution and the singularities of the fields it generates: the reduction of the twistor constraint to the single invariant $\kappa_0\kappa_1/G$, invariant under the complex rotation about the third axis, which leaves the bisingular generator $\kappa_0\kappa_1+b^2G=0$ as the unique generating function admitting both symmetries; the three cases of the singular locus, two points on the axis for real $b$, two tori for imaginary $b=ia$, the second of which carries the tips of the string-like singularities, and two circles of radius $\lvert b_1\rvert$ at $r_z=\pm\sqrt{r'_t^2+b_0^2}$ for complex $b=b_0+ib_1$; the electromagnetic field of the solution, the classical Born field of two oppositely charged point singularities in hyperbolic motion for real $b$, and the field of a neutral torus for imaginary $b$; the branch of $G$ on which the Yang–Mills and the Weyl fields carry no singularity beyond the caustic; and the observation that the Yang–Mills strength is the electromagnetic strength multiplied by a $G$-dependent $2\times2$ matrix, so that its Bianchi identity and its Yang–Mills equation are equivalent to their Abelian counterparts. Recomputed here: the invariance of $\kappa_0\kappa_1/G$, the factorisation of the caustic for imaginary $b$, and the double root of the quadratic in $G$ on both of its sheets. Quoted and not re-derived: the field components and the Weyl spinor, which the source states for the solution.
- V. V. Kassandrov, "General Solution of the Complex 4-Eikonal Equation and the Algebrodynamical Field Theory", *Gravitation & Cosmology* **8** Suppl. 2 (2002) 57, for the two classes of eikonal solutions.
- V. V. Kassandrov and V. N. Trishin, "Particle-like Singular Solutions in Einstein–Maxwell Theory and in Algebraic Dynamics", *Gravitation & Cosmology* **5** (1999) 272, arXiv:gr-qc/0007026, for the reduction chain to the Einstein–Maxwell electrovacuum, the exhaustiveness of the quadratic family, the neutral figure-eight and toroidal singular loci, and the closed-form wave-like solution whose singular set is the neutral Lambert-function helix.
- V. V. Kassandrov, "On the Structure of General Solution of the Equations of Shear-Free Null Congruences", arXiv:gr-qc/0602046, and "On a quaternionic induced geometry with phase", arXiv:gr-qc/0602088, for the shear-free congruence structure and the induced geometry.
- V. V. Kassandrov, "A non-stationary generalization of the Kerr congruence", arXiv:0908.1123 [gr-qc] (2009), for the material recorded in *The static member, and the source's instability argument*: the virtual charge moving along the imaginary direction of complex space, $z_0=-ia+ivr'_t$, the caustic ring $z=0$, $\rho=\lvert vr'_t-a\rvert/\sqrt{1+v^2}$ collapsing at $r'_t=a/v$ and re-expanding at the speed $v/\sqrt{1+v^2}$ (the elimination recomputed here), the spinor $g=(1+iv)(x+iy)/((z-z_0)\pm r_b)$ with $r_b^2=(z-z_0)^2+\rho^2(1+v^2)$ and its eikonal and wave equations, the field components with $\tilde e=e(1+v^2)$, the time-independent elementary charge and the magnetic moment proportional to the current radius, the argument that the static congruence is unstable with respect to its scale, and the conjectured continuous transition from a naked ring to a rotating black hole and back.
- V. V. Kassandrov, "Algebrodynamics over Complex Space and Phase Extension of the Minkowski Geometry", arXiv:0907.5425 [physics.gen-ph] (2009), the survey of the programme: the explicit phase-extension invariants of the induced geometry in the real splitting $\vec z=\vec p+i\vec q$, the ensemble of duplicons as the roots of the complex null-cone equation on a complex world line, the dimerous-electron interpretation of charge and interference with the fusion condition $\Delta\alpha=2\pi N$, the random complex time and the kinematic-statistical irreversibility, and the comparison of programmes that derive or deform the Minkowski geometry cited in *Why Complexify Spacetime?*.
- V. V. Kassandrov, "Urusovskii's Geometry, Algebrodynamics and Universal Quantum-like Kinematics in Complex Space", arXiv:1209.2377 [physics.gen-ph] (2012), a short presentation of the duplicon and dimerous-electron material recorded above, with the phase relation $d\theta_{\mathrm{pha}}=ds/R$ assumed and the internal radius moved from Urusovskii's $\frac{\hbar}{c\,M}$ to $\frac{\hbar}{2\,c\,M}$ "for correspondence with quantum theory"; it reproduces the fusion condition of *The Dimerous Electron and Quantum Interference* with the same factor two, so it adds nothing here on that point. Its other half is the six-dimensional kinematics of Urusovskii, which is recorded in *The SO(4) Route to the Euclidean Frame* and not in this article, because the biquaternion algebra enters it only through the complex null condition $\sum_\mu dz_\mu^2=0$ and not through the primary equation.
- V. V. Kassandrov, "Twistor Algebraic Dynamics in Complex Space-Time and Physical Meaning of Hidden Dimensions", arXiv:gr-qc/0602064 [gr-qc] (2006), for the paper of the programme that replaces the arena by the **complex null cone of a point observer**, $\det\lVert Z-Z_{\mathrm{obs}}(\sigma)\rVert=0$, whose real dimension is six and whose topology is $\mathbb{R}_+\times S^3\times S^2$ — a 4D space, in which the proper interval is the 4D distance, plus a 2-sphere of spin directions — with the twistor index $G$ transverse to it, and with the field-preserving translations of four real parameters, a quaternionic time whose complex successor is ordered by an evolutionary curve. Verified here: the cone condition is $\lvert\operatorname{Re}Z\rvert=\lvert\operatorname{Im}Z\rvert$ with $\operatorname{Re}Z\cdot\operatorname{Im}Z=0$, so its directions are the orthonormal pairs in $\mathbb{R}^4$ and the manifold is the Stiefel manifold $V_2(\mathbb{R}^4)\cong S^3\times S^2$. Recorded as the source's and not adopted: it makes the imaginary directions an observable space-time, which *The Empirical Status of the Biquaternion Framework* declines, and it needs a four-parameter evolution and an ordering curve that the corpus does without.
- V. V. Kassandrov and I. Sh. Khasanov, "Algebraic roots of Newtonian mechanics: correlated dynamics of particles on a unique worldline", arXiv:1211.7002 [physics.gen-ph] (2013), and A. Challa, V. V. Kassandrov and N. V. Markova, "Conservative relativistic algebrodynamics induced on an implicitly defined worldline", arXiv:2104.12490 [physics.gen-ph] (2021), the two papers of a **different** sub-programme of the same authors, listed only to keep the two apart: the worldline is the root set of two polynomial equations $F(x,y,t)=0$, $G(x,y,t)=0$, the particles are the real roots and the complex-conjugate roots, a pair of roots that merge is an annihilation or a creation, and the conservation laws — the centre of mass, the total momentum and Newton's third law in the centre-of-mass frame — follow from Vieta's formulas rather than from an action; the algebra appears nowhere in either — no quaternions, no spinors, no null divisors — so they neither support nor contradict the programme recorded above, and the mass law $M=W=2p$ of the second holds only for explicitly parameterised worldlines, failing, as the paper states, for the implicit case. The 2013 paper is Galilean and leaves its relativisation open; the 2021 paper supplies it. Both share their degeneration locus with the corpus's spectral cone and neither shares its reading, the contrast being drawn in the *Limits* of *Physical Interpretation of Spectral Regularity and Degeneracy in the Biquaternion Algebra*.
- V. V. Kassandrov, I. Sh. Khasanov and N. V. Markova, "Algebraic Dynamics on a Single Worldline: Vieta Formulas and Conservation Laws", arXiv:1402.6158 [math-ph] (2014), the full account of that same sub-programme and the paper whose numbers are recorded at the end of *The Dimerous Electron and Quantum Interference*: the implicit worldline $F_A(r_x,r_y,s)=0$, the copies as its roots at fixed $s$, R-particles and C-particles, the events as multiple roots with the vanishing-Jacobian condition, the nine-root worked example with its events at $s\approx-97.3689$, $-4.0246$, $-3$, $-2.7784$, $-2.7669$ and $2932.49$ recomputed here, the Vieta route to momentum conservation and to the vanishing of the summed accelerations, and the two mis-signed printed shifts.
- V. V. Kassandrov and I. Sh. Khasanov, "The algebrodynamics: super-conservative collective dynamics on a 'Unique Worldline' and the Hubble's law", arXiv:2309.14375 [gr-qc] (2023), the sequel to arXiv:1402.6158: the worldline made implicit in three spatial unknowns and resolved by Sylvester resultants, the demonstration that any such worldline generates a null shear-free congruence through the twistor incidence, so that the light cone is induced rather than imposed and the source's earlier relativisation is corrected, and the kinematical recession of the roots with $H=1/t$.
- V. V. Kassandrov, "The Algebrodynamics: Primordial Light, Particles-Caustics and the Flow of Time", *Hypercomplex Numbers in Geometry and Physics* **1** (2004) 84, arXiv:hep-th/0312278 (the arXiv version is titled "Nature of Time and Particles-Caustics: Physical World in Algebrodynamics and in Twistor Theory"), for the Prelight flow, the caustic interpretation of particles, the duplicons, the world function and the multivaluedness of the principal field, the class-II branching condition $\Lambda=d^2\Pi/dG^2=0$, the ring family $\Pi=G^n/H$ and the Hopf-map case, the four-mode two-charge example with its cocoon and its annihilation, and the identification of the Flow of Time with the Flow of Prelight. The arXiv PDF of this paper reads cleanly, unlike that of the 2007 source paper above.
- G. C. Debney, R. P. Kerr and A. Schild, "Solutions of the Einstein and Einstein–Maxwell Equations", *Journal of Mathematical Physics* **10** (1969) 1842–1854, for the Kerr–Schild electrovacuum metric.
- E. T. Newman, "Maxwell's Equations and Complex Minkowski Space", *Journal of Mathematical Physics* **14** (1973) 102–107, and R. W. Lind and E. T. Newman, "Complexification of the Algebraically Special Gravitational Fields", *Journal of Mathematical Physics* **15** (1974) 1103–1112, for the complexified Liénard–Wiechert representation behind the duplicon picture.
- A. Sudbery, "Quaternionic Analysis", *Mathematical Proceedings of the Cambridge Philosophical Society* **85** (1979) 199–225, for the obstruction to naive quaternionic holomorphy.
- G. Scheffers, "Verallgemeinerung der Grundlagen der gewöhnlichen komplexen Funktionen", *Berichte der Sächsischen Akademie der Wissenschaften* **45** (1893) 828–842, for commutative hypercomplex differentiability.
- A. Gsponer and J.-P. Hurni, "Lanczos's Equation to Replace Dirac's Equation?", *Proceedings of the Cornelius Lanczos International Centenary Conference* (SIAM, 1994) 509–512 (arXiv:hep-ph/0112317), the second external claim to the charge-quantisation boundary, made on the linear Einstein–Mayer generalized-mass system rather than on a nonlinear equation; recorded for that contrast in *Status, Contrasts, and Boundaries*. Four pages, no derivation exhibited.
