# __The Bell Basis as the Idempotent Basis of B⊗B__

## Introduction

The companion article *Entangled Subsystems in the Biquaternion Framework* fixed the two-qubit arena used here. It introduced the tensor-product algebra $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$, the trace $\mathrm{Tr}(x\otimes y)=\mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y)$, the partial traces $\mathrm{Tr}_1$ and $\mathrm{Tr}_2$, and the singlet idempotent

$$
\tilde\Pi_{\mathrm{singlet}}=\tfrac{1}{4}\left(e_t\otimes e_t+\vec e_x\otimes \vec e_x+\vec e_y\otimes \vec e_y+\vec e_z\otimes \vec e_z\right).
$$

The companion *Exercise: The Correlation Function of the Bell States* then wrote all four Bell states as idempotents $\tilde\Pi_\epsilon$ of $\mathbb{B}\otimes\mathbb{B}$ and computed their correlation functions.

This article develops the structure that those two articles use but do not make explicit: **the four Bell states form a distinguished idempotent basis of the two-qubit algebra.** Each Bell state is an idempotent, Hermitian element of $\mathbb{M}_+\otimes\mathbb{M}_+$. The four are pairwise orthogonal, of trace one, and sum to the identity $e_t\otimes e_t$ of the algebra. They are, at the same time, the joint eigen-idempotents of two commuting Hermitian involutions — the **stabiliser operators** of the Bell basis — and the partial trace of each is the maximally mixed qubit state $\tfrac{1}{2}e_t$.

The mathematics is standard finite-dimensional algebra, recomputed here in the language of $\mathbb{B}\otimes\mathbb{B}$. The article claims no physics beyond the companion articles. What it makes visible is a structural fact: the two-qubit algebra carries a canonical, discrete idempotent basis whose members are the four Bell states; and the Bell states are singled out from the continuum of maximally entangled states by a particular **tensor structure** — by being diagonal in the tensor-product basis.

The article is organised as follows. The next section recalls the conventions and states precisely what an idempotent basis is. A short section then separates the two-qubit **state vector** from the two-qubit **state operator**, records the identification $\mathbb{C}^4\cong\mathbb{B}$ that the vector makes available, and notes the two cautions it carries: the vector is not the state, and a single quaternion is not an entangled state. Then the four Bell idempotents are introduced and identified with the standard Bell states. Orthogonality and completeness are proved, first from the stabiliser operators and then from the Hadamard structure of the sign patterns. The following section shows that the Bell basis is the joint eigenbasis of the stabiliser operators. Then maximal entanglement and the diagonal tensor structure are characterised, and a further section examines a claimed finite enumeration of the maximally entangled states and shows why the exhaustiveness claim fails. The partial traces are computed next. A closing remark discusses the status of the tensor product in the framework, which is an open question inherited from the companion articles.

One caveat is stated at the outset and revisited in the closing remark. Everything below is a construction **inside** the algebra $\mathbb{B}\otimes\mathbb{B}$. The companion article *Quantum Physics in Biquaternionic Form* lists among its open questions whether the tensor product is natural in the biquaternion framework or whether it requires additional structure, while the entangled-subsystems article simply uses $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$. We follow the latter and do not resolve the tension: the Bell basis is canonical relative to the tensor-product structure that is assumed, and whether that structure is itself canonical for the framework is exactly what remains open.

## The Two-Qubit Algebra and Idempotent Bases

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion units $e_t=1,\vec e_x,\vec e_y,\vec e_z$ satisfying $\vec e_\mu^2=-e_t$ and the cyclic relations $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$, with $\vec e_\nu \vec e_\mu=-\vec e_\mu \vec e_\nu$ for distinct $\nu,\mu\in\{x,y,z\}$, and with $i$ the scalar imaginary, $i^2=-1$. The two-qubit algebra is the tensor product

$$
\mathbb{B}\otimes\mathbb{B}\;\cong\; M_4(\mathbb{C}),
$$

taken over the complex scalars. Its trace is the tensor product of the traces of the factors,

$$
\mathrm{Tr}(x\otimes y)=\mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y),
$$

where $\mathrm{Tr}_\mathbb{B}(e_t)=2$ and $\mathrm{Tr}_\mathbb{B}(\vec e_\mu)=0$ for $\mu\in\{x,y,z\}$. The partial traces are

$$
\mathrm{Tr}_2(a\otimes b)=a\,\mathrm{Tr}_\mathbb{B}(b),\qquad
\mathrm{Tr}_1(a\otimes b)=b\,\mathrm{Tr}_\mathbb{B}(a),
$$

extended linearly. The Hermitian elements of $\mathbb{M}_+\otimes\mathbb{M}_+$ are the observables and states of the two-qubit system; in particular, a **pure state** is an idempotent of $\mathbb{B}\otimes\mathbb{B}$ that is Hermitian and of trace one.

Throughout, the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ is the one fixed by the companion article on quantum physics,

$$
e_t\mapsto I_2,\qquad \vec e_x\mapsto -i\sigma_1,\qquad \vec e_y\mapsto -i\sigma_2,\qquad \vec e_z\mapsto -i\sigma_3,
$$

with $\sigma_1,\sigma_2,\sigma_3$ the Pauli matrices. Equivalently, $\sigma_\mu$ is the image of $i\vec e_\mu$. Under this isomorphism the single-qubit idempotent $\tfrac{1}{2}(e_t+i\vec u)$ corresponds to the spin-up projector along the unit vector $\vec u$. We shall use this correspondence to identify the four Bell idempotents with the standard Bell states.

The trace gives a symmetric bilinear form $\mathrm{Tr}(XY)$ on $\mathbb{B}\otimes\mathbb{B}$, and the four Bell idempotents below will be orthonormal with respect to it. It is therefore natural to ask for an **idempotent basis**: a family of idempotents that play, for the algebra and its module, the role that an orthonormal basis plays for a Hilbert space.

**Definition (idempotent basis).** Let $E_1,\dots,E_r$ be elements of $\mathbb{B}\otimes\mathbb{B}$. The family is an *idempotent basis* of the two-qubit algebra if

$$
E_a^2=E_a,\qquad E_aE_b=\delta_{ab}E_a,\qquad \sum_{a=1}^{r}E_a=e_t\otimes e_t,
$$

and each $E_a$ is Hermitian, $E_a^{*}=E_a$, and minimal, in the sense that it cannot be written as the sum of two nonzero orthogonal idempotents. In $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$, a Hermitian idempotent is minimal if and only if its trace is one.

Two comments make the name precise.

First, an idempotent basis is **not** a linear basis of $\mathbb{B}\otimes\mathbb{B}$ as a $16$-dimensional complex vector space. A family satisfying the definition spans only the $r$-dimensional commutative subalgebra of its linear combinations. What it is a basis of is the **module** on which the algebra acts: the idempotents are the projectors onto the joint eigenspaces of a maximal set of commuting observables, and their union is a decomposition of the identity.

