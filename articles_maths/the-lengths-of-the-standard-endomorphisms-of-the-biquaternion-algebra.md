# __The Lengths of the Standard Endomorphisms of the Biquaternion Algebra: One, Two, Three and Four__

## Introduction

**The question.** Every complex-linear endomorphism of the biquaternion algebra is a sum of at most four two-sided operators, and the least number of terms is the rank of its coefficient array. The corpus writes a small and fixed list of operators on the algebra: the left and the right multiplications, the two-sided products, the Hermitian pair, the adjoint, the complex structure, the quaternion conjugation, the transposes of the frames, the Peirce projections, the derivations and the diagonal scalings. This article asks which length each of them carries, and why.

**The answer.** One for every operator that is itself a product, however many multipliers it has; two for every sum of a left and a right multiplication, for every derivation, and for the symmetrised products; three for a diagonal scaling whose four signed averages have exactly one vanishing member; four for the reflections, the coordinate projections, the transposes and the generic operator. All four values occur, and each occurs among operators the corpus writes without effort.

**The rule that decides.** The length is the rank of the array $c(M)$, and the array of a product of multipliers is the outer product of the two coefficient vectors. The array of a sum is the sum of the outer products. So the question *how many products* becomes the question *how many arrays of rank one*, and the answer is read from the multipliers without any search.

**The one family that needs a computation.** The diagonal scalings are not products, and their arrays are diagonal but not read off the eigenvalues. The four diagonal entries are the four signed averages of the eigenvalue vector, and the length is the number of them that do not vanish. This one theorem covers the identity, the conjugation, the coordinate projections and every truncation of the coordinates, and it is where the value three appears.

**The surprise.** The length is not monotone in the rank of the operator. The truncation to one coordinate has rank one and length four; the truncation to two coordinates has rank two and length two; the truncation to three coordinates has rank three and length four; the truncation to all four coordinates is the identity, of rank four and length one. Two operators of rank one can have lengths one and four, and two operators of length four can add to an operator of length two.

**Boundaries.** The theorem, the array and the strata are *The Length of an Endomorphism of the Biquaternion Algebra: Four Two-Sided Products*. The rest is carried by five articles, and each contributes one object of this one:

- *Operators Acting on One Side* and *Operators Acting on Two Sides*, the four families and their laws;
- *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra*, the basis and $\natural$;
- *The Transposition of the Two Sides*, the transpose of the model;
- *The Hermitian Pair of Operators Acting on Two Sides*, the pair $\Theta_{\tilde Q}$;
- *The Sylvester Operator and the Kronecker Sum of $M_4(\mathbb{C})$*, the derivation.

**The letters.** $\mathbb{B}$ has the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, with $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$. The families carry $L$, $R$, $LR$ and $\Theta$, as in *Operator Family Conventions*. The coefficient array is $c(M)$, the length is $\ell(M)$, and $\natural$ is the quaternion conjugation. The diagonal scaling with eigenvalue vector $a$ is $D_a$, and its signed averages are $b_t,b_x,b_y,b_z$. Greek indices run over $t,x,y,z$. The table of *Summary of Notation* at the end collects every symbol of the article in one place.

**The order of the article.** The array rule is recalled first, in one section, because every row of the table is a reading of it. The four lengths follow in order, one section each, with the section on length three carrying the theorem on the diagonal scalings. The section on the same rank and three lengths collects the counterexamples to monotonicity, and the last section places the four strata against the named operators.

## The Array Rule

**One formula.** For an endomorphism $M$ the coefficient array is
$$
c(M)_{\mu\nu}=\tfrac14\operatorname{tr}\bigl(T_{\mu\nu}^{\dagger}M\bigr),\qquad T_{\mu\nu}=L_{e_\mu}R_{e_\nu},
$$
and the length is $\ell(M)=\operatorname{rank}c(M)$. Write $c_{\tilde Q}$ for the coefficient vector of an element $\tilde Q$. The array of a product is the outer product of two such vectors,
$$
c\bigl(L_{\tilde Q_1}R_{\tilde Q_2}\bigr)_{\mu\nu}=c_{\tilde Q_1,\mu}\,c_{\tilde Q_2,\nu},
$$
so a product has length one whatever its operator rank, and a sum of $k$ products has an array of rank at most $k$. **Every statement below is a statement about one of these two displays.**

