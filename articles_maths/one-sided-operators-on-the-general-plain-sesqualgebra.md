# __One-Sided Operators on the General Plain Sesqualgebra__

## Introduction

Let $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the biquaternion algebra with its Hermitian conjugation ${}^{*}$ and the positive definite general plain sesquilinear form $(\tilde Q,\tilde{Q}_1)=\mathrm{Sc}(\tilde{Q}^{*}\tilde{Q}_1)$, whose Gram matrix in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ is the identity. For $\tilde Q_3\in\mathbb{B}$ define the **left** and the **right multiplication**

$$
L_{\tilde Q_3}(\tilde{Q}_1) = \tilde Q_3\,\tilde{Q}_1 ,\qquad R_{\tilde Q_4}(\tilde{Q}_1) = \tilde{Q}_1\,\tilde Q_4 .
$$

These are the two one-sided operators of the algebra, and the two-sided operator of the companion article is their product, $\Theta_{\tilde Q_3}=L_{\tilde Q_3}R_{\tilde Q_3^{*}}=R_{\tilde Q_3^{*}}L_{\tilde Q_3}$ (*Two-Sided Operators on the General Plain Sesqualgebra*).

The article is the parallel of that one, section for section, and the contrast is the point of the pair. **Here the parameter enters linearly**, so the ordinary rules hold: $L$ is a multiplicative and additive assignment, the adjoint of $L_{\tilde Q_3}$ is $L_{\tilde Q_3}^{\dagger}=L_{\tilde Q_3}^{*}=L_{\tilde Q_3^{*}}$, the two sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ give the **self-adjoint** and the **skew-adjoint** operators respectively, and the operators of the slice are the automorphisms. In the two-sided case the same questions have different answers — both sectors give self-adjoint operators, no nonzero operator is skew and the assignment is quadratic — because the sandwich contains the parameter twice. Reading the two articles together isolates exactly what the doubling of the parameter does.

The algebra, the dagger, the sectors and the slice are *The Biquaternion Algebra*, *The Group of Involutions* and *The Six Subspaces*; the general one-sided theory is *One-Sided Operators on a Hermitian Algebra with Hermitian Adjoint*, *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint* and *The Adjoint of the One-Sided Action with Hermitian Adjoint*, whose biquaternion instance this article is. The left and the right multiplications in coordinates are *$M_4(\mathbb{C})_L$ Representation : The Matrix Product and the Algebra Structure*; the mixed operators with two independent one-sided parameters are *Mixed Inner Conjugation and Hermitian Adjoint*.

## The One-Sided Operators

**Definition.** For $\tilde Q_3,\tilde Q_4\in\mathbb{B}$ the **left multiplication by $\tilde Q_3$** and the **right multiplication by $\tilde Q_4$** are the $\mathbb{C}$-linear operators $L_{\tilde Q_3},R_{\tilde Q_4}\in\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ with

$$
L_{\tilde Q_3}(\tilde{Q}_1)=\tilde Q_3\,\tilde{Q}_1,\qquad R_{\tilde Q_4}(\tilde{Q}_1)=\tilde{Q}_1\,\tilde Q_4 .
$$

**Proposition (linearity in the parameter).** The assignments $\tilde Q_3\mapsto L_{\tilde Q_3}$ and $\tilde Q_4\mapsto R_{\tilde Q_4}$ are $\mathbb{C}$-linear and injective:

$$
L_{\alpha \tilde Q_5+\beta \tilde Q_6} = \alpha L_{\tilde Q_5} + \beta L_{\tilde Q_6},\qquad R_{\alpha \tilde Q_7+\beta \tilde Q_8} = \alpha R_{\tilde Q_7} + \beta R_{\tilde Q_8},
$$

and $L_{\tilde Q_3}=0$ or $R_{\tilde Q_4}=0$ implies $\tilde Q_3=0$ or $\tilde Q_4=0$.

*Proof.* The two displays are the distributivity of the algebra, and the injectivity follows by evaluating on $e_t$.

