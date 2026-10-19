# __Exercise: Quantum Channels and Dephasing in M+__

## Introduction

This is one of a series of **worked exercises** on quantum physics in the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$. Earlier exercises treated the kinematics of a qubit and of a pair of qubits; each was a single problem solved twice, once in the standard Hilbert-space formulation and once in the biquaternion formulation of the Hermitian subspace $\mathbb{M}_+$. This exercise is different in structure. Its parent is the article *Quantum Channels and the Reversible/Irreversible Dichotomy*, which develops the general state map on $\mathbb{M}_+$ — the quantum channel, its Kraus representation, complete positivity, the Choi matrix, and the reversible/irreversible dichotomy. The reader is assumed to have that formalism and is asked to apply it.

The article is therefore a sequence of independent problems, each in its own section. We work throughout in the notation of the parent, returning to the standard matrix formulation only where the parent itself does (the transpose map, the Choi matrix, and the standard Kraus operators of amplitude damping). The problems are:

1. Writing the dephasing channel as a Kraus sum and computing its action on a general Bloch vector.
2. Computing the Kraus rank of dephasing and finding a minimal Kraus representation.
3. Showing that the transpose map is positive but not completely positive.
4. The amplitude-damping channel: Kraus operators, fixed states, and purity.
5. Composition of channels, and the growth of the Kraus rank.
6. The Bloch-ball contraction and the increase of the von Neumann entropy under dephasing.

The conventions are those of the companion articles. The quaternion units are $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_k^2 = -e_t$; $i$ is the central scalar imaginary. The Hermitian subspace $\mathbb{M}_+$ consists of the elements $\tilde{H} = h_t e_t + i\vec h$ with real $h_t$ and $\vec h \in \mathbb{R}^3$. A state is $\tilde{Ϛ} = \tfrac{1}{2}(e_t + i\vec r)$ with $|\vec r| \leq 1$, and $\vec r$ is its Bloch vector. The trace is $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$, so the Born rule is $\mathrm{Tr}(\tilde{Ϛ}\tilde{H}) = h_t + \vec r\cdot\vec h$. A **channel** is a completely positive, trace-preserving map with a Kraus representation $\Phi(\tilde{Q}) = \sum_l \tilde{K}_l\tilde{Q}\tilde{K}_l^{*}$ and normalization $\sum_l \tilde{K}_l^{*}\tilde{K}_l = e_t$, and the Choi matrix is $J(\Phi) = \sum_{jk}\tilde{E}_{jk}\otimes\Phi(\tilde{E}_{jk})$ as in the parent. The dephasing channel along the unit pure real quaternion $\vec u_x$ is
$$
\Phi^{\mathrm{deph}}_p(\tilde{Ϛ})
:= (1-p)\,\tilde{Ϛ}
+ p\left(\tilde\Pi_1\,\tilde{Ϛ}\,\tilde\Pi_1 + \tilde\Pi_2\,\tilde{Ϛ}\,\tilde\Pi_2\right),
\qquad
\tilde\Pi_{1,2}(\vec u_x) = \tfrac{1}{2}\left(e_t \pm i\vec u_x\right).
$$
Throughout, $\log$ denotes the natural logarithm.

## Problem 1: Dephasing as a Kraus Sum

**Problem.** Verify that the dephasing channel $\Phi^{\mathrm{deph}}_p$ is trace preserving with the three Kraus operators
$$
\tilde{K}_0 = \sqrt{1-p}\,e_t, \qquad \tilde{K}_1 = \sqrt{p}\,\tilde\Pi_1(\vec u_x), \qquad \tilde{K}_2 = \sqrt{p}\,\tilde\Pi_2(\vec u_x),
$$
and compute $\Phi^{\mathrm{deph}}_p(\tilde{Ϛ})$ for the general state $\tilde{Ϛ} = \tfrac{1}{2}(e_t + i\vec r)$.

**Solution.** Put $\alpha = i\vec u_x$, so that $\tilde\Pi_{1,2} = \tfrac{1}{2}(e_t \pm \alpha)$. Since $\vec u_x^2 = -e_t$,
$$
\alpha^2 = (i\vec u_x)^2 = i^2\vec u_x^2 = (-1)(-e_t) = e_t,
\qquad
\alpha^{*} = (i\vec u_x)^{*} = -i\,\vec u_x^{*} = -i(-\vec u_x) = \alpha,
$$
so $\alpha^2 = e_t$ and $\alpha$ is Hermitian, as the idempotent structure requires. Trace preservation is immediate: because $\tilde\Pi_{1,2}$ are Hermitian idempotents, $\tilde{K}_1^{*}\tilde{K}_1 = p\,\tilde\Pi_1$ and $\tilde{K}_2^{*}\tilde{K}_2 = p\,\tilde\Pi_2$, whence
$$
\tilde{K}_0^{*}\tilde{K}_0 + \tilde{K}_1^{*}\tilde{K}_1 + \tilde{K}_2^{*}\tilde{K}_2
= (1-p)\,e_t + p\,(\tilde\Pi_1 + \tilde\Pi_2) = e_t .
$$

