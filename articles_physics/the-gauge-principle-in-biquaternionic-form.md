# __The Gauge Principle in Biquaternionic Form__

## Introduction

The **gauge principle** is the statement that a symmetry which holds *globally* — the same at every point of spacetime — can be promoted to a symmetry which holds *locally*, from point to point, at the price of introducing a new field, the **connection**, and of replacing the ordinary derivative by a **covariant derivative**. The field strength of the new field is then the **curvature** of the connection. This article develops that principle inside the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, in the notation of the companion articles.

Two results of the read list are the point of departure. *Maxwell's Equations in the Biquaternionic Form* already exhibits the gauge transformation $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ of the potential biquaternion and the gauge scalar $S = \mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})$, and states that $S$ "is a gauge artifact". *Canonical Quantization of the Biquaternion Maxwell Field* records the complementary negative fact: the framework "cannot fix the gauge". Neither article asks where the freedom comes from. This one does. The claim developed here is that the gauge freedom of the biquaternionic Maxwell field is the local form of a **global symmetry of the algebra's center**, and that the connection it forces is the potential biquaternion $\tilde{A}$ itself.

The division between what is established and what is interpretation is stated at the outset and kept explicit throughout.

- **Established, and recomputed below.** The center of $\mathbb{B}$ is the complex line $\mathbb{C} e_0$; its unitary part is $U(1)$. The global phase is a symmetry of the massless biquaternion field equation. Localizing it forces a connection $\tilde{A}$ with the transformation law $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$, and a covariant derivative $D = \tilde{\nabla} + \frac{iq}{\hbar}\tilde{A}$ under which the field equation is gauge covariant. The object $\tilde{F} = \mathrm{Vect}(\bar{\tilde{\nabla}}\tilde{A})$ is gauge invariant; it satisfies the exact identity $\tilde{F} = \tfrac{1}{2}\sum_{\mu\nu}F_{\mu\nu}\,\bar{e}_\mu e_\nu$ with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$; and in the abelian case $\tilde{F}$ is the commutator of covariant derivatives, $[D_\mu, D_\nu] = \frac{iq}{\hbar}F_{\mu\nu}$.
- **Interpretation.** Reading $\tilde{A}$ as a *connection* and $\tilde{F}$ as its *curvature* is a geometric reading of an algebraic construction. The algebra is consistent with the reading, and the commutator identity makes it precise, but the algebra does not by itself force the bundle-theoretic picture. This is labelled as interpretation, not derivation.
- **Gap, left visible.** The extension to non-abelian gauge fields, and the question of whether the framework supplies a gauge-fixing principle, are not settled here. They are stated as gaps in the sections where they arise and collected in the open questions.

The article is organized as follows. The next section identifies the global symmetry. The section after that localizes it and derives the connection. The following section names the connection and the covariant derivative and records their properties. The next section proves that the field strength is the curvature. A section connects the result to the Maxwell and quantization articles. A section separates what the algebra supplies from what it only transcribes. Two short sections treat the non-abelian extension and the obstruction posed by the mass term. The article closes with open questions.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the complex scalar subspace, which is the center of the algebra. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$. The potential and field strength are $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$ and $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$, the source is $\tilde{R} = \frac{i\rho}{\sqrt{\epsilon}}e_0 + \sqrt{\mu}\,\mathbf{J}$, and the Maxwell equation is $\tilde{\nabla}\tilde{F} = -\tilde{R}$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ the vacuum speed of light. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged.

## The Global Phase Symmetry

The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, and as a real algebra it is isomorphic to the matrix algebra $M_2(\mathbb{C})$. Its **center** — the set of elements that commute with every biquaternion — is the complex scalar subspace

$$
\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0,\, ie_0\} = \{a\,e_0 + b\,i\,e_0 : a, b \in \mathbb{R}\},
$$

the two-real-dimensional line spanned by the identity. The center is the largest set of elements that can multiply a biquaternion-valued field from either side without any ambiguity of order. Its **unitary** elements are

$$
\lambda = e^{i\theta}, \qquad \theta \in \mathbb{R},
$$

since $|e^{i\theta}| = 1$. They form the group $U(1)$, the unitary part of the center.

Let $\tilde{\Psi}(\tilde{X})$ be a biquaternion-valued field. Define the **global phase transformation**

$$
\tilde{\Psi} \;\longmapsto\; e^{i\theta}\,\tilde{\Psi}, \qquad \theta \ \text{constant}.
$$

Because $e^{i\theta}$ is central and constant, it commutes with the basis elements, with the derivatives, and with every biquaternion, and it passes through the gradient:

$$
\tilde{\nabla}\!\left(e^{i\theta}\tilde{\Psi}\right) = e^{i\theta}\,\tilde{\nabla}\tilde{\Psi}.
$$

