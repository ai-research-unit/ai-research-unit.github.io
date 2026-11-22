# __The Length of an Endomorphism of the Biquaternion Algebra: Four Two-Sided Products__

## Introduction

**The question.** A two-sided operator of the biquaternion algebra is a product of a left and a right multiplication, $L_{\tilde Q_1}R_{\tilde Q_2}(\tilde X)=\tilde Q_1\tilde X\tilde Q_2$. The products form a cone and not a subspace, so the sum of two of them is rarely a third. This article asks for the least number of products whose sum is a given complex-linear endomorphism $M$, and for the largest value that least number takes.

**The answer.** Every complex-linear endomorphism of $\mathbb{B}$ is a sum of at most four two-sided operators, and four is the exact bound. The least number of terms is the rank of one $4\times4$ array $c(M)$, the array of the coefficients of $M$ in the sixteen basis products $T_{\mu\nu}=L_{e_\mu}R_{e_\nu}$. The bound four is the number of indices of the array, which is the complex dimension of the algebra. The array exists because the sixteen products are linearly independent, and it is canonical because they are orthogonal for the Hilbert–Schmidt form.

**The identity that carries the proof.** The ambient is the endomorphism algebra $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension sixteen, and the two-sided family is the image of the tensor product,
$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\longrightarrow\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad \tilde Q_1\otimes\tilde Q_2\longmapsto L_{\tilde Q_1}R_{\tilde Q_2},
$$
an isomorphism because $\mathbb{B}\cong M_2(\mathbb{C})$ is a central simple algebra. A product is a pure tensor. A sum of $k$ products is a tensor of rank at most $k$, and the least $k$ is the tensor rank, which the coefficient array computes. **The product condition becomes a rank condition, and the length becomes the rank of an array.** No frame of the carrier is chosen anywhere: the only numbers are the coefficients in the sixteen products.

**Why the bound is not a tautology.** The sixteen products could have spanned a proper subspace of the sixteen-dimensional ambient, and then no bound of four would exist. That they span is the first half of the theorem, and it is the isomorphism above read on the sixteen tensor products of a basis. The second half is sharpness: four is attained, by the quaternion conjugation, by the projection onto the scalar line, by the transpose of the model, and by every operator off a hypersurface. The naive objection that three terms should suffice by counting parameters is answered in §*The strongest objection, and its answer*.

**The trap.** The ambient is $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension sixteen, and not the algebra of the module endomorphisms $\operatorname{End}_{\mathbb{B}}(\mathbb{B})=\mathbb{B}^{\mathrm{opp}}$, of dimension four. The module endomorphisms are the right multiplications alone. A statement about "the endomorphisms of the algebra" is a statement about the first algebra, and the four of this article is a fact about it.

**The second count, which is a different count.** *The SVD Decomposition of Endomorphisms of the Biquaternion Algebra* writes the same $M$ as a sum of rank-one endomorphisms with weights, and the number of terms there is the number of nonzero weights. That number is the operator rank of $M$. The count of this article is the rank of the array $c(M)$, and the two counts are different functions of $M$: the identity is one product and four atoms, the projection onto the scalar line is four products and one atom, and no inequality holds between the two numbers.

**The boundary over the reals.** Every product is complex-linear, so the real span of the sixteen products is thirty-two-dimensional inside the sixty-four-dimensional space of real-linear maps. Four terms cover every complex-linear endomorphism and no real-linear map outside that space. A general real-linear endomorphism needs eight terms, four for its linear part and four for its antilinear part.

**Boundaries.** The two families and their laws are *Operators Acting on One Side* and *Operators Acting on Two Sides*; the ambient space is *The Endomorphisms of the Biquaternion Algebra*; the sixteen products in the two frames of the category are *$M_4(\mathbb{C})$ Axis-Free Representation : Operators* and *$M_4(\mathbb{C})$ Pauli Representation : Operators*; the theorem that the length is the array rank at the size of the defining representation is *$M_2(\mathbb{C})$ Pauli Representation : Operators* and, in the algebra-free form, *The Length and the Two Ranks on $M_n(\mathbb{C})$*; the Segre cone and the orthogonality of the products are *The Two-Sided Operators and the Segre Cone at $n=4$*; the other decomposition is *The SVD Decomposition of Endomorphisms of the Biquaternion Algebra*; and the split category is *$M_2(\mathbb{R})$ Standard Representation : Operators*.

**The letters.** $\mathbb{B}$ is the biquaternion algebra with basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ and $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$. The letters, the four families and the adjoint signs are those of *Operator Family Conventions*: $L$, $R$, $LR$ and $\Theta$. The sixteen basis products are $T_{\mu\nu}=L_{e_\mu}R_{e_\nu}$, with Greek indices running over $t,x,y,z$. The coefficient array is $c(M)$, the length is $\ell(M)$, $\natural$ is the quaternion conjugation, $\operatorname{Sc}$ the scalar part, and $\operatorname{rank}$ the rank of a family of vectors, hence of an array.

