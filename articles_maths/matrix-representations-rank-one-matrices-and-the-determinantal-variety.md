# __Matrix Representations : Rank-One Matrices and the Determinantal Variety__

## Introduction

The zero divisors of the biquaternion algebra are the matrices of rank one in the entry model. In the regular model each of them is doubled into a matrix of rank two. The set of all of them is the determinantal variety, a cone over the Segre quadric, and its two strata are the nilpotents and the scaled idempotents.

This article develops the factorisation, the coefficients, the two strata, the annihilators, the determinantal variety and the nilpotent corner. It is the article in which the null cone of *Matrix Representations : Trace, Determinant and the Biquaternion Norm* becomes a projective variety with two rulings.

**Conventions.** The algebra and the displays are those of *Matrix Representations : The Models and the Change of Frame*. The element is $\tilde Q=Q_te_t+\vec Q$, with $B=\mathsf M_2(\tilde Q)$, $N=\det B$ and regular matrix $L=I_2\otimes B$. In the Peirce frame the regular matrix is the block matrix of two copies of $B$.

**Boundaries.** The matrix statements are *Matrix Representations : Rank-One Matrices and the Determinantal Variety*; the cone and its topology are *The Topology of the Zero-Divisor Cone* and *The Null Cone and the Zero Divisors*; the nilpotents are *Nilpotents*; the Jordan form is *Matrix Representations : The Jordan Basis and the Jordanising Matrix*.

## Common Aspects

### The Factorisation

**The theorem in the entry model.** A nonzero $2\times2$ matrix has rank one exactly when
$$
M=uv^{\mathsf T}
$$
for nonzero vectors $u,v\in\mathbb{C}^2$. The pair is determined up to the reciprocal scaling
$$
u\longmapsto\lambda u,\qquad v\longmapsto\lambda^{-1}v,\qquad \lambda\in\mathbb{C}^{\times}.
$$

*Proof.* If $M=uv^{\mathsf T}$ with both vectors nonzero, every column is a multiple of $u$, so the rank is one. Conversely, if the rank is one, the two columns are proportional to a nonzero vector $u$; writing them as $uv_1$ and $uv_2$ gives $v=(v_1,v_2)$. A second pair with the same product satisfies $u'=\lambda u$ and $v'=\lambda^{-1}v$.

**The theorem in the regular model.** A nonzero matrix in the regular image has rank two exactly when it is the double of such a product:
$$
M=C_{\Pi}\operatorname{diag}(uv^{\mathsf T},uv^{\mathsf T})C_{\Pi}^{-1}
=u_1v_1^{\mathsf T}+u_2v_2^{\mathsf T},
$$
with $u_1=(u,0)$, $v_1=(v,0)$, $u_2=(0,u)$, $v_2=(0,v)$. The rank is twice the rank of the block, and the pair is unique up to the same scaling.

**The invariants.**
$$
\operatorname{Tr}(uv^{\mathsf T})=v^{\mathsf T}u,\qquad
\det(uv^{\mathsf T})=0,
\qquad
\operatorname{Tr}M=2v^{\mathsf T}u,\qquad
\det M=0 .
$$
The determinant vanishes identically, so every rank-one matrix is singular. The trace is the contraction of the two vectors, and it is the only invariant of the pair beyond the scaling. In biquaternion terms,
$$
2Q_t=v^{\mathsf T}u,\qquad N=0 .
$$

**The norm and the rank.**
$$
N=0\iff\det M=0\iff\operatorname{rank}M=1\ \text{(entry model)},
$$
and $\operatorname{rank}L=2$ in the regular model. The zero matrix is the only singular matrix of rank zero; every other zero divisor is rank one in the entry model and rank two in the regular model.

### The Coefficients

**The four coefficients.** For $M=uv^{\mathsf T}$ with $u=(u_1,u_2)^{\mathsf T}$ and $v=(v_1,v_2)^{\mathsf T}$,
$$
Q_t=\tfrac12v^{\mathsf T}u,\qquad
Q_k=\tfrac{i}{2}v^{\mathsf T}\sigma_k u\quad(k=x,y,z),
$$
and in entries
$$
Q_x=\tfrac{i}{2}(u_1v_2+u_2v_1),\qquad
Q_y=\tfrac12(u_2v_1-u_1v_2),\qquad
Q_z=\tfrac{i}{2}(u_1v_1-u_2v_2).
$$
The scalar part is half the contraction, and the three vector coefficients are the contractions with the Pauli matrices. The factor $i$ is the factor that makes $\mathsf M_2(\vec e_k)=-i\sigma_k$.

