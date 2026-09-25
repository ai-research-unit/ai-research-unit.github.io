
# __Multilinear Spaces__

## Introduction

Linear algebra studies maps that are additive and homogeneous in one argument. Many constructions of the subject, however, produce maps of several arguments — the product of two scalars, the evaluation of a family of functionals, the determinant as a function of the columns of a matrix — and these are additive in each argument separately rather than in a single variable. Multilinear algebra is the linear algebra of such maps. Its central object is the tensor product of several modules, a single module that linearises a map of several arguments and thereby converts a problem about several modules into a problem about one.

The construction generalises the balanced product of two modules, developed in the companion article of this category on the balanced product, and it is the language in which the tensor, symmetric and exterior algebras of Part I are phrased. This article develops the multilinear maps, the universal property that defines the tensor product of any finite family, the functoriality and associativity of the construction, the action of the symmetric group on the tensor powers, the symmetric and alternating multilinear maps together with the universal objects that represent them, and the contraction pairing between a module and its dual.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$, and $M$, $N$, $P$, $M_i$ are left $R$-modules; the tensor product over $R$ is written $\otimes_R$, or $\otimes$ when the ring is clear. The article assumes the results of the companion articles *Vector Spaces*, *Direct Sums, Free Modules and Rank* andand it uses the exactness language of *Exact Sequences*. It deliberately contains no topology and no form: the tensor product constructed here is a purely algebraic universal object, and every statement that would need a distance, a norm or a bilinear or quadratic form on a single module is deferred to Part II. The tensor, symmetric and exterior algebras themselves are not built here — they are algebras, and they belong to the categories *Symmetric Linear Algebras* and *Anti-symmetric Linear Algebras* — but their relation to the multilinear maps is recorded, since that relation is the reason the tensor product is the right object.

## Multilinear Maps

### Maps of Several Arguments

The basic notion is that of a map that is $R$-linear in each argument separately.

**Definition.** Let $M_1,\dots,M_n$ and $P$ be $R$-modules. A map

$$
f : M_1 \times \cdots \times M_n \longrightarrow P
$$

is **$R$-multilinear** if it is additive in each argument and commutes with scalars in each argument: for every $i$ and all $x,y \in M_i$, all $m_j \in M_j$ with $j \neq i$, and all $r \in R$,

$$
f(\dots,x+y,\dots)=f(\dots,x,\dots)+f(\dots,y,\dots), \qquad f(\dots,rx,\dots)=r\,f(\dots,x,\dots).
$$

The set of $R$-multilinear maps is written $\operatorname{Mult}_R(M_1,\dots,M_n;P)$; it is an $R$-module under pointwise addition and scalar multiplication. For $n=1$ the multilinear maps are exactly the $R$-linear maps, and for $n=0$ the multilinear maps $P$ with no arguments are the elements of $P$.

**Example.** The multiplication map $R \times R \to R$, $(r,s) \mapsto rs$, is $R$-bilinear, hence $R$-multilinear. More generally, for a commutative $R$-algebra $A$ the multiplication $A \times A \to A$ is $R$-multilinear, and this is the structure the tensor product of algebras linearises.

**Example.** The evaluation pairing

$$
\langle \cdot,\cdot\rangle : M^* \times M \longrightarrow R, \qquad \langle f,m\rangle = f(m),
$$

is $R$-bilinear, where $M^*=\operatorname{Hom}_R(M,R)$ is the **dual module**. It is the basic pairing between a module and its dual and is the source of the contraction operations of the last section.

**Remark.** Multilinearity is strictly weaker than linearity of the product: the map $R \times R \to R$, $(r,s) \mapsto r+s$, is additive in each variable but not $R$-multilinear, because $f(r,0)=r \neq 0$ in general. The condition $f(\dots,0,\dots)=0$ for every position is a consequence of multilinearity, obtained by taking $r=0$.

### Multilinear Maps Are Determined by Their Values on a Basis

Over a ring, the behaviour of multilinear maps on free modules is as rigid as in the linear case.

**Proposition.** Let $L_j$ be free with basis $B_j$, and let $f:L_1 \times \cdots \times L_n \to P$ be $R$-multilinear. Then $f$ is determined by its values on the tuples $(b_1,\dots,b_n)$ with $b_j \in B_j$, and these values may be prescribed arbitrarily, subject only to the requirement that $f$ be $R$-multilinear.

*Proof.* Every $x \in L_j$ is a finite sum $\sum_e a_e e$ with $a_e \in R$ and $e \in B_j$. Writing out each argument and using additivity and scalar homogeneity in each position expresses $f(x_1,\dots,x_n)$ as a finite sum of terms $a_{e_1}\cdots a_{e_n} f(e_1,\dots,e_n)$. Hence the values on the tuples of basis elements determine $f$. For the converse, given arbitrary elements $p_{(e_1,\dots,e_n)} \in P$, define $f$ by the same finite sum; the resulting map is additive and homogeneous in each variable because the basis expansions are. $\square$

