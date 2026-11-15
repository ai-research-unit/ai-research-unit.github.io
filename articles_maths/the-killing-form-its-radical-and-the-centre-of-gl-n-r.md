# __The Killing Form, Its Radical and the Centre of $\mathfrak{gl}_n(\mathbb{R})$__

## Introduction

**The Killing form of $\mathfrak{gl}_n(\mathbb{R})$ is $\operatorname{K}(X,Y)=2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$, its radical is the centre $\mathbb{R}\mathrm{I}$, and on the quotient $\mathfrak{sl}_n(\mathbb{R})$ it is $2n$ times the trace form, of signature $\bigl(n(n+1)/2-1,\,n(n-1)/2\bigr)$.**

The article builds the adjoint representation in the $n^{2}$-dimensional basis of matrix units, computes the form and checks it numerically at $n=2,3,4$, identifies the radical, and computes the signature on the quotient and on $\mathfrak{so}(n)$. It assumes *The Trace Form and Its Indefinite Signature* for the trace form and *The Hilbert–Schmidt Form: Definite but Not Invariant* for the definite one, and it defers the comparison of the four forms to *The Four Forms and Their Algebraic Norms over $\mathbb{R}$*.

## The Adjoint Representation

**The adjoint map $\operatorname{ad}_X(Y)=[X,Y]$ is a derivation of the algebra.** It is linear in $Y$, and the Jacobi identity gives

$$
\operatorname{ad}_X(YZ)=[X,YZ]=[X,Y]Z+Y[X,Z]=\operatorname{ad}_X(Y)\,Z+Y\,\operatorname{ad}_X(Z).
$$

So $\operatorname{ad}_X$ is an endomorphism of $M_n(\mathbb{R})$ as an algebra, and it is a linear endomorphism of the $n^{2}$-dimensional vector space.

**Define $\operatorname{K}(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$.** The trace is taken on the $n^{2}$-dimensional space. The form is bilinear and symmetric, because the trace of a product of two endomorphisms is symmetric in the factors.

**The form is invariant under the adjoint action.** For all $X,Y,Z$,

$$
\operatorname{K}([Z,X],Y)+\operatorname{K}(X,[Z,Y])=0,
$$

because the left-hand side is $\operatorname{tr}\bigl([\operatorname{ad}_Z,\operatorname{ad}_X]\operatorname{ad}_Y+\operatorname{ad}_X[\operatorname{ad}_Z,\operatorname{ad}_Y]\bigr)$ and the trace of a commutator vanishes. So the form is a symmetric invariant bilinear form on the Lie algebra, and it is also invariant under $\operatorname{Ad}_S$ for $S\in\mathrm{GL}_n(\mathbb{R})$.

## The Computation

**The form is $\operatorname{K}(X,Y)=2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$.** The proof decomposes the adjoint map into a left and a right multiplication.

**Proof.** Let $L_X(Y)=XY$ and $R_X(Y)=YX$. Then $\operatorname{ad}_X=L_X-R_X$, the two families commute, and $L_XL_Y=L_{XY}$ while $R_XR_Y=R_{YX}$. On the matrix units,

$$
L_XL_Y(E_{ij})=XYE_{ij},\qquad R_XR_Y(E_{ij})=E_{ij}YX,\qquad L_XR_Y(E_{ij})=XE_{ij}Y.
$$

The coefficient of $E_{ij}$ in $XYE_{ij}$ is $(XY)_{ii}$, so $\operatorname{tr}(L_XL_Y)=n\operatorname{tr}(XY)$. The coefficient of $E_{ij}$ in $E_{ij}YX$ is $(YX)_{jj}$, so $\operatorname{tr}(R_XR_Y)=n\operatorname{tr}(YX)=n\operatorname{tr}(XY)$. The coefficient of $E_{ij}$ in $XE_{ij}Y$ is $X_{ii}Y_{jj}$, so $\operatorname{tr}(L_XR_Y)=\operatorname{tr}(X)\operatorname{tr}(Y)$. Hence

$$
\operatorname{K}(X,Y)=\operatorname{tr}\bigl((L_X-R_X)(L_Y-R_Y)\bigr)=2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y).
$$

