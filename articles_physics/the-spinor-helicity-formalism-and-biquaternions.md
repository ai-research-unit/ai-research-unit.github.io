# __The Spinor-Helicity Formalism and Biquaternions__

## Introduction

The **spinor-helicity formalism** is the rewriting of massless relativistic kinematics in terms of two-component Weyl spinors. A massless four-momentum is not treated as a four-vector but as a product of two spinors,

$$
p_{\alpha\dot\beta} \;=\; \lambda_\alpha\,\tilde\lambda_{\dot\beta},
$$

and every Lorentz-invariant contraction of momenta becomes a product of two brackets,

$$
\langle ij\rangle \;=\; \lambda_i^\alpha\lambda_{j\alpha} \;=\; -\langle ji\rangle,
\qquad
[ij] \;=\; \tilde\lambda_i^{\dot\alpha}\tilde\lambda_{j\dot\alpha} \;=\; -[ji].
$$

Scattering amplitudes of massless particles are rational functions of these brackets. The simplest is the **Parke–Taylor** formula for the maximally helicity-violating gluon amplitude, a ratio of brackets whose little-group weights encode the helicities of the external particles [Parke and Taylor 1986; Elvang and Huang 2015; Dixon 2014]. The formalism is standard.

This article places it inside the biquaternion framework $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ of the companion articles, and the claim is stronger than an analogy. The framework already contains a statement that is *equivalent* to the spinor-helicity factorisation: **a nonzero biquaternion whose norm form vanishes is a zero divisor, and under the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ it is exactly a rank-one matrix.** A rank-one $2\times2$ matrix is an outer product of two spinors. A massless momentum has vanishing norm form. Therefore a massless momentum *is* a rank-one biquaternion, and its rank-one factorisation *is* the spinor-helicity factorisation $p = \lambda\tilde\lambda$. The identification is not an analogy, and it needs no new postulate: both sides are the same statement about the same matrix.

The division between what is established, what is transcribed, and what is left open is stated at the outset and kept explicit.

- **Established, and recomputed below.** A null momentum $\tilde P \in \mathbb{M}_-$ is a nonzero zero divisor, $N(\tilde P) = 0$ with $\tilde P \neq 0$; under $\Phi$ its image is a rank-one, anti-Hermitian matrix, and the rank-one factorisation $\Phi(\tilde P) = \lambda\tilde\lambda^{T}$ is the spinor-helicity factorisation. The angle and square brackets are the framework's invariant symplectic pairing $\varepsilon$ applied to the two factors, and they are antisymmetric by the antisymmetry of $\varepsilon$. The little-group scaling $\lambda\to t\lambda$, $\tilde\lambda\to t^{-1}\tilde\lambda$ is exactly the one-parameter freedom in the rank-one factorisation, and it leaves the momentum invariant; helicity is the weight of its compact $U(1)$ part. A massless momentum is *singular* in the factorisation sense: it is not invertible, whereas a massive one is.
- **Standard, transcribed.** The Parke–Taylor formula, the little-group weights of the external states, and the identification of helicity with the little-group weight are standard amplitude results. The framework reproduces the kinematic scaffolding — the factorisation, the brackets, the little-group action, the weights — and the weight of the Parke–Taylor amplitude is checked here on concrete cases; the formula itself and the color structure of the gauge theory are not derived from $\mathbb{B}$.
- **Gap, left visible.** The framework does not derive amplitudes, does not supply a colored gauge theory, and does not by itself distinguish the real material slice $\mathbb{M}_-$ from the complexified algebra $\mathbb{B}$. The general spinor-helicity variables with independent complex $\lambda,\tilde\lambda$ describe *complexified* momenta, which lie in the complexified four-vector representation carried by $\mathbb{B}$ rather than on the real slice $\mathbb{M}_-$; the real slice imposes the reality condition $\tilde\lambda \sim \lambda^{*}$ and reduces the little group to $U(1)$. The massless limit is singular and is treated as such, not by continuity: massive momenta are invertible and have no rank-one factorisation.

The article is organized as follows. The next section identifies the massless momentum as a zero divisor and shows its image is rank one. The section after that turns rank one into the factorisation and identifies it with spinor helicity. A section derives the brackets as the invariant symplectic pairing and records the one identity that links them to the momenta. The following section treats the little group, the reality condition, and helicity as its weight. A section states the Parke–Taylor formula and checks its little-group weights on concrete cases. The next section shows that the massless limit is singular. A section separates what the algebra supplies from what it only transcribes, and a short section records the gaps. The article closes with open questions.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$, and $i$ is the scalar imaginary, $i^2 = -1$, commuting with every $e_k$. The conjugations are the quaternion conjugate $\bar{\tilde Q}$, the complex conjugate $\tilde Q^{*}$, and the Hermitian conjugate $\tilde Q^\dagger = \bar{\tilde Q}^{\,*}$. The subspaces are $\mathbb{M}_- = \{\tilde Q : \tilde Q^\dagger = -\tilde Q\}$ (material, anti-Hermitian), $\mathbb{M}_+ = \{\tilde Q : \tilde Q^\dagger = \tilde Q\}$ (informational, Hermitian), $\mathbb{H}_{\mathbb{B}}$ (real quaternions), and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_\mathbb{R}\{e_0, ie_0\}$ (the centre). The matrix realization is

