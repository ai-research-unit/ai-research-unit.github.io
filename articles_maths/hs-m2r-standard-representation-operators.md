# __$M_2(\mathbb{R})$ Standard Representation : Operators__

## Introduction

**The space of operators.** The carrier is $\mathbb{H}_{\mathrm{s}}$, of real dimension four, and the operators are the real-linear maps of the carrier into itself, so the ambient algebra is

$$
\operatorname{End}_{\mathbb{R}}(\mathbb{H}_{\mathrm{s}})\cong M_4(\mathbb{R}),
$$

of dimension sixteen. The general article gives two families of operators for free, the left multiplications $L_{\tilde q}$ and the right multiplications $R_{\tilde q}$, each a copy of the algebra inside the ambient, and the whole article is about what the two families generate together.

**The count in one line.** Sixteen operators $L_{e_\mu}R_{e_\nu}$ span the ambient, so a general operator is a sum of sixteen products, and the product of a left and a right multiplication is written $L_{\tilde q}R_{\tilde p}(\tilde x)=\tilde q\tilde x\tilde p$. The pair $(\tilde q,\tilde p)$ runs over an eight-dimensional space, the operators reach a seven-dimensional cone inside the sixteen-dimensional ambient, and the generic operator is a sum of four products. Those three numbers, eight, seven and four, organise the article.

**Two things the pair does and one it does not.** It gives the full operator algebra, since the span is everything. It gives the Lorentz action, since the units act on the carrier as $SO(2,2)$. It does not give the spin structure, because the spinors are the minimal left ideals and that is a statement about modules, not about operators of the carrier. The last section says exactly where the boundary lies.

**Boundaries.** The model, its dictionary, the trace, the determinant, the spectral trichotomy, the adjugate, the norms and the projective line are the companion article *$M_2(\mathbb{R})$ Standard Representation*. The algebra is *Split-Quaternion Algebra*; the norm and the units are *Split-Quaternion Norm and Invertibility*; the zero divisors are *Split-Quaternion Zero Divisors*; the action of the units on the null cone and the hyperbolic geometry are *Split-Quaternion Rotations and the Lorentz Group*. The abstract operators of the algebra, with no matrix in them, are *Left and Right Multiplication* and *The Left and Right Multiplication Operators on a Clifford Algebra*, which this article does not replace.

**Conventions.** The basis of the algebra is $(e_t,\vec e_x,\vec e_y,\vec e_z)$ with $\vec e_x^2=-e_t$ and $\vec e_y^2=\vec e_z^2=e_t$, the model is $\mathsf{M}_2$ with images $I,J,K,D$, and $M_{\tilde q}$ is written for $\mathsf{M}_2(\tilde q)$. The trace form is $\langle X,Y\rangle_{\operatorname{tr}}=\operatorname{tr}(XY)$, of signature $(3,1)$; the Frobenius form is $\langle X,Y\rangle_F=\operatorname{tr}(X^{\mathsf T}Y)$, positive definite. The coefficient matrix $c(M)$ of an operator is its matrix in the basis $\{L_{e_\mu}R_{e_\nu}\}$.

## The One-Sided Operators

**The two families.** For $\tilde q$ in the algebra and $\tilde x$ in the carrier,

$$
L_{\tilde q}(\tilde x)=\tilde q\tilde x,\qquad R_{\tilde q}(\tilde x)=\tilde x\tilde q,
$$

with matrix forms

$$
L_{M_{\tilde q}}=M_{\tilde q}\otimes I_2,\qquad R_{M_{\tilde q}}=I_2\otimes M_{\tilde q}^{\mathsf T},
$$

in the row-major vectorisation. Both are assigned one $2\times2$ matrix per map, and that is the whole information, because the carrier is four-dimensional and the algebra is the carrier.

**What the two families are.** Each is a faithful copy of $\mathbb{H}_{\mathrm{s}}\cong M_2(\mathbb{R})$ inside $M_4(\mathbb{R})$. The two copies commute, $L_{\tilde q}R_{\tilde p}=R_{\tilde p}L_{\tilde q}$, and each is the centraliser of the other, which is the double centraliser theorem read on a full matrix algebra. They intersect in the scalars: $L_{\tilde q}=R_{\tilde q}$ exactly for $\tilde q\in\mathbb{R}e_t$.

**The invariants.** The rank, the trace and the determinant of a left multiplication are

