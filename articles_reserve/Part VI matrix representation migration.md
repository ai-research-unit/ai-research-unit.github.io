# __Part VI Migration Map — One Representation Pair per Category__

Planning note. It is not an article and does not enter the menu.

## Final Review

This pass checked the map against the corpus, against `maths.md`, and against computed examples, before any article is written. Eight things were wrong and are now corrected. The rest survives.

**Corrected: the split-biquaternion reach.** The draft put the image of $\beta$ inside $\mathrm{End}_{\mathbb{R}}(\mathbb{H}_{\mathbb{D}})=M_8(\mathbb{R})$, of dimension $64$, without saying that the image is far smaller. Every product is block diagonal, so no product has a nonzero off-diagonal block, and each block spans $M_4(\mathbb{R})$. The reach is $16+16=32$, half the ambient. The master table gained a **span** column, because the span is the number the whole "what the pair buys" question turns on.

**Corrected: the coefficient matrix was defined on the ambient space.** The arrays $c(M)$ exist only on the span of the products. They are defined for every operator only when the multiplication map $A\otimes A^{\mathrm{opp}}\to\operatorname{End}_K(A)$ is onto, which holds for $\mathbb{H}$, $\mathbb{H}_{\mathrm s}$ and $\mathbb{B}$ and fails for a commutative algebra and for $\mathbb{H}\oplus\mathbb{H}$. Without the qualification, the criterion $\operatorname{rank}c(M)\le1$ quantifies over operators that have no coefficient matrix.

**Corrected: my own errata item.** I had written that the note's evaluation argument fails, with the counterexample $Q=e_t+e_x$, $P=e_t-e_x$, "so $QP=0$". Computed from the left regular matrix, $QP=2e_t$. The counterexample is false and the note's argument is sound for $\mathbb{H}$, because $\mathbb{H}$ is a division algebra. It does not transfer to the split case, and the errata entry now says exactly that.

**Corrected: three rank sets.** $\mathbb{H}$ and $\mathbb{H}_{\mathrm s}$ were conflated. In the quaternion model every nonzero element is invertible, so the operator rank is in $\{0,4\}$ and not in $\{0,1,2,4\}$; that set belongs to $\mathbb{H}_{\mathrm s}$ and $\mathbb{B}$, where null elements exist. The split-complex rank set was $\{0,2\}$ and is $\{0,1,2\}$, the value one on the null lines. The split-biquaternion set was $\{0,2,4\}$ and is $\{0,4,8\}$, four per block.

**Corrected: the dual sandwich.** The draft wrote $QX\bar Q=Q^{2}X$. The two sides differ: $Q^{2}=q^{2}+2qq'\varepsilon$, while $QX\bar Q=q^{2}X=N(Q)X$. The scalar is the norm, not the square of the element, and only the norm makes the pattern match $\mathbb{C}$, $\mathbb{D}$ and $\mathbb{B}_{\mathrm r}$.

**Corrected: the singular set of $M_2(\mathbb{C})$.** It was called "the union of two quadrics". Over $\mathbb{C}$ it is a quadric hypersurface; over $\mathbb{R}$ it has codimension two in $M_2(\mathbb{C})\cong\mathbb{R}^{8}$, which is why the split-quaternion article contrasts it with its own hypersurface.

**Corrected: the menu surgery of three categories.** The instructions named the wrong heading for the absorbed links. In the split-complex category the three absorbed links sit under three different headings, one of them *Spectral Algebra with the Split Norm*; in the reduced biquaternion category the six sit under four; and the seven `m2r-model-` links of the split-quaternions are distributed over five headings, not three. Every instruction was rewritten against `maths.md` line by line, and the dual instruction, which omitted its deletion, now carries it.

**Corrected: a stale wording.** The order of work still spoke of "the reach of the pairs" as a section. The section no longer exists; the second layer replaced it.

**Verified against the corpus.** All $24$ absorbed slugs exist under the names given and all $18$ new slugs are free. The counts are $18$ new, $24$ absorbed, $25$ kept, and they add up by category and in total. The seven articles proposed for retitling to "Linear Representations" were opened: all seven carry Schur's lemma, the representation ring and the module classification, so the retitle is justified by content and not by taste. The tier-two claim was checked title by title: the quaternioid block has exactly six articles of the form "in the $2\times2$ [or $4\times4$] Matrix Element Representation $M_n(\mathbb{F})_{\dots}$", and the biquaternion-structures block has exactly three "$M_2(\mathbb{C})$ Representation :" articles and three "in the $4\times4$ Left Regular Representation" articles.

