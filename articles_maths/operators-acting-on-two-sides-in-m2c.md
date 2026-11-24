# __Operators Acting on Two Sides in $M_2(\mathbb{C})$__

## Introduction

**The question.** A two-sided operator multiplies its argument by one matrix on the left and by another on the right. The set of such operators is a cone and not a subspace, its linear span is the whole operator algebra, and the passage from the cone to its span costs a rank condition visible in the coefficient array. This article asks what the array of a two-sided operator is, what the cone is in the matrix space, how many products the span needs, and which two-sided operators are self-adjoint, isometric or multiplicative.

**Why it is the same statement.** This is the in-depth matrix reading of [Operators Acting on Two Sides](operators-acting-on-two-sides.html). The source works with $L_{\tilde Q}R_{\tilde Q_2}$ and its eight complex parameters; the display turns the same operator into the single array $B^{\mathsf T}\otimes A$, the cone into the rank-one coefficient arrays, and the generation theorem into the independence of sixteen signed permutations. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The array of $X\mapsto AXB$ is $B^{\mathsf T}\otimes A$, and the pair is defined up to $(\lambda A,\lambda^{-1}B)$. The composition law is $L_AR_BL_CR_D=L_{AC}R_{DB}$, so the family is a monoid that is not closed under addition; the operator $\mathrm{id}+L_{E_{11}}R_{E_{11}}$ is exhibited as the counterexample by four probes at the matrix units. The coefficient array of a two-sided operator has rank at most one, and conversely, so the cone is the Segre cone of decomposable tensors. The sixteen products $L_{e_\mu}R_{e_\nu}$ are a basis of $M_4(\mathbb{C})$, and the ladder is $1,4,7,16$. The plain adjoint exchanges the two parameters, so the self-adjoint products are the pairs of proportional matrices and no nonzero product is anti-self-adjoint. The isometries of the plain form are $\pm\operatorname{Ad}_A$, and the multiplicative members are $\operatorname{Ad}_A$.

**What the article does not do.** It does not treat the one-sided families, which is [Operators Acting on One Side in $M_2(\mathbb{C})$](operators-acting-on-one-side-in-m2c.html); it does not treat the length, which is [The Length of an Endomorphism of the Biquaternion Algebra: Four Two-Sided Products in $M_2(\mathbb{C})$](the-length-of-an-endomorphism-of-the-biquaternion-algebra-in-m2c.html); and it does not treat the enveloping algebra, which is [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure in $M_2(\mathbb{C})$](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure-in-m2c.html).

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, with $N(\tilde Q)=\det A$. The arrays are read in the Peirce frame, so that the carrier coordinates are the matrix entries and $L_A=\mathrm I_2\otimes A$, $R_B=B^{\mathsf T}\otimes\mathrm I_2$. Any $4\times4$ array printed here is the axis-free array, not the Pauli array: the axis-free family is the unique representative, among the $96$ signed-permutation bases, whose sixteen operator arrays are signed permutations, so its entries are the multiplication table read aloud and every identity checked in it is an integer check ([$M_4(\mathbb{C})$ Axis-Free Representation : Operators](m4c-axis-free-representation-operators.html)). The Pauli and gamma arrays are a translation and are refused as primary, because one entry of one of their matrices is diagonal by privilege, which puts a spatial direction into the notation; the privilege is canonical and fixes no invariant.

**Boundaries.** The slot exchange is [The Transposition of the Two Sides in $M_2(\mathbb{C})$](the-transposition-of-the-two-sides-in-m2c.html). The two ranks are [The Length and the Two Ranks at $n=2$](the-length-and-the-two-ranks-at-n-2.html). The adjoints are [Adjoint Pair of $L$ and $R$ Operators in $M_2(\mathbb{C})$](adjoint-pair-of-l-and-r-operators-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Symmetric and Antisymmetric Parts of the Operator Space at $n=2$](the-symmetric-and-antisymmetric-parts-of-the-operator-space-at-n-2.html).

**Letters.** The pair is $(A,B)$, read as a left matrix and a right matrix. The array is $M=B^{\mathsf T}\otimes A$. The coefficients of an element are $q_A=(A_t,A_x,A_y,A_z)$ and $q_B$ likewise, and $c(M)$ is the coefficient array in the basis $L_{e_\mu}R_{e_\nu}$.

## The Operator and Its Array

**The action.** For $A,B\in M_2(\mathbb{C})$ the two-sided operator is

