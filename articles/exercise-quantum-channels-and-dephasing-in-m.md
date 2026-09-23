# __Exercise: Quantum Channels and Dephasing in M+__

## Introduction

This is one of a series of **worked exercises** on quantum mechanics in the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$. Earlier exercises treated the kinematics of a qubit and of a pair of qubits; each was a single problem solved twice, once in the standard Hilbert-space formulation and once in the biquaternion formulation of the Hermitian subspace $\mathbb{M}_+$. This exercise is different in structure. Its parent is the article *Quantum Channels and the Reversible/Irreversible Dichotomy*, which develops the general state map on $\mathbb{M}_+$ — the quantum channel, its Kraus representation, complete positivity, the Choi matrix, and the reversible/irreversible dichotomy. The reader is assumed to have that formalism and is asked to apply it.

The article is therefore a sequence of independent problems, each in its own section. We work throughout in the notation of the parent, returning to the standard matrix formulation only where the parent itself does (the transpose map, the Choi matrix, and the standard Kraus operators of amplitude damping). The problems are:

1. Writing the dephasing channel as a Kraus sum and computing its action on a general Bloch vector.
2. Computing the Kraus rank of dephasing and finding a minimal Kraus representation.
3. Showing that the transpose map is positive but not completely positive.
4. The amplitude-damping channel: Kraus operators, fixed states, and purity.
5. Composition of channels, and the growth of the Kraus rank.
6. The Bloch-ball contraction and the increase of the von Neumann entropy under dephasing.

The conventions are those of the companion articles. The quaternion units are $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$; $i$ is the central scalar imaginary. The Hermitian subspace $\mathbb{M}_+$ consists of the elements $\tilde{H} = h_0 e_0 + i\mathbf{h}$ with real $h_0$ and $\mathbf{h} \in \mathbb{R}^3$. A state is $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$ with $|\mathbf{r}| \leq 1$, and $\mathbf{r}$ is its Bloch vector. The trace is $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$, so the Born rule is $\mathrm{Tr}(\tilde{\rho}\tilde{H}) = h_0 + \mathbf{r}\cdot\mathbf{h}$. A **channel** is a completely positive, trace-preserving map with a Kraus representation $\Phi(\tilde{X}) = \sum_l \tilde{K}_l\tilde{X}\tilde{K}_l^\dagger$ and normalization $\sum_l \tilde{K}_l^\dagger\tilde{K}_l = e_0$, and the Choi matrix is $J(\Phi) = \sum_{jk}\tilde{E}_{jk}\otimes\Phi(\tilde{E}_{jk})$ as in the parent. The dephasing channel along the unit pure real quaternion $\hat{\mathbf{n}}$ is
$$
\Phi^{\mathrm{deph}}_p(\tilde{\rho})
:= (1-p)\,\tilde{\rho}
+ p\left(\tilde{P}_+\,\tilde{\rho}\,\tilde{P}_+ + \tilde{P}_-\,\tilde{\rho}\,\tilde{P}_-\right),
\qquad
\tilde{P}_\pm(\hat{\mathbf{n}}) = \tfrac{1}{2}\left(e_0 \pm i\hat{\mathbf{n}}\right).
$$
Throughout, $\log$ denotes the natural logarithm.

## Problem 1: Dephasing as a Kraus Sum

**Problem.** Verify that the dephasing channel $\Phi^{\mathrm{deph}}_p$ is trace preserving with the three Kraus operators
$$
\tilde{K}_0 = \sqrt{1-p}\,e_0, \qquad \tilde{K}_1 = \sqrt{p}\,\tilde{P}_+(\hat{\mathbf{n}}), \qquad \tilde{K}_2 = \sqrt{p}\,\tilde{P}_-(\hat{\mathbf{n}}),
$$
and compute $\Phi^{\mathrm{deph}}_p(\tilde{\rho})$ for the general state $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$.

