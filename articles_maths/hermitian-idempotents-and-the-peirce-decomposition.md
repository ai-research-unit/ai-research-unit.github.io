# __Hermitian Idempotents and the Peirce Decomposition__

## Introduction

An idempotent is an element equal to its own square, and a single idempotent of an associative algebra with a unit splits the algebra into four pieces: two **corners**, where the idempotent or its complement acts on both sides, and two **mixed** spaces, where one acts on the left and the other on the right. This splitting is the **Peirce decomposition**, and it carries a multiplication table that records which pieces may be multiplied together. The present article reads that decomposition through the involution of a sesqualgebra.

The involution does two things to the decomposition. It singles out the idempotents it fixes, the **Hermitian idempotents** $e^{*} = e$, and it exchanges the two mixed spaces of such an idempotent while carrying each corner to itself. And when the sesquilinear product is read as the derived operation $x \star y = xy^{*}$ of the algebra, the Peirce table of the derived product is the **transpose** of the table of the algebra product: the two indices that must agree sit on the right in the sesquilinear table, whereas they sit in the middle in the ordinary one. This reflection is the mark that the conjugate-linear slot leaves on the decomposition.

**Setting.** Throughout, $A$ is an associative $R$-algebra with a unit $1$, $\varsigma$ is an involution of $R$, and $*$ is a $\varsigma$-semilinear involution of $A$; the derived operation $\star$, $x \star y = xy^{*}$, makes $A$ a sesqualgebra in the sense of *Sesqualgebras*, and it is the sesquilinear product of this article. The algebra product is written by juxtaposition and the derived product with $\star$, so that $x \star y = xy^{*}$ holds throughout and $e^{2} = e$ refers to the algebra product. The Peirce decomposition itself, with its table, is *Unital Algebras*, §*Idempotents and the Peirce Decomposition*; the involution and the derived product are those of *Hermitian and Skew-Hermitian Elements* and *Units and the Unitary Elements*; and the $*$-subalgebras are those of *Subalgebras and the Involution*.

## Idempotents and Hermitian Idempotents

### The Definition

**Definition.** An element $e \in A$ is an **idempotent** when $e^{2} = e$, and a **Hermitian idempotent** when $e^{2} = e$ and $e^{*} = e$. Since the sesquilinear product of this article is the derived operation, $e \star e = ee^{*}$, and the theorem below identifies the two notions: the elements with $e \star e = e$, called the **$\star$-idempotents**, are exactly the Hermitian idempotents, so the derived operation of the model has no idempotent of its own beyond them.

**Remark.** The elements $0$ and $1$ are idempotents of the algebra, and both are Hermitian, the unit because $1^{*} = 1$ by *Units and the Unitary Elements*. In a division algebra they are the only idempotents: if $e^{2} = e$ with $e \neq 0$ then $e = 1$ after multiplying by $e^{-1}$. A Hermitian idempotent different from $0$ and $1$ is therefore neither a unit nor nilpotent, and it exists only when the algebra is not a division algebra.

### The Involution on the Idempotents

**Proposition.** If $e$ is an idempotent then $e^{*}$ is an idempotent, so the involution permutes the idempotents, and the map $e \mapsto e^{*}$ is an involution of the set of idempotents whose fixed points are the Hermitian idempotents.

**Proof.** Since $*$ is anti-multiplicative and of order two, $(e^{*})(e^{*}) = (ee)^{*} = e^{*}$; hence $e^{*}$ is idempotent, and applying the same computation to $e^{*}$ returns $e$. The fixed points are by definition the elements with $e^{*} = e$, which are the Hermitian idempotents. $\square$

### The Idempotents of the Derived Operation

**Theorem.** Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution $*$ and let $\star$ be the derived operation $x \star y = xy^{*}$. An element $e \in A$ satisfies $e \star e = e$ if and only if $e^{2} = e$ and $e^{*} = e$.

