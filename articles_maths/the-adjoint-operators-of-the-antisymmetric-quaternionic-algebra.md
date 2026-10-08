# __The Adjoint Operators of the Antisymmetric Quaternionic Algebra__

## Introduction

The antisymmetric quaternionic multiplication $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ is an alternating operation with no unit and no nontrivial annihilator, it fails the Jacobi identity, and it is one of the first instances in which the invariant-form theory is degenerate (*Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*, *The Invariant Bilinear Forms of the Antisymmetric Quaternionic Algebra*). The operators of the operation are therefore the natural object left: the left multiplications $L_{\tilde A}\tilde R=\tilde A\diamond\tilde R$, their matrices, ranks and kernels, their compositions and their deviations, the derivations of the operation, and the groups of linear maps that preserve it. This article computes all of these. The operators of the parent product are *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, and the two-sided operators of the parent are *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions*; the two-sided family of the block is its left family and the negated right family, since the operation is alternating, so the left multiplication is the whole story.

The block's operators are a deformation of the cross-product operators of the plain row, and the deformation is visible in every invariant. The trace is $3A_0$ instead of $0$, where $A_0$ is the scalar part of the element; the rank is three instead of two; the commutator of two operators deviates from the operator of the value by a term that is the operator form of the Jacobi failure; the operation has **no nonzero inner derivation**, so all of its derivations are outer; and its derivations are the three-dimensional algebra of skew maps of the vector subspace, the same algebra that in the Lie case $\mathrm{APA}$ appears as the inner derivations. The automorphism group of the bracket is the group of linear maps that preserve the cross product of the vector subspace and fix the element $e_0$, of complex dimension three.

## The Left Multiplication Operator

**Definition.** The **left multiplication operator** of $\tilde A$ is

$$
L_{\tilde A}:\mathbb{B}\to\mathbb{B}, \qquad L_{\tilde A}\tilde R = \tilde A\diamond\tilde R = A_0\mathbf R - R_0\mathbf A - \mathbf A\times\mathbf R .
$$

The map $\tilde A\mapsto L_{\tilde A}$ is $\mathbb{C}$-linear and injective: the operators of the four basis elements $e_0,e_1,e_2,e_3$ are linearly independent, so they span a four-dimensional space of linear maps and $\tilde A$ is recovered from its operator.

*Proof.* Linearity is the $\mathbb{C}$-bilinearity of the operation in its first argument. If $L_{\tilde A}=0$ then $L_{\tilde A}e_0=-\mathbf A=0$, so $\tilde A=A_0e_0$, and then $L_{\tilde A}e_1=A_0e_1$, so $A_0=0$; hence $\tilde A=0$. The four operators are linearly independent by the same argument applied to a linear combination. $\square$

**Proposition (the matrix in the coefficient basis).** In the basis $e_0,e_1,e_2,e_3$, with the columns the images of the basis elements,

$$
M_{\tilde A} = L_{\tilde A} =
\begin{pmatrix}
0 & 0 & 0 & 0 \\
-A_1 & A_0 & A_3 & -A_2 \\
-A_2 & -A_3 & A_0 & A_1 \\
-A_3 & A_2 & -A_1 & A_0
\end{pmatrix}.
$$

In the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$, and writing $\tilde A=a+ia'$ with $a,a'$ real, the matrix is the realification of the complex one,

$$
\begin{pmatrix} M_a & -M_{a'} \\ M_{a'} & M_a \end{pmatrix},
$$

the standard block form of a $\mathbb{C}$-linear map of a complex space read over the reals.

*Proof.* The entries are read off the table of the block: the first column is $L_{\tilde A}e_0=-\mathbf A$, the diagonal is $A_0$ on the three vector lines and $0$ on the scalar line, and the off-diagonal entries of the vector block are the components of $-\mathbf A\times$. The realification is the definition of a $\mathbb{C}$-linear map in a real basis adapted to a complex structure. $\square$

**Proposition (the structure of the matrix).** The operator splits as

