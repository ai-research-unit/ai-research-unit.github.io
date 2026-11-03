# __Introduction to the Operator Theory of the Biquaternion Algebra__

## Introduction

**The subject.** This article fixes the four levels at which the corpus reads an operator of the biquaternion algebra, and it states the dependence between them: the algebra product, the operators $L_{\tilde Q}$ and $R_{\tilde Q}$, the matrices of those operators in a chosen basis, and the coefficient array of an arbitrary endomorphism in the basis of the sixteen products. The four levels are stated here once, with the coefficient basis of Level 1 as the only named frame; the third level holds in any basis, and no basis is singled out.

**The thesis.** Matrix theory is a coordinate display of operator theory, and operator theory is a representation of the algebra product. Neither step is an identification. A matrix is never more than an operator written in a basis, and an operator is never more than the multiplication of the algebra read with one argument fixed. The order is therefore
$$
\text{algebra product}\;\longrightarrow\;\text{operators}\;\longrightarrow\;\text{matrices}\;\longrightarrow\;\text{coefficient arrays},
$$
and each arrow is a construction: the object on the right cannot be defined without the object on the left, and the object on the left is not changed by the choice made on the right.

**What each level adds, and what it costs.** Level 2 adds composition to the algebra product and stays basis-free. Level 3 adds the array, turns composition into a matrix product and makes the trace, the determinant, the spectrum and the rank available, and loses basis-independence: the same operator receives one matrix per basis. Level 4 adds the singular value decomposition and the length, and loses the identification of the object: its element is an endomorphism of the operator space and not an element of the algebra.

**The one-sided restriction.** The object of Level 2 is a single multiplier: one element fixes one argument of the product and the other argument is the variable. The matrices of Level 3 are therefore the matrices of *one-sided* operators, one matrix per element, and the two families are four-dimensional subalgebras of the ambient, each closed under addition and under composition and each the commutant of the other. That is the whole of the operator theory used here. Level 4 then addresses an arbitrary endomorphism of the ambient, which need not be a multiplier at all.

**Boundaries.** The algebra, its basis and its multiplication table are *The Biquaternion Algebra* and *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra*. The vocabulary of the operator families is *Operator Family Conventions*; the left and right multiplier families are *The Left Regular Operators on the Biquaternion Algebra* and *The Right Regular Operators on the Biquaternion Algebra*; and their commutant is *The Commutant of the Two Regular Families*. This article states the four levels and the dependency; it proves no property of a stratum, uses no form and no norm, and names no basis beyond the coefficient basis of Level 1.

## Level One: The Algebra Product

**The only primitive datum.** The algebra is
$$
\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H},
$$
with the basis
$$
\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)
$$
and the multiplication of the units
$$
e_\mu e_\nu=\varepsilon_{\mu\nu}^{\ \ \rho}e_\rho,
\qquad
\varepsilon_{\mu\nu}^{\ \ \rho}\in\{0,\pm 1\}.
$$
Explicitly, $e_t$ is the unit and
$$
\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t,\qquad
\vec e_x\vec e_y=-\vec e_y\vec e_x=\vec e_z,\qquad
\vec e_y\vec e_z=-\vec e_z\vec e_y=\vec e_x,\qquad
\vec e_z\vec e_x=-\vec e_x\vec e_z=\vec e_y .
$$
A direction index runs over $t,x,y,z$ in that order, and every index of this article is one of those four.

**Nothing else exists at this level.** There is no coordinate column, no matrix, no frame other than $\mathcal E$ taken as a set, and no identification of an element with an array. The symbol $M_4(\mathbb{C})$ has not appeared. The structure constants are the whole input of the three levels that follow, and every statement of those levels is a consequence of the table above and of the associativity of the product.

**What the product already decides.** The product is associative, its unit is $e_t$, its centre is the line $\mathbb{C}e_t$, and the algebra is central simple over $\mathbb{C}$. It is not a division algebra, because
$$
(e_t+i\vec e_x)(e_t-i\vec e_x)=e_t+i\vec e_x-i\vec e_x-i^2\vec e_x^2=e_t-(-1)(-e_t)=0 .
$$
The zero divisors matter at Level 3: an element with a nontrivial annihilator has a singular matrix in every frame.