**The order of the article.** The ambient and the two endomorphism algebras come first, because the word *endomorphism* has to be fixed before it is counted. The basis theorem follows, then the array, then the length, then the witnesses that make four sharp. The ladder of strata follows, and then the block structure of the array and the null cone of label two, which is the one place where the length changes inside a block. The comparison with the singular decomposition, the construction of a decomposition and the list of what the length is not close the argument. The real boundary and the split category are stated last, because they are statements about the scope of the theorem and not about the algebra.

## The Ambient and the Two Endomorphism Algebras

**The algebra and the two endomorphism algebras.** Two different endomorphism algebras are read on $\mathbb{B}$, and the difference is the whole of this section.

| algebra | what it is | complex dimension |
|---|---|---|
| $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ | all complex-linear maps, the ambient | $16$ |
| $\operatorname{End}_{\mathbb{B}}(\mathbb{B})$ | the maps commuting with every left multiplication | $4$ |

**The module endomorphisms are the right multiplications.** A map $F$ with $F(\tilde Q\tilde X)=\tilde QF(\tilde X)$ for all $\tilde Q$ is determined by $F(e_t)$, and it is the right multiplication by $F(e_t)$. So $\operatorname{End}_{\mathbb{B}}(\mathbb{B})=\{R_{\tilde Q}\}=\mathbb{B}^{\mathrm{opp}}$, of dimension four. A two-sided operator with a non-central left multiplier is not of this kind: $L_{\tilde Q_1}R_{\tilde Q_2}(\tilde Q\tilde X)=\tilde Q_1\tilde Q\tilde X\tilde Q_2$ differs from $\tilde Q\tilde Q_1\tilde X\tilde Q_2$ by the commutator of $\tilde Q$ with $\tilde Q_1$. The family of the products is therefore far larger than the module endomorphisms, and the ambient of the theorem is the whole of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension sixteen.

**The identity of the two algebras, and where it comes from.** The ambient is the endomorphism algebra of a four-dimensional complex space; a map of the space is a map of the space, and any list of sixteen numbers for it is a choice of frame. The two-sided family gives a description of the same algebra, with no choice of basis: $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$, where the first slot acts on the left and the second on the right. The double centraliser theorem identifies the two descriptions, and the identification is the theorem of the next section.

**Two objects and one operator, and no frame of the carrier.**

| object | what it is | where it lives |
|---|---|---|
| $\mathsf M_2(\tilde Q)$ | the element, in the defining representation of the algebra | on the spinor space, dimension two |
| $c(M)$ | the operator, in the basis $L_{e_\mu}R_{e_\nu}$ of products | on the tensor $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$, dimension sixteen |

**The two are different objects of two different spaces.** The element lives on a two-dimensional module; the array is written in a basis of operators, not of the carrier, and it has two indices, one for each slot of $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$. The array is not a map of the algebra; it is the list of the operator's coefficients in the products. The length reads that list. The image rank of the operator, which the singular decomposition counts, is a number attached to the map and to no array at all.

**The two parameters and the one redundancy.** The pair $(\tilde Q_1,\tilde Q_2)$ runs over a space of complex dimension eight, and the operator depends on it through seven, because $L_{\lambda\tilde Q_1}R_{\lambda^{-1}\tilde Q_2}=L_{\tilde Q_1}R_{\tilde Q_2}$ for every $\lambda\neq0$. The image is therefore a cone of dimension seven inside a space of dimension sixteen, of codimension nine.

## The Sixteen Products Are a Basis

**The definition.** For two elements the two-sided operator is
$$
L_{\tilde Q_1}R_{\tilde Q_2}:\tilde X\longmapsto\tilde Q_1\tilde X\tilde Q_2 ,
$$
and the sixteen operators $T_{\mu\nu}=L_{e_\mu}R_{e_\nu}$, with $\mu,\nu\in\{t,x,y,z\}$, are the basis products.

**The composition law.** Two products compose to one product,
$$
\bigl(L_{\tilde Q_1}R_{\tilde Q_2}\bigr)\bigl(L_{\tilde P_1}R_{\tilde P_2}\bigr)
=L_{\tilde Q_1\tilde P_1}R_{\tilde P_2\tilde Q_2},
$$
because the middle factors meet as $\tilde Q_2\tilde P_1$ and the two multiplication maps act on opposite sides. The product family is closed under composition and not under addition. The two facts are the source of everything that follows: the first makes the family an algebra of operators, the second makes the length a nontrivial number.

**Theorem (the products are a basis).** The sixteen operators $T_{\mu\nu}$ are linearly independent, and their complex span is the whole of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$.

*Proof.* The ambient has complex dimension sixteen and there are sixteen products, so independence and spanning are one statement. The products are pairwise orthogonal for the Hilbert–Schmidt form with squared norm four, a finite computation from the multiplication table that is carried out in *The Two-Sided Operators and the Segre Cone at $n=4$*; sixteen nonzero pairwise orthogonal vectors are independent, so they are a basis.

