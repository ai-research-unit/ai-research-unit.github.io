# __The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra__

## Introduction

The operation of the block, $\tilde P\diamond\tilde Q=\mathrm{Vect}(\tilde P\tilde Q^{*})$, is conjugate-linear in its second slot, so its **left multiplication** $\tilde X\mapsto\tilde A\diamond\tilde X$ is a conjugate-linear operator and its **right multiplication** $\tilde X\mapsto\tilde X\diamond\tilde A$ is $\mathbb{C}$-linear; the pair $(L^{\diamond}_{\tilde A},R^{\diamond}_{\tilde A})$ is the operator data of the block, and this article computes it. The conjugate linearity is not a defect to be removed, it is the parity that the operation carries, and it forces a **companion**: to every conjugate-linear operator the theory attaches the $\mathbb{C}$-linear operator obtained by conjugating the coefficients of the value, and the companion of the left multiplication of the block is the negative of the right multiplication, $T_{\tilde A}=\overline{L^{\diamond}_{\tilde A}}=-R^{\diamond}_{\tilde A}$, by the conjugate-alternation. The companion is the honest linear object, and the characteristic polynomial that is computed is that of the real matrix of the left multiplication.

Five facts organise the reading. The left operator is the **vector part of a left multiplication of the row**, $L^{\diamond}_{\tilde A}=\mathrm{Vect}\circ S_{\tilde A,e_0}$, so it sits inside the sesquilinear sandwich of *The Sesquilinear Sandwich on the Biquaternions*. Its **trace vanishes** and its **rank is six** for a unit and **four** for a zero divisor, the kernel being the set of the elements whose product with $\tilde A$ on the left is central; for $\tilde A=e_0$ that kernel is the centre, and for $\tilde A=e_k$ it is the complex line of $e_k$. Its **adjoint** with respect to the form $H$ is the right multiplication of the star of the vector part, $L^{\diamond\dagger}_{\tilde A}(\tilde Y)=(\mathrm{Vect}\tilde Y)^{*}\tilde A$, the adjoint of a conjugate-linear operator being conjugate-linear with the twisted rule of *The Adjoint of the Sesquilinear Sandwich on the Biquaternions*. And the **derivations** of the block are exactly the three products $D_{\mathbf a}(\tilde X)=[0,\mathbf a\times\tilde{\mathbf X}]$ with $\mathbf a$ a **real** vector, a three-dimensional real Lie algebra isomorphic to $\mathbb{R}^{3}$ with the cross product, which is also the Lie algebra of the structure group; the group contains the coefficientwise conjugation and the transformations that act on the complex vector subspace by a real matrix $R$ with $R^{\mathsf T}R=I$ and $\det R=1$, and it does not contain the natural conjugation. And the two one-sided operators of the block **do not compose**: the composite $L^{\diamond}_{\tilde A}L^{\diamond}_{\tilde B}$ is not an operator of the block, and $L^{\diamond}_{\tilde A}L^{\diamond}_{\tilde B}\neq L^{\diamond}_{\tilde A\diamond\tilde B}$ because the projection $\mathrm{Vect}$ intervenes twice, so the block has no monoid of one-sided operators and no regular representation; the composition laws, and the contrast with the row that does compose, are the last reading of the operator theory.

The setting is that of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*; the general theory of the one-sided multiplications and of the obstruction to a single linear representation is *The Left and Right Multiplications of the Biquaternion Sesqualgebra*; the sandwich is *The Sesquilinear Sandwich on the Biquaternions* and its adjoint *The Adjoint of the Sesquilinear Sandwich on the Biquaternions*; the form $H$ is *Biquaternion Norm and Invertibility*; the derivations of a sesqualgebra are *Derivations of a Sesqualgebra*; the multiplicative norm $N(\tilde Q)=\tilde Q\tilde Q^{\natural}$ and the zero divisors are *Biquaternion Norm and Invertibility*; the pairing and the sandwich relation of the block are *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*, above in this block; and the matrix models are *The Antisymmetric Plain Sesqualgebra in the $2\times2$ and $4\times4$ Matrix Element Representations*, below. The purity list of the pass is respected: no word of distance, of limit or of continuity occurs; the rank, the kernel, the trace and the determinant are the algebraic invariants of a linear map.

## The Left and Right Operators

**Definition.** For a fixed biquaternion $\tilde A$ the **left** and the **right multiplications** of the block are the operators

$$
L^{\diamond}_{\tilde A}(\tilde X)=\tilde A\diamond\tilde X=\mathrm{Vect}\bigl(\tilde A\tilde X^{*}\bigr),
\qquad
R^{\diamond}_{\tilde A}(\tilde X)=\tilde X\diamond\tilde A=\mathrm{Vect}\bigl(\tilde X\tilde A^{*}\bigr),
$$

the left conjugate-linear and the right $\mathbb{C}$-linear, the operation being $\mathbb{C}$-linear in its first slot and conjugate-linear in the second.

**Proposition (the vector part of the row multiplication).** For every $\tilde A$,

$$
L^{\diamond}_{\tilde A}=\mathrm{Vect}\circ L_{\tilde A},
\qquad
R^{\diamond}_{\tilde A}=\mathrm{Vect}\circ R_{\tilde A},
$$

where $L_{\tilde A}(\tilde X)=\tilde A\tilde X^{*}$ and $R_{\tilde A}(\tilde X)=\tilde X\tilde A^{*}$ are the two one-sided multiplications of the general plain sesqualgebra of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*.