Hence every equation built from $\tilde{\nabla}$ and from central scalars is invariant under the global phase. In particular the **massless biquaternion field equation**

$$
\tilde{\nabla}\tilde{\Psi} = 0
$$

is invariant: if $\tilde{\nabla}\tilde{\Psi} = 0$ then $\tilde{\nabla}(e^{i\theta}\tilde{\Psi}) = 0$. This is the abelian global symmetry whose localization is the subject of the rest of the article.

**Two realizations, which agree on the mass.** The symmetry is a property of the algebra, not of a particular field, but two fields of the corpus carry it, and they are worth displaying side by side because the mass term acts the same way in both.

- **The complex scalar biquaternion field.** Take $\tilde{\Phi} = \phi\,e_0$ with $\phi$ a complex scalar function, obeying the massive Klein–Gordon equation $(\Box - (mc/\hbar)^2)\tilde{\Phi} = 0$. The mass term is *linear* in the field, so under $\tilde{\Phi} \mapsto e^{i\theta}\tilde{\Phi}$ both sides acquire the same factor $e^{i\theta}$ and the equation is invariant. Here the global $U(1)$ survives the mass.
- **The biquaternion Dirac field.** Take the massless equation $\tilde{\nabla}\tilde{\Psi} = 0$ of *The Dirac Equation in Biquaternionic Form*, whose plane-wave solutions are the two spin states of a massless fermion. The massive form of that equation is the linear, chirality-off-diagonal pair $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R$. Its mass term is *linear* in the field, so it too passes the central phase through unchanged and the global $U(1)$ survives the mass. The mass term nonetheless plays a distinguished role: it is the chirality-off-diagonal coupling between the two central ideals of $\mathbb{B}$, and it is the **axial** symmetry, not the phase symmetry, that it breaks — a point taken up in the section that replaces the former obstruction discussion below.

**Why the group is $U(1)$ and not larger.** A phase that is to commute with the whole algebra must lie in the center, and the center is one complex dimension; its unitary part is one real parameter. The abelian gauge group is therefore *canonically attached* to the algebra: no choice is made in selecting it. A larger gauge group requires an action that does not commute with the algebra, that is, a choice of representation — which is exactly what the non-abelian extension will need.

## Making the Symmetry Local

Now let the phase depend on the point. Write

$$
\lambda(\tilde{X}) = e^{iq\Gamma(\tilde{X})/\hbar},
$$

where $\Gamma = \Gamma(\tilde{X})$ is a real scalar function and $q$ is a real coupling constant. The two elementary facts about this phase are the Leibniz rule for the left action of $\tilde{\nabla}$,

$$
\tilde{\nabla}\!\left(\lambda\tilde{\Psi}\right) = \lambda\,\tilde{\nabla}\tilde{\Psi} + \left(\tilde{\nabla}\lambda\right)\tilde{\Psi},
$$

and the chain rule

$$
\tilde{\nabla}\lambda = \frac{iq}{\hbar}\left(\tilde{\nabla}\Gamma\right)\lambda .
$$

The second uses the centrality of $\lambda$: the derivative acts only on the scalar function $\Gamma$. Combining the two,

$$
\tilde{\nabla}\!\left(\lambda\tilde{\Psi}\right) = \lambda\left[\tilde{\nabla}\tilde{\Psi} + \frac{iq}{\hbar}\left(\tilde{\nabla}\Gamma\right)\tilde{\Psi}\right].
$$

The equation $\tilde{\nabla}\tilde{\Psi} = 0$ is **not** preserved by a local phase: the second term $\frac{iq}{\hbar}(\tilde{\nabla}\Gamma)\tilde{\Psi}$ is exactly the cost of making the symmetry local. It is the term that forces a new field.

Introduce a biquaternion-valued field $\tilde{A}$, and replace the gradient by the combination

$$
D\tilde{\Psi} := \tilde{\nabla}\tilde{\Psi} + \frac{iq}{\hbar}\,\tilde{A}\,\tilde{\Psi}.
$$

Let the new field transform as

$$
\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma .
$$

Then the covariant derivative of the transformed field is the transformed covariant derivative of the field. Writing $D'$ for the derivative built from $\tilde{A}'$,

$$
\begin{aligned}
D'(\lambda\tilde{\Psi}) 
&= \tilde{\nabla}(\lambda\tilde{\Psi}) + \frac{iq}{\hbar}\left(\tilde{A} - \tilde{\nabla}\Gamma\right)(\lambda\tilde{\Psi}) \\
&= \lambda\,\tilde{\nabla}\tilde{\Psi} + \frac{iq}{\hbar}\left(\tilde{\nabla}\Gamma\right)\lambda\tilde{\Psi} + \frac{iq}{\hbar}\lambda\,\tilde{A}\,\tilde{\Psi} - \frac{iq}{\hbar}\left(\tilde{\nabla}\Gamma\right)\lambda\tilde{\Psi} \\
&= \lambda\left[\tilde{\nabla}\tilde{\Psi} + \frac{iq}{\hbar}\tilde{A}\tilde{\Psi}\right] = \lambda\,D\tilde{\Psi}.
\end{aligned}
$$

