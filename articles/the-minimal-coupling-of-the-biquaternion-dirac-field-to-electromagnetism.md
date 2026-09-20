
# __The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism__

## Introduction

**Minimal coupling** is the prescription by which a charged field is coupled to the electromagnetic field: the ordinary derivative is replaced by the **covariant derivative**. In the biquaternion framework both objects are already fixed by the gauge principle. The connection is the potential biquaternion $\tilde{A}$ of *Maxwell's Equations in the Biquaternionic Form*, its gauge transformation is

$$
\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma,
$$

and the covariant derivative is

$$
D = \tilde{\nabla} + \frac{iq}{\hbar}\tilde{A}, \qquad D_\mu = \partial_\mu + \frac{iq}{\hbar}A_\mu .
$$

The gauge principle article derived $D$ from the localization of the algebra's central phase and verified that $D\tilde{\Psi}$ transforms homogeneously. It applied the result to a general biquaternion field, not specifically to the Dirac field. *The Dirac Equation in Biquaternionic Form* records, as its open question 7, that the precise biquaternion form of the minimal coupling of the Dirac field "depends on the representation conventions and is worth stating explicitly". This article supplies that statement, and reports what the recomputation gives.

Three results are established here. The first is the coupled equation itself: replacing the gradient in the free biquaternion Dirac equation $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat$ by the covariant derivative gives $D\tilde{\Psi} = m\tilde{\Psi}^\flat$, whose components are $\sum_\mu e_\mu(\partial_\mu + \frac{iq}{\hbar}A_\mu)\tilde{\Psi} = m\tilde{\Psi}^\flat$. The second is that this coupling is **exactly gauge covariant in the massless case** — $D\tilde{\Psi} = 0$ holds in every gauge when it holds in one — and **not gauge covariant in the massive case**, because the mass term is antilinear: under the local phase the mass term acquires the factor $e^{2iq\Gamma/\hbar}$, so the equation is form-invariant only for a constant phase with $\lambda = \pm 1$. The third is a negative result about the interaction current: the naive gauge-invariant bilinear $i\tilde{\Psi}\tilde{\Psi}^\dagger$ is a material-sector object but is **not conserved** on solutions of the massless equation, so the electromagnetic current of the coupled system is not a pure biquaternion product of this kind.

The division between what is established and what is interpretation is stated at the outset and kept explicit.

- **Established, and recomputed below.** The minimal-coupling prescription $D = \tilde{\nabla} + \frac{iq}{\hbar}\tilde{A}$ acting on the biquaternion Dirac field by left multiplication; the coupled equation and its component form; the exact gauge covariance of the massless coupled equation; the failure of gauge covariance in the massive case, with the residual symmetry $\lambda = \pm 1$; the gauge invariance and material-sector membership of $i\tilde{\Psi}\tilde{\Psi}^\dagger$; and the non-conservation of that bilinear.
- **Interpretation.** Reading the coupled equation as "the Dirac field in a background electromagnetic connection" is a geometric reading of an algebraic construction. The algebra supplies the transformation law and the covariance; the connection/curvature picture is a consistent reading, as in the gauge principle article.
- **Gaps, left visible.** The massive equation's continuous symmetry is broken by its mass term, so the minimal coupling derived here is a property of the **massless** biquaternion Dirac field. The biquaternion form of the conserved interaction current is not the naive bilinear, and is not settled here. Whether the left or the right action on the algebra is the physical matter representation is a choice the parent left open. These are stated as gaps in the sections where they arise and collected in the open questions.

The article is organized as follows. The next section recalls the Dirac field and the phase symmetry that is to be localized. The section after that states the minimal-coupling prescription. The following section proves the covariance in the massless case and fixes the sign conventions. The next section treats the massive case and isolates the obstruction. A section examines the interaction current and the Maxwell source, and reports the negative result. A section relates the construction to the standard spinor-module minimal coupling. A section separates what the algebra supplies from what it only transcribes. The article closes with open questions.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the complex scalar subspace, which is the center of the algebra. The biquaternionic gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$, and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$. The potential and field strength are $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$ and $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$, the source is $\tilde{R} = \frac{i\rho}{\sqrt{\epsilon}}e_0 + \sqrt{\mu}\,\mathbf{J}$, and the Maxwell equation is $\tilde{\nabla}\tilde{F} = -\tilde{R}$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the **speed of light in the medium** and $c_0$ the vacuum speed of light. The Dirac field is $\tilde{\Psi}\in\mathbb{B}$ with $\tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger$ and $\tilde{\Psi}^\dagger = \bar{\tilde{\Psi}}^{\,*}$. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged.

