# __$M_2(\mathbb{R})$ Model : The Sandwich and the Adjoint Action__

## Introduction

A **sandwich** is the linear map $X\mapsto AXB^{-1}$ of the matrix algebra, and the **adjoint action** is the special case $A=B$, the conjugation $X\mapsto AXA^{-1}$. The two-sided maps are the natural operators of the algebra: they are the ones that act by multiplication on the left and on the right, they contain the inner automorphisms, and their group is a quotient of $GL_2(\mathbb{R})\times GL_2(\mathbb{R})$.

This article computes the sandwich group, its determinant-preserving subgroup and the adjoint subgroup. The determinant-preserving subgroup is the orientation-preserving isometry group $SO(2,2)$ of the determinant form; its identity component is $(SL_2(\mathbb{R})\times SL_2(\mathbb{R}))/\{\pm(I,I)\}$. The adjoint action preserves the scalar line and the traceless subspace, and on the traceless subspace it is the Lorentz group $SO^{+}(2,1)$; the group $SL_2(\mathbb{R})$ is its double cover, as in *Split-Quaternion Rotations and the Lorentz Group*. The article closes with the action on the rulings of the null cone and with the enveloping algebra of the sandwiches.

The one-sided operators are *$M_2(\mathbb{R})$ Model : The Conjugations and the Adjoints*; the rank-one matrices are *$M_2(\mathbb{R})$ Model : Rank-One Matrices and the Null Cone*; and the biquaternion analogue is *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*.

## The Sandwich Group

**Definition.** For invertible matrices $A,B$ the **sandwich** is

$$
T_{A,B}(X)=AXB^{-1}.
$$

**Proposition (composition and inverse).** The sandwiches form a group:

$$
T_{A,B}\circ T_{C,D}=T_{AC,BD}, \qquad T_{A,B}^{-1}=T_{A^{-1},B}.
$$

**Proof.** Direct computation: $A(CXD^{-1})B^{-1}=(AC)X(DB)^{-1}$.

**Proposition (the kernel of the action).** The sandwiches satisfy

$$
T_{A,B}=T_{C,D} \quad\Longleftrightarrow\quad (C,D)=(\lambda A,\lambda B) \text{ for some } \lambda\in\mathbb{R}^\times.
$$

**Proof.** If $(C,D)=(\lambda A,\lambda B)$ then $CXD^{-1}=\lambda AX(\lambda B)^{-1}=AXB^{-1}$, since the two scalars cancel. Conversely, equality for all $X$ gives $C^{-1}AX=XD^{-1}B$ after multiplying on the left by $C^{-1}$ and on the right by $B$. Thus $L_{C^{-1}A}=R_{D^{-1}B}$. Taking traces gives $C^{-1}A=D^{-1}B$, and then $C^{-1}A$ commutes with every $X$, so it is scalar: $C^{-1}A=D^{-1}B=\lambda I$, that is $A=\lambda C$ and $B=\lambda D$.

**Corollary (the group of sandwiches).** The group of sandwiches is

$$
(GL_2(\mathbb{R})\times GL_2(\mathbb{R}))\big/\Delta, \qquad \Delta=\{(\lambda I,\lambda I)\},
$$

of dimension $8-1=7$. It is not $PGL_2(\mathbb{R})\times PGL_2(\mathbb{R})$: the overall scaling $X\mapsto\lambda X$ is a sandwich, with $A=\lambda I$ and $B=I$, and it is not an inner automorphism.

## The Determinant and the Isometry Group

**Proposition (the scaling of the determinant).** For every $X$,

$$
\det\bigl(T_{A,B}(X)\bigr)=\frac{\det A}{\det B}\det X.
$$

**Proof.** The determinant is multiplicative, and $\det B^{-1}=(\det B)^{-1}$.

**Corollary (the conformal character).** Every sandwich is conformal for the determinant form: if $B_{\det}$ is the polar form of the determinant, then

$$
B_{\det}\bigl(T_{A,B}(X),T_{A,B}(Y)\bigr)=\frac{\det A}{\det B}B_{\det}(X,Y).
$$

