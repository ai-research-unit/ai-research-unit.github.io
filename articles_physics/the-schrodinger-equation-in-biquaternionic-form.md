# __The Schrödinger Equation in Biquaternionic Form__

## Introduction

For a pure state $|\tilde{Ξ}_{\mathrm{sp}}(r'_t)\rangle$ and a Hamiltonian $H$, the Schrödinger equation of standard quantum physics is

$$\frac{m\,c\,i}{k_m}\partial/\partial r'_t|\tilde{Ξ}_{\mathrm{sp}}(r'_t)\rangle  = H\,|\tilde{Ξ}_{\mathrm{sp}}(r'_t)\rangle,
$$

and for a density matrix $\rho$ the same dynamics reads $\frac{m\,c\,i}{k_m}\partial/\partial r'_t\rho = [H,\rho]$. Both statements have biquaternion forms, and it matters which of the two one has in hand.

The companion article *Quantum Physics in Biquaternionic Form* treats the second form: it exhibits the $*$-unitary biquaternion $\tilde Q(r'_t)$ obeying $\frac{m\,c\,i\,d\,\tilde{Q}}{k_m\,dr'_{t}}= \tilde R_\Psi\tilde Q$ and the state equation $\frac{m\,c\,i\,d\,\tilde{Ϛ}_{\Psi}}{k_m\,dr'_{t}}= [H,\tilde{Ϛ}_{\Psi}]$ for $\tilde{Ϛ}_{\Psi} \in \mathbb{B}_{\Psi}$. It does **not** write the state-vector equation $\frac{m\,c\,i}{k_m}\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}$, nor examine its symbol $i$. That is a difference of object rather than an oversight: the "states" of the framework are the elements of $\mathbb{B}_{\Psi}$, i.e. density-matrix-like objects, whereas a wave function is something else. This article supplies the state-vector form and settles what its $i$ denotes.

The question is not decorative. In and around the algebra $\mathbb{B}$ there are three distinct things commonly written with a symbol that squares to $-1$ or plays the role of $i$:

- the **scalar imaginary** $i$, which is central;
- the **quaternion units** $\vec e_x,\vec e_y,\vec e_z$ and, more generally, the non-central roots of $-1$ in $\mathbb{B}$;
- the **complex structure** that a state space must carry for the Schrödinger equation to be complex-linear.

The first two are different elements of the algebra; no conjugation relates them, and they play unrelated roles. The third is not an element of the algebra at all but a structure that the state space carries. Conflating them is the characteristic error, and it produces equations that look like the Schrödinger equation but do not preserve probability. Separating them is the substance of this article.

The article is organized as follows. The three objects are distinguished; the scalar imaginary is shown to exchange the sectors $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$; the wave function is identified as a spinor in a Peirce carrier, a minimal left ideal here, not as a generic element of $\mathbb{B}_{\Psi}$; the equation and its solution are written and checked; the non-central alternatives are tested and one is shown to fail; the $\mathbb{B}_{\Phi}$/$\mathbb{B}_{\Psi}$ interpretation is given. It closes with an honest account of what the form adds and what it merely relabels.

## Three Objects That Square to Minus One

### The scalar imaginary

The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with quaternion basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_\mu^2 = -e_t$ and $\vec e_\mu \vec e_\nu = \varepsilon_{\mu\nu\lambda}\vec e_\lambda$ for $\mu,\nu \in \{x,y,z\}$, $\mu \neq \nu$. The **scalar imaginary** $i$ is the image of the imaginary unit of the complexifying factor $\mathbb{C}$. It satisfies $i^2 = -e_t$ and is **central**: it commutes with every element of $\mathbb{B}$.

The central elements are exactly the complex scalars,

$$
\mathbb{B}_{C} = \{Q_t\,e_t : Q_t \in \mathbb{C}\} = \operatorname{span}_{\mathbb{R}}\{e_t, i\,e_t\},
$$

a copy of the complex line embedded as the scalar part, and it is the centre of $\mathbb{B}$. Within it the roots of $-1$ are exactly $\pm i$: the scalar imaginary is not "one root of $-1$ among many" but *the* central one.

### The quaternion units and the non-central roots

Each quaternion unit satisfies $\vec e_\mu^2 = -e_t$, but the $\vec e_\mu$ do not commute: $\vec e_x \vec e_y = \vec e_z = -\vec e_y \vec e_x$. They are non-central roots of $-1$. The companion article on biquaternion roots of minus one classifies all roots $\tilde{Ζ}$ with $\tilde{Ζ}^2 = -e_t$: either $\tilde{Ζ} = \pm i$ (the central roots), or $\tilde{Ζ} = \vec Q$ is a complex vector with $(\vec Q,\vec Q) := Q_x^2 + Q_y^2 + Q_z^2 = 1$ (the non-central roots). The real members of the second family are the **unit pure real quaternions** $\vec u \in \mathbb{B}_{H}$, with $|\vec u| = 1$, so $\vec u^2 = -e_t$ and $\vec u^\dagger = -\vec u \in \mathbb{B}_{\Phi}$. They are the points of the Bloch sphere, i.e. the directions of the state. Both $\vec u$ and $i$ square to $-e_t$ and are anti-Hermitian, but $i$ is central and $\vec u$ is not.

The two appear side by side in the idempotent

$$
\tilde\Pi_{1,2}(\vec u) = \tfrac{1}{2}\left(e_t \pm i\,\vec u\right),
$$

and this expression is precisely where the conflation happens. The $i$ is the central scalar imaginary; the $\vec u$ is the axis of the state. One is the complex structure, the other a direction of the state, and they must be read separately.

### The complex structure of the state space

A Schrödinger equation presupposes a complex vector space of states. In the biquaternion framework that space is a **minimal left ideal** $\mathbb{B}\tilde\Pi \subset \mathbb{B}$ — the module of states, defined in the next section — and its complex structure is left multiplication by the central $i$. Because $i$ is central, this action commutes with the left action of $\mathbb{B}$, so the module is genuinely complex-linear.

It is important that the complex structure does **not** live on $\mathbb{B}_{\Psi}$. Multiplication by $i$ is a real-linear isomorphism

$$
i\,\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi},
\qquad
i\,\mathbb{B}_{\Phi} = \mathbb{B}_{\Psi},
$$

so $i$ carries $\mathbb{B}_{\Psi}$ out of itself; it is not an operator on $\mathbb{B}_{\Psi}$. The phrase "the complex structure of $\mathbb{B}_{\Psi}$", if used at all, can only mean the complex structure of the state module: as a real vector space $\mathbb{B}_{\Psi}$ can be given some complex structure abstractly, but none is canonical, and multiplication by $i$ is not one. A reader is most likely to slip here, because the idempotent formula $\tfrac12(e_t + i\vec u)$ contains both an $i$ and an element of $\mathbb{B}_{\Psi}$; the $i$ does not act on $\mathbb{B}_{\Psi}$, it maps it to its complement.

| Object | Where it lives | Central? | Role |
|---|---|---|---|
| Scalar imaginary $i$ | $\mathbb{B}_{C}$, the centre | Yes | Complex structure of the state module; the $i$ of the Schrödinger equation |
| Quaternion units $\vec e_\mu$ | $\mathbb{B}_{H} \cap \mathbb{B}_{\Phi}$ (pure real) | No | Rotation generators, state axes |
| Non-central roots $\vec u$ | $\mathbb{B}_{H} \cap \mathbb{B}_{\Phi}$, unit sphere | No | Bloch-sphere axes; idempotent directions |
| Complex structure of the state module | Acts on $\mathbb{B}\tilde\Pi \cong \mathbb{C}^2$ | — | Left multiplication by the central $i$; not a structure on $\mathbb{B}_{\Psi}$ |

## The Scalar Imaginary Exchanges the Two Sectors

The relation $i\,\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi}$ is the algebraic content of the Hermitian decomposition, and it is the whole reason the scalar imaginary is the right unit for the Schrödinger equation. Concretely, for a Hermitian element $\tilde R_\Psi = r_t\,e_t + i\vec r_\Psi \in \mathbb{B}_{\Psi}$, using $\tilde R_\Psi^{*} = \tilde R_\Psi$, $i^{*} = -i$, and the centrality of $i$,

