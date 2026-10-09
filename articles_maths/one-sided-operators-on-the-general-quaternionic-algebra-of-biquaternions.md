
# __One-Sided Operators on the General Quaternionic Algebra of Biquaternions__

## Introduction

The biquaternion algebra acts on itself in two ways, on the left and on the right, and the two actions are the one-sided operators

$$
L_{\tilde A}(\tilde Y)=\tilde A\tilde Y,\qquad R_{\tilde B}(\tilde Y)=\tilde Y\tilde B .
$$

Every two-sided operator is a product of one left and one right multiplication, and the twisted two-sided operator of the algebra, the conjugation sandwich $\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{\natural}}$, is the member of that family selected by the natural conjugation. This article treats the pair: the two composition laws, the commutation of the left and the right action, the two adjoints, the norm of a multiplication, and the criterion that decides which two-sided products are multiplicative. The two-sided operator itself is *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions*; the general Clifford theory of the one-sided families is *One-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*, of which this is the biquaternion instance; the corresponding one-sided operators over the dagger are *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*; and the form that supplies the adjoints is *The Four Pairings of the Biquaternion Algebra*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$, so that a general element is $\tilde A=\sum_\mu A_\mu e_\mu$ with $A_\mu\in\mathbb{C}$. The natural conjugation is $\tilde A^{\natural}=A_0e_0-A_1e_1-A_2e_2-A_3e_3$; the norm is $N(\tilde A)=\tilde A\tilde A^{\natural}=\sum_\mu A_\mu^2$, central and multiplicative; the general quaternionic bilinear form is $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P\tilde Q^{\natural})$, with adjoint written ${}^{N}$; the Hermitian form is $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$ and its adjoint is written ${}^{*}$. An operator is a $\mathbb{C}$-linear map of $\mathbb{B}$ to itself.

## The Two Multiplications

**Definition.** For $\tilde A,\tilde B\in\mathbb{B}$ the **left multiplication** by $\tilde A$ and the **right multiplication** by $\tilde B$ are the $\mathbb{C}$-linear maps

$$
L_{\tilde A}:\tilde Y\mapsto\tilde A\tilde Y,\qquad R_{\tilde B}:\tilde Y\mapsto\tilde Y\tilde B .
$$

**Proposition (linearity, the identity, injectivity).** The maps $\tilde A\mapsto L_{\tilde A}$ and $\tilde B\mapsto R_{\tilde B}$ are $\mathbb{C}$-linear and injective; $L_{e_0}=R_{e_0}=\mathrm{id}$; and $L_{\tilde A}$ and $R_{\tilde B}$ are bijections exactly when $\tilde A$ and $\tilde B$ are units, with inverses $L_{\tilde A}^{-1}=L_{\tilde A^{-1}}$ and $R_{\tilde B}^{-1}=R_{\tilde B^{-1}}$.

*Proof.* Linearity is linearity of the product in each factor. For injectivity, $L_{\tilde A}=0$ forces $\tilde A=L_{\tilde A}(e_0)=0$, and $R_{\tilde B}=0$ forces $\tilde B=R_{\tilde B}(e_0)=0$; the identity element gives $L_{e_0}=R_{e_0}=\mathrm{id}$. For the inverses, $L_{\tilde A}L_{\tilde A^{-1}}=L_{\tilde A\tilde A^{-1}}=L_{e_0}=\mathrm{id}$, and only a unit has a two-sided inverse; the injectivity of the parameter map shows that no non-unit can be invertible, since a nonzero non-unit is a zero divisor. Verified on $200$ random parameters, including the null element $e_1+ie_2$, for which $L$ and $R$ are nonzero and not invertible.

**Remark (the parameter map is linear here).** Unlike the two-sided operator, which is quadratic in its parameter, each one-sided operator is linear in its parameter: $L_{\lambda\tilde A+\mu\tilde B}=\lambda L_{\tilde A}+\mu L_{\tilde B}$, and likewise for $R$. This is the formal difference between the one-sided and the two-sided layers, and it is the reason a one-sided operator alone cannot carry the norm: the norm appears only in the composition of two.

