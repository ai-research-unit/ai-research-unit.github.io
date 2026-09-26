# __Entanglement Entropy and the Replica Trick in Biquaternionic Form__

## Introduction

**Entanglement entropy** is the von Neumann entropy of the reduced state of a subsystem, $S_A=-\mathrm{Tr}(\rho_A\log\rho_A)$ with $\rho_A=\mathrm{Tr}_B\,\rho_{AB}$. It is not a quantity one computes directly in a field theory: the reduced density matrix of a region does not exist as a density matrix, the local algebra being type III, and $S_A$ is ultraviolet divergent. The **replica trick** is the standard method for computing it anyway. One computes the moments $Z_n=\mathrm{Tr}\,\rho_A^n$ for positive integers $n$ — which are well defined, and in a field theory are partition functions on an $n$-sheeted cover — and then continues analytically to $n\to1$, where
$$
S_A=-\frac{d}{dn}\log Z_n\Big|_{n=1}.
$$
The method is the workhorse of entanglement entropy in quantum field theory and holography; the area law of the companion article is one of its outputs.

This article asks what entanglement entropy and the replica trick are in the biquaternion framework. The answer is that the framework supplies the exact finite-dimensional version of the method, in which every step is a closed-form computation.

1. **Entanglement entropy of a biquaternion state is an entropy of a biquaternion state.** For a bipartition of a state of the tensor power $\mathbb{B}^{\otimes m}$, the reduced state $\rho_A$ is again a biquaternion-algebra element of the appropriate tensor power, and when it is a single-mode state it is a Bloch-ball state whose entropy is the closed form of the relative-entropy companion article.

2. **The replica moments are explicit.** The integer moments $Z_n=\mathrm{Tr}\,\rho_A^n=\sum_i\lambda_i^n$ are the power sums of the reduced state's eigenvalues, and the replica trick's analytic continuation is the continuation of a finite sum of exponentials. The entropic content is the same as in the field: $S_A=\lim_{n\to1}S_n=-\frac{d}{dn}\log Z_n|_{n=1}$.

3. **The replica geometry is the tensor power and its shift.** The $n$-sheeted cover of the field-theoretic replica trick is replaced, in the framework, by the tensor power $\mathbb{B}^{\otimes n}$ and the cyclic permutation of the replicas; the moment $Z_n$ is the expectation of the replica shift in the $n$-fold state, and for $n=2$ it is the swap expectation that computes the purity.

The article proceeds as follows. Entanglement entropy and the Rényi entropies are defined, with the entropy as their $n\to1$ limit. The replica trick is recalled in its field-theoretic form and restated in finite dimension. The replica structure of the biquaternion tensor power is set out, with the shift operator and the swap. A two-qubit biquaternion state is worked out completely, its reduced state, its Rényi entropies and the $n\to1$ limit being computed and tabulated. The article closes with the established/interpretation/open split.

**Conventions.** Those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, scalar imaginary $i$, and isomorphism $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$, so that $\mathbb{B}\cong M_2(\mathbb{C})$. The material and informational subspaces are $\mathbb{M}_-$ and $\mathbb{M}_+$, with $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm=\mathbb{M}_\mp$. The trace is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$, with $\mathrm{Tr}(e_0)=2$; on the tensor power the trace is the product trace, $\mathrm{Tr}(\tilde A_1\otimes\cdots\otimes\tilde A_n)=\prod_i\mathrm{Tr}(\tilde A_i)$. Reduced states and partial traces are those of *Strong Subadditivity in the Biquaternion Framework*, states and the Bloch ball those of *The GNS Construction in the Biquaternion Framework*, and the entropy closed form that of *Relative Entropy and the Biquaternion Framework*.

## Entanglement Entropy and Rényi Entropies

### Definitions