$$
(i\tilde R_\Psi)^{*} = \tilde R_\Psi^{*} i^{*} = \tilde R_\Psi\,(-i) = -i\tilde R_\Psi.
$$

So $i\tilde R_\Psi \in \mathbb{B}_{\Phi}$: the map $\tilde R_\Psi \mapsto i\tilde R_\Psi$ is a real-linear isomorphism $\mathbb{B}_{\Psi} \to \mathbb{B}_{\Phi}$ with inverse $\tilde{Q} \mapsto -i\tilde{Q}$, turning a Hermitian observable into an anti-Hermitian object. For example, with $\tilde R_\Psi = i\,\vec e_x$ (Hermitian, since $(i\vec e_x)^{*} = i\vec e_x$), one has $i\tilde R_\Psi = i\,(i\vec e_x) = -\vec e_x$, and $-\vec e_x$ is anti-Hermitian because $(-\vec e_x)^{*} = -(-\vec e_x)$. This is the elementary observation on which everything below rests.

## The Wave Function Is a Spinor in the State Module

### The state module

Under the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ with $e_t \mapsto I$, $\vec e_\mu \mapsto -i\sigma_\mu$ (the convention of the companion article), the idempotent

$$
\tilde\Pi = \tfrac{1}{2}\left(e_t + i\,\vec e_z\right) \;\longmapsto\; \tfrac{1}{2}(I + \sigma_3) = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = E_{11}
$$

