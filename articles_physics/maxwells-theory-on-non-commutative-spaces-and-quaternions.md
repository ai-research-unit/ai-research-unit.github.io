# __Maxwell's Theory on Non-Commutative Spaces and Quaternions__

## Introduction

This article records a short external programme, that of S. I. Kruglov as presented in *Maxwell's Theory on Non-Commutative Spaces and Quaternions* (arXiv:hep-th/0110059, 2001). The arena is different from the corpus's. The coordinates do not commute,

$$
[x^\mu,x^\nu] = i\theta^{\mu\nu},
$$

with $\theta^{\mu\nu}$ a constant antisymmetric tensor of dimension $(\text{length})^2$, and the product of fields is deformed by the Moyal star product that this commutator induces. Maxwell's theory is then re-derived on that arena and written in what the source calls **spin-tensor (quaternion) form**. Three results follow, and they are the reason the corpus records the paper.

The first is that the vacuum stops being linear. The source's Lagrangian carries $\theta$-corrections to the Maxwell Lagrangian, and when it is written in the form $D = E + d$, $H = B + h$ the corrections $d$ and $h$ are **non-linear in the fields**. The source's own interpretation is that the vacuum of electrodynamics on non-commutative spaces behaves "similar to a medium with complicated (non-linear) properties" — a medium, moreover, that still supports **plane waves**. This bears directly on *Electromagnetism in Media — The Local Complex Structure at Work*, which defines a medium by the **linear** constitutive relations $D=\epsilon E$, $B=\mu H$ and treats the vacuum as the $\epsilon=\mu=1$ limit: here the vacuum itself is the medium, and what varies is not a permittivity but the **non-linearity**.

The second is that **electric–magnetic duality is broken** by the deformation. The corpus's *Exercise: Duality Rotation and the Riemann–Silberstein Vector* establishes duality as an exact symmetry of the free, commutative Maxwell equations, and the corpus's *Electric–Magnetic Duality and the Modular Group in Biquaternionic Form* builds on that exactness. Kruglov's $\theta$-terms are not invariant under the duality rotation, so the deformation supplies the **converse statement**: a specific modification of the arena breaks duality. Duality thereby becomes a **diagnostic of the commutative, linear case** rather than a property of Maxwell's theory as such. This is the point that most directly addresses the corpus's *The Empirical Status of the Biquaternion Framework*, which names "a non-commutative spacetime" as one of the three routes by which the framework could acquire a new scale but records only that the route is undetermined: the paper shows **what that route does to Maxwell's theory**.

The third concerns the energy–momentum tensor. The canonical tensor the source constructs is conservative, but the **symmetric tensor obtained by varying the action with respect to the metric is not**, because the action is not a Lorentz scalar on the deformed arena — $\theta^{\mu\nu}$ is a fixed tensor and does not transform. That inverts a fact the corpus relies on whenever it improves a stress tensor by the Hilbert variation, and it is recorded here as a **definitional caution**: conservation of the metric-variation tensor is not automatic when the arena is deformed. Both tensors also have **non-zero trace**, which the source calls a **trace anomaly** — a *classical* trace anomaly, distinct from the quantum Weyl anomaly of *The Trace Anomaly in Biquaternionic Form*, and the article keeps the two apart.

Three conventions must be fixed at the start, so that nothing is carried across by mistake.

First, and most important, **"non-commutative" here does not mean the non-commutativity of the quaternion algebra.** The corpus's readers meet that every day; it is not the subject. Here the **coordinates** fail to commute, and the deformation acts on the algebra of functions on spacetime, through the star product. The quaternion algebra enters only as a **compact notation** for the resulting equations — the source realises it by Pauli matrices — and the source says so: the spin-tensor form is "equivalently the quaternion form as the quaternion algebra can be realized through the Pauli matrices." Nothing about the result follows from quaternions; the quaternion form is bookkeeping, and the corpus records it as such.

Second, the deformation is of the **Moyal** type — an algebra deformation, $\theta^{\mu\nu}$ a fixed background. It is not the **C-space** programme of Clifford-valued coordinates, which deforms the arena differently; the corpus holds that programme separately and the two must be compared, not merged. The mathematical side of the Moyal deformation is the star product of *Deformation Quantization*, and the classical limit that the corpus's *Similitudes between the Poisson Bracket and the Quantum Commutator* develops is the undeformed limit here.

Third, the source's arithmetic convention is the corpus's, with the imaginary unit placed in the time coordinate: the source writes $x_4 = it$, the corpus writes $\tilde Q = ict\,e_0 + \vec x$, and both make the temporal direction imaginary. The source writes the quaternion units $e_4 = 1$, $e_1,e_2,e_3$ with $e_k^2=-1$, and realises them by $\tau_4 = i\tau_0$, $\tau_k = i\sigma_k$; the corpus's units $e_0=1,e_1,e_2,e_3$ are the same objects with different names. Throughout, $c=\hbar=1$.

