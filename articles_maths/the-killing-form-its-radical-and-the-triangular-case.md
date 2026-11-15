# __The Killing Form, Its Radical and the Triangular Case__

## Introduction

**The Killing form of $\mathfrak{gl}_n$ is $2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$, its radical is the centre $\mathbb{C}\mathrm{I}$, and on the antisymmetric half it takes the two different values $(n-2)\operatorname{tr}(XY)$ and $2n\operatorname{tr}(XY)$ according to whether it is computed inside the half or in the whole algebra; on $UT_n$ it has rank $n-1$ and radical $n_+\oplus\mathbb{R}\mathrm{I}$.**

The article computes the form from the derivation matrices, identifies the radical, gives the signature on the traceless algebra, resolves the two values on $\mathfrak{so}(n)$, and computes the triangular case as the contrast. It assumes *The Derivation $X\mapsto[A,X]$ and Its Skewness for the Trace Form* for the derivation trace form and *The Trace Form and Its Signature on the Two Halves* for the signatures. It defers the Cartan criterion to *Symmetric Pairs and Cartan Pairs: the Reductivity Criterion* and the group theory to *The Cartan Decomposition of $\mathrm{GL}_n(\mathbb{C})$*.

## The Killing Form of $\mathfrak{gl}_n$

**The Killing form is computed from the derivation matrices.** With $\operatorname{ad}$ as in *The Derivation $X\mapsto[A,X]$ and Its Skewness for the Trace Form*,

$$
B(X,Y)=\operatorname{tr}\big(\operatorname{ad}_X\operatorname{ad}_Y\big).
$$

Building the matrices of $\operatorname{ad}$ in the basis of the $n^{2}$ units and taking the trace gives

$$
B(X,Y)=2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y),
$$

which was verified at $n=2,3,4$ on random pairs, the two sides agreeing to machine precision. The formula is symmetric, bilinear and vanishes when either argument is a scalar matrix.

**The formula is the trace form corrected by the trace terms.** Since $\operatorname{tr}(XY)$ alone is not invariant under the full adjoint action of $\mathfrak{gl}_n$ up to the centre, the correction $-2\operatorname{tr}(X)\operatorname{tr}(Y)$ is exactly what removes the contribution of the scalar part. On the traceless part the correction vanishes and

$$
B(X,Y)=2n\operatorname{tr}(XY)\qquad(X,Y\in\mathfrak{sl}_n),
$$

so the Killing form of $\mathfrak{sl}_n$ is $2n$ times the trace form, which was verified at $n=2,3,4$.

**The form is invariant under all derivations.** For every $A$,

$$
B([A,X],Y)+B(X,[A,Y])=0,
$$

which follows from the formula and was checked numerically. So the Killing form is the invariant form that the derivation algebra acts by skew maps, and it is the form used in the reductivity criterion.

## The Radical and the Reductive Splitting

**The radical is the centre.** Write $X=X_0+\tfrac1n\operatorname{tr}(X)\mathrm{I}$ with $X_0$ traceless. Then

$$
B(X,Y)=2n\operatorname{tr}(X_0Y),
$$

so $B(X,Y)=0$ for all $Y$ exactly when $\operatorname{tr}(X_0Y)=0$ for all traceless $Y$, which happens exactly when $X_0=0$. Hence

$$
\operatorname{rad}B=\mathbb{C}\mathrm{I},\qquad \dim\operatorname{rad}B=1 .
$$

So the algebra is reductive and not semisimple, with a one-dimensional radical spanned by the identity.

**The Killing form is the orthogonal sum of a nondegenerate form and a zero form.** The line $\mathbb{C}\mathrm{I}$ is orthogonal to everything and carries the zero form, and on $\mathfrak{sl}_n$ the form is nondegenerate. So

$$
\mathfrak{gl}_n=\mathfrak{sl}_n\perp\mathbb{C}\mathrm{I},\qquad B|_{\mathfrak{sl}_n}\ \text{nondegenerate},\qquad B|_{\mathbb{C}\mathrm{I}}=0,
$$

which is Cartan's criterion read in the simplest case: a Lie algebra is semisimple exactly when its Killing form is nondegenerate, and $\mathfrak{gl}_n$ fails by exactly the centre.

**The two halves are not orthogonal for the Killing form.** Since the correction term involves traces, a symmetric and an antisymmetric matrix still pair through $2n\operatorname{tr}(SK)$, so the Killing form is $2n$ times the trace form on the whole algebra and the orthogonality of the halves is inherited from the trace form. What changes is the sign pattern, not the blocks.

## The Signature on $\mathfrak{sl}_n$

**On the real traceless algebra the signature is inherited from the trace form, scaled by $2n$.** Since $B=2n\operatorname{tr}$ there and $2n>0$, the signs are those of *The Trace Form and Its Signature on the Two Halves*:

$$
\operatorname{sig}\big(B|_{\mathfrak{sl}_n(\mathbb{R})}\big)=\Big(\frac{n(n+1)}{2}-1,\ \frac{n(n-1)}{2}\Big)=(2,1),\ (5,3),\ (9,6)\quad(n=2,3,4).
$$

So the form is indefinite for every $n\ge2$, of positive index $\tfrac12n(n+1)-1$ and negative index $\tfrac12n(n-1)$, and the two add to $n^{2}-1$.

**The negative directions are the rotations and the positive directions are the stretches.** The antisymmetric matrices give the negative part and the traceless symmetric matrices the positive part, with the split at the level of the trace form. So the Killing form of $\mathfrak{sl}_n(\mathbb{R})$ is negative on the compact direction and positive on the non-compact one, and the compact form $\mathfrak{su}(n)$ is the subalgebra on which it is negative definite.

**On $\mathfrak{su}(n)$ the form is negative definite.** For $X\in\mathfrak{su}(n)$, $X^{*}=-X$ and $X$ is traceless, so

$$
B(X,X)=2n\operatorname{tr}(X^{2})=-2n\operatorname{tr}(XX^{*})<0 .
$$

So the compact real form is exactly the negative definite part, and the index of the form on $\mathfrak{sl}_n(\mathbb{R})$ counts the non-compact directions.

## The Two Halves and the Two Values of the Form

**Inside the antisymmetric half the Killing form is $(n-2)\operatorname{tr}(XY)$, and in the whole algebra it is $2n\operatorname{tr}(XY)$.** Both statements are correct and they refer to different algebras:

$$
B_{\mathfrak{so}(n)}(X,Y)=(n-2)\operatorname{tr}(XY),\qquad B_{\mathfrak{gl}_n}(X,Y)\big|_{X,Y\in\mathfrak{so}(n)}=2n\operatorname{tr}(XY),
$$

which were computed separately at $n=2,3,4$: the first by building the derivations inside $\mathfrak{so}(n)$ alone, the second by building them in $\mathfrak{gl}_n$. At $n=2$ the first value is zero, since $\mathfrak{so}(2)$ is abelian, while the second is $4\operatorname{tr}(XY)\neq0$.

**The difference is the contribution of the symmetric half.** The adjoint action of $\mathfrak{so}(n)$ on the complement $\operatorname{Sym}_n$ is nontrivial, so the trace over $\mathfrak{gl}_n$ is the trace over $\mathfrak{so}(n)$ plus the trace over the module $\operatorname{Sym}_n$:

$$
2n\operatorname{tr}(XY)=(n-2)\operatorname{tr}(XY)+c_n\operatorname{tr}(XY),\qquad c_n=n+2 .
$$

So the two values differ by the trace of the action on the symmetric square, and the identity was verified at $n=3,4$ with the computed constant.

**The intrinsic value is the one that decides the structure.** Since $(n-2)\operatorname{tr}(XY)$ is negative definite for $n\ge3$, $\mathfrak{so}(n)$ is compact and semisimple; the ambient value $2n\operatorname{tr}(XY)$ is also negative definite there, so the two agree in sign but differ in scale, and only the intrinsic one is the Killing form of the algebra.

## The Triangular Case

**The Killing form of $UT_n$ vanishes on the commutator.** By Cartan's criterion a Lie algebra is solvable exactly when $B(\mathfrak{g},[\mathfrak{g},\mathfrak{g}])=0$, and $UT_n$ is solvable with commutator $n_+$. So

$$
B\big(UT_n,\,[UT_n,UT_n]\big)=0,
$$

and the radical of $B$ contains $n_+$. The computation confirms it: the form is carried entirely by the diagonal.

**On the diagonal the form is $B(D_\lambda,D_\mu)=n\sum_i\lambda_i\mu_i-\big(\sum_i\lambda_i\big)\big(\sum_i\mu_i\big)$.** With $D_\lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$, the adjoint action on $E_{ij}$ is multiplication by $\lambda_i-\lambda_j$, and only the strictly upper part contributes, so

$$
B(D_\lambda,D_\mu)=\sum_{i<j}(\lambda_i-\lambda_j)(\mu_i-\mu_j)=n\sum_i\lambda_i\mu_i-\sum_i\lambda_i\sum_i\mu_i .
$$

On the units this gives $B(E_{ii},E_{jj})=n\delta_{ij}-1$, which the computation reproduces at $n=2,3,4,5$, and the rank is $n-1$.

**The radical is $n_+\oplus\mathbb{R}\mathrm{I}$.** The kernel of the diagonal form is the line of scalars, and $n_+$ is in the radical by Cartan's criterion, so

