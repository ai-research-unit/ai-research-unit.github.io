# __Complementary Idempotents and the Peirce Decomposition__

## Introduction

An idempotent $e$ of an algebra has a unique complement $f=1_A-e$. The pair $e,f$ is the smallest complete orthogonal family: $e^2=e$, $f^2=f$, $ef=fe=0$ and $e+f=1_A$. The one-idempotent Peirce decomposition of *Unital Algebras*, §*Idempotents and the Peirce Decomposition*,

$$
A=eAe\oplus eAf\oplus fAe\oplus fAf,
$$

is the case $r=2$ of a decomposition indexed by a complete orthogonal family $e_1,\dots,e_r$. The present article passes from the pair to the family, and uses the complement as the operation that refines and coarsens the decomposition.

Three results organise the article. First, the complement $e\mapsto1_A-e$ is a fixed-point-free involution of the set of idempotents, it reverses the natural order, and inside a corner the relevant complement is the relative one $g-e$. Second, a complete orthogonal family gives the Peirce decomposition $A=\bigoplus_{i,j}A_{ij}$ with $A_{ij}=e_iAe_j$ and the multiplication table $A_{ij}A_{kl}\subseteq\delta_{jk}A_{il}$; the algebra is a generalised matrix algebra of corners. Third, splitting a member refines the decomposition, merging a block coarsens it, and a central family is exactly a product decomposition.

**Terminology.** In this article *complementary* refers to a pair $e,f=1_A-e$, with $ef=fe=0$ and $e+f=1_A$. The same word is used in *Idempotents and Involutions of an Algebra*, §*Complementary Idempotents*, for the involution-relative condition $e^*=1_A-e$. That condition says that the plain complement is also the image under an involution; it is a special case, and no involution is assumed here.

Throughout, $k$ is a field, $A$ is a unital associative $k$-algebra with $1_A\neq0$, and $e_1,\dots,e_r$ is a finite complete orthogonal family of idempotents. The algebra is not assumed commutative, and it is finite-dimensional only where a statement says so. The complement of $e$ is $f=1_A-e$, and the Peirce corners of a family are $A_{ij}=e_iAe_j$. The one-idempotent case is *Unital Algebras* and *Off-Diagonal Peirce Components and Noncentral Idempotents*; the involution-relative theory is *Idempotents and Involutions of an Algebra*; the primitive case is *Primitive Idempotents and Minimal Left Ideals*; the diagonal part of an eigenvalue decomposition is *The Centraliser and the Diagonal Peirce Part*; and the operator reading is *The Sandwich Operators on the Peirce Components*.

## The Complement Operation

### Definition and elementary properties

**Definition.** Two idempotents $e,f$ are **orthogonal** when $ef=fe=0$. They are **complementary** when they are orthogonal and $e+f=1_A$. The **complement** of an idempotent $e$ is $f=1_A-e$.

**Proposition.** Let $e\in A$ be idempotent and $f=1_A-e$.

**(a)** $f$ is idempotent, $ef=fe=0$ and $e+f=1_A$; it is the unique idempotent with these properties.

**(b)** The map $e\mapsto1_A-e$ is an involution of the set of idempotents, and it has no fixed point.

**(c)** $e$ is trivial, $e=0$ or $e=1_A$, exactly when $f$ is trivial; $e$ is central exactly when $f$ is central.

**(d)** $e$ is a unit exactly when $e=1_A$, and then $f=0$.

**(e)** A nontrivial idempotent is a zero divisor: $e(1_A-e)=0=(1_A-e)e$.

**(f)** If $e$ is primitive, $f$ need not be primitive.