**Corollary.** If $L_1,\dots,L_n$ are free of ranks $r_1,\dots,r_n$ then $\operatorname{Mult}_R(L_1,\dots,L_n;P)$ is isomorphic to a direct product of $r_1\cdots r_n$ copies of $P$.

The rigidity recorded here is what makes the universal module of the next section computable: it is generated by the elementary products of basis elements, and it is free when the factors are free.

## The Tensor Product of a Family

### The Universal Property

The tensor product turns a multilinear map of several arguments into a linear map of one argument.

**Definition.** A **tensor product** of the family $M_1,\dots,M_n$ over $R$ is an $R$-module

$$
M_1 \otimes_R \cdots \otimes_R M_n
$$

together with an $R$-multilinear map

$$
\otimes : M_1 \times \cdots \times M_n \longrightarrow M_1 \otimes_R \cdots \otimes_R M_n, \qquad (m_1,\dots,m_n) \longmapsto m_1 \otimes \cdots \otimes m_n,
$$

such that for every $R$-module $P$ and every $R$-multilinear $f:M_1 \times \cdots \times M_n \to P$ there is a unique $R$-linear map

$$
\bar f : M_1 \otimes_R \cdots \otimes_R M_n \longrightarrow P \quad \text{with} \quad \bar f(m_1 \otimes \cdots \otimes m_n) = f(m_1,\dots,m_n).
$$

The property says that the map $\otimes$ is the universal multilinear map out of the product, and that the tensor product represents the functor $P \mapsto \operatorname{Mult}_R(M_1,\dots,M_n;P)$.

### Existence and Uniqueness

**Theorem.** For every finite family $M_1,\dots,M_n$ of $R$-modules a tensor product exists and is unique up to a unique isomorphism commuting with the maps $\otimes$.

*Proof.* Let $F$ be the free $R$-module on the set $M_1 \times \cdots \times M_n$, with basis symbols $e_{(m_1,\dots,m_n)}$, and let $K$ be the submodule generated by the elements

$$
e_{(\dots,m_i+m_i',\dots)} - e_{(\dots,m_i,\dots)} - e_{(\dots,m_i',\dots)}, \qquad e_{(\dots,rm_i,\dots)} - r\,e_{(\dots,m_i,\dots)},
$$

for all positions $i$. Put $T=F/K$ and $m_1 \otimes \cdots \otimes m_n = e_{(m_1,\dots,m_n)}+K$. The defining relations say exactly that $\otimes$ is $R$-multilinear, and the elementary tensors generate $T$ because the $e_{(m_1,\dots,m_n)}$ generate $F$. Given a multilinear $f$, the universal property of $F$ gives a linear $\tilde f:F \to P$ with $\tilde f(e_{(m_1,\dots,m_n)})=f(m_1,\dots,m_n)$; each displayed generator of $K$ is killed by the multilinearity of $f$, so $\tilde f$ factors through $K$ and descends to $\bar f$. Uniqueness follows because the elementary tensors generate. For the uniqueness of $T$ up to isomorphism, apply the universal property of $T$ to the universal map of a second tensor product $T'$ and conversely; the two composites fix the elementary tensors and are therefore identities by the uniqueness part of the property. $\square$

The construction is a quotient of a free module, exactly as for the balanced product; the difference is only the number of arguments. In particular the tensor product of a finite family depends only on the modules, not on any choices, and it is functorial: linear maps $u_i:M_i \to N_i$ induce $u_1\otimes\cdots\otimes u_n$ by applying the universal property to the multilinear map $(m_1,\dots,m_n)\mapsto u_1(m_1)\otimes\cdots\otimes u_n(m_n)$.

### Elementary Tensors and Their Relations

**Definition.** An element of $M_1 \otimes_R \cdots \otimes_R M_n$ of the form $m_1 \otimes \cdots \otimes m_n$ is an **elementary tensor**; a general element is a finite sum of elementary tensors.

**Proposition.** For all arguments and all $r \in R$, the elementary tensors satisfy

