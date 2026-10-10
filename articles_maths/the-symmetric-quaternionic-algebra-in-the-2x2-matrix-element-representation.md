# __The Symmetric Quaternionic Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$__

## Introduction

The symmetric quaternionic multiplication is the central-valued operation $\tilde P\star\tilde Q=B(\tilde P,\tilde Q)e_0$ (*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*). This article reads the operation in the $2\times2$ matrix model, the realisation $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*; it is the first of the two representation articles of the block, and its companion *The Symmetric Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* repeats the reading on the left regular representation. In the model the product of two elements becomes the symmetrisation of a matrix product, the matrix of the quaternion conjugation acts on it, and the value is a scalar matrix whose coefficient is the quaternion form $B$; the article records the trace and the rank of the resulting endomorphism and the matrix form of the form.

The model itself, the isomorphism $\mathsf{M}_2$, the trace $\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_0$, the determinant $\det\mathsf{M}_2(\tilde Q)=N(\tilde Q)$ and the matrix of the conjugation as the adjugate are those of the cited articles and are used here, not restated. The form $B$ and its Gram matrix are *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*; the operators are *The Multiplication Operators of the Symmetric Quaternionic Algebra*; the normal forms of the singular matrices are *Biquaternion 2×2 Matrix Element Representation*. Nothing of the enriched layer is used.

