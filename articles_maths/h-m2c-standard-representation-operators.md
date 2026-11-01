# __$M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation : Operators__

## Introduction

**Two sizes.** The model of the previous article is a $2\times2$ complex map; its carrier is the quaternion algebra, of real dimension four; the operators of the carrier are therefore $4\times4$ real matrices, and the ambient is

$$
\operatorname{End}_{\mathbb{R}}(\mathbb{H})\cong M_4(\mathbb{R}),
$$

of dimension sixteen. The operator layer lives one size above the model, and every statement of this article is a statement about $M_4(\mathbb{R})$, never about $M_2(\mathbb{C})$. This is the first structural difference from the split-quaternion pair, where the carrier was a matrix algebra and the two levels coincided.

**The count.** The left multiplications $L_{\tilde q}$ and the right multiplications $R_{\tilde q}$ are two four-dimensional families inside the ambient; the sixteen products $L_{e_\mu}R_{e_\nu}$ form a basis of the ambient; a single product is a pair $(\tilde q,\tilde p)$ modulo one real scaling; the products reach a seven-dimensional cone; and a general operator needs four of them. The numbers four, sixteen, seven and four are the skeleton of the article.

**The one number that changes.** In the split-quaternion category the operator rank of a single product was $\operatorname{rank}A\cdot\operatorname{rank}B$, ranging over $\{0,1,2,4\}$, because a split quaternion can be a zero divisor. Here every nonzero quaternion is a unit, so the two factors have rank two each and the product has rank four. The operator rank therefore takes only the values four and zero, and **the rank tells nothing at all about the length**. That single collapse is what makes the quaternion operator layer the cleanest of the category.

**Boundaries.** The model, its dictionary, the trace, the determinant, the spectral projectors, the adjugate and the subspaces are the previous article, *$M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation*. The algebra is *Quaternion Algebra*, the norm is *Quaternion Norm and Invertibility*, the unit group is *Quaternion Exponential and Lie Group Structure*. The abstract operator articles, with no matrix in them, are *The One-Sided Operators*, *Two-Sided Operators* and *The Enveloping Operator Algebra*, which this article does not replace; the two-sided operator on the *matrix space* rather than on the carrier is *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*.

**Conventions.** The basis of the algebra is $(e_t,\vec e_x,\vec e_y,\vec e_z)$ with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ cyclically; the model is $\mathsf{M}_2$ with the image $M_2(\mathbb{H})$; the norm is $N$. The left and right multiplication matrices are written $L_{\tilde q},R_{\tilde q}\in M_4(\mathbb{R})$, in the real basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ of the carrier. The coefficient matrix $c(M)$ of an operator is its $4\times4$ array of coordinates in the basis $T_{e_\mu,e_\nu}=L_{e_\mu}R_{e_\nu}$.

## The One-Sided Operators

**The two families.** For $\tilde q$ in the algebra,

$$
L_{\tilde q}(\tilde x)=\tilde q\tilde x,\qquad R_{\tilde q}(\tilde x)=\tilde x\tilde q,
$$

which in the model read $A\mapsto\mathsf{M}_2(\tilde q)A$ and $A\mapsto A\mathsf{M}_2(\tilde q)$, both preserving the image because the image is a subalgebra.

**The two copies.** Each family is a faithful copy of $\mathbb{H}$ inside $M_4(\mathbb{R})$:

$$
L(\mathbb{H})=\{L_{\tilde q}\},\qquad R(\mathbb{H})=\{R_{\tilde q}\},\qquad \dim L(\mathbb{H})=\dim R(\mathbb{H})=4 .
$$

They commute, each is the centraliser of the other, and they intersect in the scalars:

$$
L(\mathbb{H})\cap R(\mathbb{H})=\mathbb{R}\,I_4,\qquad \dim\bigl(L(\mathbb{H})+R(\mathbb{H})\bigr)=7 .
$$