**The scaling.** The reciprocal scaling leaves $uv^{\mathsf T}$ fixed and leaves every $Q_\mu$ fixed, because each formula is bilinear. The coefficients are functions of the matrix, not of the chosen factorisation.

**The regular display.** The same four numbers are the coefficients of the regular matrix, because the block is the entry-model matrix of the element. The doubling changes the trace and the rank, not the coefficients.

### The Two Strata

**The trace splits the cone.**

| Stratum | Condition | Algebra reading | Real dimension |
|---|---|---|---|
| pure | $v^{\mathsf T}u=0$ | $Q_t=0$, nilpotent | $4$ |
| non-pure | $v^{\mathsf T}u\neq0$ | $Q_t\neq0$, scalar multiple of an idempotent | $6$ |

The conditions are exclusive and exhaustive on the nonzero cone.

**The pure stratum.** If $v^{\mathsf T}u=0$ then
$$
M^2=u(v^{\mathsf T}u)v^{\mathsf T}=0,
$$
so $M$ is nilpotent of trace zero and only eigenvalue zero. Conversely a rank-one nilpotent has trace zero and hence $v^{\mathsf T}u=0$. The pure stratum is exactly the set of nonzero nilpotents.

**The non-pure stratum.** If $v^{\mathsf T}u\neq0$, the matrix
$$
P=\frac{uv^{\mathsf T}}{v^{\mathsf T}u}
$$
satisfies $P^2=P$, $\operatorname{Tr}P=1$ and $\det P=0$. It is the projector onto the line $\mathbb{C}u$ along the kernel $\ker v^{\mathsf T}$. Every rank-one idempotent arises this way, and the non-pure stratum is the set of nonzero complex multiples of these idempotents.

**The dimensions.** A rank-one idempotent is a pair of distinct lines, an open dense subset of $\mathbb{P}^1\times\mathbb{P}^1$ of complex dimension two; adding the complex scale gives complex dimension three, real dimension six. The pure stratum is the graph of the projective duality $[u]\mapsto[u^{\perp}]$, a conic of complex dimension one; adding the scale gives complex dimension two, real dimension four. The pure stratum is the boundary of the non-pure one.

**The regular display.** The doubling does not change the projective variety or the dimensions: the regular cone is the same cone with every matrix doubled, and the two strata keep real dimensions four and six.

### The Determinantal Variety

**The variety.** In the entry model,
$$
\mathcal{D}=\{M\in M_2(\mathbb{C}):\det M=0\}
$$
is the zero set of the determinant, a complex cone of complex dimension three with apex at the origin. In the regular image,
$$
\mathcal{D}_L=\{M\in M_4(\mathbb{C})_{\mathbb{B}_L}:\det M=0\}
$$
is the zero set of the determinant of degree four, the same cone with every point doubled.

**The Segre quadric.** Every nonzero point is $uv^{\mathsf T}$ with $u,v\neq0$, and the pair is defined up to reciprocal scaling. Projectivising,
$$
\mathbb{P}(\mathcal{D})\cong\mathbb{P}^1\times\mathbb{P}^1\subset\mathbb{P}^3,
$$
the Segre quadric. Its two rulings are the row family, with $u$ fixed and $v$ varying, and the column family, with $v$ fixed and $u$ varying. They are the two chiralities of the rank-one elements.

**The singular locus.** The cone is smooth away from the apex. At the apex the gradient of the determinant vanishes and the tangent cone is the whole variety. The apex is the image of the zero element, and it is the only point where the rank drops below one in the entry model or below two in the regular model.

**The two strata in the projective picture.** The pure stratum is the graph of the projective duality, a conic of bidegree $(1,1)$ inside $\mathbb{P}^1\times\mathbb{P}^1$; the non-pure stratum is its complement, an open dense set. The closure of the non-pure stratum is the whole quadric, and the pure stratum is its boundary.

**The link.** The projectivisation has real dimension four, and the link of the cone is an $S^1$-bundle over it, of real dimension five. The two rulings are the two spinor directions of *Matrix Representations : Peirce Coordinates, Matrix Units and the Spinor Planes*.

### The Nilpotents and the Jordan Block

