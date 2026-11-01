# __$M_2(\mathbb{C})$ Defining Representation : Operators__

## Introduction

**The carrier is a module and not an algebra, and the whole article turns on that difference.** In the algebra categories a two-sided operator is a sandwich $X\mapsto QXP$, with both slots elements of the algebra. Here there is no product of two elements of the carrier: $V=\mathbb{C}^{2}$ is a module, a sum of two columns is not a column of a product, and the second slot must be a covector. The two-sided operator is therefore
$$
T_{u,\phi}(v)=\phi(v)\,u=u\phi^{\mathsf T},
$$
with $u\in V$ a column and $\phi\in V^{*}$ a row.

**The result in one line.** Every two-sided operator of the carrier is a rank-one matrix, that is a point of the determinantal cone $\{\det=0\}$ in $M_2(\mathbb{C})=\mathbb{C}^{4}$; the family is closed under composition, with the scalar absorbed; it has no identity, no inverses, no isometries and no nonzero skew-adjoint member; and its length equals its rank and is at most two. **The pair is a semigroup with zero and not a group, and the reason is arithmetic: the identity has rank two and the cone has rank one.**

**Why the pair is still worth having.** Three things are gained. The parametrisation by $V\times V^{*}$ modulo scaling, which turns every statement about the cone into a statement about a point of $\mathbb{P}^{1}\times\mathbb{P}^{1}$. The single quadratic criterion $\det M=0$, which at this size is the whole of the rank condition. And the length formula, which makes the rank of a matrix the number of elementary products it needs. **What is lost is exactly the algebra: the identity, the inverses and the isometry group.**

**Two cones and not one.** The space $M_2(\mathbb{C})$ carries two rank-one families, the bilinear one $u\phi^{\mathsf T}$ and the Hermitian one $uu^{\dagger}$, and both belong to this pair. The first is the Segre quadric and the second is the light cone, its projectivisation is one projective line and not a product, and the collapse is the quotient by the phase. **This is the only pair of the corpus where the two cones must be compared side by side**, because it is the only one where both are cones of operators on a module rather than of elements of an algebra.

**Boundaries.** The space, the three forms and the two cones as point sets are *$M_2(\mathbb{C})$ Defining Representation*; the operators of the biquaternion algebra, with the sandwich $X\mapsto QXP$, its cone, its length $1,4,7,16$ and its gauge, are *$M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation : Operators*; the general rank criterion and the determinantal variety at the size four are *$M_4(\mathbb{C})$ Standard Peirce Representation* and its operators companion; the endomorphism algebra, $\mathrm{GL}_2(\mathbb{C})$ and $\mathrm{PGL}_2(\mathbb{C})$ are *The Endomorphisms of $\mathbb{C}^2$*; the lattice and the incidence are *The Subspaces of $\mathbb{C}^2$*. The general theory of operators on a module, with the two-sided operators and the tensor form of the linear map, is *Modules*, and the vectorisation and the coefficient array are *The Sylvester Operator and the Kronecker Sum of $M_4(\mathbb{C})$*.

**Conventions.** The carrier is $V=\mathbb{C}^{2}$ with the basis $e_1,e_2$, the dual is $V^{*}$ with the dual basis, $\phi(u)=\phi^{\mathsf T}u$ is the pairing with no conjugation, $E_{jk}=e_je_k^{\mathsf T}$ are the matrix units, $M^{\mathsf T}$ and $M^{\dagger}$ are the transpose and the conjugate transpose, and $J_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$. The operator is written $T_{u,\phi}=u\phi^{\mathsf T}$ with the column on the left and the row on the right, and $\mathcal{C}$ is the set of all of them, the **bilinear cone**, with $\mathcal{C}_{H}$ the **Hermitian cone** of the matrices $uu^{\dagger}$.

## The One-Sided Operators

**The left side of the carrier is a full matrix algebra and the right side is a dual space, and the two sides are of different kinds.**

### The Left Multiplication

**Definition.** For $A\in M_2(\mathbb{C})$ the **left multiplication** is the operator
$$
L_A:V\longrightarrow V,\qquad L_A(v)=Av .
$$

**Proposition (the left operators are all the $\mathbb{C}$-linear operators).** The map $A\mapsto L_A$ is an isomorphism of algebras $M_2(\mathbb{C})\to\operatorname{End}_{\mathbb{C}}(V)$, and it is faithful; the left operators form a space of complex dimension four and real dimension eight.

*Proof.* The map is linear, multiplicative because $L_A L_B=L_{AB}$, and injective because $L_A$ determines the columns of $A$ as the images of the basis; both spaces have complex dimension four.

**The left side is therefore the whole algebra.** In the algebra categories the left multiplication acts on an algebra and its image is a proper subspace; here it acts on the module, which is smaller than the algebra, and the image is everything that can happen. **The left operator is nothing but the matrix, and no information is lost in writing it.**

