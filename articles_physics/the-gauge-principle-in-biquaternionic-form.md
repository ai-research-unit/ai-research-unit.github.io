# __The Gauge Principle in Biquaternionic Form__

## Introduction

The **gauge principle** is the statement that a symmetry which holds *globally* — the same at every point of spacetime — can be promoted to a symmetry which holds *locally*, from point to point, at the price of introducing a new field, the **connection**, and of replacing the ordinary derivative by a **covariant derivative**. The field strength of the new field is then the **curvature** of the connection. This article develops that principle inside the biquaternion algebra $\mathbb{B}$ of *Algebra and Element Conventions*, in the notation of the companion articles.

**The article writes its operators as actions.** Where the corpus names an operator, the page writes what the operator does to an element: the action $\tilde Q\mapsto a\tilde Q b$, a product of two elements of $\mathbb{B}$, and no operator symbol stands between the reader and that product. Two names are kept. The first is the covariant derivative $D$, whose action is displayed once and used thereafter. The second is the **Dirac adjoint** $\bar{\tilde\Psi}=\tilde{\Psi}^{*}i\vec e_x$, which is kept because it is a pairing of two states and not an action on one. The cells of the frame appear, with their frame names, only in §*The Legacy Pauli Gamma Formulation*; the reasons for writing the action rather than the cell are those of *Why AXF Matrices instead of Pauli and Gamma Matrices*.

**Two Dirac equations, not one.** The corpus carries the one-sided chiral pair, two elements $\tilde\Psi_L$ and $\tilde\Psi_R$ with one equation each, and the two-sided single equation on the algebra. The pair writes the value of the subscript as a splitting of the field; the two-sided equation writes it as a multiplication on the right, and its mass term carries a coefficient conjugation. The subscript takes its two values from *Special Element Conventions*, §*The Chirality Convention*: $L$ for the value minus one of the chirality cell, $R$ for the value plus one. This article uses the pair for the gauging and records the two-sided form in the section on the mass term, where the two are set side by side. They are related by the real-linear dictionary $A$ of *The Dirac Equation in Biquaternionic Form* and are not the same operator.

Two results in the corpus are the point of departure. *Maxwell's Equations in the Biquaternionic Formulation* already exhibits the gauge transformation $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$ of the potential biquaternion and the gauge scalar $S = \mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$, and states that $S$ "is a gauge artifact". *Canonical Quantization of the Biquaternion Maxwell Field* records the complementary negative fact: the framework "cannot fix the gauge". Neither article asks where the freedom comes from. This one does. The claim developed here is that the gauge freedom of the biquaternionic Maxwell field is the local form of a **global symmetry of the algebra's centre**, and that the connection it forces is the potential biquaternion $\tilde{A}$ itself.

The division between what is established and what is interpretation is stated at the outset and kept explicit throughout.

- **Established, and recomputed below.** The centre of $\mathbb{B}$ is the complex scalar subspace $\mathbb{C}_{\mathbb{B}}$ of *Algebra and Element Conventions*; its $*$-unitary part is $\mathrm{U}(1)$. The global phase is a symmetry of the one-sided chiral pair, massive or massless. Localizing it forces a connection $\tilde{A}$ with the transformation law $\tilde A_2=\tilde A-\tilde\nabla\Gamma$, and a covariant derivative whose action is $\tilde\Psi\mapsto\tilde\nabla\tilde\Psi+\frac{iϙ}{\hbar}\tilde{A}\tilde\Psi$, under which the field equation is gauge covariant. The element $\tilde{F} = \mathrm{Vect}(\tilde{\nabla}^{\natural}\tilde{A})$ is gauge invariant; it satisfies the exact identity $\tilde{F} = \tfrac{1}{2}\sum_{\mu\nu}F_{\mu\nu}\,\bar{e}_\mu e_\nu$ with $F_{\mu\nu} = \partial/\partial Q_\mu A_\nu - \partial/\partial Q_\nu A_\mu$; and in the abelian case $\tilde{F}$ is the commutator of the components of $D$, $[D_\mu, D_\nu] = \frac{iϙ}{\hbar}F_{\mu\nu}$.
- **Interpretation.** Reading $\tilde{A}$ as a *connection* and $\tilde{F}$ as its *curvature* is a geometric interpretation of an algebraic construction. The algebra is consistent with the interpretation, and the commutator identity makes it precise, but the algebra does not by itself force the bundle-theoretic picture. This is labelled as interpretation, not derivation.
- **Gap, left visible.** The extension to non-abelian gauge fields, and the question of whether the framework supplies a gauge-fixing principle, are not settled here. They are stated as gaps in the sections where they arise and collected in the open questions.

The article is organized as follows. The next section identifies the global symmetry. The section after that localizes it and derives the connection. The following section names the connection and the covariant derivative and records their properties. The next section proves that the field strength is the curvature. A section connects the result to the Maxwell and quantization articles. A section separates what the algebra supplies from what it only transcribes. Two short sections treat the non-abelian extension and the axial question raised by the mass term, and one records an external, frame-free construction that reaches the same local $\mathrm{U}(1)$. The article closes with the open questions, the Gamma Formulation, the summary, the notation table and the literature.

## The Global Phase Symmetry

The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$. Its **centre** — the set of elements that commute with every biquaternion — is the complex scalar subspace $\mathbb{C}_{\mathbb{B}}$ of *Algebra and Element Conventions*: the complex line through the identity $e_t$, with $i$ the single scalar imaginary of the algebra, $i^2=-1$. The centre is the largest set of elements that can multiply a biquaternion-valued field from either side without any ambiguity of order. Its **$*$-unitary** elements are the phases

$$
\lambda = \exp(i\theta), \qquad \theta \in \mathbb{R},
$$

since $|\exp(i\theta)| = 1$. They form the group $\mathrm{U}(1)$, the $*$-unitary part of the centre.

Let $\tilde{\Psi}(\tilde{Q})$ be a biquaternion-valued field. The **global phase transformation** is

$$
\tilde{\Psi} \;\longmapsto\; \lambda\,\tilde{\Psi}, \qquad \lambda=\exp(i\theta),\quad \theta \ \text{constant}.
$$

Because $\lambda$ is central and constant it passes through the gradient, and the product rule for the gradient gives

$$
\tilde{\nabla}(\lambda\tilde{\Psi})=(\tilde{\nabla}\lambda)\tilde{\Psi}+\lambda\,\tilde{\nabla}\tilde{\Psi}
=\lambda\,\tilde{\nabla}\tilde{\Psi},
\qquad \tilde{\nabla}\lambda = 0 .
$$

Hence every equation built from $\tilde{\nabla}$ and from central scalars is invariant under the global phase. In particular the **massless biquaternion field equation**

$$
\tilde{\nabla}\tilde{\Psi} = 0
$$

is invariant: if $\tilde{\nabla}\tilde{\Psi} = 0$ then $\tilde{\nabla}(\lambda\tilde{\Psi}) = 0$. This is the abelian global symmetry whose localization is the subject of the rest of the article.

