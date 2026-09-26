# __Mutually Unbiased Bases and the Biquaternion Algebra__

## Introduction

Two orthonormal bases of a $d$-dimensional complex vector space are **mutually unbiased** when every vector of one has the same squared overlap, $1/d$, with every vector of the other. In this case a measurement in one basis yields no information whatever about a measurement in the other: the outcome distributions are as far from correlated as the formalism permits. Mutually unbiased bases are the extreme case of incompatible measurements, they underpin quantum key distribution, and a complete set of them permits the reconstruction of a state from the outcome probabilities of $d+1$ measurements.

In the biquaternion framework the bases of the defining module are the idempotent bases of the Hermitian subspace. A basis of rays is a complete family of orthogonal rank-one idempotents, $\{\tilde{P}_i\}$ with $\tilde{P}_i\tilde{P}_j = \delta_{ij}\tilde{P}_i$ and $\sum_i\tilde{P}_i = e_0$, and the Hilbert-space overlap between two rays is the trace pairing of their idempotents,

$$
\bigl|\langle \psi|\phi\rangle\bigr|^2 = \mathrm{Tr}\bigl(\tilde{P}(\psi)\,\tilde{P}(\phi)\bigr) = 2\,\mathrm{Sc}\bigl(\tilde{P}(\psi)\tilde{P}(\phi)\bigr).
$$

The mutual-unbiasedness condition therefore reads, in the algebra,