**The two conventions that the numbers depend on.** The array is written in the basis of products of the units, in the order $(t,x,y,z)$, and the sign of a coefficient depends on the conjugation that fixes the basis. The lengths do not depend on either choice, because a change of basis acts on the two slots of the tensor by invertible factors and preserves the rank. The intermediate displays, such as the four entries $\tfrac14(1,-1,-1,-1)$, are written in the basis of the four units fixed by *Matrix Representations Conventions*.

## Length One: The Dressed Multiplications

**The class.** An operator of length one is a product, and the table lists the products the corpus writes.

| operator | definition | array | operator rank |
|---|---|---|---|
| the identity | $\tilde X\mapsto\tilde X$ | $c_{e_t}c_{e_t}^{\mathsf T}$ | $4$ |
| a left multiplication | $\tilde X\mapsto\tilde Q\tilde X$ | $c_{\tilde Q}c_{e_t}^{\mathsf T}$ | $0,2,4$ |
| a right multiplication | $\tilde X\mapsto\tilde X\tilde P$ | $c_{e_t}c_{\tilde P}^{\mathsf T}$ | $0,2,4$ |
| a two-sided product | $\tilde X\mapsto\tilde Q\tilde X\tilde P$ | $c_{\tilde Q}c_{\tilde P}^{\mathsf T}$ | $0,1,2,4$ |
| the Hermitian pair | $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ | $c_{\tilde Q}c_{\tilde Q^{*}}^{\mathsf T}$ | $0,1,4$ |
| the adjoint, or inner automorphism | $\mathrm{Ad}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{-1}}$ | $c_{\tilde Q}c_{\tilde Q^{-1}}^{\mathsf T}$ | $4$ |
| the complex structure | $\tilde X\mapsto i\tilde X$ | $c_{ie_t}c_{e_t}^{\mathsf T}$ | $4$ |
| a Peirce corner | $\tilde X\mapsto\tilde\Pi_i\tilde X\tilde\Pi_j$ | $c_{\tilde\Pi_i}c_{\tilde\Pi_j}^{\mathsf T}$ | $0,1$ |
| a one-sided Peirce projection | $\tilde X\mapsto\tilde X\tilde\Pi_j$ | $c_{e_t}c_{\tilde\Pi_j}^{\mathsf T}$ | $0,2$ |

**Why the length is one in every row.** Each row is a product by construction, and the array of a product is an outer product, of rank one unless a multiplier vanishes. The Hermitian pair is a product because the second slot is the fixed element $\tilde Q^{*}$: the star is applied to the parameter and not to the operator, so the pair is complex-linear and is the two-sided product with multipliers $\tilde Q$ and $\tilde Q^{*}$. The adjoint is a product because the inverse is a fixed element.

**The adjoint, and what the word gauge names.** The operator $\mathrm{Ad}_{\tilde Q}$ has array of rank one and operator rank four, the two factors of the outer product being $c_{\tilde Q}$ and $c_{\tilde Q^{-1}}$. The gap between the two numbers is the point of the row: length one and invertible are independent properties. The name *gauge* belongs elsewhere. The gauge of the corpus is the rescaling of a Peirce frame, $E_{ij}\mapsto(t_i/t_j)E_{ij}$, and that rescaling is conjugation by the element $t_1\tilde\Pi_1+t_2\tilde\Pi_2$, since $\tilde\Pi_1\tilde X\tilde\Pi_2$ is scaled by $t_1/t_2$ under it. The Peirce gauge is therefore the diagonal torus inside the adjoint action, of one parameter in $M_2(\mathbb{C})$, and the adjoint is the larger group of all conjugations. The physical word for $\mathrm{Ad}$ is rotation rather than gauge: it fixes $e_t$ and acts on the traceless part, which is the complexified rotation group.

**The one-sided families are inside the two-sided one.** A left multiplication is $L_{\tilde Q}R_{e_t}$ and a right multiplication is $L_{e_t}R_{\tilde Q}$, so the one-sided families are the two coordinate faces of the cone of products. The identity is the vertex pattern $L_{e_t}R_{e_t}$, and the products with both multipliers in the centre are its scalar multiples.

**Length one does not mean invertible.** The two-sided product with two multipliers of rank two has operator rank one and length one; it is as far from invertible as an operator can be. Conversely the conjugation is invertible and has length four. The length counts the terms of the decomposition and says nothing about the invertibility of either the terms or the sum.