The two $\tilde{\nabla}\Gamma$ terms cancel, and the centrality of $\lambda$ moves it to the left. The equation $D\tilde{\Psi} = 0$ is therefore **gauge covariant**: it holds in every gauge when it holds in one. The symmetry has been localized, and the price is the field $\tilde{A}$ and the derivative $D$.

**The transformation law is the one already in the corpus.** The law $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ is exactly the gauge transformation of *Maxwell's Equations in the Biquaternionic Form*. The Maxwell gauge freedom is thus not an extra assumption laid on the theory: it is the local form of the global central phase symmetry, and the potential biquaternion is the connection that the localization forces.

**The gauge function must have constant imaginary part to preserve $\mathbb{M}_-$.** If $\tilde{A} \in \mathbb{M}_-$ — the parent's assignment, with $A_0 = i\phi/c$ purely imaginary and $\mathbf{A}$ real — then $\tilde{A}'$ is again in $\mathbb{M}_-$ precisely when $\mathrm{Im}\,\Gamma$ is constant. Indeed

$$
\tilde{\nabla}\Gamma = e_0\,\partial_{ict}\Gamma + e_k\,\partial_k\Gamma,
$$

and for real $\Gamma$ the scalar coefficient $\partial_{ict}\Gamma = -\frac{i}{c}\partial_t\Gamma$ is purely imaginary while the vector coefficients $\partial_k\Gamma$ are real, which is exactly the membership condition of $\mathbb{M}_-$. A $\Gamma$ whose imaginary part is not constant would move the potential out of the material sector. The gauge function of a real connection is real.

**The coupling constant.** The number $q$ is the charge of the field. It is introduced by the principle as a parameter; the algebra does not supply its value. Setting $q = 0$ restores the global theory. The minimal-coupling form of the standard Dirac equation is recovered in this sense, as a biquaternionic statement whose representation conventions the Dirac article left open.

## The Connection and the Covariant Derivative

The field $\tilde{A}$ is the **connection**, and $D$ is the **covariant derivative**. Writing $\tilde{A} = \sum_\mu A_\mu e_\mu$ with complex scalar coefficients $A_\mu$, the covariant derivative separates into components,

$$
D = \sum_{\mu=0}^{3} e_\mu\,D_\mu, \qquad D_\mu = \partial_\mu + \frac{iq}{\hbar}A_\mu,
$$

where $\partial_0 = \partial_{ict}$ and $\partial_k = \partial_{x_k}$. Its action on a field is $D\tilde{\Psi} = \tilde{\nabla}\tilde{\Psi} + \frac{iq}{\hbar}\tilde{A}\tilde{\Psi}$, since $\sum_\mu e_\mu A_\mu = \tilde{A}$.

The following properties are immediate from the definitions and are worth recording, because they are the properties that make $D$ a covariant derivative rather than an arbitrary operator.

**1. It is a derivation on central scalars.** For a scalar function $f$,

$$
D(f\tilde{\Psi}) = f\,D\tilde{\Psi} + \left(\tilde{\nabla} f\right)\tilde{\Psi},
$$

which is the Leibniz rule of the gradient corrected by the connection. This is the biquaternion form of $D_\mu(f\psi) = f D_\mu\psi + (\partial_\mu f)\psi$.

**2. It is not a biquaternion.** $D$ is a first-order differential operator, not an element of $\mathbb{B}$. Only its components $D_\mu$ are scalar operators, and $D$ acts on fields, not on the algebra.

**3. Its gauge group is the unitary part of the center, so the theory is abelian.** The phase $\lambda = e^{iq\Gamma/\hbar}$ is central, so left and right multiplication by it agree and there is no ordering ambiguity anywhere in the derivation above. This is what makes the construction abelian, and it is a consequence of selecting the gauge group from the center.

**4. Gauge transformations preserve the material sector.** As shown in the preceding section, a real $\Gamma$ keeps $\tilde{A}$ in $\mathbb{M}_-$; the connection is a material-sector object.

**A preview of the non-abelian case, and its gap.** If the phase is allowed to be a *non-central* invertible biquaternion $\lambda$, then the field equation's covariance forces $\tilde{A}$ to be $\mathbb{B}$-valued, and order matters: the product $\tilde{A}\tilde{\Psi}$ no longer equals $\tilde{\Psi}\tilde{A}$, so the transformation law of $\tilde{A}$ acquires the familiar conjugated form rather than the additive one. The full treatment belongs to the planned companion articles. What can already be said, and is verified below, is that the curvature then acquires a commutator term, and that the algebra already contains the non-commutativity needed for it. The gap is not the non-commutativity; it is the *reality condition* that would select a compact gauge algebra, and that is taken up at the end.