$$
\Phi:\;\tilde Q = \sum_{\mu=0}^{3}Q_\mu e_\mu \;\longmapsto\;
\begin{pmatrix}
Q_0 - iQ_3 & -iQ_1 - Q_2\\[2pt]
-iQ_1 + Q_2 & Q_0 + iQ_3
\end{pmatrix},
\qquad
\Phi(e_0)=I_2,\quad \Phi(e_k)=-i\sigma_k,\quad \Phi(i)=iI_2,
$$

satisfying $\Phi(\tilde Q\tilde R) = \Phi(\tilde Q)\Phi(\tilde R)$, $\det\Phi(\tilde Q) = N(\tilde Q) = \tilde Q\bar{\tilde Q} = \sum_\mu Q_\mu^2$, and $\Phi(\tilde Q^\dagger) = \Phi(\tilde Q)^\dagger$. The **spinor module** is $S = \mathbb{C}^2$, the unique simple left $\mathbb{B}$-module, with its conjugate module $\bar S$; the invariant symplectic pairing is $\varepsilon(\psi,\phi) = \psi^{T}\epsilon\,\phi$ with $\epsilon = \left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$. The four-momentum is $\tilde P = iE/c\,e_0 + \mathbf p \in \mathbb{M}_-$, with norm form $N(\tilde P) = -E^2/c^2 + \mathbf p^2 = -m^2c^2$ on the mass shell, and $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium. The trace formula $\mathrm{Tr}(\tilde P\tilde H) = 2\,\mathrm{Sc}(\tilde P\tilde H)$ is inherited unchanged.

## The Massless Momentum as a Zero Divisor

The zero divisors of $\mathbb{B}$ are characterized by the norm form: a nonzero biquaternion $\tilde Q$ is a zero divisor if and only if $N(\tilde Q) = 0$ (*Biquaternion Zero Divisors*). Equivalently, because the norm form is the determinant of the matrix realization, the nonzero zero divisors are exactly the rank-one elements of $M_2(\mathbb{C})$.

The four-momentum of a particle of mass $m$ is

$$
\tilde P \;=\; \frac{iE}{c}\,e_0 + \mathbf p, \qquad \mathbf p = p_1 e_1 + p_2 e_2 + p_3 e_3,
$$

an element of $\mathbb{M}_-$: its scalar part is purely imaginary and its vector part is real. Its norm form is

$$
N(\tilde P) \;=\; \tilde P\bar{\tilde P} \;=\; -\frac{E^2}{c^2} + \mathbf p^2 \;=\; -m^2c^2 .
$$

Two consequences follow immediately.

**A massless momentum has vanishing norm form.** For $m = 0$ the dispersion relation is $E = c|\mathbf p|$, the four-momentum is null, and $N(\tilde P) = 0$. Since $\tilde P \neq 0$ whenever $E \neq 0$, the massless momentum is a **zero divisor** of $\mathbb{B}$. This is the exact algebraic image of the statement that a massless particle travels on the light cone: the light cone of $\mathbb{M}_-$ *is* the zero-divisor cone (*The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*).

**A massive momentum is invertible.** For $m \neq 0$ one has $N(\tilde P) = -m^2c^2 \neq 0$, so $\tilde P$ is invertible and is *not* a zero divisor. This is the structural asymmetry between the two cases, and it will reappear in the section on the singular massless limit: the rank of $\Phi(\tilde P)$ is one at $m=0$ and two at $m\neq0$.

The zero divisor here is of the **non-pure** kind: its scalar part $iE/c$ does not vanish (for $E\neq0$). The general non-pure zero divisor satisfies the square relation $\tilde Q^2 = 2Q_0\tilde Q$ (*Biquaternion Zero Divisors*), so the massless momentum obeys

$$
\tilde P^2 \;=\; 2\,\frac{iE}{c}\,\tilde P .
$$

**Rank one.** In the matrix realization,

$$
\det\Phi(\tilde P) \;=\; N(\tilde P) \;=\; 0 \quad\text{at } m=0,
$$

and $\Phi(\tilde P) \neq 0$ when $\tilde P \neq 0$; hence $\Phi(\tilde P)$ has rank exactly one. Explicitly, for $\tilde P = iE/c\,e_0 + \mathbf p$,

$$
\Phi(\tilde P) \;=\; i\left(\frac{E}{c}\,I_2 - \mathbf p\cdot\boldsymbol\sigma\right).
$$

The matrix in parentheses, $p_{\alpha\dot\beta} := \frac{E}{c}\delta_{\alpha\dot\beta} - (\mathbf p\cdot\boldsymbol\sigma)_{\alpha\dot\beta}$, is the **standard spinor-helicity bispinor**; it is Hermitian, its determinant is $E^2/c^2 - \mathbf p^2 = m^2c^2$, and it is rank one exactly when $m=0$. The factor $i$ in $\Phi(\tilde P)$ is the $ict$ convention of the framework, and it is the only difference between the framework's momentum matrix and the textbook bispinor. Equivalently, with $\tilde H = -i\tilde P \in \mathbb{M}_+$ one has $\Phi(\tilde H) = p_{\alpha\dot\beta}$ exactly.

