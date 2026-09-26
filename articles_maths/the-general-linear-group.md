
# __The General Linear Group__

## Introduction

The invertible linear transformations of a vector space form a group under composition, and that group — the general linear group — is the symmetry group of the vector space itself. It carries the whole linear structure and nothing else: its subgroups that preserve an additional piece of structure are precisely the classical groups, and its action on the collection of subspaces organises the incidence geometry of the space. This article develops the group as a group, its dependence on a choice of basis, its centre and its projective quotient, and its actions on lines and on Grassmannians.

Throughout, $F$ is a field, $V$ is an $F$-vector space of finite dimension $n \ge 1$, and $\operatorname{GL}(V)$ is the group of $F$-linear bijections $V \to V$. The matrix group $\operatorname{GL}_n(F)$ is the same object after a basis is chosen, and the dependence on that choice is made explicit rather than suppressed. The determinant is used here only as the group homomorphism $\det:\operatorname{GL}(V)\to F^{\times}$; its construction, its uniqueness as an alternating multilinear invariant and the structure of its kernel are the business of the category, on the special linear group and the determinant.

The article ends where the geometry begins: $\operatorname{GL}(V)$ acts transitively on the $k$-dimensional subspaces for each $k$, the stabiliser of a subspace is a block-triangular subgroup, and the subgroups preserving a bilinear or sesquilinear form are the classical groups. The material is self-contained except for the standard facts about group actions and the Jordan canonical form, which is used only to describe conjugacy classes.

## The Group of Automorphisms

### Definition and Group Structure

**Definition.** A linear map $T:V \to V$ is **invertible** if there exists $S:V \to V$ with $ST=TS=\operatorname{id}_V$. The set of invertible linear maps is the **general linear group**

$$
\operatorname{GL}(V)=\operatorname{Aut}_F(V),
$$

with multiplication composition and identity $\operatorname{id}_V$.

**Proposition.** $\operatorname{GL}(V)$ is a group, and $T:V \to V$ is invertible if and only if $\ker T=0$, equivalently if and only if $T$ is surjective.

*Proof.* Composition is associative, $\operatorname{id}_V$ is an identity, and the inverse of a bijective linear map is linear, so $\operatorname{GL}(V)$ is a group. For a linear endomorphism of a finite-dimensional space, injective, surjective and bijective coincide by the rank–nullity theorem of the linear-maps article. $\square$

Since the spaces arising here are finite-dimensional, no distinction between left and right inverses is needed. In infinite dimension the group of invertible bounded operators is a genuinely different object, and the algebraic general linear group of all invertible linear maps becomes a large non-finitely-generated group; the finite-dimensional case is the one used in this category.

### Matrices and the Isomorphism with $\operatorname{GL}_n(F)$

Fix a basis $\mathcal{B}$ of $V$. The map

$$
\operatorname{GL}(V) \longrightarrow \operatorname{GL}_n(F), \qquad T \longmapsto [T]_{\mathcal{B}}^{\mathcal{B}},
$$

is an isomorphism of groups: it is a bijection because a linear map is determined by its matrix and every invertible matrix defines an invertible map, and it is multiplicative because the matrix of a composite is the product of the matrices, both facts proved in the linear-maps article. Its inverse sends a matrix $A$ to the operator $x \mapsto Ax$ on $F^n$.

The isomorphism is **not canonical**: it depends on $\mathcal{B}$. If $\mathcal{B}'$ is a second basis and $P=[\operatorname{id}_V]_{\mathcal{B}'}^{\mathcal{B}}$ is the change-of-basis matrix, then

$$
[T]_{\mathcal{B}'}^{\mathcal{B}'}=P^{-1}[T]_{\mathcal{B}}^{\mathcal{B}}P .
$$

So the two matrix realisations of $\operatorname{GL}(V)$ differ by conjugation by $P$, and an intrinsic statement about $\operatorname{GL}(V)$ is exactly a statement about $\operatorname{GL}_n(F)$ invariant under conjugation.

