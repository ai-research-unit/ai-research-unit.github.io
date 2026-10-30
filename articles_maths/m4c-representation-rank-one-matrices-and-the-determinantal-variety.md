# __$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : Rank-One Matrices and the Determinantal Variety__

## Introduction

The zero divisors of the biquaternion algebra are the nonzero elements of vanishing quaternionic norm. In the regular model they are the nonzero singular matrices, and a nonzero singular matrix in the image has rank two: it is the direct sum of two identical rank-one blocks. Every one of them is the double of an outer product of two vectors, and the two vectors carry the two pieces of data the algebra sees: a direction and a covector.

This article develops the factorisation, the two strata of the regular determinantal variety, the annihilators and the geometry of the cone. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety*. The title is inherited from the $2\times2$ article; the object in the regular model is the rank-two double of a rank-one matrix.

**Conventions.** The algebra and the model are those of *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant*. The norm is $N=Q_t^2+B^2$, and $\det\mathsf{M}_4^{L}(\tilde Q)=N^2$. A vector of $\mathbb{C}^2$ is a column $u$, a covector is a row $v^{\mathsf T}$, and $uv^{\mathsf T}$ is the matrix of entries $(uv^{\mathsf T})_{ij}=u_iv_j$. The Peirce basis identifies the image with the block matrices $\operatorname{diag}(A,A)$.

**Boundaries.** The null cone and its stratification are *The N-Degenerate Sector*; the nilpotents are *Nilpotents*; the rank-one elements and the Peirce corners are *The Peirce Decomposition of the Biquaternion Algebra*; the singular matrices as a determinantal variety are also treated in *The Determinant and Alternating Forms*.

**Frame.** Unless a basis is named, matrices are written in the canonical frame of *Conventions of the Representations*, §*The Matrix Models*, where $\mathsf{M}_4^{L}(\tilde Q)=I_2\otimes\mathsf{M}_2(\tilde Q)$. The coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ is the conjugate display: $\mathsf M_{4,\mathrm{coef}}^{L}=S\,(I_2\otimes\mathsf M_2)\,S^{-1}$, with $S$ the change of *The Product, the Trace and the Determinant*.

## The Factorisation

**Theorem.** A nonzero matrix $M\in M_4(\mathbb{C})_{\mathbb{B},L}$ has rank two exactly when there are nonzero vectors $u,v\in\mathbb{C}^2$ with
$$
M=S\operatorname{diag}(uv^{\mathsf T},uv^{\mathsf T})S^{-1}.
$$
Equivalently, in the fixed basis, $M=u_1v_1^{\mathsf T}+u_2v_2^{\mathsf T}$ with
$$
u_1=(u,0),\quad v_1=(v,0),\quad u_2=(0,u),\quad v_2=(0,v).
$$
The pair $(u,v)$ is determined up to the reciprocal scaling $u\mapsto\lambda u$, $v\mapsto\lambda^{-1}v$ with $\lambda\in\mathbb{C}^{\times}$.

*Proof.* If $M$ is the double of $uv^{\mathsf T}$ with both vectors nonzero, its rank is twice the rank of $uv^{\mathsf T}$, hence two. Conversely, if the rank is two, the block form $M=\operatorname{diag}(A,A)$ has $\operatorname{rank}A=1$, so $A=uv^{\mathsf T}$, and the pair is unique up to reciprocal scaling by the $2\times2$ theorem. The decomposition into two rank-one matrices is the splitting of the two copies.

**The two invariants of the factorisation.**
$$
\operatorname{Tr}(uv^{\mathsf T})=v^{\mathsf T}u,\qquad
\det(uv^{\mathsf T})=0.
$$
In the regular model the trace doubles,
$$
\operatorname{Tr}M=2\,v^{\mathsf T}u,\qquad
\det M=0.
$$
The determinant vanishes identically, so every rank-two matrix in the image is singular. The trace is twice the contraction of the two vectors, and it is the only invariant of the pair beyond the scaling. In biquaternion terms,
$$
M=\mathsf{M}_4^{L}(\tilde Q)\quad\Longrightarrow\quad
4Q_t=2\,v^{\mathsf T}u,\qquad N=0.
$$

