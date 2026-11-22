# __$M_2(\mathbb{C})$ Defining Representation : Operators__

## Introduction

**The carrier is a module and not an algebra, and the whole article turns on that difference.** In the algebra categories a two-sided operator is a map $X\mapsto QXP$, with both slots elements of the algebra. Here there is no product of two elements of the carrier: $V=\mathbb{C}^{2}$ is a module, a sum of two columns is not a column of a product, and the second slot must be a covector. The two-sided operator is therefore
$$
L_{u}R_{\phi}(v)=\phi(v)\,u=u\phi^{\mathsf T},
$$
with $u\in V$ a column and $\phi\in V^{*}$ a row.

**The result in one line.** Every two-sided operator of the carrier is a rank-one matrix, that is a point of the determinantal cone $\{\det=0\}$ in $M_2(\mathbb{C})=\mathbb{C}^{4}$; the family is closed under composition, with the scalar absorbed; it has no identity, no inverses, no isometries and no nonzero anti-self-adjoint member; and its length equals its rank and is at most two. **The pair is a semigroup with zero and not a group, and the reason is arithmetic: the identity has rank two and the cone has rank one.**

**Why the module reading is still worth having.** Three things are gained. The parametrisation by $V\times V^{*}$ modulo scaling, which turns every statement about the cone into a statement about a point of $\mathbb{P}^{1}\times\mathbb{P}^{1}$. The single quadratic criterion $\det M=0$, which at this size is the whole of the rank condition. And the length formula, which makes the rank of a matrix the number of elementary products it needs. **What is lost is exactly the algebra: the identity, the inverses and the isometry group.**

**Two cones and not one.** The space $M_2(\mathbb{C})$ carries two rank-one families, the bilinear one $u\phi^{\mathsf T}$ and the Hermitian one $uu^{\dagger}$, and both belong to this module. The first is the Segre quadric and the second is the light cone, its projectivisation is one projective line and not a product, and the collapse is the quotient by the phase. **This is the only pair of the corpus where the two cones must be compared side by side**, because it is the only one where both are cones of operators on a module rather than of elements of an algebra.

**Boundaries.** The space, the two generators, the ambient four units and the two cones as point sets are *$M_2(\mathbb{C})$ Defining Representation*; the pairings of two columns and of two operators, their Gram matrices and the four norms are *$M_2(\mathbb{C})$ Defining Representation : Products, Forms and Norms*; the operators of the biquaternion algebra, with the two-sided operator $X\mapsto QXP$, its cone, its ladder $1,4,7,16$ and its gauge, are *$M_2(\mathbb{C})$ Pauli Representation : Operators*; the general rank criterion and the determinantal variety at the size four are *$M_4(\mathbb{C})$ Pauli Representation* and its operators companion; the endomorphism algebra, $\mathrm{GL}_2(\mathbb{C})$ and $\mathrm{PGL}_2(\mathbb{C})$ are *The Endomorphisms of $\mathbb{C}^2$*; the lattice and the incidence are *The Subspaces of $\mathbb{C}^2$*. The general theory of operators on a module, with the two-sided operators and the tensor form of the linear map, is *Modules*, and the vectorisation and the coefficient array are *The Sylvester Operator and the Kronecker Sum of $M_4(\mathbb{C})$*.

**Conventions.** The carrier is $V=\mathbb{C}^{2}$ with the basis $e_1,e_2$, the dual is $V^{*}$ with the dual basis, $\phi(u)=\phi^{\mathsf T}u$ is the pairing with no conjugation, $E_{jk}=e_je_k^{\mathsf T}$ are the matrix units, $M^{\mathsf T}$ and $M^{\dagger}$ are the transpose and the conjugate transpose, and $J_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$. The operator is written $L_{u}R_{\phi}=u\phi^{\mathsf T}$ with the column on the left and the row on the right, and $\mathcal{C}$ is the set of all of them, the **bilinear cone**, with $\mathcal{C}_{H}$ the **Hermitian cone** of the matrices $uu^{\dagger}$.

## The One-Sided Operators

**The left side of the carrier is a full matrix algebra and the right side is a dual space, and the two sides are of different kinds.**

### The Left Multiplication

**Definition.** For $A\in M_2(\mathbb{C})$ the **left multiplication** is the operator
$$
L_A:V\longrightarrow V,\qquad L_A(v)=Av .
$$

**Proposition (the left operators are all the $\mathbb{C}$-linear operators).** The map $A\mapsto L_A$ is an isomorphism of algebras $M_2(\mathbb{C})\to\operatorname{End}_{\mathbb{C}}(V)$, and it is faithful; the left operators form a space of complex dimension four and real dimension eight.

*Proof.* The map is linear, multiplicative because $L_A L_B=L_{AB}$, and injective because $L_A$ determines the columns of $A$ as the images of the basis; both spaces have complex dimension four.

**The four left operators of the basis are the four units.** For $A=E_{jk}$ the operator sends $e_k$ to $e_j$ and kills the other basis column, so
$$
L_{E_{11}}=\begin{pmatrix}1&0\\ 0&0\end{pmatrix},\quad
L_{E_{12}}=\begin{pmatrix}0&1\\ 0&0\end{pmatrix},\quad
L_{E_{21}}=\begin{pmatrix}0&0\\ 1&0\end{pmatrix},\quad
L_{E_{22}}=\begin{pmatrix}0&0\\ 0&1\end{pmatrix},
$$
and the image of the four units is the four units. For $A=\begin{pmatrix}1&2\\ 3&4\end{pmatrix}$ the two images of the basis are $Ae_1=(1,3)$ and $Ae_2=(2,4)$, which are the two columns of the matrix, the reading of §*The Carrier and Its Basis* of the defining article. **The left operator adds nothing to the matrix, and it is not a proper subspace of the operators.**

**The left side is therefore the whole algebra.** In the algebra categories the left multiplication acts on an algebra and its image is a proper subspace; here it acts on the module, which is smaller than the algebra, and the image is everything that can happen. **The left operator is nothing but the matrix, and no information is lost in writing it.**

### The Right Slot

**Definition.** The **right slot** of a two-sided operator is its second parameter, and it is an element of the dual,
$$
\phi:V\longrightarrow\mathbb{C},\qquad v\longmapsto\phi(v)=\phi^{\mathsf T}v .
$$
The operator built from a functional is $L_{u_0}R_{\phi}=u_0\phi^{\mathsf T}$, for a column $u_0$.

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
L_{u}R_{\phi}=u\phi^{\mathsf T},\qquad L_{u}R_{\phi}(v)=\phi(v)\,u .
$$

**Proposition (the elementary properties).** For all $u,u'\in V$, $\phi,\phi'\in V^{*}$ and $\lambda\in\mathbb{C}$:
$$
L_{u}R_{\phi}+L_{u'}R_{\phi}=L_{u+u'}R_{\phi},\qquad
L_{u}R_{\phi}+L_{u}R_{\phi'}=L_{u}R_{\phi+\phi'},\qquad
L_{\lambda u}R_{\phi}=L_{u}R_{\lambda\phi}=\lambda\,L_{u}R_{\phi},
$$
and $L_{u}R_{\phi}=0$ if and only if $u=0$ or $\phi=0$.

*Proof.* The three identities are the distributivity of the matrix product over the sum of rank-one factors. The last is the statement that a product of a nonzero column and a nonzero row is nonzero, entrywise.