**The Peirce corner projections are the shortest non-trivial operators of the category.** With $\tilde\Pi_i$ a member of a complete orthogonal pair, the corner map $\tilde X\mapsto\tilde\Pi_i\tilde X\tilde\Pi_j$ is a projection of rank one, and it is a single product. It is the operator that reads one entry of the Peirce matrix, and it is of length one. The four corner maps sum to the identity, again of length one.

## Length Two: One Left and One Right

**The class.** A sum of a left and a right multiplication is the smallest operator that is not a product in general, and the criterion is exact.

**Proposition.** For $\tilde Q$ and $\tilde P$ such that $L_{\tilde Q}+R_{\tilde P}\neq0$, the length of $L_{\tilde Q}+R_{\tilde P}$ is two unless $\tilde Q$ or $\tilde P$ is central, in which case it is one.

*Proof.* The array is $c_{\tilde Q}c_{e_t}^{\mathsf T}+c_{e_t}c_{\tilde P}^{\mathsf T}$. It has rank one exactly when the two outer products are proportional, which happens exactly when $c_{\tilde Q}$ is proportional to $c_{e_t}$, that is when $\tilde Q$ is central, or when $c_{\tilde P}$ is proportional to $c_{e_t}$. Otherwise it has rank two.

**The derivation.** The commutator with an element is a difference of a left and a right multiplication,
$$
\operatorname{ad}_{\tilde Q}=L_{\tilde Q}-R_{\tilde Q},\qquad \operatorname{ad}_{\tilde Q}(\tilde X)=\tilde Q\tilde X-\tilde X\tilde Q .
$$
Its array is $c_{\tilde Q}c_{e_t}^{\mathsf T}-c_{e_t}c_{\tilde Q}^{\mathsf T}$, of rank two for a non-central $\tilde Q$ and of rank zero for a central one. So **every derivation of this form has length two**, and its operator rank is two, which is the dimension of the image modulo the centre. The qualification *of this form* costs nothing: the derivations of a central simple algebra are inner, and $\mathbb{B}\cong M_2(\mathbb{C})$ is central simple, so $\operatorname{ad}_{\tilde Q}$ with $\tilde Q\in\mathbb{B}$ already runs over every derivation of the algebra. The derivation is the operator of the Lie bracket, and its length two is the statement that a bracket is the difference of two products.

**The symmetrised product.** The Jordan product with a parameter is
$$
\tfrac12\bigl(L_{\tilde Q}+R_{\tilde Q}\bigr),\qquad \tilde X\longmapsto\tfrac12(\tilde Q\tilde X+\tilde X\tilde Q),
$$
of length two for non-central $\tilde Q$. The anticommutator $L_{\tilde Q}+R_{\tilde Q}$ has the same length. So the two classical products built from a left and a right multiplication, the bracket and the anticommutator, are both of length two, and neither is a product.

**The Peirce sums.** The sum of two corner maps, $\tilde X\mapsto\tilde\Pi_1\tilde X\tilde\Pi_1+\tilde\Pi_2\tilde X\tilde\Pi_2$, has the array $E_{11}+E_{22}$, of rank two, so its length is two. The sum of three corner maps has the array $E_{11}+E_{12}+E_{21}$, of rank two, so its length is also two, although its operator rank is three. The last row is the cleanest example in the algebra of an operator of operator rank three: no single product has that rank, and a sum of two has it without adding a third term.

**Two is the generic value, and the class is a subspace.** The map $(\tilde Q,\tilde P)\mapsto L_{\tilde Q}+R_{\tilde P}$ is linear, and its kernel is one-dimensional, spanned by $(e_t,-e_t)$. So the class is a seven-dimensional linear subspace of the sixteen-dimensional ambient, most of its members have length two, and the length one members are the two faces on which one multiplier is central. The class is a subspace and not a cone, and it misses most operators.

## The Diagonal Scalings: The Four Signed Averages

**The family.** Fix a vector $a=(a_t,a_x,a_y,a_z)$ and let
$$
D_a(\tilde X)=\sum_\mu a_\mu x_\mu e_\mu ,
$$
the scaling of the four coordinates. The identity is $D_{(1,1,1,1)}$, the quaternion conjugation is $D_{(1,-1,-1,-1)}$, the projection onto the coordinate line $\mathbb{C}e_\mu$ is $D_{e_\mu}$, the truncation to a set $S$ of coordinates is $D_{\mathbf 1_S}$, and the scaling of eigenvalue vector $(1,2,3,4)$ is $D_{(1,2,3,4)}$. The family is four-dimensional and commutative, and it meets the cone of products exactly at the four rays of the products $L_{e_\mu}R_{e_\mu}$.

