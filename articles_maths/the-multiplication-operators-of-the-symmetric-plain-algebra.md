# __The Multiplication Operators of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra of $\mathbb{B}$ carries the product $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ of *Introduction to the Symmetric Plain Algebra*. This article reads the **multiplication operators** of the block, $L^{\bullet}_{\tilde A}\tilde Q=\tilde A\bullet\tilde Q$ and $R^{\bullet}_{\tilde A}\tilde Q=\tilde Q\bullet\tilde A$, and the operator theory they carry: their relation to the operators of the plain product, their composition, their traces, determinants and ranks, their associate with respect to the trace form, the Jordan identity read on them, and the derivations and automorphisms of the block.

The block is commutative, so the left and the right operator of an element coincide, and the operator theory is a theory of one operator to an element. The operator identity that opens the article is a factor of two away from the sum of the plain operators, and that factor is computed here; the trace form with respect to which the associate is taken is *The Trace Form and the Invariance of the Symmetric Plain Algebra*, and the plain operators are *Two-Sided Operators on the Biquaternion Algebra* and *One-Sided Operators on the General Plain Algebra of Biquaternions*. The derivations and the automorphisms of the block are read as the structure group and the Lie algebra of the Jordan algebra, and the matrix models of the same operators are *Introduction to the Symmetric Plain Algebra*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and central scalar imaginary $i$. An element is $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=\sum_\mu Q_\mu\vec e_\mu$ and $Q_\mu\in\mathbb{C}$, and $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ is the generic norm. On the operators, $L_{\tilde A},R_{\tilde A}$ are the left and right multiplications of the **plain** product, $L_{\tilde A}\tilde Q=\tilde A\tilde Q$ and $R_{\tilde A}\tilde Q=\tilde Q\tilde A$, and $L^{\bullet}_{\tilde A},R^{\bullet}_{\tilde A}$ are those of the block, $L^{\bullet}_{\tilde A}\tilde Q=\tilde A\bullet\tilde Q$ and $R^{\bullet}_{\tilde A}\tilde Q=\tilde Q\bullet\tilde A$. The trace form is $\tau(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\bullet\tilde Q)=P_tQ_t-(\vec P,\vec Q)$, and the commutator of two operators is written with brackets, $[L^{\bullet}_{\tilde A},L^{\bullet}_{\tilde Q_1}]=L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde Q_1}-L^{\bullet}_{\tilde Q_1}L^{\bullet}_{\tilde A}$.

## The Multiplication Operators

### The Definition and the Coincidence of the Two Operators

**Definition.** The **left** and **right multiplication operators** of the block by an element $\tilde A$ are

$$
L^{\bullet}_{\tilde A}\tilde Q=\tilde A\bullet\tilde Q,\qquad R^{\bullet}_{\tilde A}\tilde Q=\tilde Q\bullet\tilde A .
$$

**Proposition.** The block is commutative, so the two operators of an element coincide:

$$
L^{\bullet}_{\tilde A}=R^{\bullet}_{\tilde A}.
$$

*Proof.* $\tilde A\bullet\tilde Q=\tilde Q\bullet\tilde A$ by the commutativity of the block.

So the operator theory of the block is a theory of one operator to an element, and the left and right operators are not two families but one.

### The Relation to the Plain Operators

**Theorem.** The multiplication operator of the block is **half** the sum of the two plain operators:

$$
L^{\bullet}_{\tilde A}=\tfrac12\bigl(L_{\tilde A}+R_{\tilde A}\bigr),\qquad\text{equivalently}\qquad L_{\tilde A}+R_{\tilde A}=2L^{\bullet}_{\tilde A}.
$$

*Proof.* $L^{\bullet}_{\tilde A}\tilde Q=\tfrac12(\tilde A\tilde Q+\tilde Q\tilde A)=\tfrac12(L_{\tilde A}+R_{\tilde A})\tilde Q$.

**Remark (the sum is twice the operator).** The sum $L_{\tilde A}+R_{\tilde A}$ is the operator of the **doubled** product, $(L_{\tilde A}+R_{\tilde A})\tilde Q=\tilde A\tilde Q+\tilde Q\tilde A=2(\tilde A\bullet\tilde Q)$, and it is twice the multiplication operator of the block. **The identity between the operator of the block and the sum of the two plain operators carries the factor $\tfrac12$**, and a statement without it would be off by two.

### The Trace, the Determinant and the Rank

**Theorem.** For every $\tilde A$,

$$
\operatorname{Tr}\bigl(L^{\bullet}_{\tilde A}\bigr)=4A_t,\qquad
\det\bigl(L^{\bullet}_{\tilde A}\bigr)=A_t^2\,\langle\tilde A\rangle_{\natural}.
$$