## The Composition Laws and the Two Actions

**Proposition (the composition laws).** For all $\tilde A,\tilde B$,

$$
L_{\tilde A}\circ L_{\tilde B}=L_{\tilde A\tilde B},\qquad
R_{\tilde A}\circ R_{\tilde B}=R_{\tilde B\tilde A},\qquad
L_{\tilde A}\circ R_{\tilde B}=R_{\tilde B}\circ L_{\tilde A}.
$$

*Proof.* $L_{\tilde A}L_{\tilde B}(\tilde Y)=\tilde A\tilde B\tilde Y=L_{\tilde A\tilde B}(\tilde Y)$; $R_{\tilde A}R_{\tilde B}(\tilde Y)=\tilde Y\tilde B\tilde A=R_{\tilde B\tilde A}(\tilde Y)$; and the left and right multiplications commute by associativity, $\tilde A(\tilde Y\tilde B)=(\tilde A\tilde Y)\tilde B$. Verified on $200$ random triples.

**Remark (the two laws are opposite).** The left law preserves the order of the parameters and the right law reverses it: $L$ is a representation of the algebra and $R$ is a representation of the opposite algebra, $R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}$. This is the formal reason the two-sided product $L_{\tilde A}R_{\tilde B}$ is not multiplicative in general, and the reason the natural conjugation, which is an anti-automorphism, is the right partner for the left multiplication.

**Proposition (the double centraliser).** The operators commuting with every left multiplication are exactly the right multiplications: $\{T:TL_{\tilde A}=L_{\tilde A}T\text{ for all }\tilde A\}=\{R_{\tilde B}\}$. Dually, the operators commuting with every right multiplication are the left multiplications; and the operators commuting with both families are the scalars, $T=\lambda\,\mathrm{id}$.

*Proof.* A right multiplication commutes with every left multiplication by associativity, which is one inclusion. For the converse, let $T$ commute with all $L_{\tilde A}$, and put $\tilde B=T(e_0)$; then $T(\tilde A)=T(L_{\tilde A}e_0)=L_{\tilde A}T(e_0)=\tilde A\tilde B=R_{\tilde B}(\tilde A)$, so $T=R_{\tilde B}$. An operator commuting with both families commutes with all products $L_{\tilde A}R_{\tilde B}$, hence is multiplication by a central element, that is by a scalar. Verified on the generators: the condition on the operator $T$ is a linear system of $16$ unknowns whose solution space is the four-dimensional space of the right multiplications.

## The Two-Sided Products and the Sign

**Definition.** A **two-sided operator** is a product $L_{\tilde A}R_{\tilde B}$; the **twisted two-sided operator** is the member $\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{\natural}}$.

**Proposition (the criterion).** For all $\tilde Y,\tilde Z$ the product satisfies

$$
L_{\tilde A}R_{\tilde B}(\tilde Y)\,L_{\tilde A}R_{\tilde B}(\tilde Z)=L_{\tilde A}R_{\tilde B}\bigl(\tilde Y\,(\tilde B\tilde A)\,\tilde Z\bigr),
$$

so it is multiplicative up to the scalar $\tilde B\tilde A$ exactly when $\tilde B\tilde A$ is central, and strictly multiplicative exactly when $\tilde B\tilde A=e_0$; up to scalar multiples, the products that are multiplicative in this sense are exactly the twisted two-sided operators.

*Proof.* The left side is $\tilde A\tilde Y\tilde B\tilde A\tilde Z\tilde B=\tilde A\tilde Y(\tilde B\tilde A)\tilde Z\tilde B$, which is $L_{\tilde A}R_{\tilde B}$ applied to $\tilde Y(\tilde B\tilde A)\tilde Z$; when $\tilde B\tilde A=\mu e_0$ is scalar it may be moved out, giving $L(\tilde Y)L(\tilde Z)=\mu L(\tilde Y\tilde Z)$, and the strict case is $\mu=1$. Conversely, for units $\tilde A,\tilde B$ the identity for all $\tilde Y,\tilde Z$ forces the factor $\tilde B\tilde A$ to be scalar. With $\tilde B\tilde A=\mu e_0$ and $\tilde A$ a unit, $\tilde B=\mu\tilde A^{-1}=\mu\tilde A^{\natural}/N(\tilde A)$, proportional to $\tilde A^{\natural}$. Verified on $300$ random pairs, and on the central cases $(\tilde A,\tilde B)=(e_0,-e_0)$ and $(e_0,e_0)$.

