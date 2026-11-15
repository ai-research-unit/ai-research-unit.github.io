# __The Involutions over $\mathbb{R}$ and over $\mathbb{C}$__

## Introduction

**An involution of the algebra is a map of order two that either preserves or reverses the product, and the classification of those maps is short: two of the reversing kind over either field, and a signature's worth of the preserving kind.**

The article separates the two kinds, classifies the involutions of $M_n(\mathbb{C})$ and of $M_n(\mathbb{R})$ up to conjugacy, and records the split that every involution produces, the fixed part and the anti-fixed part. It counts the two parts: for the transpose the symmetric half has dimension $n(n+1)/2$ and the skew half $n(n-1)/2$, while for the symplectic involution the two dimensions are exchanged and the fixed half has dimension $n(n-1)/2$. It assumes *The Ideals, the Centre and the Simplicity of $M_n(\mathbb{C})$* for the inner automorphisms and *The Two Base Fields: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$* for the antilinear structures. It defers the two halves themselves to *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric* and to *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian*, and the multiplication tables to *The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$*.

## Two Kinds of Involution

**An involution is a bijective linear map $\sigma$ of the algebra with $\sigma^{2}=\mathrm{id}$ which is either an automorphism or an anti-automorphism.** The two cases are

$$
\sigma(AB)=\sigma(A)\sigma(B)\quad\text{(automorphism)},\qquad
\sigma(AB)=\sigma(B)\sigma(A)\quad\text{(anti-automorphism)} .
$$

An anti-automorphism of order two is what the word *involution* names in the theory of algebras with a form, and it is the kind that produces the symmetric and the skew halves. An automorphism of order two produces a grading instead.

**The first kind is complex-linear and the second kind is conjugate-linear.** Write $\sigma$ for an involution. If $\sigma(zA)=z\sigma(A)$ for all complex $z$, the involution is of the **first kind**; if $\sigma(zA)=\bar z\sigma(A)$, it is of the **second kind**. Over $\mathbb{R}$ there is only the first kind, since the scalars are real. Over $\mathbb{C}$ both occur, and the second kind is the one that carries the Hermitian structure.

**The three examples that matter are the transpose, the conjugate transpose and the symplectic transpose.** They are

$$
\sigma_1(A)=A^{\mathsf T},\qquad \sigma_2(A)=A^{*}=\bar A^{\mathsf T},\qquad \sigma_3(A)=JA^{\mathsf T}J^{-1},
$$

with $J$ the block-diagonal matrix of $\tfrac{n}{2}$ copies of $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$. The first two are anti-automorphisms of order two over $\mathbb{C}$; the first is of the first kind and the second of the second kind. The third is of the first kind and is defined only for even $n$.

## The Involutions of the First Kind

**Every complex-linear anti-automorphism of order two is $A\mapsto SA^{\mathsf T}S^{-1}$ with $S^{\mathsf T}=\pm S$.** An anti-automorphism $\sigma$ sends the matrix units to $E_{ij}\mapsto c_{ij}E_{\tau(i)\tau(j)}$ for a permutation $\tau$ and scalars, and the condition $\sigma^{2}=\mathrm{id}$ forces $\tau$ to be the identity or the reversal of the order of the units; the reversal case reduces to the identity composed with the transpose. So $\sigma(A)=SA^{\mathsf T}S^{-1}$, and $\sigma^{2}=\mathrm{id}$ reads $SS^{-{\mathsf T}}=\lambda\mathrm{I}$, that is $S=\pm S^{\mathsf T}$ after rescaling. Hence

$$
\sigma(A)=SA^{\mathsf T}S^{-1},\qquad S^{\mathsf T}=S\ \text{or}\ S^{\mathsf T}=-S .
$$

**There are exactly two classes, and the second needs $n$ even.** If $S$ is symmetric and invertible, a change of basis carries it to the identity and $\sigma$ to the transpose. If $S$ is skew and invertible, then $n$ is even, because a skew matrix of odd size has vanishing determinant; a change of basis carries $S$ to $J$ and $\sigma$ to the symplectic transpose. So the classes are

$$
\text{transpose type},\qquad \text{symplectic type}\ (n\ \text{even}),
$$

and at odd $n$ only the transpose type exists.

**The preserving kind has $n+1$ classes, indexed by a rank.** A complex-linear automorphism of order two is inner by Skolem–Noether, so it is $A\mapsto SAS^{-1}$ with $S^{2}=\lambda\mathrm{I}$. After scaling, $S$ has eigenvalues $\pm1$ and is diagonalisable, so it is conjugate to $\operatorname{diag}(\mathrm{I}_p,-\mathrm{I}_{n-p})$. The classes are therefore indexed by $p=0,1,\dots,n$, and the fixed algebra of the $p$-th class is $M_p(\mathbb{C})\oplus M_{n-p}(\mathbb{C})$, of dimension $p^{2}+(n-p)^{2}$.

## The Involutions of the Second Kind