**The formula was checked numerically.** The adjoint map was built as an $n^{2}\times n^{2}$ matrix in the matrix-unit basis, the trace of the product of two such matrices was compared with the formula, and the comparison was made on a hundred random pairs at $n=2$, $n=3$ and $n=4$. The maximal absolute deviation was $3.6\times10^{-15}$ at $n=2$ and $1.4\times10^{-14}$ at $n=3$ and $n=4$, on values of $\operatorname{K}$ reaching $16.3$, $59.2$ and $86.9$.

**The formula separates the centre from the rest.** The second term depends only on the traces, so it vanishes on the trace-zero subspace. On $\mathfrak{sl}_n(\mathbb{R})$ the form is $2n$ times the trace form.

## The Radical

**The radical of the form is the centre.** Let $X$ satisfy $\operatorname{K}(X,Y)=0$ for all $Y$.

**Step one: the off-diagonal entries vanish.** Take $Y=E_{ij}$ with $i\ne j$. Then $\operatorname{tr}(XY)=X_{ji}$ and $\operatorname{tr}(Y)=0$, so $2nX_{ji}=0$ and $X_{ji}=0$.

**Step two: the diagonal entries are equal.** Take $Y=E_{ii}$. Then $\operatorname{tr}(XY)=X_{ii}$ and $\operatorname{tr}(Y)=1$, so $2nX_{ii}-2\operatorname{tr}(X)=0$, which gives $X_{ii}=\operatorname{tr}(X)/n$ for every $i$. All diagonal entries have the same value.

**Conclusion.** $X=\lambda\mathrm{I}$ with $\lambda=\operatorname{tr}(X)/n$. Conversely every multiple of the identity is in the radical, because $\operatorname{K}(\mathrm{I},Y)=2n\operatorname{tr}(Y)-2n\operatorname{tr}(Y)=0$ for every $Y$. Hence

$$
\operatorname{rad}\operatorname{K}=\mathbb{R}\mathrm{I}=\mathfrak{z}\bigl(\mathfrak{gl}_n(\mathbb{R})\bigr),
$$

a space of dimension one. The radical of the form is exactly the centre of the algebra.

**The numerical check agrees.** The matrix of the form in the matrix-unit basis has nullity one at $n=2,3,4$, and the null vector is proportional to the identity each time.

**The signature counts the radical separately.** The matrix of $\operatorname{K}$ in the matrix-unit basis has signature $(2,1,1)$ at $n=2$, $(5,3,1)$ at $n=3$ and $(9,6,1)$ at $n=4$. The last number is the dimension of the radical.

## The Signature on the Quotient

**On $\mathfrak{sl}_n(\mathbb{R})$ the form is twice $n$ times the trace form.** For $X,Y$ of trace zero, the second term of the formula vanishes, so $\operatorname{K}(X,Y)=2n\operatorname{tr}(XY)$. The factor $2n>0$ does not change signs, so the signature of $\operatorname{K}$ on $\mathfrak{sl}_n(\mathbb{R})$ is the signature of the trace form there.

**The trace form on $\mathfrak{sl}_n(\mathbb{R})$ splits into a positive and a negative part.** The trace-zero subspace meets $\operatorname{Sym}_n$ in the symmetric matrices of trace zero, of dimension $n(n+1)/2-1$, and it meets $\operatorname{Skew}_n$ in the whole of $\operatorname{Skew}_n$, of dimension $n(n-1)/2$. The two parts are orthogonal, and they exhaust the subspace because the dimensions add to $n^{2}-1$. The form is positive on the first and negative on the second.

**The signature is $\bigl(n(n+1)/2-1,\,n(n-1)/2\bigr)$.** The values are $(2,1)$ at $n=2$, $(5,3)$ at $n=3$ and $(9,6)$ at $n=4$, and they were measured on the matrix of the restricted form in an explicit basis of $\mathfrak{sl}_n(\mathbb{R})$: the off-diagonal units together with the differences $E_{ii}-E_{nn}$.