## The Dirac Field and Its Phase Symmetry

The **biquaternion Dirac field** is a biquaternion-valued field $\tilde{\Psi}(\tilde{X}) \in \mathbb{B}$ satisfying the free equation

$$
\tilde{\nabla}\tilde{\Psi} = m\,\tilde{\Psi}^\flat, \qquad \tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger = -\bar{\tilde{\Psi}}^{\,*},
$$

which reduces to

$$
\tilde{\nabla}\tilde{\Psi} = 0
$$

when $m = 0$. The massless equation is identical in form to the source-free biquaternion Maxwell equation obeyed by the field-strength biquaternion $\tilde{F}$; the difference is the representation, the Maxwell field living in the vector part of the algebra and the Dirac field in the full algebra. The two are the two representations of the same Clifford algebra, as the parent article records.

The symmetry that minimal coupling localizes is the algebra's central $U(1)$, established in the gauge principle article. The center of $\mathbb{B}$ is the complex scalar subspace

$$
\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0,\, ie_0\},
$$

and its unitary elements are the phases $\lambda = e^{i\theta}$ with $\theta \in \mathbb{R}$. A **constant** central phase

$$
\tilde{\Psi} \;\longmapsto\; e^{i\theta}\tilde{\Psi}, \qquad \theta \ \text{constant},
$$

is a symmetry of the massless equation, because a central constant commutes with the basis and with the derivatives and therefore passes through the gradient:

$$
\tilde{\nabla}\!\left(e^{i\theta}\tilde{\Psi}\right) = e^{i\theta}\,\tilde{\nabla}\tilde{\Psi}.
$$

The **massive** equation carries no such continuous symmetry. The mass term pairs the field with its anti-Hermitian conjugate, and

$$
\left(\lambda\tilde{\Psi}\right)^\flat = \lambda^{*}\,\tilde{\Psi}^\flat
$$

for a central phase $\lambda$, because the conjugation $\flat$ is anti-linear. Invariance under $\tilde{\Psi}\mapsto\lambda\tilde{\Psi}$ therefore requires $\lambda = \lambda^{*}$; among unimodular phases this leaves only $\lambda = \pm 1$. This is the mass-term obstruction of the gauge principle article, recalled here for one reason: it decides in advance how much of the minimal-coupling prescription can be applied. The continuous coupling belongs to the **massless** field; the massive field carries only the discrete sign.

The **charge** $q$ is the coupling constant of the field, introduced by the gauge principle. It is a parameter: the algebra does not fix its value, its sign, or its quantization. For the electron $q = -e$; the value and the sign are inserted, as *The Electron in Biquaternionic Form* records.

## The Minimal Coupling Prescription

The prescription replaces the gradient in the free equation by the covariant derivative:

$$
\tilde{\nabla} \;\longrightarrow\; D = \tilde{\nabla} + \frac{iq}{\hbar}\tilde{A}, \qquad
D\tilde{\Psi} = \tilde{\nabla}\tilde{\Psi} + \frac{iq}{\hbar}\,\tilde{A}\,\tilde{\Psi}.
$$

The connection acts by **left multiplication** on the field. Applied to the free Dirac equation, the prescription gives the **minimally coupled biquaternion Dirac equation**

$$
\boxed{\ D\tilde{\Psi} = m\,\tilde{\Psi}^\flat\ }
$$

that is,

$$
\tilde{\nabla}\tilde{\Psi} + \frac{iq}{\hbar}\,\tilde{A}\,\tilde{\Psi} = m\,\tilde{\Psi}^\flat,
$$

and in the massless case

$$
D\tilde{\Psi} = 0, \qquad \text{i.e.} \qquad \tilde{\nabla}\tilde{\Psi} + \frac{iq}{\hbar}\,\tilde{A}\,\tilde{\Psi} = 0 .
$$

The term $\frac{iq}{\hbar}\tilde{A}\tilde{\Psi}$ is the **interaction term**. It is exactly the term that the localization of the phase forces, and it is the biquaternion representative of the familiar $\frac{iq}{\hbar}\gamma^\mu A_\mu$ coupling of the spinor-module Dirac equation.