*Proof.* (a) $f^2=1_A-2e+e^2=1_A-e=f$, and $ef=e-e^2=0=fe$. If $g$ is idempotent with $eg=ge=0$ and $e+g=1_A$, then $g=1_A-e=f$. (b) $1_A-(1_A-e)=e$. A fixed point would satisfy $2e=1_A$; multiplying by $e$ gives $2e=e$, hence $e=0$ and $1_A=0$, against the hypothesis. (c) The first assertion follows from (b), and $e$ is central exactly when $1_A-e$ is. (d) If $e$ is a unit, then $e=e^2$ gives $1_A=e$ after multiplying by $e^{-1}$. (e) is the computation of (a). (f) In $M_3(k)$ the idempotent $E_{11}$ is primitive, because its corner is $kE_{11}$, while $1_A-E_{11}$ has corner $M_2(k)$, which contains the idempotent $E_{22}$ different from $0$ and $1_A-E_{11}$. The corner criterion is that of *Primitive Idempotents and Minimal Left Ideals*, §*The corner criterion*.

**Remark.** Part (f) is the first warning that the complement does not preserve the whole theory: it preserves centrality, but not primitivity. In $M_n(k)$ with $n\ge3$, $E_{11}$ is primitive and $1_A-E_{11}$ has rank $n-1\ge2$, so it is not primitive.

### The order on idempotents

**Definition.** For idempotents $e,f$, write $e\le f$ when $ef=fe=e$.

**Proposition.** Let $e,f$ be idempotents.

**(a)** $e\le f$ exactly when $e=fef$, exactly when $e\in fAf$.

**(b)** The relation $\le$ is a partial order.

**(c)** If $e\le f$, then $f-e$ is idempotent, orthogonal to $e$, and $f=e+(f-e)$.

**(d)** The complement reverses the order: $e\le f$ exactly when $1_A-f\le1_A-e$.

**(e)** If $e\le f$, then $eAe\subseteq fAf$.

*Proof.* (a) If $e=ef=fe$, then $fef=fe=e$. If $e=fef$, then $fe=f(fef)=fef=e$ and $ef=(fef)f=fef=e$. For the second form, $e\le f$ gives $e=fef\in fAf$; conversely, if $e\in fAf$ is idempotent, then $e=fxf$ for some $x$, hence $fe=f^2xf=fxf=e$ and $ef=fxf^2=fxf=e$. (b) Reflexivity is $e^2=e$. Antisymmetry follows from $e=ef=f$. For transitivity, if $e\le f$ and $f\le g$, then $e=ef=e(fg)=(ef)g=eg$ and $e=fe=(gf)e=g(fe)=ge$, so $e\le g$. (c) $(f-e)^2=f^2-fe-ef+e^2=f-e-e+e=f-e$, and $e(f-e)=ef-e=0=(f-e)e$. (d) If $e\le f$, then $(1_A-f)(1_A-e)=1_A-f-e+fe=1_A-f$ and $(1_A-e)(1_A-f)=1_A-f$, so $1_A-f\le1_A-e$; the same computation with the pair interchanged gives the converse. (e) $eae=f(eae)f\in fAf$.

**Remark.** The order is not total. In $M_2(k)$ two distinct rank-one idempotents are incomparable, because the corner of a rank-one idempotent is one-dimensional and contains no idempotent other than $0$ and the idempotent itself.

**Remark.** On all idempotents the product $ef$ need not be idempotent, so the Boolean operations of the next paragraph are not available. In $M_2(k)$, with $e=E_{11}$ and $f=\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix}$, the product $ef=\tfrac12\begin{pmatrix}1&1\\0&0\end{pmatrix}$ has square $\tfrac14\begin{pmatrix}1&1\\0&0\end{pmatrix}\neq ef$.

### The Boolean algebra of central idempotents

**Proposition.** The set $B(A)=\{e\in Z(A):e^2=e\}$ of central idempotents, where $Z(A)$ is the centre of $A$, is a Boolean algebra under

$$
e\wedge f=ef,\qquad e\vee f=e+f-ef,\qquad \neg e=1_A-e,
$$

with bottom $0$ and top $1_A$.

*Proof.* The centre $Z(A)$ is a commutative ring, and $B(A)$ is its set of idempotents. For commuting idempotents, $ef$ is idempotent, and

$$
(e+f-ef)^2=e+f+ef+2ef-2ef-2ef=e+f-ef,
$$

so the join is idempotent as well; the computation is valid in every characteristic and central idempotents commute. The Boolean identities hold because they hold in the commutative ring $Z(A)$, and the order of the Boolean algebra is the order of §*The order on idempotents*.

