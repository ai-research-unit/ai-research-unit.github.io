# __The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_4(\mathbb{C})$__

## Introduction

**The algebra splits into the diagonal of dimension $4$ and the two strictly triangular parts of dimension $6$ each, and the sum of the first two is a Borel subalgebra of dimension $10$ whose group is the invertible upper triangular matrices, the stabiliser of the standard flag.**

The article proves the direct sum and the dimensions, identifies $\mathfrak{sl}_4$ with the three-dimensional traceless diagonal plus twelve root lines, describes the Borel subgroup and the flag it fixes, and reads the two halves against the flag: the symmetric half meets the Borel in the diagonal alone, and the antisymmetric half meets it only at zero.

It assumes *The Fine Decomposition against the Diagonal at $n=4$* for the three pieces and *The Lie Algebra $\mathfrak{gl}_4(\mathbb{C})$ and $\mathfrak{sl}_4(\mathbb{C})$ of $M_4(\mathbb{C})$* for the classical structure. The case $n=2$ is *The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_2(\mathbb{C})$*; the geometric side is *The Space of Idempotents and the Flag Varieties at $n=4$*.

## The Three Pieces and the Two Borels

**Definition.** $\mathfrak{b}=\mathfrak{h}\oplus\mathfrak{n}_+$ and $\mathfrak{b}_-=\mathfrak{h}\oplus\mathfrak{n}_-$.

**Proposition.** $\mathfrak{b}$ and $\mathfrak{b}_-$ are subalgebras, of dimension $10$, and $M_4=\mathfrak{n}_-\oplus\mathfrak{b}=\mathfrak{n}_+\oplus\mathfrak{b}_-$.

**Proof.** The product of two upper triangular matrices is upper triangular, and the diagonal part adds; the dimensions are $4+6=10$ and the direct sums follow from the position split.

**Theorem.** $\mathfrak{b}$ is a maximal solvable subalgebra, and $[\mathfrak{b},\mathfrak{b}]=\mathfrak{n}_+$.

**Proof.** The quotient $\mathfrak{b}/\mathfrak{n}_+$ is $\mathfrak{h}$, abelian, so $\mathfrak{b}$ is solvable with derived algebra inside $\mathfrak{n}_+$; the commutator $[E_{ii},E_{ij}]=(h_i-h_j)E_{ij}$ produces every unit of $\mathfrak{n}_+$, so the derived algebra is exactly $\mathfrak{n}_+$. A subalgebra strictly containing $\mathfrak{b}$ would contain some $E_{ij}$ with $i>j$, and then the bracket with the diagonal produces the transposed unit, generating the simple algebra $\mathfrak{sl}_4$, so no larger solvable subalgebra exists.

**Corollary.** $\mathfrak{n}_+$ is the nilradical of $\mathfrak{b}$, of dimension $6$, and $\mathfrak{b}$ has the semisimple quotient $\mathfrak{h}$.

**Proof.** The derived algebra is nilpotent and is the largest nilpotent ideal, since the quotient by it is abelian and reductive.

**The two Borels.** $\mathfrak{b}$ and $\mathfrak{b}_-$ are opposite: their intersection is $\mathfrak{h}$ and their sum is the algebra.

**Proof.** The intersection of the upper and lower triangular spaces is the diagonal, and $10+10-4=16$.

## The Group Picture

**Definition.** $B_4=\{g\in\mathrm{GL}_4(\mathbb{C}):g_{ij}=0\text{ for }i>j\}$ is the group of invertible upper triangular matrices, and $UT_4$ is its Lie algebra, the space of all upper triangular matrices including the diagonal.

**Proposition.** $B_4$ is a closed connected subgroup of $\mathrm{GL}_4(\mathbb{C})$ of dimension $10$, with Lie algebra $\mathfrak{b}$, and it is the semidirect product of the diagonal torus and the unipotent group $\mathrm I+\mathfrak{n}_+$.

**Proof.** An upper triangular matrix is invertible exactly when its diagonal entries are nonzero, so the group is the product of the four copies of $\mathbb{C}^{\times}$ on the diagonal and the unipotent radical; the exponential of a strictly upper triangular matrix is a polynomial and gives the unipotent group, which is isomorphic to its Lie algebra as an algebraic variety.