**Component form.** Write the potential as $\tilde{A} = \sum_\mu A_\mu e_\mu$ with complex scalar coefficients $A_\mu$ — the abelian case, in which the connection coefficients are central scalars and commute with one another. Since each $A_\mu$ is a scalar and commutes with the basis, the covariant derivative separates into components:

$$
D = \sum_{\mu=0}^{3} e_\mu\left(\partial_\mu + \frac{iq}{\hbar}A_\mu\right),
\qquad
D_\mu = \partial_\mu + \frac{iq}{\hbar}A_\mu,
$$

with $\partial_0 = \partial_{ict}$ and $\partial_k = \partial_{x_k}$. This is the identical component form derived in the gauge principle article, now read as an operator on the Dirac field. Setting $\hbar = 1$ gives $D_\mu = \partial_\mu + iqA_\mu$, the convention used for the minimal substitution in the companion article on the Dirac equation's solutions and the non-relativistic limit.

**The connection is a material-sector object.** The gauge principle article shows that a **real** gauge function $\Gamma$ keeps $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ in $\mathbb{M}_-$. The coupling is therefore the coupling of the Dirac field to a material-sector connection, and the ingredient $\frac{iq}{\hbar}\tilde{A}$ in $D$ is anti-Hermitian. This is inherited, not rederived.

**Sign convention.** The gauge principle article fixes the pair of signs $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ and $D = \tilde{\nabla} + \frac{iq}{\hbar}\tilde{A}$ with the phase $\lambda = e^{iq\Gamma/\hbar}$, and its companion records that the two must be kept together. The open question in the parent Dirac article writes the standard physics convention $\partial_\mu \to \partial_\mu - iqA_\mu/\hbar$, with the opposite sign. That is the same coupling with the opposite sign of $q$ (or of $\tilde{A}$); this article inherits the gauge principle's sign and does not silently flip it. The covariance checks below use the inherited pair.

**Left action and right action.** The prescription above acts on the left. The algebra also admits a mirror construction, with the derivative taken on the right and the connection inserted on the right:

$$
\tilde{\Psi}\overleftarrow{\tilde{\nabla}} + \frac{iq}{\hbar}\,\tilde{\Psi}\,\tilde{A},
\qquad \tilde{\Psi}\overleftarrow{\tilde{\nabla}} := \sum_\mu (\partial_\mu\tilde{\Psi})\,e_\mu .
$$

Both constructions are gauge covariant (verified below). What is **not** covariant is the mixed combination — the left gradient with the connection inserted on the right. The two consistent constructions correspond to the two ways the algebra can act on the field, and the choice between them is a choice of **matter representation**: on which module, and from which side, the Dirac field sits. The gauge principle article records this as an open question, and this article does not resolve it; it states the left-action form, which is the one the gauge principle produces, and records the right-action mirror as the alternative.

## Gauge Covariance of the Massless Coupled Equation

The gauge transformation is

$$
\tilde{\Psi}' = \lambda\,\tilde{\Psi}, \qquad \lambda = e^{iq\Gamma(\tilde{X})/\hbar}, \qquad \Gamma \ \text{real},
$$

together with $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$. The covariance is the same computation as in the gauge principle article, repeated here because it is the justification of the prescription. The Leibniz rule for the left action of the gradient,

$$
\tilde{\nabla}\!\left(\lambda\tilde{\Psi}\right) = \lambda\,\tilde{\nabla}\tilde{\Psi} + \left(\tilde{\nabla}\lambda\right)\tilde{\Psi},
$$

and the chain rule for the central phase,

$$
\tilde{\nabla}\lambda = \frac{iq}{\hbar}\left(\tilde{\nabla}\Gamma\right)\lambda ,
$$

combine into

$$
\tilde{\nabla}\!\left(\lambda\tilde{\Psi}\right) = \lambda\left[\tilde{\nabla}\tilde{\Psi} + \frac{iq}{\hbar}\left(\tilde{\nabla}\Gamma\right)\tilde{\Psi}\right].
$$

The covariant derivative built from $\tilde{A}'$ then gives