**Remark (the contrast with the two-sided case).** The parameter enters **once**, so the assignment is linear and additive; in the two-sided case it enters twice, $\Theta_{\alpha \tilde Q+\beta \tilde Q_2}(\tilde{Q}_1)=\alpha\alpha^{*}\Theta_{\tilde Q}(\tilde{Q}_1)+\beta\beta^{*}\Theta_{\tilde Q_2}(\tilde{Q}_1)+(\alpha\beta^{*}\tilde Q\tilde{Q}_1 \bar{\tilde Q_2}+\beta\alpha^{*}\tilde Q_2\tilde{Q}_1\tilde{Q}^{*})$, which is the failure of additivity. Every difference between this article and its companion traces back to this one fact.

## The Composition Laws

**Theorem (the four composition laws).** For all $\tilde Q_3,\tilde Q_4\in\mathbb{B}$,

$$
\boxed{\; L_{\tilde Q_3}L_{\tilde Q_4} = L_{\tilde Q_3\tilde Q_4},\qquad R_{\tilde Q_3}R_{\tilde Q_4} = R_{\tilde Q_4\tilde Q_3},\qquad L_{\tilde Q_3}R_{\tilde Q_4} = R_{\tilde Q_4}L_{\tilde Q_3},\qquad L_{\tilde Q_3}R_{\tilde Q_3^{*}} = \Theta_{\tilde Q_3} \;}.
$$

*Proof.* Associativity gives the first two, and the third is the associativity identity $\tilde Q_3\,(\tilde{Q}_1\,\tilde Q_4)=(\tilde Q_3\,\tilde{Q}_1)\,\tilde Q_4$; the fourth is the definition of the two-sided operator.

**Corollary (the two families, and the two-sided family as their product).** The left multiplications form a subalgebra of the operators isomorphic to $\mathbb{B}$ and the right multiplications form a subalgebra anti-isomorphic to $\mathbb{B}$, and the two subalgebras commute inside $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$; the products $L_{\tilde Q_3}R_{\tilde Q_4}$ are the **mixed** operators $\tilde{Q}_1\mapsto \tilde Q_3\tilde{Q}_1\tilde Q_4$, of which the two-sided family is the diagonal case $\tilde Q_4=\tilde Q_3^{*}$. A general mixed operator has two independent parameters and is a two-sided operator only when $\tilde Q_4=\lambda \tilde Q_3^{*}$ for a scalar $\lambda$, in which case it is $\lambda \Theta_{\tilde Q_3}$; the mixed family is the subject of *Mixed Inner Conjugation and Hermitian Adjoint*.

## The Adjoints of the One-Sided Operators

**Theorem (the adjoints).** For all $\tilde Q_3,\tilde Q_4\in\mathbb{B}$,

$$
(L_{\tilde Q_3})^{*} = L_{\tilde Q_3^{*}},\qquad (R_{\tilde Q_4})^{*} = R_{\tilde Q_4^{*}} .
$$

*Proof.* For $\tilde{Q}_1,\tilde Q_2\in\mathbb{B}$, using the anti-involution property of the dagger and the invariance of the scalar part under cyclic permutation,

$$
(L_{\tilde Q_3}\tilde{Q}_1,\tilde Q_2) = \mathrm{Sc}\bigl((\tilde Q_3\tilde{Q}_1)^{\dagger}\tilde Q_2\bigr) = \mathrm{Sc}\bigl(\tilde{Q}_1^{*}\tilde Q_3^{*}\tilde Q_2\bigr) = \bigl(\tilde{Q}_1,\ L_{\tilde Q_3^{*}}\tilde Q_2\bigr) ,
$$

and the same computation on the right with $(\tilde{Q}_1\tilde Q_4)^{\dagger}=\tilde Q_4^{*}\tilde{Q}_1^{*}$ gives $(R_{\tilde Q_4}\tilde{Q}_1,\tilde Q_2)=(\tilde{Q}_1,R_{\tilde Q_4^{*}}\tilde Q_2)$. The adjoint is unique, since the form is non-degenerate.