**Example.** In a commutative algebra every idempotent is central, so the whole set of idempotents is a Boolean algebra. In $M_2(k)$ the only central idempotents are $0$ and $1_A$, so $B(M_2(k))$ has two elements; the rank-one idempotents are not central. In $k\times k$ there are four central idempotents, and $B(k\times k)$ is the four-element Boolean algebra.

### Relative complements

**Definition.** If $e\le g$, the **complement of $e$ in $g$** is $g-e$.

**Proposition.** If $e\le g$, then $g-e$ is idempotent, orthogonal to $e$, and $e+(g-e)=g$. It is the complement of $e$ in the corner $gAg$, whose identity is $g$.

*Proof.* The computation of §*The order on idempotents*, part (c), applies. Moreover $g(g-e)=g-ge=g-e=(g-e)g$, so $g-e$ is the complement of $e$ with respect to the identity $g$ of the corner.

**Remark.** The relative complement differs from the absolute one: $1_A-e=(g-e)+(1_A-g)$ when $e\le g$. The corner $gAg$ uses $g$ as its identity, so its complement operation is $x\mapsto g-x$, not $x\mapsto1_A-x$. This is the reason the Peirce decomposition can be iterated: the decomposition of $gAg$ by $e$ is the part of the decomposition of $A$ by the family $\{e,g-e,1_A-g\}$ that carries the indices $e$ and $g-e$.

**Proposition (stability under corners).** Let $e\le g$. The Peirce corners of $e$ in the algebra $gAg$ are

$$
e(gAg)e=eAe,\qquad e(gAg)(g-e)=eA(g-e),
$$
$$
(g-e)(gAg)e=(g-e)Ae,\qquad (g-e)(gAg)(g-e)=(g-e)A(g-e).
$$

*Proof.* For the second, $e(gAg)(g-e)=e(gag)(g-e)=ea(g-e)$ because $eg=e$ and $g(g-e)=g-e$; the other three are the same computation with the factors on the other side.

## The Peirce Decomposition of a Complete Family

### The decomposition

**Definition.** A family $e_1,\dots,e_r$ of idempotents is **orthogonal** when $e_ie_j=0$ for $i\neq j$, and **complete** when $\sum_ie_i=1_A$.

**Theorem.** Let $e_1,\dots,e_r$ be a complete orthogonal family and $A_{ij}=e_iAe_j$. Then

$$
A=\bigoplus_{i,j=1}^r A_{ij}.
$$

*Proof.* For $a\in A$,

$$
a=1_Aa1_A=\Big(\sum_ie_i\Big)a\Big(\sum_je_j\Big)=\sum_{i,j}e_iae_j,
$$

which lies in the sum. If $\sum_{i,j}x_{ij}=0$ with $x_{ij}\in A_{ij}$, multiply on the left by $e_k$ and on the right by $e_l$: the term $x_{kl}$ survives, because $e_kx_{kl}e_l=x_{kl}$, and every other term carries a factor $e_ke_i$ with $i\neq k$ or $e_je_l$ with $j\neq l$, hence vanishes. So $x_{kl}=0$, and the sum is direct.

**Corollary (dimension).** If $A$ is finite-dimensional, then $\dim A=\sum_{i,j}\dim A_{ij}$.

### The multiplication table

**Theorem.** The corners obey

$$
A_{ij}A_{kl}\subseteq\delta_{jk}A_{il},
$$

and the inclusion can be strict.

*Proof.* $e_iAe_j\cdot e_kAe_l=e_iA(e_je_k)Ae_l$, which is $e_iAe_l$ when $j=k$ and zero otherwise. For strictness, in $T_2(k)$ with $e_1=E_{11}$ and $e_2=E_{22}$ one has $A_{12}A_{21}=0$, while $A_{11}=kE_{11}\neq0$.

**Proposition.** Let $e_1,\dots,e_r$ be a complete orthogonal family.

**(a)** $A_{ii}$ is a subalgebra with identity $e_i$, and $A_{ij}$ is an $(A_{ii},A_{jj})$-bimodule.

