# __Interpretation of the Wick Rotation in the Biquaternion Universe__

## Introduction

The **Wick rotation** is a computational procedure used throughout quantum field theory, statistical mechanics, and condensed-matter physics. It consists of the analytic continuation $r'_t \to -i\tau$ of the time coordinate to imaginary values, and it converts the oscillating phase of the Feynman path integral into a decaying exponential. The procedure is usually presented as a **trick**: it is justified by analytic continuation of the integrand in the complex time plane, it works for a large class of physically relevant problems, and it fails for others.

This article proposes a structural interpretation of the Wick rotation, in terms of the biquaternion algebra. The main observation is the following: the Wick rotation, in the $i r'_t$ convention, sends the imaginary time coefficient $i r'_t$ to the real value $c\tau$, while leaving the spatial coordinates $r_x, r_y, r_z$ unchanged. The result is a point of the **quaternion subspace** $\mathbb{B}_{H}$, whose four coefficients are all real. So the Wick rotation is a **change of real slice**. It replaces the reality condition of the material sector by the reality condition of $\mathbb{B}_{H}$, on one and the same complexified field. It is not a map of algebras from $\mathbb{B}_{\Phi}$ to $\mathbb{B}_{H}$, and no such map exists.

This interpretation explains, in a single structural fact, when the procedure is available and when it is not. The two subspaces are the fixed spaces of two conjugate-linear involutions of the one algebra, related by a time reflection. The rotation is a square root of that reflection, the root that fixes the three spatial coefficients up to the sign of $i$ in the time slot. A quantity crosses from one slice to the other when it is analytic across the deformation, and it fails to cross when the deformation meets a pole or a branch cut. The compactness of the slice is the reason the rotated problem is easier: a definite norm gives no zero divisors, a division algebra, an elliptic operator and a compact group in one stroke.

The article is organized as follows. First the three subspaces involved in the rotation are recalled: the quaternion subspace $\mathbb{B}_{H}$, the informational sector $\mathbb{B}_{\Psi}$, and the material sector $\mathbb{B}_{\Phi}$. Then the standard Wick rotation is recalled, and its action on the coordinates is written explicitly. Then the two reality conditions are written, and the rotation is read as a square root of the time reflection between them. Then the interpretation is applied to the standard applications of the Wick rotation, and a split is proposed between applications that transfer harmlessly and applications that resist. The article closes with the status of the interpretation.

Throughout, $c$ denotes the speed of light in the medium, and the biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$.

## The Three Subspaces of $\mathbb{B}$

The biquaternion algebra $\mathbb{B}$ is cut into remarkable real subspaces: the two-dimensional centre $\mathbb{B}_{C}$, the six-dimensional vector subspace $\mathbb{B}_{V}$, and the four four-dimensional ones — the quaternion subspace $\mathbb{B}_{H}$, the anti-quaternion subspace $\mathbb{B}_{iH}$, the informational sector $\mathbb{B}_{\Psi}$ and the material sector $\mathbb{B}_{\Phi}$. Three of the four-dimensional subspaces are involved in the Wick rotation and are recalled here. All three are real vector spaces of dimension 4, and all three are subspaces of the same algebra.

**The quaternion subspace $\mathbb{B}_{H}$.** An element has the form

$$
\tilde{Q} = q_t\, e_t + q_x\, \vec e_x + q_y\, \vec e_y + q_z\, \vec e_z = (h_t)\, e_t + r_x\, \vec e_x + r_y\, \vec e_y + r_z\, \vec e_z, \qquad q_t, q_x, q_y, q_z \in \mathbb{R}.
$$

Here the time parameter is real, $h_t$, and $\tau$ is its value on the rotated point. All four coefficients are **real**. The quadratic form

$$
\langle\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = q_t^2 + q_x^2 + q_y^2 + q_z^2
$$

has signature $(4, 0)$. The subspace is a subalgebra of $\mathbb{B}$ isomorphic to the quaternion algebra $\mathbb{H}$, and it is a division algebra: every nonzero element is invertible, and there are no zero divisors.

**The material sector $\mathbb{B}_{\Phi}$.** An element has the form

$$
\tilde R_\Phi = i r'_t\, e_t + r_x\, \vec e_x + r_y\, \vec e_y + r_z\, \vec e_z, \qquad r'_t, r_x, r_y, r_z \in \mathbb{R}.
$$