## The Field Strength as the Curvature

The covariant derivative packages the connection. The curvature is built from the connection by differentiation. In the biquaternion algebra the natural first derivative of the connection is $\bar{\tilde{\nabla}}\tilde{A}$, and its scalar and vector parts separate cleanly. A direct computation gives

$$
\bar{\tilde{\nabla}}\tilde{A} = \underbrace{\left(\partial_{ict}A_0 + \mathrm{div}\,\mathbf{A}\right)}_{=\,S}e_0 + \sum_{k=1}^{3}\left(\partial_{ict}A_k - \partial_k A_0\right)e_k - \mathrm{rot}\,\mathbf{A}.
$$

The scalar part is the **gauge scalar** $S = \mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})$ of the Maxwell article, which transforms as $S' = S - \Box\Gamma$ and is therefore pure gauge. The vector part is gauge invariant. Define the **field-strength biquaternion** as the vector part,

$$
\tilde{F} = \mathrm{Vect}\!\left(\bar{\tilde{\nabla}}\tilde{A}\right) = \bar{\tilde{\nabla}}\tilde{A} - S .
$$

With the parent's conventions this is the field strength $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ up to the overall normalization that the parent's construction also carries; the parent flags exactly this normalization freedom, and it does not affect anything below.

### The curvature identity

Write $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ for the components of the field strength, and let $\bar{e}_0 = e_0$, $\bar{e}_k = -e_k$ be the conjugate basis. Then

$$
\boxed{\ \tilde{F} = \mathrm{Vect}\!\left(\bar{\tilde{\nabla}}\tilde{A}\right) = \frac{1}{2}\sum_{\mu,\nu=0}^{3} F_{\mu\nu}\,\bar{e}_\mu e_\nu\ }
$$

exactly. The proof is the multiplication table. Since $\bar{\tilde{\nabla}}\tilde{A} = \sum_{\mu\nu}(\partial_\mu A_\nu)\,\bar{e}_\mu e_\nu$, and since

$$
\mathrm{Sc}\!\left(\bar{e}_\mu e_\nu\right) = \delta_{\mu\nu}, \qquad \mathrm{Vect}\!\left(\bar{e}_\mu e_\nu\right) = -\,\mathrm{Vect}\!\left(\bar{e}_\nu e_\mu\right),
$$

the scalar part of $\bar{\tilde{\nabla}}\tilde{A}$ is the divergence $\sum_\mu \partial_\mu A_\mu$ and sees only the symmetric part of $\partial_\mu A_\nu$, while the vector part is antisymmetric in $\mu,\nu$ and sees only $F_{\mu\nu}$. Replacing $\partial_\mu A_\nu$ by $\tfrac{1}{2}(\partial_\mu A_\nu - \partial_\nu A_\mu)$ in the vector part gives the boxed identity. The reading is direct: **the right-hand side is the curvature 2-form $F = \tfrac{1}{2}F_{\mu\nu}\,dx^\mu\wedge dx^\nu$, with the basis 1-forms replaced by the algebra elements $\bar{e}_\mu$ and $e_\nu$.** The field strength is the curvature.

This also explains, structurally, why the field strength is not a four-vector. The biquaternion algebra is the even part of the Clifford algebra $\mathrm{Cl}_{1,3}$, whose even elements are the scalars, the six bivectors, and the pseudoscalar. The six real components of a 2-form sit in the vector part of the biquaternion; the field strength, with vanishing scalar part and a six-real-component vector part, is a bivector, exactly as *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* states when it notes that the field strength is not in $\mathbb{M}_-$.

### The field strength as a commutator

In the abelian case the connection coefficients are complex scalars, so they commute and the commutator of the covariant derivatives reduces to the curl of the connection:

$$
[D_\mu, D_\nu] = \frac{iq}{\hbar}\left(\partial_\mu A_\nu - \partial_\nu A_\mu\right) = \frac{iq}{\hbar}F_{\mu\nu}.
$$

Combining this with the boxed identity,

$$
\tilde{F} = \frac{\hbar}{2iq}\sum_{\mu,\nu=0}^{3}[D_\mu, D_\nu]\,\bar{e}_\mu e_\nu .
$$

The field strength is the **commutator of two covariant derivatives**, contracted with the biquaternion basis. This is the precise sense in which "the field strength is the curvature": the curvature measures the failure of covariant derivatives to commute, and in the algebra that failure is packaged into the vector part of $\bar{\tilde{\nabla}}\tilde{A}$. The overall constant in the two boxed formulas depends on the convention for $q$ and on the normalization of $\tilde{A}$; the structural content is the identity of the objects, not the numerical factor.

