# __The Bell Basis as the Idempotent Basis of B⊗B__

## Introduction

The companion article *Entangled Subsystems in the Biquaternion Framework* fixed the two-qubit arena used here. It introduced the tensor-product algebra $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$, the trace $\mathrm{Tr}(x\otimes y)=\mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y)$, the partial traces $\mathrm{Tr}_1$ and $\mathrm{Tr}_2$, and the singlet idempotent

$$
P_{\mathrm{singlet}}=\tfrac{1}{4}\left(e_0\otimes e_0+e_1\otimes e_1+e_2\otimes e_2+e_3\otimes e_3\right).
$$

The companion *Exercise: The Correlation Function of the Bell States* then wrote all four Bell states as idempotents $P_\epsilon$ of $\mathbb{B}\otimes\mathbb{B}$ and computed their correlation functions.

This article develops the structure that those two articles use but do not make explicit: **the four Bell states form a distinguished idempotent basis of the two-qubit algebra.** Each Bell state is an idempotent, Hermitian element of $\mathbb{M}_+\otimes\mathbb{M}_+$. The four are pairwise orthogonal, of trace one, and sum to the identity $e_0\otimes e_0$ of the algebra. They are, at the same time, the joint eigen-idempotents of two commuting Hermitian involutions — the **stabiliser operators** of the Bell basis — and the partial trace of each is the maximally mixed qubit state $\tfrac{1}{2}e_0$.

The mathematics is standard finite-dimensional algebra, recomputed here in the language of $\mathbb{B}\otimes\mathbb{B}$. The article claims no physics beyond the companion articles. What it makes visible is a structural fact: the two-qubit algebra carries a canonical, discrete idempotent basis whose members are the four Bell states; and the Bell states are singled out from the continuum of maximally entangled states by a particular **tensor structure** — by being diagonal in the tensor-product basis.

The article is organised as follows. The next section recalls the conventions and states precisely what an idempotent basis is. The section after that introduces the four Bell idempotents and identifies them with the standard Bell states. Then orthogonality and completeness are proved, first from the stabiliser operators and then from the Hadamard structure of the sign patterns. The following section shows that the Bell basis is the joint eigenbasis of the stabiliser operators. Then maximal entanglement and the diagonal tensor structure are characterised, and the partial traces are computed. A closing remark discusses the status of the tensor product in the framework, which is an open question inherited from the companion articles.

One caveat is stated at the outset and revisited in the closing remark. Everything below is a construction **inside** the algebra $\mathbb{B}\otimes\mathbb{B}$. The companion article *Quantum Mechanics in Biquaternionic Form* lists among its open questions whether the tensor product is natural in the biquaternion framework or whether it requires additional structure, while the entangled-subsystems article simply uses $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$. We follow the latter and do not resolve the tension: the Bell basis is canonical relative to the tensor-product structure that is assumed, and whether that structure is itself canonical for the framework is exactly what remains open.

## The Two-Qubit Algebra and Idempotent Bases

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion units $e_0=1,e_1,e_2,e_3$ satisfying $e_k^2=-e_0$ and the cyclic relations $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, with $e_je_k=-e_ke_j$ for distinct $j,k\in\{1,2,3\}$, and with $i$ the scalar imaginary, $i^2=-1$. The two-qubit algebra is the tensor product

$$
\mathbb{B}\otimes\mathbb{B}\;\cong\; M_4(\mathbb{C}),
$$

taken over the complex scalars. Its trace is the tensor product of the traces of the factors,

$$
\mathrm{Tr}(x\otimes y)=\mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y),
$$

where $\mathrm{Tr}_\mathbb{B}(e_0)=2$ and $\mathrm{Tr}_\mathbb{B}(e_k)=0$ for $k=1,2,3$. The partial traces are

$$
\mathrm{Tr}_2(a\otimes b)=a\,\mathrm{Tr}_\mathbb{B}(b),\qquad
\mathrm{Tr}_1(a\otimes b)=b\,\mathrm{Tr}_\mathbb{B}(a),
$$

extended linearly. The Hermitian elements of $\mathbb{M}_+\otimes\mathbb{M}_+$ are the observables and states of the two-qubit system; in particular, a **pure state** is an idempotent of $\mathbb{B}\otimes\mathbb{B}$ that is Hermitian and of trace one.

Throughout, the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ is the one fixed by the companion article on quantum mechanics,

$$
e_0\mapsto I_2,\qquad e_1\mapsto -i\sigma_1,\qquad e_2\mapsto -i\sigma_2,\qquad e_3\mapsto -i\sigma_3,
$$

with $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices. Equivalently, $\sigma_k$ is the image of $ie_k$. Under this isomorphism the single-qubit idempotent $\tfrac{1}{2}(e_0+i\hat{m})$ corresponds to the spin-up projector along the unit vector $\hat{m}$. We shall use this correspondence to identify the four Bell idempotents with the standard Bell states.