**Corollary (the dagger is natural for the one-sided operators).** The assignments $\tilde Q_3\mapsto L_{\tilde Q_3}$ and $\tilde Q_4\mapsto R_{\tilde Q_4}$ carry the dagger of the algebra to the adjoint of the operator: $L_{\tilde Q_3}^{\dagger}=L_{\tilde Q_3}^{*}=L_{\tilde Q_3^{*}}$ and $R_{\tilde Q_4}^{\dagger}=R_{\tilde Q_4}^{*}=R_{\tilde Q_4^{*}}$, the dagger and the star coinciding because the adjoint in view is the one of the definite form. Consequently $L$ is a **faithful $*$-representation** of the algebra on the Hilbert space $(\mathbb{B},(\cdot,\cdot))$: it is linear, multiplicative, injective and compatible with the dagger. Since $\mathbb{B}\cong M_{2}(\mathbb{C})$ and $\dim_{\mathbb{C}}\mathbb{B}=4$, the representation is the left regular representation, that is two copies of the standard module $\mathbb{C}^{2}$ of the algebra (*Introduction to the 2×2 Matrix Element Representation $M_1(\mathbb{C})$ of Biquaternions*).

**Remark (which half of the dagger is used).** The adjoint of $L_{\tilde Q_3}$ is $L_{\tilde Q_3^{*}}$ and **not** $R_{\tilde Q_3^{*}}$: the cross identity $(L_{\tilde Q_3}\tilde{Q}_1,\tilde Q_2)=(\tilde{Q}_1,R_{\tilde Q_3^{*}}\tilde Q_2)$ is false in general. In the matrix model the point is that the Hilbert structure of the algebra is the space of matrices with the Hilbert–Schmidt form, and the adjoint of left multiplication is again left multiplication.

## Self-Adjoint, Skew and Unitary One-Sided Operators

**Theorem (the type criteria).** Let $\tilde Q_3\in\mathbb{B}$ and let $L_{\tilde Q_3}$ be the left multiplication. Then

$$
\boxed{\; L_{\tilde Q_3}\ \text{self-adjoint} \iff \tilde Q_3\in\mathbb{M}_+,\qquad
L_{\tilde Q_3}\ \text{skew-adjoint} \iff \tilde Q_3\in\mathbb{M}_- \;},
$$

$$
L_{\tilde Q_3}\ \text{unitary} \iff \tilde Q_3\in U,\qquad
L_{\tilde Q_3}\ \text{an automorphism of } (\cdot,\cdot) \iff \tilde Q_3\in U,
$$

and $L_{\tilde Q_3}$ is invertible if and only if $\tilde Q_3\in\mathbb{B}^{\times}$, with inverse $L_{\tilde Q_3^{-1}}$. The same four statements hold for the right multiplication with the same criteria on the parameter.

*Proof.* By the adjoint theorem, $L_{\tilde Q_3}^{*}=L_{\tilde Q_3^{*}}$, and the assignment is injective, so $L_{\tilde Q_3}^{*}=L_{\tilde Q_3}$ if and only if $\tilde Q_3^{*}=\tilde Q_3$, $L_{\tilde Q_3}^{*}=-L_{\tilde Q_3}$ if and only if $\tilde Q_3^{*}=-\tilde Q_3$, and $(L_{\tilde Q_3})^{*}L_{\tilde Q_3}=L_{\tilde Q_3^{*}\tilde Q_3}$ is the identity if and only if $\tilde Q_3^{*}\tilde Q_3=e_t$. The form preservation criterion is the same computation, $(L_{\tilde Q_3}\tilde{Q}_1,L_{\tilde Q_3}\tilde Q_2)=(\tilde{Q}_1,\tilde Q_3^{*}\tilde Q_3\tilde Q_2)$, and it coincides with unitarity of the operator. Invertibility is the inverse of an algebra element.

**Corollary (the two sectors give the two types).** The Hermitian and the anti-Hermitian elements act by the self-adjoint and by the skew-adjoint operators respectively, and the correspondence is exactly that of the involutions of the algebra:

$$
L_{\mathbb{M}_+} = \text{self-adjoint operators},\qquad L_{\mathbb{M}_-} = \text{skew-adjoint operators}.
$$

