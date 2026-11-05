# __The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism__

## Introduction

**Minimal coupling** is the prescription by which a charged field is coupled to the electromagnetic field: the ordinary derivative is replaced by the **covariant derivative**. In the biquaternion framework both objects are already fixed by the gauge principle. The connection is the potential biquaternion $\tilde{A}$ of *Maxwell's Equations in the Biquaternionic Formulation*, its gauge transformation is

$$
\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma,
$$

and the covariant derivative is

$$
\tilde\nabla^{\mathrm{gco}} = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A} .
$$

The gauge principle article derived $\tilde\nabla^{\mathrm{gco}}$ from the localization of the algebra's central phase and verified that the covariant derivative of a field transforms homogeneously. It applied the result to a general element, not specifically to the Dirac field. *The Dirac Equation in Biquaternionic Form* names the minimal coupling of the Dirac field as the subject of the companion treatment (its open question 7), and the coupled equation is not fixed by the free equation alone. This article supplies that statement, and reports what the recomputation gives.

Three results are established here.

1. **The coupled equation.** Replacing the gradient in the free biquaternion Dirac equation by the covariant derivative gives the pair $\tilde\nabla^{\mathrm{gco}}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde\nabla^{\mathrm{gco},\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$. The second operator is the $\natural$-image of the first, so it carries the quaternion-conjugate gradient and the conjugate connection.
2. **Exact gauge covariance, massive as well as massless.** The pair holds in every gauge when it holds in one, because the parent's mass term is linear in the field and the local phase is one central scalar multiplying the field from the left, so the mass term acquires the same factor as the derivative term. The mass breaks the *relative* phase of the two parts, not the common one.
3. **A negative result on the current.** The bilinear $i\tilde{\Psi}\tilde{\Psi}^{*}$ is a material-sector object and is gauge invariant, but it is **not conserved** on solutions of the massless equation: the exact solution written in the section on the current gives $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}_\Psi) = -2i\,e^{-2Q_t}$. The electromagnetic current of the coupled system is therefore not a product of the field with its conjugate inside the algebra.

The division between what is established and what is interpretation is stated at the outset and kept explicit.

- **Established, and recomputed below.** The minimal-coupling prescription acting on the biquaternion Dirac field by left multiplication; the coupled equation and its component form; the exact gauge covariance of the coupled equation, in the massive case as well as the massless one; the gauge invariance and material-sector membership of $i\tilde{\Psi}\tilde{\Psi}^{*}$; the non-conservation of that bilinear, exhibited on an exact solution rather than asserted; the reason the prescription attaches to the pair and not to the two-sided form of the parent.
- **Interpretation.** Interpreting the coupled equation as "the Dirac field in a background electromagnetic connection" is a geometric interpretation of an algebraic construction. The algebra supplies the transformation law and the covariance; the connection/curvature picture is a consistent interpretation, as in the gauge principle article.
- **Gaps, left visible.** No product of the field with its conjugate that the algebra offers is conserved, and which object the conserved interaction current is remains open. Whether the physical field is the one the connection multiplies from the left or its $\natural$-image is a choice the parent left open. The relative phase broken by the mass, and whether it can be gauged, is not treated here. These are stated as gaps in the sections where they arise and collected in the open questions.

The article is organized as follows. The next section recalls the Dirac field, its two values of the subscript, and the phase symmetry that is to be localized. The section after that states the minimal-coupling prescription, and a subsection of it separates the two forms of the Dirac equation that the corpus carries on the algebra — the one-sided pair and the two-sided form with the conjugation in the mass term — and states why the prescription attaches to the first. The following section proves the covariance in the massless case and fixes the sign conventions. The next section treats the massive case, where the linear mass term preserves the covariance and the relative phase is what the mass breaks. A section examines the interaction current and the Maxwell source, reports the negative result on an explicit solution, and records one external identity of the same shape, due to Arbab, which is verified here and cited without being adopted as framework content. A section separates what the algebra supplies from what it only transcribes. The article then collects the open questions, and a closing section fixes the frame in which the cells are compared with the standard matrices, and that section is the only place in which those matrices appear.

## The Dirac Field and Its Phase Symmetry

The **biquaternion Dirac field** is an element $\tilde{\Psi}(\tilde{Q}) \in \mathbb{B}$ satisfying the free equation

$$
\tilde{\nabla}\tilde{\Psi}_R = m\,\tilde{\Psi}_L, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\,\tilde{\Psi}_R .
$$

The two members are the **chiral pair**. The first acts on the $R$ part of the field by the gradient, the second on the $L$ part by the quaternion conjugate of the gradient. When $m = 0$ they decouple,

$$
\tilde{\nabla}\tilde{\Psi}_R = 0, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L = 0 .
$$

The first member is then identical in form to the source-free biquaternion Maxwell equation obeyed by the field-strength biquaternion $\tilde{F}$; the difference is the carrier, the Maxwell field being an element of the vector part and the Dirac field a general element.

**The two values of the subscript.** The field is an element, and it is written as the sum of its two parts,

$$
\tilde{\Psi} = \tilde{\Psi}_L + \tilde{\Psi}_R .
$$

The subscript takes two values and no more. It belongs to the element and not to the equation: a general element, a product, a unit and a field all carry it. The two values are exactly two, and only the zero element carries both. The value is read from the chirality cell of the declared frame (*Special Element Conventions*, §*The Chirality Convention*); the article writes the value and never computes it.

Three facts about the letters are used below. The first two are the convention's own statement, and the third follows from the first.

- **Left multiplication keeps the letter.** For a central scalar $\lambda$, the parts of $\lambda\tilde{\Psi}$ are $\lambda\tilde{\Psi}_L$ and $\lambda\tilde{\Psi}_R$.
- **A product takes the letter of its right factor.** In particular the products of the next sections carry the letter of the factor on the right.
- **The gradient keeps the letter.** The gradient acts by left multiplication by the four units and by differentiating the coefficients, and neither operation moves an element out of its part. Hence the gradient of a field whose $L$ part vanishes has only an $R$ part, and conversely.

**The real structure.** The algebra's anti-Hermitian conjugation

$$
\tilde{\Psi}^\flat = -\tilde{\Psi}^{*} = -\overline{\tilde{\Psi}^{\natural}}
$$

is an antilinear involution whose fixed space is the material sector $\mathbb{M}_-$. It is the algebra's real structure, and it is not the mass.

**The phase symmetry to be localized.** The symmetry that minimal coupling localizes is the algebra's central $\mathrm{U}(1)$, established in the gauge principle article. A **constant** central phase

$$
\tilde{\Psi} \;\longmapsto\; \exp(i\theta)\tilde{\Psi}, \qquad \theta \ \text{constant},
$$

is a symmetry of the equation, massive or massless, because a central constant commutes with the units and with the derivatives and therefore passes through both members of the pair:

$$
\tilde{\nabla}\!\left(\lambda\tilde{\Psi}_R\right) = \lambda\,\tilde{\nabla}\tilde{\Psi}_R, \qquad
\tilde{\nabla}^{\natural}\!\left(\lambda\tilde{\Psi}_L\right) = \lambda\,\tilde{\nabla}^{\natural}\tilde{\Psi}_L .
$$

