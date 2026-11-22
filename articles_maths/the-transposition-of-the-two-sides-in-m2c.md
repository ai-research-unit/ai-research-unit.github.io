# __The Transposition of the Two Sides in $M_2(\mathbb{C})$__

## Introduction

**The question.** The algebra carries an involution $\natural$ that fixes the scalar part and negates the vector part. Conjugating an operator by that involution exchanges the two sides, and the price of the exchange is a moved parameter: a left multiplication becomes a right multiplication by $\natural$ of its parameter. This article asks what the involution is as a map of matrices, what the conjugation is as an operation on arrays, and what the moved parameter costs.

**Why it is the same statement.** This is the in-depth matrix reading of [The Transposition of the Two Sides](the-transposition-of-the-two-sides.html). The display carries the $\mathbb{C}$-linear involution $\natural$ to the adjugate $A\mapsto\operatorname{adj}A=\sigma_2A^{\mathsf T}\sigma_2$, and it carries the two identities and the pair of the source to the two matrix identities of §*The First Identity* and §*The Second Identity* below. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The involution is the adjugate, $A\mapsto\operatorname{tr}(A)\mathrm I_2-A$, a $\mathbb{C}$-linear involution and an anti-automorphism, and it is *not* the Hermitian adjoint; the three conjugations $\natural$, $c$ and $*$ of the corpus are distinguished. The first identity $\natural L_A\natural=R_{\natural(A)}$ holds as the matrix identity $\Phi L_A\Phi=R_{\operatorname{adj}A}$ with $\Phi(A)=\operatorname{adj}A$. The second identity is the same with the sides exchanged. The single involution $K(X)=\Phi X\Phi$ is an automorphism of the operator algebra with $\pm1$ eigenspaces of dimensions ten and six, and the fixed operators are those whose coefficient array is symmetric on the three vector pairs and antisymmetric on the three scalar-vector pairs. The four rewriting rules and the eight pairings of a family, a conjugation and a parameter are tabulated. The exchange forces reversal: a bijection that carries every $L_A$ to $R_{\Theta(A)}$ reverses products, and the class of such bijections is exactly $\Theta(A)=CA^{\mathsf T}C^{-1}$. The three exchange-like operations of the display are compared.

**What the article does not do.** It does not treat the adjoint pair with respect to the Frobenius form, which is [Adjoint Pair of $L$ and $R$ Operators in $M_2(\mathbb{C})$](adjoint-pair-of-l-and-r-operators-in-m2c.html); it does not treat the Hermitian and anti-Hermitian sectors, which is [The Hermitian Pair of Operators Acting on One Side in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-one-side-in-m2c.html); and it does not classify the involutions of the algebra, which is [Classification of the Structures of the Operators of the Biquaternion Algebra in $M_2(\mathbb{C})$](classification-of-the-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html).

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, with trace $2Q_t$ and determinant $N(\tilde Q)=Q_t^2+Q_x^2+Q_y^2+Q_z^2$. The carrier is read in the Peirce frame, so that $L_A=\mathrm I_2\otimes A$ and $R_B=B^{\mathsf T}\otimes\mathrm I_2$. Any $4\times4$ array printed here is the axis-free array and not the Pauli array: the axis-free family is the unique representative, among the $96$ signed-permutation bases, whose sixteen operator arrays are signed permutations, so its entries are the multiplication table read aloud and every identity checked in it is an integer check ([$M_4(\mathbb{C})$ Axis-Free Representation : Operators](m4c-axis-free-representation-operators.html)). The Pauli and gamma arrays are a translation and are refused as primary, because one entry of one of their matrices is diagonal by privilege, which puts a spatial direction into the notation; the privilege is canonical and fixes no invariant.