is a rank-one projection. The **minimal left ideal**

$$
\mathbb{B}\tilde\Pi = \{\tilde{Q}\tilde\Pi : \tilde{Q} \in \mathbb{B}\}
$$

is the state module; in the matrix picture it is the space of matrices with only the first column nonzero, i.e. the column spinors $\mathbb{C}^2$. An element $\tilde{Ξ}_{\mathrm{sp}} \in \mathbb{B}\tilde\Pi$ is a **spinor**, characterized by $\tilde{Ξ}_{\mathrm{sp}}\tilde\Pi = \tilde{Ξ}_{\mathrm{sp}}$.

### Why the wave function is not a generic element of $\mathbb{B}_{\Psi}$

The temptation is to let the "state" $\tilde{Ϛ}_{\Psi} \in \mathbb{B}_{\Psi}$ of the companion article also serve as the wave function. The obstacle is not that the equation admits no $\mathbb{B}_{\Psi}$-valued solution — it does — but that $\mathbb{B}_{\Psi}$ is not stable under the action of the observables. $\mathbb{B}_{\Psi}$ is neither a subalgebra nor a left ideal of $\mathbb{B}$ (for example $(i\vec e_x)(i\vec e_y) = -\vec e_z \in \mathbb{B}_{\Phi}$), so for $\tilde{Ξ}_{\mathrm{sp}} \in \mathbb{B}_{\Psi}$ the product $\tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}$ need not lie in $\mathbb{B}_{\Psi}$, and the equation $\frac{m\,c\,i}{k_m}\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}$ does not define a flow on $\mathbb{B}_{\Psi}$.

That solutions can exist is expected, because both sides can meet in $\mathbb{B}_{\Phi}$: for $\tilde{Ξ}_{\mathrm{sp}} \in \mathbb{B}_{\Psi}$ the derivative $\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}}$ lies in the real vector space $\mathbb{B}_{\Psi}$, so $\frac{m\,c\,i}{k_m}\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} \in \mathbb{B}_{\Phi}$ at every instant, and $\tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}$ need not be Hermitian. Take $\tilde R_\Psi = i\,\vec e_x$ and

$$
\tilde{Ξ}_{\mathrm{sp}}(r'_t) = i\left(\cos\theta\,\vec e_y + \sin\theta\,\vec e_z\right), \qquad \theta =\frac{k_m\,r'_{t}}{m\,c}.
$$

Then $\tilde{Ξ}_{\mathrm{sp}}^{\dagger} = \tilde{Ξ}_{\mathrm{sp}}$, so $\tilde{Ξ}_{\mathrm{sp}}$ is Hermitian at every $r'_t$, and

$$\frac{m\,c\,i}{k_m}\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = \sin\theta\,\vec e_y - \cos\theta\,\vec e_z = (i\,\vec e_x)\,\tilde{Ξ}_{\mathrm{sp}},
$$

so the equation holds. The Hermitian-valued unknown is not inconsistent.

What disqualifies this $\tilde{Ξ}_{\mathrm{sp}}$ is not the equation but the requirement that a wave function be a state: $\langle \tilde{Ξ}_{\mathrm{sp}}\rangle_{\natural} = \tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{\natural} = -e_t$, so $\tilde{Ξ}_{\mathrm{sp}}$ is invertible and in particular not a zero divisor. A wave function in the state module satisfies $\tilde{Ξ}_{\mathrm{sp}}\tilde\Pi = \tilde{Ξ}_{\mathrm{sp}}$, hence $\tilde{Ξ}_{\mathrm{sp}}(e_t - \tilde\Pi) = 0$ with $e_t - \tilde\Pi \neq 0$: every nonzero element of $\mathbb{B}\tilde\Pi$ is a zero divisor. (The idempotent $\tilde\Pi_+ = \tfrac{1}{2}(e_t + i\vec e_z)$ — which is $\tilde\Pi$ itself — is an element of $\mathbb{B}_{\Psi}$ that does lie in the state module; a generic Hermitian element does not. Membership in $\mathbb{B}\tilde\Pi$ does not follow from being a zero divisor: $\tilde\Pi_- = \tfrac{1}{2}(e_t - i\vec e_z)$ is a zero divisor too, and $\tilde{Q}\tilde\Pi = \tilde\Pi_-$ would give $\tilde\Pi_- = \tilde\Pi_-\tilde\Pi = 0$, impossible.) The correct exclusion is therefore structural — $\mathbb{B}_{\Psi}$ is not a left ideal, and its elements need not be zero divisors — not the absence of solutions. Here $i\vec e_z$ is a root of $+1$, $(i\vec e_z)^2=e_t$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents.