**Proof.** One has $e \star e = ee^{*}$. If $ee^{*} = e$, applying the involution gives $(ee^{*})^{*} = e^{*}$, that is $e e^{*} = e^{*}$ because $(e^{*})^{*} = e$, so $e = ee^{*} = e^{*}$ and $e$ is Hermitian; then $e^{2} = ee^{*} = e$. Conversely if $e^{2} = e$ and $e^{*} = e$ then $e \star e = ee^{*} = e^{2} = e$. $\square$

**Remark.** The theorem is the reason the article is about Hermitian idempotents: the derived operation of the model has no $\star$-idempotent other than them. An idempotent of the algebra that the involution moves is an idempotent of the algebra product and not of the sesquilinear one. In $M_2(k)$ with the transpose, for instance, the element

$$
e = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}
$$

satisfies $e^{2} = e$ and is not symmetric, and $e \star e = ee^{\mathrm{T}} = 2E_{11} \neq e$. In a general sesqualgebra, where the product and the involution are independent, an element with $e \star e = e$ need not be fixed by $*$; for a derived operation that cannot happen, and the derived operation is the model treated here.

## The Peirce Decomposition

### The Classical Splitting

**Theorem (recalled, *Unital Algebras*).** Let $e$ be an idempotent and put $f = 1 - e$. Then $f$ is an idempotent orthogonal to $e$, the algebra splits as a direct sum of the four **Peirce spaces**

$$
A = eAe \oplus eAf \oplus fAe \oplus fAf ,
$$

and, writing $e_{1} = e$ and $e_{2} = f$, the products of the spaces obey

$$
(e_i A e_j)(e_k A e_l) \subseteq \delta_{jk}\, e_i A e_l .
$$

The **corners** $eAe$ and $fAf$ are subalgebras with units $e$ and $f$, and the **mixed spaces** $eAf$ and $fAe$ are bimodules over the two corners and not subalgebras.

**Proof.** This is the Peirce decomposition of *Unital Algebras*, §*Idempotents and the Peirce Decomposition*, and it is recalled here in the notation of the present article. The expansion $a = (e + f)a(e + f) = eae + eaf + fae + faf$ gives the sum, the annihilation $e_{j}e_{k} = \delta_{jk}e_{j}$ gives the table, and the two corners are closed because $eAe \cdot eAe \subseteq e^{2}Ae^{2} = eAe$, with $e$ acting as their unit. $\square$

### The Role of the Unit

**Remark.** The decomposition uses a unit, and it is the unit of the algebra rather than a unit of the sesquilinear product. For a general $\varsigma$-sesquilinear product a two-sided unit would force $(\lambda - \varsigma(\lambda))A = 0$ for every $\lambda$: applied to $x = 1$ and $y = \lambda a$ the second scalar rule gives $1 \cdot (\lambda a) = \varsigma(\lambda)\,a$, while the left unit gives $1 \cdot (\lambda a) = \lambda a$, so $\lambda a = \varsigma(\lambda) a$. Over $(\mathbb{C}, \varsigma)$ with $\lambda = i$ this forces $A = 0$, so a genuinely sesquilinear product carries at most a one-sided unit. This is the collapse of *Sesqualgebras*, §*The Collapse at the Identity*, read at the unit: there the same scalar identity is shown to make an associative or a commutative product of full type bilinear, $\varsigma = \mathrm{id}$. The derived operation of the model carries $1$ as a right unit only, $a \star 1 = a 1^{*} = a$, and it is the algebra unit $1$ that the Peirce decomposition reads.

## The Involution on the Peirce Spaces

### The Exchange of the Mixed Spaces

**Theorem (the exchange).** Let $e$ be a Hermitian idempotent and $f = 1 - e$. Then $f$ is a Hermitian idempotent and the involution exchanges the two indices of each Peirce space,

$$
(e_i A e_j)^{*} = e_j A e_i ,
$$