Second, an idempotent basis is the diagonal part of a matrix-unit basis of the algebra. If the $E_a$ are minimal, the **Peirce components** $E_a(\mathbb{B}\otimes\mathbb{B})E_b$ are one-dimensional, and choosing a nonzero element in each gives a family of matrix units $E_{ab}$ with $E_{ab}E_{cd}=\delta_{bc}E_{ad}$ and $E_{aa}=E_a$. The linear span of the $E_a$ is then a maximal commutative subalgebra — a Cartan subalgebra — of $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$. Thus "idempotent basis" means the diagonal of a matrix-unit basis, equivalently a maximal orthogonal family of minimal idempotents resolving the identity.

The companion entangled-subsystems article already exhibited one member of such a family for the two-qubit algebra: the singlet idempotent $\tilde\Pi_{\mathrm{singlet}}$. The rest of this article exhibits the full family and its structure.

## The State Vector and the State Operator: $\mathbb{C}^4\cong\mathbb{B}$

Two objects of the two-qubit arena are both four-dimensional in appearance and are easily conflated, so it is worth separating them once, before the Bell states are written down.

- The **state vector** of two qubits lies in the Hilbert space $\mathbb{C}^2\otimes\mathbb{C}^2\cong\mathbb{C}^4$, of complex dimension four.
- The **state operator** — the density matrix — lies in $\mathbb{C}^4\otimes(\mathbb{C}^4)^*\cong M_4(\mathbb{C})$, of complex dimension sixteen, realised in the framework as the tensor product $\mathbb{B}\otimes\mathbb{B}$.

The underlying complex vector space of the biquaternion algebra is $\mathbb{C}^4$, so a state vector can also be written as an element of $\mathbb{B}$. Fix the linear isomorphism by the basis order

$$
\lvert00\rangle\mapsto e_t,\qquad \lvert01\rangle\mapsto \vec e_x,\qquad \lvert10\rangle\mapsto \vec e_y,\qquad \lvert11\rangle\mapsto \vec e_z .
$$

This is a **vector-space** identification only: the algebra product on $\mathbb{B}$ does not act as the two-qubit operator product on the state. Under it the four Bell vectors are combinations of two basis units.

| Bell state | vector | element of $\mathbb{B}$ |
|---|---|---|
| $\lvert\Phi^+\rangle$ | $\tfrac{1}{\sqrt2}(\lvert00\rangle+\lvert11\rangle)$ | $\tfrac{1}{\sqrt2}(e_t+\vec e_z)$ |
| $\lvert\Phi^-\rangle$ | $\tfrac{1}{\sqrt2}(\lvert00\rangle-\lvert11\rangle)$ | $\tfrac{1}{\sqrt2}(e_t-\vec e_z)$ |
| $\lvert\Psi^+\rangle$ | $\tfrac{1}{\sqrt2}(\lvert01\rangle+\lvert10\rangle)$ | $\tfrac{1}{\sqrt2}(\vec e_x+\vec e_y)$ |
| $\lvert\Psi^-\rangle$ | $\tfrac{1}{\sqrt2}(\lvert01\rangle-\lvert10\rangle)$ | $\tfrac{1}{\sqrt2}(\vec e_x-\vec e_y)$ |

At the level of state vectors the four Bell states are therefore the four combinations $\tfrac{1}{\sqrt2}(e_\mu\pm e_\nu)$ for the unit pairs $\{e_t,e_z\}$ and $\{e_x,e_y\}$. This is the form in which they arise from the division of one particle in the mereological interpretation of the companion article *Entangled Subsystems in the Biquaternion Framework*, where the state is created by a split and the split is a division in the sense of *Mereology and Collective Set Theory*.

Two cautions follow from the identification, and both are used by the literature that motivates this section.

**The vector is not the state.** The combinations $\tfrac{1}{\sqrt2}(e_\mu\pm e_\nu)$ are elements of $\mathbb{B}$ and are in general neither Hermitian nor idempotent; they are not elements of $\mathbb{M}_+$ and they are not states in the framework's sense. The state *object* is the idempotent $\tilde\Pi_\epsilon$ of $\mathbb{B}\otimes\mathbb{B}$ whose module-theoretic image is the line spanned by the corresponding vector. The passage is from a state vector in the four-dimensional module to a rank-one idempotent in the sixteen-dimensional algebra, and the two must not be identified. The framework's convention, fixed by the companion articles, is that a pure state **is** the idempotent; the vector is the module element on which it acts. The two descriptions agree on every prediction, because both are interpretations of the same tensor-product state, but only the second is a state in the algebra.

**A single quaternion is not an entangled state.** The temptation created by the identification $\mathbb{C}^4\cong\mathbb{B}$ is to take one element of $\mathbb{B}$ and read it as an entangled two-qubit state. This fails on the standard test. Write an element of $\mathbb{B}$ as $Q=Q_t e_t+\sum_\mu Q_\mu \vec e_\mu$ and let $\mathbf c=(c_1,c_2,c_3,c_4)$ be its components in the basis order above. The corresponding two-qubit vector is a product state exactly when

$$
c_1c_4-c_2c_3=0 ,
$$

and, when it is normalised, its concurrence is $2\lvert c_1c_4-c_2c_3\rvert$. The real unit quaternion $Q=\tfrac{1}{2}(e_t-\vec e_x-\vec e_y+\vec e_z)$, that is $\mathbf c=\tfrac12(1,-1,-1,1)$, satisfies $c_1c_4=c_2c_3=\tfrac14$; its concurrence is zero, and it represents the product state $\tfrac12(\lvert0\rangle-\lvert1\rangle)\otimes(\lvert0\rangle-\lvert1\rangle)$. A single quaternion, however it is normalised, can never carry entanglement, because the entanglement of a two-qubit state is a property of the operator in $\mathbb{B}\otimes\mathbb{B}$ and not of a vector in $\mathbb{B}$. An algebraic indecomposability of an element of $\mathbb{B}$ — for instance the non-factorisation of its left-regular-representation matrix — is a statement about the multiplication operator, not about the Schmidt rank of the state, and the two must not be confused.

## The Four Bell Idempotents

In the standard Hilbert-space formulation, the four Bell states of two spin-$\tfrac{1}{2}$ particles are

$$
|\Phi^\pm\rangle=\frac{1}{\sqrt{2}}\left(|\uparrow\uparrow\rangle\pm|\downarrow\downarrow\rangle\right),\qquad
|\Psi^\pm\rangle=\frac{1}{\sqrt{2}}\left(|\uparrow\downarrow\rangle\pm|\downarrow\uparrow\rangle\right).
$$

In the biquaternion formulation each is an idempotent of $\mathbb{B}\otimes\mathbb{B}$. Following *Exercise: The Correlation Function of the Bell States*, write

$$
\tilde\Pi_\epsilon=\tfrac{1}{4}\left(e_t\otimes e_t+\epsilon_1\,\vec e_x\otimes \vec e_x+\epsilon_2\,\vec e_y\otimes \vec e_y+\epsilon_3\,\vec e_z\otimes \vec e_z\right),
$$

where $\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)$ is a triple of signs satisfying