The trace gives a symmetric bilinear form $\mathrm{Tr}(XY)$ on $\mathbb{B}\otimes\mathbb{B}$, and the four Bell idempotents below will be orthonormal with respect to it. It is therefore natural to ask for an **idempotent basis**: a family of idempotents that play, for the algebra and its module, the role that an orthonormal basis plays for a Hilbert space.

**Definition (idempotent basis).** Let $E_1,\dots,E_r$ be elements of $\mathbb{B}\otimes\mathbb{B}$. The family is an *idempotent basis* of the two-qubit algebra if

$$
E_a^2=E_a,\qquad E_aE_b=\delta_{ab}E_a,\qquad \sum_{a=1}^{r}E_a=e_0\otimes e_0,
$$

and each $E_a$ is Hermitian, $E_a^\dagger=E_a$, and minimal, in the sense that it cannot be written as the sum of two nonzero orthogonal idempotents. In $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$, a Hermitian idempotent is minimal if and only if its trace is one.

Two comments make the name precise.

First, an idempotent basis is **not** a linear basis of $\mathbb{B}\otimes\mathbb{B}$ as a $16$-dimensional complex vector space. A family satisfying the definition spans only the $r$-dimensional commutative subalgebra of its linear combinations. What it is a basis of is the **module** on which the algebra acts: the idempotents are the projectors onto the joint eigenspaces of a maximal set of commuting observables, and their union is a decomposition of the identity.

Second, an idempotent basis is the diagonal part of a matrix-unit basis of the algebra. If the $E_a$ are minimal, the **Peirce components** $E_a(\mathbb{B}\otimes\mathbb{B})E_b$ are one-dimensional, and choosing a nonzero element in each gives a family of matrix units $E_{ab}$ with $E_{ab}E_{cd}=\delta_{bc}E_{ad}$ and $E_{aa}=E_a$. The linear span of the $E_a$ is then a maximal commutative subalgebra — a Cartan subalgebra — of $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$. Thus "idempotent basis" means the diagonal of a matrix-unit basis, equivalently a maximal orthogonal family of minimal idempotents resolving the identity.

The companion entangled-subsystems article already exhibited one member of such a family for the two-qubit algebra: the singlet idempotent $P_{\mathrm{singlet}}$. The rest of this article exhibits the full family and its structure.

## The Four Bell Idempotents

In the standard Hilbert-space formulation, the four Bell states of two spin-$\tfrac{1}{2}$ particles are

$$
|\Phi^\pm\rangle=\frac{1}{\sqrt{2}}\left(|\uparrow\uparrow\rangle\pm|\downarrow\downarrow\rangle\right),\qquad
|\Psi^\pm\rangle=\frac{1}{\sqrt{2}}\left(|\uparrow\downarrow\rangle\pm|\downarrow\uparrow\rangle\right).
$$

In the biquaternion formulation each is an idempotent of $\mathbb{B}\otimes\mathbb{B}$. Following *Exercise: The Correlation Function of the Bell States*, write

$$
P_\epsilon=\tfrac{1}{4}\left(e_0\otimes e_0+\epsilon_1\,e_1\otimes e_1+\epsilon_2\,e_2\otimes e_2+\epsilon_3\,e_3\otimes e_3\right),
$$

where $\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)$ is a triple of signs satisfying

$$
\epsilon_1\,\epsilon_2\,\epsilon_3=+1.
$$

There are exactly four such triples, and they correspond to the four Bell states as follows.

| Bell state | $\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)$ | Biquaternion idempotent $P_\epsilon$ |
|---|---|---|
| $\lvert\Psi^-\rangle$ | $(+1,+1,+1)$ | $\tfrac{1}{4}(e_0\otimes e_0+e_1\otimes e_1+e_2\otimes e_2+e_3\otimes e_3)$ |
| $\lvert\Phi^+\rangle$ | $(-1,+1,-1)$ | $\tfrac{1}{4}(e_0\otimes e_0-e_1\otimes e_1+e_2\otimes e_2-e_3\otimes e_3)$ |
| $\lvert\Phi^-\rangle$ | $(+1,-1,-1)$ | $\tfrac{1}{4}(e_0\otimes e_0+e_1\otimes e_1-e_2\otimes e_2-e_3\otimes e_3)$ |
| $\lvert\Psi^+\rangle$ | $(-1,-1,+1)$ | $\tfrac{1}{4}(e_0\otimes e_0-e_1\otimes e_1-e_2\otimes e_2+e_3\otimes e_3)$ |

The first row is the singlet idempotent $P_{\mathrm{singlet}}$ already fixed by the entangled-subsystems article; the other three rows are its companions. *Exercise: The Correlation Function of the Bell States* verified that each $P_\epsilon$ with $\epsilon_1\epsilon_2\epsilon_3=+1$ is idempotent and of trace one, so we do not repeat that computation. Two further properties are worth recording.

**The $P_\epsilon$ are Hermitian.** For $k=1,2,3$ the Hermitian conjugate of $e_k$ is $-e_k$, so

$$
(e_k\otimes e_k)^\dagger=(-e_k)\otimes(-e_k)=e_k\otimes e_k .
$$

