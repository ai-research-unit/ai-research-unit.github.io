# __$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety__

## Introduction

The zero divisors of the biquaternion algebra are the nonzero elements of vanishing quaternionic norm. In the matrix model they are the nonzero singular matrices, and a nonzero singular two-by-two matrix has rank one. Every one of them is an outer product of two vectors, and the two vectors carry the two pieces of data the algebra sees: a direction and a covector.

This article develops the factorisation, the two strata of the determinantal variety, the annihilators and the geometry of the cone. It is the matrix form of *The N-Degenerate Sector*, §*The Stratification of the Cone*, and of *Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra*, §*The Peirce Coordinates and the Matrix Model*.

**Conventions.** The algebra and the model are those of *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure*. The norm is $N=Q_t^2+B^2=\det\mathsf{M}_2(\tilde Q)$. A vector of $\mathbb{C}^2$ is a column $u$, a covector is a row $v^{\mathsf T}$, and $uv^{\mathsf T}$ is the matrix of entries $(uv^{\mathsf T})_{ij}=u_iv_j$. The standard idempotents are $\tilde\Pi_\pm$ and the standard nilpotents are $\vec\Upsilon_x,\vec\Upsilon_y$.

**Boundaries.** The null cone and its stratification are *The N-Degenerate Sector*; the nilpotents are *Square Roots of Zero and the Nilpotents of the Biquaternion Algebra*; the rank-one elements and the Peirce corners are *Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra*; the singular matrices as a determinantal variety are also treated in *The Determinant and Alternating Forms*.

## The Factorisation

**Theorem.** A nonzero matrix $M\in M_2(\mathbb{C})$ has rank one exactly when there are nonzero vectors $u,v\in\mathbb{C}^2$ with

$$
M=uv^{\mathsf T}.
$$

The pair $(u,v)$ is determined up to the reciprocal scaling $u\mapsto\lambda u$, $v\mapsto\lambda^{-1}v$ with $\lambda\in\mathbb{C}^{\times}$.

*Proof.* If $M=uv^{\mathsf T}$ with both vectors nonzero, every column is a multiple of $u$, so the rank is one. Conversely, if the rank is one, the two columns are proportional to a nonzero vector $u$; write the first column as $u v_1$ and the second as $u v_2$, and put $v=(v_1,v_2)$. The pair is nonzero because $M\neq0$. A second pair $(u',v')$ giving the same matrix satisfies $u'v'^{\mathsf T}=uv^{\mathsf T}$; comparing the columns gives $u'=\lambda u$, and then $v'=\lambda^{-1}v$.

**The two invariants of the factorisation.**

$$
\operatorname{Tr}(uv^{\mathsf T})=v^{\mathsf T}u,\qquad
\det(uv^{\mathsf T})=0.
$$

The determinant vanishes identically, so every rank-one matrix is singular. The trace is the contraction of the two vectors, and it is the only invariant of the pair beyond the scaling. In biquaternion terms,

$$
uv^{\mathsf T}=\mathsf{M}_2(\tilde Q)\quad\Longrightarrow\quad
2Q_t=v^{\mathsf T}u,\qquad N=0.
$$

**The norm and the rank.** For a nonzero matrix,

$$
N=0\iff\det M=0\iff\operatorname{rank}M=1.
$$

The zero matrix is the only singular matrix of rank zero; it is the apex of the cone and the image of the zero biquaternion. Every other zero divisor is rank one.

## The Coefficients of the Factorisation

**The four coefficients.** For $M=uv^{\mathsf T}$ with $u=(u_1,u_2)^{\mathsf T}$ and $v=(v_1,v_2)^{\mathsf T}$,

$$
Q_t=\tfrac12 v^{\mathsf T}u,\qquad
Q_k=\tfrac{i}{2}\,v^{\mathsf T}\sigma_k u\quad(k=x,y,z),
$$

and in entries

$$
Q_x=\tfrac{i}{2}(u_1v_2+u_2v_1),\qquad
Q_y=\tfrac12(u_2v_1-u_1v_2),\qquad
Q_z=\tfrac{i}{2}(u_1v_1-u_2v_2).
$$

The scalar part is half the contraction of the two vectors, and the three vector coefficients are the three contractions with the Pauli matrices. The factor $i$ is the same factor that makes $\mathsf M_2(\vec e_k)=-i\sigma_k$: the vector coefficients are read on the anti-Hermitian basis matrices $-i\sigma_k$, not on the Hermitian Pauli matrices.

**The scaling.** The reciprocal scaling $u\mapsto\lambda u$, $v\mapsto\lambda^{-1}v$ leaves $uv^{\mathsf T}$ fixed and leaves every $Q_\mu$ fixed, because each formula is bilinear in the pair. The coefficients are therefore functions of the matrix, not of the chosen factorisation.

## The Two Strata

**The trace splits the cone into two pieces.**

| Stratum | Condition | Biquaternion reading | Real dimension |
|---|---|---|---|
| pure | $v^{\mathsf T}u=0$ | $Q_t=0$, nilpotent | $4$ |
| non-pure | $v^{\mathsf T}u\neq0$ | $Q_t\neq0$, scalar multiple of an idempotent | $6$ |

