# __The Schrödinger Equation in Biquaternionic Form__

## Introduction

For a pure state $|\psi(t)\rangle$ and a Hamiltonian $H$, the Schrödinger equation of standard quantum mechanics is

$$
i\hbar\,\partial_t|\psi(t)\rangle = H\,|\psi(t)\rangle,
$$

and for a density matrix $\rho$ the same dynamics reads $i\hbar\,\partial_t\rho = [H,\rho]$. Both statements have biquaternion forms, and it matters which of the two one has in hand.

The companion article *Quantum Mechanics in Biquaternionic Form* treats the second form: it exhibits the unitary biquaternion $\tilde{U}(t)$ obeying $i\hbar\,d\tilde{U}/dt = \tilde{H}\tilde{U}$ and the state equation $i\hbar\,d\tilde{\rho}/dt = [\tilde{H},\tilde{\rho}]$ for $\tilde{\rho} \in \mathbb{M}_+$. It does **not** write the state-vector equation $i\hbar\,\partial_t\psi = \tilde{H}\psi$, nor examine its symbol $i$. That is a difference of object rather than an oversight: the "states" of the framework are the elements of $\mathbb{M}_+$, i.e. density-matrix-like objects, whereas a wave function is something else. This article supplies the state-vector form and settles what its $i$ denotes.

The question is not decorative. In and around the algebra $\mathbb{B}$ there are three distinct things commonly written with a symbol that squares to $-1$ or plays the role of $i$:

- the **scalar imaginary** $i$, which is central;
- the **quaternion units** $e_1,e_2,e_3$ and, more generally, the non-central roots of $-1$ in $\mathbb{B}$;
- the **complex structure** that a state space must carry for the Schrödinger equation to be complex-linear.

The first two are different elements of the algebra; no conjugation relates them, and they play unrelated roles. The third is not an element of the algebra at all but a structure that the state space carries. Conflating them is the characteristic error, and it produces equations that look like the Schrödinger equation but do not preserve probability. Separating them is the substance of this article.

The article is organized as follows. The three objects are distinguished; the scalar imaginary is shown to exchange the sectors $\mathbb{M}_\pm$; the wave function is identified as a spinor in a minimal left ideal, not as a generic element of $\mathbb{M}_+$; the equation and its solution are written and checked; the non-central alternatives are tested and one is shown to fail; the $\mathbb{M}_-$/$\mathbb{M}_+$ reading is given. It closes with an honest account of what the form adds and what it merely relabels.

## Three Objects That Square to Minus One

### The scalar imaginary

The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_j^2 = -e_0$ and $e_je_k = \varepsilon_{jkl}e_l$ for $j,k \in \{1,2,3\}$, $j \neq k$. The **scalar imaginary** $i$ is the image of the imaginary unit of the complexifying factor $\mathbb{C}$. It satisfies $i^2 = -e_0$ and is **central**: it commutes with every element of $\mathbb{B}$.

The central elements are exactly the complex scalars,

$$
\mathbb{C}_{\mathbb{B}} = \{Q_0\,e_0 : Q_0 \in \mathbb{C}\} = \operatorname{span}_{\mathbb{R}}\{e_0, i\,e_0\},
$$

a copy of the complex line embedded as the scalar part, and it is the center of $\mathbb{B}$. Within it the roots of $-1$ are exactly $\pm i$: the scalar imaginary is not "one root of $-1$ among many" but *the* central one.

### The quaternion units and the non-central roots

Each quaternion unit satisfies $e_j^2 = -e_0$, but the $e_j$ do not commute: $e_1e_2 = e_3 = -e_2e_1$. They are non-central roots of $-1$. The companion article on biquaternion roots of minus one classifies all roots $\xi$ with $\xi^2 = -e_0$: either $\xi = \pm i$ (the central roots), or $\xi = \mathbf{X}$ is a complex vector with $(X,X) := Q_1^2 + Q_2^2 + Q_3^2 = 1$ (the non-central roots). The real members of the second family are the **unit pure real quaternions** $\hat{\mu} \in \mathbb{H}_{\mathbb{B}}$, with $|\hat{\mu}| = 1$, so $\hat{\mu}^2 = -e_0$ and $\hat{\mu}^\dagger = -\hat{\mu} \in \mathbb{M}_-$. They are the points of the Bloch sphere, i.e. the directions of the state. Both $\hat{\mu}$ and $i$ square to $-e_0$ and are anti-Hermitian, but $i$ is central and $\hat{\mu}$ is not.

