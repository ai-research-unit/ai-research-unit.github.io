
# __Linear Maps and Matrices__

## Introduction

A linear map is a homomorphism of vector spaces, and a matrix is what a linear map becomes once a basis is chosen. The two are not the same object: the map is intrinsic and the matrix depends on the choice of bases, with two matrices representing the same map exactly when they are conjugate by an invertible matrix. This article develops the dictionary between them, proves the rank–nullity theorem, identifies the rank of a matrix as a single number defined in three apparently different ways, and records what happens when the field of scalars is replaced by a ring.

The base of this category is a commutative ring, and the preceding article on projective and injective modules was written there. Rank–nullity, however, is a field statement: it uses that a subspace always has a complement, which is false over a general ring. Throughout this article $F$ is therefore a field, $V$ and $W$ are finite-dimensional $F$-vector spaces, and linear means $F$-linear; the final section records the module case, where matrices still make sense but the theory of rank changes character and the computational tool becomes reduction by elementary row and column operations, the Smith normal form over a principal ideal domain, in place of Gaussian elimination.

The article closes with the rank criterion for linear systems and the two canonical ways of simplifying a matrix by invertible row and column operations: row reduction over a field, and the Smith normal form over a principal ideal domain, whose invariants were computed in the article of this category on modules over a PID.

## Linear Maps

### Definition and Elementary Properties

**Definition.** Let $V$ and $W$ be $F$-vector spaces. A map $T:V \to W$ is **linear**, or an $F$-linear map, if $T(u+v)=T(u)+T(v)$ and $T(\lambda v)=\lambda T(v)$ for all $u,v \in V$ and $\lambda \in F$. Equivalently $T(\lambda u+\mu v)=\lambda T(u)+\mu T(v)$.

The set of linear maps $V \to W$ is written $\operatorname{Hom}_F(V,W)$ and is itself an $F$-vector space under $(S+T)(v)=S(v)+T(v)$ and $(\lambda T)(v)=\lambda T(v)$. The identity map is written $\operatorname{id}_V$, or $I$ when the space is clear. The **kernel** and **image** are

$$
\ker T=\{v \in V : T(v)=0\}, \qquad \operatorname{im}T=T(V)=\{T(v) : v \in V\},
$$

both subspaces, of $V$ and $W$ respectively, and $T$ is injective exactly when $\ker T=0$ and surjective exactly when $\operatorname{im}T=W$.

Composition of linear maps is linear, so the endomorphisms $\operatorname{End}_F(V)=\operatorname{Hom}_F(V,V)$ form a ring under addition and composition, and the invertible elements of that ring form the group $\operatorname{GL}(V)$ of **automorphisms** of $V$. This group is not covered here of the category.

### Kernel, Image and Rank–Nullity

**Definition.** The **rank** of a linear map $T:V \to W$ is $\operatorname{rk}T=\dim_F\operatorname{im}T$, and its **nullity** is $\operatorname{null}T=\dim_F\ker T$.

**Theorem (rank–nullity).** For every $T:V \to W$ with $V$ finite-dimensional,

$$
\dim_F V=\dim_F\ker T+\dim_F\operatorname{im}T, \qquad \text{that is} \qquad \dim_F V=\operatorname{null}T+\operatorname{rk}T .
$$

*Proof.* Let $u_1,\dots,u_k$ be a basis of $\ker T$. By the basis extension theorem it extends to a basis $u_1,\dots,u_k,v_1,\dots,v_r$ of $V$. The images $T(v_1),\dots,T(v_r)$ span $\operatorname{im}T$, because any $T(v)$ with $v=\sum a_i u_i+\sum b_j v_j$ equals $\sum b_j T(v_j)$. They are independent: if $\sum b_j T(v_j)=0$ then $T(\sum b_j v_j)=0$, so $\sum b_j v_j \in \ker T$ and hence is a combination of the $u_i$; independence of the full basis forces all $b_j=0$. Thus $T(v_1),\dots,T(v_r)$ is a basis of $\operatorname{im}T$, so $\operatorname{rk}T=r$ and $k+r=\dim_F V$. $\square$