The statement that a massless momentum is a zero divisor is not an observation about the framework's arithmetic. It is the statement that the light cone is the determinant-zero locus of $\mathbb{B}\cong M_2(\mathbb{C})$, and that a point of it is a rank-one matrix. The next section shows that this is the spinor-helicity factorisation.

## Rank One Is Factorisability: The Spinor-Helicity Factorisation

The passage from "rank one" to "product of two spinors" is a lemma about $2\times2$ matrices.

**Lemma.** A nonzero $2\times2$ matrix $M$ has rank one if and only if there exist nonzero columns $\lambda,\tilde\lambda \in \mathbb{C}^2$ with

$$
M \;=\; \lambda\,\tilde\lambda^{T}.
$$

The pair is determined up to the scaling $(\lambda,\tilde\lambda) \mapsto (t\lambda, t^{-1}\tilde\lambda)$, $t \in \mathbb{C}^\times$.

*Proof.* If $M = \lambda\tilde\lambda^T$ with both factors nonzero, every column of $M$ is a multiple of $\lambda$, so the column space is one-dimensional and $\operatorname{rank} M = 1$. Conversely, if $\operatorname{rank} M = 1$, choose a nonzero column $\lambda$ of $M$; every other column is a multiple of it, and every row is a multiple of the row $\tilde\lambda^T$ read off any nonzero row of $M$ divided by the corresponding entry of $\lambda$. Then $M = \lambda\tilde\lambda^T$. The scaling is the elementary ambiguity: $(t\lambda)(t^{-1}\tilde\lambda)^T = \lambda\tilde\lambda^T$. $\square$

Applying the lemma to the null momentum,

$$
\Phi(\tilde P) \;=\; \lambda\,\tilde\lambda^{T},
\qquad
\tilde P \text{ null},\quad \lambda \in S,\ \tilde\lambda \in \bar S,
$$

the two factors being concretely columns in $\mathbb{C}^2$, with $\lambda$ in the defining module $S$ and $\tilde\lambda$ in the conjugate module $\bar S$. This is the **spinor-helicity factorisation** $p = \lambda\tilde\lambda$. It is not a separate formalism laid over the algebra; it is the rank-one condition of the zero-divisor cone written in coordinates. The correspondence with the standard notation is fixed by the matrix realization: the two indices of $\Phi(\tilde P)$ are the unprimed and primed spinor indices $\alpha$ and $\dot\beta$ (the Hermitian bispinor is $-i$ times $\Phi(\tilde P)$, the $ict$ factor identified above), and the factorisation is

$$
p_{\alpha\dot\beta} \;=\; \lambda_\alpha\,\tilde\lambda_{\dot\beta},
$$

with $\lambda$ in the spinor module $S$ — the left-handed Weyl module $(\tfrac12,0)$ — and $\tilde\lambda$ transforming in the conjugate (right-handed) Weyl module $(0,\tfrac12)$. This is exactly the factorization $\phi_\alpha\pi^{\dot\beta}$ of the null quadric's mixed spinor $A_\alpha{}^{\dot\beta}$ (*Biquaternion Null Quadric and Projective Geometry*), and it is the statement that a null bispinor is a point of the Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$: the two factors are the two rulings.

**Reality and the two Weyl spinors.** For a real momentum, $\tilde P \in \mathbb{M}_-$ is anti-Hermitian, so $\Phi(\tilde P)$ is anti-Hermitian. An anti-Hermitian rank-one matrix is $i$ times a Hermitian rank-one matrix, and a positive-semidefinite Hermitian rank-one matrix is $u u^\dagger$ for a single spinor $u$; consequently the two factors in $\Phi(\tilde P) = \lambda\tilde\lambda^T$ are conjugate up to a phase,

$$
\tilde\lambda \;\sim\; \lambda^{*} \quad (\text{up to a complex phase}),
$$

which is the real-momentum reality condition of the spinor-helicity formalism. The two factors are the two Weyl spinors of opposite chirality, related here by the framework's complex conjugation, which is the real structure that exchanges the defining module $S$ and its conjugate $\bar S$. For a *complexified* momentum — the general kinematical setting of the formalism — the components $Q_\mu$ are complex, $\tilde P$ lies in the complexified four-vector representation carried by $\mathbb{B}$, and $\lambda$ and $\tilde\lambda$ become independent. That complexification is a genuine extension of the real material sector, and it is flagged as such below.

**The two representations in which the factorisation is read.** Two conventions describe the same content and it is worth naming both, because the factor of $i$ between them is a frequent source of sign errors. In the framework's own reading the null momentum $\tilde P\in\mathbb{M}_-$ is the zero divisor and $\Phi(\tilde P)$ is the anti-Hermitian rank-one matrix factorised above. In the textbook reading the Hermitian bispinor $p_{\alpha\dot\beta} = \frac Ec\delta_{\alpha\dot\beta} - \mathbf p\cdot\boldsymbol\sigma = \Phi(\tilde H)$ is factorised, where $\tilde H = -i\tilde P \in \mathbb{M}_+$. The two matrices differ by the factor $i$, which can be absorbed into either spinor; the rank, the factorisation, the scaling freedom, and all little-group weights are unchanged. We work with $\Phi(\tilde P)$ throughout and translate only where the textbook form is wanted.