So the two one-sided families, taken together, span a seven-dimensional subspace of the sixteen-dimensional ambient. That seven is not the seven of the cone of products, and the two numbers coincide for a reason that the section on the cone explains.

**The relation between the copies.** In the model, right multiplication is left multiplication read through the adjoint, $R_{\tilde q}=C L_{\tilde q^{*}}C$ with $C(A)=A^{*}$ the conjugate transpose. Since $C$ is conjugate-linear, the identity does not say that the two copies are equal; it says that they are exchanged by an anti-linear isometry of the carrier.

**The invariants.** For a nonzero element,

$$
\operatorname{rank}L_{\tilde q}=\operatorname{rank}R_{\tilde q}=4,\qquad
\det L_{\tilde q}=\det R_{\tilde q}=N(\tilde q)^{2},\qquad
\operatorname{tr}L_{\tilde q}=4q_t .
$$

The determinant is a square, and the trace sees only the scalar part. Both families are therefore inside $GL_4(\mathbb{R})$ once the element is non-zero, and the image of the algebra in each copy is a four-dimensional subspace of the sixteen-dimensional group.

**The adjoints.** With respect to the Frobenius form $\langle X,Y\rangle_F=\operatorname{tr}(X^{\mathsf T}Y)$ of the carrier, the adjoint of $L_{\tilde q}$ is $L_{\tilde q^{*}}$ and the adjoint of $R_{\tilde q}$ is $R_{\tilde q^{*}}$: the transpose of a left multiplication is the left multiplication by the conjugate, which is the real form of the statement that the model is conformal normal. With respect to the trace form $\langle X,Y\rangle_{\operatorname{tr}}=\operatorname{tr}(XY)$, whose restriction to the carrier has signature $(1,3)$, the two families are mutual adjoints:

$$
\langle L_{\tilde q}X,Y\rangle_{\operatorname{tr}}=\operatorname{tr}(\tilde qXY)=\operatorname{tr}(X\,Y\tilde q)=\langle X,R_{\tilde q}Y\rangle_{\operatorname{tr}} .
$$

So the two-sidedness of the adjoint is a property of the indefinite form here as well, and the positive definite form keeps each family to itself.

## The Two-Sided Operator

**Definition.** For a pair $(\tilde q,\tilde p)$,

$$
T_{\tilde q,\tilde p}=L_{\tilde q}R_{\tilde p},\qquad T_{\tilde q,\tilde p}(\tilde x)=\tilde q\,\tilde x\,\tilde p,
$$

a $4\times4$ real matrix. The pair has eight real parameters and the operator has sixteen entries; the map between them is bilinear and far from injective.

**The scaling.** $T_{\lambda\tilde q,\lambda^{-1}\tilde p}=T_{\tilde q,\tilde p}$ for every $\lambda\neq0$, so the effective parameter count is seven. This is the only redundancy: the fibre of $(\tilde q,\tilde p)\mapsto T_{\tilde q,\tilde p}$ over a non-zero product is exactly the scaling orbit, a line.

**Proof of the exactness of the fibre.** If $L_{\tilde q}R_{\tilde p}=L_{\tilde q'}R_{\tilde p'}$, then applying both sides to $e_t$ and using $L_{\tilde q'}^{-1}L_{\tilde q}R_{\tilde p}=R_{\tilde p'}$ gives a right multiplication equal to a left multiplication composed with a right one; acting on the identity and using that the two copies intersect in the scalars yields $\tilde q'=\lambda\tilde q$ and $\tilde p'=\lambda^{-1}\tilde p$.

**The invariants.** For every pair,

$$
\operatorname{rank}T_{\tilde q,\tilde p}\in\{0,4\},\qquad
\det T_{\tilde q,\tilde p}=N(\tilde q)^{2}N(\tilde p)^{2}>0\ \ (\tilde q,\tilde p\neq0),
$$