$$
\epsilon_1\,\epsilon_2\,\epsilon_3=+1.
$$

There are exactly four such triples, and they correspond to the four Bell states as follows.

| Bell state | $\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)$ | Biquaternion idempotent $\tilde\Pi_\epsilon$ |
|---|---|---|
| $\lvert\Psi^-\rangle$ | $(+1,+1,+1)$ | $\tfrac{1}{4}(e_t\otimes e_t+\vec e_x\otimes \vec e_x+\vec e_y\otimes \vec e_y+\vec e_z\otimes \vec e_z)$ |
| $\lvert\Phi^+\rangle$ | $(-1,+1,-1)$ | $\tfrac{1}{4}(e_t\otimes e_t-\vec e_x\otimes \vec e_x+\vec e_y\otimes \vec e_y-\vec e_z\otimes \vec e_z)$ |
| $\lvert\Phi^-\rangle$ | $(+1,-1,-1)$ | $\tfrac{1}{4}(e_t\otimes e_t+\vec e_x\otimes \vec e_x-\vec e_y\otimes \vec e_y-\vec e_z\otimes \vec e_z)$ |
| $\lvert\Psi^+\rangle$ | $(-1,-1,+1)$ | $\tfrac{1}{4}(e_t\otimes e_t-\vec e_x\otimes \vec e_x-\vec e_y\otimes \vec e_y+\vec e_z\otimes \vec e_z)$ |

The first row is the singlet idempotent $\tilde\Pi_{\mathrm{singlet}}$ already fixed by the entangled-subsystems article; the other three rows are its companions. *Exercise: The Correlation Function of the Bell States* verified that each $\tilde\Pi_\epsilon$ with $\epsilon_1\epsilon_2\epsilon_3=+1$ is idempotent and of trace one, so we do not repeat that computation. Two further properties are worth recording.

**The $\tilde\Pi_\epsilon$ are Hermitian.** For $\mu\in\{x,y,z\}$ the Hermitian conjugate of $\vec e_\mu$ is $-\vec e_\mu$, so

$$
(\vec e_\mu\otimes \vec e_\mu)^{*}=(-\vec e_\mu)\otimes(-\vec e_\mu)=\vec e_\mu\otimes \vec e_\mu .
$$

The tensor terms are therefore individually Hermitian, the coefficients $\epsilon_\mu$ and $\tfrac14$ are real, and $\tilde\Pi_\epsilon^{*}=\tilde\Pi_\epsilon$. Each $\tilde\Pi_\epsilon$ is a legitimate state, not merely an algebraic idempotent.

**The $\tilde\Pi_\epsilon$ lie in the physical subspace.** The Hermitian subspace $\mathbb{M}_+$ has real basis $e_t,i\vec e_x,i\vec e_y,i\vec e_z$. Hence

$$
\vec e_\mu\otimes \vec e_\mu=-(i\vec e_\mu)\otimes(i\vec e_\mu)\in\mathbb{M}_+\otimes\mathbb{M}_+ .
$$

So every $\tilde\Pi_\epsilon$ is an element of $\mathbb{M}_+\otimes\mathbb{M}_+$, the space of two-qubit states and observables, as required.

**Identification with the standard Bell states.** Under the isomorphism, $\vec e_\mu$ corresponds to $-i\sigma_\mu$, so $\vec e_\mu\otimes \vec e_\mu$ corresponds to $-\sigma_\mu\otimes\sigma_\mu$. Writing $\tilde\Pi_\epsilon$ in the Pauli-string basis gives

$$
\tilde\Pi_\epsilon\;\longmapsto\;\tfrac{1}{4}\left(I\otimes I-\epsilon_1\,\sigma_1\otimes\sigma_1-\epsilon_2\,\sigma_2\otimes\sigma_2-\epsilon_3\,\sigma_3\otimes\sigma_3\right),
$$

which is exactly the standard Bell projector for the sign pattern in the table. For example, the singlet $\epsilon=(+1,+1,+1)$ gives $\tfrac14(I\otimes I-\sum_\mu\sigma_\mu\otimes\sigma_\mu)$, the projector onto $|\Psi^-\rangle$, in agreement with the entangled-subsystems article. The general idempotency condition $\epsilon_1\epsilon_2\epsilon_3=+1$ is the algebraic reflection of the fact that there are exactly four Bell states.

## Orthogonality and Completeness

The four $\tilde\Pi_\epsilon$ are not merely four idempotents; they are mutually orthogonal and they resolve the identity. Both facts follow cleanly from a pair of commuting observables, which we introduce first because they will also serve in the next section.

### The stabiliser involutions

Define the two tensor-product elements

$$
S_1:=-\vec e_x\otimes \vec e_x,\qquad S_3:=-\vec e_z\otimes \vec e_z .
$$

They have three elementary properties, each a direct computation.

**Hermiticity.** As in the previous section, $(\vec e_\mu\otimes \vec e_\mu)^{*}=\vec e_\mu\otimes \vec e_\mu$, so $S_1^{*}=S_1$ and $S_3^{*}=S_3$.

**Involution.** Using $(\vec e_\mu\otimes \vec e_\mu)^2=\vec e_\mu^2\otimes \vec e_\mu^2=(-e_t)\otimes(-e_t)=e_t\otimes e_t$, we get

$$
S_1^2=S_3^2=e_t\otimes e_t .
$$

**Commutativity.** Using $\vec e_x\vec e_z=-\vec e_y$ and $\vec e_z\vec e_x=\vec e_y$, together with $(\vec e_\nu\otimes \vec e_\nu)(\vec e_\mu\otimes \vec e_\mu)=(\vec e_\nu \vec e_\mu)\otimes(\vec e_\nu \vec e_\mu)$, we get

$$
S_1S_3=(-\vec e_x\otimes \vec e_x)(-\vec e_z\otimes \vec e_z)=(\vec e_x\vec e_z)\otimes(\vec e_x\vec e_z)=(-\vec e_y)\otimes(-\vec e_y)=\vec e_y\otimes \vec e_y,
$$

and the same computation in the other order gives $S_3S_1=\vec e_y\otimes \vec e_y$. Hence $S_1S_3=S_3S_1$.

Under the isomorphism, $S_1$ corresponds to $\sigma_1\otimes\sigma_1$ and $S_3$ to $\sigma_3\otimes\sigma_3$; these are the standard Pauli stabiliser generators of the Bell basis, and this is the sense in which the word "stabiliser" is used below.

### Orthogonality and completeness from the spectral projectors

Because $S_1$ and $S_3$ are commuting Hermitian involutions, the operator

$$
\tilde\Pi_{(s_1,s_3)}
=\tfrac{1}{2}\left(e_t\otimes e_t+s_1S_1\right)\cdot\tfrac{1}{2}\left(e_t\otimes e_t+s_3S_3\right)
=\tfrac{1}{4}\left(e_t\otimes e_t+s_1S_1+s_3S_3+s_1s_3\,S_1S_3\right)
$$