**(b)** The diagonal part $D=\bigoplus_iA_{ii}$ is a unital subalgebra with identity $1_A$.

**(c)** The off-diagonal part $N=\bigoplus_{i\neq j}A_{ij}$ is a $D$-bimodule, and $A=D\oplus N$ as $k$-vector spaces.

**(d)** For $r=2$, $N^2\subseteq D$; for $r\ge3$, $N^2$ can have a nonzero off-diagonal component.

*Proof.* (a) The product rule gives $A_{ii}A_{ii}\subseteq A_{ii}$ and $e_iae_i=e_i$ for $e_i$ itself, so $e_i$ is the identity of the corner; the bimodule statement is the cases $j=i$ and $k=j$ of the table. (b) The product of two diagonal terms lies in $A_{ii}A_{jj}$, which is zero for $i\neq j$ by the table, and $\sum_ie_i=1_A$. (c) The same computation shows that the diagonal part acts on the off-diagonal part; the direct sum is the theorem. (d) For $r=2$ the only off-diagonal products are $A_{12}A_{21}\subseteq A_{11}$ and $A_{21}A_{12}\subseteq A_{22}$. For $r\ge3$, $A_{12}A_{23}\subseteq A_{13}$, and in $M_3(k)$ with $e_i=E_{ii}$ one has $E_{12}E_{23}=E_{13}\neq0$.

**The diagonal projection.** Define $\pi:A\to D$ by $\pi(a)=\sum_ie_iae_i$. It is $k$-linear, unital, $D$-bimodule linear, and it is the projection onto $D$ along $N$. Its defect from multiplicativity is

$$
\pi(ab)-\pi(a)\pi(b)=\sum_i\sum_{j\neq i}e_iae_jbe_i.
$$

Hence $\pi$ is multiplicative exactly when $A_{ij}A_{ji}=0$ for all $i\neq j$, the vanishing of the diagonal part of $N^2$. This condition is neither implied by nor implies $N^2\subseteq D$ in general: in $M_2(k)$ with $E_{11},E_{22}$ one has $N^2=D$, so $N^2\subseteq D$, while the product $A_{12}A_{21}=kE_{11}$ is nonzero; in $T_3(k)$ with $E_{11},E_{22},E_{33}$ all the products $A_{ij}A_{ji}$ vanish because one of the two corners is zero, while $A_{12}A_{23}=kE_{13}$ is a nonzero off-diagonal component of $N^2$. It holds in $T_2(k)$, where $A_{12}A_{21}=0$, and then $\pi$ is the diagonal projection of the upper triangular matrices.

### The generalised matrix form

**Proposition.** The map $a\mapsto(a_{ij})$, with $a_{ij}=e_iae_j$, is an isomorphism of $k$-algebras from $A$ onto the algebra of $r\times r$ matrices $(a_{ij})$ with $a_{ij}\in A_{ij}$ and product

$$
(ab)_{il}=\sum_ja_{ij}b_{jl}.
$$

*Proof.* The Peirce decomposition gives a bijection and $k$-linearity, the product formula is the expansion of $ab$, and associativity is inherited from $A$. The identity is the diagonal matrix with entries $e_i$.

**Remark.** This is the **generalised matrix algebra** of the literature. When only the diagonal corners are nonzero, it is the product $\prod_iA_{ii}$ of §*Central Families and Products*. When the family is the one of a matrix algebra, the corners are the rectangular blocks.

### The one-idempotent case

For $r=2$ with $e_1=e$ and $e_2=1_A-e$, the theorem is the four-corner decomposition of *Unital Algebras*, §*Idempotents and the Peirce Decomposition*. The second member is the complement, and the analysis of the off-diagonal part $N$ is *Off-Diagonal Peirce Components and Noncentral Idempotents*. Passing from $r=2$ to general $r$ replaces the four-corner table by the $r\times r$ table of corners. The commutator interpretation of the two-corner case generalises when the family comes from a split element $a=\sum_i\lambda_ie_i$, through the eigenvalues $\lambda_i-\lambda_j$ of $\operatorname{ad}_a$; for an arbitrary family there is no canonical single derivation, but the diagonal projection and the generalised matrix form remain.