$$
\operatorname{rad}B_{UT_n}=n_+\oplus\mathbb{R}\mathrm{I},\qquad \dim=1+\frac{n(n-1)}{2},
$$

which was verified by the rank of the Gram matrix: the ranks are $1,2,3,4$ and the nullities $2,4,7,11$ at $n=2,3,4,5$, equal to $1+n(n-1)/2$ in each case.

**So the two algebras of dimension $n(n+1)/2$ have Killing forms of rank $n(n+1)/2$ and $n-1$.** The symmetric half is not a Lie algebra and has no Killing form of its own, but the comparison is with the antisymmetric half, whose form has full rank: $n(n-1)/2$ on $\mathfrak{so}(n)$ and $n^{2}-1$ on $\mathfrak{sl}_n$. The triangular algebra is the degenerate case, and its degeneracy is the exact measure of its solvability.

## The Case $n=2$

**At $n=2$ the form is $4\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$ with one-dimensional radical.** In the basis $\mathrm{I},J$ of the diagonal algebra,

$$
B(\mathrm{I},\mathrm{I})=0,\qquad B(\mathrm{I},J)=0,\qquad B(J,J)=-8,
$$

which the computation confirms, so the radical is $\mathbb{R}\mathrm{I}$ and the traceless line is negative definite. The antisymmetric half is the traceless line, and the value $-8$ is $2n\operatorname{tr}(J^{2})=4\cdot(-2)$.

**The two values on the antisymmetric line are $0$ and $-8$.** The intrinsic Killing form of $\mathfrak{so}(2)$ vanishes because the algebra is abelian, and the ambient form takes the value $-8$ on $J$; the difference is the action on $\operatorname{Sym}_2$, of constant $c_2=4$. So at $n=2$ the discrepancy between the two values is as large as it can be, since one of them is zero.

**At $n=2$ the triangular algebra has a rank-one Killing form.** $UT_2$ has dimension $3$, the form has rank $1$ and nullity $2$, and on the units

$$
B(E_{11},E_{11})=B(E_{22},E_{22})=1,\qquad B(E_{11},E_{22})=-1,\qquad B(E_{12},\cdot)=0,
$$

which the computation reproduces. So the radical is $n_+\oplus\mathbb{R}\mathrm{I}$, the line of the companion nilpotent plus the line of the identity, and the only nondegenerate direction is the traceless diagonal.

## Summary

The Killing form of $\mathfrak{gl}_n$ is $2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$, its radical is the centre $\mathbb{C}\mathrm{I}$, and on $\mathfrak{sl}_n$ it reduces to $2n\operatorname{tr}(XY)$ with signature $(n(n+1)/2-1,n(n-1)/2)$, negative definite on the compact form $\mathfrak{su}(n)$. On the antisymmetric half the intrinsic value is $(n-2)\operatorname{tr}(XY)$ and the ambient value is $2n\operatorname{tr}(XY)$, differing by the trace of the action on the symmetric square with constant $n+2$. On $UT_n$ the form vanishes on the commutator $n_+$, is $n\sum\lambda_i\mu_i-\sum\lambda\sum\mu$ on the diagonal with rank $n-1$, and has radical $n_+\oplus\mathbb{R}\mathrm{I}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$ | the Killing form |
| $2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$ | its value on $\mathfrak{gl}_n$ |
| $\operatorname{rad}B=\mathbb{C}\mathrm{I}$ | the radical, the centre |
| $(n-2)\operatorname{tr}(XY)$ | the Killing form of $\mathfrak{so}(n)$ computed inside itself |
| $2n\operatorname{tr}(XY)$ | the restriction of the ambient form to $\mathfrak{so}(n)$ |
| $n+2$ | the constant of the difference, the trace on the symmetric square |
| $n\sum\lambda_i\mu_i-\sum\lambda_i\sum\mu_i$ | the form on the diagonal of $UT_n$ |
| $n_+\oplus\mathbb{R}\mathrm{I}$ | the radical of the form on $UT_n$ |

## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the Killing form, Cartan's criterion and reductive algebras.
- Karin Erdmann and Mark J. Wildon, *Introduction to Lie Algebras* (Springer, 2006), for the computation of the Killing form from the adjoint matrices.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the signature of the Killing form and the compact forms.
- [The Derivation $X\mapsto[A,X]$ and Its Skewness for the Trace Form](the-derivation-commutator-and-its-skewness-for-the-trace-form.html), for the derivation trace form that the Killing form is.
- [The Trace Form and Its Signature on the Two Halves](the-trace-form-and-its-signature-on-the-two-halves.html), for the signatures that the form inherits.
- [The Antisymmetric Part inside $UT_n$: the Radical as the Commutator](the-antisymmetric-part-inside-utn-the-radical-as-the-commutator.html), for the solvability that makes the triangular form degenerate.