The theorem fails once $F$ is replaced by a ring, and the failure is structural: the proof extends a basis of $\ker T$ to a basis of $V$, which requires $\ker T$ to be a direct summand. Over $R=\mathbb{Z}$ the map $T:\mathbb{Z}\to\mathbb{Z}$, $T(x)=2x$, has kernel $0$ and image $2\mathbb{Z}\cong\mathbb{Z}$, and the numerical identity $1=0+1$ survives, but the subgroup $2\mathbb{Z}$ has no complement in $\mathbb{Z}$, so no basis of $\mathbb{Z}$ adapted to the kernel exists. Over a non-domain the very notion of dimension disappears; over $R=\mathbb{Z}/4\mathbb{Z}$ the map $x \mapsto 2x$ has kernel and image both equal to the two-element submodule $2R$, which is not free, so no rank is defined.

### Consequences

**Corollary.** For $T:V \to W$ with $\dim_F V=\dim_F W=n$, the following are equivalent: $T$ is injective; $T$ is surjective; $T$ is an isomorphism; $\operatorname{rk}T=n$.

*Proof.* By rank–nullity, injectivity means $\dim\ker T=0$, hence $\operatorname{rk}T=n$, hence $\dim\operatorname{im}T=n$, hence $\operatorname{im}T=W$. The other implications are immediate. $\square$

This is the finite-dimensional statement that fails in infinite dimension and over rings: the shift map on the space of sequences $(a_1,a_2,\dots)\mapsto(0,a_1,a_2,\dots)$ is injective and not surjective; and the multiplication-by-$2$ map on $\mathbb{Z}$ is injective and not surjective.

**Corollary.** If $S:U \to V$ and $T:V \to W$ are linear then $\operatorname{rk}(TS) \le \min(\operatorname{rk}S,\operatorname{rk}T)$, and

$$
\operatorname{rk}S+\operatorname{rk}T-\dim_F V \le \operatorname{rk}(TS) .
$$

*Proof.* The image of $TS$ is contained in the image of $T$, so $\operatorname{rk}(TS) \le \operatorname{rk}T$; and $\operatorname{im}(TS)=T(\operatorname{im}S)$ is the image under $T$ of the subspace $\operatorname{im}S$, so $\operatorname{rk}(TS) \le \dim\operatorname{im}S=\operatorname{rk}S$. For the lower bound, the restriction of $T$ to $\operatorname{im}S$ has image $\operatorname{im}(TS)$ and kernel $\operatorname{im}S \cap \ker T$; rank–nullity applied to that restriction gives $\operatorname{rk}(TS)=\operatorname{rk}S-\dim(\operatorname{im}S\cap\ker T) \ge \operatorname{rk}S-\dim\ker T=\operatorname{rk}S+\operatorname{rk}T-\dim V$. $\square$

The second inequality is **Sylvester's rank inequality**; the first is the elementary bound. Both are used in the theory of canonical forms.

## Matrices

### Coordinates and the Matrix of a Map

**Definition.** A **basis** $\mathcal{B}$ of $V$ is an ordered list $v_1,\dots,v_n$ spanning $V$ and linearly independent. The **coordinate vector** of $v \in V$ is the unique column $[v]_{\mathcal{B}}=(a_1,\dots,a_n)^{\mathsf{T}}$ with $v=\sum_i a_i v_i$.

**Definition.** Let $\mathcal{B}=v_1,\dots,v_n$ be a basis of $V$ and $\mathcal{C}=w_1,\dots,w_m$ a basis of $W$. The **matrix of $T$ with respect to $\mathcal{B}$ and $\mathcal{C}$** is the $m \times n$ matrix $[T]_{\mathcal{B}}^{\mathcal{C}}$ whose $j$-th column is the coordinate vector $[T(v_j)]_{\mathcal{C}}$. It is characterised by

$$
[T(v)]_{\mathcal{C}}=[T]_{\mathcal{B}}^{\mathcal{C}}\,[v]_{\mathcal{B}} \qquad \text{for all } v \in V .
$$

The superscript names the basis of the target and the subscript the basis of the source. The $j$-th column records where the $j$-th basis vector goes; linearity then determines the whole map, so the assignment $T \mapsto [T]_{\mathcal{B}}^{\mathcal{C}}$ is a bijection

$$
\operatorname{Hom}_F(V,W) \longrightarrow M_{m\times n}(F)
$$

that is linear, and it is an isomorphism of vector spaces of dimension $mn$. Writing $E_{ij}$ for the matrix with a single $1$ in position $(i,j)$, the maps whose matrices are $E_{ij}$ form a basis of $\operatorname{Hom}_F(V,W)$.