**Proposition (the fibre is exactly the scaling orbit).** If $L_{u}R_{\phi}=L_{u'}R_{\phi'}\neq0$ then $u'=\lambda u$ and $\phi'=\lambda^{-1}\phi$ for a unique $\lambda\in\mathbb{C}^{\times}$; the fibres of the parametrisation are therefore the orbits
$$
(u,\phi)\longmapsto(\lambda u,\lambda^{-1}\phi),
$$
and the parametrisation is injective in each slot once the other is fixed.

*Proof.* Both matrices have the same image, which is the line $\mathbb{C}u=\mathbb{C}u'$, so $u'=\lambda u$; then $u\phi^{\mathsf T}=u\lambda\phi'^{\mathsf T}$ and the rows are equal because $u\neq0$ and the map $\phi\mapsto u\phi^{\mathsf T}$ is injective.

**A worked member.** For $u=(1,i)$ and $\phi=(2,1-i)$ the products of the coordinates are the four entries,
$$
L_{u}R_{\phi}=u\phi^{\mathsf T}=\begin{pmatrix}2&1-i\\ 2i&1+i\end{pmatrix},
$$
with $\operatorname{tr}=3+i=\phi(u)$ and $\det=0$. The two rows are proportional with ratio $i$ and the two columns with ratio $(1+i)/2i=(1-i)/2$, which is the fibre of the parametrisation at work.

**The dimension count.** The parameter space has complex dimension four. The fibre has complex dimension one. The image has complex dimension three and real dimension six, inside an ambient of complex dimension four and real dimension eight. **The deficit of one complex dimension is the scaling and nothing else**, which is the sharpest difference from the algebra categories, where the cone is cut out twice: once by the scaling and once by the failure of the parameter to reach the whole ambient.

**The cone is not a subspace.** The identity is not a member, $I_2\notin\mathcal{C}$, and it is the sum of the two members $E_{11}$ and $E_{22}$. **The additive failure of the family is the identity itself**, and this is the smallest possible witness: two rank-one terms of rank sum two.

## The Cone and the Coefficient Matrix

**Definition.** Fix the **operator basis** $E_{11},E_{12},E_{21},E_{22}$ of $M_2(\mathbb{C})$ and write $M=\sum_{j,k}w_{jk}E_{jk}$. The **coefficient array** of $M$ is the matrix $c(M)$ of its four coefficients, and in this basis it is the matrix itself.

**Proposition (the criterion, in the rank form and then in the determinant form).** For $M\in M_2(\mathbb{C})$ the following are equivalent: $M\in\mathcal{C}$; $\operatorname{rank}M\le1$; $c(M)$ has rank at most one; $\det M=0$.

*Proof.* The first two are equivalent by the definition and the rank-one factorisation of matrices of rank at most one. The coefficient array is the matrix, so the third is the second. The determinant vanishes exactly when the two columns are dependent, which is the second; **and the determinant form is available only because the carrier is two-dimensional**, the general criterion being the rank inequality (*$M_4(\mathbb{C})$ Pauli Representation*).

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
| ambient | $M_2(\mathbb{C})$, complex dimension $4$ | the Hermitian subspace, the four real coordinates $t,x,y,z$ |
| equation | $\det M=0$ | $\det M=0$ on the Hermitian subspace |
| dimension | complex $3$ | real $3$ |
| parameters modulo the fibre | $([u],[\phi])\in\mathbb{P}^{1}\times\mathbb{P}^{1}$ | $[u]\in\mathbb{P}^{1}$ |
| fibres of the parametrisation | $\mathbb{C}^{\times}$, real dimension $2$ | $S^{1}$, real dimension $1$ |
| rulings | two, independent | one |
| fixed by the dagger | no | yes |
| trace | $\phi(u)$, any complex value | $\lVert u\rVert^{2}\ge0$ |
| trace-free members | $\phi(u)=0$, a hyperplane section | $u=0$ only |

**The two lines of the table that carry the reading.** The fibres: the bilinear cone quotients by a complex scaling and the Hermitian cone by a phase, so the second quotient is a circle and the first is a complex line with the origin removed. The trace: a member of the bilinear cone can have any complex trace, and a member of the Hermitian cone has a nonnegative one. **The positivity of the trace is the inertia of the definite form, and it is the whole difference between a cone of operators and a cone of states.**

### The Light Cone

**Theorem (the Hermitian cone is the light cone).** The Pauli coordinates of $M\in\mathcal{C}_{H}$ satisfy
$$
t^{2}-x^{2}-y^{2}-z^{2}=0,\qquad t=\tfrac12\operatorname{tr}M\ge0,
$$
and the map is onto the closed future cone.

*Proof.* The determinant identity $\det M=t^{2}-\lvert\vec x\rvert^{2}$ on the Hermitian subspace and the vanishing of the determinant on $\mathcal{C}_{H}$ give the equation; the trace is $\lVert u\rVert^{2}=2t\ge0$; and every point of the cone is attained by a column of norm $\sqrt{2t}$ in the corresponding direction. The computation is in *$M_2(\mathbb{C})$ Defining Representation*, §*The Pauli Coordinates*.

**Three involutions act on the one cone, and each fixes its own family.** The transposition $T\mapsto T^{\mathsf T}$ fixes the symmetric rank-one matrices $c\,uu^{\mathsf T}$ and **exchanges the two rulings**, because it swaps the column and the row; the conjugation $T\mapsto\bar T$ fixes the real matrices $u\phi^{\mathsf T}$ with $u,\phi$ real and acts on **each** ruling separately, sending $(u,\phi)$ to $(\bar u,\bar\phi)$ without exchanging them; the dagger $T\mapsto T^{\dagger}$ fixes the Hermitian ones. **The cone is closed under all three, and the three fixed loci have two distinct sizes**: the symmetric family is a complex cone of complex dimension two, that is real dimension four, because its scalar is complex, while the real family and the Hermitian family are both of real dimension three, $2+2-1$ for the pair of real columns modulo the real scaling and $2+1$ for the column modulo its phase times its modulus.

## The Composition

**The family is closed under composition, the scalar is absorbed, and the trace records the absorption.**

**Proposition (the composition rule).** For all pairs,
$$
L_{u}R_{\phi}\,L_{u'}R_{\phi'}=\phi(u')\,L_{u}R_{\phi'} .
$$

*Proof.* $u\phi^{\mathsf T}u'\phi'^{\mathsf T}=u(\phi^{\mathsf T}u')\phi'^{\mathsf T}$ and $\phi^{\mathsf T}u'=\phi(u')$ is a scalar.

**Corollary (the powers).** For $n\ge1$,
$$
\bigl(L_{u}R_{\phi}\bigr)^{n}=\phi(u)^{\,n-1}\,L_{u}R_{\phi} .
$$

*Proof.* Induction on the rule, the scalar being $\phi(u)$ at every step.

**Proposition (the three types of member).** For $T=L_{u}R_{\phi}\neq0$,
$$
T^{2}=0\iff\phi(u)=0,\qquad T^{2}=T\iff\phi(u)=1,
$$
and $T$ is invertible for no pair $(u,\phi)$.

*Proof.* The two equivalences are the corollary at $n=2$. Invertibility would require the rank to be two, since the inverse of a matrix has the rank of the matrix, and the rank is one.