**Theorem (the length of a diagonal scaling).** The array of $D_a$ is diagonal, with the four entries $b_t,b_x,b_y,b_z$ on its diagonal, where
$$
b_t=\tfrac14(a_t+a_x+a_y+a_z),\quad
b_x=\tfrac14(-a_t-a_x+a_y+a_z),\quad
b_y=\tfrac14(-a_t+a_x-a_y+a_z),\quad
b_z=\tfrac14(-a_t+a_x+a_y-a_z),
$$
and $\ell(D_a)=\#\{\mu:\ b_\mu\neq0\}$.

*Proof.* Compute the four products $L_{e_\mu}R_{e_\mu}$ on the units. For $\mu=t$ the product is the identity, of eigenvalue vector $v_t=(1,1,1,1)$. For an imaginary $\mu$ the product negates $e_t$ and $e_\mu$ and fixes the two remaining units; so $v_x=(-1,-1,1,1)$, $v_y=(-1,1,-1,1)$ and $v_z=(-1,1,1,-1)$. The four vectors are pairwise orthogonal with squared norm four, so the dual basis of $(v_\mu)$ is $\tfrac14(v_\mu)$, and every vector $a$ expands as $a=\tfrac14\sum_\mu(v_\mu\cdot a)v_\mu$. The map $a\mapsto D_a$ is linear, and $D_{v_\mu}=L_{e_\mu}R_{e_\mu}$ because $v_\mu$ was computed as the eigenvalue vector of that product; applying the linear map to the expansion of $a$ gives $D_a=\tfrac14\sum_\mu(v_\mu\cdot a)L_{e_\mu}R_{e_\mu}$. A diagonal scaling is determined by its eigenvalue vector, so the equality of eigenvalue vectors is the equality of operators. The array of $L_{e_\mu}R_{e_\mu}$ is the unit array $E_{\mu\mu}$, so the array of $D_a$ is diagonal with the four coefficients displayed, and its rank is the number of nonzero entries. **The length of a diagonal scaling is the number of nonzero signed averages of its eigenvalue vector.**

**The table of the named cases.** The theorem answers every row at once.

| operator | $a$ | $b$ | length |
|---|---|---|---|
| the identity | $(1,1,1,1)$ | $(1,0,0,0)$ | $1$ |
| the quaternion conjugation $\natural$ | $(1,-1,-1,-1)$ | $(-\tfrac12,-\tfrac12,-\tfrac12,-\tfrac12)$ | $4$ |
| the sign flip of $\vec e_y$, the transpose | $(1,1,-1,1)$ | $(\tfrac12,-\tfrac12,\tfrac12,-\tfrac12)$ | $4$ |
| the projection onto $\mathbb{C}e_t$ | $(1,0,0,0)$ | $\tfrac14(1,-1,-1,-1)$ | $4$ |
| the truncation to $\{t,x\}$ | $(1,1,0,0)$ | $\tfrac12(1,-1,0,0)$ | $2$ |
| the truncation to $\{t,x,y\}$ | $(1,1,1,0)$ | $\tfrac14(3,-1,-1,1)$ | $4$ |
| $D_{(1,2,3,4)}$ | $(1,2,3,4)$ | $(\tfrac52,1,\tfrac12,0)$ | $3$ |
| $D_{(1,2,3,5)}$ | $(1,2,3,5)$ | $(\tfrac{11}{4},\tfrac54,\tfrac34,-\tfrac14)$ | $4$ |

**The four short scalings.** A diagonal scaling has length one exactly when three of its four averages vanish, and the vectors with that property are the four rays of $v_t,v_x,v_y,v_z$, which are the four diagonal products $L_{e_\mu}R_{e_\mu}$. The identity is the ray of $v_t$, and the central scalings are the scalar multiples of the identity. Every other scaling of the family has length two, three or four, and the generic one has four.

