# __$M_4(\mathbb{R})_{\mathbb{H}_L}$ Regular Representation : Operators__

## Introduction

**The same operators, a second reading.** The carrier of this article is the quaternion algebra, of real dimension four, and the ambient is

$$
\operatorname{End}_{\mathbb{R}}(\mathbb{H})\cong M_4(\mathbb{R}),
$$

of dimension sixteen. That is exactly the carrier and the ambient of *$M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation : Operators*. The two articles therefore describe the **same** operators. What changes is the frame: there the carrier was reached through the $2\times2$ complex model, here through the Cayley matrix. This article does not repeat the cone, the membership test or the length theorem; it establishes the identity of the two readings, and then records what the regular frame makes visible and what it cannot show.

**What is genuinely new.** One thing, and it is structural. The coefficient array of an operator and the matrix of the operator are both $4\times4$ real arrays in this frame, because the carrier and the ambient are both four-dimensional over $\mathbb{R}$. Nowhere else in Part VI does that happen: in the split-quaternion category the coefficient array was $2\times2$ and the operator matrix $4\times4$; in the complex model the operator matrix is $4\times4$ and the coefficient array $4\times4$ as well, but the carrier of the complex model is eight-real-dimensional and the operator acts on a space of matrices. Here the two arrays are of the same size and describe the same linear map on the same four-dimensional carrier, so they can be compared **entrywise**, and the comparison is the content.

**The frame dictionary, in one line.** A matrix in the ambient acts on coordinate columns in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$; its $(\mu,\nu)$ entry is the $\mu$-th coordinate of the image of $\tilde e_\nu$; and the sixteen matrices $T_{e_\mu,e_\nu}=L_{e_\mu}R_{e_\nu}$ are a basis of the ambient in which the coefficient array of an operator is read. The two bases of the ambient — the sixteen matrix units and the sixteen products — are the two readings.

**Boundaries.** The model, the Cayley display, the trace, the determinant, the adjugate and the subspaces are *$M_4(\mathbb{R})_{\mathbb{H}_L}$ Regular Representation*. The operators, the cone, the length theorem and the two-ranks discussion are *$M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation : Operators*, whose results hold verbatim here and are cited rather than reproved. The abstract one-sided and two-sided operators are *The One-Sided Operators* and *Two-Sided Operators on the Quaternion Algebra*; the enveloping algebra is *The Enveloping Operator Algebra of the Quaternion Algebra and the Bi-module Structure*.

**Conventions.** The basis is $(e_t,\vec e_x,\vec e_y,\vec e_z)$; $\mathsf{M}_4$ is the Cayley matrix of left multiplication; $L_{\tilde q}=\mathsf{M}_4(\tilde q)$ and $R_{\tilde q}$ is right multiplication, with $R_{\tilde q}=D\mathsf{M}_4(\tilde q)^{\mathsf T}D$ and $D=\operatorname{diag}(1,-1,-1,-1)$; $T_{\tilde q,\tilde p}=L_{\tilde q}R_{\tilde p}$; $c(M)$ is the coefficient array of $M$ in the basis of the sixteen products.

## The One-Sided Operators

**The two copies, in the Cayley frame.** The left family is the image of the model itself:

$$
L(\mathbb{H})=\mathsf{M}_4(\mathbb{H})=\{\mathsf{M}_4(\tilde q)\},
$$

so the Cayley matrices *are* the left multiplications, entrywise, and the display of the model article is a display of this family. The right family is the signed transpose of the same set:

$$
R(\mathbb{H})=D\,\mathsf{M}_4(\mathbb{H})^{\mathsf T}D .
$$

**The two frames of one statement.** In the complex model the two families were related by the conjugate transpose, an anti-linear operation of the ambient $M_2(\mathbb{C})$; here they are related by a signed transpose, a linear operation of $M_4(\mathbb{R})$. The regular frame therefore turns an anti-linear relation into a linear one, at the price of losing the complex structure that the anti-linearity encoded. This is the general trade of realification, and it is worth naming: **the conjugate transpose of the complex model becomes the signed transpose of the regular model.**

**The intersection and the sum.** The two families are four-dimensional, they commute, their intersection is the scalar line, and their sum has dimension seven:

$$
\dim L(\mathbb{H})=4,\qquad \dim R(\mathbb{H})=4,\qquad \dim\bigl(L(\mathbb{H})+R(\mathbb{H})\bigr)=7 .
$$