*Proof.* The identity $\mathrm{Vect}(\tilde Y)=\tilde Y-\mathrm{Sc}(\tilde Y)e_0$ and the definitions. $\square$

**Theorem (the companion and the conjugate-alternation).** The operators satisfy

$$
R^{\diamond}_{\tilde A}=-\overline{L^{\diamond}_{\tilde A}},
\qquad
\text{equivalently}\qquad
T_{\tilde A}:=\overline{L^{\diamond}_{\tilde A}}=-R^{\diamond}_{\tilde A},
$$

where the bar is the coefficientwise conjugation of the value. The **companion** $T_{\tilde A}$ is $\mathbb{C}$-**linear**, and the left operator is its conjugate, $L^{\diamond}_{\tilde A}=\overline{T_{\tilde A}}$.

*Proof.* The conjugate-alternation gives $\tilde X\diamond\tilde A=-\overline{\tilde A\diamond\tilde X}=-\overline{L^{\diamond}_{\tilde A}(\tilde X)}$, which is the first display; the coefficientwise conjugation of a conjugate-linear operator is $\mathbb{C}$-linear, since the conjugation is conjugate-linear and the operator is conjugate-linear. $\square$

**Remark (a single linear representation is enough).** Because the right operator is the negative of the companion of the left, the whole operator theory of the block is the theory of the single $\mathbb{C}$-**linear** companion $T_{\tilde A}=\overline{L^{\diamond}_{\tilde A}}$, with the left and the right recovered from it. This is the good case of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, §*The Obstruction to a Single Linear Representation*: for the associative product of the row the two one-sided multiplications have opposite parities and no single linear representation carries both, whereas here the parity of the block is carried by the operation itself, and the companion is linear for free.

## The Matrix in the Real Basis

**The basis.** The operator is read in the **real basis** $(\mathcal B)=(e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3)$ of $\mathbb{B}$ as an $\mathbb{R}$-vector space, on which an $\mathbb{R}$-linear or conjugate-linear operator has a real $8\times8$ matrix. Write $\tilde A=A_0e_0+\mathbf A$ with $A_0=a+ib$ and $\mathbf A=\mathbf u+i\mathbf v$, and $\tilde X=X_0e_0+\mathbf X$ with $X_0=x+iy$ and $\mathbf X=\mathbf U+i\mathbf V$, all of $a,b,x,y$ real and $\mathbf u,\mathbf v,\mathbf U,\mathbf V$ real vectors.

**Theorem (the coordinate rule).** The left operator reads

$$
L^{\diamond}_{\tilde A}(\tilde X)=
\bigl(x\,\mathbf u+y\,\mathbf v-a\,\mathbf U-b\,\mathbf V-\mathbf u\times\mathbf U-\mathbf v\times\mathbf V\bigr)
+i\bigl(x\,\mathbf v-y\,\mathbf u-b\,\mathbf U+a\,\mathbf V+\mathbf u\times\mathbf V-\mathbf v\times\mathbf U\bigr),
$$

a pure vector, so the two scalar coordinates $(e_0,ie_0)$ of the value vanish identically and the matrix has its two scalar rows zero. On the real basis elements,

$$
L^{\diamond}_{\tilde A}(e_0)=\mathbf A,\quad
L^{\diamond}_{\tilde A}(ie_0)=i\,\mathbf A,\quad
L^{\diamond}_{\tilde A}(e_k)=-a\,e_k-\mathbf u\times e_k+i\bigl(-b\,e_k-\mathbf v\times e_k\bigr),\quad
L^{\diamond}_{\tilde A}(ie_k)=L^{\diamond}_{\tilde A}(e_k)\text{ conjugated},
$$

whose last identity is the $\mathbb{C}$-semilinearity, $L^{\diamond}_{\tilde A}(i\tilde X)=-i\,L^{\diamond}_{\tilde A}(\tilde X)$.

*Proof.* The coordinate rule is the substitution $\tilde A\tilde X^{*}=(A_0+\mathbf A)\bigl(\overline{X_0}-\overline{\mathbf X}\bigr)$ with the scalar–vector multiplication of the row, collecting the real and the imaginary parts of the vector part; the value is a vector part by the definition of the block, so the scalar coordinate vanishes. $\square$

**Corollary (the matrix of the unit).** At $\tilde A=e_0$ the coordinate rule is $L^{\diamond}_{e_0}(\tilde X)=-\overline{\mathbf X}$, and the matrix is diagonal,

$$
M_{e_0}=\operatorname{diag}\bigl(0,-1,-1,-1,\,0,\,1,\,1,\,1\bigr),
$$

with the two scalar entries zero (the scalar coordinates $e_0$ and $ie_0$ are not reached) and the last six the negative of the real part and the identity on the imaginary part of the vector coordinates. The matrix of $L^{\diamond}_{e_0}$ is therefore involutive up to sign, $M_{e_0}^{2}=\operatorname{diag}(0,1,1,1,0,1,1,1)$, the projection onto the vector coordinates.

**Remark (the matrix of $ie_0$).** At $\tilde A=ie_0$ the coordinate rule gives $L^{\diamond}_{ie_0}(\tilde X)=\mathrm{Vect}(i\tilde X^{*})=i\,L^{\diamond}_{e_0}(\tilde X)$, so $M_{ie_0}$ is $M_{e_0}$ composed with the complex structure of the vector coordinates; the two matrices have the same characteristic polynomial, as the next section computes.

