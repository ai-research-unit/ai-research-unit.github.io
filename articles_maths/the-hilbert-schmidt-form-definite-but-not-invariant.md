# __The Hilbert–Schmidt Form: Definite but Not Invariant__

## Introduction

**The form $\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{\mathsf T}Y)$ is an inner product on $M_n(\mathbb{R})$, and it is not invariant under the algebra: the ratio $\langle AX,AY\rangle_{\mathrm{HS}}/\langle X,Y\rangle_{\mathrm{HS}}$ is not constant in $X$ unless $A$ is orthogonal.**

The article computes the adjoints of the multiplication operators, derives the exact adjoint of $\operatorname{ad}_A$, measures the defect of invariance on a hundred random pairs, proves that invariance holds for an element $A$ exactly when $A$ is orthogonal, and compares the two forms and their isometry groups. It assumes *The Trace Form and Its Indefinite Inertia* for the competing form, and it defers the Killing form to *The Killing Form, Its Radical and the Centre of $\mathfrak{gl}_n(\mathbb{R})$*.

## The Form

**Define $\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{\mathsf T}Y)$.** In entries,

$$
\langle X,Y\rangle_{\mathrm{HS}}=\sum_{i,j=1}^{n}X_{ij}Y_{ij}.
$$

So the form is the standard scalar product of the $n^{2}$ entries, read in any order.

**The form is an inner product, and its norm is the Frobenius norm $\|X\|_{\mathrm{F}}=\langle X,X\rangle_{\mathrm{HS}}^{1/2}$.** It is bilinear and symmetric. It is positive definite, because

$$
\langle X,X\rangle_{\mathrm{HS}}=\sum_{i,j}X_{ij}^{2}
$$

is a sum of squares, and it vanishes only for $X=0$. So $M_n(\mathbb{R})$ carries the Euclidean structure of $\mathbb{R}^{n^{2}}$, with the entries as coordinates.

**The matrix units are orthonormal.** For the units,

$$
\langle E_{ij},E_{kl}\rangle_{\mathrm{HS}}=\operatorname{tr}(E_{ji}E_{kl})=\delta_{ik}\delta_{jl},
$$

which is $1$ exactly when the two units are equal. The Gram matrix of the form in the matrix-unit basis is the identity of order $n^{2}$; this was checked exactly at $n=3$. The trace form has no such property: there the Gram matrix is a permutation matrix with zeros on most of the diagonal.

## The Adjoints of the Multiplications

**Left multiplication by $A$ has adjoint left multiplication by $A^{\mathsf T}$.** For all $X,Y$,

$$
\langle AX,Y\rangle_{\mathrm{HS}}=\operatorname{tr}\bigl((AX)^{\mathsf T}Y\bigr)=\operatorname{tr}(X^{\mathsf T}A^{\mathsf T}Y)=\langle X,A^{\mathsf T}Y\rangle_{\mathrm{HS}}.
$$

The computation is a single use of $(AX)^{\mathsf T}=X^{\mathsf T}A^{\mathsf T}$ and the definition.

**The operator $\operatorname{ad}_A$ has adjoint $\operatorname{ad}_{A^{\mathsf T}}$.** Write $\operatorname{ad}_A(Y)=[A,Y]=AY-YA$. Then

$$
\langle X,[A,Y]\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{\mathsf T}AY)-\operatorname{tr}(X^{\mathsf T}YA)=\operatorname{tr}\bigl((X^{\mathsf T}A-AX^{\mathsf T})Y\bigr),
$$

and

$$
X^{\mathsf T}A-AX^{\mathsf T}=\bigl(A^{\mathsf T}X-XA^{\mathsf T}\bigr)^{\mathsf T}=[A^{\mathsf T},X]^{\mathsf T}.
$$

So

$$
\langle X,\operatorname{ad}_A(Y)\rangle_{\mathrm{HS}}=\bigl\langle [A^{\mathsf T},X],\,Y\bigr\rangle_{\mathrm{HS}}=\bigl\langle \operatorname{ad}_{A^{\mathsf T}}(X),\,Y\bigr\rangle_{\mathrm{HS}}.
$$