**Verified by computation.** $\operatorname{Tr}T_{Q,P}=4Q_tP_t$ and $\det T_{Q,P}=\langle Q\rangle_{\#}^{2}\langle P\rangle_{\#}^{2}$, both symbolic. $\operatorname{rank}T_{Q,P}=\operatorname{rank}\mathsf M(Q)\operatorname{rank}\mathsf M(P)$, with values in $\{0,1,2,4\}$ for $\mathbb{B}$ and $\{0,4\}$ for $\mathbb{H}$. $c(T_{tt}+T_{xx})=\operatorname{diag}(1,1,0,0)$, of rank two, which is the decisive proof of the additive failure. The $\mathbb{C}^2$ criterion on a product, $\det=0$ and rank one, and on $E_{11}+E_{22}$, $\det=1$ and rank two. The block-diagonal structure of every $\mathbb{H}_{\mathbb{D}}$ product.

**Left open, by design.** The six decisions below are decisions, not defects. The retitling of the seven "Element Representations" articles is the one that blocks work; the rest can be settled while writing.

## Review of the First Draft

The first draft was checked against the corpus. Six things were wrong and are corrected below; three were learned.

**One substantive error, repeated in four sections.** The draft claimed that a general endomorphism is a sum of pairs in every category, with a count of two or four. That is false as soon as the algebra is commutative. For a commutative algebra,

$$
L_QR_P(X)=QXP=(QP)X=L_{QP}(X),
$$

so every sandwich is again a left multiplication, the span of the two-sided family is the regular representation alone, and no number of pairs reaches a general endomorphism. The categories concerned are $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$ and the reduced biquaternions. The operators articles now prove the collapse and name what is missing: the conjugate-linear half. The count of pairs survives only for the non-commutative categories, $\mathbb{C}^2$, $\mathbb{H}$, $\mathbb{H}_{\mathrm s}$ and $\mathbb{H}_{\mathbb{D}}$.

**The "two or four" rule was wrong.** The draft said that a different matrix size is a second model. The split-complex $4\times4$ is not a second model of $\mathbb{D}$; it is the regular representation of the complexification $\mathbb{D}_{\mathbb{C}}\cong\mathbb{C}\times\mathbb{C}$, which is the reduced biquaternion algebra. The reduced biquaternion $4\times4$ is the realification of its own $2\times2$ complex model. Both are sections today, in one article each. The rule is now: one pair per **standing** matrix model, and a size that is the realification or the complexification of a covered model is a section. Only the quaternions keep four, because there the two sizes are both standing articles and neither is the realification of the other.

**Three arithmetic errors.** The split-quaternion model was called nine-dimensional; it is four-dimensional over $\mathbb{R}$. The split-biquaternion pair count was eight; the sandwich splits blockwise and each block is the $M_2(\mathbb{H})$ problem, so four. The quaternion pair count was justified by "the algebra is four-dimensional"; the count comes from the size of the coefficient matrix, not from the dimension of the algebra.

**Two wrong formulas.** The trace of the split-biquaternion diagonal matrix is $Q_++Q_-\in\mathbb{H}$, a quaternion, not a sum of two scalars. The split-complex sandwich has $\{N=1\}$ as the kernel of $Q\mapsto\Theta_Q$, not as the kernel of $\Theta_Q$.

**One over-claim.** The $\mathbb{C}^2$ pair was said to absorb half of *The Endomorphisms of $\mathbb{C}^2$*. It absorbs nothing: that article is the algebra $M_2(\mathbb{C})$, which belongs to the biquaternion category.

**Counts corrected.** Twenty-four articles are absorbed, not twenty-five, and the per-category lists now name them. The summary table gained a column recording which algebra each model represents.

**Two facts verified against the corpus.** For the split-quaternions, $\det\mathsf M_2(\tilde q)=\langle\tilde q\rangle_{\natural}=q_t^2+q_x^2-q_y^2-q_z^2$, of signature $(2,2)$, the adjugate is the conjugation and the image is all of $M_2(\mathbb{R})$. For the reduced biquaternions, $\operatorname{tr}=2Q_\blacktriangle$ in the complex model, $\det=Q_\blacktriangle^2-Q_\blacktriangledown^2=Q_+Q_-$, and $\det L_{\breve Q}=|Q_+Q_-|^2$ in the real $4\times4$ model.

**One discovery about tier two.** The biquaternion-structures block already carries the target title pattern on six of its articles, and the quaternioid block carries "in the $2\times2$ Matrix Element Representation" on six. Tier two is therefore twelve renames, not a writing pass.

**One whole layer was missing.** The first draft treated the operators article as "one matrix per side, a pair for the two-sided operator, four pairs for a general endomorphism". That stops one step short. The two technical notes on $T_{Q,P}=L_QR_P$ show that the two-sided family has a structure of its own, and that the structure is the same in every category: the image is a **cone** (the Segre cone of decomposable tensors), a single product is recognised by a **rank-one coefficient matrix**, and a general operator needs exactly **length $=$ coefficient rank** products. The draft's "four pairs" is the special case $n=4$ of that theorem, not an independent fact, and it is wrong where it was applied to commutative algebras. The map now carries this as a second layer with its own sections, master table and per-category numbers.

## What This Map Does

The biquaternion category was rebuilt around two matrix models. Each model got a general article and an operators article:

- *$M_2(\mathbb{C})$ Standard Peirce Representation* and *$M_2(\mathbb{C})$ Standard Peirce Representation : Operators*;
- *$M_4(\mathbb{C})$ e-basis Representation* and *$M_4(\mathbb{C})$ e-basis Representation : Operators*.

Before the rebuild the same material was spread over twenty-four articles, one per topic. The rebuild kept the abstract operator articles, folded the topic articles into the two general articles, and added the missing matrix readings.

This note applies that shape to every category of Part VI from *Complex Numbers* to *Split-Biquaternions*. It gives, for each category, the model, the new articles with their section lists, the articles they absorb, the articles that stay, and the menu surgery.

## The Rule

### The Pair

Every category gets a **general article** and an **operators article** for each of its matrix models.

The general article owns the model: the frame, the two matrices of an element, the product, the trace, the determinant, the spectral projectors, the adjugate, the norms and the subspace table. It answers "what is this algebra as a set of matrices".

The operators article owns the maps: one matrix per side, a pair of matrices for the two-sided operator, the Kronecker display, the pair as a semigroup, the cone of single products with its coefficient matrix, and the length. It answers three questions: which maps of the model come from multiplication, which of those maps are a single product, and how many products a general map needs.

### One Pair or Two

The count is set by the **standing matrix models** of the category, not by the number of bases and not by the number of sizes.

- A basis is a section. The split-complex Peirce basis, the reduced biquaternion idempotent basis and the biquaternion Standard Peirce frame are sections or sibling articles, not new pairs.
- A realification or a complexification of a covered model is a section. The split-complex $4\times4$ and the reduced biquaternion $4\times4$ are sections for this reason.
- A second model counts only when the corpus already develops it as a standing article with its own invariants, and when it is not the realification or the complexification of the first. This is the quaternion case alone.

The table records, for each model, which algebra it represents: the algebra itself, its complexification, or its realification. That column is the guard against duplicating another category's pair.

### The Naming Rule

The title is the model followed by the frame:

$$
\text{\$M_n(\mathbb{F})\$ ⟨frame⟩ Representation}
\qquad\text{and}\qquad
\text{\$M_n(\mathbb{F})\$ ⟨frame⟩ Representation : Operators.}
$$

The qualifier names the **basis**, never the algebra. "Standard Peirce" and "e-basis" already follow this rule; the new ones are "Cayley" for $(1,i)$, "Hyperbolic" for $(1,j)$, "Triangular" for $(1,\varepsilon)$, "Reduced" for the reduced locus, "Defining" for the action on $\mathbb{C}^2$, "Standard" for $M_2(\mathbb{R})$ of the split quaternions, "Regular" for the Cayley matrix in $M_4(\mathbb{R})$, and "Diagonal" for the two blocks in $M_2(\mathbb{H})$.

The slug carries the algebra tag when the model is shared by several categories. The biquaternion slugs need none, because there the model is the algebra. The real models are shared, so they do:

| category | slug prefix |
|---|---|
| complex | `c-` |
| split-complex | `d-` |
| dual | `dual-` |
| duo-complex | `c2-` |
| reduced biquaternion | `rb-` |
| quaternion | `h-` |
| split-quaternion | `hs-` |
| split-biquaternion | `sb-` |

A slug is `<prefix>-<model>-<frame>[-operators].md`, for example `hs-m2r-standard-representation.md` and `hs-m2r-standard-representation-operators.md`.

### What Moves and What Stays

Moves into the pair:

- every article whose title names a **topic of the model**: the regular matrix, the centraliser, the conjugations, the subspaces as matrix conditions, the rank-one strata, the sandwich, the adjoint action, the projective line;
- every article that reads one model and nothing else.

Stays:

- the **abstract** operator articles, which carry no matrix: the one-sided family, the two-sided family, the enveloping algebra, the commutant, the Hermitian sandwich, the pin and spin groups;
- the **module** articles: the two-component column, the four-vector, the spinor and Peirce-coordinate articles, the tensor square;
- the **polar** family, the sectors, the spectral regularity articles;
- everything under Topology, Analysis, Geometry, Fractal Geometry and Applications.

### The Contract

So that the sixteen to eighteen articles are recognisable as one scheme, each general article carries these sections, in this order, and each operators article these:

| general article | operators article |
|---|---|
| Introduction | Introduction |
| The Frame | The One-Sided Operators |
| The Left and the Right Matrices | The Two-Sided Operator |
| The Product | The Cone and the Coefficient Matrix |
| The Trace | The Pair as a Semigroup |
| The Determinant | The Length |
| The Spectral Projectors | The Two Ranks |
| The Adjugate and the Inverse | What the Pair Buys and Does Not |
| The Norms | Summary |
| The Subspaces | Summary of Notation |
| Summary, Summary of Notation, Further Reading | Further Reading |

A section is dropped only when the object does not exist, and the Introduction then says why. **One category inverts the contract**: in the duo-complex category the general article is about the module and not the algebra, so it carries the module contract of that section instead of the left column, and it cites the biquaternion $M_2$ pair for every algebra invariant.

The operators article always carries the three sections of the second layer, *The Cone and the Coefficient Matrix*, *The Length* and *The Two Ranks*, because the cone either is a real cone or has collapsed to a subspace, and the article has to say which.

### The Second Layer: the Cone, the Coefficient Matrix and the Length

One layer is missing from the biquaternion template, and it is the layer the operators article lives on. The template answers "which map is $T_{Q,P}=L_QR_P$". The second layer answers two sharper questions: **which operators are a single product**, and **how many products does a general operator need**. Both have the same answer in all eight categories, and that answer is the spine of every operators article.

#### The Map and the Six Facts

Let $A$ be the carrier, of dimension $n$ over the field $K$, and let

$$
\beta:A\times A\longrightarrow\operatorname{End}_K(A),\qquad \beta(Q,P)=T_{Q,P}=L_QR_P .
$$

1. **The image is a cone.** $\beta$ is bilinear and not linear, so $aT_{Q,P}+bT_{R,S}$ is a product only when the two pairs share a slot. In particular $\lambda T_{Q,P}=T_{\lambda Q,P}=T_{Q,\lambda P}$ for every $\lambda\in K$.
2. **The scaling is free.** $\beta(\lambda Q,\lambda^{-1}P)=\beta(Q,P)$, so the parameter count drops by one; the group $K^{\times}$ acts on $A\times A$ and $\beta$ is constant on each orbit.
3. **The zero set.** $T_{Q,P}=0$ iff $Q=0$ or $P=0$. The zero operator is the vertex of the cone, and it is the image of every degenerate pair.
4. **The fibres.** For a nonzero product and a non-commutative $A$, the fibre is exactly one scaling orbit. For a commutative $A$ the fibre is larger, and this is where the cone collapses.
5. **The dimension.** $\dim(\text{image})=\dim(A\times A)-\dim(\text{fibre})$.
6. **The vertex is not a member of the group.** $T_{Q,P}$ is invertible iff both $Q$ and $P$ are units, so the invertible members form a coset of the scaling orbit and the cone is a cone over a base of dimension one less.

#### The Coefficient Matrix

The products $T_{\mu\nu}=L_{e_\mu}R_{e_\nu}$ over a basis of $A$ are orthogonal for the Hilbert–Schmidt form. They span the image of $\beta$, and they span the ambient space $\operatorname{End}_K(A)$ exactly when the multiplication map $A\otimes_K A^{\mathrm{opp}}\to\operatorname{End}_K(A)$ is onto. That fails for a commutative $A$, where the image is the regular representation, and it fails again for $\mathbb{H}_{\mathbb{D}}=\mathbb{H}\oplus\mathbb{H}$, where the image is the block-diagonal part of $M_8(\mathbb{R})$, of dimension $32$ inside $64$, and no product has a nonzero off-diagonal block. On the span, every operator $M$ has a unique coefficient matrix

$$
c(M)_{\mu\nu}=\tfrac1n\operatorname{Tr}\big(T_{\mu\nu}^{\dagger}M\big),
\qquad
M=\sum_{\mu\nu}c(M)_{\mu\nu}T_{\mu\nu},
\qquad
c(T_{Q,P})=[Q]\,[P]^{\mathsf T}.
$$

The last identity is the whole point. It converts a question about operators into a question about a matrix of numbers:

$$
M \text{ is a single product} \iff \operatorname{rank}c(M)\le1 \iff \text{every }2\times2\text{ minor of }c(M)\text{ vanishes}.
$$

Projectively the cone is the Segre variety $\mathbb{P}^{n-1}\times\mathbb{P}^{n-1}$ inside $\mathbb{P}^{n^2-1}$, the cone of decomposable tensors.

The coefficient matrix is the **realignment** of the operator matrix. The operator matrix of $T_{Q,P}$ is the Kronecker product $\mathsf M(P)^{\mathsf T}\otimes\mathsf M(Q)$, indexed by pairs of matrix indices; $c(M)$ is the same array with its row and column indices regrouped so that one pair runs over the basis of $A$ and the other over the same basis. Under that regrouping a decomposable operator becomes a rank-one array, and the length becomes the **tensor rank** of $M$ as an element of $A\otimes_K A^{\mathrm{opp}}$. This is why the Kronecker display and the coefficient matrix are the same object in two index orders, and why the length theorem is the statement "tensor rank equals the rank of the realignment".

#### The Length

Set

$$
\ell(M)=\min\{r\ge0: M=\textstyle\sum_{i=1}^{r}T_{Q_i,P_i}\},\qquad \ell(0)=0 .
$$

Then

$$
\boxed{\;\ell(M)=\operatorname{rank}c(M)\;}
$$

in both directions: a decomposition into $r$ products makes $c(M)$ a sum of $r$ rank-one matrices, so $\operatorname{rank}c(M)\le r$; and a rank factorisation $c=UV$ with $U$ of size $n\times r$ turns the columns of $U$ into the $[Q_i]$ and the rows of $V$ into the $[P_i]^{\mathsf T}$, so $r=\operatorname{rank}c(M)$ suffices. Hence $\ell\le n$: no operator needs more than $n$ products, and a generic one needs exactly $n$.

#### The Two Ranks

The matrix rank and the coefficient rank are unrelated, and confusing them is the usual error:

$$
\operatorname{rank}T_{Q,P}=\operatorname{rank}\mathsf M(Q)\cdot\operatorname{rank}\mathsf M(P),
\qquad
\ell(T_{Q,P})=1 .
$$

A rank-one matrix can need four products, and a rank-two matrix can be one product. Only $c(M)$ decides. The article must state both ranks in a table, with one example of each discrepancy.

#### Addition Fails

$$
c(T_{Q,P}+T_{R,S})=[Q][P]^{\mathsf T}+[R][S]^{\mathsf T},
$$

generically of rank two, so the sum of two products is not a product. The family is a multiplicative semigroup and not an additive one, and the smallest witness is $T_{tt}+T_{xx}$, of coefficient rank two.

#### The Algebra Carrier and the Module Carrier

The middle slot is where the two carriers part.

| | algebra carrier $A$ | module carrier $V$ |
|---|---|---|
| operator | $T_{Q,P}(X)=QXP$ | $T_{u,\phi}(v)=\phi(v)u=u\phi^{\mathsf T}$ |
| right slot | an element $P\in A$ | a covector $\phi\in V^*$ |
| composition | $T_{Q,P}T_{R,S}=T_{QR,SP}$ | $T_{u,\phi}T_{u',\phi'}=\phi(u')\,T_{u,\phi'}$ |
| middle factor | multiplies | pairs, and its value becomes a scalar |
| identity | $T_{e,e}=\mathrm{id}$ | none: every member is rank one and $\mathrm I$ is not |
| algebraic shape | multiplicative monoid | semigroup with zero |

The module carrier has no $QXP$ to write, because $V$ has no product; the pairing $\phi(u')$ has nowhere to go and is absorbed into the left slot. That is why the cone survives the composition law but loses the identity.

#### The Collapse for a Commutative Algebra

For $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$ and $\mathbb{B}_{\mathrm r}$,

$$
T_{Q,P}(X)=QXP=(QP)X=L_{QP}(X),
$$

so the image is not a cone with a vertex but the linear subspace of the regular representation, of dimension $n$. The fibre over $L_c$ is $\{(Q,P):QP=c\}$, of dimension $n-1$ plus the scaling, larger than one orbit; the parameter count falls from $2n$ to $n$, not to $2n-1$; the membership test is linear, not determinantal; the Segre picture collapses to the graph of the multiplication map; and $\ell\in\{0,1\}$, because every element of the image is already one $L_c$. The second layer therefore reports a negative result in these four categories, and it must report it as a theorem, with the fibre computation as proof.

#### The Master Table

Dimensions over $K$; the ambient is $\operatorname{End}_K(A)$, of dimension $n^2$.

| category | carrier | $K$ | $n$ | ambient | span | cone dim | membership test | identity | $\ell$ | isometries |
|---|---|---|---|---|---|---|---|---|---|---|
| Complex | $\mathbb{C}$ | $\mathbb{R}$ | 2 | 4 | 2 | 2 | linear: conformal | yes | $\{0,1\}$ | dim 1 |
| Split-complex | $\mathbb{D}$ | $\mathbb{R}$ | 2 | 4 | 2 | 2 | linear: symmetric, equal diagonal | yes | $\{0,1\}$ | dim 1 |
| Dual | $\mathbb{D}'$ | $R$ | 2 | 4 | 2 | 2 | linear: parabolic | yes | $\{0,1\}$ | dim 1 |
| Duo-complex | $V=\mathbb{C}^2$ | $\mathbb{C}$ | 2 | 4 | 4 | 3 | $\det M=0$ | no | $\{0,1,2\}$ | none |
| Reduced biquaternion | $\mathbb{B}_{\mathrm r}$ | $\mathbb{R}$ | 4 | 16 | 4 | 4 | linear: the commutant of $\sigma_1$ | yes | $\{0,1\}$ | dim 3 |
| Quaternion, $M_2$ | $\mathbb{H}$ | $\mathbb{R}$ | 4 | 16 | 16 | 7 | $\operatorname{rank}c\le1$ | yes | $\{0,\dots,4\}$ | dim 3 |
| Quaternion, $M_4$ | $\mathbb{H}$ | $\mathbb{R}$ | 4 | 16 | 16 | 7 | $\operatorname{rank}c\le1$ | yes | $\{0,\dots,4\}$ | dim 3 |
| Split-quaternion | $\mathbb{H}_{\mathrm s}$ | $\mathbb{R}$ | 4 | 16 | 16 | 7 | $\operatorname{rank}c\le1$ | yes | $\{0,\dots,4\}$ | dim 3 |
| Split-biquaternion | $\mathbb{H}_{\mathbb{D}}$ | $\mathbb{R}$ | 8 | 64 | 32 | 14 | $\operatorname{rank}c\le1$ blockwise | yes | $\{0,\dots,4\}$ | dim 6 |
| Biquaternion | $\mathbb{B}$ | $\mathbb{C}$ | 4 | 16 | 16 | 7 | $\operatorname{rank}c\le1$ | yes | $\{0,\dots,4\}$ | dim 3 |

The **span** column is the reach: it is $\dim\beta(A\times A)$, and it equals the ambient only for $\mathbb{H}$, $\mathbb{H}_{\mathrm s}$, $\mathbb{B}$ and the module carrier. In the other five the pairs never reach the whole endomorphism space, and in four of those the reason is the same, commutativity.

The split-biquaternion row has cone dimension $14=7+7$ and length at most four, not eight, because the two blocks factorise in parallel: the two factorisations can use the same index. Its fibre is $(\mathbb{R}^{\times})^2$, of dimension two, which is the double scaling $\tilde Q_\pm\mapsto\lambda_\pm\tilde Q_\pm$.

#### What Each Operators Article Does With This

Each operators article carries the second layer in three sections, in this order:

1. **The Cone and the Coefficient Matrix.** The five facts about $\beta$, the fibre computation, the dimension count, the basis $T_{\mu\nu}$, $c(T_{Q,P})=[Q][P]^{\mathsf T}$, and the membership test of that category's row.
2. **The Length.** The definition, the theorem $\ell=\operatorname{rank}c$, the values in that category's range, and the extremal examples.
3. **The Two Ranks.** The matrix rank of a product, the coefficient rank, and a table with one case of each discrepancy.

Two further points belong to specific categories and are named in their sections below: for $\mathbb{C}^2$ the length equals the matrix rank because the operator basis is the matrix-unit basis, and for $\mathbb{H}$ the matrix rank of every nonzero product is four, so the cone minus its vertex lies inside $GL_4(\mathbb{R})$ while the length still reaches four.

### The Table

| # | category | model | represents | new articles | absorbed |
|---|---|---|---|---|---|
| 1 | Complex Numbers | $M_2(\mathbb{R})$ | $\mathbb{C}$ itself | 2 | 1 |
| 2 | Split-Complex Numbers | $M_2(\mathbb{R})$ | $\mathbb{D}$ itself | 2 | 3 |
| 3 | Dual Numbers | $M_2(R)$ | $\mathbb{D}'$ itself | 2 | 1 |
| 4 | Duo-Complex Numbers | $M_2(\mathbb{C})$ | the module $\mathbb{C}^2$ | 2 | 0 |
| 5 | Reduced Biquaternions | $M_2(\mathbb{C})$ | $\mathbb{B}_{\mathrm r}$ itself | 2 | 6 |
| 6 | Quaternions | $M_2(\mathbb{C})_{\mathbb{H}}$ | $\mathbb{H}$ inside $\mathbb{H}_{\mathbb{C}}\cong M_2(\mathbb{C})$ | 2 | 2 |
| 6 | Quaternions | $M_4(\mathbb{R})_{\mathbb{H}_L}$ | $\mathbb{H}$ itself, regular | 2 | 2 |
| 7 | Split-Quaternions | $M_2(\mathbb{R})$ | $\mathbb{H}_{\mathrm s}$ itself | 2 | 8 |
| 8 | Split-Biquaternions | $M_2(\mathbb{H})$ | $\mathbb{H}_{\mathbb{D}}$ itself, diagonal | 2 | 1 |
| — | Biquaternions | $M_2(\mathbb{C})$, $M_4(\mathbb{C})$ | done | 4 done | 24 done |

Eighteen new articles, twenty-four absorbed. The four biquaternion articles already exist and set the template.

---

## 1. Complex Numbers

### The Model

$\mathbb{C}$ is two-dimensional over $\mathbb{R}$. Left multiplication by $Q=q+iq'$ in the basis $(1,i)$ is the Cayley matrix

$$
M_Q=\begin{pmatrix}q&-q'\\ q'&q\end{pmatrix}.
$$

The image is the algebra of conformal matrices, of real dimension two inside the four of $M_2(\mathbb{R})$.

### $M_2(\mathbb{R})$ Cayley Representation

Slug `c-m2r-cayley-representation.md`. Absorbs *Complex Regular Element Representation*.

- **The Frame.** The basis $(1,i)$; the complex structure $J$ with $J^2=-\mathrm I_2$; the matrix units; the one frame, and why a second basis gives the same model by conjugation.
- **The Left and the Right Matrices.** $L_Q=R_Q=M_Q$ on the nose, because the algebra is commutative; the single copy, against the two of the quaternions.
- **The Product.** $M_QM_P=M_{QP}$; the image is closed, two-dimensional and not all of $M_2(\mathbb{R})$; the isomorphism onto $\mathbb{R}\mathrm I_2+\mathbb{R}J$.
- **The Trace.** $\operatorname{tr}M_Q=2q$; the scalar part as $\tfrac12\operatorname{tr}$; the traceless part as $i\mathbb{R}$.
- **The Determinant.** $\det M_Q=q^2+q'^2$, the modulus squared; multiplicativity; the unit criterion $\det\neq0$; the contrast with the indefinite determinant of the split case.
- **The Spectral Projectors.** No real idempotent but $0$ and $1$, because $\mathbb{C}$ is a field; the eigenvalues $\lambda$ and $\bar\lambda$; the diagonalising matrix over $\mathbb{C}$ and the rotation it performs.
- **The Adjugate and the Inverse.** $\operatorname{adj}M_Q=M_{\bar Q}$ and $M_Q^{-1}=M_{\bar Q}/N$; the transpose as the conjugation, $M_Q^{\mathsf T}=M_{\bar Q}$.
- **The Norms.** The trace form, the determinant form, the Frobenius norm and the modulus; which one is the determinant and which one is only positive definite.
- **The Subspaces.** The fixed-point subspaces of the involution group, $\mathbb{C}$ and $\mathbb{R}$, as matrix conditions; the count two against the six of the biquaternion algebra.
- **Summary**, **Summary of Notation**, **Further Reading**.

### $M_2(\mathbb{R})$ Cayley Representation : Operators

Slug `c-m2r-cayley-representation-operators.md`. New.

- **Introduction.** The count of matrices per map; the fact that the two sides coincide here; the collapse of the pairs; boundaries; conventions.
- **The One-Sided Operators.** $L_Q=M_Q$; the kernel and the image; the faithful copy of $\mathbb{C}$ inside $\mathrm{End}_{\mathbb{R}}(\mathbb{C})$.
- **The Two-Sided Operator.** $T_{Q,P}(X)=QXP=M_{QP}(X)$; the pair is not a pair, it is the product; the scaling orbit collapses; four real parameters fall to two.
- **The Kronecker Display.** $B^{\mathsf T}\otimes A$ for the $2\times2$ case; the vectorisation identity; the coefficient matrix $[Q][P]^{\mathsf T}$ of rank one.
- **The Rank and the Invariants.** $\operatorname{rank}T=2$ when $QP\neq0$ and $0$ otherwise; $\operatorname{tr}T=2\operatorname{Re}(QP)$; $\det T=N(QP)$.
- **The Pair as a Semigroup.** Composition; the automorphisms $X\mapsto AXA^{-1}$ are the identity, so the inner automorphism group is trivial; the absence of a matrix-unit system.
- **The Cone and the Coefficient Matrix.** $\beta(Q,P)=L_{QP}$; the image is the two-dimensional subspace of conformal matrices and not a cone, because the fibre over $L_c$ is $\{(Q,P):QP=c\}$, of real dimension two, one scaling orbit times the free $P$; the parameter count falls from four to two; the membership test is the linear condition "conformal", against the determinantal test of the non-commutative categories; the basis is $\{T_{e_t},T_{ie_t}\}$ and $c(T_Q)$ is the single complex number $Q$.
- **The Length.** $\ell\in\{0,1\}$; every nonzero member of the span is already one $L_Q$, so no sum is ever needed and the value $2$ does not occur; the span and the family coincide, which is the degenerate case of the length theorem.
- **The Two Ranks.** $\operatorname{rank}T_Q=2$ for $Q\neq0$ and $0$ at zero, while the coefficient rank is $1$; the two differ at every nonzero member, and the reason is structural: $\mathbb{C}$ is a division algebra, so its left action is by invertible matrices.
- **What the Pair Buys and Does Not.** The pair buys nothing beyond the regular representation, and the article says so; the missing half is the conjugation, which is where the second product of the complexoid block lives.
- **Summary**, **Summary of Notation**, **Further Reading**.

### Matrix Articles Today

| slug | title | fate |
|---|---|---|
| `complex-regular-element-representation` | Complex Regular Element Representation | absorbed into the pair, deleted |
| `complex-element-representations` | Complex Element Representations | kept, retitled *Complex Linear Representations* |
| `complex-two-component-element-representation` | Complex Two-Component Element Representation | kept, the column module |
| `the-matrix-element-representations-of-the-complexoid` | The Matrix Element Representations of the Complexoid | kept, cited by the pair |

### Menu Surgery

In **Algebra**, after the spectral subsection, add `#### Matrix Representations` with the two links. Delete the *Complex Regular Element Representation* link from `#### Element Representations`.

### What Stays

*Complex Element Representations* stays, retitled, because its subject is Schur's lemma and the representation ring, which is the other meaning of the word. *Complex Two-Component Element Representation* stays as the column module.

---

## 2. Split-Complex Numbers

### The Model

$\mathbb{D}$ is two-dimensional over $\mathbb{R}$ with $j^2=+1$. Left multiplication by $Q=q+jq'$ in the basis $(1,j)$ is

$$
M_Q=\begin{pmatrix}q&q'\\ q'&q\end{pmatrix}.
$$

The Peirce basis $(\Pi_+,\Pi_-)$ with $\Pi_\pm=\tfrac12(1\pm j)$ turns it into $\operatorname{diag}(q+q',q-q')$. Same size, so one model. The $4\times4$ of the eigenbasis article is the regular representation of $\mathbb{D}_{\mathbb{C}}\cong\mathbb{C}\times\mathbb{C}$, which is the reduced biquaternion algebra; it is a section.

### $M_2(\mathbb{R})$ Hyperbolic Representation

Slug `d-m2r-hyperbolic-representation.md`. Absorbs *Split-Complex Regular Element Representation*, *Eigenbasis of a Split-Complex Number in Matrix Elements Representations*.

- **The Frame.** The basis $(1,j)$; the hyperbolic unit $K$ with $K^2=+\mathrm I_2$; the two null directions; the Peirce frame and the congruence that reaches it; the complexified $4\times4$ model as a closing subsection.
- **The Left and the Right Matrices.** $L_Q=R_Q$, the algebra being commutative; the one copy; the conjugation as the transpose.
- **The Product.** $M_QM_P=M_{QP}$; the image of dimension two; the two idempotent images $M_{\Pi_\pm}$.
- **The Trace.** $2q$; the scalar part.
- **The Determinant.** $q^2-q'^2$, the split norm, indefinite; $\det=0$ exactly on the two null lines, which are the zero divisors; the rank drop; the contrast with the definite complex case.
- **The Spectral Projectors.** The two real idempotents $\Pi_\pm$; the diagonalising matrix; the degenerate case of a zero divisor, where the two projectors coalesce and the matrix is not diagonalisable.
- **The Adjugate and the Inverse.** $\operatorname{adj}M_Q=M_{\bar Q}$; the inverse on $\{N\neq0\}$; the four components of the group of units.
- **The Norms.** The split norm and the Euclidean trace form; the two metrics of the plane, which is where the sign of the form changes sides against the complex case.
- **The Subspaces.** The null lines, the fixed-point subspaces of identity and conjugation, the two idempotent lines, as matrix conditions.
- **Summary**, **Summary of Notation**, **Further Reading**.

### $M_2(\mathbb{R})$ Hyperbolic Representation : Operators

Slug `d-m2r-hyperbolic-representation-operators.md`. Absorbs *Operator and the Polar Decomposition of a Split-Complex Number*.

- **Introduction.** One matrix per side, the sides coincide, the pair collapses, and the polar word reads as a one-parameter subgroup.
- **The One-Sided Operators.** $M_Q$ as the faithful copy; the boost $M_Q=rM_\epsilon\exp(\phi K)$; the two eigenvalues $e^{\pm\phi}$ as the scales of the two Peirce lines.
- **The Two-Sided Operator.** $T_{Q,P}=M_{QP}$; the sandwich $\Theta_Q(X)=QX\bar Q=N(Q)X$, a scalar; the image the ray of the identity; the kernel of $Q\mapsto\Theta_Q$ is $\{N=1\}$.
- **The Kronecker Display.** $B^{\mathsf T}\otimes A$; the coefficient matrix; the collapse to rank one.
- **The Rank and the Invariants.** The rank in $\{0,1,2\}$: two on the units, one exactly on the two null lines, zero at the origin; the zero-divisor case in full.
- **The Pair as a Semigroup.** Composition; the trivial inner automorphism group; the absence of a half-angle and of a spin double cover.
- **The Cone and the Coefficient Matrix.** $\beta(Q,P)=L_{QP}$; the image is the two-dimensional subspace of hyperbolic matrices $\begin{pmatrix}q&q'\\q'&q\end{pmatrix}$, not a cone; the fibre over $L_c$ is $\{(Q,P):QP=c\}$, of real dimension two; the membership test is the pair of linear conditions "symmetric with equal diagonal", against the determinantal test of the non-commutative categories.
- **The Length.** $\ell\in\{0,1\}$; every element of $\mathbb{D}$ is one $L_Q$; the null lines of the algebra are not a failure of the length, because a zero divisor is still a single product.
- **The Two Ranks.** $\operatorname{rank}T_Q\in\{0,1,2\}$, the value $1$ exactly on the zero divisors, while the coefficient rank is $1$ on all of them; the singular members are single products of rank one, which separates this case from the matrix algebras where a rank-one operator can need four products.
- **What the Pair Buys and Does Not.** The indefinite form makes the sandwich a scalar, so the two-sided family carries no group action, against $\mathbb{B}$ where it carries $CO^{+}(1,3)$.
- **Summary**, **Summary of Notation**, **Further Reading**.

### Matrix Articles Today

| slug | title | fate |
|---|---|---|
| `split-complex-regular-element-representation` | Split-Complex Regular Element Representation | absorbed, deleted |
| `eigenbasis-of-a-split-complex-number-in-matrix-elements-representations` | Eigenbasis of a Split-Complex Number in Matrix Elements Representations | absorbed, deleted |
| `operator-and-the-polar-decomposition-of-a-split-complex-number` | Operator and the Polar Decomposition of a Split-Complex Number | absorbed into the operators article, deleted |
| `split-complex-element-representations` | Split-Complex Element Representations | kept, retitled *Split-Complex Linear Representations* |
| `split-complex-two-component-element-representation` | Split-Complex Two-Component Element Representation | kept |
| `the-matrix-element-representations-of-the-split-complexoid` | The Matrix Element Representations of the Split-Complexoid | kept, cited by the pair |

### Menu Surgery

In **Algebra**, add `#### Matrix Representations` with the two links. The three absorbed links sit in three places: *Split-Complex Regular Element Representation* under `#### Element Representations`, the eigenbasis article under `#### Spectral Algebra with the Split Norm`, and the polar-operator article under `#### Operators Representations` in **Analysis**. Delete `#### Operators Representations` from **Analysis** and keep its polar content under Analysis, with the operator half moved up to Algebra.

### What Stays

The two-component column, the polar family, the four sectors, the abstract eigenbasis article and the separate *Worked Examples of Eigenbasis of a Split-Complex Number* stay. Only the eigenbasis article **in matrix elements** is absorbed, and its worked examples move into the general article.

---

## 3. Dual Numbers

### The Model

$\mathbb{D}'=R[\varepsilon]/(\varepsilon^2)$ over a commutative ring $R$ in which $2$ is invertible. Left multiplication by $Q=q+\varepsilon q'$ in the basis $(1,\varepsilon)$ is

$$
M_Q=\begin{pmatrix}q&q'\\ 0&q\end{pmatrix}.
$$

The model is triangular. It is the only model of the eight that is not semisimple.

### $M_2(R)$ Triangular Representation

Slug `dual-m2r-triangular-representation.md`. Absorbs *Dual-Numbers Matrix Element Representation*.

- **The Frame.** The basis $(1,\varepsilon)$; the nilpotent unit $N$ with $N^2=0$; the maximal ideal as the strictly upper corner.
- **The Left and the Right Matrices.** $L_Q=R_Q$; the one copy; the transpose leaves the image, because the lower corner is filled.
- **The Product.** $M_QM_P=M_{QP}$; the image is the parabolic subalgebra of dimension two; the flag it fixes.
- **The Trace.** $2q$; the trace detects only the constant term.
- **The Determinant.** $q^2$, independent of $q'$; $\det=0$ exactly on the maximal ideal; the rank ladder $0,1,2$; the determinant cannot see the nilpotent direction.
- **The Spectral Projectors.** Only $0$ and $1$; no nontrivial idempotent; the double eigenvalue $q$; the matrix is diagonalisable only when it is scalar; the Jordan form $q\mathrm I+q'N$.
- **The Adjugate and the Inverse.** The adjugate $\begin{pmatrix}q&-q'\\0&q\end{pmatrix}$; the inverse $\begin{pmatrix}1/q&-q'/q^2\\0&1/q\end{pmatrix}$ on $q\neq0$; the shear it produces.
- **The Norms.** The determinant form $q^2$; the algebraic norm $Q^2$, which is algebra-valued and not a real norm; the criterion of invertibility $q\neq0$; the defect.
- **The Subspaces.** The constants, the maximal ideal, the fixed-point subspaces of the two involutions, as matrix conditions.
- **Summary**, **Summary of Notation**, **Further Reading**.

### $M_2(R)$ Triangular Representation : Operators

Slug `dual-m2r-triangular-representation-operators.md`. New.

- **Introduction.** The count, the collapse of the pair, and the nilpotent operator the model produces.
- **The One-Sided Operators.** $M_Q=q\mathrm I+q'N$; the one-parameter shear $\exp(tN)$; the logarithm reading.
- **The Two-Sided Operator.** $T_{Q,P}=M_{QP}$; the sandwich $QX\bar Q=N(Q)X=q^{2}X$, a scalar, where $N(Q)=q^{2}$ is not $Q^{2}=q^{2}+2qq'\varepsilon$; the image is the ray of the identity; the kernel of $Q\mapsto\Theta_Q$ is $\{q=\pm1\}$, of real dimension one and two components, against the connected $\{N=1\}$ of the split-complex case.
- **The Kronecker Display.** $B^{\mathsf T}\otimes A$; the coefficient matrix; the rank one.
- **The Rank and the Invariants.** The rank in $\{0,1,2\}$; the two-sided rank two exactly when $QP\notin(\varepsilon)$.
- **The Pair as a Semigroup.** Composition; the trivial inner automorphism group; the gauge $q\mapsto q+\varepsilon q'$ as a shear of the model.
- **The Cone and the Coefficient Matrix.** $\beta(Q,P)=L_{QP}$; the image is the two-dimensional parabolic subspace $\begin{pmatrix}q&q'\\0&q\end{pmatrix}$; the fibre has dimension two; the membership test is the single linear condition on the lower-left entry; the basis is $\{T_1,T_\varepsilon\}$ and $c(T_Q)=(q,q')$.
- **The Length.** $\ell\in\{0,1\}$; the nilpotent direction is one product, not two, so the degeneracy of the algebra does not lengthen anything.
- **The Two Ranks.** $\operatorname{rank}T_Q\in\{0,1,2\}$, the value $1$ exactly on the maximal ideal, while the coefficient rank is $1$ throughout; the determinant and the length are blind to the nilpotent direction in the same way, and the rank is the only invariant that sees it.
- **What the Pair Buys and Does Not.** The article says which invariant detects the nilpotent direction, since the determinant does not.
- **Summary**, **Summary of Notation**, **Further Reading**.

### Matrix Articles Today

| slug | title | fate |
|---|---|---|
| `dual-numbers-matrix-element-representation` | Dual-Numbers Matrix Element Representation | absorbed, deleted |
| `dual-numbers-element-representations` | Dual-Numbers Element Representations | kept, retitled *Dual-Numbers Linear Representations* |

### Menu Surgery

In **Algebra**, add `#### Matrix Representations` with the two links after `#### Element Representations`, from which the absorbed *Dual Numbers Matrix Element Representation* link is removed. The dual category has no `#### Operators` subsection today, so the operators article is its first entry there, under **Algebra** and not under **Analysis**.

### What Stays

The degenerate sector, the norm and invertibility, the shears and the projective geometry stay.

---

## 4. Duo-Complex Numbers

### The Model

This category is not an algebra but the space $\mathbb{C}^2$. Its model is $M_2(\mathbb{C})$ acting on the column, and that is the defining module of the biquaternion algebra.

**The $M_2(\mathbb{C})$ collision.** This is the only category whose matrix model is an algebra another category already owns. The name matters, because the collision is at the level of the **model**, not of the **subject**: what the two categories share is the algebra $M_2(\mathbb{C})$, not the space $\mathbb{C}^2$. Calling it "the $\mathbb{C}^2$ duplication", as the first draft did, was wrong on both words: $\mathbb{C}^2$ is shared with nothing, and nothing is duplicated if the split below is made.

The ledger, side by side:

| | biquaternion $M_2(\mathbb{C})$ pair | duo-complex $M_2(\mathbb{C})$ pair |
|---|---|---|
| subject | the algebra $\mathbb{B}\cong M_2(\mathbb{C})$ as a set of matrices | the module $\mathbb{C}^2$, and $M_2(\mathbb{C})$ as the algebra of its endomorphisms |
| objects | frame, product, trace, determinant, projectors, adjugate, norms, subspaces **of the algebra** | the column, the real structure $J$, the forms $h$ and $\omega$, the lines, the flags, the spinor |
| spectral theory | of an element $Q$ | of an operator $A$ acting on the module |
| the numbers | $Q_t,Q_x,Q_y,Q_z$, the norm $\langle Q\rangle_{\#}$ | the components of a spinor, the light cone, the Bloch vector |
| group | the units of the algebra | $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$, $SU(2)$ acting on the space |

After the split the two pairs share **no section and no object**: one is the algebra, the other is the space it acts on. The collision was never in the content, it was in the template. The contract of the general article is an algebra contract, and copying it here is what produced the duplication.

**Why this category cannot be dropped.** $\mathbb{C}^2$ is the spinor space. `physics.md` carries $86$ spinor links, $23$ of them Weyl, and $19$ qubit links with five mentions of the Bloch sphere, while the mathematics corpus carries no qubit, no Bloch-vector and no light-cone article at all: the physics side is already written against a space the mathematics side never introduces. Three readings sit on the same carrier and use the same matrices:

- **The Lorentz spinor.** $SL_2(\mathbb{C})$ is the double cover of $SO^{+}(3,1)$, and its defining action on $\mathbb{C}^2$ is the Weyl spinor, of type $(\tfrac12,0)$, with the conjugate module $\bar{\mathbb{C}}^2$ of type $(0,\tfrac12)$. The vector is recovered from the spinor by $v\mapsto vv^{\dagger}$, a **Hermitian** rank-one matrix: $\det(vv^{\dagger})=0$ and $\operatorname{tr}(vv^{\dagger})=\lVert v\rVert^{2}$, so the four Pauli coefficients $\tfrac12\operatorname{tr}(\sigma_{\mu}vv^{\dagger})$ satisfy $t^{2}-x^{2}-y^{2}-z^{2}=0$, so the Hermitian rank-one cone **is** the future light cone, read as a \(2\times2\) Hermitian matrix through the Pauli basis.
- **The qubit.** The same $\mathbb{C}^2$ with the definite Hermitian form and $SU(2)$ acting: the pure states are the points of $\mathbb{P}^1$, which is the Bloch sphere, and the Bloch vector is $\langle\sigma\rangle\in\mathbb{R}^{3}$, of length one exactly on the pure states. The projectors $vv^{\dagger}/\lVert v\rVert^{2}$ are again rank one and Hermitian, so the same equation serves both readings.
- **The null flag.** A spinor modulo phase is a point of $\mathbb{P}^1$, that is a null direction; the residual phase is the rotation of the flag half-plane. The Hopf fibration $S^{3}\to S^{2}$ is this quotient, and the corpus already carries it under *The Unit Sphere and the Hopf Fibration*.

The two physics readings differ only by **which form is used on the same carrier**: the definite Hermitian $h$ for the qubit, the complex bilinear $\omega$ and the real structure $J$ for the Lorentz spinor. That is exactly the three-form theme the category already carries, and it is why the forms, and not the matrices, are the subject here.

**Consequence for the operators article.** Two rank-one cones live in $M_2(\mathbb{C})$, and both belong to this pair:

$$
\text{bilinear: } T_{u,\phi}=u\phi^{\mathsf T},\ \det=0,\ \dim_{\mathbb{C}}=3
\qquad
\text{Hermitian: } uu^{\dagger},\ \det=0,\ \dim_{\mathbb{R}}=3 .
$$

The first is the Segre cone $\mathbb{P}^1\times\mathbb{P}^1$ of the operators article. The second is the light cone, and its projectivisation is a single $\mathbb{P}^1$ and not a product, because $u$ and $u e^{i\theta}$ give the same projector: the phase is quotiented, the two rulings collapse to one. The conjugate-linear half, which the commutative categories name as what is missing, is precisely what produces the second cone here, and it is the reason this article is the one place where the two cones must be compared side by side.

### $M_2(\mathbb{C})$ Defining Representation

Slug `c2-m2c-defining-representation.md`. Absorbs nothing. **This general article does not follow the algebra contract.** It carries the module contract below, because the algebra invariants are not its subject.

Three articles already own pieces of the module, and this one cites them instead of repeating them: *The Endomorphisms of $\mathbb{C}^2$* owns the action, the conjugate-linear maps, the centraliser and double centraliser of $J$, $GL_2$ and $PGL_2$; the biquaternion $M_2(\mathbb{C})$ pair owns the frame, the product, the trace, the determinant, the projectors, the adjugate and the norms of the algebra; *The Subspaces of $\mathbb{C}^2$* owns the lattice. What is left, and what is new, is the module read through its three structures and the readings they produce.

- **Introduction.** The collision and the division of labour, in the three lines above. What the pair adds: the two cones, the spinor, the qubit, the flag. Boundaries; the three structures named once and used throughout.
- **The Column, the Dual and the Three Structures.** The basis $(e_1,e_2)$ and the column; the dual $V^{*}$ and the row; the real structure $J$ with $J^{2}=-\mathrm I_4$ on the realification; the antisymmetric bilinear form $\omega(u,v)=u^{\mathsf T}Jv$; the Hermitian form $h(u,v)=u^{\dagger}v$; the real dimension four and the complex dimension two; which reading uses which structure, and the fact that the two physics readings differ **only** by the choice of form.
- **The Lines, the Flags and the Projective Line.** The lines of $V$; a line is a rank-one projector; the flag $0\subset\ell\subset V$ and its half-plane; $\mathbb{P}^{1}$ as the space of lines; the dual line and the incidence; the two rulings of the Segre quadric as pairs $(\ell,\ell')$ of one line and one dual line, with the citation to *The Subspaces of $\mathbb{C}^2$* for the lattice.
- **The Bilinear Cone and the Segre Quadric.** $\omega$ and the isotropic lines, which are the two rulings; the quadric $\{u^{\mathsf T}Ju=0\}$; the identification of a rank-one **bilinear** operator $u\phi^{\mathsf T}$ with a pair (column, row); the projectivisation $\mathbb{P}^{1}\times\mathbb{P}^{1}$; the citation to the operators article for the cone as a set of operators.
- **The Hermitian Cone and the Light Cone.** $h$; the **Hermitian** rank-one matrices $uu^{\dagger}$, with $\det(uu^{\dagger})=0$ and $\operatorname{tr}(uu^{\dagger})=\lVert u\rVert^{2}$ (both checked symbolically, the second with the factor $2$ on the right and not on the left); the Pauli basis $\sigma_0,\sigma_1,\sigma_2,\sigma_3$, the coefficient vector $x^{\mu}=\tfrac12\operatorname{tr}(\sigma_{\mu}uu^{\dagger})$, and the identity $t^{2}-x^{2}-y^{2}-z^{2}=\det(uu^{\dagger})=0$; the future cone for a definite $h$ and the full null cone for an indefinite one; the real dimension three; why this cone is not the Segre cone of the previous section, the phase being quotiented here and not there.
- **The Spinor and the Two Actions.** $SL_2(\mathbb{C})$ as the double cover of $SO^{+}(3,1)$, of kernel $\{\pm\mathrm I\}$; the defining module as the Weyl spinor of type $(\tfrac12,0)$ and the conjugate module $\bar V$ of type $(0,\tfrac12)$; self-duality through $\omega$, so the dual module is the module; the reason a spinor is not a pair of independent scalars but a pair of **conjugate** scalars, which is exactly the difference from the algebra $\mathbb{C}\times\mathbb{C}$; the vector recovered as $uu^{\dagger}$, hence the map spinor $\to$ null vector, of degree two.
- **The Qubit and the Bloch Vector.** The definite $h$ and $SU(2)$; the pure states as the rank-one projectors $uu^{\dagger}/\lVert u\rVert^{2}$; $\mathbb{P}^{1}$ as the Bloch sphere; $\langle\sigma\rangle\in\mathbb{R}^{3}$ and its length, one exactly on the pure states; the mixed states as the interior of the ball and the trace-one condition as the affine chart; the comparison with the spinor reading, which is the same carrier with a different form.
- **The Phase, the Hopf Fibration and the Flag.** $S^{3}\to S^{2}$ as the quotient of the normalized spinors by the phase; the phase as the rotation of the flag half-plane; the effect on the two cones: the bilinear one keeps both rulings, the Hermitian one collapses them to a single $\mathbb{P}^{1}$, and that collapse is the phase quotient written geometrically.
- **Summary**, **Summary of Notation**, **Further Reading**.

### $M_2(\mathbb{C})$ Defining Representation : Operators

Slug `c2-m2c-defining-representation-operators.md`. New. This is the case where the carrier is a **module** and not an algebra, and the whole article turns on that difference.

- **Introduction.** The carrier is $V=\mathbb{C}^2$, of complex dimension two, and it is not an algebra; there is no $QXP$ to write, and the right slot has to be a covector. The result in one line: every two-sided operator is the rank-one map $T_{u,\phi}(v)=\phi(v)u=u\phi^{\mathsf T}$, that is, a point of the three-dimensional determinantal cone $\{\det=0\}$ in $M_2(\mathbb{C})=\mathbb{C}^4$; composition is closed with the scalar absorbed; there is no identity, no inverse, no isometry and no nonzero skew-adjoint member; the length equals the matrix rank and is at most two. Boundaries; the three notation systems of the article.
- **The One-Sided Operators.** Left multiplication by $A$ is the action $v\mapsto Av$, one matrix in $M_2(\mathbb{C})$; the right slot is the dual, $\phi\in V^{*}$ with $\phi(v)=\phi^{\mathsf T}v$; the identification of the two through the standard basis; why the right slot cannot be a second matrix acting on $V$.
- **The Two-Sided Operator.** $T_{u,\phi}=u\phi^{\mathsf T}$; the bilinearity, hence a cone and not a subspace; the scaling invariance $T_{\lambda u,\lambda^{-1}\phi}=T_{u,\phi}$; the zero set $u=0$ or $\phi=0$; injectivity in each slot with the other nonzero; the fibres are single scaling orbits; the dimension count $4-1=3$.
- **The Cone and the Coefficient Matrix.** The ambient basis $E_{ij}=e_ie_j^{\mathsf T}$, so $c(M)=M$ and $c(T_{u,\phi})=u\phi^{\mathsf T}$; the criterion $M=T_{u,\phi}$ iff $\operatorname{rank}M\le1$ iff $\det M=0$; the projective picture $\mathbb{P}^1\times\mathbb{P}^1$ inside $\mathbb{P}^3$; the cone is the determinantal quadric, of complex dimension three.
- **The Hermitian Cone and the Light Cone.** The second rank-one cone in the same space: $uu^{\dagger}$, Hermitian, with $\det=0$; its projectivisation is a single $\mathbb{P}^{1}$ and not a product, because $u$ and $ue^{i\theta}$ give the same matrix, so the phase quotient collapses the two rulings of the Segre cone to one; the Pauli reading of $uu^{\dagger}$ as a future null $4$-vector, hence the light cone of the Lorentz group; the two cones side by side, bilinear against Hermitian, $\mathbb{P}^{1}\times\mathbb{P}^{1}$ against $\mathbb{P}^{1}$, both of complex or real dimension three; the conjugating adjoint $T\mapsto (T^{\dagger})$ as the map that carries one family to the other through rank one.
- **The Composition.** $T_{u,\phi}T_{u',\phi'}=\phi(u')\,T_{u,\phi'}$: the scalar $\phi(u')$ is absorbed into the left slot and the cone stays closed; the powers $(T_{u,\phi})^n=\phi(u)^{n-1}T_{u,\phi}$; nilpotent when $\phi(u)=0$, idempotent when $\phi(u)=1$; $\operatorname{tr}T_{u,\phi}=\phi(u)$ and $\det T_{u,\phi}=0$; hence a semigroup with zero, and not a monoid, because $\mathrm I_2$ has determinant one. The biquaternion family differs at exactly this point: it contains $T_{e_t,e_t}$.
- **The Length.** $\ell(M)=\min\{r:M=\sum_{i\le r}T_{u_i,\phi_i}\}$; $\ell(M)=\operatorname{rank}M$; the values $\{0,1,2\}$; $\ell=1$ iff $\det M=0$ and $\ell=2$ for the generic matrix; the extremal cases, including the identity at length two.
- **The Two Ranks.** The operator basis here is the matrix-unit basis, so the coefficient matrix is the matrix and the two ranks coincide; the contrast with the algebra carrier, where the operator basis is $\{T_{\mu\nu}\}$ and the two ranks separate; the table of the biquaternion note transposed to this case.
- **The Adjoints and the Types.** With $\langle X,Y\rangle=\operatorname{Tr}(X^{\mathsf T}Y)$, the adjoint is $(T_{u,\phi})^{*}=T_{\phi^{\#},u^{\#}}$, in coordinates $(uv^{\mathsf T})^{*}=vu^{\mathsf T}$; self-adjoint iff $uv^{\mathsf T}=vu^{\mathsf T}$ iff $u$ and $v$ are proportional, so the self-adjoint cone is the symmetric rank-one family; the skew-adjoint sector is $\{0\}$; the conjugate-linear adjoint fixes exactly the Hermitian cone $uu^{\dagger}$, which is the second cone of the previous section and not the bilinear one; no nonzero product is an isometry, because $(T_{u,v})^{*}T_{u,v}=(u^{\mathsf T}u)vv^{\mathsf T}$ has rank at most one while $\mathrm I_2$ has rank two.
- **The Carrier with an Algebra Structure.** The two products on $\mathbb{C}^2$ and what each gives: pointwise $\mathbb{C}\times\mathbb{C}$ gives $T=\operatorname{diag}(ac,bd)$, a two-dimensional subspace of diagonal matrices; the dual numbers give $T=\begin{pmatrix}ac&ad\\bc&ad+bc\end{pmatrix}$, a three-dimensional subspace $\{w=y+z\}$. In both readings the image is a subspace and the Segre structure is lost, so the module reading is the one that preserves the cone, and the article takes it and says why.
- **What the Pair Buys and Does Not.** What it buys: the parametrisation by $V\times V^{*}$ modulo scaling, the single quadratic criterion, the length formula, the adjoint theory. What it does not: identity, inverses, isometries, additivity, and any reach beyond the cone without a sum. The eight-row comparison table against the biquaternion case.
- **Summary**, **Summary of Notation**, **Further Reading**.

### Matrix Articles Today

| slug | title | fate |
|---|---|---|
| `the-endomorphisms-of-the-duo-complex-numbers` | The Endomorphisms of $\mathbb{C}^2$ | kept, cited by the pair; it is the algebra $M_2(\mathbb{C})$, owned by the biquaternion category |
| `the-subspaces-of-the-duo-complex-numbers` | The Subspaces of $\mathbb{C}^2$ | kept, the lattice article |
| `the-tensor-square-of-the-duo-complex-numbers` | The Tensor Square of $\mathbb{C}^2$ | kept |

The category has no matrix article to delete today; the pair is new material.

### Menu Surgery

In **Algebra**, keep `#### Linear Maps and the Endomorphism Algebra` with its two links, and add a sibling `#### Matrix Representations` with the two new links.

### What Stays

*The Tensor Square*, *The Subspaces*, *The Realification*, *The Three Canonical Forms* and the whole Topology, Analysis and Geometry blocks stay.

---

## 5. Reduced Biquaternions

### The Model

$\mathbb{B}_{\mathrm r}=\mathbb{C}[j]/(j^2-1)$, with basis $1,j$ over $\mathbb{C}$ and $j$ central, so $\mathbb{B}_{\mathrm r}\cong\mathbb{C}\times\mathbb{C}$ and the algebra is commutative and semisimple. Write $Q=Q_\blacktriangle+jQ_\blacktriangledown$ with the two entries in $\mathbb{C}$. Left multiplication on the complex two-dimensional space with basis $(1,j)$ is

$$
M_Q=\begin{pmatrix}Q_\blacktriangle&Q_\blacktriangledown\\ Q_\blacktriangledown&Q_\blacktriangle\end{pmatrix}.
$$

The idempotents are $\Pi_\pm=\tfrac12(1\pm j)$, and in their basis the matrix is $\operatorname{diag}(Q_+,Q_-)$ with $Q_\pm=Q_\blacktriangle\pm Q_\blacktriangledown$. One model with two frames, so one pair: the general article carries both frames and the operators article carries the family. The real $4\times4$ is the realification and stays a section, not a second pair.

### $M_2(\mathbb{C})$ Reduced Representation

Slug `rb-m2c-reduced-representation.md`. Absorbs *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions*, *The Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions*, *Eigenbasis of a Reduced Biquaternion in Matrix Elements Representations*.

- **The Frame.** The basis $(1,j)$ over $\mathbb{C}$; the real basis of four; the idempotent frame $(\Pi_+,\Pi_-)$ with $\Pi_\pm=\tfrac12(1\pm j)$; the congruence $P=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ that switches them, of determinant $-2$; the real $4\times4$ model as a closing subsection.
- **The Left and the Right Matrices.** $L_Q=R_Q$, the algebra being commutative; the one copy; the conjugation as the block swap composed with the entry conjugations.
- **The Product.** $M_QM_P=M_{QP}$ in the block form $(Q,U)(R,S)=(QR+US,QS+UR)$; the image is four-real-dimensional inside the eight of $M_2(\mathbb{C})$ read over $\mathbb{R}$; the image is the commutant of $\sigma_1$.
- **The Trace.** $2Q_\blacktriangle$ in the complex model and $4q_\blacktriangle$ in the real $4\times4$ one; the scalar part; why the two differ by the realification.
- **The Determinant.** $Q_\blacktriangle^2-Q_\blacktriangledown^2=Q_+Q_-$, the reduced norm, and $|Q_+Q_-|^2$ in the real $4\times4$ model; $\det=0$ exactly on the zero divisors, which are the elements with exactly one vanishing component.
- **The Spectral Projectors.** The two central idempotents; the diagonalising matrix $P$; the zero-divisor case, where one component vanishes and the rank drops to one.
- **The Adjugate and the Inverse.** The adjugate $\begin{pmatrix}Q_\blacktriangle&-Q_\blacktriangledown\\-Q_\blacktriangledown&Q_\blacktriangle\end{pmatrix}$; the inverse on the complement of the zero-divisor cone; the unit criterion $Q_+\neq0$ and $Q_-\neq0$.
- **The Norms.** The reduced norm as the determinant; the four products and the four algebraic norms; the coordinatewise order and the non-negative cone.
- **The Subspaces.** The centre, the two complex lines, the remarkable subspaces, as block conditions; the two involutions and their fixed points.
- **Summary**, **Summary of Notation**, **Further Reading**.

### $M_2(\mathbb{C})$ Reduced Representation : Operators

Slug `rb-m2c-reduced-representation-operators.md`. Absorbs *The Multiplication Operators of the Algebra of the Reduced Biquaternions*, *Operators on the Reduced Biquaternions*, *Operator and the Polar Decomposition of a Reduced Biquaternion*.

- **Introduction.** The count; the commutative collapse; the doubled boost and the cancelled phases that the model shows.
- **The One-Sided Operators.** $M_{\breve Q}$; the faithful copy; the polar word $\breve Q=\rho e^{\phi j}e^{i\alpha}e^{ij\beta}$ read as one matrix, with the full boost $\phi$ and no half-angle.
- **The Two-Sided Operator.** $\Theta_{\breve Q}(\breve X)=\breve Q\breve X\bar{\breve Q}=\operatorname{diag}(\lvert Q_+\rvert^{2},\lvert Q_-\rvert^{2})\breve X$ in the idempotent basis, which is a scalar only when the two components have equal modulus; the image the positive quadrant, which is the cone; the kernel the torus $T^2=\{Q:\lvert Q_+\rvert=\lvert Q_-\rvert=1\}$ as the kernel of $\breve Q\mapsto\Theta_{\breve Q}$; the plain sandwich $\breve Q\breve X\breve Q=L_{\breve Q^{2}}$, which is the corpus convention and is kept for the plain product; the two involutions and their two sandwiches.
- **The Kronecker Display.** $B^{\mathsf T}\otimes A$ with the block entries; the coefficient matrix; the rank one.
- **The Rank and the Invariants.** The rank in $\{0,1,2\}$ over $\mathbb{C}$ and in $\{0,2,4\}$ in the realification; the determinant and the trace.
- **The Pair as a Semigroup.** Composition; the trivial inner automorphism group; the gauge.
- **The Cone and the Coefficient Matrix.** $\beta(Q,P)=L_{QP}$; the image is the four-real-dimensional subspace which is the commutant of $\sigma_1$, not a cone; the parameter space has real dimension eight and the fibre four, so the count falls from eight to four and not to seven; the membership test is the linear block-symmetric form $\begin{pmatrix}A&B\\B&A\end{pmatrix}$, against the determinantal test of the quaternions.
- **The Length.** $\ell\in\{0,1\}$; every reduced biquaternion is one $L_{\breve Q}$, including the zero divisors, so the two-component structure costs no length.
- **The Two Ranks.** Over $\mathbb{R}$ the matrix rank is in $\{0,2,4\}$ and the coefficient rank is in $\{0,1\}$; over $\mathbb{C}$ the matrix rank is in $\{0,1,2\}$; the passage between the two columns is the realification of *The Four-Vector Element Representation*, and it is the only category where the same element carries two different matrix ranks in two models of the same family.
- **What the Pair Buys and Does Not.** The reduced case sits between the complex and the quaternionic ones: it has an idempotent frame and a matrix model, and no spin.
- **Summary**, **Summary of Notation**, **Further Reading**.

### Matrix Articles Today

| slug | title | fate |
|---|---|---|
| `introduction-to-the-2x2-matrix-element-representation-of-reduced-biquaternions` | Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions | absorbed, deleted |
| `the-general-plain-algebra-in-the-2x2-matrix-element-representation-of-the-reduced-biquaternions` | The Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions | absorbed, deleted |
| `eigenbasis-of-a-reduced-biquaternion-in-matrix-elements-representations` | Eigenbasis of a Reduced Biquaternion in Matrix Elements Representations | absorbed, deleted |
| `the-multiplication-operators-of-the-general-plain-algebra-of-the-reduced-biquaternions` | The Multiplication Operators of the Algebra of the Reduced Biquaternions | absorbed into the operators article, deleted |
| `operators-on-the-reduced-biquaternions` | Operators on the Reduced Biquaternions | absorbed into the operators article, deleted |
| `operator-and-the-polar-decomposition-of-a-reduced-biquaternion` | Operator and the Polar Decomposition of a Reduced Biquaternion | absorbed into the operators article, deleted |
| `introduction-to-reduced-biquaternion-element-representations` | Introduction to Reduced Biquaternion Element Representations | kept, retitled *Introduction to Reduced Biquaternion Linear Representations* |
| `the-four-vector-element-representation-of-the-reduced-biquaternions` | The Four-Vector Element Representation of the Reduced Biquaternions | kept |
| `reduced-biquaternion-other-algebraic-element-representations` | Reduced Biquaternion Other Algebraic Element Representations | kept |
| `reduced-biquaternion-objects-and-their-matrix-correspondences` | Reduced Biquaternion Objects and their Matrix Correspondences | kept, the catalogue |
| `matrix-equations-and-structured-solutions-over-the-reduced-biquaternions` | Matrix Equations and Structured Solutions over the Reduced Biquaternions | kept, applications |
| `hermitian-solutions-of-the-pair-matrix-equation-over-the-reduced-biquaternions` | Hermitian Solutions of the Pair Matrix Equation | kept, applications |
| `non-negative-matrix-factorization-over-the-reduced-biquaternions` | Non-Negative Matrix Factorization | kept, applications |

### Menu Surgery

In **Algebra**, add `#### Matrix Representations` with the two new links. The six absorbed links sit in four places: the two $2\times2$ articles under `#### Element Representations`, the eigenbasis article under `#### Spectral Algebra with the Reduced Norm`, the two operator articles under `#### Operators`, and the polar-operator article under `#### Operators Representations` in **Analysis**, whose heading is then deleted.

### What Stays

The four-vector, the other algebraic representations, the Peirce, spinor, sector and polar articles stay.

---

## 6. Quaternions

### The Models

Two models.

- $M_2(\mathbb{C})_{\mathbb{H}}$: the image of $\mathbb{H}$ in its complexification $\mathbb{H}_{\mathbb{C}}\cong M_2(\mathbb{C})$, which is the biquaternion algebra. Size two over $\mathbb{C}$. Determinant $N$, trace $2\operatorname{Re}\alpha$.
- $M_4(\mathbb{R})_{\mathbb{H}_L}$: the Cayley matrix of left multiplication in the basis $(e_0,e_1,e_2,e_3)$; the algebra itself, regular. Size four over $\mathbb{R}$. Determinant $N^2$, trace $4q_0$.

Four articles. These two operators articles are **additions**, not folds: the abstract operator articles carry no matrix, so the matrix reading is missing today.

### $M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation

Slug `h-m2c-standard-representation.md`. Absorbs *Introduction to the $2\times2$ Matrix Element Representation of Quaternions*, *The Quaternion Algebra in the $2\times2$ Matrix Element Representation*.

- **The Frame.** The embedding; the images of the four units, $\mathrm I_2$, $\begin{pmatrix}0&-i\\-i&0\end{pmatrix}$, $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, $\begin{pmatrix}-i&0\\0&i\end{pmatrix}$; the conjugate-linear structure that makes the image a real form; the absence of a real $2\times2$ model.
- **The Left and the Right Matrices.** Both sides stay inside the image, so $L_q$ and $R_q$ are again quaternion matrices; the two copies; the relation by the conjugate transpose.
- **The Product.** The product is the matrix product; the image is closed and four-real-dimensional in the eight of $M_2(\mathbb{C})$ over $\mathbb{R}$.
- **The Trace.** $2\operatorname{Re}\alpha$; the scalar part; the traceless part as the pure quaternions.
- **The Determinant.** $|\alpha|^2+|\beta|^2=N$; multiplicativity; the unit criterion; the definite form and the absence of a null cone.
- **The Spectral Projectors.** The eigenvalues over $\mathbb{C}$; the eigenlines; the diagonalising matrix; the repeated case and the two-dimensional commutant.
- **The Adjugate and the Inverse.** The adjugate is the conjugate transpose, which is the image of the quaternion conjugation; the inverse $\operatorname{adj}A/N$.
- **The Norms.** The determinant as the norm; the trace form; the Frobenius norm; the Hermitian and anti-Hermitian parts.
- **The Subspaces.** The scalar line, the three-dimensional vector space, the Hermitian and anti-Hermitian subspaces, as matrix conditions; the projection onto the Hermitian part as $\tfrac12(A+A^{*})$.
- **Summary**, **Summary of Notation**, **Further Reading**.

### $M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation : Operators

Slug `h-m2c-standard-representation-operators.md`. New.

- **Introduction.** One matrix per side, a pair for the two-sided operator, four pairs for a general endomorphism; the same count as the biquaternion $2\times2$ model, on a smaller scalar field.
- **The One-Sided Operators.** $Y\mapsto AY$ and $Y\mapsto YB$ with $A,B$ in the image; the two copies.
- **The Two-Sided Operator.** $Y\mapsto AYB$; the seven effective real parameters; the scaling.
- **The Kronecker Display.** $B^{\mathsf T}\otimes A$; the coefficient matrix; the rank formula.
- **The Rank and the Invariants.** $\operatorname{rank}A\cdot\operatorname{rank}B$ in $\{0,4\}$, not in $\{0,1,2,4\}$: every nonzero quaternion is invertible, so each factor has rank two and a nonzero product has rank four; trace and determinant; the contrast with the split case, where rank one and rank two both occur.
- **The Pair as a Semigroup.** Composition; the inverse; the automorphisms $B=A^{-1}$ with the conjugation $AYA^{-1}$.
- **The Cone and the Coefficient Matrix.** The carrier is $\mathbb{H}$, of real dimension four, so the ambient is $\operatorname{End}_{\mathbb{R}}(\mathbb{H})=M_4(\mathbb{R})$ and the cone has real dimension $7$; the parameter space $\mathbb{H}\times\mathbb{H}$ has real dimension eight, and the fibre is one real scaling orbit; the membership test is $\operatorname{rank}c(M)\le1$; the reading in this article is over $\mathbb{R}$, and the reading over $\mathbb{C}$ is the biquaternion cone, of which this is the slice with both parameters in $\mathbb{H}$.
- **The Length.** $\ell=\operatorname{rank}c(M)\in\{0,1,2,3,4\}$; the coefficient matrix is a real $4\times4$ in the basis $T_{\mu\nu}$; a generic operator on $\mathbb{H}$ needs four products and none needs five.
- **The Two Ranks.** $\operatorname{rank}T_{q,p}=4$ for every nonzero pair, because $\mathbb{H}$ is a division algebra, so the cone minus its vertex lies inside $GL_4(\mathbb{R})$ while the length still reaches four; an operator can be invertible and need four products, and an operator can be rank one and need one; the matrix rank is in $\{0,4\}$ and tells nothing about the length.
- **What the Pair Buys and Does Not.** The model is not the algebra, so the operator algebra is strictly larger than the algebra; the extra dimension is the content.
- **Summary**, **Summary of Notation**, **Further Reading**.

### $M_4(\mathbb{R})_{\mathbb{H}_L}$ Regular Representation

Slug `h-m4r-regular-representation.md`. Absorbs *Introduction to the $4\times4$ Matrix Element Representation of Quaternions*, *The Quaternion Algebra in the $4\times4$ Matrix Element Representation*.

- **The Frame.** The basis $(e_0,e_1,e_2,e_3)$; the four Cayley matrices; the left regular frame and the right regular frame.
- **The Left and the Right Matrices.** $L_q$ and $R_q$; the stitch $R_q=D L_q^{\mathsf T}D$ with the diagonal sign matrix $D$; the two commuting copies.
- **The Product.** Associativity gives multiplicativity; the image is four-real-dimensional in the sixteen of $M_4(\mathbb{R})$.
- **The Trace.** $4q_0$; the scalar part as $\tfrac14\operatorname{tr}$; the trace vanishes on the pure quaternions.
- **The Determinant.** $N^2$, the square of the norm; why the square; the unit criterion.
- **The Spectral Projectors.** The two conjugate pairs of eigenvalues and the two invariant planes; the real block form; the diagonalisation over $\mathbb{C}$.
- **The Adjugate and the Inverse.** $\operatorname{adj}L_q=N L_{q^{*}}$; the inverse $L_{q^{*}}/N$.
- **The Norms.** The determinant, its square root, the Frobenius norm.
- **The Subspaces.** The scalar, vector, Hermitian and anti-Hermitian images, as matrix conditions; the double centraliser; the comparison with the complex case.
- **Summary**, **Summary of Notation**, **Further Reading**.

### $M_4(\mathbb{R})_{\mathbb{H}_L}$ Regular Representation : Operators

Slug `h-m4r-regular-representation-operators.md`. New.

- **Introduction.** The three levels of the biquaternion $M_4$ article, transposed to the real case.
- **The One-Sided Operators.** The two four-dimensional copies $L(\mathbb{H})$ and $R(\mathbb{H})$; their intersection $\mathbb{R}\mathrm I_4$; the Conway basis as the edge rows.
- **The Two-Sided Operator.** $T_{q,p}=L_qR_p$; the seven-dimensional cone; the composition law.
- **The Kronecker Display.** The $16\times16$ matrix; the coefficient matrix; the length.
- **The Rank and the Invariants.** The rank ladder; trace and determinant of the operator.
- **The Pair as a Semigroup.** Composition; the isometries; the multiplicative members.
- **The Cone and the Coefficient Matrix.** The same cone as in the $M_2$ article, of real dimension $7$ inside $M_4(\mathbb{R})$; what changes is the bookkeeping: the basis $T_{\mu\nu}=L_{e_\mu}R_{e_\nu}$ is indexed by the regular basis, and the coefficient matrix is the $4\times4$ array of *Left Regular Representation* coordinates.
- **The Length.** $\ell=\operatorname{rank}c\in\{0,1,2,3,4\}$; the regular reading makes the extremal cases visible: length one is the cone, length four the open dense set, and the strata of intermediate length are the determinantal varieties of $c$.
- **The Two Ranks.** $\operatorname{rank}T_{q,p}\in\{0,4\}$ against $\ell\in\{0,\dots,4\}$; the article tabulates the two for the sixteen basis operators, all of which have length one and matrix rank four except those with a non-unit parameter, which have neither.
- **What the Pair Buys and Does Not.** The real model carries no Peirce frame and no chirality; the two missing structures are named.
- **Summary**, **Summary of Notation**, **Further Reading**.

### Matrix Articles Today

| slug | title | fate |
|---|---|---|
| `introduction-to-the-2x2-matrix-element-representation-of-quaternions` | Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})_{\mathbb{H}}$ of Quaternions | absorbed, deleted |
| `the-quaternion-algebra-in-the-2x2-matrix-element-representation` | The Quaternion Algebra in the 2×2 Matrix Element Representation $M_2(\mathbb{C})_{\mathbb{H}}$ | absorbed, deleted |
| `introduction-to-the-4x4-matrix-element-representation-of-quaternions` | Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{R})_{\mathbb{H}_L}$ of Quaternions | absorbed, deleted |
| `the-quaternion-algebra-in-the-4x4-matrix-element-representation` | The Quaternion Algebra in the 4×4 Matrix Element Representation $M_4(\mathbb{R})_{\mathbb{H}_L}$ | absorbed, deleted |
| `quaternion-element-representations` | Introduction to Quaternion Element Representations | kept, retitled *Quaternion Linear Representations* |
| `quaternion-four-vector-element-representation` | Quaternion Four-Vector Element Representation | kept |
| `quaternion-other-algebraic-element-representations` | Quaternion Other Algebraic Element Representations | kept |

### Menu Surgery

In **Algebra**, remove the four absorbed links from `#### Element Representations` and add `#### Matrix Representations` with the four new links, one pair per model. Keep `#### Operators` for the abstract family and add `##### Matrix Operator Representations` inside it.

### What Stays

*Quaternion Four-Vector*, *Quaternion Other Algebraic Element Representations*, *The One-Sided Operators*, *Two-Sided Operators*, *The Enveloping Operator Algebra* and *The Pin and Spin Groups* stay.

---

## 7. Split-Quaternions

### The Model

$\mathbb{H}_{\mathrm s}\cong M_2(\mathbb{R})$. Here the model **is** the algebra: every matrix is an element and every element is a matrix, so the general article is a dictionary and not an embedding. This is the closest case to the biquaternion one, and it is the one to do first.

### $M_2(\mathbb{R})$ Standard Representation

Slug `hs-m2r-standard-representation.md`. Absorbs *Split-Quaternion Matrix Element Representations*, *$M_2(\mathbb{R})$ Model : The Subspaces as Matrix Conditions*, *$M_2(\mathbb{R})$ Model : The Idempotents and the Peirce Decomposition*, *$M_2(\mathbb{R})$ Model : Rank-One Matrices and the Null Cone*, *$M_2(\mathbb{R})$ Model : The Centraliser*, *$M_2(\mathbb{R})$ Model : The Conjugations and the Adjoints*, *$M_2(\mathbb{R})$ Model : The Projective Line and the Möbius Action*.

- **The Frame.** The images of $1,i,j,k$ in $M_2(\mathbb{R})$; the trace pairing; the identity of the two four-dimensional spaces; the uniqueness of the model up to conjugacy.
- **The Left and the Right Matrices.** Both are multiplication in $M_2(\mathbb{R})$, and the algebra is not commutative, so $L_A\neq R_A$; the two copies and their commutant.
- **The Product.** The product is the matrix product; the model is surjective and the image is all of $M_2(\mathbb{R})$, against the embedding of the quaternions.
- **The Trace.** $\operatorname{tr}A=2\operatorname{Sc}(A)$; the traceless part as the three-dimensional $\mathfrak{sl}_2(\mathbb{R})$.
- **The Determinant.** $\det A=\langle\tilde q\rangle_{\natural}=q_t^2+q_x^2-q_y^2-q_z^2$, of signature $(2,2)$; $\det=0$ on the null cone; the rank-one matrices as the two rulings; the singular set as a quadric cone, against the codimension-two singular set of $M_2(\mathbb{C})$.
- **The Spectral Projectors.** The discriminant and the trichotomy: $\mathbb{C}$, the dual numbers and $\mathbb{R}\times\mathbb{R}$, by the sign of $\operatorname{tr}^2-4\det$; the two real idempotents in the split case; the single one in the parabolic case; the centraliser as a polynomial algebra of dimension two.
- **The Adjugate and the Inverse.** The adjugate is the conjugation, $\operatorname{adj}\mathsf M_2(\tilde q)=\mathsf M_2(\tilde q^{\natural})$; the inverse $\operatorname{adj}/\det$; the transpose and the three involutions.
- **The Norms.** The determinant form of signature $(2,2)$; the trace form; the Killing form on the traceless part; the absence of a positive definite invariant form.
- **The Subspaces.** The scalar line, the vector space, the fixed points of the four involutions, the isotropic lines, as matrix conditions.
- **The Projective Line.** The Möbius action of $PGL_2(\mathbb{R})$ on $\mathbb{P}^1(\mathbb{R})$, which is the geometry of the model itself.
- **Summary**, **Summary of Notation**, **Further Reading**.

### $M_2(\mathbb{R})$ Standard Representation : Operators

Slug `hs-m2r-standard-representation-operators.md`. Absorbs *$M_2(\mathbb{R})$ Model : The Sandwich and the Adjoint Action*.

- **Introduction.** The model is the algebra, so the matrices and the elements form one four-dimensional space; the count of pairs; what the pair adds.
- **The One-Sided Operators.** $L_A$ and $R_B$; the adjoints through the trace form; the self-adjoint sector.
- **The Two-Sided Operator.** $T_{A,B}(X)=AXB$; the group $(GL_2\times GL_2)/\Delta$; the determinant-preserving subgroup $SO(2,2)$ and its identity component $(SL_2\times SL_2)/\{\pm1\}$; the sandwiched $T_{A,A^{-1}}$, which is the adjoint action $PGL_2\cong SO(2,1)$ and the double cover of the Lorentz group.
- **The Kronecker Display.** $B^{\mathsf T}\otimes A$; the coefficient matrix; the rank formula $\operatorname{rank}A\cdot\operatorname{rank}B$.
- **The Rank and the Invariants.** The rank ladder; the determinant of the operator; the trace.
- **The Pair as a Semigroup.** Composition; the inverse; the automorphisms $B=A^{-1}$; the matrix-unit system and the four-dimensional subspace they span.
- **The Cone and the Coefficient Matrix.** The carrier is $\mathbb{H}_{\mathrm s}\cong M_2(\mathbb{R})$, of real dimension four, so the ambient is $M_4(\mathbb{R})$, of dimension sixteen, and the cone has real dimension $7$: the Segre variety $\mathbb{P}^3\times\mathbb{P}^3$ inside $\mathbb{P}^{15}$; the criterion is $\operatorname{rank}c(M)\le1$, with $c(T_{A,B})=[A][B]^{\mathsf T}$ in the basis $L_{e_\mu}R_{e_\nu}$; the cone is not a subspace here, because the algebra is not commutative.
- **The Length.** $\ell=\operatorname{rank}c(M)\in\{0,1,2,3,4\}$; a generic operator needs four products and four always suffice; the strata of length at most $1,2,3,4$ are the determinantal varieties of the coefficient matrix, of dimensions $7,12,15,16$, so the cone of single products is the smallest closed stratum.
- **The Two Ranks.** $\operatorname{rank}T_{A,B}=\operatorname{rank}A\cdot\operatorname{rank}B\in\{0,1,2,4\}$, never three, against $\ell(T_{A,B})=1$. Two recomputed witnesses separate the two numbers. $T_{tt}+T_{tz}$ is the single product $T_{e_t,e_t+e_z}$: its coefficient matrix has rank one, its operator rank is $2$, and it is singular because $\det(e_t+e_z)=0$. $T_{tt}+T_{xx}$ is not a single product: its coefficient matrix is $\operatorname{diag}(1,1,0,0)$, of rank two, and its operator rank is also $2$. So equal operator rank, unequal length, which is the sharpest form of the statement that the operator rank is not the length. The converse extreme is real: $T_{tt}$ is the identity of the carrier, of operator rank $4$, with coefficient rank one. Measured range of the coefficient rank for operators of image rank one: $1$ or $2$, never more, so an image of rank one can cost two products but not four.
- **What the Pair Buys and Does Not.** The pair supplies the Lorentz action and the rulings; it does not supply a spin structure, which the quaternions do.
- **Summary**, **Summary of Notation**, **Further Reading**.

### Matrix Articles Today

| slug | title | fate |
|---|---|---|
| `split-quaternion-matrix-element-representations` | Split-Quaternion Matrix Element Representations | absorbed, deleted |
| `m2r-model-the-subspaces-as-matrix-conditions` | $M_2(\mathbb{R})$ Model : The Subspaces as Matrix Conditions | absorbed, deleted |
| `m2r-model-the-idempotents-and-the-peirce-decomposition` | $M_2(\mathbb{R})$ Model : The Idempotents and the Peirce Decomposition | absorbed, deleted |
| `m2r-model-rank-one-matrices-and-the-null-cone` | $M_2(\mathbb{R})$ Model : Rank-One Matrices and the Null Cone | absorbed, deleted |
| `m2r-model-the-centraliser` | $M_2(\mathbb{R})$ Model : The Centraliser | absorbed, deleted |
| `m2r-model-the-conjugations-and-the-adjoints` | $M_2(\mathbb{R})$ Model : The Conjugations and the Adjoints | absorbed, deleted |
| `m2r-model-the-projective-line-and-the-mobius-action` | $M_2(\mathbb{R})$ Model : The Projective Line and the Möbius Action | absorbed, deleted |
| `m2r-model-the-sandwich-and-the-adjoint-action` | $M_2(\mathbb{R})$ Model : The Sandwich and the Adjoint Action | absorbed into the operators article, deleted |
| `split-quaternion-element-representations` | Split-Quaternion Element Representations | kept, retitled *Split-Quaternion Linear Representations* |
| `split-quaternion-four-vector-element-representation` | Split-Quaternion Four-Vector Element Representation | kept |
| `split-quaternion-other-algebraic-element-representations` | Split-Quaternion Other Algebraic Element Representations | kept |

### Menu Surgery

The seven `m2r-model-` links sit today under five headings: one under `#### The Algebra and Its Vector Spaces`, two under `#### The Products and the Classes`, two under `#### Element Representations`, one under `#### Operators` in **Algebra**, and one under `#### Operators` in **Geometry**.

### What Stays

The four-vector, the other algebraic representations, the four sectors, the spectral regularity and the polar family stay.

---

## 8. Split-Biquaternions

### The Model

$\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ is not a full matrix algebra. Its faithful model is the diagonal subalgebra of $M_2(\mathbb{H})$,

$$
\tilde Q\mapsto\begin{pmatrix}\tilde Q_+&0\\ 0&\tilde Q_-\end{pmatrix},
$$

with the two idempotents $\tfrac12(1\pm\omega)$ projecting onto the two blocks. There are no off-diagonal units, and that absence is the content of the general article.

### $M_2(\mathbb{H})$ Diagonal Representation

Slug `sb-m2h-diagonal-representation.md`. Absorbs *Split-Biquaternion Algebraic Element Representations*, whose section *The Absence of a Matrix Representation* becomes the frame section.

- **The Frame.** The basis of eight real coefficients; the split unit $\omega$ with $\omega^2=1$; the two idempotents $\tfrac12(1\pm\omega)$; the two blocks; the degenerate system of matrix units and why the off-diagonal entries vanish.
- **The Left and the Right Matrices.** Blockwise; the two copies; the diagonal form of both.
- **The Product.** Blockwise product; the algebra is a product of two division algebras, so every computation separates; the failure of the model to be surjective.
- **The Trace.** $\operatorname{tr}\begin{pmatrix}\tilde Q_+&0\\0&\tilde Q_-\end{pmatrix}=\tilde Q_++\tilde Q_-\in\mathbb{H}$, a quaternion; its scalar part is the sum of the two scalar parts; the trace is not central.
- **The Determinant.** $N(\tilde Q_+)N(\tilde Q_-)$, the reduced norm; $\det=0$ exactly on the zero divisors, which are the elements with a vanishing block.
- **The Spectral Projectors.** The two central idempotents; the block diagonalisation as the primary spectral statement; the two independent spectra; the comparison with the single spectrum of $\mathbb{B}$.
- **The Adjugate and the Inverse.** Blockwise; the inverse on the complement of the zero-divisor set.
- **The Norms.** The reduced norm as the determinant; the split signs; the four subspace norms.
- **The Subspaces.** The split-complex, quaternion, Hermitian and anti-Hermitian subspaces, as block conditions; the involution lattice.
- **Summary**, **Summary of Notation**, **Further Reading**.

### $M_2(\mathbb{H})$ Diagonal Representation : Operators

Slug `sb-m2h-diagonal-representation-operators.md`. New.

- **Introduction.** The operators split blockwise, and the article says what survives of the biquaternion ladder $1,4,7,16$.
- **The One-Sided Operators.** Two commuting copies acting blockwise; the rank as the sum of the two block ranks.
- **The Two-Sided Operator.** $T_{\tilde Q,\tilde P}$ blockwise; the cone splits into two cones; the composition.
- **The Kronecker Display.** The block diagonal Kronecker product; the coefficient matrix; the length.
- **The Rank and the Invariants.** The rank in $\{0,4,8\}$ by blocks, four per block and never two, because each block is a division algebra; trace and determinant.
- **The Pair as a Semigroup.** Composition; the isometries; the multiplicative members.
- **The Cone and the Coefficient Matrix.** Two blocks, so two cones. Every product is block diagonal, so the reach is the block-diagonal part of $\mathrm{End}_{\mathbb{R}}(\mathbb{H}_{\mathbb{D}})=M_8(\mathbb{R})$, of dimension $32$ inside $64$; this is the one category where even the **span** falls short of the ambient, and the reason is that $\mathbb{H}_{\mathbb{D}}$ is not simple while $\mathbb{H}$ is. The image is the product of the two seven-dimensional cones, of real dimension $14$ inside that $32$; the parameter space has real dimension sixteen and the fibre is $(\mathbb{R}^{\times})^2$, of dimension two, which is the double scaling $\tilde Q_\pm\mapsto\lambda_\pm\tilde Q_\pm$, and the count $16-2=14$ is consistent; the criterion is applied blockwise, $\operatorname{rank}c(M_\pm)\le1$ in each block, with $c$ indexed by the block-diagonal basis.
- **The Length.** $\ell\le4$, not $8$: the two block factorisations run in parallel and can share their index, so the composite takes the larger of the two lengths and not their sum; the values are $\{0,\dots,4\}$.
- **The Two Ranks.** $\operatorname{rank}T_{\tilde Q,\tilde P}\in\{0,4,8\}$, blockwise, because each block is a division algebra; $\ell$ ranges over $\{0,\dots,4\}$; the two are as unrelated here as in the quaternion case, and the table gives one witness for each of the two discrepancies.
- **What the Pair Buys and Does Not.** The two blocks give two independent operator families and no mixing; the missing mixing is the difference from $\mathbb{B}$.
- **Summary**, **Summary of Notation**, **Further Reading**.

### Matrix Articles Today

| slug | title | fate |
|---|---|---|
| `split-biquaternion-algebraic-element-representations` | Split-Biquaternion Algebraic Element Representations | absorbed, deleted |
| `split-biquaternion-four-vector-element-representation` | Split-Biquaternion Four-Vector Element Representation | kept |
| `split-biquaternion-element-representation-theory` | Split-Biquaternion Element Representation Theory | kept, retitled *Split-Biquaternion Linear Representations* |

### Menu Surgery

In **Algebra**, add `#### Matrix Representations` with the two new links after `#### Element Representations`, from which the absorbed link is removed. The category has no `#### Operators` subsection today; the operators article creates it.

### What Stays

*Split-Biquaternion Four-Vector*, the retitled linear-representation article, the sectors, the Clifford formulation and the polar family stay.

---

## Tier Two — The Algebraic-Structure Blocks

Four blocks sit inside the categories and are not number systems: *Complexoid*, *Split-Complexoid*, *Quaternioid* and *Biquaternion Algebraic Structures*. Each block is a family of products on one space, so one pair per product would explode the count.

The rule here is **defer, and rename only**.

- **Complexoid and split-complexoid.** Both read products on $\mathbb{C}$ and on $\mathbb{D}$. Their model is the one of the parent category, so the pair already exists and the block cites it. *The Matrix Element Representations of the Complexoid* and its split twin keep their articles and gain a pointer to the pair.
- **Quaternioid.** Six articles carry "in the $2\times2$ Matrix Element Representation" or "in the $4\times4$ …". They are the second product on the quaternion models and they stay. Rename them to the pair's frame names: "$M_2(\mathbb{C})_{\mathbb{H}}$ Representation : X" and "$M_4(\mathbb{R})_{\mathbb{H}_L}$ Representation : X".
- **Biquaternion structures.** Six articles carry the pattern already, three as "$M_2(\mathbb{C})$ Representation : The X of Biquaternions" and three as "X in the $M_4(\mathbb{C})$ Left Regular Representation". The first three are the target form; convert the last three to "$M_4(\mathbb{C})$ e-basis Representation : The X of Biquaternions".

Tier two is twelve renames and no new articles.

## Errata in the Two Notes

Both notes were read line by line. Five corrections, none of which changes a conclusion.

1. **The biquaternion note is pasted twice.** The second and third blocks of the message are identical. Nothing is lost; one copy is enough.

2. **"$-T_{\mu\nu}$ is not in the family" is false.** The cone is closed under scaling, so $-T_{\mu\nu}=T_{-\mu,\nu}$ is a product like any other. The monoid is not a group for the correct reason: $T_{Q,P}$ is invertible iff **both** parameters are units, so any pair with a non-unit parameter is a non-invertible member, and non-invertible members exist in abundance.

3. **The additive-failure parenthesis is valid for $\mathbb{H}$ and does not transfer.** The note proves $T_{tt}+T_{xx}$ is not a product twice: by the coefficient matrix $\operatorname{diag}(1,1,0,0)$, of rank two, and by an evaluation argument, "the value at $e_t$ forces $QP=0$, and $QP=0$ cannot reproduce $2e_y$ at $e_y$". The second argument is correct **only because $\mathbb{H}$ is a division algebra**, where $QP=0$ forces $Q=0$ or $P=0$, and then every value vanishes. In $\mathbb{H}_{\mathrm s}$ the implication fails, since $\begin{pmatrix}1&0\\0&0\end{pmatrix}\begin{pmatrix}0&0\\0&1\end{pmatrix}=0$ with both factors nonzero, and the evaluation argument would have to be redone. The article should lead with the coefficient-rank proof in all categories and keep the division-algebra argument as a remark specific to $\mathbb{H}$ and $\mathbb{B}$.

4. **"The two isomorphism classes of 2-dimensional complex algebras" needs the word "commutative unital".** Without it the classification is incomplete. With it, the section is correct and the two images it computes are the right ones.

5. **The $\mathbb{C}^2$ note's determinant language needs one guard.** "$\det M=0$" is the criterion only because the carrier is two-dimensional. In the general module case the criterion is $\operatorname{rank}M\le1$, and the determinant is the special form it takes in $M_2$. The article should state the rank form first and the determinant second, so that the parallel with the algebra categories is visible.

Two numbers were checked against the corpus and are right: for the biquaternion, $\operatorname{Tr}T_{Q,P}=4Q_tP_t$ and $\det T_{Q,P}=\langle Q\rangle_{\#}^{2}\langle P\rangle_{\#}^{2}$, from $\operatorname{rank}(B^{\mathsf T}\otimes A)=\operatorname{rank}A\cdot\operatorname{rank}B$ and $\det(A\otimes B)=\det(A)^{n}\det(B)^{n}$ with $n=2$.

## The Eighteen Articles to Write

Flat list, in writing order. "Absorbs" counts the existing articles deleted at the same time. Every slug was checked free.

| # | slug | title | absorbs | writes |
|---|---|---|---|---|
| 1 | `hs-m2r-standard-representation.md` | $M_2(\mathbb{R})$ Standard Representation | 7 | general, split-quaternions |
| 2 | `hs-m2r-standard-representation-operators.md` | $M_2(\mathbb{R})$ Standard Representation : Operators | 1 | operators, split-quaternions |
| 3 | `h-m2c-standard-representation.md` | $M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation | 2 | general, quaternions |
| 4 | `h-m2c-standard-representation-operators.md` | $M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation : Operators | 0 | operators, quaternions |
| 5 | `h-m4r-regular-representation.md` | $M_4(\mathbb{R})_{\mathbb{H}_L}$ Regular Representation | 2 | general, quaternions |
| 6 | `h-m4r-regular-representation-operators.md` | $M_4(\mathbb{R})_{\mathbb{H}_L}$ Regular Representation : Operators | 0 | operators, quaternions |
| 7 | `c-m2r-cayley-representation.md` | $M_2(\mathbb{R})$ Cayley Representation | 1 | general, complex |
| 8 | `c-m2r-cayley-representation-operators.md` | $M_2(\mathbb{R})$ Cayley Representation : Operators | 0 | operators, complex |
| 9 | `d-m2r-hyperbolic-representation.md` | $M_2(\mathbb{R})$ Hyperbolic Representation | 2 | general, split-complex |
| 10 | `d-m2r-hyperbolic-representation-operators.md` | $M_2(\mathbb{R})$ Hyperbolic Representation : Operators | 1 | operators, split-complex |
| 11 | `dual-m2r-triangular-representation.md` | $M_2(R)$ Triangular Representation | 1 | general, dual |
| 12 | `dual-m2r-triangular-representation-operators.md` | $M_2(R)$ Triangular Representation : Operators | 0 | operators, dual |
| 13 | `rb-m2c-reduced-representation.md` | $M_2(\mathbb{C})$ Reduced Representation | 3 | general, reduced biquaternions |
| 14 | `rb-m2c-reduced-representation-operators.md` | $M_2(\mathbb{C})$ Reduced Representation : Operators | 3 | operators, reduced biquaternions |
| 15 | `sb-m2h-diagonal-representation.md` | $M_2(\mathbb{H})$ Diagonal Representation | 1 | general, split-biquaternions |
| 16 | `sb-m2h-diagonal-representation-operators.md` | $M_2(\mathbb{H})$ Diagonal Representation : Operators | 0 | operators, split-biquaternions |
| 17 | `c2-m2c-defining-representation.md` | $M_2(\mathbb{C})$ Defining Representation | 0 | general, duo-complex, module contract |
| 18 | `c2-m2c-defining-representation-operators.md` | $M_2(\mathbb{C})$ Defining Representation : Operators | 0 | operators, duo-complex, two cones |

$18$ articles, $24$ absorbed, $25$ kept.

### The Per-Pair Cycle

Each pair is one unit of work, repeated eight times. The order inside the unit matters.

1. **Recompute.** Run the three checks of *Claims to Recompute* for that category only: the cone, the fibre, the membership test, the length range, the isometry dimension; one operator that is a single product and one that is not. Write the numbers down before writing prose.
2. **General article.** Eight sections against the contract in *The Rule*, plus Introduction and the three closing sections.
3. **Operators article.** The five common sections, then whatever the category adds, then the three sections of the second layer.
4. **Cross-links.** One link from the general article to the operators article, one back, and the citations to the articles that stay.
5. **Menu surgery.** Insert the two links under the heading named for that category, delete the absorbed links, in the same edit.
6. **Delete the absorbed files.** Only now, after the links are moved, so no menu entry ever points at a missing file.
7. **Counts.** Re-run the count of the map's tables against the corpus.

Deleting before writing is the one order that cannot be repaired: the menu would point at a missing article and the content would be gone.

### What Is Actually Next

1. **Settle the retitle.** Seven articles change *Element Representations* to *Linear Representations*. It is the only blocking decision, it is a one-line edit each, and it must happen before the first pair lands or the new titles collide with the old ones.
2. **Pre-flight on pair 1.** Recompute the split-quaternion second layer: the two cones, the length of one composite, the coefficient rank on the null lines. The biquaternion note's numbers transfer here without change, which is why this pair is first.
3. **Write pairs 1 and 2.** Fifteen articles' worth of material compressed into four, and it removes the last seven `m2r-model-` titles.
4. **Write pairs 7 to 12**, the three commutative categories, where the second layer degenerates and the article has to carry a negative theorem.
5. **Write pairs 13 to 16**, then 17 and 18.
6. **Tier two.** Twelve renames, once the pair titles are fixed.

### Why This Order

The table above is the writing order. The reasons, category by category:

- **Split-quaternions first**, because the second layer is the part that is easiest to get wrong and the biquaternion note's numbers transfer here without change. It also removes the last block of `m2r-model-` titles, so the wording of the model names is settled once and for all.
- **Quaternions second.** Two models, so two pairs, and the only category where the two determinants differ, $N$ against $N^{2}$. The abstract operator articles stay, so the matrix reading is pure addition.
- **Complex, split-complex, dual third.** One collapse proof, $L_QR_P=L_{QP}$, serves all three, and all three report $\ell\in\{0,1\}$. Doing them together keeps the wording identical.
- **Reduced biquaternions fourth.** The block form makes the passage to the idempotent frame easy, and the category sits between the complex and the quaternionic cases, which by then are both written.
- **Split-biquaternions fifth**, because the model has to be stated and defended: the algebra is not a full matrix algebra, and the off-diagonal entries are empty. That argument reads better once every other model is written.
- **Duo-complex sixth.** It needs the biquaternion pair finished, since it cites it and must not repeat it.
- **Tier two last.** Twelve renames, which need the pair titles fixed first.

The reason the second layer comes second in every operators article, and never first: it is the only part with no counterpart in the current corpus, so it is the only part that can be wrong without anything to compare against.

## Open Decisions

1. **The $M_2(\mathbb{C})$ collision.** The duo-complex model is the algebra of the biquaternion category, so the two pairs meet on one algebra. The proposal resolves it by subject, not by model: the biquaternion pair owns the algebra, the duo-complex pair owns the module and the readings it produces, and the general article takes the module contract. Under that split the two pairs share no section and no object. The alternative — no pair at all here — is now the weaker option, because the spinor, the light cone and the qubit would then have no home: no article of the mathematics corpus mentions them, and `physics.md` uses them throughout.
2. **"Model" against "Representation".** The seven split-quaternion articles use "$M_2(\mathbb{R})$ Model :". They are absorbed by the pair, so the word disappears if the pair is written first. If they are kept, the corpus carries both words for one thing.
3. **The double meaning of "representation".** Seven articles use it for Schur's lemma and the representation ring. The map assumes they are retitled "Linear Representations". Without that, the new titles collide with the old ones.
4. **Four articles for the quaternions, or two.** Four respects the two standing models, whose determinants differ, $N$ against $N^2$. Two would fold the regular model into a section of the defining one and save two articles.
5. **The commutative categories end on a negative result.** Their operators articles close on the collapse. Confirm that is the wanted ending, rather than a shorter article that stops after the semigroup.
6. **The polar family.** It is not representation material and is not absorbed. Confirm that the polar articles keep their place under Analysis, since two of them are absorbed as operator content today.

## Claims to Recompute

Before writing any of these articles, recompute on at most a hundred elements:

1. The second layer, category by category: the cone dimension, the fibre dimension, the membership test, the length range and the isometry dimension of the master table. The sharpest single check is the length theorem on one operator of each category that is **not** a single product, together with one that is. The two cases from the notes should be reproduced first, $T_{tt}+T_{tz}$ and $T_{tt}+T_{xx}$ in the biquaternion algebra, then the $\mathbb{C}^2$ pair $E_{11}+E_{22}$.

2. The length bounds: $\ell\in\{0,1\}$ for $\mathbb{C}$, $\mathbb{D}$ and $\mathbb{D}'$; $\ell\le2$ for the module; $\ell\le4$ for $\mathbb{H}$, $\mathbb{H}_{\mathrm s}$ and $\mathbb{B}$; and $\ell\le4$ for $\mathbb{H}_{\mathbb{D}}$, where the two blocks share their index and do not add. The split-biquaternion case is the one to check twice.
3. The collapse: the span of $\{L_QR_P\}$ has the dimension of the algebra for $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$ and $\mathbb{B}_{\mathrm r}$, namely $2,2,2,4$ over $\mathbb{R}$.
4. The six adjugates: $M_{\bar Q}$ twice, the triangular one, the reduced one, the conjugate transpose, $N L_{q^{*}}$.
5. The nine determinants: $q^2+q'^2$, $q^2-q'^2$, $q^2$, $Q_+Q_-$, $|Q_+Q_-|^2$, $N$, $N^2$, $\langle\tilde q\rangle_{\natural}$, $N(\tilde Q_+)N(\tilde Q_-)$.
6. The traces: $2q$, $2Q_\blacktriangle$, $4q_\blacktriangle$, $2\operatorname{Re}\alpha$, $4q_0$, and the quaternion-valued $\tilde Q_++\tilde Q_-$.

## What This Map Does Not Touch

Topology, Analysis, Geometry and Fractal Geometry, the applications, the sector articles, the spectral regularity and degeneracy articles, the involutions and conjugations articles outside the model, the modules and ideals articles, and the physics corpus. The map changes the representation slots of Part VI only.
