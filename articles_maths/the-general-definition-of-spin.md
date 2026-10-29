# __The General Definition of Spin__

## Introduction

**Spin is the highest weight of a copy of $\mathfrak{sl}_2$.** That is the representation theory of *Representations of Lie Algebras*, applied to the smallest semisimple algebra: a triple $(S,U,V)$ with

$$
[S,U]=U,\qquad [S,V]=-V,\qquad [U,V]=2S
$$

spans a copy of $\mathfrak{sl}_2$, and on an irreducible finite-dimensional module the eigenvalues of $S$ are $j,j-1,\dots,-j$. The largest, $j$, is the spin.

**The one step of this article is where the triple comes from.** It need not be given as Lie data. In an associative algebra the product splits into a symmetric and an antisymmetric part,

$$
UV=\tfrac12\{U,V\}+\tfrac12[U,V],
$$

and the antisymmetric part $\tfrac12[U,V]$ is an element of the same algebra. A pair $(U,V)$ whose antisymmetric part $S=\tfrac12[U,V]$ is nonzero and satisfies $[S,U]=U$, $[S,V]=-V$ therefore produces a triple. The definition needs an algebra and two elements; the copy of $\mathfrak{sl}_2$ is produced by them, not chosen in advance. This is why the biquaternion carries spin; in a commutative algebra the antisymmetric part vanishes and no pair exists.

**The rest is the standard representation theory of that triple.** Once the triple exists, the carrier is a module, the weights are the eigenvalues of $S$, and the spin is their maximum. The article proves the structure theorem once, computes the elementary lists for the matrix algebras, the commutative algebras and the products, and separates the spin from the labels beside it. The lists belong to the pair, not to the algebra alone: $M_n(\mathbb{C})$ carries a principal pair and a balanced Peirce pair, and they give different spins.

The base field is $\mathbb{R}$ or $\mathbb{C}$, of characteristic zero, and a real algebra is complexified when a pair is needed; the indexing is $1$-based, and no form and no Clifford algebra are used. The $\mathfrak{sl}_2$ modules, the enveloping algebra and the Casimir element are those of *Representations of Lie Algebras* and *The Casimir Operator*, cited rather than reproved. The other articles write the Cartan as $H=2S$, with weights $2j,2j-2,\dots,-2j$; this article writes $S$, so that the spin is a weight and not half a weight.

## The Spin Structure

### The Product Split

**The product of two elements has two halves.** In an associative algebra over $k$,

$$
UV=\tfrac12\{U,V\}+\tfrac12[U,V],
$$

with $\{U,V\}=UV+VU$ and $[U,V]=UV-VU$. The first term is symmetric in $U,V$; the second is antisymmetric. The symmetric term is the Jordan product, the antisymmetric one is the Lie product. A spin structure is a pair whose antisymmetric part is nonzero and acts on the pair with eigenvalues $+1$ and $-1$.

**Definition (spin pair).** Let $A$ be a $k$-algebra with $k$ of characteristic zero. A **spin pair** in $A$ is a pair $(U,V)\in A^2$ with $[U,V]\neq0$ and

$$
[[U,V],U]=2U,\qquad [[U,V],V]=-2V .
$$

**Definition (spin element).** The **spin element** of the pair is the antisymmetric part of the product,

$$
S=\tfrac12(UV-VU)=\tfrac12[U,V].
$$

**Proposition (the spin triple).** For a spin pair, $[S,U]=U$, $[S,V]=-V$ and $[U,V]=2S$. The element $S$ is nonzero, and the span of $S,U,V$ is a copy of $\mathfrak{sl}_2(k)$. Conversely, a triple $(S,U,V)$ with these three relations and $S\neq0$ is the triple of a spin pair.

*Proof.* $[S,U]=\tfrac12[[U,V],U]=U$ and $[S,V]=\tfrac12[[U,V],V]=-V$ by the two conditions, and $[U,V]=2S$ by the definition of $S$. If $S=0$, then $[U,V]=0$, contradicting $[U,V]\neq0$. The three relations are the standard relations of $\mathfrak{sl}_2$. For the converse, the pair $(U,V)$ of a triple has $[U,V]=2S\neq0$, $[[U,V],U]=[2S,U]=2U$ and $[[U,V],V]=[2S,V]=-2V$.

A **spin algebra** is a pair $(A,\mathfrak{s})$ of an algebra and a spin pair in it.

**Remark (the pair is the data).** The spin element is derived, not assumed: it is the antisymmetric part of the product, and the condition $[U,V]\neq0$ is the statement that $U$ and $V$ do not commute. The zero pair is the only pair that the condition excludes, since $[U,V]=0$ forces $U=V=0$ through the two double-commutator relations; it is the zero representation of $\mathfrak{sl}_2$, not a spin structure. The span of $S,U,V$ is closed under the bracket and is $\mathfrak{sl}_2(k)$ with the standard basis $h=2S$, $e=U$, $f=V$, so the representation theory of $\mathfrak{sl}_2$ applies to every carrier.

### The Carrier

**Definition (carrier of the triple).** Let $(A,\mathfrak{s})$ be a spin algebra, with $\mathfrak{s}$ the spin pair. A **carrier of the triple** is a nonzero finite-dimensional module $W$ for the Lie algebra spanned by $S,U,V$, a copy of $\mathfrak{sl}_2$. The triple acts by $\rho(S),\rho(U),\rho(V)\in\operatorname{End}_k(W)$.