**The element and its coordinates.** An element is
$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,
\qquad
Q_\mu\in\mathbb{C},
$$
and the four coefficients are complex numbers. They are the coordinates of $\tilde Q$ *in the frame $\mathcal E$*, and they are a display of the element in that frame; the element itself is the linear combination and carries no index.

## Level Two: The Operators

**The two multipliers.** For an element $\tilde Q$ define two maps of $\mathbb{B}$ into itself by
$$
L_{\tilde Q}(\tilde X)=\tilde Q\tilde X,
\qquad
R_{\tilde Q}(\tilde X)=\tilde X\tilde Q .
$$
Each is $\mathbb{C}$-linear, because the product is bilinear and the scalar field is central. Neither definition mentions a basis: the two use the product alone. At this level the objects are *maps*, and the law that carries information is composition; addition exists in the ambient, but no trace, determinant, spectrum or rank is defined there.

**On the units.** The two definitions agree on a product of two units while their left-hand sides differ:
$$
L_{e_\mu}(e_\nu)=e_\mu e_\nu,
\qquad
R_{e_\nu}(e_\mu)=e_\mu e_\nu .
$$
The right-hand side is one element of the algebra. The left-hand sides are two different operators, each applied to one basis element, and the coincidence of the right-hand sides is the whole content of the word *left* and *right*.

**The composition laws.** For all elements,
$$
L_{\tilde Q}\circ L_{\tilde P}=L_{\tilde Q\tilde P},
\qquad
R_{\tilde Q}\circ R_{\tilde P}=R_{\tilde P\tilde Q},
\qquad
L_{\tilde Q}\circ R_{\tilde P}=R_{\tilde P}\circ L_{\tilde Q}.
$$
The first identity says that $L$ is a representation of the algebra; the second that $R$ is an anti-representation, the order of the parameters being reversed; the third that every left multiplier commutes with every right multiplier. The three are the associative law read in three ways. The anti-law is $(\tilde X\tilde P)\tilde Q=\tilde X(\tilde P\tilde Q)$ read with the outermost factor on the left, and the commutation is $\tilde Q(\tilde X\tilde P)=(\tilde Q\tilde X)\tilde P$ read with the two factors separated.

**Injectivity, kernel and image.** $L_{\tilde Q}=0$ exactly when $\tilde Q=0$, because $L_{\tilde Q}(e_t)=\tilde Q$; and the same test gives $R_{\tilde Q}=0$ exactly when $\tilde Q=0$. The kernels and the images are the two annihilators and the two ideals:
$$
\ker L_{\tilde Q}=\{\tilde X:\tilde Q\tilde X=0\},
\qquad
\operatorname{im}L_{\tilde Q}=\mathbb{B}\tilde Q,
\qquad
\ker R_{\tilde Q}=\{\tilde X:\tilde X\tilde Q=0\},
\qquad
\operatorname{im}R_{\tilde Q}=\tilde Q\mathbb{B}.
$$

**The two families as subspaces.** The left multipliers form the set $\operatorname{End}_L(\mathbb{B})$ and the right multipliers the set $\operatorname{End}_R(\mathbb{B})$, both inside the ambient $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ of complex dimension $16$. By injectivity each set is a complex subspace of dimension $4$, the two meet in the line of the identity,
$$
\operatorname{End}_L(\mathbb{B})\cap\operatorname{End}_R(\mathbb{B})=\mathbb{C}\cdot\mathrm{I}_4,
$$
they span $4+4-1=7$ dimensions together, and each is the commutant of the other,
$$
\operatorname{End}_L(\mathbb{B})'=\operatorname{End}_R(\mathbb{B}),
\qquad
\operatorname{End}_R(\mathbb{B})'=\operatorname{End}_L(\mathbb{B}).
$$
The four identities of the preceding paragraph are therefore a statement about two subalgebras and not about two lists of maps.

## Level Three: The Matrices

**The coordinate column.** The frame $\mathcal E$ gives the linear isomorphism
$$
[\cdot]_{\mathcal E}:\mathbb{B}\longrightarrow\mathbb{C}^4,
\qquad
[\tilde Q]_{\mathcal E}=(Q_t,Q_x,Q_y,Q_z)^{\mathsf T},
\qquad
[e_\mu]_{\mathcal E}=\epsilon_\mu,
$$
with $\epsilon_\mu$ the $\mu$-th standard column. The column is a display of the element in the frame, and the element is not the column.