The two conditions are exclusive and exhaustive on the nonzero cone, and they are the matrix form of the split of the null cone into its pure and non-pure strata.

**The pure stratum.** If $v^{\mathsf T}u=0$ then $M^2=u(v^{\mathsf T}u)v^{\mathsf T}=0$. The matrix is nilpotent, its trace is zero, and its only eigenvalue is zero. Conversely, a rank-one nilpotent has trace zero, hence $v^{\mathsf T}u=0$. The pure stratum is therefore exactly the set of nonzero nilpotents.

**The non-pure stratum.** If $v^{\mathsf T}u\neq0$ then

$$
P=\frac{uv^{\mathsf T}}{v^{\mathsf T}u}
$$

satisfies $P^2=P$, $\operatorname{Tr}P=1$ and $\det P=0$. It is a rank-one idempotent, hence a projector onto the line $\mathbb{C}u$ along the kernel $\ker v^{\mathsf T}$. Conversely, every rank-one idempotent has trace one and is of this form. The non-pure stratum is the set of nonzero complex multiples of rank-one idempotents: the scale is $v^{\mathsf T}u$, and the idempotent is the scale-free part.

**The pure stratum as a graph of duality.** The condition $v^{\mathsf T}u=0$ says that the line $\mathbb{C}u$ is the kernel of the covector $v^{\mathsf T}$, so the point $[u]$ and the covector line $[v]$ determine each other. The pure stratum is the graph of the projective duality $[u]\mapsto[u^{\perp}]$, a conic in $\mathbb{P}^1(\mathbb{C})\times\mathbb{P}^1(\mathbb{C})$. It is the cone over that conic, of real dimension four: one complex dimension for the conic and one for the complex scale.

**The idempotents as pairs of lines.** A rank-one idempotent is determined by its image line and its kernel line, a pair of distinct lines, an open dense subset of $\mathbb{P}^1(\mathbb{C})\times\mathbb{P}^1(\mathbb{C})$, of complex dimension two. Adding the complex scale gives the non-pure stratum of complex dimension three, real dimension six. The two strata have different dimensions, and the pure stratum is the boundary of the non-pure one in the cone.

## The Annihilators

**The left and right annihilators.** For $M=uv^{\mathsf T}$,

$$
\{X:XM=0\}=\{X:Xu=0\},\qquad
\{X:MX=0\}=\{X:v^{\mathsf T}X=0\}.
$$

Each is a two-dimensional subspace of $M_2(\mathbb{C})$, and each is a maximal left or right ideal.

*Proof.* $XM=Xuv^{\mathsf T}$ vanishes exactly when $Xu=0$, because $v\neq0$. The solutions of $Xu=0$ form the set of matrices whose rows lie in the annihilator line $u^{\perp}\subset(\mathbb{C}^2)^{*}$, a two-dimensional left ideal. The right statement is the transpose.

**The ideals generated.** The left ideal generated by $M$ is

$$
\mathbb{B}M=\{Xuv^{\mathsf T}:X\in M_2(\mathbb{C})\}=\{wv^{\mathsf T}:w\in\mathbb{C}^2\},
$$

the set of matrices whose rows lie in $\mathbb{C}v^{\mathsf T}$; it is the minimal left ideal of the covector $v$ and has dimension two. The right ideal generated by $M$ is

$$
M\mathbb{B}=\{uv^{\mathsf T}X:X\in M_2(\mathbb{C})\}=\{uw^{\mathsf T}:w\in\mathbb{C}^2\},
$$

the set of matrices whose image lies in $\mathbb{C}u$; it is the minimal right ideal of the vector $u$. The left ideal is attached to the covector and the right ideal to the vector of the factorisation.

**The ranks of the one-sided operators.** Left multiplication by $M$ is the linear map $L_M:X\mapsto MX$ on the four-dimensional algebra. Its kernel is the right annihilator $\{X:v^{\mathsf T}X=0\}$, of dimension two, so its rank is two. Right multiplication $R_M:X\mapsto XM$ has kernel the left annihilator $\{X:Xu=0\}$, also of dimension two, and rank two. The rank-one element is therefore rank one as an element and rank two as an operator on the regular module; the two ranks are different invariants and are not to be confused.

**The annihilator pairing.** The left annihilator is the minimal left ideal of the covector line $u^{\perp}$, and the right annihilator is the minimal right ideal of the vector line $\ker v^{\mathsf T}$. The pair of annihilators is the Peirce data of the rank-one element: the image line, the kernel line, and their two annihilators.

## The Determinantal Variety

**The variety.** The set

$$
\mathcal{D}=\{M\in M_2(\mathbb{C}):\det M=0\}
$$

is the determinantal variety of rank at most one. It is the zero set of the single polynomial $\det$, of degree two, and it is a complex cone of complex dimension three with apex at the origin.

**The cone over the Segre quadric.** Every nonzero point of $\mathcal{D}$ is $uv^{\mathsf T}$ with $u,v\neq0$, and the pair is defined up to reciprocal scaling. Projectivising,