$$
M_{\tilde A} = A_0\,P + \Lambda_{\tilde A} , \qquad P=\operatorname{diag}(0,1,1,1) ,
$$

where $P$ is the projection onto the vector part and the vector block of $\Lambda_{\tilde A}$ is the skew matrix of the map $\mathbf R\mapsto-\mathbf A\times\mathbf R$, whose characteristic polynomial is $\mu(\mu^2+(\mathbf A,\mathbf A))$. The scalar part of the element therefore scales the vector lines, and the vector part of the element contributes the skew block and the first column $-\mathbf A$.

*Proof.* The matrix has the first row zero and its vector block equal to the sum of $A_0I_3$ and the skew matrix of $\mathbf R\mapsto-\mathbf A\times\mathbf R$; the first column is $0,-\mathbf A$, so $\Lambda_{\tilde A}e_0=-\mathbf A$ and $\Lambda_{\tilde A}$ acts on the vector lines by that skew matrix. The characteristic polynomial of a skew $3\times3$ matrix is $\mu(\mu^2+(\mathbf A,\mathbf A))$, which is the standard computation for the matrix of a cross product, the sign of $\mathbf A$ not entering. $\square$

## The Trace, the Rank and the Characteristic Polynomial

**Proposition (the trace).** The trace of the operator is

$$
\operatorname{Tr}L_{\tilde A} = 3A_0 ,
$$

the sum of the three diagonal entries $A_0$ on the vector lines. The trace vanishes exactly on the vector subspace, and it vanishes identically on the quotient by the image, since the operator maps into $\mathrm{Vect}(\mathbb{B})$ and the induced operator on the one-dimensional quotient $\mathbb{B}/\mathrm{Vect}(\mathbb{B})$ is zero.

*Proof.* The diagonal is $0,A_0,A_0,A_0$ from the matrix, and the sum is $3A_0$. The scalar-part functional is the quotient map, and the operator lowers the scalar part to zero, so the induced map on the quotient is zero and has trace zero. $\square$

**Proposition (the characteristic polynomial and the rank).** The characteristic polynomial is

$$
\chi_{L_{\tilde A}}(\lambda) = \lambda\,(\lambda-A_0)\bigl(\lambda^2-2A_0\lambda+N(\tilde A)\bigr),
\qquad N(\tilde A)=A_0^2+A_1^2+A_2^2+A_3^2 ,
$$

with $N$ the norm of the algebra; the eigenvalues are $0$, $A_0$ and the two roots of the quadratic; the determinant is zero; and the rank is

$$
\operatorname{rank}L_{\tilde A} = 3 \iff N(\tilde A)\neq 0, \qquad
\operatorname{rank}L_{\tilde A} = 2 \iff N(\tilde A)=0,\ \tilde A\neq 0, \qquad
\operatorname{rank}L_{\tilde A} = 0 \iff \tilde A=0 ,
$$

so the rank is decided by the norm alone and drops exactly on the isotropic cone of the norm.

*Proof.* The second row of the matrix has no entry in the scalar column, so the characteristic polynomial has a factor $\lambda$; the remaining three-dimensional block is $A_0I_3-[\mathbf A]_\times$, whose characteristic polynomial is $(A_0-\lambda)\bigl((A_0-\lambda)^2+\lvert\mathbf A\rvert^2\bigr)$ by the identity $\det(\mu I_3+[\mathbf u]_\times)=\mu(\mu^2+(\mathbf u,\mathbf u))$ for a skew matrix, and the product with the factor $\lambda$ is the displayed expression after expanding. The determinant is the constant term, zero. The rank is read on the image, which is spanned by the first column $-\mathbf A$ and by the image of that three-dimensional block. If $A_0\neq0$ the block has determinant $A_0N(\tilde A)$, so it is invertible and the rank is three when $N(\tilde A)\neq0$, and of rank two with $-\mathbf A$ lying in its image when $N(\tilde A)=0$. If $A_0=0$ the block is $-[\mathbf A]_\times$, of rank two for $\mathbf A\neq0$ with image $\{\mathbf A\}^{\perp}$, and the first column $-\mathbf A$ adds one dimension exactly when $\mathbf A\notin\{\mathbf A\}^{\perp}$, that is when $N(\tilde A)\neq0$. In both cases the rank is three when $N(\tilde A)\neq0$ and two when $N(\tilde A)=0$ with $\tilde A\neq0$. The eigenvalues do not decide it: at a pure non-isotropic element the root $0$ has multiplicity two in the characteristic polynomial but the kernel is only the line of the element, the operator being defective there. $\square$