**Proposition (the sign, and the factorisation).** For every element,

$$
\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{\natural}}=N(\tilde A)\,\mathrm{Ad}_{\tilde A}\quad(\tilde A\text{ a unit}),\qquad
\Theta_{\tilde A}(\tilde Y)\Theta_{\tilde A}(\tilde Z)=N(\tilde A)\,\Theta_{\tilde A}(\tilde Y\tilde Z),
$$

and $\Theta_{\tilde A}\Theta_{\tilde B}=\Theta_{\tilde A\tilde B}$. The right factor is the inverse right multiplication up to the norm, $R_{\tilde A^{\natural}}=N(\tilde A)R_{\tilde A^{-1}}$ on a unit, so it is the left factor $L_{\tilde A}$ that carries the conjugation, and the norm scalar that appears in the multiplication law is the price of that choice.

*Proof.* Each identity is the corresponding identity of *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions*, read in the one-sided notation; the factorisation $R_{\tilde A^{\natural}}=N(\tilde A)R_{\tilde A^{-1}}$ is $\tilde A^{\natural}=N(\tilde A)\tilde A^{-1}$ for a unit. Verified on $200$ random triples.

**Remark (why the left factor carries the sign).** A one-sided operator does not act on the vector subspace: no left multiplication and no right multiplication carries $\mathbb{C}\{e_1,e_2,e_3\}$ into itself except the scalar ones, so the sign cannot be detected one-sidedly. It is the product of the two factors that acts on the vector subspace as a form-preserving map, and the sign sits in the left factor as the reflection of the parameter.

**Remark (the two normalisations of the sign).** The general two-sided family $\Phi^{\theta,c}_x(y)=\theta(x)y\,c(x)$ of *Two-Sided Operators on a Clifford Algebra* has five members, and the name "signed inner conjugation" is used in the corpus for two of them: the member $\theta=\alpha$, $c=(\ )^{-1}$, which is $\alpha(\tilde A)\tilde Y\tilde A^{-1}=\varepsilon_{\tilde A}\mathrm{Ad}_{\tilde A}$ with the parity sign $\varepsilon$, and the member $\theta=\mathrm{id}$, $c={}^{\natural}$, the conjugation sandwich $\tilde A\tilde Y\tilde A^{\natural}=N(\tilde A)\mathrm{Ad}_{\tilde A}$, which is the operator of this article. They coincide exactly on the homogeneous parameters with $N(\tilde A)=\varepsilon_{\tilde A}$. The one-sided factors below are those of the second normalisation, the one whose right factor is $R_{\tilde A^{\natural}}=N(\tilde A)R_{\tilde A^{-1}}$; the factors of the first differ by the same scalar and are the ones used in *Biquaternion Versors and the Orthogonal Group*.

## The Adjoints for the Bilinear Form

**Proposition (the two adjoints).** For the general quaternionic bilinear form,

$$
\bigl(L_{\tilde A}\bigr)^{N}=L_{\tilde A^{\natural}},\qquad
\bigl(R_{\tilde B}\bigr)^{N}=R_{\tilde B^{\natural}} .
$$

*Proof.* $\langle L_{\tilde A}\tilde X,\tilde Y\rangle_{\natural}=\mathrm{Sc}(\tilde A\tilde X\tilde Y^{\natural})$, and by the cyclicity of the scalar part this equals $\mathrm{Sc}(\tilde X\tilde Y^{\natural}\tilde A)=\mathrm{Sc}(\tilde X(\tilde A^{\natural}\tilde Y)^{\natural})=\langle\tilde X,L_{\tilde A^{\natural}}\tilde Y\rangle_{\natural}$, since ${}^{\natural}$ is an anti-automorphism; the right case is the same computation with the factors in the other order. Verified on $200$ random triples for each family.

