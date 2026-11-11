# __The Schrödinger Equation in Biquaternionic Form__

## Introduction

The Schrödinger equation in biquaternionic form is

$$
i\hbar\,c\,\partial/\partial r'_t\,\tilde\Xi_{\mathrm{sp}} = \tilde R_\Psi\,\tilde\Xi_{\mathrm{sp}},
\qquad
\tilde R_\Psi = r_t\,e_t + i\vec r_\Psi \in \mathbb{B}_{\Psi},
\qquad
\tilde\Xi_{\mathrm{sp}} \in \mathbb{B}.
$$

Dividing by $i\hbar\,c$ gives the same equation in a second writing,

$$
\partial/\partial r'_t\,\tilde\Xi_{\mathrm{sp}} = -\frac{i}{\hbar\,c}\tilde R_\Psi\,\tilde\Xi_{\mathrm{sp}},
\qquad
-\frac{i}{\hbar\,c}\tilde R_\Psi = \frac{\vec r_\Psi - i\,r_t\,e_t}{\hbar\,c} \in \mathbb{B}_{\Phi}.
$$

Dividing by $i\hbar\,c$ is always possible, because $i\hbar\,c$ is a central unit. The centrality of $i$ is what gives the result its content: it makes $i\tilde R_\Psi$ anti-Hermitian, and with it $-i\tilde R_\Psi/\hbar\,c$, so the generator of the second writing lies in the material sector $\mathbb{B}_{\Phi}$.

The two writings are one equation, and they say different things about it. The first names the observable: it states the dynamics as left multiplication by the Hermitian $\tilde R_\Psi$, and it is the writing in which $\tilde R_\Psi$ is read as an energy. The second names the generator: it states the dynamics as left multiplication by an anti-Hermitian element, and it places that element in the same four-dimensional real space that carries the four-vectors. The central $i$ is the canonical isomorphism between the two, and no other element of the algebra supplies one, up to sign.

Three things in and around $\mathbb{B}$ play the role of $i$: the central scalar imaginary, the non-central roots of minus one, and the complex structure that a carrier must carry. The first two are elements of the algebra, and they are different elements. The third is not an element at all. Confusing them produces equations that look like the Schrödinger equation and do not preserve the trace. The first section separates them and decides which is the $i$ of the two writings above.

The companion article *Quantum Physics in Biquaternionic Form* takes the density matrix for its object. It exhibits the $*$-unitary biquaternion $\tilde Q(r'_t)$ obeying $i\hbar\,c\,d\tilde{Q}/dr'_{t}= \tilde R_\Psi\tilde Q$, and the state equation $i\hbar\,c\,d\tilde{Ϛ}_{\Psi}/dr'_{t}= [\tilde R_\Psi,\tilde{Ϛ}_{\Psi}]$ for $\tilde{Ϛ}_{\Psi} \in \mathbb{B}_{\Psi}$. This article takes the field for its object and writes $i\hbar\,c\,\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}$ for $\tilde{Ξ}_{\mathrm{sp}} \in \mathbb{B}$. The difference is the object and not the equation: both writings apply to both objects, and the field equation is shown to imply the density-matrix equation. The subscript `sp` carried by the field is the corpus's caret for the spinor role, beside `scl` for the scalar role and `fop` for the field operator, as the caret table of *Algebra and Element Conventions* fixes it; it names a role and not a sector.

The article is organised as the two writings demand. The three objects that square to minus one are separated. The central $i$ is shown to be the intertwiner that produces the second writing. The carrier is shown to be $\mathbb{B}$ and not one of its sectors, because both writings must hold in it. The equation is solved in the $\mathbb{B}_{\Psi}$ writing and read in the $\mathbb{B}_{\Phi}$ writing. The unit is shown to be $\pm i$ and nothing else. The closing sections separate what the form adds from what it merely relabels.

## Three Objects That Square to Minus One

The equation carries one symbol that squares to minus one, and that symbol is $i$. Three objects in and around $\mathbb{B}$ answer to the same description, and they are not interchangeable. The first two are elements of the algebra and the third is a structure on a carrier. The table at the end of the section collects them, and its column *role* is what decides the two writings.

### The scalar imaginary

The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with quaternion basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_\mu^2 = -e_t$ and $\vec e_\mu \vec e_\nu = \varepsilon_{\mu\nu\lambda}\vec e_\lambda$ for $\mu,\nu \in \{x,y,z\}$, $\mu \neq \nu$. The **scalar imaginary** $i$ is the image of the imaginary unit of the complexifying factor $\mathbb{C}$. It satisfies $i^2 = -e_t$ and is **central**: it commutes with every element of $\mathbb{B}$.

The central elements are exactly the complex scalars,

$$
\mathbb{B}_{C} = \{Q_t\,e_t : Q_t \in \mathbb{C}\} = \operatorname{span}_{\mathbb{R}}\{e_t, i\,e_t\},
$$

a copy of the complex line embedded as the scalar part, and it is the centre of $\mathbb{B}$. Within it the roots of $-1$ are exactly $\pm i$: the scalar imaginary is not "one root of $-1$ among many" but *the* central one.

### The quaternion units and the non-central roots

Each quaternion unit satisfies $\vec e_\mu^2 = -e_t$, but the $\vec e_\mu$ do not commute: $\vec e_x \vec e_y = \vec e_z = -\vec e_y \vec e_x$. They are non-central roots of $-1$. The companion article on biquaternion roots of minus one classifies all roots $\tilde{Ζ}$ with $\tilde{Ζ}^2 = -e_t$: either $\tilde{Ζ} = \pm i$ (the central roots), or $\tilde{Ζ} = \vec Q$ is a complex vector with $(\vec Q,\vec Q) := Q_x^2 + Q_y^2 + Q_z^2 = 1$ (the non-central roots). The real members of the second family are the **unit pure real quaternions** $\vec u \in \mathbb{B}_{H}$ (the real quaternion subalgebra $\operatorname{span}_{\mathbb{R}}\{e_t,\vec e_x,\vec e_y,\vec e_z\}$), with $|\vec u| = 1$, so $\vec u^2 = -e_t$ and $\vec u^{*} = -\vec u \in \mathbb{B}_{\Phi}$. They are the roots of $-1$ that the algebra itself carries, and each is the axis a rotor turns about. Both $\vec u$ and $i$ square to $-e_t$ and are anti-Hermitian, but $i$ is central and $\vec u$ is not.

The two appear side by side in the polar word of the field,

$$
\tilde\Xi=r\,e^{i\alpha}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
$$

and this expression is precisely where the conflation happens. The $i$ in $e^{i\alpha}$ is the central scalar imaginary, and the angle $\alpha$ is a number; the rotor $\tilde u_{\mathrm r}$ is built from a non-central root $\vec u$, and $\vec u$ is an axis the field carries. One is the complex structure, the other a direction the field has turned, and they must be read separately.

### The complex structure of the carrier

A Schrödinger equation presupposes a complex vector space of states. In the biquaternion framework that space is $\mathbb{B}$ itself, read as a complex vector space of dimension four, and its complex structure is left multiplication by the central $i$. Because $i$ is central, this action commutes with the left action of $\mathbb{B}$, so the module is genuinely complex-linear.

It is important that the complex structure does **not** live on $\mathbb{B}_{\Psi}$. Multiplication by $i$ is a real-linear isomorphism

$$
i\,\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi},
\qquad
i\,\mathbb{B}_{\Phi} = \mathbb{B}_{\Psi},
$$

