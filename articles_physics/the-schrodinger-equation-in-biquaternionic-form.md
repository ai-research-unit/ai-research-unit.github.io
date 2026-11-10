# __The Schrödinger Equation in Biquaternionic Form__

## Introduction

For a state $|\Xi\rangle$ and a Hamiltonian $H$, the Schrödinger equation of standard quantum physics is

$$i\hbar\,c\partial/\partial r'_t|\Xi\rangle = H\,|\Xi\rangle,
$$

and for a density matrix $\rho$ the same dynamics reads $i\hbar\,c\partial/\partial r'_t\rho = [H,\rho]$. Both statements have biquaternion forms, and it matters which of the two one has in hand.

The companion article *Quantum Physics in Biquaternionic Form* treats the second form: it exhibits the $*$-unitary biquaternion $\tilde Q(r'_t)$ obeying $i\hbar\,c\,\frac{d\tilde{Q}}{dr'_{t}}= \tilde R_\Psi\tilde Q$ and the state equation $i\hbar\,c\,\frac{d\tilde{Ϛ}_{\Psi}}{dr'_{t}}= [H,\tilde{Ϛ}_{\Psi}]$ for $\tilde{Ϛ}_{\Psi} \in \mathbb{B}_{\Psi}$. It does **not** write the field equation $i\hbar\,c\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}$, nor examine its symbol $i$. That is a difference of object rather than an oversight: the objects of that equation are Hermitian elements of $\mathbb{B}_{\Psi}$, i.e. density-matrix-like objects, whereas the field of a wave equation is something else. This article supplies the field form and settles what its $i$ denotes.

The question is not decorative. In and around the algebra $\mathbb{B}$ there are three distinct things commonly written with a symbol that squares to $-1$ or plays the role of $i$:

- the **scalar imaginary** $i$, which is central;
- the **quaternion units** $\vec e_x,\vec e_y,\vec e_z$ and, more generally, the non-central roots of $-1$ in $\mathbb{B}$;
- the **complex structure** that a carrier must carry for the Schrödinger equation to be complex-linear.

The first two are different elements of the algebra; no conjugation relates them, and they play unrelated roles. The third is not an element of the algebra at all but a structure that the carrier carries. Conflating them is the characteristic error, and it produces equations that look like the Schrödinger equation but do not preserve probability. Separating them is the substance of this article.

The article is organized as follows. The three objects are distinguished; the scalar imaginary is shown to exchange the sectors $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$; the field is identified as one element of the algebra, with four complex coefficients, and not as an element of $\mathbb{B}_{\Psi}$; the equation and its solution are written and checked; the non-central alternatives are tested and one is shown to fail; the $\mathbb{B}_{\Phi}$/$\mathbb{B}_{\Psi}$ interpretation is given. It closes with an honest account of what the form adds and what it merely relabels.

## Three Objects That Square to Minus One

### The scalar imaginary

The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with quaternion basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_\mu^2 = -e_t$ and $\vec e_\mu \vec e_\nu = \varepsilon_{\mu\nu\lambda}\vec e_\lambda$ for $\mu,\nu \in \{x,y,z\}$, $\mu \neq \nu$. The **scalar imaginary** $i$ is the image of the imaginary unit of the complexifying factor $\mathbb{C}$. It satisfies $i^2 = -e_t$ and is **central**: it commutes with every element of $\mathbb{B}$.

The central elements are exactly the complex scalars,

$$
\mathbb{B}_{C} = \{Q_t\,e_t : Q_t \in \mathbb{C}\} = \operatorname{span}_{\mathbb{R}}\{e_t, i\,e_t\},
$$

a copy of the complex line embedded as the scalar part, and it is the centre of $\mathbb{B}$. Within it the roots of $-1$ are exactly $\pm i$: the scalar imaginary is not "one root of $-1$ among many" but *the* central one.

### The quaternion units and the non-central roots

Each quaternion unit satisfies $\vec e_\mu^2 = -e_t$, but the $\vec e_\mu$ do not commute: $\vec e_x \vec e_y = \vec e_z = -\vec e_y \vec e_x$. They are non-central roots of $-1$. The companion article on biquaternion roots of minus one classifies all roots $\tilde{Ζ}$ with $\tilde{Ζ}^2 = -e_t$: either $\tilde{Ζ} = \pm i$ (the central roots), or $\tilde{Ζ} = \vec Q$ is a complex vector with $(\vec Q,\vec Q) := Q_x^2 + Q_y^2 + Q_z^2 = 1$ (the non-central roots). The real members of the second family are the **unit pure real quaternions** $\vec u \in \mathbb{B}_{H}$, with $|\vec u| = 1$, so $\vec u^2 = -e_t$ and $\vec u^\dagger = -\vec u \in \mathbb{B}_{\Phi}$. They are the roots of $-1$ that the algebra itself carries, and each is the axis a rotor turns about. Both $\vec u$ and $i$ square to $-e_t$ and are anti-Hermitian, but $i$ is central and $\vec u$ is not.

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

## The Scalar Imaginary Exchanges the Two Sectors

The relation $i\,\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi}$ is the algebraic content of the Hermitian decomposition, and it is the whole reason the scalar imaginary is the right unit for the Schrödinger equation. Concretely, for a Hermitian element $\tilde R_\Psi = r_t\,e_t + i\vec r_\Psi \in \mathbb{B}_{\Psi}$, using $\tilde R_\Psi^{*} = \tilde R_\Psi$, $i^{*} = -i$, and the centrality of $i$,