$$
\operatorname{tr}T_{\tilde q,\tilde p}=4\,q_t\,p_t .
$$

The rank statement and the determinant statement are the same fact: the ambient is four-dimensional, $L_{\tilde q}$ and $R_{\tilde p}$ are both invertible when the parameters are non-zero, so their product is invertible. The trace statement is the surprise: the Gram matrix of the bilinear form $(q,p)\mapsto\operatorname{tr}(L_{\tilde q}R_{\tilde p})$ in the basis of the four units is

$$
\operatorname{tr}\bigl(L_{e_\mu}R_{e_\nu}\bigr)=4\,\delta_{\mu t}\delta_{\nu t},
$$

so the trace of a two-sided operator is four times the product of the two **scalar** parts and vanishes as soon as either parameter is pure. The trace of the operator is therefore a much finer invariant than the trace of the element, and it is the only one of the four numbers above that is not forced by invertibility.

**The conjugation.** The case $\tilde p=\tilde q^{-1}$ is the inner automorphism,

$$
T_{\tilde q,\tilde q^{-1}}(\tilde x)=\tilde q\tilde x\tilde q^{-1},
$$

whose kernel on the pairs of units is $\mathbb{R}^{\times}e_t$, so the effective group is

$$
\mathbb{H}^{\times}/\mathbb{R}^{\times}\cong SO(3),
$$

of dimension three, acting on the pure part as the rotation group. In the split-quaternion category this group was $\mathrm{PGL}_2(\mathbb{R})\cong SO^{+}(2,1)$, of the same dimension but of a different signature: the Lorentz group of $2+1$ dimensions there, the rotation group of $3$ dimensions here. The change is exactly the change of sign of the determinant form.

**The sandwich.** The case $\tilde p=\tilde q$ gives $\tilde x\mapsto\tilde q\tilde x\tilde q$, which is not a conjugation, and its determinant is $N(\tilde q)^{4}$, a fourth power. So the para-hermitian and the hermitian readings of the two-sided operator differ, and only the first is a group action.

## The Kronecker Display

**The display does not transfer.** In the split-quaternion category the carrier was itself a matrix algebra, $M_2(\mathbb{R})$, so the left multiplication was $M\otimes I_2$ and the right one $I_2\otimes M^{\mathsf T}$, and the two-sided operator was displayed as the Kronecker product $A\otimes B^{\mathsf T}$. Here the carrier is the division algebra $\mathbb{H}$, which is not a tensor product of two smaller real algebras, so no such factorisation exists: $L_{\tilde q}$ is a $4\times4$ matrix that does not split as a tensor product of two $2\times2$ real matrices.

**The reason in one line.** The Kronecker display of the split case is the display of a matrix algebra acting on itself, and a division algebra acting on itself has no matrix units to split along.

**What replaces it.** The coefficient matrix. The sixteen operators

$$
T_{e_\mu,e_\nu}=L_{e_\mu}R_{e_\nu}\qquad(\mu,\nu\in\{t,x,y,z\})
$$

form a basis of the ambient, because the map

$$
\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}\longrightarrow\operatorname{End}_{\mathbb{R}}(\mathbb{H}),\qquad \tilde q\otimes\tilde p\longmapsto L_{\tilde q}R_{\tilde p}
$$

is an isomorphism of sixteen-dimensional real spaces. Every operator $M$ therefore has coordinates $c_{\mu\nu}(M)$ in that basis, and for a single product

$$
c\bigl(T_{\tilde q,\tilde p}\bigr)=\tilde q\,\tilde p^{\,\mathsf T},
$$

the outer product of the two coordinate vectors, a matrix of rank one. The array $c(M)$ is the object that decides every question of the rest of this article.

