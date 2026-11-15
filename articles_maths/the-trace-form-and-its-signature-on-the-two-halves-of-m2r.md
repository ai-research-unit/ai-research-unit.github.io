# __The Trace Form and Its Signature on the Two Halves of $M_2(\mathbb{R})$__

## Introduction

**The form $\langle X,Y\rangle=\operatorname{tr}(XY)$ on $M_2(\mathbb{R})$ is symmetric, nondegenerate and of signature $(3,1)$, positive definite on the symmetric half and negative definite on the antisymmetric line, so the real matrix algebra carries the geometry of a four-dimensional Minkowski space.**

The article polarises the quadratic form $\operatorname{tr}(X^{2})$, exhibits an orthogonal basis with the signs $+1,+1,+1,-1$, describes the isotropic cone and its cone of light, reads the form through Cayley–Hamilton as $(\operatorname{tr}X)^{2}-2\det X$, and identifies the Lie algebra of the isometry group with the image of the adjoint action. It assumes *The Two Halves as Orthogonal Complements at $n=2$*, *The Derivation $X\mapsto[A,X]$ and Its Anti-Self-Adjointness for the Trace Form* and *The Elementary Symmetric Functions: $\operatorname{tr}$ and $\det$ in Dimension Two*.

It defers the Killing form to *The Killing Form of $\mathfrak{sl}_2$ and Its Three Signatures*, the Hilbert–Schmidt form to *The Hilbert–Schmidt Form at $n=2$*, and the four forms with their norms to *The Four Forms and Their Algebraic Norms at $n=2$*.

## The Form and Its Polarisation

**Definition.** The **trace form** on $M_2(\mathbb{R})$ is $\langle X,Y\rangle=\operatorname{tr}(XY)$, the polar form of the quadratic form $Q(X)=\operatorname{tr}(X^{2})$.

**Proposition.** The form is symmetric and nondegenerate.

**Proof.** $\operatorname{tr}(XY)=\operatorname{tr}(YX)$ by cyclicity. If $\operatorname{tr}(XY)=0$ for every $Y$ then taking $Y=E_{ji}$ gives $x_{ij}=0$ for every pair of indices, so $X=0$.

**Corollary.** The polarisation $\langle X,Y\rangle=\tfrac12\bigl(Q(X+Y)-Q(X)-Q(Y)\bigr)$ recovers the form from the quadratic form, so the two carry the same information.

**Proof.** Expand $Q(X+Y)=\operatorname{tr}(X^{2})+\operatorname{tr}(Y^{2})+2\operatorname{tr}(XY)$ and compare.

**The form is the derivative of the determinant along the diagonal.** At the identity one has $\det(I+tX)=1+t\operatorname{tr}(X)+t^{2}\det(X)$, so the linear term is the trace, and the quadratic term is the determinant.

**Proof.** Expand the determinant of $I+tX$ in the two eigenvalues, or use the Cayley–Hamilton identity at $I$.

## The Gram Matrix and the Signs

**Theorem.** In the basis $I/\sqrt2$, $\sigma_{3}/\sqrt2$, $\sigma_{1}/\sqrt2$, $J/\sqrt2$ the Gram matrix of the trace form is $\operatorname{diag}(1,1,1,-1)$.

**Proof.** $\operatorname{tr}(I^{2})=\operatorname{tr}(\sigma_{3}^{2})=\operatorname{tr}(\sigma_{1}^{2})=2$ and $\operatorname{tr}(J^{2})=-2$, while every mixed pairing vanishes by *The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$ at $n=2$*.

**Corollary.** The signature is $(3,1)$: the form is positive definite of rank $3$ on the symmetric half and negative definite of rank $1$ on the antisymmetric line.

**Proof.** The Gram matrix in these coordinates is diagonal with three entries $+1$ and one entry $-1$, and the two halves are the spans of the first three and of the last basis vector.

