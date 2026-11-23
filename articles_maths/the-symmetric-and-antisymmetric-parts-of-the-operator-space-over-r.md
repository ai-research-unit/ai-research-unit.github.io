# __The Symmetric and Antisymmetric Parts of the Operator Space over $\mathbb{R}$__

## Introduction

**The operator space is itself a matrix algebra, of degree $n^{2}$, and its transpose cuts it into two halves of dimensions $n^{2}(n^{2}+1)/2$ and $n^{2}(n^{2}-1)/2$; the second half is the Lie algebra of $\mathrm{O}(n^{2})$.** The cut is the Hilbert–Schmidt adjoint of the preceding article, and on this space it is the ordinary matrix transpose. The two halves are the operator reading of the two halves of $M_n$, with $n$ replaced by $n^{2}$.

The article defines the involution, proves the dimension count, identifies the antisymmetric half with $\mathfrak{so}(n^{2})$, computes which left multiplications and derivations lie in each half, compares the halves of the operator space with $\operatorname{Sym}_n$ and $\operatorname{Skew}_n$, and exhibits a second involution whose fixed space has the same dimension. It assumes *The Adjoints and the Polar Decomposition of an Operator* for the adjoint and the form, and it defers the topology of the two halves of $M_n$ to *The Two Halves and Their Topology*.

Throughout $n\ge2$, $M_n=M_n(\mathbb{R})$, $\operatorname{End}=\operatorname{End}(M_n)$ and $N=n^{2}$.

## The Involution of the Operator Space

**Definition.** For $S\in\operatorname{End}$ let $S^{*}$ be the adjoint for the Hilbert–Schmidt form, that is $\langle SX,Y\rangle=\langle X,S^{*}Y\rangle$.

**The involution is the matrix transpose.** In an orthonormal basis of $M_n$ the adjoint of $S$ is the transpose of the matrix of $S$, so the map $S\mapsto S^{*}$ is the transpose of $M_{N}(\mathbb{R})$ under the identification $\operatorname{End}\cong M_{N}(\mathbb{R})$ given by the basis of matrix units. Hence

$$
(S^{*})^{*}=S,\qquad (ST)^{*}=T^{*}S^{*},\qquad (\lambda S+\mu T)^{*}=\lambda S^{*}+\mu T^{*},
$$

the three axioms of an involution of the first kind. It is $\mathbb{R}$-linear, it is an anti-automorphism of the algebra of operators, and it fixes the scalars.

**The involution comes from the form.** The adjoint depends on the form, and the form is the Hilbert–Schmidt one. The trace form gives another involution on the same space, with transposition replaced by the exchange of the factors; the two agree only on the operators whose matrix is symmetric. This article uses the definite form throughout.

**Two examples fix the picture.** The identity operator has $N$ ones on the diagonal of its matrix, so $\mathrm{I}^{*}=\mathrm{I}$: the identity is self-adjoint. The transpose operator $\tau$ has the permutation matrix of the transposition, which is symmetric, so $\tau^{*}=\tau$: the transpose operator is self-adjoint, and measured at $n=2$ and $n=3$ its matrix satisfies $\tau=\tau^{\mathsf T}$.

## The Two Halves and the Count

**Every operator splits uniquely.** Write

$$
\operatorname{End}_{\mathrm{sym}}=\{S:S^{*}=S\},\qquad \operatorname{End}_{\mathrm{anti}}=\{S:S^{*}=-S\},
$$

and, since $2$ is invertible in $\mathbb{R}$,

$$
S=\underbrace{\tfrac12(S+S^{*})}_{\in\operatorname{End}_{\mathrm{sym}}}+\underbrace{\tfrac12(S-S^{*})}_{\in\operatorname{End}_{\mathrm{anti}}} .
$$

The two subspaces meet only at the zero operator, so the sum is direct and

$$
\operatorname{End}=\operatorname{End}_{\mathrm{sym}}\oplus\operatorname{End}_{\mathrm{anti}} .
$$

**Theorem.** $\dim\operatorname{End}_{\mathrm{sym}}=N(N+1)/2$ and $\dim\operatorname{End}_{\mathrm{anti}}=N(N-1)/2$, with $N=n^{2}$. So