$$
\operatorname{rank}L_{\tilde q}=2\operatorname{rank}M_{\tilde q},\qquad
\operatorname{tr}L_{\tilde q}=4q_t,\qquad
\det L_{\tilde q}=\langle\tilde q\rangle_{\natural}^{2},
$$

and the same three numbers hold for $R_{\tilde q}$, since transposition does not change them. The spectrum of $L_{\tilde q}$ is the spectrum of $M_{\tilde q}$ doubled: each eigenvalue occurs twice, because the operator acts on the algebra and not on the plane.

**The adjoints for the trace form.** With respect to $\langle X,Y\rangle_{\operatorname{tr}}=\operatorname{tr}(XY)$,

$$
\langle L_{\tilde q}X,Y\rangle_{\operatorname{tr}}=\operatorname{tr}(\tilde qXY)=\operatorname{tr}(X\,Y\tilde q)=\langle X,R_{\tilde q}Y\rangle_{\operatorname{tr}},
$$

so the adjoint of a left multiplication is the right multiplication by the same element, and conversely. The two families are mutual adjoints. The consequence is immediate and slightly surprising: a left multiplication is self-adjoint for the trace form exactly when it is central, so the self-adjoint sector of the left family is the one-dimensional scalar line.

**The adjoints for the Frobenius form.** With respect to $\langle X,Y\rangle_F=\operatorname{tr}(X^{\mathsf T}Y)$,

$$
L_{\tilde q}^{*}=L_{\tilde q^{\mathsf T}},
$$

where $\tilde q^{\mathsf T}$ is the element whose matrix is the transpose, that is the element with $q_x$ negated. So the positive definite form makes the left family self-adjoint on the three-dimensional symmetric subspace and pairs the two families differently: the adjoint stays on the left, and the right family never appears.

**The reading.** The trace form pairs the two copies and is indefinite; the Frobenius form is definite and keeps each copy to itself. This is the operator-level form of the statement of the general article that no form is at once invariant and positive definite.

## The Two-Sided Operator

**Definition.** For a pair $(\tilde q,\tilde p)$ the two-sided operator is

$$
L_{\tilde q}R_{\tilde p},\qquad L_{\tilde q}R_{\tilde p}(\tilde x)=\tilde q\tilde x\tilde p .
$$

In the model it is $L_{A}R_{B}(X)=AXB$ with $A=M_{\tilde q}$ and $B=M_{\tilde p}$, and its $4\times4$ matrix is $A\otimes B^{\mathsf T}$.

**The scaling.** The pair is not free:

$$
L_{\lambda\tilde q}R_{\lambda^{-1}\tilde p}=L_{\tilde q}R_{\tilde p}\qquad(\lambda\in\mathbb{R}^{\times}),
$$

because $\lambda$ cancels between the two slots. So the eight parameters of the pair act on the operator through seven, and the fibre of the map $(\tilde q,\tilde p)\mapsto L_{\tilde q}R_{\tilde p}$ over a non-zero product is exactly one scaling orbit, a line.

**The two parameters that do not act.** The pair is not a two-parameter object at all when the algebra is commutative, and that is the collapse of the complex, split-complex and dual categories. Here the algebra is not commutative, so the two slots are genuinely two, and the only redundancy is the scaling. The number seven is the first place where the model is not degenerate.

**The determinant.** Since $\det(A\otimes B^{\mathsf T})=\det(A)^{2}\det(B)^{2}$,

$$
\det L_{A}R_{B}=\langle\tilde q\rangle_{\natural}^{2}\langle\tilde p\rangle_{\natural}^{2}\geq0 .
$$

The inequality is structural and not an accident of the example: a two-sided operator which is a single product has a **non-negative** determinant, and it vanishes exactly when one of the two elements is a zero divisor. So the image of $GL_2(\mathbb{R})\times GL_2(\mathbb{R})$ under the map lies in $\{M:\det M>0\}$, a proper open subset of the group of invertible operators.

**The trace.** $\operatorname{tr}L_{A}R_{B}=\operatorname{tr}A\cdot\operatorname{tr}B=4q_tp_t$, symmetric in the two slots and vanishing whenever either element is traceless.

**The conjugation.** The case $B=A^{-1}$ gives the adjoint action,

$$
L_{A}R_{A^{-1}}(X)=AXA^{-1},
$$

whose kernel on the pairs of units is the centre $\mathbb{R}^{\times}I$, so the effective group is