so $i$ carries $\mathbb{B}_{\Psi}$ out of itself; it is not an operator on $\mathbb{B}_{\Psi}$. The phrase "the complex structure of $\mathbb{B}_{\Psi}$", if used at all, can only mean the complex structure of the carrier: as a real vector space $\mathbb{B}_{\Psi}$ can be given some complex structure abstractly, but none is canonical, and multiplication by $i$ is not one. A reader is most likely to slip here, because the polar word $r\,e^{i\alpha}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ contains both an $i$, inside the central factor, and a non-central root inside the rotor; the $i$ does not act on $\mathbb{B}_{\Psi}$, it maps it to its complement.

| Object | Where it lives | Central? | Role |
|---|---|---|---|
| Scalar imaginary $i$ | $\mathbb{B}_{C}$, the centre | Yes | Complex structure of the carrier $\mathbb{B}$; the $i$ of the Schrödinger equation |
| Quaternion units $\vec e_\mu$ | $\mathbb{B}_{H} \cap \mathbb{B}_{\Phi}$ (pure real) | No | Rotation generators, rotor axes |
| Non-central roots $\vec u$ | $\mathbb{B}_{H} \cap \mathbb{B}_{\Phi}$, unit sphere | No | Rotation axes of the rotor |
| Complex structure of the carrier | Acts on $\mathbb{B}$, of complex dimension four | — | Left multiplication by the central $i$; not a structure on $\mathbb{B}_{\Psi}$ |

The row whose *role* is the complex structure of the carrier names the $i$ of the equation. The two rows whose *role* is a rotation axis name what it is not.

## The Intertwiner Between the Two Writings

The relation $i\,\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi}$ is the algebraic content of the Hermitian decomposition, and it is what produces the second writing. Concretely, for a Hermitian element $\tilde R_\Psi = r_t\,e_t + i\vec r_\Psi \in \mathbb{B}_{\Psi}$, using $\tilde R_\Psi^{*} = \tilde R_\Psi$, $i^{*} = -i$, and the centrality of $i$,

$$
(i\tilde R_\Psi)^{*} = \tilde R_\Psi^{*} i^{*} = \tilde R_\Psi\,(-i) = -i\tilde R_\Psi.
$$

So $i\tilde R_\Psi \in \mathbb{B}_{\Phi}$: the map $\tilde R_\Psi \mapsto i\tilde R_\Psi$ is a real-linear isomorphism $\mathbb{B}_{\Psi} \to \mathbb{B}_{\Phi}$ with inverse $\tilde{Q} \mapsto -i\tilde{Q}$, turning a Hermitian observable into an anti-Hermitian object. For example, with $\tilde R_\Psi = i\,\vec e_x$ (Hermitian, since $(i\vec e_x)^{*} = i\vec e_x$), one has $i\tilde R_\Psi = i\,(i\vec e_x) = -\vec e_x$, and $-\vec e_x$ is anti-Hermitian because $(-\vec e_x)^{*} = -(-\vec e_x)$.

**This computation is the second writing.** The generator of the second writing is $-\frac{i}{\hbar\,c}\tilde R_\Psi$, so the computation says of it what it says of $i\tilde R_\Psi$: it is anti-Hermitian. An anti-Hermitian generator exponentiates to a $*$-unitary flow, because conjugation reverses the sign of the exponent, so the exponential of an anti-Hermitian element and its conjugate are mutual inverses. The two writings therefore carry one equation. The first multiplies by the Hermitian observable. The second multiplies by its anti-Hermitian image under $i$. The two differ by the central $i$, and by nothing else.

## The Field Is One Element of the Algebra

### The carrier

The field is one element $\tilde{Ξ}_{\mathrm{sp}}$ of $\mathbb{B}$, with four complex coefficients, that is eight real numbers. The equation is left multiplication by $\tilde R_\Psi$, and $\mathbb{B}$ is an algebra, so a product of two elements is an element: if the right-hand side is in the carrier, so is the left-hand side, and the equation restricts nothing.

**Nothing stands behind the field.** No column, no ideal, no projector, no idempotent and no declared axis is needed to write the equation or to solve it. This is the ruling of *Why AXF Matrices instead of Pauli and Gamma Matrices*: a field is an element, the operator is left multiplication, and the display, when one is wanted, is the axis-free array of the multiplication table.

