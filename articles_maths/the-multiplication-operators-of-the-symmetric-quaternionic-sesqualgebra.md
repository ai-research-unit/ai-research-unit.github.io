# __The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra__

## Introduction

The product $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ is conjugate-linear in its second argument, so the left multiplication by a fixed element is conjugate-linear and the right multiplication is linear. The two families are

$$
L^{\star}_{\tilde A}(\tilde X)=\tilde A\star\tilde X,
\qquad
R^{\star}_{\tilde A}(\tilde X)=\tilde X\star\tilde A,
$$

and they are the operators of the block. The parity split is the first thing to record: $L^{\star}_{\tilde A}$ is $\bar{\cdot}$-semilinear, $R^{\star}_{\tilde A}$ is $\mathbb{C}$-linear, and the product of two left multiplications is therefore linear while a single left multiplication is conjugate-linear. This parity is the source of every departure of the block from the operator theory of an algebra: the composition $L^{\star}_{\tilde A}\circ L^{\star}_{\tilde B}$ cannot equal $L^{\star}_{\tilde A\star\tilde B}$ off the zero operator, because the two have different parities.

The article computes the operators in the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$. It records the matrices of the two families for the unit candidate $e_0$ and for $e_1$, their ranks, which depend on the scalar part and the norm of $\tilde A$, and their traces, $0$ for the left family and $-4\mathrm{Re}(A_0)$ for the right family. It exhibits the four-dimensional image that the left multiplication acquires when the element lies in the vector subspace, a subspace that is not one of the six. It computes the adjoint with respect to the Krein form $K$, and the $J$-self-adjointness it gives with the involution $J={}^{\natural}$. It then reads the group of linear maps preserving $K$ with its Lie algebra and the structure group of the block.

The operators of the general quaternionic sesquilinear product are *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*; the operators with the conjugate transpose and the $J$-unitary family are *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*; the form $K$ is *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*; and the product is *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*. The adjoint relation used below is the compatibility theorem of the form article.

**Conventions.** The real basis is $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$, and a real-linear operator is written as an $8\times8$ real matrix in it; the coefficient basis is $e_0,e_1,e_2,e_3$ over $\mathbb{C}$, and a $\mathbb{C}$-linear operator there is a $4\times4$ complex matrix. By the *matrix of an operator* is meant the matrix of its real-linear action in the real basis. The norm is $N(\tilde A)=\tilde A^{\natural}\tilde A=A_0^{2}+A_1^{2}+A_2^{2}+A_3^{2}$.

## The Two Families and Their Parity

**Theorem (parity).** $L^{\star}_{\tilde A}$ is $\bar{\cdot}$-semilinear, $R^{\star}_{\tilde A}$ is $\mathbb{C}$-linear, and the two are related by the conjugate-commutativity,

$$
L^{\star}_{\tilde A}(\tilde X)=\overline{R^{\star}_{\tilde A}(\tilde X)}.
$$

*Proof.* The product is $\mathbb{C}$-linear in its first argument and $\bar{\cdot}$-semilinear in its second; putting the fixed element in the first slot gives the linear right multiplication, and in the second slot the conjugate-linear left multiplication. Conjugate-commutativity reads $\tilde A\star\tilde X=\overline{\tilde X\star\tilde A}$, whose right side is $\overline{R^{\star}_{\tilde A}(\tilde X)}$, which is the displayed relation. $\square$

**Corollary (the parity of the compositions).** The composition of two left multiplications is $\mathbb{C}$-linear, the composition of two right multiplications is $\mathbb{C}$-linear, and a single left multiplication is conjugate-linear. Hence $L^{\star}_{\tilde A}\circ L^{\star}_{\tilde B}\neq L^{\star}_{\tilde A\star\tilde B}$ whenever the left side is nonzero.

*Proof.* The composition of two conjugate-linear maps is linear; a single left multiplication is conjugate-linear; a map that is both is zero. $\square$

## The Matrices in the Real Basis

**Theorem (the two operators of $e_0$).** In the real basis,

$$
L^{\star}_{e_0}=\mathrm{diag}(1,-1,-1,-1,-1,1,1,1),
\qquad
R^{\star}_{e_0}=\mathrm{diag}(1,-1,-1,-1,1,-1,-1,-1).
$$