**Example.** For $n=1$, $\operatorname{GL}(V)=F^{\times}$, since a linear map on a line is multiplication by a nonzero scalar. For $n=0$, the group is trivial. For $n=2$ over $F$, $\operatorname{GL}_2(F)$ consists of the matrices $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ with $ad-bc \neq 0$; over the finite field $\mathbb{F}_q$ this gives $|\operatorname{GL}_2(\mathbb{F}_q)|=(q^2-1)(q^2-q)$, the count developed in the applications article on vector spaces over finite fields.

### The Centre and the Scalar Subgroup

**Definition.** The **centre** $Z(\operatorname{GL}(V))$ is the set of invertible maps commuting with every invertible map.

**Proposition.** If $V \neq 0$ then $Z(\operatorname{GL}(V))=\{\lambda \operatorname{id}_V : \lambda \in F^{\times}\}$, a subgroup isomorphic to $F^{\times}$.

*Proof.* A scalar map commutes with everything. Conversely, let $T$ commute with every $S \in \operatorname{GL}(V)$ and let $v \neq 0$. First $T(v) \in \langle v\rangle$: were $v,T(v)$ linearly independent they would extend to a basis, and the map $S$ with $S(v)=v$ and $S(T(v))=v+T(v)$ would be invertible with $ST(v)=v+T(v)$ while $TS(v)=T(v)$, contradicting $ST=TS$. Write $T(v)=\lambda_vv$, with $\lambda_v \neq 0$ because $T$ is invertible. If $u,v$ are independent then $T(u+v)=\lambda_{u+v}(u+v)=\lambda_uu+\lambda_vv$ forces $\lambda_u=\lambda_v$; if $u=cv$ are dependent then $\lambda_ucv=T(cv)=c\lambda_vv$, so again $\lambda_u=\lambda_v$. Hence all $\lambda_v$ agree and $T=\lambda\operatorname{id}_V$ with $\lambda \in F^{\times}$. $\square$

The centre is the group of **homotheties**, or dilations, and it is the kernel of the action of $\operatorname{GL}(V)$ on lines. It is not a complement to $\operatorname{SL}(V)$ in general: the scalar $\lambda \operatorname{id}$ has determinant $\lambda^n$, so the scalars meeting $\operatorname{SL}(V)$ are the $n$-th roots of unity.

## The Determinant Homomorphism

**Theorem.** The determinant defines a surjective group homomorphism

$$
\det:\operatorname{GL}(V) \longrightarrow F^{\times},
$$

whose kernel is the subgroup of automorphisms of determinant $1$.

*Proof.* Multiplicativity $\det(AB)=\det A \det B$ gives $\det(ST)=\det S \det T$, and invertibility forces $\det T \neq 0$, so the image lies in $F^{\times}$. Surjectivity: every $\lambda \in F^{\times}$ occurs, for instance as the determinant of the diagonal map sending a basis vector $v_1$ to $\lambda v_1$ and each other $v_i$ to itself. The kernel description is the definition of the kernel. $\square$

**Definition.** $\operatorname{SL}(V)=\ker\det$ is the **special linear group** of $V$.

The determinant is not merely one homomorphism among many: it is the unique alternating multilinear function of the columns with value $1$ on the identity, and it is therefore an invariant of the linear structure, not of the chosen basis. Another article of the category proves this uniqueness and works out the structure of $\operatorname{SL}(V)$, its generation by elementary operations, and its role as the commutator subgroup of $\operatorname{GL}(V)$; here only the homomorphism property and its consequences for the centre are used.

**Proposition.** $\operatorname{SL}(V)$ is a normal subgroup of $\operatorname{GL}(V)$, and $\operatorname{GL}(V)/\operatorname{SL}(V) \cong F^{\times}$.

*Proof.* It is the kernel of a homomorphism, hence normal, and the first isomorphism theorem identifies the quotient with the image $F^{\times}$. $\square$

## The Projective General Linear Group

### The Action on Lines

Let $\mathbb{P}(V)$ be the set of one-dimensional subspaces of $V$, the **projective space** of $V$. Every $T \in \operatorname{GL}(V)$ carries a line to a line, so there is an action

$$
\operatorname{GL}(V) \times \mathbb{P}(V) \longrightarrow \mathbb{P}(V), \qquad (T,\langle v\rangle) \longmapsto \langle T(v)\rangle .
$$