One and the same $\lambda$ multiplies both members. The pair therefore scales uniformly, and the mass term, which is linear in the field, is invariant.

**What the mass breaks is the relative phase.** With $\varkappa$ a nonzero central constant, the massless pair is invariant under

$$
\tilde{\Psi}_R \;\longmapsto\; \varkappa\,\tilde{\Psi}_R, \qquad \tilde{\Psi}_L \;\longmapsto\; \varkappa^{-1}\,\tilde{\Psi}_L ,
$$

because each member acquires the product $\varkappa\varkappa^{-1} = 1$. The massive pair is not: its two sides acquire $\varkappa$ and $\varkappa^{-1}$, so it is form-invariant only for $\varkappa^2 = 1$, and for a central constant that is $\varkappa = \pm 1$. A local $\varkappa$ fails already in the massless case, because the derivative acts on $\varkappa$ and the two members acquire derivative terms that do not cancel. The mass therefore keeps the common phase and breaks the relative one. Whether the relative one can be gauged is open question 1.

A mass term that *paired the field with its conjugate* would be a different object: $\flat$ is antilinear, $(\lambda\tilde{\Psi})^\flat = \lambda^{*}\tilde{\Psi}^\flat$ for a central phase, so such a term would acquire the factor $\exp(2iϙ\Gamma/\hbar)$ under a local phase and would be form-invariant only for $\lambda = \pm 1$. That obstruction belongs to the real structure and is treated in the companion articles on the neutrino and on the two kinds of mass; it is not a property of the parent's mass term, which pairs $\tilde{\Psi}_L$ with $\tilde{\Psi}_R$.

The **charge** $ϙ$ is the coupling constant of the field, introduced by the gauge principle. It is a parameter: the algebra does not fix its value, its sign, or its quantization. For the electron $ϙ = -e$; the value and the sign are inserted, as *The Electron in Biquaternionic Form* records.

## The Minimal Coupling Prescription

The prescription replaces the gradient in the free equation by the covariant derivative. Written out as an action on the field,

$$
\tilde{\Psi} \;\longmapsto\; \tilde{\nabla}\tilde{\Psi} + \frac{iϙ}{\hbar}\,\tilde{A}\,\tilde{\Psi},
$$

that is, $\tilde\nabla^{\mathrm{gco}} = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A}$ acting by **left multiplication**. Applied to the free Dirac equation in its linear form, the prescription gives the **minimally coupled biquaternion Dirac equation**

$$
\boxed{\ \tilde\nabla^{\mathrm{gco}}\tilde{\Psi}_R = m\,\tilde{\Psi}_L, \qquad \tilde\nabla^{\mathrm{gco},\natural}\tilde{\Psi}_L = m\,\tilde{\Psi}_R\ }
$$

with $\tilde\nabla^{\mathrm{gco},\natural} := \tilde{\nabla}^{\natural} + \frac{iϙ}{\hbar}\tilde{A}^{\natural}$ — the quaternion conjugate of the operator, not the operator of the opposite charge — that is,

$$
\tilde{\nabla}\tilde{\Psi}_R + \frac{iϙ}{\hbar}\,\tilde{A}\,\tilde{\Psi}_R = m\,\tilde{\Psi}_L, \qquad \tilde{\nabla}^{\natural}\tilde{\Psi}_L + \frac{iϙ}{\hbar}\,\tilde{A}^{\natural}\,\tilde{\Psi}_L = m\,\tilde{\Psi}_R,
$$

and in the massless case the two members decouple separately,

$$
\tilde\nabla^{\mathrm{gco}}\tilde{\Psi}_R = 0, \qquad \tilde\nabla^{\mathrm{gco},\natural}\tilde{\Psi}_L = 0 .
$$

The term $\frac{iϙ}{\hbar}\tilde{A}\tilde{\Psi}$ is the **interaction term**. It is exactly the term that the localization of the phase forces, and the connection it forces is the potential biquaternion of the Maxwell article.

**Component form.** Write the potential as $\tilde{A} = \sum_\mu A_\mu e_\mu$ with complex scalar coefficients $A_\mu$ — the abelian case, in which the connection coefficients are central scalars and commute with one another and with the units. Since each $A_\mu$ is central, the covariant derivative separates into components:

$$
\tilde\nabla^{\mathrm{gco}} = \sum_{\mu\in\{t,x,y,z\}} e_\mu\,\tilde\nabla^{\mathrm{gco}}_\mu,
\qquad
\tilde\nabla^{\mathrm{gco}}_\mu = \partial/\partial Q_\mu + \frac{iϙ}{\hbar}A_\mu,
$$

with $\partial/\partial Q_t = -(i/c)\,\partial/\partial t'$ and $\partial/\partial Q_k = \partial/\partial x_k$. This is the identical component form derived in the gauge principle article, now read as an operator on the Dirac field. Setting $\hbar = 1$ gives $\tilde\nabla^{\mathrm{gco}}_\mu = \partial/\partial Q_\mu + iϙA_\mu$, the convention used for the minimal substitution in the companion article on the solutions and the non-relativistic limit.

**The connection is a material-sector object.** The gauge principle article shows that a **real** gauge function $\Gamma$ keeps $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$ in $\mathbb{M}_-$. The coupling is therefore the coupling of the Dirac field to a material-sector connection, and the ingredient $\frac{iϙ}{\hbar}\tilde{A}$ in $\tilde\nabla^{\mathrm{gco}}$ is Hermitian:

$$
\left(i\tilde{A}\right)^{*} = -i\,\tilde{A}^{*} = i\tilde{A},
$$

since $\tilde{A}^{*} = -\tilde{A}$ on $\mathbb{M}_-$. The factor $i$ is what converts the anti-Hermitian connection into a Hermitian coupling. This is inherited, not rederived.

**Sign convention.** The gauge principle article fixes the pair of signs $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$ and $\tilde\nabla^{\mathrm{gco}} = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A}$ with the phase $\lambda = \exp(iϙ\Gamma/\hbar)$, and its companion records that the two must be kept together. The open question in the parent Dirac article writes the standard physics convention $\partial/\partial Q_\mu \to \partial/\partial Q_\mu - iϙA_\mu/\hbar$, with the opposite sign. That is the same coupling with the opposite sign of $ϙ$ (or of $\tilde{A}$); this article inherits the gauge principle's sign and does not silently flip it. The covariance checks below use the inherited pair.

**Left action, and the mirror read through $\natural$.** Every coupling used in this article acts on the left. The mirror construction — derivative and connection both inserted on the right — is not a second prescription: it is the same one applied to the conjugate field. The renaming theorem of *Operator and Calculus Conventions*, §*The Two Sides and the Renaming Theorem*, gives $(\tilde{\Psi}\tilde\nabla^{\mathrm{gco}})^{\natural} = \tilde\nabla^{\mathrm{gco},\natural}\tilde{\Psi}^{\natural}$; the right-action equation on $\tilde\Psi$ is the left-action equation on $\tilde\Psi^{\natural}$, with the operator $\tilde\nabla^{\mathrm{gco},\natural}$ that the second member of the pair already carries. Nothing needs a right arrow: the side is given by position, and $\natural$ is what changes it.