is the joint spectral projector onto the common eigenspace with eigenvalues $(s_1,s_3)\in\{\pm1\}^2$. Each factor $\tfrac12(e_t\otimes e_t+s_\mu S_\mu)$ is idempotent and Hermitian because $S_\mu$ is an involution, and the two factors commute; hence the product is idempotent and Hermitian as well. Summing over the four sign pairs,

$$
\sum_{s_1,s_3=\pm1}\tilde\Pi_{(s_1,s_3)}=e_t\otimes e_t .
$$

Substituting $S_1=-\vec e_x\otimes \vec e_x$, $S_3=-\vec e_z\otimes \vec e_z$, and $S_1S_3=\vec e_y\otimes \vec e_y$ gives

$$
\tilde\Pi_{(s_1,s_3)}=\tfrac{1}{4}\left(e_t\otimes e_t-s_1\,\vec e_x\otimes \vec e_x-s_3\,\vec e_z\otimes \vec e_z+s_1s_3\,\vec e_y\otimes \vec e_y\right),
$$

which is exactly $\tilde\Pi_\epsilon$ with

$$
\epsilon_1=-s_1,\qquad \epsilon_2=s_1s_3,\qquad \epsilon_3=-s_3 .
$$

The identity $\epsilon_1\epsilon_2\epsilon_3=(-s_1)(s_1s_3)(-s_3)=s_1^2s_3^2=+1$ is then automatic. We have therefore proved, in one step, that the four Bell idempotents of the previous section are pairwise orthogonal, sum to the identity, and are Hermitian of trace one. In detail:

- **Orthogonality:** $\tilde\Pi_\epsilon \tilde\Pi_{\epsilon'}=\delta_{\epsilon\epsilon'}\tilde\Pi_\epsilon$, because distinct joint spectral projectors of a family of commuting Hermitian operators are orthogonal.
- **Completeness:** $\sum_\epsilon \tilde\Pi_\epsilon=e_t\otimes e_t$, the resolution of the identity.
- **Trace-normalisation:** $\mathrm{Tr}(\tilde\Pi_\epsilon)=\tfrac14\,\mathrm{Tr}(e_t\otimes e_t)=\tfrac14\cdot4=1$, because $\mathrm{Tr}(\vec e_\mu\otimes \vec e_\mu)=\mathrm{Tr}_\mathbb{B}(\vec e_\mu)^2=0$.
- **Trace-orthonormality:** $\mathrm{Tr}(\tilde\Pi_\epsilon \tilde\Pi_{\epsilon'})=\delta_{\epsilon\epsilon'}$, combining orthogonality with trace-normalisation.

Together with Hermiticity and the fact that the Peirce components $\tilde\Pi_\epsilon(\mathbb{B}\otimes\mathbb{B})\tilde\Pi_{\epsilon'}$ are one-dimensional, these four properties say precisely that $\{\tilde\Pi_\epsilon\}$ is an idempotent basis in the sense of the definition above. Its linear span is the four-dimensional maximal commutative subalgebra generated by $S_1$ and $S_3$, a Cartan subalgebra of $\mathbb{B}\otimes\mathbb{B}$.

### The Hadamard structure of the sign patterns

The orthogonality and completeness relations have a combinatorial shadow that is worth recording, because it explains *why* the four sign patterns are the right ones.

Adjoin $\epsilon_t:=1$ to each triple, write $(\epsilon_x,\epsilon_y,\epsilon_z)=(\epsilon_1,\epsilon_2,\epsilon_3)$, and form the four vectors

$$
v_\epsilon=(\epsilon_t,\epsilon_x,\epsilon_y,\epsilon_z)\in\{\pm1\}^4,\qquad \epsilon_1\epsilon_2\epsilon_3=+1 .
$$

These are the rows of a $4\times4$ sign matrix $H$, whose row for the singlet is $(1,1,1,1)$. Direct evaluation gives

$$
\sum_{\rho\in\{t,x,y,z\}}\epsilon_\rho\,\epsilon'_\rho=4\,\delta_{\epsilon,\epsilon'},\qquad
\sum_{\epsilon}\epsilon_\rho\,\epsilon_{\rho'}=4\,\delta_{\rho,\rho'} .
$$

Thus $HH^{T}=H^{T}H=4I_4$, i.e. $H$ is a Hadamard matrix. The first relation says that the four sign vectors are pairwise orthogonal of squared length four; the second says that the four columns are also orthogonal and that, in particular, $\sum_\epsilon\epsilon_\mu=0$ for each $\mu\in\{x,y,z\}$. The first relation is the algebraic content of operator orthogonality — the mixed terms cancel exactly — and the vanishing column sums are the reason the mixed terms cancel in the resolution of the identity $\sum_\epsilon \tilde\Pi_\epsilon=e_t\otimes e_t$. The Bell idempotents are, in this sense, the operator form of a Hadamard matrix.

It is worth noting what the Hadamard structure does **not** yet show. The relations above concern the four sign patterns with $\epsilon_1\epsilon_2\epsilon_3=+1$; they do not by themselves exclude the existence of a diagonal-form idempotent with some other pattern, or with non-unit coefficients. We settle that question in the section on maximal entanglement, where the diagonal-form idempotents are classified.

## The Bell Basis as a Stabiliser Eigenbasis

The projector formula of the previous section already contains the eigenvalue relations. Since $\tilde\Pi_{(s_1,s_3)}$ is by construction the joint spectral projector for eigenvalues $(s_1,s_3)$, and since $\tilde\Pi_\epsilon=\tilde\Pi_{(s_1,s_3)}$ with $s_1=-\epsilon_1$ and $s_3=-\epsilon_3$, we have

$$
S_1\tilde\Pi_\epsilon=-\epsilon_1\,\tilde\Pi_\epsilon,\qquad S_3\tilde\Pi_\epsilon=-\epsilon_3\,\tilde\Pi_\epsilon .
$$

Equivalently, $\tilde\Pi_\epsilon$ is a joint eigen-idempotent of the two stabiliser involutions, with eigenvalue table

| Bell state | $\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)$ | $S_1=-\vec e_x\otimes \vec e_x$ | $S_3=-\vec e_z\otimes \vec e_z$ |
|---|---|---|---|
| $\lvert\Psi^-\rangle$ | $(+1,+1,+1)$ | $-1$ | $-1$ |
| $\lvert\Phi^+\rangle$ | $(-1,+1,-1)$ | $+1$ | $+1$ |
| $\lvert\Phi^-\rangle$ | $(+1,-1,-1)$ | $-1$ | $+1$ |
| $\lvert\Psi^+\rangle$ | $(-1,-1,+1)$ | $+1$ | $-1$ |

The four eigenvalue pairs $(-\epsilon_1,-\epsilon_3)$ are all distinct, so the joint spectrum of $\{S_1,S_3\}$ is non-degenerate. In the language of quantum measurement, $\{S_1,S_3\}$ is a **complete set of commuting observables** (a CSCO), and the Bell idempotents are exactly the elements of its joint eigenbasis. The statement "the Bell basis is the eigenbasis of the stabiliser operators" is therefore not an analogy: it is the statement that a two-element CSCO of tensor-product observables has the four Bell idempotents as its spectral resolution.