**Explicit check.** The factorisation was verified on four independently chosen null momenta, none of them built from the factorisation: $(\frac Ec,\mathbf p) = (5;3,4,0)$, $(13;3,4,12)$, $(7;2,3,6)$, and $(3;1,2,2)$. For each, $N(\tilde P)=0$, $\operatorname{rank}\Phi(\tilde P)=1$, and the matrix was reconstructed exactly from its nonzero column $\lambda$ and the corresponding row $\tilde\lambda^T$ (residual zero in exact arithmetic). The reconstruction used the lemma's construction, so it also checks the converse direction of the lemma on data not chosen to make it work.

## The Brackets as the Invariant Symplectic Pairing

The two spinors carry the framework's invariant symplectic form $\varepsilon(\psi,\phi) = \psi^{T}\epsilon\,\phi$ on the spinor module (*The Spinor Module in Biquaternionic Form and Its Lorentz Action*). The angle and square brackets are that form applied to the two factors of two different momenta:

$$
\langle ij\rangle \;=\; \varepsilon(\lambda_i,\lambda_j) \;=\; \lambda_i^{T}\epsilon\,\lambda_j,
\qquad
[ij] \;=\; \varepsilon(\tilde\lambda_i,\tilde\lambda_j) \;=\; \tilde\lambda_i^{T}\epsilon\,\tilde\lambda_j .
$$

Three properties are inherited rather than postulated.

**Antisymmetry.** The form $\varepsilon$ is antisymmetric, $\varepsilon(\psi,\phi) = -\varepsilon(\phi,\psi)$, because $\epsilon$ is antisymmetric. Hence

$$
\langle ij\rangle = -\langle ji\rangle, \qquad [ij] = -[ji].
$$

This is the antisymmetry stressed at the start of the article; it is the antisymmetry of the invariant spinor metric, not a convention imposed on the brackets. It was checked symbolically, $\langle ij\rangle+\langle ji\rangle = 0$ for arbitrary spinors.

**Lorentz invariance.** Since $g^{T}\epsilon\,g = (\det g)\epsilon = \epsilon$ for every $g \in SL(2,\mathbb{C})$, the brackets are invariant under the one-sided Lorentz action $\lambda \mapsto g\lambda$, $\tilde\lambda \mapsto g^{*}\tilde\lambda$ (the latter being the conjugate defining representation, equivalent to $\Phi(\tilde\Lambda^{*})$ up to the invariant-tensor convention recorded in *Exercise: Chirality and the Weyl Spinors*). The brackets are therefore the Lorentz-invariant contractions of the formalism, as in the standard calculus.

**The bracket–momentum identity.** The polar form of the norm is $B(\tilde P,\tilde Q) = \tfrac12\big(N(\tilde P+\tilde Q)-N(\tilde P)-N(\tilde Q)\big) = \sum_\mu P_\mu Q_\mu$. For two null momenta factorised as above, the determinant of the sum of two rank-one matrices is a product of two brackets, and one finds

$$
\langle ij\rangle\,[ij] \;=\; \det\!\big(\Phi(\tilde P_i)+\Phi(\tilde P_j)\big) \;=\; 2\,B(\tilde P_i,\tilde P_j).
$$

The determinant identity was verified symbolically for two independently factorised momenta with independent complex spinors (all eight spinor components free), and the equality with $2B$ was verified on the same general symbols. For real momenta, $B(\tilde P_i,\tilde P_j) = -\frac{E_iE_j}{c^2} + \mathbf p_i\cdot\mathbf p_j$ in the framework's $ict$ (mostly-plus) convention; in the mostly-minus convention common in amplitude reviews the same identity carries the opposite overall sign. The relative sign of $\langle ij\rangle$ and $[ij]$ is convention-dependent; once both are defined by the same $\varepsilon$, their product is the momentum contraction.

**On signs.** The antisymmetry is the classic source of error in the Parke–Taylor formula. Because $\langle ij\rangle^4$ is even in the interchange $i\leftrightarrow j$, the numerator is insensitive to the ordering, but every bracket that enters linearly — in particular the denominator — changes sign when its two indices are exchanged. A one-line check confirms the effect: replacing a single $\langle 12\rangle$ by $\langle 21\rangle$ in a bracket ratio multiplies the ratio by $-1$.

## The Little Group, the Reality Condition, and Helicity

The scaling freedom of the rank-one factorisation is the kinematic little group.

**The scaling leaves the momentum invariant.** If $\Phi(\tilde P) = \lambda\tilde\lambda^{T}$ and one sends

$$
\lambda \;\longmapsto\; t\,\lambda, \qquad \tilde\lambda \;\longmapsto\; t^{-1}\,\tilde\lambda, \qquad t \in \mathbb{C}^\times,
$$

then $\lambda\tilde\lambda^{T} \mapsto (t\lambda)(t^{-1}\tilde\lambda)^{T} = \lambda\tilde\lambda^{T}$, so $\Phi(\tilde P)$ and hence $\tilde P$ are unchanged. The invariance was verified symbolically for arbitrary complex spinors and arbitrary nonzero $t$. The scaling is precisely the ambiguity of the lemma: a nonzero biquaternion determines its factorisation only up to this one-parameter freedom.

**From $\mathbb{C}^\times$ to $U(1)$.** For a real momentum the reality condition $\tilde\lambda \sim \lambda^{*}$ fixes the modulus of $t$ and leaves its phase:

$$
\lambda \;\longmapsto\; t\,\lambda, \qquad \tilde\lambda \;\longmapsto\; t^{-1}\,\tilde\lambda, \qquad |t|=1,
$$

a $U(1)$. This is the group of the spinor-helicity little-group scaling. It is also realized geometrically inside the framework: the rotation about the momentum axis is the rotor $\tilde R = \cos(\theta/2) + \sin(\theta/2)\,\hat{\mathbf p}$ in the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$, with $\hat{\mathbf p} = \mathbf p/|\mathbf p|$; it commutes with $\tilde P$, since $iE/c$ is central and $\hat{\mathbf p}$ commutes with $\mathbf p$. Hence $\tilde R\tilde P\tilde R^\dagger = \tilde P$ — verified by the vanishing of the commutator and the unitarity relation $\tilde R\tilde R^\dagger = e_0$ — and on the spinor module $\Phi(\tilde R)$ acts by a phase,

$$
\Phi(\tilde R)\,\lambda = e^{\pm i\theta/2}\,\lambda \quad \text{on the two eigen-components},
$$

so that $\lambda \mapsto t\lambda$ and $\tilde\lambda \mapsto t^{-1}\tilde\lambda$ with $t = e^{\mp i\theta/2}$. The little-group scaling is therefore not an abstract relabelling: it is the action of the rotation about $\mathbf p$ on the two factors, and it is the framework's compact $SU(2)$ rotation subgroup acting on the spinor module.

**Helicity is the weight.** A one-particle state or an amplitude of definite helicity $h$ carries a definite weight under the scaling: in the standard normalization,

$$
\text{a helicity-}h \text{ object scales as } t^{-2h} \text{ under } \lambda_i \to t\lambda_i,\ \tilde\lambda_i \to t^{-1}\tilde\lambda_i .
$$

Equivalently, a monomial with $\lambda$-degree $d_\lambda$ and $\tilde\lambda$-degree $d_{\tilde\lambda}$ in particle $i$ has helicity $h_i = \tfrac12(d_{\tilde\lambda,i} - d_{\lambda,i})$. The spinor $\lambda$ has $\lambda$-degree $d_\lambda=+1$, hence helicity $h=-\tfrac12$, and the conjugate $\tilde\lambda$ has $d_{\tilde\lambda}=-1$, hence helicity $h=+\tfrac12$; the spin-$\tfrac12$ field is the weight-$\pm\tfrac12$ object. This is the sense in which the massless little group is $U(1)$ and the helicity is its weight. Two qualifications are kept explicit. First, the full little group of a massless particle is not $U(1)$ but the two-dimensional Euclidean group $ISO(2)$; the compact $U(1)$ of rotations about $\mathbf p$ is the part that acts nontrivially on finite-helicity states, and it is the part realized by the factorisation freedom above. Second, the identification of helicity with the $U(1)$ weight is standard representation theory; the framework supplies the $U(1)$ action natively through its rotation rotors, but it does not by itself select which weight is physical — that selection is the dynamics of the massless field, not the kinematics of the momentum.

**Why the massless case is the rank-one case.** The structural unity of the section is this. The compact $U(1)$ part of the little group that leaves a null momentum invariant is the group of automorphisms of its rank-one factorisation. The factorisation is the zero-divisor structure. Therefore *the little group and the helicity weight are properties of the zero-divisor cone*, not of an added spinor formalism: the null momentum's rank-one matrix factorises, the factorisation is ambiguous by exactly the little-group scaling, and the helicity is the weight of that ambiguity.

## The Parke–Taylor Formula and Its Little-Group Weights

The Parke–Taylor formula is the kinematic factor of the tree-level amplitude for $n$ gluons in the maximally helicity-violating (MHV) configuration, in which all but two gluons have positive helicity. With the two negative-helicity gluons at positions $i$ and $j$, and with the color-ordered labels in cyclic order,

$$
\mathcal A_n^{\mathrm{MHV}} \;\propto\;
\frac{\langle ij\rangle^{4}}{\langle 12\rangle\langle 23\rangle\cdots\langle n1\rangle}.
$$

The complete amplitude carries a coupling constant, a color factor (for the partial amplitude, the single-trace structure), and the momentum-conserving delta function; the kinematical content is the bracket ratio, which is what the framework can address. We state the formula as standard and transcribe it.

The formula is a function of the $\lambda$'s only. Since each particle appears twice in the product of adjacent brackets $\langle 12\rangle\langle 23\rangle\cdots\langle n1\rangle$, the denominator is homogeneous of degree $2$ in each $\lambda_k$, while the numerator $\langle ij\rangle^4$ is homogeneous of degree $4$ in $\lambda_i$ and in $\lambda_j$ and of degree $0$ in the others. Hence the $\lambda$-degree of particle $k$ is

$$
d_{\lambda,k} \;=\;
\begin{cases} +2, & k = i \text{ or } k = j \quad (\text{helicity } -1),\\[2pt] -2, & \text{otherwise} \quad (\text{helicity } +1),\end{cases}
\qquad\text{that is, } d_{\lambda,k} = -2h_k .
$$

This is exactly the little-group weight required of an amplitude whose particle $k$ has helicity $h_k$. The $\tilde\lambda$-degree is zero for every particle, so the $\lambda$-degree is the whole weight and the condition $d_{\lambda,k} = -2h_k$ is satisfied.

