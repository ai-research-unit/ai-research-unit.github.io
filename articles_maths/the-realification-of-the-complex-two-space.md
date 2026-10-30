# __The Realification of $\mathbb{C}^2$__

## Introduction

The realification of $\mathbb{C}^2$ is the real vector space $\mathbb{C}^2_{\mathbb{R}}$ obtained by forgetting the multiplication by $i$ and keeping only the multiplication by real scalars. As a set and as an abelian group it is the same space; as a vector space it is $\mathbb{R}^4$. This article reads the complex space through its realification: it fixes the real basis and the real coordinates, states what the complex structure adds, separates the complex-linear from the conjugate-linear maps, and computes the real picture of the three canonical forms. It closes with the dictionary between the complex statements and the real ones.

The article is the bridge between the space of the previous article and the real topology, analysis and geometry that follow. It does not restate the general theory of the change of scalars, which is *The Realification and the Effect of the Change of Scalars on the Complexoid*; it reads that theory on the two-dimensional complex space. The forms are defined in *Complex Two-Space* and computed in *The Three Canonical Forms on $\mathbb{C}^2$*; the topology is *The Topology of $\mathbb{C}^2$*.

**The guiding statement is that the realification loses exactly one datum, the operator $J$, and that every complex notion is a real notion plus a condition of compatibility with $J$.** The article makes that statement precise in the four places where it bears: the dimensions, the maps, the forms and the dictionary.

## The Underlying Real Space

**The realification is the same set with the scalar multiplication restricted to $\mathbb{R}$; it is a real vector space of dimension $4$, and it carries no canonical complex structure.**

**Definition.** Let $V=\mathbb{C}^2$. The **realification** $V_{\mathbb{R}}$ is the abelian group $(V,+)$ with the scalar multiplication
$$
\mathbb{R}\times V\longrightarrow V,\qquad (a,Q)\longmapsto aQ,
$$
where the right side is the complex product of $Q$ by the real number $a$. The complex multiplication is forgotten as a structure and remembered as the operator $J$ of *Complex Two-Space*.

**Proposition (the dimension doubles).** For every finite-dimensional complex vector space $V$, $\dim_{\mathbb{R}}V_{\mathbb{R}}=2\dim_{\mathbb{C}}V$. In particular $\dim_{\mathbb{R}}\mathbb{C}^2_{\mathbb{R}}=4$.

*Proof.* A complex basis $v_1,\dots,v_n$ gives the real basis $v_1,iv_1,\dots,v_n,iv_n$: it spans, since every complex coefficient splits into its real and imaginary parts, and it is independent over $\mathbb{R}$, since a real relation separates into the real and imaginary parts of a complex relation. Hence the real dimension is $2n$.

The real basis and the real coordinates are those of *Complex Two-Space*:
$$
Q=q_{\blacktriangle}e_1+q'_{\blacktriangle}(ie_1)+q_{\blacktriangledown}e_2+q'_{\blacktriangledown}(ie_2),\qquad Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle},\quad Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}.
$$
The realification is recorded by the following table.

| Complex object | Real object |
|---|---|
| the set $\mathbb{C}^2$ | the set $\mathbb{R}^4$ |
| addition | addition |
| multiplication by $\lambda\in\mathbb{C}$ | multiplication by $\operatorname{Re}\lambda$ and by $\operatorname{Im}\lambda$ composed with $J$ |
| the complex basis $e_1,e_2$ | the real basis $e_1,ie_1,e_2,ie_2$ |
| $\dim_{\mathbb{C}}=2$ | $\dim_{\mathbb{R}}=4$ |
| a complex subspace $W$ | a real subspace $W$ with $JW=W$ |

**Remark (the realification is not a section of the complexification).** The passage from a complex space to a real one has no canonical inverse. **A real space of dimension $4$ is not a complex space until an operator $J$ with $J^2=-I$ is chosen**, and the choice is an extra datum, not a reconstruction. The real space $\mathbb{R}^4$ carries a whole family of complex structures, of real dimension $8$: the homogeneous space $\mathrm{GL}_4(\mathbb{R})/\mathrm{GL}_2(\mathbb{C})$, where $\mathrm{GL}_2(\mathbb{C})$ is the stabiliser of the standard $J$ in $\mathrm{GL}_4(\mathbb{R})$.