Two immediate consequences complete the picture.

**Conjugation stabilisation.** Because $S_\mu$ is an involution and $S_\mu\tilde\Pi_\epsilon=\pm \tilde\Pi_\epsilon$, multiplying on the right by $S_\mu$ gives $S_\mu\tilde\Pi_\epsilon S_\mu=\tilde\Pi_\epsilon$. Thus each Bell idempotent is invariant under conjugation by either stabiliser operator, $S_1\tilde\Pi_\epsilon S_1=S_3\tilde\Pi_\epsilon S_3=\tilde\Pi_\epsilon$.

**The stabiliser group.** For a fixed $\epsilon$, the four elements

$$
e_t\otimes e_t,\qquad -\epsilon_1 S_1,\qquad -\epsilon_3 S_3,\qquad \epsilon_1\epsilon_3\,S_1S_3
$$

form a Klein four-group, and each acts on $\tilde\Pi_\epsilon$ with eigenvalue $+1$. Indeed $-\epsilon_1S_1 \tilde\Pi_\epsilon=(-\epsilon_1)(-\epsilon_1)\tilde\Pi_\epsilon=\tilde\Pi_\epsilon$, and similarly for the other generators; the product acts with eigenvalue $(-\epsilon_1)(-\epsilon_3)=\epsilon_1\epsilon_3$, which is compensated by the explicit sign in front. This is the standard stabiliser group of a Bell state, expressed in the algebra $\mathbb{B}\otimes\mathbb{B}$.

The stabiliser eigenvalues are also the entries of the correlation matrix of *Exercise: The Correlation Function of the Bell States*. That article defined $T_{\nu\mu}=\langle\Psi|\sigma_\nu\otimes\sigma_\mu|\Psi\rangle$ and found $T_{\nu\nu}=-\epsilon_\nu$ with vanishing off-diagonal entries. Since $S_\nu=-\vec e_\nu\otimes \vec e_\nu$ corresponds to $\sigma_\nu\otimes\sigma_\nu$, the diagonal entry $T_{\nu\nu}$ is exactly the eigenvalue of $S_\nu$ on $\tilde\Pi_\epsilon$. The correlation data and the stabiliser data are the same data, read in two ways.

## Maximal Entanglement and the Diagonal Tensor Structure

The four Bell states are the standard examples of maximally entangled states. The framework gives this notion a clean algebraic form and, at the same time, shows that the Bell idempotents are a *discrete* family inside a *continuous* one.

### Maximal entanglement as a partial-trace condition

A pure two-qubit state $\tilde\Pi$ is **maximally entangled** if tracing out either subsystem leaves the maximally mixed single-qubit state. In the framework, with the partial traces recalled in the second section, the condition is

$$
\mathrm{Tr}_2(\tilde\Pi)=\mathrm{Tr}_1(\tilde\Pi)=\tfrac{1}{2}e_t .
$$

The Bell idempotents satisfy this, as we compute in the next section. This is the algebraic definition of maximal entanglement in the framework, and it is a condition on the partial trace, not an additional postulate.

### The diagonal tensor structure

The distinguishing structural feature of the Bell idempotents is visible directly in their definition. Expanding an arbitrary element of $\mathbb{B}\otimes\mathbb{B}$ in the tensor basis,

$$
\tilde{Q}=\sum_{\mu,\nu\in\{t,x,y,z\}}Q_{\mu\nu}\,e_\mu\otimes e_\nu,
$$

the Bell idempotents are precisely those **trace-one idempotents** whose expansion contains only the **diagonal** terms $e_\mu\otimes e_\mu$:

$$
\tilde\Pi_\epsilon=\tfrac{1}{4}\sum_{\mu\in\{t,x,y,z\}}\epsilon_\mu\,e_\mu\otimes e_\mu,\qquad \epsilon_t=1 .
$$

There are no cross terms $e_\mu\otimes e_\nu$ with $\mu\neq\nu$. This is the "particular tensor structure" of the Bell states: the two tensor factors carry matched indices throughout, so the element is a sum of correlated pairs rather than of arbitrary products. In particular, $\tilde\Pi_\epsilon$ is invariant under the tensor flip $\tau(e_\mu\otimes e_\nu)=e_\nu\otimes e_\mu$.

A natural question is how many idempotents of this diagonal form **of trace one** there are. Let

$$
\tilde\Pi=\tfrac{1}{4}\left(\lambda_0\,e_t\otimes e_t+\lambda_1\,\vec e_x\otimes \vec e_x+\lambda_2\,\vec e_y\otimes \vec e_y+\lambda_3\,\vec e_z\otimes \vec e_z\right).
$$

Imposing $\tilde\Pi^2=\tilde\Pi$ and $\mathrm{Tr}(\tilde\Pi)=1$ determines the coefficients completely. The trace gives $\lambda_0=1$. The coefficient of $e_t\otimes e_t$ in $\tilde\Pi^2$ is $\tfrac{1}{16}\sum_\mu\lambda_\mu^2$, which must equal $\tfrac14\lambda_0=\tfrac14$, so $\sum_\mu\lambda_\mu^2=4$. The coefficient of $\vec e_\lambda\otimes \vec e_\lambda$ (for $\lambda\in\{x,y,z\}$, where $\{\nu,\mu,\lambda\}=\{x,y,z\}$) is $\tfrac{1}{16}\left(2\lambda_\lambda+2\lambda_\nu\lambda_\mu\right)$, which must equal $\tfrac14\lambda_\lambda$, so $\lambda_\nu\lambda_\mu=\lambda_\lambda$. Multiplying the three relations by $\lambda_1,\lambda_2,\lambda_3$ respectively gives $\lambda_1^2=\lambda_2^2=\lambda_3^2=\lambda_1\lambda_2\lambda_3$; combined with $\lambda_0=1$ and $\sum_\mu\lambda_\mu^2=4$ this yields $\lambda_1^2=\lambda_2^2=\lambda_3^2=1$. Hence each $\lambda_\mu=\pm1$ and $\lambda_1\lambda_2\lambda_3=+1$. (For the four sign patterns, the direct verification of idempotency is the computation in *Exercise: The Correlation Function of the Bell States*.) So there are exactly **four** diagonal-form idempotents **of trace one**, and they are the four Bell idempotents. No other trace-one diagonal idempotent exists.

### The Bell idempotents inside the continuum of maximally entangled states

The diagonal-form condition is genuinely restrictive. The maximally entangled pure states of two qubits form a continuum: for any unitary element $\tilde U$ of $\mathbb{B}$ with $\tilde U\tilde U^{*}=e_t$, acting on the first factor,

$$
\tilde\Pi\;=\;(\tilde U\otimes e_t)\,\tilde\Pi_{\Phi^+}\,(\tilde U^{*}\otimes e_t)
$$

is again a rank-one idempotent, and its partial traces are still $\tfrac{1}{2}e_t$, because $\mathrm{Tr}_2(\tilde\Pi)=U(\tfrac12 e_t)U^{*}=\tfrac12 e_t$ with the central scalar $\tfrac12 e_t$ invariant. A generic such $\tilde\Pi$ is **not** diagonal in the tensor basis.

