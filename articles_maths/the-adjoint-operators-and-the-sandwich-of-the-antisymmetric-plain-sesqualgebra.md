# __The Adjoint Operators and the Sandwich of the Antisymmetric Plain Sesqualgebra__

## Introduction

The operation of the block, $\tilde Q_1\diamond\tilde Q_2=\mathrm{Vect}(\tilde Q_1\tilde Q_2^{*})$, is conjugate-linear in its second slot, so its **left multiplication** $\tilde Q_1\mapsto\tilde Q_5\diamond\tilde Q_1$ is a conjugate-linear operator and its **right multiplication** $\tilde Q_1\mapsto\tilde Q_1\diamond\tilde Q_5$ is $\mathbb{C}$-linear; the pair $(L^{\diamond}_{\tilde Q_5},R^{\diamond}_{\tilde Q_5})$ is the operator data of the block, and this article computes it. The conjugate linearity is not a defect to be removed, it is the parity that the operation carries, and it forces a **companion**: to every conjugate-linear operator the theory attaches the $\mathbb{C}$-linear operator obtained by conjugating the coefficients of the value, and the companion of the left multiplication of the block is the negative of the right multiplication, $T_{\tilde Q_5}=\overline{L^{\diamond}_{\tilde Q_5}}=-R^{\diamond}_{\tilde Q_5}$, by the conjugate-alternation. The companion is the honest linear object, and the characteristic polynomial that is computed is that of the real matrix of the left multiplication.

Five facts organise the reading. The left operator is the **vector part of a left multiplication of the row**, $L^{\diamond}_{\tilde Q_5}=\mathrm{Vect}\circ S_{\tilde Q_5,e_t}$, so it sits inside the sesquilinear sandwich of *The Sesquilinear Sandwich on the Biquaternion*. Its **trace vanishes** and its **rank is six** for a unit and **four** for a zero divisor, the kernel being the set of the elements whose product with $\tilde Q_5$ on the left is central; for $\tilde Q_5=e_t$ that kernel is the centre, and for $\tilde Q_5=\vec e_\mu$ it is the complex line of $\vec e_\mu$. Its **adjoint** with respect to the form $\langle\cdot,\cdot\rangle_{*}$ is the right multiplication of the star of the vector part, $L^{\diamond\dagger}_{\tilde Q_5}(\tilde Q_2)=(\mathrm{Vect}\tilde Q_2)^{*}\tilde Q_5$, the adjoint of a conjugate-linear operator being conjugate-linear with the twisted rule of *The Adjoint of the Sesquilinear Sandwich on the Biquaternion*. And the **derivations** of the block are exactly the three products $D_{\vec a}(\tilde Q_1)=[0,\vec a\times\vec Q_1]$ with $\vec a$ a **real** vector, a three-dimensional real Lie algebra isomorphic to $\mathbb{R}^{3}$ with the cross product, which is also the Lie algebra of the structure group; the group contains the coefficientwise conjugation and the transformations that act on the complex vector subspace by a real matrix $R$ with $R^{\mathsf T}R=I$ and $\det R=1$, and it does not contain the natural conjugation. And the two one-sided operators of the block **do not compose**: the composite $L^{\diamond}_{\tilde Q_5}L^{\diamond}_{\tilde Q_3}$ is not an operator of the block, and $L^{\diamond}_{\tilde Q_5}L^{\diamond}_{\tilde Q_3}\neq L^{\diamond}_{\tilde Q_5\diamond\tilde Q_3}$ because the projection $\mathrm{Vect}$ intervenes twice, so the block has no monoid of one-sided operators and no regular representation; the composition laws, and the contrast with the row that does compose, are the last reading of the operator theory.

The setting is that of *Introduction to the Antisymmetric Plain Sesqualgebra*; the general theory of the one-sided multiplications and of the obstruction to a single linear representation is *The Left and Right Multiplications of the Biquaternion Sesqualgebra*; the sandwich is *The Sesquilinear Sandwich on the Biquaternion* and its adjoint *The Adjoint of the Sesquilinear Sandwich on the Biquaternion*; the form $\langle\cdot,\cdot\rangle_{*}$ is *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*; the derivations of a sesqualgebra are *Derivations of a Sesqualgebra*; the multiplicative norm $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ and the zero divisors are *Norm and Invertibility in the General Quaternionic Algebra*; the pairing and the sandwich relation of the block are *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*, above in this block; and the matrix models are *Introduction to the Symmetric Plain Sesqualgebra*, below. The rank, the kernel, the trace and the determinant are the algebraic invariants of a linear map.

## The Left and Right Operators

**Definition.** For a fixed biquaternion $\tilde Q_5$ the **left** and the **right multiplications** of the block are the operators

$$
L^{\diamond}_{\tilde Q_5}(\tilde Q_1)=\tilde Q_5\diamond\tilde Q_1=\mathrm{Vect}\bigl(\tilde Q_5\tilde Q_1^{*}\bigr),
\qquad
R^{\diamond}_{\tilde Q_5}(\tilde Q_1)=\tilde Q_1\diamond\tilde Q_5=\mathrm{Vect}\bigl(\tilde Q_1\tilde Q_5^{*}\bigr),
$$

the left conjugate-linear and the right $\mathbb{C}$-linear, the operation being $\mathbb{C}$-linear in its first slot and conjugate-linear in the second.

**Proposition (the vector part of the row multiplication).** For every $\tilde Q_5$,

$$
L^{\diamond}_{\tilde Q_5}=\mathrm{Vect}\circ L_{\tilde Q_5},
\qquad
R^{\diamond}_{\tilde Q_5}=\mathrm{Vect}\circ R_{\tilde Q_5},
$$

where $L_{\tilde Q_5}(\tilde Q_1)=\tilde Q_5\tilde Q_1^{*}$ and $R_{\tilde Q_5}(\tilde Q_1)=\tilde Q_1\tilde Q_5^{*}$ are the two one-sided multiplications of the general plain sesqualgebra of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*.