**The equation is complex-linear, and its symbol is Hermitian.** Since $i$ is central,

$$
L_{\tilde R_\Psi}(i\tilde X)=i\,L_{\tilde R_\Psi}\tilde X,
$$

so the equation is complex-linear on $\mathbb{B}$ read as a complex vector space of dimension four. And since $\tilde R_\Psi^{*}=\tilde R_\Psi$, the sesquilinear form $\langle\tilde X,\tilde Y\rangle_{*}=\mathrm{Sc}(\tilde X\tilde Y^{*})$ satisfies

$$
\mathrm{Sc}\bigl((\tilde R_\Psi\tilde X)\tilde Y^{*}\bigr)=\mathrm{Sc}\bigl(\tilde X(\tilde R_\Psi\tilde Y)^{*}\bigr),
$$

so the symbol $L_{\tilde R_\Psi}$ is Hermitian for that form, and the flow it generates preserves $\mathrm{Sc}(\tilde X\tilde X^{*})$. Both identities were checked on a hundred random pairs.

**The display, where a display is wanted, is the axis-free array.** In the coefficient basis the symbol is the array $L_{\mathrm{axf}}(\tilde R_\Psi)$, a $4\times4$ complex matrix with $\mathrm{Tr}L_{\mathrm{axf}}(\tilde R_\Psi)=4r_t$ and $\det L_{\mathrm{axf}}(\tilde R_\Psi)=\langle\tilde R_\Psi\rangle_{\natural}^{2}$, where $\langle\tilde R_\Psi\rangle_\natural=r_t^{2}-|\vec r_\Psi|^{2}$: the determinant of left multiplication is the square of the reduced norm, the identity and its numerical verification being those of *Why AXF Matrices instead of Pauli and Gamma Matrices*. The array is Hermitian on the nose, and it names no spatial direction. The equation is therefore the ordinary complex-linear Schrödinger equation on four complex coefficients with that Hermitian symbol, and nothing beyond the algebra enters the display.

### The four coefficients, and the central field

The field carries one complex coefficient of $e_t$ and three of $\vec e_\mu$, that is $2+6$ real numbers. A field with only the scalar coefficient nonzero,

$$
\tilde\Xi_{\mathrm{sp}}(r'_t)=\Xi_t(r'_t)\,e_t,
$$

is called **central**, and for it $\tilde R_\Psi\tilde\Xi_{\mathrm{sp}}=r_t\Xi_t\,e_t$ exactly when $\vec r_\Psi=0$: the equation then reduces to the ordinary one-component equation for $\Xi_t$. The remaining six real parameters are the field's rotor and boost, and *The Polar Form of the Schrödinger Equation in Biquaternionic Form* reads them.

**Why not $\mathbb{B}_{\Psi}$.** The temptation is to let the state $\tilde{Ϛ}_{\Psi}\in\mathbb{B}_{\Psi}$ of the companion article serve as the field. The equation rules it out, and the reason is closure. The field is multiplied on the left by every Hermitian element, because the Hamiltonian is arbitrary, so the carrier must be closed under left multiplication by $\mathbb{B}_{\Psi}$. The sector is not closed under its own products: $(i\vec e_x)(i\vec e_y)=-\vec e_z\in\mathbb{B}_{\Phi}$, so a field confined to $\mathbb{B}_{\Psi}$ is multiplied out of it by its own equation. Every element of $\mathbb{B}$ is a sum of a Hermitian and an anti-Hermitian part,

$$
\tilde Q=\tfrac12(\tilde Q+\tilde Q^{*})+\tfrac12(\tilde Q-\tilde Q^{*}),
$$

and the second part is $-i$ times a Hermitian element. Closure under $\mathbb{B}_{\Psi}$ is therefore closure under all of $\mathbb{B}$, and the smallest such carrier containing $e_t$ is $\mathbb{B}$ itself. The second writing shows the same from the other side: its multiplier $-i\tilde R_\Psi/\hbar\,c$ ranges over $\mathbb{B}_{\Phi}$ as $\tilde R_\Psi$ ranges over $\mathbb{B}_{\Psi}$, so the multipliers named by the two writings together span $\mathbb{B}$. A Hermitian-valued solution exists — with $\tilde R_\Psi=i\vec e_x$ and $\tilde\Xi_{\mathrm{sp}}(r'_t)=i(\cos\theta\,\vec e_y+\sin\theta\,\vec e_z)$, $\theta=r'_t/(\hbar\,c)$, both sides equal $\sin\theta\,\vec e_y-\cos\theta\,\vec e_z$ — but its being a solution is a coincidence of that sector and not a structure of the equation. The carrier of the flow is $\mathbb{B}$.

### Vanishing, the cone, and the density

The ordinary wave function may vanish, and the vanishing is a point at which the polar parametrisation of the companion article is undefined. Here the analogous locus is larger and it is algebraic: the field is a zero divisor exactly when its quaternionic norm vanishes,

$$
\langle\tilde\Xi_{\mathrm{sp}}\rangle_{\natural}=\tilde\Xi_{\mathrm{sp}}\tilde\Xi_{\mathrm{sp}}^{\natural}=0,
$$

which is the zero-divisor cone of the algebra. A generic element is off it — a random element has $\langle\tilde\Xi_{\mathrm{sp}}\rangle_{\natural}\neq0$ with probability one — and the flow keeps it there, because $\langle\tilde Q\tilde\Xi\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}\langle\tilde\Xi\rangle_{\natural}$ and $\langle\tilde Q\rangle_{\natural}$ is a central unit. So the field of this equation is a unit of the algebra at almost every point of space and time, and it stays one.

**The density is the Hermitian norm.** Put