$$
\mathrm{PGL}_2(\mathbb{R})\cong SO^{+}(2,1),
$$

the identity component of the Lorentz group in $2+1$ dimensions. This is the operator form of the statement of the general article that the automorphisms of the algebra are inner: the inner automorphisms act on the algebra as the conjugations, and the conjugations are exactly the two-sided operators with $B=A^{-1}$.

**The sandwich.** The case $B=A$ gives $X\mapsto AXA$, which is not a conjugation and whose determinant is $\det(A)^{4}$, a fourth power. The two sandwiches $L_{A}R_{A^{-1}}$ and $L_{A}R_{A}$ differ by the conjugation composed with the left multiplication by $A^{2}$, and only the first is a group action.

## The Kronecker Display

**The display.** The operator $L_{A}R_{B}$ is displayed as a Kronecker product,

$$
L_{A}R_{B}=A\otimes B^{\mathsf T},\qquad
\operatorname{vec}(AXB)=\bigl(A\otimes B^{\mathsf T}\bigr)\operatorname{vec}X,
$$

and the display is exact, not an approximation: the four-by-four matrix is the tensor product of two two-by-two matrices, and every entry of the operator is a product of one entry of $A$ and one entry of $B$.

**The coefficient matrix.** The sixteen operators $L_{e_\mu}R_{e_\nu}$, for $\mu,\nu\in\{t,x,y,z\}$, form a basis of $M_4(\mathbb{R})$, because $\{M_{e_\mu}\}$ is a basis of $M_2(\mathbb{R})$ and the tensor products of two bases form a basis. Every operator $M$ therefore has coordinates $c_{\mu\nu}(M)$ in that basis, and for a single product

$$
c\bigl(L_{\tilde q}R_{\tilde p}\bigr)=[\,\tilde q\,][\,\tilde p\,]^{\mathsf T},
$$

the outer product of the two coordinate vectors, a matrix of rank one. The array $c(M)$ is a $4\times4$ array of real numbers for each operator $M$, and it is the object that decides every question of the next three sections.

**The reading.** The coefficient matrix turns a question about a four-by-four operator into a question about a four-by-four array of numbers, and the two are different arrays: the first is the operator, the second is its coordinates in a basis of products. The whole of the second layer is the comparison of the two.

## The Rank and the Invariants

**Theorem (the rank is a product).** For all $\tilde q,\tilde p$,

$$
\operatorname{rank}L_{\tilde q}R_{\tilde p}=\operatorname{rank}A\cdot\operatorname{rank}B
\in\{0,1,2,4\},
$$

and the value three never occurs.

**Proof.** The rank of a Kronecker product is the product of the ranks, and the rank of a $2\times2$ matrix is $0$, $1$ or $2$. The products are then $0$, $1$, $2$ or $4$, and $3$ is not among them.

**The consequences.** A single product is invertible exactly when both elements are units, and then its rank is four. It has rank one exactly when one of the two is a rank-one matrix and the other is a unit. It has rank two in two ways, and the two ways are not distinguishable by the rank alone. And it vanishes exactly when one of the two is zero.

**The invariants collected.** The table gathers the four numbers of a single product.

| quantity | value for $L_{A}R_{B}$ | depends on |
|---|---|---|
| operator rank | $\operatorname{rank}A\cdot\operatorname{rank}B$ | the ranks of the two |
| trace | $\operatorname{tr}A\cdot\operatorname{tr}B$ | the traces of the two |
| determinant | $\det(A)^{2}\det(B)^{2}$ | the norms of the two |
| coefficient rank | $1$ | nothing |

The last row is the point of the whole article: the coefficient rank of a single product is always one, whatever the two elements are, so it carries no information about them and it is the correct measure of the *length* rather than of the size.

## The Pair as a Semigroup

**Composition.** For two products,

$$
L_{A}R_{B}\,L_{A'}R_{B'}=L_{AA'}R_{\,B'B},
$$

so the family is closed under composition, and the composition law is the product in the first slot and the **opposite** product in the second. The family is therefore a copy of $M_2(\mathbb{R})\times M_2(\mathbb{R})^{\mathrm{opp}}$ inside the algebra of all operators, and not a copy of $M_2\times M_2$: the reversal of the second factor is the associativity of the original product showing through.

**The units of the semigroup.** The invertible members are the products of two units, and their inverses are $L_{A^{-1}}R_{B^{-1}}$. They form the group