$$
F_{A,B}:M_2(\mathbb{C})\to M_2(\mathbb{C}),\qquad F_{A,B}(X)=AXB .
$$

**The array.** In the Peirce frame, with the carrier coordinates taken column by column,

$$
[F_{A,B}]=B^{\mathsf T}\otimes A
=\begin{pmatrix}a_{11}B^{\mathsf T}&a_{12}B^{\mathsf T}\\a_{21}B^{\mathsf T}&a_{22}B^{\mathsf T}\end{pmatrix}.
$$

*Proof.* In the entry coordinates, left multiplication by $A$ is $\mathrm I_2\otimes A$ and right multiplication by $B$ is $B^{\mathsf T}\otimes\mathrm I_2$; the mixed-product rule of Kronecker products gives the display.

**The words.** A product of one left array with one right array at a pair of units is a **word** $W_{\mu\nu}=L_{e_\mu}R_{e_\nu}$, and here it is $B^{\mathsf T}\otimes A$ with $A=\mathsf M_2(e_\mu)$ and $B=\mathsf M_2(e_\nu)$. So a word is a Kronecker product of two of the four matrices $\mathrm I_2,-i\sigma_1,-i\sigma_2,-i\sigma_3$, the right unit's in the first slot and the left unit's in the second.

**The sixteen words, and the fifteen.** The words are orthogonal, $\operatorname{tr}(W_{\mu\nu}^{*}W_{\rho\sigma})=4\,\delta_{\mu\rho}\delta_{\nu\sigma}$, because $\operatorname{tr}\bigl((L_AR_B)^{*}L_CR_D\bigr)=\operatorname{tr}(A^{*}C)\operatorname{tr}(B^{*}D)$ and $\operatorname{tr}\bigl(\mathsf M_2(e_\mu)^{*}\mathsf M_2(e_\nu)\bigr)=2\delta_{\mu\nu}$. They are four by four in number, $16$, and they are a basis of the operator algebra. Only $W_{tt}=\mathrm I_4$ has a nonzero trace, so the traceless part of the operator space is spanned by the fifteen words of the grid of pairs without the corner.

**The parametrisation is two-to-one at each point.** The pairs $(A,B)$ and $(\lambda A,\lambda^{-1}B)$ give the same operator for every $\lambda\neq0$, and no other pair does:
$$
F_{A,B}=F_{C,D}\iff (C,D)=(\lambda A,\lambda^{-1}B).
$$
The eight complex parameters of the source are therefore seven effective ones, and the scaling orbit is the one-dimensional complex fibre of the parametrisation.

**The two boundary cases.** At $B=\mathrm I_2$ the operator is $L_A$; at $A=\mathrm I_2$ it is $R_B$. In the array the first case has $A$ in the two diagonal blocks and the second has $B^{\mathsf T}$ there.

**The invariants.** The rank is $\operatorname{rank}A\cdot\operatorname{rank}B$, with the values $0,1,2,4$. The trace is $\operatorname{Tr}A\operatorname{Tr}B=4Q_tP_t$, and the determinant is $(\det A\det B)^2=N(\tilde Q)^2N(\tilde P)^2$.

## Composition and the Two Closures

**The composition law.** $L_AR_BL_CR_D=L_{AC}R_{DB}$, because the two middle factors commute and the products associate. In arrays,

$$
(B^{\mathsf T}\otimes A)(D^{\mathsf T}\otimes C)=(BD)^{\mathsf T}\otimes(AC).
$$

**Closed under composition.** The family is closed under composition, contains the identity as $L_{\mathrm I_2}R_{\mathrm I_2}$, and contains the inverse of every invertible member.

**Not closed under addition.** The operator $\mathrm{id}+L_{E_{11}}R_{E_{11}}$ is not of the form $F_{C,D}$.

*Proof.* Its array is $\mathrm I_4+E_{11}\otimes E_{11}$, of rank $4$. Suppose it equals $C^{\mathsf T}\otimes D$. Probes at the four matrix units give
$$
CE_{11}D=2E_{11},\quad CE_{22}D=E_{22},\quad CE_{12}D=E_{12},\quad CE_{21}D=E_{21}.
$$
The first two force $C$ and $D$ diagonal, $C=\operatorname{diag}(\alpha,\alpha)$ and $D=\operatorname{diag}(2/\alpha,1/\alpha)$. The third gives the second row of $D$ equal to $(1/\alpha)e_2^{\mathsf T}$ and the fourth gives its first row equal to $(1/\alpha)e_1^{\mathsf T}$, so $D=\alpha^{-1}\mathrm I_2$, and then $CE_{11}D=\alpha^{-1}CE_{11}=E_{11}$, contradicting $CE_{11}D=2E_{11}$.