**Solution.** Put $\alpha = i\hat{\mathbf{n}}$, so that $\tilde{P}_\pm = \tfrac{1}{2}(e_0 \pm \alpha)$. Since $\hat{\mathbf{n}}^2 = -e_0$,
$$
\alpha^2 = (i\hat{\mathbf{n}})^2 = i^2\hat{\mathbf{n}}^2 = (-1)(-e_0) = e_0,
\qquad
\alpha^\dagger = (i\hat{\mathbf{n}})^\dagger = -i\,\hat{\mathbf{n}}^\dagger = -i(-\hat{\mathbf{n}}) = \alpha,
$$
so $\alpha^2 = e_0$ and $\alpha$ is Hermitian, as the idempotent structure requires. Trace preservation is immediate: because $\tilde{P}_\pm$ are Hermitian idempotents, $\tilde{K}_1^\dagger\tilde{K}_1 = p\,\tilde{P}_+$ and $\tilde{K}_2^\dagger\tilde{K}_2 = p\,\tilde{P}_-$, whence
$$
\tilde{K}_0^\dagger\tilde{K}_0 + \tilde{K}_1^\dagger\tilde{K}_1 + \tilde{K}_2^\dagger\tilde{K}_2
= (1-p)\,e_0 + p\,(\tilde{P}_+ + \tilde{P}_-) = e_0 .
$$

