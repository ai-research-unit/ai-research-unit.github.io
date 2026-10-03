
# __Split Bioctonions and the Clifford Algebra Cl(7)__

## Introduction

The complex octonions $\mathbb{C}\otimes\mathbb{O}$ are non-associative, but their left multiplications form an associative algebra, the complex octonionic chain algebra, which is the Clifford algebra $\mathrm{Cl}(6)$; the companion article *Complex Octonions and the Clifford Algebra Cl(6)* builds it in full, together with a maximal totally isotropic subspace of ladder operators, an intrinsic $\mathrm{su}(3)\oplus\mathrm{u}(1)$, a primitive idempotent and an eight-dimensional minimal left ideal whose basis carries the charges $0,\tfrac13,\tfrac13,\tfrac13,\tfrac23,\tfrac23,\tfrac23,1$. This article adjoins to that construction a single central **split** unit. The result is the **complex split bioctonionic chain algebra**,
$$
\mathrm{Cl}(7) \cong \mathrm{Cl}(6)\oplus\mathrm{Cl}(6) \cong M_8(\mathbb{C})\oplus M_8(\mathbb{C}),
$$
the complex Clifford algebra of the **split bioctonions** $\mathbb{D}\otimes_{\mathbb{R}}\mathbb{O}$. Its structure is fixed by the same mechanism as the one-rung-lower case of *Complex Split Biquaternions and the Clifford Algebra Cl(3)*: the volume element of an odd-dimensional Clifford algebra is central, and here it is an involution, so it splits the algebra into the direct sum of two copies of the complex octonionic chain algebra,
$$
\mathrm{Cl}(7) = \mathrm{Cl}(7)\Pi_+ \oplus \mathrm{Cl}(7)\Pi_-, \qquad \Pi_\pm = \tfrac12(1\pm J), \qquad J = e_1e_2e_3e_4e_5e_6e_7 .
$$
Each copy is a full $\mathrm{Cl}(6)$ and therefore carries its own Fano chain algebra, its own ladder operators, its own $\mathrm{su}(3)\oplus\mathrm{u}(1)$ and its own eight-dimensional minimal left ideal with the same charge spectrum; the two copies are the two **pinor representations** of $\mathrm{Cl}(7)$, are inequivalent, and are interchanged by the parity automorphism $e_i\mapsto -e_i$. This is the algebraic content of a generation of fermions carrying both chiralities, developed in *Left-Right Symmetric Fermions from Complex Split Biquaternions and Bioctonions*.

The article is the octonionic member of the doubling pair whose lower member is *Complex Split Biquaternions and the Clifford Algebra Cl(3)*. The octonions, their norm, their conjugation and their relation to the division algebras are *Octonion Algebra* and *Octonion Norm and Invertibility*; the complex octonions, Furey's Fano convention, the chain algebra $\mathrm{Cl}(6)\cong M_8(\mathbb{C})$, its ladder operators, its $\mathrm{su}(3)$, its primitive idempotent and its charges are *Complex Octonions and the Clifford Algebra Cl(6)*; the general ladder and number-operator construction is *Maximal Totally Isotropic Subspaces and Their Unitary Symmetries*; and the split bioctonions' lower-dimensional relative is *Split-Biquaternion Algebra*.

**Conventions.** The seven generators $e_1,\dots,e_7$ satisfy
$$
e_i^2=-1, \qquad e_ie_j=-e_je_i \quad (i\neq j),
$$
so that $\{e_i,e_j\}=-2\delta_{ij}$, and the $2^7=128$ monomials are a $\mathbb{C}$-basis of $\mathrm{Cl}(7)\cong\mathrm{Cl}_7(\mathbb{C})$. The first six are the six units of the companion article, and their product is the **$\mathrm{Cl}(6)$ volume element**
$$
\Gamma := e_1e_2e_3e_4e_5e_6, \qquad \Gamma^2=-1,
$$
which *Complex Octonions and the Clifford Algebra Cl(6)* writes as $e_7$. In the present article the label $e_7$ denotes the **seventh generator**, not that volume element; the two labels must not be read index by index across the two articles. The Hermitian adjoint is fixed by $e_i^{\dagger}=-e_i$ and $i^{\dagger}=-i$, so that $\gamma_i=ie_i$ are Hermitian, as in the companion articles; the scalar imaginary is $i$. The split complex algebra is $\mathbb{D}$, with unit $j$, $j^2=+1$, as in *Split-Biquaternion Algebra*; the octonion multiplication is that of *Octonion Algebra*, and the warning of the companion article applies — the chain algebra result is stated in terms of the Clifford algebra, not in terms of the corpus octonion basis index by index.