**The two closures.** The family is a multiplicative monoid and not an additive one. Its linear span is the whole operator algebra, and the family itself is the cone inside that span.

## The Coefficient Array Has Rank One

**The theorem.** An operator is two-sided exactly when its coefficient array has rank at most one:

$$
M=L_AR_B\iff c(M)=q_Aq_B^{\mathsf T},
$$

where $q_A,q_B$ are the coefficient columns of $A$ and $B$.

*Proof.* The product expands as $L_AR_B=\sum_{\mu\nu}q_{A\mu}q_{B\nu}L_{e_\mu}R_{e_\nu}$, which is the outer product of the two coefficient columns read in the basis $L_{e_\mu}R_{e_\nu}$. The residual of $c(L_AR_B)=q_Aq_B^{\mathsf T}$ on a hundred random pairs is below $10^{-15}$.

**The cone.** The two-sided operators are therefore the decomposable tensors of the coefficient space, that is the Segre cone of $\mathbb{C}^4\otimes\mathbb{C}^4$. Its dimension as an algebraic variety is $4+4-1=7$, which is the seven of the source, and its vertex is the zero operator.

**The contrast with the one-sided families.** A one-sided operator has a coefficient array supported in one row or in one column, and those are the rank-one arrays of the special form $q_Ae_t^{\mathsf T}$ and $e_tq_B^{\mathsf T}$. The cone contains both families and much more, and the three sets have dimensions $4$, $4$ and $7$.

## The Generation Theorem

**The sixteen products.** The operators $L_{e_\mu}R_{e_\nu}$ for the sixteen pairs of units have the arrays $L_\mu R_\nu$, each a signed permutation matrix of $M_4(\mathbb{C})$.

**The theorem.** The sixteen arrays $L_\mu R_\nu$ are linearly independent and span $M_4(\mathbb{C})$:
$$
\operatorname{Span}\{L_AR_B:A,B\in M_2(\mathbb{C})\}=M_4(\mathbb{C}),\qquad \dim_{\mathbb{C}}M_4(\mathbb{C})=16 .
$$

*Proof.* The elementary computation is $E_{ij}E_{mn}E_{kl}=\delta_{jm}\delta_{nk}E_{il}$: for fixed $(i,j,k,l)$ the operator $E_{ij}[\,]E_{kl}$ is the matrix unit of the operator space with a single nonzero entry in the row $(i,l)$ and the column $(j,k)$. The sixteen choices of $(i,j,k,l)$ give the sixteen matrix units of $\operatorname{End}(M_2)$. The change from the matrix units to the coefficient units is the tensor square of an invertible $4\times4$ matrix, hence invertible, and the sixteen products $e_\mu[\,]e_\nu$ are a basis. The stacked matrix of the sixteen arrays has rank sixteen, checked numerically.

**The count.** Every operator is a sum of at most sixteen two-sided operators, because it is a combination of the sixteen basis products and each basis product is one two-sided operator. The bound is far from sharp at this size: the length of an operator is an integer between one and four, as [Operator Chirality on the Biquaternion Algebra in $M_2(\mathbb{C})$](operator-chirality-on-the-biquaternion-algebra-in-m2c.html) shows, and four is attained by the transpose.

**The parameters and the operators.** Eight complex parameters, seven effective ones, describe one point of the cone, and the cone spans sixteen complex dimensions. The parametrisation is bilinear and not linear, and the count is not a contradiction.

## The Ladder $1,4,7,16$

**The chain.** The scalars, the one-sided families, their sum and the whole operator space form

$$
\mathbb{C}\cdot\mathrm I_4\ \subset\ \operatorname{End}_L\ \subset\ \operatorname{End}_L+\operatorname{End}_R\ \subset\ M_4(\mathbb{C}),
\qquad
1<4<7<16 .
$$

**The three inclusions are proper.** The scalars are $\lambda\mathrm I_4=L_{\lambda\mathrm I_2}R_{\mathrm I_2}$. The left family has dimension four because $A\mapsto\mathrm I_2\otimes A$ is injective. The sum has dimension $4+4-1=7$ because the intersection is the scalars. The last inclusion is proper because $L_{E_{12}}R_{E_{21}}$ is not one-sided.