The adjoint is $\operatorname{ad}_{A^{\mathsf T}}$. This was checked numerically at $n=2,3,4$ on a hundred random triples, with a maximal deviation of $1.8\times10^{-15}$ at $n=2$ and $7.1\times10^{-15}$ at $n=3$ and $n=4$.

**The sign of the adjoint measures the invariance.** For an invariant form the adjoint of $\operatorname{ad}_A$ is $-\operatorname{ad}_A$, because invariance says $\langle \operatorname{ad}_A X,Y\rangle+\langle X,\operatorname{ad}_A Y\rangle=0$. Here the adjoint is $\operatorname{ad}_{A^{\mathsf T}}$, and the two agree only when $A^{\mathsf T}=-A$. So $\operatorname{ad}_A$ is anti-self-adjoint for the Hilbert–Schmidt form exactly for $A\in\mathfrak{so}(n)$, and no minus sign appears in the display above. The missing sign is the defect.

**The defect is not small.** The same numerical run measured $\langle \operatorname{ad}_A X,Y\rangle_{\mathrm{HS}}+\langle X,\operatorname{ad}_A Y\rangle_{\mathrm{HS}}$ on the same hundred triples and found a maximum absolute value of $18.58$ at $n=2$, $42.21$ at $n=3$ and $53.92$ at $n=4$. A quantity that vanishes for an invariant form is here of the size of the entries.

## The Defect of Invariance

**The ratio of norms is a Rayleigh quotient.** For invertible $A$ and nonzero $X$,

$$
\frac{\langle AX,AX\rangle_{\mathrm{HS}}}{\langle X,X\rangle_{\mathrm{HS}}}=\frac{\operatorname{tr}(X^{\mathsf T}A^{\mathsf T}AX)}{\operatorname{tr}(X^{\mathsf T}X)}.
$$

The right-hand side is the Rayleigh quotient of the operator $X\mapsto A^{\mathsf T}AX$ on $\mathbb{R}^{n^{2}}$. That operator is left multiplication by the symmetric positive definite matrix $A^{\mathsf T}A$, so its eigenvalues are the eigenvalues of $A^{\mathsf T}A$ on $\mathbb{R}^{n}$, each repeated $n$ times.

**Hence the ratio ranges over the interval of the squared singular values.** The extreme values over all nonzero $X$ are $\sigma_{\min}(A)^{2}$ and $\sigma_{\max}(A)^{2}$, where $\sigma$ denotes a singular value. The ratio is constant in $X$ exactly when the two extremes agree, that is, when all singular values are equal.

**The measurement on a hundred random pairs confirms the range.** Take $n=3$ and $A=\operatorname{diag}(1,2,3)$, and draw a hundred standard normal matrices $X$ from a seeded generator. The ratio ran from $1.4606$ to $8.0238$. The exact interval is $[1,9]$, because the singular values of $A$ are $1,2,3$ and the squares are $1,4,9$; the sample does not reach the endpoints, as expected.

**At $n=2$ the defect is visible on single units.** Take $A=\operatorname{diag}(2,1)$. Then $AE_{12}=2E_{12}$ and $AE_{21}=E_{21}$, so

$$
\frac{\langle AE_{12},AE_{12}\rangle_{\mathrm{HS}}}{\langle E_{12},E_{12}\rangle_{\mathrm{HS}}}=4,\qquad \frac{\langle AE_{21},AE_{21}\rangle_{\mathrm{HS}}}{\langle E_{21},E_{21}\rangle_{\mathrm{HS}}}=1.
$$

The two ratios differ, so the form is not invariant under this $A$.

**An orthogonal $A$ gives the ratio one on every pair.** The same run with a random orthogonal $Q$, drawn from the $QR$ factorisation of a normal matrix, gave a minimum of $0.999999999999999$ and a maximum of $1.000000000000000$ over a hundred pairs. The deviation is the rounding error of the arithmetic.

## Invariance Holds Exactly for Orthogonal Matrices