**The same theorem without a computation.** The assignment $\beta(\tilde Q_1\otimes\tilde Q_2)=L_{\tilde Q_1}R_{\tilde Q_2}$ is the standard algebra isomorphism $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ for a central simple algebra. Since $\mathbb{B}\cong M_2(\mathbb{C})$, the left side is $M_2\otimes M_2\cong\operatorname{End}(M_2)$, and the tensor products of a basis with a basis are a basis. The images of the sixteen tensor products $e_\mu\otimes e_\nu$ are the sixteen products. The two proofs are the two readings of one fact: the orthogonal basis is the computation, the tensor isomorphism is the reason.

**The orthogonality, which makes the array computable.** With the coefficient inner product $\langle\tilde X,\tilde Y\rangle=\sum_\mu\bar X_\mu Y_\mu$, the Hilbert–Schmidt form on the ambient is $\langle M,N\rangle_{\mathrm{HS}}=\operatorname{tr}(M^{\dagger}N)$, and the basis products are orthogonal with a constant squared norm,
$$
\operatorname{tr}\bigl(T_{\mu\nu}^{\dagger}T_{\rho\sigma}\bigr)=4\,\delta_{\mu\rho}\delta_{\nu\sigma}.
$$
Consequently the coefficient array of an operator is one quarter of a trace,
$$
c(M)_{\mu\nu}=\tfrac14\operatorname{tr}\bigl(T_{\mu\nu}^{\dagger}M\bigr),
$$
and the expansion $M=\sum_{\mu\nu}c(M)_{\mu\nu}T_{\mu\nu}$ is exact for every $M$. The constant four is the squared norm of a basis product and depends on the form $\operatorname{tr}(M^{\dagger}N)$ taken without a normalising denominator; another normalisation of the trace form rescales $c$ by a nonzero constant and leaves its rank, hence the length, unchanged. The array is not an artefact of a clever choice of basis: the products are an orthogonal basis, so the array is as canonical as the coordinates of a vector in an orthogonal frame.

**The single products are one cone.** The set of products is the image of the bilinear map $(\tilde Q_1,\tilde Q_2)\mapsto L_{\tilde Q_1}R_{\tilde Q_2}$ from $\mathbb{C}^4\times\mathbb{C}^4$, so it is the cone over the Segre variety $\mathbb{P}^3\times\mathbb{P}^3$, of complex dimension $6+1=7$. In the array picture it is the set of arrays of rank at most one. The identification of the two descriptions is the content of *The Two-Sided Operators and the Segre Cone at $n=4$*; this article uses it in one direction only, that a product has an array of rank one.

## The Length Is the Rank of One Array

**Definition.** The **length** of an operator is the least number of products whose sum it is,
$$
\ell(M)=\min\Bigl\{k:\ M=L_{\tilde Q_1}R_{\tilde P_1}+\cdots+L_{\tilde Q_k}R_{\tilde P_k}\Bigr\},
$$
with $\ell(0)=0$.

**Theorem (the length is the array rank).** For every endomorphism $M$ of $\mathbb{B}$,
$$
\ell(M)=\operatorname{rank}c(M)\in\{0,1,2,3,4\}.
$$

*Proof.* Write $c_{\tilde Q}$ for the coefficient vector of an element $\tilde Q$. The array of a single product is the outer product of two such vectors,
$$
c(L_{\tilde Q_1}R_{\tilde Q_2})_{\mu\nu}=c_{\tilde Q_1,\mu}c_{\tilde Q_2,\nu},
$$
so it has rank one. Hence the array of a sum of $k$ products is a sum of $k$ outer products, of rank at most $k$, and $\ell(M)\ge\operatorname{rank}c(M)$. Conversely, an array of rank $r$ is a sum of $r$ outer products of vectors, $c(M)=\sum_{k\le r}u_kv_k^{\mathsf T}$, and by the surjectivity of the coefficient map each $u_k$ is $c_{\tilde Q_k}$ for an element $\tilde Q_k$ and each $v_k$ is $c_{\tilde P_k}$ for an element $\tilde P_k$; then $M=\sum_{k\le r}L_{\tilde Q_k}R_{\tilde P_k}$, and $\ell(M)\le r$.

**The corollary.** Every endomorphism is a sum of at most four products, and the bound four is the side of the array, that is the complex dimension of the algebra. The number is not a property of the map; it is the size of the algebra in which the map is written.

**The invariance under a change of basis.** A change of basis of the algebra acts on the two slots of the tensor independently, so it replaces $c$ by $S_1cS_2$ with $S_1$ and $S_2$ invertible. Both factors preserve the rank. The length is therefore a property of the operator and not of the frame in which the array is written.

**The strongest objection, and its answer.** *The bound of four is trivial, since a $4\times4$ array has rank at most four.* The objection is right about the bound and wrong about the content. The bound is trivial once the array is written. What is not trivial is that the array exists, which is the independence theorem of the previous section, and that the bound is attained, which is the subject of the next. The same objection in another form says that a two-sided operator has seven effective parameters, so two of them have fourteen and three have twenty-one, and three should suffice by counting. The naive count is wrong, because the map from a $k$-tuple of products to its sum is not injective: a linear recombination of the $k$ tuples leaves the sum unchanged, which is the gauge freedom used in §*How a Decomposition Is Found*, so the $7k$ parameters overcount. Seven per product give fourteen for two terms, but the image of the pair of tuples is only twelve-dimensional. The right count is the dimension of the image, the determinantal variety of the arrays of rank at most $k$: twelve for two terms and fifteen for three, and fifteen is a hypersurface in the sixteen-dimensional ambient. That count is the rank of the array, and it gives four.