This is the sharpest contrast with the companion article, where both sectors give self-adjoint operators and no nonzero operator is skew: there the parameter appears twice, and the sign that separates the sectors is squared away.

**Corollary (the exponential and the unitary group).** Since $L_{\tilde Q_3}^{*}=L_{\tilde Q_3^{*}}$, the image of the slice $U$ under $L$ is a group of unitary operators isomorphic to $\mathrm{U}(2)$, and the image of the anti-Hermitian subspace $\mathbb{M}_-$ is a space of skew-adjoint operators closed under the commutator, that is the Lie algebra of that unitary group. The exponential of a skew-adjoint one-sided operator is again one-sided: $\exp(L_{\tilde Q_3})=L_{\exp(\tilde Q_3)}$ for $\tilde Q_3\in\mathbb{M}_-$, since the exponential series and the linearity of the assignment commute. In the matrix model this is the familiar statement that the anti-Hermitian matrices exponentiate into $\mathrm{U}(2)$.

## The Commutant and the Double Centraliser

**Theorem (the double centraliser).** An operator $S\in\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ commutes with every left multiplication if and only if it is a right multiplication, and conversely:

$$
\boxed{\; \{\,S : SL_{\tilde Q_3}=L_{\tilde Q_3}S\ \ \forall \tilde Q_3\,\} = \{\,R_{\tilde Q_4} : \tilde Q_4\in\mathbb{B}\,\},\qquad
\{\,S : SR_{\tilde Q_4}=R_{\tilde Q_4}S\ \ \forall \tilde Q_4\,\} = \{\,L_{\tilde Q_3} : \tilde Q_3\in\mathbb{B}\,\} \;}.
$$

*Proof.* Let $S$ commute with all $L_{\tilde Q_3}$ and put $\tilde Q_4=S(e_t)$. For every $\tilde Q_3$, using $\tilde Q_3=L_{\tilde Q_3}(e_t)$ and the commutation,

$$
S(\tilde Q_3) = S\bigl(L_{\tilde Q_3}(e_t)\bigr) = L_{\tilde Q_3}\bigl(S(e_t)\bigr) = \tilde Q_3\,\tilde Q_4 = R_{\tilde Q_4}(\tilde Q_3),
$$

so $S=R_{\tilde Q_4}$; the converse is the third composition law. The second identity is the same argument with the roles exchanged.

**Corollary (the bicommutant is the scalars).** An operator commuting with both families is a scalar multiple of the identity:

$$
\{\,S : SL_{\tilde Q_3}=L_{\tilde Q_3}S\ \text{and}\ SR_{\tilde Q_4}=R_{\tilde Q_4}S\ \ \forall \tilde Q_3,\tilde Q_4\,\} = \mathbb{C}\,\mathrm{id}.
$$

*Proof.* By the theorem $S=R_{\tilde Q_4}$ for some $\tilde Q_4$, and the commutation with every $R_{\tilde Q_3}$ reads $R_{\tilde Q_3}R_{\tilde Q_4}=R_{\tilde Q_4}R_{\tilde Q_3}$, that is $\tilde Q_4\tilde Q_3=\tilde Q_3\tilde Q_4$ for all $\tilde Q_3$ by the second composition law; so $\tilde Q_4$ is central, $\tilde Q_4=\lambda e_t$, and $R_{\lambda e_t}=\lambda\,\mathrm{id}$.

**Remark (why the two families are exactly two).** The algebra is central simple, of complex dimension four, and the left regular representation has the same dimension; the double centraliser theorem then says that the left and the right multiplications exhaust each other's commutants, with the centre as the only overlap. There is no room for a third independent family of one-sided operators.

## The Form That Makes the Action Self-Adjoint

**Theorem (the defining property of the form).** The scalar form satisfies, for all $\tilde Q_3,\tilde{Q}_1,\tilde Q_2$,

$$
(\tilde Q_3\,\tilde{Q}_1,\ \tilde Q_2) = \bigl(\tilde{Q}_1,\ \tilde Q_3^{*}\tilde Q_2\bigr) ,
$$