**An antilinear anti-automorphism of order two is a Hermitian structure, and its classes are the signatures.** Let $\sigma$ be conjugate-linear and an anti-automorphism with $\sigma^{2}=\mathrm{id}$. Then $\sigma(A)=SA^{*}S^{-1}$ with $S$ Hermitian, and the condition on $S$ is only that it be invertible and self-adjoint up to scale. A change of basis carries $S$ to a diagonal matrix with $p$ entries $+1$ and $q$ entries $-1$, so the classes are indexed by the **signature** $(p,q)$ with $p+q=n$, and there are $n+1$ of them. The case $p=n$ is the conjugate transpose $\sigma(A)=A^{*}$.

**The count over $\mathbb{C}$ is therefore $2+(n+1)$ of the reversing kind and $n+1$ of the preserving kind.** Over $\mathbb{R}$ the antilinear cases disappear and the counts are: two reversing classes, transpose and symplectic, and $n+1$ preserving classes. The table summarises the four families.

| Field | Kind | Product | Classes |
|---|---|---|---|
| $\mathbb{C}$ | linear | reversed | $2$: transpose, symplectic |
| $\mathbb{C}$ | linear | preserved | $n+1$: inner by $\operatorname{diag}(\mathrm{I}_p,-\mathrm{I}_{n-p})$ |
| $\mathbb{C}$ | antilinear | reversed | $n+1$: signatures $(p,q)$ |
| $\mathbb{C}$ | antilinear | preserved | $2$: $M_n(\mathbb{R})$ and $M_{n/2}(\mathbb{H})$ |

## The Split into Fixed and Anti-Fixed

**Every involution splits the algebra into the fixed part and the anti-fixed part.** For $\sigma^{2}=\mathrm{id}$ the eigenvalues are $\pm1$ and

$$
M_n(\mathbb{C})=\operatorname{Fix}\sigma\oplus\operatorname{Anti}\sigma,\qquad
A=\tfrac12(A+\sigma A)+\tfrac12(A-\sigma A).
$$

The two projections $\tfrac12(\mathrm{I}\pm\sigma)$ are idempotent and add to the identity. They are linear maps on the algebra, not elements of it, and they are the only two projections produced by $\sigma$ alone.

**For the transpose the halves are the symmetric and the skew matrices.** With $\sigma(A)=A^{\mathsf T}$,

$$
\operatorname{Sym}_n=\{A:A^{\mathsf T}=A\},\qquad \operatorname{Skew}_n=\{A:A^{\mathsf T}=-A\}.
$$

The first is closed under the product and the second is closed under the commutator; this is the whole content of the following two articles and the source of the four multiplication tables.

**For the symplectic involution the halves are the two symplectic symmetry classes.** With $\sigma(A)=JA^{\mathsf T}J^{-1}$, the fixed part is $\{A:AJ\ \text{skew}\}$ and the anti-fixed part is $\{A:AJ\ \text{symmetric}\}$, and the two have the dimensions $n(n-1)/2$ and $n(n+1)/2$. So the symplectic involution exchanges the dimensions that the transpose gives, and the exchange is the reason a symplectic form has no preferred half of larger size.

## The Two Dimensions

**The symmetric half has dimension $n(n+1)/2$ and the skew half $n(n-1)/2$.** The symmetric matrices are determined by their entries on and above the diagonal, and there are $n(n+1)/2$ of those; the skew matrices are determined by their entries above the diagonal, and there are $n(n-1)/2$. The sum is

$$
\frac{n(n+1)}{2}+\frac{n(n-1)}{2}=n^{2},
$$

and the values for $n=2,\dots,6$ are

| $n$ | $\dim\operatorname{Sym}_n$ | $\dim\operatorname{Skew}_n$ | sum |
|---|---|---|---|
| $2$ | $3$ | $1$ | $4$ |
| $3$ | $6$ | $3$ | $9$ |
| $4$ | $10$ | $6$ | $16$ |
| $5$ | $15$ | $10$ | $25$ |
| $6$ | $21$ | $15$ | $36$ |

**The Hermitian and anti-Hermitian halves have equal real dimension $n^{2}$.** For $\sigma(A)=A^{*}$ the two halves are complex subspaces of real dimension $n^{2}$ each, since a Hermitian matrix is determined by $n$ real diagonal entries and $\binom{n}{2}$ complex off-diagonal ones, $n+2\binom{n}{2}=n^{2}$. So the transpose split halves $n^{2}$ into two unequal parts, while the conjugate-transpose split halves $2n^{2}$ into two equal parts.

**Every Hermitian involution has a fixed space of real dimension $n^{2}$, whatever its signature.** For $\sigma(A)=SA^{*}S^{-1}$ with $S$ Hermitian of signature $(p,q)$, the fixed space is the set of $S$-Hermitian matrices, and the count of parameters is again $n$ real diagonal entries and $\binom{n}{2}$ complex off-diagonal ones. The signature does not change the dimension; it changes the signature of the trace form restricted to the half, which is computed in *The Trace Form and Its Signature on the Two Halves*.