$$
m_1 \otimes \cdots \otimes (m_i+m_i') \otimes \cdots \otimes m_n = m_1 \otimes \cdots \otimes m_i \otimes \cdots \otimes m_n + m_1 \otimes \cdots \otimes m_i' \otimes \cdots \otimes m_n,
$$

$$
r(m_1 \otimes \cdots \otimes m_n) = m_1 \otimes \cdots \otimes (r m_i) \otimes \cdots \otimes m_n,
$$

and any factor zero makes the elementary tensor zero. Distinct elementary tensors may coincide, and a general element need not be an elementary tensor.

*Proof.* These are the defining relations read in the quotient, together with the computation $0 \otimes x = (0+0)\otimes x = 0\otimes x + 0\otimes x$. The other two claims are visible already for $n=2$: $(r m)\otimes n = m \otimes (r n)$ can identify distinct pairs, and $\sum_i m_i \otimes n_i$ need not factor. $\square$

### The Case of Two Factors and the Relation to the Balanced Product

For $n=2$ the definition reproduces the balanced product of the companion article, and the two universal properties agree: $\operatorname{Hom}_R(M \otimes_R N,P) \cong \operatorname{Bilin}_R(M,N;P)$, with $\operatorname{Bilin}_R$ the balanced maps in the commutative case. For $n=1$ the tensor product is $M_1$ itself, the universal map being the identity, and for $n=0$ it is $R$, the universal map being the inclusion of the empty product and the universal property reducing to $\operatorname{Hom}_R(R,P) \cong P$.

### Associativity and Commutativity

The tensor product is associative and commutative up to natural isomorphism, and these isomorphisms are what let one write $M_1 \otimes \cdots \otimes M_n$ without brackets and without ordering.

**Theorem.** There are natural isomorphisms

$$
(M \otimes_R N) \otimes_R P \;\cong\; M \otimes_R (N \otimes_R P), \qquad M \otimes_R N \;\cong\; N \otimes_R M, \qquad R \otimes_R M \;\cong\; M .
$$

*Proof.* The map $((m,n),p) \mapsto m \otimes (n \otimes p)$ is well defined and trilinear in the appropriate sense and induces the first isomorphism, whose inverse is induced by $(m,(n,p))\mapsto (m \otimes n)\otimes p$. The second is induced by $m \otimes n \mapsto n \otimes m$, with inverse induced by $n \otimes m \mapsto m \otimes n$. The third is $r \otimes m \mapsto rm$, with inverse $m \mapsto 1 \otimes m$. Naturality in each module is immediate from the construction on elementary tensors. $\square$

**Corollary.** For any partition of the indices into consecutive blocks there is a natural isomorphism

$$
M_1 \otimes_R \cdots \otimes_R M_n \;\cong\; \bigl(M_{i_1}\otimes_R\cdots\otimes_R M_{i_p}\bigr) \otimes_R \bigl(M_{j_1}\otimes_R\cdots\otimes_R M_{j_q}\bigr),
$$

so a multilinear map of $n$ arguments corresponds to a bilinear map of two arguments whose entries are tensors. Iterating, every multilinear map may be linearised two arguments at a time.

### Distribution over Direct Sums

**Proposition.** The tensor product distributes over finite direct sums in each variable:

$$
\Bigl(\bigoplus_{\alpha \in A} M_\alpha\Bigr) \otimes_R N \;\cong\; \bigoplus_{\alpha \in A} (M_\alpha \otimes_R N),
$$

for an arbitrary index set $A$, and the same holds in every variable.

*Proof.* The map sending $(\sum_\alpha m_\alpha, n)$ to the family $(m_\alpha \otimes n)_\alpha$ is bilinear and has image in the direct sum, since the sum is finite; it induces a homomorphism out of the tensor product. The inverse is induced by the coproduct of the maps $M_\alpha \otimes N \to (\bigoplus_\alpha M_\alpha)\otimes N$. The two are inverse on elementary tensors. $\square$

**Corollary.** If $L_i$ are free of ranks $r_i$, then $L_1 \otimes_R \cdots \otimes_R L_n$ is free of rank $r_1 \cdots r_n$, with basis the elementary tensors $b_1 \otimes \cdots \otimes b_n$ over bases of the factors.

*Proof.* Induction on $n$ using the case $n=2$ and distribution over direct sums: $R^{r}\otimes_R R^{s} \cong (R^{r})^{\oplus s}\cong R^{rs}$. $\square$

**Example.** Over $R=\mathbb{Z}$ the formula gives $\mathbb{Z}^m \otimes_{\mathbb{Z}} \mathbb{Z}^n \cong \mathbb{Z}^{mn}$, and over a field $F$ it gives $\dim_F(V_1\otimes_F\cdots\otimes_F V_n)=\prod_i \dim_F V_i$. The elementary tensors of bases form a basis of the tensor product, and the coordinate functions of this basis are the entries of the multidimensional array attached to a tensor.

## Functoriality and Exactness of the Tensor Product

### Additivity and Induced Maps

For fixed $M_2,\dots,M_n$ the construction $M_1 \mapsto M_1 \otimes_R M_2 \otimes_R \cdots \otimes_R M_n$ is a functor: an $R$-linear $u:M_1 \to N_1$ induces $u \otimes \operatorname{id}\otimes \cdots \otimes \operatorname{id}$. The functor is additive, $(u+u')\otimes \operatorname{id} = u\otimes \operatorname{id} + u'\otimes \operatorname{id}$, and it preserves identity and composition. It preserves direct sums and cokernels, and it need not preserve kernels, exactly as for two factors.

**Theorem.** The functor $-\otimes_R M_2 \otimes_R \cdots \otimes_R M_n$ is right exact: if $M_1' \to M_1 \to M_1'' \to 0$ is exact, then so is

$$
M_1'\otimes_R M_2\otimes_R\cdots\otimes_R M_n \longrightarrow M_1\otimes_R M_2\otimes_R\cdots\otimes_R M_n \longrightarrow M_1''\otimes_R M_2\otimes_R\cdots\otimes_R M_n \longrightarrow 0 .
$$

*Proof.* For $n=2$ this is the right exactness of the balanced product, proved in the companion article on flatness and exactness. For larger $n$, associate the tensor product so that the varying factor is the first argument of a two-factor product whose second factor is the tensor product of the remaining modules, and apply the case $n=2$. $\square$

The general tensor product therefore inherits the asymmetry of the balanced product: in each variable it is a left adjoint, hence preserves colimits and is right exact. Exactness in the first variable holds when the tensor product of the remaining factors is flat, by the associativity of the construction and the two-factor case; this is the multilinear form of the flatness criterion of the companion article on flatness and exactness.

## The Symmetric Group Action

### Permutation of Factors

When the factors are equal, the symmetric group acts on the tensor power by permuting the positions, and this action is the origin of the symmetric and the antisymmetric tensors.

Let $M$ be an $R$-module and $n \ge 1$. The **$n$-th tensor power** is $M^{\otimes n}=M\otimes_R\cdots\otimes_R M$, with $n$ factors, and $M^{\otimes 0}=R$.

**Proposition.** For each permutation $\sigma \in S_n$ the assignment

$$
\sigma \cdot (m_1 \otimes \cdots \otimes m_n) = m_{\sigma^{-1}(1)} \otimes \cdots \otimes m_{\sigma^{-1}(n)}
$$

extends uniquely to an $R$-linear automorphism of $M^{\otimes n}$, and $\sigma \mapsto (\sigma \cdot)$ is a group homomorphism $S_n \to \operatorname{Aut}_R(M^{\otimes n})$. Thus $M^{\otimes n}$ is a left $R[S_n]$-module.

*Proof.* The map $(m_1,\dots,m_n)\mapsto m_{\sigma^{-1}(1)}\otimes\cdots\otimes m_{\sigma^{-1}(n)}$ is multilinear, so the universal property gives the endomorphism; it has the endomorphism attached to $\sigma^{-1}$ as inverse, hence is an automorphism. The identity $\sigma\tau \cdot x = \sigma\cdot(\tau\cdot x)$ is checked on elementary tensors, where both sides reorder the arguments by $\sigma\tau$. $\square$

### Symmetric and Alternating Tensors

**Definition.** An element $x \in M^{\otimes n}$ is **symmetric** if $\sigma \cdot x = x$ for all $\sigma \in S_n$, and **antisymmetric** if $\sigma \cdot x = \operatorname{sgn}(\sigma)x$ for all $\sigma$, where $\operatorname{sgn}:S_n \to \{\pm 1\}$ is the sign. The symmetric tensors form a submodule $(M^{\otimes n})^{S_n}$, and the antisymmetric tensors form a submodule written $M^{\wedge n}$.

**Example.** For $n=2$ the symmetric tensors satisfy $m \otimes m' = m' \otimes m$ and the antisymmetric tensors satisfy $m \otimes m' = -m' \otimes m$. The pure tensor $m\otimes m$ is symmetric, and it is antisymmetric only when $2\,m\otimes m=0$; the antisymmetric tensors of degree two are exactly the elements of the image of $x\mapsto x-\tau x$, with $\tau$ the transposition, that is the multiples of tensors $m\otimes m'-m'\otimes m$. In the exterior square the same relation reads $m\wedge m'=-m'\wedge m$, and in particular $m\wedge m=0$. For $n=3$ the antisymmetrisation

$$
\sum_{\sigma \in S_3}\operatorname{sgn}(\sigma)\,m_{\sigma(1)}\otimes m_{\sigma(2)}\otimes m_{\sigma(3)}
$$

is a sum of six terms and is antisymmetric; it vanishes whenever two of the $m_i$ coincide. Over a field of characteristic not $2$, or generally when $n!$ is invertible in $R$, replacing the antisymmetrisation by its normalised form $e_-\cdot x$ exhibits the antisymmetric tensors as the image of an idempotent of $R[S_n]$ acting on $M^{\otimes n}$.

In characteristic different from $2$ the symmetric and the antisymmetric tensors are the images of the two central idempotents of $R[S_n]$, the symmetriser

$$
e_+ = \frac{1}{n!}\sum_{\sigma \in S_n}\sigma \qquad \text{and the antisymmetriser} \qquad e_- = \frac{1}{n!}\sum_{\sigma \in S_n}\operatorname{sgn}(\sigma)\,\sigma .
$$

When $R$ is a field of characteristic zero, or more generally a ring in which $n!$ is invertible, these are idempotents and $M^{\otimes n}$ decomposes as the direct sum of the images of $e_+$ and of the other idempotents of the group algebra $R[S_n]$ provided by its irreducible representations. Over a general ring the operators $\sum_\sigma \sigma$ and $\sum_\sigma \operatorname{sgn}(\sigma)\sigma$ still act, but dividing by $n!$ may be impossible, and the symmetric and the antisymmetric parts are then defined as the images of these unnormalised operators. The full decomposition of $M^{\otimes n}$ into its symmetry types belongs to the representation theory of the symmetric group, developed in the companion articles of the *Rings and Fields* category, and is not needed here.

### Symmetric and Alternating Multilinear Maps

**Definition.** A multilinear map $f:M^n \to P$ is **symmetric** if $f(m_{\sigma(1)},\dots,m_{\sigma(n)})=f(m_1,\dots,m_n)$ for every $\sigma$, and **skew-symmetric** if $f(m_{\sigma(1)},\dots,m_{\sigma(n)})=\operatorname{sgn}(\sigma)f(m_1,\dots,m_n)$ for every $\sigma$. It is **alternating** if $f$ vanishes whenever two of its arguments are equal.

**Proposition.** An alternating multilinear map is skew-symmetric; conversely a skew-symmetric map is alternating when $2$ is invertible in $R$. Over a ring in which $2$ is not invertible the two conditions differ, and being alternating is the stronger of the two.

*Proof.* Suppose $f$ is alternating. For fixed arguments $x,y$ in two positions, multilinearity applied to $x+y$ in both positions gives
$$
0=f(\dots,x+y,\dots,x+y,\dots)=f(\dots,x,\dots,x,\dots)+f(\dots,x,\dots,y,\dots)+f(\dots,y,\dots,x,\dots)+f(\dots,y,\dots,y,\dots),
$$
and the two repeated-argument terms vanish while the left side does, so $f(\dots,x,\dots,y,\dots)=-f(\dots,y,\dots,x,\dots)$; a transposition therefore changes the sign, and $f$ is skew-symmetric. Conversely, if $f$ is skew-symmetric and two arguments are equal to $x$, interchanging them changes the sign while leaving $f$ unchanged, so $f=-f$; this gives $f=0$ when $2$ is invertible, and $f$ is alternating. $\square$

The **universal symmetric multilinear map** and the **universal alternating multilinear map** are constructed by factoring the elementary tensors by the relations $m_1\otimes\cdots\otimes m_n = m_{\sigma(1)}\otimes\cdots\otimes m_{\sigma(n)}$ and $m_1\otimes\cdots\otimes m_n=\operatorname{sgn}(\sigma)m_{\sigma(1)}\otimes\cdots\otimes m_{\sigma(n)}$ respectively. The resulting modules are the **symmetric power** $S^nM$ and the **exterior power** $\Lambda^nM$, characterised by

$$
\operatorname{Hom}_R(S^nM,P) \;\cong\; \bigl\{f \in \operatorname{Mult}_R(M^n;P) : f \text{ symmetric}\bigr\},
$$

$$
\operatorname{Hom}_R(\Lambda^nM,P) \;\cong\; \bigl\{f : f \text{ alternating}\bigr\},
$$

and they satisfy $S^1M=\Lambda^1M=M$, $S^0M=\Lambda^0M=R$, and $\Lambda^nM=0$ for $n$ larger than the rank of a free module $M$. Their structure, their bases and their relations are developed in ; here they are introduced only as the universal objects of the two symmetry conditions.

## The Relation to the Tensor, Symmetric and Exterior Algebras

The tensor powers assemble into graded objects by taking direct sums.

**Definition.** The **tensor algebra** on $M$ is

$$
T(M) = \bigoplus_{n \ge 0} M^{\otimes n},
$$

with multiplication $M^{\otimes p}\otimes_R M^{\otimes q}\to M^{\otimes(p+q)}$ induced by the associativity isomorphism, extended bilinearly. It is an associative $R$-algebra with unit $1 \in R=M^{\otimes 0}$, not commutative when $M \neq 0$, and it is generated by $M=M^{\otimes 1}$.

The algebra $T(M)$ is the free associative algebra on the module $M$; it is the universal target of linear maps out of $M$: every $R$-linear $u:M \to A$ into an associative $R$-algebra $A$ with unit factors uniquely through the inclusion $M \hookrightarrow T(M)$ as an algebra homomorphism. The tensor algebra is built here, where this universal property is proved.

**Definition.** The **symmetric algebra** is the quotient $S(M)=\bigoplus_{n\ge0}S^nM$ of $T(M)$ by the two-sided ideal generated by the elements $m\otimes m'-m'\otimes m$, and the **exterior algebra** is the quotient $\Lambda(M)=\bigoplus_{n\ge0}\Lambda^nM$ of $T(M)$ by the ideal generated by the elements $m\otimes m$. The first is commutative, the second is graded-commutative with $m\wedge m'=-m'\wedge m$.

Their structure, their universal properties among commutative and among graded-commutative algebras, and their bases over free modules are the subject of . The role of the present article is to supply what those articles presuppose: the tensor product as the universal recipient of multilinear maps, the symmetric group action that defines the two symmetry conditions, and the fact that $S^nM$ and $\Lambda^nM$ are the universal objects representing symmetric and alternating multilinear maps. In the vocabulary of the corpus, the tensor, symmetric and exterior powers are the degree-$n$ pieces, and the three algebras are their direct sums with the products induced from the tensor algebra.

**Remark.** The determinant of a square matrix is the unique alternating multilinear function of the columns normalised to $1$ on the identity, and it is the reason the exterior power $\Lambda^nR^n$ is free of rank one. That statement uses only alternating multilinear maps, and it is the bridge between the present article and the article of this category on *The Special Linear Group and the Determinant*. No metric, no orientation and no volume is needed: $\Lambda^n$ of a free module of rank $n$ is free of rank one on purely algebraic grounds.

## Contraction and the Dual Module

### The Dual Module

**Definition.** The **dual** of $M$ is $M^*=\operatorname{Hom}_R(M,R)$. It is an $R$-module, and the evaluation pairing $\langle f,m\rangle=f(m)$ is $R$-bilinear. A linear map $u:M \to N$ induces $u^*:N^*\to M^*$ by $u^*(f)=f\circ u$, so that $(-)^*$ is a contravariant functor.

**Proposition.** If $L$ is free with basis $B$ then $L^*$ is free with the dual basis $B^*=\{b^* : b \in B\}$ defined by $b^*(b')=\delta_{bb'}$, where $\delta$ is the Kronecker symbol. For finite free $L$ there is a natural isomorphism $L \cong L^{**}$, given by $x \mapsto (\text{evaluation at } x)$.

*Proof.* A homomorphism out of a free module is determined by its values on $B$, and these may be prescribed arbitrarily; hence $B^*$ is a basis. For finite $B$, the map $x \mapsto \langle\cdot,x\rangle$ has the inverse sending $\xi \in L^{**}$ to $\sum_{b \in B}\xi(b^*)b$. $\square$

For a general module the natural map $M \to M^{**}$ need not be injective or surjective; over a field it is an isomorphism exactly when $M$ is finite-dimensional.

### Contraction

The tensor product of a module with its dual carries a canonical evaluation.

**Proposition.** There is a unique $R$-linear map

$$
c : M^* \otimes_R M \longrightarrow R, \qquad c(f \otimes m) = f(m),
$$

natural in $M$; it is the **contraction** of the module with its dual.

*Proof.* The evaluation pairing is bilinear, so the universal property of the tensor product gives a unique linear $c$ with $c(f\otimes m)=f(m)$; naturality is the identity $c(u^*(f)\otimes m)=c(f\otimes u(m))$, checked on elementary tensors. $\square$

**Corollary (the trace as a contraction).** For a finitely generated projective module $P$ and $\varphi \in \operatorname{End}_R(P)$ the trace of the article on projective and injective modules equals the composite

$$
R \cong P^* \otimes_R P \xrightarrow{\ \operatorname{id}\otimes\varphi\ } P^*\otimes_R P \xrightarrow{\ c\ } R
$$

under the identification $P^*\otimes_R P \cong \operatorname{End}_R(P)$ for finitely generated projective $P$, whose direct-basis form is recorded in that article.

Contraction generalises to arbitrary tensors: from $M^{\otimes p}\otimes (M^*)^{\otimes q}$ one may contract any pair of a tensor slot and a dual slot, and iterating produces all the classical operations of raising and lowering indices. Over a general ring these operations need the dual basis to exist; over a field they are available for every finite-dimensional space, and the tensor algebra of $M\oplus M^*$ with the contraction is the setting of the mixed tensor calculus.

## Base Change and Change of Rings

The tensor product is compatible with extension of scalars, and this compatibility is what makes multilinear algebra behave well under a change of the base ring.

**Theorem.** Let $\varphi:R \to S$ be a homomorphism of commutative rings and let $M_1,\dots,M_n$ be $R$-modules. There is a natural isomorphism of $S$-modules

$$
S \otimes_R (M_1 \otimes_R \cdots \otimes_R M_n) \;\cong\; (S\otimes_R M_1)\otimes_S \cdots \otimes_S (S\otimes_R M_n).
$$

*Proof.* Both sides are universal for $S$-multilinear maps out of the product of the $S$-modules $S\otimes_RM_i$. On the left, an $S$-multilinear map out of the product of the $M_i$ is an $R$-multilinear map, and $S\otimes_R(-)$ is universal for $S$-linear maps out of an $R$-module; on the right, $S$-multilinearity is exactly the universal property of the tensor product over $S$. The two universal properties coincide, and uniqueness of the representing object gives the isomorphism. $\square$

**Corollary.** Base change commutes with the tensor algebra, the symmetric powers and the exterior powers in the sense that $S\otimes_R T(M)\cong T(S\otimes_RM)$, $S\otimes_R S^nM\cong S^n(S\otimes_RM)$ and $S\otimes_R\Lambda^nM\cong\Lambda^n(S\otimes_RM)$.

*Proof.* The first is the theorem applied degree by degree and extended linearly; the second and third follow because base change preserves the quotient defining each, being right exact and carrying the relations $m\otimes m'-m'\otimes m$ and $m\otimes m$ to the corresponding relations. $\square$

**Example (complexification of a tensor product).** For real vector spaces $V_1,\dots,V_n$, the complexification satisfies $(V_1\otimes_{\mathbb{R}}\cdots\otimes_{\mathbb{R}}V_n)_{\mathbb{C}}\cong (V_1)_{\mathbb{C}}\otimes_{\mathbb{C}}\cdots\otimes_{\mathbb{C}}(V_n)_{\mathbb{C}}$, and the dimension over $\mathbb{C}$ is $\prod_i\dim_{\mathbb{R}}V_i$, the same as the real dimension of the original tensor product, in agreement with the rule that complexification preserves dimension. This is the base-change statement of the companion article on extension of scalars, read for several factors.

## Examples and Computations

### The Tensor Product of Cyclic Modules

**Proposition.** Over $R=\mathbb{Z}$ one has

$$
\mathbb{Z}/m\mathbb{Z} \otimes_{\mathbb{Z}} \mathbb{Z}/n\mathbb{Z} \;\cong\; \mathbb{Z}/\gcd(m,n)\mathbb{Z}, \qquad \mathbb{Q}\otimes_{\mathbb{Z}}\mathbb{Z}/n\mathbb{Z}=0 .
$$

*Proof.* Both are the computations of the companion article on the balanced product; the first is the $n=2$ case of the general theory and the second follows because every element of $\mathbb{Z}/n\mathbb{Z}$ is $n$-torsion while multiplication by $n$ is invertible on $\mathbb{Q}$. $\square$

### Polynomial and Multilinear Expressions

**Example.** Let $M=R^d$ be free with basis $e_1,\dots,e_d$. Then $M^{\otimes n}$ is free with basis the $d^n$ elementary tensors $e_{i_1}\otimes\cdots\otimes e_{i_n}$, and an element is a finite family of coefficients $a_{i_1\dots i_n}$ indexed by the $n$-tuples. A multilinear map $f:M^n\to P$ corresponds to the arbitrary family of its values $f(e_{i_1},\dots,e_{i_n})$, so multilinear algebra over a free module is the algebra of arrays of rank $n$ with no symmetry imposed. Imposing symmetry produces the symmetric powers, whose dimension over a field is $\binom{d+n-1}{n}$, and imposing alternation produces the exterior powers, of dimension $\binom{d}{n}$; those dimension counts are proved in the companion articles on symmetric and exterior powers, and they are the reason the determinant is a single scalar rather than a family.

**Example.** For $M=R$ and $P=R$ the multilinear maps $R^n\to R$ are the elements of $R$, and the elementary tensors of $R^{\otimes n}$ all equal $1$. The tensor product $R^{\otimes n}$ is $R$ for every $n$, and the symmetric and exterior powers are $S^nR\cong R$ and $\Lambda^nR=0$ for $n\ge2$. This degenerate case shows that the tensor product does not record the number of arguments beyond the ring element, and it is the reason the interesting algebra of tensors begins with a module of rank at least two.

### A Rank and a Non-Rank

**Proposition.** If $M$ has rank $r$ and $N$ has rank $s$, in the sense of the maximal number of linearly independent elements, then $M\otimes_RN$ has rank at most $rs$; over a field the rank is the product, and over a principal ideal domain the rank of $M\otimes_RN$ is the product of the ranks of the torsion-free parts.

*Proof.* Choose maximal independent families $x_1,\dots,x_r$ in $M$ and $y_1,\dots,y_s$ in $N$; the $rs$ elementary tensors $x_i\otimes y_j$ span a free submodule of rank $rs$, and every elementary tensor $m\otimes n$ lies in the span of the $x_i\otimes y_j$ together with torsion corrections that may be killed. Over a field the spanning family is independent by the basis theorem; over a principal ideal domain the rank of a tensor product of torsion-free modules is the product of the ranks, and torsion is annihilated by the tensor product against a torsion-free module only up to the appropriate divisibility, giving the stated bound. $\square$

The example $M=N=\mathbb{Z}/2\mathbb{Z}$ shows that the bound can be far from attained: both factors have rank zero, and the tensor product is $\mathbb{Z}/2\mathbb{Z}$, of rank zero but nonzero.

## Summary

Multilinear algebra linearises maps of several arguments. An $R$-multilinear map $f:M_1\times\cdots\times M_n\to P$ is additive and scalar-homogeneous in each argument separately, and the tensor product $M_1\otimes_R\cdots\otimes_R M_n$, constructed as the quotient of the free module on the product by the multilinearity relations, is the universal recipient of such maps: there is a natural isomorphism $\operatorname{Hom}_R(M_1\otimes_R\cdots\otimes_R M_n,P)\cong\operatorname{Mult}_R(M_1,\dots,M_n;P)$. The construction is associative, commutative and unital up to natural isomorphism, so the family may be written without brackets, and it distributes over direct sums, so the tensor product of free modules is free with rank the product of the ranks.

For a single module the symmetric group acts on the tensor power $M^{\otimes n}$ by permuting the factors, and the symmetric and the antisymmetric tensors are its fixed and sign-isotypic parts. Symmetric and alternating multilinear maps have universal targets $S^nM$ and $\Lambda^nM$, the symmetric and exterior powers, whose structure belongs to ; the direct sums $T(M)$, $S(M)$ and $\Lambda(M)$ are the tensor, symmetric and exterior algebras, built in the *Linear Algebras* category. The dual module $M^*=\operatorname{Hom}_R(M,R)$ supports the contraction $M^*\otimes_RM\to R$, from which the trace of an endomorphism of a finitely generated projective module is recovered, and base change along $R\to S$ commutes with the tensor product of a family and with the tensor, symmetric and exterior algebras.

Throughout, no distance, norm or form enters. Every statement is a universal property of a constructed module or a computation with elementary tensors, and every enrichment that would need a metric on a module or a form on a single space is deferred to Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | commutative ring with identity $1 \neq 0$ |
| $M$, $N$, $P$, $M_i$ | left $R$-modules |
| $\operatorname{Mult}_R(M_1,\dots,M_n;P)$ | $R$-multilinear maps |
| $\operatorname{Bilin}_R(M,N;P)$ | $R$-bilinear maps |
| $M_1\otimes_R\cdots\otimes_R M_n$ | tensor product of a finite family |
| $m_1\otimes\cdots\otimes m_n$ | elementary tensor |
| $M^{\otimes n}$ | $n$-th tensor power, $M^{\otimes 0}=R$ |
| $S_n$ | symmetric group on $n$ letters |
| $\operatorname{sgn}$ | the sign homomorphism $S_n\to\{\pm1\}$ |
| $M^{\wedge n}$ | the submodule of antisymmetric tensors in $M^{\otimes n}$ |
| $S^nM$, $\Lambda^nM$ | symmetric and exterior powers |
| $T(M)$, $S(M)$, $\Lambda(M)$ | tensor, symmetric and exterior algebras |
| $M^*=\operatorname{Hom}_R(M,R)$ | dual module |
| $\langle f,m\rangle=f(m)$ | evaluation pairing |
| $c:M^*\otimes_RM\to R$ | contraction |
| $\delta_{bb'}$ | Kronecker symbol |
| $\bigoplus$, $\bigotimes$ | direct sum, tensor product of a family |



## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for multilinear maps, tensor products and the symmetric and exterior algebras.
- Henri Cartan and Samuel Eilenberg, *Homological Algebra* (Princeton University Press, 1956), for the tensor product as a universal object and its exactness properties.
- Werner Greub, *Multilinear Algebra*, 2nd ed. (Springer, 1978), for the systematic theory of multilinear maps and the tensor algebra.
- Thomas W. Hungerford, *Algebra* (Springer, 1974), for the tensor product of modules and the trace form.
- Nathan Jacobson, *Basic Algebra II*, 2nd ed. (Dover, 2009), for the tensor, symmetric and exterior algebras and their universal properties.
- Serge Lang, *Algebra*, 3rd ed. (Springer, 2002), for multilinear algebra in the generality of modules over a commutative ring.
- Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed. (Springer, 1998), for the universal-property formulation of the tensor product.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for the tensor product and its derived functors.