**Proposition.** The kernel of this action is $Z(\operatorname{GL}(V))$, so the action factors through an action of $\operatorname{GL}(V)/Z(\operatorname{GL}(V))$ on $\mathbb{P}(V)$ that is faithful and transitive.

*Proof.* $T$ fixes every line exactly when every vector is an eigenvector of $T$, which forces $T$ to be scalar; that is the centre. By the first isomorphism theorem the quotient acts faithfully. For transitivity, any two nonzero vectors lie in bases of $V$ of the same cardinality, and a linear isomorphism carries one basis to the other. $\square$

**Definition.** The **projective general linear group** is

$$
\operatorname{PGL}(V)=\operatorname{GL}(V)/Z(\operatorname{GL}(V))=\operatorname{GL}(V)/F^{\times},
$$

and the **projective special linear group** is $\operatorname{PSL}(V)=\operatorname{SL}(V)/(\operatorname{SL}(V)\cap Z(\operatorname{GL}(V)))$.

Two automorphisms have the same image in $\operatorname{PGL}(V)$ exactly when they differ by a nonzero scalar, and the class of a matrix is often written $[A]$. Since the scalars in $\operatorname{SL}(V)$ are the $n$-th roots of unity $\mu_n=\{\lambda \in F^{\times} : \lambda^n=1\}$, one has $\operatorname{PSL}(V) \cong \operatorname{SL}(V)/\mu_n$, and over a field in which every element has an $n$-th root, in particular over an algebraically closed field, $\operatorname{PSL}(V)=\operatorname{PGL}(V)$.

**Theorem (fundamental theorem of projective geometry).** For $\dim_F V \ge 3$, every automorphism of the incidence structure of $\mathbb{P}(V)$ — that is, every bijection of $\mathbb{P}(V)$ preserving collinearity — is induced by a semilinear automorphism of $V$, hence by an element of $\operatorname{PGL}(V)$ together with a field automorphism. In particular $\operatorname{Aut}(\mathbb{P}(V)) \cong \operatorname{PGL}(V) \rtimes \operatorname{Aut}(F)$ when every collineation is induced.

This is the classical rigidity statement: for dimension at least $3$ the projective geometry determines the linear group, so the quotient $\operatorname{PGL}(V)$ is not merely a group that acts on the geometry but is essentially the whole automorphism group of that geometry. In dimension $2$ the statement is false — the projective line is too small — which is one reason the low-dimensional cases of the transformation groups behave exceptionally.

## Actions on Subspaces and Grassmannians

### Transitivity and Stabilisers

For $0 \le k \le n$ let $\operatorname{Gr}_k(V)$ be the **Grassmannian** of $k$-dimensional subspaces of $V$; for $k=1$ it is $\mathbb{P}(V)$, and for $k=n-1$ the set of hyperplanes.

**Theorem.** $\operatorname{GL}(V)$ acts transitively on $\operatorname{Gr}_k(V)$ for each $k$. The stabiliser of a fixed $k$-subspace $W$ is the subgroup

$$
P_W=\{T \in \operatorname{GL}(V) : T(W) \subseteq W\}=\{T : T(W)=W\},
$$

and in a basis obtained by extending a basis of $W$ to a basis of $V$, the matrices of $P_W$ are exactly the invertible block upper triangular matrices

$$
\begin{pmatrix} A & B \\ 0 & D \end{pmatrix}, \qquad A \in \operatorname{GL}_k(F),\ D \in \operatorname{GL}_{n-k}(F).
$$

*Proof.* Transitivity: a linear isomorphism carries any $k$-subspace to any other, because bases of the two subspaces extend to bases of $V$, and a bijection of bases extends to an automorphism. For the stabiliser, an operator with $T(W) \subseteq W$ and $\dim W=\dim T(W)$ in finite dimension has $T(W)=W$, so the containment is an equality. In a basis adapted to $W$ the first $k$ columns of the matrix have their last $n-k$ entries zero, which is the block form, and invertibility is exactly $A,D$ invertible. $\square$