**The matrix of an operator.** For $F\in\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ the matrix $[F]_{\mathcal E}$ is the unique $4\times 4$ matrix with
$$
[F(\tilde X)]_{\mathcal E}=[F]_{\mathcal E}\,[\tilde X]_{\mathcal E}
\qquad\text{for every }\tilde X .
$$
Equivalently, its columns are the coordinate columns of the images of the basis elements:
$$
[F]_{\mathcal E}\,\epsilon_\mu=[F(e_\mu)]_{\mathcal E}.
$$

### The Matrix Families

**Two constructions, and two only.** The matrices of the elements are built by two constructions, side by side and independent of one another. Each takes an element and a basis and returns a matrix; each uses the product of Level 1 and nothing else; neither is derived from the other.

**The left construction.** Let $\mathcal B=(f_0,f_1,f_2,f_3)$ be a basis of $\mathbb{B}$, with coordinate column $[\cdot]_{\mathcal B}$. The **left matrix** of an element $\tilde Q$ in the basis $\mathcal B$ is the unique matrix defined by
$$
L^{\mathcal B}(\tilde Q)\,\epsilon_\nu=[\tilde Q f_\nu]_{\mathcal B},
\qquad \nu=0,1,2,3 .
$$
The fixed factor stands in front. Nothing enters the definition but the product, the basis and the coordinate column.

**The right construction.** The **right matrix** of the same element in the same basis is defined by the other column rule,
$$
R^{\mathcal B}(\tilde Q)\,\epsilon_\nu=[f_\nu\tilde Q]_{\mathcal B},
\qquad \nu=0,1,2,3 .
$$
The fixed factor stands behind. The two rules read the same product with the fixed argument on either side, and neither rule mentions the other matrix.

**A basis produces a pair, and nothing more.** For a fixed basis the level returns one matrix of each kind per element, and the shorthand of the article is
$$
L(\tilde Q):=L^{\mathcal E}(\tilde Q),
\qquad
R(\tilde Q):=R^{\mathcal E}(\tilde Q),
\qquad
L_{e_\mu}:=L(e_\mu),
\qquad
R_{e_\nu}:=R(e_\nu),
$$
the basis $\mathcal E$ being the one named in the article. The columns of $L(\tilde Q)$ are the coordinate columns of $\tilde Qe_\nu$ and those of $R(\tilde Q)$ are the coordinate columns of $e_\nu\tilde Q$; the assignment $\tilde Q\mapsto L(\tilde Q)$ is injective because $L$ is. The output of the level is thus not a matrix attached to an element, but two families of matrices indexed by the bases of $\mathbb{B}$.

**The product becomes a matrix product.** The composition laws of Level 2 become, in the basis $\mathcal B$, the product laws of Level 3:
$$
L^{\mathcal B}(\tilde Q\tilde P)=L^{\mathcal B}(\tilde Q)L^{\mathcal B}(\tilde P),
\qquad
R^{\mathcal B}(\tilde Q\tilde P)=R^{\mathcal B}(\tilde P)R^{\mathcal B}(\tilde Q),
\qquad
L^{\mathcal B}(\tilde Q)R^{\mathcal B}(\tilde P)=R^{\mathcal B}(\tilde P)L^{\mathcal B}(\tilde Q).
$$
This is the whole gain of the level: a composition of maps is read as a product of arrays, and the order of the factors is preserved on the left and reversed on the right. The laws hold in every basis, and the arrays satisfying them are carried from one basis to the next by the conjugation below.