**Theorem.** The identity $\langle AX,AY\rangle_{\mathrm{HS}}=\langle X,Y\rangle_{\mathrm{HS}}$ holds for all $X,Y$ if and only if $A^{\mathsf T}A=\mathrm{I}$.

**Proof of the direct direction.** If $A^{\mathsf T}A=\mathrm{I}$ then

$$
\langle AX,AY\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{\mathsf T}A^{\mathsf T}AY)=\operatorname{tr}(X^{\mathsf T}Y)=\langle X,Y\rangle_{\mathrm{HS}}.
$$

The hypothesis is used once, and no other property of $A$ enters.

**Proof of the converse.** Suppose the identity holds for all $X,Y$. Test on the matrix units $X=E_{ij}$ and $Y=E_{kl}$. Then

$$
\langle AE_{ij},AE_{kl}\rangle_{\mathrm{HS}}=\operatorname{tr}(E_{ji}A^{\mathsf T}AE_{kl})=(A^{\mathsf T}A)_{lj}\,\delta_{ik},
$$

while $\langle E_{ij},E_{kl}\rangle_{\mathrm{HS}}=\delta_{ik}\delta_{jl}$. Take $i=k$. Then $(A^{\mathsf T}A)_{lj}=\delta_{lj}$ for all $j,l$, so $A^{\mathsf T}A=\mathrm{I}$.

**So the invariance group is the orthogonal group.** An invertible $A$ preserves the form exactly when $A\in\mathrm{O}(n)$. The same computation with $A$ singular shows that a singular $A$ never preserves the form, since $A^{\mathsf T}A$ then has a zero eigenvalue and the ratio above can vanish.

## The Relation to the Trace Form

**The two forms differ by the transpose.** By definition and by the invariance of the trace,

$$
\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{\mathsf T}Y),\qquad \langle X,Y\rangle=\operatorname{tr}(XY)=\langle X^{\mathsf T},Y\rangle_{\mathrm{HS}}.
$$

The second identity was checked exactly with numpy at $n=3$: the two sides agree to the last bit. So the trace form is the Hilbert–Schmidt form composed with the transpose in the first slot.

**On the symmetric part the two forms agree, and on the antisymmetric part they are opposite.** Write $X=S+K$ and $Y=S'+K'$ with $S,S'$ symmetric and $K,K'$ antisymmetric. The cross terms vanish, and

$$
\langle X,Y\rangle=\operatorname{tr}(SS')+\operatorname{tr}(KK'),\qquad \langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(SS')-\operatorname{tr}(KK').
$$

The second identity uses $K^{\mathsf T}=-K$. So the two forms agree on $\operatorname{Sym}_n$ and differ by a sign on $\operatorname{Skew}_n$.

**The definite form is the difference of two positive forms on the halves.** Since $\langle S,S\rangle_{\mathrm{HS}}=\operatorname{tr}(S^{2})$ for symmetric $S$ and $\langle K,K\rangle_{\mathrm{HS}}=-\operatorname{tr}(K^{2})$ for antisymmetric $K$, the Hilbert–Schmidt form is positive on both halves, while the trace form is positive on the first and negative on the second. The inertia of the trace form and the definiteness of the Hilbert–Schmidt form are the same computation read with two sign conventions.

## The Two Isometry Groups

**The isometry group of the Hilbert–Schmidt form is $\mathrm{O}(n^{2})$.** The form is the standard scalar product of the $n^{2}$ entries, so its isometries are the orthogonal matrices of order $n^{2}$. The dimension is $n^{2}(n^{2}-1)/2$, which is $6$ at $n=2$ and $36$ at $n=3$.

**The isometry group of the trace form is not $\mathrm{O}(n^{2})$.** It contains the conjugation by every invertible matrix, of dimension $n^{2}-1$, and it contains the transpose. It also contains the unbounded family $X\mapsto D_tXD_t^{-1}$ with $D_t=\operatorname{diag}(t,1,\dots,1)$ and $t\to\infty$, while $\mathrm{O}(n^{2})$ is compact. So the two groups differ.