$$
\rho=\mathrm{Tr}\bigl(\tilde\Xi_{\mathrm{sp}}^{*}\tilde\Xi_{\mathrm{sp}}\bigr)=2\,\mathrm{Sc}\bigl(\tilde\Xi_{\mathrm{sp}}\tilde\Xi_{\mathrm{sp}}^{*}\bigr)\ge0,
\qquad
\tilde{Ϛ}_{\Psi}=\frac{\tilde\Xi_{\mathrm{sp}}\tilde\Xi_{\mathrm{sp}}^{*}}{\rho}\in\mathbb{B}_{\Psi},
$$

which is Hermitian, positive and of unit trace, so $\tilde{Ϛ}_{\Psi}$ is a state in the sense of the companion article. The field and that state are not the same object; they are related by $\tilde\Xi_{\mathrm{sp}}\mapsto\tilde\Xi_{\mathrm{sp}}\tilde\Xi_{\mathrm{sp}}^{*}$, and the same central $i$ acts as the complex structure on the field while exchanging the sectors in which the operator is expressed. The expectation of the Hamiltonian in a field is $\mathrm{Sc}(\tilde R_\Psi\tilde{Ϛ}_{\Psi})$, which is real by the Hermiticity above.

## The Equation Written in $\mathbb{B}_{\Psi}$, and Its Solution

With the objects separated, the first writing reads

$$
\boxed{\;i\hbar\,c\,\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}}(r'_t) = \tilde R_\Psi\,\tilde{Ξ}_{\mathrm{sp}}(r'_t),
\qquad
\tilde R_\Psi = r_t\,e_t + i\vec r_\Psi \in \mathbb{B}_{\Psi},
\qquad
\tilde{Ξ}_{\mathrm{sp}}(r'_t) \in \mathbb{B}\;},
$$

where $i$ is the scalar imaginary and $\hbar$ is the reduced Planck constant. Because $i$ is central, $i\tilde R_\Psi=\tilde R_\Psi i$, and there is no left/right ordering ambiguity in the equation. Because $\mathbb{B}$ is an algebra, $\tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}\in\mathbb{B}$: the equation is consistent in the carrier, and no ideal is needed for the consistency.

**Solution.** Since $-i\tilde R_\Psi = -i r_t\,e_t + \vec r_\Psi$ and the scalar and vector parts commute,