*Proof.* The identity $\mathrm{Vect}(\tilde Q_2)=\tilde Q_2-\mathrm{Sc}(\tilde Q_2)e_t$ and the definitions.

**Theorem (the companion and the conjugate-alternation).** The operators satisfy

$$
R^{\diamond}_{\tilde Q_5}=-\overline{L^{\diamond}_{\tilde Q_5}},
\qquad
\text{equivalently}\qquad
T_{\tilde Q_5}:=\overline{L^{\diamond}_{\tilde Q_5}}=-R^{\diamond}_{\tilde Q_5},
$$

where the bar is the coefficientwise conjugation of the value. The **companion** $T_{\tilde Q_5}$ is $\mathbb{C}$-**linear**, and the left operator is its conjugate, $L^{\diamond}_{\tilde Q_5}=\overline{T_{\tilde Q_5}}$.

*Proof.* The conjugate-alternation gives $\tilde Q_1\diamond\tilde Q_5=-\overline{\tilde Q_5\diamond\tilde Q_1}=-\overline{L^{\diamond}_{\tilde Q_5}(\tilde Q_1)}$, which is the first display; the coefficientwise conjugation of a conjugate-linear operator is $\mathbb{C}$-linear, since the conjugation is conjugate-linear and the operator is conjugate-linear.

**Remark (a single linear representation is enough).** Because the right operator is the negative of the companion of the left, the whole operator theory of the block is the theory of the single $\mathbb{C}$-**linear** companion $T_{\tilde Q_5}=\overline{L^{\diamond}_{\tilde Q_5}}$, with the left and the right recovered from it. This is the good case of *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, §*The Obstruction to a Single Linear Representation*: for the associative product of the row the two one-sided multiplications have opposite parities and no single linear representation carries both, whereas here the parity of the block is carried by the operation itself, and the companion is linear for free.

## The Matrix in the Real Basis

**The basis.** The operator is read in the **real basis** $(\mathcal B)=(e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z)$ of $\mathbb{B}$ as an $\mathbb{R}$-vector space, on which an $\mathbb{R}$-linear or conjugate-linear operator has a real $8\times8$ matrix. Write $\tilde Q_5=A_te_t+\vec A$ with $A_t=a+ib$ and $\vec A=\vec q+i\vec v$, and $\tilde Q_1=Q_{1t}e_t+\vec Q_1$ with $Q_{1t}=x+iy$ and $\vec Q_1=\vec U+i\vec V$, all of $a,b,x,y$ real and $\vec q,\vec v,\vec U,\vec V$ real vectors.

**Theorem (the coordinate rule).** The left operator reads

$$
L^{\diamond}_{\tilde Q_5}(\tilde Q_1)=
\bigl(x\,\vec q+y\,\vec v-a\,\vec U-b\,\vec V-\vec q\times\vec U-\vec v\times\vec V\bigr)
+i\bigl(x\,\vec v-y\,\vec q-b\,\vec U+a\,\vec V+\vec q\times\vec V-\vec v\times\vec U\bigr),
$$

a pure vector, so the two scalar coordinates $(e_t,ie_t)$ of the value vanish identically and the matrix has its two scalar rows zero. On the real basis elements,

$$
L^{\diamond}_{\tilde Q_5}(e_t)=\vec A,\quad
L^{\diamond}_{\tilde Q_5}(ie_t)=-i\,\vec A,\quad
L^{\diamond}_{\tilde Q_5}(\vec e_\mu)=-a\,\vec e_\mu-\vec q\times \vec e_\mu+i\bigl(-b\,\vec e_\mu-\vec v\times \vec e_\mu\bigr),\quad
L^{\diamond}_{\tilde Q_5}(i\vec e_\mu)=L^{\diamond}_{\tilde Q_5}(\vec e_\mu)\text{ conjugated},
$$

whose last identity is the $\mathbb{C}$-semilinearity, $L^{\diamond}_{\tilde Q_5}(i\tilde Q_1)=-i\,L^{\diamond}_{\tilde Q_5}(\tilde Q_1)$.

*Proof.* The coordinate rule is the substitution $\tilde Q_5\tilde Q_1^{*}=(A_t+\vec A)\bigl(\overline{Q_{1t}}-\overline{\vec Q_1}\bigr)$ with the scalar–vector multiplication of the row, collecting the real and the imaginary parts of the vector part; the value is a vector part by the definition of the block, so the scalar coordinate vanishes.

**Corollary (the matrix of the unit).** At $\tilde Q_5=e_t$ the coordinate rule is $L^{\diamond}_{e_t}(\tilde Q_1)=-\overline{\vec Q_1}$, and the matrix is diagonal,

$$
M_{e_t}=\operatorname{diag}\bigl(0,-1,-1,-1,\,0,\,1,\,1,\,1\bigr),
$$

with the two scalar entries zero (the scalar coordinates $e_t$ and $ie_t$ are not reached) and the last six the negative of the real part and the identity on the imaginary part of the vector coordinates. The matrix of $L^{\diamond}_{e_t}$ is therefore involutive up to sign, $M_{e_t}^{2}=\operatorname{diag}(0,1,1,1,0,1,1,1)$, the projection onto the vector coordinates.

**Remark (the matrix of $ie_t$).** At $\tilde Q_5=ie_t$ the coordinate rule gives $L^{\diamond}_{ie_t}(\tilde Q_1)=\mathrm{Vect}(i\tilde Q_1^{*})=i\,L^{\diamond}_{e_t}(\tilde Q_1)$, so $M_{ie_t}$ is $M_{e_t}$ composed with the complex structure of the vector coordinates; the two matrices have the same characteristic polynomial, as the next section computes.

## The Kernel, the Rank and the Characteristic Polynomial

**Theorem (the kernel).** For a nonzero $\tilde Q_5$,

$$
\ker L^{\diamond}_{\tilde Q_5}=\bigl\{\tilde Q_1:\ \tilde Q_5\tilde Q_1^{*}\in\mathbb{C}_{\mathbb{B}}\bigr\},
$$