The seven is visible in the Cayley frame without any computation: a general element of the sum is $q_tI_4$ plus the three skew-symmetric generators plus the three signed transposes of them, and these seven matrices are linearly independent while the identity is counted once.

**The adjoints.** With respect to the Frobenius form of the ambient, the adjoint of $L_{\tilde q}$ is $L_{\tilde q}^{\,T}=D R_{\tilde q}D$, which is not in $L(\mathbb{H})$ but in $R(\mathbb{H})$: the adjoint operation exchanges the two families. With respect to the trace form it is the same statement with the parameters swapped, $\langle L_{\tilde q}X,Y\rangle_{\operatorname{tr}}=\langle X,R_{\tilde q}Y\rangle_{\operatorname{tr}}$. So in the regular frame the two-sidedness of the adjoint is stated once and read twice, and the exchange is a linear map of the ambient rather than a conjugation.

**The sixteen products.** In the regular frame the products are the natural matrices of the reading, and their entries are $0,\pm1$: the $\nu'$-th column of $T_{e_\mu,e_\nu}$ is the coordinate column of $e_\mu\tilde e_{\nu'}\tilde e_\nu$, a product of three basis elements and hence a basis element up to sign. So the sixteen matrices are signed permutation matrices, orthogonal, of determinant one:

$$
T_{e_\mu,e_\nu}^{\mathsf T}T_{e_\mu,e_\nu}=I_4,\qquad \det T_{e_\mu,e_\nu}=1,\qquad \operatorname{rank}T_{e_\mu,e_\nu}=4 .
$$

**The finite group.** The thirty-two matrices $\pm T_{e_\mu,e_\nu}$ form a finite subgroup of $SO(4)$ of order $32$, the image of the quaternion group $Q_8$ acting on both sides, with kernel $\{\pm(e_t,e_t)\}$. It is the regular reading of the fact that the products of four unit parameters are again unit parameters: there the group is continuous, here it is the finite group generated by the four units.

**The trace table.** The only one of the sixteen with a nonzero trace is $T_{e_t,e_t}=I_4$:

$$
\operatorname{tr}T_{e_\mu,e_\nu}=4\,\delta_{\mu t}\delta_{\nu t}.
$$

The table is the regular reading of the general formula $\operatorname{tr}T_{\tilde q,\tilde p}=4q_tp_t$: among the basis operators only the identity has a scalar part in both slots.

## The Two-Sided Operator

**Definition and invariants.** For a pair $(\tilde q,\tilde p)$,

$$
T_{\tilde q,\tilde p}=L_{\tilde q}R_{\tilde p},\qquad T_{\tilde q,\tilde p}(\tilde x)=\tilde q\,\tilde x\,\tilde p,
$$

with

$$
\operatorname{rank}T_{\tilde q,\tilde p}\in\{0,4\},\qquad
\det T_{\tilde q,\tilde p}=N(\tilde q)^{2}N(\tilde p)^{2},\qquad
\operatorname{tr}T_{\tilde q,\tilde p}=4q_tp_t .
$$

All three are inherited from the complex reading; the third is the one that needs care, since the trace of the operator is not the product of the traces of its factors.

**Why the trace is $4q_tp_t$.** The bilinear form $(q,p)\mapsto\operatorname{tr}(L_{\tilde q}R_{\tilde p})$ has Gram matrix $4\,E_{tt}$ in the basis of the four units, so it is the rank-one form $4q_tp_t$. In the regular frame this is visible from the trace table of the previous section: only the pair $(e_t,e_t)$ contributes.

**The scaling.** The pair has eight real parameters and the operator has sixteen entries; the kernel of the map is the line of scalings $(\lambda\tilde q,\lambda^{-1}\tilde p)$, so the effective parameter count is seven and the fibre over a non-zero product is one real line.

**The group.** The units of the pair form the group

$$
\bigl(\mathbb{H}^{\times}\times\mathbb{H}^{\times}\bigr)/\mathbb{R}^{\times},
$$

of dimension seven, and the inner automorphisms $T_{\tilde q,\tilde q^{-1}}$ form $\mathbb{H}^{\times}/\mathbb{R}^{\times}\cong SO(3)$, acting on the pure part as the rotation group. In the regular frame the second group is visible as the group of conjugations of the Cayley matrices by the units, which is the classical statement that $SU(2)$ covers $SO(3)$ twice; the double cover is the sign ambiguity of $\tilde q$.

