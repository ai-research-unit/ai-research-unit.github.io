
# __The Left and Right Multiplications of the Biquaternion Sesqualgebra__

## Introduction

Every element of the sesqualgebra $(\mathbb{B},\star)$ of *Introduction to the General Plain Sesqualgebra of Biquaternions* gives two operators on the underlying space, the **left multiplication** $L_{\tilde A}(\tilde X)=\tilde A\star\tilde X$ and the **right multiplication** $R_{\tilde A}(\tilde X)=\tilde X\star\tilde A$. The multiplication is $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$, so on the coordinates

$$
L_{\tilde A}(\tilde X)=\tilde A\tilde X^{*}, \qquad R_{\tilde A}(\tilde X)=\tilde X\tilde A^{*} .
$$

The first operator carries the involution in the variable and is conjugate-linear; the second carries it in the parameter and is linear; and the two parities are opposite, because the second scalar rule reads a scalar through the conjugation in the second slot. This is the operator-level form of the two scalar rules, and it is the whole difference from the bilinear products of the space.

The consequence is an asymmetry between the two families. The left multiplications do **not** compose inside themselves: the composite $L_{\tilde A}L_{\tilde B}$ has two conjugations and is therefore $\mathbb{C}$-linear, so it is the ordinary two-sided multiplication $\tilde X\mapsto\tilde A\tilde X\tilde B^{*}$ and not a left multiplication, and the left family is not closed under composition and has no identity. The right multiplications, by contrast, compose, $R_{\tilde A}R_{\tilde B}=R_{\tilde A\tilde B}$, and the family contains $R_{e_0}=\mathrm{id}$; the two mixed composites close it up, $L_{\tilde A}R_{\tilde B}=L_{\tilde A\tilde B}$ returning to the left family and $R_{\tilde A}L_{\tilde B}$ producing the sandwich of *The Sesquilinear Sandwich on the Biquaternions*. The two families together therefore generate a monoid of four kinds of operator, and the left family alone is not a monoid. The two bilinear multiplications of $\mathbb{B}$ behave differently: their left multiplications do compose, and the regular representation is available there.

The subject is the operator theory of the biquaternion sesqualgebra, read from the general article *The Left and Right Multiplication Operators of a Sesqualgebra*, whose parity theorem, regular maps and obstruction to a linear representation are quoted. The ternary operator forms are *The Ternary Product as an Operator* and *The Adjoint of the Ternary Product*; the two-sided operator produced by the left compositions is *The Sesquilinear Sandwich on the Biquaternions*; and the comparison with the bilinear readings is *Comparison Between the Four Biquaternion Products*.

The setting is that of *Introduction to the General Plain Sesqualgebra of Biquaternions*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the unit, ${}^{*}$ the conjugate-linear involution with $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ and $\varepsilon=(1,-1,-1,-1)$, and the multiplication $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$. The scalar and vector parts are written $\tilde Q=Q_0e_0+\mathbf Q$, and the two halves of the involution are the subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ of *Hermitian and Skew-Hermitian Elements*, where the ordinary product $\tilde P\tilde Q$ makes $\mathbb{M}_+$ a Jordan algebra, by *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

## The Two Operators

### The Definition

**Definition.** For $\tilde A\in\mathbb{B}$ the **left multiplication** and the **right multiplication** of the sesquilinear multiplication are the maps

$$
L_{\tilde A}(\tilde X)=\tilde A\star\tilde X=\tilde A\tilde X^{*}, \qquad R_{\tilde A}(\tilde X)=\tilde X\star\tilde A=\tilde X\tilde A^{*} .
$$

Both are additive in $\tilde X$, since the multiplication is additive in each variable, and both are determined by $\tilde A$. The definition is the one of *The Left and Right Multiplication Operators of a Sesqualgebra*, §*The Two Operators*, read on $\mathbb{B}$ with the standard example $\star$.

