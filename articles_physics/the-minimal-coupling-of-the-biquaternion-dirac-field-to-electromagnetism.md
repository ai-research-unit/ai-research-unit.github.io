# __The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism__

## Introduction

**Minimal coupling** is the prescription by which a charged field is coupled to the electromagnetic field: the ordinary derivative is replaced by the **covariant derivative**. In the biquaternion framework both objects are already fixed by the gauge principle. The connection is the potential biquaternion $\tilde{A}$ of *Maxwell's Equations in the Biquaternionic Formulation*, its gauge transformation is

$$
\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma,
$$

and the covariant derivative is

$$
D = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A}, \qquad D_\mu = \partial/\partial Q_\mu + \frac{iϙ}{\hbar}A_\mu .
$$

The gauge principle article derived $D$ from the localization of the algebra's central phase and verified that $D\tilde{\Psi}$ transforms homogeneously. It applied the result to a general biquaternion field, not specifically to the Dirac field. *The Dirac Equation in Biquaternionic Form* names the minimal coupling of the Dirac field as the subject of the companion treatment (its open question 7); the precise biquaternion form is representation-dependent. This article supplies that statement, and reports what the recomputation gives.

Three results are established here.

1. **The coupled equation.** Replacing the gradient in the free biquaternion Dirac equation by the covariant derivative gives the chiral pair $D\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{D}\tilde{\Psi}_L = m\tilde{\Psi}_R$. The second operator is the $\natural$-image of the first, so it carries the quaternion-conjugate gradient and the conjugate connection; its explicit form is given in the prescription section.
2. **Exact gauge covariance, massive as well as massless.** The pair holds in every gauge when it holds in one, because the parent's mass term is the linear chiral pair and the central phase passes through it. The factor $\lambda$ on both sides is the algebra statement, where the field is a biquaternion and $\lambda$ is one scalar multiplying it from the left; on the parent's conjugate-module assignment the same phase is axial, the mass term is not invariant there, and the choice between the two is the matter-representation question, open question 2.
3. **A negative result on the current.** The naive gauge-invariant bilinear $i\tilde{\Psi}\tilde{\Psi}^{*}$ is a material-sector object but is **not conserved** on solutions of the massless equation, so the electromagnetic current of the coupled system is not a pure biquaternion product of this kind.

The division between what is established and what is interpretation is stated at the outset and kept explicit.

- **Established, and recomputed below.** The minimal-coupling prescription $D = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A}$ acting on the biquaternion Dirac field by left multiplication; the coupled equation and its component form; the exact gauge covariance of the coupled equation, in the massive case as well as the massless one; the gauge invariance and material-sector membership of $i\tilde{\Psi}\tilde{\Psi}^{*}$; the non-conservation of that bilinear, exhibited on an exact field rather than asserted; and the distinction among the three forms of the Dirac equation the corpus carries, with the reason the prescription attaches to the one written on the algebra.
- **Interpretation.** Interpreting the coupled equation as "the Dirac field in a background electromagnetic connection" is a geometric interpretation of an algebraic construction. The algebra supplies the transformation law and the covariance; the connection/curvature picture is a consistent interpretation, as in the gauge principle article.
- **Gaps, left visible.** The biquaternion form of the conserved interaction current is not the naive bilinear, and is not settled here. Whether the left or the right action on the algebra is the physical matter representation is a choice the parent left open, and it decides whether the mass term is invariant: on the Dirac module the central phase acts as the axial rotation. The axial symmetry broken by the mass — and whether it can be gauged — is not treated here. These are stated as gaps in the sections where they arise and collected in the open questions.

The article is organized as follows. The next section recalls the Dirac field and the phase symmetry that is to be localized. The section after that states the minimal-coupling prescription, and a subsection of it separates the three forms of the Dirac equation that the corpus carries — the one-sided chiral pair written on the algebra, the same pair read on the Dirac module, and the two-sided form with the conjugation in the mass term — and states why the prescription attaches to the first. The following section proves the covariance in the massless case and fixes the sign conventions. The next section treats the massive case, where the linear mass term preserves the covariance and the axial symmetry is what the mass breaks. A section examines the interaction current and the Maxwell source, reports the negative result on an explicit field, and records one external identity of the same shape, due to Arbab, which is verified here and cited without being adopted as framework content. A section relates the construction to the standard spinor-module minimal coupling. A section separates what the algebra supplies from what it only transcribes. The article then collects the open questions, and a reference section fixes the matrix frame in which the cells are compared with the standard matrices, and that section is the only place in which those matrices appear.

## The Dirac Field and Its Phase Symmetry

The **biquaternion Dirac field** is a biquaternion-valued field $\tilde{\Psi}(\tilde{Q}) \in \mathbb{B}$ satisfying the free equation

$$
\tilde{\nabla}\tilde{\Psi}_R = m\,\tilde{\Psi}_L, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\,\tilde{\Psi}_R .
$$

The two members are the **chiral pair**. The first acts on the right-chiral half by the gradient, the second on the left-chiral half by the quaternion conjugate of the gradient. When $m = 0$ they decouple,

$$
\tilde{\nabla}\tilde{\Psi}_R = 0, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = 0 .
$$

The right-chiral member is then identical in form to the source-free biquaternion Maxwell equation obeyed by the field-strength biquaternion $\tilde{F}$; the difference is the representation, the Maxwell field living in the vector part of the algebra and the Dirac field in the full algebra. The two are the two representations of the same Clifford algebra, as the parent article records.

**The two halves.** The splitting is by the chirality, which is the central sign of the complexification and not a Clifford matrix (*The Dirac Equation in Biquaternionic Form*, §*Chirality and the Central Sign*). With $\tilde{\Xi}_{\mathrm{ad}}$ the adjoined central root of $-1$, the two central idempotents and the chirality are

$$
e_{\pm} = \tfrac12\left(1 + i\tilde{\Xi}_{\mathrm{ad}}\right), \qquad
\chi = i\tilde{\Xi}_{\mathrm{ad}} = e_{+} - e_{-}, \qquad
\chi^2 = e_t ,
$$

and the chiral halves of the field are the two projections

$$
P_L = \tfrac12\left(e_t - \chi\right), \qquad P_R = \tfrac12\left(e_t + \chi\right), \qquad \tilde{\Psi}_{L,R} = P_{L,R}\tilde{\Psi} .
$$

On the Dirac module $\Delta = S\oplus S^{\mathrm{c}}$ the chirality is $\operatorname{diag}(-I_2,I_2)$, so $P_L$ projects onto $S$ and $P_R$ onto $S^{\mathrm{c}}$. The grading is not the Peirce index: the two Peirce carriers of $\mathbb{B}$ are two copies of $S$ and carry no chirality, and the sign that flips between them is the inner sign $R_{i\vec e_z}^{\mathrm{axf}}$, not the central $\chi$. The distinction matters for the mass term, and the subsection *Which equation, and on which module* below turns on it.

The **real structure** is the anti-Hermitian conjugation

$$
\tilde{\Psi}^\flat = -\tilde{\Psi}^{*} = -\overline{\tilde{\Psi}^{\natural}} ,
$$

whose fixed space is the material sector $\mathbb{M}_-$. It is the algebra's $\flat$, and it is not the mass.

The symmetry that minimal coupling localizes is the algebra's central $\mathrm{U}(1)$, established in the gauge principle article. The centre of $\mathbb{B}$ is the complex scalar subspace

$$
\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t,\, ie_t\},
$$

and its $*$-unitary elements are the phases $\lambda = \exp(i\theta)$ with $\theta \in \mathbb{R}$. A **constant** central phase

$$
\tilde{\Psi} \;\longmapsto\; \exp(i\theta)\tilde{\Psi}, \qquad \theta \ \text{constant},
$$

is a symmetry of the equation, massive or massless, because a central constant commutes with the basis and with the derivatives and therefore passes through both members of the pair:

$$
\tilde{\nabla}\!\left(\lambda\tilde{\Psi}_R\right) = \lambda\,\tilde{\nabla}\tilde{\Psi}_R, \qquad
\tilde{\nabla}^{\natural}\!\left(\lambda\tilde{\Psi}_L\right) = \lambda\,\tilde{\nabla}^{\natural}\tilde{\Psi}_L .
$$

The **vector** character matters: one and the same $\lambda$ multiplies both chiral halves, so the pair $D\tilde\Psi_R = m\tilde\Psi_L$ scales uniformly and the mass term is invariant. Read on the Dirac module the same central element acts as $\lambda$ on one half and $\bar\lambda$ on the other, and there the mass term is not invariant; the two readings are compared in *Which equation, and on which module* below.

What the mass term breaks is the **axial** rotation,

$$
\tilde{\Psi} \;\longmapsto\; \exp(i\alpha\chi)\,\tilde{\Psi}, \qquad \alpha \ \text{real},
$$

which on the Dirac module is $\operatorname{diag}(e^{-i\alpha}I_2,\, e^{+i\alpha}I_2)$: the two halves acquire opposite phases, while the mass term pairs them, so a term that pairs $L$ with $R$ cannot be invariant under a transformation that scales them oppositely. The algebra's anti-Hermitian conjugation $\flat$ is antilinear,

$$
\left(\lambda\tilde{\Psi}\right)^\flat = \lambda^{*}\,\tilde{\Psi}^\flat
$$

for a central phase $\lambda$, so a mass term that *paired* the field with its conjugate would require $\lambda = \lambda^{*}$ and would retain only $\lambda = \pm 1$; but that is a property of the real structure $\flat$, not of the parent's mass term, and it is developed in the companion articles on the neutrino and on chirality. In the algebra form the continuous vector coupling therefore belongs to the massive field as well as to the massless one.

The **charge** $ϙ$ is the coupling constant of the field, introduced by the gauge principle. It is a parameter: the algebra does not fix its value, its sign, or its quantization. For the electron $ϙ = -e$; the value and the sign are inserted, as *The Electron in Biquaternionic Form* records.

## The Minimal Coupling Prescription

The prescription replaces the gradient in the free equation by the covariant derivative:

$$
\tilde{\nabla} \;\longrightarrow\; D = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A}, \qquad
D\tilde{\Psi} = \tilde{\nabla}\tilde{\Psi} + \frac{iϙ}{\hbar}\,\tilde{A}\,\tilde{\Psi}.
$$

The connection acts by **left multiplication** on the field. Applied to the free Dirac equation in its linear, chirality-off-diagonal form, the prescription gives the **minimally coupled biquaternion Dirac equation**

$$
\boxed{\ D\tilde{\Psi}_R = m\,\tilde{\Psi}_L, \qquad \bar{D}\tilde{\Psi}_L = m\,\tilde{\Psi}_R\ }
$$

with $\bar{D} := \tilde{\nabla}^{\natural} + \frac{iϙ}{\hbar}\tilde{A}^{\natural}$, that is,

$$
\tilde{\nabla}\tilde{\Psi}_R + \frac{iϙ}{\hbar}\,\tilde{A}\,\tilde{\Psi}_R = m\,\tilde{\Psi}_L, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L + \frac{iϙ}{\hbar}\,\tilde{A}^{\natural}\,\tilde{\Psi}_L = m\,\tilde{\Psi}_R,
$$

and in the massless case the two members decouple separately,

$$
D\tilde{\Psi}_R = 0, \qquad \bar{D}\tilde{\Psi}_L = 0,
$$

that is, $\tilde{\nabla}\tilde{\Psi}_R + \frac{iϙ}{\hbar}\tilde{A}\tilde{\Psi}_R = 0$ and $\tilde{\nabla}^{\natural}\tilde{\Psi}_L + \frac{iϙ}{\hbar}\tilde{A}^{\natural}\tilde{\Psi}_L = 0$. The term $\frac{iϙ}{\hbar}\tilde{A}\tilde{\Psi}$ is the **interaction term**. It is exactly the term that the localization of the phase forces, and it is the biquaternion representative of the familiar spinor-module coupling, in which the four-potential is contracted with the four generators.

**Component form.** Write the potential as $\tilde{A} = \sum_\mu A_\mu e_\mu$ with complex scalar coefficients $A_\mu$ — the abelian case, in which the connection coefficients are central scalars and commute with one another. Since each $A_\mu$ is a scalar and commutes with the basis, the covariant derivative separates into components:

$$
D = \sum_{\mu\in\{t,x,y,z\}} e_\mu\left(\partial/\partial Q_\mu + \frac{iϙ}{\hbar}A_\mu\right),
\qquad
D_\mu = \partial/\partial Q_\mu + \frac{iϙ}{\hbar}A_\mu,
$$

with $\partial/\partial Q_t = -(i/c)\,\partial/\partial t'$ and $\partial/\partial Q_k = \partial/\partial x_k$. This is the identical component form derived in the gauge principle article, now read as an operator on the Dirac field. Setting $\hbar = 1$ gives $D_\mu = \partial/\partial Q_\mu + iϙA_\mu$, the convention used for the minimal substitution in the companion article on the Dirac equation's solutions and the non-relativistic limit.

**The connection is a material-sector object.** The gauge principle article shows that a **real** gauge function $\Gamma$ keeps $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$ in $\mathbb{M}_-$. The coupling is therefore the coupling of the Dirac field to a material-sector connection, and the ingredient $\frac{iϙ}{\hbar}\tilde{A}$ in $D$ is Hermitian:

$$
\left(i\tilde{A}\right)^{*} = -i\,\tilde{A}^{*} = i\tilde{A},
$$

since $\tilde{A}^{*} = -\tilde{A}$ on $\mathbb{M}_-$. The factor $i$ is what converts the anti-Hermitian connection into a Hermitian coupling. This is inherited, not rederived.

**Sign convention.** The gauge principle article fixes the pair of signs $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$ and $D = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A}$ with the phase $\lambda = \exp(iϙ\Gamma/\hbar)$, and its companion records that the two must be kept together. The open question in the parent Dirac article writes the standard physics convention $\partial/\partial Q_\mu \to \partial/\partial Q_\mu - iϙA_\mu/\hbar$, with the opposite sign. That is the same coupling with the opposite sign of $ϙ$ (or of $\tilde{A}$); this article inherits the gauge principle's sign and does not silently flip it. The covariance checks below use the inherited pair.

**Left action only, and the mirror written without an arrow.** Every coupling used in this article acts on the left. The mirror construction — derivative and connection both inserted on the right — is not a second prescription: it is the same one applied to the conjugate field. Read the same operator on the right, $\tilde\Psi D = \sum_\mu\left(\partial/\partial Q_\mu\tilde\Psi\right)e_\mu + \frac{iϙ}{\hbar}\tilde\Psi\tilde{A}$, and put $\Phi := \tilde\Psi^{\natural}$. Since $\natural$ is an anti-automorphism that fixes the central $i$ and negates the three spatial units,

$$
\left(\tilde\Psi D\right)^{\natural}
= D^{\natural}\,\tilde\Psi^{\natural}
= \left(\tilde{\nabla}^{\natural} + \frac{iϙ}{\hbar}\tilde{A}^{\natural}\right)\Phi
= \bar{D}\Phi ,
$$

with $D^{\natural} = \bar{D}$, so the right-action equation on $\tilde\Psi$ is a left-action equation on $\Phi$, with the operator $\bar{D}$ that the second member of the pair already carries. Nothing needs a right arrow: the side is given by position, and $\natural$ is what changes it.