**The real block structure.** A two-sided operator commutes with nothing in general, but its action on the carrier can be read block by block: for a pure parameter the Cayley matrix splits as two identical blocks, so $T_{\tilde q,\tilde p}$ acts as two copies of the same $2\times2$ block on the two invariant planes of the complex structure. The doubling is the realification, and it is the operator-level reason why the determinant of every product is a square.

## The Kronecker Display and the Two Arrays

**The failure, restated.** The carrier is a division algebra and not a matrix algebra, so no Kronecker factorisation exists: $L_{\tilde q}$ is not $A\otimes I$ for any $2\times2$ real $A$. The complex model does have a display, because its model is a matrix algebra; so the display is a property of the *complex* reading and not of the carrier.

**The two arrays.** In the regular frame there are two $4\times4$ real arrays attached to an operator $M$:

- the **Cayley array** of $M$, that is the matrix of $M$ in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ of the carrier;
- the **coefficient array** $c(M)$, that is the coordinates of $M$ in the basis $T_{e_\mu,e_\nu}$ of the ambient.

For a single product,

$$
c\bigl(T_{\tilde q,\tilde p}\bigr)=\tilde q\,\tilde p^{\,\mathsf T},
$$

of rank one, while the Cayley array is $L_{\tilde q}R_{\tilde p}$, of rank four. The two arrays of a product are therefore maximally different: the first is a conformal matrix with all singular values $\sqrt{N(\tilde q)N(\tilde p)}$, the second an outer product.

**Theorem (the two arrays are related by a fixed linear map).** There is a linear isomorphism $\Phi$ of $M_4(\mathbb{R})$ with itself, independent of the operator, such that

$$
M=\Phi\bigl(c(M)\bigr)
$$

for every operator, and $\Phi$ is given in the two bases by the sixteen matrices $T_{e_\mu,e_\nu}$ themselves.

**Proof.** Both arrays are coordinate systems of the same sixteen-dimensional space, so the change of basis is a fixed linear map; its matrix has the sixteen Cayley arrays of the products as columns.

**What the comparison buys.** Since the two arrays have the same size, the questions of the operator layer can be asked of either. The rank of the array is the length, in the coefficient reading, and the rank of the operator is the rank of the array in the Cayley reading. So the length and the operator rank become two ranks of two arrays of the *same* size, attached to the *same* operator, and the fact that they differ is no longer a difference of size between the carrier and the algebra but a genuine property of the two coordinate systems. This is the sharpest formulation of the phenomenon, and it is available only in this frame.

**The display that does exist.** Over $\mathbb{C}$, on the complexified carrier, the operator $Y\mapsto AYB$ is $A\otimes B^{\mathsf T}$ in the row-major vectorisation, of size $4\times4$ over $\mathbb{C}$. That is the biquaternion layer, treated in *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*; the regular frame of this article is the real slice on which both parameters lie in $\mathbb{H}$.

## The Rank and the Invariants

**The rank ladder is empty.** The second rank of the split-quaternion category, the operator rank $\operatorname{rank}A\cdot\operatorname{rank}B$, is not a ladder here: it is the two-point set $\{0,4\}$. Every nonzero product is invertible, so the cone of products minus its vertex lies inside $GL_4(\mathbb{R})$.

**The table.**

| quantity | value on $T_{\tilde q,\tilde p}$ | on the sixteen basis operators |
|---|---|---|
| operator rank | $4$ if both parameters non-zero, else $0$ | $4$ for all sixteen |
| trace | $4q_tp_t$ | $4$ for $T_{tt}$, $0$ otherwise |
| determinant | $N(\tilde q)^{2}N(\tilde p)^{2}$ | $1$ for all sixteen |
| coefficient rank | $1$ | $1$ for all sixteen |
| Frobenius norm$^{2}$ | $4\,N(\tilde q)N(\tilde p)$ | $4$ for all sixteen |

**The reading of the table.** All sixteen basis operators have length one, operator rank four, determinant one and coefficient rank one: they are simultaneously extremal in the length and generic in the rank, and they are the clearest possible witness of the independence of the two numbers. A single column of this table settles the question that the whole of the split-quaternion category spent a section on.