the set of the elements whose left product with $\tilde Q_5$ is central. In particular $\ker L^{\diamond}_{e_t}=\mathbb{C}_{\mathbb{B}}$, the centre, of real dimension two; and $\ker L^{\diamond}_{\vec e_\mu}=\mathbb{C}\,\vec e_\mu$, the complex line of $\vec e_\mu$, of real dimension two.

*Proof.* $L^{\diamond}_{\tilde Q_5}(\tilde Q_1)=0$ is the vanishing of the vector part of $\tilde Q_5\tilde Q_1^{*}$, which is the centrality of $\tilde Q_5\tilde Q_1^{*}$. At $\tilde Q_5=e_t$ the centrality of $\tilde Q_1^{*}$ is the centrality of $\tilde Q_1$, which is the centre. At $\tilde Q_5=\vec e_\mu$, the product $\vec e_\mu\tilde Q_1^{*}$ central forces $\tilde Q_1^{*}\in\mathbb{C}\vec e_\mu$, that is $\tilde Q_1\in\mathbb{C}\vec e_\mu$.

**Theorem (the rank and the trace).** The trace of $L^{\diamond}_{\tilde Q_5}$ vanishes for every $\tilde Q_5$, and

$$
\mathrm{rank}\,L^{\diamond}_{\tilde Q_5}=6\ \text{ if } \tilde Q_5 \text{ is a unit},\qquad
\mathrm{rank}\,L^{\diamond}_{\tilde Q_5}=4\ \text{ if } \tilde Q_5 \text{ is a zero divisor},
$$

the rank being read over $\mathbb{R}$ on the eight-dimensional real space.

*Proof.* The diagonal of $M_{\tilde Q_5}$: from the coordinate rule the real part of the vector coordinate $U_\mu$ contributes $a$ with a sign and the imaginary part $V_\mu$ contributes $a$ with the opposite sign in the diagonal, so the trace is $-3a+3a=0$; equivalently the trace of $M_{e_t}$ and of $M_{\vec e_\mu}$ are zero by the corollaries above, and $M_{\tilde Q_5}$ is a complex-linear combination of them. For the rank, $\tilde Q_5$ is a unit exactly when its multiplicative norm $\langle\tilde Q_5\rangle_{\natural}=\tilde Q_5\tilde Q_5^{\natural}$ is nonzero, by *Norm and Invertibility in the General Quaternionic Algebra*, and then $L_{\tilde Q_5}$ is injective on the values and the kernel is the two-dimensional one above, giving rank six; for a zero divisor the kernel grows.

**Theorem (the characteristic polynomial).** The real matrix $M_{\tilde Q_5}$ of $L^{\diamond}_{\tilde Q_5}$ in the real basis has an even characteristic polynomial, of the form

$$
\chi_{M_{\tilde Q_5}}(\lambda)=\lambda^{2}\,P(\lambda),
$$

with $P$ an even polynomial of degree six. On the basis,

$$
\chi_{M_{e_t}}=\lambda^{2}(\lambda^{2}-1)^{3},\qquad
\chi_{M_{\vec e_\mu}}=\lambda^{4}(\lambda^{2}+1)^{2}\ (\mu=x,y,z),\qquad
\chi_{M_{\vec e_x+i\vec e_y}}=\lambda^{4}(\lambda^{2}+2)^{2}.
$$

*Proof.* The matrix $M_{\tilde Q_5}$ is real and exchanges the two complex structures of the vector coordinates, so its characteristic polynomial is even in $\lambda^{2}$ on the six vector coordinates; the two scalar coordinates are annihilated, which gives the factor $\lambda^{2}$. The three displayed polynomials are the characteristic polynomials of the displayed matrices, computed on the real basis.

**Remark (the zero eigenvalue and the rank).** The factor $\lambda^{2}$ at the unit is the annihilation of the two scalar coordinates, and the kernel of $L^{\diamond}_{e_t}$ is the centre, of real dimension two. At a basis vector $\vec e_\mu$ the factor is $\lambda^{4}$ while the kernel is still the complex line $\mathbb{C}\vec e_\mu$, of real dimension two, so the operator is not semisimple there; at the zero divisor $\vec e_x+i\vec e_y$ the factor $\lambda^{4}$ is the four-dimensional kernel. It is the dimension of the kernel, and not the multiplicity of the zero eigenvalue, that fixes the rank, six on the units and four on the zero divisor; the eigenvalues of $M_{\tilde Q_5}$ are the zero of multiplicity two at the unit and four off it, together with three pairs $\pm$: $\pm1$ thrice at $e_t$, $\pm i$ twice at the basis vectors, and $\pm i\sqrt2$ twice at the zero divisor.

## The Adjoint and the Companion

**Definition.** With the Hermitian form $\varphi=H$ of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, the **adjoint** of a conjugate-linear operator $S$ is the conjugate-linear operator $S^{\dagger}$ defined by

$$
\varphi(S\tilde Q_1,\tilde Q_2)=\overline{\varphi(\tilde Q_1,S^{\dagger}\tilde Q_2)},
$$

the twisted rule of *The Adjoint of the Sesquilinear Sandwich on the Biquaternion*, §*The Twisted Adjoint Rule*.

**Theorem (the adjoint of the left operator).** For every $\tilde Q_5$,

$$
\bigl(L^{\diamond}_{\tilde Q_5}\bigr)^{\dagger}(\tilde Q_2)=\bigl(\mathrm{Vect}(\tilde Q_2)\bigr)^{*}\,\tilde Q_5 ,
$$

the conjugate-linear **right multiplication by $\tilde Q_5$ of the star of the vector part**. In coordinates, with $\tilde Q_2=Q_{2t}e_t+\vec Q_2$ and $A_t=a+ib$, $\vec A=\vec q+i\vec v$,

$$
\bigl(L^{\diamond}_{\tilde Q_5}\bigr)^{\dagger}(\tilde Q_2)
=\bigl(\vec A,\overline{\vec Q_2}\bigr)e_t
-a\,\overline{\vec Q_2}+\vec q\times\overline{\vec Q_2}+i\bigl(-b\,\overline{\vec Q_2}+\vec v\times\overline{\vec Q_2}\bigr),
$$