**The dictionary, stated once.** The involution $\natural$ of the source is $\mathbb{C}$-linear: it leaves the four coefficients untouched and negates the three vector coefficients. Its matrix is the **adjugate**,
$$
\natural(A)=\operatorname{adj}A=\sigma_2A^{\mathsf T}\sigma_2=\operatorname{tr}(A)\mathrm I_2-A ,
$$
and *not* the Hermitian adjoint $A^{\dagger}=\bar A^{\mathsf T}$. The Hermitian adjoint is the matrix of the star conjugation $\tilde Q^{*}$, the composition of $\natural$ with the entrywise conjugation of the coefficients. The two differ on a general element and coincide on the Hermitian and anti-Hermitian sectors, where they are both equal to $\pm A$. The three conjugations are tabulated in §*The Three Conjugations*, and the residual of $\mathsf M_2(\tilde Q^{\natural})=\operatorname{adj}A$ on a hundred random elements is below $2\cdot10^{-15}$.

**Boundaries.** The two families are [Operators Acting on One Side in $M_2(\mathbb{C})$](operators-acting-on-one-side-in-m2c.html). The two-sided operators are [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html). The Hermitian pair is [The Hermitian Pair of Operators Acting on One Side in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-one-side-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html).

**Letters.** The involution on matrices is $\Phi(A)=\operatorname{adj}A$. The three conjugations are $\natural$ (the adjugate), $c$ (the congruence $\sigma_2\bar A\sigma_2$ of the entrywise conjugate) and $*$ (the Hermitian adjoint $A^{\dagger}$). The conjugation of operators by $\Phi$ is $K(X)=\Phi X\Phi$.

## The Two Families

**The arrays.** In the Peirce frame the two one-sided operators are the Kronecker products

$$
L_A=\mathrm I_2\otimes A,\qquad R_B=B^{\mathsf T}\otimes\mathrm I_2,
$$

each four-dimensional inside $M_4(\mathbb{C})$, commuting, meeting in the scalars and summing to seven dimensions. The parameter is read at the unit: $L_A(\mathrm I_2)=A=R_A(\mathrm I_2)$, so a parameter written in a display is written uniquely.

**The two laws.** $L_AL_C=L_{AC}$ and $R_BR_D=R_{DB}$. The first family is a copy of the algebra and the second a copy of the opposite algebra, and the difference between the two laws is the only place where the noncommutativity of the display is visible in the operator algebra.

**The question of this article.** An operation that exchanges the two families must move a left multiplication to a right one. There are three such operations in the display — the conjugation by $\natural$, the plain bilinear adjoint and the exchange $\sigma$ — and they charge different prices. The article separates them.

## The Three Conjugations

**The involution.** The quaternion conjugation of the source is, in the display,

$$
\Phi(A)=\operatorname{adj}A=\operatorname{tr}(A)\mathrm I_2-A
=\begin{pmatrix}a_{22}&-a_{12}\\-a_{21}&a_{11}\end{pmatrix},
$$

the adjugate. In the coefficient basis it is the sign change $(Q_t,Q_x,Q_y,Q_z)\mapsto(Q_t,-Q_x,-Q_y,-Q_z)$; that is, the matrix of $\Phi$ in the basis $\mathrm I_2,\sigma_1,\sigma_2,\sigma_3$ is $\operatorname{diag}(1,-1,-1,-1)$.

**The two properties.** $\Phi$ is an involution and it reverses products:

$$
\Phi(\Phi(A))=A,\qquad \Phi(AB)=\Phi(B)\Phi(A).
$$

*Proof.* The first is Cayley–Hamilton: $\Phi(\Phi(A))=\operatorname{tr}(\Phi(A))\mathrm I_2-\Phi(A)$, and $\operatorname{tr}(\operatorname{adj}A)=\operatorname{tr}A$ for a $2\times2$ matrix, so the expression returns $A$. The second is the multiplicativity of the determinant and the adjugate, $\operatorname{adj}(AB)=\operatorname{adj}B\operatorname{adj}A$, together with $\operatorname{adj}(\lambda A)=\lambda\operatorname{adj}A$.

**The three conjugations.** The corpus uses three involutions of the display, and they are three different maps:

| conjugation | matrix | on the coefficients |
|---|---|---|
| $\natural$ | $\operatorname{adj}A=\sigma_2A^{\mathsf T}\sigma_2$ | $(Q_t,Q_x,Q_y,Q_z)\mapsto(Q_t,-Q_x,-Q_y,-Q_z)$ |
| $c$ | $\sigma_2\bar A\sigma_2$ | entrywise conjugation of the four coefficients |
| $*$ | $A^{\dagger}=\bar A^{\mathsf T}$ | the two together |

The first is $\mathbb{C}$-linear and is the involution of the transposition; the second is anti-linear and is the matrix of the entrywise conjugate of the element; the third is anti-linear and is the Hermitian adjoint. The compositions satisfy $(A^{c})^{\natural}=\overline{A}^{\mathsf T}$ and $(A^{c})^{*}=\bar A^{\dagger}$, as in the display articles of the group.

**The warning.** The transposition of the two sides uses $\natural$ and not $*$. The confusion is natural, because both are involutions and both are anti-automorphisms, and it is fatal for one formula: $\natural(A)=A$ is the condition $\operatorname{adj}A=A$, which forces $A=\tfrac12\operatorname{tr}(A)\mathrm I_2$ and therefore fixes exactly the line of scalars, whereas $A^{\dagger}=A$ is the four-real-dimensional Hermitian space. The two fixed spaces have different dimensions and different meanings, and the transposition is the first.

**The star and the sectors.** The Hermitian sector $\{A:A^{\dagger}=A\}$ is the informational sector of the corpus and the anti-Hermitian sector $\{A:A^{\dagger}=-A\}$ is the material one. The involution $\natural$ fixes the scalars and negates the traceless part, so its fixed space is the line of scalars and its negated space is the three-dimensional traceless part. The two are related by $A^{\dagger}=\sigma_2\operatorname{adj}(\bar A)\sigma_2$: the Hermitian adjoint is the adjugate of the entrywise conjugate, transported by the fixed congruence.

## The First Identity

**The statement.** For every $A$,

$$
\Phi\,L_A\,\Phi=R_{\Phi(A)},
$$

where the composite means: conjugate the input by $\Phi$, multiply on the left by $A$, conjugate the result by $\Phi$.

**The proof.** For every $Y$,

$$
\bigl(\Phi L_A\Phi\bigr)(Y)=\Phi\bigl(A\,\Phi(Y)\bigr)=\Phi(\Phi(Y))\,\Phi(A)=Y\,\Phi(A)=R_{\Phi(A)}(Y),
$$

using the reversal property and then the involution property. The residual on a hundred random elements is below $6\cdot10^{-15}$.

**The reading.** The parameter is conjugated and crosses from the left of the input to its right. The crossing is the reversal, and the conjugation of the parameter is its price. Nothing else is used: not the size of the matrix, not a basis, not the choice of involution beyond its being an involution and an anti-automorphism.

**The unit check.** At $Y=\mathrm I_2$ the composite gives $\Phi(A\,\Phi(\mathrm I_2))=\Phi(A)$, and the right multiplication gives $\mathrm I_2\Phi(A)=\Phi(A)$. The two agree, and the unit is the probe that the source uses.

## The Second Identity

**The statement.**

$$
\Phi\,R_B\,\Phi=L_{\Phi(B)} .
$$

**The proof.** For every $Y$,

$$
\bigl(\Phi R_B\Phi\bigr)(Y)=\Phi\bigl(\Phi(Y)\,B\bigr)=\Phi(B)\,\Phi(\Phi(Y))=\Phi(B)\,Y=L_{\Phi(B)}(Y).
$$

This time the parameter stood on the right and crosses to the left, and it arrives conjugated. The residual on a hundred random elements is below $6\cdot10^{-15}$.

**The two proofs are one.** The first identity and the second are the same computation with the two factors of the product written in the opposite order. The whole difference between the two families is that order, and the reversal of $\Phi$ is what moves a parameter across it.

## The Symmetric Pair

**The pair.** Solving each identity for the family gives the form in which the pair is used:

$$
L_A=\Phi\,R_{\Phi(A)}\,\Phi,\qquad\qquad R_A=\Phi\,L_{\Phi(A)}\,\Phi .
$$