The two appear side by side in the idempotent

$$
\tilde{P}_\pm(\hat{\mu}) = \tfrac{1}{2}\left(e_0 \pm i\,\hat{\mu}\right),
$$

and this expression is precisely where the conflation happens. The $i$ is the central scalar imaginary; the $\hat{\mu}$ is the axis of the state. One is the complex structure, the other a direction of the state, and they must be read separately.

### The complex structure of the state space

A Schrödinger equation presupposes a complex vector space of states. In the biquaternion framework that space is a **minimal left ideal** $\mathbb{B}\tilde{P} \subset \mathbb{B}$ — the module of states, defined in the next section — and its complex structure is left multiplication by the central $i$. Because $i$ is central, this action commutes with the left action of $\mathbb{B}$, so the module is genuinely complex-linear.

It is important that the complex structure does **not** live on $\mathbb{M}_+$. Multiplication by $i$ is a real-linear isomorphism

$$
i\,\mathbb{M}_+ = \mathbb{M}_-,
\qquad
i\,\mathbb{M}_- = \mathbb{M}_+,
$$

so $i$ carries $\mathbb{M}_+$ out of itself; it is not an operator on $\mathbb{M}_+$. The phrase "the complex structure of $\mathbb{M}_+$", if used at all, can only mean the complex structure of the state module: as a real vector space $\mathbb{M}_+$ can be given some complex structure abstractly, but none is canonical, and multiplication by $i$ is not one. A reader is most likely to slip here, because the idempotent formula $\tfrac12(e_0 + i\hat{\mu})$ contains both an $i$ and an element of $\mathbb{M}_+$; the $i$ does not act on $\mathbb{M}_+$, it maps it to its complement.

| Object | Where it lives | Central? | Role |
|---|---|---|---|
| Scalar imaginary $i$ | $\mathbb{C}_{\mathbb{B}}$, the center | Yes | Complex structure of the state module; the $i$ of the Schrödinger equation |
| Quaternion units $e_j$ | $\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ (pure real) | No | Rotation generators, state axes |
| Non-central roots $\hat{\mu}$ | $\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$, unit sphere | No | Bloch-sphere axes; idempotent directions |
| Complex structure of the state module | Acts on $\mathbb{B}\tilde{P} \cong \mathbb{C}^2$ | — | Left multiplication by the central $i$; not a structure on $\mathbb{M}_+$ |

## The Scalar Imaginary Exchanges the Two Sectors

The relation $i\,\mathbb{M}_+ = \mathbb{M}_-$ is the algebraic content of the Hermitian decomposition, and it is the whole reason the scalar imaginary is the right unit for the Schrödinger equation. Concretely, for a Hermitian element $\tilde{H} = h_0e_0 + i\mathbf{h} \in \mathbb{M}_+$, using $\tilde{H}^\dagger = \tilde{H}$, $i^\dagger = -i$, and the centrality of $i$,

$$
(i\tilde{H})^\dagger = \tilde{H}^\dagger i^\dagger = \tilde{H}\,(-i) = -i\tilde{H}.
$$

So $i\tilde{H} \in \mathbb{M}_-$: the map $\tilde{H} \mapsto i\tilde{H}$ is a real-linear isomorphism $\mathbb{M}_+ \to \mathbb{M}_-$ with inverse $\tilde{K} \mapsto -i\tilde{K}$, turning a Hermitian observable into an anti-Hermitian object. For example, with $\tilde{H} = i\,e_1$ (Hermitian, since $(ie_1)^\dagger = ie_1$), one has $i\tilde{H} = i\,(ie_1) = -e_1$, and $-e_1$ is anti-Hermitian because $(-e_1)^\dagger = -(-e_1)$. This is the elementary observation on which everything below rests.