**Remark.** The operators are written with the ordinary product on the right, so that the involution is visible: $L_{\tilde A}$ is the two-sided multiplication by $\tilde A$ composed with the involution, $L_{\tilde A}=T_{\tilde A,e_0}\circ{}^{*}$, and $R_{\tilde A}$ is the transpose of the same, $R_{\tilde A}=T_{e_0,\tilde A^{*}}$. The two-sided multiplication $T_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X\tilde Q$ is the linear operator of *The Sesquilinear Sandwich on the Biquaternions*; it is not itself a left or a right multiplication unless one of its parameters is the unit.

### The Two Parities

**Proposition (the parities).** For every $\tilde A$ the left multiplication $L_{\tilde A}$ is conjugate-linear and the right multiplication $R_{\tilde A}$ is linear:

$$
L_{\tilde A}(\lambda\tilde X)=\overline{\lambda}\,L_{\tilde A}(\tilde X), \qquad R_{\tilde A}(\lambda\tilde X)=\lambda\,R_{\tilde A}(\tilde X), \qquad \lambda\in\mathbb{C} .
$$

Consequently $L_{\tilde A}$ is $\mathbb{R}$-linear and lies in the space of the conjugate-linear operators, while $R_{\tilde A}$ is $\mathbb{C}$-linear.

**Proof.** This is the parity theorem of *The Left and Right Multiplication Operators of a Sesqualgebra*, §*The Two Parities*, with $\varsigma$ the complex conjugation, read on $\mathbb{B}$. In coordinates, $L_{\tilde A}(\lambda\tilde X)=\tilde A(\lambda\tilde X)^{*}=\tilde A\overline{\lambda}\tilde X^{*}=\overline{\lambda}L_{\tilde A}(\tilde X)$ by the conjugate-linearity of ${}^{*}$, and $R_{\tilde A}(\lambda\tilde X)=(\lambda\tilde X)\tilde A^{*}=\lambda R_{\tilde A}(\tilde X)$. $\square$

**Remark.** The two families have opposite parities, and this is the operator statement of the two scalar rules. Over $\mathbb{C}$ no single space of $\mathbb{C}$-linear endomorphisms contains both families: a conjugate-linear and a linear map can agree only when they are both zero at every point where the scalars act, which forces the vanishing of the operator. The common home of the two families is the space of the $\mathbb{R}$-linear endomorphisms of the eight-dimensional real space $\mathbb{B}$.

**Proposition (the operators on the basis).** The two operators on the basis elements are

$$
L_{e_0}={}^{*}, \qquad L_{e_k}=(\text{the ordinary left multiplication by }e_k)\text{ composed with the conjugation,}
$$

which is the content of $L_{\tilde A}(\tilde X)=\tilde A\tilde X^{*}$; in particular, at the unit and at a vector element,

$$
L_{e_\mu}(\tilde X)=e_\mu\tilde X^{*}, \qquad R_{e_\mu}(\tilde X)=\tilde X e_\mu^{*}, \qquad e_\mu^{*}=\varepsilon_\mu e_\mu .
$$

**Proof.** Substituting $\tilde A=e_\mu$ in the definition and using $e_\mu^{*}=\varepsilon_\mu e_\mu$ from the multiplication table of *Introduction to the General Plain Sesqualgebra of Biquaternions* gives the two displays. $\square$

### The Parameter Maps

**Proposition (the parameter maps).** The assignment $\tilde A\mapsto L_{\tilde A}$ is $\mathbb{C}$-linear, and the assignment $\tilde A\mapsto R_{\tilde A}$ is conjugate-linear:

$$
L_{\lambda\tilde A}=\lambda L_{\tilde A}, \qquad R_{\lambda\tilde A}=\overline{\lambda}R_{\tilde A}, \qquad \lambda\in\mathbb{C} .
$$

**Proof.** $L_{\lambda\tilde A}(\tilde X)=(\lambda\tilde A)\star\tilde X=\lambda L_{\tilde A}(\tilde X)$ by the first scalar rule, and $R_{\lambda\tilde A}(\tilde X)=\tilde X\star(\lambda\tilde A)=\overline{\lambda}R_{\tilde A}(\tilde X)$ by the second; these are the two displays of *The Left and Right Multiplication Operators of a Sesqualgebra*, §*The Two Operators*. $\square$

