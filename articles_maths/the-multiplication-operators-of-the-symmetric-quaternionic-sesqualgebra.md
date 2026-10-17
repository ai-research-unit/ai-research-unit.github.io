# __The Multiplication Operators of the Symmetric Quaternionic Sesqualgebra__

## Introduction

The product $\tilde P\star\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ is conjugate-linear in its second argument, so the left multiplication by a fixed element is conjugate-linear and the right multiplication is linear. The two families are

$$
L^{\star}_{\tilde A}(\tilde Q_1)=\tilde A\star\tilde Q_1,
\qquad
R^{\star}_{\tilde A}(\tilde Q_1)=\tilde Q_1\star\tilde A,
$$

and they are the operators of the block. The parity split is the first thing to record: $L^{\star}_{\tilde A}$ is $\bar{\cdot}$-semilinear, $R^{\star}_{\tilde A}$ is $\mathbb{C}$-linear, and the product of two left multiplications is therefore linear while a single left multiplication is conjugate-linear. This parity is the source of every departure of the block from the operator theory of an algebra: the composition $L^{\star}_{\tilde A}\circ L^{\star}_{\tilde Q_2}$ cannot equal $L^{\star}_{\tilde A\star\tilde Q_2}$ off the zero operator, because the two have different parities.

The article computes the operators in the real basis $e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z$. It records the matrices of the two families for the unit candidate $e_t$ and for $\vec e_x$, their ranks, which depend on the scalar part and the norm of $\tilde A$, and their traces, $0$ for the left family and $-4\mathrm{Re}(A_t)$ for the right family. It exhibits the four-dimensional image that the left multiplication acquires when the element lies in the vector subspace, a subspace that is not one of the remarkable subspaces. It computes the adjoint with respect to the Krein form $\langle\cdot,\cdot\rangle_{\natural*}$, and the $J$-self-adjointness it gives with the involution $J={}^{\natural}$. It then reads the group of linear maps preserving $\langle\cdot,\cdot\rangle_{\natural*}$ with its Lie algebra and the structure group of the block.

The operators of the general quaternionic sesquilinear product are *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*; the operators with the conjugate transpose and the $J$-unitary family are *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra*; the form $\langle\cdot,\cdot\rangle_{\natural*}$ is *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*; and the product is *Introduction to the Symmetric Quaternionic Sesqualgebra*. The adjoint relation used below is the compatibility theorem of the form article.

**Conventions.** The real basis is $e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z$, and a real-linear operator is written as an $8\times8$ real matrix in it; the coefficient basis is $e_t,\vec e_x,\vec e_y,\vec e_z$ over $\mathbb{C}$, and a $\mathbb{C}$-linear operator there is a $4\times4$ complex matrix. By the *matrix of an operator* is meant the matrix of its real-linear action in the real basis. The norm is $\langle\tilde A\rangle_{\natural}=\tilde A^{\natural}\tilde A=A_t^{2}+A_x^{2}+A_y^{2}+A_z^{2}$.

## The Two Families and Their Parity

**Theorem (parity).** $L^{\star}_{\tilde A}$ is $\bar{\cdot}$-semilinear, $R^{\star}_{\tilde A}$ is $\mathbb{C}$-linear, and the two are related by the conjugate-commutativity,

$$
L^{\star}_{\tilde A}(\tilde Q_1)=\overline{R^{\star}_{\tilde A}(\tilde Q_1)}.
$$

*Proof.* The product is $\mathbb{C}$-linear in its first argument and $\bar{\cdot}$-semilinear in its second; putting the fixed element in the first slot gives the linear right multiplication, and in the second slot the conjugate-linear left multiplication. Conjugate-commutativity reads $\tilde A\star\tilde Q_1=\overline{\tilde Q_1\star\tilde A}$, whose right side is $\overline{R^{\star}_{\tilde A}(\tilde Q_1)}$, which is the displayed relation.