**The trace and the spectrum.** The eigenvalues are $\phi(u)$ and $0$, so $\operatorname{tr}T=\phi(u)$ and $\det T=0$; the trace is the scalar that appears in the composition rule, and the Cayley–Hamilton identity degenerates to $T^{2}=\phi(u)T$. **The whole spectral theory of the pair is the single number $\phi(u)$**, and the two cases of the corollary are its two values.

**The semigroup.** The product is associative by the associativity of the matrix product. There is a zero, $L_{0}R_{\phi}=0$, and there is no identity, because $I_2$ has rank two and every member has rank at most one. The family is thus a **semigroup with zero and without identity**, and the multiplicative structure is the one of $\mathbb{P}^{1}\times\mathbb{P}^{1}$ with the pairing as the structure scalar.

**Remark (the comparison with the algebra family).** The family of the biquaternion algebra contains $L_{e_t}R_{e_t}$, the identity, and it contains inverses whenever both parameters are invertible (*$M_2(\mathbb{C})$ Pauli Representation : Operators*). **The module family contains neither**, and the reason is not the choice of parametrisation but the rank: a rank-one operator can never be the identity of a two-dimensional space.

## The Length

**Definition.** The **length** of $M\in M_2(\mathbb{C})$ is
$$
\ell(M)=\min\Bigl\{r:M=\sum_{i=1}^{r}L_{u_i}R_{\phi_i}\Bigr\},
$$
the least number of rank-one terms whose sum is $M$.

**Theorem (the length is the rank).** For every $M\in M_2(\mathbb{C})$,
$$
\ell(M)=\operatorname{rank}M,\qquad \ell(M)\in\{0,1,2\}.
$$

*Proof.* A sum of $r$ rank-one matrices has rank at most $r$, so $\ell(M)\ge\operatorname{rank}M$. Conversely, writing $c_j$ for the $j$-th column of $M$ and $e_j^{\mathsf T}$ for the $j$-th row of the identity,
$$
M=\sum_{j=1}^{2}c_j\,e_j^{\mathsf T},
$$
a sum of at most two rank-one terms, the terms with a zero column being dropped; so $\ell(M)$ is at most two and equals the rank. The identity is $E_{11}+E_{22}$ and has rank two.

**Remark (the row must be the basis row and not the row of $M$).** The sum $\sum_j c_jr_j^{\mathsf T}$ with the $j$-th row of $M$ in the second slot is $M^{2}$ and not $M$ (§*The Two Canonical Decompositions*), so the split of the proof uses the basis row $e_j^{\mathsf T}$; the two sums agree exactly on the projections, where $M^{2}=M$.

**The extremal cases.** The zero matrix has length zero, the cone is the set of length one, and the complement of the cone is the set of length two. **The length does not see the size of the entries**: a matrix of length two is a matrix of length two however small its determinant.

**Proposition (the elementary inequalities).** For all $M,N$ and $\lambda\neq0$,
$$
\ell(M+N)\le\ell(M)+\ell(N),\qquad \ell(\lambda M)=\ell(M),\qquad \ell(MN)\le\min\{\ell(M),\ell(N)\}.
$$

*Proof.* The first is the concatenation of two decompositions; the second is the homogeneity of the cone; the third is the rank inequality $\operatorname{rank}(MN)\le\min\{\operatorname{rank}M,\operatorname{rank}N\}$.

**The length of the product is not the sum.** In the algebra categories the composed operator can need as many terms as the sum of the two lengths, because the two slots carry independent parameters. Here the composition is a single rank-one product and the length of a product is at most one. **The length of the biquaternion pair runs over $0,1,2,3,4$, its chain of nested sets has dimensions $1,4,7,16$, and here the length collapses to $0,1,2$ and the chain to the three members $0\subset\mathcal{C}\subset M_2(\mathbb{C})$ of dimensions $0,3,4$**: the scalar line is not in the cone here, because $I_2$ has rank two, so the chain has no first member above the vertex, and the collapse is the collapse of the carrier from an algebra to a module.

## The Gallery of Members

**Nineteen members, twelve of length one and seven of length two, each read by the same four numbers.**

### The Reading of a Member

**A length-one member is read by four numbers and two lines, and no other datum exists.**

**Proposition (the entries, the square, the kernel and the image).** For $u=(p,q)$ and $\phi=(r,s)$,
$$
L_{u}R_{\phi}=\begin{pmatrix}pr&ps\\ qr&qs\end{pmatrix},\qquad
\operatorname{tr}L_{u}R_{\phi}=\phi(u)=pr+qs,\qquad
\det L_{u}R_{\phi}=0,
$$
$$
\bigl(L_{u}R_{\phi}\bigr)^{2}=\phi(u)\,L_{u}R_{\phi},\qquad
\ker L_{u}R_{\phi}=\ker\phi,\qquad
\operatorname{im}L_{u}R_{\phi}=\mathbb{C}u .
$$
**The four entries are the four products $pr$, $ps$, $qr$, $qs$, so the two rows are proportional and so are the two columns**, and the pair $(u,\phi)$ is recovered from the matrix up to the single scaling of §*The Two-Sided Operator*.

*Proof.* The matrix is the product of the column by the row, entry by entry. The trace is the sum of the two diagonal entries $pr$ and $qs$. The determinant vanishes because the two rows are $\phi^{\mathsf T}$ multiplied by $p$ and by $q$. The square is $u(\phi^{\mathsf T}u)\phi^{\mathsf T}$, and $\phi^{\mathsf T}u=\phi(u)$ is a scalar. The image is the line of $u$, because $L_{u}R_{\phi}(v)=\phi(v)u$ and $\phi(v)$ is a scalar; the kernel is the kernel of $\phi$, because $u\neq0$. ∎

### Twelve Members of Length One

**Each line is a pair of a column and a row, the matrix they produce, the scalar that decides its type, and the reading of the geometry.**

| Member | The pair $(u,\phi)$ | $\phi(u)$ | $M^{2}$ | The reading |
|---|---|---|---|---|
| $E_{11}=\begin{pmatrix}1&0\\0&0\end{pmatrix}$ | $e_1,\ e_1^{\mathsf T}$ | $1$ | $E_{11}$ | the projector onto $\mathbb{C}e_1$ along $\mathbb{C}e_2$ |
| $E_{22}=\begin{pmatrix}0&0\\0&1\end{pmatrix}$ | $e_2,\ e_2^{\mathsf T}$ | $1$ | $E_{22}$ | the complementary projector |
| $E_{12}=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ | $e_1,\ e_2^{\mathsf T}$ | $0$ | $0$ | the shift that sends $e_2$ to $e_1$ and kills $e_1$ |
| $E_{21}=\begin{pmatrix}0&0\\1&0\end{pmatrix}$ | $e_2,\ e_1^{\mathsf T}$ | $0$ | $0$ | the other shift |
| $P=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ | $(1,1),\ (1,1)$ | $2$ | $2P$ | the diagonal projector, doubled |
| $K=\begin{pmatrix}1&i\\ i&-1\end{pmatrix}$ | $(1,i),\ (1,i)$ | $0$ | $0$ | the isotropic nilpotent, symmetric and of square zero |
| $\pi=\tfrac12\begin{pmatrix}1&-i\\ i&1\end{pmatrix}$ | $\tfrac{1}{\sqrt2}(1,i),\ \tfrac{1}{\sqrt2}(1,-i)$ | $1$ | $\pi$ | the Hermitian projector onto the line $\mathbb{C}(1,i)$ |
| $\tfrac12\begin{pmatrix}1&i\\-i&1\end{pmatrix}$ | $\tfrac{1}{\sqrt2}(1,-i),\ \tfrac{1}{\sqrt2}(1,i)$ | $1$ | itself | the complementary Hermitian projector |
| $T=\begin{pmatrix}2&1-i\\ 2i&1+i\end{pmatrix}$ | $(1,i),\ (2,1-i)$ | $3+i$ | $(3+i)T$ | the worked member of §*The Two-Sided Operator* |
| $3E_{11}=\begin{pmatrix}3&0\\0&0\end{pmatrix}$ | $(3,0),\ (1,0)$ | $3$ | $3M$ | a member off the idempotent locus |
| $(1+i)E_{12}=\begin{pmatrix}0&1+i\\0&0\end{pmatrix}$ | $(1+i,0),\ (0,1)$ | $0$ | $0$ | a complex multiple of a nilpotent, still nilpotent |
| $\begin{pmatrix}2&6\\1&3\end{pmatrix}$ | $(2,1),\ (1,3)$ | $5$ | $5M$ | four nonzero entries, rows in the ratio $2$ |