**Corollary.** $\dim B_4=10=\dim\mathfrak{b}$, and the unipotent radical has dimension $6$.

**Proof.** The torus contributes $4$ and the unipotent part $6$.

**The two numbers that meet here.** The Borel has dimension $10$ and so does the symmetric half; the unipotent radical has dimension $6$ and so does the antisymmetric half. The coincidence is a coincidence of dimensions only, and the two articles *$UT_4$ as the Complement of the Antisymmetric Part* and *$UT_4$ as a Linear Model of $\operatorname{Sym}_4$: Same Space, Wrong Product* are about the difference behind it.

## The Roots of $\mathfrak{sl}_4$

**Theorem.** With $\mathfrak{h}_0=\{H\in\mathfrak{h}:\operatorname{tr}H=0\}$, of dimension $3$,

$$
\mathfrak{sl}_4=\mathfrak{h}_0\oplus\bigoplus_{\alpha}\mathfrak{g}_\alpha,\qquad \mathfrak{g}_\alpha=\mathbb{C}E_{ij},\quad \alpha=\varepsilon_i-\varepsilon_j,\ i\neq j,
$$

and there are twelve roots, each a one-dimensional root space.

**Proof.** The traceless condition removes one dimension from the diagonal; the twelve off-diagonal units are eigenvectors of $\mathfrak{h}_0$ with the weights $\varepsilon_i-\varepsilon_j$, and the weights are distinct as functionals restricted to $\mathfrak{h}_0$ because $\varepsilon_i-\varepsilon_j=\varepsilon_k-\varepsilon_l$ forces $i=k$ and $j=l$.

**Corollary.** $15=3+12$, and the six roots with $i<j$ are the positive ones for the choice of $\mathfrak{b}$.

**Proof.** $\dim\mathfrak{sl}_4=16-1=15$ and the roots split into the six upper and six lower units.

**The root string.** For a positive root and a simple root the bracket is either zero or another root space, and the two-dimensional strings that occur have length at most three; the Chevalley commutator formulas of $A_3$ record them, and the twelve roots form the root system of type $A_3$, whose Dynkin diagram is a chain of three nodes.

**The half sum and the rank.** The rank is $3$ for the traceless algebra and $4$ for the full one, the number of positive roots is $6$, and $12=2\cdot6$; the Weyl group is the symmetric group on four letters, of order $24$.

**Proof.** The Weyl group of $A_3$ permutes the four coordinates, and its order is $4!=24$.

## The Flag the Borel Stabilises

**Definition.** The **standard flag** is $0\subset\langle e_1\rangle\subset\langle e_1,e_2\rangle\subset\langle e_1,e_2,e_3\rangle\subset\mathbb{C}^{4}$.

**Proposition.** An invertible matrix lies in $B_4$ exactly when it preserves the standard flag, that is when it maps each $\langle e_1,\dots,e_k\rangle$ into itself.

**Proof.** The image of $e_j$ is the $j$-th column; preserving $\langle e_1,\dots,e_k\rangle$ for every $k$ says that the $j$-th column lies in $\langle e_1,\dots,e_j\rangle$, that is $g_{ij}=0$ for $i>j$.

**Corollary.** $\mathrm{GL}_4/B_4$ is the variety of complete flags, of dimension $16-10=6$.

**Proof.** The group acts transitively on flags — any flag can be sent to the standard one — and the stabiliser of the standard flag is $B_4$; the dimension of the quotient is the difference of the dimensions.

**The three partial flags.** Dropping the condition at one step gives the Grassmannians: $\mathrm{GL}_4/P_1=\mathbb{P}^{3}$, $\mathrm{GL}_4/P_2=\mathrm{Gr}_2$, $\mathrm{GL}_4/P_3=\mathrm{Gr}_3$, of dimensions $3$, $4$ and $3$. The parabolic subgroups are the blocks-upper-triangular ones, and the Levi factors are the block-diagonal ones, which are the corner recursions of the Peirce article.

**Proof.** The quotient by a parabolic is the variety of subspaces of the corresponding dimension, and the dimension of $\mathrm{Gr}_k(\mathbb{C}^{4})$ is $k(4-k)$.