The subgroups $P_W$ are the **maximal parabolics** of $\operatorname{GL}(V)$; they are conjugate as $W$ varies over $\operatorname{Gr}_k(V)$, and their conjugacy classes are the conjugacy classes of parabolic subgroups. A maximal flag

$$
0=V_0 \subset V_1 \subset \cdots \subset V_n=V, \qquad \dim V_i=i,
$$

has stabiliser the group $B$ of invertible upper triangular matrices in a basis adapted to the flag, the **Borel subgroup**. The set of all maximal flags is the **flag variety**, on which $\operatorname{GL}(V)$ acts transitively with stabiliser $B$.

### The Bruhat Decomposition

The $B$-orbits on the flag variety are indexed by the symmetric group and give the classical double-coset decomposition.

**Theorem (Bruhat).** Let $B$ be the upper triangular subgroup of $\operatorname{GL}_n(F)$ and let $W=S_n$, represented by the permutation matrices. Then

$$
\operatorname{GL}_n(F)=\bigsqcup_{w \in W} B w B,
$$

a disjoint union of double cosets indexed by the symmetric group. The double coset of the longest element $w_0$ is open and dense, and for every $w$ the closure of $BwB$ is the union of the $BvB$ with $v \le w$ in the Bruhat order.

This is quoted as standard; it is one of the two structural decompositions of the general linear group, the other being Gaussian elimination. A matrix $M$ lies in $BwB$ exactly when its rank matrix is that of $w$:

$$
\operatorname{rk}M[i..n,1..j]=\#\{k \le j:w(k) \ge i\}, \qquad 1 \le i,j \le n .
$$

For $w=w_0$ the right-hand side is $\min(j,n+1-i)$, so the big cell $Bw_0B$ is the set of matrices whose bottom-left corner minors $\det M[n-k+1..n,1..k]$ are all nonzero. The element $w_0$ itself lies in this cell, while its leading principal minors of size less than $n$ vanish, so the big cell is not described by the leading principal minors; those describe instead the open cell $B_-B$ of the opposite Borel subgroup $B_-$ of lower triangular matrices, which is the set of matrices on which Gaussian elimination without row interchanges succeeds. The decomposition shows that the group is controlled by its Borel subgroup and its Weyl group $W$, and it generalises to every reductive group.

## Classical Groups as Stabilisers of Forms

The linear structure alone gives $\operatorname{GL}(V)$; imposing one more piece of structure cuts the group down to a subgroup preserving it. Three cases are standard.

**Definition.** Let $g$ be a nondegenerate bilinear form on $V$ and let $q$ be a nondegenerate quadratic form with polar form $g$. The **orthogonal group** is

$$
O(V,q)=\{T \in \operatorname{GL}(V) : q(Tv)=q(v) \text{ for all } v \in V\},
$$

equivalently the maps preserving the polar form, $g(Tu,Tv)=g(u,v)$ for all $u,v$.

**Definition.** Let $\omega$ be a nondegenerate alternating bilinear form on $V$, which requires $\dim_F V$ even. The **symplectic group** is

$$
\operatorname{Sp}(V,\omega)=\{T \in \operatorname{GL}(V) : \omega(Tu,Tv)=\omega(u,v) \text{ for all } u,v \in V\}.
$$

**Definition.** Let $h$ be a nondegenerate sesquilinear form on a vector space over a field with an involution, Hermitian in the complex case. The **unitary group** is

$$
U(V,h)=\{T \in \operatorname{GL}(V) : h(Tu,Tv)=h(u,v) \text{ for all } u,v \in V\}.
$$

Each set is a subgroup, because each is defined by the preservation of a form and the composition of two form-preserving maps preserves the form. The determinants are constrained: for a nondegenerate quadratic form over a field of characteristic not $2$, every $T \in O(V,q)$ has $\det T=\pm1$, and the subgroup with $\det T=1$ is $SO(V,q)$, of index at most $2$ in $O(V,q)$; every symplectic map has $\det T=1$, so $\operatorname{Sp}(V,\omega)\subseteq\operatorname{SL}(V)$; and every unitary map has $\det T$ of norm $1$ under the involution, in the complex case $|\det T|=1$. The determinant-one subgroups $SO(V,q)$, $SU(V,h)$ and $\operatorname{Sp}(V,\omega)$ are the classical groups.