Both constructions are gauge covariant, and they must be, being the same construction seen through $\natural$. What is **not** covariant is the mixed combination — the left gradient with the connection inserted on the right — because there the two $\tilde{\nabla}\Gamma$ terms do not cancel: the chain rule brings $\tilde{\nabla}\Gamma$ in from the left and the gauge shift removes it from the right, and the two differ by a commutator. Applying the mixed operator to $\lambda\tilde\Psi$ and subtracting $\lambda$ times the mixed operator applied to $\tilde\Psi$ leaves

$$
\frac{iϙ}{\hbar}\,\lambda\left[\tilde{\nabla}\Gamma,\ \tilde{\Psi}\right],
$$

which vanishes for every field only when $\tilde{\nabla}\Gamma$ is central, that is, only when the gauge function is constant. The two consistent constructions correspond to the two sides on which the algebra can act, and the choice between them is a choice of matter representation: from which side the connection multiplies the field. The gauge principle article records this as an open question, and this article does not resolve it; it states the left-action form, which is the one the gauge principle produces, and records the right-action mirror as the alternative.

### Which Equation the Prescription Attaches To

Two forms are in circulation on the algebra, and the prescription of this article attaches to the first.

**The pair.** The field is an element and $\lambda$ is one central element multiplying it from the left. Then the pair

$$
\tilde\nabla^{\mathrm{gco}}\tilde\Psi_R = m\tilde\Psi_L, \qquad \tilde\nabla^{\mathrm{gco},\natural}\tilde\Psi_L = m\tilde\Psi_R
$$

is covariant for the reason computed in the next section: $\lambda$ is central, so it passes through both gradients and through the mass.

**The two-sided form.** The parent also carries Kravchenko's equation, a single equation on a general element $F$ in which the derivative acts on the left and the mass term on the right (*The Dirac Equation in Biquaternionic Form*, §*The One-Sided and the Two-Sided Equation*), with $\vec u$ the declared unit of the frame:

$$
\mathcal{N}F = -\tilde{\nabla}^{\natural}F - m\,i\,\overline{F}\,\vec u = 0 ,
$$

the bar being the complex conjugation of the coefficients and not the real structure $\flat$. The mass term combines a conjugation, the central $i$ and a right multiplication by $\vec u$, and it is not a scalar multiple of the field.

**Why the prescription attaches to the pair.** Under a constant central phase $F\mapsto\lambda F$ the two terms of the two-sided form scale differently,

$$
-\tilde{\nabla}^{\natural}\left(\lambda F\right) = \lambda\left(-\tilde{\nabla}^{\natural}F\right),
\qquad
-m\,i\,\overline{\lambda F}\,\vec u = \bar\lambda\left(-m\,i\,\overline{F}\,\vec u\right),
$$

and $\bar\lambda\ne\lambda$ for a non-real $\lambda$. The two-sided form therefore has **no continuous central phase symmetry**: its symmetry group is the real rescalings $F\mapsto rF$, $r\in\mathbb{R}^{\times}$. There is no phase to localize, so the minimal-coupling prescription cannot be transferred to it by replacing the gradient with the covariant derivative; coupling that form would be a different construction, which this article does not attempt.

The two forms carry the same operator content and are not the same statement: the mass term of the second is a conjugation and a right multiplication, and it is the place where the difference shows. That is why the biquaternion form of the coupling is not fixed by the free equation alone. The third object of the older literature, on which the central phase reaches the field one way on one part and the other way on the other, is named in the closing section and is not used as a tool anywhere in this article.

## Gauge Covariance of the Coupled Equation

The gauge transformation is

$$
\tilde{\Psi}_2 = \lambda\,\tilde{\Psi}, \qquad \lambda = \exp(iϙ\Gamma(\tilde{Q})/\hbar), \qquad \Gamma \ \text{real},
$$

together with $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$. The covariance is the same computation as in the gauge principle article, repeated here because it is the justification of the prescription. The pair needs one Leibniz rule per member and one chain rule per member. The chain rules are

$$
\tilde{\nabla}\lambda = \frac{iϙ}{\hbar}\left(\tilde{\nabla}\Gamma\right)\lambda ,
\qquad
\tilde{\nabla}^{\natural}\lambda = \frac{iϙ}{\hbar}\left(\tilde{\nabla}^{\natural}\Gamma\right)\lambda ,
$$

because $\lambda$ is a central scalar function and each derivative acts on it coefficient by coefficient. The first member then gives

$$
\begin{aligned}
\tilde\nabla^{\mathrm{gco}}_{2}(\lambda\tilde{\Psi}_R)
&= \tilde{\nabla}(\lambda\tilde{\Psi}_R) + \frac{iϙ}{\hbar}\left(\tilde{A} - \tilde{\nabla}\Gamma\right)(\lambda\tilde{\Psi}_R) \\
&= \lambda\,\tilde{\nabla}\tilde{\Psi}_R + \frac{iϙ}{\hbar}\left(\tilde{\nabla}\Gamma\right)\lambda\tilde{\Psi}_R + \frac{iϙ}{\hbar}\lambda\,\tilde{A}\,\tilde{\Psi}_R - \frac{iϙ}{\hbar}\left(\tilde{\nabla}\Gamma\right)\lambda\tilde{\Psi}_R \\
&= \lambda\left[\tilde{\nabla}\tilde{\Psi}_R + \frac{iϙ}{\hbar}\tilde{A}\tilde{\Psi}_R\right] = \lambda\,\tilde\nabla^{\mathrm{gco}}\tilde{\Psi}_R .
\end{aligned}
$$

The two $\tilde{\nabla}\Gamma$ terms cancel, and the central $\lambda$ moves to the left, past $\tilde{A}$ and past the field. The second member repeats the computation with $\natural$ throughout, using $\tilde{A}_2^{\natural} = \tilde{A}^{\natural} - \tilde{\nabla}^{\natural}\Gamma$:

$$
\begin{aligned}
\tilde\nabla^{\mathrm{gco},\natural}_{2}(\lambda\tilde{\Psi}_L)
&= \tilde{\nabla}^{\natural}(\lambda\tilde{\Psi}_L) + \frac{iϙ}{\hbar}\left(\tilde{A}^{\natural} - \tilde{\nabla}^{\natural}\Gamma\right)(\lambda\tilde{\Psi}_L) \\
&= \lambda\,\tilde{\nabla}^{\natural}\tilde{\Psi}_L + \frac{iϙ}{\hbar}\left(\tilde{\nabla}^{\natural}\Gamma\right)\lambda\tilde{\Psi}_L + \frac{iϙ}{\hbar}\lambda\,\tilde{A}^{\natural}\,\tilde{\Psi}_L - \frac{iϙ}{\hbar}\left(\tilde{\nabla}^{\natural}\Gamma\right)\lambda\tilde{\Psi}_L \\
&= \lambda\,\tilde\nabla^{\mathrm{gco},\natural}\tilde{\Psi}_L .
\end{aligned}
$$