**The Jordan form.** A nonzero nilpotent is a rank-one matrix of trace zero. It has only the eigenvalue zero and its minimal polynomial is $X^2$, so it is conjugate to
$$
J=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
$$
In the regular display the nilpotent is the double
$$
J\oplus J=
\begin{pmatrix}
0&1&0&0\\
0&0&0&0\\
0&0&0&1\\
0&0&0&0
\end{pmatrix},
$$
two blocks of size two, not one block of size four, because the two copies are independent.

**The Peirce corners.** The rank-one idempotents $E_{11}$ and $E_{22}$ are the diagonal corners; the nilpotents $E_{12}$ and $E_{21}$ are the off-diagonal corners. The four together are the standard matrix units. The rank-one elements are therefore of two kinds: the idempotent corners, which are projectors, and the nilpotent corners, which are the off-diagonal units.

**The products of two nilpotents.**
$$
E_{12}E_{21}=E_{11},\qquad
E_{21}E_{12}=E_{22},\qquad
E_{12}^2=E_{21}^2=0 .
$$
The product of the two nilpotents is the idempotent of the opposite corner, and every nontrivial idempotent arises this way after a change of matrix units.

**The scaled idempotent.** A rank-one idempotent is not nilpotent: $P^2=P$ and $P\neq0$. It is nevertheless a zero divisor, because $P(e_t-P)=0$ and $e_t-P\neq0$; its annihilator is the ideal of the complementary line. The distinction between idempotent and nilpotent is the distinction between the non-pure and the pure strata.

## The Coefficient Frame

**The coefficient display.** In the coefficient frame the rank-one matrix is
$$
M_{\mathrm{coef}}=C_{\Pi}\operatorname{diag}(uv^{\mathsf T},uv^{\mathsf T})C_{\Pi}^{-1},
$$
and its first column is the coefficient column
$$
[Q]=\bigl(\tfrac12v^{\mathsf T}u,\ \tfrac{i}{2}v^{\mathsf T}\sigma_xu,\ \tfrac{i}{2}v^{\mathsf T}\sigma_yu,\ \tfrac{i}{2}v^{\mathsf T}\sigma_zu\bigr)^{\mathsf T}.
$$
The four coefficients are functions of the element, not of the display; the coefficient frame carries them in one column and the Peirce frame in two equal blocks.

**The cone.** The determinant is $N^2=0$ in every frame, and the determinantal variety is the same cone. The projectivisation is still the Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$, because the Peirce change is a linear isomorphism and commutes with the scale. The two rulings are the two spinor directions of *Matrix Representations : Peirce Coordinates, Matrix Units and the Spinor Planes*, and they are visible in the coefficient frame as the two families of coefficient columns.

**The doubling.** The coefficient matrix is full, but it is the conjugate of the block matrix $\operatorname{diag}(uv^{\mathsf T},uv^{\mathsf T})$. The rank is two, the trace is $2v^{\mathsf T}u$, and the determinant is zero; the block structure is hidden, not changed.

## The Entry Model

**The factorisation.** A nonzero $2\times2$ matrix has rank one exactly when $M=uv^{\mathsf T}$ for nonzero vectors $u,v\in\mathbb{C}^2$, uniquely up to $u\mapsto\lambda u$, $v\mapsto\lambda^{-1}v$. If $M=uv^{\mathsf T}$, every column is a multiple of $u$; conversely, two proportional columns give the pair.

**The coefficients and the trace.** With $u=(u_1,u_2)^{\mathsf T}$ and $v=(v_1,v_2)^{\mathsf T}$,
$$
Q_t=\tfrac12v^{\mathsf T}u,\qquad
Q_x=\tfrac{i}{2}(u_1v_2+u_2v_1),\qquad
Q_y=\tfrac12(u_2v_1-u_1v_2),\qquad
Q_z=\tfrac{i}{2}(u_1v_1-u_2v_2),
$$
and $\operatorname{Tr}M=v^{\mathsf T}u=2Q_t$, $\det M=0$. The factor $i$ makes $\mathsf M_2(\vec e_k)=-i\sigma_k$; the reciprocal scaling leaves every coefficient fixed.

**The strata.** The trace splits the cone. The pure stratum $v^{\mathsf T}u=0$ is the set of nonzero nilpotents, of real dimension four; the non-pure stratum $v^{\mathsf T}u\neq0$ is the set of nonzero complex multiples of rank-one idempotents, of real dimension six. The pure stratum is the boundary of the non-pure one in the projective quadric.