*Proof.* The trace is $\tfrac12\bigl(\operatorname{Tr}(L_{\tilde A})+\operatorname{Tr}(R_{\tilde A})\bigr)$, and the two plain operators have trace $4A_t$ each; the determinant is computed on the matrix of the operator. In the $2\times2$ model of *Introduction to the Symmetric Plain Algebra* the operator is $M\mapsto\tfrac12(\mathsf{M}_2(\tilde A)M+M\mathsf{M}_2(\tilde A))$, whose eigenvalues are $\tfrac12(\lambda_i+\lambda_j)$ over the eigenvalues $\lambda_1,\lambda_2$ of $\mathsf{M}_2(\tilde A)$, with $\lambda_1\lambda_2=\langle\tilde A\rangle_{\natural}$ and $\lambda_1+\lambda_2=2A_t$; the determinant is $\bigl(\tfrac12(\lambda_1+\lambda_1)\bigr)\bigl(\tfrac12(\lambda_1+\lambda_2)\bigr)\bigl(\tfrac12(\lambda_2+\lambda_1)\bigr)\bigl(\tfrac12(\lambda_2+\lambda_2)\bigr)=A_t^2\,\langle\tilde A\rangle_{\natural}$.

**Theorem (the rank).** The multiplication operator of the block has rank four exactly when $\tilde A$ has non-zero scalar part and non-zero generic norm,

$$
\operatorname{rank}L^{\bullet}_{\tilde A}=4\iff A_t\neq0\ \text{and}\ \langle\tilde A\rangle_{\natural}\neq0,
$$

and otherwise the rank is

$$
\operatorname{rank}L^{\bullet}_{\tilde A}=
\begin{cases}
3,& A_t\neq0,\ \langle\tilde A\rangle_{\natural}=0,\\
2,& A_t=0,\ \tilde A\neq0,\\
0,& \tilde A=0.
\end{cases}
$$

*Proof.* The determinant vanishes exactly when $A_t=0$ or $\langle\tilde A\rangle_{\natural}=0$, which gives the first statement and the three remaining rows by exclusion; the three cases are computed on the eigenvalues of $\mathsf{M}_2(\tilde A)$ and of $\tfrac12(\mathsf{M}_2(\tilde A)M+M\mathsf{M}_2(\tilde A))$. On a zero divisor with $A_t\neq0$ the roots of the characteristic polynomial are $0$ and $2A_t$, so the four eigenvalues of the operator are $0,A_t,A_t,2A_t$, all distinct, and the rank is three. On the hyperplane $A_t=0$ the matrix $\mathsf{M}_2(\tilde A)$ is traceless, of eigenvalues $\lambda,-\lambda$; if $\langle\tilde A\rangle_{\natural}\neq0$ then $\lambda\neq0$ and the operator has the eigenvalues $\lambda,0,0,-\lambda$, of rank two; if $\langle\tilde A\rangle_{\natural}=0$ and $\tilde A\neq0$ then $\mathsf{M}_2(\tilde A)$ is a non-zero nilpotent, conjugate to $\begin{pmatrix}0&1\\0&0\end{pmatrix}$, and the operator is nilpotent, of rank two as well. At $\tilde A=0$ the operator vanishes.

**Remark (the kernel on the hyperplane).** For $\tilde A=\vec e_x$, a traceless element of the hyperplane $A_t=0$, the kernel is the plane spanned by $\vec e_y,\vec e_z$, since $\vec e_x\bullet \vec e_y=\vec e_x\bullet \vec e_z=0$; the operator is singular on the whole hyperplane $A_t=0$ and at every zero divisor, and it is invertible exactly on the units of the block with a non-zero scalar part. **The multiplication operator of the block is singular precisely on the union of the zero divisors and the trace-zero hyperplane**, and it is invertible off them.

## The Composition and the Failure of Multiplicativity

**Proposition.** The composition of two multiplication operators is

$$
L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde Q_1}=\tfrac14\bigl(L_{\tilde A\tilde Q_1}+L_{\tilde A}R_{\tilde Q_1}+R_{\tilde A}L_{\tilde Q_1}+R_{\tilde Q_1\tilde A}\bigr),
$$

and the composition is **not** the multiplication operator of the product:

$$
L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde Q_1}\neq L^{\bullet}_{\tilde A\bullet\tilde Q_1}\qquad\text{in general.}
$$