$$
\boxed{\;\tilde Q(r'_t) = \exp\!\left(-i\frac{\tilde R_\Psi\,r'_{t}}{\hbar\,c}\right)
= \exp(-i\frac{r_t\,r'_t}{\hbar\,c})\left(\cos\theta\,e_t + \sin\theta\,\vec u_\Psi\right),
\qquad
\theta =\frac{|\vec r_\Psi|r'_t}{\hbar\,c}\;},
$$

with $\vec u_\Psi=\vec r_\Psi/|\vec r_\Psi|$, and $\tilde{Ξ}_{\mathrm{sp}}(r'_t) = \tilde Q(r'_t)\tilde{Ξ}_{\mathrm{sp}}(0)$. The element $\tilde Q$ is $*$-unitary, $\tilde Q\tilde Q^{*} = e_t$: the central phase cancels, and the real factor $\cos\theta\,e_t + \sin\theta\,\vec u_\Psi$ is a unit real quaternion. Consequently the Hermitian norm $\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^{*}\tilde{Ξ}_{\mathrm{sp}})$ is preserved: with $\tilde{Ξ}_{\mathrm{sp}}(r'_t) = \tilde Q\tilde{Ξ}_{\mathrm{sp}}(0)$,

$$
\mathrm{Tr}\!\left(\tilde{Ξ}_{\mathrm{sp}}(r'_t)^{*}\tilde{Ξ}_{\mathrm{sp}}(r'_t)\right)
= \mathrm{Tr}\!\left(\tilde{Ξ}_{\mathrm{sp}}(0)^{*} \tilde Q^{*}\tilde Q\,\tilde{Ξ}_{\mathrm{sp}}(0)\right)
= \mathrm{Tr}\!\left(\tilde{Ξ}_{\mathrm{sp}}(0)^{*}\tilde{Ξ}_{\mathrm{sp}}(0)\right).
$$

Differentiating the solution gives $i\hbar\,c\,\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} =i\hbar\,c(-\frac{i}{\hbar\,c}\tilde R_\Psi)\tilde{Ξ}_{\mathrm{sp}} = \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}$, so it is the required solution.

**This is the second writing.** The exponent of the solution is $-\frac{i}{\hbar\,c}\tilde R_\Psi r'_t$, and its coefficient is the generator of the second writing. The $*$-unitarity of $\tilde Q$ is the statement that this coefficient is anti-Hermitian. The conservation of $\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^{*}\tilde{Ξ}_{\mathrm{sp}})$ is therefore not an extra postulate about $\tilde Q$; it is the anti-Hermiticity of the material-sector element, which is what the second writing displays.

**Case checked.** For $\tilde R_\Psi = i\,\vec e_x$ one has $r_t = 0$, $\vec r_\Psi = \vec e_x$, and $\tilde Q(r'_t) = \cos(\frac{r'_t}{\hbar\,c})e_t + \sin(\frac{r'_t}{\hbar\,c})\vec e_x$. Then $\tilde Q(r'_t)$ is $*$-unitary, and $\tilde R_\Psi\tilde Q = i \vec e_x(\cos(\frac{r'_t}{\hbar\,c})e_t + \sin(\frac{r'_t}{\hbar\,c})\vec e_x) = i\cos(\frac{r'_t}{\hbar\,c})\vec e_x - i\sin(\frac{r'_t}{\hbar\,c})e_t$ equals $i\hbar\,c\,\frac{d\tilde{Q}}{dr'_{t}}= i(-\sin(\frac{r'_t}{\hbar\,c})e_t + \cos(\frac{r'_t}{\hbar\,c})\vec e_x)$, term by term. This case was chosen independently of the general formula and confirms it.

**Consistency with the density matrix.** The companion article's equation follows from the field equation. For $\tilde{Ϛ}_{\Psi} = \tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{*}$, differentiating and using $\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = -\frac{i}{\hbar\,c}\tilde R_\Psi\tilde\Xi_{\mathrm{sp}}$ and $\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}}^{*} =\frac{i}{\hbar\,c}\tilde\Xi_{\mathrm{sp}}^{*}\tilde R_\Psi$ (valid because $\tilde R_\Psi^{*} = \tilde R_\Psi$) gives

$$
\boxed{\;\partial/\partial r'_t\tilde{Ϛ}_{\Psi} = -\frac{i}{\hbar\,c}\tilde R_\Psi\tilde{Ϛ}_{\Psi} +\frac{i}{\hbar\,c}\tilde{Ϛ}_{\Psi}\tilde R_\Psi
= -\frac{i}{\hbar\,c}[\tilde R_\Psi,\tilde{Ϛ}_{\Psi}],
\qquad\text{i.e.}\qquad i\hbar\,c\,\partial/\partial r'_t\tilde{Ϛ}_{\Psi} = [\tilde R_\Psi,\tilde{Ϛ}_{\Psi}]\;},
$$

which is the von Neumann equation of the companion article. The normalisation by $\rho$ is a constant scalar and passes through the derivative, so the same equation holds for the unit-trace state. The mean of an observable in the field is read from the same object and needs nothing further: for Hermitian $\tilde R_\Psi$,

$$
\langle\tilde R_\Psi\rangle_{\tilde{Ξ}} = \frac{\mathrm{Sc}(\tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{*})}{\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{*})} = \mathrm{Sc}\bigl(\tilde R_\Psi\tilde{Ϛ}_{\Psi}\bigr)\in\mathbb{R},
$$

which is real because the symbol is Hermitian, and which reduces in the matrix picture to $\operatorname{Tr}(H\mathsf{M}_2(\tilde{Ϛ}_{\Psi}))$, with $H$ the energy reading of $\tilde R_\Psi$. Questions of the form "is the field on this axis" belong to the corpus's measurement articles and are not needed here; no projector enters this article.

## The Equation Written in $\mathbb{B}_{\Phi}$

The second writing puts the derivative alone on the left and the generator on the right,

$$
\partial/\partial r'_t\,\tilde{Ξ}_{\mathrm{sp}} = -\frac{i}{\hbar\,c}\tilde R_\Psi\,\tilde{Ξ}_{\mathrm{sp}},
\qquad
-\frac{i}{\hbar\,c}\tilde R_\Psi = \frac{\vec r_\Psi - i r_t\,e_t}{\hbar\,c} \in \mathbb{B}_{\Phi}.
$$

The generator is anti-Hermitian, and that is the general reason the exponential is $*$-unitary. The element carries no glyph of its own in this article: it is the observable multiplied by the central number $-\frac{i}{\hbar\,c}$, and a second letter would hide that.

**The material-sector interpretation.** The generator lies in $\mathbb{B}_{\Phi}$, the *material* sector, the same four-dimensional real space that carries the four-vectors of relativistic physics. The time-translation generator is an element of that sector, and multiplying it by $i\hbar\,c$ returns the Hermitian observable $\tilde R_\Psi$. The two writings are then one statement about one space and its image under the central $i$: the observable is what the generator reads as when the intertwiner is undone.

**What this does not show.** The equation carries $\partial/\partial r'_t$ and no spatial derivative, so it is not a four-dimensional equation, and nothing here applies the Lorentz action $\tilde R_\Phi\mapsto\tilde U_{\mathrm{lor}}\tilde R_\Phi\tilde U_{\mathrm{lor}}^{*}$ to the generator. The label *material sector* says which space the generator belongs to. It does not say that the generator transforms as a four-vector, and this article does not show that it does. Whether a Lorentz-covariant reading replaces $\partial/\partial r'_t$ by a four-gradient is open, and the question is stated with the non-relativistic limit at the end of the article.

**The von Neumann form is the cleanest instance.** For $\tilde R_\Psi, \tilde{Ϛ}_{\Psi} \in \mathbb{B}_{\Psi}$,

$$
\left([\tilde R_\Psi,\tilde{Ϛ}_{\Psi}]\right)^{*} = \tilde{Ϛ}_{\Psi}\tilde R_\Psi - \tilde R_\Psi\tilde{Ϛ}_{\Psi} = -[\tilde R_\Psi,\tilde{Ϛ}_{\Psi}],
$$

so $[\tilde R_\Psi,\tilde{Ϛ}_{\Psi}] \in \mathbb{B}_{\Phi}$; and since $\tilde{Ϛ}_{\Psi} \in \mathbb{B}_{\Psi}$ and $i\,\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi}$, the term $i\hbar\,c\,\partial/\partial r'_t\tilde{Ϛ}_{\Psi}$ is also in $\mathbb{B}_{\Phi}$. The von Neumann equation is an identity in a single sector, while its solution returns to the complementary one. Both of its sides are elements of the material sector, and the state they act on is in the informational one.

**The sectors label operators, not states.** The decomposition $\mathbb{B} = \mathbb{B}_{\Psi} \oplus \mathbb{B}_{\Phi}$ classifies Hermitian observables and anti-Hermitian generators, and the field $\tilde{Ξ}_{\mathrm{sp}}$, being one general element of $\mathbb{B}$, carries no such label. What returns to $\mathbb{B}_{\Psi}$ is the bilinear object $\tilde{Ϛ}_{\Psi} = \tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{*}$, not $\tilde{Ξ}_{\mathrm{sp}}$. Reading the sector labels onto the wave function is the same error as conflating the wave function with the density matrix.

## Why the Unit Must Be Central

It remains to show that $i$ is the only unit that keeps both writings available at once. Suppose a root $\tilde{Ζ}$ with $\tilde{Ζ}^2 = -e_t$ is used in place of $i$:

$$
\hbar\,c\,\tilde{Ζ}\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}
\qquad\Longrightarrow\qquad
\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = -\frac{\tilde{Ζ}\tilde R_\Psi}{\hbar\,c}\,\tilde{Ξ}_{\mathrm{sp}},
$$

