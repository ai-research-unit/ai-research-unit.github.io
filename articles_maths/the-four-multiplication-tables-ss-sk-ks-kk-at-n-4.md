# __The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$ at $n=4$__

## Introduction

**The one associative product, restricted to the two halves, gives four tables — a pair of symmetric factors, a symmetric and an antisymmetric one in each order, and a pair of antisymmetric ones — and the four are the four blocks of the multiplication in the $\mathbb{Z}_2\times\mathbb{Z}_2$ grading by parity, with the two diagonal blocks landing in the whole algebra and the two mixed ones in the traceless algebra.**

The article writes the four tables, states the image of each as a bilinear map, records the closures that hold and the ones that fail, shows $SK\neq KS$ with an explicit pair, and identifies the four tables with the four general products of the biquaternion algebra: each general product is a signed sum of the four tables, the sign being the insertion of the conjugation in a slot.

It assumes *The Symmetric and Antisymmetric Parts of a Product at $n=4$* for the parity rule and *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=4$* for the halves. The biquaternion partner is *The Four General Products and Their Relations over the Biquaternion Algebra*; the case $n=2$ is *The Four Multiplication Tables $SS$, $SK$, $KS$, $KK$ at $n=2$*.

## The Four Tables

**Definition.** The four tables are the restrictions of the associative product to the four pairs of halves:

$$
SS:\operatorname{Sym}\times\operatorname{Sym}\to M_4,\quad SK:\operatorname{Sym}\times\operatorname{Skew}\to M_4,\quad KS:\operatorname{Skew}\times\operatorname{Sym}\to M_4,\quad KK:\operatorname{Skew}\times\operatorname{Skew}\to M_4,
$$

each sending a pair to its ordinary product $AB$.

**Proposition.** The four tables split by parity, and the split is the content of each table:

| Table | Symmetric part | Antisymmetric part |
|---|---|---|
| $SS$ | $\tfrac12\{S,S'\}$ | $\tfrac12[S,S']$ |
| $SK$ | $\tfrac12[S,K]$ | $\tfrac12\{S,K\}$ |
| $KS$ | $\tfrac12[K,S]$ | $\tfrac12\{K,S\}$ |
| $KK$ | $\tfrac12\{K,K'\}$ | $\tfrac12[K,K']$ |

**Proof.** The parity rule of the product article: for two symmetric or two antisymmetric factors the anticommutator is symmetric and the commutator antisymmetric, while for a symmetric and an antisymmetric factor the anticommutator is antisymmetric and the commutator symmetric.

**Corollary.** The two diagonal tables have their symmetric parts symmetric and their antisymmetric parts antisymmetric, and the two mixed tables have the two roles interchanged.

**Proof.** Read the table row by row.

**The dimensions.** $\operatorname{Sym}_4$ has dimension $10$ and $\operatorname{Skew}_4$ dimension $6$, so the four bilinear maps start from spaces of dimensions $20$, $60$, $60$ and $36$ respectively, and the ten and the six are the numbers that govern every count in the block.

**Proof.** The dimension of a space of bilinear maps on a pair of spaces of dimensions $p$ and $q$ is $pq$; the halves have dimensions $10$ and $6$.

## The Images

**Theorem.** The images of the four tables, as spans over the whole domain, are

$$
\operatorname{Im}SS=M_4,\qquad \operatorname{Im}SK=\mathfrak{sl}_4,\qquad \operatorname{Im}KS=\mathfrak{sl}_4,\qquad \operatorname{Im}KK=M_4,
$$

of dimensions $16,15,15,16$.

**Proof.** For $SS$: $E_{ii}E_{ii}=E_{ii}$ and $(E_{ij}+E_{ji})E_{jj}=E_{ij}$ give all sixteen units. For $KK$: $(E_{ij}-E_{ji})^{2}=-(E_{ii}+E_{jj})$ and $(E_{ij}-E_{ji})(E_{jk}-E_{kj})=E_{ik}$ give all sixteen. For the mixed tables: $\operatorname{tr}(SK)=0$ for every pair, so the image lies in $\mathfrak{sl}_4$, and $E_{ii}(E_{ij}-E_{ji})=E_{ij}$ and $(E_{ij}-E_{ji})E_{jj}=E_{ij}$ produce every unit with $i\neq j$, together with the traceless diagonals from products of two off-diagonal units, which fills the fifteen.

**Corollary.** The two mixed tables never produce a scalar matrix, while the two diagonal ones do.

**Proof.** A scalar matrix has nonzero trace, and every mixed product has trace zero; $E_{ii}E_{ii}=E_{ii}$ is not scalar but sums of such products give $\mathrm I_4$.

**The ranks in one slot.** Fixing the first factor and letting the second run, the map $S'\mapsto SS'$ has rank $10$ when $S$ is invertible and less otherwise, and $K'\mapsto KK'$ has rank $6$ when $K$ is invertible; the rank drops exactly where the fixed factor has a kernel meeting the half.

**Proof.** Multiplication by an invertible matrix is injective; a singular factor has a kernel, and the intersection of that kernel with the half is what is lost.

**The closures.** The diagonal tables are not closed: $SS$ leaves the symmetric half and $KK$ leaves the antisymmetric half. The mixed tables are not closed either: $SK$ leaves the antisymmetric half unless the factors commute, as $E_{13}$ shows.