**Explicit check.** The weights were computed symbolically for three independent configurations: $n=4$ with negative helicities at positions $1,2$; $n=5$ with negative helicities at positions $1,3$; and $n=6$ with negative helicities at positions $2,5$. In each case the $\lambda$-degree of particle $k$ came out $+2$ for the two negative-helicity particles and $-2$ for the others, with zero $\tilde\lambda$-degree throughout. The $n=5$ and $n=6$ cases were chosen with the negative helicities *non-adjacent*, so that the check does not depend on the special adjacency of the $n=4$ example; the $n=6$ case places one negative helicity across the cyclic boundary, so that it exercises the closing bracket $\langle n1\rangle$.

**Sign check.** The numerator $\langle ij\rangle^4$ is invariant under $i\leftrightarrow j$ because the exponent is even, so the formula does not depend on the order in which the two negative-helicity labels are written. Every bracket entering linearly does depend on the order: replacing one $\langle 12\rangle$ by $\langle 21\rangle$ in a bracket ratio sends the ratio to its negative. This is the concrete sense in which the antisymmetry $\langle ij\rangle = -\langle ji\rangle$ is the classic source of sign errors in the Parke–Taylor formula, and it was checked directly.

**What is not derived.** The framework checks the little-group weights of the kinematic factor, and it supplies the brackets as invariant pairings and the factorisation as the zero-divisor structure. It does not derive the formula, the color factor, the coupling, or the existence of the gluon. The weight check is a consistency test of the transcription, not a derivation from $\mathbb{B}$.

## The Massless Limit Is Singular

It is tempting to say that the massive case follows from the massless one by continuity, or the reverse. It does not, and the algebra shows why in one line.

For a massive momentum $N(\tilde P) = -m^2c^2 \neq 0$, so $\Phi(\tilde P)$ is invertible and has rank two. There is no rank-one factorisation into a single pair of spinors. The massive bispinor requires two terms,

$$
p_{\alpha\dot\beta} \;=\; \lambda_\alpha\tilde\lambda_{\dot\beta} \;+\; \mu_\alpha\tilde\mu_{\dot\beta},
$$

the pair of spinors accounting for the two physical polarizations of a massive particle, and the little group of a massive particle is $SU(2)$, not the $U(1)$ of the massless case. The two situations are different representations of different little groups.

The algebraic defect measures the discontinuity. For $\tilde P = iE/c\,e_0 + \mathbf p$ with $E^2/c^2 = \mathbf p^2 + m^2c^2$ one has, using the quaternion square,

$$
\tilde P^2 \;=\; -\frac{E^2}{c^2}e_0 - \mathbf p^2 e_0 + 2\,\frac{iE}{c}\,\mathbf p
\;=\; 2\,\frac{iE}{c}\,\tilde P \;+\; m^2c^2\,e_0 .
$$

The zero-divisor relation $\tilde P^2 = 2P_0\tilde P$ of the massless case holds only at $m=0$; the mass term is an additive defect of order $m^2$. The relation was verified symbolically for a general massive momentum $(\sqrt{25+m^2};3,4,0)$ as well as at rest, and the massless identity $\tilde P^2 = 2P_0\tilde P$ was verified independently on four null momenta.

Three things therefore fail to be continuous in the limit.

1. **Rank.** $\Phi(\tilde P)$ has rank two for $m\neq0$ and rank one at $m=0$; the rank drops.
2. **Factorisation.** A rank-two matrix is not an outer product of two spinors; the one-term factorisation exists only at $m=0$, and the massive bispinor needs both $\lambda\tilde\lambda$ and $\mu\tilde\mu$.
3. **Little group.** The massive little group is $SU(2)$ and the massless one is $ISO(2)$, whose compact part is $U(1)$. The representations are different and neither is a limit of the other in the naive sense.

The massless limit is therefore singular at the level of the spinor variables and of the little group, and the article does not claim otherwise. The framework represents a massive momentum and a massless one on the same footing — both are elements of $\mathbb{M}_-$ — but the zero-divisor structure, which is what the spinor-helicity formalism exploits, exists only at $m=0$. A massive spinor-helicity calculus would require additional structure (the two-term bispinor and its $SU(2)$ little group), and it is not developed here.

## What the Framework Supplies and What It Does Not

**Supplied natively.** The equivalence *null momentum* $\Leftrightarrow$ *zero divisor* $\Leftrightarrow$ *rank-one matrix* $\Leftrightarrow$ *factorisable as $\lambda\tilde\lambda^T$* is a theorem of the algebra, already available in the companion articles on zero divisors and the null quadric; nothing is added to make it true. The angle and square brackets are the invariant symplectic pairing $\varepsilon$ of the spinor module, and their antisymmetry is the antisymmetry of $\varepsilon$. The little-group scaling is the ambiguity of the rank-one factorisation, and for real momenta the realization of its $U(1)$ part is the framework's rotation rotor about the momentum axis. Helicity is the weight of that action.

**Transcribed.** The standard spinor-helicity calculus — the Parke–Taylor formula, the momentum-conservation constraints, the explicit spinor parametrizations of momenta — is transcribed. The brackets and the weights are checked here, but the calculus is not derived.