The tensor terms are therefore individually Hermitian, the coefficients $\epsilon_k$ and $\tfrac14$ are real, and $P_\epsilon^\dagger=P_\epsilon$. Each $P_\epsilon$ is a legitimate state, not merely an algebraic idempotent.

**The $P_\epsilon$ lie in the physical subspace.** The Hermitian subspace $\mathbb{M}_+$ has real basis $e_0,ie_1,ie_2,ie_3$. Hence

$$
e_k\otimes e_k=-(ie_k)\otimes(ie_k)\in\mathbb{M}_+\otimes\mathbb{M}_+ .
$$

So every $P_\epsilon$ is an element of $\mathbb{M}_+\otimes\mathbb{M}_+$, the space of two-qubit states and observables, as required.

**Identification with the standard Bell states.** Under the isomorphism, $e_k$ corresponds to $-i\sigma_k$, so $e_k\otimes e_k$ corresponds to $-\sigma_k\otimes\sigma_k$. Writing $P_\epsilon$ in the Pauli-string basis gives

$$
P_\epsilon\;\longmapsto\;\tfrac{1}{4}\left(I\otimes I-\epsilon_1\,\sigma_1\otimes\sigma_1-\epsilon_2\,\sigma_2\otimes\sigma_2-\epsilon_3\,\sigma_3\otimes\sigma_3\right),
$$

which is exactly the standard Bell projector for the sign pattern in the table. For example, the singlet $\epsilon=(+1,+1,+1)$ gives $\tfrac14(I\otimes I-\sum_k\sigma_k\otimes\sigma_k)$, the projector onto $|\Psi^-\rangle$, in agreement with the entangled-subsystems article. The general idempotency condition $\epsilon_1\epsilon_2\epsilon_3=+1$ is the algebraic reflection of the fact that there are exactly four Bell states.

## Orthogonality and Completeness

The four $P_\epsilon$ are not merely four idempotents; they are mutually orthogonal and they resolve the identity. Both facts follow cleanly from a pair of commuting observables, which we introduce first because they will also serve in the next section.

### The stabiliser involutions

Define the two tensor-product elements

$$
S_1:=-e_1\otimes e_1,\qquad S_3:=-e_3\otimes e_3 .
$$

They have three elementary properties, each a direct computation.

**Hermiticity.** As in the previous section, $(e_k\otimes e_k)^\dagger=e_k\otimes e_k$, so $S_1^\dagger=S_1$ and $S_3^\dagger=S_3$.

**Involution.** Using $(e_k\otimes e_k)^2=e_k^2\otimes e_k^2=(-e_0)\otimes(-e_0)=e_0\otimes e_0$, we get

$$
S_1^2=S_3^2=e_0\otimes e_0 .
$$

**Commutativity.** Using $e_1e_3=-e_2$ and $e_3e_1=e_2$, together with $(e_j\otimes e_j)(e_k\otimes e_k)=(e_je_k)\otimes(e_je_k)$, we get

$$
S_1S_3=(-e_1\otimes e_1)(-e_3\otimes e_3)=(e_1e_3)\otimes(e_1e_3)=(-e_2)\otimes(-e_2)=e_2\otimes e_2,
$$

and the same computation in the other order gives $S_3S_1=e_2\otimes e_2$. Hence $S_1S_3=S_3S_1$.

Under the isomorphism, $S_1$ corresponds to $\sigma_1\otimes\sigma_1$ and $S_3$ to $\sigma_3\otimes\sigma_3$; these are the standard Pauli stabiliser generators of the Bell basis, and this is the sense in which the word "stabiliser" is used below.

### Orthogonality and completeness from the spectral projectors

Because $S_1$ and $S_3$ are commuting Hermitian involutions, the operator

$$
\Pi_{(s_1,s_3)}
=\tfrac{1}{2}\left(e_0\otimes e_0+s_1S_1\right)\cdot\tfrac{1}{2}\left(e_0\otimes e_0+s_3S_3\right)
=\tfrac{1}{4}\left(e_0\otimes e_0+s_1S_1+s_3S_3+s_1s_3\,S_1S_3\right)
$$

is the joint spectral projector onto the common eigenspace with eigenvalues $(s_1,s_3)\in\{\pm1\}^2$. Each factor $\tfrac12(e_0\otimes e_0+s_kS_k)$ is idempotent and Hermitian because $S_k$ is an involution, and the two factors commute; hence the product is idempotent and Hermitian as well. Summing over the four sign pairs,

$$
\sum_{s_1,s_3=\pm1}\Pi_{(s_1,s_3)}=e_0\otimes e_0 .
$$

Substituting $S_1=-e_1\otimes e_1$, $S_3=-e_3\otimes e_3$, and $S_1S_3=e_2\otimes e_2$ gives

$$
\Pi_{(s_1,s_3)}=\tfrac{1}{4}\left(e_0\otimes e_0-s_1\,e_1\otimes e_1-s_3\,e_3\otimes e_3+s_1s_3\,e_2\otimes e_2\right),
$$