### The Right Slot

**Definition.** The **right slot** of a two-sided operator is its second parameter, and it is an element of the dual,
$$
\phi:V\longrightarrow\mathbb{C},\qquad v\longmapsto\phi(v)=\phi^{\mathsf T}v .
$$
The operator built from a functional is $T_{u_0,\phi}=u_0\phi^{\mathsf T}$, for a column $u_0$.

**Proposition (there is no right multiplication by an element of the carrier).** For $u\in V$ there is no linear map $v\mapsto vu$.

*Proof.* A product $vu$ would require an algebra structure on $V$, and the carrier has none: $V$ is a module and its only product is the action $Av$ of an endomorphism on a column. What the carrier has instead is the pairing with the dual, which is the functional $\phi$.

**The asymmetry is the whole first section.** The left side is a space of dimension four over $\mathbb{C}$ and the right side is a space of dimension two, that is four over $\mathbb{R}$; **the two sides are of different complex dimensions and they are not interchangeable.** The general theory of a two-sided operator on a module takes its second slot in the dual for exactly this reason (*Modules*).

### The Adjoints of the Two Sides

**Definition.** With the complex bilinear form $\langle X,Y\rangle=\operatorname{Tr}(X^{\mathsf T}Y)$ on the operator space, the **transpose adjoint** of $L_A$ is $L_{A^{\mathsf T}}$; with the Hermitian form $\langle X,Y\rangle_{H}=\operatorname{Tr}(X^{\dagger}Y)$ the **Hermitian adjoint** is $L_{A^{\dagger}}$.

**Proposition (the two adjoints of the left operator).** For every $A$ and every $u,v$,
$$
\langle L_Au,v\rangle_{\text{bil}}=u^{\mathsf T}A^{\mathsf T}v=\langle u,L_{A^{\mathsf T}}v\rangle_{\text{bil}},\qquad
H(L_Au,v)=H(u,A^{\dagger}v).
$$

*Proof.* The first is the associativity of the transposition, $u^{\mathsf T}Av=(A^{\mathsf T}u)^{\mathsf T}v$, read in the other order; the second is the definition of the adjoint of a matrix for the Hermitian form, $H(Au,v)=u^{\mathsf T}\overline{Av}=u^{\mathsf T}\bar A\bar v=H(u,A^{\dagger}v)$.

**The transpose adjoint of the right slot is the left slot.** A row $\phi$ is the transpose of a column, so the two sides are exchanged by the transpose and are **not** exchanged by the dagger, which sends a row to a column of the conjugate space. **The transposition swaps the two sides of the theory and the conjugation does not**, which is why the transpose fixed locus is the symmetric cone and the dagger fixed locus the Hermitian one, as §*The Adjoints and the Types* shows.

## The Two-Sided Operator

**Definition.** The **two-sided operator** of the pair $(u,\phi)$ is
$$
T_{u,\phi}=u\phi^{\mathsf T},\qquad T_{u,\phi}(v)=\phi(v)\,u .
$$

**Proposition (the elementary properties).** For all $u,u'\in V$, $\phi,\phi'\in V^{*}$ and $\lambda\in\mathbb{C}$:
$$
T_{u,\phi}+T_{u',\phi}=T_{u+u',\phi},\qquad
T_{u,\phi}+T_{u,\phi'}=T_{u,\phi+\phi'},\qquad
T_{\lambda u,\phi}=T_{u,\lambda\phi}=\lambda\,T_{u,\phi},
$$
and $T_{u,\phi}=0$ if and only if $u=0$ or $\phi=0$.

*Proof.* The three identities are the distributivity of the matrix product over the sum of rank-one factors. The last is the statement that a product of a nonzero column and a nonzero row is nonzero, entrywise.

**Proposition (the fibre is exactly the scaling orbit).** If $T_{u,\phi}=T_{u',\phi'}\neq0$ then $u'=\lambda u$ and $\phi'=\lambda^{-1}\phi$ for a unique $\lambda\in\mathbb{C}^{\times}$; the fibres of the parametrisation are therefore the orbits
$$
(u,\phi)\longmapsto(\lambda u,\lambda^{-1}\phi),
$$
and the parametrisation is injective in each slot once the other is fixed.

*Proof.* Both matrices have the same image, which is the line $\mathbb{C}u=\mathbb{C}u'$, so $u'=\lambda u$; then $u\phi^{\mathsf T}=u\lambda\phi'^{\mathsf T}$ and the rows are equal because $u\neq0$ and the map $\phi\mapsto u\phi^{\mathsf T}$ is injective.

**The dimension count.** The parameter space has complex dimension four. The fibre has complex dimension one. The image has complex dimension three and real dimension six, inside an ambient of complex dimension four and real dimension eight. **The deficit of one complex dimension is the scaling and nothing else**, which is the sharpest difference from the algebra categories, where the cone is cut out twice: once by the scaling and once by the failure of the parameter to reach the whole ambient.