**Corollary (the parity of the compositions).** The composition of two left multiplications is $\mathbb{C}$-linear, the composition of two right multiplications is $\mathbb{C}$-linear, and a single left multiplication is conjugate-linear. Hence $L^{\star}_{\tilde A}\circ L^{\star}_{\tilde Q_2}\neq L^{\star}_{\tilde A\star\tilde Q_2}$ whenever the left side is nonzero.

*Proof.* The composition of two conjugate-linear maps is linear; a single left multiplication is conjugate-linear; a map that is both is zero.

## The Matrices in the Real Basis

**Theorem (the two operators of $e_t$).** In the real basis,

$$
L^{\star}_{e_t}=\mathrm{diag}(1,-1,-1,-1,-1,1,1,1),
\qquad
R^{\star}_{e_t}=\mathrm{diag}(1,-1,-1,-1,1,-1,-1,-1).
$$

The first is the star conjugation $\tilde Q_1\mapsto\tilde Q_1^{*}$ and the second the natural conjugation $\tilde Q_1\mapsto\tilde Q_1^{\natural}$.

*Proof.* $L^{\star}_{e_t}(\tilde Q_1)=e_t\star\tilde Q_1=\tilde Q_1^{*}=\tilde Q_1^{\natural}\circ\bar{\cdot}$: the coefficient conjugation negates each imaginary coordinate and the natural conjugation negates the three vector directions, so the diagonal is $(1,-1,-1,-1)$ on the real coordinates followed by $(-1,1,1,1)$ on the imaginary ones, the display. $R^{\star}_{e_t}(\tilde Q_1)=\tilde Q_1\star e_t=\tilde Q_1^{\natural}$, which on the real coordinates negates the three vector directions and leaves the imaginary coordinates' signs after the negation of the vector directions, giving the second display.

**Theorem (the two operators of $\vec e_x$).** In the real basis,

$$
L^{\star}_{\vec e_x}=
\begin{pmatrix}
0&-1&0&0\\ -1&0&0&0\\ 0&0&0&0\\ 0&0&0&0
\end{pmatrix}
\oplus
\begin{pmatrix}
0&1&0&0\\ 1&0&0&0\\ 0&0&0&0\\ 0&0&0&0
\end{pmatrix},
\qquad
R^{\star}_{\vec e_x}=
\begin{pmatrix}
0&-1&0&0\\ -1&0&0&0\\ 0&0&0&0\\ 0&0&0&0
\end{pmatrix}
\oplus
\begin{pmatrix}
0&-1&0&0\\ -1&0&0&0\\ 0&0&0&0\\ 0&0&0&0
\end{pmatrix},
$$

the two blocks acting on the real coordinates $(e_t,\vec e_x,\vec e_y,\vec e_z)$ and on the imaginary coordinates $(ie_t,i\vec e_x,i\vec e_y,i\vec e_z)$.

*Proof.* On the real basis directions, $\vec e_x\star e_t=-\vec e_x$, $\vec e_x\star \vec e_x=-e_t$ and $\vec e_x\star \vec e_k=0$ for $k\in\{y,z\}$; on the imaginary directions, $\vec e_x\star ie_t=i\vec e_x$ and $\vec e_x\star i\vec e_x=ie_t$, with zero for $k\in\{y,z\}$, from the definition and the table. This gives the first display; the right multiplication is read from $e_t\star \vec e_x=-\vec e_x$, $\vec e_x\star \vec e_x=-e_t$, $ie_t\star \vec e_x=-i\vec e_x$, $i\vec e_x\star \vec e_x=-ie_t$, giving the second.

**Remark (the general matrix).** For a general element $\tilde A$, the two matrices are obtained from the single rule $\tilde A\star\tilde Q_1=\langle\tilde A,\tilde Q_1\rangle_{\natural*}e_t-A_t\overline{\vec Q_1}-\overline{Q_{1t}}\vec A$: the columns record the images of the basis elements, and the entries are the real and imaginary parts of the coefficients of $\tilde A$. The two special matrices above are the two cases in which the images are pure basis directions, and they show the block structure of the two families.

## Rank, Image and Trace

**Theorem (the rank of the two operators).** For an element $\tilde A$,