**Two realizations, which agree on the mass.** The symmetry is a property of the algebra, not of a particular field, but two fields of the corpus carry it, and they are worth displaying side by side because the mass term acts the same way in both.

- **The complex scalar biquaternion field.** Take $\tilde{\Phi} = \phi\,e_t$ with $\phi$ a complex scalar function, obeying the massive Klein–Gordon equation $(\Box - (mc/\hbar)^2)\tilde{\Phi} = 0$. The mass term is *linear* in the field, so under $\tilde{\Phi} \mapsto \lambda\tilde{\Phi}$ both sides acquire the same factor $\lambda$ and the equation is invariant. Here the global $\mathrm{U}(1)$ survives the mass.
- **The biquaternion Dirac field.** Take the massless chiral pair of *The Dirac Equation in Biquaternionic Form*, whose two lines are the two Weyl equations, $\tilde\nabla\tilde\Psi_R=0$ and $\tilde\nabla^\natural\tilde\Psi_L=0$. Each line carries one value of the subscript of a massless fermion; the full massless field is the pair, not either line alone. The massive form is the linear, off-diagonal pair $\tilde\nabla\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde\nabla^\natural\tilde{\Psi}_L = m\tilde{\Psi}_R$. Its mass term is *linear* in the field, so it too passes the central phase through unchanged and the global $\mathrm{U}(1)$ survives the mass. The mass term nonetheless plays a distinguished role: it couples the two values of the subscript, and it is the **axial** symmetry, not the phase symmetry, that it breaks — a point taken up in §*The Mass Term and the Axial Symmetry* below. The two-sided form of the same physics is recorded there as well, because it is the form in which the mass is a multiplication on the right rather than a pairing.

**Why the group is $\mathrm{U}(1)$ and not larger.** A phase that is to commute with the whole algebra must lie in the centre, and the centre is one complex dimension; its $*$-unitary part is one real parameter. The abelian gauge group is therefore *canonically attached* to the algebra: no choice is made in selecting it. A larger gauge group requires an action that does not commute with the algebra, that is, a choice of representation — which is exactly what the non-abelian extension will need.

## Making the Symmetry Local

Now let the phase depend on the point. Write

$$
\lambda(\tilde{Q}) = \exp(iϙ\Gamma(\tilde{Q})/\hbar),
$$

where $\Gamma = \Gamma(\tilde{Q})$ is a real scalar function and $ϙ$ is a real coupling constant. Two elementary facts govern it. The product rule for the gradient, applied to a field,

$$
\tilde{\nabla}(\lambda\tilde{\Psi})=(\tilde{\nabla}\lambda)\tilde{\Psi}+\lambda\,\tilde{\nabla}\tilde{\Psi},
$$

and the chain rule

$$
\tilde{\nabla}\lambda = \frac{iϙ}{\hbar}\,\lambda\,\tilde{\nabla}\Gamma .
$$

The second uses the centrality of $\lambda$: the derivative acts only on the scalar function $\Gamma$, and $\lambda$ passes through $\tilde{\nabla}\Gamma$. Combining the two,

$$
\tilde{\nabla}(\lambda\tilde{\Psi})
=\lambda\,\tilde{\nabla}\tilde{\Psi}+\frac{iϙ}{\hbar}\,\lambda\,(\tilde{\nabla}\Gamma)\tilde{\Psi}.
$$

The equation $\tilde{\nabla}\tilde{\Psi} = 0$ is **not** preserved by a local phase: the second term is exactly the cost of making the symmetry local. It is the term that forces a new field.

Introduce a biquaternion-valued field $\tilde{A}$, and replace the gradient by the **covariant derivative**

$$
D\tilde{\Psi} := \tilde{\nabla}\tilde{\Psi}+\frac{iϙ}{\hbar}\,\tilde{A}\tilde{\Psi},
$$

the multiplication by $\tilde{A}$ being on the left. Let the new field transform as

$$
\boxed{\;\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma\;}.
$$

Then the covariant derivative built from the transformed connection, applied to the transformed field, is the phase times the covariant derivative applied to the original field. Writing $D_2$ for the derivative built from $\tilde{A}_2$,

$$
\begin{aligned}
D_2(\lambda\tilde\Psi)
&=\tilde\nabla(\lambda\tilde\Psi)+\frac{iϙ}{\hbar}\tilde A_2(\lambda\tilde\Psi) \\
&=\lambda\,\tilde\nabla\tilde\Psi+\frac{iϙ}{\hbar}\lambda(\tilde\nabla\Gamma)\tilde\Psi
 +\frac{iϙ}{\hbar}\tilde A\lambda\tilde\Psi
 -\frac{iϙ}{\hbar}(\tilde\nabla\Gamma)\lambda\tilde\Psi \\
&=\lambda\left(\tilde\nabla\tilde\Psi+\frac{iϙ}{\hbar}\tilde A\tilde\Psi\right)
 =\lambda\,D\tilde\Psi .
\end{aligned}
$$

The two $\tilde{\nabla}\Gamma$ terms cancel, and the centrality of $\lambda$ moves it to the left. The equation $D\tilde{\Psi} = 0$ is therefore **gauge covariant**: it holds in every gauge when it holds in one. The symmetry has been localized, and the price is the field $\tilde{A}$ and the derivative $D$.

**The transformation law is the one already in the corpus.** The law $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$ is exactly the gauge transformation of *Maxwell's Equations in the Biquaternionic Formulation*. The Maxwell gauge freedom is thus not an extra assumption laid on the theory: it is the local form of the global central phase symmetry, and the potential biquaternion is the connection that the localization forces.

**The gauge function must have constant imaginary part to preserve $\mathbb{M}_-$.** If $\tilde{A} \in \mathbb{M}_-$ — the parent's assignment, with $A_0 = i\phi/c$ purely imaginary and $\vec A$ real — then $\tilde{A}_2$ is again in $\mathbb{M}_-$ precisely when $\mathrm{Im}\,\Gamma$ is constant. Indeed

$$
\tilde{\nabla}\Gamma = e_t\,\partial/\partial Q_t\,\Gamma + \sum_{k=1}^{3}\,\vec e_k\,\partial/\partial Q_k\,\Gamma,
$$

and for real $\Gamma$ the scalar coefficient $\partial/\partial Q_t\,\Gamma = -\frac{i}{c}\partial/\partial t'\Gamma$ is purely imaginary while the vector coefficients $\partial/\partial Q_k\,\Gamma$ are real, which is exactly the membership condition of $\mathbb{M}_-$. A $\Gamma$ whose imaginary part is not constant would move the potential out of the material sector. The gauge function of a real connection is real.

**The coupling constant.** The number $ϙ$ is the charge of the field. It is introduced by the principle as a parameter; the algebra does not supply its value. Setting $ϙ = 0$ restores the global theory. The minimal-coupling form of the standard Dirac equation is recovered in this sense, as a biquaternionic statement whose representation conventions the Dirac article left open.

## The Connection and the Covariant Derivative