**Proof.** Both sides are the polar forms of the quadratic forms $\det\circ T_{A,B}$ and $(\det A/\det B)\det$, which agree by the proposition.

**Theorem (the determinant-preserving subgroup).** The sandwiches that preserve the determinant are exactly those with $\det A=\det B$, and they form a group isomorphic to the isometry group

$$
SO(2,2)=\{g\in O(2,2) : \det g=+1\}.
$$

Its identity component is

$$
SO^{+}(2,2)\cong \bigl(SL_2(\mathbb{R})\times SL_2(\mathbb{R})\bigr)\big/\{\pm(I,I)\}.
$$

**Proof.** The determinant is preserved exactly when $\det A=\det B$, by the proposition. The action is faithful on the quotient by $\Delta$ by the kernel proposition, and it lands in $SO(2,2)$ because it preserves the quadratic form and has determinant one as an operator on the four-dimensional space. The group $\{(\det A=\det B)\}/\Delta$ has dimension $8-1-1=6$, the dimension of $SO(2,2)$, and it has two components according to the sign of the common determinant. The map to $SO(2,2)$ is injective, so its image is an open subgroup of the same dimension; an open subgroup is also closed, hence a union of components. The two components of the source map to the two components of the target, since a path from a pair with negative common determinant to $(I,I)$ would make the determinant pass through zero. So the image is all of $SO(2,2)$.

For the identity component, write a pair with $\det A=\det B=d>0$ as $A=\sqrt d\,A'$ and $B=\sqrt d\,B'$ with $A',B'\in SL_2(\mathbb{R})$. The diagonal scaling identifies $(A,B)$ with $(A',B')$, and the only remaining identification is $(A',B')\sim(-A',-B')$. This gives $(SL_2\times SL_2)/\{\pm(I,I)\}$. Its dimension is $3+3=6$, since the kernel $\{\pm(I,I)\}$ is discrete.

**Remark (the two components).** The component with $\det A=\det B<0$ is the coset of the identity component represented by $A=B=\operatorname{diag}(1,-1)$, whose adjoint action negates $q_x$ and $q_y$. In terms of the rulings of the null quadric, this element reverses the orientation of both ruling circles, so it is not in the identity component. The full isometry group $SO(2,2)$ has two components, and the identity component is the one containing the sandwiches with both determinants positive.

## The Adjoint Action

**Definition.** The **adjoint action** is the sandwich with $A=B$:

$$
\operatorname{Ad}_A(X)=AXA^{-1}.
$$

**Proposition (the kernel and the image).** The kernel of $A\mapsto\operatorname{Ad}_A$ is the group of scalar matrices, and the image is

$$
GL_2(\mathbb{R})/\mathbb{R}^\times I=PGL_2(\mathbb{R}),
$$

of dimension three. It has two components; its identity component is $PSL_2(\mathbb{R})=SL_2(\mathbb{R})/\{\pm I\}$.

**Proof.** $\operatorname{Ad}_A=\operatorname{id}$ means $AX=XA$ for all $X$, so $A$ is scalar. The quotient is $PGL_2$ by definition, and it has two components: $GL_2$ has two, and scaling by $\lambda$ multiplies the determinant by $\lambda^2>0$, so it preserves the sign of the determinant. A class with a representative of positive determinant is connected to the identity through scalings and the connected group $SL_2$; a class of negative determinant is not. So the identity component is the image of $SL_2$, which is $PSL_2$.

**Theorem (the Lorentz group).** The adjoint action fixes the identity and preserves the traceless subspace $V$. On $V$ it preserves the determinant form, of signature $(2,1)$, and the map

$$
PGL_2(\mathbb{R})\longrightarrow SO(2,1)
$$

is an isomorphism. On the identity components it restricts to an isomorphism $PSL_2(\mathbb{R})\to SO^{+}(2,1)$, and the map $SL_2(\mathbb{R})\to SO^{+}(2,1)$ is a double cover with kernel $\{\pm I\}$.