**Proof.** The instances are those of the product article: $S=E_{12}+E_{21}$ and $S'=E_{11}$ give $E_{21}$ from $SS$; $K=E_{12}-E_{21}$ and $K'=E_{23}-E_{32}$ give $E_{13}$ from $KK$; $S=E_{11}$ and $K=E_{12}-E_{21}$ give $E_{12}$ from $SK$, which is neither symmetric nor antisymmetric.

## $SK$ and $KS$ Are Not the Same Table

**Proposition.** $SK\neq KS$ as bilinear maps, and their values on a pair are related by transposition:

$$
(SK)(S,K)=SK,\qquad (KS)(S,K)=KS=-(SK)^{\mathsf T}.
$$

**Proof.** $(SK)^{\mathsf T}=K^{\mathsf T}S^{\mathsf T}=-KS$.

**Corollary.** The two mixed tables have the same image up to sign — both are $\mathfrak{sl}_4$, which is stable under transposition — and they differ as maps.

**Proof.** The relation $KS=-(SK)^{\mathsf T}$ identifies the images as transposes, and $\mathfrak{sl}_4$ is stable under transposition since the transpose preserves the trace.

**The example.** $S=E_{11}$ and $K=E_{12}-E_{21}$ give $SK=E_{12}$ and $KS=-E_{21}$, two different matrices, transposes up to sign.

**Proof.** Direct multiplication.

**Why the asymmetry is structural.** The left multiplication by $S$ and the right multiplication by $S$ are different operators, and transposition exchanges them; the mixed tables inherit that exchange. A table that treated $SK$ and $KS$ as one would be a table of the symmetrised product, which is a different object.

## The Biquaternion Reading

**The four general products.** The biquaternion algebra carries four products, one for each choice of reading each slot as it stands or through a conjugation:

$$
\tilde Q_1\tilde Q_2,\qquad \tilde Q_1^{\natural}\tilde Q_2,\qquad \tilde Q_1\tilde Q_2^{\ast},\qquad \tilde Q_1^{\natural}\tilde Q_2^{\ast}.
$$

**Theorem.** With the two projections $P_\pm$ onto the symmetric and the antisymmetric half, every general product expands into the four tables with signs given by the insertions:

$$
A^{\mathsf T}B=(P_+A-P_-A)(P_+B+P_-B)=SS+SK-KS-KK,
$$

$$
AB^{\mathsf T}=(P_+A+P_-A)(P_+B-P_-B)=SS-SK+KS-KK,
$$

and the doubly conjugated product carries a minus on both odd slots, that is $SS-SK-KS+KK$.

**Proof.** Inserting the transpose in a slot replaces $P_+-P_-$ for $P_++P_-$, which is the identity on the even part and the negative of the identity on the odd part; expanding the product of the four blocks gives the displayed sums.

**Corollary.** The four tables and the four general products are the same $\mathbb{Z}_2\times\mathbb{Z}_2$ read twice: the tables are the unsigned blocks, the products the signed ones, and the passage from one to the other is the insertion of the involution in a slot.

**Proof.** The two slots are independent in both constructions, and the sign rule is the same in each: the odd part changes sign under the insertion.

**Why this article is the matrix-side partner.** *The Four General Products and Their Relations over the Biquaternion Algebra* reads the four products on the coordinates of the algebra, with the two conjugations $\natural$ and $\ast$, and finds that no two agree on every pair. This article reads the same four on the matrix side, with the transpose in place of $\natural$ and the conjugation in place of $\ast$, and the four tables are its unsigned skeleton. In the axis-free frame the transpose **is** the quaternion conjugation, so the two readings coincide there, and the dictionary between the two articles is exact in that frame and carries a correction matrix in the Peirce frame.

## Summary

The product restricted to the two halves gives four tables, and each table splits into a symmetric and an antisymmetric part whose places depend on the parities of the factors: the two diagonal tables have the anticommutator symmetric, the two mixed tables have it antisymmetric.

The diagonal tables span the whole algebra and the mixed ones span the traceless algebra, of dimensions $16$ and $15$; no table is closed, and the failure is exhibited by three explicit pairs of invertibles. The two mixed tables are transposes of one another up to sign and are different maps with the same image.

The four tables are the unsigned blocks of the multiplication in the grading by parity, and the four general products of the biquaternion algebra are the signed combinations obtained by inserting the conjugation in one slot or both. The axis-free frame, where the transpose is the quaternion conjugation, makes the dictionary between the two articles exact.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $SS$, $SK$, $KS$, $KK$ | the four tables of the product on the halves |
| $P_\pm$ | the projections onto $\operatorname{Sym}_4$ and $\operatorname{Skew}_4$ |
| $\mathfrak{sl}_4$ | the traceless matrices, the image of the mixed tables |
| $\natural$, $\ast$ | the quaternion conjugation and the conjugate transpose |
| $\mathbb{Z}_2\times\mathbb{Z}_2$ | the group of the four choices of reading |
| $T_{\mu\nu}$ | the axis-free basis, where the transpose is $\natural$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for gradings by a group and the block decomposition of a product.
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the same four choices read on the coordinates.
- [The Symmetric and Antisymmetric Parts of a Product at $n=4$](the-symmetric-and-antisymmetric-parts-of-a-product-at-n-4.html), for the parity rule behind every table.
- [The Jordan Algebra $\operatorname{Sym}_4$](the-jordan-algebra-sym-4.html), for the symmetrised product of the diagonal table.
- [The Four Multiplication Tables $SS$, $SK$, $KS$, $KK$ at $n=2$](the-four-multiplication-tables-ss-sk-ks-kk-at-n-2.html), for the same four tables at order two.