**Proposition (the complex structures form one orbit).** Every two complex structures on $\mathbb{R}^4$ are conjugate by a real-linear automorphism, and the set of them is $\mathrm{GL}_4(\mathbb{R})/\mathrm{GL}_2(\mathbb{C})$, of real dimension $8$.

*Proof.* The group $\mathrm{GL}_4(\mathbb{R})$ acts on the set of operators $J$ with $J^2=-I$ by $J\mapsto AJA^{-1}$, and the action is transitive: two such operators are both conjugate to the standard one after a choice of a real basis adapted to each. The stabiliser of the standard $J$ is the set of real matrices commuting with $J$, which is $\mathrm{GL}_2(\mathbb{C})$ by the proposition of the next section. The dimension is $16-8=8$.

## Complex-Linear against Conjugate-Linear Maps

**A real-linear map of $\mathbb{C}^2$ is complex-linear exactly when it commutes with $J$ and conjugate-linear exactly when it anticommutes, and every real-linear map is the sum of one of each kind.**

**Definition.** Let $T:V\to V$ be real-linear. The map is **complex-linear** when $T(\lambda Q)=\lambda T(Q)$ for every $\lambda\in\mathbb{C}$, and **conjugate-linear** when $T(\lambda Q)=\overline{\lambda}T(Q)$ for every $\lambda\in\mathbb{C}$.

**Proposition (the two commutation rules).** A real-linear $T$ is complex-linear exactly when $TJ=JT$, and conjugate-linear exactly when $TJ=-JT$.

*Proof.* The complex-linear condition is equivalent to its case $\lambda=i$, which is $T(iQ)=iT(Q)$, that is $TJ=JT$. The conjugate-linear condition is $T(iQ)=-iT(Q)$, that is $TJ=-JT$. The case of a general $\lambda$ follows from the case $\lambda=i$ together with real linearity: $\lambda=a+ib$ gives $T(\lambda Q)=aT(Q)+bT(iQ)=aT(Q)+bJT(Q)$, which is $\lambda T(Q)$ in the first case and $\bar\lambda T(Q)$ in the second.

**Theorem (the splitting of the real endomorphisms).** Every real-linear $T:V\to V$ is uniquely
$$
T=T_++T_-,\qquad T_+=\tfrac12(T-JTJ),\qquad T_-=\tfrac12(T+JTJ),
$$
with $T_+$ complex-linear and $T_-$ conjugate-linear. Hence
$$
\operatorname{End}_{\mathbb{R}}(V)=\operatorname{End}_{\mathbb{C}}(V)\oplus\operatorname{Hom}_{\bar{\mathbb{C}}}(V,V),
$$
and the two summands have real dimensions $8$ and $8$.

*Proof.* The operators $T_+$ and $T_-$ are real-linear and satisfy $T_++T_-=T$ and $T_+-T_-=JTJ$. For the commutation, compute
$$
T_+J=\tfrac12(TJ-JTJ^2)=\tfrac12(TJ+JT)=J\tfrac12(T-JTJ)=JT_+,
$$
using $J^2=-I$, so $T_+$ is complex-linear; and
$$
T_-J=\tfrac12(TJ+JTJ^2)=\tfrac12(TJ-JT)=-J\tfrac12(T+JTJ)=-JT_-,
$$
so $T_-$ is conjugate-linear. Uniqueness follows because a map that is both complex-linear and conjugate-linear satisfies $T(iQ)=iT(Q)=-iT(Q)$, hence $T=0$. The dimensions are those of $M_2(\mathbb{C})$ over $\mathbb{R}$, twice.

**Remark (the sum is not a sum of algebras).** The product of two conjugate-linear maps is complex-linear, because $T_-S_-(\lambda Q)=T_-(S_-(\lambda Q))=T_-(\bar\lambda S_-(Q))=\bar{\bar\lambda}T_-(S_-(Q))=\lambda T_-S_-(Q)$. **The subspace $\operatorname{Hom}_{\bar{\mathbb{C}}}$ is an $\operatorname{End}_{\mathbb{C}}$-bimodule and not a subalgebra**, and $\operatorname{End}_{\mathbb{R}}$ is not the direct product of the two summands as a ring. The grading by the two kinds is a $\mathbb{Z}_2$-grading of the algebra, with the even part $\operatorname{End}_{\mathbb{C}}$ and the odd part $\operatorname{Hom}_{\bar{\mathbb{C}}}$.

