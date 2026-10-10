# __The Symmetric Quaternionic Algebra in the Matrix Representations__

## Introduction

The symmetric quaternionic multiplication is the central-valued operation
$\tilde P\star\tilde Q=B(\tilde P,\tilde Q)e_0$ (*Introduction to the Symmetric Quaternionic Algebra of
Biquaternions*). This article reads the operation in the two matrix models of the algebra: the **$2\times2$
model** $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ of *Introduction to the 2×2 Matrix Representation of
Biquaternions*, and the **$4\times4$ regular model** $\rho_L$ of *Biquaternion 4×4 Regular Matrix Element
Representation*. In each, the product of two elements becomes the symmetrisation of a matrix product, the
matrix of the quaternion conjugation acts on it, and the value is a scalar matrix whose coefficient is the
quaternion form $B$; the article records the trace and the rank of the resulting endomorphism and the matrix
form of the form.

The models themselves, the isomorphism $\Phi$, the trace $\operatorname{Tr}\Phi(\tilde Q)=2Q_0$, the
determinant $\det\Phi(\tilde Q)=N(\tilde Q)$, the matrix of the conjugation as the adjugate and the regular
representation are those of the cited articles and are used here, not restated. The form $B$ and its Gram matrix are
*The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*; the operators are *The Multiplication
Operators of the Symmetric Quaternionic Algebra*; the normal forms of the singular matrices are *Biquaternion
2×2 Matrix Element Representation* and *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$*. Nothing of
the enriched layer is used.

