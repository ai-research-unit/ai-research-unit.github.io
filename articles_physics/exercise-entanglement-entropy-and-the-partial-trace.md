# __Exercise: Entanglement Entropy and the Partial Trace__

## Introduction

This article is one of a series of **worked exercises** that illustrate quantum physics in two parallel presentations: the standard Hilbert-space formulation, and the biquaternion formulation developed in the companion articles. The goal is not to derive new physics, but to give a concrete, computationally explicit demonstration of the correspondence between the two formalisms.

The immediately preceding exercise, *Exercise: The Reduced State of an Entangled Subsystem*, introduced the partial trace $\mathrm{Tr}_2$ and computed the reduced state of the singlet. That exercise is about the **state**; it observed, in passing, that the reduced state $\tfrac12 e_t$ has von Neumann entropy $\log 2$. The present exercise is about that number. It poses the computation of the **entanglement entropy** of a general pure two-qubit state, works the solution by two routes — the Schmidt decomposition, and the partial trace in $\mathbb{B}\otimes\mathbb{B}$ — and closes with further problems left to the reader. The reduced state of the singlet is used here only as a limiting case, and its computation is not repeated.

The exercise applies three results of the parent articles and assumes them without rederivation: the partial trace $\mathrm{Tr}_2(a\otimes b)=a\,\mathrm{Tr}_\mathbb{B}(b)$ and its mirror $\mathrm{Tr}_1(a\otimes b)=b\,\mathrm{Tr}_\mathbb{B}(a)$, established in *Entangled Subsystems in the Biquaternion Framework* and *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*; the single-qubit spectral decomposition and entropy of *Quantum Physics in Biquaternionic Form*, namely $\tilde{Ϛ}=\lambda_+\tilde\Pi_1(\vec u_r)+\lambda_-\tilde\Pi_2(\vec u_r)$ with $\lambda_\pm=\tfrac12(1\pm|\vec r|)$ and $S(\tilde{Ϛ})=-\lambda_+\log\lambda_+-\lambda_-\log\lambda_-$; and the Bell idempotent basis $\tilde\Pi_\epsilon$ of *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*. The article also takes up one of the open questions of *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* — whether the candidate entropy functional $S(\tilde{Ϛ})=-2\,\mathrm{Sc}(\tilde{Ϛ}\log\tilde{Ϛ})$ is correct — and reports what the recomputation gives, including the point at which the candidate's domain ends.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$. The quaternion units are $e_t=1,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_k^2=-e_t$, and $i$ is the scalar imaginary, $i^2=-1$. The trace of an element of $\mathbb{M}_+$ is twice its scalar part, $\mathrm{Tr}(\tilde{Q})=2\,\mathrm{Sc}(\tilde{Q})$, and in particular $\mathrm{Tr}(\tilde\Pi\tilde H)=2\,\mathrm{Sc}(\tilde\Pi\tilde H) = 2\langle\tilde\Pi,\tilde{H}\rangle$ for idempotent $\tilde\Pi$ and Hermitian $\tilde{H}$. The two-qubit state space is the tensor product $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$, with $\mathrm{Tr}(x\otimes y)=\mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y)$. Throughout, $\log$ denotes the natural logarithm, and

$$
h(p)=-p\log p-(1-p)\log(1-p),\qquad p\in[0,1],
$$

is the binary entropy, with the convention $0\log 0=0$.

## The Exercise

Two spin-$\tfrac{1}{2}$ particles are prepared in a pure state $|\psi\rangle$ of the two-qubit Hilbert space $\mathbb{C}^2\otimes\mathbb{C}^2$. Let

$$
\rho=|\psi\rangle\langle\psi|,\qquad
\rho_1=\mathrm{Tr}_2(\rho),\qquad
\rho_2=\mathrm{Tr}_1(\rho),
$$

be the joint state and the two reduced states. The **entanglement entropy** of $|\psi\rangle$ is the von Neumann entropy of either reduced state,

$$
S=-\,\mathrm{Tr}\!\left(\rho_1\log\rho_1\right).
$$

The exercise has four parts.

1. **The two reduced states carry the same entropy.** Show that $S(\rho_1)=S(\rho_2)$, and identify the invariant on which $S$ depends.
2. **A worked family.** For

$$
|\psi_\theta\rangle=\cos\theta\,|\uparrow\uparrow\rangle+\sin\theta\,|\downarrow\downarrow\rangle,\qquad \theta\in[0,\tfrac{\pi}{4}],
$$

compute $\rho_1$ and $S$ explicitly, first in the standard formulation and then in the biquaternion formulation.
3. **The limits.** Check that $S$ vanishes on the product states and equals $\log 2$ on the Bell states, and locate the maximum.
4. **The entropy functional.** Decide whether the candidate

$$
S(\tilde{Ϛ})=-\,2\,\mathrm{Sc}\!\left(\tilde{Ϛ}\log\tilde{Ϛ}\right)
$$