The first is the star conjugation $\tilde X\mapsto\tilde X^{*}$ and the second the natural conjugation $\tilde X\mapsto\tilde X^{\natural}$.

*Proof.* $L^{\star}_{e_0}(\tilde X)=e_0\star\tilde X=\tilde X^{*}=\tilde X^{\natural}\circ\bar{\cdot}$: the coefficient conjugation negates each imaginary coordinate and the natural conjugation negates the three vector directions, so the diagonal is $(1,-1,-1,-1)$ on the real coordinates followed by $(-1,1,1,1)$ on the imaginary ones, the display. $R^{\star}_{e_0}(\tilde X)=\tilde X\star e_0=\tilde X^{\natural}$, which on the real coordinates negates the three vector directions and leaves the imaginary coordinates' signs after the negation of the vector directions, giving the second display. $\square$

**Theorem (the two operators of $e_1$).** In the real basis,

$$
L^{\star}_{e_1}=
\begin{pmatrix}
0&-1&0&0\\ -1&0&0&0\\ 0&0&0&0\\ 0&0&0&0
\end{pmatrix}
\oplus
\begin{pmatrix}
0&1&0&0\\ 1&0&0&0\\ 0&0&0&0\\ 0&0&0&0
\end{pmatrix},
\qquad
R^{\star}_{e_1}=
\begin{pmatrix}
0&-1&0&0\\ -1&0&0&0\\ 0&0&0&0\\ 0&0&0&0
\end{pmatrix}
\oplus
\begin{pmatrix}
0&-1&0&0\\ -1&0&0&0\\ 0&0&0&0\\ 0&0&0&0
\end{pmatrix},
$$

the two blocks acting on the real coordinates $(e_0,e_1,e_2,e_3)$ and on the imaginary coordinates $(ie_0,ie_1,ie_2,ie_3)$.

*Proof.* On the real basis directions, $e_1\star e_0=-e_1$, $e_1\star e_1=-e_0$ and $e_1\star e_k=0$ for $k=2,3$; on the imaginary directions, $e_1\star ie_0=ie_1$ and $e_1\star ie_1=ie_0$, with zero for $k=2,3$, from the definition and the table. This gives the first display; the right multiplication is read from $e_0\star e_1=-e_1$, $e_1\star e_1=-e_0$, $ie_0\star e_1=-ie_1$, $ie_1\star e_1=-ie_0$, giving the second. $\square$

**Remark (the general matrix).** For a general element $\tilde A$, the two matrices are obtained from the single rule $\tilde A\star\tilde X=K(\tilde A,\tilde X)e_0-A_0\overline{\mathbf{X}}-\overline{A_0}\mathbf{X}$: the columns record the images of the basis elements, and the entries are the real and imaginary parts of the coefficients of $\tilde A$. The two special matrices above are the two cases in which the images are pure basis directions, and they show the block structure of the two families.

## Rank, Image and Trace

**Theorem (the rank of the two operators).** For an element $\tilde A$,

$$
\mathrm{rank}\,L^{\star}_{\tilde A}=\mathrm{rank}\,R^{\star}_{\tilde A}=
\begin{cases}
0,&\tilde A=0,\\
4,&A_0=0,\ \tilde A\neq0,\\
8,&A_0\neq0,\ N(\tilde A)\neq0,\\
6,&A_0\neq0,\ N(\tilde A)=0,
\end{cases}
$$

where the rank is the rank of the real-linear operator on the eight-real-dimensional space.