$$
\bigl(GL_2(\mathbb{R})\times GL_2(\mathbb{R})\bigr)/\mathbb{R}^{\times},
$$

of dimension seven, where the quotient is by the simultaneous scaling $(\lambda,\lambda^{-1})$.

**The automorphisms.** The inner automorphisms of the algebra appear as the products $L_{A}R_{A^{-1}}$, and they form the subgroup $\mathrm{PGL}_2(\mathbb{R})$ of the group above, of dimension three. So the semigroup contains two distinguished subgroups: the full seven-dimensional group of the products of units, and the three-dimensional group of the conjugations. The four dimensions between them are the sandwiches $L_{A}R_{B}$ with $AB\neq I$.

**The matrix units.** The sixteen basis operators $L_{e_\mu}R_{e_\nu}$ are the matrix units of the ambient under the tensor identification, and the four corners of the Peirce decomposition give four of them. The algebra is a full matrix algebra and the semigroup carries a complete system of such units; the quaternion and split-biquaternion categories do not, which is the structural difference that their operators articles have to state.

**The absence of a unit in the pair.** The identity operator is $L_{e_t}R_{e_t}$, a single product, so the semigroup has a unit and the unit is a product of length one. The pair is therefore not a subsemigroup of the group of operators by accident: it contains the identity, and the composition is the operator composition. What it does not contain is the whole group: the operators of negative determinant are not products, since a product has a non-negative determinant.

## The Cone and the Coefficient Matrix

**The map.** Put $\beta(\tilde q,\tilde p)=L_{\tilde q}R_{\tilde p}$. It is bilinear, $\beta(\lambda\tilde q,\mu\tilde p)=\lambda\mu\,\beta(\tilde q,\tilde p)$, and its image is therefore a cone with vertex at the zero operator and not a linear subspace,

$$
\beta:\mathbb{H}_{\mathrm{s}}\times\mathbb{H}_{\mathrm{s}}\longrightarrow\operatorname{End}_{\mathbb{R}}(\mathbb{H}_{\mathrm{s}}).
$$

The additive failure is the ordinary one of a bilinear map: $\beta(\tilde q_1+\tilde q_2,\tilde p)\neq\beta(\tilde q_1,\tilde p)+\beta(\tilde q_2,\tilde p)$ in general, and section *The Two Ranks* gives the witness.

**The image is the Segre cone.** By the coefficient matrix, $\beta(\tilde q,\tilde p)$ is a single product exactly when $c$ has rank one, so

$$
\operatorname{Im}\beta=\{M:\operatorname{rank}c(M)\le1\}\cup\{0\},
$$

which is the affine cone over the Segre variety $\mathbb{P}^3(\mathbb{R})\times\mathbb{P}^3(\mathbb{R})$ inside $\mathbb{P}^{15}(\mathbb{R})$. Its dimension is $3+3+1=7$, the seven of the pair modulo scaling.

**The membership test.** An operator is a single product **if and only if** its coefficient matrix has rank one, and then the two factors are recovered from the two singular vectors: if $c=uv^{\mathsf T}$ then $\tilde q=\sum u_\mu e_\mu$ and $\tilde p=\sum v_\nu e_\nu$. The test is exact, it needs no solving, and it is the one test that the four remaining sections use.

**The rulings.** Two families of maximal linear subspaces sweep the cone: the set of products with $\tilde p$ fixed, and the set with $\tilde q$ fixed. Each is a copy of the algebra, of dimension four, and the intersection of a member of one family with a member of the other is the single point where the two parameters are the given ones. This is the operator-level picture of the two rulings of the null quadric.

**The cone is not the null cone.** The cone of the operators and the null cone of the norm are different objects in different spaces: one lives in $M_4(\mathbb{R})$ and is the set of single products, the other lives in the algebra and is the set of zero divisors. They meet, because a product of two zero divisors is a zero divisor and its operator is singular, but neither contains the other.

## The Length

**Definition.** The **length** of an operator is the least number of single products whose sum it is,

$$
\ell(M)=\min\Bigl\{k:\ M=\sum_{i=1}^{k}L_{\tilde q_i}R_{\tilde p_i}\Bigr\}.
$$

**Theorem (the length is the coefficient rank).** For every operator $M$ of the span, which here is the whole ambient,

$$
\ell(M)=\operatorname{rank}c(M)\in\{0,1,2,3,4\}.
$$