**Corollary.** The symmetric half is positive definite and the antisymmetric line is the unique timelike direction, up to the sign of the vector.

**Proof.** The restriction of the form to $\operatorname{Sym}_2$ is positive definite with eigenvalues $1,1,2$ in the Pauli basis, as computed in *The Two Halves as Orthogonal Complements at $n=2$*, and the restriction to the line is $-2c^{2}$ at $cJ$.

## The Isotropic Cone

**Theorem.** A matrix $X=S+cJ$ with $S$ symmetric is isotropic for the trace form exactly when $\operatorname{tr}(S^{2})=2c^{2}$.

**Proof.** $\operatorname{tr}((S+cJ)^{2})=\operatorname{tr}(S^{2})+2c\operatorname{tr}(SJ)+c^{2}\operatorname{tr}(J^{2})=\operatorname{tr}(S^{2})-2c^{2}$, since $SJ$ is antisymmetric and traceless.

**Corollary.** The isotropic cone is a double cone over the ellipsoid $\operatorname{tr}(S^{2})=2$ in the symmetric half, and its two nappes are separated by the sign of $c$.

**Proof.** The equation is $c^{2}=\tfrac12\operatorname{tr}(S^{2})$, which gives two values of $c$ for each direction $S$ and one point $S=0$, $c=0$.

**Corollary.** The cone contains no nonzero symmetric matrix, and every nonzero isotropic matrix has a nonzero antisymmetric part.

**Proof.** On the symmetric half the form is positive definite, so $\operatorname{tr}(S^{2})=0$ only for $S=0$, and the equation then forces $c=0$.

**The cone is the light cone of a Lorentz form.** The level sets $\operatorname{tr}(X^{2})=1$ are the hyperboloids of a Minkowski space of dimension four, and the two halves are the space directions and the time direction.

**Proof.** The Gram matrix is $\operatorname{diag}(1,1,1,-1)$, which is the standard Lorentz form in four dimensions after a linear change of coordinates.

## The Cayley–Hamilton Reading

**Proposition.** For every two-by-two matrix

$$
\operatorname{tr}(X^{2})=\bigl(\operatorname{tr}X\bigr)^{2}-2\det X .
$$

**Proof.** The eigenvalues $\lambda_{1},\lambda_{2}$ give $\operatorname{tr}(X^{2})=\lambda_{1}^{2}+\lambda_{2}^{2}$ and $(\operatorname{tr}X)^{2}-2\det X=(\lambda_{1}+\lambda_{2})^{2}-2\lambda_{1}\lambda_{2}=\lambda_{1}^{2}+\lambda_{2}^{2}$.

**Corollary.** The sign of $Q$ is the sign of $(\operatorname{tr}X)^{2}-2\det X$, so $Q$ vanishes on the cone $\det X=\tfrac12(\operatorname{tr}X)^{2}$ and is negative on the matrices whose determinant is large with respect to their trace, such as $J$.

**Proof.** The identity writes the form as a difference of the two invariants, and $\det J=1$ with $\operatorname{tr}J=0$ gives $Q(J)=-2$.

**Corollary.** On the traceless plane the form is $-\operatorname{tr}(X^{2})=2\det X$ up to sign, so the form and the determinant carry the same data there.

**Proof.** With $\operatorname{tr}X=0$ the identity gives $\operatorname{tr}(X^{2})=-2\det X$.

## The Isometry Group

**Theorem.** The isometry group of the trace form is $\mathrm{O}(3,1)$, of dimension $6$.

**Proof.** The isometry group of a nondegenerate form of signature $(3,1)$ on a space of dimension four is the orthogonal group of that signature, and the dimension of the orthogonal group of a form in $n$ dimensions is $n(n-1)/2=6$ for $n=4$.

**Corollary.** The Lie algebra of the isometry group is the space of endomorphisms $T$ with $\langle TX,Y\rangle+\langle X,TY\rangle=0$, of dimension $6$.