**Every entry of the table is checked by the proposition above.** For $K$ the two rows are $(1,i)$ and $(i,-1)=i(1,i)$, the two columns are $(1,i)$ and $(i,-1)$, and the trace is $1+(-1)=0$; for $\pi$ the trace is one and the matrix is Hermitian, so $\pi^{2}=\pi$ is the projection property itself. **The two entries $E_{12}$ and $K$ have square zero and the four entries $E_{11}$, $E_{22}$, $P/2$ and $\pi$ have square themselves**, and no other type occurs.

**The two nilpotents of the table are not the same nilpotent.** $E_{12}$ has image $\mathbb{C}e_1$ and kernel $\mathbb{C}e_1$, equal lines and non-isotropic; $K$ has image and kernel the isotropic line $\mathbb{C}(1,i)$. **Both are of length one and both have square zero, and they are distinguished by the form $B$ and by nothing in the matrix**: $e_1^{\mathsf T}e_1=1$ and $(1,i)^{\mathsf T}(1,i)=0$.

### The Scalar That Decides

**One number, three types, and the type is the geometry of the two lines.**

**Proposition (the trichotomy).** For $T=L_{u}R_{\phi}\neq0$,
$$
T^{2}=0\iff\phi(u)=0\iff\mathbb{C}u\subseteq\ker\phi,\qquad
T^{2}=T\iff\phi(u)=1 .
$$
In the general case $\phi(u)\neq0$ the member $\phi(u)^{-1}T$ is a projector, and the image line and the kernel line are complementary exactly when $\phi(u)\neq0$.

*Proof.* The two equivalences are the square read twice. The inclusion $\mathbb{C}u\subseteq\ker\phi$ is the vanishing of $\phi$ on $u$, which is $\phi(u)=0$. When $\phi(u)\neq0$ the scalar $\phi(u)^{-1}$ makes the square equal the member itself. The lines are complementary exactly when $u\notin\ker\phi$, which is the same vanishing read the other way. ∎

**The three lines of the trichotomy are the three readings of the corner $(p,q;r,s)$.** A member of length one is therefore a line, a transverse line through it, and a complex number; **the nilpotent case is the degenerate one in which the two lines coincide**, and the idempotent case is the normalised one in which the complex number is one.

### The Hermitian Members of Length One

**A length-one member cannot be indefinite, and the obstruction is the rank.**

**Proposition (the Hermitian members of length one).** A member $L_{u}R_{\phi}\neq0$ is Hermitian exactly when $\phi=\mu\overline{u}$ with $\mu$ real, and then
$$
L_{u}R_{\phi}=\mu\,uu^{\dagger},\qquad
\operatorname{spec}=\bigl\{\mu\lVert u\rVert^{2},\ 0\bigr\},
\qquad
\bigl(\mu uu^{\dagger}\bigr)^{2}=\mu\lVert u\rVert^{2}\bigl(\mu uu^{\dagger}\bigr).
$$
**So the Hermitian members of length one are the positive multiples of a rank-one projector and their negatives, and none of them is indefinite.**

*Proof.* The matrix $u\phi^{\mathsf T}$ is Hermitian when $u_j\overline{\phi_k}=\overline{u_k\phi_j}$ for all $j,k$. If $u_1\neq0$ the pair $(j,k)=(1,1)$ gives $\phi_1$ in terms of $u$, and the pair $(1,k)$ then forces $\phi_k=\mu\overline{u_k}$ with $\mu=\phi_1/\overline{u_1}$, real because the entry $(1,1)$ is self-conjugate; the case $u_1=0$ is the same argument on the other coordinate. The spectrum is read from the square, whose scalar is $\mu(u^{\mathsf T}\overline{u})=\mu\lVert u\rVert^{2}$, a positive real multiple of $\mu$. ∎

**The consequence is a sharp separation of the two lengths.** The member $\sigma_3=\operatorname{diag}(1,-1)$ is Hermitian and indefinite, so it is not of length one and its length is two. **The Hermitian cone of §*The Hermitian Cone and the Light Cone* is exactly the set of the positive Hermitian members of length one**, and the indefinite Hermitian operators sit in the length-two stratum: the length and the signature are two readings of the same failure, which is the failure of the rank.

### The Members of Length Two

**Length two is invertibility, and the seven following members are the standard witnesses.**

| Member | $\det$ | $\operatorname{tr}$ | The reading |
|---|---|---|---|
| $I_2$ | $1$ | $2$ | the identity, $E_{11}+E_{22}$ |
| $J_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ | $1$ | $0$ | the complex structure, $J_2^{2}=-I_2$ |
| $\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | $-1$ | $0$ | the reflection in the diagonal, $\sigma_1^{2}=I_2$ |
| $\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ | $-1$ | $0$ | the indefinite Hermitian member, $\sigma_3^{2}=I_2$ |
| $N=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ | $1$ | $2$ | the unipotent shear, not diagonalisable |
| $\operatorname{diag}(\varepsilon,1)$ | $\varepsilon$ | $1+\varepsilon$ | of length two for every $\varepsilon\neq0$ |
| $\begin{pmatrix}1&2\\3&4\end{pmatrix}$ | $-2$ | $5$ | a generic member, no structure at all |

**The fifth line is the one that carries the reading.** $N$ has a single eigenvalue, the value $1$, and its eigenspace is the line $\mathbb{C}e_1$ of dimension one, so $N$ is not diagonalisable and $N^{k}=\begin{pmatrix}1&k\\0&1\end{pmatrix}$ for every $k\ge1$. **A member of length two can have a repeated eigenvalue and can fail to be diagonalisable, and a member of length one cannot fail in that way**: a rank-one member has the two eigenvalues $\phi(u)$ and $0$, and its eigenspaces are $\ker\phi$ and the line $\mathbb{C}u$, of dimensions one and one whenever $\phi(u)\neq0$.

**The sixth line is the statement that the length is not the size of the entries.** For every $\varepsilon\neq0$ the determinant is $\varepsilon$ and the length is two; at $\varepsilon=0$ the member is $E_{22}$ and the length drops to one. **The length is constant on the complement of the cone and jumps at its boundary**, and the jump is the drop of the rank.

### The Two Canonical Decompositions

**A member of length two has two natural splits into two rank-one terms, and the two splits are different.**