whose scalar part is the form $\langle \vec A,\vec Q_2\rangle_{*}$ of the two vector parts and whose vector part is the displayed one.

*Proof.* The projection $\mathrm{Vect}$ is self-adjoint for the form, $\varphi(\mathrm{Vect}\tilde Q_1,\tilde Q_2)=\varphi(\mathrm{Vect}\tilde Q_1,\mathrm{Vect}\tilde Q_2)=\varphi(\tilde Q_1,\mathrm{Vect}\tilde Q_2)$, because the form depends on a pure vector only through the vector part. The adjoint of the left multiplication $L_{\tilde Q_5}(\tilde Q_1)=\tilde Q_5\tilde Q_1^{*}$ of the row is the right multiplication by $\tilde Q_5$, $L_{\tilde Q_5}^{\dagger}(\tilde Q_2)=\tilde Q_2^{*}\tilde Q_5$, by *The Adjoint of the Sesquilinear Sandwich on the Biquaternion*, §*The Special Cases*, since $L_{\tilde Q_5}=S_{\tilde Q_5,e_t}$ and $S_{\tilde Q_1,\tilde Q_2}^{\dagger}=S_{\tilde Q_2^{*},\tilde Q_1^{*}}=S_{e_t,\tilde Q_5^{*}}$ reads $\tilde Q_2^{*}\tilde Q_5$. Therefore $(L^{\diamond}_{\tilde Q_5})^{\dagger}(\tilde Q_2)=(\mathrm{Vect}\tilde Q_2)^{*}\tilde Q_5$, and the coordinate form is its scalar–vector expansion.

**Corollary (the companion adjoint).** The companion $T_{\tilde Q_5}=\overline{L^{\diamond}_{\tilde Q_5}}$ is $\mathbb{C}$-linear, so its adjoint is read by the linear rule of the twisted adjoint rule, and it is the $\mathbb{C}$-linear operator

$$
T_{\tilde Q_5}^{\dagger}(\tilde Q_2)=\bigl(\mathrm{Vect}(\overline{\tilde Q_2})\bigr)^{*}\,\tilde Q_5 ,
$$

with the involution property $T_{\tilde Q_5}^{\dagger\dagger}=T_{\tilde Q_5}$. The right operator is the negative of the companion, $R^{\diamond}_{\tilde Q_5}=-T_{\tilde Q_5}$, and the adjoint is $\mathbb{C}$-linear in the operator under the linear rule, so

$$
R^{\diamond\dagger}_{\tilde Q_5}=-T_{\tilde Q_5}^{\dagger}.
$$

*Proof.* The companion is linear, so its adjoint is defined by the linear rule $\langle T_{\tilde Q_5}\tilde Q_1,\tilde Q_2\rangle_{*}=\langle\tilde Q_1,T_{\tilde Q_5}^{\dagger}\tilde Q_2\rangle_{*}$. Using $\langle\overline{\tilde Q_4},\tilde Q_2\rangle_{*}=\overline{\langle\tilde Q_4,\overline{\tilde Q_2}\rangle_{*}}$ and the twisted adjoint of the left operator, $\langle L^{\diamond}_{\tilde Q_5}\tilde Q_1,\overline{\tilde Q_2}\rangle_{*}=\overline{\langle\tilde Q_1,(\mathrm{Vect}\overline{\tilde Q_2})^{*}\tilde Q_5\rangle_{*}}$, so the two conjugations cancel and $T_{\tilde Q_5}^{\dagger}\tilde Q_2=(\mathrm{Vect}\overline{\tilde Q_2})^{*}\tilde Q_5$; the involution is the general involution of the adjoint on the linear parity. The right operator satisfies $R^{\diamond}_{\tilde Q_5}=-T_{\tilde Q_5}$ by the companion theorem, and the linear rule is $\mathbb{C}$-linear in the operator, so the second display follows.

**Corollary (the self-adjoint operators).** The left operator is self-adjoint, $L^{\diamond\dagger}_{\tilde Q_5}=L^{\diamond}_{\tilde Q_5}$, exactly when $\tilde Q_5$ is **central**, $\tilde Q_5=\lambda e_t$ with $\lambda\in\mathbb{C}$; on the central elements the two sides coincide, and off them they differ.

*Proof.* By the theorem the adjoint is $\tilde Q_2\mapsto(\mathrm{Vect}\tilde Q_2)^{*}\tilde Q_5$, and self-adjointness reads $(\mathrm{Vect}\tilde Q_2)^{*}\tilde Q_5=\mathrm{Vect}(\tilde Q_5\tilde Q_2^{*})$ for all $\tilde Q_2$. At $\tilde Q_5=\lambda e_t$ both sides are $-\overline{\lambda}\,\overline{\vec Q_2}$ and the identity holds. For $\tilde Q_5=\vec e_\mu$ the left side is $(\mathrm{Vect}\tilde Q_2)^{*}\vec e_\mu$ and the right side $\mathrm{Vect}(\vec e_\mu\tilde Q_2^{*})$; the witness $\tilde Q_2=e_t$ gives $0$ on the left and $\vec e_\mu$ on the right, so the identity fails, and the general element has a non-central part with the same witness.

## The Sandwich

**Theorem (the operator inside the sandwich).** For every $\tilde Q_5$,

$$
L^{\diamond}_{\tilde Q_5}=\mathrm{Vect}\circ S_{\tilde Q_5,e_t},
$$

with $S_{\tilde Q_5,e_t}(\tilde Q_1)=\tilde Q_5\tilde Q_1^{*}$ the sesquilinear sandwich of *The Sesquilinear Sandwich on the Biquaternion* with second parameter the unit; and more generally, for the full sandwich $S_{\tilde Q_5,\tilde Q_3}(\tilde Q_1)=\tilde Q_5\tilde Q_1^{*}\tilde Q_3^{*}$,