For the action on the state, use the elementary identity
$$
\tilde{P}_+\,\tilde{X}\,\tilde{P}_+ + \tilde{P}_-\,\tilde{X}\,\tilde{P}_-
= \tfrac{1}{2}\left(\tilde{X} + \alpha\,\tilde{X}\,\alpha\right),
$$
valid for every $\tilde{X} \in \mathbb{B}$: the cross terms come with opposite signs,
$$
\tfrac{1}{4}\left(e_0 \pm \alpha\right)\tilde{X}\left(e_0 \pm \alpha\right)
= \tfrac{1}{4}\left(\tilde{X} \pm \alpha\tilde{X} \pm \tilde{X}\alpha + \alpha\tilde{X}\alpha\right),
$$
and cancel in the sum. The two products needed are
$$
\alpha\,e_0\,\alpha = \alpha^2 = e_0, \qquad
\alpha\,(i\mathbf{r})\,\alpha = i^3\,\hat{\mathbf{n}}\,\mathbf{r}\,\hat{\mathbf{n}} = -i\,\hat{\mathbf{n}}\,\mathbf{r}\,\hat{\mathbf{n}} .
$$
For the second we use the quaternion identity
$$
\hat{\mathbf{n}}\,\mathbf{r}\,\hat{\mathbf{n}} = \mathbf{r} - 2(\hat{\mathbf{n}}\cdot\mathbf{r})\,\hat{\mathbf{n}} .
$$
*Proof:* decompose $\mathbf{r} = \mathbf{r}_\parallel + \mathbf{r}_\perp$ with $\mathbf{r}_\parallel = (\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}}$ and $\mathbf{r}_\perp \perp \hat{\mathbf{n}}$. Then $\hat{\mathbf{n}}\,\mathbf{r}_\parallel\,\hat{\mathbf{n}} = (\hat{\mathbf{n}}\cdot\mathbf{r})\,\hat{\mathbf{n}}^3 = -(\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}} = -\mathbf{r}_\parallel$, because $\hat{\mathbf{n}}^3 = \hat{\mathbf{n}}\hat{\mathbf{n}}^2 = -\hat{\mathbf{n}}$; and for the orthogonal part $\hat{\mathbf{n}}\,\mathbf{r}_\perp = \hat{\mathbf{n}}\times\mathbf{r}_\perp$, so $\hat{\mathbf{n}}\,\mathbf{r}_\perp\,\hat{\mathbf{n}} = (\hat{\mathbf{n}}\times\mathbf{r}_\perp)\times\hat{\mathbf{n}} = \mathbf{r}_\perp$. Summing gives the identity. Therefore
$$
\alpha\,\tilde{\rho}\,\alpha
= \tfrac{1}{2}\left(e_0 - i\,\hat{\mathbf{n}}\,\mathbf{r}\,\hat{\mathbf{n}}\right)
= \tfrac{1}{2}\left(e_0 - i\mathbf{r} + 2i(\hat{\mathbf{n}}\cdot\mathbf{r})\,\hat{\mathbf{n}}\right),
$$
and hence
$$
\tilde{P}_+\tilde{\rho}\tilde{P}_+ + \tilde{P}_-\tilde{\rho}\tilde{P}_-
= \tfrac{1}{2}\left(\tilde{\rho} + \alpha\tilde{\rho}\alpha\right)
= \tfrac{1}{2}\left(e_0 + i(\hat{\mathbf{n}}\cdot\mathbf{r})\,\hat{\mathbf{n}}\right).
$$
Combining with the mixture,
$$
\boxed{\;\Phi^{\mathrm{deph}}_p(\tilde{\rho}) = \tfrac{1}{2}\left(e_0 + i\,\mathbf{r}'\right),
\qquad
\mathbf{r}' = (1-p)\,\mathbf{r} + p\,(\hat{\mathbf{n}}\cdot\mathbf{r})\,\hat{\mathbf{n}}.\;}
$$
The transverse components of the Bloch vector are multiplied by $1-p$, while the longitudinal component is untouched. At $p=0$ the channel is the identity; at $p=1$ it is the projection $\mathbf{r} \mapsto (\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}}$, the "measure-and-forget" channel of the parent.

**Special case $\hat{\mathbf{n}} = e_3$.** The Kraus operators are $\tilde{K}_0 = \sqrt{1-p}\,e_0$, $\tilde{K}_1 = \tfrac{1}{2}\sqrt{p}\,(e_0 + ie_3)$, $\tilde{K}_2 = \tfrac{1}{2}\sqrt{p}\,(e_0 - ie_3)$, and the Bloch map is $\mathbf{r}' = (1-p)(r_1 e_1 + r_2 e_2) + r_3 e_3$.

## Problem 2: The Kraus Rank of Dephasing

**Problem.** Compute the Choi matrix of $\Phi^{\mathrm{deph}}_p$ in the computational basis and determine its rank. Deduce the minimal Kraus rank, exhibit a minimal Kraus representation, and decide whether the three-operator representation of Problem 1 is minimal.

**Solution.** The rank of the Choi matrix is invariant under unitary conjugation, and dephasing along any unit axis is unitarily equivalent to dephasing along $e_3$; we therefore fix $\hat{\mathbf{n}} = e_3$. Let $E_{jk} = |j\rangle\langle k|$ be the matrix units of the computational basis, expressed in the algebra as
$$
E_{00} = \tfrac{1}{2}(e_0 + ie_3), \quad
E_{11} = \tfrac{1}{2}(e_0 - ie_3), \quad
E_{01} = \tfrac{1}{2}(ie_1 - e_2), \quad
E_{10} = \tfrac{1}{2}(ie_1 + e_2).
$$
These are the elements the parent denotes $\tilde{E}_{jk}$; they satisfy $\mathrm{Tr}(E_{jk}E_{lm}) = \delta_{kl}\delta_{jm}$. The idempotents $\tilde{P}_\pm = \tfrac{1}{2}(e_0 \pm ie_3)$ are exactly $E_{00}$ and $E_{11}$. Since dephasing fixes the populations and scales the coherences by $1-p$,
$$
\Phi(E_{00}) = E_{00}, \qquad \Phi(E_{11}) = E_{11}, \qquad \Phi(E_{01}) = (1-p)\,E_{01}, \qquad \Phi(E_{10}) = (1-p)\,E_{10},
$$
the off-diagonal statement following because $\tilde{P}_\pm E_{01}\tilde{P}_\pm = 0$. With the parent's convention $J(\Phi) = \sum_{jk}E_{jk}\otimes\Phi(E_{jk})$ and the product basis $(|00\rangle,|01\rangle,|10\rangle,|11\rangle)$,
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
\tilde{K}_0 = \sqrt{1-\tfrac{p}{2}}\;e_0, \qquad \tilde{K}_1 = \sqrt{\tfrac{p}{2}}\;i\hat{\mathbf{n}} .
$$
At $p=2$ the first operator vanishes, $\tilde{K}_0=0$, and the pair collapses to the single operator $\tilde{K}_1=i\hat{\mathbf{n}}$, which is unitary; that endpoint lies outside the parent's physical range $0\le p\le 1$.

Trace preservation holds because $(i\hat{\mathbf{n}})^\dagger(i\hat{\mathbf{n}}) = (i\hat{\mathbf{n}})^2 = i^2\hat{\mathbf{n}}^2 = e_0$, so $\tilde{K}_0^\dagger\tilde{K}_0 + \tilde{K}_1^\dagger\tilde{K}_1 = (1-\tfrac{p}{2})e_0 + \tfrac{p}{2}e_0 = e_0$. The action is
$$
\Phi(\tilde{\rho}) = \left(1-\tfrac{p}{2}\right)\tilde{\rho} + \tfrac{p}{2}\,(i\hat{\mathbf{n}})\,\tilde{\rho}\,(i\hat{\mathbf{n}}).
$$
Since $(i\hat{\mathbf{n}})\tilde{\rho}(i\hat{\mathbf{n}}) = -\hat{\mathbf{n}}\tilde{\rho}\hat{\mathbf{n}} = \tfrac{1}{2}\left(e_0 - i\mathbf{r} + 2i(\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}}\right)$, this reproduces $\mathbf{r}' = (1-p)\mathbf{r} + p(\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}}$, as required.