## The Halves against the Flag

**Proposition.** $\operatorname{Sym}_4\cap\mathfrak{b}=\mathfrak{h}$ and $\operatorname{Skew}_4\cap\mathfrak{b}=0$; hence $\operatorname{Skew}_4\oplus\mathfrak{b}=M_4$.

**Proof.** A symmetric upper triangular matrix is diagonal, since $s_{ij}=s_{ji}=0$ for $i<j$. An antisymmetric upper triangular matrix is zero, since its diagonal vanishes and its upper entries vanish. Then $\dim(\operatorname{Skew}_4+\mathfrak{b})=6+10-0=16$.

**Corollary.** The antisymmetric half is a complement of the Borel, and the symmetric half is not: it sits inside the Borel as its diagonal.

**Proof.** The first is the dimension count with zero intersection; the second is the identity $\operatorname{Sym}_4\cap\mathfrak{b}=\mathfrak{h}$ of dimension $4$.

**What the flag sees of the halves.** The Borel preserves a flag; the antisymmetric half is transverse to it; the symmetric half shares with it the diagonal, which is the part of the Borel that acts on the flag by rescaling each step. The diagonal is the Levi quotient of the Borel, and the symmetric half meets the Borel exactly in that quotient.

**The three decompositions again.** $\operatorname{Skew}_4\oplus UT_4$ is a split with a solvable summand and a Lie summand; $\operatorname{Sym}_4\oplus\operatorname{Skew}_4$ is a split with a Jordan summand and a Lie summand; $\mathfrak{n}_-\oplus\mathfrak{h}\oplus\mathfrak{n}_+$ refines both. Each answers a different question: which spaces carry a product, which carry a flag, and which diagonalise a form.

## Summary

The algebra is the direct sum of the diagonal of dimension $4$ and the two strictly triangular parts of dimension $6$, and the sum of the diagonal with either triangular part is a Borel subalgebra of dimension $10$, maximal solvable, with derived algebra the corresponding nilpotent part.

The traceless part of the diagonal has dimension $3$ and carries twelve root lines, so $\mathfrak{sl}_4=3+12=15$, with root system $A_3$ and Weyl group of order $24$. The Borel is the Lie algebra of the invertible upper triangular group, which is the stabiliser of the standard complete flag; the quotient has dimension $6$, and the three partial quotients are the Grassmannians of dimensions $3$, $4$, $3$.

Against the flag the antisymmetric half is transverse and complementary, while the symmetric half meets the Borel exactly in the diagonal. The dimensions $10$ and $6$ of the Borel and its radical agree with those of the two halves, and the agreements are numerical only.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{h}$, $\mathfrak{h}_0$ | the diagonal and the traceless diagonal, dimensions $4$ and $3$ |
| $\mathfrak{n}_+$, $\mathfrak{n}_-$ | strictly upper and lower, dimension $6$ |
| $\mathfrak{b}$, $\mathfrak{b}_-$ | the two opposite Borels, dimension $10$ |
| $B_4$ | the invertible upper triangular group |
| $UT_4$ | the upper triangular Lie algebra, dimension $10$ |
| $\varepsilon_i-\varepsilon_j$ | the twelve roots |
| $\mathrm{GL}_4/B_4$ | the complete flag variety, dimension $6$ |

## Further Reading

- James E. Humphreys, *Linear Algebraic Groups* (Springer, 1975), for Borel subgroups, parabolic subgroups and flag varieties.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for root systems and the triangular decomposition.
- [The Fine Decomposition against the Diagonal at $n=4$](the-fine-decomposition-against-the-diagonal-at-n-4.html), for the position split and the weights.
- [The Lie Algebra $\mathfrak{gl}_4(\mathbb{C})$ and $\mathfrak{sl}_4(\mathbb{C})$ of $M_4(\mathbb{C})$](the-lie-algebra-gl4c-and-sl4c-of-m4c.html), for the classical structure of the same algebra.
- [The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_2(\mathbb{C})$](the-triangular-decomposition-h-n-plus-n-minus-of-m2c.html), for the same three pieces at order two.