The correct relation between the two kinds of state is bilinear. From $\tilde{Ξ}_{\mathrm{sp}} \in \mathbb{B}\tilde\Pi$ one forms

$$
\tilde{Ϛ}_{\Psi} = \frac{\tilde{Ξ}_{\mathrm{sp}}\,\tilde{Ξ}_{\mathrm{sp}}^{\dagger}}{\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\tilde{Ξ}_{\mathrm{sp}})} \in \mathbb{B}_{\Psi},
$$

which is Hermitian, positive, and trace one — an element of the Bloch ball, hence a state in the sense of the companion article. The wave function and the density matrix are not the same object; they are related by $\tilde{Ξ}_{\mathrm{sp}} \mapsto \tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$, and the same element $i$ acts as complex structure on the spinor while exchanging the sectors in which the operator is expressed.

## The Schrödinger Equation and Its Solution

With these objects separated, the equation reads

$$
\boxed{\;\frac{m\,c\,i}{k_m}\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}}(r'_t) = \tilde R_\Psi\,\tilde{Ξ}_{\mathrm{sp}}(r'_t),
\qquad
\tilde R_\Psi = r_t\,e_t + i\vec r_\Psi \in  \mathbb{B}_{\Psi},
\qquad
\tilde{Ξ}_{\mathrm{sp}}(r'_t) \in  \mathbb{B}\tilde\Pi\;},
$$

where $i$ is the scalar imaginary. Because $i$ is central, $i\tilde R_\psii$, and there is no left/right ordering ambiguity in the equation. Because $\mathbb{B}\tilde\Pi$ is a left ideal, $\tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}} \in \mathbb{B}\tilde\Pi$, so the equation is consistent within the module.

**Solution.** Since $-i\tilde R_\Psi = -i r_t\,e_t + \vec r_\Psi$ and the scalar and vector parts commute,