A concrete example makes the point. Take $\tilde U=\tfrac{3}{5}e_t+\tfrac{4}{5}\vec e_x$, a unit real quaternion. The resulting rank-one idempotent has partial trace $\tfrac{1}{2}e_t$ and is therefore maximally entangled, but its tensor expansion contains the off-diagonal terms

$$
\tfrac{6}{25}\,\vec e_z\otimes \vec e_y+\tfrac{6}{25}\,\vec e_y\otimes \vec e_z,
$$

and it is not one of the four Bell idempotents. So maximal entanglement alone does not select the Bell basis.

What does select it is the diagonal tensor structure, equivalently the eigenvalue conditions of the previous section: the Bell idempotents are the maximally entangled pure states that are joint eigenstates of the stabiliser operators $S_1$ and $S_3$. In this sense the Bell basis is the canonical, discrete maximal-entanglement family that the tensor-product algebra carries.

The four Bell idempotents are also a single orbit of one another. Conjugating $\tilde\Pi_{\Phi^+}$ by the unit real quaternions $e_t,\vec e_x,\vec e_y,\vec e_z$ on the first factor permutes the four Bell idempotents:

$$
\tilde\Pi_{\Phi^+}\xrightarrow{\,e_t\,}\tilde\Pi_{\Phi^+},\quad
\tilde\Pi_{\Phi^+}\xrightarrow{\,\vec e_x\,}\tilde\Pi_{\Psi^+},\quad
\tilde\Pi_{\Phi^+}\xrightarrow{\,\vec e_y\,}\tilde\Pi_{\Psi^-},\quad
\tilde\Pi_{\Phi^+}\xrightarrow{\,\vec e_z\,}\tilde\Pi_{\Phi^-}.
$$

The local action of the quaternion group therefore organises the Bell basis into a single orbit, while the global sign pattern $\epsilon$ labels the members.

A final observation is that the four Bell idempotents are **locally indistinguishable**. Since every one of them has the same partial trace $\tfrac{1}{2}e_t$ on each factor, no measurement on a single qubit can reveal which Bell state was prepared. The entire distinction between them resides in the correlated, tensor-product terms $\vec e_\mu\otimes \vec e_\mu$ — that is, in the signs $\epsilon$, which determine the stabiliser eigenvalues and the diagonal correlation entries. The local data are constant across the basis; the correlation data are what vary.

## A Claimed Enumeration of the Maximally Entangled States

The preceding section showed that the maximally entangled pure states form a continuum and that the Bell idempotents are a discrete family inside it. A source in the literature reaches the opposite conclusion, and it is worth recording why that conclusion fails, both because the corpus possesses the tools to state the failure exactly and because the disagreement is a good illustration of the continuum.

For a normalised pure two-qubit state

$$
\lvert\psi\rangle=c_1\lvert00\rangle+c_2\lvert01\rangle+c_3\lvert10\rangle+c_4\lvert11\rangle ,
$$

the **concurrence** is $C=2\lvert c_1c_4-c_2c_3\rvert$, and $C=1$ exactly when the state is maximally entangled in the partial-trace sense of this article. Thus maximal entanglement is the single equation

$$
\lvert c_1c_4-c_2c_3\rvert=\tfrac{1}{2}.
$$

Obojska (*Journal of Physics Communications* **4** (2020) 055018), working in the algebra $\mathbb{B}$ with the basis written $1,i,j,k$ and using the division relation of *Mereology and Collective Set Theory*, reads a two-qubit state as an element of $\mathbb{C}^4\cong\mathbb{B}$ and restricts the quotients of its amplitudes to the set $\{-i,i,-1\}$. Under this restriction she obtains twelve **patterns** of pure maximally entangled states — eight of a simple form, four of a general form — and asserts as **Corollary 1** that "in the algebra of biquaternions there are no other maximally entangled states than those described by [the twelve patterns]".

**The premise already implies a continuum.** The proof of the corollary begins from the concurrence equation above, whose solution set is the entire continuum of maximally entangled states. The clearest family of solutions is

$$
\lvert\psi_\phi\rangle=\tfrac{1}{\sqrt2}\left(\lvert00\rangle+\exp(i\phi)\lvert11\rangle\right),\qquad \phi\in[0,2\pi),
$$

for which $c_1=\tfrac{1}{\sqrt2}$, $c_4=\tfrac{1}{\sqrt2}\exp(i\phi)$, $c_2=c_3=0$, so $c_1c_4=\tfrac12 \exp(i\phi)$, $\lvert c_1c_4-c_2c_3\rvert=\tfrac12$, and $C=1$ for every $\phi$. Every member of the family is maximally entangled. The source's own first case — $\lvert c_1\rvert=\lvert c_4\rvert$, $c_2=c_3=0$ — is exactly this family, so the free relative phase $\phi$ is already present in the source's case analysis.

**What the patterns select.** The twelve written patterns do not enumerate this family. They are obtained from the additional assumption — not part of the concurrence equation — that the quotient of the two amplitudes in the division lies in $\{-i,i,-1\}$. In every one of the twelve forms the relative phase of the two nonzero amplitudes is thereby fixed to one of the four values $0,\pm\pi/2,\pi$. A member of the family with $\phi=\pi/4$, say

$$
\lvert\psi_{\pi/4}\rangle=\tfrac{1}{\sqrt2}\left(\lvert00\rangle+\exp(i\pi/4)\lvert11\rangle\right),
$$

has $C=1$ and is of none of the twelve forms: its relative phase lies outside the discrete set. **Corollary 1 is therefore false as stated.** The twelve patterns are a proper subset of the maximally entangled states, namely the part admitted by the extra quotient assumption. (The source itself remarks that there are "uncountably many" such states, so the corollary can only be read as an exhaustiveness claim; that interpretation is what fails.)

**Why no finite list can work.** The point is dimensional and independent of the source's conventions. The pure states of two qubits are the rays of $\mathbb{C}P^3$, a real manifold of dimension six; the condition that a pure state be maximally entangled, $\mathrm{Tr}_2(\tilde\Pi)=\tfrac12 e_t$, places three independent real conditions on those rays, so the maximally entangled rays form a set of real dimension three. No finite union of one-parameter families — and the twelve patterns amount to that, with the overall complex phase free — can cover a three-dimensional set.

**What remains.** None of this touches the patterns as constructions: each is a maximally entangled state, and their totality is a legitimate partial catalogue, with the Bell states among them. What fails is the exhaustiveness claim, and with it the use of the concurrence criterion as a complete classification. The corpus's own statement is the correct one: the maximally entangled pure states are a continuum, singled out by the partial-trace condition, and any discrete family among them — the Bell basis included — must be selected by additional structure. For the Bell basis that structure is the diagonal tensor form; for the source's patterns it is the quotient rule.

## Partial Traces and Maximal Mixedness

We now compute the partial trace of each Bell idempotent and confirm the maximal-entanglement condition used above.