The rank therefore drops exactly on the isotropic cone of the norm, where $N(\tilde A)=0$; it does not drop on the vector subspace, the operator of a pure non-isotropic vector having rank three. The isotropic cone is the classical degeneracy of the biquaternion algebra, and the operator of the block detects it.

## The Kernel and the Image

**Proposition.** The kernel of $L_{\tilde A}$ always contains $\tilde A$, since $\tilde A\diamond\tilde A=0$; the image is always contained in the vector subspace, since the values of the operation are pure vectors. Off the isotropic cone, with $N(\tilde A)\neq0$,

$$
\ker L_{\tilde A} = \mathbb{C}\tilde A , \qquad \operatorname{Im}L_{\tilde A} = \mathrm{Vect}(\mathbb{B}) ,
$$

of complex dimensions one and three; on the isotropic cone, for $N(\tilde A)=0$ and $\tilde A\neq0$, the kernel and the image are both of dimension two.

*Proof.* The kernel contains $\tilde A$ by alternation and the image lies in the vector subspace because the values have zero scalar part. The rank is three off the isotropic cone, so the kernel is one-dimensional and, containing $\tilde A$, is exactly $\mathbb{C}\tilde A$; the image is a three-dimensional subspace of the three-dimensional vector subspace, hence the whole of it. A pure vector with $N(\mathbf A)\neq0$ is off the cone, so its kernel is the line $\mathbb{C}\mathbf A$ and its image is the whole vector subspace: the operator is $L_{\mathbf A}\tilde R=-R_0\mathbf A-\mathbf A\times\mathbf R$, whose image is spanned by $\mathbf A$ and the plane $\mathbf A\times\mathbb{R}^3=\{\mathbf A\}^{\perp}$, and the line $\mathbb{C}\mathbf A$ enlarges that plane to the whole space. On the isotropic cone the rank is two and both spaces are two-dimensional, by the rank formula. $\square$

**Remark.** The line $\mathbb{C}\tilde A$ is always in the kernel, so the operator of an element is never injective and the block has no regular element in the naive sense; the content of the rank formula is the size of the kernel above that line. The element is **regular** exactly when $N(\tilde A)\neq0$, and there the kernel is the line alone.

## The Composition and the Deviation from the Value

**Proposition (the composition).** For all $\tilde A,\tilde B,\tilde R$,

$$
L_{\tilde A}L_{\tilde B}\tilde R
= A_0B_0\mathbf R - A_0R_0\mathbf B - A_0\,\mathbf B\times\mathbf R - B_0\,\mathbf A\times\mathbf R
+ R_0\,\mathbf A\times\mathbf B + (\mathbf A,\mathbf R)\mathbf B - (\mathbf A,\mathbf B)\mathbf R .
$$

*Proof.* Expand $L_{\tilde A}(L_{\tilde B}\tilde R)=\tilde A\diamond(\tilde B\diamond\tilde R)$ with the explicit form and use the double cross identity $\mathbf A\times(\mathbf B\times\mathbf R)=\mathbf B(\mathbf A,\mathbf R)-\mathbf R(\mathbf A,\mathbf B)$. $\square$

**Proposition (the operator form of the Jacobi failure).** For all $\tilde A,\tilde B$,

$$
[L_{\tilde A},L_{\tilde B}] - L_{\tilde A\diamond\tilde B} = D(\tilde A,\tilde B), \qquad
D(\tilde A,\tilde B)\tilde R = A_0\,(\mathbf B\times\mathbf R) - B_0\,(\mathbf A\times\mathbf R) + R_0\,(\mathbf A\times\mathbf B) .
$$

