# __The Killing Form of $\mathfrak{sl}_2$ and Its Three Signatures__

## Introduction

**The Killing form of $\mathfrak{sl}_2$ is four times the trace form, and its signature is $(2,1)$ on the split real form, $(0,3)$ on the compact form $\mathfrak{su}(2)$ and $(3,3)$ on the complex form read over the reals.**

The article defines the Killing form, proves the formula $K(X,Y)=4\operatorname{tr}(XY)$ on the traceless matrices, computes the Gram matrix in the basis $H,E,F$ with eigenvalues $-4,4,8$, computes the negative definite form of $\mathfrak{su}(2)$ in the basis $i\sigma_{k}/2$ with eigenvalues $-2,-2,-2$, computes the form of $\mathfrak{sl}_2(\mathbb{C})$ over $\mathbb{R}$ with the signature $(3,3)$, and explains what the three signs mean. It assumes *The Lie Algebra $\operatorname{Skew}_2$: One Dimension, Hence Abelian*, *The Derivation $X\mapsto[A,X]$ and Its Anti-Self-Adjointness for the Trace Form* and *The Trace Form and Its Signature on the Two Halves of $M_2(\mathbb{R})$*.

It defers the Hilbert–Schmidt form to *The Hilbert–Schmidt Form at $n=2$* and the four forms with their norms to *The Four Forms and Their Algebraic Norms at $n=2$*.

## The Definition

**Definition.** The **Killing form** of a Lie algebra is $K(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$, the trace of the product of the two adjoint operators.

**Proposition.** The form is symmetric and invariant: $K([X,Y],Z)+K(Y,[X,Z])=0$.

**Proof.** A trace of a product is symmetric in the two factors, which gives the symmetry; the invariance is the cyclicity of the trace applied to $\operatorname{ad}_{[X,Y]}=[\operatorname{ad}_X,\operatorname{ad}_Y]$.

**Corollary.** The radical of the form is an ideal, and the form is nondegenerate exactly when the algebra is semisimple over a field of characteristic zero.

**Proof.** Invariance makes the radical stable under the adjoint action, and the criterion of Cartan says that a Lie algebra is semisimple exactly when its Killing form is nondegenerate.

**At order two the algebra is small enough to compute the form by hand.** The adjoint representation is three-dimensional on $\mathfrak{sl}_2$, so the form is a $3\times3$ matrix of traces of products of $3\times3$ matrices.

## The Formula on the Traceless Matrices

**Theorem.** On $\mathfrak{sl}_2(\mathbb{C})$ the Killing form is

$$
K(X,Y)=4\operatorname{tr}(XY).
$$

**Proof.** The adjoint representation of $\mathfrak{sl}_2$ is the fundamental representation tensored with its dual, so its character is $\chi(X)\overline{\chi(Y)}$ and $\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)=2n\operatorname{tr}(XY)$ with $n=2$ for the two-dimensional fundamental representation, which gives the constant $4$.

**Corollary.** The Killing form is four times the trace form, so it vanishes on the scalars, and on the traceless matrices it inherits the splitting of the trace form.

**Proof.** The two forms agree up to the constant, and the trace form was computed in *The Trace Form and Its Signature on the Two Halves of $M_2(\mathbb{R})$*.

**Corollary.** In the basis $H=\sigma_{3}$, $E=E_{12}$, $F=E_{21}$ the Gram matrix of the Killing form is

$$
\begin{pmatrix}8&0&0\\ 0&0&4\\ 0&4&0\end{pmatrix}.
$$

**Proof.** $4\operatorname{tr}(H^{2})=8$ and $4\operatorname{tr}(EF)=4$, while the other pairings vanish.

## The Split Form

**Theorem.** The eigenvalues of the Killing form of $\mathfrak{sl}_2(\mathbb{R})$ are $-4$, $4$ and $8$, so its signature is $(2,1)$.

**Proof.** The characteristic polynomial of the displayed matrix is $(8-\lambda)(\lambda^{2}-16)$, whose roots are $8$, $4$ and $-4$; two are positive and one is negative.

**Corollary.** The form is positive definite on the traceless symmetric plane and negative definite on the antisymmetric line, so the two halves of the algebra separate by the sign of the form.

**Proof.** $K(\sigma_{3},\sigma_{3})=K(\sigma_{1},\sigma_{1})=8$ and $K(J,J)=4\operatorname{tr}(J^{2})=-8$.

**Corollary.** $\mathfrak{sl}_2(\mathbb{R})$ is semisimple but not compact, and its Killing form is nondegenerate and indefinite.

**Proof.** The form is nondegenerate because its three eigenvalues are nonzero, and it is indefinite because the signs differ; the compact algebras are exactly those with a negative definite Killing form.

## The Compact Form

**Theorem.** In the basis $X_{1}=i\sigma_{1}/2$, $X_{2}=i\sigma_{2}/2$, $X_{3}=i\sigma_{3}/2$ of $\mathfrak{su}(2)$ the Killing form is $-2$ times the identity, so its eigenvalues are $-2,-2,-2$ and its signature is $(0,3)$.

**Proof.** $4\operatorname{tr}(X_{j}X_{k})=4\cdot(-\tfrac14\cdot2\delta_{jk})=-2\delta_{jk}$, since $\operatorname{tr}(\sigma_{j}\sigma_{k})=2\delta_{jk}$ and the two factors of $i$ give $-1$.

**Corollary.** The form is negative definite, and $\mathfrak{su}(2)$ is a compact real form of $\mathfrak{sl}_2$.