*Proof.* Apply the second identity to $\Phi(A)$: $\Phi R_{\Phi(A)}\Phi=L_{\Phi(\Phi(A))}=L_A$. The other display is the first identity applied to $\Phi(A)$.

**The corollary is the working form.** The identities say what conjugation does to a family; the pair says that each family is the conjugate of the other, with no conjugation left outstanding. An equation written in one family can be rewritten in the other by conjugating both sides, and the pair is the substitution that does it.

## The Single Involution on the Operator Space

**The definition.** Put $K(X)=\Phi X\Phi$ for an operator $X\in M_4(\mathbb{C})$.

**The properties.** $K$ is an involution of the operator algebra and an automorphism of it:

$$
K^2=\mathrm{id},\qquad K(XY)=K(X)K(Y).
$$

The first is $\Phi^2=\mathrm{id}$. The second holds because $\Phi(XY)=\Phi(Y)\Phi(X)$ twice: $K(XY)=\Phi XY\Phi=(\Phi X\Phi)(\Phi Y\Phi)$. Two reversals cancel, so the conjugation of an anti-automorphism is an automorphism.

**The orbits.** The orbits of $K$ are the pairs $\{L_A,R_{\Phi(A)}\}$ and $\{R_B,L_{\Phi(B)}\}$. A one-sided operator is fixed exactly when $R_{\Phi(A)}=L_A$, that is when the two families meet, that is when $A$ is a scalar. Elsewhere the orbit has two elements, one in each family.

**The two eigenspaces.** The involution $K$ splits the operator space:

$$
M_4(\mathbb{C})=\operatorname{Fix}(K)\oplus\operatorname{Neg}(K),
\qquad
\dim\operatorname{Fix}(K)=10,\quad\dim\operatorname{Neg}(K)=6 .
$$

The eigenvalues of $\Phi$ are $+1$ once and $-1$ three times, so those of $K$ are the products $\pm1$ with multiplicities $1+9=10$ and $6$.

**The fixed operators.** On the coefficient array $K$ acts by
$$
c(K(X))_{ab}=\varepsilon_a\varepsilon_b\,c(X)_{ba},
$$
with $\varepsilon_t=1$ and $\varepsilon_x=\varepsilon_y=\varepsilon_z=-1$: a transposition of the two indices followed by the sign. An operator is fixed exactly when its array is symmetric on the three pairs of vector indices, $c_{xy}=c_{yx}$ and cyclically, and antisymmetric on the three pairs joining the scalar index to a vector index, $c_{tx}=-c_{xt}$. The diagonal entries are free. The count is $4+3+3=10$. The negated space is the complementary six-dimensional space of the reversed conditions.

**The two involutions compared.** The swap $\sigma$ of the slots and the conjugation $K$ are both involutions of $M_4(\mathbb{C})$ with eigenspaces of dimensions ten and six. They are different maps: $\sigma$ transposes the coefficient array, and $K$ transposes it and then multiplies entrywise by the sign $\varepsilon_a\varepsilon_b$. They commute, and their product is the entrywise sign involution, whose fixed space is thirteen-dimensional.

## The Rewriting Rules

**The rules.** The pair converts one family into the other, and a composite is converted factor by factor because $K$ preserves products. The rules are four lines.

| the operator | rewritten with the other family |
|---|---|
| $R_B$ | $\Phi\,L_{\Phi(B)}\,\Phi$ |
| $L_A$ | $\Phi\,R_{\Phi(A)}\,\Phi$ |
| $\Phi\,R_B\,\Phi$ | $L_{\Phi(B)}$ |
| $\Phi\,L_A\,\Phi$ | $R_{\Phi(A)}$ |

The first two rows are the pair, and the last two are the identities, which are the same content read the other way: a conjugated one-sided operator *is* a one-sided operator of the other family, with no conjugation left over.

**A couple.** For a product of one operator from each family, the first row gives

$$
L_AR_B=L_A\,\Phi\,L_{\Phi(B)}\,\Phi ,
$$