Both constructions are gauge covariant (verified below), and they must be, being the same construction seen through $\natural$. What is **not** covariant is the mixed combination — the left gradient with the connection inserted on the right — because there the two $\tilde{\nabla}\Gamma$ terms do not cancel: the chain rule brings $\tilde{\nabla}\Gamma$ in from the left and the gauge shift removes it from the right, and the two differ by a commutator. The failure is explicit. Applying the mixed operator to $\lambda\tilde\Psi$ and subtracting $\lambda$ times the mixed operator applied to $\tilde\Psi$ leaves

$$
\frac{iϙ}{\hbar}\,\lambda\left[\tilde{\nabla}\Gamma,\ \tilde\Psi\right],
$$

which vanishes for every field only when $\tilde{\nabla}\Gamma$ is central, that is, only when the gauge function is constant. The two consistent constructions correspond to the two ways the algebra can act on the field, and the choice between them is a choice of **matter representation**: on which module, and from which side, the Dirac field sits. The gauge principle article records this as an open question, and this article does not resolve it; it states the left-action form, which is the one the gauge principle produces, and records the right-action mirror as the alternative.

### Which equation, and on which module

Three statements are in circulation. The first two carry the same mass term and differ in the module the field occupies, hence in what the central phase does to that mass term; the third differs in the mass term itself. The prescription of this article is the first.

**The chiral pair, written on the algebra.** The field is a biquaternion and $\lambda$ is one central element multiplying it from the left. Then the pair

$$
D\tilde\Psi_R = m\tilde\Psi_L, \qquad \bar D\tilde\Psi_L = m\tilde\Psi_R
$$

is covariant for the reason computed in the next section: $\lambda$ is central, so it passes through both gradients and through the mass, and no choice of module is needed for the statement.

**The same pair on the Dirac module.** The parent assigns the field to $\Delta = S\oplus S^{\mathrm{c}}$, with $\tilde\Psi_L = P_L\tilde\Psi$ and $\tilde\Psi_R = P_R\tilde\Psi$. There $S^{\mathrm{c}}$ carries the conjugate scalar action, so left multiplication by $\lambda$ multiplies the $S$ component by $\lambda$ and the $S^{\mathrm{c}}$ component by $\bar\lambda$ — the **axial** rotation, under which the mass term is not invariant. The phase that the standard theory gauges is the **vector** phase, which multiplies the two Weyl components alike and is therefore $\operatorname{diag}(\lambda,\lambda)$ on $\Delta$. That is not the parent's left action by any element of the algebra: that action acts by left multiplication on $S$ and by the conjugate of left multiplication on $S^{\mathrm c}$, so a central $\lambda$ reaches $\Delta$ as $(\lambda,\bar\lambda)$, and $\operatorname{diag}(\lambda,\lambda)$ would need $\lambda$ real. The algebra's theorem therefore holds as stated on the algebra and does not transfer to $\Delta$ unchanged; the point of failure is the mass term, and the difference of the two phases is the difference between the vector and the axial symmetry.

**The two-sided form.** The parent also carries Kravchenko's equation, a single equation on $F\in\mathbb{B}$ in which the derivative acts on the left and the mass term on the right (*The Dirac Equation in Biquaternionic Form*, §*The One-Sided and the Two-Sided Equation*),

$$
\mathcal{N}F = -\tilde{\nabla}^{\natural}F - m\,i\,\overline{F}\,\vec e_z = 0 ,
$$

the bar being the complex conjugation of the coefficients and not the real structure $\flat$. The mass term combines a right multiplication by $\vec e_z$, the central $i$ and that conjugation. On real quaternions the conjugation is inert and the operator is, up to the overall $-m$, the right multiplication by $i\vec e_z$ — the inner Peirce sign $R_{i\vec e_z}^{\mathrm{axf}}$ of the regular module, an involution because $(i\vec e_z)^2 = e_t$ — so there the mass enters as the eigenvalue of the copy label; on a general element of $\mathbb{B}$ the conjugation is not inert and the mass term is a right multiplication followed by a conjugation, not a single cell. Under a constant central phase $F\mapsto\lambda F$ the two terms scale differently,

$$
-\tilde{\nabla}^{\natural}\left(\lambda F\right) = \lambda\left(-\tilde{\nabla}^{\natural}F\right),
\qquad
-m\,i\,\overline{\lambda F}\,\vec e_z = \bar\lambda\left(-m\,i\,\overline{F}\,\vec e_z\right),
$$

and $\bar\lambda\ne\lambda$ for a non-real $\lambda$. The two-sided equation therefore has **no continuous central phase symmetry**: its symmetry group is the real rescalings $F\mapsto rF$, $r\in\mathbb{R}^{\times}$. There is no global phase to localize, so the minimal-coupling prescription cannot be transferred to it by the replacement $\partial\to D$; coupling that form would be a different construction, which this article does not attempt.

The three are one equation only in the sense that they carry the same operator content; they are not the same statement, and the passage from one to another is a change of representation. That is why the biquaternion form of the coupling is representation-dependent, and why the mass term is the place where the dependence shows.

## Gauge Covariance of the Coupled Equation

The gauge transformation is

$$
\tilde{\Psi}_2 = \lambda\,\tilde{\Psi}, \qquad \lambda = \exp(iϙ\Gamma(\tilde{Q})/\hbar), \qquad \Gamma \ \text{real},
$$

together with $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$. The covariance is the same computation as in the gauge principle article, repeated here because it is the justification of the prescription. The pair needs one Leibniz rule per member and one chain rule per member. For a central $\lambda$,

$$
\tilde{\nabla}\!\left(\lambda\tilde{\Psi}_R\right) = \lambda\,\tilde{\nabla}\tilde{\Psi}_R + \left(\tilde{\nabla}\lambda\right)\tilde{\Psi}_R,
\qquad
\tilde{\nabla}^{\natural}\!\left(\lambda\tilde{\Psi}_L\right) = \lambda\,\tilde{\nabla}^{\natural}\tilde{\Psi}_L + \left(\tilde{\nabla}^{\natural}\lambda\right)\tilde{\Psi}_L,
$$

and the chain rules are

$$
\tilde{\nabla}\lambda = \frac{iϙ}{\hbar}\left(\tilde{\nabla}\Gamma\right)\lambda ,
\qquad
\tilde{\nabla}^{\natural}\lambda = \frac{iϙ}{\hbar}\left(\tilde{\nabla}^{\natural}\Gamma\right)\lambda ,
$$

because $\lambda$ is a scalar function and each derivative acts on it componentwise. The first member then gives

$$
\begin{aligned}
D_2(\lambda\tilde{\Psi}_R)
&= \tilde{\nabla}(\lambda\tilde{\Psi}_R) + \frac{iϙ}{\hbar}\left(\tilde{A} - \tilde{\nabla}\Gamma\right)(\lambda\tilde{\Psi}_R) \\
&= \lambda\,\tilde{\nabla}\tilde{\Psi}_R + \frac{iϙ}{\hbar}\left(\tilde{\nabla}\Gamma\right)\lambda\tilde{\Psi}_R + \frac{iϙ}{\hbar}\lambda\,\tilde{A}\,\tilde{\Psi}_R - \frac{iϙ}{\hbar}\left(\tilde{\nabla}\Gamma\right)\lambda\tilde{\Psi}_R \\
&= \lambda\left[\tilde{\nabla}\tilde{\Psi}_R + \frac{iϙ}{\hbar}\tilde{A}\tilde{\Psi}_R\right] = \lambda\,D\tilde{\Psi}_R .
\end{aligned}
$$

The two $\tilde{\nabla}\Gamma$ terms cancel and the central $\lambda$ moves to the left. The second member repeats the computation with $\natural$ throughout, using $\tilde{A}_2^{\natural} = \tilde{A}^{\natural} - \tilde{\nabla}^{\natural}\Gamma$:

$$
\begin{aligned}
\bar{D}_2(\lambda\tilde{\Psi}_L)
&= \tilde{\nabla}^{\natural}(\lambda\tilde{\Psi}_L) + \frac{iϙ}{\hbar}\left(\tilde{A}^{\natural} - \tilde{\nabla}^{\natural}\Gamma\right)(\lambda\tilde{\Psi}_L) \\
&= \lambda\,\tilde{\nabla}^{\natural}\tilde{\Psi}_L + \frac{iϙ}{\hbar}\left(\tilde{\nabla}^{\natural}\Gamma\right)\lambda\tilde{\Psi}_L + \frac{iϙ}{\hbar}\lambda\,\tilde{A}^{\natural}\,\tilde{\Psi}_L - \frac{iϙ}{\hbar}\left(\tilde{\nabla}^{\natural}\Gamma\right)\lambda\tilde{\Psi}_L \\
&= \lambda\,\bar{D}\tilde{\Psi}_L .
\end{aligned}
$$

Both members are homogeneous, with the **same** factor $\lambda$:

$$
\boxed{\;D_2\tilde{\Psi}_{R,2} = \lambda\,D\tilde{\Psi}_R, \qquad \bar{D}_2\tilde{\Psi}_{L,2} = \lambda\,\bar{D}\tilde{\Psi}_L\;}
$$

Consequently the **massless minimally coupled biquaternion Dirac equation is exactly gauge covariant**:

$$
D\tilde{\Psi}_R = 0 \quad \Longleftrightarrow \quad D_2\tilde{\Psi}_{R,2} = 0, \qquad
\bar{D}\tilde{\Psi}_L = 0 \quad \Longleftrightarrow \quad \bar{D}_2\tilde{\Psi}_{L,2} = 0 .
$$

It holds in every gauge when it holds in one, and the phase of the field is not observable on its own. This is the charged massless fermion: the biquaternion form of the two decoupled Weyl fields.

The common factor $\lambda$ is the point to keep, and it follows from $\lambda$ being a central *scalar*: $\natural$ negates the three spatial units and fixes the coefficients, so it leaves the scalar $\lambda$ alone. On the Dirac module the same left multiplication acts as $\lambda$ on one chiral half and $\bar\lambda$ on the other, so the two members do not carry the same factor; the subsection *Which equation, and on which module* records where the difference sits.

**The second-order consequence.** The covariant derivative of the companion article satisfies the operator identity

$$
\bar{D}D = \sum_{\mu\in\{t,x,y,z\}} D_\mu^{2} + \frac{iϙ}{\hbar}\tilde{F}
$$

(*The Covariant Derivative and the Gauge Connection in Biquaternionic Form*). Applying $\bar{D}$ to the first member of the massive pair and using the second gives

$$
\bar{D}D\tilde{\Psi}_R = m\,\bar{D}\tilde{\Psi}_L = m^{2}\tilde{\Psi}_R,
$$

that is,

$$
\left(\sum_{\mu\in\{t,x,y,z\}} D_\mu^{2} + \frac{iϙ}{\hbar}\tilde{F} - m^{2}\right)\tilde{\Psi}_R = 0 ,
$$

a covariant wave equation with a curvature term. The corresponding statement for $\tilde\Psi_L$ carries $D\bar{D}$ in place of $\bar{D}D$. The parallel with the standard spinor-module square is an interpretation of this identity and not a derivation of it: there the second-order operator carries, beside the d'Alembertian, a contraction of the field strength with the spin tensor of the Lorentz generators; here the corresponding term is the algebra element $\frac{iϙ}{\hbar}\tilde{F}$ multiplying the field, and no Clifford matrix enters. The spin tensor needed for the comparison is the one defined in *The Legacy Gamma Formulation*.

## The Massive Case: Gauge Covariance and the Axial Symmetry

The massive equation is where the mass term's role is decided, and with the linear chiral pair it is benign. Suppose the minimally coupled massive equation holds in one gauge:

$$
D\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{D}\tilde{\Psi}_L = m\tilde{\Psi}_R .
$$

Because $D$ is covariant, the left-hand side of the transformed first equation is

$$
D_2\tilde{\Psi}_{R,2} = \lambda\,D\tilde{\Psi}_R ,
$$

and the right-hand side is the transformed mass term, which for a **linear** mass term carries the same factor:

$$
m\tilde{\Psi}_{L,2} = m\,\lambda\,\tilde{\Psi}_L .
$$

The two sides transform identically, because the central phase is a scalar and commutes with the mass. The same holds for the second equation, and with the **same** $\lambda$ rather than its conjugate: that is what the second display of the previous section establishes, the factor being $\lambda$ for either member. The massive coupled equation is therefore **form-invariant** under the local phase, and it holds in every gauge when it holds in one — exactly as in the massless case.

**Which module, and which phase.** The common factor $\lambda$ on both sides is a statement about left multiplication on the algebra. On the Dirac module the same left multiplication is the axial rotation, the two members acquire $\lambda$ and $\bar\lambda$, and the mass term is not invariant; the phase that the standard theory gauges is the vector one, and it is not a left multiplication there. The statement of this section is therefore the algebra's, and its transcription to the module is the matter-representation question of open question 2.

This is the biquaternion form of the standard fact that a mass term linear in the field is compatible with a gauged continuous $\mathrm{U}(1)$ (fermion number). The standard four-component Dirac equation has the linear mass term $m\psi$ and is gauge covariant under minimal coupling, and the biquaternion chiral pair is its algebra-level transcription. A mass term that instead pairs the field with its conjugate — a Majorana-type mass, built on the algebra's anti-Hermitian conjugation $\flat$, which is antilinear — would acquire the factor $\exp(2iϙ\Gamma/\hbar)$ and would be form-invariant only for $\lambda = \pm 1$. That obstruction is a property of the real structure $\flat$, not of the parent's mass term, and it belongs to the companion articles on the neutrino and on chirality rather than here.

**What it is not.** The article does not declare the standard minimal coupling deficient, and with the linear mass term it does not need to: the massive sector is gauge covariant on the same footing as the massless one, in the algebra form. What the biquaternion form adds is the algebra-level location of the coupling — the covariant derivative $D = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A}$ acting by left multiplication, with the central phase passing through the linear mass and the **axial** symmetry broken instead. The residual question of the left-versus-right matter representation is the parent's, and is collected in the open questions below.

**The interpretation that is taken.** The parent's linear mass term is read here as the real-form expression of an ordinary Dirac mass: the physical coupling is the standard spinor-module one, and the massive sector carries the charge. The alternative reading — that the framework's massive equation is a Majorana-type equation, with no continuously charged massive field — remains available, but only for a different equation, one genuinely built on $\flat$; it is a statement about the algebra's real structure rather than about the parent, and it is where the companion articles on the neutrino and on chirality continue the discussion.

## The Interaction Current and the Maxwell Source

Minimal coupling has a second half: the coupled field must **source** the electromagnetic field. In the biquaternion framework the sourced Maxwell equation is $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$, and the four-current $\tilde J$ satisfies the integrability condition $\sqrt{\mu}\,\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) = 0$, the biquaternionic form of charge conservation.

The natural candidate for the current of the Dirac field is the bilinear

$$
\tilde J_{\Psi} = i\,\tilde{\Psi}\,\tilde{\Psi}^{*} .
$$

Three of its properties are immediate and exact. It is **gauge invariant**, because for a unimodular central phase

$$
\left(\lambda\tilde{\Psi}\right)\left(\lambda\tilde{\Psi}\right)^{*} = \lambda\,\tilde{\Psi}\tilde{\Psi}^{*}\,\lambda^{*} = |\lambda|^2\,\tilde{\Psi}\tilde{\Psi}^{*} = \tilde{\Psi}\tilde{\Psi}^{*} ,
$$

and it is **anti-Hermitian**, $\tilde J_{\Psi}^{*} = -\tilde J_{\Psi}$, hence an element of the material sector $\mathbb{M}_-$ — the same sector as the four-current $ic\rho\,e_t + \vec J$ of the Maxwell article. The third property is the one that makes it a density candidate. The bilinear before the $i$ has the real scalar part