**Proof.** Every eigenvalue is negative; and a real form whose Killing form is negative definite is compact by the criterion of Cartan.

**Corollary.** The two real forms have opposite signs, and the passage from one to the other multiplies the form by $-1$ on the traceless part.

**Proof.** The values $8$ and $-2$ differ in sign, and the basis change from $H$ to $X_{3}$ is the multiplication by $i/2$, which changes the real form.

**The compact form is the one of the unitary matrices.** The anti-Hermitian traceless matrices form the Lie algebra of $\mathrm{SU}(2)$, which is diffeomorphic to the sphere $S^{3}$ and hence compact.

**Proof.** $\mathrm{SU}(2)$ is the group of unitary two-by-two matrices of determinant one, and its Lie algebra is the space of traceless anti-Hermitian matrices.

## The Complex Form over the Reals

**Theorem.** Read over the reals, $\mathfrak{sl}_2(\mathbb{C})$ has dimension $6$ and its Killing form has the eigenvalues $-8,-4,-4,4,4,8$, with signature $(3,3)$.

**Proof.** A real basis is $H,E,F,iH,iE,iF$. The real part of the form sends a pair of real matrices $(A,B)$ to $4\bigl(\operatorname{tr}(A^{2})-\operatorname{tr}(B^{2})\bigr)$, and the Gram matrix of that quadratic form in the six-element basis has the characteristic polynomial with the roots $-8,-4,-4,4,4,8$.

**Corollary.** The real part is the difference of two trace forms, positive of signature $(2,1)$ on the traceless real matrices and negative of signature $(1,2)$ on the imaginary ones.

**Proof.** On the traceless matrices of $M_2(\mathbb{R})$ the trace form has signature $(2,1)$, as computed in the section on the split form, and the minus sign reverses the two counts.

**Corollary.** The three signatures $(2,1)$, $(0,3)$ and $(3,3)$ come from the two real forms and from the complex form read over the reals, and the complex form is not the complexification of either form read on the real algebra alone.

**Proof.** The first two signatures are those of the two real forms; the third is that of the complex algebra with the real part of the complex bilinear form, which mixes the two real directions instead of adding their signatures.

## What the Three Signs Mean

**Proposition.** The sign of the Killing form measures the compactness of the real form: negative definite for the compact one, indefinite for the split one.

**Proof.** Cartan's criterion states that a real semisimple Lie algebra is compact exactly when its Killing form is negative definite, and the two computations above give the two cases.

**Corollary.** The compact form has no nonzero nilpotent element in its image under the trace form, while the split form has the nilpotent line of the strictly triangular matrices.

**Proof.** On $\mathfrak{su}(2)$ the form is $-2$ times the identity, so every nonzero element has a nonzero square length; on $\mathfrak{sl}_2(\mathbb{R})$ the element $E_{12}$ is nilpotent and is isotropic for the form.

**Corollary.** The trace form of the algebra and the Killing form of the traceless part are proportional, so the sign difference between the two real forms is visible already in the elementary trace.

**Proof.** $K=4\operatorname{tr}$ on the traceless part, and the trace form has signature $(3,1)$ on the real algebra with the traceless part of signature $(2,1)$ and the antisymmetric line negative.

## Summary

The Killing form of $\mathfrak{sl}_2$ is $K(X,Y)=4\operatorname{tr}(XY)$. In the basis $H,E,F$ of the split form its Gram matrix is $\begin{pmatrix}8&0&0\\ 0&0&4\\ 0&4&0\end{pmatrix}$ with eigenvalues $-4,4,8$ and signature $(2,1)$, positive on the traceless symmetric plane and negative on the antisymmetric line.

On the compact form $\mathfrak{su}(2)$, in the basis $i\sigma_{k}/2$, the form is $-2$ times the identity with eigenvalues $-2,-2,-2$ and signature $(0,3)$, so the form is negative definite and the algebra is compact. On $\mathfrak{sl}_2(\mathbb{C})$ read over the reals the eigenvalues are $-8,-4,-4,4,4,8$ with signature $(3,3)$, the complexification of the two real forms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K(X,Y)$ | $\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$, the Killing form |
| $H,E,F$ | $\sigma_{3}$, $E_{12}$, $E_{21}$, the basis of the split form |
| $X_{k}$ | $i\sigma_{k}/2$, the basis of $\mathfrak{su}(2)$ |
| $\operatorname{ad}_X$ | the operator $Y\mapsto[X,Y]$ |
| $\operatorname{tr}(XY)$ | the trace form, proportional to $K$ on the traceless part |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Geometric Analysis* (AMS, 2001), for the Killing form, its signature and the compactness criterion.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2002), for the real forms of $\mathfrak{sl}_2$ and their Cartan decompositions.
- [The Trace Form and Its Signature on the Two Halves of $M_2(\mathbb{R})$](the-trace-form-and-its-signature-on-the-two-halves-of-m2r.html), for the trace form that the Killing form multiplies by four.
- [The Lie Algebra $\operatorname{Skew}_2$: One Dimension, Hence Abelian](the-lie-algebra-skew-2-one-dimension-hence-abelian.html), for the antisymmetric line on which the form is negative.
- [The Derivation $X\mapsto[A,X]$ and Its Anti-Self-Adjointness for the Trace Form](the-derivation-commutator-and-its-anti-self-adjointness-for-the-trace-form.html), for the adjoint operators whose traces define the form.