so the two corners $eAe$ and $fAf$ are carried to themselves and the involution exchanges the two mixed spaces, $(eAf)^{*} = fAe$ and $(fAe)^{*} = eAf$.

**Proof.** For the complement, $f^{*} = (1 - e)^{*} = 1 - e^{*} = 1 - e = f$, so $f$ is Hermitian. For the spaces, $(e_i a e_j)^{*} = e_j^{*} a^{*} e_i^{*} = e_j a^{*} e_i$ by the anti-multiplicativity of $*$ and the Hermitian character of the two idempotents, and $a^{*}$ runs over $A$ with $a$, so $(e_i A e_j)^{*} = e_j A e_i$. $\square$

**Corollary (the corners are $*$-subalgebras).** For a Hermitian idempotent the corners $eAe$ and $fAf$ are stable under the involution, so each is a $*$-subalgebra of $A$, and the restriction of $*$ to it is a $\varsigma$-semilinear involution.

**Proof.** They are subalgebras by the classical theorem and $(eAe)^{*} = eAe$, $(fAf)^{*} = fAf$ by the exchange; the restriction of $*$ is additive, of order two, anti-multiplicative, and $\varsigma$-semilinear on the same scalars. $\square$

**Remark.** Writing $A_{ij} = e_i A e_j$, the theorem says $A_{ij}^{*} = A_{ji}$: the involution acts on the four spaces as the transposition of their two indices. This is the algebraic form of the statement that conjugation reverses the order of a product, read on the decomposition.

### Why the Hermitian Condition is Needed

**Remark.** The classical decomposition holds for every idempotent, but the exchange holds only for the Hermitian ones. For a general idempotent $e$ and $f = 1 - e$ the same computation gives

$$
(eAf)^{*} = f^{*} A e^{*} ,
$$

which is $fAe$ when $e$ is Hermitian, since then $f$ is too, and which need not be $fAe$ for a general idempotent. In $M_2(k)$ with the transpose and the non-symmetric idempotent $e$ above one has $f^{*}Ae^{*} \neq fAe$, so the conjugate of the mixed space $eAf$ is not the other mixed space $fAe$. The Hermitian condition is therefore what makes the involution exchange the two mixed spaces.

## Orthogonality and the Partial Order

### Orthogonal Hermitian Idempotents

**Definition.** Two idempotents $e$ and $f$ are **orthogonal** when $ef = fe = 0$.

**Proposition.** For Hermitian idempotents, $ef = 0$ if and only if $fe = 0$.

**Proof.** For Hermitian $e$ and $f$, $(ef)^{*} = f^{*}e^{*} = fe$, so $fe = (ef)^{*}$ and one of the two products vanishes exactly when the conjugate of the other does. $\square$

**Remark.** For Hermitian idempotents one has $e \star f = ef^{*} = ef$ and $f \star e = fe$, so the two notions of orthogonality, for the algebra product and for the derived product, coincide on Hermitian idempotents.

### The Sum of Two Hermitian Idempotents

**Theorem.** Suppose $A$ associative and $2$ invertible in $R$, and let $e$ and $f$ be Hermitian idempotents. Then $e + f$ is an idempotent if and only if $ef = fe = 0$.

**Proof.** If $ef = fe = 0$ then $(e + f)^{2} = e^{2} + ef + fe + f^{2} = e + f$, so $e + f$ is an idempotent, and this direction uses neither associativity nor $2$. Conversely if $(e + f)^{2} = e + f$ then $e^{2} + ef + fe + f^{2} = e + f$, that is $ef + fe = 0$. Multiplying that relation on the left by $e$ gives $ef + efe = 0$ and on the right by $e$ gives $efe + fe = 0$, whence $ef = fe = -efe$; then $ef = fe$ and $2ef = ef + fe = 0$. As $2$ is invertible, $ef = 0$, and $fe = ef = 0$. $\square$