**Proof.** A sum of $k$ products has a coefficient matrix which is a sum of $k$ matrices of rank one, hence of rank at most $k$; so $\ell\ge\operatorname{rank}c$. Conversely a matrix of rank $r$ is a sum of $r$ matrices of rank one, and each of those is the coefficient matrix of a product, by the membership test applied to each summand; so $\ell\le\operatorname{rank}c$.

**The strata.** The sets of operators of length at most $r$ are the determinantal sets $\{\operatorname{rank}c\le r\}$, of dimensions

| $r$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| $\dim\{M:\operatorname{rank}c(M)\le r\}$ | $0$ | $7$ | $12$ | $15$ | $16$ |

so the generic operator has length four and four always suffice, the single products are the smallest closed stratum, and the operators of length two fill a set of dimension twelve which is neither open nor the cone.

**The reading of the strata.** The number $7$ is the cone of single products, the same seven as the image of $\beta$; the number $12$ is the set of sums of two, which contains the operators of rank two that no single product reaches; the number $15$ is the complement of the open set of length four in all but one dimension. The closed sets are the cumulative ones. The operators of length exactly three are the difference of two closed sets and are therefore neither closed nor open, which is why the length is not read off by a limit argument.

## The Two Ranks

**The two numbers.** The **operator rank** is the rank of the four-by-four matrix; the **coefficient rank** is the length. They measure different things and neither determines the other, and this section gives the two extreme witnesses.

**The identity.** $L_{e_t}R_{e_t}$ is the identity operator. Its operator rank is four, the largest possible, and its coefficient rank is one, the smallest for a non-zero operator. So a maximal operator rank costs a single product.

**A singular product.** $L_{e_t}R_{e_t}+L_{e_t}R_{\vec e_z}$ is the single product $L_{e_t}R_{\,e_t+\vec e_z}$, because the two coefficient matrices share their first factor and add to one of rank one. Its coefficient rank is one, and its operator rank is two, since $\det(e_t+\vec e_z)=0$ and the element $e_t+\vec e_z$ is a zero divisor of rank one. So a product can be singular, and the singular product is still one product; the algebra's zero divisors do not lengthen anything.

**A genuine sum.** $L_{e_t}R_{e_t}+L_{\vec e_x}R_{\vec e_x}$ is the operator $X\mapsto X+\vec e_xX\vec e_x$, and it is **not** a single product: its coefficient matrix is $\operatorname{diag}(1,1,0,0)$, of rank two. Its operator rank is also two, and it is singular, since $X=e_t$ is killed. So two operators of the same operator rank, two, have lengths one and two, and the length is the finer invariant.

**The independence.** The two numbers are independent in both directions. A rank-one image can carry length two: with $E_{11}$ the matrix unit, the operator $X\mapsto\bigl(x_t+2x_x+3x_y+4x_z\bigr)E_{11}$, where the $x_\mu$ are the coordinates of $X$, has image rank one and coefficient rank two, so it is not a single product. And a full-rank operator can carry length one, as the identity shows. The measured range of the coefficient rank on operators of image rank one is $\{1,2\}$: one image dimension costs at most two products and never more.

**The lesson.** The operator rank measures the size of the image and the length measures the complexity of the tensor. For a single product the first is the product of two ranks and the second is one; for a sum the first can only fall and the second only rise. The pair is useful precisely because the two numbers separate the two facts.

## What the Pair Buys and Does Not

**What it buys.** The span of the sixteen products is the whole of $\operatorname{End}_{\mathbb{R}}(\mathbb{H}_{\mathrm{s}})$, so every real-linear operator of the carrier is a sum of at most four products and the pair describes the operator algebra completely. It gives the group of the products of units, of dimension seven, containing the conformal group $SO(2,2)$ through $SL_2(\mathbb{R})\times SL_2(\mathbb{R})$, and the group of the conjugations, $\mathrm{PGL}_2(\mathbb{R})$, of dimension three. It gives the two rulings of the cone of single products, and it gives the length filtration with its determinantal strata.

**What it does not buy.** Nothing that is not a linear operator of the carrier. The norm is a quadratic form and not a linear map; the conjugation of the algebra, $\tilde q\mapsto\tilde q^{\natural}$, is the adjugate and is polynomial of degree one in the entries of the adjugate but not linear in the operator sense; the projective line is a set of ideals and not a set of vectors of the carrier. In particular the spinors of the algebra are the minimal left ideals, and the double cover $SL_2(\mathbb{R})\to SO^{+}(2,1)$ acts on them; that action is a statement about modules, and the operators of the carrier see only its shadow, the conjugation.