**The norm and the rank.** For a nonzero matrix in the image,
$$
N=0\iff\det M=0\iff\operatorname{rank}M=2.
$$
The zero matrix is the only singular matrix of rank zero; it is the apex of the cone and the image of the zero biquaternion. Every other zero divisor has rank two, twice the rank of its $2\times2$ block.

## The Coefficients of the Factorisation

**The four coefficients.** For $A=uv^{\mathsf T}$ with $u=(u_1,u_2)^{\mathsf T}$ and $v=(v_1,v_2)^{\mathsf T}$,
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
The formulas are those of the $2\times2$ model, because the block $A$ is the $2\times2$ matrix of the element. The scalar part is half the contraction of the two vectors, and the three vector coefficients are the three contractions with the Pauli matrices. The factor $i$ is the same factor that makes $\mathsf{M}_4^{L}(\vec e_k)=-i\Sigma_k$.

**The scaling.** The reciprocal scaling $u\mapsto\lambda u$, $v\mapsto\lambda^{-1}v$ leaves $uv^{\mathsf T}$ fixed and leaves every $Q_\mu$ fixed, because each formula is bilinear in the pair. The coefficients are therefore functions of the matrix, not of the chosen factorisation.

## The Two Strata

**The trace splits the cone into two pieces.**

| Stratum | Condition | Biquaternion reading | Real dimension |
|---|---|---|---|
| pure | $v^{\mathsf T}u=0$ | $Q_t=0$, nilpotent | $4$ |
| non-pure | $v^{\mathsf T}u\neq0$ | $Q_t\neq0$, scalar multiple of an idempotent | $6$ |

The two conditions are exclusive and exhaustive on the nonzero cone, and they are the matrix form of the split of the null cone into its pure and non-pure strata. The dimensions are those of the $2\times2$ strata: the doubling of the block does not add parameters.

**The pure stratum.** If $v^{\mathsf T}u=0$ then $A^2=u(v^{\mathsf T}u)v^{\mathsf T}=0$, so $M^2=\operatorname{diag}(A^2,A^2)=0$. The matrix is nilpotent, its trace is zero, and its only eigenvalue is zero. Conversely, a rank-two nilpotent in the image has trace zero, hence $v^{\mathsf T}u=0$. The pure stratum is therefore exactly the set of nonzero nilpotents, and each is the double of a rank-one nilpotent.

**The non-pure stratum.** If $v^{\mathsf T}u\neq0$ then
$$
P=\frac{uv^{\mathsf T}}{v^{\mathsf T}u}
$$
satisfies $P^2=P$, $\operatorname{Tr}P=1$ and $\det P=0$. Its double $S\operatorname{diag}(P,P)S^{-1}$ satisfies $P_L^2=P_L$, $\operatorname{Tr}P_L=2$ and $\operatorname{rank}P_L=2$. It is a rank-two idempotent, the projector onto the two-dimensional space $\mathbb{C}u\oplus\mathbb{C}u$ along the kernel $\ker v^{\mathsf T}\oplus\ker v^{\mathsf T}$. The non-pure stratum is the set of nonzero complex multiples of these idempotents.

**The pure stratum as a graph of duality.** The condition $v^{\mathsf T}u=0$ says that the line $\mathbb{C}u$ is the kernel of the covector $v^{\mathsf T}$, so the point $[u]$ and the covector line $[v]$ determine each other. The pure stratum is the graph of the projective duality $[u]\mapsto[u^{\perp}]$, a conic in $\mathbb{P}^1(\mathbb{C})\times\mathbb{P}^1(\mathbb{C})$. It is the cone over that conic, of real dimension four. The regular model doubles the vector $u$ and the covector $v$, but the parameter line and the conic are the same.

**The idempotents as pairs of lines.** A rank-two idempotent in the image is determined by its image plane and its kernel plane, each the double of a line. The pair of lines is an open dense subset of $\mathbb{P}^1(\mathbb{C})\times\mathbb{P}^1(\mathbb{C})$, of complex dimension two. Adding the complex scale gives the non-pure stratum of complex dimension three, real dimension six. The two strata have different dimensions, and the pure stratum is the boundary of the non-pure one in the cone.

## The Annihilators