## The Wave Function Is a Spinor in the State Module

### The state module

Under the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ with $e_0 \mapsto I$, $e_j \mapsto -i\sigma_j$ (the convention of the companion article), the idempotent

$$
\tilde{P} = \tfrac{1}{2}\left(e_0 + i\,e_3\right) \;\longmapsto\; \tfrac{1}{2}(I + \sigma_3) = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = E_{11}
$$

is a rank-one projection. The **minimal left ideal**

$$
\mathbb{B}\tilde{P} = \{\tilde{\chi}\tilde{P} : \tilde{\chi} \in \mathbb{B}\}
$$

is the state module; in the matrix picture it is the space of matrices with only the first column nonzero, i.e. the column spinors $\mathbb{C}^2$. An element $\psi \in \mathbb{B}\tilde{P}$ is a **spinor**, characterized by $\psi\tilde{P} = \psi$.

### Why the wave function is not a generic element of $\mathbb{M}_+$

The temptation is to let the "state" $\tilde{\rho} \in \mathbb{M}_+$ of the companion article also serve as the wave function. The obstacle is not that the equation admits no $\mathbb{M}_+$-valued solution — it does — but that $\mathbb{M}_+$ is not stable under the action of the observables. $\mathbb{M}_+$ is neither a subalgebra nor a left ideal of $\mathbb{B}$ (for example $(ie_1)(ie_2) = -e_3 \in \mathbb{M}_-$), so for $\psi \in \mathbb{M}_+$ the product $\tilde{H}\psi$ need not lie in $\mathbb{M}_+$, and the equation $i\hbar\,\partial_t\psi = \tilde{H}\psi$ does not define a flow on $\mathbb{M}_+$.

That solutions can exist is expected, because both sides can meet in $\mathbb{M}_-$: for $\psi \in \mathbb{M}_+$ the derivative $\partial_t\psi$ lies in the real vector space $\mathbb{M}_+$, so $i\hbar\,\partial_t\psi \in \mathbb{M}_-$ at every instant, and $\tilde{H}\psi$ need not be Hermitian. Take $\tilde{H} = i\,e_1$ and

$$
\psi(t) = i\left(\cos\theta\,e_2 + \sin\theta\,e_3\right), \qquad \theta = \frac{t}{\hbar}.
$$

Then $\psi^\dagger = \psi$, so $\psi$ is Hermitian at every $t$, and

$$
i\hbar\,\partial_t\psi = \sin\theta\,e_2 - \cos\theta\,e_3 = (i\,e_1)\,\psi,
$$

so the equation holds. The Hermitian-valued unknown is not inconsistent.

What disqualifies this $\psi$ is not the equation but the requirement that a wave function be a state: $N(\psi) = \psi\bar{\psi} = -e_0$, so $\psi$ is invertible and in particular not a zero divisor. A wave function in the state module satisfies $\psi\tilde{P} = \psi$, hence $\psi(e_0 - \tilde{P}) = 0$ with $e_0 - \tilde{P} \neq 0$: every nonzero element of $\mathbb{B}\tilde{P}$ is a zero divisor. (The idempotent $\tilde{P}_+ = \tfrac{1}{2}(e_0 + ie_3)$ — which is $\tilde{P}$ itself — is an element of $\mathbb{M}_+$ that does lie in the state module; a generic Hermitian element does not. Membership in $\mathbb{B}\tilde{P}$ does not follow from being a zero divisor: $\tilde{P}_- = \tfrac{1}{2}(e_0 - ie_3)$ is a zero divisor too, and $X\tilde{P} = \tilde{P}_-$ would give $\tilde{P}_- = \tilde{P}_-\tilde{P} = 0$, impossible.) The correct exclusion is therefore structural — $\mathbb{M}_+$ is not a left ideal, and its elements need not be zero divisors — not the absence of solutions.