**Remark.** The parities are exchanged between the family and its parameter: the left family is linear in its parameter and its values are conjugate-linear, the right family is conjugate-linear in its parameter and its values are linear. The product of the two parities is the same on the two sides, which is why the two families carry the same information through opposite routes.

### The Two Special Values

**Proposition.** With the unit $e_0$ of the algebra, which is a right unit and not a left unit of the multiplication, the two operators are the two elementary operators

$$
L_{e_0}={}^{*}, \qquad R_{e_0}=\mathrm{id},
$$

the involution and the identity.

**Proof.** $L_{e_0}(\tilde X)=e_0\star\tilde X=\tilde X^{*}$, and $R_{e_0}(\tilde X)=\tilde X\star e_0=\tilde X$ by the right unit of *Introduction to the General Plain Sesqualgebra of Biquaternions*, §*The Right Unit*. $\square$

**Remark.** The unit therefore gives the two extreme operators: the involution on the left side and the identity on the right. The identity of the composition is a right multiplication and not a left one, which is the operator form of the one-sided unit and the first hint that the two families are not symmetric.

## The Composition

### The Left Family Does Not Close

**Theorem (the composite of two left multiplications).** For all $\tilde A,\tilde B$,

$$
L_{\tilde A}L_{\tilde B}=T_{\tilde A,\tilde B^{*}} ,
$$

the ordinary two-sided multiplication with the parameters $\tilde A$ and $\tilde B^{*}$. A nonzero such composite is $\mathbb{C}$-linear, so it is not a left multiplication; the left family is therefore not closed under composition, contains no identity, and forms no monoid.

**Proof.** $L_{\tilde A}L_{\tilde B}(\tilde X)=L_{\tilde A}(\tilde B\tilde X^{*})=\tilde A(\tilde B\tilde X^{*})^{*}=\tilde A\tilde X\tilde B^{*}=T_{\tilde A,\tilde B^{*}}(\tilde X)$, using $(uv)^{*}=v^{*}u^{*}$. The composite is $\mathbb{C}$-linear, as the composition of two conjugate-linear maps; a nonzero left multiplication is conjugate-linear, so the two can agree only if the composite vanishes, that is only if $\tilde A=0$ or $\tilde B=0$. The identity, being $\mathbb{C}$-linear, is not a left multiplication either. $\square$

**Remark.** The obstruction is the general one of *The Left and Right Multiplication Operators of a Sesqualgebra*, §*The Standard Example*: the composition law $L_{\tilde A}L_{\tilde B}=L_{\tilde A\star\tilde B}$ would require the product to be associative, and the collapse theorem of *Sesqualgebras* forbids that here, so the composite leaves the family. The residue is the two-sided multiplication $T_{\tilde A,\tilde B^{*}}$, which is the object of the sandwich article; the two compositions and the involution generate the whole operator theory of the multiplication.

### The Right Family Closes

**Theorem (the composite of two right multiplications).** For all $\tilde A,\tilde B$,

$$
R_{\tilde A}R_{\tilde B}=R_{\tilde A\tilde B} .
$$

So the right multiplications are closed under composition, they contain the identity $R_{e_0}$, and they form a monoid anti-isomorphic to the multiplicative monoid $(\mathbb{B},\cdot)$ of the algebra under $\tilde A\mapsto R_{\tilde A}$.

**Proof.** $R_{\tilde A}R_{\tilde B}(\tilde X)=R_{\tilde A}(\tilde X\tilde B^{*})=(\tilde X\tilde B^{*})\tilde A^{*}=\tilde X(\tilde A\tilde B)^{*}=R_{\tilde A\tilde B}(\tilde X)$. The identity is $R_{e_0}$, and the map $\tilde A\mapsto R_{\tilde A}$ reverses products, hence embeds the opposite monoid; its image is the whole right family. $\square$

**Remark.** The asymmetry is the exact content of the two parities: a composite of two linear maps is linear, so the right family closes, while a composite of two conjugate-linear maps is linear, so the left family cannot. The general composition laws of *The Left and Right Multiplication Operators of a Sesqualgebra*, written $R_aR_b=T_{1,(ab)^{*}}$, agree with the theorem because $T_{1,c^{*}}$ is the right multiplication $R_c$.