**Remark.** Both hypotheses are used in the forward direction: the multiplication by $e$ on either side is associativity, and the deduction $ef = 0$ from $2ef = 0$ is the invertibility of $2$. The second cannot be dropped. Over $\mathbb{F}_{2}$ the Hermitian idempotents $e = E_{22}$ and $f = 1$ of $M_2(\mathbb{F}_{2})$ with the transpose satisfy $e + f = E_{11}$, an idempotent, because $1 = E_{11} + E_{22}$ in characteristic two, while $ef = E_{22} \neq 0$. The Hermitian hypothesis is carried for the rest of the section, where the equivalence of $ef = 0$ and $fe = 0$ does use it; the implication proved here does not.

### The Partial Order

**Definition.** For Hermitian idempotents write $e \preceq f$ when $ef = fe = e$.

**Proposition.** The relation $\preceq$ is a partial order on the Hermitian idempotents, and $0 \preceq e \preceq 1$ for every Hermitian idempotent $e$.

**Proof.** It is reflexive because $e^{2} = e$. It is antisymmetric: if $e \preceq f$ and $f \preceq e$ then $e = ef = f$. It is transitive: if $e \preceq f$ and $f \preceq g$ then $ef = e$ and $fg = f$, so

$$
eg = (ef)g = e(fg) = ef = e, \qquad ge = g(fe) = (gf)e = fe = e ,
$$

and $e \preceq g$; both chains use associativity. Finally $0 \preceq e$ because $0e = e0 = 0$, and $e \preceq 1$ because $e1 = 1e = e$. $\square$

**Proposition.** If $e \preceq f$ then $g = f - e$ is a Hermitian idempotent orthogonal to $e$ with $f = e + g$. Conversely if $g$ is a Hermitian idempotent orthogonal to $e$ then $e \preceq e + g$.

**Proof.** If $e \preceq f$ then $fe = ef = e$, so $g^{*} = f^{*} - e^{*} = f - e = g$ and

$$
g^{2} = (f - e)^{2} = f^{2} - fe - ef + e^{2} = f - e - e + e = f - e = g ,
$$

while $eg = ef - e^{2} = e - e = 0$ and $ge = fe - e^{2} = 0$. Conversely if $g$ is Hermitian and $eg = ge = 0$ then $e(e + g) = e^{2} + eg = e$ and $(e + g)e = e^{2} + ge = e$, so $e \preceq e + g$. $\square$

**Proposition (the join of orthogonal idempotents).** If $e$ and $f$ are orthogonal Hermitian idempotents then $e + f$ is their least upper bound for $\preceq$.

**Proof.** The element $e + f$ is a Hermitian idempotent because the two are Hermitian and $ef = fe = 0$, with no hypothesis on $2$. One has $e(e + f) = e^{2} + ef = e$ and $(e + f)e = e^{2} + fe = e$, so $e \preceq e + f$, and symmetrically $f \preceq e + f$. If $e \preceq g$ and $f \preceq g$ then $eg = ge = e$ and $fg = gf = f$, so

$$
(e + f)g = eg + fg = e + f, \qquad g(e + f) = ge + gf = e + f ,
$$

and $e + f \preceq g$. Hence $e + f$ is the least upper bound. $\square$

**Remark.** The Hermitian idempotents carry the operations that a Boolean algebra carries: $0$ is the least element and $1$ the greatest, $f - e$ is the complement of $e$ inside $f$, and a pair of orthogonal idempotents has a join. The analogy stops short of the Boolean laws because two Hermitian idempotents need not be comparable or orthogonal, and the complement is available only inside a larger idempotent rather than in the algebra as a whole.

## The Corner as a Sesqualgebra

**Theorem.** Let $e$ be a Hermitian idempotent. Then the corner $eAe$ is stable under the involution and under the derived product, it contains $e$, and with the restricted product $\star$ and the restricted involution it is a sesqualgebra. The element $e$ is a right $\star$-unit of it, and the corner is again the derived operation of an associative algebra with a unit, namely of $eAe$ itself with the restricted product and the unit $e$.