$$
S_{\tilde Q_5,\tilde Q_3}=R_{\tilde Q_3}\circ S_{\tilde Q_5,e_t},
\qquad
\mathrm{Vect}\circ S_{\tilde Q_5,\tilde Q_3}=R_{\tilde Q_3}\circ L^{\diamond}_{\tilde Q_5}.
$$

*Proof.* The first display is the proposition of §*The Left and Right Operators* with the identification $S_{\tilde Q_5,e_t}=L_{\tilde Q_5}$; the second factors the second parameter and applies $\mathrm{Vect}$.

**Corollary (the factorisation of the two-parameter sandwich).** For all $\tilde Q_5,\tilde Q_3,\tilde Q_1$,

$$
S_{\tilde Q_5,\tilde Q_3}(\tilde Q_1)=\tilde Q_5\tilde Q_1^{*}\tilde Q_3^{*}=L^{\diamond}_{\tilde Q_5}(\tilde Q_1)\,\tilde Q_3^{*}+\langle\tilde Q_5,\tilde Q_1\rangle_{*}\,\tilde Q_3^{*},
$$

the sum of the vector part of $\tilde Q_5\tilde Q_1^{*}$ multiplied by $\tilde Q_3^{*}$ and the scalar part $\langle\tilde Q_5,\tilde Q_1\rangle_{*}$ multiplied by $\tilde Q_3^{*}$, and its vector part is

$$
\mathrm{Vect}\bigl(\tilde Q_5\tilde Q_1^{*}\tilde Q_3^{*}\bigr)=\mathrm{Vect}\bigl(L^{\diamond}_{\tilde Q_5}(\tilde Q_1)\,\tilde Q_3^{*}\bigr)-\langle\tilde Q_5,\tilde Q_1\rangle_{*}\,\overline{\vec Q_3}.
$$

The sandwich therefore carries the block in the first factor of its vector part and the form $\langle\cdot,\cdot\rangle_{*}$ in the scalar correction, which is the operator form of the split of the row: the two halves $\mathrm{SPS}$ and $\diamond$ of the product appear as the scalar part and the vector part of $\tilde Q_5\tilde Q_1^{*}$, as in *The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra*, §*The Compatibility with the Sandwich*.

**Remark (the parities).** The sandwich $S_{\tilde Q_1,\tilde Q_2}$ is conjugate-linear, the left operator $L^{\diamond}_{\tilde Q_5}$ is conjugate-linear, the right multiplication $R_{\tilde Q_3}$ of the row is $\mathbb{C}$-linear; the composites $S_{\tilde Q_5,\tilde Q_3}=R_{\tilde Q_3}\circ S_{\tilde Q_5,e_t}$ and $R_{\tilde Q_3}\circ L^{\diamond}_{\tilde Q_5}$ are therefore conjugate-linear too, the product of one factor of each parity, and the companion of the composite is the composite of the companions. The block is one factor of the ternary product of the row seen through its vector part, and the adjoint of *The Adjoint of the Sesquilinear Sandwich on the Biquaternion* applies to the other factor.

## The Composition of Two Operators

**Theorem (the composition laws).** For all biquaternions $\tilde Q_5,\tilde Q_3,\tilde Q_1$,

$$
L^{\diamond}_{\tilde Q_5}L^{\diamond}_{\tilde Q_3}(\tilde Q_1)
=\mathrm{Vect}\bigl(\tilde Q_5\tilde Q_1\tilde Q_3^{*}\bigr)-\overline{\langle\tilde Q_3,\tilde Q_1\rangle_{*}}\,\mathrm{Vect}(\tilde Q_5),
$$

$$
R^{\diamond}_{\tilde Q_5}R^{\diamond}_{\tilde Q_3}(\tilde Q_1)
=\mathrm{Vect}\bigl(\tilde Q_1(\tilde Q_5\tilde Q_3)^{*}\bigr)-\langle\tilde Q_1,\tilde Q_3\rangle_{*}\,\mathrm{Vect}(\tilde Q_5^{*}),
$$

and the two composites are $\mathbb{C}$-**linear**, the product of two conjugate-linear operators being linear.

*Proof.* $L^{\diamond}_{\tilde Q_5}L^{\diamond}_{\tilde Q_3}(\tilde Q_1)=L^{\diamond}_{\tilde Q_5}\bigl(\mathrm{Vect}(\tilde Q_3\tilde Q_1^{*})\bigr)=\mathrm{Vect}\bigl(\tilde Q_5\,(\mathrm{Vect}(\tilde Q_3\tilde Q_1^{*}))^{*}\bigr)$; writing $\mathrm{Vect}(\tilde Q_3\tilde Q_1^{*})=\tilde Q_3\tilde Q_1^{*}-\langle\tilde Q_3,\tilde Q_1\rangle_{*}e_t$, whose star is $\tilde Q_1\tilde Q_3^{*}-\overline{\langle\tilde Q_3,\tilde Q_1\rangle_{*}}e_t$, gives $\tilde Q_5(\mathrm{Vect}(\tilde Q_3\tilde Q_1^{*}))^{*}=\tilde Q_5\tilde Q_1\tilde Q_3^{*}-\overline{\langle\tilde Q_3,\tilde Q_1\rangle_{*}}\,\tilde Q_5$, and taking the vector part gives the first display. For the second, $R^{\diamond}_{\tilde Q_5}R^{\diamond}_{\tilde Q_3}(\tilde Q_1)=\mathrm{Vect}\bigl(\mathrm{Vect}(\tilde Q_1\tilde Q_3^{*})\,\tilde Q_5^{*}\bigr)$, and the same substitution gives $\mathrm{Vect}(\tilde Q_1\tilde Q_3^{*}\tilde Q_5^{*})-\langle\tilde Q_1,\tilde Q_3\rangle_{*}\,\mathrm{Vect}(\tilde Q_5^{*})$; since $\tilde Q_3^{*}\tilde Q_5^{*}=(\tilde Q_5\tilde Q_3)^{*}$, this is the second display. The linearity is the parity of the product of two conjugate-linear maps.