*Proof.* Expand $\tfrac12(L_{\tilde A}+R_{\tilde A})\cdot\tfrac12(L_{\tilde Q_1}+R_{\tilde Q_1})$ with $L_{\tilde A}L_{\tilde Q_1}=L_{\tilde A\tilde Q_1}$ and $R_{\tilde A}R_{\tilde Q_1}=R_{\tilde Q_1\tilde A}$; for the failure, take $\tilde A=\tilde Q_1=\vec e_x$ and evaluate on $\vec e_y$:

$$
(L^{\bullet}_{\vec e_x})^2\vec e_y=\vec e_x\bullet(\vec e_x\bullet \vec e_y)=\vec e_x\bullet0=0,\qquad
L^{\bullet}_{\vec e_x\bullet \vec e_x}\vec e_y=L^{\bullet}_{-e_t}\vec e_y=-\vec e_y,
$$

and the two values differ.

**Remark (the block is not associative).** The failure of multiplicativity of the left regular representation is the operator form of the failure of associativity of the block: an associative multiplication would give $L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde Q_1}=L^{\bullet}_{\tilde A\tilde Q_1}$. **The block is a Jordan algebra and not an associative one, and its left regular representation is not multiplicative**; what survives is the Jordan identity of the next section.

## The Associate with Respect to the Trace Form

**Theorem.** Every multiplication operator of the block is **self-associate** with respect to the trace form:

$$
\tau\bigl(L^{\bullet}_{\tilde A}\tilde Q_2,\tilde Q_3\bigr)=\tau\bigl(\tilde Q_2,L^{\bullet}_{\tilde A}\tilde Q_3\bigr),
$$

so $(L^{\bullet}_{\tilde A})^{\approx}=L^{\bullet}_{\tilde A}$ in the mark $\approx$ of the associate of *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples*.

*Proof.* By the definition of the operator and the invariance of the trace form,

$$
\tau\bigl(L^{\bullet}_{\tilde A}\tilde Q_2,\tilde Q_3\bigr)=\tau(\tilde A\bullet\tilde Q_2,\tilde Q_3)=\tau(\tilde A,\tilde Q_2\bullet\tilde Q_3),
$$

and, by the symmetry of the form and the invariance again,

$$
\tau(\tilde A,\tilde Q_2\bullet\tilde Q_3)=\tau(\tilde Q_2\bullet\tilde Q_3,\tilde A)=\tau(\tilde Q_2,\tilde Q_3\bullet\tilde A)=\tau(\tilde Q_2,\tilde A\bullet\tilde Q_3)=\tau\bigl(\tilde Q_2,L^{\bullet}_{\tilde A}\tilde Q_3\bigr).
$$


**Remark (the mark, and the other adjoint).** The form is the **indefinite** general plain bilinear form, so its transpose is the **associate** $\approx$ and not the dagger; the dagger belongs to the positive definite Hermitian form, and with respect to it the operator is adjoint to another operator, $(L^{\bullet}_{\tilde A})^{\dagger}=L^{\bullet}_{\tilde A^{*}}$, which is $L^{\bullet}_{\tilde A}$ exactly when $\tilde A$ is Hermitian. **The multiplication operators are self-associate and not self-adjoint**, and the two marks must not be exchanged; the Hermitian form, its involutions and its adjoints are *Two-Sided Operators on the General Plain Sesqualgebra* and the Hilbert-algebra series.

**Remark (the operators are symmetric).** The multiplication operators of the block form a **family of self-associate operators** for the trace form; the family is **not** commutative, because the commutator of two of them is the inner derivation $\tfrac14\operatorname{ad}_{[\tilde A,\tilde Q_1]}$ of §*The Derivations*, which vanishes only when the two parameters commute. **Every element of the block acts by a $\tau$-symmetric operator**, and the family is the image of the linear map $\tilde A\mapsto L^{\bullet}_{\tilde A}$ from the algebra into the endomorphisms of the underlying space. The symmetry is the operator form of the associativity of the form, and it holds for the plain operators relative to the same form as well.

## The Jordan Identity on the Operators

**Theorem.** For every $\tilde Q_2$,

$$
\bigl[L^{\bullet}_{\tilde Q_2},L^{\bullet}_{\tilde Q_2\bullet\tilde Q_2}\bigr]=0 .
$$

*Proof.* This is the operator form of the Jordan identity: writing the identity $(\tilde Q_2\bullet\tilde Q_3)\bullet(\tilde Q_2\bullet\tilde Q_2)=\tilde Q_2\bullet(\tilde Q_3\bullet(\tilde Q_2\bullet\tilde Q_2))$ with the left operator gives $L^{\bullet}_{\tilde Q_2\bullet\tilde Q_2}L^{\bullet}_{\tilde Q_2}=L^{\bullet}_{\tilde Q_2}L^{\bullet}_{\tilde Q_2\bullet\tilde Q_2}$ for every $\tilde Q_3$, which is the displayed commutation.