**Proof.** For $u = eae$ and $v = ebe$ in $eAe$ one has $v^{*} = eb^{*}e \in eAe$ by the exchange, so

$$
u \star v = uv^{*} = (eae)(eb^{*}e) = e\,(ae b^{*})\,e \in eAe ,
$$

and the corner is closed under the derived product; it is stable under $*$ and contains $e$. The two scalar rules are inherited from $A$, and the restriction of $*$ is an additive, anti-multiplicative involution of order two with the same $\varsigma$-semilinearity, so $eAe$ is a sesqualgebra. In it the element $e$ acts on the right, $u \star e = u e^{*} = ue = u$, and not on the left in general, so $e$ is a right $\star$-unit. The restricted juxtaposition is the product of the subalgebra $eAe$, whose unit is $e$, and the restricted $\star$ is by definition its derived operation. $\square$

**Remark.** The corner is an object of the same kind as the algebra it comes from, so the theory of this article applies to it in turn: its Hermitian idempotents are the elements of $eAe$ with $g^{2} = g$ and $g^{*} = g$, and its Hermitian elements are $H(eAe) = eAe \cap H(A)$.

## The Sesquilinear Peirce Table

### The Transposed Table

**Theorem.** Let $e$ be a Hermitian idempotent, $f = 1 - e$, and write $A_{ij} = e_i A e_j$ with $e_{1} = e$ and $e_{2} = f$. For the derived product,

$$
A_{ij} \star A_{kl} \subseteq \delta_{jl}\, A_{ik} .
$$

So the two indices that must agree are the right index $j$ of the first factor and the right index $l$ of the second, while the outer indices of the result are the two left indices $i$ and $k$. In the table of the algebra product it is instead the right index of the first factor and the left index of the second that must agree, $(e_i A e_j)(e_k A e_l) \subseteq \delta_{jk} e_i A e_l$; the sesquilinear table is the transpose of the ordinary one.

**Proof.** For $u = e_i a e_j$ and $v = e_k b e_l$ in the two spaces, the conjugate of $v$ is $v^{*} = e_l b^{*} e_k$ by the exchange of the Peirce spaces, so

$$
u \star v = u v^{*} = e_i a\,(e_j e_l)\,b^{*} e_k = \delta_{jl}\, e_i a e_j b^{*} e_k ,
$$

and the last element lies in $e_i A e_k = A_{ik}$ because $e_j b^{*} e_k$ is an element of $A$. The ordinary table is the classical one of *Unital Algebras*. $\square$

### The Products of the Derived Table

**Corollary.** With the notation above: $A_{ij} \star A_{kl} = 0$ unless $j = l$; $A_{ij} \star A_{kj} \subseteq A_{ik}$; and $A_{ij} \star A_{ij} \subseteq A_{ii}$. In particular each diagonal corner is closed under $\star$, and the two mixed spaces annihilate in the reversed order, $A_{12} \star A_{21} = 0$, whereas $A_{12}A_{21} \subseteq A_{11}$ for the algebra product.

**Proof.** The first statement is the general rule; the second is the rule with $l = j$; the third is the rule with $l = j$ and $k = i$. For the mixed spaces, $A_{12} \star A_{21} \subseteq \delta_{21}A_{11} = 0$, while $A_{12}A_{21} \subseteq \delta_{22}A_{11} = A_{11}$ in the ordinary table. $\square$

**Remark (the reading).** The mechanism is the exchange: the involution swaps the two indices of the second factor and sends $A_{kl}$ to $A_{lk}$, and then the classical table is applied to the first factor and to that conjugate, its agreeing indices $j$ and $l$ now both on the right. The reflection is exactly the transposition of the table, and it is the mark that the conjugate-linear slot leaves on the decomposition.

## The Two-Sided Decomposition