## Four Is Attained

**The generic value.** The condition $\ell(M)\le3$ is $\det c(M)=0$, a single polynomial equation. The operators of length four are therefore the complement of a hypersurface: they are open and dense. Four is the value on almost every operator, and no smaller bound holds.

**Witnesses, all elementary.** The following operators are the ones a reader of the category meets first, and their lengths settle the question.

| operator | definition | operator rank | array | length |
|---|---|---|---|---|
| the identity | $\tilde X\mapsto\tilde X$ | $4$ | $\operatorname{diag}(1,0,0,0)$ | $1$ |
| a left multiplication | $\tilde X\mapsto\tilde Q\tilde X$ | $0,2,4$, twice the rank of $\tilde Q$ | $c_{\tilde Q}\,c_{e_t}^{\mathsf T}$ | $1$ |
| the quaternion conjugation | $\tilde X\mapsto\tilde X^{\natural}$ | $4$ | $-\tfrac12\mathrm I_4$ | $4$ |
| the projection onto the scalar line | $\tilde X\mapsto\operatorname{Sc}(\tilde X)e_t$ | $1$ | $\tfrac14\operatorname{diag}(1,-1,-1,-1)$ | $4$ |
| the transpose in the model | $\mathsf Y\mapsto\mathsf Y^{\mathsf T}$ | $4$ | $\tfrac12\operatorname{diag}(1,-1,1,-1)$ | $4$ |

**The conjugation is minus one half of the diagonal sum.** The array $-\tfrac12\mathrm I_4$ is the array of $-\tfrac12\sum_\mu T_{\mu\mu}$, so the quaternion conjugation has the explicit four-term form
$$
\tilde X^{\natural}=-\tfrac12\sum_{\mu\in\{t,x,y,z\}}e_\mu\tilde X e_\mu ,
$$
which is a finite computation from the multiplication table, and the four terms are the minimum, because the array is a nonzero multiple of the identity, of rank four. This is the cleanest sharpness statement in the algebra: the conjugation is the most natural operator the algebra carries, and it is not a dressed multiplication.

**The projection is the operator of smallest image and largest length.** The map $\tilde X\mapsto\operatorname{Sc}(\tilde X)e_t$ has image of rank one, and its length is four. Its array is $\tfrac14\operatorname{diag}(1,-1,-1,-1)$, of rank four, so four products are needed for an operator whose image is a line. The map is $\tfrac12(\mathrm I+\natural)$, and this identity reads its length a second way: the array of the identity operator, which is the single product $T_{tt}$, has rank one, and that of the conjugation has rank four, and the half-sum is a diagonal array with four nonzero entries.

**The rank-one stratum is not short.** The operators of length at most three are the zeros of the polynomial $\det c$, so they form a proper closed subset of the rank-one stratum, and the operators of length four are dense in that stratum. A rank-one operator of length four can be written down with rational entries: the operator $F(\tilde X)=\langle\tilde X,v\rangle\,u$ with $u=(1,-1,2,-1)$ and $v=(3,2,3,2)$ in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ has image of rank one and coefficient array
$$
\tfrac14\begin{pmatrix}5&2&3&-12\\-12&3&-2&-5\\3&0&-13&-2\\2&13&0&3\end{pmatrix},
$$
of rank four: the determinant of this integer array is $-33124$, so the array, one quarter of it, has determinant $-33124/256\neq0$ and rank four by inspection. The four terms are minimal, and the array is exact, so the example does not rest on a numerical tolerance. **The length of an operator is therefore not bounded by any function of the rank of its image**: the smallest general bound, four, is already needed on the stratum of image rank one.

**The transpose and the conjugation are one phenomenon.** In the canonical frame the transpose fixes $e_t,\vec e_x,\vec e_z$ and negates $\vec e_y$, while the conjugation negates the three imaginary units and fixes $e_t$. Both are signed diagonal maps, and both have arrays of rank four. The transpose is the subject of *The Transposition of the Two Sides*, and *$M_2(\mathbb{C})$ Pauli Representation : Operators*, §*The Transpose*, proves that it needs four pairs and no fewer.

## The Ladder

**The strata.** The set of operators of length at most $r$ is the inverse image under the linear isomorphism $c$ of the determinantal variety of the arrays of rank at most $r$, whose complex dimension is $2r\cdot4-r^2=8r-r^2$. The values at $r=0,1,2,3,4$ are the whole ladder.

| $r$ | $\dim\{M:\ell(M)\le r\}$ | the set |
|---|---|---|
| $0$ | $0$ | the zero operator |
| $1$ | $7$ | the cone of products, the Segre cone |
| $2$ | $12$ | the sums of two products |
| $3$ | $15$ | a hypersurface, the complement of the open set of length four |
| $4$ | $16$ | the whole ambient |