The field $\tilde{A}$ is the **connection**, and $D$ is the **covariant derivative**. Writing $\tilde{A} = \sum_\mu A_\mu e_\mu$ with complex scalar coefficients $A_\mu$, the action of $D$ on a field separates into components,

$$
D\tilde\Psi = \sum_{\mu\in\{t,x,y,z\}} e_\mu\,D_\mu\tilde\Psi, \qquad D_\mu = \partial/\partial Q_\mu + \frac{iϙ}{\hbar}A_\mu,
$$

where $\partial/\partial Q_t = \partial/\partial(ict')$ and $\partial/\partial Q_k = \partial/\partial x_k$, and where $A_0:=A_t$ in the component displays below.

The following properties are immediate from the definitions and are worth recording, because they are the properties that make $D$ a covariant derivative rather than an arbitrary operator.

**1. It is a derivation on central scalars.** For a central scalar function $f$,

$$
D(f\tilde\Psi)= f\,D\tilde\Psi+(\tilde{\nabla} f)\tilde\Psi,
$$

which is the Leibniz rule of the gradient corrected by the connection. This is the biquaternion form of $D_\mu(f\psi) = f D_\mu\psi + (\partial/\partial Q_\mu f)\psi$.

**2. It is not an element of the algebra.** $D$ is a first-order differential operator, not a biquaternion. Only its components $D_\mu$ are scalar operators, and $D$ acts on fields, not on the algebra.

**3. Its gauge group is the $*$-unitary part of the centre, so the theory is abelian.** The phase $\lambda = \exp(iϙ\Gamma/\hbar)$ is central, so multiplication by it on the left and on the right agree and there is no ordering ambiguity anywhere in the derivation above. This is what makes the construction abelian, and it is a consequence of selecting the gauge group from the centre.

**4. Gauge transformations preserve the material sector.** As shown in the preceding section, a real $\Gamma$ keeps $\tilde{A}$ in $\mathbb{M}_-$; the connection is a material-sector object.

**A preview of the non-abelian case, and its gap.** If the phase is allowed to be a *non-central* invertible biquaternion $\lambda$, then the covariance of the field equation forces $\tilde{A}$ to be algebra-valued, and order matters: the product $\tilde{A}\tilde{\Psi}$ no longer equals $\tilde{\Psi}\tilde{A}$, so the transformation law of $\tilde{A}$ acquires the conjugated $\lambda\tilde{A}\lambda^{-1}$ term rather than remaining additive. The full treatment belongs to the planned companion articles. What can already be said, and is verified below, is that the curvature then acquires a commutator term, and that the algebra already contains the non-commutativity needed for it. The gap is not the non-commutativity; it is the *reality condition* that would select a compact gauge algebra, and that is taken up at the end.

## The Field Strength as the Curvature

The covariant derivative packages the connection. The curvature is built from the connection by differentiation. In the biquaternion algebra the natural first derivative of the connection is the product $\tilde{\nabla}^{\natural}\tilde{A}$, and its scalar and vector parts separate cleanly. A direct computation gives

$$
\tilde{\nabla}^{\natural}\tilde{A} = \underbrace{\left(\partial/\partial Q_t\,A_0 + \mathrm{div}\,\vec A\right)}_{=\,S}e_t + \sum_{k=1}^{3}\left(\partial/\partial Q_t\,A_k - \partial/\partial Q_k A_0\right)\vec e_k - \mathrm{rot}\,\vec A.
$$

The scalar part is the **gauge scalar** $S = \mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$ of the Maxwell article, which transforms as $S_2 = S - \Box\Gamma$ and is therefore pure gauge. The vector part is gauge invariant. Define the **field-strength biquaternion** as the vector part,

$$
\tilde{F} = \mathrm{Vect}\!\left(\tilde{\nabla}^{\natural}\tilde{A}\right) = \tilde{\nabla}^{\natural}\tilde{A} - S .
$$

With the parent's conventions this is the field strength $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ up to the overall normalization that the parent's construction also carries; the parent flags exactly this normalization freedom, and it does not affect anything below.

### The curvature identity

Write $F_{\mu\nu} = \partial/\partial Q_\mu A_\nu - \partial/\partial Q_\nu A_\mu$ for the components of the field strength, and let $\bar{e}_t = e_t$, $\bar{e}_k = -\vec e_k$ be the conjugate basis of *Algebra and Element Conventions*. Then

$$
\boxed{\ \tilde{F} = \mathrm{Vect}\!\left(\tilde{\nabla}^{\natural}\tilde{A}\right) = \frac{1}{2}\sum_{\mu,\nu\in\{t,x,y,z\}} F_{\mu\nu}\,\bar{e}_\mu e_\nu\ }
$$

The identity is exact. The proof is the multiplication table. Since $\tilde{\nabla}^{\natural}\tilde{A} = \sum_{\mu\nu}(\partial/\partial Q_\mu A_\nu)\,\bar{e}_\mu e_\nu$, and since

$$
\mathrm{Sc}\!\left(\bar{e}_\mu e_\nu\right) = \delta_{\mu\nu}, \qquad \mathrm{Vect}\!\left(\bar{e}_\mu e_\nu\right) = -\,\mathrm{Vect}\!\left(\bar{e}_\nu e_\mu\right),
$$

the scalar part of $\tilde{\nabla}^{\natural}\tilde{A}$ is the divergence $\sum_\mu \partial/\partial Q_\mu A_\mu$ and sees only the symmetric part of $\partial/\partial Q_\mu A_\nu$, while the vector part is antisymmetric in $\mu,\nu$ and sees only $F_{\mu\nu}$. Replacing $\partial/\partial Q_\mu A_\nu$ by $\tfrac{1}{2}(\partial/\partial Q_\mu A_\nu - \partial/\partial Q_\nu A_\mu)$ in the vector part gives the boxed identity. The interpretation is direct: **the right-hand side is the curvature 2-form $F = \tfrac{1}{2}\sum_{\mu,\nu}F_{\mu\nu}\,dx_\mu\wedge dx_\nu$, with the basis 1-forms replaced by the algebra elements $\bar{e}_\mu$ and $e_\nu$.** The field strength is the curvature.

This also explains, structurally, why the field strength is not a four-vector. The vector part of $\mathbb{B}$ has six real dimensions, the number of independent components of a 2-form, and the field strength has a vanishing scalar part, so its six real components sit in the vector part. It is a bivector of the algebra, not a four-vector, exactly as *The Material Sector: Four-Vectors, Interval and Lorentz Action* states when it notes that the field strength is not in $\mathbb{M}_-$.

### The field strength as a commutator

In the abelian case the connection coefficients are complex scalars, so they commute and the commutator of the covariant derivatives reduces to the field strength, the curl of the potential:

$$
\boxed{\;[D_\mu, D_\nu] = \frac{iϙ}{\hbar}\left(\partial/\partial Q_\mu A_\nu - \partial/\partial Q_\nu A_\mu\right) = \frac{iϙ}{\hbar}F_{\mu\nu}\;}.
$$

Combining this with the boxed identity,

$$
\tilde{F} = \frac{\hbar}{2iϙ}\sum_{\mu,\nu\in\{t,x,y,z\}}[D_\mu, D_\nu]\,\bar{e}_\mu e_\nu .
$$

The field strength is the **commutator of two covariant derivatives**, contracted with the biquaternion basis. This is the precise sense in which "the field strength is the curvature": the curvature measures the failure of covariant derivatives to commute, and in the algebra that failure is packaged into the vector part of $\tilde{\nabla}^{\natural}\tilde{A}$. The overall constant in the two boxed formulas depends on the convention for $ϙ$ and on the normalization of $\tilde{A}$; the structural content is the identity of the objects, not the numerical factor.

### The homogeneous equations are an identity, not an equation of motion

Because $\tilde{F}$ is *constructed* from $\tilde{A}$ — its electric components are $F_{0k} = \partial/\partial Q_t\,A_k - \partial/\partial Q_k A_0$ and its magnetic components are $-(\mathrm{rot}\,\vec A)_k$ — the two homogeneous Maxwell equations hold identically. The magnetic field is $\vec B = \mathrm{rot}\,\vec A$, so $\mathrm{div}\,\vec B = 0$; and $\vec E = -\partial/\partial t'\vec A - \nabla\phi$, so Faraday's law holds. In the language of forms this is $dF = d^2A = 0$: the homogeneous pair is the **Bianchi identity** of the connection, and it is automatic. The detailed biquaternionic form of the Bianchi identity, and the sense in which a single biquaternion equation carries it, are the subject of the planned companion *Gauge Curvature and the Bianchi Identity*; this article does not claim a one-line form for it. What is established here is the weaker and safer statement: given the potential representation $\tilde{F} = \mathrm{Vect}(\tilde{\nabla}^{\natural}\tilde{A})$, the homogeneous equations are not independent.

## The Gauge Principle and the Maxwell Field

The construction now meets the two parent articles.

**The Maxwell field is the gauge field of the central phase.** The connection $\tilde{A}$, its transformation law $\tilde{A}_2=\tilde{A}-\tilde{\nabla}\Gamma$, the gauge scalar $S$, and the field strength $\tilde{F}$ are exactly the objects of *Maxwell's Equations in the Biquaternionic Formulation*. The single Maxwell equation $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$ is then the **sourced curvature equation** of the abelian connection. The source is expressed in terms of the potential, and the integrability condition $\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}(\sqrt{\mu}\,\tilde{J})\right) = 0$ — the biquaternionic form of charge conservation — is the consistency condition of the sourced equation. With the obstruction of the dynamical question removed by deriving the gauge freedom from a symmetry, the Maxwell structure is seen to be one instantiation of the gauge principle rather than a separate fact about electromagnetism.

**The gauge redundancy is not removed by the principle.** The Lorenz gauge $S = 0$ is a *choice*: it sets the scalar part of $\tilde{\nabla}^{\natural}\tilde{A}$ to zero, and the parent states plainly that $S$ is not physical. The gauge principle produces the connection but does not select a representative. Here the second parent enters. *Canonical Quantization of the Biquaternion Maxwell Field* finds that the framework **cannot fix the gauge**: the Legendre transform is singular, the conjugate momenta give the primary constraint $\mathrm{Sc}(\tilde{\pi}) \approx 0$ and the secondary Gauss-law constraint $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{\pi}) \approx 0$, both first class, and the first-class constraints *generate* the gauge transformations. The freedom derived here from a global symmetry is the same freedom that the quantization article finds the algebra unable to remove. The two results are consistent and complementary: the gauge principle explains the *origin* of the connection and of its redundancy; the quantization article shows that the redundancy is not an artifact that the algebra can eliminate. Neither supplies a gauge-fixing principle, and that remains a gap.