**The rank.** The rank is one for every nonzero singular matrix and zero only at $M=0$. The one-sided operators have rank two, so the entry element has rank one while its left and right multiplications have rank two; the doubling in the regular model makes the two ranks agree.

## The Peirce Frame

### The Annihilators

**The left and right annihilators.** In the entry model,
$$
\{X:XM=0\}=\{X:Xu=0\},\qquad
\{X:MX=0\}=\{X:v^{\mathsf T}X=0\}.
$$
Each is a two-dimensional subspace of $M_2(\mathbb{C})$, and each is a maximal one-sided ideal.

**The regular display.**
$$
\{X\in M_4(\mathbb{C}):XM=0\}=\{X:Xu_1=0,\ Xu_2=0\},
$$
of dimension eight in the ambient algebra and dimension two inside the image; the right annihilator is the transpose statement. The ambient annihilator is larger, because the ambient algebra has more room to annihilate the two vectors.

**The ideals generated.** The left ideal generated by $M$ is
$$
M_2(\mathbb{C})M=\{wv^{\mathsf T}:w\in\mathbb{C}^2\},
$$
the matrices whose rows lie in $\mathbb{C}v^{\mathsf T}$; it is the minimal left ideal of the covector $v$, of dimension two. The right ideal is
$$
MM_2(\mathbb{C})=\{uw^{\mathsf T}:w\in\mathbb{C}^2\},
$$
the matrices whose image lies in $\mathbb{C}u$; it is the minimal right ideal of the vector $u$. In the regular display both ideals are doubled.

**The ranks of the one-sided operators.** Left multiplication by $M$ has kernel the right annihilator, of dimension two, so its rank is two. Right multiplication has kernel the left annihilator, also of dimension two, and rank two. In the entry model the element has rank one but its one-sided operators have rank two; in the regular model the element has rank two and the operators have rank two, so the doubling makes the two ranks agree.

**The Peirce reading.** The left annihilator is the minimal left ideal of the covector line $u^{\perp}$, and the right annihilator is the minimal right ideal of the vector line $\ker v^{\mathsf T}$. The pair of annihilators is the Peirce data of the rank-one element: the image line, the kernel line, and their annihilators.

## Summary

A nonzero singular matrix has rank one in the entry model and rank two in the regular model, and factorises as $uv^{\mathsf T}$ or as its double, uniquely up to reciprocal scaling. Its trace is $v^{\mathsf T}u$, doubled in the regular model, and the trace splits the cone into the pure stratum $v^{\mathsf T}u=0$ of nilpotents, of real dimension four, and the non-pure stratum $v^{\mathsf T}u\neq0$ of scaled idempotents, of real dimension six. The annihilators are the minimal ideals of the complementary line and covector, and the one-sided operators have rank two in both displays. The determinantal variety is the cone over the Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$, with apex at the zero matrix; the pure stratum is the incidence conic and the non-pure stratum its complement. Every nilpotent is conjugate to the Jordan block, doubled in the regular display.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M=uv^{\mathsf T}$ | the rank-one factorisation |
| $v^{\mathsf T}u$ | the trace, the contraction |
| $N=0$ | the singularity condition |
| pure stratum | $v^{\mathsf T}u=0$, the nilpotents |
| non-pure stratum | $v^{\mathsf T}u\neq0$, the scaled idempotents |
| $\mathcal{D}$ | the determinantal variety |
| $\mathbb{P}^1\times\mathbb{P}^1$ | the Segre quadric |
| $J$ | the Jordan block |

## Further Reading

- [Matrix Representations : Trace, Determinant and the Biquaternion Norm](matrix-representations-trace-determinant-and-the-biquaternion-norm.html), for the null cone
- [Matrix Representations : The Jordan Basis and the Jordanising Matrix](matrix-representations-the-jordan-basis-and-the-jordanising-matrix.html), for the nilpotent form
- [Matrix Representations : Peirce Coordinates, Matrix Units and the Spinor Planes](matrix-representations-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the corners
- [Matrix Representations : The Models and the Change of Frame](matrix-representations-the-models-and-the-change-of-frame.html), for the displays
- [The Topology of the Zero-Divisor Cone](the-topology-of-the-zero-divisor-cone.html), for the topology