**The left and right annihilators.** For $M$ the double of $uv^{\mathsf T}$,
$$
\{X\in M_4(\mathbb{C}):XM=0\}=\{X:Xu_1=0,\ Xu_2=0\},\qquad
\{X\in M_4(\mathbb{C}):MX=0\}=\{X:v_1^{\mathsf T}X=0,\ v_2^{\mathsf T}X=0\}.
$$
Each is an eight-dimensional subspace of $M_4(\mathbb{C})$, and inside the image each is a two-dimensional subspace.

*Proof.* $XM=X(u_1v_1^{\mathsf T}+u_2v_2^{\mathsf T})$ vanishes exactly when $Xu_1=Xu_2=0$, because $v_1,v_2\neq0$. The solutions form the set of matrices whose rows lie in the annihilator of the two-dimensional space spanned by $u_1,u_2$, of dimension $16-8=8$. Intersecting with the four-dimensional image gives dimension two. The right statement is the transpose.

**The ideals generated.** The left ideal generated by $M$ inside the image is
$$
M_4(\mathbb{C})_{\mathbb{B},L}\,M=\{X M:X\in M_4(\mathbb{C})_{\mathbb{B},L}\},
$$
the set of doubled matrices whose rows lie in $\mathbb{C}v^{\mathsf T}$; it is the minimal left ideal of the covector $v$, doubled, and has complex dimension two. The right ideal generated by $M$ is
$$
M\,M_4(\mathbb{C})_{\mathbb{B},L}=\{M X:X\in M_4(\mathbb{C})_{\mathbb{B},L}\},
$$
the set of doubled matrices whose image lies in $\mathbb{C}u$; it is the minimal right ideal of the vector $u$, doubled.

**The ranks of the one-sided operators.** Left multiplication by $M$ is the linear map $L_M:X\mapsto MX$ on the four-dimensional image. Its kernel is the right annihilator inside the image, of dimension two, so its rank is two. Right multiplication $R_M:X\mapsto XM$ has kernel the left annihilator inside the image, also of dimension two, and rank two. The rank-two element is therefore rank two as an element and rank two as an operator on the regular module; the doubling makes the two ranks agree, unlike the $2\times2$ case.

**The annihilator pairing.** The left annihilator is the minimal left ideal of the covector line $u^{\perp}$, doubled, and the right annihilator is the minimal right ideal of the vector line $\ker v^{\mathsf T}$, doubled. The pair of annihilators is the Peirce data of the rank-two element: the image plane, the kernel plane, and their two annihilators.

## The Determinantal Variety

**The variety.** The set
$$
\mathcal{D}_L=\{M\in M_4(\mathbb{C})_{\mathbb{B},L}:\det M=0\}
$$
is the determinantal variety of the image, of rank at most two. It is the zero set of the single polynomial $\det$, of degree four, and it is a complex cone of complex dimension three with apex at the origin. The ambient variety $\{M\in M_4(\mathbb{C}):\det M=0\}$ is larger, of dimension fifteen; the image meets it in the cone described here.

**The cone over the Segre quadric.** Every nonzero point of $\mathcal{D}_L$ is the double of $uv^{\mathsf T}$ with $u,v\neq0$, and the pair is defined up to reciprocal scaling. Projectivising,
$$
\mathbb{P}(\mathcal{D}_L)=\{[uv^{\mathsf T}]:u,v\neq0\}\cong\mathbb{P}^1\times\mathbb{P}^1,
$$
the Segre quadric in $\mathbb{P}^3$, with every point doubled in the regular model. The two rulings are the two families of lines: fixing $u$ and varying $v$ gives the row family, and fixing $v$ and varying $u$ gives the column family. The two rulings are the two chiralities of the rank-one blocks.

**The singular locus.** The cone is smooth away from the apex. At the apex the gradient of the determinant vanishes, and the tangent cone is the whole variety. The apex is the image of the zero biquaternion, and it is the only point where the rank drops below two.

**The two strata in the projective picture.** The pure stratum is the graph of the projective duality, a conic of bidegree $(1,1)$ inside $\mathbb{P}^1\times\mathbb{P}^1$; the non-pure stratum is its complement, an open dense set. The closure of the non-pure stratum is the whole quadric, and the pure stratum is its boundary.

**The biquaternion reading.** The determinantal variety is the image of the null cone. Its two strata are the pure and non-pure parts of the cone; its apex is the zero element; its projectivisation is the Segre quadric; the two rulings are the two spinor directions. The statement is the matrix form of the topology of the zero-divisor cone in *The Topology of the Zero-Divisor Cone*, with every cell doubled.