Because $\tilde\Pi_\epsilon$ is a sum of diagonal tensor terms, the partial trace over the second factor is immediate. Applying $\mathrm{Tr}_2(e_\mu\otimes e_\nu)=e_\mu\,\mathrm{Tr}_\mathbb{B}(e_\nu)$ term by term,

$$
\mathrm{Tr}_2(\tilde\Pi_\epsilon)
=\tfrac{1}{4}\left(\mathrm{Tr}_\mathbb{B}(e_t)\,e_t+\sum_{\mu\in\{x,y,z\}}\epsilon_\mu\,\mathrm{Tr}_\mathbb{B}(\vec e_\mu)\,\vec e_\mu\right)
=\tfrac{1}{4}\left(2\,e_t+0\right)
=\tfrac{1}{2}\,e_t .
$$

The same computation with the roles of the factors exchanged gives

$$
\mathrm{Tr}_1(\tilde\Pi_\epsilon)=\tfrac{1}{2}\,e_t .
$$

The reason is exactly the one identified in the entangled-subsystems article: the entangled terms $\vec e_\mu\otimes \vec e_\mu$ with $\mu \neq t$ are traceless in each factor, so the partial trace keeps only the $e_t\otimes e_t$ term and produces the scalar-only element $\tfrac{1}{2}e_t$, which is not idempotent. The mixedness of the reduced state is the algebraic residue of the entanglement of the joint state.

The reduced state $\tilde{Ϛ}_1=\tilde{Ϛ}_2=\tfrac{1}{2}e_t$ is the maximally mixed qubit state, the centre of the Bloch ball. Its purity and entropy are the standard ones:

$$
\mathrm{Tr}(\tilde{Ϛ}_1^2)=\mathrm{Tr}\!\left(\tfrac{1}{4}e_t\right)=\tfrac{1}{4}\cdot2=\tfrac{1}{2},\qquad
S(\tilde{Ϛ}_1)=-\tfrac12\log\tfrac12-\tfrac12\log\tfrac12=\log 2 .
$$

So each Bell idempotent is maximally entangled in the precise sense of the previous section: its partial trace is maximally mixed, its reduced purity is $\tfrac12$ (the minimum for a qubit), and its reduced entropy is $\log 2$ (the maximum). The computation is the same for all four states and reproduces, for the singlet, the result $\tilde{Ϛ}_1=\tfrac12e_t$ of the entangled-subsystems article and of *Exercise: The Reduced State of an Entangled Subsystem*.

Combined with the previous section, the picture is complete. The four Bell idempotents form an idempotent basis of $\mathbb{B}\otimes\mathbb{B}$; they are the joint eigenbasis of the stabiliser operators $S_1$ and $S_3$; they are the only trace-one diagonal-form idempotents; and their partial traces are all the maximally mixed state $\tfrac{1}{2}e_t$. The Bell basis is thus a canonical object of the tensor-product algebra, singled out by the tensor structure and the stabiliser spectrum, and maximally entangled like every pure state in the surrounding continuum.

## A Remark on the Status of the Tensor Product

The construction above lives entirely inside the tensor-product algebra $\mathbb{B}\otimes\mathbb{B}$. It is therefore worth stating clearly how that algebra stands in the framework, because the companion articles do not speak with one voice about it.

The entangled-subsystems article uses the tensor product directly: it defines the two-qubit state space as $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$, defines the trace by $\mathrm{Tr}(x\otimes y)=\mathrm{Tr}_\mathbb{B}(x)\mathrm{Tr}_\mathbb{B}(y)$, and computes with the singlet idempotent without further comment. The quantum-physics article, in its ten-point checklist, likewise lists a composition rule and calls the tensor product "a natural extension of the framework."

At the same time, the same quantum-physics article lists, among its open questions, the following: "The extension to $n$ qubits requires the tensor product $\mathbb{B}^{\otimes_\mathbb{C}n}$ ... Is the tensor product natural in the biquaternion framework, or does it require additional structure?" The introduction article poses the same point as an open question about the extension to many qubits.

These two positions are not reconciled here. The present article uses the tensor product exactly as the entangled-subsystems article does, and every statement above is a statement about the algebra $\mathbb{B}\otimes\mathbb{B}$ once that algebra is granted. The Bell basis is canonical **relative to** the tensor-product structure: given $\mathbb{B}\otimes\mathbb{B}$ with its trace, the four Bell idempotents are singled out by the stabiliser operators and the diagonal tensor structure, with no further choices.

Whether the tensor-product algebra is itself canonical for the biquaternion framework — whether, that is, the two-qubit algebra is forced by the structure of $\mathbb{B}$, or whether it is one natural construction among several — is the open question. If the tensor product were to require additional structure, then the Bell basis would inherit that contingency: it would be canonical within the tensor-product description, but the passage from one qubit to two would carry an assumption that the framework has not yet justified. This article takes no position on that question; it records it, because the Bell basis is a construction in the tensor-product algebra, and the status of that algebra is exactly what remains open.

## Summary

The four Bell states of two qubits are, in the biquaternion framework, four idempotents of the tensor-product algebra $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$. Following *Exercise: The Correlation Function of the Bell States*, they are written

$$
\tilde\Pi_\epsilon=\tfrac{1}{4}\left(e_t\otimes e_t+\epsilon_1\,\vec e_x\otimes \vec e_x+\epsilon_2\,\vec e_y\otimes \vec e_y+\epsilon_3\,\vec e_z\otimes \vec e_z\right),
\qquad \epsilon_1\epsilon_2\epsilon_3=+1 ,
$$

one for each of the four admissible sign triples.

The article established the following structure.