**The invariants of the pair.** Only two of the four numbers above vary on the cone: the trace, which sees the two scalar parts, and the determinant and norm, which see the two norms. So the numerical content of a product is exactly the two scalars and the two norms, and the rank content is one bit. The cone is seven-dimensional and its numerical invariants span a set of dimension four, with the scaling making the count consistent.

## The Pair as a Semigroup

**Composition.** $T_{\tilde q,\tilde p}T_{\tilde q',\tilde p'}=T_{\tilde q\tilde q',\tilde p'\tilde p}$, with the reversal in the second slot; the family is a copy of $\mathbb{H}\times\mathbb{H}^{\mathrm{opp}}$.

**The units.** Invertible members are the products of two non-zero elements, with inverse $T_{\tilde q^{-1},\tilde p^{-1}}$, forming the seven-dimensional group of the previous section.

**The isometries.** A product has four equal singular values $\sqrt{N(\tilde q)N(\tilde p)}$, so it is orthogonal exactly when $N(\tilde q)N(\tilde p)=1$, a condition invariant under the scaling and therefore a six-dimensional family inside the seven-dimensional cone. The multiplicative members among them are those with $\tilde p=\tilde q^{-1}$, which is the three-dimensional group $SO(3)$. So the intersection of the pair with $O(4)$ is strictly larger than the group of automorphisms, and the excess consists of the two-sided rotations with no conjugation in them.

**The multiplicative members.** A member of the pair is an algebra endomorphism of the carrier exactly when $\tilde p=\tilde q^{-1}$, by the double centraliser theorem: an endomorphism commuting with the left action is a right multiplication, and it is an algebra map exactly when the parameter is a unit acting by conjugation.

## The Cone and the Coefficient Matrix

**The cone and its dimension.** The image of $(\tilde q,\tilde p)\mapsto T_{\tilde q,\tilde p}$ is the cone of operators of coefficient rank one, of real dimension seven inside sixteen:

$$
\operatorname{Im}\beta=\{M:\operatorname{rank}c(M)\le1\},
$$

the Segre cone over $\mathbb{P}^{3}(\mathbb{R})\times\mathbb{P}^{3}(\mathbb{R})$. The result is the same as in the complex reading, because the operator is the same; only its coordinates have changed.

**The membership test.** An operator is a single product exactly when its coefficient array has rank one, and then the two parameters are the two singular vectors of that array. In the regular frame the test can be stated without leaving the ambient: $M$ is a product exactly when the sixteen coordinates of $M$ in the basis $T_{e_\mu,e_\nu}$ form a rank-one array.

**The two rulings.** Fixing $\tilde p$ gives a copy of the algebra inside the cone, of dimension four, and fixing $\tilde q$ gives another; two members of different families meet in one point. In the regular frame the two rulings are visible as the two statements $L(\mathbb{H})$ and $R(\mathbb{H})$: the first ruling is the left copy parametrised by $\tilde q$, the second the right copy parametrised by $\tilde p$.

**The vertex and the base.** The vertex is the zero operator; the base is the Segre variety $\mathbb{P}^{3}\times\mathbb{P}^{3}$, of dimension six, and its two rulings are the two projective families. The base is the projectivisation of the algebra in each slot, which is the projective space of the element: this is the only place in the quaternion category where projective geometry appears, and it appears on the operator side and not on the algebra side, because the algebra has no projective geometry of its own (its null cone is a point).

**The stratification.** The cone is smooth away from the vertex: the rank-one locus minus the origin is a smooth manifold of dimension seven, the image of the submersion $(\tilde q,\tilde p)\mapsto\tilde q\tilde p^{\mathsf T}$ whose fibres are the scaling lines. So the only singular point is the vertex, and no intermediate stratum exists, unlike the split-quaternion cone, whose singular locus contained the null quadric and its rulings.

## The Length

**The theorem, restated in this frame.** With $c(M)$ the coefficient array,

$$
\ell(M)=\operatorname{rank}c(M)\in\{0,1,2,3,4\},
$$

and the strata $\{\operatorname{rank}c\le r\}$ have dimensions $0,7,12,15,16$.

**The regular reading of the strata.**

- Length zero: the zero operator.
- Length one: the cone, of dimension seven; its base is the Segre variety.
- Length two: a determinantal variety of dimension twelve, which contains the sums of two products and nothing else; the singular operators of the form $T_{e_t,e_t}+T_{\vec e_x,\vec e_x}$ live here.
- Length three: dimension fifteen, the complement of the length-two stratum inside a hypersurface.
- Length four: the complement of a closed algebraic set, hence open and dense.