*Proof.* The two families have the same rank, because the two determinants agree, $\det L^{\star}_{\tilde A}=\det R^{\star}_{\tilde A}=|N(\tilde A)|^{2}|A_0|^{4}$ as real-linear operators in the real basis: a direct expansion of the two $8\times8$ matrices gives the product of the squared norm and the fourth power of the scalar part in each case, and the two determinants agree because $L^{\star}_{\tilde A}=C\circ R^{\star}_{\tilde A}$ with $C$ the coefficientwise conjugation, whose real matrix $\mathrm{diag}(1,1,1,1,-1,-1,-1,-1)$ has determinant $+1$, by the parity theorem. Hence the rank is eight exactly when $A_0\neq0$ and $N(\tilde A)\neq0$, and the remaining values are read directly: $\tilde A=0$ gives the zero map, and $A_0=0$ with $\tilde A\neq0$ gives rank four by the next corollary. In the remaining case $A_0\neq0$ the kernel is computed without the determinant. The vector part is $-A_0\overline{\mathbf{X}}-\overline{X_0}\mathbf{A}$, so it vanishes exactly when $\mathbf{X}=-(X_0/\overline{A_0})\overline{\mathbf{A}}$, which determines the vector part of a kernel element by its scalar coefficient; substituting this into the scalar part $A_0\overline{X_0}-\sum_kA_k\overline{X_k}$ leaves $\overline{X_0}\,N(\tilde A)/A_0$. The kernel is therefore zero when $N(\tilde A)\neq0$ and the complex line $\{\mathbf{X}=-(X_0/\overline{A_0})\overline{\mathbf{A}}\}$, of real dimension two, when $N(\tilde A)=0$; the rank is $8$ in the first case and $6$ in the second, and at $\tilde A=e_0+ie_2$ that line is spanned by $e_0+ie_2$ and $ie_0-e_2$. $\square$

**Corollary (the four-dimensional image).** For $\tilde A$ in the vector subspace, the image of $L^{\star}_{\tilde A}$ is a four-dimensional real subspace that is not one of the six. For $\tilde A=e_1$,

$$
L^{\star}_{e_1}(\mathbb{B})=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0,e_1,ie_1\},
$$

the sum of the complex line through $e_0$ and the complex line through $e_1$.

*Proof.* For $A_0=0$ the display reads $\tilde A\star\tilde X=K(\tilde A,\tilde X)e_0-\overline{X_0}\mathbf{A}$, so the image is the sum of the complex line $\mathbb{C}e_0$ carried by the first term and the complex line $\mathbb{C}\mathbf{A}$ carried by $\bar X_0$, and the two lines are independent because $\mathbf{A}$ lies in the vector subspace; the image has real dimension four, and for $\tilde A=e_1$ it is spanned by $e_1\star e_1=-e_0$, $e_1\star e_0=-e_1$, $e_1\star ie_1=ie_0$, $e_1\star ie_0=ie_1$, that is the displayed span. The image always contains the whole centre $\mathbb{C}e_0$, whereas each of the four four-dimensional subspaces of the six meets the centre in a single real line, $\mathbb{R}e_0$ or $\mathbb{R}ie_0$; so the image is not one of the four, and it is neither the centre nor the vector subspace, whose real dimensions are two and six. $\square$

**Theorem (the traces).** For every element $\tilde A$,

$$
\mathrm{tr}\,L^{\star}_{\tilde A}=0,
\qquad
\mathrm{tr}\,R^{\star}_{\tilde A}=-4\,\mathrm{Re}(A_0),
$$

the traces being the traces of the real-linear operators in the real basis.

*Proof.* The trace is real-linear in the real coordinates of $\tilde A$. For the left family the diagonal of the real matrix of $L^{\star}_{\tilde A}$ is $\mathrm{Re}(A_0)$ times the diagonal of $L^{\star}_{e_0}$, which is $(1,-1,-1,-1,-1,1,1,1)$ and has sum $0$, and every other real basis direction of $\tilde A$ contributes zero on the diagonal; hence $\mathrm{tr}\,L^{\star}_{\tilde A}=0$, as the two special matrices show at $\tilde A=e_0$ and at $\tilde A=e_1$. For the right family the diagonal is $\mathrm{Re}(A_0)$ times the diagonal of $R^{\star}_{e_0}$, which is $(1,-1,-1,-1,1,-1,-1,-1)$ and has sum $-4$, so $\mathrm{tr}\,R^{\star}_{\tilde A}=-4\mathrm{Re}(A_0)$, again zero contribution from every other direction, as the two special matrices show at $\tilde A=e_0$ ($-4$) and at $\tilde A=e_1$ ($0$). $\square$

**Theorem (the kernel).** The kernel of $L^{\star}_{\tilde A}$ is zero when the rank is eight, of real dimension two when $A_0\neq0$ and $N(\tilde A)=0$, of real dimension four when $A_0=0$ and $\tilde A\neq0$, and is the whole space when $\tilde A=0$.

