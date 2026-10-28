# __Off-Diagonal Peirce Components and Noncentral Idempotents__

## Introduction

An idempotent $e$ in a unital associative algebra splits the algebra into four corners: the two diagonal corners $eAe$ and $(1-e)A(1-e)$, which are algebras, and the two off-diagonal corners $eA(1-e)$ and $(1-e)Ae$, which are bimodules. The diagonal part is the centraliser of $e$; the off-diagonal part is the set of elements that fail to commute with $e$. This article studies the off-diagonal part as the precise measure of the noncentrality of $e$.

The article assumes the Peirce decomposition of *Unital Algebras*, §*Idempotents and the Peirce Decomposition*, and the centraliser theorem of *The Centraliser and the Diagonal Peirce Part*. The passage from one idempotent to a complete orthogonal family, with the relative complement in a corner and the refinement and coarsening of the decomposition, is *Complementary Idempotents and the Peirce Decomposition*. The commutator operator is *The Commutator Operator*; the ideals and quotients are *Ideals and Quotients of Algebras*; the biquaternion example is *The Peirce Decomposition of the Biquaternion Algebra*. The primitive idempotents and the minimal left ideals are treated in *List of Rings by Their Idempotents* and *Simple and Semisimple Modules*; this article does not use them. The base is a field $k$ and $A$ is a finite-dimensional unital associative $k$-algebra. The idempotent $e \in A$ is arbitrary, and $f = 1_A - e$.

The main point is a warning about language. The off-diagonal part measures the failure of $e$ to be central, not the failure of $A$ to be commutative. A nonzero off-diagonal part forces $A$ to be noncommutative, but a noncommutative algebra can have idempotents with a zero off-diagonal part, and a commutative algebra has no other kind. The article separates the two notions carefully.

## The Four Corners

### The Peirce decomposition

Let $e \in A$ be an idempotent, $e^2 = e$, and let $f = 1_A - e$. Then $f$ is also an idempotent, $e f = f e = 0$, and $e + f = 1_A$. Every $x \in A$ has the expansion

$$
x = (e+f)x(e+f) = exe + exf + fxe + fxf .
$$

The four summands lie in the four subspaces

$$
eAe, \qquad eAf, \qquad fAe, \qquad fAf,
$$

and the sum is direct. Indeed, if $x = x_{00} + x_{01} + x_{10} + x_{11}$ with $x_{ij} \in e_i A e_j$ (where $e_0 = e$ and $e_1 = f$), then multiplying by $e$ or $f$ on the left and on the right isolates each summand. This is the **Peirce decomposition** of $A$ relative to $e$:

$$
\boxed{\;A = eAe \oplus eAf \oplus fAe \oplus fAf\;} .
$$

The decomposition is the $r=2$ case of the two-sided Peirce decomposition of *The Eigenvalue Decomposition of an Element*, with the complete orthogonal family $e, f$ and the eigenvalues $1, 0$.

### The multiplication table

The four corners multiply according to the rule

$$
(e_i A e_j)(e_k A e_l) \subseteq \delta_{jk}\, e_i A e_l, \qquad i,j,k,l \in \{0,1\},
$$

with $e_0 = e$ and $e_1 = f$. In words: a product of two corners is nonzero only when the right index of the first equals the left index of the second, and then the result lies in the corner with the outer indices. The rule is the associativity of $A$ together with $e^2=e$, $f^2=f$ and $ef=fe=0$.

The rule has several consequences.

- The **diagonal corners** $eAe$ and $fAf$ are algebras with identities $e$ and $f$ respectively. They are not unital subalgebras of $A$ in the sense of sharing $1_A$, unless the corner is zero; their identities are $e$ and $f$.
- The **mixed corners** $eAf$ and $fAe$ are bimodules over the diagonal corners: $eAe$ acts on $eAf$ on the left, $fAf$ acts on it on the right, and similarly for $fAe$.
- Each mixed corner **squares to zero**: $(eAf)(eAf) = eA f e A f = 0$, and similarly $(fAe)^2 = 0$.
- The product of the two mixed corners lands in the diagonal corners: $(eAf)(fAe) \subseteq eAe$ and $(fAe)(eAf) \subseteq fAf$.

### The diagonal and off-diagonal parts

Define

$$
D = eAe \oplus fAf, \qquad N = eAf \oplus fAe .
$$

The subspace $D$ is the **diagonal Peirce part** and $N$ is the **off-diagonal Peirce part**. Then $A = D \oplus N$ as $k$-vector spaces.