**Why four is generic.** The generic operator of the sixteen-dimensional ambient has a coefficient array of full rank four, so four products suffice and are generically necessary; three products suffice on a set of dimension fifteen, that is on a hypersurface, and two on a set of dimension twelve.

**The measured behaviour.** A sum of $k$ random products has coefficient rank $\min(k,4)$ for $k=1,2,3,4$ and coefficient rank four for every larger $k$, in this frame as in the other, because the coefficient array is the same array. The regular frame adds nothing to the theorem and everything to the picture: the coefficient array is now the array of the operator's coordinates among the sixteen products, which is the array the next section compares with the operator itself.

**The extremal witnesses, in the regular frame.** In the Cayley frame the two basis products are diagonal:

$$
T_{e_t,e_t}=I_4=\operatorname{diag}(1,1,1,1),\qquad
T_{\vec e_x,\vec e_x}=\operatorname{diag}(-1,-1,1,1),
$$

the second being the operator $\tilde x\mapsto\vec e_x\tilde x\vec e_x$, which fixes the plane $\operatorname{span}(\vec e_y,\vec e_z)$ and reverses the plane $\operatorname{span}(e_t,\vec e_x)$. Both are products of length one and both have rank four, with determinant one. Their sum is

$$
T_{e_t,e_t}+T_{\vec e_x,\vec e_x}=\operatorname{diag}(0,0,2,2),
$$

twice the projection onto $\operatorname{span}(\vec e_y,\vec e_z)$: it kills both $e_t$ and $\vec e_x$, has rank two and coefficient rank two, and is not a product. The regular reading makes the annihilation visible at a glance, and it shows that the loss of rank comes from a cancellation between two diagonal matrices rather than from any singularity of the factors.

## The Two Ranks

**The two numbers, and where they part.** The operator rank is the rank of the Cayley array; the length is the rank of the coefficient array. In this frame the two arrays are both $4\times4$, so the comparison is between two ranks of two arrays of the same size, and the content is that they are not the same rank:

$$
\operatorname{rank}_{\text{Cayley}}(M)\ \text{against}\ \operatorname{rank}_{\text{coeff}}(M).
$$

**The four witnesses.**

| operator | Cayley rank | coefficient rank | comment |
|---|---|---|---|
| $0$ | $0$ | $0$ | the vertex |
| $T_{e_t,e_t}=I_4$ | $4$ | $1$ | a unit of length one |
| $T_{\vec e_x,\vec e_x}$ | $4$ | $1$ | a product of determinant one with a negative eigenvalue |
| $T_{e_t,e_t}+T_{\vec e_x,\vec e_x}$ | $2$ | $2$ | a sum that is singular and not a product |
| a generic sum of two products | $4$ | $2$ | invertible, length two |

**The reading.** The first column can take the values $0,2,4$ on the cone and on its small sums, and always $4$ on the open dense set; the second takes $0,1,2,3,4$. Neither determines the other: rank four occurs at length one and at length four, and length one occurs at rank two and at rank four. This is the sharpest statement of the independence available in the category, and the regular frame is where it can be written with two arrays of one size.

**The general rule.** The two ranks measure two different things: the Cayley rank measures the size of the image of the operator on the carrier, the coefficient rank measures the number of products needed. The first is a property of the operator as a map; the second is a property of the operator as a tensor in $\mathbb{H}\otimes\mathbb{H}$. Two different structures on the same sixteen-dimensional space, and the regular frame displays both.

## What the Pair Buys and Does Not

**What it buys.** The operator algebra of the carrier, completely: every real-linear operator is a sum of at most four products, the products form a seven-dimensional cone, the units of the pair form a seven-dimensional group with $SO(3)$ of automorphisms inside it, and the length filtration is the determinantal filtration of a $4\times4$ array of the same size as the operator. It also buys the finite group of order $32$ of the signed basis products, a concrete object with which every computation of the category can be done by hand.

**What it does not buy: the Peirce frame.** The regular model carries no matrix units, because the algebra is a division algebra: there is no idempotent, hence no Peirce decomposition, hence no corners, and therefore no corner operators. In the split-quaternion category the Peirce frame was an operator tool: the corners indexed the strata and the four Peirce components gave four families of operators. That tool is absent here, and its absence is not a gap in the article but a property of the algebra.