*Proof.* This is the rank theorem, read as $8-\mathrm{rank}$. For $\tilde A=e_1$ the kernel is $\mathrm{span}_{\mathbb{R}}\{e_2,e_3,ie_2,ie_3\}$, since $e_1\star e_k=e_1\star ie_k=0$ for $k=2,3$. $\square$

## The Composition and the Defect of Multiplicativity

**Theorem (the defect).** The two families do not multiply:

$$
L^{\star}_{\tilde A}\circ L^{\star}_{\tilde B}\neq L^{\star}_{\tilde A\star\tilde B},
\qquad
R^{\star}_{\tilde A}\circ R^{\star}_{\tilde B}\neq R^{\star}_{\tilde A\star\tilde B},
$$

the defect of the left composition is the associator

$$
\tilde A\star(\tilde B\star\tilde X)-(\tilde A\star\tilde B)\star\tilde X,
$$

the defect of the right composition is the mirrored expression $(\tilde X\star\tilde B)\star\tilde A-\tilde X\star(\tilde A\star\tilde B)$, and each is nonzero on a general triple. For the left family the inequality is forced by parity, the composition being $\mathbb{C}$-linear and the single left multiplication conjugate-linear.

*Proof.* The defect of $L^{\star}$ at $\tilde X$ is the associator, and the defect of $R^{\star}$ is the same computation read with the factors in the other order. At $\tilde A=\tilde B=\tilde X=e_1$ the associator is $e_1\star(e_1\star e_1)-(e_1\star e_1)\star e_1=e_1\star(-e_0)-(-e_0)\star e_1=e_1-e_1=0$; at a generic triple both defects are nonzero, since the block is not associative. For the left family, the composition of two conjugate-linear maps is linear, while $L^{\star}_{\tilde A\star\tilde B}$ is conjugate-linear, so the two agree only if both are zero. $\square$

**Remark.** The block fails multiplicativity of the operators for two independent reasons: the associator, which is the ordinary defect of a non-associative product, and the parity, which the left family alone carries. The corresponding statement for the general quaternionic sesquilinear product is in *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*.

## The Adjoint with Respect to $K$ and $J$-Self-Adjointness

**Theorem (the adjoint).** With respect to the Krein form $K$,

$$
K\bigl(L^{\star}_{\tilde A}\tilde X,\tilde Y\bigr)
=\overline{K\bigl(\tilde X,L^{\star}_{\tilde A^{\natural}}\tilde Y\bigr)},
$$

so the adjoint of the left multiplication by $\tilde A$ is the left multiplication by $\tilde A^{\natural}$.

*Proof.* This is the compatibility theorem of *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*: $K(\tilde A\star\tilde X,\tilde Y)=\overline{K(\tilde X,\tilde A^{\natural}\star\tilde Y)}$, which is exactly the display; the conjugate on the right is the parity correction of the conjugate-linear operator. $\square$

**Corollary ($J$-self-adjointness).** The left multiplication by $\tilde A$ is self-adjoint with respect to $K$ exactly when $\tilde A^{\natural}=\tilde A$, that is on the centre $\mathbb{C}e_0$, the fixed set of the natural conjugation.

*Proof.* The adjoint is the left multiplication by $\tilde A^{\natural}$; it equals the left multiplication by $\tilde A$ exactly when the two elements are equal, since the map $\tilde A\mapsto L^{\star}_{\tilde A}$ is injective. The fixed elements of the natural conjugation, $\tilde A^{\natural}=\tilde A$, are the central ones, $A_1=A_2=A_3=0$ and $A_0$ arbitrary. $\square$

**Remark (the involution $J$).** The involution singled out by the adjoint is the natural conjugation $J={}^{\natural}$, acting on the parameter of the operator; the block is inert under the family $\tilde A\mapsto\tilde A^{\natural}$ because the natural conjugation is an automorphism of the product, so the adjoint is a permutation of the left multiplications. The operators with the conjugate transpose of the general quaternionic sesquilinear product are *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*, where the same involution appears.

## The Groups