so the generator of the flow is $-\frac{\tilde{Ζ}\tilde R_\Psi}{\hbar\,c}$. The first writing needs no condition on $\tilde{Ζ}$: its coefficient is the Hermitian $\tilde R_\Psi$ by hypothesis. The second writing needs its generator anti-Hermitian, for every Hermitian $\tilde R_\Psi$, because the Hamiltonian is arbitrary. The flow preserves the Hermitian form, i.e. $\exp(-\frac{\tilde{Ζ}\tilde R_\Psi\,r'_t}{\hbar\,c})$ is $*$-unitary, exactly when $-\frac{\tilde{Ζ}\tilde R_\Psi}{\hbar\,c}$ is anti-Hermitian, which is the condition

$$
(\tilde{Ζ}\tilde R_\Psi)^{*} = -\tilde{Ζ}\tilde R_\Psi
\qquad\Longleftrightarrow\qquad
\tilde R_\Psi\tilde{Ζ}^{*} = -\tilde{Ζ}\tilde R_\Psi
\quad\text{for all Hermitian } \tilde R_\Psi.
$$

Taking $\tilde R_\Psi = e_t$ gives $\tilde{Ζ}^{*} = -\tilde{Ζ}$, so $\tilde{Ζ}$ must be anti-Hermitian; the condition then becomes $\tilde R_\Psi\tilde{Ζ} = \tilde{Ζ}\tilde R_\Psi$ for every Hermitian $\tilde R_\Psi$. Take $\tilde R_\Psi = i\,\vec e_\mu$ with $\mu = x,y,z$, which is Hermitian: since $i$ is central, the condition reads $\vec e_\mu \tilde{Ζ} = \tilde{Ζ}\vec e_\mu$, so $\tilde{Ζ}$ commutes with the quaternion units. Writing $\tilde{Ζ} = q_t e_t + \sum_\mu q_\mu \vec e_\mu$ with $\mu=x,y,z$, the relation with $\vec e_x$ gives $q_y = q_z = 0$, and the relation with $\vec e_z$ then gives $q_x = 0$, leaving $\tilde{Ζ} = q_te_t$ with $q_t \in \mathbb{C}$. The centralizer of the quaternion units is therefore the centre $\mathbb{B}_{C} = \operatorname{span}_{\mathbb{R}}\{e_t, ie_t\}$: $\tilde{Ζ}$ is central. Then $\tilde{Ζ}^2 = -e_t$ gives $q_t^2 = -1$, so $q_t = \pm i$. Thus the scalar imaginary is the *unique* choice, up to sign, that keeps the second writing in the material sector for every Hermitian Hamiltonian, and with it keeps the flow norm-preserving. The same computation is the flow theorem of *Unitarity from Centrality: The Biquaternion Norm-Preservation Theorem*, stated there for the general unit.

**A counterexample for a quaternion unit.** Take $\vec{Ζ} = \vec e_z$ (a root of $-1$) and the Hermitian $\tilde R_\Psi = i\,\vec e_x$. Then

$$
\vec{Ζ}\tilde R_\Psi = \vec e_z\,(i \vec e_x) = i\,\vec e_z \vec e_x = i\,\vec e_y,
$$

using $\vec e_z \vec e_x = \vec e_y$. Since $i\,\vec e_y$ is Hermitian, $(i\vec e_y)^{*} = i\vec e_y$, the generator $-\frac{\vec Ζ\,\tilde R_\Psi}{\hbar\,c}= -\frac{i\,\vec e_{y}}{\hbar\,c}$ is Hermitian, not anti-Hermitian. That is the failure, and it is a failure of the second writing: the generator is not in $\mathbb{B}_{\Phi}$, so the second writing is not available. The loss of norm follows. Explicitly, at $r'_t =\frac{\pi\,\hbar\,c}{2}$,

$$
\tilde Q^{*}\tilde Q = \exp\!\left(-i\pi \vec e_y\right)
= \cosh(\pi)\,e_t - i\sinh(\pi)\,\vec e_y \neq e_t,
$$

so the norm is not preserved by this "Schrödinger equation". The failure is generic: after the necessary condition $\tilde{Ζ}^{*}=-\tilde{Ζ}$ is met, the requirement is $\tilde R_\Psi\tilde{Ζ}=\tilde{Ζ}\tilde R_\Psi$, so a non-central root fails for every Hermitian Hamiltonian that does not commute with it, and every non-central root has such Hamiltonians.

There is a second defect in the non-central choice: because $\vec e_z \vec e_x = \vec e_y$ while $\vec e_x \vec e_z = -\vec e_y$, the elements $\vec e_z\tilde{Ξ}_{\mathrm{sp}}$ and $\tilde{Ξ}_{\mathrm{sp}} \vec e_z$ differ, so the left- and right-handed interpretations of "the same" equation produce opposite generators. The centrality of $i$ removes this ambiguity.

**A caveat, stated honestly.** A non-central $\tilde{Ζ}$ is not always inadmissible: if a particular $\tilde R_\Psi$ commutes with $\tilde{Ζ}$, then $\tilde{Ζ}\tilde R_\Psi$ can be anti-Hermitian and the flow $*$-unitary on that sector (for instance $\tilde R_\Psi = i\,\vec e_z$ and $\vec{Ζ} = \vec e_z$, giving $\vec{Ζ}\tilde R_\Psi = -ie_t$). What fails is uniformity, and a unit that works only for Hamiltonians aligned with a preferred direction is not a unit for the Schrödinger equation, which claims no preferred direction. The caveat survives in the summary: the uniqueness is a uniqueness *for all Hermitian Hamiltonians*, and it is that uniformity, not the sign, that the algebra forces.

## What the Biquaternion Form Adds and What It Merely Relabels

**The relabelling.** Write the field in the coefficient basis as a column of four complex numbers. Left multiplication by $\tilde R_\Psi$ is then the array $L_{\mathrm{axf}}(\tilde R_\Psi)$, the central $i$ is the standard imaginary unit, $\tilde Q(r'_t)=\exp(-iL_{\mathrm{axf}}(\tilde R_\Psi)r'_t/(\hbar\,c))$ is a unitary array, and the equation is literally the complex-linear Schrödinger equation with that Hermitian symbol. In that basis the two writings are two elementary statements about arrays: the array of $\tilde R_\Psi$ is Hermitian, and the array of $-\frac{i}{\hbar\,c}\tilde R_\Psi$ is anti-Hermitian. Nothing is added to the predictions: the equation says what the standard one says, coefficient by coefficient. The one coefficient of $e_t$ carries the ordinary one-component equation; the other three carry the same equation and, in addition, a rotor and a boost that the standard equation does not name.

**What is structural.** Three features are genuinely rearranged rather than merely renamed.

1. *The isomorphism between the writings is canonical.* $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ are the fixed-point subspaces of Hermitian conjugation, and $i$ is the real-linear isomorphism that relates them. The second writing is exactly the map $\tilde R_\Psi \mapsto -\frac{i\,\tilde R_\Psi}{\hbar\,c}$ from observables to generators, and the algebra supplies that map once, without a choice. A formulation without a central unit must choose an isomorphism, or work sector by sector and carry the choice as extra input. Here the quaternion units are not candidates, being non-central, and the central root is unique up to sign.

2. *The complex structure is supplied, not chosen.* Since $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ contains the central element $i$ by construction, the complex structure of the carrier is fixed by the algebra. In a purely quaternionic formulation — wave functions valued in $\mathbb{H}$, with no complexifying factor — there is no central imaginary unit, and one must *choose* a complex structure on the carrier, so the choice becomes extra input. This is definitional — $\mathbb{C}$ was put into $\mathbb{B}$ by fiat — but the content is that the same algebra contains both the quaternion units and the central root of $-1$, unique up to sign, that quantum physics requires.

3. *The roots of $-1$ are separated by role.* The central roots $\pm i$ are the complex structure; the non-central roots $\vec u$ are rotor axes and rotation generators. A formulation that writes the Schrödinger equation with a quaternion unit destroys the first while leaving the second in place, and the counterexample above shows how. The biquaternion form keeps the two apart by construction.

**Why $\hbar$ here and not the mass wave number.** The relativistic articles of the corpus write $\tilde\nabla\tilde\Xi=k_m\tilde\Xi$ with $k_m=mc/\hbar$, and there the letter earns its place: the mass is absorbed into a wave number and the equation's constant *is* that wave number. In this equation it does not. The factor that multiplies $\partial/\partial r'_t$ is $i\hbar\,c$, the mass does not appear in it at all, and the only quantity it holds is $\hbar$. Writing $k_m$ in that slot would require the composite $\frac{m\,c^{2}\,i}{k_m}$, in which $m$ cancels, so the letter would say nothing about the mass and would hide $\hbar$ behind a symbol that the reader has to invert. The rule this article follows is that a wave number is written only where a mass, a momentum or an energy is absorbed by it. Here none is: the mass enters only through $\tilde R_\Psi$, when the Hamiltonian is read as kinetic plus potential, and the constant that multiplies the time derivative is $\hbar c$. The relativistic companions keep $k_m$; this article does not use it.

**Honest bottom line.** For a field with four complex coefficients this is the standard equation of a Hermitian symbol on that carrier. The algebra supplies the carrier, the constant $i$, and the split $\mathbb{B}=\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$ that $i$ relates; the first two are the standard equation's own, and only the third is added. It is interesting because the same algebra also carries the Lorentz group and the Dirac equation, and because its two Hermitian fixed-point subspaces correspond to the physical and informational sectors of the wider proposal; but it produces no new prediction here. Whether it produces one in the many-body or relativistic setting is open.

## Open Questions

**1. The local complex structure.** The series makes the complex structure local: it is set by the medium through $c = 1/\sqrt{\epsilon\mu}$ and reduces to $i r'_t$ in vacuum. The scalar imaginary $i$ is a global central element of $\mathbb{B}$, and a central element cannot vary from point to point. Does the $i$ of the Schrödinger equation remain global, or does the carrier inherit a local complex structure from the medium? The question is the one stated in *The Local Complex Structure and the Speed of Light*, and this article takes no position on it: it uses the global $i$ throughout. The two treatments must agree before the question is closed.

**2. Many fields.** The extension to several fields is via $\mathbb{B}^{\otimes n}$, a complex algebra of dimension $2^{2n}$. The companion article leaves the tensor product over $\mathbb{C}$ as an open question. If it is taken over $\mathbb{C}$, the scalar imaginary remains available as the complex structure; if not, the question of the imaginary unit returns in a new form.

**3. Which of the four coefficients is physical.** The field has four complex coefficients and the equation treats them alike. Whether all four are physical, or whether three of them are a gauge artefact of the quaternionic structure, is not settled here. The polar companion article shows that three of them form the field's rotor: the rotor's angle runs at $|\vec r_\Psi|/\hbar$, and every direction it carries turns at $2|\vec r_\Psi|/\hbar$, so the rotor is not removable by a phase.

**4. The non-relativistic limit, and the transformation law.** Two questions belong together here. Whether this Schrödinger equation is the precise non-relativistic limit of the biquaternion Dirac equation, or only an independent equation with the same symbol, is not checked here. And the material-sector reading of the generator lacks its transformation law: the article shows that $-i\tilde R_\Psi/\hbar\,c$ lies in $\mathbb{B}_{\Phi}$ and does not show that it transforms as a four-vector under $\tilde U_{\mathrm{lor}}$. A four-gradient in place of $\partial/\partial r'_t$ would settle both, and neither is attempted.

**5. Second quantization and the path integral.** The framework is first-quantized and has no path-integral form in this article; both are open in the parent.

## Summary

One equation carries two writings. The first is $i\hbar\,c\,\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}$, with $\tilde R_\Psi = r_t\,e_t + i\vec r_\Psi \in \mathbb{B}_{\Psi}$ Hermitian and $\tilde{Ξ}_{\mathrm{sp}}$ one element of $\mathbb{B}$ with four complex coefficients. The second is $\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = -\frac{i}{\hbar\,c}\tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}$, whose generator $-\frac{i}{\hbar\,c}\tilde R_\Psi=\frac{\vec r_\Psi-i r_t e_t}{\hbar\,c}$ lies in the material sector $\mathbb{B}_{\Phi}$. They are one equation: the scalar imaginary $i$ is central, so $i\tilde R_\Psi$ is anti-Hermitian, and the two writings differ by the central constant $i\hbar\,c$.