**The cone is not a subspace.** The identity is not a member, $I_2\notin\mathcal{C}$, and it is the sum of the two members $E_{11}$ and $E_{22}$. **The additive failure of the family is the identity itself**, and this is the smallest possible witness: two rank-one terms of rank sum two.

## The Cone and the Coefficient Matrix

**Definition.** Fix the **operator basis** $E_{11},E_{12},E_{21},E_{22}$ of $M_2(\mathbb{C})$ and write $M=\sum_{j,k}w_{jk}E_{jk}$. The **coefficient array** of $M$ is the matrix $c(M)$ of its four coefficients, and in this basis it is the matrix itself.

**Proposition (the criterion, in the rank form and then in the determinant form).** For $M\in M_2(\mathbb{C})$ the following are equivalent: $M\in\mathcal{C}$; $\operatorname{rank}M\le1$; $c(M)$ has rank at most one; $\det M=0$.

*Proof.* The first two are equivalent by the definition and the rank-one factorisation of matrices of rank at most one. The coefficient array is the matrix, so the third is the second. The determinant vanishes exactly when the two columns are dependent, which is the second; **and the determinant form is available only because the carrier is two-dimensional**, the general criterion being the rank inequality (*$M_4(\mathbb{C})$ Standard Peirce Representation*).

**The projective picture.** The cone is the determinantal quadric of $\mathbb{P}^{3}$,
$$
\{[M]:\det M=0\}=\mathbb{P}^{1}\times\mathbb{P}^{1}\subset\mathbb{P}^{3},
$$
of complex dimension three, ruled in the two families of §*The Bilinear Cone and the Segre Quadric* of *$M_2(\mathbb{C})$ Defining Representation*. **It is a quadric of rank four and not a cone over a plane**: its two rulings are the images of the two factors.

**The cone is homogeneous.** Every statement above is invariant under $\lambda\mapsto\lambda M$, so $\lambda\mathcal{C}=\mathcal{C}$ and the projectivisation carries the whole content. **There is no affine statement about the family that is not a statement about its projectivisation together with the origin.**

## The Hermitian Cone and the Light Cone

**A second rank-one family lives in the same space, it is the fixed locus of the dagger, and its projectivisation is a single projective line.**

### The Second Family

**Definition.** The **Hermitian cone** is $\mathcal{C}_{H}=\{uu^{\dagger}:u\in V\}$, the set of positive semidefinite matrices of rank at most one.

**Proposition (the Hermitian members of the cone).** A member of $\mathcal{C}$ is Hermitian exactly when it is a real multiple of a member of $\mathcal{C}_{H}$, that is when $\phi=c\,\bar u$ with $c$ real. In particular $\mathcal{C}_{H}\subset\mathcal{C}$, and the Hermitian members of the cone are the real line through the Hermitian cone.

*Proof.* The computation is the one of *$M_2(\mathbb{C})$ Defining Representation*, §*The Hermitian Cone and the Light Cone*: the equality $u\phi^{\mathsf T}=\bar\phi u^{\mathsf T}$ forces $\phi=c\bar u$ with $c$ real and the matrix $c\,uu^{\dagger}$.

**The dagger is the only operation that carries one family to the other.** It is conjugate-linear, it sends $u\phi^{\mathsf T}$ to $\bar\phi u^{\mathsf T}$, and the fixed points are exactly the Hermitian family up to real scale. **The conjugate-linear half of the operator theory is therefore not an ornament: it is where the second cone comes from.**

### The Two Cones Side by Side

| | bilinear cone $\mathcal{C}$ | Hermitian cone $\mathcal{C}_{H}$ |
|---|---|---|
| definition | $u\phi^{\mathsf T}$ | $uu^{\dagger}$ |
| ambient | $M_2(\mathbb{C})$, real dimension $8$ | the Hermitian subspace, real dimension $4$ |
| equation | $\det M=0$ | $\det M=0$ on the Hermitian subspace |
| real dimension | $6$ | $3$ |
| parameters modulo the fibre | $([u],[\phi])\in\mathbb{P}^{1}\times\mathbb{P}^{1}$ | $[u]\in\mathbb{P}^{1}$ |
| fibres of the parametrisation | $\mathbb{C}^{\times}$, real dimension $2$ | $S^{1}$, real dimension $1$ |
| rulings | two, independent | one |
| fixed by the dagger | no | yes |
| trace | $\phi(u)$, any complex value | $\lVert u\rVert^{2}\ge0$ |
| trace-free members | $\phi(u)=0$, a hyperplane section | $u=0$ only |