### Matrix Multiplication is Composition

**Proposition.** For linear maps $U \xrightarrow{S} V \xrightarrow{T} W$ and bases $\mathcal{A},\mathcal{B},\mathcal{C}$,

$$
[T \circ S]_{\mathcal{A}}^{\mathcal{C}}=[T]_{\mathcal{B}}^{\mathcal{C}}\,[S]_{\mathcal{A}}^{\mathcal{B}} .
$$

*Proof.* Both sides have the same effect on every coordinate vector: $[T(S(u))]_{\mathcal{C}}=[T]_{\mathcal{B}}^{\mathcal{C}}[S(u)]_{\mathcal{B}}=[T]_{\mathcal{B}}^{\mathcal{C}}[S]_{\mathcal{A}}^{\mathcal{B}}[u]_{\mathcal{A}}$, and two matrices agreeing on all coordinate vectors are equal. $\square$

So matrix multiplication is defined the way it is precisely so that it computes composition. The associativity of matrix multiplication is the associativity of composition, and the identity matrix is the matrix of the identity map in any basis.

### Change of Basis

Let $\mathcal{B}$ and $\mathcal{B}'$ be two bases of $V$. The **change-of-basis matrix** from $\mathcal{B}'$ to $\mathcal{B}$ is $P=[\operatorname{id}_V]_{\mathcal{B}'}^{\mathcal{B}}$, whose columns are the coordinates of the vectors of $\mathcal{B}'$ in $\mathcal{B}$; it is invertible with inverse $P^{-1}=[\operatorname{id}_V]_{\mathcal{B}}^{\mathcal{B}'}$, and $[v]_{\mathcal{B}}=P[v]_{\mathcal{B}'}$.

**Proposition.** If $T:V \to V$ is linear, then

$$
[T]_{\mathcal{B}'}^{\mathcal{B}'}=P^{-1}[T]_{\mathcal{B}}^{\mathcal{B}}P .
$$

*Proof.* Compose the three maps: $\operatorname{id}_V$ from $\mathcal{B}'$ to $\mathcal{B}$, then $T$, then $\operatorname{id}_V$ from $\mathcal{B}$ to $\mathcal{B}'$. The matrix of a composition is the product of the matrices, giving $[\operatorname{id}]_{\mathcal{B}}^{\mathcal{B}'}[T]_{\mathcal{B}}^{\mathcal{B}}[\operatorname{id}]_{\mathcal{B}'}^{\mathcal{B}}=P^{-1}[T]_{\mathcal{B}}^{\mathcal{B}}P$. $\square$

Two matrices $A,B$ related by $B=P^{-1}AP$ for some invertible $P$ are called **similar**, or **conjugate**; the proposition says precisely that similar matrices represent the same endomorphism in different bases. Similarity is an equivalence relation, and every invariant of an endomorphism — rank, trace, determinant, characteristic polynomial, minimal polynomial — is a similarity invariant. Deciding when two matrices are similar is the content of the theory of canonical forms, treated in the applications article of this category on the Jordan form.

For a map between different spaces one changes bases independently: if $P$ is a change of basis in $V$ and $Q$ in $W$, the matrix of $T$ transforms as

$$
[T]_{\mathcal{B}'}^{\mathcal{C}'}=Q^{-1}[T]_{\mathcal{B}}^{\mathcal{C}}P .
$$

Matrices related in this way are **equivalent**, and over a field every matrix is equivalent to one of the form

$$
\begin{pmatrix} I_{r} & 0 \\ 0 & 0 \end{pmatrix}
$$

with exactly $r$ ones on the diagonal, where $r=\operatorname{rk}T$. This normal form under independent row and column operations is Gaussian elimination, and it is the matrix form of the rank–nullity theorem.

## Rank

### Column Rank Equals Row Rank

**Definition.** Let $A$ be an $m \times n$ matrix over $F$. Its **column rank** is the dimension of the subspace of $F^m$ spanned by its columns, its **row rank** the dimension of the subspace of $F^n$ spanned by its rows, and its **(linear) rank** $\operatorname{rk}A$ is its column rank.

**Theorem.** For every matrix, column rank equals row rank.

*Proof.* Let $T:F^n \to F^m$ be the linear map with matrix $A$ in the standard bases, so that $\operatorname{im}T$ is the column space and $\operatorname{rk}A=\operatorname{rk}T$. The transpose $A^{\mathsf{T}}$ is the matrix of the linear map $T^*:F^m \to F^n$ given by $T^*(y)=A^{\mathsf{T}}y$, whose image is exactly the row space of $A$. Hence row rank $=\operatorname{rk}T^*$. Now $\ker T^*=(\operatorname{im}T)^{\perp}=\{y : y^{\mathsf{T}}Ax=0 \text{ for all } x \in F^n\}$, which has dimension $m-\dim\operatorname{im}T=m-\operatorname{rk}A$; applying rank–nullity to $T^*:F^m \to F^n$ gives

$$
\operatorname{rk}T^*=m-\dim\ker T^*=m-(m-\operatorname{rk}A)=\operatorname{rk}A . \qquad \square
$$

Because the two ranks agree, one writes $\operatorname{rk}A$ without qualification. The rank is the number of pivots in any row-echelon form of $A$, equivalently the size of the largest invertible square submatrix — the last equivalence is proved next.

### Rank and Minors

**Definition.** A **minor** of order $k$ of $A$ is the determinant of a $k \times k$ submatrix obtained by deleting $m-k$ rows and $n-k$ columns. The **determinantal rank** of $A$ is the largest $k$ for which some minor of order $k$ is nonzero, or $0$ if $A=0$.

**Theorem.** The linear rank equals the determinantal rank.

*Proof.* If columns $j_1,\dots,j_k$ are linearly dependent, then some nontrivial combination of them is zero, so every $k \times k$ minor using those columns has dependent columns and vanishes. Conversely, if a set of $k$ columns is independent, they span a $k$-dimensional space and the $m \times k$ matrix formed from them has rank $k$; among its rows some $k$ are independent, and the corresponding $k \times k$ minor is nonzero. Hence the largest size of a nonzero minor equals the largest size of an independent set of columns. $\square$

Over a field this gives the practical criterion: $\operatorname{rk}A \ge k$ if and only if some $k \times k$ minor is nonzero, and $\operatorname{rk}A=k$ if and only if some $k \times k$ minor is nonzero and every $(k+1)\times(k+1)$ minor vanishes. Over a ring the minors still generate the determinantal ideals $D_k(A)$ of the modules-over-a-PID article, but they no longer determine the module: over $\mathbb{Z}$ the matrices $(2)$ and $(1)$ have the same rank $1$ and cokernels $\mathbb{Z}/2\mathbb{Z}$ and $0$, so the rank of a matrix over a ring does not decide the structure of the quotient it defines.

### Rank in Terms of Composition

Rank has a characterisation by factorisation that is often the cleanest.

**Proposition.** $\operatorname{rk}T=r$ if and only if $T=S \circ R$ where $R:V \to F^r$ is surjective and $S:F^r \to W$ is injective.

*Proof.* If $\operatorname{rk}T=r$, choose a basis $w_1,\dots,w_r$ of $\operatorname{im}T$ and define $R(v)$ to be the coordinates of $T(v)$ in that basis, so that $R$ is surjective; define $S$ on the standard basis of $F^r$ by $e_i \mapsto w_i$, so that $S$ is injective and $T=SR$. Conversely, if $T=SR$ with $R$ surjective and $S$ injective, then $\operatorname{im}T=S(\operatorname{im}R)=S(F^r) \cong F^r$. $\square$

## The Dual Map and the Transpose

### The Dual Space

**Definition.** The **dual space** of $V$ is $V^*=\operatorname{Hom}_F(V,F)$, and the **dual basis** of a basis $v_1,\dots,v_n$ is the basis $v^1,\dots,v^n$ of $V^*$ defined by $v^i(v_j)=\delta^i_j$.

The dual basis is a basis, so $\dim_F V^*=\dim_F V$, and the evaluation map $V \to V^{**}$, $v \mapsto (\varphi \mapsto \varphi(v))$, is an isomorphism in finite dimension. This is a finite-dimensional accident: for an infinite-dimensional space the evaluation is injective and not surjective.

**Definition.** For linear $T:V \to W$, the **dual map** (or transpose) is

$$
T^*:W^* \to V^*, \qquad T^*(\varphi)=\varphi \circ T .
$$

The map $T \mapsto T^*$ is linear and reverses composition: $(TS)^*=S^*T^*$. If $A$ is the matrix of $T$ in bases $\mathcal{B},\mathcal{C}$, then the matrix of $T^*$ in the dual bases $\mathcal{C}^*,\mathcal{B}^*$ is $A^{\mathsf{T}}$, because

$$
(A^{\mathsf{T}})^i{}_j = A^j{}_i = \text{($j$-th coordinate of $T(v_i)$)} = \text{($T^*(w^j)$ applied to $v_i$)} .
$$

Hence the transpose operation on matrices is the coordinate form of the dual map, and the equality of row rank and column rank proved above is the statement $\operatorname{rk}T=\operatorname{rk}T^*$ combined with the identification of the row space with $\operatorname{im}T^*$.

### The Annihilator

For a subspace $U \subseteq V$ let $U^0=\{\varphi \in V^* : \varphi|_U=0\}$, the **annihilator**. Then $\dim_F U+\dim_F U^0=\dim_F V$, and

$$
\ker T^*=(\operatorname{im}T)^0, \qquad \operatorname{im}T^*=(\ker T)^0 .
$$

These identities are the dual form of rank–nullity and are the reason the rank of a map and of its dual agree in finite dimension.

## Systems of Linear Equations

### The Rank Criterion

A system $Ax=b$ with $A$ an $m \times n$ matrix over $F$ asks for the $x \in F^n$ with $T(x)=b$, where $T$ is the map with matrix $A$. The system is **consistent** if $b \in \operatorname{im}T$, that is, if $b$ lies in the column space of $A$; and the solution set, when non-empty, is a coset of $\ker T$, of size $|F|^{\operatorname{null}T}$ when $F$ is finite.

**Theorem (rank criterion).** The system $Ax=b$ is consistent if and only if

$$
\operatorname{rk}A=\operatorname{rk}[A \mid b],
$$

where $[A\mid b]$ is the augmented matrix.

*Proof.* The column space of $[A\mid b]$ contains the column space of $A$ and is spanned by it together with $b$; the two have the same dimension exactly when $b$ lies in the column space of $A$, which is consistency. $\square$

**Corollary.** If $m=n$ and $A$ is invertible, the system has a unique solution $x=A^{-1}b$. If $F$ is finite of order $q$ and $A$ is consistent with $\operatorname{null}A=k$, the system has $q^k$ solutions.

### Gaussian Elimination

The computational content behind the rank criterion is row reduction. The three **elementary row operations** are: interchange two rows; add a multiple of one row to another; multiply a row by a nonzero scalar. Each is left multiplication by an invertible matrix, so each preserves the row space and the consistency of the system, and a finite sequence of them puts $A$ into **reduced row-echelon form**, in which the first nonzero entry of each nonzero row, the **pivot**, is $1$, is the only nonzero entry of its column, and the pivots move strictly to the right. The number of pivots is the rank, the system is consistent exactly when no row has its only nonzero entry in the augmented column, and the solution is read off by setting the non-pivot variables to parameters.

Over a field, every matrix is equivalent by row and column operations to $\operatorname{diag}(I_r,0)$, so rank is a complete invariant of a matrix up to independent row and column operations. Up to similarity the invariant is much larger, and it is the subject of the articles on eigenvalues and on the Jordan form.

## Matrices over a Ring

### Invertibility

Let $A$ be an $n \times n$ matrix over a commutative ring $R$. If $AB=I$ for some $B$, then taking determinants gives $\det A \cdot \det B=1$, so $\det A$ is a unit of $R$; conversely, if $\det A$ is a unit then the adjugate matrix $A^{\mathrm{adj}}$ satisfies $A\,A^{\mathrm{adj}}=\det(A)I$, so $A$ is invertible with $A^{-1}=(\det A)^{-1}A^{\mathrm{adj}}$. Hence

$$
A \in \operatorname{GL}_n(R) \iff \det A \in R^{\times},
$$

the determinant being the multilinear alternating function fixed by the treatment in the article of this category on the special linear group. Over a field this says $A$ is invertible exactly when $\det A \neq 0$ and the rank criterion is $\operatorname{rk}A=n$.

### The Failure of Rank–Nullity

Over a ring, Gaussian elimination fails at the step that divides by a pivot: a nonzero non-unit cannot be used to clear a column, and the best available reduction is by elementary row and column operations, which over a principal ideal domain produce the Smith normal form. Rank–nullity is recovered only after passing to the fraction field: a submodule need not be a direct summand, so the basis-extension proof does not carry over, and what remains true for a map of finitely generated modules over a domain is that the **rational rank**, obtained by tensoring with the fraction field $K=\operatorname{Frac}(R)$, is additive on short exact sequences. The numerical identity therefore survives with the rational rank in place of the dimension, but it no longer determines the kernel or the image up to isomorphism, since the rank cannot see torsion. What replaces the rank of a matrix over a principal ideal domain is the Smith normal form, whose nonzero diagonal entries number the rank and whose remaining diagonal entries carry the torsion; this is the content of the modules-over-a-PID article, and it is the form in which rank is invoked for integer matrices and lattices later in the category.

**Example.** Over $R=\mathbb{Z}$ the matrix $A=(2)$ is not invertible, since $2$ is not a unit, and the map $\mathbb{Z}\to\mathbb{Z}$, $x \mapsto 2x$, has kernel $0$ and image $2\mathbb{Z}$ of rational rank $1$, so for this map the rational rank is additive, $1=0+1$. The failure lies elsewhere. The rank cannot see the torsion of the cokernel $\mathbb{Z}/2\mathbb{Z}$, which has rank $0$ although the module is nonzero, and the minimal number of generators is not additive: in the presentation $0 \to \mathbb{Z} \xrightarrow{\cdot 2} \mathbb{Z} \to \mathbb{Z}/2\mathbb{Z} \to 0$ the kernel $2\mathbb{Z}$ and the cokernel $\mathbb{Z}/2\mathbb{Z}$ each need one generator, while the middle term needs one as well, so no additivity of generator counts can hold. Over the field $\mathbb{Q}$ the same matrix becomes invertible and the cokernel disappears; the difference is exactly the torsion, invisible over a field.

## The Trace and the Determinant of a Matrix

The two scalar invariants attached to a square matrix are fixed here because the other articles of this category use them without redefining them.

**Definition.** For $A=(a_{ij}) \in M_n(F)$ the **trace** is $\operatorname{tr}A=\sum_{i=1}^{n}a_{ii}$, and the **determinant** is

$$
\det A=\sum_{\sigma \in S_n}\operatorname{sgn}(\sigma)\prod_{i=1}^{n}a_{i\sigma(i)},
$$

the sum running over the symmetric group $S_n$ and $\operatorname{sgn}$ being the sign of a permutation.

**Proposition.** (i) $\operatorname{tr}(AB)=\operatorname{tr}(BA)$, hence $\operatorname{tr}(P^{-1}AP)=\operatorname{tr}A$. (ii) $\det(AB)=\det A \det B$, hence $\det(P^{-1}AP)=\det A$. (iii) $A$ is invertible if and only if $\det A \neq 0$, and then $\det(A^{-1})=(\det A)^{-1}$. (iv) $\operatorname{rk}A$ is the largest $r$ for which some $r \times r$ minor of $A$ is nonzero.

*Proof.* (i) Both sides are $\sum_{i,j}a_{ij}b_{ji}$. (ii) is proved in the article of this category on the special linear group, where the determinant is characterised as the unique alternating multilinear function of the columns normalised to $\det I=1$. (iii) If $AB=I$ then $\det A \det B=1$, so $\det A \neq 0$; conversely a nonzero determinant admits the adjugate formula $A^{-1}=(\det A)^{-1}A^{\mathrm{adj}}$ with $A A^{\mathrm{adj}}=(\det A)I$. (iv) is the theorem on minors above. $\square$

Trace and determinant are therefore similarity invariants, unlike the individual matrix entries, and they are the first two coefficients of the characteristic polynomial $c_A(x)=\det(xI-A)=x^n-(\operatorname{tr}A)x^{n-1}+\cdots+(-1)^n\det A$. They are not complete invariants: the matrices $\operatorname{diag}(1,1)$ and $\operatorname{diag}(2,0)$ over $\mathbb{Q}$ have determinants $1$ and $0$ and are trivially different, while the Jordan block $\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix}$ and the scalar $\lambda I_2$ have the same trace and determinant and are not similar. Similarity classification requires the full characteristic and minimal polynomials and is not covered here and its applications.