**The matrix $S$ between two families.** Let $\mathcal B'=(f'_0,\dots,f'_3)$ be a second basis, and let $S\in GL_4(\mathbb{C})$ be the change of basis, its $\nu$-th column being the coordinate column of $f'_\nu$ in $\mathcal B$:
$$
f'_\nu=\sum_\mu S_{\mu\nu}f_\mu,
\qquad
S\epsilon_\nu=[f'_\nu]_{\mathcal B},
\qquad
[x]_{\mathcal B'}=S^{-1}[x]_{\mathcal B}.
$$
Then, for every element $\tilde Q$,
$$
L^{\mathcal B'}(\tilde Q)=S^{-1}L^{\mathcal B}(\tilde Q)\,S,
\qquad
R^{\mathcal B'}(\tilde Q)=S^{-1}R^{\mathcal B}(\tilde Q)\,S .
$$
The proof is one line from the column rule: applying $S^{-1}$ to $L^{\mathcal B}(\tilde Q)\epsilon_\nu=[\tilde Qf_\nu]_{\mathcal B}$ gives $S^{-1}L^{\mathcal B}(\tilde Q)\epsilon_\nu=[\tilde Qf_\nu]_{\mathcal B'}$, while $f'_\nu$ and $S^{-1}\epsilon_\nu$ are one and the same column of the new basis; the two sides therefore agree on the four columns. The same line, with the column rule of $R$, gives the right-hand identity.

**One orbit.** The two formulas say that a change of basis conjugates the whole pair at once. The set of the matrix families, indexed by the bases, is therefore a single orbit of $GL_4(\mathbb{C})$ acting by simultaneous conjugation,
$$
(L,R)\longmapsto\bigl(S^{-1}LS,\,S^{-1}RS\bigr),
$$
and no basis is distinguished: the families differ by a matrix multiplication on the left and by its inverse on the right, and by nothing else. This is the exact sense in which the matrices of the algebra are obtained only up to a matrix multiplication.

**What the conjugation carries.** The quantities that are the same in every basis are the properties of the operators:
$$
\text{the operators }L_{\tilde Q},R_{\tilde Q},
\qquad
\operatorname{Tr}L(\tilde Q)=\operatorname{Tr}R(\tilde Q)=4Q_t,
$$
together with the determinant, the spectrum, the characteristic and the minimal polynomials and the rank of each, the two copies $\mathbb{B}_L=L(\mathbb{B})$ and $\mathbb{B}_R=R(\mathbb{B})$ as subalgebras with their intersection, their commutants and their dimensions, the commutation $L(\tilde Q)R(\tilde P)=R(\tilde P)L(\tilde Q)$, and the two types, $L$ a representation and $R$ an anti-representation. None of them is touched by a conjugation.

**What the conjugation moves.** The quantities that change with the basis are the display:

| Carried by the operator | Carried by the display |
|---|---|
| the operators, their trace, determinant, spectrum and rank | the entries |
| the two copies as subalgebras, their intersection and their commutants | the sparsity pattern of the arrays |
| the laws $L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P}$ and $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$ | the ring generated by the entries |
| the product and the anti-product | the subspaces $\mathbb{B}_L^{\mathcal B}=L^{\mathcal B}(\mathbb{B})$ and $\mathbb{B}_R^{\mathcal B}=R^{\mathcal B}(\mathbb{B})$ of $M_4(\mathbb{C})$, equal as algebras and conjugated as subsets |

The subspaces of the last row are the clearest case: they are the same two algebras in every basis, and different subsets of $M_4(\mathbb{C})$ in every basis. The coefficient matrix of Level 4 belongs to the right-hand column as well, and it moves by a congruence and not by a conjugation: the two transformations are distinct, and the length survives the first because the first preserves the rank.

**Why two families, and why the ambient needs both.** A single family does not reach the ambient: the products $L^{\mathcal B}(\tilde Q)$ alone form the four-dimensional copy $\mathbb{B}_L$, and the products $R^{\mathcal B}(\tilde P)$ alone form $\mathbb{B}_R$. The elementary operators of the ambient are the products of one of each, $L^{\mathcal B}(\tilde Q)R^{\mathcal B}(\tilde P)$, and every endomorphism is a sum of at most four of them. The reason is the singular value decomposition of Level 4: the coefficient array of an endomorphism is a $4\times 4$ array, its rank $r$ is at most four, and the SVD writes it as a sum of $r$ rank-one terms $u_iw_i^{\mathsf T}$, each of which is the coefficient array of one product $L(\tilde Q_i)R(\tilde P_i)$. The number of terms is the length, the singular values are weights attached to the display, and only their count is a property of the operator.

### The Two Writings and the Rule That Keeps Them Apart

**The two writings.** The same data are written twice, and the two writings are not interchangeable:
$$
\text{operator writing: } L_{e_\mu}(e_\nu)=e_\mu e_\nu,
\qquad
\text{matrix writing: } L_{e_\mu}\epsilon_\nu=[e_\mu e_\nu]_{\mathcal E}.
$$
Both lines say that the left multiplier of the $\mu$-th unit sends the $\nu$-th unit to the product of the two. The first applies an operator to an element and returns an element. The second applies a matrix to a column and returns a column.

**The rule.** The three symbols $L_{e_\mu}(e_\nu)$, $L_{e_\mu}\epsilon_\nu$ and $L(e_\mu)e_\nu$ are not three notations for one thing: the third is meaningless. It applies a matrix to an element of the algebra, and the product of a $4\times 4$ array with a linear combination of the units is not defined; the two live in different spaces and the only bridge between them is the bracket $[\cdot]_{\mathcal E}$. An article that writes $L_{e_\mu}\epsilon_\nu$ has passed to the matrices, and an article that writes $L_{e_\mu}(e_\nu)$ has not.

**The four glyphs.** The corpus keeps four:

| Glyph | Object | Carries |
|---|---|---|
| $L_{\tilde Q}$ | the operator | no frame |
| $[F]_{\mathcal B}$ | the matrix of a general operator | its basis $\mathcal B$, always written |
| $L(\tilde Q)$ | the matrix of a left multiplier | the frame named in the article |
| $L_{e_\mu}$ | the matrix of a basis element | the frame named in the article |

The bracket carries a frame and never omits it; a matrix written without its frame is the matrix of no operator.

**A matrix is not an element.** The ambient $M_4(\mathbb{C})=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ carries no biquaternion structure: it is the algebra of endomorphisms of the coordinate space. The matrices of elements form the four-dimensional subspace $\mathbb{B}_L=L(\mathbb{B})$, and the twelve complementary dimensions are endomorphisms that are not multiplications by an element.

**The cost of the level.** The operator is the invariant object and the array is the display: one operator, one matrix per basis, and the conjugation of §*The Matrix Families* is the price of the passage. The matrix of a general operator follows the same rule,
$$
[F]_{\mathcal E'}=S^{-1}[F]_{\mathcal E}S .
$$

**What a matrix buys.** Addition of operators is available at Level 2, in the ambient space, but multiplication written as an array, the trace, the determinant, the spectrum, the rank and the system of linear equations are not. Each of them is a statement about the operator read through a frame, and each is either invariant under the change of frame, as the trace, the determinant, the spectrum and the rank are, or a property of the display alone, as an entry is.

## Level Four: The Coefficient Matrix

**The sixteen products.** An endomorphism of the ambient need not be a multiplication by an element; the ambient is nevertheless spanned by products of multipliers. The products of one left and one right basis matrix,
$$
B_{\mu\nu}=L_{e_\mu}R_{e_\nu},
$$
are sixteen matrices, and they are a basis of the ambient $M_4(\mathbb{C})$. In the frame $\mathcal E$ they are orthogonal for the transpose pairing,
$$
\operatorname{Tr}\bigl(B_{\mu\nu}^{\mathsf T}B_{\rho\sigma}\bigr)=4\,\delta_{\mu\rho}\delta_{\nu\sigma},
$$
and the same sixteen arrays, in any frame, are linearly independent because the frame change is an invertible conjugation and linear independence is preserved.

**The coefficient array.** Every endomorphism has therefore a unique expansion
$$
M=\sum_{\mu\nu}c_{\mu\nu}(M)\,B_{\mu\nu},
$$
and the array $c(M)=(c_{\mu\nu}(M))$ is the **coefficient matrix** of $M$. In the frame $\mathcal E$, where the sixteen are orthogonal, the coefficients are the traces
$$
c_{\mu\nu}(M)=\tfrac14\operatorname{Tr}\bigl(B_{\mu\nu}^{\mathsf T}M\bigr),
$$
while in another basis they are read from the Gram matrix of the sixteen, and the congruence stated below holds for them. The map $c$ is a linear isomorphism of $M_4(\mathbb{C})$ onto itself and it is not an algebra map.

**Why a fourth level.** The coefficient matrix is the array of an endomorphism of the sixteen-dimensional operator space in the basis of the sixteen products. It is a second coordinate layer, above the matrix: $M$ displays an operator of $\mathbb{B}$ in a frame of $\mathbb{B}$, while $c(M)$ displays $M$ itself in a frame of the operator space. The two are easily confused, and the confusion is the source of the false sentence "$E_{11}$ has length four": the entry $E_{11}$ is an array at Level 3, while a length is a property of an operator at Level 4.

**The length.** The **length** $\ell(M)$ is the least number of products $L(\tilde Q)R(\tilde P)$ summing to $M$, with $\ell(0)=0$. The coefficient array of one product is $[Q][P]^{\mathsf T}$, of rank one, and conversely every rank-one array is of that form. A sum of $r$ products therefore has coefficient rank at most $r$, and a rank factorisation of a coefficient array of rank $r$ reads off $r$ pairs. Hence
$$
\ell(M)=\operatorname{rank}c(M)\in\{0,1,2,3,4\},
$$
and $\ell(M)=4$ exactly when $\det c(M)\neq0$.

**The singular value decomposition.** The decomposition of the fourth level is the SVD of the coefficient array,
$$
c(M)=\sum_{i=1}^{r}\sigma_i\,u_iw_i^{\mathsf T},
\qquad
r=\operatorname{rank}c(M)\le 4,
$$
and it reads, through the construction, a decomposition of the operator:
$$
M=\sum_{i=1}^{r}\sigma_i\,L(\tilde Q_i)R(\tilde P_i),
$$
where $\tilde Q_i$ and $\tilde P_i$ are the elements whose coordinate columns are $u_i$ and $w_i$. The number of terms is the length, and the singular values are weights; the SVD says nothing about Levels 1 to 3 directly, it says that the rank of a coordinate array is the number of one-sided factors of the operator behind it. The rank is the invariant of the construction, the weights are not: the change of basis of the coefficient array is a congruence (§*The Matrix Families*), and a congruence preserves the rank and moves the singular values.

**The change of basis is a congruence.** Let $f_\alpha=\sum_\mu C_{\mu\alpha}e_\mu$ be another basis of the algebra, and let $c'$ be the coefficient array in the products of the new basis. Then
$$
c'(M)=C^{-1}c(M)\,C^{-\mathsf T},
$$
a congruence, so $\operatorname{rank}c'(M)=\operatorname{rank}c(M)$ and the two bases return one length. The rank of the coefficient array is a property of the operator and not of the frame; the array itself is not.

**What the fourth level does not say.** An array has no length of its own: it displays an operator in the frame at hand, and the same array in two frames names two operators whose lengths may differ. The invariance above is the invariance of the operator's length, not of the array's.

## The Dependency Chain

**The chain.** The four levels and the construction that carries one to the next:

| Level | Object | Construction from the level above |
|---|---|---|
| $1$ | the algebra product on $\mathbb{B}$, structure constants $\varepsilon_{\mu\nu}^{\ \ \rho}$ | the input |
| $2$ | the operators $L_{\tilde Q}$, $R_{\tilde Q}$ on $\mathbb{B}$ | fix one argument of the product |
| $3$ | the matrices $L(\tilde Q)$, $R(\tilde Q)$ in $M_4(\mathbb{C})$ | choose a basis of $\mathbb{B}$ |
| $4$ | the coefficient array $c(M)$ in $M_4(\mathbb{C})$ | choose the basis $B_{\mu\nu}=L_{e_\mu}R_{e_\nu}$ of the ambient |

Every arrow is a construction and not an identity. $L(\tilde Q)$ cannot be written before $\mathcal E$ is chosen, $c(M)$ cannot be written before the sixteen products exist, and the sixteen products cannot exist before the four units $e_\mu$ and the product are given.

**The two-step answer.** The statement *matrix theory is based on operator theory* is the composite of two steps: a matrix is a coordinate representation of an operator, and an operator is a representation of the algebra product. The order is therefore algebra, then operators, then matrices, then coefficient arrays, and at each step the objects gain new operations and lose basis-independence: composition and its two laws at Level 2, the matrix product, the trace, the determinant, the spectrum and the rank at Level 3, the length and the singular value decomposition at Level 4.

**The two copies and the ambient.** The left multipliers alone give the four-dimensional copy $\mathbb{B}_L=L(\mathbb{B})$, the right multipliers alone give $\mathbb{B}_R=R(\mathbb{B})$, and the sixteen products of one of each give the ambient. The matrices of elements are the matrices of the two copies; the ambient is reached only at Level 4, where the object is an arbitrary endomorphism and no longer an element.

## Summary

The corpus reads an operator at four levels. Level 1 is the algebra product and its structure constants, the only primitive datum. Level 2 is the pair of multipliers $L_{\tilde Q}(\tilde X)=\tilde Q\tilde X$ and $R_{\tilde Q}(\tilde X)=\tilde X\tilde Q$, basis-free maps with the laws $L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P}$, $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$ and $L_{\tilde Q}R_{\tilde P}=R_{\tilde P}L_{\tilde Q}$. Level 3 is the coordinate column and the matrix of an operator in a chosen basis, where composition becomes multiplication and where the trace, the determinant, the spectrum and the rank become available. Level 4 is the coefficient array of an endomorphism in the sixteen products, where the length is the rank and the singular value decomposition counts the one-sided factors.

Each arrow is a construction: matrix theory is the coordinate display of operator theory, and operator theory is the algebra product read with one argument fixed. The two one-sided families are four-dimensional subalgebras meeting in the identity line, spanning seven dimensions together and each the commutant of the other. The matrices of elements are those of the one-sided operators, and they are defined only up to a change of basis: all the matrix families of the two kinds form one orbit of $GL_4(\mathbb{C})$ under simultaneous conjugation by the change-of-basis matrix $S$, so that a family is fixed only up to a matrix multiplication on the left and its inverse on the right, while the trace, the determinant, the spectrum, the rank and the two copies as subalgebras are fixed outright. Level 4 leaves the element behind and arrays an arbitrary endomorphism of the ambient.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ | the coefficient basis, the only frame of Level 1 |
| $\varepsilon_{\mu\nu}^{\ \ \rho}$ | the structure constants, $e_\mu e_\nu=\varepsilon_{\mu\nu}^{\ \ \rho}e_\rho$ |
| $L_{\tilde Q}$, $R_{\tilde Q}$ | the left and the right multiplier, $X\mapsto\tilde QX$ and $X\mapsto X\tilde Q$ |
| $\operatorname{End}_L$, $\operatorname{End}_R$ | the two one-sided families |
| $\operatorname{End}(\mathbb{B})=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ | the ambient, of complex dimension $16$ |
| $[\tilde X]_{\mathcal E}$ | the coordinate column of an element, $\epsilon_\mu$ that of $e_\mu$ |
| $[F]_{\mathcal E}$ | the matrix of an operator in the frame $\mathcal E$ |
| $L^{\mathcal B}(\tilde Q)$, $R^{\mathcal B}(\tilde Q)$ | the two matrix families in the basis $\mathcal B$ |
| $L(\tilde Q)$, $R(\tilde Q)$, $L_{e_\mu}$, $R_{e_\nu}$ | the same in the basis $\mathcal E$ of the article; the matrices of the units |
| $S$ | the change of basis; its $\nu$-th column is $[f'_\nu]_{\mathcal B}$, and $L^{\mathcal B'}=S^{-1}L^{\mathcal B}S$, $R^{\mathcal B'}=S^{-1}R^{\mathcal B}S$ |
| $B_{\mu\nu}=L_{e_\mu}R_{e_\nu}$ | the sixteen products, a basis of the ambient |
| $c(M)$ | the coefficient matrix; in the frame $\mathcal E$, $c_{\mu\nu}=\tfrac14\operatorname{Tr}(B_{\mu\nu}^{\mathsf T}M)$ |
| $\ell(M)$ | the length, the least number of one-sided factors; equal to $\operatorname{rank}c(M)$ |

## Further Reading

- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra, the multiplication table and the zero divisors.
- [The Element, the Coordinates and the Conjugations in the Biquaternion Algebra](the-element-the-coordinates-and-the-conjugations.html), for the element, its four coordinate systems and the conjugations.
- [Operator Family Conventions](operator-family-conventions.html), for the letters $L$ and $R$, the slots and the frames of the matrices.
- [The Left Regular Operators on the Biquaternion Algebra](the-left-regular-operators-on-the-biquaternion-algebra.html), for the left multiplier, its rank, its kernel and its spectrum.
- [The Right Regular Operators on the Biquaternion Algebra](the-right-regular-operators-on-the-biquaternion-algebra.html), for the right multiplier and the anti-law.
- [The Commutant of the Two Regular Families](the-commutant-of-the-two-regular-families.html), for the two centralisers and their intersection.