The diagonal part is a unital subalgebra of $A$: it contains $1_A = e + f$, and $D \cdot D \subseteq D$ by the multiplication table. The off-diagonal part is a $D$-bimodule, and

$$
N^2 \subseteq D,
$$

because the two mixed corners multiply into the diagonal corners. This is the $r=2$ case of the general statement of *The Centraliser and the Diagonal Peirce Part*; for $r \ge 3$ the square of the off-diagonal part can have off-diagonal components, but here there are only two indices and the product of two mixed corners is diagonal.

The projection onto the diagonal part along $N$ is

$$
\pi : A \longrightarrow D, \qquad \pi(x) = exe + fxf .
$$

It is unital, $D$-bimodule linear, and idempotent. It is multiplicative if and only if $N^2 = 0$, by the computation of *The Centraliser and the Diagonal Peirce Part*: for $x = \pi(x) + n_x$ and $y = \pi(y) + n_y$, one has

$$
\pi(xy) = \pi(x)\pi(y) + n_x n_y,
$$

and $n_x n_y \in N^2 \subseteq D$, so the obstruction is exactly the product of the off-diagonal parts.

## The Commutator Interpretation

### The off-diagonal part as a commutator

The commutator of $e$ with $x$ is

$$
[e,x] = ex - xe = (exe + exf) - (exe + fxe) = exf - fxe .
$$

The diagonal terms cancel, and the result lies in $N = eAf \oplus fAe$. Conversely, every element of $N$ is a commutator with $e$:

$$
[e, eaf] = e(eaf) - (eaf)e = eaf, \qquad [e, fae] = e(fae) - (fae)e = -fae .
$$

Therefore

$$
\boxed{\;[e,A] = N\;} .
$$

The off-diagonal part is exactly the image of the inner derivation $\operatorname{ad}_e(x) = [e,x]$. Its kernel is the centraliser

$$
C(e) = \{x : ex = xe\} = D,
$$

which is the diagonal part. This is the $r=2$ case of the theorem of *The Centraliser and the Diagonal Peirce Part*: the centraliser of an idempotent is its diagonal Peirce part.

### The eigenspaces of the commutator

The map $\operatorname{ad}_e$ acts on the four corners by

$$
\operatorname{ad}_e(eae) = 0, \quad \operatorname{ad}_e(faf) = 0, \quad \operatorname{ad}_e(eaf) = eaf, \quad \operatorname{ad}_e(fae) = -fae .
$$

Thus $A$ is the direct sum of the eigenspaces of $\operatorname{ad}_e$ for the eigenvalues $0, 1, -1$:

$$
A = \underbrace{fAe}_{-1} \oplus \underbrace{(eAe \oplus fAf)}_{0} \oplus \underbrace{eAf}_{+1} .
$$

On the diagonal part, $\operatorname{ad}_e = 0$; on the off-diagonal part, $\operatorname{ad}_e^2 = \mathrm{id}$. Hence $\operatorname{ad}_e^2$ is the projection onto $N$ with kernel $D$, and

$$
\pi = 1_A - \operatorname{ad}_e^2 .
$$

The Peirce decomposition is therefore the eigenspace decomposition of the inner derivation $\operatorname{ad}_e$, and the diagonal projection is the spectral projection of $\operatorname{ad}_e$ for the eigenvalue $0$. The eigenvalues $+1$ and $-1$ are the two off-diagonal directions.

### The grading

The eigenspace decomposition can be read as a $\mathbb{Z}$-grading. Put

$$
A_{-1} = fAe, \qquad A_0 = eAe \oplus fAf, \qquad A_1 = eAf .
$$

Then

$$
\boxed{\;A = A_{-1} \oplus A_0 \oplus A_1, \qquad A_p A_q \subseteq A_{p+q}\;},
$$

with $A_p = 0$ for $|p| > 1$. The multiplication table verifies the grading: $A_1 A_1 = 0 = A_2$, $A_{-1} A_{-1} = 0 = A_{-2}$, $A_1 A_{-1} \subseteq A_0$, $A_{-1} A_1 \subseteq A_0$, and $A_0$ acts on $A_{\pm 1}$ by left and right multiplication. The Peirce decomposition is the graded decomposition of $A$ by the eigenvalues of $\operatorname{ad}_e$, with the degree $p$ equal to the eigenvalue.

The grading is a property of the single idempotent $e$. It does not extend to the family of eigenprojectors of a general split separable element with more than two eigenvalues: there the off-diagonal part is a sum over pairs and the product of two off-diagonal pieces can have a third index, as explained in *The Centraliser and the Diagonal Peirce Part*.

## Central versus Noncentral Idempotents