**Conclusion.** The three-operator representation of Problem 1 is valid but **not minimal**: for $0<p<1$ the span of $\{\tilde{K}_0,\tilde{K}_1,\tilde{K}_2\}$ is two-dimensional, since $\tilde{K}_0 = \sqrt{1-p}\,(\tilde{P}_+ + \tilde{P}_-)$. The minimal representation given above has two operators. Consistently with the parent's dichotomy, dephasing has Kraus rank one at $p=0$ (the identity) and Kraus rank two for $0<p\le1$, and is therefore irreversible throughout the physical range except at its identity endpoint. The formal continuation to $p\in(1,2]$ is completely positive but leaves that range, and at $p=2$ it degenerates: $\tilde{K}_0=0$ and the channel reduces to the unitary conjugation $\tilde{\rho}\mapsto(i\hat{\mathbf{n}})\tilde{\rho}(i\hat{\mathbf{n}})^\dagger$, of Kraus rank one and reversible.

## Problem 3: A Positive Map That Is Not Completely Positive

**Problem.** In the matrix representative of $\mathbb{B}$, let $\Phi_T$ be the transpose, $\Phi_T(\tilde{X}) = \tilde{X}^{\mathsf{T}}$. Show that $\Phi_T$ is positive and trace preserving, but not completely positive.