$$
\mathrm{rank}\,L^{\star}_{\tilde A}=\mathrm{rank}\,R^{\star}_{\tilde A}=
\begin{cases}
0,&\tilde A=0,\\
4,&A_t=0,\ \tilde A\neq0,\\
8,&A_t\neq0,\ \langle\tilde A\rangle_{\natural}\neq0,\\
6,&A_t\neq0,\ \langle\tilde A\rangle_{\natural}=0,
\end{cases}
$$

where the rank is the rank of the real-linear operator on the eight-real-dimensional space.

*Proof.* The two families have the same rank, because the two determinants agree, $\det L^{\star}_{\tilde A}=\det R^{\star}_{\tilde A}=|\langle\tilde A\rangle_{\natural}|^{2}|A_t|^{4}$ as real-linear operators in the real basis: a direct expansion of the two $8\times8$ matrices gives the product of the squared norm and the fourth power of the scalar part in each case, and the two determinants agree because $L^{\star}_{\tilde A}=C\circ R^{\star}_{\tilde A}$ with $C$ the coefficientwise conjugation, whose real matrix $\mathrm{diag}(1,1,1,1,-1,-1,-1,-1)$ has determinant $+1$, by the parity theorem. Hence the rank is eight exactly when $A_t\neq0$ and $\langle\tilde A\rangle_{\natural}\neq0$, and the remaining values are read directly: $\tilde A=0$ gives the zero map, and $A_t=0$ with $\tilde A\neq0$ gives rank four by the next corollary. In the remaining case $A_t\neq0$ the kernel is computed without the determinant. The vector part is $-A_t\overline{\vec Q_1}-\overline{Q_{1t}}\vec A$, so it vanishes exactly when $\vec Q_1=-(Q_{1t}/\overline{A_t})\overline{\vec A}$, which determines the vector part of a kernel element by its scalar coefficient; substituting this into the scalar part $A_t\overline{Q_{1t}}-\sum_kA_k\overline{Q_{1k}}$ leaves $\overline{Q_{1t}}\,\langle\tilde A\rangle_{\natural}/A_t$. The kernel is therefore zero when $\langle\tilde A\rangle_{\natural}\neq0$ and the complex line $\{\vec Q_1=-(Q_{1t}/\overline{A_t})\overline{\vec A}\}$, of real dimension two, when $\langle\tilde A\rangle_{\natural}=0$; the rank is $8$ in the first case and $6$ in the second, and at $\tilde A=e_t+i\vec e_y$ that line is spanned by $e_t+i\vec e_y$ and $ie_t-\vec e_y$.

**Corollary (the four-dimensional image).** For $\tilde A$ in the vector subspace, the image of $L^{\star}_{\tilde A}$ is a four-dimensional real subspace that is not one of the remarkable subspaces. For $\tilde A=\vec e_x$,

$$
L^{\star}_{\vec e_x}(\mathbb{B})=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t,\vec e_x,i\vec e_x\},
$$

the sum of the complex line through $e_t$ and the complex line through $\vec e_x$.

*Proof.* For $A_t=0$ the display reads $\tilde A\star\tilde Q_1=\langle\tilde A,\tilde Q_1\rangle_{\natural*}e_t-\overline{Q_{1t}}\vec A$, so the image is the sum of the complex line $\mathbb{C}e_t$ carried by the first term and the complex line $\mathbb{C}\vec A$ carried by $\bar Q_{1t}$, and the two lines are independent because $\vec A$ lies in the vector subspace; the image has real dimension four, and for $\tilde A=\vec e_x$ it is spanned by $\vec e_x\star \vec e_x=-e_t$, $\vec e_x\star e_t=-\vec e_x$, $\vec e_x\star i\vec e_x=ie_t$, $\vec e_x\star ie_t=i\vec e_x$, that is the displayed span. The image always contains the whole centre $\mathbb{C}e_t$, whereas each of the four four-dimensional subspaces of the remarkable subspaces meets the centre in a single real line, $\mathbb{R}e_t$ or $\mathbb{R}ie_t$; so the image is not one of the four, and it is neither the centre nor the vector subspace, whose real dimensions are two and six.