**Definition (carrier of the algebra).** A carrier of the triple is a **carrier of the algebra** when $A$ also acts on it, in one of two ways:

- the **associative action** $L_a(w)=aw$, which makes $W$ a left $A$-module;
- the **adjoint action** $\operatorname{ad}_a(w)=aw-wa$ on $A$ and on its $\operatorname{ad}(A)$-stable subspaces, which makes $W$ a module for the Lie algebra $A^-$, the algebra $A$ with the commutator, not for the associative algebra $A$.

A carrier of the algebra is **elementary** if it is nonzero and has no nonzero proper invariant subspace for the chosen algebra action.

For a real algebra with a pair in $A_{\mathbb{C}}$, a carrier of the triple is a finite-dimensional module for the complexified triple; a real carrier is complexified to one. The two actions are the two actions of the corpus: left multiplication and the commutator.

**Definition (weights, weight string, spin).** The **weights** of a carrier of the triple are the eigenvalues of $\rho(S)$, counted with multiplicity. The **weight string** is the multiset of weights. The **highest weight** $\lambda_{\max}$ is the largest weight. The **spin** is the largest weight,

$$
\boxed{\;j=\lambda_{\max}(\rho(S))=\max\operatorname{spec}\rho(S)\;}
$$

and the carrier is a **spin-$j$ carrier**. The element $S$ is the **spin operator**.

**Remark (a vector has a weight, not a spin).** A nonzero $w\in W$ with $\rho(S)w=mw$ has weight $m$; it is a state of magnetic quantum number $m$ in a carrier of spin $j\ge\lvert m\rvert$. The spin $j$ is the highest weight of the whole carrier, not the weight of one vector. The vector alone does not determine $j$; the carrier does.

**Remark (the trace of $S$ is zero).** Since $S=\tfrac12[U,V]$, $\operatorname{tr}\rho(S)=\tfrac12\operatorname{tr}[\rho(U),\rho(V)]=0$. The weights of a carrier sum to zero. The trace of $S$ is therefore not the spin, and it cannot distinguish carriers.

**Remark (the doubled notation).** The other articles of the corpus write the Cartan as

$$
H=2S=[U,V],
$$

so that $[H,U]=2U$ and the weights of $H$ are the integers $2j,2j-2,\dots,-2j$. This article writes $S$ and the weights $j,j-1,\dots,-j$. The two are the same triple; the factor $2$ is the antisymmetrisation of the product, moved from the definition of $S$ into the relation $[H,U]=2U$. The table of the cases quotes the spin $j$, which is the same number in both notations.

**Remark (real algebras).** A real algebra need not contain a real spin pair. The quaternions contain $\mathfrak{su}(2)$, not $\mathfrak{sl}_2(\mathbb{R})$: for $S\in\operatorname{Im}\mathbb{H}$ the operator $\operatorname{ad}_S$ has eigenvalues $0,\pm2i\lvert S\rvert$ over $\mathbb{C}$ and no nonzero real eigenvalue, so $[S,U]=U$ has no nonzero real solution. The pair of $\mathbb{H}$ lives in the complexification $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}=\mathbb{B}$. For a real algebra $A$, a **spin structure** is a spin pair in $A_{\mathbb{C}}=A\otimes_{\mathbb{R}}\mathbb{C}$; a real carrier is complexified with the algebra. The split quaternions $\mathbb{H}_{\mathrm{s}}\cong M_2(\mathbb{R})$ do contain a real pair, and no complexification is needed for the pair itself.

**Remark (normalisation).** The pair is determined up to $U\mapsto\mu U$, $V\mapsto\mu^{-1}V$, which preserves $[U,V]$ and hence $S$, and up to the Weyl symmetry $(S,U,V)\mapsto(-S,V,U)$, which exchanges the two ladder elements and reverses the grading. The spin is unchanged by both.

### What the Definition Does Not Use

- No form, no norm and no Hermitian structure: the pair and the module suffice.
- No Clifford algebra: the bracket is the algebra commutator.
- No choice of basis: the weights are eigenvalues.
- No semisimplicity of $A$: the triple is a copy of $\mathfrak{sl}_2$, whose own representation theory is semisimple; $A$ need not be.
- No topology and no completion: the algebra and the carriers are finite-dimensional over $k$.

## The Structure Theorem

### The Irreducibles

**Theorem (the carriers of a spin triple).** Let $k$ be algebraically closed of characteristic zero. Every finite-dimensional module of $\mathfrak{sl}_2(k)$ is a direct sum of irreducibles $W_j$, $j\in\tfrac12\mathbb{Z}_{\ge0}$, where $\dim W_j=2j+1$ and the weights of $W_j$ are

$$
j,\ j-1,\ \dots,\ -j .
$$

The highest weight is $j$, and the spin of $W_j$ is $j$. A carrier $W$ therefore has a well-defined spin, the largest $j$ of its summands, and the multiset of the highest weights of its summands is a complete invariant of $W$ as a module of the triple.

*Proof.* This is the standard representation theory of $\mathfrak{sl}_2$ over an algebraically closed field of characteristic zero (the real case is read after complexification to $\mathbb{C}$): a highest-weight vector generates an irreducible module of dimension $2j+1$, the ladder moves between weight spaces in steps of one, and Weyl's theorem makes every finite-dimensional module a direct sum of these. The triple is a copy of $\mathfrak{sl}_2$ by the previous remark.

**Corollary (the spin is the highest weight).** On a carrier $W$, the eigenvalues of $\rho(S)$ are the weights; the largest is $j$.