**Every value occurs.** Each $r$ from zero to four is the length of some operator, because a $4\times4$ array of rank $r$ exists for each $r$: take the array with $r$ ones down the diagonal.

**The increments.** The ladder grows by $7,5,3,1$. The last increment is the single condition $\det c\neq0$: the set of operators of length at most three is closed, and its complement, the set of length four, is open.

**What the ladder forbids.** A bound of the form $\ell(M)\le f(\operatorname{rank}M)$ with $f(1)\le3$ is false: the projection onto the scalar line has image rank one and length four. No bound that grows with the image rank is available either, because the rank-one operators of length four are dense in the rank-one stratum, so the length is four on almost every rank-one operator.

## The Null Cone of Label Two

**The four blocks.** The left index of the array runs over the scalar line $e_t$ and the vector triple $e_x,e_y,e_z$, and so does the right index. The array therefore splits into four blocks: the corner $(t,t)$ of one entry, the two arms $(i,t)$ and $(t,j)$ of three entries each, and the vector square $(i,j)$ of nine.

**Proposition (the four blocks are invariant).** Let $\tilde U$ be invertible and let $\Phi=L_{\tilde U}R_{\tilde U^{-1}}$, the conjugation $\tilde X\mapsto\tilde U\tilde X\tilde U^{-1}$. Let $\mathsf R$ be the matrix of that conjugation on the vector triple, $\tilde U e_i\tilde U^{-1}=\sum_k\mathsf R_{ki}e_k$. Then
$$
c\bigl(\Phi M\Phi^{-1}\bigr)=\operatorname{diag}(1,\mathsf R)\,c(M)\,\operatorname{diag}(1,\mathsf R)^{\mathsf T}.
$$
Each block is carried into itself, the factor is complex orthogonal of determinant one, and the length is constant on the orbit.

*Proof.* On a basis product, $\Phi T_{\mu\nu}\Phi^{-1}=T_{\tilde Ue_\mu\tilde U^{-1},\,\tilde Ue_\nu\tilde U^{-1}}$. The element $e_t$ is central, so the scalar slot is fixed and the vector slot is carried by $\mathsf R$; hence the diagonal form. The algebra automorphism preserves the trace, so the scalar part of an element is preserved and $\mathsf R$ acts inside the vector triple, and it preserves the norm form $\tilde v\bar{\tilde v}$, so $\mathsf R^{\mathsf T}\mathsf R=I$; the determinant is one because the conjugations form the connected group $SO(3,\mathbb{C})$. Congruence by invertible factors preserves the rank, hence, by the theorem on the length, the length. Checked on ten complex units: the residual of the congruence is $4\cdot10^{-14}$, and the entries outside a block vanish to the same order.

**The length inside a block.** An element whose array is supported in one block has the length of that block, since the rank of a matrix with support in one block is the rank of the block.

| block | entries | shape | lengths |
|---|---|---|---|
| the corner $(t,t)$ | $1$ | $1\times1$ | $1$ |
| the left arm $(i,t)$ | $3$ | $3\times1$ | $1$ |
| the right arm $(t,j)$ | $3$ | $1\times3$ | $1$ |
| the vector square $(i,j)$ | $9$ | $3\times3$ | $1,2,3$ |

**Corollary.** No element supported in a single block has length four. The maximum length inside a block is the number of rows or of columns that the block occupies, and only the vector square reaches three.

**The three pieces of the vector square.** A $3\times3$ block $B$ splits as
$$
B=\lambda I+A+S,\qquad \lambda=\tfrac13\operatorname{tr}B,\quad A^{\mathsf T}=-A,\quad S^{\mathsf T}=S,\quad \operatorname{tr}S=0,
$$
of dimensions $1,3,5$. The congruence preserves the three pieces: symmetry is carried by any $\mathsf R$, and the trace by the relation $\mathsf R^{\mathsf T}\mathsf R=I$. They are the three summands of the tensor square of the vector triple, $3\otimes3=1\oplus3\oplus5$, of labels $0,1,2$ by the rule of *The Clebsch–Gordan Decomposition of the Operators*.

**Theorem (the length of the label-two element).** Let $M$ be supported in the vector square with block $S$ symmetric, traceless and nonzero. Then $\ell(M)=\operatorname{rank}S$, and
$$
\ell(M)=2\iff\det S=0\iff\operatorname{tr}S^{3}=0\iff\text{the eigenvalues are }(\sigma,-\sigma,0)\text{ with }\sigma\neq0,
$$
and $\ell(M)=3$ otherwise.

*Proof.* The array is block diagonal with block $S$ and zeros elsewhere, so its rank is $\operatorname{rank}S$. A rank-one symmetric matrix is $c\,vv^{\mathsf T}$, of trace $c\,v^{\mathsf T}v\neq0$, so a traceless matrix has no rank one and the values are $0,2,3$. For a traceless symmetric matrix $\operatorname{tr}S^{3}=3\det S$, because $a^{3}+b^{3}+c^{3}=3abc$ when $a+b+c=0$. A vanishing determinant is a vanishing eigenvalue, and the trace zero then leaves the other two equal and opposite.