**Examples.** Over $\mathbb{R}$ with the standard positive definite form, $O(n)$ is the group of rotations and reflections and $SO(n)$ the rotations; these are the compact classical groups, and their structure depends on the signature of the form, a split form giving the non-compact groups $O(p,q)$. Over $\mathbb{C}$ the orthogonal and symplectic groups are the isometry groups of the corresponding complex forms. Over $\mathbb{F}_q$ the same definitions give the finite classical groups, whose orders are computed by the same counting as for $\operatorname{GL}_n(\mathbb{F}_q)$ and are used in the applications article on vector spaces over finite fields.

**Remark.** The groups above are exactly the stabilisers of the forms: an element of $\operatorname{GL}(V)$ lies in $O(V,q)$ precisely when it preserves $q$, and the definition of a classical group is a definition by a preservation condition. This is the sense in which the classical groups are the subgroups of the general linear group that respect additional geometrical structure; the general linear group itself is the case of no additional structure.

## Generation and Structure

**Theorem.** Over a field, $\operatorname{GL}_n(F)$ is generated by the elementary matrices $E_{ij}(\lambda)=I+\lambda e_{ij}$, where $e_{ij}$ is the matrix unit with a $1$ in position $(i,j)$ and zeros elsewhere, $i \neq j$, together with the invertible diagonal matrices.

*Proof.* This is Gaussian elimination read backwards: every invertible matrix can be reduced to the identity by row operations, so it is a product of elementary matrices and one diagonal matrix; the elementary row operations are left multiplication by the matrices $E_{ij}(\lambda)$, transposition of two rows, and scaling of a row. A transposition matrix is a product of elementary matrices and a diagonal sign change over a field, and scaling is diagonal. $\square$

**Theorem.** For $n \ge 2$ and $F$ a field, $\operatorname{SL}_n(F)$ is generated by the elementary matrices $E_{ij}(\lambda)$.

This is the generation statement that makes the special linear group computable; it is not covered here of the category, together with the exceptional cases $\operatorname{SL}_2(\mathbb{F}_2)$ and $\operatorname{SL}_2(\mathbb{F}_3)$, which are generated by elementary matrices all the same but are not perfect: their abelianisations have order $2$ and $3$ respectively. The elementary matrices are transvections, and their generation of $\operatorname{SL}(V)$ is the algebraic content of Gaussian elimination.

**Remark (conjugacy classes).** Two elements of $\operatorname{GL}(V)$ are conjugate exactly when they have the same rational canonical form; over an algebraically closed field this is exactly the same Jordan type, and over $\mathbb{R}$ it is the same real Jordan type. The classification of conjugacy classes of $\operatorname{GL}(V)$ is thus the classification of linear operators up to similarity, and it is the content of the applications article on the Jordan form. The class functions of $\operatorname{GL}(V)$ — functions constant on conjugacy classes — are the functions of the similarity class, hence over an algebraically closed field the functions of the Jordan type; among them the polynomial class functions are exactly the symmetric polynomials in the eigenvalues, of which the trace and the determinant are the first two.

## Summary

The invertible linear maps of a finite-dimensional vector space $V$ over a field $F$ form the group $\operatorname{GL}(V)$ under composition, isomorphic to $\operatorname{GL}_n(F)$ once a basis is fixed, with the isomorphism depending on the basis through conjugation by the change-of-basis matrix. Its centre consists of the scalar maps $\lambda\operatorname{id}_V$ with $\lambda \neq 0$, and the determinant is a surjective homomorphism $\det:\operatorname{GL}(V)\to F^{\times}$ whose kernel is the special linear group $\operatorname{SL}(V)$, a normal subgroup with $\operatorname{GL}(V)/\operatorname{SL}(V)\cong F^{\times}$.