$$
\begin{aligned}
D'(\lambda\tilde{\Psi})
&= \tilde{\nabla}(\lambda\tilde{\Psi}) + \frac{iq}{\hbar}\left(\tilde{A} - \tilde{\nabla}\Gamma\right)(\lambda\tilde{\Psi}) \\
&= \lambda\,\tilde{\nabla}\tilde{\Psi} + \frac{iq}{\hbar}\left(\tilde{\nabla}\Gamma\right)\lambda\tilde{\Psi} + \frac{iq}{\hbar}\lambda\,\tilde{A}\,\tilde{\Psi} - \frac{iq}{\hbar}\left(\tilde{\nabla}\Gamma\right)\lambda\tilde{\Psi} \\
&= \lambda\left[\tilde{\nabla}\tilde{\Psi} + \frac{iq}{\hbar}\tilde{A}\tilde{\Psi}\right] = \lambda\,D\tilde{\Psi}.
\end{aligned}
$$

The two $\tilde{\nabla}\Gamma$ terms cancel and the central $\lambda$ moves to the left. Consequently

$$
D\tilde{\Psi} = 0 \qquad \Longleftrightarrow \qquad D'\tilde{\Psi}' = 0 :
$$

the **massless minimally coupled biquaternion Dirac equation is exactly gauge covariant**. It holds in every gauge when it holds in one, and the phase of the field is not observable on its own. This is the charged massless fermion — the biquaternion form of the gauged Weyl field.

The same computation gives the mirror statement for the right action. With the derivative on the right and the connection inserted on the right, and with the same transformation laws for $\tilde{\Psi}$ and $\tilde{A}$, the right covariant derivative is also homogeneous, so the right-action coupled equation is also covariant. The **mixed** insertion is not: the two gradient terms involving $\tilde{\nabla}\Gamma$ no longer cancel, because one acts on the field from the left and the other multiplies it from the right. This is the algebraic content of the statement that the matter representation must be chosen consistently.

## The Massive Case: The Mass Term Obstructs the Coupling

The massive equation is where the prescription fails, and it fails for a reason that is structural rather than technical. Suppose the minimally coupled massive equation holds in one gauge:

$$
D\tilde{\Psi} = m\,\tilde{\Psi}^\flat .
$$

Because $D$ is covariant, the left-hand side of the transformed equation is

$$
D'\tilde{\Psi}' = \lambda\,D\tilde{\Psi} = \lambda\,m\,\tilde{\Psi}^\flat .
$$

The right-hand side is the transformed mass term, and the conjugation is anti-linear:

$$
m\left(\tilde{\Psi}'\right)^\flat = m\left(\lambda\tilde{\Psi}\right)^\flat = m\,\lambda^{*}\,\tilde{\Psi}^\flat .
$$

Writing this in terms of the transformed field, for which $\tilde{\Psi}^\flat = \left(\tilde{\Psi}'\right)^\flat/\lambda^{*}$,

$$
D'\tilde{\Psi}' = m\,\frac{\lambda}{\lambda^{*}}\,\left(\tilde{\Psi}'\right)^\flat = m\,e^{2iq\Gamma/\hbar}\,\left(\tilde{\Psi}'\right)^\flat .
$$

The mass term acquires the phase factor $e^{2iq\Gamma/\hbar}$. The equation is **not form-invariant** under a local phase: the operator side transforms by one power of $\lambda$ and the mass side by the conjugate. Equivalently, the difference between the two sides of the transformed equation is

$$
\lambda\,m\,\tilde{\Psi}^\flat - m\,\lambda^{*}\,\tilde{\Psi}^\flat = m\left(\lambda - \lambda^{*}\right)\tilde{\Psi}^\flat ,
$$

which vanishes identically only when $\lambda$ is real. Among the unimodular phases this leaves

$$
\lambda = \pm 1 :
$$

the continuous $U(1)$ of the massless theory is broken to a discrete $\mathbb{Z}_2$ by the mass term, and the abelian minimal coupling derived above does not survive it.

**What this is.** The computation is elementary and exact, and it is the biquaternion form of a familiar fact: a mass term that pairs a field with its conjugate — a **Majorana-type** mass — is incompatible with a gauged continuous $U(1)$ (fermion number), whereas a mass term linear in the field is compatible. The complex scalar realization of the phase symmetry in the gauge principle article has a linear mass term and keeps its $U(1)$ even when massive. The standard four-component Dirac equation has the linear mass term $m\psi$ and is gauge covariant under minimal coupling. The biquaternion equation, as written by the parent, has the **antilinear** mass term $m\tilde{\Psi}^\flat$, and it is this object that the phase cannot pass through.

**What it is not.** The article does not declare the parent's equation defective. It records that, as written, the equation's mass term is antilinear, that the continuously gauged minimal coupling therefore applies to the massless sector, and that the massive sector is where the framework's gauge structure and the parent's mass term do not yet meet. Whether the parent's mass term is *intended* as a Majorana-type coupling, or whether it is the real-form expression of an ordinary linear Dirac mass whose $U(1)$ is realized differently on the spinor module, is not decided here; it is the gauge principle article's open question 5, and it is left open.

**Candidate readings of the massive equation.** Two inequivalent readings are available, and they are not equivalent, so the article states both and chooses neither. (i) The biquaternion equation is a **Majorana-type** equation; then the charged minimal coupling is genuinely absent in the massive sector, and only the massless (Weyl) field carries electromagnetism. (ii) The parent's mass term is a **real-form encoding** of a linear Dirac mass, in which case the physical coupling is the standard one on the spinor module, where the mass term is linear and the minimal coupling is covariant; the antilinear algebra-level equation is then not the equation that carries the charge. The choice between these readings changes the conclusion about the charged massive field, and the framework as inherited does not decide between them; this article states both and leaves the decision open.

## The Interaction Current and the Maxwell Source

Minimal coupling has a second half: the coupled field must **source** the electromagnetic field. In the biquaternion framework the sourced Maxwell equation is $\tilde{\nabla}\tilde{F} = -\tilde{R}$, and the source $\tilde{R}$ satisfies the integrability condition $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{R}) = 0$, the biquaternionic form of charge conservation.

The natural candidate for the current of the Dirac field is the bilinear

$$
\tilde{J} = i\,\tilde{\Psi}\,\tilde{\Psi}^\dagger .
$$

Two of its properties are immediate and exact. It is **gauge invariant**, because for a unimodular central phase

$$
\left(\lambda\tilde{\Psi}\right)\left(\lambda\tilde{\Psi}\right)^\dagger = \lambda\,\tilde{\Psi}\tilde{\Psi}^\dagger\,\lambda^{*} = |\lambda|^2\,\tilde{\Psi}\tilde{\Psi}^\dagger = \tilde{\Psi}\tilde{\Psi}^\dagger ,
$$

and it is **anti-Hermitian**, $\tilde{J}^\dagger = -\tilde{J}$, hence an element of the material sector $\mathbb{M}_-$ — the same sector as the current $\tilde{J} = ic\rho\,e_0 + \mathbf{j}$ of the Maxwell article. Its scalar part is $i\,\mathrm{Sc}(\tilde{\Psi}\tilde{\Psi}^\dagger) = i\,\|\tilde{\Psi}\|_E^2$, a positive imaginary number, matching the $ic\rho$ form of a positive density. It is, by these tests, a plausible current.

**It is not conserved.** The divergence of $\tilde{J}$ in the $ict$ convention is the scalar part of $\bar{\tilde{\nabla}}\tilde{J}$,

$$
\mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{J}\right) = \partial_{ict}J_0 + \mathrm{div}\,\mathbf{J},
$$

the quantity that would have to vanish on solutions. It does not. To check this without relying on the case that suggested the candidate, take a field generated from a wave-equation potential: if $\phi$ is a biquaternion whose every component satisfies the scalar wave equation $\Box\phi = 0$, then

$$
\tilde{\Psi} = \bar{\tilde{\nabla}}\phi
$$

satisfies $\tilde{\nabla}\tilde{\Psi} = \tilde{\nabla}\bar{\tilde{\nabla}}\phi = \Box\phi = 0$, so it is a genuine solution of the massless equation. On such a solution, with $\phi$ built from superposed plane waves so that no accidental cancellation is available, the divergence $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{J})$ is not zero; the computation gives values of order $10^2$ at generic points, for either sign of the bilinear. The naive biquaternion product is therefore **not** the conserved electromagnetic current of the Dirac field.