**Conventions.** The product is $\tilde P\star\tilde Q=B(\tilde P,\tilde Q)e_0$ with $B(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$; the realisation is $\mathsf{M}_2$, an algebra isomorphism with $\mathsf{M}_2(e_0)=I_2$ and $\mathsf{M}_2(e_k)=-i\sigma_k$; the adjugate of a matrix is written $\operatorname{adj}$, and it is the matrix of the natural conjugation, $\mathsf{M}_2(\tilde Q^{\natural})=\operatorname{adj}\mathsf{M}_2(\tilde Q)$.

## The Symmetrisation of the Matrix Product

**Proposition (the symmetrisation of the matrix product).** For all $\tilde P,\tilde Q$,

$$
\mathsf{M}_2\bigl(\tilde P\star\tilde Q\bigr)
= \tfrac12\Bigl(\operatorname{adj}\bigl(\mathsf{M}_2(\tilde P)\bigr)\mathsf{M}_2(\tilde Q)
+ \operatorname{adj}\bigl(\mathsf{M}_2(\tilde Q)\bigr)\mathsf{M}_2(\tilde P)\Bigr)
= B(\tilde P,\tilde Q)\,I_2 .
$$

*Proof.* The realisations of the two summands of $\tilde P\star\tilde Q$ are
$\mathsf{M}_2(\tilde P^{\natural}\tilde Q)=\mathsf{M}_2(\tilde P^{\natural})\mathsf{M}_2(\tilde Q)=\operatorname{adj}(\mathsf{M}_2(\tilde P))\mathsf{M}_2(\tilde Q)$ and its exchange, since $\mathsf{M}_2$ is an algebra isomorphism and
the image of the conjugation is the adjugate (*The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*). The half-sum
is the image of the product, and it equals $\mathsf{M}_2(B(\tilde P,\tilde Q)e_0)=B(\tilde P,\tilde Q)I_2$ because the
value is central. Verified on random pairs. $\square$

**Corollary (trace of the value).** Taking the trace of the display,

$$
\operatorname{Tr}\mathsf{M}_2\bigl(\tilde P\star\tilde Q\bigr) = 2\,B(\tilde P,\tilde Q),
$$

so the quaternion form is half the trace of the matrix of the value, and the value is recovered from its trace
as $\mathsf{M}_2(\tilde P\star\tilde Q)=\tfrac12\operatorname{Tr}\mathsf{M}_2(\tilde P\star\tilde Q)\,I_2$. Verified on the model.

**Remark (the adjugate is the conjugation).** The matrix of the quaternion conjugation in the model is the
adjugate, $\mathsf{M}_2(\tilde Q^{\natural})=\operatorname{adj}(\mathsf{M}_2(\tilde Q))=\epsilon\mathsf{M}_2(\tilde Q)^{\mathsf T}\epsilon^{-1}$
with $\epsilon=i\sigma_2$ (*The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*). The symmetrisation is therefore
read on the pair as the half-sum of the two products in which one factor is adorned with the conjugation, and
the identity $\operatorname{adj}(\mathsf{M}_2(\tilde P))\mathsf{M}_2(\tilde Q)+\operatorname{adj}(\mathsf{M}_2(\tilde Q))\mathsf{M}_2(\tilde P)=2B(\tilde P,\tilde Q)I_2$
is the matrix form of the centrality of the operation.

**Proposition (the resulting endomorphism).** Fix $\tilde A$ and let $A=\mathsf{M}_2(\tilde A)$. The endomorphism of
$M_2(\mathbb{C})$ given by

$$
X \longmapsto \tfrac12\Bigl(\operatorname{adj}(A)\,X + \operatorname{adj}(X)\,A\Bigr)
$$

is complex-linear, its image is the line $\mathbb{C}I_2$ of the scalar matrices, its rank is $1$ for
$\tilde A\ne0$, and its trace is $\tilde A_0$. The endomorphism is the transport of the multiplication
$L^{\star}_{\tilde A}$ by the realisation.

*Proof.* For $2\times2$ matrices the adjugate is linear in the entries,
$\operatorname{adj}(X)=\begin{pmatrix}x_{22}&-x_{12}\\-x_{21}&x_{11}\end{pmatrix}$, so the map is linear. Its
image is contained in the scalar matrices by the identity of the first proposition. It is not the zero map for
$\tilde A\ne0$: the image of $X=\mathsf{M}_2(e_\mu)$ is the scalar $B(\tilde A,e_\mu)=\tilde A_\mu$, and some
coordinate $\tilde A_\mu$ is nonzero, so the image is a nonzero line and the rank is $1$. The trace is computed
as the sum of the diagonal coefficients and equals $\tilde A_0$, the trace of $L^{\star}_{\tilde A}$ in
*The Multiplication Operators of the Symmetric Quaternionic Algebra* (both for a non-isotropic and for an
isotropic $\tilde A$, the trace being $\tilde A_0$ in either case). Verified on general elements. $\square$

**Remark (the kernel).** The vectors of the kernel of the endomorphism are the matrices $X$ with
$B(\tilde A,\mathsf{M}_2^{-1}(X))=0$, a linear hyperplane of complex dimension $3$ in $M_2(\mathbb{C})$ (the kernel is
a linear subspace, not an affine one; the affine hyperplanes are the level sets $B(\tilde A,\mathsf{M}_2^{-1}(X))=c$
with $c\ne0$).

## The Matrix Form of the Form

**Proposition (the form as a trace pairing).** The quaternion form reads

$$
B(\tilde P,\tilde Q) = \tfrac12\operatorname{Tr}\Bigl(\operatorname{adj}\bigl(\mathsf{M}_2(\tilde P)\bigr)\mathsf{M}_2(\tilde Q)\Bigr),
$$

so the form in the model is the trace pairing $\operatorname{Tr}(\operatorname{adj}(\mathsf{M}_2(\tilde P))\mathsf{M}_2(\tilde Q))$, equal to $2B(\tilde P,\tilde Q)$.

*Proof.* The identity is the trace of the product
$\operatorname{adj}(\mathsf{M}_2(\tilde P))\mathsf{M}_2(\tilde Q)=\mathsf{M}_2(\tilde P^{\natural}\tilde Q)$, whose trace is $2B(\tilde P,\tilde Q)$. Verified on random pairs. $\square$

**Proposition (the isotropic cone).** An element is isotropic, $N(\tilde Q)=0$, exactly when its image is singular:

$$
N(\tilde Q)=0 \quad\Longleftrightarrow\quad \det\mathsf{M}_2(\tilde Q)=0 ,
$$

the determinant being $N(\tilde Q)$. The Gram matrix of $B$ in the basis is $I_4$.

*Proof.* $\det\mathsf{M}_2(\tilde Q)=N(\tilde Q)$ is the trace-and-determinant theorem of *Introduction to the 2×2
Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, so the determinant vanishes together with $N$. The Gram matrix is the table of
*The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*. $\square$

**Remark (the definite rows in the model).** Under $\mathsf{M}_2$ the definite rows are read through the subspace
conditions of the two representation articles: the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the fixed
space of complex conjugation, is the set of elements with real coefficients, on which the form is positive
definite, and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ is its image under the multiplication by
$i$, on which the form is negative definite. The Hermitian subspace $\mathbb{M}_+$, the fixed space of Hermitian
conjugation, is realised by the matrices equal to their conjugate transpose, and the form has signature
$(1,3)$ on it. The correspondence is the one of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* and
*Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, which own the subspace conditions.

## Worked Examples

**The unit and a vector.** For $\tilde P=e_0$ and $\tilde Q=e_1$ the product is $B(e_0,e_1)e_0=0$, and the
matrix identity reads $\tfrac12(\mathsf{M}_2(e_1)+\operatorname{adj}(\mathsf{M}_2(e_1)))=0$, the two summands being opposite
because $\operatorname{adj}(\mathsf{M}_2(e_1))=\mathsf{M}_2(e_1^{\natural})=-\mathsf{M}_2(e_1)$.

**A central pair.** For $\tilde P=e_0$, $\tilde Q=ie_0$ the product is $ie_0$ and the coefficient is $B=i$;
the matrix of the value is $iI_2$, of trace $2i$ and determinant $i^2=-1=N(ie_0)$.

**A vector square.** For $\tilde P=\tilde Q=e_1$ the product is $e_0$, and the identity gives
$\operatorname{adj}(\mathsf{M}_2(e_1))\mathsf{M}_2(e_1)=I_2$, since $\mathsf{M}_2(e_1)$ is invertible of determinant $N(e_1)=1$; the
symmetrisation of the product with itself is the product itself and equals $I_2$.

**An isotropic element.** For $\tilde Q=e_0+ie_1$ the norm is $N=1+i^2=0$, so $\mathsf{M}_2(\tilde Q)$ is singular of
rank one and the matrix identity gives
$\tfrac12(\operatorname{adj}(\mathsf{M}_2(\tilde Q))\mathsf{M}_2(\tilde Q)+\operatorname{adj}(\mathsf{M}_2(\tilde Q))\mathsf{M}_2(\tilde Q))=0$,
the zero scalar matrix, although $\mathsf{M}_2(\tilde Q)\ne0$.

**A pair with a real coefficient.** For $\tilde P=e_0+e_1$ and $\tilde Q=e_0-e_1$ the coefficient is
$B=1-1=0$, so the symmetrised matrix product vanishes: two nonzero matrices symmetrise to $0$. The two are the
images of conjugate directions, and their images are related by the adjugate, which is why the cross terms
cancel in the symmetrisation.

## The Matrices

**The generators.** The realization is fixed on the basis by four matrices:

$$
\mathsf{M}_2(e_0)=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
\mathsf{M}_2(e_1)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
\mathsf{M}_2(e_2)=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\mathsf{M}_2(e_3)=\begin{pmatrix}-i&0\\0&i\end{pmatrix}.
$$

A general element has the matrix $\mathsf{M}_2(\tilde Q)$ of trace $2Q_0$ and determinant $N(\tilde Q)$.

**The value, entry by entry.** The symmetrisation of the two adjugated products is the scalar matrix of the form, and the involution reduces it: since $\operatorname{adj}X=(\operatorname{Tr}X)I-X$, the value is the scalar-plus-anticommutator expression

$$
\tfrac12\Bigl(\operatorname{adj}(X)\,Y+\operatorname{adj}(Y)\,X\Bigr)
=P_0Y+Q_0X-\tfrac12\bigl\{X,Y\bigr\}
=B(\tilde P,\tilde Q)\,I_2,
$$

the two scalar multiples carrying the $P_0$ and $Q_0$ parts of the form and the anticommutator the rest. At the pair $e_1,e_1$ the reduction reads $\operatorname{adj}\mathsf{M}_2(e_1)\mathsf{M}_2(e_1)=I_2=B(e_1,e_1)I_2$, the matrix being its own adjugate up to sign.

**The trace of the value, entry by entry.** The trace of the value is twice the form, $\operatorname{Tr}\mathsf{M}_2(\tilde P\star\tilde Q)=2B(\tilde P,\tilde Q)$, and at the pair $e_1,e_1$ it is $\operatorname{Tr}I_2=2=2B(e_1,e_1)$; at the isotropic element $e_0+ie_1$ the value is the zero scalar matrix, $\mathsf{M}_2(e_0+ie_1)=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ being singular of rank one.

## Summary

In the $2\times2$ model the symmetric quaternionic multiplication reads
$\tfrac12(\operatorname{adj}(\mathsf{M}_2(\tilde P))\mathsf{M}_2(\tilde Q)+\operatorname{adj}(\mathsf{M}_2(\tilde Q))\mathsf{M}_2(\tilde P))=B(\tilde P,\tilde Q)I_2$,
the adjugate being the matrix of the quaternion conjugation, and the trace of the value is $2B(\tilde P,\tilde Q)$;
the resulting endomorphism of $M_2(\mathbb{C})$ has image the scalar matrices, rank $1$ and trace
$\tilde P_0$. The form is half the trace of the twisted matrix product,
$B=\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_2(\tilde P)\,\mathsf{M}_2(\tilde Q))$; the isotropic elements are exactly the
singular matrices, the determinant of the model being $N(\tilde Q)$; the Gram matrix in the basis is $I_4$; and
the definite rows and the two Hermitian subspaces are read through the subspace conditions of the two
representation articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ | the $2\times2$ realisation, $\mathsf{M}_2(e_0)=I_2$, $\det\mathsf{M}_2(\tilde Q)=N(\tilde Q)$ |
| $\operatorname{adj}$ | the adjugate, the matrix of the quaternion conjugation in the model |
| $\mathsf{M}_2(\tilde P\star\tilde Q)=\tfrac12(\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)+\operatorname{adj}\mathsf{M}_2(\tilde Q)\mathsf{M}_2(\tilde P))=B(\tilde P,\tilde Q)I_2$ | the product in the model |
| $\operatorname{Tr}\mathsf{M}_2(\tilde P\star\tilde Q)=2B(\tilde P,\tilde Q)$ | the trace of the value |
| $B=\tfrac12\operatorname{Tr}(\operatorname{adj}\mathsf{M}_2(\tilde P)\,\mathsf{M}_2(\tilde Q))$ | the form as a trace pairing |
| $N(\tilde Q)=0\Longleftrightarrow\det\mathsf{M}_2(\tilde Q)=0$ | the isotropic cone as the singular matrices |

## Further Reading

- *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-element-representation-of-biquaternions.md`), for the realisation, the trace and the determinant
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), for the adjugate and the singular elements
- *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra* (`articles_maths/the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra.md`), for the form $B$ and its Gram matrix
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra.md`), for the operators transported by the model
- *The Symmetric Quaternionic Algebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-symmetric-quaternionic-algebra-in-the-4x4-matrix-element-representation.md`), for the reading on the left regular representation
- *Introduction to the Symmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-biquaternions.md`), for the operation itself