**The two sevens.** The sum is a seven-dimensional subspace and the cone is a seven-dimensional variety, and they are different objects: the sum is linear and is not closed under composition, the cone is closed under composition and is not linear.

**The dimension of the cone.** It is $8-1=7$, the number of parameters minus the scaling orbit, which is the dimension of the Segre variety $\mathbb{P}^3\times\mathbb{P}^3$ plus one.

## The Plain Adjoint

**The theorem.** For the plain form $\langle X,Y\rangle=\tfrac12\operatorname{tr}(XY)$,

$$
\bigl(L_AR_B\bigr)^{\approx}=L_BR_A .
$$

*Proof.* $\tfrac12\operatorname{tr}(AXBY)=\tfrac12\operatorname{tr}(XBYA)$ by cyclicity. In arrays the adjoint is $\sigma(M)=FM^{\mathsf T}F$, and $\sigma(B^{\mathsf T}\otimes A)=F(B\otimes A^{\mathsf T})F=A^{\mathsf T}\otimes B$, which is the array of $L_BR_A$. The residual on a hundred random pairs is below $2\cdot10^{-15}$.

**The swap.** The adjoint exchanges the two parameters and conjugates neither. It is the two-sided form of $(L_A)^{\approx}=R_A$ and $(R_B)^{\approx}=L_B$.

**The involution.** The adjoint is an involution, and it reverses a composition: $(F_{A,B}F_{C,D})^{\approx}=F_{D,C}^{\approx}F_{B,A}^{\approx}$.

**The self-adjoint pairs.** For $A\neq0$,

$$
\bigl(L_AR_B\bigr)^{\approx}=L_AR_B\iff B=\lambda A\ \text{for some }\lambda .
$$

*Proof.* Self-adjointness is $AXB=BXA$ for all $X$. On the matrix units it reads $A_{ik}B_{lj}=B_{ik}A_{lj}$. Choose $(k_0,i_0)$ with $A_{k_0i_0}\neq0$ and put $\lambda=B_{k_0i_0}/A_{k_0i_0}$; then $B=\lambda A$. Conversely $B=\lambda A$ makes the two sides equal for every $X$.

**The anti-self-adjoint sector is trivial.** No nonzero two-sided operator is anti-self-adjoint. The probe gives $B_{ik}A_{lj}=-A_{ik}B_{lj}$, which forces $B=\mu A$; substituting back gives $2\mu AXA=0$ for all $X$, hence $\mu=0$ and $B=0$.

**The reading.** The plain form has a self-adjoint sector and no antisymmetric one among the nonzero members. The reason is the symmetry of the swap: proportional pairs are symmetric, and the only antisymmetric scalar is zero.

## Isometries and Multiplicative Members

**The isometries.** The operator $F_{A,B}$ preserves the plain form exactly when $BA=\pm\mathrm I_2$, that is $B=\pm A^{-1}$, and then $F_{A,B}=\pm\operatorname{Ad}_A$.

*Proof.* An isometry of a non-degenerate form is injective, so both matrices are invertible, and its inverse is its adjoint, so $F_{A,B}F_{B,A}=\mathrm{id}$. By the composition law this is $F_{AB,BA}$, and $F_{C,C}=\mathrm{id}$ exactly when $C=\pm\mathrm I_2$. The identity $\langle\operatorname{Ad}_AX,\operatorname{Ad}_AY\rangle=\langle X,Y\rangle$ was checked on sixty invertible matrices with relative residual better than $10^{-13}$.

**The group.** The isometries inside the family are the two cosets $\pm\operatorname{Ad}_A$ with $A$ invertible. The inner automorphism depends on $A$ only through its class in $\mathrm{GL}_2(\mathbb{C})/\mathbb{C}^{\times}$, so the group is

$$
\{\pm\operatorname{Ad}_A\}\cong\bigl(\mathrm{GL}_2(\mathbb{C})/\mathbb{C}^{\times}\bigr)\times\{\pm1\},
$$

of complex dimension three. It is not all of $O_4(\mathbb{C})$, which has dimension six.

**The multiplicative members.** A nonzero $F_{A,B}$ is multiplicative exactly when $AB=\mathrm I_2$, that is $B=A^{-1}$, and then it is $\operatorname{Ad}_A$.

*Proof.* Multiplicativity is $AX\,BA\,Y\!B=AXY\!B$ for all $X,Y$, that is $AX(BA-\mathrm I_2)Y\!B=0$. With $A$ and $B$ nonzero this forces $BA=\mathrm I_2$, by testing on the matrix units.