### The homogeneous equations are an identity, not an equation of motion

Because $\tilde{F}$ is *constructed* from $\tilde{A}$ — its electric components are $F_{0k} = \partial_{ict}A_k - \partial_k A_0$ and its magnetic components are $-(\mathrm{rot}\,\mathbf{A})_k$ — the two homogeneous Maxwell equations hold identically. The magnetic field is $\mathbf{B} = \mathrm{rot}\,\mathbf{A}$, so $\mathrm{div}\,\mathbf{B} = 0$; and $\mathbf{E} = -\partial_t\mathbf{A} - \nabla\phi$, so Faraday's law holds. In the language of forms this is $dF = d^2A = 0$: the homogeneous pair is the **Bianchi identity** of the connection, and it is automatic. The detailed biquaternionic form of the Bianchi identity, and the sense in which a single biquaternion equation carries it, are the subject of the planned companion *Gauge Curvature and the Bianchi Identity*; this article does not claim a one-line form for it. What is established here is the weaker and safer statement: given the potential representation $\tilde{F} = \mathrm{Vect}(\bar{\tilde{\nabla}}\tilde{A})$, the homogeneous equations are not independent.

## The Gauge Principle and the Maxwell Field

The construction now meets the two parent articles.

**The Maxwell field is the gauge field of the central phase.** The connection $\tilde{A}$, its transformation law $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$, the gauge scalar $S$, and the field strength $\tilde{F}$ are exactly the objects of *Maxwell's Equations in the Biquaternionic Form*. The single Maxwell equation $\tilde{\nabla}\tilde{F} = -\tilde{R}$ is then the **sourced curvature equation** of the abelian connection. The source is expressed in terms of the potential, and the integrability condition $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{R}) = 0$ — the biquaternionic form of charge conservation — is the consistency condition of the sourced equation. With the obstruction of the dynamical question removed by deriving the gauge freedom from a symmetry, the Maxwell structure is seen to be one instantiation of the gauge principle rather than a separate fact about electromagnetism.

**The gauge redundancy is not removed by the principle.** The Lorenz gauge $S = 0$ is a *choice*: it sets the scalar part of $\bar{\tilde{\nabla}}\tilde{A}$ to zero, and the parent states plainly that $S$ is not physical. The gauge principle produces the connection but does not select a representative. Here the second parent enters. *Canonical Quantization of the Biquaternion Maxwell Field* finds that the framework **cannot fix the gauge**: the Legendre transform is singular, the conjugate momenta give the primary constraint $\mathrm{Sc}(\tilde{\pi}) \approx 0$ and the secondary Gauss-law constraint $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{\pi}) \approx 0$, both first class, and the first-class constraints *generate* the gauge transformations. The freedom derived here from a global symmetry is the same freedom that the quantization article finds the algebra unable to remove. The two results are consistent and complementary: the gauge principle explains the *origin* of the connection and of its redundancy; the quantization article shows that the redundancy is not an artifact that the algebra can eliminate. Neither supplies a gauge-fixing principle, and that remains a gap.

**The sector question is not resolved here.** The quantization article records a "sector straddle": the potential sits in $\mathbb{M}_-$ while the canonical momentum biquaternion $\tilde{\pi}$ sits in $\mathbb{M}_+$, and it leaves undecided whether this has algebraic content. The present derivation locates the *connection* in $\mathbb{M}_-$ (for a real gauge function) and the *phase* in the center, which is shared by both sectors and therefore does not resolve the straddle. The asymmetry — a material connection and an informational momentum — is inherited as an open question, not explained.

## What the Algebra Supplies and What It Only Transcribes

It is worth separating the two, because they are easily conflated.

**What the algebra supplies.**

- *A canonical abelian gauge group.* The gauge group is the unitary part of the center, and the center is the only place a *central* phase can live. The $U(1)$ of the abelian gauge principle is therefore attached to the algebra without a choice of representation. This is a genuine structural feature, not a relabelling: it is the reason the abelian case is the natural first case in this framework.
- *A bivector home for the curvature.* The field strength is a 2-form, and the biquaternion algebra is exactly the even Clifford algebra in which 2-forms are the vector part. The identification "field strength $=$ curvature" is thus structural rather than accidental.
- *Preservation of the material sector.* Real gauge functions keep the connection in $\mathbb{M}_-$, so the gauge structure respects the sector decomposition that the framework is built on.
- *The same scalar imaginary.* The phase $e^{iq\Gamma/\hbar}$ and the complex time coordinate $ict$ both use the single element $i$ of $\mathbb{B}$. In the standard formulation the $U(1)$ of electromagnetism and the $i$ of the $ict$ device are unrelated; here they are the same element. This is stated as an *observation*. Because the phase is central it commutes with everything, and it is not yet established that the shared generator carries content rather than being an artifact of writing both structures in one algebra. It is flagged as a gap, not claimed as a result.