$$
\mathrm{Sc}\!\left(\tilde{\Psi}\tilde{\Psi}^{*}\right) = \|\tilde{\Psi}\|_E^2 \ \ge 0 ,
$$

the Euclidean modulus squared, so the scalar part of $\tilde J_{\Psi}$ itself is $i\,\|\tilde{\Psi}\|_E^2$: a positive imaginary number, of the $ic\rho$ form of a positive density with $c\rho = \|\tilde{\Psi}\|_E^2$. By these three tests it is a plausible current.

**It is not conserved.** The divergence of $\tilde J_{\Psi}$ in the $ict'$ convention is the scalar part of $\tilde{\nabla}^{\natural}\tilde J_{\Psi}$,

$$
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde J_{\Psi}\right) = \partial/\partial Q_t\,\mathrm{Sc}\left(\tilde J_\Psi\right) + \mathrm{div}\,\vec J,
$$

where $\vec J$ is the vector part of $\tilde J_\Psi$ — the quantity that would have to vanish on solutions. It does not, and one exact field is enough to show it. Take a biquaternion $\phi$ whose every component satisfies the scalar wave equation $\Box\phi = 0$; then

$$
\tilde{\Psi} = \tilde{\nabla}^{\natural}\phi
$$

satisfies $\tilde{\nabla}\tilde{\Psi} = \tilde{\nabla}\tilde{\nabla}^{\natural}\phi = \Box\phi = 0$; and since the gradient commutes with the central projectors, $\tilde{\nabla}\tilde{\Psi}_R = P_R\tilde{\nabla}\tilde{\Psi} = 0$, so it is a genuine solution of the massless equation. The simplest choice is a single plane wave with a null exponent,

$$
\phi = \exp\left(iQ_x - Q_t\right)e_t ,
\qquad
\Box\phi = \left(\partial^2/\partial Q_x^2 + \partial^2/\partial Q_t^2\right)\phi = -\phi + \phi = 0 .
$$

On it,

$$
\tilde{\Psi} = \left(-e_t - i\vec e_x\right)\phi ,
\qquad
\tilde J_{\Psi} = 2i\left(e_t + i\vec e_x\right)|\phi|^2 ,
\qquad
|\phi|^2 = e^{-2Q_t} ,
$$

the square $\left(-e_t - i\vec e_x\right)^2 = 2\left(e_t + i\vec e_x\right)$ having been used, and only the time derivative survives in the divergence:

$$
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde J_{\Psi}\right)
= \mathrm{Sc}\!\left(e_t\,\partial/\partial Q_t\,\tilde J_{\Psi}\right)
= -4i\,e^{-2Q_t} .
$$

It is $-4i$ at the origin and non-zero everywhere. The naive biquaternion product is therefore **not** the conserved electromagnetic current of the Dirac field. The sign of the bilinear does not help: with $\tilde J_{\Psi}^{*}$ in place of $\tilde J_{\Psi}$ the same computation gives $+4i\,e^{-2Q_t}$, because $\tilde J_\Psi^{*} = -\tilde J_\Psi$.

**Why, and what the current is instead.** The reason is representation-theoretic. The conserved current of the Dirac field is the spinor-module bilinear, built with the generator cell $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ of the coordinate $x_\mu$ — $\nu(t)=x$ and $\nu(k)=y$ — and with the **Dirac adjoint** $\bar\psi = \psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}$, the row spinor that pairs with the cell:

$$
j_\mu = \bar{\psi}\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\,\psi .
$$

Written out, the two $i$'s stand next to each other, and $i\cdot i = -1$:

$$
j_\mu = \psi^{\dagger}\,iR_{\vec e_x}^{\mathrm{axf}}\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\,\psi
= -\psi^{\dagger}R_{\vec e_x}^{\mathrm{axf}}L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\,\psi .
$$

The adjacent cells then combine into one, so the bilinear reduces to

$$
j_\mu =
\begin{cases}
\psi^{\dagger}\psi, & \mu = t,\\[4pt]
\psi^{\dagger}L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\psi, & \mu = k,
\end{cases}
$$

using $R_{\vec e_x}^{\mathrm{axf}}L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}} = -e_t$ and $R_{\vec e_x}^{\mathrm{axf}}L_{e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}} = -L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, which are the cell identities $(R_{\vec e_x}^{\mathrm{axf}})^{2} = -e_t$ and $\vec e_y\vec e_x = -\vec e_z$ read through $L_aR_bL_cR_d = L_{ac}R_{db}$. The time component is the density $\psi^{\dagger}\psi$ and the spatial ones are the usual $\psi^{\dagger}\alpha_k\psi$; that the reduction lands on those two is the check that the transcription is the standard one.

The factor $iR_{\vec e_x}^{\mathrm{axf}}$ is Clifford-**odd**. It is not in the even subalgebra $\mathbb{C}\ell_{1,3}^+ \cong \mathbb{B}$, and it is exactly the extra ingredient that the biquaternion formulation needs to recover the four-component Dirac spinor from its pair of Weyl spinors. A bilinear formed only from $\tilde{\Psi}$ and $\tilde{\Psi}^{*}$ inside $\mathbb{B}$ cannot supply it, which is why the naive product fails. The physical current therefore lies partly **outside** the algebra. That the electron's current is nevertheless an $\mathbb{M}_-$ four-vector — $\tilde J = ic\rho\,e_t + \vec J$ with $c\rho = \psi^{\dagger}\psi$ and $\vec J = \sum_k\left(\psi^{\dagger}L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}\psi\right)\vec e_k$ — is a statement about the spinor-module transcription, not about a product in $\mathbb{B}$.

This is the same representation question as the left/right action of the previous sections, met from the current side. The parent Dirac article's open question flags the representation conventions; this article records that they are not idle. The biquaternion form of the conserved current, and the sense in which the sourced Maxwell equation $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$ is fed by the Dirac field, remain open.

### An External Identity for the Source: The Mixed Invariant

The source term is the one element of the coupled system that the algebra has not supplied, and an outside treatment of a coupled biquaternionic Dirac field records an identity of exactly that kind. It is recorded here for its structure, and it is an external result, not a development of the framework.

The source is A. I. Arbab, *Coupling of a biquaternionic Dirac field to a bosonic field*, arXiv:1708.06230v2. It works with a matter field and a background boson field, writing for them a Maxwell-like system in ordinary units, with matter electric and magnetic fields $\vec E_D$ and $\vec B_D$, matter charge and current densities $\rho_D$ and $\vec J_D$, and boson potentials $\varphi_g$ and $\vec A_g$. Taking the divergence of its Faraday-like equation and eliminating the matter fields with the other equations of its system, it obtains

$$
\vec B_g\cdot\vec B_D - \frac{1}{c^2}\,\vec E_g\cdot\vec E_D
= \mu_0\left(\vec A_g\cdot\vec J_D - \varphi_g\,\rho_D\right),
$$

where $\vec E_g = -\nabla\varphi_g - \partial/\partial t'\,\vec A_g$ and $\vec B_g = \nabla\times\vec A_g$ are the boson's own electric and magnetic fields. The source cites its eqs. (5) and (8) for the elimination; the residual form given below shows what the identity rests on, namely the whole four-equation system, the Ampère-like equation included.

**What the identity says.** The left-hand side is a mixed invariant: the cross-contraction $\tfrac12\sum_{\mu,\nu}F_{g,\mu\nu}F_D^{\mu\nu}$ of the two field strengths. Written on the fields it is $\vec B_g\cdot\vec B_D - \vec E_g\cdot\vec E_D/c^2$, which is $-I_1^{\mathrm{cross}}/c^2$ with $I_1^{\mathrm{cross}} = \vec E_g\cdot\vec E_D - c^2\vec B_g\cdot\vec B_D$ — the two-field analogue of the corpus's $I_1 = \vec E^2 - c^2\vec B^2$, which contracts one field strength with itself.