$$
\boxed{\;\tilde Q(r'_t) = \exp\!\left(-\frac{k_m\,i\,Hr'_{t}}{m\,c}\right)
= \exp(-\frac{k_m\,i\,r_{t}\,r'_{t}}{m})\left(\cos\theta\,e_t + \sin\theta\,\vec u_\Psi\right),
\qquad
\theta =\frac{|\vec r_\Psi|r'_t}{\frac{m\,c}{k_m}}\;},
$$

and $\tilde{Ξ}_{\mathrm{sp}}(r'_t) = \tilde Q(r'_t)\tilde{Ξ}_{\mathrm{sp}}(0)$. The element $\tilde Q$ is $*$-unitary, $\tilde Q\tilde Q^{*} = e_t$: the central phase cancels and $R = \cos\theta\,e_t + \sin\theta\,\vec u_\Psi$ is a unit real quaternion, $R R^{*} = e_t$. Consequently the Hermitian norm $\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\tilde{Ξ}_{\mathrm{sp}})$ is preserved: with $\tilde{Ξ}_{\mathrm{sp}}(r'_t) = \tilde Q\tilde{Ξ}_{\mathrm{sp}}(0)$,

$$
\mathrm{Tr}\!\left(\tilde{Ξ}_{\mathrm{sp}}(r'_t)^\dagger\tilde{Ξ}_{\mathrm{sp}}(r'_t)\right)
= \mathrm{Tr}\!\left(\tilde{Ξ}_{\mathrm{sp}}(0)^\dagger \tilde Q^{*}\tilde Q\,\tilde{Ξ}_{\mathrm{sp}}(0)\right)
= \mathrm{Tr}\!\left(\tilde{Ξ}_{\mathrm{sp}}(0)^\dagger\tilde{Ξ}_{\mathrm{sp}}(0)\right).
$$

Differentiating the solution gives $\frac{m\,c\,i}{k_m}\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} =\frac{m\,c\,i}{k_m}(-\frac{k_m\,i\,H}{m\,c})\tilde{Ξ}_{\mathrm{sp}} = \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}$, so it is the required solution.

**Case checked.** For $\tilde R_\Psi = i\,\vec e_x$ one has $r_t = 0$, $\vec r_\Psi = \vec e_x$, and $\tilde Q(r'_t) = \cos(\frac{k_m\,r'_{t}}{m\,c})e_t + \sin(\frac{k_m\,r'_{t}}{m\,c})\vec e_x$. Then $\tilde Q(r'_t)$ is $*$-unitary, and $\tilde R_\Psi\tilde Q = i \vec e_x(\cos(\frac{k_m\,r'_{t}}{m\,c})e_t + \sin(\frac{k_m\,r'_{t}}{m\,c})\vec e_x) = i\cos(\frac{k_m\,r'_{t}}{m\,c})\vec e_x - i\sin(\frac{k_m\,r'_{t}}{m\,c})e_t$ equals $\frac{m\,c\,i\,d\,\tilde{Q}}{k_m\,dr'_{t}}= i(-\sin(\frac{k_m\,r'_{t}}{m\,c})e_t + \cos(\frac{k_m\,r'_{t}}{m\,c})\vec e_x)$, term by term. This case was chosen independently of the general formula and confirms it.

**Consistency with the density matrix.** The companion article's equation for $\tilde{Ϛ}_{\Psi} = \tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$ follows from the spinor equation. Differentiating $\tilde{Ϛ}_{\Psi} = \tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$ and using $\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = -\frac{k_m\,i\,\tilde{R}_{\Psi}\,\tilde{Ξ}_{\mathrm{sp}}}{m\,c}$, $\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}}^{\dagger} =\frac{k_m\,i\,\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\,\tilde{R}_{\Psi}}{m\,c}$ (valid because $\tilde R_\Psi^{*} = \tilde R_\Psi$) gives

$$
\boxed{\;\partial/\partial r'_t\tilde{Ϛ}_{\Psi} = -\frac{k_m\,i}{m\,c}\tilde R_\Psi\tilde{Ϛ}_{\Psi} +\frac{k_m\,i}{m\,c}\tilde{Ϛ}_{\Psi}\tilde R_\Psi
= -\frac{k_m\,i}{m\,c}[H,\tilde{Ϛ}_{\Psi}],
\qquad\text{i.e.}\qquad\frac{m\,c\,i}{k_m}\partial/\partial r'_t\tilde{Ϛ}_{\Psi} = [H,\tilde{Ϛ}_{\Psi}]\;},
$$

which is the von Neumann equation of the parent article. The Born rule follows as there: with $\tilde{Ϛ}_{\Psi} = \tfrac12(e_t + i\vec r)$ and $\tilde\Pi_1(\vec u) = \tfrac12(e_t + i\vec u)$,

$$
p_+ = \frac{\langle\tilde\Pi_1(\vec u),\tilde{Ϛ}_{\Psi}\rangle_{*}}{\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}} = \frac{\mathrm{Sc}(\tilde\Pi_1(\vec u)\tilde{Ϛ}_{\Psi}^{*})}{\mathrm{Sc}(\tilde{Ϛ}_{\Psi})} = \frac{\mathrm{Sc}(\tilde\Pi_1(\vec u)\tilde{Ϛ}_{\Psi})}{\mathrm{Sc}(\tilde{Ϛ}_{\Psi})} = \frac{\operatorname{Tr}(\tilde\Pi_1(\vec u)\tilde{Ϛ}_{\Psi})}{\operatorname{Tr}(\tilde{Ϛ}_{\Psi})} = \tfrac12\left(1 + \vec u\cdot\vec r\right).
$$

For the up-state spinor $\tilde{Ξ}_{\mathrm{sp}} = \begin{pmatrix} 1 \\ 0\end{pmatrix}$ one has $\vec r = \vec e_z$, and $p_+ = \tfrac12(1 + \vec u\cdot \vec e_z)$, the standard result.

## Why the Scalar Imaginary, and Not a Quaternion Unit

It is worth making precise why the obvious alternatives to $i$ fail. Suppose a root $\tilde{Ζ}$ with $\tilde{Ζ}^2 = -1$ is used in place of $i$:

$$\frac{m\,c\,\tilde{Ζ}}{k_m}\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}
\qquad\Longrightarrow\qquad
\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = -\frac{k_m}{m\,c}\tilde{Ζ}\tilde R_\Psi\,\tilde{Ξ}_{\mathrm{sp}},
$$

so the generator of the flow is $-\frac{k_m\,\tilde{Ζ}\,\tilde{R}_{\Psi}}{m\,c}$. The flow preserves the Hermitian form, i.e. $\exp(-\frac{k_m\,r'_{t}\,\tilde{Ζ}\,\tilde{R}_{\Psi}}{m\,c})$ is $*$-unitary, exactly when $-\frac{k_m\,\tilde{Ζ}\,\tilde{R}_{\Psi}}{m\,c}$ is anti-Hermitian, which is the condition

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

using $\vec e_z \vec e_x = \vec e_y$. Since $i\,\vec e_y$ is Hermitian, $(i\vec e_y)^{*} = i\vec e_y$, the generator $-\frac{k_m\,\vec Ζ\,\tilde{R}_{\Psi}}{m\,c}= -\frac{k_m\,i\,\vec e_{y}}{m\,c}$ is Hermitian, not anti-Hermitian, and $\exp(-\frac{k_m\,r'_{t}\,\vec Ζ\,\tilde{R}_{\Psi}}{m\,c})$ is not $*$-unitary. Explicitly, at $r'_t =\frac{m\,c\,\pi}{2\,k_m}$,

$$
\tilde Q^{*}\tilde Q = \exp\!\left(-i\pi \vec e_y\right)
= \cosh(\pi)\,e_t - i\sinh(\pi)\,\vec e_y \neq e_t,
$$

so the norm is not preserved by this "Schrödinger equation". The failure is generic: a non-central $\vec{Ζ}$ fails as soon as $\tilde R_\Psi$ does not commute with it.

There is a second defect in the non-central choice: because $\vec e_z \vec e_x = \vec e_y$ while $\vec e_x \vec e_z = -\vec e_y$, the elements $\vec e_z\tilde{Ξ}_{\mathrm{sp}}$ and $\tilde{Ξ}_{\mathrm{sp}} \vec e_z$ differ, so the left- and right-handed interpretations of "the same" equation produce opposite generators. The centrality of $i$ removes this ambiguity.

**A caveat, stated honestly.** A non-central $\tilde{Ζ}$ is not always inadmissible: if a particular $\tilde R_\Psi$ commutes with $\tilde{Ζ}$, then $\tilde{Ζ}\tilde R_\Psi$ can be anti-Hermitian and the flow $*$-unitary on that sector (for instance $\tilde R_\Psi = i\,\vec e_z$ and $\vec{Ζ} = \vec e_z$, giving $\vec{Ζ}\tilde R_\Psi = -ie_t$). What fails is uniformity, and a unit that works only for Hamiltonians aligned with a preferred direction is not a unit for the Schrödinger equation.

## The $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ Readings of the Equation

The equation can be rearranged into a statement that lives entirely in one sector at a time. Dividing by $\frac{m\,c\,i}{k_m}$,

$$
\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = -\frac{k_m\,i}{m\,c}\tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}},
\qquad
-\frac{k_m\,i}{m\,c}\tilde R_\Psi =\frac{\vec r_\Psi - i r_t e_t}{\frac{m\,c}{k_m}} \in  \mathbb{B}_{\Phi}.
$$

The generator $-\frac{k_m\,i\,H}{m\,c}$ is anti-Hermitian; this is the general reason the exponential is $*$-unitary. The two interpretations are then:

- **$\mathbb{B}_{\Psi}$ interpretation.** The Hamiltonian $\tilde R_\Psi \in \mathbb{B}_{\Psi}$ is a Hermitian observable — an energy. The equation says that the dynamics is generated by that observable, read through the intertwiner $i$.
- **$\mathbb{B}_{\Phi}$ interpretation.** The generator $-\frac{k_m\,i\,H}{m\,c\,\in\,\mathbb{B}}_{\Phi}$ lies in the *material* sector, the same four-dimensional real space that carries the four-vectors of relativistic physics. The time-translation generator is an element of that sector; multiplying it by $\frac{m\,c\,i}{k_m}$ returns the Hermitian observable $\tilde R_\Psi$.

In the von Neumann form the split is even cleaner. For $\tilde R_\Psi, \tilde{Ϛ}_{\Psi} \in \mathbb{B}_{\Psi}$,

$$
\left([H,\tilde{Ϛ}_{\Psi}]\right)^\dagger = \tilde{Ϛ}_{\Psi}\tilde R_\Psi - \tilde R_\Psi\tilde{Ϛ}_{\Psi} = -[H,\tilde{Ϛ}_{\Psi}],
$$

so $[H,\tilde{Ϛ}_{\Psi}] \in \mathbb{B}_{\Phi}$; and since $\tilde{Ϛ}_{\Psi} \in \mathbb{B}_{\Psi}$ and $i\,\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi}$, the term $\frac{m\,c\,i}{k_m}\partial/\partial r'_t\tilde{Ϛ}_{\Psi}$ is also in $\mathbb{B}_{\Phi}$. The von Neumann equation is thus an identity in a single sector, while its solution returns to the complementary one.

A structural caution belongs here. The wave function $\tilde{Ξ}_{\mathrm{sp}}$ itself is an element of the state module $\mathbb{B}\tilde\Pi$, not of either sector; it carries no $\mathbb{B}_{\Psi}/\mathbb{B}_{\Phi}$ label. The decomposition $\mathbb{B} = \mathbb{B}_{\Psi} \oplus \mathbb{B}_{\Phi}$ classifies Hermitian observables and anti-Hermitian generators, not state vectors. What returns to $\mathbb{B}_{\Psi}$ is the bilinear object $\tilde{Ϛ}_{\Psi} = \tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$, not $\tilde{Ξ}_{\mathrm{sp}}$. Reading the sector labels onto the wave function is the same error as conflating the wave function with the density matrix.

## What the Biquaternion Form Adds and What It Merely Relabels

**The relabelling.** Under $\mathbb{B} \cong M_2(\mathbb{C})$ with $\vec e_\mu \mapsto -i\sigma_\mu$, a spinor in $\mathbb{B}\tilde\Pi$ is a column vector in $\mathbb{C}^2$, the scalar imaginary is the standard imaginary unit, $\tilde Q(r'_t)$ is a standard element of $\mathrm{U}(2)$, and the equation is literally the two-component Schrödinger equation. Nothing is added for a single qubit beyond vocabulary: the biquaternion equation predicts exactly what the standard one predicts.

**What is structural.** Three features are genuinely rearranged rather than merely renamed.

1. *The complex structure is supplied, not chosen.* Since $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ contains the central element $i$ by construction, the complex structure of the state module is fixed by the algebra. In a purely quaternionic formulation — wave functions valued in $\mathbb{H}$, with no complexifying factor — there is no central imaginary unit, and one must *choose* a complex structure on the state space, so the choice becomes extra input. Here the algebra supplies it, and the quaternion units, being non-central, are not candidates. This is definitional — $\mathbb{C}$ was put into $\mathbb{B}$ by fiat — but the content is that the same algebra contains both the quaternion units and the central root of $-1$, unique up to sign, that quantum physics requires.

2. *The observable/generator split is intrinsic.* $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ are the fixed-point subspaces of Hermitian conjugation, and $i$ is the canonical real-linear isomorphism relating them. The Schrödinger equation is exactly the map $\tilde R_\Psi \mapsto  -\frac{k_m\,i\,H}{m\,c}$ from observables to generators. In $M_2(\mathbb{C})$ language this is the elementary statement that $\tilde R_\Psi$ is Hermitian iff $-i H$ is anti-Hermitian; the biquaternion form names the two sectors that the statement relates, and places the generator in the material sector.

3. *The roots of $-1$ are separated by role.* The central roots $\pm i$ are the complex structure; the non-central roots $\vec u$ are state axes and rotation generators. A formulation that writes the Schrödinger equation with a quaternion unit destroys the first while leaving the second in place, and the counterexample above shows how. The biquaternion form keeps the two apart by construction.

**Honest bottom line.** For a single qubit this is a rewriting of a known equation. It is interesting because the same algebra also carries the Lorentz group and the Dirac equation, and because its two Hermitian fixed-point subspaces correspond to the physical and informational sectors of the wider proposal; but it produces no new prediction here. Whether it produces one in the many-body or relativistic setting is open.

## Open Questions

**1. The local complex structure.** The series makes the complex structure local: it is set by the medium through $c = 1/\sqrt{\epsilon\mu}$ and reduces to $i r'_t$ in vacuum. The scalar imaginary $i$ is a global central element of $\mathbb{B}$, and a central element cannot vary from point to point. Does the $i$ of the Schrödinger equation remain global, or does a local complex structure enter the state module? The relation between the two is unresolved.

**2. Many qubits.** The extension to $n$ qubits is via $\mathbb{B}^{\otimes n} \cong M_{2^n}(\mathbb{C})$. The companion article leaves the tensor product over $\mathbb{C}$ as an open question. If it is taken over $\mathbb{C}$, the scalar imaginary remains available as the complex structure; if not, the question of the imaginary unit returns in a new form.

**3. Dependence on the choice of minimal left ideal.** The choice $\tilde\Pi = \tfrac12(e_t + i\vec e_z)$ is a choice of the state axis. Different minimal left ideals are unitarily equivalent, so the physics should be independent of it, but this article has not argued that explicitly; it should be stated as a basis choice.

**4. The non-relativistic limit.** Whether this Schrödinger equation is the precise non-relativistic limit of the biquaternion Dirac equation, or only an independent qubit equation, is not checked here.

**5. Second quantization and the path integral.** The framework is first-quantized and has no path-integral form in this article; both are open in the parent.

## Summary

The Schrödinger equation in biquaternionic form is

$$
\boxed{\;\frac{m\,c\,i}{k_m}\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}\;},
$$

with $\tilde R_\Psi = r_t\,e_t + i\vec r_\Psi \in \mathbb{B}_{\Psi}$ Hermitian, $\tilde{Ξ}_{\mathrm{sp}}$ a spinor in the Peirce carrier $\mathbb{B}\tilde\Pi \cong \mathbb{C}^2$, a minimal left ideal here, and $i$ the **scalar imaginary** — the central root of $-1$ in $\mathbb{B}$, unique up to sign.

The symbol $i$ must not be confused with the quaternion units or the non-central roots of $-1$, which are rotation axes, and it is not a complex structure on $\mathbb{B}_{\Psi}$, since $i\,\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi}$: the scalar imaginary is the canonical isomorphism between the two sectors, not an operator on either. The wave function is a spinor in the state module, not a generic element of $\mathbb{B}_{\Psi}$; the density matrix is recovered as $\tilde{Ϛ}_{\Psi} = \tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}/\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\tilde{Ξ}_{\mathrm{sp}}) \in \mathbb{B}_{\Psi}$, and the spinor equation implies the parent article's von Neumann equation $\frac{m\,c\,i}{k_m}\partial/\partial r'_t\tilde{Ϛ}_{\Psi} = [H,\tilde{Ϛ}_{\Psi}]$.