**Remark (the operator identity and the element identity).** The commutation $[L^{\bullet}_{\tilde Q_2},L^{\bullet}_{\tilde Q_2\bullet\tilde Q_2}]=0$ is the operator form of the Jordan identity, and it is exactly the statement that the operator $L^{\bullet}_{\tilde Q_2}$ commutes with the operator of its own square. **The operators of the block satisfy the Jordan identity in the operator form and fail multiplicativity**, and the two facts together are the operator reading of a Jordan algebra that is not associative.

## The Derivations

### The Inner Derivations

**Proposition.** The commutator of two multiplication operators is an **inner derivation**:

$$
\bigl[L^{\bullet}_{\tilde A},L^{\bullet}_{\tilde Q_1}\bigr]=\tfrac14\operatorname{ad}_{[\tilde A,\tilde Q_1]},
\qquad \operatorname{ad}_{\tilde Q_4}=L_{\tilde Q_4}-R_{\tilde Q_4},
$$

where $[\tilde A,\tilde Q_1]=\tilde A\tilde Q_1-\tilde Q_1\tilde A$ is the commutator of the plain product, and the commutator of two plain operators is $\operatorname{ad}_{\tilde Q_4}$.

*Proof.* Compute

$$
\bigl[L^{\bullet}_{\tilde A},L^{\bullet}_{\tilde Q_1}\bigr]=\tfrac14\bigl[L_{\tilde A}+R_{\tilde A},L_{\tilde Q_1}+R_{\tilde Q_1}\bigr]
=\tfrac14\bigl([L_{\tilde A},L_{\tilde Q_1}]+[R_{\tilde A},R_{\tilde Q_1}]\bigr),
$$

because a left and a right operator commute. The two plain commutators are $[L_{\tilde A},L_{\tilde Q_1}]=L_{[\tilde A,\tilde Q_1]}$ and $[R_{\tilde A},R_{\tilde Q_1}]=-R_{[\tilde A,\tilde Q_1]}$, since $R_{\tilde A}R_{\tilde Q_1}=R_{\tilde Q_1\tilde A}$; their sum is $L_{[\tilde A,\tilde Q_1]}-R_{[\tilde A,\tilde Q_1]}=\operatorname{ad}_{[\tilde A,\tilde Q_1]}$, and the displayed identity follows.

Each inner derivation is a derivation of the block: $\operatorname{ad}_{\tilde Q_4}$ is a derivation of the associative plain product, $\operatorname{ad}_{\tilde Q_4}(\tilde Q_2\tilde Q_3)=\operatorname{ad}_{\tilde Q_4}\tilde Q_2\cdot\tilde Q_3+\tilde Q_2\cdot\operatorname{ad}_{\tilde Q_4}\tilde Q_3$, and a derivation of a product is a derivation of its symmetrisation, because the symmetrised product is a linear combination of plain products. The derivation identity reads

$$
\operatorname{ad}_{\tilde Q_4}(\tilde Q_2\bullet\tilde Q_3)=\operatorname{ad}_{\tilde Q_4}\tilde Q_2\bullet\tilde Q_3+\tilde Q_2\bullet\operatorname{ad}_{\tilde Q_4}\tilde Q_3 .
$$

### The Derivation Algebra and the Automorphisms

**Definition.** The **derivations** of the block are the $\mathbb{C}$-linear maps $D$ of $\mathbb{B}$ with

$$
D(\tilde Q_2\bullet\tilde Q_3)=D\tilde Q_2\bullet\tilde Q_3+\tilde Q_2\bullet D\tilde Q_3 .
$$

They form a Lie algebra under the commutator, the **derivation algebra** $\operatorname{Der}(\mathbb{B},\bullet)$.

**Theorem.** Every derivation of the block is inner:

$$
\operatorname{Der}(\mathbb{B},\bullet)=\operatorname{Inn}(\mathbb{B},\bullet)=\bigl\{\tfrac14\operatorname{ad}_{\tilde Q_4}:\tilde Q_4\in[\mathbb{B},\mathbb{B}]\bigr\}\cong\mathfrak{sl}(2,\mathbb{C}),
$$

of complex dimension three, and $[\mathbb{B},\mathbb{B}]$ is the trace-zero subspace of $\mathbb{B}$.