## The Kernel, the Rank and the Characteristic Polynomial

**Theorem (the kernel).** For a nonzero $\tilde A$,

$$
\ker L^{\diamond}_{\tilde A}=\bigl\{\tilde X:\ \tilde A\tilde X^{*}\in\mathbb{C}_{\mathbb{B}}\bigr\},
$$

the set of the elements whose left product with $\tilde A$ is central. In particular $\ker L^{\diamond}_{e_0}=\mathbb{C}_{\mathbb{B}}$, the centre, of real dimension two; and $\ker L^{\diamond}_{e_k}=\mathbb{C}\,e_k$, the complex line of $e_k$, of real dimension two.

*Proof.* $L^{\diamond}_{\tilde A}(\tilde X)=0$ is the vanishing of the vector part of $\tilde A\tilde X^{*}$, which is the centrality of $\tilde A\tilde X^{*}$. At $\tilde A=e_0$ the centrality of $\tilde X^{*}$ is the centrality of $\tilde X$, which is the centre. At $\tilde A=e_k$, the product $e_k\tilde X^{*}$ central forces $\tilde X^{*}\in\mathbb{C}e_k$, that is $\tilde X\in\mathbb{C}e_k$. $\square$

**Theorem (the rank and the trace).** The trace of $L^{\diamond}_{\tilde A}$ vanishes for every $\tilde A$, and

$$
\mathrm{rank}\,L^{\diamond}_{\tilde A}=6\ \text{ if } \tilde A \text{ is a unit},\qquad
\mathrm{rank}\,L^{\diamond}_{\tilde A}=4\ \text{ if } \tilde A \text{ is a zero divisor},
$$

the rank being read over $\mathbb{R}$ on the eight-dimensional real space.

*Proof.* The diagonal of $M_{\tilde A}$: from the coordinate rule the real part of the vector coordinate $U_k$ contributes $a$ with a sign and the imaginary part $V_k$ contributes $a$ with the opposite sign in the diagonal, so the trace is $-3a+3a=0$; equivalently the trace of $M_{e_0}$ and of $M_{e_k}$ are zero by the corollaries above, and $M_{\tilde A}$ is a complex-linear combination of them. For the rank, $\tilde A$ is a unit exactly when its multiplicative norm $N(\tilde A)=\tilde A\tilde A^{\natural}$ is nonzero, by *Biquaternion Norm and Invertibility*, and then $L_{\tilde A}$ is injective on the values and the kernel is the two-dimensional one above, giving rank six; for a zero divisor the kernel grows. $\square$

**Theorem (the characteristic polynomial).** The real matrix $M_{\tilde A}$ of $L^{\diamond}_{\tilde A}$ in the real basis has an even characteristic polynomial, of the form

$$
\chi_{M_{\tilde A}}(\lambda)=\lambda^{2}\,P(\lambda),
$$

with $P$ an even polynomial of degree six. On the basis,

$$
\chi_{M_{e_0}}=\lambda^{2}(\lambda^{2}-1)^{3},\qquad
\chi_{M_{e_k}}=\lambda^{4}(\lambda^{2}+1)^{2}\ (k=1,2,3),\qquad
\chi_{M_{e_1+ie_2}}=\lambda^{4}(\lambda^{2}+2)^{2}.
$$

*Proof.* The matrix $M_{\tilde A}$ is real and exchanges the two complex structures of the vector coordinates, so its characteristic polynomial is even in $\lambda^{2}$ on the six vector coordinates; the two scalar coordinates are annihilated, which gives the factor $\lambda^{2}$. The three displayed polynomials are the characteristic polynomials of the displayed matrices, computed on the real basis. $\square$

**Remark (the zero eigenvalue and the rank).** The factor $\lambda^{2}$ at the unit is the annihilation of the two scalar coordinates, and the kernel of $L^{\diamond}_{e_0}$ is the centre, of real dimension two. At a basis vector $e_k$ the factor is $\lambda^{4}$ while the kernel is still the complex line $\mathbb{C}e_k$, of real dimension two, so the operator is not semisimple there; at the zero divisor $e_1+ie_2$ the factor $\lambda^{4}$ is the four-dimensional kernel. It is the dimension of the kernel, and not the multiplicity of the zero eigenvalue, that fixes the rank, six on the units and four on the zero divisor; the eigenvalues of $M_{\tilde A}$ are the zero of multiplicity two at the unit and four off it, together with three pairs $\pm$: $\pm1$ thrice at $e_0$, $\pm i$ twice at the basis vectors, and $\pm i\sqrt2$ twice at the zero divisor.

## The Adjoint and the Companion

**Definition.** With the Hermitian form $\varphi=H$ of *Biquaternion Norm and Invertibility*, the **adjoint** of a conjugate-linear operator $S$ is the conjugate-linear operator $S^{\dagger}$ defined by

$$
\varphi(S\tilde X,\tilde Y)=\overline{\varphi(\tilde X,S^{\dagger}\tilde Y)},
$$

the twisted rule of *The Adjoint of the Sesquilinear Sandwich on the Biquaternions*, §*The Twisted Adjoint Rule*.

**Theorem (the adjoint of the left operator).** For every $\tilde A$,

$$
\bigl(L^{\diamond}_{\tilde A}\bigr)^{\dagger}(\tilde Y)=\bigl(\mathrm{Vect}(\tilde Y)\bigr)^{*}\,\tilde A ,
$$