The correct relation between the two kinds of state is bilinear. From $\psi \in \mathbb{B}\tilde{P}$ one forms

$$
\tilde{\rho} = \frac{\psi\,\psi^\dagger}{\mathrm{Tr}(\psi^\dagger\psi)} \in \mathbb{M}_+,
$$

which is Hermitian, positive, and trace one — an element of the Bloch ball, hence a state in the sense of the companion article. The wave function and the density matrix are not the same object; they are related by $\psi \mapsto \psi\psi^\dagger$, and the same element $i$ acts as complex structure on the spinor while exchanging the sectors in which the operator is expressed.

## The Schrödinger Equation and Its Solution

With these objects separated, the equation reads

$$
i\hbar\,\partial_t\psi(t) = \tilde{H}\,\psi(t),
\qquad
\tilde{H} = h_0e_0 + i\mathbf{h} \in \mathbb{M}_+,
\qquad
\psi(t) \in \mathbb{B}\tilde{P},
$$

where $i$ is the scalar imaginary. Because $i$ is central, $i\tilde{H} = \tilde{H}i$, and there is no left/right ordering ambiguity in the equation. Because $\mathbb{B}\tilde{P}$ is a left ideal, $\tilde{H}\psi \in \mathbb{B}\tilde{P}$, so the equation is consistent within the module.

**Solution.** Since $-i\tilde{H} = -ih_0e_0 + \mathbf{h}$ and the scalar and vector parts commute,

$$
\tilde{U}(t) = \exp\!\left(-i\tilde{H}t/\hbar\right)
= e^{-ih_0t/\hbar}\left(\cos\theta\,e_0 + \sin\theta\,\hat{\mathbf{h}}\right),
\qquad
\theta = \frac{|\mathbf{h}|t}{\hbar},
$$

and $\psi(t) = \tilde{U}(t)\psi(0)$. The element $\tilde{U}$ is unitary, $\tilde{U}\tilde{U}^\dagger = e_0$: the central phase cancels and $R = \cos\theta\,e_0 + \sin\theta\,\hat{\mathbf{h}}$ is a unit real quaternion, $R R^\dagger = e_0$. Consequently the Hermitian norm $\mathrm{Tr}(\psi^\dagger\psi)$ is preserved: with $\psi(t) = \tilde{U}\psi(0)$,

$$
\mathrm{Tr}\!\left(\psi(t)^\dagger\psi(t)\right)
= \mathrm{Tr}\!\left(\psi(0)^\dagger \tilde{U}^\dagger\tilde{U}\,\psi(0)\right)
= \mathrm{Tr}\!\left(\psi(0)^\dagger\psi(0)\right).
$$

Differentiating the solution gives $i\hbar\,\partial_t\psi = i\hbar(-i\tilde{H}/\hbar)\psi = \tilde{H}\psi$, so it is the required solution.

**Case checked.** For $\tilde{H} = i\,e_1$ one has $h_0 = 0$, $\mathbf{h} = e_1$, and $\tilde{U}(t) = \cos(t/\hbar)e_0 + \sin(t/\hbar)e_1$. Then $\tilde{U}(t)$ is unitary, and $\tilde{H}\tilde{U} = i e_1(\cos(t/\hbar)e_0 + \sin(t/\hbar)e_1) = i\cos(t/\hbar)e_1 - i\sin(t/\hbar)e_0$ equals $i\hbar\,\dot{\tilde{U}} = i(-\sin(t/\hbar)e_0 + \cos(t/\hbar)e_1)$, term by term. This case was chosen independently of the general formula and confirms it.

**Consistency with the density matrix.** The companion article's equation for $\tilde{\rho} = \psi\psi^\dagger$ follows from the spinor equation. Differentiating $\tilde{\rho} = \psi\psi^\dagger$ and using $\partial_t\psi = -i\tilde{H}\psi/\hbar$, $\partial_t\psi^\dagger = i\psi^\dagger\tilde{H}/\hbar$ (valid because $\tilde{H}^\dagger = \tilde{H}$) gives