**The sector question is not resolved here.** The quantization article records a "sector straddle": the potential sits in $\mathbb{M}_-$ while the canonical momentum biquaternion $\tilde{\pi}$ sits in $\mathbb{M}_+$, and it leaves undecided whether this has algebraic content. The present derivation locates the *connection* in $\mathbb{M}_-$ (for a real gauge function) and the *phase* in the centre, which is shared by both sectors and therefore does not resolve the straddle. The asymmetry — a material connection and an informational momentum — is inherited as an open question, not explained.

## What the Algebra Supplies and What It Only Transcribes

It is worth separating the two, because they are easily conflated.

**What the algebra supplies.**

- *A canonical abelian gauge group.* The gauge group is the $*$-unitary part of the centre, and the centre is the only place a *central* phase can live. The $\mathrm{U}(1)$ of the abelian gauge principle is therefore attached to the algebra without a choice of representation. This is a genuine structural feature, not a relabelling: it is the reason the abelian case is the natural first case in this framework.
- *A home for the curvature.* The field strength is a 2-form, with six independent components in four dimensions, and the vector part of $\mathbb{B}$ has exactly six real dimensions. The identification "field strength $=$ curvature" is thus structural rather than accidental.
- *Preservation of the material sector.* Real gauge functions keep the connection in $\mathbb{M}_-$, so the gauge structure respects the sector decomposition that the framework is built on.
- *The same scalar imaginary.* The phase $\exp(iϙ\Gamma/\hbar)$ and the complex time coordinate $ict'$ both use the single element $i$ of $\mathbb{B}$. In the standard formulation the $\mathrm{U}(1)$ of electromagnetism and the $i$ of the $ict'$ device are unrelated; here they are the same element. This is stated as an *observation*. Because the phase is central it commutes with everything, and it is not yet established that the shared generator carries content rather than being an artifact of writing both structures in one algebra. It is flagged as a gap, not claimed as a result.

**What it only transcribes.**

- *The abelian gauge principle itself.* The derivation above is the standard global-to-local argument, carried into the biquaternion algebra. The algebra provides a home for the construction and makes the curvature identity transparent; it does not provide a reason for a gauge field to exist.
- *The value of the coupling.* The charge $ϙ$ is a parameter. The algebra does not fix it.
- *The gauge-fixing principle.* As the quantization article establishes, the algebra does not select a gauge.

**What is interpretation.** Reading $\tilde{A}$ as a connection on a bundle and $\tilde{F}$ as its curvature is a geometric interpretation. The algebraic content is the transformation law, the covariance, and the curvature identities; the bundle picture is a consistent interpretation of that content, and the commutator identity above is what makes the interpretation precise. The article does not claim that the algebra forces the geometric picture.

## The Non-Abelian Extension, and Where the Gap Is

The non-abelian case is the subject of the planned companion articles, but one structural fact belongs here because it sharpens the gap.

If the connection is allowed to be algebra-valued — $A_\mu$ an element of $\mathbb{B}$ rather than a complex scalar — then the multiplications by the components no longer commute, and the curvature acquires a commutator term:

$$
D_\mu D_\nu\tilde\Psi-D_\nu D_\mu\tilde\Psi = \frac{iϙ}{\hbar}F_{\mu\nu}\tilde\Psi, \qquad
F_{\mu\nu} = \partial/\partial Q_\mu A_\nu - \partial/\partial Q_\nu A_\mu + \frac{iϙ}{\hbar}[A_\mu, A_\nu],
$$