**Proof.** $\operatorname{Ad}_A(I)=I$ and $\operatorname{Ad}_A$ preserves the trace, so it preserves $V$. On $V$ the determinant restricts to the form $\operatorname{diag}(1,-1,-1)$ in the basis $\vec e_x,\vec e_y,\vec e_z$, of signature $(2,1)$. The image is a subgroup of $SO(2,1)$ of dimension three; it is open, hence a union of components, and it has two components because $GL_2$ has two. So it is all of $SO(2,1)$, and the identity components give $PSL_2\cong SO^{+}(2,1)$. The kernel on $SL_2$ is $\{\pm I\}$ by the proposition.

**Corollary (the split-quaternion double cover).** Under the identification of the norm-one group with $SL_2(\mathbb{R})$, the adjoint action is the conjugation of *Split-Quaternion Rotations and the Lorentz Group*, and the double cover $SL_2(\mathbb{R})\to SO^{+}(2,1)$ is the one computed there.

**Proof.** The unit group of the algebra is the set of matrices of non-zero determinant, and the norm-one group is $SL_2(\mathbb{R})$; conjugation by a unit is $\operatorname{Ad}_A$. The identification with the Lorentz group is the theorem.

## The Action on the Rulings

**Proposition (the action on rank-one matrices).** For $X=uv^{\mathsf T}$,

$$
T_{A,B}(X)=(Au)\bigl(B^{-\mathsf T}v\bigr)^{\mathsf T}.
$$

**Proof.** $Auv^{\mathsf T}B^{-1}=Au\,(B^{-\mathsf T}v)^{\mathsf T}$, since $(B^{-1})^{\mathsf T}=B^{-\mathsf T}$.

**Corollary (the action on the quadric).** On the projective null quadric $\mathbb{R}P^1\times\mathbb{R}P^1$, the sandwich acts by

$$
([u],[v])\longmapsto\bigl([Au],[B^{-\mathsf T}v]\bigr).
$$

**Proof.** The image line of $X$ is $[Au]$ and its kernel line is $[B^{-\mathsf T}v]$, and the two determine the point of the quadric by *$M_2(\mathbb{R})$ Model : Rank-One Matrices and the Null Cone*.

So the two rulings of the quadric are moved independently, the first by $A$ and the second by $B^{-\mathsf T}$. The adjoint action moves both rulings by the same projective transformation: it is the diagonal of the Möbius group inside $PGL_2\times PGL_2$. That is why it preserves the traceless part and acts on it as a Lorentz transformation.

## The Enveloping Algebra

**Theorem (the sandwiches span the full endomorphism algebra).** The linear span of the sandwiches is

$$
\operatorname{span}\{T_{A,B}\}=\operatorname{End}\bigl(M_2(\mathbb{R})\bigr)\cong M_4(\mathbb{R})\cong M_2(\mathbb{R})\otimes M_2(\mathbb{R})^{\mathrm{op}},
$$

of dimension sixteen.

**Proof.** The map $A\otimes B^{\mathsf T}\mapsto T_{A,B}$ is a linear isomorphism from $M_2\otimes M_2$ onto the span, since the two spaces have dimension sixteen and the map is injective: if $\sum A_iXB_i=0$ for all $X$, the matrix units $X=E_{jk}$ give $\sum A_iE_{jk}B_i=0$ for all $j,k$, which forces the tensor to vanish. The identification $M_2\otimes M_2^{\mathrm{op}}\cong M_4(\mathbb{R})$ is the standard isomorphism for a central simple algebra.

**Corollary (the Kronecker form).** With the column-stacking vectorisation,

$$
\operatorname{vec}\bigl(T_{A,B}(X)\bigr)=\bigl(B^{-\mathsf T}\otimes A\bigr)\operatorname{vec}X.
$$

**Proof.** The identity $\operatorname{vec}(AXB)=(B^{\mathsf T}\otimes A)\operatorname{vec}X$ is applied to $B^{-1}$ in place of $B$.

**Remark (the group inside the algebra).** The group of invertible sandwiches has dimension seven, while the algebra of all sandwiches has dimension sixteen. The gap is the same as in the biquaternion category: the sandwich group is a small group acting on a four-dimensional space, and its linear span is the full endomorphism algebra of that space. The one-sided operators $L_A$ and $R_B$ span a seven-dimensional subspace, since the only relation between them is $L_{\lambda I}=R_{\lambda I}$, and the products of a left and a right operator fill the whole sixteen-dimensional algebra.