**The two lines of the table that carry the reading.** The fibres: the bilinear cone quotients by a complex scaling and the Hermitian cone by a phase, so the second quotient is a circle and the first is a complex line with the origin removed. The trace: a member of the bilinear cone can have any complex trace, and a member of the Hermitian cone has a nonnegative one. **The positivity of the trace is the signature of the definite form, and it is the whole difference between a cone of operators and a cone of states.**

### The Light Cone

**Theorem (the Hermitian cone is the light cone).** The Pauli coordinates of $M\in\mathcal{C}_{H}$ satisfy
$$
t^{2}-x^{2}-y^{2}-z^{2}=0,\qquad t=\tfrac12\operatorname{tr}M\ge0,
$$
and the map is onto the closed future cone.

*Proof.* The determinant identity $\det M=t^{2}-\lvert\vec x\rvert^{2}$ on the Hermitian subspace and the vanishing of the determinant on $\mathcal{C}_{H}$ give the equation; the trace is $\lVert u\rVert^{2}=2t\ge0$; and every point of the cone is attained by a column of norm $\sqrt{2t}$ in the corresponding direction. The computation is in *$M_2(\mathbb{C})$ Defining Representation*, §*The Pauli Coordinates*.

**Three involutions act on the one cone, and the three fixed loci are three families.** The transposition $T\mapsto T^{\mathsf T}$ fixes the symmetric rank-one matrices, the conjugation $T\mapsto\bar T$ fixes the real ones and exchanges the two rulings, and the dagger $T\mapsto T^{\dagger}$ fixes the Hermitian ones. **The cone is closed under all three, and the three fixed loci are of three different sizes**: complex dimension two for the symmetric family, four for the real one and three for the Hermitian one.

## The Composition

**The family is closed under composition, the scalar is absorbed, and the trace records the absorption.**

**Proposition (the composition rule).** For all pairs,
$$
T_{u,\phi}\,T_{u',\phi'}=\phi(u')\,T_{u,\phi'} .
$$

*Proof.* $u\phi^{\mathsf T}u'\phi'^{\mathsf T}=u(\phi^{\mathsf T}u')\phi'^{\mathsf T}$ and $\phi^{\mathsf T}u'=\phi(u')$ is a scalar.

**Corollary (the powers).** For $n\ge1$,
$$
\bigl(T_{u,\phi}\bigr)^{n}=\phi(u)^{\,n-1}\,T_{u,\phi} .
$$

*Proof.* Induction on the rule, the scalar being $\phi(u)$ at every step.

**Proposition (the three types of member).** For $T=T_{u,\phi}\neq0$,
$$
T^{2}=0\iff\phi(u)=0,\qquad T^{2}=T\iff\phi(u)=1,
$$
and $T$ is invertible for no pair $(u,\phi)$.

*Proof.* The two equivalences are the corollary at $n=2$. Invertibility would require the rank to be two, since the inverse of a matrix has the rank of the matrix, and the rank is one.

**The trace and the spectrum.** The eigenvalues are $\phi(u)$ and $0$, so $\operatorname{tr}T=\phi(u)$ and $\det T=0$; the trace is the scalar that appears in the composition rule, and the Cayley–Hamilton identity degenerates to $T^{2}=\phi(u)T$. **The whole spectral theory of the pair is the single number $\phi(u)$**, and the two cases of the corollary are its two values.

**The semigroup.** The product is associative by the associativity of the matrix product. There is a zero, $T_{0,\phi}=0$, and there is no identity, because $I_2$ has rank two and every member has rank at most one. The family is thus a **semigroup with zero and without identity**, and the multiplicative structure is the one of $\mathbb{P}^{1}\times\mathbb{P}^{1}$ with the pairing as the structure scalar.

**Remark (the comparison with the algebra family).** The family of the biquaternion algebra contains $T_{e_t,e_t}$, the identity, and it contains inverses whenever both parameters are units (*$M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation : Operators*). **The module family contains neither**, and the reason is not the choice of parametrisation but the rank: a rank-one operator can never be the identity of a two-dimensional space.

## The Length

**Definition.** The **length** of $M\in M_2(\mathbb{C})$ is
$$
\ell(M)=\min\Bigl\{r:M=\sum_{i=1}^{r}T_{u_i,\phi_i}\Bigr\},
$$
the least number of rank-one terms whose sum is $M$.

**Theorem (the length is the rank).** For every $M\in M_2(\mathbb{C})$,
$$
\ell(M)=\operatorname{rank}M,\qquad \ell(M)\in\{0,1,2\}.
$$

*Proof.* A sum of $r$ rank-one matrices has rank at most $r$, so $\ell(M)\ge\operatorname{rank}M$. Conversely, writing $c_j$ for the $j$-th column of $M$ and $r_j^{\mathsf T}$ for its $j$-th row,
$$
M=\sum_{j=1}^{2}c_j\,r_j^{\mathsf T},
$$
a sum of at most two rank-one terms, the terms with a zero column being dropped; so $\ell(M)$ is at most two and equals the rank. The identity is $E_{11}+E_{22}$ and has rank two.