*Proof.* The inner derivations are $\tfrac14\operatorname{ad}_{\tilde Q_4}$ with $\tilde Q_4=[\tilde A,\tilde Q_1]$ by the previous section, and $[\tilde A,\tilde Q_1]$ ranges over the trace-zero subspace, because the commutator of two elements is always trace-zero and every trace-zero element is a commutator in this algebra. The derivation algebra contains the inner derivations, and a direct computation of the linear system $D(\tilde Q_2\bullet\tilde Q_3)=D\tilde Q_2\bullet\tilde Q_3+\tilde Q_2\bullet D\tilde Q_3$ on the sixteen basis pairs gives a space of complex dimension three; the two agree.

**Remark (no outer derivations).** **The derivation algebra of the block is exactly its algebra of inner derivations**, of dimension three, and it is isomorphic to the Lie algebra $\mathfrak{sl}(2,\mathbb{C})$ of the trace-zero elements under the commutator. The derivations of the **plain** product, by contrast, are the maps $\operatorname{ad}_{\tilde Q_4}$ and are all inner as well, but of dimension three over the trace-zero elements; the two derivation algebras are the same Lie algebra read on the two products, because $\tfrac14\operatorname{ad}_{\tilde Q_4}$ and $\operatorname{ad}_{\tilde Q_4}$ span the same three-dimensional space.

## The Automorphisms and the Structure Group

### The Automorphisms

**Definition.** An **automorphism** of the block is an invertible $\mathbb{C}$-linear map $g$ of $\mathbb{B}$ with

$$
g(\tilde Q_2\bullet\tilde Q_3)=g\tilde Q_2\bullet g\tilde Q_3 .
$$

They form a group, the **automorphism group** $\operatorname{Aut}(\mathbb{B},\bullet)$, and every automorphism fixes the unit, $g(e_t)=e_t$, and preserves the generic trace and the generic norm:

$$
T(g\tilde Q_2)=T(\tilde Q_2),\qquad \langle g\tilde Q_2\rangle_{\natural}=\langle\tilde Q_2\rangle_{\natural}.
$$

*Proof.* The automorphism group is a group under composition. An automorphism fixes the unit: by surjectivity every $\tilde Q_2$ is $g(\tilde Q_3)$, so

$$
g(e_t)\bullet\tilde Q_2=g(e_t)\bullet g(\tilde Q_3)=g(e_t\bullet\tilde Q_3)=g(\tilde Q_3)=\tilde Q_2,
$$

and $g(e_t)$ is therefore a two-sided identity of the block; the identity is unique, so $g(e_t)=e_t$. Applying $g$ to the quadratic identity $\tilde Q_2\bullet\tilde Q_2-T(\tilde Q_2)\tilde Q_2+\langle\tilde Q_2\rangle_{\natural}e_t=0$ gives the quadratic identity of $g\tilde Q_2$ with the same two coefficients, because $g$ fixes $e_t$ and is linear. The generic trace is half the operator trace, $T(\tilde Q_2)=\tfrac12\operatorname{Tr}(L^{\bullet}_{\tilde Q_2})$, and the generic norm is recovered from the trace and the square, $\langle\tilde Q_2\rangle_{\natural}=\tfrac12\bigl(T(\tilde Q_2)^2-T(\tilde Q_2\bullet\tilde Q_2)\bigr)$; both are unchanged by $g$, because $L^{\bullet}_{g\tilde Q_2}=gL^{\bullet}_{\tilde Q_2}g^{-1}$ and $g$ preserves the product, so the traces agree. Hence $T(g\tilde Q_2)=T(\tilde Q_2)$ and $\langle g\tilde Q_2\rangle_{\natural}=\langle\tilde Q_2\rangle_{\natural}$.

**Theorem.** The **inner automorphisms** are automorphisms: for every unit $\tilde A$ of the block,

$$
\operatorname{Ad}_{\tilde A}:\tilde Q_2\longmapsto\tilde A\tilde Q_2\tilde A^{-1}
$$

satisfies $\operatorname{Ad}_{\tilde A}(\tilde Q_2\bullet\tilde Q_3)=\operatorname{Ad}_{\tilde A}\tilde Q_2\bullet\operatorname{Ad}_{\tilde A}\tilde Q_3$.

*Proof.* Conjugation by a unit is an automorphism of the associative plain product, and it carries the symmetrised product to the symmetrised product:

$$
\operatorname{Ad}_{\tilde A}(\tilde Q_2\bullet\tilde Q_3)
=\tfrac12\bigl(\tilde A(\tilde Q_2\tilde Q_3+\tilde Q_3\tilde Q_2)\tilde A^{-1}\bigr)
=\tfrac12\bigl(\tilde A\tilde Q_2\tilde A^{-1}\tilde A\tilde Q_3\tilde A^{-1}+\tilde A\tilde Q_3\tilde A^{-1}\tilde A\tilde Q_2\tilde A^{-1}\bigr)
=\operatorname{Ad}_{\tilde A}\tilde Q_2\bullet\operatorname{Ad}_{\tilde A}\tilde Q_3 ,
$$