**Corollary (integrality).** The spin is a nonnegative integer or half-integer, $j\in\tfrac12\mathbb{Z}_{\ge0}$; equivalently $2j\in\mathbb{Z}_{\ge0}$.

**Corollary (the weight string is the union).** If $W=\bigoplus_\alpha W_{j_\alpha}$, the weights of $W$ are the union, with multiplicity, of the strings $j_\alpha,j_\alpha-1,\dots,-j_\alpha$. The highest weight is $\max_\alpha j_\alpha$.

**Corollary (the multiplicity formula).** Let $\mu(m)$ be the multiplicity of the weight $m$. Each $W_j$ contributes one to $\mu(m)$ for every weight $m$ of $W_j$, so

$$
\mu(m)=\sum_{j\ge\lvert m\rvert,\ j-m\in\mathbb{Z}}m_j
$$

and therefore

$$
m_j=\mu(j)-\mu(j+1),
$$

where $m_j$ is the multiplicity of $W_j$ in the carrier.

### The Casimir

**Proposition (the Casimir).** The element

$$
C=S^2+\tfrac12(UV+VU)=S^2+\tfrac12\{U,V\}
$$

commutes with $S,U,V$ and acts on $W_j$ as the scalar $j(j+1)$.

*Proof.* The commutators $[C,U]$ and $[C,V]$ vanish by the relations, and $[C,S]=0$ because $[UV+VU,S]=0$; hence $C$ commutes with the triple. On a highest-weight vector $v$ of $W_j$, $\rho(S)v=jv$, $\rho(U)v=0$ and $\rho(V)\rho(U)v=0$; the relation $[U,V]=2S$ gives $\rho(U)\rho(V)v=2jv$. Hence $Cv=(j^2+j)v=j(j+1)v$. Since $C$ is central in the span of the triple and $W_j$ is irreducible, it acts by this scalar on all of $W_j$.

**Remark (the Casimir is not the spin).** The Casimir acts by $j(j+1)$, a function of the spin; it is not the spin. On a carrier with summands of different spins it is not scalar, and its largest eigenvalue gives $j$ by solving $j(j+1)=\lambda$.

### The Period and the Half-Angle

**Proposition (the period).** On $W_j$, the operator $\exp(-2\pi iS)$ is the scalar $(-1)^{2j}$: $+1$ for integer $j$ and $-1$ for half-integer $j$. For $j>0$, the rotor $T\mapsto\exp(-iTS)$ has period $2\pi$ on an integer-spin carrier and $4\pi$ on a half-integer one; the spin-$0$ carrier carries the trivial rotor.

*Proof.* The eigenvalues of $S$ on $W_j$ are $j,j-1,\dots,-j$; each differs from $j$ by an integer, so $e^{-2\pi i m}=e^{-2\pi i j}=(-1)^{2j}$ for every weight $m$. The period is the smallest $T>0$ with $e^{-iTS}=1$; it is $2\pi$ when $2j$ is even and $4\pi$ when $2j$ is odd.

**Remark (the half-angle).** The half-angle is not the spin. The rotor $\exp(-i\theta S)$ has exponent $\theta$ times the spin operator and acts on a weight-$m$ state by the phase $e^{-i\theta m}$. When the spin operator is written as $\tfrac12 i\vec u$, the angle in the rotor is $\theta/2$; that half is the coordinate of the weight, not the highest weight. Two carriers with the same polar angle and different $j$ have different spins. The half-angle is why a spinor rotation has period $4\pi$; it is not a normalisation of the spin.

### The Bound

**Proposition (the bound).** On a carrier of dimension $N$, the spin satisfies $2j+1\le N$, so $j\le(N-1)/2$. On the regular module of an algebra of dimension $d$, $j\le(d-1)/2$.

*Proof.* $W_j$ has dimension $2j+1$ and is a subspace of the carrier; hence $2j+1\le N$. The regular module has dimension $d$.

**Remark (higher spin).** The bound applies to the carriers of the triple. The tensor product of two carriers is a carrier of the triple, with the diagonal action, but not of the algebra unless the algebra has a coproduct. The spins $3/2,2,\dots$ therefore occur on the triple's tensor products while the algebra's own elementary list stays bounded. This is the distinction developed in *Higher Spin from Tensor Products*.

## The Elementary Carriers

### The List

**Definition (elementary carrier and spin list).** Let $(A,\mathfrak{s})$ be a spin algebra. An **elementary carrier** is a nonzero irreducible carrier of the algebra under one of the two actions: a simple left $A$-module for the associative action, or an irreducible $\operatorname{ad}(A)$-stable subspace of $A$ for the adjoint action. The **spin content** of a carrier is the multiset of the spins of its simple summands as a module of the triple. The **spin** of the carrier is the largest element of its content. The **elementary spin list** $\Sigma(A,\mathfrak{s})$ is the set of the spins of the elementary carriers.

**Proposition (where the list comes from).** The associative elementary carriers are the simple left $A$-modules; when $A$ is semisimple, they are the simple summands of the left regular module $A$. The adjoint elementary carriers are the irreducible modules for $A^-$ inside the adjoint module; when $A$ is semisimple, $A^-$ is reductive and they are its simple summands. The list is the union of the spins of the two families. The finer decomposition of an elementary carrier into the $W_j$ is its spin content; the lower $j$ are triple components of that carrier, not additional elementary carriers.

**Remark (the list is relative to the pair).** The same algebra with two pairs has two lists. The next two subsections compute the two canonical pairs of $M_n(\mathbb{C})$ and show that they differ.