### The central case

The following conditions are equivalent:

1. $e$ is central, $e \in Z(A)$;
2. $eA = Ae$;
3. $eAf = 0$ and $fAe = 0$;
4. $N = 0$;
5. $A = D = eAe \oplus fAf$;
6. $A \cong Ae \times Af$ as algebras.

The equivalence of 1 and 2 is the definition of centrality. If $e$ is central, then $eaf = aef = 0$ and $fae = fea = 0$. More directly, $eA = Ae$ implies $eAf = Ae f = 0$ and $fAe = f e A = 0$. Conversely, if $eAf = 0$ and $fAe = 0$, then for every $x$,

$$
ex = e x e + e x f = e x e, \qquad xe = e x e + f x e = e x e,
$$

so $ex = xe$. If $N = 0$, then $A = D$, and the computation above shows $e$ is central. If $e$ is central, the map $a \mapsto (ae, af)$ is an isomorphism $A \to Ae \times Af$ with inverse $(u,v) \mapsto u+v$, because $u = ae$ and $v = af$ satisfy $uv = a e a' f = a a' e f = 0$. The converse is the product decomposition: in $A = B \times C$, the idempotent $(1_B,0)$ is central.

In the central case the Peirce decomposition is a product decomposition. The idempotent splits the algebra into two independent factors, and the off-diagonal part vanishes. This is the case treated in *Unital Algebras*, §*Idempotents and the Peirce Decomposition*, in the corollary that a central idempotent splits the algebra.

### The noncentral case

If $e$ is not central, then $N \neq 0$: some element fails to commute with $e$, and the commutator $[e,x]$ is a nonzero element of $N$. The Peirce decomposition is then not a product decomposition. The diagonal part $D$ is a subalgebra, but it is not an ideal; the off-diagonal part $N$ is a $D$-bimodule, but it is not a subalgebra and need not be an ideal.

The left and right ideals generated by $e$ are

$$
Ae = eAe \oplus fAe, \qquad eA = eAe \oplus eAf .
$$

The two-sided ideal $AeA$ is larger. Expanding a product $aeb$ in Peirce components shows that a term $a_{i0}eb_{0l}$ lies in $A_{il}$; in particular, it contains the products $A_{10}A_{01}\subseteq fAf$. In $M_n(k)$ these products span $fAf$, so $fAf\subseteq AeA$. Thus $AeA$ is not the complement of $fAf$ in general. In a simple algebra, in particular in $M_n(k)$ for $e\neq0$, it is the whole algebra.

The corner $fAf$ is a subalgebra, but the map

$$
\varphi : A \longrightarrow fAf, \qquad \varphi(a) = faf,
$$

is not multiplicative in general. Its kernel is the subspace $eAe\oplus eAf\oplus fAe$ of elements with zero $fAf$ corner, so $A/\ker\varphi \cong fAf$ only as $k$-vector spaces. The corner is a quotient algebra exactly in the central case: if $e$ is central, then $AeA=Ae$ and $A/Ae \cong Af=fAf$ as algebras.

A nontrivial idempotent therefore need not generate a proper two-sided ideal: in $M_2(k)$, the idempotent $E_{11}$ generates the whole algebra. What is proper is the left ideal $Ae$ when $e\neq1$, and the right ideal $eA$. This is the first step in the structure theory of finite-dimensional algebras: the primitive idempotents are those for which the corner $eAe$ has no nontrivial idempotents (it is a local ring in the finite-dimensional case, and a division algebra in the semisimple case), and the minimal left ideals are the corresponding $Ae$.

### The off-diagonal part as a measure of noncentrality

The off-diagonal part $N$ measures the failure of $e$ to be central. It does not measure the failure of $A$ to be commutative. The logical relations are:

- If $A$ is commutative, then every idempotent is central, so $N = 0$ for every $e$.
- If $N \neq 0$, then $A$ is not commutative. This is the contrapositive of the previous point.
- If $N = 0$, then $A$ need not be commutative. The algebra $M_2(k) \times M_2(k)$ with $e = (1,0)$ is noncommutative, and $e$ is central. The idempotents $0$ and $1$ in any noncommutative algebra are central. So a zero off-diagonal part is compatible with noncommutativity.

In one sentence: $N \neq 0$ is a sufficient witness of noncommutativity, but it is exactly the failure of centrality of $e$, and centrality is stronger than commutativity of the ambient algebra. The article's title uses "noncentral idempotents" for this reason; "noncommutativity" would overstate what $N$ detects.