**The partial law.** If $BA=\mu\mathrm I_2$ the operator multiplies products by $\mu$: $F(X)F(Y)=\mu F(XY)$. The scalar is the proportionality of the pair and not a norm of the element.

**Multiplicative and isometric.** Such an operator is $\operatorname{Ad}_A$ without the minus, because the multiplicative criterion excludes $\mu=-1$.

**No pin group.** The quadratic form $\mathfrak{Q}(X)=\tfrac12\operatorname{tr}(X^2)$ of the plain form is not multiplicative, so no level set of it is a group, and the isometry group of the family is only the three-dimensional $\{\pm\operatorname{Ad}_A\}$. The pin group of the quadratic space lives in the Clifford algebra and is not contained in the family. In the display this is the statement that the level set $\{X:\operatorname{tr}(X^2)=\pm2\}$ is not closed under multiplication, while the group $\{\pm\operatorname{Ad}_A\}$ is.

## Where $n=2$ Differs

**The size of the ambient space.** At $n=2$ the ambient space is $M_4(\mathbb{C})$, of complex dimension sixteen, and the cone of two-sided operators has dimension seven. At order $n$ the ambient space is $M_{n^2}(\mathbb{C})$, of dimension $n^4$, and the cone has dimension $2n^2-1$, so the gap is $n^4-2n^2+1$.

**The coefficient array.** The criterion "two-sided exactly when the coefficient array has rank at most one" holds at every order. At $n=2$ the array is $4\times4$ and a single product has rank $0$ or $1$.

**The one difference of substance.** At $n=2$ four products reach every operator, so the length is at most four, while the generation bound is sixteen. At order $n$ the length bound is $n^2$ and the transpose needs $n$ products. The number four is the value at $n=2$ of a bound that grows.

**Nothing else differs.** The composition, the failure of addition, the generation theorem, the adjoint swap, the self-adjoint criterion, the isometry criterion and the multiplicative criterion hold at every order with the same proofs.

## Summary

The two-sided operator $F_{A,B}(X)=AXB$ has the array $B^{\mathsf T}\otimes A$, and the pair is defined up to $(\lambda A,\lambda^{-1}B)$. The composition is $L_AR_BL_CR_D=L_{AC}R_{DB}$, the family is a monoid and not a subspace, and $\mathrm{id}+L_{E_{11}}R_{E_{11}}$ is a sum of two members that is not a member.

The coefficient array of a two-sided operator has rank one, $c(L_AR_B)=q_Aq_B^{\mathsf T}$, so the cone is the Segre cone of the coefficient space, of dimension seven. The sixteen products $L_{e_\mu}R_{e_\nu}$ are a basis of the sixteen-dimensional operator space, and the ladder of dimensions is $1,4,7,16$.

The plain adjoint exchanges the parameters: $(L_AR_B)^{\approx}=L_BR_A$. The self-adjoint products are the pairs with $B=\lambda A$, and no nonzero product is anti-self-adjoint. The isometries of the plain form are $\pm\operatorname{Ad}_A$, a group of complex dimension three, and the multiplicative members are $\operatorname{Ad}_A$ alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F_{A,B}(X)=AXB$ | the two-sided operator |
| $B^{\mathsf T}\otimes A$ | its array |
| $q_A,q_B$ | the coefficient columns of $A$ and $B$ |
| $c(M)$ | the coefficient array in the basis $L_{e_\mu}R_{e_\nu}$ |
| $\approx$ | the adjoint for the plain form $\tfrac12\operatorname{tr}(XY)$ |
| $\operatorname{Ad}_A(X)=AXA^{-1}$ | the inner automorphism |
| $\mathfrak{Q}(X)=\tfrac12\operatorname{tr}(X^2)$ | the quadratic form of the plain form |

## Further Reading

- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the source cone, the generation theorem and the isometry group.
- [Operators Acting on One Side in $M_2(\mathbb{C})$](operators-acting-on-one-side-in-m2c.html), for the two families and their intersection.
- [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), for the cone read as a Segre variety.
- [The Length of an Endomorphism of the Biquaternion Algebra: Four Two-Sided Products in $M_2(\mathbb{C})$](the-length-of-an-endomorphism-of-the-biquaternion-algebra-in-m2c.html), for the minimum number of products.
- [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html), for the two-sided arrays in the display.