**Why, and what the current is instead.** The reason is representation-theoretic. The conserved current of the Dirac field is the spinor-module bilinear $j^\mu = \bar{\psi}\gamma^\mu\psi$ with the **Dirac adjoint** $\bar{\psi} = \psi^\dagger\gamma^0$. The factor $\gamma^0$ is a Clifford-**odd** element; it is not in the even subalgebra $\mathbb{C}\ell_{1,3}^+ \cong \mathbb{B}$, and it is exactly the extra ingredient that the biquaternion formulation needs to recover the four-component Dirac spinor from its pair of Weyl spinors. A bilinear formed only from $\tilde{\Psi}$ and $\tilde{\Psi}^\dagger$ inside $\mathbb{B}$ cannot supply it. The physical current therefore lies partly **outside** the algebra, and the pure-biquaternion form of the interaction current is not given by the naive product. That the electron's current is nevertheless an $\mathbb{M}_-$ four-vector — $\tilde{J} = ic\,j^0e_0 + \mathbf{j}$ with $j^0 = \psi^\dagger\psi$ — is a statement about the spinor-module transcription, not about a product in $\mathbb{B}$.

This is the same representation question as the left/right action of the previous sections, met from the current side. The parent Dirac article's open question flags the representation conventions; this article records that they are not idle. The biquaternion form of the conserved current, and the sense in which the sourced Maxwell equation $\tilde{\nabla}\tilde{F} = -\tilde{R}$ is fed by the Dirac field, remain open.

## Recovering the Standard Minimal Coupling

The construction meets the standard theory in the spinor-module transcription. The biquaternion field, viewed as an element of $\mathbb{B}\cong M_2(\mathbb{C})$, is a pair of two-component Weyl spinors, and the biquaternion gradient plays the role of the Dirac operator $\not\partial = \gamma^\mu\partial_\mu$ on the spinor module. Under that transcription, left multiplication by the connection $\tilde{A} = \sum_\mu A_\mu e_\mu$ is the representative of the matrix $\gamma^\mu A_\mu$, and the coupled biquaternion equation becomes the standard minimally coupled Dirac equation

$$
\left(i\hbar\gamma^\mu D_\mu - mc\right)\psi = 0, \qquad D_\mu = \partial_\mu + \frac{iq}{\hbar}A_\mu ,
$$

**provided the mass term is the linear Dirac mass** $m\psi$. With the linear mass the equation is gauge covariant in the standard way, the conserved current is $j^\mu = \bar{\psi}\gamma^\mu\psi$, and the standard consequences — the tree-level gyromagnetic factor $g = 2$, the correct non-relativistic limit, the magnetic moment — follow by the computations of the companion articles on the electron and on the solutions and non-relativistic limit. Those results are not repeated here; the point for this article is the contrast: they are obtained with a **linear** mass term, whereas the biquaternion equation as written by the parent has an antilinear one.

The transcription carries the representation conventions that the parent Dirac article explicitly left open — the identification of the biquaternion units with the gamma matrices, the placement of the two chiralities in the algebra, and the role of the Dirac adjoint. This article does not fix them. What it fixes is the biquaternion form of the coupling itself: the covariant derivative $D = \tilde{\nabla} + \frac{iq}{\hbar}\tilde{A}$ acting by left multiplication, the component operators $D_\mu = \partial_\mu + \frac{iq}{\hbar}A_\mu$, and the coupled equation $D\tilde{\Psi} = m\tilde{\Psi}^\flat$.

## What the Algebra Supplies and What It Only Transcribes

It is worth separating the two, because they are easily conflated.

**What the algebra supplies.**

- *A canonical abelian coupling.* The gauge group is the unitary part of the center, and the center is the only place a central phase can live. The $U(1)$ that minimal coupling gauges is attached to the algebra without a choice of representation, as the gauge principle article establishes.
- *The covariant derivative as the localization of the phase.* The interaction term $\frac{iq}{\hbar}\tilde{A}\tilde{\Psi}$ is not added by hand: it is the term the localized phase forces, and the connection it forces is exactly the potential biquaternion of the Maxwell article.
- *Exact covariance of the massless coupled equation*, with the component operators $D_\mu$ and the phase law $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ inherited unchanged.
- *A material-sector connection.* For a real gauge function the connection stays in $\mathbb{M}_-$, so the coupling respects the sector decomposition the framework is built on.

**What it only transcribes.**