### The Mixed Composites

Both mixed composites are expressible in the two families and the two-sided operators.

**Theorem (the mixed composites).** For all $\tilde A,\tilde B$,

$$
L_{\tilde A}R_{\tilde B}=L_{\tilde A\tilde B} , \qquad R_{\tilde A}L_{\tilde B}=S_{\tilde B,\tilde A} , \qquad S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*} .
$$

So the composite of a left and a right multiplication, in the order left-of-right, is again a left multiplication; in the other order it is the **sandwich** of *The Sesquilinear Sandwich on the Biquaternions*, below in this group.

**Proof.** $L_{\tilde A}R_{\tilde B}(\tilde X)=\tilde A(\tilde X\tilde B^{*})^{*}=\tilde A\tilde B\tilde X^{*}=L_{\tilde A\tilde B}(\tilde X)$. In the other order, $R_{\tilde A}L_{\tilde B}(\tilde X)=(\tilde B\tilde X^{*})\tilde A^{*}=\tilde B\tilde X^{*}\tilde A^{*}=S_{\tilde B,\tilde A}(\tilde X)$, and the last display is the definition of the sandwich in that article. $\square$

**Remark.** The two mixed composites are not equal, and the difference is the failure of the left and the right multiplications to commute, $L_{\tilde A}R_{\tilde B}\neq R_{\tilde B}L_{\tilde A}$ in general: the first is the left multiplication $L_{\tilde A\tilde B}$, the second is a conjugate-linear sandwich, and the two can agree only when the sandwich happens to be a left multiplication, which the sandwich article shows it is not for general parameters. The witness is the pair $\tilde A=e_1$, $\tilde B=e_2$ at $\tilde X=e_0$: $L_{e_1}R_{e_2}(e_0)=e_1e_2=e_3$ while $R_{e_2}L_{e_1}(e_0)=e_1e_0^{*}e_2^{*}=e_1\cdot e_0\cdot(-e_2)=-e_3$.

### The Monoid Generated by the Two Families

**Theorem (the four kinds of operator).** The set generated by the left and the right multiplications under composition is contained in the union of the four families

$$
\{L_{\tilde A}\}, \qquad \{R_{\tilde A}\}, \qquad \{S_{\tilde P,\tilde Q}\}, \qquad \{T_{\tilde P,\tilde Q}\},
$$

the left multiplications, the right multiplications, the sandwiches and the ordinary two-sided multiplications, and it is a monoid with identity $R_{e_0}=T_{e_0,e_0}=\mathrm{id}$.

**Proof.** The four composition laws of the two preceding theorems give $L_{\tilde A}L_{\tilde B}=T_{\tilde A,\tilde B^{*}}$, $L_{\tilde A}R_{\tilde B}=L_{\tilde A\tilde B}$, $R_{\tilde A}R_{\tilde B}=R_{\tilde A\tilde B}$ and $R_{\tilde A}L_{\tilde B}=S_{\tilde B,\tilde A}$; the composition table of *The Sesquilinear Sandwich on the Biquaternions* closes the remaining cases, and every composite is in one of the four families. The identity belongs to the right family and to the two-sided family. $\square$

**Remark.** The generated monoid is therefore not the union of the two regular representations but a four-parameter family, and the passage from the left family to the two-sided one is the residue of the failure of associativity. The table of the four composition laws is the operator form of the multiplication table of the sesqualgebra, and the two families of the bilinear products, which generate only the first two kinds, are the degenerate case.

## The Two Regular Maps

### The Maps

**Definition.** The **left regular map** and the **right regular map** of the sesqualgebra are

$$
\lambda:\mathbb{B}\longrightarrow \mathrm{End}_{\mathbb{R}}(\mathbb{B}), \quad \lambda(\tilde A)=L_{\tilde A} ; \qquad \rho:\mathbb{B}\longrightarrow \mathrm{End}_{\mathbb{R}}(\mathbb{B}), \quad \rho(\tilde A)=R_{\tilde A} .
$$

They are the two halves of the regular representation of *The Left and Right Multiplication Operators of a Sesqualgebra*, §*The Two Representations*, and they are not the same map.