$$
(i\tilde R_\Psi)^{*} = \tilde R_\Psi^{*} i^{*} = \tilde R_\Psi\,(-i) = -i\tilde R_\Psi.
$$

So $i\tilde R_\Psi \in \mathbb{B}_{\Phi}$: the map $\tilde R_\Psi \mapsto i\tilde R_\Psi$ is a real-linear isomorphism $\mathbb{B}_{\Psi} \to \mathbb{B}_{\Phi}$ with inverse $\tilde{Q} \mapsto -i\tilde{Q}$, turning a Hermitian observable into an anti-Hermitian object. For example, with $\tilde R_\Psi = i\,\vec e_x$ (Hermitian, since $(i\vec e_x)^{*} = i\vec e_x$), one has $i\tilde R_\Psi = i\,(i\vec e_x) = -\vec e_x$, and $-\vec e_x$ is anti-Hermitian because $(-\vec e_x)^{*} = -(-\vec e_x)$. This is the elementary observation on which everything below rests.

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

**The display, where a display is wanted, is the axis-free array.** In the coefficient basis the symbol is the array $L_{\mathrm{axf}}(\tilde R_\Psi)$, a $4\times4$ complex matrix with $\mathrm{Tr}L_{\mathrm{axf}}(\tilde R_\Psi)=4r_t$ and $\det L_{\mathrm{axf}}(\tilde R_\Psi)=\langle\tilde R_\Psi\rangle_{\natural}^{2}$, Hermitian on the nose, and it names no spatial direction. The equation is therefore the ordinary complex-linear Schrödinger equation on four complex coefficients with that Hermitian symbol, and nothing beyond the algebra enters the display.

### The four coefficients, and the central field

The field carries one complex coefficient of $e_t$ and three of $\vec e_\mu$, that is $2+6$ real numbers. A field with only the scalar coefficient nonzero,

$$
\tilde\Xi_{\mathrm{sp}}(r'_t)=\Xi_t(r'_t)\,e_t,
$$

is called **central**, and for it $\tilde R_\Psi\tilde\Xi_{\mathrm{sp}}=H\Xi_t\,e_t$ exactly when $\vec r_\Psi=0$: the equation then reduces to the ordinary one-component equation for $\Xi_t$. The remaining six real parameters are the field's rotor and boost, and *The Polar Form of the Schrödinger Equation in Biquaternionic Form* reads them.

**Why not $\mathbb{B}_{\Psi}$.** The temptation is to let the "state" $\tilde{Ϛ}_{\Psi}\in\mathbb{B}_{\Psi}$ of the companion article serve as the field. The obstacle is not that the equation admits no $\mathbb{B}_{\Psi}$-valued solution — it does — but that $\mathbb{B}_{\Psi}$ is neither a subalgebra nor closed under left multiplication by a Hermitian element (for example $(i\vec e_x)(i\vec e_y)=-\vec e_z\in\mathbb{B}_{\Phi}$), so $\tilde R_\Psi\tilde\Xi_{\mathrm{sp}}$ need not be Hermitian, and the equation does not define a flow on $\mathbb{B}_{\Psi}$. A Hermitian-valued solution exists — with $\tilde R_\Psi=i\vec e_x$ and $\tilde\Xi_{\mathrm{sp}}(r'_t)=i(\cos\theta\,\vec e_y+\sin\theta\,\vec e_z)$, $\theta=r'_t/(\hbar\,c)$, both sides equal $\sin\theta\,\vec e_y-\cos\theta\,\vec e_z$ — but its being a solution is a coincidence of that sector and not a structure of the equation. The carrier of the flow is $\mathbb{B}$.

### Vanishing, the cone, and the density

The ordinary wave function may vanish, and the vanishing is a point at which the polar parametrisation of the companion article is undefined. Here the analogous locus is larger and it is algebraic: the field is a zero divisor exactly when its quaternionic norm vanishes,

$$
\langle\tilde\Xi_{\mathrm{sp}}\rangle_{\natural}=\tilde\Xi_{\mathrm{sp}}\tilde\Xi_{\mathrm{sp}}^{\natural}=0,
$$

which is the zero-divisor cone of the algebra. A generic element is off it — a random element has $N\neq0$ with probability one — and the flow keeps it there, because $\langle\tilde Q\tilde\Xi\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}\langle\tilde\Xi\rangle_{\natural}$ and $\langle\tilde Q\rangle_{\natural}$ is a central unit. So the field of this equation is a unit of the algebra at almost every point of space and time, and it stays one.