**Remark (the mixed composites).** The two mixed orders carry the same correction. For the left-then-right order,
$L^{\diamond}_{\tilde Q_5}R^{\diamond}_{\tilde Q_3}(\tilde Q_1)=\mathrm{Vect}\bigl(\tilde Q_5\tilde Q_3\tilde Q_1^{*}\bigr)-\overline{\langle\tilde Q_1,\tilde Q_3\rangle_{*}}\,\mathrm{Vect}(\tilde Q_5)$, and for the right-then-left order $R^{\diamond}_{\tilde Q_5}L^{\diamond}_{\tilde Q_3}(\tilde Q_1)=\mathrm{Vect}\bigl(\mathrm{Vect}(\tilde Q_3\tilde Q_1^{*})\,\tilde Q_5^{*}\bigr)$: the projection inside the composite is the obstruction, and the composite is an operator of the block only in the degenerate cases.

**Corollary (the failure of multiplicativity).** The assignment $\tilde Q_5\mapsto L^{\diamond}_{\tilde Q_5}$ is $\mathbb{C}$-linear, $\lambda\tilde Q_5$ giving $\lambda$ times the operator, while the assignment $\tilde Q_5\mapsto R^{\diamond}_{\tilde Q_5}$ is conjugate-linear, $\lambda\tilde Q_5$ giving $\overline{\lambda}$ times the operator, by the parity of the two slots, and neither is **multiplicative**:
$L^{\diamond}_{\tilde Q_5}L^{\diamond}_{\tilde Q_3}\neq L^{\diamond}_{\tilde Q_5\diamond\tilde Q_3}$, and likewise for the right family. The witness is $\tilde Q_5=\tilde Q_3=\vec e_x$, $\tilde Q_1=\vec e_y$: the composite sends $\vec e_y$ to $-\vec e_y$, since $L^{\diamond}_{\vec e_x}(\vec e_y)=-\vec e_z$ and $L^{\diamond}_{\vec e_x}(-\vec e_z)=-\vec e_y$, while $L^{\diamond}_{\vec e_x\diamond \vec e_x}=L^{\diamond}_{0}=0$. The operators of the block therefore do **not** form a monoid under composition, and the block has no regular representation: the failure is stronger than the failure of a single linear representation, it is the failure of a multiplicative one.

**Remark (the contrast with the row).** For the general plain sesqualgebra the two composites close: there $L_{\tilde Q_5}L_{\tilde Q_3}=T_{\tilde Q_5,\tilde Q_3^{*}}$ is the ordinary two-sided multiplication and $R_{\tilde Q_5}R_{\tilde Q_3}=R_{\tilde Q_5\tilde Q_3}$, by *The Left and Right Multiplications of the Biquaternion Sesqualgebra*, §*The Mixed Composites*. The block is the projection $\mathrm{Vect}$ of each of those operators, and the projection intervenes twice, so the composition acquires the correction terms $-\overline{\langle\tilde Q_3,\tilde Q_1\rangle_{*}}\,\mathrm{Vect}(\tilde Q_5)$ and $-\langle\tilde Q_1,\tilde Q_3\rangle_{*}\,\mathrm{Vect}(\tilde Q_5^{*})$; the projection is not an algebra map of the row, and that is what destroys the multiplicativity.

**Corollary (the companion composes into the right family).** Since $T_{\tilde Q_5}=-R^{\diamond}_{\tilde Q_5}$ and $R^{\diamond}_{\tilde Q_5}R^{\diamond}_{\tilde Q_3}$ is the composition of the two right operators, the companions compose as
$T_{\tilde Q_5}T_{\tilde Q_3}=R^{\diamond}_{\tilde Q_5}R^{\diamond}_{\tilde Q_3}$, so the $\mathbb{C}$-linear companion family composes into the right family and not into itself, and the companion is not multiplicative either.

## The Derivations

**Definition.** A **derivation** of the block is an $\mathbb{R}$-linear operator $D$ of $\mathbb{B}$ satisfying the Leibniz rule

$$
D(\tilde Q_1\diamond\tilde Q_2)=D(\tilde Q_1)\diamond\tilde Q_2+\tilde Q_1\diamond D(\tilde Q_2)
$$

for all $\tilde Q_1,\tilde Q_2$; the derivations form a Lie algebra under the commutator, the derivation algebra of the block, by *Derivations of a Sesqualgebra*.

**Theorem (the derivation algebra).** For a real vector $\vec a=a_x\vec e_x+a_y\vec e_y+a_z\vec e_z$ define

$$
D_{\vec a}(\tilde Q_1)=[0,\ \vec a\times\vec Q_1],
$$

the cross product of $\vec a$ with the vector part, a $\mathbb{C}$-linear operator annihilating the centre. Then $D_{\vec a}$ is a derivation of the block exactly when $\vec a$ is **real**, and the derivations so obtained form a three-dimensional real space with basis $D_{\vec e_x},D_{\vec e_y},D_{\vec e_z}$, closed under the commutator,

$$
[D_{\vec a},D_{\vec b}]=D_{\vec a\times\vec b},
$$

so that the derivation algebra of the block is isomorphic to $\mathbb{R}^{3}$ with the cross product, and it is exactly this space. A derivation $D_{\vec a}$ with a non-real $\vec a$ fails the Leibniz rule, and a scalar derivation $\tilde Q_1\mapsto\lambda\tilde Q_1$ satisfies it only for $\lambda=0$; the three displayed derivations therefore exhaust the algebra.