**Where the display does appear.** Over $\mathbb{C}$. The complexified algebra is $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}=M_2(\mathbb{C})$, the biquaternion algebra, and there the display is exact: the operator $Y\mapsto AYB$ on the matrix space is $A\otimes B^{\mathsf T}$ in the row-major vectorisation. The quaternion layer of this article is the slice of that complex layer on which both parameters lie in the real form $\mathbb{H}$, and the coefficient matrix is the real bookkeeping of that slice. The complex layer is the subject of *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*.

## The Rank and the Invariants

**Theorem (the rank never takes an intermediate value).** For every pair,

$$
\operatorname{rank}T_{\tilde q,\tilde p}=0\ \text{if }\tilde q=0\text{ or }\tilde p=0,\qquad
\operatorname{rank}T_{\tilde q,\tilde p}=4\ \text{otherwise}.
$$

**Proof.** $L_{\tilde q}$ is invertible exactly when $\tilde q\neq0$, because the algebra is a division algebra; the same holds for $R_{\tilde p}$; a product of invertible maps is invertible.

**The consequence for the cone.** The cone of single products, minus its vertex, lies entirely inside $GL_4(\mathbb{R})$, the open dense subset of the ambient. So every non-zero product is an invertible operator, and no product is a projection, a nilpotent or a rank-one map. This is the sharpest single difference from the split-quaternion category, where the products filled the singular strata as well.

**The table.**

| quantity | value for $T_{\tilde q,\tilde p}$ | depends on |
|---|---|---|
| operator rank | $4$ if both parameters are non-zero, $0$ otherwise | nothing else |
| trace | $4q_tp_t$ | the two scalar parts |
| determinant | $N(\tilde q)^{2}N(\tilde p)^{2}$ | the two norms |
| coefficient rank | $1$ | nothing |

The first and last rows are constant on the cone, and the two middle rows are the only numerical invariants. The asymmetry is the point: the operator rank of a product carries one bit of information, the length carries none, and the numerical invariants of the pair do not reach the length at all.

**The comparison with the split case.** There the four possible ranks $0,1,2,4$ were the image of the four possible pairs of element ranks, and the rank was a genuine numerical invariant of the product. Here the rank is a dichotomy, and everything that varies has moved into the trace and the determinant. A category whose products are all invertible has no interesting rank theory, and the length is the only stratification left.

## The Pair as a Semigroup

**Composition.** For two products,

$$
T_{\tilde q,\tilde p}\,T_{\tilde q',\tilde p'}=T_{\tilde q\tilde q',\ \tilde p'\tilde p},
$$

so the family is a copy of $\mathbb{H}\times\mathbb{H}^{\mathrm{opp}}$ inside the algebra of all operators, and not a copy of $\mathbb{H}\times\mathbb{H}$: the second slot composes in the reverse order. The reversal is associativity showing through, and it is the same law as in the split category.

**The units.** The invertible members are the products of two non-zero elements, with inverse $T_{\tilde q^{-1},\tilde p^{-1}}$, and they form the group

$$
\bigl(\mathbb{H}^{\times}\times\mathbb{H}^{\times}\bigr)/\mathbb{R}^{\times},
$$

of dimension seven.

**The automorphisms.** The inner automorphisms appear as $T_{\tilde q,\tilde q^{-1}}$ and form the subgroup $\mathbb{H}^{\times}/\mathbb{R}^{\times}\cong SO(3)$ of dimension three. The four dimensions between the two groups are the sandwiches with $\tilde q\tilde p\neq e_t$.

**The absence of matrix units.** The algebra has no idempotent, so it has no system of matrix units, and the sixteen basis operators $T_{e_\mu,e_\nu}$ are a basis of the ambient and not a system of units in the algebra. The Peirce frame of the split category has no counterpart, and the corner structure of that frame is replaced here by the single fact that the two copies intersect in the scalars.

**What survives from the semigroup.** The composition law, the units, the automorphisms, and the identity $T_{e_t,e_t}=I_4$, which is a product of length one. So the family is a semigroup with unit, closed under inversion on its units, and it does not contain the whole group $GL_4(\mathbb{R})$: it contains only the operators of the form $L_{\tilde q}R_{\tilde p}$, a seven-dimensional submanifold of the sixteen-dimensional group.