**The density is the Hermitian norm.** Put

$$
\rho=\mathrm{Tr}\bigl(\tilde\Xi_{\mathrm{sp}}^{\dagger}\tilde\Xi_{\mathrm{sp}}\bigr)=2\,\mathrm{Sc}\bigl(\tilde\Xi_{\mathrm{sp}}\tilde\Xi_{\mathrm{sp}}^{*}\bigr)\ge0,
\qquad
\tilde\varrho_{\Psi}=\frac{\tilde\Xi_{\mathrm{sp}}\tilde\Xi_{\mathrm{sp}}^{\dagger}}{\rho}\in\mathbb{B}_{\Psi},
$$

which is Hermitian, positive and of unit trace, so $\tilde\varrho_{\Psi}$ is a state in the sense of the companion article. The field and that state are not the same object; they are related by $\tilde\Xi_{\mathrm{sp}}\mapsto\tilde\Xi_{\mathrm{sp}}\tilde\Xi_{\mathrm{sp}}^{\dagger}$, and the same central $i$ acts as the complex structure on the field while exchanging the sectors in which the operator is expressed. The expectation of the Hamiltonian in a field is $\mathrm{Sc}(\tilde R_\Psi\tilde\varrho_{\Psi})$, which is real by the Hermiticity above.

## The Schrödinger Equation and Its Solution

With these objects separated, the equation reads

$$
\boxed{\;i\hbar\,c\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}}(r'_t) = \tilde R_\Psi\,\tilde{Ξ}_{\mathrm{sp}}(r'_t),
\qquad
\tilde R_\Psi = r_t\,e_t + i\vec r_\Psi \in \mathbb{B}_{\Psi},
\qquad
\tilde{Ξ}_{\mathrm{sp}}(r'_t) \in \mathbb{B}\;},
$$

where $i$ is the scalar imaginary and $\hbar$ is the reduced Planck constant. Because $i$ is central, $i\tilde R_\Psi=\tilde R_\Psi i$, and there is no left/right ordering ambiguity in the equation. Because $\mathbb{B}$ is an algebra, $\tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}\in\mathbb{B}$: the equation is consistent in the carrier, and no ideal is needed for the consistency.

**Why $\hbar$ here and not the mass wave number.** The relativistic articles of the corpus write $\tilde\nabla\tilde\Xi=k_m\tilde\Xi$ with $k_m=mc/\hbar$, and there the letter earns its place: the mass is absorbed into a wave number and the equation's constant *is* that wave number. In this equation it does not. The factor that multiplies $\partial/\partial r'_t$ is $i\hbar\,c$, the mass does not appear in it at all, and the only quantity it holds is $\hbar$. Writing $k_m$ in that slot would require the composite $\frac{m\,c^{2}\,i}{k_m}$, in which $m$ cancels, so the letter would say nothing about the mass and would hide $\hbar$ behind a symbol that the reader has to invert. The rule this article follows is that a wave number is written only where a mass, a momentum or an energy is absorbed by it. Here none is: the mass enters only in the operator, through the kinetic term of the potential, and the constant that multiplies the time derivative is $\hbar c$. The relativistic companions keep $k_m$; this article does not use it. 

**Solution.** Since $-i\tilde R_\Psi = -i r_t\,e_t + \vec r_\Psi$ and the scalar and vector parts commute,