The action of $\operatorname{GL}(V)$ on the projective space of lines has kernel the centre, so it factors through the faithful, transitive action of $\operatorname{PGL}(V)=\operatorname{GL}(V)/F^{\times}$; the projective special linear group is $\operatorname{PSL}(V)=\operatorname{SL}(V)/\mu_n$, with $\mu_n$ the $n$-th roots of unity, and the two coincide over an algebraically closed field. For dimension at least three, the fundamental theorem of projective geometry identifies $\operatorname{PGL}(V)$ with the whole automorphism group of the projective geometry modulo field automorphisms.

$\operatorname{GL}(V)$ acts transitively on the Grassmannian $\operatorname{Gr}_k(V)$ of $k$-subspaces, the stabiliser of a subspace being the parabolic subgroup of block upper triangular matrices, and the stabiliser of a maximal flag is the Borel subgroup of upper triangular matrices; the Bruhat decomposition writes the group as a disjoint union of the double cosets $BwB$ over the symmetric group. The subgroups of $\operatorname{GL}(V)$ that preserve a nondegenerate form — orthogonal, symplectic and unitary groups, together with their determinant-one subgroups — are the classical groups, each defined as the stabiliser of the form. Over a field the group is generated by elementary matrices and diagonal matrices, and the special linear group by the elementary matrices alone; its conjugacy classes are the similarity classes of operators.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | a field |
| $V$ | $F$-vector space of dimension $n \ge 1$ |
| $\operatorname{GL}(V)=\operatorname{Aut}_F(V)$ | general linear group of invertible linear maps |
| $\operatorname{GL}_n(F)$ | group of invertible $n \times n$ matrices over $F$ |
| $\operatorname{SL}(V)=\ker\det$ | special linear group |
| $Z(\operatorname{GL}(V)) \cong F^{\times}$ | centre: scalar maps $\lambda\operatorname{id}_V$ |
| $\det:\operatorname{GL}(V)\to F^{\times}$ | determinant homomorphism |
| $\mu_n$ | the $n$-th roots of unity in $F^{\times}$ |
| $\mathbb{P}(V)$ | projective space of lines in $V$ |
| $\operatorname{PGL}(V)=\operatorname{GL}(V)/F^{\times}$ | projective general linear group |
| $\operatorname{PSL}(V)=\operatorname{SL}(V)/\mu_n$ | projective special linear group |
| $\operatorname{Gr}_k(V)$ | Grassmannian of $k$-dimensional subspaces |
| $P_W$ | stabiliser of $W$; a parabolic subgroup |
| $B$ | Borel subgroup of upper triangular matrices |
| $B_-$ | opposite Borel subgroup of lower triangular matrices |
| $S_n=W$ | symmetric group, the Weyl group of $\operatorname{GL}_n$ |
| $w_0$ | longest element of $W$, indexing the big Bruhat cell |
| $E_{ij}(\lambda)=I+\lambda e_{ij}$ | elementary matrix |
| $e_{ij}$ | matrix unit, $1$ in position $(i,j)$ and zeros elsewhere |
| $O(V,q)$, $SO(V,q)$ | orthogonal group of a quadratic form, and its determinant-one subgroup |
| $\operatorname{Sp}(V,\omega)$ | symplectic group of an alternating form |
| $U(V,h)$, $SU(V,h)$ | unitary group of a sesquilinear form |
| $\mathbb{F}_q$ | finite field with $q$ elements |



## Further Reading

- Michael Artin, *Algebra* (Pearson, 2nd ed. 2011), for group actions and the classical groups.
- Armand Borel, *Linear Algebraic Groups* (Springer, 2nd ed. 1991), for parabolics, Borels and the Bruhat decomposition.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the general linear group and its matrix realisation.
- Roger W. Carter, *Finite Groups of Lie Type* (Wiley, 1985), for the finite classical groups and their orders.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 3rd ed. 1971), for the classical groups and the fundamental theorem of projective geometry.
- Larry C. Grove, *Classical Groups and Geometric Algebra* (American Mathematical Society, 2002), for a uniform treatment of the classical groups.
- James E. Humphreys, *Linear Algebraic Groups* (Springer, 1975), for the structure theory of the general linear group as an algebraic group.
- Derek J. S. Robinson, *A Course in the Theory of Groups* (Springer, 2nd ed. 1996), for the group-theoretic background.