## Refinement and Coarsening

### Splitting a member

**Proposition.** Let $e_1,\dots,e_r$ be a complete orthogonal family, and let $e_1=e_{1a}+e_{1b}$ with $e_{1a},e_{1b}$ nonzero orthogonal idempotents. Then $e_{1a},e_{1b},e_2,\dots,e_r$ is a complete orthogonal family, and the old corners split as

$$
e_1Ae_1=e_{1a}Ae_{1a}\oplus e_{1a}Ae_{1b}\oplus e_{1b}Ae_{1a}\oplus e_{1b}Ae_{1b},
$$
$$
e_1Ae_j=e_{1a}Ae_j\oplus e_{1b}Ae_j,\qquad e_iAe_1=e_iAe_{1a}\oplus e_iAe_{1b}
$$

for $i,j\neq1$.

*Proof.* The element $e_{1b}=e_1-e_{1a}$ is the relative complement of $e_{1a}$ in $e_1$, so the first identity is the Peirce decomposition of the corner $e_1Ae_1$ by $e_{1a}$, whose identity is $e_1$. The other two are the expansion $e_1=e_{1a}+e_{1b}$ inside $e_1Ae_j$ and $e_iAe_1$.

**Remark.** Splitting a member is the elementary refinement. Applied to a nontrivial idempotent, it replaces one member by two and increases the number of Peirce corners from $r^2$ to $(r+1)^2$: the corner $e_1Ae_1$ becomes four corners, and each of the $2(r-1)$ corners adjacent to the index $1$ becomes two.

### Merging a block

**Proposition.** Let $e_1,\dots,e_r$ be a complete orthogonal family and let $\{1,\dots,r\}=\bigsqcup_{k=1}^sJ_k$ be a partition. Put $g_k=\sum_{i\in J_k}e_i$. Then $g_1,\dots,g_s$ is a complete orthogonal family, and

$$
g_kAg_l=\bigoplus_{i\in J_k}\bigoplus_{j\in J_l}A_{ij}.
$$

*Proof.* Expand $g_kag_l=\sum_{i\in J_k}\sum_{j\in J_l}e_iae_j$ and use the orthogonality of the family.

**Remark.** The discrete partition gives the original family, and the one-block partition gives $g_1=1_A$ and the trivial decomposition $A=A$. Merging is the inverse of splitting when the split is by a two-element block. For a fixed family, the coarsenings are therefore indexed by the partitions of $\{1,\dots,r\}$, ordered by refinement; the Peirce decomposition of a coarsening is the sum of the corners of the blocks.

### Primitive families

**Definition.** A complete orthogonal family is **primitive** when each member is primitive.

**Proposition.** In a finite-dimensional algebra, every complete orthogonal family of nonzero idempotents can be refined to a primitive one, and the refinement terminates.

*Proof.* A zero member contributes nothing to the Peirce decomposition and is deleted first, so it is enough to refine a family of nonzero idempotents. If $e_i$ is not primitive, write $e_i=e'+e''$ with nonzero orthogonal idempotents. The corner dimension splits as

$$
\dim e_iAe_i=\dim e'Ae'+\dim e'Ae''+\dim e''Ae'+\dim e''Ae'',
$$

and the two diagonal terms are positive. Hence the sum of the squares of the corner dimensions of the family strictly decreases under the split, and since it is a positive integer the process terminates.

**Proposition.** A primitive family admits no nontrivial refinement. In a finite-dimensional algebra the corner $e_iAe_i$ of a primitive idempotent is local; in the semisimple case it is a division algebra.

*Proof.* The first assertion is the definition of primitivity. The second is the corner criterion and the local-ring statement of *Primitive Idempotents and Minimal Left Ideals*, §*The corner criterion* and §*Primitivity without a division corner*.

**Proposition.** Let $e_1,\dots,e_r$ be a complete primitive family and let $z$ be a central idempotent. Then $z=\sum_{i\in J}e_i$ with $J=\{i:ze_i=e_i\}$.