and it is, up to a positive scalar, the **only** general plain sesquilinear form on $\mathbb{B}$ that is $\mathbb{C}$-linear in the second argument and invariant in the sense that the adjoint of $L_{\tilde Q_3}$ is $L_{\tilde Q_3^{*}}$ and the form is positive definite.

*Proof.* The identity is the adjoint theorem. For the uniqueness, let $\phi$ be such a form with matrix $G$ in the basis. The invariance with respect to every $L_{\tilde Q_3}$ reads $G A = A^{\dagger}G$ for every matrix $A=\mathsf{M}_1(\tilde Q_3)$ of the algebra; taking $A$ running over the matrix units forces $G$ to be a scalar matrix, and positivity then forces the scalar to be positive. See *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint* and *The Adjoint of the One-Sided Action with Hermitian Adjoint* for the general statement.

**Corollary (the module picture).** The algebra, seen as a module over itself carrying the form $(\cdot,\cdot)$, is a **Hermitian Clifford module** in the sense of the corpus: the action is by left multiplication and the adjoint of the action is the action of the adjoint element. The two-sided operator is then the operator of the module with both factors, $\Theta_{\tilde Q_3}=L_{\tilde Q_3}R_{\tilde Q_3^{*}}=L_{\tilde Q_3}(R_{\tilde Q_3})^{*}$, the product of the action with the adjoint of the *other* action. Note that $L_{\tilde Q_3}L_{\tilde Q_3}^{*}=L_{\tilde Q_3}L_{\tilde Q_3^{*}}=L_{\tilde Q_3\tilde Q_3^{*}}$ is left multiplication by the Hermitian element $\tilde Q_3\tilde Q_3^{*}$, which is **not** $\Theta_{\tilde Q_3}$; the two factors of the sandwich are one left and one right, and never two left.

## Worked Examples

**The identity and the central scalars.** $L_{e_t}=R_{e_t}=\mathrm{id}$. For a central scalar $\lambda e_t$ the two one-sided operators agree, $L_{\lambda e_t}=R_{\lambda e_t}=\lambda\,\mathrm{id}$, and they are self-adjoint exactly for $\lambda$ real, skew-adjoint exactly for $\lambda$ imaginary, unitary exactly for $\lvert\lambda\rvert=1$. The central circle gives the scalar unitary operators, a subgroup $\mathrm{U}(1)$ of the group of unitary operators, to be compared with the kernel $\mathrm{U}(1)$ of the two-sided assignment.

**The vector generators.** For $\tilde Q_3=\vec e_\mu$, $\mu\in\{x,y,z\}$, one has $\vec e_\mu^{\dagger}=-\vec e_\mu$ and $\vec e_\mu^{2}=-e_t$, so $L_{\vec e_\mu}$ is skew-adjoint and $L_{\vec e_\mu}^{2}=L_{-e_t}=-\mathrm{id}$: the left multiplication by a vector generator is a complex structure on the algebra, of square minus the identity. This is the operator form of the relations of the Clifford structure (*Biquaternion Versors and the Orthogonal Group*), and the three operators $L_{\vec e_x},L_{\vec e_y},L_{\vec e_z}$ satisfy the anticommutation relations of the generators.

**A parameter in neither sector.** For $\tilde Q_3=\vec e_x+i\vec e_y$ the dagger acts as $\tilde Q_3^{*}=-\vec e_x+i\vec e_y$, so the Hermitian part of the parameter is $(\tilde Q_3+\tilde Q_3^{*})/2=i\vec e_y$, which lies in $\mathbb{M}_+$, and the anti-Hermitian part is $(\tilde Q_3-\tilde Q_3^{*})/2=\vec e_x$, which lies in $\mathbb{M}_-$. Accordingly the operator splits into a self-adjoint and a skew-adjoint part,

$$
L_{\tilde Q_3} = L_{i\vec e_y} + L_{\vec e_x},
$$

and is therefore of neither of the two types, in agreement with the theorem: the parameter is in neither sector. The example records where the type is decided: by the parameter, through the sector it lies in, and never by the argument.