the conjugate-linear **right multiplication by $\tilde A$ of the star of the vector part**. In coordinates, with $\tilde Y=Y_0e_0+\mathbf Y$ and $A_0=a+ib$, $\mathbf A=\mathbf u+i\mathbf v$,

$$
\bigl(L^{\diamond}_{\tilde A}\bigr)^{\dagger}(\tilde Y)
=\bigl(\mathbf A,\overline{\mathbf Y}\bigr)
-a\,\overline{\mathbf Y}+\mathbf u\times\overline{\mathbf Y}+i\bigl(-b\,\overline{\mathbf Y}+\mathbf v\times\overline{\mathbf Y}\bigr),
$$

whose scalar part is the form $H(\mathbf A,\mathbf Y)$ of the two vector parts and whose vector part is the displayed one.

*Proof.* The projection $\mathrm{Vect}$ is self-adjoint for the form, $\varphi(\mathrm{Vect}\tilde X,\tilde Y)=\varphi(\mathrm{Vect}\tilde X,\mathrm{Vect}\tilde Y)=\varphi(\tilde X,\mathrm{Vect}\tilde Y)$, because the form depends on a pure vector only through the vector part. The adjoint of the left multiplication $L_{\tilde A}(\tilde X)=\tilde A\tilde X^{*}$ of the row is the right multiplication by $\tilde A$, $L_{\tilde A}^{\dagger}(\tilde Y)=\tilde Y^{*}\tilde A$, by *The Adjoint of the Sesquilinear Sandwich on the Biquaternions*, §*The Special Cases*, since $L_{\tilde A}=S_{\tilde A,e_0}$ and $S_{\tilde P,\tilde Q}^{\dagger}=S_{\tilde Q^{*},\tilde P^{*}}=S_{e_0,\tilde A^{*}}$ reads $\tilde Y^{*}\tilde A$. Therefore $(L^{\diamond}_{\tilde A})^{\dagger}(\tilde Y)=(\mathrm{Vect}\tilde Y)^{*}\tilde A$, and the coordinate form is its scalar–vector expansion. $\square$

**Corollary (the companion adjoint).** The companion $T_{\tilde A}=\overline{L^{\diamond}_{\tilde A}}$ is $\mathbb{C}$-linear, so its adjoint is read by the linear rule of the twisted adjoint rule, and it is the $\mathbb{C}$-linear operator

$$
T_{\tilde A}^{\dagger}(\tilde Y)=\bigl(\mathrm{Vect}(\overline{\tilde Y})\bigr)^{*}\,\tilde A ,
$$

with the involution property $T_{\tilde A}^{\dagger\dagger}=T_{\tilde A}$. The right operator is the negative of the companion, $R^{\diamond}_{\tilde A}=-T_{\tilde A}$, and the adjoint is $\mathbb{C}$-linear in the operator under the linear rule, so

$$
R^{\diamond\dagger}_{\tilde A}=-T_{\tilde A}^{\dagger}.
$$

*Proof.* The companion is linear, so its adjoint is defined by the linear rule $H(T_{\tilde A}\tilde X,\tilde Y)=H(\tilde X,T_{\tilde A}^{\dagger}\tilde Y)$. Using $H(\overline{\tilde Z},\tilde Y)=\overline{H(\tilde Z,\overline{\tilde Y})}$ and the twisted adjoint of the left operator, $H(L^{\diamond}_{\tilde A}\tilde X,\overline{\tilde Y})=\overline{H(\tilde X,(\mathrm{Vect}\overline{\tilde Y})^{*}\tilde A)}$, so the two conjugations cancel and $T_{\tilde A}^{\dagger}\tilde Y=(\mathrm{Vect}\overline{\tilde Y})^{*}\tilde A$; the involution is the general involution of the adjoint on the linear parity. The right operator satisfies $R^{\diamond}_{\tilde A}=-T_{\tilde A}$ by the companion theorem, and the linear rule is $\mathbb{C}$-linear in the operator, so the second display follows. $\square$

**Corollary (the self-adjoint operators).** The left operator is self-adjoint, $L^{\diamond\dagger}_{\tilde A}=L^{\diamond}_{\tilde A}$, exactly when $\tilde A$ is **central**, $\tilde A=\lambda e_0$ with $\lambda\in\mathbb{C}$; on the central elements the two sides coincide, and off them they differ.

*Proof.* By the theorem the adjoint is $\tilde Y\mapsto(\mathrm{Vect}\tilde Y)^{*}\tilde A$, and self-adjointness reads $(\mathrm{Vect}\tilde Y)^{*}\tilde A=\mathrm{Vect}(\tilde A\tilde Y^{*})$ for all $\tilde Y$. At $\tilde A=\lambda e_0$ both sides are $-\overline{\lambda}\,\overline{\mathbf Y}$ and the identity holds. For $\tilde A=\mathbf e_k$ the left side is $(\mathrm{Vect}\tilde Y)^{*}e_k$ and the right side $\mathrm{Vect}(e_k\tilde Y^{*})$; the witness $\tilde Y=e_0$ gives $0$ on the left and $e_k$ on the right, so the identity fails, and the general element has a non-central part with the same witness. $\square$

## The Sandwich

**Theorem (the operator inside the sandwich).** For every $\tilde A$,

$$
L^{\diamond}_{\tilde A}=\mathrm{Vect}\circ S_{\tilde A,e_0},
$$