## The Bioctonions and the Split Bioctonions

**Definition.** The **bioctonions** are the complexification $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{O}$ of the octonions; the **split bioctonions** are the tensor product $\mathbb{D}\otimes_{\mathbb{R}}\mathbb{O}$ of the split complex algebra with the octonions; and the **complex split bioctonions** are the complexification
$$
\mathbb{C}\otimes_{\mathbb{R}}\mathbb{D}\otimes_{\mathbb{R}}\mathbb{O}.
$$

**Proposition (splitting of the complex split bioctonions).** The split complex algebra decomposes as $\mathbb{D}\cong\mathbb{C}\oplus\mathbb{C}$ through the idempotents $\tfrac12(1\pm j)$, and consequently
$$
\mathbb{C}\otimes_{\mathbb{R}}\mathbb{D}\otimes_{\mathbb{R}}\mathbb{O} \cong (\mathbb{C}\otimes_{\mathbb{R}}\mathbb{O}) \oplus (\mathbb{C}\otimes_{\mathbb{R}}\mathbb{O}).
$$

*Proof.* Since $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{D}\cong\mathbb{C}\oplus\mathbb{C}$ (*Split-Complex Algebra*), tensoring with $\mathbb{O}$ over $\mathbb{R}$ distributes: $\mathbb{C}\otimes\mathbb{D}\otimes\mathbb{O}\cong(\mathbb{C}\oplus\mathbb{C})\otimes\mathbb{O}\cong(\mathbb{C}\otimes\mathbb{O})\oplus(\mathbb{C}\otimes\mathbb{O})$. $\square$

Thus the complex split bioctonions are not new non-associative material: they are a pair of copies of the complex octonions. What is new is the algebra generated by their left multiplications.

**Proposition (chain algebra of a direct sum).** If $A$ is a real algebra and $L_A$ is the algebra generated by the left multiplications $L_a:b\mapsto ab$, then the chain algebra of $A\oplus A$ is $L_A\oplus L_A$.

*Proof.* Left multiplication by $(a,b)\in A\oplus A$ is $L_{(a,b)}=L_a\oplus L_b$, since the product in a direct sum is componentwise; as $a$ and $b$ range over $A$ the pairs $(L_a,L_b)$ range over $L_A\oplus L_A$, and the generated algebra is the direct sum. $\square$

**Theorem (the chain algebra of the complex split bioctonions).** The chain algebra of the complex split bioctonions is the complex Clifford algebra
$$
\mathrm{Cl}(7) \cong \mathrm{Cl}(6)\oplus\mathrm{Cl}(6) \cong M_8(\mathbb{C})\oplus M_8(\mathbb{C}),
$$
of complex dimension $128$, and its two direct summands are the two copies of the complex octonionic chain algebra of *Complex Octonions and the Clifford Algebra Cl(6)*.

*Proof.* By the two propositions, the chain algebra is $L_{\mathbb{C}\otimes\mathbb{O}}\oplus L_{\mathbb{C}\otimes\mathbb{O}}\cong\mathrm{Cl}(6)\oplus\mathrm{Cl}(6)$. The low-dimensional classification gives $\mathrm{Cl}_6(\mathbb{C})\cong M_8(\mathbb{C})$ and $\mathrm{Cl}_7(\mathbb{C})\cong M_8(\mathbb{C})\oplus M_8(\mathbb{C})$, and the two are isomorphic as algebras; both statements were confirmed by the dimension count $2\cdot 64=128=2^7$. $\square$

## The Volume Element and the Doubling

**Proposition (the volume element).** The element
$$
J := e_1e_2e_3e_4e_5e_6e_7 = \Gamma e_7
$$
satisfies
$$
J^2=1, \qquad J e_i = e_i J \quad (i=1,\dots,7), \qquad J^{\dagger}=J .
$$
That is, $J$ is central, it is an involution, and it is self-adjoint.

*Proof.* Each generator crosses the other six once, at the cost of six signs, which cancel, so $J$ commutes with every generator and hence with the algebra. The square is $(-1)^{n(n-1)/2}c^n$ at $n=7$, $c=-1$, that is, $(-1)^{21}(-1)^7=+1$. The adjoint reverses seven anti-Hermitian factors, at the cost of $(-1)^7$ from anti-Hermiticity and one more sign from the reversal of seven anticommuting factors, and $(-1)^7\cdot(-1)=+1$, so $J^{\dagger}=J$. All three identities were checked on the generators with zero residual. $\square$