## What Transposition Does to $UT_n$

**The transpose does not preserve the triangular algebra; it exchanges it with the lower triangular one.** For $A\in UT_n$ the transpose $A^{\mathsf T}$ is lower triangular, so

$$
UT_n^{\mathsf T}=LT_n,\qquad UT_n\cap UT_n^{\mathsf T}=\{\text{diagonal matrices}\}.
$$

The fixed set of the transpose inside $UT_n$ is therefore the diagonal, of dimension $n$, and the anti-fixed set is $\{0\}$: a triangular matrix that is antisymmetric is zero, since its diagonal entries vanish and its entries above the diagonal are the negatives of entries below it, which are absent.

**The symmetric half of the algebra is the natural model of the carrier space of $UT_n$, not its product.** Both spaces have dimension $n(n+1)/2$, and the projection $\tfrac12(\mathrm{I}+{}^{\mathsf T})$ maps $M_n(\mathbb{C})$ onto $\operatorname{Sym}_n$. That projection is a linear map of the algebra and it is not of the form $A\mapsto eA$ for an element $e$, which is the precise reason $UT_n$ is not a Peirce corner of the transpose split; see *$UT_n$ as the Complement of the Antisymmetric Part (Transpose Case)*.

## The Case $n=2$

**At $n=2$ the transpose split is $4=3+1$.** The symmetric half is spanned by $\mathrm{I}$, $\sigma_3=\operatorname{diag}(1,-1)$, $\sigma_1$, and the skew half by the single matrix $i\sigma_2$, the rotation. So

$$
\operatorname{Sym}_2=\operatorname{span}\{\mathrm{I},\sigma_1,\sigma_3\},\qquad \operatorname{Skew}_2=\mathbb{C}\cdot i\sigma_2 ,
$$

and the three Pauli matrices together with $\mathrm{I}$ are a basis of the algebra in which the split is visible.

**At $n=2$ the symplectic type exists and is not conjugate to the transpose.** Since $2$ is even both classes of the reversing kind are present. With $J=i\sigma_2$ the symplectic involution $A\mapsto JA^{\mathsf T}J^{-1}$ has a fixed half of dimension $1$ and an anti-fixed half of dimension $3$. A conjugation $A\mapsto TAT^{-1}$ carries $SA^{\mathsf T}S^{-1}$ to $(TST^{\mathsf T})A^{\mathsf T}(TST^{\mathsf T})^{-1}$, which keeps $S$ symmetric or skew, so no inner automorphism exchanges the two classes.

## Summary

An involution is an automorphism or an anti-automorphism of order two, of the first kind if complex-linear and of the second if conjugate-linear. The reversing complex-linear involutions of $M_n(\mathbb{C})$ are the transpose and, for even $n$, the symplectic transpose; the preserving ones are inner by $\operatorname{diag}(\mathrm{I}_p,-\mathrm{I}_{n-p})$, $n+1$ classes; the antilinear reversing ones are the Hermitian structures, $n+1$ classes indexed by signature; the antilinear preserving ones are the two real structures. Every involution splits the algebra into a fixed and an anti-fixed part by $\tfrac12(\mathrm{I}\pm\sigma)$. The transpose gives halves of dimensions $n(n+1)/2$ and $n(n-1)/2$, the symplectic involution exchanges them, and the conjugate transpose gives two halves of real dimension $n^{2}$ whatever the signature. Transposition exchanges $UT_n$ with $LT_n$ and fixes only the diagonal.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$ | an involution, automorphism or anti-automorphism with $\sigma^{2}=\mathrm{id}$ |
| $A^{\mathsf T}$ | the transpose, a reversing involution of the first kind |
| $A^{*}=\bar A^{\mathsf T}$ | the conjugate transpose, a reversing involution of the second kind |
| $J$ | the symplectic matrix, $\tfrac{n}{2}$ blocks of $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ |
| $\operatorname{Fix}\sigma$, $\operatorname{Anti}\sigma$ | the $\pm1$ eigenspaces of $\sigma$ |
| $\operatorname{Sym}_n$, $\operatorname{Skew}_n$ | the fixed and anti-fixed halves of the transpose, of dimensions $n(n\pm1)/2$ |
| $(p,q)$ | the signature of a Hermitian structure, $p+q=n$ |
| $UT_n$, $LT_n$ | the upper and the lower triangular algebras |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for involutions of the first and second kind and their classification.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (AMS, 1998), for the classification of involutions on central simple algebras.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for symmetric, antisymmetric, Hermitian and anti-Hermitian matrices.
- [The Two Base Fields: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$](the-two-base-fields-mnr-inside-mnc.html), for the antilinear involutions and the two real structures.
- [The Ideals, the Centre and the Simplicity of $M_n(\mathbb{C})$](the-ideals-the-centre-and-the-simplicity-of-mnc.html), for the inner automorphisms used in the classification.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the conjugate transpose and the trace form.