**Proposition (the multiplicativity).** The map $\lambda$ is $\mathbb{C}$-linear and satisfies $\lambda(\tilde A\star\tilde B)=\lambda(\tilde A)\lambda(\tilde B)$ for all $\tilde A,\tilde B$ if and only if the multiplication is associative; the map $\rho$ is conjugate-linear and satisfies $\rho(\tilde A\star\tilde B)=\rho(\tilde B)\rho(\tilde A)$ for all $\tilde A,\tilde B$ if and only if the multiplication is associative. Neither is multiplicative here.

**Proof.** $\lambda(\tilde A\star\tilde B)(\tilde X)=(\tilde A\star\tilde B)\star\tilde X$ and $\lambda(\tilde A)\lambda(\tilde B)(\tilde X)=\tilde A\star(\tilde B\star\tilde X)$, which agree for every $\tilde X$ exactly when the product is associative; the computation for $\rho$ is the same with the two factors reversed. The product of $\mathbb{B}$ is not associative, by *Introduction to the General Plain Sesqualgebra of Biquaternions*, §*Neither Associative Nor Commutative*. $\square$

**Remark.** The right regular map is nevertheless close to multiplicative, by §*The Right Family Closes*: $\rho(\tilde A\tilde B)=\rho(\tilde A)\rho(\tilde B)$ with the plain product as the parameter, but the multiplication of the sesqualgebra is $\tilde A\star\tilde B=\tilde A\tilde B^{*}$ and not $\tilde A\tilde B$, so the law reads $\rho(\tilde A\star\tilde B)=\rho(\tilde B)\rho(\tilde A)$ and its failure is the conjugate in the parameter of the right family.

### The Obstruction to a Single Linear Representation

**Proposition (the obstruction).** Let $\tilde A\neq0$ and suppose $L_{\tilde A}$ is $\mathbb{C}$-linear. Then $L_{\tilde A}=0$; consequently no nonzero left multiplication is an element of a $\mathbb{C}$-algebra representation of $\mathbb{B}$.

**Proof.** The proposition is the obstruction of *The Left and Right Multiplication Operators of a Sesqualgebra*, §*The Failure of a Single Linear Representation*, with $\varsigma$ the conjugation: $\mathbb{C}$-linearity would give $(\lambda-\overline{\lambda})(\tilde A\star\tilde X)=0$ for every $\lambda$ and $\tilde X$, and choosing a non-real $\lambda$ and an $\tilde X$ with $\tilde A\star\tilde X\neq0$ — which exists since $\tilde A\neq0$ — gives a contradiction. $\square$

**Remark.** The obstruction is why the left multiplication lives among the $\mathbb{R}$-linear operators and not the $\mathbb{C}$-linear ones, and it is the same parity mismatch that the adjoint article repairs with a twisted rule. A sesqualgebra therefore carries two regular representations and no single linear one, and the failure is a property of the multiplication and not of the algebra.

## The Comparison with the Two Bilinear Multiplications

The two bilinear multiplications $\tilde P\tilde Q$ and $\tilde P^{\natural}\tilde Q$ have $\mathbb{C}$-linear left multiplications, and their left families compose. The two sesquilinear products carry the involution in a slot, and of the two families only the right one of the derived product survives composition.

| multiplication | left multiplication | $L_{\tilde A}L_{\tilde B}$ | right multiplication | $R_{\tilde A}R_{\tilde B}$ |
|---|---|---|---|---|
| $\tilde P\tilde Q$ (associative) | $L_{\tilde A}(\tilde X)=\tilde A\tilde X$ | $L_{\tilde A\tilde B}$ | $R_{\tilde A}(\tilde X)=\tilde X\tilde A$ | $R_{\tilde B\tilde A}$ |
| $\tilde P^{\natural}\tilde Q$ | $L_{\tilde A}(\tilde X)=\tilde A^{\natural}\tilde X$ | $L_{\tilde B\tilde A}$ | $R_{\tilde A}(\tilde X)=\tilde X^{\natural}\tilde A$ | not a right multiplication |
| $\tilde P\tilde Q^{*}$ (this article) | $L_{\tilde A}(\tilde X)=\tilde A\tilde X^{*}$ | $T_{\tilde A,\tilde B^{*}}$ | $R_{\tilde A}(\tilde X)=\tilde X\tilde A^{*}$ | $R_{\tilde A\tilde B}$ |