Both members are homogeneous, with the **same** factor $\lambda$:

$$
\boxed{\;\tilde\nabla^{\mathrm{gco}}_{2}\tilde{\Psi}_{R,2} = \lambda\,\tilde\nabla^{\mathrm{gco}}\tilde{\Psi}_R, \qquad \tilde\nabla^{\mathrm{gco},\natural}_{2}\tilde{\Psi}_{L,2} = \lambda\,\tilde\nabla^{\mathrm{gco},\natural}\tilde{\Psi}_L\;}
$$

Consequently the **massless minimally coupled biquaternion Dirac equation is exactly gauge covariant**:

$$
\tilde\nabla^{\mathrm{gco}}\tilde{\Psi}_R = 0 \quad \Longleftrightarrow \quad \tilde\nabla^{\mathrm{gco}}_{2}\tilde{\Psi}_{R,2} = 0, \qquad
\tilde\nabla^{\mathrm{gco},\natural}\tilde{\Psi}_L = 0 \quad \Longleftrightarrow \quad \tilde\nabla^{\mathrm{gco},\natural}_{2}\tilde{\Psi}_{L,2} = 0 .
$$

It holds in every gauge when it holds in one, and the phase of the field is not observable on its own. The common factor $\lambda$ is the point to keep, and it follows from $\lambda$ being a central *scalar*: $\natural$ negates the three spatial units and fixes the coefficients, so it leaves the scalar $\lambda$ alone.

**The second-order consequence.** The covariant derivative of the companion article satisfies the operator identity

$$
\tilde\nabla^{\mathrm{gco},\natural}\tilde\nabla^{\mathrm{gco}} = \sum_{\mu\in\{t,x,y,z\}} \tilde\nabla^{\mathrm{gco}}_\mu^{2} + \frac{iϙ}{\hbar}\tilde{F}
$$

(*The Covariant Derivative and Gauge Connection in Biquaternionic Form*), the scalar part being the covariant d'Alembertian and the vector part the curvature. Applying $\tilde\nabla^{\mathrm{gco},\natural}$ to the first member of the massive pair and using the second gives

$$
\tilde\nabla^{\mathrm{gco},\natural}\tilde\nabla^{\mathrm{gco}}\tilde{\Psi}_R = m\,\tilde\nabla^{\mathrm{gco},\natural}\tilde{\Psi}_L = m^{2}\tilde{\Psi}_R,
$$

that is,

$$
\left(\sum_{\mu\in\{t,x,y,z\}} \tilde\nabla^{\mathrm{gco}}_\mu^{2} + \frac{iϙ}{\hbar}\tilde{F} - m^{2}\right)\tilde{\Psi}_R = 0 ,
$$

a covariant wave equation with a curvature term. The corresponding statement for $\tilde\Psi_L$ carries $\tilde\nabla^{\mathrm{gco}}\tilde\nabla^{\mathrm{gco},\natural}$ in place of $\tilde\nabla^{\mathrm{gco},\natural}\tilde\nabla^{\mathrm{gco}}$. The curvature term is the algebra element $\frac{iϙ}{\hbar}\tilde{F}$ multiplying the field; no further object is introduced, and the comparison of this second-order operator with the one of the older literature is a matter of display and is not made in this article.

## The Massive Case: Gauge Covariance and the Broken Relative Phase

The massive equation is where the mass term's role is decided, and with the linear pair it is benign. Suppose the minimally coupled massive equation holds in one gauge:

$$
\tilde\nabla^{\mathrm{gco}}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \tilde\nabla^{\mathrm{gco},\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R .
$$

Because $\tilde\nabla^{\mathrm{gco}}$ is covariant, the left-hand side of the transformed first equation is

$$
\tilde\nabla^{\mathrm{gco}}_{2}\tilde{\Psi}_{R,2} = \lambda\,\tilde\nabla^{\mathrm{gco}}\tilde{\Psi}_R ,
$$

and the right-hand side is the transformed mass term, which for a **linear** mass term carries the same factor:

$$
m\tilde{\Psi}_{L,2} = m\,\lambda\,\tilde{\Psi}_L .
$$

The two sides transform identically, because the central phase is a scalar and the mass is one. The same holds for the second equation, and with the **same** $\lambda$ rather than its conjugate: the factor is $\lambda$ for either member. The massive coupled equation is therefore **form-invariant** under the local phase, and it holds in every gauge when it holds in one — exactly as in the massless case.

This is the biquaternion form of the standard fact that a mass term linear in the field is compatible with a gauged continuous $\mathrm{U}(1)$. The two parts of the field acquire the same phase; what the mass forbids is the opposite assignment of the two, as the section on the field records.

**What it is not.** The article does not declare the standard minimal coupling deficient, and with the linear mass term it does not need to: the massive sector is gauge covariant on the same footing as the massless one. What the biquaternion form adds is the location of the coupling in the algebra — the covariant derivative acting by left multiplication, with the central phase passing through the linear mass and the relative phase broken instead. The residual question of the left-versus-right matter representation is the parent's, and is collected in the open questions below.

**The interpretation that is taken.** The parent's linear mass term is read here as the expression of an ordinary Dirac mass: a term that pairs the two parts of one element, and therefore carries the charge. The alternative reading — a mass term built on the real structure $\flat$, with no continuously charged massive field — remains available, but only for a different equation, one genuinely built on $\flat$; it is a statement about the algebra's real structure rather than about the parent, and it is where the companion articles on the neutrino and on the two kinds of mass continue the discussion.

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

and it is **anti-Hermitian**, $\tilde J_{\Psi}^{*} = -\tilde J_{\Psi}$, hence an element of the material sector $\mathbb{M}_-$ — the same sector as the four-current $ic\rho\,e_t + \vec J$ of the Maxwell article. The third property makes it a density candidate: the bilinear before the $i$ has the real scalar part

$$
\mathrm{Sc}\!\left(\tilde{\Psi}\tilde{\Psi}^{*}\right) = \|\tilde{\Psi}\|_E^2 \ \ge 0 ,
$$

the square of the topological norm, so the scalar part of $\tilde J_{\Psi}$ itself is $i\,\|\tilde{\Psi}\|_E^2$ — a positive imaginary number, of the $ic\rho$ form of a positive density with $c\rho = \|\tilde\Psi\|_E^2$. By these three tests it is a plausible current.

**It is not conserved.** The divergence of $\tilde J_{\Psi}$ in the $ict'$ convention is the scalar part of $\tilde{\nabla}^{\natural}\tilde J_{\Psi}$,

$$
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde J_{\Psi}\right) = \frac{\partial}{\partial Q_t}\mathrm{Sc}\left(\tilde J_\Psi\right) + \mathrm{div}\,\vec J,
$$