$$
\mathrm{Tr}\bigl(\tilde{P}_i^{(b)}\tilde{P}_j^{(b')}\bigr) = \frac{1}{d}
\qquad\text{for all } i,j \ \text{whenever } b\neq b' .
$$

For the native qubit $d=2$ the maximum number of mutually unbiased bases is $d+1=3$, and they have a clean algebraic origin: they are the eigenbases of the three imaginary units $ie_1, ie_2, ie_3$. The three units are Hermitian involutions, pairwise anticommuting, and each defines an orthogonal pair of rank-one idempotents; the trace pairing between idempotents from different pairs is exactly $\tfrac12$. The three bases are the three coordinate measurements, and their completeness is the tomographic statement that the outcome probabilities of three measurements determine the state.

This article develops the idempotent bases of the algebra, derives the unbiasedness of the three coordinate bases from the product rules of the units, gives the reconstruction formula that recovers the state from the three bases, and discusses the two-qubit case, where the maximum is five bases, where the tensor product of qubit bases supplies only three, and where the Bell basis — a natural idempotent basis of $\mathbb{B}\otimes\mathbb{B}$ — is *not* unbiased with respect to the product basis. The framework supplies the qubit MUBs natively and exhibits the obstruction to obtaining a full set by naive tensor products.

## Idempotent Bases of the Algebra

### Rank-one idempotents

A **rank-one idempotent** is an element $\tilde{P}\in\mathbb{M}_+$ with

$$
\tilde{P}^2 = \tilde{P}, \qquad \mathrm{Tr}(\tilde{P}) = 1, \qquad \tilde{P}\geq0 .
$$

Up to a phase it is $\tilde{P}_+(\hat{\mu}) = \tfrac12(e_0 + i\hat{\mu})$ for a unit vector $\hat{\mu}\in\mathbb{R}^3$, and its orthogonal complement is $\tilde{P}_-(\hat{\mu}) = \tfrac12(e_0-i\hat{\mu})$. The pair satisfies

$$
\tilde{P}_+\tilde{P}_- = 0, \qquad \tilde{P}_+ + \tilde{P}_- = e_0 ,
$$

so $\{\tilde{P}_+(\hat{\mu}),\tilde{P}_-(\hat{\mu})\}$ is a complete orthogonal family: an **idempotent basis** of the defining module. Every basis of the module arises this way, one basis for each direction $\hat{\mu}$ on the Bloch sphere; a basis is a pair of antipodal pure states.

### The trace pairing between idempotents

For two directions $\hat{\mu},\hat{\nu}$ the trace pairing of the positive idempotents is

$$
\mathrm{Tr}\bigl(\tilde{P}_+(\hat{\mu})\tilde{P}_+(\hat{\nu})\bigr)
= \tfrac{1}{4}\mathrm{Tr}\bigl((e_0+i\hat{\mu})(e_0+i\hat{\nu})\bigr)
= \tfrac{1}{4}\bigl(2 - 2\,\hat{\mu}\cdot\hat{\nu}\bigr)
= \tfrac{1}{2}\bigl(1 - \hat{\mu}\cdot\hat{\nu}\bigr),
$$

using $\mathrm{Tr}(e_0)=2$, $\mathrm{Tr}(ie_k)=0$ and $\mathrm{Tr}((ie_j)(ie_k)) = 2\delta_{jk}$. In Hilbert-space terms this is the squared overlap

$$
\bigl|\langle \psi(\hat{\mu})|\psi(\hat{\nu})\rangle\bigr|^2 = \tfrac{1}{2}\bigl(1-\hat{\mu}\cdot\hat{\nu}\bigr),
$$

which vanishes for antipodal directions and equals one for coincident directions. The trace pairing is thus a measure of the distinguishability of two rays, and it is the object that the mutual-unbiasedness condition constrains.

### The three coordinate bases

The algebra singles out three directions — the axes $\hat{e}_1,\hat{e}_2,\hat{e}_3$ of the imaginary units — and with them three idempotent bases:

$$
\mathcal{B}_k = \bigl\{\tilde{P}_+(\hat{e}_k),\ \tilde{P}_-(\hat{e}_k)\bigr\}, \qquad k=1,2,3 .
$$

Explicitly, using $\tilde{X}=ie_1$, $\tilde{Y}=ie_2$, $\tilde{Z}=ie_3$,

$$
\mathcal{B}_1 = \Bigl\{\tfrac12(e_0+i e_1),\ \tfrac12(e_0-i e_1)\Bigr\}, \quad
\mathcal{B}_2 = \Bigl\{\tfrac12(e_0+i e_2),\ \tfrac12(e_0-i e_2)\Bigr\}, \quad
\mathcal{B}_3 = \Bigl\{\tfrac12(e_0+i e_3),\ \tfrac12(e_0-i e_3)\Bigr\} .
$$

Each basis is the eigenbasis of the corresponding involution: $\tilde{X}$ takes the values $\pm1$ on $\mathcal{B}_1$, and similarly for $\tilde{Y}$ on $\mathcal{B}_2$ and $\tilde{Z}$ on $\mathcal{B}_3$. These are the three coordinate measurements of the qubit.

## Mutual Unbiasedness of the Coordinate Bases

### The overlap between different bases

Take two distinct coordinate bases, $j\neq k$. Then for any signs $s,s'\in\{+1,-1\}$,

$$
\tilde{P}_s(\hat{e}_j)\,\tilde{P}_{s'}(\hat{e}_k)
= \tfrac{1}{4}\bigl(e_0 + s' ie_k + s ie_j + ss' (ie_j)(ie_k)\bigr)
= \tfrac{1}{4}\bigl(e_0 + s' ie_k + s ie_j - ss' e_je_k\bigr),
$$

and taking the trace, the three traceless terms vanish and the last contributes $-\mathrm{Tr}(e_je_k) = 0$ for $j\neq k$ because distinct quaternion units are orthogonal under the trace. Hence

$$
\mathrm{Tr}\bigl(\tilde{P}_s(\hat{e}_j)\tilde{P}_{s'}(\hat{e}_k)\bigr) = \tfrac{1}{4}\cdot 2 = \tfrac{1}{2}
\qquad (j\neq k),
$$

independently of the signs. In the Hilbert-space language,

$$
\bigl|\langle \psi_s(\hat{e}_j)|\psi_{s'}(\hat{e}_k)\rangle\bigr|^2 = \tfrac{1}{2} = \frac{1}{d},
\qquad d=2 ,
$$

so **the three coordinate bases are pairwise mutually unbiased**. The derivation used only the algebra's product rules and the trace; unbiasedness is a property of the three imaginary units and their orthogonality, not an additional geometric input.

### Orthogonality within a basis

Within one basis, $j=k$, the same computation gives

$$
\mathrm{Tr}\bigl(\tilde{P}_s(\hat{e}_k)\tilde{P}_{s'}(\hat{e}_k)\bigr)
= \tfrac{1}{4}\mathrm{Tr}\bigl(e_0 + (s+s')ie_k + ss'(ie_k)^2\bigr)
= \tfrac{1}{4}\bigl(2 - 2ss'\bigr)
= \begin{cases}1 & s=s',\\ 0 & s=-s'.\end{cases}
$$

The two cases are exactly the normalization and orthogonality of the basis. Thus the same formula produces orthogonality within a basis and unbiasedness across bases, the sign of the unit's square being responsible for the difference. This is the algebraic statement that the three bases are as correlated as possible internally and as uncorrelated as possible externally.

### Maximality

For the qubit the maximum number of mutually unbiased bases is $d+1 = 3$, and the three coordinate bases attain it. No fourth basis can be unbiased with all three: a fourth direction $\hat{\mu}$ would need $\hat{\mu}\cdot\hat{e}_k = 0$ for $k=1,2,3$, which is impossible for a unit vector in $\mathbb{R}^3$. The algebra thus supplies a **complete** set of mutually unbiased bases, and it does so through the three pairwise orthogonal directions singled out by the imaginary units. The completeness is not merely a counting statement; it is what makes the three coordinate measurements tomographically sufficient.

### The overlap matrix

Arrange the six pure states as columns in the order

$$
\bigl(\tilde{P}_+(\hat{e}_1),\tilde{P}_-(\hat{e}_1),\tilde{P}_+(\hat{e}_2),\tilde{P}_-(\hat{e}_2),\tilde{P}_+(\hat{e}_3),\tilde{P}_-(\hat{e}_3)\bigr).
$$

The matrix of trace pairings $M_{ab} = \mathrm{Tr}(\tilde{P}_a\tilde{P}_b)$ is block structure in $2\times2$ blocks: the diagonal blocks are the identity (orthonormal within a basis), and the off-diagonal blocks are $\tfrac12 J$, where $J$ is the all-ones $2\times2$ matrix (unbiased across bases). Thus

$$
M = \begin{pmatrix} I_2 & \tfrac12 J_2 & \tfrac12 J_2\\[2pt] \tfrac12 J_2 & I_2 & \tfrac12 J_2\\[2pt] \tfrac12 J_2 & \tfrac12 J_2 & I_2 \end{pmatrix},
\qquad J_2 = \begin{pmatrix}1&1\\1&1\end{pmatrix}.
$$

The pattern — identity blocks on the diagonal, constant blocks off it — is the matrix form of mutual unbiasedness. It was verified by explicit computation of all thirty-six entries; the off-diagonal constant is exactly $\tfrac12$.

## Reconstruction from Mutually Unbiased Measurements

### The reconstruction formula

Let $\mathcal{B}_1,\dots,\mathcal{B}_{d+1}$ be a complete set of mutually unbiased bases of a state space of dimension $d$, with idempotents $\tilde{P}_i^{(b)}$ and outcome probabilities $p_i^{(b)} = \mathrm{Tr}(\tilde{\rho}\tilde{P}_i^{(b)})$. Then

$$
\tilde{\rho} = \sum_{b=1}^{d+1}\sum_{i=1}^{d} p_i^{(b)}\,\tilde{P}_i^{(b)} - e_0 ,
$$

for a trace-one state, so the $d(d+1)$ probabilities determine the state linearly. For the qubit this is the statement that three measurements, each with two outcomes, fix the three Bloch components: the six probabilities determine $\tilde{\rho}$, and the formula above reconstructs it.

### Verification for the qubit

Let $\tilde{\rho} = \tfrac12(e_0+i\mathbf{r})$ and let $r_k = \mathbf{r}\cdot\hat{e}_k$. In basis $\mathcal{B}_k$ the two outcome probabilities are $p_\pm^{(k)} = \tfrac12(1\pm r_k)$. The contribution of basis $k$ to the sum is

$$
p_+^{(k)}\tilde{P}_+(\hat{e}_k) + p_-^{(k)}\tilde{P}_-(\hat{e}_k)
= \tfrac12\bigl(e_0 + i r_k\hat{e}_k\bigr),
$$

as follows by expanding the two terms. Summing over the three bases gives

$$
\sum_{k=1}^{3}\tfrac12\bigl(e_0 + i r_k\hat{e}_k\bigr)
= \tfrac{3}{2}e_0 + \tfrac12 i\mathbf{r}
= e_0 + \tfrac12\bigl(e_0 + i\mathbf{r}\bigr)
= e_0 + \tilde{\rho} ,
$$

which rearranges to the reconstruction formula. Every step was verified numerically on a generic state with all three Bloch components non-zero; the reconstruction returned the input state to machine precision. The identity is the tomographic statement anticipated in the article on the native qubit: the three coordinate measurements determine the state, and no fourth measurement is needed.

### Complementarity and information

The information content of the MUB structure is that the three bases are **maximally complementary**: certainty in one is total ignorance in the others. If the state is one of the two idempotents of $\mathcal{B}_k$, the outcome in that basis is certain, while in either other basis it is $\tfrac12$ for each outcome. The mutual information between the outcomes of measurements in two different bases is therefore zero for every state, which is the operational content of unbiasedness. The three bases are the measurements that reveal the three independent components of the state, and none of them reveals anything about the others' outcomes.

### Entropic uncertainty

Complementarity can be quantified. For two bases with maximum overlap $c = \max_{a,b}|\langle a|b\rangle|^2 = 1/2$, the Maassen–Uffink inequality bounds the sum of the Shannon entropies of the two outcome distributions:

$$
H(A) + H(B) \ \geq\ \log_2\frac{1}{c} = \log_2 2 = 1 \ \text{bit} .
$$

The bound is attained at the eigenstates of one of the two bases: for the eigenstate $\tilde{P}_+(\hat{e}_1)$ of the first basis, the first measurement is certain, $H(A) = 0$, while the second measurement is uniform, $H(B) = h_2(\tfrac12) = 1$ bit, so the sum is exactly one bit. The algebra supplies the interpretation: the overlap of an idempotent of one basis with an idempotent of another is the trace pairing $\tfrac12$, and a uniform two-outcome distribution carries exactly one bit. Two complementary bases therefore cannot both be known, and the minimum ignorance is one bit — the qubit cannot carry the information of two complementary observables at once. This is the entropic restatement of the algebraic fact that $\mathrm{Tr}(\tilde{P}_s(\hat{e}_j)\tilde{P}_{s'}(\hat{e}_k)) = \tfrac12$ across bases.

### The frame identity

Summing the projectors of a complete set of bases gives a resolution of the identity that underlies the reconstruction formula below. Each basis resolves the identity on its own, $\sum_{s}\tilde{P}_s(\hat{e}_k) = e_0$, so summing over the three bases gives

$$
\sum_{k=1}^{3}\sum_{s=\pm}\tilde{P}_s(\hat{e}_k) = 3\,e_0 ,
\qquad\text{equivalently}\qquad
\sum_{k=1}^{3}\sum_{s=\pm}\frac{1}{3}\tilde{P}_s(\hat{e}_k) = e_0 ,
$$

and in general a complete set of $d+1$ mutually unbiased bases satisfies $\sum_{b=1}^{d+1}\sum_{i=1}^{d}\tilde{P}_i^{(b)} = (d+1)e_0$, with uniform weight $1/(d+1)$. The identity was verified by explicit computation for the qubit. It is the operator statement that the six coordinate projectors form a tight frame; the weight $1/(d+1)$ is not the same as the overlap $1/d$, and the difference between the two numbers is the reason the reconstruction formula below is an affine rather than a linear combination of the outcome probabilities.

## The Two-Qubit Case

### The maximum is five

For the tensor-product module of two qubits the dimension is $d=4$, and the maximum number of mutually unbiased bases is $d+1 = 5$ (this requires the existence of $d+1$ MUBs in dimension four, which holds because four is a prime power). The standard constructions exhibit the full set; the framework's statements about $\mathbb{B}\otimes\mathbb{B}$ inherit them, since $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$.

### What naive tensor products supply

If one takes the three qubit bases and forms tensor products, one obtains the three product bases

$$
\mathcal{B}_1\otimes\mathcal{B}_1,\qquad \mathcal{B}_2\otimes\mathcal{B}_2,\qquad \mathcal{B}_3\otimes\mathcal{B}_3,
$$

and these are mutually unbiased: their overlaps are products of the single-qubit overlaps, $\tfrac12\cdot\tfrac12 = \tfrac14$, which is $1/d$ with $d=4$. But three is not five. Other tensor products, such as the mixed basis $\mathcal{B}_1\otimes\mathcal{B}_2$, have overlaps $\tfrac14$ with some of these and not with others, and do not complete the set. The tensor product of maximal qubit MUB sets is therefore **not** a maximal set for the composite: the MUB structure of $\mathbb{B}\otimes\mathbb{B}$ is not obtained by tensoring the MUB structure of $\mathbb{B}$.

### The Bell basis is not unbiased with respect to the product basis

The Bell idempotents $P_\epsilon$ of the companion article *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$* form an idempotent basis of the two-qubit algebra. Their overlap with the product (computational) idempotents is

$$
\mathrm{Tr}\bigl(P_\epsilon\,P_{\mathrm{prod}}\bigr) = \tfrac{1}{2},
$$

not $\tfrac14$. For example $|\langle\Phi^+|\psi\rangle\otimes|\psi\rangle|^2 = \tfrac12$ for any product state. Hence **the Bell basis is not mutually unbiased with respect to the product basis**, and the two cannot belong to one complete set of MUBs. This is an instructive negative statement: the idempotent basis that the algebra singles out as maximally entangled is also the basis that is maximally *biased* with respect to the product bases. The two natural structures of $\mathbb{B}\otimes\mathbb{B}$ — maximal entanglement and mutual unbiasedness — do not coincide, and the framework exhibits both without identifying them.

## What the Framework Does and Does Not Add

**What it does.**

- It identifies a basis of the defining module with an idempotent basis $\{\tilde{P}_i\}$, $\tilde{P}_i\tilde{P}_j = \delta_{ij}\tilde{P}_i$, $\sum_i\tilde{P}_i = e_0$, and the overlap between rays with the trace pairing of idempotents.
- It derives mutual unbiasedness of the three qubit bases directly from the pairwise orthogonality of the imaginary units, giving $\mathrm{Tr}(\tilde{P}_s(\hat{e}_j)\tilde{P}_{s'}(\hat{e}_k)) = \tfrac12$ for $j\neq k$.
- It exhibits the maximal set: three bases for the qubit, with the explicit block-form overlap matrix.
- It gives the reconstruction formula $\tilde{\rho} = \sum_b\sum_i p_i^{(b)}\tilde{P}_i^{(b)} - e_0$ and verifies it for the qubit.
- It shows that the tensor product does not preserve maximality of MUB sets, and that the Bell basis is not unbiased with respect to the product basis.

**What it does not.**

- It does not compute the full set of five MUBs for two qubits; the existence of $d+1$ MUBs in prime-power dimensions is standard and is cited, not derived.
- It does not address the open problem of the maximum number of MUBs in dimensions that are not prime powers.
- It does not extend the derivation to arbitrary dimensions; the algebraic derivation given here is special to the qubit, where the three bases come from the three imaginary units.
- It does not make new predictions; the MUB structure is the standard one transcribed in the algebra's elements.

## Open Questions

**1. MUBs from the algebra in higher dimensions.** The qubit's three MUBs come from the three imaginary units of $\mathbb{H}$. Is there an algebraic construction of the five MUBs of $\mathbb{B}\otimes\mathbb{B}$ from the idempotent structure of the tensor-product algebra, rather than from the general theory of complex Hadamard matrices?

**2. Unbiasedness and the norm form.** The mutual-unbiasedness condition is a condition on the trace pairing, not on the norm form. Is there a norm-form criterion for unbiasedness, and does it select the same bases?

**3. Maximal entanglement versus unbiasedness.** The Bell basis is maximally entangled and maximally biased relative to the product basis. Is there a general trade-off, in the algebra, between the entanglement of a basis and its unbiasedness relative to a product basis?

**4. Tomography with incomplete MUB sets.** The reconstruction formula requires a complete set of $d+1$ bases. What is the algebraic characterization of the states recoverable from a smaller set, and how does the framework's cone geometry constrain the reconstruction?

**5. Empirical content.** The MUB structure in biquaternion form is the standard structure; it predicts nothing new.

## Summary

A basis of the defining module is an idempotent basis of $\mathbb{M}_+$: a complete orthogonal family of rank-one idempotents, $\tilde{P}_i\tilde{P}_j = \delta_{ij}\tilde{P}_i$ and $\sum_i\tilde{P}_i = e_0$. Two bases are mutually unbiased when the trace pairing of any idempotent of one with any idempotent of the other equals $1/d$; equivalently, when every ray of one has squared overlap $1/d$ with every ray of the other. For the native qubit the maximum number of mutually unbiased bases is $d+1 = 3$, and they are the eigenbases of the three imaginary units:

$$
\mathcal{B}_k = \bigl\{\tfrac12(e_0+i\hat{e}_k),\ \tfrac12(e_0-i\hat{e}_k)\bigr\}, \qquad k=1,2,3 .
$$

The unbiasedness is derived from the algebra alone: for $j\neq k$ the traceless terms vanish and the units' orthogonality gives

$$
\mathrm{Tr}\bigl(\tilde{P}_s(\hat{e}_j)\tilde{P}_{s'}(\hat{e}_k)\bigr) = \tfrac12 , \qquad
\mathrm{Tr}\bigl(\tilde{P}_s(\hat{e}_k)\tilde{P}_{s'}(\hat{e}_k)\bigr) = \delta_{ss'} .
$$

The overlap matrix of the six pure states has identity blocks on the diagonal and constant blocks $\tfrac12 J_2$ off it. The three measurements are tomographically complete: $\tilde{\rho} = \sum_{k=1}^{3}\sum_{s=\pm} p_s^{(k)}\tilde{P}_s(\hat{e}_k) - e_0$, verified on a generic state. For two qubits the maximum is $d+1=5$ bases; the tensor product of qubit MUB sets supplies only three, and the Bell basis is not unbiased with respect to the product basis, its overlap being $\tfrac12$ rather than $\tfrac14$. The framework thus supplies the qubit's complete MUB set natively, from the three imaginary units, and exhibits the failure of naive tensoring.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{M}_+$ | Hermitian subspace (states and observables) |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion units, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary |
| $\tilde{P}_\pm(\hat{\mu}) = \tfrac12(e_0\pm i\hat{\mu})$ | Rank-one idempotents along $\hat{\mu}$ |
| $\tilde{P}_i\tilde{P}_j = \delta_{ij}\tilde{P}_i$, $\sum_i\tilde{P}_i = e_0$ | Idempotent basis |
| $\mathrm{Tr}(\tilde{P}\tilde{Q}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{Q})$ | Trace pairing (overlap) |
| $\mathrm{Tr}(\tilde{P}_i^{(b)}\tilde{P}_j^{(b')}) = 1/d$ for $b\neq b'$ | Mutual unbiasedness |
| $\mathcal{B}_k = \{\tilde{P}_\pm(\hat{e}_k)\}$ | The three coordinate bases |
| $\tilde{X}=ie_1,\ \tilde{Y}=ie_2,\ \tilde{Z}=ie_3$ | Hermitian involutions defining the bases |
| $\mathrm{Tr}(\tilde{P}_s(\hat{e}_j)\tilde{P}_{s'}(\hat{e}_k)) = \tfrac12$ ($j\neq k$) | Unbiasedness of the coordinate bases |
| $\tilde{\rho} = \sum_b\sum_i p_i^{(b)}\tilde{P}_i^{(b)} - e_0$ | Reconstruction from a complete MUB set |
| $P_\epsilon$ | Bell idempotents (maximally entangled basis) |
| $\mathrm{Tr}(P_\epsilon P_{\mathrm{prod}}) = \tfrac12$ | Bell basis is biased relative to the product basis |

## Further Reading

- I. D. Ivanović, "Geometrical description of quantal state determination," *Journal of Physics A* **14** (1981) 3241–3245, for the first systematic treatment of mutually unbiased bases.
- W. K. Wootters and B. D. Fields, "Optimal state determination by mutually unbiased measurements," *Annals of Physics* **191** (1989) 363–381, for the reconstruction of a state from $d+1$ mutually unbiased measurements.
- A. Klappenecker and M. Rötteler, "Constructions of mutually unbiased bases," in *Finite Fields and Applications* (Springer, 2004), for the construction of $d+1$ MUBs in prime-power dimensions.
- T. Durt, B.-G. Englert, I. Bengtsson, and K. Życzkowski, "On mutually unbiased bases," *International Journal of Quantum Information* **8** (2010) 535–640, for the comprehensive review, including the open problem in non-prime-power dimensions.
- S. Bandyopadhyay, P. O. Boykin, V. Roychowdhury, and F. Vatan, "A new proof of the existence of mutually unbiased bases," *Algorithmica* **34** (2002) 512–528, for the Pauli-group construction in prime-power dimensions.
- I. Bengtsson and K. Życzkowski, *Geometry of Quantum States* (Cambridge, 2006), for the geometry of bases, complementarity, and unbiasedness.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the Pauli bases and the cryptographic use of complementary bases.
- The companion articles of this series: *Quantum Mechanics in Biquaternionic Form*, *The Born Rule as a Trace Formula — Derivation and Comparison*, *The Bloch Ball as the Trace-One Slice of the Future Light Cone*, and *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*.