**Proposition (the column form and the row form).** For every $M\in M_2(\mathbb{C})$,
$$
M=\sum_{j=1}^{2}c_j\,e_j^{\mathsf T}=\sum_{k=1}^{2}e_k\,\rho_k^{\mathsf T},
$$
where $c_j$ is the $j$-th column of $M$ and $\rho_k^{\mathsf T}$ is its $k$-th row. **The first keeps one column and kills the other column, and the second keeps one row and kills the other row**; both are sums of two members of length one when $\det M\neq0$.

*Proof.* The first sum reproduces the $j$-th column in the $j$-th place and puts a zero in the other column, so the sum is $M$; the second reproduces the $k$-th row in the $k$-th place and puts a zero in the other row. ∎

**The shear, in the two forms.** For $N=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ the two columns are $c_1=(1,0)$ and $c_2=(1,1)$, so
$$
N=c_1e_1^{\mathsf T}+c_2e_2^{\mathsf T}
=\begin{pmatrix}1&0\\0&0\end{pmatrix}+\begin{pmatrix}0&1\\0&1\end{pmatrix},
\qquad
N=e_1\rho_1^{\mathsf T}+e_2\rho_2^{\mathsf T}
=\begin{pmatrix}1&1\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\0&1\end{pmatrix},
$$
**two different pairs of members of length one for one member of length two**, and the two pairs share no term.

**A generic member, in the two forms.** For $G=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ the columns are $c_1=(1,3)$ and $c_2=(2,4)$ and the rows are $(1,2)$ and $(3,4)$, so
$$
G=\begin{pmatrix}1&0\\3&0\end{pmatrix}+\begin{pmatrix}0&2\\0&4\end{pmatrix}
=\begin{pmatrix}1&2\\0&0\end{pmatrix}+\begin{pmatrix}0&0\\3&4\end{pmatrix}.
$$

**Remark (the wrong split, and the identity that corrects it).** The product $c_jr_j^{\mathsf T}$ of a column with the row of the same index is not a term of $M$: the sum
$$
\sum_{j=1}^{2}c_j\,r_j^{\mathsf T}
$$
has the entry $\sum_j M_{ij}M_{jk}$ in the place $(i,k)$, which is $M^{2}$ and not $M$. **The two agree exactly when $M^{2}=M$**, that is, on the projections; the correct split uses the basis row $e_j^{\mathsf T}$ in place of the row $r_j^{\mathsf T}$. The confusion is the confusion of the two slots: the column of $M$ and the row of $M$ are both computed from $M$, and only one of them may be used per term if the sum is to be $M$ and not $M^{2}$.

### The Four Matrices of the Diagonal Basis

**Two columns produce four members of length one, and the four are a basis in which every standard matrix is one line.**

**The four members.** With $a=(1,1)$ and $b=(1,-1)$,
$$
aa^{\mathsf T}=\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
ab^{\mathsf T}=\begin{pmatrix}1&-1\\1&-1\end{pmatrix},\qquad
ba^{\mathsf T}=\begin{pmatrix}1&1\\-1&-1\end{pmatrix},\qquad
bb^{\mathsf T}=\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
$$
**each of length one and each of rank one**, the first and the fourth symmetric, the second and the third not.

**Proposition (the standard matrices as one line each).** In this basis,
$$
I_2=\tfrac12\bigl(aa^{\mathsf T}+bb^{\mathsf T}\bigr),\qquad
\sigma_1=\tfrac12\bigl(aa^{\mathsf T}-bb^{\mathsf T}\bigr),\qquad
\sigma_3=\tfrac12\bigl(ab^{\mathsf T}+ba^{\mathsf T}\bigr),\qquad
J_2=\tfrac12\bigl(ba^{\mathsf T}-ab^{\mathsf T}\bigr).
$$
**The four members of length one are linearly independent, and the four standard matrices of the article are their symmetric and antisymmetric combinations**, so the operator space is spanned by members of length one and every element is a short sum of them.

*Proof.* Each identity is read on the four entries, or from the two expansions $e_1=\tfrac12(a+b)$ and $e_2=\tfrac12(a-b)$ substituted in the definition of the matrix. For the independence, a vanishing combination
$$
\alpha\,aa^{\mathsf T}+\beta\,ab^{\mathsf T}+\gamma\,ba^{\mathsf T}+\delta\,bb^{\mathsf T}
=a\,\lambda^{\mathsf T}+b\,\mu^{\mathsf T},\qquad
\lambda=\alpha a+\beta b,\quad \mu=\gamma a+\delta b,
$$
evaluated at an arbitrary $v$ gives $\lambda(v)a+\mu(v)b=0$, hence $\lambda(v)=\mu(v)=0$ because $a$ and $b$ are independent; so $\lambda=\mu=0$ and then $\alpha=\beta=\gamma=\delta=0$, again by the independence of $a$ and $b$. ∎

**Remark (what the table of this section says about the length).** The identity, the reflection, the indefinite form and the complex structure are each the half-sum or half-difference of two members of length one, so their length is at most two; and each of them has a nonzero determinant, so the length is exactly two. **The length is the number of terms, and this basis exhibits the two terms of every one of them.**

### The Spectral Decomposition of $J_2$

**The smallest member of length two is the difference of two projectors, and the two projectors are Hermitian.**

**Proposition (the spectral pair of $J_2$).** The eigenvalues of $J_2$ are $i$ and $-i$, on the isotropic lines $\mathbb{C}(1,i)$ and $\mathbb{C}(1,-i)$, and the spectral members are
$$
\pi=\tfrac12\begin{pmatrix}1&-i\\ i&1\end{pmatrix},\qquad
I_2-\pi=\tfrac12\begin{pmatrix}1&i\\-i&1\end{pmatrix},
$$
both Hermitian, both of length one, both of square themselves and mutually orthogonal, $\pi(I_2-\pi)=0$. Then
$$
J_2=i\,\pi-i\,(I_2-\pi).
$$