**Corollary (the self-adjoint, the skew-adjoint and the congruent multiplications).** The left multiplication $L_{\tilde A}$ is $N$-self-adjoint exactly for $\tilde A$ central, $N$-skew-adjoint exactly for $\tilde A$ pure, and an automorphism of the form exactly for $N(\tilde A)=1$; for the right multiplication the same three criteria hold with $\tilde B$ in place of $\tilde A$.

*Proof.* By the injectivity of the parameter map, $L_{\tilde A^{\natural}}=L_{\tilde A}$ is $\tilde A^{\natural}=\tilde A$, that is $\tilde A$ central; $L_{\tilde A^{\natural}}=-L_{\tilde A}=L_{-\tilde A}$ is $\tilde A^{\natural}=-\tilde A$, that is $\tilde A$ pure; and the preservation condition is read from the norm of the image, $N(L_{\tilde A}\tilde X)=N(\tilde A)N(\tilde X)$, which is $1$ for all $\tilde X$ exactly when $N(\tilde A)=1$. Verified on $300$ random parameters for each statement.

**Remark (the two sectors are populated here).** Both the self-adjoint and the skew-adjoint sector are non-empty for the one-sided operators, the centre $\mathbb{C}_{\mathbb{B}}$ and the vector subspace $\mathrm{Vect}(\mathbb{B})$: the sign character of the algebra splits the parameters, and the two sectors are its two eigenspaces. The contrast with the two-sided operator, where the skew-adjoint sector collapses, is one more sign that the two-sided operator is the twisted object and the one-sided ones are not.

## The Norm and the Determinant of a Multiplication

**Proposition (the conformal factor and the determinant).** For all $\tilde A,\tilde X$,

$$
N\bigl(L_{\tilde A}\tilde X\bigr)=N(\tilde A)\,N(\tilde X),\qquad
N\bigl(R_{\tilde A}\tilde X\bigr)=N(\tilde A)\,N(\tilde X),
$$

so that each multiplication scales the form by the norm of its parameter; in the coefficient basis,

$$
\det L_{\tilde A}=\det R_{\tilde A}=N(\tilde A)^{2}.
$$

*Proof.* $N(\tilde A\tilde X)=N(\tilde A)N(\tilde X)$ is the multiplicativity of the norm, and the right case is the same with the factors interchanged. For the determinant, the matrix realisation $\Phi$ of the algebra sends $L_{\tilde A}$ to the map $B\mapsto\Phi(\tilde A)B$ on $M_2(\mathbb{C})$, which is $\Phi(\tilde A)\otimes I_2$; the determinant of a Kronecker product is $\det(\Phi(\tilde A))^{2}\det(I_2)^{2}=\det(\Phi(\tilde A))^{2}=N(\tilde A)^{2}$, since $\det\Phi(\tilde A)=N(\tilde A)$. Verified by expansion on $200$ random parameters.

**Corollary (the form-preserving multiplications).** The multiplications that preserve the form are exactly those by an element of norm one, and their group is the norm-one slice of $\mathbb{B}^\times$; the multiplications by an element of norm $-1$ reverse the sign of the form.

**Proposition (the matrix models of the multiplications).** The two multiplications are the two Kronecker products of the matrix $\Phi(\tilde A)$ with the identity:

$$
\Phi\bigl(L_{\tilde A}\tilde X\bigr)=\Phi(\tilde A)\,\Phi(\tilde X),\qquad
\Phi\bigl(R_{\tilde A}\tilde X\bigr)=\Phi(\tilde X)\,\Phi(\tilde A),
$$