- **Idempotent basis.** The four $\tilde\Pi_\epsilon$ are Hermitian idempotents of trace one, pairwise orthogonal, summing to the identity: $\tilde\Pi_\epsilon \tilde\Pi_{\epsilon'}=\delta_{\epsilon\epsilon'}\tilde\Pi_\epsilon$ and $\sum_\epsilon \tilde\Pi_\epsilon=e_t\otimes e_t$. They form a maximal orthogonal family of minimal idempotents — an idempotent basis — of the two-qubit algebra, whose span is a Cartan subalgebra of dimension four.
- **Stabiliser eigenbasis.** The commuting Hermitian involutions $S_1=-\vec e_x\otimes \vec e_x$ and $S_3=-\vec e_z\otimes \vec e_z$ (corresponding to $\sigma_1\otimes\sigma_1$ and $\sigma_3\otimes\sigma_3$) form a complete set of commuting observables whose joint spectrum is non-degenerate; the $\tilde\Pi_\epsilon$ are its joint eigen-idempotents, with eigenvalues $(-\epsilon_1,-\epsilon_3)$. Each $\tilde\Pi_\epsilon$ is conjugation-invariant under $S_1$ and $S_3$, and its stabiliser group is the Klein four-group generated by the sign-corrected $S_1$ and $S_3$.
- **Diagonal tensor structure.** The Bell idempotents are exactly the idempotents of diagonal tensor form $\tfrac14\sum_\mu\epsilon_\mu\,e_\mu\otimes e_\mu$. There are exactly four of them, and the sign matrix whose rows are $(1,\epsilon_1,\epsilon_2,\epsilon_3)$ is Hadamard. A generic maximally entangled state is a continuum and is not diagonal; the Bell basis is the discrete, canonical family selected by the diagonal structure.
- **Maximal mixedness.** The partial trace of every Bell idempotent is the maximally mixed state, $\mathrm{Tr}_1(\tilde\Pi_\epsilon)=\mathrm{Tr}_2(\tilde\Pi_\epsilon)=\tfrac12 e_t$, of purity $\tfrac12$ and entropy $\log 2$. The four states are locally indistinguishable; their distinction resides entirely in the correlated tensor terms, i.e. in the signs $\epsilon$.
- **State vector versus state operator.** The Bell states also have a vector form in $\mathbb{C}^4\cong\mathbb{B}$, where they are the combinations $\tfrac{1}{\sqrt2}(e_\mu\pm e_\nu)$ for the unit pairs $\{e_t,e_z\}$ and $\{e_x,e_y\}$. The vector is not the state: it is an element of the four-dimensional module, while the state object is the rank-one idempotent of the sixteen-dimensional algebra. In particular a single quaternion, read as a two-qubit vector, is a product state — $Q=\tfrac12(e_t-\vec e_x-\vec e_y+\vec e_z)$ has concurrence zero — and never carries entanglement.
- **Maximal entanglement is a continuum, not a finite list.** A claimed enumeration of twelve patterns of maximally entangled states, obtained under an extra quotient rule, fails its exhaustiveness corollary: the family $\lvert\psi_\phi\rangle=\tfrac{1}{\sqrt2}(\lvert00\rangle+\exp(i\phi)\lvert11\rangle)$ is maximally entangled for every $\phi$, while the twelve forms fix the relative phase to $\{0,\pm\pi/2,\pi\}$. The maximally entangled rays have real dimension three, so no finite union of one-parameter families covers them; any discrete family among them is selected by additional structure.

All of this is standard finite-dimensional algebra, expressed in the conventions of the companion articles. The construction presupposes the tensor-product algebra $\mathbb{B}\otimes\mathbb{B}$; whether that algebra is canonical for the framework is an open question inherited from the companion articles and is left unresolved.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$ | Two-qubit tensor-product algebra |
| $\mathbb{C}^2\otimes\mathbb{C}^2\cong\mathbb{C}^4\cong\mathbb{B}$ | Two-qubit state space (state vectors) |
| $\tfrac{1}{\sqrt2}(e_t\pm \vec e_z),\ \tfrac{1}{\sqrt2}(\vec e_x\pm \vec e_y)$ | Bell vectors written in the algebra basis |
| $C=2\lvert c_1c_4-c_2c_3\rvert$ | Concurrence of a two-qubit pure state |
| $\lvert\psi_\phi\rangle=\tfrac{1}{\sqrt2}(\lvert00\rangle+\exp(i\phi)\lvert11\rangle)$ | Maximally entangled family, $C=1$ for every $\phi$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\mu^2=-e_t$, cyclic products |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_+$ | Hermitian subspace: real scalar, imaginary vector |
| $\mathrm{Tr}_\mathbb{B}$ | Trace on a single factor: $\mathrm{Tr}_\mathbb{B}(e_t)=2$, $\mathrm{Tr}_\mathbb{B}(\vec e_\mu)=0$ |
| $\mathrm{Tr}(x\otimes y)=\mathrm{Tr}_\mathbb{B}(x)\mathrm{Tr}_\mathbb{B}(y)$ | Trace on the tensor product |
| $\mathrm{Tr}_1,\mathrm{Tr}_2$ | Partial traces |
| $\tilde\Pi_{\mathrm{singlet}}=\tfrac14(e_t\otimes e_t+\sum_\mu \vec e_\mu\otimes \vec e_\mu)$ | Singlet idempotent |
| $\tilde\Pi_\epsilon=\tfrac14(e_t\otimes e_t+\sum_\mu\epsilon_\mu \vec e_\mu\otimes \vec e_\mu)$ | Bell idempotent, $\epsilon_1\epsilon_2\epsilon_3=+1$ |
| $\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)$ | Sign pattern labelling a Bell state |
| $S_1=-\vec e_x\otimes \vec e_x,\ S_3=-\vec e_z\otimes \vec e_z$ | Stabiliser involutions ($\leftrightarrow\sigma_1\otimes\sigma_1,\ \sigma_3\otimes\sigma_3$) |
| $S_1S_3=\vec e_y\otimes \vec e_y$ | Product of the stabiliser involutions |
| $S_\mu\tilde\Pi_\epsilon=-\epsilon_\mu\tilde\Pi_\epsilon$ | Eigenvalue relation |
| $\mathrm{Tr}_2(\tilde\Pi_\epsilon)=\mathrm{Tr}_1(\tilde\Pi_\epsilon)=\tfrac12 e_t$ | Maximally mixed reduced state |
| $T_{\nu\nu}=-\epsilon_\nu$ | Diagonal correlation matrix entry |
| $e_t\mapsto I_2,\ \vec e_\mu\mapsto-i\sigma_\mu$ | Isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

## Further Reading

- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Bell states, the Bell basis, the stabiliser formalism, and the standard treatment of maximal entanglement.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard textbook treatment of two spin-$\tfrac{1}{2}$ particles and the Bell states.
- A. Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for the density-matrix formalism, partial traces, and maximal entanglement.
- C. H. Bennett, G. Brassard, C. Crépeau, R. Jozsa, A. Peres, and W. K. Wootters, "Teleporting an unknown quantum state via dual classical and Einstein–Podolsky–Rosen channels," *Physical Review Letters* **70** (1993) 1895–1899, for the Bell-basis measurement and its role in quantum information.
- R. F. Werner, "All teleportation and dense coding schemes," *Journal of Physics A: Mathematical and General* **34** (2001) 7081–7094, for the classification of maximally entangled states and the role of the Bell basis.
- S. L. Braunstein, A. Mann, and M. Revzen, "Maximal violation of Bell inequalities for mixed states," *Physical Review Letters* **68** (1992) 3259–3261, for the correlation structure of the Bell states.
- Lidia Obojska, "Bi-particle entanglement and its quaternion representation," *Journal of Physics Communications* **2** (2018) 085021, for the interpretation of a bipartite state as the division of one particle, and "Patterns of maximally entangled states within the algebra of biquaternions," *Journal of Physics Communications* **4** (2020) 055018, for the twelve-pattern catalogue and the exhaustiveness claim examined in *A Claimed Enumeration of the Maximally Entangled States*.
- The companion articles of this series: *Introduction to the Biquaternion Universe*, *The Material Sector: Four-Vectors, Interval and Lorentz Action*, *The Informational Sector: States, Observables and Probability*, *Quantum Physics in Biquaternionic Form*, *Entangled Subsystems in the Biquaternion Framework*, *Exercise: Two Spins in the Singlet State*, and *Exercise: The Correlation Function of the Bell States*.