The centrality of $J$ is the statement that the algebra is odd-dimensional; the reality $J^2=+1$ is the statement that it is *split* rather than complex, and it is the one place where the octonionic case differs from $\mathrm{Cl}(6)$, whose volume element $\Gamma$ has square $-1$ and generates a $\mathrm{u}(1)$ rather than a splitting.

**Proposition (the seventh generator is the $\mathrm{Cl}(6)$ volume element).** Because $J=\Gamma e_7$ and $\Gamma$ anticommutes with $e_7$,
$$
e_7 = -\Gamma J .
$$
On each central summand, where $J$ acts as the scalar $\pm1$, the seventh generator acts as $\mp\Gamma$, the $\mathrm{Cl}(6)$ volume element, with opposite signs on the two summands.

*Proof.* From $\Gamma^2=-1$ and $e_7\Gamma=-\Gamma e_7$: $\Gamma J=\Gamma^2e_7=-e_7$, so $e_7=-\Gamma J$, and $J$ is $\pm1$ on the summands. $\square$

**Theorem (the central splitting).** With $\Pi_\pm=\tfrac12(1\pm J)$, the elements $\Pi_+,\Pi_-$ are a complete family of orthogonal central idempotents,
$$
\Pi_+^2=\Pi_+, \qquad \Pi_-^2=\Pi_-, \qquad \Pi_+\Pi_-=0, \qquad \Pi_++\Pi_-=1,
$$
and
$$
\mathrm{Cl}(7) = \mathrm{Cl}(7)\Pi_+ \oplus \mathrm{Cl}(7)\Pi_- ,
$$
a direct sum of two two-sided ideals, each of complex dimension $64$ and each isomorphic to the complex octonionic chain algebra,
$$
\mathrm{Cl}(7)\Pi_\pm \cong \mathrm{Cl}(6) \cong M_8(\mathbb{C}).
$$

*Proof.* Idempotency, orthogonality and completeness come from $J^2=1$ as in the companion Cl(3) article; centrality from centrality of $J$. The two-sided ideals are the two simple summands of $\mathrm{Cl}(7)\cong M_8(\mathbb{C})\oplus M_8(\mathbb{C})$, each of complex dimension $64$; left multiplication by $\Pi_\pm$ was checked to be a rank-$64$ projector of the $128$-dimensional space. $\square$

**Theorem (the parity automorphism and the two pinor representations).** The map
$$
\sigma : \mathrm{Cl}(7)\to\mathrm{Cl}(7), \qquad \sigma(e_i)=-e_i ,
$$
is an algebra automorphism which fixes the even monomials and negates the odd ones, satisfies $\sigma(J)=-J$, and interchanges the two summands, $\sigma(\Pi_+)=\Pi_-$, $\sigma(\Pi_-)=\Pi_+$. The two summands are the two pinor representations of $\mathrm{Cl}(7)$, inequivalent and distinguished by the eigenvalue $\pm1$ of the central volume element $J$; equivalently, by the proposition above, by the sign of the $\mathrm{Cl}(6)$ volume element $\Gamma$ that each induces.

*Proof.* As in the companion Cl(3) article: sending every generator to its negative preserves the quadratic relations and is invertible; on the volume element the seven sign flips give $\sigma(J)=(-1)^7J=-J$; and the two projections are the two nonequivalent simple modules of $M_8(\mathbb{C})\oplus M_8(\mathbb{C})$. $\square$

## The Furey Structure in Each Summand

Each summand is a $\mathrm{Cl}(6)$ and inherits the whole octonionic chain structure of the companion article verbatim. It is collected here in the form used in the companion physics article.

**Proposition (the ladder operators).** Define, as in *Complex Octonions and the Clifford Algebra Cl(6)*,
$$
\alpha_1=\tfrac12(-e_5+ie_4), \qquad \alpha_2=\tfrac12(-e_3+ie_1), \qquad \alpha_3=\tfrac12(-e_6+ie_2),
$$
with Hermitian conjugates $\alpha_i^{\dagger}$. Then
$$
\{\alpha_i,\alpha_j\}=0, \qquad \{\alpha_i^{\dagger},\alpha_j^{\dagger}\}=0, \qquad \{\alpha_i,\alpha_j^{\dagger}\}=\delta_{ij}I ,
$$
so that $\operatorname{span}\{\alpha_1,\alpha_2,\alpha_3\}$ is a three-dimensional maximal totally isotropic subspace of the complexified six-space, its conjugate span is the conjugate MTIS, and the six together span the six-space.

*Proof.* Direct expansion in the Clifford relations $e_i^2=-1$, $e_ie_j=-e_je_i$; all nine relations in each family were recomputed inside $\mathrm{Cl}(7)$ with zero residual, confirming that adjoining the seventh generator does not disturb them (the $\alpha_i$ do not involve $e_7$). $\square$