- *The minimal-coupling principle itself.* The derivation is the standard global-to-local argument carried into the biquaternion algebra. The algebra supplies a home for it and makes the component structure transparent; it does not supply a reason for the gauge field to exist.
- *The value of the coupling.* The charge $q$ is a parameter; the algebra does not fix it.
- *The standard spinor-module results.* The conserved current, the non-relativistic limit, and $g=2$ are properties of the Dirac equation the framework contains, obtained with the linear mass term on the spinor module; the framework transcribes them.

**What is interpretation.** Reading the coupled equation as a Dirac field propagating in a background connection is a geometric interpretation. The algebraic content is the transformation law, the covariance of the massless equation, and the explicit component form; the bundle picture is a consistent reading of that content, as in the gauge principle article.

## Open Questions

1. **The massive sector.** Is the parent's antilinear mass term a Majorana-type coupling, in which case the continuously charged massive field is genuinely absent and only the massless sector carries electromagnetism? Or is it the real-form expression of a linear Dirac mass, in which case the physical coupling is the standard spinor-module one and the antilinear algebra-level equation is not the charged equation? The two readings are inequivalent and change the conclusion about the charged massive field.

2. **The matter representation.** The gauge principle produces a left-action covariant derivative; a right-action mirror is equally covariant, and the mixed insertion is not. Which action — which spinor module — is the physical Dirac field in? What fixes it inside the algebra?

3. **The interaction current.** The naive gauge-invariant bilinear $i\tilde{\Psi}\tilde{\Psi}^\dagger$ is in $\mathbb{M}_-$ but is not conserved. The physical current uses the Clifford-odd $\gamma^0$, outside $\mathbb{B}$. Is there a biquaternion-natural current, perhaps on a restricted module, or is the current irreducibly a representation-level object?

4. **The sourced system.** How does the Dirac current feed the biquaternionic Maxwell equation $\tilde{\nabla}\tilde{F} = -\tilde{R}$, and does the coupled system close on the algebra or require the spinor module? The integrability condition $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{R}) = 0$ must be recovered from the current.