**Remark.** The table is read with *Comparison Between the Four Biquaternion Products*: for the two bilinear products the left family is closed, in the ordinary order for $\tilde P\tilde Q$ and in the reversed order $L_{\tilde A}L_{\tilde B}=L_{\tilde B\tilde A}$ for $\tilde P^{\natural}\tilde Q$ by the anti-multiplicativity of ${}^{\natural}$, and the ordinary right family is closed as well, $R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}$. The right family of the ${}^{\natural}$-product, $R_{\tilde A}(\tilde X)=\tilde X^{\natural}\tilde A$, does not close: its composite is $\tilde X\mapsto\bigl(\tilde X^{\natural}\tilde B\bigr)^{\natural}\tilde A=\tilde B^{\natural}\tilde X\tilde A$, which is not a right multiplication. For the sesquilinear product the left family is open onto the two-sided multiplications while the right family closes, and the closing of the right family is a property of the derived operation and not of a general product. The fourth product, whose first slot carries ${}^{\natural}$, has the same operator shapes as the third in the first column but is not the derived operation, by *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*.

## The Action on the Two Halves

**Proposition.** For the Hermitian subspace $\mathbb{M}_+$ of *Hermitian and Skew-Hermitian Elements*, every left multiplication restricts to the ordinary left multiplication on the Hermitian half,

$$
\tilde X\in\mathbb{M}_+ \implies L_{\tilde A}(\tilde X)=\tilde A\tilde X , \qquad \tilde X\in\mathbb{M}_+ \implies R_{\tilde A}(\tilde X)=\tilde X\tilde A^{*} ,
$$

whatever the parity of the parameter $\tilde A$; and $L_{\tilde A}$ carries $\mathbb{M}_+$ into $\mathbb{M}_+$ exactly when $\tilde A$ is a real scalar, so that the only left multiplications preserving the Hermitian half are the real scalar multiples of the identity.

**Proof.** For $\tilde X\in\mathbb{M}_+$ one has $\tilde X^{*}=\tilde X$, so $L_{\tilde A}(\tilde X)=\tilde A\tilde X^{*}=\tilde A\tilde X$ and $R_{\tilde A}(\tilde X)=\tilde X\tilde A^{*}$, with no sign entering from the parity of $\tilde A$, because the involution acts on the variable and not on the parameter. For the preservation, $L_{\tilde A}$ carries $\mathbb{M}_+$ into $\mathbb{M}_+$ exactly when $\tilde A\tilde X$ is Hermitian for every Hermitian $\tilde X$, that is when $\tilde A\tilde X=\tilde X\tilde A^{*}$ for every Hermitian $\tilde X$; taking $\tilde X=e_0$ gives $\tilde A=\tilde A^{*}$, so $\tilde A$ is Hermitian, and the condition is then that $\tilde A$ commutes with every Hermitian element. The Hermitian elements span $\mathbb{B}$ over $\mathbb{R}$, so $\tilde A$ is central and Hermitian, that is a real scalar. $\square$

**Remark.** On the Hermitian half the left multiplication coincides with the ordinary multiplication, and the derived product and the algebra product agree there; but the Hermitian half is not closed under the ordinary product — it is a Jordan algebra, by *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* — so the coincidence is a coincidence of the two products on the half and not the statement that the half is a subalgebra. The half is carried into itself only by the real scalars, and off the half the difference between the two products is the involution carried by the variable, which is the obstruction of §*The Left Family Does Not Close*. The right multiplication has the same reading with the parameter rather than the variable restricted.