**Where the value three comes from.** The condition $\ell(D_a)=3$ is the vanishing of exactly one of the four averages, a single linear equation in $a$: a hyperplane inside the family. The vector $(1,2,3,4)$ lies on the hyperplane $b_z=0$, because $-1+2+3-4=0$, and $(2,3,4,5)$ lies on the same hyperplane. So the value three is not exotic; it is the generic value on the hyperplane where one average vanishes, and it is the only way the value arises in this family.

**The eigenvalues do not give the length.** The scaling $D_a$ has eigenvalues $a$, and the length is neither the number of nonzero eigenvalues nor the number of distinct ones. The vector $(1,2,3,4)$ has four distinct nonzero eigenvalues and length three; the identity has one eigenvalue and length one; the conjugation has two eigenvalues and length four. The four averages are a signed transform of the eigenvalue vector and not the vector itself.

**The other truncations.** The same rule gives the lengths of all the truncations at once: the truncation to a set of $k$ coordinates has length $4$ for $k=1$, $2$ for $k=2$, $4$ for $k=3$ and $1$ for $k=4$, for every choice of the set. The pattern is read from the four averages of the indicator vector, and each of the four values $1,2,4$ occurs, with the value three never occurring among the truncations.

## Length Four: The Reflections

**The criterion.** An operator has length four exactly when $\det c(M)\neq0$, because length at most three is the single polynomial condition $\det c(M)=0$. The operators of length four are therefore the complement of a hypersurface, and every named operator of this section is a witness on that open set. What follows is the list of witnesses the corpus writes, with the reason each one falls there.

**The class.** The operators of length four in the corpus negate one coordinate, permute the coordinates oddly, project onto a coordinate line, or are generic.

**The quaternion conjugation.** $\natural$ is $D_{(1,-1,-1,-1)}$, of length four, and it is also $-\tfrac12\sum_\mu L_{e_\mu}R_{e_\mu}$: the two readings agree because the four diagonal products are the four entries of the array. The conjugation is the reflection in the scalar line and the most elementary operator of the algebra after the multiplications, and it is of maximal length.

**The sign flips.** The sign flip of one imaginary coordinate is $D_{(1,1,-1,1)}$ for $\vec e_y$, of length four, and the same for $\vec e_x$ and $\vec e_z$. The flip of all three is the conjugation, also of length four. So no reflection of the sign of a coordinate is short, and the four rays of the diagonal products are the only short diagonal maps.

**The transposes.** The transpose of the model fixes $e_t,\vec e_x,\vec e_z$ and negates $\vec e_y$, so it is the sign flip of $\vec e_y$ and its length is four. The transposition of the two sides converts a left multiplication into a right one by composing with $\natural$ on both sides, and the operator that the transpose of the model represents is the sign flip of $\vec e_y$; the two statements are the two faces of one conjugation.

**The coordinate projections.** The projection onto the line $\mathbb{C}e_\mu$ is $D_{e_\mu}$, of length four, for every $\mu$ including $\mu=t$. So the four coordinate lines carry projections of maximal length, and the projection onto the scalar line is the case $\mu=t$ of one statement about four lines.

**The permutations, and the parity that decides.** A permutation of the four units is not a diagonal scaling, and parity fixes its length.

*The odd ones are not products.* No product has determinant $-1$. The left multiplication acts by $\tilde Q$ on each of the two Peirce columns and the right multiplication acts by $\tilde P$ on each of them, so
$$
\det L_{\tilde Q}=(\det\tilde Q)^{2},\qquad \det R_{\tilde P}=(\det\tilde P)^{2},
$$
so the determinant of a product is a square and in particular never $-1$; an odd permutation of the units has determinant $-1$, so it is not a product. The sixteen entries of its array are a direct computation from the multiplication table, and over the twelve odd permutations they take the closed form $\tfrac12\Sigma$ with $\Sigma$ a signed permutation array. The odd permutations fall in two conjugacy classes, a transposition and a four-cycle, and one representative of each is enough to display the form:
$$
\tfrac12\begin{pmatrix}1&0&0&0\\0&-1&0&0\\0&0&0&-1\\0&0&-1&0\end{pmatrix}\quad(y\ z),\qquad
\tfrac12\begin{pmatrix}0&0&-1&0\\0&0&0&-1\\0&-1&0&0\\1&0&0&0\end{pmatrix}\quad(t\ z\ x\ y).
$$
Each has determinant $\pm\tfrac1{16}$, so the array has rank four and the length is four. **Every odd permutation has length four.**