$$
\boxed{\;\tilde Q(r'_t) = \exp\!\left(-i\frac{H\,r'_{t}}{\hbar\,c}\right)
= \exp(-i\frac{r_t\,r'_t}{\hbar\,c})\left(\cos\theta\,e_t + \sin\theta\,\vec u_\Psi\right),
\qquad
\theta =\frac{|\vec r_\Psi|r'_t}{\hbar\,c}\;},
$$

and $\tilde{Ξ}_{\mathrm{sp}}(r'_t) = \tilde Q(r'_t)\tilde{Ξ}_{\mathrm{sp}}(0)$. The element $\tilde Q$ is $*$-unitary, $\tilde Q\tilde Q^{*} = e_t$: the central phase cancels and $R = \cos\theta\,e_t + \sin\theta\,\vec u_\Psi$ is a unit real quaternion, $R R^{*} = e_t$. Consequently the Hermitian norm $\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\tilde{Ξ}_{\mathrm{sp}})$ is preserved: with $\tilde{Ξ}_{\mathrm{sp}}(r'_t) = \tilde Q\tilde{Ξ}_{\mathrm{sp}}(0)$,

$$
\mathrm{Tr}\!\left(\tilde{Ξ}_{\mathrm{sp}}(r'_t)^\dagger\tilde{Ξ}_{\mathrm{sp}}(r'_t)\right)
= \mathrm{Tr}\!\left(\tilde{Ξ}_{\mathrm{sp}}(0)^\dagger \tilde Q^{*}\tilde Q\,\tilde{Ξ}_{\mathrm{sp}}(0)\right)
= \mathrm{Tr}\!\left(\tilde{Ξ}_{\mathrm{sp}}(0)^\dagger\tilde{Ξ}_{\mathrm{sp}}(0)\right).
$$

Differentiating the solution gives $i\hbar\,c\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} =i\hbar\,c(-\frac{i\,H}{\hbar\,c})\tilde{Ξ}_{\mathrm{sp}} = \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}$, so it is the required solution.

**Case checked.** For $\tilde R_\Psi = i\,\vec e_x$ one has $r_t = 0$, $\vec r_\Psi = \vec e_x$, and $\tilde Q(r'_t) = \cos(\frac{r'_t}{\hbar\,c})e_t + \sin(\frac{r'_t}{\hbar\,c})\vec e_x$. Then $\tilde Q(r'_t)$ is $*$-unitary, and $\tilde R_\Psi\tilde Q = i \vec e_x(\cos(\frac{r'_t}{\hbar\,c})e_t + \sin(\frac{r'_t}{\hbar\,c})\vec e_x) = i\cos(\frac{r'_t}{\hbar\,c})\vec e_x - i\sin(\frac{r'_t}{\hbar\,c})e_t$ equals $i\hbar\,c\,\frac{d\tilde{Q}}{dr'_{t}}= i(-\sin(\frac{r'_t}{\hbar\,c})e_t + \cos(\frac{r'_t}{\hbar\,c})\vec e_x)$, term by term. This case was chosen independently of the general formula and confirms it.

**Consistency with the density matrix.** The companion article's equation for $\tilde{Ϛ}_{\Psi} = \tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$ follows from the field equation. Differentiating $\tilde{Ϛ}_{\Psi} = \tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$ and using $\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = -\frac{i\,\tilde R_\Psi\tilde\Xi_{\mathrm{sp}}}{\hbar\,c}$, $\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}}^{\dagger} =\frac{i\,\tilde\Xi_{\mathrm{sp}}^{\dagger}\tilde R_\Psi}{\hbar\,c}$ (valid because $\tilde R_\Psi^{*} = \tilde R_\Psi$) gives

$$
\boxed{\;\partial/\partial r'_t\tilde{Ϛ}_{\Psi} = -\frac{i}{\hbar\,c}\tilde R_\Psi\tilde{Ϛ}_{\Psi} +\frac{i}{\hbar\,c}\tilde{Ϛ}_{\Psi}\tilde R_\Psi
= -\frac{i}{\hbar\,c}[H,\tilde{Ϛ}_{\Psi}],
\qquad\text{i.e.}\qquadi\hbar\,c\partial/\partial r'_t\tilde{Ϛ}_{\Psi} = [H,\tilde{Ϛ}_{\Psi}]\;},
$$

which is the von Neumann equation of the parent article. The mean of an observable in the field is read from the same object and needs nothing further: for Hermitian $\tilde R_\Psi$,

$$
\langle\tilde R_\Psi\rangle_{\tilde{Ξ}} = \frac{\mathrm{Sc}(\tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{\dagger})}{\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{\dagger})} = \mathrm{Sc}\bigl(\tilde R_\Psi\tilde\varrho_{\Psi}\bigr)\in\mathbb{R},
$$

which is real because the symbol is Hermitian, and which reduces to $\operatorname{Tr}(H\varrho)$ in the matrix picture. Questions of the form "is the field on this axis" belong to the corpus's measurement articles and are not needed here; no projector enters this article.

## Why the Scalar Imaginary, and Not a Quaternion Unit

It is worth making precise why the obvious alternatives to $i$ fail. Suppose a root $\tilde{Ζ}$ with $\tilde{Ζ}^2 = -1$ is used in place of $i$:

$$\hbar\,c\,\tilde{Ζ}\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}
\qquad\Longrightarrow\qquad
\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = -\frac{\tilde{Ζ}\tilde R_\Psi}{\hbar\,c}\,\tilde{Ξ}_{\mathrm{sp}},
$$

so the generator of the flow is $-\frac{\tilde{Ζ}\tilde R_\Psi}{\hbar\,c}$. The flow preserves the Hermitian form, i.e. $\exp(-\frac{\tilde{Ζ}\tilde R_\Psi\,r'_t}{\hbar\,c})$ is $*$-unitary, exactly when $-\frac{\tilde{Ζ}\tilde R_\Psi}{\hbar\,c}$ is anti-Hermitian, which is the condition

$$
(\tilde{Ζ}\tilde R_\Psi)^{*} = -\tilde{Ζ}\tilde R_\Psi
\qquad\Longleftrightarrow\qquad
\tilde R_\Psi\tilde{Ζ}^\dagger = -\tilde{Ζ}\tilde R_\Psi
\quad\text{for all Hermitian } \tilde R_\Psi.
$$

Taking $\tilde R_\Psi = e_t$ gives $\tilde{Ζ}^\dagger = -\tilde{Ζ}$, so $\tilde{Ζ}$ must be anti-Hermitian; the condition then becomes $\tilde R_\Psi\tilde{Ζ} = \tilde{Ζ}\tilde R_\Psi$ for every Hermitian $\tilde R_\Psi$. Take $\tilde R_\Psi = i\,\vec e_\mu$ with $\mu = x,y,z$, which is Hermitian: since $i$ is central, the condition reads $\vec e_\mu \tilde{Ζ} = \tilde{Ζ}\vec e_\mu$, so $\tilde{Ζ}$ commutes with the quaternion units. Writing $\tilde{Ζ} = q_t e_t + \sum_\mu q_\mu \vec e_\mu$ with $\mu=x,y,z$, the relations $\vec e_x\tilde{Ζ} = \tilde{Ζ}\vec e_x$ and $\vec e_y\tilde{Ζ} = \tilde{Ζ}\vec e_y$ give $q_y = q_z = 0$ and then $q_x = 0$, leaving $\tilde{Ζ} = q_te_t$ with $q_t \in \mathbb{C}$. The centralizer of the quaternion units is therefore the centre $\mathbb{B}_{C} = \operatorname{span}_{\mathbb{R}}\{e_t, ie_t\}$: $\tilde{Ζ}$ is central. Then $\tilde{Ζ}^2 = -e_t$ gives $q_t^2 = -1$, so $q_t = \pm i$. Thus the scalar imaginary is the *unique* choice, up to sign, that makes the equation norm-preserving for every Hermitian Hamiltonian.

**A counterexample for a quaternion unit.** Take $\vec{Ζ} = \vec e_z$ (a root of $-1$) and the Hermitian $\tilde R_\Psi = i\,\vec e_x$. Then

$$
\vec{Ζ}\tilde R_\Psi = \vec e_z\,(i \vec e_x) = i\,\vec e_z \vec e_x = i\,\vec e_y,
$$

using $\vec e_z \vec e_x = \vec e_y$. Since $i\,\vec e_y$ is Hermitian, $(i\vec e_y)^{*} = i\vec e_y$, the generator $-\frac{\vec Ζ\,\tilde R_\Psi}{\hbar\,c}= -\frac{i\,\vec e_{y}}{\hbar\,c}$ is Hermitian, not anti-Hermitian, and $\exp(-\frac{\vec Ζ\,\tilde R_\Psi\,r'_t}{\hbar\,c})$ is not $*$-unitary. Explicitly, at $r'_t =\frac{\pi\,\hbar\,c}{2}$,

$$
\tilde Q^{*}\tilde Q = \exp\!\left(-i\pi \vec e_y\right)
= \cosh(\pi)\,e_t - i\sinh(\pi)\,\vec e_y \neq e_t,
$$

so the norm is not preserved by this "Schrödinger equation". The failure is generic: a non-central $\vec{Ζ}$ fails as soon as $\tilde R_\Psi$ does not commute with it.

There is a second defect in the non-central choice: because $\vec e_z \vec e_x = \vec e_y$ while $\vec e_x \vec e_z = -\vec e_y$, the elements $\vec e_z\tilde{Ξ}_{\mathrm{sp}}$ and $\tilde{Ξ}_{\mathrm{sp}} \vec e_z$ differ, so the left- and right-handed interpretations of "the same" equation produce opposite generators. The centrality of $i$ removes this ambiguity.

**A caveat, stated honestly.** A non-central $\tilde{Ζ}$ is not always inadmissible: if a particular $\tilde R_\Psi$ commutes with $\tilde{Ζ}$, then $\tilde{Ζ}\tilde R_\Psi$ can be anti-Hermitian and the flow $*$-unitary on that sector (for instance $\tilde R_\Psi = i\,\vec e_z$ and $\vec{Ζ} = \vec e_z$, giving $\vec{Ζ}\tilde R_\Psi = -ie_t$). What fails is uniformity, and a unit that works only for Hamiltonians aligned with a preferred direction is not a unit for the Schrödinger equation.

## The $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ Readings of the Equation

The equation can be rearranged into a statement that lives entirely in one sector at a time. Dividing by $i\hbar\,c$,

$$
\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = -\frac{i}{\hbar\,c}\tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}},
\qquad
-\frac{i}{\hbar\,c}\tilde R_\Psi =\frac{\vec r_\Psi - i r_t e_t}{\hbar\,c} \in \mathbb{B}_{\Phi}.
$$

The generator $-\frac{i\,H}{\hbar\,c}$ is anti-Hermitian; this is the general reason the exponential is $*$-unitary. The two interpretations are then:

- **$\mathbb{B}_{\Psi}$ interpretation.** The Hamiltonian $\tilde R_\Psi \in \mathbb{B}_{\Psi}$ is a Hermitian observable — an energy. The equation says that the dynamics is generated by that observable, read through the intertwiner $i$.
- **$\mathbb{B}_{\Phi}$ interpretation.** The generator $-\frac{i\,H}{\hbar\,c}\in\mathbb{B}_{\Phi}$ lies in the *material* sector, the same four-dimensional real space that carries the four-vectors of relativistic physics. The time-translation generator is an element of that sector; multiplying it by $i\hbar\,c$ returns the Hermitian observable $\tilde R_\Psi$.

In the von Neumann form the split is even cleaner. For $\tilde R_\Psi, \tilde{Ϛ}_{\Psi} \in \mathbb{B}_{\Psi}$,

$$
\left([H,\tilde{Ϛ}_{\Psi}]\right)^\dagger = \tilde{Ϛ}_{\Psi}\tilde R_\Psi - \tilde R_\Psi\tilde{Ϛ}_{\Psi} = -[H,\tilde{Ϛ}_{\Psi}],
$$

so $[H,\tilde{Ϛ}_{\Psi}] \in \mathbb{B}_{\Phi}$; and since $\tilde{Ϛ}_{\Psi} \in \mathbb{B}_{\Psi}$ and $i\,\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi}$, the term $i\hbar\,c\partial/\partial r'_t\tilde{Ϛ}_{\Psi}$ is also in $\mathbb{B}_{\Phi}$. The von Neumann equation is thus an identity in a single sector, while its solution returns to the complementary one.

A structural caution belongs here. The field $\tilde{Ξ}_{\mathrm{sp}}$ itself is a general element of $\mathbb{B}$, not of either sector; it carries no $\mathbb{B}_{\Psi}/\mathbb{B}_{\Phi}$ label. The decomposition $\mathbb{B} = \mathbb{B}_{\Psi} \oplus \mathbb{B}_{\Phi}$ classifies Hermitian observables and anti-Hermitian generators, not state vectors. What returns to $\mathbb{B}_{\Psi}$ is the bilinear object $\tilde{Ϛ}_{\Psi} = \tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$, not $\tilde{Ξ}_{\mathrm{sp}}$. Reading the sector labels onto the wave function is the same error as conflating the wave function with the density matrix.

## What the Biquaternion Form Adds and What It Merely Relabels

**The relabelling.** Write the field in the coefficient basis as a column of four complex numbers. Left multiplication by $\tilde R_\Psi$ is then the array $L_{\mathrm{axf}}(\tilde R_\Psi)$, the central $i$ is the standard imaginary unit, $\tilde Q(r'_t)=\exp(-L_{\mathrm{axf}}(\tilde R_\Psi)r'_t/(\hbar\,c))$ is a unitary array, and the equation is literally the complex-linear Schrödinger equation with that Hermitian symbol. Nothing is added to the predictions: the equation says what the standard one says, coefficient by coefficient. The one coefficient of $e_t$ carries the ordinary one-component equation; the other three carry the same equation and, in addition, a rotor and a boost that the standard equation does not name.

**What is structural.** Three features are genuinely rearranged rather than merely renamed.

1. *The complex structure is supplied, not chosen.* Since $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ contains the central element $i$ by construction, the complex structure of the carrier is fixed by the algebra. In a purely quaternionic formulation — wave functions valued in $\mathbb{H}$, with no complexifying factor — there is no central imaginary unit, and one must *choose* a complex structure on the carrier, so the choice becomes extra input. Here the algebra supplies it, and the quaternion units, being non-central, are not candidates. This is definitional — $\mathbb{C}$ was put into $\mathbb{B}$ by fiat — but the content is that the same algebra contains both the quaternion units and the central root of $-1$, unique up to sign, that quantum physics requires.

2. *The observable/generator split is intrinsic.* $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ are the fixed-point subspaces of Hermitian conjugation, and $i$ is the canonical real-linear isomorphism relating them. The Schrödinger equation is exactly the map $\tilde R_\Psi \mapsto -\frac{i\,\tilde R_\Psi}{\hbar\,c}$ from observables to generators. In the coefficient basis this is the elementary statement that the array of $\tilde R_\Psi$ is Hermitian iff the array of $-iH$ is anti-Hermitian; the biquaternion form names the two sectors that the statement relates, and places the generator in the material sector.

3. *The roots of $-1$ are separated by role.* The central roots $\pm i$ are the complex structure; the non-central roots $\vec u$ are rotor axes and rotation generators. A formulation that writes the Schrödinger equation with a quaternion unit destroys the first while leaving the second in place, and the counterexample above shows how. The biquaternion form keeps the two apart by construction.

**Honest bottom line.** For a field with four complex coefficients this is the standard equation of a Hermitian symbol on that carrier, and the algebra's only service is to hold the coefficients and to supply $i$. It is interesting because the same algebra also carries the Lorentz group and the Dirac equation, and because its two Hermitian fixed-point subspaces correspond to the physical and informational sectors of the wider proposal; but it produces no new prediction here. Whether it produces one in the many-body or relativistic setting is open.

## Open Questions

**1. The local complex structure.** The series makes the complex structure local: it is set by the medium through $c = 1/\sqrt{\epsilon\mu}$ and reduces to $i r'_t$ in vacuum. The scalar imaginary $i$ is a global central element of $\mathbb{B}$, and a central element cannot vary from point to point. Does the $i$ of the Schrödinger equation remain global, or does the carrier inherit a local complex structure from the medium? The relation between the two is unresolved.

**2. Many fields.** The extension to several fields is via $\mathbb{B}^{\otimes n}$, a complex algebra of dimension $2^{2n}$. The companion article leaves the tensor product over $\mathbb{C}$ as an open question. If it is taken over $\mathbb{C}$, the scalar imaginary remains available as the complex structure; if not, the question of the imaginary unit returns in a new form.

**3. Which of the four coefficients is physical.** The field has four complex coefficients and the equation treats them alike. Whether all four are physical, or whether three of them are a gauge artefact of the quaternionic structure, is not settled here. The polar companion article shows that three of them form the field's rotor, which precesses at $2|\vec r_\Psi|/\hbar$ and is therefore not removable by a phase.

**4. The non-relativistic limit.** Whether this Schrödinger equation is the precise non-relativistic limit of the biquaternion Dirac equation, or only an independent equation with the same symbol, is not checked here.

**5. Second quantization and the path integral.** The framework is first-quantized and has no path-integral form in this article; both are open in the parent.

## Summary

The Schrödinger equation in biquaternionic form is

$$
\boxed{\;i\hbar\,c\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}\;},
$$

with $\tilde R_\Psi = r_t\,e_t + i\vec r_\Psi \in \mathbb{B}_{\Psi}$ Hermitian, $\tilde{Ξ}_{\mathrm{sp}}$ one element of $\mathbb{B}$ with four complex coefficients, and $i$ the **scalar imaginary** — the central root of $-1$ in $\mathbb{B}$, unique up to sign.

The symbol $i$ must not be confused with the quaternion units or the non-central roots of $-1$, which are rotation axes, and it is not a complex structure on $\mathbb{B}_{\Psi}$, since $i\,\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi}$: the scalar imaginary is the canonical isomorphism between the two sectors, not an operator on either. The field is a general element of $\mathbb{B}$, not an element of $\mathbb{B}_{\Psi}$; the density matrix is recovered as $\tilde{Ϛ}_{\Psi} = \tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}/\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\tilde{Ξ}_{\mathrm{sp}}) \in \mathbb{B}_{\Psi}$, and the field equation implies the parent article's von Neumann equation $i\hbar\,c\partial/\partial r'_t\tilde{Ϛ}_{\Psi} = [H,\tilde{Ϛ}_{\Psi}]$.