*Proof.* The two displays are the two readings: $\pi$ is the member $\tfrac{1}{\sqrt2}(1,i)\cdot\tfrac{1}{\sqrt2}(1,-i)^{\mathsf T}$, and $I_2-\pi$ is the other; their sum is $I_2$ by the previous section, $\pi^{2}=\pi$ by the trace, and the product vanishes by $\phi(u')=0$ on the complementary pair. The last identity is the difference read on the four entries. ∎

**The reading.** A member of length two is a complex combination of two orthogonal members of length one, and the coefficients are its eigenvalues. **In the module there is no algebra product to carry the spectral theorem, and yet the spectral decomposition survives as the shortest decomposition of the member**, with the two terms being the two eigenprojectors and the two scalars being the two eigenvalues. The real form $J_2$ of the complex structure has the pair $(\pi,I_2-\pi)$ attached to it, and the pair is the whole of its spectral theory.

### The Kernel, the Image and the Rank

**The two lines and the two scalars of a member are the table, and the rank is the collapse of the two lines.**

| Member | $\ker$ | $\operatorname{im}$ | The relation of the two |
|---|---|---|---|
| $E_{11}$ | $\mathbb{C}e_2$ | $\mathbb{C}e_1$ | transverse, disjoint |
| $E_{12}$ | $\mathbb{C}e_1$ | $\mathbb{C}e_1$ | equal |
| $K$ | $\mathbb{C}(1,i)$ | $\mathbb{C}(1,i)$ | equal, and isotropic |
| $\pi$ | $\mathbb{C}(1,-i)$ | $\mathbb{C}(1,i)$ | orthogonal, $\ker\pi=(\operatorname{im}\pi)^{\perp}$ |
| $T$ | $\ker(2,1-i)$ | $\mathbb{C}(1,i)$ | transverse, $\phi(u)=3+i\neq0$ |
| $I_2$, $J_2$, $N$ | $\{0\}$ | $V$ | no line at all |

**The first five lines are all the length-one geometry, and the last line is the whole of the length-two geometry.** A rank-one member carries one line through its image and one line as its kernel, and the kernel line is the image line exactly in the nilpotent case. **A rank-two member carries no line**: its kernel is the origin and its image is the whole carrier, and the only data left are the four entries.

## The Two Ranks

**Definition.** For $M\in M_2(\mathbb{C})$ let $\operatorname{rank}_{\mathrm{op}}M$ be the rank of $M$ as an operator on $V$ and $\operatorname{rank}c(M)$ the rank of its coefficient array in the operator basis.

**Proposition (the two ranks coincide identically).** In the matrix-unit basis,
$$
\operatorname{rank}_{\mathrm{op}}M=\operatorname{rank}c(M)=\operatorname{rank}M ,
$$
for every $M$.

*Proof.* The coefficient array is the matrix, so the two ranks are the same number computed twice.

**Why this is a statement and not a tautology.** In the algebra categories the operator space is not the algebra: the two-sided operator $L_{Q}R_{P}$ acts on the algebra, of complex dimension four in the biquaternion case, inside an ambient of complex dimension sixteen, and its coefficient array is taken in a basis $L_{e_\mu}R_{e_\nu}$ which is not the matrix-unit basis of the source. There the rank of the operator and the rank of the coefficient array separate, and the criterion $\operatorname{rank}c(M)\le1$ is stronger than the rank-one condition. **Here the operator space and the ambient are the same space, the basis is the matrix-unit basis, and the two ranks are one number**: which is why the criterion of §*The Cone and the Coefficient Matrix* can be stated as $\det M=0$ and still be exact.

**The table of the comparison.**

| | this module | the algebra pair |
|---|---|---|
| ambient of the operator | $M_2(\mathbb{C})$, complex dimension $4$ | $\operatorname{End}(\mathbb{B})$, complex dimension $16$ |
| operator basis | $E_{jk}$ | $L_{e_\mu}R_{e_\nu}$ |
| coefficient array | the matrix | sixteen coefficients |
| two ranks | equal | independent |
| criterion | $\operatorname{rank}M\le1$ | $\operatorname{rank}c(M)\le1$ |
| the length | $0,1,2$ | $0,\dots,4$ |
| the chain of nested sets | $0\subset\mathcal{C}\subset M_2(\mathbb{C})$, dimensions $0,3,4$ | $1,4,7,16$ |

## The Adjoints and the Types

**Two adjoints act on the pair, the transpose and the dagger, and each has a family of fixed points that is a rank-one family.**

### The Transpose Adjoint

**Definition.** With the complex bilinear form $\langle X,Y\rangle=\operatorname{Tr}(X^{\mathsf T}Y)$ on $M_2(\mathbb{C})$, the **transpose adjoint** of $T$ is the unique $T^{\mathsf T}$ with $\langle TX,Y\rangle=\langle X,T^{\mathsf T}Y\rangle$.

**Proposition (the transpose swaps the slots).** For every pair,
$$
\bigl(L_{u}R_{\phi}\bigr)^{\mathsf T}=L_{\phi}R_{u},
$$
that is $\phi u^{\mathsf T}$ in coordinates.

*Proof.* $(u\phi^{\mathsf T})^{\mathsf T}=\phi u^{\mathsf T}$, the column becoming a row and the row a column.

**The families of the transposition.**

| Family | Condition | Description |
|---|---|---|
| self-adjoint | $\phi=c\,u$ | the symmetric rank-one matrices $c\,uu^{\mathsf T}$ |
| anti-self-adjoint | $\phi=-c\,u$ with $c\neq0$ | empty: $c\,uu^{\mathsf T}=-c\,uu^{\mathsf T}$ forces $c=0$ |
| general | none | the cone |

**Proposition (no nonzero member of the cone is anti-self-adjoint).** If $T\in\mathcal{C}$ and $T^{\mathsf T}=-T$ then $T=0$.

*Proof.* An antisymmetric matrix of size two is $\lambda J_2=\lambda\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, whose rank is two for $\lambda\neq0$ and which is therefore not in the cone; and $\lambda=0$ is the zero matrix.

**The self-adjoint cone is the symmetric rank-one family.** It is the set of matrices $c\,uu^{\mathsf T}$, of complex dimension two, and it is the **complex** analogue of the Hermitian cone: **the same construction with the transpose in place of the dagger, and the two families are as different as a complex line is from a circle.**

### The Hermitian Adjoint

**Definition.** With $\langle X,Y\rangle_{H}=\operatorname{Tr}(X^{\dagger}Y)$, the **Hermitian adjoint** of $L_{u}R_{\phi}$ is
$$
\bigl(L_{u}R_{\phi}\bigr)^{\dagger}=L_{\bar\phi}R_{\bar u}=\bar\phi\,\bar u^{\mathsf T}.
$$

The conjugate is taken in **both** slots: the first because the row $\phi^{\mathsf T}$ becomes $\bar\phi^{\mathsf T}$, the second because $u$ is conjugated in the transpose, $(u\phi^{\mathsf T})^{\dagger}=\bar\phi\,\bar u^{\mathsf T}$. The transpose, by contrast, conjugates nothing and only exchanges the slots.

**Proposition (the fixed points of the dagger).** $T^{\dagger}=T$ for a nonzero $T\in\mathcal{C}$ exactly when $T$ is a real multiple of a member of $\mathcal{C}_{H}$.

*Proof.* The computation of §*The Hermitian Cone and the Light Cone*: the equality forces $\phi=c\bar u$ with $c$ real, and the matrix is $c\,uu^{\dagger}$.

**The three involutions and their fixed loci.**

| Involution | Action on $L_{u}R_{\phi}$ | Fixed locus |
|---|---|---|
| transposition | $L_{\phi}R_{u}$ | the symmetric cone $c\,uu^{\mathsf T}$ |
| conjugation | $L_{\bar u}R_{\bar\phi}$ | the real cone |
| dagger | $L_{\bar\phi}R_{\bar u}$ | the Hermitian cone $\mathcal{C}_{H}$ |

**The anti-Hermitian members are in the cone and not in the Hermitian cone.** The matrix $i\,uu^{\dagger}$ is anti-Hermitian, it is a member of $\mathcal{C}$ since $i\,uu^{\dagger}=L_{u}R_{i\bar u}$, and it is not in $\mathcal{C}_{H}$ because its trace is imaginary. **The cone is closed under multiplication by any complex scalar and the Hermitian cone is closed only under the real ones**, so the first is a complex object and the second a real one, and the anti-Hermitian members are what the complex scaling adds.

### The Isometries

**Proposition (there is no nonzero isometry).** For every nonzero $T\in\mathcal{C}$ the two products $T^{\dagger}T$ and $T^{\mathsf T}T$ have rank at most one, so neither equals $I_2$.

*Proof.* Two scalars are in play and they must not be confused. The Hermitian one is the norm, $\lVert u\rVert^{2}=u^{\dagger}u=\sum_j\lvert u_j\rvert^{2}>0$ for $u\neq0$; the bilinear one is $\tau=u^{\mathsf T}u=\sum_ju_j^{2}$, which **can vanish for a nonzero $u$**, as it does for $u=(1,i)$. With the dagger,
$$
T^{\dagger}T=\bar\phi\,(\bar u^{\mathsf T}u)\,\phi^{\mathsf T}=\lVert u\rVert^{2}\,\bar\phi\,\phi^{\mathsf T},
$$
a matrix of rank at most one, and the identity has rank two. With the transpose,
$$
T^{\mathsf T}T=\phi\,(u^{\mathsf T}u)\,\phi^{\mathsf T}=\tau\,\phi\,\phi^{\mathsf T},
$$
of rank at most one as well, and of rank zero when $\tau=0$. Neither can be $I_2$.

**The family therefore contains no isometry, no orthogonal member and no unitary member.** In the algebra categories the invertibles of the algebra give isometries of the operator space, and the length ladder starts at one because the identity is a product; here the identity is not a product at all, and the isometry group of the family is empty.

## The Two Generators and the Ambient Space

**Two matrices generate the regular representation of the two-dimensional algebra, and the four units are the basis of the ambient space of all operators: two counts, two questions, and neither corrects the other.**

**The two generators.** Put the reduced biquaternion product on the carrier, $(a+jb)(c+jd)=(ac+bd)+j(ad+bc)$ with $j^{2}=1$, so that the algebra is $\mathbb{C}[j]/(j^{2}-1)$, of complex dimension two with the basis $1,j$. The left multiplications are
$$
L(z)=\begin{pmatrix}z_{\blacktriangle}&z_{\blacktriangledown}\\ z_{\blacktriangledown}&z_{\blacktriangle}\end{pmatrix},
\qquad
L(1)=I_2,\qquad
L(j)=\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},
$$
**two matrices and no more**, and the two-sided family is
$$
\{L_uR_v\}=\{L_{uv}\mid uv\in\mathbb{C}[j]/(j^{2}-1)\}=\operatorname{span}\{I_2,\sigma_1\},
$$
of complex dimension two. **The identity is the first generator in every basis and the second generator carries the whole choice**: in the basis $(e_+,e_-)$ of idempotents it is $\tfrac12(I_2-\sigma_3)$ and in the basis $(1,ij)$ it is $-J_2$, the three being conjugate by the change of basis, and the details are §*The Two Generators* of the defining article.