*The even ones are products.* Two factorisations, each a lookup in the multiplication table, generate the alternating group: with $\epsilon=\tfrac12(e_t+e_x+e_y+e_z)$, of norm one,
$$
(x\ y\ z)=L_\epsilon R_{\epsilon^{-1}},\qquad (t\ x)(y\ z)=-L_{e_z}R_{e_y}.
$$
The first is the conjugation $\tilde X\mapsto\epsilon\tilde X\epsilon^{-1}$, which fixes $e_t$ and cycles the three imaginary units; the second is a single product with a sign. These two permutations generate a group of order twelve, and it is the alternating group, so every even permutation is a word in them. Since a product composed with a product is a product, by the composition law $L_{\tilde Q_1}R_{\tilde Q_2}L_{\tilde P_1}R_{\tilde P_2}=L_{\tilde Q_1\tilde P_1}R_{\tilde P_2\tilde Q_2}$, every even permutation is a product and has length one.

**The twelve even permutations of the units have length one and the twelve odd ones have length four**, and the six transpositions are the odd ones of order two.

**The generic operator.** A generic endomorphism has length four, a generic two-sided product has length one, and a generic sum of a left and a right multiplication has length two. Four is not a rare value: by the criterion above it is the value on the complement of a hypersurface, hence on almost every operator.

## The Same Rank, Three Lengths

**The rank does not fix the length.** The following table is computed from the theorem of the diagonal scalings and from the array rule, and every row is an operator of the corpus.

| operator | operator rank | length |
|---|---|---|
| the Peirce corner $\tilde X\mapsto\tilde\Pi_1\tilde X\tilde\Pi_1$ | $1$ | $1$ |
| the truncation to one coordinate | $1$ | $4$ |
| the Peirce projection $\tilde X\mapsto\tilde X\tilde\Pi_1$ | $2$ | $1$ |
| the truncation to two coordinates | $2$ | $2$ |
| the sum of three Peirce corners | $3$ | $2$ |
| the truncation to three coordinates | $3$ | $4$ |
| the identity | $4$ | $1$ |

**Two rank-one projections of lengths one and four.** The corner projection onto the Peirce line is a single product, and the coordinate projection onto $\mathbb{C}e_t$ is $D_{e_t}$, of length four. Both are idempotent, both have rank one, and both are operators of the same algebra. The difference is not the size of the image but the shape of the array: an outer product for the first, a full-rank diagonal array for the second.

**The length of a truncation is not its rank.** The truncations form the pattern $4,2,4,1$ for ranks $1,2,3,4$. The pattern is read from the four signed averages of the indicator vector, and it shows that adding a coordinate can shorten an operator and adding another can lengthen it.

**A sum of two long operators can be short.** The truncation to $\{t,x\}$ is the sum of the truncation to $\{t\}$ and the truncation to $\{x\}$, and its length is two while each summand has length four. So the length is not subadditive in the useful direction: $\ell(A+B)$ can be smaller than both $\ell(A)$ and $\ell(B)$, and no lower bound in terms of the summands exists.

**The four corner maps and their sums.** Each corner map has length one. A partial sum of two or three corners has length two. The sum of all four is the identity, of length one. So a sum of four operators of length one can have length two or length one, according to the pattern of the corners, and the two-sided family does not behave like a basis in which the coefficients are read one at a time.

## The Strata and the Named Operators

**The strata.** The operators of length at most $r$ are the arrays of rank at most $r$, of complex dimension $8r-r^2$, so the ladder is $0,7,12,15,16$ for $r=0,1,2,3,4$.

| $r$ | the named operators of length exactly $r$ |
|---|---|
| $0$ | the zero operator |
| $1$ | the identity, $L_{\tilde Q}$, $R_{\tilde P}$, $L_{\tilde Q}R_{\tilde P}$, $\Theta_{\tilde Q}$, $\mathrm{Ad}_{\tilde Q}$, $i\,\cdot$, the Peirce corners, the even permutations of the units |
| $2$ | $L_{\tilde Q}+R_{\tilde P}$, the derivations, the symmetrised products, the sums of two and of three Peirce corners, the truncations to two coordinates |
| $3$ | the diagonal scalings with exactly one vanishing signed average, such as $D_{(1,2,3,4)}$ |
| $4$ | $\natural$, the sign flips, the odd permutations, the transpose, the coordinate projections, the truncations to one and to three coordinates, the generic operator |