### The Principal Pair of $M_n(\mathbb{C})$

**Proposition (the principal pair).** Let $n\ge2$ and

$$
S=\operatorname{diag}\Bigl(\frac{n+1}{2}-k\Bigr)_{k=1}^{n},\qquad
U=\sum_{k=1}^{n-1}\sqrt{k(n-k)}\,E_{k,k+1},\qquad
V=\sum_{k=1}^{n-1}\sqrt{k(n-k)}\,E_{k+1,k}.
$$

Then $(S,U,V)$ is a spin triple. The defining module $\mathbb{C}^n$ is $W_{(n-1)/2}$, of spin $(n-1)/2$. The adjoint module decomposes under the triple as

$$
\mathfrak{gl}_n=\bigoplus_{k=0}^{n-1}W_k,
$$

so its **spin content** is $0,1,\dots,n-1$. As a module for $A^-=\mathfrak{gl}_n$, however, $\mathfrak{gl}_n=\mathbb{C}I\oplus\mathfrak{sl}_n$: the centre is $W_0$, and the traceless part $\mathfrak{sl}_n$ is irreducible, of top spin $n-1$. The components $W_1,\dots,W_{n-1}$ are triple components of $\mathfrak{sl}_n$; their sum is irreducible under $\operatorname{ad}(A)$, with top spin $n-1$. The elementary list is therefore

$$
\Sigma\bigl(M_n(\mathbb{C}),\text{principal}\bigr)=\Bigl\{0,\ \frac{n-1}{2},\ n-1\Bigr\}.
$$

*Proof.* The commutators $[S,E_{k,k+1}]=E_{k,k+1}$ and $[S,E_{k+1,k}]=-E_{k+1,k}$ are immediate from the diagonal weights. The normalisation gives $[U,V]=2S$: the coefficient of $E_{kk}$ in the commutator is $k(n-k)-(k-1)(n-k+1)=n+1-2k$, which is twice the $k$-th diagonal entry of $S$. The weights of $S$ on $\mathbb{C}^n$ are $\frac{n-1}{2},\frac{n-3}{2},\dots,-\frac{n-1}{2}$, so the highest is $(n-1)/2$ and the spin is $(n-1)/2$. On $\mathfrak{gl}_n$ the weights are the differences $\lambda_i-\lambda_j=j-i$; the multiplicity of the integer $m$ is $n-\lvert m\rvert$ for $\lvert m\rvert\le n-1$, and the multiplicity formula gives the content $W_0\oplus\cdots\oplus W_{n-1}$. The centre is the weight-$0$ line $\mathbb{C}I$; the traceless part is the sum $W_1\oplus\cdots\oplus W_{n-1}$, irreducible under $\operatorname{ad}(A)$, with top spin $n-1$. The defining module adds the spin $(n-1)/2$.

**Corollary (the small cases).** The lists are:

| $n$ | defining spin | adjoint content | elementary spin list |
|---|---|---|---|
| $2$ | $\tfrac12$ | $0,1$ | $0,\tfrac12,1$ |
| $3$ | $1$ | $0,1,2$ | $0,1,2$ |
| $4$ | $\tfrac32$ | $0,1,2,3$ | $0,\tfrac32,3$ |
| $5$ | $2$ | $0,1,2,3,4$ | $0,2,4$ |
| $6$ | $\tfrac52$ | $0,1,2,3,4,5$ | $0,\tfrac52,5$ |

**The case $n=5$.** The defining module $\mathbb{C}^5$ is $W_2$. The adjoint's spin content is $W_0\oplus W_1\oplus W_2\oplus W_3\oplus W_4$, the spins $0,1,2,3,4$. The elementary carriers are the centre $\mathbb{C}I$ (spin $0$), the defining module $\mathbb{C}^5$ (spin $2$) and the traceless part $\mathfrak{sl}_5$ (spin $4$); the elementary list is $0,2,4$. The components $W_1,W_2,W_3,W_4$ are triple components of $\mathfrak{sl}_5$; since $\mathfrak{sl}_5$ is irreducible under $\operatorname{ad}(A)$, none of them is a separate elementary carrier.

**Remark (no half-integer for odd $n$).** For odd $n$, $(n-1)/2$ is an integer, so the elementary list $\{0,(n-1)/2,n-1\}$ contains no half-integer. For even $n$, $(n-1)/2$ is a half-integer and it is the only half-integer in the list. This is a property of the principal pair, not of the algebra: the balanced Peirce pair of the next subsection has $\tfrac12$ for every even $n$.

### The Balanced Peirce Pair

**Proposition (the Peirce pair).** Let $n=2r$ and let $e$ be an idempotent of rank $r$ in $M_n(\mathbb{C})$. After a change of basis that puts $e$ in the form $\operatorname{diag}(1,\dots,1,0,\dots,0)$,

$$
S=e-\tfrac12,\qquad U=\sum_{i=1}^{r}E_{i,r+i},\qquad V=\sum_{i=1}^{r}E_{r+i,i}
$$

is a spin triple. The defining module is $rW_{1/2}$; the adjoint's spin content is $r^2(W_1\oplus W_0)$. The adjoint elementary carriers are the centre $\mathbb{C}I$ (spin $0$) and the traceless part $\mathfrak{sl}_n$ (top spin $1$); the elementary list is $0,\tfrac12,1$.