the inner factors $\tilde A^{-1}\tilde A$ cancelling.

**Theorem.** The inner automorphisms $\operatorname{Ad}_{\tilde A}$, over the units $\tilde A$, form the group $\operatorname{InnAut}(\mathbb{B},\bullet)$ of complex dimension three, isomorphic to the units modulo the central scalars; its Lie algebra is the derivation algebra, so that the group is the projective general linear group:

$$
\operatorname{InnAut}(\mathbb{B},\bullet)\cong\mathbb{B}^{\times}/\mathbb{C}^{\times}\cong PGL(2,\mathbb{C}),\qquad
\operatorname{Lie}\operatorname{InnAut}(\mathbb{B},\bullet)=\operatorname{Der}(\mathbb{B},\bullet)\cong\mathfrak{sl}(2,\mathbb{C}),\qquad
\dim_{\mathbb{C}}\operatorname{InnAut}(\mathbb{B},\bullet)=3 .
$$

*Proof.* The map $\tilde A\mapsto\operatorname{Ad}_{\tilde A}$ is a homomorphism from the units onto the inner automorphisms, of kernel the central scalars $\mathbb{C}^{\times}e_t$; the units are the non-isotropic elements, of complex dimension four and isomorphic to $GL(2,\mathbb{C})$ through $\mathsf{M}_2$, and the kernel one, so the image has dimension three and is the quotient $\mathbb{B}^{\times}/\mathbb{C}^{\times}\cong PGL(2,\mathbb{C})$. The derivations of the block are exactly the commutators $[\tilde Q_4,\cdot\,]$, of dimension three, and they are the Lie algebra of the inner automorphisms because $[\operatorname{ad}_{\tilde Q_4},\operatorname{ad}_{\tilde D}]=\operatorname{ad}_{[\tilde Q_4,\tilde D]}$.

**Theorem.** Every inner automorphism preserves the antisymmetric part,

$$
\operatorname{Ad}_{\tilde A}[\tilde Q_2,\tilde Q_3]=[\operatorname{Ad}_{\tilde A}\tilde Q_2,\operatorname{Ad}_{\tilde A}\tilde Q_3],
$$

while the natural conjugation **reverses** it:

$$
[\tilde Q_2^{\natural},\tilde Q_3^{\natural}]=-[\tilde Q_2,\tilde Q_3]^{\natural}.
$$

*Proof.* The inner automorphism is the conjugation by a unit in the associative plain algebra, so it is an automorphism of the plain product and preserves the commutator. For the natural conjugation, $(\tilde Q_2\tilde Q_3)^{\natural}=\tilde Q_3^{\natural}\tilde Q_2^{\natural}$, so $[\tilde Q_2,\tilde Q_3]^{\natural}=(\tilde Q_2\tilde Q_3-\tilde Q_3\tilde Q_2)^{\natural}=\tilde Q_3^{\natural}\tilde Q_2^{\natural}-\tilde Q_2^{\natural}\tilde Q_3^{\natural}=-[\tilde Q_2^{\natural},\tilde Q_3^{\natural}]$, which is the displayed identity.

**Remark (the natural conjugation is an outer automorphism).** The **natural conjugation** $\tilde Q_2\mapsto\tilde Q_2^{\natural}$ is an automorphism of the block, because it is an anti-automorphism of the associative product and the symmetrisation repairs the order:

$$
(\tilde Q_2\bullet\tilde Q_3)^{\natural}=\tfrac12\bigl((\tilde Q_2\tilde Q_3)^{\natural}+(\tilde Q_3\tilde Q_2)^{\natural}\bigr)=\tfrac12\bigl(\tilde Q_3^{\natural}\tilde Q_2^{\natural}+\tilde Q_2^{\natural}\tilde Q_3^{\natural}\bigr)=\tilde Q_2^{\natural}\bullet\tilde Q_3^{\natural}.
$$

It is **not inner**, by the reversal of the antisymmetric part just proved: an inner automorphism preserves the bracket and the natural conjugation negates it, and the bracket is non-zero. It acts as the identity on the centre and as the negation on the vector part, that is on the vector subspace and on the anti-quaternion directions $i\vec e_x,i\vec e_y,i\vec e_z$; the centre is the fixed subspace and the vector part the anti-fixed one. **The automorphism group of the block is the inner automorphisms, of dimension three and with the derivation algebra as Lie algebra, together with their coset through the natural conjugation, which is an outer automorphism.**