$$
\frac{n^{2}(n^{2}+1)}{2}+\frac{n^{2}(n^{2}-1)}{2}=n^{4}.
$$

*Proof.* A symmetric $N\times N$ matrix is determined by its entries on and above the diagonal, of number $N(N+1)/2$; an antisymmetric one by its entries strictly above the diagonal, of number $N(N-1)/2$. The two counts add to $N^{2}=n^{4}$.

**The counts at the first two dimensions.** At $n=2$, $N=4$ and $16=10+6$. At $n=3$, $N=9$ and $81=45+36$. Both splits were measured by counting the eigenspaces of the involution.

**The halves are the eigenspaces of the involution.** $\operatorname{End}_{\mathrm{sym}}$ is the eigenspace of eigenvalue $+1$ and $\operatorname{End}_{\mathrm{anti}}$ the eigenspace of eigenvalue $-1$. So the split is the spectral decomposition of the involution, and the two dimensions are the multiplicities of its two eigenvalues.

## The Lie Algebra of the Orthogonal Group

**Theorem.** The Lie algebra of $\mathrm{O}(N)$ for the Hilbert–Schmidt form is $\operatorname{End}_{\mathrm{anti}}$, of dimension $N(N-1)/2=n^{2}(n^{2}-1)/2$.

*Proof.* A path $U(t)$ in $\mathrm{O}(N)$ with $U(0)=\mathrm{I}$ satisfies $U(t)^{*}U(t)=\mathrm{I}$. Differentiating at $t=0$ gives $S^{*}+S=0$, where $S=U'(0)$. Conversely, for antisymmetric $S$ the exponential $\exp(tS)$ is orthogonal, because $(\exp tS)^{*}=\exp(tS^{*})=\exp(-tS)=(\exp tS)^{-1}$, and it starts at the identity. So the tangent space at the identity is the antisymmetric half.

**The dimension is the dimension of the group.** $\dim\mathrm{O}(N)=N(N-1)/2$, and

$$
\dim\mathrm{O}(n^{2})=\frac{n^{2}(n^{2}-1)}{2},
$$

which is the count above. At $n=2$ this is $6$, the dimension of $\mathrm{O}(4)$; at $n=3$ it is $36$, the dimension of $\mathrm{O}(9)$.

**The self-adjoint half is the complement, not a Lie algebra.** The commutator of two self-adjoint operators is antisymmetric, since $[S,T]^{*}=[T^{*},S^{*}]=[T,S]=-[S,T]$. So the self-adjoint half is closed under the anticommutator and the antisymmetric half under the commutator: $\operatorname{End}_{\mathrm{sym}}$ is a Jordan algebra and $\operatorname{End}_{\mathrm{anti}}$ is a Lie algebra. This is the same dichotomy as in *The Matrix Algebra $M_n(\mathbb{R})$*, one level up.

## The Left Multiplication

**Theorem.** $L_A$ is self-adjoint exactly when $A$ is symmetric.

*Proof.* $L_A^{*}=L_{A^{\mathsf T}}$ by the preceding article, so $L_A^{*}=L_A$ exactly when $A^{\mathsf T}=A$.

**The condition $L_A=R_{A^{\mathsf T}}$ is a different one.** It says $AX=XA^{\mathsf T}$ for all $X$. At $X=\mathrm{I}$ it gives $A=A^{\mathsf T}$, and then it says that $A$ commutes with every $X$, so $A=\lambda\mathrm{I}$. So the left multiplications that are also right multiplications are the scalars, of dimension $1$, while the left multiplications that are self-adjoint are the symmetric matrices, of dimension $n(n+1)/2$. The two conditions are not the same, and only the second is self-adjointness.

**The one-sided operators sit in the halves as follows.** $L_A$ is self-adjoint for $A\in\operatorname{Sym}_n$ and neither self-adjoint nor antisymmetric otherwise; measured at $n=3$, $L_A$ is self-adjoint for a symmetric $A$ and not for an anti-Hermitian or a generic one. The operator $L_A-R_{A^{\mathsf T}}$ is antisymmetric for every $A$, since its adjoint is $L_{A^{\mathsf T}}-R_A=-(L_A-R_{A^{\mathsf T}})$. So the space of these operators, of dimension $n^{2}-1$, lies in the antisymmetric half.