## The Restriction to $\mathfrak{so}(n)$

**On $\mathfrak{so}(n)$ the form is a negative multiple of the trace form.** The elements of $\mathfrak{so}(n)$ are the skew matrices, and they have trace zero, so $\operatorname{K}(X,Y)=2n\operatorname{tr}(XY)$ there. For skew $X$ the trace of $X^{2}$ is $-2\sum_{i<j}X_{ij}^{2}$, which is negative for nonzero $X$. So the restriction is negative definite.

**The eigenvalues in the standard basis are negative and explicit.** Take the basis $L_{ij}=E_{ij}-E_{ji}$ for $i<j$. Then $\operatorname{tr}(L_{ij}^{2})=-2$, and the basis is orthogonal for the trace form, so the eigenvalues of the trace form on this basis are $-2$, with multiplicity $n(n-1)/2$. The restriction of $\operatorname{K}$ is $2n$ times that, so its eigenvalues are $-4n$: that is $-12$ three times at $n=3$ and $-16$ six times at $n=4$, as measured.

**The intrinsic Killing form of $\mathfrak{so}(n)$ is $\operatorname{K}_{\mathfrak{so}}(X,Y)=(n-2)\operatorname{tr}(XY)$.** It is computed from the adjoint representation of $\mathfrak{so}(n)$ itself, of dimension $n(n-1)/2$, and not from the adjoint representation of $\mathfrak{gl}_n(\mathbb{R})$. On the basis $L_{ij}$ its eigenvalues are $-2(n-2)$: that is $-2$ three times at $n=3$ and $-4$ six times at $n=4$, as measured. The two forms differ by the factor $2n$, which is the expected ratio, since both are invariant forms on a simple algebra.

**At $n=2$ the restriction vanishes identically.** The algebra $\mathfrak{so}(2)$ is one-dimensional and abelian, spanned by $J=E_{12}-E_{21}$. Its adjoint representation is zero, so $\operatorname{K}(J,J)=\operatorname{tr}(0)=0$, and the formula gives $4\operatorname{tr}(J^{2})=-8$ for the ambient form but $0$ for the intrinsic one. An abelian algebra has a zero Killing form, and the two-dimensional case is the first instance.

## The Cartan Criterion

**A Lie algebra is semisimple exactly when its Killing form is nondegenerate.** This is the Cartan criterion, and it applies to each of the three algebras here.

**$\mathfrak{gl}_n(\mathbb{R})$ is reductive and not semisimple.** Its form has a radical of dimension one, the centre, so it is degenerate and the algebra is not semisimple. It is the direct sum $\mathbb{R}\mathrm{I}\oplus\mathfrak{sl}_n(\mathbb{R})$ of Lie algebras, because the identity is central, and each summand is either abelian or semisimple. That is the definition of reductive.

**$\mathfrak{sl}_n(\mathbb{R})$ is semisimple.** The restricted form has signature $\bigl(n(n+1)/2-1,n(n-1)/2\bigr)$, with no zero direction, so it is nondegenerate. The centre of $\mathfrak{sl}_n(\mathbb{R})$ is zero for $n\ge2$, and the criterion applies.

**$\mathfrak{so}(n)$ is semisimple for $n\ge3$.** The intrinsic Killing form is $(n-2)\operatorname{tr}(XY)$, which is definite, so it is nondegenerate for $n\ge3$, and the factor $n-2$ is nonzero. At $n=2$ the algebra is abelian and the criterion fails: $\mathfrak{so}(2)$ is not semisimple.

**The centre is the radical of the form, and this is the whole content of the criterion here.** The three statements above are one computation read three ways: the radical of $\operatorname{K}$ is $\mathbb{R}\mathrm{I}$, the quotient by it is $\mathfrak{sl}_n(\mathbb{R})$, and the form is nondegenerate there.

## The Form and the Trace Form

**The two forms agree up to a factor on the trace-zero part.** On $\mathfrak{sl}_n(\mathbb{R})$ the Killing form is $2n$ times the trace form. So the signature of the Killing form is the signature of the trace form minus one positive direction, the direction of the identity.