**Not supplied.** The framework does not contain the dynamics of the massless fields whose amplitudes these are; it does not contain a colored gauge theory; it does not derive the Parke–Taylor formula; and it does not by itself supply a massive spinor-helicity extension. The identification of a state of helicity $h$ with a definite weight under the little group is standard representation theory, imported.

**Interpretation.** Reading the rank-one zero divisor as the momentum of a massless particle, and its factorisation as the spinor-helicity variables, is the interpretation that makes the algebra kinematical. The algebra contains the structure; the reading of it as a particle's momentum is the physics input, exactly as the reading of $\mathbb{M}_-$ as spacetime is an input elsewhere in the series.

## Gaps and Open Questions

**Gaps.**

1. **Complexified momenta versus the real slice.** The general spinor-helicity variables have independent complex $\lambda,\tilde\lambda$, and the corresponding momentum is complex: it lies in the complexified four-vector representation carried by $\mathbb{B}$, off the real material slice $\mathbb{M}_-$. The framework's physical sector is the real slice, where the reality condition $\tilde\lambda \sim \lambda^{*}$ reduces the little group to $U(1)$. The framework therefore supports the formalism most directly in the case of *real* kinematics; complex kinematics is an extension of the physical sector. This article does not resolve whether the framework's local, medium-dependent complex structure (the scale $c = 1/\sqrt{\epsilon\mu}$ making the $ict$ direction local) has anything to do with the complexification that spinor-helicity amplitudes use, and it does not claim that it does.

2. **No derivation of amplitudes.** The Parke–Taylor formula is checked for consistency but not derived. The framework has a scattering article (*The S-Matrix in Biquaternionic Form*) that hosts a one-mode truncation of the $S$-matrix, but that construction is not a theory of massless scattering amplitudes and does not contain spinor-helicity variables.

3. **$ISO(2)$ versus $U(1)$.** The full massless little group includes null rotations (the translations of $ISO(2)$), which act trivially on finite-helicity states. The framework's factorisation is invariant under the compact $U(1)$ and under the complexified scaling; the precise status of the null-rotation generators in the factorisation picture is not worked out here.

4. **The two families of zero divisors.** Real null momenta are non-pure zero divisors ($P_0 = iE/c \neq 0$ for $E\neq0$). The complexified null cone also contains the pure nilpotent branch, which no real null momentum of nonzero energy reaches. What, if anything, the pure branch describes physically is left open.

**Open questions.** (1) Can the framework's spinor-module Dirac and Weyl equations supply an independent *dynamics* for the factors $\lambda$ and $\tilde\lambda$, rather than only their kinematics? (2) The massless little group's null rotations act trivially on helicity states; can the framework exhibit them as an invariance of the zero-divisor cone at fixed momentum, and does that invariance have a name in the algebra? (3) Is the trace formula $\mathrm{Tr}(\tilde P\tilde H) = 2\,\mathrm{Sc}(\tilde P\tilde H)$ the natural pairing in which to state the amplitudes' positivity or unitarity, given that it is the framework's Born rule? (4) Does the complexification required by spinor-helicity, and the framework's local complex structure in a medium, have a common formulation? These are recorded as questions, not as results.

## Summary

The spinor-helicity formalism writes a massless momentum as a product of two Weyl spinors, $p_{\alpha\dot\beta} = \lambda_\alpha\tilde\lambda_{\dot\beta}$, and builds amplitudes from the antisymmetric brackets $\langle ij\rangle = -\langle ji\rangle$ and $[ij] = -[ji]$. This article has shown that the framework's zero-divisor structure *is* that factorisation, not an analogue of it. A massless momentum $\tilde P = iE/c\,e_0 + \mathbf p$ has $N(\tilde P) = 0$ and $\tilde P \neq 0$, so it is a zero divisor; under $\Phi$ it is a rank-one, anti-Hermitian matrix; a rank-one $2\times2$ matrix is an outer product $\lambda\tilde\lambda^T$; and $\Phi(\tilde P) = i\big(\frac Ec I_2 - \mathbf p\cdot\boldsymbol\sigma\big)$ is the standard bispinor up to the $ict$ factor. The factorisation was verified on four independently chosen null momenta.

The brackets are the invariant symplectic pairing $\varepsilon$ of the spinor module, antisymmetric by the antisymmetry of $\varepsilon$, and they satisfy $\langle ij\rangle[ij] = \det(\Phi(\tilde P_i)+\Phi(\tilde P_j)) = 2B(\tilde P_i,\tilde P_j)$, checked symbolically. The little-group scaling $\lambda\to t\lambda$, $\tilde\lambda\to t^{-1}\tilde\lambda$ is exactly the ambiguity of the rank-one factorisation and leaves the momentum invariant; for real momenta it is a $U(1)$, realized by the framework's rotation rotor about the momentum axis, and helicity is its weight, $d_{\lambda,k} = -2h_k$. The Parke–Taylor kinematic factor has precisely these weights, checked symbolically for $n=4,5,6$ including non-adjacent and cyclic-boundary negative helicities.