the bracket $[D_\mu,D_\nu]$ being read as the difference of the two compositions applied to a field. The biquaternion algebra already contains the non-commutativity this needs: no enlargement of the algebra is required to write a non-abelian curvature. But the commutator algebra of $\mathbb{B}$ is the general linear algebra $\mathfrak{gl}(2,\mathbb{C})$, not a compact simple algebra; to land on a gauge algebra such as $\mathrm{SU}(2)$ one must impose a reality condition (anti-Hermiticity, and tracelessness) on the connection. **The algebra supplies the non-commutativity but not the compactness.** Whether the reality conditions required are natural in the biquaternion framework, and which gauge algebras they admit, is the open question that the planned companions on the covariant derivative, non-abelian fields, and Yang–Mills must settle. This article does not.

## The Mass Term and the Axial Symmetry

The gauge principle above was derived for the massless equation. Two Dirac equations carry the name in this corpus, and the distinction matters here.

**The one-sided chiral pair.** The biquaternion Dirac field is the pair of elements $\tilde\Psi_L$ and $\tilde\Psi_R$, one per value of the subscript, and its equation is the off-diagonal pair

$$
\boxed{\;\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,\qquad \tilde\nabla^\natural\tilde\Psi_L=m\tilde\Psi_R\;}
$$

with $\tilde\nabla$ the gradient and $\tilde\nabla^\natural$ its quaternion conjugate. The two lines are one equation per value of the subscript. Both gradients multiply the field on the left, so the pair is one-sided; at $m=0$ the two lines decouple into the two Weyl equations, and at $m\ne0$ the mass couples them off the diagonal. The mass term of the pair is **linear** in the field.

**The two-sided single equation.** Read on the algebra rather than on the pair, the same physics has a one-equation form whose two sides are the two multiplications,

$$
\boxed{\;\tilde\nabla^\natural F=-im\,\bar F\,\vec e_z\;}
$$

where $F$ is the biquaternion-valued field of this form — not the field strength $\tilde{F}$ of §*The Field Strength as the Curvature* — and $\bar F$ is its coefficient conjugate. The mass term is the mass times the **chirality cell** applied to $\bar F$. The chirality cell is the multiplication on the right by $-i\vec e_z$; applied twice it returns the element unchanged, so an element splits into two eigenspaces, one per value of the subscript. The derivative acts on the left, the mass on the right, and the conjugation supplies the second element of the pair. This is the two-sided form: the value of the subscript is a multiplication on the right, not a splitting of the field, and the mass term is **antilinear**. The two forms are related by the real-linear dictionary $A$ of *The Dirac Equation in Biquaternionic Form* and are not the same operator: the pair is linear in the field throughout, while the two-sided equation is linear in its derivative term and antilinear in its mass term. The pair is the representation used for the gauging below; the two-sided form is recorded because it is the one that exhibits the mass as a multiplication on the right, and because the axial current inserts the same cell.

**The central phase acts on the pair.** For $\lambda$ central and constant, $\lambda\tilde\Psi_L$ and $\lambda\tilde\Psi_R$ satisfy the pair whenever $\tilde\Psi_L$ and $\tilde\Psi_R$ do, term by term, because $\lambda$ commutes with $m$ and passes through the two gradients. The continuous global phase symmetry therefore survives the mass, and the abelian gauge principle derived above applies to the massive Dirac field as well as to the massless one — exactly as it does for the complex scalar realization in the previous section. The two realizations agree rather than contrast. The two-sided form is related to the pair by the same real-linear dictionary $A$, not by a complex-linear change of field; the pair is the representation in which the central phase acts linearly, and that is why the gauging is written on it.

What the mass breaks is the **axial** symmetry, not the phase. The axial rotation multiplies the two values of the subscript by opposite phases, $\tilde\Psi_R\mapsto\exp(i\alpha)\tilde\Psi_R$, $\tilde\Psi_L\mapsto\exp(-i\alpha)\tilde\Psi_L$. Each gradient term is multiplied by one of these phases and can be divided out; the mass term cannot, because it pairs the two values and so carries the *relative* factor $\exp(i\alpha)/\exp(-i\alpha)=\exp(2i\alpha)$. The pair is invariant only when $\exp(2i\alpha)=1$, that is $\alpha\equiv0\pmod{\pi}$, where the rotation has degenerated into the global phase $\pm1$. The continuous axial rotation is broken by the mass, exactly as the divergence below records.

Write $\bar{\tilde\Psi}:=\tilde\Psi^{*}i\vec e_x$ for the **Dirac adjoint** of *Chiral Fermions in the Biquaternion Framework* — the Hermitian form, a pairing of two states and not an action on one, to be distinguished from the coefficient conjugation $\bar F$ of the two-sided equation above, and from the quaternionic norm $\tilde\Psi^{\natural}\tilde\Psi$, which vanishes on the zero-divisor cone and cannot serve as a density. The chirality cell acts on the field by $\tilde\Psi\mapsto-i\tilde\Psi\vec e_z$, so the axial current inserts it,

$$
j_{5\mu}=\bar{\tilde\Psi}\,\bigl(e_\mu\,\tilde\Psi\,\vec e_z\,\vec e_{\tau(\mu)}\bigr),
\qquad \tau(t)=x,\quad \tau(k)=y,
$$

where the frame cell of the coordinate $\mu$ and the chirality cell have been applied in that order, and their two factors of $i$ have been reduced by $i(-i)=+1$. The surviving right multiplier is the product $\vec e_z\vec e_{\tau(\mu)}$, in that order: right multipliers compose in the order in which they act. Its divergence is the plain sum over $\mu$, with no metric signs, because the metric is already spent inside the frame cells: the cell $Q\mapsto ie_\mu Q\vec e_{\tau(\mu)}$ applied twice returns $g_{\mu\mu}Q$, so weighting the sum by $g_{\mu\mu}$ a second time would apply the metric twice.

$$
\sum_\mu\partial/\partial Q_\mu\,j_{5\mu}
=2im\,\bar{\tilde\Psi}\,\bigl(\tilde\Psi(-i\vec e_z)\bigr)
=2m\,\bar{\tilde\Psi}\,\tilde\Psi\,\vec e_z,
$$

which vanishes identically only when $m=0$. The factors are reduced in the second form, $i(-i)=+1$. In the biquaternion interpretation this is the statement that the mass is the **off-diagonal coupling between the two values of the subscript** — the two halves that the axial rotation turns in opposite directions — so the symmetry it breaks is exactly the one that rotates those two halves, while the *central* $\mathrm{U}(1)$ that the algebra canonically carries is untouched.

Two things should be said about this, one established and one open.