*Proof.* The Leibniz defect of $D_{\vec a}$ is the computation of $\vec a\times(\vec Q_1\diamond\vec Q_2)$ against $(\vec a\times\vec Q_1)\diamond\vec Q_2+\vec Q_1\diamond(\vec a\times\vec Q_2)$; the two cross products in the three terms combine by the Jacobi identity of the cross product exactly when $\vec a$ is fixed by the conjugation, and the terms carrying $\overline{\vec a}$ in the sesquilinear slots cancel only then; the bracket is the vector triple identity $[D_{\vec a},D_{\vec b}](\tilde Q_1)=\vec a\times(\vec b\times\vec Q_1)-\vec b\times(\vec a\times\vec Q_1)=(\vec a\times\vec b)\times\vec Q_1$. The dimension three is the dimension of the space of the real vectors $\vec a$, the operators $D_{\vec e_x},D_{\vec e_y},D_{\vec e_z}$ being independent on the vector coordinates.

**Remark (the derivations act by the cross product).** The operator $D_{\vec a}$ acts on the complex vector subspace by the cross product with $\vec a$, which is the infinitesimal form of the transformations of the vector coordinates preserving the cross product; on the real vectors $D_{\vec a}(\vec Q_1)=\vec a\times\vec Q_1$ is the derivation of the cross product, and the derivation algebra $\mathbb{R}^{3}$ is the infinitesimal form of the group of the transformations of the real vector triple preserving the cross product and the dot product, of determinant one. The central direction is dead: $D_{\vec a}$ annihilates the centre for every $\vec a$, and the central component of an operator never enters the Leibniz rule, since the block reads the centre only through the vector part.

## The Structure Group

**Definition.** The **structure group** of the block is the group of the invertible $\mathbb{R}$-linear maps $T$ of $\mathbb{B}$ satisfying

$$
T(\tilde Q_1\diamond\tilde Q_2)=T(\tilde Q_1)\diamond T(\tilde Q_2)
$$

for all $\tilde Q_1,\tilde Q_2$; its identity component has Lie algebra the derivation algebra above, by the differentiation of the defining equation at the identity, *Derivations of a Sesqualgebra*, §*The Lie Algebra of Derivations*.

**Theorem (the two kinds of elements).** The structure group contains the following.

1. The **coefficientwise conjugation** $\overline{\cdot}$: it is an automorphism of the block, $\overline{\tilde Q_1\diamond\tilde Q_2}=\overline{\tilde Q_1}\diamond\overline{\tilde Q_2}$, and it is **conjugate-linear**, so the structure group is not confined to the linear maps.
2. The **complex linear extensions of the real transformations preserving the cross product**: for a real $3\times3$ matrix $R$ with $R^{\mathsf T}R=I$ and $\det R=1$, the map $T_R$ fixing the centre and acting on the complex vector subspace by $R$ in its two real components,
   $$
   T_R(Q_te_t+\vec U+i\vec V)=Q_te_t+R\vec U+iR\vec V,
   $$
   is a $\mathbb{C}$-linear automorphism of the block.

The **natural conjugation** $^{\natural}$ is **not** an automorphism of the block: it fails $T(\tilde Q_1\diamond\tilde Q_2)=T(\tilde Q_1)\diamond T(\tilde Q_2)$ on a general pair.

*Proof.* The first statement is the proposition of *Introduction to the Antisymmetric Plain Sesqualgebra*, §*Conjugate-Alternation*. For the second, $T_R$ preserves the complex bilinear dot and cross products of the vector parts, since $R$ preserves the dot and the cross products of the real vectors, $R^{\mathsf T}R=I$ and $\det R=1$; the block is built from the dot and the cross of the vector parts through the sesquilinear slots, so $T_R(\tilde Q_1\diamond\tilde Q_2)=T_R(\tilde Q_1)\diamond T_R(\tilde Q_2)$. For the third, the natural conjugation negates the vector part and fixes the scalar part, so it reverses the cross term of the block; the witness $(\tilde Q_1,\tilde Q_2)=(\vec e_x,\vec e_y)$ gives $^{\natural}(\vec e_x\diamond \vec e_y)={}^{\natural}(-\vec e_z)=\vec e_z$ on the left against $^{\natural}\vec e_x\diamond{}^{\natural}\vec e_y=(-\vec e_x)\diamond(-\vec e_y)=\vec e_x\diamond \vec e_y=-\vec e_z$ on the right.

**Remark (the group and its Lie algebra).** The transformations $T_R$ form a group isomorphic to the group of the transformations of the real vector triple preserving the cross product and the dot product, of determinant one, acting on the complex vector subspace by the same real matrix in both real components, and its Lie algebra is the three-dimensional algebra with basis the three derivations $D_{\vec e_x},D_{\vec e_y},D_{\vec e_z}$ of the preceding section; the coefficientwise conjugation supplies the second component, conjugate-linear, which inverts with the complex-linear one to a linear automorphism when composed with a sign on the vector part. The structure group is therefore the semidirect product of the linear transformations of that group and the order-two conjugation, and its Lie algebra is the three-dimensional cross-product algebra of the derivations. The group of the transformations preserving the **form** $\langle\cdot,\cdot\rangle_{*}$ alone is larger, the group of *Units and the Unitary Elements*; the structure group of the block is the subgroup cut out by the preservation of the product.

## Summary