**Solution.** On the matrix units $\Phi_T$ acts by $E_{jk} \mapsto E_{kj}$; equivalently, on a state,
$$
\Phi_T\!\left(\tfrac{1}{2}(e_0 + i\mathbf{r})\right) = \tfrac{1}{2}\left(e_0 + i(r_1 e_1 - r_2 e_2 + r_3 e_3)\right),
$$
because $\sigma_1$ and $\sigma_3$ are real while $\sigma_2$ is imaginary. So $\Phi_T$ acts on the Bloch ball by the reflection
$$
(r_1, r_2, r_3) \longmapsto (r_1, -r_2, r_3).
$$
This map is **trace preserving** (the transpose fixes $e_0$ and preserves the trace) and **positive**: the reflection is an isometry of $\mathbb{R}^3$ that maps the ball $|\mathbf{r}|\leq 1$ onto itself, so it maps states to states.

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
Writing $s = \sqrt{1-\gamma} \in [0,1]$ and using $\sigma_3 = ie_3$ and $|0\rangle\langle 1| = \tfrac{1}{2}(ie_1 - e_2)$, these translate to
$$
\tilde{K}_0 = \frac{1+s}{2}\,e_0 + i\,\frac{1-s}{2}\,e_3 \;\in \mathbb{M}_+,
\qquad
\tilde{K}_1 = \frac{\sqrt{\gamma}}{2}\left(i e_1 - e_2\right) \in \mathbb{B}.
$$
Here $\tilde{K}_0$ is Hermitian (it is an element of $\mathbb{M}_+$), while $\tilde{K}_1$ is not. Trace preservation follows from
$$
\tilde{K}_0^\dagger\tilde{K}_0 = \frac{1+s^2}{2}\,e_0 + i\,\frac{1-s^2}{2}\,e_3,
\qquad
\tilde{K}_1^\dagger\tilde{K}_1 = \frac{\gamma}{2}\left(e_0 - ie_3\right),
$$
whose sum is $e_0$, since $1 + s^2 + \gamma = 2$ and $1 - s^2 - \gamma = 0$. A direct quaternion expansion of $\tilde{K}_0\tilde{\rho}\tilde{K}_0^\dagger + \tilde{K}_1\tilde{\rho}\tilde{K}_1^\dagger$ for $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$ gives $\tfrac{1}{2}(e_0 + i\mathbf{r}')$ with exactly the Bloch map stated above; the $\tilde{K}_1$ term contributes the population $\tfrac{\gamma}{4}(1-r_3)(e_0 + ie_3)$ that is transferred to the ground state.

**Fixed states.** Set $r_1 = r_2 = 0$ and $z = \gamma + (1-\gamma)z$, giving $z = 1$. For every $\gamma>0$ the channel has the **unique** fixed state
$$
\tilde{\rho}_* = \tfrac{1}{2}\left(e_0 + ie_3\right) = \tilde{P}_+(\hat{\mathbf{z}}),
$$
the pure ground state. For $\gamma = 0$ the channel is the identity and every state is fixed.

**Non-unitality.** The channel does not fix the maximally mixed state:
$$
\Phi\left(\tfrac{1}{2}e_0\right) = \tfrac{1}{2}\left(e_0 + i\gamma e_3\right) \neq \tfrac{1}{2}e_0 .
$$
The center of the Bloch ball is moved to the Bloch vector $(0,0,\gamma)$. This is the structural difference from dephasing, which is unital.

**Ground and excited states.** The ground state $\mathbf{r} = (0,0,1)$ is fixed, as noted. The excited state $\mathbf{r} = (0,0,-1)$ is mapped to
$$
\mathbf{r}' = \left(0,\,0,\,\gamma - (1-\gamma)\right) = \left(0,\,0,\,2\gamma - 1\right).
$$
At $\gamma = \tfrac{1}{2}$ the excited state is driven to the **maximally mixed state** $(0,0,0)$; at $\gamma = 1$ it reaches the ground state. This is the standard incoherent decay of the excited state.

**Purity.** For a general input,
$$
\mathrm{Tr}\!\left(\tilde{\rho}'^2\right) = \tfrac{1}{2}\left(1 + (1-\gamma)\left(r_1^2 + r_2^2\right) + \left(\gamma + (1-\gamma)r_3\right)^2\right).
$$
For the maximally mixed input ($\mathbf{r} = 0$) the purity rises from $\tfrac{1}{2}$ to $\tfrac{1}{2}(1+\gamma^2) \geq \tfrac{1}{2}$: amplitude damping *purifies* the maximally mixed state by driving it toward the pure ground state. This is possible precisely because the channel is non-unital, and it is the opposite of the behaviour of dephasing. For the excited input $\mathbf{r} = (0,0,-1)$ the output purity is $\tfrac{1}{2}(1 + (2\gamma-1)^2)$, which is $\tfrac{1}{2}$ at $\gamma = \tfrac{1}{2}$ — the maximally mixed value — and rises to $1$ at $\gamma = 1$. Finally, the Choi rank of the channel is two for $\gamma>0$ (one at $\gamma=0$), so it is irreversible for every $\gamma>0$.

## Problem 5: Composition of Channels and the Growth of Kraus Rank

**Problem.** Let $\Phi_1$ have Kraus operators $\{A_m\}_{m=1}^{n_1}$ and $\Phi_2$ have Kraus operators $\{B_l\}_{l=1}^{n_2}$. Show that $\Phi_2\circ\Phi_1$ has Kraus operators $\{B_l A_m\}$ and deduce that $\mathrm{rank}(\Phi_2\circ\Phi_1) \leq \mathrm{rank}(\Phi_1)\,\mathrm{rank}(\Phi_2)$. Then compose two dephasing channels and determine the resulting Kraus rank.

**Solution.** Composing,
$$
\Phi_2\!\left(\Phi_1(\tilde{X})\right)
= \sum_l B_l\left(\sum_m A_m\tilde{X}A_m^\dagger\right)B_l^\dagger
= \sum_{l,m}\left(B_l A_m\right)\tilde{X}\left(B_l A_m\right)^\dagger ,
$$
so $\{B_l A_m\}$ is a Kraus set for the composite, and it is trace preserving whenever both factors are. The Kraus rank of the composite is the dimension of the span of the products $B_l A_m$, which cannot exceed the product of the dimensions of the individual spans; hence $\mathrm{rank}(\Phi_2\circ\Phi_1) \leq \mathrm{rank}(\Phi_1)\,\mathrm{rank}(\Phi_2)$. For a qubit the composite has rank at most $4$, since its Choi matrix is $4\times4$.

**Composition of dephasings.** The Bloch map of $\Phi^{\mathrm{deph}}_p$ along $\hat{\mathbf{n}}$ is the linear map $D(\hat{\mathbf{n}},p) = (1-p)I + p\,\hat{\mathbf{n}}\hat{\mathbf{n}}^{\mathsf{T}}$ acting on $\mathbb{R}^3$. Composing two of them,
$$
D(\hat{\mathbf{m}},q)\,D(\hat{\mathbf{n}},p)
= (1-p)(1-q)\,I
+ p(1-q)\,\hat{\mathbf{n}}\hat{\mathbf{n}}^{\mathsf{T}}
+ q(1-p)\,\hat{\mathbf{m}}\hat{\mathbf{m}}^{\mathsf{T}}
+ pq\,(\hat{\mathbf{m}}\cdot\hat{\mathbf{n}})\,\hat{\mathbf{m}}\hat{\mathbf{n}}^{\mathsf{T}} .
$$
For **parallel axes**, $\hat{\mathbf{m}} = \hat{\mathbf{n}}$, the projector identity $\hat{\mathbf{n}}\hat{\mathbf{n}}^{\mathsf{T}}\hat{\mathbf{n}}\hat{\mathbf{n}}^{\mathsf{T}} = \hat{\mathbf{n}}\hat{\mathbf{n}}^{\mathsf{T}}$ collapses the sum to
$$
D(\hat{\mathbf{n}},q)\,D(\hat{\mathbf{n}},p) = D(\hat{\mathbf{n}},\,p+q-pq),
$$
so the composite is again a dephasing channel, with effective parameter $p' = p+q-pq$; its Kraus rank is at most two.

For **orthogonal axes and full dephasing**, take $\hat{\mathbf{n}} = e_3$, $\hat{\mathbf{m}} = e_1$ and $p = q = 1$. Then $D(e_3,1) = e_3e_3^{\mathsf{T}}$, $D(e_1,1) = e_1e_1^{\mathsf{T}}$, and
$$
D(e_1,1)\,D(e_3,1) = e_1\left(e_1^{\mathsf{T}}e_3\right)e_3^{\mathsf{T}} = 0 .
$$
The composite is the **completely depolarizing channel**, $\tilde{\rho} \mapsto \tfrac{1}{2}e_0$ for every state: every Bloch vector is sent to the origin. Its Choi matrix is
$$
J = \sum_{jk} E_{jk}\otimes\Phi(E_{jk}) = \sum_{k} E_{kk}\otimes \tfrac{1}{2}e_0 = \tfrac{1}{2}I_4,
$$
of rank four. Thus composing two rank-two channels produces a rank-four channel, saturating the qubit bound $4 = 2\times 2$. More generally, for two distinct axes and $0<p,q<1$ the composite also saturates the bound and has Kraus rank four (checked numerically over the parameter range); the rank drops to two only when the axes are parallel or one of the channels is trivial.

## Problem 6: Bloch-Ball Contraction and the Increase of Entropy

**Problem.** Show that dephasing contracts the Bloch ball, $|\mathbf{r}'| \leq |\mathbf{r}|$, that it does not increase the purity, and that it does not decrease the von Neumann entropy. Evaluate a concrete case.

**Solution.** Decompose $\mathbf{r} = \mathbf{r}_\parallel + \mathbf{r}_\perp$ with $\mathbf{r}_\parallel = (\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}}$ and $\mathbf{r}_\perp \perp \hat{\mathbf{n}}$. From the Bloch map,
$$
\mathbf{r}' = (1-p)\mathbf{r} + p(\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}} = (1-p)\,\mathbf{r}_\perp + \mathbf{r}_\parallel,
$$
so
$$
|\mathbf{r}'|^2 = (1-p)^2\,r_\perp^2 + r_\parallel^2 \leq r_\perp^2 + r_\parallel^2 = |\mathbf{r}|^2 ,
$$
with equality if and only if $p=0$ or $r_\perp = 0$ (the state already lies on the dephasing axis). The **purity**,
$$
\mathrm{Tr}(\tilde{\rho}^2) = \tfrac{1}{2}\left(1 + |\mathbf{r}|^2\right),
$$
therefore does not increase, and strictly decreases for any off-axis state when $p>0$.

**Entropy.** The eigenvalues of $\tilde{\rho}$ are $\lambda_\pm = \tfrac{1}{2}(1 \pm x)$ with $x = |\mathbf{r}|$, and
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
so $S$ is a decreasing function of $x$. Since $|\mathbf{r}'| \leq |\mathbf{r}|$,
$$
S(\tilde{\rho}') \geq S(\tilde{\rho}),
$$
with equality if and only if $p=0$ or the state is on the dephasing axis. Dephasing strictly increases the entropy of every off-axis state, for every $0 < p \leq 1$. This is consistent with the channel being unital: $\Phi(\tfrac{1}{2}e_0) = \tfrac{1}{2}e_0$, and unital channels are mixedness-increasing.

**Concrete case.** Take the pure state $\tilde{\rho} = \tilde{P}_+(e_1) = \tfrac{1}{2}(e_0 + ie_1)$, with $\mathbf{r} = (1,0,0)$, purity $1$, and entropy $0$. Dephase along $e_3$ with $p = \tfrac{1}{2}$. Then $\mathbf{r}' = (\tfrac{1}{2},0,0)$, so $|\mathbf{r}'| = \tfrac{1}{2}$, the eigenvalues are $\lambda_\pm = \tfrac{3}{4}, \tfrac{1}{4}$, and
$$
S = -\tfrac{3}{4}\log\tfrac{3}{4} - \tfrac{1}{4}\log\tfrac{1}{4}
= \tfrac{3}{4}\log\tfrac{4}{3} + \tfrac{1}{4}\log 4 \approx 0.562335 \ \text{nats},
$$
while the purity falls to $\tfrac{1}{2}(1 + \tfrac{1}{4}) = \tfrac{5}{8} = 0.625$. At $p=1$ the Bloch vector collapses to the origin, the state becomes maximally mixed, and $S = \log 2 \approx 0.693147$ nats. The entropy rises monotonically from $0$ to $\log 2$ as $p$ runs from $0$ to $1$.

## Summary

We have worked six problems that exercise the channel formalism of the parent article in $\mathbb{M}_+$.

1. **Dephasing as a Kraus sum.** The channel $\Phi^{\mathrm{deph}}_p$ has Kraus operators $\sqrt{1-p}\,e_0$, $\sqrt{p}\,\tilde{P}_+$, $\sqrt{p}\,\tilde{P}_-$ and acts on the Bloch vector as $\mathbf{r}' = (1-p)\mathbf{r} + p(\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}}$, scaling the transverse coherence by $1-p$ and leaving the populations fixed.
2. **Kraus rank.** The Choi matrix of dephasing has spectrum $\{2-p,\,p,\,0,\,0\}$; its rank is two for $0<p<2$, dropping to one at the endpoints $p=0$ and $p=2$. On the parent's physical range $0\le p\le1$ it is therefore two for every $p>0$. The minimal Kraus rank is two, not three: the three-operator representation of the parent is valid but non-minimal, and $\sqrt{1-\tfrac{p}{2}}\,e_0$, $\sqrt{\tfrac{p}{2}}\,i\hat{\mathbf{n}}$ is a minimal set.
3. **Positive but not completely positive.** The transpose map acts on the Bloch ball as $(r_1,r_2,r_3)\mapsto(r_1,-r_2,r_3)$, is positive and trace preserving, and has Choi matrix equal to the swap operator, with spectrum $\{1,1,1,-1\}$. It is not a channel.
4. **Amplitude damping.** With $s=\sqrt{1-\gamma}$, the Kraus operators are $\tilde{K}_0 = \tfrac{1+s}{2}e_0 + i\tfrac{1-s}{2}e_3$ and $\tilde{K}_1 = \tfrac{\sqrt{\gamma}}{2}(ie_1 - e_2)$; the channel is non-unital, has the unique fixed state $\tilde{P}_+(\hat{\mathbf{z}})$, sends the excited state to $(0,0,2\gamma-1)$, and raises the purity of the maximally mixed state to $\tfrac{1}{2}(1+\gamma^2)$.
5. **Composition and rank.** Composing channels multiplies Kraus operators, $B_lA_m$, and the Kraus rank of a composition is at most the product of the ranks. Two dephasings compose to a dephasing along the common axis with $p' = p+q-pq$ when the axes are parallel, but to the rank-four completely depolarizing channel when they are orthogonal and full.
6. **Contraction and entropy.** Dephasing contracts the Bloch ball, $|\mathbf{r}'|^2 = (1-p)^2 r_\perp^2 + r_\parallel^2 \leq |\mathbf{r}|^2$, lowers the purity, and raises the entropy, since $dS/d|\mathbf{r}| = \tfrac{1}{2}\log\frac{1-|\mathbf{r}|}{1+|\mathbf{r}|} \leq 0$. For $\tilde{P}_+(e_1)$ dephased along $e_3$ with $p=\tfrac{1}{2}$, the entropy rises from $0$ to $\approx 0.562335$ nats and the purity falls to $0.625$.

The two canonical channels illustrate the two faces of irreversibility. Dephasing is unital and destroys coherence without changing populations; amplitude damping is non-unital and drives the state toward a pure ground state. Both have Kraus rank two on their physical ranges ($0<p\le1$ for dephasing, $0<\gamma\le1$ for damping), both are irreversible there, and both are instances of the parent's dichotomy: reversible if and only if Kraus rank one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_+$ | Hermitian subspace (states, observables) |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\tilde{\rho} = \tfrac{1}{2}(e_0 + i\mathbf{r})$ | State; $\mathbf{r}$ the Bloch vector |
| $\mathrm{Tr}(\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{Q})$ | Trace |
| $\tilde{P}_\pm(\hat{\mathbf{n}}) = \tfrac{1}{2}(e_0 \pm i\hat{\mathbf{n}})$ | Idempotents along $\hat{\mathbf{n}}$ |
| $\Phi(\tilde{X}) = \sum_l \tilde{K}_l\tilde{X}\tilde{K}_l^\dagger$ | Kraus representation |
| $\sum_l \tilde{K}_l^\dagger\tilde{K}_l = e_0$ | Trace-preservation condition |
| $J(\Phi) = \sum_{jk}\tilde{E}_{jk}\otimes\Phi(\tilde{E}_{jk})$ | Choi matrix; Kraus rank $=\mathrm{rank}\,J$ |
| $\Phi^{\mathrm{deph}}_p$ | Dephasing channel along $\hat{\mathbf{n}}$ |
| $\mathbf{r} \mapsto (1-p)\mathbf{r} + p(\hat{\mathbf{n}}\cdot\mathbf{r})\hat{\mathbf{n}}$ | Dephasing Bloch map |
| $E_{jk} = \lvert j\rangle\langle k\rvert$ | Matrix units of the computational basis |
| $\gamma$ | Amplitude-damping parameter |
| $\mathrm{Tr}(\tilde{\rho}^2) = \tfrac{1}{2}(1+\lvert\mathbf{r}\rvert^2)$ | Purity |
| $S = -\lambda_+\log\lambda_+ - \lambda_-\log\lambda_-$ | von Neumann entropy |

## Further Reading

- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for quantum operations, the Kraus representation, the Choi matrix, and the depolarizing, dephasing, and amplitude-damping channels.
- K. Kraus, *States, Effects, and Operations* (Springer, 1983), for the original formulation of completely positive maps.
- M.-D. Choi, "Completely positive linear maps on complex matrices," *Linear Algebra and its Applications* **10** (1975) 285–290, for the complete-positivity criterion used in Problem 3.
- M. B. Ruskai, S. Szarek, and E. Werner, "An analysis of completely-positive trace-preserving maps on $2\times2$ matrices," *Linear Algebra and its Applications* **347** (2002) 159–187, for the affine Bloch-ball picture of qubit channels.
- The companion articles of this series: *Quantum Mechanics in Biquaternionic Form*, *Quantum Channels and the Reversible/Irreversible Dichotomy*, and the earlier exercises of this series.