proposed as an open question in *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* is correct, and state its domain.

A fifth part, which is not a computation but a warning, is developed in the section *A case the partial trace does not decide*: the entropy of the reduced state is an entanglement measure **for pure joint states only**, and the exercise states the counterexample rather than leaving the impression that the partial trace alone measures entanglement in general.

## Solution I: The Schmidt Route

### The reduced states from the coefficient matrix

Write the pure state in the product basis,

$$
|\psi\rangle=\sum_{i,j\in\{0,1\}}M_{ij}\,|i\rangle|j\rangle,
\qquad |0\rangle=|\uparrow\rangle,\quad |1\rangle=|\downarrow\rangle,
$$

with a complex $2\times2$ coefficient matrix $M=(M_{ij})$. Normalisation is

$$
\langle\psi|\psi\rangle=\sum_{i,j}|M_{ij}|^2=\mathrm{Tr}(MM^\dagger)=1 .
$$

The partial traces are computed directly from this form. The matrix elements of $\rho_1$ are

$$
(\rho_1)_{ii'}=\sum_j M_{ij}\overline{M_{i'j}}=(MM^\dagger)_{ii'},
$$

and those of $\rho_2$ are

$$
(\rho_2)_{jj'}=\sum_i M_{ij}\overline{M_{ij'}}=(M^\dagger M)_{jj'} .
$$

So the reduced states are the two products of the coefficient matrix with its adjoint:

$$
\boxed{\;\rho_1=MM^\dagger,\qquad \rho_2=M^\dagger M.\;}
$$

For the worked family the matrix is $M_\theta=\mathrm{diag}(\cos\theta,\sin\theta)$, so $\rho_1=\rho_2=\mathrm{diag}(\cos^2\theta,\sin^2\theta)$ immediately; the general structural statement is the subject of the next subsection.

### The Schmidt decomposition, and why the two entropies agree

The singular value decomposition of $M$ is

$$
M=U\Sigma V^\dagger,\qquad \Sigma=\mathrm{diag}(s_1,s_2),\quad s_1\ge s_2\ge 0,
$$

with $U,V$ unitary. The $s_i$ are the **Schmidt coefficients** of $|\psi\rangle$, and normalisation reads $s_1^2+s_2^2=1$. Substituting into $|\psi\rangle=\sum_{ij}M_{ij}|i\rangle|j\rangle$ gives the **Schmidt decomposition**

$$
|\psi\rangle=s_1\,|u_x\rangle|v_1\rangle+s_2\,|u_y\rangle|v_2\rangle,
$$

where $|u_k\rangle=\sum_i U_{ik}|i\rangle$ and $|v_k\rangle=\sum_j V_{jk}|j\rangle$ are orthonormal bases of the two factors. The reduced states are then

$$
\rho_1=MM^\dagger=\sum_{k}s_k^2\,|u_k\rangle\langle u_k|,
\qquad
\rho_2=M^\dagger M=\sum_{k}s_k^2\,|v_k\rangle\langle v_k| .
$$

This is the whole content of part (a) of the exercise. $\rho_1$ and $\rho_2$ are **not** equal in general — they act on different factors and have different eigenvectors — but they have the **same eigenvalues**, namely $s_1^2,s_2^2$, because the nonzero eigenvalues of $MM^\dagger$ and $M^\dagger M$ coincide. The entropy is a function of the spectrum alone, so

$$
S(\rho_1)=S(\rho_2)=-\sum_k s_k^2\log s_k^2
=h(s_1^2),
$$

using $s_1^2+s_2^2=1$ and $h(1-p)=h(p)$. The invariant on which the entanglement entropy depends is the **larger Schmidt coefficient squared**, $s_1^2\in[\tfrac12,1]$, or equivalently the pair of Schmidt coefficients; it is not the full state. For two qubits there is only one independent Schmidt parameter, and the entropy is the binary entropy of it.

Two immediate consequences, which are part (c) of the exercise:

- $S=0$ if and only if one Schmidt coefficient vanishes, i.e. $|\psi\rangle$ is a **product state** $|u\rangle|v\rangle$.
- $S=\log 2$ if and only if $s_1=s_2=1/\sqrt2$, i.e. $|\psi\rangle$ is **maximally entangled**. The four Bell states are the canonical examples, but they are not the only ones: any state of the form $(\tilde{U}\otimes\tilde{V})|\Phi^+\rangle$ with local unitaries is maximally entangled.

The maximally entangled states are therefore a **continuum**, of three real dimensions among the six of the pure-state rays, and no finite catalogue exhausts them. A source that lists twelve patterns of maximally entangled states and claims they are all of them (Obojska, *Journal of Physics Communications* **4** (2020) 055018) is mistaken for exactly this reason: the twelve patterns are a measure-zero subset selected by an extra quotient rule on the amplitudes, and the family $\tfrac{1}{\sqrt2}(|00\rangle+\exp(i\phi)|11\rangle)$ is a counterexample for every $\phi$ outside the discrete set the patterns allow. The computation is in *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*, in the section *A Claimed Enumeration of the Maximally Entangled States*.

Since $h$ is strictly concave on $[0,1]$, its maximum over the admissible range $s_1^2\in[\tfrac12,1]$ is at $s_1^2=\tfrac12$, with value $\log2$; its minimum is $0$ at $s_1^2=1$. There is no other case for two qubits: the entropy is either $0$, $\log2$, or a value of $h(p)$ strictly between them.

## Solution II: The Biquaternion Route

### The biquaternion form of the worked family

The two-qubit state space is $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$, and the pure state $|\psi_\theta\rangle$ corresponds to a Hermitian idempotent $\tilde\Pi_\theta$ of trace one. To write it in the tensor basis, expand the joint density in Pauli strings and translate with the isomorphism of the companion articles, $e_t\mapsto I_2$ and $\vec e_k\mapsto -i\sigma_k$. Equivalently, $\sigma_k\mapsto i \vec e_k$.

For the state $|\psi_\theta\rangle=\cos\theta\,|\uparrow\uparrow\rangle+\sin\theta\,|\downarrow\downarrow\rangle$, the Pauli-string coefficients $R_{\mu\nu}=\langle\sigma_\mu\otimes\sigma_\nu\rangle$, with $\sigma_t=I_2$ and $\mu,\nu\in\{t,x,y,z\}$, are

$$
R_{tt}=1,\qquad R_{tz}=R_{zt}=\cos 2\theta,\qquad R_{zz}=1,
$$
$$
R_{xx}=\sin 2\theta,\qquad R_{yy}=-\sin 2\theta,
$$

and all other $R_{\mu\nu}$ vanish. The entries are recomputed directly: the diagonal weights give $R_{tz}=R_{zt}=\cos^2\theta-\sin^2\theta=\cos2\theta$ and $R_{zz}=\cos^2\theta+\sin^2\theta=1$; the only off-diagonal coherence is $\langle\uparrow\uparrow|\psi_\theta\rangle\langle\psi_\theta|\downarrow\downarrow\rangle$, which produces $R_{xx}=\sin2\theta$ via $\sigma_1\otimes\sigma_1$ and $R_{yy}=-\sin2\theta$ via $\sigma_2\otimes\sigma_2$. Translating $\sigma_\mu\otimes\sigma_\nu\mapsto(ie_\mu)\otimes(ie_\nu)$ (with $ie_t\mapsto e_t$) gives

$$
\tilde\Pi_\theta=\tfrac14\Bigl(e_t\otimes e_t-\vec e_z\otimes \vec e_z
+\sin2\theta\,\bigl(\vec e_y\otimes \vec e_y-\vec e_x\otimes \vec e_x\bigr)
+i\cos2\theta\,\bigl(\vec e_z\otimes e_t+e_t\otimes \vec e_z\bigr)\Bigr).
$$

At $\theta=0$ this reduces to $\tilde\Pi_1\otimes \tilde\Pi_1$, a product idempotent; at $\theta=\tfrac{\pi}{4}$ it reduces to the Bell idempotent $\tilde\Pi_{\Phi^+}$. It is therefore the correct one-parameter interpolation between the product state $|\uparrow\uparrow\rangle$ and the maximally entangled $|\Phi^+\rangle$.

### The partial trace

The partial trace over the second factor acts on the tensor basis by

$$
\mathrm{Tr}_2(e_\mu\otimes e_\nu)=e_\mu\,\mathrm{Tr}_\mathbb{B}(e_\nu)
=2\,\delta_{\nu t}\,e_\mu,
$$

because $\mathrm{Tr}_\mathbb{B}(e_t)=2$ and $\mathrm{Tr}_\mathbb{B}(\vec e_k)=0$ for $k\in\{x,y,z\}$. Term by term:

- $\tfrac14 e_t\otimes e_t\mapsto\tfrac14\cdot 2\,e_t=\tfrac12 e_t$;
- $-\tfrac14 \vec e_z\otimes \vec e_z\mapsto 0$;
- $\tfrac14\sin2\theta\,(\vec e_y\otimes \vec e_y-\vec e_x\otimes \vec e_x)\mapsto 0$;
- $\tfrac14 i\cos2\theta\,\vec e_z\otimes e_t\mapsto\tfrac14 i\cos2\theta\cdot 2\,\vec e_z=\tfrac{i\cos2\theta}{2}\vec e_z$;
- $\tfrac14 i\cos2\theta\,e_t\otimes \vec e_z\mapsto 0$.

Summing,

$$
\boxed{\;\tilde{Ϛ}_1=\mathrm{Tr}_2(\tilde\Pi_\theta)=\tfrac12 e_t+\tfrac{i\cos2\theta}{2}\vec e_z
=\tfrac12\left(e_t+i\cos2\theta\,\vec e_z\right).\;}
$$

This is a state of $\mathbb{M}_+$ of the standard form $\tfrac12(e_t+i\vec r)$ with Bloch vector

$$
\vec r=\cos2\theta\,\vec e_z,\qquad |\vec r|=|\cos2\theta| .
$$

The mechanism is worth naming precisely, because it corrects an interpretation that the Bell case invites. The terms that survive the partial trace are those with $e_t$ in the **second** factor. For the Bell idempotents the only such term is $e_t\otimes e_t$, which is why their reduced state is scalar; but the general entangled state also carries terms $e_\mu\otimes e_t$ with $\mu\in\{x,y,z\}$, and those survive and make the reduced state non-scalar. Here the term $i\cos2\theta\,\vec e_z\otimes e_t$ is exactly what turns $\tfrac12 e_t$ into $\tfrac12(e_t+i\cos2\theta\,\vec e_z)$. The rule is not "only $e_t\otimes e_t$ survives"; it is "only terms with $e_t$ in the traced factor survive".

### The entropy from the single-qubit formula

The reduced state is an element of $\mathbb{M}_+$ with Bloch vector of length $|\cos2\theta|$. The parent article *Quantum Physics in Biquaternionic Form* gives the spectral decomposition and entropy of such a state:

$$
\lambda_\pm=\tfrac12\left(1\pm|\vec r|\right),
\qquad
S(\tilde{Ϛ})=-\lambda_+\log\lambda_+-\lambda_-\log\lambda_- .
$$

For $\theta\in[0,\tfrac{\pi}{4}]$, $\cos2\theta\ge0$, so $|\vec r|=\cos2\theta$ and

$$
\lambda_+=\tfrac{1+\cos2\theta}{2}=\cos^2\theta,\qquad
\lambda_-=\tfrac{1-\cos2\theta}{2}=\sin^2\theta,
$$

and therefore

$$
\boxed{\;S(\tilde{Ϛ}_1)=-\cos^2\theta\,\log\cos^2\theta-\sin^2\theta\,\log\sin^2\theta
=h(\cos^2\theta).\;}
$$

This agrees with the Schmidt route, as it must: the Schmidt coefficients of $|\psi_\theta\rangle$ are $(\cos\theta,\sin\theta)$, and $h(\cos^2\theta)=h(s_1^2)$. The biquaternion route reaches the same number by a different mechanism — it never diagonalises $M$; it reads the Bloch vector off the partial trace and then uses the single-qubit entropy formula on $\mathbb{M}_+$.

At the endpoints:

$$
\theta=0:\quad \tilde{Ϛ}_1=\tilde\Pi_1,\quad \vec r=\vec e_z,\quad S=0;
$$
$$
\theta=\tfrac{\pi}{4}:\quad \tilde{Ϛ}_1=\tfrac12 e_t,\quad \vec r=0,\quad S=\log2 .
$$

The value at $\theta=\tfrac{\pi}{4}$ is $\log2$, the same entropy as the reduced state of the singlet computed in *Exercise: The Reduced State of an Entangled Subsystem*; here it appears as one endpoint of a continuous curve, at the maximally entangled Bell state $|\Phi^+\rangle$ rather than at the singlet.

### The general biquaternion statement

The worked family is the special case of a general statement, which is the biquaternion form of the Schmidt theorem. Let $\tilde\Pi$ be a pure two-qubit idempotent of $\mathbb{B}\otimes\mathbb{B}$, and let

$$
\tilde{Ϛ}_1=\mathrm{Tr}_2(\tilde\Pi)=\tfrac12\left(e_t+i\vec r_1\right),
\qquad
\tilde{Ϛ}_2=\mathrm{Tr}_1(\tilde\Pi)=\tfrac12\left(e_t+i\vec r_2\right)
$$

be its reduced states. Then $\tilde{Ϛ}_1$ and $\tilde{Ϛ}_2$ are states of $\mathbb{M}_+$, and their spectra are $(1\pm|\vec r_1|)/2$ and $(1\pm|\vec r_2|)/2$. The Schmidt theorem says the spectra coincide, hence

$$
|\vec r_1|=|\vec r_2|,
\qquad
S(\tilde{Ϛ}_1)=S(\tilde{Ϛ}_2)
=h\!\left(\frac{1+|\vec r_1|}{2}\right).
$$

So the entanglement entropy of a pure two-qubit state is a function of a single invariant, the **length of either reduced Bloch vector**. Maximal entanglement is $|\vec r_1|=0$; a product state is $|\vec r_1|=1$. The reduced Bloch vectors may point in different directions — they do, in general, since they live on different factors — but their lengths agree.

## The Entropy Functional on $\mathbb{M}_+$

The parent article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* closes its list of open questions with the following: the logarithm on $\mathbb{B}$ exists but is multivalued, the trace is available but is a scalar, and "a natural candidate would be $S(\tilde{Ϛ})=-2\,\mathrm{Sc}(\tilde{Ϛ}\log\tilde{Ϛ})$, but this needs verification." The candidate can now be checked.

Let $\tilde{Ϛ}=\tfrac12(e_t+i\vec r)$ be a state with $0<|\vec r|<1$. Its eigenvalues are $\lambda_\pm=\tfrac12(1\pm|\vec r|)$, both positive, and its spectral decomposition is

$$
\tilde{Ϛ}=\lambda_+\,\tilde\Pi_1(\vec u_r)
+\lambda_-\,\tilde\Pi_2(\vec u_r),
\qquad \vec u_r=\vec r/|\vec r| .
$$

The **principal** logarithm of the parent's elementary-functions article, applied to this element, is the spectral logarithm:

$$
\log\tilde{Ϛ}
=\tfrac12\log(\lambda_+\lambda_-)\,e_t
+\tfrac{i}{2}\log\frac{\lambda_+}{\lambda_-}\,\vec u_r
=\log\lambda_+\,\tilde\Pi_1(\vec u_r)
+\log\lambda_-\,\tilde\Pi_2(\vec u_r).
$$

The two expressions agree because $\tfrac12(e_t\pm i\vec u_r)=\tilde\Pi_{1,2}(\vec u_r)$ and because $\log(\lambda_+\lambda_-)=2\log R$, $\log(\lambda_+/\lambda_-)=2\Theta/i$ in the notation of that article. Multiplying and taking the scalar part,

$$
\tilde{Ϛ}\log\tilde{Ϛ}
=\lambda_+\log\lambda_+\,\tilde\Pi_1(\vec u_r)
+\lambda_-\log\lambda_-\,\tilde\Pi_2(\vec u_r),
$$

since the idempotents are orthogonal. Using $\mathrm{Sc}(\tilde\Pi_{1,2})=\tfrac12$,

$$
2\,\mathrm{Sc}\!\left(\tilde{Ϛ}\log\tilde{Ϛ}\right)
=\lambda_+\log\lambda_++\lambda_-\log\lambda_-
=\mathrm{Tr}\!\left(\tilde{Ϛ}\log\tilde{Ϛ}\right),
$$

the last equality being the general trace identity $\mathrm{Tr}(\tilde{Q})=2\,\mathrm{Sc}(\tilde{Q})$. Hence

$$
-2\,\mathrm{Sc}\!\left(\tilde{Ϛ}\log\tilde{Ϛ}\right)
=-\mathrm{Tr}\!\left(\tilde{Ϛ}\log\tilde{Ϛ}\right)
=S(\tilde{Ϛ}).
$$

**The candidate is correct**, for states in the interior of the Bloch ball, with the principal branch of the logarithm. The maximally mixed case $\vec r=0$ is the scalar case, where the same computation with $\log(\tfrac12 e_t)=\log\tfrac12\,e_t$ gives $S=\log2$; the case $|\vec r|=1$ is excluded and is discussed below. The scalar part is not an obstruction: because the trace on $\mathbb{B}$ *is* twice the scalar part, the candidate is not an analogue of the trace formula but the trace formula itself.

Two qualifications belong with the verification, and neither is a defect of the formula.

**The branch is load-bearing.** The biquaternion logarithm is multivalued. The genuine extra branches — an added $2\pi i n\,e_t$ in the scalar part, or a shift $\Theta\mapsto\Theta+2\pi k$ in the angle — change $\mathrm{Sc}(\tilde{Ϛ}\log\tilde{Ϛ})$ by a purely imaginary amount, so what is branch-dependent is the *complex* value of the candidate, not its real part. The candidate must nonetheless be read with the principal branch, the one that agrees with the spectral logarithm, because that is the branch that makes $S$ real and equal to $-\mathrm{Tr}(\tilde{Ϛ}\log\tilde{Ϛ})$.

**The domain ends at the pure states.** The logarithm of a biquaternion exists exactly on the group of units $\langle\tilde{Q}\rangle_{\natural}\neq0$. A pure state $\tilde{Ϛ}=\tilde\Pi(\vec u_r)=\tfrac12(e_t+i\vec u_r)$ is an idempotent and a zero divisor: $\langle\tilde{Ϛ}\rangle_{\natural}=0$. So the logarithm, and with it the candidate functional, is undefined at $|\vec r|=1$. The value $S=0$ at the pure states is the continuous limit of the formula as $|\vec r|\to1$, not a value the formula takes. The parent's single-qubit entropy formula escapes this limitation only in appearance: it is written in terms of the eigenvalues $\lambda_\pm$, which remain defined at the boundary, whereas the candidate is written in terms of $\log\tilde{Ϛ}$, which does not. On the interior the two agree exactly; on the boundary only the eigenvalue form survives.

## A Case the Partial Trace Does Not Decide

The fifth part of the exercise is a warning as much as a computation. The phrase "entanglement entropy" suggests that $S(\rho_1)$ measures the entanglement of the joint state. For **pure** joint states it does, by the Schmidt theorem. For **mixed** joint states it does not, and the counterexample is elementary.

Consider the equal mixture of the two Bell idempotents $\tilde\Pi_{\Phi^+}$ and $\tilde\Pi_{\Phi^-}$,

$$
\tilde{Ϛ}_{\mathrm{mix}}=\tfrac12 \tilde\Pi_{\Phi^+}+\tfrac12 \tilde\Pi_{\Phi^-}.
$$

Its partial trace is $\tfrac12 e_t$ on each factor, since every Bell idempotent has $\mathrm{Tr}_1(\tilde\Pi_\epsilon)=\mathrm{Tr}_2(\tilde\Pi_\epsilon)=\tfrac12 e_t$ and the partial trace is linear. Hence

$$
\tilde{Ϛ}_1=\tfrac12 e_t,\qquad |\vec r_1|=0,\qquad S(\tilde{Ϛ}_1)=\log2 .
$$

So the partial-trace entropy is maximal. But the joint state is **separable**. Using $\tilde\Pi_{\Phi^\pm}=\tfrac14(e_t\otimes e_t\mp \vec e_x\otimes \vec e_x\pm \vec e_y\otimes \vec e_y-\vec e_z\otimes \vec e_z)$, the mixture is

$$
\tilde{Ϛ}_{\mathrm{mix}}=\tfrac14\left(e_t\otimes e_t-\vec e_z\otimes \vec e_z\right)
=\tfrac12\,\tilde\Pi_1\otimes \tilde\Pi_1
+\tfrac12\,\tilde\Pi_2\otimes \tilde\Pi_2,
$$

a classical mixture of the product states $|\uparrow\uparrow\rangle$ and $|\downarrow\downarrow\rangle$. Its entanglement is zero by any measure; its reduced entropy is maximal. The number $\log2$ here measures the mixedness of the *marginal*, not the entanglement of the *joint state*.

The lesson is not that the partial trace is wrong but that its entropy has two roles that coincide only for pure states. For a pure $|\psi\rangle$, $S(\mathrm{Tr}_2|\psi\rangle\langle\psi|)$ is the entanglement entropy. For a mixed $\rho$, $S(\mathrm{Tr}_2\rho)$ is the entropy of a marginal; it is not an entanglement measure, and no function of $\rho_1$ alone can be one, because many joint states with different entanglement share the same marginals. The mixed-state measure — the entanglement of formation, or the relative entropy of entanglement — requires more than the partial trace, and is not developed in this series. That is a genuine gap, and it is the gap the title of this exercise does not close.

## Further Problems

The following problems extend the exercise. They are left to the reader; the first three are routine applications of the methods above, the last three raise the questions the methods do not settle.

**P1 (the other real family).** For $|\psi\rangle=\cos\theta\,|\uparrow\downarrow\rangle+\sin\theta\,|\downarrow\uparrow\rangle$, compute $\rho_1$, $\rho_2$ and $S$. Show that $\rho_1$ and $S$ are *the same* as for the family of the worked solution, while $\rho_2$ has its two eigenvalues exchanged, so that the two families are indistinguishable by any measurement on the **first** particle, even though at $\theta=\tfrac{\pi}{4}$ they are the different Bell states $|\Psi^+\rangle$ and $|\Phi^+\rangle$. (Hint: the Schmidt coefficients are unchanged; the difference is in which factor carries which Schmidt vector, equivalently in the tensor terms of the idempotent.)

**P2 (general pure state).** For arbitrary $|\psi\rangle=\sum_{ij}M_{ij}|i\rangle|j\rangle$, express $S$ in terms of $\det M$. Show $S=h\!\left(\tfrac{1+\sqrt{1-4|\det M|^2}}{2}\right)$ and hence that $S$ is determined by $|\det M|$ alone. (For two qubits $s_1^2s_2^2=|\det M|^2$.)

**P3 (local invariance).** Show that under a local rotor conjugation $\tilde\Pi\mapsto(\tilde{U}_1\otimes\tilde{U}_2)\,\tilde\Pi\,(\tilde{U}_1^{*}\otimes\tilde{U}_2^{*})$ with $\tilde{U}_j\tilde{U}_j^{*}=e_t$, the reduced state transforms as $\tilde{Ϛ}_1\mapsto\tilde{U}_1\tilde{Ϛ}_1\tilde{U}_1^{*}$, and hence $S$ is invariant. In the biquaternion language, identify the induced action on the Bloch vectors $\vec r_1,\vec r_2$ and check that their lengths are unchanged.

**P4 (the shape of the curve).** Show that $S=h(\cos^2\theta)$ is concave in $p=\cos^2\theta$, that

$$
\frac{\mathrm{d}S}{\mathrm{d}\theta}=2\sin2\theta\,\log\cot\theta\;\ge\;0
\qquad\text{on }[0,\tfrac{\pi}{4}],
$$

vanishing at both endpoints, and that with respect to the Schmidt weight $p=s_1^2\in[\tfrac12,1]$,

$$
\frac{\mathrm{d}S}{\mathrm{d}p}=\log\frac{1-p}{p}\;\le\;0,
$$

which tends to $-\infty$ as $p\to1$. Interpret: as entanglement is switched on from a product state the entropy rises with an infinite slope in $p$, whereas at maximal entanglement ($p=\tfrac12$) the slope vanishes; the last increment of entanglement is entropically the cheapest.

**P5 (the mixed-state question, unresolved).** For the Bell-diagonal mixture $\tilde{Ϛ}_p=p\tilde\Pi_{\Phi^+}+(1-p)\tilde\Pi_{\Phi^-}$, show that $\tilde{Ϛ}_1=\tfrac12 e_t$ and $S(\tilde{Ϛ}_1)=\log2$ for every $p\in[0,1]$, while the joint state is separable at least at $p=\tfrac12$. Determine the set of $p$ for which $\tilde{Ϛ}_p$ is entangled, and show that no function of $\tilde{Ϛ}_1$ can reproduce that set. What extra data about $\tilde{Ϛ}$ is needed? (The answer is the subject of the entanglement-of-formation literature; it is not developed in this series.)

**P6 (purification).** Show that for any state $\tilde{Ϛ}_1$ of $\mathbb{M}_+$ there is a pure two-qubit idempotent $\tilde\Pi$ in $\mathbb{B}\otimes\mathbb{B}$ with $\mathrm{Tr}_2(\tilde\Pi)=\tilde{Ϛ}_1$, and that the entanglement entropy of $\tilde\Pi$ equals $S(\tilde{Ϛ}_1)$. Conclude that the partial-trace entropy of a mixed state is the entanglement entropy of its **purification**, not of the state itself. This is the precise sense in which the partial trace does measure entanglement — of a larger, pure system.

## Relation to the Other Exercises

| | Reduced State of an Entangled Subsystem | Correlation Function of the Bell States | Entanglement Entropy and the Partial Trace |
|---|---|---|---|
| System | Two qubits | Two qubits | Two qubits |
| Physical process | Reduction of one subsystem | Joint spin correlation | Entropy of the reduction |
| Structural object | Partial trace of a state | Bell idempotents | Spectrum of the partial trace |
| Rule used | Partial trace | Tensor-product trace pairing | Partial trace + spectral entropy |
| Result | $\tilde{Ϛ}_1=\tfrac12 e_t$ (singlet) | $E=-\sum_j\epsilon_j a_jb_j$ | $S=h(s_1^2)$, $S=\log2$ at maximal entanglement |
| Scope | The reduced state | All four Bell states | All pure two-qubit states; **not** mixed joint states |

The three exercises form a sequence: the first computes the reduced state, the second computes the correlations of the joint state, and this one computes a number — the entropy — from the reduced state, and marks the boundary at which that number stops being an entanglement measure.

## Summary

The entanglement entropy of a pure two-qubit state is the von Neumann entropy of either reduced state, $S=-\mathrm{Tr}(\rho_1\log\rho_1)$, and it is computed from the partial trace. The exercise worked the computation by two routes and reached the same number both times.

**The Schmidt route.** Writing $|\psi\rangle=\sum_{ij}M_{ij}|i\rangle|j\rangle$ gives $\rho_1=MM^\dagger$ and $\rho_2=M^\dagger M$. The singular values of $M$ are the Schmidt coefficients $s_1,s_2$, and the reduced states have the common spectrum $s_1^2,s_2^2$. Hence $S(\rho_1)=S(\rho_2)=h(s_1^2)$: the entropy depends on the Schmidt data alone, vanishes exactly on product states, and equals $\log2$ exactly on maximally entangled states.

**The biquaternion route.** For the family $|\psi_\theta\rangle=\cos\theta|\uparrow\uparrow\rangle+\sin\theta|\downarrow\downarrow\rangle$, the state is the idempotent $\tilde\Pi_\theta=\tfrac14(e_t\otimes e_t-\vec e_z\otimes \vec e_z+\sin2\theta(\vec e_y\otimes \vec e_y-\vec e_x\otimes \vec e_x)+i\cos2\theta(\vec e_z\otimes e_t+e_t\otimes \vec e_z))$. The partial trace keeps the terms with $e_t$ in the traced factor and gives $\tilde{Ϛ}_1=\tfrac12(e_t+i\cos2\theta\,\vec e_z)$, whose Bloch vector has length $|\cos2\theta|$. The single-qubit entropy formula on $\mathbb{M}_+$ then gives $S=h(\cos^2\theta)$.

**The entropy functional.** The candidate of *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, $S(\tilde{Ϛ})=-2\,\mathrm{Sc}(\tilde{Ϛ}\log\tilde{Ϛ})$, is correct for states in the interior of the Bloch ball when the principal branch of the biquaternion logarithm is used. It is the trace formula in disguise, since $\mathrm{Tr}=2\,\mathrm{Sc}$. Two qualifications are recorded: the branch must be the principal one, and the logarithm — hence the formula — is undefined at the pure states, which are zero divisors; the value $S=0$ there is the continuous extension.

**The limit of the interpretation.** For pure joint states, the partial-trace entropy is the entanglement entropy. For mixed joint states it is not: the equal mixture of $\tilde\Pi_{\Phi^+}$ and $\tilde\Pi_{\Phi^-}$ is a separable state whose reduced entropy is nevertheless $\log2$. The title of the exercise holds for pure states and is left, deliberately, unclosed for mixed ones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$ | Two-qubit tensor-product algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_+$ | Hermitian subspace (states, observables) |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector) |
| $\mathrm{Tr}_\mathbb{B}$ | Trace on one factor: $\mathrm{Tr}_\mathbb{B}(e_t)=2$, $\mathrm{Tr}_\mathbb{B}(\vec e_k)=0$ |
| $\mathrm{Tr}(x\otimes y)=\mathrm{Tr}_\mathbb{B}(x)\mathrm{Tr}_\mathbb{B}(y)$ | Trace on the tensor product |
| $\mathrm{Tr}_1,\mathrm{Tr}_2$ | Partial traces: $\mathrm{Tr}_2(a\otimes b)=a\,\mathrm{Tr}_\mathbb{B}(b)$ |
| $\mathrm{Tr}(\tilde{Q})=2\,\mathrm{Sc}(\tilde{Q})$ | Trace equals twice the scalar part |
| $\tilde\Pi(\pm\vec u)=\tfrac12(e_t\pm i\vec u)$ | Single-qubit idempotents |
| $\tilde\Pi_\epsilon=\tfrac14(e_t\otimes e_t+\sum_k\epsilon_k \vec e_k\otimes \vec e_k)$ | Bell idempotent, $\epsilon_1\epsilon_2\epsilon_3=+1$ |
| $|\psi_\theta\rangle=\cos\theta|\uparrow\uparrow\rangle+\sin\theta|\downarrow\downarrow\rangle$ | Worked family |
| $\tilde\Pi_\theta$ | Its idempotent in $\mathbb{B}\otimes\mathbb{B}$ |
| $\tilde{Ϛ}=\tfrac12(e_t+i\vec r)$ | General state of $\mathbb{M}_+$, $|\vec r|\le1$ |
| $\tilde{Ϛ}_1=\mathrm{Tr}_2\tilde\Pi$ | Reduced state (Bloch vector $\vec r_1$) |
| $s_1,s_2$ | Schmidt coefficients, $s_1^2+s_2^2=1$ |
| $h(p)=-p\log p-(1-p)\log(1-p)$ | Binary entropy |
| $S(\tilde{Ϛ})=-\mathrm{Tr}(\tilde{Ϛ}\log\tilde{Ϛ})$ | von Neumann entropy |
| $S(\tilde{Ϛ})=-2\,\mathrm{Sc}(\tilde{Ϛ}\log\tilde{Ϛ})$ | Equivalent form (interior of the Bloch ball) |
| $\log$ | Natural logarithm (principal branch) |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{Q}_1^{\natural}\tilde{Q}_2)$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_2\rangle_{\natural}$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |

## Further Reading

- E. Schrödinger, "Discussion of probability relations between separated systems," *Mathematical Proceedings of the Cambridge Philosophical Society* **31** (1935) 555–563, for the reduced density matrix and the entropy of a subsystem.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Schmidt decomposition, the entropy of entanglement, purification, and the partial trace.
- Charles H. Bennett, Herbert J. Bernstein, Sandu Popescu, and Benjamin Schumacher, "Concentrating partial entanglement by local operations," *Physical Review A* **53** (1996) 2046–2052, for the theorem that the entropy of entanglement is the unique measure of entanglement for pure bipartite states.
- William K. Wootters, "Entanglement of formation of an arbitrary two-qubit state," *Physical Review Letters* **80** (1998) 2245–2248, for the mixed-state measure that the partial trace alone does not provide.
- Lidia Obojska, "Patterns of maximally entangled states within the algebra of biquaternions," *Journal of Physics Communications* **4** (2020) 055018, for the twelve-pattern catalogue whose exhaustiveness claim is corrected in *Solution I: The Schmidt Route*.
- Asher Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for the density-matrix formalism, the partial trace, and the thermodynamics of entanglement.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard textbook treatment of the singlet state and the reduced density matrix.
- The companion articles of this series: *Introduction to the Biquaternion Universe*, *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, *Quantum Physics in Biquaternionic Form*, *Entangled Subsystems in the Biquaternion Framework*, *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*, *Exercise: Two Spins in the Singlet State*, *Exercise: The Correlation Function of the Bell States*, and *Exercise: The Reduced State of an Entangled Subsystem*.