The dimension of $N$ is a quantitative measure of the noncentrality. In a matrix algebra it is $2k(n-k)$ for an idempotent of rank $k$, which is zero exactly at the central idempotents $k=0$ and $k=n$ and is maximal at $k=n/2$. In a general algebra the dimension of $N$ is the defect of the centraliser, $\dim N = \dim A - \dim C(e)$.

## The Matrix Case

### The corners of a rank-$k$ idempotent

Let $A = M_n(k)$ and let $e$ be an idempotent of rank $k$. After conjugating by an invertible matrix, $e = \operatorname{diag}(I_k, 0)$, and the four corners are

$$
eAe \cong M_k(k), \qquad fAf \cong M_{n-k}(k), \qquad eAf \cong M_{k,n-k}(k), \qquad fAe \cong M_{n-k,k}(k).
$$

Their dimensions are $k^2$, $(n-k)^2$, $k(n-k)$ and $k(n-k)$, and their sum is $n^2$. The diagonal part has dimension $k^2 + (n-k)^2$, and the off-diagonal part has dimension

$$
\dim N = 2k(n-k).
$$

The off-diagonal part vanishes exactly when $k = 0$ or $k = n$, that is, exactly when $e = 0$ or $e = 1$; these are the only central idempotents of $M_n(k)$. For $0 < k < n$, the idempotent is noncentral and $N \neq 0$.

### The square of the off-diagonal part

For $0 < k < n$, the two mixed corners multiply onto the full diagonal corners:

$$
eAf \cdot fAe = eAe, \qquad fAe \cdot eAf = fAf .
$$

Hence

$$
N^2 = eAe \oplus fAf = D \neq 0 .
$$

The diagonal projection $\pi$ is therefore not multiplicative. It is the projection of a matrix onto its two diagonal blocks; the product of two off-diagonal blocks can be a nonzero diagonal block, and the projection of the product differs from the product of the projections.

The off-diagonal part is not an ideal when $0 < k < n$: if it were an ideal, then $N^2 \subseteq N \cap D = 0$, contradicting $N^2 = D \neq 0$. The two-sided ideal generated by $e$ is $A$ itself, because $M_n(k)$ is simple and $e\neq0$. The set of matrices whose $fAf$ block is zero is the kernel of the linear map $\varphi$, not the ideal $AeA$ and not an ideal at all.

### The extremal ranks

- **Rank zero or full rank.** $e = 0$ or $e = 1$. The off-diagonal part is zero, the idempotent is central, and the Peirce decomposition is the trivial one. In $M_n(k)$ these are the only central idempotents, because a central idempotent is a scalar idempotent and the only scalar idempotents in a field are $0$ and $1$.
- **Rank one.** $k = 1$. The off-diagonal part has dimension $2(n-1)$: the first row and the first column off the diagonal. The left ideal $Ae$ is the set of matrices whose last $n-1$ columns vanish, and the right ideal $eA$ is the set whose last $n-1$ rows vanish; both are minimal. The two-sided ideal $AeA$ is the whole algebra. The corner $eAe$ is one-dimensional, so $e$ is a primitive idempotent. This is treated in *Simple and Semisimple Modules*.
- **Half rank.** $k = n/2$ for even $n$. The off-diagonal part has the maximal dimension $n^2/2$, equal to the dimension of the diagonal part. The two mixed blocks are square and as large as possible.

## The Biquaternion Case

Let $\mathbb{B} \cong M_2(\mathbb{C})$ be the biquaternion algebra, and let $\Pi_+$ be the idempotent of the Peirce decomposition of *The Peirce Decomposition of the Biquaternion Algebra*. In the matrix model, $\Pi_+$ is a rank-one projection, conjugate to $\operatorname{diag}(1,0)$. The four corners are one-dimensional:

$$
\Pi_+ \mathbb{B} \Pi_+ \cong \mathbb{C}, \qquad \Pi_- \mathbb{B} \Pi_- \cong \mathbb{C}, \qquad \Pi_+ \mathbb{B} \Pi_- \cong \mathbb{C}, \qquad \Pi_- \mathbb{B} \Pi_+ \cong \mathbb{C},
$$

with $\Pi_- = 1 - \Pi_+$. The diagonal part is two-dimensional and commutative, the off-diagonal part is two-dimensional, and $N^2 = D$. The off-diagonal directions are the two nilpotent directions that mix the two Peirce components; they are the biquaternion analogue of the strictly upper and strictly lower triangular matrix units. The idempotent $\Pi_+$ is not central, because the two components of the biquaternion algebra are not independent under the full multiplication; the Peirce decomposition is not a product decomposition.