**Corollary (the skew part).** On the skew part the length is two: a nonzero skew $3\times3$ matrix has even rank, and rank two is the only possibility, since rank three is odd.

**The cone.** The elements of length two are the null cone of the label, cut by the single cubic $\operatorname{tr}S^{3}$ in the five coefficients of $S$. The cone has dimension four in the five-dimensional space, and its complement, where the length is three, is dense and open. Length three is the rule and length two is the exception.

**The reading.** The length is constant on each orbit and not on the label: label two carries both values, two on the cone and three off it, so the label alone does not determine the length. Nor is any label-two element a single product: length one would need a rank-one block, and the traceless condition forbids it, so the label costs one term at least. Over the real form $S$ is a traceless quadratic form on the vector triple, the cone is the set of the degenerate ones, and a rank-two point is a pair of planes.

## Two Lengths, Two Arrays

**The other decomposition.** *The SVD Decomposition of Endomorphisms of the Biquaternion Algebra* writes an endomorphism as a sum of rank-one endomorphisms $\mathcal P_{\tilde U,\tilde V}(\tilde X)=\tilde U\langle\tilde X,\tilde V\rangle_{*}$, with weights $\rho_1\ge\dots\ge\rho_4\ge0$, and the number of terms is the number of nonzero weights, at most four. That count is the rank of the operator itself, read in a frame orthonormal for the Hermitian form, and it is a number attached to the map.

**The two arrays are different.** Both are arrays of the same operator, and neither is the other rewritten in another basis of one space: $c(M)$ is a tensor in $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$, written in the basis $e_\mu\otimes e_\nu$, while the other is the number attached to the map by a frame of four elements. The two spaces are different even though both have dimension sixteen, and the two ranks are unrelated: no inequality holds between them, and the table shows the two extreme disagreements.

| operator | the length, $\operatorname{rank}c$ | the operator rank |
|---|---|---|
| the identity | $1$ | $4$ |
| the projection onto the scalar line | $4$ | $1$ |
| a generic operator | $4$ | $4$ |

**Why they disagree.** The singular decomposition uses an orthonormal frame, in which the sixteen rank-one atoms are spread over the whole ambient; the multiplicative decomposition uses the products, which are a seven-dimensional cone inside it. An operator that is a single atom, such as the projection, is far from the cone; an operator that is a single product, such as the identity, is far from a single atom of the orthonormal frame. The two decompositions answer two different questions: how many orthogonal directions does the map use, and how many algebra multiplications does it take.

**The corpus sentence that the projection refutes.** It has been stated in the split category that the coefficient rank on operators of image rank one takes the values one and two only. The example of that statement, the map $\tilde X\mapsto(x_t+2x_x+3x_y+4x_z)e_t$, is right: it has image rank one and length two. The generalisation from it is wrong, and the projection onto the scalar line refutes it. The refutation stays inside the split category, because the projection there has the array $\tfrac14\operatorname{diag}(1,1,1,-1)$, of rank four, as §*The Split Category* displays. *$M_2(\mathbb{R})$ Standard Representation : Operators* now states the corrected form: the rank of the array is not bounded by a function of the rank of the image, and the length four is attained on the rank-one stratum.

## How a Decomposition Is Found

**The factorisation.** The proof of the theorem is constructive. Compute the array $c(M)$, write it as a sum of $r=\operatorname{rank}c(M)$ outer products $u_kv_k^{\mathsf T}$, read each $u_k$ and each $v_k$ as the coefficient vector of an element, and sum the $r$ products. The steps are the steps of a rank factorisation of an array, and they cost nothing beyond the array.

**The decomposition is not unique.** A factorisation $c=\sum_k u_kv_k^{\mathsf T}$ can be replaced by $c=\sum_k (Gu)_k(G^{-1}v)_k^{\mathsf T}$ for every invertible $r\times r$ array $G$, and the two factorisations give different decompositions of the same operator. The set of decompositions of an operator of length $r$ is therefore a stratum and not a point: the gauge group $\mathrm{GL}_r(\mathbb{C})$ acts on the terms. Two facts follow. The four terms of a decomposition are not determined by the operator, and a question about *the* terms of a decomposition is a question about a choice.

**The balanced choice.** The singular value decomposition of the array, $c=U\Sigma W^{\dagger}$, fixes the gauge up to phases and permutations: with $U$ and $W$ unitary, the terms $L_{\tilde Q_k}R_{\tilde P_k}$ with $\tilde Q_k$ read off the $k$-th vector of $U\Sigma$ and $\tilde P_k$ off the $k$-th vector of $W^{\dagger}$ carry the singular values once each. This is the natural normal form of the decomposition, and it is the one a computation produces.

**A caution on the minimality.** The factorisation gives the smallest number of terms only when the array is factored at its rank. A factorisation at the full size four gives four terms for every operator, including the identity, and the identity is one term.