- **Established.** The computation is elementary and exact. It was checked by direct computation on superpositions of on-shell plane waves, in the display of §*The Legacy Pauli Gamma Formulation*: the unweighted sum reproduces $2im\,\bar{\tilde\Psi}(\tilde\Psi(-i\vec e_z))$ exactly, up to the overall sign carried by the convention for the mass term, whereas the metric-weighted sum is not proportional to it at all — its ratio to the right-hand side varies with the superposition, which is how the redundant metric announces itself. At $m = 0$ both currents are conserved. It is the biquaternion form of the familiar fact that a mass term linear in the field preserves fermion number and breaks the axial symmetry, whereas a mass term that pairs a field with its conjugate — a Majorana-type mass — would break the continuous $\mathrm{U}(1)$ itself. The latter is a statement about the algebra's real structure $\flat = -{\tilde{\Psi}}^{*}$, which is not the Dirac mass. The two-sided equation of the preceding paragraph is not that pairing: it is the representation in which the Dirac mass is a multiplication on the right, and its conjugation belongs to the real-linear dictionary, not to the real structure $\flat$.
- **Open, and left open.** Whether the symmetry that rotates the two values of the subscript can be *gauged*, and whether the framework's central-element structure supplies anything analogous to the would-be Goldstone statement for the axial breaking, is not decided here. A gauged axial symmetry, if it exists, is a question for the non-abelian extension, where the phase no longer commutes with the algebra.

## An External Construction That Gets a Local U(1) Without Frames

An independent construction reaches the abelian principle of this article from the opposite direction, and it is worth recording because it confirms the corpus's intuition that the algebra carries a natural $\mathrm{U}(1)$.

J. Fredsted (*Spinor fields without Lorentz frames in curved spacetime using complexified quaternions*, arXiv:0811.1357v4 [math-ph], 2009) builds a coordinate-covariant and locally Lorentz-invariant formalism for tensor fields and for the field of the pair in curved spacetime that uses no local Lorentz frame and no vierbein, carrying instead a basis $s_\mu \in \mathbb{M}_-$ and a single connection $\omega_\mu \in \mathbb{B}$ subject to the reality condition $\mathrm{Sc}(\omega_\mu + \bar\omega_\mu^\ast) = 0$. The connection's imaginary-scalar part is a local $\mathrm{U}(1)$ freedom, and in the source's words a local $\mathrm{U}(1)$ gauge symmetry "emerges naturally", which the source speculates "might be related to electromagnetism". The transformation is the corpus's own. In the corpus's notation it reads:

$$
\omega_{2,\mu} = \omega_\mu - i\partial/\partial Q_\mu\,\phi, \qquad
\psi_{L,2} = \exp(+i\phi)\psi_L, \qquad
\psi_{R,2} = \exp(-i\phi)\psi_R, \qquad \phi = \phi(x_\mu) \in \mathbb{R},
$$

and it leaves the covariant derivatives covariant, $(D_{2,\mu}\psi_{L,2}) = \exp(+i\phi)D_\mu\psi_L$ and $(D_{2,\mu}\psi_{R,2}) = \exp(-i\phi)D_\mu\psi_R$, exactly as the local phase $\lambda = \exp(iϙ\Gamma/\hbar)$ of this article leaves $D_\mu\tilde\Psi$ covariant. With the central phase identified as $\phi = ϙ\Gamma/\hbar$ and the dictionary $\omega_\mu = i(ϙ/\hbar)A_\mu$ — so that $-i\omega_\mu = (ϙ/\hbar)A_\mu$ is the potential, and the shift $-i\partial/\partial Q_\mu\,\phi$ is the gradient term — the source's transformation is this article's $\tilde A_2 = \tilde A - \tilde\nabla\Gamma$, component by component. The source's $\mathrm{U}(1)$ is thus the central direction of $\mathbb{B}$, its generator the same scalar imaginary $i$, and the phase on $\psi_L$ carries the same sign as the multiplication on the left that this article's parent uses for the charged massive field. The opposite phase on $\psi_R$ is consistent with $\psi_R$ being the conjugate half of the pair: a central phase read through the algebra's real structure is $\lambda^{\flat}=-\bar\lambda$, the antilinear half recorded in §*The Mass Term and the Axial Symmetry*. In that reading the source's pair of phases is one central phase, not two symmetries.

The construction bears on Open Question 3. In the source, the shared generator $i$ is **content-bearing rather than vacuous**: the imaginary-scalar direction of $\omega_\mu$ *is* the $\mathrm{U}(1)$ direction, and the same $i$ is what lets the two-sided vector derivative $\partial/\partial Q_\mu V + \omega_\mu V + V\bar\omega_\mu^\ast$ reduce to a one-sided one on the central piece. The source makes the point explicitly in a note added to the paper: the local Lorentz transformations, which obey $\bar\Lambda = \Lambda^{-1}$, and the local $\mathrm{U}(1)$ transformations, $\Lambda = \exp(i\phi)$, are two cases of the single law $\omega_{2,\mu} = \Lambda\omega_\mu\Lambda^{-1} - (\partial/\partial Q_\mu\,\Lambda)\Lambda^{-1}$. So there the internal phase and the local frame are not merely neighbours in one algebra; they are two subgroups of one local symmetry, and the connection is one object.

The construction also has a catch, and the source states it. Under a local $\mathrm{U}(1)$ transformation a real quaternionic **vector** field is unchanged, $\Lambda V\bar\Lambda=V$ for $\Lambda=\exp(i\phi)$, because a central phase commutes with it and $\bar\Lambda=\Lambda^{-1}$; so at the level of $\mathbb{B}$-valued fields **only the field of the pair can carry the charge**, the vector fields of the algebra being untouched. The source notes that this "flat out contradicts Nature", which contains the charged vector bosons $W^\pm$, and speculates that generalizing from complexified quaternions to complexified octonions might make room for them. The speculation is recorded and not upgraded: the corpus takes no position on it, and the corpus's own empirical contact remains the open question it is everywhere.

What the external construction gives this article is therefore not a new result but an independent route to the same one: a local $\mathrm{U}(1)$ out of the biquaternion structure, obtained without frames and on a curved background, whose phase is the corpus's central phase and whose generator is the same scalar imaginary. It does not supply a principle of gauge fixing, and it does not produce a prediction distinguishing it from ordinary abelian gauge theory — the two standing gaps of this article are untouched by it.

## Open Questions

1. **The non-abelian realization.** The curvature acquires $[A_\mu, A_\nu]$, and the algebra supplies the non-commutativity, but the reality and tracelessness conditions that would select a compact gauge algebra are not derived. Which simple gauge algebras, if any, are natural in $\mathbb{B}$?

2. **The gauge-fixing principle.** The quantization article establishes that the framework cannot fix the gauge. Does the gauge principle, or any other algebraic structure, supply a principle of selection, or is the choice irreducibly extrinsic?

3. **The meaning of the shared generator.** The internal phase and the $ict'$ complex structure share the scalar imaginary $i$. Is this identification content-bearing, or vacuous because the phase is central and commutes with everything? An external frame-free construction, recorded in *An External Construction That Gets a Local U(1) Without Frames*, is one in which the identification is content-bearing; that does not settle the question for this framework.