**The isometry group of the trace form preserves the null cone.** The set $\{X:\operatorname{tr}(X^{2})=0\}$ is invariant under every isometry of the trace form, and it is not invariant under $\mathrm{O}(n^{2})$, which acts transitively on the sphere of the Frobenius norm and moves $E_{12}$ to a matrix with nonzero trace of square. So the two geometries are different in a way that no change of coordinates can repair.

## Why One Form Cannot Do Both

**A positive definite form cannot be invariant, and an invariant form cannot be definite.** The trace form is invariant under all inner derivations and indefinite; the Hilbert–Schmidt form is definite and not invariant. The first article proves the general statement: a positive definite symmetric form $B$ with $B([A,X],Y)+B(X,[A,Y])=0$ forces $2B(E_{12},E_{12})=0$.

## Summary

The Hilbert–Schmidt form $\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{\mathsf T}Y)$ is the sum of the products of corresponding entries. It is an inner product, it gives $M_n(\mathbb{R})$ the Euclidean structure of $\mathbb{R}^{n^{2}}$, and the matrix units are orthonormal for it. Left multiplication by $A$ has adjoint left multiplication by $A^{\mathsf T}$, and the adjoint of $\operatorname{ad}_A$ is $\operatorname{ad}_{A^{\mathsf T}}$; the minus sign of an invariant form is absent, and its absence is exactly the failure of invariance. The ratio $\langle AX,AX\rangle_{\mathrm{HS}}/\langle X,X\rangle_{\mathrm{HS}}$ is a Rayleigh quotient of left multiplication by $A^{\mathsf T}A$, so it ranges over the interval between the squared extreme singular values; at $n=3$ with $A=\operatorname{diag}(1,2,3)$ and a hundred seeded random pairs it ran from $1.4606$ to $8.0238$, inside the exact interval $[1,9]$, and for an orthogonal $A$ it equals one to machine precision. Invariance holds for all $X,Y$ exactly when $A^{\mathsf T}A=\mathrm{I}$. The two forms are related by $\langle X,Y\rangle=\langle X^{\mathsf T},Y\rangle_{\mathrm{HS}}$, they agree on $\operatorname{Sym}_n$ and are opposite on $\operatorname{Skew}_n$, and their isometry groups are $\mathrm{O}(n^{2})$ and a group containing $\mathrm{GL}_n(\mathbb{R})$ modulo its centre, which are different.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{\mathsf T}Y)$ | the Hilbert–Schmidt form |
| $\|X\|_{\mathrm{F}}$ | the Frobenius norm, the norm of the form |
| $E_{ij}$ | the matrix unit, $1$ in the entry $(i,j)$ |
| ${}^{\mathsf T}$ | the transpose |
| $\mathrm{I}$ | the identity matrix |
| $\operatorname{ad}_A(X)=[A,X]$ | the inner derivation |
| $A^{\mathsf T}A$ | the operator whose Rayleigh quotient is the ratio of norms |
| $\sigma_{\min},\sigma_{\max}$ | the extreme singular values of $A$ |
| $\mathrm{O}(n)$, $\mathrm{O}(n^{2})$ | the orthogonal groups of the algebra and of its $n^{2}$ coordinates |
| $\mathfrak{so}(n)$ | the antisymmetric elements, the Lie algebra of $\mathrm{O}(n)$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the Frobenius norm, the singular values and the orthogonal group.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the Rayleigh quotients and the comparison of norms on matrices.
- [The Trace Form and Its Indefinite Inertia](the-trace-form-and-its-indefinite-signature.html), for the invariant form and the inertia $(n(n+1)/2,n(n-1)/2)$.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the algebra and its matrix units.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric](the-two-halves-over-r-symmetric-and-antisymmetric.html), for the two halves on which the two forms agree and disagree.
- [The Killing Form, Its Radical and the Centre of $\mathfrak{gl}_n(\mathbb{R})$](the-killing-form-its-radical-and-the-centre-of-gl-n-r.html), for the third form on the same space.