where $\vec J$ is the vector part of $\tilde J_\Psi$ — the quantity that would have to vanish on solutions. It does not, and one exact solution is enough to show it. Take

$$
\phi = \exp\left(iQ_x - Q_t\right), \qquad
\tilde{\Psi}_R = \tfrac12\,\phi\left(-e_t - i\vec e_x + \vec e_y + i\vec e_z\right).
$$

The element in brackets is constant, so the gradient acts on $\phi$ alone, and

$$
\tilde{\nabla}\tilde{\Psi}_R = \tfrac12\left(-e_t + i\vec e_x\right)\phi\left(-e_t - i\vec e_x + \vec e_y + i\vec e_z\right) = 0 ,
$$

the left factor $(-e_t+i\vec e_x)$ annihilating the right one term by term. The field is therefore a solution of the first member of the massless pair; its $L$ part is zero, so the second member holds as well, and it is a solution of the massless biquaternion Dirac equation. It is the $R$ part of $\tilde{\nabla}^{\natural}\phi$ for this $\phi$. On it,

$$
\tilde J_{\Psi} = i\,\tilde{\Psi}_R\tilde{\Psi}_R^{*} = i\,e^{-2Q_t}\left(e_t + i\vec e_x\right),
\qquad
\mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde J_{\Psi}\right) = -2i\,e^{-2Q_t},
$$

the scalar part of $\tilde J_\Psi$ being $i\,e^{-2Q_t}$, of the required $ic\rho$ form. The divergence is non-zero everywhere and equals $-2i$ at the origin. The naive biquaternion product is therefore **not** the conserved electromagnetic current of the Dirac field. The sign of the bilinear does not help: $\tilde J_\Psi^{*} = -\tilde J_\Psi$, so passing to the conjugate flips the divergence to $+2i\,e^{-2Q_t}$.

**What the algebra does not supply.** The field, its conjugate and the two products of the algebra are the only ingredients the algebra offers for a bilinear of this kind, and the one product of this form that is gauge invariant and of the density sign fails the conservation test on an exact solution. The failure is therefore not an accident of the sign or of the normalization. Whether some other construction inside the algebra — a restriction to a subspace, a further factor of the field, a second field — gives a conserved object is not settled here; the question is open question 3. What can be said without a further construction is that the conserved current of the older literature is not a product of the field with its conjugate inside the algebra, and needs an ingredient outside it; that statement is made in the closing section, where the frame is written.

## An External Identity for the Source: The Mixed Invariant

The source term is the one element of the coupled system that the algebra has not supplied, and an outside treatment of a coupled biquaternionic Dirac field records an identity of exactly that kind. It is recorded here for its structure; it is an external result, not a development of the framework.

The source is A. I. Arbab, *Coupling of a biquaternionic Dirac field to a bosonic field*, arXiv:1708.06230v2. It works with a matter field and a background boson field, writing for them a Maxwell-like system in ordinary units, with matter electric and magnetic fields $\vec E_\tilde\nabla^{\mathrm{gco}}$ and $\vec B_\tilde\nabla^{\mathrm{gco}}$, matter charge and current densities $\rho_\tilde\nabla^{\mathrm{gco}}$ and $\vec J_\tilde\nabla^{\mathrm{gco}}$, and boson potentials $\varphi_g$ and $\vec A_g$. Taking the divergence of its Faraday-like equation and eliminating the matter fields with the other equations of its system, it obtains

$$
\vec B_g\cdot\vec B_\tilde\nabla^{\mathrm{gco}} - \frac{1}{c^2}\,\vec E_g\cdot\vec E_\tilde\nabla^{\mathrm{gco}}
= \mu_0\left(\vec A_g\cdot\vec J_\tilde\nabla^{\mathrm{gco}} - \varphi_g\,\rho_\tilde\nabla^{\mathrm{gco}}\right),
$$

where $\vec E_g = -\nabla\varphi_g - \partial/\partial t'\,\vec A_g$ and $\vec B_g = \nabla\times\vec A_g$ are the boson's own electric and magnetic fields. The source cites its eqs. (5) and (8) for the elimination, and the residual form given below shows what the identity rests on, namely the whole four-equation system, the Ampère-like equation included. The identity is recorded as the source states it and is not re-derived here.

**What the identity says.** The left-hand side is a mixed invariant: the cross-contraction $\tfrac12\sum_{\mu,\nu}F_{g,\mu\nu}F_\tilde\nabla^{\mathrm{gco}}^{\mu\nu}$ of the two field strengths. Written on the fields it is $\vec B_g\cdot\vec B_\tilde\nabla^{\mathrm{gco}} - \vec E_g\cdot\vec E_\tilde\nabla^{\mathrm{gco}}/c^2$, which is $-I_1^{\mathrm{cross}}/c^2$ with $I_1^{\mathrm{cross}} = \vec E_g\cdot\vec E_\tilde\nabla^{\mathrm{gco}} - c^2\vec B_g\cdot\vec B_\tilde\nabla^{\mathrm{gco}}$ — the two-field analogue of the corpus's $I_1 = \vec E^2 - c^2\vec B^2$, which contracts one field strength with itself.

The right-hand side is the pairing of the boson potential with the matter source. The identity therefore says that once two fields are coupled, their mixed invariant is not free: it is fixed by the source, and fixed by a source built linearly from the potential and the four-current. It is a constraint on the source, not an independent field equation, and it is the shape of answer that Open Question 4 asks for.

The source notes the two-field coincidence, where the identity reads $\epsilon_0\vec E^2 - \vec B^2/\mu_0 = \varphi\rho - \vec A\cdot\vec J$, that is, $\frac{1}{2\mu_0}\sum_{\mu,\nu}F_{\mu\nu}F^{\mu\nu} = -\sum_\nu A_\nu J^\nu$ in the $({+}{-}{-}{-})$ signature, the minus being the signature's; the mixed form above is the general one.

**Domain.** The matter fields of the source are built from its own biquaternion Dirac field, in its own conventions, and are read off a Maxwell-like system that costs one of the field's four coefficient components: the source fixes that component by a linear relation to the other three, and its Appendix B gives the modified system that replaces the relation, with an extra real field appearing in all four equations. The identity is therefore stated on the constrained system, and it concerns the source's field strengths, not the corpus's $\tilde{\Psi}$ or its $\sqrt{\mu}\,\tilde{J}$.

Written as a residual, with the source's own residual combinations $r_5,\dots,r_8$ of its fields — the vectors $\vec r_6,\vec r_7$ and the scalars $r_5,r_8$ —