**Definition.** A family $e_{1}, \dots, e_{n}$ of Hermitian idempotents is **orthogonal** when $e_{i}e_{j} = 0$ for $i \neq j$, and **complete** when $e_{1} + \cdots + e_{n} = 1$.

**Theorem.** Let $e_{1}, \dots, e_{n}$ be an orthogonal complete family of Hermitian idempotents. Then

$$
A = \bigoplus_{i,j} e_i A e_j ,
$$

the table of the algebra product is $(e_i A e_j)(e_k A e_l) \subseteq \delta_{jk} e_i A e_l$, and the table of the derived product is $(e_i A e_j) \star (e_k A e_l) \subseteq \delta_{jl} e_i A e_k$. The diagonal sum $\bigoplus_{i} e_i A e_i$ is a $*$-subalgebra with unit $1$, each $e_i A e_i$ is a corner with unit $e_i$, and the off-diagonal sum is a bimodule over the diagonal.

**Proof.** Since $\sum_{i} e_{i} = 1$ acts as a unit, $a = \bigl(\sum_{i} e_{i}\bigr) a \bigl(\sum_{j} e_{j}\bigr) = \sum_{i,j} e_i a e_j$, which gives the sum. It is direct: a relation $\sum x_{ij} = 0$ with $x_{ij} \in e_i A e_j$, multiplied on the left by $e_{i'}$ and on the right by $e_{j'}$, leaves $x_{i'j'} = 0$ because $e_{i'} e_i = \delta_{i'i} e_{i'}$ and $e_j e_{j'} = \delta_{jj'} e_j$. For the two tables, the orthogonality $e_i e_j = \delta_{ij} e_i$ of the family gives

$$
(e_i A e_j)(e_k A e_l) = e_i A (e_j e_k) A e_l \subseteq \delta_{jk}\, e_i A e_l ,
$$

and, conjugating the second factor by the exchange so that it lies in $e_l A e_k$,

$$
(e_i A e_j) \star (e_k A e_l) = e_i A (e_j e_l) A e_k \subseteq \delta_{jl}\, e_i A e_k .
$$

The diagonal sum is closed under the product, since $e_i A e_i \cdot e_j A e_j \subseteq \delta_{ij}\, e_i A e_i$, and under $*$, and it contains $1 = \sum e_i$; the off-diagonal sum is carried into itself by multiplication on either side by the diagonal sum, because $e_i A e_i \cdot e_j A e_k \subseteq \delta_{ij}\, e_i A e_k$ with $j \neq k$, and symmetrically, so it is a two-sided bimodule over the diagonal sum. $\square$

**Remark.** The case $n = 2$ is the one-idempotent theorem read with $e_{1} = e$ and $e_{2} = f = 1 - e$, and the two statements are the same. There the off-diagonal sum is the two mixed spaces and its square lands in the diagonal sum, $e_1 A e_2 \cdot e_2 A e_1 \subseteq e_1 A e_1$ and $e_2 A e_1 \cdot e_1 A e_2 \subseteq e_2 A e_2$, the other products of two off-diagonal spaces being zero. For $n \geq 3$ that last statement fails: with three distinct indices $e_1 A e_2 \cdot e_2 A e_3 \subseteq e_1 A e_3$ is again off-diagonal, so only the bimodule statement survives in general. The family form is the one that a coordinate decomposition of a matrix algebra produces.

## The Matrix Model

### The Complex Matrices

**Example.** Let $A = M_n(\mathbb{C})$ with the conjugate transpose and the derived operation $S \star T = ST^{*}$. The Hermitian idempotents are the matrices $P$ with $P^{2} = P = P^{*}$, and by the theorem on the derived operation they are exactly the $\star$-idempotents. For such a $P$ the four Peirce spaces are the four blocks that $P$ cuts out: the corner $PAP$, the two mixed spaces $PA(1 - P)$ and $(1 - P)AP$, and the complementary corner $(1 - P)A(1 - P)$. When $P$ is diagonal with $0$ and $1$ on the diagonal, the corner $PAP$ is the algebra of the matrices supported on the coordinates where the diagonal entry is $1$, and it is isomorphic to $M_k(\mathbb{C})$ with $k = \operatorname{tr} P$, while the two mixed spaces are the two off-diagonal blocks.

### Two-by-Two Cases

**Example (a diagonal idempotent).** For $A = M_2(\mathbb{C})$ with $P = E_{11}$ and $Q = 1 - P = E_{22}$ the four Peirce spaces are the four lines $\mathbb{C}E_{11}$, $\mathbb{C}E_{12}$, $\mathbb{C}E_{21}$ and $\mathbb{C}E_{22}$. The corner $PAP = \mathbb{C}E_{11}$ is a copy of $\mathbb{C}$ with the product $z \star w = z\bar w$, and the derived table reads

$$
E_{11} \star E_{11} = E_{11}, \qquad E_{12} \star E_{12} = E_{11}, \qquad E_{21} \star E_{21} = E_{22}, \qquad E_{11} \star E_{12} = 0 ,
$$

with $E_{12} \star E_{21} = E_{21} \star E_{12} = 0$ in agreement with the general rule, against $E_{12}E_{21} = E_{11}$ for the algebra product. The difference between the two tables is visible in the pair $E_{12}, E_{21}$: the ordinary product of the two mixed lines is the corner, while the derived product vanishes.

**Example (a non-diagonal idempotent).** For $A = M_2(\mathbb{C})$ and

$$
P = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} ,
$$