**Proof.** The Lie algebra of a linear group is the tangent space at the identity, which consists of the endomorphisms $T$ with $e^{tT}$ an isometry to the first order, and that condition is the display.

**Theorem.** The adjoint action embeds $\mathfrak{sl}_2(\mathbb{R})$ into the isometry algebra, as the copy of $\mathfrak{so}(2,1)$.

**Proof.** Every $\operatorname{ad}_A$ is anti-self-adjoint for the form by *The Derivation $X\mapsto[A,X]$ and Its Anti-Self-Adjointness for the Trace Form*, the kernel of the adjoint action is the scalars, and the traceless algebra has dimension $3$; the compact dual of $\mathfrak{sl}_2(\mathbb{R})$ is $\mathfrak{so}(3)$ and the split one is $\mathfrak{so}(2,1)$, so the image is the split copy.

**Corollary.** The conjugation $X\mapsto gXg^{-1}$ by $g\in\mathrm{SL}_2(\mathbb{R})$ is an isometry, and these are the isometries produced by the adjoint action.

**Proof.** $\operatorname{tr}(gXg^{-1}\,gYg^{-1})=\operatorname{tr}(XY)$ for every invertible $g$, and the derivative at the identity is $\operatorname{ad}_A$ with $A$ traceless.

**The one-sided multiplications are not isometries.** The map $X\mapsto JX$ does not preserve the form, since $\langle JI,JI\rangle=\operatorname{tr}(J^{2})=-2$ while $\langle I,I\rangle=2$; so the isometry algebra is not obtained by multiplying on one side.

**Proof.** The value at the identity matrix is computed directly, and an isometry cannot change the squared length of a vector.

**Corollary.** The isometry algebra is strictly larger than the image of the adjoint action, by three dimensions, and it is not generated by the one-sided multiplications of the algebra.

**Proof.** The image has dimension $3$ and the algebra has dimension $6$; and the multiplication on one side already fails at the single vector $I$.

## Summary

The trace form $\langle X,Y\rangle=\operatorname{tr}(XY)$ on $M_2(\mathbb{R})$ is symmetric and nondegenerate, with Gram matrix $\operatorname{diag}(1,1,1,-1)$ in the normalised Pauli basis, hence of signature $(3,1)$: positive definite on the symmetric half and negative definite on the antisymmetric line.

The form is the polar form of $\operatorname{tr}(X^{2})$, which Cayley–Hamilton writes as $(\operatorname{tr}X)^{2}-2\det X$; its isotropic cone is the double cone $c^{2}=\tfrac12\operatorname{tr}(S^{2})$ over the ellipsoid in the symmetric half, and the isometry group is $\mathrm{O}(3,1)$ of dimension $6$, whose Lie algebra receives the adjoint action of the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle X,Y\rangle$ | $\operatorname{tr}(XY)$, the trace form |
| $Q(X)$ | $\operatorname{tr}(X^{2})$, the quadratic form |
| $\sigma_{3},\sigma_{1}$ | traceless symmetric Pauli matrices |
| $J$ | the antisymmetric unit, the timelike direction |
| $\mathrm{O}(3,1)$ | the isometry group of the form |
| $\mathfrak{so}(2,1)$ | the three-dimensional part of the isometry algebra |

## Further Reading

- Barrett O'Neill, *Semi-Riemannian Geometry* (Academic Press, 1983), for forms of signature $(3,1)$ and their isotropic cones.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the trace form and the Cayley–Hamilton identity.
- [The Two Halves as Orthogonal Complements at $n=2$](the-two-halves-as-orthogonal-complements-at-n-2.html), for the Gram matrices of the two halves.
- [The Derivation $X\mapsto[A,X]$ and Its Anti-Self-Adjointness for the Trace Form](the-derivation-commutator-and-its-anti-self-adjointness-for-the-trace-form.html), for the anti-self-adjoint endomorphisms of the form.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-2.html), for the two halves and their dimensions.