## The Derivations

**Theorem.** $\operatorname{ad}_A$ is self-adjoint exactly when $A$ is symmetric, and antisymmetric exactly when $A$ is antisymmetric.

*Proof.* $\operatorname{ad}_A^{*}=\operatorname{ad}_{A^{\mathsf T}}$, so self-adjointness is $A=A^{\mathsf T}$ and antisymmetry is $A=-A^{\mathsf T}$.

**Measured at $n=3$.** For a random antisymmetric $A$ the pairing $\langle \operatorname{ad}_AX,Y\rangle+\langle X,\operatorname{ad}_AY\rangle$ vanishes, and for a random symmetric $A$ it does not. So the derivations with symmetric $A$ fill the self-adjoint half, and the derivations with antisymmetric $A$ fill a subspace of the antisymmetric half of dimension $n(n-1)/2$.

**The inner derivations form a Lie algebra of dimension $n^{2}-1$.** The kernel of $A\mapsto\operatorname{ad}_A$ is $\mathbb{R}\mathrm{I}$, so the inner derivations form $\mathfrak{gl}_n(\mathbb{R})/\mathbb{R}\mathrm{I}\cong\mathfrak{sl}_n(\mathbb{R})$. Their intersection with the antisymmetric half is the image of $\operatorname{Skew}_n$, of dimension $n(n-1)/2$, the Lie algebra of $\mathrm{SO}(n)$ acting by conjugation.

**The invariant form changes the answer.** For the trace form every derivation is antisymmetric, as shown in *The Adjoints and the Polar Decomposition of an Operator*. Under the Hilbert–Schmidt form only the derivations with antisymmetric $A$ are. The two statements are the two forms' readings of the same operator.

## The Two Halves against the Two Halves of $M_n$

**The same construction at $n$ and at $n^{2}$.** The table puts the two splits side by side:

| Space | Symmetric half | Antisymmetric half |
|---|---|---|
| $M_n$, dimension $n^{2}$ | $n(n+1)/2$ | $n(n-1)/2$ |
| $\operatorname{End}$, dimension $n^{4}$ | $n^{2}(n^{2}+1)/2$ | $n^{2}(n^{2}-1)/2$ |

The second row is the first with $n$ replaced by $n^{2}$, so the operator space repeats the algebra's own split one level up: $\mathfrak{so}(n)$ has dimension $n(n-1)/2$ and $\mathfrak{so}(n^{2})$ has dimension $n^{2}(n^{2}-1)/2$.

**The inclusion is not the split.** $\operatorname{Sym}_n$ is a subspace of $M_n$ of dimension $n(n+1)/2$, while $\operatorname{End}_{\mathrm{sym}}$ is a subspace of $\operatorname{End}$ of dimension $n^{2}(n^{2}+1)/2$. The first is not contained in the second in any natural way: an element of $\operatorname{Sym}_n$ is a matrix, an element of $\operatorname{End}_{\mathrm{sym}}$ is an operator on matrices. What repeats is the formula, not the object.

**The two halves of the operator space are bigger than the operators of the two halves.** The two-sided operators $T_{A,B}$ with $A,B$ symmetric are self-adjoint, and they form the cone over the product of the two symmetric rank-one varieties; but the self-adjoint half also contains every operator $T_{A,B}+T_{A,B}^{*}$ and their sums, which are not two-sided. So the self-adjoint half is the linear span of the self-adjoint two-sided operators, and it is far larger than their cone.

## The Second Involution

**Definition.** Let $\tau$ be the transpose operator and $\Theta(S)=\tau S\tau$, that is $\Theta(S)(X)=(S(X^{\mathsf T}))^{\mathsf T}$.

**Theorem.** $\Theta$ is an involutive automorphism of the operator algebra, and its fixed space has dimension $n^{2}(n^{2}+1)/2$.