$$
\partial_t\tilde{\rho} = -\frac{i}{\hbar}\tilde{H}\tilde{\rho} + \frac{i}{\hbar}\tilde{\rho}\tilde{H}
= -\frac{i}{\hbar}[\tilde{H},\tilde{\rho}],
\qquad\text{i.e.}\qquad
i\hbar\,\partial_t\tilde{\rho} = [\tilde{H},\tilde{\rho}],
$$

which is the von Neumann equation of the parent article. The Born rule follows as there: with $\tilde{\rho} = \tfrac12(e_0 + i\mathbf{r})$ and $\tilde{P}_+(\hat{\mu}) = \tfrac12(e_0 + i\hat{\mu})$,

$$
p_+ = \mathrm{Tr}\!\left(\tilde{P}_+(\hat{\mu})\,\tilde{\rho}\right) = \tfrac12\left(1 + \hat{\mu}\cdot\mathbf{r}\right).
$$

For the up-state spinor $\psi = \begin{pmatrix} 1 \\ 0\end{pmatrix}$ one has $\mathbf{r} = e_3$, and $p_+ = \tfrac12(1 + \hat{\mu}\cdot e_3)$, the standard result.

## Why the Scalar Imaginary, and Not a Quaternion Unit

It is worth making precise why the obvious alternatives to $i$ fail. Suppose a root $J$ with $J^2 = -1$ is used in place of $i$:

$$
\hbar\,J\,\partial_t\psi = \tilde{H}\psi
\qquad\Longrightarrow\qquad
\partial_t\psi = -\frac{1}{\hbar}J\tilde{H}\,\psi,
$$

so the generator of the flow is $\tilde{G} = -\hbar^{-1}J\tilde{H}$. The flow preserves the Hermitian form, i.e. $\exp(t\tilde{G})$ is unitary, exactly when $\tilde{G}$ is anti-Hermitian, which is the condition

$$
(J\tilde{H})^\dagger = -J\tilde{H}
\qquad\Longleftrightarrow\qquad
\tilde{H}J^\dagger = -J\tilde{H}
\quad\text{for all Hermitian } \tilde{H}.
$$

Taking $\tilde{H} = e_0$ gives $J^\dagger = -J$, so $J$ must be anti-Hermitian; the condition then becomes $\tilde{H}J = J\tilde{H}$ for every Hermitian $\tilde{H}$. Take $\tilde{H} = i\,e_j$ with $j = 1,2,3$, which is Hermitian: since $i$ is central, the condition reads $e_jJ = Je_j$, so $J$ commutes with the quaternion units. Writing $J = \sum_\mu q_\mu e_\mu$, the relations $e_1J = Je_1$ and $e_2J = Je_2$ give $q_2 = q_3 = 0$ and then $q_1 = 0$, leaving $J = q_0e_0$ with $q_0 \in \mathbb{C}$. The centralizer of the quaternion units is therefore the center $\mathbb{C}_{\mathbb{B}} = \operatorname{span}_{\mathbb{R}}\{e_0, ie_0\}$: $J$ is central. Then $J^2 = -e_0$ gives $q_0^2 = -1$, so $q_0 = \pm i$. Thus the scalar imaginary is the *unique* choice, up to sign, that makes the equation norm-preserving for every Hermitian Hamiltonian.

**A counterexample for a quaternion unit.** Take $J = e_3$ (a root of $-1$) and the Hermitian $\tilde{H} = i\,e_1$. Then

$$
J\tilde{H} = e_3\,(i e_1) = i\,e_3e_1 = i\,e_2,
$$

using $e_3e_1 = e_2$. Since $i\,e_2$ is Hermitian, $(ie_2)^\dagger = ie_2$, the generator $\tilde{G} = -\hbar^{-1}J\tilde{H} = -\hbar^{-1}i\,e_2$ is Hermitian, not anti-Hermitian, and $\exp(t\tilde{G})$ is not unitary. Explicitly, at $t = \pi\hbar/2$,