**A mixed operator that is not two-sided.** The operator $\tilde{Q}_1\mapsto \vec e_x\tilde{Q}_1\vec e_y=L_{\vec e_x}R_{\vec e_y}$ is not of the form $\Theta_{\tilde Q}$ for any $\tilde Q$. Indeed a two-sided operator satisfies $\Theta_{\tilde Q}(e_t)=\tilde Q\tilde{Q}^{*}\in\mathbb{M}_+$, whereas $L_{\vec e_x}R_{\vec e_y}(e_t)=\vec e_x\vec e_y=\vec e_z$, which is anti-Hermitian; so no parameter $\tilde Q$ reproduces the operator. In general $L_{\tilde Q_3}R_{\tilde Q_4}$ is two-sided only if $\tilde Q_3\tilde Q_4\in\mathbb{M}_+$, and when $\tilde Q_4=\lambda \tilde Q_3^{*}$ with $\lambda=\lvert\mu\rvert^{2}\geq0$ one has $L_{\tilde Q_3}R_{\tilde Q_4}=\Theta_{\mu \tilde Q_3}$. Its adjoint is $L_{\vec e_x^{\dagger}}R_{\vec e_y^{\dagger}}=L_{-\vec e_x}R_{-\vec e_y}=L_{\vec e_x}R_{\vec e_y}$, so this particular mixed operator is self-adjoint, a phenomenon that the two-sided family does not show.

**A check of the composition and the adjoint.** For random $\tilde Q_3,\tilde Q_4$ and random $\tilde{Q}_1,\tilde Q_2$, the identities $L_{\tilde Q_3}L_{\tilde Q_4}=L_{\tilde Q_3\tilde Q_4}$, $L_{\tilde Q_3}R_{\tilde Q_4}=R_{\tilde Q_4}L_{\tilde Q_3}$ and $(L_{\tilde Q_3}\tilde{Q}_1,\tilde Q_2)=(\tilde{Q}_1,L_{\tilde Q_3^{*}}\tilde Q_2)$ were verified to machine precision, as were the four type criteria over the four subspaces.

## Summary