**Theorem (the traces).** For every element $\tilde A$,

$$
\mathrm{tr}\,L^{\star}_{\tilde A}=0,
\qquad
\mathrm{tr}\,R^{\star}_{\tilde A}=-4\,\mathrm{Re}(A_t),
$$

the traces being the traces of the real-linear operators in the real basis.

*Proof.* The trace is real-linear in the real coordinates of $\tilde A$. For the left family the diagonal of the real matrix of $L^{\star}_{\tilde A}$ is $\mathrm{Re}(A_t)$ times the diagonal of $L^{\star}_{e_t}$, which is $(1,-1,-1,-1,-1,1,1,1)$ and has sum $0$, and every other real basis direction of $\tilde A$ contributes zero on the diagonal; hence $\mathrm{tr}\,L^{\star}_{\tilde A}=0$, as the two special matrices show at $\tilde A=e_t$ and at $\tilde A=\vec e_x$. For the right family the diagonal is $\mathrm{Re}(A_t)$ times the diagonal of $R^{\star}_{e_t}$, which is $(1,-1,-1,-1,1,-1,-1,-1)$ and has sum $-4$, so $\mathrm{tr}\,R^{\star}_{\tilde A}=-4\mathrm{Re}(A_t)$, again zero contribution from every other direction, as the two special matrices show at $\tilde A=e_t$ ($-4$) and at $\tilde A=\vec e_x$ ($0$).

**Theorem (the kernel).** The kernel of $L^{\star}_{\tilde A}$ is zero when the rank is eight, of real dimension two when $A_t\neq0$ and $\langle\tilde A\rangle_{\natural}=0$, of real dimension four when $A_t=0$ and $\tilde A\neq0$, and is the whole space when $\tilde A=0$.

*Proof.* This is the rank theorem, read as $8-\mathrm{rank}$. For $\tilde A=\vec e_x$ the kernel is $\mathrm{span}_{\mathbb{R}}\{\vec e_y,\vec e_z,i\vec e_y,i\vec e_z\}$, since $\vec e_x\star \vec e_k=\vec e_x\star i\vec e_k=0$ for $k\in\{y,z\}$.

## The Composition and the Defect of Multiplicativity

**Theorem (the defect).** The two families do not multiply:

$$
L^{\star}_{\tilde A}\circ L^{\star}_{\tilde Q_2}\neq L^{\star}_{\tilde A\star\tilde Q_2},
\qquad
R^{\star}_{\tilde A}\circ R^{\star}_{\tilde Q_2}\neq R^{\star}_{\tilde A\star\tilde Q_2},
$$

the defect of the left composition is the associator

$$
\tilde A\star(\tilde Q_2\star\tilde Q_1)-(\tilde A\star\tilde Q_2)\star\tilde Q_1,
$$

the defect of the right composition is the mirrored expression $(\tilde Q_1\star\tilde Q_2)\star\tilde A-\tilde Q_1\star(\tilde A\star\tilde Q_2)$, and each is nonzero on a general triple. For the left family the inequality is forced by parity, the composition being $\mathbb{C}$-linear and the single left multiplication conjugate-linear.

*Proof.* The defect of $L^{\star}$ at $\tilde Q_1$ is the associator, and the defect of $R^{\star}$ is the same computation read with the factors in the other order. At $\tilde A=\tilde Q_2=\tilde Q_1=\vec e_x$ the associator is $\vec e_x\star(\vec e_x\star \vec e_x)-(\vec e_x\star \vec e_x)\star \vec e_x=\vec e_x\star(-e_t)-(-e_t)\star \vec e_x=\vec e_x-\vec e_x=0$; at a generic triple both defects are nonzero, since the block is not associative. For the left family, the composition of two conjugate-linear maps is linear, while $L^{\star}_{\tilde A\star\tilde Q_2}$ is conjugate-linear, so the two agree only if both are zero.