5. **The shared generator.** The internal phase $e^{iq\Gamma/\hbar}$ and the complex time coordinate $ict$ both use the single element $i$ of $\mathbb{B}$. Is this identification content-bearing, or vacuous because the phase is central? (The gauge principle article's open question.)

6. **The non-abelian extension.** When the connection becomes $\mathbb{B}$-valued, the field must be placed in a representation of the gauge group and the left/right question becomes sharp. The planned companions on the covariant derivative, non-abelian fields, and Yang–Mills must settle it.

7. **Empirical content.** As everywhere in the framework, the unresolved question is whether any of this yields a prediction distinguishing it from standard gauge theory. The minimal coupling as presented is a reformulation; the framework-level question of empirical contact remains open.

## Summary

The minimal coupling of the biquaternion Dirac field to electromagnetism is the replacement of the gradient by the covariant derivative of the gauge principle,

$$
D = \tilde{\nabla} + \frac{iq}{\hbar}\tilde{A}, \qquad D_\mu = \partial_\mu + \frac{iq}{\hbar}A_\mu,
$$

acting by left multiplication on the field. The coupled equation is

$$
D\tilde{\Psi} = m\tilde{\Psi}^\flat, \qquad \tilde{\nabla}\tilde{\Psi} + \frac{iq}{\hbar}\tilde{A}\tilde{\Psi} = m\tilde{\Psi}^\flat,
$$

with the interaction term $\frac{iq}{\hbar}\tilde{A}\tilde{\Psi}$ that the localized central phase forces, and the massless case $D\tilde{\Psi} = 0$.

The **massless** coupled equation is exactly gauge covariant: with $\tilde{\Psi}' = e^{iq\Gamma/\hbar}\tilde{\Psi}$ and $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$, one has $D'\tilde{\Psi}' = \lambda D\tilde{\Psi}$, so $D\tilde{\Psi} = 0$ holds in every gauge when it holds in one. The **massive** coupled equation is not: the mass term is antilinear, $(\lambda\tilde{\Psi})^\flat = \lambda^{*}\tilde{\Psi}^\flat$, so the transformed mass term acquires the factor $e^{2iq\Gamma/\hbar}$ and the equation is form-invariant only for a constant phase with $\lambda = \pm 1$. The continuous $U(1)$ of the massless theory is broken to a discrete $\mathbb{Z}_2$ by the mass term. This is the biquaternion form of the statement that a Majorana-type mass term is incompatible with a gauged continuous $U(1)$; the standard linear Dirac mass does not have this obstruction, and on the spinor module the standard minimal coupling is recovered.

The interaction current is not a pure biquaternion product. The gauge-invariant, material-sector bilinear $i\tilde{\Psi}\tilde{\Psi}^\dagger$ is not conserved on solutions of the massless equation; the physical current is the spinor-module $j^\mu = \bar{\psi}\gamma^\mu\psi$, whose Dirac adjoint uses the Clifford-odd $\gamma^0$ outside $\mathbb{B}$. The pure-biquaternion form of the current, and the closure of the sourced system, are left as open questions, together with the choice of the left or right matter representation and the meaning of the massive sector.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ | Center of the algebra; source of the abelian gauge group |
| $\tilde{\nabla} = e_0\partial_{ict} + e_k\partial_k$ | Biquaternionic gradient (Dirac operator) |
| $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_k\partial_k$ | Quaternion-conjugate gradient |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla}$ | d'Alembertian |
| $\tilde{\Psi}$ | Biquaternion Dirac field |
| $\tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger$, $\tilde{\Psi}^\dagger = \bar{\tilde{\Psi}}^{\,*}$ | Anti-Hermitian conjugate of the field |
| $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat$ | Free biquaternion Dirac equation |
| $\tilde{A} = i\phi/c\,e_0 + \mathbf{A}$ | Connection = potential biquaternion (in $\mathbb{M}_-$) |
| $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ | Gauge transformation of the connection |
| $\lambda = e^{iq\Gamma/\hbar}$ | Local central phase; $\Gamma$ real scalar |
| $q$ | Charge (coupling constant), not fixed by the algebra |
| $D = \tilde{\nabla} + \frac{iq}{\hbar}\tilde{A}$ | Covariant derivative (left action) |
| $D_\mu = \partial_\mu + \frac{iq}{\hbar}A_\mu$ | Components; $\partial_0 = \partial_{ict}$ |
| $D\tilde{\Psi} = m\tilde{\Psi}^\flat$ | Minimally coupled Dirac equation |
| $\frac{iq}{\hbar}\tilde{A}\tilde{\Psi}$ | Interaction term |
| $e^{2iq\Gamma/\hbar}$ | Phase acquired by the mass term under a local phase |
| $\tilde{J} = i\tilde{\Psi}\tilde{\Psi}^\dagger$ | Naive bilinear; gauge invariant, in $\mathbb{M}_-$, **not conserved** |
| $j^\mu = \bar{\psi}\gamma^\mu\psi$, $\bar{\psi} = \psi^\dagger\gamma^0$ | Spinor-module conserved current (involves the Clifford-odd $\gamma^0$) |
| $\tilde{R} = \frac{i\rho}{\sqrt{\epsilon}}e_0 + \sqrt{\mu}\,\mathbf{J}$ | Maxwell source biquaternion |
| $\tilde{\nabla}\tilde{F} = -\tilde{R}$ | Biquaternionic Maxwell equation |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace pairing of the informational sector |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original equation and the minimal coupling.
- Hermann Weyl, "Elektron und Gravitation," *Zeitschrift für Physik* **56** (1929) 330–352, for the origin of the local phase and the gauge principle.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard treatment of minimal coupling, the conserved current, and the non-relativistic limit.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), and S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the standard abelian and non-abelian gauge couplings.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Majorana and Dirac mass terms and the fermion-number symmetry.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of the biquaternion algebra with the even part of $\mathrm{Cl}_{1,3}$ and the relation of $\gamma^0$ to the even subalgebra.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the gauge-theoretic reading of the covariant derivative in geometric algebra.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of the Dirac equation in spacetime algebra.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component spinor calculus and the Dirac adjoint.
- Companion articles: *The Gauge Principle in Biquaternionic Form*; *Maxwell's Equations in the Biquaternionic Form*; *The Dirac Equation in Biquaternionic Form*; *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit*; *The Electron in Biquaternionic Form*; *Canonical Quantization of the Biquaternion Dirac Field*; *Canonical Quantization of the Biquaternion Maxwell Field*; *$\mathbb{M}_-$ as the Material Space*; *$\mathbb{M}_+$ as the Informational Space*.