**Remark (the ternary operators).** The operators of the ternary product of *The Ternary Product and the Associator of the Biquaternion Sesqualgebra* are read through the two families: the two outer slots give the linear operators $\tilde Z\mapsto\tilde X\tilde Y^{*}\tilde Z$ and $\tilde X\mapsto\tilde X\tilde Y^{*}\tilde Z$, the ordinary left and right multiplications by $\tilde X\tilde Y^{*}$ and $\tilde Y^{*}\tilde Z$, while the middle slot gives the conjugate-linear operator $\tilde Y\mapsto\tilde X\tilde Y^{*}\tilde Z$, which is the sandwich $S_{\tilde X,\tilde Z^{*}}$ of *The Sesquilinear Sandwich on the Biquaternions*. The quadratic representation is the sandwich $S_{\tilde Z,\tilde Z^{*}}$ evaluated on the middle variable.

## Summary

The left and the right multiplication of the sesquilinear product are $L_{\tilde A}(\tilde X)=\tilde A\tilde X^{*}$ and $R_{\tilde A}(\tilde X)=\tilde X\tilde A^{*}$; the left is conjugate-linear and the right is linear, and in the parameter the left family is linear and the right conjugate-linear. The unit gives the two elementary operators $L_{e_0}={}^{*}$ and $R_{e_0}=\mathrm{id}$.

The left family does not close: $L_{\tilde A}L_{\tilde B}=T_{\tilde A,\tilde B^{*}}$ is the ordinary two-sided multiplication, hence $\mathbb{C}$-linear, hence not a left multiplication, and the left family is neither a monoid nor a representation. The right family does close, $R_{\tilde A}R_{\tilde B}=R_{\tilde A\tilde B}$, and is a monoid anti-isomorphic to the algebra; the mixed composites are $L_{\tilde A}R_{\tilde B}=L_{\tilde A\tilde B}$ and $R_{\tilde A}L_{\tilde B}=S_{\tilde B,\tilde A}$, the sandwich. The two families together generate a monoid of four kinds of operator, the left and the right multiplications, the sandwiches and the two-sided multiplications, and the residue is the operator form of the failure of associativity. The two bilinear multiplications of the space are the case in which the left family closes and the ordinary left regular representation is available.

## Summary of Notation

| symbol | meaning |
|---|---|
| $L_{\tilde A}(\tilde X)=\tilde A\star\tilde X=\tilde A\tilde X^{*}$ | the left multiplication, conjugate-linear |
| $R_{\tilde A}(\tilde X)=\tilde X\star\tilde A=\tilde X\tilde A^{*}$ | the right multiplication, linear |
| $T_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X\tilde Q$ | the ordinary two-sided multiplication, linear |
| $S_{\tilde P,\tilde Q}(\tilde X)=\tilde P\tilde X^{*}\tilde Q^{*}$ | the sesquilinear sandwich, conjugate-linear |
| $L_{\lambda\tilde A}=\lambda L_{\tilde A}$ | the left family is linear in its parameter |
| $R_{\lambda\tilde A}=\overline{\lambda}R_{\tilde A}$ | the right family is conjugate-linear in its parameter |
| $L_{e_0}={}^{*}$, $R_{e_0}=\mathrm{id}$ | the two elementary operators at the unit |
| $L_{\tilde A}L_{\tilde B}=T_{\tilde A,\tilde B^{*}}$ | the composite of two left multiplications |
| $R_{\tilde A}R_{\tilde B}=R_{\tilde A\tilde B}$ | the composite of two right multiplications |
| $L_{\tilde A}R_{\tilde B}=L_{\tilde A\tilde B}$, $R_{\tilde A}L_{\tilde B}=S_{\tilde B,\tilde A}$ | the mixed composites |
| $\lambda,\rho$ | the left and the right regular maps |
| $\mathbb{M}_+,\mathbb{M}_-$ | the Hermitian and the anti-Hermitian halves |

## Further Reading

- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the regular representation and the left and right multiplication of an algebra.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the operators attached to a ring with involution and the conjugate-linear maps they produce.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society Colloquium Publications 37, 1956), for the regular representation of a ring and the module theory attached to it.
- Richard S. Pierce, *Associative Algebras* (Graduate Texts in Mathematics 88, Springer, 1982), for the left and right multiplications of an associative algebra and the criterion that locates associativity in their composition.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the semilinear operators attached to an algebra with an involution.