$$
\mathbb{P}(\mathcal{D})=\{[uv^{\mathsf T}]:u,v\neq0\}\cong\mathbb{P}^1\times\mathbb{P}^1,
$$

the Segre quadric in $\mathbb{P}^3$. The two rulings are the two families of lines: fixing $u$ and varying $v$ gives the row family, and fixing $v$ and varying $u$ gives the column family. The two rulings are the two chiralities of the rank-one elements, and they meet in a single point for each pair of a line and a covector.

**The singular locus.** The cone is smooth away from the apex. At the apex the gradient of the determinant vanishes, and the tangent cone is the whole variety. The apex is the image of the zero biquaternion, and it is the only point where the rank drops below one.

**The two strata in the projective picture.** The pure stratum is the graph of the projective duality, a conic of bidegree $(1,1)$ inside $\mathbb{P}^1\times\mathbb{P}^1$; the non-pure stratum is its complement, an open dense set. The closure of the non-pure stratum is the whole quadric, and the pure stratum is its boundary.

**The biquaternion reading.** The determinantal variety is the image of the null cone. Its two strata are the pure and non-pure parts of the cone; its apex is the zero element; its projectivisation is the Segre quadric, of real dimension four, and the link of the cone is an $S^1$-bundle over it, of real dimension five; the two rulings are the two spinor directions. The statement is the matrix form of the topology of the zero-divisor cone in *The Topology of the Zero-Divisor Cone*.

## The Nilpotents and the Jordan Block

**The Jordan form.** A nonzero nilpotent is a rank-one matrix with trace zero. It has only the eigenvalue zero, and its minimal polynomial is $X^2$; it is therefore conjugate to the single Jordan block

$$
J=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
$$

The two standard nilpotents $E_{12}$ and $E_{21}$ are the two off-diagonal blocks, and every nilpotent is a conjugate of one of them. The conjugating matrix is the one that sends the image line of the nilpotent to the first coordinate line and its kernel to the second.

**The Peirce corners.** The rank-one idempotents $E_{11}$ and $E_{22}$ are the two diagonal corners; the nilpotents $E_{12}$ and $E_{21}$ are the two off-diagonal corners. The four together are the standard matrix units. The rank-one elements of the algebra are therefore of two kinds: the idempotent corners, which are projectors, and the nilpotent corners, which are the off-diagonal units.

**The products of two nilpotents.** For the standard pair,

$$
E_{12}E_{21}=E_{11},\qquad E_{21}E_{12}=E_{22},\qquad
E_{12}^2=E_{21}^2=0.
$$

The product of the two nilpotents is the idempotent of the opposite corner, and every rank-one idempotent arises this way after a change of matrix units. The statement is the matrix form of the fact that every nontrivial idempotent is a product of two nilpotents, proved in *$M_2(\mathbb{C})$ Representation : The Peirce Coordinates and the Matrix Units*.

**The scaled idempotent.** A rank-one idempotent is not nilpotent: $P^2=P$ and $P\neq0$. It is nevertheless a zero divisor, because $P(e_t-P)=0$ and $e_t-P\neq0$; its annihilator is the ideal of the complementary line. The distinction between the idempotent and the nilpotent is the distinction between the non-pure and the pure strata.

## Summary

A nonzero singular matrix has rank one and factorises as $uv^{\mathsf T}$, uniquely up to reciprocal scaling. Its trace is $v^{\mathsf T}u$, and the trace splits the cone into the pure stratum $v^{\mathsf T}u=0$ of nilpotents, of real dimension four, and the non-pure stratum $v^{\mathsf T}u\neq0$ of scaled idempotents, of real dimension six. The left and right annihilators are the ideals of the complementary line and covector, and the one-sided operators have rank two. The determinantal variety is the cone over the Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$, with apex at the zero matrix; the pure stratum is the incidence line and the non-pure stratum its complement. Every nilpotent is conjugate to the Jordan block.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $uv^{\mathsf T}$ | the rank-one matrix of the vectors $u,v$ |
| $v^{\mathsf T}u$ | its trace, twice the scalar part |
| $P=uv^{\mathsf T}/(v^{\mathsf T}u)$ | the rank-one idempotent |
| $\mathcal{D}=\{\det=0\}$ | the determinantal variety |
| $\mathbb{P}^1\times\mathbb{P}^1$ | the Segre quadric, the projectivised cone |
| $J=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ | the Jordan block of the nilpotents |
| $E_{ij}$ | the matrix units, the four Peirce corners |

## Further Reading

- [The N-Degenerate Sector](the-n-degenerate-sector.html), for the null cone and its strata
- [Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html), for the nilpotent cone
- [Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the rank-one elements and the corners
- [The Topology of the Zero-Divisor Cone](the-topology-of-the-zero-divisor-cone.html), for the link and its topology
- [$M_2(\mathbb{C})$ Representation : The Peirce Coordinates and the Matrix Units](m2c-representation-the-peirce-coordinates-and-the-matrix-units.html), for the matrix units
- [$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm](m2c-representation-trace-determinant-and-the-biquaternion-norm.html), for the determinant
- [The Determinant and Alternating Forms](the-determinant-and-alternating-forms.html), for determinantal varieties