$$
\tilde{U}^\dagger\tilde{U} = \exp\!\left(-i\pi e_2\right)
= \cosh(\pi)\,e_0 - i\sinh(\pi)\,e_2 \neq e_0,
$$

so the norm is not preserved by this "Schrödinger equation". The failure is generic: a non-central $J$ fails as soon as $\tilde{H}$ does not commute with it.

There is a second defect in the non-central choice: because $e_3e_1 = e_2$ while $e_1e_3 = -e_2$, the elements $e_3\psi$ and $\psi e_3$ differ, so the left- and right-handed readings of "the same" equation produce opposite generators. The centrality of $i$ removes this ambiguity.

**A caveat, stated honestly.** A non-central $J$ is not *never* admissible: if a particular $\tilde{H}$ commutes with $J$, then $J\tilde{H}$ can be anti-Hermitian and the flow unitary on that sector (for instance $\tilde{H} = i\,e_3$ and $J = e_3$, giving $J\tilde{H} = -ie_0$). What fails is uniformity, and a unit that works only for Hamiltonians aligned with a preferred direction is not a unit for the Schrödinger equation.

## The $\mathbb{M}_-$ and $\mathbb{M}_+$ Readings of the Equation

The equation can be rearranged into a statement that lives entirely in one sector at a time. Dividing by $i\hbar$,

$$
\partial_t\psi = \tilde{G}\psi,
\qquad
\tilde{G} = -\frac{i}{\hbar}\tilde{H} = \frac{\mathbf{h} - i h_0 e_0}{\hbar} \in \mathbb{M}_-.
$$

The generator $\tilde{G}$ is anti-Hermitian; this is the general reason the exponential is unitary. The two readings are then:

- **$\mathbb{M}_+$ reading.** The Hamiltonian $\tilde{H} \in \mathbb{M}_+$ is a Hermitian observable — an energy. The equation says that the dynamics is generated by that observable, read through the intertwiner $i$.
- **$\mathbb{M}_-$ reading.** The generator $\tilde{G} \in \mathbb{M}_-$ lies in the *material* sector, the same four-dimensional real space that carries the four-vectors of relativistic physics. The time-translation generator is an element of that sector, and the Hamiltonian is recovered as $\tilde{H} = i\hbar\tilde{G}$.

In the von Neumann form the split is even cleaner. For $\tilde{H}, \tilde{\rho} \in \mathbb{M}_+$,

$$
\left([\tilde{H},\tilde{\rho}]\right)^\dagger = \tilde{\rho}\tilde{H} - \tilde{H}\tilde{\rho} = -[\tilde{H},\tilde{\rho}],
$$

so $[\tilde{H},\tilde{\rho}] \in \mathbb{M}_-$; and since $\tilde{\rho} \in \mathbb{M}_+$ and $i\,\mathbb{M}_+ = \mathbb{M}_-$, the term $i\hbar\,\partial_t\tilde{\rho}$ is also in $\mathbb{M}_-$. The von Neumann equation is thus an identity in a single sector, while its solution returns to the complementary one.

A structural caution belongs here. The wave function $\psi$ itself is an element of the state module $\mathbb{B}\tilde{P}$, not of either sector; it carries no $\mathbb{M}_\pm$ label. The decomposition $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$ classifies Hermitian observables and anti-Hermitian generators, not state vectors. What returns to $\mathbb{M}_+$ is the bilinear object $\tilde{\rho} = \psi\psi^\dagger$, not $\psi$. Reading the sector labels onto the wave function is the same error as conflating the wave function with the density matrix.

## What the Biquaternion Form Adds and What It Merely Relabels