**Theorem (the ideal and its charges in each summand).** Let
$$
\omega := \alpha_1\alpha_2\alpha_3, \qquad P := \omega\,\omega^{\dagger}=\alpha_1\alpha_2\alpha_3\,\alpha_3^{\dagger}\alpha_2^{\dagger}\alpha_1^{\dagger},
\qquad N := \sum_{i=1}^{3}\alpha_i^{\dagger}\alpha_i .
$$
Then $P$ is a primitive idempotent, $\alpha_iP=0$, and
$$
S := \mathrm{Cl}(7)\,P = \operatorname{span}_{\mathbb{C}}\bigl\{\,P,\ \alpha_1^{\dagger}P,\ \alpha_2^{\dagger}P,\ \alpha_3^{\dagger}P,\
\alpha_3^{\dagger}\alpha_2^{\dagger}P,\ \alpha_1^{\dagger}\alpha_3^{\dagger}P,\ \alpha_2^{\dagger}\alpha_1^{\dagger}P,\
\alpha_3^{\dagger}\alpha_2^{\dagger}\alpha_1^{\dagger}P\,\bigr\}
$$
is an eight-dimensional minimal left ideal on which $N$ takes the values $0,1,1,1,2,2,2,3$, so that the charge operator
$$
Q=\tfrac13 N
$$
takes the values
$$
0,\ \tfrac13,\ \tfrac13,\ \tfrac13,\ \tfrac23,\ \tfrac23,\ \tfrac23,\ 1 .
$$
The intrinsic symmetry algebra on $S$ is $\mathrm{su}(3)\oplus\mathrm{u}(1)$; the $\mathrm{su}(3)$ is generated by the eight chains $\Lambda_1,\dots,\Lambda_8$ of the companion article, and the $\mathrm{u}(1)$ by $N$.

*Proof.* The construction is that of *Complex Octonions and the Clifford Algebra Cl(6)* carried out on the generators $e_1,\dots,e_6$ inside $\mathrm{Cl}(7)$, which satisfy the same relations. The rank of $P$, the independence of the eight elements, the eigenvalues of $N$ on them and the commutation of $\Lambda_1$ with $N$ were recomputed inside $\mathrm{Cl}(7)$ with zero residual; the $\mathrm{su}(3)$ structure constants and the weight and Casimir computations are the companion article's and are not repeated. $\square$

Because the $\alpha_i$, $P$, $N$ and $\Lambda_a$ involve only $e_1,\dots,e_6$, they commute with the seventh generator and hence with $J$; the ideal $S$ therefore lies inside a single summand, and its image under the parity automorphism is the corresponding ideal of the other summand. Explicitly,
$$
[\Lambda_a,J]=0, \qquad [N,J]=0, \qquad [\Lambda_a,N]=0
$$
(all residuals zero), so the two summands carry **the same** $\mathrm{su}(3)\oplus\mathrm{u}(1)$ and the same charge spectrum, and differ only in chirality: the eigenvalue of $J$, equivalently the sign of $\Gamma$.

## Summary