The right-hand side is the pairing of the boson potential with the matter source. The identity therefore says that once two fields are coupled, their mixed invariant is not free: it is fixed by the source, and fixed by a source built linearly from the potential and the four-current. It is a constraint on the source, not an independent field equation, and it is the shape of answer that Open Question 4 asks for.

The source notes the two-field coincidence, where the identity reads $\epsilon_0\vec E^2 - \vec B^2/\mu_0 = \varphi\rho - \vec A\cdot\vec J$, that is, $\frac{1}{2\mu_0}\sum_{\mu,\nu}F_{\mu\nu}F^{\mu\nu} = -\sum_\sigma A_\sigma J^\sigma$ in the $(+{-}{-}{-})$ signature, the minus being the signature's; the mixed form above is the general one.

**Domain.** The matter fields of the source are built from its own biquaternion Dirac field, in its own conventions, and are read off a Maxwell-like system that costs one of the field's four components: the constraint $\psi_0 = -c\beta\sum_k iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\psi_k$ must be imposed, and the source's Appendix B gives the modified system that replaces it, with an extra real field $\Lambda=\beta\psi_0+c\sum_k iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\psi_k$ appearing in all four equations. The identity is therefore stated on the constrained system, and it is a statement about the source's field strengths, not about the corpus's $\tilde{\Psi}$ or about its $\sqrt{\mu}\,\tilde{J}$.

Written as a residual, with the source's own residual combinations $r_5,\dots,r_8$ of its fields — the vectors $\vec r_6,\vec r_7$ and the scalars $r_5,r_8$ —

$$
\vec B_g\cdot\vec B_D - \frac{1}{c^2}\vec E_g\cdot\vec E_D - \mu_0\left(\vec A_g\cdot\vec J_D - \varphi_g\rho_D\right)
= \frac{\hbar}{ϙ\,c}\,\nabla\cdot\vec r_6 + \vec A_g\cdot\vec r_7 - \frac{\varphi_g}{c^2}\,r_5 - \frac{\hbar}{ϙ\,c}\,\partial/\partial t'\,r_8 ,
$$

the identity holds exactly on the solution set of the four equations and not for arbitrary fields: the right-hand side collects the four residuals, each with the weight its own equation carries, and vanishes when all four are imposed.

**Not adopted.** The same source carries three further claims, and none of them is used here. It reports an inertial mass and a "magnetic mass" as separately conserved; its own continuity equation has a vanishing right-hand side, and the split into two separately vanishing continuity equations is declared — "the continuity equation dictates that it split" — rather than derived, and the source states that no further definition of the magnetic mass is given. It reads the photon as carrying a magnetic charge, quotes the product $ϙ_mϙ_e = \hbar/2$ as Dirac's quantisation rule, and reads that product as an uncertainty relation between two behaviours of one photon; the quantisation condition fixes the product $eg = 2\pi n\hbar c$ of a magnetic and an electric charge, and says nothing about the state of a single photon. And it presents Wilczek's axion electrodynamics as a special case reached by matching the axion derivatives to the potentials, which is a matching and not a derivation. The corpus records the identity above and cites the source for that identity alone.

## Recovering the Standard Minimal Coupling

The construction meets the standard theory in the spinor-module transcription. The biquaternion field, viewed as a $2\times2$ complex matrix, carries a pair of two-component spinors, and the biquaternion gradient is the Dirac operator of the algebra; $\mathbb{D}$ below is the pair operator of *Operator and Calculus Conventions*. Under that transcription, left multiplication by the connection $\tilde{A} = \sum_\mu A_\mu e_\mu$ is the representative of the spinor-module contraction of the four-potential with the four generators, and the coupled biquaternion equation becomes the standard minimally coupled Dirac equation — **provided the mass term is the linear Dirac mass** $m\psi$ — with $\mathbb{D}_A$ the pair operator with $\partial/\partial Q_\mu$ replaced by $D_\mu$:

$$
\boxed{\;\left(\mathbb{D}_A - \frac{mc}{\hbar}\right)\psi = 0\;}
$$

With the linear mass the equation is gauge covariant in the standard way, the conserved current is the spinor-module bilinear $j_\mu = \bar{\psi}\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\psi$, and the standard consequences — the tree-level gyromagnetic factor $g = 2$, the correct non-relativistic limit, the magnetic moment — follow by the computations of the companion articles on the electron and on the solutions and non-relativistic limit. Those results are not repeated here; the point for this article is that they are obtained with a **linear** mass term, which is exactly the form the parent's biquaternion equation carries, so the transcription and the standard treatment agree on the massive sector as well as on the massless one.

This is also where the module question of the previous subsection is answered in practice. On the four-component column the gauge transformation is the scalar multiplication $\psi\mapsto\lambda\psi$, which multiplies both Weyl components by the same factor, and the covariance checked in the standard theory is the covariance of that multiplication. The algebra's left action reproduces the connection term of the spinor-module derivative; how its scalar multiplication is to be written inside the algebra is the remaining question, and it is the one the module reading of $\Delta$ leaves open.

The transcription carries the representation conventions that the parent Dirac article explicitly left open — the identification of the biquaternion units with the Clifford generators, the placement of the two chiralities in the algebra, and the role of the Dirac adjoint. This article does not fix them. What it fixes is the biquaternion form of the coupling itself: the covariant derivative $D = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A}$ acting by left multiplication, the component operators $D_\mu = \partial/\partial Q_\mu + \frac{iϙ}{\hbar}A_\mu$, and the coupled equation $D\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{D}\tilde{\Psi}_L = m\tilde{\Psi}_R$.

## What the Algebra Supplies and What It Only Transcribes

What the algebra forces and what it merely rewrites in its own notation are easily conflated, and the separation is worth making explicit before the open questions.

**What the algebra supplies.**

- *A canonical abelian coupling.* The gauge group is the $*$-unitary part of the centre, and the centre is the only place a central phase can live. The $\mathrm{U}(1)$ that minimal coupling gauges is attached to the algebra without a choice of representation, as the gauge principle article establishes.
- *The covariant derivative as the localization of the phase.* The interaction term $\frac{iϙ}{\hbar}\tilde{A}\tilde{\Psi}$ is not added by hand: it is the term the localized phase forces, and the connection it forces is exactly the potential biquaternion of the Maxwell article.
- *Exact covariance of the coupled equation, in the massive case as well as the massless one*, with the component operators $D_\mu$ and the phase law $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$ inherited unchanged.
- *The second-order equation with its curvature term.* The operator identity $\bar{D}D = \sum_\mu D_\mu^2 + \frac{iϙ}{\hbar}\tilde{F}$ turns the coupled pair into a covariant wave equation carrying $\frac{iϙ}{\hbar}\tilde{F}$ as a term, with no Clifford matrix inserted by hand.
- *A material-sector connection.* For a real gauge function the connection stays in $\mathbb{M}_-$, so the coupling respects the sector decomposition the framework is built on.

**What it only transcribes.**

- *The minimal-coupling principle itself.* The derivation is the standard global-to-local argument carried into the biquaternion algebra. The algebra supplies a home for it and makes the component structure transparent; it does not supply a reason for the gauge field to exist.
- *The value of the coupling.* The charge $ϙ$ is a parameter; the algebra does not fix it.
- *The standard spinor-module results.* The conserved current, the non-relativistic limit, and $g=2$ are properties of the Dirac equation the framework contains, obtained with the linear mass term on the spinor module; the framework transcribes them.