*Proof.* $[S,E_{i,r+j}]=E_{i,r+j}$, $[S,E_{r+i,j}]=-E_{r+i,j}$, and $[U,V]=\sum_i(E_{ii}-E_{r+i,r+i})=2e-1=2S$. The defining module has $r$ weights $+\tfrac12$ and $r$ weights $-\tfrac12$, hence $r$ copies of $W_{1/2}$. The adjoint weights are $+1$ with multiplicity $r^2$, $-1$ with multiplicity $r^2$, and $0$ with multiplicity $2r^2$ (the two diagonal blocks); the multiplicity formula gives the content $r^2$ copies of $W_1$ and $r^2$ copies of $W_0$. The centre is the weight-$0$ line $\mathbb{C}I$; the traceless part is irreducible with top spin $1$. Together with the defining spin $\tfrac12$, the elementary list is $0,\tfrac12,1$.

**Corollary (the biquaternion is $r=1$).** At $n=2$, $r=1$, the Peirce pair is the frame pair of $\mathbb{B}=M_2(\mathbb{C})$, the defining module is $W_{1/2}$ (the spinor plane), and the adjoint's content is $W_1\oplus W_0$ (the traceless part and the centre). In the notation of that article, $2S=\tilde\Xi$, $U=\vec\Upsilon_-$ and $V=\vec\Upsilon_+$. This is the exact content of *The Spin of a Biquaternion*.

**Remark (the list depends on the pair).** On $M_4(\mathbb{C})$, the principal pair gives the elementary list $\Sigma=\{0,\tfrac32,3\}$ and the adjoint content $0,1,2,3$, while the balanced Peirce pair gives $\Sigma=\{0,\tfrac12,1\}$ and the adjoint content $0,1$. On $M_6(\mathbb{C})$, the principal pair gives $\Sigma=\{0,\tfrac52,5\}$ and the adjoint content $0,\dots,5$, while the Peirce pair gives $\Sigma=\{0,\tfrac12,1\}$ and the adjoint content $0,1$. The algebra has not changed; the pair has. There is no spin list of $M_4$ or $M_6$ without a pair.

**Remark (the frame root is not always a pair).** An idempotent $e$ gives the root $h=2e-1=2S$ and the corner signs, but not always a spin pair. The root closes to a pair exactly when $h\in[A_{+-},A_{-+}]$; this forces $h$ traceless. For a primitive idempotent of $M_n$, $\operatorname{tr}h=2-n$, so only $n=2$ can close; this is the failure proved in *The Weight of a Frame Root and the Spin Quantum Number*. For a balanced idempotent of $M_{2r}$, it closes for every $r$. A central idempotent gives a central root and no pair.

**Remark (the adjoint is not always integral).** For $\mathbb{B}$ and for $M_n(\mathbb{C})$ with the principal pair, the adjoint's spin content is integral. This is not a general law. The block upper triangular algebra with diagonal blocks $M_2$ and $M_3$ and the diagonal principal pair has, on its off-diagonal block, the adjoint weights obtained by subtracting a weight $1,0,-1$ of the $M_3$ block from a weight $\tfrac12$ of the $M_2$ block, namely $-\tfrac12,\tfrac12,\tfrac32$ and their negatives; the off-diagonal block is an adjoint carrier whose content contains $\tfrac12$ and $\tfrac32$, so its top spin is $\tfrac32$; the adjoint content of the algebra is therefore not integral. The integer-spin result of *Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form* is a property of the biquaternion and of the principal matrix pairs, not of every spin algebra.

### The Commutative Algebras

**Proposition (no pair, no spin).** If $A$ is commutative, then $[U,V]=0$ for all $U,V$, so there is no spin pair. A commutative algebra therefore has no spin structure and no carrier of nonzero spin; its modules are spinless.

**The cases.** The proposition covers:

- the complex numbers $\mathbb{C}$, read over $\mathbb{R}$ or over $\mathbb{C}$;
- the split-complex algebra $\mathbb{D}=\mathbb{R}[j]/(j^2-1)\cong\mathbb{R}\oplus\mathbb{R}$;
- the dual numbers $\mathbb{R}[\epsilon]/(\epsilon^2)$;
- the reduced biquaternion algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$;
- the real numbers $\mathbb{R}$ and every product of commutative algebras.

The reduced biquaternion algebra has a Peirce frame and nontrivial idempotents, but its root is central in each factor and does not close to a pair. A frame is not a spin.

**Remark (the complex numbers are not spin $0$).** The algebra $\mathbb{C}$ has no spin pair, so it has no spin. The value $0$ that one might assign to its module is not a spin of $\mathbb{C}$; it is the trivial value of the zero pair, which is excluded. When $\mathbb{C}$ sits as the centre $\mathbb{C}e_t$ of $\mathbb{B}$, the adjoint action of the biquaternion pair makes it the spin-$0$ carrier. That spin belongs to the biquaternion pair, not to $\mathbb{C}$.

**The solvable algebras.** The upper triangular algebra $T_n$ is solvable; a solvable Lie algebra has no subalgebra isomorphic to $\mathfrak{sl}_2$, which is semisimple. Hence $T_n$ has no spin pair and no spin, although it is non-commutative. The strictly upper triangular algebra is nilpotent and the same conclusion holds.

### Products and Split Forms

**Proposition (products).** Let $A$ and $B$ be spin algebras with pairs $\mathfrak{s}_A$ and $\mathfrak{s}_B$. Then $\bigl((S_A,S_B),(U_A,U_B),(V_A,V_B)\bigr)$ is a spin triple in $A\times B$. A simple module of $A\times B$ is a simple module of one factor with the other acting trivially; the elementary spin list is the union $\Sigma(A,\mathfrak{s}_A)\cup\Sigma(B,\mathfrak{s}_B)$.