The first coefficient is **imaginary**, the three remaining coefficients are **real**. The quadratic form

$$
\langle\tilde R_\Phi\rangle_{\natural} = -c^2(r'_t)^2 + r_x^2 + r_y^2 + r_z^2
$$

has signature $(3, 1)$. The subspace is not a subalgebra, and it contains a three-dimensional cone of zero divisors.

**The informational sector $\mathbb{B}_{\Psi}$.** An element has the form

$$
\tilde H_\Psi = h_t\, e_t + i h'_x\, \vec e_x + i h'_y\, \vec e_y + i h'_z\, \vec e_z, \qquad h_t, h'_x, h'_y, h'_z \in \mathbb{R}.
$$

The first coefficient is **real**, the three remaining coefficients are **imaginary**. The quadratic form

$$
\langle\tilde H_\Psi\rangle_{\natural} = h_t^2 - (h'_x)^2 - (h'_y)^2 - (h'_z)^2
$$

has signature $(1, 3)$, the mirror image of the signature on $\mathbb{B}_{\Phi}$.

The three subspaces are distinct, and each has its own algebraic and analytic character. The specific form of the differential operators on each subspace — the gradient, the d'Alembertian, and the square of the gradient — has been developed in the companion articles on the biquaternion analysis.

## The Standard Wick Rotation

In relativistic field theory, a point of the material sector is written

$$
\tilde R_\Phi = i r'_t\, e_t + r_x\, \vec e_x + r_y\, \vec e_y + r_z\, \vec e_z \in \mathbb{B}_{\Phi},
$$

where $r'_t$ is the time coordinate and $r_x, r_y, r_z$ the spatial ones, so that the four coefficients are $i r'_t, r_x, r_y, r_z$.

The **standard Wick rotation** is the substitution

$$
r'_t \;\longmapsto\; -i\tau, \qquad \tau \in \mathbb{R},
$$

in the time coordinate. Under this substitution, the first coefficient of $\tilde{R}_\Phi$ changes as

$$
\boxed{\;i r'_t \;\longmapsto\; i c\,(-i\tau) = c\tau\;},
$$

while the spatial coefficients $r_x, r_y, r_z$ are unchanged. The rotated point is

$$
\tilde{Q}_\mathbb{H} = c\tau\, e_t + r_x\, \vec e_x + r_y\, \vec e_y + r_z\, \vec e_z,
$$

with **all four coefficients real**. In the notation of the quaternion subspace these are the four parameters $q_t = c\tau$, $q_x = r_x$, $q_y = r_y$, $q_z = r_z$.

So the standard Wick rotation acts on the coefficient tuple by the linear map

$$
W=\mathrm{diag}(-i,\,1,\,1,\,1),\qquad W(i r'_t,\ r_x,\ r_y,\ r_z)=(r'_t,\ r_x,\ r_y,\ r_z)=(c\tau,\ r_x,\ r_y,\ r_z),
$$

with $\tau=r'_t$ the parameter of the image. The map multiplies the time coefficient by $-i$ and fixes the three spatial ones. It is $\mathbb{C}$-linear and bijective, and it is not a ring map. It carries $\mathbb{B}_{\Phi}$ onto $\mathbb{B}_{H}$ coefficient by coefficient, and it is not an isometry: the quadratic form changes sign in the time–time component, and the signature changes from $(3, 1)$ to $(4, 0)$.

**Two operations carry the name, and the algebra tells them apart.** The substitution $r'_t\mapsto-i\tau$ is a rotation of the contour. It takes the material coordinate off the real axis, and at $\tau$ real the source point has $r'_t=-i\tau$ with time coefficient $c\tau$, which is real, so the source is not a point of $\mathbb{B}_{\Phi}$ at all. The relabelling $i r'_t\mapsto c\tau$ is a different operation: it multiplies the time coefficient by $-i$, produces the real coefficient $r'_t$, and has $\tau=r'_t$. That operation is the map $W$. It is a bijection of $\mathbb{B}_{\Phi}$ onto $\mathbb{B}_{H}$ and it is the one this article reads. The first is the device of the calculation; the second is the change of reality condition.

**The two subspaces are two reality conditions on one algebra.** Each is the fixed space of a conjugate-linear involution of $\mathbb{B}$:

$$
\mathbb{B}_{H}=\{\tilde Q:\ \bar{\tilde Q}=\tilde Q\},\qquad \mathbb{B}_{\Phi}=\{\tilde Q:\ \tilde Q^{\flat}=\tilde Q\}.
$$

Both involutions are exact, and $W$ carries each fixed space onto the other. With $T=\mathrm{diag}(-1,1,1,1)$ the time reflection,

$$
\boxed{\;\flat=\bar{\cdot}\circ T,\qquad W^{2}=T,\qquad \text{hence}\qquad \flat=\bar{\cdot}\circ W^{2}.\;}
$$

So the Wick rotation is a **square root of the reflection that separates the two reality conditions**. The bijection between the two subspaces is $W$; the reflection is $W^{2}=T$; and the passage from one reality condition to the other is $\flat=\bar{\cdot}\circ W^{2}$, one reflection and one complex conjugation. The rotation is half of that passage.

**The two reality conditions are not of the same kind.** $\mathbb{B}_{H}$ is a real form of $\mathbb{B}$ as an algebra: it is closed under multiplication, and $\mathbb{B}_{H}\otimes_{\mathbb{R}}\mathbb{C}=\mathbb{B}$. $\mathbb{B}_{\Phi}$ is a real form of the underlying vector space only. It is not closed under multiplication, because $i e_t$ and $\vec e_x$ commute and their product is $i\vec e_x$, which lies outside $\mathbb{B}_{\Phi}$. The asymmetry is why no ring map carries one onto the other: $\mathbb{B}\cong M_2(\mathbb{C})$ is simple of real dimension eight, and $\mathbb{H}$ has real dimension four.

## The Procedure Read as a Change of Real Slice

The standard Wick rotation is used to convert oscillatory integrals into convergent ones. The Lorentzian path integral

$$
Z = \int  \mathcal{D}\xi\; \exp(iS[\xi]/\hbar)
$$

has an oscillating integrand, and it is not absolutely convergent. After the Wick rotation, the path integral becomes

$$
Z_E = \int  \mathcal{D}\xi\; \exp(-S_E[\xi]/\hbar),
$$

with a decaying integrand, and it is convergent (at least formally). The basis of the procedure is that the wave operator of the Lorentzian formulation, $-\partial^2/\partial {r'_{t}}^2 + \Delta_\Phi$, becomes the Euclidean Laplacian $\partial^2/\partial \tau^2/c^2 + \Delta$, which is elliptic and well behaved.

In the biquaternion interpretation, the operation is the following. The Lorentzian field $\xi$ on $\mathbb{B}_{\Phi}$ is continued to a field on $\mathbb{B}_{H}$ by the substitution $i r'_t \mapsto c\tau$. The d'Alembertian, read on the material sector, is

$$
\Box_\Phi = \Delta_\Phi - \frac{\partial^2}{\partial {r'_{t}}^2},
$$

and the same operator, read on the real coordinates of $\mathbb{B}_{H}$, is

$$
\boxed{\;\Box = \frac{1}{c^2}\frac{\partial^2}{\partial \tau^2} + \Delta\;}.
$$

The oscillating phase $\exp(iS)$ becomes the decaying exponential $\exp(-S_E)$, where $S_E$ is the action of the continued field. This is the standard procedure, expressed in the biquaternion framework as a change of the reality condition on one field.

So the Wick rotation is a **change of real slice**: it is available where the deformation of the coefficient crosses no singularity, and it is unavailable where one is crossed. Its biquaternion content is that $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{H}$ are the two real structures of one algebra, related by $W^{2}=T$. The change is not an artefact of the calculation, and a medium can produce it: when $\epsilon\mu<0$ the scale $c^2=1/(\epsilon\mu)$ is negative, the interval takes the signature $(4,0)$, and the imaginary time direction becomes real (*The Effective Optical Metric of the Local Complex Structure*).

## Why the Change Works: the Properties of $\mathbb{B}_{H}$

The reason the change is useful is that $\mathbb{B}_{H}$ is the compact real slice and $\mathbb{B}_{\Phi}$ is not. The first five rows of the table below are five names for that one fact.

| Property | $\mathbb{B}_{H}$ | $\mathbb{B}_{\Phi}$ |
|---|---|---|
| Signature of the quadratic form | $(4, 0)$ positive-definite | $(3, 1)$ indefinite |
| d'Alembertian | $\partial^2/\partial \tau^2/c^2 + \Delta$ (elliptic) | $-\partial^2/\partial {r'_{t}}^2 + \Delta_\Phi$ (hyperbolic) |
| Zero divisors | None | Light cone |
| Division algebra | Yes | No |
| Symmetry group | $SO(4)$, compact | $SO(3, 1)$, non-compact |
| Analytic theory | Fueter quaternionic analysis | Lorentzian Clifford analysis |

The quaternion subspace is elliptic, has no zero divisors, is a division algebra, and admits a compact symmetry group. The material sector is hyperbolic, has a light cone of zero divisors, is not a division algebra, and has a non-compact symmetry group. The elliptic character of $\mathbb{B}_{H}$ is what makes the continued problem tractable: the elliptic Laplacian has a well-behaved fundamental solution, a Cauchy integral formula, a maximum principle, and a mean-value property, all of which are properties of elliptic operators and not of hyperbolic ones.

The rows are not independent. A finite-dimensional real algebra whose norm is positive definite has no zero divisors, so it is a division algebra; its gradient is elliptic, and its group of linear isometries is compact. Each row on the right of the table is the indefiniteness of the material form read once more. The one exception is the last row, which is a statement about the literature and not about the algebra: the analysis of a definite slice is Fueter's and the analysis of an indefinite one is the Lorentzian Clifford calculus.

The passage from $\mathbb{B}_{\Phi}$ to $\mathbb{B}_{H}$ therefore replaces a problem in an indefinite setting by a problem in a definite one. The definite problem is easier: it has fewer pathologies, it has more structure, and its solutions behave better at infinity.

## Why the Change Sometimes Fails

The same passage also removes part of the structure. The Lorentzian structure of $\mathbb{B}_{\Phi}$ — the light cone, the causal ordering of events, the phase $\exp(i\theta_{\mathrm{act}})$ with its specific oscillation — is not preserved by the passage to $\mathbb{B}_{H}$. The signs are changed: the quadratic form becomes positive-definite, the hyperbolic operator becomes elliptic, the light cone disappears, because there are no zero divisors on $\mathbb{B}_{H}$.

Throughout this article $\theta_{\mathrm{act}}:=\mathrm{Re}\,S/\hbar$ is the angle of the action: it is real whenever the action is real, and it is the angle the wave form carries. The weight $\kappa_{\mathrm{act}}:=-\mathrm{Im}\,S/\hbar$ accompanies it, zero for a real action and positive for a decaying amplitude, so that $\exp(iS/\hbar)=\exp(i\theta_{\mathrm{act}})\exp(-\kappa_{\mathrm{act}})$. A complex action carries both factors; a real action carries the angle alone.

The two slices carry different reality conditions on one complexified quantity, so a quantity must be continued and not carried over. The continuation exists exactly when the deformation of the coefficient crosses no singularity of the continued quantity: no pole and no branch cut in the strip it sweeps. This is the reason the Wick rotation sometimes fails, and the failure is a statement about the analyticity of the quantity, not about the difficulty of the calculation. A free field is continued exactly, and interacting theories fail where the deformation meets the singularities of the continued Green function.

The two facts — that the change is useful and that it can fail — are one fact seen twice. The definite slice is easier precisely because it is a different reality condition on the same quantity. Both statements are read off the single identity $\flat=\bar{\cdot}\circ W^{2}$: the operator $W^{2}$ is what separates the two conditions, and the operator $W$ is the square root of it.

## A Classification: Which Applications Transfer, Which Resist

The interpretation above suggests a classification of the applications of the Wick rotation by whether the physics of the problem depends on the Lorentzian structure or not. The criterion is the analyticity of the continued quantity, and in practice the two agree: the cases that fail are the ones whose continuation meets a singularity in the strip.

**Applications that are essentially insensitive to the Lorentzian structure** (and therefore transfer harmlessly to $\mathbb{B}_{H}$):

- The Euclidean path integral, in its role as a generating functional of correlation functions.
- Finite-temperature field theory, in its equilibrium aspects: the Matsubara formalism and the thermal partition function.
- Lattice gauge theory, in its static and equilibrium computations.
- The correspondence between quantum field theory and statistical mechanics, as a formal identity of partition functions.
- Stochastic quantization, as a stochastic process on the Euclidean sector.

**Applications that are essentially sensitive to the Lorentzian structure** (and therefore transfer problematically to $\mathbb{B}_{H}$):

- Real-time dynamics: transport coefficients, relaxation, response functions.
- Massless-particle physics, where the light cone is essential.
- Non-equilibrium systems, which require real-time methods.
- The sign problem in finite-density QCD, where the complex phase cannot be projected out by the transfer.
- Quantum gravity, where the Euclidean action is unbounded below.
- Any process in which the causal ordering of events matters.

**The map is exact on the time axis.** On a translation in $r'_t$ it is the analytic continuation $r'_t\mapsto-i\tau$, and on the central phase it turns the oscillation into a real exponential. On the three spatial axes it multiplies the coefficient by $-i$, so it is not the identity there. A rotor is not fixed: an element such as $\cos\frac{\theta_{\mathrm{axr}}}{2}e_t+\sin\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}$ has a real scalar coefficient, and the map sends it to an imaginary one.

The product is not carried over, and the cause is not non-commutativity. It is that $W$ is $\mathbb{C}$-linear and not a ring map. A witness with commuting factors: $i e_t$ and $\vec e_x$ commute, their product is $i\vec e_x$, and $W$ sends it to $\vec e_x$, which is not $W(ie_t)W(\vec e_x)=e_t\vec e_x$.

Two continuations must be kept apart here. Continuing a parameter inside an analytic expression is multiplicative, by the identity theorem, so the continued polar word $e^{i\tilde{Ξ}\vec u_{\mathrm b}/2}e^{\theta_{\mathrm{axr}}\vec u_{\mathrm r}/2}$ at $\tilde{Ξ}\mapsto i\tilde{Ξ}$ is the word of the continued factors: the boost goes to a real rotor, because $\cosh$ and $\sinh$ of an imaginary rapidity are $\cos$ and $-\sin$, and the rotor $\tilde u_{\mathrm r}$ is untouched. The coefficient map $W$ is a different operation, and it is the one that fails. That is the BCH defect of *The Exponential Word and Its Boundary*.

The split is not exact; some applications lie between the two lists. But the general pattern is as follows: whenever a problem is genuinely about **correlations and equilibrium**, the passage to $\mathbb{B}_{H}$ is harmless; whenever a problem is genuinely about **causality and dynamics**, the passage destroys what the problem was about.

**The strongest objection.** On the first list, the rotated computation often has a rival that never leaves $\mathbb{B}_{\Phi}$. The Matsubara formalism is reached with the Hermitian form carrying the positivity, and the thermal circle is the compactified material direction (*The Matsubara Thermal Formalism in Biquaternionic Form*; *The KMS Condition and the Biquaternion Framework*). Where that route exists, the change of slice is convenient and not necessary. The rival supports the reading rather than weakening it: a quantity that is analytic across the deformation can be evaluated on either slice, and the material slice is one of them. What the rival rules out is the claim that the thermal results are evidence for the rotation; they are evidence that the continuation is available.

The split is observed in practice. The successful uses (lattice computations of equilibrium quantities, finite-temperature partition functions, instanton calculus) are all in the first list. The persistent difficulties (sign problem, real-time dynamics, quantum gravity) are all in the second list, and each of them is a failure of analyticity in the strip: a complex phase that cannot be reached, a real-time contour that meets the poles of the propagator, an action unbounded below so that the continued weight does not decay. The reading as a change of reality condition accounts for this pattern.

## Status of the Reading

The interpretation of the Wick rotation as a change of real slice is an **interpretation**, not an established result. What is established is the following.

- The biquaternion algebra contains four natural four-dimensional real subspaces: $\mathbb{B}_{H}$, $\mathbb{B}_{iH}$, $\mathbb{B}_{\Psi}$, and $\mathbb{B}_{\Phi}$. Three of them — $\mathbb{B}_{H}$, $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ — are involved in the Wick rotation.
- The three subspaces have distinct signatures: $(4, 0)$, $(1, 3)$, $(3, 1)$.
- $\mathbb{B}_{H}$ and $\mathbb{B}_{\Phi}$ are the fixed spaces of the conjugate-linear involutions $\bar{\cdot}$ and $\flat$, and $\flat=\bar{\cdot}\circ T$ with $W^{2}=T$.
- The standard Wick rotation acts on a point of $\mathbb{B}_{\Phi}$ by the coefficient map $W=\mathrm{diag}(-i,1,1,1)$, which sends the imaginary coefficient $i r'_t$ to the real $c\tau$ and leaves the spatial coefficients unchanged.
- The resulting point lies in $\mathbb{B}_{H}$.
- The map is $\mathbb{C}$-linear, bijective and not a ring map; $\mathbb{B}_{H}$ is closed under multiplication and $\mathbb{B}_{\Phi}$ is not.

What is an **interpretation** is the following.

- That the standard Wick rotation is best read as the change of reality condition $\flat\to\bar{\cdot}$, with $W$ a square root of the reflection between them.
- That the usefulness of the change is explained by $\mathbb{B}_{H}$ being the compact real slice.
- That the failure of the change is explained by the analyticity of the continued quantity in the strip swept by the deformation.
- That the split of applications into "harmless" and "resisting" follows from the two slices being different reality conditions on one quantity.

The interpretation is consistent with the known behaviour of the Wick rotation. It is not derived from established physics, and it does not constitute a prediction of new physics. It is a structural interpretation that clarifies the operation and organizes the applications.

## Summary

The standard Wick rotation is the analytic continuation $r'_t \to -i\tau$ of the time coordinate, which converts the Lorentzian structure of spacetime into a Euclidean one and turns the oscillating phase of the Feynman path integral into a decaying exponential. It is usually presented as a trick.

In the biquaternion framework, the standard Wick rotation is the coefficient map $W=\mathrm{diag}(-i,1,1,1)$, which sends the imaginary coefficient $i r'_t$ to the real coefficient $c\tau$ and leaves the spatial coefficients $r_x, r_y, r_z$ unchanged. The material sector $\mathbb{B}_{\Phi}$ and the quaternion subspace $\mathbb{B}_{H}$ are two reality conditions on one algebra: each is the fixed space of a conjugate-linear involution, and $\flat=\bar{\cdot}\circ T$ with $W^{2}=T$. The rotation is a square root of the time reflection that separates the two conditions, the root that fixes the three spatial coefficients up to the sign of $i$ in the time slot, and it is not a map of algebras between them.

The quaternion subspace $\mathbb{B}_{H}$ is the compact real slice: its quadratic form is positive-definite, it has no zero divisors, it is a division algebra, its d'Alembertian is elliptic, and its isometry group is compact. Those are one property under five names. The change is useful because the continued problem on the compact slice is easier than the original problem on the indefinite one.

The passage also changes the object: the light cone, the causal ordering and the phase belong to $\mathbb{B}_{\Phi}$ and not to $\mathbb{B}_{H}$. A quantity therefore has to be continued and not carried over, and the continuation is available exactly where the deformation of the coefficient meets no pole and no branch cut. The usefulness of the change and the possibility of its failure are one fact, read off $W^{2}=T$.

The interpretation organizes the applications into a split between those that transfer harmlessly to $\mathbb{B}_{H}$ (equilibrium, correlation, statistical) and those that resist (real-time dynamics, causal propagation, massless particles, the sign problem, quantum gravity). The split is observed in practice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{B}_{C}$, $\mathbb{B}_{V}$, $\mathbb{B}_{iH}$ | The centre, the vector subspace, and the remaining four-dimensional subspace; not involved in the Wick rotation |
| $\mathbb{B}_{H}$ | Quaternion subspace: signature $(4, 0)$, elliptic |
| $\mathbb{B}_{\Psi}$ | Informational sector: signature $(1, 3)$, mirror hyperbolic |
| $\mathbb{B}_{\Phi}$ | Material sector: signature $(3, 1)$, hyperbolic |
| $q_t, q_x, q_y, q_z$ | Real parameters on $\mathbb{B}_{H}$, on $e_t, \vec e_x, \vec e_y, \vec e_z$; the rotated point has $q_t = c\tau$ |
| $(h_t)\,e_t + r_x\,\vec e_x + r_y\,\vec e_y + r_z\,\vec e_z$ | The same element in physical coordinates; $q_t = h_t$ and $(q_x,q_y,q_z)=(r_x,r_y,r_z)$ |
| $r'_t, r_x, r_y, r_z$ | Real parameters on $\mathbb{B}_{\Phi}$, on $ie_t, \vec e_x, \vec e_y, \vec e_z$ |
| $h_t, h'_x, h'_y, h'_z$ | Real parameters on $\mathbb{B}_{\Psi}$, on $e_t, i\vec e_x, i\vec e_y, i\vec e_z$ |
| $c$ | Speed of light in the medium |
| $r'_t$ | Time coordinate on $\mathbb{B}_{\Phi}$ |
| $\tau$ | Euclidean coordinate on $\mathbb{B}_{H}$ |
| $i r'_t$ | Imaginary time coefficient on $\mathbb{B}_{\Phi}$ |
| $r'_t \to -i\tau$ | Standard Wick rotation |
| $W=\mathrm{diag}(-i,1,1,1)$ | The coefficient map of the rotation: the time coefficient times $-i$, the three space coefficients fixed |
| $T=\mathrm{diag}(-1,1,1,1)$ | The time reflection; $W^{2}=T$, so $\flat=\bar{\cdot}\circ W^{2}$ |
| $\bar{\cdot}$, $\flat$ | The conjugate-linear involutions whose fixed spaces are $\mathbb{B}_{H}$ and $\mathbb{B}_{\Phi}$ |

## Further Reading

- G. C. Wick, "Properties of Bethe-Salpeter wave functions," *Physical Review* **96** (1954) 1124–1134, for the original introduction of the standard Wick rotation.
- J. Schwinger, "On the Euclidean structure of relativistic field theory," *Proceedings of the National Academy of Sciences* **44** (1958) 956–965, for the Euclidean formulation of field theory.
- J. Glimm and A. Jaffe, *Quantum Physics: A Functional Integral Point of View* (Springer, 1987), for the rigorous Euclidean approach to constructive quantum field theory.
- K. Osterwalder and R. Schrader, "Axioms for Euclidean Green's functions," *Communications in Mathematical Physics* **31** (1973) 83–112, for the reconstruction of the Lorentzian theory from the Euclidean one, which is the warrant for reading the two slices as one continued quantity.
- M. Le Bellac, *Thermal Field Theory* (Cambridge, 1996), for the finite-temperature imaginary-time formalism.
- M. Creutz, *Quarks, Gluons and Lattices* (Cambridge, 1983), for lattice gauge theory.
- A. M. Polyakov, *Gauge Fields and Strings* (Harwood, 1987), for instantons and non-perturbative effects.
- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934–35) 307–330, for the elliptic quaternionic analysis of the subspace $\mathbb{B}_{H}$.
- Roger Penrose, *The Road to Reality* (Knopf, 2004), Chapters 18 and 33, for the complex structure of spacetime.
- V. V. Kassandrov, "Urusovskii's Geometry, Algebrodynamics and Universal Quantum-like Kinematics in Complex Space", arXiv:1209.2377 [physics.gen-ph] (2012), for an arrival at the same two-subspace split from kinematics, with the priority reversed: there the physical half is $\mathbb{B}_{H}$ and the Lorentzian sector is the derived one, which is the reverse of this article's reading. The comparison is drawn in *The SO(4) Route to the Euclidean Frame*.
- Companion articles: [The SO(4) Route to the Euclidean Frame](the-so4-route-to-the-euclidean-frame-an-alternative-to-the-imaginary-time-coordinate.html), for the second route to a Euclidean frame and the comparison with this reading; [The Biquaternion Space, the Group of Involutions and the Six Subspaces](the-biquaternion-space-the-group-of-involutions-and-the-six-subspaces.html), for the involutions whose fixed spaces are the subspaces used here; [Each Sector Is the Other's Clock](each-sector-is-the-others-clock-the-sector-exchange-as-relational-time.html), for the exchange that multiplies the whole element and is not this continuation; [The Effective Optical Metric of the Local Complex Structure](the-effective-optical-metric-of-the-local-complex-structure.html), for the medium in which $\epsilon\mu<0$ produces the change of slice.

---