Let $\rho_{AB}$ be a state of a bipartite system with Hilbert space $\mathcal H_A\otimes\mathcal H_B$, and let
$$
\rho_A=\mathrm{Tr}_B\,\rho_{AB}
$$
be the reduced state of $A$. The **entanglement entropy** of the bipartition is the von Neumann entropy of the reduced state,
$$
S_A=-\mathrm{Tr}\big(\rho_A\log\rho_A\big)=S(\rho_A).
$$
It vanishes if and only if $\rho_{AB}$ is a product across the bipartition; it is symmetric, $S_A=S_B$ when $\rho_{AB}$ is pure; and it is basis-independent. The **Rényi entropies** of order $n>0$, $n\ne1$, are
$$
S_n=\frac{1}{1-n}\log\mathrm{Tr}\big(\rho_A^n\big)=\frac{1}{1-n}\log Z_n,
\qquad
Z_n=\mathrm{Tr}\big(\rho_A^n\big),
$$
and the von Neumann entropy is their limit as $n\to1$. The moments $Z_n$ are called the **replica moments**; $Z_1=1$; $Z_2=\mathrm{Tr}\rho_A^2$ is the purity, $1/Z_2$ being the participation ratio; and the Rényi entropies are non-increasing in $n$, with $S_n\to S_0=\log\mathrm{rank}\,\rho_A$ as $n\to0$ and $S_n\to S_\infty=-\log\lambda_{\max}$ as $n\to\infty$.

### The Entropy as the Limit of the Rényi Entropies