so that $L_{\tilde A}$ is the left factor and $R_{\tilde A}$ the right factor of the regular representation: each is the Kronecker product of $\Phi(\tilde A)$ with the identity $I_2$, the left one carrying $\Phi(\tilde A)$ itself and the right one carrying its transpose, the transpose entering because the two factors of a Kronecker product act on the two sides of the matrix. Independently of which slot the identity occupies, $\Phi(\tilde A)$ acts on the left factor for $L_{\tilde A}$ and $\Phi(\tilde A)^{\mathsf T}$ on the right factor for $R_{\tilde A}$, so the two determinants are $\det\Phi(\tilde A)^{2}=N(\tilde A)^{2}$ each and the two traces are $2\,\mathrm{tr}\,\Phi(\tilde A)=4A_0$ each; the two commute for every pair of parameters, which is the associativity of the algebra read in the regular representation.

*Proof.* The multiplication map $B\mapsto\Phi(\tilde A)B$ on $M_2(\mathbb{C})\cong\mathbb{C}^{4}$ is a Kronecker product of $\Phi(\tilde A)$ with $I_2$, of determinant $\det\Phi(\tilde A)^{2}=N(\tilde A)^{2}$ by the multiplicativity of the determinant of a Kronecker product, and $B\mapsto B\Phi(\tilde A)$ is the same product with $\Phi(\tilde A)$ replaced by its transpose, of the same determinant because the determinant is invariant under transposition. The trace of either product is $\mathrm{tr}\,\Phi(\tilde A)\cdot\mathrm{tr}\,I_2=2A_0\cdot2=4A_0$ because $\mathrm{tr}\,\Phi(\tilde A)=2A_0$; the commutation is the mixed-product rule for Kronecker products, $(A\otimes I_2)(I_2\otimes A^{\mathsf T})=(I_2\otimes A^{\mathsf T})(A\otimes I_2)$. Verified on $100$ pairs: the two matrices commute, their determinant is $N(\tilde A)^{2}$, and their trace is $4A_0$.

## The Hermitian Layer

**Proposition (the dagger adjoints).** For the general plain sesquilinear form,

$$
\bigl(L_{\tilde A}\bigr)^{*}=L_{\tilde A^{*}},\qquad
\bigl(R_{\tilde B}\bigr)^{*}=R_{\tilde B^{*}} .
$$

*Proof.* $\langle L_{\tilde A}\tilde X,\tilde Y\rangle_{*}=\mathrm{Sc}(\tilde A\tilde X\tilde Y^{*})$ and $\langle\tilde X,L_{\tilde A^{*}}\tilde Y\rangle_{*}=\mathrm{Sc}(\tilde X(\tilde A^{*}\tilde Y)^{*})=\mathrm{Sc}(\tilde X\tilde Y^{*}\tilde A)$; the two agree by the cyclicity of the scalar part, since $(\tilde A^{*}\tilde Y)^{*}=\tilde Y^{*}\tilde A$. Verified on $200$ random triples.

**Corollary (the sectors for the dagger).** For the Hermitian form, $L_{\tilde A}$ is self-adjoint exactly for $\tilde A\in\mathbb{M}_+$, skew-adjoint exactly for $\tilde A\in\mathbb{M}_-$, and unitary exactly on the slice $a^{*}a=e_0$; the two sectors are the two halves of the Hermitian splitting, and the dagger layer is where the pair of sectors is symmetric (*One-Sided Operators on the General Plain Sesqualgebra of Biquaternions*).

## Worked Examples

**A scalar parameter.** For $\tilde A=\lambda e_0$ the multiplications are scalars, $L_{\tilde A}=R_{\tilde A}=\lambda\,\mathrm{id}$; they are self-adjoint for every $\lambda$, since a scalar parameter is central, and a form-preserving map exactly for $\lambda^{2}=1$, that is $\lambda=\pm1$.

**A vector parameter.** For $\tilde V=e_1$, $N(\tilde V)=1$ and $\tilde V^{\natural}=-e_1$, so $L_{\tilde V}$ is skew-adjoint and an automorphism of the form; the right multiplication $R_{\tilde V}$ has the same two properties, and $L_{\tilde V}R_{\tilde V}=\Theta_{\tilde V}$ is the reflection-like operator of the two-sided layer.