which is exactly $P_\epsilon$ with

$$
\epsilon_1=-s_1,\qquad \epsilon_2=s_1s_3,\qquad \epsilon_3=-s_3 .
$$

The identity $\epsilon_1\epsilon_2\epsilon_3=(-s_1)(s_1s_3)(-s_3)=s_1^2s_3^2=+1$ is then automatic. We have therefore proved, in one step, that the four Bell idempotents of the previous section are pairwise orthogonal, sum to the identity, and are Hermitian of trace one. In detail:

- **Orthogonality:** $P_\epsilon P_{\epsilon'}=\delta_{\epsilon\epsilon'}P_\epsilon$, because distinct joint spectral projectors of a family of commuting Hermitian operators are orthogonal.
- **Completeness:** $\sum_\epsilon P_\epsilon=e_0\otimes e_0$, the resolution of the identity.
- **Trace-normalisation:** $\mathrm{Tr}(P_\epsilon)=\tfrac14\,\mathrm{Tr}(e_0\otimes e_0)=\tfrac14\cdot4=1$, because $\mathrm{Tr}(e_k\otimes e_k)=\mathrm{Tr}_\mathbb{B}(e_k)^2=0$.
- **Trace-orthonormality:** $\mathrm{Tr}(P_\epsilon P_{\epsilon'})=\delta_{\epsilon\epsilon'}$, combining orthogonality with trace-normalisation.

Together with Hermiticity and the fact that the Peirce components $P_\epsilon(\mathbb{B}\otimes\mathbb{B})P_{\epsilon'}$ are one-dimensional, these four properties say precisely that $\{P_\epsilon\}$ is an idempotent basis in the sense of the definition above. Its linear span is the four-dimensional maximal commutative subalgebra generated by $S_1$ and $S_3$, a Cartan subalgebra of $\mathbb{B}\otimes\mathbb{B}$.

### The Hadamard structure of the sign patterns

The orthogonality and completeness relations have a combinatorial shadow that is worth recording, because it explains *why* the four sign patterns are the right ones.

Adjoin $\epsilon_0:=1$ to each triple and form the four vectors

$$
v_\epsilon=(1,\epsilon_1,\epsilon_2,\epsilon_3)\in\{\pm1\}^4,\qquad \epsilon_1\epsilon_2\epsilon_3=+1 .
$$

These are the rows of a $4\times4$ sign matrix $H$, whose row for the singlet is $(1,1,1,1)$. Direct evaluation gives

$$
\sum_{m=0}^{3}\epsilon_m\,\epsilon'_m=4\,\delta_{\epsilon,\epsilon'},\qquad
\sum_{\epsilon}\epsilon_m\,\epsilon_{m'}=4\,\delta_{m,m'} .
$$

Thus $HH^{T}=H^{T}H=4I_4$, i.e. $H$ is a Hadamard matrix. The first relation says that the four sign vectors are pairwise orthogonal of squared length four; the second says that the four columns are also orthogonal and that, in particular, $\sum_\epsilon\epsilon_k=0$ for each $k=1,2,3$. The first relation is the algebraic content of operator orthogonality — the mixed terms cancel exactly — and the vanishing column sums are the reason the mixed terms cancel in the resolution of the identity $\sum_\epsilon P_\epsilon=e_0\otimes e_0$. The Bell idempotents are, in this sense, the operator form of a Hadamard matrix.

It is worth noting what the Hadamard structure does **not** yet show. The relations above concern the four sign patterns with $\epsilon_1\epsilon_2\epsilon_3=+1$; they do not by themselves exclude the existence of a diagonal-form idempotent with some other pattern, or with non-unit coefficients. We settle that question in the section on maximal entanglement, where the diagonal-form idempotents are classified.

## The Bell Basis as a Stabiliser Eigenbasis

The projector formula of the previous section already contains the eigenvalue relations. Since $\Pi_{(s_1,s_3)}$ is by construction the joint spectral projector for eigenvalues $(s_1,s_3)$, and since $P_\epsilon=\Pi_{(s_1,s_3)}$ with $s_1=-\epsilon_1$ and $s_3=-\epsilon_3$, we have

$$
S_1P_\epsilon=-\epsilon_1\,P_\epsilon,\qquad S_3P_\epsilon=-\epsilon_3\,P_\epsilon .
$$

Equivalently, $P_\epsilon$ is a joint eigen-idempotent of the two stabiliser involutions, with eigenvalue table

| Bell state | $\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)$ | $S_1=-e_1\otimes e_1$ | $S_3=-e_3\otimes e_3$ |
|---|---|---|---|
| $\lvert\Psi^-\rangle$ | $(+1,+1,+1)$ | $-1$ | $-1$ |
| $\lvert\Phi^+\rangle$ | $(-1,+1,-1)$ | $+1$ | $+1$ |
| $\lvert\Phi^-\rangle$ | $(+1,-1,-1)$ | $-1$ | $+1$ |
| $\lvert\Psi^+\rangle$ | $(-1,-1,+1)$ | $+1$ | $-1$ |