### The Structure Group

**Definition.** The **structure group** of the block is the group of invertible $\mathbb{C}$-linear maps that multiply the generic norm by a fixed scalar:

$$
\Gamma(\mathbb{B},\bullet)=\bigl\{g\in GL_{\mathbb{C}}(\mathbb{B}):\ \exists\,\nu(g)\in\mathbb{C}^{\times},\ \langle g\tilde Q_2\rangle_{\natural}=\nu(g)\,\langle\tilde Q_2\rangle_{\natural}\ \text{for all }\tilde Q_2\bigr\}.
$$

**Proposition.** The structure group contains the automorphism group, with $\nu=1$, and the scalar multiplications, with $\nu(\lambda)=\lambda^2$; it is the group of linear maps that preserve the norm form up to a scalar, and it is strictly larger than the automorphism group.

*Proof.* An automorphism preserves $\langle\cdot,\cdot\rangle_{\natural}$ by the theorem above, so $\operatorname{Aut}\subseteq\Gamma$ with $\nu=1$; a scalar $\lambda$ gives $\langle\lambda\tilde Q_2\rangle_{\natural}=\lambda^2\langle\tilde Q_2\rangle_{\natural}$. The condition $\langle g\tilde Q_2\rangle_{\natural}=\nu(g)\langle\tilde Q_2\rangle_{\natural}$ is the condition that $g$ preserve the quadratic form $\langle\cdot,\cdot\rangle_{\natural}$ up to scale, and the group of such linear maps is larger than the automorphism group: the scalar multiplications with $\lambda\neq\pm1$ preserve the form up to scale and are not automorphisms of the product.

**Theorem.** The Lie algebra of the structure group is

$$
\operatorname{Lie}\Gamma=\bigl\{X\in\operatorname{End}_{\mathbb{C}}(\mathbb{B}):\ b(X\tilde Q_2,\tilde Q_3)+\mathfrak{b}(\tilde Q_2,X\tilde Q_3)=\lambda\,\mathfrak{b}(\tilde Q_2,\tilde Q_3)\ \text{for some }\lambda\in\mathbb{C}\bigr\},
$$

where $\mathfrak{b}(\tilde Q_2,\tilde Q_3)=\tfrac12\bigl(\langle\tilde Q_2+\tilde Q_3\rangle_{\natural}-\langle\tilde Q_2\rangle_{\natural}-\langle\tilde Q_3\rangle_{\natural}\bigr)=\sum_\mu X_\mu Y_\mu$ is the polar form of the norm; it has complex dimension seven, the six-dimensional part of the maps skew for $b$ together with the one-dimensional part of the scalars.

*Proof.* Read the condition over the dual numbers $\mathbb{D}'=\mathbb{C}[\varepsilon]/(\varepsilon^2)$. The map $g=\mathrm{id}+\varepsilon X$ belongs to $\Gamma$ with multiplier $1+\lambda\varepsilon$ exactly when $\langle(\mathrm{id}+\varepsilon X)\tilde Q_2\rangle_{\natural}=(1+\lambda\varepsilon)\langle\tilde Q_2\rangle_{\natural}$ for every $\tilde Q_2$; since $\varepsilon^2=0$ the left side is $\langle\tilde Q_2\rangle_{\natural}+2\varepsilon\,b(X\tilde Q_2,\tilde Q_2)$, so the condition is $2b(X\tilde Q_2,\tilde Q_2)=\lambda \mathfrak{b}(\tilde Q_2,\tilde Q_2)$, whose polarisation in $\tilde Q_2$ is the displayed identity. In the coefficient basis, where the polar form is the identity, the same condition is $X^{\mathsf T}\mathrm{I}_4+\mathrm{I}_4X=\lambda\mathrm{I}_4$, that is

$$
X^{\mathsf T}+X=\lambda\mathrm{I}_4,
$$

whose solutions are the **skew** matrices, of dimension six, and the scalars, of dimension one.

**Remark (the two groups of the block).** The automorphism group of the block is a group of dimension three, the inner automorphisms together with the natural conjugation; the structure group is the larger group of dimension seven preserving the generic norm up to scale. **The automorphism group preserves the product, and the structure group preserves the norm; the second is the group of the quadratic structure and the first the group of the product**, and the derivations of the block are the Lie algebra of $\operatorname{Aut}$ and a three-dimensional subspace of the seven-dimensional Lie algebra of $\Gamma$.

## Summary