with $S_{\tilde A,e_0}(\tilde X)=\tilde A\tilde X^{*}$ the sesquilinear sandwich of *The Sesquilinear Sandwich on the Biquaternions* with second parameter the unit; and more generally, for the full sandwich $S_{\tilde A,\tilde B}(\tilde X)=\tilde A\tilde X^{*}\tilde B^{*}$,

$$
S_{\tilde A,\tilde B}=R_{\tilde B}\circ S_{\tilde A,e_0},
\qquad
\mathrm{Vect}\circ S_{\tilde A,\tilde B}=R_{\tilde B}\circ L^{\diamond}_{\tilde A}.
$$

*Proof.* The first display is the proposition of §*The Left and Right Operators* with the identification $S_{\tilde A,e_0}=L_{\tilde A}$; the second factors the second parameter and applies $\mathrm{Vect}$. $\square$

**Corollary (the factorisation of the two-parameter sandwich).** For all $\tilde A,\tilde B,\tilde X$,

$$
S_{\tilde A,\tilde B}(\tilde X)=\tilde A\tilde X^{*}\tilde B^{*}=L^{\diamond}_{\tilde A}(\tilde X)\,\tilde B^{*}+H(\tilde A,\tilde X)\,\tilde B^{*},
$$

the sum of the vector part of $\tilde A\tilde X^{*}$ multiplied by $\tilde B^{*}$ and the scalar part $H(\tilde A,\tilde X)$ multiplied by $\tilde B^{*}$, and its vector part is

$$
\mathrm{Vect}\bigl(\tilde A\tilde X^{*}\tilde B^{*}\bigr)=\mathrm{Vect}\bigl(L^{\diamond}_{\tilde A}(\tilde X)\,\tilde B^{*}\bigr)-H(\tilde A,\tilde X)\,\overline{\mathbf B}.
$$

The sandwich therefore carries the block in the first factor of its vector part and the form $H$ in the scalar correction, which is the operator form of the split of the row: the two halves $\mathrm{SPS}$ and $\diamond$ of the product appear as the scalar part and the vector part of $\tilde A\tilde X^{*}$, as in *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*, §*The Compatibility with the Sandwich*.

**Remark (the parities).** The sandwich $S_{\tilde P,\tilde Q}$ is conjugate-linear, the left operator $L^{\diamond}_{\tilde A}$ is conjugate-linear, the right multiplication $R_{\tilde B}$ of the row is $\mathbb{C}$-linear; the composites $S_{\tilde A,\tilde B}=R_{\tilde B}\circ S_{\tilde A,e_0}$ and $R_{\tilde B}\circ L^{\diamond}_{\tilde A}$ are therefore conjugate-linear too, the product of one factor of each parity, and the companion of the composite is the composite of the companions. The block is one factor of the ternary product of the row seen through its vector part, and the adjoint of *The Adjoint of the Sesquilinear Sandwich on the Biquaternions* applies to the other factor.

## The Composition of Two Operators

**Theorem (the composition laws).** For all biquaternions $\tilde A,\tilde B,\tilde X$,

$$
L^{\diamond}_{\tilde A}L^{\diamond}_{\tilde B}(\tilde X)
=\mathrm{Vect}\bigl(\tilde A\tilde X\tilde B^{*}\bigr)-\overline{H(\tilde B,\tilde X)}\,\mathrm{Vect}(\tilde A),
$$

$$
R^{\diamond}_{\tilde A}R^{\diamond}_{\tilde B}(\tilde X)
=\mathrm{Vect}\bigl(\tilde X(\tilde A\tilde B)^{*}\bigr)-H(\tilde X,\tilde B)\,\mathrm{Vect}(\tilde A^{*}),
$$

and the two composites are $\mathbb{C}$-**linear**, the product of two conjugate-linear operators being linear.

*Proof.* $L^{\diamond}_{\tilde A}L^{\diamond}_{\tilde B}(\tilde X)=L^{\diamond}_{\tilde A}\bigl(\mathrm{Vect}(\tilde B\tilde X^{*})\bigr)=\mathrm{Vect}\bigl(\tilde A\,(\mathrm{Vect}(\tilde B\tilde X^{*}))^{*}\bigr)$; writing $\mathrm{Vect}(\tilde B\tilde X^{*})=\tilde B\tilde X^{*}-H(\tilde B,\tilde X)e_0$, whose star is $\tilde X\tilde B^{*}-\overline{H(\tilde B,\tilde X)}e_0$, gives $\tilde A(\mathrm{Vect}(\tilde B\tilde X^{*}))^{*}=\tilde A\tilde X\tilde B^{*}-\overline{H(\tilde B,\tilde X)}\,\tilde A$, and taking the vector part gives the first display. For the second, $R^{\diamond}_{\tilde A}R^{\diamond}_{\tilde B}(\tilde X)=\mathrm{Vect}\bigl(\mathrm{Vect}(\tilde X\tilde B^{*})\,\tilde A^{*}\bigr)$, and the same substitution gives $\mathrm{Vect}(\tilde X\tilde B^{*}\tilde A^{*})-H(\tilde X,\tilde B)\,\mathrm{Vect}(\tilde A^{*})$; since $\tilde B^{*}\tilde A^{*}=(\tilde A\tilde B)^{*}$, this is the second display. The linearity is the parity of the product of two conjugate-linear maps. $\square$