The four eigenvalue pairs $(-\epsilon_1,-\epsilon_3)$ are all distinct, so the joint spectrum of $\{S_1,S_3\}$ is non-degenerate. In the language of quantum measurement, $\{S_1,S_3\}$ is a **complete set of commuting observables** (a CSCO), and the Bell idempotents are exactly the elements of its joint eigenbasis. The statement "the Bell basis is the eigenbasis of the stabiliser operators" is therefore not an analogy: it is the statement that a two-element CSCO of tensor-product observables has the four Bell idempotents as its spectral resolution.

Two immediate consequences complete the picture.

**Conjugation stabilisation.** Because $S_k$ is an involution and $S_kP_\epsilon=\pm P_\epsilon$, multiplying on the right by $S_k$ gives $S_kP_\epsilon S_k=P_\epsilon$. Thus each Bell idempotent is invariant under conjugation by either stabiliser operator, $S_1P_\epsilon S_1=S_3P_\epsilon S_3=P_\epsilon$.

**The stabiliser group.** For a fixed $\epsilon$, the four elements

$$
e_0\otimes e_0,\qquad -\epsilon_1 S_1,\qquad -\epsilon_3 S_3,\qquad \epsilon_1\epsilon_3\,S_1S_3
$$

form a Klein four-group, and each acts on $P_\epsilon$ with eigenvalue $+1$. Indeed $-\epsilon_1S_1 P_\epsilon=(-\epsilon_1)(-\epsilon_1)P_\epsilon=P_\epsilon$, and similarly for the other generators; the product acts with eigenvalue $(-\epsilon_1)(-\epsilon_3)=\epsilon_1\epsilon_3$, which is compensated by the explicit sign in front. This is the standard stabiliser group of a Bell state, expressed in the algebra $\mathbb{B}\otimes\mathbb{B}$.

The stabiliser eigenvalues are also the entries of the correlation matrix of *Exercise: The Correlation Function of the Bell States*. That article defined $T_{jk}=\langle\Psi|\sigma_j\otimes\sigma_k|\Psi\rangle$ and found $T_{jj}=-\epsilon_j$ with vanishing off-diagonal entries. Since $S_j=-e_j\otimes e_j$ corresponds to $\sigma_j\otimes\sigma_j$, the diagonal entry $T_{jj}$ is exactly the eigenvalue of $S_j$ on $P_\epsilon$. The correlation data and the stabiliser data are the same data, read in two ways.

## Maximal Entanglement and the Diagonal Tensor Structure

The four Bell states are the standard examples of maximally entangled states. The framework gives this notion a clean algebraic form and, at the same time, shows that the Bell idempotents are a *discrete* family inside a *continuous* one.

### Maximal entanglement as a partial-trace condition

A pure two-qubit state $P$ is **maximally entangled** if tracing out either subsystem leaves the maximally mixed single-qubit state. In the framework, with the partial traces recalled in the second section, the condition is

$$
\mathrm{Tr}_2(P)=\mathrm{Tr}_1(P)=\tfrac{1}{2}e_0 .
$$

The Bell idempotents satisfy this, as we compute in the next section. This is the algebraic definition of maximal entanglement in the framework, and it is a condition on the partial trace, not an additional postulate.

### The diagonal tensor structure

The distinguishing structural feature of the Bell idempotents is visible directly in their definition. Expanding an arbitrary element of $\mathbb{B}\otimes\mathbb{B}$ in the tensor basis,

$$
X=\sum_{\mu,\nu=0}^{3}X_{\mu\nu}\,e_\mu\otimes e_\nu,
$$

the Bell idempotents are precisely those **trace-one idempotents** whose expansion contains only the **diagonal** terms $e_\mu\otimes e_\mu$:

$$
P_\epsilon=\tfrac{1}{4}\sum_{\mu=0}^{3}\epsilon_\mu\,e_\mu\otimes e_\mu,\qquad \epsilon_0=1 .
$$

There are no cross terms $e_\mu\otimes e_\nu$ with $\mu\neq\nu$. This is the "particular tensor structure" of the Bell states: the two tensor factors carry matched indices throughout, so the element is a sum of correlated pairs rather than of arbitrary products. In particular, $P_\epsilon$ is invariant under the tensor flip $\tau(e_\mu\otimes e_\nu)=e_\nu\otimes e_\mu$.

A natural question is how many idempotents of this diagonal form **of trace one** there are. Let

$$
P=\tfrac{1}{4}\left(\lambda_0\,e_0\otimes e_0+\lambda_1\,e_1\otimes e_1+\lambda_2\,e_2\otimes e_2+\lambda_3\,e_3\otimes e_3\right).
$$