*Proof.* The commutator in a product is componentwise, so the relations hold componentwise. For the associative action, a simple module of $A\times B$ is a simple module of one factor with the other acting trivially, hence $W_A\boxtimes k$ or $k\boxtimes W_B$. For the adjoint action, the adjoint module of $A\times B$ is the direct sum of the adjoint modules of the two factors. In both cases the elementary list is the union, and the spin is that of the nonzero factor.

**Remark (diagonal pairs).** A product also admits diagonal pairs, for example $\{((u,u),(v,v)):(u,v)\text{ a pair in }\mathfrak{sl}_2\}$ in $\mathfrak{sl}_2\times\mathfrak{sl}_2$. Under the diagonal pair, the module $W_{1/2}\boxtimes W_{1/2}$ has weights $1,0,0,-1$ and spin $1$; it is a carrier of the diagonal pair, not a module of the product algebra. This is the simplest way a pair in a product reaches a spin above the spins of the two factors.

**The split biquaternion.** The split biquaternion $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ is a product. A pair in one complexified factor gives the list $0,\tfrac12,1$, with the other factor trivial; the diagonal pair gives the tensor products of the two factors.

### The Table of the Cases

| algebra | base field | pair | elementary spins | adjoint content |
|---|---|---|---|---|
| $\mathbb{H}$ | $\mathbb{R}$ | frame pair in $\mathbb{B}$ | $0,\tfrac12,1$ | $0,1$ |
| $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{R}$ | real principal | $0,\tfrac12,1$ | $0,1$ |
| $\mathbb{B}$ | $\mathbb{C}$ | frame | $0,\tfrac12,1$ | $0,1$ |
| $M_2(\mathbb{C})$ | $\mathbb{C}$ | principal | $0,\tfrac12,1$ | $0,1$ |
| $M_3(\mathbb{C})$ | $\mathbb{C}$ | principal | $0,1,2$ | $0,1,2$ |
| $M_4(\mathbb{C})$ | $\mathbb{C}$ | principal | $0,\tfrac32,3$ | $0,1,2,3$ |
| $M_4(\mathbb{C})$ | $\mathbb{C}$ | balanced Peirce | $0,\tfrac12,1$ | $0,1$ |
| $M_5(\mathbb{C})$ | $\mathbb{C}$ | principal | $0,2,4$ | $0,1,2,3,4$ |
| $M_6(\mathbb{C})$ | $\mathbb{C}$ | principal | $0,\tfrac52,5$ | $0,1,2,3,4,5$ |
| $M_6(\mathbb{C})$ | $\mathbb{C}$ | balanced Peirce | $0,\tfrac12,1$ | $0,1$ |
| $M_n(\mathbb{C})$ | $\mathbb{C}$ | principal | $\{0,\tfrac{n-1}{2},n-1\}$ | $\{0,\dots,n-1\}$ |
| $\mathbb{H}_{\mathbb{D}}$ | $\mathbb{R}$ | one complexified factor | $0,\tfrac12,1$ | $0,1$ |

| algebra | reason for no spin |
|---|---|
| $\mathbb{C}$, $\mathbb{D}$, $\mathbb{R}[\epsilon]$, $\mathbb{B}_{\mathrm{r}}$, $\mathbb{R}$ | commutative |
| $T_n$ | solvable |

## The Real Forms

**The same spin, three types.** The quaternion algebra $\mathbb{H}$, the biquaternion algebra $\mathbb{B}$ read over $\mathbb{R}$, and the split quaternion algebra $\mathbb{H}_{\mathrm{s}}$ give the same elementary spin list but different carriers:

| real algebra | simple carrier | $\dim_{\mathbb{R}}$ | $\operatorname{End}$ | complexification of the carrier |
|---|---|---|---|---|
| $\mathbb{H}$ | $\mathbb{H}$ | $4$ | $\mathbb{H}$ | $2W_{1/2}$ |
| $\mathbb{B}$ | $\mathbb{C}^2$ | $4$ | $\mathbb{C}$ | $2W_{1/2}$ |
| $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{R}^2$ | $2$ | $\mathbb{R}$ | $W_{1/2}$ |

The complex algebra $\mathbb{B}$ has two real forms, $\mathbb{H}$ and $\mathbb{H}_{\mathrm{s}}$; reading $\mathbb{B}$ over $\mathbb{R}$ is the realification, not a third real form. The Frobenius–Schur type, read from the endomorphism ring, is quaternionic, complex and real. The spin is $\tfrac12$ in all three; the real dimension and the endomorphism ring are not.

**The general principle.** The spin is computed after complexification, so it is the same for a real algebra and for its complexification. The real form fixes the type of the carrier: real, complex or quaternionic, with endomorphism ring $\mathbb{R}$, $\mathbb{C}$ or $\mathbb{H}$. The same spin can therefore be carried by modules of different real dimensions; the type is read from the endomorphism ring, not from $j$.

**The spin-two example.** The real algebras $M_5(\mathbb{R})$, $M_5(\mathbb{C})$ read over $\mathbb{R}$, and $M_5(\mathbb{H})$ give the same spin $2$ on the defining carrier, with different real dimensions:

| real algebra | simple carrier | $\dim_{\mathbb{R}}$ | $\operatorname{End}$ | complexification under the triple |
|---|---|---|---|---|
| $M_5(\mathbb{R})$ | $\mathbb{R}^5$ | $5$ | $\mathbb{R}$ | $W_2$ |
| $M_5(\mathbb{C})$ | $\mathbb{C}^5$ | $10$ | $\mathbb{C}$ | $2W_2$ |
| $M_5(\mathbb{H})$ | $\mathbb{H}^5$ | $20$ | $\mathbb{H}$ | $4W_2$ |

## What Is Not a Definition

**The definition has one form: $j=\lambda_{\max}(\rho(S))$ on a carrier of a nonzero spin pair.** The following are not definitions.

- **The dimension.** A carrier of dimension $2$ can be $W_{1/2}$ or $W_0\oplus W_0$; a carrier of dimension $3$ can be $W_1$ or $W_{1/2}\oplus W_0$. The dimension bounds the spin but does not determine it.
- **The rank or determinant of a multiplication operator.** On a spinor plane of $\mathbb{B}$, the determinant of $L_{\tilde Q}$ is the norm and its rank is $2$ or $1$; the spin stays $\tfrac12$. Half the rank is $1$ or $\tfrac12$; the rank does not determine the spin. This is the computation of *The Spin of a Biquaternion*.
- **The Peirce index.** The right action of the root $2S$ is $+1$ on one plane and $-1$ on the other; the right action of $S$ is $\pm\tfrac12$. That sign labels two copies of one left module. It is a Peirce index, not the spin and not a chirality. In the real form $\mathbb{B}_{\mathbb{R}}$, the chirality is the central sign $\chi=ij$ of the complexification $\mathbb{B}_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}$, $\chi^2=1$, which grades $S$ against $S^{\mathrm{c}}$; it is not in $\mathbb{B}_{\mathbb{R}}$.
- **The half-angle.** The angle $\theta/2$ of the rotor is half the exponential coordinate $\theta$ of the spin operator; it is a coordinate of the weight, not the highest weight. The spin is $j$. A spinor rotation has period $4\pi$ because $j=\tfrac12$, not because the half-angle is the spin.
- **The Casimir value.** The Casimir acts by $j(j+1)$; it is a function of the spin. On a carrier with summands of different spins it is not a single number, and its largest eigenvalue gives $j$ by solving $j(j+1)=\lambda$.
- **The weight of a vector.** A vector of weight $m$ has magnetic quantum number $m$; it is not a carrier of spin $m$. The spin is the highest weight of the carrier that contains it.
- **The algebra or the element.** An algebra has no spin; an element has no spin. The element $S$ is the spin operator; the element $U$ is a ladder operator.
- **The zero pair.** The zero pair satisfies the double-commutator conditions and assigns spin $0$ to everything; it is excluded because $[U,V]=0$, so the antisymmetric part vanishes.
- **A central root.** An idempotent whose root is central gives no pair; its formal $\lambda_{\max}$ is not a spin. This excludes $e=0$ and $e=1$, and the roots of the commutative algebras.

## Summary

- A spin is a property of a carrier of a chosen spin pair $(U,V)$, with $[U,V]\neq0$, $[[U,V],U]=2U$ and $[[U,V],V]=-2V$; the algebra alone has no spin.
- The spin element is the antisymmetric part of the product, $S=\tfrac12(UV-VU)=\tfrac12[U,V]$; it satisfies $[S,U]=U$, $[S,V]=-V$, $[U,V]=2S$, and the span of $S,U,V$ is $\mathfrak{sl}_2$. The other articles write $H=2S$.
- A carrier of the triple is a finite-dimensional module for the triple; a carrier of the algebra is also a module for $A$ under the associative action, or for the Lie algebra $A^-$ under the adjoint action. The weights are the eigenvalues of $\rho(S)$, the highest weight is the largest, and the spin is $j=\lambda_{\max}$.
- The Casimir $C=S^2+\tfrac12(UV+VU)$ acts by $j(j+1)$.
- Every finite-dimensional carrier of the triple is a direct sum of $W_j$, with $\dim W_j=2j+1$ and weights $j,j-1,\dots,-j$; the multiset of the summands is the spin content, the spin is its maximum, and the multiplicity formula is $m_j=\mu(j)-\mu(j+1)$.
- The elementary carriers are the simple left modules and the irreducible $\operatorname{ad}(A)$-stable subspaces of the adjoint module; for a semisimple algebra the second family is the simple summands of the adjoint. The elementary spin list is their union, and it depends on the pair.
- For $M_n(\mathbb{C})$ with the principal pair, the defining spin is $(n-1)/2$, the adjoint's spin content is $0,\dots,n-1$, and the elementary carriers are the centre ($0$), the defining module ($(n-1)/2$) and the traceless part ($n-1$); the elementary list is $\{0,(n-1)/2,n-1\}$. For $M_5(\mathbb{C})$ the list is $0,2,4$ and the adjoint content is $0,\dots,4$.
- For $M_n(\mathbb{C})$ with the balanced Peirce pair of an idempotent of rank $n/2$, the list is $0,\tfrac12,1$ and the adjoint content is $0,1$ for every even $n$; the biquaternion is the case $n=2$.
- $\mathbb{H}$, $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{B}$ all have the list $0,\tfrac12,1$; they differ in the real form of the spin-$\tfrac12$ carrier, which is quaternionic, real and complex respectively.
- $\mathbb{C}$, the split-complex algebra, the dual numbers and the reduced biquaternions are commutative; the upper triangular algebras are solvable; they admit no spin pair and carry no spin. The spin-$0$ carrier of $\mathbb{B}$ is its centre, not the algebra $\mathbb{C}$.
- The adjoint's spin content is integral for $\mathbb{B}$ and for $M_n(\mathbb{C})$ with the principal pair, but not for every pair; the block upper triangular algebra with blocks $M_2$ and $M_3$ has adjoint content containing $\tfrac12$ and $\tfrac32$.
- The dimension, the rank, the Peirce index, the half-angle, the Casimir value, the weight of a vector, the algebra and the element are not the spin; the zero pair and a central root are not spin structures.