## The Non-Commutative Arena

### The commutator, the bound, and the deformation

The coordinates obey $[x^\mu,x^\nu]=i\theta^{\mu\nu}$ with $\theta^{\mu\nu}$ constant and antisymmetric, of dimension $(\text{length})^2$. Momentum commutes with itself and with position in the ordinary way, $[x^\mu,p^\nu]=i\hbar\delta^{\mu\nu}$, and the source parametrises the deformation by a scale,

$$
\theta^{\mu\nu} = \frac{1}{\Lambda_{NC}^2}\,\epsilon^{\mu\nu},
$$

with $\epsilon^{\mu\nu}$ dimensionless and antisymmetric and $\Lambda_{NC}\ge 10^{3}$ GeV the bound the source quotes. Two consequences are stated at once, because they shape everything that follows. The tensor $\theta^{\mu\nu}$ is **constant**, so it picks out a direction in the Lorentz group: **Lorentz invariance is broken** on the deformed arena. And because a constant $\theta$ can be traded for a shift of the coordinates,

$$
\tilde x_i = x_i + \frac{1}{2\hbar}\theta_{ij}p_j,
$$

the field theories on the arena are **non-local** — the same shift that removes the coordinate commutator introduces a derivative-dependent displacement.

### The star product

Field operators are split into plane waves and recombined; the product of two operators becomes the **Moyal product** of the corresponding functions,