*Proof.* The element $ze_i$ is idempotent, because $(ze_i)^2=z^2e_i^2=ze_i$, and it lies in the corner $e_iAe_i$, because $ze_i=e_i(ze_i)e_i$ using the centrality of $z$. The corner has no idempotent other than $0$ and $e_i$, so $ze_i$ is either $0$ or $e_i$. Summing over $i$ gives $z=\sum_ize_i=\sum_{i\in J}e_i$.

**Remark.** Primitive is not central. In $M_n(k)$, the family $E_{11},\dots,E_{nn}$ is primitive and complete, and its corners are the one-dimensional algebras $kE_{ii}$; but the idempotents are not central when $n\ge2$, so the finest Peirce decomposition is not a product decomposition. The proposition shows the relation between the two: every central idempotent is a sum of members of the primitive family, so the product decomposition is a coarsening of the primitive one, not a refinement of it.

## Central Families and Products

### The criterion

**Theorem.** For a complete orthogonal family $e_1,\dots,e_r$, the following are equivalent.

**(a)** Every $e_i$ is central.

**(b)** $A_{ij}=0$ for all $i\neq j$.

**(c)** The canonical map $\prod_iA_{ii}\to A$, $(a_i)\mapsto\sum_ia_i$, is an isomorphism of unital $k$-algebras.

*Proof.* (a)$\Rightarrow$(b): $A_{ij}=e_iAe_j=Ae_ie_j=0$. (b)$\Rightarrow$(a): for $a\in A$, $e_ia=\sum_je_iae_j=e_iae_i$ and $ae_i=\sum_je_jae_i=e_iae_i$. (b)$\Rightarrow$(c): the Peirce decomposition has only diagonal terms, the product is componentwise because $A_{ii}A_{jj}=0$ for $i\neq j$, and the inverse is $a\mapsto(e_iae_i)_i$. (c)$\Rightarrow$(b): if the canonical map is an isomorphism, then $A$ is the product of the corners through it, and the Peirce corners of a product by its standard idempotents are the diagonal factors.

**Corollary.** A single idempotent $e$ is central exactly when $eA(1_A-e)=(1_A-e)Ae=0$, exactly when $A\cong Ae\times A(1_A-e)$. This is the corollary of *Unital Algebras*, §*Idempotents and the Peirce Decomposition*.

### Atoms and indecomposable factors

**Definition.** An **atom** of $B(A)$ is a minimal nonzero central idempotent.

**Proposition.** In a finite-dimensional algebra, the atoms of $B(A)$ are pairwise orthogonal, finitely many, and sum to $1_A$. If $e$ is an atom, the two-sided ideal $Ae$ is indecomposable as a unital algebra, and $A\cong\prod_{e\ \mathrm{atom}}Ae$.

*Proof.* A finite-dimensional commutative algebra is a finite product of local algebras, and a local algebra has only the idempotents $0$ and $1$; hence $B(A)$ is finite, and a finite Boolean algebra is the power set of its atoms, whose join is $1_A$. A nontrivial central idempotent of $Ae$ would be a central idempotent of $A$ strictly below $e$, against the minimality of $e$.

### The noncentral case

**Remark.** If some $e_i$ is not central, then some off-diagonal corner is nonzero, and the Peirce decomposition is not a product. The two-sided ideal $Ae_iA$ generated by $e_i$ need not be proper: in a simple algebra it is $A$ for every $e_i\neq0$. The one-sided ideals $Ae_i$ and $e_iA$ are proper whenever $e_i\neq1_A$. The failure of centrality is therefore visible in the off-diagonal corners. When $Ae_iA$ is proper, the quotient $A/Ae_iA$ is not the complementary corner in general; the correct substitute for the product decomposition is the Peirce decomposition. The point is developed in *Off-Diagonal Peirce Components and Noncentral Idempotents*.

## Examples

### The split-complex algebra

Let $A=\mathbb{R}[j]/(j^2-1)$ and $\Pi_\pm=\tfrac12(1\pm j)$. Then $\Pi_+^2=\Pi_+$, $\Pi_-^2=\Pi_-$, $\Pi_+\Pi_-=0$ and $\Pi_++\Pi_-=1_A$; the pair is a complete orthogonal family, and it is central because $A$ is commutative. The corners are