**Proposition (the matrix form).** In the standard complex basis, every real-linear $T$ is
$$
T(Q)=AQ+B\overline{Q},\qquad A,B\in M_2(\mathbb{C}),
$$
where $\overline{Q}=(\overline{Q}_{\blacktriangle},\overline{Q}_{\blacktriangledown})$. The map is complex-linear exactly when $B=0$ and conjugate-linear exactly when $A=0$.

*Proof.* The expression is real-linear for every pair $A,B$. Conversely, a real-linear map is determined by its values on $e_1,ie_1,e_2,ie_2$, and the four values are the columns of a real $4\times4$ matrix; the pair $(A,B)$ collects the images of $e_1,e_2$ and of $ie_1,ie_2$ in the complex basis, and the two collections determine the map. The conditions follow from $T(iQ)=iAQ-iB\overline{Q}$ compared with $iT(Q)=iAQ+iB\overline{Q}$ and with $-iT(Q)=-iAQ-iB\overline{Q}$.

**Remark (the conjugate space).** The conjugate vector space $\overline{V}$ has the same abelian group and the scalar multiplication $\lambda\cdot v=\overline{\lambda}v$. **A conjugate-linear map $V\to V$ is the same thing as a complex-linear map $\overline{V}\to V$**, and the identity map $V\to\overline{V}$ is conjugate-linear. The two summands of the splitting are $\operatorname{Hom}_{\mathbb{C}}(V,V)$ and $\operatorname{Hom}_{\mathbb{C}}(\overline{V},V)$, each of complex dimension $4$.

## The Realification of the Three Forms

**Each complex form realifies to two real forms, its real and imaginary parts, and the pair is not arbitrary: the two parts are related by the complex structure, and their signatures are the real data that the complex form alone does not display.**

**Definition.** Let $F$ be a $\mathbb{C}$-bilinear form on $V$. Its **realification** is the pair of real bilinear forms $\operatorname{Re}F$ and $\operatorname{Im}F$. For the Hermitian form $H$, the realification is the pair $\operatorname{Re}H$ and $\operatorname{Im}H$; the form is not $\mathbb{C}$-bilinear, and its real picture is read with the same formulas.

**Proposition (the Cauchy–Riemann compatibility).** For a $\mathbb{C}$-bilinear $F$,
$$
\operatorname{Re}F(JQ_1,Q_2)=-\operatorname{Im}F(Q_1,Q_2),\qquad \operatorname{Im}F(JQ_1,Q_2)=\operatorname{Re}F(Q_1,Q_2),
$$
and the same two identities hold with $J$ in the second slot.

*Proof.* $F(JQ_1,Q_2)=F(iQ_1,Q_2)=iF(Q_1,Q_2)$; taking real and imaginary parts gives the two identities. The second slot is the same computation with $F(Q_1,iQ_2)=iF(Q_1,Q_2)$.

**Theorem (the signatures).** On the real space $\mathbb{R}^4$:

- $\operatorname{Re}H$ is symmetric and positive definite, of signature $(4,0)$;
- $\operatorname{Im}H$ is alternating and nondegenerate, of rank $4$;
- $\operatorname{Re}B$ and $\operatorname{Im}B$ are symmetric and nondegenerate, each of signature $(2,2)$;
- $\operatorname{Re}\omega$ and $\operatorname{Im}\omega$ are alternating and nondegenerate, each of rank $4$.

*Proof.* In the real basis $e_1,ie_1,e_2,ie_2$, the form $\operatorname{Re}H$ is $q_{\blacktriangle}^2+{q'_{\blacktriangle}}^2+q_{\blacktriangledown}^2+{q'_{\blacktriangledown}}^2$, the identity matrix. The form $\operatorname{Im}H$ is $-(dq_{\blacktriangle}\wedge dq'_{\blacktriangle}+dq_{\blacktriangledown}\wedge dq'_{\blacktriangledown})$, whose matrix is block diagonal with two copies of $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, of total Pfaffian $1$. The form $\operatorname{Re}B$ is $q_{\blacktriangle}^2-{q'_{\blacktriangle}}^2+q_{\blacktriangledown}^2-{q'_{\blacktriangledown}}^2$, of signature $(2,2)$; the form $\operatorname{Im}B$ is $2q_{\blacktriangle}q'_{\blacktriangle}+2q_{\blacktriangledown}q'_{\blacktriangledown}$, whose matrix has the two eigenvalues $\pm1$ in each coordinate plane, again of signature $(2,2)$. The forms $\operatorname{Re}\omega$ and $\operatorname{Im}\omega$ are computed in *The Three Canonical Forms on $\mathbb{C}^2$*, where their Pfaffians are $1$.