Using a non-central root $\tilde{Ζ}$ in place of $i$ fails generically: the generator $-\frac{k_m\,\tilde{Ζ}\,\tilde{R}_{\Psi}}{m\,c}$ need not be anti-Hermitian, so the flow is not $*$-unitary and the norm is not preserved (explicitly for $\vec{Ζ} = \vec e_z$, $\tilde R_\Psi = i\vec e_x$). The scalar imaginary is the only choice, up to sign, that works for every Hermitian Hamiltonian.

Read in the two sectors, the equation says that the Hermitian observable $\tilde R_\Psi \in \mathbb{B}_{\Psi}$ generates, through the intertwiner $i$, a flow whose generator $-\frac{k_m\,i\,H}{m\,c}$ lies in the material sector $\mathbb{B}_{\Phi}$. For a single qubit this is a rewriting of the standard two-component equation; the structural content is that the complex structure is supplied by the algebra, the observable/generator split is intrinsic to the Hermitian decomposition, and the roots of $-1$ are separated by role.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\mu^2 = -e_t$ |
| $i$ | Scalar imaginary, central, $i^2 = -e_t$ |
| $\mathbb{B}_{C}$ | Complex subspace $\operatorname{span}_{\mathbb{R}}\{e_t, ie_t\}$; the centre |
| $\mathbb{B}_{\Psi}$ | Hermitian subspace (observables): $\frac{m\,c\,i}{k_m}\partial/\partial r'_t\tilde{Ξ}_{\mathrm{sp}} = \tilde R_\Psi\tilde{Ξ}_{\mathrm{sp}}$ has $\tilde R_\Psi \in \mathbb{B}_{\Psi}$ |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian subspace (generators): the generator is $-\frac{k_m\,i\,H}{m\,c\,\in\,\mathbb{B}}_{\Phi}$ |
| $\mathbb{B}_{H}$ | Real quaternion subspace; home of the unit pure quaternions $\vec u$ |
| $\tilde R_\Psi = r_t\,e_t + i\vec r_\Psi$ | Hermitian element (Hamiltonian) |
| $\tilde\Pi_{1,2}(\vec u) = \tfrac12(e_t \pm i\vec u)$ | Idempotent (pure state); $\vec u$ the state axis |
| $\mathbb{B}\tilde\Pi \cong \mathbb{C}^2$ | Minimal left ideal: the state module of spinors $\tilde{Ξ}_{\mathrm{sp}}$ |
| $\tilde{Ϛ}_{\Psi} = \tilde{Ξ}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}/\mathrm{Tr}(\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\tilde{Ξ}_{\mathrm{sp}})$ | Density matrix associated to a spinor |
| $\tilde Q(r'_t) = \exp(-\frac{k_m\,i\,Hr'_{t}}{m\,c})$ | $*$-Unitary evolution, $\tilde{Ξ}_{\mathrm{sp}}(r'_t) = \tilde Q(r'_t)\tilde{Ξ}_{\mathrm{sp}}(0)$ |
| $2\,\mathrm{Sc}(\tilde\Pi_1(\vec u)\tilde R_\Psi^{*}) = r_t + \vec u\cdot\vec r_\Psi = \operatorname{Tr}(\tilde\Pi_1(\vec u)\tilde R_\Psi^{*})$ | Trace reading last / Born rule |
| $\vec e_\mu \vec e_\nu = \varepsilon_{\mu\nu\lambda}\vec e_\lambda$, $\mu \neq \nu$ | Quaternion multiplication |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |

## Further Reading

- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the original state-vector formulation.
- John von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton, 1932), for the density-matrix formulation and the von Neumann equation.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard two-component Schrödinger equation.
- Stephen L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford, 1995), for the quaternionic formulation in which a complex structure must be chosen.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the algebra of $\mathbb{B}$ and its minimal left ideals.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of spinors and the Schrödinger equation.