## The Nilpotents and the Jordan Block

**The Jordan form.** A nonzero nilpotent in the image is a rank-two matrix with trace zero. It has only the eigenvalue zero and its minimal polynomial is $X^2$; it is therefore conjugate to the direct sum of two copies of the single Jordan block
$$
J=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
J\oplus J=
\begin{pmatrix}
0&1&0&0\\
0&0&0&0\\
0&0&0&1\\
0&0&0&0
\end{pmatrix}.
$$
The Jordan form has two blocks of size two, not one block of size four, because the two copies are independent. The two standard nilpotents are the doubles of $E_{12}$ and $E_{21}$, and every nilpotent in the image is a conjugate of one of them.

**The Peirce corners.** The rank-two idempotents are the doubles of $E_{11}$ and $E_{22}$; the nilpotents are the doubles of $E_{12}$ and $E_{21}$. The four together are the doubled matrix units. The rank-one blocks of the algebra are therefore of two kinds: the idempotent corners, which are projectors, and the nilpotent corners, which are the off-diagonal units.

**The products of two nilpotents.** For the standard pair,
$$
E_{12}E_{21}=E_{11},\qquad E_{21}E_{12}=E_{22},\qquad
E_{12}^2=E_{21}^2=0.
$$
The product of the two doubled nilpotents is the doubled idempotent of the opposite corner, and every rank-two idempotent arises this way after a change of matrix units. The statement is the matrix form of the fact that every nontrivial idempotent is a product of two nilpotents, proved in *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*.

**The scaled idempotent.** A rank-two idempotent is not nilpotent: $P_L^2=P_L$ and $P_L\neq0$. It is nevertheless a zero divisor, because $P_L(e_t-P_L)=0$; its annihilator is the ideal of the complementary plane. The distinction between the idempotent and the nilpotent is the distinction between the non-pure and the pure strata.

## Summary

A nonzero singular matrix in the regular image has rank two and is the double of a rank-one matrix $uv^{\mathsf T}$, uniquely up to reciprocal scaling. Its trace is twice $v^{\mathsf T}u$, and the trace splits the cone into the pure stratum $v^{\mathsf T}u=0$ of nilpotents, of real dimension four, and the non-pure stratum $v^{\mathsf T}u\neq0$ of scaled idempotents, of real dimension six. The left and right annihilators are the doubled ideals of the complementary line and covector, and the one-sided operators have rank two. The determinantal variety of the image is the cone over the Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$, with apex at the zero matrix; the pure stratum is the incidence line and the non-pure stratum its complement. Every nilpotent is conjugate to two copies of the Jordan block.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $uv^{\mathsf T}$ | the rank-one block of the vectors $u,v$ |
| $\operatorname{diag}(uv^{\mathsf T},uv^{\mathsf T})$ | the rank-two regular matrix |
| $v^{\mathsf T}u$ | its trace, twice the scalar part of the block |
| $P=uv^{\mathsf T}/(v^{\mathsf T}u)$ | the rank-one idempotent block |
| $\mathcal{D}_L=\{\det=0\}$ | the determinantal variety of the image |
| $\mathbb{P}^1\times\mathbb{P}^1$ | the Segre quadric, the projectivised cone |
| $J\oplus J$ | the Jordan form of the nilpotents |
| $E_{ij}$ | the matrix units of the block, doubled |

## Further Reading

- [The N-Degenerate Sector](the-n-degenerate-sector.html), for the null cone and its strata
- [Nilpotents](nilpotents.html), for the nilpotent cone
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the rank-one elements and the corners
- [The Topology of the Zero-Divisor Cone](the-topology-of-the-zero-divisor-cone.html), for the link and its topology
- [$M_4(\mathbb{C})_{\mathbb{B}}$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](m4c-model-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the matrix units
- [$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : Trace, Determinant and the Biquaternion Norm](m4c-representation-trace-determinant-and-the-biquaternion-norm.html), for the determinant
- [$M_2(\mathbb{C})$ Representation : Rank-One Matrices and the Determinantal Variety](m2c-representation-rank-one-matrices-and-the-determinantal-variety.html), for the $2\times2$ version
- [The Determinant and Alternating Forms](the-determinant-and-alternating-forms.html), for determinantal varieties