The example is the smallest noncommutative case: the algebra is four-dimensional over $\mathbb{C}$, the diagonal part is two-dimensional, and the off-diagonal part is two-dimensional. The failure of centrality is visible in the two nilpotent directions. The two-sided ideal generated by $\Pi_+$ is $\mathbb{B}$ itself, because $\mathbb{B}$ is simple; the left ideal $\mathbb{B}\Pi_+$ is two-dimensional, and the corner $\Pi_-\mathbb{B}\Pi_-$ is one-dimensional.

## Summary

An idempotent $e$ with $f = 1-e$ gives the Peirce decomposition

$$
A = eAe \oplus eAf \oplus fAe \oplus fAf,
$$

with diagonal part $D = eAe \oplus fAf$ and off-diagonal part $N = eAf \oplus fAe$. The diagonal part is a unital subalgebra, the off-diagonal part is a $D$-bimodule, and $N^2 \subseteq D$. The centraliser of $e$ is $C(e) = D$, and the image of the inner derivation $\operatorname{ad}_e$ is $N$: the off-diagonal part is exactly the set of commutators $[e,x]$. The Peirce decomposition is the eigenspace decomposition of $\operatorname{ad}_e$ for the eigenvalues $0, +1, -1$, equivalently the $\mathbb{Z}$-grading with $A_{-1} = fAe$, $A_0 = D$, $A_1 = eAf$.

The idempotent $e$ is central if and only if $N = 0$, if and only if $A \cong Ae \times Af$. In that case the Peirce decomposition is a product decomposition. If $e$ is noncentral, $N \neq 0$ and the decomposition is not a product. The two-sided ideal $AeA$ need not be proper: it is the whole algebra when $A$ is simple and $e\neq0$. The corner $fAf$ is always a subalgebra, but it is a quotient algebra of $A$ exactly in the central case. The left ideal $Ae$ and the right ideal $eA$ are proper whenever $e\neq1$.

The off-diagonal part measures noncentrality, not noncommutativity. A nonzero $N$ forces $A$ to be noncommutative, but a noncommutative algebra can have a central idempotent with $N = 0$ (for example $M_2(k) \times M_2(k)$ with $e = (1,0)$), and a commutative algebra has only central idempotents. In $M_n(k)$ with $e$ of rank $k$, $\dim N = 2k(n-k)$, the off-diagonal part vanishes exactly at $k=0,n$, and $N^2 = D \neq 0$ for $0<k<n$. The biquaternion algebra with a rank-one idempotent is the smallest noncommutative example: two diagonal directions and two off-diagonal nilpotent directions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e$ | An idempotent, $e^2 = e$ |
| $f$ | $1_A - e$, the complementary idempotent |
| $eAe$, $fAf$ | The diagonal corners, algebras with identities $e$ and $f$ |
| $eAf$, $fAe$ | The mixed corners, bimodules over the diagonal corners |
| $D = eAe \oplus fAf$ | The diagonal Peirce part; equal to $C(e)$ |
| $N = eAf \oplus fAe$ | The off-diagonal Peirce part; equal to $[e,A]$ |
| $\pi(x) = exe + fxf$ | The projection onto $D$ along $N$ |
| $\operatorname{ad}_e(x) = ex - xe$ | The inner derivation; $\ker \operatorname{ad}_e = D$, $\operatorname{im} \operatorname{ad}_e = N$ |
| $A_{-1} = fAe$, $A_0 = D$, $A_1 = eAf$ | The $\mathbb{Z}$-grading by the eigenvalues of $\operatorname{ad}_e$ |
| $Ae$ | The left ideal $eAe \oplus fAe$ generated by $e$ |
| $eA$ | The right ideal $eAe \oplus eAf$ generated by $e$ |
| $AeA$ | The two-sided ideal generated by $e$; equal to $A$ when $A$ is simple and $e\neq0$ |
| $k$ | In $M_n(k)$, the rank of $e$; $\dim N = 2k(n-k)$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and the corner algebras.
- Yurij A. Drozd and Vladimir V. Kirichenko, *Finite Dimensional Algebras* (Springer, 1994), for the Peirce decomposition and the corner algebras.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for the idempotent $e$, the corner $eAe$ and the left and right ideals $Ae$ and $eA$.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for central idempotents, product decompositions and the structure of matrix rings.
- Nicolas Bourbaki, *Algèbre*, Chapitre VII, for the Peirce decomposition and the graded structure attached to an idempotent.
- The corpus article *The Peirce Decomposition of the Biquaternion Algebra*, for the explicit biquaternion Peirce decomposition used in §*The Biquaternion Case*.