an expression in the left family alone, with the parameter $\Phi(B)$ and two conjugations inserted where the right multiplication stood. Read the other way, the same product is a product of right multiplications only. The price of the move is the conjugation of the parameters and the two copies of $\Phi$ between the factors.

**The right law follows from the left law.** As a consistency check, derive $R_BR_D=R_{DB}$ from the pair:

$$
R_BR_D=\Phi L_{\Phi(B)}\Phi\,\Phi L_{\Phi(D)}\Phi=\Phi L_{\Phi(B)\Phi(D)}\Phi=\Phi L_{\Phi(DB)}\Phi=R_{DB},
$$

using $\Phi(B)\Phi(D)=\Phi(DB)$, which is the reversal property on two elements. The two laws of the two families are one law seen on the two orbits of $K$.

**Equations.** Because $K$ is an involution it is injective, so conjugating both sides of an equation gives an equivalent equation; because it preserves products it acts factor by factor; and because it exchanges the families it writes the result in the other family. An equation written mostly with right multiplications becomes one written mostly with left multiplications, and the four rules are the whole of the operation.

## The Pairings That Look Alike

**The eight displays.** A pairing of a family, a conjugation and a parameter has eight forms. Four are true and four are false, and the rule that separates them is that the parameter written inside must be the image of the parameter written outside.

| display | verdict |
|---|---|
| $L_A=\Phi R_{\Phi(A)}\Phi$ | true |
| $R_A=\Phi L_{\Phi(A)}\Phi$ | true |
| $\Phi R_A\Phi=L_{\Phi(A)}$ | true |
| $\Phi L_A\Phi=R_{\Phi(A)}$ | true |
| $L_A=\Phi R_A\Phi$ | false unless $\Phi(A)=A$, that is unless $A$ is a scalar |
| $R_A=\Phi L_A\Phi$ | false for the same reason |
| $\Phi R_A\Phi=L_A$ | false for the same reason |
| $\Phi L_A\Phi=R_A$ | false for the same reason |

**The failure is exact.** For a non-scalar $A$ the difference between the true and the false displays is the difference between $\Phi(A)$ and $A$, which is $\operatorname{tr}(A)\mathrm I_2-2A$ and does not vanish. There is no element at which all four pairs agree except the scalars.

**Why a conjugation is needed.** A mapping of the operator algebra that carries every $L_A$ to $R_A$ would have to be additive and would have to satisfy $L_{A+C}\mapsto R_{A+C}$, which is consistent; but it would also have to turn the product $L_AL_C=L_{AC}$ into $R_AR_C=R_{CA}$, and the two orders disagree. No multiplicative map of that kind exists. The conjugation is not decoration: it is what repairs the order, and the repair costs the image of the parameter.

## Why the Exchange Is Reversal

**An arbitrary anti-automorphism.** Let $\Theta$ be a bijection with $\Theta(XY)=\Theta(Y)\Theta(X)$. Then for every $Y$,

$$
\bigl(\Theta L_A\Theta^{-1}\bigr)(Y)
=\Theta\bigl(A\,\Theta^{-1}(Y)\bigr)
=\Theta(\Theta^{-1}(Y))\,\Theta(A)=Y\,\Theta(A)=R_{\Theta(A)}(Y).
$$

**An arbitrary automorphism.** Let $\Sigma$ preserve products. Then

$$
\bigl(\Sigma L_A\Sigma^{-1}\bigr)(Y)=\Sigma\bigl(A\,\Sigma^{-1}(Y)\bigr)=\Sigma(A)\,\Sigma(\Sigma^{-1}(Y))=\Sigma(A)\,Y=L_{\Sigma(A)}(Y).
$$

**The contrast.** In the first computation the two factors change places, so the parameter ends on the right and the operator becomes a right multiplication. In the second they keep their places, and the operator remains a left multiplication. The exchange of the sides is exactly the reversal of the two factors, and nothing else can produce it.

**The proposition.** Let $\Theta$ be a bijection with $\Theta L_A\Theta^{-1}=R_{\Theta(A)}$ for every $A$. Then $\Theta$ reverses products.