The split bioctonions are $\mathbb{D}\otimes_{\mathbb{R}}\mathbb{O}$, and the complex split bioctonions are $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{D}\otimes_{\mathbb{R}}\mathbb{O}\cong(\mathbb{C}\otimes_{\mathbb{R}}\mathbb{O})\oplus(\mathbb{C}\otimes_{\mathbb{R}}\mathbb{O})$. Their chain algebra, the algebra generated by the left multiplications, is the complex Clifford algebra
$$
\mathrm{Cl}(7) \cong \mathrm{Cl}(6)\oplus\mathrm{Cl}(6) \cong M_8(\mathbb{C})\oplus M_8(\mathbb{C}),
$$
of complex dimension $128$. Its volume element $J=e_1e_2e_3e_4e_5e_6e_7$ is central, self-adjoint and an involution, $J^2=1$, and through the idempotents $\Pi_\pm=\tfrac12(1\pm J)$ it splits the algebra into two copies of the complex octonionic chain algebra $\mathrm{Cl}(6)\cong M_8(\mathbb{C})$, each of complex dimension $64$. The seventh generator acts on the two copies as the $\mathrm{Cl}(6)$ volume element $\Gamma=e_1\cdots e_6$ with opposite signs, $e_7=-\Gamma J$. The parity automorphism $e_i\mapsto-e_i$ negates $J$ and interchanges the two copies, which are the two inequivalent pinor representations of $\mathrm{Cl}(7)$, distinguished by the eigenvalue of $J$; this is the doubling of the octonionic chain algebra into the two chiralities of a generation. Each copy carries the Furey ladder operators with $\{\alpha_i,\alpha_j^{\dagger}\}=\delta_{ij}$, an eight-dimensional minimal left ideal with charges $0,\tfrac13,\tfrac13,\tfrac13,\tfrac23,\tfrac23,\tfrac23,1$ under $Q=\tfrac13N$, and the same intrinsic $\mathrm{su}(3)\oplus\mathrm{u}(1)$, which commutes with $J$: the two copies differ only in chirality. The construction is the six-dimensional case of the general statement that the chain algebra of a split normed algebra is $\mathrm{Cl}(2n)\oplus\mathrm{Cl}(2n)\cong\mathrm{Cl}(2n+1)$, of which the quaternionic case is *Complex Split Biquaternions and the Clifford Algebra Cl(3)*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{O}$, $\mathbb{C}\otimes\mathbb{O}$ | Octonions and complex octonions (bioctonions) |
| $\mathbb{D}\otimes\mathbb{O}$ | Split bioctonions |
| $\mathbb{C}\otimes\mathbb{D}\otimes\mathbb{O}\cong(\mathbb{C}\otimes\mathbb{O})\oplus(\mathbb{C}\otimes\mathbb{O})$ | Complex split bioctonions |
| $e_1,\dots,e_7$ | Clifford generators, $e_i^2=-1$, $e_ie_j=-e_je_i$ |
| $\Gamma=e_1\cdots e_6$ | $\mathrm{Cl}(6)$ volume element, $\Gamma^2=-1$; the companion's $e_7$ |
| $J=e_1\cdots e_7=\Gamma e_7$ | $\mathrm{Cl}(7)$ volume element, central, self-adjoint, $J^2=1$ |
| $e_7=-\Gamma J$ | Seventh generator as the $\mathrm{Cl}(6)$ volume element on each summand |
| $\Pi_\pm=\tfrac12(1\pm J)$ | Complete orthogonal central idempotents |
| $\mathrm{Cl}(7)\Pi_\pm\cong\mathrm{Cl}(6)\cong M_8(\mathbb{C})$ | The two summands, each of complex dimension $64$ |
| $\sigma:e_i\mapsto-e_i$ | Parity automorphism, interchanges the summands |
| $\alpha_i,\alpha_i^{\dagger}$ | Furey ladder operators of a summand |
| $N=\sum_i\alpha_i^{\dagger}\alpha_i$ | Number operator |
| $P=\alpha_1\alpha_2\alpha_3\alpha_3^{\dagger}\alpha_2^{\dagger}\alpha_1^{\dagger}$ | Primitive idempotent of a summand |
| $S=\mathrm{Cl}(7)P$ | Eight-dimensional minimal left ideal |
| $Q=\tfrac13N$ | Charge operator, values $0,\tfrac13,\tfrac23,1$ |
| $\Lambda_1,\dots,\Lambda_8$ | $\mathrm{su}(3)$ generators, commuting with $N$ and $J$ |

## Further Reading

- V. Vaibhav and T. P. Singh, "Left-Right Symmetric Fermions and Sterile Neutrinos from Complex Split Biquaternions and Bioctonions," arXiv:2108.01858, for the construction of this article's algebra and its physics reading.
- C. Furey, "Standard model physics from an algebra?" (2016), arXiv:1611.09182, for the octonionic chain algebra, its ladder operators, its $\mathrm{su}(3)$ and its minimal left ideal, which the two summands reproduce.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the classification $\mathrm{Cl}_7(\mathbb{C})\cong M_8(\mathbb{C})\oplus M_8(\mathbb{C})$, the centrality of the volume element of an odd complex Clifford algebra, and the two pinor representations.
- H. B. Lawson and M.-L. Michelsohn, *Spin Geometry* (Princeton, 1989), for the volume element, the chirality grading and the passage $\mathrm{Cl}(2n)\to\mathrm{Cl}(2n+1)$.
- J. C. Baez, "The octonions," *Bulletin of the American Mathematical Society* **39** (2002) 145–205, for the octonions, the complex octonions and the split octonions.
- Companion article *Complex Octonions and the Clifford Algebra Cl(6)*, for the chain algebra, the ladder operators, the $\mathrm{su}(3)$, the idempotent and the charges of each summand, and the warning about the two bases.
- Companion article *Complex Split Biquaternions and the Clifford Algebra Cl(3)*, for the same doubling in the quaternionic case.
- Companion article *Maximal Totally Isotropic Subspaces and Their Unitary Symmetries*, for the general ladder, number-operator and charge construction.