*Proof.* Since $\tau^{2}=\mathrm{I}$, $\Theta$ is an involution. Since $\Theta(ST)=\tau ST\tau=(\tau S\tau)(\tau T\tau)=\Theta(S)\Theta(T)$, it is an automorphism. The fixed space is the centraliser of $\tau$. The transpose has eigenvalues $+1$ on $\operatorname{Sym}_n$ and $-1$ on $\operatorname{Skew}_n$, so an operator commuting with it preserves each half, and the centraliser has dimension

$$
\Big(\frac{n(n+1)}{2}\Big)^{2}+\Big(\frac{n(n-1)}{2}\Big)^{2}=\frac{n^{2}(n^{2}+1)}{2} .
$$

Measured at $n=2$ and $n=3$, the dimension of the fixed space of $\Theta$ is $10$ and $45$, and $\Theta$ is an automorphism to machine precision.

**Two involutions of the first kind, with fixed spaces of the same dimension.** The adjoint is an anti-automorphism and $\Theta$ is an automorphism, and both fix a space of dimension $n^{2}(n^{2}+1)/2$. This is the operator echo of the pair of involutions of $M_n$ described in *The Involutions of the First Kind: Transpose and Symplectic*: two involutions, distinguished by their algebraic type rather than by the dimension of their fixed spaces.

**The two involutions commute.** $\Theta\sigma=\sigma\Theta$, because $(\tau S\tau)^{\mathsf T}=\tau S^{\mathsf T}\tau$ and $\tau$ is symmetric. Their product is a third involution, and the operators fixed by both are the symmetric operators commuting with the transpose; measured, this intersection has dimension $7$ at $n=2$ and $27$ at $n=3$.

## Summary

The operator space $\operatorname{End}(M_n(\mathbb{R}))$ is the matrix algebra $M_{n^{2}}(\mathbb{R})$, and its Hilbert–Schmidt adjoint is the transpose, an involution of the first kind. It splits the space into a self-adjoint half of dimension $n^{2}(n^{2}+1)/2$ and an antisymmetric half of dimension $n^{2}(n^{2}-1)/2$, the second being the Lie algebra $\mathfrak{so}(n^{2})$ of $\mathrm{O}(n^{2})$. The left multiplication $L_A$ is self-adjoint exactly when $A$ is symmetric, and $L_A=R_{A^{\mathsf T}}$ forces $A$ to be scalar. The derivation $\operatorname{ad}_A$ is self-adjoint for symmetric $A$ and antisymmetric for antisymmetric $A$, while for the trace form every derivation is antisymmetric. A second involution, conjugation by the transpose, is an automorphism whose fixed space has the same dimension $n^{2}(n^{2}+1)/2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S^{*}$ | the adjoint for the Hilbert–Schmidt form, the transpose of the $n^{2}\times n^{2}$ matrix |
| $\operatorname{End}_{\mathrm{sym}}$, $\operatorname{End}_{\mathrm{anti}}$ | the self-adjoint and antisymmetric halves, of dimensions $n^{2}(n^{2}\pm1)/2$ |
| $N=n^{2}$ | the degree of the operator algebra, so that $\dim\operatorname{End}=N^{2}$ |
| $\mathfrak{so}(n^{2})$ | the Lie algebra of $\mathrm{O}(n^{2})$, equal to $\operatorname{End}_{\mathrm{anti}}$ |
| $L_A$, $R_B$ | left and right multiplication |
| $\operatorname{ad}_A=L_A-R_A$ | the inner derivation |
| $\tau$ | the transpose operator $X\mapsto X^{\mathsf T}$ |
| $\Theta(S)=\tau S\tau$ | conjugation by the transpose, an involutive automorphism |

## Further Reading

- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the transpose, the orthogonal group and the symmetric and antisymmetric matrices.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the involutions of a matrix algebra and the centraliser of an involution.
- [The Adjoints and the Polar Decomposition of an Operator](the-adjoints-and-the-polar-decomposition-of-an-operator-over-r.html), for the Hilbert–Schmidt form and the adjoints.
- [The Involutions of the First Kind: Transpose and Symplectic](the-involutions-of-the-first-kind-transpose-and-symplectic.html), for the classification of the involutions of $M_n(\mathbb{R})$.
- [The Two Halves and Their Topology](the-two-halves-and-their-topology-over-r.html), for $\operatorname{Sym}_n$ and $\operatorname{Skew}_n$ and their strata.