**Nothing is required of the multipliers.** The multipliers of a decomposition may be zero divisors, and often are. The four terms of the conjugation are $-\tfrac12T_{\mu\mu}$, each of which has operator rank four and is invertible, and their sum has no invertible structure of its own. Conversely, a product with two non-invertible multipliers is still a product, of length one. In $\mathbb{B}\cong M_2(\mathbb{C})$ the two classes coincide, because an element is a zero divisor exactly when its $2\times2$ image is singular: every nonzero element is either invertible or a zero divisor, so no third case exists. The length counts terms, not the quality of the terms.

## What the Length Is Not

**It is not the operator rank.** The identity has operator rank four and length one; the projection onto the scalar line has operator rank one and length four. The two numbers are independent, and the two examples give both directions.

**It is not the rank of the element.** The rank of an element is the rank of its $2\times2$ image, a number between zero and two. The length is a property of an operator and the rank of an element is a property of an element: the identity operator has length one and the unit has rank two.

**It is not invertibility.** A product of two units is invertible and has length one; the conjugation is invertible and has length four.

**It is not unique.** The gauge group of the previous section acts on the terms, so a decomposition is a stratum and not a point.

**It is not additive.** The products are a cone and not a subspace: the sum of two products is a product only when the two arrays share a factor, and in general two arrays of rank one add to an array of rank two. The length is not a linear invariant, and the strata are determinantal varieties and not subspaces. Nor is the length bounded below by the lengths of the summands: two operators of length four can add to an operator of length two, as the companion article shows with two coordinate truncations.

**It is submultiplicative.** Since a product composes with a product into a product, a sum of $k$ products composed with a sum of $m$ products is a sum of $km$ products, so
$$
\ell(MN)\le\ell(M)\,\ell(N).
$$
The bound of sixteen is never attained by generic operators, and the composition of two generic operators of length four has length four: when $M$ is invertible as an operator the map $N\mapsto MN$ is a linear bijection of the ambient, so it carries the dense open set $\{\ell=4\}$ to itself. The bound holds and is far from sharp.

## The Real-Linear Boundary

**What the products span over the reals.** Each $T_{\mu\nu}$ is complex-linear, so the real span of the sixteen products contains their complex combinations, of real dimension thirty-two, and nothing more:
$$
\dim_{\mathbb{R}}\operatorname{span}_{\mathbb{R}}\{T_{\mu\nu}\}=32\quad\text{out of}\quad\dim_{\mathbb{R}}\operatorname{End}_{\mathbb{R}}(\mathbb{B})=64 .
$$

**The consequence for the claim.** *Endomorphism* in the theorem means complex-linear. A general real-linear map is not a sum of four products: the sums of four complex-linear products are exactly the complex-linear maps of length at most four, which is the whole of the thirty-two-dimensional space, and no real-linear map outside it is reached.

**The bound over the reals.** Write $J$ for the multiplication by $i$, a real-linear map. Every real-linear $F$ splits as $F=\tfrac12(F-iFi)+\tfrac12(F+iFi)$, and the two pieces are complex-linear and complex-antilinear. The antilinear piece is $N\circ J$ with $N$ complex-linear, so it is a sum of at most four products composed with $J$. Hence every real-linear endomorphism is a sum of at most eight terms drawn from the two families $\{T_{\mu\nu}\}$ and $\{T_{\mu\nu}J\}$, and a general one needs eight, because for a general real-linear map both the linear and the antilinear part are of length four, and the split is unique.

**The operators that stay inside the bound.** Every complex-linear operator the category writes on the algebra falls under the bound: the quaternion conjugation $\natural$, the transposes of the frames, the Peirce corner projections, the adjoint $\mathrm{Ad}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{-1}}$, the Hermitian pair $L_{\tilde Q}R_{\tilde Q^{*}}$, which is complex-linear because the second slot is a fixed element. The dagger and the star are conjugate-linear, so they are not endomorphisms of the complex vector space at all: they are read in the corpus as ties and as forms, and when one is treated as a map it lies in the second family $\{T_{\mu\nu}J\}$.

## The Split Category

**The same theorem, a different algebra.** The split algebra $\mathbb{B}_{\mathrm{spl}}$ is $M_2(\mathbb{R})$ in the Pauli dictionary, and the theorem holds with the same proof and the same bound: $\mathbb{B}_{\mathrm{spl}}\otimes\mathbb{B}_{\mathrm{spl}}^{\mathrm{opp}}\cong M_4(\mathbb{R})$, the sixteen products are a basis, and the length is the rank of the array. The algebra is split and not a division algebra, and that difference does not enter the theorem, which uses only the dimension and the centrality.

**The same witnesses, with other signs.** The conjugations of the split category differ from those of the biquaternion category, so the arrays of the same operators differ, and the ranks do not. The projection onto the scalar line has the array $\tfrac14\operatorname{diag}(1,1,1,-1)$, of rank four, and the length four. The conjugation has the array $\tfrac12\operatorname{diag}(-1,1,1,-1)$, of rank four: the same operator carries a different array and the same length, because the four diagonal products distribute their signs differently across the four coordinates. The rank-one operator of length four exists with rational entries there too.

## Summary

Every complex-linear endomorphism of the biquaternion algebra is a sum of at most four two-sided operators $L_{\tilde Q_1}R_{\tilde Q_2}$, and four is exact.