**Remark (the mixed composites).** The two mixed orders carry the same correction. For the left-then-right order,
$L^{\diamond}_{\tilde A}R^{\diamond}_{\tilde B}(\tilde X)=\mathrm{Vect}\bigl(\tilde A\tilde B\tilde X^{*}\bigr)-\overline{H(\tilde X,\tilde B)}\,\mathrm{Vect}(\tilde A)$, and for the right-then-left order $R^{\diamond}_{\tilde A}L^{\diamond}_{\tilde B}(\tilde X)=\mathrm{Vect}\bigl(\mathrm{Vect}(\tilde B\tilde X^{*})\,\tilde A^{*}\bigr)$: the projection inside the composite is the obstruction, and the composite is an operator of the block only in the degenerate cases.

**Corollary (the failure of multiplicativity).** The assignment $\tilde A\mapsto L^{\diamond}_{\tilde A}$ is conjugate-linear, $\lambda\tilde A$ giving $\overline{\lambda}$ times the operator, and it is **not** multiplicative:
$L^{\diamond}_{\tilde A}L^{\diamond}_{\tilde B}\neq L^{\diamond}_{\tilde A\diamond\tilde B}$, and likewise for the right family. The witness is $\tilde A=\tilde B=e_1$, $\tilde X=e_2$: the composite sends $e_2$ to $-e_2$, since $L^{\diamond}_{e_1}(e_2)=-e_3$ and $L^{\diamond}_{e_1}(-e_3)=-e_2$, while $L^{\diamond}_{e_1\diamond e_1}=L^{\diamond}_{0}=0$. The operators of the block therefore do **not** form a monoid under composition, and the block has no regular representation: the failure is stronger than the failure of a single linear representation, it is the failure of a multiplicative one.

**Remark (the contrast with the row).** For the general plain sesqualgebra the two composites close: there $L_{\tilde A}L_{\tilde B}=T_{\tilde A,\tilde B^{*}}$ is the ordinary two-sided multiplication and $R_{\tilde A}R_{\tilde B}=R_{\tilde A\tilde B}$, by *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, §*The Mixed Composites*. The block is the projection $\mathrm{Vect}$ of each of those operators, and the projection intervenes twice, so the composition acquires the correction terms $-\overline{H(\tilde B,\tilde X)}\,\mathrm{Vect}(\tilde A)$ and $-H(\tilde X,\tilde B)\,\mathrm{Vect}(\tilde A^{*})$; the projection is not an algebra map of the row, and that is what destroys the multiplicativity.

**Corollary (the companion composes into the right family).** Since $T_{\tilde A}=-R^{\diamond}_{\tilde A}$ and $R^{\diamond}_{\tilde A}R^{\diamond}_{\tilde B}$ is the composition of the two right operators, the companions compose as
$T_{\tilde A}T_{\tilde B}=R^{\diamond}_{\tilde A}R^{\diamond}_{\tilde B}$, so the $\mathbb{C}$-linear companion family composes into the right family and not into itself, and the companion is not multiplicative either.

## The Derivations

**Definition.** A **derivation** of the block is an $\mathbb{R}$-linear operator $D$ of $\mathbb{B}$ satisfying the Leibniz rule

$$
D(\tilde P\diamond\tilde Q)=D(\tilde P)\diamond\tilde Q+\tilde P\diamond D(\tilde Q)
$$

for all $\tilde P,\tilde Q$; the derivations form a Lie algebra under the commutator, the derivation algebra of the block, by *Derivations of a Sesqualgebra*.

**Theorem (the derivation algebra).** For a real vector $\mathbf a=\sum_k a_ke_k$ define

$$
D_{\mathbf a}(\tilde X)=[0,\ \mathbf a\times\tilde{\mathbf X}],
$$

the cross product of $\mathbf a$ with the vector part, a $\mathbb{C}$-linear operator annihilating the centre. Then $D_{\mathbf a}$ is a derivation of the block exactly when $\mathbf a$ is **real**, and the derivations so obtained form a three-dimensional real space with basis $D_{e_1},D_{e_2},D_{e_3}$, closed under the commutator,

$$
[D_{\mathbf a},D_{\mathbf b}]=D_{\mathbf a\times\mathbf b},
$$

so that the derivation algebra of the block is isomorphic to $\mathbb{R}^{3}$ with the cross product, and it is exactly this space. A derivation $D_{\mathbf a}$ with a non-real $\mathbf a$ fails the Leibniz rule, and a scalar derivation $\tilde X\mapsto\lambda\tilde X$ satisfies it only for $\lambda=0$; the three displayed derivations therefore exhaust the algebra.

*Proof.* The Leibniz defect of $D_{\mathbf a}$ is the computation of $\mathbf a\times(\tilde{\mathbf P}\diamond\tilde{\mathbf Q})$ against $(\mathbf a\times\tilde{\mathbf P})\diamond\tilde{\mathbf Q}+\tilde{\mathbf P}\diamond(\mathbf a\times\tilde{\mathbf Q})$; the two cross products in the three terms combine by the Jacobi identity of the cross product exactly when $\mathbf a$ is fixed by the conjugation, and the terms carrying $\overline{\mathbf a}$ in the sesquilinear slots cancel only then; the bracket is the vector triple identity $[D_{\mathbf a},D_{\mathbf b}](\tilde X)=\mathbf a\times(\mathbf b\times\tilde{\mathbf X})-\mathbf b\times(\mathbf a\times\tilde{\mathbf X})=(\mathbf a\times\mathbf b)\times\tilde{\mathbf X}$. The dimension three is the dimension of the space of the real vectors $\mathbf a$, the operators $D_{e_1},D_{e_2},D_{e_3}$ being independent on the vector coordinates. $\square$