## The Cone and the Coefficient Matrix

**The map.** Put $\beta(\tilde q,\tilde p)=T_{\tilde q,\tilde p}$. It is bilinear, so its image is a cone with vertex at the zero operator and not a linear subspace:

$$
\beta:\mathbb{H}\times\mathbb{H}\longrightarrow M_4(\mathbb{R}).
$$

**Theorem (the cone is the Segre cone).** The image of $\beta$ is

$$
\operatorname{Im}\beta=\{M:\operatorname{rank}c(M)\le1\},
$$

the affine cone over the Segre variety $\mathbb{P}^{3}(\mathbb{R})\times\mathbb{P}^{3}(\mathbb{R})$, of real dimension $7$.

**Proof.** A single product has $c=\tilde q\tilde p^{\,\mathsf T}$ of rank one by the display; conversely a rank-one array $c=uv^{\mathsf T}$ is the coefficient matrix of $T_{\tilde q,\tilde p}$ with $\tilde q=\sum u_\mu e_\mu$ and $\tilde p=\sum v_\nu e_\nu$, since the basis is a basis. The dimension is $3+3+1=7$, the dimension of the pair modulo the scaling.

**The membership test.** An operator is a single product **if and only if** its coefficient matrix has rank exactly one, and then the two factors are the two singular vectors. The test is exact and needs no solving, and it is the reason the two-sided operator of this category is decidable: a given $4\times4$ matrix is or is not of the form $\tilde q\,\cdot\,\tilde p$.

**The additive failure.** The map $\beta$ is not additive, so the sum of two products is in general not a product; the smallest witness is in the next section. The cone is therefore a genuine cone and not a subspace, and the difference between the cone and its linear span, $\dim\operatorname{span}=16$ against $\dim\operatorname{cone}=7$, is the measure of the failure.

**The two rulings.** The products with $\tilde p$ fixed form a copy of the algebra, of dimension four, and so do the products with $\tilde q$ fixed. Two members of different families meet in exactly one point, the product of the two fixed parameters. This is the operator-level picture of the two rulings of the Segre variety, and it is the exact analogue of the rulings of the split-quaternion null quadric, transported from the algebra to the operator space.

**The slice.** The cone of this article is the real slice of the complex cone of the biquaternion pair, taken on the pairs with both parameters in the real form. The complex cone is the same construction over $\mathbb{C}$, where the ambient is $M_4(\mathbb{C})$ and the coefficient matrix is a complex $4\times4$; the real slice is the subset on which the complex conjugation of the pair is the quaternionic one.

## The Length

**Definition.** The **length** of an operator is the least number of single products of which it is a sum,

$$
\ell(M)=\min\Bigl\{k:\ M=\sum_{i=1}^{k}T_{\tilde q_i,\tilde p_i}\Bigr\}.
$$

**Theorem (the length is the coefficient rank).** For every operator of the ambient,

$$
\ell(M)=\operatorname{rank}c(M)\in\{0,1,2,3,4\}.
$$

**Proof.** A sum of $k$ products has a coefficient matrix that is a sum of $k$ arrays of rank one, hence of rank at most $k$, so $\ell\ge\operatorname{rank}c$. Conversely an array of rank $r$ is a sum of $r$ arrays of rank one, and each is the coefficient matrix of a product by the membership test, so $\ell\le\operatorname{rank}c$.

**The strata.** The sets of operators of length at most $r$ are the determinantal sets $\{\operatorname{rank}c\le r\}$ of a $4\times4$ array, of dimensions

| $r$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| $\dim\{\operatorname{rank}c\le r\}$ | $0$ | $7$ | $12$ | $15$ | $16$ |