**A null parameter.** For $\tilde A=e_1+ie_2$, $N(\tilde A)=0$: both multiplications are nonzero, neither is invertible, and both collapse the form, $N(L_{\tilde A}\tilde X)=0$ for every $\tilde X$.

**A unit of norm one.** For $\tilde A=(e_0+e_1)/\sqrt2$ the multiplications are automorphisms of the form, and the two-sided product $L_{\tilde A}R_{\tilde A^{\natural}}$ is an inner automorphism.

## Summary

The one-sided operators of the biquaternion algebra are the left and right multiplications $L_{\tilde A}(\tilde Y)=\tilde A\tilde Y$ and $R_{\tilde B}(\tilde Y)=\tilde Y\tilde B$: linear and injective in the parameter, invertible exactly for units, with the composition laws $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$, $R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}$ and $L_{\tilde A}R_{\tilde B}=R_{\tilde B}L_{\tilde A}$. The operators commuting with all left multiplications are exactly the right multiplications, and the operators commuting with both families are the scalars. For the general quaternionic bilinear form the adjoints are $(L_{\tilde A})^{N}=L_{\tilde A^{\natural}}$ and $(R_{\tilde B})^{N}=R_{\tilde B^{\natural}}$; a left multiplication is self-adjoint exactly for a central parameter, skew-adjoint exactly for a pure one, and a form-preserving map exactly for norm one, and each multiplication scales the form by the norm of its parameter. For the Hermitian form the adjoints are the same with ${}^{*}$, with the two sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ and unitarity on the slice $a^{*}a=e_0$. The two-sided products $L_{\tilde A}R_{\tilde B}$ are multiplicative up to the scalar $\tilde B\tilde A$ exactly when $\tilde B\tilde A$ is central and strictly multiplicative exactly when $\tilde B\tilde A=e_0$, that is, up to scalars, exactly for the twisted two-sided operators $\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{\natural}}$, whose multiplicativity holds up to the norm.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde A}(\tilde Y)=\tilde A\tilde Y$, $R_{\tilde B}(\tilde Y)=\tilde Y\tilde B$ | The one-sided operators |
| $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$, $R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}$, $L_{\tilde A}R_{\tilde B}=R_{\tilde B}L_{\tilde A}$ | The composition laws |
| $\{T:TL_{\tilde A}=L_{\tilde A}T\}=\{R_{\tilde B}\}$ | The commutant; the double centraliser |
| $(L_{\tilde A})^{N}=L_{\tilde A^{\natural}}$, $(R_{\tilde B})^{N}=R_{\tilde B^{\natural}}$ | The adjoints for the general quaternionic bilinear form |
| $(L_{\tilde A})^{*}=L_{\tilde A^{*}}$, $(R_{\tilde B})^{*}=R_{\tilde B^{*}}$ | The adjoints for the Hermitian form |
| $N(L_{\tilde A}\tilde X)=N(\tilde A)N(\tilde X)$, $\det L_{\tilde A}=N(\tilde A)^{2}$ | The conformal factor and the determinant |
| $\Theta_{\tilde A}=L_{\tilde A}R_{\tilde A^{\natural}}$ | The twisted two-sided product |
| $\tilde B\tilde A$ central; $=e_0$ | $L_{\tilde A}R_{\tilde B}$ multiplicative up to the scalar $\tilde B\tilde A$; strictly multiplicative for $\tilde B\tilde A=e_0$ |

## Further Reading

- *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-quaternionic-algebra-of-biquaternions.md`), for the product of the two factors
- *One-Sided Operators on the General Plain Sesqualgebra of Biquaternions* (`articles_maths/one-sided-operators-on-the-general-plain-sesqualgebra-of-biquaternions.md`), for the dagger layer
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the form and its adjoint
- *One-Sided Operators on a Clifford Algebra with Signed Inner Conjugation* (`articles_maths/one-sided-operators-on-a-clifford-algebra-with-signed-inner-conjugation.md`), for the general theory