Using a non-central root $\tilde{Ζ}$ in place of $i$ fails generically: the generator $-\frac{\tilde{Ζ}\tilde R_\Psi}{\hbar\,c}$ need not be anti-Hermitian, so the flow is not $*$-unitary and the norm is not preserved (explicitly for $\vec{Ζ} = \vec e_z$, $\tilde R_\Psi = i\vec e_x$). The scalar imaginary is the only choice, up to sign, that works for every Hermitian Hamiltonian.

Read in the two sectors, the equation says that the Hermitian observable $\tilde R_\Psi \in \mathbb{B}_{\Psi}$ generates, through the intertwiner $i$, a flow whose generator $-\frac{i\,\tilde R_\Psi}{\hbar\,c}$ lies in the material sector $\mathbb{B}_{\Phi}$. The equation is the standard complex-linear equation on four complex coefficients with a Hermitian symbol; the structural content is that the complex structure is supplied by the algebra, the observable/generator split is intrinsic to the Hermitian decomposition, and the roots of $-1$ are separated by role.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\mu^2 = -e_t$ |
| $i$ | Scalar imaginary, central, $i^2 = -e_t$ |
| $\hbar$ | Reduced Planck constant; the constant of the equation, $i\hbar\,c\,\partial/\partial r'_t\tilde\Xi=\tilde R_\Psi\tilde\Xi$ |
| $\mathbb{B}_{C}$ | Complex subspace $\operatorname{span}_{\mathbb{R}}\{e_t, ie_t\}$; the centre |
| $\mathbb{B}_{\Psi}$ | Hermitian subspace (observables): $i\hbar\,c\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}$ has $\tilde R_\Psi \in \mathbb{B}_{\Psi}$ |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian subspace (generators): the generator is $-\frac{i\,H}{\hbar\,c}\in\mathbb{B}_{\Phi}$ |
| $\mathbb{B}_{H}$ | Real quaternion subspace; home of the unit pure quaternions $\vec u$ |
| $\tilde R_\Psi = r_t\,e_t + i\vec r_\Psi$ | Hermitian element (Hamiltonian) |
| $\tilde{Ξ}_{\mathrm{sp}}$ | The field: one element of $\mathbb{B}$ |
| $L_{\tilde R_\Psi}$, $L_{\mathrm{axf}}(\tilde R_\Psi)$ | Left multiplication by $\tilde R_\Psi$; its $4\times4$ axis-free array in the coefficient basis |
| $\tilde{Ϛ}_{\Psi} = \tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}/\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\tilde{Ξ}_{\mathrm{sp}})$ | Density matrix associated to the field |
| $\tilde Q(r'_t) = \exp(-i\tilde R_\Psi r'_{t}/(\hbar\,c))$ | $*$-Unitary evolution, $\tilde{Ξ}_{\mathrm{sp}}(r'_t) = \tilde Q(r'_t)\tilde{Ξ}_{\mathrm{sp}}(0)$ |
| $\langle\tilde R_\Psi\rangle_{\tilde{Ξ}} = \mathrm{Sc}(\tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{\dagger})/\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{\dagger})$ | Mean of the observable in the field |
| $\vec e_\mu \vec e_\nu = \varepsilon_{\mu\nu\lambda}\vec e_\lambda$, $\mu \neq \nu$ | Quaternion multiplication |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |

## Further Reading

- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the original state-vector formulation.
- John von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton, 1932), for the density-matrix formulation and the von Neumann equation.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard two-component Schrödinger equation.
- Stephen L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford, 1995), for the quaternionic formulation in which a complex structure must be chosen.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the algebra $\mathbb{B}\cong M_2(\mathbb{C})$ and its representation theory, used here only as an external check.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of the Schrödinger equation.