The $\mathbb{B}_{\Psi}$ writing is the physical one. It names the observable, and its solution $\tilde Q(r'_t)=\exp(-i\tilde R_\Psi r'_t/\hbar\,c)$ is $*$-unitary. That $*$-unitarity is exactly the anti-Hermiticity of the generator, so the conservation of $\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^{*}\tilde{Ξ}_{\mathrm{sp}})$ is the second writing read back in the first.

The $\mathbb{B}_{\Phi}$ writing locates the generator in the material sector, the four-dimensional real space that carries the four-vectors. Multiplying the generator by $i\hbar\,c$ returns the observable. What the article does not show is that the generator transforms as a four-vector; the label names the space and not yet the transformation law.

The field is a general element of $\mathbb{B}$, not an element of $\mathbb{B}_{\Psi}$, because both writings must hold in the carrier for every Hermitian Hamiltonian, and only $\mathbb{B}$ is closed under left multiplication by both sectors. The density matrix is recovered as $\tilde{Ϛ}_{\Psi} = \tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{*}/\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^{*}\tilde{Ξ}_{\mathrm{sp}}) \in \mathbb{B}_{\Psi}$, and the field equation implies the companion article's von Neumann equation $i\hbar\,c\,\partial/\partial r'_t\tilde{Ϛ}_{\Psi} = [\tilde R_\Psi,\tilde{Ϛ}_{\Psi}]$.