## Summary

A linear map $T:V \to W$ is a homomorphism of $F$-vector spaces, with kernel and image subspaces and with rank $\operatorname{rk}T=\dim\operatorname{im}T$ and nullity $\operatorname{null}T=\dim\ker T$. The rank–nullity theorem states $\dim V=\operatorname{null}T+\operatorname{rk}T$, and it is proved by extending a basis of the kernel to a basis of $V$ and observing that the images of the appended vectors form a basis of the image. For square maps it forces injective, surjective and bijective to coincide, and it yields Sylvester's rank inequality for composites.

A basis converts a linear map into a matrix, with the rule $[T(v)]_{\mathcal{C}}=[T]_{\mathcal{B}}^{\mathcal{C}}[v]_{\mathcal{B}}$, and composition of maps into matrix multiplication; a change of basis conjugates the matrix, $[T]_{\mathcal{B}'}=P^{-1}[T]_{\mathcal{B}}P$, so similar matrices are the same endomorphism in different coordinates, while independent changes of bases give equivalence. The column rank, row rank and determinantal rank of a matrix all agree; the first is the dimension of the image of the map, the second the dimension of the image of the dual map, and the third the size of the largest nonvanishing minor. The dual space and the dual map give the transpose, whose rank equals that of the original.

A linear system $Ax=b$ is consistent exactly when $\operatorname{rk}A=\operatorname{rk}[A\mid b]$, and Gaussian elimination computes the rank, decides consistency and parametrises the solution set by the nullity. Over a commutative ring the determinant remains the invertibility criterion, $A \in \operatorname{GL}_n(R) \iff \det A \in R^{\times}$, but rank–nullity is recovered only over the fraction field and Gaussian elimination is replaced by elementary row and column operations, which over a principal ideal domain produce the Smith normal form; the rank is then the number of nonzero diagonal entries of that form, and the missing information is the torsion.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | a field; the scalars of this article |
| $V$, $W$, $U$ | finite-dimensional $F$-vector spaces |
| $T$, $S$ | linear maps |
| $\operatorname{Hom}_F(V,W)$ | vector space of linear maps $V \to W$ |
| $\operatorname{End}_F(V)$ | algebra of endomorphisms of $V$ |
| $\operatorname{GL}(V)$ | group of automorphisms of $V$ |
| $\ker T$, $\operatorname{im}T$ | kernel and image |
| $\operatorname{rk}T$, $\operatorname{null}T$ | rank $\dim\operatorname{im}T$ and nullity $\dim\ker T$ |
| $\mathcal{A},\mathcal{B},\mathcal{C}$ | bases |
| $[v]_{\mathcal{B}}$ | coordinate column of $v$ in $\mathcal{B}$ |
| $[T]_{\mathcal{B}}^{\mathcal{C}}$ | matrix of $T$, columns indexed by source basis, rows by target |
| $M_{m\times n}(F)$ | $m \times n$ matrices over $F$ |
| $E_{ij}$ | matrix with a single $1$ in position $(i,j)$ |
| $P$ | change-of-basis matrix, $[v]_{\mathcal{B}}=P[v]_{\mathcal{B}'}$ |
| $P^{-1}AP$ | similar matrices |
| $F^r$, $\operatorname{diag}(I_r,0)$ | normal form of a matrix under row and column operations |
| $A^{\mathsf{T}}$ | transpose matrix, matrix of the dual map |
| $T^*$ | dual map, $T^*(\varphi)=\varphi \circ T$ |
| $V^*$, $v^i$ | dual space and dual basis, $v^i(v_j)=\delta^i_j$ |
| $U^0$ | annihilator of a subspace |
| $\delta^i_j$ | Kronecker delta |
| $[A\mid b]$ | augmented matrix |
| $\operatorname{tr}$, $\det$ | trace and determinant |
| $R^{\times}$ | unit group of a ring $R$ |
| $\mathbb{Z}/n\mathbb{Z}$ | integers modulo $n$ |





## Further Reading

- Sheldon Axler, *Linear Algebra Done Right* (Springer, 3rd ed. 2015), for the determinant-free linear-map treatment and rank–nullity.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the module-theoretic treatment of linear and multilinear algebra.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for matrices over rings and the Smith normal form.
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004), for rank, change of basis and systems of equations.
- Kenneth Hoffman and Ray Kunze, *Linear Algebra* (Prentice Hall, 2nd ed. 1971), for the dual space, transpose and rank.
- Serge Lang, *Linear Algebra* (Springer, 3rd ed. 1987), for the classical coordinate treatment.
- Steven Roman, *Advanced Linear Algebra* (Springer, 3rd ed. 2008), for canonical forms and matrices over rings.