$$
A_{++}=\mathbb{R}\Pi_+,\qquad A_{--}=\mathbb{R}\Pi_-,\qquad A_{+-}=A_{-+}=0,
$$

and the canonical map is the isomorphism $A\cong\mathbb{R}\times\mathbb{R}$, $a+bj\mapsto(a+b,a-b)$. The Boolean algebra $B(A)$ has the four elements $0,\Pi_+,\Pi_-,1_A$. This is the smallest nontrivial central family; the comparison with $\mathbb{C}$, which has only $0$ and $1$, is *The Number Systems as Algebras with and without Nontrivial Idempotents*.

### The upper triangular algebra

Let $A=T_2(k)$ and $e_1=E_{11}$, $e_2=E_{22}$. The family is complete and orthogonal, and the corners are

$$
A_{11}=kE_{11},\qquad A_{22}=kE_{22},\qquad A_{12}=kE_{12},\qquad A_{21}=0.
$$

The Peirce matrix is triangular, with dimensions $1,1,1,0$ and total $3=\dim A$. The family is not central, although both idempotents are primitive with corner $k$. The off-diagonal part is $N=kE_{12}$, and $N^2=0$, so the diagonal projection is multiplicative. The example shows that a complete family of primitive idempotents need not give a product decomposition, and that the two mixed corners need not be symmetric.

### The matrix algebra

Let $A=M_n(k)$ and let $V=k^n=\bigoplus_{i=1}^rV_i$ be a direct sum decomposition, with $e_i$ the projection onto $V_i$ along the other summands. Then $e_1,\dots,e_r$ is a complete orthogonal family, and

$$
A_{ij}=e_iAe_j\cong\operatorname{Hom}_k(V_j,V_i),\qquad \dim A_{ij}=n_in_j,
$$

where $n_i=\dim V_i$. The dimension formula reads $\sum_{i,j}n_in_j=(\sum_in_i)^2=n^2$. If all $n_i=1$, the corners are the matrix units $kE_{ij}$; if $r=2$ and $n_1=m$, the four corners have dimensions $m^2,m(n-m),(n-m)m,(n-m)^2$, which is the block decomposition of *Off-Diagonal Peirce Components and Noncentral Idempotents*. The family is not central for $r\ge2$, because $M_n(k)$ is simple.

### The biquaternion algebra

Let $A=\mathbb{B}\cong M_2(\mathbb{C})$ and let $e$ be a rank-one idempotent, with $f=1_A-e$. The four corners are one-dimensional, and the Peirce decomposition is the matrix-unit decomposition in a basis adapted to $e$. The idempotent $e$ is not central, $A$ is simple, and $AeA=A$. The explicit Peirce table of the biquaternion algebra is *Ideals and Peirce Decomposition of the Biquaternion Algebra*, §*The Peirce Decomposition*; the comparison with the other number systems is *The Number Systems as Algebras with and without Nontrivial Idempotents*.

### A noncentral idempotent in $M_3(k)$

Let $e_1=E_{11}$ and $e_2=E_{22}+E_{33}$ in $M_3(k)$. The family is complete and orthogonal, and the corners are

$$
A_{11}=kE_{11},\qquad A_{22}=M_2(k),\qquad A_{12}=\operatorname{span}\{E_{12},E_{13}\},\qquad A_{21}=\operatorname{span}\{E_{21},E_{31}\}.
$$

The dimensions are $1,4,2,2$, with total $9$. The corner $A_{22}$ is noncommutative, the mixed corners have dimension $2$, and neither idempotent is central. The Peirce matrix is the block matrix

| Corner | right $e_1$ | right $e_2$ |
|---|---|---|
| left $e_1$ | $k$ | $k^{1\times2}$ |
| left $e_2$ | $k^{2\times1}$ | $M_2(k)$ |

with the entries read as the corresponding corner algebras and bimodules.

## Summary