Imposing $P^2=P$ and $\mathrm{Tr}(P)=1$ determines the coefficients completely. The trace gives $\lambda_0=1$. The coefficient of $e_0\otimes e_0$ in $P^2$ is $\tfrac{1}{16}\sum_\mu\lambda_\mu^2$, which must equal $\tfrac14\lambda_0=\tfrac14$, so $\sum_\mu\lambda_\mu^2=4$. The coefficient of $e_l\otimes e_l$ (for $l=1,2,3$, where $\{j,k,l\}=\{1,2,3\}$) is $\tfrac{1}{16}\left(2\lambda_l+2\lambda_j\lambda_k\right)$, which must equal $\tfrac14\lambda_l$, so $\lambda_j\lambda_k=\lambda_l$. Multiplying the three relations by $\lambda_1,\lambda_2,\lambda_3$ respectively gives $\lambda_1^2=\lambda_2^2=\lambda_3^2=\lambda_1\lambda_2\lambda_3$; combined with $\lambda_0=1$ and $\sum_\mu\lambda_\mu^2=4$ this yields $\lambda_1^2=\lambda_2^2=\lambda_3^2=1$. Hence each $\lambda_k=\pm1$ and $\lambda_1\lambda_2\lambda_3=+1$. (For the four sign patterns, the direct verification of idempotency is the computation in *Exercise: The Correlation Function of the Bell States*.) So there are exactly **four** diagonal-form idempotents **of trace one**, and they are the four Bell idempotents. No other trace-one diagonal idempotent exists.

### The Bell idempotents inside the continuum of maximally entangled states

The diagonal-form condition is genuinely restrictive. The maximally entangled pure states of two qubits form a continuum: for any unitary element $\tilde U$ of $\mathbb{B}$ with $\tilde U\tilde U^\dagger=e_0$, acting on the first factor,

$$
P\;=\;(\tilde U\otimes e_0)\,P_{\Phi^+}\,(\tilde U^\dagger\otimes e_0)
$$

is again a rank-one idempotent, and its partial traces are still $\tfrac{1}{2}e_0$, because $\mathrm{Tr}_2(P)=U(\tfrac12 e_0)U^\dagger=\tfrac12 e_0$ with the central scalar $\tfrac12 e_0$ invariant. A generic such $P$ is **not** diagonal in the tensor basis.

A concrete example makes the point. Take $\tilde U=\tfrac{3}{5}e_0+\tfrac{4}{5}e_1$, a unit real quaternion. The resulting rank-one idempotent has partial trace $\tfrac{1}{2}e_0$ and is therefore maximally entangled, but its tensor expansion contains the off-diagonal terms

$$
\tfrac{6}{25}\,e_3\otimes e_2+\tfrac{6}{25}\,e_2\otimes e_3,
$$

and it is not one of the four Bell idempotents. So maximal entanglement alone does not select the Bell basis.

What does select it is the diagonal tensor structure, equivalently the eigenvalue conditions of the previous section: the Bell idempotents are the maximally entangled pure states that are joint eigenstates of the stabiliser operators $S_1$ and $S_3$. In this sense the Bell basis is the canonical, discrete maximal-entanglement family that the tensor-product algebra carries.

The four Bell idempotents are also a single orbit of one another. Conjugating $P_{\Phi^+}$ by the unit real quaternions $e_0,e_1,e_2,e_3$ on the first factor permutes the four Bell idempotents:

$$
P_{\Phi^+}\xrightarrow{\,e_0\,}P_{\Phi^+},\quad
P_{\Phi^+}\xrightarrow{\,e_1\,}P_{\Psi^+},\quad
P_{\Phi^+}\xrightarrow{\,e_2\,}P_{\Psi^-},\quad
P_{\Phi^+}\xrightarrow{\,e_3\,}P_{\Phi^-}.
$$

The local action of the quaternion group therefore organises the Bell basis into a single orbit, while the global sign pattern $\epsilon$ labels the members.

A final observation is that the four Bell idempotents are **locally indistinguishable**. Since every one of them has the same partial trace $\tfrac{1}{2}e_0$ on each factor, no measurement on a single qubit can reveal which Bell state was prepared. The entire distinction between them resides in the correlated, tensor-product terms $e_k\otimes e_k$ — that is, in the signs $\epsilon$, which are precisely the stabiliser eigenvalues and the diagonal correlation entries. The local data are constant across the basis; the correlation data are what vary.

## Partial Traces and Maximal Mixedness

We now compute the partial trace of each Bell idempotent and confirm the maximal-entanglement condition used above.

Because $P_\epsilon$ is a sum of diagonal tensor terms, the partial trace over the second factor is immediate. Applying $\mathrm{Tr}_2(e_\mu\otimes e_\nu)=e_\mu\,\mathrm{Tr}_\mathbb{B}(e_\nu)$ term by term,

$$
\mathrm{Tr}_2(P_\epsilon)
=\tfrac{1}{4}\left(\mathrm{Tr}_\mathbb{B}(e_0)\,e_0+\sum_{k=1}^{3}\epsilon_k\,\mathrm{Tr}_\mathbb{B}(e_k)\,e_k\right)
=\tfrac{1}{4}\left(2\,e_0+0\right)
=\tfrac{1}{2}\,e_0 .
$$

The same computation with the roles of the factors exchanged gives

$$
\mathrm{Tr}_1(P_\epsilon)=\tfrac{1}{2}\,e_0 .
$$