The deviation $D(\tilde A,\tilde B)$ is zero for all pairs exactly when the operation satisfies the Jacobi identity, so it is the operator form of the failure of the block; it is the negative of the cyclic sum, $D(\tilde A,\tilde B)\tilde R=-J(\tilde A,\tilde B,\tilde R)$, and its trace is zero for every pair.

*Proof.* The deviation is $[L_{\tilde A},L_{\tilde B}]\tilde R-L_{\tilde A\diamond\tilde B}\tilde R = \tilde A\diamond(\tilde B\diamond\tilde R)-\tilde B\diamond(\tilde A\diamond\tilde R)-(\tilde A\diamond\tilde B)\diamond\tilde R$; comparing with the definition of the cyclic sum, the right side is $-J(\tilde A,\tilde B,\tilde R)$, and the closed form is the one computed in *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra* with the sign reversed. The vanishing of $D$ for all pairs is the vanishing of $J$, which is the Jacobi identity. The trace is zero because the first row of $D$ is zero in the coefficient basis and the diagonal of the vector block is zero. $\square$

**Corollary.** The operators of the block are not a representation of the block: $[L_{\tilde A},L_{\tilde B}]\neq L_{\tilde A\diamond\tilde B}$ in general, at $(e_0,e_1)$ for instance, where the deviation is $D(e_0,e_1)\tilde R=e_1\times\tilde R$ with $\mathbf R$ arbitrary, nonzero. The commutator of two operators is the operator of the value plus the deviation, and the deviation is exactly the obstruction.

**Remark (the algebra generated by the operators).** The four operators and their pairwise products span an associative algebra of linear maps of dimension $12$ inside the $16$-dimensional algebra of all linear maps, of dimension $13$ once the identity is adjoined, and not all of the ambient algebra; the operators span four dimensions, their pairwise products already span the algebra, and no further products are independent. The quotient by the four-dimensional span is the operator echo of the associativity defect.

## The Derivations and the Inner Ones

**Definition.** A linear map $\delta:\mathbb{B}\to\mathbb{B}$ is a **derivation** of the block if $\delta(\tilde P\diamond\tilde Q)=\delta\tilde P\diamond\tilde Q+\tilde P\diamond\delta\tilde Q$ for all $\tilde P,\tilde Q$. A derivation is **inner** if it is $\operatorname{ad}_{\tilde A}=[\tilde A,\cdot\,]$ for some $\tilde A$.

**Proposition (the derivations).** The derivations of the block are the maps that annihilate the scalar line and act on the vector subspace by a skew matrix,

$$
\operatorname{Der}(\diamond) = \left\{ \delta : \delta(e_0)=0,\ \delta|_{\mathbb{C}^3}\ \text{a skew } \mathbb{C}\text{-linear map} \right\},
$$

of complex dimension three, and they are all **outer**: there is no nonzero inner derivation.

*Proof.* Let $D$ be the matrix of a general linear map and impose the derivation condition on the sixteen basis pairs. The system forces the first row and the first column to vanish, so $\delta(e_0)=0$, and leaves the vector block a general skew $3\times3$ matrix; its dimension is $3$. For the inner derivations, $\operatorname{ad}_{\tilde A}=2L_{\tilde A}$ by the alternation of the operation, and $L_{\tilde A}e_0=-\mathbf A$, which is zero for every derivation; so $\mathbf A=0$, and then $L_{\tilde A}(e_1)=A_0e_1$ must be zero, so $A_0=0$ as well. Hence the only inner derivation is zero. $\square$

**Remark.** The derivations of the block are exactly the skew maps of the vector subspace, and their dimension three is the dimension of the group of linear maps of the vector subspace that the automorphism group below realises. The block therefore has a three-dimensional derivation algebra, all of it outer, whereas the adjacent Lie case $\mathrm{APA}$ has a three-dimensional derivation algebra all of it inner: for $\mathrm{APA}$ the adjoint map is a representation and its image is the whole derivation algebra, and for the block the adjoint map is not a representation and contributes nothing.