The left multiplication of the block is the conjugate-linear operator $L^{\diamond}_{\tilde Q_5}=\mathrm{Vect}\circ S_{\tilde Q_5,e_t}$, the vector part of the left multiplication of the row; the right multiplication is its conjugate, $R^{\diamond}_{\tilde Q_5}=-\overline{L^{\diamond}_{\tilde Q_5}}$, so a single $\mathbb{C}$-linear companion $T_{\tilde Q_5}=\overline{L^{\diamond}_{\tilde Q_5}}=-R^{\diamond}_{\tilde Q_5}$ carries the whole operator theory. In the real basis the matrix has its two scalar rows zero and its trace zero; it has rank six for a unit and four for a zero divisor, the kernel being the set of the $\tilde Q_1$ with $\tilde Q_5\tilde Q_1^{*}$ central, which is the centre for $\tilde Q_5=e_t$ and the line $\mathbb{C}\vec e_\mu$ for $\tilde Q_5=\vec e_\mu$. The characteristic polynomial of the matrix $M_{\tilde Q_5}$ is even, $\lambda^{2}P(\lambda)$, with $P$ even of degree six: $\lambda^{2}(\lambda^{2}-1)^{3}$ at the unit, $\lambda^{4}(\lambda^{2}+1)^{2}$ at the basis vectors, and $\lambda^{4}(\lambda^{2}+2)^{2}$ at the zero divisor $\vec e_x+i\vec e_y$. The adjoint with respect to $\langle\cdot,\cdot\rangle_{*}$ is the right multiplication of the star of the vector part, $(L^{\diamond}_{\tilde Q_5})^{\dagger}(\tilde Q_2)=(\mathrm{Vect}\tilde Q_2)^{*}\tilde Q_5$, a conjugate-linear operator with scalar part $\langle \vec A,\vec Q_2\rangle_{*}$; the operator is the first factor of the two-parameter sandwich, whose value is $L^{\diamond}_{\tilde Q_5}(\tilde Q_1)\tilde Q_3^{*}+\langle\tilde Q_5,\tilde Q_1\rangle_{*}\tilde Q_3^{*}$. The derivations are the cross products $D_{\vec a}(\tilde Q_1)=[0,\vec a\times\vec Q_1]$ with $\vec a$ real, a three-dimensional Lie algebra isomorphic to $\mathbb{R}^{3}$ with the cross product; the structure group contains the coefficientwise conjugation (conjugate-linear) and the complex-linear extensions of the real transformations preserving the cross product of the vector triple, of determinant one, with Lie algebra the derivation algebra, and it does not contain the natural conjugation. The two one-sided operators do not compose, $L^{\diamond}_{\tilde Q_5}L^{\diamond}_{\tilde Q_3}(\tilde Q_1)=\mathrm{Vect}(\tilde Q_5\tilde Q_1\tilde Q_3^{*})-\overline{\langle\tilde Q_3,\tilde Q_1\rangle_{*}}\,\mathrm{Vect}(\tilde Q_5)$ while $L^{\diamond}_{\vec e_x}L^{\diamond}_{\vec e_x}(\vec e_y)=-\vec e_y$ against $L^{\diamond}_{\vec e_x\diamond \vec e_x}=0$, so the block has no monoid of operators and no regular representation; the companion family composes into the right family, $T_{\tilde Q_5}T_{\tilde Q_3}=R^{\diamond}_{\tilde Q_5}R^{\diamond}_{\tilde Q_3}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L^{\diamond}_{\tilde Q_5}(\tilde Q_1)=\tilde Q_5\diamond\tilde Q_1$ | the conjugate-linear left multiplication of the block |
| $R^{\diamond}_{\tilde Q_5}(\tilde Q_1)=\tilde Q_1\diamond\tilde Q_5=-\overline{L^{\diamond}_{\tilde Q_5}}$ | the right multiplication, minus the companion |
| $T_{\tilde Q_5}=\overline{L^{\diamond}_{\tilde Q_5}}$ | the $\mathbb{C}$-linear companion, the honest linear object |
| $(\mathcal B)=(e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z)$ | the real basis in which the matrices are read |
| $L^{\diamond}_{\tilde Q_5}=\mathrm{Vect}\circ S_{\tilde Q_5,e_t}$ | the operator inside the sesquilinear sandwich |
| $M_{e_t}=\operatorname{diag}(0,-1,-1,-1,0,1,1,1)$ | the matrix of the unit, trace zero, rank six |
| $\chi_{M_{\tilde Q_5}}=\lambda^{2}P(\lambda)$ | the characteristic polynomial of the real matrix of $L^{\diamond}_{\tilde Q_5}$, even, $P$ even of degree six |
| $(L^{\diamond}_{\tilde Q_5})^{\dagger}(\tilde Q_2)=(\mathrm{Vect}\tilde Q_2)^{*}\tilde Q_5$ | the adjoint under the twisted rule |
| $D_{\vec a}(\tilde Q_1)=[0,\vec a\times\vec Q_1]$ | the derivation by a real vector, the algebra $\mathbb{R}^{3}$ with the cross product |
| $T_R$ | the complex-linear automorphism from a real $R$ with $R^{\mathsf T}R=I$, $\det R=1$ |

## Further Reading

- [Introduction to the Antisymmetric Plain Sesqualgebra](introduction-to-the-antisymmetric-plain-sesqualgebra.html), for the operation, the conjugate-alternation and the coefficientwise automorphism
- [The Left and Right Multiplications of the Biquaternion Sesqualgebra](the-left-and-right-multiplications-of-the-biquaternion-sesqualgebra.html), for the one-sided multiplications of the row and the obstruction to a single linear representation
- [The Sesquilinear Sandwich on the Biquaternion](the-sesquilinear-sandwich-on-the-biquaternion.html) and [The Adjoint of the Sesquilinear Sandwich on the Biquaternion](the-adjoint-of-the-sesquilinear-sandwich-on-the-biquaternion.html), for the sandwich, the twisted adjoint rule and the adjoints of the one-sided operators
- [The Sesquilinear Pairing of the Antisymmetric Plain Sesqualgebra](the-sesquilinear-pairing-of-the-antisymmetric-plain-sesqualgebra.html), for the form, the Gram data and the sandwich relation of the block
- [Derivations of a Sesqualgebra](derivations-of-a-sesqualgebra.html), for the derivation algebra, the group of the automorphisms and its Lie algebra
- [Norm and Invertibility in the General Quaternionic Algebra](norm-and-invertibility-in-the-general-quaternionic-algebra.html), for the units, the zero divisors and the form $\langle\cdot,\cdot\rangle_{*}$
- [Units and the Unitary Elements](units-and-the-unitary-elements.html), for the group preserving the form, larger than the structure group of the block
- [Introduction to the Symmetric Plain Sesqualgebra](introduction-to-the-symmetric-plain-sesqualgebra.html), for the operator and its invariants in the realization
- [Introduction to the Symmetric Plain Sesqualgebra](introduction-to-the-symmetric-plain-sesqualgebra.html), for the operator and its invariants in the regular model