The multiplication operators of the block are $L^{\bullet}_{\tilde A}$ and $R^{\bullet}_{\tilde A}$, and they coincide because the product is commutative; they are half the sum of the plain operators, $L^{\bullet}_{\tilde A}=\tfrac12(L_{\tilde A}+R_{\tilde A})$, so $L_{\tilde A}+R_{\tilde A}=2L^{\bullet}_{\tilde A}$, with the factor of two. The trace is $4A_t$, the determinant is $A_t^2\langle\tilde A\rangle_{\natural}$, and the operator is invertible exactly when $A_t\neq0$ and $\langle\tilde A\rangle_{\natural}\neq0$, of rank three on the zero divisors with $A_t\neq0$, of rank two on the non-zero trace-zero elements and of rank zero at the origin. The composition is $L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde Q_1}=\tfrac14(L_{\tilde A\tilde Q_1}+L_{\tilde A}R_{\tilde Q_1}+R_{\tilde A}L_{\tilde Q_1}+R_{\tilde Q_1\tilde A})$ and does not equal $L^{\bullet}_{\tilde A\bullet\tilde Q_1}$, the witness being $\vec e_x,\vec e_x,\vec e_y$. Every operator is self-associate for the trace form, $\tau(L^{\bullet}_{\tilde A}\tilde Q_2,\tilde Q_3)=\tau(\tilde Q_2,L^{\bullet}_{\tilde A}\tilde Q_3)$, and the Jordan identity reads $[L^{\bullet}_{\tilde Q_2},L^{\bullet}_{\tilde Q_2\bullet\tilde Q_2}]=0$. The commutator of two operators is the inner derivation $\tfrac14\operatorname{ad}_{[\tilde A,\tilde Q_1]}$, and every derivation of the block is inner, so $\operatorname{Der}(\mathbb{B},\bullet)=\operatorname{Inn}(\mathbb{B},\bullet)\cong\mathfrak{sl}(2,\mathbb{C})$ of dimension three. The inner automorphisms are the conjugations by the units, of dimension three with the derivation algebra as Lie algebra, and the natural conjugation is an outer automorphism because it reverses the antisymmetric part; the structure group, the group of linear maps that multiply the norm by a scalar, is the larger group of dimension seven.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L^{\bullet}_{\tilde A}\tilde Q=\tilde A\bullet\tilde Q$, $R^{\bullet}_{\tilde A}\tilde Q=\tilde Q\bullet\tilde A$ | the multiplication operators of the block |
| $L^{\bullet}_{\tilde A}=R^{\bullet}_{\tilde A}=\tfrac12(L_{\tilde A}+R_{\tilde A})$ | coincidence of the two and the relation to the plain operators |
| $\operatorname{Tr}(L^{\bullet}_{\tilde A})=4A_t$, $\det(L^{\bullet}_{\tilde A})=A_t^2\langle\tilde A\rangle_{\natural}$ | trace and determinant |
| $(L^{\bullet}_{\tilde A})^{\approx}=L^{\bullet}_{\tilde A}$ | self-association for the trace form $\tau$ |
| $[L^{\bullet}_{\tilde Q_2},L^{\bullet}_{\tilde Q_2\bullet\tilde Q_2}]=0$ | the Jordan identity on the operators |
| $[L^{\bullet}_{\tilde A},L^{\bullet}_{\tilde Q_1}]=\tfrac14\operatorname{ad}_{[\tilde A,\tilde Q_1]}$ | the inner derivations |
| $\operatorname{Der}(\mathbb{B},\bullet)=\operatorname{Inn}(\mathbb{B},\bullet)\cong\mathfrak{sl}(2,\mathbb{C})$ | the derivation algebra, all derivations inner |
| $\operatorname{Ad}_{\tilde A}$, $\tilde Q_2\mapsto\tilde A\tilde Q_2\tilde A^{-1}$ | the inner automorphisms, $\operatorname{InnAut}(\mathbb{B},\bullet)\cong\mathbb{B}^{\times}/\mathbb{C}^{\times}\cong PGL(2,\mathbb{C})$ |
| $\Gamma=\{g:N\circ g=\nu\,N\}$ | the structure group, the norm similarities |

## Further Reading

- *Two-Sided Operators on the Biquaternion Algebra* and *One-Sided Operators on the General Plain Algebra of Biquaternions*, for the plain operators whose half-sum is the operator of the block.
- *The Trace Form and the Invariance of the Symmetric Plain Algebra*, for the trace form, the invariance and the operator trace.
- *Introduction to the Symmetric Plain Algebra*, for the matrices of the operators in the two models.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, for the generic trace and the generic norm preserved by the automorphisms.
- *The 12 Products of the Biquaternioid Complex Space*, for the placement of the block and its Jordan structure.