**Remark.** The block fails multiplicativity of the operators for two independent reasons: the associator, which is the ordinary defect of a non-associative product, and the parity, which the left family alone carries. The corresponding statement for the general quaternionic sesquilinear product is in *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*.

## The Adjoint with Respect to $K$ and $J$-Self-Adjointness

**Theorem (the adjoint).** With respect to the Krein form $\langle\cdot,\cdot\rangle_{\natural*}$,

$$
K\bigl(L^{\star}_{\tilde A}\tilde Q_1,\tilde Q_3\bigr)
=\overline{K\bigl(\tilde Q_1,L^{\star}_{\tilde A^{\natural}}\tilde Q_3\bigr)},
$$

so the adjoint of the left multiplication by $\tilde A$ is the left multiplication by $\tilde A^{\natural}$.

*Proof.* This is the compatibility theorem of *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*: $\langle\tilde A\star\tilde Q_1,\tilde Q_3\rangle_{\natural*}=\overline{\langle\tilde Q_1,\tilde A^{\natural}\star\tilde Q_3\rangle_{\natural*}}$, which is exactly the display; the conjugate on the right is the parity correction of the conjugate-linear operator.

**Corollary ($J$-self-adjointness).** The left multiplication by $\tilde A$ is self-adjoint with respect to $K$ exactly when $\tilde A^{\natural}=\tilde A$, that is on the centre $\mathbb{C}e_t$, the fixed set of the natural conjugation.

*Proof.* The adjoint is the left multiplication by $\tilde A^{\natural}$; it equals the left multiplication by $\tilde A$ exactly when the two elements are equal, since the map $\tilde A\mapsto L^{\star}_{\tilde A}$ is injective. The fixed elements of the natural conjugation, $\tilde A^{\natural}=\tilde A$, are the central ones, $A_x=A_y=A_z=0$ and $A_t$ arbitrary.

**Remark (the involution $J$).** The involution singled out by the adjoint is the natural conjugation $J={}^{\natural}$, acting on the parameter of the operator; the block is inert under the family $\tilde A\mapsto\tilde A^{\natural}$ because the natural conjugation is an automorphism of the product, so the adjoint is a permutation of the left multiplications. The operators with the conjugate transpose of the general quaternionic sesquilinear product are *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra*, where the same involution appears.

## The Groups

**Theorem (the group of linear maps preserving $K$).** The set of $\mathbb{C}$-linear operators $T$ with $\langle T\tilde P,T\tilde Q\rangle_{\natural*}=\langle\tilde P,\tilde Q\rangle_{\natural*}$ for all $\tilde P,\tilde Q$ is a group of real dimension sixteen; in the coefficient basis its matrices $M$ satisfy

$$
M^{\dagger}EM=E,
\qquad E=\mathrm{diag}(1,-1,-1,-1),
$$

and its Lie algebra is the set of $\mathbb{C}$-linear $X$ with $X^{\dagger}E+EX=0$, of real dimension sixteen.

*Proof.* Write $\langle\tilde P,\tilde Q\rangle_{\natural*}=P^{T}E\overline{Q}$ in the coefficient basis; then $\langle T\tilde P,T\tilde Q\rangle_{\natural*}=P^{T}M^{T}E\overline{M}\,\overline{Q}$, which equals $\langle\tilde P,\tilde Q\rangle_{\natural*}$ for all $P,Q$ exactly when $M^{T}E\overline{M}=E$, equivalently, after conjugation, $M^{\dagger}EM=E$. The condition is quadratic and its linearisation at the identity is $X^{\dagger}E+EX=0$; the matrices of the group are counted by $32$ real parameters subject to the $16$ real equations of $M^{\dagger}EM=E$, since $M^{\dagger}EM$ is Hermitian, so the group has real dimension $16$.

**Remark.** The group is the one of the general quaternionic sesquilinear row, because $\langle\cdot,\cdot\rangle_{\natural*}$ is that form with the arguments read in the other order; the details and the corresponding $J$-unitary family are in *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra*. The Lie algebra of the theorem is the linearisation recorded there.