For the action on the state, use the elementary identity
$$
\tilde\Pi_1\,\tilde{Q}\,\tilde\Pi_1 + \tilde\Pi_2\,\tilde{Q}\,\tilde\Pi_2
= \tfrac{1}{2}\left(\tilde{Q} + \alpha\,\tilde{Q}\,\alpha\right),
$$
valid for every $\tilde{Q} \in \mathbb{B}$: the cross terms come with opposite signs,
$$
\tfrac{1}{4}\left(e_t \pm \alpha\right)\tilde{Q}\left(e_t \pm \alpha\right)
= \tfrac{1}{4}\left(\tilde{Q} \pm \alpha\tilde{Q} \pm \tilde{Q}\alpha + \alpha\tilde{Q}\alpha\right),
$$
and cancel in the sum. The two products needed are
$$
\alpha\,e_t\,\alpha = \alpha^2 = e_t, \qquad
\alpha\,(i\vec r)\,\alpha = i^3\,\vec u_x\,\vec r\,\vec u_x = -i\,\vec u_x\,\vec r\,\vec u_x .
$$
For the second we use the quaternion identity
$$
\vec u_x\,\vec r\,\vec u_x = \vec r - 2(\vec u_x\cdot\vec r)\,\vec u_x .
$$
*Proof:* decompose $\vec r = \vec r_\parallel + \vec r_\perp$ with $\vec r_\parallel = (\vec u_x\cdot\vec r)\vec u_x$ and $\vec r_\perp \perp \vec u_x$. Then $\vec u_x\,\vec r_\parallel\,\vec u_x = (\vec u_x\cdot\vec r)\,\vec u_x^3 = -(\vec u_x\cdot\vec r)\vec u_x = -\vec r_\parallel$, because $\vec u_x^3 = \vec u_x\vec u_x^2 = -\vec u_x$; and for the orthogonal part $\vec u_x\,\vec r_\perp = \vec u_x\times\vec r_\perp$, so $\vec u_x\,\vec r_\perp\,\vec u_x = (\vec u_x\times\vec r_\perp)\times\vec u_x = \vec r_\perp$. Summing gives the identity. Therefore
$$
\alpha\,\tilde{Ϛ}\,\alpha
= \tfrac{1}{2}\left(e_t - i\,\vec u_x\,\vec r\,\vec u_x\right)
= \tfrac{1}{2}\left(e_t - i\vec r + 2i(\vec u_x\cdot\vec r)\,\vec u_x\right),
$$
and hence
$$
\tilde\Pi_1\tilde{Ϛ}\tilde\Pi_1 + \tilde\Pi_2\tilde{Ϛ}\tilde\Pi_2
= \tfrac{1}{2}\left(\tilde{Ϛ} + \alpha\tilde{Ϛ}\alpha\right)
= \tfrac{1}{2}\left(e_t + i(\vec u_x\cdot\vec r)\,\vec u_x\right).
$$
Combining with the mixture,
$$
\boxed{\;\Phi^{\mathrm{deph}}_p(\tilde{Ϛ}) = \tfrac{1}{2}\left(e_t + i\,\vec r'\right),
\qquad
\vec r' = (1-p)\,\vec r + p\,(\vec u_x\cdot\vec r)\,\vec u_x.\;}
$$
The transverse components of the Bloch vector are multiplied by $1-p$, while the longitudinal component is untouched. At $p=0$ the channel is the identity; at $p=1$ it is the projection $\vec r \mapsto (\vec u_x\cdot\vec r)\vec u_x$, the "measure-and-forget" channel of the parent.

**Special case $\vec u_x = \vec e_z$.** The Kraus operators are $\tilde{K}_0 = \sqrt{1-p}\,e_t$, $\tilde{K}_1 = \tfrac{1}{2}\sqrt{p}\,(e_t + i\vec e_z)$, $\tilde{K}_2 = \tfrac{1}{2}\sqrt{p}\,(e_t - i\vec e_z)$, and the Bloch map is $\vec r' = (1-p)(r_1 \vec e_x + r_2 \vec e_y) + r_3 \vec e_z$.

## Problem 2: The Kraus Rank of Dephasing

**Problem.** Compute the Choi matrix of $\Phi^{\mathrm{deph}}_p$ in the computational basis and determine its rank. Deduce the minimal Kraus rank, exhibit a minimal Kraus representation, and decide whether the three-operator representation of Problem 1 is minimal.

**Solution.** The rank of the Choi matrix is invariant under unitary conjugation, and dephasing along any unit axis is unitarily equivalent to dephasing along $\vec e_z$; we therefore fix $\vec u_x = \vec e_z$. Let $E_{jk} = |j\rangle\langle k|$ be the matrix units of the computational basis, expressed in the algebra as
$$
E_{00} = \tfrac{1}{2}(e_t + i\vec e_z), \quad
E_{11} = \tfrac{1}{2}(e_t - i\vec e_z), \quad
E_{01} = \tfrac{1}{2}(i\vec e_x - \vec e_y), \quad
E_{10} = \tfrac{1}{2}(i\vec e_x + \vec e_y).
$$
These are the elements the parent denotes $\tilde{E}_{jk}$; they satisfy $\mathrm{Tr}(E_{jk}E_{lm}) = \delta_{kl}\delta_{jm}$. The idempotents $\tilde\Pi_+ = \tfrac{1}{2}(e_t + i\vec e_z)$ and $\tilde\Pi_- = \tfrac{1}{2}(e_t - i\vec e_z)$ are exactly $E_{00}$ and $E_{11}$; the element $i\vec e_z$ is a root of $+1$, $(i\vec e_z)^2 = e_t$, and the two are its associated idempotents. Since dephasing fixes the populations and scales the coherences by $1-p$,
$$
\Phi(E_{00}) = E_{00}, \qquad \Phi(E_{11}) = E_{11}, \qquad \Phi(E_{01}) = (1-p)\,E_{01}, \qquad \Phi(E_{10}) = (1-p)\,E_{10},
$$
the off-diagonal statement following because $\tilde\Pi_+ E_{01}\tilde\Pi_+ = \tilde\Pi_- E_{01}\tilde\Pi_- = 0$. With the parent's convention $J(\Phi) = \sum_{jk}E_{jk}\otimes\Phi(E_{jk})$ and the product basis $(|00\rangle,|01\rangle,|10\rangle,|11\rangle)$,
$$
E_{01}\otimes E_{01} = |00\rangle\langle 11|, \qquad E_{10}\otimes E_{10} = |11\rangle\langle 00|,
$$
so
$$
J = \begin{pmatrix}
1 & 0 & 0 & 1-p\\
0 & 0 & 0 & 0\\
0 & 0 & 0 & 0\\
1-p & 0 & 0 & 1
\end{pmatrix}.
$$
The only nonzero block is $\begin{pmatrix}1 & 1-p\\ 1-p & 1\end{pmatrix}$, whose eigenvalues are $1 \pm (1-p)$; hence
$$
\mathrm{spec}\,J = \{\,2-p,\; p,\; 0,\; 0\,\}.
$$
Thus $J \succeq 0$ for $0 \leq p \leq 2$, confirming complete positivity (the parent restricts to the sub-range $0 \leq p \leq 1$, where $\Phi^{\mathrm{deph}}_p$ is a convex mixture of the identity and the full-dephasing measurement channel), and
$$
\mathrm{rank}\,J = 2 \text{ for } 0 < p < 2, \qquad \mathrm{rank}\,J = 1 \text{ at } p=0 \text{ and at } p=2 .
$$
By the parent's rank theorem, the **minimal Kraus rank is two** for $0<p<2$, and a minimal representation is
$$
\tilde{K}_0 = \sqrt{1-\tfrac{p}{2}}\;e_t, \qquad \tilde{K}_1 = \sqrt{\tfrac{p}{2}}\;i\vec u_x .
$$
At $p=2$ the first operator vanishes, $\tilde{K}_0=0$, and the pair collapses to the single operator $\tilde{K}_1=i\vec u_x$, which is unitary; that endpoint lies outside the parent's physical range $0\le p\le 1$.

Trace preservation holds because $(i\vec u_x)^{*}(i\vec u_x) = (i\vec u_x)^2 = i^2\vec u_x^2 = e_t$, so $\tilde{K}_0^{*}\tilde{K}_0 + \tilde{K}_1^{*}\tilde{K}_1 = (1-\tfrac{p}{2})e_t + \tfrac{p}{2}e_t = e_t$. The action is
$$
\Phi(\tilde{Ϛ}) = \left(1-\tfrac{p}{2}\right)\tilde{Ϛ} + \tfrac{p}{2}\,(i\vec u_x)\,\tilde{Ϛ}\,(i\vec u_x).
$$
Since $(i\vec u_x)\tilde{Ϛ}(i\vec u_x) = -\vec u_x\tilde{Ϛ}\vec u_x = \tfrac{1}{2}\left(e_t - i\vec r + 2i(\vec u_x\cdot\vec r)\vec u_x\right)$, this reproduces $\vec r' = (1-p)\vec r + p(\vec u_x\cdot\vec r)\vec u_x$, as required.

**Conclusion.** The three-operator representation of Problem 1 is valid but **not minimal**: for $0<p<1$ the span of $\{\tilde{K}_0,\tilde{K}_1,\tilde{K}_2\}$ is two-dimensional, since $\tilde{K}_0 = \sqrt{1-p}\,(\tilde\Pi_1 + \tilde\Pi_2)$. The minimal representation given above has two operators. Consistently with the parent's dichotomy, dephasing has Kraus rank one at $p=0$ (the identity) and Kraus rank two for $0<p\le1$, and is therefore irreversible throughout the physical range except at its identity endpoint. The formal continuation to $p\in(1,2]$ is completely positive but leaves that range, and at $p=2$ it degenerates: $\tilde{K}_0=0$ and the channel reduces to the unitary conjugation $\tilde{Ϛ}\mapsto(i\vec u_x)\tilde{Ϛ}(i\vec u_x)^{*}$, of Kraus rank one and reversible.

## Problem 3: A Positive Map That Is Not Completely Positive

**Problem.** In the matrix representative of $\mathbb{B}$, let $\Phi_T$ be the transpose, $\Phi_T(\tilde{Q}) = \tilde{Q}^{\mathsf{T}}$. Show that $\Phi_T$ is positive and trace preserving, but not completely positive.

**Solution.** On the matrix units $\Phi_T$ acts by $E_{jk} \mapsto E_{kj}$; equivalently, on a state,
$$
\Phi_T\!\left(\tfrac{1}{2}(e_t + i\vec r)\right) = \tfrac{1}{2}\left(e_t + i(r_1 \vec e_x - r_2 \vec e_y + r_3 \vec e_z)\right),
$$
because $\sigma_1$ and $\sigma_3$ are real while $\sigma_2$ is imaginary. So $\Phi_T$ acts on the Bloch ball by the reflection
$$
(r_1, r_2, r_3) \longmapsto (r_1, -r_2, r_3).
$$
This map is **trace preserving** (the transpose fixes $e_t$ and preserves the trace) and **positive**: the reflection is an isometry of $\mathbb{R}^3$ that maps the ball $|\vec r|\leq 1$ onto itself, so it maps states to states.

To test complete positivity, compute the Choi matrix. Transposition swaps the off-diagonal units, $\Phi_T(E_{01}) = E_{10}$ and $\Phi_T(E_{10}) = E_{01}$, while fixing $E_{00}$ and $E_{11}$. Hence, using $E_{01}\otimes E_{10} = |01\rangle\langle 10|$ and $E_{10}\otimes E_{01} = |10\rangle\langle 01|$,
$$
J_T = E_{00}\otimes E_{00} + E_{11}\otimes E_{11} + E_{01}\otimes E_{10} + E_{10}\otimes E_{01}
= \begin{pmatrix}
1 & 0 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 0 & 1
\end{pmatrix}.
$$
This is the **swap operator**, $J_T|jk\rangle = |kj\rangle$. Its eigenvalues are $+1$ on the symmetric subspace $\{|00\rangle, |11\rangle, (|01\rangle+|10\rangle)/\sqrt{2}\}$ and $-1$ on the antisymmetric (singlet) direction $(|01\rangle-|10\rangle)/\sqrt{2}$, so
$$
\mathrm{spec}\,J_T = \{\,1,\;1,\;1,\;-1\,\}.
$$
The Choi matrix is therefore not positive semidefinite, and by the parent's criterion $\Phi_T$ is **not completely positive**. Equivalently, transposing one qubit of a maximally entangled state can produce an operator with a negative eigenvalue: the antisymmetric direction of $J_T$ is exactly the singlet, which acquires the eigenvalue $-1$. No physical process can act that way on half of an entangled pair, so $\Phi_T$ is not a channel, despite being positive and trace preserving. This is the parent's point that positivity must be strengthened to complete positivity, made explicit on the simplest example.

The conclusion does not depend on the choice of matrix representative: transposes in two orthonormal bases are related by unitary conjugation, and the spectrum of the Choi matrix is invariant under unitary conjugation of the channel.

## Problem 4: The Amplitude-Damping Channel

**Problem.** The amplitude-damping channel with damping parameter $\gamma \in [0,1]$ acts on the Bloch vector as
$$
(r_1, r_2, r_3) \longmapsto \left(\sqrt{1-\gamma}\,r_1,\ \sqrt{1-\gamma}\,r_2,\ \gamma + (1-\gamma)r_3\right).
$$
Find its Kraus operators in $\mathbb{B}$, verify trace preservation, and determine its fixed states, its action on the ground and excited states, and its effect on purity.

**Solution.** In the matrix representative the standard Kraus operators are
$$
K_0 = \begin{pmatrix}1 & 0\\ 0 & \sqrt{1-\gamma}\end{pmatrix},
\qquad
K_1 = \begin{pmatrix}0 & \sqrt{\gamma}\\ 0 & 0\end{pmatrix} = \sqrt{\gamma}\,|0\rangle\langle 1| .
$$
Writing $s = \sqrt{1-\gamma} \in [0,1]$ and using $\sigma_3 = i\vec e_z$ and $|0\rangle\langle 1| = \tfrac{1}{2}(i\vec e_x - \vec e_y)$, these translate to
$$
\tilde{K}_0 = \frac{1+s}{2}\,e_t + i\,\frac{1-s}{2}\,\vec e_z \;\in \mathbb{M}_+,
\qquad
\tilde{K}_1 = \frac{\sqrt{\gamma}}{2}\left(i \vec e_x - \vec e_y\right) \in \mathbb{B}.
$$
Here $\tilde{K}_0$ is Hermitian (it is an element of $\mathbb{M}_+$), while $\tilde{K}_1$ is not. Trace preservation follows from
$$
\tilde{K}_0^{*}\tilde{K}_0 = \frac{1+s^2}{2}\,e_t + i\,\frac{1-s^2}{2}\,\vec e_z,
\qquad
\tilde{K}_1^{*}\tilde{K}_1 = \frac{\gamma}{2}\left(e_t - i\vec e_z\right),
$$
whose sum is $e_t$, since $1 + s^2 + \gamma = 2$ and $1 - s^2 - \gamma = 0$. A direct quaternion expansion of $\tilde{K}_0\tilde{Ϛ}\tilde{K}_0^{*} + \tilde{K}_1\tilde{Ϛ}\tilde{K}_1^{*}$ for $\tilde{Ϛ} = \tfrac{1}{2}(e_t + i\vec r)$ gives $\tfrac{1}{2}(e_t + i\vec r')$ with exactly the Bloch map stated above; the $\tilde{K}_1$ term contributes the population $\tfrac{\gamma}{4}(1-r_3)(e_t + i\vec e_z)$ that is transferred to the ground state.

**Fixed states.** Set $r_1 = r_2 = 0$ and $z = \gamma + (1-\gamma)z$, giving $z = 1$. For every $\gamma>0$ the channel has the **unique** fixed state
$$
\tilde{Ϛ}_* = \tfrac{1}{2}\left(e_t + i\vec e_z\right) = \tilde\Pi_1(\vec u_z),
$$
the pure ground state. For $\gamma = 0$ the channel is the identity and every state is fixed.

**Non-unitality.** The channel does not fix the maximally mixed state:
$$
\Phi\left(\tfrac{1}{2}e_t\right) = \tfrac{1}{2}\left(e_t + i\gamma \vec e_z\right) \neq \tfrac{1}{2}e_t .
$$
The centre of the Bloch ball is moved to the Bloch vector $(0,0,\gamma)$. This is the structural difference from dephasing, which is unital.

**Ground and excited states.** The ground state $\vec r = (0,0,1)$ is fixed, as noted. The excited state $\vec r = (0,0,-1)$ is mapped to
$$
\vec r' = \left(0,\,0,\,\gamma - (1-\gamma)\right) = \left(0,\,0,\,2\gamma - 1\right).
$$
At $\gamma = \tfrac{1}{2}$ the excited state is driven to the **maximally mixed state** $(0,0,0)$; at $\gamma = 1$ it reaches the ground state. This is the standard incoherent decay of the excited state.

**Purity.** For a general input,
$$
\mathrm{Tr}\!\left(\tilde{Ϛ}'^2\right) = \tfrac{1}{2}\left(1 + (1-\gamma)\left(r_1^2 + r_2^2\right) + \left(\gamma + (1-\gamma)r_3\right)^2\right).
$$
For the maximally mixed input ($\vec r = 0$) the purity rises from $\tfrac{1}{2}$ to $\tfrac{1}{2}(1+\gamma^2) \geq \tfrac{1}{2}$: amplitude damping *purifies* the maximally mixed state by driving it toward the pure ground state. This is possible precisely because the channel is non-unital, and it is the opposite of the behaviour of dephasing. For the excited input $\vec r = (0,0,-1)$ the output purity is $\tfrac{1}{2}(1 + (2\gamma-1)^2)$, which is $\tfrac{1}{2}$ at $\gamma = \tfrac{1}{2}$ — the maximally mixed value — and rises to $1$ at $\gamma = 1$. Finally, the Choi rank of the channel is two for $\gamma>0$ (one at $\gamma=0$), so it is irreversible for every $\gamma>0$.

## Problem 5: Composition of Channels and the Growth of Kraus Rank

**Problem.** Let $\Phi_1$ have Kraus operators $\{A_m\}_{m=1}^{n_1}$ and $\Phi_2$ have Kraus operators $\{B_l\}_{l=1}^{n_2}$. Show that $\Phi_2\circ\Phi_1$ has Kraus operators $\{B_l A_m\}$ and deduce that $\mathrm{rank}(\Phi_2\circ\Phi_1) \leq \mathrm{rank}(\Phi_1)\,\mathrm{rank}(\Phi_2)$. Then compose two dephasing channels and determine the resulting Kraus rank.

**Solution.** Composing,
$$
\Phi_2\!\left(\Phi_1(\tilde{Q})\right)
= \sum_l B_l\left(\sum_m A_m\tilde{Q}A_m^{*}\right)B_l^{*}
= \sum_{l,m}\left(B_l A_m\right)\tilde{Q}\left(B_l A_m\right)^\dagger ,
$$
so $\{B_l A_m\}$ is a Kraus set for the composite, and it is trace preserving whenever both factors are. The Kraus rank of the composite is the dimension of the span of the products $B_l A_m$, which cannot exceed the product of the dimensions of the individual spans; hence $\mathrm{rank}(\Phi_2\circ\Phi_1) \leq \mathrm{rank}(\Phi_1)\,\mathrm{rank}(\Phi_2)$. For a qubit the composite has rank at most $4$, since its Choi matrix is $4\times4$.

**Composition of dephasings.** The Bloch map of $\Phi^{\mathrm{deph}}_p$ along $\vec u_x$ is the linear map $D(\vec u_x,p) = (1-p)I + p\,\vec u_x\vec u_x^{\mathsf{T}}$ acting on $\mathbb{R}^3$. Composing two of them,
$$
D(\vec u_y,q)\,D(\vec u_x,p)
= (1-p)(1-q)\,I
+ p(1-q)\,\vec u_x\vec u_x^{\mathsf{T}}
+ q(1-p)\,\vec u_y\vec u_y^{\mathsf{T}}
+ pq\,(\vec u_y\cdot\vec u_x)\,\vec u_y\vec u_x^{\mathsf{T}} .
$$
For **parallel axes**, $\vec u_y = \vec u_x$, the projector identity $\vec u_x\vec u_x^{\mathsf{T}}\vec u_x\vec u_x^{\mathsf{T}} = \vec u_x\vec u_x^{\mathsf{T}}$ collapses the sum to
$$
D(\vec u_x,q)\,D(\vec u_x,p) = D(\vec u_x,\,p+q-pq),
$$
so the composite is again a dephasing channel, with effective parameter $p' = p+q-pq$; its Kraus rank is at most two.

For **orthogonal axes and full dephasing**, take $\vec u_x = \vec e_z$, $\vec u_y = \vec e_x$ and $p = q = 1$. Then $D(\vec e_z,1) = \vec e_z\vec e_z^{\mathsf{T}}$, $D(\vec e_x,1) = \vec e_x\vec e_x^{\mathsf{T}}$, and
$$
D(\vec e_x,1)\,D(\vec e_z,1) = \vec e_x\left(\vec e_x^{\mathsf{T}}\vec e_z\right)\vec e_z^{\mathsf{T}} = 0 .
$$
The composite is the **completely depolarizing channel**, $\tilde{Ϛ} \mapsto \tfrac{1}{2}e_t$ for every state: every Bloch vector is sent to the origin. Its Choi matrix is
$$
J = \sum_{jk} E_{jk}\otimes\Phi(E_{jk}) = \sum_{k} E_{kk}\otimes \tfrac{1}{2}e_t = \tfrac{1}{2}I_4,
$$
of rank four. Thus composing two rank-two channels produces a rank-four channel, saturating the qubit bound $4 = 2\times 2$. More generally, for two distinct axes and $0<p,q<1$ the composite also saturates the bound and has Kraus rank four (checked numerically over the parameter range); the rank drops to two only when the axes are parallel or one of the channels is trivial.

## Problem 6: Bloch-Ball Contraction and the Increase of Entropy

**Problem.** Show that dephasing contracts the Bloch ball, $|\vec r'| \leq |\vec r|$, that it does not increase the purity, and that it does not decrease the von Neumann entropy. Evaluate a concrete case.

**Solution.** Decompose $\vec r = \vec r_\parallel + \vec r_\perp$ with $\vec r_\parallel = (\vec u_x\cdot\vec r)\vec u_x$ and $\vec r_\perp \perp \vec u_x$. From the Bloch map,
$$
\vec r' = (1-p)\vec r + p(\vec u_x\cdot\vec r)\vec u_x = (1-p)\,\vec r_\perp + \vec r_\parallel,
$$
so
$$
|\vec r'|^2 = (1-p)^2\,r_\perp^2 + r_\parallel^2 \leq r_\perp^2 + r_\parallel^2 = |\vec r|^2 ,
$$
with equality if and only if $p=0$, or $r_\perp = 0$ (the state already lies on the dephasing axis). The **purity**,
$$
\mathrm{Tr}(\tilde{Ϛ}^2) = \tfrac{1}{2}\left(1 + |\vec r|^2\right),
$$
therefore does not increase, and strictly decreases for any off-axis state when $p>0$.

**Entropy.** The eigenvalues of $\tilde{Ϛ}$ are $\lambda_\pm = \tfrac{1}{2}(1 \pm x)$ with $x = |\vec r|$, and
$$
S(x) = -\lambda_+\log\lambda_+ - \lambda_-\log\lambda_-
= -\frac{1+x}{2}\log\frac{1+x}{2} - \frac{1-x}{2}\log\frac{1-x}{2}.
$$
Differentiating,
$$
\frac{dS}{dx}
= -\frac{1}{2}\left(\log\frac{1+x}{2} + 1\right) + \frac{1}{2}\left(\log\frac{1-x}{2} + 1\right)
= \frac{1}{2}\log\frac{1-x}{1+x} \leq 0 \qquad (0 \leq x < 1),
$$
so $S$ is a decreasing function of $x$. Since $|\vec r'| \leq |\vec r|$,
$$
S(\tilde{Ϛ}') \geq S(\tilde{Ϛ}),
$$
with equality if and only if $p=0$ or the state is on the dephasing axis. Dephasing strictly increases the entropy of every off-axis state, for every $0 < p \leq 1$. This is consistent with the channel being unital: $\Phi(\tfrac{1}{2}e_t) = \tfrac{1}{2}e_t$, and unital channels are mixedness-increasing.

**Concrete case.** Take the pure state $\tilde{Ϛ} = \tilde\Pi_1(\vec e_x) = \tfrac{1}{2}(e_t + i\vec e_x)$, with $\vec r = (1,0,0)$, purity $1$, and entropy $0$. Dephase along $\vec e_z$ with $p = \tfrac{1}{2}$. Then $\vec r' = (\tfrac{1}{2},0,0)$, so $|\vec r'| = \tfrac{1}{2}$, the eigenvalues are $\lambda_\pm = \tfrac{3}{4}, \tfrac{1}{4}$, and
$$
S = -\tfrac{3}{4}\log\tfrac{3}{4} - \tfrac{1}{4}\log\tfrac{1}{4}
= \tfrac{3}{4}\log\tfrac{4}{3} + \tfrac{1}{4}\log 4 \approx 0.562335 \ \text{nats},
$$
while the purity falls to $\tfrac{1}{2}(1 + \tfrac{1}{4}) = \tfrac{5}{8} = 0.625$. At $p=1$ the Bloch vector collapses to the origin, the state becomes maximally mixed, and $S = \log 2 \approx 0.693147$ nats. The entropy rises monotonically from $0$ to $\log 2$ as $p$ runs from $0$ to $1$.

## Summary

We have worked six problems that exercise the channel formalism of the parent article in $\mathbb{M}_+$.

1. **Dephasing as a Kraus sum.** The channel $\Phi^{\mathrm{deph}}_p$ has Kraus operators $\sqrt{1-p}\,e_t$, $\sqrt{p}\,\tilde\Pi_1$, $\sqrt{p}\,\tilde\Pi_2$ and acts on the Bloch vector as $\vec r' = (1-p)\vec r + p(\vec u_x\cdot\vec r)\vec u_x$, scaling the transverse coherence by $1-p$ and leaving the populations fixed.
2. **Kraus rank.** The Choi matrix of dephasing has spectrum $\{2-p,\,p,\,0,\,0\}$; its rank is two for $0<p<2$, dropping to one at the endpoints $p=0$ and $p=2$. On the parent's physical range $0\le p\le1$ it is therefore two for every $p>0$. The minimal Kraus rank is two, not three: the three-operator representation of the parent is valid but non-minimal, and $\sqrt{1-\tfrac{p}{2}}\,e_t$, $\sqrt{\tfrac{p}{2}}\,i\vec u_x$ is a minimal set.
3. **Positive but not completely positive.** The transpose map acts on the Bloch ball as $(r_1,r_2,r_3)\mapsto(r_1,-r_2,r_3)$, is positive and trace preserving, and has Choi matrix equal to the swap operator, with spectrum $\{1,1,1,-1\}$. It is not a channel.
4. **Amplitude damping.** With $s=\sqrt{1-\gamma}$, the Kraus operators are $\tilde{K}_0 = \tfrac{1+s}{2}e_t + i\tfrac{1-s}{2}\vec e_z$ and $\tilde{K}_1 = \tfrac{\sqrt{\gamma}}{2}(i\vec e_x - \vec e_y)$; the channel is non-unital, has the unique fixed state $\tilde\Pi_1(\vec u_z)$, sends the excited state to $(0,0,2\gamma-1)$, and raises the purity of the maximally mixed state to $\tfrac{1}{2}(1+\gamma^2)$.
5. **Composition and rank.** Composing channels multiplies Kraus operators, $B_lA_m$, and the Kraus rank of a composition is at most the product of the ranks. Two dephasings compose to a dephasing along the common axis with $p' = p+q-pq$ when the axes are parallel, but to the rank-four completely depolarizing channel when they are orthogonal and full.
6. **Contraction and entropy.** Dephasing contracts the Bloch ball, $|\vec r'|^2 = (1-p)^2 r_\perp^2 + r_\parallel^2 \leq |\vec r|^2$, lowers the purity, and raises the entropy, since $dS/d|\vec r| = \tfrac{1}{2}\log\frac{1-|\vec r|}{1+|\vec r|} \leq 0$. For $\tilde\Pi_1(\vec e_x)$ dephased along $\vec e_z$ with $p=\tfrac{1}{2}$, the entropy rises from $0$ to $\approx 0.562335$ nats and the purity falls to $0.625$.

The two canonical channels illustrate the two faces of irreversibility. Dephasing is unital and destroys coherence without changing populations; amplitude damping is non-unital and drives the state toward a pure ground state. Both have Kraus rank two on their physical ranges ($0<p\le1$ for dephasing, $0<\gamma\le1$ for damping), both are irreversible there, and both are instances of the parent's dichotomy: reversible if and only if Kraus rank one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_+$ | Hermitian subspace (states, observables) |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\tilde{Ϛ} = \tfrac{1}{2}(e_t + i\vec r)$ | State; $\vec r$ the Bloch vector |
| $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$ | Trace |
| $\tilde\Pi_{1,2}(\vec u_x) = \tfrac{1}{2}(e_t \pm i\vec u_x)$ | Idempotents along $\vec u_x$ |
| $\Phi(\tilde{Q}) = \sum_l \tilde{K}_l\tilde{Q}\tilde{K}_l^{*}$ | Kraus representation |
| $\sum_l \tilde{K}_l^{*}\tilde{K}_l = e_t$ | Trace-preservation condition |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |
| $J(\Phi) = \sum_{jk}\tilde{E}_{jk}\otimes\Phi(\tilde{E}_{jk})$ | Choi matrix; Kraus rank $=\mathrm{rank}\,J$ |
| $\Phi^{\mathrm{deph}}_p$ | Dephasing channel along $\vec u_x$ |
| $\vec r \mapsto (1-p)\vec r + p(\vec u_x\cdot\vec r)\vec u_x$ | Dephasing Bloch map |
| $E_{jk} = \lvert j\rangle\langle k\rvert$ | Matrix units of the computational basis |
| $\gamma$ | Amplitude-damping parameter |
| $\mathrm{Tr}(\tilde{Ϛ}^2) = \tfrac{1}{2}(1+\lvert\vec r\rvert^2)$ | Purity |
| $S = -\lambda_+\log\lambda_+ - \lambda_-\log\lambda_-$ | von Neumann entropy |

## Further Reading

- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for quantum operations, the Kraus representation, the Choi matrix, and the depolarizing, dephasing, and amplitude-damping channels.
- K. Kraus, *States, Effects, and Operations* (Springer, 1983), for the original formulation of completely positive maps.
- M.-D. Choi, "Completely positive linear maps on complex matrices," *Linear Algebra and its Applications* **10** (1975) 285–290, for the complete-positivity criterion used in Problem 3.
- M. B. Ruskai, S. Szarek, and E. Werner, "An analysis of completely-positive trace-preserving maps on $2\times2$ matrices," *Linear Algebra and its Applications* **347** (2002) 159–187, for the affine Bloch-ball picture of qubit channels.
- The companion articles of this series: *Quantum Physics in Biquaternionic Form*, *Quantum Channels and the Reversible/Irreversible Dichotomy*, and the earlier exercises of this series.