**The comparison.** The quaternion category, whose model is an embedding, has an operator algebra strictly larger than its algebra, and the extra dimension is its content. The split-quaternion category, whose model is an isomorphism, has the opposite situation: the operator algebra is the tensor square of the algebra, of dimension sixteen against four, and the content is the whole of that square. The first asks what the model adds; the second asks what the tensor square says about the product. This article is the second question.

## Summary

1. The left and right multiplications are the two commuting copies $A\otimes I$ and $I\otimes B^{\mathsf T}$ of the algebra inside $M_4(\mathbb{R})$, and the sixteen products $L_{e_\mu}R_{e_\nu}$ span the whole ambient.
2. With respect to the trace form the two families are mutual adjoints; with respect to the Frobenius form a left multiplication is self-adjoint exactly when its matrix is symmetric.
3. A two-sided operator is $L_{A}R_{B}(X)=AXB$, of determinant $\det(A)^{2}\det(B)^{2}\ge0$ and trace $\operatorname{tr}A\operatorname{tr}B$; the scaling $(\lambda,\lambda^{-1})$ is its only redundancy.
4. The rank is $\operatorname{rank}A\cdot\operatorname{rank}B\in\{0,1,2,4\}$, never three.
5. The composition is $L_{A}R_{B}L_{A'}R_{B'}=L_{AA'}R_{B'B}$, so the family is $M_2\times M_2^{\mathrm{opp}}$; the conjugations form $\mathrm{PGL}_2(\mathbb{R})$.
6. The coefficient matrix of a single product is $[\tilde q][\tilde p]^{\mathsf T}$, of rank one, and a single product is recognised by $\operatorname{rank}c\le1$; the cone of single products is the Segre cone $\mathbb{P}^3\times\mathbb{P}^3$, of dimension seven.
7. The length is the coefficient rank, in $\{0,1,2,3,4\}$, with strata of dimensions $0,7,12,15,16$.
8. The operator rank and the length are independent: the identity has rank four and length one, and a rank-one image can have length two.
9. The pair describes the whole operator algebra and not the module structure; the spinors stay outside it.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $L_{\tilde q},R_{\tilde q}$ | left and right multiplication on the carrier | *$M_2(\mathbb{R})$ Standard Representation* |
| $L_{\tilde q}R_{\tilde p}$ | the product $L_{\tilde q}R_{\tilde p}$, that is $X\mapsto\tilde qX\tilde p$ | this article |
| $L_{A}R_{B}$ | the same in matrices, $X\mapsto AXB$, of matrix $A\otimes B^{\mathsf T}$ | this article |
| $c(M)$ | the coefficient matrix of $M$ in the basis $L_{e_\mu}R_{e_\nu}$ | this article |
| $\ell(M)$ | the length, equal to $\operatorname{rank}c(M)$ | this article |
| $\langle\cdot,\cdot\rangle_{\operatorname{tr}}$ | the trace form $\operatorname{tr}(XY)$, of signature $(3,1)$ | this article |
| $\langle\cdot,\cdot\rangle_F$ | the Frobenius form $\operatorname{tr}(X^{\mathsf T}Y)$, positive definite | this article |
| $\mathrm{PGL}_2(\mathbb{R})$ | the group of the conjugations, $SO^{+}(2,1)$ | *Split-Quaternion Rotations and the Lorentz Group* |
| $\mathbb{P}^3(\mathbb{R})$ | the projectivised algebra, the space of the rulings | this article |
| $E_{ij}$ | the matrix units, the Peirce corners of the model | *$M_2(\mathbb{R})$ Standard Representation* |

## Further Reading

- Thomas Y. Lam, *The Algebraic Theory of Quadratic Forms* (Benjamin, 1973), for the tensor square of a matrix algebra and the split-quaternion norm.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the double centraliser theorem and the structure of $M_2\otimes M_2$.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for $SL_2(\mathbb{R})\times SL_2(\mathbb{R})\to SO(2,2)$ and the two rulings of the null quadric.
- Joseph Landsberg, *Tensors: Geometry and Applications* (American Mathematical Society, 2012), for the Segre variety, the rank of a tensor and the determinantal strata.