**Theorem (the structure group of the block).** The natural conjugation ${}^{\natural}$ is a $\mathbb{C}$-linear automorphism of the product, the coefficientwise conjugation $\bar{\cdot}$ is a conjugate-linear automorphism, and the star conjugation ${}^{*}$ is their composite, also a conjugate-linear automorphism. The two involutions ${}^{\natural}$ and $\bar{\cdot}$ generate a group of order four,

$$
\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\},
$$

acting on the block.

*Proof.* The three maps satisfy $\varphi(\tilde P\star\tilde Q)=\varphi(\tilde P)\star\varphi(\tilde Q)$ for all $\tilde P,\tilde Q$, by the definition of the product and the two anti-automorphism properties of the conjugations; each is an involution and ${}^{*}={}^{\natural}\circ\bar{\cdot}$, so they generate the Klein group of the display.

**Remark (what is not decided).** The theorem exhibits four automorphisms; whether they exhaust the automorphism group of the block is not decided here. The group preserving $K$ is larger, of dimension sixteen, and the two groups are not the same: the automorphisms of the product are a finite group, while the maps preserving the form include the whole sixteen-dimensional family of the theorem above.

## Worked Examples

**The two operators at a general element.** $\tilde Q_1=e_t+\vec e_x$: $L^{\star}_{e_t}\tilde Q_1=\tilde Q_1^{*}=e_t-\vec e_x$ and $R^{\star}_{e_t}\tilde Q_1=\tilde Q_1^{\natural}=e_t-\vec e_x$, the two operators agreeing on a real element; $L^{\star}_{\vec e_x}\tilde Q_1=\vec e_x\star(e_t+\vec e_x)=-\vec e_x-e_t$.

**A four-dimensional image.** For $\tilde A=\vec e_x$ the image is $\mathrm{span}_{\mathbb{R}}\{e_t,ie_t,\vec e_x,i\vec e_x\}$: it contains the complex line $\mathbb{C}e_t$ and the complex line $\mathbb{C}\vec e_x$ and nothing else, and it is not among the remarkable subspaces.

**A trace.** $\mathrm{tr}\,R^{\star}_{e_t}=-4\mathrm{Re}(1)=-4$, as the diagonal matrix of the theorem shows.

**A kernel.** For $\tilde A=\vec e_x$ the kernel is $\mathrm{span}_{\mathbb{R}}\{\vec e_y,\vec e_z,i\vec e_y,i\vec e_z\}$, of real dimension four, since $\vec e_x\star \vec e_y=\vec e_x\star \vec e_z=0$.

**A self-adjoint element.** $\tilde A=ie_t\in\mathbb{C}e_t$: $\tilde A^{\natural}=ie_t=\tilde A$, so the left multiplication is self-adjoint with respect to $K$. An element of $\mathbb{M}_{+}$, for instance $e_t+i\vec e_x$, is not self-adjoint, since $(e_t+i\vec e_x)^{\natural}=e_t-i\vec e_x\neq e_t+i\vec e_x$.

**An automorphism.** ${}^{\natural}(\vec e_x\star \vec e_y)={}^{\natural}(0)=0$ and $\vec e_x^{\natural}\star \vec e_y^{\natural}=(-\vec e_x)\star(-\vec e_y)=\vec e_x\star \vec e_y=0$; the natural conjugation respects the product.

## Summary