**Conventions.** The product is $\tilde P\star\tilde Q=B(\tilde P,\tilde Q)e_0$ with
$B(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$; the realisation is $\Phi$, an algebra isomorphism with
$\Phi(e_0)=I_2$, and the adjugate of a matrix is written $\operatorname{adj}$; the left-regular
representation is $\rho_L(\tilde P)\tilde Q=\tilde P\tilde Q$, with $\rho_L(\tilde P^\natural)=\rho_L(\tilde P)^{\mathsf T}$
in the basis.

## The 2×2 Model

**Proposition (the symmetrisation of the matrix product).** For all $\tilde P,\tilde Q$,

$$
\Phi\bigl(\tilde P\star\tilde Q\bigr)
= \tfrac12\Bigl(\operatorname{adj}\bigl(\Phi(\tilde P)\bigr)\Phi(\tilde Q)
+ \operatorname{adj}\bigl(\Phi(\tilde Q)\bigr)\Phi(\tilde P)\Bigr)
= B(\tilde P,\tilde Q)\,I_2 .
$$

*Proof.* The realisations of the two summands of $\tilde P\star\tilde Q$ are
$\Phi(\tilde P^{\natural}\tilde Q)=\Phi(\tilde P^{\natural})\Phi(\tilde Q)=\operatorname{adj}(\Phi(\tilde P))\Phi(\tilde Q)$ and its exchange, since $\Phi$ is an algebra isomorphism and
the image of the conjugation is the adjugate (*Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$*). The half-sum
is the image of the product, and it equals $\Phi(B(\tilde P,\tilde Q)e_0)=B(\tilde P,\tilde Q)I_2$ because the
value is central. $\square$

**Corollary (trace of the value).** Taking the trace of the display,

$$
\operatorname{Tr}\Phi\bigl(\tilde P\star\tilde Q\bigr) = 2\,B(\tilde P,\tilde Q),
$$

so the quaternion form is half the trace of the matrix of the value, and the value is recovered from its trace
as $\Phi(\tilde P\star\tilde Q)=\tfrac12\operatorname{Tr}\Phi(\tilde P\star\tilde Q)\,I_2$.

**Proposition (the resulting endomorphism).** Fix $\tilde A$ and let $A=\Phi(\tilde A)$. The endomorphism of
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
$\tilde A\ne0$: the image of $X=\Phi(e_\mu)$ is the scalar $B(\tilde A,e_\mu)=\tilde A_\mu$, and some
coordinate $\tilde A_\mu$ is nonzero, so the image is a nonzero line and the rank is $1$. The trace is computed
as the sum of the diagonal coefficients and equals $\tilde A_0$, the trace of $L^{\star}_{\tilde A}$ in
*The Multiplication Operators of the Symmetric Quaternionic Algebra* (both for a non-isotropic and for an
isotropic $\tilde A$, the trace being $\tilde A_0$ in either case). $\square$

**Remark (the adjugate is the conjugation).** The matrix of the quaternion conjugation in the model is the
adjugate, $\Phi(\tilde Q^{\natural})=\operatorname{adj}(\Phi(\tilde Q))=\epsilon\Phi(\tilde Q)^{\mathsf T}\epsilon^{-1}$
with $\epsilon=i\sigma_2$ (*Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$*). The symmetrisation is therefore
read on the pair as the half-sum of the two products in which one factor is adorned with the conjugation, and
the identity $\operatorname{adj}(\Phi(\tilde P))\Phi(\tilde Q)+\operatorname{adj}(\Phi(\tilde Q))\Phi(\tilde P)=2B(\tilde P,\tilde Q)I_2$
is the matrix form of the centrality of the operation. The vectors of the kernel of the endomorphism are the matrices $X$ with
$B(\tilde A,\Phi^{-1}(X))=0$, a linear hyperplane of complex dimension $3$ in $M_2(\mathbb{C})$ (the kernel is
a linear subspace, not an affine one; the affine hyperplanes are the level sets $B(\tilde A,\Phi^{-1}(X))=c$
with $c\ne0$).

## The 4×4 Regular Model

**Proposition (the symmetrisation of the left multiplications).** In the basis $e_0,e_1,e_2,e_3$ the
left-regular representation satisfies $\rho_L(\tilde P^\natural)=\rho_L(\tilde P)^{\mathsf T}$, and for all
$\tilde P,\tilde Q$,

$$
\tfrac12\Bigl(\rho_L(\tilde P)^{\mathsf T}\rho_L(\tilde Q)
+ \rho_L(\tilde Q)^{\mathsf T}\rho_L(\tilde P)\Bigr)
= \rho_L\bigl(\tilde P\star\tilde Q\bigr) = B(\tilde P,\tilde Q)\,I_4 .
$$

*Proof.* The left-regular representation is multiplicative, so
$\rho_L(\tilde P^{\natural}\tilde Q)=\rho_L(\tilde P^\natural)\rho_L(\tilde Q)=\rho_L(\tilde P)^{\mathsf T}\rho_L(\tilde Q)$; the half-sum is $\rho_L$ of the product, and the value is
central, so the matrix is the scalar matrix $B(\tilde P,\tilde Q)I_4$. The transpose identity is read on the
basis: for $\tilde P=e_1$ the matrix $\rho_L(e_1)$ and its transpose are opposite, $\rho_L(e_1)^{\mathsf T}=-\rho_L(e_1)=\rho_L(e_1^\natural)$,
and the general case follows by linearity. $\square$

**Corollary (the regular endomorphism).** Fix $\tilde A$ and let $A=\rho_L(\tilde A)$. On the image of the
regular representation — the matrices $\rho_L(\tilde Q)$ — the map is the transport of the multiplication
$L^{\star}_{\tilde A}$:

$$
X=\rho_L(\tilde Q)\quad\Longrightarrow\quad
\tfrac12\bigl(A^{\mathsf T}X+X^{\mathsf T}A\bigr)
= \rho_L\bigl(\tilde A\star\tilde Q\bigr) = B(\tilde A,\tilde Q)\,I_4 ,
$$

because $X^{\mathsf T}=\rho_L(\tilde Q)^\natural$ on the image of $\rho_L$ by the transpose identity above. On
that four-dimensional space the map has image the line $\mathbb{C}I_4$ of the scalar matrices, rank $1$ for
$\tilde A\ne0$ and trace $\tilde A_0$. The same formula read on the whole of $M_4(\mathbb{C})$ is a larger map:
there $X^{\mathsf T}$ is not the conjugation of an element of $\mathbb{B}$, the image leaves the scalar
matrices, and the rank is larger than one (it is $5$ for $\tilde A=e_1$ and $7$ for a generic $\tilde A$). The
two models differ here because the $2\times2$ realisation is onto $M_2(\mathbb{C})$ — there "all matrices" and
"the image of the realisation" are the same set — while $\rho_L(\mathbb{B})$ is a four-dimensional subspace of
the sixteen-dimensional $M_4(\mathbb{C})$. The rank-one statement is a statement about the transport of the
multiplication, not about the formula on arbitrary matrices.

*Proof.* For $X=\rho_L(\tilde Q)$ one has $A^{\mathsf T}X=\rho_L(\tilde A^\natural)\rho_L(\tilde Q)=\rho_L(\tilde A^\natural\tilde Q)$
and $X^{\mathsf T}A=\rho_L(\tilde Q^\natural)\rho_L(\tilde A)=\rho_L(\tilde Q^\natural\tilde A)$, so the
half-sum is $\rho_L(\tilde A\star\tilde Q)=B(\tilde A,\tilde Q)I_4$. The rank is $1$ because the image is a
nonzero line for $\tilde A\ne0$ (the image of $X=\rho_L(e_\mu)$ is $\tilde A_\mu I_4$) and the trace on the
image of $\rho_L$ is the coefficient of $\rho_L(e_0)$, namely $B(\tilde A,e_0)=\tilde A_0$. On the whole of
$M_4(\mathbb{C})$ the map is larger: on the sixteen matrix units its rank is $5$ for $\tilde A=e_1$ and $7$ for
a generic $\tilde A$, so the rank-one statement must not be read on arbitrary matrices. $\square$

**Remark (the identity in the two models).** The two displays are the same statement transported by the two
models: in the $2\times2$ model the conjugation is the adjugate, in the $4\times4$ model it is the transpose,
and in both the symmetrised product of two matrices is the scalar matrix whose scalar is the quaternion form.
The regular model exhibits the reason more plainly: the four-dimensional regular representation is faithful,
and the transpose of a left multiplication is the left multiplication by the conjugate, which is the identity
$\rho_L(\tilde P^\natural)=\rho_L(\tilde P)^{\mathsf T}$ that makes the symmetrisation central.

## The Matrix Form of the Form

**Proposition (the form in the two models).** The quaternion form reads

$$
B(\tilde P,\tilde Q) = \tfrac12\operatorname{Tr}\Bigl(\operatorname{adj}\bigl(\Phi(\tilde P)\bigr)\Phi(\tilde Q)\Bigr)
= \tfrac14\operatorname{Tr}\Bigl(\rho_L(\tilde P)^{\mathsf T}\rho_L(\tilde Q)\Bigr).
$$

*Proof.* The first identity is the trace of the product $\operatorname{adj}(\Phi(\tilde P))\Phi(\tilde Q)=\Phi(\tilde P^{\natural}\tilde Q)$, whose trace is $2B(\tilde P,\tilde Q)$; the second is the trace of
$\rho_L(\tilde P^{\natural}\tilde Q)$, whose trace is $4\operatorname{Sc}(\tilde P^{\natural}\tilde Q)=4B(\tilde P,\tilde Q)$.
$\square$

**Proposition (the isotropic cone and the Gram matrix).** An element is isotropic, $N(\tilde Q)=0$, exactly
when its image is singular in either model:

$$
N(\tilde Q)=0 \quad\Longleftrightarrow\quad \det\Phi(\tilde Q)=0
\quad\Longleftrightarrow\quad \det\rho_L(\tilde Q)=0 ,
$$

the two determinants being $N(\tilde Q)$ and $N(\tilde Q)^2$. The Gram matrix of $B$ in the basis is $I_4$,
and the form in the $2\times2$ model is the trace pairing
$\operatorname{Tr}(\operatorname{adj}(\Phi(\tilde P))\Phi(\tilde Q))$, equal to $2B(\tilde P,\tilde Q)$.

*Proof.* $\det\Phi(\tilde Q)=N(\tilde Q)$ is the trace-and-determinant theorem of *Introduction to the 2×2
Matrix Representation of Biquaternions*, and $\det\rho_L(\tilde Q)=N(\tilde Q)^2$ is the determinant of the
left regular representation (*Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$*); the two vanish together with $N$. The Gram matrix is the table of
*The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*. $\square$

**Remark (the definite rows in the models).** Under $\Phi$ the definite rows are read through the subspace
conditions of the two representation articles: the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the fixed
space of complex conjugation, is the set of elements with real coefficients, on which the form is positive
definite, and the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ is its image under the multiplication by
$i$, on which the form is negative definite. The Hermitian subspace $\mathbb{M}_+$, the fixed space of Hermitian
conjugation, is realised by the matrices equal to their conjugate transpose, and the form has signature
$(1,3)$ on it. The correspondence is the one of *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$* and
*Introduction to the 2×2 Matrix Representation of Biquaternions*, which own the subspace conditions.

## Worked Examples

**The unit and a vector.** For $\tilde P=e_0$ and $\tilde Q=e_1$ the product is $B(e_0,e_1)e_0=0$, and the
matrix identity reads $\tfrac12(\Phi(e_1)+\operatorname{adj}(\Phi(e_1)))=0$, the two summands being opposite
because $\operatorname{adj}(\Phi(e_1))=\Phi(e_1^{\natural})=-\Phi(e_1)$.

**A central pair.** For $\tilde P=e_0$, $\tilde Q=ie_0$ the product is $ie_0$ and the coefficient is $B=i$;
the matrix of the value is $iI_2$, of trace $2i$ and determinant $i^2=-1=N(ie_0)$.

**A vector square.** For $\tilde P=\tilde Q=e_1$ the product is $e_0$, and the identity gives
$\operatorname{adj}(\Phi(e_1))\Phi(e_1)=I_2$, since $\Phi(e_1)$ is invertible of determinant $N(e_1)=1$; the
symmetrisation of the product with itself is the product itself and equals $I_2$.

**An isotropic element.** For $\tilde Q=e_0+ie_1$ the norm is $N=1+i^2=0$, so $\Phi(\tilde Q)$ is singular of
rank one and the matrix identity gives
$\tfrac12(\operatorname{adj}(\Phi(\tilde Q))\Phi(\tilde Q)+\operatorname{adj}(\Phi(\tilde Q))\Phi(\tilde Q))=0$,
the zero scalar matrix, although $\Phi(\tilde Q)\ne0$.

**A pair with a real coefficient.** For $\tilde P=e_0+e_1$ and $\tilde Q=e_0-e_1$ the coefficient is
$B=1-1=0$, so the symmetrised matrix product vanishes: two nonzero matrices symmetrise to $0$. The two are the
images of conjugate directions, and their images are related by the adjugate, which is why the cross terms
cancel in the symmetrisation.

## Summary

In the $2\times2$ model the symmetric quaternionic multiplication reads
$\tfrac12(\operatorname{adj}(\Phi(\tilde P))\Phi(\tilde Q)+\operatorname{adj}(\Phi(\tilde Q))\Phi(\tilde P))=B(\tilde P,\tilde Q)I_2$,
the adjugate being the matrix of the quaternion conjugation, and the trace of the value is $2B(\tilde P,\tilde Q)$;
the resulting endomorphism of $M_2(\mathbb{C})$ has image the scalar matrices, rank $1$ and trace
$\tilde P_0$. In the $4\times4$ regular model the same identity reads
$\tfrac12(\rho_L(\tilde P)^{\mathsf T}\rho_L(\tilde Q)+\rho_L(\tilde Q)^{\mathsf T}\rho_L(\tilde P))=B(\tilde P,\tilde Q)I_4$,
the transpose being the matrix of the conjugation, and the transport of the multiplication on the image of
$\rho_L$, $X=\rho_L(\tilde Q)\mapsto\tfrac12(\rho_L(\tilde P)^{\mathsf T}X+X^{\mathsf T}\rho_L(\tilde P))$, has
image the scalar matrices, rank $1$ and trace $\tilde P_0$. The form is half the trace in the $2\times2$ model and a quarter of the trace in the $4\times4$
model; the isotropic elements are exactly the singular matrices, the determinants of the two models being
$N(\tilde Q)$ and $N(\tilde Q)^2$; the Gram matrix in the basis is $I_4$; and the definite rows and the two
Hermitian subspaces are read through the subspace conditions of the two representation articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ | the $2\times2$ realisation, $\Phi(e_0)=I_2$, $\det\Phi(\tilde Q)=N(\tilde Q)$ |
| $\operatorname{adj}$ | the adjugate, the matrix of the quaternion conjugation in the $2\times2$ model |
| $\rho_L(\tilde P^\natural)=\rho_L(\tilde P)^{\mathsf T}$ | the conjugation as the transpose in the regular model |
| $\Phi(\tilde P\star\tilde Q)=\tfrac12(\operatorname{adj}\Phi(\tilde P)\Phi(\tilde Q)+\operatorname{adj}\Phi(\tilde Q)\Phi(\tilde P))=B(\tilde P,\tilde Q)I_2$ | the product in the $2\times2$ model |
| $\tfrac12(\rho_L(\tilde P)^{\mathsf T}\rho_L(\tilde Q)+\rho_L(\tilde Q)^{\mathsf T}\rho_L(\tilde P))=B(\tilde P,\tilde Q)I_4$ | the product in the $4\times4$ regular model |
| $\operatorname{Tr}\Phi(\tilde P\star\tilde Q)=2B(\tilde P,\tilde Q)$ | the trace of the value |
| $B=\tfrac12\operatorname{Tr}(\operatorname{adj}\Phi(\tilde P)\,\Phi(\tilde Q))=\tfrac14\operatorname{Tr}(\rho_L(\tilde P)^{\mathsf T}\rho_L(\tilde Q))$ | the form in the two models |
| $N(\tilde Q)=0\Longleftrightarrow\det\Phi(\tilde Q)=0\Longleftrightarrow\det\rho_L(\tilde Q)=0$ | the isotropic cone as the singular matrices |

## Further Reading

- *Introduction to the 2×2 Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-representation-of-biquaternions.md`), for the realisation, the trace and the determinant
- *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/biquaternion-2x2-matrix-element-representation-m2c.md`), for the adjugate and the singular elements
- *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/biquaternion-4x4-matrix-element-representation.md`), for the regular model and its determinant
- *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra* (`articles_maths/the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra.md`), for the form $B$ and its Gram matrix
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra.md`), for the operators transported by the models
- *Introduction to the Symmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-biquaternions.md`), for the operation itself
