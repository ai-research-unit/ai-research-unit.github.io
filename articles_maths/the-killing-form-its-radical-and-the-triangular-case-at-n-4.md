# __The Killing Form, Its Radical and the Triangular Case at $n=4$__

## Introduction

**The Killing form of $\mathfrak{gl}_4(\mathbb{C})$ is $K(X,Y)=8\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$, its radical is the line of scalars, so the algebra is reductive and not semisimple; on $\mathfrak{sl}_4$ the formula collapses to $8\operatorname{tr}(XY)$ and is non-degenerate; on the Borel it is $4\operatorname{tr}(XY)-\operatorname{tr}X\operatorname{tr}Y$, with radical the scalars together with $\mathfrak{n}_+$, of dimension $7$, and rank $3$.**

The article computes the formula and the constant $2n=8$, identifies the radical on the full algebra, proves non-degeneracy on the traceless algebra by Cartan's criterion, computes the Borel case where the form vanishes on the derived algebra, and shows the two $\mathfrak{sl}_2$ ideals of $\mathfrak{so}(4)$ orthogonal for $K$.

It assumes *The Trace Form and Its Inertia on the Two Halves of $M_4(\mathbb{C})$* for the trace pairing and *The Lie Algebra $\operatorname{Skew}_4\cong\mathfrak{so}(4)$* for the split. The general case at every order is *The Killing Form, Its Radical and the Triangular Case*; the trace form on the Borel is *The Antisymmetric Part inside $UT_4$: the Radical as the Commutator*.

## The Formula on the Full Algebra