The left and the right multiplications $L_{\tilde Q_3}(\tilde{Q}_1)=\tilde Q_3\tilde{Q}_1$ and $R_{\tilde Q_4}(\tilde{Q}_1)=\tilde{Q}_1\tilde Q_4$ are the one-sided operators of the biquaternion algebra, and the two-sided operator of the companion article is their product $\Theta_{\tilde Q_3}=L_{\tilde Q_3}R_{\tilde Q_3^{*}}$. The parameter enters **linearly**, and everything follows: the assignment is additive and injective, the composition laws are $L_{\tilde Q_3}L_{\tilde Q_4}=L_{\tilde Q_3\tilde Q_4}$, $R_{\tilde Q_3}R_{\tilde Q_4}=R_{\tilde Q_4\tilde Q_3}$ and $L_{\tilde Q_3}R_{\tilde Q_4}=R_{\tilde Q_4}L_{\tilde Q_3}$, the adjoints are $(L_{\tilde Q_3})^{*}=L_{\tilde Q_3^{*}}$ and $(R_{\tilde Q_4})^{*}=R_{\tilde Q_4^{*}}$, so that $L$ is a faithful $*$-representation of the algebra on the Hilbert space of the scalar form, of complex dimension four, that is two copies of the standard module. The **type criteria** are the ones of the involution lattice: $L_{\tilde Q_3}$ is self-adjoint exactly on $\mathbb{M}_+$, skew-adjoint exactly on $\mathbb{M}_-$, unitary and congruent exactly on the slice $U$, and invertible exactly on the group of units; the Lie algebra of the unitary one-sided operators is $L_{\mathbb{M}_-}$ and the exponential stays inside the family, $\exp(L_{\tilde Q_3})=L_{\exp(\tilde Q_3)}$. The **double centraliser theorem** holds in two lines: the commutant of the left multiplications is the right multiplications and conversely, the bicommutant is the scalars, and the mixed operators $L_{\tilde Q_3}R_{\tilde Q_4}$ with two independent parameters are the ones that are not two-sided. Finally the scalar form is characterised among the positive definite general plain sesquilinear forms by the property that the adjoint of the action is the action of the adjoint element, which is the statement that the algebra is a Hermitian Clifford module over itself. The pair of articles isolates in this way what the doubling of the parameter in the sandwich costs: the additivity, the separation of the two sectors, the existence of skew operators, and the injectivity of the assignment.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra; basis $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| ${}^{*}$ | Hermitian conjugation; $\mathbb{M}_+$ fixed, $\mathbb{M}_-$ anti-fixed |
| $(\tilde Q,\tilde{Q}_1)=\mathrm{Sc}(\tilde{Q}^{*}\tilde{Q}_1)$ | The scalar form; Gram matrix the identity |
| $L_{\tilde Q_3}(\tilde{Q}_1)=\tilde Q_3\tilde{Q}_1$ | Left multiplication; $\mathbb{C}$-linear and injective in $\tilde Q_3$ |
| $R_{\tilde Q_4}(\tilde{Q}_1)=\tilde{Q}_1\tilde Q_4$ | Right multiplication; the anti-homomorphism family |
| $\Theta_{\tilde Q_3}=L_{\tilde Q_3}R_{\tilde Q_3^{*}}$ | The two-sided operator, the product of the two |
| $L_{\tilde Q_3}L_{\tilde Q_4}=L_{\tilde Q_3\tilde Q_4}$, $R_{\tilde Q_3}R_{\tilde Q_4}=R_{\tilde Q_4\tilde Q_3}$ | Composition laws |
| $L_{\tilde Q_3}R_{\tilde Q_4}=R_{\tilde Q_4}L_{\tilde Q_3}$ | The two families commute |
| $(L_{\tilde Q_3})^{*}=L_{\tilde Q_3^{*}}$, $(R_{\tilde Q_4})^{*}=R_{\tilde Q_4^{*}}$ | The adjoints; $L$ is a $*$-representation |
| $U=\{\tilde{Q}^{*}\tilde Q=e_t\}=\mathrm{U}(2)$ | The unitary slice; the automorphisms and the unitary operators |
| $\{S : SL_{\tilde Q_3}=L_{\tilde Q_3}S\ \forall \tilde Q_3\}=R(\mathbb{B})$ | The double centraliser theorem |
| $L_{\tilde Q_3}R_{\tilde Q_4}$ | Mixed operator; two-sided only if $\tilde Q_4=\lambda \tilde Q_3^{*}$ |

## Further Reading

- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), for the algebra, the four conjugations and the remarkable subspaces.
- [Two-Sided Operators on the General Plain Sesqualgebra](two-sided-operators-on-the-general-plain-sesqualgebra.html), the companion article, with the composition and the type theorems for the product of the two one-sided families.
- [$M_4(\mathbb{C})_L$ Representation : The Matrix Product and the Algebra Structure](m4c-representation-the-matrix-product-and-the-algebra-structure.html), for the left and the right regular representations in matrix form.
- [One-Sided Operators on a Hermitian Algebra with Hermitian Adjoint](one-sided-operators-on-a-hermitian-algebra-with-hermitian-adjoint.html), for the general one-sided theory, the double centraliser and the images as ideals.
- [Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint](hermitian-modules-over-a-hermitian-algebra-with-hermitian-adjoint.html), for the module axiom $(\tilde Q_3\cdot s,t)=(s,\tilde Q_3^{*}\cdot t)$ used in the last section.
- [The Adjoint of the One-Sided Action with Hermitian Adjoint](the-adjoint-of-the-one-sided-action-with-hermitian-adjoint.html), for the $*$-structure on the operator algebra and the reason a Dirac operator is formally self-adjoint.
- [Mixed Inner Conjugation and Hermitian Adjoint](mixed-inner-conjugation-and-hermitian-adjoint.html), for the operators with two independent one-sided parameters.
- [Unitary Equivalence and Congruence of Operators with Hermitian Adjoint](unitary-equivalence-and-congruence-of-operators-with-hermitian-adjoint.html), for the equivalence relations of the operator families.