The reason is exactly the one identified in the entangled-subsystems article: the entangled terms $e_k\otimes e_k$ with $k\neq0$ are traceless in each factor, so the partial trace keeps only the $e_0\otimes e_0$ term and produces the scalar-only element $\tfrac{1}{2}e_0$, which is not idempotent. The mixedness of the reduced state is the algebraic residue of the entanglement of the joint state.

The reduced state $\rho_1=\rho_2=\tfrac{1}{2}e_0$ is the maximally mixed qubit state, the centre of the Bloch ball. Its purity and entropy are the standard ones:

$$
\mathrm{Tr}(\rho_1^2)=\mathrm{Tr}\!\left(\tfrac{1}{4}e_0\right)=\tfrac{1}{4}\cdot2=\tfrac{1}{2},\qquad
S(\rho_1)=-\tfrac12\log\tfrac12-\tfrac12\log\tfrac12=\log 2 .
$$

So each Bell idempotent is maximally entangled in the precise sense of the previous section: its partial trace is maximal mixed, its reduced purity is $\tfrac12$ (the minimum for a qubit), and its reduced entropy is $\log 2$ (the maximum). The computation is the same for all four states and reproduces, for the singlet, the result $\rho_1=\tfrac12e_0$ of the entangled-subsystems article and of *Exercise: The Reduced State of an Entangled Subsystem*.

Combined with the previous section, the picture is complete. The four Bell idempotents form an idempotent basis of $\mathbb{B}\otimes\mathbb{B}$; they are the joint eigenbasis of the stabiliser operators $S_1$ and $S_3$; they are the only trace-one diagonal-form idempotents; and their partial traces are all the maximally mixed state $\tfrac{1}{2}e_0$. The Bell basis is thus a canonical object of the tensor-product algebra, selected simultaneously by the tensor structure, by the stabiliser spectrum, and by maximal entanglement.

## A Remark on the Status of the Tensor Product

The construction above lives entirely inside the tensor-product algebra $\mathbb{B}\otimes\mathbb{B}$. It is therefore worth stating clearly how that algebra stands in the framework, because the companion articles do not speak with one voice about it.

The entangled-subsystems article uses the tensor product directly: it defines the two-qubit state space as $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$, defines the trace by $\mathrm{Tr}(x\otimes y)=\mathrm{Tr}_\mathbb{B}(x)\mathrm{Tr}_\mathbb{B}(y)$, and computes with the singlet idempotent without further comment. The quantum-mechanics article, in its ten-point checklist, likewise lists a composition rule and calls the tensor product "a natural extension of the framework."

At the same time, the same quantum-mechanics article lists, among its open questions, the following: "The extension to $n$ qubits requires the tensor product $\mathbb{B}^{\otimes_\mathbb{C}n}$ ... Is the tensor product natural in the biquaternion framework, or does it require additional structure?" The introduction article poses the same point as an open question about the extension to many qubits.

These two positions are not reconciled here. The present article uses the tensor product exactly as the entangled-subsystems article does, and every statement above is a statement about the algebra $\mathbb{B}\otimes\mathbb{B}$ once that algebra is granted. The Bell basis is canonical **relative to** the tensor-product structure: given $\mathbb{B}\otimes\mathbb{B}$ with its trace, the four Bell idempotents are singled out by the stabiliser operators, by the diagonal tensor structure, and by maximal mixedness, with no further choices.

Whether the tensor-product algebra is itself canonical for the biquaternion framework — whether, that is, the two-qubit algebra is forced by the structure of $\mathbb{B}$, or whether it is one natural construction among several — is the open question. If the tensor product were to require additional structure, then the Bell basis would inherit that contingency: it would be canonical within the tensor-product description, but the passage from one qubit to two would carry an assumption that the framework has not yet justified. This article takes no position on that question; it records it, because the Bell basis is a construction in the tensor-product algebra, and the status of that algebra is exactly what remains open.

## Summary

The four Bell states of two qubits are, in the biquaternion framework, four idempotents of the tensor-product algebra $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$. Following *Exercise: The Correlation Function of the Bell States*, they are written

$$
P_\epsilon=\tfrac{1}{4}\left(e_0\otimes e_0+\epsilon_1\,e_1\otimes e_1+\epsilon_2\,e_2\otimes e_2+\epsilon_3\,e_3\otimes e_3\right),
\qquad \epsilon_1\epsilon_2\epsilon_3=+1 ,
$$

one for each of the four admissible sign triples.

The article established the following structure.