**Remark (the derivations act by the cross product).** The operator $D_{\mathbf a}$ acts on the complex vector subspace by the cross product with $\mathbf a$, which is the infinitesimal form of the transformations of the vector coordinates preserving the cross product; on the real vectors $D_{\mathbf a}(\mathbf X)=\mathbf a\times\mathbf X$ is the derivation of the cross product, and the derivation algebra $\mathbb{R}^{3}$ is the infinitesimal form of the group of the transformations of the real vector triple preserving the cross product and the dot product, of determinant one. The central direction is dead: $D_{\mathbf a}$ annihilates the centre for every $\mathbf a$, and the central component of an operator never enters the Leibniz rule, since the block reads the centre only through the vector part.

## The Structure Group

**Definition.** The **structure group** of the block is the group of the invertible $\mathbb{R}$-linear maps $T$ of $\mathbb{B}$ satisfying

$$
T(\tilde P\diamond\tilde Q)=T(\tilde P)\diamond T(\tilde Q)
$$

for all $\tilde P,\tilde Q$; its identity component has Lie algebra the derivation algebra above, by the differentiation of the defining equation at the identity, *Derivations of a Sesqualgebra*, §*The Lie Algebra of Derivations*.

**Theorem (the two kinds of elements).** The structure group contains the following.

1. The **coefficientwise conjugation** $\overline{\cdot}$: it is an automorphism of the block, $\overline{\tilde P\diamond\tilde Q}=\overline{\tilde P}\diamond\overline{\tilde Q}$, and it is **conjugate-linear**, so the structure group is not confined to the linear maps.
2. The **complex linear extensions of the real transformations preserving the cross product**: for a real $3\times3$ matrix $R$ with $R^{\mathsf T}R=I$ and $\det R=1$, the map $T_R$ fixing the centre and acting on the complex vector subspace by $R$ in its two real components,
   $$
   T_R(Q_0e_0+\mathbf U+i\mathbf V)=Q_0e_0+R\mathbf U+iR\mathbf V,
   $$
   is a $\mathbb{C}$-linear automorphism of the block.

The **natural conjugation** $^{\natural}$ is **not** an automorphism of the block: it fails $T(\tilde P\diamond\tilde Q)=T(\tilde P)\diamond T(\tilde Q)$ on a general pair.

*Proof.* The first statement is the proposition of *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions*, §*Conjugate-Alternation*. For the second, $T_R$ preserves the complex bilinear dot and cross products of the vector parts, since $R$ preserves the dot and the cross products of the real vectors, $R^{\mathsf T}R=I$ and $\det R=1$; the block is built from the dot and the cross of the vector parts through the sesquilinear slots, so $T_R(\tilde P\diamond\tilde Q)=T_R(\tilde P)\diamond T_R(\tilde Q)$. For the third, the natural conjugation negates the vector part and fixes the scalar part, so it reverses the cross term of the block; the witness $(\tilde P,\tilde Q)=(e_1,e_2)$ gives $^{\natural}(e_1\diamond e_2)={}^{\natural}(-e_3)=e_3$ on the left against $^{\natural}e_1\diamond{}^{\natural}e_2=(-e_1)\diamond(-e_2)=e_1\diamond e_2=-e_3$ on the right. $\square$

**Remark (the group and its Lie algebra).** The transformations $T_R$ form a group isomorphic to the group of the transformations of the real vector triple preserving the cross product and the dot product, of determinant one, acting on the complex vector subspace by the same real matrix in both real components, and its Lie algebra is the three-dimensional algebra with basis the three derivations $D_{e_1},D_{e_2},D_{e_3}$ of the preceding section; the coefficientwise conjugation supplies the second component, conjugate-linear, which inverts with the complex-linear one to a linear automorphism when composed with a sign on the vector part. The structure group is therefore the semidirect product of the linear transformations of that group and the order-two conjugation, and its Lie algebra is the three-dimensional cross-product algebra of the derivations. The group of the transformations preserving the **form** $H$ alone is larger, the group of *Units and the Unitary Elements*; the structure group of the block is the subgroup cut out by the preservation of the product.

## Summary