**The extremal cases.** The zero matrix has length zero, the cone is the set of length one, and the complement of the cone is the set of length two. **The length does not see the size of the entries**: a matrix of length two is a matrix of length two however small its determinant.

**Proposition (the elementary inequalities).** For all $M,N$ and $\lambda\neq0$,
$$
\ell(M+N)\le\ell(M)+\ell(N),\qquad \ell(\lambda M)=\ell(M),\qquad \ell(MN)\le\min\{\ell(M),\ell(N)\}.
$$

*Proof.* The first is the concatenation of two decompositions; the second is the homogeneity of the cone; the third is the rank inequality $\operatorname{rank}(MN)\le\min\{\operatorname{rank}M,\operatorname{rank}N\}$.

**The length of the product is not the sum.** In the algebra categories the composed operator can need as many terms as the sum of the two lengths, because the two slots carry independent parameters. Here the composition is a single rank-one product and the length of a product is at most one. **The ladder of the biquaternion pair, $1,4,7,16$, collapses to $0,1,2$**, and the collapse is the collapse of the carrier from an algebra to a module.

## The Two Ranks

**Definition.** For $M\in M_2(\mathbb{C})$ let $\operatorname{rank}T_M$ be the rank of $M$ as an operator on $V$ and $\operatorname{rank}c(M)$ the rank of its coefficient array in the operator basis.

**Proposition (the two ranks coincide identically).** In the matrix-unit basis,
$$
\operatorname{rank}T_M=\operatorname{rank}c(M)=\operatorname{rank}M ,
$$
for every $M$.

*Proof.* The coefficient array is the matrix, so the two ranks are the same number computed twice.

**Why this is a statement and not a tautology.** In the algebra categories the operator space is not the algebra: the two-sided operator $T_{Q,P}$ acts on the algebra, of dimension sixteen in the reduced biquaternion case, and its coefficient array is taken in a basis $T_{\mu\nu}$ which is not the matrix-unit basis of the source. There the rank of the operator and the rank of the coefficient array separate, and the criterion $\operatorname{rank}c(M)\le1$ is stronger than the rank-one condition. **Here the operator space and the ambient are the same space, the basis is the matrix-unit basis, and the two ranks are one number**: which is why the criterion of §*The Cone and the Coefficient Matrix* can be stated as $\det M=0$ and still be exact.

**The table of the comparison.**

| | this pair | the algebra pair |
|---|---|---|
| ambient of the operator | $M_2(\mathbb{C})$, complex dimension $4$ | $\operatorname{End}(\mathbb{B})$, complex dimension $16$ |
| operator basis | $E_{jk}$ | $T_{\mu\nu}$ |
| coefficient array | the matrix | a $16\times16$ array |
| two ranks | equal | independent |
| criterion | $\operatorname{rank}M\le1$ | $\operatorname{rank}c(M)\le1$ |
| length | $0,1,2$ | $1,4,7,16$ |

## The Adjoints and the Types

**Two adjoints act on the pair, the transpose and the dagger, and each has a family of fixed points that is a rank-one family.**

### The Transpose Adjoint

**Definition.** With the complex bilinear form $\langle X,Y\rangle=\operatorname{Tr}(X^{\mathsf T}Y)$ on $M_2(\mathbb{C})$, the **transpose adjoint** of $T$ is the unique $T^{\mathsf T}$ with $\langle TX,Y\rangle=\langle X,T^{\mathsf T}Y\rangle$.

**Proposition (the transpose swaps the slots).** For every pair,
$$
\bigl(T_{u,\phi}\bigr)^{\mathsf T}=T_{\phi,u},
$$
that is $\phi u^{\mathsf T}$ in coordinates.

*Proof.* $(u\phi^{\mathsf T})^{\mathsf T}=\phi u^{\mathsf T}$, the column becoming a row and the row a column.

**The families of the transposition.**

| Family | Condition | Description |
|---|---|---|
| self-adjoint | $\phi=c\,u$ | the symmetric rank-one matrices $c\,uu^{\mathsf T}$ |
| skew-adjoint | $\phi=-c\,u$ with $c\neq0$ | empty: $c\,uu^{\mathsf T}=-c\,uu^{\mathsf T}$ forces $c=0$ |
| general | none | the cone |

**Proposition (no nonzero member of the cone is skew-adjoint).** If $T\in\mathcal{C}$ and $T^{\mathsf T}=-T$ then $T=0$.

*Proof.* A skew-symmetric matrix of size two is $\lambda J_2=\lambda\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, whose rank is two for $\lambda\neq0$ and which is therefore not in the cone; and $\lambda=0$ is the zero matrix.