The four real pictures are collected below. The notation $\Omega$ is the Kähler form,
$$
\Omega=-\operatorname{Im}H=dq_{\blacktriangle}\wedge dq'_{\blacktriangle}+dq_{\blacktriangledown}\wedge dq'_{\blacktriangledown},
$$
chosen with the sign that makes it positive on the complex lines.

| Complex form | Real part | Imaginary part | Reading |
|---|---|---|---|
| $H$ | $\operatorname{Re}H=g$, signature $(4,0)$ | $\operatorname{Im}H=-\Omega$, symplectic | Euclidean metric and Kähler form |
| $B$ | $\operatorname{Re}B$, signature $(2,2)$ | $\operatorname{Im}B$, signature $(2,2)$ | two indefinite metrics, related by $J$ |
| $\omega$ | $\operatorname{Re}\omega$, symplectic | $\operatorname{Im}\omega$, symplectic | two symplectic forms, related by $J$ |

**Theorem (the Hermitian form is the metric and the Kähler form).** The Hermitian form is recovered from its real part and the complex structure by
$$
H(Q_1,Q_2)=g(Q_1,Q_2)-i\Omega(Q_1,Q_2),\qquad g=\operatorname{Re}H,\qquad \Omega(Q_1,Q_2)=g(JQ_1,Q_2).
$$

*Proof.* The first identity is the definition of the real and imaginary parts. For the second, $g(JQ_1,Q_2)=\operatorname{Re}H(iQ_1,Q_2)=\operatorname{Re}\bigl(iH(Q_1,Q_2)\bigr)=-\operatorname{Im}H(Q_1,Q_2)=\Omega(Q_1,Q_2)$.

**Remark (a complex form is two real forms plus a compatibility).** The pair $(\operatorname{Re}F,\operatorname{Im}F)$ is not an arbitrary pair: it satisfies the two Cauchy–Riemann identities above, which say that $\operatorname{Im}F$ is determined by $\operatorname{Re}F$ and $J$. **Conversely, a real bilinear form $G$ determines the complex bilinear form $F=G-iG(J\cdot,\cdot)$ exactly when $G$ is compatible with $J$**, and the compatibility is the symmetry of $F$ in the symmetric case or its alternation in the alternating case. The realification of a complex form is therefore a pair with a constraint, and the constraint is the complex structure again.

## The Dictionary

**Every complex statement has a real translation, and the translation is mechanical once the four primitives — the dimension, the subspace, the map and the form — are fixed.**

The dictionary is gathered in one table. The left column is the complex statement, the right column its real reading on $V_{\mathbb{R}}$ with the operator $J$; the third column records where the real statement is proved or used.