a real symmetric matrix, so that $P^{2} = P = P^{*}$, the corner $PAP = \mathbb{C}P$ is again a copy of $\mathbb{C}$ with $P$ as its unit, and the two mixed spaces are $PA(1 - P)$ and $(1 - P)AP$.

### The Field and the Quaternions

**Example.** For $A = \mathbb{C}$ with the conjugation and $x \star y = x\bar y$, an idempotent is a solution of $e\bar e = e$. Writing $e = a + bi$ with real $a$ and $b$, the product $e\bar e = a^{2} + b^{2}$ is real, so $b = 0$ and $a^{2} = a$, whence $e$ is $0$ or $1$. The only idempotents are therefore $0$ and $1$ and the Peirce decomposition is the trivial one. The quaternion algebra $\mathbb{H}$ with the quaternion conjugation is a division algebra, so its only idempotents are $0$ and $1$ as well, and its Peirce decomposition is trivial; the biquaternion algebra $\mathbb{B} \cong M_2(\mathbb{C})$ falls under the matrix model.

### A Central Idempotent that is Not Hermitian

**Example.** In $A = R \times R$ with the involution that exchanges the two factors, the element $e = (1,0)$ is a central idempotent, and it is not Hermitian, since $e^{*} = (0,1) \neq e$. The classical Peirce decomposition applies to it, but the corner $eAe = R \times 0$ is not stable under the involution, its conjugate being $0 \times R$; the two mixed spaces are both $0$ here, since $eAf = fAe = 0$, so the failure is visible only at the corner. Centrality and the Hermitian condition are therefore independent: the unit is central and Hermitian, the element $(1,0)$ is central and not Hermitian, and a non-central Hermitian idempotent is $E_{11}$ in $M_n(\mathbb{C})$ with the conjugate transpose.

## Summary