The uniqueness of $i$ up to sign is what makes both writings available simultaneously. Using a non-central root $\tilde{Ζ}$ in place of $i$ fails generically: the generator $-\frac{\tilde{Ζ}\tilde R_\Psi}{\hbar\,c}$ need not be anti-Hermitian, so it need not lie in $\mathbb{B}_{\Phi}$, and the norm is not preserved (explicitly for $\vec{Ζ} = \vec e_z$, $\tilde R_\Psi = i\vec e_x$). The scalar imaginary is the only choice, up to sign, that works for every Hermitian Hamiltonian.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\mu^2 = -e_t$ |
| $i$ | Scalar imaginary, central, $i^2 = -e_t$ |
| $\hbar$ | Reduced Planck constant; the constant of the equation, $i\hbar\,c\,\partial/\partial r'_t\tilde\Xi=\tilde R_\Psi\tilde\Xi$ |
| $\mathbb{B}_{C}$ | Complex subspace $\operatorname{span}_{\mathbb{R}}\{e_t, ie_t\}$; the centre |
| $\mathbb{B}_{\Psi}$ | Hermitian subspace (observables): $i\hbar\,c\,\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}$ has $\tilde R_\Psi \in \mathbb{B}_{\Psi}$ |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian subspace (generators, the material sector): the generator is $-\frac{i\,\tilde R_\Psi}{\hbar\,c}\in\mathbb{B}_{\Phi}$ |
| $\mathbb{B}_{H}$ | Real quaternion subspace; home of the unit pure quaternions $\vec u$ |
| $\tilde R_\Psi = r_t\,e_t + i\vec r_\Psi$ | Hermitian element; the Hamiltonian, and the observable named by the first writing |
| $-\frac{i}{\hbar\,c}\tilde R_\Psi=\frac{\vec r_\Psi-i r_t e_t}{\hbar\,c}$ | The generator named by the second writing; anti-Hermitian, in $\mathbb{B}_{\Phi}$ |
| $\tilde{Ξ}_{\mathrm{sp}}$ | The field: one element of $\mathbb{B}$; `sp` marks the spinor role |
| $L_{\tilde R_\Psi}$, $L_{\mathrm{axf}}(\tilde R_\Psi)$ | Left multiplication by $\tilde R_\Psi$; its $4\times4$ axis-free array in the coefficient basis |
| $\tilde{Ϛ}_{\Psi} = \tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{*}/\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^{*}\tilde{Ξ}_{\mathrm{sp}})$ | Density matrix associated to the field |
| $\tilde Q(r'_t) = \exp(-i\tilde R_\Psi r'_{t}/(\hbar\,c))$ | $*$-Unitary evolution, $\tilde{Ξ}_{\mathrm{sp}}(r'_t) = \tilde Q(r'_t)\tilde{Ξ}_{\mathrm{sp}}(0)$ |
| $\langle\tilde R_\Psi\rangle_{\tilde{Ξ}} = \mathrm{Sc}(\tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{*})/\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{*})$ | Mean of the observable in the field |
| $\vec e_\mu \vec e_\nu = \varepsilon_{\mu\nu\lambda}\vec e_\lambda$, $\mu \neq \nu$ | Quaternion multiplication |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | The general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | The general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |

## Further Reading

- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the original state-vector formulation.
- John von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton, 1932), for the density-matrix formulation and the von Neumann equation.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard two-component Schrödinger equation.
- Stephen L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford, 1995), for the quaternionic formulation in which a complex structure must be chosen.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the algebra $\mathbb{B}\cong M_2(\mathbb{C})$ and its representation theory, used here only as an external check.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of the Schrödinger equation.