so four products always suffice, a generic operator needs exactly four, the single products are the smallest closed stratum, and the operators of length two fill a closed set of dimension twelve.

**The measured behaviour.** A sum of $k$ random products has coefficient rank $k$ for $k=1,2,3,4$ and coefficient rank four for every larger $k$, so the length saturates at four and the distribution is as the table predicts. The single products are a set of measure zero in the ambient, and the operators of length four are the complement of a closed set of dimension fifteen, hence open and dense.

**What the strata are not.** They are not strata of the operator's rank, which is four on almost everything. They are strata of the coefficient array, an artefact of the chosen basis of products, and their dimensions $7,12,15$ are the dimensions of the determinantal varieties of a $4\times4$ matrix. The length is a coordinate-dependent notion in that sense and an invariant in another: it does not depend on the basis of the carrier, because it counts products, which are basis-free objects.

## The Two Ranks

**The two numbers.** The **operator rank** is the rank of the four-by-four matrix; the **length** is the coefficient rank. In this category the first takes two values and the second takes five, and neither determines the other. Three witnesses settle the question.

**The identity.** $T_{e_t,e_t}=I_4$ has operator rank four and length one, so a maximal operator rank costs a single product. Every non-zero product has operator rank four, so this witness is generic in the rank and extremal in the length.

**A singular sum.** $T_{e_t,e_t}+T_{\vec e_x,\vec e_x}$ is the operator

$$
\tilde x\longmapsto \tilde x+\vec e_x\tilde x\vec e_x ,
$$

which kills both $e_t$ and $\vec e_x$, because $\vec e_x e_t\vec e_x=\vec e_x^{2}=-e_t$ and $\vec e_x\vec e_x\vec e_x=-\vec e_x$. Its kernel contains the plane $\operatorname{span}\{e_t,\vec e_x\}$, so its operator rank is at most two and in fact exactly two; its coefficient matrix is $\operatorname{diag}(1,1,0,0)$, of rank two. So the sum is **not** a single product, and it is singular although no single product is singular. Its operator rank has fallen below the value four that every product attains, and its length has risen to two.

**A full-rank sum.** A sum of two generic products has operator rank four, like a single product, and length two. So equal operator rank, unequal length, in the sharpest available form.

**The independence.** The operator rank is a two-valued invariant of the product and a much finer invariant of the sum, but it cannot separate length one from length four, since both occur at rank four. The length separates them, and it is the only stratification of the cone. The lesson of the split-quaternion category, that the two numbers measure the size of the image and the complexity of the tensor, becomes here the sharper statement that the size of the image is almost always maximal and only the complexity varies.

## What the Pair Buys and Does Not

**What it buys.** The sixteen products span the ambient, so every real-linear operator of the carrier is a sum of at most four of them and the pair describes the operator algebra completely. It gives the seven-dimensional group of products of units, with the three-dimensional group $SO(3)$ of the inner automorphisms inside it, and it gives the seven-dimensional cone of single products with its two rulings. It gives the length filtration and, through it, the statement that the four products always suffice and are generically necessary.

**What it does not buy.** The model is not the algebra, so the operator algebra is strictly larger than the algebra in a way it was not in the split case: there the carrier was the algebra and the ambient was its tensor square; here the carrier is a four-dimensional real form of a matrix algebra and the ambient is the full $M_4(\mathbb{R})$, in which the algebra sits as a proper subspace through two different embeddings, $L$ and $R$. The difference between the two categories is exactly this: the split case asks what the tensor square says about the product, and the quaternion case asks what the ambient says about a subalgebra that is not all of it.

**What stays outside.** The complex structure, the spectral projectors and the Hermitian metric are properties of the *model*, not of the operator layer. The operator layer sees only the real form: it knows that $\mathbb{H}$ is a division algebra, that its unit group is a three-sphere up to scale, and that its automorphism group is $SO(3)$, and it cannot see the $2\times2$ complex matrices that make those facts computable. The spinors, the minimal left ideals and the Peirce frame of the split category have no counterpart, because a division algebra has no proper one-sided ideal.