A Hermitian idempotent of a sesqualgebra is an idempotent fixed by the involution. For the derived operation $x \star y = xy^{*}$ of an associative algebra with a unit and a $\varsigma$-semilinear involution, the $\star$-idempotents are exactly the Hermitian idempotents of the algebra, since $e \star e = ee^{*}$ and $e \star e = e$ already force $e^{*} = e$. The Peirce decomposition of the algebra, recalled from *Unital Algebras*, splits $A = eAe \oplus eAf \oplus fAe \oplus fAf$ with $f = 1 - e$, and the involution acts on it by the exchange $(e_i A e_j)^{*} = e_j A e_i$: it carries the two corners to themselves and exchanges the two mixed spaces. That exchange is exactly what fails for a non-Hermitian idempotent, for which $(eAf)^{*} = f^{*}Ae^{*}$ need not be $fAe$. Two Hermitian idempotents are orthogonal when $ef = 0$, equivalently $fe = 0$, and, when $2$ is invertible, $e + f$ is an idempotent exactly when they are orthogonal; the two hypotheses are used in the forward direction, and over $\mathbb{F}_2$ the implication fails, as $e = E_{22}$ and $f = 1$ in $M_2(\mathbb{F}_2)$ show. The Hermitian idempotents carry the partial order $e \preceq f$ defined by $ef = fe = e$, under which $f - e$ is the complement of $e$ in $f$ and the sum of orthogonal idempotents is their join. A corner of a Hermitian idempotent is a $*$-stable subalgebra and, with the restricted product and involution, a sesqualgebra of the same kind, with $e$ as a right $\star$-unit. Finally the derived product obeys the transposed Peirce table $A_{ij} \star A_{kl} \subseteq \delta_{jl}A_{ik}$, whose two agreeing indices are on the right, against the classical table $(e_i A e_j)(e_k A e_l) \subseteq \delta_{jk}e_i A e_l$ whose agreeing indices are in the middle; the transposition is the mark of the conjugate-linear slot and it separates the two tables, for instance $A_{12} \star A_{21} = 0$ against $A_{12}A_{21} \subseteq A_{11}$. A complete orthogonal family of Hermitian idempotents gives the two-sided decomposition $A = \bigoplus_{i,j} e_i A e_j$, whose diagonal sum is a $*$-subalgebra with unit $1$. The model is $M_n(\mathbb{C})$ with the conjugate transpose, where the Hermitian idempotents are the matrices with $P^{2} = P = P^{*}$, the Peirce spaces of a diagonal idempotent are the four blocks, and the corner is a matrix algebra $M_k(\mathbb{C})$ with $k = \operatorname{tr} P$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $e^{2} = e$ | an idempotent of the associative algebra |
| $e^{*} = e$ | the Hermitian condition; a Hermitian idempotent satisfies both |
| $x \star y = xy^{*}$ | the derived operation, the sesquilinear product of the article |
| $e \star e = e$ | a $\star$-idempotent, equivalently a Hermitian idempotent |
| $f = 1 - e$ | the complementary idempotent, Hermitian when $e$ is |
| $eAe$, $eAf$, $fAe$, $fAf$ | the four Peirce spaces of $e$ |
| $A_{ij} = e_i A e_j$ | the Peirce spaces in the two-index notation, $e_1 = e$, $e_2 = f$ |
| $(e_i A e_j)^{*} = e_j A e_i$ | the exchange of the Peirce spaces by the involution |
| $ef = fe = 0$ | orthogonality of two Hermitian idempotents |
| $A_{ij} \star A_{kl} \subseteq \delta_{jl}A_{ik}$ | the transposed Peirce table of the derived product |
| $e \preceq f \iff ef = fe = e$ | the partial order of the Hermitian idempotents |
| $e_{1}, \dots, e_{n}$ | an orthogonal complete family, $\sum e_i = 1$ |
| $\bigoplus_{i,j} e_i A e_j$ | the two-sided Peirce decomposition |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Graduate Texts in Mathematics 88, Springer, 1982), for the idempotents, the Peirce decomposition of an associative algebra, and the corner algebras that a family of orthogonal idempotents produces.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Graduate Texts in Mathematics 131, Springer, 2001), for the idempotents and the Peirce decomposition in the theory of rings and modules.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the Hermitian elements and the fixed idempotents of an involution and the corners they cut out.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the Hermitian idempotents of an algebra with involution and the self-adjoint idempotents of the classical matrix case.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Peirce decomposition of a Jordan algebra, where a single middle space replaces the two mixed spaces of the associative case.