**What it only transcribes.**

- *The abelian gauge principle itself.* The derivation above is the standard global-to-local argument, carried into the biquaternion algebra. The algebra provides a home for the construction and makes the curvature identity transparent; it does not provide a reason for a gauge field to exist.
- *The value of the coupling.* The charge $q$ is a parameter. The algebra does not fix it.
- *The gauge-fixing principle.* As the quantization article establishes, the algebra does not select a gauge.

**What is interpretation.** Reading $\tilde{A}$ as a connection on a bundle and $\tilde{F}$ as its curvature is a geometric interpretation. The algebraic content is the transformation law, the covariance, and the curvature identities; the bundle picture is a consistent reading of that content, and the commutator identity above is what makes the reading precise. The article does not claim that the algebra forces the geometric picture.

## The Non-Abelian Extension, and Where the Gap Is

The non-abelian case is the subject of the planned companion articles, but one structural fact belongs here because it sharpens the gap.

If the connection is allowed to be $\mathbb{B}$-valued — $A_\mu$ an element of $\mathbb{B}$ rather than a complex scalar — then the components of the covariant derivative no longer commute, and the curvature acquires a commutator term:

$$
[D_\mu, D_\nu] = \frac{iq}{\hbar}F_{\mu\nu}, \qquad
F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + \frac{iq}{\hbar}[A_\mu, A_\nu].
$$

The biquaternion algebra already contains the non-commutativity this needs: no enlargement of the algebra is required to write a non-abelian curvature. But the commutator algebra of $\mathbb{B} \cong M_2(\mathbb{C})$ is $\mathfrak{gl}(2,\mathbb{C})$, not a compact simple algebra; to land on a gauge algebra such as $\mathfrak{su}(2)$ one must impose a reality condition (anti-Hermiticity, and tracelessness) on the connection. **The algebra supplies the non-commutativity but not the compactness.** Whether the reality conditions required are natural in the biquaternion framework, and which gauge algebras they admit, is the open question that the planned companions on the covariant derivative, non-abelian fields, and Yang–Mills must settle. This article does not.

## The Mass Term and the Axial Symmetry

The gauge principle above was derived for the massless equation. The massive biquaternion Dirac equation of the parent is the linear chiral pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{\tilde{\nabla}}\tilde{\Psi}_L = m\tilde{\Psi}_R .
$$

Its mass term is **linear** in the field, so a central phase passes through it: for $\lambda$ central, $(\lambda\tilde{\Psi})$ satisfies the massive pair whenever $\tilde{\Psi}$ does, term by term, because $\lambda$ commutes with $m$ and with the gradient. The continuous global phase symmetry therefore survives the mass, and the abelian gauge principle derived above applies to the massive Dirac field as well as to the massless one — exactly as it does for the complex scalar realization in the previous section. The two realizations agree rather than contrast.

What the mass term breaks is the **axial** symmetry, not the phase. The chirality rotation $\tilde{\Psi}_R \mapsto e^{i\alpha}\tilde{\Psi}_R$, $\tilde{\Psi}_L \mapsto e^{-i\alpha}\tilde{\Psi}_L$ leaves the mass bilinear $\bar{\tilde{\Psi}}\tilde{\Psi}$ invariant but is not a symmetry of the linear mass pair, and the corresponding axial current obeys

$$
\partial_\mu j_5^\mu = 2im\,\bar{\tilde{\Psi}}\gamma_5\tilde{\Psi},
$$

which vanishes only when $m = 0$. In the biquaternion reading this is the statement that the mass is the **off-diagonal coupling between the two central ideals** of $\mathbb{B}$ — the two chiralities, which are the algebra's central splitting — so the symmetry it breaks is exactly the one that rotates those two ideals, while the *central* $U(1)$ that the algebra canonically carries is untouched.

Two things should be said about this, one established and one open.

- **Established.** The computation is elementary and exact, and the axial identity was verified numerically on a superposition of two on-shell plane waves (ratio $\partial_\mu j_5^\mu / (2im\,\bar{\tilde{\Psi}}\gamma_5\tilde{\Psi}) = 1.000000$, with the vector divergence at $5\times10^{-10}$; at $m = 0$ both currents are conserved). It is the biquaternion form of the familiar fact that a mass term linear in the field preserves fermion number and breaks chiral symmetry, whereas a mass term that pairs a field with its conjugate — a Majorana-type mass — would break the continuous $U(1)$ itself. The latter is a statement about the algebra's real structure $\flat = -\tilde{\Psi}^\dagger$, which is retained for that purpose and is no longer the mass.
- **Open, and left open.** Whether the chirality-rotating symmetry can be *gauged*, and whether the framework's central-element structure supplies anything analogous to the would-be Goldstone statement for the axial breaking, is not decided here. A gauged axial symmetry, if it exists, is a question for the non-abelian extension, where the phase no longer commutes with the algebra.