**The self-adjoint cone is the symmetric rank-one family.** It is the set of matrices $c\,uu^{\mathsf T}$, of complex dimension two, and it is the **complex** analogue of the Hermitian cone: **the same construction with the transpose in place of the dagger, and the two families are as different as a complex line is from a circle.**

### The Hermitian Adjoint

**Definition.** With $\langle X,Y\rangle_{H}=\operatorname{Tr}(X^{\dagger}Y)$, the **Hermitian adjoint** of $T_{u,\phi}$ is
$$
\bigl(T_{u,\phi}\bigr)^{\dagger}=T_{\bar\phi,u}=\bar\phi\,u^{\mathsf T}.
$$

**Proposition (the fixed points of the dagger).** $T^{\dagger}=T$ for a nonzero $T\in\mathcal{C}$ exactly when $T$ is a real multiple of a member of $\mathcal{C}_{H}$.

*Proof.* The computation of §*The Hermitian Cone and the Light Cone*: the equality forces $\phi=c\bar u$ with $c$ real, and the matrix is $c\,uu^{\dagger}$.

**The three involutions and their fixed loci.**

| Involution | Action on $T_{u,\phi}$ | Fixed locus |
|---|---|---|
| transposition | $T_{\phi,u}$ | the symmetric cone $c\,uu^{\mathsf T}$ |
| conjugation | $T_{\bar u,\bar\phi}$ | the real cone |
| dagger | $T_{\bar\phi,u}$ | the Hermitian cone $\mathcal{C}_{H}$ |

**The anti-Hermitian members are in the cone and not in the Hermitian cone.** The matrix $i\,uu^{\dagger}$ is anti-Hermitian, it is a member of $\mathcal{C}$ since $i\,uu^{\dagger}=T_{u,i\bar u}$, and it is not in $\mathcal{C}_{H}$ because its trace is imaginary. **The cone is closed under multiplication by any complex scalar and the Hermitian cone is closed only under the real ones**, so the first is a complex object and the second a real one, and the anti-Hermitian members are what the complex scaling adds.

### The Isometries

**Proposition (there is no nonzero isometry).** For every nonzero $T\in\mathcal{C}$ the two products $T^{\dagger}T$ and $T^{\mathsf T}T$ have rank at most one, so neither equals $I_2$.

*Proof.* With $\sigma=u^{\mathsf T}u=\sum_ju_j^{2}$, a scalar that may vanish,
$$
T^{\dagger}T=\bar\phi\,u^{\mathsf T}u\,\phi^{\mathsf T}=\sigma\,\bar\phi\bar\phi^{\dagger},
$$
a matrix of rank at most one, and the identity has rank two. The same computation with the transpose gives $T^{\mathsf T}T=\sigma\,\phi\phi^{\mathsf T}$.

**The family therefore contains no isometry, no orthogonal member and no unitary member.** In the algebra categories the units of the algebra give isometries of the operator space, and the length ladder starts at one because the identity is a product; here the identity is not a product at all, and the isometry group of the family is empty.

## The Carrier with an Algebra Structure

**Two products can be put on the carrier, and both destroy the cone: the pointwise product gives a subspace and the dual-number product gives a dense subset of a hyperplane.**

### The Pointwise Product

**Definition.** The **pointwise product** on $\mathbb{C}^{2}$ is $(a,b)(c,d)=(ac,bd)$, which makes the carrier the algebra $\mathbb{C}\times\mathbb{C}$.

**Proposition (the pointwise product gives the diagonal).** For $u=(a,b)$ and $v=(c,d)$ acting on $w=(y,z)$,
$$
T_{u,v}=\begin{pmatrix}ac&0\\0&bd\end{pmatrix},
$$
and the image of the product is the whole two-dimensional subspace of diagonal matrices.

*Proof.* The action is $y\mapsto acy$ and $z\mapsto bdz$, so the matrix is diagonal; conversely the diagonal matrix $\operatorname{diag}(r,s)$ is $T_{u,v}$ with $u=(r,s)$ and $v=(1,1)$.

### The Dual-Number Product

**Definition.** The **dual-number product** is $(a,b)(c,d)=(ac,ad+bc)$, with $\epsilon^{2}=0$.

**Proposition (the image is dense in a hyperplane and is not the hyperplane).** The operator of the product is
$$
T=\begin{pmatrix}ac&ad\\ bc&ad+bc\end{pmatrix},
$$
so its coefficients satisfy the linear relation
$$
w_{22}=w_{12}+w_{21},
$$
and the image is a three-dimensional subset of that hyperplane of $M_2(\mathbb{C})$. It is not the hyperplane: a matrix with $w_{11}=0$ and $w_{12}w_{21}\neq0$ is never attained, because $w_{11}=ac=0$ forces $a=0$, hence $w_{12}=ad=0$, or $c=0$, hence $w_{21}=bc=0$.