The limit is worth deriving once, because the replica trick is its field-theoretic evaluation. Write the eigenvalues of $\rho_A$ as $\lambda_i$, so that $Z_n=\sum_i\lambda_i^n$ and $Z_1=\sum_i\lambda_i=1$. Then
$$
S_n=\frac{1}{1-n}\log\sum_i\lambda_i^n,
$$
and both numerator and denominator vanish at $n=1$. L'Hôpital's rule gives
$$
\lim_{n\to1}S_n
=\frac{\frac{d}{dn}\log Z_n\big|_{n=1}}{\frac{d}{dn}(1-n)\big|_{n=1}}
=-\frac{Z_1'}{1}
=-\sum_i\lambda_i\log\lambda_i
=-\mathrm{Tr}\big(\rho_A\log\rho_A\big)=S_A,
$$
using $Z_1'=\sum_i\lambda_i\log\lambda_i$. Hence
$$
S_A=\lim_{n\to1}S_n=-\frac{d}{dn}\log Z_n\Big|_{n=1}.
$$
The derivation uses only that $\rho_A$ has a finite spectrum, so it holds verbatim in the biquaternion framework.

## The Replica Trick

### The Field-Theoretic Trick

In a quantum field theory the reduced density matrix of a region does not exist, but the moments $Z_n=\mathrm{Tr}\rho_A^n$ do. They are the partition functions of the theory on an $n$-sheeted cover of spacetime: the region $A$ is the branch locus, the $n$ sheets are the replicas, and the trace over the field configurations joining them cyclically is exactly the $n$-th moment of the reduced state. The entropies are then
$$
S_n=\frac{1}{1-n}\log\frac{Z_n}{Z_1^n},
\qquad
S_A=-\frac{\partial}{\partial n}\log\frac{Z_n}{Z_1^n}\Big|_{n=1},
$$
where $Z_1$ is the ordinary partition function. The quotient removes the non-universal volume term and leaves the entropic part. The method is standard; its output in the most important case is that the entanglement entropy of a region scales with the area of its boundary, which is the subject of the companion article on the area law.

### The Finite-Dimensional Trick

In finite dimension the replica trick is not a trick at all: the continuation is the continuation of an explicit function. If $\rho_A$ has eigenvalues $\lambda_i$, then
$$
Z_n=\sum_i\lambda_i^n
$$
for every integer $n\ge1$, and the right-hand side is an entire function of $n$, so its continuation to non-integer $n$ is immediate. The Rényi entropies are $S_n=\frac{1}{1-n}\log\sum_i\lambda_i^n$, and the entropy is the limit above. In the biquaternion framework the eigenvalues of a single-mode reduced state are $\tfrac12(1\pm|\mathbf r_A|)$, where $\mathbf r_A$ is the reduced state's Bloch vector, so
$$
S_A=-\tfrac12\log\frac{1-|\mathbf r_A|^2}{4}-|\mathbf r_A|\,\mathrm{artanh}\big(|\mathbf r_A|\big),
$$
the closed form of the relative-entropy companion article. The replica trick and the closed form are two routes to the same number, and the worked example below checks them against each other.

## The Replica Structure of the Biquaternion Tensor Power

### The Tensor Power and the Cyclic Shift

The $n$ replicas of a biquaternion system are the factors of the tensor power
$$
\mathbb{B}^{\otimes n},
$$
and the replica shift is the cyclic permutation of the factors. On a state $\rho_{A_1B_1}\otimes\cdots\otimes\rho_{A_nB_n}$ of $n$ replicas, the shift acts on the $A$ factors alone,
$$
\Pi_n:\ A_1\to A_2\to\cdots\to A_n\to A_1,
\qquad \text{with the } B_i \text{ fixed},
$$
and the replica moment is the expectation of the shift,
$$
Z_n=\mathrm{Tr}\Big[\big(\rho_{AB}\big)^{\otimes n}\,\Pi_n\Big].
$$
This is the finite-dimensional image of the $n$-sheeted cover: the sheets are the replicas, the branch locus is the $A$ factor, and the cyclic joining of the sheets is the cyclic permutation. The state is the $n$-fold product, so the expectation is a product-state matrix element, which is why the computation is elementary.

### The Swap Operator and the Purity

The case $n=2$ is the one used most, and it exhibits the mechanism. The shift is the **swap** $\mathbb F_{AA'}$ on the two copies of $A$, and
$$
Z_2=\mathrm{Tr}\big(\rho_A^2\big)
=\mathrm{Tr}\Big[\big(\rho_{AB}\otimes\rho_{A'B'}\big)\,\mathbb F_{AA'}\Big],
$$
where the primed factors are the second replica. The identity was checked on the two-qubit state of the next section: with $\rho_{AB}=|\psi_\theta\rangle\langle\psi_\theta|$ and $\theta=0.4$, both sides equal $0.7427001194$, agreeing with $\cos^4\theta+\sin^4\theta$ to twelve digits. The purity is thus a swap expectation, and the Rényi entropy of order two is $S_2=-\log Z_2$.

## The Schmidt Decomposition and the Entanglement Spectrum

For a **pure** bipartite state the reduced spectra of the two sides coincide, and the reason is the Schmidt decomposition. Every $|\Psi\rangle\in\mathcal H_A\otimes\mathcal H_B$ can be written
$$
|\Psi\rangle=\sum_i\sqrt{\lambda_i}\,|a_i\rangle\otimes|b_i\rangle,
\qquad \lambda_i\ge0,\quad \sum_i\lambda_i=1,
$$
with orthonormal sets $\{|a_i\rangle\}$ and $\{|b_i\rangle\}$; then
$$
\rho_A=\sum_i\lambda_i\,|a_i\rangle\langle a_i|,
\qquad
\rho_B=\sum_i\lambda_i\,|b_i\rangle\langle b_i|,
$$
so the two reduced states have the same spectrum, $S_A=S_B$, and the same replica moments $Z_n=\sum_i\lambda_i^n$. In the biquaternion framework the bipartite algebra $\mathbb{B}\otimes\mathbb{B}$ has complex dimension sixteen and the modules on which pure states live are smaller; for a two-qubit pure state the Schmidt decomposition has at most two terms, which is why the worked example below has two eigenvalues and why the reduced state is a Bloch-ball state.

The **entanglement spectrum** is the set $\{-\log\lambda_i\}$, the spectrum of the modular Hamiltonian of the reduced state, by the first-law companion article. Its spacing controls the entanglement, and its two limits are the two extreme cases: a product state has one Schmidt coefficient equal to one and the rest zero, so the entanglement spectrum is a single level at zero and $S_A=0$; a maximally entangled state has all nonzero coefficients equal, so the spectrum is degenerate and $S_A$ is maximal. The replica moments are the power sums of $e^{-\varepsilon_i}$ with $\varepsilon_i$ the entanglement energies, so the Rényi entropies are free-energy differences of the entanglement spectrum: with $\tilde\rho_A=e^{-K}$ and $Z_n=\mathrm{Tr}\,e^{-nK}$, and writing $F(T)=-T\log\mathrm{Tr}\,e^{-K/T}$ for the free energy of the spectrum at temperature $T$, one has $S_n=\frac{n}{n-1}\big[F(1/n)-F(1)\big]$ — the standard reading, available in the framework because the entanglement spectrum is the spectrum of an ordinary $\mathbb{M}_+$ element.

## Worked Example: a Two-Qubit Biquaternion State

### The Reduced State and Its Spectrum

Take the pure two-qubit state
$$
|\psi_\theta\rangle=\cos\theta\,|00\rangle+\sin\theta\,|11\rangle,
\qquad
\rho_{AB}=|\psi_\theta\rangle\langle\psi_\theta|.
$$
Tracing out $B$ in the biquaternion tensor product — equivalently, using the partial trace of the strong-subadditivity companion article — gives the reduced state
$$
\rho_A=\cos^2\theta\,|0\rangle\langle0|+\sin^2\theta\,|1\rangle\langle1|
=\frac{1}{2}\Big(e_0+i\cos(2\theta)\,e_3\Big),
$$
a biquaternion state of the Bloch ball with
$$
\mathbf r_A=\cos(2\theta)\,\hat{\mathbf e}_3,
\qquad
|\mathbf r_A|=\big|\cos(2\theta)\big|,
\qquad
\lambda_\pm=\frac{1\pm\cos2\theta}{2}=\cos^2\theta,\ \sin^2\theta .
$$
The purity is $Z_2=\cos^4\theta+\sin^4\theta$, and the entanglement entropy is $S_A=h(\cos^2\theta)$, the binary entropy of the squared cosine.

### The Two Routes to the Entropy

The reduced state is a single-mode biquaternion state, so the closed form of the relative-entropy companion article applies:
$$
S_A=-\tfrac12\log\frac{1-r_A^2}{4}-r_A\,\mathrm{artanh}(r_A),
\qquad
r_A=\big|\cos2\theta\big|.
$$
That this equals the binary entropy $h(\cos^2\theta)$ is an identity, and it was checked numerically: at $\theta=0.2$ both give $0.1662545197$; at $\theta=0.4$ both give $0.4255547593$; at $\theta=\pi/4$ both give $\log2=0.6931471806$. The replica route gives the same number through the moments.

### Rényi Entropies and the $n\to1$ Limit

The replica moments of the reduced state are
$$
Z_n=\cos^{2n}\theta+\sin^{2n}\theta,
\qquad
S_n=\frac{1}{1-n}\log\big(\cos^{2n}\theta+\sin^{2n}\theta\big).
$$
The entropies are tabulated for three angles and four orders. All values were recomputed from the eigenvalue formula.

| $\theta$ | $Z_2$ | $S_1$ | $S_2$ | $S_3$ | $S_5$ | $S_\infty$ |
|---|---|---|---|---|---|---|
| $0.2$ | $0.9241767$ | $0.1662545$ | $0.0788520$ | $0.0603696$ | $0.0503369$ | $0.0402695$ |
| $0.4$ | $0.7427001$ | $0.4255548$ | $0.2974629$ | $0.2438393$ | $0.2055269$ | $0.1644580$ |
| $\pi/4$ | $0.5000000$ | $0.6931472$ | $0.6931472$ | $0.6931472$ | $0.6931472$ | $0.6931472$ |

The table displays the three regimes: near the product state ($\theta=0.2$, $r_A=0.921$) the entropies are small and strongly ordered by $n$; at maximal entanglement ($\theta=\pi/4$, $r_A=0$) all Rényi entropies equal $\log2$, as they must for a maximally mixed reduced state; and $\theta=0.4$ interpolates. The $n\to1$ limit was checked directly: $S_{1.001}=0.4253642$ and $S_{0.999}=0.4257455$ at $\theta=0.4$, bracketing the value $S_1=0.4255548$, and the same at $\theta=0.2$. The replica method and the biquaternion closed form therefore agree on the whole one-parameter family.

### The Replica Shift at Higher $n$

For $n\ge3$ the moment is the expectation of the cyclic shift on the $n$-fold tensor power, and for the state above the reduced spectrum is $\cos^2\theta,\sin^2\theta$, so the shift's expectation reduces to the power sum $\cos^{2n}\theta+\sin^{2n}\theta$. The general finite-dimensional statement is that $Z_n=\mathrm{Tr}[\rho_{AB}^{\otimes n}\Pi_n]$ holds for every $n$ with the cyclic shift $\Pi_n$; the two-qubit case of the previous subsection is the $n=2$ instance, verified by the swap computation. The identity was checked further against $\mathrm{Tr}(\rho_A^n)$ on a generic two-qubit pure state at $n=2,3,4$, where the two sides agree to machine precision. The finite framework's replica geometry is thus the tensor power with its cyclic permutation, and the analytic continuation is the continuation of the power sum.

### A Second Example: the W State

A second example has a different spectrum. The three-qubit W state, reduced to two qubits by tracing out the third, has the reduced state of the strong-subadditivity companion article,
$$
\rho_{AB}=\tfrac13|00\rangle\langle00|
+\tfrac13\big(|01\rangle+|10\rangle\big)\big(\langle01|+\langle10|\big),
$$
a rank-two state on the four-dimensional pair space, with eigenvalues $\tfrac23,\tfrac13,0,0$. The replica moments are therefore
$$
Z_n=\left(\tfrac23\right)^n+\left(\tfrac13\right)^n,
\qquad
Z_2=\tfrac59=0.555556,\qquad
Z_3=\tfrac13=0.333333,
$$
and the entropies are $S_1=h(1/3)=0.636514$, $S_2=0.587787$, $S_3=0.549306$, $S_5=0.499138$, and $S_\infty=-\log(2/3)=0.405465$, all recomputed from the eigenvalues. The W reduction has the same rank as the two-qubit family and a different spectrum, and its moments are, again, power sums of that spectrum: the method is rank-independent because it is a statement about the eigenvalues.

## What Is Established and What Is Interpretation

**Established (theorem, imported).** The definition of entanglement entropy and the Rényi entropies; their ordering and limits; the identification $S_A=\lim_{n\to1}S_n=-\frac{d}{dn}\log Z_n|_{1}$; the field-theoretic replica trick as a partition function on an $n$-sheeted cover, including the quotient by $Z_1^n$; the area-law output of the method. All standard.

**Established (recomputed here).** The finite-dimensional replica moments $Z_n=\sum_i\lambda_i^n$; the replica formula $Z_n=\mathrm{Tr}[\rho_{AB}^{\otimes n}\Pi_n]$ with the $n=2$ swap identity and its $n=2,3,4$ instances, verified on the explicit state and on a generic two-qubit state; the reduced state of the two-qubit family as a biquaternion Bloch state with $r_A=|\cos2\theta|$; the agreement of the biquaternion entropy closed form with the binary entropy; and the Rényi table with its $n\to1$ convergence.

**Interpretation.** That the tensor power and its cyclic shift are read as the framework's replica geometry, and that the entanglement entropy of a bipartition is read as the entropy of a reduced biquaternion state.

**Gaps, left visible.** The framework's replica structure is finite-dimensional and supplies no field-theoretic branched cover, no ultraviolet divergence, and no geometric area law; those are the field theory's. The analytic continuation is trivial in finite dimension and is the whole difficulty in the field. No empirical consequence is derived.

## Open Questions

**1. The replica shift and the sector structure.** The cyclic shift $\Pi_n$ permutes the tensor factors. Is there a reading of $\Pi_n$ in terms of the material/informational decomposition of $\mathbb{B}^{\otimes n}$, and does the shift's expectation factor across the sectors?

**2. The many-mode replica moments.** For a state of $\mathbb{B}^{\otimes m}$ with a bipartition into several modes, the reduced state has $2^{m_A}$ eigenvalues and the moments are power sums. Do these reproduce, in a regulated chain, the scaling of the field-theoretic entanglement entropy that the area law describes?

**3. The Rényi entropy at $n=0$ and $n=\infty$.** The limits $S_0=\log\mathrm{rank}\,\rho_A$ and $S_\infty=-\log\lambda_{\max}$ are properties of the reduced state's spectrum. In the framework they are the rank and the largest eigenvalue of a biquaternion state; does the zero-divisor boundary give them a distinguished role?

**4. The swap and the modular Hamiltonian.** The swap operator and the modular Hamiltonian of the first-law companion article are both built from the reduced state. Is there an operator identity relating them at $n=2$, in the spirit of the Rényi entropy's relation to the modular flow at integer $n$?

**5. Empirical contact.** As everywhere in the subcategory, no prediction distinguishing the reading from standard quantum information theory is derived.

## Summary

Entanglement entropy is the von Neumann entropy of a reduced state, $S_A=-\mathrm{Tr}(\rho_A\log\rho_A)$ with $\rho_A=\mathrm{Tr}_B\rho_{AB}$, and the replica trick computes it from the moments $Z_n=\mathrm{Tr}\rho_A^n$ by continuation to $n\to1$: $S_A=-d\log Z_n/dn|_1$. In quantum field theory the moments are partition functions on $n$-sheeted covers; in finite dimension they are power sums of the reduced state's eigenvalues.

In the biquaternion framework the replicas are the factors of the tensor power $\mathbb{B}^{\otimes n}$, the replica geometry is the cyclic permutation $\Pi_n$ of the factors, and the moment is the shift expectation $Z_n=\mathrm{Tr}[\rho_{AB}^{\otimes n}\Pi_n]$. The case $n=2$ is the swap expectation that computes the purity, verified on the explicit two-qubit state. For the pure family $|\psi_\theta\rangle=\cos\theta|00\rangle+\sin\theta|11\rangle$, the reduced state is a biquaternion Bloch state with $r_A=|\cos2\theta|$, the moments are $Z_n=\cos^{2n}\theta+\sin^{2n}\theta$, and the Rényi entropies $S_n=\frac{1}{1-n}\log Z_n$ interpolate between the product state and the maximally entangled state. The biquaternion entropy closed form agrees with the binary entropy at every angle, and the $n\to1$ limit was checked to bracket $S_1$ at two angles.

The framework thus reproduces the replica method exactly in finite dimension, with the entanglement entropy of a bipartition equal to the entropy of a reduced biquaternion state. What it cannot reproduce is the field-theoretic content: the branched cover, the ultraviolet divergence, and the geometric scaling that the area-law companion article treats.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_+,\mathbb{M}_-$ | Informational (Hermitian) and material (anti-Hermitian) subspaces |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace pairing; $\mathrm{Tr}(e_0)=2$ |
| $\mathbb{B}^{\otimes n}\cong M_{2^n}(\mathbb{C})$ | Tensor power; $n$ replicas |
| $\rho_A=\mathrm{Tr}_B\rho_{AB}$ | Reduced state |
| $S_A=S(\rho_A)=-\mathrm{Tr}(\rho_A\log\rho_A)$ | Entanglement entropy |
| $Z_n=\mathrm{Tr}(\rho_A^n)$ | Replica moment |
| $S_n=\frac{1}{1-n}\log Z_n$ | Rényi entropy of order $n$ |
| $S_A=-\frac{d}{dn}\log Z_n\big|_{n=1}$ | Replica-trick representation of $S_A$ |
| $\Pi_n$ | Cyclic shift of the $n$ replicas |
| $\mathbb F_{AA'}$ | Swap operator; $n=2$ replica shift |
| $\mathbf r_A$, $r_A=|\mathbf r_A|$ | Bloch vector and radius of a single-mode reduced state |
| $\cos^2\theta,\sin^2\theta$ | Eigenvalues of $\rho_A$ for $|\psi_\theta\rangle$ |
| $h(p)$ | Binary entropy $-p\log p-(1-p)\log(1-p)$ |

## Further Reading

- C. Holzhey, F. Larsen, and F. Wilczek, "Geometric and renormalized entropy in conformal field theory," *Nuclear Physics B* **424** (1994) 443–467, for the replica computation of entanglement entropy in conformal field theory.
- P. Calabrese and J. Cardy, "Entanglement entropy and quantum field theory," *Journal of Statistical Mechanics* **2004** (2004) P06002, for the replica trick and the Rényi entropies in quantum field theory.
- A. Rényi, "On measures of entropy and information," *Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability* **1** (1961) 547–561, for the entropy family.
- H. Araki and E. H. Lieb, "Entropy inequalities," *Communications in Mathematical Physics* **18** (1970) 160–170, for the ordering of the Rényi entropies.
- M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for entanglement entropy, the Schmidt decomposition, and the purity.
- E. Witten, "Notes on some entanglement properties of quantum field theory," *Reviews of Modern Physics* **90** (2018) 045003, for the replica geometry, the divergent terms, and the area law.
- M. Ohya and D. Petz, *Quantum Entropy and Its Use* (Springer, 1993), for the moment/entropy relations and the limiting cases.
- S. Ryu and T. Takayanagi, "Holographic derivation of entanglement entropy from the anti-de Sitter space/conformal field theory correspondence," *Physical Review Letters* **96** (2006) 181602, for the holographic evaluation of the same moments.
- Companion article *Strong Subadditivity in the Biquaternion Framework*, for the reduced states, the partial trace, and the tensor powers.
- Companion article *Relative Entropy and the Biquaternion Framework*, for the entropy closed form of a biquaternion state.
- Companion article *The Modular Hamiltonian and the First Law of Entanglement in Biquaternionic Form*, for the modular Hamiltonian of a reduced state.
- Companion article *The Area Law of Entanglement Entropy in Biquaternionic Form*, for what the replica moments give in the field.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the state space and the trace pairing.