| Complex statement | Real statement | Reference |
|---|---|---|
| a complex vector space $V$ | a real space $V_{\mathbb{R}}$ with $J^2=-I$ | this article |
| $\dim_{\mathbb{C}}V=n$ | $\dim_{\mathbb{R}}V=2n$ | this article |
| a complex subspace $W$ | a real subspace with $JW=W$ | *The Subspaces of $\mathbb{C}^2$* |
| a complex line | a $J$-invariant real $2$-plane | *The Subspaces of $\mathbb{C}^2$* |
| a complex-linear map | a real-linear map with $TJ=JT$ | this article |
| a conjugate-linear map | a real-linear map with $TJ=-JT$ | this article |
| a Hermitian form $H$ | a pair $(g,\Omega)$ with $g$ positive definite, $\Omega$ symplectic, $\Omega=g(J\cdot,\cdot)$ | this article |
| a unitary operator | an orthogonal operator with $TJ=JT$ | *The Classical Groups of $\mathbb{C}^2$* |
| $\operatorname{tr}_{\mathbb{R}}T=2\operatorname{Re}\operatorname{tr}_{\mathbb{C}}T$ | the real trace is twice the real part of the complex one | *The Endomorphisms of $\mathbb{C}^2$* |
| $\det_{\mathbb{R}}T=\lvert\det_{\mathbb{C}}T\rvert^2$ | the real determinant is the squared modulus | *The Endomorphisms of $\mathbb{C}^2$* |
| a holomorphic map | a real differentiable map satisfying the Cauchy–Riemann equations | *Analysis on $\mathbb{C}^2$* |
| the holomorphic form $\omega$ | the pair $(\operatorname{Re}\omega,\operatorname{Im}\omega)$, with $\omega\wedge\overline{\omega}=2\Omega^2$ | *The Three Canonical Forms on $\mathbb{C}^2$* |
| a Kähler structure | $(g,\Omega,J)$ with $\Omega=g(J\cdot,\cdot)$ and $d\Omega=0$ | *The Flat Kähler Structure of $\mathbb{C}^2$* |

**Proposition (the two traces and the two determinants).** For $T\in\operatorname{End}_{\mathbb{C}}(V)$,
$$
\operatorname{tr}_{\mathbb{R}}T=2\operatorname{Re}\operatorname{tr}_{\mathbb{C}}T,\qquad \det_{\mathbb{R}}T=\lvert\det_{\mathbb{C}}T\rvert^2.
$$

*Proof.* In a complex basis, $T$ is a complex matrix. Its realification is the block matrix obtained by replacing each entry $a+ib$ by the $2\times2$ block $\begin{pmatrix}a&-b\\b&a\end{pmatrix}$. The trace of the block matrix is twice the sum of the real parts of the diagonal entries. The determinant of the block matrix is the squared modulus of the complex determinant: the block matrix is the composition of the complex matrix with the identification $\mathbb{C}^n\cong\mathbb{R}^{2n}$, and its determinant is the product of the two complex eigenvalues counted with the real and imaginary parts, which gives $\prod_k\lvert\lambda_k\rvert^2$.

## The Trap of the Count of Operations

**Counting real dimensions suggests that the complex structure adds freedom, while it in fact removes it: the complex-linear maps are a subspace of the real-linear ones, not a complement.**

The real algebra $\operatorname{End}_{\mathbb{R}}(\mathbb{C}^2)$ has dimension $16$. The complex-linear maps form the subspace $\operatorname{End}_{\mathbb{C}}(\mathbb{C}^2)$ of dimension $8$, and the conjugate-linear maps form another subspace of dimension $8$; the two sum to the whole. **The complex structure does not add eight dimensions of freedom: it cuts the space of operators into two halves and selects one of them as the complex-linear maps.** The mistake of counting $16$ as "twice the complex dimension" and concluding that the complex theory is richer is the trap.

The same trap appears on the scalars. Multiplication by a complex number $\lambda=a+ib$ is the real-linear map $a\,\mathrm{id}+bJ$, two real parameters, not one. A complex vector space of dimension $n$ has $2n$ real parameters per vector, and a complex-linear map has $2n^2$ real parameters, against $4n^2$ for a real-linear one. **The factor is not a gain in structure but a loss of maps.**

**Remark (the realification is not full).** The realification functor from complex vector spaces to real vector spaces is faithful but not full: it has more maps on the real side. **A statement about $\mathbb{C}^2$ is a statement about a real space together with a privileged operator, and the privileged operator is not visible to the real topology.** That is why the topology of $\mathbb{C}^2$ is the topology of $\mathbb{R}^4$ and carries no trace of the complex structure, while the analysis and the geometry of $\mathbb{C}^2$ do.

## Summary

The realification of $\mathbb{C}^2$ is the real vector space $\mathbb{R}^4$ obtained by restricting the scalars to $\mathbb{R}$; the complex basis $e_1,e_2$ becomes the real basis $e_1,ie_1,e_2,ie_2$, and the dimension doubles from $2$ to $4$. The information lost in the passage is the complex structure $J$, the real operator $JQ=iQ$ with $J^2=-I$; a real space of dimension $4$ becomes complex only when such an operator is chosen, and the complex structures on $\mathbb{R}^4$ form the homogeneous space $\mathrm{GL}_4(\mathbb{R})/\mathrm{GL}_2(\mathbb{C})$ of dimension $8$.