**The relabelling.** Under $\mathbb{B} \cong M_2(\mathbb{C})$ with $e_j \mapsto -i\sigma_j$, a spinor in $\mathbb{B}\tilde{P}$ is a column vector in $\mathbb{C}^2$, the scalar imaginary is the standard imaginary unit, $\tilde{U}(t)$ is a standard element of $U(2)$, and the equation is literally the two-component Schrödinger equation. Nothing is added for a single qubit beyond vocabulary: the biquaternion equation predicts exactly what the standard one predicts.

**What is structural.** Three features are genuinely rearranged rather than merely renamed.

1. *The complex structure is supplied, not chosen.* Since $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ contains the central element $i$ by construction, the complex structure of the state module is fixed by the algebra. In a purely quaternionic formulation — wave functions valued in $\mathbb{H}$, with no complexifying factor — there is no central imaginary unit, and one must *choose* a complex structure on the state space, so the choice becomes extra input. Here the algebra supplies it, and the quaternion units, being non-central, are not candidates. This is definitional — $\mathbb{C}$ was put into $\mathbb{B}$ by fiat — but the content is that the same algebra contains both the quaternion units and the central root of $-1$, unique up to sign, that quantum mechanics requires.

2. *The observable/generator split is intrinsic.* $\mathbb{M}_+$ and $\mathbb{M}_-$ are the fixed-point subspaces of Hermitian conjugation, and $i$ is the canonical real-linear isomorphism relating them. The Schrödinger equation is exactly the map $\tilde{H} \mapsto \tilde{G} = -i\tilde{H}/\hbar$ from observables to generators. In $M_2(\mathbb{C})$ language this is the elementary statement that $\tilde{H}$ is Hermitian iff $-i\tilde{H}$ is anti-Hermitian; the biquaternion form names the two sectors that the statement relates, and places the generator in the material sector.

3. *The roots of $-1$ are separated by role.* The central roots $\pm i$ are the complex structure; the non-central roots $\hat{\mu}$ are state axes and rotation generators. A formulation that writes the Schrödinger equation with a quaternion unit destroys the first while leaving the second in place, and the counterexample above shows how. The biquaternion form keeps the two apart by construction.

**Honest bottom line.** For a single qubit this is a rewriting of a known equation. It is interesting because the same algebra also carries the Lorentz group and the Dirac equation, and because its two Hermitian fixed-point subspaces correspond to the physical and informational sectors of the wider proposal; but it produces no new prediction here. Whether it produces one in the many-body or relativistic setting is open.

## Open Questions

**1. The local complex structure.** The series makes the complex structure local: it is set by the medium through $c = 1/\sqrt{\epsilon\mu}$ and reduces to $ic_0t$ in vacuum. The scalar imaginary $i$ is a global central element of $\mathbb{B}$, and a central element cannot vary from point to point. Does the $i$ of the Schrödinger equation remain global, or does a local complex structure enter the state module? The relation between the two is unresolved.

**2. Many qubits.** The extension to $n$ qubits is via $\mathbb{B}^{\otimes n} \cong M_{2^n}(\mathbb{C})$. The companion article leaves the tensor product over $\mathbb{C}$ as an open question. If it is taken over $\mathbb{C}$, the scalar imaginary remains available as the complex structure; if not, the question of the imaginary unit returns in a new form.

**3. Dependence on the choice of minimal left ideal.** The choice $\tilde{P} = \tfrac12(e_0 + ie_3)$ is a choice of the state axis. Different minimal left ideals are unitarily equivalent, so the physics should be independent of it, but this article has not argued that explicitly; it should be stated as a basis choice.

**4. The non-relativistic limit.** Whether this Schrödinger equation is the precise non-relativistic limit of the biquaternion Dirac equation, or only an independent qubit equation, is not checked here.

**5. Second quantization and the path integral.** The framework is first-quantized and has no path-integral form in this article; both are open in the parent.

## Summary

The Schrödinger equation in biquaternionic form is

$$
i\hbar\,\partial_t\psi = \tilde{H}\psi,
$$