The complement of an idempotent $e$ is the unique idempotent $f=1_A-e$ with $ef=fe=0$ and $e+f=1_A$. The map $e\mapsto1_A-e$ is a fixed-point-free involution of the set of idempotents, it reverses the order $e\le f\iff ef=fe=e$, and it preserves centrality but not primitivity: in $M_3(k)$ the idempotent $E_{11}$ is primitive while its complement is not. Inside a corner the complement is the relative one $g-e$, and the Peirce decomposition of the corner $gAg$ by $e$ is the part of the decomposition of $A$ by the family $\{e,g-e,1_A-g\}$ that carries the indices $e$ and $g-e$.

A complete orthogonal family $e_1,\dots,e_r$ gives the Peirce decomposition $A=\bigoplus_{i,j}A_{ij}$ with $A_{ij}=e_iAe_j$, the multiplication table $A_{ij}A_{kl}\subseteq\delta_{jk}A_{il}$, the diagonal subalgebra $D=\bigoplus_iA_{ii}$ and the off-diagonal $D$-bimodule $N=\bigoplus_{i\neq j}A_{ij}$. The algebra is the generalised matrix algebra of its corners, $(ab)_{il}=\sum_ja_{ij}b_{jl}$. The one-idempotent case is $r=2$, and the off-diagonal analysis is *Off-Diagonal Peirce Components and Noncentral Idempotents*. The diagonal projection $\pi(a)=\sum_ie_iae_i$ is multiplicative exactly when $A_{ij}A_{ji}=0$ for all $i\neq j$.

Splitting a member refines the decomposition, and the refinement is the relative-complement construction in the split corner; merging a block of a partition coarsens it, and the corners of the coarsening are the sums of the corners of the block. In a finite-dimensional algebra every family refines to a primitive one, and the corner of a primitive idempotent is local. A central family is exactly a product decomposition, $A\cong\prod_iA_{ii}$; in a finite-dimensional algebra the atoms of the Boolean algebra $B(A)$ give the finest product decomposition. A noncentral family has nonzero off-diagonal corners, and its two-sided ideals $Ae_iA$ need not be proper.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | A field |
| $A$ | A unital associative $k$-algebra with $1_A\neq0$ |
| $1_A$ | The identity of $A$ |
| $e,f$ | Idempotents, $e^2=e$; the complement of $e$ is $f=1_A-e$ |
| $e_1,\dots,e_r$ | A finite complete orthogonal family: $e_ie_j=\delta_{ij}e_i$ and $\sum_ie_i=1_A$ |
| $A_{ij}=e_iAe_j$ | The Peirce corners of the family |
| $D=\bigoplus_iA_{ii}$ | The diagonal part, a unital subalgebra |
| $N=\bigoplus_{i\neq j}A_{ij}$ | The off-diagonal part, a $D$-bimodule |
| $\pi(a)=\sum_ie_iae_i$ | The diagonal projection onto $D$ along $N$ |
| $e\le f$ | The idempotent order: $ef=fe=e$ |
| $g-e$ | The relative complement of $e$ in $g$, when $e\le g$ |
| $B(A)$ | The Boolean algebra of central idempotents |
| $Z(A)$ | The centre of $A$ |
| $r$ | The number of members of the family; the number of corners is $r^2$ |
| $n_i$ | In $M_n(k)$, the dimension of the $i$-th summand of $V$; $\dim A_{ij}=n_in_j$ |
| $\delta_{jk}$ | The Kronecker delta |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition, the corners and the generalised matrix algebra.
- Yurij A. Drozd and Vladimir V. Kirichenko, *Finite Dimensional Algebras* (Springer, 1994), for the Peirce decomposition, the refinement to primitive idempotents and the local corners.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for idempotents, corners and the direct summands of the regular module.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the Boolean algebra of central idempotents and the product decompositions.
- Nicolas Bourbaki, *Algèbre*, Chapitre VII, for the Peirce decomposition and the matrix of corners.
- The corpus article *Unital Algebras*, §*Idempotents and the Peirce Decomposition*, for the one-idempotent case, and *Off-Diagonal Peirce Components and Noncentral Idempotents*, for the off-diagonal part and its commutator interpretation.