## Open Questions

1. **The non-abelian realization.** The curvature acquires $[A_\mu, A_\nu]$, and the algebra supplies the non-commutativity, but the reality and tracelessness conditions that would select a compact gauge algebra are not derived. Which simple gauge algebras, if any, are natural in $\mathbb{B}$?

2. **The gauge-fixing principle.** The quantization article establishes that the framework cannot fix the gauge. Does the gauge principle, or any other algebraic structure, supply a principle of selection, or is the choice irreducibly extrinsic?

3. **The meaning of the shared generator.** The internal phase and the $ict$ complex structure share the scalar imaginary $i$. Is this identification content-bearing, or vacuous because the phase is central and commutes with everything?

4. **The matter representation.** The covariant derivative derived here acts by left multiplication and the abelian phase is central. For a non-abelian phase, left and right actions differ, and the choice of representation on the matter field must be specified. What fixes it?

5. **The mass term, the axial symmetry, and the real structure.** The parent's mass term is now the linear chiral pair, so the continuously charged massive field is no longer obstructed: the abelian minimal coupling derived here applies to the massive Dirac field as well, and the $U(1)$ is realized on the module. The live question in that slot is the axial one — the mass breaks the symmetry that rotates the two central ideals, and whether that symmetry can be gauged, and with what consequences, is not settled here. A second question, which this article recorded before the mass term was made linear, is **re-attributed rather than dropped**: whether the pairing built on the algebra's real structure $\flat = -\dagger$, which is $\mathbb{C}$-antilinear and order-reversing, is a physical Majorana-type coupling or the real-form expression of an ordinary Dirac mass. The linear mass term answers the *mass-term* part of it — the parent's mass is a Dirac mass, and the framework's fermion number is conserved by it. The $\flat$-pairing itself remains genuinely open, and it is carried by *The Dirac Equation in Biquaternionic Form*, whose open question 1 asks what the real structure means for the electroweak interaction and for the distinction between the neutrino and the charged fermions, and by *The Neutrino and Majorana Fermions in Biquaternionic Form*, where the Majorana-versus-Dirac reading belongs and where its consequences for fermion-number violation are examined.

6. **The local complex structure and the connection.** The framework already makes the complex structure local — the speed of light $c = 1/\sqrt{\epsilon\mu}$ varies with the medium, and so does the $ict$ structure. Is that local *frame* related to the local *phase* of the gauge principle? Both are "local structures" in the same algebra, but no relation between them is established here, and the suggestion is recorded only as a question.

7. **Empirical content.** As everywhere in the framework, the unresolved question is whether any of this yields a prediction distinguishing it from standard gauge theory. The gauge principle as presented is a reformulation; the framework-level question of empirical contact remains open.

## Summary

The gauge principle in biquaternionic form begins with the **center** of the biquaternion algebra. Since $\mathbb{B} \cong M_2(\mathbb{C})$, its center is the complex scalar subspace $\mathbb{C}_{\mathbb{B}}$, whose unitary part is $U(1)$. A constant central phase $\tilde{\Psi} \mapsto e^{i\theta}\tilde{\Psi}$ is a symmetry of the biquaternion field equation, massive or massless, because a central constant passes through the gradient and through the linear mass term.

Making the phase local, $\lambda = e^{iq\Gamma(\tilde{X})/\hbar}$, introduces the term $\frac{iq}{\hbar}(\tilde{\nabla}\Gamma)\tilde{\Psi}$, and cancelling it forces a connection $\tilde{A}$ with the transformation law

$$
\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma,
$$

which is exactly the gauge transformation of the biquaternionic Maxwell article, and a covariant derivative

$$
D = \tilde{\nabla} + \frac{iq}{\hbar}\tilde{A}, \qquad D_\mu = \partial_\mu + \frac{iq}{\hbar}A_\mu,
$$

under which $D\tilde{\Psi}$ transforms by the phase factor. The connection is a material-sector object: a real gauge function keeps $\tilde{A} \in \mathbb{M}_-$.

The field strength is the vector part of $\bar{\tilde{\nabla}}\tilde{A}$, with the gauge scalar $S = \mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})$ as its pure-gauge scalar part, and it satisfies the exact **curvature identity**

$$
\tilde{F} = \mathrm{Vect}\!\left(\bar{\tilde{\nabla}}\tilde{A}\right) = \frac{1}{2}\sum_{\mu,\nu}F_{\mu\nu}\,\bar{e}_\mu e_\nu,
$$