with $\tilde{H} = h_0e_0 + i\mathbf{h} \in \mathbb{M}_+$ Hermitian, $\psi$ a spinor in a minimal left ideal $\mathbb{B}\tilde{P} \cong \mathbb{C}^2$, and $i$ the **scalar imaginary** — the central root of $-1$ in $\mathbb{B}$, unique up to sign.

The symbol $i$ must not be confused with the quaternion units or the non-central roots of $-1$, which are rotation axes, and it is not a complex structure on $\mathbb{M}_+$, since $i\,\mathbb{M}_+ = \mathbb{M}_-$: the scalar imaginary is the canonical isomorphism between the two sectors, not an operator on either. The wave function is a spinor in the state module, not a generic element of $\mathbb{M}_+$; the density matrix is recovered as $\tilde{\rho} = \psi\psi^\dagger/\mathrm{Tr}(\psi^\dagger\psi) \in \mathbb{M}_+$, and the spinor equation implies the parent article's von Neumann equation $i\hbar\,\partial_t\tilde{\rho} = [\tilde{H},\tilde{\rho}]$.

Using a non-central root $J$ in place of $i$ fails generically: the generator $-\hbar^{-1}J\tilde{H}$ need not be anti-Hermitian, so the flow is not unitary and the norm is not preserved (explicitly for $J = e_3$, $\tilde{H} = ie_1$). The scalar imaginary is the only choice, up to sign, that works for every Hermitian Hamiltonian.

Read in the two sectors, the equation says that the Hermitian observable $\tilde{H} \in \mathbb{M}_+$ generates, through the intertwiner $i$, a flow whose generator $\tilde{G} = -i\tilde{H}/\hbar$ lies in the material sector $\mathbb{M}_-$. For a single qubit this is a rewriting of the standard two-component equation; the structural content is that the complex structure is supplied by the algebra, the observable/generator split is intrinsic to the Hermitian decomposition, and the roots of $-1$ are separated by role.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_j^2 = -e_0$ |
| $i$ | Scalar imaginary, central, $i^2 = -e_0$ |
| $\mathbb{C}_{\mathbb{B}}$ | Complex subspace $\operatorname{span}_{\mathbb{R}}\{e_0, ie_0\}$; the center |
| $\mathbb{M}_+$ | Hermitian subspace (observables): $i\hbar\,\partial_t\psi = \tilde{H}\psi$ has $\tilde{H} \in \mathbb{M}_+$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (generators): $\tilde{G} = -i\tilde{H}/\hbar \in \mathbb{M}_-$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subspace; home of the unit pure quaternions $\hat{\mu}$ |
| $\tilde{H} = h_0e_0 + i\mathbf{h}$ | Hermitian element (Hamiltonian) |
| $\tilde{P}_\pm(\hat{\mu}) = \tfrac12(e_0 \pm i\hat{\mu})$ | Idempotent (pure state); $\hat{\mu}$ the state axis |
| $\mathbb{B}\tilde{P} \cong \mathbb{C}^2$ | Minimal left ideal: the state module of spinors $\psi$ |
| $\tilde{\rho} = \psi\psi^\dagger/\mathrm{Tr}(\psi^\dagger\psi)$ | Density matrix associated to a spinor |
| $\tilde{U}(t) = \exp(-i\tilde{H}t/\hbar)$ | Unitary evolution, $\psi(t) = \tilde{U}(t)\psi(0)$ |
| $\mathrm{Tr}(\tilde{P}_+(\hat{\mu})\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}_+(\hat{\mu})\tilde{H}) = h_0 + \hat{\mu}\cdot\mathbf{h}$ | Trace formula / Born rule |
| $e_j e_k = \varepsilon_{jkl}e_l$, $j \neq k$ | Quaternion multiplication |

## Further Reading

- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the original state-vector formulation.
- John von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton, 1932), for the density-matrix formulation and the von Neumann equation.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard two-component Schrödinger equation.
- Stephen L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford, 1995), for the quaternionic formulation in which a complex structure must be chosen.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the algebra of $\mathbb{B}$ and its minimal left ideals.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of spinors and the Schrödinger equation.