*Proof.* Let $Y$ be arbitrary and put $X=\Theta(Y)$. Evaluating the hypothesis at $X$,
$$
\Theta(AY)=\Theta L_A\Theta^{-1}(X)=R_{\Theta(A)}(X)=X\,\Theta(A)=\Theta(Y)\Theta(A),
$$
which is the reversal.

**The class.** The bijections transposing the two families are exactly the anti-automorphisms of the display, and these are exactly the maps

$$
\Theta(A)=C\,A^{\mathsf T}\,C^{-1},\qquad C\in\mathrm{GL}_2(\mathbb{C}).
$$

The map $\natural$ is the member $C=\sigma_2$. The automorphisms of the display are the inner maps $A\mapsto CAC^{-1}$, and none of them transposes the families, by the second computation. The class is therefore one orbit under the inner action, and the involution $\natural$ is one representative of it.

**The consequence for the table.** A bijection that exchanges the families carries the parameter to its image, by the first computation, and it must reverse products, by the proposition. So no bijection exchanges the families and leaves the parameter in place. The false rows of the table above are not merely unproved; they describe a map that cannot exist.

## The Sense of the Name

**Three operations that look alike.** The display carries three operations that move a parameter or a side, and they are different:

| operation | on $L_A$ | on the parameter | inner on $\operatorname{End}$? |
|---|---|---|---|
| the conjugation $K$ | $R_{\Phi(A)}$ | moved by $\natural$ | yes |
| the plain bilinear adjoint | $R_A$ | kept | no |
| the Hermitian adjoint | $L_{A^{\dagger}}$ | kept, conjugated | no, and no exchange |

**The plain bilinear adjoint.** With the form $\langle X,Y\rangle=\tfrac12\operatorname{tr}(XY)$ on the carrier, the adjoint of $L_A$ is $R_A$, because

$$
\tfrac12\operatorname{tr}(AXY)=\tfrac12\operatorname{tr}(XYA).
$$

On the operator space this is the map $\sigma(X)=F X^{\mathsf T}F$ of [Operators Acting on One Side in $M_2(\mathbb{C})$](operators-acting-on-one-side-in-m2c.html): transposition of the array together with the flip. It exchanges the families and keeps the parameter, and it is not a conjugation by a matrix.

**The Hermitian adjoint.** With the Frobenius form on operators, the adjoint of $L_A$ is $L_{A^{\dagger}}$, because

$$
\operatorname{Tr}\bigl((AX)^{\dagger}Y\bigr)=\operatorname{Tr}\bigl(X^{\dagger}A^{\dagger}Y\bigr).
$$

It does not exchange the families at all: it is the map of [Adjoint Pair of $L$ and $R$ Operators in $M_2(\mathbb{C})$](adjoint-pair-of-l-and-r-operators-in-m2c.html), and its conjugation of the parameter is the Hermitian adjoint and not $\natural$.

**The conjugation.** The map $K$ exchanges the families, moves the parameter by $\natural$ and is inner on the operator algebra. It is the only one of the three that is an automorphism of $\operatorname{End}(M_2)$; the other two are not, one being anti-multiplicative and the other being a transpose.

**The name.** The source calls the pair a transposition of the two sides, and the name is justified by the plain bilinear adjoint, which is a genuine transpose and which exchanges the sides. The conjugation is the same exchange with the parameter moved, and the two are reconciled by $\Phi$: the conjugated operator and the plain adjoint differ by the conjugation of the parameter.

## Where $n=2$ Differs

**The adjugate is linear.** At $n=2$ the adjugate is $A\mapsto\operatorname{tr}(A)\mathrm I_2-A$, a linear map of the matrix, and the involution $\natural$ is therefore a linear map of the four coefficients, namely the sign change of the three vector coefficients. At order $n$ the adjugate is homogeneous of degree $n-1$ and is not linear, so the involution is no longer a linear map of the coefficients and the coefficient-array formulae of §*The Single Involution* have no direct analogue.