4. **The matter representation.** The covariant derivative derived here multiplies the field on the left and the abelian phase is central. For a non-abelian phase the two sides differ, and the choice of representation on the matter field must be specified. What fixes it?

5. **The mass term, the axial symmetry, and the real structure.** The mass term is the linear chiral pair, so the continuously charged massive field is not obstructed: the abelian minimal coupling derived here applies to the massive Dirac field as well, and the $\mathrm{U}(1)$ is realized on the pair. The live question is the axial one — the mass breaks the symmetry that rotates the two values of the subscript, and whether that symmetry can be gauged, and with what consequences, is not settled here. Separately, the pairing built on the algebra's real structure $\flat = -{}^{*}$, which is $\mathbb{C}$-antilinear and order-reversing, is not the Dirac mass; whether it is a physical Majorana-type coupling or the real-form expression of an ordinary Dirac mass remains open. That question is carried by *The Dirac Equation in Biquaternionic Form*, whose open question 1 asks what the real structure means for the electroweak interaction and for the distinction between the neutrino and the charged fermions, and by *The Neutrino and Majorana Fermions in Biquaternionic Form*, where the Majorana-versus-Dirac reading belongs and where its consequences for fermion-number violation are examined.

6. **The local complex structure and the connection.** The framework already makes the complex structure local — the speed of light $c = 1/\sqrt{\epsilon\mu}$ varies with the medium, and so does the $ict'$ structure. Is that local *frame* related to the local *phase* of the gauge principle? Both are "local structures" in the same algebra, but no relation between them is established here, and the suggestion is recorded only as a question.

7. **Empirical content.** As everywhere in the framework, the unresolved question is whether any of this yields a prediction distinguishing it from standard gauge theory. The gauge principle as presented is a reformulation; the framework-level question of empirical contact remains open.
## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate and on the metric, $g[\mathbb{B}]$ or $g[\mathbb{M}_-]$.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. They are the only place in the article where a $\gamma$ symbol is used.

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

The factors of $i$ are reduced before the squares are read, $i^2=-1$:

$$
\gamma_0^2=i^2L_{e_t}^{\mathrm{pau}}R_{\vec e_x^2}^{\mathrm{pau}}=(-1)(+1)(-1)I_4=I_4,\qquad
\gamma_k^2=i^2L_{\vec e_k^2}^{\mathrm{pau}}R_{\vec e_y^2}^{\mathrm{pau}}=(-1)(-1)(-1)I_4=-I_4,
$$

In the axis-free display:

$$
\gamma_0^2=i^2L_{e_t}^{\mathrm{axf}}R_{\vec e_x^2}^{\mathrm{axf}}=(-1)(+1)(-1)I_4=I_4,\qquad
\gamma_k^2=i^2L_{\vec e_k^2}^{\mathrm{axf}}R_{\vec e_y^2}^{\mathrm{axf}}=(-1)(-1)(-1)I_4=-I_4,
$$

so the frame carries the Lorentzian signature. With $\mu,\nu\in\{0,1,2,3\}$ in this section only, the five cells satisfy

$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad \varepsilon=(1,-1,-1,-1),\qquad
\{\gamma_\mu,\gamma_5\}=0,\qquad
\gamma_5^2=I_4,\qquad
\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3 .
$$

The last identity fixes the sign: $\gamma_0\gamma_1\gamma_2\gamma_3=-i\gamma_5$, so the product of the four generator cells is the chirality cell up to the central factor.

$\gamma_5$ is the chirality cell $\chi=-iR_{\vec e_z}^{\mathrm{pau}}$ used in the body, since $L_{e_t}^{\mathrm{pau}}=I$. The central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$, with $\tilde\Xi_{\mathrm{ad}}$ the adjoined central root of $-e_t$ so that $\tilde\Xi_{\mathrm{ad}}^2=-e_t$ and $\chi_{\mathrm{ad}}^2=e_t$, is a different object: being central it is the difference of the two central idempotents of the complexified algebra, and $\gamma_5$ is its representative on the Dirac module.

The correspondence with the matrix algebra is complex-linear. Over $\mathbb{R}$ the products of the four generator cells, with real coefficients, span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$, and the cells $L_aR_b$ with $a,b$ in the real quaternion algebra span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$; with biquaternion parameters the cells span all of $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The gauge principle in biquaternionic form begins with the **centre** of the biquaternion algebra. The centre is the complex scalar subspace $\mathbb{C}_{\mathbb{B}}$, whose $*$-unitary part is $\mathrm{U}(1)$. A constant central phase $\tilde{\Psi} \mapsto \lambda\tilde{\Psi}$ is a symmetry of the one-sided chiral pair, massive or massless, because a central constant passes through the gradient and through the linear mass term.

Making the phase local, $\lambda = \exp(iϙ\Gamma(\tilde{Q})/\hbar)$, adds the term $\frac{iϙ}{\hbar}\lambda(\tilde{\nabla}\Gamma)\tilde{\Psi}$, and cancelling it forces a connection $\tilde{A}$ with the transformation law

$$
\boxed{\;\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma\;},
$$

which is exactly the gauge transformation of the biquaternionic Maxwell article, together with a covariant derivative

$$
\boxed{\;D\tilde\Psi = \tilde{\nabla}\tilde\Psi + \frac{iϙ}{\hbar}\tilde{A}\tilde\Psi, \qquad D_\mu = \partial/\partial Q_\mu + \frac{iϙ}{\hbar}A_\mu\;},
$$

under which $D\tilde{\Psi}$ transforms by the phase factor. The connection is a material-sector object: a real gauge function keeps $\tilde{A} \in \mathbb{M}_-$.

The field strength is the vector part of $\tilde{\nabla}^{\natural}\tilde{A}$, with the gauge scalar $S = \mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$ as its pure-gauge scalar part, and it satisfies the exact **curvature identity**

$$
\tilde{F} = \mathrm{Vect}\!\left(\tilde{\nabla}^{\natural}\tilde{A}\right) = \frac{1}{2}\sum_{\mu,\nu}F_{\mu\nu}\,\bar{e}_\mu e_\nu,
$$

the six real components of the curvature 2-form sitting in the vector part of the algebra, and the **commutator identity**

$$
[D_\mu, D_\nu] = \frac{iϙ}{\hbar}F_{\mu\nu}, \qquad \tilde{F} = \frac{\hbar}{2iϙ}\sum_{\mu,\nu}[D_\mu, D_\nu]\,\bar{e}_\mu e_\nu .
$$

Because $\tilde{F}$ is constructed from $\tilde{A}$, the homogeneous Maxwell equations are an identity — the Bianchi identity of the connection — not equations of motion.

The result connects directly to the two parents. The Maxwell field is the gauge field of the central phase, and its single equation $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$ is the sourced curvature equation; the gauge redundancy derived here is the one that *Canonical Quantization of the Biquaternion Maxwell Field* finds the algebra unable to remove. The algebra supplies a canonical abelian gauge group, a six-dimensional home for the curvature, and preservation of the material sector; it does not supply the coupling constant, a gauge-fixing principle, or a derivation of the geometric interpretation, which is interpretation.