**What it does not buy: chirality.** There is no left-right asymmetry of the algebra to display. Both the left and the right copies are copies of the whole algebra, they meet in the scalars, and neither is preferred; the division algebra has no minimal left ideal and no minimal right ideal, so no spinor and no chiral pair exists. The complex model does have a minimal left ideal, the first column of the model, but it is a module of real dimension two and not an ideal of the algebra.

**What the two missing structures have in common.** Both the Peirce frame and the chirality come from a system of matrix units, and a division algebra has none. So the two absences are one absence, and the category of the quaternions is the first in Part VI where the operator layer is a purely metric and tensor-theoretic object, with no combinatorial structure at all.

**What stays outside.** The complex structure, the Hermitian forms, the spectral projectors: those belong to the complex model and are read there. The regular frame is the frame of the real form, and it sees the real form only.

## Summary

1. The carrier and the ambient are the same as in the complex reading: $\mathbb{H}$ of dimension four and $M_4(\mathbb{R})$ of dimension sixteen. The two operators articles describe the same operators.
2. The left family is the image of the Cayley model itself; the right family is its signed transpose, $R_{\tilde q}=D\mathsf{M}_4(\tilde q)^{\mathsf T}D$; the two are mutual centralisers meeting in the scalars and spanning seven dimensions.
3. The sixteen products $T_{e_\mu,e_\nu}$ are signed permutation matrices, orthogonal, of determinant one and rank four; the thirty-two matrices $\pm T_{e_\mu,e_\nu}$ form a group of order $32$ inside $SO(4)$.
4. Only $T_{e_t,e_t}$ has a nonzero trace among the sixteen, which is the regular reading of $\operatorname{tr}T_{\tilde q,\tilde p}=4q_tp_t$.
5. A two-sided operator has rank four whenever both parameters are non-zero, determinant $N(\tilde q)^{2}N(\tilde p)^{2}$ and Frobenius norm squared $16N(\tilde q)N(\tilde p)$.
6. The Kronecker display does not transfer; in its place the operator carries two $4\times4$ arrays of the same size, the Cayley array and the coefficient array, related by one fixed linear map.
7. The cone is the Segre cone of dimension seven; the membership test is the rank-one condition on the coefficient array; the two rulings are the left and the right copies of the algebra.
8. The length is the coefficient rank, with strata of dimensions $0,7,12,15,16$; four products always suffice and generically are needed.
9. The operator rank and the length are two ranks of two arrays of one size, and neither determines the other; the four witnesses of the table settle it.
10. The Peirce frame and the chirality are both absent, and for one reason: a division algebra has no system of matrix units.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathsf{M}_4$ | the Cayley matrix of left multiplication | *$M_4(\mathbb{R})_{\mathbb{H}_L}$ Regular Representation* |
| $L_{\tilde q},R_{\tilde q}$ | the two one-sided families, $R_{\tilde q}=D\mathsf{M}_4(\tilde q)^{\mathsf T}D$ | this article |
| $D$ | the sign matrix $\operatorname{diag}(1,-1,-1,-1)$ | this article |
| $T_{\tilde q,\tilde p}$ | $L_{\tilde q}R_{\tilde p}$, the operator $\tilde x\mapsto\tilde q\tilde x\tilde p$ | this article |
| $c(M)$ | the coefficient array in the basis $T_{e_\mu,e_\nu}$ | this article |
| $\Phi$ | the fixed linear map taking $c(M)$ to the Cayley array of $M$ | this article |
| $\ell(M)$ | the length, equal to $\operatorname{rank}c(M)$ | this article |
| $Q_8$ | the quaternion group of the eight signed units | *Quaternion Algebra* |
| $SO(3)$ | the inner automorphisms, $\mathbb{H}^{\times}/\mathbb{R}^{\times}$ | *Quaternion Rotations and the Lorentz Group* |
| $\mathbb{P}^{3}(\mathbb{R})$ | the projectivised algebra, the base of each ruling | this article |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the double centraliser theorem, the regular representation and the tensor decomposition of the operator algebra.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the Cayley matrix, the signed transpose and the finite group of the signed units.
- Joseph Landsberg, *Tensors: Geometry and Applications* (American Mathematical Society, 2012), for the Segre variety, the tensor rank and the determinantal strata of a square array.
- Fuzhen Zhang, *Matrix Theory* (Springer, 2011), for the realification identities, the singular values of a realified complex matrix and the trace of a Kronecker product.