**Theorem (the group of linear maps preserving $K$).** The set of $\mathbb{C}$-linear operators $T$ with $K(T\tilde P,T\tilde Q)=K(\tilde P,\tilde Q)$ for all $\tilde P,\tilde Q$ is a group of real dimension sixteen; in the coefficient basis its matrices $M$ satisfy

$$
M^{\dagger}EM=E,
\qquad E=\mathrm{diag}(1,-1,-1,-1),
$$

and its Lie algebra is the set of $\mathbb{C}$-linear $X$ with $X^{\dagger}E+EX=0$, of real dimension sixteen.

*Proof.* Write $K(\tilde P,\tilde Q)=P^{T}E\overline{Q}$ in the coefficient basis; then $K(T\tilde P,T\tilde Q)=P^{T}M^{T}E\overline{M}\,\overline{Q}$, which equals $K(\tilde P,\tilde Q)$ for all $P,Q$ exactly when $M^{T}E\overline{M}=E$, equivalently, after conjugation, $M^{\dagger}EM=E$. The condition is quadratic and its linearisation at the identity is $X^{\dagger}E+EX=0$; the matrices of the group are counted by $32$ real parameters subject to the $16$ real equations of $M^{\dagger}EM=E$, since $M^{\dagger}EM$ is Hermitian, so the group has real dimension $16$. $\square$

**Remark.** The group is the one of the general quaternionic sesquilinear row, because $K$ is that form with the arguments read in the other order; the details and the corresponding $J$-unitary family are in *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*. The Lie algebra of the theorem is the linearisation recorded there.

**Theorem (the structure group of the block).** The natural conjugation ${}^{\natural}$ is a $\mathbb{C}$-linear automorphism of the product, the coefficientwise conjugation $\bar{\cdot}$ is a conjugate-linear automorphism, and the star conjugation ${}^{*}$ is their composite, also a conjugate-linear automorphism. The two involutions ${}^{\natural}$ and $\bar{\cdot}$ generate a group of order four,

$$
\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\},
$$

acting on the block.

*Proof.* The three maps satisfy $\varphi(\tilde P\star\tilde Q)=\varphi(\tilde P)\star\varphi(\tilde Q)$ for all $\tilde P,\tilde Q$, by the definition of the product and the two anti-automorphism properties of the conjugations; each is an involution and ${}^{*}={}^{\natural}\circ\bar{\cdot}$, so they generate the Klein group of the display. $\square$

**Remark (what is not decided).** The theorem exhibits four automorphisms; whether they exhaust the automorphism group of the block is not decided here. The group preserving $K$ is larger, of dimension sixteen, and the two groups are not the same: the automorphisms of the product are a finite group, while the maps preserving the form include the whole sixteen-dimensional family of the theorem above.

## Worked Examples

**The two operators at a general element.** $\tilde X=e_0+e_1$: $L^{\star}_{e_0}\tilde X=\tilde X^{*}=e_0-e_1$ and $R^{\star}_{e_0}\tilde X=\tilde X^{\natural}=e_0-e_1$, the two operators agreeing on a real element; $L^{\star}_{e_1}\tilde X=e_1\star(e_0+e_1)=-e_1-e_0$.

**A four-dimensional image.** For $\tilde A=e_1$ the image is $\mathrm{span}_{\mathbb{R}}\{e_0,ie_0,e_1,ie_1\}$: it contains the complex line $\mathbb{C}e_0$ and the complex line $\mathbb{C}e_1$ and nothing else, and it is not among the six.

**A trace.** $\mathrm{tr}\,R^{\star}_{e_0}=-4\mathrm{Re}(1)=-4$, as the diagonal matrix of the theorem shows.

**A kernel.** For $\tilde A=e_1$ the kernel is $\mathrm{span}_{\mathbb{R}}\{e_2,e_3,ie_2,ie_3\}$, of real dimension four, since $e_1\star e_2=e_1\star e_3=0$.

**A self-adjoint element.** $\tilde A=ie_0\in\mathbb{C}e_0$: $\tilde A^{\natural}=ie_0=\tilde A$, so the left multiplication is self-adjoint with respect to $K$. An element of $\mathbb{M}_{+}$, for instance $e_0+ie_1$, is not self-adjoint, since $(e_0+ie_1)^{\natural}=e_0-ie_1\neq e_0+ie_1$.