$$
\vec B_g\cdot\vec B_\tilde\nabla^{\mathrm{gco}} - \frac{1}{c^2}\vec E_g\cdot\vec E_\tilde\nabla^{\mathrm{gco}} - \mu_0\left(\vec A_g\cdot\vec J_\tilde\nabla^{\mathrm{gco}} - \varphi_g\rho_\tilde\nabla^{\mathrm{gco}}\right)
= \frac{\hbar}{ϙ\,c}\,\nabla\cdot\vec r_6 + \vec A_g\cdot\vec r_7 - \frac{\varphi_g}{c^2}\,r_5 - \frac{\hbar}{ϙ\,c}\,\frac{\partial r_8}{\partial t'} ,
$$

the identity holds exactly on the solution set of the four equations and not for arbitrary fields: the right-hand side collects the four residuals, each with the weight its own equation carries, and vanishes when all four are imposed.

**Not adopted.** The same source carries three further claims, and none of them is used here. It reports an inertial mass and a "magnetic mass" as separately conserved; its own continuity equation has a vanishing right-hand side, and the split into two separately vanishing continuity equations is declared — "the continuity equation dictates that it split" — rather than derived, and the source states that no further definition of the magnetic mass is given. It reads the photon as carrying a magnetic charge, quotes the product of a magnetic and an electric charge as Dirac's quantisation rule, and reads that product as an uncertainty relation between two behaviours of one photon; the quantisation condition fixes the product $eg = 2\pi n\hbar c$ of a magnetic and an electric charge, and says nothing about the state of a single photon. And it presents Wilczek's axion electrodynamics as a special case reached by matching the axion derivatives to the potentials, which is a matching and not a derivation. The corpus records the identity above and cites the source for that identity alone.

## What the Algebra Supplies and What It Only Transcribes

What the algebra forces and what it merely rewrites in its own notation are easily conflated, and the separation is worth making explicit before the open questions.

**What the algebra supplies.**

- *A canonical abelian coupling.* The gauge group is the $*$-unitary part of the centre, and the centre is the only place a central phase can live. The $\mathrm{U}(1)$ that minimal coupling gauges is attached to the algebra without a choice of representation, as the gauge principle article establishes.
- *The covariant derivative as the localization of the phase.* The interaction term $\frac{iϙ}{\hbar}\tilde{A}\tilde{\Psi}$ is not added by hand: it is the term the localized phase forces, and the connection it forces is exactly the potential biquaternion of the Maxwell article.
- *Exact covariance of the coupled equation*, in the massive case as well as the massless one, with the component operators $\tilde\nabla^{\mathrm{gco}}_\mu$ and the phase law $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$ inherited unchanged.
- *The second-order equation with its curvature term.* The operator identity $\tilde\nabla^{\mathrm{gco},\natural}\tilde\nabla^{\mathrm{gco}} = \sum_\mu \tilde\nabla^{\mathrm{gco}}_\mu^2 + \frac{iϙ}{\hbar}\tilde{F}$ turns the coupled pair into a covariant wave equation carrying $\frac{iϙ}{\hbar}\tilde{F}$ as a term, the curvature entering as an element and not as an extra structure.
- *A material-sector connection.* For a real gauge function the connection stays in $\mathbb{M}_-$, so the coupling respects the sector decomposition the framework is built on.

**What it only transcribes.**

- *The minimal-coupling principle itself.* The derivation is the standard global-to-local argument carried into the biquaternion algebra. The algebra supplies a home for it and makes the component structure transparent; it does not supply a reason for the gauge field to exist.
- *The value of the coupling.* The charge $ϙ$ is a parameter; the algebra does not fix it.
- *The standard results of the Dirac theory.* The conserved current, the non-relativistic limit and the gyromagnetic factor are properties of the equation the framework contains, obtained with a linear mass term; the framework transcribes them, and the companion articles on the electron and on the solutions compute them.

**The commutativity that makes this unambiguous — and the sector where it fails.** The whole prescription rests on a property used above without being named: for an internal gauge group the substitution of the covariant derivative gives the same equation whether it is applied to the action or to the equation of motion, so it does not matter which of the two is gauged. The reason is that the phase is a **central scalar**: it commutes with the gradient and with every element, so the localization and the variation cannot disagree. The property is not universal. When the transformation is not central — when it acts by an element of the algebra multiplying the field, as the Lorentz transformation of the vierbein formulation does — the two orders differ, because the gradient does not pass through a non-central factor, and the difference is the commutator of that factor with the gradient. J. Fredsted (arXiv:1906.12200v3, 2019) proves the mismatch for the gravitationally coupled fermion and constructs a world-index formalism in which it is removed, recorded in *Curved Spacetime and the Biquaternion Framework*. The consequence for this article is a boundary rather than a defect: the minimal-coupling prescription derived here is unambiguous **because** its gauge group is internal and its phase central, and it must not be transferred to the gravitational sector unchanged, where the same prescription is a different and inequivalent construction.

**What is interpretation.** Reading the coupled equation as a Dirac field propagating in a background connection is a geometric interpretation. The algebraic content is the transformation law, the covariance of the coupled equation in both the massless and the massive case, and the explicit component form; the connection picture is a consistent interpretation of that content, as in the gauge principle article.

## Open Questions

1. **The relative phase of the two parts.** The mass keeps the common central phase and breaks the relative one. Can the relative phase be gauged, and does the framework's central-element structure supply anything analogous to the would-be Goldstone statement for the breaking? A mass term built on the antilinear real structure $\flat$ would be incompatible with a gauged common phase as well, and the companion on the neutrino takes that case up.

2. **The matter representation.** The gauge principle produces a left-action covariant derivative; a right-action mirror is equally covariant, and the mixed insertion is not. Which side is the physical Dirac field multiplied from? The second member of the pair is the $\natural$-image of the first, so the algebra relates the two sides without choosing between them, and the choice is made where the field is placed, not by the equation. What fixes it inside the algebra?

3. **The interaction current.** The gauge-invariant bilinear $i\tilde{\Psi}\tilde{\Psi}^{*}$ is in $\mathbb{M}_-$ but is not conserved: the exact solution $\tilde\Psi_R = \tfrac12\phi\left(-e_t - i\vec e_x + \vec e_y + i\vec e_z\right)$, with $\phi = \exp(iQ_x-Q_t)$, gives $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde J_\Psi) = -2i\,e^{-2Q_t}$. Is there a construction on the algebra, on a restricted subspace or with a further factor of the field, that is conserved? Or is the current irreducibly an object of a larger structure, as the older literature's construction suggests? Not settled here.

4. **The sourced system.** How does the Dirac current feed the biquaternionic Maxwell equation $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$, and does the coupled system close on the algebra? The integrability condition $\sqrt{\mu}\,\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{J}) = 0$ must be recovered from the current. The external identity of the section on the mixed invariant supplies the shape of an answer — the source contraction is fixed by the two field strengths — but it is stated for the source's own field strengths, not for $\tilde{\Psi}$, so it does not by itself close the corpus's system.

5. **The shared generator.** The internal phase $\exp(iϙ\Gamma/\hbar)$ and the complex time coordinate $ict'$ both use the single element $i$ of $\mathbb{B}$. Is this identification content-bearing, or vacuous because the phase is central? (The gauge principle article's open question.)

6. **The non-abelian extension.** When the connection becomes $\mathbb{B}$-valued it is no longer central, so it no longer commutes with the field, and the left/right question becomes sharp: the order of the factors is then part of the statement. The companions on the covariant derivative, on non-abelian fields and on the Yang–Mills equation place the field, but the choice is made there rather than forced.