*Proof.* The relation is read off the four entries. The exclusion is the computation just given. The image is dense in the hyperplane because for $w_{11}=ac\neq0$ the entries $w_{12}$ and $w_{21}$ are free, $d=w_{12}/a$ and $b=w_{21}/c$.

### Why the Module Reading Is the One to Take

| Structure on $\mathbb{C}^{2}$ | Operator family | Dimension | Contains the cone? |
|---|---|---|---|
| none, the module | $u\phi^{\mathsf T}$ | complex $3$ | is the cone |
| $\mathbb{C}\times\mathbb{C}$ | $\operatorname{diag}(ac,bd)$ | complex $2$ | no, only the diagonal |
| the dual numbers | the hyperplane $w_{22}=w_{12}+w_{21}$ minus a set | complex $3$ | no, and not even closed |

**In both algebra readings the family is a subspace, or almost one, and the Segre structure is lost.** A subspace has no rulings, no cone and no length; a family dense in a hyperplane has a closure that is a subspace. **The module reading is the only one that preserves the cone, and this is the reason the pair takes it**, even at the price of the identity, the inverses and the isometries.

## What the Pair Buys and Does Not

**What it buys.**

- The **parametrisation** of the cone by $V\times V^{*}$ modulo the scaling, hence by $\mathbb{P}^{1}\times\mathbb{P}^{1}$, which turns every rank-one matrix into a pair of lines and every statement about the cone into a statement about the two rulings.
- The **single criterion** $\det M=0$, exact at this size and reducible to the rank inequality in general.
- The **composition rule** $T_{u,\phi}T_{u',\phi'}=\phi(u')T_{u,\phi'}$, whose scalar is the trace, and with it the whole spectral theory of the family in one number.
- The **length formula** $\ell=\operatorname{rank}$, the values $0,1,2$ and the identity at length two.
- The **two cones** and the dagger that relates them, which is the only place in the corpus where the bilinear and the Hermitian rank-one families are compared on the same carrier.
- The **two adjoints**, with the self-adjoint family, the empty skew-adjoint family and the Hermitian fixed locus.

**What it does not buy.**

- **The identity.** $I_2$ has rank two and is not a member; the family is a semigroup with zero and not a monoid.
- **The inverses.** No member is invertible; the group of units is empty.
- **The isometries.** No nonzero member satisfies $T^{*}T=I_2$, so there is no orthogonal or unitary sector.
- **The reach beyond the cone.** Every member is of rank at most one; a matrix of rank two needs a sum of two members, and the sum is not a member.
- **The mixing of the two rulings.** The two rulings are independent, but the composition contracts them to a single pair, and there is no product that mixes the two families.

**The comparison table.**

| | this pair | the biquaternion $M_2(\mathbb{C})$ pair |
|---|---|---|
| carrier | the module $V$, complex dimension $2$ | the algebra $\mathbb{B}$, complex dimension $4$ |
| two-sided operator | $u\phi^{\mathsf T}$, one column and one row | $QXP$, two algebra elements |
| parameter space | $V\times V^{*}$, complex dimension $4$ | $\mathbb{B}\times\mathbb{B}$, complex dimension $8$ |
| fibre | $\mathbb{C}^{\times}$, complex dimension $1$ | the scalars, complex dimension $1$ |
| reach | complex dimension $3$ | complex dimension $7$ |
| identity in the family | no | yes, $T_{e_t,e_t}$ |
| inverses in the family | no | yes, for pairs of units |
| isometries | none | a family, of dimension seven |
| length | $0,1,2$ | $1,4,7,16$ |
| rank constraint | rank $\le1$ | rank $\le4$, by the division algebra |
| the second cone | the Hermitian cone, distinct | no second cone of the same kind |

**The single sentence.** The pair is the cleanest operator theory of the corpus because the cone is thin and the composition is a scalar; it is also the poorest, because a rank-one family has no group of units, and **everything that the algebra pairs gain they gain by the identity being a product.**

## Summary

The carrier is the module $V=\mathbb{C}^{2}$, and there is no product on it, so the two-sided operator of the pair is $T_{u,\phi}(v)=\phi(v)u=u\phi^{\mathsf T}$, a rank-one matrix with a column and a row. The left side is the whole algebra $M_2(\mathbb{C})$ acting faithfully, of complex dimension four, and the right side is the dual $V^{*}$, of complex dimension two; the transpose adjoint of the right slot is the left slot and the Hermitian adjoint is not. The parametrisation by $V\times V^{*}$ has fibres the scaling orbits $\mathbb{C}^{\times}$ and image the determinantal cone of $\mathbb{P}^{3}$, that is the Segre quadric $\mathbb{P}^{1}\times\mathbb{P}^{1}$, of complex dimension three and real dimension six inside an ambient of real dimension eight; the coefficient array in the matrix-unit basis is the matrix itself, so the rank criterion and the determinant criterion are the same condition, and the cone spans the ambient although the identity is not a member.