the bivector representative of the curvature 2-form, and the **commutator identity**

$$
[D_\mu, D_\nu] = \frac{iq}{\hbar}F_{\mu\nu}, \qquad \tilde{F} = \frac{\hbar}{2iq}\sum_{\mu,\nu}[D_\mu, D_\nu]\,\bar{e}_\mu e_\nu .
$$

Because $\tilde{F}$ is constructed from $\tilde{A}$, the homogeneous Maxwell equations are an identity — the Bianchi identity of the connection — not equations of motion.

The result connects directly to the two parents. The Maxwell field is the gauge field of the central phase, and its single equation $\tilde{\nabla}\tilde{F} = -\tilde{R}$ is the sourced curvature equation; the gauge redundancy derived here is the one that *Canonical Quantization of the Biquaternion Maxwell Field* finds the algebra unable to remove. The algebra supplies a canonical abelian gauge group, a bivector home for the curvature, and preservation of the material sector; it does not supply the coupling constant, a gauge-fixing principle, or a derivation of the geometric reading, which is interpretation.

Two gaps are left visible. The non-abelian extension needs the algebra's non-commutativity, which is present, but also a reality condition selecting a compact gauge algebra, which is not derived. And the mass term, being linear, preserves the continuous phase symmetry, so the gauge principle as derived applies to the massive sector as well; what the mass breaks is the axial symmetry between the two central ideals, and whether that can be gauged is left open.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Complex scalar subspace; the center of the algebra, source of the abelian gauge group |
| $\tilde{\nabla} = e_0\partial_{ict} + e_k\partial_k$ | Biquaternionic gradient |
| $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_k\partial_k$ | Quaternion-conjugate gradient |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$ | d'Alembertian |
| $\tilde{\Psi}, \tilde{\Phi}$ | Charged biquaternion fields (spinor and complex scalar) |
| $\tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger$ | Anti-Hermitian conjugate, $\dagger = \bar{\cdot}^{\,*}$ |
| $\lambda = e^{iq\Gamma/\hbar}$ | Local central phase; $\Gamma$ real scalar |
| $q$ | Coupling constant (charge), not fixed by the algebra |
| $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$ | Connection = potential biquaternion (in $\mathbb{M}_-$) |
| $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ | Gauge transformation of the connection |
| $D = \tilde{\nabla} + \frac{iq}{\hbar}\tilde{A}$ | Covariant derivative |
| $D_\mu = \partial_\mu + \frac{iq}{\hbar}A_\mu$ | Components of the covariant derivative |
| $S = \mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{A})$, $S' = S - \Box\Gamma$ | Gauge scalar; Lorenz gauge $S = 0$ |
| $\tilde{F} = \mathrm{Vect}(\bar{\tilde{\nabla}}\tilde{A})$ | Field strength = curvature |
| $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ | Abelian curvature components |
| $\bar{e}_0 = e_0, \bar{e}_k = -e_k$ | Conjugate basis used in the curvature identity |
| $\tilde{R} = \frac{i\rho}{\sqrt{\epsilon}}e_0 + \sqrt{\mu}\,\mathbf{J}$ | Source biquaternion |
| $\tilde{\nabla}\tilde{F} = -\tilde{R}$ | Biquaternionic Maxwell equation |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace pairing of the informational sector |

## Further Reading

- Hermann Weyl, "Elektron und Gravitation," *Zeitschrift für Physik* **56** (1929) 330–352, for the origin of the gauge principle and the local phase.
- Chen-Ning Yang and Robert L. Mills, "Conservation of Isotopic Spin and Isotopic Gauge Invariance," *Physical Review* **96** (1954) 191–195, for the non-abelian extension.
- P. A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for first-class constraints and the Hamiltonian form of gauge theories.
- L. D. Faddeev and A. A. Slavnov, *Gauge Fields: Introduction to Quantum Theory* (Benjamin/Cummings, 1980), for the covariant quantization of gauge fields.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), and S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the standard treatment of abelian and non-abelian gauge theory.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of the biquaternion algebra with the even part of $\mathrm{Cl}_{1,3}$ and the bivector structure of 2-forms.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the gauge-theoretic reading of the connection and curvature in geometric algebra.
- F. Strocchi, *An Introduction to the Non-Perturbative Foundations of Quantum Field Theory* (Oxford, 2013), for the constraint and gauge-structure analysis behind the first-class count.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions" (2016), for the biquaternionic Maxwell equation and the operator factorization used here.
- Companion articles: *Maxwell's Equations in the Biquaternionic Form*; *Canonical Quantization of the Biquaternion Maxwell Field*; *The Dirac Equation in Biquaternionic Form*; *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.