**The commutativity that makes this unambiguous — and the sector where it fails.** The whole prescription rests on a property that this article has used without naming: for an internal gauge group the substitution $\partial \to D$ gives the same equation whether it is applied to the action or to the Euler–Lagrange equation of motion, so it does not matter which of the two is gauged. The reason is that the generators of an internal group act on an internal index, while the four matrices of the gradient act on the spinor index, so the two sets commute; the abelian $\mathrm{U}(1)$ of this article is the simplest case. The property is not universal. For a Dirac fermion coupled to gravity in the vierbein formulation the gauge generators are the Lorentz generators $S_{cd}$, which act on the spinor index itself and therefore do **not** commute with the matrices of the gradient — the commutator is stated and checked in *The Legacy Gamma Formulation* below — and the two procedures then differ by an anticommutator term. J. Fredsted (arXiv:1906.12200v3 [physics.gen-ph], 2019) proves the mismatch and constructs a world-index formalism in which it is removed, recorded in *Curved Spacetime and the Biquaternion Framework*. The consequence for this article is a boundary rather than a defect: the minimal-coupling prescription derived here is unambiguous **because** its gauge group is internal, and it must not be transferred to the gravitational sector unchanged, where the same prescription is a different and inequivalent construction.

**What is interpretation.** Reading the coupled equation as a Dirac field propagating in a background connection is a geometric interpretation. The algebraic content is the transformation law, the covariance of the coupled equation in both the massless and the massive case, and the explicit component form; the bundle picture is a consistent interpretation of that content, as in the gauge principle article.

## Open Questions

1. **The massive sector and the axial symmetry.** With the linear mass term the vector $\mathrm{U}(1)$ survives and the massive sector is gauge covariant in the algebra reading; on the Dirac module the same left multiplication is the axial rotation, so whether the massive sector is covariant depends on which module the field occupies, which is question 2. What the mass breaks is the axial symmetry between the two chiral halves. Can that symmetry be gauged, and does the framework's central-element structure supply anything analogous to the would-be Goldstone statement for the breaking? The Majorana-type alternative is a question about the algebra's real structure $\flat$ and not about the parent's mass term, which is linear; the companion on the neutrino takes it up.

2. **The matter representation.** The gauge principle produces a left-action covariant derivative; a right-action mirror is equally covariant, and the mixed insertion is not. Which action — which spinor module — is the physical Dirac field in? On $\Delta = S\oplus S^{\mathrm c}$ the vector phase is not a left multiplication by any element at all, so the module and the transformation law cannot be chosen independently. What fixes them inside the algebra?

3. **The interaction current.** The naive gauge-invariant bilinear $i\tilde{\Psi}\tilde{\Psi}^{*}$ is in $\mathbb{M}_-$ but is not conserved: the plane wave $\phi = \exp(iQ_x - Q_t)e_t$ gives $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde J_\Psi) = -4i\,e^{-2Q_t}$. The physical current uses the Clifford-odd $iR_{\vec e_x}^{\mathrm{axf}}$, outside $\mathbb{B}$. Is there a biquaternion-natural current, perhaps on a restricted module, or is the current irreducibly a representation-level object?

4. **The sourced system.** How does the Dirac current feed the biquaternionic Maxwell equation $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$, and does the coupled system close on the algebra or require the spinor module? The integrability condition $\sqrt{\mu}\,\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) = 0$ must be recovered from the current. The external identity of the section on the mixed invariant supplies the shape of an answer — the source contraction is fixed by the two field strengths — but it is stated for the source's own field strengths, not for $\tilde{\Psi}$, so it does not by itself close the corpus's system.

5. **The shared generator.** The internal phase $\exp(iϙ\Gamma/\hbar)$ and the complex time coordinate $ict'$ both use the single element $i$ of $\mathbb{B}$. Is this identification content-bearing, or vacuous because the phase is central? (The gauge principle article's open question.)

6. **The non-abelian extension.** When the connection becomes $\mathbb{B}$-valued, the field must be placed in a representation of the gauge group and the left/right question becomes sharp. The companions on the covariant derivative, on non-abelian fields and on the Yang–Mills equation place the field, but the choice is made there rather than forced.

7. **Empirical content.** As everywhere in the framework, the unresolved question is whether any of this yields a prediction distinguishing it from standard gauge theory. The minimal coupling as presented is a reformulation; the framework-level question of empirical contact remains open.

## The Legacy Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra, and they are used only in this section, as the frame in which the cells can be compared with the standard matrices.

Write $L_a\psi=a\psi$ and $R_b\psi=\psi b$ for the left and right multiplications of the regular module, and $c(M)$ for the matrix of a cell in the basis of the sixteen products. The four gammas and $\gamma_5$ are single cells:

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

A single cell is a tensor $a\otimes b$ read through $L_aR_b$, so its coefficient matrix has rank one; the cells form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and every element of $M_4(\mathbb{C})$ is a sum of at most four of them.

$\gamma_5$ is the reference-frame cell of the chirality operator; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module. That $\gamma_5$ has eigenvalues $\pm1$ with multiplicity two each is the module statement of $\chi^2=e_t$.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
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
The four contraction sums are frame statements, because a cell's square is. In the Euclidean frame, where every cell squares to $+I_4$,

$$
\sum_\mu\gamma_\mu\gamma_\mu=4I_4,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4\delta_{\alpha\beta}I_4,
$$
$$
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\delta\gamma_\mu=-2\,\gamma_\delta\gamma_\beta\gamma_\alpha .
$$

In the $\mathbb{M}_-$ frame the metric enters and $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The minimal coupling of the biquaternion Dirac field to electromagnetism is the replacement of the gradient by the covariant derivative of the gauge principle,

$$
D = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A}, \qquad D_\mu = \partial/\partial Q_\mu + \frac{iϙ}{\hbar}A_\mu,
$$

acting by left multiplication on the field. The coupled equation is

$$
D\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \bar{D}\tilde{\Psi}_L = m\tilde{\Psi}_R,
$$

that is,

$$
\tilde{\nabla}\tilde{\Psi}_R + \frac{iϙ}{\hbar}\tilde{A}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad
\tilde{\nabla}^{\natural}\tilde{\Psi}_L + \frac{iϙ}{\hbar}\tilde{A}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R,
$$

with the interaction term $\frac{iϙ}{\hbar}\tilde{A}\tilde{\Psi}$ that the localized central phase forces. In the massless case the two members decouple, $D\tilde{\Psi}_R = 0$ and $\bar{D}\tilde{\Psi}_L = 0$.

The **massless** and the **massive** coupled equations are both exactly gauge covariant: with $\tilde{\Psi}_2 = \exp(iϙ\Gamma/\hbar)\tilde{\Psi}$ and $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$,

$$
D_2\tilde{\Psi}_{R,2} = \lambda\,D\tilde{\Psi}_R, \qquad \bar{D}_2\tilde{\Psi}_{L,2} = \lambda\,\bar{D}\tilde{\Psi}_L,
$$

and the parent's linear mass term acquires the same factor $\lambda$, so $D\tilde{\Psi}_R = m\tilde{\Psi}_L$ holds in every gauge when it holds in one. The continuous $\mathrm{U}(1)$ of the massless theory survives the mass. Squaring the pair gives the covariant wave equation

$$
\left(\sum_{\mu\in\{t,x,y,z\}} D_\mu^{2} + \frac{iϙ}{\hbar}\tilde{F} - m^{2}\right)\tilde{\Psi}_R = 0 .
$$

The covariance statement is the algebra reading, in which $\lambda$ is one central element multiplying the field from the left. On the Dirac module the same left multiplication is the axial rotation: the two members acquire $\lambda$ and $\bar\lambda$, and the mass term is not invariant there. The biquaternion form of the statement that a Majorana-type mass term — built on the antilinear real structure $\flat$ — is incompatible with a gauged continuous $\mathrm{U}(1)$ is given in the companion articles on the neutrino and on chirality; the standard linear Dirac mass, which is the parent's form, does not have that obstruction, and on the spinor module the standard minimal coupling is recovered.