- **Idempotent basis.** The four $P_\epsilon$ are Hermitian idempotents of trace one, pairwise orthogonal, summing to the identity: $P_\epsilon P_{\epsilon'}=\delta_{\epsilon\epsilon'}P_\epsilon$ and $\sum_\epsilon P_\epsilon=e_0\otimes e_0$. They form a maximal orthogonal family of minimal idempotents — an idempotent basis — of the two-qubit algebra, whose span is a Cartan subalgebra of dimension four.
- **Stabiliser eigenbasis.** The commuting Hermitian involutions $S_1=-e_1\otimes e_1$ and $S_3=-e_3\otimes e_3$ (corresponding to $\sigma_1\otimes\sigma_1$ and $\sigma_3\otimes\sigma_3$) form a complete set of commuting observables whose joint spectrum is non-degenerate; the $P_\epsilon$ are its joint eigen-idempotents, with eigenvalues $(-\epsilon_1,-\epsilon_3)$. Each $P_\epsilon$ is conjugation-invariant under $S_1$ and $S_3$, and its stabiliser group is the Klein four-group generated by the sign-corrected $S_1$ and $S_3$.
- **Diagonal tensor structure.** The Bell idempotents are exactly the idempotents of diagonal tensor form $\tfrac14\sum_\mu\epsilon_\mu\,e_\mu\otimes e_\mu$. There are exactly four of them, and the sign matrix whose rows are $(1,\epsilon_1,\epsilon_2,\epsilon_3)$ is Hadamard. A generic maximally entangled state is a continuum and is not diagonal; the Bell basis is the discrete, canonical family selected by the diagonal structure.
- **Maximal mixedness.** The partial trace of every Bell idempotent is the maximally mixed state, $\mathrm{Tr}_1(P_\epsilon)=\mathrm{Tr}_2(P_\epsilon)=\tfrac12 e_0$, of purity $\tfrac12$ and entropy $\log 2$. The four states are locally indistinguishable; their distinction resides entirely in the correlated tensor terms, i.e. in the signs $\epsilon$.

All of this is standard finite-dimensional algebra, expressed in the conventions of the companion articles. The construction presupposes the tensor-product algebra $\mathbb{B}\otimes\mathbb{B}$; whether that algebra is canonical for the framework is an open question inherited from the companion articles and is left unresolved.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$ | Two-qubit tensor-product algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, cyclic products |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_+$ | Hermitian subspace: real scalar, imaginary vector |
| $\mathrm{Tr}_\mathbb{B}$ | Trace on a single factor: $\mathrm{Tr}_\mathbb{B}(e_0)=2$, $\mathrm{Tr}_\mathbb{B}(e_k)=0$ |
| $\mathrm{Tr}(x\otimes y)=\mathrm{Tr}_\mathbb{B}(x)\mathrm{Tr}_\mathbb{B}(y)$ | Trace on the tensor product |
| $\mathrm{Tr}_1,\mathrm{Tr}_2$ | Partial traces |
| $P_{\mathrm{singlet}}=\tfrac14(e_0\otimes e_0+\sum_k e_k\otimes e_k)$ | Singlet idempotent |
| $P_\epsilon=\tfrac14(e_0\otimes e_0+\sum_k\epsilon_k e_k\otimes e_k)$ | Bell idempotent, $\epsilon_1\epsilon_2\epsilon_3=+1$ |
| $\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)$ | Sign pattern labelling a Bell state |
| $S_1=-e_1\otimes e_1,\ S_3=-e_3\otimes e_3$ | Stabiliser involutions ($\leftrightarrow\sigma_1\otimes\sigma_1,\ \sigma_3\otimes\sigma_3$) |
| $S_1S_3=e_2\otimes e_2$ | Product of the stabiliser involutions |
| $S_kP_\epsilon=-\epsilon_kP_\epsilon$ | Eigenvalue relation |
| $\mathrm{Tr}_2(P_\epsilon)=\mathrm{Tr}_1(P_\epsilon)=\tfrac12 e_0$ | Maximally mixed reduced state |
| $T_{jj}=-\epsilon_j$ | Diagonal correlation matrix entry |
| $e_0\mapsto I_2,\ e_k\mapsto-i\sigma_k$ | Isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ |

## Further Reading

- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Bell states, the Bell basis, the stabiliser formalism, and the standard treatment of maximal entanglement.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard textbook treatment of two spin-$\tfrac{1}{2}$ particles and the Bell states.
- A. Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for the density-matrix formalism, partial traces, and maximal entanglement.
- C. H. Bennett, G. Brassard, C. Crépeau, R. Jozsa, A. Peres, and W. K. Wootters, "Teleporting an unknown quantum state via dual classical and Einstein–Podolsky–Rosen channels," *Physical Review Letters* **70** (1993) 1895–1899, for the Bell-basis measurement and its role in quantum information.
- R. F. Werner, "All teleportation and dense coding schemes," *Journal of Physics A: Mathematical and General* **34** (2001) 7081–7094, for the classification of maximally entangled states and the role of the Bell basis.
- S. L. Braunstein, A. Mann, and M. Revzen, "Maximal violation of Bell inequalities for mixed states," *Physical Review Letters* **68** (1992) 3259–3261, for the correlation structure of the Bell states.
- The companion articles of this series: *Introduction to the Biquaternion Universe*, *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, *Quantum Mechanics in Biquaternionic Form*, *Entangled Subsystems in the Biquaternion Framework*, *Exercise: Two Spins in the Singlet State*, and *Exercise: The Correlation Function of the Bell States*.