The left multiplication of the block is the conjugate-linear operator $L^{\diamond}_{\tilde A}=\mathrm{Vect}\circ S_{\tilde A,e_0}$, the vector part of the left multiplication of the row; the right multiplication is its conjugate, $R^{\diamond}_{\tilde A}=-\overline{L^{\diamond}_{\tilde A}}$, so a single $\mathbb{C}$-linear companion $T_{\tilde A}=\overline{L^{\diamond}_{\tilde A}}=-R^{\diamond}_{\tilde A}$ carries the whole operator theory. In the real basis the matrix has its two scalar rows zero and its trace zero; it has rank six for a unit and four for a zero divisor, the kernel being the set of the $\tilde X$ with $\tilde A\tilde X^{*}$ central, which is the centre for $\tilde A=e_0$ and the line $\mathbb{C}e_k$ for $\tilde A=e_k$. The characteristic polynomial of the matrix $M_{\tilde A}$ is even, $\lambda^{2}P(\lambda)$, with $P$ even of degree six: $\lambda^{2}(\lambda^{2}-1)^{3}$ at the unit, $\lambda^{4}(\lambda^{2}+1)^{2}$ at the basis vectors, and $\lambda^{4}(\lambda^{2}+2)^{2}$ at the zero divisor $e_1+ie_2$. The adjoint with respect to $H$ is the right multiplication of the star of the vector part, $(L^{\diamond}_{\tilde A})^{\dagger}(\tilde Y)=(\mathrm{Vect}\tilde Y)^{*}\tilde A$, a conjugate-linear operator with scalar part $H(\mathbf A,\mathbf Y)$; the operator is the first factor of the two-parameter sandwich, whose vector part is $L^{\diamond}_{\tilde A}(\tilde X)\tilde B^{*}+H(\tilde A,\tilde X)\tilde B^{*}$. The derivations are the cross products $D_{\mathbf a}(\tilde X)=[0,\mathbf a\times\tilde{\mathbf X}]$ with $\mathbf a$ real, a three-dimensional Lie algebra isomorphic to $\mathbb{R}^{3}$ with the cross product; the structure group contains the coefficientwise conjugation (conjugate-linear) and the complex-linear extensions of the real transformations preserving the cross product of the vector triple, of determinant one, with Lie algebra the derivation algebra, and it does not contain the natural conjugation. The two one-sided operators do not compose, $L^{\diamond}_{\tilde A}L^{\diamond}_{\tilde B}(\tilde X)=\mathrm{Vect}(\tilde A\tilde X\tilde B^{*})-\overline{H(\tilde B,\tilde X)}\,\mathrm{Vect}(\tilde A)$ while $L^{\diamond}_{e_1}L^{\diamond}_{e_1}(e_2)=-e_2$ against $L^{\diamond}_{e_1\diamond e_1}=0$, so the block has no monoid of operators and no regular representation; the companion family composes into the right family, $T_{\tilde A}T_{\tilde B}=R^{\diamond}_{\tilde A}R^{\diamond}_{\tilde B}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L^{\diamond}_{\tilde A}(\tilde X)=\tilde A\diamond\tilde X$ | the conjugate-linear left multiplication of the block |
| $R^{\diamond}_{\tilde A}(\tilde X)=\tilde X\diamond\tilde A=-\overline{L^{\diamond}_{\tilde A}}$ | the right multiplication, minus the companion |
| $T_{\tilde A}=\overline{L^{\diamond}_{\tilde A}}$ | the $\mathbb{C}$-linear companion, the honest linear object |
| $(\mathcal B)=(e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3)$ | the real basis in which the matrices are read |
| $L^{\diamond}_{\tilde A}=\mathrm{Vect}\circ S_{\tilde A,e_0}$ | the operator inside the sesquilinear sandwich |
| $M_{e_0}=\operatorname{diag}(0,-1,-1,-1,0,1,1,1)$ | the matrix of the unit, trace zero, rank six |
| $\chi_{M_{\tilde A}}=\lambda^{2}P(\lambda)$ | the characteristic polynomial of the real matrix of $L^{\diamond}_{\tilde A}$, even, $P$ even of degree six |
| $(L^{\diamond}_{\tilde A})^{\dagger}(\tilde Y)=(\mathrm{Vect}\tilde Y)^{*}\tilde A$ | the adjoint under the twisted rule |
| $D_{\mathbf a}(\tilde X)=[0,\mathbf a\times\tilde{\mathbf X}]$ | the derivation by a real vector, the algebra $\mathbb{R}^{3}$ with the cross product |
| $T_R$ | the complex-linear automorphism from a real $R$ with $R^{\mathsf T}R=I$, $\det R=1$ |

## Further Reading

- *Introduction to the Antisymmetric Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-sesqualgebra-of-biquaternions.md`), for the operation, the conjugate-alternation and the coefficientwise automorphism
- *The Left and Right Multiplications of the Biquaternion Sesqualgebra* (`articles_maths/the-left-and-right-multiplications-of-the-biquaternion-sesqualgebra.md`), for the one-sided multiplications of the row and the obstruction to a single linear representation
- *The Sesquilinear Sandwich on the Biquaternions* (`articles_maths/the-sesquilinear-sandwich-on-the-biquaternions.md`) and *The Adjoint of the Sesquilinear Sandwich on the Biquaternions* (`articles_maths/the-adjoint-of-the-sesquilinear-sandwich-on-the-biquaternions.md`), for the sandwich, the twisted adjoint rule and the adjoints of the one-sided operators
- *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra* (`articles_maths/the-sesquilinear-pairing-of-the-antisymmetric-plain-sesqualgebra.md`), for the form, the Gram data and the sandwich relation of the block
- *Derivations of a Sesqualgebra* (`articles_maths/derivations-of-a-sesqualgebra.md`), for the derivation algebra, the group of the automorphisms and its Lie algebra
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the units, the zero divisors and the form $H$
- *Units and the Unitary Elements* (`articles_maths/units-and-the-unitary-elements.md`), for the group preserving the form, larger than the structure group of the block
- *The Antisymmetric Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-antisymmetric-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the operator and its invariants in the realization
- *The Antisymmetric Plain Sesqualgebra in the $4\times4$ Matrix Element Representation $M_4(\mathbb{C})_L$* (`articles_maths/the-antisymmetric-plain-sesqualgebra-in-the-4x4-matrix-element-representation.md`), for the operator and its invariants in the regular model