**The four units.** The ambient space is $M_2(\mathbb{C})$, of complex dimension four, with the basis $E_{jk}=L_{e_j}R_{\epsilon^{k}}$, and the rank-one cone is a cone of complex dimension three inside it.

| Object | Complex dimension | Its generators or basis | The family it describes |
|---|---|---|---|
| the algebra, with its product | $2$ | two matrices, $I_2$ and $L_\beta$ | the plane $\{L_uR_v\}$ |
| the ambient operator space | $4$ | the four units $E_{jk}$ | the cone $u\phi^{\mathsf T}$ |

**The plane is not the cone, and the difference is the point of the article.** The plane carries the identity, is closed under the product and is a subalgebra; its members are $\begin{pmatrix}\alpha&\beta\\ \beta&\alpha\end{pmatrix}$, of determinant $\alpha^{2}-\beta^{2}$, so it meets the rank-one cone exactly in the two lines $\alpha=\pm\beta$, which are the isotropic lines of the split norm and the lines of the idempotents $e_{\pm}$. The cone carries no identity, is not closed under the sum and is the determinantal variety of §*The Cone and the Coefficient Matrix*. **Two matrices describe the algebra exactly and describe the cone only along two of its lines.**

**The reading in force.** The rest of the article uses the module, because in the module reading the family of two-sided operators is exactly the rank-one locus and the parametrisation by $V\times V^{*}$ modulo scaling is exact. **The two-generator reading is the algebra reading, and it is not the same object.**

## What the Pair Buys and Does Not

**What it buys.**

- The **parametrisation** of the cone by $V\times V^{*}$ modulo the scaling, hence by $\mathbb{P}^{1}\times\mathbb{P}^{1}$, which turns every rank-one matrix into a pair of lines and every statement about the cone into a statement about the two rulings.
- The **single criterion** $\det M=0$, exact at this size and reducible to the rank inequality in general.
- The **composition rule** $L_{u}R_{\phi}L_{u'}R_{\phi'}=\phi(u')L_{u}R_{\phi'}$, whose scalar is the trace, and with it the whole spectral theory of the family in one number.
- The **length formula** $\ell=\operatorname{rank}$, the values $0,1,2$ and the identity at length two.
- The **two cones** and the dagger that relates them, which is the only place in the corpus where the bilinear and the Hermitian rank-one families are compared on the same carrier.
- The **two adjoints**, with the self-adjoint family, the empty anti-self-adjoint family and the Hermitian fixed locus.

**What it does not buy.**

- **The identity.** $I_2$ has rank two and is not a member; the family is a semigroup with zero and not a monoid.
- **The inverses.** No member is invertible; the group of invertibles is empty.
- **The isometries.** No nonzero member satisfies $T^{*}T=I_2$, so there is no orthogonal or unitary sector.
- **The reach beyond the cone.** Every member is of rank at most one; a matrix of rank two needs a sum of two members, and the sum is not a member.
- **The mixing of the two rulings.** The two rulings are independent, but the composition contracts them to a single pair, and no operation of the pair mixes the two families.

**The comparison table.**

| | this module | the biquaternion $M_2(\mathbb{C})$ pair |
|---|---|---|
| carrier | the module $V$, complex dimension $2$ | the algebra $\mathbb{B}$, complex dimension $4$ |
| two-sided operator | $u\phi^{\mathsf T}$, one column and one row | $QXP$, two algebra elements |
| parameter space | $V\times V^{*}$, complex dimension $4$ | $\mathbb{B}\times\mathbb{B}$, complex dimension $8$ |
| fibre | $\mathbb{C}^{\times}$, complex dimension $1$ | the scalars, complex dimension $1$ |
| reach | complex dimension $3$ | complex dimension $7$ |
| identity in the family | no | yes, $L_{e_t}R_{e_t}$ |
| inverses in the family | no | yes, for pairs of invertibles |
| isometries | none | the group $\{\pm\mathrm{Ad}_{\tilde Q}\}$, of complex dimension three |
| the length | $0,1,2$ | $0,\dots,4$ |
| the chain of nested sets | $0\subset\mathcal{C}\subset M_2(\mathbb{C})$, dimensions $0,3,4$ | $1,4,7,16$ |
| rank constraint | rank $\le1$ | rank $0$ or $4$, by the division algebra |
| the second cone | the Hermitian cone, distinct | no second cone of the same kind |

**The single sentence.** The pair is the cleanest operator theory of the corpus because the cone is thin and the composition is a scalar; it is also the poorest, because a rank-one family has no group of invertibles, and **everything that the algebra pairs gain they gain by the identity being a product.**

## Summary