The number of terms is the rank of one $4\times4$ array, the array of the operator in the sixteen basis products; the array is canonical because the products are orthogonal for the Hilbert–Schmidt form, with squared norm four.

The bound holds because the sixteen products are linearly independent, which is $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ read on the sixteen tensor products of a basis; it is sharp because $\det c=0$ is the condition for three terms, a hypersurface.

Four is attained by the quaternion conjugation, which is $-\tfrac12\sum_\mu L_{e_\mu}R_{e_\mu}$; by the projection onto the scalar line, whose image is a line; by the transpose of the model; and by every operator off a hypersurface.

The theorem is about $\operatorname{End}_{\mathbb{C}}(\mathbb{B})=M_4(\mathbb{C})$ and not about the module endomorphisms $\mathbb{B}^{\mathrm{opp}}$, of dimension four; over the reals the products span thirty-two of sixty-four dimensions, and a general real-linear map needs eight terms.

Inside a block of the array the length is the rank of that block, so no element supported in one block has length four; inside the vector square the length is the rank of a $3\times3$ matrix, and on the traceless symmetric part, the label two, it is two exactly on the null cone $\det S=0$ and three off it.

The four of this article is not the four of the singular decomposition. The two decompositions use two different arrays, and they disagree at the two most elementary operators: the identity is one product and four atoms, the projection onto the scalar line is four products and one atom.

## Summary of Notation

| symbol | meaning | article |
|---|---|---|
| $\mathbb{B}$ | the biquaternion algebra, basis $e_t,\vec e_x,\vec e_y,\vec e_z$ | *Algebra and Element Conventions* |
| $L_{\tilde Q}$, $R_{\tilde Q}$ | left and right multiplication | *Operator Family Conventions* |
| $L_{\tilde Q_1}R_{\tilde Q_2}$ | the two-sided operator $\tilde X\mapsto\tilde Q_1\tilde X\tilde Q_2$ | *Operators Acting on Two Sides* |
| $T_{\mu\nu}$ | $L_{e_\mu}R_{e_\nu}$, the sixteen basis products | this article |
| $c(M)$ | the coefficient array, $c_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{\dagger}M)$ | *The Length and the Two Ranks on $M_n(\mathbb{C})$* |
| $c_{\tilde Q}$ | the coefficient vector of an element, so that $c(L_{\tilde Q_1}R_{\tilde Q_2})=c_{\tilde Q_1}c_{\tilde Q_2}^{\mathsf T}$ | this article |
| $\ell(M)$ | the length, the least number of products | *The Length and the Two Ranks on $M_n(\mathbb{C})$* |
| $\natural$ | the quaternion conjugation | *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra* |
| $\operatorname{Sc}$ | the scalar part | *Algebra and Element Conventions* |
| $\operatorname{rank}$ | the rank of a family of vectors, hence of an array | *Algebra and Element Conventions* |
| $\mathcal P_{\tilde U,\tilde V}$ | the unweighted rank-one endomorphism of the singular decomposition | *The SVD Decomposition of Endomorphisms of the Biquaternion Algebra* |
| $\rho_k$ | the weights of the singular decomposition | *The SVD Decomposition of Endomorphisms of the Biquaternion Algebra* |
| $\mathsf R$ | the matrix of the conjugation $\tilde X\mapsto\tilde U\tilde X\tilde U^{-1}$ on the vector triple | this article |
| $B=\lambda I+A+S$ | the vector square of the array, split into trace, skew and traceless symmetric parts | this article |

## Further Reading

- [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html), for the bound of four pairs at the element size and the proof that the transpose needs four.
- [The Length and the Two Ranks on $M_n(\mathbb{C})$](the-length-and-the-two-ranks-on-mnc.html), for the theorem that the length is the array rank at every $n$, and for the determinantal strata.
- [The Length and the Two Ranks at $n=4$](the-length-and-the-two-ranks-at-n-4.html), for the same theorem at the size of this algebra, and for an operator of rank three.
- [The Two-Sided Operators and the Segre Cone at $n=4$](the-two-sided-operators-and-the-segre-cone-at-n-4.html), for the rank-one criterion, the cone, and the orthogonality $\operatorname{tr}(T^{\dagger}T)=4\delta$.
- [$M_4(\mathbb{C})$ Axis-Free Representation : Operators](m4c-axis-free-representation-operators.html) and [$M_4(\mathbb{C})$ Pauli Representation : Operators](m4c-pauli-representation-operators.html), for the sixteen basis operators and the coefficient arrays in the two frames of the category.
- [The SVD Decomposition of Endomorphisms of the Biquaternion Algebra](the-svd-decomposition-of-endomorphisms-of-the-biquaternion-algebra.html), for the other decomposition, its weights, and the comparison with the products.
- [The Transposition of the Two Sides](the-transposition-of-the-two-sides.html), for the conversion between the one-sided families and the operator that the transpose of the model represents.
- [$M_2(\mathbb{R})$ Standard Representation : Operators](m2r-standard-representation-operators.html), for the split category and the corrected statement on the rank-one stratum.