$$
A(x)\star B(x) = \exp\!\left(\frac{i}{2}\theta^{\mu\nu}\partial_\mu\partial'_\nu\right) A(x)B(x')\Big|_{x=x'},
$$

the Weyl–Moyal correspondence. The star product is associative. Two facts about it matter here. First, the **quadratic (kinetic) terms of an action are unchanged** by the deformation, because the $\theta$-correction is a total derivative at second order; the propagators are therefore identical to the commutative ones, and, as the source puts it, the deformed theory has the same degrees of freedom as the commutative one, related to it by the Seiberg–Witten map. Second, the deformation first shows itself at **cubic and higher order in the fields** — which is why the free Maxwell action stays quadratic but its field equations do not stay linear.

At first order in $\theta$ the Seiberg–Witten expansion gives

$$
A_\mu = A_\mu - \tfrac12\theta^{\alpha\beta}A_\alpha(\partial_\beta A_\mu + F_{\beta\mu}),
\qquad
F_{\mu\nu} = F_{\mu\nu} + \theta^{\alpha\beta}F_{\mu\alpha}F_{\nu\beta} - \theta^{\alpha\beta}A_\alpha\partial_\beta F_{\mu\nu},
$$

with $e$ absorbed into $\theta^{\alpha\beta}$. The quadratic term of $F_{\mu\nu}$ is the source of every non-linearity below.

## The Non-Linear Maxwell Equations

### The Lagrangian

The free Maxwell action on the deformed arena is

$$
S = -\frac14\int d^4x\, F_{\mu\nu}\star F^{\mu\nu},
\qquad
F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu - ie[A_\mu,A_\nu]_M,
$$

with the Moyal bracket $[A_\mu,A_\nu]_M = A_\mu\star A_\nu - A_\nu\star A_\mu$. Expanding to first order in $\theta$ gives the Lagrangian

$$
\mathcal L = -\frac14 F_{\mu\nu}^2 + \frac18\theta^{\alpha\beta}F_{\alpha\beta}F_{\mu\nu}^2 - \frac12\theta^{\alpha\beta}F_{\mu\alpha}F_{\nu\beta}F_{\mu\nu} + O(\theta^2) + A_\mu J_\mu,
$$

which the source recasts, with $E_i = iF_{i4}$ and $B_i = \epsilon_{ijk}F_{jk}$, as

$$
\mathcal L = \frac12\left(\vec E^2 - \vec B^2\right)\left[1 + \vec\theta\cdot\vec B\right] - (\vec\theta\cdot\vec E)(\vec E\cdot\vec B) + O(\theta^2) + A_\mu J_\mu ,
$$

where $\theta_i = \tfrac12\epsilon_{ijk}\theta_{jk}$ and $\theta_{i4}=0$. At $\vec\theta=0$ this is the Maxwell Lagrangian. The $\vec\theta$-terms are **odd under $CP$**, which is the source's first structural remark. The corpus's *The Field-Strength Biquaternion and Its Invariants* works with the two invariants $\vec E^2-\vec B^2$ and $\vec E\cdot\vec B$, and they appear here multiplied by the two $\vec\theta$-scalars $\vec\theta\cdot\vec B$ and $\vec\theta\cdot\vec E$ — which is exactly why the deformation cannot preserve every symmetry those invariants otherwise carry.

The two forms are the same quantity: the $\theta$-part of the four-index expression reproduces the three-vector expression identically (checked numerically on random fields for the companion `.context`).

### The constitutive relations

The field equations follow from $\mathcal L$ by the Lagrange–Euler equation. Cast in the form used in matter, they are the familiar pair

$$
\frac{\partial}{\partial t}\vec D - \mathrm{rot}\,\vec H = -\vec J,
\qquad
\mathrm{div}\,\vec D = \rho,
$$

together with the source-free pair

$$
\frac{\partial}{\partial t}\vec B + \mathrm{rot}\,\vec E = 0,
\qquad
\mathrm{div}\,\vec B = 0 .
$$

The pair with sources closes on the **displacement and magnetic fields**, and these differ from $\vec E$ and $\vec B$ by $\vec\theta$-dependent corrections that are **quadratic in the fields**:

$$
\vec D = \vec E + \vec d,
\qquad
\vec d = (\vec\theta\cdot\vec B)\vec E - (\vec\theta\cdot\vec E)\vec B - (\vec E\cdot\vec B)\vec\theta,
$$

$$
\vec H = \vec B + \vec h,
\qquad
\vec h = (\vec\theta\cdot\vec B)\vec B + (\vec\theta\cdot\vec E)\vec E - \tfrac12\left(\vec E^2 - \vec B^2\right)\vec\theta .
$$

This is the central structural result of the paper, and it is worth stating in the corpus's own terms. At small $\vec\theta$ the displacement and magnetic fields are not proportional to $\vec E$ and $\vec B$: they are `$(\text{linear}) + \vec\theta\times(\text{quadratic})$`, and the quadratic terms mix the two fields and the background. The relations are exactly what a **non-linear medium** supplies. Both follow from the Lagrangian by $\vec D = \partial\mathcal L/\partial\vec E$ and $\vec H = -\partial\mathcal L/\partial\vec B$, which is the check that fixes the signs (verified numerically for the companion `.context`). The casting of the deformed field equation into the sourced Maxwell form with these $\vec d$ and $\vec h$ is attributed by the source to Guralnik, Jackiw, Pi and Polychronakos; the Lagrangian and the $\vec\theta$-expansion are the source's own.

The corpus's media article develops the **linear** case in full: for a homogeneous medium $D=\epsilon E$, $B=\mu H$, and the two parameters are the speed $c=1/\sqrt{\epsilon\mu}$ and the impedance $Z=\sqrt{\mu/\epsilon}$. The deformed vacuum is the case in which those relations acquire field-dependent terms and a **fixed background direction** $\vec\theta$. It is the same logical slot — a constitutive relation — filled non-linearly.

## Plane Waves Survive the Non-Linearity

The source's second-order equations are obtained by eliminating D and H. Applying the curl to the first sourced equation, substituting rot E from the source-free pair, and using the constitutive relations, gives

$$
\Delta\vec B - \frac{\partial^2}{\partial t^2}\vec B + \Delta\vec h - \mathrm{grad}\,\mathrm{div}\,\vec h + \frac{\partial}{\partial t}\mathrm{rot}\,\vec d = -\mathrm{rot}\,\vec J,
$$

$$
\Delta\vec E - \frac{\partial^2}{\partial t^2}\vec E - \frac{\partial^2}{\partial t^2}\vec d + \mathrm{grad}\,\mathrm{div}\,\vec d + \frac{\partial}{\partial t}\mathrm{rot}\,\vec h = \frac{\partial}{\partial t}\vec J + \mathrm{grad}\,\rho .
$$

The time derivative in front of the two rotation terms belongs there: it is what makes the deformed terms cancel for a plane wave, and it is easily lost in the two-column layout of the source. At $\vec\theta=0$ these are the ordinary wave equations. At $\vec\theta\ne0$ they are **non-linear**, because $\vec d$ and $\vec h$ are quadratic in the fields.

The striking result is that the **plane electromagnetic wave is still a solution**. With the usual ansatz

$$
\vec E = \vec E_0\,\exp(ik_\mu x^\mu),
\qquad
\vec B = (\vec u\times\vec E_0)\,\exp(ik_\mu x^\mu),
\qquad
\vec u = \vec k/k_0,
$$

the non-linear terms arrange themselves to cancel, and the plane wave solves the deformed equations exactly as it solves the linear ones. The cancellation is worth one line of algebra because it is not an accident: for a vacuum plane wave $\vec E^2=\vec B^2$, so the last term of $\vec h$ drops; $\vec d$ and $\vec h$ become the transverse pair multiplying the single phase $\exp(2ik_\mu x^\mu)$; the double-frequency phase squares the wave vector, and the vacuum dispersion $k^2=0$ makes the deformed contributions vanish identically, for every $\vec\theta$ (checked for the companion `.context`, where dropping the two time derivatives — as the column layout invites — makes the same test fail). Two consequences follow. First, **"plane wave" does not imply "linear theory"**: non-linearity does not by itself destroy plane-wave propagation, and the corpus's *Exercise: Plane-Wave Propagation in a Medium* is, in this picture, the **linear limit** of a one-parameter family. Second, the deformation is nonetheless physically present, because it does affect the **speed**. The source cites the result that for propagation **transverse to a background magnetic induction** the velocity differs from $c$ — a birefringence-like effect that is a direct consequence of the non-linearity and that is **very small**, being suppressed by $\vec\theta$.

The honest interpretation is therefore: the plane-wave solution is exact, and the deviation from $c$ is a computable consequence of a specified deformation, not a new free parameter. The source attributes both the plane-wave observation and the transverse-velocity result to Guralnik, Jackiw, Pi and Polychronakos, and reports them rather than deriving them. The corpus's empirical-agenda standard applies — the effect is real but $\theta$-suppressed, so nothing here is a candidate signature.

## Duality Is Broken

The corpus's duality exercise establishes that the free Maxwell equations are invariant under the rotation

$$
\vec E \mapsto \vec E\cos\alpha + \vec B\sin\alpha,
\qquad
\vec B \mapsto \vec B\cos\alpha - \vec E\sin\alpha,
$$

equivalently under $\vec N\mapsto \exp(-i\alpha)\vec N$ with $\vec N = \vec E + ic\vec B$, and that this is a symmetry of the **polarisation space**, rotating the polarisation axes about the wave vector. In four-dimensional notation the transformation is

$$
F'_{\mu\nu} = F_{\mu\nu}\cos\alpha - \tilde F_{\mu\nu}\sin\alpha,
\qquad
\tilde F'_{\mu\nu} = \tilde F_{\mu\nu}\cos\alpha + F_{\mu\nu}\sin\alpha,
$$

with $\tilde F$ the dual tensor.

On the deformed arena this fails. The deformation enters the Lagrangian only as the two scalars $\vec\theta\cdot\vec B$ and $\vec\theta\cdot\vec E$ multiplying the two invariants, and under the rotation those two scalars **do not stay put**: they rotate into each other, $\vec\theta\cdot\vec B\mapsto(\vec\theta\cdot\vec B)\cos\alpha-(\vec\theta\cdot\vec E)\sin\alpha$ and similarly for $\vec\theta\cdot\vec E$, while $I_1=\vec E^2-\vec B^2$ and $I_2=\vec E\cdot\vec B$ are invariant. The $\vec\theta$-terms of the Lagrangian are therefore not invariant, and neither are the field equations that follow from them. Setting $\vec\theta=0$ restores duality exactly, as the source notes. The violation is not small in principle — it is a misalignment of an angle — only the *magnitude* of the effects it produces is $\theta$-suppressed (verified on random fields and rotation angles for the companion `.context`: the $\vec\theta$-part of the Lagrangian changes by a quantity of order the field magnitude for every angle that is not a multiple of $\pi/2$).

The structural interpretation is worth stating as the paper's sharpest contribution to the corpus. In the commutative, linear arena, duality is an **exact symmetry** of the free equations, and the corpus builds on that exactness in the modular-group article. Here a **specified modification of the arena breaks it**. Duality thus becomes a **diagnostic**: it holds for the undeformed, linear Maxwell theory, and its violation is a pointer to a deformation of the arena or to non-linearity. This is the converse of the corpus's theorem and it is the reason the paper is recorded in the Electromagnetism section rather than only in the research agenda.

## Energy, Momentum, and the Two Stress Tensors

### The densities and the conservation law

Multiplying the sourced equations by $\vec E$ and the source-free ones by $\vec H$ and adding gives the Poynting theorem in its deformed form,

$$
\frac{\partial\mathcal E}{\partial t} = -(\vec J\cdot\vec E) - \mathrm{div}\,\vec P,
\qquad
\vec P = \vec E\times\vec H,
$$

so that with $\vec J=0$ the four-vector $P_\mu = (\vec P, i\mathcal E)$ is conserved. The energy density and momentum density are

$$
\mathcal E = \frac{\vec E^2+\vec B^2}{2}\left[1+\vec\theta\cdot\vec B\right] - (\vec E\cdot\vec B)(\vec\theta\cdot\vec E),
$$

$$
\vec P = \left[1+\vec\theta\cdot\vec B\right](\vec E\times\vec B) + \tfrac12\left(\vec B^2-\vec E^2\right)(\vec E\times\vec\theta).
$$

The deformations of the corpus's $W = \tfrac12(\epsilon\vec E^2+\mu\vec H^2)$ and of the Poynting vector $\vec E\times\vec H$ are visible: the free energy density acquires a term proportional to $(\vec E\cdot\vec B)(\vec\theta\cdot\vec E)$ that is **not positive definite** and a factor $1+\vec\theta\cdot\vec B$ on the positive part.

### The canonical tensor, and the symmetric tensor that is not conserved

The paper's most delicate technical point follows, and it is a caution rather than a result.

The **canonical** energy–momentum tensor of the Lagrangian,

$$
T^{\mathrm{can}}_{\mu\nu} = (\partial_\nu A_\alpha)\frac{\partial\mathcal L}{\partial(\partial_\mu A_\alpha)} - \delta_{\mu\nu}\mathcal L,
$$

is conservative, $\partial_\mu T^{\mathrm{can}}_{\mu\nu}=0$. To reach a gauge-invariant tensor one adds a term $\Lambda_{\mu\nu}$ with $\partial_\mu\Lambda_{\mu\nu}=0$; the source's choice is

$$
\Lambda_{\mu\nu} = -(\partial_\alpha A_\nu)\frac{\partial\mathcal L}{\partial(\partial_\mu A_\alpha)},
$$

and the argument that $\partial_\mu\Lambda_{\mu\nu}=0$ is the standard one: the derivative tensor is antisymmetric in $\mu,\alpha$ because $\mathcal L$ depends on $A$ only through $F$, so the first contraction vanishes by symmetry, and the second vanishes by the equation of motion $\partial\mathcal L/\partial A_\nu=0$ when $J=0$. Nothing in that argument uses $\vec\theta$, so the **canonical tensor remains conservative**. The resulting tensor is still not symmetric, but it becomes symmetric at $\vec\theta=0$.

For the **symmetric** tensor the source varies the action with respect to the metric. The covariant form of the Lagrangian is written down, and then the observation is made that the expression only *looks* covariant: because $\theta^{\mu\nu}$ is a fixed tensor and does not transform under a change of metric, the action is **not a scalar**, and the standard conclusion — that the metric variation gives a conserved tensor — does not follow. Varying anyway produces a symmetric tensor that differs from the canonical one by $\vec\theta$-terms, and this tensor is **not conserved** on the deformed arena.

This is the point the corpus should carry as a boundary rule. The corpus improves stress tensors by the Hilbert variation in several places, and derives the conservation of the result from the invariance of the action. Kruglov's construction shows that **both halves of that reasoning can fail together**: a tensor that looks like a metric variation need not be conserved, and the reason is that the arena is not invariant. Whenever the corpus's gravity-adjacent material varies an action on a background that carries a fixed tensor, conservation is not automatic and must be checked. The source is explicit that the covariance "is broken because the variable $\theta^{\mu\nu}$ is not transformed as the second rank tensor at the Lorentz transformations."

### The components, and the mixed non-symmetry

The **components** of the canonical tensor make its conservation explicit, and one of them is not in the abbreviated treatment above:

$$
T_{44} = \mathcal E, \qquad T_{m4} = -iP_m, \qquad
T_{4m} = -i\epsilon_{mnk}\left\{E_nB_k\left[1+\vec\theta\cdot\vec B\right] + (\vec E\cdot\vec B)B_n\theta_k\right\}.
$$

The last of the three is not $-iP_m$: the **mixed** components are non-symmetric, as well as the spatial ones, which the source's "still not symmetric" leaves implicit. Their difference is

$$
T_{4m} - T_{m4} = -i\left[(\vec E\cdot\vec B)(\vec B\times\vec\theta)
+ \tfrac12\left(\vec E^2-\vec B^2\right)(\vec E\times\vec\theta)\right],
$$

proportional to the two invariants contracted with the background, and therefore vanishing at $\vec\theta=0$ and on null fields. So the antisymmetric part of the canonical tensor is present in **both** its spatial and its mixed components, and the spacetime asymmetry of the deformed arena appears as a non-symmetric stress tensor. The corpus records the fact and not an interpretation: whether the antisymmetric part can be absorbed by a Belinfante-type improvement on this arena is not shown by the source and is left open.

### The energy density as an integrability condition

The relation behind the Poynting theorem above,
$\vec E\cdot\partial_t\vec D + \vec H\cdot\partial_t\vec B = \partial_t\mathcal E$, is not a
convenience: it is the **integrability condition** for an energy density to exist at all, and it holds because
$\vec D$ and $\vec H$ are the field-derivatives of a Lagrangian. This is a statement about variational
non-linear media generally rather than about non-commutativity — the energy density is defined precisely when
the one-form $\vec E\cdot\delta\vec D + \vec H\cdot\delta\vec B$ is exact — and it is what lets the
deformed vacuum be read as a medium without ambiguity. It also gives the **medium form** of the energy,

$$
\mathcal E = \frac{\vec D^2+\vec H^2}{2} - (\vec\theta\cdot\vec B)\vec B^2,
$$

which agrees with the form quoted above to first order in $\vec\theta$ (the source states it to
$O(\theta^2)$).
$3.6\times10^{-9}$ on random fields and random time derivatives, the $O(\theta)$ agreement of the two energy
forms, the printed $T_{4m}$, and the mixed antisymmetry to machine precision.

### The trace anomaly

Both tensors have **non-zero trace**. For the canonical tensor,

$$
T^\mu{}_\mu = (\vec\theta\cdot\vec B)\left(\vec E^2-\vec B^2\right) - 2(\vec\theta\cdot\vec E)(\vec E\cdot\vec B),
$$

and for the symmetric tensor the trace is exactly twice this,

$$
T^{\mathrm{sym}\,\mu}{}_{\mu} = 2\left[(\vec\theta\cdot\vec B)\left(\vec E^2-\vec B^2\right) - 2(\vec\theta\cdot\vec E)(\vec E\cdot\vec B)\right].
$$

The source reads a non-zero trace as a **trace anomaly at the classical level**, reflecting the breaking of classical conformal invariance, and relates it to the breaking of Lorentz invariance by the constant $\vec\theta$; it suggests the anomaly contributes to the cosmological constant and might be the source of an inflationary period. Two properties of the expressions are checkable and are worth recording, because they show when the anomaly is present.

First, the trace is built from $\vec E^2-\vec B^2$ and $\vec E\cdot\vec B$ — the corpus's two invariants — contracted with $\vec\theta$. It therefore **vanishes whenever both invariants vanish**, which is the case for any **null field**, plane electromagnetic waves included. So the deformed vacuum is anomalous for **non-null** fields and anomaly-free for plane waves. Second, at $\vec\theta=0$ the trace vanishes for every field, recovering the classical result. Both were verified on the explicit tensor components for the companion `.context`, together with the factor-two relation between the two traces.

The corpus must **not** conflate this with its own trace anomaly. *The Trace Anomaly in Biquaternionic Form* treats the **quantum** Weyl anomaly: a non-vanishing trace generated by the regularisation of a determinant, whose coefficient counts the field's real components. Kruglov's anomaly is **classical**: it is present in the tree-level stress tensor of a deformed but unquantised theory, it is caused by the deformation of the arena rather than by regularisation, and its coefficient is not a multiplicity but the background $\vec\theta$. The two share a name and a symptom — a non-zero $T^\mu{}_\mu$ indicating that a conformal symmetry is broken — and nothing else. The corpus records them separately and says so.

## The Spin-Tensor (Quaternion) Form

The paper's title promises quaternions, and the last section supplies them. Multiplying the source-free equation by $i$ and adding it to the sourced one, and using the Pauli-matrix identity, the whole system collapses into a single matrix equation,

$$
\nabla F + \tfrac12\left(\nabla G + G^+\overleftarrow{\nabla}\right) = -J,
$$

where $\nabla = \tau^\mu\partial_\mu$, $F = f_\mu\tau^\mu$ with $f_k = D_k+iB_k$ and $f_4=0$, $G = g_m\tau^m$ with $g_m = d_m + ih_m$, $J = J_\mu\tau^\mu$ with $J_4=i\rho$, and $G^+$ is the Hermitian conjugate. The complex vector $\vec g = \vec d + i\vec h$ has the compact form

$$
\vec g = i(\vec\theta\cdot\vec v^*)\vec v - \frac{i}{2}\vec\theta(\vec v^*)^2,
\qquad
\vec v = \vec E + i\vec B,
$$

which shows the non-linearity in one line: the correction is quadratic in the Riemann–Silberstein vector $\vec v$ and its conjugate. The spin-tensor is defined through the potential by $F = -\nabla A$ with $A = A_\mu\tau^\mu$, which reproduces $F_{\mu\nu}=\partial_\mu A_\nu - \partial_\nu A_\mu$. The source notes that Eq. (45) "is equivalent to the quaternion form as the quaternion algebra can be realized through the Pauli matrices", and that at $\theta^{\mu\nu}=0$ it becomes the quaternion form of the standard Maxwell equations that the corpus records in *Maxwell's Equations in the Biquaternionic Formulation*. This is the sense in which the paper is about quaternions: the algebra gives the compact form and nothing else.

The transformation properties close the section. Under $X' = L^+XL$ with $L\in SL(2,\mathbb C)$, the matrices transform as $\nabla' = L^+\nabla L$, $F' = L^{-1}FL$, $J' = L^+JL$, and the Lorentz **invariants** of the transformations are the **determinants** of the matrices. The $\vec\theta$-terms in the equation violate this Lorentz symmetry, which is the same statement as before, seen in the matrix form. The appendix realises the quaternion algebra on the Pauli matrices, $e_4=\tau_0$, $e_k=i\tau_k$, with $e_4^2=1$ and $e_k^2=-1$, and records the biquaternion Lorentz transformation $x' = LxL^*$ with $L\bar L=1$, the six-parameter $SO(3,1)$ action the corpus's *The Lorentz Transformation as a Biquaternionic Rotation* derives from the same algebra.

## Status, Contrasts, and Boundaries

What is reportable, and with what confidence:

- The **star-product formalism** and the **Seiberg–Witten expansion** are standard and are used here as the source uses them; the corpus does not re-derive them. The statement that the kinetic terms are unaffected and the propagators unchanged is a property of the star product and is exact.
- The **Lagrangian** in its two forms, the **field equations**, the **constitutive relations** $\vec d$ and $\vec h$, and the **plane-wave solutions** are algebraic and were verified for the companion `.context` (the last two the source attributes to Guralnik et al.).
- The **trace expressions** and the factor two between them follow from the components the source prints and were verified.
- The **duality breaking** is a property of the $\vec\theta$-terms and is immediate from the invariants.

What is framing, and is recorded as the author's:

- The superstring motivation (D-branes with a background magnetic field) is the source's setting, not a result of the paper.
- The interpretation of the deformed vacuum as a medium is an interpretation, though a natural one given the constitutive relations.
- The cosmological-constant and inflation suggestion at the end is a speculation, and is recorded as such.

The boundaries are four.

First, the **quaternion form is notation**. The paper's results are properties of the Moyal deformation, not of quaternions. A reader who takes the title as a claim that the quaternion algebra *causes* the duality breaking or the trace anomaly has the wrong interpretation; the corpus's own algebra is not deformed here, the arena is.

Second, **non-commutative spacetime is not the non-commutative quaternion algebra**, and it is not the C-space programme either. The three are distinct, the corpus holds the latter separately, and the paper is a comparison point for both rather than an instance of either.

Third, the deformation **breaks Lorentz invariance** by construction, because $\vec\theta$ is a fixed tensor. The corpus's framework is Lorentz-covariant, so this is a genuinely different arena and not a variant of the corpus's own. The corpus records it as a neighbouring theory.

Fourth, the effects are **$\theta$-suppressed**, and the bound the source quotes, $\Lambda_{NC}\ge 10^3$ GeV, is far below the Planck scale the corpus's empirical-agenda discussion already invokes. So nothing here is an observable signature; the value of the paper to the corpus is structural.

The corpus's *The Empirical Status of the Biquaternion Framework* lists three routes by which the framework could acquire content that distinguishes it, and names "a non-commutative spacetime" as the first. The paper recorded here does not derive that deformation from the biquaternion algebra — it **inserts** it, exactly as the agenda predicts such a deformation would have to be inserted. What it supplies is the answer to the question the agenda leaves open: a deformation of the arena of the Moyal type makes the vacuum non-linear, preserves plane waves, breaks duality, and produces a classical trace anomaly. That is a sharper statement than "a scale would help", and it is what the corpus takes from the paper.

## Summary

Kruglov's *Maxwell's Theory on Non-Commutative Spaces and Quaternions* re-derives Maxwell's theory on an arena whose coordinates do not commute, $[x^\mu,x^\nu]=i\theta^{\mu\nu}$, using the Moyal star product and writing the result in spin-tensor (quaternion) form. Its content for the corpus is threefold. First, the deformation makes the **vacuum a non-linear medium**: the displacement and magnetic fields acquire the field-quadratic corrections $\vec d$ and $\vec h$, so that the constitutive relations are non-linear, while **plane electromagnetic waves remain exact solutions** — "plane wave" does not imply a linear theory. Second, **duality is broken** by the deformation, which makes duality a diagnostic of the commutative, linear case and gives the corpus the converse of its own duality theorem. Third, the **canonical energy–momentum tensor is conservative but the symmetric one obtained from the metric variation is not**, because the action is not a Lorentz scalar when $\vec\theta$ is fixed, and both tensors have non-zero trace — a **classical trace anomaly** that vanishes for null (plane-wave) fields and at $\vec\theta=0$, and that must not be conflated with the corpus's quantum Weyl anomaly. The quaternion form is a compact notation, not the source of the results; the deformation of the arena is what does the work, and the effects are $\theta$-suppressed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $x^\mu$, $x^\mu$ | Non-commuting coordinate operator and its commutative image |
| $\theta^{\mu\nu}$ | Constant antisymmetric deformation tensor, dimension $(\text{length})^2$ |
| $\Lambda_{NC}$, $\epsilon^{\mu\nu}$ | Non-commutativity scale and dimensionless shape tensor, $\theta^{\mu\nu}=\epsilon^{\mu\nu}/\Lambda_{NC}^2$ |
| $\theta_i$ | Three-vector of the deformation, $\theta_i=\tfrac12\epsilon_{ijk}\theta_{jk}$, $\theta_{i4}=0$ |
| $[x^\mu,x^\nu]=i\theta^{\mu\nu}$ | The defining commutator; the corpus's "$ict$" convention is kept for time |
| $\star$ | Moyal star product, $\exp(\tfrac{i}{2}\theta^{\mu\nu}\partial_\mu\partial'_\nu)$ |
| $[A_\mu,A_\nu]_M$ | Moyal bracket $A_\mu\star A_\nu - A_\nu\star A_\mu$ |
| $F_{\mu\nu}$, $\tilde F_{\mu\nu}$ | Field strength and its dual; $E_i=iF_{i4}$, $B_i=\epsilon_{ijk}F_{jk}$ |
| $\vec D,\vec H$ | Displacement and magnetic fields; $\vec D=\vec E+\vec d$, $\vec H=\vec B+\vec h$ |
| $\vec d,\vec h$ | Field-quadratic $\vec\theta$-corrections of eqs. (18), (19) — the non-linear constitutive relations |
| $\vec v=\vec E+i\vec B$ | Riemann–Silberstein vector; the non-linearity is $\vec g\propto\vec\theta\vec v^2$ |
| $\mathcal E,\vec P$ | Deformed energy density and momentum density; $P_\mu=(\vec P,i\mathcal E)$ |
| $T^{\mathrm{can}}_{\mu\nu}$, $T^{\mathrm{sym}}_{\mu\nu}$ | Canonical (conservative) and symmetric (not conserved on the deformed arena) stress tensors |
| $T^\mu{}_\mu$ | Classical trace anomaly, $\propto(\vec\theta\cdot\vec B)(\vec E^2-\vec B^2)-2(\vec\theta\cdot\vec E)(\vec E\cdot\vec B)$; doubles for the symmetric tensor |
| $\tau_\mu=(\tau_k,\tau_4)$, $\tau_4=i\tau_0$ | Pauli matrices realising the quaternion units; $e_4=\tau_0$, $e_k=i\tau_k$ |
| $F=f_\mu\tau^\mu$, $G=g_m\tau^m$ | Spin-tensor (quaternion) field and correction; $f_k=D_k+iB_k$, $g_m=d_m+ih_m$ |

## Further Reading

- S. I. Kruglov, "Maxwell's Theory on Non-Commutative Spaces and Quaternions", arXiv:hep-th/0110059 (2001), the source of this article.
- N. Seiberg and E. Witten, "String theory and noncommutative geometry", *Journal of High Energy Physics* **09** (1999) 032; arXiv:hep-th/9908142, for the D-brane origin of non-commutative coordinates and the map between deformed and commutative field theory.
- J. E. Moyal, "Quantum mechanics as a statistical theory", *Proceedings of the Cambridge Philosophical Society* **45** (1949) 99, for the star product; and A. Connes, *Noncommutative Geometry* (Academic Press, 1994), for the geometric setting.
- H. S. Snyder, "Quantized space-time", *Physical Review* **71** (1947) 38, for the earliest proposal of non-commuting coordinates.
- A. Bichl, J. Grimstrup, L. Popp, M. Schweda and R. Wulkenhaar, arXiv:hep-th/0102044, for the Lagrangian and the Seiberg–Witten expansion to first order in $\theta$ that the source uses.
- Z. Guralnik, R. Jackiw, S.-Y. Pi and A. P. Polychronakos, arXiv:hep-th/0106044, for the casting of the deformed field equations into the sourced Maxwell form with the non-linear $\vec d$ and $\vec h$, and for the plane-wave solution and the transverse-velocity result that the source reports; the source spells the first name "Guralnic".
- L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the canonical and symmetric energy–momentum tensors and the metric-variation construction.
- G. Casanova, *L'algèbre Vectorielle* (Presses Universitaires de France, 1976), for the quaternion realisation of the Lorentz group that the appendix follows.