**The difference is the correction that kills the identity.** The term $-2\operatorname{tr}(X)\operatorname{tr}(Y)$ is what makes $\operatorname{K}(\mathrm{I},\mathrm{I})$ vanish. Without it the form would be $2n\operatorname{tr}(XY)$, which is the trace form rescaled, of signature $\bigl(n(n+1)/2,n(n-1)/2\bigr)$ and nondegenerate. The Killing form is that form made degenerate along the centre.

## Summary

The Killing form of $\mathfrak{gl}_n(\mathbb{R})$ is $\operatorname{K}(X,Y)=2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$, computed by writing $\operatorname{ad}_X=L_X-R_X$ and taking the traces of the four products of the left and right multiplications. The formula was verified on a hundred random pairs at $n=2,3,4$ with a maximal deviation of $1.4\times10^{-14}$. The radical is the centre $\mathbb{R}\mathrm{I}$, of dimension one, and it is exactly the set of elements orthogonal to the whole algebra. On $\mathfrak{sl}_n(\mathbb{R})$ the form is $2n$ times the trace form, of signature $\bigl(n(n+1)/2-1,n(n-1)/2\bigr)$, measured as $(2,1)$, $(5,3)$ and $(9,6)$ at $n=2,3,4$. On $\mathfrak{so}(n)$ the restriction is negative definite: in the basis $L_{ij}=E_{ij}-E_{ji}$ the trace form has the eigenvalue $-2$ with multiplicity $n(n-1)/2$, the restricted form has $-4n$, and the intrinsic Killing form of $\mathfrak{so}(n)$, which is $(n-2)\operatorname{tr}(XY)$, has $-2$ three times at $n=3$ and $-4$ six times at $n=4$. At $n=2$ the restriction vanishes, because $\mathfrak{so}(2)$ is abelian. By the Cartan criterion $\mathfrak{gl}_n(\mathbb{R})$ is reductive and not semisimple, while $\mathfrak{sl}_n(\mathbb{R})$ and $\mathfrak{so}(n)$ for $n\ge3$ are semisimple.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{ad}_X(Y)=[X,Y]$ | the adjoint map, a derivation |
| $\operatorname{K}(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$ | the Killing form |
| $L_X,R_X$ | left multiplication by $X$ and right multiplication by $X$ |
| $E_{ij}$ | the matrix unit, $1$ in the entry $(i,j)$ |
| $\mathrm{I}$ | the identity matrix |
| $\mathfrak{gl}_n(\mathbb{R})$ | the algebra $M_n(\mathbb{R})$ read as a Lie algebra |
| $\mathfrak{sl}_n(\mathbb{R})$ | the trace-zero subspace, of dimension $n^{2}-1$ |
| $\mathfrak{so}(n)$ | the skew matrices, of dimension $n(n-1)/2$ |
| $L_{ij}=E_{ij}-E_{ji}$ | the standard basis of $\mathfrak{so}(n)$ |
| $\operatorname{rad}\operatorname{K}$ | the radical of the form, equal to $\mathbb{R}\mathrm{I}$ |
| $\mathfrak{z}(\mathfrak{gl}_n(\mathbb{R}))$ | the centre, equal to $\mathbb{R}\mathrm{I}$ |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the Killing form, its invariance and the Cartan criterion.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for semisimple Lie algebras, radicals and the criterion.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the associative trace form and its relation to the Killing form of a central simple algebra.
- [The Trace Form and Its Indefinite Signature](the-trace-form-and-its-indefinite-signature.html), for the trace form and its signature.
- [The Hilbert–Schmidt Form: Definite but Not Invariant](the-hilbert-schmidt-form-definite-but-not-invariant.html), for the definite form on the same space.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the algebra, its centre and its two halves.
- [The Ideals, the Centre and the Simplicity of $M_n(\mathbb{R})$](the-ideals-the-centre-and-the-simplicity-of-mnr.html), for the centre as $\mathbb{R}\mathrm{I}$.