**The fixed space.** At every order the involution fixes exactly the scalars, because $\operatorname{adj}A=A$ forces $A=\lambda\mathrm I$. Here the fixed space of $\natural$ on the carrier is one complex-dimensional and the negated space three-dimensional.

**The operator involution.** The space of operators is sixteen-dimensional, and $K$ splits it into ten and six. At order $n$ the split is into $n^4$ dimensions with the two parts counted by the symmetry conditions of the coefficient array; here ten and six.

**Nothing else differs.** The two identities, the pair, the rewriting rules, the proposition and the class of anti-automorphisms are statements about an algebra of matrices over a field, and they hold at every order with the same proofs. The matrix $\sigma_2$ is replaced by any invertible $C$.

## Summary

The involution $\natural$ of the source is the adjugate in the display, $\Phi(A)=\operatorname{adj}A=\operatorname{tr}(A)\mathrm I_2-A=\sigma_2A^{\mathsf T}\sigma_2$, a $\mathbb{C}$-linear involution and an anti-automorphism. It is not the Hermitian adjoint; the Hermitian adjoint is the star conjugation, and the two agree only on the Hermitian and anti-Hermitian sectors.

The two identities are $\Phi L_A\Phi=R_{\Phi(A)}$ and $\Phi R_B\Phi=L_{\Phi(B)}$, and they hold because the parameter crosses the other factor and the reversal of $\Phi$ carries it across. The symmetric pair $L_A=\Phi R_{\Phi(A)}\Phi$ and $R_A=\Phi L_{\Phi(A)}\Phi$ is the working form, and the four rewriting rules are the pair read forwards and backwards.

The single involution $K(X)=\Phi X\Phi$ is an automorphism of the operator algebra; on the coefficient array it transposes the two indices and multiplies by $\varepsilon_a\varepsilon_b$, and its eigenspaces have dimensions ten and six. The exchange forces reversal: the bijections that transpose the families are exactly the anti-automorphisms $A\mapsto CA^{\mathsf T}C^{-1}$, and no automorphism transposes them. Of the three exchange-like operations of the display, the conjugation is the only automorphism, the plain bilinear adjoint is the genuine transpose, and the Hermitian adjoint does not exchange the sides at all.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\natural$, $\Phi(A)=\operatorname{adj}A$ | the quaternion conjugation, the adjugate |
| $c(A)=\sigma_2\bar A\sigma_2$ | the congruence of the entrywise conjugate |
| $A^{\dagger}=\bar A^{\mathsf T}$ | the Hermitian adjoint |
| $K(X)=\Phi X\Phi$ | the conjugation of operators |
| $\varepsilon=(\varepsilon_t,\varepsilon_x,\varepsilon_y,\varepsilon_z)=(1,-1,-1,-1)$ | the signs of $\natural$ |
| $L_A=\mathrm I_2\otimes A$, $R_B=B^{\mathsf T}\otimes\mathrm I_2$ | the two one-sided arrays |
| $\sigma(X)=FX^{\mathsf T}F$ | the plain bilinear adjoint |
| $F$ | the flip of the two tensor factors |

## Further Reading

- [The Transposition of the Two Sides](the-transposition-of-the-two-sides.html), for the source identities, the pair and the eight pairings.
- [Operators Acting on One Side in $M_2(\mathbb{C})$](operators-acting-on-one-side-in-m2c.html), for the two families and the exchange $\sigma$.
- [Adjoint Pair of $L$ and $R$ Operators in $M_2(\mathbb{C})$](adjoint-pair-of-l-and-r-operators-in-m2c.html), for the Hermitian adjoint of an operator, which does not exchange the sides.
- [The Hermitian Pair of Operators Acting on One Side in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-one-side-in-m2c.html), for the Hermitian and anti-Hermitian sectors.
- [Operator Chirality on the Biquaternion Algebra in $M_2(\mathbb{C})$](operator-chirality-on-the-biquaternion-algebra-in-m2c.html), for the slot label and the two four-dimensional images.
- [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html), for the display and the three conjugations.