The operators of the block are $L^{\star}_{\tilde A}(\tilde Q_1)=\tilde A\star\tilde Q_1$, conjugate-linear, and $R^{\star}_{\tilde A}(\tilde Q_1)=\tilde Q_1\star\tilde A$, linear, related by $L^{\star}_{\tilde A}(\tilde Q_1)=\overline{R^{\star}_{\tilde A}(\tilde Q_1)}$. In the real basis $L^{\star}_{e_t}$ is the star conjugation and $R^{\star}_{e_t}$ the natural conjugation, and the operators of $\vec e_x$ have the exhibited block matrices. The ranks of the two families, equal, are $0$ at $\tilde A=0$, $4$ for $\tilde A$ in the vector subspace, $8$ for $A_t\neq0$ with $\langle\tilde A\rangle_{\natural}\neq0$ and $6$ for $A_t\neq0$ with $\langle\tilde A\rangle_{\natural}=0$; the four-dimensional image at $\tilde A=\vec e_x$ is $\mathrm{span}_{\mathbb{R}}\{e_t,ie_t,\vec e_x,i\vec e_x\}$, not one of the remarkable subspaces. The traces are $0$ for the left family and $-4\mathrm{Re}(A_t)$ for the right; the kernels are read from the ranks. The operators do not multiply: the left defect is the associator and the right defect its mirror, the left case being forced by parity. The adjoint with respect to $K$ is $\langle L^{\star}_{\tilde A}\tilde Q_1,\tilde Q_3\rangle_{\natural*}=\overline{\langle\tilde Q_1,L^{\star}_{\tilde A^{\natural}}\tilde Q_3\rangle_{\natural*}}$, which gives the $J$-self-adjointness with $J={}^{\natural}$ on the centre $\mathbb{C}e_t$. The group of $\mathbb{C}$-linear maps preserving $K$ has real dimension sixteen and its matrices satisfy $M^{\dagger}EM=E$; the structure group of the block contains the four automorphisms $\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L^{\star}_{\tilde A}(\tilde Q_1)=\tilde A\star\tilde Q_1$ | the left multiplication, conjugate-linear |
| $R^{\star}_{\tilde A}(\tilde Q_1)=\tilde Q_1\star\tilde A$ | the right multiplication, linear |
| $L^{\star}_{e_t}=\tilde Q_1^{*}$, $R^{\star}_{e_t}=\tilde Q_1^{\natural}$ | the two conjugations as operators |
| $\mathrm{rank}\,L^{\star}_{\tilde A}=\mathrm{rank}\,R^{\star}_{\tilde A}\in\{0,4,6,8\}$ | the rank of the two families |
| $\mathrm{span}_{\mathbb{R}}\{e_t,ie_t,\vec e_x,i\vec e_x\}$ | the four-dimensional image at $\tilde A=\vec e_x$ |
| $\mathrm{tr}\,L^{\star}_{\tilde A}=0$, $\mathrm{tr}\,R^{\star}_{\tilde A}=-4\mathrm{Re}(A_t)$ | the traces |
| $\langle L^{\star}_{\tilde A}\tilde Q_1,\tilde Q_3\rangle_{\natural*}=\overline{\langle\tilde Q_1,L^{\star}_{\tilde A^{\natural}}\tilde Q_3\rangle_{\natural*}}$ | the adjoint with respect to $K$; $J={}^{\natural}$ |
| $M^{\dagger}EM=E$ | the condition of the group of linear maps preserving $K$ |
| $\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$ | the automorphisms of the block exhibited |

## Further Reading

- *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product* (`articles_maths/the-left-and-right-multiplications-of-the-quaternionic-sesquilinear-product.md`), for the operators of the unsplit product.
- *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra* (`articles_maths/j-self-adjoint-and-j-unitary-operators-on-the-general-quaternionic-sesqualgebra.md`), for the operators with the conjugate transpose and the group preserving the form.
- *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra* (`articles_maths/the-krein-form-as-a-product-on-the-symmetric-quaternionic-sesqualgebra.md`), for the form $\langle\cdot,\cdot\rangle_{\natural*}$ and the adjoint relation in the form setting.
- *Introduction to the Symmetric Quaternionic Sesqualgebra* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra.md`), for the product and its parity.
- *Remarkable Subspaces under the Symmetric Quaternionic Sesqualgebra* (`articles_maths/remarkable-subspaces-under-the-symmetric-quaternionic-sesqualgebra.md`), for the remarkable subspaces and the vector subspace carrying the four-dimensional image.
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra.md`), for the norm $\langle\cdot\rangle_{\natural}$ entering the rank table.
- *The 12 Products of the Biquaternioid Complex Space* (`articles_maths/the-12-products-of-the-biquaternioid-complex-space.md`), for the comparison of the operators of the twelve operations.