**An automorphism.** ${}^{\natural}(e_1\star e_2)={}^{\natural}(0)=0$ and $e_1^{\natural}\star e_2^{\natural}=(-e_1)\star(-e_2)=e_1\star e_2=0$; the natural conjugation respects the product.

## Summary

The operators of the block are $L^{\star}_{\tilde A}(\tilde X)=\tilde A\star\tilde X$, conjugate-linear, and $R^{\star}_{\tilde A}(\tilde X)=\tilde X\star\tilde A$, linear, related by $L^{\star}_{\tilde A}(\tilde X)=\overline{R^{\star}_{\tilde A}(\tilde X)}$. In the real basis $L^{\star}_{e_0}$ is the star conjugation and $R^{\star}_{e_0}$ the natural conjugation, and the operators of $e_1$ have the exhibited block matrices. The ranks of the two families, equal, are $0$ at $\tilde A=0$, $4$ for $\tilde A$ in the vector subspace, $8$ for $A_0\neq0$ with $N(\tilde A)\neq0$ and $6$ for $A_0\neq0$ with $N(\tilde A)=0$; the four-dimensional image at $\tilde A=e_1$ is $\mathrm{span}_{\mathbb{R}}\{e_0,ie_0,e_1,ie_1\}$, not one of the six. The traces are $0$ for the left family and $-4\mathrm{Re}(A_0)$ for the right; the kernels are read from the ranks. The operators do not multiply: the left defect is the associator and the right defect its mirror, the left case being forced by parity. The adjoint with respect to $K$ is $K(L^{\star}_{\tilde A}\tilde X,\tilde Y)=\overline{K(\tilde X,L^{\star}_{\tilde A^{\natural}}\tilde Y)}$, which gives the $J$-self-adjointness with $J={}^{\natural}$ on the centre $\mathbb{C}e_0$. The group of $\mathbb{C}$-linear maps preserving $K$ has real dimension sixteen and its matrices satisfy $M^{\dagger}EM=E$; the structure group of the block contains the four automorphisms $\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L^{\star}_{\tilde A}(\tilde X)=\tilde A\star\tilde X$ | the left multiplication, conjugate-linear |
| $R^{\star}_{\tilde A}(\tilde X)=\tilde X\star\tilde A$ | the right multiplication, linear |
| $L^{\star}_{e_0}=\tilde X^{*}$, $R^{\star}_{e_0}=\tilde X^{\natural}$ | the two conjugations as operators |
| $\mathrm{rank}\,L^{\star}_{\tilde A}=\mathrm{rank}\,R^{\star}_{\tilde A}\in\{0,4,6,8\}$ | the rank of the two families |
| $\mathrm{span}_{\mathbb{R}}\{e_0,ie_0,e_1,ie_1\}$ | the four-dimensional image at $\tilde A=e_1$ |
| $\mathrm{tr}\,L^{\star}_{\tilde A}=0$, $\mathrm{tr}\,R^{\star}_{\tilde A}=-4\mathrm{Re}(A_0)$ | the traces |
| $K(L^{\star}_{\tilde A}\tilde X,\tilde Y)=\overline{K(\tilde X,L^{\star}_{\tilde A^{\natural}}\tilde Y)}$ | the adjoint with respect to $K$; $J={}^{\natural}$ |
| $M^{\dagger}EM=E$ | the condition of the group of linear maps preserving $K$ |
| $\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$ | the automorphisms of the block exhibited |

## Further Reading

- *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product* (`articles_maths/the-left-and-right-multiplications-of-the-quaternionic-sesquilinear-product.md`), for the operators of the unsplit product.
- *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/j-self-adjoint-and-j-unitary-operators-on-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the operators with the conjugate transpose and the group preserving the form.
- *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-krein-form-as-a-product-on-the-symmetric-quaternionic-sesqualgebra.md`), for the form $K$ and the adjoint relation in the form setting.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the product and its parity.
- *The Six Subspaces under the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the six subspaces and the vector subspace carrying the four-dimensional image.
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm $N$ entering the rank table.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the comparison of the operators of the twelve operations.