## The Automorphism Group and the Structure Group

**Proposition (the automorphism group).** A linear isomorphism $T$ satisfies $T(\tilde P\diamond\tilde Q)=T\tilde P\diamond T\tilde Q$ for all $\tilde P,\tilde Q$ if and only if

$$
T(e_0)=e_0 , \qquad T|_{\mathbb{C}^3}\ \text{preserves the cross product of the vector subspace} ;
$$

so the automorphism group of the bracket is the group of linear maps that fix the element $e_0$ and preserve the cross product of the vector subspace, of complex dimension three, and its Lie algebra is the derivation algebra of skew maps computed above.

*Proof.* Every value of the operation is a pure vector and every pure vector is a value, so the image of the operation is the vector subspace and $T$ carries the vector subspace into itself; being invertible, it carries it onto itself. From $e_0\diamond\tilde U=\mathbf U$ and the automorphism property, $T\tilde U = T(e_0)\diamond T\tilde U$ for every pure vector $\tilde U$; as $T\tilde U$ ranges over the vector subspace, $X\diamond\mathbf W=\mathbf W$ for all pure $\mathbf W$ with $X=T(e_0)$, which forces $X=e_0$. On the vector subspace the property reads $T(\mathbf U\times\mathbf V)=T\mathbf U\times T\mathbf V$, so $T|_{\mathbb{C}^3}$ preserves the cross product; the maps that do so are exactly the maps that preserve the bilinear form of the vector part and have determinant one, and they form a group of complex dimension three. $\square$

**Proposition (the structure group).** A linear isomorphism $T$ with $T(\tilde P\diamond\tilde Q)=\lambda\,(T\tilde P\diamond T\tilde Q)$ for a fixed $\lambda\in\mathbb{C}^{*}$ acts as

$$
T|_{\mathbb{C}^3} = cR , \qquad T(e_0) = c\det(R)\,e_0 , \qquad \lambda = \frac{1}{c\det R} ,
$$

with $c\in\mathbb{C}^{*}$ and $R$ a linear map preserving the cross product of the vector subspace; the structure group is of complex dimension four, and its subgroup with $c=1$ is the automorphism group.

*Proof.* The image argument again makes $T$ preserve the vector subspace, and the scalar line is preserved as well; the condition on the vector subspace is $M\mathbf U\times M\mathbf V=\lambda^{-1}M(\mathbf U\times\mathbf V)$, whose solutions are the matrices $M=cR$ with $c\in\mathbb{C}^{*}$ and $R$ preserving the cross product, and the comparison on the scalar line fixes $T(e_0)$ and $\lambda$ as displayed. $\square$

The automorphism group of the bracket is therefore a subgroup of the structure group, obtained by fixing $c=1$; the extra dimension is the scalar freedom that changes the value of the operation by the factor $\lambda$ and is not an automorphism unless $\lambda=1$.

## The Comparison with the Lie Case

**Remark.** The adjacent block $\mathrm{APA}$ is the cross product on the vector subspace, $\tilde P\wedge\tilde Q=\mathbf P\times\mathbf Q$; its adjoint operator is $\operatorname{ad}_{\tilde P}=\mathbf P\times$, which annihilates the centre, has trace zero, has rank two, and has for kernel the centre and the line of $\mathbf P$ (*The Lie Algebra of the Antisymmetric Plain Algebra*, *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*). The operators of the block of this article differ in every one of these invariants. The trace is $3A_0$ instead of zero, and it vanishes exactly on the vector subspace. The rank is three instead of two, and it drops on the isotropic cone. The kernel is the line of the element instead of a two-dimensional subspace of the centre and the element. The commutator of two operators is the operator of the value plus the deviation $D$, the operator form of the failure of the Jacobi identity, instead of being exactly the operator of the value. And the derivation algebra is three-dimensional but all outer, where for $\mathrm{APA}$ it is three-dimensional and all inner. In the Lie case the adjoint map is a representation whose image is the derivation algebra; in the block the adjoint map is not a representation, its image contributes no derivation, and the derivations are realised only by the skew maps of the vector subspace.