## The Scalar–Vector Splitting

**Proposition (when the splitting is preserved).** A sandwich preserves the scalar line $S$ exactly when $AB^{-1}$ is scalar, and then it preserves $V$ as well; in that case it is a scalar multiple of an inner automorphism:

$$
T_{A,B}=\lambda\,\operatorname{Ad}_B, \qquad A=\lambda B.
$$

**Proof.** $T_{A,B}(I)=AB^{-1}$, so the scalar line is preserved exactly when $AB^{-1}=\lambda I$. Then $A=\lambda B$ and $T_{A,B}(X)=\lambda BXB^{-1}$. The subspace $V$ is the kernel of the trace, and $T_{A,B}$ preserves it exactly when $\operatorname{tr}(AXB^{-1})=0$ for every traceless $X$. Since $\operatorname{tr}(AXB^{-1})=\operatorname{tr}((B^{-1}A)X)$, this functional vanishes on the trace-zero hyperplane exactly when $B^{-1}A$ is scalar, which is the same condition.

**Corollary (the generic sandwich does not preserve the splitting).** A sandwich with $AB^{-1}$ not scalar moves the scalar line to the line $\mathbb{R}AB^{-1}$ and does not preserve the traceless subspace.

**Proof.** The image of the scalar line is the line spanned by $T_{A,B}(I)=AB^{-1}$, and the traceless subspace is not preserved by the previous proposition.

So the determinant-preserving sandwiches of the theorem are not the same as the sandwiches preserving the algebra's scalar–vector decomposition. The isometry group $SO(2,2)$ is larger than the group of scalar multiples of inner automorphisms, and the extra transformations mix the scalar direction with the traceless directions.

## Summary

The sandwiches $T_{A,B}(X)=AXB^{-1}$ form the group $(GL_2\times GL_2)/\Delta$ of dimension seven, with $\Delta$ the diagonal scalars. Every sandwich scales the determinant by $\det A/\det B$, and the sandwiches with $\det A=\det B$ are exactly the orientation-preserving isometries of the determinant form: they form $SO(2,2)$, whose identity component is $(SL_2\times SL_2)/\{\pm(I,I)\}\cong SO^{+}(2,2)$.

The adjoint action has kernel the scalars and image $PGL_2\cong SO(2,1)$. It fixes the identity, preserves the traceless subspace, and acts there as $SO(2,1)$; on the identity components it is $PSL_2\cong SO^{+}(2,1)$, and the map $SL_2\to SO^{+}(2,1)$ is the double cover of the Lorentz group. On the null quadric the sandwich moves the two rulings independently, by $A$ and by $B^{-\mathsf T}$, and the sandwiches span the full endomorphism algebra $M_4(\mathbb{R})$. A sandwich preserves the scalar–vector splitting only when it is a scalar multiple of an inner automorphism.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $T_{A,B}$ | the sandwich $X\mapsto AXB^{-1}$ | this article |
| $\operatorname{Ad}_A$ | the adjoint action $X\mapsto AXA^{-1}$ | this article |
| $\Delta$ | the diagonal scalars $(\lambda I,\lambda I)$ | this article |
| $B_{\det}$ | the determinant form of signature $(2,2)$ | *$M_2(\mathbb{R})$ Model : The Conjugations and the Adjoints* |
| $SO^{+}(2,2)$ | the identity component of the isometry group of $B_{\det}$ | this article |
| $SO(2,1)$ | the orientation-preserving isometry group of the traceless part | this article |
| $SO^{+}(2,1)$ | the Lorentz group of signature $(2,1)$ | *Split-Quaternion Rotations and the Lorentz Group* |
| $\operatorname{vec}$ | column-stacking vectorisation | this article |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the endomorphism algebra of a matrix algebra and the sandwich representation.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the isometry groups of the split forms and the isomorphism $SO^{+}(2,2)\cong(SL_2\times SL_2)/\{\pm1\}$.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the adjoint representation and the double cover of the Lorentz group.