Two things are deliberately not claimed. The framework does not derive the Parke–Taylor formula or the gauge theory, and it does not treat the massless limit as continuous: massive momenta are invertible, have rank-two image, carry a two-term bispinor, and have little group $SU(2)$, while the massless ones are zero divisors with rank-one image, a one-term factorisation, and little group $ISO(2)$ with compact part $U(1)$; the defect $\tilde P^2 = 2P_0\tilde P + m^2c^2e_0$ measures the discontinuity. And the general spinor-helicity variables with independent complex spinors describe complexified momenta, off the real material slice; on the real slice the reality condition $\tilde\lambda\sim\lambda^{*}$ holds. Within these limits the identification is exact.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\Phi(\tilde Q)$ | Matrix realization, $\mathbb{B}\cong M_2(\mathbb{C})$ |
| $N(\tilde Q)=\tilde Q\bar{\tilde Q}=\sum_\mu Q_\mu^2=\det\Phi(\tilde Q)$ | Norm form |
| $\mathbb{M}_-$ | Material (anti-Hermitian) subspace, four-vectors |
| $\mathbb{M}_+$ | Informational (Hermitian) subspace |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, rotation rotors |
| $\tilde P = iE/c\,e_0+\mathbf p$ | Four-momentum, null when $N(\tilde P)=0$ |
| $S=\mathbb{C}^2$, $\bar S$ | Spinor module and its conjugate |
| $\varepsilon(\psi,\phi)=\psi^{T}\epsilon\phi$ | Invariant symplectic pairing on $S$ |
| $\lambda$ (unprimed), $\tilde\lambda$ (primed) | Spinor-helicity factors; $\Phi(\tilde P)=\lambda\tilde\lambda^{T}$, so $\Phi(\tilde H)=-i\lambda\tilde\lambda^{T}$ with $\tilde H=-i\tilde P$ |
| $p_{\alpha\dot\beta}=\frac Ec\delta_{\alpha\dot\beta}-(\mathbf p\cdot\boldsymbol\sigma)_{\alpha\dot\beta}$ | Standard spinor-helicity bispinor |
| $\langle ij\rangle=\lambda_i^{T}\epsilon\lambda_j$ | Angle bracket, $=-\langle ji\rangle$ |
| $[ij]=\tilde\lambda_i^{T}\epsilon\tilde\lambda_j$ | Square bracket, $=-[ji]$ |
| $\lambda\to t\lambda,\ \tilde\lambda\to t^{-1}\tilde\lambda$ | Little-group scaling, $t\in\mathbb{C}^\times$; $|t|=1$ real |
| $h$ | Helicity, the little-group weight; $d_\lambda=-2h$ |
| $\tilde H=-i\tilde P\in\mathbb{M}_+$ | Hermitian four-vector, $\Phi(\tilde H)=p_{\alpha\dot\beta}$ |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace formula (Born rule), inherited |
| $\mathcal A_n^{\mathrm{MHV}}\propto\langle ij\rangle^4/\prod_k\langle k,k+1\rangle$ | Parke–Taylor kinematic factor |

## Further Reading

- Stephen J. Parke and T. R. Taylor, "An amplitude for $n$ gluon scattering," *Physical Review Letters* **56** (1986) 2459–2460, for the original Parke–Taylor formula.
- Henriette Elvang and Yu-tin Huang, *Scattering Amplitudes in Gauge Theory and Gravity* (Cambridge University Press, 2015), for the spinor-helicity formalism, the little-group weights, and the Parke–Taylor amplitude.
- Lance J. Dixon, "A brief introduction to modern amplitude methods," in *Proceedings of the 2012 European School of High-Energy Physics* (CERN Yellow Reports, 2014), for a compact review of the spinor-helicity calculus.
- Zvi Bern, Lance J. Dixon, and David A. Kosower, "On-shell methods in perturbative QCD," *Annals of Physics* **322** (2007) 1587–1634, for the use of helicity amplitudes in practical calculations.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1: *Two-Spinor Calculus and Relativistic Fields* (Cambridge University Press, 1984), for the two-component spinor calculus and the reality condition on the momentum bispinor.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge University Press, 1995), for the little group of a massless particle and helicity as the weight of its compact subgroup.
- Companion article *Biquaternion Zero Divisors*, for the criterion $N(\tilde Q)=0$, the pure and non-pure families, and the rank-one statement.
- Companion article *Biquaternion Null Quadric and Projective Geometry*, for the Segre quadric, the two rulings, and the mixed-spinor factorisation $A_\alpha{}^{\dot\beta}=\phi_\alpha\pi^{\dot\beta}$.
- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the module $S$, the conjugate module, the symplectic form $\varepsilon$, and the Lorentz action.
- Companion article *Exercise: Chirality and the Weyl Spinors*, for the chirality projectors, the conjugate defining representation in the $\varepsilon$ convention.
- Companion article *The Lorentz Group in Biquaternionic Form — Structure and Representations*, for the $(m,n)$ classification containing $(\tfrac12,0)$ and $(0,\tfrac12)$.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the identification of the null cone of $\mathbb{M}_-$ with the light cone and the role of the $ict$ convention.
- Companion article *The Photon in Biquaternionic Form*, for the realized helicity $\pm1$ of the massless vector field and its two-state spectrum.
- Companion article *The S-Matrix in Biquaternionic Form*, for what the framework does and does not supply at the level of scattering.
- Companion article *Twistor Theory and Biquaternions*, for the related conformal and null geometry and the distinction between the biquaternion algebra and twistor space.