7. **Empirical content.** As everywhere in the framework, the unresolved question is whether any of this yields a prediction distinguishing it from standard gauge theory. The minimal coupling as presented is a reformulation; the framework-level question of empirical contact remains open.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate and on the metric, $g[\mathbb{B}]$ or $g[\mathbb{M}_-]$.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra, and they are used only in this section, as the frame in which the cells can be compared with the standard matrices.

Write $L_a\psi=a\psi$ and $R_b\psi=\psi b$ for the left and right multiplications, and $c(M)$ for the matrix of a cell in the basis of the sixteen products. The four gammas and $\gamma_5$ are single cells:

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

A single cell is a tensor $a\otimes b$ read through $L_aR_b$, so its coefficient matrix has rank one; the cells form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and every element of $M_4(\mathbb{C})$ is a sum of at most four of them.

$\gamma_5$ is the chirality cell of the frame, $\mathsf{V}^{\mathrm{vol}}$, the cell $-iR_{\vec e_z}$ of the axis-free display. Its eigenvalues are $\pm1$, with multiplicity two each; read in the frame, that is the statement that the two values of the subscript are two.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The conserved current of the older literature.** The object that the previous sections cannot build is written here, once, in this display. The conserved current is the bilinear built with the generator cell of the coordinate $x_\mu$ — the cell $iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$, with $\nu(t)=x$ and $\nu(k)=y$ — and with the adjoint row $\psi^{\dagger}iR_{\vec e_x}$:

$$
j_\mu = \psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\,\psi ,
$$

whose time component is $\psi^{\dagger}\psi$ and whose spatial components are $\psi^{\dagger}\alpha_k\psi$ with $\alpha_k = L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$. The ingredient that the algebra's own bilinears cannot supply is the adjoint row, which is built on the one-sided cell $iR_{\vec e_x}$ and lies outside the algebra. That is why $i\tilde\Psi\tilde\Psi^{*}$ cannot be the conserved current, and why the current is recorded in this section and nowhere else.

**The other form of the Dirac equation.** The third object of the older literature is the four-column form, on which the central phase multiplies the field one way on one part and the other way on the other, so that the vector phase and the relative phase exchange their roles. It is the carrier the closing sentence of *The Dirac Equation in Biquaternionic Form* names, and no construction of this article uses it: the algebra's own field carries the common phase, as the section on the field shows.

**The identities the corpus cites.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the cells,
$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$, so that $\sum_\mu\gamma^\mu\gamma_\mu=-4I_4$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\mu=2\gamma_\alpha$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\beta\gamma_\mu=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu\gamma_\gamma\gamma_\beta\gamma_\alpha\gamma_\mu=-2\gamma_\gamma\gamma_\beta\gamma_\alpha$.

## Summary

The minimal coupling of the biquaternion Dirac field to electromagnetism is the replacement of the gradient by the covariant derivative of the gauge principle,

$$
\tilde\nabla^{\mathrm{gco}} = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A}, \qquad \tilde\nabla^{\mathrm{gco}}_\mu = \frac{\partial}{\partial Q_\mu} + \frac{iϙ}{\hbar}A_\mu,
$$

acting by left multiplication on the field. The coupled equation is

$$
\tilde\nabla^{\mathrm{gco}}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad \tilde\nabla^{\mathrm{gco},\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R,
$$

that is,

$$
\tilde{\nabla}\tilde{\Psi}_R + \frac{iϙ}{\hbar}\tilde{A}\tilde{\Psi}_R = m\tilde{\Psi}_L, \qquad
\tilde{\nabla}^{\natural}\tilde{\Psi}_L + \frac{iϙ}{\hbar}\tilde{A}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R,
$$

with the interaction term $\frac{iϙ}{\hbar}\tilde{A}\tilde{\Psi}$ that the localized central phase forces. In the massless case the two members decouple, $\tilde\nabla^{\mathrm{gco}}\tilde{\Psi}_R = 0$ and $\tilde\nabla^{\mathrm{gco},\natural}\tilde{\Psi}_L = 0$.

The **massless** and the **massive** coupled equations are both exactly gauge covariant: with $\tilde{\Psi}_2 = \exp(iϙ\Gamma/\hbar)\tilde{\Psi}$ and $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$,

$$
\tilde\nabla^{\mathrm{gco}}_{2}\tilde{\Psi}_{R,2} = \lambda\,\tilde\nabla^{\mathrm{gco}}\tilde{\Psi}_R, \qquad \tilde\nabla^{\mathrm{gco},\natural}_{2}\tilde{\Psi}_{L,2} = \lambda\,\tilde\nabla^{\mathrm{gco},\natural}\tilde{\Psi}_L,
$$

the same factor $\lambda$ for either member, and the parent's linear mass term acquires that same factor, so $\tilde\nabla^{\mathrm{gco}}\tilde{\Psi}_R = m\tilde{\Psi}_L$ holds in every gauge when it holds in one. The continuous $\mathrm{U}(1)$ of the massless theory survives the mass; what the mass breaks is the relative phase that multiplies the two parts oppositely. Squaring the pair gives the covariant wave equation

$$
\left(\sum_{\mu\in\{t,x,y,z\}} \tilde\nabla^{\mathrm{gco}}_\mu^{2} + \frac{iϙ}{\hbar}\tilde{F} - m^{2}\right)\tilde{\Psi}_R = 0 .
$$

The prescription attaches to the one-sided pair and not to the parent's two-sided form, because the two-sided form's mass term is a conjugation and a right multiplication and carries no continuous central phase to localize.

The interaction current is not a product of the field with its conjugate inside the algebra. The gauge-invariant, material-sector bilinear $i\tilde{\Psi}\tilde{\Psi}^{*}$ is not conserved on solutions of the massless equation: the exact solution $\tilde\Psi_R = \tfrac12\phi\left(-e_t - i\vec e_x + \vec e_y + i\vec e_z\right)$ with $\phi = \exp(iQ_x-Q_t)$ gives $\mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde J_\Psi) = -2i\,e^{-2Q_t}$, while the scalar part of $\tilde J_\Psi$ has the required density form $i\,c\rho$. The conserved current of the older literature is not of this kind: it carries an adjoint built on a one-sided cell outside the algebra, and its form is recorded in the closing section with the other gamma-display statements. The pure-biquaternion form of the current, and the closure of the sourced system, are left as open questions, together with the choice of the left or right matter representation and the gauging of the relative phase of the two parts.