The interaction current is not a pure biquaternion product. The gauge-invariant, material-sector bilinear $i\tilde{\Psi}\tilde{\Psi}^{*}$ is not conserved on solutions of the massless equation: the field $\tilde\Psi = \tilde{\nabla}^{\natural}\phi$ built on the null plane wave $\phi = \exp(iQ_x - Q_t)e_t$ gives $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde J_\Psi) = -4i\,e^{-2Q_t}$. The physical current is the spinor-module bilinear $j_\mu = \bar{\psi}\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\psi$, whose Dirac adjoint uses the Clifford-odd $iR_{\vec e_x}^{\mathrm{axf}}$ outside $\mathbb{B}$; there the two $i$'s multiply to $-1$ and the adjacent cells combine, leaving $\psi^{\dagger}\psi$ for $\mu=t$ and $\psi^{\dagger}\alpha_k\psi$ for $\mu=k$. The pure-biquaternion form of the current, and the closure of the sourced system, are left as open questions, together with the choice of the left or right matter representation and the axial symmetry of the massive sector.

One external result is recorded on the source side, and it is not a development of the framework: the identity of A. I. Arbab (arXiv:1708.06230v2), by which the mixed invariant of the two coupled field strengths is fixed by the pairing of the potential with the four-current. It is a constraint following from that source's own four equations, verified exactly here, and its other claims are not adopted. It is recorded because it has the shape that Open Question 4 asks for, and because the corpus has no statement of that shape.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $\mathrm{Sc}(\tilde Q) = \tfrac12\,\mathrm{Tr}\,\tilde Q$ | Scalar part: the coefficient of $e_t$, and half the trace of the $2\times2$ matrix |
| $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$, $L_{a}R_{b}\psi = a\psi b$ | Generator cells; $iR_{\vec e_x}^{\mathrm{axf}} = iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ and $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Centre of the algebra; source of the abelian gauge group |
| $\tilde{\nabla} = e_t\partial/\partial Q_t + \sum_{k=x,y,z}\vec e_k\,\partial/\partial Q_k$ | Biquaternionic gradient (Dirac operator) |
| $\tilde{\nabla}^{\natural} = e_t\partial/\partial Q_t - \sum_{k=x,y,z}\vec e_k\,\partial/\partial Q_k$ | Quaternion-conjugate gradient |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla}$ | d'Alembertian |
| $\tilde{\Psi}$ | Biquaternion Dirac field; in the parent a section of $\Delta = S\oplus S^{\mathrm c}$ |
| $\tilde{\Psi}^\flat = -\tilde{\Psi}^{*}$, $\tilde{\Psi}^{*} = \overline{\tilde{\Psi}^{\natural}}$ | Anti-Hermitian conjugate of the field (the algebra's real structure; **not** the mass) |
| $\chi = i\tilde{\Xi}_{\mathrm{ad}} = e_+-e_-$, $P_{L,R} = \tfrac12(e_t\mp\chi)$ | Chirality (central sign of the complexification) and the chiral projectors; $\tilde\Psi_{L,R} = P_{L,R}\tilde\Psi$ |
| $\exp(i\alpha\chi)$ | Axial rotation; multiplies the two halves by $e^{\mp i\alpha}$ and is broken by the mass |
| $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$ | Free biquaternion Dirac equation (massive chiral pair) |
| $\tilde{A} = i\phi/c\,e_t + \vec A$ | Connection = potential biquaternion (in $\mathbb{M}_-$) |
| $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$ | Gauge transformation of the connection |
| $\lambda = \exp(iϙ\Gamma/\hbar)$ | Local central phase; $\Gamma$ real scalar |
| $ϙ$ | Charge (coupling constant), not fixed by the algebra |
| $D = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A}$ | Covariant derivative (left action) |
| $\bar{D} = \tilde{\nabla}^{\natural} + \frac{iϙ}{\hbar}\tilde{A}^{\natural}$ | Its $\natural$-image; the operator of the second member of the pair |
| $D_\mu = \partial/\partial Q_\mu + \frac{iϙ}{\hbar}A_\mu$ | Components; $\partial/\partial Q_t = -(i/c)\,\partial/\partial t'$ |
| $\nu(\mu)$ | Cell index: $\nu(t)=x$, $\nu(k)=y$ |
| $\alpha_k = L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | The spatial Dirac matrices in the cell frame (Hermitian, $\alpha_k^2 = I_4$) |
| $\tilde{F}$ | Field-strength biquaternion; $\bar{D}D = \sum_\mu D_\mu^2 + \frac{iϙ}{\hbar}\tilde{F}$ |
| $D\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\bar{D}\tilde{\Psi}_L = m\tilde{\Psi}_R$ | Minimally coupled Dirac equation |
| $\frac{iϙ}{\hbar}\tilde{A}\tilde{\Psi}$ | Interaction term |
| $\exp(2iϙ\Gamma/\hbar)$ | Phase that an antilinear (Majorana-type) mass term would acquire under a local phase; the linear mass term acquires $\lambda$ instead |
| $\|\tilde\Psi\|_E^2 = \mathrm{Sc}(\tilde\Psi\tilde\Psi^{*})$ | Euclidean modulus squared; real and $\ge 0$, the sum of the four squared coefficient moduli |
| $\tilde J_{\Psi} = i\tilde{\Psi}\tilde{\Psi}^{*}$ | Naive bilinear; gauge invariant, in $\mathbb{M}_-$, **not conserved** |
| $j_\mu = \bar{\psi}\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\psi$, $\bar{\psi} = \psi^\dagger iR_{\vec e_x}^{\mathrm{axf}}$ | Spinor-module conserved current (involves the Clifford-odd $iR_{\vec e_x}^{\mathrm{axf}}$) |
| $\tilde J = ic\rho\,e_t + \vec J$ | Four-current; the Maxwell source is $\sqrt{\mu}\,\tilde J$ |
| $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$ | Biquaternionic Maxwell equation |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Matrix trace against the scalar part; the reading used for the Euclidean modulus |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original equation and the minimal coupling.
- Hermann Weyl, "Elektron und Gravitation," *Zeitschrift für Physik* **56** (1929) 330–352, for the origin of the local phase and the gauge principle.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard treatment of minimal coupling, the conserved current, and the non-relativistic limit.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), and S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the standard abelian and non-abelian gauge couplings.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Majorana and Dirac mass terms and the fermion-number symmetry.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of the biquaternion algebra with the even part of $\mathrm{Cl}_{1,3}$ and the relation of the timelike generator to the even subalgebra.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the gauge-theoretic interpretation of the covariant derivative in geometric algebra.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of the Dirac equation in spacetime algebra.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component spinor calculus and the Dirac adjoint.
- J. Fredsted, "Obtaining consistent Lorentz gauging for a gravitationally coupled fermion," arXiv:1906.12200v3 [physics.gen-ph] (2019), for the external result recorded in *What the Algebra Supplies and What It Only Transcribes*: that for the Lorentz gauge group of the standard vierbein coupling, localization and the Euler–Lagrange variation do not commute, which is what makes the internal-gauge commutativity this article relies on a restriction and not a truism. Cited as an external claim; the gravitational construction is recorded in *Curved Spacetime and the Biquaternion Framework*.
- A. I. Arbab, "Coupling of a biquaternionic Dirac field to a bosonic field," arXiv:1708.06230v2 (2017), for the external identity recorded in *An External Identity for the Source: The Mixed Invariant*: with a background boson field $g$ and a matter field $D$, the mixed invariant of the two field strengths obeys $\vec B_g\cdot\vec B_D - c^{-2}\vec E_g\cdot\vec E_D = \mu_0(\vec A_g\cdot\vec J_D - \varphi_g\rho_D)$, a consequence of the source's own four Maxwell-like equations and verified here symbolically. Cited for that identity alone; the source's magnetic-mass, single-photon-charge and axion-reduction claims are not adopted.
- Companion articles: [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html); [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html); [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html); [The Electron in Biquaternionic Form](the-electron-in-biquaternionic-form.html); [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html); [Canonical Quantization of the Biquaternion Maxwell Field](canonical-quantization-of-the-biquaternion-maxwell-field.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html).