**Definition.** $K(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$, where $\operatorname{ad}_X(Z)=[X,Z]$.

**Theorem.** $K(X,Y)=8\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$ on $\mathfrak{gl}_4(\mathbb{C})$.

**Proof.** In the matrix-unit basis, $\operatorname{ad}_X(E_{ij})=XE_{ij}-E_{ij}X=\sum_k x_{ki}E_{kj}-\sum_l x_{jl}E_{il}$. The coefficient of $E_{ij}$ in its own image is $x_{ii}-x_{jj}$; the other coefficients are $x_{ki}$ in the slot $(kj)\leftarrow(ij)$ and $-x_{jl}$ in the slot $(il)\leftarrow(ij)$. In $\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$ the two off-diagonal families pair against one another and cancel, leaving the diagonal sum

$$
\sum_{i,j}(x_{ii}-x_{jj})(y_{ii}-y_{jj})=2n\sum_i x_{ii}y_{ii}-2\Bigl(\sum_i x_{ii}\Bigr)\Bigl(\sum_j y_{jj}\Bigr),
$$

since each diagonal entry is counted once for every index it is subtracted from. With $n=4$ this is $8\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$.

**Corollary.** $K$ is symmetric, bilinear and invariant: $K([X,Y],Z)=K(X,[Y,Z])$.

**Proof.** The trace of a product is symmetric in the factors, and the invariance is the cyclic invariance read through $\operatorname{tr}([\operatorname{ad}_X,\operatorname{ad}_Y]\operatorname{ad}_Z)$.

**The check on the scalar.** $K(\mathrm I_4,Y)=8\operatorname{tr}Y-2\cdot4\operatorname{tr}Y=0$ for every $Y$.

**Proof.** Substitute $X=\mathrm I_4$ and $\operatorname{tr}\mathrm I_4=4$.

## The Constant $2n$

**Proposition.** For $\mathfrak{gl}_n$ the constant is $2n$, so it is $8$ at order four, and it counts the two orders of each pair of distinct indices.

**Proof.** The expansion of the diagonal sum above produces the factor $n$ because each diagonal entry $x_{ii}y_{ii}$ occurs once for every index $j$, and the two cross sums subtract the same total twice.

**Corollary.** In the traceless algebra the trace terms vanish and the formula is $8\operatorname{tr}(XY)$.

**Proof.** $\operatorname{tr}X=\operatorname{tr}Y=0$ on $\mathfrak{sl}_4$.

**The dependence on the order.** The constant grows with $n$, so the Killing form of $\mathfrak{gl}_4$ is not the restriction of the Killing form of a larger algebra: the normalisation is intrinsic and must be computed, not guessed.

**Proof.** The constant $2n$ depends on the dimension of the algebra on which $\operatorname{ad}$ acts.

## The Radical and Reductivity

**Theorem.** The radical of $K$ on $\mathfrak{gl}_4$ is $\mathbb{C}\mathrm I_4$, of dimension $1$.

**Proof.** $K(\mathrm I_4,Y)=0$ gives one inclusion. Conversely, if $K(X,Y)=0$ for all $Y$, take $Y=E_{ij}$: then $8x_{ji}-2\operatorname{tr}X\,\delta_{ij}=0$. For $i\neq j$ this gives $x_{ji}=0$, so $X$ is diagonal; for $i=j$ it gives $8x_{ii}=2\operatorname{tr}X$, so all diagonal entries are equal and $X$ is a scalar.

**Corollary.** $\mathfrak{gl}_4$ is reductive and not semisimple, and $K$ is degenerate with a one-dimensional radical.

**Proof.** A semisimple algebra has non-degenerate Killing form, and the radical found above is the centre.

**Corollary.** The form descends to $\mathfrak{gl}_4/\mathbb{C}\mathrm I_4\cong\mathfrak{sl}_4$, where it is non-degenerate.

**Proof.** The descended form is defined on the quotient by the radical, and it is the restriction of $K$ to any complement.

**The complement.** On the traceless part the form is $8\operatorname{tr}(XY)$, and it is non-degenerate there.

**Proof.** If $\operatorname{tr}(XY)=0$ for every traceless $Y$ then $X$ is a scalar, and a traceless scalar is zero.

## The Traceless Algebra

**Theorem (Cartan's criterion).** The Killing form of $\mathfrak{sl}_4$ is non-degenerate, equivalently $\mathfrak{sl}_4$ is semisimple.

**Proof.** The form is $8\operatorname{tr}(XY)$ and the non-degeneracy is the computation above; the criterion states that a Lie algebra is semisimple exactly when its Killing form is non-degenerate.

**Corollary.** $\mathfrak{sl}_4$ is a direct sum of simple ideals, and here there is one, of dimension $15$.

**Proof.** Semisimplicity gives a sum of simples, and $\mathfrak{sl}_4$ is simple.

**Corollary.** The invariant symmetric forms on $\mathfrak{sl}_4$ are the multiples of $K$, and every derivation of it is inner.

**Proof.** For a simple algebra the invariant forms are proportional; inner-ness of derivations is the standard consequence of semisimplicity.

**The inertia.** On the real traceless algebra the form $8\operatorname{tr}(XY)$ is positive definite on the traceless symmetric part of dimension $9$ and negative definite on the antisymmetric part of dimension $6$.

**Proof.** The signs are those of the trace pairing, computed in the article on the two halves, and $9+6=15$.

## The Borel and Cartan's Criterion

**Theorem.** On $\mathfrak{b}=\mathfrak{h}\oplus\mathfrak{n}_+$ the Killing form is $K_{\mathfrak{b}}(X,Y)=4\operatorname{tr}(XY)-\operatorname{tr}X\operatorname{tr}Y$; its radical is $\mathbb{C}\mathrm I_4\oplus\mathfrak{n}_+$, of dimension $7$; its rank is $3$.

**Proof.** In an upper triangular basis $\operatorname{ad}_X$ is upper triangular, with eigenvalue $x_{ii}-x_{jj}$ on the root space $\mathbb{C}E_{ij}$ and eigenvalue $0$ on $\mathfrak{h}$. Hence

$$
K_{\mathfrak{b}}(X,Y)=\sum_{i<j}(x_{ii}-x_{jj})(y_{ii}-y_{jj})=\tfrac12\Bigl(8\operatorname{tr}(D_XD_Y)-2\operatorname{tr}X\operatorname{tr}Y\Bigr)=4\operatorname{tr}(D_XD_Y)-\operatorname{tr}X\operatorname{tr}Y,
$$

where only the diagonal parts enter. The radical is the set of $X$ with $4\operatorname{tr}(D_XD_Y)=\operatorname{tr}X\operatorname{tr}Y$ for all $Y\in\mathfrak{b}$; taking $Y=E_{ii}$ forces $4x_{ii}=\operatorname{tr}X$ for every $i$, so $D_X$ is a scalar matrix and the strictly upper part is free. That space is $\mathbb{C}\mathrm I_4\oplus\mathfrak{n}_+$ of dimension $7$, and the rank is $10-7=3$.

**Corollary.** $K_{\mathfrak{b}}(\mathfrak{b},[\mathfrak{b},\mathfrak{b}])=0$, since $[\mathfrak{b},\mathfrak{b}]=\mathfrak{n}_+$ lies in the radical; this is Cartan's criterion for solvability read on the form.

**Proof.** The derived algebra is contained in the radical, and the radical pairs to zero with everything.

**Corollary.** $\mathfrak{b}$ is solvable and not reductive, and its rank $3$ is the rank of $\mathfrak{sl}_4$, the dimension of the traceless diagonal.

**Proof.** The rank computation, and $\mathfrak{h}_0$ has dimension $3$.

**The comparison with the trace form.** The trace form on $\mathfrak{b}$ has radical exactly $\mathfrak{n}_+$, of dimension $6$, and rank $4$; the Killing form has radical the scalars together with $\mathfrak{n}_+$, of dimension $7$, and rank $3$. The difference is the scalar line, which the trace form pairs non-degenerately and the Killing form kills.

**Proof.** $K(\mathrm I_4,Y)=0$ for every $Y$, while $\beta(\mathrm I_4,E_{ii})=1$.

## The Two Ideals of $\mathfrak{so}(4)$

**Theorem.** On $\mathfrak{so}(4)$ the Killing form is $8\operatorname{tr}(XY)$, negative definite, and the two $\mathfrak{sl}_2$ ideals are orthogonal.

**Proof.** Every element of $\mathfrak{so}(4)$ is traceless, so the formula reduces to $8\operatorname{tr}(XY)$, negative definite there. For a self-dual $\omega$ and an anti-self-dual $\tau$ the product $\omega\tau$ has zero trace, so $K(\omega,\tau)=0$.

**Corollary.** $\mathfrak{so}(4)=\mathfrak{sl}_2\oplus\mathfrak{sl}_2$ is a direct sum of orthogonal ideals, and $K$ is non-degenerate on each summand.

**Proof.** Orthogonality together with non-degeneracy on the sum gives non-degeneracy on each summand.

**Corollary.** Each summand carries one Casimir, and the two scales are independent.

**Proof.** On a simple algebra the invariant symmetric forms are proportional to $K$, and a direct sum gives one scale per summand.

**The three signs.** The form is negative definite on $\mathfrak{so}(4)$, positive definite on the traceless symmetric part, and zero on the scalars; the three statements together are the inertia of the trace pairing, read on $K$.

**Proof.** $K$ has the sign of $8\operatorname{tr}(XY)$ on traceless elements, and it vanishes on the scalars.

## Summary

The Killing form of $\mathfrak{gl}_4$ is $8\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$, with radical the scalars: the algebra is reductive and not semisimple. On $\mathfrak{sl}_4$ it is $8\operatorname{tr}(XY)$ and non-degenerate, so the traceless algebra is semisimple, which is Cartan's criterion.

On the Borel the form is $4\operatorname{tr}(XY)-\operatorname{tr}X\operatorname{tr}Y$, with radical the scalars together with $\mathfrak{n}_+$, of dimension $7$, and rank $3$. It vanishes on the derived algebra, so the Borel is solvable and not reductive, and the rank $3$ is the rank of $\mathfrak{sl}_4$. The trace form differs from it by exactly the scalar line.

On $\mathfrak{so}(4)$ the form is negative definite and the two $\mathfrak{sl}_2$ ideals are orthogonal, each with its own Casimir.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$ | the Killing form |
| $8\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$ | its value on $\mathfrak{gl}_4$ |
| $\mathbb{C}\mathrm I_4$ | the radical on the full algebra |
| $\mathbb{C}\mathrm I_4\oplus\mathfrak{n}_+$ | the radical on the Borel, dimension $7$ |
| $4\operatorname{tr}(XY)-\operatorname{tr}X\operatorname{tr}Y$ | its value on the Borel |
| $\mathfrak{sl}_2\oplus\mathfrak{sl}_2$ | the two orthogonal ideals of $\mathfrak{so}(4)$ |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the computation of the Killing form of $\mathfrak{gl}_n$ and Cartan's criteria.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the radical, semisimplicity and solvability criteria.
- [The Killing Form, Its Radical and the Triangular Case](the-killing-form-its-radical-and-the-triangular-case.html), for the same computation at general order.
- [The Lie Algebra $\operatorname{Skew}_4\cong\mathfrak{so}(4)$](the-lie-algebra-skew-4-and-so-4.html), for the two ideals and their brackets.
- [The Trace Form and Its Inertia on the Two Halves of $M_4(\mathbb{C})$](the-trace-form-and-its-inertia-on-the-two-halves-of-m4c.html), for the form that differs from $K$ by the scalar line.