**The classes are not the strata.** The table of the length one class is a list of operators, not the whole stratum of length one: the stratum is the Segre cone, of dimension seven, and the products with two invertible multipliers are its open dense part. The same remark holds for the other rows. What the table asserts is that each stratum is met by the named operators, and that no named operator of the corpus is left without a place.

**The unlisted operators.** The two antilinear conjugations, the coefficient conjugation $\bar{\cdot}$ and the star, are not complex-linear endomorphisms and have no length in this sense. They belong to the second real family $\{T_{\mu\nu}J\}$, and their real length is that of their linear part plus four. The dagger of an operator is not an endomorphism either; it is a tie on the operator space.

## Summary

The length of every standard operator of the biquaternion algebra is read from its coefficient array. The array is an outer product for a product and a sum of two outer products for a sum of a left and a right multiplication.

Every operator that is a product has length one, whatever its operator rank: the identity, the one-sided multiplications, the two-sided products, the Hermitian pair, the adjoint, the complex structure, the Peirce corner projections, the one-sided Peirce projections and the even permutations of the units.

Every sum of a left and a right multiplication has length two unless one multiplier is central, and the derivations and the symmetrised products belong to this class. The sums of two and of three Peirce corners also have length two, the second one with operator rank three.

The diagonal scalings satisfy a closed rule: the array is diagonal, its four entries are the signed averages of the eigenvalue vector, and the length is the number of nonzero entries. The only short scalings are the four diagonal products, of which the identity is one; the conjugation and the coordinate projections have length four, and the value three occurs exactly on the hyperplane where one average vanishes, as at $D_{(1,2,3,4)}$.

The reflections, the transposes, the odd permutations of the coordinates, the truncations to one and to three coordinates, and the generic operator have length four.

The length is not a function of the rank of the operator. Two rank-one projections have lengths one and four, the truncations of ranks one to four have lengths four, two, four and one, and the sum of two operators of length four can have length two.

## Summary of Notation

| symbol | meaning | article |
|---|---|---|
| $c(M)$ | the coefficient array in the sixteen products | *The Length of an Endomorphism of the Biquaternion Algebra: Four Two-Sided Products* |
| $\ell(M)$ | the length, the least number of two-sided products | *The Length of an Endomorphism of the Biquaternion Algebra: Four Two-Sided Products* |
| $T_{\mu\nu}$ | $L_{e_\mu}R_{e_\nu}$ | *Operators Acting on Two Sides* |
| $\Theta_{\tilde Q}$ | the Hermitian pair $L_{\tilde Q}R_{\tilde Q^{*}}$ | *The Hermitian Pair of Operators Acting on Two Sides* |
| $\operatorname{ad}_{\tilde Q}$ | the derivation $L_{\tilde Q}-R_{\tilde Q}$ | *The Sylvester Operator and the Kronecker Sum of $M_4(\mathbb{C})$* |
| $D_a$ | the diagonal scaling $\sum_\mu a_\mu x_\mu e_\mu$ | this article |
| $b_t,b_x,b_y,b_z$ | the four signed averages of $a$ | this article |
| $\tilde\Pi_1,\tilde\Pi_2$ | a complete orthogonal pair of idempotents | *Special Element and Peirce Conventions* |
| $\natural$ | the quaternion conjugation | *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra* |

## Further Reading

- [The Length of an Endomorphism of the Biquaternion Algebra: Four Two-Sided Products](the-length-of-an-endomorphism-of-the-biquaternion-algebra.html), for the theorem, the array, the strata and the comparison with the singular decomposition.
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the composition law of the products and the cone.
- [Operators Acting on One Side](operators-acting-on-one-side.html), for the two one-sided families and their laws.
- [The Hermitian Pair of Operators Acting on Two Sides](the-hermitian-pair-of-operators-acting-on-two-sides.html), for the fourth family.
- [The Transposition of the Two Sides](the-transposition-of-the-two-sides.html), for the conversion between the families and the transpose of the model.
- [The Sylvester Operator and the Kronecker Sum of $M_4(\mathbb{C})$](the-sylvester-operator-and-the-kronecker-sum-of-m4c.html), for the derivation as a difference of a left and a right multiplication.
- [The Length and the Two Ranks at $n=4$](the-length-and-the-two-ranks-at-n-4.html), for the same statements at the size of this algebra.