A real-linear endomorphism is complex-linear exactly when $TJ=JT$ and conjugate-linear exactly when $TJ=-JT$; every one splits uniquely as $T=T_++T_-$ with $T_\pm=\tfrac12(T\mp JTJ)$, so $\operatorname{End}_{\mathbb{R}}=\operatorname{End}_{\mathbb{C}}\oplus\operatorname{Hom}_{\bar{\mathbb{C}}}$ with dimensions $16=8+8$. In a complex basis every real-linear map is $T(Q)=AQ+B\overline{Q}$, with $B=0$ for the complex-linear maps and $A=0$ for the conjugate-linear ones.

Each complex form realifies to its real and imaginary parts: $\operatorname{Re}H$ is the positive definite metric of signature $(4,0)$, $\operatorname{Im}H=-\Omega$ is the Kähler form, $\operatorname{Re}B$ and $\operatorname{Im}B$ are symmetric of signature $(2,2)$, and $\operatorname{Re}\omega$ and $\operatorname{Im}\omega$ are symplectic. The Hermitian form is recovered by $H=g-i\Omega$ with $\Omega(Q_1,Q_2)=g(JQ_1,Q_2)$, and the real traces and determinants are $\operatorname{tr}_{\mathbb{R}}=2\operatorname{Re}\operatorname{tr}_{\mathbb{C}}$ and $\det_{\mathbb{R}}=\lvert\det_{\mathbb{C}}\rvert^2$. The dictionary between the complex and the real statements is mechanical, and the count of real dimensions records a loss of structure rather than a gain of freedom.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V_{\mathbb{R}}$ | the realification of $V=\mathbb{C}^2$, the real space $\mathbb{R}^4$ |
| $e_1,ie_1,e_2,ie_2$ | the real basis |
| $J$ | the complex structure, $JQ=iQ$, $J^2=-I$ |
| $\operatorname{End}_{\mathbb{C}}(V)$ | the complex-linear endomorphisms, $M_2(\mathbb{C})$, real dimension $8$ |
| $\operatorname{Hom}_{\bar{\mathbb{C}}}(V,V)$ | the conjugate-linear endomorphisms, real dimension $8$ |
| $T_\pm=\tfrac12(T\mp JTJ)$ | the complex-linear and conjugate-linear parts of a real-linear $T$ |
| $g=\operatorname{Re}H$ | the Euclidean metric, signature $(4,0)$ |
| $\Omega=-\operatorname{Im}H$ | the Kähler form, $dq_{\blacktriangle}\wedge dq'_{\blacktriangle}+dq_{\blacktriangledown}\wedge dq'_{\blacktriangledown}$ |
| $\omega$ | the holomorphic symplectic form, $\omega\wedge\overline{\omega}=2\Omega^2$ |
| $\overline{V}$ | the conjugate space, with $\lambda\cdot v=\overline{\lambda}v$ |

## Further Reading

- [Complex Two-Space](the-complex-two-space.html), the previous article of this category, for the space, the bases and the complex structure.
- [The Three Canonical Forms on $\mathbb{C}^2$](the-three-canonical-forms-on-the-complex-two-space.html), below in this category, for the Gram matrices and the computations of the real and imaginary parts.
- [The Subspaces of $\mathbb{C}^2$](the-subspaces-of-the-complex-two-space.html), below in this category, for the $J$-invariant and the totally real subspaces.
- [The Endomorphisms of $\mathbb{C}^2$](the-endomorphisms-of-the-complex-two-space.html), below in this category, for the matrix form $T(Q)=AQ+B\overline{Q}$ and the trace and determinant identities.
- [The Realification and the Effect of the Change of Scalars on the Complexoid](the-realification-and-the-effect-of-the-change-of-scalars-on-the-complexoid.html), for the general theory of the change of scalars read on an algebra rather than on a space.
- [The Flat Kähler Structure of $\mathbb{C}^2$](the-flat-kahler-structure-of-the-complex-two-space.html), for the metric, the Kähler form and the isometries.
- [Real Topology](real-topology.html), for the topology of $\mathbb{R}^4$, which is the topology of the realification.