## Summary of Notation

| symbol | meaning |
|---|---|
| $A$, $k$ | algebra and base field, of characteristic zero |
| $A_{\mathbb{C}}$ | complexification of a real algebra |
| $A^-$ | the algebra $A$ with the commutator, a Lie algebra |
| $(U,V)$ | spin pair, $[U,V]\neq0$, $[[U,V],U]=2U$, $[[U,V],V]=-2V$ |
| $S=\tfrac12[U,V]$ | spin element, the antisymmetric part of $UV$ |
| $(S,U,V)$ | spin triple, $[S,U]=U$, $[S,V]=-V$, $[U,V]=2S$ |
| $H=2S$ | the Cartan in the doubled notation of the other articles |
| $\rho$ | action of the triple, and of $A$ when the carrier is a carrier of the algebra |
| $W_j$ | irreducible carrier of the triple, of spin $j$, dimension $2j+1$, weights $j,\dots,-j$ |
| spin content | the multiset of the spins of the triple summands of a carrier |
| elementary carrier | a nonzero irreducible module for $A$ (associative) or an irreducible $\operatorname{ad}(A)$-stable subspace of $A$ (adjoint) |
| $\lambda$, $\mu(\lambda)$ | a weight of $S$ and its multiplicity |
| $\lambda_{\max}$ | highest weight |
| $j=\lambda_{\max}$ | spin |
| $C=S^2+\tfrac12(UV+VU)$ | Casimir, eigenvalue $j(j+1)$ |
| $\Sigma(A,\mathfrak{s})$ | elementary spin list |
| $M_n(\mathbb{C})$ | matrix algebra, $1$-based indices |
| $J_3,J_\pm$ | principal triple of $M_n(\mathbb{C})$, with $S=J_3$ |
| $E_{ij}$ | matrix unit |
| $\mathbb{B}$ | biquaternion algebra, $\mathbb{C}\otimes\mathbb{H}$ |
| $\mathbb{B}_{\mathbb{R}}$ | real form of $\mathbb{B}$ |
| $\mathbb{H}$, $\mathbb{H}_{\mathrm{s}}$ | quaternion and split-quaternion algebras |
| $\mathbb{D}$, $\mathbb{B}_{\mathrm{r}}$ | split-complex and reduced biquaternion algebras |
| Peirce triple | $(e-\tfrac12,u,v)$ of a balanced idempotent |

## Further Reading

- [Representations of Lie Algebras](representations-of-lie-algebras.html), for the modules, the weights, the highest weight and the classification of the $\mathfrak{sl}_2$ modules.
- [The Casimir Operator](the-casimir-operator.html), for the Casimir element, its centrality and its eigenvalue.
- [The Spin of a Biquaternion](the-spin-of-a-biquaternion.html), for the frame pair and the three elementary carriers of $\mathbb{B}$.
- [The Weight of a Frame Root and the Spin Quantum Number](the-weight-of-a-frame-root-and-the-spin-quantum-number.html), for the definitions of carrier, weight and the Peirce root.
- [The Spin Chain and the Adjoint Decomposition of $M_n(\mathbb{C})$](the-spin-chain-and-the-adjoint-decomposition-mnc.html), for the principal pair and the adjoint chain.
- [Spinors as Peirce Coordinates in $n$ Dimensions](spinors-as-peirce-coordinates-in-n-dimensions.html), for the Peirce coordinates and the half-angle.
- [The Peirce Decomposition in $n$ Dimensions](the-peirce-decomposition-in-n-dimensions.html), for the corners and the frame.
- [The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-mnc.html), for the frame and its nilpotents.
- [The Biquaternion Algebra](the-biquaternion-algebra-and-its-vector-spaces.html), for $\mathbb{B}$.
- [The Quaternion Algebra](quaternion-algebra.html), [The Split-Quaternion Algebra](split-quaternion-algebra.html), [The Split-Complex Algebra](split-complex-algebra.html), and [Introduction to the General Plain Algebra of the Reduced Biquaternions](introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the cases.
- [The Matrix Algebra $M_5(\mathbb{C})$](the-matrix-algebra-m5c.html), for the spin-two chain.
- [Chirality: The Conjugate Pair](chirality-the-conjugate-pair.html), for the central sign $\chi=ij$ and the Peirce index.
- [Spin and the Three Elementary Carriers](../articles_physics/spin-and-the-three-elementary-carriers.html), for the physical interpretation of the list $0,\tfrac12,1$.
- [Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form](../articles_physics/integer-spin-quantization-and-the-adjoint-action-on-the-material-sector-in-biquaternionic-form.html), for the integer spins of the adjoint.
- [Higher Spin from Tensor Products](../articles_physics/higher-spin-from-tensor-products-why-the-biquaternion-algebra-admits-only-spin-0-and-one-half.html), for the spins above the elementary list.
- [Conventions in the Biquaternion Universe](../articles_physics/conventions-in-the-biquaternion-universe.html), for the conventions of the corpus.