## Summary

1. The carrier is $\mathbb{H}$, of real dimension four, and the ambient is $M_4(\mathbb{R})$, of dimension sixteen; the model of size two over $\mathbb{C}$ plays no role in the operator layer.
2. The two one-sided families are four-dimensional, commute, intersect in the scalars, and span a seven-dimensional subspace of the ambient.
3. The two-sided operator $T_{\tilde q,\tilde p}(\tilde x)=\tilde q\tilde x\tilde p$ has rank four whenever both parameters are non-zero, determinant $N(\tilde q)^{2}N(\tilde p)^{2}>0$ and trace $4q_tp_t$.
4. The Kronecker display of the split category does not transfer, because a division algebra is not a tensor product of smaller real algebras; the coefficient matrix replaces it, and the display reappears over $\mathbb{C}$ in the biquaternion layer.
5. The sixteen operators $L_{e_\mu}R_{e_\nu}$ form a basis, and $c(T_{\tilde q,\tilde p})=\tilde q\tilde p^{\,\mathsf T}$ has rank one.
6. The cone of single products is the Segre cone $\mathbb{P}^{3}\times\mathbb{P}^{3}$, of dimension seven, and the membership test is $\operatorname{rank}c\le1$.
7. The composition is $T_{\tilde q,\tilde p}T_{\tilde q',\tilde p'}=T_{\tilde q\tilde q',\tilde p'\tilde p}$, the units form a group of dimension seven, and the inner automorphisms form $SO(3)$.
8. The length is the coefficient rank, in $\{0,\dots,4\}$, with strata of dimensions $0,7,12,15,16$; four products always suffice and generically are needed.
9. The operator rank is two-valued and the length five-valued; the identity has rank four and length one, and the sum $T_{e_t,e_t}+T_{\vec e_x,\vec e_x}$ is a singular operator of rank two and length two.
10. The operator algebra is strictly larger than the algebra, and the excess is the content of the category.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $L_{\tilde q},R_{\tilde q}$ | left and right multiplication on the carrier, $4\times4$ real matrices | this article |
| $T_{\tilde q,\tilde p}$ | the product $L_{\tilde q}R_{\tilde p}$, that is $\tilde x\mapsto\tilde q\tilde x\tilde p$ | this article |
| $T_{e_\mu,e_\nu}$ | the sixteen basis operators of the ambient | this article |
| $c(M)$ | the coefficient matrix of $M$ in that basis | this article |
| $\ell(M)$ | the length, equal to $\operatorname{rank}c(M)$ | this article |
| $\langle\cdot,\cdot\rangle_{\operatorname{tr}}$ | the trace form $\operatorname{tr}(XY)$, of signature $(1,3)$ | *$M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation* |
| $\langle\cdot,\cdot\rangle_F$ | the Frobenius form, positive definite | this article |
| $SO(3)$ | the group of the inner automorphisms, $\mathbb{H}^{\times}/\mathbb{R}^{\times}$ | *Quaternion Rotations and the Lorentz Group* |
| $\mathbb{P}^{3}(\mathbb{R})$ | the projectivised algebra, the space of the rulings | this article |
| $N$ | the norm, equal to $\det\mathsf{M}_2(\tilde q)$ | *Quaternion Norm and Invertibility* |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the double centraliser theorem in the division-algebra case and the structure of $\mathbb{H}\otimes\mathbb{H}^{\mathrm{opp}}$.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the two-sided action of $\mathbb{H}$ and the double cover $SU(2)\to SO(3)$.
- Joseph Landsberg, *Tensors: Geometry and Applications* (American Mathematical Society, 2012), for the Segre variety, the rank of a tensor and the determinantal strata.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the left and right regular representations of $\mathbb{H}$ and their intersection.