The composition is $T_{u,\phi}T_{u',\phi'}=\phi(u')T_{u,\phi'}$, with powers $\phi(u)^{n-1}T_{u,\phi}$; the member is nilpotent exactly when $\phi(u)=0$ and idempotent exactly when $\phi(u)=1$; the trace is $\phi(u)$, the determinant is zero, and the Cayley–Hamilton identity is $T^{2}=\phi(u)T$. The family is a semigroup with zero and without identity, and no member is invertible. The length is the rank, with the values $0,1,2$: zero for the zero matrix, one on the cone, two on the complement, and two for the identity. The two ranks, of the operator and of its coefficient array, coincide identically here, in contrast with the algebra pairs, where the operator basis is $T_{\mu\nu}$ and the two separate.

Two rank-one families live in the ambient: the bilinear cone, of real dimension six, with two rulings and fibres $\mathbb{C}^{\times}$, and the Hermitian cone $uu^{\dagger}$, of real dimension three, with one ruling, fibres $S^{1}$, and the future light cone $t^{2}-\lvert\vec x\rvert^{2}=0$, $t\ge0$ in the Pauli coordinates; the second is the fixed locus of the dagger in the first, up to real scale. The transpose adjoint swaps the slots and its fixed locus is the symmetric cone $c\,uu^{\mathsf T}$; the dagger's fixed locus is the Hermitian cone; no nonzero member of the cone is skew-adjoint, and no nonzero member is an isometry. Putting an algebra structure on the carrier destroys the cone: the pointwise product gives the diagonal subspace and the dual-number product gives a set dense in the hyperplane $w_{22}=w_{12}+w_{21}$ and missing the matrices with $w_{11}=0$ and $w_{12}w_{21}\neq0$. **The pair buys the parametrisation, the single criterion, the composition rule, the length and the comparison of the two cones, and it pays with the identity, the inverses, the isometries and the ladder $1,4,7,16$.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V=\mathbb{C}^{2}$ | the carrier, the defining module |
| $V^{*}$, $\phi,\psi$ | the dual and its elements, the rows |
| $\phi(u)=\phi^{\mathsf T}u$ | the pairing, with no conjugation |
| $L_A$ | the left multiplication $v\mapsto Av$ |
| $E_{jk}$ | the matrix units |
| $T_{u,\phi}=u\phi^{\mathsf T}$ | the two-sided operator of the pair $(u,\phi)$ |
| $\mathcal{C}$ | the bilinear cone, the set of all $T_{u,\phi}$ |
| $\mathcal{C}_{H}$ | the Hermitian cone, the set of all $uu^{\dagger}$ |
| $M^{\mathsf T}$, $M^{\dagger}$ | the transpose and the conjugate transpose |
| $\langle X,Y\rangle$, $\langle X,Y\rangle_{H}$ | the bilinear and the Hermitian forms on the operator space |
| $c(M)$ | the coefficient array of $M$ in the matrix-unit basis |
| $\ell(M)$ | the length, the least number of rank-one terms |
| $J_2$ | the alternating matrix $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ |
| $w_{jk}$ | the coefficients of $M$ in the basis $E_{jk}$ |
| $t,x,y,z$ | the Pauli coordinates of a Hermitian matrix |
| $\mathbb{P}^{1}\times\mathbb{P}^{1}$ | the projectivised cone, the Segre quadric |

## Further Reading

*$M_2(\mathbb{C})$ Defining Representation* is the first article of the pair: the space, the three forms, the lines, the flags, the two cones as point sets, the spinor and the qubit. *$M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation* and its operators companion are the algebra pair on the same algebra: the frame, the Peirce decomposition, the trace, the determinant, the sandwich $X\mapsto QXP$, the cone of the algebra, the length ladder $1,4,7,16$ and the gauge, and they are what this article is measured against. *The Endomorphisms of $\mathbb{C}^2$* carries the algebra $M_2(\mathbb{C})$, the conjugate-linear maps, $\mathrm{GL}_2(\mathbb{C})$, $\mathrm{PGL}_2(\mathbb{C})$ and the centraliser of $J$. *The Subspaces of $\mathbb{C}^2$* carries the lattice, the flag and the incidence.

On the general theory, *Modules* fixes the two-sided operator on a module and its second slot in the dual, *The Sylvester Operator and the Kronecker Sum of $M_4(\mathbb{C})$* carries the vectorisation and the coefficient array, *The Determinant and Alternating Forms* carries the determinant as a form, and *$M_4(\mathbb{C})$ Standard Peirce Representation* with its operators companion carries the rank criterion and the determinantal variety at the general size, of which the determinant criterion here is the two-dimensional case. *The Forms, the Norms and the Singular Set of $M_4(\mathbb{C})$* develops the stratified picture of the singular set, and *Direct Sums, Free Modules and Rank* the notion of rank that the length computes.