The carrier is the module $V=\mathbb{C}^{2}$, and there is no product on it, so the two-sided operator of the module is $L_{u}R_{\phi}(v)=\phi(v)u=u\phi^{\mathsf T}$, a rank-one matrix with a column and a row; with the reduced biquaternion product it is the algebra $\mathbb{C}[j]/(j^{2}-1)$ and the family is the plane $\operatorname{span}\{I_2,\sigma_1\}$, the two-generator reading of §*The Two Generators and the Ambient Space*. The left side is the whole algebra $M_2(\mathbb{C})$ acting faithfully, of complex dimension four, and the right side is the dual $V^{*}$, of complex dimension two; the transpose adjoint of the right slot is the left slot and the Hermitian adjoint is not. The parametrisation by $V\times V^{*}$ has fibres the scaling orbits $\mathbb{C}^{\times}$ and image the determinantal cone of $\mathbb{P}^{3}$, that is the Segre quadric $\mathbb{P}^{1}\times\mathbb{P}^{1}$, of complex dimension three and real dimension six inside an ambient of real dimension eight; the coefficient array in the matrix-unit basis is the matrix itself, so the rank criterion and the determinant criterion are the same condition, and the cone spans the ambient although the identity is not a member.

The composition is $L_{u}R_{\phi}L_{u'}R_{\phi'}=\phi(u')L_{u}R_{\phi'}$, with powers $\phi(u)^{n-1}L_{u}R_{\phi}$; the member is nilpotent exactly when $\phi(u)=0$ and idempotent exactly when $\phi(u)=1$; the trace is $\phi(u)$, the determinant is zero, and the Cayley–Hamilton identity is $T^{2}=\phi(u)T$. The family is a semigroup with zero and without identity, and no member is invertible. The length is the rank, with the values $0,1,2$: zero for the zero matrix, one on the cone, two on the complement, and two for the identity. The two ranks, of the operator and of its coefficient array, coincide identically here, in contrast with the algebra pairs, where the operator basis is $L_{e_\mu}R_{e_\nu}$ and the two separate.

**The gallery of §*The Gallery of Members* is the whole of the length formula at this size.** A member is a column, a row and the single scalar $\phi(u)$: the scalar zero gives the nilpotents, of which $E_{12}$ has kernel equal to image and $K=\begin{pmatrix}1&i\\ i&-1\end{pmatrix}$ has kernel and image the isotropic line; the scalar one gives the four projectors $E_{11}$, $E_{22}$, $\frac12 P$ and $\pi=\frac12\begin{pmatrix}1&-i\\ i&1\end{pmatrix}$; and the general scalar gives the member up to the projectors. **The Hermitian members of length one are the real multiples of $uu^{\dagger}$ and none is indefinite**, so $\sigma_3$ sits in the length-two stratum; and every length-two member has the two canonical splits $M=\sum_j c_je_j^{\mathsf T}=\sum_k e_k\rho_k^{\mathsf T}$, which for $J_2$ become the spectral pair $J_2=i\pi-i(I_2-\pi)$.

Two rank-one families live in the ambient: the bilinear cone, of complex dimension three, with two rulings and fibres $\mathbb{C}^{\times}$, and the Hermitian cone $uu^{\dagger}$, of real dimension three, with one ruling, fibres $S^{1}$, and the future light cone $t^{2}-\lvert\vec x\rvert^{2}=0$, $t\ge0$ in the Pauli coordinates; the second is the fixed locus of the dagger in the first, up to real scale. The transpose adjoint swaps the slots and its fixed locus is the symmetric cone $c\,uu^{\mathsf T}$; the dagger's fixed locus is the Hermitian cone; no nonzero member of the cone is anti-self-adjoint, and no nonzero member is an isometry. Four generators are needed and two do not suffice: the four matrix units $E_{jk}=L_{e_j}R_{\epsilon^{k}}$ are a basis of the operator space, and two matrices with complex coefficients span a plane through $I_2$, of complex dimension two, which is the shape of every two-dimensional unital algebra and is never the rank-one locus. **The pair buys the parametrisation, the single criterion, the composition rule, the length and the comparison of the two cones, and it pays with the identity, the inverses, the isometries and the ladder $1,4,7,16$.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V=\mathbb{C}^{2}$ | the carrier, the defining module |
| $V^{*}$, $\phi,\psi$ | the dual and its elements, the rows |
| $\phi(u)=\phi^{\mathsf T}u$ | the pairing, with no conjugation |
| $L_A$ | the left multiplication $v\mapsto Av$ |
| $E_{jk}=L_{e_j}R_{\epsilon^{k}}$ | the matrix units, the basis of the ambient operator space |
| $L_{u}R_{\phi}=u\phi^{\mathsf T}$ | the two-sided operator of the pair $(u,\phi)$ |
| $\mathcal{C}$ | the bilinear cone, the set of all $L_{u}R_{\phi}$ |
| $\mathcal{C}_{H}$ | the Hermitian cone, the set of all $uu^{\dagger}$ |
| $M^{\mathsf T}$, $M^{\dagger}$ | the transpose and the conjugate transpose |
| $\langle X,Y\rangle$, $\langle X,Y\rangle_{H}$ | the bilinear and the Hermitian forms on the operator space |
| $c(M)$ | the coefficient array of $M$ in the matrix-unit basis |
| $\ell(M)$ | the length, the least number of rank-one terms |
| $J_2$ | the alternating matrix $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ |
| $N$ | the shear $\begin{pmatrix}1&1\\0&1\end{pmatrix}$, of length two and not diagonalisable |
| $\pi$ | the Hermitian projector $\tfrac12\begin{pmatrix}1&-i\\ i&1\end{pmatrix}$ |
| $w_{jk}$ | the coefficients of $M$ in the basis $E_{jk}$ |
| $t,x,y,z$ | the Pauli coordinates of a Hermitian matrix |
| $\mathbb{P}^{1}\times\mathbb{P}^{1}$ | the projectivised cone, the Segre quadric |

## Further Reading

*Duo-Complex Numbers* is the entry point of the category: the space, its two scalar structures, the bases, the complex structure $J$ and the norm, and it is where the triangles of the coordinates are fixed. *$M_2(\mathbb{C})$ Defining Representation* is the first article of the trio: the two basis columns, the four matrix units and the five bases of the operator space, the three forms, the lines, the flags, the two cones as point sets, the spinor and the qubit. *$M_2(\mathbb{C})$ Defining Representation : Products, Forms and Norms* is the second: the three pairings of two columns and their six real forms, the two pairings of two operators, the determinant as a quadratic form and the four norms. *$M_2(\mathbb{C})$ Pauli Representation* and its operators companion are the algebra pair on the same algebra: the frame, the Peirce decomposition, the trace, the determinant, the two-sided operator $X\mapsto QXP$, the cone of the algebra, the length ladder $1,4,7,16$ and the gauge, and they are what this article is measured against. *The Endomorphisms of $\mathbb{C}^2$* carries the algebra $M_2(\mathbb{C})$, the conjugate-linear maps, $\mathrm{GL}_2(\mathbb{C})$, $\mathrm{PGL}_2(\mathbb{C})$ and the centraliser of $J$. *The Subspaces of $\mathbb{C}^2$* carries the lattice, the flag and the incidence.

On the general theory, *Modules* fixes the two-sided operator on a module and its second slot in the dual, *The Sylvester Operator and the Kronecker Sum of $M_4(\mathbb{C})$* carries the vectorisation and the coefficient array, *The Determinant and Alternating Forms* carries the determinant as a form, and *$M_4(\mathbb{C})$ Pauli Representation* with its operators companion carries the rank criterion and the determinantal variety at the general size, of which the determinant criterion here is the two-dimensional case. *The Forms, the Norms and the Singular Set of $M_4(\mathbb{C})$* develops the stratified picture of the singular set, and *Direct Sums, Free Modules and Rank* the notion of rank that the length computes.