Two gaps are left visible. The non-abelian extension needs the algebra's non-commutativity, which is present, but also a reality condition selecting a compact gauge algebra, which is not derived. And the mass term, being linear in the one-sided pair, preserves the continuous phase symmetry, so the gauge principle as derived applies to the massive sector as well; what the mass breaks is the axial symmetry between the two values of the subscript, and whether that can be gauged is left open. The breaking is visible in the current: $j_{5\mu}=\bar{\tilde\Psi}\,(e_\mu\tilde\Psi\vec e_z\vec e_{\tau(\mu)})$ has divergence $2m\,\bar{\tilde\Psi}\,\tilde\Psi\,\vec e_z$, which is the mass times a non-zero bilinear. The two-sided form of the same mass is recorded only for the chirality link: its mass term is a multiplication on the right with a conjugation, and the pair is the representation on which the phase acts linearly.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra of *Algebra and Element Conventions*, the carrier of every element of this article |
| $e_t, \vec e_x, \vec e_y, \vec e_z$ | the units of the algebra; $e_t$ is the unit, $\vec e_k^2 = -\vec e_t$ |
| $i$ | the scalar imaginary, $i^2 = -1$ |
| $\tilde Q$ | a generic element of $\mathbb{B}$ |
| $\tilde\Psi, \tilde\Phi$ | biquaternion-valued fields: the Dirac pair and the complex scalar |
| $\tilde\Psi_L, \tilde\Psi_R$ | the two elements of the Dirac pair; $L$ and $R$ are the two values of the subscript |
| $\tilde\Psi \mapsto -i\tilde\Psi\vec e_z$ | the chirality cell written as an action; applied twice it returns the element unchanged |
| $\bar{\tilde\Psi} = \tilde{\Psi}^{*}i\vec e_x$ | the Dirac adjoint, a pairing of two states and not an action on one |
| $\mathbb{M}_-, \mathbb{M}_+$ | the material and informational sectors |
| $\mathbb{C}_{\mathbb{B}}$ | the complex scalar subspace, the centre of the algebra |
| $\tilde{\nabla}$, $\tilde{\nabla}^{\natural}$, $\Box$ | the biquaternionic gradient, its quaternion conjugate, the d'Alembertian |
| $\bar e_\mu$ | the conjugate basis, $\bar e_t = e_t$ and $\bar e_k = -\vec e_k$ |
| $\lambda = \exp(iϙ\Gamma/\hbar)$ | the local central phase; $\Gamma$ a real scalar |
| $ϙ$ | the coupling constant (charge), not fixed by the algebra |
| $\tilde{A} = \sum_\mu A_\mu e_\mu$ | the connection, the potential biquaternion of $\mathbb{M}_-$ |
| $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$ | the gauge transformation of the connection |
| $D\tilde\Psi = \tilde{\nabla}\tilde\Psi + \frac{iϙ}{\hbar}\tilde{A}\tilde\Psi$ | the covariant derivative, written as an action |
| $D_\mu = \partial/\partial Q_\mu + \frac{iϙ}{\hbar}A_\mu$ | its components |
| $S = \mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$, $S_2 = S - \Box\Gamma$ | the gauge scalar; Lorenz gauge $S = 0$ |
| $\tilde{F} = \mathrm{Vect}(\tilde{\nabla}^{\natural}\tilde{A})$ | the field strength, the curvature |
| $F_{\mu\nu} = \partial/\partial Q_\mu A_\nu - \partial/\partial Q_\nu A_\mu$ | the abelian curvature components |
| $\tilde\nabla\tilde\Psi_R = m\tilde\Psi_L$, $\tilde\nabla^\natural\tilde\Psi_L = m\tilde\Psi_R$ | the one-sided chiral pair; the mass is linear in the field |
| $\tilde\nabla^\natural F = -im\bar F\vec e_z$ | the two-sided Dirac equation; $\bar F$ the coefficient conjugate, the mass term antilinear |
| $F$ | the field of the two-sided equation, not the field strength $\tilde F$ |
| $j_{5\mu} = \bar{\tilde\Psi}(e_\mu\tilde\Psi\vec e_z\vec e_{\tau(\mu)})$ | the axial current; $\tau(t) = x$, $\tau(k) = y$; its divergence is the plain sum |
| $\tilde J = ic\rho\,e_t + \vec J$ | the four-current; the source of the Maxwell equation is $\sqrt{\mu}\,\tilde J$ |
| $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$ | the biquaternionic Maxwell equation |
| $c = 1/\sqrt{\epsilon\mu}$ | the speed of light in the medium |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- Hermann Weyl, "Elektron und Gravitation," *Zeitschrift für Physik* **56** (1929) 330–352, for the origin of the gauge principle and the local phase.
- Chen-Ning Yang and Robert L. Mills, "Conservation of Isotopic Spin and Isotopic Gauge Invariance," *Physical Review* **96** (1954) 191–195, for the non-abelian extension.
- P. A. M. Dirac, *Lectures on Quantum Mechanics* (Yeshiva University, 1964), for first-class constraints and the Hamiltonian form of gauge theories.
- L. D. Faddeev and A. A. Slavnov, *Gauge Fields: Introduction to Quantum Theory* (Benjamin/Cummings, 1980), for the covariant quantization of gauge fields.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), and S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the standard treatment of abelian and non-abelian gauge theory.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of the biquaternion algebra with the even part of the real Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{R})$ and the bivector structure of 2-forms.
- V. V. Kravchenko, *Applied Quaternionic Analysis*, Research and Exposition in Mathematics 28 (Heldermann, 2003), for the two-sided quaternionic Dirac equation set beside the one-sided chiral pair in §*The Mass Term and the Axial Symmetry*.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the gauge-theoretic interpretation of the connection and curvature in geometric algebra.
- F. Strocchi, *An Introduction to the Non-Perturbative Foundations of Quantum Field Theory* (Oxford, 2013), for the constraint and gauge-structure analysis behind the first-class count.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions" (2016), for the biquaternionic Maxwell equation and the operator factorization used here.
- J. Fredsted, "Spinor fields without Lorentz frames in curved spacetime using complexified quaternions," arXiv:0811.1357v4 [math-ph] (2009), for the external construction recorded in *An External Construction That Gets a Local U(1) Without Frames*: a coordinate-covariant, vierbein-free formalism in which the imaginary-scalar part of a single algebra-valued connection is a local $\mathrm{U}(1)$, and the local Lorentz and local $\mathrm{U}(1)$ symmetries are two cases of one transformation law. Cited as an external claim; the corpus does not adopt it.
- Companion articles: [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html); [Canonical Quantization of the Biquaternion Maxwell Field](canonical-quantization-of-the-biquaternion-maxwell-field.html); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html); [The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form](the-dirac-hestenes-equation-and-spacetime-algebra-in-biquaternionic-form.html); [Parra's Four Options of the Dirac Equation and the Discrete Symmetries](parras-four-options-of-the-dirac-equation-and-the-discrete-symmetries.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html).