## Summary

The left multiplication operator of the block is $L_{\tilde A}\tilde R=A_0\mathbf R-R_0\mathbf A-\mathbf A\times\mathbf R$; the map $\tilde A\mapsto L_{\tilde A}$ is injective with four-dimensional image, and the matrix in the coefficient basis is displayed, with the real basis carrying its realification. The trace is $3A_0$, vanishing exactly on the vector subspace and on the quotient by the image; the characteristic polynomial is $\lambda(\lambda-A_0)(\lambda^2-2A_0\lambda+N(\tilde A))$, the determinant is zero, and the rank is three exactly when $N(\tilde A)\neq0$, two on the isotropic cone away from the origin, and zero only at $\tilde A=0$. The kernel always contains the line of the element, the image always lies in the vector subspace, and for a regular element the kernel is the line and the image the whole vector subspace. The commutator of two operators deviates from the operator of the value by $D(\tilde A,\tilde B)\tilde R=A_0(\mathbf B\times\mathbf R)-B_0(\mathbf A\times\mathbf R)+R_0(\mathbf A\times\mathbf B)$, which is the negative of the cyclic sum and the operator form of the Jacobi failure; the operators and their pairwise products span an associative algebra of dimension $12$, of dimension $13$ with the identity. The derivations of the block are the maps that annihilate the scalar line and act on the vector subspace by skew matrices, they form a three-dimensional space, and none is inner. The automorphism group of the bracket is the group of linear maps that fix the element $e_0$ and preserve the cross product of the vector subspace, of complex dimension three; the structure group is its four-dimensional conformal enlargement, with the multiplier $\lambda=1/(c\det R)$. Each invariant is compared with the Lie case $\mathrm{APA}$, where the trace vanishes, the rank is two, the derivation algebra is all inner and the adjoint map is a representation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $L_{\tilde A}\tilde R=\tilde A\diamond\tilde R$ | the left multiplication operator of the block |
| $M_{\tilde A}$ | the matrix of $L_{\tilde A}$ in the coefficient basis, and its realification in the real basis |
| $\operatorname{Tr}L_{\tilde A}=3A_0$ | the trace, vanishing exactly on the vector subspace |
| $N(\tilde A)=A_0^2+\sum_kA_k^2$ | the norm; the rank drops on its vanishing |
| $\chi_{L_{\tilde A}}(\lambda)=\lambda(\lambda-A_0)(\lambda^2-2A_0\lambda+N(\tilde A))$ | the characteristic polynomial |
| $\ker L_{\tilde A}=\mathbb{C}\tilde A$ | the kernel for a regular element $N\neq0$ |
| $\operatorname{Im}L_{\tilde A}=\mathrm{Vect}(\mathbb{B})$ | the image for a regular element |
| $D(\tilde A,\tilde B)=[L_{\tilde A},L_{\tilde B}]-L_{\tilde A\diamond\tilde B}$ | the deviation, the operator form of the Jacobi failure |
| $\operatorname{Der}(\diamond)=$ the skew maps of the vector subspace | the derivation algebra, three-dimensional, all outer |
| $\operatorname{Aut}(\diamond)=$ the maps fixing $e_0$ and preserving the cross product | the automorphism group of the bracket, of complex dimension three |

## Further Reading

- *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the operation, its table and its image
- *The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-jacobi-failure-and-the-associator-defect-of-the-antisymmetric-quaternionic-algebra.md`), for the cyclic sum that the deviation reverses, and for the trivial alternating centre
- *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* (`articles_maths/the-left-multiplications-of-the-quaternionic-product-and-the-opposite-monoid.md`), for the operators of the parent product
- *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-quaternionic-algebra-of-biquaternions.md`), for the two-sided family of the parent product
- *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra* (`articles_maths/the-adjoint-operators-and-the-derivations-of-the-antisymmetric-plain-algebra.md`), for the Lie case, whose adjoint map is a representation and whose derivations are inner
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm and its isotropic cone, on which the rank of the operator drops