One external result is recorded on the source side, and it is not a development of the framework: the identity of A. I. Arbab (arXiv:1708.06230v2), by which the mixed invariant of the two coupled field strengths is fixed by the pairing of the potential with the four-current. It is a constraint following from that source's own four equations, and the residual form in that section exhibits that dependence; it is not re-derived here, and its other claims are not adopted. It is recorded because it has the shape that Open Question 4 asks for, and because the corpus has no statement of that shape.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $\mathrm{Sc}(\tilde Q)$ | Scalar part: the coefficient of $e_t$, and half the trace in the frame of the closing section |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Centre of the algebra; source of the abelian gauge group |
| $\tilde{\nabla} = e_t\partial/\partial Q_t + \sum_{k=x,y,z}\vec e_k\,\partial/\partial Q_k$ | Biquaternionic gradient (Dirac operator) |
| $\tilde{\nabla}^{\natural} = e_t\partial/\partial Q_t - \sum_{k=x,y,z}\vec e_k\,\partial/\partial Q_k$ | Quaternion-conjugate gradient |
| $\vec u$ | The declared unit of the frame, in the parent's two-sided form |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla}$ | d'Alembertian |
| $\tilde{\Psi}$ | Biquaternion Dirac field, an element of $\mathbb{B}$ |
| $\tilde\Psi_L, \tilde\Psi_R$ | The two parts of the field; the subscript takes two values and no more |
| $\tilde{\Psi}^\flat = -\tilde{\Psi}^{*}$, $\tilde{\Psi}^{*} = \overline{\tilde{\Psi}^{\natural}}$ | Anti-Hermitian conjugate of the field (the algebra's real structure; **not** the mass) |
| $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$ | Free biquaternion Dirac equation (massive chiral pair) |
| $\tilde{A} = i\phi/c\,e_t + \vec A$ | Connection = potential biquaternion (in $\mathbb{M}_-$) |
| $\tilde{A}_2 = \tilde{A} - \tilde{\nabla}\Gamma$ | Gauge transformation of the connection |
| $\lambda = \exp(iϙ\Gamma/\hbar)$ | Local central phase; $\Gamma$ real scalar |
| $\varkappa$ | A second central constant, in the relative phase $\tilde\Psi_R\mapsto\varkappa\tilde\Psi_R$, $\tilde\Psi_L\mapsto\varkappa^{-1}\tilde\Psi_L$ |
| $ϙ$ | Charge (coupling constant), not fixed by the algebra |
| $\tilde\nabla^{\mathrm{gco}} = \tilde{\nabla} + \frac{iϙ}{\hbar}\tilde{A}$ | Covariant derivative (left action) |
| $\tilde\nabla^{\mathrm{gco},\natural} = \tilde{\nabla}^{\natural} + \frac{iϙ}{\hbar}\tilde{A}^{\natural}$ | Its $\natural$-image; the operator of the second member of the pair |
| $\tilde\nabla^{\mathrm{gco}}_\mu = \partial/\partial Q_\mu + \frac{iϙ}{\hbar}A_\mu$ | Components; $\partial/\partial Q_t = -(i/c)\,\partial/\partial t'$ |
| $\tilde{F}$ | Field-strength biquaternion; $\tilde\nabla^{\mathrm{gco},\natural}\tilde\nabla^{\mathrm{gco}} = \sum_\mu \tilde\nabla^{\mathrm{gco}}_\mu^2 + \frac{iϙ}{\hbar}\tilde{F}$ |
| $\tilde\nabla^{\mathrm{gco}}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde\nabla^{\mathrm{gco},\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$ | Minimally coupled Dirac equation |
| $\frac{iϙ}{\hbar}\tilde{A}\tilde{\Psi}$ | Interaction term |
| $\exp(2iϙ\Gamma/\hbar)$ | Phase that an antilinear mass term would acquire under a local phase; the linear mass term acquires $\lambda$ instead |
| $\|\tilde\Psi\|_E^2 = \mathrm{Sc}(\tilde\Psi\tilde\Psi^{*})$ | Euclidean modulus squared; real and $\ge 0$, the sum of the four squared coefficient moduli |
| $\tilde J_{\Psi} = i\tilde{\Psi}\tilde{\Psi}^{*}$ | Naive bilinear; gauge invariant, in $\mathbb{M}_-$, **not conserved** |
| $\tilde J = ic\rho\,e_t + \vec J$ | Four-current; the Maxwell source is $\sqrt{\mu}\,\tilde J$ |
| $\tilde{\nabla}\tilde{F} = -\sqrt{\mu}\,\tilde{J}$ | Biquaternionic Maxwell equation |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $r_5,\dots,r_8$ | The external source's own residual combinations of its fields (scalars $r_5,r_8$, vectors $\vec r_6,\vec r_7$) |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original equation and the minimal coupling.
- Hermann Weyl, "Elektron und Gravitation," *Zeitschrift für Physik* **56** (1929) 330–352, for the origin of the local phase and the gauge principle.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard treatment of minimal coupling, the conserved current, and the non-relativistic limit.
- M. E. Peskin and \tilde\nabla^{\mathrm{gco}}. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), and S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the standard abelian and non-abelian gauge couplings.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the Majorana and Dirac mass terms and the fermion-number symmetry.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of the biquaternion algebra with the even part of $\mathrm{Cl}_{1,3}$ and the relation of the timelike generator to the even subalgebra.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the gauge-theoretic interpretation of the covariant derivative in geometric algebra.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of the Dirac equation in spacetime algebra.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component calculus and the Dirac adjoint.
- J. Fredsted, "Obtaining consistent Lorentz gauging for a gravitationally coupled fermion," arXiv:1906.12200v3 [physics.gen-ph] (2019), for the external result recorded in *What the Algebra Supplies and What It Only Transcribes*: that for the Lorentz gauge group of the standard vierbein coupling, localization and the Euler–Lagrange variation do not commute, which is what makes the internal-gauge commutativity this article relies on a restriction and not a truism. Cited as an external claim; the gravitational construction is recorded in *Curved Spacetime and the Biquaternion Framework*.
- A. I. Arbab, "Coupling of a biquaternionic Dirac field to a bosonic field," arXiv:1708.06230v2 (2017), for the external identity recorded in *An External Identity for the Source: The Mixed Invariant*: with a background boson field $g$ and a matter field $\tilde\nabla^{\mathrm{gco}}$, the mixed invariant of the two field strengths obeys $\vec B_g\cdot\vec B_\tilde\nabla^{\mathrm{gco}} - c^{-2}\vec E_g\cdot\vec E_\tilde\nabla^{\mathrm{gco}} = \mu_0(\vec A_g\cdot\vec J_\tilde\nabla^{\mathrm{gco}} - \varphi_g\rho_\tilde\nabla^{\mathrm{gco}})$, a consequence of the source's own four Maxwell-like equations, recorded with the residual form that exhibits that dependence. Cited for that identity alone; the source's magnetic-mass, single-photon-charge and axion-reduction claims are not adopted.
- Companion articles: [The Gauge Principle in Biquaternionic Form](the-gauge-principle-in-biquaternionic-form.html); [The Covariant Derivative and Gauge Connection in Biquaternionic Form](the-covariant-derivative-and-gauge-connection-in-biquaternionic-form.html); [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html); [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html); [The Electron in Biquaternionic Form](the-electron-in-biquaternionic-form.html); [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html); [Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form](antilinear-structure-and-the-two-kinds-of-mass-in-biquaternionic-form.html); [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html); [Canonical Quantization of the Biquaternion Maxwell Field](canonical-quantization-of-the-biquaternion-maxwell-field.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html).
